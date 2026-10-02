"""平成29年度 第22問（建物）の解説図8枚を、見取図の距離・調査図素図の寸法から作図してPNGに書き出す。

`../prompt_H29_dai22mon_kaisetsuzu.md` の図1〜図8どおり。作図の共通部品は `tools/zu_helpers.py`。
敷地は座標値一覧表がないので、1番1と1番2を合わせた区画（東西40.00・南北40.00）の南西の角を原点にした
(X＝北, Y＝東) で持つ（S(東, 北) で作る）。隅切りは「底辺（斜めの辺）2メートルの直角二等辺三角形」（〔見取図〕の（注）6）
なので、直角をはさむ辺は √2。建物の平面は (東, 南)（原点＝建物を囲む長方形の北西の角）で持ち、P() で (北, 東) に変換する。
建物図面の建物の位置は、筆界から外壁までの距離（〔見取図〕の（注）3・〔調査図素図〕の（注）3）で置く。壁・板の厚さの
注記がないので、外壁と柱・板の中心のずれは考えない（縮尺500分の1では図上に現れない）。
図3（建物図面）と図7（各階平面図）の完成形は、試験の答案用紙（`public/kijutsu/H29-tatemono/a2.webp`）の第3欄の欄
（家屋番号・建物の所在・申請人〈略〉・作成者〈略〉〈平成29年○月○日作成〉・縮尺）の形の枠の中に描く（2026-10-02）。
実行: python3 note-articles-Kijyutsu/H29/Q22/zu/draw_H29_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Arc, Rectangle  # noqa: E402

from zu_helpers import Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN, PURPLE  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []
INK = '#1a3a8f'   # 答案用紙への記入（濃い青）
S2 = math.sqrt(2)          # 隅切りの直角をはさむ辺（2 ÷ √2）


def S(e, n):
    """敷地の (東, 北) を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(n, e)


def P(e, s):
    """建物の平面の (東, 南)（原点＝建物を囲む長方形の北西の角）を (北 + 東i) にする。"""
    return complex(-s, e)


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


def rect(e0, s0, e1, s1, f=P):
    return [f(e0, s0), f(e1, s0), f(e1, s1), f(e0, s1)]


# ---- 敷地（〔見取図〕）：1番1は区画から南西の1番2（12.00×15.00）を除いた形、隅切りは北西・北東・南東。1番2は南西に隅切り ----
LOT1 = [S(0, 15), S(0, 40 - S2), S(S2, 40), S(40 - S2, 40), S(40, 40 - S2), S(40, S2), S(40 - S2, 0), S(12, 0), S(12, 15)]
LOT2 = [S(0, S2), S(0, 15), S(12, 15), S(12, 0), S(S2, 0)]
assert round(area(LOT1), 2) == 1417.00 and round(area(LOT2), 2) == 179.00    # 登記記録の地積と一致

# ---- 建物（調査図素図の寸法。甲建物は軽量鉄骨の柱の中心、丙建物は発泡ポリスチレン板の中心） ----
KOU = [(0, 1.82), (3.64, 1.82), (3.64, 0), (18.18, 0), (18.18, 10.92), (3.64, 10.92), (3.64, 9.10), (0, 9.10)]
HEI = [(0, 0), (8, 0), (8, 7.5), (0, 7.5)]
HEI_WRONG = [(0, 0.3), (8, 0.3), (8, 7.2), (0, 7.2)]
OTSU = [(0, 0), (7.28, 0), (7.28, 10.92), (0, 10.92)]
assert round(area([P(*v) for v in KOU]), 4) == 185.2760
assert round(area([P(*v) for v in HEI]), 2) == 60.00 and round(area([P(*v) for v in HEI_WRONG]), 2) == 55.20
assert round(area([P(*v) for v in OTSU]), 4) == 79.4976

# ---- 建物の位置（筆界から外壁まで）：甲建物は北2.00（東の部分）・西3.00（西の張り出し）、丙建物は北3.00・東4.00、乙建物は西2.00・南2.00 ----
K_W, K_N = 3.00, 40 - 2.00                 # 甲建物を囲む長方形の北西の角（西の張り出しの西の壁の線・東の部分の北の壁の線）
H_W, H_N = 40 - 4.00 - 8.00, 40 - 3.00     # 丙建物の北西の角
O_W, O_N = 2.00, 2.00 + 10.92              # 乙建物の北西の角


