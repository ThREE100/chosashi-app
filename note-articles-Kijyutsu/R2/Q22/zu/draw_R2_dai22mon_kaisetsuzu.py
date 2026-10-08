"""令和2年度 第22問（建物）の解説図15枚を、座標値・頂点座標から作図してPNGに書き出す。

`../prompt_R2_dai22mon_kaisetsuzu.md` の図1〜図15どおり（番号は記事の挿入順。2026-10-08に図を7枚足して振り直した）。作図の共通部品は `tools/zu_helpers.py`。
図7（建物図面）と図11（問4の完成形）は、答案用紙の第4欄の欄（家屋番号・建物の所在・申請人・作成者・縮尺）の形の枠の中に描く。
欄の形は試験の答案用紙（`../touan_youshi/R2_dai22mon_touan_youshi.pdf` の2ページ目）で確かめた：第4欄はA3横の1枚の枠の左半分が各階平面図、
右半分が建物図面（中央の上下に短い仕切りの線）。建物図面の上に「家屋番号（略）」の箱が枠の外に、「建物の所在」の記入欄が枠の中の上端にあり、
下に「申請人（略）」「縮尺 1/500」。各階平面図の下に「作成者（略）（令和2年○月○日作成）」「縮尺 1/250」。縮尺は分数の形で印刷。
敷地は〔調査図〕の〔座標一覧表〕の (X, Y)＝(北, 東) をそのまま使う。
本件新建物の各階は (東, 南) で持ち（原点は壁の中心線で囲んだ建物の北西の角）、zu_helpers の (北, 東) には B() で変換する。
図1の旧建物3棟の形・位置だけは、〔調査図〕と【建物図面】の図から読み取った模式（寸法は目安）。
実行: python3 note-articles-Kijyutsu/R2/Q22/zu/draw_R2_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN)  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []


def B(e, s):
    """建物の (東, 南) を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(-s, e)


def rect(e0, s0, e1, s1):
    return [B(e0, s0), B(e1, s0), B(e1, s1), B(e0, s1)]


def srect(y0, x0, y1, x1):
    """敷地の座標で、Y（東）y0〜y1・X（北）x0〜x1 の長方形。"""
    return [complex(x1, y0), complex(x1, y1), complex(x0, y1), complex(x0, y0)]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


def hatch(ax, pts, color=GRAY):
    ax.add_patch(MPoly([xy(p) for p in pts], closed=True, fill=False, hatch='///', edgecolor=color, lw=0, zorder=1))


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def dim_line(z, p, q, text, color=BLACK, ls='-', dirs=None, offsets=None, fs=15):
    """寸法線（両矢印）と数値。短くて文字が入らない寸法は dirs を指定して引き出し線で外に書く。"""
    z.ax.annotate('', xy=xy(q), xytext=xy(p),
                  arrowprops=dict(arrowstyle='<->', lw=1.6, color=color, ls=ls, shrinkA=0, shrinkB=0), zorder=4)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    if dirs:
        return z.callout(m, text, dirs=dirs, fs=fs - 1, dists=(40, 55, 70, 90, 110, 130, 150), color=color)
    return z.free_text(m, text, fs=fs, color=color, offsets=offsets or ((16, 0), (-16, 0), (0, 14), (0, -14)))


# ---- 本件新建物（〔平面図〕。外壁の外側の測定値から、壁の中心線は0.05内側＝〔平面図〕の（注）3・（注）5） ----
F12 = rect(0, 0, 11.9, 6.0)                      # 1階・2階（各階同型）
PORCH = rect(0, 0, 1.5, 3.5)                     # 北西の旧ポーチ（10月12日にエントランスへ）
OUTER = rect(-0.05, -0.05, 11.95, 6.05)          # 外壁の外側の線 12.00×6.10
F3 = [B(0, 0), B(11.9, 0), B(11.9, 6.0), B(4.1, 6.0), B(4.1, 4.2), B(0, 4.2)]
W3 = rect(0, 0, 4.1, 4.2)                        # 3階 西の列（LDK）
E3 = rect(4.1, 0, 11.9, 6.0)                     # 3階 東の列
W3_NG = rect(0, 0, 4.0, 4.2)                     # 藍子：全部から0.10引いた西の列
GAP = rect(4.0, 0, 4.1, 4.2)                     # 抜け落ちた帯 0.10×4.20
SW_OUT = rect(0, 4.2, 4.1, 6.0)                  # 3階の南西の屋外部分（バルコニーとつながる）
BAL_S = rect(0, 6.0, 11.9, 6.9)                  # 南のバルコニー（奥行き0.90。模式）

assert round(area(F12), 2) == 71.40 and round(area(OUTER), 2) == 73.20 and round(area(PORCH), 2) == 5.25
assert round(area(F12) - area(PORCH), 2) == 66.15
assert round(area(F3), 2) == 64.02 == round(area(W3) + area(E3), 2)
assert round(area(W3), 2) == 17.22 and round(area(E3), 2) == 46.80
assert round(area(W3_NG) + area(E3), 2) == 63.60 and round(area(GAP), 2) == 0.42

# ---- 敷地（〔座標一覧表〕。X＝北、Y＝東） ----
PT = {'A': complex(46.6, 0), 'B': complex(46.6, 19.2), 'C': complex(0, 0), 'D': complex(0, 19.2),
      'E': complex(-11.2, 0), 'F': complex(-11.2, 19.2), 'G': complex(-17.4, 0), 'H': complex(-17.4, 19.2),
      'I': complex(-19.9, 0), 'J': complex(-19.9, 19.2)}
SOUTH, NORTH, WEST, EAST = -19.9 + 3.2, -19.9 + 3.2 + 6.1, 3.9, 3.9 + 12.0
SITE_BLDG = srect(WEST, SOUTH, EAST, NORTH)     # 本件新建物の1階の外形（外壁の外側）
assert (round(SOUTH, 2), round(NORTH, 2), round(EAST, 2)) == (-16.7, -10.6, 15.9)
assert round(area(SITE_BLDG), 2) == 73.20
assert round(SOUTH - PT['G'].real, 2) == 0.70 and round(NORTH - PT['E'].real, 2) == 0.60


# ---- 図1：取り壊した建物（本件旧建物）の家屋番号の特定図（模式図） ----
def px_cho(x, y):
    """〔調査図〕の図の画素位置を、座標（北, 東）の目安に換算する（A・B・C点の位置から縮尺を出した模式）。"""
    return complex(46.6 - (y - 300) / 14.5, (x - 490) / 14.43)


