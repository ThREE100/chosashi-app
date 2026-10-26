"""平成20年度 第21問（土地）会話形式note記事の解説図を、座標値から作図する（2026-10-26に27枚へ。画像の中に図番は入れない）。

`../prompt_H20_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../H23/Q21/zu/draw_H23_dai21mon_kaisetsuzu.py`。

6番1と6番2の境の線（E点から北北西へ延びる線）は、問題文に座標がないので、見取図の向きを模式的に短く描く（図の中で「位置は模式」と書く）。
4番・7番・6番1・6番2・道路は、座標のある筆界の外側に地番の文字だけを置く。

実行: python3 note-articles-Kijyutsu/H20/Q21/zu/draw_H20_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, dms, to_dms, area, chiseki, radial  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
INK_BLUE = '#1a3a8f'

# ---- 座標（問題文のK市基準点・測量成果、記事で求めた点） ------------------
T1, T2, T3 = P(32.74, 3.31), P(13.73, 1.85), P(3.54, 30.35)
A, C, D = P(31.63, 9.85), P(7.03, 28.98), P(32.26, 31.00)
T101R = radial(T2, T1, 10.71, dms(150, 21, 32))              # 調整前のT101′
T3R = radial(T101R, T2, 23.91, dms(116, 25, 26))             # 計算で出したT3′
ERR = T3 - T3R                                               # 補正量（正しい値 − 計算した値）
T101X = T101R + ERR * 10.71 / (10.71 + 23.91)                # 調整後（丸める前）
T101 = r2(T101X)
BX = radial(T101, T2, 6.22, dms(24, 44, 42))
B = r2(BX)
E = r2(A + (D - A) * 4 / 9)
W = (E - B) / (C - B)
FX = B + (C - B) * (W + W.conjugate()) / 2
F = r2(FX)
# 誤りの点
T101_SIGN = T101R - ERR * 10.71 / 34.62                      # 補正量の向きを逆に
T101_2391 = T101R + ERR * 23.91 / 34.62                      # 23.91で配った
BW_DIR = T101 + cmath.rect(6.22, cmath.phase(T2 - T101R) + dms(24, 44, 42))   # 調整前の向きを使った
BW_RAW = radial(T101R, T2, 6.22, dms(24, 44, 42))           # 調整前のT101′から放射
EW = r2(A + (D - A) * 4 / 5)                                  # 5分の4進めた
FW = r2(B + (C - B) * (E.imag - B.imag) / (C.imag - B.imag))  # Eから真南に下ろした

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('T101', T101, P(4.04, 6.43)), ('B', B, P(10.26, 6.37)), ('E', E, P(31.91, 19.25)),
                     ('F', F, P(8.89, 15.96)), ('T101_SIGN', r2(T101_SIGN), P(4.05, 6.41)),
                     ('T101_2391', r2(T101_2391), P(4.03, 6.44)), ('BW_DIR', r2(BW_DIR), P(10.26, 6.38)),
                     ('BW_RAW', r2(BW_RAW), P(10.26, 6.36)), ('EW', EW, P(32.13, 26.77)), ('FW', FW, P(8.42, 19.25))]:
    assert abs(got - want) < 1e-9, (n, got, want)
assert to_dms(cmath.phase(T1 - T2)) == '4°23′30.45″'
assert to_dms(cmath.phase(T1 - T2) + dms(150, 21, 32)) == '154°45′02.45″'
assert to_dms(cmath.phase(T2 - T101R)) == '−25°14′57.55″'
assert to_dms(cmath.phase(T2 - T101R) + dms(116, 25, 26)) == '91°10′28.45″'
assert to_dms(cmath.phase(T2 - T101)) == '−25°17′52.31″'
assert to_dms(cmath.phase(T2 - T101) + dms(24, 44, 42)) == '−0°33′10.31″'
assert to_dms(cmath.phase(T2 - T101R) + dms(24, 44, 42)) == '−0°30′15.55″'
assert f'{ERR.real:.4f}' == '-0.0131' or f'{ERR.real:.5f}'.startswith('-0.0131')
assert f'{abs(ERR):.4f}'[:6] == '0.0296'
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = [(A, B, '21.65'), (B, F, '9.69'), (F, C, '13.15'), (C, D, '25.31'), (D, E, '11.76'), (E, A, '9.40')]
BUNKATSU = (E, F, '23.25')
for p, q, want in SIDES + [BUNKATSU]:
    assert d2(p, q) == want, (p, q, d2(p, q), want)
RO = [A, B, F, E]                            # （ロ）5番2
I_ = [E, F, C, D]                            # （イ）5番1
GO = [A, B, C, D]                            # 5番（分筆前）
assert f'{area(I_):.5f}' == '300.79265' and chiseki(area(I_)) == 300.79
assert f'{area(RO):.5f}' == '212.58635' and chiseki(area(RO)) == 212.58
assert f'{area(GO):.3f}' == '513.379'
assert f'{area([A, B, FW, E]):.4f}' == '251.2274' and f'{area([E, FW, C, D]):.4f}' == '262.1516'
assert abs(((C - B).conjugate() * (F - E)).real) < 0.05
# 誤りの点の向き：FWはFより東、EWはEより東、T101_SIGNは正しいT101より北西
assert FW.imag > F.imag + 3 and EW.imag > E.imag + 7
assert T101_SIGN.real > T101X.real and T101_SIGN.imag < T101X.imag
print('数値の照合: すべて一致')


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


def fixed_figure(title, caption):
    setup_font()
    f = plt.figure(figsize=(16, 12), dpi=100)
    f.patch.set_facecolor('white')
    f.suptitle(title, fontsize=24, weight='bold', y=0.965)
    a = f.add_axes([0.03, 0.10, 0.94, 0.80])
    a.set_xlim(0, 100)
    a.set_ylim(0, 100)
    a.axis('off')
    f.text(0.5, 0.035, caption, ha='center', va='center', fontsize=16)
    return f, a


def bearing(p, q):
    """pからqへの方向角（北から時計回り、度。0〜360）。"""
    b = math.degrees(cmath.phase(q - p))
    return b + 360 if b < 0 else b


def ext(p, q, k):
    """pからqの向きへ、pから長さkの点。"""
    return p + (q - p) / abs(q - p) * k


KIND = {'A': 'metal', 'B': 'metal', 'C': 'concrete', 'D': 'concrete', 'E': 'concrete', 'F': 'dot'}
N6 = ext(E, E + cmath.rect(1, math.radians(-28)), 4.5)     # 6番1と6番2の境の線（向きは模式。北北西へ）
INNER = centroid(GO)
ALL_PROBLEMS = []

# =====================================================================
# 図1：全体像
# =====================================================================
fig, (ax,) = new_figure('北を上にして描き直した全体像',
                        'A→Dはほぼ東西だが、Xが31.63から32.26へ少し上がる。B→Cも東へ行くほど南へ下がる（軸に平行な辺はない）。\n'
                        '基準点は、T2が西、T101が南西、T3が南の外で、T1は北西の外。6番1と6番2の境の線は、座標がないので向きは模式。')
z = Zu(ax, fontsize=14)
fit(ax, [T1, T2, T3, T101, A, B, C, D, N6, ext(A, D, -3.0), ext(D, A, -3.0), ext(B, C, -3.0), ext(C, B, -3.0)],
    margin=0.07, pad_aspect=True)
z.poly(RO, fill=ORANGE, lw=2.4)
z.poly(I_, fill=BLUE, lw=2.4)
z.line(ext(A, D, -3.0), A, lw=1.6)
z.line(D, ext(D, A, -3.0), lw=1.6)
z.line(ext(B, C, -3.0), B, lw=1.6)
z.line(C, ext(C, B, -3.0), lw=1.6)
z.line(E, N6, lw=1.6, ls='--', color=GRAY)
z.line(E, F, color=RED, lw=2.6)
z.north_arrow()
z.free_text(centroid(RO), '（ロ）\n南野二郎が\n買った部分', fs=15, offsets=((0, 0), (0, 16), (0, -16)))
z.free_text(centroid(I_), '（イ）', fs=15, offsets=((0, 0), (0, 16), (0, -16)))
for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F')]:
    z.point(p, KIND[n], color=RED if n in 'BEF' else BLACK)
    z.point_label(p, n, away=INNER, color=RED if n in 'BEF' else BLACK)
for p, n in [(T1, 'T1'), (T2, 'T2'), (T3, 'T3'), (T101, 'T101')]:
    z.point(p, 'kijun', color=RED if n == 'T101' else BLACK)
    z.point_label(p, n, away=INNER, color=RED if n == 'T101' else BLACK)
z.free_text(P(35.0, 13.5), '6－2', fs=15, color=GRAY, offsets=((0, 0), (0, 14), (-16, 0)))
z.free_text(P(35.4, 25.0), '6－1', fs=15, color=GRAY, offsets=((0, 0), (0, 14), (16, 0)))
z.free_text(P(20.0, 4.2), '4', fs=16, color=GRAY, offsets=((0, 0), (0, 14), (-16, 0)))
z.free_text(P(20.0, 34.0), '7', fs=16, color=GRAY, offsets=((0, 0), (0, 14), (16, 0)))
z.free_text(P(5.8, 19.0), '道　路', fs=15, color=GRAY, offsets=((0, 0), (0, -14), (20, 0)))
z.callout(N6, '6番1と6番2の境（位置は模式）', dirs=(150, 170, 130), color=GRAY, fs=13, dists=(40, 60, 80))
ALL_PROBLEMS += save(fig, [z], 'H20_dai21mon_zu03_zentaizu.png')

# =====================================================================
# 図2：問1 結合トラバース T2→T101′→T3′（全体と、T3のまわりの拡大）
# =====================================================================
fig, (ax1, ax2) = new_figure('問1　結合トラバース（T2 → T101′ → T3′）と閉合誤差',
                             'T101′ ＝ T2 ＋ 10.71∠(4°23′30.45″ ＋ 150°21′32″)。T2→T101′は154°45′02.45″（180° − 25°14′57.55″。真数表の25°14′58″）。\n'
                             'T3′ ＝ T101′ ＋ 23.91∠(−25°14′57.55″ ＋ 116°25′26″)。T101′→T3′は91°10′28.45″（真数表の1°10′28″ ＝ 91°10′28″ − 90°）。\n'
                             '成果表のT3とのずれ T3 − T3′ ＝ −0.0131… ＋ 0.0265…i（長さ0.0296…、約3cm）。これが閉合誤差（右の拡大）。',
                             ncols=2, width_ratios=[1.15, 0.85])
za = Zu(ax1, fontsize=14)
fit(ax1, [T1, T2, T3, T101R, B, P(8.0, -3.0)], margin=0.08, pad_aspect=True)
za.poly(GO, color=GRAY, lw=1.2, fill=GRAY, alpha=0.08)
za.line(T2, T1, color=BLUE, lw=1.8)
za.line(T2, T101R, color=RED, lw=2.6)
za.line(T101R, T3R, color=RED, lw=2.6)
za.line(T2, T2 + P(4.0, 0), color=GRAY, lw=1.2, ls='--')
za.angle_arc(T2, 3.4, 0, bearing(T2, T1), color=BLUE)
za.angle_arc(T2, 2.3, bearing(T2, T1), bearing(T2, T1) + 150 + 21 / 60 + 32 / 3600, color=RED)
za.angle_arc(T101R, 2.4, bearing(T101R, T2), bearing(T101R, T2) + 116 + 25 / 60 + 26 / 3600, color=RED)
za.north_arrow()
for p, n in [(T1, 'T1'), (T2, 'T2'), (T3, 'T3')]:
    za.point(p, 'kijun')
    za.point_label(p, n, away=T101R if n != 'T1' else T2)
za.point(T101R, 'dot', color=RED, size=9)
za.callout(T101R, 'T101′（調整前）\n4.0432… ＋ 6.4184…i', dirs=(-120, -140, -100, 180), color=RED, dists=(50, 70, 90))
za.edge_label(T2, T101R, '10.71', T3, color=RED, fs=14)
za.edge_label(T101R, T3R, '23.91', T2 + P(8, 0), color=RED, fs=14)
za.free_text(T2 + P(3.0, 0), '方向角\n4°23′30.45″', color=BLUE, fs=13, ha='right', offsets=((-14, 0), (-24, 10), (-30, -10)))
za.free_text(T2 + P(-1.2, 0), '150°21′32″\n（右回り）', color=RED, fs=13, ha='right', offsets=((-14, 0), (-20, -12), (-24, 10)))
za.free_text(T101R + P(1.8, 1.8), '116°25′26″（右回り）', color=RED, fs=13, ha='left', offsets=((14, 10), (24, 22), (30, 0)))
za.free_text(centroid(GO), '5番', fs=15, color=GRAY, offsets=((0, 0), (0, 16)))
zb = Zu(ax2, fontsize=14)
fit(ax2, [(T3 + T3R) / 2 + P(-0.032, -0.032), (T3 + T3R) / 2 + P(0.032, 0.032)], margin=0.02, pad_aspect=True)
zb.line(T3R, T3, color=RED, lw=2.4)
zb.line(T3R + (T3R - T101R) / abs(T3R - T101R) * (-0.03), T3R, color=RED, lw=1.4, ls='--')
zb.north_arrow()
zb.point(T3, 'kijun')
zb.callout(T3, 'T3（成果表）\n3.54 ＋ 30.35i', dirs=(-90, -110, -70, -130), dists=(50, 70, 90))
zb.point(T3R, 'dot', color=RED, size=11)
zb.callout(T3R, 'T3′（T101′から計算）\n3.5531… ＋ 30.3234…i', dirs=(90, 70, 110, 50), color=RED, dists=(50, 70, 90))
zb.free_text((T3 + T3R) / 2, 'T3 − T3′\n−0.0131… ＋ 0.0265…i', color=RED, fs=13, offsets=((70, 30), (80, 44), (70, -36), (-80, -30)))
ax2.set_title('T3のまわりの拡大（約7cm四方）', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H20_dai21mon_zu04_T101_ketsugou.png')

# =====================================================================
# 補正量の向き（T3 − T3′）と配る割合（10.71 ÷ 34.62）
# =====================================================================
def arrow(ax, p, q, color, lw=2.4, style='-|>', ls='-', ms=18):
    ax.annotate('', xy=xy(q), xytext=xy(p), arrowprops=dict(arrowstyle=style, color=color, lw=lw, ls=ls, mutation_scale=ms,
                                                                shrinkA=0, shrinkB=0), zorder=4)


# ---- zu05：補正量の向き ----
fig, (ax1, ax2) = new_figure('問1　補正量の向きは「正しい値 − 計算した値」（T3 − T3′）',
                             '補正量 ＝ T3 − T3′ ＝ −0.0131… ＋ 0.0265…i（南東へ約3cm）。T3′をT3へ戻す向きに、T101′も動かす。\n'
                             'T101 ＝ T101′ ＋ 補正量 × 10.71 ÷ 34.62 → 南へ4mm・東へ8mm動いて（4.04, 6.43）。\n'
                             '向きを逆にして T3′ − T3 を足すと、T101′から北西へ動いて（4.05, 6.41）。正しい点から北西へ約2cmずれる。',
                             ncols=2, width_ratios=[0.9, 1.1])
za = Zu(ax1, fontsize=14)
c1 = (T3 + T3R) / 2
fit(ax1, [c1 + P(-0.032, -0.032), c1 + P(0.032, 0.032)], margin=0.02, pad_aspect=True)
arrow(ax1, T3R, T3, RED)
za.north_arrow()
za.point(T3, 'kijun')
za.callout(T3, 'T3（成果表）\n3.54 ＋ 30.35i', dirs=(-90, -110, -70, -130), dists=(50, 70, 90))
za.point(T3R, 'dot', color=GRAY, size=11)
za.callout(T3R, 'T3′（計算）\n3.5531… ＋ 30.3234…i', dirs=(90, 70, 110, 50), color=GRAY, dists=(50, 70, 90))
za.free_text(c1, '補正量 T3 − T3′\n（T3′からT3へ）', color=RED, fs=14, offsets=((75, 10), (85, 24), (-85, 10)))
ax1.set_title('T3のまわりの拡大（約6cm四方）', fontsize=17, weight='bold', pad=6)
zb = Zu(ax2, fontsize=14)
fit(ax2, [T101R + P(-0.026, -0.026), T101R + P(0.026, 0.026)], margin=0.02, pad_aspect=True)
arrow(ax2, T101R, T101X, RED)
arrow(ax2, T101R, T101_SIGN, GRAY, ls='--')
zb.north_arrow()
zb.point(T101R, 'dot', color=BLACK, size=10)
zb.callout(T101R, 'T101′（調整前）', dirs=(20, 0, 40), dists=(45, 60, 75))
zb.point(T101X, 'dot', color=RED, size=12)
zb.callout(T101X, 'T101（調整後）\n4.0391… ＋ 6.4266…i\n→（4.04, 6.43）', dirs=(-100, -80, -120), color=RED, dists=(45, 60, 75))
zb.point(T101_SIGN, 'dot', color=GRAY, size=11)
zb.callout(T101_SIGN, '向きを逆にした誤り\n（4.05, 6.41）', dirs=(150, 130, 170, 110), color=GRAY, dists=(45, 60, 75))
ax2.set_title('T101のまわりの拡大（約5cm四方）', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H20_dai21mon_zu05_hosei_muki.png')

# ---- zu06：配る割合 ----
fig, (ax1, ax2) = new_figure('問1　コンパスの法則：T2からの距離に比例して配る（10.71 ÷ 34.62）',
                             'T101までの距離10.71 ÷ 全長（10.71 ＋ 23.91 ＝ 34.62）＝ 0.3093…。T3で全部、T101では約31％だけ直す。\n'
                             '後の辺の23.91 ÷ 34.62 ＝ 0.6906…（約69％）で配ると（4.03, 6.44）で、正しい点より約1cm先へ行き過ぎる。\n'
                             'T101 ＝ T101′ ＋ (T3 − T3′) × 10.71 ÷ (10.71 ＋ 23.91) ＝ 4.0391… ＋ 6.4266…i → T101（4.04, 6.43）',
                             ncols=2, width_ratios=[0.85, 1.15])
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
ax1.axis('off')
X0, X1 = 8, 92
xs = lambda d: X0 + (X1 - X0) * d / 34.62  # noqa: E731
ax1.plot([X0, X1], [62, 62], color=BLACK, lw=2.4)
for d, lab, sub in [(0, 'T2', '0'), (10.71, 'T101', '10.71'), (34.62, 'T3', '34.62')]:
    ax1.plot([xs(d)], [62], 'o', ms=12, color=RED if lab == 'T101' else BLACK)
    ax1.text(xs(d), 67, lab, ha='center', fontsize=18, weight='bold', color=RED if lab == 'T101' else BLACK)
    ax1.text(xs(d), 55, sub, ha='center', va='top', fontsize=15)
ax1.text(50, 90, 'T2からの距離の合計', ha='center', fontsize=18, weight='bold')
ax1.plot([X0, X1], [30, 30 + 22], color=RED, lw=2.0)
ax1.plot([xs(10.71), xs(10.71)], [30, 30 + 22 * 10.71 / 34.62], color=RED, lw=2.0, ls='--')
ax1.plot([X1, X1], [30, 52], color=RED, lw=2.0, ls='--')
ax1.text(X1 - 1, 49, '全部\n(T3 − T3′)', ha='right', va='top', fontsize=14, color=RED)
ax1.text(xs(10.71) + 2, 34, '× 10.71 ÷ 34.62（約31％）', ha='left', va='center', fontsize=14, color=RED)
ax1.text(50, 18, '直す量は、出発点からの距離に比例する', ha='center', fontsize=16)
ax1.text(50, 11, '（T101は10.71 ÷ 34.62、T3は全部）', ha='center', fontsize=16)
zb = Zu(ax2, fontsize=14)
fit(ax2, [T101R, T101X, T101_2391, T101R + P(0.010, -0.012), T101_2391 + P(-0.004, 0.010)], margin=0.40, pad_aspect=True)
arrow(ax2, T101R, T101X, RED)
arrow(ax2, T101X, T101_2391, GRAY, ls='--')
zb.north_arrow()
zb.point(T101R, 'dot', color=BLACK, size=10)
zb.callout(T101R, 'T101′（調整前）', dirs=(60, 40, 80), dists=(45, 60, 75))
zb.point(T101X, 'dot', color=RED, size=12)
zb.callout(T101X, 'T101（調整後）\n約31％\n→（4.04, 6.43）', dirs=(-150, -130, -170), color=RED, dists=(45, 60, 75))
zb.point(T101_2391, 'dot', color=GRAY, size=11)
zb.callout(T101_2391, '23.91で配った誤り\n約69％\n（4.03, 6.44）', dirs=(-30, -10, -50, -70), color=GRAY, dists=(45, 60, 75))
ax2.set_title('T101のまわりの拡大（約4cm四方）', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [zb], 'H20_dai21mon_zu06_compass_wariai.png')


# =====================================================================
# 図4：問2 B点（調整後のT101から後視の向きを取り直す）
# =====================================================================
fig, (ax1, ax2) = new_figure('問2　B点の求め方（調整後のT101からT2を後視して放射）',
                             '後視の向きは調整後のT101から取り直す：arg(T2 − T101) ＝ −25°17′52.31″（真数表の25°17′52″）。\n'
                             '24°44′42″を足して −0°33′10.31″（真数表の0°33′10″）、6.22m進んでB（10.26, 6.37）。\n'
                             '調整前の向き −25°14′57.55″ を使うと（10.26, 6.38）、調整前のT101′から放射すると（10.26, 6.36）。',
                             ncols=2, width_ratios=[1.0, 1.0])
za = Zu(ax1, fontsize=14)
fit(ax1, [T2, T101, B, P(12.0, 10.5), P(1.0, -1.0)], margin=0.08, pad_aspect=True)
za.line(ext(B, A, 3.0), B, color=GRAY, lw=1.4)
za.line(B, ext(B, C, 4.0), color=GRAY, lw=1.4)
za.line(T101, T2, color=BLUE, lw=1.8)
za.line(T101, T101 + P(7.2, 0), color=GRAY, lw=1.2, ls='--')
za.line(T101, B, color=RED, lw=2.8)
za.angle_arc(T101, 2.8, bearing(T101, T2), 360, color=BLUE)
za.angle_arc(T101, 1.9, bearing(T101, T2), bearing(T101, T2) + 24 + 44 / 60 + 42 / 3600, color=RED)
za.north_arrow()
za.point(T2, 'kijun')
za.point_label(T2, 'T2', away=T101)
za.point(T101, 'kijun', color=RED)
za.point_label(T101, 'T101（4.04, 6.43）', away=T101 + P(-1, 1), color=RED)
za.point(B, 'metal', color=RED)
za.callout(B, 'B（10.26, 6.37）', dirs=(20, 0, 40), color=RED, dists=(50, 70, 90))
za.edge_label(T101, B, '6.22', T2, color=RED, fs=14)
za.free_text(T101 + P(2.4, -0.3), '方向角\n−25°17′52.31″', color=BLUE, fs=13, ha='right', offsets=((-40, 0), (-50, 12), (-60, -8), (-70, 20)))
za.free_text(T101 + P(2.0, 0.6), '24°44′42″（右回り）', color=RED, fs=13, ha='left', offsets=((14, 4), (22, 14), (30, -6)))
za.free_text(ext(B, A, 2.2), '5番の西の筆界（A→B）', color=GRAY, fs=13, ha='left', offsets=((14, 0), (20, 12), (20, -12)))
zb = Zu(ax2, fontsize=14)
cb = (BX + BW_DIR + BW_RAW) / 3
fit(ax2, [cb + P(-0.013, -0.013), cb + P(0.013, 0.013)], margin=0.02, pad_aspect=True)
zb.line(P(cb.real - 0.012, 6.375), P(cb.real + 0.004, 6.375), color=GRAY, lw=1.2, ls='--')
zb.line(P(cb.real - 0.012, 6.365), P(cb.real + 0.004, 6.365), color=GRAY, lw=1.2, ls='--')
zb.north_arrow()
zb.point(BX, 'dot', color=RED, size=12)
zb.callout(BX, '正しいB\n10.2597… ＋ 6.3699…i\n→（10.26, 6.37）', dirs=(-90, -70, -110), color=RED, dists=(50, 70, 90))
zb.point(BW_DIR, 'dot', color=GRAY, size=11)
zb.callout(BW_DIR, '調整前の向きの誤り\n6.3752… →（10.26, 6.38）', dirs=(110, 90, 130), color=GRAY, dists=(70, 90, 110))
zb.point(BW_RAW, 'dot', color=GRAY, size=11)
zb.callout(BW_RAW, 'T101′から放射した誤り\n→（10.26, 6.36）', dirs=(70, 90, 50), color=GRAY, dists=(60, 80, 100))
zb.free_text(P(cb.real - 0.012, 6.375), 'Y ＝ 6.375\n四捨五入の境目', color=GRAY, fs=12, va='top', offsets=((0, -6), (0, -16)))
zb.free_text(P(cb.real - 0.012, 6.365), 'Y ＝ 6.365\n四捨五入の境目', color=GRAY, fs=12, va='top', offsets=((0, -6), (0, -16)))
ax2.set_title('Bのまわりの拡大（約2.4cm四方）', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H20_dai21mon_zu07_B_housha.png')

# =====================================================================
# 図5：問2 E点（A→Dを4：5に内分）
# =====================================================================
fig, (ax,) = new_figure('問2　E点の求め方（A→Dを4：5に内分）',
                        'AE：ED ＝ 4：5 なので、ADを9等分した4つ目。E ＝ A ＋ (D − A) × 4 ÷ 9 ＝ 31.91 ＋ 19.25i（割り切れる）。\n'
                        '検算：AE ＝ 9.4041…、ED ＝ 11.7552…、9.4041… ÷ 11.7552… ＝ 0.8（＝ 4 ÷ 5）。\n'
                        '5分の4進めると（32.13, 26.77）で、それは AE：AD ＝ 4：5 の点（D点の4m少し手前まで東に寄る）。')
z = Zu(ax, fontsize=14)
fit(ax, [A, D, ext(A, B, 3.5), ext(D, C, 3.5), P(35.0, 20.0)], margin=0.06, pad_aspect=True)
z.line(A, ext(A, B, 3.5), color=GRAY, lw=1.4)
z.line(D, ext(D, C, 3.5), color=GRAY, lw=1.4)
z.line(A, D, lw=2.6)
for k in range(1, 9):
    q = A + (D - A) * k / 9
    n = (D - A) / abs(D - A) * 1j * 0.35
    z.line(q - n, q + n, color=GRAY, lw=1.2)
z.north_arrow()
z.point(A, 'metal')
z.point_label(A, 'A', away=A + P(-1, 1))
z.point(D, 'concrete')
z.point_label(D, 'D', away=D + P(-1, -1))
z.point(E, 'concrete', color=RED)
z.callout(E, 'E（31.91, 19.25）', dirs=(90, 110, 70), color=RED, dists=(55, 75, 95))
z.point(EW, 'dot', color=GRAY, size=9)
z.callout(EW, '5分の4の誤り（32.13, 26.77）', dirs=(-60, -80, -40), color=GRAY, dists=(55, 75, 95))
z.edge_label(A, E, 'AE 9.40（9分の4）', D + P(-5, 0), color=RED, fs=14, dists=(16, 22, 30))
z.edge_label(E, D, 'ED 11.76（9分の5）', A + P(-5, 0), color=BLUE, fs=14, dists=(16, 22, 30))
z.free_text(P(29.6, 20.0), '5番（南へ続く）', fs=15, color=GRAY, offsets=((0, 0), (0, -16)))
ALL_PROBLEMS += save(fig, [z], 'H20_dai21mon_zu08_E_naibun.png')

# =====================================================================
# 図6：問2 F点（Eから直線BCへの垂線の足）
# =====================================================================
fig, (ax,) = new_figure('問2　F点の求め方（Eから直線BCへの垂線の足）',
                        'C − B ＝ −3.23 ＋ 22.61i：BCは東へ22.61m進む間に南へ3.23m下がる（東西の線ではない）。\n'
                        'w ＝ (E − B) ÷ (C − B) ＝ 0.4242… − 1.0181…i、F ＝ B ＋ (C − B) × (w ＋ Conjg(w)) ÷ 2 ＝ 8.8898 ＋ 15.9614i → F（8.89, 15.96）。\n'
                        '検算：Conjg(C − B) × (F − E) ＝ −0.0323 ＋ 531.1089i（実部がほぼ0で直角）。Eから真南に下ろすと（8.42, 19.25）で3.3m東にずれる。')
z = Zu(ax, fontsize=14)
fit(ax, GO + [P(4.5, 15.0)], margin=0.08, pad_aspect=True)
z.poly(GO, color=GRAY, lw=1.4, fill=GRAY, alpha=0.08)
z.line(B, C, lw=2.6)
z.line(E, F, color=RED, lw=2.6)
z.line(E, FW, color=GRAY, lw=1.6, ls='--')
z.right_angle(F, C, E, size=0.9, color=RED)
z.north_arrow()
for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E')]:
    z.point(p, KIND[n])
    z.point_label(p, n, away=INNER)
z.point(F, 'dot', color=RED, size=10)
z.callout(F, 'F（8.89, 15.96）', dirs=(-110, -130, -90), color=RED, dists=(50, 70, 90))
z.point(FW, 'dot', color=GRAY, size=9)
z.callout(FW, 'Eから真南の誤り（8.42, 19.25）', dirs=(-60, -40, -80), color=GRAY, dists=(55, 75, 95))
z.callout(B + (C - B) * 0.2, 'C − B ＝ −3.23 ＋ 22.61i', dirs=(-120, -140, -100), color=BLUE, dists=(60, 80, 100))
z.edge_label(E, F, 'F − E ＝ −23.02 − 3.29i', C, color=RED, fs=13, ts=(0.5, 0.4, 0.6), dists=(14, 20, 28))
ALL_PROBLEMS += save(fig, [z], 'H20_dai21mon_zu09_F_suisen.png')

# =====================================================================
# 図7：問3の前提 （ロ）と（イ）の面積（対角線2本）
# =====================================================================
fig, (ax1, ax2) = new_figure('問3の前提　（ロ）と（イ）の面積（対角線2本で出す）',
                             '四角形PQRSの倍面積 ＝ Conjg(R − P) × (S − Q) のiの係数。宅地なので小数第2位未満を切り捨てる。\n'
                             '（ロ）Conjg(F − A) × (E − B) ＝ −413.6242 − 425.1727i → 212.58635 → 212.58㎡\n'
                             '（イ）Conjg(C − E) × (D − F) ＝ −435.1064 − 601.5853i → 300.79265 → 300.79㎡。5番全体は513.379㎡',
                             ncols=2, width_ratios=[0.9, 1.1])
for axx, pts, diag, fillc, name, val in [
        (ax1, RO, [(A, F), (B, E)], ORANGE, '（ロ）', '212.58635\n→ 212.58㎡'),
        (ax2, I_, [(E, C), (F, D)], BLUE, '（イ）', '300.79265\n→ 300.79㎡')]:
    zz = Zu(axx, fontsize=14)
    fit(axx, pts, margin=0.10, pad_aspect=True)
    zz.poly(pts, fill=fillc, lw=2.4)
    for p, q in diag:
        zz.line(p, q, color=RED, lw=1.6, ls='--')
    zz.north_arrow()
    cc = centroid(pts)
    for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F')]:
        if p in pts:
            zz.point(p, KIND[n] if n != 'F' else 'dot', color=RED if n in 'BEF' else BLACK)
            zz.point_label(p, n, away=cc)
    zz.free_text(cc, f'{name}\n{val}', fs=15, offsets=[(dx, dy) for dy in (0, 50, -50, 90, -90, 130, -130) for dx in (0, -50, 50)])
    axx.set_title(f'{name}　対角線 {"A→F と B→E" if name == "（ロ）" else "E→C と F→D"}', fontsize=17, weight='bold', pad=6)
    ALL_PROBLEMS += zz.check_overlaps('図7 ' + name)
path = os.path.join(OUT, 'H20_dai21mon_zu10_menseki.png')
fig.savefig(path, dpi=100, facecolor='white')
print('  →', path)

# =====================================================================
# 図8：公差の数直線（固定配置）
# =====================================================================
fig, ax = fixed_figure('問3の前提　地積更正は要らない（市街地地域の甲2）',
                       '分筆前の512.66㎡を基準にした甲2の公差は2.21㎡（調査結果の6の表）。分筆後の合計513.37㎡との差0.71㎡は範囲の内側（準則第72条第1項）。')
lo, hi = 510.0, 515.5
sx = lambda v: 8 + 84 * (v - lo) / (hi - lo)  # noqa: E731
ax.add_patch(plt.Rectangle((sx(512.66 - 2.21), 44), sx(512.66 + 2.21) - sx(512.66 - 2.21), 12, color=GREEN, alpha=0.22))
ax.plot([sx(lo), sx(hi)], [50, 50], color=BLACK, lw=2.4)
for v in [510, 511, 512, 513, 514, 515]:
    ax.plot([sx(v), sx(v)], [48.5, 51.5], color=BLACK, lw=1.4)
    ax.text(sx(v), 40, f'{v}', ha='center', va='top', fontsize=15)
ax.plot([sx(512.66)], [50], 'o', ms=14, color=BLACK)
ax.text(sx(512.66), 70, '登記記録\n512.66㎡', ha='center', fontsize=17, weight='bold')
ax.annotate('', xy=(sx(512.66), 53), xytext=(sx(512.66), 68), arrowprops=dict(arrowstyle='-|>', lw=1.6))
ax.plot([sx(513.37)], [50], 'o', ms=14, color=RED)
ax.text(sx(513.37) + 0.5, 78, '分筆後の合計\n513.37㎡（300.79 ＋ 212.58）', ha='left', fontsize=17, weight='bold', color=RED)
ax.annotate('', xy=(sx(513.37), 53), xytext=(sx(513.37) + 2, 76), arrowprops=dict(arrowstyle='-|>', lw=1.6, color=RED))
ax.annotate('', xy=(sx(513.37), 30), xytext=(sx(512.66), 30), arrowprops=dict(arrowstyle='<|-|>', lw=1.8, color=RED))
ax.text((sx(512.66) + sx(513.37)) / 2, 26, '差 0.71㎡', ha='center', va='top', fontsize=17, color=RED, weight='bold')
ax.text(sx(512.66 - 2.21), 60, '510.45', ha='center', fontsize=14, color=GREEN)
ax.text(sx(512.66 + 2.21), 60, '514.87', ha='center', fontsize=14, color=GREEN)
ax.text(50, 14, '甲2の公差 ± 2.21㎡ の範囲（緑）の内側 → 地積更正は不要。登記の目的は「土地分筆登記」', ha='center', fontsize=18,
        weight='bold', color=GREEN)
ax.text(50, 6, '丸める前の513.379㎡で比べても差0.719㎡で同じ結論。甲1（0.89㎡）の列で比べる必要はない', ha='center', fontsize=15)
path = os.path.join(OUT, 'H20_dai21mon_zu12_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図8: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図9：相続関係図（固定配置）
# =====================================================================
fig, ax = fixed_figure('問3　西川四郎の相続人は和子・二郎・八郎の3人',
                       '子の七郎は相続の放棄で初めから相続人でない（民法第939条）。父母も死亡しているので兄弟姉妹へ。\n'
                       '兄弟姉妹の代襲は子まで（民法第889条第2項は第887条第2項だけを準用し、再代襲の第887条第3項は準用しない）。')


def person(x, y, name, sub='', col=BLACK, fc='#f7f7f7', w=13, h=8):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0.4', fc=fc, ec=col, lw=2.0))
    ax.text(x, y + (1.3 if sub else 0), name, ha='center', va='center', fontsize=17, weight='bold', color=col)
    if sub:
        ax.text(x, y - 2.2, sub, ha='center', va='center', fontsize=12.5, color=col)


def link(x1, y1, x2, y2, ls='-', col=GRAY):
    ax.plot([x1, x2], [y1, y2], color=col, lw=1.8, ls=ls)


# 1段目：美子＝一郎（離婚）、一郎＝弘子
person(14, 88, '西川美子', '一郎と離婚', GRAY)
person(40, 88, '西川一郎', '平成12年死亡', GRAY)
person(66, 88, '西川弘子', '平成14年死亡', GRAY)
link(20.5, 88, 33.5, 88, ls=':')
link(46.5, 88, 59.5, 88)
# 2段目：二郎（美子との子）、三郎・四郎・五郎（弘子との子）
link(27, 88, 27, 75)
link(12, 75, 27, 75)
link(12, 75, 12, 70)
link(53, 88, 53, 75)
link(34, 75, 88, 75)
for x in (34, 58, 88):
    link(x, 75, x, 70)
person(12, 66, '西川二郎', '父だけ同じ兄→相続人', RED, '#fff5f5', w=18)
person(34, 66, '西川三郎', '平成8年死亡', GRAY)
person(58, 66, '西川四郎', '被相続人（H19.6.1死亡）', BLACK, '#eef3fb', w=20)
person(88, 66, '西川五郎', '平成15年死亡', GRAY)
person(77, 50, '西川和子', '配偶者→相続人', RED, '#fff5f5', w=16)
link(68, 64, 69, 52)
# 3段目
person(34, 44, '西川六郎', '欠格', GRAY)
person(56, 32, '西川七郎', '相続の放棄（H19.7.1）', GRAY, w=19)
person(90, 32, '西川八郎', '五郎を代襲→相続人', RED, '#fff5f5', w=16)
link(34, 62, 34, 48)
link(56, 62, 56, 36)
link(88, 62, 90, 36)
# 4段目
person(34, 22, '西川九郎', '再代襲しない', GRAY)
link(34, 40, 34, 26)
ax.text(13, 22, '兄弟姉妹の相続は\nおい・めいまで', ha='center', va='center', fontsize=14, color=GRAY)
ax.text(4, 10, '相続人（被代位者）：西川和子・西川二郎・西川八郎', ha='left', fontsize=19, weight='bold', color=RED)
ax.text(4, 3, '花子（三郎の妻）・陽子（五郎の妻）・悦子（六郎の妻）・美子は四郎の相続人ではない', ha='left', fontsize=15, color=GRAY)
path = os.path.join(OUT, 'H20_dai21mon_zu17_souzoku_kankei.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図9: 相続関係図（固定配置）\n  →', path)

# =====================================================================
# 図10：代位の関係図（固定配置）
# =====================================================================
fig, ax = fixed_figure('問3　買主の南野二郎が、相続人3人に代位して分筆を申請する',
                       '分筆は所有権の登記名義人（死亡していればその相続人。不動産登記法第30条）しか申請できない（同法第39条第1項）。\n'
                       '買主は自分の所有権移転登記請求権を守るため、相続人に代わって申請する（民法第423条、不動産登記令第3条第4号）。')
BOX10 = [
    (4, 62, 40, 30, '登記名義人（被相続人）', BLACK, ['西川四郎', '平成19年6月1日死亡', '5番の所有権の登記名義人'], []),
    (56, 62, 40, 30, '相続人3人（被代位者）', RED, ['西川和子・西川二郎・西川八郎', '不動産登記法第30条で', '分筆を申請できる立場'], [0]),
    (56, 10, 40, 36, '買主（代位者＝申請人）', BLUE, ['南野二郎', '平成19年5月1日に（ロ）を', '西川四郎から買い受けた', '代位原因：平成19年5月1日売買の', '所有権移転登記請求権'], [0, 3, 4]),
    (4, 10, 40, 36, '添付書類に加わるもの', PURPLE, ['代位原因証書', '（不動産登記令第7条第1項第3号）', '相続証明書', '（同項第4号）'], [0, 2]),
]
for x, y, w, hh, head, col, lines, red in BOX10:
    ax.add_patch(FancyBboxPatch((x, y), w, hh, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=col, lw=2.0))
    ax.text(x + 2, y + hh - 4, head, fontsize=19, weight='bold', va='center', color=col)
    for i, t in enumerate(lines):
        ax.text(x + 3, y + hh - 11 - i * 5.4, t, fontsize=16, va='center', color=RED if i in red else BLACK)
ax.annotate('', xy=(55, 77), xytext=(45, 77), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=GRAY))
ax.text(50, 80.5, '相続', ha='center', fontsize=15, color=GRAY)
ax.annotate('', xy=(76, 60.5), xytext=(76, 47.5), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=BLUE))
ax.text(77.5, 54, '代わって申請', ha='left', va='center', fontsize=15, color=BLUE)
ax.annotate('', xy=(45, 28), xytext=(55, 28), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=PURPLE))
path = os.path.join(OUT, 'H20_dai21mon_zu19_daii.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図10: 代位の関係図（固定配置）\n  →', path)

# =====================================================================
# 図11：分筆前と分筆後の区画と地番
# =====================================================================
fig, (ax1, ax2) = new_figure('問3　分筆前と分筆後の区画と地番',
                             '支号のない本番の5番を分筆すると、各筆に支号を付ける（準則第67条第1項第4号本文）。（イ）5番1は「①③5番1、5番2に分筆」、\n'
                             '（ロ）5番2は「5番から分筆」。1行目の地積は登記記録の512.66（地積更正をしないので、計算の513.37は書かない）。',
                             ncols=2)
for axx, after in [(ax1, False), (ax2, True)]:
    zz = Zu(axx, fontsize=14)
    fit(axx, GO, margin=0.12, pad_aspect=True)
    if after:
        zz.poly(RO, fill=ORANGE, lw=2.4)
        zz.poly(I_, fill=BLUE, lw=2.4)
        zz.line(E, F, color=RED, lw=2.6)
    else:
        zz.poly(GO, fill=GRAY, lw=2.4, alpha=0.15)
    zz.north_arrow()
    for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D')] + ([(E, 'E'), (F, 'F')] if after else []):
        zz.point(p, KIND[n], color=RED if n in 'EF' else BLACK)
        zz.point_label(p, n, away=INNER, color=RED if n in 'EF' else BLACK)
    if after:
        zz.free_text(centroid(RO), '（ロ）5番2\n212.58㎡\n南野二郎が\n買った部分', fs=15, offsets=((0, 0), (0, 16), (0, -16)))
        zz.free_text(centroid(I_), '（イ）5番1\n300.79㎡', fs=15, offsets=((0, 0), (0, 16), (0, -16)))
        axx.set_title('分筆後（申請書の2行目・3行目）', fontsize=17, weight='bold', pad=6)
    else:
        zz.free_text(INNER, '5番　宅地\n512.66㎡\n（登記記録）', fs=16, offsets=((0, 0), (0, 16), (0, -16)))
        axx.set_title('分筆前（申請書の1行目）', fontsize=17, weight='bold', pad=6)
    ALL_PROBLEMS += zz.check_overlaps('図11')
path = os.path.join(OUT, 'H20_dai21mon_zu22_chiban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('  →', path)

# =====================================================================
# 図26：問4 地積測量図の完成見本（黒、塗りなし）。試験の答案用紙（touan_youshi/p2.png）の問4の枠の中に、
#   縦横とも実際の縮尺（1/250で 1m ＝ 4mm）で描く。答案用紙は縮小されたA3横（1400px ＝ 420mm、1px ＝ 0.3mm）。
#   印刷済み：「問4」「地積測量図」の表題、地番・土地の所在の欄の枠、折り目の印、作成者の（略）と
#   「（平成20年8月24日作成）」、申請人の（略）、縮尺 1/250。枠は約32cm × 19cm。画像の中に図番は入れない
# =====================================================================
from matplotlib.patches import Rectangle  # noqa: E402
setup_font()
FW_, FH_ = 16, 13.0
fig = plt.figure(figsize=(FW_, FH_), dpi=100)
fig.patch.set_facecolor('white')
SX0, SW, SY0 = 70.0, 1110.0, 85.0           # 答案用紙の画像（1400×989px）のうち、描く範囲の左端・幅・上端（px）
K_ = FW_ * 100 / SW                          # 画像の1px → この図の何px
fx = lambda x: (x - SX0) / SW                # noqa: E731
fy = lambda y: 1 - (y - SY0) * K_ / (FH_ * 100)   # noqa: E731


def frect(x0, y0, x1, y1, lw=1.6):
    fig.add_artist(Rectangle((fx(x0), fy(y1)), fx(x1) - fx(x0), fy(y0) - fy(y1), transform=fig.transFigure, fill=False,
                             edgecolor=BLACK, lw=lw))


def fline(x0, y0, x1, y1, lw=1.4):
    fig.add_artist(plt.Line2D([fx(x0), fx(x1)], [fy(y0), fy(y1)], transform=fig.transFigure, color=BLACK, lw=lw))


def ftext(x, y, s_, **kw):
    kw.setdefault('ha', 'center')
    kw.setdefault('va', 'center')
    fig.text(fx(x), fy(y), s_, **kw)


frect(87, 142, 1160, 789, lw=1.8)                        # 図を描く枠
fline(624, 142, 624, 158)                                # 折り目の印（上・下）
fline(624, 773, 624, 789)
ftext(90, 106, '問4', fontsize=17, weight='bold', ha='left')
frect(652, 100, 870, 142)                                # 地番の欄
fline(744, 100, 744, 142)
ftext(698, 121, '地　　番', fontsize=14)
ftext(807, 121, '5番1、5番2', fontsize=17, weight='bold')
frect(652, 142, 1160, 186)                               # 土地の所在の欄
fline(744, 142, 744, 186)
ftext(698, 164, '土地の所在', fontsize=14)
ftext(760, 164, 'K市B町一丁目', fontsize=17, weight='bold', ha='left')
ftext(1010, 122, '地　積　測　量　図', fontsize=20)
frect(86, 789, 588, 842)                                 # 作成者の欄
fline(172, 789, 172, 842)
ftext(128, 815, '作 成 者', fontsize=14)
ftext(380, 815, '（略）', fontsize=14)
ftext(583, 828, '（平成20年8月24日作成）', fontsize=13, ha='right')
frect(657, 789, 1160, 844)                               # 申請人・縮尺の欄
fline(742, 789, 742, 844)
ftext(699, 817, '申 請 人', fontsize=14)
ftext(890, 817, '（略）', fontsize=15)
fline(1040, 789, 1040, 844)
fline(1078, 789, 1078, 844)
ftext(1059, 817, '縮尺', fontsize=13)
fline(1078, 842, 1158, 792, lw=1.0)
ftext(1105, 803, '1', fontsize=13)
ftext(1138, 828, '250', fontsize=13)
# 図を描く範囲：枠の内側（所在の欄の下、折り目の印の間）。縦横とも 1m ＝ 4mm（1/250）
AX0, AX1, AY0, AY1 = 92.0, 1156.0, 190.0, 784.0
ax = fig.add_axes([fx(AX0), fy(AY1), fx(AX1) - fx(AX0), fy(AY0) - fy(AY1)])
PPM = 4.0 / 0.3 * K_                          # 1m が図の何px（答案用紙A3横＝420mm、1400px）
ax.set_xlim(16.4 - (AX1 - AX0) * K_ / PPM / 2, 16.4 + (AX1 - AX0) * K_ / PPM / 2)
ax.set_ylim(17.3 - (AY1 - AY0) * K_ / PPM / 2, 17.3 + (AY1 - AY0) * K_ / PPM / 2)
ax.set_aspect('equal', adjustable='datalim')
ax.axis('off')
z = Zu(ax, fontsize=13)
z.poly(RO, lw=2.2)
z.poly(I_, lw=2.2)
z.line(ext(A, D, -2.0), A, lw=1.4)
z.line(D, ext(D, A, -2.0), lw=1.4)
z.line(ext(B, C, -2.0), B, lw=1.4)
z.line(C, ext(C, B, -2.0), lw=1.4)
z.line(E, E + (N6 - E) * 0.6, lw=1.4)
z.north_arrow()
for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F')]:
    z.point(p, KIND[n] if n != 'F' else 'dot')
for p, q, n in SIDES:
    z.edge_label(p, q, n, INNER, fs=13)
z.edge_label(E, F, '23.25', C, fs=13, outward=True)
for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F')]:
    z.point_label(p, n, away=INNER, weight='normal')
for p, n in [(T1, 'T1'), (T2, 'T2'), (T3, 'T3'), (T101, 'T101')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=INNER, weight='normal')
z.free_text(centroid(RO), '（ロ）\n5－2', fs=15, offsets=((0, 0), (0, 16), (0, -16)))
z.free_text(centroid(I_), '（イ）\n5－1', fs=15, offsets=((0, 0), (0, 16), (0, -16)))
z.free_text(P(34.6, 13.5), '6－2', fs=13, offsets=((0, 0), (0, 12), (-12, 0)))
z.free_text(P(35.0, 25.0), '6－1', fs=13, offsets=((0, 0), (0, 12), (12, 0)))
z.free_text(P(22.0, 5.0), '4', fs=14, offsets=((0, 0), (0, 12), (-12, 0)))
z.free_text(P(21.0, 32.4), '7', fs=14, offsets=((0, 0), (0, 12), (12, 0)))
z.free_text(P(6.2, 18.5), '道　路', fs=13, offsets=((0, 0), (0, -12), (20, 0)))
z.free_text(P(3.0, 38.0), 'A・B：金属標　C・D・E：コンクリート杭\nF：金属鋲　T1・T2・T3：K市基準点\nT101：多角点　（単位：m）',
            fs=12, ha='left', offsets=((0, 0), (0, -10), (10, 0), (0, 20)))
fig.text(0.5, 0.075,
         '印刷済み：「問4」「地積測量図」、地番・土地の所在の欄の枠、折り目の印、作成者の（略）と「（平成20年8月24日作成）」、申請人の（略）、縮尺 1/250\n'
         '書くもの：地番（5番1、5番2）、土地の所在（K市B町一丁目）、図（縮尺1/250で 1m ＝ 4mm。基準点T1・T2・T3と多角点T101まで入れても枠に楽に収まる）、辺長7本、\n'
         '（イ）（ロ）の符号と地番、境界標の記号と凡例、方位記号、隣接地の地番と道路、基準点・多角点の位置と名称、単位（m）\n'
         '書かないもの：各筆界点の座標値・求積の方法・地積（問題文の注3）。辺長は小数第3位を四捨五入（DE 11.7552…→11.76、EA 9.4041…→9.40）',
         ha='center', va='center', fontsize=14, linespacing=1.6)
ALL_PROBLEMS += save(fig, [z], 'H20_dai21mon_zu26_sokuryouzu.png')


# =====================================================================
# 図13：本番で解く順番（固定配置）
# =====================================================================
fig, ax = fixed_figure('本番で解く順番（T101が要るのはB点から後）',
                       'T101 → B → F → 面積 と一本の鎖でつながる。鎖に入らない申請書の大半とE点を先に終わらせてから、T101に取りかかる。')
STEPS = [('①', '相続人の確定と申請書の地積以外の欄', '和子・二郎・八郎、代位者の南野二郎、代位原因、添付書類、登録免許税2,000円、所在、1行目、地番と原因', BLACK),
         ('②', 'E点', 'A→Dの9分の4。T101と関係なく、すぐ出る（31.91, 19.25）', BLACK),
         ('③', 'T101（コンパスの法則）', 'T101′・T3′を放射し、補正量 T3 − T3′ に 10.71 ÷ 34.62 を掛けて足す（4.04, 6.43）', RED),
         ('④', 'B点', '調整後のT101から後視の向きを取り直す（10.26, 6.37）', RED),
         ('⑤', 'F点', 'Eから直線BCへの垂線の足（8.89, 15.96）。真南に下ろさない', RED),
         ('⑥', '面積と公差', '（イ）300.79・（ロ）212.58、差0.71は甲2の2.21の内側で地積更正は不要', RED),
         ('⑦', '辺長7本と地積測量図', '21.65・9.69・13.15・25.31・11.76・9.40・23.25。基準点と多角点T101も描く', RED)]
for k, (no, head, body, col) in enumerate(STEPS):
    y = 90 - k * 13.2
    ax.add_patch(FancyBboxPatch((5, y - 4.8), 90, 9.6, boxstyle='round,pad=0.5', fc='#fff5f5' if col == RED else '#f7f7f7',
                                ec=col, lw=2.0))
    ax.text(8, y + 1.7, f'{no}　{head}', fontsize=19, weight='bold', va='center', color=col)
    ax.text(12, y - 2.4, body, fontsize=15, va='center', color=BLACK)
    if k < len(STEPS) - 1:
        ax.annotate('', xy=(50, y - 8.2), xytext=(50, y - 5.6), arrowprops=dict(arrowstyle='-|>', lw=2.0, color=GRAY))
path = os.path.join(OUT, 'H20_dai21mon_zu27_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図13: 整理図（固定配置）\n  →', path)

# =====================================================================
# 固定配置の整理図（座標を使わない図）。重なりの自動検査の対象外なので、PNGを目で確かめる
# =====================================================================
def fbox(ax, x, y, w, h, head, col, lines=(), red=(), gray=(), fs=15, hfs=19, fc='#f7f7f7', lh=5.4, top=10.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.6', fc=fc, ec=col, lw=2.0))
    ax.text(x + 2, y + h - 4, head, fontsize=hfs, weight='bold', va='center', color=col)
    for i, t in enumerate(lines):
        c = RED if i in red else (GRAY if i in gray else BLACK)
        ax.text(x + 3, y + h - top - i * lh, t, fontsize=fs, va='center', color=c)


def darrow(ax, x0, y0, x1, y1, col=GRAY, lw=2.2):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle='-|>', lw=lw, color=col))


def fsave(fig, name, label):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print(f'[重なり検査] {label}: 整理図（固定配置。目視で確認）\n  →', path)


# ---- zu01：全体の時系列 ----
fig, ax = fixed_figure('全体の時系列（売買は、西川四郎の死亡の1か月前）',
                       '代位原因の日付は売買の日（5月1日）、死亡の日（6月1日）は相続が始まった日。目盛りは一定ではない。')
ax.text(2, 95, '親族の死亡（相続人の確定に使う）', fontsize=18, weight='bold', color=GRAY, va='center')
ROWA = [(10, '平成8年', '三郎が死亡'), (30, '平成12年', '父 一郎が死亡'), (50, '平成14年', '母 弘子が死亡'), (70, '平成15年', '五郎が死亡')]
ax.annotate('', xy=(97, 78), xytext=(3, 78), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=GRAY))
for x, d, t in ROWA:
    ax.plot([x], [78], 'o', ms=11, color=GRAY)
    ax.text(x, 85, d, ha='center', fontsize=16, weight='bold', color=GRAY)
    ax.text(x, 72, t, ha='center', va='top', fontsize=15, color=BLACK)
ax.text(2, 60, '本件土地の経過', fontsize=18, weight='bold', color=BLACK, va='center')
ROWB = [(8, '平成2年5月14日', '西川四郎が5番を\n売買で取得\n（6月7日受付）', BLACK),
        (31, '平成19年5月1日', '南野二郎が（ロ）を\n2,000万円で買う', RED),
        (52, '平成19年6月1日', '西川四郎が死亡\n遺産分割協議なし', BLACK),
        (73, '平成19年7月1日', '西川七郎が\n相続を放棄', BLACK),
        (92, '平成20年8月24日', '申請\n（答案用紙に印刷）', BLACK)]
ax.annotate('', xy=(99, 40), xytext=(2, 40), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=BLACK))
for x, d, t, col in ROWB:
    ax.plot([x], [40], 'o', ms=12, color=col)
    ax.text(x, 47, d, ha='center', fontsize=15, weight='bold', color=col)
    ax.text(x, 33, t, ha='center', va='top', fontsize=14, color=BLACK)
ax.annotate('', xy=(52, 14), xytext=(31, 14), arrowprops=dict(arrowstyle='<|-|>', lw=2.0, color=RED))
ax.text(41.5, 9, '1か月。売買が先', ha='center', va='top', fontsize=17, weight='bold', color=RED)
fsave(fig, 'H20_dai21mon_zu01_jikeiretsu.png', '全体の時系列')

# ---- zu02：注の仕分け ----
fig, ax = fixed_figure('注は4か所と、注ではない調査結果に分かれている',
                       '赤は今年だけ効く記述、灰色は毎年ほぼ同じ記述。記事では「問題文の注3」「測量成果の表の下の注2」のように、どこの注かを添えて書く。')
NB = [(2, 52, '見取図の注', BLACK,
       ['A〜Eは筆界点、T1〜T3はK市基準点', 'T101はK市基準点を基に測った多角点', 'E点：ADを4：5に内分する点', 'F点：Eを通りBCに直交する線とBCの交点', 'AとBは金属標、ほかはコンクリート杭'], [2, 3], [0]),
      (35.5, 52, '親族関係の注', BLACK,
       ['記載のある者だけが親族', '特に記載のない者は生存している', '→ 相続人の確定に使う'], [2], []),
      (69, 52, '測量成果の表の下の注1〜3', BLACK,
       ['注1　測量は基準点に基づく', '注2　水平角は後視を0度として右回り', '注3　座標値・距離の単位はメートル'], [1], [0, 2]),
      (2, 5, '問題文の注1〜4', BLACK,
       ['注1　座標は小数第3位を四捨五入', '注2　訂正の方法', '注3　辺長は四捨五入、座標値・求積・', '　　　地積は省略可、基準点・多角点は描く', '注4　地図は500分の1、測量図は250分の1'], [2, 3, 4], [0, 1]),
      (35.5, 5, '調査結果の5〜7（注ではない）', BLACK,
       ['5　三角関数真数表（方向角の検算に使う）', '6　公差の表（本件土地は市街地地域）', '7　オンライン庁・書面申請'], [1], []),
      (69, 5, '読み方', PURPLE,
       ['同じ番号の注が別の場所にある', '（問題文の注3と、測量成果の表の下の注3）', '→ どこの注かを添えて読む'], [2], [])]
for x, y, head, col, lines, red, gray in NB:
    fbox(ax, x, y, 29.5, 42, head, col, lines, red=red, gray=gray, fs=12.5, hfs=15, lh=6.2, top=11)
fsave(fig, 'H20_dai21mon_zu02_chu_shiwake.png', '注の仕分け')

# ---- zu11：精度区分は地域で決まる ----
fig, ax = fixed_figure('精度区分は地域で決まる（市街地地域は甲2）',
                       '差0.71㎡は、甲2の2.21㎡の内側。今年は甲1の0.89㎡でも結論は同じだが、選び方は地域から決める（土地の呼び名や地目では決めない）。')
ax.text(3, 94, '地域と精度区分（不動産登記規則第10条第4項）', fontsize=18, weight='bold', va='center')
for i, (reg, sei, red) in enumerate([('市街地地域', '精度区分は甲2', True), ('村落・農耕地域', '精度区分は乙1', False), ('山林・原野地域', '精度区分は乙3', False)]):
    x = 3 + i * 32.5
    fbox(ax, x, 68, 30, 20, reg, RED if red else GRAY, [sei], red=[0] if red else [], gray=[] if red else [0], fs=17, hfs=17, top=12.5)
ax.text(3, 58, '公差の表（調査結果の6。分筆前の512.66㎡の行。甲3〜乙3は省略）', fontsize=18, weight='bold', va='center')
HEAD = ['甲1', '甲2', '甲3', '乙1', '乙2', '乙3']
VAL = ['0.89', '2.21', '…', '…', '…', '…']
ax.add_patch(plt.Rectangle((3, 38), 17, 8, fc='#f7f7f7', ec=BLACK, lw=1.6))
ax.add_patch(plt.Rectangle((3, 30), 17, 8, fc='#f7f7f7', ec=BLACK, lw=1.6))
ax.text(11.5, 42, '精度区分', ha='center', va='center', fontsize=15)
ax.text(11.5, 34, '512.66㎡', ha='center', va='center', fontsize=15)
for i in range(6):
    x = 20 + i * 12.8
    hit = i == 1
    ax.add_patch(plt.Rectangle((x, 38), 12.8, 8, fc='#fff0f0' if hit else 'white', ec=BLACK, lw=1.6))
    ax.add_patch(plt.Rectangle((x, 30), 12.8, 8, fc='#fff0f0' if hit else 'white', ec=RED if hit else BLACK, lw=3.0 if hit else 1.6))
    ax.text(x + 6.4, 42, HEAD[i], ha='center', va='center', fontsize=16, weight='bold', color=RED if hit else BLACK)
    ax.text(x + 6.4, 34, VAL[i], ha='center', va='center', fontsize=17, weight='bold' if hit else 'normal', color=RED if hit else GRAY)
ax.text(3, 21, '市街地地域 → 甲2 → 2.21㎡', fontsize=20, weight='bold', color=RED, va='center')
ax.text(3, 13, '分筆後の合計513.37㎡との差 0.71㎡ ＜ 2.21㎡ → 地積更正は不要', fontsize=18, va='center')
fsave(fig, 'H20_dai21mon_zu11_seido_kubun.png', '精度区分')

# ---- zu13：分筆を申請できる人 ----
fig, ax = fixed_figure('分筆を申請できるのは、登記名義人（死亡後はその相続人）',
                       '買主の南野二郎は売買をしただけで、所有権の移転の登記は未了。だから自分では分筆を申請できない。')
fbox(ax, 3, 72, 94, 22, '分筆の登記を申請できる人（不動産登記法第39条第1項）', BLUE,
     ['表題部所有者　又は　所有権の登記名義人（それ以外の者は申請できない）'], red=[0], fs=17, hfs=19, top=13)
fbox(ax, 3, 36, 45, 30, '5番の登記記録（甲区）', BLACK,
     ['甲区　所有権移転', '原因　平成2年5月14日売買', '（平成2年6月7日受付）', '所有者　西川四郎'], red=[3], fs=15, hfs=18)
fbox(ax, 52, 36, 45, 30, '買主　南野二郎', GRAY,
     ['平成19年5月1日に（ロ）を買った', 'でも所有権の移転の登記は未了', '→ 登記名義人ではない', '→ 自分では分筆を申請できない'], red=[3], fs=15, hfs=18)
fbox(ax, 3, 5, 94, 25, '登記名義人が死亡したら（不動産登記法第30条）', PURPLE,
     ['相続人が、表示に関する登記を申請できる', '遺産分割協議はしていない → 相続人全員', '→ まず相続人を確定する（次の図から）'], red=[2], fs=16, hfs=19, top=11.5)
darrow(ax, 25.5, 36, 25.5, 31.5)
fsave(fig, 'H20_dai21mon_zu13_mibun_shinsei.png', '分筆を申請できる人')

# ---- zu14：相続の順位と放棄 ----
fig, ax = fixed_figure('相続人の順位：七郎は放棄で子がいないのと同じ → 兄弟姉妹へ',
                       '放棄した人は初めから相続人とならなかったものとみなされる（民法第939条）。配偶者の和子は順位に関係なく常に相続人。')
fbox(ax, 3, 66, 63, 28, '第1順位　子（民法第887条第1項）', BLACK,
     ['子の西川七郎 → 平成19年7月1日に相続を放棄', '放棄した人は初めから相続人でない（第939条）', '→ 子はいないのと同じ'], red=[2], fs=15, hfs=18, top=11)
fbox(ax, 3, 36, 63, 24, '第2順位　直系尊属（第889条第1項第1号）', BLACK,
     ['父 一郎（平成12年死亡）・母 弘子（平成14年死亡）', '→ 生きている直系尊属はいない'], red=[1], fs=15, hfs=18, top=11)
fbox(ax, 3, 4, 63, 26, '第3順位　兄弟姉妹（第889条第1項第2号）', RED,
     ['三郎（平成8年死亡）・二郎・五郎（平成15年死亡）', '→ 兄弟姉妹の代まで下りる', '（代襲と半血は、次の図で確かめる）'], red=[1], gray=[2], fs=15, hfs=18, top=11)
fbox(ax, 70, 66, 28, 28, '配偶者', GREEN, ['西川和子', '常に相続人', '（民法第890条）'], red=[1], fs=15, hfs=19, top=12)
darrow(ax, 34, 66, 34, 61.5)
darrow(ax, 34, 36, 34, 31.5)
fsave(fig, 'H20_dai21mon_zu14_soz_junni.png', '相続の順位と放棄')

# ---- zu15：兄弟姉妹の代襲はおい・めいまで ----
fig, ax = fixed_figure('兄弟姉妹の代襲相続は、おい・めいまで（九郎は相続しない）',
                       '民法第889条第2項は第887条第2項（子の代襲）だけを準用し、再代襲を定めた第887条第3項は準用しない。')
fbox(ax, 3, 38, 45, 54, '三郎の系統', GRAY,
     ['三郎（平成8年死亡）', '↓ 子', '六郎　欠格事由（民法第891条）', '↓ 子', '九郎　再代襲しない', '→ 三郎の系統は相続人なし'], red=[4, 5], fs=15, hfs=19, lh=6.6, top=12)
fbox(ax, 52, 38, 45, 54, '五郎の系統', RED,
     ['五郎（平成15年死亡）', '↓ 子', '八郎　五郎を代襲して相続人', '（第889条第2項・第887条第2項）'], red=[2], fs=15, hfs=19, lh=6.6, top=12)
fbox(ax, 3, 4, 94, 28, '兄弟姉妹の代襲は子（おい・めい）まで', PURPLE,
     ['第889条第2項は、第887条第2項（子の代襲）だけを準用する', '再代襲を定めた第887条第3項は準用しない', '→ 欠格の六郎の子の九郎は、三郎の代わりに相続できない'], red=[2], fs=16, hfs=19, top=11.5)
fsave(fig, 'H20_dai21mon_zu15_daishuu.png', '代襲と再代襲')

# ---- zu16：父だけが同じ兄（半血） ----
fig, ax = fixed_figure('父だけが同じ二郎も、兄弟姉妹として相続人（半血）',
                       '二郎は一郎と前の妻の子。依頼人の南野二郎と同じ「二郎」なので読み流しやすい。相続分は申請書に書かない。')
ax.add_patch(FancyBboxPatch((40, 82), 20, 10, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=BLACK, lw=2))
ax.text(50, 87, '西川一郎', ha='center', va='center', fontsize=18, weight='bold')
ax.add_patch(FancyBboxPatch((5, 82), 25, 10, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=GRAY, lw=2))
ax.text(17.5, 87, '前の妻 美子\n（一郎と離婚）', ha='center', va='center', fontsize=13, color=GRAY)
ax.add_patch(FancyBboxPatch((70, 82), 25, 10, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=BLACK, lw=2))
ax.text(82.5, 87, '妻 弘子\n（平成14年死亡）', ha='center', va='center', fontsize=13)
ax.plot([30.5, 39.5], [87, 87], color=GRAY, lw=2, ls=':')
ax.plot([60.5, 69.5], [87, 87], color=GRAY, lw=2)
ax.plot([17.5, 17.5], [82, 74], color=GRAY, lw=2)
ax.plot([82.5, 82.5], [82, 74], color=GRAY, lw=2)
ax.add_patch(FancyBboxPatch((5, 56), 25, 17, boxstyle='round,pad=0.5', fc='#fff5f5', ec=RED, lw=2.4))
ax.text(17.5, 66, '西川二郎', ha='center', va='center', fontsize=18, weight='bold', color=RED)
ax.text(17.5, 60.5, '父だけが同じ（半血）', ha='center', va='center', fontsize=13, color=RED)
ax.add_patch(FancyBboxPatch((52, 56), 44, 17, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=BLACK, lw=2))
ax.text(74, 66, '三郎・四郎・五郎', ha='center', va='center', fontsize=17, weight='bold')
ax.text(74, 60.5, '父母とも同じ（全血）。四郎が被相続人', ha='center', va='center', fontsize=13)
fbox(ax, 3, 6, 46, 40, '二郎は相続人になる', RED,
     ['父母の一方だけが同じ兄弟姉妹も', '兄弟姉妹として相続人（第889条第1項第2号）', '相続分が半分になるだけ', '（第900条第4号ただし書）'], red=[0, 2], fs=14, hfs=18, top=11.5, lh=6.4)
fbox(ax, 52, 6, 45, 40, '参考：相続分（申請書には書かない）', GRAY,
     ['和子　4分の3（第900条第3号）', '八郎　6分の1（五郎の分。全血）', '二郎　12分の1（半血）', '表示に関する登記の申請人に', '相続分は関係ない'], gray=[0, 1, 2, 3, 4], fs=14, hfs=16, top=11.5, lh=6.0)
fsave(fig, 'H20_dai21mon_zu16_hanketsu.png', '半血')

# ---- zu19：代位原因の日付は売買の日 ----
fig, ax = fixed_figure('代位原因の日付は、売買の日（死亡の日ではない）',
                       '代位原因は、南野さんが持つ権利そのもの。死亡の日（相続が始まった日）は、相続証明書で示す。')
ax.annotate('', xy=(97, 82), xytext=(3, 82), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
ax.plot([27], [82], 'o', ms=14, color=RED)
ax.text(27, 90, '平成19年5月1日', ha='center', fontsize=19, weight='bold', color=RED)
ax.text(27, 74, '売買（（ロ）を買う）', ha='center', va='top', fontsize=16)
ax.plot([68], [82], 'o', ms=14, color=GRAY)
ax.text(68, 90, '平成19年6月1日', ha='center', fontsize=19, weight='bold', color=GRAY)
ax.text(68, 74, '西川四郎が死亡', ha='center', va='top', fontsize=16)
fbox(ax, 3, 30, 45, 32, '代位原因の日付', RED,
     ['南野さんの請求権が生まれた日', '＝ 売買の日', '代位原因　平成19年5月1日売買の', '　　　　　所有権移転登記請求権'], red=[1, 2, 3], fs=15, hfs=19, top=11.5)
fbox(ax, 52, 30, 45, 32, '死亡の日（6月1日）', GRAY,
     ['相続が始まった日', '相続人が申請できる立場は', '相続証明書で示す', '（不動産登記令第7条第1項第4号）'], fs=15, hfs=19, top=11.5)
ax.text(3, 21, '誤り　代位原因　平成19年6月1日相続による所有権移転登記請求権', fontsize=16, color=GRAY, va='center')
ax.text(3, 13, '正しい　代位原因　平成19年5月1日売買の所有権移転登記請求権', fontsize=18, weight='bold', color=RED, va='center')
fsave(fig, 'H20_dai21mon_zu18_daii_hizuke.png', '代位原因の日付')

# ---- zu20：添付書類 ----
fig, ax = fixed_figure('添付書類は4つ（登記識別情報と印鑑証明書は要らない）',
                       '登記識別情報と印鑑証明書は、合筆のときの書類。分筆だけなら付けない。相続証明書は今は法定相続情報番号でも代えられる。')
ax.add_patch(FancyBboxPatch((3, 6), 63, 88, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=BLUE, lw=2.0))
ax.text(5, 90, '付けるもの（4つ）', fontsize=20, weight='bold', color=BLUE, va='center')
ROWS20 = [('地積測量図', '令別表8の項添付情報欄イ（分筆後の土地）', ''),
          ('相続証明書', '令第7条第1項第4号（法第30条の申請）', '今は法定相続情報番号でも可（規則第37条の3第1項）'),
          ('代位原因証書', '令第7条第1項第3号（売買契約書など）', ''),
          ('代理権限証書', '令第7条第1項第2号（調査士への委任状）', '')]
for i, (nm, b1, b2) in enumerate(ROWS20):
    y = 78 - i * 18.5
    ax.text(6, y, nm, fontsize=19, weight='bold', color=RED, va='center')
    ax.text(6, y - 6, b1, fontsize=14, va='center')
    if b2:
        ax.text(6, y - 11.5, b2, fontsize=13, color=GRAY, va='center')
fbox(ax, 70, 36, 27, 58, '付けないもの', GRAY,
     ['登記識別情報', '印鑑証明書', '', '合筆のときの書類。', '分筆だけなら', '要らない'], gray=[0, 1, 2, 3, 4, 5], fs=15, hfs=18, top=12, lh=6.4)
fsave(fig, 'H20_dai21mon_zu20_tenpu.png', '添付書類')

# ---- zu21：登録免許税 ----
fig, ax = fixed_figure('登録免許税は、分筆後の個数 × 1,000円（欄がなくても書く）',
                       '登録免許税法別表第一の一（十三）イ。分筆後は5番1と5番2の2個。代位の申請でも税はかかる。')
fbox(ax, 3, 40, 56, 54, '分筆の登録免許税', RED,
     ['分筆後の土地の個数 × 1,000円', '5番1 ＋ 5番2 ＝ 2個', '2個 × 1,000円 ＝ 金2,000円', '（元の地番が残る土地も数える）'], red=[2], fs=18, hfs=20, top=13, lh=8)
fbox(ax, 62, 40, 35, 54, '課税されない登記', GRAY,
     ['土地の表題登記など', 'は課税されない', '（登録免許税の', '　欄もない）'], gray=[0, 1, 2, 3], fs=15, hfs=18, top=13, lh=7)
fbox(ax, 3, 6, 94, 28, '答案用紙に欄がなくても', BLUE,
     ['課税される登記は、申請人などを書く大きな枠の最後の行に書く', '「登録免許税　金2,000円」'], red=[1], fs=17, hfs=19, top=12.5)
fsave(fig, 'H20_dai21mon_zu21_tourokumenkyozei.png', '登録免許税')

# ---- zu23：土地の表示の行ごとの書き方 ----
fig, ax = fixed_figure('土地の表示の3行：何を書き、何を書かないか',
                       '1行目は分筆前の登記記録のまま（地積更正をしないので、計算の513.37は書かない）。地目は変わらない（イ）の行は空欄。')
ax.text(3, 94, '所在の欄：K市B町一丁目', fontsize=18, weight='bold', va='center')
TX = [3, 17, 26, 39, 58]   # 地番｜地目｜地積（整数部｜小数部）｜原因 の境
ax.add_patch(plt.Rectangle((TX[0], 30), TX[4] - TX[0], 56, fc='white', ec=BLACK, lw=2.6))
for yy in (78, 62, 46):
    ax.plot([TX[0], TX[4]], [yy, yy], color=BLACK, lw=1.6)
for xx in (TX[1], TX[2], TX[3]):
    ax.plot([xx, xx], [30, 86], color=BLACK, lw=1.6 if xx != 35 else 1.2)
ax.plot([32.5, 32.5], [30, 78], color=GRAY, lw=1.4, ls='--')
for xc, t in [((TX[0] + TX[1]) / 2, '①地番'), ((TX[1] + TX[2]) / 2, '②地目'), ((TX[2] + TX[3]) / 2, '③地積'), ((TX[3] + TX[4]) / 2, '原因及びその日付')]:
    ax.text(xc, 82, t, ha='center', va='center', fontsize=14)
GY = [(70, '5番', '宅地', '512', '66', ''), (54, '（イ）5番1', '', '300', '79', '①③5番1、\n5番2に分筆'), (38, '（ロ）5番2', '宅地', '212', '58', '5番から分筆')]
for yc, a, b, c, d, e in GY:
    ax.text(TX[0] + 1, yc, a, fontsize=15, color=INK_BLUE, va='center')
    ax.text((TX[1] + TX[2]) / 2, yc, b, fontsize=15, color=INK_BLUE, va='center', ha='center')
    ax.text(31.5, yc, c, fontsize=15, color=INK_BLUE, va='center', ha='right')
    ax.text(33.5, yc, d, fontsize=15, color=INK_BLUE, va='center', ha='left')
    ax.text(TX[3] + 1, yc, e, fontsize=13, color=INK_BLUE, va='center')
NOTES = [(70, ['分筆前の登記記録のまま', '計算した513.37は書かない'], RED),
         (54, ['地番が変わる → ①、地積が変わる → ③', '地目は変わらないので空欄'], RED),
         (38, ['新しい土地。元の地番（5番）から分筆', '新しい土地なので地目も書く'], RED)]
for yc, tt, col in NOTES:
    ax.annotate('', xy=(59.5, yc), xytext=(62, yc), arrowprops=dict(arrowstyle='-|>', lw=1.8, color=col))
    ax.text(63, yc + 3.2, tt[0], fontsize=14, color=col, va='center', weight='bold')
    ax.text(63, yc - 3.2, tt[1], fontsize=14, color=BLACK, va='center')
ax.text(3, 20, '地積は整数部と小数部を点線で分けて書く（小数点は書かない）', fontsize=15, color=GRAY, va='center')
ax.text(3, 13, '宅地なので小数第2位未満を切り捨てる：300.79265 → 300.79、212.58635 → 212.58', fontsize=15, va='center')
fsave(fig, 'H20_dai21mon_zu23_tochi_hyouji_gyou.png', '土地の表示の行')

# ---- zu24：辺長の端数処理 ----
fig, ax = fixed_figure('辺長7本は小数第3位を四捨五入（DEは繰り上げ、EAは0を残す）',
                       '問題文の注3。小数第3位が5以上なら切り上げ、4以下なら切り捨て。9.40の末尾の0は落とさない。')
for xc, t in [(6, '辺'), (20, '表示（丸める前）'), (50, '小数第3位'), (68, '地積測量図に書く辺長')]:
    ax.text(xc, 91, t, fontsize=16, weight='bold', va='center')
ax.plot([3, 97], [86, 86], color=BLACK, lw=1.6)
ED = [('AB', '21.6514…', 1, '21.65'), ('BF', '9.6873…', 7, '9.69'), ('FC', '13.1521…', 2, '13.15'), ('CD', '25.3107…', 0, '25.31'),
      ('DE', '11.7552…', 5, '11.76'), ('EA', '9.4041…', 4, '9.40'), ('EF', '23.2539…', 3, '23.25')]
for i, (nm, v, dg, r) in enumerate(ED):
    y = 79 - i * 8.6
    hit = nm in ('DE', 'EA')
    col = RED if hit else BLACK
    ax.text(6, y, nm, fontsize=18, weight='bold', color=col, va='center')
    ax.text(20, y, v, fontsize=18, color=col, va='center')
    ax.text(53, y, str(dg), fontsize=18, color=col, va='center', ha='center', weight='bold' if hit else 'normal')
    ax.text(68, y, r, fontsize=19, color=col, va='center', weight='bold')
    if hit:
        ax.add_patch(plt.Rectangle((3, y - 4), 94, 8, fc='none', ec=RED, lw=1.6))
ax.text(3, 14, 'DE：小数第3位が5 → 切り上げて11.76（11.75と切り捨てない）', fontsize=16, color=RED, va='center', weight='bold')
ax.text(3, 7, 'EA：9.4041… → 9.40（0を落として9.4と書かない）', fontsize=16, color=RED, va='center', weight='bold')
fsave(fig, 'H20_dai21mon_zu24_hencho_hasuu.png', '辺長の端数')

# ---- zu25：地積測量図に書くもの・書かないもの ----
fig, ax = fixed_figure('地積測量図に書くもの・書かないもの・書きようがないもの',
                       '座標値・求積・地積は省略してよい（問題文の注3）。基準点T1〜T3と多角点T101は位置と名称を描く。測量の年月日は問題文に日付がないので書かない。')
fbox(ax, 2, 6, 46, 88, '書くもの', BLUE,
     ['地番の欄　5番1、5番2', '土地の所在の欄　K市B町一丁目', '方位', '辺長7本（単位 m）', '区画の中の地番　（イ）5－1・（ロ）5－2',
      '隣接地　6－2・6－1・4・7・道路', '境界標　A・B金属標、C・D・E杭、F金属鋲', '基準点T1〜T3と多角点T101', '　の位置と名称（座標値は書かない）'], red=[7, 8],
     fs=13, hfs=20, top=12.5, lh=7.6)
fbox(ax, 51, 50, 47, 44, '書かないもの（問題文の注3）', RED,
     ['各筆界点・基準点等の座標値', '求積とその方法', '地積'], fs=15, hfs=18, top=13, lh=7.5)
fbox(ax, 51, 6, 47, 40, '書きようがない・印刷済み', GRAY,
     ['測量の年月日：問題文に日付がない', '→ 日付を作って書かない', '作成者・申請人：（略）の印刷', '縮尺：1／250の印刷'], red=[1], gray=[2, 3], fs=14, hfs=18, top=12, lh=6.8)
fsave(fig, 'H20_dai21mon_zu25_kaku_kakanai.png', '書くもの・書かないもの')


print('重なりの合計:', len(ALL_PROBLEMS))
