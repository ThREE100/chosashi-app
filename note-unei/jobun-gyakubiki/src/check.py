"""条文の逆引き図鑑の機械チェック。NG 0件にしてから公開する。
- 条文ごとのページが全部あり、一覧のリンク先が存在する
- 各ページの肢の数・年度の数が data/jobun.json と一致する
- 肢の文と正誤が一問一答バンクと一致する（バンクにない令和8年度は記事の引用文）
- 条文の原文が note-articles/laws/ の原文そのまま（取り出した文が原文ファイルに含まれる）
- 個人の演習結果の語が入っていない
"""
import glob, html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BASE))
sys.path.insert(0, HERE)
from build import slug, jn, clean_law  # noqa: E402
sys.path.insert(0, os.path.join(ROOT, 'daily-drill'))
import lawtext  # noqa: E402
ng = []
shi = {s['id']: s for s in json.load(open(os.path.join(BASE, 'data/shi.json'), encoding='utf-8'))}
jobun = json.load(open(os.path.join(BASE, 'data/jobun.json'), encoding='utf-8'))
bank = json.load(open(os.path.join(ROOT, 'tools/drill/data/items.json'), encoding='utf-8'))['items']
bid = {b['id']: b for b in bank}
idx = open(os.path.join(BASE, 'site/index.html'), encoding='utf-8').read()
data = json.loads(re.search(r'const D=(\{.*?\});\n', idx).group(1))
pages = set(os.listdir(os.path.join(BASE, 'site/j')))
if len(pages) != len(jobun):
    ng.append(f'ページ数 {len(pages)} と条文数 {len(jobun)} が違う')
for r in data['rows']:
    if os.path.basename(r['href']) not in pages:
        ng.append('リンク切れ ' + r['href'])
lawsrc = {}
for r in jobun:
    p = os.path.join(BASE, 'site/j', slug(r['law'], r['article']) + '.html')
    t = open(p, encoding='utf-8').read()
    n = t.count('<li><div class="meta">')
    if n != r['shi']:
        ng.append(f"{p} の肢 {n} ≠ {r['shi']}")
    if f"<b>{r['years']}年度・{r['shi']}肢</b>" not in t:
        ng.append(f'{p} の数が合わない')
    txt = clean_law(lawtext.article(r['law'], jn(r['article'])))
    if txt and html.escape(txt) not in t:
        ng.append(f'{p} の原文が取り出した原文と違う')
    for i in r['shi_ids']:
        s = shi[i]
        if s['bank_id']:
            b = bid[s['bank_id']]
            if b['statement'] != s['statement'] or b['truth'] != s['truth']:
                ng.append(f'{i} の文・正誤がバンクと違う')
        if html.escape(s['statement']) not in t:
            ng.append(f'{i} の文が {p} にない')
for w in ['演習', '誤答', '正答率', '回答回数', '解いた回数']:
    for p in glob.glob(os.path.join(BASE, 'site/**/*.html'), recursive=True):
        if w in open(p, encoding='utf-8').read():
            ng.append(f'{p} に「{w}」')
print(f'条文 {len(jobun)}・ページ {len(pages)}：NG {len(ng)}件')
for x in ng[:30]:
    print(' NG', x)
sys.exit(1 if ng else 0)
