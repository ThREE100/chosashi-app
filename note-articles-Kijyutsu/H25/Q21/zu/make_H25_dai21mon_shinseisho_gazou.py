"""平成25年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H25_dai21mon_toukishinseisho_gazou.md`（基本フォーム＋記入データ）どおり。縦長（横1200px）
- 添削　：`../prompt_H25_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第1欄（問1のB点・F点の座標値）・第2欄（問2の説明）：申請書でない解答欄も、答案用紙の欄の形で別の画像にする（横1200px）。
  欄の形は試験の答案用紙（`public/kijutsu/H25-tochi/a1.webp`）どおり。第1欄は「B点・F点」×「X座標（m）・Y座標（m）」の表、
  第2欄は「山川一郎及び海川二郎に対して説明すべき内容」の大きな記述枠

見本は `../../../R6/Q21/zu/make_R6_dai21mon_shinseisho_gazou.py`。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・IPAゴシック。Noto があればそちらを優先）
実行: python3 note-articles-Kijyutsu/H25/Q21/zu/make_H25_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
table.land td {{ border: 1.5px solid #111; font-size: 22px; padding: 6px 12px; height: 110px; vertical-align: middle; }}
table.land tr.first td {{ height: 70px; }}
.box.fix {{ line-height: 1.75; }}
table.land td.head {{ height: 50px; text-align: center; font-size: 20px; }}
table.land td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.land td.shozai-lab {{ text-align: center; height: 76px; }}
table.land td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 6px; }}
table.land td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 6px; }}
table.land td.chimoku {{ text-align: center; }}
table.land td .ink, .box .ink {{ font-size: 26px; }}
table.land td.gen .ink, table.land td.gen .red {{ font-size: 23px; line-height: 1.5; }}
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
.bubrow.table {{ margin: 14px 0 0 0; display: flex; flex-direction: column; gap: 14px; align-items: flex-start; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.okrow {{ position: relative; }}
.check {{ position: absolute; right: -8px; top: -30px; }}
.addmark {{ position: absolute; margin-left: -30px; margin-top: -14px; font-size: 24px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def land_table(rows, n_rows=3, shozai=''):
    """土地の表示の表（答案用紙どおり記入行は3行。1行目は低い）。rows: [(地番, 地目, 整数部, 小数部, 登記原因)]"""
    h = ['<table class="land"><colgroup><col style="width:6%"><col style="width:17%"><col style="width:14%">'
         '<col style="width:12%"><col style="width:7%"><col style="width:44%"></colgroup>',
         f'<tr><td class="shozai-lab" colspan="2">所　在</td><td colspan="4">{shozai}</td></tr>',
         f'<tr><td class="vert" rowspan="{n_rows + 1}">土地の表示</td><td class="head">①地　　番</td>'
         '<td class="head">②地　　目</td><td class="head" colspan="2">③地　積　（m²）</td>'
         '<td class="head">登記原因及びその日付</td></tr>']
    for i in range(n_rows):
        c, m, a, b, g = rows[i] if i < len(rows) else ('', '', '', '', '')
        h.append(f'<tr class="{"first" if i == 0 else ""}"><td>{c}</td><td class="chimoku">{m}</td><td class="int">{a}</td>'
                 f'<td class="dec">{b}</td><td class="gen">{g}</td></tr>')
    h.append('</table>')
    return ''.join(h)


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---- 完成形（記入データは prompt_H25_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '平成25年８月23日　申請　Ａ地方法務局'
APPLICANT = 'Ａ市Ｂ町三丁目４番５号　海川二郎'
SHOZAI = 'Ａ市Ｂ町二丁目'
GEN_I = '平成25年６月21日一部地目変更<br>①③5番１、5番２に分筆'
ROWS = [('5番', '雑種地', '255', '', ''),
        ('（イ）5番１', '', '141', '', GEN_I),
        ('（ロ）5番２', '宅地', '113', '90', '5番から分筆')]
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('土地一部地目変更・分筆登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:62px">{ink('地積測量図　代理権限証書')}</div></div>
<div class="plain">{DATE}</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:110px">{ink(APPLICANT)}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink('金2,000円')}</div></div>
<div style="height:14px"></div>
{land_table([tuple(ink(v) for v in r) for r in ROWS], shozai=ink(SHOZAI))}
<div class="caption">平成25年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----
WRONG_APPLICANT = 'Ａ市Ｂ町二丁目20番１号　山川一郎'
WRONG_GEN_I = '平成25年６月21日一部地目変更<br>③5番１、5番２に分筆'
B1 = '申請人は所有権の登記名義人（土地の所有者）。借主・建物の所有者ではない！'
B2 = '（イ）は分筆で変わる事項だけ。地目は変わらないので空欄、地番が変わるので①も付ける'
B3 = '（ロ）は座標法で求積（113.9083）。255から引き算しない'


def snippet(applicant_html, rows, bubble1='', bubbles2=(), good=False, fix=False):
    """答案用紙の順序（申請の日付と提出先 → 申請人 → 代理人 → 土地の表示）どおりに、申請人欄と土地の表示を描く。"""
    box_cls = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    b2 = ''.join(f'<span class="bubble">{b}</span>' for b in bubbles2)
    return f'''<div class="plain">{DATE}</div>
<div class="row okrow"><div class="lab">申　　請　　人</div><div class="box{box_cls}{' fix' if fix else ''}" style="height:{'110' if bubble1 else '84'}px">{applicant_html}</div>{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble1}</span></div>' if bubble1 else ''}
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="{'good' if good else ''}" style="position:relative">{land_table(rows, shozai=ink(SHOZAI))}{chk if good else ''}</div>
{f'<div class="bubrow table">{b2}</div>' if b2 else ''}'''


ng_rows = [tuple(ink(v) for v in ('5番', '雑種地', '255', '', '')),
           tuple(ink(v) for v in ('（イ）5番１', '雑種地', '141', '', WRONG_GEN_I)),
           tuple(ink(v) for v in ('（ロ）5番２', '宅地', '113', '30', '5番から分筆'))]
fix_rows = [ng_rows[0],
            (ink('（イ）5番１'), '<span class="ink strike">雑種地</span>', ink('141'), '',
             '<span class="ink">平成25年６月21日一部地目変更</span><br>'
             '<span class="red" style="font-size:26px;font-weight:bold">①</span><span class="ink">③5番１、5番２に分筆</span>'),
            (ink('（ロ）5番２'), ink('宅地'), ink('113'),
             f'<span class="red" style="font-size:24px;position:absolute;margin-top:-34px">90</span><span class="ink strike">30</span>',
             ink('5番から分筆'))]
ng_panel = snippet(ink(WRONG_APPLICANT), ng_rows)
fix_panel = snippet(
    f'<span class="ink strike">{WRONG_APPLICANT}</span><br><span class="red">{APPLICANT}</span>', fix_rows,
    bubble1=B1, bubbles2=(B2, B3), fix=True)
ok_panel = snippet(ink(APPLICANT), [tuple(ink(v) for v in r) for r in ROWS], good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成25年度 第21問｜申請人は土地の所有者、（イ）の原因は①③、（ロ）は座標法で求積</div>''')

# ---- 第1欄・第2欄（申請書でない解答欄。2026-10-02追加） ----
RAN_CSS = '''
.ran {{ padding: 60px 60px 40px; }}
.ranhead {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin-bottom: 14px; }}
table.zahyo {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.zahyo td {{ border: 1.5px solid #111; font-size: 24px; height: 96px; text-align: center; vertical-align: middle; }}
table.zahyo tr.h td {{ height: 60px; font-size: 22px; }}
table.zahyo td .ink {{ font-size: 30px; }}
.kijutsu {{ border: 3px solid #111; padding: 26px 30px; min-height: 520px; font-size: 25px; line-height: 2.0; }}
'''.format()
DAI1 = [('B点', '151.63', '171.42'), ('F点', '138.08', '170.37')]
DAI2 = ('地目は、土地の主な用途による分類であり、土地が現にどのように利用されているかを登記記録によって公示するための登記事項である。'
        '一筆の土地には一つの地目しか登記することができない。'
        '本件土地は、平成25年6月21日に建物が完成し、ブロック塀の西側は建物の敷地（宅地）、東側は資材置場（雑種地）として区画して利用されており、'
        '一筆の土地の一部が別の地目になっている。'
        'このままでは登記記録が実際の利用形態を公示しないので、所有者である海川二郎が、西側部分を分筆してその部分の地目を宅地に変更する'
        '土地一部地目変更・分筆登記を申請する必要がある。')


def ran_page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}{RAN_CSS}</style></head><body>{body}</body></html>'


rows1 = ''.join(f'<tr><td>{n}</td><td>{ink(x)}</td><td>{ink(y)}</td></tr>' for n, x, y in DAI1)
dai1 = ran_page(f'''<div class="ran"><div class="ranhead">第１欄　Ｂ点及びＦ点の座標値</div>
<table class="zahyo"><colgroup><col style="width:30%"><col style="width:35%"><col style="width:35%"></colgroup>
<tr class="h"><td></td><td>Ｘ座標（m）</td><td>Ｙ座標（m）</td></tr>{rows1}</table>
<div class="caption">平成25年度 土地家屋調査士試験 第21問 第1欄（問1）解答例</div></div>''')
dai2 = ran_page(f'''<div class="ran"><div class="ranhead">第２欄　山川一郎及び海川二郎に対して説明すべき内容</div>
<div class="kijutsu">{ink(DAI2)}</div>
<div class="caption">平成25年度 土地家屋調査士試験 第21問 第2欄（問2）解答例</div></div>''')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 200})
    for name, html in [('H25_dai21mon_dai1ran_kansei', dai1), ('H25_dai21mon_dai2ran_kansei', dai2),
                       ('H25_dai21mon_toukishinseisho_kansei', kansei), ('H25_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（第1欄・第2欄はそれでよい）'))
    browser.close()
