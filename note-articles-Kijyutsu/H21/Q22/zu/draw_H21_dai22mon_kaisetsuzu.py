"""平成21年度 第22問（建物）の解説図8枚を、寸法から作図してPNGに書き出す。

`../prompt_H21_dai22mon_kaisetsuzu.md` の図1〜図8どおり。作図の共通部品は `tools/zu_helpers.py`。
- 座標値一覧表がない年度なので、敷地は〔配置図〕の筆界点間の距離（東西10.00×南北13.10の長方形）から描く
- 形は (東, 南) で持ち、P() で zu_helpers の複素数 (北 + 東i) に変換する
  - 敷地・建物図面（図1・図2）：原点＝3番4の北西の角（道路境界線と西の筆界の交点）
  - 各階（図4〜図7）：原点＝建物の北西の角（壁の中心線）
- 断面（図3）：原点＝ロフトの床の西の端（押入の外壁の中心）、(東, 高さ)。Q() で (北＝高さ, 東) にする
実行: python3 note-articles-Kijyutsu/H21/Q22/zu/draw_H21_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, BLACK, GRAY, RED, BLUE, ORANGE, GREEN,  # noqa: E402
                        PURPLE)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []


def P(e, s):
    """(東, 南) の点を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(-s, e)


def Q(e, h):
    """断面図の (東, 高さ) の点を複素数 (北＝高さ + 東i) にする。"""
    return complex(h, e)


def rect(e0, s0, e1, s1):
    return [P(e0, s0), P(e1, s0), P(e1, s1), P(e0, s1)]


def shift(pts, de, ds):
    return [p + complex(-ds, de) for p in pts]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


def trunc2(v):
    return math.floor(v * 100 + 1e-9) / 100


def hatch(z, pts, color=GRAY, pattern='///'):
    z.ax.add_patch(MPoly([xy(p) for p in pts], closed=True, fill=False, hatch=pattern, edgecolor=color, lw=0, zorder=1))


def arrow(z, p, q, both=False):
    """寸法の矢印（p→q）。線分を重なり検査に登録する。"""
    z.ax.annotate('', xy=xy(q), xytext=xy(p),
                  arrowprops=dict(arrowstyle='<|-|>' if both else '-|>', lw=1.2, color=BLACK, mutation_scale=11))
    z.segments.append((xy(p), xy(q)))


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def dims(z, pts, labels, fs=13, outward=True):
    """多角形の各辺に寸法（None は書かない）を書く。"""
    c = centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs, outward=outward)


# ---- 各階の形（原点＝建物の北西の角の壁の中心、(東, 南)） ----
F1 = [P(0, 0), P(6.37, 0), P(6.37, 1.82), P(5.46, 1.82), P(5.46, 7.28), P(0, 7.28)]
F2 = [P(0, 0), P(4.55, 0), P(4.55, 1.82), P(5.46, 1.82), P(5.46, 6.37), P(0, 6.37)]
F3 = rect(0, 0, 4.55, 1.82)
R1_N, R1_S = rect(0, 0, 6.37, 1.82), rect(0, 1.82, 5.46, 7.28)
R2_N, R2_S = rect(0, 0, 4.55, 1.82), rect(0, 1.82, 5.46, 6.37)
FUKINUKE, BERANDA = rect(4.55, 0, 5.46, 1.82), rect(0, 6.37, 5.46, 7.28)
OSHIIRE, LOFT = rect(0, 0, 0.91, 1.82), rect(0.91, 0, 4.55, 1.82)
assert round(area(F1), 4) == 41.405 and trunc2(area(F1)) == 41.40 and round(area(F1) + 1e-9, 2) == 41.41
assert round(area(R1_N), 4) == 11.5934 and round(area(R1_S), 4) == 29.8116
assert round(area(F2), 4) == 33.124 and trunc2(area(F2)) == 33.12
assert round(area(R2_N), 4) == 8.281 and round(area(R2_S), 4) == 24.843
assert round(area(F3), 4) == 8.281 and trunc2(area(F3)) == 8.28
assert round(area(LOFT), 4) == 6.6248 and trunc2(area(LOFT)) == 6.62
assert round(5.46 * 6.37, 4) == 34.7802 and round(5.46 * 7.28, 4) == 39.7488

