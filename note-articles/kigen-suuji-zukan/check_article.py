"""「数字の図鑑」記事・図解プロンプトの機械チェック。

使い方：python3 note-articles/kigen-suuji-zukan/check_article.py
原文（../laws/fudousan-touki-hou.md の本則、fudousan-touki-kisoku-1.md の第28条・第28条の2）と照らして、次を確かめる。
  1. 記事・プロンプトの「第N条」「第N条のM」が、法の本則に実在する（規則は第28条・第28条の2を別に確かめる）。
  2. 記事で述べた数字（一月以内、三年以内、二年以内、過料、罰金、十年・二十年・三十年、保存期間など）が、該当条文にある。
  3. 画像挿入マーカーが図1〜図7の順で、プロンプトの図の順と一致する。note用・Instagram用が各7本ある。
  4. 見出し画像のプロンプトが2種類ある。画像に入れる文字に数字・英字がない（図の語を除く）。
  5. 禁止語・個人の演習結果が入っていない。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LAWS = os.path.join(HERE, '..', 'laws')
ARTICLE = os.path.join(HERE, '01-fudousan-touki-hou-kigen-suuji-zukan.md')
PROMPTS = os.path.join(HERE, '01-zukai-prompts.md')
HEADER = os.path.join(HERE, '02-header-image-prompts.md')

ng = []


def check(cond, msg):
    if not cond:
        ng.append(msg)


law = open(os.path.join(LAWS, 'fudousan-touki-hou.md'), encoding='utf-8').read()
body = law[law.index('# 本則'):law.index('## 附則')]
arts = {}
parts = re.split(r'^##### 第(\d+)条(の\d+)?（', body, flags=re.M)
for i in range(1, len(parts), 3):
    arts[parts[i] + (parts[i + 1] or '')] = parts[i + 2].split('）', 1)[-1]
check(len(arts) == 175, f'本則の条数が175でない: {len(arts)}')

kisoku = open(os.path.join(LAWS, 'fudousan-touki-kisoku-1.md'), encoding='utf-8').read()
k28 = kisoku[kisoku.index('##### 第二十八条 （保存期間）'):kisoku.index('##### 第二十九条')]

article = open(ARTICLE, encoding='utf-8').read()
prompts = open(PROMPTS, encoding='utf-8').read()
header = open(HEADER, encoding='utf-8').read()


def art(n):
    return arts.get(n, '')


# 1. 条文番号の実在（規則の語が近くにある行は法の本則と見なさない）
for label, text in (('記事', article), ('プロンプト', prompts)):
    for line in text.splitlines():
        if '規則' in line:
            continue
        for m in re.finditer(r'第(\d+)条(の\d+)?', line):
            n = m.group(1) + (m.group(2) or '')
            check(n in arts, f'{label}: 第{n}条が本則にない（{line[:30]}…）')
check('不動産登記規則第28条・第28条の2' in article, '記事に規則第28条・第28条の2の記載がない')

# 2. 数字の文言
CLAIMS = [
    ('36', '一月以内'), ('37', '一月以内'), ('42', '一月以内'), ('47', '一月以内'), ('49', '一月以内'), ('51', '一月以内'), ('57', '一月以内'), ('58', '一月以内'),
    ('76の2', '三年以内'), ('76の5', '二年以内'),
    ('164', '十万円以下の過料'), ('164', '五万円以下の過料'),
    ('159', '二年以下の拘禁刑又は百万円以下の罰金'), ('160', '二年以下の拘禁刑又は五十万円以下の罰金'),
    ('161', '二年以下の拘禁刑又は五十万円以下の罰金'), ('162', '三十万円以下の罰金'),
    ('69の2', '契約の日から十年を経過'), ('70', '被担保債権の弁済期から二十年を経過'), ('70の2', '被担保債権の弁済期から三十年を経過'),
    ('70の2', 'その法人の解散の日から三十年を経過'),
    ('71', '一月以内の期間'), ('157', '三日以内'), ('127', '二年とする'), ('10', '四親等内'),
    ('36', 'その所有権の取得の日から'), ('42', 'その滅失の日から'), ('57', 'その滅失の日から'), ('49', '当該合体の日から'),
    ('58', '当該規約の廃止の日から'), ('58', 'その所有権の取得の日から'),
    ('76の2', '遺産の分割の日から三年以内'), ('76の3', '遺産の分割の日から三年以内'),
    ('76の5', 'その変更があった日から'),
]
for n, w in CLAIMS:
    check(w in art(n), f'第{n}条に「{w}」がない')
for n in ('三十六条', '三十七条第一項', '四十二条', '四十七条第一項', '四十九条第一項', '五十一条第一項から第四項まで', '五十七条', '五十八条第六項若しくは第七項', '七十六条の二第一項若しくは第二項', '七十六条の三第四項'):
    check('第' + n in art('164'), f'第164条第1項の対象に第{n}がない')
check('第七十六条の五' in art('164'), '第164条第2項に第七十六条の五がない')
# 第3条の権利は10個
rights = re.findall(r'^- [一二三四五六七八九十]+　', art('3'), flags=re.M)
check(len(rights) == 10, f'第3条の権利が10個でない: {len(rights)}')
# 規則第28条・第28条の2
K = [
    ('登記記録（閉鎖登記記録（閉鎖した登記記録をいう。以下同じ。）を除く。）　永久',),
    ('地図及び地図に準ずる図面（閉鎖したものを含む。）　永久',),
    ('建物所在図（閉鎖したものを含む。）　永久',),
    ('土地に関する閉鎖登記記録　閉鎖した日から五十年間',),
    ('建物に関する閉鎖登記記録　閉鎖した日から三十年間',),
    ('共同担保目録　当該共同担保目録に記録されているすべての事項を抹消した日から十年間',),
    ('信託目録　信託の登記の抹消をした日から二十年間',),
    ('受付帳に記録された情報　受付の年の翌年から十年間（登記識別情報に関する証明の請求に係る受付帳にあっては、受付の年の翌年から一年間）',),
    ('表示に関する登記の申請情報及びその添付情報', '受付の日から三十年間'),
    ('権利に関する登記の申請情報及びその添付情報　受付の日から三十年間',),
    ('職権表示登記等事件簿に記録された情報　立件の日から五年間',),
    ('永久（閉鎖したものにあっては、閉鎖した日から三十年間）',),
    ('地役権図面', '閉鎖した日から三十年間'),
    ('登記識別情報の失効の申出に関する情報　当該申出の受付の日から十年間',),
]
for ks in K:
    check(all(k in k28 for k in ks), f'規則第28条に {ks[0][:20]}… の文言がない')
k28b = kisoku[kisoku.index('##### 第二十八条の二'):kisoku.index('##### 第二十九条')]
for w in ('法定相続情報一覧図つづり込み帳　作成の年の翌年から五年間', '不正登記防止申出書類つづり込み帳、土地価格通知書つづり込み帳、建物価格通知書つづり込み帳及び諸表つづり込み帳　作成の年の翌年から三年間', '登記識別情報通知書交付簿、登記事務日記帳及び登記事項証明書等用紙管理簿　作成の年の翌年から一年間'):
    check(w in k28b, f'規則第28条の2に「{w[:20]}…」がない')

# 3. マーカーと図
marks = re.findall(r'画像挿入：図(\d)', article)
check(marks == [str(i) for i in range(1, 8)], f'画像挿入マーカーが図1〜図7の順でない: {marks}')
heads = re.findall(r'^## 図(\d)：', prompts, flags=re.M)
check(heads == [str(i) for i in range(1, 8)], f'プロンプトの図が図1〜図7の順でない: {heads}')
check(prompts.count('### note用') == 7 and prompts.count('### Instagram用') == 7, 'note用・Instagram用が各7本でない')
check(prompts.count('INSTAGRAM FEED FORMAT') == 7, 'Instagram用の安全余白の指示が7本でない')
check(prompts.count('1080x1350') >= 14, 'Instagram用のサイズ指定が足りない')
check(prompts.count('NO NUMBERING') == 14 and prompts.count('ILLUSTRATION TEXT RULE') == 14, 'NO NUMBERING / ILLUSTRATION TEXT RULE が14本でない')
words_lines = re.findall(r'Words allowed on this poster[^\n]*', prompts)
check(len(words_lines) == 14, f'Words allowedの行が14本でない: {len(words_lines)}')
for a, b in zip(words_lines[0::2], words_lines[1::2]):
    check(a == b, 'note用とInstagram用で画像に入れる語が違う')
for w in words_lines:
    check(not re.search(r'「図\d', w), f'画像の語に図番がある: {w[:40]}')
    check(not re.search(r'[A-Za-z]', w.split(':', 1)[1]), '画像の語に英字がある')

# 4. 見出し画像
check(header.count('```') == 4, '見出し画像: コードブロックが2つでない')
check('1280x670' in header and '1080x1350' in header, '見出し画像: 2つのサイズがない')
for s in ('不動産登記法の', '数字の図鑑', '何の登記か　いつから数えるか', '期限と数字を整理する'):
    check(s in header, f'見出し画像: 「{s}」がない')
check(header.count('Do NOT draw トリ先生') == 2, '見出し画像: MC1人の指示が2本でない')
check('safe margin of 54px' in header, 'Instagram用: 安全余白の指示がない')
for line in re.findall(r'^(不動産登記法の|数字の図鑑|何の登記か　いつから数えるか|期限と数字を整理する)$', header, flags=re.M):
    check(not re.search(r'[0-9A-Za-z]', line), f'見出し画像: 画像の文字に数字・英字がある: {line}')

# 5. 禁止語・個人情報
BAN = ['教材としてまとめたもの', '合格するまで更新', '予備校の解答例と照合', '決定木', '判定木', 'ツリー']
for w in BAN:
    check(w not in article and w not in prompts and w not in header, f'禁止語「{w}」がある')
for w in ('誤答', '間違えた回数', '自分の回答', '復習中', '要復習', '出題頻度'):
    check(w not in article, f'確かめていない主張・個人の演習結果らしい語「{w}」が記事にある')


# 6. Instagramのキャプション案
CAP = os.path.join(HERE, '03-instagram-captions.md')
cap = open(CAP, encoding='utf-8').read()
blocks = re.findall(r'```\n(.*?)```', cap, flags=re.S)
check(len(blocks) == 9, f'キャプションが9本（A＋B-0〜B-7）でない: {len(blocks)}')
for i, b in enumerate(blocks):
    check(len(b) <= 2200, f'キャプション{i}が2200字を超える')
    check(3 <= len(re.findall(r'#\S+', b)) <= 5, f'キャプション{i}のハッシュタグが3〜5個でない')
    check('http' not in b, f'キャプション{i}にURLがある')
    if i:
        check('プロフィールのリンク' in b or i == 1, f'キャプション{i}にプロフィールのリンクへの誘導がない')
    for m in re.finditer(r'第(\d+)条(の\d+)?', b):
        if '規則' in b.split(m.group(0))[0][-12:]:
            continue
        n = m.group(1) + (m.group(2) or '')
        check(n in arts, f'キャプション{i}: 第{n}条が本則にない')
    for w in BAN + ['誤答', '間違えた回数', '出題頻度']:
        check(w not in b, f'キャプション{i}に「{w}」がある')
# キャプションの数字が条文と合う
for n, w in (('36', '一月以内'), ('76の2', '三年以内'), ('76の5', '二年以内'), ('164', '十万円以下'), ('164', '五万円以下'), ('69の2', '十年'), ('70の2', '三十年')):
    check(w in art(n), f'第{n}条に「{w}」がない（キャプションの根拠）')

if ng:
    print('NG', len(ng))
    for m in ng:
        print(' -', m)
    sys.exit(1)
print('NG 0件（条文%d条、図7枚、マーカー7か所、プロンプト14本＋見出し画像2本）' % len(arts))
