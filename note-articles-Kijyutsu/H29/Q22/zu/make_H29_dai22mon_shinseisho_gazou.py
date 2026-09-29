"""平成29年度 第22問（建物）の答案用紙の画像（第1欄の完成形、登記申請書の完成形、添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 第1欄　：`../prompt_H29_dai22mon_toukishinseisho_gazou.md` の記入データ1どおり。①登記の目的・②理由（印刷された書き出し
  「主である建物のみについて所有権の移転の登記を行うためには，」の続き）・③各階平面図の添付の要否の3つの枠。
  答案用紙はA3横で、第1欄は左の列の上にある。申請書ではない解答欄なので別の画像にする（R3/Q22・R4/Q22と同じ扱い）
- 完成形：同じく記入データ2どおり。答案用紙の第2欄は、左の列の下（登記の目的・添付書類・申請の日付と提出先）から右の列
  （申請人・代理人・建物の表示）へ続くので、左 → 右の順に縦に積んで横1200pxの縦長にする。
  欄の形は試験の答案用紙どおり：申請の日付・提出先（平成29年8月18日　申請　Ａ地方法務局）と代理人の「（略）」、
  表の下の「土地家屋調査士　法　務　守」は印刷済み、申請人は記入枠。建物の表示は、不動産番号、所在2段（上段1枠・下段2枠）、
  家屋番号（2枠）、見出し（主である建物又は附属建物・①種類・②構造・③床面積・登記原因及びその日付）、記入行4行、最下段の空欄。
  登録免許税の欄はない
- 添削　：`../prompt_H29_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `R4/Q22/zu/make_R4_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/H29/Q22/zu/make_H29_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.sign {{ text-align: right; font-size: 22px; margin-top: 10px; letter-spacing: 0.1em; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 18px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 1.2em; padding: 0; font-size: 21px; }}
table.t td.lab2 {{ text-align: center; font-size: 18px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 76px; }}
table.t td.val {{ height: 56px; }}
table.t td.entry {{ height: 118px; }}
table.t td.blank {{ height: 84px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 34px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 第1欄 */
table.r1 {{ width: 100%; border-collapse: collapse; border: 3px solid #111; }}
table.r1 td {{ border: 1.5px solid #111; font-size: 21px; padding: 10px 14px; line-height: 1.8; vertical-align: top; }}
table.r1 td.h {{ height: 50px; vertical-align: middle; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.red {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; }}
.strike {{ text-decoration: line-through; text-decoration-color: {RED}; text-decoration-thickness: 3px; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 21px; font-weight: bold; background: #fff5f5; line-height: 1.5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubrow {{ margin: 16px 0 0; }}
.wave {{ border: 2.5px dashed {RED}; border-radius: 16px; padding: 12px 14px; margin-top: 14px; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 3px; background: #f1faf2; }}
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
    """床面積の整数部・小数部のセル。floors: [(整数部, 小数部)]"""
    ints = br(*[ink(a) for a, _ in floors])
    decs = br(*[ink(b) for _, b in floors])
    return f'<td class="{cls} int">{ints}</td><td class="{cls} dec">{decs}</td>'


# ---- 第1欄（問1） ----
REASON_HEAD = '主である建物のみについて所有権の移転の登記を行うためには，'
REASON = ('甲建物と乙建物が登記記録上一個の建物として登記されており、その一部である甲建物のみについて所有権の移転の登記をすることは'
          'できないため、乙建物を甲建物の登記記録から分割して、登記記録上別の一個の建物とする必要がある。')
dai1 = page(f'''<div class="page">
<div style="font-size:22px;margin-bottom:14px">第１欄　【事実関係】５の依頼を受けて行うべき本件建物について必要となる表示に関する登記の申請について</div>
<table class="r1">
<tr><td class="h">①登記の目的</td></tr>
<tr><td style="height:96px">{ink('建物分割登記')}</td></tr>
<tr><td class="h">②当該登記の申請をする必要がある理由</td></tr>
<tr><td style="height:300px">{REASON_HEAD}{ink(REASON)}</td></tr>
<tr><td class="h">③当該登記の申請に各階平面図を添付しなければならないかどうか</td></tr>
<tr><td style="height:96px">{ink('添付しなければならない。')}</td></tr>
</table>
<div class="caption">平成29年度 土地家屋調査士試験 第22問 第1欄 解答例</div>
</div>''')

# ---- 建物の表示（答案用紙の形：不動産番号、所在2段、家屋番号2枠、見出し、記入行4行、最下段の空欄） ----
COLS = ('<colgroup><col style="width:5%"><col style="width:13%"><col style="width:11%"><col style="width:22%">'
        '<col style="width:11%"><col style="width:6%"><col style="width:32%"></colgroup>')
HEAD = ('<td class="head">主である<br>建物又は<br>附属建物</td><td class="head">①種類</td><td class="head">②構　　造</td>'
        '<td class="head" colspan="2">③床面積　m²</td><td class="head">登記原因及びその日付</td>')


def entry_row(shu, kind, struct, floors, genin):
    return (f'<tr><td class="entry center">{shu}</td><td class="entry center">{kind}</td>'
            f'<td class="entry center">{struct}</td>{area(floors)}<td class="entry genin">{genin}</td></tr>')


EMPTY_ROW = ('<tr><td class="entry"></td><td class="entry"></td><td class="entry"></td>'
             '<td class="entry int"></td><td class="entry dec"></td><td class="entry"></td></tr>')

S_KOU = '軽量鉄骨造亜鉛メッ<br>キ鋼板ぶき平家建'
S_HEI = '発泡ポリスチレ<br>ン造平家建'
SHOZAI_OK = 'Ａ市Ｂ町三丁目１番地１'
SHOZAI_NG = 'Ａ市Ｂ町三丁目１番地１、１番地２'
ROW1 = entry_row(ink('主'), ink('集会所'), ink(S_KOU), [('185', '27')], '')
ROW2 = entry_row('', ink('保育所'), '', [('', '')], ink('①平成29年７月20日種類<br>変更'))
ROW3 = entry_row(ink('符号２'), ink('倉庫'), ink(S_HEI), [('60', '00')], ink('平成29年８月10日新築'))


def table(shozai_cell, row3=ROW3, extra_rows=True):
    rows = f'{ROW1}{ROW2}{row3}' + (f'{EMPTY_ROW}<tr><td class="blank" colspan="6"></td></tr>' if extra_rows else '')
    n = 8 if extra_rows else 6
    return (f'<table class="t">{COLS}'
            f'<tr><td class="lab2 val" colspan="2">不動産番号</td><td class="val" colspan="5"></td></tr>'
            f'<tr><td class="vert" rowspan="{n + 1}">建物の表示</td><td class="lab2" rowspan="2">所　　在</td>'
            f'<td class="val" colspan="5">{shozai_cell}</td></tr>'
            f'<tr><td class="val" colspan="2"></td><td class="val" colspan="3"></td></tr>'
            f'<tr><td class="lab2 val">家屋番号</td><td class="val" colspan="2">{ink("１番１")}</td><td class="val" colspan="3"></td></tr>'
            f'<tr>{HEAD}</tr>{rows}</table>')


kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物表題部変更登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:120px">{ink(br('建物図面　各階平面図　所有権証明書　登記事項証明書', '代理権限証書'))}</div></div>
<div class="dateline">平成29年８月18日　申請　　Ａ地方法務局</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:120px">{ink(br('Ａ市Ｃ町二丁目６番２号　社会福祉法人Ｃ福祉会', '　　　　　　　　　　　　理事長　人権岩男'))}</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{table(ink(SHOZAI_OK))}
<div class="sign">土地家屋調査士　法　務　守</div>
<div class="caption">平成29年度 土地家屋調査士試験 第22問 登記申請書 解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：所在・家屋番号と、記入行1〜3 ----
def snippet(shozai_cell, row3, good=False):
    g = ' class="t good"' if good else ' class="t"'
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><table{g}>{COLS}'
            f'<tr><td class="vert" rowspan="6" style="letter-spacing:0.2em">建物の表示</td>'
            f'<td class="lab2 val">所　　在</td><td class="val" colspan="5">{shozai_cell}</td></tr>'
            f'<tr><td class="lab2 val">家屋番号</td><td class="val" colspan="5">{ink("１番１")}</td></tr>'
            f'<tr>{HEAD}</tr>{ROW1}{ROW2}{row3}</table>{chk}</div>')


ROW3_NG = entry_row(ink('符号１'), ink('倉庫'), ink(S_HEI), [('60', '00')], ink('平成29年８月10日新築'))
ROW3_FIX = entry_row(ink('符号') + '<span class="ink strike">１</span><span class="red">２</span>', ink('倉庫'), ink(S_HEI),
                     [('60', '00')], ink('平成29年８月10日新築'))
SHOZAI_FIX = ink('Ａ市Ｂ町三丁目１番地１') + '<span class="ink strike">、１番地２</span>'
ng_panel = snippet(ink(SHOZAI_NG), ROW3_NG)
fix_panel = snippet(SHOZAI_FIX, ROW3_FIX) + \
    ('<div class="wave"><div class="bubrow"><span class="bubble">所在：調査日（4/28）は分割の登記（5/19）の前！　乙建物が抜けて甲建物は１番地１だけ。'
     '丙建物も１番１の土地の上</span></div>'
     '<div class="bubrow"><span class="bubble">符号：符号１は乙建物の記録として、抹消の記号付きで甲建物の登記記録に残っている → 次の番号</span></div>'
     '<div class="bubrow" style="text-align:center"><span class="red" style="font-size:24px">どちらも分割の後の登記記録で考える</span></div></div>')
ok_panel = snippet(f'<span class="good">{ink(SHOZAI_OK)}</span>',
                   entry_row(f'<span class="good">{ink("符号２")}</span>', ink('倉庫'), ink(S_HEI), [('60', '00')],
                             ink('平成29年８月10日新築')), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成29年度 第22問｜所在も符号も、分割の後の登記記録で</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 100})   # 高さは内容に合わせる（full_page）
        for name, html in [('H29_dai22mon_dai1ran_kansei', dai1), ('H29_dai22mon_toukishinseisho_kansei', kansei),
                           ('H29_dai22mon_toukishinseisho_machigai', machigai)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（第1欄は小さい表なので横長でもよい）'))
        browser.close()