# ---- 敷地と建物の位置（原点＝3番4の北西の角、(東, 南)） ----
LOT = rect(0, 0, 10.00, 13.10)
T = 0.18                                  # 壁厚（問題文の注2）
DE, DS = 1.00 + T / 2, 1.10 + 2.00 + T / 2   # 壁の中心線：西の筆界から1.09、道路境界線から3.19
B1 = shift(F1, DE, DS)
assert round(area(LOT), 2) == 131.00
assert round(DE, 2) == 1.09 and round(DS, 2) == 3.19
E_OUT, S_OUT = DE + 6.37 + T / 2, DS + 7.28 + T / 2        # 東の外壁 7.55、南の外壁 10.56
assert round(10.00 - E_OUT, 2) == 2.45 and round(13.10 - S_OUT, 2) == 2.54


def neighbors(z, fs=14):
    """隣接地の地番（〔配置図〕どおり）。"""
    for e, s, t in [(-2.2, 6.5, '3－3'), (12.2, 6.5, '3－5'), (5.0, 14.6, '3－11'), (-2.2, 14.6, '3－12'), (12.2, 14.6, '3－10')]:
        z.free_text(P(e, s), t, fs=fs, color=GRAY)


def lot_lines(z):
    """敷地と、筆界の延長（隣接地との境）。"""
    z.poly(LOT, color=BLACK, lw=2.2)
    z.line(P(0, 13.10), P(0, 16.0), color=BLACK, lw=1.4)
    z.line(P(10, 13.10), P(10, 16.0), color=BLACK, lw=1.4)
    z.line(P(-3.6, 13.10), P(0, 13.10), color=BLACK, lw=1.4)
    z.line(P(10, 13.10), P(13.6, 13.10), color=BLACK, lw=1.4)


def zu01():
    fig, axes = new_figure('3番4の敷地の確認（作図チェック用。辺長は建物図面には書かない）',
                           '〔配置図〕：東西10.00×南北13.10の長方形（角は直角）。道路の幅1.80、中心線は道路境界線から0.90北。\n'
                           '道路後退線は中心線から2.00（道路境界線から1.10南）。後退部分は分筆しない（調査結果11）ので、筆界は道路境界線のまま',
                           w=16, h=13)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    fit(ax, LOT, margin=0.10, extra=[xy(P(-5.5, -3.6)), xy(P(16.5, 16.2))], pad_aspect=True)
    z.poly(LOT, color=BLACK, lw=0, fill=BLUE, alpha=0.08, check=False)
    lot_lines(z)
    z.line(P(-3.6, -1.80), P(10.6, -1.80), color=BLACK, lw=1.6)
    z.line(P(-3.6, 0), P(0, 0), color=BLACK, lw=1.6)
    z.line(P(10, 0), P(10.6, 0), color=BLACK, lw=1.6)
    z.line(P(-3.6, -0.90), P(10.6, -0.90), color=GRAY, lw=1.3, ls='-.')
    z.line(P(0, 1.10), P(10, 1.10), color=RED, lw=1.6, ls='--')
    z.poly(B1, color=GRAY, lw=1.4, ls=':')
    for p, q, r in [(P(0, 0), P(10, 0), P(0, 13.1)), (P(10, 0), P(0, 0), P(10, 13.1)),
                    (P(0, 13.1), P(10, 13.1), P(0, 0)), (P(10, 13.1), P(0, 13.1), P(10, 0))]:
        z.right_angle(p, q, r, size=0.55)
    z.north_arrow()
    c = centroid(LOT)
    z.edge_label(P(0, 13.1), P(10, 13.1), '（10.00）', c, fs=14)
    z.edge_label(P(0, 0), P(0, 13.1), '（13.10）', c, fs=14, ts=(0.62, 0.72, 0.5))
    z.edge_label(P(10, 0), P(10, 13.1), '（13.10）', c, fs=14, ts=(0.62, 0.72, 0.5))
    # 道路側の寸法（敷地の東の外に縦に並べる）
    arrow(z, P(11.6, -1.80), P(11.6, 0), both=True)
    arrow(z, P(11.6, 0), P(11.6, 1.10), both=True)
    arrow(z, P(13.8, -0.90), P(13.8, 1.10), both=True)
    z.line(P(10.6, -1.80), P(14.3, -1.80), color=GRAY, lw=0.8)
    z.line(P(10.6, -0.90), P(14.3, -0.90), color=GRAY, lw=0.8)
    z.line(P(10.6, 0), P(14.3, 0), color=GRAY, lw=0.8)
    z.line(P(10.0, 1.10), P(14.3, 1.10), color=GRAY, lw=0.8)
    z.free_text(P(11.6, -1.35), '1.80', fs=12, ha='left', offsets=((8, 0), (10, 0)))
    z.free_text(P(11.6, 0.55), '1.10', fs=12, ha='left', offsets=((8, 0), (10, 0)))
    z.free_text(P(13.8, 0.3), '2.00', fs=12, ha='left', offsets=((8, 0), (10, 0)))
    # 建物までの距離
    arrow(z, P(1.6, 1.10), P(1.6, 3.10))
    arrow(z, P(3.2, 0), P(3.2, 3.10))
    z.free_text(P(1.6, 2.1), '2.00', fs=12, ha='right', offsets=((-8, 0), (-10, 0)))
    z.free_text(P(3.2, 2.55), '1.10＋2.00＝3.10', fs=13, color=RED, ha='left', offsets=((10, 0), (12, 0)))
    z.free_text(P(4.0, -2.55), '道　路（幅1.80）', fs=14, color=GRAY)
    z.free_text(P(-3.5, -1.35), '道路の中心線', fs=12, color=GRAY, ha='left')
    z.free_text(P(-3.5, 0.55), '道路境界線＝筆界', fs=12, color=BLUE, ha='left')
    z.free_text(P(9.8, 1.55), '道路後退線（筆界ではない）', fs=12, color=RED, ha='right', offsets=((0, 0), (0, -4)))
    z.free_text(P(4.2, 11.6), '3－4（10.00×13.10）', fs=15)
    z.free_text(P(3.8, 7.0), '建物の位置（点線）', fs=12, color=GRAY)
    neighbors(z)
    save(fig, [z], 'H21_dai22mon_zu01_shikichi_kakunin')


