"""令和4年度 第21問（土地）登記申請書の画像（完成形・添削）を、HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_R4_dai21mon_toukishinseisho_gazou.md`（基本フォーム＋記入データ）どおり。縦長（横1200px）。
  答案用紙のとおり、土地の表示の記入行は5行で、5行とも③地積を点線で整数部・小数部に分ける（「（略）」の印刷はない）
- 添削　：`../prompt_R4_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第1欄（問1のI点・J点）・第2欄（問2のア〜エ）・第5欄（問5の①〜⑤）：申請書でない解答欄も、記号ごとの記入欄の形で
  別の画像にする（横1200pxの横長。2026-10-02追加）。試験の答案用紙そのものはリポジトリにないので、欄の見出しと記号・記入欄だけの
  簡素な形（令和6年度の答案用紙の第1欄・第2欄の形にならった仮のもの）にしている

見本は `R7/Q21/zu/make_R7_dai21mon_shinseisho_gazou.py`（CSSと部品を同じ形にしている）。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（IPA明朝・IPAゴシック。Noto があればそちらを優先）
実行: python3 note-articles-Kijyutsu/R4/Q21/zu/make_R4_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 26px; line-height: 1.6; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.plain {{ font-size: 22px; margin: 4px 0 26px; }}
.dairi {{ display: flex; font-size: 22px; margin-bottom: 26px; }}
.dairi .lab {{ padding-top: 0; }}
.dairi .ryaku {{ flex: 1; text-align: center; }}
table.land {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.land td {{ border: 1.5px solid #111; font-size: 22px; padding: 6px 12px; height: 96px; vertical-align: middle;
                 white-space: nowrap; }}
table.land td.cause {{ white-space: normal; line-height: 1.45; }}
table.land td.cause .ink {{ font-size: 23px; }}
table.land td.head {{ height: 50px; text-align: center; font-size: 20px; padding: 0 6px; }}
table.land td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px;
                      white-space: nowrap; }}
table.land td.shozai-lab {{ text-align: center; height: 76px; }}
table.land td.int {{ text-align: right; border-right: 1.5px dashed #555; padding-right: 6px; }}
table.land td.dec {{ text-align: left; border-left: 1.5px dashed #555; padding-left: 6px; }}
table.land td.chimoku {{ text-align: center; }}
table.land td .ink, .box .ink {{ font-size: 26px; }}
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
table.land td .red {{ font-size: 23px; }}
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; left: 60px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: -12px 0 24px 170px; }}
.bubrow.tbl {{ margin: 14px 0 6px 60px; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.okrow {{ position: relative; }}
.check {{ position: absolute; right: -8px; top: -30px; }}
.tblwrap {{ position: relative; }}
.tblwrap .check {{ right: -14px; top: -26px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


def land_table(rows, shozai=None, n_rows=5, cls=''):
    """土地の表示の表（R4の答案用紙の形）。記入行は n_rows 行で、どの行も③地積を点線で整数部・小数部に分ける。
    rows: [(地番, 地目, 整数部, 小数部, 登記原因)]（足りない行は空欄）。shozai が None なら所在の行を描かない（添削用）"""
    h = [f'<table class="land {cls}"><colgroup><col style="width:6%"><col style="width:19%"><col style="width:12%">'
         '<col style="width:12%"><col style="width:7%"><col style="width:44%"></colgroup>']
    if shozai is not None:
        h.append(f'<tr><td class="shozai-lab" colspan="2">所　在</td><td colspan="4">{shozai}</td></tr>')
    h.append(f'<tr><td class="vert" rowspan="{n_rows + 1}">土地の表示</td><td class="head">①地　　番</td>'
             '<td class="head">②地　　目</td><td class="head" colspan="2">③地　積　（m²）</td>'
             '<td class="head">登記原因及びその日付</td></tr>')
    rows = list(rows) + [('', '', '', '', '')] * (n_rows - len(rows))
    for c, m, a, b, g in rows:
        h.append(f'<tr><td>{c}</td><td class="chimoku">{m}</td><td class="int">{a}</td><td class="dec">{b}</td>'
                 f'<td class="cause">{g}</td></tr>')
    h.append('</table>')
    return ''.join(h)


# ---- 完成形（記入データは prompt_R4_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '令和４年10月14日　申請　Ａ地方法務局'
PURPOSE = '土地一部地目変更・分筆登記'
ATTACH = '地積測量図　代理権限証書'
APPLICANT = 'Ａ市Ｃ台206番地３　春野朝子'
CAUSE_I1 = '令和４年10月５日一部地目変更'
CAUSE_I2 = '③184番１、184番３、184番４に分筆'
CAUSE_RO = '184番１から分筆'
ROW1 = (ink('184番１'), ink('宅地'), ink('584'), ink('75'), '')
ROW_I = (ink('（イ）'), '', ink('212'), ink('23'), f'{ink(CAUSE_I1)}<br>{ink(CAUSE_I2)}')
ROW_RO = (ink('（ロ）184番３'), ink('雑種地'), ink('357'), '', ink(CAUSE_RO))
ROW_HA = (ink('（ハ）184番４'), ink('宅地'), ink('15'), ink('06'), ink(CAUSE_RO))

kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="height:62px">{ink(PURPOSE)}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box" style="height:170px">{ink(ATTACH)}</div></div>
<div class="plain">{DATE}</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="height:100px">{ink(APPLICANT)}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="height:62px">{ink('金3,000円')}</div></div>
<div style="height:14px"></div>
{land_table([ROW1, ROW_I, ROW_RO, ROW_HA], shozai=ink('Ａ市Ｂ字八幡'))}
<div class="caption">令和4年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')


# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ。登記の目的と土地の表示の1〜3行目） ----
def snippet(purpose_html, rows, bubble1='', bubble2='', good=False):
    g = ' good' if good else ''
    chk = CHECK_SVG if good else ''
    return f'''<div class="row okrow"><div class="lab">登記の目的</div><div class="box{g}" style="min-height:62px">{purpose_html}</div>{chk}</div>
{f'<div class="bubrow"><span class="bubble">{bubble1}</span></div>' if bubble1 else ''}
<div class="tblwrap">{land_table(rows, n_rows=3, cls=g.strip())}{chk}</div>
{f'<div class="bubrow tbl"><span class="bubble">{bubble2}</span></div>' if bubble2 else ''}'''


ng_panel = snippet(ink('土地分筆登記'),
                   [ROW1, (ink('（イ）'), '', ink('212'), ink('23'), ink(CAUSE_I2)),
                    (ink('（ロ）184番３'), ink('宅地'), ink('357'), ink('44'), ink(CAUSE_RO))])
fix_panel = snippet(
    f'<span class="ink strike">土地分筆登記</span><br><span class="red">{PURPOSE}</span>',
    [ROW1,
     (ink('（イ）'), '', ink('212'), ink('23'), f'<span class="red">（加入）{CAUSE_I1}</span><br>{ink(CAUSE_I2)}'),
     (ink('（ロ）184番３'), f'<span class="ink strike">宅地</span><br><span class="red">雑種地</span>', ink('357'),
      '<span class="ink strike">44</span>', ink(CAUSE_RO))],
    bubble1='中央部分は10月5日から月極駐車場＝雑種地。一部地目変更も一緒に申請',
    bubble2='一部地目変更は（イ）の行に日付付きで。雑種地は1㎡未満切捨て')
ok_panel = snippet(ink(PURPOSE), [ROW1, ROW_I, ROW_RO], good=True)
machigai = page(f'''
<div class="panel"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">令和4年度 第21問｜月極駐車場になった部分は一部地目変更・分筆登記</div>''')

# ---- 申請書でない解答欄（第1欄・第2欄・第5欄。2026-10-02追加）----
RAN_CSS = (
    '* { box-sizing: border-box; margin: 0; padding: 0; }'
    'body { background: #fff; width: 1200px; font-family: "Noto Serif CJK JP", "IPAMincho", serif; color: #111; }'
    '.ran { padding: 46px 60px 26px; }'
    '.rt { font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin-bottom: 12px; }'
    'table.rz { width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; }'
    'table.rz td { border: 1.5px solid #111; height: 84px; font-size: 22px; text-align: center; vertical-align: middle; }'
    'table.rz td.head { height: 60px; font-size: 21px; }'
    'table.rz td.diag { background: linear-gradient(to top right, transparent calc(50% - 1px), #111 50%, transparent calc(50% + 1px)); }'
    f'.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 28px; }}'
    '.cap { text-align: center; font-size: 17px; color: #555; margin-top: 22px; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }')


def ran_page(title, table, caption):
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{RAN_CSS}</style></head><body>'
            f'<div class="ran"><div class="rt">{title}</div>{table}<div class="cap">{caption}</div></div></body></html>')


def zahyou_table(rows):
    """座標の欄。rows: [(点名, X, Y)]"""
    trs = ''.join(f'<tr><td>{n}</td><td>{ink(x)}</td><td>{ink(y)}</td></tr>' for n, x, y in rows)
    return ('<table class="rz"><colgroup><col style="width:30%"><col style="width:35%"><col style="width:35%"></colgroup>'
            '<tr><td class="head diag"></td><td class="head">Ｘ座標（ｍ）</td><td class="head">Ｙ座標（ｍ）</td></tr>'
            f'{trs}</table>')


def anaume_table(items):
    """穴埋めの欄。記号と記入欄を2組ずつ横に並べる。items: [(記号, 答え)]"""
    trs = ''
    for k in range(0, len(items), 2):
        pair = items[k:k + 2]
        tds = ''.join(f'<td>{m}</td><td>{ink(a)}</td>' for m, a in pair)
        if len(pair) == 1:
            tds += '<td></td><td></td>'
        trs += f'<tr>{tds}</tr>'
    return ('<table class="rz"><colgroup><col style="width:8%"><col style="width:42%"><col style="width:8%">'
            f'<col style="width:42%"></colgroup>{trs}</table>')


DAI1 = [('Ｉ点', '300.13', '293.12'), ('Ｊ点', '279.30', '293.12')]
DAI2 = [('ア', '表題登記'), ('イ', '隣接'), ('ウ', '位置'), ('エ', '範囲')]
DAI5 = [('①', '日時'), ('②', '場所'), ('③', 'その状況'), ('④', '申請の権限'), ('⑤', '登記名義人')]
dai1 = ran_page('第1欄　Ｉ点及びＪ点の座標値', zahyou_table(DAI1), '令和4年度 土地家屋調査士試験 第21問 第1欄（問1）解答例')
dai2 = ran_page('第2欄　筆界特定の定義（ア〜エ）', anaume_table(DAI2), '令和4年度 土地家屋調査士試験 第21問 第2欄（問2）解答例')
dai5 = ran_page('第5欄　本人確認情報（①〜⑤）', anaume_table(DAI5), '令和4年度 土地家屋調査士試験 第21問 第5欄（問5）解答例（①〜③は順不同）')

if __name__ == '__main__':
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
        pg = browser.new_page(viewport={'width': 1200, 'height': 100})
        for name, html in [('R4_dai21mon_toukishinseisho_kansei', kansei),
                           ('R4_dai21mon_toukishinseisho_machigai', machigai),
                           ('R4_dai21mon_dai1ran_kansei', dai1), ('R4_dai21mon_dai2ran_kansei', dai2),
                           ('R4_dai21mon_dai5ran_kansei', dai5)]:
            hp = os.path.join(OUT, name + '.html')
            open(hp, 'w', encoding='utf-8').write(html)
            pg.set_content(html)
            pg.wait_for_timeout(300)
            png = os.path.join(OUT, name + '.png')
            pg.screenshot(path=png, full_page=True)
            w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
            print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
        browser.close()
