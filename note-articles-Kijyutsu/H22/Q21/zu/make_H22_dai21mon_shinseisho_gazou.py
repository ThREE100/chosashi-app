"""平成22年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H22_dai21mon_toukishinseisho_gazou.md`（基本フォーム＋記入データ。項目の順序は平成22年度の答案用紙どおり）。縦長（横1200px）
- 添削　：`../prompt_H22_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 問1・問2の欄（2026-10-02追加）：答案用紙（その一）はA3横で、左の列に問1（【結論】【理由】の記述の枠）と問2（C点・D点・K点の座標の表）、
  右の列に問3の申請書がある。申請書でない解答欄も答えの直後に置くルールに合わせ、問1・問2の欄をそれぞれ別の画像（横1200px）にする

様式の部品（CSS・土地の表示の表）は `../../../H23/Q21/zu/make_H23_dai21mon_shinseisho_gazou.py` と同じ。ただし、平成22年度の答案用紙は、
登録免許税・添付書類・代理人が「略」と印刷済みで、申請人の枠に項目名がなく、所在「A市B町二丁目」が印刷済み、土地の表示の記入行は4行、
表の下に「土地家屋調査士　北野一郎　職印」が印刷されている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・IPAゴシック。Noto があればそちらを優先）
実行: python3 note-articles-Kijyutsu/H22/Q21/zu/make_H22_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
.page.ran {{ min-height: 0; padding: 40px 70px 30px; }}
.sheet {{ font-size: 22px; color: #333; margin-bottom: 6px; }}
.q {{ font-size: 26px; font-weight: bold; margin: 26px 0 12px; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.kijutsu {{ border: 2.5px solid #111; padding: 18px 22px 22px; font-size: 22px; }}
.kijutsu .kl {{ margin: 6px 0 6px; }}
.kijutsu .ink {{ font-size: 23px; line-height: 1.75; display: block; margin-bottom: 14px; }}
table.xy {{ border-collapse: collapse; border: 2.5px solid #111; margin-bottom: 18px; table-layout: fixed; width: 640px; }}
table.xy td {{ border: 1.5px solid #111; text-align: center; font-size: 22px; }}
table.xy td.h {{ height: 50px; }}
table.xy td.v {{ height: 82px; }}
table.xy td.v .ink {{ font-size: 28px; }}
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
.note {{ font-size: 17px; color: #444; margin-top: 18px; line-height: 1.6;
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

.shokuin {{ text-align: right; font-size: 22px; margin-top: 14px; }}
.shokuin span.in {{ border: 1.5px solid #111; padding: 0 4px; font-size: 18px; margin-left: 8px; }}
.applicant {{ line-height: 1.75; }}
.applicant .ind {{ padding-left: 1.2em; display: block; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def land_table(rows, n_rows=4, shozai='', compact=False):
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


def applicant(lines, strike=(), add_after=None, red_add=''):
    """申請人の枠の中身。lines: [(字下げするか, 文字)]。strike に入れた行は取消線、add_after の行の下に赤字 red_add を足す。"""
    out = []
    for k, (ind, s) in enumerate(lines):
        cls = 'ind' if ind else ''
        txt = f'<span class="ink{" strike" if k in strike else ""}">{s}</span>'
        out.append(f'<span class="{cls}" style="display:block">{txt}</span>')
        if add_after is not None and k == add_after:
            out.append(f'<span class="ind red" style="display:block;font-size:24px">{red_add}</span>')
    return '<div class="applicant">' + ''.join(out) + '</div>'


# ---- 完成形（記入データは prompt_H22_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '平成22年8月22日申請　Ａ地方法務局'
SHOZAI = 'Ａ市Ｂ町二丁目'
APP_OK = [(False, '申請人（被相続人　杉山太郎）'), (True, '相続人　Ｃ市Ｄ町二丁目５番６号　杉山良子'),
          (True, '上記成年後見人　Ｅ市Ｇ町四丁目２番１号　木村光江'), (True, '相続人　Ｃ市Ｄ町三丁目４番６号　杉山健二')]
ROWS = [('６番２', '宅地', '432', '76', ''),
        ('（Ｂ）', '', '201', '86', '③６番２、６番４に分筆'),
        ('（Ｃ）６番４', '宅地', '230', '91', '６番２から分筆')]
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('土地分筆登記')}</div></div>
<div class="plain">登録免許税　　略</div>
<div class="plain">添　付　書　類　　略</div>
<div class="plain">{DATE}</div>
<div class="row"><div class="box" style="min-height:200px">{applicant(APP_OK)}</div></div>
<div class="plain">代　理　人　　略</div>
{land_table([tuple(ink(v) for v in r) for r in ROWS], shozai=SHOZAI)}
<div class="shokuin">土地家屋調査士　北野一郎<span class="in">職印</span></div>
<div class="caption">平成22年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 問1・問2の欄（答案用紙（その一）の左の列。記入データはプロンプトどおり） ----
TOI1_KETSURON = ('登記所に提出されている地積測量図（平成8年の分筆のときのもの）に記録された道路境界線'
                 '（D点・E点・F点を結ぶ線）を採用すべきである。')
TOI1_RIYUU = ('筆界は、土地が登記された時にその境を構成するものとされた線であり、所有者とA市の協議や道路境界承諾書によって動くものではない。'
              '道路管理図の線（H点・I点・J点を結ぶ線）は、道路拡幅のための用地の予定線であり、その部分の分筆も所有権の移転もされていないので、'
              '登記によって公示された筆界ではない。現地の境界標と平成8年の地積測量図の座標は整合している。')
TOI2 = [('C', '532.49m', '481.86m'), ('D', '534.67m', '500.24m'), ('K', '533.69m', '491.97m')]


def ran(q, body):
    return page(f'''<div class="page ran">
<div class="sheet">第二十一問答案用紙（その一）</div>
<div class="q">{q}</div>{body}
<div class="caption">平成22年度 土地家屋調査士試験 第21問 答案用紙（その一） {q} 解答例</div>
</div>''')


kansei_toi1 = ran('問1', f'''<div class="kijutsu"><div class="kl">【結論】</div>{ink(TOI1_KETSURON)}
<div class="kl">【理由】</div>{ink(TOI1_RIYUU)}</div>''')
kansei_toi2 = ran('問2', ''.join(f'<table class="xy"><tr><td class="h">{p_}点のX座標</td><td class="h">{p_}点のY座標</td></tr>'
                                 f'<tr><td class="v">{ink(x)}</td><td class="v">{ink(y)}</td></tr></table>' for p_, x, y in TOI2))

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ） ----
APP_NG = [(False, '申請人（被相続人　杉山太郎）'), (True, '相続人　Ｃ市Ｄ町二丁目５番６号　杉山良子'),
          (True, '相続人　Ｃ市Ｄ町二丁目５番７号　杉山敏夫'), (True, '相続人　Ｃ市Ｄ町三丁目４番６号　杉山健二'),
          (True, '相続人　Ｃ市Ｄ町一丁目８番１号　田中文子')]


def snippet(app_html, rows, bubble1='', bubble2='', good=False, fix=False):
    """答案用紙の順序（申請人の枠 → 代理人〈省略〉 → 土地の表示）どおりに、申請人の枠と土地の表示の記入行1〜3を描く。"""
    box_cls = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return f'''<div class="row okrow"><div class="box{box_cls}{' fix' if fix else ''}" style="min-height:150px">{app_html}</div>{chk}</div>
{f'<div class="bubrow" style="margin-left:20px"><span class="bubble">{bubble1}</span></div>' if bubble1 else ''}
<div class="plain" style="color:#888;font-size:18px">（代理人の欄は省略）</div>
<div class="{'good' if good else ''}" style="position:relative">{land_table(rows, n_rows=3, shozai=SHOZAI, compact=True)}{chk if good else ''}</div>
{f'<div class="bubrow table"><span class="bubble">{bubble2}</span></div>' if bubble2 else ''}'''


def rows_html(new_no, strike=False, red=''):
    """記入行1〜3。new_no は（Ｃ）の新しい地番。strike なら新しい地番に取消線を引き、red を上に赤で書く。"""
    def no(s):
        if strike:
            return f'<span class="over"><span class="red up">{red}</span><span class="ink strike">{s}</span></span>'
        return ink(s)
    return [(ink('６番２'), ink('宅地'), ink('432'), ink('76'), ''),
            (ink('（Ｂ）'), '', ink('201'), ink('86'), ink('③６番２、') + no(new_no) + ink('に分筆')),
            (ink('（Ｃ）') + no(new_no), ink('宅地'), ink('230'), ink('91'), ink('６番２から分筆'))]


ng_panel = snippet(applicant(APP_NG), rows_html('６番３'))
fix_panel = snippet(applicant(APP_NG, strike=(2, 4), add_after=1, red_add='上記成年後見人　Ｅ市Ｇ町四丁目２番１号　木村光江'),
                    rows_html('６番３', strike=True, red='６番４'),
                    bubble1='申請人は6番2を取得した良子と健二。良子は成年後見人が代表する',
                    bubble2='最終の支号6番3の次は6番4（6番3は使用済み）', fix=True)
ok_panel = snippet(applicant(APP_OK), rows_html('６番４'), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成22年度 第21問｜申請人は6番2を取得した良子（成年後見人）と健二、新しい地番は6番4</div>''')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 100})  # 欄だけの画像が引き伸ばされないよう低くする
    for name, html in [('H22_dai21mon_toukishinseisho_kansei_toi1', kansei_toi1), ('H22_dai21mon_toukishinseisho_kansei_toi2', kansei_toi2),
                       ('H22_dai21mon_toukishinseisho_kansei', kansei), ('H22_dai21mon_toukishinseisho_machigai', machigai)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（欄だけの画像なら可）'))
    browser.close()
