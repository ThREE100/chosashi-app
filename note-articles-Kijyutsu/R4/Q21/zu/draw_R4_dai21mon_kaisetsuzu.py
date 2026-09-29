"""令和4年度 第21問（土地）会話形式note記事の解説図10枚を、座標値から作図する。

`../prompt_R4_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。

実行: python3 note-articles-Kijyutsu/R4/Q21/zu/draw_R4_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, area, chiseki  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
A, B, C, D = P(298.21, 273.89), P(279.30, 274.90), P(279.30, 303.07), P(301.13, 303.07)
E, F, G, H = P(298.09, 272.68), P(289.14, 272.74), P(279.30, 279.15), P(286.41, 274.52)
K, L = P(301.99, 311.25), P(296.75, 259.24)
T1, T2 = P(306.89, 305.35), P(303.64, 272.19)
Pp = r2(radial(T1, T2, 13.74, dms(338, 29, 30)))
Pw = r2(T1 + cmath.rect(13.74, cmath.phase(T2 - T1) - dms(338, 29, 30)))   # 反時計回りに測った誤り
J = P(C.real, Pp.imag)
I = r2(E + (D - E) * (Pp.imag - E.imag) / (D.imag - E.imag))
Dp = D + 1.49                                  # 拡幅前の道路の線の上の点（合成図）

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, (got, want) in {'P': (Pp, P(300.63, 293.12)), 'I': (I, P(300.13, 293.12)), 'J': (J, P(279.30, 293.12)),
                       '誤りのP': (Pw, P(310.66, 292.14))}.items():
    assert abs(got - want) < 1e-9, (n, got, want)
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731
SIDES = {'EA': (E, A, '1.22'), 'AI': (A, I, '19.33'), 'ID': (I, D, '10.00'), 'DC': (D, C, '21.83'),
         'CJ': (C, J, '9.95'), 'JG': (J, G, '13.97'), 'GH': (G, H, '8.48'), 'HF': (H, F, '3.26'),
         'FE': (F, E, '8.95'), 'IJ': (I, J, '20.83'), 'AH': (A, H, '11.82')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert d2(Dp, F) == '33.19' and d2(Dp, G) == '33.41' and d2(Dp, B) == '36.57' and d2(Pp, I) == '0.50'
HON = [E, D, C, G, F]          # 本件土地（筆界E→F→G）
ABQ = [A, D, C, B]             # AB線で囲んだ四角形
I1 = [C, D, I, J]              # （イ）184番1
RO = [A, I, J, G, H]           # （ロ）184番3
HA = [E, A, H, F]              # （ハ）184番4
HBG = [H, B, G]                # 185番3の一部（悠人→春野）
AREAS = {'本件土地': (HON, 584.8248), 'AB線': (ABQ, 584.84705), '（イ）': (I1, 212.2335),
         '（ロ）': (RO, 357.44415), '（ハ）': (HA, 15.0604), 'HBG': (HBG, 15.10875)}
for n, (pts, want) in AREAS.items():
    assert abs(area(pts) - want) < 5e-6, (n, area(pts), want)
assert chiseki(area(RO), takuchi=False) == 357 and chiseki(area(I1)) == 212.23 and chiseki(area(HA)) == 15.06
assert abs(area(I1) + area(RO) + area(HA) - 584.73805) < 5e-6
print('数値の照合: すべて一致')

ALL_PROBLEMS = []


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


def mark(z, p, n, away, color=BLACK):
    kind = {'A': 'metal', 'C': 'metal', 'J': 'metal', 'D': 'concrete', 'E': 'concrete', 'F': 'concrete',
            'G': 'concrete', 'I': 'concrete', 'B': 'metal'}.get(n, 'dot')
    z.point(p, kind, color=color)
    z.point_label(p, n, away=away, color=color)


# =====================================================================
# 図1：全体像
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像（令和4年10月14日の申請時）',
                        '問題の調査図素図は傾いている。座標どおりに北を上にすると、B・G・C は真東向き（X＝279.30）、C・D は真北向き（Y＝303.07）の直線。\n'
                        '春野朝子と夏野悠人が境だと思っていたAB線（灰色の破線）と、杭が見つかった筆界E→F→G（黒）の違いに注意。')
z = Zu(ax)
fit(ax, [L, K, B, C, T1, T2], margin=0.08, pad_aspect=True)
z.poly(HON, fill=BLUE)
z.line(L, K, color=BLACK, lw=1.4)
z.line(A, B, color=GRAY, lw=1.8, ls='--')
z.north_arrow()
co = centroid(HON)
z.free_text(co, '本件土地\n184番1　宅地\n584.75㎡', fs=17)
for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (H, 'H')]:
    mark(z, p, n, co)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
for p, n in [(K, 'K'), (L, 'L')]:
    z.point(p, 'dot', color=GRAY)
    z.point_label(p, n, away=co, color=GRAY)
z.callout(A + (B - A) * 0.35, 'AB線（2人の認識）', dirs=(180, 160, 200), color=GRAY, dists=(90, 120))
z.edge_label(D, C, '183番1', co, fs=15, rotate=False, dists=(40, 50))
z.edge_label(G, C, '196', co, fs=15, rotate=False, dists=(30, 40))
z.edge_label(F, E, '185番3', co, fs=15, rotate=False, dists=(45, 55))
z.edge_label(E, D, '道路（184番2）', co, fs=15, rotate=False, dists=(38, 48))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：AB線とE→F→Gの比較
# =====================================================================
fig, (ax1, ax2) = new_figure('図2　面積では筆界を決められない（AB線とE→F→G）',
                             '左：AB線で囲むと584.84㎡、右：E→F→Gで囲むと584.82㎡。どちらも登記記録の584.75㎡に近い。\n'
                             '西側のE・A・H・F（15.06㎡）と△HBG（15.10㎡）がほぼ同じ面積なので、差し引きでほとんど変わらない。',
                             ncols=2)
zs = []
for ax, pts, head, s, col in [(ax1, ABQ, 'AB線で囲む（2人の認識）', '584.84㎡', GRAY),
                              (ax2, HON, 'E→F→Gで囲む（杭の位置）', '584.82㎡', RED)]:
    z = Zu(ax, fontsize=14)
    fit(ax, [E, D, C, B], margin=0.22, pad_aspect=True)
    z.poly(pts, fill=BLUE)
    if pts is HON:
        z.poly(HA, color=ORANGE, lw=0, fill=ORANGE, alpha=0.45, check=False)
        z.poly(HBG, color=PURPLE, lw=1.2, ls='--', fill=PURPLE, alpha=0.35)
        z.line(A, B, color=GRAY, lw=1.2, ls='--')
    else:
        z.poly(HON, color=GRAY, lw=1.0, ls=':')
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=18, color=col, weight='bold', pad=6)
    z.free_text(centroid(pts), s, fs=18, color=col, weight='bold')
    for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (H, 'H')]:
        z.point(p, 'dot')
        z.point_label(p, n, away=centroid(pts))
    zs.append(z)
zs[1].callout(centroid(HA), 'E・A・H・F　15.06㎡', dirs=(-10, 10, -25), color=ORANGE, dists=(60, 80, 100))
zs[1].callout(centroid(HBG), '△HBG　15.10㎡', dirs=(-60, -40, -80), color=PURPLE, dists=(50, 70, 90))
ALL_PROBLEMS += save(fig, zs, 'R4_dai21mon_zu02_hikkai_hikaku.png')

# =====================================================================
# 図3：合成図の辺長で筆界を裏付ける
# =====================================================================
fig, (ax,) = new_figure('図3　合成図の33.19・33.41で筆界E→F→Gを裏付ける',
                        '合成図の対角線は、拡幅前の道路の線の上の点D′（D点から真北へ1.49）から引かれている。\n'
                        'D′からF点まで33.19、G点まで33.41で合成図と一致。AB線の端のB点までは36.57で、合成図のどこにもない。\n'
                        '拡幅前の道路の線は、E点から北へ1.37の点とD′を結んだ模式（問題文に座標はない）。')
z = Zu(ax)
fit(ax, [E, Dp, C, B], margin=0.14, pad_aspect=True)
z.poly(HON, fill=BLUE)
z.line(D, Dp, color=BLACK, lw=1.4)
z.line(E + 1.37, Dp, color=GRAY, lw=1.2, ls='-.')
z.line(Dp, F, color=RED, lw=2.0, ls='--')
z.line(Dp, G, color=RED, lw=2.0, ls='--')
z.line(Dp, B, color=GRAY, lw=1.2, ls=':')
z.north_arrow()
co = centroid(HON)
for p, n in [(D, 'D'), (C, 'C'), (G, 'G'), (F, 'F'), (E, 'E'), (B, 'B')]:
    z.point(p, 'dot', color=GRAY if n == 'B' else BLACK)
    z.point_label(p, n, away=co, color=GRAY if n == 'B' else BLACK)
z.point(Dp, 'dot', color=RED)
z.point_label(Dp, 'D′', away=co, color=RED)
z.edge_label(Dp, F, '33.19', C, color=RED, fs=17, ts=(0.5, 0.38, 0.62))
z.edge_label(Dp, G, '33.41', F, color=RED, fs=17, ts=(0.5, 0.62, 0.38))
z.edge_label(Dp, B, '36.57（合成図にない）', C, color=GRAY, fs=13, ts=(0.62, 0.72, 0.5))
z.free_text(D + 0.745, '1.49', fs=14, ha='left', offsets=((10, 0), (16, -6), (16, 6), (24, 0)))
z.callout(E + 1.37 + (Dp - E - 1.37) * 0.3, '拡幅前の道路の線（位置は模式）', dirs=(90, 120, 60), color=GRAY, dists=(40, 60))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu03_gouseizu.png')

# =====================================================================
# 図4：問1 P点（放射）
# =====================================================================
fig, (ax,) = new_figure('図4　問1　P点の求め方（T1から放射）',
                        'T1→T2の方向角は −95°35′51.58″（360°を足して 264°24′08.42″）。これに時計回りの観測角 338°29′30″ を足すと 242°53′38.42″。\n'
                        'その方向へ 13.74m 進んだ点がP。反時計回りに測ると、道路の北の向こう側に出てしまう。')
z = Zu(ax)
fit(ax, [T1 + P(1, 9), T2 + P(0, -2), Pp + P(-3, 0), Pw + P(1.5, 0)], margin=0.06, pad_aspect=True)
z.poly(HON, color=GRAY, lw=1.2)
z.line(L, K, color=GRAY, lw=1.2)
z.line(T1, T1 + 6, color=GRAY, lw=1.2, ls='--')
z.free_text(T1 + 6, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(T1, T2, color=BLUE, lw=2.0)
z.line(T1, Pp, color=RED, lw=2.6)
z.line(T1, Pw, color=GRAY, lw=1.4, ls=':')
z.north_arrow()
z.angle_arc(T1, 3.0, 0, 264.402, color=BLUE)
z.angle_arc(T1, 1.9, 264.402, 242.894 + 360, color=RED)
for p in (T1, T2):
    z.point(p, 'kijun')
z.point(Pp, 'dot', color=RED)
z.point(Pw, 'dot', color=GRAY)
z.edge_label(T1, Pp, '13.74', T1 + P(-10, 0), color=RED, fs=18, ts=(0.62, 0.72, 0.5), dists=(16, 22, 30))
z.callout(T1 + P(0.3, -3.0), '方向角 264°24′08.42″\n（北から時計回りにT2の方向）', dirs=(110, 130, 90), color=BLUE,
          dists=(90, 120, 150))
z.callout(T1 + P(-1.9, 0.2), '観測角 338°29′30″\n（T2の方向から時計回り）', dirs=(-20, -40, 0, -60), color=RED,
          dists=(90, 120, 150))
z.callout(Pp, 'P（300.63, 293.12）', dirs=(-120, -150, -100), color=RED)
z.callout(Pw, '反時計回りに測った誤り\n（310.66, 292.14）', dirs=(180, 160, 200), color=GRAY)
z.callout(T1, 'T1（306.89, 305.35）', dirs=(60, 40, 80), color=BLACK, dists=(90, 120, 150))
z.callout(T2, 'T2（303.64, 272.19）', dirs=(120, 150, 90), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu04_P_housha.png')

# =====================================================================
# 図5：問1 I点・J点
# =====================================================================
fig, (ax1, ax2) = new_figure('図5　問1　I点とJ点の求め方',
                             '左：BCは真東向きなので、Pを通りBCに直交する線は真北向き（Y＝293.12）。J ＝（279.30, 293.12）。\n'
                             '右（拡大）：I は直線ED上で Y＝293.12 の点。I ＝ E ＋ (D − E) × 20.44 ÷ 30.39。P（側溝の北の目印）はIの0.50m北。',
                             ncols=2, width_ratios=[1.35, 1])
za = Zu(ax1, fontsize=14)
fit(ax1, [E, D, C, B, Pp], margin=0.14, pad_aspect=True)
za.poly(HON, color=BLACK, lw=1.6)
za.poly(I1, color=RED, lw=0, fill=GREEN, alpha=0.25, check=False)
za.line(Pp, J, color=RED, lw=2.2)
za.right_angle(J, C, Pp, size=1.0, color=RED)
za.north_arrow(length=0.07)
co = centroid(HON)
for p, n in [(B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (G, 'G'), (F, 'F')]:
    za.point(p, 'dot')
    za.point_label(p, n, away=co)
za.point(J, 'dot', color=RED)
za.point(Pp, 'dot', color=RED)
za.point_label(Pp, 'P', away=co, color=RED)
za.callout(J, 'J（279.30, 293.12）', dirs=(-100, -70, -130), color=RED, dists=(40, 55, 70))
za.free_text(centroid(I1), '東側部分\n（高橋へ）', fs=14)
za.edge_label(Pp, J, 'Y＝293.12', co, color=RED, fs=13, ts=(0.3, 0.4, 0.2))

zb = Zu(ax2, fontsize=14)
Z1, Z2 = E + (D - E) * 0.60, E + (D - E) * 0.76
fit(ax2, [Z1, Z2, Pp + 0.9, I - 1.2], margin=0.05, pad_aspect=True)
zb.line(Z1, Z2, color=BLACK, lw=2.0)
zb.line(Z1 + 0.35, Z2 + 0.35, color=GRAY, lw=1.0)
zb.line(Z1 + 0.05, Z2 + 0.05, color=GRAY, lw=1.0)
zb.line(Pp + 0.6, I - 1.0, color=RED, lw=1.6, ls='--')
zb.north_arrow(length=0.08)
zb.point(Pp, 'dot', color=RED)
zb.point(I, 'concrete', color=RED)
zb.callout(Pp, 'P（300.63, 293.12）', dirs=(150, 180, 120), color=RED, dists=(60, 80))
zb.callout(I, 'I（300.13, 293.12）', dirs=(-30, -60, 0), color=RED, dists=(60, 80))
zb.free_text(I + (Pp - I) * 0.5, 'IP ＝ 0.50', color=RED, fs=15, ha='left', offsets=((20, 22), (30, 30), (20, 38), (40, 40)))
zb.free_text(Z1 + (Z2 - Z1) * 0.2 + 0.2, '側溝（位置は模式）', color=GRAY, fs=13, offsets=((0, 22), (0, 30)))
zb.edge_label(Z1, Z2, '直線ED（道路境界）', Pp, fs=13, ts=(0.25, 0.35, 0.75))
ALL_PROBLEMS += save(fig, [za, zb], 'R4_dai21mon_zu05_I_J.png')

# =====================================================================
# 図6：問2 筆界特定
# =====================================================================
fig, (ax,) = new_figure('図6　問2　筆界特定の定義（不動産登記法第123条）',
                        '筆界特定 ＝（ア：表題登記）がある一筆の土地及びこれに（イ：隣接）する他の土地について、筆界の現地における（ウ：位置）を特定すること\n'
                        '（その位置を特定することができないときは、その位置の（エ：範囲）を特定すること）。所有権界のAB線は、筆界特定で決めるものではない。')
z = Zu(ax)
fit(ax, [E, D, C, B, P(279.3, 262.0)], margin=0.10, pad_aspect=True)
z.poly(HON, color=GRAY, lw=1.2, check=False)
for s in [(E, D), (D, C), (C, G)]:
    z.segments.append((xy(s[0]), xy(s[1])))
ax.plot([xy(p)[0] for p in (E, F, G)], [xy(p)[1] for p in (E, F, G)], color=ORANGE, lw=38, alpha=0.25,
        solid_capstyle='round', solid_joinstyle='round', zorder=1)
z.poly([E, F, G], color=RED, lw=3.0, closed=False)
z.line(A, B, color=GRAY, lw=1.6, ls='--')
z.north_arrow()
co = centroid(HON)
for p, n in [(E, 'E'), (F, 'F'), (G, 'G'), (A, 'A'), (B, 'B')]:
    z.point(p, 'dot', color=RED if n in 'EFG' else GRAY)
    z.point_label(p, n, away=co, color=RED if n in 'EFG' else GRAY)
z.free_text(co, '184番1\n（ア：表題登記がある一筆の土地）', fs=15)
z.free_text(P(289.0, 267.3), '185番3\n（イ：隣接する他の土地）', fs=15)
z.callout(F + (G - F) * 0.5, 'ウ：筆界の「位置」（E→F→G）', dirs=(-150, 180, -120), color=RED, dists=(90, 120))
z.callout(E + (F - E) * 0.35 + P(0, 0.9), 'エ：決めきれないときは「位置の範囲」', dirs=(10, 25, -10), color=ORANGE,
          dists=(80, 110, 140))
z.callout(A + (B - A) * 0.62, 'AB線＝所有権界（筆界特定の対象外）', dirs=(0, 20, -20), color=GRAY, dists=(90, 120))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu06_hikkai_tokutei.png')

# =====================================================================
# 図7：問3の前提　地積更正の要否（数直線）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図7　問3　地積更正が要るかの判定（精度区分 乙1）', fontsize=24, weight='bold', y=0.96)
ax = fig.add_axes([0.06, 0.30, 0.88, 0.50])
ax.set_xlim(575.5, 594.0)
ax.set_ylim(-1.8, 2.6)
ax.axis('off')
ax.plot([576, 593.5], [0, 0], color=BLACK, lw=2)
for v in range(576, 594, 2):
    ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1.2)
    ax.text(v, -0.28, f'{v}', ha='center', va='top', fontsize=13, color=GRAY)
ax.axvspan(584.75 - 7.17, 584.75 + 7.17, ymin=0.34, ymax=0.50, color=GREEN, alpha=0.25)
ax.text(584.75, 1.05, '乙1の公差の範囲（584.75 ± 7.17）', ha='center', va='bottom', fontsize=15, color=GREEN)
ax.axvspan(584.75 - 2.39, 584.75 + 2.39, ymin=0.50, ymax=0.56, color=GRAY, alpha=0.25)
ax.text(584.75 + 2.6, 0.53, '（参考）甲2の範囲 ±2.39', ha='left', va='center', fontsize=12, color=GRAY)
ax.plot([584.75], [0], 'o', ms=12, color=BLUE)
ax.text(582.2, -0.75, '登記記録\n584.75㎡', ha='center', va='top', fontsize=16, color=BLUE, weight='bold')
ax.plot([584.8248], [0], 'o', ms=9, color=RED)
ax.plot([584.73805], [0], 'o', ms=9, color=PURPLE)
ax.text(587.6, -0.75, '分筆前の実測 584.8248㎡（差0.07）\n分筆後3筆の合計 584.73805㎡（差0.01）', ha='left', va='top',
        fontsize=14, color=RED, weight='bold')
ax.text(584.75, 1.8, '差はどちらも公差 7.17㎡ の範囲内　→　地積更正は不要', ha='center', va='bottom', fontsize=17,
        color=RED, weight='bold')
fig.text(0.5, 0.15, '本件土地の地域は村落地域（不動産登記規則第10条第2項第2号）。誤差の限度は精度区分 乙1 まで（同条第4項第2号）。\n'
         '問題文の表から 584.75㎡ の乙1の公差 7.17㎡ を読む。地目が宅地だからといって市街地地域の甲2にしない。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'R4_dai21mon_zu07_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図7: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図8：問3 分筆後の区画と地番・地目
# =====================================================================
fig, (ax,) = new_figure('図8　問3　分筆後の区画と地番・地目（土地一部地目変更・分筆登記）',
                        '問題文の注7：最も東の土地を184番1、その余は184番3から東側から順に（184番2は道路で使用済み）。\n'
                        '中央部分は令和4年10月5日から月極駐車場なので雑種地（1㎡未満切捨てで357㎡）。△HBGは185番3の土地で、この申請の対象外。')
z = Zu(ax)
fit(ax, [E, D, C, B, P(290.0, 262.0), P(290.0, 306.0)], margin=0.08, pad_aspect=True)
z.poly(I1, fill=GREEN)
z.poly(RO, fill=ORANGE)
z.poly(HA, fill=BLUE, alpha=0.4)
z.poly(HBG, color=GRAY, lw=1.0, ls='--')
z.north_arrow()
z.free_text(centroid(I1), '（イ）184番1\n宅地　212.23㎡\n東側部分\n→ 高橋優子へ', fs=15)
z.free_text(centroid(RO), '（ロ）184番3\n雑種地　357㎡\n中央部分（月極駐車場）\n春野朝子に残る', fs=15)
z.callout(centroid(HA), '（ハ）184番4　宅地　15.06㎡\n西側部分 → 夏野悠人へ', dirs=(150, 180, 120), color=BLUE,
          dists=(90, 120))
z.callout(centroid(HBG), '△HBG（185番3）\n悠人 → 春野（対象外）', dirs=(-150, 200, -120), color=GRAY, dists=(70, 95))
for p, n in [(A, 'A'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (H, 'H'), (I, 'I'), (J, 'J')]:
    z.point(p, 'dot')
    z.point_label(p, n, away=centroid(RO))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu08_bunpitsu_chiban.png')

# =====================================================================
# 図9：問4 地積測量図の完成見本
# =====================================================================
fig, (ax,) = new_figure('図9　問4　地積測量図（184番1・184番3・184番4）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm。辺長は小数第3位を四捨五入（AI は 19.3256 なので 19.33）。\n'
                        '座標値・地積・求積方法は書かない（問題文の注5）。基準点T1・T2は位置と点名だけ（問題文の注6）。H点には境界標がない。B点は描かない。')
z = Zu(ax)
fit(ax, HON + [T1, T2, P(275.5, 259.0)], margin=0.07, pad_aspect=True)
z.poly(HON, lw=2.0)
z.line(I, J, lw=2.0)
z.line(A, H, lw=2.0)
z.line(E, E + (E - D) * 0.10, lw=1.0)
z.line(D, D + (D - E) * 0.10, lw=1.0)
z.line(G, G + (G - C) * 0.25, lw=1.0)
z.line(C, C + (C - G) * 0.10, lw=1.0)
z.line(D, D + 1.8, lw=1.0)
z.line(C, C - 2.0, lw=1.0)
z.line(E, E + 1.8, lw=1.0)
z.north_arrow(pos=(0.07, 0.78))
co = centroid(HON)
for n, (p, q, s) in SIDES.items():
    if n == 'EA':
        z.free_text(E + (A - E) * 0.5, s, fs=15, offsets=((16, 24), (22, 30), (28, 36), (14, 40)))
        continue
    ref = {'IJ': centroid(I1), 'AH': centroid(RO)}.get(n, co)
    z.edge_label(p, q, s, ref, fs=15, outward=(n not in ('IJ', 'AH')),
                 dists=(9, 15, 22) if n != 'EA' else (12, 20, 28, 36), ts=(0.5, 0.38, 0.62, 0.28, 0.72) if n != 'EA' else (0.5, 0.7, 0.3))
z.free_text(centroid(I1), '（イ）\n184－1', fs=17)
z.free_text(centroid(RO), '（ロ）\n184－3', fs=17)
z.callout(centroid(HA), '（ハ）184－4', dirs=(200, 215, 230), fs=16, dists=(110, 140, 170))
for p, n in [(A, 'A'), (C, 'C'), (J, 'J')]:
    z.point(p, 'metal', size=9)
    z.point_label(p, n, away=co)
for p, n in [(D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (I, 'I')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=co)
z.point_label(H, 'H', away=co)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.edge_label(D, C, '１８３－１', co, fs=15, dists=(45, 55), rotate=False)
z.edge_label(G, C, '１９６', co, fs=15, dists=(40, 50), rotate=False)
z.edge_label(F, E, '１８５－３', co, fs=15, dists=(50, 60), rotate=False)
z.edge_label(E, D, '道路　１８４－２', co, fs=15, dists=(40, 50), rotate=False, ts=(0.4, 0.3))
z.free_text(D, '１８３－２', fs=15, offsets=((50, 22), (60, 30), (60, 10), (70, 45), (80, 55), (90, 20)))
z.free_text(E, '１８５－６', fs=15, offsets=((-70, 30), (-80, 40), (-80, 20)))
z.free_text(P(276.0, 259.5), '（単位：ｍ）\n● 金属標：A・C・J\n◎ コンクリート杭：D・E・F・G・I\n△ 基準点：T1・T2', fs=13,
            ha='left', va='bottom', offsets=((0, 0), (0, 30), (0, -30)))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu09_chiseki_sokuryouzu.png')

# =====================================================================
# 図10：問5 本人確認情報
# =====================================================================
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図10　問5　本人確認情報に明らかにする事項（不動産登記規則第72条第1項）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.12, 0.94, 0.78])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')


def box(x, y, w, h, text, ec=BLACK, fc='white', fs=17, color=BLACK, weight='normal'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.6', ec=ec, fc=fc, lw=2))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs, color=color, weight=weight)


box(20, 80, 60, 13, '第1号（必ず書く）\n面談した（①日時）、（②場所）及び（③その状況）', ec=RED, fc='#fdecea', fs=19, weight='bold')
ax.annotate('', xy=(30, 63), xytext=(45, 78), arrowprops=dict(arrowstyle='-|>', lw=2, color=GRAY))
ax.annotate('', xy=(70, 63), xytext=(55, 78), arrowprops=dict(arrowstyle='-|>', lw=2, color=GRAY))
ax.text(25, 71, '面識がある', ha='center', fontsize=17, color=GRAY)
ax.text(75, 71, '面識がない（本問）', ha='center', fontsize=17, color=RED, weight='bold')
box(4, 38, 40, 22, '第2号\n氏名を知り、かつ、面識がある旨\n及びその面識が生じた経緯', ec=GRAY, fs=17, color=GRAY)
box(52, 30, 44, 30, '第3号\n（④申請の権限）を有する（⑤登記名義人）\nであることを確認するために\n提示を受けた書類の内容\n及び（④申請の権限）を有する（⑤登記名義人）\nであると認めた理由', ec=RED, fc='#fdecea',
    fs=16)
box(52, 8, 44, 13, '本問：良夫から運転免許証の提示を受けた\n（第72条第2項第1号の書類）', ec=GRAY, fs=15, color=GRAY)
box(4, 8, 40, 20, '答え\n① 日時　② 場所　③ その状況（①〜③順不同）\n④ 申請の権限　⑤ 登記名義人', ec=BLUE, fc='#eaf1fb', fs=17,
    color=BLUE, weight='bold')
fig.text(0.5, 0.04, '合筆の登記には登記識別情報の提供が必要（不動産登記令第8条第1項第1号）。失念したときは、資格者代理人の本人確認情報を\n'
         '登記官が相当と認めれば、事前通知をしないで登記される（不動産登記法第23条第4項第1号）。', ha='center', va='bottom', fontsize=15)
path = os.path.join(OUT, 'R4_dai21mon_zu10_honnin_kakunin.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図10: 図式（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
