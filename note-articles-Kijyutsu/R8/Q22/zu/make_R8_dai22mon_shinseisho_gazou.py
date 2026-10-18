"""令和8年度 第22問（建物）の答案の画像（第1欄・第4欄・登記申請書の完成形、欄ごとの添削5枚）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 答案用紙の形式はまだ発表されていない（2026-10-18現在）。欄の形・順序は、区分建物区分登記を書かせた令和3年度・
  敷地権のある区分の年度（H20・H27）の答案用紙にならった「仮」の形。発表されたら、この形を答案用紙どおりに直す
- 完成形：`../prompt_R8_dai22mon_toukishinseisho_gazou.md` の記入データどおり。縦長（横1200px）
- 添削　：`../prompt_R8_dai22mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）。
  誤答の欄ごとに1枚（申請人・添付書類・登録免許税・区分した建物の表示の原因・敷地権の表示の原因）
- 第1欄（問1）・第4欄（問4）：申請書でない解答欄も、記入欄の形で別の画像にする

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
table.t td {{ border: 1.5px solid #111; font-size: 19px; padding: 8px 10px; vertical-align: middle; line-height: 1.5; }}
table.t td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.12em; padding: 0 4px; font-size: 19px; }}
table.t td.head {{ text-align: center; font-size: 18px; height: 60px; }}
table.t td.e {{ height: 92px; }}
table.t td.c {{ text-align: center; }}
table.t td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 4px; white-space: nowrap; }}
table.t td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 4px; }}
table.t td .ink {{ font-size: 20px; }}
table.t td.g .ink {{ font-size: 18px; }}
.note {{ font-family: {SANS}; font-size: 16px; color: #555; margin: -16px 0 22px; }}
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
TENPU = br('建物図面　各階平面図　規約証明書', '抵当権消滅承諾証明書　代理権限証書')
SHINSEININ = br('A市B町四丁目6番3-701号', '白　石　　恵')
ZEI = '金2,000円'
SHOZAI = 'A市B町四丁目6番地3'
MEISHOU = 'WKマンション'
K701 = 'B町四丁目6番3の701'
K702 = 'B町四丁目6番3の702'
KOUZOU = '鉄筋コンクリート造1階建'
G701 = '③6番3の701、6番3の702に区分'
G702 = '6番3の701から区分'
G_SHIKI = '平成12年6月17日敷地権'

KUBUN_COLS = ('<colgroup><col style="width:5%"><col style="width:21%"><col style="width:9%"><col style="width:21%">'
              '<col style="width:13%"><col style="width:6%"><col style="width:25%"></colgroup>')
KUBUN_HEAD = ('<tr><td class="vert" rowspan="{n}">区分した建物の表示</td><td class="head">家屋番号</td><td class="head">①種類</td>'
              '<td class="head">②構造</td><td class="head" colspan="2">③床面積（㎡）</td>'
              '<td class="head">登記原因及びその日付</td></tr>')


def kubun_row(kaoku, kind, struct, intp, decp, genin):
    return (f'<tr><td class="e">{kaoku}</td><td class="e c">{kind}</td><td class="e c">{struct}</td>'
            f'<td class="e int">{intp}</td><td class="e dec">{decp}</td><td class="e g">{genin}</td></tr>')


def kubun_table(r1g, r2g, r3g, good=False):
    rows = (kubun_row(ink(K701), ink('居宅'), ink(KOUZOU), ink('7階部分　76'), ink('16'), r1g)
            + kubun_row(ink(K701), '', '', ink('7階部分　49'), ink('22'), r2g)
            + kubun_row(ink(K702), ink('居宅'), ink(KOUZOU), ink('7階部分　25'), ink('87'), r3g))
    g = ' good' if good else ''
    return f'<table class="t{g}">{KUBUN_COLS}{KUBUN_HEAD.format(n=4)}{rows}</table>'


SHIKI_COLS = ('<colgroup><col style="width:5%"><col style="width:21%"><col style="width:13%"><col style="width:17%">'
              '<col style="width:17%"><col style="width:27%"></colgroup>')


def shiki_table(g1, g2, good=False):
    rows = ''.join(f'<tr><td class="e">{ink(k)}</td><td class="e c">{ink("1")}</td><td class="e c">{ink("所有権")}</td>'
                   f'<td class="e c">{ink(w)}</td><td class="e g">{g}</td></tr>'
                   for k, w, g in [(K701, '70分の3', g1), (K702, '70分の2', g2)])
    gg = ' good' if good else ''
    return (f'<table class="t{gg}">{SHIKI_COLS}<tr><td class="vert" rowspan="3">敷地権の表示</td><td class="head">区分した建物</td>'
            f'<td class="head">①土地の符号</td><td class="head">②敷地権の種類</td><td class="head">③敷地権の割合</td>'
            f'<td class="head">登記原因及びその日付</td></tr>{rows}</table>')


ITTOU = ('<table class="t"><colgroup><col style="width:5%"><col style="width:16%"><col style="width:79%"></colgroup>'
         f'<tr><td class="vert" rowspan="4">一棟の建物の表示</td><td class="head">所　在</td><td class="e">{ink(SHOZAI)}</td></tr>'
         f'<tr><td class="head">建物の名称</td><td class="e">{ink(MEISHOU)}</td></tr>'
         '<tr><td class="head">①構造</td><td class="e"></td></tr>'
         '<tr><td class="head">②床面積</td><td class="e"></td></tr></table>'
         '<div class="note">①構造・②床面積は、建物の名称を書くので記載を省略できる（不動産登記令第3条第8号ヘ）。登記記録の抜粋も「床面積（省略）」</div>')
TOCHI = ('<table class="t"><colgroup><col style="width:5%"><col style="width:13%"><col style="width:36%"><col style="width:12%">'
         '<col style="width:12%"><col style="width:6%"><col style="width:16%"></colgroup>'
         '<tr><td class="vert" rowspan="2" style="font-size:15px">敷地権の目的<br>である土地</td><td class="head">①土地の符号</td>'
         '<td class="head">②所在及び地番</td><td class="head">③地目</td><td class="head" colspan="2">④地積（㎡）</td>'
         '<td class="head">登記原因及び<br>その日付</td></tr>'
         f'<tr><td class="e c">{ink("1")}</td><td class="e">{ink("A市B町四丁目6番3")}</td><td class="e c">{ink("宅地")}</td>'
         f'<td class="e int">{ink("233")}</td><td class="e dec">{ink("75")}</td><td class="e"></td></tr></table>')

kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
{field('登記の目的', ink(MOKUTEKI))}
{field('添　付　書　類', ink(TENPU), h=110)}
<div class="date">{ink('令和８年10月18日')}申請　　（略）法務局</div>
{field('申　　請　　人', ink(SHINSEININ), h=110)}
<div class="plainrow"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
{field('登録免許税', ink(ZEI))}
{ITTOU}
{TOCHI}
{kubun_table('', ink(G701), ink(G702))}
{shiki_table(ink(G_SHIKI), ink(G_SHIKI))}
<div class="caption">令和8年度 土地家屋調査士試験 第22問 問2 登記申請書（区分建物区分登記）完成形<br>
答案用紙の形式は未発表のため、欄の形は過去の年度にならった仮の形</div>
</div>''')

# ---- 添削1：申請人 ----
SH_NG = br('A市B町四丁目6番3-701号　白石　恵', 'A市C町三丁目5番1号　安田　結')
m_shinseinin = three(
    '申請人',
    field('申　　請　　人', ink(SH_NG), h=110),
    field('申　　請　　人', br(ink('A市B町四丁目6番3-701号　白石　恵'),
                               '<span class="ink strike">A市C町三丁目5番1号　安田　結</span>'), h=110)
    + '<div class="bubrow"><span class="bubble">区分の登記を申請できるのは表題部所有者か所有権の登記名義人だけ（不動産登記法第54条第1項）。<br>'
      '安田さんは売買契約をしただけで、まだ登記名義人ではない</span></div>',
    field('申　　請　　人', ink(SHINSEININ), good=True, h=110),
    '令和8年度 第22問｜702の申請人も、いまの所有権の登記名義人の白石恵さん')

# ---- 添削2：添付書類 ----
TP_NG = br('建物図面　各階平面図　登記識別情報　印鑑証明書', '規約証明書　代理権限証書')
m_tenpu = three(
    '添付書類',
    field('添　付　書　類', ink(TP_NG), h=110),
    field('添　付　書　類', br(ink('建物図面　各階平面図　') + '<span class="ink strike">登記識別情報　印鑑証明書</span>',
                              ink('規約証明書　') + '<span class="red">抵当権消滅承諾証明書</span>' + ink('　代理権限証書')), h=110)
    + '<div class="bubrow"><span class="bubble">区分は表示に関する登記で、登記識別情報・印鑑証明書は要らない。<br>'
      'Eタイプの1番抵当権を消すには、蓮の花銀行の承諾書が要る（法第54条第3項・第40条）</span></div>',
    field('添　付　書　類', ink(TENPU), good=True, h=110),
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
    kubun_table(ink('6番3の701、6番3の702に区分'), ink(G702), ink(G702)),
    kubun_table('<span class="ink strike">6番3の701、6番3の702に区分</span>',
                '<span class="ink strike">6番3の701から区分</span><br><span class="red">' + G701 + '</span>', ink(G702))
    + '<div class="bubrow"><span class="bubble">区分建物を区分すると、701の登記記録は残る（不動産登記規則第129条第3項・第4項）。<br>'
      '新しくできるのは702だけ。701は床面積が変わるので③を付けて「に区分」</span></div>',
    kubun_table('', ink(G701), ink(G702), good=True),
    '令和8年度 第22問｜非区分の建物を区分する年度（R3・H27）と、行の書き方が違う')

# ---- 添削5：敷地権の表示の原因 ----
m_shikichiken = three(
    '敷地権の表示',
    shiki_table(ink('令和8年10月18日敷地権'), ink('令和8年10月18日敷地権')),
    shiki_table('<span class="ink strike">令和8年10月18日敷地権</span><br><span class="red">' + G_SHIKI + '</span>',
                '<span class="ink strike">令和8年10月18日敷地権</span><br><span class="red">' + G_SHIKI + '</span>')
    + '<div class="bubrow"><span class="bubble">敷地権は区分で生まれたのではなく、新築のときから701に付いていた。<br>'
      '702の70分の2も、その一部を分けたもの。日付は敷地権が生じた平成12年6月17日のまま</span></div>',
    shiki_table(ink(G_SHIKI), ink(G_SHIKI), good=True),
    '令和8年度 第22問｜区分の原因に日付はないが、敷地権の原因には日付がある')

# ---- 第1欄（問1） ----
dai1 = page(f'''<div class="page">
<div style="font-size:28px;font-weight:bold;font-family:{SANS};margin-bottom:16px">第1欄</div>
<table class="t"><colgroup><col style="width:22%"><col style="width:78%"></colgroup>
<tr><td class="c" style="height:150px;font-size:22px">構造上の独立性</td><td style="font-size:22px">{ink('建物の構成部分である壁、床、天井などによって、他の部分と遮断されていること。')}</td></tr>
<tr><td class="c" style="height:150px;font-size:22px">利用上の独立性</td><td style="font-size:22px">{ink('その部分だけで独立して住居などの建物としての用途に供することができること（外部に直接出入りできること）。')}</td></tr>
</table>
<div class="caption">令和8年度 土地家屋調査士試験 第22問 第1欄（問1）解答例｜答案用紙の形式は未発表のため仮の形</div></div>''')

# ---- 第4欄（問4） ----
dai4 = page(f'''<div class="page">
<div style="font-size:28px;font-weight:bold;font-family:{SANS};margin-bottom:16px">第4欄</div>
<table class="t"><colgroup><col style="width:12%"><col style="width:38%"><col style="width:12%"><col style="width:38%"></colgroup>
<tr><td class="c" style="height:84px;font-size:26px">ア</td><td style="font-size:26px">{ink('床面積')}</td>
<td class="c" style="font-size:26px">イ</td><td style="font-size:26px">{ink('議事録')}</td></tr>
<tr><td class="c" style="height:84px;font-size:26px">ウ</td><td style="font-size:26px" colspan="3">{ink('書面による合意')}</td></tr>
</table>
<div class="caption">令和8年度 土地家屋調査士試験 第22問 第4欄（問4）解答例｜答案用紙の形式は未発表のため仮の形</div></div>''')

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