def zu01():
    fig, axes = new_figure('取り壊した建物（本件旧建物）の家屋番号の特定（模式図）',
                           '39番3の2と39番3の4は最初の登記記録が同じ → 建物図面の形と位置を〔調査図〕の現存建物と見比べて特定する',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    lot = [PT['A'], PT['B'], PT['D'], PT['C']]
    z.poly(lot, color=BLACK, lw=2.4, fill=GRAY, alpha=0.06)
    sq = [px_cho(574, 332), px_cho(705, 332), px_cho(705, 437), px_cho(574, 437)]
    step = [px_cho(x, y) for x, y in [(594, 482), (606, 468), (725, 468), (725, 628), (698, 628), (698, 634),
                                        (580, 634), (580, 576), (634, 576), (634, 521), (594, 521)]]
    fuzoku = srect(11.2, 13.1, 16.6, 22.2)          # 39番3の4の附属建物（車庫）：【建物図面】39番3の4から読んだ模式
    shu = srect(7.6, 1.9, 16.6, 11.3)                # 39番3の4の主である建物
    z.poly(sq, color=BLUE, lw=2.2, fill=BLUE, alpha=0.25)
    z.poly(step, color=GREEN, lw=2.2, fill=GREEN, alpha=0.25)
    z.poly(fuzoku, color=RED, lw=2.0, ls='--')
    z.poly(shu, color=RED, lw=2.0, ls='--')
    for bx in (fuzoku, shu):   # バツ印（2本の線）
        z.line(bx[0], bx[2], color=RED, lw=2.4, check=False)
        z.line(bx[1], bx[3], color=RED, lw=2.4, check=False)
    fit(ax, lot, margin=0.05, extra=[(-14, 20), (52, 20), (9.6, 51.5), (9.6, -5.5)], pad_aspect=True)
    z.north_arrow()
    z.free_text(complex(49.0, 9.6), '39－2', fs=15, color=GRAY)
    z.free_text(complex(-1.8, 9.6), '42－1', fs=15, color=GRAY)
    z.free_text(complex(23.3, -3.0), '道路（102）', fs=15, color=GRAY, rotation=90)
    z.free_text(complex(15.0, 21.5), '40', fs=15, color=GRAY)
    z.callout(centroid(sq), '建物図面「39番3」\n北の筆界から2.1・道路から5.8の四角い建物\n→ 現存（北端）',
              dirs=(0, 15, -15), dists=(150, 180, 210), fs=13, color=BLUE)
    z.callout(centroid(step), '建物図面「39番3の2」\n西側が段々に欠けた形\n→ 現存（真ん中）',
              dirs=(0, 10, -10), dists=(150, 180, 210), fs=13, color=GREEN)
    z.callout(centroid(shu), '建物図面「39番3の4」（主＋符号1の車庫）\n南端・42番1との境のすぐ北 → 今は何もない\n'
                             '＝令和2年10月12日に取壊し（本件旧建物）', dirs=(0, 15, 30), dists=(150, 180, 210), fs=13, color=RED)
    z.free_text(complex(6.6, 7.0), '主', fs=14, color=RED, weight='bold', ha='right')
    z.free_text(complex(17.6, 10.6), '附1（車庫）', fs=13, color=RED, weight='bold', ha='right')
    save(fig, [z], 'R2_dai22mon_zu01_kaoku_bangou')


# ---- 図6：敷地と建物の位置の確認図（作図チェック用） ----
def lots_lines(z, lw=2.0, north_top=10.0):
    """C・D、E・F、G・H、I・Jの線と、西の辺（Y＝0）・東の辺（Y＝19.2）。39番3は C・D の北10mまで描く。"""
    z.line(complex(north_top, 0), PT['I'], color=BLACK, lw=lw)
    z.line(complex(north_top, 19.2), PT['J'], color=BLACK, lw=lw)
    for a, b in ['CD', 'EF', 'GH', 'IJ']:
        z.line(PT[a], PT[b], color=BLACK, lw=lw)


def zu06():
    fig, axes = new_figure('敷地と建物の位置の確認図（作図チェック用）',
                           '〔3.2〕は42番3を飛び越えて42番4との境まで。建物図面に書くのは42番3との境までの0.7。建物の北の0.60だけが42番1にかかる',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    lots_lines(z, north_top=6.0)
    z.poly(SITE_BLDG, color=BLACK, lw=2.2, fill=ORANGE, alpha=0.22)
    over = srect(WEST, PT['E'].real, EAST, NORTH)    # 42番1にかかる北の0.60
    z.poly(over, color=RED, lw=0, fill=RED, alpha=0.45, check=False)
    fit(ax, [complex(6, 0), PT['J']], margin=0.06, extra=[(-9, -24), (29, 8)], pad_aspect=True)
    z.north_arrow()
    for n in 'CDEFGHIJ':
        z.point(PT[n], size=6)
    for n in 'CEGI':
        z.point_label(PT[n], n, away=complex(PT[n].real, 5))
    for n in 'DFHJ':
        z.point_label(PT[n], n, away=complex(PT[n].real, 14))
    z.free_text(complex(3.8, 9.6), '39－3', fs=15)
    z.free_text(complex(-5.5, 9.6), '42－1', fs=15)
    z.free_text(complex(-12.2, 17.4), '42－2', fs=15)
    z.free_text(complex(-18.65, 17.2), '42－3', fs=13)
    z.free_text(complex(-21.8, 12.0), '42－4', fs=15, color=GRAY)
    z.free_text(complex(-7.0, 22.3), '40', fs=15, color=GRAY)
    z.free_text(complex(-7.0, -3.3), '道路（102）', fs=15, color=GRAY, rotation=90)
    z.free_text(complex(0.9, 9.6), '19.20m', fs=13)
    z.free_text(complex(-5.6, -1.4), '11.20m', fs=13, rotation=90)
    z.free_text(complex(-14.3, -1.4), '6.20m', fs=13, rotation=90)
    z.callout(complex(-18.65, 19.2), '2.50m', dirs=(0, 20, -20), fs=13)
    dim_line(z, complex(SOUTH, WEST + 0.8), PT['I'] + (WEST + 0.8) * 1j, '〔3.2〕（42-4との境まで。平面図の値）', color=GRAY,
             ls='--', dirs=(-150, -165, -135), fs=14)
    dim_line(z, complex(SOUTH, 14.8), complex(PT['G'].real, 14.8), '0.7（42-3との境まで。建物図面に書く値）', color=RED,
             dirs=(5, 15, -5), fs=14)
    dim_line(z, complex(SOUTH + 1.4, 0), complex(SOUTH + 1.4, WEST), '3.9', offsets=((0, 12), (0, -12)))
    z.callout(complex(NORTH - 0.3, 9.9), '42-1にかかるのは北の0.60だけ', dirs=(70, 90, 50), dists=(60, 80, 100), fs=13, color=RED)
    z.free_text(complex(-14.0, 9.9), '本件新建物\n42-2の上に5.50', fs=14)
    save(fig, [z], 'R2_dai22mon_zu06_shikichi_ichi')


# ---- 答案用紙の第4欄（建物図面・各階平面図の完成形を描く枠）。2026-10-08、試験の答案用紙の寸法どおりに描き直した ----
# 寸法は試験の答案用紙（`../touan_youshi/R2_dai22mon_touan_youshi_p2.png`、A3横 420mm × 297mm を 2482px × 1755px で画像にしたもの）の
# 罫線の位置から mm に直した値（1mm ＝ 5.91px）。作図は用紙の左下を原点とする mm の座標で行い、図面の中身は
# 建物図面が縮尺1/500（1m ＝ 2mm）、各階平面図が縮尺1/250（1m ＝ 4mm）の実際の大きさで描く。
# 第4欄は1枚の枠の左半分が各階平面図、右半分が建物図面（中央の上下に短い仕切りの線）。建物図面の上に「家屋番号（略）」の箱が枠の外に、
# 「建物の所在」の記入欄が枠の中の上端にある。下に「作成者（略）（令和2年○月○日作成）」「縮尺 1/250」と「申請人（略）」「縮尺 1/500」。
INK = '#1a3a8f'   # 記入（濃い青）
FR_L, FR_R, FR_B, FR_T = 80.5, 382.3, 40.5, 271.4     # 図を描く枠
MID = 231.3                                          # 中央の仕切り
SH_X0, SH_X1, SH_Y0, SH_Y1 = 45.0, 415.0, -16.0, 297.0  # 画像に入れる範囲（mm）


def M(x, y):
    """用紙の mm の位置（x：右向き、y：上向き）を zu_helpers の複素数（北＝縦、東＝横）にする。"""
    return complex(y, x)


def S500(n, e):
    """建物図面（縮尺1/500）：敷地の座標 (X＝北, Y＝東) [m] を用紙の mm に置く。1m ＝ 2mm。"""
    return M(287.0 + 2 * e, 165.0 + 2 * n)


def S250(p, x0, y0):
    """各階平面図（縮尺1/250）：建物の点 B(東, 南) [m] を用紙の mm に置く。原点（北西の角）を (x0, y0) mm に。1m ＝ 4mm。"""
    return M(x0 + 4 * p.imag, y0 + 4 * p.real)


def sheet_figure(title):
    setup_font()
    w_mm, h_mm = SH_X1 - SH_X0, SH_Y1 - SH_Y0
    fig = plt.figure(figsize=(22, 22 * h_mm / w_mm), dpi=100)
    fig.patch.set_facecolor('white')
    ax = fig.add_axes([0, 0, 1, 1])
    z = Zu(ax, fontsize=10)
    ax.set_xlim(SH_X0, SH_X1)
    ax.set_ylim(SH_Y0, SH_Y1)
    ax.text((SH_X0 + SH_X1) / 2, 291.5, title, ha='center', va='center', fontsize=21, weight='bold')
    return fig, ax, z


def sheet4(ax):
    """第4欄の印刷（試験の答案用紙どおり）。記入（家屋番号は（略）なので建物の所在だけ）は別に書く。"""
    def rect(x0, y0, x1, y1, lw=1.3):
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, lw=lw, ec=BLACK, zorder=3))

    def ln(x0, y0, x1, y1, lw=1.0, **kw):
        ax.plot([x0, x1], [y0, y1], color=kw.pop('color', BLACK), lw=lw, zorder=3, **kw)

    def txt(x, y, s, fs=12, ha='center', **kw):
        ax.text(x, y, s, ha=ha, va='center', fontsize=fs, zorder=4, family='Noto Serif CJK JP', **kw)

    rect(56.0, 22.4, 406.6, 285.0, lw=1.0)                    # 外枠（二重線）
    rect(56.9, 23.3, 405.7, 284.1, lw=1.6)
    ax.text(58.7, 278.0, '第4欄', ha='left', va='center', fontsize=12, weight='bold', zorder=4)
    rect(FR_L, FR_B, FR_R, FR_T, lw=1.6)                      # 図を描く枠
    ln(MID, FR_T, MID, 261.3, lw=1.6)                         # 中央の仕切り（上下の短い線だけが印刷）
    ln(MID, FR_B, MID, 50.4, lw=1.6)
    txt(160.6, 275.6, '各　階　平　面　図', fs=15)
    txt(336.7, 275.6, '建　物　図　面', fs=15)
    rect(240.3, FR_T, 302.2, 281.3)                           # 家屋番号の箱（枠の外の上）
    ln(264.3, FR_T, 264.3, 281.3)
    txt(252.3, 276.3, '家 屋 番 号', fs=11)
    txt(283.2, 276.3, '（略）', fs=11)
    rect(240.3, 261.3, FR_R, FR_T)                            # 建物の所在の欄（枠の中の上端）
    ln(264.3, 261.3, 264.3, FR_T)
    txt(252.3, 266.3, '建物の所在', fs=11)
    rect(FR_L, 26.0, 223.3, FR_B)                             # 作成者・縮尺 1/250
    for x in (99.5, 189.2, 199.3):
        ln(x, 26.0, x, FR_B)
    txt(90.0, 33.2, '作 成 者', fs=11)
    txt(144.0, 36.0, '（略）', fs=11)
    txt(188.0, 29.5, '（令和2年○月○日作成）', fs=10, ha='right')
    txt(194.2, 33.2, '縮尺', fs=10)
    ln(201.5, 28.0, 221.0, 38.5, lw=0.9)
    txt(206.0, 36.6, '1', fs=10)
    txt(215.5, 29.6, '250', fs=10)
    rect(239.3, 26.0, FR_R, FR_B)                             # 申請人・縮尺 1/500
    for x in (258.1, 347.9, 358.2):
        ln(x, 26.0, x, FR_B)
    txt(248.7, 33.2, '申 請 人', fs=11)
    txt(303.0, 33.2, '（略）', fs=11)
    txt(353.0, 33.2, '縮尺', fs=10)
    ln(360.5, 28.0, 380.0, 38.5, lw=0.9)
    txt(365.0, 36.6, '1', fs=10)
    txt(374.5, 29.6, '500', fs=10)
    ax.text(270.0, 266.3, 'A市B区T町三丁目42番地2、42番地1', ha='left', va='center', fontsize=12, color=INK, zorder=4)


