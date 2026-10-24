"""毎日ドリルのA4印刷用HTMLを out/ に作る。
  out/dayNNN-am.html      朝（オリジナル択一1問＋書いて説明）の問題 1ページ
  out/dayNNN-am-ans.html  朝の解答（原文の根拠つき）
  out/dayNNN-pm.html      夜（記述式：計算または申請書の欄）の問題 1ページ
  out/dayNNN-pm-ans.html  夜の解答
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
import draw_forms  # noqa: E402

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
.ex{font-size:8.3pt;line-height:1.44}
.ex h2{font-size:9.5pt;margin:2.2mm 0 1mm}
.ex p{margin:0 0 1.2mm}
.ex ol{margin:0;padding-left:4.6mm}.ex ol li{margin:0 0 1.1mm}
.ans-box{width:100%;border-collapse:collapse;margin:1mm 0 2mm;font-size:10pt}
.ans-box th,.ans-box td{border:1.5px solid var(--ink);padding:1.2mm 2.5mm;text-align:left;height:9mm}
.ans-box th{background:var(--soft);font-weight:500;width:58mm}
.ans-box.c2 th{width:38mm;font-size:8.6pt}
.ans-box td.fill{color:var(--g);font-weight:700;font-size:10.5pt}
.q2{font-size:9pt;line-height:1.5}.q2 h2{font-size:9.8pt;margin:2.4mm 0 1mm}.q2 p{margin:0 0 1.4mm}.q2 ol{margin:0 0 1mm;padding-left:5mm}.q2 ol li{margin:0 0 1.3mm}
.dense .ans-box th,.dense .ans-box td{padding:.3mm 2mm;height:6.4mm;font-size:9pt}.dense .box{height:5.4mm}.dense .q2{font-size:8.3pt;line-height:1.42}.dense .q2 h2{margin:1.6mm 0 .6mm}.dense .q2 li{margin:0 0 .7mm}
.drawwrap{margin:0 0 3mm}.drawwrap svg{display:block;width:182mm;height:auto}
.tg{display:grid;grid-template-columns:1fr 1fr;gap:3mm;margin-top:2mm}
.tg table{width:100%;border-collapse:collapse;font-size:9.2pt}.tg caption{text-align:left;font-weight:700;font-size:9pt;padding:.3mm 0}
.tg th,.tg td{border:1px solid var(--line);padding:.7mm 1.8mm;text-align:center;white-space:nowrap}.tg th{background:var(--soft);font-weight:500}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:4mm;align-items:start}
.reg{width:100%;border-collapse:collapse;margin:0 0 1.6mm;font-size:8.4pt}
.reg caption{text-align:left;font-weight:700;padding:.4mm 0}
.reg th,.reg td{border:1px solid var(--line);padding:.5mm 1.6mm;text-align:left}
.reg th{background:var(--soft);font-weight:500;width:27mm}
.ex .figrow{margin:1mm 0}.ex .coord table{font-size:8.2pt}.ex .coord th,.ex .coord td{padding:.4mm 1.2mm}
.ex .notes{font-size:8.2pt;margin-top:1.5mm}
.form{border:1.5px solid var(--ink);margin-top:2mm}
.form .ttl{text-align:center;font-size:13pt;font-weight:700;letter-spacing:.3em;padding:2.5mm;border-bottom:1.5px solid var(--ink)}
.form .row{display:flex;border-bottom:1px solid var(--ink)}
.form .row:last-child{border-bottom:0}
.form .lb{flex:0 0 33mm;padding:2mm 2.5mm;background:var(--soft);border-right:1px solid var(--ink);font-size:9.5pt;display:flex;align-items:center}
.form .val{flex:1;padding:2mm 3mm;font-size:10.5pt;white-space:pre-wrap;color:var(--g);font-weight:500}
.form table.t{width:100%;border-collapse:collapse;font-size:9.5pt}
.form table.t th,.form table.t td{border:1px solid var(--ink);padding:1.5mm 2mm;text-align:center;height:13mm;vertical-align:middle}
.form table.t th{background:var(--soft);font-weight:500;height:auto}
.form table.t td{color:var(--g);font-weight:500;white-space:pre-wrap}
.form table.t td.rn{background:var(--soft);color:var(--ink);font-weight:500;width:18mm}
.tbl-wrap{padding:0}
pre.keys{margin:.5mm 0;padding:1.2mm 2.5mm;background:var(--soft);border-left:3px solid var(--g);font-family:"Space Mono",Menlo,monospace;font-size:8.6pt;white-space:pre-wrap;line-height:1.5}
code{font-family:"Space Mono",Menlo,monospace;font-size:9.5pt}
@page{size:A4;margin:0}
@media print{html{background:#fff}.sheet{margin:0;box-shadow:none;page-break-after:always;break-after:page;overflow:hidden;height:297mm}.sheet.flow{height:auto;overflow:visible}}
"""


