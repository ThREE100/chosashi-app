"""令和8年度 第22問（建物）の答案の画像（第1欄・第4欄・登記申請書の完成形、欄ごとの添削5枚）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 欄の形・順序は、アガルートの解答例（答案用紙の再現。A3横、左の列に第1欄・第2欄〈登記申請書・一棟の建物の表示・敷地権の目的である
  土地の表示〉、右の列に区分した建物の表示・敷地権の表示・第4欄）どおり（2026-10-20に照らし直し）。完成形は左の列 → 右の列の順に縦に積む
- 答案用紙に「（略）」と印刷された欄（提出先の後半を除く代理人以外の欄：一棟の建物の所在・構造・床面積、敷地権の目的である土地、
  区分前の行の種類・構造・床面積、敷地権の表示の区分前の行）にも、自力で解いた答えを記入する（ユーザー指示、2026-10-20）。
  一棟の建物の構造・床面積は、名称を書くので省略できる（不動産登記令第3条第8号ヘ）ため、自力の答えでも書いていない
- 添削：①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）。誤答の欄ごとに1枚
- 第1欄（問1）・第4欄（問4）：申請書でない解答欄も、答案用紙の欄の形で別の画像にする

必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP）
実行: python3 note-articles-Kijyutsu/R8/Q22/zu/make_R8_dai22mon_shinseisho_gazou.py [出力フォルダ]
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
body {{ background: #fff; width: 1200px; font-family: "Noto Serif CJK JP", "IPAMincho", serif; color: #111; }}
.page {{ padding: 60px 60px 40px; }}
.title {{ text-align: center; font-size: 40px; letter-spacing: 0.9em; margin: 0 0 40px 0.9em; }}
.row {{ display: flex; align-items: flex-start; margin-bottom: 22px; }}
.lab {{ width: 170px; font-size: 22px; padding-top: 10px; white-space: nowrap; }}
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 24px; line-height: 1.6; min-height: 62px; }}
.ink {{ color: {INK}; font-family: {SANS}; }}
.plainrow {{ display: flex; font-size: 22px; margin-bottom: 22px; }}
.plainrow .ryaku {{ flex: 1; text-align: center; }}
.date {{ font-size: 23px; margin: 0 0 22px 170px; }}
table.t {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; margin-bottom: 26px; }}
table.t td {{ border: 1.5px solid #111; font-size: 17px; padding: 8px 10px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.12em; padding: 0 4px; font-size: 19px; }}
table.t td.head {{ text-align: center; font-size: 18px; height: 60px; }}
table.t td.e {{ height: 92px; }}
table.t td.c {{ text-align: center; }}
table.t td.int {{ vertical-align: bottom; text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ vertical-align: bottom; text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td .ink {{ font-size: 20px; }}
table.t td.g .ink {{ font-size: 18px; }}
.note {{ font-family: {SANS}; font-size: 16px; color: #555; margin: -16px 0 22px; }}
td.note2 {{ font-family: {SANS}; font-size: 14px !important; color: #555; }}
.ryk {{ color: #888; font-size: 15px; }}
.ranlab {{ font-family: {SANS}; font-weight: bold; font-size: 24px; margin-bottom: 14px; }}
.colsep {{ font-family: {SANS}; color: #888; font-size: 16px; border-top: 2px dashed #aaa; padding-top: 6px; margin: 10px 0 18px; }}
.caption {{ text-align: center; font-size: 17px; color: #555; margin-top: 24px; font-family: {SANS}; }}
.panel {{ padding: 26px 60px 30px; border-bottom: 2px solid #bbb; }}
.ptitle {{ font-family: {SANS}; font-size: 28px; font-weight: bold; margin-bottom: 20px; }}
.ptitle.ng {{ color: #555; }} .ptitle.fix {{ color: {RED}; }} .ptitle.ok {{ color: {GREEN}; }}
.strike {{ text-decoration: line-through; text-decoration-color: {RED}; text-decoration-thickness: 3px; }}
.red {{ color: {RED}; font-family: {SANS}; font-weight: bold; }}
.bubble {{ display: inline-block; border: 2.5px solid {RED}; border-radius: 14px; padding: 8px 18px; color: {RED};
           font-size: 21px; font-weight: bold; background: #fff5f5; line-height: 1.5; font-family: {SANS}; }}
.bubrow {{ margin: 14px 0 0; text-align: right; }}
.bubrow .bubble {{ text-align: left; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; background: #f1faf2; }}
/* 問1・問4の解答欄の行の高さ（表のセルの height は最小の高さとして働く。原本の行は問1が15mm・問4が14mm） */
table.t td.q1 {{ height: 110px; font-size: 24px; }}
table.t td.q1a {{ font-size: 28px; padding-left: 40px; }}
.q1w {{ display: flex; justify-content: space-between; align-items: baseline; }}
.dok {{ font-size: 22px; }}
table.t td.q4 {{ height: 84px; font-size: 24px; }}
table.t td.q4a {{ font-size: 26px; padding-left: 28px; }}
.tall {{ min-height: 1300px; display: flex; flex-direction: column; justify-content: space-around; }}
'''


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def br(*lines):
    return '<br>'.join(lines)


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def three(title_ng, ng, fix, ok, caption):
    return page(f'''<div class="tall">
<div class="panel"><div class="ptitle ng">①誤答（{title_ng}）</div>{ng}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix}</div>
<div class="panel" style="border-bottom:none"><div class="ptitle ok">③正解</div>{ok}</div>
<div class="caption" style="margin:10px 0 30px">{caption}</div></div>''')


def field(lab, content, good=False, h=None):
    g = ' good' if good else ''
    st = f' style="min-height:{h}px"' if h else ''
    return f'<div class="row"><div class="lab">{lab}</div><div class="box{g}"{st}>{content}</div></div>'


# ---- 記入データ ----
MOKUTEKI = '区分建物区分登記'
TENPU = br('規約証明書　建物図面　各階平面図', '抵当権消滅承諾書　代理権限証書')
SHINSEININ = 'A市B町四丁目6番3－701号　白石恵'
ZEI = '金2,000円'
SHOZAI = 'A市B町四丁目6番地3'
MEISHOU = 'WKマンション'
K701 = 'B町四丁目<br>6番3の<br>701'
K702 = 'B町四丁目<br>6番3の<br>702'
KOUZOU = '鉄筋コンクリート<br>造1階建'
G701 = '③6番3の<br>702を区分'
G702 = '6番3の701<br>から区分'
G_HEN = '③令和8年10月18日変更'
G_SHIKI = '平成12年6月17日敷地権'
RYAKU = '<span class="ryk">（略）</span>'


def r(s_):   # 答案用紙に（略）と印刷された欄に書いた自力の答え
    return f'{RYAKU}<br>{ink(s_)}' if s_ else RYAKU


# 列の幅は、アガルートの解答例（答案用紙の再現、A3のベクターPDF）の縦の罫線のx座標（mm）から測った比（2026-10-26）。
# 区分した建物の表示：235.7・243.0・267.2・280.9・295.7・315.7・348.2・368.2・378.2・402.0
KUBUN_PCT = (4.4, 14.6, 8.2, 8.9, 12.0, 19.5, 12.0, 6.0, 14.4)
# 敷地権の表示：235.7・243.0・267.2・303.4・345.3・402.0
SHIKI_PCT = (4.4, 14.6, 21.8, 25.2, 34.0)
# 一棟の建物の表示：62.2・74.8・90.9（所在の見出し）・105.3・138.8・154.4・184.0・198.9・223.2
ITTOU_PCT = (7.8, 10.0, 8.9, 20.8, 9.7, 18.4, 9.3, 15.1)
# 敷地権の目的である土地の表示：62.2・74.8・96.4・134.4・154.4・184.0・198.9・223.2
TOCHI_PCT = (7.8, 13.4, 23.6, 12.4, 18.4, 9.3, 15.1)


def cols(pct):
    return '<colgroup>' + ''.join(f'<col style="width:{p}%">' for p in pct) + '</colgroup>'


KUBUN_COLS = cols(KUBUN_PCT)
KUBUN_HEAD = ('<tr><td class="vert" rowspan="{n}">区分した建物の表示</td><td class="head">家屋<br>番号</td>'
              '<td class="head">建物の<br>名称</td><td class="head" style="font-size:12px">主たる<br>建物又は<br>附属建物</td>'
              '<td class="head">①種類</td><td class="head">②構　造</td><td class="head" colspan="2">③床面積<br>㎡</td>'
              '<td class="head">原因及び<br>その日付</td></tr>')


def kubun_row(kaoku, kind, struct, intp, decp, genin):
    return (f'<tr><td class="e">{kaoku}</td><td class="e"></td><td class="e"></td><td class="e c">{kind}</td>'
            f'<td class="e c">{struct}</td><td class="e int">{intp}</td><td class="e dec">{decp}</td><td class="e g">{genin}</td></tr>')


def kubun_table(r0g, r1g, r2g, good=False):
    rows = (kubun_row(r(K701), r('居宅'), r(KOUZOU), r('7階部分<br>76'), ink('16'), r0g)
            + kubun_row('（イ）', '', '', ink('7階部分<br>49'), ink('22'), r1g)
            + kubun_row('（ロ）<br>' + ink(K702), ink('居宅'), ink(KOUZOU), ink('7階部分<br>25'), ink('87'), r2g))
    g = ' good' if good else ''
    return f'<table class="t{g}">{KUBUN_COLS}{KUBUN_HEAD.format(n=4)}{rows}</table>'


SHIKI_COLS = cols(SHIKI_PCT)


def shiki_table(g1, g2, good=False):
    rows = (f'<tr><td class="e c">{r("1")}</td><td class="e c">{r("所有権")}</td><td class="e c">{r("70分の5")}</td><td class="e"></td></tr>'
            f'<tr><td class="e c">（イ）<br>{ink("1")}</td><td class="e c">{ink("所有権")}</td><td class="e c">{ink("70分の3")}</td>'
            f'<td class="e g">{g1}</td></tr>'
            f'<tr><td class="e c">（ロ）<br>{ink("1")}</td><td class="e c">{ink("所有権")}</td><td class="e c">{ink("70分の2")}</td>'
            f'<td class="e g">{g2}</td></tr>')
    gg = ' good' if good else ''
    return (f'<table class="t{gg}">{SHIKI_COLS}<tr><td class="vert" rowspan="4">敷地権の表示</td><td class="head">①土地の<br>符号</td>'
            f'<td class="head">②敷地権の種類</td><td class="head">③敷地権の割合</td><td class="head">原因及びその日付</td></tr>{rows}</table>')


ITTOU = (f'<table class="t">{cols(ITTOU_PCT)}'
         f'<tr><td class="vert" rowspan="5">一棟の建物の表示</td><td class="head">所　在</td><td class="e" colspan="6">{r(SHOZAI)}</td></tr>'
         f'<tr><td class="head" colspan="2">建物の名称</td><td class="e" colspan="5">{ink(MEISHOU)}</td></tr>'
         '<tr><td class="head" colspan="2">①構　造</td><td class="head" colspan="4">②床　面　積　㎡</td><td class="head">原因及び<br>その日付</td></tr>'
         f'<tr><td class="e c" colspan="2">{RYAKU}</td><td class="e c">{RYAKU}</td><td class="e"></td><td class="e c">{RYAKU}</td>'
         '<td class="e"></td><td class="e"></td></tr>'
         '<tr><td class="note2" colspan="7">①構造・②床面積は、建物の名称を書くので記載を省略できる（不動産登記令第3条第8号ヘ）。登記記録の抜粋も「床面積（省略）」</td></tr></table>')
TOCHI = (f'<table class="t">{cols(TOCHI_PCT)}'
         '<tr><td class="vert" rowspan="2" style="font-size:14px">敷地権の目的である土地の表示</td><td class="head">①土地の符号</td>'
         '<td class="head">②所在及び地番</td><td class="head">③地目</td><td class="head" colspan="2">④地積　㎡</td>'
         '<td class="head">原因及び<br>その日付</td></tr>'
         f'<tr><td class="e c">{r("1")}</td><td class="e">{r("A市B町四丁目6番3")}</td><td class="e c">{r("宅地")}</td>'
         f'<td class="e int">{r("233")}</td><td class="e dec">{ink("75")}</td><td class="e"></td></tr></table>')

kansei = page(f"""<div class="page">
<div class="title">登記申請書</div>
{field('登記の目的', ink(MOKUTEKI))}
{field('添　付　書　類', ink(TENPU), h=96)}
<div class="date">{ink('令和８年10月18日')}　申請　　〇〇地方法務局〇〇支局</div>
{field('申　　請　　人', ink(SHINSEININ), h=86)}
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{field('登録免許税', ink(ZEI))}
{ITTOU}
{TOCHI}
<div class="colsep">ここから答案用紙の右の列</div>
{kubun_table('', ink(G701), ink(G702))}
{shiki_table(ink(G_HEN), ink(G_SHIKI))}
<div class="caption">令和8年度 土地家屋調査士試験 第22問 問2 登記申請書（区分建物区分登記）完成形<br>
A3横の答案用紙の左の列（登記申請書）の下に、右の列（区分した建物の表示・敷地権の表示）を積んだ形。
灰色の（略）は答案用紙の印刷で、その欄にも自力で解いた答えを記入した</div>
</div>""")

# ---- 添削1：申請人 ----
SH_NG = br('A市B町四丁目6番3－701号　白石恵', 'A市C町三丁目5番1号　安田結')
m_shinseinin = three(
    '申請人',
    field('申　　請　　人', ink(SH_NG), h=96),
    field('申　　請　　人', br(ink('A市B町四丁目6番3－701号　白石恵'),
                               '<span class="ink strike">A市C町三丁目5番1号　安田結</span>'), h=96)
    + '<div class="bubrow"><span class="bubble">区分の登記を申請できるのは表題部所有者か所有権の登記名義人だけ（不動産登記法第54条第1項）。<br>'
      '安田さんは売買契約をしただけで、まだ登記名義人ではない</span></div>',
    field('申　　請　　人', ink(SHINSEININ), good=True, h=96),
    '令和8年度 第22問｜702の申請人も、いまの所有権の登記名義人の白石恵さん')

# ---- 添削2：添付書類 ----
TP_NG = br('建物図面　各階平面図　登記識別情報　印鑑証明書', '規約証明書　代理権限証書')
m_tenpu = three(
    '添付書類',
    field('添　付　書　類', ink(TP_NG), h=96),
    field('添　付　書　類', br(ink('建物図面　各階平面図　') + '<span class="ink strike">登記識別情報　印鑑証明書</span>',
                              ink('規約証明書　') + '<span class="red">抵当権消滅承諾書</span>' + ink('　代理権限証書')), h=96)
    + '<div class="bubrow"><span class="bubble">区分は表示に関する登記で、登記識別情報・印鑑証明書は要らない。<br>'
      'Eタイプの1番抵当権を消すには、蓮の花銀行の承諾書が要る（法第54条第3項・第40条）</span></div>',
    field('添　付　書　類', ink(TENPU), good=True, h=96),
    '令和8年度 第22問｜要らない2つを消して、抵当権の承諾書を足す')

# ---- 添削3：登録免許税 ----
m_menkyo = three(
    '登録免許税',
    field('登録免許税', ink('不要')),
    field('登録免許税', '<span class="ink strike">不要</span>　<span class="red">金2,000円</span>')
    + '<div class="bubrow"><span class="bubble">所有権の登記がある建物の区分は課税。区分後の建物の個数×1,000円<br>'
      '（登録免許税法別表第一の一（十三）イ）。701と702の2個で2,000円</span></div>',
    field('登録免許税', ink(ZEI), good=True),
    '令和8年度 第22問｜問のただし書きの「不要」は、非課税のときの書き方の指示にすぎない')

# ---- 添削4：区分した建物の表示の原因 ----
m_genin = three(
    '区分した建物の表示',
    kubun_table(ink('6番3の701、<br>6番3の702<br>に区分'), ink(G702), ink(G702)),
    kubun_table('<span class="ink strike">6番3の701、<br>6番3の702<br>に区分</span>',
                '<span class="ink strike">6番3の701<br>から区分</span><br><span class="red">' + G701 + '</span>', ink(G702))
    + '<div class="bubrow"><span class="bubble">区分建物を区分すると、701の登記記録は残る（不動産登記規則第129条第3項・第4項）。<br>'
      '残る（イ）の行は「③702を区分」、新しくできる（ロ）の行だけが「701から区分」</span></div>',
    kubun_table('', ink(G701), ink(G702), good=True),
    '令和8年度 第22問｜非区分の建物を区分する年度（R3・H27）と、行の書き方が違う')

# ---- 添削5：敷地権の表示の原因 ----
m_shikichiken = three(
    '敷地権の表示',
    shiki_table(ink('令和8年10月18日敷地権'), ink('令和8年10月18日敷地権')),
    shiki_table('<span class="ink strike">令和8年10月18日敷地権</span><br><span class="red">' + G_HEN + '</span>',
                '<span class="ink strike">令和8年10月18日敷地権</span><br><span class="red">' + G_SHIKI + '</span>')
    + '<div class="bubrow"><span class="bubble">701は割合が70分の5から70分の3に変わっただけ → ③（割合の欄）の変更。<br>'
      '702の70分の2は、新築のときから701に付いていた敷地権を分けたもの → もともとの日付</span></div>',
    shiki_table(ink(G_HEN), ink(G_SHIKI), good=True),
    '令和8年度 第22問｜残る建物は「変更」、新しくできる建物は敷地権が生じた日')

# ---- 第1欄（問1） ----
dai1 = page(f"""<div class="page">
<div class="ranlab">第1欄</div>
<table class="t">{cols((10.4, 39.6, 10.4, 39.6))}
<tr><td class="c q1">①</td><td class="q1a"><div class="q1w">{ink('利用上')}<span class="dok">の独立性</span></div></td>
<td class="c q1">②</td><td class="q1a"><div class="q1w">{ink('構造上')}<span class="dok">の独立性</span></div></td></tr>
</table>
<div class="caption">令和8年度 土地家屋調査士試験 第22問 第1欄（問1）解答例</div></div>""")

# ---- 第4欄（問4） ----
dai4 = page(f"""<div class="page">
<div class="ranlab">第4欄</div>
<table class="t"><colgroup><col style="width:32%"><col style="width:68%"></colgroup>
<tr><td class="c q4">（ア）</td><td class="q4a">{ink('床面積')}</td></tr>
<tr><td class="c q4">（イ）</td><td class="q4a">{ink('議事録')}</td></tr>
<tr><td class="c q4">（ウ）</td><td class="q4a">{ink('合意書')}</td></tr>
</table>
<div class="caption">令和8年度 土地家屋調査士試験 第22問 第4欄（問4）解答例</div></div>""")

PAGES = [('R8_dai22mon_dai1ran_kansei', dai1), ('R8_dai22mon_dai4ran_kansei', dai4),
         ('R8_dai22mon_toukishinseisho_kansei', kansei),
         ('R8_dai22mon_toukishinseisho_machigai_shinseinin', m_shinseinin),
         ('R8_dai22mon_toukishinseisho_machigai_tenpu', m_tenpu),
         ('R8_dai22mon_toukishinseisho_machigai_menkyo', m_menkyo),
         ('R8_dai22mon_toukishinseisho_machigai_genin', m_genin),
         ('R8_dai22mon_toukishinseisho_machigai_shikichiken', m_shikichiken)]

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 200})
        for name, html in PAGES:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
        browser.close()
