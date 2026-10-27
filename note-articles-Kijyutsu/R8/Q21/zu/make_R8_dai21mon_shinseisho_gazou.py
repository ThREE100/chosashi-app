"""令和8年度 第21問（土地）登記申請書の画像（完成形・添削）と、申請書でない解答欄（第1欄・第2欄・第4欄）の画像を、
HTML＋ヘッドレスブラウザでPNGに書き出す。

- 完成形：`../prompt_R8_dai21mon_toukishinseisho_gazou.md` どおり（問3・令和8年8月20日の土地分合筆登記）。縦長（横1200px）
- 添削　：`../prompt_R8_dai21mon_toukishinseisho_machigai.md` どおり。①誤答・②添削・③正解の3コマを縦に積んだ縦長（横1200px）
- 第1欄（問1のア〜エ）・第2欄（問2のK点）・第4欄（問4のC点）：申請書でない解答欄を別の画像にする（横1200px）
- 欄の形・順序・印刷文字は、アガルートの解答例（2026-10-20受領、答案用紙を再現したもの）どおり：第3欄の申請書は
  登記の目的・添付書類・記号欄（小さな枠）・「令和８年８月20日　申請　Ａ地方法務局」・申請人・代理人（略）・登録免許税の順。
  土地の表示は記入行6行、見出しは「③地　積（㎡）」。列幅は解答例の画像の縦の罫線から測った比
  （縦書き6・地番16・地目16・地積21〈整数部14・小数部7〉・原因41）
- 解答例は（イ）の行と合筆後の行の地目を空欄にしているが、完成形の画像は自分で解いたときの記入（宅地）のままにした（ユーザー指示）
  記号欄は解答例どおり「イ，エ」

R5/Q21の `make_R5_dai21mon_shinseisho_gazou.py` の様式（CSS・土地の表示の表）を使った。
必要なもの：Python の playwright、Chromium（/opt/pw-browsers）、日本語フォント（Noto Serif/Sans CJK JP。なければIPA明朝・IPAゴシック）
実行: python3 note-articles-Kijyutsu/R8/Q21/zu/make_R8_dai21mon_shinseisho_gazou.py [出力フォルダ]
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
.box {{ flex: 1; border: 2px solid #111; padding: 10px 16px; font-size: 26px; }}
.ink {{ color: {INK}; font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.plain {{ font-size: 22px; margin: 4px 0 26px; }}
.dairi {{ display: flex; font-size: 22px; margin-bottom: 26px; }}
.dairi .lab {{ padding-top: 0; }}
.dairi .ryaku {{ flex: 1; text-align: center; }}
table.land {{ width: 100%; border-collapse: collapse; border: 3px solid #111; table-layout: fixed; }}
table.land td {{ border: 1.5px solid #111; font-size: 22px; padding: 0 12px; height: 132px; vertical-align: middle; }}
table.land.compact td.vert {{ letter-spacing: 0.05em; font-size: 18px; }}
.box.fix {{ line-height: 1.75; }}
table.land td.head {{ height: 46px; text-align: center; font-size: 20px; }}
table.land td.vert {{ writing-mode: vertical-rl; text-align: center; letter-spacing: 0.9em; padding: 0; font-size: 22px; }}
table.land td.shozai-lab {{ text-align: center; height: 100px; }}
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
.bubble {{ display: inline-block; position: relative; border: 2.5px solid {RED}; border-radius: 14px;
           padding: 8px 18px; color: {RED}; font-size: 22px; font-weight: bold; background: #fff5f5;
           font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; }}
.bubble::before {{ content: ""; position: absolute; top: -16px; left: 60px; border: 8px solid transparent;
                   border-bottom: 8px solid {RED}; }}
.bubrow {{ margin: -12px 0 20px 170px; }}
.bubrow.table {{ margin: 14px 0 0 480px; }}
.bubrow.table2 {{ margin: 18px 0 0 0; }}
.good {{ outline: 3px solid {GREEN}; outline-offset: 4px; border-radius: 2px; background: #f1faf2; }}
.okrow {{ position: relative; }}
.check {{ position: absolute; right: -8px; top: -30px; }}
'''

CHECK_SVG = (f'<svg class="check" width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="#fff" '
             f'stroke="{GREEN}" stroke-width="3"/><path d="M11 23 L19 31 L33 14" fill="none" stroke="{GREEN}" '
             f'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


LAND_COLS_PCT = [5.88, 12.96, 2.96, 15.88, 14.17, 7.06, 41.09]   # 合計100（原本の罫線から）


def land_table(rows, n_rows=6, shozai='Ｍ市Ａ町二丁目', compact=False):
    """土地の表示の表。rows: [(地番, 地目, 整数部, 小数部, 登記原因)]。各値は HTML（記入部分は呼び出し側で .ink を付ける）"""
    # 列の幅と行の高さは、解答例のPDF（ベクター）の罫線を pymupdf の get_drawings で測った値（2026-10-26）。
    # 表の外枠 x 684.6〜1140.6pt、縦の罫線 711.4・770.5（所在の欄だけ）・784.0・856.4・921.0（点線）・953.2。
    # 行の高さは 所在 43.1pt・見出し 19.8pt・記入行 56.7pt × 6。画像の表の幅 1060px ÷ 456pt ＝ 2.325px/pt
    cols = ''.join(f'<col style="width:{w}%">' for w in LAND_COLS_PCT)
    h = [f'<table class="land{" compact" if compact else ""}"><colgroup>{cols}</colgroup>',
         f'<tr><td class="shozai-lab" colspan="2">所　在</td><td colspan="5">{shozai}</td></tr>',
         f'<tr><td class="vert" rowspan="{n_rows + 1}">土地の表示</td><td class="head" colspan="2">①地　　番</td>'
         '<td class="head">②地　　目</td><td class="head" colspan="2">③地　　積（㎡）</td>'
         '<td class="head">登記原因及びその日付</td></tr>']
    for i in range(n_rows):
        c, m, a, b, g = rows[i] if i < len(rows) else ('', '', '', '', '')
        h.append(f'<tr><td colspan="2">{c}</td><td class="chimoku">{m}</td><td class="int">{a}</td><td class="dec">{b}</td>'
                 f'<td>{g}</td></tr>')
    h.append('</table>')
    return ''.join(h)


def ink(s):
    return f'<span class="ink">{s}</span>' if s else ''


def page(body):
    return f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


# ---- 完成形（記入データは prompt_R8_dai21mon_toukishinseisho_gazou.md のとおり） ----
DATE = '令和８年８月20日　申請　Ａ地方法務局'
PURPOSE = '土地分合筆登記'
ATTACH = '地積測量図　登記識別情報　印鑑証明書　代理権限証書'
KIGOU = 'イ，エ'
APPLICANT = 'Ｍ市Ａ町二丁目２番19号　佐藤佑介'
TAX = '金2,000円'
SHOZAI = 'Ｍ市Ａ町二丁目'
ROWS = [('２番19', '宅地', '413', '30', ''),
        ('(イ)２番19', '宅地', '392', '17', '③２番42に一部合併'),
        ('(ロ)', '', '21', '15', '２番19から分割して２番42に合併する部分'),
        ('２番42', '宅地', '344', '84', ''),
        ('２番42', '宅地', '365', '99', '③２番19から一部合併')]
kansei = page(f'''<div class="page">
<div class="title">登記申請書</div>
<div class="row"><div class="lab">登記の目的</div><div class="box" style="min-height:62px">{ink(PURPOSE)}</div></div>
<div class="row"><div class="lab">添　付　書　類</div><div class="box fix" style="min-height:130px">{ink(ATTACH)}</div></div>
<div class="row"><div class="lab" style="padding-left:150px;width:420px">記　号　欄</div><div class="box" style="min-height:62px;flex:0 0 300px;text-align:center">{ink(KIGOU)}</div></div>
<div class="plain">{DATE}</div>
<div class="row"><div class="lab">申　　請　　人</div><div class="box" style="min-height:96px">{ink(APPLICANT)}</div></div>
<div class="dairi"><div class="lab">代　　理　　人</div><div class="ryaku">（略）</div></div>
<div class="row"><div class="lab">登録免許税</div><div class="box" style="min-height:62px">{ink(TAX)}</div></div>
<div style="margin-top:14px"></div>
{land_table([tuple(ink(v) for v in r) for r in ROWS], shozai=ink(SHOZAI))}
<div class="caption">令和8年度 土地家屋調査士試験 第21問 登記申請書 解答例</div>
</div>''')

# ---- 添削（①誤答 → ②添削 → ③正解 を縦に3コマ。添付書類の欄だけ） ----
WRONG_ATTACH = '地積測量図　登記識別情報　代理権限証書'


def snippet(attach_html, bubble='', good=False):
    chk = CHECK_SVG if good else ''
    return (f'<div class="row okrow"><div class="lab">添　付　書　類</div><div class="box fix{" good" if good else ""}" '
            f'style="min-height:96px">{attach_html}</div>{chk}</div>'
            + (f'<div class="bubrow"><span class="bubble">{bubble}</span></div>' if bubble else ''))


ng_panel = snippet(ink(WRONG_ATTACH))
fix_panel = snippet(f'{ink(WRONG_ATTACH)}<span class="red">　印鑑証明書</span>',
                    bubble='分合筆も合筆。委任状に記名押印して印鑑証明書（令第18条）')
ok_panel = snippet(ink(ATTACH), good=True)
machigai = page(f'''
<div class="panel" style="min-height:420px"><div class="ptitle ng">①誤答</div>{ng_panel}</div>
<div class="panel" style="min-height:420px"><div class="ptitle fix">②添削（赤ペン）</div>{fix_panel}</div>
<div class="panel" style="min-height:420px"><div class="ptitle ok">③正解</div>{ok_panel}</div>
<div class="caption" style="margin:10px 0 30px">令和8年度 第21問｜分合筆（合筆）の添付書類に印鑑証明書を忘れない</div>''')
# ---- 第1欄（申請書でない解答欄。解答例に再現された答案用紙の第1欄の形） ----
RAN_CSS = '''
.ranpage { padding: 50px 60px 34px; }
.ranhead { font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin-bottom: 14px; }
table.ran { width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; }
table.ran td { border: 1.5px solid #111; height: 84px; font-size: 22px; vertical-align: middle; }
table.ran td.k { text-align: center; }
table.ran td.v { padding-left: 22px; }
table.ran td.v .ink { font-size: 28px; }
'''


def ran_image(head, pairs, caption):
    """記号と記入欄を1行に2組ずつ並べた穴埋めの欄（解答例に再現された答案用紙の第1欄の形）"""
    trs = ''
    for i in range(0, len(pairs), 2):
        cells = ''.join(f'<td class="k">{k}</td><td class="v">{ink(v)}</td>' for k, v in pairs[i:i + 2])
        trs += f'<tr>{cells}</tr>'
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}{RAN_CSS}</style></head><body>'
            f'<div class="ranpage"><div class="ranhead">{head}</div>'
            f'<table class="ran"><colgroup><col style="width:10%"><col style="width:40%"><col style="width:10%">'
            f'<col style="width:40%"></colgroup>{trs}</table>'
            f'<div class="caption">{caption}</div></div></body></html>')


DAI1 = [('ア', '登記名義人'), ('イ', '運転免許証'), ('ウ', '個人番号カード'), ('エ', '旅券等')]
dai1 = ran_image('第1欄', DAI1, '令和8年度 土地家屋調査士試験 第21問 第1欄（問1）解答例')


# ---- 座標の欄（申請書でない解答欄。2026-10-02追加。解答例に再現された答案用紙の第2欄・第4欄の形：左上の斜線の欄・X座標（m）・Y座標（m）、3列等幅） ----
Z_CSS = '''
.ranpage { padding: 50px 60px 34px; }
.ranhead { font-family: "Noto Sans CJK JP", "IPAGothic", sans-serif; font-size: 26px; font-weight: bold; margin: 0 0 14px; }
table.zh { width: 100%; border-collapse: collapse; border: 2.5px solid #111; table-layout: fixed; }
table.zh td { border: 1.5px solid #111; height: 72px; font-size: 22px; text-align: center; vertical-align: middle; }
table.zh td.diag { background: linear-gradient(to top right, transparent calc(50% - 1px), #111 50%, transparent calc(50% + 1px)); }
table.zh td .ink { font-size: 28px; }
'''


def zahyou(head, rows, caption):
    """rows: [(点名, X, Y)]"""
    trs = ''.join(f'<tr><td>{n}</td><td>{ink(x)}</td><td>{ink(y)}</td></tr>' for n, x, y in rows)
    return (f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>{CSS}{Z_CSS}</style></head><body>'
            f'<div class="ranpage"><div class="ranhead">{head}</div><table class="zh"><colgroup><col style="width:33.3%">'
            f'<col style="width:33.35%"><col style="width:33.35%"></colgroup>'
            f'<tr><td class="diag"></td><td>Ｘ座標（m）</td><td>Ｙ座標（m）</td></tr>{trs}</table>'
            f'<div class="caption">{caption}</div></div></body></html>')


dai2 = zahyou('第2欄', [('Ｋ点', '506.23', '492.18')],
               '令和8年度 土地家屋調査士試験 第21問 第2欄（問2）解答例')
dai4 = zahyou('第4欄', [('Ｃ点', '510.78', '506.79')],
               '令和8年度 土地家屋調査士試験 第21問 第4欄（問4）解答例')

exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe[-1] if exe else None)
    pg = browser.new_page(viewport={'width': 1200, 'height': 200})
    for name, html in [('R8_dai21mon_dai1ran_kansei', dai1), ('R8_dai21mon_dai2ran_kansei', dai2), ('R8_dai21mon_toukishinseisho_kansei', kansei),
                       ('R8_dai21mon_toukishinseisho_machigai', machigai), ('R8_dai21mon_dai4ran_kansei', dai4)]:
        hp = os.path.join(OUT, name + '.html')
        open(hp, 'w', encoding='utf-8').write(html)
        pg.set_content(html)
        pg.wait_for_timeout(300)
        png = os.path.join(OUT, name + '.png')
        pg.screenshot(path=png, full_page=True)
        w, h = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.scrollHeight]')
        print(f'{png}  {w}×{h}px  ' + ('縦長' if h > w else '横長'))
    browser.close()
