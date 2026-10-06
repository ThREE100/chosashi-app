"""平成23年度 第22問（建物）登記申請書の画像（第1欄の完成形、添削、第2欄の完成形）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H23_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  欄の形は試験の答案用紙（その1）の第1欄に合わせる（登記の目的・添付書類の枠、枠なしの「平成23年8月21日申請　A地方法務局」、
  申請人の枠、代理人（略）、所在は2段で2段目は左右2つの枠、家屋番号、見出し行、記入行4行。登録免許税の欄はない。
  表の左に縦書きの「建物の表示」の列はない）
- 添削　：`../prompt_H23_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第2欄：問3の記述欄（点線の罫線の枠）
- 添削2：所在の欄の①誤答・②添削・③正解（2026-10-05追加。記事の所在の欄の誤答に添削画像がなかった）

CSSと部品の作りは `R7/Q22/zu/make_R7_dai22mon_shinseisho_gazou.py` と同じ形にしている。
実行: python3 note-articles-Kijyutsu/H23/Q22/zu/make_H23_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.page {{ padding: 70px 60px 40px; min-height: 1650px; display: flex; flex-direction: column; }}
.page .caption {{ margin-top: auto; padding-top: 30px; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 48px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 26px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.dateline {{ font-size: 22px; margin: 0 0 26px; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 26px; }}
.plainrow .ryaku {{ padding-left: 20px; padding-top: 10px; }}
table.bldg {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.bldg td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 10px; vertical-align: middle; line-height: 1.5; }}
table.bldg td.lab2 {{ text-align: center; font-size: 19px; }}
table.bldg td.head {{ text-align: center; font-size: 18px; height: 70px; }}
table.bldg td.val {{ height: 64px; }}
table.bldg td.entry {{ height: 150px; }}
table.bldg td.center {{ text-align: center; }}
table.bldg td.struct {{ font-size: 17px; }}
table.bldg td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.bldg td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.bldg td.genin {{ font-size: 17px; }}
table.bldg td .ink {{ font-size: 20px; }}
table.bldg td.struct .ink, table.bldg td.genin .ink {{ font-size: 18px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 30px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 第2欄 */
.ran2 {{ border: 3px solid #111; margin: 0 40px; padding: 6px 24px 20px; }}
.ran2 .line {{ border-bottom: 1.5px dashed #777; height: 46px; font-size: 22px; line-height: 46px; white-space: nowrap; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.tall .panel {{ padding: 50px 60px 54px; }}
.panel:last-of-type {{ border-bottom: none; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.strike {{ position: relative; }}
.strike::after {{ content: ""; position: absolute; left: -4px; right: -4px; top: 52%; border-top: 3px solid {RED};
                  transform: rotate(-3deg); }}
.red {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; }}
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

# 列（答案用紙の比率）：主である建物又は附属建物・①種類・②構造・③床面積（整数部・小数部）・登記原因及びその日付
COLS = ('<colgroup><col style="width:13%"><col style="width:9%"><col style="width:31%">'
        '<col style="width:12%"><col style="width:8%"><col style="width:27%"></colgroup>')
HEAD = ('<tr><td class="head lab2">主である建物<br>又は附属建物</td><td class="head">①種類</td>'
        '<td class="head">②構　造</td><td class="head" colspan="2">③床面積<br>（m²）</td>'
        '<td class="head">登記原因<br>及びその日付</td></tr>')


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def br(*lines):
    return '<br>'.join(lines)


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def area(*floors, cls='entry'):
    ints = br(*[ink(f'{k}　{a}' if k else a) for k, a, _ in floors])
    decs = br(*[ink(b) for _, _, b in floors])
    return f'<td class="{cls} int">{ints}</td><td class="{cls} dec">{decs}</td>'


def entry_row(label, kind, struct, floors, genin):
    return (f'<tr><td class="entry lab2">{label}</td><td class="entry center">{kind}</td>'
            f'<td class="entry struct">{struct}</td>{area(*floors)}<td class="entry genin">{genin}</td></tr>')


SHOZAI = 'Ａ市Ｂ町二丁目５番地２'
S_OMOYA = '木造かわらぶき２階建'
S_ITTO = 'Ａ市Ｂ町五丁目10番地１　コンクリートブロック造陸屋根平家建　床面積49.50㎡'
S_SENYU = 'コンクリートブロック造陸屋根平家建'
S_SHIKICHI = '敷地権の表示　Ａ市Ｂ町五丁目10番１　宅地　792.95㎡の土地の所有権6分の2'
G_ZOU = '③平成23年8月2日増築'
G_SHIN, G_SHIKI = '平成23年8月2日新築', '平成23年8月4日敷地権'

rows = (entry_row(ink('主'), ink('居宅'), ink(S_OMOYA), [('1階', '82', '81'), ('2階', '66', '24')], '')
        + entry_row('', '', '', [('1階', '98', '73'), ('2階', '66', '24')], ink(G_ZOU))
        + entry_row(ink('符号1'), ink('車庫'), br(ink(S_ITTO), ink(S_SENYU)), [('', '23', '82')], br(ink(G_SHIN), ink(G_SHIKI)))
        + entry_row('', '', ink(S_SHIKICHI), [('', '', '')], ''))
table = (f'<table class="bldg">{COLS}'
         f'<tr><td class="lab2" rowspan="2">所　在</td><td class="val" colspan="5">{ink(SHOZAI)}</td></tr>'
         f'<tr><td class="val" colspan="3"></td><td class="val" colspan="2"></td></tr>'
         f'<tr><td class="lab2 val">家屋番号</td><td class="val" colspan="5">{ink("５番２")}</td></tr>'
         f'{HEAD}{rows}</table>')
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物表題部変更登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:62px">{ink('建物図面　各階平面図　所有権証明書　代理権限証書')}</div></div>
<div class="dateline">平成23年8月21日申請　　Ａ地方法務局</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:110px">{ink('Ａ市Ｂ町二丁目５番地２　畑山邦彦')}</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{table}
<div class="caption">平成23年度 土地家屋調査士試験 第22問 問1 登記申請書 解答例</div>
</div>''')

# ---- 第2欄（問3） ----
DAI2 = ('車庫が、家屋番号5番2の建物（居宅）の効用を補うために利用されていない場合は、附属建物と認められない。'
        '附属建物は、表題登記がある建物に附属し、その建物と一体のものとして1個の建物として登記される建物であり'
        '（不動産登記法第2条第23号）、数棟の建物を1個の建物として取り扱うのは、効用上一体として利用される状態にある場合である'
        '（不動産登記事務取扱手続準則第78条第1項）。所有者が同じで、所有者が附属建物として登記することを望んでも、'
        'この状態になければ1個の建物にはならないからである。例えば、畑山邦彦が車庫を第三者に賃貸し、その第三者が自己の自動車の'
        '車庫として利用している場合や、居宅の居住者のためではなく10番1の建物の事務所の来客用の車庫として利用されている場合が'
        'これに当たる。この場合、車庫は独立した1個の建物（区分建物）として表題登記をすることになる。')
PER = 44
chunks = [DAI2[i:i + PER] for i in range(0, len(DAI2), PER)]
lines = ''.join(f'<div class="line">{ink(c)}</div>' for c in chunks) + ''.join('<div class="line"></div>' for _ in range(3))
dai2ran = page(f'''<div style="padding:50px 20px 30px">{'<div class="ran2">' + lines + '</div>'}
<div class="caption">平成23年度 土地家屋調査士試験 第22問 問3（第2欄）解答例</div></div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：符号1の行 ----
def snippet(rows_, good=False):
    g = ' class="good"' if good else ''
    chk = CHECK_SVG if good else ''
    return f'<div class="okwrap"><table class="bldg"{g}>{COLS}{HEAD}{rows_}</table>{chk}</div>'


ng_panel = snippet(entry_row(ink('符号1'), ink('車庫'), ink(S_SENYU), [('', '24', '75')], ink(G_SHIN)))
fix_rows = (f'<tr><td class="entry lab2">{ink("符号1")}</td><td class="entry center">{ink("車庫")}</td>'
            f'<td class="entry struct"><span class="red">{S_ITTO}</span><br>{ink(S_SENYU)}</td>'
            f'<td class="entry int"><span class="ink strike">24</span><br><span class="red">23</span></td>'
            f'<td class="entry dec"><span class="ink strike">75</span><br><span class="red">82</span></td>'
            f'<td class="entry genin">{ink(G_SHIN)}<br><span class="red">{G_SHIKI}</span></td></tr>'
            f'<tr><td class="entry lab2"></td><td class="entry"></td><td class="entry struct"><span class="red">{S_SHIKICHI}</span></td>'
            f'<td class="entry int"></td><td class="entry dec"></td><td class="entry"></td></tr>')
fix_panel = snippet(fix_rows) + ('<div class="bubrow"><span class="bubble">区分建物の附属建物は、一棟の建物の所在・構造・床面積と敷地権も書く！<br>'
                                  '床面積は内法（北のシャッターは引かない）<br>敷地権は持分を取得した8月4日</span></div>')
ok_panel = snippet(entry_row(ink('符号1'), ink('車庫'), br(ink(S_ITTO), ink(S_SENYU)), [('', '23', '82')], br(ink(G_SHIN), ink(G_SHIKI)))
                   + entry_row('', '', ink(S_SHIKICHI), [('', '', '')], ''), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成23年度 第22問｜区分建物の附属建物は、一棟の建物と敷地権まで書く</div>''')


# ---- 添削2（2026-10-05追加）：所在の欄（①誤答 → ②添削 → ③正解 を縦に3コマ） ----
SHOZAI_NG = 'Ａ市Ｂ町二丁目５番地２、Ａ市Ｂ町五丁目10番地１'
G_SHOZAI_NG = '平成23年8月2日変更'


def shozai_snippet(row2_left, row2_right, good=False):
    g = ' class="good"' if good else ''
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><table class="bldg"{g}>{COLS}'
            f'<tr><td class="lab2" rowspan="2">所　在</td><td class="val" colspan="5">{ink(SHOZAI)}</td></tr>'
            f'<tr><td class="val" colspan="3">{row2_left}</td><td class="val genin" colspan="2">{row2_right}</td></tr>'
            f'<tr><td class="lab2 val">家屋番号</td><td class="val" colspan="5">{ink("５番２")}</td></tr></table>{chk}</div>')


ng2_panel = shozai_snippet(ink(SHOZAI_NG), ink(G_SHOZAI_NG))
fix2_panel = (shozai_snippet(f'<span class="ink strike">{SHOZAI_NG}</span>', f'<span class="ink strike">{G_SHOZAI_NG}</span>')
              + ('<div class="bubrow"><span class="bubble">区分建物である附属建物は、一棟の建物の所在を登記する（法第44条第1項第5号かっこ書き）。<br>'
                 'その所在は符号1の「構造」の欄に書く（規則別表二）ので、所在の欄は5番地2のまま。<br>'
                 '所在の変更は起きていないので、2段目も原因も空欄（建物図面の所在だけ2筆）</span></div>'))
ok2_panel = shozai_snippet('', '', good=True)
machigai_shozai = page(f'''<div class="tall" style="min-height:1320px; display:flex; flex-direction:column; justify-content:space-between">
<div class="panel"><div class="ptitle ng">①誤答</div>{ng2_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix2_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok2_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成23年度 第22問｜申請書の所在の欄は主である建物の5番地2のまま</div></div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 800})
        for name, html in [('H23_dai22mon_toukishinseisho_kansei', kansei),
                           ('H23_dai22mon_toukishinseisho_kansei_dai2ran', dai2ran),
                           ('H23_dai22mon_toukishinseisho_machigai', machigai),
                           ('H23_dai22mon_toukishinseisho_machigai_shozai', machigai_shozai)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
        browser.close()
