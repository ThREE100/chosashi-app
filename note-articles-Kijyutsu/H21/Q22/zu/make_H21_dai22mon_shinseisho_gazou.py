"""平成21年度 第22問（建物）登記申請書の画像（問1の完成形、問2の解答欄の完成形、添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H21_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  欄の形は試験の答案用紙（その1）の問1に合わせる（登記の目的・添付書類の枠、枠なしの「平成21年8月23日　申請　D地方法務局B出張所」、
  申請人の枠、代理人の枠と印、（連絡先電話番号　略）、表の左に縦書きの「建物の表示」の列、不動産番号、所在は2段、
  家屋番号は「（記載不要）」が印刷済みで右に空いた枠、見出し行、記入行3行と横いっぱいの1行、表の下の職印の枠。登録免許税の欄はない）
- 問2　：「所有権を有することを証する情報として添付する具体的書面（情報）の例」の見出しと記入行3行
- 添削　：`../prompt_H21_dai22mon_toukishinseisho_machigai.md` どおり。欄ごとに1枚（構造・床面積）。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 寸法：試験の答案用紙（`public/kijutsu/H21-tatemono/a1.webp`、990×1400px）の罫線から測った比。答案用紙の100px＝この画像の約145px（1.45倍）

CSSと部品の作りは `H23/Q22/zu/make_H23_dai22mon_shinseisho_gazou.py` と同じ形にしている。
実行: python3 note-articles-Kijyutsu/H21/Q22/zu/make_H21_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.page {{ padding: 40px 57px 40px 72px; min-height: 1390px; display: flex; flex-direction: column; position: relative; }}
.qlab {{ font-size: 21px; margin: 0 0 14px -12px; }}
.page .caption {{ margin-top: auto; padding-top: 30px; }}
.title {{ text-align: center; font-size: 34px; letter-spacing: 0.9em; margin: 0 0 30px 0.9em; width: 940px; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 22px; }}
.lab {{ width: 182px; font-size: 22px; padding-top: 8px; white-space: nowrap; }}
.box {{ width: 686px; border: 2px solid #111; padding: 8px 16px; font-size: 24px; line-height: 1.5; }}
.stamp {{ width: 38px; height: 38px; border: 2px solid #111; border-radius: 50%; margin: 8px 0 0 18px; font-size: 18px;
          display: flex; align-items: center; justify-content: center; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.dateline {{ font-size: 22px; margin: 0 0 26px; }}
.tel {{ font-size: 19px; margin: -10px 0 24px 258px; }}
table.bldg {{ width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; }}
.tbl {{ position: relative; width: 940px; }}
.stars {{ position: absolute; left: 959px; border: 2px solid #111; width: 112px; font-size: 14px; padding: 2px 6px; }}
table.bldg td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 10px; vertical-align: middle; line-height: 1.5; }}
table.bldg td.lab2 {{ text-align: center; font-size: 19px; }}
table.bldg td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 1.6em; font-size: 21px; padding: 10px 0; }}
table.bldg td.head {{ text-align: center; font-size: 15px; height: 44px; padding: 4px 6px; }}
table.bldg td.val {{ height: 36px; padding-top: 2px; padding-bottom: 2px; }}
table.bldg td.val0 {{ height: 28px; padding: 0 10px; font-size: 16px; text-align: center; }}
table.bldg td.entry {{ height: 90px; }}
table.bldg td.wide {{ height: 90px; }}
table.bldg td.center {{ text-align: center; }}
table.bldg td.struct {{ font-size: 17px; }}
table.bldg td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.bldg td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.bldg td.genin {{ font-size: 17px; }}
table.bldg td .ink {{ font-size: 20px; }}
table.bldg td.struct .ink, table.bldg td.genin .ink {{ font-size: 19px; }}
.shokuin {{ display: flex; align-items: center; margin: 24px 0 0 454px; }}
.shokuin .sbox {{ width: 402px; border: 2px solid #111; padding: 8px 14px; font-size: 21px; }}
.shokuin .sin {{ border: 2px solid #111; padding: 2px 6px; margin-left: 14px; font-size: 15px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 30px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 問2 */
table.toi2 {{ width: 940px; border-collapse: collapse; border: 2.5px solid #111; }}
table.toi2 td {{ border: 1.5px solid #111; font-size: 21px; padding: 14px 16px; height: 84px; }}
table.toi2 td.h {{ height: 40px; padding: 6px 12px; font-size: 19px; }}
/* 添削画像 */
.panel {{ padding: 56px 60px 66px; border-bottom: 2px solid #bbb; }}
.panel:last-of-type {{ border-bottom: none; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.strike {{ position: relative; white-space: nowrap; }}
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

# 列（答案用紙の罫線から測った比。全幅648px）：建物の表示（縦書き）40・主たる建物又は附属建物86・①種類77・②構造106＋10（家屋番号の仕切り）・
# ③床面積 整数部128＋小数部46・登記原因及びその日付155
COLS = ('<colgroup><col style="width:6.2%"><col style="width:13.3%"><col style="width:11.9%"><col style="width:16.4%">'
        '<col style="width:1.5%"><col style="width:19.8%"><col style="width:7.1%"><col style="width:23.9%"></colgroup>')
HEAD = ('<td class="head lab2">主たる建物<br>又は附属建物</td><td class="head">①種類</td>'
        '<td class="head" colspan="2">②構　造</td><td class="head" colspan="2">③床面積 m²</td>'
        '<td class="head">登記原因及びその日付</td>')
COLS_SNIP = ('<colgroup><col style="width:13%"><col style="width:9%"><col style="width:30%">'
             '<col style="width:12%"><col style="width:7%"><col style="width:29%"></colgroup>')


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


def entry_cells(label, kind, struct, floors, genin):
    return (f'<td class="entry lab2">{label}</td><td class="entry center">{kind}</td>'
            f'<td class="entry struct" colspan="2">{struct}</td>{area(*floors)}<td class="entry genin">{genin}</td>')


SHOZAI = 'Ａ市Ｂ町二丁目３番地４'
KOUZOU = '木造かわらぶき３階建'
FLOORS = [('1階', '41', '40'), ('2階', '33', '12'), ('3階', '8', '28')]
GENIN = '平成21年8月8日新築'

VERT = '<td class="vert" rowspan="8">建物の表示</td>'
table = (f'<div class="tbl"><table class="bldg">{COLS}'
         f'<tr><td class="lab2 val0" colspan="2">不動産番号</td><td class="val0" colspan="6"></td></tr>'
         f'<tr>{VERT}<td class="lab2" rowspan="2">所　在</td><td class="val" colspan="6">{ink(SHOZAI)}</td></tr>'
         f'<tr><td class="val" colspan="6"></td></tr>'
         f'<tr><td class="lab2 val">家屋番号</td><td class="val center" colspan="2">（記載不要）</td><td class="val" colspan="4"></td></tr>'
         f'<tr>{HEAD}</tr>'
         f'<tr>{entry_cells("", ink("居宅"), ink(KOUZOU), FLOORS, ink(GENIN))}</tr>'
         f'<tr>{entry_cells("", "", "", [("", "", "")], "")}</tr>'
         f'<tr>{entry_cells("", "", "", [("", "", "")], "")}</tr>'
         f'<tr><td class="wide" colspan="7"></td></tr></table>'
         f'<div class="stars" style="top:406px;min-height:128px">※</div></div>')
kansei = page(f'''<div class="page">
<div class="qlab">問1（登記申請書）</div>
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="min-height:51px">{ink('建物表題登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="min-height:106px;font-size:22px">{ink('建物図面　各階平面図　所有権証明書　住所証明書　代理権限証書')}</div></div>
<div class="dateline" style="margin-top:8px">平成21年8月23日　　申請　　Ｄ地方法務局Ｂ出張所</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="min-height:52px">{ink('Ａ市Ｂ町二丁目３番地４　土野一郎')}</div></div>
<div class="row"><div class="lab">代　　理　　人</div><div class="box" style="min-height:52px">{ink('Ａ市Ｃ町五丁目６番地７　家野二郎')}</div><div class="stamp">印</div></div>
<div class="tel">（連絡先電話番号　　略　　）</div>
{table}
<div class="shokuin"><div class="sbox">{ink('土地家屋調査士　家野二郎')}</div><div class="sin">職印</div></div>
<div class="caption">平成21年度 土地家屋調査士試験 第22問 問1 登記申請書 解答例</div>
</div>''')

# ---- 問2 ----
TOI2 = ['建築基準法第6条の確認があったことを証する書面（確認済証）',
        '建築基準法第7条の検査があったことを証する書面（検査済証）',
        '株式会社建倉工務店が作成した工事完了引渡証明書（同社の印鑑証明書付き）']
rows2 = ''.join(f'<tr><td>{ink(s)}</td></tr>' for s in TOI2)
toi2 = page(f'''<div style="padding:40px 57px 30px 72px">
<div class="qlab">問2</div>
<div class="tbl"><table class="toi2"><tr><td class="h">所有権を有することを証する情報として添付する具体的書面（情報）の例</td></tr>{rows2}</table>
<div class="stars" style="top:164px;min-height:126px">※</div></div>
<div class="caption" style="margin-top:130px">平成21年度 土地家屋調査士試験 第22問 問2 解答例</div></div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：欄ごとに1枚。建物の表示の記入行1だけを取り出す ----
HEAD_SNIP = ('<td class="head lab2">主たる建物<br>又は附属建物</td><td class="head">①種類</td>'
             '<td class="head">②構　造</td><td class="head" colspan="2">③床面積 m²</td>'
             '<td class="head">登記原因及びその日付</td>')


def snippet(cells, good=False):
    g = ' class="good"' if good else ''
    chk = CHECK_SVG if good else ''
    return f'<div class="okwrap"><table class="bldg"{g}>{COLS_SNIP}<tr>{HEAD_SNIP}</tr><tr>{cells}</tr></table>{chk}</div>'


def snip_cells(struct, int_html, dec_html, genin=None):
    return ('<td class="entry lab2"></td>'
            f'<td class="entry center">{ink("居宅")}</td>'
            f'<td class="entry struct">{struct}</td>'
            f'<td class="entry int">{int_html}</td><td class="entry dec">{dec_html}</td>'
            f'<td class="entry genin">{ink(genin or GENIN)}</td>')


def strike(t):
    return f'<span class="ink strike">{t}</span>'


def red(t):
    return f'<span class="red">{t}</span>'


def three(cap, ng, fix, ok, bubble):
    return page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{snippet(ng)}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{snippet(fix)}<div class="bubrow"><span class="bubble">{bubble}</span></div></div>
<div class="panel"><div class="ptitle ok">③正解</div>{snippet(ok, good=True)}</div>
<div class="caption" style="margin:10px 0 30px">{cap}</div>''')


ints = br(*[ink(f'{k}　{a}') for k, a, _ in FLOORS])
decs = br(*[ink(b) for _, _, b in FLOORS])
OK_CELLS = snip_cells(ink(KOUZOU), ints, decs)

# 構造の欄：屋根が2種類あっても30％未満の種類は書かない
ng1 = snip_cells(ink('木造かわら・合金メッキ鋼板ぶき３階建'), ints, decs)
fix1 = snip_cells(f'{ink("木造かわら")}{strike("・合金メッキ鋼板")}<br>{ink("ぶき３階建")}', ints, decs)
machigai_kouzou = three('平成21年度 第22問｜構造の欄：30％未満の小屋根は書かない', ng1, fix1, OK_CELLS,
                        '玄関の小屋根は0.91×1.82＝1.6562で、1階41.405の約4％。<br>'
                        '床面積に算入する部分の屋根面積の30％未満の種類の屋根は表示しない！')

# 床面積の欄：切り捨て（41.40）、ロフトの押入も算入（8.28）
ng_int = br(ink('1階　41'), ink('2階　33'), ink('3階　6'))
ng_dec = br(ink('41'), ink('12'), ink('62'))
fix_int = br(ink('1階　41'), ink('2階　33'), f'{ink("3階　")}{strike("6")}{red("8")}')
fix_dec = br(f'{strike("41")} {red("40")}', ink('12'), f'{strike("62")} {red("28")}')
ng2 = snip_cells(ink(KOUZOU), ng_int, ng_dec)
fix2 = snip_cells(ink(KOUZOU), fix_int, fix_dec)
machigai_yukamenseki = three('平成21年度 第22問｜床面積の欄：切り捨てと、ロフトの押入も算入', ng2, fix2, OK_CELLS,
                             '41.405は切り捨てて41.40（四捨五入の41.41ではない）<br>'
                             'ロフトは押入も含めて4.55×1.82＝8.2810 → 8.28（押入を除く6.62ではない）')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 800})
        for name, html in [('H21_dai22mon_toukishinseisho_kansei', kansei),
                           ('H21_dai22mon_toukishinseisho_kansei_toi2', toi2),
                           ('H21_dai22mon_toukishinseisho_machigai_kouzou', machigai_kouzou),
                           ('H21_dai22mon_toukishinseisho_machigai_yukamenseki', machigai_yukamenseki)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_viewport_size({'width': 1200, 'height': 200})   # 内容の高さで書き出す（下に余白を残さない）
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
        browser.close()
