"""図解企画6本（01〜06）の機械チェック。python3 note-articles/topics/zukai-kikaku/check_article.py
  1. 記事・プロンプト・キャプションの「第N条」が、不動産登記法の本則に実在する。
  2. 記事の要点（一月以内、ただし書、準用、みなす、表題登記の定義など）が、原文の該当条にある。期限の定めがないと述べた条に「一月以内」がない。
  3. 添付情報の早見図（KZ_03）の○△－が、不動産登記令の別表の原文と合う。
  4. 画像挿入マーカーが、図の数と順に一致する。生成物（図解・見出し・キャプション）がデータと合う。
  5. 見出し画像の文字（英数字なし）、キャプション（2200字以内、タグ3〜5個、URLなし、プロフィールのリンク）、禁止語。
NG が0件なら終了コード0。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'src'))
from data import TOPICS  # noqa: E402

LAWDIR = os.path.join(HERE, '..', '..', 'laws')
ng = []


def check(c, m):
    if not c:
        ng.append(m)


def rd(*p):
    return open(os.path.join(*p), encoding='utf-8').read()


law = rd(LAWDIR, 'fudousan-touki-hou.md')
body = law[law.index('# 本則'):law.index('## 附則')]
parts = re.split(r'^##### 第(\d+)条(の\d+)?（', body, flags=re.M)
arts = {parts[i] + (parts[i + 1] or ''): parts[i + 2] for i in range(1, len(parts), 3)}
check(len(arts) == 175, '本則の条数が175でない: %d' % len(arts))


def art(n):
    return arts.get(n, '')


files = {}
for t in TOPICS:
    files[t['id']] = dict(article=rd(HERE, t['slug'] + '.md'))
article_all = {k: v['article'] for k, v in files.items()}
others = {'zukai-prompts': ''.join(rd(HERE, f) for f in sorted(os.listdir(HERE)) if f.startswith('zukai-prompts-')),
          'header': rd(HERE, 'header-image-prompts.md'), 'captions': rd(HERE, 'instagram-captions.md'),
          'yonkoma': rd(HERE, '06-yonkoma-prompt.md'), 'reel': rd(HERE, '06-reel-storyboard.md')}

# 1. 条文番号の実在
for label, text in list(article_all.items()) + list(others.items()):
    for m in re.finditer(r'第(\d+)条(の\d+)?', text):
        n = m.group(1) + (m.group(2) or '')
        check(n in arts, '%s: 第%s条が本則にない' % (label, n))

# 2. 原文の確認
CLAIMS = [('36', '一月以内'), ('36', '所有権の取得の日'), ('37', '一月以内'), ('42', '一月以内'), ('47', '一月以内'),
          ('51', '一月以内'), ('49', '一月以内'), ('49', '合体の日'), ('57', '一月以内'), ('57', '滅失の日'), ('42', '滅失の日'),
          ('74', '表題部所有者'), ('39', '以外の者は、申請することができない'), ('54', '以外の者は、申請することができない'),
          ('41', '相互に接続していない土地'), ('41', '地目又は地番区域が相互に異なる'), ('56', '合併の登記は、することができない'),
          ('54', '建物の分割の登記'), ('54', '建物の区分の登記'), ('54', '建物の合併の登記'), ('54', '第四十条の規定は'), ('54', '準用する'),
          ('25', 'この限りでない'), ('25', '補正'), ('25', '却下しなければならない'),
          ('16', '法令に別段の定めがある場合を除き'), ('51', '前項の登記事項について変更があった後'),
          ('40', '分筆の登記をする場合'), ('19', '同時にされたものとみなす'), ('29', '調査することができる'),
          ('11', '登記簿に登記事項を記録することによって'), ('18', '電子情報処理組織'), ('18', '申請情報を記載した書面'),
          ('2', '表示に関する登記のうち、当該不動産について表題部に最初にされる登記'), ('2', '一筆の土地又は一個の建物ごと'),
          ('38', '更正の登記'), ('53', '更正の登記'), ('19', '受付をしなければならない'), ('12', '表題部及び権利部に区分')]
for n, w in CLAIMS:
    check(w in art(n), '第%s条に「%s」がない' % (n, w))
# 期限の定めがないと述べた条
for n in ('38', '39', '53', '54', '56', '41', '74'):
    check('一月以内' not in art(n), '第%s条に「一月以内」がある（期限の定めがないと述べている）' % n)
# 第2条の号番号（表題登記は第20号、登記記録は第5号、表題部・権利部は第7・8号）
a2 = art('2')
check(re.search(r'二十　表題登記', a2) is not None, '第2条第20号が表題登記でない')
check(re.search(r'五　登記記録', a2) is not None, '第2条第5号が登記記録でない')
# 第41条の号数（第1号〜第6号）
check(len(re.findall(r'^- [一二三四五六]　', art('41'), flags=re.M)) == 6, '第41条の号が6つでない')

# 調査士法 第3条第1項第1号〜第3号
cj = rd(LAWDIR, 'chousashi-hou.md')
i = cj.index('### 第3条')
c3 = cj[i:i + 900]
check('一　不動産の表示に関する登記について必要な土地又は家屋に関する調査又は測量' in c3, '調査士法第3条第1号の文言')
check('二　不動産の表示に関する登記の申請手続' in c3 and '代理' in c3, '調査士法第3条第2号の文言')
check('三　不動産の表示に関する登記の申請手続' in c3 and '作成' in c3, '調査士法第3条第3号の文言')

# 3. 令別表
bt = rd(LAWDIR, 'fudousan-touki-rei-betsuhyou.md')
sec = {}
for m in re.finditer(r'^#### (\S+)\n(.*?)(?=^#### |^### |\Z)', bt, flags=re.M | re.S):
    sec[m.group(1)] = m.group(2)


def attach(k):
    s = sec[k]
    return s[s.index('**添付情報**'):]


def kinds(k, words):
    a = attach(k)
    return [w in a for w in words]


LAND = ['土地所在図', '地積測量図', 'が所有権を有することを証する情報', '住所を証する']
BLDG = ['建物図面', '各階平面図', 'が所有権を有することを証する情報', '住所を証する']
EXPECT_LAND = {'四': [1, 1, 1, 1], '五': [0, 0, 0, 0], '六': [0, 1, 0, 0], '八': [0, 1, 0, 0]}
for k, e in EXPECT_LAND.items():
    check([int(x) for x in kinds(k, LAND)] == e, '令別表%sの項の添付情報が早見図と合わない: %s' % (k, kinds(k, LAND)))
# 九の項：通常は個別の定めなし（地役権の承役地のときだけ）
check(not any(kinds('九', LAND)), '令別表九の項の添付情報')
check('地役権' in attach('九'), '令別表九の項は地役権の場合だけ添付情報がある')
check('土地の滅失の登記' in sec['十'] and '河川管理者' in sec['十'], '令別表十の項は河川管理者の嘱託の滅失')
EXPECT_BLDG = {'十二': [1, 1, 1, 1], '十三': [1, 1, 1, 1], '十六': [1, 1, 0, 0]}
for k, e in EXPECT_BLDG.items():
    check([int(x) for x in kinds(k, BLDG)] == e, '令別表%sの項の添付情報が早見図と合わない: %s' % (k, kinds(k, BLDG)))
k14 = kinds('十四', BLDG)
check(k14[0] and k14[1] and k14[2] and not k14[3], '令別表十四の項（△△△－）が合わない: %s' % k14)
check('変更後又は更正後の建物図面' in attach('十四') and '床面積が増加するときは' in attach('十四') and '附属建物を新築したときは' in attach('十四'),
      '令別表十四の項の条件')
check('分割後、区分後又は合併後の建物図面及び各階平面図' in attach('十六'), '令別表十六の項')
check('登記' in sec['十七'] and '滅失の登記' in sec['十七'] and '共用部分' in sec['十七'], '令別表十七の項は共用部分の滅失')
check(not any('建物の滅失の登記' in v.split('**申請情報**')[0] and k != '十七' for k, v in sec.items()), '通常の建物の滅失の項が別表にある')
check('個別の定めなし' in sec['五'], '令別表五の項は個別の定めなし')
# 早見図データの記号が上と一致
t3 = [t for t in TOPICS if t['id'] == 'KZ_03'][0]
rows = {}
for f in t3['figs']:
    for m in re.finditer(r'Row 「([^」]+)」 with small tag 「([^」]+)」: 「(.)」 「(.)」 「(.)」 「(.)」', f['body']):
        rows[m.group(1)] = (m.group(2), m.group(3, 4, 5, 6))
SYM = {1: '○', 0: '－'}
exp = {'土地の表題登記': ('令別表四の項', [1, 1, 1, 1]), '地目の変更・更正': ('五の項', [0, 0, 0, 0]),
       '地積の変更・更正': ('六の項', [0, 1, 0, 0]), '分筆': ('八の項', [0, 1, 0, 0]), '合筆': ('九の項', [0, 0, 0, 0]),
       '建物の表題登記': ('令別表十二の項', [1, 1, 1, 1]), '合体による登記等': ('十三の項', [1, 1, 1, 1]),
       '分割・区分・合併': ('十六の項', [1, 1, 0, 0]), '滅失': ('別表に項なし', [0, 0, 0, 0])}
for name, (tag, vals) in exp.items():
    check(name in rows, '早見図に行「%s」がない' % name)
    if name in rows:
        check(rows[name][0] == tag, '早見図の項番「%s」: %s' % (name, rows[name][0]))
        check(rows[name][1] == tuple(SYM[v] for v in vals), '早見図の記号「%s」: %s' % (name, rows[name][1]))
check(rows.get('表題部の変更・更正', ('', ()))[1] == ('△', '△', '△', '－'), '早見図の十四の項の記号')
check(rows.get('表題部の変更・更正', ('', ()))[0] == '十四の項', '早見図の十四の項の項番')

# 4. マーカーと生成物
for t in TOPICS:
    a = files[t['id']]['article']
    marks = re.findall(r'画像挿入：([^*）（]+)', a)
    if t['figs']:
        nums = re.findall(r'画像挿入：図(\d)', a)
        check(nums == [str(i) for i in range(1, len(t['figs']) + 1)], '%s: 画像挿入マーカーが図1〜の順でない: %s' % (t['id'], nums))
    else:
        check(len(marks) == 1 and '四コマ' in marks[0], '%s: 四コマのマーカーが1か所でない: %s' % (t['id'], marks))
    check(a.startswith('## 【土地家屋調査士】'), '%s: 記事のタイトル行' % t['id'])
    for f in t['figs']:
        for w in re.findall(r'「([^」]+)」', f['body']):
            check(not re.search(r'図\d', w), '%s %s: 画像の語に図番がある: %s' % (t['id'], f['key'], w))
    n = t['id'][-2:]
    if t['figs']:
        zp = rd(HERE, 'zukai-prompts-%s.md' % n)
        check(zp.count('Words allowed on this poster') == 2 * len(t['figs']), '%s: Words allowedが図数×2でない' % t['id'])
        check(zp.count('NO NUMBERING') == 2 * len(t['figs']) and zp.count('ILLUSTRATION TEXT RULE') == 2 * len(t['figs']), '%s: NO NUMBERING / ILLUSTRATION TEXT RULE' % t['id'])
        check('1080x1440' in zp and zp.count('INSTAGRAM FEED FORMAT') == len(t['figs']), '%s: Instagram用の指示' % t['id'])
        for f in t['figs']:
            for w in re.findall(r'「([^」]+)」', f['body']):
                check('「%s」' % w in zp, '%s %s: 語「%s」がプロンプトにない' % (t['id'], f['key'], w))
    # 見出し
    h = t['header']
    for k, mx in (('l1', 12), ('l2', 10), ('band', 18), ('sub', 20)):
        check(len(h[k]) <= mx, '%s: 見出し%sが%d字超' % (t['id'], k, mx))
        check(not re.search(r'[A-Za-z0-9０-９Ａ-Ｚａ-ｚ]', h[k]), '%s: 見出し%sに英数字' % (t['id'], k))
    check(h['emph'] in h['l2'], '%s: 強調語がl2にない' % t['id'])
    check(not re.search(r'[぀-ヿ一-鿿]', h['scene_note'] + h['scene_ig']), '%s: 場面は英語で' % t['id'])
    # キャプション
    for name, text in t['captions']:
        check(len(text) <= 2200, '%s %s: 2200字超' % (t['id'], name))
        tags = re.findall(r'#\S+', text)
        check(3 <= len(tags) <= 5, '%s %s: ハッシュタグが3〜5個でない' % (t['id'], name))
        check('http' not in text, '%s %s: URLがある' % (t['id'], name))
        check('プロフィールのリンク' in text, '%s %s: プロフィールのリンクの案内がない' % (t['id'], name))
        for m in re.finditer(r'第(\d+)条(の\d+)?', text):
            check(m.group(1) + (m.group(2) or '') in arts, '%s %s: 第%s条が本則にない' % (t['id'], name, m.group(1)))
hd = others['header']
for t in TOPICS:
    check(t['id'] in hd and t['header']['l2'] in hd, '%s: 見出し画像の生成物にない' % t['id'])
check(hd.count('Do NOT draw トリ先生') == 12, '見出し画像: MC1人の指示が12本（6企画×2）でない: %d' % hd.count('Do NOT draw トリ先生'))
check(hd.count('safe margin of 54px') == 6, '見出し画像: Instagram用の安全余白が6本でない')
check(others['captions'].count('```') == 2 * sum(len(t['captions']) for t in TOPICS), 'キャプションのコードブロック数')

# 四コマ
y = others['yonkoma']
check('1080x1920' in y and y.count('PANEL ') >= 4, '四コマの大きさ・コマ数')
for w in ('第47条', '令別表十二の項', '第19条', '第29条', '第11条', '第74条'):
    check(w in y, '四コマに「%s」がない' % w)
check(y.count('「藍子」') + y.count('藍子') > 0 and 'トリ先生' in y, '四コマの登場人物')

# 5. 禁止語・個人情報
BAN = ['教材としてまとめたもの', '合格するまで更新', '予備校の解答例と照合', '決定木', '判定木', 'ツリー']
for label, text in list(article_all.items()) + list(others.items()):
    for w in BAN:
        check(w not in text, '%s: 禁止語「%s」' % (label, w))
for label, text in article_all.items():
    for w in ('誤答', '間違えた回数', '自分の回答', '復習中', '要復習'):
        check(w not in text, '%s: 個人の演習結果らしい語「%s」' % (label, w))

if ng:
    print('NG', len(ng))
    for m in ng:
        print(' -', m)
    sys.exit(1)
print('NG 0件（条文%d条、企画%d本、図%d枚、キャプション%d本）' % (len(arts), len(TOPICS), sum(len(t['figs']) for t in TOPICS), sum(len(t['captions']) for t in TOPICS)))
