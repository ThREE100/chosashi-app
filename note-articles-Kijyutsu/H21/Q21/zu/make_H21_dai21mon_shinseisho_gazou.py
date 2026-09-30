"""平成21年度 第21問（土地）答案用紙（その1）の画像（完成形・問4の添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H21_dai21mon_toukishinseisho_gazou.md` どおり。平成21年度の答案用紙（その1）は申請書の様式ではなく、
  問1（I点・J点・L点のX座標・Y座標の表）→ 問2（見取図(ロ)部分の面積）→ 問3（見取図(ハ)部分の面積）
  → 問4（登記の順番・登記の目的・登記の原因及び日付・添付情報の4列×2行の表）の順。縦長（横1200px）
- 添削　：`../prompt_H21_dai21mon_toukishinseisho_machigai.md` どおり。問4の表だけを取り出し、①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

様式の部品（CSS）は `../../../H24/Q21/zu/make_H24_dai21mon_shinseisho_gazou.py` にそろえた。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・Noto Sans CJK JP）
実行: python3 note-articles-Kijyutsu/H21/Q21/zu/make_H21_dai21mon_shinseisho_gazou.py [出力フォルダ]
"""
import glob
import os
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

INK = '#1a3a8f'      # 記入（濃い青）
RED = '#d0021b'      # 添削（赤ペン）
GREEN = '#2e9e44'    # 正解の枠

CSS = f'''
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: #fff; width: 1200px; font-family: "Noto Serif CJK JP", "IPAMincho", serif; color: #111; }}
.page {{ padding: 60px 70px 40px; min-height: 1650px; display: flex; flex-direction: column; }}
.page .caption {{ margin-top: auto; padding-top: 30px; }}
.title {{ text-align: center; font-size: 36px; letter-spacing: 0.5em; margin: 0 0 40px 0.5em; }}
.q {{ font-size: 26px; font-weight: bold; margin: 26px 0 12px; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
table.xy, table.area {{ border-collapse: collapse; border: 2.5px solid #111; margin-bottom: 18px; table-layout: fixed; }}
table.xy {{ width: 640px; }}
table.area {{ width: 640px; }}
table.xy td, table.area td {{ border: 1.5px solid #111; text-align: center; font-size: 22px; }}
table.xy td.h, table.area td.h {{ height: 50px; }}
table.xy td.v, table.area td.v {{ height: 82px; font-size: 28px; }}
table.t4 {{ width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; }}
table.t4 td {{ border: 1.5px solid #111; font-size: 21px; padding: 10px 12px; vertical-align: top; }}
table.t4 td.h {{ text-align: center; height: 50px; vertical-align: middle; font-size: 20px; }}
table.t4 td.n {{ text-align: center; vertical-align: top; padding-top: 16px; }}
table.t4 td .ink {{ font-size: 22px; line-height: 1.6; }}
table.t4 td.cell {{ height: 190px; white-space: normal; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 30px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 50px 30px; border-bottom: 2px solid #bbb; }}
.panel:last-of-type {{ border-bottom: none; }}
.ptitle {{ font-size: 26px; font-weight: bold; margin-bottom: 14px; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.ptitle.ng {{ color: #777; }}
.ptitle.fix {{ color: {RED}; }}
.ptitle.ok {{ color: {GREEN}; }}
.omit {{ color: #888; font-size: 18px; margin-bottom: 10px; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.red {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; }}
.strike {{ text-decoration: line-through; text-decoration-color: {RED}; text-decoration-thickness: 3px; }}
.good table.t4 {{ outline: 4px solid rgba(46, 158, 68, 0.35); outline-offset: 4px; }}
.bubbles {{ margin-top: 16px; }}
.bubble {{ position: relative; display: block; border: 2px solid {RED}; border-radius: 10px; color: {RED}; padding: 8px 14px;
           font-size: 19px; margin: 12px 0 0 0; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; background: #fff; }}
.bubble::before {{ content: ""; position: absolute; top: -12px; left: 40px; border-left: 10px solid transparent;
                   border-right: 10px solid transparent; border-bottom: 12px solid {RED}; }}
.chk {{ position: absolute; right: -8px; top: -46px; }}
'''


def ink(s):
    return f'<span class="ink">{s}</span>'


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def br(*lines):
    return '<br>'.join(lines)


