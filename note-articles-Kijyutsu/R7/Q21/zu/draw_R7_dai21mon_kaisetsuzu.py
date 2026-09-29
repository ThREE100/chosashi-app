"""令和7年度 第21問（土地）会話形式note記事の解説図9枚を、座標値から作図する（参照実装）。

`../prompt_R7_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。

実行: python3 note-articles-Kijyutsu/R7/Q21/zu/draw_R7_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, chiseki, intersect  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, BLACK, GRAY, RED, BLUE, ORANGE, GREEN,  # noqa: E402
                        PURPLE)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
A, B, C = P(184.31, 99.33), P(219.57, 99.33), P(219.57, 117.56)
E, F, G, H = P(184.31, 114.41), P(184.31, 130.08), P(193.50, 131.88), P(217.00, 131.88)
T1, T2 = P(185.31, 135.37), P(188.60, 92.18)
D = r2(radial(T2, T1, 25.81, dms(325, 6, 51)))
S_otsu = area([C, H, G, F, E, D])
hk = (S_otsu / 2 - area([D, C, H])) * 2 / (H.imag - D.imag)
K = r2(H - round(hk, 2))
I = B - 3.5
J = r2(C + (D - C) * 3.5 / (C.real - D.real))
O = intersect(D, C, K, H)[0]
ODK = (O.real - K.real) * (H.imag - D.imag) / 2
k = math.sqrt((ODK - 62.72) / ODK)
L, M = r2(O + (K - O) * k), r2(O + (D - O) * k)

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
EXPECT = {
    'D': (D, P(201.71, 114.41)), 'K': (K, P(199.98, 131.88)), 'I': (I, P(216.07, 99.33)),
    'J': (J, P(216.07, 116.94)), 'L': (L, P(203.64, 131.88)), 'M': (M, P(205.30, 115.04)),
}
for n, (got, want) in EXPECT.items():
    assert abs(got - want) < 1e-9, (n, got, want)
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'CH': (C, H, '14.55'), 'HK': (H, K, '17.02'), 'KG': (K, G, '6.48'), 'GF': (G, F, '9.36'),
         'FE': (F, E, '15.67'), 'ED': (E, D, '17.40'), 'DC': (D, C, '18.14'), 'DK': (D, K, '17.56')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
AREAS = {
    '乙土地': (S_otsu, 561.1905), '甲土地（D経由）': (area([A, B, C, D, E]), 559.8503),
    '甲土地（CE直線）': (area([A, B, C, E]), 587.2553), '乙土地（CE直線）': (area([C, H, G, F, E]), 533.7855),
    '△DCH': (area([D, C, H]), 131.92535), '10番1': (area([C, H, K, D]), 280.59505),
    '10番2': (area([D, K, G, F, E]), 280.59545), 'BCJI': (area([B, C, J, I]), 62.72),
    'MLKD': (area([M, L, K, D]), 62.7208), 'CHLM': (area([C, H, L, M]), 217.9026),
}
for n, (got, want) in AREAS.items():
    assert abs(got - want) < 5e-5, (n, got, want)
print('数値の照合: すべて一致')

KOU = [A, B, C, D, E]           # 甲土地（206番）
OTSU = [C, H, G, F, E, D]       # 乙土地（10番）
N1 = [C, H, K, D]               # 10番1（丙土地）
N2 = [D, K, G, F, E]            # 10番2（丁土地）


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
# 図1：全体像（北を上にして座標どおりに描き直した調査図素図）
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像（令和7年4月1日時点）',
                        '問題の調査図素図は少し傾いている。座標どおりに北を上にすると、AB・HG は南北、BC・EF は東西の直線だとわかる。\n'
                        '甲野花子の当初の説明（CとEを結ぶ直線）と、生垣の間で見つかった杭D（折れ点）の違いに注意。')
z = Zu(ax)
fit(ax, [A, B, C, H, G, F, E, T1, T2], margin=0.10, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.line(C, E, color=GRAY, lw=1.6, ls='--')
z.north_arrow()
cg, co = centroid(KOU), centroid(OTSU)
z.free_text(cg, '甲土地\n206番　畑\n559㎡', fs=17)
z.free_text(co, '乙土地\n10番　宅地\n556.00㎡', fs=17)
for p, n, ref in [(A, 'A', cg), (B, 'B', cg), (C, 'C', co), (D, 'D', co), (E, 'E', co), (F, 'F', co),
                  (G, 'G', co), (H, 'H', co)]:
    z.point(p, 'concrete' if n in 'ABCDEFH' else 'metal')
    z.point_label(p, n, away=ref)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.callout(C + (E - C) * 0.55, '花子の説明（CとEの直線）', dirs=(0, -20, 20), color=GRAY, dists=(90, 120))
z.edge_label(B, C, '205', cg, fs=15)
z.edge_label(C, H, '9', co, fs=15)
z.edge_label(H, G, '12', co, fs=15)
z.edge_label(G, F, '道路', co, fs=15)
z.edge_label(F, E, '11', co, fs=15)
z.edge_label(E, A, '207', cg, fs=15)
z.edge_label(A, B, '道路', cg, fs=15)
z.free_text(C, 'Ｓ市Ｎ町三丁目', fs=15, offsets=((-80, 40), (-100, 30)))
z.free_text(C, 'Ｓ市Ｔ町一丁目', fs=15, offsets=((80, 40), (100, 30)))
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：問1 D点（放射計算）
# =====================================================================
fig, (ax,) = new_figure('図2　問1　D点の求め方（T2から放射）',
                        'T2→T1の方向角 94°21′21.94″ に、時計回りの観測角 325°06′51″ を足す（360°を引いて 59°28′12.94″）。\n'
                        'その方向へ 25.81m 進んだ点がD。反時計回りに測ると、甲土地の外（南）に出てしまう。')
z = Zu(ax)
Dw = r2(T2 + cmath.rect(25.81, cmath.phase(T1 - T2) - dms(325, 6, 51)))   # 反時計回りに測った誤答
fit(ax, [T1, T2, D, Dw, B, C], margin=0.08, pad_aspect=True)
z.poly(KOU, color=GRAY, lw=1.2)
z.poly(OTSU, color=GRAY, lw=1.2)
z.line(T2, T2 + 9, color=GRAY, lw=1.2, ls='--')            # T2から北へ
z.free_text(T2 + 9, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(T2, T1, color=BLUE, lw=2.0)
z.line(T2, D, color=RED, lw=2.6)
z.line(T2, Dw, color=GRAY, lw=1.4, ls=':')
z.north_arrow()
z.angle_arc(T2, 5.0, 0, 94.356, color=BLUE)
z.angle_arc(T2, 3.2, 94.356, 59.470 + 360, color=RED, ls='-')
for p, kind in [(T1, 'kijun'), (T2, 'kijun'), (D, 'concrete')]:
    z.point(p, kind)
z.point(Dw, 'dot', color=GRAY)
z.edge_label(T2, T1, '後視（T1の方向）', T2 + P(10, 20), color=BLUE, fs=14, ts=(0.3, 0.22, 0.38), dists=(18, 24))
z.edge_label(T2, D, '25.81', T2 + P(10, 0), color=RED, fs=18, ts=(0.62, 0.7, 0.55, 0.8), dists=(20, 26, 32))
z.callout(T2 + P(3.6, 3.6), '方向角 94°21′21.94″\n（北から時計回りにT1の方向）', dirs=(150, 165, 135), color=BLUE,
          dists=(150, 180, 210))
z.callout(T2 + P(-2.0, -2.6), '観測角 325°06′51″\n（T1の方向から時計回り）', dirs=(235, 250, 220, 265), color=RED,
          dists=(110, 140, 170))
z.callout(D, 'D（201.71, 114.41）', dirs=(60, 30, 100, 0), color=RED)
z.callout(Dw, '反時計回りに測った誤り\n（172.27, 112.17）', dirs=(0, -20, 20, 180), color=GRAY)
z.callout(T2, 'T2（188.60, 92.18）', dirs=(-100, -60, -140), color=BLACK)
z.callout(T1, 'T1（185.31, 135.37）', dirs=(-100, -60, -140, 180), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu02_D_housha.png')

# =====================================================================
# 図3：問1・問2の前提　筆界点Dの裏付け（CE直線との比較）
# =====================================================================
fig, (ax1, ax2) = new_figure('図3　筆界はCとEの直線ではなく、杭Dで折れる',
                             '左：花子の当初の説明（CとEの直線）だと、甲土地が587.25㎡になり登記記録の559㎡と合わない。\n'
                             '右：杭Dを通すと甲土地は559.85㎡（畑は1㎡未満切捨てで559㎡）。登記記録と一致し、Dが筆界点だと裏付けられる。',
                             ncols=2)
zs = []
for ax, pts_k, pts_o, sk, so, head, col in [
    (ax1, [A, B, C, E], [C, H, G, F, E], '587.25㎡', '533.78㎡', '花子の説明（CとEの直線）', GRAY),
    (ax2, KOU, OTSU, '559.85㎡', '561.19㎡', '杭D（生垣の間）を通す', RED),
]:
    z = Zu(ax, fontsize=14)
    fit(ax, [A, B, C, H, G, F, E], margin=0.08, pad_aspect=True)
    z.poly(pts_k, fill=GREEN)
    z.poly(pts_o, fill=BLUE)
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=18, color=col, weight='bold', pad=6)
    z.free_text(centroid(pts_k), f'甲土地\n{sk}', fs=16)
    z.free_text(centroid(pts_o), f'乙土地\n{so}', fs=16)
    for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (E, 'E'), (F, 'F'), (G, 'G'), (H, 'H')]:
        z.point(p, 'concrete')
        z.point_label(p, n, away=centroid(OTSU) if n in 'CEFGH' else centroid(KOU))
    if pts_k is KOU:
        z.point(D, 'concrete', color=RED)
        z.point_label(D, 'D', away=centroid(OTSU), color=RED)
    zs.append(z)
zs[0].free_text(centroid([A, B, C, E]), '→ 登記記録の559㎡と合わない', color=GRAY, fs=14, offsets=((0, -45), (0, -60)))
zs[1].free_text(centroid(KOU), '→ 1㎡未満切捨てで559㎡\n　登記記録と一致', color=RED, fs=14,
                offsets=((-15, -50), (-30, -55), (-40, -65)))
ALL_PROBLEMS += save(fig, zs, 'R7_dai21mon_zu03_hikkai_D.png')

# =====================================================================
# 図4：問1 K点（面積2等分）
# =====================================================================
fig, (ax,) = new_figure('図4　問1　K点の求め方（乙土地を面積2等分）',
                        'HGは真北方向の直線（Y＝131.88）。△DHK の高さは D から HG までの距離＝Y座標の差 17.47。\n'
                        'HK ＝ (561.1905 ÷ 2 − 131.92535) × 2 ÷ 17.47 ＝ 17.02　→　K ＝ H − 17.02')
z = Zu(ax)
fit(ax, OTSU + [H + 3], margin=0.16, pad_aspect=True)
z.poly([D, C, H], color=BLACK, lw=0, fill=BLUE, check=False)
z.poly([D, H, K], color=BLACK, lw=0, fill=ORANGE, check=False)
z.poly(OTSU)
z.line(D, K, color=RED, lw=2.6)
z.line(D, H, color=GRAY, lw=1.2, ls='--')
foot = P(D.real, H.imag)
z.line(D, foot, color=GRAY, lw=1.4, ls='--')
z.right_angle(foot, H, D, size=0.7)
z.line(H, H + 2.5, color=GRAY, lw=1.2, ls='--')
z.line(G, G - 2.5, color=GRAY, lw=1.2, ls='--')
z.north_arrow()
z.free_text(centroid([D, C, H]), '△DCH\n131.925㎡', fs=15)
z.free_text(centroid([D, H, K]), '△DHK\n148.670㎡', fs=15, offsets=((0, 12), (0, 20)))
z.free_text(centroid(N2), '10番2\n280.59㎡', fs=16)
for p, n in [(C, 'C'), (H, 'H'), (K, None), (G, 'G'), (F, 'F'), (E, 'E'), (D, 'D')]:
    z.point(p, 'dot')
    if n:
        z.point_label(p, n, away=centroid(OTSU))
z.edge_label(D, foot, '高さ 17.47', D + P(6, 0), color=GRAY, fs=14, outward=False)
z.edge_label(H, K, 'HK ＝ 17.02', centroid(OTSU), color=RED, fs=16)
z.free_text(H + 2.9, 'Y＝131.88（H・K・G は一直線）', color=GRAY, fs=13, offsets=((70, 0), (90, 10)))
z.free_text(C + P(4.5, -2), '10番1 ＝ △DCH ＋ △DHK ＝ 280.595㎡\n→ 地積 280.59㎡（宅地は小数第2位未満切捨て）',
            fs=14, color=BLACK, offsets=((0, 0), (40, 0), (-40, 0)))
z.callout(K, 'K（199.98, 131.88）', dirs=(-20, 0, 20, -45), color=RED)
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu04_K_nitoubun.png')

# =====================================================================
# 図5：問2 公差の判定（数直線）
# =====================================================================
from zu_helpers import setup_font  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図5　問2　地積更正が必要かの判定（精度区分 甲2）', fontsize=24, weight='bold', y=0.96)
ax = fig.add_axes([0.06, 0.30, 0.88, 0.50])
ax.set_xlim(552.5, 563.5)
ax.set_ylim(-1.6, 2.4)
ax.axis('off')
ax.plot([552.8, 563.2], [0, 0], color=BLACK, lw=2)
for v in range(553, 564):
    ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1.2)
    ax.text(v, -0.28, f'{v}', ha='center', va='top', fontsize=13, color=GRAY)
ax.axvspan(556.00 - 2.32, 556.00 + 2.32, ymin=0.30, ymax=0.52, color=GREEN, alpha=0.25)
ax.text(556.0, 0.62, '公差の範囲（556.00 ± 2.32）', ha='center', va='bottom', fontsize=15, color=GREEN)
ax.plot([556.0], [0], 'o', ms=12, color=BLUE)
ax.text(556.0, -0.75, '登記記録\n556.00㎡', ha='center', va='top', fontsize=16, color=BLUE, weight='bold')
ax.plot([561.1905], [0], 'o', ms=12, color=RED)
ax.text(561.1905, -0.75, '実測\n561.1905㎡', ha='center', va='top', fontsize=16, color=RED, weight='bold')
ax.annotate('', xy=(561.1905, 1.55), xytext=(556.0, 1.55), arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
ax.text(558.6, 1.7, '差 5.19㎡ ＞ 公差 2.32㎡　→　範囲を超えている', ha='center', va='bottom', fontsize=17,
        color=RED, weight='bold')
fig.text(0.5, 0.15, '市街地地域（不動産登記規則第10条第2項第1号）の地積測量図の誤差の限度は精度区分 甲2 まで（同条第4項第1号）。\n'
         '問題文の表から 556.00㎡ の甲2の公差 2.32㎡ を読む。\n'
         '→ 分筆の前に、登記原因を「錯誤」とする地積更正の登記が必要（分筆と一の申請情報で申請する）',
         ha='center', va='center', fontsize=16)
fig.text(0.5, 0.05, '分筆後の各土地　10番1 280.59㎡・10番2 280.59㎡（宅地は小数第2位未満切捨て）', ha='center',
         va='center', fontsize=15, color=GRAY)
path = os.path.join(OUT, 'R7_dai21mon_zu05_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図5: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図6：問3 地積測量図（8月15日申請分）の完成見本
# =====================================================================
fig, (ax,) = new_figure('図6　問3　地積測量図（10番1・10番2）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm。辺長は小数第3位を四捨五入（GF は 9.3646 なので 9.36）。\n'
                        '座標値・地積・求積方法は書かない（注5）。基準点T1・T2は位置と点名だけ（注6）。')
z = Zu(ax)
fit(ax, OTSU + [T1, T2], margin=0.12, pad_aspect=True)
z.poly(OTSU, lw=2.0)
z.line(D, K, lw=2.0)
z.line(C, C + 5, color=BLACK, lw=1.0, ls='-.', check=True)
z.line(E, E - 5, color=BLACK, lw=1.0, ls='-.', check=True)
z.north_arrow()
co = centroid(OTSU)
for n, (p, q, s) in SIDES.items():
    ref = co if n != 'DK' else centroid(N1)
    z.edge_label(p, q, s, ref, fs=16, outward=(n != 'DK'))
z.free_text(centroid(N1), '（イ）\n10－1', fs=17)
z.free_text(centroid(N2), '（ロ）\n10－2', fs=17)
for p, n in [(C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (H, 'H')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=co)
for p, n in [(G, 'G'), (K, 'K')]:
    z.point(p, 'metal', size=9)
    z.point_label(p, n, away=co)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.edge_label(C, H, '９', co, fs=16, dists=(34, 44), rotate=False)
z.edge_label(H, K, '１２', co, fs=16, dists=(34, 44), rotate=False)
z.edge_label(G, F, '道路', co, fs=16, dists=(38, 48), rotate=False)
z.edge_label(F, E, '１１', co, fs=16, dists=(34, 44), rotate=False)
z.edge_label(D, C, '２０６', co, fs=16, dists=(40, 50), ts=(0.0, 0.1), rotate=False)
z.free_text(C, '２０５', fs=16, offsets=((-50, 22), (-65, 10), (-65, 35)))
z.free_text(E, '２０７', fs=16, offsets=((-50, -22), (-65, -10), (-65, -35)))
z.free_text(C, 'Ｓ市Ｎ町三丁目', fs=15, offsets=((-80, 50), (-95, 45), (-110, 40)))
z.free_text(C, 'Ｓ市Ｔ町一丁目', fs=15, offsets=((80, 50), (95, 45), (110, 40)))
z.free_text(P(183.0, 93.0), '（単位：ｍ）\n◎ コンクリート杭：C・D・E・F・H\n● 金属標：G・K\n△ 基準点：T1・T2', fs=13,
            ha='left', va='bottom', offsets=((0, 0), (0, 30), (0, 60)))
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu06_chiseki_sokuryouzu.png')

# =====================================================================
# 図7：問4 J点（I点から平行線）
# =====================================================================
fig, (ax,) = new_figure('図7　問4　J点の求め方（IJ ∥ BC）',
                        'BAは真南方向（Y＝99.33）なので I ＝ B − 3.5。BCは真東方向なので、IJ上の点はすべて X＝216.07。\n'
                        'J は直線CD上で X＝216.07 の点：J ＝ C ＋ (D − C) × 3.5 ÷ 17.86。台形BCJI ＝ (18.23 ＋ 17.61) ÷ 2 × 3.5 ＝ 62.72㎡')
z = Zu(ax)
fit(ax, [B, C, D, H, K, I + P(-6, 0)], margin=0.10, pad_aspect=True)
z.poly(KOU, color=BLACK, lw=1.8, check=False)
z.poly(N1, color=BLACK, lw=1.8, check=False)
for s in [(A, B), (B, C), (C, D), (D, E), (C, H), (H, K), (K, D)]:
    z.segments.append((xy(s[0]), xy(s[1])))
z.poly([B, C, J, I], color=RED, lw=0, fill=GREEN, alpha=0.3, check=False)
z.line(I, J, color=RED, lw=2.6)
z.line(I, I + P(0, 22.5), color=GRAY, lw=1.2, ls='--', check=False)
z.parallel_marks(B, C, n=2)
z.parallel_marks(I, J, n=2)
z.north_arrow()
z.free_text(centroid([B, C, J, I]), '62.72㎡（花子→一郎）', fs=15, offsets=((0, 0), (0, 3)))
z.free_text(P(207.0, 106.0), '206（甲土地・花子）', fs=16)
z.free_text(centroid(N1), '10番1（丙土地・一郎）', fs=16)
for p, n in [(B, 'B'), (C, 'C'), (D, 'D'), (H, 'H'), (K, 'K'), (I, 'I'), (J, 'J')]:
    z.point(p, 'dot', color=RED if n in 'IJ' else BLACK)
    if n not in 'IJ':
        z.point_label(p, n, away=centroid([B, C, J, I]) if n in 'BC' else centroid(N1))
z.edge_label(B, I, '3.5', centroid(KOU), color=RED, fs=16)
z.edge_label(B, C, 'BC ＝ 18.23', centroid([B, C, J, I]), fs=15)
z.edge_label(I, J, 'IJ ＝ 17.61', centroid([B, C, J, I]), fs=15)
z.free_text(I + P(0.5, 23.5), 'X＝216.07', color=GRAY, fs=13, offsets=((40, -10), (60, -14)))
z.callout(I, 'I（216.07, 99.33）', dirs=(-45, -60, -30), color=RED, dists=(40, 60, 80))
z.callout(J, 'J（216.07, 116.94）', dirs=(-60, -30, -90), color=RED)
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu07_J_heikousen.png')

# =====================================================================
# 図8：問4 L点（延長線の交点Oで相似）
# =====================================================================
fig, (ax1, ax2) = new_figure('図8　問4　L点・M点の求め方（DCとKHの延長の交点Oで相似）',
                             '左：DCとKHを北へ延ばすと、O（300.76, 131.88）で交わる。△ODK ＝ 100.7821… × 17.47 ÷ 2 ＝ 880.3318…㎡。\n'
                             '右：△OML ＝ △ODK − 62.72。相似比 k ＝ √(817.6118… ÷ 880.3318…) ＝ 0.9637…、L ＝ O ＋ (K − O) × k、M ＝ O ＋ (D − O) × k',
                             ncols=2, width_ratios=[1, 2.1])
za = Zu(ax1, fontsize=13)
fit(ax1, [O, D, K, E, F], margin=0.10, pad_aspect=True)
za.poly(N1, color=BLACK, lw=1.4)
za.poly(N2, color=GRAY, lw=1.0)
za.poly([O, D, K], color=GRAY, lw=0, fill=ORANGE, alpha=0.18, check=False)
za.line(C, O, color=GRAY, lw=1.3, ls='--')
za.line(H, O, color=GRAY, lw=1.3, ls='--')
za.north_arrow(length=0.07)
for p, n in [(O, None), (D, 'D'), (K, 'K'), (C, 'C'), (H, 'H')]:
    za.point(p, 'dot', color=RED if n is None else BLACK)
    if n:
        za.point_label(p, n, away=centroid([O, D, K]) if n != 'C' else H)
za.callout(P(245, 128.8), '△ODK 880.33㎡', dirs=(180, 200, 160), color=BLACK, dists=(60, 80, 100))
za.callout(O, 'O（300.76, 131.88）', dirs=(-150, 180, -120), color=RED)
za.edge_label(K, O, 'KO ＝ 100.78', centroid([O, D, K]), fs=12, color=GRAY)

zb = Zu(ax2)
fit(ax2, [C, H, K, D, M, L], margin=0.30, pad_aspect=True)
zb.poly(N1)
zb.poly([M, L, K, D], color=BLACK, lw=0, fill=PURPLE, alpha=0.28, check=False)
zb.line(M, L, color=RED, lw=2.6)
zb.parallel_marks(D, K, n=1)
zb.parallel_marks(M, L, n=1)
zb.north_arrow()
zb.free_text(centroid([M, L, K, D]), '62.72㎡（一郎→花子）', fs=15)
zb.free_text(centroid([C, H, L, M]), '残る10番1\n217.90㎡', fs=16)
for p, n in [(C, 'C'), (H, 'H'), (K, 'K'), (D, 'D'), (L, 'L'), (M, 'M')]:
    zb.point(p, 'dot', color=RED if n in 'LM' else BLACK)
    if n not in 'LM':
        zb.point_label(p, n, away=centroid(N1))
zb.callout(L, 'L（203.64, 131.88）', dirs=(35, 50, 20), color=RED, dists=(40, 55, 70))
zb.callout(M, 'M（205.30, 115.04）', dirs=(-130, -150, -110), color=RED, dists=(50, 70, 90))
zb.edge_label(D, K, 'DK ＝ 17.56', centroid([M, L, K, D]), fs=15)
zb.edge_label(M, L, 'ML ＝ 16.92', centroid([M, L, K, D]), fs=15)
zb.edge_label(K, L, 'KL ＝ 3.66', centroid(N1), fs=14, color=RED)
ALL_PROBLEMS += save(fig, [za, zb], 'R7_dai21mon_zu08_L_souji.png')

# =====================================================================
# 図9：問5 10月30日の分筆（地番の付け方）
# =====================================================================
fig, (ax,) = new_figure('図9　問5　10月30日の分筆（10番1 → （イ）10番1 ＋ （ロ）10番3）',
                        '10番2は8月の分筆ですでに使われているので、帯状地MLKDには本番10の最終の支号の次の10番3を付ける（北側の残地が10番1のまま）。\n'
                        '（イ）217.90㎡ ＋（ロ）62.72㎡ ＝ 280.62㎡。登記記録の280.59㎡との差 0.03㎡ は公差の範囲内なので、地積更正は不要。\n'
                        '地番の流れ　8月15日：10番 → 10番1（北）・10番2（南）　／　10月30日：10番1 → 10番1（北）・10番3（南）')
z = Zu(ax)
fit(ax, [B, C, H, G, F, E, A], margin=0.07, pad_aspect=True)
z.poly(KOU, color=GRAY, lw=1.2)
z.poly(N2, color=GRAY, lw=1.2)
z.poly([C, H, L, M], fill=BLUE)
z.poly([M, L, K, D], fill=PURPLE, alpha=0.3)
z.poly([B, C, J, I], color=GRAY, lw=1.0, ls='--', fill=GREEN, alpha=0.18)
z.north_arrow()
z.free_text(centroid([C, H, L, M]), '（イ）10番1\n217.90㎡', fs=17)
z.free_text(centroid([M, L, K, D]), '（ロ）10番3　62.72㎡', fs=15)
z.free_text(centroid(N2), '10番2（丁土地・二郎）\n変わらない', fs=15, color=GRAY)
z.free_text(centroid(KOU) - 4, '206（甲土地）\n※BCJIの分筆は甲土地側の\n　別の申請（問5の対象外）', fs=13, color=GRAY)
for p, n in [(C, 'C'), (H, 'H'), (L, 'L'), (K, 'K'), (D, 'D'), (M, 'M')]:
    z.point(p, 'metal' if n in 'KL' else 'concrete')
    z.point_label(p, n, away=centroid(N1))
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu09_bunpitsu_chiban.png')

print('重なりの合計:', len(ALL_PROBLEMS))