def zu02():
    fig, axes = new_figure('建物図面の完成形（縮尺500分の1）',
                           '1階の形を壁の中心線で描く（不動産登記規則第82条第1項）。距離は外壁まで（問題文の注3）。\n'
                           '北は道路後退線ではなく道路境界線（筆界）から3.10、西は1.00を2か所。建物の所在は「A市B町二丁目3番地4」',
                           w=16, h=13)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    fit(ax, LOT, margin=0.10, extra=[xy(P(-4.0, -3.0)), xy(P(15.0, 16.2))], pad_aspect=True)
    lot_lines(z)
    z.line(P(-3.6, 0), P(0, 0), color=BLACK, lw=1.6)
    z.line(P(10, 0), P(13.6, 0), color=BLACK, lw=1.6)
    z.line(P(-3.6, -1.80), P(13.6, -1.80), color=BLACK, lw=1.6)
    z.poly(B1, color=BLACK, lw=2.4)
    z.north_arrow()
    wall_n, wall_w = DS - T / 2, DE - T / 2      # 北の外壁 3.10、西の外壁 1.00
    arrow(z, P(1.9, 0), P(1.9, wall_n))
    arrow(z, P(0, DS + 0.7), P(wall_w, DS + 0.7))
    arrow(z, P(0, DS + 6.6), P(wall_w, DS + 6.6))
    z.free_text(P(1.9, 1.55), '3.10', fs=14, ha='left', offsets=((8, 0), (10, 0)))
    z.free_text(P(0, DS + 0.7), '1.00', fs=14, ha='right', offsets=((-8, 0), (-12, 0)))
    z.free_text(P(0, DS + 6.6), '1.00', fs=14, ha='right', offsets=((-8, 0), (-12, 0)))
    z.free_text(P(8.4, 11.6), '3－4', fs=16)
    z.free_text(P(5.0, -0.9), '道　路', fs=15)
    neighbors(z, fs=15)
    save(fig, [z], 'H21_dai22mon_zu02_tatemono_zumen')


# ---- 断面（ロフト）：(東, 高さ)。屋根は外壁で0.80、押入とロフトの境・ロフトの東の端で1.20、中央で2.00 ----
SLOPE = (1.20 - 0.80) / 0.91


def roof_h(e):
    return 2.00 - SLOPE * abs(e - 2.73)


assert round(roof_h(0), 2) == 0.80 and round(roof_h(0.91), 2) == 1.20 and round(roof_h(4.55), 2) == 1.20
assert round(roof_h(2.73), 2) == 2.00 and round(roof_h(5.46), 2) == 0.80
E15 = 2.73 - (2.00 - 1.50) / SLOPE           # 天井の高さが1.5mになる位置 1.5925
assert round(E15, 4) == 1.5925


