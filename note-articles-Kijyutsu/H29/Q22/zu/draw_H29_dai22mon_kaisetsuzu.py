"""平成29年度 第22問（建物）の解説図15枚を、見取図の距離・調査図素図の寸法から作図してPNGに書き出す。

`../prompt_H29_dai22mon_kaisetsuzu.md` の図1〜図15どおり（番号は記事の挿入順。2026-10-08に図2〜図6・図8・図11を足して振り直した）。
画像の題には図の番号を書かない（番号はファイル名と記事のマーカーの管理用）。作図の共通部品は `tools/zu_helpers.py`。
敷地は座標値一覧表がないので、1番1と1番2を合わせた区画（東西40.00・南北40.00）の南西の角を原点にした
(X＝北, Y＝東) で持つ（S(東, 北) で作る）。隅切りは「底辺（斜めの辺）2メートルの直角二等辺三角形」（〔見取図〕の（注）6）
なので、直角をはさむ辺は √2。建物の平面は (東, 南)（原点＝建物を囲む長方形の北西の角）で持ち、P() で (北, 東) に変換する。
建物図面の建物の位置は、筆界から外壁までの距離（〔見取図〕の（注）3・〔調査図素図〕の（注）3）で置く。壁・板の厚さの
注記がないので、外壁と柱・板の中心のずれは考えない（縮尺500分の1では図上に現れない）。
図9（建物図面）と図14（各階平面図）の完成形は、試験の答案用紙（`public/kijutsu/H29-tatemono/a2.webp`）の第3欄の
右半分・左半分を、用紙の寸法（mm）どおりに描き、図形も1/500・1/250の縮尺どおりに置く（2026-10-08）。
図2〜図5・図11・図15は固定配置の図なので重なりの自動検査の対象外（書き出したPNGを目で確かめる）。
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


def zu07():
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
    save(fig, [z, z2], 'H29_dai22mon_zu07_shikichi_henchou')


def zu10():
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
    save(fig, [z], 'H29_dai22mon_zu10_kou_kyuuseki')


def zu12():
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
    save(fig, [z, z2, z3], 'H29_dai22mon_zu12_hei_ayamari_hikaku')


def zu13():
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
    save(fig, [z], 'H29_dai22mon_zu13_hei_kyuuseki')


def zu15():
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
    path = os.path.join(OUT, 'H29_dai22mon_zu15_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図15: 解く順番（固定配置）\n  →', path)


# ---- 答案用紙の第3欄（試験の答案用紙 `public/kijutsu/H29-tatemono/a2.webp` の寸法。A3横で1px＝0.3mm として読んだ） ----
# 第3欄は1枚の枠（横301.5mm × 縦205.2mm）を中央の短い目印で左右に分け、左半分が各階平面図、右半分が建物図面。
# 家屋番号・建物の所在の欄は建物図面の側の上に1つだけ（各階平面図と共通）。作成者・申請人は（略）、
# 作成の日付は「（平成29年○月○日作成）」、縮尺は「1」と分母を斜線で区切った分数で、どれも印刷済み。
# 図は用紙の上の長さ（mm）で描き、建物図面は1mm＝0.5m（1/500）、各階平面図は1mm＝0.25m（1/250）で縮尺どおりに置く。
HALF_W, SHEET_H = 150.9, 205.2       # 半分の枠の横・縦（mm）
TICK_TOP, TICK_BOTTOM = 9.9, 9.6     # 中央の目印の長さ（mm）


def paper(fig_w_in, x0, x1, y0, y1):
    """用紙の座標（mm。原点は枠の下の辺と左の辺が交わる点）で描く軸を、図全体に1つ作る。縦横は同じ縮尺。"""
    setup_font()
    h_in = fig_w_in * (y1 - y0) / (x1 - x0)
    fig = plt.figure(figsize=(fig_w_in, h_in), dpi=100)
    fig.patch.set_facecolor('white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax


def pline(ax, pts, lw=1.6, color=BLACK, ls='-'):
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=color, lw=lw, ls=ls, solid_capstyle='butt', zorder=1)


def pbox(ax, x0, y0, x1, y1, text='', fs=15, ha='center', color=BLACK, lw=1.6):
    pline(ax, [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], lw=lw)
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 2.2
        ax.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


def pfrac(ax, x0, y0, x1, y1, den):
    """縮尺の欄（答案用紙の印刷どおり、左上に「1」、右下に分母、その間に斜めの線）。"""
    pbox(ax, x0, y0, x1, y1)
    w, h = x1 - x0, y1 - y0
    pline(ax, [(x0 + 0.18 * w, y0 + 0.2 * h), (x0 + 0.85 * w, y0 + 0.82 * h)], lw=1.2)
    ax.text(x0 + 0.38 * w, y0 + 0.76 * h, '1', ha='center', va='center', fontsize=14)
    ax.text(x0 + 0.66 * w, y0 + 0.26 * h, den, ha='center', va='center', fontsize=14)


def half_frame(ax, cut):
    """第3欄の半分の枠。切り取った側（cut='left'〈建物図面〉か 'right'〈各階平面図〉）は灰色の点線にし、
    答案用紙の中央の短い目印（上下）を実線で描く。"""
    xs, xc = (HALF_W, 0.0) if cut == 'left' else (0.0, HALF_W)
    pline(ax, [(xc, SHEET_H), (xs, SHEET_H), (xs, 0), (xc, 0)], lw=1.9)
    pline(ax, [(xc, 0), (xc, SHEET_H)], lw=1.0, color=GRAY, ls=(0, (4, 4)))
    pline(ax, [(xc, SHEET_H), (xc, SHEET_H - TICK_TOP)], lw=1.9)
    pline(ax, [(xc, 0), (xc, TICK_BOTTOM)], lw=1.9)


def to_pfrac(ax, x, y):
    """用紙の座標（mm）を軸の割合にする（north_arrow の位置の指定用）。"""
    (x0, x1), (y0, y1) = ax.get_xlim(), ax.get_ylim()
    return ((x - x0) / (x1 - x0), (y - y0) / (y1 - y0))


SITE_X0, SITE_Y0 = 35.0, 52.0        # 建物図面：区画（40.00×40.00）の南西の角を置く用紙の位置（mm）


def Sp(e, n):
    """敷地の (東, 北)（m）を、建物図面の用紙の座標（mm、1/500＝1m→2mm）の複素数（縦＋横i）にする。"""
    return complex(SITE_Y0 + 2 * n, SITE_X0 + 2 * e)


def to_paper500(p):
    """S() で作った敷地の点（北＋東i、m）を用紙の座標にする。"""
    return Sp(p.imag, p.real)


def zu09():
    """建物図面の完成形（答案用紙の第3欄の右半分〈建物図面〉の枠の中に、縮尺1/500どおり）。"""
    fig, ax = paper(15, -8, HALF_W + 6, -42, SHEET_H + 33)
    ax.text(HALF_W / 2, SHEET_H + 27, '建物図面の完成形（答案用紙の第3欄の右半分・縮尺1/500）', ha='center', va='center',
            fontsize=21, weight='bold')
    half_frame(ax, cut='left')
    # 上の欄：家屋番号（枠の上に飛び出す）・建物の所在（枠の中の1行目）。記入は濃い青
    pbox(ax, 7.8, SHEET_H, 31.8, SHEET_H + 9.6, '家屋番号', fs=14)
    pbox(ax, 31.8, SHEET_H, 69.9, SHEET_H + 9.6, '1番1', fs=15, ha='left', color=INK)
    ax.text(104.4, SHEET_H + 3.6, '建　物　図　面', ha='center', va='center', fontsize=19)
    pbox(ax, 7.8, SHEET_H - 9.9, 31.8, SHEET_H, '建物の所在', fs=14)
    pbox(ax, 31.8, SHEET_H - 9.9, HALF_W, SHEET_H, 'A市B町三丁目1番地1', fs=15, ha='left', color=INK)
    # 下の欄：申請人（略）・縮尺 1/500（枠の下に接する別の枠）
    pbox(ax, 7.8, -14.7, 27.0, 0, '申 請 人', fs=14)
    pbox(ax, 27.0, -14.7, 117.0, 0, '（略）', fs=14)
    pbox(ax, 117.0, -14.7, 126.9, 0, '縮尺', fs=13)
    pfrac(ax, 126.9, -14.7, HALF_W, 0, '500')
    ax.text(HALF_W / 2, -29, '敷地1-1の中に甲建物（主）と丙建物（附2）。距離は筆界から外壁まで。乙建物は分割で別の建物になったので描かない。\n'
            '所在は1番地1だけ（1番地2と書かない）。敷地の辺長は書かない（答案用紙の第3欄は1枚の枠で、左の点線から左は各階平面図の欄）',
            ha='center', va='center', fontsize=12.5, linespacing=1.6)
    z = Zu(ax, fontsize=14)
    lot1 = [to_paper500(p) for p in LOT1]
    lot2 = [to_paper500(p) for p in LOT2]
    kou = [to_paper500(p) for p in KOU_SITE]
    hei = [to_paper500(p) for p in HEI_SITE]
    z.north_arrow(pos=to_pfrac(ax, 136, 160), length=0.07)
    z.poly(lot1, color=BLACK, lw=2.0)
    z.poly(lot2, color=GRAY, lw=1.0, ls=':', check=False)
    z.poly(kou, color=BLACK, lw=2.4)
    z.poly(hei, color=BLACK, lw=2.2)
    # 甲建物：北2.00（東の部分の北西の角・北東の角）、西3.00（西の張り出し）
    dist_arrow(z, Sp(6.64, 38), Sp(6.64, 40), '2.00', side=(-24, 0), fs=13)
    dist_arrow(z, Sp(21.18, 38), Sp(21.18, 40), '2.00', side=(-24, 0), fs=13)
    dist_arrow(z, Sp(0, 30.5), Sp(3, 30.5), '3.00', side=(0, -14), fs=13)
    # 丙建物：北3.00（北西の角）、東4.00（北東の角・南東の角）
    dist_arrow(z, Sp(28, 37), Sp(28, 40), '3.00', side=(-24, 0), fs=13)
    dist_arrow(z, Sp(36, 37), Sp(40, 37), '4.00', side=(0, -14), fs=13)
    dist_arrow(z, Sp(36, 29.5), Sp(40, 29.5), '4.00', side=(0, 14), fs=13)
    z.free_text(to_paper500(K_(11, 5.5)), '主', fs=15, bbox=dict(boxstyle='circle,pad=0.25', fc='white', ec=BLACK, lw=1.2))
    z.free_text(to_paper500(H_(4, 3.75)), '附2', fs=12, bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=BLACK, lw=1.2))
    z.free_text(Sp(26, 16), '1-1', fs=16, offsets=OFFS)
    z.free_text(Sp(6, 7.5), '1-2', fs=14, color=GRAY, offsets=OFFS)
    z.free_text(Sp(20, 43.5), '道路（101）', fs=14, offsets=OFFS)
    z.free_text(Sp(26, -3.5), '道路（101）', fs=14, offsets=OFFS)
    z.free_text(Sp(43, -9), '（単位：m）', fs=12, offsets=OFFS)
    # 縮尺どおりか：区画の東西40.00mが用紙の80mm（1/500）
    assert abs(abs(Sp(40, 0) - Sp(0, 0)) - 80.0) < 1e-9
    save(fig, [z], 'H29_dai22mon_zu09_tatemono_zumen')


def P250(x0, y0):
    """建物の平面の (東, 南)（m）を、各階平面図の用紙の座標（mm、1/250＝1m→4mm）の複素数にする。
    (x0, y0) は建物を囲む長方形の北西の角を置く用紙の位置（mm）。"""
    return lambda e, s: complex(y0 - 4 * s, x0 + 4 * e)


def zu14():
    """各階平面図の完成形（答案用紙の第3欄の左半分〈各階平面図〉の枠の中に、縮尺1/250どおり。求積図とちがい塗り分けはしない）。"""
    fig, ax = paper(15, -6, HALF_W + 8, -42, SHEET_H + 33)
    ax.text(HALF_W / 2, SHEET_H + 27, '各階平面図の完成形（答案用紙の第3欄の左半分・縮尺1/250）', ha='center', va='center',
            fontsize=21, weight='bold')
    ax.text(80.1, SHEET_H + 3.3, '各　階　平　面　図', ha='center', va='center', fontsize=19)
    half_frame(ax, cut='right')
    # 下の欄：作成者（略）（平成29年○月○日作成）・縮尺 1/250（すべて印刷済み）
    pbox(ax, 0, -14.7, 18.9, 0, '作 成 者', fs=14)
    pbox(ax, 18.9, -14.7, 109.2, 0)
    ax.text(35.1, -7.0, '（略）', ha='center', va='center', fontsize=14)
    ax.text(107.4, -11.2, '（平成29年○月○日作成）', ha='right', va='center', fontsize=12.5)
    pbox(ax, 109.2, -14.7, 119.1, 0, '縮尺', fs=13)
    pfrac(ax, 119.1, -14.7, 143.1, 0, '250')
    ax.text(HALF_W / 2, -29, '軽量鉄骨の柱の中心・発泡ポリスチレン板の中心の寸法で、主である建物と附属建物（符号2）を描き分け、求積表と床面積を横に書く。\n'
            '丙建物は天井の低い北と南の端も含めた8.00×7.50（準則第82条第1号ただし書）。乙建物は描かない（右の点線から右は建物図面の欄）',
            ha='center', va='center', fontsize=12.5, linespacing=1.6)
    zs = []
    # 主である建物（甲建物）：北西の角を用紙の (12, 182) に置く。18.18m × 10.92m → 72.72mm × 43.68mm
    PK = P250(12, 180)
    k = [PK(*v) for v in KOU]
    z = Zu(ax, fontsize=13)
    z.poly(k, color=BLACK, lw=2.2)
    dims(z, k, ['3.64', '1.82', '14.54', '10.92', '14.54', '1.82', '3.64', '7.28'], fs=13)
    ax.text(48.4, 190.5, '主である建物', ha='center', va='center', fontsize=15, weight='bold')
    ax.text(96, 158, '3.64×7.28＝26.4992\n14.54×10.92＝158.7768\n計　185.2760\n床面積　185.27m²',
            ha='left', va='center', fontsize=13.5, linespacing=1.7)
    # 附属建物（丙建物）符号2：北西の角を用紙の (18, 92) に置く。8.00m × 7.50m → 32.00mm × 30.00mm
    PH = P250(20, 94)
    h = [PH(*v) for v in HEI]
    z.poly(h, color=BLACK, lw=2.2)
    dims(z, h, ['8.00', '7.50', '8.00', '7.50'], fs=13)
    ax.text(36, 103, '附属建物　符号2', ha='center', va='center', fontsize=15, weight='bold')
    ax.text(70, 79, '8.00×7.50＝60.0000\n床面積　60.00m²', ha='left', va='center', fontsize=13.5, linespacing=1.7)
    zs.append(z)
    # 縮尺どおりか（1/250）・面積
    assert abs(abs(k[2] - k[3]) - 4 * 14.54) < 1e-9 and abs(abs(h[0] - h[1]) - 4 * 8.00) < 1e-9
    assert round(area(k) / 16, 4) == 185.276 and round(area(h) / 16, 4) == 60.0
    save(fig, zs, 'H29_dai22mon_zu14_kakukai_heimenzu')


def fixed(title, caption, w=16, h=10):
    """固定配置の図（座標 0〜100 の軸）。重なりの自動検査の対象外なので、書き出したPNGを目で確かめる。"""
    setup_font()
    fig = plt.figure(figsize=(w, h), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=23, weight='bold', y=0.965)
    if caption:
        fig.text(0.5, 0.035, caption, ha='center', va='center', fontsize=15, linespacing=1.6)
    ax = fig.add_axes([0.02, 0.12, 0.96, 0.78])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    return fig, ax


def fbox(ax, x, y, w, h, text='', col=BLACK, fc=None, alpha=0.14, fs=14, ls='-', lw=2.0, weight='normal', tcol=BLACK):
    ax.add_patch(Rectangle((x, y), w, h, facecolor='none', edgecolor=col, lw=lw, ls=ls))
    if fc:
        ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, alpha=alpha, edgecolor='none'))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs, weight=weight, color=tcol, linespacing=1.5)


def farrow(ax, p, q, col=GRAY, lw=2.2):
    ax.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle='-|>', lw=lw, color=col, mutation_scale=22))


def save_fixed(fig, name):
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print(f'[重なり検査] {name}（固定配置。目で確かめる）\n  →', path)


def zu02():
    """建物区分登記と建物分割登記の比較（固定配置）。"""
    fig, ax = fixed('区分と分割：一棟の中を区分建物にするか、附属建物を切り離すか',
                    '本問の乙建物は、甲建物から離れて建つ別の棟の附属建物。区分建物でもないので、区分ではなく分割（建物分割登記）。\n'
                    'どちらも表題部所有者か所有権の登記名義人しか申請できない（不動産登記法第54条第1項）')
    ax.plot([50, 50], [2, 98], color=GRAY, lw=1.2)
    # 左：区分
    ax.text(25, 95, '建物の区分の登記（同項第2号）', ha='center', va='center', fontsize=18, weight='bold', color=GRAY)
    ax.text(25, 88, '一棟の建物の中の、構造上区分された部分を\n登記記録上区分建物にする（例：マンションの各部屋）', ha='center', va='center', fontsize=13.5)
    fbox(ax, 10, 52, 30, 26, col=BLACK, fc=GRAY, alpha=0.08)
    for i, (x, y, t) in enumerate([(10, 65, '201'), (25, 65, '202'), (10, 52, '101'), (25, 52, '102')]):
        fbox(ax, x, y, 15, 13, t, col=BLACK, fs=15)
    ax.text(25, 81, '一棟の建物（登記記録は1つ）', ha='center', va='center', fontsize=13.5)
    farrow(ax, (25, 49), (25, 41))
    for i, t in enumerate(['101', '102', '201', '202']):
        fbox(ax, 4 + i * 11.2, 24, 9.6, 13, f'区分建物\n{t}', col=GRAY, fc=GRAY, alpha=0.1, fs=12)
    ax.text(25, 18, '部屋ごとに登記記録ができる', ha='center', va='center', fontsize=14, color=GRAY)
    # 右：分割（本問）
    ax.text(75, 95, '建物の分割の登記（同項第1号）', ha='center', va='center', fontsize=18, weight='bold', color=BLUE)
    ax.text(75, 88, '離れて建つ附属建物を登記記録から切り離して\n登記記録上別の一個の建物にする（本問の問1）', ha='center', va='center', fontsize=13.5)
    fbox(ax, 55, 50, 40, 31, col=RED, ls='--', lw=2.2)
    ax.text(75, 78, '家屋番号1番1（一個の建物）', ha='center', va='center', fontsize=13.5, color=RED)
    fbox(ax, 58, 53, 18, 20, '甲建物\n主', col=BLACK, fc=BLUE, alpha=0.18, fs=14)
    fbox(ax, 81, 53, 11, 14, '乙建物\n符号1', col=BLACK, fc=GREEN, alpha=0.2, fs=13)
    farrow(ax, (75, 48), (75, 41))
    fbox(ax, 56, 18, 20, 21, col=BLUE, ls='--', lw=2.0)
    fbox(ax, 58, 21, 16, 12, '甲建物', col=BLACK, fc=BLUE, alpha=0.18, fs=14)
    ax.text(66, 36, '1番1', ha='center', va='center', fontsize=13, color=BLUE)
    fbox(ax, 79, 18, 16, 21, col=GREEN, ls='--', lw=2.0)
    fbox(ax, 81, 21, 12, 12, '乙建物', col=BLACK, fc=GREEN, alpha=0.2, fs=14)
    ax.text(87, 36, '別の登記記録', ha='center', va='center', fontsize=13, color=GREEN)
    ax.text(75, 11, '甲建物だけの所有権の移転の登記ができるようになる', ha='center', va='center', fontsize=14, color=BLUE, weight='bold')
    save_fixed(fig, 'H29_dai22mon_zu02_kubun_bunkatsu')


def zu03():
    """各階平面図の添付の要否（固定配置）。"""
    fig, ax = fixed('問1③　分割の登記に各階平面図は要るか',
                    '形も床面積も変わらなくても、分割で登記記録が2つになる。建物図面と各階平面図は一個の建物ごとに作り（不動産登記規則第81条）、\n'
                    '分割後の各建物を表示して符号を付ける（同規則第84条）。だから「添付しなければならない。」')
    ax.plot([50, 50], [2, 98], color=GRAY, lw=1.2)
    ax.text(25, 94, '所在だけを変える表題部の変更の登記', ha='center', va='center', fontsize=17, weight='bold', color=GRAY)
    fbox(ax, 12, 62, 26, 22, '一個の建物\n（登記記録は1つのまま）', col=GRAY, fc=GRAY, alpha=0.1, fs=14)
    farrow(ax, (25, 60), (25, 52))
    fbox(ax, 5, 26, 40, 24, '添付：変更後の建物図面だけ\n（不動産登記令別表14の項、\n添付情報欄イ）', col=GRAY, fs=15)
    ax.text(25, 16, '各階平面図は要らない', ha='center', va='center', fontsize=16, color=GRAY, weight='bold')
    ax.text(75, 94, '建物の分割の登記（本問の問1）', ha='center', va='center', fontsize=17, weight='bold', color=BLUE)
    fbox(ax, 62, 72, 26, 14, '1番1（甲建物＋乙建物）', col=RED, ls='--', fs=14)
    farrow(ax, (70, 70), (64, 63))
    farrow(ax, (80, 70), (86, 63))
    for x, t, c in [(52, '1番1\n甲建物', BLUE), (76, '別の家屋番号\n乙建物', GREEN)]:
        fbox(ax, x, 50, 22, 12, t, col=c, fc=c, alpha=0.12, fs=13)
        fbox(ax, x + 1, 41, 9.5, 7, '建物図面', col=BLACK, fs=11)
        fbox(ax, x + 11.5, 41, 9.5, 7, '各階平面図', col=BLACK, fs=11)
    fbox(ax, 55, 20, 40, 17, '添付：分割後の建物図面及び各階平面図\n（不動産登記令別表16の項、添付情報欄イ）', col=BLUE, fc=BLUE, alpha=0.08, fs=15)
    ax.text(75, 12, '添付しなければならない', ha='center', va='center', fontsize=17, color=BLUE, weight='bold')
    save_fixed(fig, 'H29_dai22mon_zu03_kakukai_youhi')


def zu04():
    """建物ごとの時系列メモ（固定配置）。"""
    fig, ax = fixed('建物ごとの時系列メモ（平成29年）',
                    '問2の申請書に書く日付は、甲建物の種類変更（7月20日）と丙建物の新築（8月10日）。どちらも変更から1月以内に申請（不動産登記法第51条第1項）。\n'
                    '登記記録の調査日（4月28日）は分割の登記（5月19日）より前なので、所在・符号は分割の後の登記記録で考える',
                    w=16, h=9.5)
    dates = [('4/28', 18), ('5/19', 33), ('6/2', 46), ('7/20', 62), ('8/10', 77), ('8/18', 91)]
    lanes = [('甲建物\n（主である建物）', 72, BLUE), ('乙建物\n（符号1の附属建物）', 46, GREEN), ('丙建物\n（倉庫）', 20, ORANGE)]
    for d, x in dates:
        ax.plot([x, x], [8, 88], color='#cccccc', lw=1.2, ls='--', zorder=0)
        ax.text(x, 93, d, ha='center', va='center', fontsize=17, weight='bold', color=PURPLE)
    for t, y, c in lanes:
        ax.plot([12, 97], [y, y], color=c, lw=3, alpha=0.5)
        ax.text(5.5, y, t, ha='center', va='center', fontsize=14, weight='bold', color=c)
    ev = [(18, 72, '依頼・調査日\n（登記記録は分割前）', GRAY), (33, 72, '分割の登記の完了\n所在は1番地1だけに', BLUE),
          (46, 72, 'C福祉会へ\n所有権の移転', BLUE), (62, 72, '内装工事の完了\n保育所に種類変更', RED),
          (33, 46, '分割で別の\n一個の建物に', GREEN), (57, 46, 'B町自治会が持ち続ける\n（問2の申請書には出てこない）', GRAY),
          (77, 20, '新築\n符号2の附属建物', RED)]
    for x, y, t, c in ev:
        ax.plot(x, y, 'o', ms=12, color=c, zorder=3)
        ax.text(x, y - 5.5, t, ha='center', va='top', fontsize=12.5, color=BLACK if c != RED else RED, linespacing=1.4)
    ax.plot([91, 91], [10, 86], color=PURPLE, lw=2.6)
    ax.text(91, 6, '申請（答案用紙に印刷済み）', ha='center', va='center', fontsize=13, color=PURPLE)
    ax.annotate('', xy=(33, 99), xytext=(18, 99), arrowprops=dict(arrowstyle='<->', lw=1.5, color=GRAY))
    ax.text(25.5, 101.5, '問1（分割）', ha='center', va='bottom', fontsize=13, color=GRAY)
    ax.annotate('', xy=(91, 99), xytext=(62, 99), arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    ax.text(76.5, 101.5, '問2（表題部変更登記）', ha='center', va='bottom', fontsize=13, color=RED)
    ax.set_ylim(0, 106)
    save_fixed(fig, 'H29_dai22mon_zu04_jikeiretsu')


def zu05():
    """注の仕分け（固定配置）。"""
    fig, ax = fixed('注の仕分け　3系統の注を名前で呼び分ける',
                    '「注3」は3つある（縮尺／筆界から外壁までの距離が2つ）。記事でも「問題文の注3」「〔見取図〕の（注）6」「〔調査図素図〕の（注）4」と書き分ける',
                    w=16, h=11)
    cat = {'作図': (RED, '問3の作図（縮尺）'), '距離': (BLUE, '建物図面の距離'), '敷地': (ORANGE, '敷地の地積の検算'),
           '床': (GREEN, '床面積'), '前提': (GRAY, '読み方の前提'), '書き方': (PURPLE, '答案の書き方')}
    cols = [('問題文の注', [('1', '行為・書類は全て適法', '書き方'), ('2', '書面申請', '書き方'),
                         ('3', '建物図面1/500・各階平面図1/250', '作図'), ('4', '訂正・加入・削除の仕方', '書き方')]),
            ('〔見取図〕の（注）', [('1', '距離の単位はメートル', '前提'), ('2', '（　）内は土地の地番', '前提'),
                               ('3', '距離は筆界線から外壁まで', '距離'), ('4', '隅切りを除き直交', '前提'),
                               ('5', '北の方向は道路・建物に平行又は垂直', '前提'), ('6', '隅切りは底辺2mの直角二等辺三角形', '敷地')]),
            ('〔調査図素図〕の（注）', [('1', '距離の単位はメートル', '前提'), ('2', '（　）内は土地の地番', '前提'),
                                 ('3', '距離は筆界線から外壁まで', '距離'), ('4', '測定値は柱の中心・発泡ポリスチレン板の中心', '床'),
                                 ('5', '建物の隅角部は全て直角', '前提'), ('6', '立面図と平面図は縮尺が違う', '床')])]
    for i, (head, items) in enumerate(cols):
        x = 1 + i * 33
        ax.text(x + 15.5, 96, head, ha='center', va='center', fontsize=18, weight='bold')
        for j, (no, t, k) in enumerate(items):
            c = cat[k][0]
            y = 83 - j * 11.5
            fbox(ax, x, y, 31, 9.5, col=c, fc=c, alpha=0.13, lw=1.8)
            ax.text(x + 1.5, y + 4.75, no, ha='left', va='center', fontsize=17, weight='bold', color=c)
            ax.text(x + 5, y + 4.75, t, ha='left', va='center', fontsize=12.5)
    for j, (k, (c, t)) in enumerate(cat.items()):
        x = 3 + j * 16.3
        ax.add_patch(Rectangle((x, 2), 3, 3, facecolor=c, alpha=0.4, edgecolor=c))
        ax.text(x + 4, 3.5, t, ha='left', va='center', fontsize=12.5, color=c if c != GRAY else BLACK)
    save_fixed(fig, 'H29_dai22mon_zu05_chuu_shiwake')


def zu06():
    """隅切りの読み違い（1番2の南西の角を拡大。左＝直角をはさむ辺を2.00と読んだ誤り、右＝底辺2.00の正解）。"""
    fig, axes = new_figure('隅切りの「2.00」は斜めの辺（底辺）',
                           '〔見取図〕の（注）6は「底辺を2メートルとする直角二等辺三角形」。底辺は直角の向かい側の斜めの辺なので、高さは1.00、面積は2.00×1.00÷2＝1.00。\n'
                           '1番2＝12.00×15.00−1.00＝179.00、1番1＝1600.00−180.00−3.00＝1417.00で、どちらも登記記録の地積と一致する（図は1番2の南西の角の拡大）',
                           w=16, h=10.5, ncols=2)
    fig.subplots_adjust(top=0.86, bottom=0.17, wspace=0.10)
    lot2_ng = [S(0, 2), S(0, 15), S(12, 15), S(12, 0), S(2, 0)]
    zs = []
    for k, (ax, pts, tri) in enumerate([(axes[0], lot2_ng, [S(0, 2), S(0, 0), S(2, 0)]),
                                         (axes[1], LOT2, [S(0, S2), S(0, 0), S(S2, 0)])]):
        z = Zu(ax, fontsize=14)
        col = RED if k == 0 else GREEN
        fit(ax, [S(-1.6, -1.6), S(5.4, 5.4)], margin=0.0, pad_aspect=True)
        ax.set_clip_on(True)
        z.poly(pts, color=BLACK, lw=2.6, fill=ORANGE, alpha=0.15, check=False)
        z.poly(tri, color=col, lw=2.0, ls='--', fill=col, alpha=0.25, check=False)
        z.segments += [(xy(tri[0]), xy(tri[1])), (xy(tri[1]), xy(tri[2])), (xy(tri[2]), xy(tri[0])),
                       (xy(S(0, 2 if k == 0 else S2)), xy(S(0, 6))), (xy(S(2 if k == 0 else S2, 0)), xy(S(6, 0)))]
        z.free_text(S(3.6, 4.4), '1-2', fs=18, color=GRAY)
        if k == 0:
            z.edge_label(S(0, 2), S(0, 0), '2.00', S(1, 1), fs=16, color=RED, dists=(16, 24, 32))
            z.edge_label(S(0, 0), S(2, 0), '2.00', S(1, 1), fs=16, color=RED, dists=(16, 24, 32))
            z.free_text(S(3.4, 2.6), '隅切り 2.00×2.00÷2＝2.00\n12.00×15.00−2.00＝178.00\n登記記録179.00と合わない', fs=16, color=RED)
            ax.set_title('誤り：直角をはさむ2本の辺を2.00と読む', fontsize=17, weight='bold', color=RED, pad=12)
        else:
            z.edge_label(S(0, S2), S(S2, 0), '2.00（底辺）', S(2, 2), fs=16, color=GREEN, dists=(-30, -38, -46))
            z.edge_label(S(0, S2), S(0, 0), '1.41', S(1, 1), fs=14, dists=(16, 24, 32))
            z.edge_label(S(0, 0), S(S2, 0), '1.41', S(1, 1), fs=14, dists=(16, 24, 32))
            z.line(S(0, 0), S(S2 / 2, S2 / 2), color=PURPLE, lw=2.0)
            z.callout(S(S2 / 4, S2 / 4), '高さ 1.00', dirs=(-45, -30, -60), dists=(70, 90, 110), fs=15, color=PURPLE)
            z.free_text(S(3.4, 2.6), '隅切り 2.00×1.00÷2＝1.00\n12.00×15.00−1.00＝179.00\n登記記録と一致', fs=16, color=GREEN)
            ax.set_title('正解：斜めの辺（底辺）が2.00', fontsize=17, weight='bold', color=GREEN, pad=12)
            z.north_arrow()
        zs.append(z)
    assert round(180 - 2 * 2 / 2, 2) == 178.00 and round(180 - 2 * 1 / 2, 2) == 179.00
    assert abs(abs(S(0, S2) - S(S2, 0)) - 2) < 1e-9 and abs(abs(S(S2 / 2, S2 / 2)) - 1) < 1e-9
    save(fig, zs, 'H29_dai22mon_zu06_sumikiri_ayamari')


def zu08():
    """所在の確認（筆界からの距離で建物の位置を出し、1番2〈東12.00・北15.00まで〉にかかるかを確かめる）。"""
    fig, axes = new_figure('所在の確認：建物の位置を距離から出して、1番2にかかるか確かめる',
                           '区画の南西の角を原点に、西の筆界・南の筆界からの距離で比べる。甲建物と丙建物は1番1だけ（所在「1番地1」）。\n'
                           '乙建物は1番2の中にあり、分割で甲建物の登記記録から抜けるので、甲建物の所在から「1番地2」が消える',
                           w=16, h=11, ncols=2, width_ratios=[1.05, 0.95])
    fig.subplots_adjust(top=0.90, bottom=0.15, wspace=0.04)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fit(ax, LOT1 + LOT2, margin=0.06, extra=[xy(S(-3, -4)), xy(S(43, 44))], pad_aspect=True)
    z.poly(LOT1, color=BLACK, lw=2.0)
    z.poly(LOT2, color=BLACK, lw=2.0, fill=ORANGE, alpha=0.2)
    z.line(S(12, 15), S(40, 15), color=ORANGE, lw=1.4, ls='--')
    z.free_text(S(33, 15), '1番2の北の端（15.00）', fs=13, color=ORANGE, offsets=((0, 12), (0, -12), (-20, 12)))
    z.line(S(28, 29.5), S(28, 21), color=GRAY, lw=1.2, ls=':')
    z.poly(KOU_SITE, color=BLACK, lw=2.2, fill=BLUE, alpha=0.2)
    z.poly(HEI_SITE, color=BLACK, lw=2.2, fill=GREEN, alpha=0.22)
    z.poly(OTSU_SITE, color=GRAY, lw=1.6, ls='--', fill=GRAY, alpha=0.12)
    z.free_text(K_(11, 5.5), '甲建物', fs=15)
    z.free_text(H_(4, 3.75), '丙建物', fs=14)
    z.free_text(O_(3.64, 5.46), '乙建物\n（分割）', fs=13, color=GRAY)
    dist_arrow(z, S(19, 0), S(19, 27.08), '27.08', side=(24, 0), fs=14)
    dist_arrow(z, S(0, 22), S(28, 22), '28.00', side=(0, 12), fs=14)
    z.edge_label(LOT2[1], LOT2[2], '12.00', centroid(LOT2), fs=13, color=ORANGE)
    z.edge_label(LOT2[2], LOT2[3], '15.00', centroid(LOT2), fs=13, color=ORANGE)
    z.free_text(S(28, 8), '1-1', fs=16, color=GRAY, offsets=OFFS)
    z.callout(S(1.5, 1.5), '1-2', dirs=(200, 215, 185), dists=(40, 55, 70), fs=14, color=ORANGE)
    z.north_arrow()
    ax2 = axes[1]
    ax2.axis('off')
    lines = [('甲建物（東の部分）', '南の外壁＝40.00−2.00−10.92\n＝27.08 ＞ 15.00', BLUE),
             ('甲建物（西の張り出し）', '南の外壁＝40.00−(2.00＋1.82＋7.28)\n＝28.90 ＞ 15.00', BLUE),
             ('丙建物', '西の端＝40.00−4.00−8.00＝28.00 ＞ 12.00\n（南の外壁 40.00−3.00−7.50＝29.50）', GREEN),
             ('乙建物（分割済み）', '東の端＝2.00＋7.28＝9.28 ≦ 12.00\n北の端＝2.00＋10.92＝12.92 ≦ 15.00', GRAY)]
    for i, (h_, t, c) in enumerate(lines):
        y = 0.94 - i * 0.205
        ax2.text(0.02, y, h_, transform=ax2.transAxes, fontsize=16, weight='bold', color=c, va='top')
        ax2.text(0.04, y - 0.05, t, transform=ax2.transAxes, fontsize=15, va='top', linespacing=1.5)
    ax2.text(0.02, 0.10, '→ 所在は「A市B町三丁目1番地1」だけ', transform=ax2.transAxes, fontsize=17, weight='bold', color=RED, va='center')
    assert round(40 - 2 - 10.92, 2) == 27.08 and round(40 - (2 + 1.82 + 7.28), 2) == 28.90
    assert round(40 - 4 - 8, 2) == 28.00 and round(40 - 3 - 7.5, 2) == 29.50 and round(2 + 7.28, 2) == 9.28 and round(2 + 10.92, 2) == 12.92
    save(fig, [z], 'H29_dai22mon_zu08_shozai_kakunin')


def zu11():
    """準則第82条第1号の読み方（固定配置）。"""
    fig, ax = fixed('準則第82条第1号は、ただし書まで読む',
                    '「天井の高さ１．５メートル未満の地階及び屋階（特殊階）は、床面積に算入しない。ただし、１室の一部が天井の高さ１．５メートル未満であっても、\n'
                    'その部分は、当該１室の面積に算入する。」（不動産登記事務取扱手続準則第82条第1号）。6.90は西側立面図の高さ1.50での幅で、平面の寸法ではない')
    fbox(ax, 30, 84, 40, 11, '天井の高さ1.5m未満の部分がある', col=BLACK, fs=17, weight='bold')
    farrow(ax, (50, 83), (50, 75))
    fbox(ax, 22, 60, 56, 14, '階全体が天井の低い地階・屋階（特殊階）か？\nそれとも1室の一部が低いだけか？', col=PURPLE, fc=PURPLE, alpha=0.08, fs=16)
    farrow(ax, (34, 59), (22, 48), col=GRAY)
    farrow(ax, (66, 59), (78, 48), col=GREEN)
    ax.text(18, 55, '階全体が低い', ha='center', va='center', fontsize=14, color=GRAY)
    ax.text(83, 56, '1室の一部が低いだけ', ha='left', va='center', fontsize=14, color=GREEN)
    fbox(ax, 3, 28, 38, 19, '本文：床面積に算入しない\n（例：天井の低い屋根裏の\n物置〈屋階〉）', col=GRAY, fc=GRAY, alpha=0.1, fs=16)
    fbox(ax, 56, 28, 41, 19, 'ただし書：当該1室の\n面積に算入する', col=GREEN, fc=GREEN, alpha=0.12, fs=18, weight='bold')
    fbox(ax, 50, 3, 49, 21, '丙建物：仕切りのない1室。中央の高さは3.75m、\n北と南の壁ぎわ0.30mだけが1.5m未満\n→ 8.00×7.50＝60.00㎡（55.20㎡は誤り）',
         col=GREEN, fs=15)
    ax.text(25, 13, '本問には当たらない', ha='center', va='center', fontsize=16, color=GRAY)
    save_fixed(fig, 'H29_dai22mon_zu11_jousoku82')


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
