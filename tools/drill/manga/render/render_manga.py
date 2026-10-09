#!/usr/bin/env python3
"""4コマ解説図解を、画像生成AIを使わずに HTML＋Chromium で描き出す（文字が崩れない版）。

使い方: python3 tools/drill/manga/render/render_manga.py <layoutの名前> [--html]
- 文字はすべて、同梱の固定フォント（render/fonts/zen-maru-gothic、SIL OFL）で描く。文字が崩れたり、似た字（合体⇔合併）に化けたりしない。
- タイトル・見出し・台詞・結論帯・チェック欄は、manga_specs.py の SPECS（構成表の正本）から読む。図の中身は layouts/<名前>.py の構造化データ。
  図の文字列が構成表（fig 行の「」の中）と一致しない場合は、描く前にエラーにする。
- キャラクターは sprites/ の透過PNG（画像生成AIが描いた藍子・トリ先生の切り抜き。試作では生成済みの図から切り出した）。
- 出力: render/out/<名前>.png（1080×1920）
必要なもの: Python の playwright と Chromium（/opt/pw-browsers）。"""
import sys, re, html, pathlib, importlib.util, glob, os
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import manga_specs  # noqa: E402

NAVY, PALE, CREAM, YEL = "#1f3a68", "#eaf1fb", "#fffaf0", "#ffe66d"
W, H = 1080, 1920

import budoux  # 日本語の文節で折り返すため（<wbr>を入れる）
_BX = budoux.load_default_japanese_parser()

def esc(s): return html.escape(s, quote=False)

def T(s):
    """文節（BudouX）の切れ目に <wbr> を入れる。CSSの word-break:keep-all と組み合わせ、文節の途中では折り返さない。"""
    return "<wbr>".join(esc(x) for x in _BX.parse(s))

def hl(text, key):
    """強調語（黄色マーカー）。keyが台詞の文中にあるときだけ囲む。"""
    if key and key in text:
        a, b = text.split(key, 1)
        return T(a) + f"<mark>{T(key)}</mark>" + T(b)
    return T(text)

def load_layout(name):
    p = HERE / "layouts" / f"{name}.py"
    ns = {}; exec(compile(p.read_text(encoding="utf8"), str(p), "exec"), ns)
    return ns["LAYOUT"]

def fig_strings(layout):
    out = []
    for p in layout["panels"]:
        k = p["kind"]
        if k == "table":
            out += p["header"] + [c for r in p["rows"] for c in r]
        elif k == "cards":
            for c in p["cards"]: out += [c["heading"], c["tag"]] + c["lines"]
        elif k == "steps":
            for s in p["steps"]: out += [s["heading"], s["body"]] + ([s["ribbon"]] if s.get("ribbon") else [])
    return out

def check(layout, sp):
    quoted = set()
    for p in sp["panels"]:
        for ln in p["fig"]:
            quoted.update(re.findall(r"「([^」]+)」", ln))
    bad = [s for s in fig_strings(layout) if s not in quoted]
    if bad:
        raise SystemExit("図の文字列が構成表（SPECSのfig行）にない:\n  " + "\n  ".join(bad))

CSS = """
@font-face { font-family:'ZMG'; font-weight:500; src:url(%(f500)s); }
"""

def font_css():
    base = HERE / "fonts" / "zen-maru-gothic"
    css = ""
    for w in (500, 700):
        t = (base / f"{w}.css").read_text(encoding="utf8")
        t = t.replace("url(./files/", f"url(file://{base}/files/")
        css += t + "\n"
    return css

def bubble(who, text, hlkey, brk, extra_cls=""):
    cls = "aiko" if who == "藍子" else "tori"
    body = hl(text, hlkey)   # 画像生成AI用の改行指定は使わず、ブラウザが自動で折り返す
    return f'<div class="bubble {cls} {extra_cls}">{body}</div>'

