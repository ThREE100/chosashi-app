"""令和3年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_R3_dai21mon_toukishinseisho_gazou.md` どおり。縦長（横1200px）。
  項目の順序は試験の答案用紙（`../touan_youshi/`。A3横の左の列が「第3欄」の表題と登記の目的・添付書類・登録免許税、右の列が
  項目名のない申請人の枠・代理人（略）・申請の日付と提出先・所在と土地の表示）どおり、左の列の下に右の列を積んで
  「第3欄 → 登記の目的 → 添付書類 → 登録免許税 → 申請人の枠（項目名なし）→ 代理人 → 申請の日付と提出先 → 土地の表示」
- 添削　：`../prompt_R3_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第1欄（問1のA点・C点・H点・L点）・第2欄（問2のア〜カ）：申請書でない解答欄も、別の画像にする（横1200pxの横長。2026-10-02追加）。
  欄の形は試験の答案用紙（`../touan_youshi/R3_dai21mon_touan_youshi.pdf`）で確かめた（2026-10-02）。見出しは印刷どおり「第1欄」「第2欄」だけ。
  第1欄は左上が斜線のセル・「Ｘ座標（m）」「Ｙ座標（m）」の見出し行と「Ａ点」「Ｃ点」「Ｈ点」「Ｌ点」の4行、
  第2欄は「ア｜イ」「ウ｜エ」「オ｜カ」の3行（記号と記入欄を2組ずつ横に並べる）
- 完成形の表の下に、相続証明書の今の扱い（法定相続情報番号）の注を入れる（2026-10-02追加。記事の本文の注と同じ文言）

必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・Noto Sans CJK JP。なければIPAゴシック）
実行: python3 note-articles-Kijyutsu/R3/Q21/zu/make_R3_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
SANS = '"Noto Sans CJK JP", "IPAGothic", sans-serif'

CSS = f'''
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: #fff; width: 1200px; font-family: "IPAMincho", "Noto Serif CJK JP", serif; color: #111; }}
.page {{ padding: 70px 70px 40px; min-height: 1700px; display: flex; flex-direction: column; }}
.page .caption {{ margin-top: auto; padding-top: 30px; }}
.ranno {{ font-family: {SANS}; font-size: 22px; font-weight: bold; margin: 0 0 -38px; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 50px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 28px; position: relative; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.7; }}
.ink {{ color: {INK}; font-family: {SANS}; }}
.plain {{ font-size: 22px; margin: 4px 0 24px; }}
.dairi {{ display: flex; font-size: 22px; margin: 4px 0 18px; }}
.dairi .lab {{ padding-top: 0; }}
.dairi .ryaku {{ flex: 1; text-align: right; padding-right: 180px; }}
.appbox {{ border: 2px solid #111; padding: 16px 22px; margin-bottom: 22px; position: relative; }}
table.app {{ border-collapse: collapse; font-size: 24px; line-height: 1.75; }}
table.app td {{ padding: 0; vertical-align: top; white-space: nowrap; }}
table.app td.k {{ width: 200px; }}
table.app td.r {{ width: 96px; }}
table.app td.center {{ text-align: center; }}
table.land {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.land td {{ border: 1.5px solid #111; font-size: 22px; padding: 0 12px; height: 92px; vertical-align: middle; }}
table.land td.head {{ height: 50px; text-align: center; font-size: 20px; }}
table.land td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.land td.shozai-lab {{ text-align: center; height: 76px; }}
table.land td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 6px; }}
table.land td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 6px; }}
table.land td.chimoku {{ text-align: center; }}
table.land td .ink {{ font-size: 24px; }}
table.land td.cause .ink {{ font-size: 22px; line-height: 1.45; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 30px; font-family: {SANS}; }}
/* 添削画像 */
.panel {{ padding: 26px 70px 28px; border-bottom: 2px solid #bbb; }}
.panel:last-of-type {{ border-bottom: none; }}
.ptitle {{ font-family: {SANS}; font-size: 28px; font-weight: bold; margin-bottom: 18px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.strike {{ position: relative; }}
.strike::after {{ content: ""; position: absolute; left: -3px; right: -3px; top: 52%; border-top: 3px solid {RED};
                  transform: rotate(-3deg); }}
.red {{ color: {RED}; font-family: {SANS}; }}
.over {{ position: relative; display: inline-block; }}
.over .up {{ position: absolute; left: -6px; top: -26px; font-size: 19px; color: {RED}; font-family: {SANS};
             white-space: nowrap; font-weight: bold; }}
.caret {{ color: {RED}; font-family: {SANS}; font-weight: bold; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5; font-family: {SANS}; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; left: 60px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: -8px 0 16px 0; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.check {{ position: absolute; right: -14px; top: -22px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---- 記入データ（prompt_R3_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '令和３年10月17日　申請　Ａ地方法務局'
PURPOSE = '土地分筆登記'
ATTACH = ['地積測量図　相続証明書', '代位原因証書　代理権限証書']
TAX = '金3,000円'
HISOZOKU = '（被相続人　山田太郎）'
ICHIRO = 'Ｍ市Ｄ町五丁目２番２号　山田一郎'
SABURO = 'Ｓ市Ｄ町一丁目３番５号　山田三郎'
JIRO = 'Ｋ市Ｄ町二丁目10番１号　山田二郎'
DAII = '代位原因　令和３年８月１日遺産分割の所有権移転登記請求権'
SHOZAI = 'Ｋ市Ｄ町二丁目'
ROWS = [('10番１', '宅地', '386', '30', ''),
        ('（イ）', '', '126', '84', '③10番１、10番８、10番９に分筆'),
        ('（ロ）10番８', '宅地', '123', '21', '10番１から分筆'),
        ('（ハ）10番９', '宅地', '135', '84', '10番１から分筆')]


def applicant_table(rows):
    """申請人の枠の中身。rows: [(左の見出し, 相続人の語, 住所・氏名)] または ('center', 文字) / ('line', 文字)"""
    h = ['<table class="app">']
    for r in rows:
        if r[0] == 'center':
            h.append(f'<tr><td colspan="3" class="center">{r[1]}</td></tr>')
        elif r[0] == 'line':
            h.append(f'<tr><td colspan="3">{r[1]}</td></tr>')
        elif r[0] == 'gap':
            h.append('<tr><td colspan="3" style="height:14px"></td></tr>')
        else:
            h.append(f'<tr><td class="k">{r[0]}</td><td class="r">{r[1]}</td><td>{r[2]}</td></tr>')
    h.append('</table>')
    return ''.join(h)


def land_table(rows, n_rows=5):
    h = ['<table class="land"><colgroup><col style="width:6%"><col style="width:17%"><col style="width:14%">'
         '<col style="width:13%"><col style="width:7%"><col style="width:43%"></colgroup>',
         f'<tr><td class="shozai-lab" colspan="2">所　在</td><td colspan="4">{ink(SHOZAI)}</td></tr>',
         f'<tr><td class="vert" rowspan="{n_rows + 1}">土地の表示</td><td class="head">①地　　番</td>'
         '<td class="head">②地　　目</td><td class="head" colspan="2">③地　積　（m²）</td>'
         '<td class="head">登記原因及びその日付</td></tr>']
    for i in range(n_rows):
        c, m, a, b, g = rows[i] if i < len(rows) else ('', '', '', '', '')
        h.append(f'<tr><td>{ink(c)}</td><td class="chimoku">{ink(m)}</td><td class="int">{ink(a)}</td>'
                 f'<td class="dec">{ink(b)}</td><td class="cause">{ink(g)}</td></tr>')
    h.append('</table>')
    return ''.join(h)


OK_APPLICANT = [('center', ink(HISOZOKU)),
                (ink('被代位者'), ink('相続人'), ink(ICHIRO)),
                ('', '', ink(SABURO)),
                (ink('申請人兼代位者'), '', ink(JIRO)),
                ('gap',),
                ('line', ink(DAII))]

NOTE = ('※相続証明書は、今は法定相続情報一覧図の写しか法定相続情報番号の提供で代えることもできる（不動産登記規則第37条の3第1項）。'
        '出題当時は法定相続情報番号の制度がなかった')
CSS += ('.tnote { font-size: 17px; color: #444; margin-top: 12px; line-height: 1.6; '
        'font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }')
kansei = page(f'''<div class="page">
<div class="ranno">第3欄</div>
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink(PURPOSE)}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:176px">{ink(ATTACH[0])}<br>{ink(ATTACH[1])}</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink(TAX)}</div></div>
<div class="appbox" style="min-height:260px">{applicant_table(OK_APPLICANT)}</div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="plain">{DATE}</div>
{land_table(ROWS)}
<div class="tnote">{NOTE}</div>
<div class="caption">令和3年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ。添付書類 → 登録免許税 → 申請人の枠 の答案用紙の順） ----
def snippet(attach_html, app_rows, bubble='', good=False):
    g = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return f'''<div class="row"><div class="lab">添　付　書　類</div><div class="box{g}" style="min-height:112px">{attach_html}</div>{chk}</div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:58px">{ink(TAX)}</div></div>
<div class="appbox{g}">{applicant_table(app_rows)}{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble}</span></div>' if bubble else ''}'''


ng_panel = snippet(ink('地積測量図　相続証明書　代理権限証書'),
                   [('center', ink(HISOZOKU)), (ink('相続人'), '', ink(JIRO))])
fix_panel = snippet(
    ink('地積測量図　相続証明書') + '<span class="caret">＜</span><span class="red">代位原因証書</span>'
    + '<br>' + ink('代理権限証書'),
    [('center', ink(HISOZOKU)),
     (f'<span class="red">被代位者</span>', '<span class="red">相続人</span>', f'<span class="red">{ICHIRO}</span>'),
     ('', '', f'<span class="red">{SABURO}</span>'),
     (f'<span class="over"><span class="up">申請人兼代位者</span><span class="ink strike">相続人</span></span>', '',
      ink(JIRO)),
     ('gap',),
     ('line', f'<span class="red">{DAII}</span>')],
    bubble='分筆は亡太郎の相続人3人の立場。二郎1人なら一郎・三郎の分は代位！')
ok_panel = snippet(ink(ATTACH[0]) + '<br>' + ink(ATTACH[1]), OK_APPLICANT, good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">令和3年度 第21問｜二郎1人の申請なら、一郎と三郎の分は代位</div>''')

# ---- 申請書でない解答欄（第1欄・第2欄。2026-10-02追加）----
RAN_CSS = (
    '* { box-sizing: border-box; margin: 0; padding: 0; }'
    'body { background: #fff; width: 1200px; font-family: "Noto Serif CJK JP", "IPAMincho", serif; color: #111; }'
    '.ran { padding: 46px 60px 26px; }'
    '.rt { font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin-bottom: 12px; }'
    'table.rz { width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; }'
    'table.rz td { border: 1.5px solid #111; height: 84px; font-size: 22px; text-align: center; vertical-align: middle; }'
    'table.rz td.head { height: 60px; font-size: 21px; }'
    'table.rz td.diag { background: linear-gradient(to top right, transparent calc(50% - 1px), #111 50%, transparent calc(50% + 1px)); }'
    f'.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; }}'
    '.cap { text-align: center; font-size: 17px; color: #555; margin-top: 22px; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }')


def ran_page(title, table, caption):
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{RAN_CSS}</style></head><body>'
            f'<div class="ran"><div class="rt">{title}</div>{table}<div class="cap">{caption}</div></div></body></html>')


def zahyou_table(rows_):
    """座標の欄。rows_: [(点名, X, Y)]"""
    trs = ''.join(f'<tr><td>{n}</td><td>{ink(x)}</td><td>{ink(y)}</td></tr>' for n, x, y in rows_)
    return ('<table class="rz"><colgroup><col style="width:30%"><col style="width:35%"><col style="width:35%"></colgroup>'
            '<tr><td class="head diag"></td><td class="head">Ｘ座標（m）</td><td class="head">Ｙ座標（m）</td></tr>'
            f'{trs}</table>')


def anaume_table(items):
    """穴埋めの欄。記号と記入欄を2組ずつ横に並べる。items: [(記号, 答え)]"""
    trs = ''
    for k in range(0, len(items), 2):
        pair = items[k:k + 2]
        tds = ''.join(f'<td>{m}</td><td>{ink(a)}</td>' for m, a in pair)
        if len(pair) == 1:
            tds += '<td></td><td></td>'
        trs += f'<tr>{tds}</tr>'
    return ('<table class="rz"><colgroup><col style="width:8%"><col style="width:42%"><col style="width:8%">'
            f'<col style="width:42%"></colgroup>{trs}</table>')


DAI1 = [('Ａ点', '505.93', '495.62'), ('Ｃ点', '499.79', '526.75'), ('Ｈ点', '504.61', '500.55'), ('Ｌ点', '514.27', '521.83')]
DAI2 = [('ア', '登記所'), ('イ', '位置'), ('ウ', '形状'), ('エ', '地番'), ('オ', '閉鎖'), ('カ', '永久')]
dai1 = ran_page('第1欄', zahyou_table(DAI1), '令和3年度 土地家屋調査士試験 第21問 第1欄（問1　Ａ点、Ｃ点、Ｈ点及びＬ点の座標値）解答例')
dai2 = ran_page('第2欄', anaume_table(DAI2), '令和3年度 土地家屋調査士試験 第21問 第2欄（問2　地図に準ずる図面の説明）解答例（イ〜エは順不同）')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 100})
    for name, html in [('R3_dai21mon_toukishinseisho_kansei', kansei), ('R3_dai21mon_toukishinseisho_machigai', machigai),
                       ('R3_dai21mon_dai1ran_kansei', dai1), ('R3_dai21mon_dai2ran_kansei', dai2)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
    browser.close()
