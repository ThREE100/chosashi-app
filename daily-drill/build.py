"""毎日ドリルのA4印刷用HTMLを out/ に作る。
  out/dayNN-am.html      朝（オリジナル択一1問＋書いて説明）の問題 1ページ
  out/dayNN-am-ans.html  朝の解答（原文の根拠つき）
  out/dayNN-pm.html      夜（記述式：計算または申請書の欄）の問題 1ページ
  out/dayNN-pm-ans.html  夜の解答
  out/index.html         日ごとの一覧
ブラウザで開き、印刷（A4・余白なし）またはタブレットで書き込む。
使い方: python3 daily-drill/build.py"""
import glob
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lawtext import article  # noqa: E402
import figure  # noqa: E402

OUT = os.path.join(HERE, 'out')
E = html.escape
CIRC = ['①', '②', '③', '④', '⑤']

CSS = """
:root{--g:#009775;--ink:#1d2b27;--mute:#5d6b66;--line:#cfd8d4;--soft:#f2f8f6;--warn:#b3261e}
*{box-sizing:border-box}
html{background:#e9eeec}
body{margin:0;font-family:"Noto Sans JP","Hiragino Sans","Yu Gothic",Meiryo,sans-serif;color:var(--ink);font-size:10.5pt;line-height:1.6}
.sheet{width:210mm;min-height:297mm;margin:8mm auto;background:#fff;padding:12mm 14mm;box-shadow:0 1px 6px rgba(0,0,0,.15);position:relative}
.hd{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid var(--g);padding-bottom:2mm;margin-bottom:3mm}
.hd h1{font-size:13pt;margin:0;color:var(--g)}
.hd .meta{font-size:9pt;color:var(--mute)}
h2{font-size:10.5pt;margin:4mm 0 1.5mm;padding-left:2mm;border-left:3px solid var(--g)}
.theme{font-size:9.5pt;color:var(--mute);margin:0 0 2mm}
ol.st{list-style:none;margin:0;padding:0}
ol.st li{display:flex;gap:2mm;margin:1.2mm 0}
ol.st .lb{flex:none;font-weight:700}
.ch{display:flex;flex-wrap:wrap;gap:1mm 6mm;margin:2mm 0;font-size:10pt}
.box{border:1px solid var(--ink);display:inline-block;min-width:16mm;height:7mm;vertical-align:middle;margin-left:2mm}
.lines{background-image:repeating-linear-gradient(#fff 0,#fff 7.4mm,var(--line) 7.4mm,var(--line) 7.9mm);border:1px solid var(--line);}
.pt{width:100%;border-collapse:collapse;margin:1mm 0 2mm;font-size:10pt}
.pt th,.pt td{border:1px solid var(--line);padding:1mm 2.5mm;text-align:left}
.pt th{background:var(--soft);font-weight:500;width:26mm}
.ans{border:1px dashed var(--g);padding:1.5mm 3mm;margin:1.5mm 0;font-size:10pt}
.q{margin:2.5mm 0 1mm;font-weight:500}
.tag{font-size:8.5pt;color:#fff;background:var(--g);padding:0 2mm;border-radius:2mm;margin-right:2mm}
.ok{color:var(--g);font-weight:700}.ng{color:var(--warn);font-weight:700}
blockquote{margin:1mm 0 1mm 0;padding:1mm 3mm;border-left:3px solid var(--line);color:var(--mute);font-size:9.5pt;background:var(--soft)}
.src{font-size:9pt;color:var(--mute)}
.full{white-space:pre-wrap;font-size:9.5pt;border:1px solid var(--line);padding:2mm 3mm;background:var(--soft)}
.chk{margin:0;padding:0;list-style:none;columns:2}
.foot{position:absolute;left:14mm;right:14mm;bottom:7mm;font-size:8pt;color:var(--mute);display:flex;justify-content:space-between}
.clz{border:1px solid var(--line);padding:3mm 4mm;margin:2mm 0}
.cl{margin:0 0 2.2mm;font-size:10.5pt;line-height:1.95}
.blank{display:inline-block;min-width:24mm;border-bottom:1.5px solid var(--ink);text-align:left;font-size:8pt;color:var(--mute);margin:0 1mm;vertical-align:baseline}
.figrow{margin:2mm 0}
.figrow svg.fig{display:block;width:100%;height:auto}
.coord{margin-top:2mm}
.coord table{width:100%;border-collapse:collapse;font-size:10pt}
.coord th,.coord td{border:1px solid var(--line);padding:.9mm 2mm;text-align:right;white-space:nowrap}
.coord th{background:var(--soft);font-weight:500;text-align:center}
.coord td.n{text-align:center;font-weight:700}
.coord p{margin:1.2mm 0 0;font-size:9.5pt;color:var(--mute);line-height:1.5}
code{font-family:"Space Mono",Menlo,monospace;font-size:9.5pt}
@page{size:A4;margin:0}
@media print{html{background:#fff}.sheet{margin:0;box-shadow:none;page-break-after:always;break-after:page;overflow:hidden;height:297mm}.sheet.flow{height:auto;overflow:visible}}
"""