def panel_html(i, p, lp, sp_panel):
    label = esc(sp_panel["label"])
    chars = sp_panel.get("chars")
    bub = sp_panel["bubbles"]
    out = [f'<section class="panel p{i}"><div class="tab">{label}</div>']
    k = lp["kind"]
    if k == "table":
        widths = lp["widths"]
        t = '<table class="tbl"><tr>' + "".join(f'<th style="width:{w}px">{esc(h)}</th>' for h, w in zip(lp["header"], widths)) + "</tr>"
        for r in lp["rows"]:
            t += "<tr>" + "".join(f"<td>{T(c)}</td>" for c in r) + "</tr>"
        t += "</table>"
        out.append(f'<div class="center small">{t}</div>')
    elif k == "cards":
        cs = ""
        for c in lp["cards"]:
            cs += (f'<div class="card"><div class="ch">{esc(c["heading"])}</div><div class="tag">{esc(c["tag"])}</div>'
                   + "".join(f'<div class="cl">{T(l)}</div>' for l in c["lines"]) + "</div>")
        out.append(f'<div class="center cards">{cs}</div>')
    elif k == "steps":
        ss = ""
        for n, s in enumerate(lp["steps"], 1):
            rib = f'<div class="rib">{esc(s["ribbon"])}</div>' if s.get("ribbon") else ""
            ss += f'<div class="step"><div class="sh"><span class="num">{n}</span>{esc(s["heading"])}</div>{rib}<div class="sb">{T(s["body"])}</div></div>'
        out.append(f'<div class="stepcol">{ss}</div>')
    elif k == "checklist":
        items = "".join(f'<div class="ci"><span class="chk">✓</span><span>{T(c)}</span></div>' for c in sp_panel["checklist"])
        out.append(f'<div class="center check"><div class="cbox">{items}</div></div>')
    if chars == "faces":
        rows = ""
        for who, text, key, brk in [(b[0], b[1], b[2], b[3] if len(b) > 3 else None) for b in bub]:
            face = f'<span class="face {"fa" if who == "藍子" else "ft"}"></span>'
            b = bubble(who, text, key, brk, "faces")
            rows += f'<div class="frow {"L" if who == "藍子" else "R"}">{face if who=="藍子" else ""}{b}{face if who!="藍子" else ""}</div>'
        out.append(f'<div class="conv">{rows}</div>')
    else:
        small = chars == "small"
        a_sprite, t_sprite = "aiko_think", "tori_point"
        out.append(f'<img class="spr aiko {"sm" if small else ""}" src="file://{HERE}/sprites/{a_sprite}.png">')
        out.append(f'<img class="spr tori {"sm" if small else ""}" src="file://{HERE}/sprites/{t_sprite}.png">')
        for who, text, key, brk in [(b[0], b[1], b[2], b[3] if len(b) > 3 else None) for b in bub]:
            out.append(bubble(who, text, key, brk, "small" if small else ""))
    out.append("</section>")
    return "".join(out)

def build_html(layout, sp):
    panels = ""
    for i, (lp, spp) in enumerate(zip(layout["panels"], sp["panels"])):
        panels += panel_html(i, lp, lp, spp)
    title = hl(sp["title"], sp["title_hl"])
    band1 = hl(sp["band1"], None)
    css = font_css() + f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{word-break:keep-all;overflow-wrap:anywhere;text-wrap:balance;width:{W}px;height:{H}px;background:{CREAM};font-family:'Zen Maru Gothic','IPAGothic',sans-serif;font-weight:500;color:{NAVY};position:relative;overflow:hidden}}
