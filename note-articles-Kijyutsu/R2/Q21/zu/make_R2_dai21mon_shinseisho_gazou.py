"""令和2年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_R2_dai21mon_toukishinseisho_gazou.md`（基本フォーム＋記入データ）どおり。縦長（横1200px）。
  R2の答案用紙のとおり、項目の順序は 登記の目的 → 添付書類 → 登録免許税 → 申請人 → 代理人 → 申請の日付と提出先。
  土地の表示は記入行6行で、③地積はすべての行で点線により整数部・小数部に分け、「（略）」の印刷はない
- 添削　：`../prompt_R2_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第1欄（問1のB点・G点・H点）・第3欄（問3のア〜オ）：申請書でない解答欄も、別の画像にする（横1200pxの横長。2026-10-02追加）。
  試験の答案用紙そのものはリポジトリにないので、欄の見出しと記号・記入欄だけの簡素な形（令和6年度の答案用紙の第1欄・第2欄の
  形にならった仮のもの）にしている
- 完成形の表の下に、相続証明書の今の扱い（法定相続情報番号）の注を入れる（2026-10-02追加。記事の本文の注と同じ文言）

見本は `R6/Q21/zu/`・`R7/Q21/zu/` の生成スクリプト（CSSと部品を同じ形にしている）。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・IPAゴシック。Noto があればそちらを優先）
実行: python3 note-articles-Kijyutsu/R2/Q21/zu/make_R2_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 26px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.plain {{ font-size: 22px; margin: 4px 0 26px; }}
.dairi {{ display: flex; font-size: 22px; margin-bottom: 26px; }}
.dairi .lab {{ padding-top: 0; }}
.dairi .ryaku {{ flex: 1; text-align: center; }}
table.land {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.land td {{ border: 1.5px solid #111; font-size: 22px; padding: 0 12px; height: 92px; vertical-align: middle; white-space: nowrap; }}
table.land td.vert {{ white-space: normal; }}
table.land td.head {{ height: 50px; text-align: center; font-size: 20px; }}
table.land td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.land td.shozai-lab {{ text-align: center; height: 76px; }}
table.land td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 6px; }}
table.land td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 6px; }}
table.land td.ryaku {{ text-align: center; }}
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
.bubrow {{ margin: -12px 0 24px 170px; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.okrow {{ position: relative; }}
.check {{ position: absolute; right: -8px; top: -30px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def land_table(rows, n_rows=6, shozai=''):
    """土地の表示の表（R2の答案用紙の形）。rows: [(地番, 地目, 整数部, 小数部, 登記原因)]。すべての行で地積を点線で分ける。"""
    h = ['<table class="land"><colgroup><col style="width:6%"><col style="width:17%"><col style="width:11%">'
         '<col style="width:11%"><col style="width:7%"><col style="width:48%"></colgroup>',
         f'<tr><td class="shozai-lab" colspan="2">所　在</td><td colspan="4">{shozai}</td></tr>',
         f'<tr><td class="vert" rowspan="{n_rows + 1}">土地の表示</td><td class="head">①地　　番</td>'
         '<td class="head">②地　　目</td><td class="head" colspan="2">③地　積　（m²）</td>'
         '<td class="head">登記原因及びその日付</td></tr>']
    for i in range(n_rows):
        c, m, a, b, g = rows[i] if i < len(rows) else ('', '', '', '', '')
        h.append(f'<tr><td>{c}</td><td class="chimoku">{m}</td><td class="int">{a}</td><td class="dec">{b}</td>'
                 f'<td class="cause">{g}</td></tr>')
    h.append('</table>')
    return ''.join(h)


EXTRA_CSS = """
table.land td.cause { white-space: normal; line-height: 1.35; }
table.land td.cause .ink { font-size: 23px; }
"""
CSS = CSS + EXTRA_CSS + """
.tnote { font-size: 17px; color: #444; margin-top: 12px; line-height: 1.6;
         font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }
