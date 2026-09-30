"""平成23年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H23_dai21mon_toukishinseisho_gazou.md`（基本フォーム＋記入データ。項目の順序は平成23年度の答案用紙どおり）。縦長（横1200px）
- 添削　：`../prompt_H23_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

様式の部品（CSS・土地の表示の表）は `../../../H28/Q21/zu/make_H28_dai21mon_shinseisho_gazou.py` と同じ。ただし、平成23年度の答案用紙には
登録免許税の欄がなく、申請の日付と提出先（平成23年8月21日申請　Ａ地方法務局）と代理人（氏名・住所・電話番号）が印刷済みで、
土地の表示の記入行は3行。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・IPAゴシック。Noto があればそちらを優先）
実行: python3 note-articles-Kijyutsu/H23/Q21/zu/make_H23_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
.dairi {{ display: flex; font-size: 22px; margin-bottom: 30px; }}
.dairi .lab {{ padding-top: 0; }}
.dairi .txt {{ flex: 1; line-height: 1.6; }}
table.land {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.land td {{ border: 1.5px solid #111; font-size: 22px; padding: 0 12px; height: 92px; vertical-align: middle; }}
table.land.compact td.vert {{ letter-spacing: 0.02em; font-size: 15px; }}
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
.over {{ position: relative; display: inline-block; }}
.item {{ display: inline-block; white-space: nowrap; margin-right: 0.9em; }}
.over .up {{ position: absolute; left: 0; top: -30px; font-size: 24px; white-space: nowrap; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; left: 60px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: -12px 0 20px 170px; }}
.bubrow.table {{ margin: 14px 0 0 200px; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.okrow {{ position: relative; }}
.check {{ position: absolute; right: -8px; top: -30px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def land_table(rows, n_rows=3, shozai='', compact=False):
    """土地の表示の表。rows: [(地番, 地目, 整数部, 小数部, 登記原因)]。各値は HTML（記入部分は呼び出し側で .ink を付ける）"""
    h = [f'<table class="land{" compact" if compact else ""}"><colgroup><col style="width:6%"><col style="width:18%"><col style="width:15%">'
         '<col style="width:13%"><col style="width:7%"><col style="width:41%"></colgroup>',
         f'<tr><td class="shozai-lab" colspan="2">所　在</td><td colspan="4">{shozai}</td></tr>',
         f'<tr><td class="vert" rowspan="{n_rows + 1}">土地の表示</td><td class="head">①地番</td>'
         '<td class="head">②地目</td><td class="head" colspan="2">③地積　　m²</td>'
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


# ---- 完成形（記入データは prompt_H23_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '平成23年8月21日申請　Ａ地方法務局'
TENPU = '土地所在図　地積測量図　所有権証明書　住所証明書　代理権限証書'
APPLICANT = 'Ａ市Ｂ町五丁目50番地１　宗教法人雨堤天満宮<br>代表役員　荒牧英雄'
DAIRI = 'Ａ市Ｂ町三丁目１番２号　土地家屋調査士　中村　容子　㊞<br>連絡先の電話番号　×××−×××−××××'
SHOZAI = 'Ａ市Ｂ町五丁目'
ROWS = [('', '境内地', '113', '', '不詳')]
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('土地表題登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:150px">{ink(TENPU)}</div></div>
<div class="plain">{DATE}</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:130px">{ink(APPLICANT)}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="txt">{DAIRI}</div></div>
<div style="height:6px"></div>
{land_table([tuple(ink(v) for v in r) for r in ROWS], shozai=ink(SHOZAI))}
<div class="caption">平成23年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----


def snippet(tenpu_html, chimoku, dec, genin, bubble1='', bubble2='', good=False, fix=False):
    """答案用紙の順序（添付書類 → 申請の日付・申請人・代理人〈省略〉 → 土地の表示）どおりに、添付書類欄と土地の表示の記入行1を描く。"""
    box_cls = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    rows = [('', chimoku, ink('113'), dec, genin)]
    return f'''<div class="row okrow"><div class="lab">添　付　書　類</div><div class="box{box_cls}{' fix' if fix else ''}" style="min-height:110px">{tenpu_html}</div>{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble1}</span></div>' if bubble1 else ''}
<div class="plain" style="color:#888;font-size:18px">（申請の日付と提出先・申請人・代理人の欄は省略）</div>
<div class="{'good' if good else ''}" style="position:relative">{land_table(rows, n_rows=1, shozai=ink(SHOZAI), compact=True)}{chk if good else ''}</div>
{f'<div class="bubrow table"><span class="bubble">{bubble2}</span></div>' if bubble2 else ''}'''


NG_TENPU = '土地所在図　地積測量図　所有権証明書　住所証明書　資格証明書　代理権限証書'


def items(s, strike=()):
    """添付書類を書類ごとの塊にして、書類名の途中で折り返さないようにする。strike に入れた書類には取消線。"""
    return ''.join(f'<span class="item"><span class="ink{" strike" if t in strike else ""}">{t}</span></span>' for t in s.split('　'))


ng_panel = snippet(items(NG_TENPU), ink('宅地'), ink('87'), ink('昭和26年8月19日時効取得'))
fix_panel = snippet(
    items(NG_TENPU, strike=('資格証明書',)),
    '<span class="over"><span class="red up">境内地</span><span class="ink strike">宅地</span></span>',
    '<span class="ink strike">87</span>',
    '<span class="over"><span class="red up">不詳</span><span class="ink strike">昭和26年8月19日時効取得</span></span>',
    bubble1='問題文の注5：登記所が同一なので資格証明書は不要',
    bubble2='境内地は1㎡未満切捨て、原因は土地が生じた原因の不詳', fix=True)
ok_panel = snippet(ink(TENPU), ink('境内地'), '', ink('不詳'), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成23年度 第21問｜資格証明書は注5で不要、境内地113㎡、原因は不詳</div>''')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 800})
    for name, html in [('H23_dai21mon_toukishinseisho_kansei', kansei), ('H23_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（要確認）'))
    browser.close()
