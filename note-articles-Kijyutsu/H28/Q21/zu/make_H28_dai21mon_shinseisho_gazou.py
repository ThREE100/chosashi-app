"""平成28年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H28_dai21mon_toukishinseisho_gazou.md`（基本フォーム＋記入データ。項目の順序は平成28年度の答案用紙どおり）。縦長（横1200px）
- 添削　：`../prompt_H28_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

様式の部品（CSS・土地の表示の表）は `../../../R6/Q21/zu/make_R6_dai21mon_shinseisho_gazou.py` と同じ。ただし、土地の表示は答案用紙どおり6行で、
「（イ）40番２」が折り返さないよう地番の列を広げ（地番20・地目11）、見出しは答案用紙の印刷どおり「①地番」「②地目」「③地積　m²」にした。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・IPAゴシック。Noto があればそちらを優先）
実行: python3 note-articles-Kijyutsu/H28/Q21/zu/make_H28_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.okrow {{ position: relative; }}
.check {{ position: absolute; right: -8px; top: -30px; }}
/* 申請書でない解答欄（第1欄・第2欄）。2026-10-02追加 */
.ranpage {{ padding: 50px 70px 30px; }}
.ranhead {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin: 0 0 12px; }}
table.ran {{ width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; margin-bottom: 44px; }}
table.ran td {{ border: 1.5px solid #111; font-size: 22px; height: 64px; text-align: center; vertical-align: middle; }}
table.ran td .ink {{ font-size: 28px; }}
.kijutsu {{ border: 2.5px solid #111; margin-bottom: 30px; }}
.kijutsu .sec {{ padding: 14px 22px 22px; }}
.kijutsu .sec + .sec {{ border-top: 1.5px dashed #555; }}
.kijutsu .sec.solid + .sec.solid {{ border-top: 1.5px solid #111; }}
.kijutsu .slab {{ font-size: 20px; margin-bottom: 8px; }}
.kijutsu .ink {{ font-size: 24px; line-height: 1.8; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def land_table(rows, n_rows=6, shozai='Ａ市Ｂ町一丁目', compact=False):
    """土地の表示の表。rows: [(地番, 地目, 整数部, 小数部, 登記原因)]。各値は HTML（記入部分は呼び出し側で .ink を付ける）"""
    h = [f'<table class="land{" compact" if compact else ""}"><colgroup><col style="width:6%"><col style="width:20%"><col style="width:11%">'
         '<col style="width:13%"><col style="width:7%"><col style="width:43%"></colgroup>',
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


# ---- 完成形（記入データは prompt_H28_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '平成28年○月○日　申請　Ａ地方法務局'
APPLICANT = 'Ａ市Ｂ町一丁目16番１号　甲野太郎'
ROWS = [('40番２', '畑', '276', '', ''),
        ('（イ）40番２', '', '230', '', '③32番１に一部合併'),
        ('（ロ）', '', '46', '', '40番２から分割して32番１に合併する部分'),
        ('32番１', '畑', '351', '', ''),
        ('32番１', '', '398', '', '③40番２から一部合併')]
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('土地分合筆登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:130px">{ink('地積測量図　登記識別情報　印鑑証明書　代理権限証書')}</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink('金2,000円')}</div></div>
<div class="plain">{DATE}</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:96px">{ink(APPLICANT)}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div style="height:6px"></div>
{land_table([tuple(ink(v) for v in r) for r in ROWS], shozai=ink('Ａ市Ｂ町一丁目'))}
<div class="caption">平成28年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----


def snippet(tax_html, row5_area, bubble1='', bubble2='', good=False, fix=False):
    """答案用紙の順序（登録免許税 → 申請の日付・申請人・代理人〈省略〉 → 土地の表示）どおりに、登録免許税欄と土地の表示の4・5行目を描く。"""
    box_cls = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    rows = [(ink('32番１'), ink('畑'), ink('351'), '', ''),
            (ink('32番１'), '', row5_area, '', ink('③40番２から一部合併'))]
    return f'''<div class="row okrow"><div class="lab">登録免許税</div><div class="box{box_cls}{' fix' if fix else ''}" style="height:{'96' if fix else '62'}px">{tax_html}</div>{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble1}</span></div>' if bubble1 else ''}
<div class="plain" style="color:#888;font-size:18px">（申請の日付と提出先・申請人・代理人の欄は省略）</div>
<div class="{'good' if good else ''}" style="position:relative">{land_table(rows, n_rows=2, shozai=ink('Ａ市Ｂ町一丁目'), compact=True)}{chk if good else ''}</div>
{f'<div class="bubrow table"><span class="bubble">{bubble2}</span></div>' if bubble2 else ''}'''


ng_panel = snippet(ink('金3,000円'), ink('397'))
fix_panel = snippet(
    f'<span class="ink strike">金3,000円</span>　<span class="red">金2,000円</span>',
    f'<span class="red" style="font-size:24px;position:absolute;margin-top:-30px">398</span><span class="ink strike">397</span>',
    bubble1='分合筆1件なら、分合筆後の2個で2,000円！',
    bubble2='351.67100＋46.4342＝398.1052 → 398', fix=True)
ok_panel = snippet(ink('金2,000円'), ink('398'), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成28年度 第21問｜分合筆は1件で2,000円、合筆後の32番1は398㎡</div>''')

# ---- 申請書でない解答欄：第1欄（座標値）・第2欄（必要となる登記・一の申請情報の可否・理由）。2026-10-02追加 ----
# 記入データは完成形のプロンプトの末尾の節のとおり。答案用紙はA3横で、左の列に第1欄・第2欄、右の列に第3欄の登記申請書がある
DAI1 = [('Ｄ点', '335.61', '306.61'), ('Ｊ点', '346.15', '265.61')]
HITSUYOU = '土地表題登記（（ニ）部分と（ハ）部分を2筆の土地として）'
KAHI = '一の申請情報によって申請することができる。'
RIYUU = ('戊土地は、（ニ）部分が畑、（ハ）部分が宅地で地目が異なるため、2筆の土地として土地表題登記を申請する必要がある。'
         '（ニ）部分の取得原因は時効取得、（ハ）部分の取得原因は売払いと異なるが、土地表題登記の登記原因は土地が生じた原因であり、'
         '2筆ともその登記原因及びその日付は不詳で同一である。同一の登記所の管轄区域内にある2筆の土地について、'
         '登記の目的並びに登記原因及びその日付が同一であるから、一の申請情報によって申請することができる（不動産登記令第4条ただし書）。')


def zahyo_table(rows):
    h = ['<table class="ran"><colgroup><col style="width:33%"><col style="width:33.5%"><col style="width:33.5%"></colgroup>',
         '<tr><td></td><td>Ｘ座標（ｍ）</td><td>Ｙ座標（ｍ）</td></tr>']
    h += [f'<tr><td>{n}</td><td>{ink(x)}</td><td>{ink(y)}</td></tr>' for n, x, y in rows]
    return ''.join(h) + '</table>'


dai1 = page(f'''<div class="ranpage">
<div class="ranhead">第１欄　Ｄ点及びＪ点の座標値</div>
{zahyo_table(DAI1)}
<div class="caption">平成28年度 土地家屋調査士試験 第21問 第1欄（問1）解答例</div>
</div>''')
dai2 = page(f'''<div class="ranpage">
<div class="ranhead">第２欄</div>
<div class="kijutsu">
<div class="sec solid"><div class="slab">必要となる登記</div>{ink(HITSUYOU)}</div>
<div class="sec solid"><div class="slab">一の申請情報によって申請することができるか否か</div>{ink(KAHI)}</div>
<div class="sec solid"><div class="slab">理由</div>{ink(RIYUU)}</div>
</div>
<div class="caption">平成28年度 土地家屋調査士試験 第21問 第2欄（問2）解答例</div>
</div>''')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 200})
    for name, html in [('H28_dai21mon_dai1ran_kansei', dai1), ('H28_dai21mon_dai2ran_kansei', dai2),
                       ('H28_dai21mon_toukishinseisho_kansei', kansei), ('H28_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（欄の画像は横長でよい）'))
    browser.close()
