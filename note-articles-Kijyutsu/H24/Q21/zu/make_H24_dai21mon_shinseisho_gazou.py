"""平成24年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H24_dai21mon_toukishinseisho_gazou.md`（基本フォーム＋記入データ。項目の順序は平成24年度の答案用紙どおり）。縦長（横1200px）
- 添削　：`../prompt_H24_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第1欄（問1のK点・L点の座標値）・第3欄（問4の結論と理由）：申請書でない解答欄も、答案用紙の欄の形で別の画像にする（横1200px）。
  欄の形は試験の答案用紙（`public/kijutsu/H24-tochi/a1.webp`）どおり。第1欄は「K点・L点」×「X座標（m）・Y座標（m）」の表、
  第3欄は「結論」の1行と「理由」の罫線（点線）の枠

様式の部品（CSS・土地の表示の表）は `../../../H26/Q21/zu/make_H26_dai21mon_shinseisho_gazou.py` と同じ。平成24年度の答案用紙に合わせて
項目の順序（登記の目的 → 添付書類 → 登録免許税〈「金　円」の間に枠〉 → 申請の日付と提出先〈「平成何年何月何日申請　Ａ地方法務局」と印刷〉
→ 申請人 → 代理人〈（略）〉 → 土地の表示）を変え、所在は2行とも空欄（記入）、記入行5行の下に4列を結合した横に長い欄（今回は空欄）を置いた。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・Noto Sans CJK JP）
実行: python3 note-articles-Kijyutsu/H24/Q21/zu/make_H24_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
.dairi .ryaku {{ padding-left: 20px; }}
.zei {{ display: flex; align-items: center; margin-bottom: 28px; font-size: 22px; }}
.zei .lab {{ padding-top: 0; }}
.zei .kin {{ margin: 0 12px 0 20px; }}
.zei .zbox {{ width: 230px; border: 2px solid #111; padding: 6px 14px; font-size: 26px; text-align: center; }}
.zei .en {{ margin-left: 10px; }}
table.land {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.land td {{ border: 1.5px solid #111; font-size: 22px; padding: 0 12px; height: 92px; vertical-align: middle; }}
table.land.compact td.vert {{ letter-spacing: 0.05em; font-size: 18px; }}
table.land td.head {{ height: 56px; text-align: center; font-size: 20px; }}
table.land td.saika {{ height: 80px; padding-left: 20px; }}
table.land td.shozai {{ height: 52px; }}
table.land td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.land td.shozai-lab {{ text-align: center; }}
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
.redup {{ position: absolute; margin-top: -34px; font-size: 24px; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; left: 60px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: 14px 0 0 300px; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.okrow {{ position: relative; }}
.check {{ position: absolute; right: -8px; top: -30px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def land_table(rows, shozai='', n_rows=5, saika=True, compact=False):
    """土地の表示の表（平成24年度の答案用紙どおり：所在は2行とも記入欄、見出し、記入行5行、4列を結合した最下欄）。
    rows: [(地番, 地目, 整数部, 小数部, 登記原因)]。各値は HTML（記入部分は呼び出し側で .ink を付ける）"""
    h = [f'<table class="land{" compact" if compact else ""}"><colgroup><col style="width:6%"><col style="width:17%"><col style="width:17%">'
         '<col style="width:13%"><col style="width:8%"><col style="width:39%"></colgroup>',
         f'<tr><td class="vert" rowspan="{n_rows + 3 + (1 if saika else 0)}">土地の表示</td>'
         f'<td class="shozai-lab" rowspan="2">所　在</td><td class="shozai" colspan="4">{shozai}</td></tr>',
         '<tr><td class="shozai" colspan="4"></td></tr>',
         '<tr><td class="head">①　地　番</td><td class="head">②　地　目</td><td class="head" colspan="2">③　地　積　㎡</td>'
         '<td class="head">登記原因及びその日付</td></tr>']
    for i in range(n_rows):
        c, m, a, b, g = rows[i] if i < len(rows) else ('', '', '', '', '')
        h.append(f'<tr><td>{c}</td><td class="chimoku">{m}</td><td class="int">{a}</td><td class="dec">{b}</td>'
                 f'<td>{g}</td></tr>')
    if saika:
        h.append('<tr><td class="saika" colspan="5"></td></tr>')
    h.append('</table>')
    return ''.join(h)


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---- 完成形（記入データは prompt_H24_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '平成何年何月何日申請　　Ａ地方法務局'
SHOZAI = 'Ｄ市Ｅ町六丁目'
ROWS = [(ink('5番２'), ink('宅地'), ink('143'), ink('47'), ''),
        (ink('5番３'), ink('宅地'), ink('11'), ink('33'), ink('5番２に合筆')),
        (ink('5番２'), ink('宅地'), ink('154'), ink('80'), ink('③5番３を合筆'))]
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('土地合筆登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:110px">{ink('登記識別情報　印鑑証明書　代理権限証書')}</div></div>
<div class="zei"><div class="lab">登録免許税</div><span class="kin">金</span><span class="zbox">{ink('1,000')}</span><span class="en">円</span></div>
<div class="plain">{DATE}</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:62px">{ink('Ａ市Ｃ町六丁目４番９号　海川二郎')}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div style="height:6px"></div>
{land_table(ROWS, shozai=ink(SHOZAI))}
<div class="caption">平成24年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----


def snippet(rows, bubbles=(), good=False):
    """答案用紙の順序どおり、土地の表示の所在・見出し・記入行1〜3を描く。"""
    chk = CHECK_SVG if good else ''
    bub = ''.join(f'<div class="bubrow"><span class="bubble">{b}</span></div>' for b in bubbles)
    return f'''<div class="plain" style="color:#888;font-size:18px">（登記の目的から代理人までの欄は省略）</div>
<div class="{'good' if good else ''} okrow" style="position:relative">{land_table(rows, shozai=ink(SHOZAI), n_rows=3, saika=False, compact=True)}{chk}</div>
{bub}'''


def fixed(new, old):
    return f'<span class="red redup">{new}</span><span class="ink strike">{old}</span>'


ng_panel = snippet([(ink('5番２'), ink('宅地'), ink('153'), ink('90'), ''),
                    (ink('5番３'), ink('宅地'), ink('11'), ink('33'), ''),
                    (ink('5番２'), ink('宅地'), ink('154'), ink('81'), ink('③5番３を合筆'))])
fix_panel = snippet([(ink('5番２'), ink('宅地'), fixed('143', '153'), fixed('47', '90'), ''),
                     (ink('5番３'), ink('宅地'), ink('11'), ink('33'), '<span class="red" style="font-size:24px">5番２に合筆</span>'),
                     (ink('5番２'), ink('宅地'), ink('154'), fixed('80', '81'), ink('③5番３を合筆'))],
                    bubbles=('1行目はイ（5番4）を分筆した後の 143.47（153.90は平成23年の分筆のとき）',
                             '合筆後は 143.4704＋11.3374＝154.8078 → 154.80（5点で回した154.81ではない）',
                             '合筆される5番3の行に「5番２に合筆」'))
ok_panel = snippet(ROWS, good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成24年度 第21問｜5番2は143.47、合筆後は154.80</div>''')

# ---- 第1欄・第3欄（申請書でない解答欄。2026-10-02追加） ----
RAN_CSS = '''
.ran {{ padding: 60px 60px 40px; }}
.ranhead {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin-bottom: 14px; }}
table.zahyo {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.zahyo td {{ border: 1.5px solid #111; font-size: 24px; height: 96px; text-align: center; vertical-align: middle; }}
table.zahyo tr.h td {{ height: 60px; font-size: 22px; }}
table.zahyo td .ink {{ font-size: 30px; }}
.kekka {{ border: 2px solid #111; }}
.kekka .lab {{ width: auto; font-size: 20px; padding: 6px 0 0 10px; }}
.kekka .ketsu {{ border-bottom: 1.5px dashed #555; padding: 0 20px 10px 70px; font-size: 24px; line-height: 50px; min-height: 64px; }}
.kekka .riyu {{ padding: 0 20px 10px 70px; font-size: 24px; line-height: 50px; min-height: 300px;
                 background-image: repeating-linear-gradient(to bottom, transparent 0, transparent 49px, #999 49px, #999 50px); }}
'''.format()
DAI1 = [('K点', '−8024.35', '−2520.22'), ('L点', '−8033.30', '−2510.33')]
KETSURON = 'お互いの土地の地積を更正する方法による登記の手続をすることはできない。'
RIYU = '地積の更正の登記は、登記記録の地積が筆界に囲まれた土地の実際の面積と相違する場合に、これを正すための登記であり、筆界を変更する登記ではない。5番1の土地と5番2の土地の筆界は、G点、H点及びC点を順次直線で結んだ線であり、公法上の境界である筆界は所有者間の合意によって変更することができないから、地積の更正の登記によってI点、K点及びL点を順次直線で結んだ線を筆界とすることはできない。'


def ran_page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}{RAN_CSS}</style></head><body>{body}</body></html>'


rows1 = ''.join(f'<tr><td>{n}</td><td>{ink(x)}</td><td>{ink(y)}</td></tr>' for n, x, y in DAI1)
dai1 = ran_page(f'''<div class="ran"><div class="ranhead">第１欄</div>
<table class="zahyo"><colgroup><col style="width:30%"><col style="width:35%"><col style="width:35%"></colgroup>
<tr class="h"><td></td><td>Ｘ座標（m）</td><td>Ｙ座標（m）</td></tr>{rows1}</table>
<div class="caption">平成24年度 土地家屋調査士試験 第21問 第1欄（問1）解答例</div></div>''')
dai3 = ran_page(f'''<div class="ran"><div class="ranhead">第３欄</div>
<div class="kekka"><div class="lab">結論</div><div class="ketsu">{ink(KETSURON)}</div>
<div class="lab">理由</div><div class="riyu">{ink(RIYU)}</div></div>
<div class="caption">平成24年度 土地家屋調査士試験 第21問 第3欄（問4）解答例</div></div>''')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 200})
    for name, html in [('H24_dai21mon_dai1ran_kansei', dai1), ('H24_dai21mon_dai3ran_kansei', dai3),
                       ('H24_dai21mon_toukishinseisho_kansei', kansei), ('H24_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（第1欄・第3欄はそれでよい）'))
    browser.close()
