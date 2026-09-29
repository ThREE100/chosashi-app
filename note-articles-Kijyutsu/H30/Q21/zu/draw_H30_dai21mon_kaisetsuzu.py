"""平成30年度 第21問（土地）会話形式note記事の解説図11枚を、座標値から作図する。

`../prompt_H30_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
座標は世界測地系IX系の −5万台なので、記事と同じく原点を（−50720.00, −14880.00）にずらして作図し、
吹き出しには元の座標を書く（ずらしても距離・方向・面積は変わらない）。
参照実装は `../../../R6/Q21/zu/draw_R6_dai21mon_kaisetsuzu.py`。

実行: python3 note-articles-Kijyutsu/H30/Q21/zu/draw_H30_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, chiseki, intersect  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値。原点を（−50720, −14880）にずらす） ------------------
O = P(-50720.00, -14880.00)
RAW = {'T1': (-50731.54, -14904.34), 'T2': (-50732.19, -14875.11), 'T3': (-50710.35, -14900.56),
       'T4': (-50736.86, -14856.95), 'A': (-50729.15, -14899.00), 'B': (-50733.63, -14859.25),
       'C': (-50721.79, -14857.95), 'E': (-50720.03, -14879.67), 'F': (-50719.93, -14888.41),
       'G': (-50719.87, -14897.37), 'H': (-50710.06, -14878.97), 'J': (-50731.33, -14879.66),
       'K': (-50720.07, -14878.87)}
S = {k: r2(P(*v) - O) for k, v in RAW.items()}
T1, T2, T3, T4 = S['T1'], S['T2'], S['T3'], S['T4']
A, B, C, E, F, G, H, J, K = (S[k] for k in 'ABCEFGHJK')
D = r2(radial(T2, T1, 13.22, dms(116, 50, 31)))
I = r2(intersect(H, E, A, B)[0])
Dw = r2(radial(T2, T1, 13.22, -dms(116, 50, 31)))    # 反時計回りに測った誤り
Iw = r2(intersect(E, E + 1, A, B)[0])                # Eの真南にとった誤り


def ab(p):
    """ずらした点を元の座標の文字列にする。"""
    q = p + O
    return f'（{q.real:.2f}, {q.imag:.2f}）'.replace('-', '−')


# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
assert ab(D) == '（−50720.53, −14868.88）' and ab(I) == '（−50731.24, −14880.46）'
assert ab(Dw) == '（−50744.12, −14869.40）' and ab(Iw) == '（−50731.33, −14879.67）'
assert f'{T2.real - Dw.real:.2f}' == '11.93'
assert f'{abs(Iw - J):.2f}' == '0.01' and Iw.imag - I.imag > 0   # 誤りのIはJとほぼ重なり、正しいIより東
_t = intersect(H, E, A, B)[1]
assert f'{_t:.4f}' == '2.1244'
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'EK': (E, K, '0.80'), 'KD': (K, D, '10.00'), 'DC': (D, C, '11.00'), 'CB': (C, B, '11.91'),
         'BJ': (B, J, '20.54'), 'JI': (J, I, '0.81'), 'IE': (I, E, '11.24'), 'KJ': (K, J, '11.29')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert f'{abs(J - I):.4f}' == '0.8050'
KOU = [A, G, F, E, I]               # 甲土地（10番1）
KOU_W = [A, G, F, E, Iw]            # 誤りのIで囲んだ甲土地
OTSU = [E, K, D, C, B, J, I]        # 乙土地（11番）分筆前
RO = [E, I, J, K]                   # （ロ）11番2（売る帯。宅地）
II = [K, D, C, B, J]                # （イ）11番1（残る駐車場。雑種地）
assert f'{area(KOU):.5f}' == '187.18645' and f'{chiseki(area(KOU)):.2f}' == '187.18'
assert f'{chiseki(area(KOU_W)):.2f}' == '191.65'
assert f'{area(OTSU):.5f}' == '253.60035' and chiseki(area(OTSU), takuchi=False) == 253
assert f'{area(RO):.5f}' == '9.03935' and f'{chiseki(area(RO)):.2f}' == '9.03'
assert f'{area(II):.3f}' == '244.561' and chiseki(area(II), takuchi=False) == 244
BRG_T1 = math.degrees(cmath.phase(T1 - T2)) + 360          # T2→T1の方向角 271.27°
BRG_D = BRG_T1 + 116 + 50 / 60 + 31 / 3600                 # 388.12° → 28.12°
assert to_dms(math.radians(BRG_T1)) == '271°16′26.04″'
assert to_dms(math.radians(math.degrees(cmath.phase(H - E)))) == '4°00′58.26″'
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

# =====================================================================
# 図1：全体像（北を上にして座標どおりに描き直した調査図素図）
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像（平成30年10月の測量時点）',
                        '座標は世界測地系IX系の −5万台。原点を（−50720.00, −14880.00）にずらして計算する（距離・方向・面積は変わらない）。\n'
                        '甲土地（10番1）と、乙土地（11番）の細い帯E・I・J・Kを山田太郎に売る。ブロック塀はK→Jの直線の上（平成30年10月1日完了）。')
z = Zu(ax, fontsize=14)
fit(ax, [A, G, H, C, B, T1, T2, T3, T4], margin=0.06, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.poly(RO, color=RED, lw=0, fill=RED, alpha=0.35, check=False)
z.line(E, H, color=BLACK, lw=2.0)
z.line(K, J, color=RED, lw=3.0, ls='--')
z.north_arrow()
z.free_text(centroid(KOU), '甲土地\n10番1　宅地\n187.18㎡\n（本件建物）', fs=15)
z.free_text(centroid(II), '乙土地\n11番　雑種地\n253㎡\n（駐車場）', fs=15)
z.callout(E + (I - E) * 0.25, '売る帯E・I・J・K', dirs=(20, 40, 0), color=RED, dists=(160, 190, 220))
z.callout(K + (J - K) * 0.7, 'ブロック塀（K→J）', dirs=(-20, -40, 0), color=RED, dists=(90, 120, 150))
for p, n, ref in [(A, 'A', KOU), (G, 'G', KOU), (F, 'F', KOU), (E, 'E', KOU), (I, 'I', KOU), (H, 'H', RO),
                  (B, 'B', OTSU), (C, 'C', OTSU), (D, 'D', OTSU), (J, 'J', OTSU), (K, 'K', OTSU)]:
    z.point(p, 'concrete' if n in 'ABGJKD' else 'metal')
    z.point_label(p, n, away=centroid(ref) if n != 'H' else H + P(-3, 0))
for p, n in [(T1, 'T1'), (T2, 'T2'), (T3, 'T3'), (T4, 'T4')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=centroid(OTSU))
z.free_text(P(5.5, -10.0), '10番2', fs=15, color=GRAY)
z.free_text(P(5.5, 10.0), '10番3', fs=15, color=GRAY)
z.edge_label(A, I, '道路', centroid(KOU), fs=15, color=GRAY, dists=(26, 34), rotate=False)
z.edge_label(C, B, '道路', centroid(OTSU), fs=15, color=GRAY, dists=(26, 34), rotate=False)
z.edge_label(G, A, '道路', centroid(KOU), fs=15, color=GRAY, dists=(26, 34), rotate=False)
ALL_PROBLEMS += save(fig, [z], 'H30_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：問1 D点（T2から放射）
# =====================================================================
fig, (ax,) = new_figure('図2　問1　D点の求め方（T2に据えてT1を後視する放射）',
                        'T2→T1の方向角 271°16′26.04″（電卓の表示は −88°43′33.96″）に、時計回りの観測角 116°50′31″ を足し、13.22m 進む。\n'
                        '反時計回りに測ると、T2より11.93m南の道路の向こう（−50744.12, −14869.40）に出てしまう。\n'
                        '検算：K点がE・Dを結ぶ直線の上（△EDKの倍面積のiの係数 0.0316、ED線から約0.003m）。')
z = Zu(ax, fontsize=14)
fit(ax, [T1, T2, D, Dw, T2 + P(4, 0)] + KOU + OTSU, margin=0.06, pad_aspect=True)   # 背景の区画の頂点も全部入れる
z.poly(KOU, color=GRAY, lw=1.1)
z.poly(OTSU, color=GRAY, lw=1.1)
z.line(T2, T2 + 4, color=GRAY, lw=1.2, ls='--')
z.free_text(T2 + 4, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(T2, T1, color=BLUE, lw=2.0)
z.line(T2, D, color=RED, lw=2.6)
z.line(T2, Dw, color=GRAY, lw=1.4, ls=':')
z.north_arrow()
z.angle_arc(T2, 2.0, 0, BRG_T1, color=BLUE)
z.angle_arc(T2, 3.2, BRG_T1, BRG_D, color=RED)
for p in (T1, T2):
    z.point(p, 'kijun')
z.point(D, 'dot', color=RED, size=9)
z.point(Dw, 'dot', color=GRAY)
for p, n in [(E, 'E'), (K, 'K'), (C, 'C')]:
    z.point(p, 'metal' if n != 'K' else 'concrete')
    z.point_label(p, n, away=centroid(OTSU))
z.edge_label(T2, T1, '後視（T1の方向）', T2 + P(4, 0), color=BLUE, fs=14, ts=(0.55, 0.65, 0.45), dists=(16, 22))
z.edge_label(T2, D, '13.22', T2 + P(0, 6), color=RED, fs=17, ts=(0.55, 0.65, 0.45), dists=(14, 20, 26))
z.callout(T2 + P(1.6, -1.2), '方向角 271°16′26.04″\n（北から時計回りにT1の方向）', dirs=(150, 130, 170), color=BLUE,
          dists=(90, 120, 150))
z.callout(T2 + P(2.4, 2.2), '観測角 116°50′31″\n（T1の方向から時計回り）', dirs=(-30, -10, -50), color=RED,
          dists=(100, 130, 160))
z.callout(D, 'D' + ab(D), dirs=(100, 80, 120, 60), color=RED)
z.callout(Dw, '反時計回りに測った誤り\n' + ab(Dw), dirs=(180, 160, -160), color=GRAY)
z.callout(T2, 'T2' + ab(T2), dirs=(-120, -140, -100), color=BLACK, dists=(80, 110, 140))
z.callout(T1, 'T1' + ab(T1), dirs=(-90, -110, -70, 90), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'H30_dai21mon_zu02_D_housha.png')

# =====================================================================
# 図3：問1 I点（H→Eの延長線とA→Bの交点）
# =====================================================================
fig, (ax1, ax2) = new_figure('図3　問1　I点の求め方（H→Eの延長線とA→Bの交点）',
                             'E→Hは北へ9.97m進む間に東へ0.70m傾いている（真北から東へ4°00′58.26″）。真南北の線ではない。\n'
                             'I′ ＝ H′ ＋ (E′ − H′) × t、t ＝ 848.5619 ÷ 399.4435 ＝ 2.1243…（1を超えるので延長線上）。\n'
                             'Eの真南にとると（−50731.33, −14879.67）で、J点とわずか0.01mしか離れず、正しいIより0.79m東。',
                             ncols=2, width_ratios=[1, 1])
za = Zu(ax1, fontsize=14)
fit(ax1, [H] + KOU + OTSU, margin=0.06, pad_aspect=True)   # 背景の区画の頂点も全部入れる
za.poly(KOU, color=GRAY, lw=1.1)
za.poly(OTSU, color=GRAY, lw=1.1)
za.line(H, E, color=BLACK, lw=2.4)
za.line(E, I, color=RED, lw=2.4, ls='--')
za.line(A, B, color=BLUE, lw=2.0)
za.north_arrow(length=0.07)
for p, n in [(H, 'H'), (E, 'E')]:
    za.point(p, 'metal')
    za.point_label(p, n, away=p + P(0, 3))
for p, n in [(A, 'A'), (B, 'B')]:
    za.point(p, 'concrete')
    za.point_label(p, n, away=centroid(OTSU))
za.point(I, 'dot', color=RED, size=9)
za.callout(I, 'I' + ab(I), dirs=(-150, -130, -170), color=RED, dists=(60, 80, 100))
za.callout(H + (E - H) * 0.5, 'H→E（t＝0〜1）', dirs=(170, 150, -170), color=BLACK, dists=(60, 80, 100))
za.callout(E + (I - E) * 0.5, '延長線（t＝1〜2.1243…）', dirs=(10, -10, 30), color=RED, dists=(60, 80, 100))
za.callout(A + (B - A) * 0.75, '直線A→B', dirs=(-60, -80, -40), color=BLUE, dists=(50, 70, 90))
ax1.set_title('全体', fontsize=17, weight='bold', pad=6)

zb = Zu(ax2, fontsize=14)
cen = (I + J) / 2
lo, hi = cen + P(-0.7, -0.9), cen + P(0.7, 0.9)
fit(ax2, [lo, hi], margin=0, pad_aspect=True)
x0, x1 = ax2.get_xlim()
tA = (x0 - A.imag) / (B.imag - A.imag)
tB = (x1 - A.imag) / (B.imag - A.imag)
zb.line(A + (B - A) * tA, A + (B - A) * tB, color=BLUE, lw=2.0)
zb.line(I + (E - I) * (0.6 / abs(E - I)), I, color=RED, lw=2.4, ls='--')
zb.line(Iw, Iw + 0.6, color=GRAY, lw=1.4, ls=':')
zb.north_arrow(length=0.07)
zb.point(I, 'dot', color=RED, size=11)
zb.point(J, 'concrete', size=9)
zb.point(Iw, 'dot', color=GRAY, size=8)
zb.callout(I, 'I' + ab(I), dirs=(-120, -140, -100), color=RED, dists=(60, 80, 100))
zb.callout(J, 'J' + ab(J), dirs=(-80, -100, -60), color=BLACK, dists=(70, 90, 110))
zb.callout(Iw, 'Eの真南にとった誤り\n' + ab(Iw), dirs=(120, 140, 100), color=GRAY, dists=(90, 110, 130))
zb.edge_label(I, Iw, '0.79', I + P(-0.3, 0), color=RED, fs=16, dists=(14, 20), rotate=False)
ax2.set_title('I・Jのまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H30_dai21mon_zu03_I_kouten.png')

# =====================================================================
# 図4：問1 I点の裏付け（甲土地の面積）
# =====================================================================
fig, (ax1, ax2) = new_figure('図4　問1　I点の裏付け（甲土地の面積と登記記録187.18㎡）',
                             '左：H→Eの延長線とA→Bの交点のIで囲むと187.18645 → 187.18㎡。登記記録の187.18㎡と一致。\n'
                             '右：Eの真南にとった誤りのIで囲むと191.65㎡。差4.47㎡は、187㎡の甲2の公差1.19㎡を大きく超える。',
                             ncols=2)
zs = []
for ax, pts, ip, s_area, head, col in [(ax1, KOU, I, '187.18㎡', '正しいI（延長線の交点）', RED),
                                        (ax2, KOU_W, Iw, '191.65㎡', 'Eの真南にとった誤りのI', GRAY)]:
    z = Zu(ax, fontsize=14)
    fit(ax, [A, G, F, E, I, Iw, J + P(0, 3)], margin=0.12, pad_aspect=True)
    z.poly(pts, fill=GREEN)
    z.line(E, J + (J - E) * 0.0, color=GRAY, lw=0.8, ls=':', check=False)
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=18, color=col, weight='bold', pad=6)
    z.free_text(centroid(pts), f'甲土地\n{s_area}', fs=18)
    for p, n in [(A, 'A'), (G, 'G'), (F, 'F'), (E, 'E')]:
        z.point(p, 'concrete' if n in 'AG' else 'metal')
        z.point_label(p, n, away=centroid(pts))
    z.point(ip, 'dot', color=col, size=9)
    z.point_label(ip, 'I', away=centroid(pts), color=col)
    zs.append(z)
zs[0].free_text(centroid(KOU), '→ 登記記録と一致', color=RED, fs=15, offsets=((0, -70), (0, -85)))
zs[1].free_text(centroid(KOU_W), '→ 登記記録と4.47㎡違う', color=GRAY, fs=15, offsets=((0, -70), (0, -85)))
ALL_PROBLEMS += save(fig, zs, 'H30_dai21mon_zu04_kou_menseki.png')

# =====================================================================
# 図5：問2 筆界の定義（整理図。固定配置）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図5　問2　筆界の定義（不動産登記法第123条第1号）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
BOXES = [
    (76, '（ア）どの土地の筆界か',
     ['表題登記 がある一筆の土地（所有権の登記がなくても、表題登記があれば筆界はある）', '誤り：所有権の登記'], [0]),
    (53, '（イ）どの土地との境か',
     ['これに 隣接する 他の土地（表題登記がない土地を含む）', ''], [0]),
    (30, '（ウ）いつ決まった境か',
     ['当該一筆の土地が 登記された 時にその境を構成するものとされた二以上の点及びこれらを結ぶ直線',
      '誤り：分筆された（分筆していない土地にも筆界はある）'], [0]),
    (7, '（エ）条文の外の説明：筆界は動かない',
     ['所有者の 意思 によって変更することはできない（空欄の前は「所有者の」）',
      '誤り：合意（「所有者間の合意」なら通る）。K→Jのブロック塀を建てて売っても、筆界はE→Iのまま'], [0]),
]
for y, head, lines, red in BOXES:
    ax.add_patch(FancyBboxPatch((3, y), 94, 18, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=BLACK, lw=1.4))
    ax.text(5, y + 15, head, fontsize=19, weight='bold', va='center')
    for i, s in enumerate(lines):
        if s:
            ax.text(8, y + 9.5 - i * 5.5, s, fontsize=16, va='center', color=RED if i in red else GRAY)
fig.text(0.5, 0.035, '答え：ア 表題登記、イ 隣接する、ウ 登記された、エ 意思。ア〜ウは第123条第1号の文言どおり。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H30_dai21mon_zu05_hikkai_teigi.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図5: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図6：問3 必要な登記（帯E・I・J・Kの一部地目変更と分筆）
# =====================================================================
fig, (ax,) = new_figure('図6　問3　必要な登記（乙土地11番の土地一部地目変更・分筆登記）',
                        '平成30年10月1日、K→Jのブロック塀が完成し、帯E・I・J・Kは駐車場から切り離されて本件建物の敷地（宅地）になった。\n'
                        '地目の変更（法第37条第1項）と、売るための分筆を一の申請情報で申請する（規則第35条第7号）。申請人は登記名義人の丙山次郎。\n'
                        '甲土地は地目も地積も変わらないので表示の登記は要らない。買った土地どうしは当分合筆しない。')
z = Zu(ax, fontsize=14)
fit(ax, [A, G, E, C, B, J, I], margin=0.08, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(II, fill=BLUE)
z.poly(RO, color=RED, lw=0, fill=RED, alpha=0.45, check=False)
z.line(K, J, color=RED, lw=3.0, ls='--')
z.north_arrow()
z.free_text(centroid(KOU), '甲土地（10番1）\n宅地\n→ 表示の登記は不要', fs=15)
z.free_text(centroid(II), '乙土地の残り\n駐車場（雑種地のまま）', fs=15)
z.callout(E + (I - E) * 0.4, '帯E・I・J・K\n雑種地 → 宅地\n（平成30年10月1日）', dirs=(20, 40, 0), color=RED,
          dists=(170, 200, 230))
z.callout(K + (J - K) * 0.8, 'ブロック塀（K→J）', dirs=(-20, -40, 0), color=RED, dists=(90, 120, 150))
for p, n, ref in [(E, 'E', KOU), (I, 'I', KOU), (J, 'J', II), (K, 'K', II)]:
    z.point(p, 'metal' if n in 'EI' else 'concrete')
    z.point_label(p, n, away=centroid(ref))
ALL_PROBLEMS += save(fig, [z], 'H30_dai21mon_zu06_hitsuyou_touki.png')

# =====================================================================
# 図7：問3 公差の判定（数直線）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図7　問3　地積更正は要るか（乙土地　登記記録253㎡）', fontsize=24, weight='bold', y=0.95)
ax = fig.add_axes([0.06, 0.28, 0.88, 0.52])
ax.set_xlim(248.5, 257.5)
ax.set_ylim(-1.2, 2.2)
ax.axis('off')
ax.plot([248.5, 257.5], [0, 0], color=BLACK, lw=1.5)
for v in range(249, 258):
    ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1)
    ax.text(v, -0.3, str(v), ha='center', va='top', fontsize=14)
ax.add_patch(plt.Rectangle((253 - 4.13, 0.9), 2 * 4.13, 0.35, color=GRAY, alpha=0.25))
ax.text(253, 1.42, '乙1の公差 ±4.13㎡（市街地地域では使わない）', ha='center', fontsize=15, color=GRAY)
ax.add_patch(plt.Rectangle((253 - 1.43, 0.15), 2 * 1.43, 0.45, color=BLUE, alpha=0.3))
ax.text(253, 0.72, '甲2の公差 ±1.43㎡（市街地地域）', ha='center', fontsize=15, color=BLUE)
for v, lab, col, dy in [(253.0, '登記記録\n253', BLACK, -0.75), (253.60035, '座標の面積\n253.60035\n（差0.60）', RED, -0.75),
                        (253.03, '分筆後の合計\n253.03', PURPLE, 1.95)]:
    ax.plot([v], [0], 'o', color=col, ms=9, zorder=5)
x_off = {253.0: -0.55, 253.60035: 0.75, 253.03: 0.0}
for v, lab, col, dy in [(253.0, '登記記録\n253', BLACK, -0.75), (253.60035, '座標の面積\n253.60035\n（差0.60）', RED, -0.75),
                        (253.03, '分筆後の合計 253.03（差0.03）', PURPLE, 1.9)]:
    ax.text(v + x_off[v], dy, lab, ha='center', va='center', fontsize=15, color=col)
fig.text(0.5, 0.08, '市街地地域（規則第10条第2項第1号）なので精度区分は甲2まで（同条第4項第1号）。差0.60㎡も、分筆後の合計との差0.03㎡も1.43㎡の範囲内。\n'
         '→ 地積更正の登記は要らない（準則第72条第1項）。「乙土地」「雑種地」という名前につられて乙1で比べない。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'H30_dai21mon_zu07_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図7: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図8：問3 分筆後の区画と地番
# =====================================================================
fig, (ax,) = new_figure('図8　問3　分筆後の区画と地番（11番 → （イ）11番1 ＋ （ロ）11番2）',
                        '支号のない11番を分筆するので、元の土地も11番1に変わる（準則第67条第1項第4号本文）。（イ）の原因は「①③11番1、11番2に分筆」。\n'
                        '（イ）11番1（雑種地）：244.561 → 1㎡未満を切り捨てて244㎡。（ロ）11番2（宅地）：9.03935 → 9.03㎡。\n'
                        '切り捨て前の合計 244.561 ＋ 9.03935 ＝ 253.60035 で、分筆前の乙土地の座標の面積と一致。')
z = Zu(ax, fontsize=14)
fit(ax, [G, E, C, B, J, I, A + (I - A) * 0.6], margin=0.08, pad_aspect=True)
z.poly(II, fill=BLUE)
z.poly(RO, color=BLACK, lw=1.6, fill=PURPLE, alpha=0.45)
z.north_arrow()
z.free_text(centroid(II), '（イ）11番1\n雑種地\n244㎡', fs=19)
z.callout(E + (I - E) * 0.45, '（ロ）11番2\n宅地\n9.03㎡', dirs=(170, 150, -170), color=PURPLE, dists=(110, 140, 170), fs=16)
for p, n, ref in [(E, 'E', II), (I, 'I', II), (J, 'J', II), (K, 'K', II), (D, 'D', II), (C, 'C', II), (B, 'B', II)]:
    z.point(p, 'metal' if n in 'EIC' else 'concrete')
    z.point_label(p, n, away=centroid(ref) if n not in 'EI' else p + P(0, 3))
z.edge_label(K, C, '10番3', centroid(II), fs=15, color=GRAY, dists=(30, 40), rotate=False)
z.edge_label(C, B, '道路', centroid(II), fs=15, color=GRAY, dists=(30, 40), rotate=False)
z.edge_label(B, J, '道路', centroid(II), fs=15, color=GRAY, dists=(30, 40), rotate=False)
z.free_text(A + (I - A) * 0.75 + P(4, 0), '10番1（甲土地）', fs=15, color=GRAY)
ALL_PROBLEMS += save(fig, [z], 'H30_dai21mon_zu08_bunpitsu_chiban.png')

# =====================================================================
# 図9：問4 地積測量図（11番1・11番2）の完成見本
# =====================================================================
fig, (ax,) = new_figure('図9　問4　地積測量図（11番1・11番2）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm（乙土地は東西約90mm・南北約54mm、T4まで入れて東西約94mm・南北約67mm）。\n'
                        'JIは0.8050…で四捨五入の境目なので0.81。座標値・地積・求積方法・測量年月日は書かない（問題文の注5）。T2・T4は位置と点名だけ（問題文の注6）。\n'
                        '地番欄は「11番1、11番2」、土地の所在は「A市B町三丁目」。T1・T3と、乙土地の筆界点でないA・F・G・Hは描かない。')
z = Zu(ax, fontsize=15)
fit(ax, [E, C, B, I, T2, T4, E + P(4, 0)], margin=0.08, pad_aspect=True)
z.poly(OTSU, lw=2.0)
z.line(K, J, lw=2.0)
z.north_arrow()
co = centroid(II)
REF = {'IE': E + P(-5, 3)}
for n, (p, q, s) in SIDES.items():
    if n in ('EK', 'JI'):
        z.free_text((p + q) / 2, s, fs=15, offsets=((-8, 26), (8, 28), (-20, 22)) if n == 'EK' else ((10, -26), (-8, -28), (20, -22)))
    elif n == 'KJ':
        z.edge_label(p, q, s, co, fs=15, outward=False)
    elif n == 'IE':
        z.edge_label(p, q, s, REF['IE'], fs=15, dists=(18, 26, 34))
    else:
        z.edge_label(p, q, s, co, fs=15)
z.free_text(co, '（イ）\n11－1', fs=17)
z.callout(E + (I - E) * 0.5, '（ロ）11－2', dirs=(180, 160, -160), color=BLACK, dists=(70, 90, 110))
for p, n in [(B, 'B'), (D, 'D'), (J, 'J'), (K, 'K')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=co if n != 'J' else J + P(-2, -2))
for p, n in [(C, 'C'), (E, 'E'), (I, 'I')]:
    z.point(p, 'metal', size=9)
    z.point_label(p, n, away=co if n == 'C' else p + P(0, 3))
for p, n in [(T2, 'T2'), (T4, 'T4')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co, dists=(18, 24, 30))
z.edge_label(K, C, '10－3', co, fs=15, dists=(40, 50), rotate=False)
z.free_text(E, '10－2', fs=15, offsets=((-45, 40), (-60, 30), (-60, 50)))
z.edge_label(I, E, '10－1', co, fs=15, dists=(90, 100), rotate=False)
z.edge_label(C, B, '道路', co, fs=15, dists=(40, 50), rotate=False)
z.edge_label(B, J, '道路', co, fs=15, dists=(46, 56), rotate=False, ts=(0.3, 0.2, 0.4))
z.free_text(P(-18.6, 9.0), '（単位：ｍ）\n◎ コンクリート杭：B・D・J・K\n● 金属標：C・E・I\n△ 基準点：T2・T4', fs=13,
            ha='left', va='bottom', offsets=((0, 0), (0, 30), (-40, 0)))
ALL_PROBLEMS += save(fig, [z], 'H30_dai21mon_zu09_chiseki_sokuryouzu.png')

# =====================================================================
# 図10：問3 別解 帯（四角形）の面積を対角線2本で出す
# =====================================================================
dg = (E - J).conjugate() * (K - I)
assert f'{dg.real:.4f}' == '126.2051' and f'{dg.imag:.4f}' == '18.0787' and f'{abs(dg.imag) / 2:.5f}' == '9.03935'
fig, (ax1, ax2) = new_figure('図10　問3　別解　帯（四角形E・I・J・K）の面積を対角線2本で出す',
                             '四角形の倍面積は、対角線2本の Conjg(E′ − J′) × (K′ − I′) のiの係数だけで出る（4点を順にたどる式と同じ18.0787）。\n'
                             '18.0787 ÷ 2 ＝ 9.03935 → 宅地なので9.03㎡。点を4つたどる式の検算に使う。',
                             ncols=2, width_ratios=[1, 1.4])
za = Zu(ax1, fontsize=14)
fit(ax1, RO + [E + P(0, 3), I + P(0, -3)], margin=0.06, pad_aspect=True)
za.poly(RO, fill=PURPLE)
za.line(E, J, color=RED, lw=2.4, ls='--')
za.line(I, K, color=BLUE, lw=2.4, ls='--')
za.north_arrow(length=0.07)
for p, n in [(E, 'E'), (I, 'I'), (J, 'J'), (K, 'K')]:
    za.point(p, 'metal' if n in 'EI' else 'concrete')
    za.point_label(p, n, away=centroid(RO))
za.callout(E + (J - E) * 0.3, '対角線 E→J', dirs=(180, 160, -160), color=RED, dists=(60, 80, 100))
za.callout(I + (K - I) * 0.3, '対角線 I→K', dirs=(0, 20, -20), color=BLUE, dists=(60, 80, 100))
ax1.set_title('帯E・I・J・K（幅約0.8m）', fontsize=17, weight='bold', pad=6)
ax2.axis('off')
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 100)
for y, txt, col, fs in [(86, '4点を順にたどる式', BLACK, 18),
                        (77, 'E′・Conjg(I′) ＋ I′・Conjg(J′) ＋ J′・Conjg(K′) ＋ K′・Conjg(E′)', BLACK, 14),
                        (69, '表示：128.9305 ＋ 18.0787i', BLACK, 15),
                        (52, '対角線2本の式（別解）', RED, 18),
                        (43, 'Conjg(E′ − J′) × (K′ − I′)', RED, 16),
                        (35, '表示：126.2051 ＋ 18.0787i', RED, 15),
                        (18, 'どちらもiの係数は18.0787（実部は使わない）', BLACK, 15),
                        (9, '18.0787 ÷ 2 ＝ 9.03935 → （ロ）11番2は9.03㎡', BLACK, 15)]:
    ax2.text(4, y, txt, fontsize=fs, color=col, va='center', weight='bold' if fs >= 18 else 'normal')
ALL_PROBLEMS += save(fig, [za], 'H30_dai21mon_zu10_obi_taikakusen.png')

# =====================================================================
# 図11：本番の解く順番（流れ図。固定配置）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図11　本番の解く順番（D点・I点がなくても書ける欄を先に）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
STEPS = [
    ('①', '問2の穴埋め（ア 表題登記・イ 隣接する・ウ 登記された・エ 意思）', '計算なし', GREEN),
    ('②', '申請書の計算の要らない欄（登記の目的・添付書類・登録免許税・申請人・所在・1行目・地番と原因・（ロ）の地目）', '計算なし', GREEN),
    ('③', '原点を（−50720.00, −14880.00）にずらす', '約1分', BLUE),
    ('④', 'D点（T2から放射。K点がE・D線に乗るかで検算）', 'D・Iと裏付けで約10分', BLUE),
    ('⑤', 'I点（H→Eの延長線とA→Bの交点）と甲土地187.18㎡の裏付け', '', BLUE),
    ('⑥', '乙土地・帯・残りの面積と公差の判定（いちばん時間を食う。D・Iがないと始められない）', '約10分', RED),
    ('⑦', '地積測量図の辺長8本と作図', '約15分', PURPLE),
]
for k, (no, txt, tm, col) in enumerate(STEPS):
    y = 88 - k * 13
    ax.add_patch(FancyBboxPatch((3, y - 4.5), 94, 9, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=col, lw=1.8))
    ax.text(5, y, no, fontsize=20, weight='bold', color=col, va='center')
    ax.text(10, y, txt, fontsize=15, va='center')
    if tm:
        ax.text(95, y, tm, fontsize=15, va='center', ha='right', color=col, weight='bold')
    if k < len(STEPS) - 1:
        ax.annotate('', (50, y - 8.3), xytext=(50, y - 5.2), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.6))
fig.text(0.5, 0.045, '①②は座標がなくても書ける。面積の計算で時間が足りなくなっても、問2と申請書の大部分は先に取れている。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'H30_dai21mon_zu11_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図11: 流れ図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