def K_(e, s):
    return S(K_W + e, K_N - s)


def H_(e, s):
    return S(H_W + e, H_N - s)


def O_(e, s):
    return S(O_W + e, O_N - s)


KOU_SITE = [K_(*v) for v in KOU]
HEI_SITE = [H_(*v) for v in HEI]
OTSU_SITE = [O_(*v) for v in OTSU]
assert [(round(p.imag, 2), round(p.real, 2)) for p in KOU_SITE] == \
    [(3.0, 36.18), (6.64, 36.18), (6.64, 38.0), (21.18, 38.0), (21.18, 27.08), (6.64, 27.08), (6.64, 28.9), (3.0, 28.9)]
assert [(round(p.imag, 2), round(p.real, 2)) for p in HEI_SITE] == [(28.0, 37.0), (36.0, 37.0), (36.0, 29.5), (28.0, 29.5)]
assert [(round(p.imag, 2), round(p.real, 2)) for p in OTSU_SITE] == [(2.0, 12.92), (9.28, 12.92), (9.28, 2.0), (2.0, 2.0)]
# 所在の確認：甲建物・丙建物は1番1の中（1番2〈東12・北15まで〉にかからない）、乙建物は1番2の中だけ
for p in KOU_SITE + HEI_SITE:
    assert 0 < p.imag < 40 and 0 < p.real < 40 and not (p.imag <= 12 and p.real <= 15)
    assert p.imag + p.real < 80 - S2       # 北東の隅切りより内側
for p in OTSU_SITE:
    assert 0 < p.imag < 12 and 0 < p.real < 15


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def dims(z, pts, labels, fs=14):
    """多角形の各辺に寸法（None は書かない）を外側に書く。"""
    c = centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs)


def dist_arrow(z, p, q, text, color=BLACK, fs=15, side=(8, 0)):
    """筆界から外壁までの距離の矢印（両向き）と数値。"""
    z.ax.annotate('', xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='<|-|>', color=color, lw=1.6,
                                                           mutation_scale=12, shrinkA=0, shrinkB=0), zorder=6)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    return z.free_text(m, text, fs=fs, color=color,
                       offsets=(side, (-side[0], -side[1]), (0, 12), (0, -12), (side[0] * 2, side[1] * 2),
                                (-side[0] * 2, -side[1] * 2)), ha='center', va='center')


OFFS = ((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0))


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.01
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


