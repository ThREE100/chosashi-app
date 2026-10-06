"""令和6年度 第21問（土地）会話形式note記事の解説図12枚を、座標値から作図する。

`../prompt_R6_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../R7/Q21/zu/draw_R7_dai21mon_kaisetsuzu.py`。

実行: python3 note-articles-Kijyutsu/R6/Q21/zu/draw_R6_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, chiseki, intersect  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
T1, T2 = P(16.63, 61.67), P(26.91, 64.19)
A, C, E, F, G = P(25.09, 48.35), P(27.49, 60.92), P(35.40, 60.81), P(35.40, 50.15), P(33.82, 48.35)
H, I, J, K = P(21.83, 54.17), P(21.83, 60.90), P(19.83, 60.93), P(19.83, 48.35)
B = r2(radial(T2, T1, 10.03, dms(78, 58, 8)))
D = r2(radial(T2, T1, 4.60, dms(118, 24, 27)))
PP = r2(intersect(B, C, D, J)[0])          # P点（ブロック塀の線BCと道路境界DJの交点）

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('B', B, P(27.39, 54.17)), ('D', D, P(30.00, 60.78)), ('P', PP, P(27.49, 60.82))]:
    assert abs(got - want) < 1e-9, (n, got, want)
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'BP': (B, PP, '6.65'), 'PD': (PP, D, '2.51'), 'DB': (D, B, '7.11'), 'PI': (PP, I, '5.66'),
         'IH': (I, H, '6.73'), 'HB': (H, B, '5.56')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
for n, (p, q, want) in {'AB': (A, B, '6.26'), 'DJ': (D, J, '10.17')}.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
KOU = [A, B, D, E, F, G]            # 甲土地（2番1）の筆界
OTSU = [B, D, I, H]                 # 乙土地（3番1）の筆界（残地）
N32 = [A, K, J, I, H, B]            # 3番2
KOU_USE = [A, B, C, D, E, F, G]     # 甲土地の利用状況（ブロック塀 A→B→C）
OTSU_USE = [B, H, I, C]             # 乙土地の利用状況
I_31 = [B, PP, I, H]                # 分筆後の（イ）3番1
RO_33 = [B, D, PP]                  # 分筆後の（ロ）3番3
fl = lambda v: f'{chiseki(v):.2f}'  # noqa: E731  地積・比較用の面積（小数第2位未満切捨て）
AREAS = {'甲土地（筆界）': (KOU, '96.29'), '乙土地（筆界）': (OTSU, '45.86'), '甲土地（利用状況）': (KOU_USE, '104.76'),
         '乙土地（利用状況）': (OTSU_USE, '37.81'), '（イ）3番1': (I_31, '37.53'), '（ロ）3番3': (RO_33, '8.34'),
         '3番2': (N32, '50.79')}
for n, (pts, want) in AREAS.items():
    assert fl(area(pts)) == want, (n, fl(area(pts)), want)
assert f'{area([A, B, D]):.4f}' == '0.0064'
assert to_dms(cmath.phase(T1 - T2) + 2 * math.pi) == '193°46′25.18″'
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
BRG_T1 = math.degrees(cmath.phase(T1 - T2)) + 360          # T2→T1の方向角（北から時計回り）193.77°
BRG_B = BRG_T1 + 78 + 58 / 60 + 8 / 3600
BRG_D = BRG_T1 + 118 + 24 / 60 + 27 / 3600

# =====================================================================
# 図1：全体像（北を上にして座標どおりに描き直した調査図素図）
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像（令和6年10月の調査時点）',
                        'ブロック塀（A→B→C）と金属標Cは、測量によらず二人が合意した位置に設置したもの。\n'
                        '地図に準ずる図面では、甲土地と乙土地の境はAのあたりからDまで1本の直線（A→B→D）に描かれている。')
z = Zu(ax)
fit(ax, [A, G, F, E, D, J, K, T1, T2], margin=0.10, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.poly(N32, fill=ORANGE, alpha=0.15)
z.line(A, B, color=RED, lw=5.0)
z.line(B, C, color=RED, lw=5.0)
z.line(C, D, color=GRAY, lw=1.0, ls=':')
z.north_arrow()
cg, co, c32 = centroid(KOU), centroid(OTSU), centroid(N32)
z.free_text(cg, '甲土地\n2番1　宅地\n97.00㎡\n山田太郎', fs=16)
z.free_text(co + P(-1.2, 0.2), '乙土地\n3番1　宅地\n45.88㎡\n野原花子', fs=14)
z.free_text(P(20.9, 51.3), '3番2', fs=15)
for p, n, ref in [(A, 'A', cg), (B, 'B', cg), (D, 'D', co), (E, 'E', cg), (F, 'F', cg), (G, 'G', cg),
                  (H, 'H', c32), (I, 'I', c32), (J, 'J', c32), (K, 'K', c32)]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=ref)
z.point(C, 'metal', size=9)
z.point_label(C, 'C', away=cg)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.callout(A + (B - A) * 0.5, 'ブロック塀（A→B→C）', dirs=(-120, -140, -100), color=RED, dists=(70, 95, 120))
z.callout(B + (D - B) * 0.85, '地図に準ずる図面の境\n（A→B→Dの直線）', dirs=(25, 40, 10, -10), color=BLACK,
          dists=(90, 120, 150, 180))
z.edge_label(F, E, '2－2', cg, fs=15, dists=(22, 30), rotate=False)
z.edge_label(E, D, '1－1', cg, fs=15, dists=(26, 34), rotate=False)
z.edge_label(G, A, '5', cg, fs=15, dists=(22, 30), rotate=False)
z.edge_label(A, K, '5', c32, fs=15, dists=(22, 30), rotate=False)
z.edge_label(K, J, '道路', c32, fs=15, dists=(22, 30), rotate=False)
z.edge_label(I, J, '道路', c32, fs=15, dists=(28, 36), rotate=False, ts=(0.5, 0.3, 0.7))
z.edge_label(G, F, '道路', cg, fs=15, dists=(22, 30), rotate=False)
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：問2 B点（T2から放射）
# =====================================================================
fig, (ax,) = new_figure('図2　問2　B点の求め方（T2から放射）',
                        'T2→T1の方向角 193°46′25.18″（電卓の表示は −166°13′34.82″）に、時計回りの観測角 78°58′08″ を足し、10.03m 進む。\n'
                        '反時計回りに測ると、道路を越えた東に出てしまう。\n'
                        '検算：BH＝5.56、AB＝6.26（昭和50年の地積測量図の辺長と一致）。')
z = Zu(ax)
Bw = r2(radial(T2, T1, 10.03, -dms(78, 58, 8)))    # 反時計回りに測った誤答
fit(ax, [T1, T2, B, Bw, H, A, D, T2 + P(3.5, 0)], margin=0.08, pad_aspect=True)
z.poly([A, B, D], color=GRAY, lw=1.1, closed=False)   # 甲土地は乙土地との境だけ（北側まで描くと端が切れる）
z.poly(OTSU, color=GRAY, lw=1.1)
z.poly(N32, color=GRAY, lw=1.1)
z.line(T2, T2 + 3.5, color=GRAY, lw=1.2, ls='--')
z.free_text(T2 + 3.5, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(T2, T1, color=BLUE, lw=2.0)
z.line(T2, B, color=RED, lw=2.6)
z.line(T2, Bw, color=GRAY, lw=1.4, ls=':')
z.north_arrow()
z.angle_arc(T2, 1.6, 0, BRG_T1, color=BLUE)
z.angle_arc(T2, 2.6, BRG_T1, BRG_B, color=RED)
for p, kind in [(T1, 'kijun'), (T2, 'kijun'), (B, 'concrete'), (H, 'concrete'), (A, 'concrete')]:
    z.point(p, kind)
z.point(Bw, 'dot', color=GRAY)
for p, n in [(H, 'H'), (A, 'A')]:
    z.point_label(p, n, away=centroid(N32))
z.edge_label(T2, T1, '後視（T1の方向）', T2 + P(0, -5), color=BLUE, fs=14, ts=(0.55, 0.65, 0.45), dists=(16, 22))
z.edge_label(T2, B, '10.03', T2 + P(-5, 0), color=RED, fs=17, ts=(0.62, 0.7, 0.55, 0.8), dists=(14, 20, 26))
z.edge_label(B, H, 'BH ＝ 5.56', centroid(OTSU), color=BLACK, fs=14, outward=False, dists=(16, 22))
z.edge_label(A, B, 'AB ＝ 6.26', centroid(N32), color=BLACK, fs=14, dists=(14, 20))
z.callout(T2 + P(0.3, 1.57), '方向角 193°46′25.18″\n（北から時計回りにT1の方向）', dirs=(60, 40, 80, 20), color=BLUE,
          dists=(90, 120, 150))
z.callout(T2 + P(-2.55, -0.5), '観測角 78°58′08″\n（T1の方向から時計回り）', dirs=(-110, -130, -90, -60), color=RED,
          dists=(60, 85, 110))
z.callout(B, 'B（27.39, 54.17）', dirs=(120, 100, 140, 160), color=RED)
z.callout(Bw, '反時計回りに測った誤り\n（22.70, 73.29）', dirs=(-90, -120, -60, 180), color=GRAY)
z.callout(T2, 'T2（26.91, 64.19）', dirs=(10, -5, 25), color=BLACK, dists=(110, 140, 170))
z.callout(T1, 'T1（16.63, 61.67）', dirs=(0, -20, 20), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu02_B_housha.png')

# =====================================================================
# 図3：問2 D点（T2から放射）
# =====================================================================
fig, (ax,) = new_figure('図3　問2　D点の求め方（T2から放射）',
                        'B点と同じ器械点T2・同じ後視T1。T2→T1の方向角 193°46′25.18″ に、時計回りの観測角 118°24′27″ を足し、4.60m 進む。\n'
                        '検算：DJ＝10.17（道路境界確認図のK1K2の10.17と一致。D＝K1、J＝K2）。')
z = Zu(ax)
fit(ax, [T1, T2, D, J, B, T2 + P(3.5, 0)], margin=0.08, pad_aspect=True)
z.poly([A, B, D], color=GRAY, lw=1.1, closed=False)   # 甲土地は乙土地との境だけ（北側まで描くと端が切れる）
z.poly(OTSU, color=GRAY, lw=1.1)
z.poly(N32, color=GRAY, lw=1.1)
z.line(T2, T2 + 3.5, color=GRAY, lw=1.2, ls='--')
z.free_text(T2 + 3.5, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(T2, T1, color=BLUE, lw=2.0)
z.line(T2, D, color=RED, lw=2.6)
z.north_arrow()
z.angle_arc(T2, 1.6, 0, BRG_T1, color=BLUE)
z.angle_arc(T2, 1.1, BRG_T1, BRG_D, color=RED)
for p, kind in [(T1, 'kijun'), (T2, 'kijun'), (D, 'concrete'), (J, 'concrete'), (B, 'concrete')]:
    z.point(p, kind)
for p, n in [(J, 'J'), (B, 'B')]:
    z.point_label(p, n, away=centroid(OTSU) if n == 'B' else centroid(N32))
z.edge_label(T2, T1, '後視（T1の方向）', T2 + P(0, -5), color=BLUE, fs=14, ts=(0.55, 0.65, 0.45), dists=(16, 22))
z.edge_label(T2, D, '4.60', T2 + P(0, 5), color=RED, fs=17, ts=(0.5, 0.62, 0.4), dists=(14, 20, 26))
z.edge_label(D, J, 'DJ ＝ 10.17', centroid(OTSU), color=BLACK, fs=14, ts=(0.5, 0.62, 0.38), dists=(16, 22, 30))
z.callout(T2 + P(-1.2, 1.03), '方向角 193°46′25.18″\n（北から時計回りにT1の方向）', dirs=(-20, -40, 0, -60), color=BLUE,
          dists=(90, 120, 150, 180))
z.callout(T2 + P(-0.9, -0.6), '観測角 118°24′27″\n（T1の方向から時計回り）', dirs=(-100, -120, -80, -60), color=RED,
          dists=(90, 120, 150))
z.callout(D, 'D（30.00, 60.78）', dirs=(120, 100, 140, 80), color=RED)
z.callout(T2, 'T2（26.91, 64.19）', dirs=(10, -5, 25), color=BLACK, dists=(120, 150, 180))
z.callout(T1, 'T1（16.63, 61.67）', dirs=(0, -20, 20), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu03_D_housha.png')

# =====================================================================
# 図4：問1（ア）筆界の判断（利用状況と地図に準ずる図面の比較）
# =====================================================================
fig, (ax1, ax2) = new_figure('図4　問1（ア）　筆界はブロック塀ではなく、地図に準ずる図面の直線',
                             '左：ブロック塀（A→B→C）を境にすると、甲土地104.76㎡・乙土地37.81㎡で、登記記録の97.00㎡・45.88㎡と合わない。\n'
                             '右：地図に準ずる図面の直線（A→B→D。A・B・Dは一直線で△ABDは0.0064㎡）なら、甲土地96.29㎡・乙土地45.86㎡で合う。\n'
                             '残地の地積測量図が測っているのは3番2の周り（A・B・H・I・J・K）だけで、B→Dの長さは書かれていない。',
                             ncols=2)
zs = []
for ax, pk, po, sk, so, head, col in [
    (ax1, KOU_USE, OTSU_USE, '104.76㎡', '37.81㎡', '利用状況（ブロック塀 A→B→C）', GRAY),
    (ax2, KOU, OTSU, '96.29㎡', '45.86㎡', '地図に準ずる図面の形（A→B→D）', RED),
]:
    z = Zu(ax, fontsize=14)
    fit(ax, [A, G, F, E, D, J, K], margin=0.20, pad_aspect=True)
    z.poly(pk, fill=GREEN)
    z.poly(po, fill=BLUE)
    z.poly(N32, color=GRAY, lw=1.0)
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=18, color=col, weight='bold', pad=6)
    z.free_text(centroid(pk), f'甲土地\n{sk}', fs=16)
    z.callout(centroid(po), f'乙土地 {so}', dirs=(-60, -40, -80), color=BLACK, dists=(80, 100, 120))
    for p, n in [(A, 'A'), (B, 'B'), (D, 'D'), (H, 'H'), (I, 'I')]:
        z.point(p, 'concrete')
        z.point_label(p, n, away=centroid(pk) if n in 'AB' else centroid(N32))
    if pk is KOU_USE:
        z.point(C, 'metal', size=9)
        z.point_label(C, 'C', away=centroid(pk))
    zs.append(z)
zs[0].free_text(centroid(KOU_USE), '→ 登記記録の\n97.00㎡・45.88㎡と合わない', color=GRAY, fs=14,
                offsets=((0, 60), (0, 75), (0, -70), (0, -85), (-20, 60), (20, 60)))
zs[1].free_text(centroid(KOU), '→ 登記記録の\n97.00㎡・45.88㎡と合う', color=RED, fs=14,
                offsets=((0, 60), (0, 75), (0, -70), (0, -85), (-20, 60), (20, 60)))
ALL_PROBLEMS += save(fig, zs, 'R6_dai21mon_zu04_hikkai_handan.png')

# =====================================================================
# 図5：問2 P点（ブロック塀の線BCと道路境界DJの交点）
# =====================================================================
fig, (ax1, ax2) = new_figure('図5　問2　P点の求め方（ブロック塀の線と道路境界の交点）',
                             'P ＝ B ＋ (C − B) × t、t ＝ 67.6152 ÷ 68.6625（Conjgの積のiの係数の比）。\n'
                             'C点の金属標は道路境界D→Jから道路側に0.10mはみ出していた。Cのまま分けると2筆の合計が46.28㎡になり、元の45.88㎡より増える。',
                             ncols=2, width_ratios=[1.3, 1])
za = Zu(ax1)
fit(ax1, [B, D, I, H, J, C, C + P(0, 3.5)], margin=0.12, pad_aspect=True)
za.poly(OTSU, fill=BLUE)
za.line(I, J, color=BLACK, lw=2.0)
za.line(B, C, color=RED, lw=4.0)
za.north_arrow()
for p, n in [(B, 'B'), (D, 'D'), (I, 'I'), (H, 'H'), (J, 'J')]:
    za.point(p, 'concrete')
    za.point_label(p, n, away=centroid(OTSU))
za.point(PP, 'dot', color=RED, size=9)
za.callout(PP, 'P（27.49, 60.82）', dirs=(-30, -10, -50), color=RED)
za.callout(B + (C - B) * 0.45, 'ブロック塀の線（B→C）', dirs=(-110, -130, -90), color=RED, dists=(60, 80, 100))
za.edge_label(D, J, '道路境界（D→J）', centroid(OTSU), fs=14, ts=(0.75, 0.85, 0.65), dists=(16, 24))

zb = Zu(ax2)
lo, hi = PP + P(-0.30, -0.35), PP + P(0.30, 0.35)
ax2.set_xlim(lo.imag, hi.imag)
ax2.set_ylim(lo.real, hi.real)
t_lo, t_hi = (lo.real - D.real) / (J.real - D.real), (hi.real - D.real) / (J.real - D.real)
zb.line(D + (J - D) * t_hi, D + (J - D) * t_lo, color=BLACK, lw=2.0)
zb.line(B + (C - B) * 0.955, C, color=RED, lw=4.0)
zb.north_arrow()
zb.point(C, 'metal', size=11)
zb.point(PP, 'dot', color=RED, size=11)
zb.callout(C, 'C（27.49, 60.92）\n移設前の金属標', dirs=(45, 30, 60, 20), color=GRAY, dists=(60, 80, 100))
zb.callout(PP, 'P（27.49, 60.82）', dirs=(-120, -140, -100), color=RED)
zb.edge_label(PP, C, '0.10', PP + P(-0.2, 0), color=RED, fs=17, dists=(14, 20), rotate=False)
zb.free_text(PP + P(-0.22, 0.22), '道路', fs=18, color=GRAY, offsets=((0, 0), (0, 10), (10, 0)))
zb.free_text(PP + P(-0.22, -0.2), '乙土地', fs=18, color=BLUE, offsets=((0, 0), (0, 10), (-10, 0)))
ax2.set_title('Pのまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'R6_dai21mon_zu05_P_kousa.png')

# =====================================================================
# 図6：問1（イ）〜（エ）必要な登記の流れ
# =====================================================================
fig, (ax,) = new_figure('図6　問1（イ）〜（エ）　野原花子が乙土地について分筆の登記を申請する',
                        '筆界（A→B→D）と利用状況（A→B→P）のずれは三角形B・D・P。筆界の上では乙土地なのに、山田太郎が使っている。\n'
                        '①野原花子が乙土地を分筆（今回の申請。イ＝9、ウ＝5、エ＝6）→ ②三角形の土地を山田太郎へ所有権移転 → ③2番1と合筆。\n'
                        '地図に準ずる図面は筆界どおりなので地図訂正は不要。地積も公差の範囲内なので地積更正も不要（選択肢7は誤り）。')
z = Zu(ax)
fit(ax, [A, G, F, E, D, I, H], margin=0.14, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.poly(RO_33, color=RED, lw=0, fill=RED, alpha=0.35, check=False)
z.line(B, PP, color=RED, lw=3.0)
z.north_arrow()
z.free_text(centroid(KOU), '甲土地（2番1）\n山田太郎', fs=17)
z.free_text(centroid(I_31), '乙土地（3番1）\n野原花子', fs=15)
z.callout(centroid(RO_33), '三角形B・D・P\n筆界の上では乙土地なのに\n山田太郎が使っている', dirs=(60, 40, 80), color=RED,
          dists=(90, 120, 150))
z.callout(B + (PP - B) * 0.15, '利用状況の境（ブロック塀の線 B→P）', dirs=(-120, -110, -130), color=RED,
          dists=(200, 230, 260))
for p, n in [(A, 'A'), (B, 'B'), (D, 'D'), (H, 'H'), (I, 'I'), (E, 'E'), (F, 'F'), (G, 'G')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=centroid(KOU) if n in 'EFGA' else centroid(OTSU))
z.point(PP, 'metal', size=9)
z.point_label(PP, 'P', away=centroid(OTSU))
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu06_hitsuyou_touki.png')

# =====================================================================
# 図7：問3 分筆後の区画と地番
# =====================================================================
fig, (ax,) = new_figure('図7　問3　分筆後の区画と地番（3番1 → （イ）3番1 ＋ （ロ）3番3）',
                        '問題文の注8により、面積の小さい三角形B・D・P（8.34㎡）が（ロ）3番3、残る四角形B・P・I・H（37.53㎡）が（イ）3番1のまま。\n'
                        '切り捨て前の合計 8.34775 ＋ 37.5329 ＝ 45.88065 で登記記録の45.88㎡と一致。申請書の1行目の地積は登記記録の45.88（計算値の45.86ではない）。')
z = Zu(ax)
fit(ax, OTSU + [H + P(0, -2.5), D + P(1.6, 0)], margin=0.16, pad_aspect=True)
z.poly(I_31, fill=BLUE)
z.poly(RO_33, fill=PURPLE, alpha=0.30)
z.north_arrow()
z.free_text(centroid(I_31), '（イ）3番1\n37.53㎡', fs=18)
z.callout(centroid(RO_33), '（ロ）3番3　8.34㎡', dirs=(100, 80, 120), color=PURPLE, dists=(70, 90, 110))
for p, n in [(B, 'B'), (D, 'D'), (H, 'H'), (I, 'I')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=centroid(OTSU))
z.point(PP, 'metal', size=9)
z.point_label(PP, 'P', away=centroid(OTSU))
z.edge_label(B, D, '2番1（甲土地）', centroid(OTSU), fs=15, color=GRAY, dists=(34, 44), rotate=False,
             ts=(0.3, 0.2, 0.4))
z.edge_label(H, B, '3番2', centroid(OTSU), fs=15, color=GRAY, dists=(30, 40), rotate=False)
z.edge_label(I, H, '3番2', centroid(OTSU), fs=15, color=GRAY, dists=(26, 36), rotate=False)
z.edge_label(PP, I, '道路', centroid(OTSU), fs=15, color=GRAY, dists=(30, 40), rotate=False)
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu07_bunpitsu_chiban.png')

# =====================================================================
# 図8：問4 地積測量図（3番1・3番3）の完成見本
# =====================================================================
fig, (ax,) = new_figure('図8　問4　地積測量図（3番1・3番3）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm（図は横約27mm・縦約33mmと小さい）。辺長は小数第3位を四捨五入（DB は 7.1066 なので 7.11）。\n'
                        '座標値・地積・求積方法・測量年月日は書かない（問題文の注5）。基準点T1・T2は位置と点名だけ（問題文の注6）。C点は描かない（金属標はPに移設）。\n'
                        'T1・T2まで入れても、南北13.37m（約53mm）・東西10.02m（約40mm）で答案用紙の枠に収まる。')
z = Zu(ax)
fit(ax, OTSU + [T1, T2], margin=0.12, pad_aspect=True)
z.poly([B, D, PP, I, H], lw=2.0)
z.line(B, PP, lw=2.0)
z.north_arrow()
co = centroid(OTSU)
for n, (p, q, s) in SIDES.items():
    if n == 'BP':
        z.edge_label(p, q, s, centroid(I_31), fs=16, outward=False)
    else:
        z.edge_label(p, q, s, co, fs=16)
z.free_text(centroid(I_31), '（イ）\n3－1', fs=17)
z.free_text(centroid(RO_33), '（ロ）3－3', fs=13, offsets=((0, 0), (-10, 3), (10, 3)))
for p, n in [(B, 'B'), (D, 'D'), (H, 'H'), (I, 'I')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=co)
z.point(PP, 'metal', size=9)
z.point_label(PP, 'P', away=co)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.edge_label(D, B, '２－１', co, fs=16, dists=(40, 50), rotate=False, ts=(0.3, 0.2, 0.4))
z.free_text(D, '１－１', fs=16, offsets=((40, 28), (50, 20), (55, 35)))
z.edge_label(H, B, '３－２', co, fs=16, dists=(40, 50), rotate=False)
z.edge_label(I, H, '３－２', co, fs=16, dists=(36, 46), rotate=False)
z.edge_label(PP, I, '道路', co, fs=16, dists=(44, 54), rotate=False)
z.free_text(P(18.2, 51.0), '（単位：ｍ）\n◎ コンクリート杭：B・D・H・I\n● 金属標：P\n△ 基準点：T1・T2', fs=13,
            ha='left', va='bottom', offsets=((0, 0), (0, 30), (0, 60)))
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu08_chiseki_sokuryouzu.png')

# =====================================================================
# 図9：問5 地図に準ずる図面の訂正の申出（整理図。固定配置）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図9　問5　地図に準ずる図面の訂正の申出（不動産登記規則第16条）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
BOXES = [
    (76, '①　申出ができる者（第1項）',
     ['土地の表題部所有者若しくは所有権の登記名義人', '又はこれらの相続人その他の一般承継人'], [0, 1]),
    (53, '②（ア）　どんな誤りか（第1項）',
     ['地図：土地の区画又は地番', '地図に準ずる図面：土地の位置、形状又は 地番 （ア）'], [1]),
    (30, '②（イ）　申出権のない者からの申出',
     ['訂正の申出の趣旨なら却下（第13項第2号）', 'そうでなければ、登記官の 職権 （イ）の発動を促す申出として扱える（職権で訂正できる：第15項）'], [1]),
    (7, '②（ウ）　申出と併せて提供する情報（第5項）',
     ['第1号：誤りがあることを証する情報（どの申出にも）',
      '第2号：位置又は形状に誤りがあるとき → 土地所在図又は地積測量図 （ウ）'], [1]),
]
for y, head, lines, red in BOXES:
    ax.add_patch(FancyBboxPatch((3, y), 94, 18, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=BLACK, lw=1.4))
    ax.text(5, y + 15, head, fontsize=19, weight='bold', va='center')
    for i, s in enumerate(lines):
        ax.text(8, y + 9.5 - i * 5.5, s, fontsize=17, va='center', color=RED if i in red else BLACK)
fig.text(0.5, 0.035, '地図の「区画」と、地図に準ずる図面の「位置、形状」を混ぜない。第1号の情報は常に必要で、（ウ）で問われているのは位置・形状の誤りのときの第2号。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R6_dai21mon_zu09_chizu_teisei.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図9: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図10：問題文の注の仕分け（毎年同じ注と今年だけの注、調査図素図の注。整理図。固定配置）
# 2026-10-02追加（予備校の解説と見比べて記事に足した読み方の図）
# =====================================================================
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図10　問題文の注の仕分け（毎年同じ注と、今年だけの注）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.14, 0.94, 0.76])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
COLS = [
    (1, '毎年ほぼ同じ決まり文句', GRAY,
     ['注1　行為は全て適法、書類も適法', '注2　書面申請', '注3　座標値は小数第3位を四捨五入',
      '注4　地積測量図は250分の1、\n　　　筆界点間の距離は小数第3位を四捨五入', '注9　答案用紙の字画・訂正の方法']),
    (34, '今年だけ①　地積測量図に書かないもの', BLUE,
     ['注5　座標値、平面直角座標系の番号又は記号、\n　　　地積及びその求積方法、測量年月日', '注6　A市基準点は位置と点名だけ\n　　　（座標値は書かない）']),
    (67, '今年だけ②　分筆後の地番', RED,
     ['注7　甲土地を分筆する場合は\n　　　面積の小さい土地を2番3', '注8　乙土地を分筆する場合は\n　　　面積の小さい土地を3番3',
      '→ 両方あるのは、どちらを分筆するかを\n　 迷わせるため（分筆するのは乙土地）']),
]
for x0, head, col, items in COLS:
    ax.add_patch(FancyBboxPatch((x0, 22), 31, 70, boxstyle='round,pad=0.5', fc='white', ec=col, lw=2.2))
    ax.text(x0 + 15.5, 88, head, ha='center', va='center', fontsize=16, color=col, weight='bold')
    for k, it in enumerate(items):
        ax.text(x0 + 1.5, 79 - k * 12.5, it, ha='left', va='top', fontsize=14, linespacing=1.4,
                color=RED if it.startswith('→') else BLACK)
ax.add_patch(FancyBboxPatch((1, 2), 97, 12, boxstyle='round,pad=0.5', fc='white', ec=PURPLE, lw=2.2))
ax.text(49.5, 8, '調査図素図の（注）：D点からJ点は直線であり、I点はその直線上にある（P点を求める直線D→Jの根拠）',
        ha='center', va='center', fontsize=15, color=PURPLE, weight='bold')
fig.text(0.5, 0.06, '問題文の注と調査図素図の（注）は別物なので、記事では「問題文の注7」「調査図素図の注」と言い分ける。', ha='center',
         va='center', fontsize=16)
path = os.path.join(OUT, 'R6_dai21mon_zu10_chuu_shiwake.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図10: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図11：問3　四角形B・P・I・Hの面積を対角線で出す別解
# 2026-10-02追加（予備校の解説と見比べて記事に足した別解の図）
# =====================================================================
dd = (B - I).conjugate() * (PP - H)
assert f'{dd.real:.4f}' == '-13.2849' and f'{dd.imag:.4f}' == '75.0658'
assert abs(dd.imag / 2 - area(I_31)) < 1e-9
fig, (ax,) = new_figure('図11　問3　四角形B・P・I・Hの面積を対角線で出す（別解）',
                        '倍面積 ＝ Conjg(B − I) × (P − H) のiの係数 75.0658（4点を順に回る式と同じ）。75.0658 ÷ 2 ＝ 37.5329 → （イ）37.53㎡\n'
                        '分筆後の地積の合計 37.53 ＋ 8.34 ＝ 45.87㎡。登記記録の45.88㎡との差 0.01㎡は、参考の甲2の公差（約0.51㎡）の範囲内。')
z = Zu(ax)
XD = intersect(B, I, PP, H)[0]                         # 対角線の交点
fit(ax, [B, D, PP, I, H, P(24.6, 50.2)], margin=0.12, pad_aspect=True)
z.poly(I_31, fill=BLUE)
z.poly(RO_33, fill=ORANGE)
z.line(B, I, color=RED, lw=2.2, ls='--')
z.line(PP, H, color=RED, lw=2.2, ls='--')
z.north_arrow()
for p_, n_ in [(B, 'B'), (D, 'D'), (PP, 'P'), (I, 'I'), (H, 'H')]:
    z.point(p_, 'dot')
    z.point_label(p_, n_, away=centroid([B, D, I, H]))
z.free_text(centroid([B, H, XD]), '（イ）3番1\n37.5329\n→ 37.53㎡', fs=14, offsets=((0, 0), (-10, 0), (-10, 10)))
z.callout(centroid(RO_33), '（ロ）3番3　8.34775 → 8.34㎡', dirs=(60, 40, 80, 20), color=ORANGE, dists=(70, 95, 120))
z.callout((B + I) / 2 + (I - B) * 0.18, '対角線 B − I', dirs=(-150, -130, -170), color=RED, dists=(70, 95))
z.callout((PP + H) / 2 + (PP - H) * 0.22, '対角線 P − H', dirs=(-30, -50, -10), color=RED, dists=(70, 95))
z.free_text(P(24.6, 51.6), 'Conjg(B − I) × (P − H)\n＝ −13.2849 ＋ 75.0658i', fs=15, color=RED,
            offsets=((0, 0), (0, -20), (20, 0), (-20, 0)))
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu11_taikakusen.png')

# =====================================================================
# 図12：本番で解く順番（P点と面積がいちばん重い）
# 2026-10-02追加
# =====================================================================
fig = plt.figure(figsize=(16, 8), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図12　本番で解く順番　P点と（イ）（ロ）の面積は後に回す', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
STEPS = [
    ('①', '問1と問5\n（計算なし）', '第1欄・第5欄', BLUE),
    ('②', 'B点・D点の\n放射', '第2欄 B・D', BLUE),
    ('③', '申請書の\n地積以外の欄', '第3欄\n（1行目の45.88も）', GREEN),
    ('④', 'P点の交点', '第2欄 P', RED),
    ('⑤', '（イ）（ロ）の\n面積', '第3欄の地積', RED),
    ('⑥', '地積測量図の\n辺長と作図', '第4欄', ORANGE),
]
w, h, gap = 14.2, 42, 2.2
for i, (no, t, ran, col) in enumerate(STEPS):
    x = 1 + i * (w + gap)
    ax.add_patch(FancyBboxPatch((x, 22), w, h, boxstyle='round,pad=0.4', facecolor=col, alpha=0.14, edgecolor=col,
                                lw=2))
    ax.text(x + w / 2, 22 + h - 3, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
    ax.text(x + w / 2, 22 + h / 2 - 4, t, ha='center', va='center', fontsize=17, linespacing=1.5)
    ax.text(x + w / 2, 17, ran, ha='center', va='top', fontsize=14, color=col, weight='bold', linespacing=1.4)
    if i < len(STEPS) - 1:
        ax.annotate('', xy=(x + w + gap - 0.3, 43), xytext=(x + w + 0.3, 43),
                    arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
ax.text(1 + 1.5 * (w + gap) - gap / 2, 76, 'P点がなくても書ける', ha='center', fontsize=15, color=GREEN, weight='bold')
ax.annotate('', xy=(1 + 3 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=GREEN))
ax.text(1 + 4 * (w + gap) - gap / 2, 76, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
ax.annotate('', xy=(1 + 5 * (w + gap) - gap, 72), xytext=(1 + 3 * (w + gap), 72),
            arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
fig.text(0.5, 0.09, '申請書は、登記の目的・添付書類・申請人・登録免許税・所在・1行目の45.88・（ロ）の地番と地目・2つの登記原因を先に書ける。\n'
         '途中で時間が切れても、書ける欄は全部埋まっているようにする。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R6_dai21mon_zu12_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図12: 解く順番（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
