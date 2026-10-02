"""令和5年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_R5_dai21mon_toukishinseisho_gazou.md` どおり（問4・令和5年10月16日の土地地目変更・分合筆登記）。縦長（横1200px）
- 添削　：`../prompt_R5_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第1欄（問1のア〜エ）・第5欄（問5の①〜④）：申請書でない解答欄も、記号ごとの記入欄の形で別の画像にする（横1200pxの横長。
  2026-10-02追加）。試験の答案用紙そのものはリポジトリにないので、同じ時期の令和6年度・令和7年度の第21問の答案用紙
  （`public/kijutsu/R06-tochi/a1.webp`・`R07-tochi/a1.png`）の穴埋めの欄（記号と記入欄を1行に2組ずつ並べた表）にならった仮の形にしている

R6/Q21の `make_R6_dai21mon_shinseisho_gazou.py` の様式（CSS・土地の表示の表）を使い、地番の列を広げた（「（イ）１番４」が折り返さないように）。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP。なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/R5/Q21/zu/make_R5_dai21mon_shinseisho_gazou.py [出力フォルダ]
- 座標の欄（R5・R6は第2欄、R7は第1欄・第4欄）も、答案用紙の座標値の表の形で別の画像にする（横1200pxの横長。2026-10-02追加）
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
.page {{ padding: 80px 70px 40px; min-height: 1650px; display: flex; flex-direction: column; }}
.page .caption {{ margin-top: auto; padding-top: 30px; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 56px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 32px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 26px; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.plain {{ font-size: 22px; margin: 4px 0 26px; }}
.dairi {{ display: flex; font-size: 22px; margin-bottom: 26px; }}
.dairi .lab {{ padding-top: 0; }}
.dairi .ryaku {{ flex: 1; text-align: center; }}
table.land {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.land td {{ border: 1.5px solid #111; font-size: 22px; padding: 0 12px; height: 92px; vertical-align: middle; }}
table.land.compact td.vert {{ letter-spacing: 0.05em; font-size: 18px; }}
.box.fix {{ line-height: 1.75; }}
table.land td.head {{ height: 50px; text-align: center; font-size: 20px; }}
table.land td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.land td.shozai-lab {{ text-align: center; height: 76px; }}
table.land td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 6px; }}
table.land td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 6px; }}
table.land td.chimoku {{ text-align: center; }}
table.land td .ink, .box .ink {{ font-size: 26px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 30px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 70px 30px; border-bottom: 2px solid #bbb; }}
.panel:last-of-type {{ border-bottom: none; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.strike {{ position: relative; }}
.strike::after {{ content: ""; position: absolute; left: -4px; right: -4px; top: 52%; border-top: 3px solid {RED};
                  transform: rotate(-2deg); }}
.red {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; left: 60px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: -12px 0 20px 170px; }}
.bubrow.table {{ margin: 14px 0 0 480px; }}
.bubrow.table2 {{ margin: 18px 0 0 0; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.okrow {{ position: relative; }}
.check {{ position: absolute; right: -8px; top: -30px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def land_table(rows, n_rows=5, shozai='Ａ市Ｂ町二丁目', compact=False):
    """土地の表示の表。rows: [(地番, 地目, 整数部, 小数部, 登記原因)]。各値は HTML（記入部分は呼び出し側で .ink を付ける）"""
    h = [f'<table class="land{" compact" if compact else ""}"><colgroup><col style="width:6%"><col style="width:20%"><col style="width:12%">'
         '<col style="width:13%"><col style="width:7%"><col style="width:42%"></colgroup>',
         f'<tr><td class="shozai-lab" colspan="2">所　在</td><td colspan="4">{shozai}</td></tr>',
         f'<tr><td class="vert" rowspan="{n_rows + 1}">土地の表示</td><td class="head">①地　　番</td>'
         '<td class="head">②地　目</td><td class="head" colspan="2">③地　積　（m²）</td>'
         '<td class="head">登記原因及びその日付</td></tr>']
    for i in range(n_rows):
        c, m, a, b, g = rows[i] if i < len(rows) else ('', '', '', '', '')
        h.append(f'<tr><td>{c}</td><td class="chimoku">{m}</td><td class="int">{a}</td><td class="dec">{b}</td>'
                 f'<td>{g}</td></tr>')
    h.append('</table>')
    return ''.join(h)


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---- 完成形（記入データは prompt_R5_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '令和５年10月16日　申請　Ａ地方法務局'
PURPOSE = '土地地目変更・分合筆登記'
ATTACH = '地積測量図　登記識別情報　印鑑証明書　代理権限証書'
APPLICANT = 'Ａ市Ｂ町二丁目２番地１　河野桂子'
TAX = '金2,000円'
SHOZAI = 'Ａ市Ｂ町二丁目'
ROWS = [('１番４', '宅地', '25', '61', ''),
        ('（イ）１番４', '宅地', '3', '52', '③１番１に一部合併'),
        ('（ロ）', '', '22', '09', '１番４から分筆して１番１に合併する部分'),
        ('１番１', '雑種地', '335', '', ''),
        ('１番１', '宅地', '357', '59', '②③令和５年９月20日地目変更<br>③１番４から一部合併')]
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink(PURPOSE)}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box fix" style="height:130px">{ink(ATTACH)}</div></div>
<div class="plain">{DATE}</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:96px">{ink(APPLICANT)}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink(TAX)}</div></div>
<div style="height:14px"></div>
{land_table([tuple(ink(v) for v in r) for r in ROWS], shozai=ink(SHOZAI))}
<div class="caption">令和5年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----
WRONG_ATTACH = '地積測量図　登記識別情報　代理権限証書'


def snippet(attach_html, row, bubble1='', bubble2='', good=False):
    """答案用紙の順序どおり「添付書類」の欄を上に、土地の表示の表（所在と記入行1行）を下に描く。"""
    chk = CHECK_SVG if good else ''
    return f'''<div class="row okrow"><div class="lab">添　付　書　類</div><div class="box fix{' good' if good else ''}" style="min-height:96px">{attach_html}</div>{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble1}</span></div>' if bubble1 else ''}
<div class="{'good' if good else ''}" style="position:relative">{land_table([row], n_rows=1, shozai=ink(SHOZAI), compact=True)}{chk if good else ''}</div>
{f'<div class="bubrow table2">{bubble2}</div>' if bubble2 else ''}'''


GEN_NG = ink('②令和５年９月20日地目変更<br>③１番４から一部合併')
GEN_OK = ink('②③令和５年９月20日地目変更<br>③１番４から一部合併')
ng_panel = snippet(ink(WRONG_ATTACH), (ink('１番１'), ink('宅地'), ink('357'), ink('09'), GEN_NG))
fix_panel = snippet(
    f'{ink(WRONG_ATTACH)}<span class="red">　印鑑証明書</span>',
    (ink('１番１'), ink('宅地'), ink('357'),
     '<span class="red" style="font-size:24px;display:block;line-height:1">59</span><span class="ink strike">09</span>',
     '<span class="ink">②</span><span class="red">③</span><span class="ink">令和５年９月20日地目変更<br>③１番４から一部合併</span>'),
    bubble1='合筆は委任状に記名押印＋印鑑証明書（令第18条）',
    bubble2='<span class="bubble">問題文の注9：地積測量図の335.5096500を援用 → 335.5096500＋22.09＝357.59965</span><br>'
            '<span class="bubble" style="margin-top:22px">宅地になると地積の表示が変わるので③も付ける</span>')
ok_panel = snippet(ink(ATTACH), (ink('１番１'), ink('宅地'), ink('357'), ink('59'), GEN_OK), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">令和5年度 第21問｜合筆には印鑑証明書、地積の端数は地積測量図から援用</div>''')

# ---- 第1欄・第5欄（申請書でない解答欄。2026-10-02追加） ----
RAN_CSS = '''
.ranpage { padding: 50px 60px 34px; }
.ranhead { font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin-bottom: 14px; }
table.ran { width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; }
table.ran td { border: 1.5px solid #111; height: 84px; font-size: 22px; vertical-align: middle; }
table.ran td.k { text-align: center; }
table.ran td.v { padding-left: 22px; }
table.ran td.v .ink { font-size: 28px; }
'''


def ran_image(head, pairs, caption):
    """記号と記入欄を1行に2組ずつ並べた穴埋めの欄（令和6年度・令和7年度の答案用紙の形）"""
    trs = ''
    for i in range(0, len(pairs), 2):
        cells = ''.join(f'<td class="k">{k}</td><td class="v">{ink(v)}</td>' for k, v in pairs[i:i + 2])
        trs += f'<tr>{cells}</tr>'
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}{RAN_CSS}</style></head><body>'
            f'<div class="ranpage"><div class="ranhead">{head}</div>'
            f'<table class="ran"><colgroup><col style="width:9%"><col style="width:41%"><col style="width:9%">'
            f'<col style="width:41%"></colgroup>{trs}</table>'
            f'<div class="caption">{caption}</div></div></body></html>')


DAI1 = [('ア', '一筆'), ('イ', '測量'), ('ウ', 'Ｆ点'), ('エ', 'Ｊ点')]
DAI5 = [('①', '表題部所有者'), ('②', '所有権'), ('③', '異議'), ('④', '職権')]
dai1 = ran_image('第1欄', DAI1, '令和5年度 土地家屋調査士試験 第21問 第1欄（問1）解答例')
dai5 = ran_image('第5欄', DAI5, '令和5年度 土地家屋調査士試験 第21問 第5欄（問5）解答例')


# ---- 座標の欄（申請書でない解答欄。2026-10-02追加。答案用紙の座標値の表の形：左上の斜線の欄・X座標（m）・Y座標（m）） ----
Z_CSS = '''
.ranpage { padding: 50px 60px 34px; }
.ranhead { font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin: 0 0 14px; }
table.zh { width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; }
table.zh td { border: 1.5px solid #111; height: 72px; font-size: 22px; text-align: center; vertical-align: middle; }
table.zh td.diag { background: linear-gradient(to top right, transparent calc(50% - 1px), #111 50%, transparent calc(50% + 1px)); }
table.zh td .ink { font-size: 28px; }
'''


def zahyou(head, rows, caption):
    """rows: [(点名, X, Y)]"""
    trs = ''.join(f'<tr><td>{n}</td><td>{ink(x)}</td><td>{ink(y)}</td></tr>' for n, x, y in rows)
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}{Z_CSS}</style></head><body>'
            f'<div class="ranpage"><div class="ranhead">{head}</div><table class="zh"><colgroup><col style="width:32%">'
            f'<col style="width:34%"><col style="width:34%"></colgroup>'
            f'<tr><td class="diag"></td><td>Ｘ座標（m）</td><td>Ｙ座標（m）</td></tr>{trs}</table>'
            f'<div class="caption">{caption}</div></div></body></html>')


dai2 = zahyou('第2欄', [('Ｂ点', '702.67', '702.62'), ('Ｈ点', '680.64', '702.62')],
               '令和5年度 土地家屋調査士試験 第21問 第2欄（問2）解答例')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 200})
    for name, html in [('R5_dai21mon_dai1ran_kansei', dai1), ('R5_dai21mon_dai2ran_kansei', dai2), ('R5_dai21mon_toukishinseisho_kansei', kansei),
                       ('R5_dai21mon_toukishinseisho_machigai', machigai), ('R5_dai21mon_dai5ran_kansei', dai5)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
    browser.close()