def page(title, body, foot='', flow=False, right='条文は note-articles/laws/ の原文で照合済み'):
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><style>{CSS}</style></head><body><div class="sheet{" flow" if flow else ""}">{body}'
            f'<div class="foot"><span>{E(foot)}</span><span>{E(right)}</span></div></div></body></html>')


def head(day, kind, theme, minutes):
    return (f'<div class="hd"><h1>第{day}日　{kind}</h1><span class="meta">日付：　　月　　日　／　目安 {minutes}分　／　時間：　　分</span></div>'
            f'<p class="theme">{E(theme)}</p>')


def lines(mm):
    return f'<div class="lines" style="height:{mm}mm"></div>'


def quote_block(b):
    return f'<blockquote>{E(b["law"])}{E(_art(b["article"]))}「{E(b["quote"])}」</blockquote>'


def _art(a):
    return a if a.startswith(('第', '別表')) else f'{a}の項'


# ---------- 朝 ----------
CN = ['①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '⑪', '⑫', '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '⑳']


def cloze_html(w, answers=False):
    """空欄補充。問題では下線つきの空欄（番号入り）、解答では答えを太字で埋める。"""
    out = ''
    for ln in w['cloze']:
        parts = re.split(r'\{(\d+)\}', ln)
        h = ''
        for i, seg in enumerate(parts):
            if i % 2 == 0:
                h += E(seg)
            else:
                n = int(seg)
                h += (f'<b class="ok">{E(w["blanks"][n - 1])}</b>' if answers else f'<span class="blank">{CN[n - 1]}</span>')
        out += f'<p class="cl">{h}</p>'
    return f'<div class="clz">{out}</div>'

def am_q(p):
    st = ''.join(f'<li><span class="lb">{s["label"]}</span><span>{E(s["text"])}</span></li>' for s in p['statements'])
    ch = ''.join(f'<span>{CIRC[i]} {"・".join(c)}</span>' for i, c in enumerate(p['choices']))
    body = head(p['day'], '朝：択一1問＋条文の空欄補充', f'択一：{p["theme"]}　／　空欄補充：{p["write"]["theme"]}', 10)
    body += f'<h2>択一（4分）</h2><p>{E(p["stem"])}</p><ol class="st">{st}</ol><div class="ch">{ch}</div>'
    body += '<p>解答：<span class="box"></span></p>'
    w = p['write']
    if 'cloze' in w:
        body += f'<h2>条文の空欄補充（6分）　<span class="src">条文のキーワードを空欄に</span></h2><p>{E(w["prompt"])}</p>{cloze_html(w)}'
    else:
        body += f'<h2>書いて説明（6分）　<span class="src">原文を見ずに、条文の言葉で</span></h2><p>{E(w["prompt"])}</p>{lines(104)}'
    return page(f'第{p["day"]}日 朝 問題', body, f'{p["id"]}')


