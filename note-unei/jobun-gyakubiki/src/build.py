"""条文の逆引き図鑑のWebページ（1枚のHTML）を作る。
入力：data/shi.json・data/jobun.json（extract.py が作る）、note-urls.csv（記事のパス→noteのURL。空欄なら記事名でnote内検索）、
      条文の原文（note-articles/laws/。daily-drill/lawtext.py で取り出す。手で打たない）。
出力：site/index.html（データを埋め込んだ1ファイル。GitHub Pages に置けばそのまま動く）。
"""
import csv, json, os, sys, html, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BASE))
sys.path.insert(0, os.path.join(ROOT, 'daily-drill'))
import lawtext  # noqa: E402

YEARS = ["h17","h18","h19","h20","h21","h22","h23","h24","h25","h26","h27","h28","h29","h30","r1","r2","r3","r4","r5","r6","r7","r8"]
YLAB = [y.upper() if y[0] == 'h' else ('R1' if y == 'r1' else y.upper()) for y in YEARS]
LAW_ORDER = ['不動産登記法', '不動産登記令', '不動産登記規則', '不動産登記事務取扱手続準則', '区分所有法',
             '土地家屋調査士法', '土地家屋調査士法施行規則', '民法']


def note_urls(shi):
    """note-urls.csv を読む。なければ記事の一覧で作る（url は空欄。ユーザーが埋める）。"""
    p = os.path.join(BASE, 'note-urls.csv')
    arts = {}
    for s in shi:
        arts.setdefault(s['path'], s['title'])
    have = {}
    if os.path.exists(p):
        for r in csv.DictReader(open(p, encoding='utf-8')):
            have[r['path']] = r.get('url', '').strip()
    with open(p, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['path', 'title', 'url'])
        for path in sorted(arts):
            w.writerow([path, arts[path], have.get(path, '')])
    out = {}
    for path, title in arts.items():
        u = have.get(path, '')
        if not u:
            core = title.replace('【土地家屋調査士試験】', '').replace('〜', ' ').strip()
            u = 'https://note.com/search?' + urllib.parse.urlencode({'q': core, 'context': 'note'})
            out[path] = {'url': u, 'direct': False}
        else:
            out[path] = {'url': u, 'direct': True}
    return out


SLUG = {'不動産登記法': 'hou', '不動産登記令': 'rei', '不動産登記規則': 'kisoku', '不動産登記事務取扱手続準則': 'junsoku',
        '区分所有法': 'kubun', '土地家屋調査士法': 'chousashi', '土地家屋調査士法施行規則': 'chousashi-kisoku', '民法': 'minpou'}
SHORT = {'不動産登記事務取扱手続準則': '準則', '土地家屋調査士法施行規則': '調査士法施行規則'}
SITE_NAME = '条文の逆引き図鑑'
PERIOD = '平成17年度〜令和8年度'
e = html.escape


def jn(art):
    b, _, sub = art.partition('の')
    return f"第{b}条" + (f"の{sub}" if sub else "")


def slug(law, art):
    return f"{SLUG[law]}-{art.replace('の', '-')}"


def clean_law(text):
    if not text:
        return ''
    lines = text.split('\n')
    if lines and lines[0].startswith('#'):
        lines = lines[1:]
    return '\n'.join(l.replace('  - ', '').rstrip() for l in lines).strip()


def page(title, desc, body, depth):
    css = '../' * depth + 'style.css'
    return f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="stylesheet" href="{css}"></head>
<body><main>{body}</main>
<footer><p>正誤は現行の法令で確かめた結果です（出題当時の公式の正答と違うことがあります）。条文は e-Gov 法令検索などから取得した原文です。</p>
<p>解説の全文はnoteの記事にあります。</p></footer></body></html>
"""


def strip(ys):
    return '<div class="strip" aria-label="出題された年度">' + ''.join(
        f'<span class="cell{" on" if i in ys else ""}" title="{YLAB[i]}">{YLAB[i] if i in ys else ""}</span>'
        for i in range(len(YEARS))) + '</div>'


def lab(s):
    if s.get('kuuran'):
        return '空欄' + s['label']
    return ('肢' + s['label']) if s['label'].isdigit() or s['label'] in '①②③④⑤⑥⑦⑧⑨⑩' else s['label']


def truth_mark(t):
    if t is True:
        return '<span class="tf ok" aria-label="正しい">○</span>'
    if t is False:
        return '<span class="tf ng" aria-label="誤り">×</span>'
    return '<span class="tf un" aria-label="記事で確認">？</span>'


def main():
    shi = json.load(open(os.path.join(BASE, 'data', 'shi.json'), encoding='utf-8'))
    jobun = json.load(open(os.path.join(BASE, 'data', 'jobun.json'), encoding='utf-8'))
    urls = note_urls(shi)
    S = {s['id']: s for s in shi}
    site = os.path.join(BASE, 'site')
    os.makedirs(os.path.join(site, 'j'), exist_ok=True)
    for f in os.listdir(os.path.join(site, 'j')):
        os.remove(os.path.join(site, 'j', f))
    index_rows, missing = [], []
    for r in jobun:
        law, art = r['law'], r['article']
        name = f"{law}{jn(art)}"
        txt = clean_law(lawtext.article(law, jn(art)))
        if not txt:
            missing.append(name)
        ys = [YEARS.index(y) for y in r['year_list']]
        items = sorted((S[i] for i in r['shi_ids']), key=lambda s: (-YEARS.index(s['year']), s['q'], s['label']))
        lis = []
        for s in items:
            u = urls[s['path']]
            lis.append(f"""<li><div class="meta">{e(s['year_ja'])} 第{s['q']}問 {e(lab(s))}</div>