# ---- 記入データ（プロンプトの記入データと一字一句同じ） ----
Q1 = [('I', '507.07m', '485.26m'), ('J', '509.07m', '485.26m'), ('L', '509.07m', '495.56m')]
Q2 = '2.43㎡'
Q3 = '3.82㎡'
ROWS = [
    ('1', '土地地目変更登記', ['②③平成21年8月3日地目変更'], ['代理権限証明情報']),
    ('2', '土地分筆登記', ['③100番1、100番3、100番4に分筆', '100番1から分筆', '100番1から分筆'],
     ['地積測量図', '抵当権消滅承諾証明情報', '代理権限証明情報']),
]


def t4(rows):
    """問4の表（登記の順番・登記の目的・登記の原因及び日付・添付情報）。rows の各セルは HTML 文字列。"""
    head = ('<tr><td class="h" style="width:12%">登記の順番</td><td class="h" style="width:22%">登記の目的</td>'
            '<td class="h" style="width:36%">登記の原因及び日付</td><td class="h" style="width:30%">添付情報</td></tr>')
    body = ''.join(f'<tr><td class="n">{n}</td><td class="cell">{a}</td><td class="cell">{b}</td><td class="cell">{c}</td></tr>'
                   for n, a, b, c in rows)
    return f'<table class="t4">{head}{body}</table>'


def rows_ink(rows):
    return [(n, ink(a), ink(br(*b)), ink(br(*c))) for n, a, b, c in rows]


q1 = ''.join(f'<table class="xy"><tr><td class="h">{p}点のX座標</td><td class="h">{p}点のY座標</td></tr>'
             f'<tr><td class="v">{ink(x)}</td><td class="v">{ink(y)}</td></tr></table>' for p, x, y in Q1)
kansei = page(f'''<div class="page">
<div class="title">第21問答案用紙（その1）</div>
<div class="q">問1</div>{q1}
<div class="q">問2</div><table class="area"><tr><td class="h">見取図(ロ)部分の面積</td></tr><tr><td class="v">{ink(Q2)}</td></tr></table>
<div class="q">問3</div><table class="area"><tr><td class="h">見取図(ハ)部分の面積</td></tr><tr><td class="v">{ink(Q3)}</td></tr></table>
<div class="q">問4</div>{t4(rows_ink(ROWS))}
<div class="caption">平成21年度 土地家屋調査士試験 第21問 答案用紙（その1） 解答例</div>
</div>''')


def fixed(new, old):
    return f'<span class="red">{new}</span> <span class="ink strike">{old}</span>'


CHK = ('<svg class="chk" width="44" height="40" viewBox="0 0 44 40"><path d="M4 22 L16 34 L40 6" fill="none" '
       f'stroke="{GREEN}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ng_rows = [('1', ink('土地地目変更登記'), ink('②平成21年8月3日地目変更'), ink('代理権限証明情報')),
           ('2', ink('土地分筆登記'), ink(br('③100番1、100番3に分筆', '100番1から分筆')), ink(br('地積測量図', '代理権限証明情報')))]
fix_rows = [('1', ink('土地地目変更登記'), '<span class="red">②③</span>' + ink('<span class="strike">②</span>平成21年8月3日地目変更'),
             ink('代理権限証明情報')),
            ('2', ink('土地分筆登記'),
             ink('③100番1、') + '<span class="red">100番3、100番4</span>' + ink('に分筆<br>100番1から分筆') + '<br><span class="red">100番1から分筆</span>',
             ink('地積測量図') + '<br><span class="red">抵当権消滅承諾証明情報</span><br>' + ink('代理権限証明情報'))]
BUB = ['地目が宅地になると地積の表し方（1㎡単位→小数第2位まで）も変わるので③も付ける',
       '（ロ）と（ハ）は離れているので1筆にできない。100番1・100番3・100番4の3筆（原因は3行）',
       '分筆後の（ロ）（ハ）の1番抵当権を消す承諾書一式（不動産登記法第40条）を添付']
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div><div class="omit">（問1〜問3の欄は省略）</div>{t4(ng_rows)}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div><div class="omit">（問1〜問3の欄は省略）</div>{t4(fix_rows)}
<div class="bubbles">{''.join(f'<div class="bubble">{b}</div>' for b in BUB)}</div></div>
<div class="panel"><div class="ptitle ok">③正解</div><div class="omit">（問1〜問3の欄は省略）</div>
<div class="good" style="position:relative">{t4(rows_ink(ROWS))}{CHK}</div></div>
<div class="caption" style="margin:10px 0 30px">平成21年度 第21問｜地目変更は②③、分筆は3筆、抵当権消滅承諾証明情報</div>''')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 800})
    for name, html in [('H21_dai21mon_toukishinseisho_kansei', kansei), ('H21_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（要確認）'))
    browser.close()
