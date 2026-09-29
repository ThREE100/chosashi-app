"""令和4年度 第22問（建物）登記申請書の画像（完成形、添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_R4_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  欄の形は試験の答案用紙（第1欄）に合わせる：申請の日付・提出先（令和4年10月17日　申請　Ｅ地方法務局）と
  代理人の「（略）」は印刷済み、申請人は記入枠。建物の表示は、所在1段、家屋番号、見出し
  （主である建物又は附属建物・①種類・②構造・③床面積・原因及びその日付）、記入行5行。登録免許税の欄はない
- 添削　：`../prompt_R4_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `R5/Q22/zu/make_R5_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/R4/Q22/zu/make_R4_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 1.2em; padding: 0; font-size: 21px; }}
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
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 34px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.red {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; }}
.caret {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; font-size: 15px;
          vertical-align: super; }}
.circle {{ border: 2.5px solid {RED}; border-radius: 50%; padding: 2px 6px; }}
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


# ---- 建物の表示（答案用紙の形：所在1段、家屋番号、見出し、記入行5行） ----
COLS = ('<colgroup><col style="width:5%"><col style="width:12%"><col style="width:10%"><col style="width:19%">'
        '<col style="width:12%"><col style="width:6%"><col style="width:36%"></colgroup>')
HEAD = ('<td class="head">主である<br>建物又は<br>附属建物</td><td class="head">①種　類</td><td class="head">②構　造</td>'
        '<td class="head" colspan="2">③床面積<br>m²</td><td class="head">原因及びその日付</td>')


def entry_row(shu, kind, struct, floors, genin):
    return (f'<tr><td class="entry center">{shu}</td><td class="entry center">{kind}</td>'
            f'<td class="entry center">{struct}</td>{area(floors)}<td class="entry genin">{genin}</td></tr>')


EMPTY_ROW = ('<tr><td class="entry"></td><td class="entry"></td><td class="entry"></td>'
             '<td class="entry int"></td><td class="entry dec"></td><td class="entry"></td></tr>')

S_OLD = '木造スレー<br>トぶき平家<br>建'
S_NEW = '木造スレー<br>トぶき２階<br>建'
S_GAR = '鉄骨造亜鉛<br>メッキ鋼板<br>ぶき平家建'
GENIN_OK = '①②③令和４年９月30日種類・<br>構造変更、増築、符号１の附属<br>建物合体'

ROW1 = entry_row(ink('主'), ink('事務所'), ink(S_OLD), [('', '72', '00')], '')
ROW2 = entry_row('', ink('居宅'), ink(S_NEW), [('1階', '113', '00'), ('2階', '25', '00')], ink(GENIN_OK))
ROW3 = entry_row(ink('符号１'), ink('倉庫'), ink(S_NEW), [('1階', '25', '00'), ('2階', '25', '00')],
                 ink('令和４年９月30日主である<br>建物に合体'))
ROW4 = entry_row(ink('符号２'), ink('車庫'), ink(S_GAR), [('', '20', '00')], ink('令和４年９月30日新築'))

TABLE = (f'<table class="t">{COLS}'
         f'<tr><td class="lab2 val" colspan="2">所　在</td><td class="val" colspan="5">{ink("Ａ市Ｂ町一丁目５番地３")}</td></tr>'
         f'<tr><td class="vert" rowspan="7">建物の表示</td><td class="lab2 val">家屋番号</td>'
         f'<td class="val" colspan="5">{ink("５番３")}</td></tr>'
         f'<tr>{HEAD}</tr>{ROW1}{ROW2}{ROW3}{ROW4}{EMPTY_ROW}</table>')

kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物表題部変更登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:100px">{ink(br('建物図面　各階平面図　所有権証明書　代理権限証書'))}</div></div>
<div class="dateline">令和４年10月17日　申請　　Ｅ地方法務局</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:96px">{ink('Ａ市Ｂ町一丁目５番３号　和田令子')}</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{TABLE}
<div class="caption">令和4年度 土地家屋調査士試験 第22問 登記申請書 解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：主である建物の2行（変更前・変更後） ----
def snippet(row2, row1=ROW1, good=False):
    g = ' class="t good"' if good else ' class="t"'
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><table{g}>{COLS}'
            f'<tr><td class="vert" rowspan="3" style="letter-spacing:0.2em">建物の表示</td>{HEAD}</tr>'
            f'{row1}{row2}</table>{chk}</div>')


NG = '③令和４年９月30日増築、符号１<br>の附属建物合体'
FIX = (f'<span class="caret">∨①②</span><span class="ink">③令和４年９月30日</span>'
       f'<span class="caret">∨種類・構造変更、</span><br><span class="ink">増築、符号１の附属建物合体</span>')
S_OLD_FIX = ink('木造スレー<br>トぶき') + '<span class="circle">' + ink('平家') + '</span><br>' + ink('建')
S_NEW_FIX = ink('木造スレー<br>トぶき') + '<span class="circle">' + ink('２階') + '</span><br>' + ink('建')
ROW1_FIX = entry_row(ink('主'), f'<span class="circle">{ink("事務所")}</span>', S_OLD_FIX,
                     [('', '72', '00')], '')
ng_panel = snippet(entry_row('', ink('居宅'), ink(S_NEW), [('1階', '113', '00'), ('2階', '25', '00')], ink(NG)))
fix_panel = snippet(entry_row('', f'<span class="circle">{ink("居宅")}</span>', S_NEW_FIX,
                              [('1階', '113', '00'), ('2階', '25', '00')], FIX), row1=ROW1_FIX) + \
    ('<div class="bubrow"><span class="bubble">①種類：事務所 → 居宅、②構造：平家建 → ２階建（階数も構造の一部）<br>'
     '変わった欄の番号「①②」と「種類・構造変更」が抜けている！</span></div>')
ok_panel = snippet(entry_row('', ink('居宅'), ink(S_NEW), [('1階', '113', '00'), ('2階', '25', '00')], ink(GENIN_OK)),
                   good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">令和4年度 第22問｜変わった欄の番号と原因は、全部書く</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 800})
        for name, html in [('R4_dai22mon_toukishinseisho_kansei', kansei),
                           ('R4_dai22mon_toukishinseisho_machigai', machigai)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（要確認）'))
        browser.close()
