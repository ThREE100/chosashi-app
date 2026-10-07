"""令和7年度 第21問（土地）会話形式note記事の解説図18枚を、座標値から作図する（参照実装）。

`../prompt_R7_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。

実行: python3 note-articles-Kijyutsu/R7/Q21/zu/draw_R7_dai21mon_kaisetsuzu.py [出力フォルダ]

2026-10-07：最新の執筆指示書で照らし直し、図を記事の挿入順に振り直して18枚にした（PNG名の zu01〜zu18 が記事の順）。
作成済みの図（旧図1〜5・7〜12）は「作成済みの記事のほかの図は変えず、番号を振り直すときもその画像の中の文字は変えない」
のルールどおり、下のコメントとタイトルの「図N」を作成時の番号のまま残し、PNG名だけを付け替えた（書き出す画像は以前と同じ）。
新しく足した図（zu01・zu03・zu06・zu09・zu11・zu14）と、答案用紙の第3欄の書式で描き直した地積測量図（zu12）には図番を入れない。
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
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu02_zentaizu.png')

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
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu04_D_housha.png')

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
ALL_PROBLEMS += save(fig, zs, 'R7_dai21mon_zu05_hikkai_D.png')

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
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu07_K_nitoubun.png')

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
path = os.path.join(OUT, 'R7_dai21mon_zu10_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図5: 数直線（固定配置）\n  →', path)

# =====================================================================
# 問3 地積測量図（8月15日申請分）の完成見本　※2026-10-07に、試験の答案用紙の第3欄の書式で描き直した
#   （public/kijutsu/R07-tochi/a2.png：左上の「第3欄」、上の「地番」「土地の所在」の欄と「地積測量図」の表題、
#     下の「作成者（略）（令和７年○月○日作成）」「申請人（略）」「縮尺 1/250」は印刷済み）。画像の中に図番は入れない
# =====================================================================
from matplotlib.patches import Rectangle  # noqa: E402
setup_font()
fig = plt.figure(figsize=(16, 13), dpi=100)
fig.patch.set_facecolor('white')
FL = dict(transform=fig.transFigure, fill=False, edgecolor=BLACK)


def frect(x0, y0, x1, y1, lw=1.6):
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, lw=lw, **FL))


def fline(x0, y0, x1, y1, lw=1.4):
    fig.add_artist(plt.Line2D([x0, x1], [y0, y1], transform=fig.transFigure, color=BLACK, lw=lw))


SH = 0.215   # 答案用紙の枠の下端
frect(0.015, SH, 0.985, 0.99, lw=1.2)                       # 外枠（二重線）
frect(0.020, SH + 0.005, 0.980, 0.985, lw=2.2)
fig.text(0.03, 0.965, '第3欄', fontsize=17, weight='bold', va='center')
IL, IR, IT, IB = 0.085, 0.935, 0.905, 0.315                  # 図を描く枠
frect(IL, IB, IR, IT, lw=1.8)
fline(0.50, IT, 0.50, IT - 0.035)                            # 折り目の印（上・下）
fline(0.50, IB, 0.50, IB + 0.035)
frect(0.53, IT, 0.71, 0.955)                                 # 地番の欄
fline(0.60, IT, 0.60, 0.955)
fig.text(0.565, 0.93, '地　　番', fontsize=15, ha='center', va='center')
fig.text(0.655, 0.93, '10番1、10番2', fontsize=16, ha='center', va='center', weight='bold')
frect(0.53, IT - 0.045, IR, IT)                              # 土地の所在の欄
fline(0.60, IT - 0.045, 0.60, IT)
fig.text(0.565, IT - 0.0225, '土地の所在', fontsize=15, ha='center', va='center')
fig.text(0.625, IT - 0.0225, 'Ｓ市Ｔ町一丁目', fontsize=16, ha='left', va='center', weight='bold')
fig.text(0.825, 0.93, '地　積　測　量　図', fontsize=19, ha='center', va='center')
BB, BT = IB - 0.065, IB                                      # 下の作成者・申請人・縮尺の欄
frect(IL, BB, 0.48, BT)
fline(0.135, BB, 0.135, BT)
fig.text(0.110, (BB + BT) / 2, '作 成 者', fontsize=14, ha='center', va='center')
fig.text(0.30, (BB + BT) / 2 + 0.01, '（略）', fontsize=14, ha='center', va='center')
fig.text(0.475, BB + 0.012, '（令和７年○月○日作成）', fontsize=13, ha='right', va='center')
frect(0.505, BB, IR, BT)
fline(0.555, BB, 0.555, BT)
fig.text(0.530, (BB + BT) / 2, '申 請 人', fontsize=14, ha='center', va='center')
fig.text(0.70, (BB + BT) / 2, '（略）', fontsize=14, ha='center', va='center')
fline(0.845, BB, 0.845, BT)
fline(0.875, BB, 0.875, BT)
fig.text(0.860, (BB + BT) / 2, '縮尺', fontsize=14, ha='center', va='center')
fline(0.885, BB + 0.01, 0.925, BT - 0.01, lw=1.0)
fig.text(0.892, BT - 0.016, '1', fontsize=13, ha='center', va='center')
fig.text(0.915, BB + 0.016, '250', fontsize=13, ha='center', va='center')
fig.text(0.5, 0.115,
         '印刷済み：「第3欄」「地積測量図」、地番・土地の所在の欄の枠、作成者と申請人の「（略）」、作成日の欄、縮尺 1/250（作成者・申請人・縮尺は書かない）\n'
         '書くもの：地番（10番1、10番2）、土地の所在（Ｓ市Ｔ町一丁目）、図（縮尺1/250で 1m ＝ 4mm）、辺長8本、（イ）（ロ）の符号と地番、\n'
         '境界標の記号、方位記号（印刷されていないので必ず描く）、隣接地の地番、町界と町名、基準点T1・T2の位置と点名（問題文の注6）\n'
         '書かないもの：座標値・座標系の番号・地積と求積方法・測量年月日（問題文の注5）。辺長は小数第3位を四捨五入（GF は 9.3646 なので 9.36）',
         ha='center', va='center', fontsize=14, linespacing=1.6)
ax = fig.add_axes([IL + 0.01, IB + 0.01, IR - IL - 0.02, IT - IB - 0.065])
z = Zu(ax)
fit(ax, OTSU + [T1, T2], margin=0.18, pad_aspect=True)
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
z.free_text(P(177.0, 76.0), '（単位：ｍ）\n◎ コンクリート杭：C・D・E・F・H\n● 金属標：G・K\n△ 基準点：T1・T2', fs=13,
            ha='left', va='bottom', offsets=((0, 0), (0, 30), (30, 0), (0, 60)))
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu12_chiseki_sokuryouzu.png')

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
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu13_J_heikousen.png')

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
ALL_PROBLEMS += save(fig, [za, zb], 'R7_dai21mon_zu15_L_souji.png')

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
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu16_bunpitsu_chiban.png')

# =====================================================================
# 図10：問1 K点の別解（2つの三角形の面積の比でHGを分ける）
# =====================================================================
Q_DGFE = area([D, G, F, E])
T_DHK, T_DKG = S_otsu / 2 - area([D, C, H]), S_otsu / 2 - Q_DGFE
assert abs(Q_DGFE - 223.99265) < 1e-6 and abs(T_DKG - 56.6026) < 1e-6 and abs(T_DHK - 148.6699) < 1e-6
KG_alt = abs(H - G) * T_DKG / (T_DHK + T_DKG)
assert r2(G + (H - G) / abs(H - G) * KG_alt) == K
fig, (ax,) = new_figure('図10　問1　K点の別解（△DHKと△DKGの面積の比でHGを分ける）',
                        '北から△DCH、南から四角形DGFEを、それぞれ半分の280.59525㎡から引くと、△DHK 148.6699㎡と△DKG 56.6026㎡。\n'
                        '2つの三角形は頂点Dが共通で、底辺がどちらも直線HGの上にあるので高さが等しい。面積の比 ＝ HK：KG。\n'
                        'KG ＝ 23.50 × 56.6026 ÷ (148.6699 ＋ 56.6026) ＝ 6.4799…　→　K ＝ G ＋ 6.48（北へ）')
z = Zu(ax)
fit(ax, OTSU + [H + 3, G - 3], margin=0.16, pad_aspect=True)
z.poly([D, C, H], color=BLACK, lw=0, fill=GRAY, alpha=0.18, check=False)
z.poly([D, G, F, E], color=BLACK, lw=0, fill=GRAY, alpha=0.18, check=False)
z.poly([D, H, K], color=BLACK, lw=0, fill=ORANGE, check=False)
z.poly([D, K, G], color=BLACK, lw=0, fill=GREEN, check=False)
z.poly(OTSU)
z.line(D, K, color=RED, lw=2.6)
z.line(D, H, color=GRAY, lw=1.2, ls='--')
z.line(D, G, color=GRAY, lw=1.2, ls='--')
z.north_arrow()
z.free_text(centroid([D, C, H]), '△DCH\n131.92535㎡', fs=14, color=GRAY)
z.free_text(centroid([D, G, F, E]), '四角形DGFE\n223.99265㎡', fs=14, color=GRAY)
z.free_text(centroid([D, H, K]), '△DHK\n148.6699㎡', fs=14, offsets=((0, 10), (0, 20), (-20, 10)))
z.callout(centroid([D, K, G]), '△DKG 56.6026㎡', dirs=(-100, -120, -80, -140), color=GREEN, dists=(60, 80, 100))
for p, n in [(C, 'C'), (H, 'H'), (G, 'G'), (F, 'F'), (E, 'E'), (D, 'D')]:
    z.point(p, 'dot')
    z.point_label(p, n, away=centroid(OTSU))
z.point(K, 'dot', color=RED)
z.edge_label(H, K, 'HK ＝ 17.02', centroid(OTSU), color=ORANGE, fs=15)
z.edge_label(K, G, 'KG ＝ 6.48', centroid(OTSU), color=GREEN, fs=15)
z.callout(K, 'K（199.98, 131.88）', dirs=(-20, 0, 20, -45), color=RED)
z.free_text(C + P(4.5, -2), 'HK：KG ＝ △DHK：△DKG\n＝ 148.6699：56.6026（HG ＝ 23.50）', fs=14,
            offsets=((0, 0), (40, 0), (-40, 0)))
ALL_PROBLEMS += save(fig, [z], 'R7_dai21mon_zu08_K_menseki_hi.png')

# =====================================================================
# 図11：問5 10月30日の申請までの時系列（名義・住所と、要る添付情報）
# =====================================================================
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図11　問5　10月30日の申請の日に、10番1は「誰の名義で、どの住所」か', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.20, 0.94, 0.66])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
EV = [  # (x, 日付, 出来事, 色, 上下)
    (4, '4月1日', '甲野太郎が死亡', GRAY, 1),
    (15, '8月10日', '遺産分割協議', GRAY, -1),
    (27, '8月15日', '地積更正・分筆を申請\n（相続人が申請）', BLUE, 1),
    (39, '8月31日', '相続による所有権の\n登記を申請', GRAY, -1),
    (51, '9月20日', '同上 完了\n10番1が一郎の名義に', GREEN, 1),
    (63, '10月1日', '一郎がT町一丁目\n10番1号へ転居', GRAY, -1),
    (75, '10月20日', '住所変更登記 完了\n登記記録も新住所に', GREEN, 1),
    (91, '10月30日', '分筆を申請（問5）', RED, 1),
]
ax.annotate('', xy=(98, 50), xytext=(1, 50), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, d, t, col, ud in EV:
    ax.plot([x], [50], 'o', ms=13, color=col, zorder=5)
    ax.plot([x, x], [50, 50 + ud * 12], color=col, lw=1.4)
    ax.text(x, 50 + ud * 14, d, ha='center', va='bottom' if ud > 0 else 'top', fontsize=15, color=col, weight='bold')
    ax.text(x, 50 + ud * 22, t, ha='center', va='bottom' if ud > 0 else 'top', fontsize=13, color=BLACK)
# 10番1の登記記録の名義・住所の帯
for x0, x1, t, col, tx in [(1, 51, '登記名義人：甲野太郎（亡）', GRAY, 26), (51, 75, '甲野一郎　S市M町二丁目3番5号', ORANGE, 63),
                           (75, 98, '甲野一郎　S市T町一丁目\n10番1号', GREEN, 83)]:
    ax.add_patch(plt.Rectangle((x0, 4), x1 - x0, 9, color=col, alpha=0.22, lw=0))
    ax.text(tx, 8.5, t, ha='center', va='center', fontsize=13)
ax.text(1, 15, '10番1の登記記録', fontsize=13, color=GRAY, va='bottom')
ax.plot([91, 91], [13.5, 50], color=RED, lw=1.5, ls='--')
fig.text(0.5, 0.115, '10月30日の時点で、10番1は相続による所有権の登記が済み（9月20日）、住所変更登記も済んでいる（10月20日）。', ha='center',
         fontsize=16)
fig.text(0.5, 0.06, '→ 申請人は「S市T町一丁目10番1号　甲野一郎」。相続を証する情報も、住所のつながりを証する情報も付けない\n'
         '（法定相続情報一覧図の写しの住所「S市M町二丁目3番5号」は、一覧図を作ったときの住所）', ha='center', va='center',
         fontsize=15, color=RED)
path = os.path.join(OUT, 'R7_dai21mon_zu17_jikeiretsu_10gatsu.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図11: 時系列（固定配置）\n  →', path)

# =====================================================================
# 図12：本番で解く順番（どの点が出れば、どの欄が書けるか）
# =====================================================================
fig = plt.figure(figsize=(16, 8), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図12　本番で解く順番　L点は最後に回す', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
STEPS = [
    ('①', 'D点（放射）', '第1欄 D', BLUE),
    ('②', 'K点（面積2等分）', '第1欄 K', BLUE),
    ('③', '問2の穴埋め', '第2欄 ア〜カ', BLUE),
    ('④', '地積測量図', '第3欄', BLUE),
    ('⑤', 'J点（平行線）', '第4欄 J', GREEN),
    ('⑥', '問5の申請書', '第5欄（地積は「（略）」）', GREEN),
    ('⑦', 'L点（相似・台形）', '第4欄 L（X座標だけ）', RED),
]
w, h, gap = 12.2, 42, 1.8
for i, (no, t, ran, col) in enumerate(STEPS):
    x = 1 + i * (w + gap)
    ax.add_patch(plt.Rectangle((x, 22), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
    ax.text(x + w / 2, 22 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
    ax.text(x + w / 2, 22 + h / 2 - 3, t.replace('（', '\n（', 1), ha='center', va='center', fontsize=17)
    ax.text(x + w / 2, 18, ran.replace('（', '\n（', 1), ha='center', va='top', fontsize=14, color=col)
    if i < len(STEPS) - 1:
        ax.annotate('', xy=(x + w + gap - 0.2, 43), xytext=(x + w + 0.2, 43),
                    arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
ax.text(1 + 1.5 * (w + gap), 76, '8月の分（D点とK点だけで全部書ける）', ha='center', fontsize=15, color=BLUE, weight='bold')
ax.annotate('', xy=(1 + 4 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
ax.text(1 + 5 * (w + gap) - gap / 2, 76, '10月の分（Lがなくても書ける）', ha='center', fontsize=15, color=GREEN, weight='bold')
ax.annotate('', xy=(1 + 6 * (w + gap) - gap, 72), xytext=(1 + 4 * (w + gap), 72),
            arrowprops=dict(arrowstyle='<->', lw=1.5, color=GREEN))
ax.text(1 + 6 * (w + gap) + w / 2, 76, 'いちばん重い', ha='center', fontsize=15, color=RED, weight='bold')
fig.text(0.5, 0.09, 'L点のY座標はHGと同じ131.88なので、残るのはX座標だけ（O点・△ODK 880.3318…・相似比 k ＝ 0.9637…）。\n'
         '問5の申請書は分筆後の地積の欄が「（略）」なので、L点・M点が出ていなくても完成できる。L点で時間切れになっても、ほかの欄は埋まっているようにする。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R7_dai21mon_zu18_kaku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図12: 解く順番（固定配置）\n  →', path)

# =====================================================================
# 2026-10-07追加の図（最新の執筆指示書で照らし直し）。画像の中に図番は入れない
#   zu01 全体の時系列、zu03 注の仕分け、zu06 2等分の基準、zu09 精度区分、zu11 一の申請情報、zu14 台形
# =====================================================================


def board(h=9):
    f = plt.figure(figsize=(16, h), dpi=100)
    f.patch.set_facecolor('white')
    a = f.add_axes([0.03, 0.03, 0.94, 0.86])
    a.set_xlim(0, 100)
    a.set_ylim(0, 100)
    a.axis('off')
    return f, a


def put_board(f, name):
    path = os.path.join(OUT, name)
    f.savefig(path, dpi=100, facecolor='white')
    print(f'[重なり検査] {name}: 整理図（固定配置）\n  →', path)


# ---- zu01：全体の時系列（第1章） ----
fig, ax = board(8)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('全体の時系列　8月の申請が問1〜問3、10月の申請が問4・問5', fontsize=24, weight='bold', y=0.965)
EV = [  # (x, 日付, 出来事, 色, 上下)
    (3, '4月1日', '甲野太郎が死亡', GRAY, 1),
    (12, '6月5日', '法定相続情報\n一覧図の申出', GRAY, -1),
    (21, '8月10日', '遺産分割協議\n（D・Kで2等分）', GRAY, 1),
    (30, '8月12日', 'K点に\n金属標を設置', GRAY, -1),
    (39, '8月15日', '乙土地の地積更正\n・分筆を申請', BLUE, 1),
    (47, '8月25日', '同上 完了', BLUE, -1),
    (56, '8月31日', '相続による\n所有権の登記を申請', GRAY, 1),
    (65, '9月20日', '同上 完了', GRAY, -1),
    (74, '10月1日', '一郎が転居', GRAY, 1),
    (83, '10月20日', '住所変更登記 完了\nM点・L点に標識設置', GRAY, -1),
    (94, '10月30日', '丙土地（10番1）の\n分筆を申請', RED, 1),
]
ax.annotate('', xy=(99, 50), xytext=(0.5, 50), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, d, t, col, ud in EV:
    ax.plot([x], [50], 'o', ms=12, color=col, zorder=5)
    ax.plot([x, x], [50, 50 + ud * 10], color=col, lw=1.4)
    ax.text(x, 50 + ud * 11, d, ha='center', va='bottom' if ud > 0 else 'top', fontsize=14, color=col, weight='bold')
    ax.text(x, 50 + ud * 18, t, ha='center', va='bottom' if ud > 0 else 'top', fontsize=12, color=BLACK)
for x0, x1, t, col in [(17, 51, '8月の申請：問1（D・K）・問2・問3（地積測量図）', BLUE), (68, 99, '10月の申請：問4（J・L）・問5（申請書）', RED)]:
    ax.add_patch(plt.Rectangle((x0, 2), x1 - x0, 9, color=col, alpha=0.18, lw=0))
    ax.text((x0 + x1) / 2, 6.5, t, ha='center', va='center', fontsize=14, color=col, weight='bold')
fig.text(0.5, 0.035, '8月15日の申請は登記名義人（亡太郎）の相続人による申請。10月30日の申請の日には、10番1は一郎の名義で、住所も新しい住所になっている。',
         ha='center', fontsize=14)
put_board(fig, 'R7_dai21mon_zu01_jikeiretsu_zentai.png')

# ---- zu03：注の仕分け（第1章） ----
fig, ax = board(10)
fig.suptitle('注は2系統　問題文の注1〜8と、観測値の表の注1・2', fontsize=24, weight='bold', y=0.965)
BOX = [  # (x, y, w, h, 見出し, 本文, 色)
    (1, 52, 31, 44, '毎年ほぼ同じ決まり文句', '問題文の注1　行為・書類は全て適法\n問題文の注2　書面申請\n問題文の注7　字画を明確に、\n　　　　　　　訂正・加入・削除の仕方', GRAY),
    (34, 52, 31, 44, '計算の条件', '問題文の注3　座標値は小数第3位を\n　　　　　　　四捨五入\n問題文の注4　縮尺250分の1、\n　　　　　　　辺長は小数第3位を四捨五入', BLUE),
    (67, 52, 32, 44, '地積測量図に書かないもの', '問題文の注5　座標値・座標系の番号・\n　地積と求積方法・測量年月日は不要\n問題文の注6　基準点は位置と点名だけ\n　（座標値は書かない）', GREEN),
    (1, 4, 48, 42, '今年の答えに効く指示', '問題文の注8　分筆で新しい地番が生じるときは、\n　北側から順に付ける\n→ 8月：北が10番1・南が10番2\n→ 10月：残る北が10番1、帯状地は10番3', RED),
    (51, 4, 48, 42, '観測値の表の下の注（番号がかぶる）', '観測値の表の注1　観測角は時計回りの角度\n　→ ∠で足す（引くと甲土地の南の外に出る）\n観測値の表の注2　北はX軸の正方向\n　→ Z ＝ X ＋ Yi（X＝北、Y＝東）', ORANGE),
]
for x, y, w, h, t, b, col in BOX:
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=col, alpha=0.10, edgecolor=col, lw=2))
    ax.text(x + 1.5, y + h - 3, t, ha='left', va='top', fontsize=16, color=col, weight='bold')
    ax.text(x + 1.5, y + h - 11, b, ha='left', va='top', fontsize=13, linespacing=1.6)
fig.text(0.5, 0.02, '記事では「問題文の注○」「観測値の表の注○」と言い分ける（「注1」だけでは、どちらの注か分からない）', ha='center',
         fontsize=14, color=GRAY)
put_board(fig, 'R7_dai21mon_zu03_chuu_shiwake.png')

# ---- zu06：2等分の基準（登記記録の地積の半分ではなく、実測の面積の半分） ----
Kw = r2(H - round((278.00 - area([D, C, H])) * 2 / (H.imag - D.imag), 2))
assert Kw == P(200.28, 131.88)
NW, SW = area([C, H, Kw, D]), area([D, Kw, G, F, E])
assert abs(NW - 277.97455) < 5e-5 and abs(SW - 283.21595) < 5e-5, (NW, SW)
fig, (ax1, ax2) = new_figure('問1　2等分するのは「実測の面積」の半分',
                             '登記記録の556.00㎡は実測と合っていない（問2の質問）。その半分の278.00㎡で北側を作ると、HK 16.72・K（200.28, 131.88）で、\n'
                             '北側 277.97㎡・南側 283.21㎡と2等分にならない。実測の561.1905㎡の半分の280.59525㎡で作ると、北側・南側とも280.59㎡になる。',
                             ncols=2)
for ax, kk, col, head, tn, ts in [
        (ax1, Kw, GRAY, '登記記録の半分 278.00㎡（誤り）', '北側 277.97㎡', '南側 283.21㎡'),
        (ax2, K, RED, '実測の半分 280.59525㎡（正しい）', '北側 280.59㎡', '南側 280.59㎡')]:
    z = Zu(ax, fontsize=14)
    fit(ax, OTSU, margin=0.20, extra=[(150.0, 200.0)], pad_aspect=True)
    z.poly([C, H, kk, D], fill=BLUE)
    z.poly([D, kk, G, F, E], fill=ORANGE, alpha=0.18)
    z.line(D, kk, color=col, lw=2.6)
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=18, color=col, weight='bold', pad=6)
    z.free_text(centroid([C, H, kk, D]), tn, fs=16)
    z.free_text(centroid([D, kk, G, F, E]), ts, fs=16)
    for p, n in [(C, 'C'), (H, 'H'), (G, 'G'), (F, 'F'), (E, 'E'), (D, 'D')]:
        z.point(p, 'dot')
        z.point_label(p, n, away=centroid(OTSU))
    z.point(kk, 'dot', color=col)
    z.callout(kk, f'K（{kk.real:.2f}, {kk.imag:.2f}）', dirs=(-30, -50, -15, 20), color=col, dists=(50, 70, 90))
    z.edge_label(H, kk, f'HK ＝ {abs(H - kk):.2f}', centroid(OTSU), color=col, fs=14)
    ALL_PROBLEMS += z.check_overlaps('R7_dai21mon_zu06_nitoubun_kijun.png')
path = os.path.join(OUT, 'R7_dai21mon_zu06_nitoubun_kijun.png')
fig.savefig(path, dpi=100, facecolor='white')
print('  →', path)

# ---- zu09：精度区分は地域で決まる（「乙土地」の呼び名につられない） ----
fig, ax = board(9)
fig.suptitle('問2　精度区分は土地の呼び名ではなく地域で決まる', fontsize=24, weight='bold', y=0.965)
COLS = [('精度区分', '556.00㎡'), ('甲1', '0.93㎡'), ('甲2', '2.32㎡'), ('甲3', '4.64㎡'), ('乙1', '6.93㎡'), ('乙2', '13.91㎡'),
        ('乙3', '27.82㎡')]
cw, x0 = 13.4, 3.1
for i, (a, b) in enumerate(COLS):
    x = x0 + i * cw
    fc = '#d8f0dc' if a == '甲2' else ('#fbe3e3' if a == '乙1' else 'white')
    for yy, txt in [(78, a), (64, b)]:
        ax.add_patch(plt.Rectangle((x, yy), cw, 14, facecolor=fc, edgecolor=BLACK, lw=1.4))
        ax.text(x + cw / 2, yy + 7, txt, ha='center', va='center', fontsize=17)
ax.text(x0 + 2.5 * cw, 58, '市街地地域（不動産登記規則第10条第2項第1号）\n→ 誤差の限度は甲2まで（同条第4項第1号）', ha='center', va='top',
        fontsize=14, color=GREEN, weight='bold')
ax.text(x0 + 4.5 * cw, 41, '「乙土地」はただの呼び名\n乙1で比べるのは誤り', ha='center', va='top', fontsize=14, color=RED,
        weight='bold')
ax.plot([x0 + 4 * cw + 1, x0 + 5 * cw - 1], [65, 77], color=RED, lw=2.4)
ax.plot([x0 + 4 * cw + 1, x0 + 5 * cw - 1], [77, 65], color=RED, lw=2.4)
ax.text(50, 20, '差 561.1905 − 556.00 ＝ 5.19㎡（分筆後の合計 561.18 でも差 5.18㎡）', ha='center', fontsize=16)
ax.text(27, 8, '甲2 2.32㎡ と比べる → ウ「超えています」\n→ エ「錯誤」オ「土地の地積の更正」カ「必要があります」', ha='center', va='center',
        fontsize=14, color=GREEN, weight='bold')
ax.text(75, 8, '乙1 6.93㎡ と比べると「超えていません」\n→ ウ・エ・オ・カの4つが全部崩れる', ha='center', va='center', fontsize=14,
        color=RED, weight='bold')
put_board(fig, 'R7_dai21mon_zu09_seido_kubun.png')

# ---- zu11：地積更正と分筆は一の申請情報 → 地積測量図は分筆後の2筆 ----
fig, (ax1, ax2) = new_figure('問3　地積更正と分筆は一の申請情報　地積測量図は分筆後の2筆を描く',
                             '同じ土地の表題部の更正の登記（地積の更正）と分筆の登記は、一の申請情報で申請できる（不動産登記規則第35条第7号）。\n'
                             '登記の目的は「土地地積更正・分筆登記」の1件なので「1件目の登記」はなく、添付するのは分筆後の10番1・10番2を表示した地積測量図。',
                             ncols=2)
for ax, split, col, head, txt in [
        (ax1, False, GRAY, '2件に分けて「1件目」の図（誤り）', '乙土地　10番\n（分筆線なし）'),
        (ax2, True, RED, '一の申請情報の図（正しい）', None)]:
    z = Zu(ax, fontsize=14)
    fit(ax, OTSU, margin=0.20, pad_aspect=True)
    z.poly(OTSU, fill=BLUE if split else GRAY)
    if split:
        z.line(D, K, color=RED, lw=2.6)
        z.free_text(centroid(N1), '（イ）10番1', fs=16)
        z.free_text(centroid(N2), '（ロ）10番2', fs=16)
    else:
        z.free_text(centroid(OTSU), txt, fs=16)
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=18, color=col, weight='bold', pad=6)
    for p, n in [(C, 'C'), (H, 'H'), (G, 'G'), (F, 'F'), (E, 'E'), (D, 'D')] + ([(K, 'K')] if split else []):
        z.point(p, 'dot')
        z.point_label(p, n, away=centroid(OTSU))
    ALL_PROBLEMS += z.check_overlaps('R7_dai21mon_zu11_ikkatsu_shinsei.png')
path = os.path.join(OUT, 'R7_dai21mon_zu11_ikkatsu_shinsei.png')
fig.savefig(path, dpi=100, facecolor='white')
print('  →', path)

# ---- zu14：M・L・K・D は平行四辺形ではなく台形 ----
hw = 62.72 / 17.56                                   # 平行四辺形のつもりの「高さ」3.5717…
nv = -(K - D) / abs(K - D) * 1j                      # DKに直角で北向きの単位ベクトル
Lw = r2(intersect(K, H, D + nv * hw, K + nv * hw)[0])
Mw = r2(intersect(D, C, D + nv * hw, K + nv * hw)[0])
assert Lw == P(203.57, 131.88) and Mw == P(205.24, 115.03), (Lw, Mw)
Aw = area([Mw, Lw, K, D])
assert abs(Aw - 61.6166) < 5e-5, Aw
fig, (ax, axr) = new_figure('問4　M・L・K・Dは平行四辺形ではなく台形',
                             '平行なのはMLとDKの1組だけ。DMは筆界CDの上、KLはHKの上で、CDとHKは平行でないので、北へ行くほど幅が狭くなる。\n'
                             '平行四辺形のつもりでDKから62.72 ÷ 17.56 ＝ 3.57離した線で切ると、L′（203.57, 131.88）・M′（205.24, 115.03）で\n'
                             '面積は61.61㎡しかない（1.11㎡足りない）。正しいL（203.64, 131.88）・M（205.30, 115.04）なら62.72㎡',
                             ncols=2, width_ratios=[1.45, 1])
pos = axr.get_position()
axr.remove()
axL = fig.add_axes([pos.x0, pos.y0 + pos.height * 0.53, pos.width, pos.height * 0.45])
axM = fig.add_axes([pos.x0, pos.y0, pos.width, pos.height * 0.45])
z = Zu(ax)
fit(ax, [C, H, K, D], margin=0.12, pad_aspect=True)
z.poly(N1)
z.poly([M, L, K, D], color=BLACK, lw=0, fill=PURPLE, alpha=0.28, check=False)
z.line(M, L, color=RED, lw=2.6)
z.parallel_marks(D, K, n=1)
z.parallel_marks(M, L, n=1)
z.north_arrow()
z.free_text(centroid(N1) + P(4, 0), '残る10番1', fs=16)
z.free_text(centroid([M, L, K, D]), '台形 62.72㎡', fs=15)
for p, n in [(C, 'C'), (H, 'H'), (K, 'K'), (D, 'D'), (L, 'L'), (M, 'M')]:
    z.point(p, 'dot', color=RED if n in 'LM' else BLACK)
    z.point_label(p, n, away=centroid(N1) if n not in 'LM' else centroid([M, L, K, D]))
z.callout(C + (D - C) * 0.45, 'CD（筆界）は斜め', dirs=(0, 20, -20), color=BLACK, dists=(60, 80, 100))
z.callout(H + (K - H) * 0.45, 'HKは真南北', dirs=(180, 160, 200), color=BLACK, dists=(60, 80, 100))
zs = [z]
for axz, pt, ptw, n, other, ext in [(axL, L, Lw, 'L', H, (K, H)), (axM, M, Mw, 'M', C, (D, C))]:
    zz = Zu(axz, fontsize=13)
    c0 = (pt + ptw) / 2
    fit(axz, [c0 + P(0.16, 0.16), c0 - P(0.16, 0.16)], margin=0.0, pad_aspect=True)
    for spine in axz.spines.values():
        spine.set_visible(True)
    axz.axis('on')
    axz.set_xticks([])
    axz.set_yticks([])
    u = (L - M) / abs(L - M)
    zz.line(ext[0], ext[1], lw=2.0)
    zz.line(pt - u * 3, pt + u * 3, color=RED, lw=2.6, check=False)
    zz.line(ptw - u * 3, ptw + u * 3, color=GRAY, lw=2.0, ls='--', check=False)
    zz.point(pt, 'dot', color=RED, size=9)
    zz.point(ptw, 'dot', color=GRAY, size=9)
    zz.callout(pt, f'{n}（{pt.real:.2f}, {pt.imag:.2f}）', dirs=(150, 170, 130, -150, 30, 0), color=RED, dists=(50, 70, 90))
    zz.callout(ptw, f'{n}′（{ptw.real:.2f}, {ptw.imag:.2f}）', dirs=(-150, -170, -130, 150, -30, 0), color=GRAY,
               dists=(50, 70, 90))
    axz.set_title(f'{n}のあたりの拡大（平行四辺形のつもりの線は灰色の破線）', fontsize=13, color=BLACK, pad=4)
    zs.append(zz)
ALL_PROBLEMS += save(fig, zs, 'R7_dai21mon_zu14_daikei.png')

print('重なりの合計:', len(ALL_PROBLEMS))