<div class="row">{truth_mark(s['truth'])}<p class="st">{e(s['statement']) or '（記事の問題文を見てください）'}</p></div>
<p class="pt">ポイント：{e(s['heading'])}</p>
<a class="go" href="{e(u['url'])}" rel="noopener">{"解説を読む（note）" if u['direct'] else "noteで記事を探す"}</a></li>""")
        hot = '毎年のように出る' if r['years'] >= 10 else ('くり返し出る' if r['years'] >= 4 else '')
        body = f"""<nav><a href="../index.html">← {SITE_NAME}（条文の一覧）</a></nav>
<h1>{e(law)} {e(jn(art))}</h1>
<p class="lead">{PERIOD}の択一式で、<b>{r['years']}年度・{r['shi']}肢</b>の解説がこの条文を引いています。{e(hot) + '条文です。' if hot else ''}</p>
{strip(ys)}
<details class="law"{' open' if len(txt) < 600 else ''}><summary>条文の原文を読む</summary><pre>{e(txt) if txt else '（今の法令にはない条文です。改正で削られたか、手元の原文の収録範囲の外です。解説記事で確かめてください）'}</pre></details>
<h2>この条文を解説で引いている肢（新しい年度から）</h2>
<ul class="shi">{''.join(lis)}</ul>"""
        title = f"{name}の過去問（{r['years']}年度・{r['shi']}肢）｜土地家屋調査士 {SITE_NAME}"
        desc = f"土地家屋調査士試験の択一式（{PERIOD}）で{name}が問われた{r['shi']}肢を、年度・問・肢と正誤、条文の原文つきで一覧にしました。"
        open(os.path.join(site, 'j', slug(law, art) + '.html'), 'w', encoding='utf-8').write(page(title, desc, body, 1))
        kw = ' '.join(sorted({S[i]['heading'] for i in r['shi_ids']} | {S[i]['topic'] for i in r['shi_ids'] if S[i]['topic']}))
        index_rows.append({'law': law, 's': SHORT.get(law, law), 'a': art, 'ny': r['years'], 'ns': r['shi'],
                           'j': jn(art), 'ys': ys, 'href': 'j/' + slug(law, art) + '.html', 'kw': kw})
    data = {'years': YLAB, 'laws': LAW_ORDER, 'rows': index_rows}
    tpl = open(os.path.join(HERE, 'index_template.html'), encoding='utf-8').read()
    n_cited = sum(1 for s in shi if s['cites'])
    tpl = (tpl.replace('/*DATA*/null', json.dumps(data, ensure_ascii=False, separators=(',', ':')))
              .replace('{{N_Q}}', str(len({s['path'] for s in shi}))).replace('{{N_SHI}}', str(len(shi)))
              .replace('{{N_CITED}}', str(n_cited)).replace('{{N_JOBUN}}', str(len(index_rows)))
              .replace('{{PERIOD}}', PERIOD).replace('{{SITE}}', SITE_NAME))
    open(os.path.join(site, 'index.html'), 'w', encoding='utf-8').write(tpl)
    import shutil
    shutil.copy(os.path.join(HERE, 'style.css'), os.path.join(site, 'style.css'))
    print(f"条文 {len(index_rows)} ページ・条文を拾えた肢 {n_cited}/{len(shi)}、原文が見つからない条文 {len(missing)}", missing[:12])
    print(f"noteのURLが入っている記事 {sum(1 for v in urls.values() if v['direct'])}/{len(urls)}")


if __name__ == '__main__':
    main()