_REG = json.load(open(os.path.join(HERE, 'registry.json'), encoding='utf-8'))
_TAX = json.load(open(os.path.join(HERE, 'taxonomy.json'), encoding='utf-8'))


def log_box(p, side):
    """解答ページの最後に置く「記録」の欄：この問の想定のひっかけの型と、記録のコマンド"""
    names = _TAX['traps_morning'] if side == 'morning' else _TAX['traps_evening']
    ts = _REG.get(p['id'], {}).get('traps', [])
    items = ''.join(f'<li>□ {E(t)}　{E(names.get(t, ""))}</li>' for t in ts)
    ex = ts[0] if ts else ('M3' if side == 'morning' else 'A2')
    return ('<h2>記録（○・△・× と、引っかかった型に✓）</h2>'
            f'<ul class="chk">{items}<li>□ 他（メモ：　　　　　　　　）</li></ul>'
            f'<p class="src">記録：<code>python3 daily-drill/kiroku.py add {E(p["id"])} × {E(ex)} --item 欄の名前</code>（○ のときは型を書かない）。集計と解き直しの予定は daily-drill/log/report.md</p>')


def pages(title, bodies, foot='', right='条文は note-articles/laws/ の原文で照合済み', flow=False):
    sheets = ''.join(f'<div class="sheet{" flow" if flow else ""}">{x}<div class="foot"><span>{E(foot)}　{i + 1}/{len(bodies)}</span><span>{E(right)}</span></div></div>' for i, x in enumerate(bodies))
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><style>{CSS}</style></head><body>{sheets}</body></html>')


def page(title, body, foot='', flow=False, right='条文は note-articles/laws/ の原文で照合済み'):
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><style>{CSS}</style></head><body><div class="sheet{" flow" if flow else ""}">{body}'
            f'<div class="foot"><span>{E(foot)}</span><span>{E(right)}</span></div></div></body></html>')


def daylab(day):
    """見出しの日の表示（本番形式の統合問題などは、日の番号の代わりに名前を入れる）"""
    return f'第{day}日' if isinstance(day, int) and day > 0 else str(day)


def head(day, kind, theme, minutes):
    return (f'<div class="hd"><h1>{daylab(day)}　{kind}</h1><span class="meta">日付：　　月　　日　／　目安 {minutes}分　／　時間：　　分</span></div>'
            f'<p class="theme">{E(theme)}</p>')


def lines(mm):
    return f'<div class="lines" style="height:{mm}mm"></div>'


def quote_block(b):
    if 'doc' in b:          # 先例など：過去問の解説の記載
        return f'<blockquote>{E(b.get("label", "先例"))}（過去問の解説 {E(b["doc"].split("/")[-1])}）「{E(b["quote"])}」</blockquote>'
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
    return page(f'{daylab(p["day"])} 朝 問題', body, f'{p["id"]}')


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
    return page(f'{daylab(p["day"])} 朝 解答', body, f'{p["id"]} 解答', flow=True)


