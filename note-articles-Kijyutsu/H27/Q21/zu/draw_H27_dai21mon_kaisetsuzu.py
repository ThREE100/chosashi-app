"""平成27年度 第21問（土地）会話形式note記事の解説図7枚を、座標値から作図する。

`../prompt_H27_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../R6/Q21/zu/draw_R6_dai21mon_kaisetsuzu.py`。

実行: python3 note-articles-Kijyutsu/H27/Q21/zu/draw_H27_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, chiseki  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標と、記事で求めた点） --------------------------------
T1, T2 = P(527.57, 483.20), P(512.57, 521.95)
B, C, D, E, F, G = P(475.50, 427.50), P(430.00, 427.50), P(430.00, 493.00), P(445.75, 493.00), P(500.00, 493.00), \
    P(500.00, 500.00)
I, J, L, M, N = P(442.25, 500.00), P(430.00, 500.00), P(500.00, 530.00), P(500.00, 537.00), P(470.00, 537.00)
A = r2(radial(T1, T2, 18.82, dms(136, 26, 37)))
K = r2(E + (N - I) * (530 - 493) / (537 - 500))
H = r2(E + (K - E) * (500 - 493) / (530 - 493))
Aw = r2(radial(T2, T1, 18.82, dms(136, 26, 37)))      # 器械点と後視点を入れ替えた誤り
Kw = P(470.00, 530.00)                                  # Nの真西にとった誤り
Hw = I + 7.00                                           # Iの真北7.00mにとった誤り


def dist_NI(p):
    """点pから直線NIまでの距離（三角形の倍面積のiの係数 ÷ NI）。"""
    return abs(((I - N).conjugate() * (p - N)).imag) / abs(I - N)


# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('A', A, P(520.40, 465.80)), ('K', K, P(473.50, 530.00)), ('H', H, P(451.00, 500.00)),
                     ('Aw', Aw, P(519.74, 539.35))]:
    assert abs(got - want) < 1e-9, (n, got, want)
assert f'{dist_NI(E):.2f}' == '7.00' and f'{dist_NI(K):.2f}' == '7.00'
assert f'{dist_NI(Kw):.2f}' == '4.20' and f'{dist_NI(Hw):.2f}' == '5.60'
assert Aw.imag - A.imag > 70   # 誤りのAは東へ約74m
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'LK': (L, K, '26.50'), 'KH': (K, H, '37.50'), 'HI': (H, I, '8.75'), 'IN': (I, N, '46.25'),
         'NM': (N, M, '30.00'), 'ML': (M, L, '7.00')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert d2(F, E) == '54.25' and d2(G, H) == '49.00' and d2(E, H) == '8.75'
I_1 = [A, B, C, D, E, F]            # 分筆後の（イ）100番1（宅地）
RO_3 = [F, E, H, G]                 # 分筆後の（ロ）100番3（用悪水路）＝甲土地の東側部分
KOU = [A, B, C, D, E, H, G, F]      # 甲土地（分筆前の100番1）
OTSU = [L, K, H, I, N, M]           # 乙土地
N1002 = [G, L, K, H]                # 100番2
SUIRO = [E, H, I, J, D]             # 南へ続く水路（無番地）
assert f'{area(I_1):.3f}' == '4783.925' and f'{chiseki(area(I_1)):.2f}' == '4783.92'
assert f'{area(RO_3):.3f}' == '361.375' and chiseki(area(RO_3), takuchi=False) == 361
assert f'{area(OTSU):.3f}' == '490.875' and chiseki(area(OTSU), takuchi=False) == 490
assert f'{area(KOU):.2f}' == '5145.30'
BRG_T2 = math.degrees(cmath.phase(T2 - T1))                  # T1→T2の方向角 111.16°
BRG_A = BRG_T2 + 136 + 26 / 60 + 37 / 3600                  # T1→Aの方向角 247.60°
assert to_dms(math.radians(BRG_T2)) == '111°09′40.54″'
assert to_dms(math.radians(BRG_A) - 2 * math.pi) == '−112°23′42.46″'
print('数値の照合: すべて一致')


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


def foot(p, a, b):
    """点pから直線abへ下ろした垂線の足。"""
    u = (b - a) / abs(b - a)
    return a + u * ((p - a) * u.conjugate()).real


ALL_PROBLEMS = []

# =====================================================================
# 図1：全体像（北を上にして座標どおりに描き直した調査素図）
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像（平成27年8月10日の測量時点）',
                        '甲土地（100番1）の東側部分F・E・H・Gは、7月20日に悪水はいせつ用の水路になった（新設した水路）。\n'
                        '乙土地L・K・H・I・N・Mは、国有の水路を埋め立てた土地（8月5日竣工認可の告示）。F・G、D・J、L・Mの幅はどれも7.00m。')
z = Zu(ax, fontsize=14)
fit(ax, [A, B, C, J, M, N, T1, T2, P(430, 545)], margin=0.06, pad_aspect=True)
z.poly(I_1, fill=GREEN)
z.poly(RO_3, fill=BLUE, alpha=0.35)
z.poly(OTSU, fill=ORANGE, alpha=0.30)
z.poly(N1002, color=GRAY, lw=1.4)
z.poly(SUIRO, color=GRAY, lw=1.4, fill=BLUE, alpha=0.12)
z.line(P(507, 488), P(507, 545), color=GRAY, lw=1.2, ls='--')
z.north_arrow()
z.free_text(centroid(I_1), '甲土地（100番1）のうち\n宅地として残る部分\n製菓工場', fs=16)
z.callout(centroid(RO_3) + P(12, 0), '甲土地の東側部分\n（F・E・H・G）\n新設した水路', dirs=(150, 165, 135), color=BLUE,
          dists=(150, 175, 200))
z.callout(centroid(OTSU) + P(4, 0), '乙土地\n（埋め立てた水路）', dirs=(-20, -40, 0), color=ORANGE, dists=(90, 110, 130))
z.free_text(centroid(N1002), '100番2\n従業員用\n駐車場', fs=13, color=GRAY)
z.free_text(P(452, 520), '101番\n月極駐車場', fs=14, color=GRAY, offsets=((0, 0), (20, -20), (30, -40)))
z.callout(centroid(SUIRO), '水路（無番地）', dirs=(-150, -170, -130), color=GRAY, dists=(90, 120, 150))
z.free_text(P(426.5, 465), '道路', fs=15, color=GRAY, offsets=((0, 0), (0, -4)))
z.free_text(P(503.5, 515), '既存水路', fs=15, color=GRAY, offsets=((0, 0), (20, 0), (40, 0)))
for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (H, 'H'), (I, 'I'), (J, 'J'),
             (L, 'L'), (M, 'M')]:
    z.point(p, 'stone')
for p, n in [(K, 'K'), (N, 'N')]:
    z.point(p, 'concrete')
for p, n, ref in [(A, 'A', I_1), (B, 'B', I_1), (C, 'C', I_1), (D, 'D', SUIRO), (J, 'J', SUIRO), (E, 'E', SUIRO),
                  (F, 'F', RO_3), (G, 'G', RO_3), (H, 'H', RO_3), (I, 'I', OTSU), (L, 'L', OTSU), (M, 'M', OTSU),
                  (K, 'K', OTSU), (N, 'N', OTSU)]:
    z.point_label(p, n, away=centroid(ref))
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=centroid(KOU))
ALL_PROBLEMS += save(fig, [z], 'H27_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：問1 A点（T1から放射）
# =====================================================================
fig, (ax,) = new_figure('図2　問1　A点の求め方（T1に据えてT2を後視する放射）',
                        'T1→T2の方向角 111°09′40.54″ に、右回りの観測角 136°26′37″ を足す（T1→Aの方向角 247°36′17.54″）。T1から18.82m 進む。\n'
                        '器械点と後視点を入れ替えてT2から測ると、甲土地から約74m東の（519.74, 539.35）に出てしまう。\n'
                        '真数表の検算：247°36′17.54″ − 180° ＝ 67°36′17.54″（表の67°36′17″の行）、ΔX ＝ −18.82 × 0.3809、ΔY ＝ −18.82 × 0.9245。')
z = Zu(ax, fontsize=14)
fit(ax, [T1, T2, A, Aw, T1 + 6, P(505, 450), P(505, 545)], margin=0.06, pad_aspect=True)
z.line(A, F, color=GRAY, lw=1.1)
z.line(A, A + (B - A) * 0.25, color=GRAY, lw=1.1)
z.line(T1, T1 + 6, color=GRAY, lw=1.2, ls='--')
z.free_text(T1 + 6, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(T1, T2, color=BLUE, lw=2.0)
z.line(T1, A, color=RED, lw=2.6)
z.line(T2, Aw, color=GRAY, lw=1.4, ls=':')
z.north_arrow()
z.angle_arc(T1, 3.2, 0, BRG_T2, color=BLUE)
z.angle_arc(T1, 5.0, BRG_T2, BRG_A, color=RED)
for p in (T1, T2):
    z.point(p, 'kijun')
z.point(A, 'dot', color=RED, size=9)
z.point(Aw, 'dot', color=GRAY)
z.point(F, 'stone')
z.point_label(F, 'F', away=F + P(3, -3))
z.free_text(A + (F - A) * 0.55, '甲土地', color=GRAY, fs=15, offsets=((-40, -40), (-50, -60), (-30, -70)))
z.edge_label(T1, T2, '後視（T2の方向）', T1 + P(8, 0), color=BLUE, fs=14, ts=(0.6, 0.7, 0.5), dists=(16, 22))
z.edge_label(T1, A, '18.82', T1 + P(-8, 8), color=RED, fs=17, ts=(0.6, 0.7, 0.5), dists=(14, 20, 26))
z.callout(T1 + P(1.2, 3.0), '方向角 111°09′40.54″\n（北から右回りにT2の方向）', dirs=(40, 20, 60), color=BLUE,
          dists=(90, 120, 150))
z.callout(T1 + P(-4.6, 1.9), '観測角 136°26′37″\n（T2の方向から右回り）', dirs=(-40, -20, -60), color=RED,
          dists=(90, 120, 150))
z.callout(A, 'A（520.40, 465.80）', dirs=(-150, -170, -130, 180), color=RED)
z.callout(Aw, '器械点と後視点を入れ替えた誤り\n（519.74, 539.35）', dirs=(-90, -110, -70), color=GRAY)
z.callout(T1, 'T1（527.57, 483.20）', dirs=(170, 150, 190), color=BLACK)
z.callout(T2, 'T2（512.57, 521.95）', dirs=(-100, -120, -80), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'H27_dai21mon_zu02_A_housha.png')

# =====================================================================
# 図3：問1 K点（N・Iに平行で7.00m離れた岸と、Y＝530の岸の交点）
# =====================================================================
fig, (ax,) = new_figure('図3　問1　K点の求め方（幅7.00mの平行な岸の交点）',
                        'EはN・Iの線からちょうど7.00m（倍面積のiの係数 323.75 ÷ NI 46.25）。北西の岸はEを通ってN・Iに平行。\n'
                        'K ＝ E ＋ (N − I) × (530 − 493) ÷ (537 − 500) ＝ E ＋ (N − I)。Lを通る岸（Y＝530）との交点。\n'
                        'Nの真西（470.00, 530.00）にとると、N・Iの線まで4.20mしかなく、水路が細くなる。')
z = Zu(ax, fontsize=14)
fit(ax, [E, I, L, M, N, P(505, 540), P(440, 490)], margin=0.06, pad_aspect=True)
z.poly(OTSU, color=BLACK, lw=0, fill=ORANGE, alpha=0.22, check=False)
z.line(M, N, color=BLACK, lw=2.2)
z.line(N, I, color=BLACK, lw=2.2)
z.line(L, K, color=RED, lw=2.6)
z.line(E, K, color=RED, lw=2.6)
z.line(L, M, color=GRAY, lw=1.2, ls='--')
z.line(E, Kw, color=GRAY, lw=1.3, ls=':')
fN = foot(N, E, K)
z.line(N, fN, color=BLUE, lw=1.6, ls='--')
z.right_angle(fN, K, N, size=1.2, color=BLUE)
fE = foot(E, N, I)
z.line(E, fE, color=BLUE, lw=1.6, ls='--')
z.right_angle(fE, I, E, size=1.2, color=BLUE)
fKw = foot(Kw, N, I)
z.line(Kw, fKw, color=GRAY, lw=1.3, ls='--')
z.parallel_chevron(I, N, size=1.4)
z.parallel_chevron(E, K, size=1.4)
z.north_arrow()
for p in (E, I, L, M):
    z.point(p, 'stone')
z.point(N, 'concrete')
z.point(K, 'dot', color=RED, size=9)
z.point(Kw, 'dot', color=GRAY)
for p, n in [(E, 'E'), (I, 'I'), (L, 'L'), (M, 'M'), (N, 'N')]:
    z.point_label(p, n, away=centroid(OTSU))
z.edge_label(N, fN, '7.00', N + P(0, 5), color=BLUE, fs=15, dists=(12, 18))
z.edge_label(E, fE, '7.00', E + P(0, -5), color=BLUE, fs=15, dists=(12, 18))
z.edge_label(L, M, '7.00', L + P(-5, 0), color=GRAY, fs=15, dists=(12, 18))
z.edge_label(Kw, fKw, '4.20', Kw + P(-3, 3), color=GRAY, fs=14, dists=(12, 18, 24))
z.callout(K, 'K（473.50, 530.00）', dirs=(150, 170, 130), color=RED)
z.callout(Kw, 'Nの真西にとった誤り\n（470.00, 530.00）', dirs=(-150, -130, -170), color=GRAY, dists=(95, 120, 150))
z.callout(E + (K - E) * 0.5, '北西の岸（Eを通ってN・Iに平行）', dirs=(150, 130, 170), color=RED, dists=(60, 80, 100))
z.callout(L + (K - L) * 0.5, 'Lを通る岸（Y＝530）', dirs=(170, 150, 190), color=RED, dists=(60, 80, 100))
ALL_PROBLEMS += save(fig, [z], 'H27_dai21mon_zu03_K_kousa.png')

# =====================================================================
# 図4：問1 H点（直線EKと直線IG〈Y＝500〉の交点）
# =====================================================================
fig, (ax,) = new_figure('図4　問1　H点の求め方（直線E→KとI・Gを結ぶ直線の交点）',
                        'I・GはY＝500の南北の線なので比例で出る：H ＝ E ＋ (K − E) × (500 − 493) ÷ (530 − 493)。\n'
                        '7.00mは岸に直角に測った幅。南北の線に沿って横切ると 7.00 ÷ sin 53°07′48″ ＝ 8.75（I→H）。\n'
                        'Iから真北へ7.00mの（449.25, 500.00）にとると、N・Iの線まで5.60mしかない。')
z = Zu(ax, fontsize=14)
fit(ax, [E, I, H, K + (E - K) * 0.55, P(457, 507), P(439, 493)], margin=0.08, pad_aspect=True)
KK = E + (K - E) * 0.42
NN = I + (N - I) * 0.30
z.poly([H, KK, NN, I], color=BLACK, lw=0, fill=ORANGE, alpha=0.22, check=False)
z.line(E, KK, color=RED, lw=2.6)
z.line(I, NN, color=BLACK, lw=2.2)
z.line(I + P(-3, 0), H + P(6, 0), color=GRAY, lw=1.4, ls='--')
fI = foot(I, E, K)
z.line(I, fI, color=BLUE, lw=1.6, ls='--')
z.right_angle(fI, KK, I, size=0.5, color=BLUE)
z.north_arrow()
z.point(E, 'stone')
z.point(I, 'stone')
z.point(H, 'dot', color=RED, size=9)
z.point(Hw, 'dot', color=GRAY)
z.point_label(E, 'E', away=E + P(2, 3))
z.point_label(I, 'I', away=I + P(3, 3))
z.edge_label(I, fI, '幅 7.00', I + P(3, -3), color=BLUE, fs=15, dists=(12, 18, 24))
z.edge_label(I, H, '8.75', I + P(0, 5), color=RED, fs=16, dists=(14, 20), ts=(0.5, 0.35, 0.65))
z.callout(H, 'H（451.00, 500.00）', dirs=(-20, -40, 0), color=RED)
z.callout(Hw, 'Iから真北へ7.00mの誤り\n（449.25, 500.00）', dirs=(170, 150, 190), color=GRAY, dists=(70, 95, 120))
z.callout(I + P(-2.2, 0), 'I・Gを結ぶ直線（Y＝500）', dirs=(-20, -35, 0), color=GRAY, dists=(80, 100, 120))
z.callout(E + (KK - E) * 0.8, '直線E→K', dirs=(120, 100, 140), color=RED, dists=(50, 70, 90))
ALL_PROBLEMS += save(fig, [z], 'H27_dai21mon_zu04_H_kousa.png')

# =====================================================================
# 図5：問2 登記の対象となる土地かどうか（整理図。固定配置）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図5　問2　水路になっても、登記の対象となる土地', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
BOXES = [
    (70, '甲土地の東側部分（F・E・H・G）', BLUE,
     ['会社が自分の土地を掘って、悪水はいせつ用の水路にした（平成27年7月20日）',
      '所有者は山川製菓のまま → 私権の客体（権利の目的）であることは変わらない',
      '→ 依然として登記の対象。地目が用悪水路に変わっただけ（不動産登記規則第99条）'], [2]),
    (40, '乙土地（L・K・H・I・N・M）', ORANGE,
     ['国有の公共用の水路（公有水面）で無番地 → 公有水面埋立法の免許を受けて埋め立て',
      '竣工認可の告示（平成27年8月5日）で会社が所有権を取得',
      '→ 新たに生じた土地として土地の表題登記（不動産登記法第36条）'], [2]),
    (10, '比べておく：土地が海に沈んで公有水面になった', GRAY,
     ['土地そのものがなくなった（私権の客体でなくなった）',
      '→ 土地の滅失の登記（不動産登記法第42条）',
      '水路にしただけの甲土地の東側部分は、これに当たらない'], [1]),
]
for y, head, col, lines, red in BOXES:
    ax.add_patch(FancyBboxPatch((3, y), 94, 24, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=col, lw=2.2))
    ax.text(5, y + 20.5, head, fontsize=20, weight='bold', va='center', color=col)
    for i, s in enumerate(lines):
        ax.text(8, y + 14 - i * 5.8, s, fontsize=17, va='center', color=RED if i in red else BLACK)
fig.text(0.5, 0.04, '結論：依然として登記の対象となる土地である。　理由：私権の客体となる土地のままで、水路となったのは地目（用悪水路）の変更にすぎないから。',
         ha='center', va='center', fontsize=16, color=RED)
path = os.path.join(OUT, 'H27_dai21mon_zu05_touki_taishou.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図5: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図6：問3 分筆後の区画と地番
# =====================================================================
fig, (ax,) = new_figure('図6　問3　分筆後の区画と地番（100番1 → （イ）100番1 ＋ （ロ）100番3）',
                        '（イ）100番1（宅地）：座標法で4783.925 → 小数第2位未満を切り捨てて4783.92㎡（四捨五入の4783.93ではない）。\n'
                        '（ロ）100番3（用悪水路）：台形 (54.25 ＋ 49.00) × 7 ÷ 2 ＝ 361.375 → 1㎡未満を切り捨てて361㎡。\n'
                        '切り捨て前の合計5145.30と登記記録の5144.50の差0.80は公差の範囲内なので、地積更正は不要。')
z = Zu(ax, fontsize=14)
fit(ax, [A, B, C, D, J, G, L, K], margin=0.06, pad_aspect=True)
z.poly(I_1, fill=GREEN)
z.poly(RO_3, fill=PURPLE, alpha=0.35)
z.poly(OTSU, color=GRAY, lw=1.2)
z.poly(N1002, color=GRAY, lw=1.2)
z.poly(SUIRO, color=GRAY, lw=1.2)
z.north_arrow()
z.free_text(centroid(I_1), '（イ）100番1\n宅地\n4783.92㎡', fs=20)
z.callout(centroid(RO_3) + P(10, 0), '（ロ）100番3\n用悪水路\n361㎡', dirs=(10, -10, 30), color=PURPLE,
          dists=(110, 140, 170), fs=16)
for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (H, 'H')]:
    z.point(p, 'stone')
    z.point_label(p, n, away=centroid(I_1) if n in 'ABCD' else centroid(RO_3))
z.edge_label(F, E, '54.25', centroid(RO_3), fs=14, dists=(14, 20), ts=(0.3, 0.2, 0.4))
z.edge_label(G, H, '49.00', centroid(RO_3), fs=14, dists=(14, 20), ts=(0.3, 0.2, 0.4))
z.free_text(centroid(N1002), '100番2', fs=14, color=GRAY)
z.callout(centroid(OTSU), '乙土地', dirs=(-40, -60, -20), color=GRAY, dists=(60, 80))
z.callout(centroid(SUIRO), '水路', dirs=(-30, -10, -50), color=GRAY, dists=(70, 90))
ALL_PROBLEMS += save(fig, [z], 'H27_dai21mon_zu06_bunpitsu_chiban.png')

# =====================================================================
# 図7：問4 土地所在図兼地積測量図（乙土地）の完成見本
# =====================================================================
fig, (ax,) = new_figure('図7　問4　土地所在図兼地積測量図（乙土地）の完成見本',
                        '縮尺1/500で答案用紙に描くと 1m ＝ 2mm（T1からIまで南北約171mm、T1からM・Nまで東西約108mm）。辺長は割り切れて四捨五入の境目はない。\n'
                        '座標値・地積・求積方法・測量年月日は書かない（注6）。T1・T2は位置と点名だけ（注7）。地番と作成者・申請人は「（略）」が印刷済み。\n'
                        '乙土地の表題登記を先に申請するので、Hの北西に接するのは分筆前の100－1（100－3ではない）。')
z = Zu(ax, fontsize=15)
fit(ax, [T1, T2, I, M, N, P(440, 470)], margin=0.05, pad_aspect=True)
z.poly(OTSU, lw=2.0)
z.north_arrow()
co = centroid(OTSU)
REF = {'LK': L + P(-10, 4), 'NM': N + P(10, -4), 'ML': P(490, 533.5)}   # 縦の部分は、区画の内側の点を個別に指定する
for n, (p, q, s) in SIDES.items():
    z.edge_label(p, q, s, REF.get(n, co), fs=15)
z.free_text(P(488, 533.5), '申請地', fs=14)
for p, n in [(L, 'L'), (H, 'H'), (I, 'I'), (M, 'M')]:
    z.point(p, 'stone')
    z.point_label(p, n, away=co)
for p, n in [(K, 'K'), (N, 'N')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=co)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.free_text(P(480, 518), '100－2', fs=15, offsets=((0, 0), (0, 20), (-20, 0)))
z.free_text(H, '100－1', fs=15, offsets=((-45, 30), (-55, 20), (-55, 40)))
z.edge_label(I, N, '101', co, fs=15, dists=(42, 52), rotate=False)
z.edge_label(M, L, '水路', co, fs=15, dists=(30, 40), rotate=False)
z.edge_label(H, I, '水路', co, fs=15, dists=(46, 56), rotate=False)
z.free_text(P(452, 475), '（単位：ｍ）\n□ 石杭：L・H・I・M\n◎ コンクリート杭：K・N\n△ 基準点：T1・T2\n土地の所在　B市C町一丁目', fs=14,
            ha='left', va='bottom', offsets=((0, 0), (0, 30), (0, 60)))
ALL_PROBLEMS += save(fig, [z], 'H27_dai21mon_zu07_chiseki_sokuryouzu.png')

print('重なりの合計:', len(ALL_PROBLEMS))
