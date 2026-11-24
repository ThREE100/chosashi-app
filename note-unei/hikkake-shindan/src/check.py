"""ひっかけの型の診断の機械チェック。NG 0件にしてから投稿する。"""
import json, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BASE))
sys.path.insert(0, HERE)
from data import TYPES, QUESTIONS  # noqa: E402
from build import load, TITLE  # noqa: E402
ng = []
rows = load()
art = open(os.path.join(BASE, 'article.md'), encoding='utf-8').read()
tax = json.load(open(os.path.join(ROOT, 'daily-drill/taxonomy.json'), encoding='utf-8'))['traps_morning']
if len(rows) != 10: ng.append('10問ではない')
c = collections.Counter(r['type'] for r in rows)
for t in TYPES:
    if c[t['key']] != 2: ng.append(f"型{t['key']}が2問ではない")
    for k in t['tax']:
        if k not in tax: ng.append(f'分類 {k} が taxonomy.json にない')
if len({(r['q'], r['label']) for r in rows}) != 10: ng.append('同じ肢が重複')
for r in rows:
    if r['status'] != 'verified': ng.append(f"{r['q']}{r['label']} がバンクで確認済みでない")
    if r['statement'] not in art: ng.append(f"{r['q']}{r['label']} の文が記事にない")
    if not r['cites']: ng.append(f"{r['q']}{r['label']} の根拠の条文がない")
nt = sum(r['truth'] for r in rows)
if not 3 <= nt <= 7: ng.append(f'○が{nt}問で偏っている')
ans = ''.join('○' if r['truth'] else '×' for r in rows)
if re.search('○{4}|×{4}', ans): ng.append(f'答えの並び {ans} に同じ記号が4つ続く')
for a, b in zip(rows, rows[1:]):
    if a['type'] == b['type']: ng.append('同じ型の問題が続く')
tbl = re.findall(r'^\| (\d+) \| ([○×]) \|', art, re.M)
if ''.join(x[1] for x in tbl) != ans: ng.append('答えの表がデータと違う')
if not art.startswith('## ' + TITLE) or not TITLE.startswith('【土地家屋調査士試験】'): ng.append('タイトルの形')
for w in ['演習', '誤答', '回答回数', '解いた回数', '正答率', '私は', '僕は']:
    if w in art: ng.append(f'記事に「{w}」（個人の結果・体験は書かない）')
i1 = art.find('### 10問チェック'); i2 = art.find('### 答えと型')
if not 0 < i1 < i2 or '○' in art[i1:i2].replace('「○」', ''): ng.append('答えより前に○×が出ている')
print(f'答え {ans}：NG {len(ng)}件')
for x in ng: print(' NG', x)
sys.exit(1 if ng else 0)