def zumen_content(z):
    """右半分：建物図面（縮尺1/500、1m ＝ 2mm）。1階の位置・形状と、筆界からの距離（小数第1位）、地番・道路・方位。"""
    for n0, n1, e in [(10.0, -19.9, 0.0), (10.0, -19.9, 19.2)]:
        z.line(S500(n0, e), S500(n1, e), lw=1.2)
    for n in (0.0, -11.2, -17.4, -19.9):
        z.line(S500(n, 0), S500(n, 19.2), lw=1.2)
    z.poly([S500(NORTH, WEST), S500(NORTH, EAST), S500(SOUTH, EAST), S500(SOUTH, WEST)], lw=2.0)
    z.north_arrow(pos=(0.86, 0.66), length=0.045)
    dim_line(z, S500(SOUTH + 1.6, 0), S500(SOUTH + 1.6, WEST), '3.9', fs=10, offsets=((0, 9), (0, -9)))
    dim_line(z, S500(SOUTH, WEST + 0.7), S500(PT['G'].real, WEST + 0.7), '0.7', fs=10, dirs=(-140, -120, -160))
    dim_line(z, S500(SOUTH, EAST - 0.7), S500(PT['G'].real, EAST - 0.7), '0.7', fs=10, dirs=(-40, -60, -20))
    z.free_text(S500(5.0, 9.6), '39－3', fs=10)
    z.free_text(S500(-5.6, 9.6), '42－1', fs=10)
    z.callout(S500(-12.4, 17.55), '42－2', dirs=(20, 0, 40), dists=(28, 36, 46), fs=9)
    z.free_text(S500(-18.65, 9.6), '42－3', fs=9)
    z.free_text(S500(-5.6, 25.0), '40', fs=10)
    z.free_text(S500(-5.6, -5.0), '道路（102）', fs=10, rotation=90)
    z.free_text(M(365.0, 47.0), '（単位：m）', fs=9)


