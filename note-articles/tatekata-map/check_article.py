"""「建て付け」マップ記事・図解プロンプトの機械チェック。

使い方：python3 note-articles/tatekata-map/check_article.py
原文（note-articles/laws/fudousan-touki-hou.md の本則）と照らして、次を確かめる。
  1. 記事・プロンプトに出てくる「第N条」「第N条のM」が、本則に実在する。
  2. 8つの棚・款の条文範囲が、目次の章立てと一致する。
  3. 記事で述べた文言（一月以内、十万円以下の過料、職権、共同申請、登記の前後、三年以内、二年以内など）が、該当条文にある。
  4. 画像挿入マーカーが図1〜図7の順に並び、プロンプトの図の順と一致する。
  5. 書かないことの語、個人の演習結果、図番の焼き込み、「決定木」などの禁止語が入っていない。
NG が0件なら終了コード0。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LAW = os.path.join(HERE, '..', 'laws', 'fudousan-touki-hou.md')
ARTICLE = os.path.join(HERE, '01-fudousan-touki-hou-tatekata-map.md')
PROMPTS = os.path.join(HERE, '01-zukai-prompts.md')

ng = []


def check(cond, msg):
    if not cond:
        ng.append(msg)


law = open(LAW, encoding='utf-8').read()
body = law[law.index('# 本則'):law.index('## 附則')] if '## 附則' in law else law[law.index('# 本則'):]
toc = law[:law.index('# 本則')]

# 条文の辞書：「12」「76の2」→ 本文
arts = {}
parts = re.split(r'^##### 第(\d+)条(の\d+)?（', body, flags=re.M)
for i in range(1, len(parts), 3):
    arts[parts[i] + (parts[i + 1] or '')] = parts[i + 2].split('）', 1)[-1]
check(len(arts) == 175, f'本則の条数が175でない: {len(arts)}')


def art(n):
    return arts.get(n, '')


article = open(ARTICLE, encoding='utf-8').read()
prompts = open(PROMPTS, encoding='utf-8').read()

# 1. 条文番号の実在
for label, text in (('記事', article), ('プロンプト', prompts)):
    for m in re.finditer(r'第(\d+)条(の\d+)?', text):
        n = m.group(1) + (m.group(2) or '')
        check(n in arts, f'{label}: 第{n}条が本則にない')

# 2. 章立てとの一致
RANGES = [
    ('第一章　総則', 1, 5), ('第二章　登記所及び登記官', 6, 10), ('第三章　登記記録等', 11, 15),
    ('第四章　登記手続', 16, 118), ('第五章　登記事項の証明等', 119, 122), ('第六章　筆界特定', 123, 150),
    ('第七章　雑則', 151, 158), ('第八章　罰則', 159, 164),
    ('第一節　総則', 16, 26), ('第二節　表示に関する登記', 27, 58), ('第三節　権利に関する登記', 59, 118),
    ('第二款　土地の表示に関する登記', 34, 43), ('第三款　建物の表示に関する登記', 44, 58),
    ('第一款　通則', 27, 33),
]
for name, a, b in RANGES:
    ok = re.search(re.escape(name) + r'（第%d条―第%d条）' % (a, b), toc) is not None
    check(ok, f'目次の範囲が合わない: {name} 第{a}条―第{b}条')
# 権利の款
KAN = [('通則', '59', '73'), ('所有権に関する登記', '73の2', '77'), ('用益権に関する登記', '78', '82'),
       ('担保権等に関する登記', '83', '96'), ('信託に関する登記', '97', '104の2'), ('仮登記', '105', '110'),
       ('仮処分に関する登記', '111', '114'), ('官庁又は公署が関与する登記等', '115', '118')]
def jo(n):
    """'73の2' -> '第73条の2'、'59' -> '第59条'"""
    return '第' + (n.replace('の', '条の') if 'の' in n else n + '条')


for name, a, b in KAN:
    check(re.search(r'第.款　' + re.escape(name) + '（%s―%s）' % (jo(a), jo(b)), toc) is not None, f'款の範囲が合わない: {name} {jo(a)}―{jo(b)}')
    label = name if name == '通則' else name
    check(f'| {label} | {jo(a)}〜{jo(b)} |' in article, f'記事の款の表に{name}の範囲がない')
# 記事の棚の表
SHELVES = [('土台', 1, 5), ('担い手', 6, 10), ('記録', 11, 15), ('共通手続', 16, 26), ('表示', 27, 58), ('権利', 59, 118), ('確かめる', 119, 150), ('周辺', 151, 164)]
for name, a, b in SHELVES:
    check(f'| {name} | 第{a}条〜第{b}条 |' in article, f'記事の棚の表に{name}の範囲がない')
    check(f'第{a}条〜第{b}条' in prompts, f'プロンプトに{name}の範囲 第{a}条〜第{b}条 がない')
check(art('1').strip().startswith('この法律は、不動産の表示及び不動産に関する権利を公示するための登記'), '第1条の文言が想定と違う')

# 3. 文言
CLAIMS = [
    ('36', '一月以内'), ('37', '一月以内'), ('42', '一月以内'), ('47', '一月以内'), ('51', '一月以内'), ('57', '一月以内'),
    ('28', '職権ですることができる'), ('60', '共同して'), ('4', '登記の前後'), ('61', '登記原因を証する情報'),
    ('76の2', '三年以内'), ('76の5', '二年以内'),
    ('119', '何人も'), ('123', '筆界の現地における位置を特定'), ('12', '表題部及び権利部に区分'), ('11', '登記官が登記簿に登記事項を記録'),
    ('20', '受付番号の順序'), ('25', '却下しなければならない'), ('21', '登記識別情報'), ('29', '調査'),
    ('16', '嘱託がなければ'), ('19', '受付をしなければならない'), ('74', '申請することができない'), ('39', '以外の者は、申請することができない'),
    ('41', ''), ('56', ''), ('83', ''), ('88', ''), ('54', ''), ('53', ''), ('38', ''), ('105', ''), ('164', '十万円以下の過料'),
]
for n, word in CLAIMS:
    check(word in art(n), f'第{n}条に「{word}」がない')
# 第164条が過料の対象に挙げている条
for n in ('三十六条', '三十七条第一項', '四十二条', '四十七条第一項', '五十一条第一項', '五十七条'):
    check('第' + n in art('164'), f'第164条の対象に第{n}がない')
check('五万円以下の過料' in art('164'), '第164条第2項（第76条の5）の過料の文言がない')
check('一筆の土地又は一個の建物ごと' in art('2'), '第2条に「一筆の土地又は一個の建物ごと」がない')
for n in ('配偶者居住権', '採石権'):
    check(n in art('3'), f'第3条に{n}がない')
check('登記権利者及び登記義務者が共同して' in art('60'), '第60条の文言')

# 4. マーカー
marks = re.findall(r'画像挿入：図(\d)', article)
check(marks == [str(i) for i in range(1, 8)], f'画像挿入マーカーが図1〜図7の順でない: {marks}')
heads = re.findall(r'^## 図(\d)：', prompts, flags=re.M)
check(heads == [str(i) for i in range(1, 8)], f'プロンプトの図が図1〜図7の順でない: {heads}')
check('Instagram用：図1の3:4版' in prompts and '1080x1440' in prompts, 'Instagram用の3:4版がない')
check(prompts.count('NO NUMBERING') >= 8, 'NO NUMBERINGの指示が各プロンプトにない')
check(prompts.count('ILLUSTRATION TEXT RULE') >= 8, 'ILLUSTRATION TEXT RULEが各プロンプトにない')

check('条文の探し方' not in article and '図8' not in article, '削除したはずの条文の探し方・図8が残っている')

# 4b. 見出し画像のプロンプト（note用・Instagram用）
HEADER = os.path.join(HERE, '02-header-image-prompts.md')
hp = open(HEADER, encoding='utf-8').read()
check('1280x670' in hp and '1080x1440' in hp, '見出し画像: note用1280x670とInstagram用1080x1440の両方がない')
check(hp.count('```') == 4, '見出し画像: コードブロックが2つでない')
for s in ('不動産登記法の', '建て付けマップ', '八つの棚で眺める'):
    check(hp.count(s) >= 3, f'見出し画像: 「{s}」が2つのプロンプトに入っていない')
check('全体像と押さえどころ' in hp, '見出し画像: 全体像と押さえどころの語がない')
check('条文を八つの棚に分けると探せる' not in hp and '探せる' not in hp, '見出し画像: 古い副題が残っている')
check('Do NOT draw トリ先生' in hp, '見出し画像: MC1人の指示がない')
check('safe margin of 54px' in hp, 'Instagram用: 安全余白の指示がない')
for line in re.findall(r'^(不動産登記法の|建て付けマップ|八つの棚で眺める[^\n]*|全体像と押さえどころが見えてくる)$', hp, flags=re.M):
    check(not re.search(r'[0-9A-Za-z0-9]', line), f'見出し画像: 画像の文字に数字・英字がある: {line}')
check('見出し画像' in prompts and '02-header-image-prompts.md' in prompts, '図解プロンプトから見出し画像の案内がない')

# 5. 禁止語・個人情報
BAN = ['教材としてまとめたもの', '合格するまで更新', '予備校の解答例と照合', '決定木', '判定木', 'ツリー']
for w in BAN:
    check(w not in article and w not in prompts and w not in hp, f'禁止語「{w}」がある')
for w in ('誤答', '間違えた回数', '自分の回答', '復習中', '要復習'):
    check(w not in article, f'個人の演習結果らしい語「{w}」が記事にある')
# 画像の中に入れる語に図番がない
words_lines = re.findall(r'Words allowed on this poster[^\n]*', prompts)
for w in words_lines:
    check(not re.search(r'「図\d', w), f'画像の語に図番がある: {w[:40]}')
check(len(words_lines) == 8, f'Words allowedの行が8本（図7＋IG）でない: {len(words_lines)}')

# 画像の語が、記事にも出ているか（棚名・款名）
for name, _, _ in SHELVES:
    check(name in article, f'記事に棚名{name}がない')

if ng:
    print('NG', len(ng))
    for m in ng:
        print(' -', m)
    sys.exit(1)
print('NG 0件（条文%d条、図7枚、マーカー7か所）' % len(arts))
