"""平成22年度 第22問（建物）答案用紙の画像（問1の完成形と代位原因の添削、問2(1)の登記申請書の完成形、
登記の目的・申請人／合体前の行の構造／存続登記の表／課税価格・登録免許税の添削）を、
HTML＋ヘッドレスブラウザでPNGに書き出す。

- 問1：`../prompt_H22_dai22mon_toukishinseisho_gazou.md` の画像1。答案用紙（その1）の上の部分（(1)登記の目的・添付情報、(2)代位原因）
- 完成形：同じプロンプトの画像2。答案用紙（その1）の下の部分（登記申請書の登記の目的・添付情報・申請の日付と提出先・申請人・代理人）の下に、
  （その2）の建物の表示・「一　合体前の建物の所有権登記の表示」・「二　抵当権等の登記で合体後の登記建物につき存続すべきものの表示」・
  「法第74条第1項第1号の規定による新築建物のためにする所有権保存の登記」（課税価格・登録免許税）を縦に積んだ縦長（横1200px）。
  欄の形は試験の答案用紙に合わせる：欄の名前は「添付情報」。申請の日付と提出先（平成22年8月22日　申請　Ａ地方法務局）は申請人の上に印刷済み、
  代理人は住所・氏名・電話番号まで印刷済み（「（略）」ではない）。建物の表示は所在2段、見出し（地番・家屋番号・①種類・②構造・③床面積 m²・
  登記の原因及びその日付）、記入行3行と、仕切りのない最下段
- 添削：`../prompt_H22_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `H30/Q22/zu/make_H30_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/H22/Q22/zu/make_H22_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.toi {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; font-size: 24px; margin: 0 0 10px; }}
.sub {{ font-size: 22px; margin: 6px 0 12px; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 24px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.dateline {{ font-size: 22px; margin: 2px 0 16px 20px; }}
.dairi {{ display: flex; font-size: 22px; margin-bottom: 30px; }}
.dairi .v {{ line-height: 1.7; margin-left: 40px; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 18px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 1.2em; padding: 0; font-size: 21px; }}
table.t td.lab2 {{ text-align: center; font-size: 18px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 62px; }}
table.t td.val {{ height: 50px; }}
table.t td.entry {{ height: 118px; }}
table.t td.low {{ height: 70px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
.sec {{ font-size: 24px; margin: 38px 0 4px; }}
table.s td {{ height: 64px; text-align: center; font-size: 18px; }}
table.s td.head {{ height: 62px; font-size: 17px; }}
.taxhead {{ font-size: 24px; margin: 38px 0 10px; }}
.taxbox {{ border: 2.5px solid #111; padding: 18px 24px; font-size: 24px; line-height: 2.0; width: 80%; background: #fff; }}
.taxbox .k {{ display: inline-block; width: 150px; font-weight: bold; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 34px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 40px 60px 44px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold; margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.red {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; }}
.caret {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; font-size: 15px;
          vertical-align: super; }}
.strike {{ text-decoration: line-through; text-decoration-color: {RED}; text-decoration-thickness: 3px; }}
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
tr.cut td {{ background: #fff0f0; }}
.note {{ font-size: 20px; margin-top: 14px; color: #444; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
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


# ---- 問1（答案用紙（その1）の上の部分） ----
TOI1_PURPOSE = '建物表題部変更登記'
TOI1_ATTACH = '建物図面　各階平面図　所有権証明情報　代理権限証明情報'
TOI1_DAII = '不動産登記法第52条第4項'
toi1 = page(f'''<div class="page">
<div class="toi">問１</div><div class="sub">(1)</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:84px">{ink(TOI1_PURPOSE)}</div></div>
<div class="row"><div class="lab">添　付　情　報</div><div class="box" style="height:120px">{ink(TOI1_ATTACH)}</div></div>
<div class="sub">(2)</div>
<div class="row"><div class="lab">代　位　原　因</div><div class="box" style="height:84px">{ink(TOI1_DAII)}</div></div>
<div class="caption">平成22年度 土地家屋調査士試験 第22問 問1 解答例（答案用紙（その1）の上の部分）</div>
</div>''')

# ---- 問2(1)：登記申請書 ----
PURPOSE = '合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消並びに所有権の保存の登記'
ATTACH = ['建物図面　各階平面図　所有権証明情報　住所証明情報', '登記済証　印鑑証明書　承諾証明情報',
          '抵当権消滅承諾証明情報　代理権限証明情報']
APPLICANT = br(ink('Ａ市Ｄ町一丁目２番１号　持分　10分の４　大面太郎'),
               ink('Ａ市Ｄ町一丁目２番２号　　　　　10分の６　大面健一郎'))
DAIRI = br('Ａ市Ｆ町二丁目６番８号', '波　　臼　　良　　子', '連絡先の電話番号　０＊＊－＊＊＊＊－１２３４')

COLS = ('<colgroup><col style="width:5%"><col style="width:11%"><col style="width:10%"><col style="width:9%">'
        '<col style="width:17%"><col style="width:12%"><col style="width:6%"><col style="width:30%"></colgroup>')
HEAD = ('<td class="head">地　番</td><td class="head">家屋番号</td><td class="head">①種類</td><td class="head">②構　造</td>'
        '<td class="head" colspan="2">③床面積　m²</td><td class="head">登記の原因及びその日付</td>')


def entry_row(chiban, kaoku, kind, struct, floors, genin):
    return (f'<tr><td class="entry center">{chiban}</td><td class="entry center">{kaoku}</td>'
            f'<td class="entry center">{kind}</td><td class="entry center">{struct}</td>{area(floors)}'
            f'<td class="entry genin">{genin}</td></tr>')


ROW1 = entry_row(ink('21番地'), ink('21番'), ink('居宅'), ink('木造瓦葺<br>２階建'), [('1階', '81', '00'), ('2階', '51', '84')],
                 ink('平成22年７月30日22番と<br>合体'))
ROW2 = entry_row(ink('22番地'), ink('22番'), ink('居宅'), ink('木造セメント<br>瓦葺平家建'), [('', '68', '04')],
                 ink('平成22年７月30日21番と<br>合体'))
ROW3 = entry_row(ink(br('21番地', '22番地')), '', ink('居宅'), ink('木造スレート<br>ぶき２階建'),
                 [('1階', '194', '04'), ('2階', '51', '84')], ink('平成22年７月30日21番、<br>22番を合体'))
TABLE = (f'<table class="t">{COLS}'
         f'<tr><td class="vert" rowspan="7">建物の表示</td><td class="lab2 val" rowspan="2">所　在</td>'
         f'<td class="val" colspan="6">{ink("Ａ市Ｄ町一丁目")}</td></tr>'
         f'<tr><td class="val" colspan="6"></td></tr>'
         f'<tr>{HEAD}</tr>{ROW1}{ROW2}{ROW3}<tr><td class="low" colspan="7"></td></tr></table>')

S1_COLS = '<colgroup><col style="width:18%"><col style="width:13%"><col style="width:35%"><col style="width:34%"></colgroup>'
S1 = (f'<div class="sec">一　合体前の建物の所有権登記の表示</div><table class="t s">{S1_COLS}'
      '<tr><td class="head">家屋番号</td><td class="head">順位番号</td><td class="head">受付年月日及び受付番号</td>'
      '<td class="head">登記名義人の氏名</td></tr>'
      f'<tr><td>{ink("21番")}</td><td>{ink("１番")}</td><td>{ink("昭和51年２月17日第1110号")}</td><td>{ink("大面太郎")}</td></tr>'
      '<tr><td></td><td></td><td></td><td></td></tr></table>')
S2_COLS = ('<colgroup><col style="width:12%"><col style="width:12%"><col style="width:15%"><col style="width:23%">'
           '<col style="width:18%"><col style="width:20%"></colgroup>')
S2_HEAD = ('<tr><td class="head">家屋番号</td><td class="head">順位番号</td><td class="head">登記の<br>目的</td>'
           '<td class="head">受付年月日<br>及び受付番号</td><td class="head">登記名義人<br>の氏名</td>'
           '<td class="head">目的とする権利</td></tr>')
S2_ROW = (f'<tr><td class="entry">{ink("21番")}</td><td class="entry">{ink("乙区２番")}</td>'
          f'<td class="entry">{ink("抵当権設定")}</td><td class="entry">{ink(br("昭和51年２月17日", "第1113号"))}</td>'
          f'<td class="entry">{ink("Ｂ信用金庫")}</td><td class="entry">{ink(br("大面太郎", "持分"))}</td></tr>')
S2_EMPTY = '<tr>' + '<td class="entry" style="height:64px"></td>' * 6 + '</tr>'
S2 = (f'<div class="sec">二　抵当権等の登記で合体後の登記建物につき存続すべきものの表示</div>'
      f'<table class="t s">{S2_COLS}{S2_HEAD}{S2_ROW}{S2_EMPTY}{S2_EMPTY}</table>')

TAX_HEAD = '<div class="taxhead">法第74条第1項第1号の規定による新築建物のためにする所有権保存の登記</div>'


def taxbox(kazei, zei, extra=''):
    return (f'<div class="taxbox"><span class="k">課税価格</span>{kazei}<br>'
            f'<span class="k">登録免許税</span>{zei}{extra}</div>')


TAX_OK = taxbox(ink('金1,200万円'), ink('金４万8,000円'))

kansei = page(f'''<div class="page">
<div class="toi">問２　(1)</div>
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:100px">{ink(PURPOSE)}</div></div>
<div class="row"><div class="lab">添　付　情　報</div><div class="box" style="height:150px">{ink(br(*ATTACH))}</div></div>
<div class="dateline">平成22年８月22日　　申請　　Ａ地方法務局</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:110px">{APPLICANT}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="v">{DAIRI}</div></div>
{TABLE}
{S1}
{S2}
{TAX_HEAD}
{TAX_OK}
<div class="caption">平成22年度 土地家屋調査士試験 第22問 問2(1) 登記申請書 解答例（答案用紙（その1）の下の部分の下に（その2）を積んだもの）</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解）：課税価格・登録免許税の欄 ----
def snippet(box, good=False):
    g = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return f'<div class="okwrap"><div class="{g.strip()}" style="padding:4px 10px 12px">{TAX_HEAD}{box}</div>{chk}</div>'


ng_box = taxbox(ink('金1,260万円'), ink('金５万400円'))
fix_box = taxbox('<span class="ink strike">金1,260万円</span><span class="caret">∨</span><span class="red">金1,200万円</span>',
                 '<span class="ink strike">金５万400円</span><span class="caret">∨</span><span class="red">金４万8,000円</span>')
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{snippet(ng_box)}
<div class="sub" style="margin-top:14px;font-size:20px">（計算：1,200万＋530万＋工事費370万＝2,100万円、×10分の６＝1,260万円、×1000分の４）</div></div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{snippet(fix_box)}
<div class="bubrow"><span class="bubble">工事費の370万円は建物の価額ではない。<br>増築部分は認定基準表で 45.00㎡×６万円＝270万円。<br>
1,200万＋530万＋270万＝2,000万円 × 10分の６ ＝ 1,200万円 × 1000分の４</span></div></div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{snippet(TAX_OK, good=True)}</div>
<div class="caption" style="margin:10px 0 30px">平成22年度 第22問｜課税価格は「工事費」ではなく「価額」から。健一郎さんの持分10分の６を掛ける</div>''')


# ---- 2026-10-05追加：申請書・問1の欄の誤答ごとの添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----
def red(t):
    return f'<span class="red">{t}</span>'


def cut(t):
    return f'<span class="ink strike">{t}</span>'


def ins(t):
    return f'<span class="caret">∨</span>{red(t)}'


def panel3(ng, fix, ok, bubble, caption, ng_note=''):
    note = f'<div class="note">{ng_note}</div>' if ng_note else ''
    return page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng}{note}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix}
<div class="bubrow"><span class="bubble">{bubble}</span></div></div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>
<div class="okwrap"><div class="good" style="padding:4px 10px 12px">{ok}</div>{CHECK_SVG}</div></div>
<div class="caption" style="margin:10px 0 30px">{caption}</div>''')


# (a) 問1(2)の代位原因（問1の欄をまとめて見せる）
def toi1_rows(daii):
    return (f'<div class="sub">(1)</div>'
            f'<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:70px">{ink(TOI1_PURPOSE)}</div></div>'
            f'<div class="row"><div class="lab">添　付　情　報</div><div class="box" style="height:70px">{ink(TOI1_ATTACH)}</div></div>'
            f'<div class="sub">(2)</div>'
            f'<div class="row"><div class="lab">代　位　原　因</div><div class="box" style="height:84px">{daii}</div></div>')


toi1_machigai = panel3(
    toi1_rows(ink('民法第423条')),
    toi1_rows(cut('民法第423条') + ins('不動産登記法第52条第4項')),
    toi1_rows(ink(TOI1_DAII)),
    '健一郎さんは太郎さんの債権者ではない（債権者代位ではない）。<br>'
    '区分建物になった2個の建物の表題部の変更は一括して申請する（第52条第3項）ので、<br>'
    '相手が申請しないときは不動産登記法が認めた代位（第52条第4項）で申請する',
    '平成22年度 第22問 問1(2)｜代位原因は「民法第423条」ではなく「不動産登記法第52条第4項」')


# (b) 登記の目的と申請人
NG_PURPOSE = '合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消'


def mokuteki_rows(purpose, applicant):
    return (f'<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:100px">{purpose}</div></div>'
            f'<div class="dateline">平成22年８月22日　　申請　　Ａ地方法務局</div>'
            f'<div class="row" style="margin-bottom:0"><div class="lab">申　　請　　人</div>'
            f'<div class="box" style="height:110px">{applicant}</div></div>')


NG_APPLICANT = br(ink('Ａ市Ｄ町一丁目２番１号　持分　10分の４　大面太郎（あ）'),
                  ink('Ａ市Ｄ町一丁目２番２号　　　　　10分の６　大面健一郎（い）'))
FIX_APPLICANT = br(ink('Ａ市Ｄ町一丁目２番１号　持分　10分の４　大面太郎') + cut('（あ）'),
                   ink('Ａ市Ｄ町一丁目２番２号　　　　　10分の６　大面健一郎') + cut('（い）'))
machigai_mokuteki = panel3(
    mokuteki_rows(ink(NG_PURPOSE), NG_APPLICANT),
    mokuteki_rows(ink(NG_PURPOSE) + ins('並びに所有権の保存の登記'), FIX_APPLICANT),
    mokuteki_rows(ink(PURPOSE), APPLICANT),
    '22番は表題登記だけ。健一郎さんを登記名義人とする所有権の登記を併せて申請する<br>'
    '（不動産登記法第49条第1項第4号・後段）。<br>'
    '太郎さんと健一郎さんは別人なので、同一の者でないとみなす持分の（あ）（い）は付けない',
    '平成22年度 第22問 問2(1)｜登記の目的に「並びに所有権の保存の登記」。持分は合意どおり、（あ）（い）なし')


# (c) 建物の表示（合体前の2行の構造）
def kouzou_table(s1, s2):
    r1 = entry_row(ink('21番地'), ink('21番'), ink('居宅'), s1, [('1階', '81', '00'), ('2階', '51', '84')],
                   ink('平成22年７月30日22番と<br>合体'))
    r2 = entry_row(ink('22番地'), ink('22番'), ink('居宅'), s2, [('', '68', '04')], ink('平成22年７月30日21番と<br>合体'))
    return (f'<table class="t" style="margin-top:0">{COLS}'
            f'<tr><td class="vert" rowspan="4">建物の表示</td><td class="lab2 val">所　在</td>'
            f'<td class="val" colspan="6">{ink("Ａ市Ｄ町一丁目")}</td></tr><tr>{HEAD}</tr>{r1}{r2}</table>')


machigai_kouzou = panel3(
    kouzou_table(ink('木造スレート<br>ぶき２階建'), ink('木造スレート<br>ぶき平家建')),
    kouzou_table(cut('木造スレート<br>ぶき２階建') + '<br>' + red('木造瓦葺<br>２階建'),
                 cut('木造スレート<br>ぶき平家建') + '<br>' + red('木造セメント<br>瓦葺平家建')),
    kouzou_table(ink('木造瓦葺<br>２階建'), ink('木造セメント<br>瓦葺平家建')),
    '合体前の行は、抹消される建物の登記記録の表示。工事後の屋根（スレート）は合体後の行だけ。<br>'
    '登記記録の「瓦葺」は、ひらがなに直さずにそのまま写す',
    '平成22年度 第22問 問2(1)｜合体前の2行の構造は登記記録どおり（木造瓦葺２階建・木造セメント瓦葺平家建）',
    '（屋根をスレートにふき替えた工事後の構造を、合体前の行にも書いてしまった）')


# (d) 存続登記の表（3行の表に3件とも書いた）
ROW_A = ('21番', '乙区１番', '抵当権設定', br('昭和51年２月17日', '第1112号'), 'Ａ銀行', br('大面太郎', '持分'))
ROW_B = ('21番', '乙区２番', '抵当権設定', br('昭和51年２月17日', '第1113号'), 'Ｂ信用金庫', br('大面太郎', '持分'))
ROW_C = ('21番', '乙区３番', '賃借権設定', br('平成７年６月14日', '第5567号'), '永野達也', br('大面太郎', '持分'))


def s2_row(cells, mode='ink'):
    if mode == 'cut':
        return '<tr class="cut">' + ''.join(f'<td class="entry">{cut(c)}</td>' for c in cells) + '</tr>'
    return '<tr>' + ''.join(f'<td class="entry">{ink(c)}</td>' for c in cells) + '</tr>'


def sonzoku_table(rows):
    return (f'<div class="sec" style="margin-top:0">二　抵当権等の登記で合体後の登記建物につき存続すべきものの表示</div>'
            f'<table class="t s">{S2_COLS}{S2_HEAD}{"".join(rows)}</table>')


machigai_sonzoku = panel3(
    sonzoku_table([s2_row(ROW_A), s2_row(ROW_B), s2_row(ROW_C)]),
    sonzoku_table([s2_row(ROW_A, 'cut'), s2_row(ROW_B), s2_row(ROW_C, 'cut')]),
    sonzoku_table([S2_ROW, S2_EMPTY, S2_EMPTY]),
    'A銀行の抵当権は消滅の承諾がある → 登記官が消滅した旨を登記する（不動産登記法第50条）。<br>'
    '賃借権は存続登記（不動産登記令別表13の項申請情報欄ハ）に当たらない。<br>'
    '書くのはB信用金庫の抵当権の1行だけ（大面太郎の持分の上に移される）',
    '平成22年度 第22問 問2(1)｜存続登記の表は3行あっても、書くのはB信用金庫の抵当権の1行だけ')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 100})   # 高さは内容に合わせる（full_page）
        for name, html in [('H22_dai22mon_toi1_kansei', toi1), ('H22_dai22mon_toi1_machigai', toi1_machigai),
                           ('H22_dai22mon_toukishinseisho_kansei', kansei),
                           ('H22_dai22mon_toukishinseisho_machigai', machigai),
                           ('H22_dai22mon_toukishinseisho_machigai_mokuteki', machigai_mokuteki),
                           ('H22_dai22mon_toukishinseisho_machigai_kouzou', machigai_kouzou),
                           ('H22_dai22mon_toukishinseisho_machigai_sonzoku', machigai_sonzoku)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            kind = '縦長' if h > w else ('横長（問1の完成形は小さい欄なので横長でよい）' if name.endswith('toi1_kansei') else '横長（要確認）')
            print(f'{png}  {w}×{h}px  ' + kind)
        browser.close()