def heimen_content(z):
    """左半分：各階平面図（縮尺1/250、1m ＝ 4mm）。壁の中心線の辺長（小数第2位）、1階・2階は各階同型で1つの図、3階には1階の位置を点線で。"""
    x0, y_12, y_3 = 98.0, 238.0, 168.0
    z.free_text(M(94.0, 252.0), '1階・2階（各階同型）', fs=11, ha='left')
    f12 = [S250(p, x0, y_12) for p in F12]
    z.poly(f12, lw=1.6)
    for i, t in enumerate(['11.90', '6.00', '11.90', '6.00']):
        z.edge_label(f12[i], f12[(i + 1) % 4], t, centroid(f12), fs=10, dists=(8, 12))
    z.free_text(M(164.0, 226.0), '求積表\n11.90×6.00＝71.4000\n床面積　71.40㎡', fs=11, ha='left', linespacing=1.6)
    z.free_text(M(94.0, 182.0), '3階', fs=11, ha='left')
    f3 = [S250(p, x0, y_3) for p in F3]
    z.line(S250(B(0, 4.2), x0, y_3), S250(B(0, 6.0), x0, y_3), lw=1.1, ls=':')    # 3階と重ならない1階の部分（南西の角）
    z.line(S250(B(0, 6.0), x0, y_3), S250(B(4.1, 6.0), x0, y_3), lw=1.1, ls=':')
    z.poly(f3, lw=1.6)
    labels3 = ['11.90', '6.00', '7.80', '1.80', '4.10', '4.20']
    c3 = centroid(f3)
    for i, t in enumerate(labels3):
        z.edge_label(f3[i], f3[(i + 1) % 6], t, c3, fs=10, dists=(8, 12))
    z.free_text(M(164.0, 155.0), '求積表\n4.10×4.20＝17.2200\n7.80×6.00＝46.8000\n計　64.0200\n床面積　64.02㎡', fs=11,
                ha='left', linespacing=1.6)


def zu07():
    """建物図面の完成形：第4欄の右半分。用紙の大きさと縮尺1/500の実際の大きさで描く（左半分の各階平面図は第5章の図11）。"""
    fig, ax, z = sheet_figure('建物図面の完成形（答案用紙の第4欄の右半分・縮尺1/500の実際の大きさ）')
    sheet4(ax)
    zumen_content(z)
    ax.text(230.0, 10.0, '筆界から外壁までの距離は小数第1位（問題文の注4）。42番1と42番2の境の線は建物の北寄りを横切る。敷地の辺長と〔3.2〕は書かない',
            ha='center', va='center', fontsize=13)
    ax.text(230.0, 2.0, '左半分の各階平面図は、床面積を求めてから描く（第5章）。家屋番号と申請人は「（略）」と印刷済みで、書くのは建物の所在だけ',
            ha='center', va='center', fontsize=12, color=GRAY)
    save(fig, [z], 'R2_dai22mon_zu07_tatemono_zumen')


def zu11():
    """問4の完成形：第4欄の左半分（各階平面図・縮尺1/250）と右半分（建物図面・縮尺1/500）。用紙の大きさと縮尺どおり。"""
    fig, ax, z = sheet_figure('問4の完成形（答案用紙の第4欄：各階平面図と建物図面を実際の大きさで）')
    sheet4(ax)
    heimen_content(z)
    zumen_content(z)
    ax.text(230.0, 10.0, '各階平面図は壁の中心線の寸法（小数第2位）。1階・2階は各階同型で1つの図と1つの求積表、3階には3階と重ならない1階の部分を点線で示す',
            ha='center', va='center', fontsize=13)
    ax.text(230.0, 2.0, '方位は建物図面だけに書く（不動産登記規則第82条第2項。各階平面図の第83条第1項には方位がない）。作成者・申請人の「（略）」と縮尺は印刷済み',
            ha='center', va='center', fontsize=12, color=GRAY)
    assert round(area(F12), 4) == 71.40 and round(area(F3), 4) == 64.02
    save(fig, [z], 'R2_dai22mon_zu11_kakukai_heimenzu')


