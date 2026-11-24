"""ranking.json から「何年度で出たか」の横棒グラフをHTMLで組み、Chromiumで書き出す（画像生成AIは使わない＝誤字ゼロ）。
使い方：python3 note-unei/hitogara/src/make_bar_chart.py <ranking.json> <出力PNG> [--top 10] [--ig]
--ig を付けると Instagram 用 3:4（1080×1440）、付けないと note 用（1280×可変）。
"""
import json, sys, argparse, html, os, glob
from playwright.sync_api import sync_playwright
SHORT = {"不動産登記法":"不登法","不動産登記令":"令","不動産登記規則":"規則","不動産登記事務取扱手続準則":"準則",
         "民法":"民法","区分所有法":"区分所有法","土地家屋調査士法":"調査士法"}
COLOR = {"民法":"#e8a05c"}  # 権利・民法＝薄い橙、それ以外（不動産登記の法令（法・令・規則・準則））＝青
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--ig", action="store_true"); ap.add_argument("--title", default="440問の解説で、根拠に引いた条文")
    ap.add_argument("--sub", default="H17〜R8の22年度のうち、何年度で出てきたか")
    a = ap.parse_args()
    d = json.load(open(a.src, encoding="utf-8")); rows = d["ranking"][:a.top]; Y = d["years_total"]
    W, H = (1080, 1440) if a.ig else (1280, None)
    bars = ""
    for i, r in enumerate(rows, 1):
        pct = r["years"] / Y * 100; c = COLOR.get(r["law"], "#3b78c2")
        name = f'{SHORT.get(r["law"], r["law"])} 第{r["article"]}条'
        bars += f'''<div class="row"><div class="rk">{i}</div><div class="nm">{html.escape(name)}</div>
<div class="bw"><div class="bar" style="width:{pct:.1f}%;background:{c}"></div></div><div class="v">{r["years"]}年度</div></div>'''
    pad = "72px 54px" if a.ig else "48px 56px"
    fs = 38 if a.ig else 34
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#fbf8f1;font-family:"Noto Sans CJK JP";color:#1f2d3d}}
.wrap{{width:{W}px;{f"height:{H}px;" if H else ""}box-sizing:border-box;padding:{pad};display:flex;flex-direction:column}}
h1{{font-size:{fs+14}px;margin:0 0 10px;line-height:1.3}} .sub{{font-size:{fs-6}px;color:#55606e;margin-bottom:30px}}
.rows{{flex:1;display:flex;flex-direction:column;justify-content:space-around}}
.row{{display:flex;align-items:center;gap:16px;margin:10px 0}}
.rk{{width:52px;height:52px;border-radius:50%;background:#1f2d3d;color:#fff;font-size:28px;display:flex;align-items:center;justify-content:center;flex:none}}
.nm{{width:{330 if a.ig else 360}px;font-size:{fs-4}px;font-weight:700;flex:none}}
.bw{{flex:1;height:34px;background:#e6e1d6;border-radius:17px;overflow:hidden}} .bar{{height:100%;border-radius:17px}}
.v{{width:{120 if a.ig else 130}px;text-align:right;font-size:{fs-6}px;flex:none}}
.leg{{margin-top:26px;font-size:{fs-12}px;color:#55606e}} .sw{{display:inline-block;width:22px;height:22px;border-radius:4px;vertical-align:-4px;margin:0 6px 0 18px}}
</style></head><body><div class="wrap"><h1>{html.escape(a.title)}</h1><div class="sub">{html.escape(a.sub)}</div>
<div class="rows">{bars}</div>
<div class="leg"><span class="sw" style="background:#3b78c2;margin-left:0"></span>不動産登記の法令（法・令・規則・準則）<span class="sw" style="background:#e8a05c"></span>民法</div>
</div></body></html>'''
    hp = os.path.splitext(a.out)[0] + ".html"; open(hp, "w", encoding="utf-8").write(doc)
    with sync_playwright() as p:
        exe = (sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome')) or [None])[0]
        b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H or 800}, device_scale_factor=1)
        pg.goto("file://" + os.path.abspath(hp)); pg.wait_for_timeout(300)
        pg.screenshot(path=a.out, full_page=not a.ig); b.close()
    print("wrote", a.out)
if __name__ == "__main__":
    main()
