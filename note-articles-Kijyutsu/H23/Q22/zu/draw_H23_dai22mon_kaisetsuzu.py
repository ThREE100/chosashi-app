"""平成23年度 第22問（建物）の解説図7枚を、座標・辺長から作図してPNGに書き出す。

`../prompt_H23_dai22mon_kaisetsuzu.md` の図1〜図7どおり。作図の共通部品は `tools/zu_helpers.py`。
- 敷地・建物図面（図2・図3）は、問題の「A〜Jの筆界点に関する座標リスト」の座標（X＝北、Y＝東）をそのまま使う
- 各階の形（図1・図4〜図6）は、建物の北西の角を原点にした (東, 南) で持ち、P() で zu_helpers の (北, 東) に変換する
実行: python3 note-articles-Kijyutsu/H23/Q22/zu/draw_H23_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
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


def Z(x, y):
    """座標リストの (X, Y) をそのまま複素数にする。"""
    return complex(x, y)


def rect(e0, s0, e1, s1):
    return [P(e0, s0), P(e1, s0), P(e1, s1), P(e0, s1)]


def zrect(x0, y0, x1, y1):
    """座標系（X＝北、Y＝東）の長方形。x0 が南、x1 が北、y0 が西、y1 が東。"""
    return [Z(x1, y0), Z(x1, y1), Z(x0, y1), Z(x0, y0)]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


def trunc2(v):
    import math
    return math.floor(v * 100 + 1e-9) / 100


def hatch(ax, pts, color=GRAY, pattern='///'):
    ax.add_patch(MPoly([xy(p) for p in pts], closed=True, fill=False, hatch=pattern, edgecolor=color, lw=0, zorder=1))


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


# ---- 座標リスト（問題文） ----
A, B, C, D, E = Z(254.43, 187.17), Z(241.25, 187.17), Z(239.25, 185.17), Z(239.25, 163.79), Z(254.43, 163.79)
F, G, H, I, J = Z(233.25, 193.63), Z(207.84, 190.15), Z(209.39, 175.36), Z(211.13, 158.65), Z(233.25, 158.65)
LOT52 = [E, A, B, C, D]
LOT101 = [J, F, G, H, I]
assert round(area(LOT52), 4) == 352.9084 and round(area(LOT101), 5) == 792.72795
assert trunc2(area(LOT52)) == 352.90 and trunc2(area(LOT101)) == 792.72

# ---- 建物の位置（壁の中心線。距離は外壁まで、壁厚12cm → 中心線は外壁から0.06内側） ----
WN = 254.43 - 1.0 - 0.06                  # 5番2の北の壁の中心線 253.37
WE_OLD = 187.17 - 7.0 - 0.06              # 増築前の東の壁の中心線 180.11
WW = WE_OLD - 10.01                       # 西の壁の中心線 170.10
WE_NEW = WE_OLD + 2.50                    # 増築部分の東の壁の中心線 182.61
assert round(WN, 2) == 253.37 and round(WE_OLD, 2) == 180.11 and round(WW, 2) == 170.10 and round(WE_NEW, 2) == 182.61
assert round(187.17 - (WE_NEW + 0.06), 2) == 4.50        # 建物図面の東の距離 7.0 − 2.5 ＝ 4.5
OMOYA = [Z(WN, WW), Z(WN, WE_NEW), Z(WN - 6.37, WE_NEW), Z(WN - 6.37, WE_OLD), Z(WN - 9.10, WE_OLD),
         Z(WN - 9.10, WW + 4.55), Z(WN - 7.28, WW + 4.55), Z(WN - 7.28, WW)]
assert round(area(OMOYA), 4) == 98.735
# 車庫（一棟）：北はシャッターの中心の線（厚さは考えない）で北の筆界から1.0、東は北東の角で東の筆界（F→G）から5.0
GN = 233.25 - 1.0
Y_FG = F.imag - (F.real - GN) * (F.imag - G.imag) / (F.real - G.real)    # 193.4930…
GE = Y_FG - 5.0 - 0.06                                                    # 東のブロック壁の中心線 188.4330…
GE = round(GE, 2)
GMID, GW, GS = GE - 4.50, GE - 9.00, GN - 5.50
ITTO = zrect(GS, GW, GN, GE)
SENYU = zrect(GS + 0.06, GW + 0.06, GN, GMID - 0.06)   # 5番2の符号1（内法）
KIZON = zrect(GS, GMID, GN, GE)                        # 10番1の符号1（既存の車庫）
assert round(area(ITTO), 2) == 49.50 and round(area(SENYU), 4) == 23.8272
assert GW - 0.06 > J.imag and GS - 0.06 > 209.0        # 一棟は10番1の中（西・南の筆界まで十分ある）


def zu01():
    fig, axes = new_figure('車庫の「増築」の正体：一棟の建物に区分建物が2つ',
                           '〔コンクリートブロック造の車庫の詳細図〕をもとにした平面図（図の上が北＝道路側のシャッター）。問題文の注9：利用上・構造上の独立性がある。\n'
                           '一棟の建物はコンクリートブロック造陸屋根平家建、9.00×5.50＝49.50㎡（壁心）。所有者の違う2つの区分建物になる',
                           w=16, h=9)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    west, east = rect(0, 0, 4.5, 5.5), rect(4.5, 0, 9.0, 5.5)
    z.poly(west, color=BLACK, lw=0, fill=ORANGE, alpha=0.30, check=False)
    z.poly(east, color=BLACK, lw=0, fill=BLUE, alpha=0.22, check=False)
    for p, q in [(P(0, 0), P(0, 5.5)), (P(0, 5.5), P(9, 5.5)), (P(9, 5.5), P(9, 0)), (P(4.5, 0), P(4.5, 5.5))]:
        z.line(p, q, color=BLACK, lw=5.5)
    z.line(P(0, 0), P(9, 0), color=GRAY, lw=2.0, ls='--')
    z.free_text(P(2.25, -0.45), 'シャッター', fs=13, color=GRAY)
    z.free_text(P(6.75, -0.45), 'シャッター', fs=13, color=GRAY)
    z.free_text(P(2.25, 1.5), '増築した車庫', fs=16, weight='bold')
    z.free_text(P(2.25, 2.7), '所有者：畑山邦彦\n（費用を負担）', fs=13)
    z.free_text(P(2.25, 4.2), '5番2の符号1\n（区分建物）', fs=15, color=RED, weight='bold')
    z.free_text(P(6.75, 1.5), '増築前の車庫', fs=16, weight='bold')
    z.free_text(P(6.75, 2.7), '所有者：海野商事・\n海野洋子の共有', fs=13)
    z.free_text(P(6.75, 4.2), '10番1の符号1\n（区分建物になる）', fs=15, color=BLUE, weight='bold')
    z.edge_label(P(0, 5.5), P(4.5, 5.5), '4.50', centroid(west), fs=14)
    z.edge_label(P(4.5, 5.5), P(9, 5.5), '4.50', centroid(east), fs=14)
    z.edge_label(P(0, 0), P(0, 5.5), '5.50', centroid(west), fs=14)
    z.edge_label(P(9, 0), P(9, 5.5), '5.50', centroid(east), fs=14)
    z.callout(P(4.5, 5.2), '間の壁で仕切られ、\nそれぞれ道路側の\nシャッターから出入りできる', dirs=(-20, -10, -35), dists=(90, 120, 150), fs=13, color=PURPLE)
    fit(ax, rect(0, 0, 9, 5.5), margin=0.10, extra=[xy(P(-1.2, 7.5)), xy(P(14.5, -1.0))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H23_dai22mon_zu01_ittou_kankei')


def zu02():
    fig, axes = new_figure('敷地の確認（作図チェック用。辺長・面積は建物図面には書かない）',
                           '座標リストの座標から描いた5番2と10番1。道路の幅は239.25−233.25＝6.00。\n'
                           '10番1は座標の面積792.72㎡で登記記録792.95㎡とほぼ一致。5番2は352.90㎡で登記記録357.70㎡より約4.8㎡少ない（形は座標どおりに描く）',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    z.poly(LOT52, color=BLACK, lw=2.2, fill=BLUE, alpha=0.10)
    z.poly(LOT101, color=BLACK, lw=2.2, fill=GREEN, alpha=0.10)
    c52, c101 = centroid(LOT52), centroid(LOT101)
    for pts, c, labels in [(LOT52, c52, ['23.38', '13.18', None, '21.38', '15.18']),
                           (LOT101, c101, ['34.98', '25.65', '14.87', '16.80', '22.12'])]:
        for i, t in enumerate(labels):
            if t:
                z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=13, outward=(t not in ('21.38', '34.98')))
    for p, n, c in [(A, 'A', c52), (B, 'B', c52), (C, 'C', c52), (D, 'D', c52), (E, 'E', c52),
                    (F, 'F', c101), (G, 'G', c101), (H, 'H', c101), (I, 'I', c101), (J, 'J', c101)]:
        z.point(p, 'dot', size=6)
        z.point_label(p, n, away=c, fs=14)
    z.free_text(c52, '5番2\n352.90㎡\n（登記記録357.70㎡）', fs=14)
    z.free_text(c101, '10番1\n792.72㎡\n（登記記録792.95㎡）', fs=14)
    z.free_text(Z(236.25, 176.0), '道　路（幅6.00）', fs=14, color=GRAY)
    z.callout((B + C) / 2, '隅切り BC 2.83', dirs=(-20, 0, -40), fs=12)
    z.free_text(Z(260.0, 175.5), '6', fs=14, color=GRAY)
    z.free_text(Z(247.0, 157.5), '5－1', fs=14, color=GRAY)
    z.free_text(Z(222.0, 152.5), '10－2', fs=14, color=GRAY)
    z.free_text(Z(222.0, 197.5), '10－3', fs=14, color=GRAY)
    z.free_text(Z(205.5, 166.0), '11－4', fs=14, color=GRAY)
    z.free_text(Z(203.5, 184.0), '11－20', fs=14, color=GRAY)
    fit(ax, LOT52 + LOT101, margin=0.08, extra=[xy(Z(262.5, 150.0)), xy(Z(200.0, 200.0))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H23_dai22mon_zu02_shikichi_kakunin')


def zu03():
    fig, axes = new_figure('建物図面の完成形（家屋番号5番2　縮尺500分の1）',
                           '主である建物と符号1（実線）、符号1の属する一棟の建物の1階（点線）。距離は外壁まで（問題文の注5）、小数第1位。\n'
                           '行政界（二丁目と五丁目の境）を一点鎖線で示す。建物の所在は「A市B町二丁目5番地2、A市B町五丁目10番地1」',
                           w=16, h=13)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    z.poly(LOT52, color=BLACK, lw=1.8)
    z.poly(LOT101, color=BLACK, lw=1.8)
    z.line(Z(239.10, 156.0), Z(239.10, 196.5), color=BLACK, lw=1.4, ls='-.')   # 行政界（道路の北の端）
    z.poly(OMOYA, color=BLACK, lw=2.2)
    z.poly(KIZON, color=BLACK, lw=1.6, ls='--')
    z.poly(zrect(GS, GW, GN, GMID), color=BLACK, lw=2.2)
    z.free_text(centroid(OMOYA), '主', fs=15, weight='bold')
    z.free_text(centroid(zrect(GS, GW, GN, GMID)), '符号1', fs=12, weight='bold')
    # 距離（矢印と数値）
    for (p, q) in [(Z(254.43, WW - 0.06), Z(WN + 0.06, WW - 0.06)), (Z(254.43, WE_NEW + 0.06), Z(WN + 0.06, WE_NEW + 0.06)),
                   (Z(WN - 1.5, 187.17), Z(WN - 1.5, WE_NEW + 0.06)),
                   (Z(233.25, GMID), Z(GN, GMID)), (Z(233.25, GE + 0.06), Z(GN, GE + 0.06)),
                   (Z(GN - 0.3, Y_FG - 0.04), Z(GN - 0.3, GE + 0.06))]:
        ax.annotate('', xy=xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='-|>', lw=1.1, color=BLACK, mutation_scale=10))
        z.segments.append((xy(p), xy(q)))
    z.free_text(Z(255.4, WW - 0.06), '1.0', fs=12, offsets=((0, 0), (-12, 0), (12, 0)))
    z.free_text(Z(255.4, WE_NEW + 0.06), '1.0', fs=12, offsets=((0, 0), (-12, 0), (12, 0)))
    z.free_text(Z(WN - 2.6, 184.9), '4.5', fs=12, offsets=((0, 0), (0, -6)))
    z.free_text(Z(234.2, GMID), '1.0', fs=12, offsets=((-14, 0), (-18, 0), (14, 0)))
    z.free_text(Z(234.2, GE + 0.06), '1.0', fs=12, offsets=((14, 0), (18, 0), (-14, 0)))
    z.free_text(Z(GN - 1.4, 191.0), '5.0', fs=12, offsets=((0, 0), (0, -6)))
    for p, t in [(Z(241.9, 169.0), '5－2'), (Z(218.0, 175.0), '10－1'), (Z(262.0, 175.5), '6'), (Z(247.0, 157.5), '5－1'),
                 (Z(222.0, 152.5), '10－2'), (Z(222.0, 197.5), '10－3'), (Z(202.5, 167.0), '11－4'),
                 (Z(201.0, 184.0), '11－20')]:
        z.free_text(p, t, fs=13)
    z.free_text(Z(236.0, 170.0), '道　路', fs=13)
    z.free_text(Z(248.0, 191.8), '道\n路', fs=13)
    z.free_text(Z(240.1, 198.2), 'A市B町二丁目', fs=12, ha='left')
    z.free_text(Z(237.9, 198.2), 'A市B町五丁目', fs=12, ha='left')
    fit(ax, LOT52 + LOT101, margin=0.10, extra=[xy(Z(262.5, 150.0)), xy(Z(199.0, 207.0))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H23_dai22mon_zu03_tatemono_zumen')


# ---- 主である建物（原点＝1階の北西の角、東・南） ----
F1 = [P(0, 0), P(12.51, 0), P(12.51, 6.37), P(10.01, 6.37), P(10.01, 9.10), P(4.55, 9.10), P(4.55, 7.28), P(0, 7.28)]
R_OLD, R_MINAMI, R_ZOU = rect(0, 0, 10.01, 7.28), rect(4.55, 7.28, 10.01, 9.10), rect(10.01, 0, 12.51, 6.37)
F2 = rect(0.91, 0, 10.01, 7.28)
assert round(area(F1), 4) == 98.735 and trunc2(area(F1)) == 98.73
assert round(area(R_OLD), 4) == 72.8728 and round(area(R_MINAMI), 4) == 9.9372 and round(area(R_ZOU), 4) == 15.925
assert round(area(F2), 3) == 66.248 and trunc2(area(F2)) == 66.24


def zu04():
    fig, axes = new_figure('主である建物の求積図（1階は増築、2階は変わらない）',
                           '1階：10.01×7.28＝72.8728 ＋ 5.46×1.82＝9.9372 ＋ 2.50×6.37＝15.9250 ＝ 98.7350 → 98.73㎡（四捨五入の98.74ではない）\n'
                           '2階：9.10×7.28＝66.2480 → 66.24㎡（登記記録と同じ）。点線は1階の位置',
                           w=17, h=8.2, ncols=2, width_ratios=[1.2, 1])
    fig.subplots_adjust(top=0.84)
    z = Zu(axes[0], fontsize=13)
    z.poly(R_OLD, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(R_MINAMI, color=GREEN, lw=0, fill=GREEN, check=False)
    z.poly(R_ZOU, color=RED, lw=0, fill=RED, alpha=0.30, check=False)
    z.line(P(10.01, 0), P(10.01, 6.37), color=GRAY, lw=1.2, ls='--')
    z.line(P(4.55, 7.28), P(10.01, 7.28), color=GRAY, lw=1.2, ls='--')
    z.poly(F1, color=BLACK, lw=2.4)
    dims(z, F1, ['12.51', '6.37', '2.50', '2.73', '5.46', '1.82', '4.55', '7.28'])
    z.free_text(P(5.0, 3.4), '10.01×7.28\n＝72.8728', fs=14)
    z.free_text(P(7.28, 8.19), '5.46×1.82＝9.9372', fs=12)
    z.free_text(P(11.26, 3.2), '増築\n2.50\n×\n6.37\n＝\n15.9250', fs=12, color=RED)
    axes[0].set_title('1階：98.73㎡', fontsize=18, weight='bold')
    fit(axes[0], F1, margin=0.16, pad_aspect=True)
    z.north_arrow()
    z2 = Zu(axes[1], fontsize=13)
    z2.poly(F1, color=GRAY, lw=1.3, ls='--')
    z2.poly(F2, color=BLACK, lw=2.4, fill=BLUE)
    dims(z2, F2, ['9.10', '7.28', None, '7.28'], outward=False)
    z2.free_text(P(5.46, 3.0), '9.10×7.28\n＝66.2480', fs=14)
    axes[1].set_title('2階：66.24㎡（変更なし）', fontsize=18, weight='bold')
    fit(axes[1], F1, margin=0.16, pad_aspect=True)
    save(fig, [z, z2], 'H23_dai22mon_zu04_omoya_kyuuseki')


# ---- 車庫（5番2の符号1）：原点＝北西の角（シャッターの中心と西の壁の中心の交点） ----
T = 0.12      # ブロック壁の厚さ（問題文の注3）
TD = 0.50     # 作図用に誇張した壁の厚さ（実寸の0.12では見えないので模式図にする）
DW = TD / 2
NG1_REAL, NG2_REAL, OK_REAL = rect(0, 0, 4.5, 5.5), rect(0.06, 0.06, 4.44, 5.44), rect(0.06, 0, 4.44, 5.44)
assert round(area(NG1_REAL), 2) == 24.75 and round(area(NG2_REAL), 4) == 23.5644 and round(area(OK_REAL), 4) == 23.8272
assert trunc2(area(NG2_REAL)) == 23.56 and trunc2(area(OK_REAL)) == 23.82


def garage_panel(ax, title, color, inner, label, note):
    z = Zu(ax, fontsize=13)
    walls = [rect(-DW, 0, DW, 5.5 + DW), rect(-DW, 5.5 - DW, 4.5 + DW, 5.5 + DW), rect(4.5 - DW, 0, 4.5 + DW, 5.5 + DW)]
    for w in walls:
        z.poly(w, color=GRAY, lw=0, fill=GRAY, alpha=0.55, check=False)
    z.line(P(-DW, 0), P(4.5 + DW, 0), color=GRAY, lw=1.6, ls='--')
    z.poly(rect(0, 0, 4.5, 5.5), color=GRAY, lw=1.0, ls=':', check=False)
    z.poly(inner, color=color, lw=2.6, fill=color, alpha=0.16)
    z.free_text(P(2.25, -0.55), 'シャッター（厚さは考えない）', fs=11, color=GRAY)
    z.free_text(P(2.25, 2.5), label, fs=14, color=color, weight='bold')
    z.free_text(P(2.25, 7.3), note, fs=12)
    ax.set_title(title, fontsize=16, weight='bold', color=color)
    fit(ax, rect(-0.6, -1.2, 5.1, 8.3), margin=0.06, pad_aspect=True)
    return z


def zu05():
    fig, axes = new_figure('符号1（区分建物）の床面積：どの線で測るか（模式図・壁の厚さは誇張）',
                           '区分建物は壁その他の区画の内側線で測る（不動産登記規則第115条）。ブロック壁は12cmなので中心から内側まで0.06。\n'
                           'シャッターの厚さは考えない（問題文の注3）ので、北の辺はシャッターの中心のまま。南北は5.50−0.06＝5.44',
                           w=18, h=8.6, ncols=3)
    fig.subplots_adjust(top=0.84, wspace=0.12)
    zs = [garage_panel(axes[0], '誤り：壁の中心で測る', RED, rect(0, 0, 4.5, 5.5), '4.50×5.50\n＝24.75㎡', '灰色の帯＝ブロック壁（厚さ12cm）\n壁心は普通の建物の測り方'),
          garage_panel(axes[1], '誤り：4辺とも0.06引く', RED, rect(DW, DW, 4.5 - DW, 5.5 - DW), '4.38×5.38\n＝23.5644\n→ 23.56㎡',
                       'シャッターの側まで引いている'),
          garage_panel(axes[2], '正解：内側線（北はシャッター）', GREEN, rect(DW, 0, 4.5 - DW, 5.5 - DW),
                       '4.38×5.44\n＝23.8272\n→ 23.82㎡', '東西 4.50−0.06−0.06＝4.38\n南北 5.50−0.06＝5.44')]
    save(fig, zs, 'H23_dai22mon_zu05_shako_ayamari_hikaku')


def zu06():
    fig, axes = new_figure('各階平面図の完成形（縮尺250分の1。求積と床面積の記載は省略してよい：問2）',
                           '主である建物の1階・2階と、附属建物符号1を書き分ける。2階には1階の位置を点線で重ねる（不動産登記規則第83条第1項）。\n'
                           '符号1は区分建物なので内法の寸法（4.38・5.44）で描く',
                           w=18, h=8.4, ncols=3, width_ratios=[1.25, 1.1, 0.75])
    fig.subplots_adjust(top=0.84, wspace=0.10)
    z = Zu(axes[0], fontsize=13)
    z.poly(F1, color=BLACK, lw=2.2)
    dims(z, F1, ['12.51', '6.37', None, None, '5.46', '1.82', '4.55', '7.28'])
    z.free_text(P(11.26, 6.37), '2.50', fs=13, offsets=((6, -14), (10, -16), (0, -20)))
    z.edge_label(P(10.01, 6.37), P(10.01, 9.10), '2.73', centroid(F1), fs=13, ts=(0.72, 0.8, 0.62))
    axes[0].set_title('主である建物　1階', fontsize=16, weight='bold')
    fit(axes[0], F1, margin=0.18, pad_aspect=True)
    z2 = Zu(axes[1], fontsize=13)
    z2.poly(F1, color=BLACK, lw=1.2, ls='--')
    z2.poly(F2, color=BLACK, lw=2.2)
    dims(z2, F2, ['9.10', '7.28', '9.10', '7.28'], outward=False)
    axes[1].set_title('主である建物　2階', fontsize=16, weight='bold')
    fit(axes[1], F1, margin=0.18, pad_aspect=True)
    z3 = Zu(axes[2], fontsize=13)
    g = rect(0, 0, 4.38, 5.44)
    z3.poly(g, color=BLACK, lw=2.2)
    dims(z3, g, ['4.38', '5.44', '4.38', '5.44'])
    axes[2].set_title('附属建物符号1', fontsize=16, weight='bold')
    fit(axes[2], g, margin=0.45, pad_aspect=True)
    save(fig, [z, z2, z3], 'H23_dai22mon_zu06_kakai_heimenzu')


def zu07():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　文章（問3）と作図は後に回す', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '問を先に読む', '問1〜問3と\n注意事項', BLUE),
        ('②', '時系列メモと\n区分建物の判定', '調査の結果1〜4\n問題文の注9', BLUE),
        ('③', '申請書の\n床面積以外', '第1欄\n（敷地権の日付\nまで）', BLUE),
        ('④', '床面積2つ', '98.73（切捨て）\n23.82（内法）', GREEN),
        ('⑤', '各階平面図と\n建物図面', '（その2）\n4.5・町界の\n一点鎖線', RED),
        ('⑥', '問3の文章', '第2欄\n結論・理由・例', RED),
        ('⑦', '見直し', '欄番号③・\n98.74にして\nいないか', GRAY),
    ]
    w, h, gap = 12.2, 42, 1.8
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 22), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 22 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
        ax.text(x + w / 2, 22 + h / 2 - 3, t, ha='center', va='center', fontsize=17)
        ax.text(x + w / 2, 18, ran, ha='center', va='top', fontsize=14, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, 43), xytext=(x + w + 0.2, 43),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 2 * (w + gap) - gap / 2, 76, '計算しなくても書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 3 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 5 * (w + gap) - gap / 2, 76, '時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 6 * (w + gap) - gap, 72), xytext=(1 + 4 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '計算は床面積2つだけ。いちばん時間がかかるのは、2筆の敷地と町界をまたぐ建物図面の作図と、問3の文章。\n'
             '申請書（第1欄）を先に仕上げておけば、作図や文章で時間が足りなくなっても点は取れている。',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'H23_dai22mon_zu07_toku_junban.png')
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
