"""一枚まとめの画像（HTML→PNG）。文字だけの図なので、画像生成AIは使わず、HTMLを組んでChromiumで書き出す。"""
import html
import os
import re

from catalog import FIELDS

W = 1080
FONT_BODY, FONT_TABLE, FONT_SMALL = 34, 30, 28   # スマホで読める下限（画像の幅1080pxのとき）
MAX_H = 4000


def esc(s):
    s = html.escape(s, quote=False)
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)


def block_html(b):
    k = b['kind']
    out = ['<section class="blk">']
    if b.get('title'):
        out.append('<h3>%s</h3>' % esc(b['title']))
    if k == 'table':
        out.append('<table><thead><tr>%s</tr></thead><tbody>' % ''.join('<th>%s</th>' % esc(h) for h in b['head']))
        for r in b['rows']:
            out.append('<tr>%s</tr>' % ''.join('<td>%s</td>' % esc(c) for c in r))
        out.append('</tbody></table>')
    elif k == 'check':
        cy = ' c2' if b.get('cols_yes') == 2 else ''
        cn = ' c2' if b.get('cols_no') == 2 else ''
        out.append('<div class="chk yes"><div class="lab">%s</div><ul class="%s">%s</ul></div>' % (esc(b.get('yes_label', '書くもの')), cy, ''.join('<li>%s</li>' % esc(x) for x in b['yes'])))
        out.append('<div class="chk no"><div class="lab">%s</div><ul class="%s">%s</ul></div>' % (esc(b.get('no_label', '書かないもの')), cn, ''.join('<li>%s</li>' % esc(x) for x in b['no'])))
    elif k == 'steps':
        out.append('<ol class="steps">%s</ol>' % ''.join('<li>%s</li>' % esc(x) for x in b['items']))
    elif k == 'defs':
        out.append('<dl>%s</dl>' % ''.join('<dt>%s</dt><dd>%s</dd>' % (esc(t), esc(d)) for t, d in b['items']))
    elif k == 'text':
        out.append('<p>%s</p>' % esc(b['text']))
    else:
        raise ValueError(k)
    if b.get('note'):
        out.append('<p class="bnote">%s</p>' % esc(b['note']))
    out.append('</section>')
    return '\n'.join(out)


