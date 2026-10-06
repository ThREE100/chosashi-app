"""平成28年度 第22問（建物）登記申請書の画像（完成形、添削）と第2欄の完成形を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H28_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  欄の形は試験の答案用紙（平成28年度 第二十二問答案用紙の第1欄）に合わせる：申請の日付・提出先
  （平成28年8月10日　申請　Ａ　地方法務局　Ｂ　出張所）と代理人の「（略）」は印刷済み、申請人は記入枠。
  建物の表示は、不動産番号（記載省略）、所在2段、家屋番号、見出し（主たる建物又は附属建物・①種類・②構造・
  ③床面積・登記原因及びその日付）、記入行4行、最終の横いっぱいの行。登録免許税の欄はない
- 第2欄：答案用紙はA3横で、左の列に第1欄（申請書）、右の列に第2欄（問2の記述）がある。第2欄は別の画像にして、
  記事の問2の答えの直後に置く（R3/Q22・R4/Q22と同じ扱い）。欄の形は答案用紙どおりの大きな記述枠
- 添削　：`../prompt_H28_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `R4/Q22/zu/make_R4_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP）
実行: python3 note-articles-Kijyutsu/H28/Q22/zu/make_H28_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 22px; align-items: baseline; }}
.plainrow .lab {{ padding-top: 0; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 18px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 1.2em; padding: 0; font-size: 21px; }}
table.t td.lab2 {{ text-align: center; font-size: 18px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 76px; }}
table.t td.val {{ height: 52px; }}
table.t td.entry {{ height: 150px; }}
table.t td.last {{ height: 56px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
.sec {{ font-size: 24px; margin: 0 0 10px; }}
.kijutsu {{ border: 2px solid #111; min-height: 520px; padding: 22px 26px; font-size: 24px; line-height: 2.0; }}
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


def area(floors, cls='entry', ints_html=None):
    """床面積の整数部・小数部のセル。floors: [(階の表示, 整数部, 小数部)]"""
    ints = ints_html or br(*[ink(f'{k}　{a}' if k else a) for k, a, _ in floors])
    decs = br(*[ink(b) for _, _, b in floors])
    return f'<td class="{cls} int">{ints}</td><td class="{cls} dec">{decs}</td>'


# ---- 建物の表示（答案用紙の形） ----
COLS = ('<colgroup><col style="width:5%"><col style="width:11%"><col style="width:9%"><col style="width:22%">'
        '<col style="width:14%"><col style="width:6%"><col style="width:33%"></colgroup>')
HEAD = ('<td class="head" style="font-size:15px">主たる建物<br>又は附属建物</td><td class="head">①種類</td><td class="head">②構造</td>'
        '<td class="head" colspan="2">③床面積　m²</td><td class="head">登記原因及びその日付</td>')


def entry_row(shu, kind, struct, floors, genin, ints_html=None):
    return (f'<tr><td class="entry center">{shu}</td><td class="entry center">{kind}</td>'
            f'<td class="entry center">{struct}</td>{area(floors, ints_html=ints_html)}<td class="entry genin">{genin}</td></tr>')


EMPTY_ROW = ('<tr><td class="entry"></td><td class="entry"></td><td class="entry"></td>'
             '<td class="entry int"></td><td class="entry dec"></td><td class="entry"></td></tr>')

S_OLD = '軽量鉄骨造合金<br>メッキ鋼板ぶき<br>２階建'
S_NEW = '軽量鉄骨造合金<br>メッキ鋼板ぶき<br>渡廊下付き３階建'
S_NG = '軽量鉄骨造合金<br>メッキ鋼板ぶき<br>３階建'
F_OLD = [('1階', '89', '10'), ('2階', '64', '80')]
F_NEW = [('1階', '89', '10'), ('2階', '118', '08'), ('3階', '46', '73')]
F_NG = [('2階', '118', '08'), ('3階', '46', '73')]
GENIN = '②③平成28年７月21日構造変更、<br>増築'

ROW1 = entry_row('', ink('居宅'), ink(S_OLD), F_OLD, '')
ROW2 = entry_row('', '', ink(S_NEW), F_NEW, ink(GENIN))

TABLE = (f'<table class="t">{COLS}'
         f'<tr><td class="lab2 val" colspan="2">不動産番号</td><td class="val center" colspan="5">記載省略</td></tr>'
         f'<tr><td class="vert" rowspan="9">建物の表示</td><td class="lab2" rowspan="2">所在</td>'
         f'<td class="val" colspan="5">{ink("Ａ市Ｂ町二丁目５番地27")}</td></tr>'
         f'<tr><td class="val" colspan="4"></td><td class="val"></td></tr>'
         f'<tr><td class="lab2 val">家屋番号</td><td class="val" colspan="2">{ink("５番27")}</td>'
         f'<td class="val" colspan="3"></td></tr>'
         f'<tr>{HEAD}</tr>{ROW1}{ROW2}{EMPTY_ROW}{EMPTY_ROW}'
         f'<tr><td class="last" colspan="6"></td></tr></table>')

kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物表題部変更登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:110px">{ink('建物図面　各階平面図　所有権証明書　代理権限証書')}</div></div>
<div class="dateline">平成28年８月10日　申請　Ａ　地方法務局　Ｂ　出張所</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:130px">{ink('Ａ市Ｂ町二丁目５番10号　乙山和雄')}</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div>（略）</div></div>
{TABLE}
<div class="caption">平成28年度 土地家屋調査士試験 第22問 登記申請書 解答例</div>
</div>''')

DAI2_TEXT = ('新館は、既存建物との間が木製のドアで仕切られているので構造上の独立性はあるが、勝手口等がなく、'
             '道路等への出入りに既存建物の2階の居間と1階の玄関を通らなければならないので、利用上の独立性がない。'
             'したがって新館は区分建物にならず、既存建物と1個の建物となるので、一不動産一登記記録の原則により、'
             '新館と渡り廊下を既存建物の増築として、既存建物の建物表題部変更登記を申請した。')
dai2 = page(f'''<div class="page"><div class="sec">第2欄</div><div class="kijutsu">{ink(DAI2_TEXT)}</div>
<div class="caption">平成28年度 土地家屋調査士試験 第22問 問2（第2欄）解答例</div></div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：変更前・変更後の2行 ----
def snippet(row2, good=False):
    g = ' class="t good"' if good else ' class="t"'
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><table{g}>{COLS}'
            f'<tr><td class="vert" rowspan="3" style="letter-spacing:0.2em">建物の表示</td>{HEAD}</tr>'
            f'{ROW1}{row2}</table>{chk}</div>')


S_FIX = (ink('軽量鉄骨造合金<br>メッキ鋼板ぶき') + '<br><span class="red" style="font-size:15px">∨渡廊下付き</span>'
         + '<span class="circle">' + ink('３階建') + '</span>')
INTS_FIX = ('<span class="caret">∨</span><span class="red">1階　89</span><br>'
            + br(ink('2階　118'), ink('3階　46')))

def fix_row():
    decs = '<span class="red">10</span><br>' + br(ink('08'), ink('73'))
    return (f'<tr><td class="entry center"></td><td class="entry center"></td><td class="entry center">{S_FIX}</td>'
            f'<td class="entry int">{INTS_FIX}</td><td class="entry dec">{decs}</td>'
            f'<td class="entry genin">{ink(GENIN)}</td></tr>')


ng_panel = snippet(entry_row('', '', ink(S_NG), F_NG, ink(GENIN)))
fix_panel = snippet(fix_row()) + \
    ('<div class="bubrow"><span class="bubble">渡り廊下でつながった一棟の建物は「渡廊下付き３階建」（準則第81条）<br>'
     '変わらない1階89.10も、変更後の床面積として書く！<br>新館の1階は全体の2階（階は建物全体で通して数える）</span></div>')
ok_panel = snippet(ROW2, good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成28年度 第22問｜渡廊下付きと、変わらない階の床面積を落とさない</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 100})   # 高さは内容に合わせる（full_page）
        for name, html in [('H28_dai22mon_toukishinseisho_kansei', kansei),
                           ('H28_dai22mon_toukishinseisho_machigai', machigai),
                           ('H28_dai22mon_dai2ran_kansei', dai2)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（要確認）'))
        browser.close()
