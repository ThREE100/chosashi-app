"""平成21年度 第21問（土地）会話形式note記事の解説図14枚を、座標値から作図する。

`../prompt_H21_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../H24/Q21/zu/draw_H24_dai21mon_kaisetsuzu.py`。

J点は、HJとDCの延長線の交点P（550.27, 485.26）がHの50m北にあるので、Pまで入れる図は縦長の全体パネルと、
乙土地のまわりの拡大パネルの2つに分ける。（ハ）部分は幅0.57mの細い帯なので、拡大パネルで描く。

実行: python3 note-articles-Kijyutsu/H21/Q21/zu/draw_H21_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, to_dms, area, chiseki, fmt_num  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の測量成果と、記事で求めた点） ------------------------------------
T1, T2 = P(498.10, 483.60), P(500.00, 500.00)
A, B, C, D = P(500.27, 484.69), P(506.89, 484.69), P(510.27, 495.26), P(500.27, 497.76)
E, F, G = P(500.27, 482.76), P(514.91, 482.76), P(518.27, 493.26)
S1, S2 = P(500.27, 481.00), P(500.27, 501.88)
H = E + 2.50j                                               # 問1の準備：EからEFに直角（東）へ2.50m
HW = A + 2.50j                                              # 誤り：Aから2.50m
IX = B + (C - B) * 0.57 / 10.57                             # 問1 I
I = r2(IX)
PP = D + (C - D) * 12.50 / 2.50                             # HJとDCの延長線の交点P
S_OTSU = abs(((C - A).conjugate() * (D - B)).imag) / 2      # 乙土地 100.3367
S_PHD = abs(((PP - H).conjugate() * (D - H)).imag) / 2      # △PHD 312.5
K_ = math.sqrt((312.5 - 100.3367) / 312.5)                  # 相似比k
JX, LX = PP + (H - PP) * K_, PP + (D - PP) * K_
J, L = r2(JX), r2(LX)
KW = math.sqrt((312.5 - 100) / 312.5)                       # 誤り：登記記録の100㎡で出したk
JW, LW = r2(PP + (H - PP) * KW), r2(PP + (D - PP) * KW)
KX = B + (C - B) * 2.18 / 3.38                              # K（BC上、X座標はJと同じ）
K = r2(KX)
S_HJLD = abs(((L - H).conjugate() * (D - J)).imag) / 2      # 交換後の乙土地（丸めたJ・L）100.32
S_RO = abs(((C - K).conjugate() * (L - K)).imag) / 2        # 問2 （ロ）2.43
S_HA = abs(((I - A).conjugate() * (H - B)).imag) / 2        # 問3 （ハ）3.8247
S_I = area([J, I, K])                                       # （イ）6.25
S_REM = area([H, I, K, L, D])                               # 分筆後の100番1 94.07
# 別解（2次方程式。真数表のtan）
T72, T166 = 3.12724, 0.25
QB, QC = 3.20 * T72, 3.20 * 3.20 * T72 / 2 - 3.8247
HH = (-QB + math.sqrt(QB * QB + 4 * 0.125 * QC)) / (2 * 0.125)

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
assert H == P(500.27, 485.26) and HW == P(500.27, 487.19)
assert f'{abs(H - E):.2f}' == '2.50' and f'{A.imag - E.imag:.2f}' == '1.93' and f'{HW.imag - E.imag:.2f}' == '4.43'
assert fmt_num(IX.real) == '507.0722…' and I == P(507.07, 485.26)
assert PP == P(550.27, 485.26) and S_PHD == 312.5
assert f'{S_OTSU:.4f}' == '100.3367' and fmt_num(K_) == '0.8239…'
assert fmt_num(JX.real) == '509.0716…' and fmt_num(LX.imag) == '495.5595…'
assert J == P(509.07, 485.26) and L == P(509.07, 495.56)
assert JW == P(509.04, 485.26) and fmt_num(KW) == '0.8246…' and JW.real < J.real
assert K == P(509.07, 491.51) and fmt_num(KX.imag) == '491.5073…'
assert f'{S_HJLD:.2f}' == '100.32' and f'{S_RO:.2f}' == '2.43' and f'{S_HA:.4f}' == '3.8247' and chiseki(S_HA) == 3.82
assert f'{S_I:.2f}' == '6.25' and f'{S_RO + S_HA:.4f}' == '6.2547' and f'{S_REM:.2f}' == '94.07'
assert f'{94.07 + 2.43 + 3.82:.2f}' == '100.32'
assert fmt_num(HH) == '1.1998…' and fmt_num(510.27 - HH) == '509.0701…'
assert to_dms(cmath.phase(C - B)) == '72°16′01.67″' and to_dms(cmath.phase(D - C)) == '165°57′49.52″'
assert fmt_num(abs(C - G)) == '8.2462…' and fmt_num(abs(C - D)) == '10.3077…'
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'AB': (A, B, '6.62'), 'BI': (B, I, '0.60'), 'IK': (I, K, '6.56'), 'KC': (K, C, '3.94'),
         'CL': (C, L, '1.24'), 'LD': (L, D, '9.07'), 'DH': (D, H, '12.50'), 'HA': (H, A, '0.57'),
         'HI': (H, I, '6.80'), 'KL': (K, L, '4.05')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
print('数値の照合: すべて一致')


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


def fixed_figure(title, h=12):
    """整理図（文字の位置を固定して並べる図）の土台。"""
    setup_font()
    fig = plt.figure(figsize=(16, h), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.08, 0.94, 0.83])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    return fig, ax


ALL_PROBLEMS = []
OTSU = [A, B, C, D]                        # 乙土地（100番1）
HEI = [E, F, G, C, B, A]                   # 丙土地（100番2）
II = [J, I, K]                             # （イ）部分（丙土地の一部）
RO = [K, C, L]                             # （ロ）部分（乙土地の一部）
HA = [A, B, I, H]                          # （ハ）部分（乙土地の一部）
REM = [H, I, K, L, D]                      # 分筆後の100番1
AFTER = [H, J, L, D]                       # 交換後の乙土地
KIND = {'A': 'concrete', 'B': 'concrete', 'C': 'concrete', 'E': 'concrete', 'G': 'concrete', 'H': 'concrete',
        'J': 'concrete', 'D': 'metal', 'F': 'metal', 'L': 'metal', 'I': 'dot', 'K': 'dot'}
PTS = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 'K': K, 'L': L}
CO = centroid(OTSU)


def pt(z, n, size=None, color=BLACK):
    k = KIND[n]
    if k == 'dot':
        z.point(PTS[n], 'dot', size=size or 6, color=color)
    else:
        z.point(PTS[n], k, size=size or (6 if k == 'concrete' else 8), color=color)


# =====================================================================
# 図1：全体図
# =====================================================================
fig, (ax,) = new_figure('北を上にして描き直した全体図',
                        '乙土地（100番1、乙山次郎、畑100㎡）は A→B→C→D、丙土地（100番2、丙川三郎、宅地150.00㎡）は E→F→G→C→B→A の旗ざお地。\n'
                        'S1・E・A・D・S2 はX座標 500.27 で東西にまっすぐ、EとFはY座標 482.76 で直線EFは真北向き。だから HJ は南北、JL は東西の線。\n'
                        '（イ）は丙土地の一部、（ロ）（ハ）は乙土地の一部。I・J・L を問1で、K を問2で求める。')
z = Zu(ax)
FN = F + (F - E) / abs(F - E) * 2.4
GN = G + (G - D) / abs(G - D) * 2.4
GE = G + (G - F) / abs(G - F) * 2.4
fit(ax, [S1, S2, T1, T2, E, F, G, FN, GN, GE, D], margin=0.06, pad_aspect=True)
z.poly(OTSU, fill=GREEN, alpha=0.12)
z.poly(HEI, fill=BLUE, alpha=0.10)
z.poly(II, color=ORANGE, lw=1.4, fill=ORANGE, alpha=0.40)
z.poly(RO, color=RED, lw=1.4, fill=RED, alpha=0.40)
z.poly(HA, color=PURPLE, lw=1.2, fill=PURPLE, alpha=0.40)
z.poly([H, J, L], color=RED, lw=2.0, ls='--', closed=False)
z.line(S1, S2, color=GRAY, lw=1.6)
z.line(F, FN, lw=1.2)
z.line(G, GN, lw=1.2)
z.line(G, GE, lw=1.2)
z.north_arrow()
z.free_text(CO + P(-1.6, 1.8), '乙土地\n100番1', fs=17)
z.free_text(centroid([E, F, G, C, B]) + P(1.8, -1.0), '丙土地\n100番2', fs=17)
for n in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'):
    pt(z, n, size=5 if KIND[n] in ('concrete', 'dot') else 7)
for n in ('A', 'B', 'C', 'D', 'E', 'F', 'G'):
    z.point_label(PTS[n], n, away=centroid([E, F, G, D]), fs=14)
z.point_label(H, 'H', away=H + P(-1, 0.3), fs=14)
z.point_label(J, 'J', away=J + P(0, 1), fs=14)
z.point_label(I, 'I', away=I + P(1, 1), fs=14)
z.point_label(K, 'K', away=K + P(1, -0.2), fs=14)
z.point_label(L, 'L', away=L + P(0, -1), fs=14)
z.callout(centroid(II), '（イ）丙土地の一部', dirs=(-150, -165, -135, 180), color=ORANGE, dists=(80, 105, 130))
z.callout(centroid(RO), '（ロ）乙土地の一部', dirs=(15, 0, 30, -15), color=RED, dists=(90, 115, 140))
z.callout(B + (A - B) * 0.45 + (H - A) * 0.5, '（ハ）乙土地の一部', dirs=(-165, 180, -150), color=PURPLE, dists=(110, 135, 160))
for p, n in [(S1, 'S1'), (S2, 'S2')]:
    z.point(p, 'metal', size=6, color=GRAY)
    z.point_label(p, n, away=p + P(1, 0), fs=13, color=GRAY, weight='normal')
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=p + P(1, 0), fs=13)
z.free_text(P(519.6, 486.5), '101', fs=15, color=GRAY, offsets=((0, 0), (0, 15), (-15, 0)))
z.free_text(P(506.0, 480.4), '102', fs=15, color=GRAY, offsets=((0, 0), (-10, 0), (0, 15)))
z.free_text(P(519.4, 497.0), '98', fs=15, color=GRAY, offsets=((0, 0), (10, 0), (0, -12)))
z.free_text(P(507.0, 499.4), '99', fs=15, color=GRAY, offsets=((0, 0), (12, 0), (0, 12)))
z.free_text(P(499.1, 491.8), '公道（市道35号線・幅員6.0m）', fs=14, color=GRAY, offsets=((0, 0), (0, -10), (30, -10)))
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu02_zentaizu.png')

# =====================================================================
# 図2：筆界点の裏付け（確認書図面と乙土地の面積）
# =====================================================================
fig, (ax,) = new_figure('筆界点は確認書と乙土地の面積で裏付ける',
                        '平成8年の確認書図面の G→C 8.25・C→D 10.31 は、座標から出した 8.2462…・10.3077… を四捨五入した値と一致する。\n'
                        '乙土地 A→B→C→D の面積は Conjg(C − A) × (D − B) で 100.3367㎡。登記記録の100㎡との差0.3367㎡は、\n'
                        '市街地地域の精度区分 甲2 の公差0.82㎡（問題文の注5）の範囲。「乙土地」の呼び名につられて乙1（2.26㎡）を選ばない。')
z = Zu(ax)
fit(ax, [A, B, C, D, E, F, G, GN, S1, S2], margin=0.06, pad_aspect=True)
z.poly(HEI, color=GRAY, lw=1.2, fill=BLUE, alpha=0.06)
z.poly(OTSU, lw=2.2, fill=GREEN, alpha=0.25)
z.line(G, GN, color=GRAY, lw=1.1)
z.line(S1, S2, color=GRAY, lw=1.4)
z.line(G, C, color=RED, lw=3.0)
z.line(C, D, color=BLUE, lw=3.0)
z.north_arrow()
for n in ('A', 'B', 'C', 'D', 'G'):
    pt(z, n)
    z.point_label(PTS[n], n, away=CO if n != 'G' else G + P(0, -1), fs=15)
z.callout(G + (C - G) * 0.5, 'G→C　確認書 8.25\n座標 8.2462… → 8.25', dirs=(20, 0, 40), color=RED, dists=(70, 95, 120))
z.callout(C + (D - C) * 0.5, 'C→D　確認書 10.31\n座標 10.3077… → 10.31', dirs=(-10, 10, -30), color=BLUE, dists=(80, 105, 130))
z.free_text(CO, '乙土地 A→B→C→D\n実測 100.3367㎡\n登記記録 100㎡\n差 0.3367㎡ ＜ 甲2 0.82㎡', fs=16)
z.free_text(centroid([E, F, G, C, B]) + P(1.5, -1.0), '丙土地', fs=15, color=GRAY)
z.free_text(P(519.0, 496.5), '98', fs=15, color=GRAY, offsets=((0, 0), (10, 0), (0, -12)))
z.free_text(P(507.0, 499.3), '99', fs=15, color=GRAY, offsets=((0, 0), (12, 0), (0, 12)))
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu05_hikkai_uradzuke.png')

# =====================================================================
# 図3：H点（E点から2.50m）
# =====================================================================
fig, (ax,) = new_figure('問1の準備　H点は E点から東へ2.50m',
                        '丙土地から公道へ出る通路の幅員は、丙土地の筆界EF（真北向き）から新しい筆界HJまで。EFが南北なので、東へ2.50m進めば直角の幅になり、\n'
                        'H ＝ E ＋ 2.50i ＝（500.27, 485.26）。今の通路は E→A の 1.93m しかない。Aから2.50mとると H が（500.27, 487.19）になり、\n'
                        '通路が 4.43m に広がってしまう（誤り）。')
z = Zu(ax)
TOP = 503.6
fit(ax, [P(499.0, 481.4), P(TOP, 488.4)], margin=0.02, pad_aspect=True)
z.poly([E, P(TOP, 482.76), P(TOP, 484.69), A], color=GRAY, lw=0.0, fill=BLUE, alpha=0.10, closed=True, check=False)
z.line(E, P(TOP, 482.76), lw=2.2)
z.line(A, P(TOP, 484.69), lw=2.2)
z.line(H, P(TOP, 485.26), color=RED, lw=2.4)
z.line(HW, P(TOP, 487.19), color=GRAY, lw=1.6, ls='--')
z.line(P(500.27, 481.4), P(500.27, 488.4), color=GRAY, lw=1.6)
z.north_arrow(length=0.08)
Y0 = 501.9
z.dim_line(P(Y0, 482.76), P(Y0, 485.26), color=RED, lw=1.8)
z.dim_line(P(Y0 - 0.9, 482.76), P(Y0 - 0.9, 484.69), color=GRAY, lw=1.8)
z.free_text(P(Y0 + 0.35, 0) + (483.97 - 0) * 1j, '幅員 2.50', fs=16, color=RED)
z.free_text(P(Y0 - 0.9 - 0.35, 0) + 483.73j, '今の通路 1.93', fs=15, color=GRAY)
for n in ('E', 'A', 'H'):
    pt(z, n, size=9)
z.point_label(E, 'E', away=E + P(0.5, 1), fs=16)
z.point_label(A, 'A', away=A + P(0.5, -0.5), fs=16)
z.point(HW, 'dot', size=9, color=GRAY)
z.callout(H, 'H（500.27, 485.26）', dirs=(-60, -40, -80), color=RED, dists=(60, 80, 100))
z.callout(HW, '誤り：Aから2.50m\n（500.27, 487.19）\n通路は 4.43m', dirs=(-40, -20, -60), color=GRAY, dists=(60, 80, 100))
z.free_text(P(502.9, 482.2), 'F へ（EF）', fs=14, offsets=((0, 0), (-10, 0), (0, -12)))
z.free_text(P(502.9, 485.8), 'J へ（HJ）', fs=14, color=RED, offsets=((0, 0), (10, 0), (0, -12)))
z.free_text(P(502.9, 484.2), 'B へ（AB）', fs=14, offsets=((0, 0), (-10, 0), (0, -12)))
z.free_text(P(499.4, 485.8), '道路境界（X＝500.27）', fs=14, color=GRAY, offsets=((0, 0), (0, -8), (30, 0)))
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu06_H_haba.png')

# =====================================================================
# 図4：I点（BCとHJの交点）
# =====================================================================
fig, (ax,) = new_figure('問1　I点は BC と HJ（Y＝485.26）の交点',
                        'HJは南北の線（Y ＝ 485.26）。BからCまでY座標は 10.57、BからHJまでは 0.57 だけ東へ進むので、I ＝ B ＋ (C − B) × 0.57 ÷ 10.57。\n'
                        '表示 507.0722… ＋ 485.26i を四捨五入して I（507.07, 485.26）。B→Cの方向角 72°16′01.67″ は、\n'
                        '問題文の注4の三角関数真数表の 72°16′2″ の行（tan 3.12724＝北へ1mで東へ3.12724m）と合う。')
z = Zu(ax)
W0 = 503.9
fit(ax, [P(W0, 483.0), P(511.4, 496.6), C + (D - C) * 0.12], margin=0.02, pad_aspect=True)
z.line(B, C, lw=2.4)
z.line(C, C + (D - C) * 0.12, lw=1.4)
z.line(P(W0, 485.26), P(510.9, 485.26), color=RED, lw=2.0, ls='--')
z.line(P(W0, 484.69), B, color=BLACK, lw=1.6)
XA = 505.3
z.dim_line(P(XA, 484.69), P(XA, 485.26), color=RED)
z.north_arrow(length=0.08)
pt(z, 'B', size=9)
pt(z, 'C', size=9)
z.point(I, 'dot', color=RED, size=10)
z.point_label(B, 'B', away=B + P(0, -1), fs=16)
z.point_label(C, 'C', away=C + P(0.5, 1), fs=16)
z.callout(I, 'I（507.07, 485.26）', dirs=(60, 40, 80), color=RED, dists=(70, 95, 120))
z.edge_label(B, C, 'Y座標の差 10.57', CO, fs=15)
z.callout(P(XA, 484.975), 'BからHJまで 0.57', dirs=(-30, -15, -45), color=RED, dists=(60, 80, 100))
z.free_text(P(510.3, 485.26), 'HJ（Y＝485.26）', fs=14, color=RED, ha='left', offsets=((8, 0), (8, 14)))
z.free_text(P(W0 + 0.35, 484.69), 'AB（Y＝484.69）', fs=14, ha='right', offsets=((-8, 0), (-8, 14)))
z.callout(C + (D - C) * 0.10, 'Dへ', dirs=(0, 20, -20), dists=(40, 55))
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu07_I_kouten.png')

# =====================================================================
# 図5：J点（交換後の乙土地と延長線の交点Pの相似）
# =====================================================================
fig, (ax1, ax2) = new_figure('問1　J点は、交換後の乙土地を元の面積にする相似比で',
                             '交換後の乙土地 H→J→L→D は、面積の変動がない交換なので、元の乙土地と同じ実測 100.3367㎡（登記記録の100㎡ではない）。\n'
                             'HJとDCを北へ延ばした交点 P（550.27, 485.26）で △PHD ＝ 312.5㎡、△PJL ＝ 312.5 − 100.3367 ＝ 212.1633㎡。JL ∥ HD なので相似で、\n'
                             'k ＝ √(212.1633 ÷ 312.5) ＝ 0.8239…、J ＝ P ＋ (H − P) × k ＝（509.07, 485.26）。100㎡で出すと k ＝ 0.8246… で J は（509.04, 485.26）。',
                             ncols=2, width_ratios=[0.75, 1.25])
za = Zu(ax1, fontsize=14)
fit(ax1, [H, D, PP, P(500.27, 483.0), P(551.0, 512.0)], margin=0.02, pad_aspect=True)
za.poly([PP, H, D], color=ORANGE, lw=1.6, ls='--', fill=ORANGE, alpha=0.10)
za.poly([PP, J, L], color=BLUE, lw=1.2, fill=BLUE, alpha=0.18)
za.poly(AFTER, color=GREEN, lw=1.6, fill=GREEN, alpha=0.35)
za.north_arrow(length=0.06)
za.point(PP, 'dot', color=RED, size=8)
za.callout(PP, 'P（550.27, 485.26）', dirs=(-60, -75, -45), color=RED, dists=(50, 70, 90), fs=13)
za.callout(P(527.0, 489.5), '△PJL\n212.1633㎡', dirs=(0, 15, -15), color=BLUE, dists=(60, 80, 100), fs=13)
za.callout(P(504.5, 492.0), '乙土地（交換後）\n100.3367㎡', dirs=(15, 30, 0), color=GREEN, dists=(60, 80, 100), fs=13)
za.point_label(H, 'H', away=H + P(0.5, -1), fs=13)
za.point_label(D, 'D', away=D + P(-0.5, 1), fs=13)
ax1.set_title('全体（△PHD ＝ 312.5㎡）', fontsize=16, weight='bold', pad=6)

zb = Zu(ax2, fontsize=15)
fit(ax2, [P(499.2, 480.2), P(515.0, 499.0)], margin=0.02, pad_aspect=True)
zb.poly(OTSU, color=GRAY, lw=1.2, ls='--')
zb.poly(AFTER, color=GREEN, lw=2.2, fill=GREEN, alpha=0.22)
zb.line(J, P(515.0, 485.26), color=ORANGE, lw=1.4, ls='--')
zb.line(L, D + (C - D) * 1.47, color=ORANGE, lw=1.4, ls='--')
zb.north_arrow(length=0.08)
pt(zb, 'H', size=9)
pt(zb, 'D', size=9)
zb.point(J, 'dot', color=RED, size=10)
zb.point(L, 'dot', color=BLUE, size=8)
zb.point_label(H, 'H', away=H + P(0.5, -1), fs=16)
zb.point_label(D, 'D', away=D + P(-0.5, 1), fs=16)
zb.point_label(L, 'L', away=L + P(0, 1), fs=16, color=BLUE)
zb.callout(J, 'J（509.07, 485.26）', dirs=(120, 135, 105), color=RED, dists=(60, 80, 100))
zb.free_text(centroid(AFTER), '交換後の乙土地\nH→J→L→D\n100.3367㎡にする', fs=16, color=GREEN)
zb.callout(J + (P(515.0, 485.26) - J) * 0.6, 'Pへ（北へ）', dirs=(170, 150, -170), color=ORANGE, dists=(50, 70, 90))
ax2.set_title('乙土地のまわりの拡大', fontsize=16, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H21_dai21mon_zu08_J_souji.png')

# =====================================================================
# 図6：L点（同じ相似比）と交換後の乙土地の検算
# =====================================================================
fig, (ax,) = new_figure('問1　L点も同じ相似比 k で出る',
                        'L ＝ P ＋ (D − P) × k（表示 509.0716… ＋ 495.5595…i）で L（509.07, 495.56）。JとLはX座標が同じで、JLは東西の線（S1S2に平行）。\n'
                        '丸めたJ・Lで交換後の乙土地 H→J→L→D を Conjg(L − H) × (D − J) で確かめると 100.32㎡（丸めのぶん100.3367との差0.0167）。\n'
                        '台形としても、HD 12.50 と JL 10.30 の平均 11.40 に高さ 8.80 を掛けて 100.32。')
z = Zu(ax)
fit(ax, [P(498.6, 482.6), P(512.2, 499.6)], margin=0.02, pad_aspect=True)
z.poly(OTSU, color=GRAY, lw=1.2, ls='--')
z.poly(AFTER, color=GREEN, lw=2.4, fill=GREEN, alpha=0.22)
z.line(C, C + (C - D) * 0.18, color=ORANGE, lw=1.4, ls='--')
z.north_arrow(length=0.08)
pt(z, 'H', size=9)
pt(z, 'D', size=9)
z.point(J, 'dot', color=BLUE, size=8)
z.point(L, 'dot', color=RED, size=10)
z.point_label(H, 'H', away=H + P(0.5, -1), fs=16)
z.point_label(D, 'D', away=D + P(-0.5, 1), fs=16)
z.point_label(J, 'J', away=J + P(0.5, -1), fs=16, color=BLUE)
z.callout(L, 'L（509.07, 495.56）', dirs=(30, 15, 45), color=RED, dists=(70, 95, 120))
z.edge_label(H, D, 'HD 12.50', CO, fs=15)
z.edge_label(J, L, 'JL 10.30', CO, fs=15)
z.edge_label(H, J, '高さ 8.80', CO, fs=15)
z.free_text(centroid(AFTER), '交換後の乙土地\nH→J→L→D\n100.32㎡', fs=17, color=GREEN)
z.callout(C + (C - D) * 0.15, 'Pへ（DCの延長）', dirs=(-20, 0, -40), color=ORANGE, dists=(50, 70, 90))
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu10_L_souji.png')

# =====================================================================
# 図7：問2（ロ）部分 K・C・L
# =====================================================================
fig, (ax,) = new_figure('問2　（ロ）部分は K→C→L の三角形で 2.43㎡',
                        'K は BC 上でX座標がJと同じ 509.07。K ＝ B ＋ (C − B) × 2.18 ÷ 3.38（表示 509.07 ＋ 491.5073…i）で K（509.07, 491.51）。\n'
                        '（ロ）は Conjg(C − K) × (L − K) の iの係数 4.86 の半分で 2.43㎡。KL 4.05 × 高さ 1.20 ÷ 2 ＝ 2.43 とも合う。')
z = Zu(ax)
fit(ax, [P(508.3, 489.6), P(511.0, 497.2)], margin=0.02, pad_aspect=True)
z.poly(RO, color=RED, lw=2.2, fill=RED, alpha=0.25)
z.line(K + (B - K) * 0.12, K, lw=1.6)
z.line(L, L + (D - L) * 0.10, lw=1.6)
z.line(P(509.07, 490.5), K, color=GRAY, lw=1.2, ls='--')
FOOT = P(509.07, 495.26)
z.line(C, FOOT, color=BLUE, lw=1.6, ls='--')
z.right_angle(FOOT, K, C, size=0.12, color=BLUE)
z.north_arrow(length=0.08)
z.point(K, 'dot', color=RED, size=9)
pt(z, 'C', size=9)
z.point(L, 'metal', size=9, color=RED)
z.point_label(C, 'C', away=C + P(0.5, 0.5), fs=16)
z.callout(K, 'K（509.07, 491.51）', dirs=(-120, -140, -100), color=RED, dists=(60, 80, 100))
z.callout(L, 'L（509.07, 495.56）', dirs=(-60, -40, -80), color=RED, dists=(60, 80, 100))
z.edge_label(K, L, 'KL 4.05', C, fs=15)
z.callout(C + (FOOT - C) * 0.5, '高さ 1.20', dirs=(60, 80, 40), color=BLUE, dists=(40, 55, 70))
z.free_text(centroid(RO) + P(0.1, -0.7), '（ロ）\n2.43㎡', fs=16, color=RED, offsets=((0, 0), (0, -15), (-15, 0)))
z.callout(K + (B - K) * 0.08, 'Bへ（BC）', dirs=(150, 170, 130), dists=(40, 55, 70))
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu11_ro_menseki.png')

# =====================================================================
# 図8：問3（ハ）部分と等積の確かめ
# =====================================================================
fig, (ax1, ax2) = new_figure('問3　（ハ）部分は 3.82㎡。（イ）＝（ロ）＋（ハ）の確かめ',
                             '（ハ）A→B→I→H は AB と HI が南北で平行な台形。Conjg(I − A) × (H − B) の iの係数 7.6494 の半分で 3.8247 → 3.82㎡。\n'
                             '（イ）J→I→K は直角三角形で JI 2.00 × JK 6.25 ÷ 2 ＝ 6.25㎡。（ロ）＋（ハ）＝ 2.43 ＋ 3.8247 ＝ 6.2547㎡で、\n'
                             '差0.0047㎡は J・K・L を小数第2位に丸めたぶん。地積の桁では等積になる。',
                             ncols=2, width_ratios=[0.8, 1.2])
za = Zu(ax1, fontsize=15)
fit(za.ax, [P(499.4, 483.3), P(508.0, 486.7)], margin=0.02, pad_aspect=True)
za.poly(HA, color=PURPLE, lw=2.2, fill=PURPLE, alpha=0.30)
za.north_arrow(length=0.07)
for n in ('A', 'B', 'H'):
    pt(za, n, size=9)
za.point(I, 'dot', size=9, color=BLACK)
za.point_label(A, 'A', away=A + P(0.3, 1), fs=15)
za.point_label(B, 'B', away=B + P(-0.3, 1), fs=15)
za.point_label(H, 'H', away=H + P(0.3, -1), fs=15)
za.point_label(I, 'I', away=I + P(-0.3, -1), fs=15)
za.edge_label(A, B, 'AB 6.62', centroid(HA), fs=14)
za.edge_label(H, I, 'HI 6.80', centroid(HA), fs=14)
za.callout(A + (H - A) * 0.5, '幅 0.57', dirs=(-100, -120, -80), dists=(40, 55, 70))
za.callout(centroid(HA), '（ハ）3.8247 → 3.82㎡', dirs=(-40, -20, -60), color=PURPLE, dists=(70, 95, 120))
ax1.set_title('（ハ）部分', fontsize=16, weight='bold', pad=6)

zb = Zu(ax2, fontsize=15)
fit(zb.ax, [P(506.4, 484.4), P(510.8, 496.4)], margin=0.02, pad_aspect=True)
zb.poly(II, color=ORANGE, lw=2.0, fill=ORANGE, alpha=0.30)
zb.poly(RO, color=RED, lw=2.0, fill=RED, alpha=0.30)
zb.line(I + (I - K) * 0.08, C, color=BLACK, lw=1.4)
zb.north_arrow(length=0.07)
zb.point(J, 'concrete', size=8)
zb.point(I, 'dot', size=8)
zb.point(K, 'dot', size=8)
zb.point(C, 'concrete', size=8)
zb.point(L, 'metal', size=9)
for n, p, aw in [('J', J, J + P(-1, 0.5)), ('I', I, I + P(1, 0.5)), ('K', K, K + P(-1, 0.3)), ('C', C, C + P(-0.5, -1)),
                 ('L', L, L + P(1, -0.3))]:
    zb.point_label(p, n, away=aw, fs=15)
zb.edge_label(J, I, 'JI 2.00', centroid(II), fs=14)
zb.edge_label(J, K, 'JK 6.25', centroid(II), fs=14)
zb.callout(centroid(II), '（イ）6.25㎡', dirs=(-60, -40, -80), color=ORANGE, dists=(60, 80, 100))
zb.callout(centroid(RO), '（ロ）2.43㎡', dirs=(-30, -10, -50), color=RED, dists=(60, 80, 100))
zb.free_text(P(506.9, 492.0), '（ロ）＋（ハ）\n＝ 2.43 ＋ 3.8247\n＝ 6.2547㎡', fs=16, offsets=((0, 0), (0, -20), (0, 20)))
ax2.set_title('（イ）部分と（ロ）部分', fontsize=16, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H21_dai21mon_zu12_ha_toseki.png')

# =====================================================================
# 図9：J点の別解（2次方程式）
# =====================================================================
fig, (ax,) = new_figure('J点の別解　（イ）＝（ロ）＋（ハ）を h の2次方程式で',
                        'JLの線からCまでの高さを h とすると、IからJLの線までは 3.20 − h。（イ）＝ (3.20 − h)² × 3.12724 ÷ 2、（ロ）＝ h² × 3.37724 ÷ 2（真数表の tan）。\n'
                        '（イ）＝（ロ）＋ 3.8247 を整理すると 0.125h² ＋ 10.007168h − 12.1867688 ＝ 0 で、h ＝ 1.1998…、JのX座標は 510.27 − 1.1998… ＝ 509.0701… → 509.07。\n'
                        '（ハ）を足し忘れて（イ）＝（ロ）にすると、JのX座標は 508.70（0.37m南）。')
z = Zu(ax)
fit(ax, [P(506.4, 481.6), P(511.8, 497.0)], margin=0.02, pad_aspect=True)
z.poly(II, color=ORANGE, lw=2.0, fill=ORANGE, alpha=0.30)
z.poly(RO, color=RED, lw=2.0, fill=RED, alpha=0.30)
z.line(I + (I - K) * 0.08, C, lw=1.4)
z.line(L, L + (D - L) * 0.10, lw=1.4)
z.line(P(510.27, 484.3), P(510.27, 496.6), color=GRAY, lw=1.2, ls='--')
z.line(P(507.07, 484.3), P(507.07, 496.6), color=GRAY, lw=1.2, ls='--')
z.north_arrow(length=0.07)
YA = 496.3
z.dim_line(P(509.07, YA), P(510.27, YA), color=BLUE, lw=1.8)
z.dim_line(P(507.07, YA), P(509.07, YA), color=ORANGE, lw=1.8)
z.free_text(P(509.67, YA), 'h', fs=17, color=BLUE, offsets=((14, 0), (18, 0)))
z.free_text(P(508.07, YA), '3.20 − h', fs=16, color=ORANGE, offsets=((34, 0), (40, 0)))
z.point(J, 'concrete', size=8)
z.point(I, 'dot', size=8)
z.point(K, 'dot', size=8)
z.point(C, 'concrete', size=8)
z.point(L, 'metal', size=9)
for n, p, aw in [('I', I, I + P(1, 0.5)), ('K', K, K + P(-1, 0.3)), ('C', C, C + P(-0.5, -1)), ('L', L, L + P(1, -0.3))]:
    z.point_label(p, n, away=aw, fs=15)
z.callout(J, 'J（509.07, 485.26）', dirs=(150, 165, 135), color=RED, dists=(60, 80, 100))
z.callout(centroid(II), '（イ）＝(3.20 − h)² × 3.12724 ÷ 2', dirs=(-40, -20, -60), color=ORANGE, dists=(90, 115, 140))
z.callout(centroid(RO), '（ロ）＝ h² × 3.37724 ÷ 2', dirs=(-100, -120, -80), color=RED, dists=(60, 80, 100))
z.free_text(P(511.15, 488.0), '真数表\n72°16′2″ の tan 3.12724（BC）\n165°57′50″ の tan −0.25（CD）', fs=15,
            offsets=((0, 0), (0, -20), (20, 0)))
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu13_J_betsukai.png')

# =====================================================================
# 図10：公差の判定（地積の更正は不要）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問4　地積の更正は要らない（甲2の公差0.82㎡の範囲）', fontsize=24, weight='bold', y=0.95)
ax = fig.add_axes([0.05, 0.22, 0.90, 0.60])
ax.set_xlim(98.8, 101.4)
ax.set_ylim(0, 10)
ax.axis('off')
for yy, head, val, col in [(7.0, '分筆後の合計　94.07 ＋ 2.43 ＋ 3.82 ＝ 100.32㎡（差 0.32㎡）', 100.32, RED),
                           (2.6, '乙土地全体の実測　100.3367㎡（差 0.3367㎡）', 100.3367, BLUE)]:
    ax.plot([98.9, 101.3], [yy, yy], color=BLACK, lw=1.6)
    ax.add_patch(plt.Rectangle((100 - 0.82, yy - 0.45), 1.64, 0.9, color=GREEN, alpha=0.25))
    for x in (99.18, 100.0, 100.82):
        ax.plot([x, x], [yy - 0.6, yy + 0.6], color=BLACK, lw=1.4)
    ax.text(99.18, yy - 1.1, '99.18', ha='center', va='top', fontsize=15)
    ax.text(100.0, yy - 1.1, '100（登記記録）', ha='center', va='top', fontsize=15)
    ax.text(100.82, yy - 1.1, '100.82', ha='center', va='top', fontsize=15)
    ax.plot([val], [yy], 'o', color=col, ms=13)
    ax.annotate('', xy=(val, yy + 0.9), xytext=(100.0, yy + 0.9), arrowprops=dict(arrowstyle='->', color=col, lw=2))
    ax.text(99.0, yy + 1.6, head, fontsize=17, weight='bold', color=col, va='bottom')
    ax.text(101.3, yy + 0.6, '甲2の公差の範囲（±0.82）', fontsize=14, color=GREEN, ha='right', va='bottom')
fig.text(0.5, 0.06, '比べるのは、分筆前の登記記録の地積（100㎡）と分筆後の地積の合計（不動産登記事務取扱手続準則第72条第1項）。乙土地は市街地地域なので甲2の0.82㎡。\n'
         '「乙土地」という呼び名につられて乙1（2.26㎡）で比べない（この年度は結論は同じでも、精度区分は地域で決める）。',
         ha='center', va='bottom', fontsize=15)
path = os.path.join(OUT, 'H21_dai21mon_zu17_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図10: 数直線の判定図（固定配置）\n  →', path)

# =====================================================================
# 図11：問4 登記の順番（整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('問4　登記の順番と添付情報（1 地目変更 → 2 分筆）')
BOXES = [
    ('1　土地地目変更登記', BLUE, [
        '原因：②③平成21年8月3日地目変更（建物の新築で畑から宅地。地積の表し方も変わるので③も）',
        '1か月以内に申請する義務（不動産登記法第37条第1項）。申請人は所有権の登記名義人の乙山次郎',
        '添付情報：代理権限証明情報（不動産登記令別表5の項に決まった添付情報はない）',
    ]),
    ('2　土地分筆登記', RED, [
        '残る100番1、（ロ）部分の100番3、（ハ）部分の100番4の3筆。離れた（ロ）と（ハ）は1筆にできない',
        '原因：③100番1、100番3、100番4に分筆（100番1の行）／100番1から分筆（100番3・100番4の行）',
        '添付情報：地積測量図　抵当権消滅承諾証明情報　代理権限証明情報',
        '（ロ）（ハ）の1番抵当権を消す承諾書一式（不動産登記法第40条）。登録免許税は3筆で3,000円（答案用紙に欄なし）',
    ]),
]
y = 95
for head, col, lines in BOXES:
    h = 9.5 + 7.0 * len(lines)
    y -= h
    ax.add_patch(FancyBboxPatch((3, y), 94, h - 2.0, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=col, lw=2.2))
    ax.text(5, y + h - 6.0, head, fontsize=22, weight='bold', va='center', color=col)
    for i, t in enumerate(lines):
        ax.text(7, y + h - 12.5 - i * 7.0, '・' + t, fontsize=15.5, va='center')
    y -= 3
ax.annotate('', xy=(50, 60.0), xytext=(50, 64.0), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=2.5, mutation_scale=25))
fig.text(0.5, 0.035, '同じ土地の地目変更と分筆は一の申請情報にもできる（不動産登記規則第35条第7号）が、問4は「必要な登記の順番に従って」2行の欄に書かせる形。',
         ha='center', va='center', fontsize=15.5)
path = os.path.join(OUT, 'H21_dai21mon_zu23_touki_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図11: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図12：分筆後の区画と地番
# =====================================================================
fig, (ax,) = new_figure('問4　分筆後の区画と地番',
                        '100番1（H→I→K→L→D）は iの係数 188.14 の半分で 94.07㎡。100番3は（ロ）部分で2.43㎡、100番4は（ハ）部分で3.82㎡。合計100.32㎡。\n'
                        '支号のある100番1の分筆なので、1筆に100番1を残し、ほかは本番100の最終の支号2の次から100番3・100番4（準則第67条第1項第4号ただし書）。\n'
                        '（イ）部分は丙土地の一部で、丙川三郎の分筆（この問の申請書には入らない）。')
z = Zu(ax)
fit(ax, [P(499.0, 483.0), P(512.0, 499.3)], margin=0.02, pad_aspect=True)
z.poly(REM, color=BLUE, lw=2.0, fill=BLUE, alpha=0.20)
z.poly(RO, color=RED, lw=2.0, fill=RED, alpha=0.35)
z.poly(HA, color=PURPLE, lw=2.0, fill=PURPLE, alpha=0.40)
z.poly(II, color=GRAY, lw=1.2, ls='--', fill=GRAY, alpha=0.10)
z.north_arrow(length=0.08)
for n in ('A', 'B', 'C', 'D', 'H', 'I', 'K', 'L'):
    pt(z, n, size=7)
for n, aw in [('A', A + P(0.5, 1)), ('B', B + P(-0.5, 1)), ('C', C + P(-0.5, -1)), ('D', D + P(0.5, -1)),
              ('H', H + P(0.5, -1)), ('I', I + P(0.5, -1)), ('K', K + P(0.5, 0)), ('L', L + P(0.5, -1))]:
    z.point_label(PTS[n], n, away=aw, fs=15)
z.free_text(centroid(REM), '100番1\n94.07㎡', fs=18, color=BLUE)
z.callout(centroid(RO), '100番3（ロ）部分\n2.43㎡', dirs=(40, 20, 60), color=RED, dists=(70, 95, 120))
z.callout(A + (B - A) * 0.55 + (H - A) * 0.5, '100番4（ハ）部分\n3.82㎡', dirs=(-165, 180, -150), color=PURPLE, dists=(60, 85, 110))
z.callout(centroid(II), '（イ）部分（丙土地）', dirs=(150, 165, 135), color=GRAY, dists=(70, 95, 120))
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu19_bunpitsu_chiban.png')

# =====================================================================
# 図13：問5 地積測量図の完成見本
# =====================================================================
fig, (ax,) = new_figure('問5　地積測量図（100番1の分筆）の完成見本',
                        '辺長は小数第3位を四捨五入（問題文の注3）。BI 0.5977… → 0.60、CL 1.2369… → 1.24。座標値・求積及びその方法・地積は省略（問題文の注3）。\n'
                        '基準点T1・T2は位置と点名を図に書き、名称と座標値を用紙の適宜の場所に書く（問5）。（イ）は分筆後に残る100番1の符号で、見取図の（イ）部分とは別。\n'
                        '縮尺1/250で 1m ＝ 4mm（T1・T2まで入れて横約66mm・縦約49mm）。')
z = Zu(ax)
fit(ax, [T1, T2, A, B, C, D, P(511.6, 479.8), P(497.2, 507.0)], margin=0.03, pad_aspect=True)
z.poly([A, B, I, K, C, L, D, H], lw=2.0)
z.line(H, I, lw=2.0)
z.line(K, L, lw=2.0)
z.line(A, A + (A - D) / abs(A - D) * 1.2, lw=1.2)
z.line(D, D + (D - A) / abs(D - A) * 1.2, lw=1.2)
z.line(C, C + (C - D) / abs(C - D) * 1.2, lw=1.2)
z.north_arrow()
for n in ('A', 'B', 'C', 'D', 'H', 'L'):
    pt(z, n, size=7)
z.point(I, 'dot', size=3)
z.point(K, 'dot', size=3)
REF = centroid(REM)
for n, aw in [('A', A + P(0.5, 1)), ('B', B + P(-0.5, 1)), ('C', C + P(-0.5, -1)), ('D', D + P(0.5, -1)),
              ('K', K + P(-1, 0)), ('L', L + P(1, -1))]:
    z.point_label(PTS[n], n, away=aw, fs=15)
z.callout(H, 'H', dirs=(-60, -80, -40), fs=15, dists=(40, 55, 70))
z.callout(I, 'I', dirs=(120, 100, 140), fs=15, dists=(40, 55, 70))
z.edge_label(A, B, '6.62', REF + P(0, 3), fs=15)
z.edge_label(I, K, '6.56', REF, fs=15)
z.edge_label(K, C, '3.94', REF, fs=15)
z.edge_label(L, D, '9.07', REF, fs=15)
z.edge_label(D, H, '12.50', REF, fs=15)
z.edge_label(H, I, '6.80', REF, fs=15, outward=False)
z.edge_label(K, L, '4.05', REF, fs=15, outward=False)
z.callout(B + (I - B) * 0.5, '0.60', dirs=(110, 130, 90), fs=15, dists=(50, 65, 80))
z.callout(C + (L - C) * 0.5, '1.24', dirs=(0, 20, -20), fs=15, dists=(45, 60, 75))
z.callout(H + (A - H) * 0.5, '0.57', dirs=(-110, -130, -90), fs=15, dists=(50, 65, 80))
z.free_text(REF, '100－1\n（イ）', fs=18)
z.callout(centroid(RO), '100－3（ロ）', dirs=(60, 80, 40), fs=16, dists=(60, 80, 100))
z.callout(A + (B - A) * 0.35 + (H - A) * 0.5, '100－4（ハ）', dirs=(-170, 170, -150), fs=16, dists=(50, 70, 90))
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=p + P(-1, 0), fs=15)
z.free_text(P(509.5, 488.5), '100－2', fs=16, color=GRAY, offsets=((0, 0), (0, 15), (-20, 0)))
z.free_text(P(504.0, 482.3), '100－2', fs=16, color=GRAY, offsets=((0, 0), (0, 15), (-15, 0)))
z.free_text(P(505.0, 499.8), '99', fs=16, color=GRAY, offsets=((0, 0), (12, 0), (0, 12)))
z.free_text(P(499.0, 491.0), '道路', fs=16, color=GRAY, offsets=((0, 0), (0, -12), (20, 0)))
z.free_text(P(504.6, 500.9),
            '（単位：ｍ）\n◎ コンクリート杭：A・B・C・H\n● 金属標：D・L\n△ 基準点\n'
            '　C市基準点T1（X 498.10、Y 483.60）\n　C市基準点T2（X 500.00、Y 500.00）\n測量の年月日　平成21年8月20日',
            fs=13, ha='left', va='top', offsets=((0, 0), (0, -20), (-20, 0)))
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu25_chiseki_sokuryouzu.png')

# =====================================================================
# 図14：本番で解く順番（整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('本番で解く順番（J点・L点と地積測量図がいちばん時間を食う）')
STEPS = [
    ('1', '問4（計算なし）', '8月3日の地目変更（②③）→ 3筆の分筆。添付情報に抵当権消滅承諾証明情報', GRAY),
    ('2', '乙土地の面積 100.3367㎡', '確認書のGC・CDも確かめる。地積の更正が要らないことも、ここでほぼ決まる', GREEN),
    ('3', 'H点とI点（問1のI）', 'H ＝ E ＋ 2.50i、I ＝ B ＋ (C − B) × 0.57 ÷ 10.57。比例だけ', BLUE),
    ('4', '問3（ハ）3.82㎡', 'A→B→I→H の台形。J点がなくても出せる', PURPLE),
    ('5', 'P点 → 相似比k → J点・L点（問1）', 'P（550.27, 485.26）、△PHD 312.5、k ＝ √(212.1633 ÷ 312.5)', RED),
    ('6', 'K点と問2（ロ）2.43㎡、公差の確かめ', 'K ＝ B ＋ (C − B) × 2.18 ÷ 3.38。100番1は94.07、合計100.32', ORANGE),
    ('7', '地積測量図（問5）', '辺長10本・境界標・T1とT2・100－1（イ）・100－3（ロ）・100－4（ハ）', BLACK),
]
y = 97
for num, head, line, col in STEPS:
    h = 12.8
    y -= h
    ax.add_patch(FancyBboxPatch((3, y), 94, h - 2.0, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=col, lw=2.2))
    ax.text(5, y + h - 5.2, f'{num}　{head}', fontsize=19, weight='bold', va='center', color=col)
    ax.text(8, y + h - 9.4, line, fontsize=15.5, va='center')
fig.text(0.5, 0.035, '1〜4はJ点がなくても書ける。J点で詰まっても、問4・問1のI・問3は先に点になる。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H21_dai21mon_zu26_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図14: 整理図（固定配置）\n  →', path)

# =====================================================================
# ここから、2026-10-26の照らし直しで足した図（記事の論点ごとに1枚。画像の中に図番は入れない）
# =====================================================================
def card(ax, x, y, w, h, ec, fc='#f7f7f7', lw=2.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.4', fc=fc, ec=ec, lw=lw))


def save_fixed(fig, name, label):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print(f'[重なり検査] {label}（固定配置）\n  →', path)


# ---- 時系列 ----
fig, ax = fixed_figure('時系列　8月3日の新築が起点（地目の変更は9月3日まで）')
ROWS = [('昭和43年8月', '丙川三郎が売買で丙土地を取得（それより前に建物はない）', GRAY),
        ('昭和43年10月30日', '丙川三郎の居宅が新築される', GRAY),
        ('平成8年3月1日', '丁商事が99番を駐車場にするとき、C点・D点の筆界を確認（確認書図面）', BLUE),
        ('平成12年8月31日', '居宅を増築。一部が乙土地の（ロ）部分に越境する', GRAY),
        ('平成21年1月', '乙山次郎が相続で乙土地を取得（甲区2番の所有権の移転は登記済み）', GREEN),
        ('平成21年8月3日', '乙山次郎が乙土地に建物を新築（畑 → 宅地）。物置も置く', RED),
        ('平成21年8月20日', '土地家屋調査士の甲野太郎が測量', GRAY),
        ('平成21年8月23日', '地積測量図の作成（答案用紙に印刷された日付）', GRAY),
        ('平成21年9月3日', '地目の変更の登記の期限（8月4日から数えて1か月後。不動産登記法第37条第1項）', RED)]
ax.plot([21.5, 21.5], [6, 94], color=GRAY, lw=3)
y = 90
for d, tx, col in ROWS:
    ax.plot([21.5], [y], 'o', ms=14, color=col)
    ax.text(19.5, y, d, fontsize=17, weight='bold', ha='right', va='center', color=col if col in (RED, GREEN, BLUE) else BLACK)
    ax.text(24, y, tx, fontsize=16.5, va='center', weight='bold' if col == RED else 'normal', color=RED if col == RED else BLACK)
    y -= 9.7
fig.text(0.5, 0.035, '8月20日の測量も、8月23日の作成日も、地目の変更の期限（9月3日）より前。相続の登記は申請より前に済んでいる。',
         ha='center', va='center', fontsize=16)
save_fixed(fig, 'H21_dai21mon_zu01_jikeiretsu.png', '時系列')

# ---- 注の仕分け ----
fig, ax = fixed_figure('注は2系統（問題文の注1〜7と、測量成果の表の下の注）')
LEFT = ('問題文の注', BLUE, [
    ('1', '座標は小数第3位を四捨五入', '毎年の注'),
    ('2', '訂正・加入・削除の押印・字数の記載は要らない', '毎年の注'),
    ('3', '地積測量図の辺長は小数第3位を四捨五入。\n座標値・求積・地積の表示は省略してよい', '今年も問5で使う'),
    ('4', '三角関数真数表', '今年だけ（検算のヒント）'),
    ('5', '乙土地の公差の表（市街地地域）', '今年だけ（問4）'),
    ('6', '書面を提出する方法で申請', '毎年の注'),
    ('7', '行為はすべて適法・書類も適法に作成', '毎年の注')])
RIGHT = ('測量成果の表の下の注', RED, [
    ('', '「このX軸は北方向と一致している」', 'X＝北（上）と読む')])
for x0, (head, col, items) in [(3, LEFT), (55, RIGHT)]:
    card(ax, x0, 5 if x0 == 3 else 66, 42, 86 if x0 == 3 else 25, col)
    ax.text(x0 + 2, 87, head, fontsize=21, weight='bold', color=col, va='center')
    yy = 80
    for num, body, tag in items:
        nl = body.count('\n') + 1
        if num:
            ax.text(x0 + 2, yy, f'注{num}', fontsize=16, weight='bold', va='top', color=col)
        ax.text(x0 + (8 if num else 2), yy, body, fontsize=14.5, va='top', linespacing=1.35)
        ax.text(x0 + 40, yy - 3.4 * nl - 0.8, tag, fontsize=13, va='top', ha='right', color=col)
        yy -= 3.4 * nl + 6.8
fig.text(0.5, 0.035, '記事では「問題文の注3」「測量成果の表の下の注」のように、どちらの注かを書き分ける。',
         ha='center', va='center', fontsize=16)
save_fixed(fig, 'H21_dai21mon_zu03_chu_shiwake.png', '注の仕分け')

# ---- 精度区分は地域で ----
fig, ax = fixed_figure('精度区分は地域で決まる（「乙土地」の呼び名で決めない）')
card(ax, 3, 36, 46, 55, BLUE)
ax.text(5, 87, '地域の区分と、誤差の限度（規則第10条第4項）', fontsize=17, weight='bold', color=BLUE, va='center')
for i, (area_, ku) in enumerate([('市街地地域（宅地が中心）', '精度区分 甲2 まで'), ('村落・農耕地域', '精度区分 乙1 まで'),
                                  ('山林・原野地域', '精度区分 乙3 まで')]):
    yy = 76 - i * 12.5
    ax.text(6, yy, area_, fontsize=16, va='center')
    ax.annotate('', xy=(33, yy), xytext=(29, yy), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=2))
    ax.text(34, yy, ku, fontsize=16, va='center', weight='bold', color=RED if i == 0 else BLACK)
ax.text(6, 41, '問題文の注5の表：甲2 0.82　乙1 2.26　乙3 9.43（単位㎡）', fontsize=14, va='center', color=GRAY)
card(ax, 53, 36, 44, 55, RED)
ax.text(55, 87, 'この問題の乙土地', fontsize=17, weight='bold', color=RED, va='center')
ax.text(56, 77, '市街地地域に属する（問題文の注5）', fontsize=16, va='center')
ax.text(56, 66, '→ 甲2　公差 0.82㎡', fontsize=19, weight='bold', color=RED, va='center')
ax.text(56, 53, '「乙土地」という呼び名につられて', fontsize=15.5, va='center', color=GRAY)
ax.text(56, 46.5, '乙1（2.26㎡）にしない', fontsize=15.5, va='center', color=GRAY)
ax.plot([56, 73], [46.5, 46.5], color=RED, lw=2.5)
card(ax, 3, 6, 94, 25, GREEN)
ax.text(5, 26.5, '登記記録の100㎡と実測の100.3367㎡の差は 0.3367㎡', fontsize=17, weight='bold', va='center')
ax.text(5, 18.5, '0.3367 ＜ 0.82（甲2）だから、公差の範囲内。', fontsize=16.5, va='center')
ax.text(5, 11.5, '精度区分を1つ読み違えると、地積の更正の要否の判断までずれる。', fontsize=15, va='center', color=GRAY)
fig.text(0.5, 0.035, '地域は問題文で決まる。この年度は乙1にしても結論は同じでも、手順（地域 → 精度区分 → 公差の表）を省かない。',
         ha='center', va='center', fontsize=15.5)
save_fixed(fig, 'H21_dai21mon_zu04_seido_kubun.png', '精度区分')

# ---- J点：登記記録の100㎡と実測100.3367㎡ ----
fig, (ax1, ax2) = new_figure('J点　登記記録の100㎡ではなく、実測の100.3367㎡で出す',
                             '交換後の乙土地H→J→L→Dの面積は、交換前の実測 100.3367㎡（登記記録の100㎡ではない）。k ＝ √((312.5 − 100.3367) ÷ 312.5) ＝ 0.8239…。\n'
                             '登記記録の100㎡で出すと k ＝ 0.8246… で J（509.04, 485.26）。0.03m南（X座標が小さい）にずれる。',
                             ncols=2, width_ratios=[0.8, 1.2])
ax1.axis('off')
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
card(ax1, 3, 52, 94, 40, GREEN)
ax1.text(6, 86, '実測の面積（座標から計算）', fontsize=16, weight='bold', color=GREEN, va='center')
ax1.text(6, 77, '乙土地 A→B→C→D', fontsize=15.5, va='center')
ax1.text(6, 68, '100.3367㎡', fontsize=24, weight='bold', color=GREEN, va='center')
ax1.text(6, 58, '→ k ＝ 0.8239…　J（509.07, 485.26）', fontsize=15, va='center')
card(ax1, 3, 6, 94, 40, GRAY)
ax1.text(6, 40, '登記記録の地積', fontsize=16, weight='bold', color=GRAY, va='center')
ax1.text(6, 31, '乙土地 100㎡', fontsize=15.5, color=GRAY, va='center')
ax1.text(6, 22, '→ k ＝ 0.8246…', fontsize=15.5, color=GRAY, va='center')
ax1.text(6, 12.5, 'J（509.04, 485.26）… 0.03m南に誤る', fontsize=15, color=RED, va='center')
ax1.set_title('どちらの面積で出すか', fontsize=16, weight='bold', pad=6)
zb = Zu(ax2, fontsize=15)
fit(ax2, [P(509.14, 485.1), P(508.96, 485.42)], margin=0.0, pad_aspect=True)
zb.line(P(509.2, 485.26), P(508.9, 485.26), color=BLACK, lw=1.8)
zb.north_arrow(length=0.08)
zb.point(J, 'concrete', size=10, color=RED)
zb.point(JW, 'dot', size=10, color=GRAY)
zb.dim_line(P(509.07, 485.36), P(509.04, 485.36), color=RED, lw=1.8)
zb.callout(J, 'J（509.07, 485.26）\n実測の100.3367㎡', dirs=(60, 40, 80), color=RED, dists=(80, 100, 120))
zb.callout(JW, '誤り（509.04, 485.26）\n登記記録の100㎡', dirs=(-60, -40, -80), color=GRAY, dists=(80, 100, 120))
zb.free_text(P(509.055, 485.395), '0.03m', fs=15, color=RED, offsets=((0, 10), (0, 14)))
ax2.set_title('Jのまわりの拡大（約0.3m四方）', fontsize=16, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [zb], 'H21_dai21mon_zu09_kiroku_hikaku.png')

# ---- 地目変更が先 ----
fig, ax = fixed_figure('地目変更が先　畑のまま分筆すると、あとでもう1回要る')
card(ax, 3, 66, 94, 27, BLUE)
ax.text(5, 88.5, '乙土地の地目の変わり目', fontsize=17, weight='bold', color=BLUE, va='center')
ax.text(5, 79, '登記記録：畑 100㎡（父がキャベツを栽培）', fontsize=16, va='center')
ax.annotate('', xy=(55, 79), xytext=(50, 79), arrowprops=dict(arrowstyle='-|>', color=RED, lw=2.5))
ax.text(56, 79, '平成21年8月3日に建物を新築 → 宅地', fontsize=16, weight='bold', color=RED, va='center')
ax.text(5, 71, '建物の敷地は宅地（準則第68条第3号）。所有権の登記名義人は、変更から1か月以内（9月3日まで）に申請する義務', fontsize=14.5, va='center')
card(ax, 3, 6, 45, 54, GRAY)
ax.text(5, 55.5, '誤り：畑のまま分筆する', fontsize=17, weight='bold', color=GRAY, va='center')
ax.text(6, 47, '100番1（畑）が3筆になる', fontsize=15.5, va='center')
ax.text(6, 39, '分筆後の3筆は、どれも畑のまま', fontsize=15.5, va='center')
ax.text(6, 31, '→ 3筆それぞれに地目の変更が要る', fontsize=15.5, weight='bold', color=RED, va='center')
ax.text(6, 21, '申請も、登録免許税の対象でない\n地目の変更の手間も3倍', fontsize=14, color=GRAY, va='center')
card(ax, 52, 6, 45, 54, GREEN)
ax.text(54, 55.5, '正しい：先に地目変更をする', fontsize=17, weight='bold', color=GREEN, va='center')
ax.text(55, 47, '1　土地地目変更登記（1回）', fontsize=15.5, va='center')
ax.text(55, 39, '2　土地分筆登記', fontsize=15.5, va='center')
ax.text(55, 31, '→ 分筆後の3筆は最初から宅地', fontsize=15.5, weight='bold', color=GREEN, va='center')
ax.text(55, 21, '分筆後の地積も、宅地の桁\n（小数第2位まで）で書ける', fontsize=14, color=GRAY, va='center')
fig.text(0.5, 0.035, '義務は8月3日から始まっている。分筆より先に、宅地への地目の変更を1回で済ませる。',
         ha='center', va='center', fontsize=16)
save_fixed(fig, 'H21_dai21mon_zu14_chimoku_saki.png', '地目変更が先')

# ---- 原因は②③（地積の表し方も変わる） ----
fig, ax = fixed_figure('原因は②③　地目が変わると、地積の表し方も変わる')
card(ax, 3, 52, 94, 40, BLUE)
ax.text(5, 87, '土地の表題部の欄の番号（準則第73条）', fontsize=17, weight='bold', color=BLUE, va='center')
for k_, (bx, lab, before, after, col) in enumerate([(8, '② 地目', '畑', '宅地', RED), (52, '③ 地積', '100', '100.00', RED)]):
    ax.text(bx, 77, lab, fontsize=17, weight='bold', va='center')
    ax.add_patch(plt.Rectangle((bx, 62), 14, 9, fc='white', ec=BLACK, lw=2))
    ax.text(bx + 7, 66.5, before, fontsize=18, ha='center', va='center')
    ax.annotate('', xy=(bx + 28, 66.5), xytext=(bx + 15.5, 66.5), arrowprops=dict(arrowstyle='-|>', color=RED, lw=3))
    ax.add_patch(plt.Rectangle((bx + 29, 62), 14, 9, fc='#fff0f0', ec=RED, lw=2.5))
    ax.text(bx + 36, 66.5, after, fontsize=18, ha='center', va='center', weight='bold', color=RED)
ax.text(5, 56, '地積の書き方（規則第100条）：宅地は小数第2位まで。宅地・鉱泉地以外で10㎡を超える土地は1㎡未満を切り捨て', fontsize=13.5, va='center')
card(ax, 3, 6, 44, 40, GRAY)
ax.text(5, 41, '誤り', fontsize=18, weight='bold', color=GRAY, va='center')
ax.text(6, 31, '②平成21年8月3日地目変更', fontsize=17, va='center', color=GRAY)
ax.text(6, 21, '地目の②だけ。地積の③を落とす', fontsize=15, va='center', color=RED)
card(ax, 53, 6, 44, 40, GREEN)
ax.text(55, 41, '正解', fontsize=18, weight='bold', color=GREEN, va='center')
ax.text(56, 31, '②③平成21年8月3日地目変更', fontsize=17, weight='bold', va='center')
ax.text(56, 21, '地目の②と、地積の③の両方を付ける', fontsize=15, va='center', color=GREEN)
fig.text(0.5, 0.035, '変更する事項の欄の番号を、登記原因の頭に付ける。畑の「100」が宅地の「100.00」の表し方に変わる。',
         ha='center', va='center', fontsize=16)
save_fixed(fig, 'H21_dai21mon_zu15_chiseki_hyouji.png', '②③')

# ---- 相続を証する情報は要らない ----
fig, ax = fixed_figure('相続を証する情報は要らない　相続の登記は申請より前に済んでいる')
card(ax, 3, 52, 94, 40, GREEN)
ax.text(5, 87.5, 'この問題（乙山次郎が申請する）', fontsize=17, weight='bold', color=GREEN, va='center')
X0 = [10, 38, 66]
for x0, lab, sub in [(X0[0], '平成21年1月', '父の死亡・相続\n乙山次郎が取得'), (X0[1], '申請より前', '甲区2番 所有権移転\n所有者 乙山次郎（登記済み）'),
                     (X0[2], '今回の申請', '登記名義人は乙山次郎本人\n相続人としての申請ではない')]:
    ax.add_patch(plt.Rectangle((x0 - 3, 58), 26, 22, fc='white', ec=GREEN, lw=2))
    ax.text(x0 + 10, 76, lab, fontsize=15.5, weight='bold', ha='center', va='center', color=GREEN)
    ax.text(x0 + 10, 66, sub, fontsize=13, ha='center', va='center', linespacing=1.5)
for xa in (X0[0] + 23.5, X0[1] + 23.5):
    ax.annotate('', xy=(xa + 3.2, 69), xytext=(xa, 69), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=2.5))
ax.text(5, 54.5, '→ 相続を証する情報（不動産登記令第7条第1項第4号）は付けない。添付は代理権限証明情報だけ（地目の変更）', fontsize=14.5,
        va='center', weight='bold')
card(ax, 3, 6, 94, 40, GRAY)
ax.text(5, 41, '比べる：登記名義人が亡くなったまま、相続人が申請する場合', fontsize=17, weight='bold', color=GRAY, va='center')
ax.text(6, 31, '表示に関する登記は、相続人が申請できる（不動産登記法第30条）', fontsize=15.5, va='center', color=GRAY)
ax.text(6, 22, '→ 申請人は「（被相続人　○○）　相続人」で、相続を証する情報を付ける', fontsize=15.5, va='center', color=GRAY)
ax.text(6, 13, '（この問題の乙山次郎は相続の登記が済んでいるので、当てはまらない）', fontsize=14, va='center', color=GRAY)
fig.text(0.5, 0.035, '「相続で取得した」という言葉につられず、登記記録（甲区2番）で名義が誰になっているかを時系列で確かめる。',
         ha='center', va='center', fontsize=16)
save_fixed(fig, 'H21_dai21mon_zu16_souzoku_fuyou.png', '相続を証する情報')

# ---- 離れた（ロ）と（ハ）は1筆にできない ----
fig, (ax,) = new_figure('離れた（ロ）と（ハ）は1筆にできない　分筆は3筆',
                        '（ハ）（A→B→I→H）は西の細い帯、（ロ）（K→C→L）は北東の三角形で、間に残る100番1（H→I→K→L→D）が入る。\n'
                        'つながっていない2つの部分は1筆にできない（合筆でも相互に接続していない土地はできない。不動産登記法第41条第1号）。\n'
                        'だから 100番1・100番3（ロ）・100番4（ハ）の3筆に分ける。')
z = Zu(ax, fontsize=15)
fit(ax, [P(499.4, 483.0), P(511.4, 499.0)], margin=0.02, pad_aspect=True)
z.poly(REM, color=BLUE, lw=2.0, fill=BLUE, alpha=0.18)
z.poly(RO, color=RED, lw=2.2, fill=RED, alpha=0.40)
z.poly(HA, color=PURPLE, lw=2.2, fill=PURPLE, alpha=0.45)
z.north_arrow(length=0.08)
for n in ('A', 'B', 'C', 'D', 'H', 'I', 'K', 'L'):
    pt(z, n, size=7)
for n, aw in [('A', A + P(0.5, 1)), ('B', B + P(-0.5, 1)), ('C', C + P(-0.5, -1)), ('D', D + P(0.5, -1)),
              ('H', H + P(0.5, -1)), ('I', I + P(0.5, -1)), ('K', K + P(0.5, 0)), ('L', L + P(0.5, -1))]:
    z.point_label(PTS[n], n, away=aw, fs=15)
z.free_text(centroid(REM), '残る部分\n100番1', fs=18, color=BLUE)
z.callout(centroid(RO), '（ロ）　100番3\n丙川さんへ渡す', dirs=(40, 20, 60), color=RED, dists=(70, 95, 120))
z.callout(A + (B - A) * 0.5 + (H - A) * 0.5, '（ハ）　100番4\n丙川さんへ渡す', dirs=(-165, 180, -150), color=PURPLE, dists=(60, 85, 110))
z.dim_line(I + P(0.57, -0.18), K + P(0.57, -0.18), color=GRAY, lw=1.4)
z.callout(I + (K - I) * 0.5 + P(0.57, -0.18), '（ハ）と（ロ）の間は\n100番1（IK 6.56m）', dirs=(-100, -120, -80), color=GRAY, dists=(50, 70, 90))
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu18_hanare_3hitsu.png')

# ---- 原因の欄は行ごと ----
fig, ax = fixed_figure('原因の欄は行ごと　100番1は③、新しい土地は「から分筆」')
card(ax, 3, 6, 94, 87, BLUE)
ax.text(5, 88, '答案用紙（問4）の「登記の原因及び日付」の2の欄（3行）', fontsize=17, weight='bold', color=BLUE, va='center')
GYO = [('1行目', '100番1（残る部分）', '③100番1、100番3、100番4に分筆', RED),
       ('2行目', '100番3（（ロ）部分）', '100番1から分筆', BLACK),
       ('3行目', '100番4（（ハ）部分）', '100番1から分筆', BLACK)]
for i, (g, tochi, gen, col) in enumerate(GYO):
    yy = 77 - i * 14
    ax.add_patch(plt.Rectangle((6, yy - 5.5), 88, 11, fc='white', ec=BLACK, lw=1.8))
    ax.text(8, yy, g, fontsize=15.5, weight='bold', va='center')
    ax.text(22, yy, tochi, fontsize=15.5, va='center', color=GRAY)
    ax.text(50, yy, gen, fontsize=17, weight='bold', va='center', color=col)
ax.text(8, 33, '1行目の③：分筆で、100番1の地積が変わるから（地積は表題部の③の欄）', fontsize=15.5, va='center')
ax.text(8, 24, '①は付けない：元の地番の100番1が残るので、地番は変わらない（準則第74条第1項）', fontsize=15.5, va='center')
ax.text(8, 15, '2行目・3行目：新しくできる土地の登記記録に、どの土地から分筆したかを書く', fontsize=15.5, va='center')
fig.text(0.5, 0.035, '支号のない本番を分筆するとき（元の地番が変わる）は①③。ここは100番1が残るので③だけ。',
         ha='center', va='center', fontsize=16)
save_fixed(fig, 'H21_dai21mon_zu20_genin_gyou.png', '原因の欄')

# ---- 抵当権消滅承諾証明情報 ----
fig, ax = fixed_figure('分筆後の（ロ）（ハ）の抵当権を消す承諾　添付情報に入れる')
card(ax, 3, 55, 94, 38, BLUE)
ax.text(5, 88, '分筆前（乙区1番に抵当権）', fontsize=17, weight='bold', color=BLUE, va='center')
ax.text(6, 78, '乙土地（100番1）全体に抵当権が付いている', fontsize=15.5, va='center')
ax.text(6, 70, '問題文：分筆後の（ロ）及び（ハ）部分の1番抵当権が消滅することについて、', fontsize=14.5, va='center')
ax.text(6, 63.5, '抵当権者の承諾書一式を受領した', fontsize=14.5, va='center', weight='bold', color=RED)
for x0, lab, sub, col in [(3, '100番1（残る）', '抵当権は\n残る', BLACK), (36, '100番3（ロ）', '抵当権が\n消える', RED), (69, '100番4（ハ）', '抵当権が\n消える', RED)]:
    card(ax, x0, 8, 28, 40, col, fc='#fff8f8' if col == RED else '#f7f7f7')
    ax.text(x0 + 14, 40.5, lab, fontsize=16.5, weight='bold', ha='center', va='center', color=col)
    ax.text(x0 + 14, 27, sub, fontsize=17, ha='center', va='center', linespacing=1.6, color=col)
ax.text(6, 59, '→ 承諾を証する情報を、分筆の申請と一緒に出す（不動産登記法第40条、規則第104条第1項第1号）', fontsize=14.5,
        va='center', weight='bold')
fig.text(0.5, 0.035, '承諾書には抵当権者が記名押印し、印鑑証明書を付ける（不動産登記令第19条）。添付情報：地積測量図・抵当権消滅承諾証明情報・代理権限証明情報。',
         ha='center', va='center', fontsize=15)
save_fixed(fig, 'H21_dai21mon_zu21_teitouken.png', '抵当権')

# ---- 登録免許税 ----
fig, ax = fixed_figure('登録免許税　分筆後の個数で数える（3筆で3,000円）')
card(ax, 3, 45, 94, 48, GREEN)
ax.text(5, 88, '分筆：分筆後の土地の個数1個につき1,000円（登録免許税法別表第一の一（十三）イ）', fontsize=16.5, weight='bold', color=GREEN, va='center')
for x0, lab in [(10, '100番1'), (40, '100番3（ロ）'), (70, '100番4（ハ）')]:
    ax.add_patch(plt.Rectangle((x0, 60), 22, 18, fc='white', ec=GREEN, lw=2.2))
    ax.text(x0 + 11, 72, lab, fontsize=15.5, ha='center', va='center', weight='bold')
    ax.text(x0 + 11, 65, '1,000円', fontsize=17, ha='center', va='center', color=GREEN)
ax.text(50, 52, '1,000円 × 3筆 ＝ 3,000円', fontsize=21, weight='bold', ha='center', va='center', color=RED)
card(ax, 3, 6, 45, 33, GRAY)
ax.text(5, 34, '誤り', fontsize=17, weight='bold', color=GRAY, va='center')
ax.text(6, 25, '新しく付く地番だけ数える\n（100番3と100番4で2,000円）', fontsize=15, va='center', color=GRAY, linespacing=1.6)
ax.text(6, 13, '元の地番が残る100番1も数える', fontsize=14, va='center', color=RED)
card(ax, 52, 6, 45, 33, BLUE)
ax.text(54, 34, '地目の変更', fontsize=17, weight='bold', color=BLUE, va='center')
ax.text(55, 25, '登録免許税はかからない', fontsize=16, va='center', weight='bold')
ax.text(55, 14.5, '答案用紙に欄はないが、\n知識として押さえる', fontsize=14, va='center', color=GRAY, linespacing=1.5)
fig.text(0.5, 0.035, '書面で申請するので、納付の方法は収入印紙。分筆後の個数で数える点は、合筆（合筆後の個数）と対にして覚える。',
         ha='center', va='center', fontsize=15.5)
save_fixed(fig, 'H21_dai21mon_zu22_touroku_menkyozei.png', '登録免許税')

# ---- 見取図の（イ）と地積測量図の（イ） ----
fig, (ax1, ax2) = new_figure('（イ）の意味が違う　見取図の（イ）と、地積測量図の（イ）',
                             '見取図の（イ）は丙土地の一部（J→I→K）。地積測量図では、分筆後の各土地に（イ）（ロ）（ハ）の符号を付け、（イ）は分筆後に残る100番1。\n'
                             '丙土地の一部のJ点・（イ）部分は、乙土地の分筆の地積測量図に描かない。',
                             ncols=2, width_ratios=[1.0, 1.0])
za = Zu(ax1, fontsize=14)
fit(ax1, [A, B, C, D, J, P(511.4, 484.0), P(504.0, 476.0)], margin=0.12, pad_aspect=True)
za.poly(OTSU, color=GRAY, lw=1.4)
za.poly(II, color=ORANGE, lw=2.0, fill=ORANGE, alpha=0.45)
za.poly(RO, color=RED, lw=1.6, fill=RED, alpha=0.30)
za.poly(HA, color=PURPLE, lw=1.6, fill=PURPLE, alpha=0.30)
za.north_arrow(length=0.07)
za.free_text(CO + P(-1.2, 0), '乙土地', fs=16, color=GRAY)
za.callout(centroid(II), '（イ）＝丙土地の一部\n（J・I・K）', dirs=(-150, -165, -135, 180, 150), color=ORANGE, dists=(80, 105, 130))
za.callout(centroid(RO), '（ロ）', dirs=(30, 15, 45), color=RED, dists=(50, 70, 90))
za.callout(A + (B - A) * 0.5 + (H - A) * 0.5, '（ハ）', dirs=(-165, 180, -150), color=PURPLE, dists=(50, 70, 90))
ax1.set_title('見取図（問題文）', fontsize=16, weight='bold', pad=6)
zb = Zu(ax2, fontsize=14)
fit(ax2, [A, B, C, D, P(511.4, 484.0), P(504.0, 476.0)], margin=0.12, pad_aspect=True)
zb.poly([A, B, I, K, C, L, D, H], color=BLACK, lw=2.0)
zb.line(H, I, color=BLACK, lw=2.0)
zb.line(K, L, color=BLACK, lw=2.0)
zb.north_arrow(length=0.07)
zb.free_text(centroid(REM), '100－1\n（イ）', fs=18)
zb.callout(centroid(RO), '100－3（ロ）', dirs=(30, 15, 45, 60, 0, -30), dists=(40, 60, 80, 100))
zb.callout(A + (B - A) * 0.5 + (H - A) * 0.5, '100－4（ハ）', dirs=(-165, 180, -150), dists=(50, 70, 90))
ax2.set_title('地積測量図（問5）', fontsize=16, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H21_dai21mon_zu24_kigou_i.png')

print('重なりの合計:', len(ALL_PROBLEMS))
