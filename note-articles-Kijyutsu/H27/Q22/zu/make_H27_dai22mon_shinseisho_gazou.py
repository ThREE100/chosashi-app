"""平成27年度 第22問（建物）答案用紙の画像を、HTML＋ヘッドレスブラウザ（Playwright）でPNGに書き出す。

書き出すもの（どれも横1200px）
- H27_dai22mon_dai1ran_kansei        ：第1欄「登記申請に際して必要な手続」（問1）の完成形
- H27_dai22mon_toukishinseisho_kansei：第2欄「平成27年8月21日に申請した登記の申請書」（問2）の完成形。縦長。
    試験の答案用紙（A3横）は、左の列に第1欄・第2欄の登記の目的〜代理人・区分した建物の表示欄（イ）と敷地権の表示、
    右の列に区分した建物の表示欄（ロ）と敷地権の表示が印刷されている。第2欄を左の列 → 右の列の順に縦に積む。
    項目の順序は答案用紙の印刷どおり「登記の目的 → 添付情報 → 平成27年8月21日　申請　Ａ地方法務局 → 申請人（略） → 代理人（略）」。
    この答案用紙には登録免許税・一棟の建物の表示の欄がないので描かない
    （欄の形・名前・順序・印刷文字は試験の答案用紙の実物 ../touan_youshi/H27_dai22mon_touan_youshi.pdf の1ページ目で確かめた。2026-10-02）
- H27_dai22mon_toukishinseisho_machigai：「敷地権の表示」欄の添削。①誤答・②添削・③正解の3コマを縦に積んだ縦長

記入データは `../prompt_H27_dai22mon_toukishinseisho_gazou.md`・`../prompt_H27_dai22mon_toukishinseisho_machigai.md` と同じ。
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
SANS = '"Noto Sans CJK JP", "IPAGothic", sans-serif'
SERIF = '"Noto Serif CJK JP", "IPAMincho", serif'

CSS = f'''
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: #fff; width: 1200px; font-family: {SERIF}; color: #111; }}
.page {{ padding: 56px 60px 40px; }}
.sec {{ font-family: {SANS}; font-weight: bold; font-size: 24px; margin: 34px 0 0; }}
.sec.top {{ margin-top: 0; }}
.row {{ display: flex; align-items: flex-start; margin-top: 22px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 12px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: {SANS}; }}
.printed {{ font-size: 22px; margin-top: 26px; }}
.ryakurow {{ display: flex; font-size: 22px; margin-top: 16px; }}
.ryakurow .lab {{ padding-top: 0; letter-spacing: 0.5em; }}
.subsec {{ font-size: 22px; font-weight: bold; margin: 36px 0 0; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 14px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.3em; padding: 0; font-size: 21px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 72px; }}
table.t td.nw {{ font-size: 15px; white-space: nowrap; padding: 4px; }}
table.t td.entry {{ height: 132px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
table.t td.kaoku {{ padding: 6px; white-space: nowrap; }}
table.t td.kaoku .ink {{ font-size: 17px; }}
table.t td.sk {{ height: 118px; text-align: center; }}
table.sktab td.vert {{ font-size: 19px; letter-spacing: 0.12em; }}
.colbreak {{ border-top: 2px dashed #999; margin: 46px 0 0; padding-top: 6px; font-size: 16px; color: #777;
             font-family: {SANS}; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 32px; font-family: {SANS}; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: {SANS}; font-size: 28px; font-weight: bold; margin-bottom: 14px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.sub {{ font-size: 20px; margin-top: 10px; }}
.dstrike {{ position: relative; }}
.dstrike::before, .dstrike::after {{ content: ""; position: absolute; left: -3px; right: -3px;
                                     border-top: 2.5px solid {RED}; }}
.dstrike::before {{ top: 42%; }} .dstrike::after {{ top: 60%; }}
.red {{ color: {RED}; font-weight: bold; font-family: {SANS}; }}
.bubrow {{ margin: 18px 0 0; text-align: right; }}
.bubble {{ display: inline-block; position: relative; text-align: left; border: 2.5px solid {RED};
           border-radius: 14px; padding: 8px 18px; color: {RED}; font-size: 21px; font-weight: bold;
           background: #fff5f5; line-height: 1.55; font-family: {SANS}; }}
.bubble::before {{ content: ""; position: absolute; top: -17px; right: 150px; border: 8px solid transparent;
                   border-bottom: 9px solid {RED}; }}
.note {{ margin-top: 12px; font-size: 18px; color: {RED}; font-family: {SANS}; }}
.memo {{ margin-top: 14px; font-size: 19px; color: {INK}; font-family: {SANS}; }}
.okwrap {{ position: relative; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; background: #f1faf2; }}
.check {{ position: absolute; right: -16px; top: -18px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" '
             f'fill="#fff" stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" '
             f'stroke="{GREEN}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body>{body}</body></html>')


# ---- 記入データ（プロンプトと同じ） ----
DAI1 = ('本件建物を区分すると、乙山一郎が単独で所有する本件土地の所有権が各専有部分の敷地利用権となり、'
        '専有部分の床面積の割合により専有部分と分離して処分することができなくなる。そこで、区分の登記の申請前に、'
        '公正証書により、専有部分と敷地利用権とを分離して処分することができる旨の規約を設定する必要がある。')
MOKUTEKI = '建物区分登記'
TENPU = '建物図面　各階平面図　規約証明情報　代理権限証明情報'
DATE = '平成27年８月21日'

# 区分した建物の表示：（家屋番号, 種類, 構造, [(階, 整数部, 小数部)], 原因及びその日付）
MAE = ('５番２７', '居宅・<br>共同住宅', '軽量鉄骨造<br>合金メッキ<br>鋼板ぶき<br>３階建',
       [('1階', '83', '63'), ('2階', '86', '95'), ('3階', '55', '48')], '５番２７の１、<br>５番２７の２に区分')
I_ROW = ('（イ）<br>Ｂ町二丁目<br>５番２７の１', '居宅', '軽量鉄骨造<br>３階建',
         [('1階部分', '2', '78'), ('2階部分', '83', '97'), ('3階部分', '52', '77')], '５番２７から区分')
RO_ROW = ('（ロ）<br>Ｂ町二丁目<br>５番２７の２', '共同住宅', '軽量鉄骨造<br>１階建',
          [('1階部分', '77', '34')], '５番２７から区分')
SK_FUYOU = ['', '', '', '記載不要']          # ①土地の符号・②敷地権の種類・③敷地権の割合・原因及びその日付
SK_NG_I = ['１', '所有権', '21686分の13952', DATE + '敷地権']
SK_NG_RO = ['１', '所有権', '21686分の7734', DATE + '敷地権']

# ---- 区分した建物の表示の表（答案用紙の列の順：家屋番号・建物の名称・主である建物又は附属建物・①種類・②構造・③床面積・原因及びその日付） ----
KUBUN_COLS = ('<colgroup><col style="width:5%"><col style="width:12%"><col style="width:9%"><col style="width:10%">'
              '<col style="width:11%"><col style="width:11%"><col style="width:14%"><col style="width:5%">'
              '<col style="width:23%"></colgroup>')
KUBUN_HEAD = ('<td class="head">家屋<br>番号</td><td class="head nw">建物の名称</td>'
              '<td class="head nw">主である建物<br>又は附属建物</td>'
              '<td class="head">①種類</td><td class="head">②構造</td>'
              '<td class="head" colspan="2">③床面積　m²</td><td class="head">原因及び<br>その日付</td>')


def kubun_tr(row):
    if row is None:
        return ('<tr>' + '<td class="entry"></td>' * 5 + '<td class="entry int"></td><td class="entry dec"></td>'
                '<td class="entry"></td></tr>')
    kaoku, kind, kouzou, floors, genin = row
    ints = '<br>'.join(ink(f'{k}　{a}') for k, a, _ in floors)
    decs = '<br>'.join(ink(b) for _, _, b in floors)
    return (f'<tr><td class="entry kaoku">{ink(kaoku)}</td><td class="entry"></td><td class="entry"></td>'
            f'<td class="entry center">{ink(kind)}</td><td class="entry center">{ink(kouzou)}</td>'
            f'<td class="entry int">{ints}</td><td class="entry dec">{decs}</td>'
            f'<td class="entry genin">{ink(genin)}</td></tr>')


def kubun_table(label, r1, r2):
    return (f'<div class="subsec">{label}</div>'
            f'<table class="t">{KUBUN_COLS}<tr><td class="vert" rowspan="3">区分した建物の表示</td>{KUBUN_HEAD}</tr>'
            f'{kubun_tr(r1)}{kubun_tr(r2)}</table>')


SK_COLS = ('<colgroup><col style="width:5%"><col style="width:22%"><col style="width:22%">'
           '<col style="width:22%"><col style="width:29%"></colgroup>')
SK_HEAD = ('<td class="head">①土地の符号</td><td class="head">②敷地権の種類</td>'
           '<td class="head">③敷地権の割合</td><td class="head">原因及びその日付</td>')


def shikichiken(cells, table_cls='t', raw=False):
    tds = ''.join(f'<td class="sk">{c if raw else ink(c)}</td>' for c in cells)
    return (f'<table class="{table_cls} sktab" style="margin-top:24px">{SK_COLS}'
            f'<tr><td class="vert" rowspan="2">敷地権の表示</td>{SK_HEAD}</tr><tr>{tds}</tr></table>')


# ---- 第1欄 ----
dai1 = page(f'''<div class="page">
<div class="sec top">第1欄　登記申請に際して必要な手続</div>
<div class="box" style="margin-top:18px;min-height:220px;line-height:1.9">{ink(DAI1)}</div>
<div class="caption">平成27年度 土地家屋調査士試験 第22問 問1（第1欄）の完成形</div>
</div>''')

# ---- 第2欄（左の列 → 右の列） ----
kansei = page(f'''<div class="page">
<div class="sec top">第2欄　平成27年８月21日に申請した登記の申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink(MOKUTEKI)}</div></div>
<div class="row"><div class="lab">添　付　情　報</div><div class="box" style="height:104px">{ink(TENPU)}</div></div>
<div class="printed">{DATE}　申請　Ａ地方法務局</div>
<div class="ryakurow"><div class="lab">申請人</div><div>（略）</div></div>
<div class="ryakurow"><div class="lab">代理人</div><div>（略）</div></div>
{kubun_table('区分した建物の表示欄（イ）', MAE, I_ROW)}
{shikichiken(SK_FUYOU)}
<div class="colbreak">（ここから答案用紙の右の列）</div>
{kubun_table('区分した建物の表示欄（ロ）', RO_ROW, None)}
{shikichiken(SK_FUYOU)}
<div class="caption">平成27年度 土地家屋調査士試験 第22問 問2 登記申請書（第2欄）の完成形</div>
</div>''')


# ---- 添削：①誤答 → ②添削 → ③正解（敷地権の表示（イ）（ロ）を縦に並べる） ----
def strike(s):
    return f'<span class="ink dstrike">{s}</span>'


def two_tables(cells_i, cells_ro, good=False, raw=False):
    cls = 't good' if good else 't'
    body = (f'<div class="sub">区分した建物の表示欄（イ）の敷地権の表示</div>{shikichiken(cells_i, cls, raw)}'
            f'<div class="sub" style="margin-top:22px">区分した建物の表示欄（ロ）の敷地権の表示</div>'
            f'{shikichiken(cells_ro, cls, raw)}')
    return f'<div class="okwrap">{body}{CHECK_SVG if good else ""}</div>'


def fixed(cells):
    out = [strike(c) for c in cells]
    out[3] += '<br><span class="red">記載不要</span>'
    return out


ng = two_tables(SK_NG_I, SK_NG_RO) + \
    ('<div class="memo">藍子のメモ：割合は床面積の割合で（イ）2.78＋83.97＋52.77＝139.52、'
     '（ロ）77.34、合計216.86</div>')
fix = two_tables(fixed(SK_NG_I), fixed(SK_NG_RO), raw=True) + \
    ('<div class="bubrow"><span class="bubble">問1のとおり、区分の前に公正証書で<br>'
     '「専有部分と敷地利用権とを分離して処分することができる」規約を設定した<br>'
     '→ 本件土地の所有権は敷地権にならない → 原因及びその日付の欄に「記載不要」</span></div>'
     '<div class="note">床面積の割合で敷地権になるのは、規約で別段の定めをしない場合'
     '（建物の区分所有等に関する法律第22条第1項・第2項・第3項）</div>')
ok = two_tables(SK_FUYOU, SK_FUYOU, good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok}</div>
<div class="caption" style="margin:8px 0 30px">平成27年度 第22問｜規約があれば敷地権は生じない（記載不要）</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 300})
        for name, html in [('H27_dai22mon_dai1ran_kansei', dai1),
                           ('H27_dai22mon_toukishinseisho_kansei', kansei),
                           ('H27_dai22mon_toukishinseisho_machigai', machigai)]:
            with open(os.path.join(OUT, name + '.html'), 'w', encoding='utf-8') as f:
                f.write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
        browser.close()
