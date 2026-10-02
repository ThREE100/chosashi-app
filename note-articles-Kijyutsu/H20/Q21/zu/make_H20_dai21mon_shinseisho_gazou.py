"""平成20年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H20_dai21mon_toukishinseisho_gazou.md` どおり。縦長（横1200px）。
  項目の順序は試験の答案用紙どおり「登記の目的 → 添付書類 → 申請の日付と提出先 → 項目名のない大きな枠 → 代理人 → 土地の表示 → 土地家屋調査士（職印）」
  答案用紙に登録免許税の欄はないので、大きな枠の最後の行に書く
- 添削　：`../prompt_H20_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 問1・問2の欄（2026-10-02追加）：申請書でない解答欄も答えの直後に置くルールに合わせ、答案用紙（その1）の問1（T101）・問2（B点・E点・F点）の
  座標の欄を、それぞれ別の画像（横1200px、高さは欄に合わせる）にする。欄の形は答案用紙どおり「点名｜X座標｜記入｜Y座標｜記入」の行

必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・Noto Sans CJK JP。なければIPAゴシック）
実行: python3 note-articles-Kijyutsu/H20/Q21/zu/make_H20_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
.page.ran {{ min-height: 0; padding: 40px 70px 30px; }}
.sheet {{ font-size: 22px; color: #333; margin-bottom: 6px; }}
.q {{ font-size: 26px; font-weight: bold; margin: 26px 0 12px; font-family: {SANS}; }}
table.xyrow {{ width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; }}
table.xyrow td {{ border: 1.5px solid #111; font-size: 22px; height: 64px; text-align: center; vertical-align: middle; }}
table.xyrow td.pt {{ width: 9%; }}
table.xyrow td.ax {{ width: 13%; }}
table.xyrow td .ink {{ font-size: 28px; }}
.page .caption {{ margin-top: auto; padding-top: 30px; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 50px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 28px; position: relative; }}
.lab {{ width: 200px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.7; }}
.ink {{ color: {INK}; font-family: {SANS}; }}
.plain {{ font-size: 22px; margin: 4px 0 18px; }}
.dairi {{ display: flex; font-size: 22px; margin: 4px 0 4px; }}
.dairi .lab {{ padding-top: 0; }}
.dairi .addr {{ flex: 1; }}
.dairi .name {{ width: 300px; letter-spacing: 0.5em; }}
.renraku {{ font-size: 20px; margin: 0 0 22px 330px; }}
.appbox {{ border: 2px solid #111; padding: 16px 22px; margin-bottom: 22px; position: relative; }}
table.app {{ border-collapse: collapse; font-size: 23px; line-height: 1.75; }}
table.app td {{ padding: 0; vertical-align: top; white-space: nowrap; }}
table.app td.k {{ width: 232px; }}
table.app td.r {{ width: 96px; }}
table.land {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.land td {{ border: 1.5px solid #111; font-size: 22px; padding: 0 12px; height: 92px; vertical-align: middle; }}
table.land td.head {{ height: 50px; text-align: center; font-size: 20px; }}
table.land td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; white-space: nowrap; }}
table.land td.shozai-lab {{ text-align: center; }}
table.land td.shozai {{ height: 48px; }}
table.land td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 6px; }}
table.land td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 6px; }}
table.land td.chimoku {{ text-align: center; }}
table.land td.cause {{ white-space: normal; }}
table.land tr.last td {{ height: 26px; }}
table.land td .ink {{ font-size: 24px; }}
table.land td.cause .ink {{ font-size: 22px; line-height: 1.45; }}
.shokuin {{ text-align: right; font-size: 22px; margin: 10px 0 0; letter-spacing: 0.3em; }}
.shokuin span {{ border: 1.5px solid #111; padding: 0 4px; letter-spacing: 0; }}
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
.note {{ color: {RED}; font-family: {SANS}; font-size: 18px; font-weight: bold; margin-left: 14px; }}
.caret {{ color: {RED}; font-family: {SANS}; font-weight: bold; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 21px; font-weight: bold; background: #fff5f5; font-family: {SANS};
           line-height: 1.5; }}
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


# ---- 記入データ（prompt_H20_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '平成20年８月24日　　申請　　Ｋ地方法務局'
PURPOSE = '土地分筆登記'
ATTACH = '地積測量図　相続証明書　代位原因証書　代理権限証書'
HISOZOKU = '被代位者（被相続人　西川四郎）'
KAZUKO = 'Ｃ市Ａ町二丁目５番２号　西川和子'
JIRO = 'Ｂ市Ｄ町三丁目１番７号　西川二郎'
HACHIRO = 'Ｂ市Ｄ町四丁目６番１号　西川八郎'
SHICHIRO = 'Ｃ市Ａ町二丁目５番２号　西川七郎'
MINAMINO = 'Ｂ市Ｃ町二丁目３番４号　南野二郎'
DAII = '代位原因　平成19年５月１日売買の所有権移転登記請求権'
TAX = '登録免許税　金2,000円'
SHOZAI = 'Ｋ市Ｂ町一丁目'
ROWS = [('５番', '宅地', '512', '66', ''),
        ('（イ）５番１', '', '300', '79', '①③５番１、５番２に分筆'),
        ('（ロ）５番２', '宅地', '212', '58', '５番から分筆')]


def applicant_table(rows):
    """大きな枠の中身。rows: [(左の見出し, 「相続人」の語, 住所・氏名)] または ('line', 文字) / ('gap',)"""
    h = ['<table class="app">']
    for r in rows:
        if r[0] == 'line':
            h.append(f'<tr><td colspan="3">{r[1]}</td></tr>')
        elif r[0] == 'gap':
            h.append('<tr><td colspan="3" style="height:10px"></td></tr>')
        else:
            h.append(f'<tr><td class="k">{r[0]}</td><td class="r">{r[1]}</td><td>{r[2]}</td></tr>')
    h.append('</table>')
    return ''.join(h)


def land_table(rows, n_rows=3):
    h = ['<table class="land"><colgroup><col style="width:6%"><col style="width:12%"><col style="width:12%">'
         '<col style="width:13%"><col style="width:14%"><col style="width:9%"><col style="width:34%"></colgroup>',
         f'<tr><td class="vert" rowspan="{n_rows + 4}">土地の表示</td>'
         f'<td class="shozai-lab" rowspan="2">所　在</td><td class="shozai" colspan="5">{ink(SHOZAI)}</td></tr>',
         '<tr><td class="shozai" colspan="5"></td></tr>',
         '<tr><td class="head" colspan="2">①地　　番</td><td class="head">②地　　目</td>'
         '<td class="head" colspan="2">③地　　積　m²</td><td class="head">登記原因及びその日付</td></tr>']
    for i in range(n_rows):
        c, m, a, b, g = rows[i] if i < len(rows) else ('', '', '', '', '')
        h.append(f'<tr><td colspan="2">{ink(c)}</td><td class="chimoku">{ink(m)}</td><td class="int">{ink(a)}</td>'
                 f'<td class="dec">{ink(b)}</td><td class="cause">{ink(g)}</td></tr>')
    h.append('<tr class="last"><td colspan="2"></td><td></td><td class="int"></td><td class="dec"></td><td></td></tr>')
    h.append('</table>')
    return ''.join(h)


OK_APPLICANT = [('line', ink(HISOZOKU)),
                ('', ink('相続人'), ink(KAZUKO)),
                ('', '', ink(JIRO)),
                ('', '', ink(HACHIRO)),
                (ink('申請人（代位者）'), '', ink(MINAMINO)),
                ('line', ink(DAII)),
                ('line', ink(TAX))]

kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink(PURPOSE)}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:112px">{ink(ATTACH)}</div></div>
<div class="plain">{DATE}</div>
<div class="appbox" style="min-height:300px">{applicant_table(OK_APPLICANT)}</div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="addr">Ａ市Ｂ町一丁目２番３号</div><div class="name">東田太郎　㊞</div></div>
<div class="renraku">（連絡先　＊＊－＊＊＊＊－＊＊＊＊）</div>
{land_table(ROWS)}
<div class="shokuin">土地家屋調査士　東田太郎　<span>職印</span></div>
<div class="caption">平成20年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ。申請の日付の下の大きな枠だけを取り出す） ----
def snippet(app_rows, bubble='', good=False):
    g = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return f'''<div class="plain">{DATE}</div>
<div class="appbox{g}">{applicant_table(app_rows)}{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble}</span></div>' if bubble else ''}'''


TAIL = [(ink('申請人（代位者）'), '', ink(MINAMINO)), ('line', ink(DAII)), ('line', ink(TAX))]
ng_panel = snippet([('line', ink(HISOZOKU)), ('', ink('相続人'), ink(KAZUKO)), ('', '', ink(SHICHIRO))] + TAIL)
fix_panel = snippet(
    [('line', ink(HISOZOKU)),
     ('', ink('相続人'), ink(KAZUKO)),
     ('', '', f'<span class="ink strike">{SHICHIRO}</span><span class="note">相続の放棄</span>'),
     ('', '<span class="caret">＜</span>', f'<span class="red">{JIRO}</span>'),
     ('', '<span class="caret">＜</span>', f'<span class="red">{HACHIRO}</span>')] + TAIL,
    bubble='七郎は相続の放棄で初めから相続人でない。父母も死亡 → 兄弟姉妹へ。<br>'
           '二郎は父だけ同じでも兄弟、八郎は五郎を代襲（九郎は再代襲しない）')
ok_panel = snippet(OK_APPLICANT, good=True)
# ---- 問1・問2の欄（答案用紙（その1）の座標の欄。記入データはプロンプトどおり） ----
TOI1 = [('T101', '4.04m', '6.43m')]
TOI2 = [('B点', '10.26m', '6.37m'), ('E点', '31.91m', '19.25m'), ('F点', '8.89m', '15.96m')]


def xyrow(rows):
    body = ''.join(f'<tr><td class="pt">{pt}</td><td class="ax">X座標</td><td>{ink(x)}</td><td class="ax">Y座標</td><td>{ink(y)}</td></tr>'
                   for pt, x, y in rows)
    return f'<table class="xyrow">{body}</table>'


def ran(q, body):
    return page(f'''<div class="page ran">
<div class="sheet">第21問答案用紙（その1）</div>
<div class="q">{q}</div>{body}
<div class="caption">平成20年度 土地家屋調査士試験 第21問 答案用紙（その1） {q} 解答例</div>
</div>''')


kansei_toi1 = ran('問1', xyrow(TOI1))
kansei_toi2 = ran('問2', xyrow(TOI2))

machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成20年度 第21問｜七郎は放棄、相続人は和子・二郎・八郎の3人</div>''')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 100})  # 欄だけの画像が引き伸ばされないよう低くする
    for name, html in [('H20_dai21mon_toukishinseisho_kansei_toi1', kansei_toi1), ('H20_dai21mon_toukishinseisho_kansei_toi2', kansei_toi2),
                       ('H20_dai21mon_toukishinseisho_kansei', kansei), ('H20_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（欄だけの画像なら可）'))
    browser.close()