# ---------- 夜 ----------
def exam_body(p):
    ex = p['exam']
    body = head(p['day'], '夜：記述式ドリル（問題）', p['title'], 15)
    left = '<h2>事実関係</h2><ol>' + ''.join(f'<li>{E(x)}</li>' for x in ex['facts']) + '</ol>'
    left += '<h2>注</h2><ol class="notes">' + ''.join(f'<li>{E(x)}</li>' for x in ex['notes']) + '</ol>'
    right = '<h2>' + ex.get('register_title', '登記記録' if p['form_type'] == 'land' else '土地の登記記録') + '</h2>'
    for sec in ex['register']:
        right += f'<table class="reg"><caption>{E(sec["name"])}</caption>' + ''.join(f'<tr><th>{E(k)}</th><td>{E(v)}</td></tr>' for k, v in sec['rows']) + '</table>'
    if p.get('layout') == 'none':
        pass
    elif p.get('layout') == 'generic':
        c = p.get('calc', {})
        names = p.get('coords', [])
        right += '<h2>' + ex.get('fig_title', '現況（座標は平面直角座標系）') + '</h2>'
        right += f'<div class="figrow">{figure.svg_generic(p["fig"], vh=560)}</div>'
        if names:
            right += '<div class="coord"><table><tr><th>点</th>' + ''.join(f'<th>{n}</th>' for n in names) + '</tr>'
            right += '<tr><th>X（北）</th>' + ''.join(f'<td>{c["points"][n][0]:.2f}</td>' for n in names) + '</tr>'
            right += '<tr><th>Y（東）</th>' + ''.join(f'<td>{c["points"][n][1]:.2f}</td>' for n in names) + '</tr></table></div>'
        right += '<p style="font-size:8.2pt;color:var(--mute);line-height:1.5">' + E(ex.get('fig_note', '点A〜Dは本件土地の境界標。点a〜dは居宅の外形の角（令和8年10月5日完成）。')) + '</p>'
    elif p['form_type'] == 'land':
        c = p['calc']
        names = list(c['points'].keys())
        right += '<h2>測量成果（座標は平面直角座標系）</h2>'
        right += f'<div class="figrow">{figure.svg_land(p)}</div>'
        right += '<div class="coord"><table><tr><th>点</th>' + ''.join(f'<th>{n}</th>' for n in names) + '</tr>'
        right += '<tr><th>X（北）</th>' + ''.join(f'<td>{c["points"][n][0]:.2f}</td>' for n in names) + '</tr>'
        right += '<tr><th>Y（東）</th>' + ''.join(f'<td>{c["points"][n][1]:.2f}</td>' for n in names) + '</tr></table></div>'
    else:
        right += '<h2>各階平面図</h2>' + f'<div class="figrow">{figure.svg_plan(p)}</div>'
        right += '<p style="font-size:8.2pt;color:var(--mute);line-height:1.5">' + '　'.join(E(x) for x in p['plan']['legend'] if x) + '</p>'
    body += f'<div class="ex"><p>{E(ex["lead"])}</p><div class="g2"><div>{left}</div><div>{right}</div></div></div>'
    return body


def form_body(p, answers=False):
    f = p['form']
    body = head(p['day'], '夜：記述式ドリル（答案用紙）' if not answers else '夜：解答（記入例）', '白紙の申請書に記入する' if not answers else p['title'], 15)
    out = f'<div class="form"><div class="ttl">{E(f["title"])}</div>'
    for it in f['items']:
        if it['kind'] == 'field':
            h = 9 + 7 * (it['lines'] - 1)
            v = E(it['answer']) if answers else ''
            out += f'<div class="row"><div class="lb">{E(it["label"])}</div><div class="val" style="min-height:{h}mm">{v}</div></div>'
        else:
            th = '<tr>' + ''.join(f'<th>{E(c)}</th>' for c in it['cols']) + '</tr>'
            trs = ''
            for r in it['rows']:
                rn = f'<td class="rn">{E(r["name"])}</td>' if it['cols'][0] == '' else ''
                cells = ''.join(f'<td>{E(c) if answers else ""}</td>' for c in r['cells'])
                trs += f'<tr>{rn}{cells}</tr>'
            if it['cols'][0] != '' and not any(r['name'] for r in it['rows']):
                pass
            out += f'<div class="row"><div class="lb">{E(it["label"])}</div><div class="val tbl-wrap" style="padding:0"><table class="t">{th}{trs}</table></div></div>'
    out += '</div>'
    return body + out


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



def calc2_answer_box_compact(p, filled=False):
    """回答欄が多いとき、2列に並べて場所を節約する（辺長・地積など単独の欄用）。xyの欄は通常の表にする。"""
    cells = []
    for a in p['answers']:
        unit = {'area': '㎡', 'len': 'm'}.get(a['kind'], '')
        v = E(a['value']) if filled else ''
        wide = a['kind'] == 'text'
        cells.append((a['label'], v, unit, wide))
    rows = ''
    i = 0
    while i < len(cells):
        lab, v, u, wide = cells[i]
        if wide:
            rows += f'<tr><th>{E(lab)}</th><td colspan="3"><span class="box" style="min-width:70mm">{v}</span></td></tr>'
            i += 1
            continue
        if i + 1 < len(cells) and not cells[i + 1][3]:
            l2, v2, u2, _ = cells[i + 1]
            rows += f'<tr><th>{E(lab)}</th><td><span class="box" style="min-width:24mm">{v}</span> {u}</td><th>{E(l2)}</th><td><span class="box" style="min-width:24mm">{v2}</span> {u2}</td></tr>'
            i += 2
        else:
            rows += f'<tr><th>{E(lab)}</th><td colspan="3"><span class="box" style="min-width:24mm">{v}</span> {u}</td></tr>'
            i += 1
    return f'<table class="ans-box c2">{rows}</table>'


