"""平成25年度 第22問（建物）の答案用紙の画像（第1欄・第2欄の登記申請書の完成形、第3欄の説明の完成形、添削）を、
HTML＋ヘッドレスブラウザでPNGに書き出す。

- 第1欄・第2欄：`../prompt_H25_dai22mon_toukishinseisho_gazou.md` の画像1・画像2の記入データどおり。縦長（横1200px）。
  答案用紙（`public/kijutsu/H25-tatemono/a1.webp`、試験の答案用紙）はA3横で、左の列に第1欄、右の列に第2欄と第3欄がある。
  第1欄と第2欄は記事の別々の問（問1・問2）の答えなので、欄ごとに別の画像にし、それぞれの答えの直後に置く。
  欄の形は試験の答案用紙どおり：見出し（本件旧建物／本件新建物に関する登記の申請書）、登記の目的、添付情報、
  申請の日付と提出先（平成25年8月23日申請　C地方法務局。印刷済み）、申請人、代理人（略）。登録免許税の欄はない。
  表は、不動産番号、建物の表示（所在2段〈上段1枠・下段は左右2枠〉、家屋番号〈左右2枠〉、見出し、記入行3行）
- 第3欄　　　：同じく画像3どおり。「土地家屋調査士民事花子の説明」の大きな枠（申請書ではない解答欄なので別の画像）
- 添削　　　：`../prompt_H25_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）

CSSと部品の作りは `H29/Q22/zu/make_H29_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/H25/Q22/zu/make_H25_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.page {{ padding: 50px 60px 40px; display: flex; flex-direction: column; }}
.head1 {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin: 0 0 30px; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 22px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.dateline {{ font-size: 22px; margin: 0 0 22px 10px; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 20px; }}
.plainrow .ryaku {{ margin-left: 40px; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 14px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 1.0em; padding: 0; font-size: 21px; }}
table.t td.lab2 {{ text-align: center; font-size: 19px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 76px; }}
table.t td.val {{ height: 56px; }}
table.t td.entry {{ height: 132px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
table.t td.genin .ink {{ font-size: 18px; }}
.setsumei {{ border: 3px solid #111; min-height: 420px; padding: 24px 28px; font-size: 25px; line-height: 1.9;
             text-indent: 1em; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 30px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 18px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.sub {{ font-size: 20px; margin-bottom: 12px; }}
table.s {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.s td {{ border: 1.5px solid #111; font-size: 22px; padding: 10px 14px; line-height: 1.7; vertical-align: middle; }}
table.s td.l {{ width: 150px; text-align: center; font-size: 21px; }}
.red {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; }}
.caret {{ color: {RED}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-weight: bold; font-size: 18px;
          vertical-align: super; }}
.bubble {{ display: inline-block; border: 2.5px solid {RED}; border-radius: 14px; padding: 8px 18px; color: {RED};
           font-size: 20px; font-weight: bold; background: #fff5f5; line-height: 1.5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubrow {{ margin: 12px 0 0; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 3px; background: #f1faf2; }}
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


def area(floors):
    """床面積の整数部・小数部のセル。floors: [(階の表示, 整数部, 小数部)]。整数部のセルは答案用紙の所在の下段の
    区切りの位置で2列にまたがる"""
    ints = br(*[ink(f'{k}　{a}' if k else a) for k, a, _ in floors])
    decs = br(*[ink(b) for _, _, b in floors])
    return f'<td class="entry int" colspan="2">{ints}</td><td class="entry dec">{decs}</td>'


# ---- 建物の表示（答案用紙の形：不動産番号、所在2段〈上段1枠・下段2枠〉、家屋番号2枠、見出し、記入行3行） ----
# 列：縦書き／主附／種類／構造a（家屋番号の区切りまで）／構造b／床面積の整数部a（所在の下段の区切りまで）／整数部b／小数部／原因
COLS = ('<colgroup><col style="width:5.7%"><col style="width:15.9%"><col style="width:12.7%"><col style="width:4.1%">'
        '<col style="width:12.4%"><col style="width:5.7%"><col style="width:10.3%"><col style="width:9.7%">'
        '<col style="width:23.5%"></colgroup>')
HEAD = ('<td class="head">主である建物<br>又は附属建物</td><td class="head">①種類</td><td class="head" colspan="2">②構造</td>'
        '<td class="head" colspan="3">③床面積　m²</td><td class="head">登記原因及びその日付</td>')
EMPTY_ROW = ('<tr><td class="entry"></td><td class="entry"></td><td class="entry" colspan="2"></td>'
             '<td class="entry int" colspan="2"></td><td class="entry dec"></td><td class="entry"></td></tr>')


def entry_row(shu, kind, struct, floors, genin):
    return (f'<tr><td class="entry center">{shu}</td><td class="entry center">{kind}</td>'
            f'<td class="entry center" colspan="2">{struct}</td>{area(floors)}<td class="entry genin">{genin}</td></tr>')


def table(shozai_top, shozai_left='', shozai_right='', kaoku='', rows=''):
    n = rows.count('<tr>')
    return (f'<table class="t">{COLS}'
            f'<tr><td class="lab2 val" colspan="2">不動産番号</td><td class="val" colspan="7"></td></tr>'
            f'<tr><td class="vert" rowspan="{4 + n}">建物の表示</td><td class="lab2" rowspan="2">所　　在</td>'
            f'<td class="val" colspan="7">{shozai_top}</td></tr>'
            f'<tr><td class="val" colspan="4">{shozai_left}</td><td class="val genin" colspan="3">{shozai_right}</td></tr>'
            f'<tr><td class="lab2 val">家屋番号</td><td class="val" colspan="2">{kaoku}</td><td class="val" colspan="5"></td></tr>'
            f'<tr>{HEAD}</tr>{rows}</table>')


def shinseisho(title, mokuteki, tenpu, shinseinin, tbl, caption):
    return page(f'''<div class="page">
<div class="head1">{title}</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink(mokuteki)}</div></div>
<div class="row"><div class="lab">添　付　情　報</div><div class="box" style="height:110px">{ink(tenpu)}</div></div>
<div class="dateline">平成25年８月23日申請　　Ｃ地方法務局</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:110px">{shinseinin}</div></div>
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{tbl}
<div class="caption">{caption}</div>
</div>''')


S_KURA = '軽量鉄骨造亜鉛<br>メッキ鋼板ぶき<br>２階建'
S_TEN = '鉄骨造陸屋根<br>平家建'
GENIN_SHU = '平成25年７月26日主である建物に変更、平成25年８月18日種類変更、増築'

# ---- 第1欄（問1）：本件旧建物 ----
ROWS1 = (entry_row(ink('主'), ink('倉庫'), ink(S_KURA), [('1階', '148', '22'), ('2階', '119', '24')], ink('平成25年７月26日取壊し'))
         + entry_row('', ink('店舗'), ink(S_TEN), [('', '38', '25')], ink(GENIN_SHU))
         + entry_row(ink('符号１'), ink('物置'), ink(S_TEN), [('', '22', '50')], ink('平成25年７月26日主である建物に変更')))
dai1 = shinseisho('本件旧建物に関する登記の申請書', '建物表題部変更登記', '建物図面　各階平面図　所有権証明情報　代理権限証明情報',
                  ink(br('Ｃ市Ｄ町一丁目３番２号　甲野春男', 'Ｃ市Ｄ町一丁目３番２号　甲野冬子')),
                  table(ink('Ｃ市Ｄ町一丁目12番地'), ink('Ｃ市Ｄ町一丁目12番地１'), ink('平成25年８月５日分筆により変更'),
                        ink('12番の１'), ROWS1),
                  '平成25年度 土地家屋調査士試験 第22問 第1欄 登記申請書 解答例')

# ---- 第2欄（問2）：本件新建物 ----
SHOZAI_OK = 'Ｃ市Ｄ町一丁目11番地、10番地'
SHINSEININ_OK = br('Ｃ市Ｄ町一丁目３番２号　持分２分の１　甲野春男', 'Ｃ市Ｄ町一丁目３番２号　　　２分の１　甲野冬子')
ROWS2 = entry_row('', ink('倉庫'), ink(S_KURA), [('1階', '148', '22'), ('2階', '119', '24')], ink('平成25年８月22日新築')) + EMPTY_ROW * 2
dai2 = shinseisho('本件新建物に関する登記の申請書', '建物表題登記',
                  br('建物図面　各階平面図　所有権証明情報　住所証明情報', '代理権限証明情報'),
                  ink(SHINSEININ_OK), table(ink(SHOZAI_OK), rows=ROWS2),
                  '平成25年度 土地家屋調査士試験 第22問 第2欄 登記申請書 解答例')

# ---- 第3欄（問3）：説明 ----
SETSUMEI = ('本件取壊建物については、建物滅失登記を申請する必要がある。建物滅失登記は、建物が滅失した事実を登記記録に反映させる'
            '報告的登記であり、その申請は共有物の保存行為に当たるから、甲野冬子が関与しなくても、共有者の1人である甲野春男が'
            '単独で申請することができる（民法第252条第5項、不動産登記法第57条）。')
dai3 = page(f'''<div class="page">
<div class="head1">土地家屋調査士民事花子の説明</div>
<div class="setsumei">{ink(SETSUMEI)}</div>
<div class="caption">平成25年度 土地家屋調査士試験 第22問 第3欄 解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：第2欄の「申請人」と「所在」 ----
def snippet(shinseinin, shozai, good=False):
    g = ' class="s good"' if good else ' class="s"'
    chk = CHECK_SVG if good else ''
    return (f'<div class="sub">本件新建物に関する登記の申請書（抜粋）</div>'
            f'<div class="okwrap"><table{g}><tr><td class="l">申　請　人</td><td style="height:100px">{shinseinin}</td></tr>'
            f'<tr><td class="l">所　　在</td><td style="height:62px">{shozai}</td></tr></table>{chk}</div>')


NG_SHINSEININ = ink(br('Ｃ市Ｄ町一丁目３番２号　甲野春男', 'Ｃ市Ｄ町一丁目３番２号　甲野冬子'))
FIX_SHINSEININ = br(ink('Ｃ市Ｄ町一丁目３番２号　') + '<span class="caret">∧</span><span class="red">持分２分の１</span>　' + ink('甲野春男'),
                    ink('Ｃ市Ｄ町一丁目３番２号　') + '<span class="caret">∧</span><span class="red">２分の１</span>　' + ink('甲野冬子'))
FIX_SHOZAI = ink('Ｃ市Ｄ町一丁目11番地') + '<span class="caret">∧</span><span class="red">、10番地</span>'
ng_panel = snippet(NG_SHINSEININ, ink('Ｃ市Ｄ町一丁目11番地'))
fix_panel = snippet(FIX_SHINSEININ, FIX_SHOZAI) + \
    ('<div class="bubrow"><span class="bubble">申請人：表題登記は、表題部所有者になる者が2人以上なら持分を書く（令3条9号）。<br>'
     '第1欄の表題部変更登記とは違う</span></div>'
     '<div class="bubrow"><span class="bubble">所在：概略図にD-Cの線がない。座標で描くと南西の角の約1.0㎡が10番。<br>'
     '床面積の多い11番地が先（準則88条2項）</span></div>')
ok_panel = snippet(ink(SHINSEININ_OK), ink(SHOZAI_OK), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成25年度 第22問｜表題登記の申請人には持分、所在は座標で決めて11番地、10番地</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 100})   # 高さは内容に合わせる（full_page）
        for name, html in [('H25_dai22mon_dai1ran_kansei', dai1), ('H25_dai22mon_dai2ran_kansei', dai2),
                           ('H25_dai22mon_dai3ran_kansei', dai3), ('H25_dai22mon_toukishinseisho_machigai', machigai)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（第3欄は文章だけの欄なので横長でもよい）'))
        browser.close()
