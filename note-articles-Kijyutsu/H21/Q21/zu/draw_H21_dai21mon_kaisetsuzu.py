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
fig, (ax,) = new_figure('図1　北を上にして描き直した全体図',
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
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：筆界点の裏付け（確認書図面と乙土地の面積）
# =====================================================================
fig, (ax,) = new_figure('図2　筆界点は確認書と乙土地の面積で裏付ける',
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
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu02_hikkai_uradzuke.png')

# =====================================================================
# 図3：H点（E点から2.50m）
# =====================================================================
fig, (ax,) = new_figure('図3　問1の準備　H点は E点から東へ2.50m',
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
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu03_H_haba.png')

# =====================================================================
# 図4：I点（BCとHJの交点）
# =====================================================================
fig, (ax,) = new_figure('図4　問1　I点は BC と HJ（Y＝485.26）の交点',
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
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu04_I_kouten.png')

# =====================================================================
# 図5：J点（交換後の乙土地と延長線の交点Pの相似）
# =====================================================================
fig, (ax1, ax2) = new_figure('図5　問1　J点は、交換後の乙土地を元の面積にする相似比で',
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
ALL_PROBLEMS += save(fig, [za, zb], 'H21_dai21mon_zu05_J_souji.png')

# =====================================================================
# 図6：L点（同じ相似比）と交換後の乙土地の検算
# =====================================================================
fig, (ax,) = new_figure('図6　問1　L点も同じ相似比 k で出る',
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
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu06_L_souji.png')

# =====================================================================
# 図7：問2（ロ）部分 K・C・L
# =====================================================================
fig, (ax,) = new_figure('図7　問2　（ロ）部分は K→C→L の三角形で 2.43㎡',
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
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu07_ro_menseki.png')

# =====================================================================
# 図8：問3（ハ）部分と等積の確かめ
# =====================================================================
fig, (ax1, ax2) = new_figure('図8　問3　（ハ）部分は 3.82㎡。（イ）＝（ロ）＋（ハ）の確かめ',
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
ALL_PROBLEMS += save(fig, [za, zb], 'H21_dai21mon_zu08_ha_toseki.png')

# =====================================================================
# 図9：J点の別解（2次方程式）
# =====================================================================
fig, (ax,) = new_figure('図9　J点の別解　（イ）＝（ロ）＋（ハ）を h の2次方程式で',
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
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu09_J_betsukai.png')

# =====================================================================
# 図10：公差の判定（地積の更正は不要）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図10　問4　地積の更正は要らない（甲2の公差0.82㎡の範囲）', fontsize=24, weight='bold', y=0.95)
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
path = os.path.join(OUT, 'H21_dai21mon_zu10_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図10: 数直線の判定図（固定配置）\n  →', path)

# =====================================================================
# 図11：問4 登記の順番（整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図11　問4　地目変更が先、分筆は3筆')
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
path = os.path.join(OUT, 'H21_dai21mon_zu11_touki_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図11: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図12：分筆後の区画と地番
# =====================================================================
fig, (ax,) = new_figure('図12　問4　分筆後の区画と地番',
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
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu12_bunpitsu_chiban.png')

# =====================================================================
# 図13：問5 地積測量図の完成見本
# =====================================================================
fig, (ax,) = new_figure('図13　問5　地積測量図（100番1の分筆）の完成見本',
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
ALL_PROBLEMS += save(fig, [z], 'H21_dai21mon_zu13_chiseki_sokuryouzu.png')

# =====================================================================
# 図14：本番で解く順番（整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図14　本番で解く順番（J点・L点と地積測量図がいちばん時間を食う）')
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
path = os.path.join(OUT, 'H21_dai21mon_zu14_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図14: 整理図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