# ---- 図8：1階・2階の床面積求積図 ----
def zu08():
    fig, axes = new_figure('1階・2階（各階同型）の床面積求積図',
                           '外壁の外側の12.00×6.10から、両端の0.05ずつ内側の壁の中心線で11.90×6.00＝71.40㎡。旧ポーチ5.25㎡は10月12日の工事で床面積に入った',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(OUTER, color=GRAY, lw=1.2)
    z.poly(F12, color=BLACK, lw=2.4, fill=BLUE, alpha=0.20)
    z.poly(PORCH, color=ORANGE, lw=1.8, fill=ORANGE, alpha=0.45)
    fit(ax, OUTER, margin=0.16, extra=[xy(B(-2.5, 8.8)), xy(B(14.5, -2.8))], pad_aspect=True)
    z.north_arrow()
    c = centroid(F12)
    z.edge_label(B(0, 0), B(11.9, 0), '11.90m', c, dists=(26, 34), fs=15)
    z.edge_label(B(11.9, 0), B(11.9, 6), '6.00m', c, dists=(26, 34), fs=15)
    z.edge_label(B(-0.05, 6.05), B(11.95, 6.05), '12.00（外壁の外側）', c, color=GRAY, dists=(12, 18), fs=12)
    z.edge_label(B(-0.05, -0.05), B(-0.05, 6.05), '6.10（外壁の外側）', c, color=GRAY, dists=(12, 18), fs=12)
    z.callout(B(0.75, 1.75), '旧ポーチ 1.50m×3.50m＝5.25㎡\n（10月12日の工事でエントランスに＝増築）', dirs=(115, 100, 130),
              dists=(80, 100, 120), fs=13, color=ORANGE)
    z.free_text(B(7.0, 3.0), '1階・2階 床面積：71.40㎡\n（新築した9月18日の1階は66.15㎡）', fs=16, weight='bold')
    save(fig, [z], 'R2_dai22mon_zu08_1kai2kai_kyuuseki')


# ---- 図9：3階の誤り比較図 ----
def zu09():
    fig, axes = new_figure('3階の床面積：全部から0.10を引いていいか',
                           '0.10減るのは両端の壁の中心線がどちらも内側へずれる寸法（12.00・6.10・4.30・7.90）だけ。4.10と1.80は両端が同じ向きにずれて変わらない',
                           w=19, h=9.5, ncols=3, width_ratios=[1.05, 1.0, 1.05])
    fig.subplots_adjust(top=0.84, bottom=0.14)
    # 誤り
    z = Zu(axes[0], fontsize=13)
    z.poly(W3_NG, color=RED, lw=2.0, fill=RED, alpha=0.22)
    z.poly(E3, color=RED, lw=2.0, fill=RED, alpha=0.22)
    hatch(axes[0], GAP, color=RED)
    axes[0].set_title('誤り：全部から0.10を引く（藍子）', fontsize=17, weight='bold', color=RED)
    fit(axes[0], F3, margin=0.2, extra=[xy(B(2, 10.5))], pad_aspect=True)
    cz = centroid(F3)
    z.edge_label(B(0, 0), B(4.0, 0), '4.00m', centroid(W3_NG), fs=13)
    z.edge_label(B(0, 4.2), B(0, 0), '4.20m', centroid(W3_NG), fs=13)
    z.edge_label(B(4.1, 0), B(11.9, 0), '7.80m', centroid(E3), fs=13)
    z.edge_label(B(11.9, 0), B(11.9, 6.0), '6.00m', centroid(E3), fs=13)
    z.callout(B(4.05, 2.1), '抜け落ちた帯\n0.10×4.20＝0.42㎡', dirs=(-100, -80, -120), dists=(80, 100, 120), fs=12, color=RED)
    z.free_text(B(6.0, 8.7), '4.00×4.20＋7.80×6.00\n＝63.60㎡', fs=14, color=RED, weight='bold')
    # 拡大（南西の入り隅。外壁の外側の測定値の座標＝建物の北西の外側の角が原点）
    z2 = Zu(axes[1], fontsize=12)
    ax2 = axes[1]

    def Q(e, s):   # 外側の測定値の座標（東, 南）を、壁の中心線の座標系に合わせる
        return B(e - 0.05, s - 0.05)
    step_wall = [Q(3.3, 4.2), Q(4.1, 4.2), Q(4.1, 4.3), Q(3.3, 4.3)]              # LDKの南の壁（厚さ0.10）
    west_wall = [Q(4.1, 4.02), Q(4.2, 4.02), Q(4.2, 4.85), Q(4.1, 4.85)]          # 洋室の西の壁（北へLDKの東の壁に続く）
    for w in (step_wall, west_wall):
        z2.poly(w, color=GRAY, lw=0, fill=GRAY, alpha=0.35, check=False)
    z2.line(Q(3.3, 4.3), Q(4.1, 4.3), color=BLACK, lw=3.0)                        # 外側の面（バルコニー側）
    z2.line(Q(4.1, 4.3), Q(4.1, 4.85), color=BLACK, lw=3.0)
    z2.line(Q(3.3, 4.25), Q(4.15, 4.25), color=BLUE, lw=1.8, ls='-.')             # 壁の中心線
    z2.line(Q(4.15, 4.02), Q(4.15, 4.85), color=BLUE, lw=1.8, ls='-.')
    ax2.set_title('南西の入り隅（拡大）', fontsize=17, weight='bold')
    fit(ax2, [Q(3.22, 3.95), Q(4.62, 5.3)], margin=0.02, pad_aspect=True)
    ax2.annotate('', xy=xy(Q(4.15, 4.7)), xytext=xy(Q(4.1, 4.7)),
                 arrowprops=dict(arrowstyle='-|>', lw=2.0, color=RED, mutation_scale=16, shrinkA=0, shrinkB=0), zorder=6)
    ax2.annotate('', xy=xy(Q(3.85, 4.25)), xytext=xy(Q(3.85, 4.3)),
                 arrowprops=dict(arrowstyle='-|>', lw=2.0, color=RED, mutation_scale=16, shrinkA=0, shrinkB=0), zorder=6)
    z2.segments += [(xy(Q(4.1, 4.7)), xy(Q(4.15, 4.7))), (xy(Q(3.85, 4.3)), xy(Q(3.85, 4.25)))]
    z2.callout(Q(4.125, 4.7), '洋室の西の壁の外側の面\n（4.10の東の端）\n→ 中心線は東へ0.05', dirs=(-55, -70, -85, -100, -40), dists=(45, 60, 75, 95),
               fs=12, color=RED)
    z2.callout(Q(3.85, 4.275), 'LDKの南の壁の\n外側の面\n→ 中心線は北へ0.05', dirs=(-120, -135, -150), dists=(45, 60, 75), fs=12,
               color=RED)
    z2.free_text(Q(3.7, 4.08), 'LDK', fs=13, color=GRAY)
    z2.free_text(Q(3.6, 4.6), 'バルコニー側（屋外）', fs=12, color=GRAY, offsets=((0, 0), (0, -20), (0, 20), (-20, 0)))
    z2.free_text(Q(4.42, 4.3), '洋室', fs=13, color=GRAY)
    z2.free_text(Q(3.95, 5.22), '建物の西の壁の中心線も東へ0.05\n→ 4.10は両端が同じ向きにずれて4.10のまま', fs=12, color=BLUE)
    # 正解
    z3 = Zu(axes[2], fontsize=13)
    z3.poly(W3, color=GREEN, lw=2.0, fill=GREEN, alpha=0.22)
    z3.poly(E3, color=GREEN, lw=2.0, fill=GREEN, alpha=0.22)
    axes[2].set_title('正解：ずれる向きで判断する', fontsize=17, weight='bold', color=GREEN)
    fit(axes[2], F3, margin=0.2, extra=[xy(B(2, 10.5))], pad_aspect=True)
    z3.edge_label(B(0, 0), B(4.1, 0), '4.10m', centroid(W3), fs=13)
    z3.edge_label(B(0, 4.2), B(0, 0), '4.20m', centroid(W3), fs=13)
    z3.edge_label(B(4.1, 0), B(11.9, 0), '7.80m', centroid(E3), fs=13)
    z3.edge_label(B(11.9, 0), B(11.9, 6.0), '6.00m', centroid(E3), fs=13)
    z3.free_text(B(6.0, 8.7), '4.10×4.20＋7.80×6.00\n＝64.02㎡', fs=14, color=GREEN, weight='bold')
    save(fig, [z, z2, z3], 'R2_dai22mon_zu09_3kai_ayamari_hikaku')


# ---- 図10：3階の床面積求積図 ----
def zu10():
    fig, axes = new_figure('3階の床面積求積図（西の列と東の列）',
                           '4.10×4.20＋7.80×6.00＝64.02㎡。南西の4.10×1.80と南のバルコニーは外気と分断されず入らない（点線は3階と重ならない1階の部分）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(W3, color=ORANGE, lw=0, fill=ORANGE, alpha=0.28, check=False)
    z.poly(E3, color=BLUE, lw=0, fill=BLUE, alpha=0.25, check=False)
    hatch(ax, SW_OUT)
    hatch(ax, BAL_S)
    z.poly(BAL_S, color=GRAY, lw=1.2, ls='--', check=False)
    z.line(B(0, 4.2), B(0, 6.0), color=BLACK, lw=1.4, ls=':')    # 3階と重ならない1階の部分（点線）
    z.line(B(0, 6.0), B(4.1, 6.0), color=BLACK, lw=1.4, ls=':')
    z.line(B(4.1, 0), B(4.1, 4.2), color=GRAY, lw=1.0, ls='--')
    z.poly(F3, color=BLACK, lw=2.4)
    fit(ax, F3 + BAL_S, margin=0.16, extra=[xy(B(-2.5, 9.8)), xy(B(14.5, -2.8))], pad_aspect=True)
    z.north_arrow()
    z.edge_label(B(0, 0), B(11.9, 0), '11.90', centroid(F3), fs=14)
    z.edge_label(B(11.9, 0), B(11.9, 6.0), '6.00', centroid(F3), fs=14)
    z.edge_label(B(0, 4.2), B(0, 0), '4.20', centroid(W3), fs=14)
    z.edge_label(B(4.1, 4.2), B(0, 4.2), '4.10', centroid(W3), fs=14, outward=False)
    z.edge_label(B(4.1, 6.0), B(4.1, 4.2), '1.80', centroid(E3), fs=14, outward=False)
    z.free_text(centroid(W3), '4.10m\n×\n4.20m', fs=14)
    z.free_text(centroid(E3), '7.80m × 6.00m', fs=14)
    z.callout(B(2.05, 5.1), '南西の4.10×1.80\nバルコニーとつながった屋外（入れない）', dirs=(180, -170, 170), dists=(90, 110, 130),
              fs=13, color=GRAY)
    z.callout(B(8.0, 6.45), 'バルコニー（入れない）', dirs=(-60, -80, -40), fs=13, color=GRAY)
    z.free_text(B(11.0, 8.9), '3階 床面積：64.02㎡', fs=16, weight='bold')
    save(fig, [z], 'R2_dai22mon_zu10_3kai_kyuuseki')


# ---- 図15：本番で解く順番（固定配置の図なので重なり検査の対象外） ----
def zu15():
    """上に事実関係の日付の時系列メモ、下に解く順番。計算のいらない問1・問2を先に書き、求積と位置は後に回す。"""
    fig = plt.figure(figsize=(16, 10), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　計算のいらない問1・問2を先に、求積と位置は後に', fontsize=24, weight='bold', y=0.965)

    # 上段：事実関係の日付の時系列メモ
    at = fig.add_axes([0.03, 0.66, 0.94, 0.24])
    at.set_xlim(0, 100)
    at.set_ylim(0, 100)
    at.axis('off')
    at.text(0, 92, '別紙の時系列メモ（令和2年）', fontsize=16, weight='bold', va='top')
    at.annotate('', xy=(99, 50), xytext=(3, 50), arrowprops=dict(arrowstyle='-|>', lw=2.0, color=GRAY))
    events = [
        (12, '9月18日', '本件新建物を新築\n引渡し（1階66.15㎡）', GREEN),
        (38, '10月3日', '松子さんが42番地2へ転居\n（今の住所・変更証明書）', BLUE),
        (64, '10月12日', 'エントランス完成（増築）\n本件旧建物を取壊し', RED),
        (89, '10月16日', '申請（2件）\n滅失・表題とも1か月以内', BLACK),
    ]
    for x, d, t, col in events:
        at.plot([x], [50], marker='o', ms=14, color=col, zorder=3)
        at.text(x, 64, d, ha='center', va='bottom', fontsize=17, weight='bold', color=col)
        at.text(x, 36, t, ha='center', va='top', fontsize=13.5, color=col)

    # 下段：解く順番
    ax = fig.add_axes([0.03, 0.14, 0.94, 0.48])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '前文・注・\n問1〜問4を\n読む', '何を答えるか\n（注4：距離は\n小数第1位）', BLUE),
        ('②', '日付の\n時系列メモ', '上の4つの日付', BLUE),
        ('③', '建物図面\n3枚で家屋\n番号を特定', '39番3の4', BLUE),
        ('④', '問1の\n申請書', '第1欄\n（今の住所・\n下線の行は\n写さない）', BLUE),
        ('⑤', '問2の\n記述', '第2欄\n（解体移転と\nえい行移転）', BLUE),
        ('⑥', '壁の中心線で\n床面積', '第3欄 床面積\n（3階は入り隅\nに注意64.02）', RED),
        ('⑦', '座標で\n建物の位置', '第3欄 所在\n（42番地2が先）\n第4欄の距離', RED),
        ('⑧', '問4の作図\n・見直し', '第4欄\n原因の併記\n「葺」「ぶき」', GRAY),
    ]
    w, h, gap = 10.6, 44, 1.8
    y0 = 36
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, y0), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, y0 + h - 3, no, ha='center', va='top', fontsize=24, color=col, weight='bold')
        ax.text(x + w / 2, y0 + h / 2 - 5, t, ha='center', va='center', fontsize=15)
        ax.text(x + w / 2, y0 - 3, ran, ha='center', va='top', fontsize=12.5, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, y0 + h / 2), xytext=(x + w + 0.2, y0 + h / 2),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 2.5 * (w + gap) - gap / 2, 91, '計算なしで書ける（問1・問2は一気に）', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 5 * (w + gap) - gap, 87), xytext=(1, 87), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 6 * (w + gap) - gap / 2, 91, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 7 * (w + gap) - gap, 87), xytext=(1 + 5 * (w + gap), 87),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.065, '所在の順序（42番地2、42番地1）は、座標で建物の位置を出して床面積の多い土地を決めてから書く。\n'
             '問1・問2を先に書いておけば、求積と作図で時間が足りなくなっても、2件の申請書の多くの欄の点は取れている。',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'R2_dai22mon_zu15_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図15: 解く順番（固定配置）\n  →', path)