def zu03():
    fig, axes = new_figure('ロフトは何階？　天井の最高部で1.5mを判定する（断面の模式図）',
                           '天井の高さ1.5m未満の屋階（特殊階）は階数・床面積に入れない（準則第81条第4項・第82条第1号）。\n'
                           'このロフトは最高部2.00で1.5m以上 → 特殊階ではない → 3階に数え、押入も含めて4.55×1.82＝8.28㎡（1室の一部が低くても算入）',
                           w=16, h=8.6)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    fit(ax, [Q(-3.0, -0.9), Q(8.9, 3.1)], margin=0.03, pad_aspect=True)
    roof = [Q(-0.35, roof_h(0) - 0.35 * SLOPE), Q(2.73, 2.00), Q(5.81, roof_h(5.46) - 0.35 * SLOPE)]
    z.poly(roof, color=BLACK, lw=2.6, closed=False)
    loft_area = [Q(0, 0), Q(0, 0.80), Q(2.73, 2.00), Q(4.55, 1.20), Q(4.55, 0)]
    z.poly(loft_area, color=BLACK, lw=0, fill=GREEN, alpha=0.14, check=False)
    high = [Q(E15, 1.5), Q(2.73, 2.00), Q(2.73 + (2.73 - E15), 1.5)]
    z.poly(high, color=GREEN, lw=0, fill=GREEN, alpha=0.30, check=False)
    z.line(Q(0, 0), Q(5.46, 0), color=BLACK, lw=2.4)                  # ロフトの床（2階の天井）
    z.line(Q(0, -0.6), Q(0, 0.80), color=BLACK, lw=2.4)               # 西の外壁
    z.line(Q(0.91, 0), Q(0.91, 1.20), color=BLACK, lw=1.6)            # 押入とロフトの境
    z.line(Q(4.55, -0.6), Q(4.55, 1.20), color=BLACK, lw=1.6)         # ロフトの東の端（吹抜との境）
    z.line(Q(5.46, -0.6), Q(5.46, 0.80), color=BLACK, lw=2.4)         # 東の外壁
    z.line(Q(-0.6, 1.5), Q(6.1, 1.5), color=RED, lw=1.8, ls='--')
    z.free_text(Q(6.1, 1.5), '天井の高さ1.5m', fs=13, color=RED, ha='left', offsets=((8, 0), (8, 10)))
    for e, t_, off, ha in [(0.14, '0.80', (-10, 0), 'right'), (1.05, '1.20', (8, 0), 'left'), (2.87, '2.00', (8, -12), 'left'),
                           (4.41, '1.20', (-8, 0), 'right')]:
        arrow(z, Q(e, 0), Q(e, roof_h(e) - 0.02), both=True)
        tx = e - 0.14 if e == 0.14 else e
        z.free_text(Q(tx if e != 0.14 else -0.05, roof_h(e) / 2), t_, fs=13, ha=ha, offsets=(off, (off[0] * 1.5, off[1])))
    z.free_text(Q(0.455, 0.22), '押入', fs=12)
    z.free_text(Q(3.7, 0.30), 'ロフト（3階）', fs=14, weight='bold')
    z.free_text(Q(5.0, -0.3), '吹抜', fs=12, color=GRAY)
    z.free_text(Q(2.3, -0.35), '2階（ウォークインクローゼット）', fs=12, color=GRAY)
    z.free_text(Q(-2.9, 2.55), '誤り：「ロフト」だから数えない\n→ 2階建（3階の8.28が抜ける）', fs=14, color=RED, ha='left')
    z.free_text(Q(5.0, 2.65), '正解：最高部2.00は1.5m以上\n→ 特殊階ではない → 3階建', fs=14, color=GREEN, ha='left')
    save(fig, [z], 'H21_dai22mon_zu03_loft_ayamari_hikaku')