def am_a(p):
    want = (p['mode'] == '正しい')
    ans = [s['label'] for s in p['statements'] if s['truth'] == want]
    idx = [i for i, c in enumerate(p['choices']) if set(c) == set(ans)][0]
    body = head(p['day'], '朝：解答', f'択一：{p["theme"]}　／　空欄補充：{p["write"]["theme"]}', 10)
    body += f'<div class="ans">正解：<b>{CIRC[idx]}</b>（{"・".join(ans)}）　※問題は「{p["mode"]}もの」を選ぶ</div>'
    for s in p['statements']:
        mark = '<span class="ok">○ 正しい</span>' if s['truth'] else '<span class="ng">× 誤り</span>'
        body += f'<div class="q"><b>{s["label"]}</b>　{mark}　{E(s["note"])}</div>'
        body += ''.join(quote_block(b) for b in s['basis'])
    w = p['write']
    if 'cloze' in w:
        body += '<h2>条文の空欄補充：答え</h2>' + cloze_html(w, answers=True)
        body += '<p class="q">自己採点（合っていれば□にチェック）</p><ul class="chk">' + ''.join(f'<li>□ {CN[i]} {E(x)}</li>' for i, x in enumerate(w['blanks'])) + '</ul>'
    else:
        body += '<h2>書いて説明：模範解答</h2><ul style="margin:0;padding-left:5mm">' + ''.join(f'<li>{E(m)}</li>' for m in w['model']) + '</ul>'
        body += '<p class="q">採点ポイント（言葉が入っていれば○）</p><ul class="chk">' + ''.join(f'<li>□ {E(x)}</li>' for x in w['points']) + '</ul>'
    full = w['basis'][0]
    txt = article(full['law'], full['article']) or ''
    txt = '\n'.join(ln for ln in txt.split('\n') if not ln.startswith('#')).strip()
    body += f'<h2>原文（音読用）　<span class="src">{E(full["law"])}{E(_art(full["article"]))}</span></h2><div class="full">{E(txt)}</div>'
    return page(f'第{p["day"]}日 朝 解答', body, f'{p["id"]} 解答', flow=True)


# ---------- 夜 ----------
def coord_table(p):
    """与えられた点の座標表（求める点は載せない）。図の下に横長で置く。"""
    g = p['given']
    names = {'radial': ['T1', 'T2'], 'area': list('ABCD'), 'foot': ['F', 'H', 'E']}.get(p['type'], list('ABCD'))
    head_ = '<tr><th>点</th>' + ''.join(f'<th>{E(k)}</th>' for k in names) + '</tr>'
    rx = '<tr><th>X（北）</th>' + ''.join(f'<td>{g[k][0]:.2f}</td>' for k in names) + '</tr>'
    ry = '<tr><th>Y（東）</th>' + ''.join(f'<td>{g[k][1]:.2f}</td>' for k in names) + '</tr>'
    extra = ''
    if p['type'] == 'radial':
        for o in g['obs']:
            a = o['angle']
            extra += f'<p><b>点{o["name"]}</b>：後視T2から時計回りに {a[0]}°{a[1]:02d}′{a[2]:02d}″、距離 {o["dist"]:.2f} m</p>'
    if p['type'] == 'parallel':
        extra += f'<p>直線ABに平行で、西側に <b>{g["off"]:.2f} m</b> 離れた直線を使う。</p>'
    return f'<div class="coord"><table>{head_}{rx}{ry}</table>{extra}</div>'


def pm_q(p):
    body = head(p['day'], '夜：記述式ドリル', p['title'], 15)
    if p['kind'] == 'calc':
        intro = {'radial': 'T1に器械を据え、T2を後視して、次の点を観測した。', 'area': '次の4点で囲まれた四角形ABCDの土地（地目は宅地）がある。'}.get(p['type'], '次の点の座標が与えられている。')
        body += f'<h2>問題</h2><p>{E(intro)}座標は、Xが北、Yが東である。答えは、小数第3位を四捨五入して小数第2位まで書く（面積の問題を除く）。</p>'
        body += f'<div class="figrow">{figure.svg(p)}{coord_table(p)}</div>'
        body += '<h2>求めるもの</h2>' + ''.join(f'<p class="q">（{i + 1}）{E(a)}</p><p>X ＝ <span class="box" style="min-width:34mm"></span>　　Y ＝ <span class="box" style="min-width:34mm"></span></p>'
                                                  if p['type'] != 'area' else f'<p class="q">（{i + 1}）{E(a)}</p><p>地積 ＝ <span class="box" style="min-width:34mm"></span> ㎡</p>'
                                                  for i, a in enumerate(p['ask']))
    else:
        sc = ''.join(f'<li>{E(x)}</li>' for x in p['scenario'])
        body += f'<h2>事案</h2><ul style="margin:0;padding-left:5mm">{sc}</ul><h2>答えよ</h2>'
        n = len(p['fields'])
        h = 190 // n if n else 20
        for f in p['fields']:
            body += f'<p class="q">{E(f["q"])}</p>{lines(max(h - 16, 12))}'
    return page(f'第{p["day"]}日 夜 問題', body, p['id'], right='' if p['kind'] == 'calc' else '条文は note-articles/laws/ の原文で照合済み')