# ---- 固定配置の図（枠と文字だけ。座標を使わないので重なりの自動検査の対象外。PNGを目で確かめる） ----
from matplotlib.patches import FancyBboxPatch  # noqa: E402


def board(title, w=16, h=10):
    setup_font()
    fig = plt.figure(figsize=(w, h), dpi=100)
    fig.patch.set_facecolor('white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100 * h / w)
    ax.axis('off')
    ax.text(50, 100 * h / w - 4.5, title, ha='center', va='center', fontsize=23, weight='bold')
    return fig, ax


def card(ax, x, y, w, h, head, body, color=BLUE, fs=15, head_fs=17, ls=1.55):
    """左下 (x, y)、幅 w、高さ h の角丸の枠。上に見出し、その下に本文（左寄せ）。"""
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.4,rounding_size=1.2', fc=color, alpha=0.08, ec='none'))
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.4,rounding_size=1.2', fc='none', ec=color, lw=2.0))
    ax.text(x + w / 2, y + h - 2.6, head, ha='center', va='center', fontsize=head_fs, weight='bold', color=color)
    ax.text(x + 1.6, y + h - 6.2, body, ha='left', va='top', fontsize=fs, linespacing=ls)


def arrow(ax, p, q, color=GRAY, lw=2.0):
    ax.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle='-|>', lw=lw, color=color, mutation_scale=22))


def save_board(fig, name):
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('書き出し（固定配置）:', path)


def zu02():
    """注の仕分け：問題文の注・〔調査図〕の（注）・〔平面図〕の（注）の3系統と、番号の付いた事実関係。赤は今年の答えに効くもの。"""
    fig, ax = board('注は3系統、番号がかぶる：どの注かを言い分ける（赤は今年の答えに効くもの）', h=10.5)
    cols = [
        ('問題文の注（1〜5）', BLUE, [
            ('1・2　全て適法／書面申請', BLACK), ('3　建物図面1/500・各階平面図1/250', BLACK),
            ('4　建物図面の距離は\n　　小数点以下第1位まで', RED), ('5　訂正・加入・削除の書き方', BLACK)]),
        ('〔調査図〕の（注）（1〜5）', GREEN, [
            ('1・2　単位はメートル／\n　　（　）は地番', BLACK), ('3　座標は〔座標一覧表〕', BLACK),
            ('4　北は102番の西側道路と\n　　平行（図面の上が北）', RED), ('5　破線は39番3に\n　　現存する建物', RED)]),
        ('〔平面図〕の（注）（1〜9）', ORANGE, [
            ('1・2　単位・地番', BLACK), ('3　外壁等の隅角部の測定値', RED), ('4　〔　〕は敷地と1階の外壁\n　　との距離', RED),
            ('5　壁厚10cm、中心線は\n　　隅角部から5cm内側', RED), ('6　天井高2.7m以上／7　☆★の柱', BLACK),
            ('8　EVは住戸B・住戸Cの専用', BLACK), ('9　外階段・バルコニーは外気\n　　分断性なし、各住戸の玄関へ', RED)]),
    ]
    top = 59
    for k, (head, col, items) in enumerate(cols):
        x = 2 + k * 32.5
        ax.add_patch(FancyBboxPatch((x, 8), 30.5, top - 8, boxstyle='round,pad=0.4,rounding_size=1.2', fc=col, alpha=0.07, ec=col, lw=2))
        ax.text(x + 15.25, top - 2.8, head, ha='center', va='center', fontsize=17, weight='bold', color=col)
        y = top - 8
        for t, c in items:
            ax.text(x + 1.2, y, t, ha='left', va='top', fontsize=14, color=c, weight='bold' if c == RED else 'normal', linespacing=1.4)
            y -= 4.6 + 3.6 * t.count('\n')
    ax.text(50, 3.5, '事実関係1〜7（9月18日新築、10月3日転居、10月12日の工事完成・取壊しなど）は注とは別の系統。'
            '「問題文の注4」「〔平面図〕の（注）4」「事実関係5」と書き分ける', ha='center', va='center', fontsize=13.5)
    save_board(fig, 'R2_dai22mon_zu02_chuu_shiwake')


