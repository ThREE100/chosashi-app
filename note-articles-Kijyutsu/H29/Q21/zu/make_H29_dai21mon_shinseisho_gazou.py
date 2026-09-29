"""平成29年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H29_dai21mon_toukishinseisho_gazou.md`（基本フォーム＋記入データ）どおり。縦長（横1200px）
- 添削　：`../prompt_H29_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

見本は `R6/Q21/zu/make_R6_dai21mon_shinseisho_gazou.py`。欄の順序・所在の2段・土地の表示の最後の空欄の段は、平成29年度の答案用紙（第3欄）に合わせた。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・IPAゴシック。Noto があればそちらを優先）
実行: python3 note-articles-Kijyutsu/H29/Q21/zu/make_H29_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
.page {{ padding: 80px 70px 40px; min-height: 1750px; display: flex; flex-direction: column; }}
.page .caption {{ margin-top: auto; padding-top: 30px; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 56px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 32px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 26px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.plain {{ font-size: 22px; margin: 4px 0 26px; }}
.dairi {{ display: flex; font-size: 22px; margin-bottom: 26px; }}
.dairi .lab {{ padding-top: 0; }}
.dairi .ryaku {{ flex: 1; text-align: center; }}
.sign {{ text-align: right; font-size: 22px; margin-top: 16px; letter-spacing: 0.3em; }}
table.land {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.land td {{ border: 1.5px solid #111; font-size: 22px; padding: 0 12px; height: 92px; vertical-align: middle; }}
table.land.compact td.vert {{ letter-spacing: 0.05em; font-size: 18px; }}
table.land td.head {{ height: 50px; text-align: center; font-size: 20px; white-space: nowrap; padding: 0 4px; }}
table.land td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.land td.shozai-lab {{ text-align: center; }}
table.land td.shozai {{ height: 52px; }}
table.land td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 6px; }}
table.land td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 6px; }}
table.land td.chimoku {{ text-align: center; }}
table.land td.gen {{ line-height: 1.5; }}
table.land td.blank {{ height: 70px; }}
table.land td .ink, .box .ink {{ font-size: 26px; }}
table.land td.gen .ink {{ font-size: 23px; }}
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
.upfix {{ position: absolute; margin-top: -34px; font-size: 24px; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; left: 60px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: -12px 0 20px 170px; }}
.bubrow.table {{ margin: 14px 0 0 330px; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.okrow {{ position: relative; }}
.check {{ position: absolute; right: -8px; top: -30px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def land_table(rows, n_rows=6, shozai='', compact=False, tail=True):
    """土地の表示の表（平成29年度の答案用紙：所在2段、記入行 n_rows 行、最後に区切りのない空欄の段）。
    rows: [(地番, 地目, 整数部, 小数部, 登記原因)]。各値は HTML（記入部分は呼び出し側で .ink を付ける）"""
    n_vert = 2 + 1 + n_rows + (1 if tail else 0)
    h = [f'<table class="land{" compact" if compact else ""}"><colgroup><col style="width:6%"><col style="width:22%">'
         '<col style="width:11%"><col style="width:12%"><col style="width:7%"><col style="width:42%"></colgroup>',
         f'<tr><td class="vert" rowspan="{n_vert}">土地の表示</td><td class="shozai-lab" rowspan="2">所　在</td>'
         f'<td class="shozai" colspan="4">{shozai}</td></tr>',
         '<tr><td class="shozai" colspan="4"></td></tr>',
         '<tr><td class="head">①地　　番</td><td class="head">②地　目</td><td class="head" colspan="2">③地　積　（m²）</td>'
         '<td class="head">登記原因及びその日付</td></tr>']
    for i in range(n_rows):
        c, m, a, b, g = rows[i] if i < len(rows) else ('', '', '', '', '')
        h.append(f'<tr><td>{c}</td><td class="chimoku">{m}</td><td class="int">{a}</td><td class="dec">{b}</td>'
                 f'<td class="gen">{g}</td></tr>')
    if tail:
        h.append('<tr><td class="blank" colspan="5"></td></tr>')
    h.append('</table>')
    return ''.join(h)


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---- 完成形（記入データは prompt_H29_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '平成29年８月18日　申請　Ａ地方法務局'
SHOZAI = 'Ａ市Ｂ町字Ｃ'
HIS = '（被相続人　甲野一郎）'
TARO = 'Ａ市Ｂ町100番地　甲野太郎'
JIRO = 'Ａ市Ｄ町210番地　甲野次郎'
APPLICANT = f'{ink(HIS)}<br>{ink("相続人　" + TARO)}<br>{ink("　　　　" + JIRO)}'
ROWS = [(ink('100番'), ink('宅地'), ink('297'), ink('52'), ''),
        (ink('（イ）100番１'), '', ink('146'), ink('62'), f'{ink("③錯誤")}<br>{ink("①③100番１、100番２に分筆")}'),
        (ink('（ロ）100番２'), ink('宅地'), ink('153'), ink('22'), ink('100番から分筆'))]
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('土地地積更正・分筆登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:120px">{ink('地積測量図　相続証明書　代理権限証書')}</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink('金2,000円')}</div></div>
<div class="plain">{DATE}</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:150px">{APPLICANT}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{land_table(ROWS, shozai=ink(SHOZAI))}
<div class="sign">土地家屋調査士　法 務　民 子</div>
<div class="caption">平成29年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----
def snippet(applicant_html, row1, box_h, bubble1='', bubble2='', good=False):
    """答案用紙の順序（申請の日付と提出先 → 申請人 → 代理人 → 土地の表示）どおりに、申請人欄と土地の表示の1行目を描く。"""
    box_cls = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return f'''<div class="plain">{DATE}</div>
<div class="row okrow"><div class="lab">申　　請　　人</div><div class="box{box_cls}" style="height:{box_h}px">{applicant_html}</div>{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble1}</span></div>' if bubble1 else ''}
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="{'good' if good else ''}" style="position:relative">{land_table([row1], n_rows=1, shozai=ink(SHOZAI), compact=True, tail=False)}{chk if good else ''}</div>
{f'<div class="bubrow table"><span class="bubble">{bubble2}</span></div>' if bubble2 else ''}'''


ng_panel = snippet(f'{ink(TARO)}<br>{ink(JIRO)}', (ink('100番'), ink('宅地'), ink('115'), ink('70'), ''), 110)
fix_panel = snippet(
    f'<span class="red">（被相続人　甲野一郎）</span><br><span class="red">相続人　</span>{ink(TARO)}<br>'
    f'<span class="red" style="visibility:hidden">相続人　</span>{ink(JIRO)}',
    (ink('100番'), ink('宅地'),
     f'<span class="red upfix">297</span><span class="ink strike">115</span>',
     f'<span class="red upfix">52</span><span class="ink strike">70</span>', ''),
    150,
    bubble1='登記名義人は亡くなった甲野一郎。相続人が法第30条で申請する！',
    bubble2='分筆するのは合筆した後の100番。地積は3筆の合計297.52')
ok_panel = snippet(APPLICANT, (ink('100番'), ink('宅地'), ink('297'), ink('52'), ''), 150, good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成29年度 第21問｜申請人は被相続人と相続人2人、分筆前の地積は合筆後の297.52</div>''')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 800})
    for name, html in [('H29_dai21mon_toukishinseisho_kansei', kansei), ('H29_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（要確認）'))
    browser.close()
