"""令和5年度 第22問（建物）登記申請書の画像（完成形、添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_R5_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  欄の形は答案用紙（第2欄）に合わせる：申請の日付・提出先は印刷済み（令和5年10月12日　申請　Ａ地方法務局）、
  代理人は印刷の「（略）」。一棟の建物の表示は所在2段（2段目の右端に原因）・建物の名称・①構造・②床面積（2列）・原因。
  敷地権の目的である土地の表示、区分した建物の表示（3行。2行目の家屋番号の位置に印刷の点線枠「所在（省略）」と「（省略）」）、
  敷地権の表示の順。答案用紙は試験の答案用紙を収録したアガルートの過去問集の「第22問 答案用紙（その1）（その2）」で確認した
- 添削　：`../prompt_R5_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `R7/Q22/zu/make_R7_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/R5/Q22/zu/make_R5_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.dateline {{ font-size: 22px; margin: 2px 0 24px 20px; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 22px; }}
.plainrow .ryaku {{ flex: 1; text-align: center; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 18px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.35em; padding: 0; font-size: 21px; }}
table.t td.lab2 {{ text-align: center; font-size: 18px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 76px; }}
table.t td.val {{ height: 52px; }}
table.t td.entry {{ height: 128px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
.omit {{ display: inline-block; border: 1.5px dashed #333; padding: 4px 14px; font-size: 17px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 34px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.strike {{ position: relative; }}
.strike::after {{ content: ""; position: absolute; left: -4px; right: -4px; top: 52%; border-top: 3px solid {RED};
                  transform: rotate(-3deg); }}
.red {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; }}
.caret {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; font-size: 15px;
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
    """床面積の整数部・小数部のセル。floors: [(階の表示, 整数部, 小数部)]。階の表示は整数部の前に書く"""
    ints = br(*[ink(f'{k}　{a}' if k else a) for k, a, _ in floors])
    decs = br(*[ink(b) for _, _, b in floors])
    return f'<td class="{cls} int">{ints}</td><td class="{cls} dec">{decs}</td>'


def area_bubun(floors):
    """区分建物の「1階部分」の書き方：階の表示を1行、数値を次の行に右寄せ"""
    ints = br(*[f'{ink(k)}<br>{ink(a)}' for k, a, _ in floors])
    decs = br(*[f'&nbsp;<br>{ink(b)}' for _, _, b in floors])
    return f'<td class="entry int">{ints}</td><td class="entry dec">{decs}</td>'


# ---- 一棟の建物の表示（答案用紙の形） ----
ITTOU_COLS = ('<colgroup><col style="width:5%"><col style="width:9%"><col style="width:11%"><col style="width:14%">'
              '<col style="width:11%"><col style="width:4%"><col style="width:13%"><col style="width:4%">'
              '<col style="width:29%"></colgroup>')


def ittou_table(shozai, kouzou, floors1, floors2=(), genin=''):
    return (f'<table class="t">{ITTOU_COLS}'
            f'<tr><td class="vert" rowspan="6">一棟の建物の表示</td>'
            f'<td class="lab2" rowspan="2">所　在</td><td class="val" colspan="7">{shozai}</td></tr>'
            f'<tr><td class="val" colspan="5"></td><td class="val genin" colspan="2"></td></tr>'
            f'<tr><td class="lab2 val" colspan="2">建物の名称</td><td class="val" colspan="3"></td>'
            f'<td class="val" colspan="3"></td></tr>'
            f'<tr><td class="head" colspan="2">①構　造</td><td class="head" colspan="4">②床　面　積<br>'
            f'<span style="display:inline-block;width:45%">m²</span><span style="display:inline-block;width:45%">m²</span></td>'
            f'<td class="head" colspan="2">原因及びその日付</td></tr>'
            f'<tr><td class="entry center" colspan="2">{kouzou}</td>{area(floors1)}{area(floors2)}'
            f'<td class="entry genin" colspan="2">{genin}</td></tr>'
            f'</table>')


SHIKICHI_MOKUTEKI = (
    '<table class="t"><colgroup><col style="width:8%"><col style="width:11%"><col style="width:19%"><col style="width:12%">'
    '<col style="width:14%"><col style="width:7%"><col style="width:29%"></colgroup>'
    '<tr><td class="vert" rowspan="2" style="font-size:18px;letter-spacing:0.1em">敷地権の目的である<br>土地の表示</td>'
    '<td class="head">①土地の<br>符号</td><td class="head">②所在及び地番</td><td class="head">③地目</td>'
    '<td class="head" colspan="2">④地積　m²</td><td class="head">原因及びその日付</td></tr>'
    '<tr><td class="entry"></td><td class="entry"></td><td class="entry"></td><td class="entry int"></td>'
    '<td class="entry dec"></td><td class="entry genin center">{genin}</td></tr></table>')

KUBUN_COLS = ('<colgroup><col style="width:6%"><col style="width:12%"><col style="width:9%"><col style="width:10%">'
              '<col style="width:10%"><col style="width:14%"><col style="width:13%"><col style="width:5%">'
              '<col style="width:21%"></colgroup>')
KUBUN_HEAD = ('<td class="head">家屋番号</td><td class="head">建物の<br>名称</td><td class="head">主である<br>建物又は<br>附属建物</td>'
              '<td class="head">①種　類</td><td class="head">②構　造</td><td class="head" colspan="2">③床面積<br>m²</td>'
              '<td class="head">原因及び<br>その日付</td>')


def kubun_row(kaoku, kind, struct, floors, genin, bubun=True):
    a = area_bubun(floors) if bubun else area(floors)
    return (f'<tr><td class="entry">{kaoku}</td><td class="entry"></td><td class="entry"></td>'
            f'<td class="entry center">{kind}</td><td class="entry center">{struct}</td>{a}'
            f'<td class="entry genin">{genin}</td></tr>')


def gappei_row(kind, struct, floors, genin):
    """2行目（合併後の建物）：家屋番号・建物の名称・主附の位置に印刷の点線枠「所在（省略）」と「（省略）」"""
    return (f'<tr><td class="entry" colspan="3" style="vertical-align:top;padding-top:14px">'
            f'<span class="omit">所在　　（省略）</span><br><span style="font-size:17px">（省略）</span></td>'
            f'<td class="entry center">{kind}</td><td class="entry center">{struct}</td>{area(floors)}'
            f'<td class="entry genin">{genin}</td></tr>')


S_OLD1 = '軽量鉄骨<br>造２階建'
S_NEW = '軽量鉄骨<br>造スレー<br>トぶき２<br>階建'
S_OLD2 = '軽量鉄骨<br>造１階建'
GENIN_OK = '②③令和5年10月6日構造変更、増築、3番9の2を合併'

ROW1 = kubun_row(ink('Ｂ町一丁目<br>３番９の１'), ink('居宅'), ink(S_OLD1), [('1階部分', '4', '61'), ('2階部分', '70', '21')], '')
ROW2 = gappei_row(ink('居宅'), ink(S_NEW), [('1階', '83', '62'), ('2階', '88', '57')], ink(GENIN_OK))
ROW3 = kubun_row(ink('Ｂ町一丁目<br>３番９の２'), ink('居宅'), ink(S_OLD2), [('1階部分', '74', '72')], ink('3番9の1に合併'))

KUBUN_SHIKICHI = (
    f'<table class="t">{KUBUN_COLS}'
    f'<tr><td class="vert" rowspan="4">区分した建物の表示</td>{KUBUN_HEAD}</tr>'
    f'{ROW1}{ROW2}{ROW3}'
    f'<tr><td class="vert" rowspan="2">敷地権の表示</td><td class="head">①土地の<br>符号</td>'
    f'<td class="head" colspan="3">②敷地権の種類</td><td class="head" colspan="2">③敷地権の割合</td>'
    f'<td class="head" colspan="3">原因及びその日付</td></tr>'
    f'<tr><td class="entry"></td><td class="entry" colspan="3"></td><td class="entry" colspan="2"></td>'
    f'<td class="entry genin center" colspan="3">{ink("記載不要")}</td></tr>'
    f'</table>')

kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('区分建物表題部変更・合併登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:118px">{ink(br('建物図面　各階平面図　登記識別情報　印鑑証明書', '所有権証明書　代理権限証書'))}</div></div>
<div class="dateline">令和５年10月12日　申請　　Ａ地方法務局</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:110px">{ink('Ａ市Ｂ町一丁目３番地９　甲田栄一')}</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink('金1,000円')}</div></div>
{ittou_table(ink('Ａ市Ｂ町一丁目３番地９'), ink('軽量鉄骨造陸屋<br>根２階建'), [('1階', '83', '62'), ('2階', '73', '99')])}
{SHIKICHI_MOKUTEKI.format(genin=ink('記載不要'))}
{KUBUN_SHIKICHI}
<div class="caption">令和5年度 土地家屋調査士試験 第22問 問2 登記申請書 解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：区分した建物の表示の2行目（合併後の建物） ----
def snippet(row, good=False):
    g = ' class="t good"' if good else ' class="t"'
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><table{g}>{KUBUN_COLS}'
            f'<tr><td class="vert" rowspan="2" style="font-size:17px;letter-spacing:0.05em">区分した<br>建物の表示</td>'
            f'{KUBUN_HEAD}</tr>{row}</table>{chk}</div>')


NG = '令和5年10月6日増築、3番9の2を合併'
FIX = (f'<span class="caret">∨②③</span>'
       f'<span class="ink">令和5年10月6日</span><span class="caret">∨構造変更、</span>'
       f'<span class="ink">増築、3番9の2を合併</span>')
ng_panel = snippet(gappei_row(ink('居宅'), ink(S_NEW), [('1階', '83', '62'), ('2階', '88', '57')], ink(NG)))
fix_panel = snippet(gappei_row(ink('居宅'), ink(S_NEW), [('1階', '83', '62'), ('2階', '88', '57')], FIX)) + \
    ('<div class="bubrow"><span class="bubble">屋根を陸屋根からスレートぶきに変えた＝構造変更が抜けている！<br>'
     '頭に、変更した欄の番号「②③」（②構造・③床面積）も付ける</span></div>')
ok_panel = snippet(gappei_row(ink('居宅'), ink(S_NEW), [('1階', '83', '62'), ('2階', '88', '57')], ink(GENIN_OK)),
                   good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">令和5年度 第22問｜登記原因のよくある書き忘れ（構造変更と欄番号）</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 800})
        for name, html in [('R5_dai22mon_toukishinseisho_kansei', kansei),
                           ('R5_dai22mon_toukishinseisho_machigai', machigai)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（要確認）'))
        browser.close()
