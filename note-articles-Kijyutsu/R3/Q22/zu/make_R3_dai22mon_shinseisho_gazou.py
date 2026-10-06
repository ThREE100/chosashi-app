"""令和3年度 第22問（建物）登記申請書の画像（完成形・第2欄・「区分した建物の表示」の原因欄の添削）を、
HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形（第1欄）：`../prompt_R3_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  試験の答案用紙（A3横。左に登記申請書・一棟の建物の表示・敷地権の目的である土地の表示、右に区分した建物の表示欄（イ）・
  敷地権の表示・第2欄）の欄を、左の列 → 右の列の順に縦に積む。項目の順序は答案用紙の印刷どおり
  「登記の目的 → 添付書類 → 登録免許税 → 申請人 → 代理人（略） → 令和3年10月17日　申請　Ｅ地方法務局」。
  一棟の建物の表示の②床面積は、整数部｜小数部に分けたセルが左右に2つ（左に1階、右に2階）
  欄の形・欄の名前・印刷文字は試験の答案用紙（../touan_youshi/R3_dai22mon_touan_youshi.pdf の1ページ目）で確かめた。
- 第2欄：①登記の目的、②敷地権の割合（（あ）部分・（い）部分等）、③添付書類（答案用紙の右下の欄の形）
- 添削　：`../prompt_R3_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `R5/Q22/zu/make_R5_dai22mon_shinseisho_gazou.py`（区分建物の欄）と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/R3/Q22/zu/make_R3_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.page {{ padding: 60px 60px 40px; display: flex; flex-direction: column; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 40px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 24px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.dateline {{ font-size: 22px; margin: 2px 0 10px 0; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 20px; }}
.plainrow .ryaku {{ flex: 1; text-align: center; }}
.sec {{ font-size: 24px; margin: 34px 0 0; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 18px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.35em; padding: 0; font-size: 21px; }}
table.t td.lab2 {{ text-align: center; font-size: 18px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 76px; }}
table.t td.val {{ height: 56px; }}
table.t td.entry {{ height: 128px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
table.r2 td {{ height: 78px; font-size: 21px; }}
table.r2 td .ink {{ font-size: 22px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 34px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.dstrike {{ position: relative; }}
.dstrike::before, .dstrike::after {{ content: ""; position: absolute; left: -3px; right: -3px; border-top: 2.5px solid {RED}; }}
.dstrike::before {{ top: 42%; }} .dstrike::after {{ top: 60%; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5; line-height: 1.5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; right: 120px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: 16px 0 0; text-align: right; }}
.bubrow .bubble {{ text-align: left; }}
.note {{ margin-top: 12px; font-size: 19px; color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; background: #f1faf2; }}
.okwrap {{ position: relative; }}
.check {{ position: absolute; right: -14px; top: -22px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def br(*lines):
    return '<br>'.join(lines)


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def area(floors, cls='entry'):
    """床面積の整数部・小数部のセル。floors: [(階の表示, 整数部, 小数部)]"""
    ints = br(*[ink(f'{k}　{a}' if k else a) for k, a, _ in floors])
    decs = br(*[ink(b) for _, _, b in floors])
    return f'<td class="{cls} int">{ints}</td><td class="{cls} dec">{decs}</td>'


KOUZOU = '鉄骨造スレー<br>トぶき２階建'

# ---- 一棟の建物の表示（所在は1段。②床面積は左右2つのセル） ----
ITTOU = (
    '<table class="t"><colgroup><col style="width:5%"><col style="width:10%"><col style="width:14%">'
    '<col style="width:14%"><col style="width:6%"><col style="width:14%"><col style="width:6%"><col style="width:31%"></colgroup>'
    '<tr><td class="vert" rowspan="4">一棟の建物の表示</td>'
    f'<td class="lab2 val">所　在</td><td class="val" colspan="6">{ink("Ａ市Ｂ町三丁目５番地２")}</td></tr>'
    '<tr><td class="lab2 val" colspan="2">建物の名称</td><td class="val" colspan="5"></td></tr>'
    '<tr><td class="head" colspan="2">①構　造</td><td class="head" colspan="4">②床　面　積<br>'
    '<span style="display:inline-block;width:48%">m²</span><span style="display:inline-block;width:48%">m²</span></td>'
    '<td class="head">原因及びその日付</td></tr>'
    f'<tr><td class="entry center" colspan="2">{ink(KOUZOU)}</td>{area([("1階", "173", "00")])}{area([("2階", "176", "00")])}'
    '<td class="entry genin"></td></tr></table>')

SHIKICHI_MOKUTEKI = (
    '<table class="t"><colgroup><col style="width:5%"><col style="width:10%"><col style="width:25%"><col style="width:11%">'
    '<col style="width:12%"><col style="width:6%"><col style="width:31%"></colgroup>'
    '<tr><td class="vert" rowspan="3" style="font-size:18px;letter-spacing:0.05em">敷地権の目的である土地の表示</td>'
    '<td class="head">①土地<br>の符号</td><td class="head">②所在及び地番</td><td class="head">③地目</td>'
    '<td class="head" colspan="2">④地　積　m²</td><td class="head">原因及びその日付</td></tr>'
    f'<tr><td class="entry center">{ink("１")}</td><td class="entry">{ink("Ａ市Ｂ町三丁目<br>５番２")}</td>'
    f'<td class="entry center">{ink("宅地")}</td>{area([("", "366", "14")])}<td class="entry genin"></td></tr>'
    '<tr><td class="entry"></td><td class="entry"></td><td class="entry"></td><td class="entry int"></td>'
    '<td class="entry dec"></td><td class="entry"></td></tr></table>')

KUBUN_COLS = ('<colgroup><col style="width:5%"><col style="width:13%"><col style="width:8%"><col style="width:9%">'
              '<col style="width:10%"><col style="width:14%"><col style="width:12%"><col style="width:5%">'
              '<col style="width:24%"></colgroup>')
KUBUN_HEAD = ('<td class="head">家屋<br>番号</td><td class="head">建物の<br>名　称</td>'
              '<td class="head" style="font-size:15px">主である<br>建物又は<br>附属建物</td>'
              '<td class="head">①種類</td><td class="head">②構　造</td><td class="head" colspan="2">③床　面　積<br>m²</td>'
              '<td class="head">原因及び<br>その日付</td>')

GENIN1_OK = '５番２の１、<br>５番２の２に区分'
GENIN2_OK = '５番２から区分'
DATE = '令和３年10月17日'


def kubun_row(kaoku, kind, floors, genin):
    return (f'<tr><td class="entry">{kaoku}</td><td class="entry"></td><td class="entry"></td>'
            f'<td class="entry center">{kind}</td><td class="entry center">{ink(KOUZOU)}</td>{area(floors)}'
            f'<td class="entry genin">{genin}</td></tr>')


ROW1 = lambda g: kubun_row(ink('５番２'), ink('共同住宅'), [('1階', '173', '00'), ('2階', '176', '00')], g)  # noqa: E731
ROW2 = lambda g: kubun_row(ink('（イ）<br>Ｂ町三丁目<br>５番２の１'), ink('居宅'), [('1階', '82', '74'), ('2階', '84', '24')], g)  # noqa: E731

KUBUN = (f'<div class="sec">区分した建物の表示欄（イ）</div>'
         f'<table class="t">{KUBUN_COLS}<tr><td class="vert" rowspan="3">区分した建物の表示</td>{KUBUN_HEAD}</tr>'
         f'{ROW1(ink(GENIN1_OK))}{ROW2(ink(GENIN2_OK))}</table>')

SHIKICHIKEN = (
    '<table class="t" style="margin-top:28px"><colgroup><col style="width:5%"><col style="width:16%"><col style="width:20%">'
    '<col style="width:22%"><col style="width:37%"></colgroup>'
    '<tr><td class="vert" rowspan="3">敷地権の表示</td><td class="head">①土地の符号</td><td class="head">②敷地権の種類</td>'
    '<td class="head">③敷地権の割合</td><td class="head">原因及びその日付</td></tr>'
    f'<tr><td class="entry center">{ink("１")}</td><td class="entry center">{ink("所有権")}</td>'
    f'<td class="entry center">{ink("２分の１")}</td><td class="entry center">{ink(DATE + "敷地権")}</td></tr>'
    '<tr><td class="entry"></td><td class="entry"></td><td class="entry"></td><td class="entry"></td></tr></table>')

kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物区分登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:100px">{ink('建物図面　各階平面図　代理権限証書')}</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink('金2,000円')}</div></div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:100px">{ink('Ａ市Ｂ町三丁目５番１号　田宮栄一')}</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="dateline">令和３年10月17日　申請　Ｅ地方法務局</div>
{ITTOU}
{SHIKICHI_MOKUTEKI}
{KUBUN}
{SHIKICHIKEN}
<div class="caption">令和3年度 土地家屋調査士試験 第22問 問1 登記申請書（第1欄）解答例</div>
</div>''')

DAI2 = (
    '<table class="t r2"><colgroup><col style="width:7%"><col style="width:23%"><col style="width:70%"></colgroup>'
    f'<tr><td class="center">①</td><td class="center">登記の目的</td><td>{ink("区分建物区分登記")}</td></tr>'
    f'<tr><td class="center" rowspan="2">②</td><td class="center" rowspan="2">敷地権の割合</td>'
    f'<td>（あ）部分　　{ink("33088分の7150")}</td></tr>'
    f'<tr><td>（い）部分等　{ink("33088分の9394")}</td></tr>'
    f'<tr><td class="center">③</td><td class="center">添付書類</td><td>{ink("敷地権の割合を定めた規約証明書")}</td></tr></table>')
dai2 = page(f'''<div class="page">
<div class="sec" style="margin-top:0">第2欄</div>
{DAI2}
<div class="caption">令和3年度 土地家屋調査士試験 第22問 問2（第2欄）解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：区分した建物の表示の原因及びその日付 ----
def snippet(r1, r2, good=False):
    g = ' class="t good"' if good else ' class="t"'
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><table{g}>{KUBUN_COLS}'
            f'<tr><td class="vert" rowspan="3" style="font-size:17px;letter-spacing:0.05em">区分した<br>建物の表示</td>'
            f'{KUBUN_HEAD}</tr>{r1}{r2}</table>{chk}</div>')


ng_panel = snippet(ROW1(ink(DATE + GENIN1_OK)), ROW2(ink(DATE + GENIN2_OK)))
fix = lambda g: f'<span class="ink dstrike">{DATE}</span>{ink(g)}'  # noqa: E731
fix_panel = snippet(ROW1(fix(GENIN1_OK)), ROW2(fix(GENIN2_OK))) + \
    ('<div class="bubrow"><span class="bubble">区分は、登記によって初めて効果が生じる形成的登記。<br>'
     '登記より前に「区分した日」はない → 日付は書かない</span></div>'
     f'<div class="note">（参考）敷地権の表示の原因は「{DATE}敷地権」と日付を書く</div>')
ok_panel = snippet(ROW1(ink(GENIN1_OK)), ROW2(ink(GENIN2_OK)), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">令和3年度 第22問｜区分の原因に日付は書かない</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 300})
        for name, html in [('R3_dai22mon_toukishinseisho_kansei', kansei),
                           ('R3_dai22mon_dai2ran_kansei', dai2),
                           ('R3_dai22mon_toukishinseisho_machigai', machigai)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
        browser.close()
