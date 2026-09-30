"""平成20年度 第21問（土地）会話形式note記事の解説図13枚を、座標値から作図する。

`../prompt_H20_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../H23/Q21/zu/draw_H23_dai21mon_kaisetsuzu.py`。

6番1と6番2の境の線（E点から北西へ延びる線）は、問題文に座標がないので、見取図の向きを模式的に短く描く（図の中で「位置は模式」と書く）。
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
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像',
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
ALL_PROBLEMS += save(fig, [z], 'H20_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：問1 結合トラバース T2→T101′→T3′（全体と、T3のまわりの拡大）
# =====================================================================
fig, (ax1, ax2) = new_figure('図2　問1　結合トラバース（T2 → T101′ → T3′）と閉合誤差',
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
ALL_PROBLEMS += save(fig, [za, zb], 'H20_dai21mon_zu02_T101_ketsugou.png')

# =====================================================================
# 図3：問1 コンパスの法則の配分（数直線と、T101のまわりの拡大）
# =====================================================================
fig, (ax1, ax2) = new_figure('図3　問1　コンパスの法則で閉合誤差を配る',
                             '補正量は「正しい値 − 計算した値」＝ T3 − T3′。T101では、T2からの距離10.71 ÷ 全長34.62の分だけ直す。\n'
                             'T101 ＝ T101′ ＋ (T3 − T3′) × 10.71 ÷ (10.71 ＋ 23.91) ＝ 4.0391… ＋ 6.4266…i → T101（4.04, 6.43）。\n'
                             '補正量の向きを逆にすると（4.05, 6.41）、23.91の割合で配ると（4.03, 6.44）で、どちらも誤り。',
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
ax1.text(xs(10.71) + 2, 34, '× 10.71 ÷ 34.62', ha='left', va='center', fontsize=14, color=RED)
ax1.text(50, 18, '直す量は、出発点からの距離に比例する', ha='center', fontsize=16)
ax1.text(50, 11, '（T101は10.71 ÷ 34.62、T3は全部）', ha='center', fontsize=16)
zb = Zu(ax2, fontsize=14)
cz = (T101R + T101X) / 2
fit(ax2, [cz + P(-0.021, -0.021), cz + P(0.021, 0.021)], margin=0.02, pad_aspect=True)
zb.line(T101R, T101X, color=RED, lw=2.4)
zb.line(T101R, T101_SIGN, color=GRAY, lw=1.6, ls='--')
zb.line(T101R, T101_2391, color=GRAY, lw=1.6, ls=':')
zb.north_arrow()
zb.point(T101R, 'dot', color=BLACK, size=10)
zb.callout(T101R, 'T101′（調整前）', dirs=(45, 65, 25), dists=(45, 60, 75))
zb.point(T101X, 'dot', color=RED, size=12)
zb.callout(T101X, 'T101（調整後）\n4.0391… ＋ 6.4266…i\n→（4.04, 6.43）', dirs=(-135, -115, -155), color=RED, dists=(45, 60, 75))
zb.point(T101_SIGN, 'dot', color=GRAY, size=10)
zb.callout(T101_SIGN, '向きが逆の誤り\n（4.05, 6.41）', dirs=(-135, -115, -155, 180), color=GRAY, dists=(40, 55, 70))
zb.point(T101_2391, 'dot', color=GRAY, size=10)
zb.callout(T101_2391, '23.91で配った誤り\n（4.03, 6.44）', dirs=(45, 65, 25, 90), color=GRAY, dists=(40, 55, 70))
ax2.set_title('T101のまわりの拡大（約3cm四方）', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [zb], 'H20_dai21mon_zu03_compass.png')

# =====================================================================
# 図4：問2 B点（調整後のT101から後視の向きを取り直す）
# =====================================================================
fig, (ax1, ax2) = new_figure('図4　問2　B点の求め方（調整後のT101からT2を後視して放射）',
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
ALL_PROBLEMS += save(fig, [za, zb], 'H20_dai21mon_zu04_B_housha.png')

# =====================================================================
# 図5：問2 E点（A→Dを4：5に内分）
# =====================================================================
fig, (ax,) = new_figure('図5　問2　E点の求め方（A→Dを4：5に内分）',
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
ALL_PROBLEMS += save(fig, [z], 'H20_dai21mon_zu05_E_naibun.png')

# =====================================================================
# 図6：問2 F点（Eから直線BCへの垂線の足）
# =====================================================================
fig, (ax,) = new_figure('図6　問2　F点の求め方（Eから直線BCへの垂線の足）',
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
ALL_PROBLEMS += save(fig, [z], 'H20_dai21mon_zu06_F_suisen.png')

# =====================================================================
# 図7：問3の前提 （ロ）と（イ）の面積（対角線2本）
# =====================================================================
fig, (ax1, ax2) = new_figure('図7　問3の前提　（ロ）と（イ）の面積（対角線2本で出す）',
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
path = os.path.join(OUT, 'H20_dai21mon_zu07_menseki.png')
fig.savefig(path, dpi=100, facecolor='white')
print('  →', path)

# =====================================================================
# 図8：公差の数直線（固定配置）
# =====================================================================
fig, ax = fixed_figure('図8　問3の前提　地積更正は要らない（市街地地域の甲2）',
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
path = os.path.join(OUT, 'H20_dai21mon_zu08_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図8: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図9：相続関係図（固定配置）
# =====================================================================
fig, ax = fixed_figure('図9　問3　西川四郎の相続人は和子・二郎・八郎の3人',
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
path = os.path.join(OUT, 'H20_dai21mon_zu09_souzoku.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図9: 相続関係図（固定配置）\n  →', path)

# =====================================================================
# 図10：代位の関係図（固定配置）
# =====================================================================
fig, ax = fixed_figure('図10　問3　買主の南野二郎が、相続人3人に代位して分筆を申請する',
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
path = os.path.join(OUT, 'H20_dai21mon_zu10_daii.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図10: 代位の関係図（固定配置）\n  →', path)

# =====================================================================
# 図11：分筆前と分筆後の区画と地番
# =====================================================================
fig, (ax1, ax2) = new_figure('図11　問3　分筆前と分筆後の区画と地番',
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
path = os.path.join(OUT, 'H20_dai21mon_zu11_bunpitsu_chiban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('  →', path)

# =====================================================================
# 図12：問4 地積測量図の完成見本（すべて黒、塗りなし）
# =====================================================================
fig, (ax,) = new_figure('図12　問4　地積測量図（1／250）の完成見本',
                        '辺長は小数第3位を四捨五入（DEは11.7552…で11.76、EAは9.4041…で9.40）。座標値・求積・地積は書かない（問題文の注3）。\n'
                        '基準点T1・T2・T3と多角点T101の位置と名称を描く（問題文の注3）。1／250で1m ＝ 4mm、基準点まで入れて縦横とも約117mm。\n'
                        '地番の欄は「5番1、5番2」、土地の所在の欄は「K市B町一丁目」。作成者・申請人・縮尺の欄は印刷済み。')
z = Zu(ax, fontsize=13)
fit(ax, [T1, T2, T3, T101, A, B, C, D, N6, ext(A, D, -2.0), ext(D, A, -2.0), ext(B, C, -2.0), ext(C, B, -2.0),
         P(0.0, 33.0)], margin=0.06, pad_aspect=True)
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
z.free_text(P(1.3, 22.0), 'A・B：金属標　C・D・E：コンクリート杭\nF：金属鋲　T1・T2・T3：K市基準点\nT101：多角点　（単位：m）',
            fs=12, offsets=((0, 0), (0, -10), (10, 0)))
ALL_PROBLEMS += save(fig, [z], 'H20_dai21mon_zu12_chiseki_sokuryouzu.png')

# =====================================================================
# 図13：本番で解く順番（固定配置）
# =====================================================================
fig, ax = fixed_figure('図13　本番で解く順番（T101が要るのはB点から後）',
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
path = os.path.join(OUT, 'H20_dai21mon_zu13_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図13: 整理図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
