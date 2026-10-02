"""平成26年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H26_dai21mon_toukishinseisho_gazou.md`（基本フォーム＋記入データ。項目の順序は平成26年度の答案用紙どおり）。縦長（横1200px）
- 添削　：`../prompt_H26_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第1欄・第2欄（問1・問2の座標値）と第3欄（問3の甲区・乙区）：申請書でない解答欄も、答案用紙の欄の形で別の画像にする（横1200px。
  2026-10-02追加。答案用紙はA3横で、左の列に第1欄〜第3欄、右の列に第4欄の登記申請書がある）。記入データは完成形のプロンプトの末尾の節のとおり

様式の部品（CSS・土地の表示の表）は `../../../H28/Q21/zu/make_H28_dai21mon_shinseisho_gazou.py` と同じ。ただし、平成26年度の答案用紙に合わせて
項目の順序（登記の目的 → 添付情報〈（略）〉 → 申請の日付 → 申請人 → 代理人〈（略）〉 → 登録免許税 → 土地の表示）を変え、所在「Ａ市Ｂ町字Ｃ」と
1行目の「100番１」「雑種地」「380」を印刷（黒）にし、土地の表示の表の一番下に地役権設定の範囲を書く横に長い最下欄を加えた。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・Noto Sans CJK JP）
実行: python3 note-articles-Kijyutsu/H26/Q21/zu/make_H26_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
table.land td.saika {{ height: 80px; padding-left: 20px; }}
table.land td.shozai2 {{ height: 44px; }}
table.land td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.land td.shozai-lab {{ text-align: center; height: 76px; }}
table.land td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 6px; }}
table.land td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 6px; }}
table.land td.chimoku {{ text-align: center; }}
.tnote {{ font-size: 17px; color: #444; margin-top: 14px; line-height: 1.6;
          font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 申請書でない解答欄（第1欄〜第3欄） */
.ranpage {{ padding: 50px 70px 30px; }}
.ranhead {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin: 0 0 12px; }}
table.ran {{ width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; margin-bottom: 44px; }}
table.ran td {{ border: 1.5px solid #111; font-size: 22px; height: 64px; text-align: center; vertical-align: middle; }}
table.ran td .ink {{ font-size: 28px; }}
table.ku td.kulab {{ letter-spacing: 1.2em; padding-left: 1.2em; }}
table.ku td.kubody {{ text-align: left; padding: 22px 26px; line-height: 1.75; height: auto; }}
table.ku td.kubody .ink {{ font-size: 24px; }}
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
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.okrow {{ position: relative; }}
.check {{ position: absolute; right: -8px; top: -30px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def land_table(rows, saika='', n_rows=5, compact=False):
    """土地の表示の表（平成26年度の答案用紙どおり：所在は印刷で2行、見出し、記入行、4列を結合した最下欄）。
    rows: [(地番, 地目, 整数部, 小数部, 登記原因)]。各値は HTML（記入部分は呼び出し側で .ink を付ける）"""
    h = [f'<table class="land{" compact" if compact else ""}"><colgroup><col style="width:6%"><col style="width:20%"><col style="width:11%">'
         '<col style="width:13%"><col style="width:7%"><col style="width:43%"></colgroup>',
         '<tr><td class="shozai-lab" colspan="2" rowspan="2">所　在</td><td colspan="4">Ａ市Ｂ町字Ｃ</td></tr>',
         '<tr><td class="shozai2" colspan="4"></td></tr>',
         f'<tr><td class="vert" rowspan="{n_rows + 2}">土地の表示</td><td class="head">①地番</td>'
         '<td class="head">②地目</td><td class="head" colspan="2">③地積</td>'
         '<td class="head">登記原因及びその日付</td></tr>']
    for i in range(n_rows):
        c, m, a, b, g = rows[i] if i < len(rows) else ('', '', '', '', '')
        h.append(f'<tr><td>{c}</td><td class="chimoku">{m}</td><td class="int">{a}</td><td class="dec">{b}</td>'
                 f'<td>{g}</td></tr>')
    h.append(f'<tr><td class="saika" colspan="5">{saika}</td></tr>')
    h.append('</table>')
    return ''.join(h)


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---- 完成形（記入データは prompt_H26_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '平成26年8月22日　申請　Ａ地方法務局'
APPLICANTS = ['Ｂ市Ｋ町213番地　乙野二郎', 'Ｂ市Ｌ三丁目４番５号　甲野明子', 'Ｋ市Ｂ町135番地　山川次郎']
NOTE = ('※申請人：今の法令では、分筆・合筆は共有物の管理として持分の価格の過半数で決められ（民法第251条第1項・第252条第1項）、'
        '過半数の持分を持つ共有者から申請できる。本問は共有者3人とも申請するので3人を書く。出題当時は共有者全員で申請する扱いだった')
SAIKA = '地役権設定の範囲　100番５の土地　南側67平方メートル'
ROWS = [('100番１', '雑種地', '380', '', ''),                        # 1行目は答案用紙に印刷済み（黒）
        (ink('（イ）100番１'), '', ink('314'), '', ink('③100番５に一部合併')),
        (ink('（ロ）'), '', ink('67'), '', ink('100番１から分割して100番５に合併する部分')),
        (ink('100番５'), ink('雑種地'), ink('186'), '', ''),
        (ink('100番５'), '', ink('254'), '', ink('③100番１から一部合併'))]
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('土地分合筆登記')}</div></div>
<div class="dairi"><div class="lab">添　付　情　報</div><div class="ryaku">（略）</div></div>
<div class="plain">{DATE}</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box fix" style="height:150px">{'<br>'.join(ink(a) for a in APPLICANTS)}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink('金2,000円')}</div></div>
<div style="height:6px"></div>
{land_table(ROWS, saika=ink(SAIKA))}
<div class="tnote">{NOTE}</div>
<div class="caption">平成26年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----


def snippet(row5_area, saika, bubbles=(), good=False):
    """答案用紙の順序どおり、土地の表示の所在・見出し・4行目・5行目・最下欄を描く。"""
    chk = CHECK_SVG if good else ''
    rows = [(ink('100番５'), ink('雑種地'), ink('186'), '', ''),
            (ink('100番５'), '', row5_area, '', ink('③100番１から一部合併'))]
    bub = ''.join(f'<div class="bubrow table"><span class="bubble">{b}</span></div>' for b in bubbles)
    return f'''<div class="plain" style="color:#888;font-size:18px">（登記の目的から登録免許税までの欄は省略）</div>
<div class="{'good' if good else ''} okrow" style="position:relative">{land_table(rows, saika=saika, n_rows=2, compact=True)}{chk}</div>
{bub}'''


ng_panel = snippet(ink('253'), '')
fix_panel = snippet(
    f'<span class="red" style="font-size:24px;position:absolute;margin-top:-30px">254</span><span class="ink strike">253</span>',
    f'<span class="red" style="font-size:24px">{SAIKA}</span>',
    bubbles=('186.6334＋67.9542＝254.5876 → 254', '範囲が合筆後の一部なら申請情報に書く！'))
ok_panel = snippet(ink('254'), ink(SAIKA), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成26年度 第21問｜合筆後の100番5は254㎡、地役権設定の範囲も書く</div>''')

# ---- 申請書でない解答欄：第1欄・第2欄（座標値）と第3欄（甲区・乙区）。記入データは完成形のプロンプトの末尾の節のとおり ----
DAI1 = [('Ｐ', '246.09', '183.49')]
DAI2 = [('Ｄ', '240.38', '194.83'), ('Ｅ', '239.31', '179.85'), ('Ｖ', '236.35', '178.39'), ('Ｗ', '236.44', '198.85')]
KOUKU = ['登記の目的　合併による所有権登記', '受付年月日・受付番号　平成26年８月22日第○号',
         '権利者その他の事項　共有者', 'Ｂ市Ｋ町213番地　持分３分の１　乙野二郎', 'Ｂ市Ｌ三丁目４番５号　３分の１　甲野明子',
         'Ｋ市Ｂ町135番地　３分の１　山川次郎']
OTSUKU = ['100番１の乙区１番の地役権の登記（平成20年10月10日', '受付第10000号、要役地　Ａ市Ｂ町字Ｃ102番）を移記し、',
          '地役権設定の範囲（南側67平方メートル）と', '地役権図面番号を記録する']


def zahyo_table(rows):
    h = ['<table class="ran"><colgroup><col style="width:33%"><col style="width:33.5%"><col style="width:33.5%"></colgroup>',
         '<tr><td>点名</td><td>Ｘ座標（ｍ）</td><td>Ｙ座標（ｍ）</td></tr>']
    h += [f'<tr><td>{n}</td><td>{ink(x)}</td><td>{ink(y)}</td></tr>' for n, x, y in rows]
    return ''.join(h) + '</table>'


dai12 = page(f'''<div class="ranpage">
<div class="ranhead">第１欄　点Ｐの座標値</div>
{zahyo_table(DAI1)}
<div class="ranhead">第２欄　Ｄ，Ｅ，Ｖ及びＷの各点の座標値</div>
{zahyo_table(DAI2)}
<div class="caption">平成26年度 土地家屋調査士試験 第21問 第1欄・第2欄（問1・問2）解答例</div>
</div>''')
dai3 = page(f'''<div class="ranpage">
<div class="ranhead">第３欄　甲区及び乙区に記録される事項</div>
<table class="ran ku"><colgroup><col style="width:24%"><col style="width:76%"></colgroup>
<tr><td class="kulab">甲区</td><td class="kubody">{'<br>'.join(ink(v) for v in KOUKU)}</td></tr>
<tr><td class="kulab">乙区</td><td class="kubody">{'<br>'.join(ink(v) for v in OTSUKU)}</td></tr>
</table>
<div class="caption">平成26年度 土地家屋調査士試験 第21問 第3欄（問3）解答例</div>
</div>''')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 200})
    for name, html in [('H26_dai21mon_dai1ran_dai2ran_kansei', dai12), ('H26_dai21mon_dai3ran_kansei', dai3),
                       ('H26_dai21mon_toukishinseisho_kansei', kansei), ('H26_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（欄の画像は横長でよい）'))
    browser.close()
