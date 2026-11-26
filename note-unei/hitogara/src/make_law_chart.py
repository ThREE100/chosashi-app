"""by_law.json（count_by_law.py の出力）から、法令ごとの「広く浅い／狭く深い」の図をHTMLで組み、Chromiumで書き出す。
左の灰色の棒＝解説に出てきた条文の種類の数、重ねた濃い棒＝そのうち半分以上の年度で出た条文の数。
使い方：python3 note-unei/hitogara/src/make_law_chart.py <by_law.json> <出力PNG> [--ig]
"""
import json, argparse, html, os, glob
from playwright.sync_api import sync_playwright
SHORT = {"不動産登記法":"不動産登記法","不動産登記令":"不動産登記令","不動産登記規則":"不動産登記規則","不動産登記事務取扱手続準則":"準則",
         "民法":"民法","区分所有法":"区分所有法","土地家屋調査士法":"調査士法","土地家屋調査士法施行規則":"調査士法施行規則"}
COLOR = {"民法":"#e8a05c"}
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("--ig", action="store_true")
    a = ap.parse_args()
    d = json.load(open(a.src, encoding="utf-8")); rows = d["by_law"]; half = d["half"]; Y = d["years_total"]
    mx = max(r["kinds"] for r in rows)
    W, H = (1080, 1440) if a.ig else (1280, None)
    fs = 34 if a.ig else 30
    body = ""
    for r in rows:
        c = COLOR.get(r["law"], "#3b78c2")
        body += f'''<div class="row"><div class="nm">{html.escape(SHORT[r["law"]])}</div>
<div class="bw"><div class="all" style="width:{r["kinds"]/mx*100:.1f}%"></div><div class="deep" style="width:{r["half_or_more"]/mx*100:.1f}%;background:{c}"></div></div>
<div class="v"><b>{r["half_or_more"]}</b>／{r["kinds"]}条</div></div>'''
    pad = "72px 54px" if a.ig else "48px 56px"
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#fbf8f1;font-family:"Noto Sans CJK JP";color:#1f2d3d}}
.wrap{{width:{W}px;{f"height:{H}px;" if H else ""}box-sizing:border-box;padding:{pad};display:flex;flex-direction:column}}
h1{{font-size:{fs+16}px;margin:0 0 10px;line-height:1.3}} .sub{{font-size:{fs-4}px;color:#55606e;margin-bottom:28px;line-height:1.5}}
.rows{{flex:1;display:flex;flex-direction:column;justify-content:space-around}}
.row{{display:flex;align-items:center;gap:16px;margin:12px 0}}
.nm{{width:{300 if a.ig else 320}px;font-size:{fs}px;font-weight:700;flex:none}}
.bw{{flex:1;height:38px;position:relative}} .all{{position:absolute;left:0;top:0;height:100%;background:#e0dacd;border-radius:8px}}
.deep{{position:absolute;left:0;top:0;height:100%;border-radius:8px;min-width:0}}
.v{{width:{170 if a.ig else 170}px;text-align:right;font-size:{fs-2}px;flex:none}} .v b{{font-size:{fs+6}px}}
.leg{{margin-top:26px;font-size:{fs-6}px;color:#55606e;line-height:1.7}} .sw{{display:inline-block;width:22px;height:22px;border-radius:4px;vertical-align:-4px;margin:0 6px 0 0}}
</style></head><body><div class="wrap"><h1>法令ごとの「広く浅い」と「狭く深い」</h1>
<div class="sub">解説に出てきた条文の種類と、そのうち{Y}年度の半分（{half}年度）以上で出てきた条文の数</div>
<div class="rows">{body}</div>
<div class="leg"><div><span class="sw" style="background:#e0dacd"></span>解説に出てきた条文の種類（右の数字の「／」の後ろ）</div><div><span class="sw" style="background:#3b78c2"></span><span class="sw" style="background:#e8a05c"></span>そのうち{half}年度以上で出た条文（右の太い数字。青＝不動産登記の法令、橙＝民法）</div></div>
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