def calc2_answer_box(p, filled=False):
    rows = ''
    for a in p['answers']:
        if a['kind'] == 'xy':
            fx = f'{a["value"][0]}' if filled else ''
            fy = f'{a["value"][1]}' if filled else ''
            cell = (f'<td>X ＝ <span class="box{" fill" if filled else ""}" style="min-width:34mm">{fx}</span>　　Y ＝ <span class="box" style="min-width:34mm">{fy}</span></td>')
        elif a['kind'] == 'text':
            v = E(a['value']) if filled else ''
            cell = f'<td><span class="box" style="min-width:70mm">{v}</span></td>'
        else:
            unit = '㎡' if a['kind'] == 'area' else 'm'
            v = a['value'] if filled else ''
            cell = f'<td><span class="box" style="min-width:34mm">{v}</span> {unit}</td>'
        rows += f'<tr><th>{E(a["label"])}</th>{cell}</tr>'
    return f'<table class="ans-box">{rows}</table>'


def calc2_tables(p, cols=2):
    out = ''
    for t in p['tables']:
        th = ''.join(f'<th>{E(c)}</th>' for c in t['cols'])
        tr = ''.join('<tr>' + ''.join(f'<td>{E(c)}</td>' for c in r) + '</tr>' for r in t['rows'])
        out += f'<div><table><caption>{E(t["title"])}</caption><tr>{th}</tr>{tr}</table></div>'
    return f'<div class="tg" style="grid-template-columns:repeat({cols},1fr)">{out}</div>'


def calc2_q(p):
    x = p['text']
    mins = p.get('minutes', 15)
    s1 = head(p['day'], '夜：記述式ドリル（問題）', p['title'], mins)
    s1 += '<h2>解答欄（小数第2位まで。ここに先に書く）</h2>' + calc2_answer_box(p)
    s1 += '<div class="q2"><p>' + E(x['lead']) + '</p>'
    s1 += '<h2>【条件】</h2><ol>' + ''.join(f'<li>{E(t)}</li>' for t in x['conditions']) + '</ol>'
    s1 += '<h2>【聞き取り結果】</h2><ol>' + ''.join(f'<li>{E(t)}</li>' for t in x['hearing']) + '</ol>'
    s1 += '<h2>【注】</h2><ol>' + ''.join(f'<li>{E(t)}</li>' for t in x['notes']) + '</ol>'
    s1 += '<p style="color:var(--mute)">図・座標値・観測値の表は、次のページにある。</p></div>'
    s2 = head(p['day'], '夜：記述式ドリル（図・測量成果）', p['title'], mins)
    s2 += '<h2>図（座標値にもとづく。黒丸＝与えられた点、赤い白抜き＝求める点）</h2>'
    s2 += f'<div class="figrow">{figure.svg_generic(p["fig"], vh=650)}</div>'
    s2 += '<h2>測量成果・地積測量図等の記載</h2>' + calc2_tables(p)
    if len(p['answers']) > 6:
        s1 = '<div class="dense">' + s1 + '</div>'
    return pages(f'{daylab(p["day"])} 夜 問題', [s1, s2], p['id'], right='')


def calc2_a(p):
    body = head(p['day'], '夜：解答', p['title'], 15)
    body += '<h2>答え</h2>' + calc2_answer_box(p, filled=True)
    body += f'<div class="figrow">{figure.svg_generic(p["fig"], reveal=True, vh=620)}</div>'
    if p.get('basis'):
        body += '<h2>根拠条文</h2>' + ''.join(quote_block(x) for x in p['basis'])
    body += f'<h2>つまずきポイント</h2><p>{E(p["trap"])}</p>'
    sheet1 = body
    body2 = head(p['day'], '夜：解答（電卓操作）', 'キヤノン F-789SG・複素数モード（[MODE] [2]）。Z ＝ X ＋ Yi（X＝北、Y＝東）。負の数は「0 − 数」で入れる', 15)
    for g in p['keys']:
        body2 += f'<h2>{E(g["title"])}</h2>'
        for s in g['steps']:
            body2 += f'<div class="q">{E(s["title"])}</div>'
            if s.get('formula'):
                body2 += f'<p class="src" style="margin:0">式：{E(s["formula"])}</p>'
            body2 += f'<pre class="keys">{E(s["keys"])}</pre>'
            if s.get('display'):
                body2 += f'<p class="ans" style="margin:.5mm 0 1.5mm">表示：<b>{E(s["display"])}</b></p>'
    return pages(f'{daylab(p["day"])} 夜 解答', [sheet1, body2], f'{p["id"]} 解答', right='', flow=True)