def sheet_html(c, s):
    fname, acc, light = FIELDS[c['field']]
    ex = s['example']
    body = '\n'.join(block_html(b) for b in s['blocks'])
    ex_lines = ''.join('<div class="exl">%s</div>' % esc(x) for x in ex['lines'])
    traps = ''.join('<li><span class="n">%s</span><span>%s</span></li>' % ('①②③'[i], esc(t)) for i, t in enumerate(s['traps']))
    concl = ''.join('<li>%s</li>' % esc(x) for x in s['conclusion'])
    basis = '　'.join(esc(x) for x in s['basis'])
    return '''<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}
body{width:%(W)dpx;background:#F7F3EE;font-family:"Noto Sans CJK JP","Noto Sans JP",sans-serif;color:#1A1A1A;line-height:1.55;font-size:%(FB)dpx}
.head{background:%(acc)s;color:#fff;padding:36px 44px 32px}
.tag{font-size:%(FS)dpx;font-weight:700;letter-spacing:.05em;opacity:.95}
.tag span{background:#fff;color:%(acc)s;border-radius:999px;padding:2px 18px;margin-left:12px}
h1{font-size:58px;line-height:1.28;margin-top:14px;font-weight:900}
.catch{font-size:36px;margin-top:10px;font-weight:700;opacity:.96}
.wrap{padding:28px 36px 30px}
.lab2{display:inline-block;background:%(acc)s;color:#fff;font-weight:700;font-size:%(FS)dpx;border-radius:8px;padding:2px 16px;margin-bottom:10px}
.concl{background:%(light)s;border:3px solid %(acc)s;border-radius:18px;padding:22px 28px 20px;margin-bottom:26px}
.concl ul{list-style:none}.concl li{font-size:36px;font-weight:700;line-height:1.5;padding-left:1.1em;text-indent:-1.1em;margin-top:6px}
.concl li:before{content:"\\25A0";color:%(acc)s;margin-right:.35em;font-size:.8em}
.blk{background:#fff;border-radius:18px;padding:22px 26px;margin-bottom:22px;box-shadow:0 2px 0 rgba(0,0,0,.07)}
h3{font-size:36px;font-weight:900;border-left:10px solid %(acc)s;padding-left:14px;margin-bottom:14px;line-height:1.35}
table{width:100%%;border-collapse:collapse;font-size:%(FT)dpx;line-height:1.45}
th{background:%(acc)s;color:#fff;font-weight:700;padding:10px 12px;text-align:left;border:2px solid #fff}
td{padding:10px 12px;border:2px solid %(light)s;vertical-align:top}
tbody tr:nth-child(even) td{background:#FAFAF8}
td:first-child{font-weight:700;background:%(light)s !important}
.chk{border-radius:14px;padding:14px 20px 12px;margin-top:12px}
.chk .lab{font-weight:900;font-size:34px;margin-bottom:4px}
.chk ul{list-style:none}.chk ul.c2{column-count:2;column-gap:20px}.chk ul.c2 li{break-inside:avoid}.chk li{font-size:%(FB)dpx;padding-left:1.1em;text-indent:-1.1em;margin-top:4px}
.chk.yes{background:#E8F4EC;border:3px solid #3E8A5A}.chk.yes .lab{color:#2B6E45}.chk.yes li:before{content:"\\25CB";margin-right:.3em;color:#2B6E45;font-weight:900}
.chk.no{background:#FBECE6;border:3px solid #C65A3A}.chk.no .lab{color:#B0431F}.chk.no li:before{content:"\\00D7";margin-right:.3em;color:#B0431F;font-weight:900}
ol.steps{list-style:none;counter-reset:s}ol.steps li{counter-increment:s;font-size:%(FB)dpx;padding-left:2.4em;position:relative;margin-top:10px}
ol.steps li:before{content:counter(s);position:absolute;left:0;top:2px;width:1.7em;height:1.7em;border-radius:50%%;background:%(acc)s;color:#fff;text-align:center;font-weight:700;font-size:.85em;line-height:1.7em}
dl{font-size:%(FB)dpx}dt{font-weight:900;color:%(acc)s;margin-top:10px}dd{margin-left:.4em}
p{font-size:%(FB)dpx}.bnote{font-size:%(FS)dpx;margin-top:10px;color:#444}
.ex{background:#E9F0EC;border:3px solid #6B8F7B;border-radius:18px;padding:20px 26px;margin-bottom:22px}
.ex h3{border-left-color:#6B8F7B}.exl{font-size:%(FB)dpx;margin-top:6px;word-break:break-all}
.trap{background:#FBECE6;border:3px solid #C65A3A;border-radius:18px;padding:20px 26px 16px;margin-bottom:22px}
.trap h3{border-left-color:#C65A3A}.trap ul{list-style:none}.trap li{display:flex;gap:12px;font-size:%(FB)dpx;margin-top:8px}
.trap .n{font-weight:900;color:#B0431F;flex:none}
.foot{font-size:%(FS)dpx;color:#444;border-top:3px solid %(acc)s;padding-top:14px;margin-top:6px;line-height:1.5}
b{font-weight:900;background:linear-gradient(transparent 62%%,#FFE9A8 62%%)}
</style></head><body>
<div class="head"><div class="tag">すきま時間の一枚まとめ<span>%(fname)s</span></div><h1>%(title)s</h1><div class="catch">%(catch)s</div></div>
<div class="wrap">
<div class="lab2">この一枚で言えること</div>
<div class="concl"><ul>%(concl)s</ul></div>
%(body)s
<div class="ex"><h3>%(exkind)s：%(extitle)s</h3>%(exlines)s</div>
<div class="trap"><h3>間違えやすい点</h3><ul>%(traps)s</ul></div>
<div class="foot">根拠：%(basis)s</div>
</div></body></html>''' % dict(W=W, FB=FONT_BODY, FT=FONT_TABLE, FS=FONT_SMALL, acc=acc, light=light, fname=esc(fname), title=esc(c['title']), catch=esc(c['catch']),
                              concl=concl, body=body, exkind=esc(ex['kind']), extitle=esc(ex['title']), exlines=ex_lines, traps=traps, basis=basis)


def find_chrome():
    import glob
    for p in sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome')):
        return p
    return None


def render_many(jobs):
    """jobs: [(html_text, png_path)] → [(width,height)]。Chromiumを1回だけ起動する。"""
    from playwright.sync_api import sync_playwright
    res = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=find_chrome(), args=['--no-sandbox'])
        pg = b.new_page(viewport={'width': W, 'height': 800}, device_scale_factor=1)
        for h, out in jobs:
            os.makedirs(os.path.dirname(out), exist_ok=True)
            html_path = out[:-4] + '.html'
            open(html_path, 'w', encoding='utf-8').write(h)
            pg.goto('file://' + os.path.abspath(html_path))
            pg.wait_for_timeout(150)
            hgt = pg.evaluate('document.documentElement.scrollHeight')
            over = pg.evaluate('''()=>[...document.querySelectorAll('td,th,li,dd,p,.exl,h1')].filter(e=>e.scrollWidth>e.clientWidth+2).length''')
            pg.screenshot(path=out, clip={'x': 0, 'y': 0, 'width': W, 'height': hgt}, full_page=True)
            res.append((W, hgt, over))
        b.close()
    return res
