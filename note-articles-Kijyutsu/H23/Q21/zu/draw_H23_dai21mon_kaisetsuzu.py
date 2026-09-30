"""平成23年度 第21問（土地）会話形式note記事の解説図13枚を、座標値から作図する。

`../prompt_H23_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../H28/Q21/zu/draw_H28_dai21mon_kaisetsuzu.py`。

B点は問題文で座標が「省略」されている（計算には使わない）。51番3の形を示す図だけ、51番3の地積測量図の三斜
（21.70 × 14.51）とABとEMの平行から逆算した参考の位置 B_REF に置き、図の中で「参考の位置」と明記する。
神楽殿・参道・社殿・社務所は座標がないので描かない（文字で示すだけ）。

実行: python3 note-articles-Kijyutsu/H23/Q21/zu/draw_H23_dai21mon_kaisetsuzu.py [出力フォルダ]
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

# ---- 座標（問題文のA市基準点成果表・測量によって得られた座標、記事で求めた点） ------------------
T1, T2, T3 = P(309.14, 292.20), P(300.12, 306.99), P(299.47, 333.78)
D, E, F, G = P(320.31, 309.24), P(326.52, 315.34), P(323.58, 334.66), P(302.56, 332.88)
I, J, L = P(312.05, 313.06), P(303.18, 315.34), P(303.65, 302.14)
A = r2(radial(T1, T2, 15.120, dms(150, 21, 44)))
M = r2(radial(T1, T2, 6.613, dms(324, 2, 29)))
K = r2(radial(T2, T3, 5.067, dms(319, 7, 54)))
C = r2(M + (E - M) * 157.3309 / 364.4865)
PX = E - 9.732                                             # E→J（真南）とD→Hの交点
H = r2(PX + cmath.rect(6.836, dms(120)))
B_REF = A + (E - M) * 314.867 / 364.4865                   # B点（座標は省略。三斜から逆算した参考の位置）
# 誤りの点
AW = r2(T1 + cmath.rect(15.120, cmath.phase(T2 - T1) - dms(150, 21, 44)))   # 反時計回り
MW = r2(T1 + cmath.rect(6.613, cmath.phase(T2 - T1) - dms(324, 2, 29)))
KW = r2(T2 + cmath.rect(5.067, cmath.phase(T3 - T2) - dms(319, 7, 54)))
CW = r2(M + (E - M) / abs(E - M) * 10.05)                  # ブロック塀の10.05mで置いた誤り
HW = r2(D + cmath.rect(6.836, dms(120)))                   # Dから6.836mと読んだ誤り

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('A', A, P(309.60, 277.09)), ('M', M, P(309.67, 298.79)), ('K', K, P(303.34, 310.90)),
                     ('C', C, P(316.94, 305.93)), ('H', H, P(313.37, 321.26)), ('AW', AW, P(322.37, 284.87)),
                     ('MW', MW, P(303.04, 294.75)), ('KW', KW, P(296.71, 310.74)), ('CW', CW, P(316.84, 305.83)),
                     ('HW', HW, P(316.89, 315.16))]:
    assert abs(got - want) < 1e-9, (n, got, want)
assert abs(PX - P(316.788, 315.34)) < 1e-9
assert f'{abs(M - A):.2f}' == '21.70' and f'{abs(B_REF - M):.2f}' == '16.27'
assert f'{abs(((M - A).conjugate() * (B_REF - A)).imag) / abs(M - A):.2f}' == '14.51'
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = [(C, D, '4.72'), (D, H, '13.88'), (H, J, '11.78'), (J, K, '4.44'), (K, I, '8.97'), (I, C, '8.65')]
for p, q, want in SIDES:
    assert d2(p, q) == want, (p, q, d2(p, q), want)
assert f'{abs(C - M):.4f}'[:7] == '10.1898'
HONKEN = [C, D, H, J, K, I]                  # 本件土地（申請地）
# 本件土地はくの字（Iが凹んだ角）なので、重心が区画の外（Iの近く）に来る。内側の代表点はIとHの中点にする
INNER = (I + H) / 2
N51_3 = [A, B_REF, C, M]                     # 51番3（Bは参考の位置）
N51_2 = [M, C, I, K, L]                      # 51番2
N50_1 = [E, F, G, J, H, D]                   # 50番1
assert f'{area(HONKEN):.3f}' == '113.875' and chiseki(area(HONKEN), False) == 113
assert f'{area([CW, D, H, J, K, I]):.3f}' == '114.479' and chiseki(area([CW, D, H, J, K, I]), False) == 114
assert f'{abs(((E - M).conjugate() * (A - M)).imag):.4f}' == '364.4865'
BRG_T2_T1 = math.degrees(cmath.phase(T2 - T1))             # T1→T2 121°22′40.17″
BRG_T3_T2 = math.degrees(cmath.phase(T3 - T2))             # T2→T3 91°23′23.58″
assert to_dms(math.radians(BRG_T2_T1)) == '121°22′40.17″' and to_dms(math.radians(BRG_T3_T2)) == '91°23′23.58″'
assert to_dms(cmath.phase(E - M)) == '44°29′07.37″' and to_dms(cmath.phase(M - A)) == '89°48′54.63″'
assert to_dms(cmath.phase(PX - D)) == '120°00′04.14″'
assert f'{abs(HW - PX):.2f}' == '0.21'
# 誤りの点の向き：AWは直線ABより西（51番3の北西の外）、KWはT2より南、MWはA→Mの線より6m以上南
t = (AW.real - A.real) / (B_REF.real - A.real)
assert AW.imag < (A + (B_REF - A) * t).imag
assert KW.real < T2.real and M.real - MW.real > 6
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


KIND = {'A': 'metal', 'L': 'metal', 'J': 'metal', 'K': 'metal', 'B': 'stone', 'E': 'stone', 'F': 'stone', 'G': 'stone',
        'M': 'stone', 'C': 'concrete', 'D': 'concrete', 'H': 'concrete', 'I': 'concrete'}
ALL_PROBLEMS = []

# =====================================================================
# 図1：全体像（北を上にして座標どおりに描き直した見取図）
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像',
                        'E→Jは真南（Y座標が同じ315.34）。C・DはE→Mの直線の上、J・KはG→Lの直線の上。ABとEMは平行。\n'
                        'B点は座標が省略されているので、51番3の地積測量図の三斜から逆算した参考の位置（灰色の破線）に置いた。')
z = Zu(ax, fontsize=14)
fit(ax, [T1, T2, T3, A, B_REF, E, F, G, L, M], margin=0.06, pad_aspect=True)
z.poly(N50_1, fill=BLUE)
z.poly(N51_2, fill=ORANGE)
z.poly(HONKEN, fill=GREEN, lw=2.6)
z.poly([M, A, B_REF, C], color=GRAY, lw=1.6, ls='--', fill=PURPLE, closed=False)
z.line(D, E, color=BLACK, lw=2.0)
z.line(E, J, color=GRAY, lw=1.3, ls=':')
z.line(A, M, color=BLACK, lw=2.0)
z.north_arrow()
z.callout(INNER + P(-4.0, -0.8), '本件土地（無番地）', dirs=(-100, -80, -120), color=GREEN, fs=15, dists=(160, 185, 210))
z.free_text(centroid(N50_1) + P(2, 3), '50番1\n雨堤天満宮', fs=15, offsets=((0, 0), (0, 16), (16, 0)))
z.free_text(centroid(N51_2), '51番2', fs=15, offsets=((0, 0), (0, -14), (-14, 0)))
z.free_text(centroid(N51_3), '51番3\n（駐車場）', fs=15, offsets=((0, 0), (0, -14), (14, 0)))
for p, n, ref in [(A, 'A', centroid(N51_3)), (M, 'M', centroid(N51_2)), (L, 'L', centroid(N51_2)),
                  (C, 'C', INNER), (D, 'D', INNER), (H, 'H', INNER),
                  (J, 'J', INNER), (K, 'K', INNER), (I, 'I', INNER),
                  (E, 'E', centroid(N50_1)), (F, 'F', centroid(N50_1)), (G, 'G', centroid(N50_1))]:
    z.point(p, KIND[n], color=RED if n in 'CH' else BLACK)
    z.point_label(p, n, away=ref, color=RED if n in 'CH' else BLACK)
z.point(B_REF, 'stone', color=GRAY)
z.callout(B_REF, 'B（参考の位置）', dirs=(90, 60, 120), color=GRAY, dists=(40, 55, 70))
for p, n in [(T1, 'T1'), (T2, 'T2'), (T3, 'T3')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=p + P(1, 0))
z.free_text(P(301.3, 322.0), '道　路', fs=15, color=GRAY, offsets=((0, 0), (0, -12), (20, 0)))
z.free_text(P(327.5, 305.0), '50－2', fs=14, color=GRAY, offsets=((0, 0), (0, 14), (-16, 0)))
z.free_text(P(327.8, 326.0), '48－5', fs=14, color=GRAY, offsets=((0, 0), (0, 14), (16, 0)))
z.free_text(P(313.0, 336.4), '49－1', fs=14, color=GRAY, offsets=((0, 0), (16, 0), (0, 14)))
z.callout(E + (J - E) * 0.5, 'E→Jは真南', dirs=(0, 20, -20), color=GRAY, dists=(55, 75, 95))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu01_zentaizu.png')


# =====================================================================
# 図2〜図4：放射（点ごとに1枚）
# =====================================================================
def housha_figure(no, name, title, caption, station, back, pt, wrong, dist, obs, fit_pts, bg_lines, st_name, bk_name,
                  pt_name, r, wrong_dirs, pt_dirs, extra=None):
    fig, (ax,) = new_figure(title, caption)
    z = Zu(ax, fontsize=14)
    fit(ax, fit_pts, margin=0.10, pad_aspect=True)
    for p, q in bg_lines:
        z.line(p, q, color=GRAY, lw=1.4)
    b_back = bearing(station, back)
    z.line(station, back, color=BLUE, lw=1.8)
    z.line(station, station + P(r * 1.45, 0), color=GRAY, lw=1.2, ls='--')
    z.line(station, pt, color=RED, lw=2.8)
    z.line(station, wrong, color=GRAY, lw=1.4, ls='--')
    z.angle_arc(station, r * 0.55, 0, b_back, color=BLUE)
    z.angle_arc(station, r, b_back, b_back + obs, color=RED)
    if extra:
        extra(z)
    z.north_arrow()
    z.point(station, 'kijun')
    z.point(back, 'kijun')
    z.point_label(back, bk_name, away=station)
    z.point_label(station, st_name, away=pt)
    z.point(pt, 'dot', color=RED, size=10)
    z.callout(pt, f'{pt_name}（{pt.real:.2f}, {pt.imag:.2f}）', dirs=pt_dirs, color=RED, dists=(50, 70, 90, 110))
    z.point(wrong, 'dot', color=GRAY, size=8)
    z.callout(wrong, f'反時計回りの誤り（{wrong.real:.2f}, {wrong.imag:.2f}）', dirs=wrong_dirs, color=GRAY,
              dists=(45, 65, 85, 105))
    z.edge_label(station, pt, f'{dist}', station + (back - station) * 0.3, color=RED, fs=15)
    return fig, z


fig, z = housha_figure(
    2, 'A', '図2　A点の求め方（T1からT2を後視して放射）',
    'T1→T2の方向角 121°22′40.17″ に、T2の方向から時計回りの観測角 150°21′44″ を足して 271°44′24.17″（真数表の1°44′24″＝271°44′24″ − 270°）。\n'
    '15.120m進んでA（309.60, 277.09）。反時計回りに引くと（322.37, 284.87）で、51番3のA→Bの線より北西の外に出る。',
    T1, T2, A, AW, '15.12', 150 + 21 / 60 + 44 / 3600, [T1, T2, A, AW, M, B_REF, P(304.5, 292.2)],
    [(A, M), (A, B_REF)], 'T1', 'T2', 'A', 3.2, (60, 30, 90, 120), (-100, -130, -70, -150))
z.free_text(T1 + P(1.4, 1.2), '方向角 121°22′40.17″', color=BLUE, fs=14, ha='left', offsets=((10, 10), (20, 30), (30, 0)))
z.free_text(T1 + P(-3.4, -2.0), '観測角 150°21′44″（時計回り）', color=RED, fs=14, offsets=((0, -20), (0, -40), (-40, -20)))
z.free_text(A + (B_REF - A) * 0.5 + (M - A) * 0.25, '51番3', color=GRAY, fs=14, offsets=((0, 0), (20, -10), (-20, 10), (30, -30)))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu02_A_housha.png')


def extra_m(z):
    z.line(A, M, color=GREEN, lw=2.2)
    z.point(A, 'metal')
    z.point_label(A, 'A', away=A + P(1, 1))
    z.edge_label(A, M, 'AM ＝ 21.70（51番3の地積測量図の底辺と一致）', A + P(5, 5), color=GREEN, fs=14,
                 ts=(0.32, 0.4, 0.25), dists=(12, 18, 26))


fig, z = housha_figure(
    3, 'M', '図3　M点の求め方（T1からT2を後視して放射）',
    'T1→T2の方向角 121°22′40.17″ ＋ 観測角 324°02′29″ ＝ 445°25′09.17″（360°を引いた85°25′09.17″と同じ向き。真数表の85°25′09″）。\n'
    '6.613m進んでM（309.67, 298.79）。AM ＝ 21.70 で51番3の地積測量図の底辺と一致。反時計回りだと（303.04, 294.75）でA→Mの線より6m以上南。',
    T1, T2, M, MW, '6.613', 324 + 2 / 60 + 29 / 3600, [T1, T2, M, MW, A, P(313.5, 299.0)],
    [], 'T1', 'T2', 'M', 2.4, (-60, -30, -90, 180), (60, 30, 90), extra=extra_m)
z.free_text(T1 + P(1.3, 1.6), '方向角\n121°22′40.17″', color=BLUE, fs=14, ha='left', offsets=((12, 10), (24, 24), (30, 0)))
z.free_text(T1 + P(2.8, -1.8), '観測角 324°02′29″（時計回り）', color=RED, fs=14, offsets=((0, 18), (0, 36), (-30, 20)))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu03_M_housha.png')


def extra_k(z):
    z.line(L, G, color=BLACK, lw=1.8)
    for p, n in [(L, 'L'), (J, 'J'), (G, 'G')]:
        z.point(p, KIND[n])
        z.point_label(p, n, away=p + P(-1, 0))
    z.free_text(L + (G - L) * 0.33, 'G→Lの直線（道路境界）', fs=14, offsets=((0, 16), (0, 26), (40, 16)))


fig, z = housha_figure(
    4, 'K', '図4　K点の求め方（T2からT3を後視して放射）',
    '器械点が変わったので、後視の向きはT2→T3の 91°23′23.58″ で取り直す。観測角 319°07′54″ を足して 410°31′17.58″（＝50°31′17.58″。真数表の50°31′18″）。\n'
    '5.067m進んでK（303.34, 310.90）。Conjg(L − G) × (K − G) ＝ 676.5154 ＋ 0.019i で、KはG→Lの直線の上。反時計回りだと（296.71, 310.74）で道路の向こう。',
    T2, T3, K, KW, '5.067', 319 + 7 / 60 + 54 / 3600, [T2, T3, K, KW, L, G, P(305.5, 306.0)],
    [], 'T2', 'T3', 'K', 2.2, (-60, -30, -90, 180), (60, 90, 120), extra=extra_k)
z.free_text(T2 + P(1.6, 2.6), '方向角 91°23′23.58″', color=BLUE, fs=14, ha='left', offsets=((12, 6), (26, 20), (40, 0)))
z.free_text(T2 + P(-2.4, -1.8), '観測角 319°07′54″（時計回り）', color=RED, fs=14, offsets=((0, -16), (-20, -30), (0, -40)))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu04_K_housha.png')

# =====================================================================
# 図5：問2 C点（高さが同じ三角形の面積の比）
# =====================================================================
fig, (ax,) = new_figure('図5　問2　C点の求め方（51番3の地積測量図の三斜と、ABとEMの平行）',
                        'BはA→Bの直線、CはM→Eの直線の上。ABとEMは平行なので、△BMC（底辺MC）と△AME（底辺ME）の高さは同じ h。\n'
                        'MC ÷ ME ＝ △BMCの倍面積 ÷ △AMEの倍面積 ＝ (16.27 × 9.67) ÷ 364.4865 ＝ 157.3309 ÷ 364.4865。\n'
                        'C ＝ M ＋ (E − M) × 157.3309 ÷ 364.4865 ＝ （316.94, 305.93）。検算：BM ＝ 16.2681… → 16.27（三斜の対角線と一致）')
z = Zu(ax, fontsize=14)
fit(ax, [A, B_REF, E, M, C, D], margin=0.08, pad_aspect=True)
z.poly([A, M, E], color=BLUE, lw=1.2, fill=BLUE, alpha=0.14)
z.poly([B_REF, M, C], color=RED, lw=1.2, fill=RED, alpha=0.22)
z.line(A, B_REF, color=BLACK, lw=2.2)
z.line(M, E, color=BLACK, lw=2.2)
z.line(B_REF, C, color=BLACK, lw=1.6, ls='--')
z.parallel_chevron(A, B_REF, size=0.9)
z.parallel_chevron(M, E, size=0.9)
foot_h = M + (E - M) * (((E - M).conjugate() * (B_REF - M)).real / abs(E - M) ** 2)   # BからMEへの垂線の足（MとEの間）
assert 0 < ((E - M).conjugate() * (B_REF - M)).real / abs(E - M) ** 2 < 1
z.line(B_REF, foot_h, color=PURPLE, lw=1.6, ls='--')
z.right_angle(foot_h, E, B_REF, size=0.7, color=PURPLE)
foot_c = M + (B_REF - M) * (((B_REF - M).conjugate() * (C - M)).real / abs(B_REF - M) ** 2)
z.line(C, foot_c, color=GRAY, lw=1.4, ls=':')
foot_b = A + (M - A) * (((M - A).conjugate() * (B_REF - A)).real / abs(M - A) ** 2)
z.line(B_REF, foot_b, color=GRAY, lw=1.4, ls=':')
z.north_arrow()
for p, n in [(A, 'A'), (M, 'M'), (E, 'E'), (D, 'D')]:
    z.point(p, KIND[n])
    z.point_label(p, n, away=centroid([A, M, E]))
z.point(B_REF, 'stone', color=GRAY)
z.point_label(B_REF, 'B（参考）', away=centroid([A, M, E]), color=GRAY)
z.point(C, 'dot', color=RED, size=10)
z.callout(C, 'C（316.94, 305.93）', dirs=(-40, -20, -60, 0), color=RED, dists=(60, 80, 100))
z.edge_label(A, M, '21.70', centroid([A, B_REF, M]), fs=14)
z.edge_label(B_REF, M, '16.27', A, fs=14, outward=True)
z.callout(foot_h + (B_REF - foot_h) * 0.7, 'h（ABとEMの間の幅）', dirs=(60, 80, 40, 100), color=PURPLE, dists=(60, 80, 100))
z.edge_label(C, foot_c, '9.67', M, color=GRAY, fs=13, outward=False, ts=(0.5, 0.35, 0.65))
z.edge_label(B_REF, foot_b, '14.51', M, color=GRAY, fs=13, outward=True, ts=(0.5, 0.35, 0.65))
z.callout(centroid([B_REF, M, C]), '△BMC　16.27 × 9.67 ＝ 157.3309', dirs=(-25, -35, -45, -15), color=RED, dists=(260, 300, 340, 380))
z.callout(centroid([A, M, E]) + P(-1.5, -2.5), '△AMEの倍面積\n364.4865', dirs=(-100, -120, -80), color=BLUE, dists=(70, 90, 110))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu05_C_menseki_hi.png')

# =====================================================================
# 図6：C点の比較（ブロック塀の10.05m ⇔ 地積測量図から出したC）
# =====================================================================
fig, (ax1, ax2) = new_figure('図6　問2　C点はブロック塀の10.05mで置かない',
                             'ブロック塀・賃貸借契約書の図面の10.05mで置いたC′（316.84, 305.83）は、51番3の地積測量図から出したC（316.94, 305.93）よりMに0.14m寄る。\n'
                             '本件土地の面積：Cなら113.875 → 113㎡、C′なら114.479 → 114㎡（境内地は1㎡未満切捨て）。',
                             ncols=2, width_ratios=[1.1, 0.9])
za = Zu(ax1, fontsize=14)
fit(ax1, [M, E, C, D, H, J, K, I, L], margin=0.08, pad_aspect=True)
za.poly(HONKEN, fill=GREEN)
za.line(M, C, color=BLACK, lw=2.0)
za.line(D, E, color=BLACK, lw=2.0)
za.poly([M, L, K], color=BLACK, lw=1.4, closed=False)
za.north_arrow()
for p, n in [(M, 'M'), (E, 'E'), (D, 'D'), (H, 'H'), (J, 'J'), (K, 'K'), (I, 'I'), (L, 'L')]:
    za.point(p, KIND[n])
    za.point_label(p, n, away=INNER if n not in 'ML' else centroid(N51_2))
za.point(C, 'dot', color=RED, size=9)
za.point_label(C, 'C', away=INNER, color=RED)
za.callout(P(313.8, 316.0), '本件土地\nCなら 113.875 → 113㎡\nC′なら 114.479 → 114㎡', dirs=(60, 45, 75, 30), fs=14, dists=(110, 130, 150, 170))
za.edge_label(M, C, 'MC ＝ 10.19', centroid(N51_2), fs=14, color=RED)
za.free_text(centroid(N51_2), '51番2', fs=14, color=GRAY, offsets=((0, -20), (0, -34), (-20, -20)))
zb = Zu(ax2, fontsize=14)
ctr = (C + CW) / 2
fit(ax2, [ctr + P(-0.35, -0.35), ctr + P(0.35, 0.35)], margin=0.02, pad_aspect=True)
u = (E - M) / abs(E - M)
zb.line(ctr - u * 0.45, ctr + u * 0.45, color=BLACK, lw=2.0)
zb.north_arrow()
zb.point(C, 'dot', color=RED, size=12)
zb.callout(C, 'C（316.94, 305.93）\n地積測量図から', dirs=(-40, -20, -60), color=RED, dists=(55, 75, 95))
zb.point(CW, 'dot', color=GRAY, size=12)
zb.callout(CW, 'C′（316.84, 305.83）\nブロック塀の10.05m', dirs=(140, 160, 120), color=GRAY, dists=(55, 75, 95))
zb.free_text((C + CW) / 2, '0.14m', color=RED, fs=16, offsets=((-30, 18), (-40, 24), (30, -18)))
zb.free_text(ctr + u * 0.38, 'Eへ', fs=14, offsets=((14, -6), (20, -14)))
zb.free_text(ctr - u * 0.38, 'Mへ', fs=14, offsets=((14, -6), (20, -14)))
ax2.set_title('Cのまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H23_dai21mon_zu06_C_hikaku.png')

# =====================================================================
# 図7：C点の別解（真数表の45°19′48″・三斜の角度）
# =====================================================================
fig, (ax,) = new_figure('図7　問2　C点の別解（真数表の角度と三斜の角度）',
                        '真数表：M→E 44°29′07″、A→M 89°48′55″、その差45°19′48″が直線AMと直線MEのはさむ角。\n'
                        'h ＝ 21.70 × 0.71116 ＝ 15.4321…、MC ＝ 157.3309 ÷ 15.4321… ＝ 10.1949…。\n'
                        '三斜の角度：∠AMB 約63°06′（14.51 ÷ 16.27 から）、∠AME ＝ 180° − 45°19′48″ ＝ 134°40′12″、∠BMC 約71°34′。\n'
                        'MC ＝ 9.67 ÷ sin 約71°34′ ＝ 10.1929…。'
                        'どの解き方でも、丸めるとC（316.94, 305.93）。本番は Conjg の面積の比（図5）がいちばん速い。')
z = Zu(ax, fontsize=14)
fit(ax, [M + P(-3.2, -9.5), M + P(9.5, 9.0), C, B_REF], margin=0.05, pad_aspect=True)
z.line(M, M + (A - M) / abs(A - M) * 9.0, color=BLACK, lw=2.0)
z.line(M, M + (E - M) / abs(E - M) * 12.0, color=BLACK, lw=2.0)
z.line(M, B_REF, color=GRAY, lw=1.6, ls='--')
z.line(C, foot_c, color=RED, lw=1.6, ls='--')
z.right_angle(foot_c, M, C, size=0.5, color=RED)
b_ma, b_mb, b_me = bearing(M, A), bearing(M, B_REF), bearing(M, E) + 360
z.angle_arc(M, 1.4, b_ma, b_mb, color=BLUE)
z.angle_arc(M, 2.3, b_mb, b_me, color=RED)
z.angle_arc(M, 3.3, b_ma, b_me, color=PURPLE, arrow=False)
z.north_arrow()
z.point(M, 'stone')
z.point_label(M, 'M', away=M + P(1, 1))
z.point(C, 'dot', color=RED, size=10)
z.callout(C, 'C（316.94, 305.93）', dirs=(0, -20, 20), color=RED, dists=(55, 75, 95))
z.point(B_REF, 'stone', color=GRAY)
z.point_label(B_REF, 'B（参考）', away=M, color=GRAY)
z.free_text(M + (A - M) / abs(A - M) * 7.5, 'Aへ（A→M 89°48′55″）', fs=14, offsets=((0, 18), (0, 30), (20, 18)))
z.free_text(M + (E - M) / abs(E - M) * 11.0, 'Eへ（M→E 44°29′07″）', fs=14, ha='right', offsets=((-16, 6), (-24, 14), (-16, -12)))
z.callout(M + cmath.rect(1.4, math.radians(90 - (b_ma + b_mb) / 2)).conjugate() * 1j, '∠AMB 約63°06′', dirs=(-150, -170, -130),
          color=BLUE, dists=(60, 80, 100))
z.callout(M + cmath.rect(2.3, math.radians(90 - (b_mb + b_me) / 2)).conjugate() * 1j, '∠BMC 約71°34′', dirs=(100, 120, 80),
          color=RED, dists=(60, 80, 100))
z.callout(M + cmath.rect(3.3, math.radians(90 - (b_ma + b_me) / 2 - 20)).conjugate() * 1j, '∠AME 134°40′12″\n（180° − 45°19′48″）',
          dirs=(160, 180, 140), color=PURPLE, dists=(60, 80, 100))
z.edge_label(C, foot_c, '9.67', M, color=RED, fs=14, outward=False)
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu07_C_betsukai.png')

# =====================================================================
# 図8：問2 H点（E→Jは真南、交点から120°の向きに6.836m）
# =====================================================================
fig, (ax1, ax2) = new_figure('図8　問2　H点の求め方（E→Jの真南の線とD→Hの交点から6.836m）',
                             'E − J ＝ 23.34（iの係数0）でE→Jは真南。交点はEのX座標から9.732引いた（316.788, 315.34）。arg(交点 − D) ＝ 120°00′04.14″ で120°の線の上。\n'
                             'H ＝ E − 9.732 ＋ 6.836∠120° ＝ （313.37, 321.26）。6.836mをDから測った誤りの点は（316.89, 315.16）で、交点から0.21mしか離れない。',
                             ncols=2, width_ratios=[1.25, 0.75])
za = Zu(ax1, fontsize=14)
fit(ax1, [C, D, E, H, J, K, I], margin=0.08, pad_aspect=True)
za.poly(HONKEN, color=GRAY, lw=1.4, fill=GREEN, alpha=0.12)
za.line(E, J, color=BLUE, lw=1.8, ls='--')
za.line(D, E, color=BLACK, lw=1.8)
za.line(D, H, color=RED, lw=2.6)
za.line(D, D + P(3.2, 0), color=GRAY, lw=1.2, ls='--')
za.angle_arc(D, 1.6, 0, 120, color=RED)
za.north_arrow()
for p, n in [(D, 'D'), (E, 'E'), (J, 'J'), (C, 'C'), (K, 'K'), (I, 'I')]:
    za.point(p, KIND[n])
    za.point_label(p, n, away=INNER)
za.point(PX, 'dot', color=BLUE, size=8)
za.callout(PX, '交点（316.788, 315.34）', dirs=(20, 40, 0), color=BLUE, dists=(60, 80, 100))
za.point(H, 'dot', color=RED, size=10)
za.callout(H, 'H（313.37, 321.26）', dirs=(-60, -80, -40, -100), color=RED, dists=(45, 60, 75, 90))
za.edge_label(E, PX, '9.732', D, color=BLUE, fs=14, outward=True)
za.edge_label(PX, H, '6.836', J, color=RED, fs=14, outward=True)
za.free_text(D + P(1.9, 0.6), '120°', color=RED, fs=15, offsets=((14, 8), (24, 14), (30, 0), (20, 26)))
za.callout(E + (J - E) * 0.8, 'E→Jは真南\nE − J ＝ 23.34', dirs=(0, 20, -20), color=BLUE, dists=(55, 75, 95))
zb = Zu(ax2, fontsize=14)
fit(ax2, [PX + P(-0.55, -0.55), PX + P(0.55, 0.55)], margin=0.02, pad_aspect=True)
zb.line(PX + P(0.5, 0), PX + P(-0.5, 0), color=BLUE, lw=1.8, ls='--')
u = cmath.rect(1, dms(120))
zb.line(PX - u * 0.9, PX + u * 0.5, color=RED, lw=2.2)
zb.north_arrow()
zb.point(PX, 'dot', color=BLUE, size=10)
zb.callout(PX, '交点', dirs=(40, 60, 20), color=BLUE, dists=(50, 70))
zb.point(HW, 'dot', color=GRAY, size=11)
zb.callout(HW, 'Dから6.836mと\n読んだ誤り\n（316.89, 315.16）', dirs=(-100, -120, -80, -140), color=GRAY, dists=(60, 80, 100, 120))
zb.free_text((HW + PX) / 2, '0.21m', color=RED, fs=15, offsets=((0, 28), (-10, 36), (10, 40), (0, 50)))
zb.free_text(PX + u * 0.42, 'Hへ', color=RED, fs=14, offsets=((10, 10), (18, 16)))
ax2.set_title('交点のまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H23_dai21mon_zu08_H_kousa.png')

# =====================================================================
# 図9：問1 時効取得（固定配置）
# =====================================================================
fig, ax = fixed_figure('図9　問1　時効取得の要件と問題文の事実',
                       '買い受けるまでは地主から借りていた（所有の意思がない）ので、占有の開始は昭和26年8月19日。20年で完成しているので民法第162条第1項。')
TL = [(8, '昭和初期〜', '地主から借りて\n神社の敷地に', GRAY), (30, '昭和26年8月19日', '50番1・51番2を買受け\n占有開始（起算日）', RED),
      (55, '昭和46年8月19日', '取得時効の完成\n（20年）', RED), (80, '平成23年6月10日', '時効取得の手続\n（A財務事務所）', BLACK)]
ax.annotate('', xy=(96, 86), xytext=(4, 86), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, head, body, col in TL:
    ax.plot([x], [86], 'o', ms=12, color=col)
    ax.text(x, 91, head, ha='center', fontsize=17, weight='bold', color=col)
    ax.text(x, 79, body, ha='center', va='top', fontsize=15, color=BLACK)
ax.annotate('', xy=(54, 70), xytext=(31, 70), arrowprops=dict(arrowstyle='<|-|>', lw=2.0, color=RED))
ax.text(42.5, 66.5, '20年間', ha='center', fontsize=17, color=RED, weight='bold')
REQ = [('他人の物', '本件土地は国有財産（A財務事務所で確認）'),
       ('所有の意思', '買い受けてから、神社の敷地（神楽殿の敷地・参道）として維持・管理'),
       ('平穏かつ公然', '一般に開放、神楽殿の建築・参道の整備。所有の問合せ・測量もなし'),
       ('20年間の継続', '昭和26年8月19日から昭和46年8月19日まで')]
ax.add_patch(FancyBboxPatch((6, 6), 88, 52, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=RED, lw=2.0))
ax.text(9, 53, '要件（民法第162条第1項）と問題文の事実', fontsize=20, weight='bold', va='center', color=RED)
for k, (req, fact) in enumerate(REQ):
    y = 43 - k * 10.5
    ax.text(10, y, req, fontsize=18, weight='bold', va='center', color=RED)
    ax.text(32, y, fact, fontsize=16, va='center', color=BLACK)
path = os.path.join(OUT, 'H23_dai21mon_zu09_jikou_youken.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図9: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図10：問3 本件土地の面積と地目
# =====================================================================
fig, (ax,) = new_figure('図10　問3　本件土地の面積と地目（境内地・1㎡未満切捨て）',
                        'C→D→H→J→K→Iを座標法で：倍面積 227.75 → 113.875㎡。境内地（準則第68条第13号）は宅地ではないので1㎡未満を切り捨てて113㎡。\n'
                        '宅地と誤ると113.87、ブロック塀の10.05mでCを置くと114.479 → 114㎡。')
z = Zu(ax, fontsize=14)
fit(ax, HONKEN + [T2, P(322.5, 322.0)], margin=0.08, pad_aspect=True)
z.poly(HONKEN, fill=GREEN, lw=2.6)
z.line(D, E, color=GRAY, lw=1.4)
z.line(M, C, color=GRAY, lw=1.4)
z.line(K, L, color=GRAY, lw=1.4)
z.line(J, G + (J - G) * 0.6, color=GRAY, lw=1.4)
z.north_arrow()
for p, n in [(C, 'C'), (D, 'D'), (H, 'H'), (J, 'J'), (K, 'K'), (I, 'I')]:
    z.point(p, KIND[n])
    z.point_label(p, n, away=INNER)
z.free_text(INNER, '本件土地\n113.875㎡\n→ 113㎡', fs=17, color=GREEN, weight='bold',
            offsets=((0, 0), (0, -16), (10, 0)))
z.callout(I + (K - I) * 0.3, '神楽殿の敷地と参道\n＝ 境内地', dirs=(180, 160, -160), color=BLACK, dists=(90, 110, 130))
z.callout(H + (J - H) * 0.5, '宅地なら 113.87（誤り）', dirs=(0, 20, -20), color=GRAY, dists=(70, 90, 110))
z.callout(C, 'C′（ブロック塀）なら\n114.479 → 114㎡（誤り）', dirs=(150, 170, 130), color=GRAY, dists=(70, 90, 110))
for p, q, n in SIDES:
    z.edge_label(p, q, n, INNER, fs=13)
z.free_text(P(301.5, 316.0), '道　路', fs=15, color=GRAY, offsets=((0, 0), (0, -12), (20, 0)))
z.free_text(P(318.0, 322.5), '50－1', fs=14, color=GRAY, offsets=((0, 0), (0, 14), (16, 0)))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu10_menseki_chimoku.png')

# =====================================================================
# 図11：問3 申請書の整理（固定配置）
# =====================================================================
fig, ax = fixed_figure('図11　問3　申請書の考え方（登記原因・添付書類・地番）',
                       '取得原因（時効取得）と表題登記の登記原因（土地が生じた原因）を混ぜない。添付書類は今の法令で会社法人等番号（出題当時の扱いは注で添える）。')
BOX11 = [
    (4, 54, 44, 40, '登記原因及びその日付', RED,
     ['表題登記の登記原因＝土地が生じた原因', '本件土地はいつ・どうしてできたか分からない', '→「不詳」',
      '「昭和26年8月19日時効取得」は取得原因'], [2]),
    (52, 54, 44, 40, '時効取得はどこに出る？', BLUE,
     ['所有権を有することを証する情報', '（不動産登記令別表4の項添付情報欄ハ）', '→ A財務事務所の書面＝所有権証明書'], [2]),
    (4, 6, 44, 42, '添付書類', PURPLE,
     ['土地所在図　地積測量図', '所有権証明書　会社法人等番号', '代理権限証書', '（出題当時は会社法人等番号がなく住所証明書を付け、', '　資格証明書は問題文の注5で不要）'], [1]),
    (52, 6, 44, 42, '土地の表示', GREEN,
     ['所在：A市B町五丁目', '①地番：空欄（登記官が付ける）', '②地目：境内地（準則第68条第13号）',
      '③地積：113（1㎡未満切捨て）', '登録免許税の欄はない（非課税）'], [2, 3]),
]
for x, y, w, hh, head, col, lines, red in BOX11:
    ax.add_patch(FancyBboxPatch((x, y), w, hh, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=col, lw=2.0))
    ax.text(x + 2, y + hh - 4, head, fontsize=20, weight='bold', va='center', color=col)
    for i, t in enumerate(lines):
        ax.text(x + 3, y + hh - 11 - i * 5.4, t, fontsize=16, va='center', color=RED if i in red else BLACK)
path = os.path.join(OUT, 'H23_dai21mon_zu11_shinseisho_seiri.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図11: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図12：問4 土地所在図（1/500）と地積測量図（1/250）の完成見本
# =====================================================================
fig, (ax1, ax2) = new_figure('図12　問4　土地所在図（1／500）と地積測量図（1／250）の完成見本',
                             '左：土地所在図は近傍類似の地図と同じ500分の1（問題文の注6、不動産登記規則第76条第2項）。地積測量図の用紙の余白に描く（準則第51条第3項）。\n'
                             '右：地積測量図は250分の1で1m ＝ 4mm。辺長は小数第3位を四捨五入（ICは8.6457…で8.65）。\n'
                             '座標値・系の番号・求積方法・地積は書かない（問題文の注3）。T2・T3は位置・名称・座標値を書く（問題文の注4）。地番の欄は空欄。',
                             ncols=2, width_ratios=[0.8, 1.2])
ext = lambda p, q, k: p + (q - p) / abs(q - p) * k  # noqa: E731
# 右の地積測量図（1/250）の表示範囲を先に決め、左の土地所在図は同じ1mあたりの長さの半分（1/500）で描く
fit(ax2, [C, D, H, J, K, I, T2, T3, P(295.5, 320.0), P(321.5, 333.0), P(317.0, 302.8)], margin=0.06, pad_aspect=True)
w2 = ax2.get_xlim()[1] - ax2.get_xlim()[0]
m_per_in = w2 / (ax2.get_position().width * fig.get_size_inches()[0])
w1 = 2 * m_per_in * ax1.get_position().width * fig.get_size_inches()[0]
h1 = 2 * m_per_in * ax1.get_position().height * fig.get_size_inches()[1]
CEN = INNER + P(-2.0, 0.0)
LEFT_LINES = [(C, M, 9), (D, E, 9), (C, B_REF, 9), (D, D + (D - H), 7), (J, G, 11), (K, L, 8)]
fit(ax1, [CEN + P(-h1 / 2, -w1 / 2), CEN + P(h1 / 2, w1 / 2)], margin=0.0, pad_aspect=True)
for p, q, k in LEFT_LINES:   # 描く線の端点がすべて表示範囲に入ること
    e = ext(p, q, k)
    assert ax1.get_xlim()[0] < e.imag < ax1.get_xlim()[1] and ax1.get_ylim()[0] < e.real < ax1.get_ylim()[1]
za = Zu(ax1, fontsize=14)
za.poly(HONKEN, lw=2.0)
for p, q, k in LEFT_LINES:
    za.line(p, ext(p, q, k), lw=1.2)
za.north_arrow()
za.callout(INNER, '申請地', dirs=(-20, 0, -40), fs=15, dists=(50, 65, 80))
za.free_text(ext(D, D + (D - H), 4) + P(2.0, 2.0), '50－2', fs=14, offsets=((0, 0), (0, 12), (12, 0)))
za.free_text(H + P(4.0, 2.0), '50－1', fs=14, offsets=((0, 0), (0, 12), (12, 0)))
za.free_text(ext(C, M, 4) + P(3.0, -4.0), '51－3', fs=14, offsets=((0, 0), (-12, 0), (0, 12)))
za.free_text(I + P(-5.0, -5.0), '51－2', fs=14, offsets=((0, 0), (0, -12), (-12, 0)))
za.free_text(P(299.0, 314.0), '道　路', fs=14, offsets=((0, 0), (0, -12), (20, 0)))
za.free_text(CEN + P(-h1 * 0.36, 0), '縮尺　1／500', fs=15, weight='bold', offsets=((0, 0), (0, -14), (20, 0)))
ax1.set_title('土地所在図', fontsize=18, weight='bold', pad=6)
zb = Zu(ax2, fontsize=13)
zb.poly(HONKEN, lw=2.4)
for p, q, k in [(C, M, 1.5), (D, E, 1.5), (C, B_REF, 1.3), (D, D + (D - H), 1.3), (J, G, 2.0), (K, L, 1.5)]:
    zb.line(p, ext(p, q, k), lw=1.4)
zb.north_arrow()
for p, n in [(C, 'C'), (D, 'D'), (H, 'H'), (J, 'J'), (K, 'K'), (I, 'I')]:
    zb.point(p, KIND[n])
for p, q, n in SIDES:
    zb.edge_label(p, q, n, INNER, fs=13)
for p, n in [(C, 'C'), (D, 'D'), (H, 'H'), (J, 'J'), (K, 'K'), (I, 'I')]:
    zb.point_label(p, n, away=INNER, weight='normal')
for p, n in [(T2, 'T2'), (T3, 'T3')]:
    zb.point(p, 'kijun')
    zb.point_label(p, n, away=p + P(-1, 0), weight='normal')
zb.free_text(INNER, '申\n請\n地', fs=15, offsets=((0, 0), (10, 0), (-10, 0)))
zb.free_text(D + P(1.2, -1.8), '50－2', fs=13, offsets=((0, 0), (-10, 10), (0, 16)))
zb.free_text(H + P(2.5, 1.5), '50－1', fs=13, offsets=((0, 0), (12, 0), (0, 12)))
zb.free_text(C + P(0.2, -1.8), '51－3', fs=13, offsets=((0, 0), (-12, 0), (0, -12)))
zb.free_text(P(306.5, 307.8), '51－2', fs=13, offsets=((0, 0), (0, -12), (-12, 0)))
zb.free_text(P(301.5, 318.5), '道　路', fs=13, offsets=((0, 0), (0, -12), (20, 0)))
zb.free_text(P(298.2, 323.0), '基本三角点等の名称及び座標値\nT2　A市基準点T2　X 300.12　Y 306.99\nT3　A市基準点T3　X 299.47　Y 333.78',
             fs=12, offsets=((0, 0), (0, -10), (10, 0)))
zb.free_text(P(318.8, 327.0), 'C・D・H・I：コンクリート杭\nJ：市金属標　K：金属標\n測量年月日：平成23年8月10日\n（単位：m）',
             fs=12, offsets=((0, 0), (0, -12), (-12, 0)))
ax2.set_title('地積測量図', fontsize=18, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H23_dai21mon_zu12_shozaizu_sokuryouzu.png')

# =====================================================================
# 図13：本番で解く順番（固定配置）
# =====================================================================
fig, ax = fixed_figure('図13　本番で解く順番（いちばん重いのはC点と2つの作図）',
                       'C点がなくても、問1の全部と、申請書の地積以外の欄は書ける。重い計算と作図は後ろに回し、先に点を積む。')
STEPS = [('①', '問1を書き切る', '計算なし。要件の言葉と問題文の事実を4組（他人の物・所有の意思・平穏かつ公然・20年間）', BLACK),
         ('②', '問3の申請書の地積以外の欄', '土地表題登記・添付書類・申請人・所在・地番は空欄・境内地・不詳', BLACK),
         ('③', 'A点・M点・K点の放射', '時計回りで足す。AM ＝ 21.70 で51番3の地積測量図を確かめる', BLACK),
         ('④', 'H点', 'E→Jは真南。交点（316.788, 315.34）から120°の向きに6.836m', BLACK),
         ('⑤', 'C点', '面積の比 157.3309 ÷ 364.4865（ブロック塀の10.05mは使わない）', RED),
         ('⑥', '面積と地積', 'C→D→H→J→K→I で113.875 → 113㎡（境内地は1㎡未満切捨て）', RED),
         ('⑦', '辺長6本と2つの作図', '4.72・13.88・11.78・4.44・8.97・8.65。土地所在図1／500、地積測量図1／250', RED)]
for k, (no, head, body, col) in enumerate(STEPS):
    y = 90 - k * 13.2
    ax.add_patch(FancyBboxPatch((5, y - 4.8), 90, 9.6, boxstyle='round,pad=0.5', fc='#fff5f5' if col == RED else '#f7f7f7',
                                ec=col, lw=2.0))
    ax.text(8, y + 1.7, f'{no}　{head}', fontsize=19, weight='bold', va='center', color=col)
    ax.text(12, y - 2.4, body, fontsize=15, va='center', color=BLACK)
    if k < len(STEPS) - 1:
        ax.annotate('', xy=(50, y - 8.2), xytext=(50, y - 5.6), arrowprops=dict(arrowstyle='-|>', lw=2.0, color=GRAY))
path = os.path.join(OUT, 'H23_dai21mon_zu13_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図13: 整理図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
