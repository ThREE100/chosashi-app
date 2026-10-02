"""令和3年度 第21問（土地）会話形式note記事の解説図12枚を、座標値から作図する。

`../prompt_R3_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。

実行: python3 note-articles-Kijyutsu/R3/Q21/zu/draw_R3_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, area, chiseki, intersect  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
T1, T2 = P(500.00, 500.00), P(496.77, 531.50)
B, D, E, F = P(498.29, 524.15), P(511.93, 530.00), P(504.63, 500.56), P(518.95, 505.48)
G, I, J, K = P(497.74, 526.20), P(502.14, 509.77), P(516.61, 513.65), P(499.94, 517.99)
A = r2(radial(T1, T2, 7.37, dms(227, 43, 36)))
Aw = r2(T1 + cmath.rect(7.37, cmath.phase(T2 - T1) - dms(227, 43, 36)))    # 反時計回りに測った誤り
C = r2(G + (D - G) / abs(D - G) * abs(B - G))
Cw = r2(G + (D - G) / abs(D - G) * 3.00)                                   # 隅切長3.00で進めた誤り
H = r2(intersect(F, E, A, B)[0])
L = r2(intersect(F, D, K, K + (J - I))[0])
Lw = r2(J + (K - I))                                                        # 平行四辺形と思い込んだ誤り


def dist_line(p, a, b):
    return abs(((b - a).conjugate() * (p - a)).imag) / abs(b - a)


# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
EXPECT = {'A': (A, P(505.93, 495.62)), 'C': (C, P(499.79, 526.75)), 'H': (H, P(504.61, 500.55)),
          'L': (L, P(514.27, 521.83)), 'Aw': (Aw, P(495.08, 494.51)), 'Cw': (Cw, P(500.64, 526.98)),
          'Lw': (Lw, P(514.41, 521.87))}
for n, (got, want) in EXPECT.items():
    assert abs(got - want) < 1e-9, (n, got, want)
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'HI': (H, I, '9.55'), 'IK': (I, K, '8.51'), 'KB': (K, B, '6.38'), 'BC': (B, C, '3.00'),
         'CD': (C, D, '12.57'), 'DL': (D, L, '8.50'), 'LJ': (L, J, '8.51'), 'JF': (J, F, '8.50'),
         'FH': (F, H, '15.16'), 'IJ': (I, J, '14.98'), 'KL': (K, L, '14.84')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert d2(B, G) == '2.12' and d2(B, Cw) == '3.68' and d2(E, F) == '15.14' and d2(E, H) == '0.02'
assert f'{dist_line(H, A, F):.2f}' == '4.73' and f'{dist_line(E, A, F):.2f}' == '4.72'
assert f'{dist_line(Lw, F, D):.2f}' == '0.15' and dist_line(Aw, I, B) > 10
assert Lw.real > F.real + (D.real - F.real) * (Lw.imag - F.imag) / (D.imag - F.imag)   # 誤りのLは筆界FDの北側
HEI, OTSU, KOU = [H, I, J, F], [I, K, L, J], [B, C, D, L, K]
ZEN = [H, B, C, D, F]
AREAS = {'丙': (HEI, 135.8455, 135.84), '乙': (OTSU, 126.8422, 126.84), '甲': (KOU, 123.2128, 123.21),
         '全体': (ZEN, 385.8952, 385.89)}
for n, (pts, raw, chi) in AREAS.items():
    assert abs(area(pts) - raw) < 5e-5 and chiseki(area(pts)) == chi, (n, area(pts))
assert abs(135.84 + 126.84 + 123.21 - 385.89) < 1e-9 and abs(386.30 - 385.89 - 0.41) < 1e-9
print('数値の照合: すべて一致')


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


ALL_PROBLEMS = []
cz = centroid(ZEN)

# =====================================================================
# 図1：全体像
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像（本件土地 10番1　宅地　登記記録386.30㎡）',
                        '道路境界（H・I・K・B）と北の筆界（F・J・L・D）は、どちらも真東から15°ほど南へ傾いた線。軸に平行な辺はない。\n'
                        'E点の杭はH点から0.02mの位置（この縮尺ではH点に重なる）。A・Gは道路境界の点で、本件土地の筆界点ではない。')
z = Zu(ax)
fit(ax, [A, B, C, D, F, T1, T2, G, F + (F - H) * 0.25, F + (F - D) * 0.20, D + (D - C) * 0.35], margin=0.08, pad_aspect=True)
z.poly(HEI, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.poly(KOU, fill=ORANGE)
z.line(A, H, color=BLACK, lw=1.4)
z.line(B, G, color=GRAY, lw=1.2, ls='--')
z.line(C, G, color=GRAY, lw=1.2, ls='--')
z.line(F, F + (F - H) * 0.25, color=BLACK, lw=1.2)
z.line(F, F + (F - D) * 0.20, color=BLACK, lw=1.2)
z.line(D, D + (D - C) * 0.35, color=BLACK, lw=1.2)
z.north_arrow()
z.free_text(centroid(HEI), '丙区画\n三郎', fs=17)
z.free_text(centroid(OTSU), '乙区画\n二郎', fs=17)
z.free_text(centroid(KOU), '甲区画\n一郎', fs=17)
for p, n, kind in [(A, 'A', 'metal'), (B, 'B', 'metal'), (C, 'C', 'metal'), (D, 'D', 'metal'), (F, 'F', 'concrete'),
                   (H, 'H', 'concrete'), (I, 'I', 'concrete'), (J, 'J', 'concrete'), (K, 'K', 'concrete'),
                   (L, 'L', 'concrete')]:
    z.point(p, kind, size=9)
    z.point_label(p, n, away=cz)
z.point(G, 'dot', color=GRAY)
z.point_label(G, 'G', away=cz, color=GRAY)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=cz)
z.edge_label(F, H, '10－2', cz, fs=16, dists=(40, 55), rotate=False)
z.edge_label(J, L, '10－4', cz, fs=16, dists=(34, 46), rotate=False)
z.edge_label(I, K, '道路', cz, fs=16, dists=(40, 55), rotate=False)
z.edge_label(C, D, '道路', cz, fs=16, dists=(40, 55), rotate=False)
z.free_text(F, '10－3', fs=16, offsets=((-45, 30), (-60, 20), (-60, 40)))
ALL_PROBLEMS += save(fig, [z], 'R3_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：問1 A点（放射）
# =====================================================================
fig, (ax,) = new_figure('図2　問1　A点の求め方（T1から放射）',
                        'T1→T2の方向角 95°51′16.66″ に、時計回りの観測角 227°43′36″ を足す（323°34′52.66″）。その方向へ 7.37m 進んだ点がA。\n'
                        'A点は道路境界（L型側溝）の直線 I・K・B の延長の上に乗る。反時計回りに引くと、道路の向こう側に出てしまう。')
z = Zu(ax)
N_T2 = T1 + (T2 - T1) / abs(T2 - T1) * 9.0
fit(ax, [T1, A, Aw, H, I, I + (I - A) * 0.15, T1 + 7.5, N_T2, H + (F - H) * 0.25, I + (J - I) * 0.25], margin=0.08,
    pad_aspect=True)
z.line(H, H + (F - H) * 0.25, color=GRAY, lw=1.2)
z.line(I, I + (J - I) * 0.25, color=GRAY, lw=1.2)
z.line(A, I + (I - A) * 0.15, color=BLACK, lw=1.6)
z.line(T1, T1 + 7.5, color=GRAY, lw=1.2, ls='--')
z.free_text(T1 + 7.5, '北', color=GRAY, fs=14, offsets=((14, 8), (-14, 8), (0, 14)))
z.line(T1, N_T2, color=BLUE, lw=2.0)
z.line(T1, A, color=RED, lw=2.6)
z.line(T1, Aw, color=GRAY, lw=1.4, ls=':')
z.north_arrow()
z.angle_arc(T1, 2.6, 0, 95.855, color=BLUE)
z.angle_arc(T1, 1.6, 95.855, 323.581, color=RED)
z.point(T1, 'kijun')
z.point(A, 'metal', size=9, color=RED)
z.point(Aw, 'dot', color=GRAY)
for p, n in [(H, 'H'), (I, 'I')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=T1)
z.edge_label(T1, A, '7.37', T1 + P(0, 3), color=RED, fs=18, ts=(0.6, 0.7, 0.5), dists=(16, 24, 32))
z.callout(T1 + P(0.9, 2.45), '方向角 95°51′16.66″\n（北から時計回りにT2の方向）', dirs=(20, 0, 40), color=BLUE,
          dists=(90, 120, 150))
z.callout(T1 + P(-1.2, -0.9), '観測角 227°43′36″\n（T2の方向から時計回り）', dirs=(-20, -40, 0), color=RED,
          dists=(110, 140, 170))
z.callout(A, 'A（505.93, 495.62）', dirs=(120, 150, 90), color=RED)
z.callout(Aw, '反時計回りに測った誤り\n（495.08, 494.51）', dirs=(0, 20, -20), color=GRAY)
z.callout(T1, 'T1（500.00, 500.00）', dirs=(-100, -80, -120), color=BLACK, dists=(140, 170, 200))
z.free_text(N_T2, 'T2の方向（後視）', color=BLUE, fs=14, offsets=((0, 20), (0, -20)))
z.free_text(I + (I - A) * 0.12, '道路境界（L型側溝）', fs=14, offsets=((0, 22), (0, -22), (-40, 22)))
ALL_PROBLEMS += save(fig, [z], 'R3_dai21mon_zu02_A_housha.png')

# =====================================================================
# 図3：問1 C点（隅切り）
# =====================================================================
fig, (ax,) = new_figure('図3　問1　C点の求め方（隅切り）',
                        'GはABの延長とDCの延長の交点。隅切長（BC）は3.00、隅切剪除長（GB＝GC）はGとBの距離 2.1224…。\n'
                        'C ＝ G ＋ (D − G) ÷ Abs(D − G) × Abs(B − G)。3.00でGから進めると、BCが3.68になり隅切長と合わない。')
z = Zu(ax)
fit(ax, [B, G, Cw, K + (B - K) * 0.3, C + (D - C) * 0.18], margin=0.10, pad_aspect=True)
z.poly([B, C, G], color=GRAY, lw=0, fill=ORANGE, alpha=0.25, check=False)
z.line(K + (B - K) * 0.3, B, color=BLACK, lw=2.2)
z.line(B, C, color=BLACK, lw=2.2)
z.line(C, C + (D - C) * 0.18, color=BLACK, lw=2.2)
z.line(B, G, color=GRAY, lw=1.4, ls='--')
z.line(G, C, color=GRAY, lw=1.4, ls='--')
z.line(B, Cw, color=GRAY, lw=1.2, ls=':')
z.north_arrow()
for p, n in [(B, 'B'), (C, None), (G, 'G')]:
    z.point(p, 'metal' if n != 'G' else 'dot', size=9, color=RED if n is None else (GRAY if n == 'G' else BLACK))
    if n:
        z.point_label(p, n, away=centroid([B, C, P(503, 520)]), color=GRAY if n == 'G' else BLACK)
z.point(Cw, 'dot', color=GRAY)
z.edge_label(B, C, 'BC ＝ 3.00（隅切長）', G, fs=15, dists=(14, 20, 28))
z.edge_label(G, B, 'GB ＝ 2.12', centroid([B, C, G]), fs=15)
z.edge_label(G, C, 'GC ＝ 2.12', centroid([B, C, G]), fs=15)
z.free_text(C + (D - C) * 0.16, 'Dの方向へ', fs=14, offsets=((-45, 0), (45, 0), (-55, -15)))
z.free_text(B + (K - B) * 0.22, 'Kの方向へ', fs=14, offsets=((0, 22), (0, -22), (0, 30)))
z.callout(C, 'C（499.79, 526.75）', dirs=(170, 150, 190), color=RED, dists=(90, 120, 150))
z.callout(Cw, 'Gから3.00進めた誤り\n（500.64, 526.98）　BC ＝ 3.68', dirs=(165, 150, 135, 180), color=GRAY,
          dists=(70, 90, 110))
z.callout(G, 'G（497.74, 526.20）', dirs=(-30, -10, -60), color=GRAY, dists=(45, 60, 80))
ALL_PROBLEMS += save(fig, [z], 'R3_dai21mon_zu03_C_sumikiri.png')

# =====================================================================
# 図4：問1 H点（交点）と10番2の地積測量図による裏付け
# =====================================================================
fig, (ax1, ax2) = new_figure('図4　問1　H点の求め方（ABとFEの延長の交点）と10番2の地積測量図による裏付け',
                             '左：H ＝ F ＋ (E − F) × 446.791 ÷ 446.1384（比が1を少し超えるので、FからEを通り越した延長線上）。\n'
                             '10番2の地積測量図の FH ＝ 15.16 と、底辺AF（16.32）への高さ 4.73 が一致するのはH点。右：E点では FE ＝ 15.14・高さ 4.72 で合わない。',
                             ncols=2, width_ratios=[1.35, 1])
za = Zu(ax1, fontsize=14)
foot = A + (F - A) * (((H - A) * (F - A).conjugate()).real / abs(F - A) ** 2)
fit(ax1, [A, F, H, I, F + (F - H) * 0.12, F + (F - J) * 0.30, F + (J - F) * 0.45], margin=0.10, pad_aspect=True)
za.poly([A, F, H], color=GRAY, lw=0, fill=BLUE, alpha=0.15, check=False)
za.line(A, I, color=BLACK, lw=2.0)
za.line(F, H, color=BLACK, lw=2.0)
za.line(F, F + (F - H) * 0.12, color=BLACK, lw=1.2)
za.line(F, F + (F - J) * 0.30, color=BLACK, lw=1.2)
za.line(F, F + (J - F) * 0.45, color=BLACK, lw=2.0)
za.line(A, F, color=GRAY, lw=1.4, ls='-.')
za.line(H, foot, color=RED, lw=1.6, ls='--')
za.right_angle(foot, F, H, size=0.45)
za.north_arrow(length=0.07)
for p, n, kind in [(A, 'A', 'metal'), (F, 'F', 'concrete'), (I, 'I', 'concrete')]:
    za.point(p, kind, size=8)
    za.point_label(p, n, away=centroid([A, F, H, I]))
za.point(H, 'concrete', size=8, color=RED)
za.point_label(H, 'H', away=P(510, 505), color=RED)
za.edge_label(F, H, 'FH ＝ 15.16', A, fs=14, outward=False, ts=(0.5, 0.4, 0.6))
za.edge_label(A, F, '底辺AF（図の16.32）', H, fs=13, color=GRAY, dists=(10, 16, 22))
za.edge_label(H, foot, '高さ 4.73', A, fs=13, color=RED, ts=(0.5, 0.4, 0.6), dists=(10, 16))
za.free_text(centroid([A, F, H]) + P(0, -2.5), '10番2', fs=16, offsets=((0, 0), (-20, 10)))
za.free_text(centroid(HEI), '本件土地\n（丙区画）', fs=15, offsets=((0, 0), (20, 0)))
za.edge_label(A, I, '道路', centroid([A, F, I]), fs=14, dists=(24, 32), rotate=False)

zb = Zu(ax2, fontsize=14)
fit(ax2, [E, H, H + (H - F) * 0.003, H - (H - F) * 0.007, H + (B - A) * 0.0035, H - (B - A) * 0.0035], margin=0.10,
    pad_aspect=True)
zb.line(H + (H - F) * 0.003, H - (H - F) * 0.007, color=BLACK, lw=2.0)
zb.line(H + (B - A) * 0.0035, H - (B - A) * 0.0035, color=BLACK, lw=2.0)
zb.north_arrow(length=0.08)
zb.point(E, 'concrete', size=9, color=GRAY)
zb.point(H, 'concrete', size=9, color=RED)
zb.callout(E, 'E（504.63, 500.56）\nFE ＝ 15.14　高さ 4.72\n→ 10番2の図と合わない', dirs=(100, 130, 70), color=GRAY,
           dists=(60, 80, 100))
zb.callout(H, 'H（504.61, 500.55）\nFH ＝ 15.16　高さ 4.73\n→ 10番2の図と一致', dirs=(-80, -110, -50), color=RED,
           dists=(60, 80, 100))
zb.edge_label(E, H, 'EH ＝ 0.02', P(504.62, 500.50), fs=14, dists=(22, 30, 40), rotate=False)
zb.edge_label(H + (B - A) * 0.0015, H + (B - A) * 0.0033, '道路境界AB', T1, fs=13, dists=(12, 18))
zb.edge_label(H - (H - F) * 0.004, H - (H - F) * 0.0068, '筆界FH（FEの延長）', A, fs=13, dists=(12, 18))
ALL_PROBLEMS += save(fig, [za, zb], 'R3_dai21mon_zu04_H_kousa.png')

# =====================================================================
# 図5：問1 L点（平行線と筆界の交点）
# =====================================================================
fig, (ax1, ax2) = new_figure('図5　問1　L点の求め方（Kを通るIJの平行線と筆界FDの交点）',
                             '左：平行なのはIJとKLの1組だけ。IKとJLは平行でないので、乙区画は台形（IJ ＝ 14.98、KL ＝ 14.84）。\n'
                             'L ＝ F ＋ (D − F) × 254.7785 ÷ 382.042。右：L ＝ J ＋ (K − I)（平行四辺形の思い込み）では、筆界FDから0.15m北（10番4の側）に外れる。',
                             ncols=2, width_ratios=[1.4, 1])
za = Zu(ax1, fontsize=14)
fit(ax1, ZEN, margin=0.10, pad_aspect=True)
za.poly(ZEN, lw=1.6)
za.poly(OTSU, color=BLACK, lw=0, fill=BLUE, alpha=0.25, check=False)
za.line(I, J, color=BLACK, lw=2.2)
za.line(K, L, color=RED, lw=2.6)
za.parallel_marks(I, J, n=1)
za.parallel_marks(K, L, n=1)
za.north_arrow(length=0.07)
for p, n in [(H, 'H'), (I, 'I'), (J, 'J'), (K, 'K'), (F, 'F'), (D, 'D'), (B, 'B'), (C, 'C')]:
    za.point(p, 'dot', size=6)
    za.point_label(p, n, away=cz)
za.point(L, 'dot', size=8, color=RED)
za.edge_label(I, J, 'IJ ＝ 14.98', centroid(OTSU), fs=13, outward=False, dists=(12, 18))
za.edge_label(K, L, 'KL ＝ 14.84', centroid(OTSU), fs=13, outward=False, dists=(12, 18))
za.callout(L, 'L（514.27, 521.83）', dirs=(80, 60, 100), color=RED, dists=(50, 70, 90))
za.free_text(centroid(OTSU), '乙区画\n（台形）', fs=14, offsets=((0, 0), (0, 10)))

zb = Zu(ax2, fontsize=14)
fit(ax2, [L, Lw, F + (D - F) * 0.66, F + (D - F) * 0.675, L - (L - K) * 0.02, Lw - (Lw - K) * 0.02], margin=0.10,
    pad_aspect=True)
zb.line(F + (D - F) * 0.66, F + (D - F) * 0.675, color=BLACK, lw=2.2)
zb.line(L - (L - K) * 0.02, L, color=RED, lw=2.2)
zb.line(Lw - (Lw - K) * 0.02, Lw, color=GRAY, lw=1.6, ls=':')
zb.north_arrow(length=0.08)
zb.point(L, 'dot', size=9, color=RED)
zb.point(Lw, 'dot', size=9, color=GRAY)
zb.callout(L, 'L（514.27, 521.83）\n筆界FDの上', dirs=(-160, -140, -120, 180), color=RED, dists=(70, 90, 110))
zb.callout(Lw, '平行四辺形の誤り\n（514.41, 521.87）\n筆界から0.15m北に外れる', dirs=(180, 200, 160, 220), color=GRAY,
           dists=(60, 80, 110))
zb.edge_label(F + (D - F) * 0.669, F + (D - F) * 0.675, '筆界FD（ブロック塀）', K, fs=13, dists=(12, 18, 26))
zb.edge_label(L, L - (L - K) * 0.02, 'KL（IJと平行）', Lw, fs=13, color=RED, dists=(12, 18, 26), ts=(0.6, 0.7, 0.8))
ALL_PROBLEMS += save(fig, [za, zb], 'R3_dai21mon_zu05_L_heikousen.png')

# =====================================================================
# 図6：問2 地図と地図に準ずる図面（固定配置の説明図）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図6　問2　地図と地図に準ずる図面', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')


def box(x, y, w, h, ec, fc, lw=2.0):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.8', ec=ec, fc=fc, lw=lw))


box(3, 58, 42, 36, GRAY, '#f4f4f4')
ax.text(24, 90, '地図（法第14条第1項・第2項）', ha='center', va='center', fontsize=19, weight='bold')
ax.text(6, 80, '・登記所に備え付ける', ha='left', va='center', fontsize=17)
ax.text(6, 72, '・一筆又は二筆以上の土地ごとに作成', ha='left', va='center', fontsize=17)
ax.text(6, 64, '・各土地の区画を明確にし、地番を表示', ha='left', va='center', fontsize=17)
box(55, 58, 42, 36, RED, '#fff1f1')
ax.text(76, 90, '地図に準ずる図面（同条第4項・第5項）', ha='center', va='center', fontsize=19, weight='bold', color=RED)
ax.text(58, 80, '・地図が備え付けられるまでの間、', ha='left', va='center', fontsize=17)
ax.text(58, 75, '　（ア）登記所 に備え付ける', ha='left', va='center', fontsize=17, color=RED, weight='bold')
ax.text(58, 68, '・一筆又は二筆以上の土地の', ha='left', va='center', fontsize=17)
ax.text(58, 62, '　（イ）位置・（ウ）形状・（エ）地番 を表示', ha='left', va='center', fontsize=17, color=RED,
        weight='bold')
ax.annotate('', xy=(55, 76), xytext=(45.5, 76), arrowprops=dict(arrowstyle='<->', color=GRAY, lw=1.6))
ax.text(50, 80, '対で覚える', ha='center', va='bottom', fontsize=14, color=GRAY)
box(3, 22, 26, 20, BLACK, 'white')
ax.text(16, 36, '登記官が', ha='center', va='center', fontsize=17)
ax.text(16, 29, '新たな地図を備え付け', ha='center', va='center', fontsize=17, weight='bold')
box(37, 22, 26, 20, RED, '#fff1f1')
ax.text(50, 36, '従前の地図に準ずる図面の', ha='center', va='center', fontsize=16)
ax.text(50, 29, '全部又は一部を（オ）閉鎖', ha='center', va='center', fontsize=17, color=RED, weight='bold')
ax.text(50, 24.5, '規則第12条第1項・第4項', ha='center', va='center', fontsize=13, color=GRAY)
box(71, 22, 26, 20, RED, '#fff1f1')
ax.text(84, 36, '閉鎖した図面の保存期間', ha='center', va='center', fontsize=16)
ax.text(84, 29, '（カ）永久', ha='center', va='center', fontsize=20, color=RED, weight='bold')
ax.text(84, 24.5, '規則第28条第2号', ha='center', va='center', fontsize=13, color=GRAY)
for x0, x1 in [(29.8, 36.2), (63.8, 70.2)]:
    ax.annotate('', xy=(x1, 32), xytext=(x0, 32), arrowprops=dict(arrowstyle='-|>', color=BLACK, lw=2.2,
                                                                    mutation_scale=22))
box(40, 3, 57, 10, GRAY, '#f4f4f4', lw=1.4)
ax.text(68.5, 8, '比べる：閉鎖した地積測量図・建物図面は「閉鎖した日から30年間」（規則第28条第13号）',
        ha='center', va='center', fontsize=14, color=GRAY)
fig.text(0.5, 0.04, '本件土地の地域には法第14条第1項の地図がなく、地図に準ずる図面が備え付けられている。'
         '（イ）〜（エ）は順不同。', ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'R3_dai21mon_zu06_chizu_junzuru.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図6: 説明図（固定配置）\n  →', path)

# =====================================================================
# 図7：問3 公差の判定（数直線）
# =====================================================================
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図7　問3　地積更正が必要かの判定（精度区分 甲2）', fontsize=24, weight='bold', y=0.96)
ax = fig.add_axes([0.06, 0.30, 0.88, 0.50])
ax.set_xlim(383.6, 389.0)
ax.set_ylim(-1.6, 2.4)
ax.axis('off')
ax.plot([383.8, 388.8], [0, 0], color=BLACK, lw=2)
for v in range(384, 389):
    ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1.2)
    ax.text(v, -0.28, f'{v}', ha='center', va='top', fontsize=13, color=GRAY)
ax.axvspan(386.30 - 1.85, 386.30 + 1.85, ymin=0.30, ymax=0.52, color=GREEN, alpha=0.25)
ax.text(386.30, 0.62, '公差の範囲（386.30 ± 1.85）', ha='center', va='bottom', fontsize=15, color=GREEN)
ax.plot([386.30], [0], 'o', ms=12, color=BLUE)
ax.text(386.55, -0.75, '登記記録\n386.30㎡', ha='left', va='top', fontsize=16, color=BLUE, weight='bold')
ax.plot([385.89], [0], 'o', ms=12, color=RED)
ax.text(385.64, -0.75, '分筆後の地積の合計\n385.89㎡', ha='right', va='top', fontsize=16, color=RED, weight='bold')
ax.annotate('', xy=(385.89, 1.55), xytext=(386.30, 1.55), arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
ax.text(386.1, 1.7, '差 0.41㎡ ≦ 公差 1.85㎡　→　範囲内なので地積更正は不要', ha='center', va='bottom', fontsize=17,
        color=RED, weight='bold')
fig.text(0.5, 0.15, '市街地地域（不動産登記規則第10条第2項第1号）の誤差の限度は精度区分 甲2 まで（同条第4項第1号、第77条第5項で準用）。\n'
         '問題文の表から 386.30㎡ の甲2の公差 1.85㎡ を読む（準則第72条第1項）。→ 申請するのは土地分筆登記だけ',
         ha='center', va='center', fontsize=16)
fig.text(0.5, 0.05, '分筆後の地積　丙区画135.84㎡ ＋ 乙区画126.84㎡ ＋ 甲区画123.21㎡ ＝ 385.89㎡（宅地は小数第2位未満切捨て）',
         ha='center', va='center', fontsize=15, color=GRAY)
path = os.path.join(OUT, 'R3_dai21mon_zu07_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図7: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図8：問3 申請人（代位）の関係図（固定配置の説明図）
# =====================================================================
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図8　問3　申請人は「二郎が一郎と三郎に代位」', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
box(33, 84, 34, 11, BLACK, '#f4f4f4')
ax.text(50, 92, '被相続人　山田太郎', ha='center', va='center', fontsize=19, weight='bold')
ax.text(50, 87, '本件土地（10番1）の所有権の登記名義人　令和3年3月1日死亡', ha='center', va='center', fontsize=13)
for x in (17, 50, 83):
    ax.annotate('', xy=(x, 70), xytext=(50 if x == 50 else (40 if x < 50 else 60), 83),
                arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.6, mutation_scale=18))
ax.text(14, 80, '相続（相続人は3名のみ）', ha='center', va='center', fontsize=14, color=GRAY)
for x, name, addr, ku, role, col, fc in [
    (3, '山田一郎', 'M市D町五丁目2番2号', '甲区画 → 10番8', '被代位者', GRAY, '#f4f4f4'),
    (36, '山田二郎', 'K市D町二丁目10番1号', '乙区画 → 10番1', '申請人兼代位者', RED, '#fff1f1'),
    (69, '山田三郎', 'S市D町一丁目3番5号', '丙区画 → 10番9', '被代位者', GRAY, '#f4f4f4'),
]:
    box(x, 44, 28, 25, col, fc)
    ax.text(x + 14, 64, name, ha='center', va='center', fontsize=20, weight='bold')
    ax.text(x + 14, 58, addr, ha='center', va='center', fontsize=14)
    ax.text(x + 14, 52, f'遺産分割：{ku}', ha='center', va='center', fontsize=14)
    ax.text(x + 14, 46.5, role, ha='center', va='center', fontsize=17, weight='bold', color=col)
for x0, x1 in [(35.5, 32.0), (64.5, 68.0)]:
    ax.annotate('', xy=(x1, 56), xytext=(x0, 56), arrowprops=dict(arrowstyle='-|>', color=RED, lw=2.4,
                                                                    mutation_scale=22))
ax.text(33.8, 60, '代位', ha='center', va='bottom', fontsize=14, color=RED, weight='bold')
ax.text(66.2, 60, '代位', ha='center', va='bottom', fontsize=14, color=RED, weight='bold')
box(3, 6, 94, 30, RED, 'white', lw=1.6)
ax.text(6, 32, '申請書の申請人の欄', ha='left', va='center', fontsize=16, weight='bold', color=RED)
ax.text(10, 26, '（被相続人　山田太郎）', ha='left', va='center', fontsize=16)
ax.text(10, 20.5, '被代位者　　　　相続人　M市D町五丁目2番2号　山田一郎', ha='left', va='center', fontsize=16)
ax.text(10, 16, '　　　　　　　　　　　　S市D町一丁目3番5号　山田三郎', ha='left', va='center', fontsize=16)
ax.text(10, 11.5, '申請人兼代位者　　　　K市D町二丁目10番1号　山田二郎', ha='left', va='center', fontsize=16)
ax.text(10, 7.5, '代位原因　令和3年8月1日遺産分割の所有権移転登記請求権', ha='left', va='center', fontsize=16)
fig.text(0.5, 0.045, '分筆の申請人は登記名義人（法第39条第1項）→ 死亡したので相続人（法第30条）。二郎1人で申請するので一郎・三郎の分は代位。\n'
         '申請情報に代位者である旨・被代位者の氏名住所・代位原因（令第3条第4号）。添付：相続証明書（令第7条第1項第4号）・代位原因証書（同項第3号）',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R3_dai21mon_zu08_dai_kankei.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図8: 説明図（固定配置）\n  →', path)

# =====================================================================
# 図9：問3 分筆後の区画と地番
# =====================================================================
fig, (ax,) = new_figure('図9　問3　分筆後の区画と地番（10番1 → 10番1・10番8・10番9）',
                        '予定地番：乙区画が10番1のまま（イ）、甲区画が10番8（ロ）、丙区画が10番9（ハ）。\n'
                        '分筆元の登記原因は「③10番1、10番8、10番9に分筆」、10番8・10番9は「10番1から分筆」。登録免許税は分筆後の3個で金3,000円。')
z = Zu(ax)
fit(ax, ZEN, margin=0.12, pad_aspect=True)
z.poly(HEI, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.poly(KOU, fill=ORANGE)
z.north_arrow()
z.free_text(centroid(HEI), '（ハ）10番9\n135.84㎡\n三郎', fs=17)
z.free_text(centroid(OTSU), '（イ）10番1\n126.84㎡\n二郎', fs=17)
z.free_text(centroid(KOU), '（ロ）10番8\n123.21㎡\n一郎', fs=17)
for p, n in [(H, 'H'), (I, 'I'), (J, 'J'), (K, 'K'), (L, 'L'), (F, 'F'), (D, 'D'), (B, 'B'), (C, 'C')]:
    z.point(p, 'dot', size=6)
    z.point_label(p, n, away=cz)
ALL_PROBLEMS += save(fig, [z], 'R3_dai21mon_zu09_bunpitsu_chiban.png')

# =====================================================================
# 図10：問4 問題文の注の仕分けと作図の範囲（固定配置の整理図。2026-10-02追加。予備校の解説と見比べて記事に足した観点用）
# =====================================================================
PTS_ALL = [T1, T2, B, C, D, F, H, I, J, K, L]   # 地積測量図に描く点（A・G・Eは描かない）
ew = max(p.imag for p in PTS_ALL) - min(p.imag for p in PTS_ALL)
ns = max(p.real for p in PTS_ALL) - min(p.real for p in PTS_ALL)
assert round(ew * 4) == 126 and round(ns * 4) == 89, (ew, ns)
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図10　問4　問題文の注の仕分けと地積測量図の作図の範囲', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
box(3, 50, 44, 44, GRAY, '#f4f4f4')
ax.text(25, 90, '毎年ほとんど同じ注', ha='center', va='center', fontsize=20, weight='bold', color=GRAY)
for k, t in enumerate(['問題文の注1　行為・書類はすべて適法', '問題文の注2　書面申請', '問題文の注3　座標は小数第3位を四捨五入',
                       '問題文の注4　縮尺は250分の1、辺長は\n　　　　　　　小数第3位を四捨五入', '問題文の注7　字画を明確に（訂正・加入・削除）']):
    ax.text(6, 81 - k * 7.2, t, ha='left', va='center', fontsize=16, linespacing=1.3)
box(53, 50, 44, 44, RED, '#fff1f1')
ax.text(75, 90, '今年だけの注（ここに印を付ける）', ha='center', va='center', fontsize=20, weight='bold', color=RED)
ax.text(56, 78, '問題文の注5　地積測量図に書かないもの', ha='left', va='center', fontsize=16, weight='bold')
ax.text(56, 71.5, '・各筆界点の座標値　・平面直角座標系の番号\n・地積とその求積方法　・測量年月日', ha='left', va='center',
        fontsize=16, linespacing=1.5)
ax.text(56, 61, '問題文の注6　K市基準点（T1・T2）', ha='left', va='center', fontsize=16, weight='bold')
ax.text(56, 55.5, '・位置と点名だけ書く（座標値は書かない）', ha='left', va='center', fontsize=16)
box(3, 6, 94, 34, BLUE, '#eef4fb')
ax.text(50, 36, '作図の範囲（T1・T2まで入れて描く）', ha='center', va='center', fontsize=20, weight='bold', color=BLUE)
ax.text(8, 27, f'東西：T1（Y 500.00）〜 T2（Y 531.50）　約{ew:.0f}m　→　1/250（1m ＝ 4mm）で約126mm', ha='left', va='center', fontsize=17)
ax.text(8, 19, f'南北：T2（X 496.77）〜 F（X 518.95）　約{ns:.0f}m　→　1/250で約89mm', ha='left', va='center', fontsize=17)
ax.text(8, 11, '答案用紙の第4欄の枠（横約30cm・縦約23cm）に収まるので、基準点を省略せずに描ける', ha='left', va='center', fontsize=17)
fig.text(0.5, 0.045, '問題文の注のうち、今年だけの注（問題文の注5・問題文の注6）が「書く・書かない」を決める。調査図素図の注（点の条件）や\n'
         '観測値の表の下の注（観測角は時計回り）とは別の番号なので、「問題文の注5」のように出どころを付けて読む。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R3_dai21mon_zu10_chuu_shiwake.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図10: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図11：問4 地積測量図の完成見本
# =====================================================================
fig, (ax,) = new_figure('図11　問4　地積測量図（10番1・10番8・10番9）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm。辺長は小数第3位を四捨五入（DL・JF は 8.4984… なので 8.50）。\n'
                        '座標値・地積・求積方法・測量年月日は書かない（問題文の注5）。基準点T1・T2は位置と点名だけ（問題文の注6）。A・G・Eは描かない。\n'
                        '答案用紙の第4欄：地番・土地の所在を記入。作成者・申請人は「（略）」、縮尺1/250は印刷済み。方位記号は自分で描く（印刷なし）。')
z = Zu(ax)
fit(ax, ZEN + [T1, T2, F + (F - H) * 0.20, F + (F - D) * 0.15, H + (H - B) * 0.12, D + (D - C) * 0.25], margin=0.08,
    pad_aspect=True)
z.poly(ZEN, lw=2.0)
z.line(I, J, lw=2.0)
z.line(K, L, lw=2.0)
z.line(F, F + (F - H) * 0.20, color=BLACK, lw=1.2)
z.line(F, F + (F - D) * 0.15, color=BLACK, lw=1.2)
z.line(H, H + (H - B) * 0.12, color=BLACK, lw=1.2)
z.line(D, D + (D - C) * 0.25, color=BLACK, lw=1.2)
z.north_arrow()
for n, (p, q, s) in SIDES.items():
    if n == 'IJ':
        z.edge_label(p, q, s, centroid(HEI), fs=15, outward=True)
    elif n == 'KL':
        z.edge_label(p, q, s, centroid(OTSU), fs=15, outward=True)
    else:
        z.edge_label(p, q, s, cz, fs=15)
z.free_text(centroid(HEI), '（ハ）\n10－9', fs=17)
z.free_text(centroid(OTSU), '（イ）\n10－1', fs=17)
z.free_text(centroid(KOU), '（ロ）\n10－8', fs=17)
for p, n in [(F, 'F'), (H, 'H'), (I, 'I'), (J, 'J'), (K, 'K'), (L, 'L')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=cz)
for p, n in [(B, 'B'), (C, 'C'), (D, 'D')]:
    z.point(p, 'metal', size=9)
    z.point_label(p, n, away=cz)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=cz)
z.edge_label(F, H, '10－2', cz, fs=16, dists=(45, 58), rotate=False)
z.edge_label(J, L, '10－4', cz, fs=16, dists=(40, 52), rotate=False)
z.edge_label(I, K, '道路', cz, fs=16, dists=(45, 58), rotate=False)
z.edge_label(C, D, '道路', cz, fs=16, dists=(45, 58), rotate=False)
z.free_text(F, '10－3', fs=16, offsets=((-45, 30), (-60, 20), (-60, 40)))
z.free_text(P(498.3, 496.0), '（単位：ｍ）\n◎ コンクリート杭：F・H・I・J・K・L\n● 金属標：B・C・D\n△ 基準点：T1・T2', fs=13,
            ha='left', va='top', offsets=((0, 0), (20, 0), (0, -20), (40, -20)))
ALL_PROBLEMS += save(fig, [z], 'R3_dai21mon_zu11_chiseki_sokuryouzu.png')

# =====================================================================
# 図12：本番の解く順番（固定配置の流れ図）
# =====================================================================
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図12　本番の解く順番（時間を食う計算を後ろへ）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
STEPS = [
    ('1', '問2の穴埋め', '条文の知識だけ（登記所・位置・形状・地番・閉鎖・永久）', GRAY, '#f4f4f4'),
    ('2', '申請書の計算の要らない欄', '登記の目的・添付書類・登録免許税・申請人の欄（代位）・所在・地番・地目・\n登記原因・分筆前の行の386.30', GRAY, '#f4f4f4'),
    ('3', 'A点 → H点', '放射（時計回り）と交点の比。FH 15.16・高さ 4.73 で検算　［時間を食う］', RED, '#fff1f1'),
    ('4', 'C点', '隅切り（GB＝GC＝2.1224…、BC＝3.00で検算）', GRAY, '#f4f4f4'),
    ('5', 'L点 → 3区画の面積 → 公差', '交点の比 → 135.84・126.84・123.21 → 差0.41 ≦ 1.85 → 地積の欄　［時間を食う］', RED, '#fff1f1'),
    ('6', '地積測量図', '辺長11本・境界標・T1とT2（1/250で約126mm×約89mm）', GRAY, '#f4f4f4'),
]
y = 92
for num, head, body, ec, fc in STEPS:
    box(4, y - 11, 92, 11, ec, fc, lw=2.0)
    ax.text(8, y - 5.5, num, ha='center', va='center', fontsize=26, weight='bold', color=ec)
    ax.text(12, y - 3.3, head, ha='left', va='center', fontsize=19, weight='bold')
    ax.text(12, y - 8.0, body, ha='left', va='center', fontsize=14, linespacing=1.3)
    if num != '6':
        ax.annotate('', xy=(50, y - 13.5), xytext=(50, y - 11.6),
                    arrowprops=dict(arrowstyle='-|>', color=BLACK, lw=1.8, mutation_scale=16))
    y -= 15.2
fig.text(0.5, 0.045, 'A点は本件土地の筆界点ではなく、H点を出すためだけに使う点。L点が出なくても、申請書は3つの地積以外を全部書ける\n'
         '（丙区画の地積はH点があれば出せる）。代位の申請人の欄を先に書いておけば、計算で詰まっても点が残る。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R3_dai21mon_zu12_kaku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図12: 流れ図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
