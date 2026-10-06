"""平成26年度 第22問（建物）答案用紙の画像（第1欄、第2欄、第4欄、第3欄〈登記申請書〉の完成形と、第2欄の添削）を、
HTML＋ヘッドレスブラウザでPNGに書き出す。

- 画像1（第1欄）・画像2（第2欄）・画像3（第4欄）・画像4（第3欄 登記申請書）：`../prompt_H26_dai22mon_toukishinseisho_gazou.md` の記入データどおり。
  noteのスマートフォン表示に合わせ、どれも横1200pxにしている（答案用紙はA3横だが、欄ごとに1枚に分け、記事のその問の答えの直後に置く。
  2026-10-02、第1欄・第2欄を1枚にしていたのを、問1・問2それぞれの答えの直後に置けるように2枚に分けた）
- 画像4の項目の順序は答案用紙の印刷どおり「登記の目的 → 添付情報 → 平成26年8月22日　申請　Ｇ地方法務局 → 申請人（略） → 代理人（略） → 建物の表示」。
  登録免許税の欄はない。添付情報は今の法令（会社法人等番号）で書き、建物の表示の表の下に出題当時の扱いの注を入れる
- 添削：`../prompt_H26_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）。
  添削1は第2欄の登記の目的・登記原因及びその日付、添削2は第3欄の建物の表示の2行目・5行目の登記原因及びその日付（2026-10-04追加）

CSSと部品の作りは `H27/Q22/zu/make_H27_dai22mon_shinseisho_gazou.py` と同じ形にしている。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP、なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/H26/Q22/zu/make_H26_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
.row {{ display: flex; align-items: flex-start; margin-bottom: 24px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.nw {{ white-space: nowrap; }}
.dateline {{ font-size: 22px; margin: 2px 0 14px 0; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 20px; }}
.plainrow .ryaku {{ flex: 1; padding-left: 60px; }}
.sec {{ font-size: 24px; margin: 34px 0 0; }}
table.k {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 16px; }}
table.k td {{ border: 1.5px solid #111; font-size: 22px; padding: 16px 16px; vertical-align: middle; line-height: 1.6; }}
table.k td.klab {{ width: 290px; text-align: center; white-space: nowrap; }}
table.k td.tall {{ height: 130px; vertical-align: top; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-top: 18px; }}
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 8px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.6em; padding: 0; font-size: 21px; }}
table.t td.shozai-lab {{ text-align: center; font-size: 19px; }}
table.t td.shozai {{ height: 52px; }}
table.t td.head {{ text-align: center; font-size: 17px; height: 76px; }}
table.t td.entry {{ height: 118px; }}
table.t td.blank {{ height: 60px; }}
table.t td.center {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td.genin {{ font-size: 17px; }}
table.t td .ink {{ font-size: 19px; }}
.tnote {{ font-size: 17px; color: #444; margin-top: 12px; line-height: 1.6;
          font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.essay {{ border: 3px solid #111; padding: 22px 26px; min-height: 460px; font-size: 24px; line-height: 1.95;
          text-indent: 1em; margin-top: 18px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 34px;
            font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
/* 添削画像 */
.panel {{ padding: 36px 60px 42px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; font-weight: bold;
           margin-bottom: 14px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.strike {{ position: relative; }}
.strike::after {{ content: ""; position: absolute; left: -3px; right: -3px; top: 52%; border-top: 3px solid {RED};
                  transform: rotate(-2deg); }}
.red {{ color: {RED}; font-weight: bold; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 21px; font-weight: bold; background: #fff5f5; line-height: 1.5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; left: 60px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: 16px 0 0 290px; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; background: #f1faf2; }}
.okwrap {{ position: relative; }}
.check {{ position: absolute; right: -14px; top: -22px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def items(*words):
    """添付情報などの語を、語の途中で折り返さないように並べる"""
    return '　'.join(f'<span class="nw">{w}</span>' for w in words)


def br(*lines):
    return '<br>'.join(lines)


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---- 画像1：第1欄、画像2：第2欄 ----
def mokuteki_table(title, mokuteki, genin, tenpu):
    return (f'<div class="sec">{title}</div>'
            f'<table class="k"><tr><td class="klab">登記の目的</td><td>{mokuteki}</td></tr>'
            f'<tr><td class="klab">登記原因及びその日付</td><td>{genin}</td></tr>'
            f'<tr><td class="klab">添付情報</td><td class="tall">{tenpu}</td></tr></table>')


DAI1 = ('平成26年7月22日に申請した登記の登記の目的等', '区分建物表題部変更登記（敷地権抹消）', '平成26年６月30日非敷地権',
        ('規約廃止証明書', '代理権限証書'))
DAI2 = ('平成26年7月24日に申請した登記の登記の目的等', '建物表題登記（共用部分廃止）', '平成26年６月30日共用部分の規約廃止',
        ('規約廃止証明書', '所有権証明書', '住所証明書', '代理権限証書'))

dai1ran = page(f'''<div class="page">
{mokuteki_table('第1欄　' + DAI1[0], ink(DAI1[1]), ink(DAI1[2]), ink(items(*DAI1[3])))}
<div class="caption">平成26年度 土地家屋調査士試験 第22問 第1欄 解答例</div>
</div>''')
dai2ran = page(f'''<div class="page">
{mokuteki_table('第2欄　' + DAI2[0], ink(DAI2[1]), ink(DAI2[2]), ink(items(*DAI2[3])))}
<div class="caption">平成26年度 土地家屋調査士試験 第22問 第2欄 解答例</div>
</div>''')

# ---- 画像3：第4欄 ----
DAI4 = ('家屋番号1番10の建物を附属建物として登記するには、主である建物と所有者が同一であり、主である建物の効用を補う建物として、'
        '主である建物と効用上一体として利用される状態にあることが必要である。家屋番号1番10の建物は事務所であり、'
        '本件建物は作業道具を一時的に保管する倉庫として事務所の効用を補うものであるから、主である建物は家屋番号1番10の建物となり、'
        '同建物を附属建物として登記することはできない。本件建物を家屋番号1番10の建物の附属建物として登記すべきである。')

gazou2 = page(f'''<div class="page">
<div class="sec" style="margin-top:0">第4欄　丙川太郎に対して説明すべき内容</div>
<div class="essay">{ink(DAI4)}</div>
<div class="caption">平成26年度 土地家屋調査士試験 第22問 第4欄 解答例</div>
</div>''')

# ---- 画像4：第3欄 登記申請書 ----
TENPU = ('建物図面', '各階平面図', '登記識別情報', '会社法人等番号', '印鑑証明書（会社法人等番号の提供により省略）', '代理権限証書')
NOTE = ('※添付情報は今の法令による。出題当時は会社法人等番号の制度（平成27年11月施行）がなく、会社法人等番号の代わりに'
        '代表者の資格を証する情報（資格証明書）を付け、印鑑証明書も省略せずに付けていた')
KOUZOU_SHAKO = '軽量鉄骨造<br>合金メッキ<br>鋼板ぶき平家建'
KOUZOU_JIMU = '鉄骨造<br>陸屋根<br>２階建'

COLS = ('<colgroup><col style="width:5%"><col style="width:12%"><col style="width:9%"><col style="width:9%">'
        '<col style="width:9%"><col style="width:15%"><col style="width:11%"><col style="width:5%">'
        '<col style="width:25%"></colgroup>')
HEAD = ('<td class="head">地　番</td><td class="head">家屋番号</td>'
        '<td class="head" style="font-size:15px">主である<br>建物又は<br>附属建物</td>'
        '<td class="head">①種類</td><td class="head">②構　造</td><td class="head" colspan="2">③床面積　m²</td>'
        '<td class="head">登記原因及び<br>その日付</td>')


def area(floors):
    """床面積の整数部・小数部のセル。floors: [(階の表示, 整数部, 小数部)]"""
    ints = br(*[ink(f'{k}　{a}' if k else a) for k, a, _ in floors])
    decs = br(*[ink(b) for _, _, b in floors])
    return f'<td class="entry int">{ints}</td><td class="entry dec">{decs}</td>'


def row(chiban, kaoku, shu, kind, kouzou, floors, genin):
    return (f'<tr><td class="entry">{chiban}</td><td class="entry center">{kaoku}</td><td class="entry center">{shu}</td>'
            f'<td class="entry center">{kind}</td><td class="entry center">{kouzou}</td>{area(floors)}'
            f'<td class="entry genin">{genin}</td></tr>')


ROWS = [
    row(ink('1番地8'), ink('1番8'), '', ink('車庫'), ink(KOUZOU_SHAKO), [('', '90', '00')], ''),
    row('', '', '', ink('倉庫'), '', [], ink('①平成26年８月10日種類変更<br>1番10に合併')),
    row(ink('1番地10'), ink('1番10'), '', ink('事務所'), ink(KOUZOU_JIMU), [('1階', '159', '82'), ('2階', '85', '29')], ''),
    row(ink('1番地10<br>1番地8'), ink('1番10'), ink('主'), ink('事務所'), ink(KOUZOU_JIMU),
        [('1階', '159', '82'), ('2階', '85', '29')], ''),
    row('', '', ink('符号１'), ink('倉庫'), ink(KOUZOU_SHAKO), [('', '90', '00')], ink('1番8を合併')),
]
TABLE3 = (f'<table class="t">{COLS}'
          f'<tr><td class="vert" rowspan="9">建物の表示</td><td class="shozai-lab" rowspan="2">所　在</td>'
          f'<td class="shozai" colspan="7">{ink("Ａ市Ｂ町一丁目")}</td></tr>'
          f'<tr><td class="shozai" colspan="6"></td><td class="shozai"></td></tr>'
          f'<tr>{HEAD}</tr>{"".join(ROWS)}'
          f'<tr><td class="blank" colspan="8"></td></tr></table>')

gazou3 = page(f'''<div class="page">
<div class="sec" style="margin:0 0 26px">第3欄　平成26年8月22日に申請した登記の登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink('建物表題部変更・合併登記')}</div></div>
<div class="row"><div class="lab">添　付　情　報</div><div class="box" style="min-height:120px">{ink(items(*TENPU))}</div></div>
<div class="dateline">平成26年8月22日　申請　Ｇ地方法務局</div>
<div class="plainrow"><div class="lab" style="padding-top:0">申　請　人</div><div class="ryaku">（略）</div></div>
<div class="plainrow"><div class="lab" style="padding-top:0">代　理　人</div><div class="ryaku">（略）</div></div>
{TABLE3}
<div class="tnote">{NOTE}</div>
<div class="caption">平成26年度 土地家屋調査士試験 第22問 第3欄 登記申請書 解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ）：第2欄の登記の目的・登記原因及びその日付 ----
def dai2_panel(mokuteki, genin, bub1='', bub2='', good=False):
    """第2欄の2行。吹き出しは縦長に合わせて各行のすぐ下に置く（行と行の間に吹き出しがあるときは表を2つに分ける）"""
    cls = 'k'
    chk = CHECK_SVG if good else ''
    wrap = 'okwrap good' if good else 'okwrap'
    t1 = f'<table class="{cls}"><tr><td class="klab">登記の目的</td><td>{mokuteki}</td></tr></table>'
    gap = 'margin-top:18px' if bub1 else 'margin-top:-3px'
    t2 = f'<table class="{cls}" style="{gap}"><tr><td class="klab">登記原因及びその日付</td><td>{genin}</td></tr></table>'
    b1 = f'<div class="bubrow"><span class="bubble">{bub1}</span></div>' if bub1 else ''
    b2 = f'<div class="bubrow"><span class="bubble">{bub2}</span></div>' if bub2 else ''
    return (f'<div class="sec" style="margin-top:0">第2欄　平成26年7月24日に申請した登記の登記の目的等</div>'
            f'<div class="{wrap}">{t1}{b1}{t2}{chk}</div>{b2}')


st = lambda s: f'<span class="ink strike">{s}</span>'  # noqa: E731
red = lambda s: f'<span class="red">{s}</span>'  # noqa: E731
ng_panel = dai2_panel(ink('建物表題部変更登記（共用部分である旨の抹消）'), ink('平成26年４月30日共用部分の規約廃止'))
fix_panel = dai2_panel(
    ink('建物表題') + st('部変更') + ink('登記') + st('（共用部分である旨の抹消）') + red('（共用部分廃止）'),
    ink('平成26年') + st('４月30日') + red('６月30日') + ink('共用部分の規約廃止'),
    bub1='共用部分の登記で権利部は抹消済み（法58条4項）<br>→規約廃止なら表題登記（法58条6項）',
    bub2='４月30日は理事会で議題があがっただけ。<br>規約の廃止は総会の決議の日（区分所有法31条1項）')
ok_panel = dai2_panel(ink('建物表題登記（共用部分廃止）'), ink('平成26年６月30日共用部分の規約廃止'), good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">平成26年度 第22問｜共用部分の規約を廃止したら表題部変更じゃなく表題登記、日付は総会の日</div>''')


# ---- 添削2（①誤答 → ②添削 → ③正解）：第3欄の建物の表示の「登記原因及びその日付」（2行目・5行目） ----
GCOLS = ('<colgroup><col style="width:24%"><col style="width:17%"><col style="width:12%">'
         '<col style="width:47%"></colgroup>')
GHEAD = ('<tr><td class="head">行</td><td class="head" style="font-size:15px">主である<br>建物又は<br>附属建物</td>'
         '<td class="head">①種類</td><td class="head">登記原因及び<br>その日付</td></tr>')


def dai3_panel(g2, g5, bub2='', bub5='', good=False):
    """第3欄の建物の表示のうち、2行目（変更後の本件建物）と5行目（合併後の附属建物）だけを取り出した表"""
    chk = CHECK_SVG if good else ''
    wrap = 'okwrap good' if good else 'okwrap'

    def tb(label, shu, kind, genin, first):
        head = GHEAD if first else ''
        mt = '' if first else 'margin-top:18px'
        return (f'<table class="t" style="{mt}">{GCOLS}{head}<tr><td class="entry" style="font-size:17px">{label}</td>'
                f'<td class="entry center">{shu}</td><td class="entry center">{kind}</td>'
                f'<td class="entry genin" style="font-size:19px">{genin}</td></tr></table>')
    b2 = f'<div class="bubrow" style="margin-left:330px"><span class="bubble">{bub2}</span></div>' if bub2 else ''
    b5 = f'<div class="bubrow" style="margin-left:330px"><span class="bubble">{bub5}</span></div>' if bub5 else ''
    return (f'<div class="sec" style="margin-top:0">第3欄　建物の表示（2行目・5行目だけ）</div>'
            f'<div class="{wrap}">{tb("2行目<br>（変更後の本件建物）", "", ink("倉庫"), g2, True)}{b2}'
            f'{tb("5行目<br>（合併後の附属建物）", ink("符号１"), ink("倉庫"), g5, False)}{chk}</div>{b5}')


ng3 = dai3_panel(ink('平成26年８月10日種類変更、1番10に合併'), ink('平成26年８月22日1番8を合併'))
fix3 = dai3_panel(red('①') + ink('平成26年８月10日種類変更') + st('、') + '<br>' + ink('1番10に合併'),
                  st('平成26年８月22日') + ink('1番8を合併'),
                  bub2='変更した欄の番号を頭に付ける（種類は①）。<br>種類変更は工事の完了を報告する登記なので日付を書く',
                  bub5='合併は登記をして初めて1個になる形成的登記。<br>日付は書かない（申請日の８月22日も書かない）')
ok3 = dai3_panel(ink('①平成26年８月10日種類変更<br>1番10に合併'), ink('1番8を合併'), good=True)
machigai3 = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng3}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix3}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok3}</div>
<div class="caption" style="margin:10px 0 30px">平成26年度 第22問｜種類変更には①と日付、合併には日付を付けない</div>''')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 300})
        for name, html in [('H26_dai22mon_dai1ran_kansei', dai1ran),
                           ('H26_dai22mon_dai2ran_kansei', dai2ran),
                           ('H26_dai22mon_dai4ran_kansei', gazou2),
                           ('H26_dai22mon_toukishinseisho_kansei', gazou3),
                           ('H26_dai22mon_toukishinseisho_machigai', machigai),
                           ('H26_dai22mon_toukishinseisho_machigai_dai3ran', machigai3)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長（要確認）'))
        browser.close()