def draw_q(p):
    x = p['text']
    mins = p.get('minutes', 20)
    s1 = head(p['day'], '夜：記述式ドリル（問題）', p['title'], mins)
    s1 += '<h2>解答欄（先に書く）</h2>' + calc2_answer_box_compact(p)
    s1 += '<div class="q2"><p>' + E(x['lead']) + '</p>'
    s1 += '<h2>【条件】</h2><ol>' + ''.join(f'<li>{E(t)}</li>' for t in x['conditions']) + '</ol>'
    s1 += '<h2>【聞き取り結果】</h2><ol>' + ''.join(f'<li>{E(t)}</li>' for t in x['hearing']) + '</ol>'
    s1 += '<h2>【注】</h2><ol>' + ''.join(f'<li>{E(t)}</li>' for t in x['notes']) + '</ol></div>'
    s1 += calc2_tables(p, 3 if len(p['tables']) >= 3 else 2)
    s1 = '<div class="dense">' + s1 + '</div>'
    if p['draw'] == 'chiseki':
        s2 = head(p['day'], '夜：記述式ドリル（答案用紙）', '地積測量図を作成する（実寸・縮尺250分の1）', mins) + f'<div class="drawwrap">{draw_forms.chiseki_blank()}</div>'
    else:
        a, b2 = draw_forms.tatemono_blank()
        s2 = head(p['day'], '夜：記述式ドリル（答案用紙）', '建物図面（500分の1）・各階平面図（250分の1）を作成する（実寸）', mins) + f'<div class="drawwrap">{a}</div><div class="drawwrap">{b2}</div>'
    return pages(f'{daylab(p["day"])} 夜 問題', [s1, s2], p['id'], right='')


def draw_a(p):
    body = head(p['day'], '夜：解答', p['title'], p.get('minutes', 20))
    body += '<h2>答え</h2>' + calc2_answer_box_compact(p, filled=True)
    body += '<h2>自己採点（できた項目に○。作図は定規で長さを測って確かめる）</h2><table class="pt">' + ''.join(f'<tr><td style="width:7mm">□</td><td>{E(t)}</td><td class="src" style="width:46mm">{E(b_)}</td></tr>' for t, b_ in p['rubric']) + '</table>'
    body += '<h2>解き方</h2><ul style="margin:0;padding-left:5mm">' + ''.join(f'<li>{E(s)}</li>' for s in p['steps']) + '</ul>'
    body += f'<h2>つまずきポイント</h2><p>{E(p["trap"])}</p>'
    sheets = [body]
    if p['draw'] == 'chiseki':
        sheets.append(head(p['day'], '夜：解答（模範の作図）', '地積測量図（実寸・縮尺250分の1。座標から機械で作図）', p.get('minutes', 20)) + f'<div class="drawwrap">{draw_forms.chiseki_solved(p["spec"])}</div>')
    else:
        a, b2 = draw_forms.tatemono_solved(p['spec'])
        sheets.append(head(p['day'], '夜：解答（模範の作図）', '建物図面・各階平面図（実寸。座標から機械で作図）', p.get('minutes', 20)) + f'<div class="drawwrap">{a}</div><div class="drawwrap">{b2}</div>')
    if p.get('keys'):
        body2 = head(p['day'], '夜：解答（電卓操作）', 'キヤノン F-789SG・複素数モード（[MODE] [2]）。負の数は「0 − 数」で入れる', p.get('minutes', 20))
        for g in p['keys']:
            body2 += f'<h2>{E(g["title"])}</h2>'
            for s in g['steps']:
                body2 += f'<div class="q">{E(s["title"])}</div>'
                if s.get('formula'):
                    body2 += f'<p class="src" style="margin:0">式：{E(s["formula"])}</p>'
                body2 += f'<pre class="keys">{E(s["keys"])}</pre>'
                if s.get('display'):
                    body2 += f'<p class="ans" style="margin:.5mm 0 1.5mm">表示：<b>{E(s["display"])}</b></p>'
        sheets.append(body2)
    return pages(f'{daylab(p["day"])} 夜 解答', sheets, f'{p["id"]} 解答', right='', flow=True)