def pm_a(p):
    body = head(p['day'], '夜：解答', p['title'], 15)
    if p['kind'] == 'calc':
        g = p['given']
        for i, (a, q) in enumerate(zip(p['answers'], p['ask'])):
            val = f'X ＝ {a[0]}　Y ＝ {a[1]}' if len(a) == 2 else f'{a[0]} ㎡'
            body += f'<div class="ans"><b>（{i + 1}）{E(q)}</b>　→　<b>{E(val)}</b></div>'
        body += f'<h2>図（赤が求めた点）</h2><div class="figrow">{figure.svg(p, reveal=True)}{coord_table(p)}</div>'
        body += '<h2>解き方（複素数モード）</h2><ul style="margin:0;padding-left:5mm">' + ''.join(f'<li><code>{E(s)}</code></li>' for s in p['steps']) + '</ul>'
        body += f'<h2>つまずきポイント</h2><p>{E(p["trap"])}</p>'
        for b in p.get('basis', []):
            body += quote_block(b)
        body += '<h2>できたか</h2><ul class="chk"><li>□ 式が立てられた</li><li>□ 電卓で打てた</li><li>□ 検算した</li><li>□ 制限時間内に終わった</li></ul>'
    else:
        for f in p['fields']:
            body += f'<div class="q">{E(f["q"])}</div><div class="ans">{E(f["answer"])}</div>'
            body += ''.join(quote_block(b) for b in f['basis'])
            if f['note']:
                body += f'<p class="src">{E(f["note"])}</p>'
    return page(f'第{p["day"]}日 夜 解答', body, f'{p["id"]} 解答', flow=True)


def main():
    os.makedirs(OUT, exist_ok=True)
    am = {json.load(open(f, encoding='utf-8'))['day']: json.load(open(f, encoding='utf-8')) for f in glob.glob(os.path.join(HERE, 'morning', 'problems', '*.json'))}
    pm = {json.load(open(f, encoding='utf-8'))['day']: json.load(open(f, encoding='utf-8')) for f in glob.glob(os.path.join(HERE, 'evening', 'problems', '*.json'))}
    rows = ''
    for d in sorted(set(am) | set(pm)):
        links = []
        if d in am:
            for suf, fn, lab in (('', am_q, '朝 問題'), ('-ans', am_a, '朝 解答')):
                n = f'day{d:02d}-am{suf}.html'
                open(os.path.join(OUT, n), 'w', encoding='utf-8').write(fn(am[d]))
                links.append(f'<a href="{n}">{lab}</a>')
        if d in pm:
            for suf, fn, lab in (('', pm_q, '夜 問題'), ('-ans', pm_a, '夜 解答')):
                n = f'day{d:02d}-pm{suf}.html'
                open(os.path.join(OUT, n), 'w', encoding='utf-8').write(fn(pm[d]))
                links.append(f'<a href="{n}">{lab}</a>')
        rows += f'<tr><td>第{d}日</td><td>{E(am[d]["theme"]) if d in am else ""}</td><td>{E(pm[d]["title"]) if d in pm else ""}</td><td>{" ／ ".join(links)}</td></tr>'
    idx = (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>毎日ドリル</title>'
           f'<style>{CSS}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid var(--line);padding:2mm 3mm;text-align:left;font-size:10pt}}a{{color:var(--g)}}</style></head>'
           f'<body><div class="sheet"><div class="hd"><h1>毎日ドリル（朝：択一＋書いて説明／夜：記述式）</h1></div>'
           f'<table><tr><th>日</th><th>朝の論点</th><th>夜の内容</th><th>リンク</th></tr>{rows}</table></div></body></html>')
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(idx)
    print('out/ に', len(os.listdir(OUT)), 'ファイル')


if __name__ == '__main__':
    main()
