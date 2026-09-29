"""平成30年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H30_dai21mon_toukishinseisho_gazou.md`（答案用紙の順序どおり）。縦長（横1200px）
- 添削　：`../prompt_H30_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

見本は `../../../R6/Q21/zu/make_R6_dai21mon_shinseisho_gazou.py`。平成30年度の答案用紙は、項目の順序が
「登記の目的 → 添付書類 → 登録免許税 → 申請人 → 代理人 → 申請の日付と提出先 → 土地の表示」で、記入行は4行。

必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto CJK。なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/H30/Q21/zu/make_H30_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
.page {{ padding: 80px 70px 40px; min-height: 1650px; display: flex; flex-direction: column; }}
.page .caption {{ margin-top: auto; padding-top: 30px; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 56px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 32px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 26px; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.plain {{ font-size: 22px; margin: 4px 0 26px; }}
.dairi {{ display: flex; font-size: 22px; margin-bottom: 26px; }}
.dairi .lab {{ padding-top: 0; }}
.dairi .ryaku {{ flex: 1; text-align: center; }}
table.land {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.land td {{ border: 1.5px solid #111; font-size: 22px; padding: 6px 12px; height: 100px; vertical-align: middle;
                 line-height: 1.5; }}
table.land td.head {{ height: 50px; text-align: center; font-size: 20px; }}
table.land td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.land.compact td.vert {{ letter-spacing: 0.3em; font-size: 20px; }}
table.land td.shozai-lab {{ text-align: center; height: 76px; }}
table.land td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 6px; }}
table.land td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 6px; }}
table.land td.chimoku {{ text-align: center; }}
table.land td .ink, .box .ink {{ font-size: 24px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 30px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 70px 30px; border-bottom: 2px solid #bbb; }}
.panel:last-of-type {{ border-bottom: none; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.strike {{ position: relative; }}
.strike::after {{ content: ""; position: absolute; left: -4px; right: -4px; top: 52%; border-top: 3px solid {RED};
                  transform: rotate(-2deg); }}
.red {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; left: 60px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: -12px 0 20px 170px; }}
.bubrow.table {{ margin: 14px 0 0 420px; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.okrow {{ position: relative; }}
.check {{ position: absolute; right: -8px; top: -30px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def land_table(rows, n_rows=4, shozai='', compact=False):
    """土地の表示の表。rows: [(地番, 地目, 整数部, 小数部, 登記原因)]。各値は HTML（記入部分は呼び出し側で .ink を付ける）"""
    h = [f'<table class="land{" compact" if compact else ""}"><colgroup><col style="width:6%"><col style="width:20%"><col style="width:12%">'
         '<col style="width:13%"><col style="width:7%"><col style="width:42%"></colgroup>',
         f'<tr><td class="shozai-lab" colspan="2">所　在</td><td colspan="4">{shozai}</td></tr>',
         f'<tr><td class="vert" rowspan="{n_rows + 1}">土地の表示</td><td class="head">①地　　番</td>'
         '<td class="head">②地　　目</td><td class="head" colspan="2">③地　積　（m²）</td>'
         '<td class="head">登記原因及びその日付</td></tr>']
    for i in range(n_rows):
        c, m, a, b, g = rows[i] if i < len(rows) else ('', '', '', '', '')
        h.append(f'<tr><td style="white-space:nowrap">{c}</td><td class="chimoku">{m}</td><td class="int">{a}</td><td class="dec">{b}</td>'
                 f'<td>{g}</td></tr>')
    h.append('</table>')
    return ''.join(h)


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---- 完成形（記入データは prompt_H30_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '平成30年10月19日　申請　Ａ地方法務局'
APPLICANT = 'Ａ市Ｂ町三丁目13番１号　丙山次郎'
SHOZAI = 'Ａ市Ｂ町三丁目'
PURPOSE = '土地一部地目変更・分筆登記'
CAUSE_I = '平成30年10月１日一部地目変更<br>①③11番１、11番２に分筆'
ROWS = [('11番', '雑種地', '253', '', ''),
        ('（イ）11番１', '', '244', '', CAUSE_I),
        ('（ロ）11番２', '宅地', '9', '03', '11番から分筆')]
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink(PURPOSE)}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:170px">{ink('地積測量図　代理権限証書')}</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink('金2,000円')}</div></div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:96px">{ink(APPLICANT)}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="plain">{DATE}</div>
{land_table([tuple(ink(v) for v in r) for r in ROWS], shozai=ink(SHOZAI))}
<div class="caption">平成30年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----
WRONG_PURPOSE = '土地分筆登記'
WRONG_CAUSE = '③11番１、11番２に分筆'


def snippet(purpose_html, rows, bubble1='', bubble2='', good=False):
    """登記の目的の欄と、土地の表示の記入行1〜3を描く（間の欄は省き、申請の日付と提出先の1行だけ残す）。"""
    box_cls = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return f'''<div class="row okrow"><div class="lab">登記の目的</div><div class="box{box_cls}" style="height:{'100' if bubble1 else '62'}px;line-height:1.6">{purpose_html}</div>{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble1}</span></div>' if bubble1 else ''}
<div class="plain">{DATE}</div>
<div class="{'good' if good else ''}" style="position:relative">{land_table(rows, n_rows=3, shozai=ink(SHOZAI), compact=True)}{chk if good else ''}</div>
{f'<div class="bubrow table"><span class="bubble">{bubble2}</span></div>' if bubble2 else ''}'''


ng_rows = [tuple(ink(v) for v in ROWS[0]),
           (ink('（イ）11番１'), '', ink('244'), '', ink(WRONG_CAUSE)),
           (ink('（ロ）11番２'), ink('雑種地'), ink('9'), ink('03'), ink('11番から分筆'))]
fix_rows = [tuple(ink(v) for v in ROWS[0]),
            (ink('（イ）11番１'), '', ink('244'), '',
             f'<span class="ink strike">{WRONG_CAUSE}</span><br><span class="red">{CAUSE_I}</span>'),
            (ink('（ロ）11番２'), f'<span class="ink strike">雑種地</span><br><span class="red">宅地</span>', ink('9'),
             ink('03'), ink('11番から分筆'))]
ok_rows = [tuple(ink(v) for v in r) for r in ROWS]
ng_panel = snippet(ink(WRONG_PURPOSE), ng_rows)
fix_panel = snippet(f'<span class="ink strike">{WRONG_PURPOSE}</span><br><span class="red">{PURPOSE}</span>', fix_rows,
                    bubble1='売った細い部分は10月1日に宅地へ。一部地目変更も一緒に！',
                    bubble2='本番の11番は地番も変わるので①③。（ロ）は宅地')
ok_panel = snippet(ink(PURPOSE), ok_rows, good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成30年度 第21問｜細い部分は宅地に変わった。土地一部地目変更・分筆登記、本番の分筆は①③</div>''')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 800})
    for name, html in [('H30_dai21mon_toukishinseisho_kansei', kansei), ('H30_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（要確認）'))
    browser.close()