def zu01():
    fig, axes = new_figure('分割の前後：一個の建物の一部だけは移転できない',
                           '分割前は甲建物と乙建物で家屋番号1番1の一個の建物。甲建物だけの所有権の移転の登記はできないので、\n先に乙建物を分割して、登記記録上別の一個の建物にする（建物分割登記）',
                           w=16, h=10, ncols=2)
    fig.subplots_adjust(top=0.84)
    frame_all = [S(0.8, 11.3), S(0.8, 39.2), S(22.4, 39.2), S(22.4, 11.3), S(10.3, 11.3), S(10.3, 0.8), S(0.8, 0.8)]
    zs = []
    for k, ax in enumerate(axes):
        z = Zu(ax, fontsize=14)
        z.poly(LOT1, color=GRAY, lw=1.2, check=False)
        z.poly(LOT2, color=GRAY, lw=1.2, check=False)
        z.poly(KOU_SITE, color=BLACK, lw=2.2, fill=BLUE, alpha=0.2)
        z.poly(OTSU_SITE, color=BLACK, lw=2.2, fill=GREEN, alpha=0.22)
        z.free_text(S(30, 20), '1-1', fs=16, color=GRAY, offsets=OFFS)
        z.callout(S(10.8, 1.0), '1-2', dirs=(10, 25, 40), dists=(35, 45, 55), fs=13, color=GRAY)
        z.free_text(K_(11, 5.5), '甲建物\n主　集会所', fs=14)
        if k == 0:
            z.poly(frame_all + [frame_all[0]], color=RED, lw=1.8, ls='--', closed=False)
            z.free_text(O_(3.64, 5.46), '乙建物\n符号1\n倉庫', fs=13)
            z.free_text(S(11.6, 40.6), '家屋番号1番1（一個の建物）', fs=15, color=RED, offsets=((0, 14), (0, 20)))
            z.free_text(S(20, -3.2), '所在：1番地1、1番地2', fs=16, offsets=((0, 0), (0, -8)))
            ax.set_title('分割前（平成29年4月28日の登記記録）', fontsize=17, weight='bold', pad=12)
        else:
            fk = [S(1.8, 25.8), S(22.4, 25.8), S(22.4, 39.2), S(1.8, 39.2)]
            fo = [S(0.8, 0.8), S(10.3, 0.8), S(10.3, 14.2), S(0.8, 14.2)]
            z.poly(fk + [fk[0]], color=BLUE, lw=1.8, ls='--', closed=False)
            z.poly(fo + [fo[0]], color=GREEN, lw=1.8, ls='--', closed=False)
            z.free_text(O_(3.64, 5.46), '乙建物\n（分割）', fs=13)
            z.free_text(S(12, 40.6), '家屋番号1番1', fs=15, color=BLUE, offsets=((0, 14), (0, 20)))
            z.free_text(S(24, 8), '乙建物は\n別の登記記録', fs=14, color=GREEN, offsets=OFFS)
            z.free_text(S(20, -3.2), '甲建物の所在：1番地1', fs=16, offsets=((0, 0), (0, -8)))
            ax.set_title('分割後（平成29年5月19日 分割の登記が完了）', fontsize=17, weight='bold', pad=12)
        fit(ax, LOT1, margin=0.06, extra=[xy(S(20, -5.5)), xy(S(20, 43.5))], pad_aspect=True)
        if k == 1:
            z.north_arrow()
        zs.append(z)
    save(fig, zs, 'H29_dai22mon_zu01_bunkatsu_zengo')


def zu02():
    fig, axes = new_figure('1番1・1番2の敷地の辺長確認図（作図チェック用）',
                           '隅切りの「2.00」は斜めの辺（底辺）。面積は2.00×1.00÷2＝1.00。1番2＝12.00×15.00−1.00＝179.00、1番1＝40.00×40.00−180.00−3.00＝1417.00で、\n登記記録の地積と一致する。辺長は作図が正しいかを確かめるためのもので、建物図面には書かない',
                           w=16, h=10.5, ncols=2, width_ratios=[1.3, 1.0])
    fig.subplots_adjust(top=0.90, bottom=0.14, wspace=0.05)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(LOT1, color=BLACK, lw=2.4, fill=BLUE, alpha=0.12)
    z.poly(LOT2, color=BLACK, lw=2.4, fill=ORANGE, alpha=0.2)
    c1 = centroid(LOT1)
    c2 = centroid(LOT2)
    z.edge_label(LOT1[3], LOT1[2], '37.17m', c1, fs=15)                      # 北
    z.edge_label(LOT1[4], LOT1[5], '37.17m', c1, fs=15)                      # 東
    z.edge_label(LOT1[6], LOT1[7], '26.59m', c1, fs=15)                      # 南
    z.edge_label(LOT1[0], LOT1[1], '23.59m', c1, fs=15)                      # 西
    z.edge_label(LOT1[7], LOT1[8], '15.00m', c2, fs=15)       # 1番2との境（縦）。1番1の側に書く
    z.edge_label(LOT1[8], LOT1[0], '12.00m', c2, fs=15)       # 1番2との境（横）
    z.edge_label(LOT2[0], LOT2[1], '13.59m', c2, fs=14)                      # 1番2の西
    z.edge_label(LOT2[3], LOT2[4], '10.59m', c2, fs=14)                      # 1番2の南
    for a, b, ref in [(LOT1[1], LOT1[2], c1), (LOT1[3], LOT1[4], c1), (LOT1[5], LOT1[6], c1), (LOT2[4], LOT2[0], c2)]:
        z.edge_label(a, b, '2.00m', ref, fs=13, color=RED)
    z.free_text(S(26, 22), '1-1（1417.00㎡）', fs=17)
    z.free_text(S(6.5, 8.5), '1-2\n（179.00㎡）', fs=14)
    z.free_text(S(20, 44.5), '道路（101）', fs=15, color=GRAY, offsets=OFFS)
    z.free_text(S(20, -4.5), '道路（101）', fs=15, color=GRAY, offsets=OFFS)
    fit(ax, LOT1 + LOT2, margin=0.12, extra=[xy(S(20, -6)), xy(S(20, 46))], pad_aspect=True)
    z.north_arrow()
    # 右：北東の隅切りの拡大（直角の頂点＝区画の北東の角）
    z2 = Zu(axes[1], fontsize=14)
    a, b, c = S(40 - S2, 40), S(40, 40), S(40, 40 - S2)
    mid = (a + c) / 2
    z2.poly([a, b, c], color=BLACK, lw=2.2, fill=RED, alpha=0.18)
    z2.line(b, mid, color=PURPLE, lw=1.4, ls='--')
    z2.edge_label(a, c, '2.00m（底辺）', b, fs=15, color=RED, dists=(14, 20, 28))
    z2.edge_label(a, b, '1.41m', mid, fs=13)
    z2.edge_label(b, c, '1.41m', mid, fs=13)
    z2.callout((b + mid) / 2, '高さ 1.00m', dirs=(20, 0, 40), dists=(60, 80, 100), fs=14, color=PURPLE)
    z2.free_text(S(38.6, 37.9), '面積＝2.00×1.00÷2＝1.00㎡', fs=16, offsets=((0, -10), (0, -20), (0, -30)))
    axes[1].set_title('隅切りの拡大（北東の角）', fontsize=16, weight='bold', pad=10)
    fit(axes[1], [a, b, c], margin=0.2, extra=[xy(S(37.6, 37.4)), xy(S(41.2, 40.4))], pad_aspect=True)
    assert abs(abs(a - c) - 2.0) < 1e-9 and abs(abs(b - mid) - 1.0) < 1e-9
    assert round(40 - 2 * S2, 2) == 37.17 and round(28 - S2, 2) == 26.59 and round(25 - S2, 2) == 23.59
    assert round(15 - S2, 2) == 13.59 and round(12 - S2, 2) == 10.59
    save(fig, [z, z2], 'H29_dai22mon_zu02_shikichi_henchou')