def zu04():
    fig, axes = new_figure('1階の求積図（2つの長方形に分けて足す）',
                           '6.37×1.82＝11.5934（北の帯、北東の角の玄関の張り出しを含む）＋ 5.46×5.46＝29.8116（南の本体）\n'
                           '＝ 41.4050 → 41.40㎡（1平方メートルの100分の1未満は切り捨て。四捨五入の41.41ではない）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fit(ax, F1, margin=0.16, extra=[xy(P(2.73, 9.6))], pad_aspect=True)
    z.poly(R1_N, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(R1_S, color=GREEN, lw=0, fill=GREEN, check=False)
    z.line(P(0, 1.82), P(5.46, 1.82), color=GRAY, lw=1.2, ls='--')
    z.poly(F1, color=BLACK, lw=2.4)
    z.north_arrow()
    dims(z, F1, ['6.37', '1.82', None, '5.46', '5.46', '7.28'])
    z.free_text(P(5.915, 1.82), '0.91', fs=14, offsets=((0, -21), (0, -25)))
    z.free_text(P(3.2, 0.91), '6.37×1.82＝11.5934', fs=14, color=BLUE)
    z.free_text(P(2.73, 4.55), '5.46×5.46\n＝29.8116', fs=16, color=GREEN)
    z.free_text(P(2.73, 9.0), '合計 41.4050 → 41.40㎡', fs=17, weight='bold')
    save(fig, [z], 'H21_dai22mon_zu04_1kai_kyuuseki')


def zu05():
    fig, axes = new_figure('2階の求積図（吹抜とベランダは入れない）',
                           '4.55×1.82＝8.2810（北の帯、北東の吹抜0.91×1.82を除く）＋ 5.46×4.55＝24.8430 ＝ 33.1240 → 33.12㎡\n'
                           '吹抜の部分は上の階の床面積に入れない（準則第82条第8号）。ベランダは洋室の南の壁の外。点線は1階の位置',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fit(ax, F1, margin=0.16, extra=[xy(P(-1.0, 9.8)), xy(P(9.5, -1.0))], pad_aspect=True)
    z.poly(F1, color=GRAY, lw=1.3, ls='--')
    z.poly(R2_N, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(R2_S, color=GREEN, lw=0, fill=GREEN, check=False)
    hatch(z, FUKINUKE)
    hatch(z, BERANDA)
    z.line(P(0, 1.82), P(4.55, 1.82), color=GRAY, lw=1.2, ls='--')
    z.poly(F2, color=BLACK, lw=2.4)
    z.north_arrow()
    dims(z, F2, ['4.55', None, None, '4.55', None, '6.37'])
    z.free_text(P(2.3, 0.91), '4.55×1.82＝8.2810', fs=14, color=BLUE)
    z.free_text(P(2.73, 4.1), '5.46×4.55\n＝24.8430', fs=16, color=GREEN)
    z.callout(P(5.0, 0.9), '吹抜（0.91×1.82）\n床がない＝入れない', dirs=(20, 0, 40), dists=(80, 100, 120), fs=12, color=RED)
    z.callout(P(2.73, 6.82), 'ベランダ（南の0.91）\n壁と屋根に囲まれていない＝入れない', dirs=(-90, -70, -110), dists=(45, 60, 75), fs=12,
              color=RED)
    z.free_text(P(2.73, 9.4), '合計 33.1240 → 33.12㎡', fs=17, weight='bold')
    save(fig, [z], 'H21_dai22mon_zu05_2kai_kyuuseki')


def zu06():
    fig, axes = new_figure('3階（ロフト）の求積図（押入も含める）',
                           '2階のウォークインクローゼットの真上、北西の角の4.55×1.82＝8.2810 → 8.28㎡。点線は1階の位置。\n'
                           '押入（0.91）の天井が低くても、1室の一部が1.5m未満の部分は算入する（準則第82条第1号ただし書）。3.64×1.82＝6.62は誤り',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fit(ax, F1, margin=0.16, pad_aspect=True)
    z.poly(F1, color=GRAY, lw=1.3, ls='--')
    z.poly(OSHIIRE, color=ORANGE, lw=0, fill=ORANGE, alpha=0.30, check=False)
    z.poly(LOFT, color=BLUE, lw=0, fill=BLUE, check=False)
    z.line(P(0.91, 0), P(0.91, 1.82), color=GRAY, lw=1.2, ls='--')
    z.poly(F3, color=BLACK, lw=2.4)
    z.north_arrow()
    dims(z, F3, ['4.55', '1.82', None, None])
    z.free_text(P(0.455, 0.91), '押入', fs=12)
    z.free_text(P(2.73, 0.91), 'ロフト', fs=14)
    z.callout(P(2.73, 1.82), '南の辺は手すり（固定式ハシゴ階段で2階へ）', dirs=(-90, -70, -110), dists=(40, 55, 70), fs=12, color=GRAY)
    z.free_text(P(2.73, 4.9), '4.55×1.82＝8.2810 → 8.28㎡', fs=17, weight='bold')
    z.free_text(P(2.73, 6.1), '誤り：押入を除く 3.64×1.82＝6.6248 → 6.62', fs=14, color=RED)
    save(fig, [z], 'H21_dai22mon_zu06_3kai_kyuuseki')


def zu07():
    fig, axes = new_figure('各階平面図の完成形（縮尺250分の1）',
                           '各階の別・形・1階の位置・周囲の長さ・床面積と求積方法を書く（不動産登記規則第83条第1項）。\n'
                           '2階・3階には1階の位置を点線で重ねる（準則第53条）',
                           w=18, h=9.4, ncols=3)
    fig.subplots_adjust(top=0.85, wspace=0.10)
    zs = []
    for ax, title, shape, kyu in [
            (axes[0], '1階', F1, '6.37×1.82＝11.5934\n5.46×5.46＝29.8116\n計 41.4050\n床面積 41.40㎡'),
            (axes[1], '2階', F2, '4.55×1.82＝8.2810\n5.46×4.55＝24.8430\n計 33.1240\n床面積 33.12㎡'),
            (axes[2], '3階', F3, '4.55×1.82＝8.2810\n床面積 8.28㎡')]:
        z = Zu(ax, fontsize=13)
        fit(ax, F1, margin=0.12, extra=[xy(P(2.73, 12.4)), xy(P(-1.0, -1.0)), xy(P(7.4, -1.0))], pad_aspect=True)
        if shape is not F1:
            z.poly(F1, color=GRAY, lw=1.2, ls='--')
        z.poly(shape, color=BLACK, lw=2.2)
        if shape is F1:
            dims(z, shape, ['6.37', '1.82', None, '5.46', '5.46', '7.28'])
            z.free_text(P(5.95, 1.82), '0.91', fs=11, offsets=((0, -18), (0, -22)))
        elif shape is F2:
            dims(z, shape, ['4.55', None, None, '4.55', '5.46', '6.37'])
            z.free_text(P(4.55, 0.91), '1.82', fs=13, rotation=90, offsets=((-14, 0), (-18, 0)))
            z.free_text(P(5.2, 1.82), '0.91', fs=12, offsets=((0, 18), (0, 22)))
        else:
            dims(z, shape, ['4.55', '1.82', None, None])
        z.free_text(P(2.73, 10.1), kyu, fs=13)
        ax.set_title(title, fontsize=18, weight='bold')
        zs.append(z)
    save(fig, zs, 'H21_dai22mon_zu07_kakai_heimenzu')


def zu08():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　ロフトの階数を先に決める', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '問を先に読む', '問1〜問3と\n問題文の注', BLUE),
        ('②', '調査結果と\n断面図のメモ', 'ロフト2.00・吹抜\n屋根2種類・通し柱\n後退線', BLUE),
        ('③', '申請書の\n床面積以外\nと問2', '目的・添付書類\n申請人・原因の日付\n確認済証など', BLUE),
        ('④', '床面積3つ\nと階数', '41.40（切捨て）\n33.12・8.28\n3階建', GREEN),
        ('⑤', '各階平面図と\n建物図面', '（その2）\n3.10・1.00', RED),
        ('⑥', '見直し', '41.41にして\nいないか・\n合金メッキ鋼板', GRAY),
    ]
    w, h, gap = 14.5, 42, 2.0
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 22), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 22 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
        ax.text(x + w / 2, 22 + h / 2 - 4, t, ha='center', va='center', fontsize=17)
        ax.text(x + w / 2, 18, ran, ha='center', va='top', fontsize=14, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, 43), xytext=(x + w + 0.2, 43),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 1.5 * (w + gap) - gap / 2, 76, '計算しなくても書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 3 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 4 * (w + gap) - gap / 2, 76, '時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 5 * (w + gap) - gap, 72), xytext=(1 + 3 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '計算は長方形5つだけ。ロフトを階に数えるかどうかは、構造の階数・床面積・各階平面図のすべてに響くので②で決める。\n'
             '申請書と問2を先に仕上げておけば、作図で時間が足りなくなっても点は取れている。',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'H21_dai22mon_zu08_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図8: 解く順番（固定配置）\n  →', path)


if __name__ == '__main__':
    zu01()
    zu02()
    zu03()
    zu04()
    zu05()
    zu06()
    zu07()
    zu08()
    print('重なり合計:', len(PROBLEMS))
