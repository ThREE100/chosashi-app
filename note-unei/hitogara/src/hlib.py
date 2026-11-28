"""第4回以降の本文の図を HTML→Chromium で書き出す共通部品。
- table_fig：見出し＋表（列ごとに幅を指定）＋注
- bar_fig：見出し＋横棒（名前・棒・値）＋注
- cards_fig：見出し＋カード（見出しと箇条書き）＋注
note用は横1280px・高さは中身なり、Instagram用は1080×1440で、収まらないときは全体を縮めて収める（縮めた倍率を表示する）。
"""
import os, glob, html
E = html.escape
CSS = '''body{{margin:0;background:#fbf8f1;font-family:"Noto Sans CJK JP";color:#1f2d3d}}
.wrap{{width:{W}px;box-sizing:border-box;padding:{pad};display:flex;flex-direction:column;transform-origin:top left}}
h1{{font-size:{h1}px;margin:0 0 8px;line-height:1.3}} .sub{{font-size:{sub}px;color:#55606e;margin-bottom:20px;line-height:1.5}}
.foot{{margin-top:16px;font-size:{foot}px;color:#55606e;line-height:1.6}}
table{{border-collapse:collapse;width:100%;font-size:{fs}px;line-height:1.4;background:#fff}}
th{{background:#1d4f91;color:#fff;font-weight:700;padding:8px 10px;text-align:left}}
td{{border-bottom:1px solid #e3dccd;padding:7px 10px;vertical-align:top}} tr.hl td{{background:#fff4e6}}
td.c{{text-align:center}} td b{{color:#1d4f91}}
.row{{display:flex;align-items:center;gap:14px;margin:7px 0}}
.nm{{width:{nmw}px;font-size:{fs}px;font-weight:700;flex:none;line-height:1.3}} .nm small{{display:block;font-size:{small}px;color:#7a7266;font-weight:400}}
.bw{{flex:1;height:{bh}px;background:#eee8dc;border-radius:8px}} .bar{{height:100%;border-radius:8px}}
.v{{width:{vw}px;text-align:right;font-size:{fs}px;flex:none}} .v b{{font-size:{vb}px}}
.grid{{display:grid;grid-template-columns:{cols};gap:14px}}
.card{{background:#fff;border:2px solid #3b78c2;border-radius:14px;padding:12px 16px}} .card.o{{border-color:#e8a05c;background:#fff8ef}} .card.g{{border-color:#b9b2a4}}
.k{{font-size:{kfs}px;font-weight:700;color:#1d4f91;margin-bottom:4px}} .card.o .k{{color:#a8561a}}
ul{{margin:0;padding-left:1.1em;font-size:{lfs}px;line-height:1.5}}
'''

def _css(ig, fs=None, cols="1fr 1fr", nmw=300):
    W = 1080 if ig else 1280
    fs = fs or (26 if ig else 23)
    return CSS.format(W=W, pad="72px 54px" if ig else "44px 52px", h1=fs + 16, sub=fs - 3, foot=fs - 6, fs=fs,
                      nmw=nmw, small=fs - 8, bh=28, vw=130, vb=fs + 4, cols=cols, kfs=fs + 1, lfs=fs - 3), W

def shot(body, out, ig, **kw):
    from playwright.sync_api import sync_playwright
    css, W = _css(ig, **kw)
    doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><div class="wrap">{body}</div></body></html>'
    hp = os.path.splitext(out)[0] + ".html"; open(hp, "w", encoding="utf-8").write(doc)
    H = 1440 if ig else None
    with sync_playwright() as p:
        exe = (sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome')) or [None])[0]
        b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H or 100}, device_scale_factor=1)
        pg.goto("file://" + os.path.abspath(hp)); pg.wait_for_timeout(300)
        if H:
            sh = pg.evaluate("document.querySelector('.wrap').scrollHeight")
            if sh > H:
                s = H / sh
                pg.evaluate(f"(()=>{{const w=document.querySelector('.wrap');w.style.transform='scale({s:.4f})';w.style.marginLeft='{(W - W*s)/2:.1f}px'}})()")
                print(f"  {os.path.basename(out)}：中身 {sh}px を {s:.2f} 倍に縮めて収めた")
                doc2 = pg.content(); open(hp, "w", encoding="utf-8").write(doc2)
            else:
                pg.evaluate(f"(()=>{{const w=document.querySelector('.wrap');w.style.minHeight='{H}px'}})()")
        pg.screenshot(path=out, full_page=not H); b.close()
    print("wrote", out)

def head(title, sub):
    return f"<h1>{E(title)}</h1><div class=\"sub\">{E(sub)}</div>"

def table_fig(out, ig, title, sub, headers, rows, foot="", hl=(), fs=None):
    th = "".join(f"<th>{E(h)}</th>" for h in headers)
    tr = ""
    for i, r in enumerate(rows):
        tds = "".join(f"<td>{c}</td>" for c in r)   # セルは呼び出し側でエスケープ済みの HTML
        tr += f'<tr class="{"hl" if i in hl else ""}">{tds}</tr>'
    body = head(title, sub) + f"<table><tr>{th}</tr>{tr}</table>" + (f'<div class="foot">{E(foot)}</div>' if foot else "")
    shot(body, out, ig, fs=fs)

def bar_fig(out, ig, title, sub, items, vmax, unit, foot="", fs=None, nmw=300):
    """items: (名前, 小さい注 or "", 値, 色)"""
    rows = ""
    for nm, sm, v, c in items:
        rows += (f'<div class="row"><div class="nm">{E(nm)}{"<small>"+E(sm)+"</small>" if sm else ""}</div>'
                 f'<div class="bw"><div class="bar" style="width:{v/vmax*100:.1f}%;background:{c}"></div></div>'
                 f'<div class="v"><b>{v}</b>{E(unit)}</div></div>')
    body = head(title, sub) + f"<div>{rows}</div>" + (f'<div class="foot">{E(foot)}</div>' if foot else "")
    shot(body, out, ig, fs=fs, nmw=nmw)

def cards_fig(out, ig, title, sub, cards, foot="", cols=None, fs=None):
    """cards: (見出し, [項目], 種類 ""/"o"/"g")。項目は HTML 可（呼び出し側でエスケープ）"""
    cols = cols or ("1fr" if ig else "1fr 1fr")
    cs = "".join(f'<div class="card {k}"><div class="k">{E(t)}</div><ul>{"".join("<li>"+x+"</li>" for x in li)}</ul></div>' for t, li, k in cards)
    body = head(title, sub) + f'<div class="grid">{cs}</div>' + (f'<div class="foot">{E(foot)}</div>' if foot else "")
    shot(body, out, ig, fs=fs, cols=cols)
