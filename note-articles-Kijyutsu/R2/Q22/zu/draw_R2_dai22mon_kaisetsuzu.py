"""令和2年度 第22問（建物）の解説図7枚を、座標値・頂点座標から作図してPNGに書き出す。

`../prompt_R2_dai22mon_kaisetsuzu.md` の図1〜図7どおり。作図の共通部品は `tools/zu_helpers.py`。
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
from matplotlib.patches import Polygon as MPoly  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, BLACK, GRAY, RED, BLUE, ORANGE, GREEN)  # noqa: E402

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


# ---- 図2：敷地と建物の位置の確認図（作図チェック用） ----
def lots_lines(z, lw=2.0, north_top=10.0):
    """C・D、E・F、G・H、I・Jの線と、西の辺（Y＝0）・東の辺（Y＝19.2）。39番3は C・D の北10mまで描く。"""
    z.line(complex(north_top, 0), PT['I'], color=BLACK, lw=lw)
    z.line(complex(north_top, 19.2), PT['J'], color=BLACK, lw=lw)
    for a, b in ['CD', 'EF', 'GH', 'IJ']:
        z.line(PT[a], PT[b], color=BLACK, lw=lw)


def zu02():
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
    save(fig, [z], 'R2_dai22mon_zu02_shikichi_ichi')


# ---- 図3：建物図面の完成形 ----
def zu03():
    fig, axes = new_figure('建物図面の完成形（縮尺1/500で描く内容）',
                           '筆界から外壁までの距離は小数第1位（問題文の注4）。42番1と42番2の境の線は建物の北寄りを横切る。敷地の辺長と〔3.2〕は書かない',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    lots_lines(z, lw=1.8, north_top=6.0)
    z.poly(SITE_BLDG, color=BLACK, lw=2.6)
    fit(ax, [complex(6, 0), PT['J']], margin=0.06, extra=[(-6, -22), (26, 8)], pad_aspect=True)
    z.north_arrow()
    dim_line(z, complex(SOUTH + 1.4, 0), complex(SOUTH + 1.4, WEST), '3.9', offsets=((0, 12), (0, -12)))
    dim_line(z, complex(SOUTH, WEST + 0.6), complex(PT['G'].real, WEST + 0.6), '0.7', dirs=(-150, -130, -170))
    dim_line(z, complex(SOUTH, EAST - 0.6), complex(PT['G'].real, EAST - 0.6), '0.7', dirs=(-30, -50, -10))
    z.free_text(complex(2.5, 9.6), '39－3', fs=15)
    z.free_text(complex(-7.5, 1.9), '42－1', fs=15)
    z.free_text(complex(-12.2, 1.9), '42－2', fs=15)
    z.free_text(complex(-18.65, 9.6), '42－3', fs=13)
    z.free_text(complex(-7.0, 22.0), '40', fs=15)
    z.free_text(complex(-7.0, -3.2), '道路（102）', fs=15, rotation=90)
    z.free_text(complex(-21.3, 20.6), '（単位：m）', fs=13, color=GRAY)
    save(fig, [z], 'R2_dai22mon_zu03_tatemono_zumen')


# ---- 図4：1階・2階の床面積求積図 ----
def zu04():
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
    save(fig, [z], 'R2_dai22mon_zu04_1kai2kai_kyuuseki')


# ---- 図5：3階の誤り比較図 ----
def zu05():
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
    save(fig, [z, z2, z3], 'R2_dai22mon_zu05_3kai_ayamari_hikaku')


# ---- 図6：3階の床面積求積図 ----
def zu06():
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
    save(fig, [z], 'R2_dai22mon_zu06_3kai_kyuuseki')


# ---- 図7：本番で解く順番（固定配置の図なので重なり検査の対象外） ----
def zu07():
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
    path = os.path.join(OUT, 'R2_dai22mon_zu07_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図7: 解く順番（固定配置）\n  →', path)


if __name__ == '__main__':
    zu01()
    zu02()
    zu03()
    zu04()
    zu05()
    zu06()
    zu07()
    print('重なり合計:', len(PROBLEMS))