def zu03():
    """住所が変わった名義人の申請：表示に関する登記（滅失登記）と権利に関する登記で、前提の住所変更の登記が要るかどうか。"""
    fig, ax = board('登記記録の住所が古いとき：滅失登記は前提の住所変更の登記が要らない', h=9)
    card(ax, 3, 10, 45, 34, '建物滅失登記（表示に関する登記）',
         '・申請人は今の住所（42番地2）で書く\n'
         '・登記記録の住所（39番地3）からのつながりを\n　示す変更証明書を付ける（名義人本人である\n　ことを示すため。不動産登記法第57条）\n'
         '・住所変更の登記を先にしなくてよい\n'
         '・滅失登記で登記記録は閉鎖される\n　（不動産登記規則第144条第1項）\n　→ 閉じる記録の住所を直す意味がない', color=BLUE)
    card(ax, 52, 10, 45, 34, '所有権移転・抵当権の抹消など（権利に関する登記）',
         '・登記義務者の住所が登記記録と合わないと\n　申請が却下される（不動産登記法第25条第7号）\n'
         '・前提として、登記名義人住所変更登記\n　（名義変更）を先に申請する\n\n'
         '・表示に関する登記の滅失登記と\n　混同しない', color=ORANGE)
    ax.text(50, 4.0, '変更証明書は、不動産登記令第7条第1項・別表で「必ず付ける」と決められた添付情報ではない（別表の建物の滅失は共用部分の17の項だけ）',
            ha='center', va='center', fontsize=13)
    save_board(fig, 'R2_dai22mon_zu03_jyuusho_zentei')


def zu04():
    """本試験当時と今の法令：住所変更の登記の義務化（不動産登記法第76条の5）と、どの不動産に義務がかかるか。"""
    fig, ax = board('本試験（令和2年）と今の法令：住所変更の登記の義務化（不動産登記法第76条の5）')
    card(ax, 3, 30, 30, 23, '本試験の令和2年',
         '・住所変更の登記の\n　申請義務はなかった\n・滅失登記は変更証明書を\n　付けて今の住所で申請', color=GRAY)
    arrow(ax, (34.5, 41.5), (39.5, 41.5))
    card(ax, 41, 30, 56, 23, '令和3年の改正（令和3年法律第24号）で第76条の5',
         '・所有権の登記名義人の住所が変わったら、2年以内に\n　住所変更の登記を申請する義務\n'
         '・改正の前に住所が変わった人にも附則で当てはめる\n・怠れば5万円以下の過料（同法第164条第2項）', color=BLUE)
    card(ax, 3, 6, 45, 19, '39番3の4（本件旧建物）',
         '・滅失登記で登記記録が閉鎖される\n・住所を先に直す意味はない\n・答案は今でも変更証明書と代理権限証書', color=GREEN, fs=14)
    card(ax, 52, 6, 45, 19, '39番3・39番3の2（取り壊していない建物）',
         '・松子さんが所有権の登記名義人として残る\n・今の法令なら、こちらに住所変更の登記の\n　申請義務がかかる', color=ORANGE, fs=14)
    save_board(fig, 'R2_dai22mon_zu04_jyuusho_gimuka')


def zu05():
    """問2：解体移転とえい行移転。39番3の土地の中で北の端から南の端へ動かす。隣の土地にかかれば所在の変更。"""
    fig, ax = board('問2　えい行移転は「所在」が変わらなければ登記不要')
    panels = [(3, '解体移転', BLUE, '解体で同一性が失われる\n→ 建物滅失登記＋建物表題登記\n（申請義務は有）', 'kaitai'),
              (35.5, 'えい行移転（39番3の中）', GREEN, '同一性は失われない\n所在は39番地3のまま\n→ 申請義務は無', 'eikou'),
              (68, '参考：隣の土地にかかったら', ORANGE, '所在の地番が変わる\n→ 建物表題部変更登記\n（所在の変更）', 'tonari')]
    for x, head, col, body, kind in panels:
        ax.text(x + 14.5, 55, head, ha='center', va='center', fontsize=17, weight='bold', color=col)
        lot = Rectangle((x + 6, 18), 12, 32, fill=False, lw=2.0, ec=BLACK)
        ax.add_patch(lot)
        ax.text(x + 12, 15.8, '39－3の土地', ha='center', va='center', fontsize=13, color=GRAY)
        if kind == 'tonari':
            ax.add_patch(Rectangle((x + 18, 18), 8, 32, fill=False, lw=1.5, ec=BLACK, ls='--'))
            ax.text(x + 22, 34, '隣の\n土地', ha='center', va='center', fontsize=12, color=GRAY)
        old = Rectangle((x + 9, 43), 6, 4.5, fill=False, lw=2.0, ec=BLACK, ls='--')
        ax.add_patch(old)
        if kind == 'kaitai':
            ax.add_patch(Rectangle((x + 9, 20.5), 6, 4.5, fc=col, alpha=0.35, ec=col, lw=2.0))
            ax.text(x + 12, 45.25, '解体', ha='center', va='center', fontsize=11, color=RED)
            ax.text(x + 12, 22.75, '新築', ha='center', va='center', fontsize=11)
        elif kind == 'eikou':
            ax.add_patch(Rectangle((x + 9, 20.5), 6, 4.5, fc=col, alpha=0.35, ec=col, lw=2.0))
        else:
            ax.add_patch(Rectangle((x + 14.5, 20.5), 6, 4.5, fc=col, alpha=0.35, ec=col, lw=2.0))
        arrow(ax, (x + 12, 42), (x + 12 if kind != 'tonari' else x + 17.5, 26.5), color=col, lw=2.4)
        ax.text(x + 14.5, 8, body, ha='center', va='center', fontsize=14, linespacing=1.5)
    ax.text(50, 2.0, '建物の所在は「どの土地の上にあるか」を地番で表すだけ。同じ土地の中の位置は登記されていない',
            ha='center', va='center', fontsize=13.5)
    save_board(fig, 'R2_dai22mon_zu05_eikou_iten')