"""

# ---- 完成形（記入データは prompt_R2_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '令和２年10月18日　申請　Ａ地方法務局'
ATTACH1 = '地積測量図　登記済証　印鑑証明書　相続証明書'
ATTACH2 = '代理権限証書'
APPLICANT = [('', '（被相続人　山川一郎）'),
             ('相続人　', 'Ａ市Ｂ町一丁目32番地４　山川小太郎'),
             ('　　　　', 'Ａ市Ｂ町一丁目32番地５　香川浪子')]
RO_CAUSE = '32番５から分割して32番４に合併する部分'
NOTE = ('※相続証明書は、今は法定相続情報一覧図の写しか法定相続情報番号の提供で代えることもできる（不動産登記規則第37条の3第1項）。'
        '出題当時は法定相続情報番号の制度がなかった')


def rows(i_int, i_dec, g_int, g_dec, red=None):
    """土地の表示の5行。red: {'i': html, 'g': html} で（イ）・合筆後の地積の小数部を差し替える。"""
    red = red or {}
    return [(ink('32番５'), ink('宅地'), ink('140'), ink('80'), ''),
            (ink('（イ）32番５'), '', ink(i_int), red.get('i', ink(i_dec)), ink('③32番４に一部合併')),
            (ink('（ロ）'), '', ink('33'), ink('12'), ink(RO_CAUSE)),
            (ink('32番４'), ink('宅地'), ink('123'), ink('00'), ''),
            (ink('32番４'), '', ink(g_int), red.get('g', ink(g_dec)), ink('③32番５から一部合併'))]


applicant_html = '<br>'.join(f'<span class="ink">{a}{b}</span>' for a, b in APPLICANT)
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('土地分合筆登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:150px">{ink(ATTACH1)}<br>{ink(ATTACH2)}</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink('金2,000円')}</div></div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="min-height:150px">{applicant_html}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="plain">{DATE}</div>
{land_table(rows('107', '73', '156', '12'), shozai=ink('Ａ市Ｂ町一丁目'))}
<div class="tnote">{NOTE}</div>
<div class="caption">令和2年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----
FIXCSS = ('<style>.redfix { color: ' + RED + '; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; '
          'font-size: 24px; margin-left: 8px; }</style>')
ng = land_table(rows('107', '68', '156', '53'), n_rows=5, shozai=ink('Ａ市Ｂ町一丁目'))
fix = land_table(rows('107', '', '156', '',
                      red={'i': '<span class="ink strike">68</span><span class="redfix">73</span>',
                           'g': '<span class="ink strike">53</span><span class="redfix">12</span>'}),
                 n_rows=5, shozai=ink('Ａ市Ｂ町一丁目'))
ok = land_table(rows('107', '73', '156', '12'), n_rows=5, shozai=ink('Ａ市Ｂ町一丁目'))
machigai = page(FIXCSS + f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix}
<div class="bubrow" style="margin:18px 0 10px 0"><span class="bubble">（イ）は分筆後の土地。座標で求めた地積（A・H・G・F）を書く</span></div>
<div class="bubrow" style="margin:28px 0 0 0"><span class="bubble">32番4は地積更正をしていない！登記記録の123.00 ＋ 33.12</span></div></div>
<div class="panel"><div class="ptitle ok">③正解</div><div class="good" style="position:relative">{ok}{CHECK_SVG}</div></div>
<div class="caption" style="margin:10px 0 30px">令和2年度 第21問｜（イ）は座標で求めた107.73、合筆後の32番4は123.00＋33.12＝156.12</div>''')

# ---- 申請書でない解答欄（第1欄・第3欄。2026-10-02追加）----
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
            '<tr><td class="head diag"></td><td class="head">Ｘ座標（ｍ）</td><td class="head">Ｙ座標（ｍ）</td></tr>'
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


DAI1 = [('Ｂ点', '25.18', '5.48'), ('Ｇ点', '14.34', '12.64'), ('Ｈ点', '23.34', '3.64')]
DAI3 = [('ア', '不動産'), ('イ', '登記名義人'), ('ウ', '書面'), ('エ', '合筆'), ('オ', '合併')]
dai1 = ran_page('第1欄　Ｂ点、Ｇ点及びＨ点の座標値', zahyou_table(DAI1), '令和2年度 土地家屋調査士試験 第21問 第1欄（問1）解答例')
dai3 = ran_page('第3欄　登記識別情報の説明（ア〜オ）', anaume_table(DAI3), '令和2年度 土地家屋調査士試験 第21問 第3欄（問3）解答例')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 100})
    for name, html in [('R2_dai21mon_toukishinseisho_kansei', kansei), ('R2_dai21mon_toukishinseisho_machigai', machigai),
                       ('R2_dai21mon_dai1ran_kansei', dai1), ('R2_dai21mon_dai3ran_kansei', dai3)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
    browser.close()
