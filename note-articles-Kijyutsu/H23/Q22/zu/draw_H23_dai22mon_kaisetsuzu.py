"""平成23年度 第22問（建物）の解説図17枚を、座標・辺長から作図してPNGに書き出す。

`../prompt_H23_dai22mon_kaisetsuzu.md` の図1〜図17どおり（図の番号は記事の挿入順。2026-10-05に記事本文に対して足りなかった図10枚を足して振り直した）。作図の共通部品は `tools/zu_helpers.py`。
- 敷地・建物図面（図2・図3）は、問題の「A〜Jの筆界点に関する座標リスト」の座標（X＝北、Y＝東）をそのまま使う
- 各階の形（図1・図4〜図6）は、建物の北西の角を原点にした (東, 南) で持ち、P() で zu_helpers の (北, 東) に変換する
- 図3（建物図面）と図6（各階平面図）の完成形は、試験の答案用紙（その2）の欄（家屋番号・建物の所在、建物図面の申請人〈空欄なので氏名を書く〉・
  縮尺1/500、各階平面図の作成者〈（略）と作成日が印刷済み〉・縮尺1/250）の形の枠の中に描く
  （答案用紙はリポジトリの public/kijutsu/H23-tatemono/a2.webp）。各階平面図の3つ（1階・2階・符号1）は同じ縮尺で1つの作図範囲に並べる
実行: python3 note-articles-Kijyutsu/H23/Q22/zu/draw_H23_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN,  # noqa: E402
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


INK = '#1a3a8f'   # 記入（濃い青）
KAOKU = '5番2'
SHOZAI = 'A市B町二丁目5番地2、A市B町五丁目10番地1'
SHINSEININ = '畑山邦彦'


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.01
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


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


def zu02():
    fig, axes = new_figure('車庫の「増築」の正体：一棟の建物に区分建物が2つ',
                           '〔コンクリートブロック造の車庫の詳細図〕をもとにした平面図（図の上が北＝道路側のシャッター）。問題文の注9：利用上・構造上の独立性がある。\n'
                           '一棟の建物はコンクリートブロック造陸屋根平家建、9.00×5.50＝49.50㎡（壁心）。所有者の違う2つの区分建物になる',
                           w=16, h=9)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    fit(ax, rect(0, 0, 9, 5.5), margin=0.10, extra=[xy(P(-1.2, 7.5)), xy(P(14.5, -1.0))], pad_aspect=True)
    z.north_arrow()
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
    save(fig, [z], 'H23_dai22mon_zu02_ittou_kankei')


def zu05():
    fig, axes = new_figure('敷地の確認（作図チェック用。辺長・面積は建物図面には書かない）',
                           '座標リストの座標から描いた5番2と10番1。道路の幅は239.25−233.25＝6.00。\n'
                           '10番1は座標の面積792.72㎡で登記記録792.95㎡とほぼ一致。5番2は352.90㎡で登記記録357.70㎡より約4.8㎡少ない（形は座標どおりに描く）',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    fit(ax, LOT52 + LOT101, margin=0.08, extra=[xy(Z(262.5, 150.0)), xy(Z(200.0, 200.0))], pad_aspect=True)
    z.north_arrow()
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
    save(fig, [z], 'H23_dai22mon_zu05_shikichi_kakunin')


def zu08():
    setup_font()
    fig = plt.figure(figsize=(16.5, 15), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面の完成形（答案用紙（その2）の欄・縮尺1/500で描く内容）', fontsize=22, weight='bold', y=0.985)
    # 答案用紙（その2）の建物図面の欄（家屋番号・建物の所在は用紙の上、申請人・縮尺は下）
    cell(fig, 0.06, 0.890, 0.20, 0.937, '家屋番号', fs=15)
    cell(fig, 0.20, 0.890, 0.46, 0.937, KAOKU, fs=16, color=INK)
    fig.text(0.70, 0.913, '建　物　図　面', ha='center', va='center', fontsize=20)
    cell(fig, 0.06, 0.843, 0.20, 0.890, '建物の所在', fs=15)
    cell(fig, 0.20, 0.843, 0.94, 0.890, SHOZAI, fs=16, ha='left', color=INK)
    cell(fig, 0.06, 0.120, 0.94, 0.843, lw=1.8)
    cell(fig, 0.06, 0.073, 0.20, 0.120, '申　請　人', fs=15)
    cell(fig, 0.20, 0.073, 0.74, 0.120, SHINSEININ, fs=16, color=INK)
    cell(fig, 0.74, 0.073, 0.83, 0.120, '縮尺', fs=15)
    cell(fig, 0.83, 0.073, 0.94, 0.120, '1/500', fs=15)
    fig.text(0.92, 0.133, '（単位：m）', ha='right', va='center', fontsize=13)
    fig.text(0.5, 0.033, '主である建物と符号1（実線）、符号1の属する一棟の建物の1階（点線）。距離は外壁まで（問題文の注5）、小数第1位。'
             '行政界（二丁目と五丁目の境）を一点鎖線で示す。\n建物の所在は2筆を書く（申請書の所在の欄は5番地2だけ）。'
             '申請人の欄は（略）と印刷されていないので氏名を書く', ha='center', va='center', fontsize=13, linespacing=1.6)
    ax = fig.add_axes([0.08, 0.15, 0.84, 0.68])
    z = Zu(ax, fontsize=13)
    fit(ax, LOT52 + LOT101, margin=0.10, extra=[xy(Z(262.5, 150.0)), xy(Z(199.0, 207.0))], pad_aspect=True)
    z.north_arrow()
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
    save(fig, [z], 'H23_dai22mon_zu08_tatemono_zumen')


# ---- 主である建物（原点＝1階の北西の角、東・南） ----
F1 = [P(0, 0), P(12.51, 0), P(12.51, 6.37), P(10.01, 6.37), P(10.01, 9.10), P(4.55, 9.10), P(4.55, 7.28), P(0, 7.28)]
R_OLD, R_MINAMI, R_ZOU = rect(0, 0, 10.01, 7.28), rect(4.55, 7.28, 10.01, 9.10), rect(10.01, 0, 12.51, 6.37)
F2 = rect(0.91, 0, 10.01, 7.28)
assert round(area(F1), 4) == 98.735 and trunc2(area(F1)) == 98.73
assert round(area(R_OLD), 4) == 72.8728 and round(area(R_MINAMI), 4) == 9.9372 and round(area(R_ZOU), 4) == 15.925
assert round(area(F2), 3) == 66.248 and trunc2(area(F2)) == 66.24


def zu09():
    fig, axes = new_figure('主である建物の求積図（1階は増築、2階は変わらない）',
                           '1階：10.01×7.28＝72.8728 ＋ 5.46×1.82＝9.9372 ＋ 2.50×6.37＝15.9250 ＝ 98.7350 → 98.73㎡（四捨五入の98.74ではない）\n'
                           '2階：9.10×7.28＝66.2480 → 66.24㎡（登記記録と同じ）。点線は1階の位置',
                           w=17, h=8.2, ncols=2, width_ratios=[1.2, 1])
    fig.subplots_adjust(top=0.84)
    z = Zu(axes[0], fontsize=13)
    fit(axes[0], F1, margin=0.16, pad_aspect=True)
    z.north_arrow()
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
    z2 = Zu(axes[1], fontsize=13)
    fit(axes[1], F1, margin=0.16, pad_aspect=True)
    z2.poly(F1, color=GRAY, lw=1.3, ls='--')
    z2.poly(F2, color=BLACK, lw=2.4, fill=BLUE)
    dims(z2, F2, ['9.10', '7.28', None, '7.28'], outward=False)
    z2.free_text(P(5.46, 3.0), '9.10×7.28\n＝66.2480', fs=14)
    axes[1].set_title('2階：66.24㎡（変更なし）', fontsize=18, weight='bold')
    save(fig, [z, z2], 'H23_dai22mon_zu09_omoya_kyuuseki')


# ---- 車庫（5番2の符号1）：原点＝北西の角（シャッターの中心と西の壁の中心の交点） ----
T = 0.12      # ブロック壁の厚さ（問題文の注3）
TD = 0.50     # 作図用に誇張した壁の厚さ（実寸の0.12では見えないので模式図にする）
DW = TD / 2
NG1_REAL, NG2_REAL, OK_REAL = rect(0, 0, 4.5, 5.5), rect(0.06, 0.06, 4.44, 5.44), rect(0.06, 0, 4.44, 5.44)
assert round(area(NG1_REAL), 2) == 24.75 and round(area(NG2_REAL), 4) == 23.5644 and round(area(OK_REAL), 4) == 23.8272
assert trunc2(area(NG2_REAL)) == 23.56 and trunc2(area(OK_REAL)) == 23.82


def garage_panel(ax, title, color, inner, label, note):
    z = Zu(ax, fontsize=13)
    fit(ax, rect(-0.6, -1.2, 5.1, 8.3), margin=0.06, pad_aspect=True)
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
    return z


def zu10():
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
    save(fig, zs, 'H23_dai22mon_zu10_shako_ayamari_hikaku')


def zu15():
    setup_font()
    fig = plt.figure(figsize=(18, 10), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図の完成形（答案用紙（その2）の欄・縮尺1/250で描く内容）', fontsize=22, weight='bold', y=0.975)
    fig.text(0.5, 0.905, '各　階　平　面　図', ha='center', va='center', fontsize=20)
    cell(fig, 0.04, 0.17, 0.96, 0.88, lw=1.8)
    cell(fig, 0.04, 0.10, 0.14, 0.17, '作　成　者', fs=15)
    cell(fig, 0.14, 0.10, 0.80, 0.17)
    fig.text(0.30, 0.135, '（略）', ha='center', va='center', fontsize=15)
    fig.text(0.78, 0.135, '（平成23年8月21日作成）', ha='right', va='center', fontsize=15)
    cell(fig, 0.80, 0.10, 0.87, 0.17, '縮尺', fs=15)
    cell(fig, 0.87, 0.10, 0.96, 0.17, '1/250', fs=15)
    fig.text(0.5, 0.045, '主である建物の1階・2階と、附属建物符号1を書き分ける（不動産登記規則第83条第1項）。2階には1階の位置を点線で重ねる。'
             '3つとも同じ縮尺1/250。\n符号1は区分建物なので内法の寸法（4.38・5.44）で描く。問2のなお書きどおり、求積と床面積の表示は書かない'
             '（作成者の欄は印刷済み）', ha='center', va='center', fontsize=14, linespacing=1.6)
    ax = fig.add_axes([0.05, 0.20, 0.90, 0.62])
    z = Zu(ax, fontsize=13)
    O2, O3 = 16.0, 31.5                       # 2階・符号1を東へずらして並べる（縮尺は同じ）
    Q = lambda pts, o: [p + complex(0, o) for p in pts]
    g = rect(0, 0, 4.38, 5.44)
    fit(ax, F1 + Q(F1, O2) + Q(g, O3), margin=0.06, extra=[xy(P(0, -2.6)), xy(P(37.0, 10.2))], pad_aspect=True)
    z.north_arrow()
    # 主である建物 1階
    z.poly(F1, color=BLACK, lw=2.2)
    dims(z, F1, ['12.51', '6.37', None, None, '5.46', '1.82', '4.55', '7.28'])
    z.free_text(P(11.26, 6.37), '2.50', fs=13, offsets=((6, -14), (10, -16), (0, -20)))
    z.edge_label(P(10.01, 6.37), P(10.01, 9.10), '2.73', centroid(F1), fs=13, ts=(0.72, 0.8, 0.62))
    z.free_text(P(6.25, -1.9), '主である建物　1階', fs=16, weight='bold')
    # 主である建物 2階（1階の位置を点線）
    z.poly(Q(F1, O2), color=BLACK, lw=1.2, ls='--')
    f2 = Q(F2, O2)
    z.poly(f2, color=BLACK, lw=2.2)
    dims(z, f2, ['9.10', '7.28', '9.10', '7.28'], outward=False)
    z.free_text(P(O2 + 6.25, -1.9), '主である建物　2階', fs=16, weight='bold')
    # 附属建物 符号1（内法）
    gg = Q(g, O3)
    z.poly(gg, color=BLACK, lw=2.2)
    dims(z, gg, ['4.38', '5.44', '4.38', '5.44'])
    z.free_text(P(O3 + 2.19, -1.9), '附属建物　符号1', fs=16, weight='bold')
    save(fig, [z], 'H23_dai22mon_zu15_kakai_heimenzu')


def zu17():
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
    path = os.path.join(OUT, 'H23_dai22mon_zu17_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図17: 解く順番（固定配置）\n  →', path)


# =====================================================================================
# 2026-10-05追加：記事本文に対して足りなかった図（藍子の誤答と訂正、最大のわなの理由、条文の当てはめ、本文の確認の数値）
# =====================================================================================
def board(title, caption, h=9.5):
    """固定配置の説明図（箱と矢印）の下地。座標は 0〜100。重なり検査の対象外なので目視で確かめる。"""
    setup_font()
    fig = plt.figure(figsize=(16, h), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=23, weight='bold', y=0.965)
    ax = fig.add_axes([0.02, 0.15, 0.96, 0.75])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.text(0.5, 0.07, caption, ha='center', va='center', fontsize=15, linespacing=1.6)
    return fig, ax


def box(ax, x0, y0, x1, y1, col, alpha=0.10, lw=2.0, ls='-'):
    ax.add_patch(plt.Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=col, alpha=alpha, edgecolor='none'))
    ax.add_patch(plt.Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, edgecolor=col, lw=lw, ls=ls))


def arrow(ax, p, q, col=BLACK, lw=2.2):
    ax.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle='-|>', lw=lw, color=col, mutation_scale=22))


def btext(ax, x, y, t, fs=14, col=BLACK, ha='center', weight='normal'):
    ax.text(x, y, t, ha=ha, va='center', fontsize=fs, color=col, weight=weight, linespacing=1.45)


def board_save(fig, name, label):
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print(f'[重なり検査] {label}（固定配置）\n  →', path)


# ---- 図1：車庫の「増築」はどの登記になるか（第1章、藍子の誤答の訂正） ----
def zu01():
    fig, ax = board('車庫の「増築」はどの登記になる？　3つの問いで決める',
                    '問題文の注9（利用上・構造上の独立性）と調査の結果2（費用を出したのは畑山邦彦）で、既存の車庫の一部（増築）ではなく区分建物になる。\n'
                    '居宅の車庫として使うので5番2の附属建物。申請は5番2の建物表題部変更登記1本（10番1の表題部の変更の登記も要るが本問では問われていない）',
                    h=10.5)
    box(ax, 1, 82, 27, 97, GRAY)
    btext(ax, 14, 89.5, '10番1の符号1（既存の車庫）に\n接続して「増築」した車庫', fs=14.5)
    # 問1
    box(ax, 33, 82, 66, 97, BLUE)
    btext(ax, 49.5, 89.5, '問い1　既存の車庫と構造上・利用上の\n独立性があるか（問題文の注9）', fs=14.5, col=BLUE)
    arrow(ax, (27, 89.5), (33, 89.5))
    box(ax, 72, 82, 99, 97, RED, alpha=0.07, ls='--')
    btext(ax, 85.5, 89.5, 'ない → 既存の車庫の一部（増築）\n10番1の床面積が増えるだけ', fs=13.5, col=RED)
    arrow(ax, (66, 89.5), (72, 89.5), col=RED)
    btext(ax, 85.5, 78.5, '藍子の誤答の筋（本問は当たらない）', fs=12.5, col=RED)
    # 問2
    arrow(ax, (49.5, 82), (49.5, 71))
    btext(ax, 53, 76.5, 'ある', fs=14, col=BLUE, ha='left', weight='bold')
    box(ax, 33, 56, 66, 71, BLUE)
    btext(ax, 49.5, 63.5, '問い2　所有者は同じか\n（増築：畑山邦彦　既存：海野商事・海野洋子）', fs=14, col=BLUE)
    box(ax, 72, 56, 99, 71, GRAY, alpha=0.07, ls='--')
    btext(ax, 85.5, 63.5, '同じなら、所有者の意思で\n一棟全部を1個の建物にできる\n（準則第78条第2項ただし書）', fs=13, col=GRAY)
    arrow(ax, (66, 63.5), (72, 63.5), col=GRAY)
    # 区分建物
    arrow(ax, (49.5, 56), (49.5, 46))
    btext(ax, 53, 51, '違う', fs=14, col=BLUE, ha='left', weight='bold')
    box(ax, 30, 33, 69, 46, ORANGE, alpha=0.16)
    btext(ax, 49.5, 39.5, '区分建物（建物の区分所有等に関する法律第1条、\n不動産登記事務取扱手続準則第78条第2項）＝「区分建物の新築」', fs=14)
    # 問3
    arrow(ax, (49.5, 33), (49.5, 25))
    box(ax, 30, 12, 69, 25, BLUE)
    btext(ax, 49.5, 18.5, '問い3　5番2の居宅と効用上一体か\n（畑山邦彦が自分の車をしまう車庫）', fs=14, col=BLUE)
    arrow(ax, (69, 18.5), (74, 18.5), col=GREEN)
    box(ax, 74, 4, 99, 33, GREEN, alpha=0.12)
    btext(ax, 86.5, 18.5, '5番2の符号1の附属建物\n（不動産登記法第2条第23号、\n準則第78条第1項）\n\n建物表題部変更登記\n（主である建物の増築＋\n附属建物の新築）', fs=13.5, col=GREEN, weight='bold')
    box(ax, 1, 4, 25, 30, GRAY, alpha=0.05, ls=':')
    btext(ax, 13, 17, '道路の向こう・別の丁目に\nあることは、附属建物に\nなれない理由にならない\n（問3で使う）', fs=13, col=GRAY)
    board_save(fig, 'H23_dai22mon_zu01_hantei_nagare', '図1: 判定の流れ')


# ---- 図3：建物ごとの時系列メモ（第1章） ----
def zu03():
    fig, ax = board('時系列メモ　どの日付が申請書のどこに入るか',
                    '工事の完了（8月2日）と持分の取得（8月4日）は別の日。主である建物の増築と附属建物の新築は8月2日、敷地権は8月4日。\n'
                    '下の枠が申請書に書く原因。申請は8月2日から1月以内（不動産登記法第51条第1項）。申請日（8月21日）は答案用紙に印刷済みで、原因の日付には使わない',
                    h=9.0)
    ax.plot([4, 96], [60, 60], color=BLACK, lw=2.4)
    pts = [(12, '8月2日', '工事が完了\n（調査の結果3）', '5番2の増築\n車庫の完成', '主：③平成23年8月2日増築\n符号1：平成23年8月2日新築', BLUE),
           (37, '8月4日', '海野洋子から\n持分の一部を取得\n（調査の結果4）', '10番1の持分\n6分の2', '符号1：平成23年8月4日敷地権', RED),
           (62, '8月12日', '登記記録を確認', '10番1の甲区に\n「持分6分の2　畑山邦彦」', '持分は登記されている\n（敷地権になれる）', GRAY),
           (87, '8月21日', '申請\n（答案用紙に印刷）', 'A地方法務局', '原因の日付には\n使わない', GRAY)]
    for x, d, ev, what, row, col in pts:
        ax.plot([x], [60], 'o', ms=14, color=col)
        btext(ax, x, 68, d, fs=18, col=col, weight='bold')
        btext(ax, x, 83, ev, fs=14)
        btext(ax, x, 48, what, fs=13.5)
        box(ax, x - 11.5, 18, x + 11.5, 36, col, alpha=0.10)
        btext(ax, x, 27, row, fs=13.5, col=col, weight='bold')
    board_save(fig, 'H23_dai22mon_zu03_jikeiretsu', '図3: 時系列メモ')


# ---- 図4：注の仕分け（第1章） ----
def zu04():
    fig, ax = board('注の仕分け　本問の注は3系統（番号が付くのは問題文の注だけ）',
                    '問題文の注3の「10番1の主である建物15cm」は求積に使わない。〔見取図〕の（注）と〔車庫の詳細図〕の（注）には番号がないので、\n'
                    '記事では「問題文の注4」「〔コンクリートブロック造の車庫の詳細図〕の（注）」のように、どの注かを書き分ける',
                    h=10.5)
    box(ax, 1, 2, 62, 97, BLUE, alpha=0.06)
    btext(ax, 31.5, 93, '問題文の注1〜10（どこで使うか）', fs=16, col=BLUE, weight='bold')
    rows = ['注1　壁・柱の中心線で測定 → 主である建物は壁心',
            '注2　既存の建物は図面と相違なし、単位はm',
            '注3　壁の厚さ（5番2は12cm、10番1の符号1は12cm）、\n　　　シャッターの厚さは考えない → 内法の0.06',
            '注4　車庫の南北はブロック壁とシャッター扉の中心で測定\n　　　→ 北（シャッター）からは引かない',
            '注5　敷地境界までの距離は外壁から → 建物図面の4.5',
            '注6　角はすべて直角　　注7　天井は2.5m以上（不算入なし）',
            '注8　増築部分の屋根はかわら → 構造変更なし',
            '注9　車庫は利用上・構造上の独立性あり → 区分建物',
            '注10　敷地は座標成果あり → 敷地を座標で描く']
    y_top = 87
    for r in rows:
        h = 6.6 * (r.count('\n') + 1)
        btext(ax, 3, y_top - h / 2, r, fs=13, ha='left')
        y_top -= h + 1.0
    assert y_top > 2
    box(ax, 66, 56, 99, 97, GREEN, alpha=0.08)
    btext(ax, 82.5, 92, '〔見取図〕の（注）', fs=16, col=GREEN, weight='bold')
    btext(ax, 82.5, 76, '点線で表記した箇所が\n設問中の増築した部分\n→ 5番2の東の2.50×6.37と、\n既存の車庫の西の車庫', fs=13.5)
    box(ax, 66, 2, 99, 51, ORANGE, alpha=0.10)
    btext(ax, 82.5, 46, '〔コンクリートブロック造の\n車庫の詳細図〕の（注）', fs=15.5, col=ORANGE, weight='bold')
    btext(ax, 82.5, 24, '数値はブロック壁及び\nシャッター扉の中心を\n測定した値\n→ 4.50・5.50は中心の寸法。\n区分建物は内法に直す', fs=13.5)
    board_save(fig, 'H23_dai22mon_zu04_chuu_shiwake', '図4: 注の仕分け')


# ---- 図6：東の距離は 7.0 − 2.5 ＝ 4.5（第2章、藍子の誤答） ----
def zu06():
    fig, axes = new_figure('東の距離は7.0のまま写さない：増築で 7.0 − 2.5 ＝ 4.5',
                           '〔5番2の建物図面（抜粋）〕の7.0は増築前の東の外壁から。増築部分（幅2.50、北の壁にそろえて長さ6.37）の壁も12cmなので、\n'
                           '外壁の面も2.50東へ出る。距離は外壁から（問題文の注5）。北の1.0は北西の角と増築部分の北東の角の2か所',
                           w=17, h=9, ncols=2)
    fig.subplots_adjust(top=0.84, wspace=0.06)
    old = [Z(WN, WW), Z(WN, WE_OLD), Z(WN - 9.10, WE_OLD), Z(WN - 9.10, WW + 4.55), Z(WN - 7.28, WW + 4.55), Z(WN - 7.28, WW)]
    win = [Z(255.6, 166.5), Z(255.6, 189.5), Z(241.5, 189.5), Z(241.5, 166.5)]
    zs = []
    for k, ax in enumerate(axes):
        z = Zu(ax, fontsize=13)
        fit(ax, win, margin=0.02, pad_aspect=True)
        z.line(E + 0.0j + complex(0, 2.7), A, color=BLACK, lw=1.8)
        z.line(A, B, color=BLACK, lw=1.8)
        z.free_text(Z(254.9, 172.5), '北の筆界（6との境）', fs=12, color=GRAY)
        z.free_text(Z(247.0, 188.5), '東の\n筆界\n（道路）', fs=12, color=GRAY)
        if k == 0:
            z.poly(old, color=BLACK, lw=2.2)
            e_out = WE_OLD + 0.06
            lab, ttl, col = '7.0', '増築前：〔5番2の建物図面（抜粋）〕の値', BLACK
        else:
            z.poly(old, color=GRAY, lw=1.2, ls='--')
            z.poly(zrect(WN - 6.37, WE_OLD, WN, WE_NEW), color=RED, lw=0, fill=RED, alpha=0.25, check=False)
            z.poly(OMOYA, color=BLACK, lw=2.2)
            e_out = WE_NEW + 0.06
            lab, ttl, col = '4.5', '増築後（建物図面に書く値）', GREEN
            z.free_text(Z(WN - 3.2, (WE_OLD + WE_NEW) / 2), '増築\n2.50\n×\n6.37', fs=12, color=RED)
        y = WN - 1.5
        p, q = Z(y, 187.17), Z(y, e_out)
        ax.annotate('', xy=xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='-|>', lw=1.4, color=col, mutation_scale=12))
        z.segments.append((xy(p), xy(q)))
        z.free_text(Z(y, (187.17 + e_out) / 2), lab, fs=16, color=col, weight='bold', offsets=((0, -14), (0, 14)))
        for yy in (WW - 0.06, (WE_OLD if k == 0 else WE_NEW) + 0.06):
            p, q = Z(254.43, yy), Z(WN + 0.06, yy)
            ax.annotate('', xy=xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='-|>', lw=1.1, color=BLACK, mutation_scale=10))
            z.segments.append((xy(p), xy(q)))
            z.free_text(Z(253.9, yy), '1.0', fs=12, offsets=((-14, 0), (14, 0)))
        z.free_text(Z(WN - 4.5, WW + 4.5), '主', fs=15, weight='bold')
        ax.set_title(ttl, fontsize=17, weight='bold', color=col)
        if k == 1:
            z.north_arrow()
        zs.append(z)
    save(fig, zs, 'H23_dai22mon_zu06_higashi_kyori')


# ---- 図7：建物が自分の筆の中に収まるかの確認（第2章、本文の確認の数値） ----
GS_OUT, GW_OUT, GE_OUT = GS - 0.06, GW - 0.06, GE + 0.06
Y_FG_S = F.imag - (F.real - GS_OUT) * (F.imag - G.imag) / (F.real - G.real)
X_HG = lambda y: H.real + (y - H.imag) * (G.real - H.real) / (G.imag - H.imag)
assert round(WW - 0.06 - E.imag, 2) == 6.25 and round(WN - 9.10 - 0.06 - D.real, 2) == 4.96
assert round(GW_OUT - J.imag, 1) == 20.7 and round(Y_FG_S - GE_OUT, 1) == 4.2 and round(GS_OUT - X_HG(GE_OUT), 1) == 18.7


def zu07():
    fig, axes = new_figure('建物は自分の筆の中に収まるか：座標と外壁までの距離で確かめる',
                           '左：5番2の主である建物（北1.0・東4.5は建物図面に書く距離、西約6.3・南約5.0は確認のための計算値）。\n'
                           '右：一棟の車庫（北1.0・東5.0は北東の角から。東の筆界FGが斜めなので南東の角では約4.2。西約20.7・南約18.7）。どちらも1筆の中',
                           w=18, h=9.5, ncols=2, width_ratios=[1, 1.25])
    fig.subplots_adjust(top=0.85, wspace=0.05)
    # 左：5番2
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    fit(ax, LOT52, margin=0.10, pad_aspect=True)
    z.poly(LOT52, color=BLACK, lw=1.8, fill=BLUE, alpha=0.06)
    z.poly(OMOYA, color=BLACK, lw=2.2)
    segs = [(Z(254.43, 172.0), Z(WN + 0.06, 172.0), '1.0', BLACK), (Z(WN - 1.5, 187.17), Z(WN - 1.5, WE_NEW + 0.06), '4.5', BLACK),
            (Z(WN - 3.5, E.imag), Z(WN - 3.5, WW - 0.06), '約6.3', BLUE),
            (Z(D.real, 177.4), Z(WN - 9.10 - 0.06, 177.4), '約5.0', BLUE)]
    for p, q, t, col in segs:
        ax.annotate('', xy=xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='<|-|>', lw=1.2, color=col, mutation_scale=10))
        z.segments.append((xy(p), xy(q)))
        vert = abs((p - q).imag) < 1e-6      # 南北の矢印なら文字を東西にずらす
        offs = ((26, 0), (-28, 0)) if vert else ((0, 12), (0, -12))
        z.free_text((p + q) / 2, t, fs=13, color=col, weight='bold', offsets=offs)
    z.free_text(centroid(OMOYA), '主', fs=15, weight='bold')
    z.free_text(Z(241.6, 167.0), '5番2', fs=13, color=GRAY)
    ax.set_title('5番2（二丁目）', fontsize=17, weight='bold')
    z.north_arrow()
    # 右：10番1
    ax = axes[1]
    z2 = Zu(ax, fontsize=13)
    fit(ax, LOT101, margin=0.06, pad_aspect=True)
    z2.poly(LOT101, color=BLACK, lw=1.8, fill=GREEN, alpha=0.06)
    z2.poly(KIZON, color=BLACK, lw=1.6, ls='--')
    z2.poly(zrect(GS, GW, GN, GMID), color=BLACK, lw=2.2)
    segs = [(Z(233.25, GMID + 2.0), Z(GN, GMID + 2.0), '1.0', BLACK),
            (Z(GN - 0.3, Y_FG - 0.04), Z(GN - 0.3, GE_OUT), '5.0', BLACK),
            (Z(GS_OUT + 0.3, Y_FG_S - 0.04), Z(GS_OUT + 0.3, GE_OUT), '約4.2', BLUE),
            (Z(GS + 2.5, J.imag), Z(GS + 2.5, GW_OUT), '約20.7', BLUE),
            (Z(X_HG(GE_OUT), GE_OUT - 1.0), Z(GS_OUT, GE_OUT - 1.0), '約18.7', BLUE)]
    for p, q, t, col in segs:
        ax.annotate('', xy=xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='<|-|>', lw=1.2, color=col, mutation_scale=10))
        z2.segments.append((xy(p), xy(q)))
        vert = abs((p - q).imag) < 1e-6
        offs = ((-22, 0), (24, 0), (-30, 0)) if vert else ((0, 12), (0, -12))
        if t == '1.0':                   # 1.0mは短く、北の筆界と北の壁の間に文字が入らないので引き出し線で外へ出す
            z2.callout((p + q) / 2, t, dirs=(160, 145, 175), dists=(40, 55, 70), fs=13, color=col)
            continue
        z2.free_text((p + q) / 2, t, fs=13, color=col, weight='bold', offsets=offs)
    z2.callout(centroid(zrect(GS, GW, GN, GMID)), '符号1（実線）\n点線は既存の車庫', dirs=(-120, -140, -100), fs=12)
    for p, n in [(F, 'F'), (G, 'G')]:
        z2.point(p, 'dot', size=6)
        z2.point_label(p, n, away=centroid(LOT101), fs=13)
    z2.free_text(Z(215.0, 168.0), '10番1', fs=13, color=GRAY)
    ax.set_title('10番1（五丁目）', fontsize=17, weight='bold')
    save(fig, [z, z2], 'H23_dai22mon_zu07_shozai_kakunin')


# ---- 図11：内法と壁心が1つの申請書に混ざる（第3章） ----
def zu11():
    fig, ax = board('1つの申請書に壁心と内法が混ざる　決め手は「その建物自体が区分建物か」',
                    '床面積は、普通の建物は壁その他の区画の中心線、区分建物は内側線で囲まれた部分で測る（不動産登記規則第115条）。\n'
                    '附属建物だから・主である建物が普通の建物だから、では決まらない。一棟の建物の床面積は壁心（不動産登記法第44条第1項第7号）',
                    h=9.5)
    cols = [(1, 33, '主である建物（居宅）', '普通の建物 → 壁心', '1階　98.73㎡\n2階　66.24㎡', BLUE),
            (35, 66, '一棟の建物（車庫の全体）', '区分建物そのものではない → 壁心', '9.00×5.50＝49.50㎡\n（構造の欄に書く）', GRAY),
            (68, 99, '符号1の専有部分（畑山邦彦）', '区分建物 → 内法', '4.38×5.44＝23.82㎡\n（床面積の欄に書く）', RED)]
    for x0, x1, t, rule, val, col in cols:
        box(ax, x0, 4, x1, 97, col, alpha=0.06)
        btext(ax, (x0 + x1) / 2, 91, t, fs=15.5, col=col, weight='bold')
        btext(ax, (x0 + x1) / 2, 83, rule, fs=14.5, weight='bold')
        btext(ax, (x0 + x1) / 2, 15, val, fs=15, col=col, weight='bold')
    # 模式図：主である建物（壁心の線）
    xs = [5, 29, 29, 24.2, 24.2, 13.7, 13.7, 5, 5]
    ys = [74, 74, 61.8, 61.8, 56.6, 56.6, 60.2, 60.2, 74]
    ax.plot(xs, ys, color=BLUE, lw=2.4)
    btext(ax, 17, 47, '壁の中心線で囲む\n（増築部分を含む1階・形は模式）', fs=13, col=BLUE)
    # 一棟：外形（壁心）
    ax.add_patch(plt.Rectangle((40, 55), 21, 18, fill=False, ec=GRAY, lw=2.4))
    ax.plot([50.5, 50.5], [55, 73], color=GRAY, lw=1.6)
    btext(ax, 50.5, 47, '西の部分＋東の部分\nの壁の中心線', fs=13, col=GRAY)
    # 専有部分：内法
    ax.add_patch(plt.Rectangle((72, 55), 22, 18, fill=False, ec=GRAY, lw=1.0, ls=':'))
    ax.add_patch(plt.Rectangle((73.3, 56.3), 19.4, 16.7, fill=True, fc=RED, alpha=0.12, ec=RED, lw=2.4))
    btext(ax, 83, 47, '内側線で囲む\n（北はシャッターの中心のまま）', fs=13, col=RED)
    board_save(fig, 'H23_dai22mon_zu11_uchinori_kabeshin', '図11: 内法と壁心')


# ---- 図12：一棟の建物の所在は登記記録のどこに載るか（第4章、所在の欄の誤答の理由） ----
def zu12():
    fig, ax = board('申請書の所在は5番地2だけ　一棟の建物の所在は附属建物の「構造」の欄',
                    '区分建物である附属建物は、その附属建物が属する一棟の建物の所在を登記する（不動産登記法第44条第1項第5号かっこ書き）。\n'
                    '登記記録では、附属建物の表示欄の構造の欄に一棟の建物の所在・構造・床面積と敷地権の内容を記録する（不動産登記規則別表二）',
                    h=10.5)
    box(ax, 1, 3, 64, 97, BLUE, alpha=0.05)
    btext(ax, 32.5, 92.5, '家屋番号5番2の登記記録（表題部）の形', fs=16, col=BLUE, weight='bold')
    box(ax, 3, 66, 62, 87, BLACK, alpha=0.03, lw=1.4)
    btext(ax, 5, 82, '主である建物の表示', fs=14, ha='left', weight='bold')
    box(ax, 5, 70, 60, 78, RED, alpha=0.10)
    btext(ax, 6.5, 74, '所在　A市B町二丁目5番地2　　（ここは変わらない）', fs=14, ha='left', col=RED, weight='bold')
    box(ax, 3, 8, 62, 63, BLACK, alpha=0.03, lw=1.4)
    btext(ax, 5, 58, '附属建物の表示　符号1　種類　車庫', fs=14, ha='left', weight='bold')
    box(ax, 5, 22, 60, 53, ORANGE, alpha=0.12)
    btext(ax, 6.5, 48, '構造の欄', fs=13.5, ha='left', col=ORANGE, weight='bold')
    btext(ax, 6.5, 41, '一棟の建物：A市B町五丁目10番地1\n　コンクリートブロック造陸屋根平家建　床面積49.50㎡', fs=13.5, ha='left')
    btext(ax, 6.5, 32, '専有部分：コンクリートブロック造陸屋根平家建', fs=13.5, ha='left')
    btext(ax, 6.5, 26, '敷地権の内容：10番1の土地の所有権6分の2', fs=13.5, ha='left')
    btext(ax, 6.5, 14, '床面積　23.82㎡（内法）　原因　8月2日新築・8月4日敷地権', fs=13.5, ha='left')
    box(ax, 68, 55, 99, 97, RED, alpha=0.06)
    btext(ax, 83.5, 92, '申請書の所在の欄', fs=16, col=RED, weight='bold')
    btext(ax, 83.5, 75, '1段目：A市B町二丁目5番地2\n2段目・原因：空欄\n\n10番地1を足さない\n（所在の変更は起きていない）', fs=14)
    arrow(ax, (68, 74), (60.5, 74), col=RED)
    box(ax, 68, 3, 99, 49, GREEN, alpha=0.08)
    btext(ax, 83.5, 44, '建物図面の「建物の所在」', fs=16, col=GREEN, weight='bold')
    btext(ax, 83.5, 24, 'A市B町二丁目5番地2、\nA市B町五丁目10番地1\n\n建物が実際に乗っている\n土地を示す図なので2筆', fs=14)
    board_save(fig, 'H23_dai22mon_zu12_touki_kiroku', '図12: 所在の載る欄')


# ---- 図13：敷地権が生じるまで（第4章、条文の流れと日付） ----
def zu13():
    fig, ax = board('畑山邦彦の車庫の敷地権　条文の順にたどると日付は8月4日',
                    '8月2日の時点では、土地所有者の了承を得て建てただけで、登記された土地の権利がない（敷地権なし）。\n'
                    '8月4日に持分を取得して登記されたので、その日に敷地権が生じる。割合は登記記録の持分のまま6分の2（約分しない）',
                    h=10.5)
    steps = [('10番1は「建物の敷地」', '一棟の建物が所在する土地\n（区分所有法第2条第5項）', GRAY),
             ('敷地利用権', '専有部分を所有するための土地の権利\n＝10番1の所有権の共有持分6分の2\n（同条第6項）', BLUE),
             ('分離して処分できない', '数人で有する所有権なので\n第22条第1項本文（規約の別段の定めなし）\n※1人で持つ場合は同条第3項', ORANGE),
             ('敷地権', '登記された敷地利用権で\n分離して処分できないもの\n（不動産登記法第44条第1項第9号）', RED)]
    w, gap = 22.5, 2.3
    for i, (t, d, col) in enumerate(steps):
        x0 = 1 + i * (w + gap)
        box(ax, x0, 58, x0 + w, 97, col, alpha=0.10)
        btext(ax, x0 + w / 2, 89, t, fs=15.5, col=col, weight='bold')
        btext(ax, x0 + w / 2, 71, d, fs=12.5)
        if i < 3:
            arrow(ax, (x0 + w + 0.2, 77), (x0 + w + gap - 0.2, 77))
    ax.plot([6, 94], [36, 36], color=BLACK, lw=2.2)
    for x, d, t, col in [(18, '8月2日', '車庫が完成\n土地は「了承」だけ → 敷地権なし', GRAY),
                         (50, '8月4日', '海野洋子から持分を取得\n→ 敷地権が生じる', RED),
                         (82, '8月12日', '登記記録に\n「持分6分の2　畑山邦彦」', BLUE)]:
        ax.plot([x], [36], 'o', ms=13, color=col)
        btext(ax, x, 44, d, fs=16, col=col, weight='bold')
        btext(ax, x, 24, t, fs=13.5)
    box(ax, 18, 1, 82, 13, RED, alpha=0.08)
    btext(ax, 50, 7, '原因：平成23年8月2日新築　平成23年8月4日敷地権　／　敷地権の表示：所有権6分の2', fs=14.5, col=RED, weight='bold')
    board_save(fig, 'H23_dai22mon_zu13_shikichiken', '図13: 敷地権')


# ---- 図14：添付書類と登録免許税（第4章、条文の当てはめ） ----
def zu14():
    fig, ax = board('添付書類は4つ　入れるもの・入れないものを根拠で分ける',
                    '答案用紙の欄の名前は「添付書類」なので「〜書」で書く。登録免許税は答案用紙に欄がない（表題部変更登記は非課税）。\n'
                    '附属建物が区分建物でも、建物の区分の登記をしたわけではないので1,000円は書かない',
                    h=10.5)
    cols = [(1, 26, '書類'), (26, 76, '根拠・理由'), (76, 99, '本問')]
    rows = [('建物図面・各階平面図', '床面積の変更（不動産登記令別表14の項添付情報欄ロ（1））\n附属建物の新築（同欄ハ）', '入れる', GREEN),
            ('所有権証明書', '増築部分（同欄ロ（2））と\n附属建物（同欄ハ）が畑山邦彦の所有であること', '入れる', GREEN),
            ('代理権限証書', '代理人による申請（同令第7条第1項第2号）', '入れる', GREEN),
            ('登記識別情報', '表示に関する登記では提供しない', '入れない', GRAY),
            ('住所証明書', '表題部所有者を新しく登記する表題登記のもの', '入れない', GRAY),
            ('規約証明書', '規約敷地でも、規約で割合を定めたのでもない', '入れない', GRAY),
            ('登録免許税', '課税は分筆・合筆、建物の分割・区分・合併など\n（登録免許税法別表第一の一（十三））', '書かない', GRAY)]
    top, rh = 97, 12.4
    for x0, x1, t in cols:
        box(ax, x0, top - 8, x1, top, BLACK, alpha=0.06, lw=1.4)
        btext(ax, (x0 + x1) / 2, top - 4, t, fs=14.5, weight='bold')
    for j, (a, b, c, col) in enumerate(rows):
        y1 = top - 8 - j * rh
        y0 = y1 - rh
        for x0, x1, _ in cols:
            ax.add_patch(plt.Rectangle((x0, y0), x1 - x0, rh, fill=False, edgecolor=BLACK, lw=1.2))
        btext(ax, 13.5, (y0 + y1) / 2, a, fs=14, weight='bold')
        btext(ax, 51, (y0 + y1) / 2, b, fs=13)
        btext(ax, 87.5, (y0 + y1) / 2, c, fs=15, col=col, weight='bold')
    board_save(fig, 'H23_dai22mon_zu14_tenpu_shorui', '図14: 添付書類')


# ---- 図16：附属建物と認められるか（第5章、問3の藍子の誤答） ----
def zu16():
    fig, ax = board('附属建物と認められるかは場所ではなく使い方で決まる（問3）',
                    '附属建物は主である建物と一体のものとして1個の建物として登記される建物（不動産登記法第2条第23号）。数棟の建物を1個の建物として\n'
                    '扱うのは効用上一体として利用される状態にある場合（準則第78条第1項）。認められない場合は、車庫を独立した1個の建物（区分建物）として表題登記する',
                    h=10)
    box(ax, 1, 70, 99, 97, RED, alpha=0.06, ls='--')
    btext(ax, 50, 88, '藍子の誤答：「道路の向こうの別の町にあるときは、附属建物にできない」', fs=16, col=RED, weight='bold')
    btext(ax, 50, 77, '本問の車庫は、道路をはさみ、二丁目と五丁目で町も違うのに5番2の附属建物になっている → 場所の離れは決め手ではない', fs=14)
    cases = [('本問（調査の結果2）', '畑山邦彦が自分の車をしまう\n＝居宅の効用を補う', '附属建物と\n認められる', GREEN),
             ('具体例1', '畑山邦彦が第三者に貸し、\nその人の自動車の車庫になっている', '認められない', RED),
             ('具体例2', '居宅の住人のためではなく、\n10番1の事務所の来客用の車庫', '認められない', RED)]
    for i, (t, d, r, col) in enumerate(cases):
        x0 = 1 + i * 33
        box(ax, x0, 4, x0 + 31, 63, col, alpha=0.08)
        btext(ax, x0 + 15.5, 56, t, fs=15.5, col=col, weight='bold')
        btext(ax, x0 + 15.5, 38, d, fs=14)
        btext(ax, x0 + 15.5, 15, r, fs=17, col=col, weight='bold')
    board_save(fig, 'H23_dai22mon_zu16_fuzoku_hantei', '図16: 附属建物の判定')


if __name__ == '__main__':
    for f in (zu01, zu02, zu03, zu04, zu05, zu06, zu07, zu08, zu09, zu10, zu11, zu12, zu13, zu14, zu15, zu16, zu17):
        f()
    print('重なり合計:', len(PROBLEMS))
