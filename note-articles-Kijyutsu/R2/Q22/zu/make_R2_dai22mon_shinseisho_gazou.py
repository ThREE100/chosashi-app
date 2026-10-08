"""令和2年度 第22問（建物）登記申請書の画像（第1欄・第3欄の完成形、第2欄の完成形、第3欄の原因の添削）を、
HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形（第1欄・第3欄）：`../prompt_R2_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  第1欄は建物の表示の表の下に、住所変更の登記の義務化（不動産登記法第76条の5。出題当時はなかった）の注を入れる。
  欄の形は試験の答案用紙に合わせる：登記の目的・添付書類・申請人は記入枠、その下に代理人の「（略）」と
  「令和2年10月16日　申請　Ａ地方法務局」が印刷。建物の表示は所在の行、家屋番号の行（第1欄は記入、第3欄は「（記載不要）」が印刷）、
  見出し行「主である建物又は附属建物・①種類・②構造・③床面積（右下に小さくm²）・原因及びその日付」、記入行（第1欄は2行、第3欄は大きな1行）。
  登録免許税の欄はない。以上は試験の答案用紙（`../touan_youshi/R2_dai22mon_touan_youshi.pdf` の1ページ目）で確かめた
- 第2欄：①「解体移転の場合／えい行移転の場合」に印刷の「有・無」と記入欄（「有・無」と同じ欄の右側に書く）、②理由の欄
  （答案用紙では①の枠が第1欄の下、②の枠が右の列の上にある。画像では2つの枠を縦に並べる）
- 添削：`../prompt_R2_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）。
  第3欄の原因のほか、2026-10-08に第1欄の申請人・添付書類・建物の表示（主である建物の行）の添削を欄ごとに1枚ずつ足した

CSSと部品の作りは `R6/Q22/zu/make_R6_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/R2/Q22/zu/make_R2_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.page.short {{ min-height: 1300px; }}
.page .caption {{ margin-top: auto; padding-top: 30px; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 48px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 26px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 22px; }}
.plainrow .lab {{ padding-top: 0; }}
.plainrow .ryaku {{ flex: 1; text-align: center; }}
.plainrow .printed {{ flex: 1; letter-spacing: 0.05em; }}
table.bldg {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.bldg td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 10px; vertical-align: middle; line-height: 1.5; }}
table.bldg td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.bldg td.vert.tight {{ letter-spacing: 0.15em; font-size: 20px; }}
table.bldg td.lab2 {{ text-align: center; font-size: 19px; }}
table.bldg td.head {{ text-align: center; font-size: 18px; height: 70px; }}
table.bldg td.val {{ height: 64px; }}
table.bldg td.entry {{ height: 170px; }}
table.bldg td.entry.big {{ height: 330px; }}
table.bldg td.center {{ text-align: center; }}
table.bldg td.head .m2 {{ display: block; text-align: right; padding-right: 22%; font-size: 15px; line-height: 1.2; }}
table.bldg td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.bldg td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.bldg td.genin {{ font-size: 17px; }}
table.bldg td .ink {{ font-size: 20px; }}
table.ran2 {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.ran2 td {{ border: 1.5px solid #111; font-size: 21px; padding: 14px 16px; height: 170px; vertical-align: middle; }}
table.ran2 td.no {{ text-align: center; font-size: 24px; }}
table.ran2 td .ink {{ font-size: 23px; }}
.circ {{ display: inline-block; border: 2.5px solid {INK}; border-radius: 50%; width: 38px; height: 38px; line-height: 33px;
         text-align: center; }}
.plain {{ display: inline-block; width: 38px; text-align: center; }}
.tnote {{ font-size: 17px; color: #444; margin-top: 12px; line-height: 1.6;
          font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 30px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.panel.tall {{ min-height: 380px; }}
.strike {{ text-decoration: line-through; text-decoration-color: {RED}; text-decoration-thickness: 3px; }}
.panel:last-of-type {{ border-bottom: none; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.ring {{ border: 3px solid {RED}; border-radius: 50%; padding: 2px 8px; }}
.red {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; }}
.caret {{ color: {RED}; font-weight: bold; font-size: 26px; margin-right: 2px; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 21px; font-weight: bold; background: #fff5f5; line-height: 1.5;
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

COLS = ('<colgroup><col style="width:5%"><col style="width:11%"><col style="width:12%"><col style="width:21%">'
        '<col style="width:14%"><col style="width:7%"><col style="width:30%"></colgroup>')
HEAD = ('<tr><td class="head lab2">主である<br>建物又は<br>附属建物</td><td class="head">①種　類</td>'
        '<td class="head">②構　造</td><td class="head" colspan="2">③床面積<br><span class="m2">m²</span></td>'
        '<td class="head">原因及びその日付</td></tr>')


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def br(*lines):
    return '<br>'.join(lines)


def page(body, cls='page'):
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body><div class="{cls}">{body}</div></body></html>')


def area(floors, big=False):
    """床面積の整数部・小数部のセル。floors: [(階の表示, 整数部, 小数部)]"""
    b = ' big' if big else ''
    ints = br(*[ink(f'{k}　{a}' if k else a) for k, a, _ in floors])
    decs = br(*[ink(d) for _, _, d in floors])
    return f'<td class="entry{b} int">{ints}</td><td class="entry{b} dec">{decs}</td>'


def entry_row(label='', kind='', struct='', floors=(('', '', ''),), genin='', big=False):
    b = ' big' if big else ''
    return (f'<tr><td class="entry{b} lab2">{label}</td><td class="entry{b} center">{kind}</td>'
            f'<td class="entry{b} center">{struct}</td>{area(floors, big)}<td class="entry{b} genin">{genin}</td></tr>')


def table(shozai, kaoku_html, rows_html, nrows):
    return (f'<table class="bldg">{COLS}'
            f'<tr><td class="lab2 val" colspan="2">所　在</td><td class="val" colspan="5">{ink(shozai)}</td></tr>'
            f'<tr><td class="vert" rowspan="{nrows + 2}">建物の表示</td>'
            f'<td class="lab2 val">家屋番号</td><td class="val" colspan="5">{kaoku_html}</td></tr>'
            f'{HEAD}{rows_html}</table>')


def front(mokuteki, tenpu_lines, shinseinin_lines):
    return (f'<div class="title">登記申請書</div>'
            f'<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink(mokuteki)}</div></div>'
            f'<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:130px">{ink(br(*tenpu_lines))}</div></div>'
            f'<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:100px">{ink(br(*shinseinin_lines))}</div></div>'
            '<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>'
            '<div class="plainrow"><div class="printed">令和２年10月16日　申請　Ａ地方法務局</div></div>')


SHINSEININ = ['Ａ市Ｂ区Ｔ町三丁目42番地２', '五輪松子']
NOTE1 = ('※今の法令では、所有権の登記名義人の住所が変わったら、2年以内に住所変更の登記を申請する義務がある（不動産登記法'
         '第76条の5。令和3年の改正で新設され、出題当時はなかった）。滅失登記で閉鎖される本件旧建物の登記記録の住所を先に直す'
         '必要はなく、この申請書の記入は今の法令でも同じ（変更証明書を付けて今の住所で申請する）')

# ---- 第1欄（問1）：本件旧建物の建物滅失登記 ----
rows1 = (entry_row('主', ink(br('居宅', '・', '店舗')), ink(br('木造スレート葺', '２階建')), [('1階', '84', '05'), ('2階', '26', '49')],
                   ink(br('令和２年10月12日', '取壊し')))
         + entry_row('符号１', ink('車庫'), ink(br('鉄骨造合金メッキ', '鋼板葺平家建')), [('', '50', '45')], ''))
toi1 = page(front('建物滅失登記', ['変更証明書　代理権限証書'], SHINSEININ)
            + table('Ａ市Ｂ区Ｔ町三丁目39番地３', ink('39番３の４'), rows1, 2)
            + f'<div class="tnote">{NOTE1}</div>'
            + '<div class="caption">令和2年度 土地家屋調査士試験 第22問 問1（第1欄） 登記申請書 解答例</div>')

# ---- 第3欄（問3）：本件新建物の建物表題登記 ----
GENIN_OK = br('令和２年９月18日新築', '令和２年10月12日増築')
FLOORS3 = [('1階', '71', '40'), ('2階', '71', '40'), ('3階', '64', '02')]
KIND3 = br('共同住宅', '・', '店舗')
STRUCT3 = br('鉄骨造合金メッキ', '鋼板ぶき３階建')
rows3 = entry_row('', ink(KIND3), ink(STRUCT3), FLOORS3, ink(GENIN_OK), big=True)
toi3 = page(front('建物表題登記', ['建物図面　各階平面図　所有権証明書', '住所証明書　代理権限証書'], SHINSEININ)
            + table('Ａ市Ｂ区Ｔ町三丁目42番地２、42番地１', '（記載不要）', rows3, 1)
            + '<div class="caption">令和2年度 土地家屋調査士試験 第22問 問3（第3欄） 登記申請書 解答例</div>')


# ---- 第2欄（問2） ----
def umu(yes):
    a = '<span class="circ ink">有</span>' if yes else '<span class="plain">有</span>'
    b = '<span class="circ ink">無</span>' if not yes else '<span class="plain">無</span>'
    return f'{a}・{b}'


RAN2_COLS = '<colgroup><col style="width:8%"><col style="width:24%"><col style="width:68%"></colgroup>'
dai2 = page(
    '<div class="ptitle" style="font-family:inherit;font-weight:normal;font-size:26px">第２欄</div>'
    f'<table class="ran2">{RAN2_COLS}'
    f'<tr><td class="no" rowspan="2">①</td><td>解体移転の場合</td><td>{umu(True)}　　{ink("建物滅失登記、建物表題登記")}</td></tr>'
    f'<tr><td>えい行移転の場合</td><td>{umu(False)}</td></tr></table>'
    '<div style="height:30px"></div>'
    f'<table class="ran2">{RAN2_COLS}'
    f'<tr><td class="no" rowspan="2">②</td><td>解体移転の場合</td><td>{ink("解体によって建物の同一性が失われるため")}</td></tr>'
    f'<tr><td>えい行移転の場合</td><td>{ink(br("建物の同一性は失われず、同じ土地の中での移動で", "所在に変更が生じないため"))}</td></tr></table>'
    '<div class="caption">令和2年度 土地家屋調査士試験 第22問 問2（第2欄） 解答例</div>', cls='page short')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：第3欄の原因及びその日付 ----
def snippet(genin_html, good=False, floor_html=None):
    g = ' class="good"' if good else ''
    chk = CHECK_SVG if good else ''
    fl = floor_html or area(FLOORS3)
    row = (f'<tr><td class="entry lab2"></td><td class="entry center">{ink(KIND3)}</td><td class="entry center">{ink(STRUCT3)}</td>'
           f'{fl}<td class="entry genin">{genin_html}</td></tr>')
    return (f'<div class="okwrap"><table class="bldg"{g}>{COLS}'
            f'<tr><td class="vert tight" rowspan="2">建物の表示</td>'
            '<td class="head lab2">主である<br>建物又は<br>附属建物</td><td class="head">①種　類</td><td class="head">②構　造</td>'
            f'<td class="head" colspan="2">③床面積<br><span class="m2">m²</span></td><td class="head">原因及びその日付</td></tr>{row}</table>{chk}</div>')


ng_panel = snippet(ink('令和２年９月18日新築'))
ring_floor = ('<td class="entry int">' + br(f'<span class="ring">{ink("1階　71")}</span>', ink('2階　71'), ink('3階　64'))
              + '</td><td class="entry dec">' + br(ink('40'), ink('40'), ink('02')) + '</td>')
fix_genin = (ink('令和２年９月18日新築') + '<br><span class="caret">∧</span>'
             '<span class="red">令和２年10月12日増築</span>')
fix_panel = snippet(fix_genin, floor_html=ring_floor) + \
    ('<div class="bubrow"><span class="bubble">1階の71.40㎡は10月12日の工事後の姿（9月18日の新築時は66.15㎡）<br>'
     '旧ポーチ1.50×3.50＝5.25㎡をエントランスにした工事＝増築。新築と増築を併記！</span></div>')
ok_panel = snippet(ink(GENIN_OK), good=True)
machigai = (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>'
            f'<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>'
            f'<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>'
            '<div class="caption" style="margin:10px 0 30px">令和2年度 第22問｜表題登記の前に増築したら、新築と増築を併記する</div>'
            '</body></html>')


# ---- 添削（2026-10-08追加）：第1欄の欄ごとに1枚（申請人・添付書類・建物の表示の主である建物の行）。3コマを縦に積む ----
def three(name_cap, ng_html, fix_html, ok_html):
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="panel tall"><div class="ptitle ng">①誤答</div>{ng_html}</div>'
            f'<div class="panel tall"><div class="ptitle fix">②添削（赤ペン）</div>{fix_html}</div>'
            f'<div class="panel tall"><div class="ptitle ok">③正解</div>{ok_html}</div>'
            f'<div class="caption" style="margin:10px 0 30px">{name_cap}</div></body></html>')


def boxrow(label, inner, good=False, height=100):
    g = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return (f'<div class="row okwrap"><div class="lab">{label}</div>'
            f'<div class="box{g}" style="min-height:{height}px">{inner}</div>{chk}</div>')


def bubble(text):
    return f'<div class="bubrow" style="margin-bottom:22px"><span class="bubble">{text}</span></div>'


# 申請人の欄：登記記録の住所（39番地３）を写した誤答 → 今の住所（42番地２）
OLD_ADDR, NEW_ADDR = 'Ａ市Ｂ区Ｔ町三丁目39番地３', 'Ａ市Ｂ区Ｔ町三丁目42番地２'
AFTER = ('<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>'
         '<div class="plainrow"><div class="printed">令和２年10月16日　申請　Ａ地方法務局</div></div>')
machigai_shinseinin = three(
    '令和2年度 第22問｜申請人の住所は、申請するときの今の住所',
    boxrow('申　　請　　人', ink(br(OLD_ADDR, '五輪松子'))) + AFTER,
    boxrow('申　　請　　人', br(f'<span class="ink strike">{OLD_ADDR}</span>　<span class="red">{NEW_ADDR}</span>', ink('五輪松子')))
    + bubble('10月3日に42番地２へ転居（事実関係3）。登記記録の住所を写さない') + AFTER,
    boxrow('申　　請　　人', ink(br(NEW_ADDR, '五輪松子')), good=True) + AFTER)

# 添付書類の欄：住所証明書の誤答 → 変更証明書
MOKUTEKI = boxrow('登記の目的', ink('建物滅失登記'), height=62)
machigai_tenpu = three(
    '令和2年度 第22問｜滅失登記に付けるのは、住所のつながりを示す変更証明書',
    MOKUTEKI + boxrow('添　付　書　類', ink('住所証明書　代理権限証書'), height=90),
    MOKUTEKI + boxrow('添　付　書　類', f'<span class="ink strike">住所証明書</span>　<span class="red">変更証明書</span>　{ink("代理権限証書")}', height=90)
    + bubble('住所証明書は表題登記で新しく表題部所有者になる人の住所。<br>'
             '滅失登記は登記記録の住所（39番地３）から今の住所（42番地２）へのつながり＝変更証明書'),
    MOKUTEKI + boxrow('添　付　書　類', ink('変更証明書　代理権限証書'), good=True, height=90))


# 建物の表示（主である建物の行）：下線の付いた当初の行を写した誤答 → 下線のない最新の行
def row_main(kind, struct, ints, decs, good=False):
    g = ' class="good"' if good else ''
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><table class="bldg"{g}>{COLS}'
            f'<tr><td class="vert tight" rowspan="2">建物の表示</td>{HEAD[4:-5]}</tr>'
            f'<tr><td class="entry lab2">主</td><td class="entry center">{kind}</td><td class="entry center">{struct}</td>'
            f'<td class="entry int">{ints}</td><td class="entry dec">{decs}</td>'
            f'<td class="entry genin">{ink(br("令和２年10月12日", "取壊し"))}</td></tr></table>{chk}</div>')


def st(x):
    return f'<span class="ink strike">{x}</span>'


def rd(x):
    return f'<span class="red">{x}</span>'


machigai_hyouji = three(
    '令和2年度 第22問｜建物の表示は、下線のない最新の事項を「葺」のまま写す',
    row_main(ink('居宅'), ink(br('木造瓦葺', '２階建')), br(ink('1階　65'), ink('2階　26')), br(ink('42'), ink('49'))),
    row_main(br(st('居宅'), rd('居宅・店舗')), br(st('木造瓦葺'), rd('木造スレート葺'), ink('２階建')),
             br(st('1階　65') + ' ' + rd('84'), ink('2階　26')), br(st('42') + ' ' + rd('05'), ink('49')))
    + bubble('下線は変更されて効力のない事項。種類・床面積は平成16年、構造は昭和62年の変更後の行を写す<br>'
             '（「葺」は登記記録どおり。2階の26.49は変わっていない）'),
    row_main(ink(br('居宅', '・', '店舗')), ink(br('木造スレート葺', '２階建')), br(ink('1階　84'), ink('2階　26')),
             br(ink('05'), ink('49')), good=True))

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 800})
        for name, html in [('R2_dai22mon_toukishinseisho_kansei_toi1', toi1),
                           ('R2_dai22mon_dai2ran_kansei', dai2),
                           ('R2_dai22mon_toukishinseisho_machigai', machigai),
                           ('R2_dai22mon_toukishinseisho_kansei_toi3', toi3),
                           ('R2_dai22mon_toukishinseisho_machigai_shinseinin', machigai_shinseinin),
                           ('R2_dai22mon_toukishinseisho_machigai_tenpu', machigai_tenpu),
                           ('R2_dai22mon_toukishinseisho_machigai_hyouji', machigai_hyouji)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（要確認）'))
        browser.close()
