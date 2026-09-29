"""平成30年度 第22問（建物）登記申請書の画像（完成形、第1欄（その2）・第2欄の完成形、添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H30_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  答案用紙はA3横で、左の列に第1欄（その1）の登記申請書、右の列に「1　合体前の建物の所有権登記の表示」
  「2　抵当権等の登記で合体後の建物につき存続すべきものの表示」がある。左の列の下に右の列を縦に積む。
  欄の形は試験の答案用紙に合わせる：登記の目的・添付書類・申請人は記入枠、代理人の「（略）」と
  申請の日付・提出先（平成30年10月19日　申請　Ｄ地方法務局Ｅ出張所）は印刷済みで、この順（代理人が上）。
  建物の表示は、所在1段、見出し（地番・家屋番号・①種類・②構造・③床面積 m²・登記原因及びその日付）、記入行4行。登録免許税の欄はない
- 第1欄（その2）・第2欄：申請書以外の解答欄は別の画像にし、記事の該当の問の直後に置く（R3/Q22・R4/Q22と同じ扱い）
- 添削：`../prompt_H30_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `R4/Q22/zu/make_R4_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/H30/Q22/zu/make_H30_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 1.2em; padding: 0; font-size: 21px; }}
table.t td.lab2 {{ text-align: center; font-size: 18px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 62px; }}
table.t td.val {{ height: 56px; }}
table.t td.entry {{ height: 118px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
.sec {{ font-size: 24px; margin: 38px 0 4px; }}
.sec.first {{ margin-top: 0; }}
table.s td {{ height: 64px; text-align: center; font-size: 18px; }}
table.s td.head {{ height: 62px; font-size: 17px; }}
table.r2 td {{ height: 72px; font-size: 22px; }}
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


# ---- 建物の表示（答案用紙の形：所在1段、見出し6列、記入行4行） ----
COLS = ('<colgroup><col style="width:5%"><col style="width:11%"><col style="width:10%"><col style="width:9%">'
        '<col style="width:17%"><col style="width:12%"><col style="width:6%"><col style="width:30%"></colgroup>')
HEAD = ('<td class="head">地　番</td><td class="head">家屋番号</td><td class="head">①種類</td><td class="head">②構造</td>'
        '<td class="head" colspan="2">③床面積　m²</td><td class="head">登記原因及びその日付</td>')


def entry_row(chiban, kaoku, kind, struct, floors, genin):
    return (f'<tr><td class="entry center">{chiban}</td><td class="entry center">{kaoku}</td>'
            f'<td class="entry center">{kind}</td><td class="entry center">{struct}</td>{area(floors)}'
            f'<td class="entry genin">{genin}</td></tr>')


EMPTY_ROW = ('<tr><td class="entry"></td><td class="entry"></td><td class="entry"></td><td class="entry"></td>'
             '<td class="entry int"></td><td class="entry dec"></td><td class="entry"></td></tr>')

S_SLATE = '木造スレート<br>ぶき平家建'
S_KAWARA = '木造かわらぶ<br>き２階建'
ROW1 = entry_row(ink('301番地'), ink('301番'), ink('居宅'), ink(S_SLATE), [('', '57', '63')],
                 ink('平成30年10月１日302番と<br>合体'))
ROW2 = entry_row(ink('302番地'), ink('302番'), ink('居宅'), ink(S_KAWARA), [('1階', '78', '49'), ('2階', '78', '49')],
                 ink('平成30年10月１日301番と<br>合体'))
ROW3 = entry_row(ink(br('302番地', '301番地')), '', ink('居宅'), ink(S_KAWARA),
                 [('1階', '190', '53'), ('2階', '78', '49')], ink('平成30年10月１日301番、<br>302番を合体'))

TABLE = (f'<table class="t">{COLS}'
         f'<tr><td class="vert" rowspan="6">建物の表示</td><td class="lab2 val">所　在</td>'
         f'<td class="val" colspan="6">{ink("Ａ市Ｂ町一丁目")}</td></tr>'
         f'<tr>{HEAD}</tr>{ROW1}{ROW2}{ROW3}{EMPTY_ROW}</table>')

APPLICANT = br(ink('Ａ市Ｂ町一丁目１番１号　持分　10分の２　甲山太郎（あ）'),
               ink('Ａ市Ｂ町一丁目１番１号　　　　　10分の８　甲山太郎（い）'))

# ---- 右の列：所有権登記の表示・存続登記 ----
S1_COLS = '<colgroup><col style="width:14%"><col style="width:13%"><col style="width:43%"><col style="width:30%"></colgroup>'
S1_HEAD = ('<tr><td class="head">家屋番号</td><td class="head">順位番号</td><td class="head">受付年月日及び受付番号</td>'
           '<td class="head">登記名義人の氏名</td></tr>')
S1 = (f'<div class="sec">1　合体前の建物の所有権登記の表示</div><table class="t s">{S1_COLS}{S1_HEAD}'
      f'<tr><td>{ink("301番")}</td><td>{ink("２番")}</td><td>{ink("平成29年１月20日第567号")}</td><td>{ink("甲山太郎（あ）")}</td></tr>'
      f'<tr><td>{ink("302番")}</td><td>{ink("１番")}</td><td>{ink("昭和60年３月12日第1234号")}</td><td>{ink("甲山太郎（い）")}</td></tr>'
      '</table>')
S2_COLS = ('<colgroup><col style="width:12%"><col style="width:12%"><col style="width:15%"><col style="width:23%">'
           '<col style="width:18%"><col style="width:20%"></colgroup>')
S2_HEAD = ('<tr><td class="head">家屋番号</td><td class="head">順位番号</td><td class="head">登記の<br>目的</td>'
           '<td class="head">受付年月日<br>及び受付番号</td><td class="head">登記名義人<br>の氏名</td>'
           '<td class="head">目的となる権利</td></tr>')


def s2_row(right):
    return (f'<tr><td class="entry">{ink("301番")}</td><td class="entry">{ink("乙区１番")}</td>'
            f'<td class="entry">{ink("抵当権設定")}</td><td class="entry">{ink(br("平成29年１月20日", "第568号"))}</td>'
            f'<td class="entry">{ink(br("株式会社", "Ｃ銀行"))}</td><td class="entry">{right}</td></tr>')


S2_EMPTY = '<tr>' + '<td class="entry"></td>' * 6 + '</tr>'
S2 = (f'<div class="sec">2　抵当権等の登記で合体後の建物につき存続すべきものの表示</div><table class="t s">{S2_COLS}{S2_HEAD}'
      f'{s2_row(ink(br("甲山太郎（あ）", "持分")))}{S2_EMPTY}</table>')

kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:100px">{ink('合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:120px">{ink(br('建物図面　各階平面図　所有権証明書　住所証明書', '登記識別情報　印鑑証明書　承諾書　代理権限証書'))}</div></div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:120px">{APPLICANT}</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="dateline">平成30年10月19日　申請　　Ｄ地方法務局Ｅ出張所</div>
{TABLE}
{S1}
{S2}
<div class="caption">平成30年度 土地家屋調査士試験 第22問 登記申請書 解答例（答案用紙の左の列の下に右の列を積んだもの）</div>
</div>''')


# ---- 第1欄（その2）・第2欄 ----
def ran(sec, rows, caption, widths=(30, 70)):
    cols = f'<colgroup><col style="width:{widths[0]}%"><col style="width:{widths[1]}%"></colgroup>'
    body = ''.join(f'<tr><td class="center">{a}</td><td class="center">{ink(b)}</td></tr>' for a, b in rows)
    return page(f'<div class="page"><div class="sec first">{sec}</div><table class="t r2">{cols}{body}</table>'
                f'<div class="caption">{caption}</div></div>')


sono2 = ran('第1欄（その2）', [('ア', '主従'), ('イ', '増築工事'), ('ウ', '隔壁を除去'), ('エ', '構造上1個')],
            '平成30年度 土地家屋調査士試験 第22問 問1（第1欄（その2））解答例')
dai2 = ran('第2欄', [('登記の目的', '建物表題部変更登記'),
                    ('主である建物についての<br>登記原因及びその日付', '③平成30年10月１日増築、符号１の附属建物合体')],
           '平成30年度 土地家屋調査士試験 第22問 問2（第2欄）解答例', widths=(34, 66))


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：申請人欄と存続登記の1行目 ----
def snippet(applicant, right, good=False):
    g = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><div class="row{g}" style="padding:4px"><div class="lab">申　　請　　人</div>'
            f'<div class="box" style="height:110px">{applicant}</div></div>'
            f'<div class="sec" style="margin-top:6px">2　抵当権等の登記で合体後の建物につき存続すべきものの表示</div>'
            f'<table class="t s{g}">{S2_COLS}{S2_HEAD}{s2_row(right)}</table>{chk}</div>')


NG_APP = ink('Ａ市Ｂ町一丁目１番１号　甲山太郎')
NG_RIGHT = ink('甲山太郎の持分')
FIX_APP = (ink('Ａ市Ｂ町一丁目１番１号') + '<span class="caret">∨</span><span class="red">持分　10分の２</span>'
           + ink('　甲山太郎') + '<span class="caret">∨</span><span class="red">（あ）</span><br>'
           + '<span class="red">Ａ市Ｂ町一丁目１番１号　10分の８　甲山太郎（い）</span>')
FIX_RIGHT = ink('甲山太郎') + '<span class="caret">∨</span><span class="red">（あ）</span><br>' + \
    '<span class="ink strike">の</span>' + ink('持分')
ng_panel = snippet(NG_APP, NG_RIGHT)
fix_panel = snippet(FIX_APP, FIX_RIGHT) + \
    ('<div class="bubrow"><span class="bubble">抵当権は301番の名義人（あ）の持分10分の２の上に存続する。<br>'
     '同じ甲山さんでも、同一の者でないとみなして持分を書く（令別表13の項ニ）！</span></div>')
ok_panel = snippet(APPLICANT, ink(br('甲山太郎（あ）', '持分')), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成30年度 第22問｜同じ甲山さんでも、（あ）と（い）の別人とみなして持分を書く</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 100})   # 高さは内容に合わせる（full_page）
        for name, html in [('H30_dai22mon_toukishinseisho_kansei', kansei),
                           ('H30_dai22mon_toukishinseisho_machigai', machigai),
                           ('H30_dai22mon_dai1ran_sono2_kansei', sono2), ('H30_dai22mon_dai2ran_kansei', dai2)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            kind = '縦長' if h > w else ('横長（第1欄（その2）・第2欄は小さい表なので横長でよい）' if 'ran' in name else '横長（要確認）')
            print(f'{png}  {w}×{h}px  ' + kind)
        browser.close()
