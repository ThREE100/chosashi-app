"""平成21年度 第22問（建物）登記申請書の画像（問1の完成形、問2の解答欄の完成形、添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H21_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  欄の形は試験の答案用紙（その1）の問1に合わせる（登記の目的・添付書類の枠、枠なしの「平成21年8月23日　申請　D地方法務局B出張所」、
  申請人の枠、代理人の枠と印、（連絡先電話番号　略）、表の左に縦書きの「建物の表示」の列、不動産番号、所在は2段、
  家屋番号は「（記載不要）」が印刷済みで右に空いた枠、見出し行、記入行3行と横いっぱいの1行、表の下の職印の枠。登録免許税の欄はない）
- 問2　：「所有権を有することを証する情報として添付する具体的書面（情報）の例」の見出しと記入行3行
- 添削　：`../prompt_H21_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

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
.page {{ padding: 70px 60px 40px; min-height: 1650px; display: flex; flex-direction: column; }}
.page .caption {{ margin-top: auto; padding-top: 30px; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 48px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 26px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.stamp {{ width: 46px; height: 46px; border: 2px solid #111; border-radius: 50%; margin: 8px 0 0 16px; font-size: 20px;
          display: flex; align-items: center; justify-content: center; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.dateline {{ font-size: 22px; margin: 0 0 26px; }}
.tel {{ font-size: 20px; margin: -14px 0 30px 300px; }}
table.bldg {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.bldg td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 10px; vertical-align: middle; line-height: 1.5; }}
table.bldg td.lab2 {{ text-align: center; font-size: 19px; }}
table.bldg td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 1.6em; font-size: 21px; padding: 10px 0; }}
table.bldg td.head {{ text-align: center; font-size: 17px; height: 70px; }}
table.bldg td.val {{ height: 56px; }}
table.bldg td.entry {{ height: 150px; }}
table.bldg td.wide {{ height: 90px; }}
table.bldg td.center {{ text-align: center; }}
table.bldg td.struct {{ font-size: 17px; }}
table.bldg td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.bldg td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.bldg td.genin {{ font-size: 17px; }}
table.bldg td .ink {{ font-size: 20px; }}
table.bldg td.struct .ink, table.bldg td.genin .ink {{ font-size: 19px; }}
.shokuin {{ display: flex; justify-content: flex-end; align-items: center; margin-top: 24px; }}
.shokuin .sbox {{ width: 470px; border: 2px solid #111; padding: 12px 18px; font-size: 22px; }}
.shokuin .sin {{ border: 2px solid #111; padding: 2px 8px; margin-left: 12px; font-size: 20px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 30px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 問2 */
table.toi2 {{ width: 100%; border-collapse: collapse; border: 3px solid #111; }}
table.toi2 td {{ border: 1.5px solid #111; font-size: 21px; padding: 14px 16px; height: 74px; }}
table.toi2 td.h {{ height: 56px; font-size: 20px; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
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

# 列（答案用紙の比率）：建物の表示（縦書き）・主たる建物又は附属建物・①種類・②構造・③床面積（整数部・小数部）・登記原因及びその日付
COLS = ('<colgroup><col style="width:5%"><col style="width:13%"><col style="width:9%"><col style="width:22%">'
        '<col style="width:12%"><col style="width:7%"><col style="width:32%"></colgroup>')
HEAD = ('<td class="head lab2">主たる建物<br>又は附属建物</td><td class="head">①種類</td>'
        '<td class="head">②構　造</td><td class="head" colspan="2">③床面積 m²</td>'
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
            f'<td class="entry struct">{struct}</td>{area(*floors)}<td class="entry genin">{genin}</td>')


SHOZAI = 'Ａ市Ｂ町二丁目３番地４'
KOUZOU = '木造かわらぶき３階建'
FLOORS = [('1階', '41', '40'), ('2階', '33', '12'), ('3階', '8', '28')]
GENIN = '平成21年8月8日新築'

VERT = '<td class="vert" rowspan="8">建物の表示</td>'
table = (f'<table class="bldg">{COLS}'
         f'<tr><td class="lab2 val" colspan="2">不動産番号</td><td class="val" colspan="5"></td></tr>'
         f'<tr>{VERT}<td class="lab2" rowspan="2">所　在</td><td class="val" colspan="5">{ink(SHOZAI)}</td></tr>'
         f'<tr><td class="val" colspan="5"></td></tr>'
         f'<tr><td class="lab2 val">家屋番号</td><td class="val center" colspan="2">（記載不要）</td><td class="val" colspan="3"></td></tr>'
         f'<tr>{HEAD}</tr>'
         f'<tr>{entry_cells("", ink("居宅"), ink(KOUZOU), FLOORS, ink(GENIN))}</tr>'
         f'<tr>{entry_cells("", "", "", [("", "", "")], "")}</tr>'
         f'<tr>{entry_cells("", "", "", [("", "", "")], "")}</tr>'
         f'<tr><td class="wide" colspan="6"></td></tr></table>')
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物表題登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:100px">{ink('建物図面　各階平面図　所有権証明書　住所証明書　代理権限証書')}</div></div>
<div class="dateline">平成21年8月23日　　申請　　Ｄ地方法務局Ｂ出張所</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:62px">{ink('Ａ市Ｂ町二丁目３番地４　土野一郎')}</div></div>
<div class="row"><div class="lab">代　　理　　人</div><div class="box" style="height:62px">{ink('Ａ市Ｃ町五丁目６番地７　家野二郎')}</div><div class="stamp">印</div></div>
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
toi2 = page(f'''<div style="padding:50px 60px 30px">
<table class="toi2"><tr><td class="h">所有権を有することを証する情報として添付する具体的書面（情報）の例</td></tr>{rows2}</table>
<div class="caption">平成21年度 土地家屋調査士試験 第22問 問2 解答例</div></div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：建物の表示の記入行1 ----
def snippet(cells, good=False):
    g = ' class="good"' if good else ''
    chk = CHECK_SVG if good else ''
    head = HEAD
    return f'<div class="okwrap"><table class="bldg"{g}>{COLS_SNIP}<tr>{head}</tr><tr>{cells}</tr></table>{chk}</div>'


ng_panel = snippet(entry_cells('', ink('居宅'), ink('木造かわら・合金メッキ鋼板ぶき２階建'), [('1階', '41', '41'), ('2階', '33', '12')],
                               ink(GENIN)))
fix_cells = ('<td class="entry lab2"></td>'
             f'<td class="entry center">{ink("居宅")}</td>'
             f'<td class="entry struct">{ink("木造かわら")}<span class="ink strike">・合金メッキ鋼板</span><br>{ink("ぶき")}'
             f'<span class="ink strike">２</span><span class="red">３</span>{ink("階建")}</td>'
             f'<td class="entry int">{ink("1階　41")}<br>{ink("2階　33")}<br><span class="red">3階　8</span></td>'
             f'<td class="entry dec"><span class="ink strike">41</span> <span class="red">40</span><br>{ink("12")}<br>'
             f'<span class="red">28</span></td>'
             f'<td class="entry genin">{ink(GENIN)}</td>')
fix_panel = snippet(fix_cells) + ('<div class="bubrow"><span class="bubble">玄関の小屋根は0.91×1.82＝1.6562で、1階41.405の約4％。<br>'
                                  '床面積に算入する部分の屋根面積の30％未満の種類の屋根は表示しない！<br>'
                                  'ロフトは天井の最高部2.00で1.5m以上 → 3階（4.55×1.82＝8.28）<br>'
                                  '41.405は切り捨てて41.40（四捨五入しない）</span></div>')
ok_panel = snippet(entry_cells('', ink('居宅'), ink(KOUZOU), FLOORS, ink(GENIN)), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成21年度 第22問｜ロフトは3階、30％未満の小屋根は書かない</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 800})
        for name, html in [('H21_dai22mon_toukishinseisho_kansei', kansei),
                           ('H21_dai22mon_toukishinseisho_kansei_toi2', toi2),
                           ('H21_dai22mon_toukishinseisho_machigai', machigai)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_viewport_size({'width': 1200, 'height': 200})   # 内容の高さで書き出す（問2の画像の下に余白を残さない）
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
        browser.close()
