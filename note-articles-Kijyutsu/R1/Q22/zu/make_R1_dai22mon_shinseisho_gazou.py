"""令和元年度 第22問（建物）登記申請書の画像（第1欄の完成形、第2欄の完成形、添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 第1欄の完成形：`../prompt_R1_dai22mon_toukishinseisho_gazou.md` の記入データ1どおり。縦長（横1200px）。
  欄の形は試験の答案用紙（第22問答案用紙、A3横）に合わせ、左の列（登記の目的・添付書類・申請人・代理人・申請の日付・
  一棟の建物の表示・敷地権の目的である土地の表示）の下に、右の列（区分した建物の表示・敷地権の表示）を縦に積む。
  答案用紙の順序どおり、申請人が申請の日付より先。代理人の「（略）」と「令和元年10月18日　申請　Ａ地方法務局」は印刷。
  登録免許税の欄はない。一棟の建物の表示の②床面積は2つの小列（それぞれ整数部と小数部を点線で分ける）
- 第2欄の完成形：記入データ2どおり。①②③の3行（横1200px）
- 添削：`../prompt_R1_dai22mon_toukishinseisho_machigai.md` どおり。敷地権の表示欄の①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `R5/Q22/zu/make_R5_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/R1/Q22/zu/make_R1_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.dateline {{ font-size: 22px; margin: 2px 0 10px 20px; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 22px; }}
.plainrow .ryaku {{ flex: 1; text-align: center; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 18px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.3em; padding: 0; font-size: 20px; }}
table.t td.lab2 {{ text-align: center; font-size: 18px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 70px; }}
table.t td.val {{ height: 56px; }}
table.t td.entry {{ height: 120px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
.gap {{ height: 26px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 34px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 第2欄 */
table.d2 {{ width: 100%; border-collapse: collapse; border: 3px solid #111; }}
table.d2 td {{ border: 1.5px solid #111; height: 86px; font-size: 26px; padding: 0 22px; }}
table.d2 td.no {{ width: 90px; text-align: center; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.strike {{ position: relative; }}
.strike::after {{ content: ""; position: absolute; left: -4px; right: -4px; top: 52%; border-top: 3px solid {RED};
                  transform: rotate(-3deg); }}
.red {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; }}
.maru {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; font-size: 15px;
         vertical-align: super; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5; line-height: 1.5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; right: 120px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: 16px 0 0; text-align: right; }}
.bubrow .bubble {{ text-align: left; }}
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


def area_bubun(floors):
    """区分建物の「1階部分」の書き方：階の表示を1行、数値を次の行に右寄せ"""
    ints = br(*[f'{ink(k)}<br>{ink(a)}' for k, a, _ in floors])
    decs = br(*[f'&nbsp;<br>{ink(b)}' for _, _, b in floors])
    return f'<td class="entry int">{ints}</td><td class="entry dec">{decs}</td>'


# ---- 一棟の建物の表示（答案用紙の形：所在・建物の名称・①構造・②床面積〈2小列〉・原因及びその日付） ----
ITTOU = (
    '<table class="t"><colgroup><col style="width:5%"><col style="width:9%"><col style="width:13%">'
    '<col style="width:17%"><col style="width:6%"><col style="width:17%"><col style="width:6%"><col style="width:27%"></colgroup>'
    '<tr><td class="vert" rowspan="4">一棟の建物の表示</td>'
    f'<td class="lab2 val">所　在</td><td class="val" colspan="6">{ink("Ａ市Ｂ町一丁目23番地１、23番地２")}</td></tr>'
    f'<tr><td class="lab2 val" colspan="2">建物の名称</td><td class="val" colspan="5">{ink("Ａランドマークタウン")}</td></tr>'
    '<tr><td class="head" colspan="2">①構　造</td><td class="head" colspan="4">②床　面　積<br>'
    '<span style="display:inline-block;width:45%">m²</span><span style="display:inline-block;width:45%">m²</span></td>'
    '<td class="head">原因及びその日付</td></tr>'
    f'<tr><td class="entry center" colspan="2" style="height:170px">{ink("鉄筋コンクリート<br>造陸屋根８階建")}</td>'
    + area([('1階', '900', '48'), ('2階', '900', '48'), ('3階', '498', '48'), ('4階', '498', '48')])
    + area([('5階', '498', '48'), ('6階', '498', '48'), ('7階', '498', '48'), ('8階', '498', '48')])
    + '<td class="entry genin"></td></tr></table>')

SHIKICHI_MOKUTEKI = (
    '<table class="t"><colgroup><col style="width:8%"><col style="width:10%"><col style="width:30%"><col style="width:10%">'
    '<col style="width:13%"><col style="width:7%"><col style="width:22%"></colgroup>'
    '<tr><td class="vert" rowspan="3" style="font-size:16px;letter-spacing:0.05em">敷地権の目的である<br>土地の表示</td>'
    '<td class="head">①土地の<br>符号</td><td class="head">②所在及び地番</td><td class="head">③地目</td>'
    '<td class="head" colspan="2">④地　積　m²</td><td class="head">原因及び<br>その日付</td></tr>'
    f'<tr><td class="entry center">{ink("1")}</td><td class="entry">{ink("Ａ市Ｂ町一丁目23番１")}</td>'
    f'<td class="entry center">{ink("宅地")}</td>{area([("", "1242", "50")])}<td class="entry genin"></td></tr>'
    f'<tr><td class="entry center">{ink("2")}</td><td class="entry">{ink("Ａ市Ｂ町一丁目23番２")}</td>'
    f'<td class="entry center">{ink("宅地")}</td>{area([("", "700", "00")])}<td class="entry genin"></td></tr>'
    '</table>')

KUBUN = (
    '<table class="t"><colgroup><col style="width:5%"><col style="width:8%"><col style="width:12%"><col style="width:9%">'
    '<col style="width:9%"><col style="width:17%"><col style="width:11%"><col style="width:5%"><col style="width:24%"></colgroup>'
    '<tr><td class="vert" rowspan="4">区分した建物の表示</td>'
    '<td class="head">家屋<br>番号</td><td class="head">建物の<br>名称</td><td class="head" style="font-size:14px">主である<br>建物又は<br>附属建物</td>'
    '<td class="head">①種類</td><td class="head">②構　造</td><td class="head" colspan="2">③床面積<br>m²</td>'
    '<td class="head">原因及び<br>その日付</td></tr>'
    f'<tr><td class="entry"></td><td class="entry">{ink("Ｂ町行政<br>センター")}</td><td class="entry center">{ink("主")}</td>'
    f'<td class="entry center">{ink("事務所")}</td><td class="entry center">{ink("鉄筋コンクリ<br>ート造２階建")}</td>'
    + area_bubun([('1階部分', '393', '82'), ('2階部分', '393', '82')])
    + f'<td class="entry genin">{ink("令和元年10月13日<br>新築")}</td></tr>'
    f'<tr><td class="entry"></td><td class="entry"></td><td class="entry center">{ink("符号1")}</td>'
    f'<td class="entry center">{ink("駐車場")}</td>'
    f'<td class="entry">{ink("Ａ市Ｂ町一丁目<br>23番地２<br>鉄骨造合金メッキ<br>鋼板ぶき平家建")}</td>'
    + area([('', '47', '25')]) + '<td class="entry genin"></td></tr>'
    '<tr><td class="entry" style="height:90px"></td><td class="entry"></td><td class="entry"></td><td class="entry"></td>'
    '<td class="entry"></td><td class="entry int"></td><td class="entry dec"></td><td class="entry"></td></tr>'
    '</table>')

SHIKI_COLS = ('<colgroup><col style="width:6%"><col style="width:14%"><col style="width:20%"><col style="width:20%">'
              '<col style="width:40%"></colgroup>')
SHIKI_HEAD = ('<td class="head">①土地の<br>符号</td><td class="head">②敷地権の種類</td>'
              '<td class="head">③敷地権の割合</td><td class="head">原因及びその日付</td>')
GENIN_OK = '令和元年10月13日敷地権'
GENIN_NG = '令和元年10月10日敷地権'


def shiki_rows(g1, g2, cls='entry'):
    return (f'<tr><td class="{cls} center">{ink("1")}</td><td class="{cls} center">{ink("地上権")}</td>'
            f'<td class="{cls} center">{ink("9分の4")}</td><td class="{cls} center">{g1}</td></tr>'
            f'<tr><td class="{cls} center">{ink("2")}</td><td class="{cls} center">{ink("所有権")}</td>'
            f'<td class="{cls} center">{ink("3分の1")}</td><td class="{cls} center">{g2}</td></tr>')


SHIKICHIKEN = (f'<table class="t">{SHIKI_COLS}<tr><td class="vert" rowspan="3">敷地権の表示</td>{SHIKI_HEAD}</tr>'
               f'{shiki_rows(ink(GENIN_OK), ink(GENIN_OK), "val")}</table>')

kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('区分建物表題登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:118px">{ink(br('建物図面　各階平面図　所有権証明書　住所証明書', '規約証明書　登記事項証明書　代理権限証書'))}</div></div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:100px">{ink(br('Ａ市Ｃ町二丁目24番４号　株式会社未来高速鉄道', '代表取締役　乙田三郎'))}</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="dateline">令和元年10月18日　申請　Ａ地方法務局</div>
{ITTOU}
{SHIKICHI_MOKUTEKI}
<div class="gap"></div>
{KUBUN}
{SHIKICHIKEN}
<div class="caption">令和元年度 土地家屋調査士試験 第22問 問1 登記申請書（第1欄）解答例</div>
</div>''')

dai2 = page(f'''<div class="page">
<table class="d2">
<tr><td class="no">①</td><td>{ink('区分建物表題部変更登記')}</td></tr>
<tr><td class="no">②</td><td>{ink('一棟の建物の名称を変更した日から1月以内')}</td></tr>
<tr><td class="no">③</td><td>{ink('10万円以下の過料の罰則がある。')}</td></tr>
</table>
<div class="caption">令和元年度 土地家屋調査士試験 第22問 問2 解答例（第2欄）</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：敷地権の表示 ----
def snippet(g1, g2, good=False):
    g = ' class="t good"' if good else ' class="t"'
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><table{g}>{SHIKI_COLS}<tr><td class="vert" rowspan="3">敷地権の表示</td>{SHIKI_HEAD}</tr>'
            f'{shiki_rows(g1, g2)}</table>{chk}</div>')


FIX = (f'<span class="ink">令和元年10月</span><span class="strike"><span class="ink">10日</span></span>'
       f'<span class="red">13日</span><span class="ink">敷地権</span>')
ng_panel = snippet(ink(GENIN_NG), ink(GENIN_NG))
fix_panel = snippet(FIX, FIX) + \
    ('<div class="bubrow"><span class="bubble">10月10日は規約の設定日。建物はまだ完成していない！<br>'
     '敷地権は、建物（10月13日完成）と敷地利用権と規約が全部そろった日に生まれる<br>'
     '（種類の地上権・所有権、割合の9分の4・3分の1はこのままでよい）</span></div>')
ok_panel = snippet(ink(GENIN_OK), ink(GENIN_OK), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">令和元年度 第22問｜敷地権の日付は、全部がそろった日（建物の完成日）</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 200})
        for name, html in [('R1_dai22mon_toukishinseisho_kansei', kansei),
                           ('R1_dai22mon_toukishinseisho_kansei_dai2ran', dai2),
                           ('R1_dai22mon_toukishinseisho_machigai', machigai)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
        browser.close()