mark{{background:linear-gradient(transparent 55%,{YEL} 55%);color:inherit}}
.title{{position:absolute;left:16px;right:16px;top:14px;height:128px;border:5px solid {NAVY};border-radius:26px;background:#fff9dd;display:flex;align-items:center;justify-content:center}}
.title span{{font-weight:700;font-size:52px;white-space:nowrap}}
.panel{{position:absolute;left:16px;right:16px;height:392px;border:5px solid {NAVY};border-radius:26px;background:#fffdf6}}
.p0{{top:154px}}.p1{{top:556px}}.p2{{top:958px}}.p3{{top:1360px}}
.tab{{position:absolute;left:-5px;top:-5px;background:{NAVY};color:#fff;font-weight:700;font-size:32px;padding:8px 30px 8px 22px;border-radius:22px 0 22px 0;height:54px;line-height:38px;white-space:nowrap}}
.band{{position:absolute;left:16px;right:16px;top:1764px;height:142px;border:5px solid {NAVY};border-radius:26px;background:#fff3b0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;font-weight:700;text-align:center;padding:0 24px}}
.band .l1{{font-size:44px;white-space:nowrap}}.band .l2{{font-size:20px;font-weight:500;line-height:1.2}}
.bubble{{position:absolute;background:#fff;border:3.5px solid {NAVY};border-radius:22px;padding:8px 18px;font-weight:700;font-size:26px;line-height:1.25;text-align:left;z-index:3;max-width:410px}}
.bubble:after{{content:"";position:absolute;bottom:-13px;width:20px;height:20px;background:#fff;border-right:3.5px solid {NAVY};border-bottom:3.5px solid {NAVY};transform:rotate(45deg)}}
.bubble.aiko{{left:96px;top:60px}}.bubble.aiko:after{{left:32px}}
.bubble.tori{{right:96px;top:60px}}.bubble.tori:after{{right:32px}}
.spr{{position:absolute;bottom:8px;z-index:2}}
.spr.aiko{{left:14px;height:200px}}.spr.tori{{right:16px;height:200px}}
.spr.sm{{height:150px}}
.center{{position:absolute;left:230px;right:230px;top:150px;bottom:14px;display:flex;align-items:flex-start;justify-content:center}}
.center.small{{left:150px;right:150px;top:164px}}
table.tbl{{border-collapse:collapse;table-layout:fixed;width:100%;font-size:22px;font-weight:700;background:#f4f7fc}}
.tbl th{{background:{NAVY};color:#fff;padding:5px 8px;border:2.5px solid {NAVY};height:38px;font-size:22px}}
.tbl td{{padding:3px 10px;border:2.5px solid #6f86ad;text-align:left;height:41px;line-height:1.2}}
.tbl td:first-child{{text-align:center}}
.cards{{left:200px;right:200px;gap:14px;align-items:stretch}}
.card{{flex:1;background:{PALE};border:4px solid {NAVY};border-radius:18px;padding:6px 8px;text-align:center;display:flex;flex-direction:column;gap:6px}}
.ch{{font-size:24px;white-space:nowrap;font-weight:700;color:{NAVY};border-bottom:3px solid {NAVY};padding-bottom:4px;line-height:1.2}}
.tag{{align-self:center;background:#cfe0f7;border-radius:999px;padding:1px 10px;font-size:17px;white-space:nowrap;font-weight:700}}
.cl{{font-size:21px;font-weight:700;line-height:1.25;background:#fff;border-radius:10px;padding:5px 7px}}
.stepcol{{position:absolute;left:18px;top:64px;width:564px;display:flex;flex-direction:column;gap:8px}}
.step{{background:{PALE};border:3.5px solid {NAVY};border-radius:14px;padding:5px 12px}}
.sh{{font-size:24px;font-weight:700;display:flex;align-items:center;gap:8px;white-space:nowrap}}
.num{{display:inline-flex;flex:0 0 30px;width:30px;height:30px;border-radius:50%;background:{NAVY};color:#fff;align-items:center;justify-content:center;font-size:20px}}
.rib{{background:{NAVY};color:#fff;font-weight:700;font-size:21px;border-radius:8px;padding:1px 12px;margin:3px 0}}
.sb{{font-size:21px;font-weight:700;line-height:1.25;margin-top:1px}}
.conv{{position:absolute;right:14px;top:62px;width:450px;bottom:10px;display:flex;flex-direction:column;justify-content:space-between}}
.frow{{display:flex;align-items:center;gap:10px;height:76px}}
.frow.R{{justify-content:flex-end}}
.bubble.faces{{position:relative;left:auto;top:auto;right:auto;font-size:23px;padding:5px 12px;line-height:1.2;border-width:3px;border-radius:18px;max-width:360px}}
.bubble.faces:after{{display:none}}
.face{{flex:0 0 68px;height:68px;border-radius:50%;border:3px solid {NAVY};background-color:#fffdf6;background-repeat:no-repeat}}
.face.fa{{background-image:url(file://{HERE}/sprites/aiko_think.png);background-size:116px;background-position:-22px -14px}}
.face.ft{{background-image:url(file://{HERE}/sprites/tori_point.png);background-size:100px;background-position:-14px -3px}}
.cbox{{background:#fff;border:4px solid {NAVY};border-radius:18px;padding:8px 16px;width:100%;display:flex;flex-direction:column;gap:4px}}
.ci{{display:flex;align-items:center;gap:12px;font-size:22px;font-weight:700;line-height:1.25;border-bottom:2px solid #c9d6ea;padding:4px 0}}
.ci:last-child{{border-bottom:none}}
.chk{{flex:0 0 34px;height:34px;border-radius:8px;background:#2f6fe0;color:#fff;font-size:24px;display:flex;align-items:center;justify-content:center}}
.center.check{{left:200px;right:200px}}
"""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="title"><span>{title}</span></div>{panels}
<div class="band"><div class="l1">{band1}</div><div class="l2">{T(sp['band2'])}</div></div>
</body></html>"""

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args: print(__doc__); sys.exit(2)
    name = args[0]
    layout = load_layout(name)
    sp = manga_specs.SPECS[layout["spec_key"]]
    check(layout, sp)
    page = build_html(layout, sp)
    out_dir = HERE / "out"; out_dir.mkdir(exist_ok=True)
    (out_dir / f"{name}.html").write_text(page, encoding="utf8")
    from playwright.sync_api import sync_playwright
    exe = None
    for c in sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")):
        exe = c
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=exe, args=["--allow-file-access-from-files"]) if exe else pw.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto(f"file://{out_dir}/{name}.html"); pg.wait_for_timeout(600)
        pg.evaluate("document.fonts.ready")
        pg.screenshot(path=str(out_dir / f"{name}.png"))
        b.close()
    print("rendered", out_dir / f"{name}.png")

main()
