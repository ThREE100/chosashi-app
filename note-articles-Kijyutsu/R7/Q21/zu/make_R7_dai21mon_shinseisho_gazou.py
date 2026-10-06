"""令和7年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_R7_dai21mon_toukishinseisho_gazou.md`（基本フォーム＋記入データ）どおり。縦長（横1200px）。
  答案用紙のとおり、土地の表示の記入行2〜5の③地積は4行を結合したセルで、印刷の「（略）」が入る
- 添削　：`../prompt_R7_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第2欄（問2のア〜カ）：申請書でない解答欄も、試験の答案用紙（`public/kijutsu/R07-tochi/a1.png`）の第2欄の形
  （「ア｜イ」「ウ｜エ」「オ｜カ」の3行）で別の画像にする（横1200pxの横長。2026-10-02追加）

見本は `R6/Q21/zu/make_R6_dai21mon_shinseisho_gazou.py`（CSSと部品を同じ形にしている）。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・IPAゴシック。Noto があればそちらを優先）
実行: python3 note-articles-Kijyutsu/R7/Q21/zu/make_R7_dai21mon_shinseisho_gazou.py [出力フォルダ]
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


def land_table(row1, rows_rest, shozai):
    """土地の表示の表（R7の答案用紙の形）。記入行1は地積を点線で整数部・小数部に分け、記入行2〜5の③地積は
    4行を結合したセルに印刷の「（略）」を入れる。row1: (地番, 地目, 整数部, 小数部, 登記原因)、
    rows_rest: [(地番, 地目, 登記原因)] × 4"""
    h = ['<table class="land"><colgroup><col style="width:6%"><col style="width:20%"><col style="width:12%">'
         '<col style="width:12%"><col style="width:7%"><col style="width:43%"></colgroup>',
         f'<tr><td class="shozai-lab" colspan="2">所　在</td><td colspan="4">{shozai}</td></tr>',
         '<tr><td class="vert" rowspan="6">土地の表示</td><td class="head">①地　　番</td>'
         '<td class="head">②地　　目</td><td class="head" colspan="2">③地　積　（m²）</td>'
         '<td class="head">登記原因及びその日付</td></tr>']
    c, m, a, b, g = row1
    h.append(f'<tr><td>{c}</td><td class="chimoku">{m}</td><td class="int">{a}</td><td class="dec">{b}</td><td>{g}</td></tr>')
    for i, (c, m, g) in enumerate(rows_rest):
        ryaku = '<td class="ryaku" colspan="2" rowspan="4">（略）</td>' if i == 0 else ''
        h.append(f'<tr><td>{c}</td><td class="chimoku">{m}</td>{ryaku}<td>{g}</td></tr>')
    h.append('</table>')
    return ''.join(h)


# ---- 完成形（記入データは prompt_R7_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '令和７年10月30日　申請　Ｓ地方法務局'
APPLICANT = 'Ｓ市Ｔ町一丁目10番１号　甲野一郎'
ATTACH = '地積測量図　代理権限証書'
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('土地分筆登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:170px">{ink(ATTACH)}</div></div>
<div class="plain">{DATE}</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:62px">{ink(APPLICANT)}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink('金2,000円')}</div></div>
<div style="height:14px"></div>
{land_table((ink('10番１'), ink('宅地'), ink('280'), ink('59'), ''),
            [(ink('（イ）'), '', ink('③10番１、10番３に分筆')),
             (ink('（ロ）10番３'), ink('宅地'), ink('10番１から分筆')),
             ('', '', ''), ('', '', '')], ink('Ｓ市Ｔ町一丁目'))}
<div class="caption">令和7年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----
OLD_ADDR = 'Ｓ市Ｍ町二丁目３番５号'
NEW_ADDR = 'Ｓ市Ｔ町一丁目10番１号'
EXTRA = '住所証明情報'


def snippet(attach_html, applicant_html, bubble1='', bubble2='', good=False):
    """答案用紙の順序（添付書類 → 申請の日付と提出先 → 申請人）どおりに描く。"""
    g = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return f'''<div class="row okrow"><div class="lab">添　付　書　類</div><div class="box{g}" style="min-height:84px">{attach_html}</div>{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble1}</span></div>' if bubble1 else ''}
<div class="plain">{DATE}</div>
<div class="row okrow"><div class="lab">申　　請　　人</div><div class="box{g}" style="min-height:62px">{applicant_html}</div>{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble2}</span></div>' if bubble2 else ''}'''


ng_panel = snippet(ink(f'{ATTACH}　{EXTRA}'), ink(f'{OLD_ADDR}　甲野一郎'))
fix_panel = snippet(
    f'{ink(ATTACH)}<span class="ink">　</span><span class="ink strike">{EXTRA}</span>',
    f'<span class="ink strike">{OLD_ADDR}</span><span class="ink">　甲野一郎</span><br><span class="red">{NEW_ADDR}</span>',
    bubble1='登記記録の住所と一致するので、住所の証明は要らない',
    bubble2='10月20日に住所変更登記が完了済み！登記記録の住所はもう新住所')
ok_panel = snippet(ink(ATTACH), ink(APPLICANT), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">令和7年度 第21問｜申請人の住所は、申請の日の登記記録の住所</div>''')

# ---- 第2欄（申請書でない解答欄。2026-10-02追加） ----
RAN_CSS = '''
.ranpage { padding: 50px 60px 34px; }
.ranhead { font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin: 0 0 14px; }
table.ran { width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; }
table.ran td { border: 1.5px solid #111; height: 84px; font-size: 22px; vertical-align: middle; }
table.ran td.k { text-align: center; }
table.ran td.v { padding-left: 22px; }
table.ran td.v .ink { font-size: 28px; }
'''
DAI2 = [('ア', '280.59'), ('イ', '2.32'), ('ウ', '超えています'), ('エ', '錯誤'), ('オ', '土地の地積の更正'),
        ('カ', '必要があります')]
trs = ''.join('<tr>' + ''.join(f'<td class="k">{k}</td><td class="v">{ink(v)}</td>' for k, v in DAI2[i:i + 2]) + '</tr>'
              for i in range(0, len(DAI2), 2))
dai2 = (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}{RAN_CSS}</style></head><body>'
        f'<div class="ranpage"><div class="ranhead">第2欄</div><table class="ran"><colgroup><col style="width:9%">'
        f'<col style="width:41%"><col style="width:9%"><col style="width:41%"></colgroup>{trs}</table>'
        f'<div class="caption">令和7年度 土地家屋調査士試験 第21問 第2欄（問2）解答例</div></div></body></html>')


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


dai1 = zahyou('第1欄', [('Ｄ点', '201.71', '114.41'), ('Ｋ点', '199.98', '131.88')],
               '令和7年度 土地家屋調査士試験 第21問 第1欄（問1）解答例')
dai4 = zahyou('第4欄', [('Ｊ点', '216.07', '116.94'), ('Ｌ点', '203.64', '131.88')],
               '令和7年度 土地家屋調査士試験 第21問 第4欄（問4）解答例')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 200})
    for name, html in [('R7_dai21mon_dai1ran_kansei', dai1), ('R7_dai21mon_dai2ran_kansei', dai2), ('R7_dai21mon_dai4ran_kansei', dai4), ('R7_dai21mon_toukishinseisho_kansei', kansei),
                       ('R7_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
    browser.close()
