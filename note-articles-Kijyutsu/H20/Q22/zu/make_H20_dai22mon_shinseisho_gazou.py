"""平成20年度 第22問（建物）登記申請書の画像（完成形・問3の欄・「敷地権の表示」欄の添削）を、
HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_H20_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）。
  試験の答案用紙（その1）（A4縦。登記申請書・一棟の建物の表示・敷地権の目的たる土地の表示）の下に、
  （その2）の区分した建物の表示・敷地権の表示を続けて縦に積む。項目の順序は答案用紙の印刷どおり
  「登記の目的 → 添付書類 → 平成20年８月24日　申請　Ａ地方法務局 → 申請人 → 代理人（印刷済み） → 登録免許税」。
  一棟の建物の表示の②床面積は、整数部｜小数部に分けたセルが左右に2つ（解答例と同じく左のセルに1階〜3階を書く）
- 問3の欄：（その2）の下の問3の欄の完成形
- 添削　：`../prompt_H20_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `R3/Q22/zu/make_R3_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/H20/Q22/zu/make_H20_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.dateline {{ font-size: 22px; margin: 2px 0 22px 0; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 6px; }}
.plainrow .addr {{ flex: 1; padding-left: 120px; }}
.renraku {{ font-size: 20px; margin: 0 0 24px 360px; }}
.taxrow {{ display: flex; align-items: center; font-size: 22px; margin-bottom: 10px; }}
.taxbox {{ width: 220px; border: 2px solid #111; padding: 8px 16px; font-size: 24px; margin: 0 12px; text-align: center; }}
.sign {{ text-align: right; font-size: 21px; margin-top: 10px; }}
.shokuin {{ border: 1.5px solid #111; padding: 0 6px; margin-left: 12px; }}
.sec {{ font-size: 22px; margin: 40px 0 0; color: #555; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 18px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.35em; padding: 0; font-size: 21px; }}
table.t td.lab2 {{ text-align: center; font-size: 18px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 76px; }}
table.t td.val {{ height: 56px; }}
table.t td.entry {{ height: 128px; }}
table.t td.low {{ height: 90px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
.toi3 {{ font-size: 22px; margin: 0 0 14px; }}
.toi3box {{ border: 2px solid #111; padding: 20px 24px; min-height: 240px; font-size: 22px; line-height: 1.8; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 34px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.after {{ font-size: 17px; color: #555; margin-top: 14px; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.dstrike {{ position: relative; }}
.dstrike::before, .dstrike::after {{ content: ""; position: absolute; left: -3px; right: -3px; border-top: 2.5px solid {RED}; }}
.dstrike::before {{ top: 42%; }} .dstrike::after {{ top: 60%; }}
.redfix {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; margin-left: 8px; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5; line-height: 1.5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; left: 330px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: 16px 0 0; }}
.note {{ margin-top: 12px; font-size: 19px; color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; background: #f1faf2; }}
.okwrap {{ position: relative; }}
.check {{ position: absolute; right: -14px; top: -22px; }}
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


ITTOU_KOUZOU = '鉄筋コンクリー<br>ト造合金メッキ<br>鋼板ぶき３階建'
RO_KOUZOU = '鉄筋コンクリート<br>造２階建'
DATE = '平成20年８月24日'

# ---- 一棟の建物の表示（所在は2段、建物の名称は左右2つ、②床面積は左右2つのセル） ----
ITTOU = (
    '<table class="t"><colgroup><col style="width:5%"><col style="width:9%"><col style="width:8%"><col style="width:18%">'
    '<col style="width:7%"><col style="width:17%"><col style="width:7%"><col style="width:29%"></colgroup>'
    '<tr><td class="vert" rowspan="5">一棟の建物の表示</td>'
    f'<td class="lab2" rowspan="2">所在</td><td class="val" colspan="6">{ink("Ａ市Ｃ町六丁目５番地６")}</td></tr>'
    '<tr><td class="val" colspan="5"></td><td class="val"></td></tr>'
    '<tr><td class="lab2 val" colspan="2">建物の名称</td><td class="val" colspan="3"></td><td class="val" colspan="2"></td></tr>'
    '<tr><td class="head" colspan="2">①構　造</td><td class="head" colspan="4">②床　面　積<br>'
    '<span style="display:inline-block;width:48%">m²</span><span style="display:inline-block;width:48%">m²</span></td>'
    '<td class="head">原因及びその日付</td></tr>'
    f'<tr><td class="entry center" colspan="2">{ink(ITTOU_KOUZOU)}</td>'
    f'{area([("1階", "131", "00"), ("2階", "131", "00"), ("3階", "120", "00")])}'
    '<td class="entry int"></td><td class="entry dec"></td><td class="entry genin"></td></tr></table>')

MOKUTEKI = (
    '<table class="t" style="margin-top:0;border-top:none"><colgroup><col style="width:5%"><col style="width:11%">'
    '<col style="width:24%"><col style="width:10%"><col style="width:12%"><col style="width:9%"><col style="width:29%"></colgroup>'
    '<tr><td class="vert" rowspan="5" style="font-size:18px;letter-spacing:0.05em">敷地権の目的たる土地の表示</td>'
    '<td class="head">①土　地<br>の符号</td><td class="head">②所在及び地番</td><td class="head">③地目</td>'
    '<td class="head" colspan="2">④地積<br>m²</td><td class="head">原因及びその日付</td></tr>'
    f'<tr><td class="low center">{ink("１")}</td><td class="low">{ink("Ａ市Ｃ町六丁目<br>５番６")}</td>'
    f'<td class="low center">{ink("宅地")}</td>{area([("", "320", "55")], "low")}<td class="low genin"></td></tr>'
    + ''.join('<tr><td class="low"></td><td class="low"></td><td class="low"></td><td class="low int"></td>'
              '<td class="low dec"></td><td class="low"></td></tr>' for _ in range(3))
    + '</table>')

KUBUN_COLS = ('<colgroup><col style="width:5%"><col style="width:8%"><col style="width:13%"><col style="width:7%">'
              '<col style="width:10%"><col style="width:7%"><col style="width:13%"><col style="width:14%"><col style="width:6%">'
              '<col style="width:17%"></colgroup>')
KUBUN_HEAD = ('<td class="head">不動産<br>番　号</td><td class="head">家屋番号</td><td class="head">建物の<br>名　称</td>'
              '<td class="head" style="font-size:15px">主たる建物<br>又は附属建物</td>'
              '<td class="head">①<br>種類</td><td class="head">②構造</td><td class="head" colspan="2">③床面積<br>m²</td>'
              '<td class="head">原因及び<br>その日付</td>')
RO_ROW = (f'<tr><td class="entry center">（略）</td><td class="entry">{ink("（ロ）<br>Ｃ町六丁目<br>５番６の２")}</td>'
          f'<td class="entry"></td><td class="entry"></td><td class="entry center">{ink("居宅")}</td>'
          f'<td class="entry center">{ink(RO_KOUZOU)}</td>{area([("2階部分", "68", "07"), ("3階部分", "116", "14")])}'
          f'<td class="entry genin">{ink("５番６から区分")}</td></tr>')
EMPTY_KUBUN = ('<tr><td class="low"></td><td class="low"></td><td class="low"></td><td class="low"></td><td class="low"></td>'
               '<td class="low"></td><td class="low int"></td><td class="low dec"></td><td class="low"></td></tr>')
KUBUN = (f'<table class="t">{KUBUN_COLS}<tr><td class="vert" rowspan="5">区分した建物の表示</td>{KUBUN_HEAD}</tr>'
         f'{RO_ROW}{EMPTY_KUBUN * 3}</table>')

SK_COLS = ('<colgroup><col style="width:5%"><col style="width:11%"><col style="width:22%"><col style="width:26%">'
           '<col style="width:36%"></colgroup>')
SK_HEAD = ('<td class="head">①土　地<br>の符号</td><td class="head">②敷地権の種類</td>'
           '<td class="head">③敷地権の割合</td><td class="head">原因及びその日付</td>')


def shikichiken(wariai, good=False, extra=''):
    g = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return (f'<div class="okwrap"><table class="t{g}" style="margin-top:28px">{SK_COLS}'
            f'<tr><td class="vert" rowspan="3">敷地権の表示</td>{SK_HEAD}</tr>'
            f'<tr><td class="low center">{ink("１")}</td><td class="low center">{ink("所有権")}</td>'
            f'<td class="low center">{wariai}</td><td class="low center">{ink(DATE + "敷地権")}</td></tr>'
            '<tr><td class="low"></td><td class="low"></td><td class="low"></td><td class="low"></td></tr>'
            f'<tr><td colspan="5" class="low"></td></tr></table>{chk}</div>{extra}')


kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物区分登記')}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:100px">{ink('建物図面　各階平面図　代理権限証書')}</div></div>
<div class="dateline">平成20年８月24日　　申請　　Ａ地方法務局</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:100px">{ink('Ａ市Ｃ町六丁目２番３号　平野大輔')}</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="addr">Ｂ市Ｄ町五丁目７番４号　　　　山　本　紀　子　㊞</div></div>
<div class="renraku">（連絡先　＊＊－＊＊＊＊－＊＊＊＊）</div>
<div class="taxrow"><div class="lab">登録免許税</div>金<div class="taxbox">{ink('2,000')}</div>円</div>
<div style="height:24px"></div>
{ITTOU}
{MOKUTEKI}
<div class="sign">土地家屋調査士　　山　本　紀　子<span class="shokuin">職印</span></div>
<div class="sec">（ここから答案用紙（その2））</div>
{KUBUN}
{shikichiken(ink('８分の３'))}
<div class="caption">平成20年度 土地家屋調査士試験 第22問 問1 登記申請書 解答例</div>
</div>''')

TOI3 = ('本件土地（５番６）の登記記録の権利部甲区に、平野大輔の持分４分の３が敷地権である旨の登記がされる。'
        'また、権利部乙区の平野大輔の持分についての抵当権の登記（平成19年５月４日受付第13239号）は、'
        '建物の抵当権の登記と登記の目的・受付年月日・受付番号・登記原因及びその日付が同一であるため、職権で抹消される。')
toi3 = page(f'''<div class="page">
<div class="toi3"><b>問３</b>　設問の登記がされると、土地の登記記録にはどのような記録がされるか簡潔に記載しなさい。</div>
<div class="toi3box">{ink(TOI3)}</div>
<div class="caption">平成20年度 土地家屋調査士試験 第22問 問3 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：敷地権の表示の③敷地権の割合 ----
ng_panel = shikichiken(ink('２分の１'))
fix_panel = shikichiken(f'<span class="ink dstrike">２分の１</span><span class="redfix">８分の３</span>',
                        extra=('<div class="bubrow"><span class="bubble">土地は平野大輔４分の３・平野友子４分の１の共有。<br>'
                               '敷地権になるのは大輔の持分４分の３だけ → ４分の３×２分の１＝８分の３</span></div>'
                               '<div class="note">（参考）（イ）部分と（ロ）部分の床面積はどちらも184.21㎡（同じ専有部分の中の壁は引かない）なので、'
                               '床面積の割合は２分の１ずつ</div>'))
ok_panel = shikichiken(ink('８分の３'), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成20年度 第22問｜敷地権の割合は土地全体に対する割合</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 300})
        for name, html in [('H20_dai22mon_toukishinseisho_kansei', kansei),
                           ('H20_dai22mon_toi3_kansei', toi3),
                           ('H20_dai22mon_toukishinseisho_machigai', machigai)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
        browser.close()