def zu12():
    """所在の順序：本件新建物の1階の外形（外壁の外側）は、42番1に北の0.60だけ、42番2に5.50。床面積の多い42番2が先。"""
    fig, axes = new_figure('所在の順序は床面積の多い土地が先：「42番地2、42番地1」',
                           '建物の1階の外形（外壁の外側）は南の外壁X＝−16.70〜北の外壁X＝−10.60。\n42番1と42番2の境（X＝−11.20）で切ると、'
                           '北の0.60だけが42番1、残りの5.50が42番2（不動産登記事務取扱手続準則第88条第2項）', w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fit(ax, [complex(-9.0, 0), complex(-17.4, 19.2)], margin=0.10, extra=[(-6, -20), (26, -8)], pad_aspect=True)
    z.poly([complex(-11.2, WEST), complex(-11.2, EAST), complex(SOUTH, EAST), complex(SOUTH, WEST)], color=BLUE, lw=0,
           fill=BLUE, alpha=0.22, check=False)
    z.poly([complex(NORTH, WEST), complex(NORTH, EAST), complex(-11.2, EAST), complex(-11.2, WEST)], color=ORANGE, lw=0,
           fill=ORANGE, alpha=0.35, check=False)
    for n0, n1, e in [(-9.0, -17.4, 0.0), (-9.0, -17.4, 19.2)]:
        z.line(complex(n0, e), complex(n1, e), lw=1.6)
    for n in (-11.2, -17.4):
        z.line(complex(n, 0), complex(n, 19.2), lw=1.6, color=RED if n == -11.2 else BLACK)
    z.poly(SITE_BLDG, lw=2.6)
    z.north_arrow()
    z.free_text(complex(-9.9, 2.0), '42－1', fs=15)
    z.free_text(complex(-16.4, 1.9), '42－2', fs=15)
    z.free_text(complex(-12.8, -3.5), '道路（102）', fs=14, rotation=90)
    z.free_text(complex(-13.8, 21.6), '40', fs=14)
    z.callout(complex(-10.9, 12.0), '42番1に北の0.60だけ', dirs=(60, 40, 80), fs=14, color=ORANGE)
    z.callout(complex(-15.6, 9.0), '42番2に5.50（大部分）', dirs=(-100, -80, -120), dists=(70, 90, 110), fs=14, color=BLUE)
    z.callout(complex(-11.2, 17.5), '42番1と42番2の境（X＝−11.20）', dirs=(70, 50, 90), fs=13, color=RED)
    ax.text(0.5, 0.10, '正：Ａ市Ｂ区Ｔ町三丁目42番地２、42番地１　　誤：地番の番号順の「42番地１、42番地２」', transform=ax.transAxes,
            ha='center', va='center', fontsize=15, weight='bold')
    assert round(NORTH - (-11.2), 2) == 0.60 and round(-11.2 - SOUTH, 2) == 5.50
    save(fig, [z], 'R2_dai22mon_zu12_shozai_junjo')


def zu13():
    """種類：玄関が別々の住戸が3つ（2階の住戸A・住戸B、3階の住戸C）なら、住まいの部分は全体で共同住宅。1階の薬局は店舗。"""
    fig, ax = board('種類は「共同住宅・店舗」：住戸ごと・階ごとに切り分けない')
    floors = [(38, '3階', [('住戸C（梅一郎さん一家）　玄関', 0, 40)]),
              (25, '2階', [('住戸A　玄関', 0, 20), ('住戸B（松子さん）　玄関', 20, 20)]),
              (12, '1階', [('薬局（エントランス・待合室・調剤室）', 0, 40)])]
    for y, f, rooms in floors:
        ax.text(5.5, y + 5, f, ha='center', va='center', fontsize=16, weight='bold')
        for t, dx, w in rooms:
            col = ORANGE if f == '1階' else BLUE
            ax.add_patch(Rectangle((9 + dx, y), w, 10, fc=col, alpha=0.18, ec=BLACK, lw=1.8))
            ax.text(9 + dx + w / 2, y + 5, t, ha='center', va='center', fontsize=14)
    ax.add_patch(Rectangle((50, 12), 4, 36, fc=GRAY, alpha=0.15, ec=GRAY, lw=1.5, ls='--'))
    ax.text(52, 30, '外\n階\n段', ha='center', va='center', fontsize=13, color=GRAY)
    for y in (30, 43):
        arrow(ax, (50, y), (47.5, y), color=GRAY, lw=1.6)
    card(ax, 59, 30, 38, 22, '正：共同住宅・店舗',
         '・玄関が別々の独立した住戸が3つ\n　→ 住まいの部分は全体で共同住宅\n・薬局は種類としては店舗\n・主な用途の順（不動産登記規則第113条）', color=GREEN, fs=14)
    card(ax, 59, 7, 38, 18, '誤：店舗・共同住宅・居宅',
         '・3階は1家族だからと居宅に切り離す\n・1棟の中の独立した住戸の1つなのに\n　階ごとに種類を分けてしまう', color=RED, fs=14)
    ax.text(30, 4.0, '〔平面図〕の（注）8・（注）9：EVは住戸B・住戸Cの専用、外階段は2階で住戸A・住戸B、3階で住戸Cの玄関に接続',
            ha='center', va='center', fontsize=12.5)
    save_board(fig, 'R2_dai22mon_zu13_shurui')


def zu14():
    """表題登記の前の増築：9月18日の新築（1階66.15㎡）→ 10月12日のエントランス（＋5.25㎡で71.40㎡）→ 10月16日に1件の表題登記で併記。"""
    fig, ax = board('表題登記の前の増築：1件の表題登記で「新築」と「増築」を併記する')
    pts = [(12, '9月18日', '新築・引渡し\n1階66.15㎡\n（ポーチは屋外）', GREEN),
           (42, '10月12日', 'エントランス完成（増築）\n旧ポーチ1.50×3.50＝5.25㎡\n1階71.40㎡', ORANGE),
           (72, '10月16日', '建物表題登記を申請\n（まだ一度も登記していない）', BLUE)]
    ax.annotate('', xy=(93, 46), xytext=(4, 46), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=GRAY))
    for x, d, t, c in pts:
        ax.plot([x], [46], 'o', ms=16, color=c, zorder=3)
        ax.text(x, 50.5, d, ha='center', va='bottom', fontsize=18, weight='bold', color=c)
        ax.text(x, 41.5, t, ha='center', va='top', fontsize=14, linespacing=1.5)
    card(ax, 3, 5, 45, 21, '正：1件の表題登記の中で経過を示す',
         '原因及びその日付\n「令和２年９月18日新築\n　令和２年10月12日増築」\n床面積は申請するときの今の姿（71.40）', color=GREEN, fs=14)
    card(ax, 52, 5, 45, 21, '誤：「令和２年９月18日新築」だけ',
         '・9月18日に1階71.40㎡の建物が\n　できたことになってしまう\n・表題登記＋表題部変更登記の2件に分けない\n　（申請件数を最も少なくしたい希望：事実関係6）', color=RED, fs=14)
    save_board(fig, 'R2_dai22mon_zu14_zouchiku_heiki')


if __name__ == '__main__':
    zu01()
    zu02()
    zu03()
    zu04()
    zu05()
    zu06()
    zu07()
    zu08()
    zu09()
    zu10()
    zu11()
    zu12()
    zu13()
    zu14()
    zu15()
    print('重なり合計:', len(PROBLEMS))
