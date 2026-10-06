"""平成27年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H27_dai21mon_toukishinseisho_gazou.md`（基本フォーム＋記入データ）どおり。縦長（横1200px）
- 添削　：`../prompt_H27_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第1欄（問1のA・H・Kの座標値）・第2欄（問2の結論と理由）：申請書でない解答欄も、答案用紙の欄の形で別の画像にする（横1200px。
  2026-10-02追加。答案用紙はA3横で、左の列に第1欄・第2欄、右の列に第3欄の登記申請書がある）。記入データは完成形のプロンプトの末尾の節のとおり
- 見本は `../../../R6/Q21/zu/make_R6_dai21mon_shinseisho_gazou.py`。答案用紙に合わせ、③の項目名を「添付情報」、所在の行を2段にした

必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・IPAゴシック。Noto があればそちらを優先）
実行: python3 note-articles-Kijyutsu/H27/Q21/zu/make_H27_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
table.land td.shozai {{ height: 46px; }}
table.land td.gen {{ font-size: 20px; line-height: 1.45; }}
table.land td.gen .ink {{ font-size: 22px; }}
table.land td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 6px; }}
table.land td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 6px; }}
table.land td.chimoku {{ text-align: center; }}
table.land td .ink, .box .ink {{ font-size: 26px; }}
.tnote {{ font-size: 17px; color: #444; margin-top: 12px; line-height: 1.6;
          font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
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


def land_table(rows, n_rows=5, shozai='Ｂ市Ｃ町一丁目', compact=False, shozai_rows=2):
    """土地の表示の表。rows: [(地番, 地目, 整数部, 小数部, 登記原因)]。各値は HTML（記入部分は呼び出し側で .ink を付ける）。
    shozai_rows=2 なら、答案用紙どおり所在の行を2段にする（2段目は空欄）。"""
    h = [f'<table class="land{" compact" if compact else ""}"><colgroup><col style="width:6%"><col style="width:19%"><col style="width:14%">'
         '<col style="width:12%"><col style="width:6%"><col style="width:43%"></colgroup>',
         f'<tr><td class="shozai-lab" colspan="2" rowspan="{shozai_rows}">所　在</td><td colspan="4" class="shozai">{shozai}</td></tr>']
    h += ['<tr><td colspan="4" class="shozai"></td></tr>'] * (shozai_rows - 1)
    h.append(f'<tr><td class="vert" rowspan="{n_rows + 1}">土地の表示</td><td class="head">①地　　番</td>'
             '<td class="head">②地　　目</td><td class="head" colspan="2">③地　積　（m²）</td>'
             '<td class="head">登記原因及びその日付</td></tr>')
    for i in range(n_rows):
        c, m, a, b, g = rows[i] if i < len(rows) else ('', '', '', '', '')
        h.append(f'<tr><td style="white-space:nowrap;padding:0 6px">{c}</td><td class="chimoku">{m}</td><td class="int">{a}</td><td class="dec">{b}</td>'
                 f'<td class="gen">{g}</td></tr>')
    h.append('</table>')
    return ''.join(h)


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---- 完成形（記入データは prompt_H27_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '平成27年○月○日　申請　○○法務局'
APPLICANT = ['Ｅ県Ｆ市Ｇ町二丁目３番４号', '株式会社山川製菓', '代表取締役　山川一郎']
NOTE = '※添付情報は今の法令による。出題当時は会社法人等番号の制度（平成27年11月施行）がなく、会社法人等番号の代わりに代表者の資格を証する情報（資格証明情報）を付けた'
ROWS = [('100番１', '宅地', '5144', '50', ''),
        ('（イ）', '', '4783', '92', '平成27年７月20日一部地目変更<br>③100番１、100番３に分筆'),
        ('（ロ）100番３', '用悪水路', '361', '', '100番１から分筆')]
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('土地一部地目変更・分筆登記')}</div></div>
<div class="row"><div class="lab">添　付　情　報</div><div class="box" style="height:130px">{ink('地積測量図　会社法人等番号　代理権限証明情報')}</div></div>
<div class="plain">{DATE}</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box fix" style="height:150px">{ink('<br>'.join(APPLICANT))}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink('金2,000円')}</div></div>
<div style="height:14px"></div>
{land_table([tuple(ink(v) for v in r) for r in ROWS], shozai=ink('Ｂ市Ｃ町一丁目'))}
<div class="tnote">{NOTE}</div>
<div class="caption">平成27年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----
WRONG_ADDR = 'Ｂ市Ｃ町一丁目１番２号'
RO = (ink('（ロ）100番３'), ink('用悪水路'), ink('361'))


def snippet(applicant_html, row1, bubble1='', bubble2='', good=False, fix=False, h=150):
    """答案用紙の順序（申請の日付と提出先 → 申請人 → 代理人 → 土地の表示）どおりに、申請人欄と土地の表示の（ロ）の行を描く。"""
    box_cls = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return f'''<div class="plain">{DATE}</div>
<div class="row okrow"><div class="lab">申　　請　　人</div><div class="box fix{box_cls}" style="min-height:{h}px">{applicant_html}</div>{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble1}</span></div>' if bubble1 else ''}
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="{'good' if good else ''}" style="position:relative">{land_table([row1], n_rows=1, shozai=ink('Ｂ市Ｃ町一丁目'), compact=True, shozai_rows=1)}{chk if good else ''}</div>
{f'<div class="bubrow table"><span class="bubble">{bubble2}</span></div>' if bubble2 else ''}'''


ng_panel = snippet(ink(WRONG_ADDR + '<br>株式会社山川製菓'), RO + (ink('37'), ink('100番１から分筆')), h=110)
fix_panel = snippet(
    f'<span class="ink strike">{WRONG_ADDR}</span><br><span class="red">Ｅ県Ｆ市Ｇ町二丁目３番４号</span><br>'
    f'{ink("株式会社山川製菓")}<br><span class="red">代表取締役　山川一郎</span>',
    RO + ('<span class="ink strike">37</span>', ink('100番１から分筆')),
    bubble1='下線は抹消の印。本店移転は付記1号で登記済み！',
    bubble2='用悪水路は1㎡未満を切り捨て。361だけ', fix=True, h=190)
ok_panel = snippet(ink('<br>'.join(APPLICANT)), RO + ('', ink('100番１から分筆')), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成27年度 第21問｜申請人は今の本店と代表者、用悪水路の地積は1㎡未満を切り捨て</div>''')

# ---- 申請書でない解答欄：第1欄（座標値）・第2欄（結論と理由）。記入データは完成形のプロンプトの末尾の節のとおり ----
DAI1 = [('Ａ', '520.40', '465.80'), ('Ｈ', '451.00', '500.00'), ('Ｋ', '473.50', '530.00')]   # 答案用紙の行の順（A・H・K）
KETSURON = '依然として登記の対象となる土地である。'
RIYUU = ['株式会社山川製菓が所有する甲土地の一部を水路としたもので、公有水面となったわけではなく、',
         '引き続き私権の客体となる土地だから。水路となったことは地目（用悪水路）の変更にすぎない',
         '（不動産登記規則第99条）。']   # 改行は入れず、枠の幅で折り返す


def zahyo_table(rows):
    h = ['<table class="ran"><colgroup><col style="width:33%"><col style="width:33.5%"><col style="width:33.5%"></colgroup>',
         '<tr><td>点名</td><td>Ｘ座標（ｍ）</td><td>Ｙ座標（ｍ）</td></tr>']
    h += [f'<tr><td>{n}</td><td>{ink(x)}</td><td>{ink(y)}</td></tr>' for n, x, y in rows]
    return ''.join(h) + '</table>'


dai1 = page(f'''<div class="ranpage">
<div class="ranhead">第１欄　Ａ，Ｈ及びＫの各点の座標値</div>
{zahyo_table(DAI1)}
<div class="caption">平成27年度 土地家屋調査士試験 第21問 第1欄（問1）解答例</div>
</div>''')
dai2 = page(f'''<div class="ranpage">
<div class="ranhead">第２欄</div>
<div class="kijutsu">
<div class="sec"><div class="slab">結論</div>{ink(KETSURON)}</div>
<div class="sec"><div class="slab">理由</div>{ink(''.join(RIYUU))}</div>
</div>
<div class="caption">平成27年度 土地家屋調査士試験 第21問 第2欄（問2）解答例</div>
</div>''')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 200})
    for name, html in [('H27_dai21mon_dai1ran_kansei', dai1), ('H27_dai21mon_dai2ran_kansei', dai2),
                       ('H27_dai21mon_toukishinseisho_kansei', kansei), ('H27_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（欄の画像は横長でよい）'))
    browser.close()
