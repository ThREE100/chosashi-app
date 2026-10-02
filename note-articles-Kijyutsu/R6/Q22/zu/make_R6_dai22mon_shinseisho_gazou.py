"""令和6年度 第22問（建物）登記申請書の画像（完成形・「共有者」欄の添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_R6_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  欄の形は試験の答案用紙（第2欄）に合わせる：申請の日付・提出先と申請人（Ａ市Ｂ町三丁目16番地13　甲野桜子）・代理人（略）は印刷。
  建物の表示は、所在が2段（2段目は右端に小さな欄）、家屋番号の右に印刷の「（略）」、記入行3行（答案用紙では2行＋続きの1行）、
  最下段に「共有者」の欄。登録免許税の欄はない
- 添削　：`../prompt_R6_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第1欄（問1）・第4欄（問4）：申請書でない解答欄。答案用紙（A3横の左上が第1欄、右の列の下が第4欄）の欄の形どおりに、それぞれ別の画像（横1200px）にする

CSSと部品の作りは `R7/Q22/zu/make_R7_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/R6/Q22/zu/make_R6_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
table.bldg td.entry {{ height: 120px; }}
table.bldg td.center {{ text-align: center; }}
table.bldg td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.bldg td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.bldg td.genin {{ font-size: 17px; }}
table.bldg td .ink {{ font-size: 20px; }}
table.bldg td.kyouyuu {{ vertical-align: top; height: 190px; font-size: 19px; }}
table.bldg td.kyouyuu .lines {{ margin: 12px 0 0 34px; line-height: 1.9; }}
table.bldg td.kyouyuu .ink {{ font-size: 21px; }}
.kgrid {{ display: grid; grid-template-columns: 290px 70px 120px auto; row-gap: 6px; }}
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
.dstrike {{ position: relative; }}
.dstrike::before, .dstrike::after {{ content: ""; position: absolute; left: -3px; right: -3px; border-top: 2.5px solid {RED}; }}
.dstrike::before {{ top: 42%; }} .dstrike::after {{ top: 60%; }}
.ring {{ border: 3px solid {RED}; border-radius: 50%; padding: 2px 8px; }}
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
.shinsei {{ font-size: 20px; margin-bottom: 14px; }}
/* 第1欄・第4欄（申請書以外の解答欄） */
.sec {{ font-size: 24px; margin: 0 0 6px; font-weight: bold; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
table.ran {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.ran td {{ border: 1.5px solid #111; height: 80px; font-size: 22px; text-align: center; vertical-align: middle; }}
table.ran td .ink {{ font-size: 26px; }}
.ranpage {{ padding: 50px 60px 30px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

COLS = ('<colgroup><col style="width:5%"><col style="width:12%"><col style="width:12%"><col style="width:24%">'
        '<col style="width:10%"><col style="width:6%"><col style="width:31%"></colgroup>')
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
    """床面積の整数部・小数部のセル。floors: [(階の表示, 整数部, 小数部)]"""
    ints = br(*[ink(f'{k}{a}') for k, a, _ in floors])
    decs = br(*[ink(b) for _, _, b in floors])
    return f'<td class="entry int">{ints}</td><td class="entry dec">{decs}</td>'


def entry_row(label='', kind='', struct='', floors=(('', '', ''),), genin=''):
    return (f'<tr><td class="entry lab2">{label}</td><td class="entry center">{kind}</td>'
            f'<td class="entry center">{struct}</td>{area(*floors)}<td class="entry genin">{genin}</td></tr>')


def kyouyuu_cell(lines_html, extra=''):
    return f'<td class="kyouyuu" colspan="6">共有者<div class="lines">{lines_html}</div>{extra}</td>'


SHOZAI = 'Ａ市Ｂ町三丁目16番地13'
KYOUYUU_OK = ('<div class="kgrid">'
              f'{ink("Ａ市Ｂ町三丁目16番地13")}{ink("持分")}{ink("５分の３")}{ink("甲野松雄")}'
              f'{ink("Ａ市Ｂ町三丁目16番地13")}<span></span>{ink("５分の２")}{ink("甲野桜子")}</div>')
SHINSEININ = '<div class="plainrow"><div class="lab">申　　請　　人</div><div class="printed">Ａ市Ｂ町三丁目16番地13　　甲　野　桜　子</div></div>'

rows = (entry_row('', ink('居宅'), ink(br('木造合金メッキ', '鋼板ぶき２階建')), [('1階', '68', '85'), ('2階', '71', '68')],
                  ink('令和６年９月30日新築'))
        + entry_row() + entry_row())
table = (f'<table class="bldg">{COLS}'
         f'<tr><td class="vert" rowspan="8">建物の表示</td>'
         f'<td class="lab2" rowspan="2">所　在</td><td class="val" colspan="5">{ink(SHOZAI)}</td></tr>'
         f'<tr><td class="val" colspan="4"></td><td class="val"></td></tr>'
         f'<tr><td class="lab2 val">家屋番号</td><td class="val center" colspan="2">（略）</td>'
         f'<td class="val" colspan="3"></td></tr>'
         f'{HEAD}{rows}<tr>{kyouyuu_cell(KYOUYUU_OK)}</tr></table>')

kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物表題登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:130px">{ink(br('建物図面　各階平面図　所有権証明書　住所証明書', '代理権限証書'))}</div></div>
<div class="plainrow"><div class="printed">令和６年10月18日　申請　Ａ地方法務局</div></div>
{SHINSEININ}
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{table}
<div class="caption">令和6年度 土地家屋調査士試験 第22問 問2 登記申請書 解答例</div>
</div>''')


# ---- 第1欄（問1）・第4欄（問4）：申請書とは別の画像（答案用紙どおり、記号と記入欄を交互に並べた表） ----
def ran(sec, cells, caption):
    cols = '<colgroup><col style="width:10%"><col style="width:40%"><col style="width:10%"><col style="width:40%"></colgroup>'
    rows = ''.join(f'<tr><td>{a}</td><td>{ink(b)}</td><td>{c}</td><td>{ink(d)}</td></tr>' for a, b, c, d in cells)
    return page(f'<div class="ranpage"><div class="sec">{sec}</div><table class="ran">{cols}{rows}</table>'
                f'<div class="caption">{caption}</div></div>')


dai1 = ran('第1欄', [('ア', '確認', 'イ', '検査'), ('ウ', '建築請負人', 'エ', '固定資産税')],
           '令和6年度 土地家屋調査士試験 第22問 問1（第1欄）解答例　※アとイは順不同')
dai4 = ran('第4欄', [('①', '構造上', '②', '利用上')],
           '令和6年度 土地家屋調査士試験 第22問 問4（第4欄）解答例')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：「共有者」欄 ----
def snippet(cell, good=False):
    g = ' class="good"' if good else ''
    chk = CHECK_SVG if good else ''
    return (f'<div class="shinsei">{SHINSEININ}</div>'
            f'<div class="okwrap"><table class="bldg"{g}>{COLS}<tr><td class="vert tight">建物の表示</td>{cell}</tr></table>{chk}</div>')


NG_LINE = 'Ａ市Ｂ町三丁目16番地13　　甲野桜子'
ng_panel = snippet(kyouyuu_cell(ink('所有者　' + NG_LINE)))
fix_cell = ('<td class="kyouyuu" colspan="6"><span class="ring">共有者</span><div class="lines">'
            f'<span class="ink dstrike">所有者</span><span class="ink">　{NG_LINE}</span><br>'
            '<span class="red">＋　甲野松雄　持分５分の３、甲野桜子　５分の２（事実関係３の費用の割合）</span></div></td>')
fix_panel = snippet(fix_cell) + \
    ('<div class="bubrow"><span class="bubble">申請人（手続をする人）と表題部所有者（登記記録に載る人）は別物！<br>'
     '共有者全員と持分を書く</span></div>')
ok_panel = snippet(kyouyuu_cell(KYOUYUU_OK), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">令和6年度 第22問｜申請人が1人でも、登記される所有者は共有者全員</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 100})   # 高さは内容に合わせる（full_page）
        for name, html in [('R6_dai22mon_toukishinseisho_kansei', kansei),
                           ('R6_dai22mon_toukishinseisho_machigai', machigai),
                           ('R6_dai22mon_dai1ran_kansei', dai1), ('R6_dai22mon_dai4ran_kansei', dai4)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else ('横長（第1欄・第4欄は小さい表なので横長でよい）' if 'ran' in name else '横長（要確認）')))
        browser.close()