def pm_q(p):
    if p['kind'] == 'draw':
        return draw_q(p)
    if p['kind'] == 'calc2':
        return calc2_q(p)
    if p['kind'] == 'shinsei2':
        return pages(f'{daylab(p["day"])} 夜 問題', [exam_body(p), form_body(p)], p['id'])
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
    return page(f'{daylab(p["day"])} 夜 問題', body, p['id'], right='' if p['kind'] == 'calc' else '条文は note-articles/laws/ の原文で照合済み')


def pm_a(p):
    if p['kind'] == 'draw':
        return draw_a(p)
    if p['kind'] == 'calc2':
        return calc2_a(p)
    if p['kind'] == 'shinsei2':
        body = form_body(p, answers=True)
        for it in p['form']['items']:
            body += f'<div class="q">{E(it["label"])}</div>'
            body += ''.join(quote_block(x) for x in it['basis'])
            body += f'<p class="src">{E(it["note"])}</p>'
        return page(f'{daylab(p["day"])} 夜 解答', body, f'{p["id"]} 解答', flow=True)
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
    else:
        for f in p['fields']:
            body += f'<div class="q">{E(f["q"])}</div><div class="ans">{E(f["answer"])}</div>'
            body += ''.join(quote_block(b) for b in f['basis'])
            if f['note']:
                body += f'<p class="src">{E(f["note"])}</p>'
    return page(f'{daylab(p["day"])} 夜 解答', body, f'{p["id"]} 解答', flow=True)


def main():
    os.makedirs(OUT, exist_ok=True)
    am = {json.load(open(f, encoding='utf-8'))['day']: json.load(open(f, encoding='utf-8')) for f in glob.glob(os.path.join(HERE, 'morning', 'problems', '*.json'))}
    pm = {json.load(open(f, encoding='utf-8'))['day']: json.load(open(f, encoding='utf-8')) for f in glob.glob(os.path.join(HERE, 'evening', 'problems', '*.json'))}
    rows = ''
    for d in sorted(set(am) | set(pm)):
        links = []
        if d in am:
            for suf, fn, lab in (('', am_q, '朝 問題'), ('-ans', am_a, '朝 解答')):
                n = f'day{d:03d}-am{suf}.html'
                open(os.path.join(OUT, n), 'w', encoding='utf-8').write(fn(am[d]))
                links.append(f'<a href="{n}">{lab}</a>')
        if d in pm:
            for suf, fn, lab in (('', pm_q, '夜 問題'), ('-ans', pm_a, '夜 解答')):
                n = f'day{d:03d}-pm{suf}.html'
                open(os.path.join(OUT, n), 'w', encoding='utf-8').write(fn(pm[d]))
                links.append(f'<a href="{n}">{lab}</a>')
        rows += f'<tr><td>第{d}日</td><td>{E(am[d]["theme"]) if d in am else ""}</td><td>{E(pm[d]["title"]) if d in pm else ""}</td><td>{" ／ ".join(links)}</td></tr>'
    extra = ''
    for pre, lab in (('sat', '土曜の20問模擬（択一式）'), ('sougou', '本番形式の統合問題（記述式・60分）')):
        fs = sorted(f for f in os.listdir(OUT) if f.startswith(pre) and f.endswith('.html') and not f.endswith('-ans.html'))
        if fs:
            extra += f'<h2>{lab}</h2><ul>' + ''.join(f'<li><a href="{f}">{f[:-5]} 問題</a> ／ <a href="{f[:-5]}-ans.html">解答</a></li>' for f in fs) + '</ul>'
    idx = (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>毎日ドリル</title>'
           f'<style>{CSS}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid var(--line);padding:2mm 3mm;text-align:left;font-size:10pt}}a{{color:var(--g)}}</style></head>'
           f'<body><div class="sheet"><div class="hd"><h1>毎日ドリル（朝：択一＋書いて説明／夜：記述式）</h1></div>'
           f'<table><tr><th>日</th><th>朝の論点</th><th>夜の内容</th><th>リンク</th></tr>{rows}</table>{extra}</div></body></html>')
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(idx)
    print('out/ に', len(os.listdir(OUT)), 'ファイル')


if __name__ == '__main__':
    main()
