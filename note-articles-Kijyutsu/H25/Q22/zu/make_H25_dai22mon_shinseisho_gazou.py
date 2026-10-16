"""平成25年度 第22問（建物）の答案用紙の画像（第1欄・第2欄の登記申請書の完成形、第3欄の説明の完成形、添削）を、
HTML＋ヘッドレスブラウザでPNGに書き出す。

- 第1欄・第2欄：`../prompt_H25_dai22mon_toukishinseisho_gazou.md` の画像1・画像2の記入データどおり。縦長（横1200px）。
  答案用紙（試験の答案用紙。`../touan_youshi/H25_dai22mon_touan_youshi.pdf` の1ページ目で確かめた。
  `public/kijutsu/H25-tatemono/a1.webp` と同じもの）はA3横で、左の列に第1欄、右の列に第2欄と第3欄がある。
  第1欄と第2欄は記事の別々の問（問1・問2）の答えなので、欄ごとに別の画像にし、それぞれの答えの直後に置く。
  欄の形は試験の答案用紙どおり：見出し（本件旧建物／本件新建物に関する登記の申請書）、登記の目的、添付情報、
  申請の日付と提出先（平成25年8月23日申請　C地方法務局。印刷済み）、申請人、代理人（略）。登録免許税の欄はない。
  表は、不動産番号（試験の答案用紙に印刷されている行。記入は空欄）、建物の表示（所在2段〈上段1枠・下段は左右2枠〉、家屋番号〈左右2枠〉、見出し、記入行3行）
- 第3欄　　　：同じく画像3どおり。「第3欄　土地家屋調査士民事花子の説明」の大きな枠（申請書ではない解答欄なので別の画像。
  見出しは答案用紙に印刷されたとおり「第3欄」を付ける。申請書の画像には「第○欄」を入れない）
- 添削　　　：`../prompt_H25_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）。
  2026-10-16、欄ごとに1枚に分けて4枚にした（第2欄の所在・第2欄の申請人・第1欄の取り壊した主である建物の行の床面積・
  第1欄の新しい主である建物の行の原因の欄番号）。枠の高さは固定せず min-height で中の文字に合わせて伸ばす（`style="height:` は使わない）。
- 列の幅：建物の表示の表の列の幅と、所在の下段・家屋番号の行の仕切りの位置は、答案用紙の原本の1ページ目（`../touan_youshi/H25_dai22mon_touan_youshi_p1.png`）
  の第1欄の表の罫線の位置（記入行の高さで測った縦線 x＝118・174・336.5・463・628.5・788・889・1125.5px、所在の下段の仕切り684.5px、
  家屋番号の仕切り505px）から比にした（照合スクリプトで画像から測り直して確かめる）

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
.mokuteki {{ min-height: 62px; }}
.tenpu {{ min-height: 110px; }}
.shinseinin {{ min-height: 110px; }}
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
table.s td.one {{ height: 62px; }}   /* 表のセルの height は最小の高さ（中の文字に合わせて伸びる） */
table.s td.two {{ height: 100px; }}
/* 添削の3コマ：横1200pxの縦長にするため、コマの最小の高さを決める（中の文字に合わせて伸びる） */
.panel.tall {{ min-height: 420px; }}
.panel.last {{ border-bottom: none; }}
.caption.tensaku {{ margin: 10px 0 30px; }}
.strike {{ text-decoration: line-through; text-decoration-thickness: 3px; }}
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
COL_W = (5.56, 16.13, 12.56, 4.17, 12.26, 5.56, 10.27, 10.02, 23.47)   # 答案用紙の原本の罫線から測った比（合計100）
COLS = '<colgroup>' + ''.join(f'<col style="width:{w}%">' for w in COL_W) + '</colgroup>'
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
<div class="row"><div class="lab">登記の目的</div><div class="box mokuteki">{ink(mokuteki)}</div></div>
<div class="row"><div class="lab">添　付　情　報</div><div class="box tenpu">{ink(tenpu)}</div></div>
<div class="dateline">平成25年８月23日申請　　Ｃ地方法務局</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box shinseinin">{shinseinin}</div></div>
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
                  '平成25年度 土地家屋調査士試験 第22問 問1 登記申請書 解答例')

# ---- 第2欄（問2）：本件新建物 ----
SHOZAI_OK = 'Ｃ市Ｄ町一丁目11番地、10番地'
SHINSEININ_OK = br('Ｃ市Ｄ町一丁目３番２号　持分２分の１　甲野春男', 'Ｃ市Ｄ町一丁目３番２号　　　２分の１　甲野冬子')
ROWS2 = entry_row('', ink('倉庫'), ink(S_KURA), [('1階', '148', '22'), ('2階', '119', '24')], ink('平成25年８月22日新築')) + EMPTY_ROW * 2
dai2 = shinseisho('本件新建物に関する登記の申請書', '建物表題登記',
                  br('建物図面　各階平面図　所有権証明情報　住所証明情報', '代理権限証明情報'),
                  ink(SHINSEININ_OK), table(ink(SHOZAI_OK), rows=ROWS2),
                  '平成25年度 土地家屋調査士試験 第22問 問2 登記申請書 解答例')

# ---- 第3欄（問3）：説明 ----
SETSUMEI = ('本件取壊建物については、建物滅失登記を申請する必要がある。建物滅失登記は、建物が滅失した事実を登記記録に反映させる'
            '報告的登記であり、その申請は共有物の保存行為に当たるから、甲野冬子が関与しなくても、共有者の1人である甲野春男が'
            '単独で申請することができる（民法第252条第5項、不動産登記法第57条）。')
dai3 = page(f'''<div class="page">
<div class="head1">第3欄　土地家屋調査士民事花子の説明</div>
<div class="setsumei">{ink(SETSUMEI)}</div>
<div class="caption">平成25年度 土地家屋調査士試験 第22問 問3 解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：欄ごとに1枚 ----
def three(sub, ng, fix, notes, ok, caption):
    bub = ''.join(f'<div class="bubrow"><span class="bubble">{n}</span></div>' for n in notes)
    return page(f'''
<div class="panel tall"><div class="ptitle ng">①誤答</div><div class="sub">{sub}</div>{ng}</div>
<div class="panel tall"><div class="ptitle fix">②添削（赤ペン）</div><div class="sub">{sub}</div>{fix}{bub}</div>
<div class="panel tall last"><div class="ptitle ok">③正解</div><div class="sub">{sub}</div>
<div class="okwrap good">{ok}{CHECK_SVG}</div></div>
<div class="caption tensaku">{caption}</div>''')


def one_row(label, body, cls='one'):
    """申請書の1つの欄（左に項目名、右に記入）の抜粋。"""
    return f'<table class="s"><tr><td class="l">{label}</td><td class="{cls}">{body}</td></tr></table>'


def hyou(rows):
    """建物の表示の表の抜粋（見出し行と記入行。列は答案用紙の比）。rows：[(主附, 種類, 構造, 床面積のセル, 原因)]"""
    w = COL_W
    cols = (f'<colgroup><col style="width:{w[1] + w[0]:.2f}%"><col style="width:{w[2]}%"><col style="width:{w[3] + w[4]:.2f}%">'
            f'<col style="width:{w[5] + w[6]:.2f}%"><col style="width:{w[7]}%"><col style="width:{w[8]}%"></colgroup>')
    head = ('<tr><td class="head">主である建物<br>又は附属建物</td><td class="head">①種類</td><td class="head">②構造</td>'
            '<td class="head" colspan="2">③床面積　m²</td><td class="head">登記原因及びその日付</td></tr>')
    body = ''.join(f'<tr><td class="entry center">{a}</td><td class="entry center">{b}</td><td class="entry center">{c}</td>{d}'
                   f'<td class="entry genin">{e}</td></tr>' for a, b, c, d, e in rows)
    return f'<table class="t">{cols}{head}{body}</table>'


def men(floors, red=False):
    f = (lambda s: f'<span class="red">{s}</span>') if red else ink
    ints = br(*[f(f'{k}　{a}' if k else a) for k, a, _ in floors])
    decs = br(*[f(b) for _, _, b in floors])
    return f'<td class="entry int">{ints}</td><td class="entry dec">{decs}</td>'


CARET = '<span class="caret">∧</span>'
SUB2 = '本件新建物に関する登記の申請書（抜粋）'
SUB1 = '本件旧建物に関する登記の申請書（抜粋）　建物の表示'

# 1) 第2欄の所在
m_shozai = three(SUB2, one_row('所　　在', ink('Ｃ市Ｄ町一丁目11番地')),
                 one_row('所　　在', ink('Ｃ市Ｄ町一丁目11番地') + CARET + '<span class="red">、10番地</span>'),
                 ['概略図にはD-Cの線がない。座標で描くと南西の角の約1.0㎡が10番に入る。', '床面積の多い11番地が先（準則88条2項）。地番の順の「10番地、11番地」にしない'],
                 one_row('所　　在', ink(SHOZAI_OK)), '平成25年度 第22問｜所在は座標で決めて11番地、10番地')
# 2) 第2欄の申請人
FIX_SHINSEININ = br(ink('Ｃ市Ｄ町一丁目３番２号　') + CARET + '<span class="red">持分２分の１</span>　' + ink('甲野春男'),
                    ink('Ｃ市Ｄ町一丁目３番２号　') + CARET + '<span class="red">２分の１</span>　' + ink('甲野冬子'))
m_shinseinin = three(SUB2, one_row('申　請　人', ink(br('Ｃ市Ｄ町一丁目３番２号　甲野春男', 'Ｃ市Ｄ町一丁目３番２号　甲野冬子')), 'two'),
                     one_row('申　請　人', FIX_SHINSEININ, 'two'),
                     ['表題登記は、表題部所有者になる者が2人以上なら持分を書く（令3条9号）。', '第1欄の表題部変更登記の申請人には書かない'],
                     one_row('申　請　人', ink(SHINSEININ_OK), 'two'), '平成25年度 第22問｜表題登記の申請人には持分を書く')
# 3) 第1欄の取り壊した主である建物の行の床面積
ROW_SHU = (ink('主'), ink('倉庫'), ink(S_KURA))
m_yuka = three(SUB1, hyou([ROW_SHU + ('<td class="entry int"></td><td class="entry dec"></td>', ink('平成25年７月26日取壊し'))]),
               hyou([ROW_SHU + (men([('1階', '148', '22'), ('2階', '119', '24')], red=True), ink('平成25年７月26日取壊し'))]),
               ['登記記録の抜粋に主である建物の床面積がなくても空欄にしない。', '事実関係1：本件新建物と相違点がない → 問4の求積値（148.22・119.24）を書く'],
               hyou([ROW_SHU + (men([('1階', '148', '22'), ('2階', '119', '24')]), ink('平成25年７月26日取壊し'))]),
               '平成25年度 第22問｜取り壊した主である建物の床面積は本件新建物の求積値で埋める')
# 4) 第1欄の新しい主である建物の行の原因（欄番号を付けない）
ROW_TEN = ('', ink('店舗'), ink(S_TEN), men([('', '38', '25')]))
m_genin = three(SUB1, hyou([ROW_TEN + (ink('①③' + GENIN_SHU),)]),
                hyou([ROW_TEN + ('<span class="red strike">①③</span>' + ink(GENIN_SHU),)]),
                ['主である建物に変更した行は、種類・構造・床面積を全部書き起こす行。', '前の行のどの欄が変わったかを示す行ではないので欄番号は付けない（準則102条）'],
                hyou([ROW_TEN + (ink(GENIN_SHU),)]), '平成25年度 第22問｜主である建物に変更した行の原因に欄番号を付けない')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 100})   # 高さは内容に合わせる（full_page）
        for name, html in [('H25_dai22mon_dai1ran_kansei', dai1), ('H25_dai22mon_dai2ran_kansei', dai2),
                           ('H25_dai22mon_dai3ran_kansei', dai3), ('H25_dai22mon_toukishinseisho_machigai_shozai', m_shozai),
                           ('H25_dai22mon_toukishinseisho_machigai_yukamenseki', m_yuka),
                           ('H25_dai22mon_toukishinseisho_machigai_genin', m_genin),
                           ('H25_dai22mon_toukishinseisho_machigai_shinseinin', m_shinseinin)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else ('横長（第3欄は文章だけの欄なので横長でもよい）' if 'dai3ran' in name else '横長（要修正）')))
        browser.close()
