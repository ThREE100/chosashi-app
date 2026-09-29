"""平成28年度 第21問（土地）会話形式note記事の解説図8枚を、座標値から作図する。

`../prompt_H28_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../R6/Q21/zu/draw_R6_dai21mon_kaisetsuzu.py`。

C点は問題文に座標がない（戊土地の北東の角）。戊土地を描く図だけ、調査素図の形に合わせた模式の位置
C_MOSHIKI に置き、図の中で「位置は模式」と明記する（計算には一切使わない）。

実行: python3 note-articles-Kijyutsu/H28/Q21/zu/draw_H28_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, dms, to_dms, area, chiseki, intersect  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値、地積測量図の抜粋の座標値、記事で求めた点） ------------------
A101, A102 = P(325.32, 272.32), P(333.27, 301.99)
A, B = P(348.50, 265.15), P(352.91, 284.25)                 # 32番1の地積測量図のK5・K4
K1, K2, K3 = P(366.00, 262.58), P(366.80, 266.81), P(369.86, 283.49)
G, F, E, H = P(350.47, 284.32), P(350.40, 293.88), P(334.85, 303.80), P(333.88, 280.15)   # 40番1の①②③④
I = P(332.29, 268.34)
D = r2(A102 + cmath.rect(5.18, cmath.phase(A101 - A102) + dms(168, 9, 0) - dms(0, 1, 0)))
J = r2(intersect(A, I, G, G + (B - A))[0])
JW = r2(A + (G - B))                                         # 平行四辺形と思い込んだ誤りの点
C_MOSHIKI = P(357.00, 300.00)                                # C点（座標なし。模式の位置）

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('D', D, P(335.61, 306.61)), ('J', J, P(346.15, 265.61)), ('JW', JW, P(346.06, 265.22))]:
    assert abs(got - want) < 1e-9, (n, got, want)
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'AB': (A, B, '19.60'), 'BG': (B, G, '2.44'), 'GH': (G, H, '17.11'), 'HI': (H, I, '11.92'),
         'IJ': (I, J, '14.13'), 'JA': (J, A, '2.39')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert d2(J, G) == '19.20'
TEI = [A, B, G, H, I]                   # 丁土地（40番2）
TEI6 = [A, B, G, H, I, J]
I_40_2 = [J, G, H, I]                   # （イ）40番2
RO = [A, B, G, J]                       # （ロ）部分
N32_1 = [K1, K2, K3, B, A]              # 乙土地（32番1）
N32_1_GO = [K1, K2, K3, B, G, J, A]     # 合筆後の32番1
N40_1 = [G, F, E, H]                    # 丙土地（40番1）
NI = [B, C_MOSHIKI, F, G]               # 戊土地（ニ）部分（模式）
HA = [C_MOSHIKI, D, E, F]               # 戊土地（ハ）部分（模式）
assert f'{area(TEI):.5f}' == '276.62015' and chiseki(area(TEI), False) == 276
assert f'{area(I_40_2):.4f}' == '230.2059' and chiseki(area(I_40_2), False) == 230
assert f'{area(RO):.4f}' == '46.4342' and chiseki(area(RO), False) == 46
assert f'{area(N32_1):.5f}' == '351.67100' and f'{area(N32_1_GO):.4f}' == '398.1052'
assert chiseki(area(N32_1_GO), False) == 398
assert f'{area(N40_1):.4f}' == '268.1361'
BRG_A101 = math.degrees(cmath.phase(A101 - A102)) + 360       # A102→A101の方向角 255°00′00.34″
assert to_dms(math.radians(BRG_A101)) == '255°00′00.34″'
BRG_D = BRG_A101 + 168 + 8 / 60                                # A101の方向から時計回りに168°08′00″
# 誤りの点の向き：JWは直線AIより西（Yが小さい）＝41番の側
t_w = (JW.real - A.real) / (I.real - A.real)
assert JW.imag < (A + (I - A) * t_w).imag
assert f'{(A + (I - A) * t_w).imag:.2f}' == '265.63'
off = abs(((JW - A) * ((I - A) / abs(I - A)).conjugate()).imag)
assert f'{off:.1f}' == '0.4'
# DはEの北東（0.76m北、2.81m東）
assert f'{(D - E).real:.2f}' == '0.76' and f'{(D - E).imag:.2f}' == '2.81'
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

# =====================================================================
# 図1：全体像（北を上にして座標どおりに描き直した調査素図）
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像',
                        '32番1のK5＝A・K4＝B、40番1の①＝G・②＝F・③＝E・④＝H（どれもA市基準点と同じ座標）。\n'
                        'J点はGを通るABの平行線と直線AIの交点。C点は問題文に座標がないため、戊土地の形は模式（灰色の破線）。')
z = Zu(ax)
fit(ax, [K1, K3, A101, A102, D, C_MOSHIKI, I], margin=0.06, pad_aspect=True)
z.poly(N32_1, fill=BLUE)
z.poly(N40_1, fill=ORANGE)
z.poly(TEI, fill=GREEN)
z.line(J, G, color=RED, lw=2.0, ls='--')
z.poly(NI, color=GRAY, lw=1.4, ls='--', fill=GRAY, alpha=0.12)
z.poly(HA, color=GRAY, lw=1.4, ls='--', fill=GRAY, alpha=0.12)
z.line(B, G, color=BLACK, lw=2.0)
z.line(F, E, color=BLACK, lw=2.0)
z.north_arrow()
z.free_text(centroid(N32_1), '乙土地\n32番1　畑\n351㎡', fs=15)
z.free_text(centroid(N40_1), '丙土地\n40番1　雑種地\n268㎡', fs=14)
z.free_text(centroid(I_40_2), '丁土地\n40番2　畑\n276㎡\n（イ）', fs=15)
z.callout(centroid(RO), '（ロ）', dirs=(-170, 180, -160), color=RED, dists=(150, 175, 200))
z.free_text(centroid(NI), '（ニ）', fs=15, offsets=((0, 0), (0, 12), (0, -12)))
z.free_text(centroid(HA), '（ハ）', fs=15, offsets=((0, 0), (0, 12), (0, -12)))
z.callout(C_MOSHIKI, 'C（座標なし。位置は模式）', dirs=(60, 40, 80), color=GRAY, dists=(55, 75, 95))
z.callout(centroid(HA) + P(-4, 0), '戊土地（無番地）', dirs=(-10, 10, -30), color=GRAY, dists=(150, 180, 210))
for p, n, ref in [(A, 'A', centroid(TEI)), (B, 'B', centroid(TEI)), (G, 'G', centroid(TEI)), (H, 'H', centroid(TEI)),
                  (I, 'I', centroid(TEI)), (J, 'J', centroid(TEI)), (F, 'F', centroid(N40_1)), (E, 'E', centroid(N40_1)),
                  (D, 'D', centroid(HA))]:
    z.point(p, 'metal' if n in 'HI' else 'concrete', color=RED if n in 'DJ' else BLACK)
    z.point_label(p, n, away=ref, color=RED if n in 'DJ' else BLACK)
for p, n in [(K1, 'K1'), (K2, 'K2'), (K3, 'K3')]:
    z.point(p, 'dot', size=5, color=GRAY)
    z.point_label(p, n, away=centroid(N32_1), color=GRAY, fs=12)
for p, n in [(A101, 'A101'), (A102, 'A102')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=centroid(N40_1))
z.free_text(P(362.5, 293.0), '31－2（甲土地）\n畑　271㎡', fs=13, color=GRAY, offsets=((0, 0), (0, 20), (20, 0)))
z.free_text(P(349.0, 308.0), '31－1\n居宅', fs=13, color=GRAY, offsets=((0, 0), (20, 0), (0, 20)))
z.free_text(P(330.5, 309.0), '30', fs=14, color=GRAY, offsets=((0, 0), (15, 0), (0, -15)))
z.edge_label(I, J, '41', centroid(TEI), fs=14, color=GRAY, dists=(28, 38), rotate=False)
z.edge_label(K1, A, '34', centroid(N32_1), fs=14, color=GRAY, dists=(28, 38), rotate=False, ts=(0.8, 0.9, 0.7))
z.edge_label(H, I, '道路', centroid(TEI), fs=15, color=GRAY, dists=(26, 36), rotate=False)
ALL_PROBLEMS += save(fig, [z], 'H28_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：問1 D点（A102から放射。後視A101の読み0°01′00″を引く）
# =====================================================================
fig, (ax1, ax2) = new_figure('図2　問1　D点の求め方（A102から放射）',
                             'A102→A101の方向角 255°00′00.34″（電卓の表示は −104°59′59.66″）。A101の読みが0°01′00″なので、\n'
                             'A101の方向から時計回りの観測角は 168°09′00″ − 0°01′00″ ＝ 168°08′00″。これを足して5.18m進む（方向角63°08′）。\n'
                             '引き忘れても5.18m先で約1.5mmのずれで、丸めると同じ座標になるのは偶然。',
                             ncols=2, width_ratios=[0.85, 1.15])
za = Zu(ax1, fontsize=14)
fit(ax1, [A101, A102, D, E, H, G], margin=0.08, pad_aspect=True)
za.poly(N40_1, color=GRAY, lw=1.1)
za.poly(TEI, color=GRAY, lw=1.1)
za.line(A102, A101, color=BLUE, lw=2.0)
za.line(A102, D, color=RED, lw=2.6)
za.north_arrow(length=0.07)
for p, kind in [(A101, 'kijun'), (A102, 'kijun'), (E, 'concrete'), (H, 'metal'), (G, 'concrete')]:
    za.point(p, kind)
za.point(D, 'concrete', color=RED)
for p, n in [(E, 'E'), (H, 'H'), (G, 'G')]:
    za.point_label(p, n, away=centroid(N40_1))
za.edge_label(A102, A101, '後視（A101の方向）', A102 + P(5, 0), color=BLUE, fs=14, ts=(0.5, 0.6, 0.4), dists=(14, 20))
za.callout(D, 'D（335.61, 306.61）', dirs=(150, 165, 135), color=RED, dists=(110, 140, 170))
za.callout(A102, 'A102（333.27, 301.99）', dirs=(-110, -125, -95), color=BLACK, dists=(60, 80, 100))
za.callout(A101, 'A101（325.32, 272.32）', dirs=(-60, -45, -75), color=BLACK, dists=(50, 70, 90))
ax1.set_title('全体', fontsize=17, weight='bold', pad=6)

zb = Zu(ax2, fontsize=14)
lo, hi = A102 + P(-4.2, -4.6), A102 + P(5.2, 7.6)
fit(ax2, [lo, hi], margin=0.0, pad_aspect=True)
zb.line(E, D, color=GRAY, lw=1.2)
zb.line(E, E + (F - E) * 0.25, color=GRAY, lw=1.2)
zb.line(E, E + (H - E) * 0.2, color=GRAY, lw=1.2)
zb.line(D, D + (C_MOSHIKI - D) * 0.25, color=GRAY, lw=1.0, ls='--')
zb.line(A102, A102 + 3.4, color=GRAY, lw=1.2, ls='--')
zb.free_text(A102 + 3.4, '北', color=GRAY, fs=14, offsets=((-14, 8), (14, 8), (0, 14)))
BK = A102 + (A101 - A102) / abs(A101 - A102) * 4.0
zb.line(A102, BK, color=BLUE, lw=2.0)
zb.line(A102, D, color=RED, lw=2.6)
zb.north_arrow(length=0.07)
zb.angle_arc(A102, 1.4, 0, BRG_A101, color=BLUE)
zb.angle_arc(A102, 2.5, BRG_A101, BRG_D, color=RED)
zb.point(A102, 'kijun')
zb.point(E, 'concrete')
zb.point(D, 'concrete', color=RED)
zb.point_label(E, 'E', away=A102 + P(3, -3))
zb.edge_label(A102, D, '5.18', A102 + P(3, -3), color=RED, fs=17, ts=(0.72, 0.8, 0.64), dists=(14, 20, 26))
zb.edge_label(A102, BK, '後視（A101へ）', A102 + P(3, 0), color=BLUE, fs=14, ts=(0.72, 0.62, 0.8), dists=(14, 20))
zb.callout(A102 + P(-1.4, 0), '方向角 255°00′00.34″\n（北から時計回りにA101の方向）', dirs=(-90, -75, -105),
           color=BLUE, dists=(40, 60, 80))
zb.callout(A102 + P(2.5, 0), '観測角 168°09′00″ − 0°01′00″ ＝ 168°08′00″\n（A101の方向から時計回り）', dirs=(90, 75, 105),
           color=RED, dists=(90, 120, 150))
zb.callout(D, 'D（335.61, 306.61）', dirs=(-60, -80, -45), color=RED, dists=(60, 80, 100))
zb.free_text(E + P(1.6, 1.3), '（ハ）', fs=14, color=GRAY, offsets=((0, 0), (10, 10), (-10, 10)))
ax2.set_title('A102のまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H28_dai21mon_zu02_D_housha.png')

# =====================================================================
# 図3：問1 J点（Gを通るABの平行線と直線AIの交点）
# =====================================================================
fig, (ax1, ax2) = new_figure('図3　問1　J点の求め方（ABの平行線と直線AIの交点）',
                             'J ＝ A ＋ (I − A) × t、t ＝ 46.9127 ÷ 323.6789（Conjgの積のiの係数の比）。平行なのはABとJGの1組だけで、A・B・G・Jは台形。\n'
                             '平行四辺形と思い込んで J ＝ A ＋ (G − B) とすると（346.06, 265.22）。直線AIより約0.4m西の41番に出る。\n'
                             '検算：△AJIは約0.02㎡（一直線）、Conjg(B − A) × (G − J) の虚部は −0.0009（平行）。',
                             ncols=2, width_ratios=[1.35, 1])
za = Zu(ax1)
fit(ax1, TEI + [A + P(0, -7), B + P(1.5, 0)], margin=0.08, pad_aspect=True)
za.poly(TEI, fill=GREEN, alpha=0.12)
za.line(J, G, color=RED, lw=2.6)
za.line(A, I, color=BLACK, lw=2.0)
za.parallel_chevron(A, B, color=BLACK, size=0.9)
za.parallel_chevron(J, G, color=RED, size=0.9)
za.north_arrow()
for p, n in [(A, 'A'), (B, 'B'), (G, 'G'), (H, 'H'), (I, 'I')]:
    za.point(p, 'metal' if n in 'HI' else 'concrete')
    za.point_label(p, n, away=centroid(TEI))
za.point(J, 'dot', color=RED, size=9)
za.callout(J, 'J（346.15, 265.61）', dirs=(-150, -170, -130, 180), color=RED, dists=(60, 80, 100))
za.edge_label(A, B, 'AB', centroid(TEI), fs=15, ts=(0.3, 0.72, 0.2), dists=(14, 20))
za.edge_label(J, G, 'Gを通るABの平行線', centroid(I_40_2), color=RED, fs=14, outward=False, ts=(0.3, 0.24, 0.76),
              dists=(16, 22))
za.edge_label(A, I, '直線AI（筆界）', centroid(TEI), fs=14, ts=(0.62, 0.72, 0.52), dists=(16, 24))
za.free_text(centroid(I_40_2), '丁土地（40番2）', fs=16, offsets=((0, -20), (0, 0), (0, -40)))
za.edge_label(I, J, '41', centroid(TEI), fs=15, color=GRAY, dists=(40, 50), rotate=False, ts=(0.4, 0.3, 0.5))

zb = Zu(ax2)
lo, hi = J + P(-0.75, -0.75), J + P(0.75, 0.75)
ax2.set_xlim(lo.imag, hi.imag)
ax2.set_ylim(lo.real, hi.real)
tl, th = (hi.real - A.real) / (I.real - A.real), (lo.real - A.real) / (I.real - A.real)
zb.line(A + (I - A) * tl, A + (I - A) * th, color=BLACK, lw=2.4)
g_hi = J + (G - J) / abs(G - J) * 0.72
zb.line(J, g_hi, color=RED, lw=2.6)
zb.line(JW, JW + (G - JW) / abs(G - JW) * 0.72, color=GRAY, lw=1.6, ls='--')
zb.north_arrow()
zb.point(J, 'dot', color=RED, size=11)
zb.point(JW, 'dot', color=GRAY, size=10)
foot = A + (I - A) * (((JW - A) * (I - A).conjugate()).real / abs(I - A) ** 2)
zb.line(JW, foot, color=GRAY, lw=1.4, check=False)
zb.callout(J, 'J（346.15, 265.61）', dirs=(60, 40, 80), color=RED, dists=(55, 75))
zb.callout(JW, '平行四辺形の誤り\n（346.06, 265.22）', dirs=(-100, -120, -80), color=GRAY, dists=(50, 70, 90))
zb.edge_label(JW, foot, '約0.4', JW + P(0.3, 0), color=GRAY, fs=15, dists=(12, 18), rotate=False)
zb.free_text(J + P(0.45, -0.55), '41番', fs=18, color=GRAY, offsets=((0, 0), (0, -12), (12, 0)))
zb.free_text(J + P(-0.45, 0.45), '丁土地', fs=18, color=GREEN, offsets=((0, 0), (0, 12), (-12, 0)))
zb.edge_label(A + (I - A) * tl, A + (I - A) * th, '直線AI', J + P(0, 1), fs=14, ts=(0.2, 0.15, 0.25), dists=(14, 20))
ax2.set_title('Jのまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H28_dai21mon_zu03_J_kousa.png')

# =====================================================================
# 図4：問3の準備 筆界点の裏付けと（イ）（ロ）の面積
# =====================================================================
fig, (ax,) = new_figure('図4　問3の準備　丁土地の筆界点の裏付けと（イ）（ロ）の面積',
                        'AB 19.60 は32番1の地積測量図のK4K5（19m60）、GH 17.11 は40番1の地積測量図の①④（17m11）と一致。\n'
                        '丁土地 A→B→G→H→I は 276.62015 → 276㎡（畑は1㎡未満切捨て）で登記記録の276㎡と一致。\n'
                        '（イ）230.2059 → 230㎡、（ロ）46.4342 → 46㎡。四角形は Conjg(対角線) × (もう一方の対角線) のiの係数が倍面積。')
z = Zu(ax)
fit(ax, TEI + [F, B + P(6, 0)], margin=0.08, pad_aspect=True)
z.poly(N32_1, color=GRAY, lw=1.2, fill=BLUE, alpha=0.10)
z.poly(N40_1, color=GRAY, lw=1.2, fill=ORANGE, alpha=0.10)
z.poly(I_40_2, fill=GREEN, alpha=0.25)
z.poly(RO, fill=RED, alpha=0.25)
z.line(J, H, color=GRAY, lw=1.0, ls=':')
z.line(G, I, color=GRAY, lw=1.0, ls=':')
z.north_arrow()
for p, n in [(A, 'A'), (B, 'B'), (G, 'G'), (H, 'H'), (I, 'I'), (J, 'J')]:
    z.point(p, 'metal' if n in 'HI' else 'concrete')
    z.point_label(p, n, away=centroid(TEI))
z.edge_label(A, B, 'AB ＝ 19.60（32番1の図のK4K5 19m60）', centroid(TEI), fs=14, dists=(16, 24), ts=(0.5, 0.45, 0.55))
z.edge_label(G, H, 'GH ＝ 17.11（40番1の図の①④ 17m11）', centroid(TEI), fs=14, outward=False, dists=(16, 24),
             ts=(0.45, 0.5, 0.4))
z.free_text(centroid(I_40_2), '（イ）\n230.2059 → 230㎡', fs=17,
            offsets=((0, -80), (0, -95), (0, 70), (-20, -80), (20, -80)))
z.callout(centroid(RO) + (B - A) * 0.3, '（ロ）46.4342 → 46㎡', dirs=(60, 45, 75), color=RED, dists=(70, 95, 120))
z.free_text(centroid(N32_1), '32番1（乙土地）', fs=15, color=GRAY, offsets=((0, 0), (0, 20)))
z.free_text(centroid(N40_1), '40番1（丙土地）', fs=15, color=GRAY, offsets=((0, 0), (0, 20)))
ALL_PROBLEMS += save(fig, [z], 'H28_dai21mon_zu04_menseki.png')

# =====================================================================
# 図5：問2 戊土地は地目の違う2筆
# =====================================================================
fig, (ax,) = new_figure('図5　問2　戊土地は地目が違う2筆の土地（土地表題登記）',
                        '（ハ）部分は31番1の居宅の附属建物（物置）の敷地で宅地。（ニ）部分は農園の受付所・農具置場で、主な目的は農園なので畑。\n'
                        '小屋は永続性がなく建物ではない。丙土地の登記記録は雑種地だが、地目は現況と利用目的で決める。一筆の土地に地目は一つなので2筆。\n'
                        'C点は問題文に座標がないため、B→C・C→D・C→Fの線は模式（破線）。')
z = Zu(ax)
fit(ax, [B, C_MOSHIKI + P(2, 0), D, E, H, G, A102], margin=0.08, pad_aspect=True)
z.poly(N40_1, fill=ORANGE, alpha=0.18, color=BLACK)
z.poly(NI, fill=GREEN, alpha=0.30, color=BLACK, lw=2.0)
z.poly(HA, fill=PURPLE, alpha=0.28, color=BLACK, lw=2.0)
for p, q in [(B, C_MOSHIKI), (C_MOSHIKI, D), (C_MOSHIKI, F)]:
    z.line(p, q, color='white', lw=2.4, check=False)
    z.line(p, q, color=GRAY, lw=2.0, ls='--')
z.north_arrow()
for p, n in [(B, 'B'), (G, 'G'), (F, 'F'), (E, 'E'), (D, 'D'), (H, 'H')]:
    z.point(p, 'metal' if n == 'H' else 'concrete')
    z.point_label(p, n, away=centroid(NI) if n in 'BG' else centroid(HA) if n in 'DE' else centroid(N40_1))
z.point(C_MOSHIKI, 'dot', size=6, color=GRAY)
z.callout(C_MOSHIKI, 'C（位置は模式）', dirs=(60, 30, 90), color=GRAY, dists=(45, 65))
z.callout(centroid(NI), '（ニ）部分：畑\n農園の受付所・農具置場\n取得原因：時効取得', dirs=(150, 165, 135), color=GREEN,
          dists=(90, 120, 150))
z.callout(centroid(HA), '（ハ）部分：宅地\n31番1の居宅の附属建物（物置）\n取得原因：売払い', dirs=(-20, 0, -40), color=PURPLE,
          dists=(110, 140, 170))
z.free_text(centroid(N40_1), '丙土地（40番1）\n登記記録は雑種地', fs=15, offsets=((0, 0), (0, 20), (0, -20)))
z.free_text(P(349.5, 306.5), '31番1（宅地）\n居宅', fs=14, color=GRAY, offsets=((0, 0), (15, 15), (15, -15)))
z.free_text(P(358.5, 292.0), '31番2（甲土地）', fs=14, color=GRAY, offsets=((0, 0), (0, 15), (-20, 15), (20, 15)))
z.free_text(P(346.5, 280.5), '40番2（丁土地）', fs=14, color=GRAY, offsets=((0, 0), (-15, 0), (0, -15)))
ALL_PROBLEMS += save(fig, [z], 'H28_dai21mon_zu05_bo_tochi_2hitsu.png')

# =====================================================================
# 図6：問2 取得原因と登記原因（整理図。固定配置）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図6　問2　取得原因は違っても、登記原因は同じ「不詳」', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
COLS = [(4, '（ニ）部分', GREEN, ['地目：畑', '取得原因：時効取得', '登記原因及びその日付：不詳']),
        (52, '（ハ）部分', PURPLE, ['地目：宅地', '取得原因：売払い', '登記原因及びその日付：不詳'])]
for x, head, col, lines in COLS:
    ax.add_patch(FancyBboxPatch((x, 58), 44, 30, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=col, lw=2.2))
    ax.text(x + 2, 84, head, fontsize=21, weight='bold', va='center', color=col)
    for i, s in enumerate(lines):
        ax.text(x + 4, 76 - i * 7, s, fontsize=18, va='center', color=RED if i == 2 else BLACK)
ax.text(50, 53.5, '地目が違う → 2筆の土地表題登記', fontsize=19, ha='center', va='center', weight='bold')
BOXES = [
    (27, '取得原因（時効取得・売払い）はどこに出る？',
     ['甲野太郎が所有権を取得した原因。登記原因ではない',
      '→ 所有権を有することを証する情報（不動産登記令別表4の項添付情報欄ハ）で示す'], []),
    (4, '一の申請情報で申請できるか（不動産登記令第4条ただし書）',
     ['表題登記の登記原因は「土地が生じた原因とその日付」。元から無番地の土地は2筆とも「不詳」',
      '同一の登記所の管轄・登記の目的（土地表題登記）・登記原因及びその日付が同一 → 一の申請情報でできる'], [1]),
]
for y, head, lines, red in BOXES:
    ax.add_patch(FancyBboxPatch((3, y), 94, 18, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=BLACK, lw=1.4))
    ax.text(5, y + 15, head, fontsize=19, weight='bold', va='center')
    for i, s in enumerate(lines):
        ax.text(7, y + 9.5 - i * 5.5, s, fontsize=16.5, va='center', color=RED if i in red else BLACK)
fig.text(0.5, 0.035, '取得原因（所有権をどうやって取得したか）と、表題登記の登記原因（土地がどうやって生じたか）を混ぜない。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H28_dai21mon_zu06_touki_genin.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図6: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図7：問3 分合筆の前と後
# =====================================================================
fig, (ax1, ax2) = new_figure('図7　問3　分合筆の前と後（登録免許税は分合筆後の2個で金2,000円）',
                             '左：申請前。32番1は登記記録351㎡（地積測量図の面積351.67100）、40番2は276㎡。（ロ）部分（46.4342）を32番1へ移す。\n'
                             '右：分合筆後。（イ）40番2は座標の230.2059 → 230㎡。32番1はK1→K2→K3→B→G→J→Aを座標法で求積し、\n'
                             '351.67100 ＋ 46.4342 ＝ 398.1052 → 398㎡（351 ＋ 46 ＝ 397 は誤り）。',
                             ncols=2)
zs = []
for ax, after in [(ax1, False), (ax2, True)]:
    z = Zu(ax, fontsize=14)
    fit(ax, N32_1 + TEI, margin=0.10, pad_aspect=True)
    if after:
        z.poly(N32_1_GO, fill=BLUE)
        z.poly(I_40_2, fill=GREEN)
        ax.set_title('分合筆の後', fontsize=18, weight='bold', color=RED, pad=6)
    else:
        z.poly(N32_1, fill=BLUE)
        z.poly(I_40_2, fill=GREEN, color=BLACK)
        z.poly(RO, fill=RED, alpha=0.30, color=BLACK)
        z.line(J, G, color=RED, lw=2.4, ls='--')
        ax.set_title('分合筆の前（登記記録）', fontsize=18, weight='bold', pad=6)
    z.north_arrow(length=0.07)
    for p, n in [(A, 'A'), (B, 'B'), (G, 'G'), (H, 'H'), (I, 'I'), (J, 'J'), (K1, 'K1'), (K2, 'K2'), (K3, 'K3')]:
        z.point(p, 'dot', size=5)
        z.point_label(p, n, away=centroid(N32_1_GO), fs=12)
    zs.append(z)
zs[0].free_text(centroid(N32_1), '32番1　畑\n351㎡\n（351.67100）', fs=16)
zs[0].free_text(centroid(I_40_2), '40番2　畑\n276㎡', fs=16, offsets=((0, 25), (0, 45), (0, 0)))
zs[0].callout(centroid(RO), '（ロ）部分 46.4342', dirs=(75, 60, 90, 105), color=RED, dists=(55, 75, 95))
zs[1].free_text(centroid(N32_1), '32番1　畑\n398㎡\n（398.1052）', fs=16, color=RED)
zs[1].free_text(centroid(I_40_2), '（イ）40番2　畑\n230㎡\n（230.2059）', fs=16, offsets=((0, 25), (0, 45), (0, 0)))
ALL_PROBLEMS += save(fig, zs, 'H28_dai21mon_zu07_bungouhitsu.png')

# =====================================================================
# 図8：問4 地積測量図（40番2）の完成見本
# =====================================================================
fig, (ax,) = new_figure('図8　問4　地積測量図（40番2）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm（丁土地は横約77mm・縦約82mm、基準点まで入れると横約147mm）。\n'
                        '辺長は小数第3位を四捨五入（ABは19.6025なので19.60、JAは2.3945…なので2.39）。（ロ）には地番を付けない。\n'
                        '座標値・地積・求積方法・測量年月日は書かない（注5）。A101・A102は位置と点名だけ（注6）。合筆先の32番1の形は描かない。')
z = Zu(ax)
fit(ax, TEI + [A101, A102], margin=0.07, pad_aspect=True)
z.poly(TEI, lw=2.0)
z.line(J, G, lw=2.0)
z.north_arrow()
ct = centroid(TEI)
for n, (p, q, s) in SIDES.items():
    if n == 'JA':
        z.edge_label(p, q, s, ct, fs=15, dists=(12, 18, 24), ts=(0.5,))
    else:
        z.edge_label(p, q, s, ct, fs=16)
z.edge_label(J, G, '19.20', centroid(I_40_2), fs=16, outward=False, ts=(0.5, 0.6, 0.4))
z.free_text(centroid(I_40_2), '（イ）\n40－2', fs=18)
z.free_text(centroid(RO), '（ロ）', fs=15, offsets=((0, 0), (-20, -2), (20, 2)))
for p, n in [(A, 'A'), (B, 'B'), (G, 'G'), (J, 'J')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=ct)
for p, n in [(H, 'H'), (I, 'I')]:
    z.point(p, 'metal', size=9)
    z.point_label(p, n, away=ct)
for p, n in [(A101, 'A101'), (A102, 'A102')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=ct)
z.edge_label(A, B, '32－1', ct, fs=16, dists=(42, 52), rotate=False)
z.free_text(B, '31－2', fs=16, offsets=((40, 30), (50, 20), (30, 40)))
z.free_text(A, '34', fs=16, offsets=((-35, 28), (-45, 20), (-30, 38)))
z.edge_label(G, H, '40－1', ct, fs=16, dists=(42, 52), rotate=False)
z.edge_label(I, J, '41', ct, fs=16, dists=(42, 52), rotate=False)
z.edge_label(H, I, '道路', ct, fs=16, dists=(40, 50), rotate=False)
z.free_text(P(349.5, 292.5), '（単位：ｍ）\n◎ コンクリート杭：A・B・G・J\n● 金属標：H・I\n△ 基準点：A101・A102', fs=13,
            ha='left', va='top', offsets=((0, 0), (0, -30), (-30, 0)))
ALL_PROBLEMS += save(fig, [z], 'H28_dai21mon_zu08_chiseki_sokuryouzu.png')

print('重なりの合計:', len(ALL_PROBLEMS))
