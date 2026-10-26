"""令和6年度 第22問（建物）登記申請書の画像（完成形・欄ごとの添削）と第1欄・第4欄の画像を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 欄の形は試験の答案用紙（`../touan_youshi/R6_dai22mon_touan_youshi.pdf` の1ページ目。A3横の左の列に第1欄・第2欄、右の列に第2欄の続きと第4欄）を
  pymupdf の `get_drawings()` で測った値に合わせる（2026-10-26、6-3）：
  ・建物の表示の表の列の幅：縦書き27.0pt・所在/家屋番号/主である建物又は附属建物65.2pt・①種類52.4pt・②構造109.1pt・
    ③床面積の整数部68.1pt＋小数部42.5pt・登記原因及びその日付107.7pt（表の幅472.0pt。右の列の表も同じ比）
  ・行の高さ：所在28.4pt×2・家屋番号22.7pt・見出し45.3pt・記入行61.0pt×2（左の列の表）、記入行60.9pt＋共有者の欄113.4pt（右の列の表）
  ・登記の目的の枠56.7pt・添付書類の枠79.4pt。申請の日付・提出先、申請人（A市B町三丁目16番地13　甲野桜子）、代理人（略）は印刷
  ・第1欄・第4欄：記号の枠56.7pt・記入の枠179.3pt（2組）、行の高さ39.6pt
  画像のpx ＝ 答案用紙のpt × 2.288（表の幅472.0pt ＝ 1080px）。HTMLは固定の height ではなく min-height にする
- 完成形：`../prompt_R6_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。答案用紙は左の列の表（記入行2行）と右の列の表
  （記入行1行＋共有者の欄）に分かれているので、左の列の内容の下に右の列の表を続けて縦に積む。申請書の画像には「第○欄」を入れない（共通フォーム）
- 添削：誤答の欄ごとに1枚（所在・構造・原因及びその日付・共有者）。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第1欄・第4欄：申請書でない解答欄は、印刷どおりの「第1欄」「第4欄」の見出しをつけた別の画像にする

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
.page {{ padding: 50px 60px 40px; min-height: 1650px; display: flex; flex-direction: column; }}
.page .caption {{ margin-top: auto; padding-top: 30px; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 40px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 26px; }}
.lab {{ width: 150px; font-size: 20px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 22px; }}
.plainrow .lab {{ padding-top: 0; font-size: 22px; width: 190px; }}
.plainrow .ryaku {{ flex: 1; text-align: center; }}
.plainrow .printed {{ flex: 1; letter-spacing: 0.05em; }}
table.bldg {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.bldg td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 6px; vertical-align: middle; line-height: 1.5; }}
table.bldg td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.bldg td.vert.tight {{ letter-spacing: 0.15em; font-size: 20px; }}
table.bldg td.lab2 {{ text-align: center; font-size: 19px; }}
table.bldg td.head {{ text-align: center; font-size: 18px; min-height: 104px; height: 104px; }}
table.bldg td.val {{ min-height: 65px; height: 65px; }}
table.bldg td.kaoku {{ min-height: 52px; height: 52px; }}
table.bldg td.entry {{ min-height: 140px; height: 140px; }}
table.bldg td.center {{ text-align: center; }}
table.bldg td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.bldg td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.bldg td.genin {{ font-size: 17px; }}
table.bldg td .ink {{ font-size: 20px; }}
table.bldg td.genin .ink {{ font-size: 17px; }}
table.bldg td.kyouyuu {{ vertical-align: top; min-height: 259px; height: 259px; font-size: 19px; }}
table.bldg td.kyouyuu .lines {{ margin: 14px 0 0 34px; line-height: 1.9; }}
table.bldg td.kyouyuu .ink {{ font-size: 21px; }}
.kgrid {{ display: grid; grid-template-columns: 290px 70px 120px auto; row-gap: 6px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 30px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.cont {{ margin-top: 14px; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.panel:last-of-type {{ border-bottom: none; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.strike {{ position: relative; }}
.strike::after {{ content: ""; position: absolute; left: -4px; right: -4px; top: 52%; border-top: 3px solid {RED};
                  transform: rotate(-3deg); }}
.ring {{ border: 3px solid {RED}; border-radius: 50%; padding: 2px 8px; }}
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
.shinsei {{ font-size: 20px; margin-bottom: 14px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# 表の列の幅の比は、試験の答案用紙（touan_youshi/ の原本PDF）の罫線から測った値（左の列の表も右の列の表も同じ）
COLS_PCT = (5.7, 13.8, 11.1, 23.1, 14.4, 9.0, 22.8)
COLS = '<colgroup>' + ''.join(f'<col style="width:{v}%">' for v in COLS_PCT) + '</colgroup>'
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


def kyouyuu_cell(lines_html, ring=False):
    lab = '<span class="ring">共有者</span>' if ring else '共有者'
    return f'<td class="kyouyuu" colspan="6">{lab}<div class="lines">{lines_html}</div></td>'


SHOZAI = 'Ａ市Ｂ町三丁目16番地13'
SHOZAI_NG = 'Ａ市Ｂ町三丁目16番13'
S_KOUZOU = br('木造合金メッキ', '鋼板ぶき２階建')
S_KOUZOU_NG = '木造２階建'
GENIN = '令和６年９月30日新築'
GENIN_NG = '令和６年10月18日新築'
KYOUYUU_OK = ('<div class="kgrid">'
              f'{ink("Ａ市Ｂ町三丁目16番地13")}{ink("持分")}{ink("５分の３")}{ink("甲野松雄")}'
              f'{ink("Ａ市Ｂ町三丁目16番地13")}<span></span>{ink("５分の２")}{ink("甲野桜子")}</div>')
NG_LINE = 'Ａ市Ｂ町三丁目16番地13　　甲野桜子'
SHINSEININ = '<div class="plainrow"><div class="lab">申　　請　　人</div><div class="printed">Ａ市Ｂ町三丁目16番地13　　甲　野　桜　子</div></div>'


def left_table(shozai1, rows):
    """答案用紙の左の列の建物の表示の表（所在2段・家屋番号・見出し・記入行2行）"""
    return (f'<table class="bldg">{COLS}'
            f'<tr><td class="vert" rowspan="6">建物の表示</td>'
            f'<td class="lab2" rowspan="2">所　在</td><td class="val" colspan="5">{shozai1}</td></tr>'
            f'<tr><td class="val" colspan="4"></td><td class="val"></td></tr>'
            f'<tr><td class="lab2 kaoku">家屋番号</td><td class="kaoku center" colspan="2">（略）</td>'
            f'<td class="kaoku" colspan="3"></td></tr>'
            f'{HEAD}{rows}</table>')


def right_table(row, kyouyuu):
    """答案用紙の右の列の建物の表示の表（記入行1行＋共有者の欄。見出しの行はない）"""
    return (f'<table class="bldg cont">{COLS}'
            f'<tr><td class="vert" rowspan="2">建物の表示</td>{row[4:]}'
            f'<tr>{kyouyuu}</tr></table>')


rows_left = (entry_row('', ink('居宅'), ink(S_KOUZOU), [('1階', '68', '85'), ('2階', '71', '68')], ink(GENIN)) + entry_row())
row_right = entry_row()
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="min-height:130px">{ink('建物表題登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="min-height:182px">{ink(br('建物図面　各階平面図　所有権証明書　住所証明書', '代理権限証書'))}</div></div>
<div class="plainrow"><div class="printed">令和６年10月18日　申請　Ａ地方法務局</div></div>
{SHINSEININ}
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{left_table(ink(SHOZAI), rows_left)}
{right_table(row_right, kyouyuu_cell(KYOUYUU_OK))}
<div class="caption">令和6年度 土地家屋調査士試験 第22問 問2 登記申請書 解答例（答案用紙の左の列の表の下に、右の列の表を続けて描いている）</div>
</div>''')


# ---- 添削：①誤答 → ②添削 → ③正解 を縦に3コマ ----
def panels(ng, fix, ok, caption):
    return page(f'''<div class="tall">
<div class="panel"><div class="ptitle ng">①誤答</div>{ng}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok}</div>
<div class="caption" style="margin:10px 0 30px">{caption}</div></div>''')


def wrap(table_html, good=False):
    chk = CHECK_SVG if good else ''
    return f'<div class="okwrap">{table_html}{chk}</div>'


def bubble(text):
    return f'<div class="bubrow"><span class="bubble">{text}</span></div>'


def shozai_snippet(shozai_html, good=False):
    g = ' good' if good else ''
    t = (f'<table class="bldg{g}">{COLS}'
         f'<tr><td class="vert tight" rowspan="2">建物の表示</td>'
         f'<td class="lab2" rowspan="2">所　在</td><td class="val" colspan="5" style="min-height:96px;height:96px">{shozai_html}</td></tr>'
         f'<tr><td class="val" colspan="4"></td><td class="val"></td></tr></table>')
    return wrap(t, good)


def row_snippet(row, good=False):
    g = ' good' if good else ''
    t = f'<table class="bldg{g}">{COLS}<tr><td class="vert tight" rowspan="2">建物の表示</td>{HEAD[4:]}{row}</table>'
    return wrap(t, good)


def kyouyuu_snippet(cell, good=False):
    g = ' good' if good else ''
    t = (f'<table class="bldg{g}">{COLS}<tr><td class="vert tight">建物の表示</td>{cell}</tr></table>')
    return f'<div class="shinsei">{SHINSEININ}</div>' + wrap(t, good)


# 所在（番地の「地」を入れ忘れた誤答）
machigai_shozai = panels(
    shozai_snippet(ink(SHOZAI_NG)),
    shozai_snippet(f'<span class="ink strike">{SHOZAI_NG}</span><br><span class="red">{SHOZAI}</span>') +
    bubble('土地の地番は「16番13」、建物の所在は「16番地13」。<br>「番」のあとに「地」を入れて、建物の所在は番地で書く'),
    shozai_snippet(ink(SHOZAI), good=True),
    '令和6年度 第22問｜土地は「番」、建物の所在は「番地」')

# 構造（屋根の種類を書き忘れた誤答）
r_ng = entry_row('', ink('居宅'), ink(S_KOUZOU_NG), [('1階', '68', '85'), ('2階', '71', '68')], ink(GENIN))
r_fix = entry_row('', ink('居宅'), f'<span class="ink strike">{S_KOUZOU_NG}</span><br><span class="red">木造合金メッキ<br>鋼板ぶき２階建</span>',
                  [('1階', '68', '85'), ('2階', '71', '68')], ink(GENIN))
r_ok = entry_row('', ink('居宅'), ink(S_KOUZOU), [('1階', '68', '85'), ('2階', '71', '68')], ink(GENIN))
machigai_kouzou = panels(
    row_snippet(r_ng),
    row_snippet(r_fix) + bubble('構造は「主な材料・屋根の種類・階数」の順。<br>屋根は事実関係4(3)の合金メッキ鋼板ぶきを書く'),
    row_snippet(r_ok, good=True),
    '令和6年度 第22問｜構造は、材料・屋根・階数をそろえて書く')

# 登記原因及びその日付（申請日を書いた誤答）
g_ng = entry_row('', ink('居宅'), ink(S_KOUZOU), [('1階', '68', '85'), ('2階', '71', '68')], ink(GENIN_NG))
g_fix = entry_row('', ink('居宅'), ink(S_KOUZOU), [('1階', '68', '85'), ('2階', '71', '68')],
                  f'<span class="ink strike">{GENIN_NG}</span><br><span class="red">{GENIN}</span>')
g_ok = entry_row('', ink('居宅'), ink(S_KOUZOU), [('1階', '68', '85'), ('2階', '71', '68')], ink(GENIN))
machigai_genin = panels(
    row_snippet(g_ng),
    row_snippet(g_fix) + bubble('書く日は、申請の日（10月18日）ではなく、<br>新築した日（完成して引渡しを受けた9月30日）'),
    row_snippet(g_ok, good=True),
    '令和6年度 第22問｜原因の日付は「申請の日」ではなく「新築の日」')

# 共有者（申請人1人だけを所有者として書いた誤答）
NG_CELL = kyouyuu_cell(ink('所有者　' + NG_LINE))
FIX_CELL = kyouyuu_cell(f'<span class="ink strike">所有者</span><span class="ink">　{NG_LINE}</span><br>'
                        '<span class="red">＋　甲野松雄　持分５分の３、甲野桜子　５分の２（事実関係３の費用の割合）</span>', ring=True)
OK_CELL = kyouyuu_cell(KYOUYUU_OK)
machigai_kyouyuu = panels(
    kyouyuu_snippet(NG_CELL),
    kyouyuu_snippet(FIX_CELL) + bubble('申請人（手続をする人）と表題部所有者（登記記録に載る人）は別物！<br>共有者全員と持分を書く'),
    kyouyuu_snippet(OK_CELL, good=True),
    '令和6年度 第22問｜申請人が1人でも、登記される所有者は共有者全員')


# ---- 第1欄・第4欄（申請書でない解答欄）：答案用紙の枠の形（記号の枠12.0％・記入の枠38.0％の2組）。印刷どおり見出しの「第N欄」を入れる ----
def anaume(title, rows, caption):
    def pair(k, v):
        return (f'<td class="lab2" style="font-size:26px;text-align:center;min-height:91px;height:91px">{k}</td>'
                f'<td style="padding-left:22px;font-size:26px">{ink(v)}</td>')
    trs = ''.join(f'<tr>{pair(*rows[i])}{pair(*rows[i + 1])}</tr>' for i in range(0, len(rows), 2))
    return page(f'''<div style="padding:50px 60px 36px">
<div style="font-size:28px;font-weight:bold;font-family:'Noto Sans CJK JP',sans-serif;margin-bottom:10px">{title}</div>
<table class="bldg"><colgroup><col style="width:12%"><col style="width:38%"><col style="width:12%"><col style="width:38%"></colgroup>{trs}</table>
<div class="caption">{caption}</div></div>''')


dai1 = anaume('第1欄', [('ア', '確認'), ('イ', '検査'), ('ウ', '建築請負人'), ('エ', '固定資産税')],
              '令和6年度 土地家屋調査士試験 第22問 問1（第1欄）解答例　※アとイは順不同')
dai4 = anaume('第4欄', [('①', '構造上'), ('②', '利用上')],
              '令和6年度 土地家屋調査士試験 第22問 問4（第4欄）解答例')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome'))   # chrome-linux（古い版）・chrome-linux64（新しい版）
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 200})
        for name, html in [('R6_dai22mon_dai1ran_kansei', dai1),
                           ('R6_dai22mon_dai4ran_kansei', dai4),
                           ('R6_dai22mon_toukishinseisho_kansei', kansei),
                           ('R6_dai22mon_toukishinseisho_machigai_shozai', machigai_shozai),
                           ('R6_dai22mon_toukishinseisho_machigai_kouzou', machigai_kouzou),
                           ('R6_dai22mon_toukishinseisho_machigai_genin', machigai_genin),
                           ('R6_dai22mon_toukishinseisho_machigai', machigai_kyouyuu)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else ('横長（第1欄・第4欄は小さい表なので横長でよい）' if 'ran' in name else '横長（要確認）')))
        browser.close()
