"""平成30年度 第21問（土地）会話形式note記事の解説図9枚を、座標値から作図する。

`../prompt_H30_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
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
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
T1, T2 = P(-50731.54, -14904.34), P(-50732.19, -14875.11)
T3, T4 = P(-50710.35, -14900.56), P(-50736.86, -14856.95)
A, B, C = P(-50729.15, -14899.00), P(-50733.63, -14859.25), P(-50721.79, -14857.95)
E, F, G = P(-50720.03, -14879.67), P(-50719.93, -14888.41), P(-50719.87, -14897.37)
H, J, K = P(-50710.06, -14878.97), P(-50731.33, -14879.66), P(-50720.07, -14878.87)
D = r2(radial(T2, T1, 13.22, dms(116, 50, 31)))                 # 問1 D点（T2から放射、時計回り）
Dw = r2(radial(T2, T1, 13.22, -dms(116, 50, 31)))               # 反時計回りに測った誤り
I = r2(intersect(H, E, A, B)[0])                                # 問1 I点（H→Eの延長線とA→Bの交点）
Iw = r2(A + (B - A) * ((E.imag - A.imag) / (B.imag - A.imag)))  # Eから真南に下ろした誤り

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('D', D, P(-50720.53, -14868.88)), ('Dw', Dw, P(-50744.12, -14869.40)),
                     ('I', I, P(-50731.24, -14880.46)), ('Iw', Iw, P(-50731.33, -14879.67))]:
    assert abs(got - want) < 1e-9, (n, got, want)
assert f'{abs(Iw - J):.2f}' == '0.01' and f'{abs(Iw - I):.2f}' == '0.80'
assert f'{Dw.real - T2.real:.2f}' == '-11.93'                   # 誤りのDはT2より11.93m南
assert Dw.real < B.real and D.real > T2.real and D.imag > T2.imag   # 誤りは南、正しいDは北東
assert Iw.imag > I.imag                                         # 誤りのIは正しいIより東（J側）
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'EK': (E, K, '0.80'), 'KD': (K, D, '10.00'), 'DC': (D, C, '11.00'), 'CB': (C, B, '11.91'),
         'BJ': (B, J, '20.54'), 'JI': (J, I, '0.81'), 'IE': (I, E, '11.24'), 'KJ': (K, J, '11.29')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert f'{abs(J - I):.4f}' == '0.8050'
KOU = [A, I, E, F, G]              # 甲土地（10番1）
KOU_W = [A, Iw, E, F, G]           # 誤りのIで囲んだ甲土地
OTSU = [I, B, C, D, E]             # 乙土地（11番）の筆界（KはDEの上）
OTSU_K = [I, J, B, C, D, K, E]     # 乙土地（作図用。J・Kを含む）
I_111 = [J, B, C, D, K]            # （イ）11番1
RO_112 = [I, J, K, E]              # （ロ）11番2
fl = lambda v: f'{chiseki(v):.2f}'  # noqa: E731
assert fl(area(KOU)) == '187.18' and fl(area(KOU_W)) == '191.65'
assert f'{area(OTSU):.4f}' == '253.6177'
assert chiseki(area(I_111), takuchi=False) == 244 and fl(area(I_111)) == '244.56'
assert fl(area(RO_112)) == '9.03'
assert f'{abs(area([E, K, D])):.4f}' == '0.0158'
BRG_T1 = math.degrees(cmath.phase(T1 - T2)) + 360          # T2→T1の方向角（北から時計回り）271.27°
BRG_D = BRG_T1 + 116 + 50 / 60 + 31 / 3600                 # 388.12°（＝28.12°）
BRG_DW = BRG_T1 - (116 + 50 / 60 + 31 / 3600)
assert to_dms(math.radians(BRG_T1)) == '271°16′26.04″' and to_dms(math.radians(BRG_D - 360)) == '28°06′57.04″'
print('数値の照合: すべて一致')

LBL = lambda n, p: f'{n}（{p.real:.2f}, {p.imag:.2f}）'.replace('-', '−')  # noqa: E731


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


ALL_PROBLEMS = []
KINDS = {'A': 'concrete', 'B': 'concrete', 'G': 'concrete', 'J': 'concrete', 'K': 'concrete', 'D': 'concrete',
         'C': 'metal', 'E': 'metal', 'F': 'metal', 'H': 'metal', 'I': 'metal'}


def mark(z, p, n, away, label=True, **kw):
    kind = KINDS.get(n, 'dot')
    if kind == 'metal':
        z.point(p, 'metal', size=9)
    else:
        z.point(p, kind)
    if label:
        z.point_label(p, n, away=away, **kw)


# =====================================================================
# 図1：全体像（北を上にして座標どおりに描き直した調査図素図）
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像（平成30年10月の調査時点）',
                        '甲土地（10番1・宅地187.18㎡）と乙土地（11番・雑種地253㎡）は、どちらも丙山次郎の所有。\n'
                        '橙の細い部分（E・I・J・K）を甲土地と一緒に山田太郎へ売り、K→Jの線上にブロック塀（10月1日完了）。')
z = Zu(ax)
fit(ax, [T1, T2, T3, T4, H, B, C, G], margin=0.06, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(OTSU_K, fill=BLUE)
z.poly(RO_112, fill=ORANGE, alpha=0.6, lw=1.2)
z.line(E, H, lw=2.0)
z.line(K, J, color=RED, lw=3.0, ls='--')
z.north_arrow()
ck, co = centroid(KOU), centroid(I_111)
z.free_text(ck, '甲土地\n10番1　宅地\n187.18㎡', fs=16)
z.free_text(co, '乙土地\n11番　雑種地\n253㎡（駐車場）', fs=16)
for n, p, ref in [('A', A, ck), ('G', G, ck), ('F', F, ck), ('H', H, ck), ('B', B, co), ('C', C, co), ('D', D, co)]:
    mark(z, p, n, ref)
for n, p in [('E', E), ('K', K), ('I', I), ('J', J)]:
    mark(z, p, n, None, label=False)
z.callout(E, 'E', dirs=(135, 150, 120), dists=(40, 55, 70))
z.callout(K, 'K', dirs=(45, 30, 60), dists=(40, 55, 70))
z.callout(I, 'I', dirs=(-135, -150, -120), dists=(40, 55, 70))
z.callout(J, 'J', dirs=(-45, -30, -60), dists=(40, 55, 70))
z.callout(K + (J - K) * 0.55, '売った細い部分\n（E・I・J・K）\nK→Jにブロック塀', dirs=(10, -10, 25), color=RED, dists=(80, 110, 140))
for p, n in [(T1, 'T1'), (T2, 'T2'), (T3, 'T3'), (T4, 'T4')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=ck)
z.edge_label(G, F, '10－2', ck, fs=15, dists=(26, 36), rotate=False)
z.edge_label(K, D, '10－3', co, fs=15, dists=(26, 36), rotate=False, ts=(0.3, 0.5, 0.2))
z.edge_label(A, I, '道路', ck, fs=15, dists=(34, 44), rotate=False, ts=(0.5, 0.3))
z.edge_label(J, B, '道路', co, fs=15, dists=(34, 44), rotate=False, ts=(0.4, 0.6))
z.edge_label(C, B, '道路', co, fs=15, dists=(30, 40), rotate=False)
z.edge_label(G, A, '道路', ck, fs=15, dists=(30, 40), rotate=False)
ALL_PROBLEMS += save(fig, [z], 'H30_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：問1 D点（T2から放射）
# =====================================================================
fig, (ax,) = new_figure('図2　問1　D点の求め方（T2から放射）',
                        'T2→T1の方向角 271°16′26.04″（電卓の表示は −88°43′33.96″）に、時計回りの観測角 116°50′31″ を足し（28°06′57.04″）、13.22m 進む。\n'
                        '反時計回りに測ると、T2より11.93m南の道路の向こう側に出てしまう。\n'
                        '検算：K点が直線DEの上にある（三角形EKDの面積 0.0158㎡）。')
z = Zu(ax)
fit(ax, [T1, T2, D, Dw, E, C, B], margin=0.05, pad_aspect=True)
z.poly(KOU, color=GRAY, lw=1.1)
z.poly(OTSU_K, color=GRAY, lw=1.1)
z.line(T2, T2 + 4.0, color=GRAY, lw=1.2, ls='--')
z.free_text(T2 + 4.0, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(T2, T1, color=BLUE, lw=2.0)
z.line(T2, D, color=RED, lw=2.6)
z.line(T2, Dw, color=GRAY, lw=1.4, ls=':')
z.line(E, D, color=RED, lw=1.0, ls='--')
z.north_arrow()
z.angle_arc(T2, 2.0, 0, BRG_T1, color=BLUE)
z.angle_arc(T2, 3.2, BRG_T1, BRG_D, color=RED)
for p, kind in [(T1, 'kijun'), (T2, 'kijun'), (D, 'concrete'), (K, 'concrete')]:
    z.point(p, kind)
z.point(E, 'metal', size=9)
z.point(Dw, 'dot', color=GRAY)
z.point_label(E, 'E', away=centroid(I_111))
z.point_label(K, 'K', away=centroid(I_111))
z.edge_label(T2, T1, '後視（T1の方向）', T2 + P(5, 0), color=BLUE, fs=14, ts=(0.55, 0.65, 0.45), dists=(16, 22))
z.edge_label(T2, D, '13.22', T2 + P(0, 8), color=RED, fs=17, ts=(0.62, 0.7, 0.55, 0.8), dists=(14, 20, 26))
z.callout(T2 + P(-1.0, -1.7), '方向角 271°16′26.04″\n（北から時計回りにT1の方向）', dirs=(-120, -140, -100, -160), color=BLUE,
          dists=(80, 110, 140))
z.callout(T2 + P(1.7, 2.7), '観測角 116°50′31″\n（T1の方向から時計回り）', dirs=(60, 40, 80, 20), color=RED,
          dists=(70, 95, 120))
z.callout(D, LBL('D', D), dirs=(60, 80, 40, 100), color=RED)
z.callout(Dw, '反時計回りに測った誤り\n' + LBL('', Dw).lstrip(), dirs=(0, 20, -20, 160), color=GRAY)
z.callout(T2, LBL('T2', T2), dirs=(-30, -10, -50), color=BLACK, dists=(80, 110, 140))
z.callout(T1, LBL('T1', T1), dirs=(-60, -90, -120), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'H30_dai21mon_zu02_D_housha.png')

# =====================================================================
# 図3：問1 I点（H→Eの延長線とA→Bの交点）
# =====================================================================
fig, (ax1, ax2) = new_figure('図3　問1　I点の求め方（H→Eの延長線とA→Bの交点）',
                             'E − H ＝ −9.97 − 0.70i。H→Eは真南ではなく、南へ9.97m進む間に西へ0.70m傾いている。I ＝ H ＋ (E − H) × 2.1243…（t が1を超えるので延長線上）。\n'
                             'Eから真南（Y座標をEと同じ −14879.67）に下ろすと（−50731.33, −14879.67）で、J点とわずか0.01m、正しいIとは0.80mずれる（右の拡大）。',
                             ncols=2, width_ratios=[1.35, 1])
z1 = Zu(ax1)
fit(ax1, [H, E, I, A, B, G, T2], margin=0.06, pad_aspect=True)
z1.poly(KOU, color=GRAY, lw=1.1)
z1.poly(OTSU_K, color=GRAY, lw=1.1)
z1.line(H, E, color=BLUE, lw=2.4)
z1.line(E, I, color=RED, lw=2.4, ls='--')
z1.line(A, B, color=BLACK, lw=2.4)
z1.north_arrow()
z1.point(H, 'metal', size=9)
z1.point(E, 'metal', size=9)
z1.point(I, 'dot', color=RED, size=9)
z1.point(A, 'concrete')
z1.point(B, 'concrete')
for p, n in [(H, 'H'), (E, 'E'), (A, 'A'), (B, 'B')]:
    z1.point_label(p, n, away=centroid(KOU) if n in 'AE' else centroid(I_111))
z1.callout(H + (E - H) * 0.5, 'H→E（t＝0〜1）', dirs=(180, 200, 160), color=BLUE, dists=(50, 70, 90))
z1.callout(E + (I - E) * 0.45, '延長線（t＝1〜2.1243…）', dirs=(0, 15, -15), color=RED, dists=(60, 80, 100))
z1.callout(I, LBL('I', I), dirs=(-120, -100, -140, -80), color=RED, dists=(55, 75, 95))
z1.free_text(centroid(KOU), '甲土地', color=GRAY, fs=16, offsets=((-60, 0), (-90, 10), (-60, 30)))
z1.free_text(centroid(I_111), '乙土地', color=GRAY, fs=16, offsets=((120, 60), (150, 40), (120, 90)))
# 右：拡大（I・J・誤りのIのまわり 約2.4m四方）
z2 = Zu(ax2)
cz = (I + J) / 2
fit(ax2, [cz + P(1.2, -1.2), cz + P(-1.2, 2.4)], margin=0.0, pad_aspect=True)
tI = (I.imag - A.imag) / (B.imag - A.imag)
z2.line(A + (B - A) * (tI - 0.04), A + (B - A) * (tI + 0.06), color=BLACK, lw=2.4)
z2.line(E + (I - E) * 0.88, I, color=RED, lw=2.4, ls='--')
z2.line(E + (Iw - E) * 0.88, Iw, color=GRAY, lw=1.6, ls=':')
z2.north_arrow()
z2.point(I, 'dot', color=RED, size=11)
z2.point(J, 'concrete')
z2.point(Iw, 'dot', color=GRAY, size=5)
z2.callout(I, LBL('I', I), dirs=(-100, -80, -120, -60), color=RED, dists=(60, 80, 100, 130))
z2.callout(J, LBL('J', J), dirs=(-60, -75, -45), color=BLACK, dists=(70, 95, 120))
z2.callout(Iw, '真南に下ろした誤り\n' + LBL('', Iw).lstrip() + '\nJとの差 0.01m', dirs=(35, 20, 50, 60), color=GRAY,
           dists=(70, 95, 120))
z2.edge_label(I, Iw, '0.80', I + P(-1, 0), color=GRAY, fs=15, rotate=False, dists=(16, 24, 32))
z2.free_text(cz + P(-0.7, 0.3), '道路', color=GRAY, fs=15, offsets=((0, 0), (40, 0), (-40, 0)))
z2.free_text(cz + P(0.7, -0.6), '甲土地', color=GRAY, fs=15, offsets=((0, 0), (0, 20), (-20, 0)))
z2.free_text(cz + P(0.7, 0.9), '乙土地', color=GRAY, fs=15, offsets=((0, 0), (0, 20), (20, 0)))
ALL_PROBLEMS += save(fig, [z1, z2], 'H30_dai21mon_zu03_I_kouten.png')

# =====================================================================
# 図4：問1 甲土地の面積でI点を裏付ける
# =====================================================================
fig, (ax1, ax2) = new_figure('図4　問1　甲土地の面積でI点を裏付ける',
                             '左：正しいI点で甲土地A→I→E→F→Gを計算すると187.18645㎡→187.18㎡で、登記記録の187.18㎡と一致する。\n'
                             '右：Eから真南に下ろした誤りのIでは191.65㎡。登記記録より4.47㎡大きく、187㎡の公差1.19㎡（甲2）を超える。',
                             ncols=2)
zs = []
for ax, pts, ip, s, head, col in [(ax1, KOU, I, '187.18㎡', '正しいI（H→Eの延長線）', RED),
                                  (ax2, KOU_W, Iw, '191.65㎡', 'Eから真南に下ろした誤りのI', GRAY)]:
    z = Zu(ax)
    fit(ax, [A, G, F, E, I, Iw, T2], margin=0.10, pad_aspect=True)
    z.poly(pts, fill=GREEN if col == RED else ORANGE)
    z.line(E, ip, color=col, lw=3.0)
    z.north_arrow()
    z.free_text(centroid(pts), f'甲土地\n{s}', fs=20, color=BLACK)
    for n, p in [('A', A), ('E', E), ('F', F), ('G', G)]:
        mark(z, p, n, centroid(pts))
    z.point(ip, 'dot', color=col, size=10)
    z.point_label(ip, 'I', away=centroid(pts), color=col)
    z.free_text(centroid(pts), head, color=col, fs=16, offsets=((0, 150), (0, 170), (0, -150)))
    z.free_text(centroid(pts), '登記記録 187.18㎡', color=BLACK, fs=15, offsets=((0, -130), (0, -150), (0, 190)))
    zs.append(z)
ALL_PROBLEMS += save(fig, zs, 'H30_dai21mon_zu04_kou_menseki.png')


def frame(title, caption):
    setup_font()
    fig = plt.figure(figsize=(16, 12), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.text(0.5, 0.04, caption, ha='center', va='center', fontsize=15)
    return fig, ax


def box(ax, x, y, w, h, fc='#f7f7f7', ec=BLACK):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.6', fc=fc, ec=ec, lw=1.4))


def arrow(ax, p, q, color=BLACK):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=22, lw=2.0, color=color))


# =====================================================================
# 図5：問2 筆界の定義（整理図。固定配置）
# =====================================================================
fig, ax = frame('図5　問2　筆界の定義（不動産登記法第123条第1号）',
                '（ア）〜（ウ）は条文どおり。（エ）は条文の外の説明で、筆界は所有者どうしが合意しても動かない（動かせるのは所有権界）。')
ROWS = [
    (78, '（ア）', '表題登記', 'がある一筆の土地', '所有権の登記　ではない（表題部所有者だけの土地にも筆界はある）'),
    (56, '（イ）', '隣接する', '他の土地との間において', '「これに隣接する他の土地（表題登記がない土地を含む。）」'),
    (34, '（ウ）', '登記された', '時にその境を構成するものとされた二以上の点及び直線', '分筆された　だけではない（分筆で新しく引いた境は分筆の登記の時、もとからの境は最初に登記された時）'),
    (12, '（エ）', '合意', 'によって変更することはできない（所有者の）', '筆界は公の線。所有者が決められるのは所有権界（今回の売買）'),
]
for y, key, ans, rest, note in ROWS:
    box(ax, 3, y, 94, 16)
    ax.text(5, y + 11.5, key, fontsize=20, weight='bold', va='center')
    ax.text(13, y + 11.5, ans, fontsize=22, weight='bold', va='center', color=RED)
    ax.text(31, y + 11.5, rest, fontsize=18, va='center')
    ax.text(13, y + 4.0, note, fontsize=16, va='center', color=GRAY)
path = os.path.join(OUT, 'H30_dai21mon_zu05_hikkai_teigi.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図5: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図6：問3 必要な登記の判断（整理図。固定配置）
# =====================================================================
fig, ax = frame('図6　問3　乙土地に必要な登記は「土地一部地目変更・分筆登記」',
                '申請人は乙土地の登記名義人の丙山次郎（不動産登記法第37条第1項・第39条第1項）。一の申請情報で申請できる（不動産登記規則第35条第7号）。')
box(ax, 3, 76, 44, 16)
ax.text(5, 88, '平成30年1月ごろ　売買契約', fontsize=19, weight='bold', va='center')
ax.text(5, 81, '甲土地の全部＋乙土地の一部（E・I・J・K）', fontsize=16, va='center')
box(ax, 53, 76, 44, 16)
ax.text(55, 88, '平成30年10月1日　工事完了', fontsize=19, weight='bold', va='center')
ax.text(55, 81, 'K→Jにブロック塀／建物の増築（甲土地の中）', fontsize=16, va='center')
box(ax, 3, 48, 44, 18, fc='#eef4ff', ec=BLUE)
ax.text(5, 61, '一部を売る → 分筆が必要', fontsize=19, weight='bold', va='center', color=BLUE)
ax.text(5, 54, '所有権の移転の登記の前提', fontsize=16, va='center')
ax.text(5, 50, '（合筆は「当分の間はしない」）', fontsize=15, va='center', color=GRAY)
box(ax, 53, 48, 44, 18, fc='#fff1e6', ec=ORANGE)
ax.text(55, 61, '細い部分が家の敷地に → 宅地', fontsize=19, weight='bold', va='center', color=ORANGE)
ax.text(55, 54, '雑種地（駐車場）から宅地へ（準則第68条第3号）', fontsize=15, va='center')
ax.text(55, 50, '1月以内に申請しなければならない（法第37条第1項）', fontsize=15, va='center')
arrow(ax, (25, 75), (25, 67.5))
arrow(ax, (75, 75), (75, 67.5), color=ORANGE)
box(ax, 13, 22, 74, 16, fc='#ffecec', ec=RED)
ax.text(50, 33, '土地一部地目変更・分筆登記（1件）', fontsize=24, weight='bold', va='center', ha='center', color=RED)
ax.text(50, 26, '日付は平成30年10月1日（契約の1月ではない）　登録免許税 金2,000円', fontsize=17, va='center', ha='center')
arrow(ax, (25, 47), (40, 39))
arrow(ax, (75, 47), (60, 39), color=ORANGE)
box(ax, 3, 3, 94, 10)
ax.text(5, 8, '対象外：増築は建物の表題部の変更の登記（法第51条第1項。申請人は山田太郎）。問3は乙土地の申請書だけ', fontsize=16,
        va='center', color=GRAY)
path = os.path.join(OUT, 'H30_dai21mon_zu06_hitsuyou_touki.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図6: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図7：問3 地積更正の要否（数直線の判定図）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図7　問3　地積更正の要否（市街地地域なので精度区分は甲2）', fontsize=24, weight='bold', y=0.95)
ax = fig.add_axes([0.05, 0.16, 0.90, 0.68])
ax.set_xlim(248.0, 258.0)
ax.set_ylim(0, 10)
ax.axis('off')
ax.plot([248.3, 257.7], [5, 5], color=BLACK, lw=2)
for v in range(249, 258):
    ax.plot([v, v], [4.8, 5.2], color=BLACK, lw=1.2)
    ax.text(v, 4.3, str(v), ha='center', va='top', fontsize=14)
ax.axvspan(253 - 4.13, 253 + 4.13, ymin=0.47, ymax=0.53, color=GRAY, alpha=0.25)
ax.axvspan(253 - 1.43, 253 + 1.43, ymin=0.44, ymax=0.56, color=BLUE, alpha=0.35)
ax.text(253, 8.9, '甲2の公差 ±1.43㎡（251.57〜254.43）', ha='center', fontsize=17, color=BLUE, weight='bold')
ax.text(249.2, 6.0, '乙1 ±4.13㎡は使わない', ha='left', fontsize=14, color=GRAY)
ax.plot([253, 253], [5.0, 7.3], color=BLACK, lw=2.4)
ax.text(253, 7.5, '登記記録 253㎡', ha='center', fontsize=17, weight='bold')
for v, lab, y, col in [(253.6177, '実測（分筆前）253.6177㎡\n差 0.6177㎡', 2.0, RED),
                       (253.03, '分筆後の合計 244＋9.03＝253.03㎡\n差 0.03㎡', 2.0, PURPLE)]:
    ax.plot(v, 5, 'o', ms=12, color=col, zorder=5)
    ax.annotate('', (v, 5.3), xytext=(253, 5.3), arrowprops=dict(arrowstyle='<->', color=col, lw=1.6))
ax.text(254.2, 2.2, '実測（分筆前）253.6177㎡　差 0.6177㎡', ha='left', va='center', fontsize=15, color=RED)
ax.annotate('', (253.6177, 4.6), xytext=(254.15, 2.4), arrowprops=dict(arrowstyle='-', color=RED, lw=1))
ax.text(251.9, 2.2, '分筆後の合計 244＋9.03＝253.03㎡　差 0.03㎡', ha='right', va='center', fontsize=15, color=PURPLE)
ax.annotate('', (253.03, 4.6), xytext=(251.95, 2.4), arrowprops=dict(arrowstyle='-', color=PURPLE, lw=1))
fig.text(0.5, 0.05, 'どちらの差も1.43㎡の範囲に収まるので、地積更正の登記は要らない（不動産登記事務取扱手続準則第72条第1項）。\n'
         '「乙土地」という呼び名や雑種地という地目で精度区分を選ばない（不動産登記規則第10条第4項第1号）。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'H30_dai21mon_zu07_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図7: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図8：問3 分筆後の区画と地番
# =====================================================================
fig, (ax1, ax2) = new_figure('図8　問3　分筆後の区画と地番（11番 → 11番1・11番2）',
                             '支号のない本番（11番）を分筆すると、元の土地も含めて支号が付く（準則第67条第1項第4号）。\n'
                             '元の土地の地番も変わるので、（イ）の行の原因は「①③11番1、11番2に分筆」。\n'
                             '（イ）11番1は雑種地のまま（1㎡未満切捨て 244.561→244）、（ロ）11番2は宅地（9.03935→9.03）。',
                             ncols=2, width_ratios=[1.6, 1])
z1 = Zu(ax1)
fit(ax1, OTSU_K + [H + (E - H) * 0.5, E + P(0, -6)], margin=0.10, pad_aspect=True)
z1.poly(I_111, fill=BLUE)
z1.poly(RO_112, fill=ORANGE, alpha=0.6)
z1.north_arrow()
z1.free_text(centroid(I_111), '（イ）11番1\n雑種地　244㎡', fs=19)
for n, p in [('B', B), ('C', C), ('D', D)]:
    mark(z1, p, n, centroid(I_111))
for n, p in [('E', E), ('K', K), ('I', I), ('J', J)]:
    mark(z1, p, n, None, label=False)
z1.callout(K + (J - K) * 0.5, '（ロ）11番2\n宅地　9.03㎡', dirs=(160, 180, 140, 200), color=ORANGE, dists=(80, 105, 130))
z1.edge_label(K, D, '10－3', centroid(I_111), fs=15, color=GRAY, dists=(26, 36), rotate=False)
z1.edge_label(J, B, '道路', centroid(I_111), fs=15, color=GRAY, dists=(26, 36), rotate=False)
z1.edge_label(C, B, '道路', centroid(I_111), fs=15, color=GRAY, dists=(30, 40), rotate=False)
z2 = Zu(ax2)
fit(ax2, RO_112, margin=0.08, pad_aspect=True)
z2.poly(RO_112, fill=ORANGE, alpha=0.6)
z2.line(K, K + (D - K) * 0.08, lw=2.0)
z2.line(J, J + (B - J) * 0.03, lw=2.0)
z2.north_arrow()
z2.callout(centroid(RO_112), '（ロ）11番2\n宅地　9.03㎡', dirs=(0, 15, -15), color=ORANGE, dists=(60, 80, 100))
for n, p in [('E', E), ('K', K), ('I', I), ('J', J)]:
    mark(z2, p, n, centroid(RO_112))
z2.edge_label(I, E, '10－1（甲土地）', centroid(RO_112), fs=14, color=GRAY, dists=(55, 70), rotate=False)
z2.edge_label(K, J, '（イ）11番1', centroid(RO_112), fs=14, color=GRAY, dists=(55, 70), rotate=False, ts=(0.25, 0.2, 0.75))
ALL_PROBLEMS += save(fig, [z1, z2], 'H30_dai21mon_zu08_bunpitsu_chiban.png')

# =====================================================================
# 図9：問4 地積測量図（11番1・11番2）の完成見本
# =====================================================================
fig, (ax,) = new_figure('図9　問4　地積測量図（11番1・11番2）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm（横約90mm・縦約54mm。（ロ）の幅は約3mm）。辺長は小数第3位を四捨五入（JI は 0.8050… なので 0.81）。\n'
                        '座標値・地積・求積方法・測量年月日は書かない（注5）。基準点T2・T4は位置と点名だけ（注6）。')
z = Zu(ax)
fit(ax, OTSU_K + [T2, T4], margin=0.10, pad_aspect=True)
z.poly(OTSU_K, lw=2.0)
z.line(K, J, lw=2.0)
z.north_arrow()
co = centroid(I_111)
for n in ['KD', 'DC', 'CB', 'BJ']:
    p, q, s = SIDES[n]
    z.edge_label(p, q, s, co, fs=16)
z.edge_label(I, E, SIDES['IE'][2], co, fs=16, dists=(12, 18, 24))
z.edge_label(K, J, SIDES['KJ'][2], centroid(RO_112), fs=16, dists=(12, 18, 24))
z.free_text(E + (K - E) * 0.5, SIDES['EK'][2], fs=16, offsets=((0, 26), (-8, 30), (8, 30)))
z.free_text(J + (I - J) * 0.5, SIDES['JI'][2], fs=16, offsets=((0, -26), (-8, -30), (8, -30)))
z.free_text(co, '（イ）11－1', fs=18)
z.callout(K + (J - K) * 0.62, '（ロ）11－2', dirs=(0, 10, -10), dists=(60, 80, 100))
for n, p in [('B', B), ('C', C), ('D', D)]:
    mark(z, p, n, co)
for n, p, d in [('E', E, (135, 150, 120)), ('K', K, (60, 45, 75)), ('I', I, (-135, -150, -120)), ('J', J, (-60, -45, -75))]:
    mark(z, p, n, None, label=False)
    z.callout(p, n, dirs=d, dists=(38, 50, 62), fs=15)
for p, n in [(T2, 'T2'), (T4, 'T4')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.edge_label(K, D, '10－3', co, fs=16, dists=(46, 58), rotate=False, ts=(0.5, 0.3, 0.7))
z.free_text(E, '10－2', fs=16, offsets=((-60, 40), (-70, 30), (-50, 55)))
z.edge_label(I, E, '10－1', co, fs=16, dists=(60, 75, 90), rotate=False)
z.edge_label(J, B, '道路', co, fs=16, dists=(44, 56), rotate=False, ts=(0.6, 0.75))
z.edge_label(C, B, '道路', co, fs=16, dists=(44, 56), rotate=False)
z.free_text(P(T4.real + 0.5, I.imag - 0.8), '（単位：ｍ）\n◎ コンクリート杭：B・D・J・K\n● 金属標：C・E・I\n△ 基準点：T2・T4', fs=14,
            ha='left', va='center', offsets=((0, 0), (0, 20), (30, 0)))
ALL_PROBLEMS += save(fig, [z], 'H30_dai21mon_zu09_chiseki_sokuryouzu.png')

print('重なりの合計:', len(ALL_PROBLEMS))
