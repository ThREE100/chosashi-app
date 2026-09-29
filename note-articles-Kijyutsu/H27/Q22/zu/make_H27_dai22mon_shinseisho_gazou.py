"""平成27年度 第22問（建物）答案用紙の画像（第1欄の完成形・第2欄〈登記申請書〉の完成形・「敷地権の表示」欄の添削）を、
HTML＋ヘッドレスブラウザでPNGに書き出す。

- 第1欄　：登記申請に際して必要な手続（問1）の完成形。横1200px
- 完成形（第2欄）：`../prompt_H27_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  試験の答案用紙（A3横。左に第1欄・第2欄の登記の目的〜代理人・区分した建物の表示欄（イ）と敷地権の表示、
  右に区分した建物の表示欄（ロ）と敷地権の表示）の第2欄を、左の列 → 右の列の順に縦に積む。
  項目の順序は答案用紙の印刷どおり「登記の目的 → 添付情報 → 平成27年8月21日　申請　Ａ地方法務局 → 申請人（略） → 代理人（略）」。
  この答案用紙には登録免許税・一棟の建物の表示の欄がないので描かない
- 添削　：`../prompt_H27_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `R3/Q22/zu/make_R3_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/H27/Q22/zu/make_H27_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.page {{ padding: 60px 60px 40px; display: flex; flex-direction: column; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 40px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 24px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.dateline {{ font-size: 22px; margin: 2px 0 10px 0; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 20px; }}
.plainrow .ryaku {{ flex: 1; text-align: center; }}
.sec {{ font-size: 24px; margin: 34px 0 0; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 18px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.35em; padding: 0; font-size: 21px; }}
table.t td.lab2 {{ text-align: center; font-size: 18px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 76px; }}
table.t td.val {{ height: 56px; }}
table.t td.entry {{ height: 128px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
table.r2 td {{ height: 78px; font-size: 21px; }}
table.r2 td .ink {{ font-size: 22px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 34px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.dstrike {{ position: relative; }}
.dstrike::before, .dstrike::after {{ content: ""; position: absolute; left: -3px; right: -3px; border-top: 2.5px solid {RED}; }}
.dstrike::before {{ top: 42%; }} .dstrike::after {{ top: 60%; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5; line-height: 1.5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; right: 120px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: 16px 0 0; text-align: right; }}
.bubrow .bubble {{ text-align: left; }}
.note {{ margin-top: 12px; font-size: 19px; color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; background: #f1faf2; }}
.okwrap {{ position: relative; }}
.check {{ position: absolute; right: -14px; top: -22px; }}
.sub {{ font-size: 20px; margin-top: 4px; }}
.red {{ color: {RED}; font-weight: bold; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.memo {{ margin-top: 14px; font-size: 19px; color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def br(*lines):
    return '<br>'.join(lines)


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def area(floors, cls='entry'):
    """床面積の整数部・小数部のセル。floors: [(階の表示, 整数部, 小数部)]"""
    ints = br(*[ink(f'{k}　{a}' if k else a) for k, a, _ in floors])
    decs = br(*[ink(b) for _, _, b in floors])
    return f'<td class="{cls} int">{ints}</td><td class="{cls} dec">{decs}</td>'


DAI1 = ('本件建物を区分すると、乙山一郎が単独で所有する本件土地の所有権が各専有部分の敷地利用権となり、'
        '専有部分の床面積の割合により専有部分と分離して処分することができなくなる。そこで、区分の登記の申請前に、'
        '公正証書により、専有部分と敷地利用権とを分離して処分することができる旨の規約を設定する必要がある。')

KUBUN_COLS = ('<colgroup><col style="width:5%"><col style="width:13%"><col style="width:8%"><col style="width:9%">'
              '<col style="width:10%"><col style="width:15%"><col style="width:13%"><col style="width:5%">'
              '<col style="width:22%"></colgroup>')
KUBUN_HEAD = ('<td class="head">家屋<br>番号</td><td class="head">建物の<br>名　称</td>'
              '<td class="head" style="font-size:15px">主である<br>建物又は<br>附属建物</td>'
              '<td class="head">①種類</td><td class="head">②構　造</td><td class="head" colspan="2">③床面積　m²</td>'
              '<td class="head">原因及び<br>その日付</td>')
EMPTY_ROW = ('<tr><td class="entry"></td><td class="entry"></td><td class="entry"></td><td class="entry"></td>'
             '<td class="entry"></td><td class="entry int"></td><td class="entry dec"></td><td class="entry"></td></tr>')


def kubun_row(kaoku, kind, kouzou, floors, genin):
    return (f'<tr><td class="entry">{kaoku}</td><td class="entry"></td><td class="entry"></td>'
            f'<td class="entry center">{kind}</td><td class="entry center">{kouzou}</td>{area(floors)}'
            f'<td class="entry genin">{genin}</td></tr>')


ROW_MAE = kubun_row(ink('５番２７'), ink('居宅・<br>共同住宅'), ink('軽量鉄骨造<br>合金メッキ<br>鋼板ぶき<br>３階建'),
                    [('1階', '83', '63'), ('2階', '86', '95'), ('3階', '55', '48')], ink('５番２７の１、<br>５番２７の２に区分'))
ROW_I = kubun_row(ink('（イ）<br>Ｂ町二丁目<br>５番２７の１'), ink('居宅'), ink('軽量鉄骨造<br>３階建'),
                  [('1階部分', '2', '78'), ('2階部分', '83', '97'), ('3階部分', '52', '77')], ink('５番２７から区分'))
ROW_RO = kubun_row(ink('（ロ）<br>Ｂ町二丁目<br>５番２７の２'), ink('共同住宅'), ink('軽量鉄骨造<br>１階建'),
                   [('1階部分', '77', '34')], ink('５番２７から区分'))


def kubun_table(label, r1, r2):
    return (f'<div class="sec">{label}</div>'
            f'<table class="t">{KUBUN_COLS}<tr><td class="vert" rowspan="3">区分した建物の表示</td>{KUBUN_HEAD}</tr>'
            f'{r1}{r2}</table>')


SK_COLS = ('<colgroup><col style="width:5%"><col style="width:20%"><col style="width:22%">'
           '<col style="width:22%"><col style="width:31%"></colgroup>')
SK_HEAD = ('<td class="head">①土地の符号</td><td class="head">②敷地権の種類</td>'
           '<td class="head">③敷地権の割合</td><td class="head">原因及びその日付</td>')


def shikichiken(cells, extra_cls=''):
    tds = ''.join(f'<td class="entry center{extra_cls}">{c}</td>' for c in cells)
    return (f'<table class="t" style="margin-top:28px">{SK_COLS}'
            f'<tr><td class="vert" rowspan="2">敷地権の表示</td>{SK_HEAD}</tr><tr>{tds}</tr></table>')


FUYOU = ['', '', '', ink('記載不要')]

dai1 = page(f'''<div class="page">
<div class="sec" style="margin-top:0">第1欄　登記申請に際して必要な手続</div>
<div class="box" style="margin-top:18px;min-height:210px;line-height:1.9">{ink(DAI1)}</div>
<div class="caption">平成27年度 土地家屋調査士試験 第22問 問1（第1欄）解答例</div>
</div>''')

kansei = page(f'''<div class="page">
<div class="sec" style="margin:0 0 30px">第2欄　平成27年８月21日に申請した登記の申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物区分登記')}</div></div>
<div class="row"><div class="lab">添　付　情　報</div><div class="box" style="height:100px">{ink('建物図面　各階平面図　規約証明情報　代理権限証明情報')}</div></div>
<div class="dateline">平成27年８月21日　申請　Ａ地方法務局</div>
<div class="plainrow"><div class="lab">申　　請　　人</div><div class="ryaku">（略）</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{kubun_table('区分した建物の表示欄（イ）', ROW_MAE, ROW_I)}
{shikichiken(FUYOU)}
<div style="border-top:2px dashed #999;margin:44px 0 0;padding-top:6px;font-size:16px;color:#777;
 font-family:'Noto Sans CJK JP','IPAGothic',sans-serif">（ここから答案用紙の右の列）</div>
{kubun_table('区分した建物の表示欄（ロ）', ROW_RO, EMPTY_ROW)}
{shikichiken(FUYOU)}
<div class="caption">平成27年度 土地家屋調査士試験 第22問 問2 登記申請書（第2欄）解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：敷地権の表示（イ）（ロ） ----
def pair(cells_i, cells_ro, good=False):
    cls = 'class="t good"' if good else 'class="t"'
    chk = CHECK_SVG if good else ''
    t_i = shikichiken(cells_i).replace('class="t"', cls)
    t_ro = shikichiken(cells_ro).replace('class="t"', cls)
    return (f'<div class="okwrap"><div class="sub">敷地権の表示（イ）</div>{t_i}'
            f'<div class="sub" style="margin-top:22px">敷地権の表示（ロ）</div>{t_ro}{chk}</div>')


DATE = '平成27年８月21日'
NG_I = [ink('１'), ink('所有権'), ink('21686分の13952'), ink(DATE + '敷地権')]
NG_RO = [ink('１'), ink('所有権'), ink('21686分の7734'), ink(DATE + '敷地権')]
st = lambda s: f'<span class="ink dstrike">{s}</span>'  # noqa: E731
FIX_I = [st('１'), st('所有権'), st('21686分の13952'), st(DATE + '敷地権') + '<br><span class="red">記載不要</span>']
FIX_RO = [st('１'), st('所有権'), st('21686分の7734'), st(DATE + '敷地権') + '<br><span class="red">記載不要</span>']
ng_panel = pair(NG_I, NG_RO) + ('<div class="memo">藍子のメモ：割合は床面積の割合　（イ）2.78＋83.97＋52.77＝139.52、'
                                '（ロ）77.34、合計216.86</div>')
fix_panel = pair(FIX_I, FIX_RO) + \
    ('<div class="bubrow"><span class="bubble">問1で教示したとおり、公正証書で「専有部分と敷地利用権とを<br>'
     '分離して処分することができる」規約を設定した<br>→ 本件土地の所有権は敷地権にならない → 記載不要（問2のなお書き）</span></div>'
     '<div class="note">床面積の割合で敷地権になるのは、規約がない場合（建物の区分所有等に関する法律第22条第1項本文・第2項・第3項）</div>')
ok_panel = pair(FUYOU, FUYOU, good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成27年度 第22問｜規約があれば敷地権は生じない（記載不要）</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 300})
        for name, html in [('H27_dai22mon_dai1ran_kansei', dai1),
                           ('H27_dai22mon_toukishinseisho_kansei', kansei),
                           ('H27_dai22mon_toukishinseisho_machigai', machigai)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
        browser.close()