def zu03():
    """建物図面の完成形（答案用紙の第3欄の右半分〈建物図面〉の枠の中）。"""
    setup_font()
    fig = plt.figure(figsize=(16, 15), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面の完成形（答案用紙の第3欄・縮尺1/500で描く内容）', fontsize=22, weight='bold', y=0.985)
    # 答案用紙の欄（家屋番号・建物の所在・申請人〈略〉・縮尺）。試験の答案用紙の第3欄の印刷どおり
    cell(fig, 0.06, 0.890, 0.20, 0.935, '家屋番号', fs=15)
    cell(fig, 0.20, 0.890, 0.46, 0.935, '1番1', fs=16, ha='left', color=INK)
    fig.text(0.70, 0.912, '建　物　図　面', ha='center', va='center', fontsize=20)
    cell(fig, 0.06, 0.845, 0.20, 0.890, '建物の所在', fs=15)
    cell(fig, 0.20, 0.845, 0.94, 0.890, 'A市B町三丁目1番地1', fs=16, ha='left', color=INK)
    cell(fig, 0.06, 0.110, 0.94, 0.845, lw=1.8)
    cell(fig, 0.06, 0.065, 0.20, 0.110, '申　請　人', fs=15)
    cell(fig, 0.20, 0.065, 0.74, 0.110, '（略）', fs=15)
    cell(fig, 0.74, 0.065, 0.83, 0.110, '縮尺', fs=15)
    cell(fig, 0.83, 0.065, 0.94, 0.110, '1/500', fs=15)
    fig.text(0.5, 0.030, '敷地1-1の中に甲建物（主）と丙建物（附2）。距離は筆界から外壁まで。乙建物は分割で別の建物になったので描かない。\n'
             '所在は1番地1だけ（1番地2と書かない）。敷地の辺長は書かない。申請人の欄は（略）と印刷済み',
             ha='center', va='center', fontsize=13)
    ax = fig.add_axes([0.08, 0.125, 0.84, 0.70])
    z = Zu(ax, fontsize=15)
    fit(ax, LOT1 + LOT2, margin=0.04, extra=[xy(S(-5, -6)), xy(S(44, 45))], pad_aspect=True)
    z.north_arrow()
    z.poly(LOT1, color=BLACK, lw=2.2)
    z.poly(LOT2, color=GRAY, lw=1.0, ls=':', check=False)
    z.poly(KOU_SITE, color=BLACK, lw=2.4)
    z.poly(HEI_SITE, color=BLACK, lw=2.2)
    # 甲建物：北2.00（東の部分の北西の角・北東の角）、西3.00（西の張り出し）
    dist_arrow(z, S(6.64, 38), S(6.64, 40), '2.00', side=(-26, 0))
    dist_arrow(z, S(21.18, 38), S(21.18, 40), '2.00', side=(-26, 0))
    dist_arrow(z, S(0, 30.5), S(3, 30.5), '3.00', side=(-46, 0))
    # 丙建物：北3.00（北西の角）、東4.00（北東の角・南東の角）
    dist_arrow(z, S(28, 37), S(28, 40), '3.00', side=(26, 0))
    dist_arrow(z, S(36, 37), S(40, 37), '4.00', side=(0, -16))
    dist_arrow(z, S(36, 29.5), S(40, 29.5), '4.00', side=(0, -16))
    z.free_text(K_(11, 5.5), '主', fs=17, bbox=dict(boxstyle='circle,pad=0.3', fc='white', ec=BLACK, lw=1.2))
    z.free_text(H_(4, 3.75), '附2', fs=14, bbox=dict(boxstyle='round,pad=0.25', fc='white', ec=BLACK, lw=1.2))
    z.free_text(S(26, 18), '1-1', fs=18, offsets=OFFS)
    z.free_text(S(6, 7.5), '1-2', fs=16, color=GRAY, offsets=OFFS)
    z.free_text(S(20, 42.5), '道路　101', fs=15, color=GRAY, offsets=OFFS)
    z.free_text(S(26, -2.5), '道路　101', fs=15, color=GRAY, offsets=OFFS)
    z.free_text(S(38, -4.5), '（単位：m）', fs=13, offsets=OFFS)
    save(fig, [z], 'H29_dai22mon_zu03_tatemono_zumen')


def zu04():
    fig, axes = new_figure('甲建物（主である建物）の床面積求積図',
                           '西の張り出し 3.64×7.28＝26.4992 ＋ 東の部分 14.54×10.92＝158.7768 ＝ 185.2760 → 100分の1未満を切り捨てて185.27㎡（四捨五入の185.28は誤り）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    r1, r2 = rect(0, 1.82, 3.64, 9.10), rect(3.64, 0, 18.18, 10.92)
    z.poly(r1, color=GREEN, lw=0, fill=GREEN, alpha=0.28, check=False)
    z.poly(r2, color=BLUE, lw=0, fill=BLUE, alpha=0.2, check=False)
    z.line(P(3.64, 1.82), P(3.64, 9.10), color=GRAY, lw=1.2, ls='--')
    k = [P(*v) for v in KOU]
    z.poly(k, color=BLACK, lw=2.4)
    dims(z, k, ['3.64m', '1.82m', '14.54m', '10.92m', '14.54m', '1.82m', '3.64m', '7.28m'])
    z.free_text(P(1.82, 5.46), '西の\n張り出し\n3.64×7.28\n＝26.4992', fs=13)
    z.free_text(P(10.91, 5.46), '東の部分\n14.54×10.92\n＝158.7768', fs=17)
    z.free_text(P(9.09, 12.9), '床面積：185.27㎡（185.2760の100分の1未満を切り捨て）', fs=17, weight='bold')
    fit(ax, k, margin=0.16, extra=[xy(P(9.09, 13.8)), xy(P(-2.5, -1.5))], pad_aspect=True)
    z.north_arrow()
    assert round(3.64 * 7.28, 4) == 26.4992 and round(14.54 * 10.92, 4) == 158.7768
    save(fig, [z], 'H29_dai22mon_zu04_kou_kyuuseki')


def zu05():
    fig, axes = new_figure('丙建物の床面積：1室なら、天井の低い端まで入れる',
                           '準則第82条第1号の本文（1.5m未満は算入しない）は地階・屋階（特殊階）の話。ただし書で、1室の一部が1.5m未満でも当該1室の面積に算入する。\n6.90は西側立面図の高さ1.50での幅で、平面の寸法ではない：8.00×6.90＝55.20ではなく、8.00×7.50＝60.00㎡',
                           w=16, h=9.5, ncols=3, width_ratios=[0.9, 1.2, 0.9])
    fig.subplots_adjust(top=0.84, wspace=0.12, bottom=0.16)
    hei = [P(*v) for v in HEI]
    wrong = [P(*v) for v in HEI_WRONG]
    # 左：誤り
    z = Zu(axes[0], fontsize=14)
    z.poly(hei, color=BLACK, lw=1.4)
    z.poly(wrong, color=RED, lw=2.2, fill=RED, alpha=0.15, check=False)
    dims(z, hei, ['8.00m', None, None, None])
    z.edge_label(wrong[1], wrong[2], '6.90m', centroid(wrong), fs=14)
    z.free_text(P(4, 3.75), '8.00×6.90\n＝55.20㎡', fs=16, color=RED)
    z.free_text(P(4, 9.3), '北と南の0.30の帯を\n床面積から除外？', fs=14, color=RED, offsets=((0, 0), (0, -8)))
    axes[0].set_title('誤り：高さ1.5m以上だけ（藍子）', fontsize=16, weight='bold', color=RED, pad=12)
    fit(axes[0], hei, margin=0.28, extra=[xy(P(4, 10.5))], pad_aspect=True)
    # 中央：西側立面図（南北の断面。半径3.75の半円、底の幅7.50、高さ1.50での幅6.90）
    ax2 = axes[1]
    z2 = Zu(ax2, fontsize=13)
    r = 3.75
    ax2.add_patch(Arc((0, 0), 2 * r, 2 * r, theta1=0, theta2=180, color=BLACK, lw=2.4, zorder=3))
    z2.line(complex(0, -r), complex(0, r), color=BLACK, lw=2.4)
    hw = 6.90 / 2
    z2.line(complex(1.5, -hw), complex(1.5, hw), color=PURPLE, lw=1.4, ls='--')
    for sgn in (-1, 1):   # 床から0.30の帯（|横| が3.45〜3.75）の上の、天井の低いところを塗る
        xs = [hw + (r - hw) * i / 20 for i in range(21)]
        ys = [math.sqrt(max(r * r - x * x, 0)) for x in xs]
        ax2.fill([sgn * hw] + [sgn * x for x in xs[::-1]] + [sgn * hw], [0] + [0] + ys[::-1][1:] + [ys[0]],
                 color=ORANGE, alpha=0.4, lw=0)
    ax2.add_patch(Rectangle((-0.45, 0), 0.9, 1.6, fill=False, ec=BLACK, lw=1.2))
    z2.segments += [((-0.45, 0), (-0.45, 1.6)), ((0.45, 0), (0.45, 1.6)), ((-0.45, 1.6), (0.45, 1.6))]
    z2.free_text(complex(0.7, 0), '扉', fs=12)
    z2.free_text(complex(-0.45, 0), '7.50（底の幅）', fs=13, offsets=((0, -14), (0, -20)))
    z2.free_text(complex(1.5, 0), '6.90（高さ1.50での幅）', fs=13, color=PURPLE, offsets=((0, 12), (0, 16)))
    z2.free_text(complex(3.75, 0), '頂部の高さ 3.75', fs=13, offsets=((0, 14), (0, 20)))
    z2.callout(complex(0.6, -3.62), '天井の低い端も\n1室の一部', dirs=(-100, -120, -80), dists=(45, 60, 75), fs=13, color=ORANGE)
    ax2.set_title('西側立面図（南北の断面）', fontsize=16, weight='bold', pad=12)
    fit(ax2, [complex(0, -r), complex(r, 0), complex(0, r)], margin=0.2, extra=[(-5.5, -2.6), (5.5, 4.6)], pad_aspect=True)
    # 右：正解
    z3 = Zu(axes[2], fontsize=14)
    z3.poly(hei, color=GREEN, lw=2.4, fill=GREEN, alpha=0.18)
    for s_ in (0.3, 7.2):
        z3.line(P(0, s_), P(8, s_), color=GRAY, lw=1.0, ls=':', check=False)
    dims(z3, hei, ['8.00m', '7.50m', None, None])
    z3.free_text(P(4, 3.75), '8.00×7.50\n＝60.00㎡', fs=16, color=GREEN)
    axes[2].set_title('正解：1室なら端まで', fontsize=16, weight='bold', color=GREEN, pad=12)
    fit(axes[2], hei, margin=0.28, pad_aspect=True)
    assert round(7.50 - 2 * 0.30, 2) == 6.90 and round(8.00 * 7.50 - 8.00 * 6.90, 2) == 4.80
    save(fig, [z, z2, z3], 'H29_dai22mon_zu05_hei_ayamari_hikaku')


def zu06():
    fig, axes = new_figure('丙建物（附属建物符号2）の床面積求積図',
                           '発泡ポリスチレン板の中心（〔調査図素図〕の（注）4）で8.00×7.50＝60.00㎡。\n点線は天井の高さ1.5mの線（北と南の壁から0.30内側）で、床面積の区切りではない',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    hei = [P(*v) for v in HEI]
    z.poly(hei, color=BLACK, lw=2.6, fill=GREEN, alpha=0.2)
    for s_ in (0.3, 7.2):
        z.line(P(0, s_), P(8, s_), color=GRAY, lw=1.2, ls=':', check=False)
    dims(z, hei, ['8.00m', '7.50m', '8.00m', '7.50m'])
    z.free_text(P(4, 3.75), '附属建物　符号2\n8.00×7.50＝60.0000', fs=17)
    z.callout(P(8, 7.2), '天井の高さ1.5mの線\n（床面積の区切りではない）', dirs=(0, 15, -15), dists=(60, 80, 100), fs=13, color=GRAY)
    z.free_text(P(4, 10.2), '床面積：60.00㎡', fs=18, weight='bold', offsets=((0, 0), (0, -10)))
    fit(ax, hei, margin=0.25, extra=[xy(P(4, 11)), xy(P(15, -1))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H29_dai22mon_zu06_hei_kyuuseki')


def zu07():
    """各階平面図の完成形（答案用紙の第3欄の左半分〈各階平面図〉の枠の中。求積図とちがい塗り分けはしない）。"""
    setup_font()
    fig = plt.figure(figsize=(18, 11), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図の完成形（答案用紙の第3欄・縮尺1/250で描く内容）', fontsize=22, weight='bold', y=0.978)
    fig.text(0.5, 0.905, '各　階　平　面　図', ha='center', va='center', fontsize=20)
    cell(fig, 0.04, 0.145, 0.96, 0.880, lw=1.8)
    cell(fig, 0.04, 0.075, 0.14, 0.145, '作　成　者', fs=15)
    cell(fig, 0.14, 0.075, 0.78, 0.145, '（略）　　　　　　　　　　　　（平成29年○月○日作成）', fs=15)
    cell(fig, 0.78, 0.075, 0.86, 0.145, '縮尺', fs=15)
    cell(fig, 0.86, 0.075, 0.96, 0.145, '1/250', fs=15)
    fig.text(0.5, 0.035, '軽量鉄骨の柱の中心・発泡ポリスチレン板の中心の寸法で、主である建物と附属建物（符号2）を描き分け、求積表と床面積を横に書く。\n'
             '丙建物は天井の低い北と南の端も含めた8.00×7.50（不動産登記事務取扱手続準則第82条第1号ただし書）。乙建物は描かない',
             ha='center', va='center', fontsize=14)
    axes = [fig.add_axes([0.06, 0.18, 0.40, 0.62]), fig.add_axes([0.66, 0.40, 0.20, 0.40])]
    fig.text(0.47, 0.49, '主である建物\n3.64×7.28＝26.4992\n14.54×10.92＝158.7768\n計　185.2760\n床面積　185.27㎡',
             ha='left', va='center', fontsize=15, linespacing=1.6)
    fig.text(0.66, 0.29, '附属建物　符号2\n8.00×7.50＝60.0000\n床面積　60.00㎡', ha='left', va='center', fontsize=15, linespacing=1.6)
    zs = []
    # 主である建物（甲建物）。2枚とも同じ縮尺（横・縦とも 約0.33インチ／m）
    z = Zu(axes[0], fontsize=14)
    axes[0].set_title('主である建物', fontsize=17, weight='bold')
    k = [P(*v) for v in KOU]
    fit(axes[0], [P(-1.95, -3.55), P(20.13, 14.47)], margin=0, pad_aspect=True)
    z.north_arrow()
    z.poly(k, color=BLACK, lw=2.4)
    dims(z, k, ['3.64', '1.82', '14.54', '10.92', '14.54', '1.82', '3.64', '7.28'], fs=14)
    zs.append(z)
    # 附属建物（丙建物）符号2
    z = Zu(axes[1], fontsize=14)
    axes[1].set_title('附属建物　符号2', fontsize=17, weight='bold')
    h = [P(*v) for v in HEI]
    fit(axes[1], [P(-1.52, -1.85), P(9.52, 9.35)], margin=0, pad_aspect=True)
    z.poly(h, color=BLACK, lw=2.4)
    dims(z, h, ['8.00', '7.50', '8.00', '7.50'], fs=14)
    zs.append(z)
    assert round(area(k), 4) == 185.276 and round(area(h), 4) == 60.0
    save(fig, zs, 'H29_dai22mon_zu07_kakukai_heimenzu')


def zu08():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    setup_font()
    fig = plt.figure(figsize=(16, 9), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　問1と計算のいらない欄を先に、作図は後に', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.02, 0.16, 0.96, 0.74])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    tl = [('4/28', '依頼\n（調査日）'), ('5/19', '分割の\n登記完了'), ('6/2', '所有権の\n移転'), ('7/20', '保育所に\n種類変更'),
          ('8/10', '丙建物\n新築'), ('8/18', '申請')]
    ax.plot([4, 96], [86, 86], color=GRAY, lw=2)
    for i, (d, t) in enumerate(tl):
        x = 6 + i * 17.6
        ax.plot(x, 86, 'o', ms=10, color=PURPLE)
        ax.text(x, 91, d, ha='center', va='bottom', fontsize=16, weight='bold', color=PURPLE)
        ax.text(x, 82, t, ha='center', va='top', fontsize=13)
    ax.text(1, 97, '時系列メモ（平成29年）', fontsize=15, weight='bold', va='bottom')
    steps = [
        ('①', '前文・問題文\nの注・問を読む', '事実関係より先', BLUE),
        ('②', '問1を答える', '第1欄\n（知識で決まる）', BLUE),
        ('③', '時系列メモ', '甲・乙・丙の\n日付を整理', BLUE),
        ('④', '問2の計算の\nいらない欄', '目的・添付・申請人・\n所在・主の2行', BLUE),
        ('⑤', '敷地の地積の\n検算', '隅切り1.00で\n1417.00・179.00', GREEN),
        ('⑥', '甲・丙の求積', '185.27・60.00\n（ただし書！）', RED),
        ('⑦', '第3欄の作図', '左に各階平面図\n右に建物図面', RED),
        ('⑧', '見直し', '所在・符号2・\n欄番号①', GRAY),
    ]
    w, h, gap = 10.6, 30, 1.6
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 20), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 20 + h - 2.5, no, ha='center', va='top', fontsize=22, color=col, weight='bold')
        ax.text(x + w / 2, 20 + h / 2 - 3, t, ha='center', va='center', fontsize=14)
        ax.text(x + w / 2, 17, ran, ha='center', va='top', fontsize=12, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, 35), xytext=(x + w + 0.2, 35),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 2 * (w + gap) - gap / 2, 60, '計算なしで書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 4 * (w + gap) - gap, 56), xytext=(1, 56), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 6 * (w + gap) - gap / 2, 60, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 7 * (w + gap) - gap, 56), xytext=(1 + 5 * (w + gap), 56),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.06, '作図の前に、甲建物の寸法の累計（東西0・3.64・18.18、南北0・1.82・9.10・10.92）をメモ。\n'
             '丙建物は、求積表を書く前に準則第82条第1号をただし書まで思い出す。作図は甲建物 → 敷地 → 丙建物の順。',
             ha='center', va='center', fontsize=15)
    assert round(3.64 + 14.54, 2) == 18.18 and round(1.82 + 7.28, 2) == 9.10
    path = os.path.join(OUT, 'H29_dai22mon_zu08_toku_junban.png')
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
