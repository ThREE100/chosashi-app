"""平成29年度 第21問（土地）会話形式note記事の解説図11枚を、座標値から作図する。

`../prompt_H29_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。

実行: python3 note-articles-Kijyutsu/H29/Q21/zu/draw_H29_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, area, chiseki, radial, dms, intersect, to_dms, fmt_num  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN)
import matplotlib.pyplot as plt  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
A201, A202 = P(365.21, 287.28), P(361.26, 307.92)
A, B, D, E = P(383.28, 289.54), P(380.12, 303.80), P(364.94, 307.17), P(368.61, 287.12)
F, G = P(378.40, 300.41), P(372.41, 299.32)          # 丁建物の側面（筆界点ではない）
Cx = radial(A202, A201, 17.92, dms(85, 53, 40))
C = r2(Cx)
Cw = r2(radial(A202, A201, 17.92, -dms(85, 53, 40)))  # 反時計回りに引いた誤り
g = cmath.phase(G - F)
Fp = F + cmath.rect(1.0, g + math.pi / 2)             # F′：Fから西へ直角に1.00m
Hx = intersect(A, B, Fp, Fp + (G - F))[0]
Ix = intersect(E, D, Fp, Fp + (G - F))[0]
H, I = r2(Hx), r2(Ix)
Hnx = intersect(A, B, F - 1j, G - 1j)[0]              # 真西に1.00mずらした誤り
Inx = intersect(E, D, F - 1j, G - 1j)[0]
Hn, In = r2(Hnx), r2(Inx)

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('C', C, P(379.06, 310.02)), ('H', H, P(380.99, 299.87)), ('I', I, P(366.75, 297.27)),
                     ('誤りのC', Cw, P(343.95, 303.30)), ('誤りのH', Hn, P(380.99, 299.88)),
                     ('誤りのI', In, P(366.75, 297.29))]:
    assert abs(got - want) < 1e-9, (n, got, want)
assert D.real - Cw.real > 20.9                                     # 誤りのCはD点より約21m南
assert to_dms(cmath.phase(A201 - A202) + 2 * math.pi) == '280°50′02.54″'
assert to_dms(g + math.pi / 2 + 2 * math.pi) == '280°18′47.75″'
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'AH': (A, H, '10.58'), 'HB': (H, B, '4.03'), 'BC': (B, C, '6.31'), 'CD': (C, D, '14.40'),
         'DI': (D, I, '10.06'), 'IE': (I, E, '10.32'), 'EA': (E, A, '14.87'), 'HI': (H, I, '14.48')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
ZEN, IP, RO = [A, B, C, D, E], [H, B, C, D, I], [A, H, I, E]
assert abs(area(ZEN) - 299.83995) < 5e-6 and chiseki(area(ZEN)) == 299.83
assert chiseki(area(IP)) == 146.62 and chiseki(area(RO)) == 153.22
assert round(chiseki(area(IP)) + chiseki(area(RO)), 2) == 299.84
assert round(299.84 - 297.52, 2) == 2.32 and 2.32 > 1.57 and 2.32 < 4.59
print('数値の照合: すべて一致')

KUI = {'A': 'concrete', 'B': 'concrete', 'C': 'concrete', 'D': 'concrete', 'E': 'concrete', 'H': 'metal',
       'I': 'metal'}
CEN = centroid(ZEN)


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


ALL = []

# =====================================================================
# 図1：全体像
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像（合筆・分筆の前）',
                        '対象土地（100番・101番・102番）の外周は A→B→C→D→E。軸に平行な辺はひとつもない。\n'
                        '分割線HI（赤の破線）は、丁建物の側面FGに平行で、その西側に1.00m離れた線。3筆の間の筆界の境界標は見つかっていない。\n'
                        'B点から北へ延びる線（110－1と110－2の境）は座標がないので、向きは調査図素図に合わせた模式。')
z = Zu(ax)
fit(ax, ZEN + [A201, A202], margin=0.10, pad_aspect=True)
z.poly(ZEN, fill=GREEN)
z.line(F, G, color=BLUE, lw=2.4)
z.line(H, I, color=RED, lw=1.8, ls='--')
z.line(B, B + P(3.0, 0.55), lw=1.4)
z.north_arrow()
z.free_text(CEN + P(-3.0, -5.0), '対象土地（100番・101番・102番）\n登記記録の合計 297.52㎡', fs=15,
            offsets=((0, 0), (0, -20), (-20, -20)))
for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E')]:
    z.point(p, KUI[n])
    z.point_label(p, n, away=(B + P(-1, -1) if n == 'B' else CEN))
for p, n in [(H, 'H'), (I, 'I')]:
    z.point(p, 'metal', size=9, color=RED)
    z.point_label(p, n, away=CEN + P(0, 3), color=RED)
for p, n in [(F, 'F'), (G, 'G')]:
    z.point(p, 'dot', color=BLUE)
    z.point_label(p, n, away=CEN + P(0, -6), color=BLUE)
for p, n in [(A201, 'A201'), (A202, 'A202')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=CEN, dists=(22, 30, 40))
z.callout(F + (G - F) * 0.5, '丁建物の側面FG', dirs=(0, 20, -20), color=BLUE, dists=(60, 80, 100))
z.callout(H + (I - H) * 0.35, 'HI：FGに平行、西へ1.00m', dirs=(160, 180, 140), color=RED, dists=(90, 120, 150))
z.edge_label(E, A, '99－3', CEN, fs=15, dists=(30, 40), rotate=False)
z.edge_label(C, D, '103－2', CEN, fs=15, dists=(34, 44), rotate=False)
z.edge_label(A, H, '110－1', CEN, fs=15, dists=(26, 36), rotate=False)
z.edge_label(B, C, '110－2', CEN, fs=15, dists=(26, 36), rotate=False)
z.edge_label(E, D, '道路', CEN, fs=15, dists=(28, 38), rotate=False, ts=(0.5, 0.4, 0.6))
ALL += save(fig, [z], 'H29_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図3：問1 C点（放射）
# =====================================================================
fig, (ax,) = new_figure('図3　問1　C点の求め方（A202から放射、観測角は時計回り）',
                        'A202→A201の方向角 −79°09′57.46″（＋360°＝280°50′02.54″、真数表の280°50′03″）に、時計回りの 85°53′40″ を足すと 6°43′42.54″。\n'
                        'C ＝ A202 ＋ 17.92∠(arg(A201 − A202) ＋ 85°53′40″) ＝ 379.0565… ＋ 310.0195…i → C（379.06, 310.02）\n'
                        '反時計回りに引くと（343.95, 303.30）。D点より約21m南の、道路の向こうに出てしまう。')
z = Zu(ax)
fit(ax, ZEN + [A201, A202, Cw], margin=0.08, pad_aspect=True)
z.poly(ZEN, color=GRAY, lw=1.4, fill=GREEN, alpha=0.12)
z.line(A202, A201, color=GRAY, lw=1.4, ls='--')
z.line(A202, C, color=RED, lw=2.4)
z.line(A202, Cw, color=GRAY, lw=1.4, ls=':')
z.line(A202, A202 + P(8.5, 0), color=GRAY, lw=1.2, ls='--')
z.angle_arc(A202, 3.2, 0, 280.834, color=BLUE, lw=1.6)
z.angle_arc(A202, 5.0, 280.834, 366.728, color=RED, lw=2.0)
z.north_arrow()
z.point(A202, 'kijun')
z.point(A201, 'kijun')
z.point(C, 'dot', color=RED)
z.point(Cw, 'dot', color=GRAY)
for p, n in [(A, 'A'), (B, 'B'), (D, 'D'), (E, 'E')]:
    z.point(p, KUI[n], color=GRAY)
    z.point_label(p, n, away=CEN, color=GRAY)
z.callout(C, 'C（379.06, 310.02）', dirs=(20, 0, 40), color=RED)
z.callout(Cw, '反時計回りに引いた誤り（343.95, 303.30）', dirs=(0, 20, -20, 160), color=GRAY, dists=(40, 60, 80))
z.callout(A202, '器械点 A202', dirs=(-20, 0, -40), dists=(40, 55, 70))
z.callout(A201, '後視点 A201', dirs=(-150, -170, 180, -130), dists=(40, 55, 70))
z.free_text(A202 + P(-5.2, 2.6), '方向角\n280°50′02.54″', color=BLUE, fs=14,
            offsets=((0, 0), (20, 0), (40, 0), (0, -20), (30, -20), (-20, -30)))
z.free_text(A202 + P(5.0, 3.2), '観測角 85°53′40″\n（時計回り）', color=RED, fs=14,
            offsets=((0, 0), (20, 0), (30, 15), (40, -10)))
z.edge_label(A202, C, '17.92', A202 + P(0, 10), color=RED, fs=15, dists=(12, 18, 24))
ALL += save(fig, [z], 'H29_dai21mon_zu03_C_housha.png')


# =====================================================================
# 図4・図5：問1 H点・I点（平行線との交点）。左に全体、右に拡大
# =====================================================================
def kouten_zu(no, name, P_ok_x, P_ok, P_ng_x, P_ng, p1, p2, pname, caption, fname):
    fig, axes = new_figure(f'図{no}　問1　{name}点の求め方（FGに平行で、西へ直角に1.00m）', caption, ncols=2,
                           width_ratios=[1.35, 1])
    zs = []
    # 左：全体
    z = Zu(axes[0], fontsize=14)
    u = (G - F) / abs(G - F)
    fit(axes[0], ZEN + [F - u * 8.5, G + u * 9.5, Fp - u * 3.5, Fp + u * 16.5], margin=0.06, pad_aspect=True)
    z.poly(ZEN, fill=GREEN, alpha=0.12)
    z.line(F - u * 8.5, G + u * 9.5, color=BLUE, lw=1.4, ls='--')
    z.line(F, G, color=BLUE, lw=2.6)
    z.line(Fp - u * 3.5, Fp + u * 16.5, color=RED, lw=1.8)
    z.line(F, Fp, color=RED, lw=1.8)
    z.right_angle(F, G, Fp, size=0.6, color=RED)
    z.north_arrow()
    for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E')]:
        z.point(p, KUI[n])
        z.point_label(p, n, away=CEN)
    z.point(F, 'dot', color=BLUE)
    z.point(G, 'dot', color=BLUE)
    z.point(Fp, 'dot', color=RED)
    z.point_label(F, 'F', away=Fp + P(0, -2), color=BLUE)
    z.point_label(G, 'G', away=Fp + P(0, -2), color=BLUE)
    z.point_label(Fp, 'F′', away=F + P(0, 2), color=RED)
    z.point(P_ok, 'metal', size=9, color=RED)
    z.callout(P_ok, f'{pname}（{P_ok.real:.2f}, {P_ok.imag:.2f}）', dirs=(150, 170, 130, 190) if pname == 'H' else
              (-150, -170, -130, 190), color=RED, dists=(55, 75, 95))
    z.callout(F + (Fp - F) * 0.5, '直角に 1.00', dirs=(60, 80, 40, 100), color=RED, dists=(55, 75, 95))
    z.callout(Fp + u * 14.5, 'F′を通り FG に平行な線', dirs=(180, 200, 160), color=RED, dists=(40, 60, 80))
    zs.append(z)
    # 右：拡大（約0.07m四方）
    z = Zu(axes[1], fontsize=14)
    ctr = (P_ok_x + P_ng_x) / 2
    box = [ctr + P(0.035, 0.035), ctr + P(-0.035, -0.035)]
    fit(axes[1], box, margin=0.0, pad_aspect=True)
    axes[1].set_title(f'{pname}点のまわりの拡大（約0.07m四方）', fontsize=17, weight='bold')
    w = (p2 - p1) / abs(p2 - p1)
    t0 = ((ctr - p1) * w.conjugate()).real
    z.line(p1 + w * (t0 - 0.06), p1 + w * (t0 + 0.06), lw=2.0)
    z.line(P_ok_x - u * 0.06, P_ok_x + u * 0.06, color=RED, lw=1.8)
    z.line(P_ng_x - u * 0.06, P_ng_x + u * 0.06, color=GRAY, lw=1.5, ls='--')
    z.point(P_ok_x, 'dot', color=RED)
    z.point(P_ng_x, 'dot', color=GRAY)
    z.callout(P_ok_x, f'正しい{pname}\n（{P_ok.real:.2f}, {P_ok.imag:.2f}）', dirs=(-150, -120, -170, -60),
              color=RED, dists=(60, 80, 100))
    z.callout(P_ng_x, f'真西に1.00mの誤り\n（{P_ng.real:.2f}, {P_ng.imag:.2f}）', dirs=(30, 60, 10, 120),
              color=GRAY, dists=(60, 80, 100))
    z.callout(p1 + w * (t0 + 0.022), '直線AB' if pname == 'H' else '直線ED', dirs=(-90, -60, -120, 90), dists=(30, 45, 60))
    zs.append(z)
    return save(fig, zs, fname)


ALL += kouten_zu(4, 'H', Hx, H, Hnx, Hn, A, B, 'H',
                 'F′ ＝ F ＋ 1.00∠(arg(G − F) ＋ 90°)（280°18′47.75″の向き）。H ＝ A ＋ (B − A) × 64.3421 ÷ 88.8618 ＝ 380.9919… ＋ 299.8652…i → H（380.99, 299.87）。\n'
                 'Yだけ1.00減らした線はFGから 1.00 × cos 10°18′48″ ＝ 0.98384 しか離れず、交点は（380.99, 299.88）にずれる。',
                 'H29_dai21mon_zu04_H_kouten.png')
ALL += kouten_zu(5, 'I', Ix, I, Inx, In, E, D, 'I',
                 'I ＝ E ＋ (D − E) × 62.8476 ÷ 124.0998 ＝ 366.7514… ＋ 297.2738…i → I（366.75, 297.27）。\n'
                 'Yだけ1.00減らした誤りの線との交点は（366.75, 297.29）で、Y座標が0.02ずれる。検算：FGからの離れ H 0.9949…、I 1.0035…',
                 'H29_dai21mon_zu05_I_kouten.png')

# =====================================================================
# 図8：問2 公差の判定（数直線）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図8　問2　地積の更正の登記が必要かの判定（市街地地域なので精度区分 甲2）', fontsize=24, weight='bold', y=0.96)
ax = fig.add_axes([0.05, 0.22, 0.90, 0.62])
reg, meas, k2, o1 = 297.52, 299.84, 1.57, 4.59
ax.set_xlim(reg - 5.6, reg + 5.6)
ax.set_ylim(-2.2, 2.6)
ax.axis('off')
ax.plot([reg - 5.3, reg + 5.3], [0, 0], color=BLACK, lw=2)
for j in range(-10, 11):
    v = reg + j * 0.5
    ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1.0)
    if j % 2 == 0:
        ax.text(v, -0.3, f'{v:.2f}', ha='center', va='top', fontsize=12, color=GRAY)
ax.axvspan(reg - k2, reg + k2, ymin=0.43, ymax=0.49, color=GREEN, alpha=0.35)
ax.text(reg - k2, 0.35, f'甲2 の公差の範囲 ±{k2:.2f}', ha='left', va='bottom', fontsize=15, color=GREEN, weight='bold')
ax.plot([reg - o1, reg + o1], [1.55, 1.55], color=GRAY, lw=3, ls='--')
ax.text(reg - o1, 1.7, f'乙1 なら ±{o1:.2f}（範囲内に見えてしまう。市街地地域では使わない）', ha='left', va='bottom',
        fontsize=14, color=GRAY)
ax.plot([reg], [0], 'o', ms=13, color=BLUE)
ax.text(reg, -0.85, f'分筆前の地積（合筆後）\n{reg:.2f}㎡', ha='center', va='top', fontsize=15, color=BLUE, weight='bold')
ax.plot([meas], [0], 'o', ms=13, color=RED)
ax.text(meas, -0.85, f'分筆後の地積の合計\n146.62 ＋ 153.22 ＝ {meas:.2f}㎡', ha='left', va='top', fontsize=15,
        color=RED, weight='bold')
ax.annotate('', xy=(meas, 0.75), xytext=(reg, 0.75), arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
ax.text((reg + meas) / 2 + 0.6, 0.85, f'差 {meas - reg:.2f}㎡ ＞ {k2:.2f}㎡　→ 範囲の外', ha='left', va='bottom',
        fontsize=16, color=RED, weight='bold')
fig.text(0.5, 0.06, '対象土地の地域は市街地地域（不動産登記規則第10条第2項第1号）。誤差の限度は精度区分 甲2 まで（同条第4項第1号、第77条第5項で準用）。\n'
         '合筆後の297.52㎡の行の甲2は1.57㎡。差2.32㎡はこれを超える → 分筆の前提として地積の更正の登記が必要（準則第72条第1項）。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'H29_dai21mon_zu08_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図8: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図9：問3 分筆後の区画と地番
# =====================================================================
fig, axes = new_figure('図9　問3　合筆の後に、地積の更正と分筆を一の申請情報で',
                       '左：先に合筆した100番（登記記録 115.70 ＋ 132.23 ＋ 49.59 ＝ 297.52㎡）。座標で求めると 299.83㎡ で、差が甲2の公差を超える。\n'
                       '右：土地地積更正・分筆登記の後。東の（イ）100番1 146.62㎡（甲野太郎）、西の（ロ）100番2 153.22㎡（甲野次郎）。',
                       ncols=2)
zs = []
for ax, after in [(axes[0], False), (axes[1], True)]:
    z = Zu(ax, fontsize=14)
    fit(ax, ZEN, margin=0.14, pad_aspect=True)
    if not after:
        ax.set_title('合筆の後（分筆の前）', fontsize=19, weight='bold')
        z.poly(ZEN, fill=GREEN)
        z.line(H, I, color=RED, lw=1.8, ls='--')
        z.free_text(centroid(IP), '100番（合筆後）\n登記記録 297.52㎡\n実測 299.83㎡', fs=16,
                    offsets=((0, 0), (10, 0), (20, 10), (-10, 10)))
        z.callout(H + (I - H) * 0.8, '分筆線 HI', dirs=(-150, -170, -130), color=RED, dists=(60, 80))
    else:
        ax.set_title('土地地積更正・分筆登記の後', fontsize=19, weight='bold')
        z.poly(IP, fill=BLUE)
        z.poly(RO, fill=ORANGE)
        z.free_text(centroid(IP), '（イ）100番1\n146.62㎡\n甲野太郎', fs=15)
        z.free_text(centroid(RO), '（ロ）100番2\n153.22㎡\n甲野次郎', fs=15)
    for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (H, 'H'), (I, 'I')]:
        z.point(p, KUI[n], size=(9 if KUI[n] == 'metal' else 7))
        z.point_label(p, n, away=CEN)
    z.north_arrow()
    zs.append(z)
ALL += save(fig, zs, 'H29_dai21mon_zu09_bunpitsu_chiban.png')

# =====================================================================
# 図10：問4 地積測量図の完成見本
# =====================================================================
fig, (ax,) = new_figure('図10　問4　地積測量図（100番1、100番2）の完成見本',
                        '縮尺1/250で 1m ＝ 4mm（横約92mm・縦約73mm）。辺長は小数第3位を四捨五入（HB 4.0251… → 4.03、CD 14.4047… → 14.40）。\n'
                        '合筆で消えた3筆の間の筆界と、丁建物の角F・Gは描かない。\n座標値・地積・求積方法・測量年月日は書かない（問題文の注5）。基準点は位置と点名だけ（問題文の注6）。\n'
                        'A201・A202まで入れると縦約88mm。B点から北へ延びる110－1と110－2の境の線は、座標がないので向きは模式。')
z = Zu(ax)
fit(ax, ZEN + [A201, A202], margin=0.10, pad_aspect=True)
z.poly([A, H, B, C, D, I, E], lw=2.0)
z.line(H, I, lw=2.0)
z.line(B, B + P(3.0, 0.55), lw=1.4)
z.north_arrow()
for n, (p, q, s) in SIDES.items():
    ref = CEN if n != 'HI' else centroid(RO)
    z.edge_label(p, q, s, ref, fs=16, outward=(n != 'HI'))
z.free_text(centroid(IP), '（イ）\n100－1', fs=17)
z.free_text(centroid(RO), '（ロ）\n100－2', fs=17)
for p, n in [(A, 'A'), (H, 'H'), (B, 'B'), (C, 'C'), (D, 'D'), (I, 'I'), (E, 'E')]:
    z.point(p, KUI[n], size=(9 if KUI[n] == 'metal' else 7))
    z.point_label(p, n, away=CEN)
for p, n in [(A201, 'A201'), (A202, 'A202')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=CEN, dists=(22, 30, 40))
z.edge_label(E, A, '99－3', CEN, fs=16, dists=(44, 54), rotate=False)
z.edge_label(C, D, '103－2', CEN, fs=16, dists=(48, 58), rotate=False)
z.edge_label(A, H, '110－1', CEN, fs=16, dists=(40, 50), rotate=False)
z.edge_label(B, C, '110－2', CEN, fs=16, dists=(40, 50), rotate=False)
z.edge_label(E, D, '道路', CEN, fs=16, dists=(44, 54), rotate=False, ts=(0.5, 0.4, 0.6))
z.free_text(P(363.6, 291.2), '（単位：ｍ）\n◎ コンクリート杭：A・B・C・D・E\n● 金属標：H・I\n△ 基準点：A201・A202', fs=13,
            ha='left', va='top', offsets=((0, 0), (0, -30), (20, 0), (-40, 0)))
ALL += save(fig, [z], 'H29_dai21mon_zu10_chiseki_sokuryouzu.png')

from matplotlib.patches import FancyBboxPatch, FancyArrowPatch  # noqa: E402


def fixed_figure(title, caption, h=12):
    setup_font()
    fig = plt.figure(figsize=(16, h), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.12, 0.94, 0.78])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.text(0.5, 0.035, caption, ha='center', va='bottom', fontsize=16)
    return fig, ax


def box(ax, x, y, w, h, text, ec=BLACK, fc='white', fs=16, weight='normal', color=BLACK, ha='center'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.6', ec=ec, fc=fc, lw=1.8))
    tx = x + w / 2 if ha == 'center' else x + 1.2
    ax.text(tx, y + h / 2, text, ha=ha, va='center', fontsize=fs, weight=weight, color=color, linespacing=1.5)


# =====================================================================
# 図2：注の仕分け（固定配置）
# =====================================================================
fig, ax = fixed_figure('図2　注の仕分け（問題文の注・調査図素図の注・観測値の表の注）',
                       '問題文の注のうち、今年の答えに効くのは注5・注6・注10と問3のただし書き。記事では「問題文の注3」「観測値の表の注1」のように、どの注かを言い分ける。')
box(ax, 2, 70, 46, 22, '問題文の注・毎年ほぼ同じ（読み流してよい）\n注1 行為は適法　注2 書面申請\n注3 座標は小数第3位を四捨五入　注4 辺長も同じ\n注7 距離の補正はしない　注8 真数表を使う　注9 訂正の方法',
    ec=GRAY, fc='#f4f4f4', fs=15)
box(ax, 2, 22, 46, 38, '問題文の注・今年の答えに効く（印を付ける）\n\n注5：地積測量図に、座標値・系の番号・\n　　 地積と求積方法・測量年月日を書かない\n注6：A市基準点は位置と点名だけ（座標値は書かない）\n注10：問3・問4は予定地番（1(6)）を使う\n　　 A区画 100番1、B区画 100番2\n問3のただし書き：合筆以外に必要な登記は\n　　 一の申請情報で（→ 土地地積更正・分筆登記）',
    ec=RED, fc='#fdeeee', fs=15, ha='left')
box(ax, 54, 58, 44, 34, '調査図素図の注\n\nH点は A点と B点を結ぶ直線上の点\nI点は E点と D点を結ぶ直線上の点\n実線は筆界、HとIを結ぶ直線は土地の分割線',
    ec=BLUE, fc='#eef4fb', fs=15)
box(ax, 54, 22, 44, 26, '観測値の表の注\n\n注1：観測角は、後視方向を0°として時計回り\n注2：北は X軸の正方向',
    ec=GREEN, fc='#eef8ee', fs=15)
box(ax, 2, 3, 96, 10, '聴取記録の6（HIは FG に平行で西へ1.00m）と真数表の 10°18′48″・280°18′48″ は、注ではないが H点・I点の計算の条件',
    ec=ORANGE, fc='#fff4e6', fs=15)
path = os.path.join(OUT, 'H29_dai21mon_zu02_chuu_shiwake.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図2: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図6：H点・I点の別解（FGからの離れを比例で分ける）
# =====================================================================
u = (G - F) / abs(G - F)
foot = lambda p: F + u * ((p - F) * u.conjugate()).real  # noqa: E731  直線FGへの垂線の足
off = lambda p: ((G - F).conjugate() * (p - F)).imag / abs(G - F)  # noqa: E731  西をプラスとする離れ
OFF = {n: off(p) for n, p in [('A', A), ('B', B), ('E', E), ('D', D)]}
assert [fmt_num(abs(v)).rstrip('…') for v in OFF.values()] == ['11.5680', '3.0272', '11.3225', '9.0605']
tH2 = (11.5680 - 1) / (11.5680 + 3.0272)
tI2 = (11.3225 - 1) / (11.3225 + 9.0605)
assert r2(A + (B - A) * tH2) == H and r2(E + (D - E) * tI2) == I
fig, axes = new_figure('図6　H点・I点の別解（FGからの離れを比例で分ける）',
                       '直線FGからの離れ（Conjg(G − F) × (P − F) のiの係数 ÷ Abs(G − F)。西をプラス、東をマイナス）：A 11.5680…、B −3.0272…、E 11.3225…、D −9.0605…\n'
                       'H ＝ A ＋ (B − A) × (11.5680 − 1) ÷ (11.5680 ＋ 3.0272)、I ＝ E ＋ (D − E) × (11.3225 − 1) ÷ (11.3225 ＋ 9.0605)\n'
                       'F′を作る方法と同じ表示（380.9919… ＋ 299.8652…i、366.7514… ＋ 297.2738…i）になる。',
                       ncols=2, width_ratios=[1.25, 1])
fig.subplots_adjust(bottom=0.19)
z = Zu(axes[0], fontsize=14)
ends = [foot(A) - u * 1.0, foot(D) + u * 1.0]
fit(axes[0], ZEN + ends, margin=0.08, pad_aspect=True)
z.poly(ZEN, fill=GREEN, alpha=0.12)
z.line(ends[0], ends[1], color=BLUE, lw=1.4, ls='--')
z.line(F, G, color=BLUE, lw=2.6)
z.line(H, I, color=RED, lw=2.0)
z.north_arrow()
for n, p in [('A', A), ('B', B), ('C', C), ('D', D), ('E', E)]:
    z.point(p, KUI[n])
    z.point_label(p, n, away=CEN)
for n, p in [('H', H), ('I', I)]:
    z.point(p, 'metal', size=9, color=RED)
    z.point_label(p, n, away=CEN + P(0, 3), color=RED)
z.point(F, 'dot', color=BLUE)
z.point(G, 'dot', color=BLUE)
z.point_label(F, 'F', away=CEN + P(0, -6), color=BLUE)
z.point_label(G, 'G', away=CEN + P(0, -6), color=BLUE)
for n, p, d in [('A', A, (120, 150, 90, 180)), ('B', B, (60, 30, 90)), ('E', E, (-70, -90, -50, -110)),
                ('D', D, (-60, -30, -90))]:
    v = OFF[n]
    z.callout(p, f'{n}の離れ　{"西へ" if v > 0 else "東へ"}{abs(v):.2f}', dirs=d, color=GRAY, dists=(45, 60, 80))
z.callout(H + (I - H) * 0.5, 'HI：西へ 1.00', dirs=(170, 190, 150), color=RED, dists=(60, 80, 100))
# 右：離れの一次式（t と離れ）
ax = axes[1]
ax.set_xlim(-0.30, 1.12)
ax.set_ylim(-11.5, 14.5)
ax.axhline(0, color=BLUE, lw=1.4)
ax.axhline(1, color=RED, lw=1.2, ls='--')
ax.plot([0, 1], [OFF['A'], OFF['B']], color=BLACK, lw=2.2)
ax.plot([0, 1], [OFF['E'], OFF['D']], color=GRAY, lw=2.2)
ax.plot([tH2], [1], 'o', color=RED, ms=9)
ax.plot([tI2], [1], 'o', color=RED, ms=9)
ax.text(-0.03, OFF['A'] + 0.5, 'A 11.57', fontsize=14, ha='right')
ax.text(1.0, OFF['B'] - 1.4, 'B −3.03', fontsize=14, ha='right')
ax.text(-0.03, OFF['E'] - 1.2, 'E 11.32', fontsize=14, color=GRAY, ha='right')
ax.text(1.0, OFF['D'] - 1.4, 'D −9.06', fontsize=14, ha='right', color=GRAY)
ax.text(tH2 + 0.03, 2.2, f'H：t ＝ {fmt_num(tH2)}', fontsize=14, color=RED)
ax.text(tI2 - 0.03, -1.6, f'I：t ＝ {fmt_num(tI2)}', fontsize=14, color=RED, ha='right')
ax.text(1.1, 0.25, '直線FG（離れ 0）', fontsize=13, color=BLUE, ha='right', va='bottom')
ax.text(-0.28, 1.3, '西へ 1.00', fontsize=13, color=RED, va='bottom')
ax.set_xlabel('AからB（EからD）へ進む割合 t', fontsize=14)
ax.set_ylabel('FGからの離れ（m、西がプラス）', fontsize=14)
ax.set_title('離れは t に比例して変わる', fontsize=17, weight='bold')
for sp in ('top', 'right'):
    ax.spines[sp].set_visible(False)
ALL += save(fig, [z], 'H29_dai21mon_zu06_HI_betsukai.png')

# =====================================================================
# 図7：（ロ）の面積を対角線で
# =====================================================================
dz = (I - A).conjugate() * (E - H)
assert f'{dz.imag:.4f}' == '306.4549' and abs(abs(dz.imag) / 2 - area(RO)) < 1e-9
fig, (ax,) = new_figure('図7　（ロ）100番2の面積を対角線で出す（四角形A・H・I・E）',
                        '四角形の倍面積は、対角線どうしの積 Conjg(I − A) × (E − H) のiの係数：306.4549 → 306.4549 ÷ 2 ＝ 153.22745 → 153.22㎡。\n'
                        '4点を順に回る式（A・Conjg(H) ＋ H・Conjg(I) ＋ I・Conjg(E) ＋ E・Conjg(A)）と同じ値。対角線はAとI、HとE（辺どうしを掛けない）。')
z = Zu(ax)
fit(ax, RO + [B, D], margin=0.10, pad_aspect=True)
z.poly(RO, fill=ORANGE, alpha=0.22)
z.poly(IP, color=GRAY, lw=1.2)
z.line(A, I, color=RED, lw=2.4)
z.line(H, E, color=BLUE, lw=2.4)
z.north_arrow()
for n, p in [('A', A), ('H', H), ('I', I), ('E', E)]:
    z.point(p, KUI[n], size=(9 if KUI[n] == 'metal' else 7))
    z.point_label(p, n, away=centroid(RO))
z.callout(A + (I - A) * 0.72, '対角線 I − A', dirs=(-20, -40, 0), color=RED, dists=(60, 80, 100))
z.callout(H + (E - H) * 0.28, '対角線 E − H', dirs=(20, 40, 0), color=BLUE, dists=(60, 80, 100))
mid_ae = (A + E) / 2
z.free_text(mid_ae + (centroid(RO) - mid_ae) * 0.45, '（ロ）100番2\n153.22745㎡', fs=16,
            offsets=((0, 0), (0, -25), (0, 25), (10, 0)))
z.free_text(centroid(IP), '（イ）100番1', fs=15, color=GRAY)
ALL += save(fig, [z], 'H29_dai21mon_zu07_ro_taikakusen.png')

# =====================================================================
# 図11：本番で解く順番（固定配置）
# =====================================================================
fig, ax = fixed_figure('図11　本番で解く順番（H点・I点がなくても書ける欄を先に）',
                       '緑はH点・I点がなくても書ける欄、橙はH点・I点が出てから書く欄。地積の更正が要るかは、C点を入れた全体の面積（299.83）だけで決まる。', h=13)
steps = [
    ('① 注と問を読む：今年だけの注（問題文の注5・注6・注10）と問3のただし書きに印', GREEN),
    ('② C点を放射で出す（観測値の表の注1：時計回りに足す）→ C（379.06, 310.02）', GREEN),
    ('③ 全体の面積 299.83 → 合筆後の297.52の行の甲2（1.57）と比べ、問2を書き上げる', GREEN),
    ('④ 申請書：登記の目的・添付書類・登録免許税・申請人・所在・1行目（297.52）・（イ）（ロ）の地番と地目と原因\n　 地積測量図：地番・所在・外周・BC・CD・EA・境界標・A201・A202・隣接地', GREEN),
    ('⑤ F′を作って H点・I点（FGからの離れが1.00になるかを検算）', ORANGE),
    ('⑥ （イ）146.62・（ロ）153.22 の地積と、辺長5本（AH・HB・DI・IE・HI）と分筆線を書き入れる', ORANGE),
]
y = 88
for i, (t, c) in enumerate(steps):
    hgt = 13 if '\n' in t else 8
    box(ax, 3, y - hgt, 94, hgt, t, ec=c, fc=('#eef8ee' if c == GREEN else '#fff4e6'), fs=16, ha='left')
    if i < len(steps) - 1:
        ax.add_patch(FancyArrowPatch((50, y - hgt - 0.6), (50, y - hgt - 4.4), arrowstyle='-|>', mutation_scale=20,
                                     color=GRAY, lw=1.6))
    y -= hgt + 5.2
path = os.path.join(OUT, 'H29_dai21mon_zu11_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図11: 流れ図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL))
