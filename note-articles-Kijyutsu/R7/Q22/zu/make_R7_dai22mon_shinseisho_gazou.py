"""令和7年度 第22問（建物）登記申請書の画像（問1・問2の完成形、添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_R7_dai22mon_toukishinseisho_gazou.md` の記入データ1（問1）・記入データ2（問2）どおり。縦長（横1200px）。
  欄の形は試験の答案用紙（`../touan_youshi/R7_dai22mon_touan_youshi.pdf` の1ページ目、第1欄・第2欄）で確かめた形
  （見出し「第1欄」「第2欄」、所在は2段で2段目の右端に原因、第1欄は家屋番号の記入欄の右に印刷の「（略）」、
  第2欄は申請人・代理人・家屋番号〈仕切りのない1つの欄〉・①種類の列〈4行をまとめた1つの欄〉が印刷の「（略）」、
  申請の日付は「令和　年　月　日」の枠に数字を記入。登録免許税の欄はない）
- 添削　：`../prompt_R7_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）。
  誤答の欄ごとに1枚（2026-10-08、最新の執筆指示書との照らし直しで3枚を追加して4枚）：
  符号（第2欄。守衛所を符号4のまま）、所在（第1欄。変更後の段を空欄）、原因の欄番号（第1欄の新しい主である建物の行に①③）、
  耐震補強（第2欄の主である建物の行に原因を書く）。第1欄の添削は第1欄の形（①種類の列に記入）、第2欄の添削は第2欄の形（①種類の列は印刷の「（略）」）
- 第4欄（問4のア〜エ。2026-10-02追加）：申請書でない解答欄も、記号ごとの記入欄の形で別の画像にする（横1200px）。
  試験の答案用紙（1ページ目の右下）の形どおり、2行2列（上の行がアとイ、下の行がウとエ）に記号と記入欄を並べる。
  答えは〔語句群〕から選んだ文言をそのまま書く

CSSと部品の作りは `R7/Q21/zu/make_R7_dai21mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/R7/Q22/zu/make_R7_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.ranlab {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; font-size: 22px; margin: -30px 0 0; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 48px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 26px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.dateline {{ display: flex; align-items: center; font-size: 22px; margin: 4px 0 26px; }}
.datebox {{ border: 2px solid #111; padding: 12px 18px; width: 470px; display: flex; justify-content: space-between; }}
.datebox .ink {{ font-size: 26px; }}
.dateline .kyoku {{ padding-left: 26px; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 22px; }}
.plainrow .ryaku {{ flex: 1; text-align: center; }}
table.bldg {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.bldg td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 10px; vertical-align: middle; line-height: 1.5; }}
table.bldg td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.bldg td.vert.tight {{ letter-spacing: 0.15em; font-size: 20px; }}
table.bldg td.lab2 {{ text-align: center; font-size: 19px; }}
table.bldg td.head {{ text-align: center; font-size: 18px; height: 70px; }}
table.bldg td.val {{ height: 64px; }}
table.bldg td.entry {{ height: 120px; }}
table.bldg td.center {{ text-align: center; }}
table.bldg td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.bldg td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.bldg td.genin {{ font-size: 17px; }}
table.bldg td .ink {{ font-size: 20px; }}
table.bldg td.genin .ink {{ font-size: 18px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 30px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
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
.tall {{ min-height: 1320px; display: flex; flex-direction: column; justify-content: space-around; }}  /* 縦長にそろえる */
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; background: #f1faf2; }}
.okwrap {{ position: relative; }}
.check {{ position: absolute; right: -14px; top: -22px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

COLS = ('<colgroup><col style="width:5%"><col style="width:12%"><col style="width:14%"><col style="width:21%">'
        '<col style="width:10%"><col style="width:6%"><col style="width:32%"></colgroup>')
HEAD = ('<tr><td class="head lab2">主である<br>建物又は<br>附属建物</td><td class="head">①種　類</td>'
        '<td class="head">②構　造</td><td class="head" colspan="2">③床　面　積<br>（m²）</td>'
        '<td class="head">登記原因及び<br>その日付</td></tr>')


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def br(*lines):
    return '<br>'.join(lines)


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def area(*floors):
    """床面積の整数部・小数部のセル。floors: [(階の表示, 整数部, 小数部)]。階の表示が空なら数値だけ"""
    ints = br(*[ink(f'{k}{a}') for k, a, _ in floors])
    decs = br(*[ink(b) for _, _, b in floors])
    return f'<td class="entry int">{ints}</td><td class="entry dec">{decs}</td>'


def entry_row(label, kind, struct, floors, genin, label_rows=1, kind_cell=True):
    lab = '' if label is None else f'<td class="entry lab2" rowspan="{label_rows}">{ink(label)}</td>'
    k = f'<td class="entry center">{kind}</td>' if kind_cell else ''
    return (f'<tr>{lab}{k}<td class="entry center">{struct}</td>{area(*floors)}'
            f'<td class="entry genin">{genin}</td></tr>')


def bldg_table(shozai1, shozai2, shozai2_genin, kaoku, rows, n_rows):
    """建物の表示の表（R7第22問の試験の答案用紙の形）。rows は entry_row() の結果を連結した文字列。
    kaoku が None なら第2欄の形（家屋番号の欄は仕切りがなく、印刷の「（略）」だけ）。
    それ以外は第1欄の形（家屋番号の記入欄の右に、床面積と原因の列の幅で印刷の「（略）」）"""
    if kaoku is None:
        kaoku_row = '<tr><td class="lab2 val">家屋番号</td><td class="val" colspan="5">（略）</td></tr>'
    else:
        kaoku_row = (f'<tr><td class="lab2 val">家屋番号</td><td class="val" colspan="2">{kaoku}</td>'
                     f'<td class="val center" colspan="3">（略）</td></tr>')
    return (f'<table class="bldg">{COLS}'
            f'<tr><td class="vert" rowspan="{4 + n_rows}">建物の表示</td>'
            f'<td class="lab2" rowspan="2">所　在</td><td class="val" colspan="5">{shozai1}</td></tr>'
            f'<tr><td class="val" colspan="4">{shozai2}</td><td class="val genin">{shozai2_genin}</td></tr>'
            f'{kaoku_row}{HEAD}{rows}</table>')


def dateline(y, m, d):
    return (f'<div class="dateline"><div class="datebox"><span>令　和</span><span>{ink(y)}　年</span>'
            f'<span>{ink(m)}　月</span><span>{ink(d)}　日</span></div><div class="kyoku">申請　Ｙ地方法務局</div></div>')


SHOZAI_OLD = 'Ｙ市Ｋ区Ａ町三丁目425番地５、425番地６'
SHOZAI_NEW = 'Ｙ市Ｋ区Ａ町三丁目425番地６、425番地５'
S_TETSU = '鉄骨造亜鉛メッキ鋼板ぶき２階建'
S_KEIRYO = '軽量鉄骨造亜鉛メッキ鋼板ぶき平家建'
S_SOUKO = '鉄骨造合金メッキ鋼板ぶき２階建'

# ---- 問1（本件工事1）：記入データ1 ----
rows1 = (
    entry_row('主', ink('事務所・倉庫'), ink('鉄骨造スレート葺２階建'), [('1階', '130', '00'), ('2階', '130', '00')],
              ink('令和7年1月21日取壊し'), label_rows=2)
    + entry_row(None, ink('事務所・倉庫'), ink(S_TETSU), [('1階', '123', '50'), ('2階', '123', '50')],
                br(ink('令和7年1月21日符号2の附属建物を主である建物に変更'), ink('令和7年1月31日種類変更、一部取壊し')))
    + entry_row('符号2', ink('倉庫'), ink(S_TETSU), [('1階', '138', '50'), ('2階', '123', '50')],
                ink('令和7年1月21日主である建物に変更'))
    + entry_row('符号4', ink('守衛所'), ink(S_KEIRYO), [('', '10', '00')], ''))
toi1 = page(f'''<div class="page">
<div class="ranlab">第1欄</div>
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物表題部変更登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:130px">{ink('建物図面　各階平面図　会社法人等番号　代理権限証書')}</div></div>
{dateline('７', '２', '６')}
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="min-height:130px">{ink(br('Ｙ市Ｋ区Ａ町三丁目５番６号　株式会社甲一物流', '（会社法人等番号　Ｚ）', '代表取締役　甲山一郎'))}</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{bldg_table(ink(SHOZAI_OLD), ink(SHOZAI_NEW), ink('令和7年1月21日主である建物取壊しにより変更'), ink('425番５'), rows1, 4)}
<div class="caption">令和7年度 土地家屋調査士試験 第22問 問1 登記申請書 解答例</div>
</div>''')

# ---- 問2（本件工事2）：記入データ2（①種類の列は答案用紙に印刷の「（略）」） ----
RYAKU_KIND = '<td class="entry center" rowspan="4">（略）</td>'
r_main = entry_row('主', '', ink(S_TETSU), [('1階', '123', '50'), ('2階', '123', '50')], '', kind_cell=False)
r_main = r_main.replace('<td class="entry center">', RYAKU_KIND + '<td class="entry center">', 1)
rows2 = (r_main
         + entry_row('符号4', '', ink(S_KEIRYO), [('', '10', '00')], ink('令和7年9月25日取壊し'), kind_cell=False)
         + entry_row('符号5', '', ink(S_SOUKO), [('1階', '190', '75'), ('2階', '156', '75')], ink('令和7年10月7日新築'),
                     kind_cell=False)
         + entry_row('符号6', '', ink(S_KEIRYO), [('', '10', '00')], ink('令和7年10月17日新築'), kind_cell=False))
toi2 = page(f'''<div class="page">
<div class="ranlab">第2欄</div>
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物表題部変更登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:130px">{ink(br('建物図面　各階平面図　所有権証明書', '会社法人等番号　代理権限証書'))}</div></div>
{dateline('７', '10', '23')}
<div class="plainrow"><div class="lab">申　　請　　人</div><div class="ryaku">（略）</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{bldg_table(ink(SHOZAI_NEW), '', '', None, rows2, 4)}
<div class="caption">令和7年度 土地家屋調査士試験 第22問 問2 登記申請書 解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：符号4の守衛所 ----
def snippet(rows, n_rows, good=False):
    g = ' class="good"' if good else ''
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><table class="bldg"{g}>{COLS}'
            f'<tr><td class="vert tight" rowspan="{1 + n_rows}">建物の表示</td>'
            f'{HEAD[4:]}{rows}</table>{chk}</div>')


def ryaku_row(label, struct, floors, genin, kind_rows=1):
    """第2欄の記入行。①種類の列は答案用紙のとおり、行をまとめた1つの欄に印刷の「（略）」（kind_rows=0 ならその欄を置かない）"""
    kind = f'<td class="entry center" rowspan="{kind_rows}">（略）</td>' if kind_rows else ''
    return (f'<tr><td class="entry lab2">{label}</td>{kind}'
            f'<td class="entry center">{struct}</td>{area(*floors)}<td class="entry genin">{genin}</td></tr>')


ng_panel = snippet(ryaku_row(ink('符号4'), ink(S_KEIRYO), [('', '10', '00')], ink('令和7年10月17日新築')), 1)
fix_panel = snippet(ryaku_row(ink('符号4'), ink(S_KEIRYO), [('', '10', '00')],
                              f'<span class="ink strike">令和7年10月17日新築</span><br><span class="red">令和7年9月25日取壊し</span>'), 1) + \
    ('<div class="bubrow"><span class="bubble">取り壊した時点で符号4は終わり！<br>'
     '建て直した守衛所は、新しい符号6の新築として別の行に書く</span></div>')
ok_panel = snippet(ryaku_row(ink('符号4'), ink(S_KEIRYO), [('', '10', '00')], ink('令和7年9月25日取壊し'), kind_rows=2)
                   + ryaku_row(ink('符号6'), ink(S_KEIRYO), [('', '10', '00')], ink('令和7年10月17日新築'), kind_rows=0),
                   2, good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答（第2欄）</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">令和7年度 第22問｜取り壊した建物は、同じ符号で生き返らない</div>''')

# ---- 添削（2026-10-08追加）：所在（第1欄）。変更後の段を空欄にした誤答 ----
def shozai_snippet(row2, row2_genin, good=False):
    g = ' class="good"' if good else ''
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><table class="bldg"{g}>{COLS}'
            f'<tr><td class="vert tight" rowspan="2">建物の表示</td>'
            f'<td class="lab2" rowspan="2">所　在</td><td class="val" colspan="5">{ink(SHOZAI_OLD)}</td></tr>'
            f'<tr><td class="val" colspan="4" style="height:76px">{row2}</td><td class="val genin">{row2_genin}</td></tr>'
            f'</table>{chk}</div>')


GENIN_SHOZAI = '令和7年1月21日主である建物取壊しにより変更'
sz_ng = shozai_snippet('', '')
sz_fix = shozai_snippet(f'<span class="red">{SHOZAI_NEW}</span>', f'<span class="red">{GENIN_SHOZAI}</span>') + \
    ('<div class="bubrow"><span class="bubble">主である建物がある土地の地番を先に書く（準則第88条第2項）。<br>'
     '主が425番６の上に移ったので、順番が入れ替わる。順番の変更も所在の変更</span></div>')
sz_ok = shozai_snippet(ink(SHOZAI_NEW), ink(GENIN_SHOZAI), good=True)
machigai_shozai = page(f'''<div class="tall">
<div class="panel"><div class="ptitle ng">①誤答（第1欄）</div>{sz_ng}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{sz_fix}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{sz_ok}</div>
<div class="caption" style="margin:10px 0 30px">令和7年度 第22問｜主が入れ替われば、所在の地番の順番も入れ替わる</div></div>''')


# ---- 添削（2026-10-08追加）：新しい主である建物の行の原因に欄番号（①③）を付けた誤答（第1欄の形） ----
def shu_snippet(genin, good=False):
    g = ' class="good"' if good else ''
    chk = CHECK_SVG if good else ''
    rows = (entry_row('主', ink('事務所・倉庫'), ink('鉄骨造スレート葺２階建'), [('1階', '130', '00'), ('2階', '130', '00')],
                      ink('令和7年1月21日取壊し'), label_rows=2)
            + entry_row(None, ink('事務所・倉庫'), ink(S_TETSU), [('1階', '123', '50'), ('2階', '123', '50')], genin))
    return (f'<div class="okwrap"><table class="bldg"{g}>{COLS}'
            f'<tr><td class="vert tight" rowspan="3">建物の表示</td>{HEAD[4:]}{rows}</table>{chk}</div>')


G1 = '令和7年1月21日符号2の附属建物を主である建物に変更'
G2 = '令和7年1月31日種類変更、一部取壊し'
gn_ng = shu_snippet(br(ink(G1), ink('①③' + G2)))
gn_fix = shu_snippet(br(ink(G1), f'<span class="ink strike">①③</span><span class="ink">{G2}</span>')) + \
    ('<div class="bubrow"><span class="bubble">主である建物として種類・構造・床面積を全部書き起こす行。<br>'
     '一部の欄を直す印の欄番号（①③）は付けない</span></div>')
gn_ok = shu_snippet(br(ink(G1), ink(G2)), good=True)
machigai_genin = page(f'''
<div class="panel"><div class="ptitle ng">①誤答（第1欄）</div>{gn_ng}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{gn_fix}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{gn_ok}</div>
<div class="caption" style="margin:10px 0 30px">令和7年度 第22問｜全部を書き起こす行に欄番号は付けない</div>''')


# ---- 添削（2026-10-08追加）：耐震補強を原因に書いた誤答（第2欄の形。①種類の列は印刷の「（略）」） ----
tai_ng = snippet(ryaku_row(ink('主'), ink(S_TETSU), [('1階', '123', '50'), ('2階', '123', '50')], ink('令和7年10月1日耐震補強')), 1)
tai_fix = snippet(ryaku_row(ink('主'), ink(S_TETSU), [('1階', '123', '50'), ('2階', '123', '50')],
                            '<span class="ink strike">令和7年10月1日耐震補強</span>'), 1) + \
    ('<div class="bubrow"><span class="bubble">構造も床面積も変わらない工事は、登記事項の変更ではない。<br>'
     '書くことは何もないので、原因の欄は空欄</span></div>')
tai_ok = snippet(ryaku_row(ink('主'), ink(S_TETSU), [('1階', '123', '50'), ('2階', '123', '50')], ''), 1, good=True)
machigai_taishin = page(f'''<div class="tall">
<div class="panel"><div class="ptitle ng">①誤答（第2欄）</div>{tai_ng}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{tai_fix}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{tai_ok}</div>
<div class="caption" style="margin:10px 0 30px">令和7年度 第22問｜登記事項が変わらない工事は書かない</div></div>''')


# ---- 第4欄（問4）の完成形：試験の答案用紙の形（2行2列。上の行がアとイ、下の行がウとエ） ----
DAI4 = [('ア', '物理'), ('イ', '報告'), ('ウ', '1月'), ('エ', '10万円以下の過料')]


def anaume(title, rows, caption):
    def pair(k, v):
        return (f'<td class="lab2" style="height:84px;font-size:26px;text-align:center">{k}</td>'
                f'<td style="padding-left:22px;font-size:26px">{ink(v)}</td>')
    trs = ''.join(f'<tr>{pair(*rows[i])}{pair(*rows[i + 1])}</tr>' for i in range(0, len(rows), 2))
    return page(f'''<div style="padding:50px 60px 36px">
<div style="font-size:28px;font-weight:bold;font-family:'Noto Sans CJK JP',sans-serif;margin-bottom:10px">{title}</div>
<table class="bldg"><colgroup><col style="width:12%"><col style="width:38%"><col style="width:12%"><col style="width:38%"></colgroup>{trs}</table>
<div class="caption">{caption}</div></div>''')


dai4 = anaume('第4欄', DAI4, '令和7年度 土地家屋調査士試験 第22問 第4欄（問4）解答例')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 200})
        for name, html in [('R7_dai22mon_dai4ran_kansei', dai4),
                           ('R7_dai22mon_toukishinseisho_kansei_toi1', toi1),
                           ('R7_dai22mon_toukishinseisho_kansei_toi2', toi2),
                           ('R7_dai22mon_toukishinseisho_machigai', machigai),
                           ('R7_dai22mon_toukishinseisho_machigai_shozai', machigai_shozai),
                           ('R7_dai22mon_toukishinseisho_machigai_genin', machigai_genin),
                           ('R7_dai22mon_toukishinseisho_machigai_taishin', machigai_taishin)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else ('横長（第4欄は小さい表なので横長でよい）' if 'ran' in name else '横長（要確認）')))
        browser.close()
