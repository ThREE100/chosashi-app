"""平成24年度 第22問（建物）登記申請書の画像（完成形・第2欄・「一棟の建物の表示」の所在の添削）を、
HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形（第1欄）：`../prompt_H24_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  試験の答案用紙（A3横。左に登記申請書・一棟の建物の表示・敷地権の目的である土地の表示〈斜線が印刷済み〉、
  右に区分した建物の表示・第2欄）の欄を、左の列 → 右の列の順に縦に積む。項目の順序は答案用紙の印刷どおり
  「登記の目的 → 添付書類 → 平成何年何月何日申請　A地方法務局 → 所有者（被代位者） → 申請人（代位者） → 代位原因 → 代理人（略）」。
  登録免許税の欄はない。一棟の建物の表示の所在は2段、建物の名称は2つのセル、②床面積は整数部｜小数部に分けたセルが左右に2つ
  （解答例どおり左のセルに1階・2階を書き、右のセルは空欄）
- 第2欄：問3の説明文（答案用紙の右下の罫線入りの欄）
- 添削　：`../prompt_H24_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `R3/Q22/zu/make_R3_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/H24/Q22/zu/make_H24_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.lab {{ width: 190px; font-size: 22px; padding-top: 10px; white-space: nowrap; line-height: 1.4; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.dateline {{ font-size: 22px; margin: 2px 0 22px 0; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 20px; }}
.plainrow .ryaku {{ flex: 1; padding: 10px 0 0 20px; }}
.sec {{ font-size: 24px; margin: 34px 0 0; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 18px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.35em; padding: 0; font-size: 21px; }}
table.t td.lab2 {{ text-align: center; font-size: 18px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 76px; }}
table.t td.val {{ height: 52px; }}
table.t td.entry {{ height: 110px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
.diag {{ height: 330px; background: linear-gradient(to top right, transparent calc(50% - 1px), #111 calc(50% - 1px),
          #111 calc(50% + 1px), transparent calc(50% + 1px)); }}
.lined {{ border: 2px solid #111; margin-top: 18px; }}
.lined div {{ border-bottom: 1.2px dashed #777; min-height: 50px; padding: 8px 18px; font-size: 21px; line-height: 1.55; }}
.lined div:last-child {{ border-bottom: none; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 34px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.add {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold;
        border-bottom: 3px solid {RED}; }}
.caret {{ color: {RED}; font-weight: bold; font-size: 26px; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5; line-height: 1.5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; left: 160px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: 16px 0 0; }}
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


KOUZOU = '木造かわら<br>ぶき２階建'
SHOZAI_OK = 'Ａ市Ｂ町三丁目120番地１、120番地２'
SHOZAI_NG = 'Ａ市Ｂ町三丁目120番地１'
ITTOU_COLS = ('<colgroup><col style="width:5%"><col style="width:10%"><col style="width:10%"><col style="width:20%">'
              '<col style="width:7%"><col style="width:20%"><col style="width:7%"><col style="width:21%"></colgroup>')


def ittou(shozai, extra_cls=''):
    """一棟の建物の表示（所在は2段、建物の名称は2つのセル、②床面積は左右2つのセル）。"""
    return (
        f'<table class="t{extra_cls}">{ITTOU_COLS}'
        '<tr><td class="vert" rowspan="5">一棟の建物の表示</td>'
        f'<td class="lab2" rowspan="2" colspan="2">所　在</td><td class="val" colspan="5">{shozai}</td></tr>'
        '<tr><td class="val" colspan="5"></td></tr>'
        '<tr><td class="lab2 val" colspan="2">建物の名称</td><td class="val" colspan="3"></td><td class="val" colspan="2"></td></tr>'
        '<tr><td class="head" colspan="2">①構　造</td><td class="head" colspan="4">②床　面　積<br>'
        '<span style="display:inline-block;width:48%">m²</span><span style="display:inline-block;width:48%">m²</span></td>'
        '<td class="head">原因及びその日付</td></tr>'
        f'<tr><td class="entry center" colspan="2">{ink(KOUZOU)}</td>'
        f'{area([("1階", "142", "50"), ("2階", "120", "00")])}'
        '<td class="entry int"></td><td class="entry dec"></td>'
        '<td class="entry genin"></td></tr></table>')


SHIKICHI_MOKUTEKI = (
    '<table class="t"><colgroup><col style="width:5%"><col style="width:95%"></colgroup>'
    '<tr><td class="vert" style="font-size:17px;letter-spacing:0.02em;height:330px">敷地権の目的である土地の表示</td>'
    '<td class="diag"></td></tr></table>')

KUBUN_COLS = ('<colgroup><col style="width:5%"><col style="width:11%"><col style="width:8%"><col style="width:10%">'
              '<col style="width:9%"><col style="width:15%"><col style="width:13%"><col style="width:6%">'
              '<col style="width:23%"></colgroup>')
KUBUN_HEAD = ('<td class="head">家屋<br>番号</td><td class="head">建物の<br>名　称</td>'
              '<td class="head" style="font-size:15px">主である<br>建物又は<br>附属建物</td>'
              '<td class="head">①<br>種類</td><td class="head">②構　造</td><td class="head" colspan="2">③床　面　積<br>m²</td>'
              '<td class="head">原因及び<br>その日付</td>')
EMPTY_ROW = ('<tr><td class="entry"></td><td class="entry"></td><td class="entry"></td><td class="entry"></td>'
             '<td class="entry"></td><td class="entry int"></td><td class="entry dec"></td><td class="entry"></td></tr>')
KUBUN = (f'<table class="t" style="margin-top:34px">{KUBUN_COLS}'
         f'<tr><td class="vert" rowspan="4">区分した建物の表示</td>{KUBUN_HEAD}</tr>'
         f'<tr><td class="entry"></td><td class="entry"></td><td class="entry"></td>'
         f'<td class="entry center">{ink("居宅")}</td><td class="entry center">{ink(KOUZOU)}</td>'
         f'{area([("1階", "68", "57"), ("2階", "57", "69")])}'
         f'<td class="entry genin">{ink("平成24年７月30日新築")}</td></tr>{EMPTY_ROW}{EMPTY_ROW}</table>')


def box(label, value, h=62):
    return f'<div class="row"><div class="lab">{label}</div><div class="box" style="height:{h}px">{value}</div></div>'


kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
{box('登記の目的', ink('区分建物表題登記'))}
{box('添　付　書　類', ink('建物図面　各階平面図　所有権証明書　住所証明書<br>代位原因証書　代理権限証書'), 112)}
<div class="dateline">平成何年何月何日申請　Ａ地方法務局</div>
{box('所　有　者<br>（被代位者）', ink('Ａ市Ｂ町三丁目３番５号　乙川夏子'), 76)}
{box('申　請　人<br>（代　位　者）', ink('Ａ市Ｂ町三丁目３番４号　甲野春男'), 76)}
{box('代　位　原　因', ink('不動産登記法第48条第２項'), 76)}
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{ittou(ink(SHOZAI_OK))}
{SHIKICHI_MOKUTEKI}
{KUBUN}
<div class="caption">平成24年度 土地家屋調査士試験 第22問 問1 登記申請書（第1欄）解答例</div>
</div>''')

DAI2_LINES = [
    '敷地権とは、区分建物の敷地利用権（専有部分を所有するための建物の敷地',
    'に関する権利）のうち、登記されたものであって、区分所有法第22条第1項本',
    '文（同条第3項において準用する場合を含む。）の規定により、区分所有者の',
    '有する専有部分と分離して処分することができないものをいう。本件の一棟',
    'の建物の敷地は120番1と120番2の2筆で、120番1は乙川夏子が、120番2は甲',
    '野春男がそれぞれ単独で所有し、相手方の土地は無償で使用する合意がある',
    'にすぎない。敷地利用権は数人で有する権利ではなく、専有部分の全部を所',
    '有する者の権利でもないから、分離処分は禁止されない。また、無償で使用す',
    'る権利（使用借権）は登記することができない。したがって、本件の敷地利用',
    '権は敷地権に当たらず、敷地権は登記されない。',
]
dai2 = page(f'''<div class="page">
<div class="sec" style="margin-top:0">第2欄</div>
<div class="lined">{''.join(f'<div>{ink(s)}</div>' for s in DAI2_LINES)}<div></div><div></div></div>
<div class="caption">平成24年度 土地家屋調査士試験 第22問 問3（第2欄）解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：一棟の建物の表示の所在 ----
ng_panel = ittou(ink(SHOZAI_NG))
fix_panel = (ittou(ink(SHOZAI_NG) + '<span class="caret">∧</span><span class="add">、120番地２</span>') +
             '<div class="bubrow"><span class="bubble">一棟の建物の表示の所在は、一棟の建物全体が建っている土地の地番。<br>'
             'Ⓐが建っている120番地１だけではない → 120番地２も書く</span></div>'
             '<div class="note">（参考）Ⓐは120番１の上だけにあるが、一棟の建物は120番１と120番２の２筆にかかっている'
             '（障壁の中心線＝C-F線）</div>')
ok_panel = f'<div class="okwrap">{ittou(ink(SHOZAI_OK), " good")}{CHECK_SVG}</div>'
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成24年度 第22問｜一棟の建物の所在は一棟全体の２筆</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 300})
        for name, html in [('H24_dai22mon_toukishinseisho_kansei', kansei),
                           ('H24_dai22mon_dai2ran_kansei', dai2),
                           ('H24_dai22mon_toukishinseisho_machigai', machigai)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
        browser.close()
