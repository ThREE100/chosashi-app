"""平成26年度 第21問（土地）会話形式note記事の解説図18枚を、座標値から作図する。

`../prompt_H26_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../H28/Q21/zu/draw_H28_dai21mon_kaisetsuzu.py`。

100番5の北の角G・Fは問題文に座標がない。100番5を描く図だけ、100番5の地積測量図の辺長（GE 10.39・GD 18.64・
GF 19.40・FC 10.00）から作った模式の位置に置き、図の中で「模式」と明記する（計算・検算には一切使わない）。

実行: python3 note-articles-Kijyutsu/H26/Q21/zu/draw_H26_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, dms, to_dms, area, chiseki, fmt_num  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） --------------------------------
T1, T2, T3 = P(256.25, 178.56), P(220.89, 168.32), P(220.72, 208.12)
A, B, C = P(223.42, 172.02), P(223.22, 199.64), P(239.65, 198.66)
B_T2 = cmath.phase(T2 - T3)                                             # T3→T2（−89°45′18.97″）
PP = r2(T3 + cmath.rect(35.36, B_T2 + dms(45, 36, 12)))
PW = r2(T3 + cmath.rect(35.36, B_T2 - dms(45, 36, 12)))                 # 反時計回りの誤り
B_T3 = cmath.phase(T3 - PP)                                             # P→T3（135°50′52.50″）
D = r2(PP + cmath.rect(12.70, B_T3 + dms(340, 52, 49)))
E = r2(PP + cmath.rect(7.70, B_T3 + dms(72, 22, 37)))
EX = PP + cmath.rect(7.70, B_T3 + dms(72, 22, 37))                      # 丸める前のE
B_P = B_T2 + dms(45, 36, 12)                                            # T3→P（−44°09′06.97″。逆向きの誤り）
DW = r2(PP + cmath.rect(12.70, B_P + dms(340, 52, 49)))
EW = r2(PP + cmath.rect(7.70, B_P + dms(72, 22, 37)))
V = r2(E + (A - E) / abs(A - E) * 3.30)
W = r2(C + (B - C) / abs(B - C) * 3.22)
VW_ = r2(A + (E - A) / abs(E - A) * 3.30)                               # Aから測った誤りのV


def _circ(p, r1, q, r2_):
    d = abs(q - p)
    a = (r1 * r1 - r2_ * r2_ + d * d) / (2 * d)
    h = math.sqrt(r1 * r1 - a * a)
    u = (q - p) / d
    return [p + u * a + u * 1j * h, p + u * a - u * 1j * h]


# 100番5の北の角（模式。地積測量図の辺長から。計算には使わない）
G_M = max(_circ(E, 10.39, D, 18.64), key=lambda z: z.real)
F_M = max(_circ(G_M, 19.40, C, 10.00), key=lambda z: z.real)

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('P', PP, P(246.09, 183.49)), ('PW', PW, P(195.56, 183.27)), ('D', D, P(240.38, 194.83)),
                     ('E', E, P(239.31, 179.85)), ('DW', DW, P(251.80, 172.15)), ('EW', EW, P(252.87, 187.13)),
                     ('V', V, P(236.35, 178.39)), ('W', W, P(236.44, 198.85)), ('VW_', VW_, P(226.38, 173.48))]:
    assert abs(got - want) < 1e-9, (n, got, want)
assert to_dms(B_T2) == '−89°45′18.97″' and to_dms(B_T2 + 2 * math.pi) == '270°14′41.03″'
assert to_dms(B_T3) == '135°50′52.50″'
assert to_dms(B_T3 + dms(340, 52, 49) - 2 * math.pi) == '116°43′41.50″'
assert to_dms(B_T3 + dms(72, 22, 37)) == '208°13′29.50″'
assert f'{EX.real:.4f}' == '239.3055'
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'AB': (A, B, '27.62'), 'BW': (B, W, '13.24'), 'WC': (W, C, '3.22'), 'CD': (C, D, '3.90'),
         'DE': (D, E, '15.02'), 'EV': (E, V, '3.30'), 'VA': (V, A, '14.41')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert d2(V, W) == '20.46'
HONKEN = [A, B, C, D, E]
I_ = [A, B, W, V]
RO = [C, D, E, V, W]
N5_M = [G_M, F_M, C, D, E]
assert f'{area(HONKEN):.4f}' == '382.4314'
assert f'{area(I_):.5f}' == '314.47645' and chiseki(area(I_), False) == 314
assert f'{area(RO):.4f}' == '67.9542' and chiseki(area(RO), False) == 67
SANKAKU = (18.64 * 8.37 + 19.40 * 9.25 + 10.00 * 3.78) / 2
assert f'{SANKAKU:.4f}' == '186.6334'
assert f'{SANKAKU + area(RO):.4f}' == '254.5876' and math.floor(SANKAKU + area(RO)) == 254
assert fmt_num(abs(D - E)) == '15.0181…' and fmt_num(abs(C - D)) == '3.8989…'
# 誤りの点の向き
assert PW.real < T2.real - 20                         # 反時計回りのPはT2・T3の線より約25m南
assert DW.real - C.real > 12 and EW.real - C.real > 12   # 逆向きのD・Eは、Cより12m以上北
assert VW_.real < V.real - 9                          # Aから測ったVは、Aのすぐ北（正しいVより約10m南）
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
KIND = {'A': 'concrete', 'C': 'concrete', 'D': 'concrete', 'W': 'concrete', 'B': 'metal', 'E': 'metal', 'V': 'metal'}
PTS = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'V': V, 'W': W}
CT = centroid(HONKEN)

# =====================================================================
# 図1：甲区の持分を1つずつ追う（整理図。固定配置）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図1　甲区の持分を1つずつ追う（今の共有者は3人で3分の1ずつ）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.02, 0.12, 0.96, 0.79])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
LANES = [
    (78, '持分①\n3分の1', [('順位1　昭和46年4月26日贈与', '甲田一郎'), ('順位2　昭和47年7月27日売買', '株式会社丁野不動産'),
                         ('順位3　昭和47年8月7日売買', '丙山三郎'), ('順位4　昭和50年7月26日売買', '甲野明子')],
     ('甲野明子', 'B市L三丁目4番5号')),
    (50, '持分②\n3分の1', [('順位1　昭和46年4月26日贈与', '乙野二郎')], ('乙野二郎', 'B市K町213番地')),
    (22, '持分③\n3分の1', [('順位1の「一部移転」の残り', '山川一郎'), None, None, ('順位5　平成15年1月26日相続', '山川次郎')],
     ('山川次郎', 'K市B町135番地')),
]
XS = [10.5, 28.5, 46.5, 64.5]
BW, BH = 16.5, 15
for y, lab, chain, final in LANES:
    ax.text(4.5, y, lab, fontsize=16, weight='bold', ha='center', va='center')
    last = None
    for x, item in zip(XS, chain):
        if item is None:
            continue
        head, name = item
        ax.add_patch(FancyBboxPatch((x, y - BH / 2), BW, BH, boxstyle='round,pad=0.4', fc='#f7f7f7',
                                    ec=RED if name in ('甲野明子', '乙野二郎', '山川次郎') else GRAY, lw=1.8))
        ax.text(x + BW / 2, y + 3.4, head, fontsize=12.5, ha='center', va='center', color='#444444')
        ax.text(x + BW / 2, y - 2.6, name, fontsize=17, weight='bold', ha='center', va='center')
        if last is not None:
            ax.annotate('', xy=(x - 0.6, y), xytext=(last + BW + 0.6, y), arrowprops=dict(arrowstyle='->', color=BLACK, lw=1.8))
        last = x
    ax.annotate('', xy=(83.2, y), xytext=(last + BW + 0.6, y), arrowprops=dict(arrowstyle='->', color=RED, lw=1.8, ls='--'))
    ax.add_patch(FancyBboxPatch((84, y - BH / 2), 14, BH, boxstyle='round,pad=0.4', fc='white', ec=RED, lw=2.4))
    ax.text(91, y + 3.4, final[1], fontsize=12.5, ha='center', va='center', color='#444444')
    ax.text(91, y - 2.6, final[0], fontsize=17, weight='bold', ha='center', va='center', color=RED)
ax.text(91, 93, '今の共有者', fontsize=18, weight='bold', ha='center', va='center', color=RED)
ax.text(46.5, 33.5, '名前は順位5番で初めて出てくる（受付は平成15年3月11日）', fontsize=13.5, ha='center', va='center', color='#444444')
ax.add_patch(FancyBboxPatch((3, 1.5), 94, 7.5, boxstyle='round,pad=0.4', fc='#f7f7f7', ec=GRAY, lw=1.4))
ax.text(5, 5.2, '（誤り）名前を拾うだけ：甲田一郎・乙野二郎・山川一郎（甲田一郎の持分は順位2番で移り、山川一郎の持分は相続で移っている）',
        fontsize=14.5, va='center', color='#555555')
fig.text(0.5, 0.075, '順位1番は「所有権一部移転」。移転した山川一郎は残りの3分の1を持ち続け、その名前は順位5番で初めて出てくる。',
         ha='center', va='center', fontsize=15.5)
fig.text(0.5, 0.04, '今の共有者は乙野二郎・甲野明子・山川次郎の3人で、3分の1ずつ。この3人が申請人になる。',
         ha='center', va='center', fontsize=15.5)
path = os.path.join(OUT, 'H26_dai21mon_zu01_mochibun.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図1: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図2：全体像
# =====================================================================
fig, (ax,) = new_figure('図2　北を上にして描き直した全体像',
                        '本件土地（100番1）をVWで（イ）と（ロ）に分け、（ロ）を100番5に合筆する。地役権の範囲は（ロ）の部分。\n'
                        'T1からは筆界点が見えないので観測点Pを置き、T3からPを、PからDとEを放射で求める。VはAE上、WはBC上の点。\n'
                        '100番5の北の角G・Fは問題文に座標がないため、地積測量図の辺長から描いた模式（灰色の破線）。')
z = Zu(ax)
fit(ax, [T1, T2, T3, PP] + HONKEN + N5_M + [V, W], margin=0.07, pad_aspect=True)
z.poly(N5_M, color=GRAY, lw=1.4, ls='--', fill=BLUE, alpha=0.10)
z.poly(I_, fill=GREEN)
z.poly(RO, fill=RED, alpha=0.20)
z.line(V, W, color=RED, lw=2.4)
z.line(T3, PP, color=GRAY, lw=1.2, ls=':')
z.line(PP, D, color=GRAY, lw=1.2, ls=':')
z.line(PP, E, color=GRAY, lw=1.2, ls=':')
z.north_arrow()
z.free_text(centroid(I_), '（イ）100番1', fs=17)
z.free_text(centroid(RO), '（ロ）', fs=16, color=RED, offsets=((0, -8), (0, 0), (-30, 0)))
z.free_text(centroid(N5_M), '100番5（模式）\n雑種地　186㎡', fs=14, color=GRAY, offsets=((-110, 10), (-110, -15), (100, 25), (0, 45)))
for n, p in PTS.items():
    z.point(p, KIND[n])
    z.point_label(p, n, away=CT)
for p, n in [(G_M, 'G'), (F_M, 'F')]:
    z.point(p, 'dot', size=5, color=GRAY)
    z.point_label(p, n, away=centroid(N5_M), color=GRAY, fs=13)
for p, n in [(T1, 'T1'), (T2, 'T2'), (T3, 'T3')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=CT)
z.point(PP, 'dot', color=RED, size=9)
z.callout(PP, 'P（観測点）', dirs=(60, 40, 80), color=RED, dists=(55, 75, 95))
z.free_text(C + P(3.5, 4.0), '100－4', fs=14, color=GRAY, offsets=((0, 0), (15, 0), (0, 15)))
z.free_text(C + P(-1.5, 5.0), '102', fs=14, color=GRAY, offsets=((0, 0), (10, 0), (0, -10)))
z.free_text(W + P(-6.0, 5.0), '101', fs=14, color=GRAY, offsets=((0, 0), (10, 0), (0, 10)))
z.edge_label(A, B, '道路', CT, fs=15, color=GRAY, dists=(30, 40), rotate=False, ts=(0.4, 0.3, 0.6))
z.edge_label(A, E, '道路', CT, fs=15, color=GRAY, dists=(30, 40), rotate=False, ts=(0.5, 0.4, 0.6))
ALL_PROBLEMS += save(fig, [z], 'H26_dai21mon_zu02_zentaizu.png')

# =====================================================================
# 図3：問1 P点（T3から放射）
# =====================================================================
BRG_T2 = math.degrees(B_T2) + 360                  # 270°14′41.03″
BRG_P = BRG_T2 + 45 + 36 / 60 + 12 / 3600          # 315°50′53.03″
fig, (ax,) = new_figure('図3　問1　P点の求め方（T3から放射）',
                        'T3→T2の方向角は 270°14′41.03″（電卓の表示は −89°45′18.97″。真数表の270°14′41″の行）。\n'
                        '観測角は右回り（時計回り）なので45°36′12″を足して35.36m進み、P（246.09, 183.49）。\n'
                        '反時計回りに引くと（195.56, 183.27）で、T2とT3を結ぶ線より約25m南（道路の向こう）に出る。')
z = Zu(ax)
fit(ax, [T1, T2, T3, PP, PW, T3 + P(0, 12), T3 + 7] + HONKEN, margin=0.07, pad_aspect=True)
z.poly(HONKEN, color=GRAY, lw=1.2, fill=GREEN, alpha=0.10)
z.line(T3, T2, color=BLUE, lw=2.0)
z.line(T3, PP, color=RED, lw=2.6)
z.line(T3, PW, color=GRAY, lw=1.6, ls='--')
z.line(T3, T3 + 7, color=GRAY, lw=1.2, ls='--')
z.north_arrow()
z.angle_arc(T3, 3.5, 0, BRG_T2, color=BLUE)
z.angle_arc(T3, 6.0, BRG_T2, BRG_P, color=RED)
z.free_text(T3 + 7, '北', color=GRAY, fs=14, offsets=((14, 0), (-14, 0), (0, 12)))
for p, n in [(T1, 'T1'), (T2, 'T2'), (T3, 'T3')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=T3 + P(8, -15) if n != 'T3' else T3 + P(-5, -5))
z.point(PP, 'dot', color=RED, size=10)
z.point(PW, 'dot', color=GRAY, size=9)
z.edge_label(T3, PP, '35.36', T3 + P(0, -30), color=RED, fs=17, ts=(0.6, 0.7, 0.5), dists=(14, 20))
z.callout(PP, 'P（246.09, 183.49）', dirs=(150, 165, 135), color=RED, dists=(60, 80, 100))
z.callout(PW, '反時計回りの誤り\n（195.56, 183.27）', dirs=(170, 150, -170), color=GRAY, dists=(60, 80, 100))
z.callout(T3 + cmath.rect(3.5, math.radians(135)), '方向角 270°14′41.03″\n（北から時計回りにT2の方向）', dirs=(-20, 0, -40),
          color=BLUE, dists=(60, 80, 100))
z.callout(T3 + cmath.rect(6.0, math.radians(293)), '観測角 45°36′12″\n（T2の方向から時計回り）', dirs=(-150, -130, -170),
          color=RED, dists=(90, 120, 150))
z.free_text(centroid(HONKEN), '本件土地', fs=15, color=GRAY, offsets=((-60, 30), (-80, 50), (-40, 60)))
z.free_text((T2 + T3) / 2 + P(-3.5, 0), '道路', fs=15, color=GRAY, offsets=((-120, 0), (-160, 0), (0, -25), (-120, -25)))
ALL_PROBLEMS += save(fig, [z], 'H26_dai21mon_zu03_P_housha.png')


# =====================================================================
# 図4・図5：問2 D点・E点（Pから放射）
# =====================================================================
BRG_T3 = math.degrees(B_T3)                        # 135°50′52.50″


def housha_fig(num, name, Q, QW, dist, ang, ang_txt, brg_q_txt, q_label, qw_label, caption, extra=None,
               ang_at=-60, ang_dirs=(160, 145, 175, 130), p_dirs=(-160, -145, -175, 180), q_dirs=(-90, -110, -70, -130)):
    fig, (ax1, ax2) = new_figure(f'図{num}　問2　{name}点の求め方（Pから放射）', caption, ncols=2, width_ratios=[0.9, 1.1])
    za = Zu(ax1, fontsize=14)
    fit(ax1, [T3, PP, Q, QW, QW + P(6, 0), A + P(-4, 0)] + HONKEN + N5_M, margin=0.08, pad_aspect=True)
    za.poly(N5_M, color=GRAY, lw=1.1, ls='--')
    za.poly(HONKEN, color=GRAY, lw=1.2, fill=GREEN, alpha=0.10)
    za.line(PP, T3, color=BLUE, lw=2.0)
    za.line(PP, Q, color=RED, lw=2.6)
    za.line(PP, QW, color=GRAY, lw=1.6, ls='--')
    za.north_arrow(length=0.07)
    za.point(T3, 'kijun')
    za.point_label(T3, 'T3', away=T3 + P(5, -5))
    za.point(PP, 'dot', color=BLACK, size=8)
    za.point_label(PP, 'P', away=PP + P(-3, 3))
    za.point(Q, 'dot', color=RED, size=9)
    za.point(QW, 'dot', color=GRAY, size=8)
    za.callout(Q, q_label, dirs=(-90, -110, -70, -130), color=RED, dists=(60, 85, 110))
    za.callout(QW, qw_label, dirs=(60, 40, 80, 20), color=GRAY, dists=(40, 60, 80))
    za.edge_label(PP, T3, '後視（T3の方向）', PP + P(0, -20), color=BLUE, fs=14, ts=(0.85, 0.9, 0.8), dists=(14, 20, 26))
    za.free_text(centroid(HONKEN), '本件土地', fs=14, color=GRAY, offsets=((0, -10), (0, -25)))
    ax1.set_title('全体', fontsize=17, weight='bold', pad=6)

    zb = Zu(ax2, fontsize=14)
    lo, hi = PP + P(-10.0, -12.0), PP + P(6.0, 16.0)
    fit(ax2, [lo, hi, V, E, D, C], margin=0.0, pad_aspect=True)
    zb.poly([V, E, D, C], color=GRAY, lw=1.2, closed=False)          # 拡大の範囲に入る筆界だけ（区画は塗らない。端が切れないように）
    zb.line(PP, PP + 5.2, color=GRAY, lw=1.2, ls='--')
    zb.free_text(PP + 5.2, '北', color=GRAY, fs=14, offsets=((14, 0), (-14, 0), (0, 12)))
    tk = PP + (T3 - PP) / abs(T3 - PP) * 5.6
    zb.line(PP, tk, color=BLUE, lw=2.0)
    zb.line(PP, Q, color=RED, lw=2.6)
    zb.north_arrow(length=0.07)
    zb.angle_arc(PP, 1.5, 0, BRG_T3, color=BLUE)
    zb.angle_arc(PP, 2.6, BRG_T3, BRG_T3 + ang, color=RED)
    zb.point(PP, 'dot', color=BLACK, size=9)
    zb.point(Q, 'dot', color=RED, size=10)
    for n in ('C', 'D', 'E', 'V'):
        if PTS[n] is not Q and abs(PTS[n] - PP) < 14:
            zb.point(PTS[n], KIND[n])
            zb.point_label(PTS[n], n, away=CT)
    zb.edge_label(PP, Q, dist, PP + P(0, 20) if Q == E else PP + P(-6, -2), color=RED, fs=17,
                  ts=(0.62, 0.72, 0.52), dists=(14, 20, 26))
    zb.callout(PP + (T3 - PP) / abs(T3 - PP) * 4.6, '後視（T3へ）', dirs=(-115, -130, -100, -145), color=BLUE, dists=(40, 60, 80))
    zb.callout(PP + cmath.rect(1.5, math.radians(BRG_T3 * 0.5)), '方向角 135°50′52.50″\n（北から時計回りにT3の方向）',
               dirs=(30, 15, 45), color=BLUE, dists=(90, 115, 140))
    zb.callout(PP + cmath.rect(2.6, math.radians(BRG_T3 + ang + ang_at)), ang_txt, dirs=ang_dirs, color=RED,
               dists=(60, 85, 110, 135))
    zb.callout(PP, 'P（246.09, 183.49）', dirs=p_dirs, color=BLACK, dists=(110, 135, 160))
    zb.callout(Q, (q_label if extra is None else extra) + '\n' + brg_q_txt, dirs=q_dirs, color=RED,
               dists=(55, 75, 95, 120))
    ax2.set_title('Pのまわりの拡大', fontsize=17, weight='bold', pad=6)
    return fig, [za, zb]


fig, zs = housha_fig(4, 'D', D, DW, '12.70', 340 + 52 / 60 + 49 / 3600,
                     '観測角 340°52′49″\n（T3の方向から時計回り）', 'P→Dの方向角 116°43′41.50″\n（476°43′41.50″ − 360°）',
                     'D（240.38, 194.83）', 'T3→Pの向きで回した誤り\n（251.80, 172.15）',
                     'Pに器械を据えてT3を後視。P→T3の方向角 135°50′52.50″ に340°52′49″を足すと 476°43′41.50″（360°を引いて116°43′41.50″）。\n'
                     '12.70m進んで D（240.38, 194.83）。前の章のT3→Pの向き（−44°09′06.97″）で回すと、DはPをはさんだ反対側の\n'
                     '（251.80, 172.15）で、本件土地の北の角Cより12m以上北に出る。')
ALL_PROBLEMS += save(fig, zs, 'H26_dai21mon_zu04_D_housha.png')

fig, zs = housha_fig(5, 'E', E, EW, '7.70', 72 + 22 / 60 + 37 / 3600,
                     '観測角 72°22′37″\n（T3の方向から時計回り）', 'P→Eの方向角 208°13′29.50″\n（電卓は −151°46′30.50″）',
                     'E（239.31, 179.85）', 'T3→Pの向きで回した誤り\n（252.87, 187.13）',
                     'P→T3の方向角 135°50′52.50″ に72°22′37″を足して 208°13′29.50″（電卓の arg は −151°46′30.50″）。7.70m進んで\n'
                     'E（239.31, 179.85）。表示のX座標 239.3055… は小数第3位が5なので、四捨五入で239.31（239.30にしない）。\n'
                     'T3→Pの向きで回すと（252.87, 187.13）で、Cより12m以上北に出る。',
                     extra='E（239.31, 179.85）　表示 239.3055… → 239.31',
                     ang_at=-15, ang_dirs=(180, 170, 190), p_dirs=(150, 165, 135), q_dirs=(-25, -40, -10))
ALL_PROBLEMS += save(fig, zs, 'H26_dai21mon_zu05_E_housha.png')

# =====================================================================
# 図6：問2 V点（直線AE上、Eから3.30m）
# =====================================================================
fig, (ax,) = new_figure('図6　問2　V点の求め方（直線AEの上で、Eから3.30m）',
                        'V ＝ E ＋ (A − E) ÷ Abs(A − E) × 3.30。出発点はE、向きはEからA（長さ1の矢印を3.30倍）。\n'
                        'V（236.35, 178.39）。「点Aと点Eを結ぶ直線上」につられてAから3.30m測ると（226.38, 173.48）で、\n'
                        'Aのすぐ北（正しいVより約10m南）に出る。VからAまでは14.41。')
z = Zu(ax)
A_B8 = A + (B - A) / abs(B - A) * 8        # ABのうちAから8mまで（図に要る部分だけ描く）
fit(ax, [A, E, D, V, VW_, A_B8, A + P(0, -9)], margin=0.08, pad_aspect=True)
z.poly([A_B8, A, E, D], color=GRAY, lw=1.2, closed=False)
z.line(A, E, color=BLACK, lw=2.4)
z.line(E, V, color=RED, lw=4.0)
z.line(A, VW_, color=GRAY, lw=4.0, ls='--')
z.north_arrow()
for n in ('A', 'E', 'D'):
    z.point(PTS[n], KIND[n])
    z.point_label(PTS[n], n, away=CT)
z.point(V, 'dot', color=RED, size=10)
z.point(VW_, 'dot', color=GRAY, size=9)
z.edge_label(E, V, '3.30', CT, color=RED, fs=17, dists=(14, 20, 26))
z.edge_label(V, A, '14.41', CT, fs=16, dists=(14, 20, 26), ts=(0.5, 0.62, 0.38))
z.callout((A + VW_) / 2, 'Aから3.30（誤り）', dirs=(180, 160, 200), color=GRAY, dists=(60, 80, 100))
z.callout(V, 'V（236.35, 178.39）', dirs=(-10, 10, -30, 20), color=RED, dists=(80, 105, 130))
z.callout(VW_, '誤りのV（226.38, 173.48）', dirs=(10, 30, -10), color=GRAY, dists=(70, 95, 120))
z.free_text(V + P(-4.0, 5.0), '本件土地', fs=15, color=GRAY, offsets=((0, 0), (0, -20), (20, 0)))
z.edge_label(A, E, '道路', CT, fs=15, color=GRAY, dists=(40, 50), rotate=False, ts=(0.35, 0.45))
ALL_PROBLEMS += save(fig, [z], 'H26_dai21mon_zu06_V.png')

# =====================================================================
# 図7：問2 W点（直線BC上、Cから3.22m）
# =====================================================================
fig, (ax,) = new_figure('図7　問2　W点の求め方（直線BCの上で、Cから3.22m）',
                        'W ＝ C ＋ (B − C) ÷ Abs(B − C) × 3.22。出発点はC、向きはCからB。W（236.44, 198.85）。\n'
                        'Cの東は102、Wの東は101。VとWのX座標は236.35と236.44で、分筆線VWは本件土地を北の（ロ）と南の（イ）に分ける。')
z = Zu(ax)
B_A8 = B + (A - B) / abs(A - B) * 8        # BAのうちBから8mまで
D_E6 = D + (E - D) / abs(E - D) * 6        # DEのうちDから6mまで
fit(ax, [B, C, D, W, B_A8, D_E6, B + P(0, 8), C + P(2, 8)], margin=0.08, pad_aspect=True)
z.poly([D_E6, D, C, B, B_A8], color=GRAY, lw=1.2, closed=False)
z.line(B, C, color=BLACK, lw=2.4)
z.line(C, W, color=RED, lw=4.0)
z.north_arrow()
for n in ('B', 'C', 'D'):
    z.point(PTS[n], KIND[n])
    z.point_label(PTS[n], n, away=CT)
z.point(W, 'dot', color=RED, size=10)
z.edge_label(C, W, '3.22', CT, color=RED, fs=17, dists=(14, 20, 26))
z.edge_label(W, B, '13.24', CT, fs=16, dists=(14, 20, 26), ts=(0.5, 0.62, 0.38))
z.callout(W, 'W（236.44, 198.85）', dirs=(-170, 170, -150), color=RED, dists=(90, 115, 140))
z.free_text(C + P(1.2, 4.0), '102', fs=16, color=GRAY, offsets=((0, 0), (0, -15), (10, 0)))
z.free_text(B + P(6.0, 4.5), '101', fs=16, color=GRAY, offsets=((0, 0), (0, 15), (10, 0)))
z.free_text(W + P(-4.0, -5.0), '本件土地', fs=15, color=GRAY, offsets=((0, 0), (0, -20), (-20, 0)))
ALL_PROBLEMS += save(fig, [z], 'H26_dai21mon_zu07_W.png')

# =====================================================================
# 図8：公差の判断（地積。数直線。固定配置）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 8), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図8　公差の判断　村落地だから乙1、地積更正は要らない', fontsize=24, weight='bold', y=0.955)
ax = fig.add_axes([0.05, 0.17, 0.90, 0.66])
ax.set_xlim(372, 388)
ax.set_ylim(0, 10)
ax.axis('off')
S = area(HONKEN)
for y, lab, half, col, ok in [(7.0, '乙1（村落地）', 5.39, GREEN, '範囲内 → 地積更正は要らない'),
                              (2.5, '甲2（誤り）', 1.83, GRAY, '超える → 要らない地積更正を付けてしまう')]:
    ax.add_patch(Rectangle((380 - half, y - 0.6), 2 * half, 1.2, fc=col, alpha=0.25, ec=col))
    ax.plot([372.5, 387.5], [y, y], color=BLACK, lw=1.4)
    ax.plot([380, 380], [y - 1.0, y + 1.0], color=BLACK, lw=2.4)
    ax.plot([S, S], [y - 1.0, y + 1.0], color=RED, lw=2.4)
    ax.text(372.5, y + 1.35, lab + f'　公差 {half:.2f}㎡（{380 - half:.2f}〜{380 + half:.2f}）', fontsize=17, weight='bold',
            color=GREEN if col == GREEN else '#555555')
    ax.text(387.5, y - 1.55, ok, fontsize=16, ha='right', color=RED if col == GREEN else '#555555')
ax.text(380, 0.2, '登記記録 380㎡', fontsize=16, ha='center')
ax.text(S, 9.1, '実測 382.4314㎡（差 2.4314㎡）', fontsize=16, ha='center', color=RED)
fig.text(0.5, 0.075, '精度区分は、市か町かでも表の順番でもなく、地域で決まる（不動産登記規則第77条第5項・第10条第4項）。',
         ha='center', va='center', fontsize=15)
fig.text(0.5, 0.035, '本件土地の周辺地域は村落地なので乙1。表の（オ）の一番上の甲2で比べない。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'H26_dai21mon_zu08_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図8: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図9：100番5の地積測量図の辺長と今回の測量（距離の公差）
# =====================================================================
fig, (ax,) = new_figure('図9　100番5の地積測量図の辺長と今回の測量（距離の公差・乙1）',
                        '100番5の地積測量図の辺長のうち、今回の測量で確かめられるのはEDとDCの2辺（G・Fは測っていない）。\n'
                        '表の（カ）の距離測定の公差（乙1）で比べると、ED 15.02と15.05の差0.03mは15mの35cmの中、DC 3.90と3.89の差0.01mは3mの27cmの中。\n'
                        'だから100番5の地積測量図は今回の測量と合っていて、その三斜の面積186.6334を使える。G・Fの位置は模式。')
z = Zu(ax)
fit(ax, [G_M, F_M, C, D, E, V, W, W + P(0, 9), V + P(0, -6)], margin=0.08, pad_aspect=True)
z.poly(N5_M, color=GRAY, lw=1.4, ls='--', fill=BLUE, alpha=0.12)
z.poly(RO, color=GRAY, lw=1.2, fill=RED, alpha=0.10)
z.line(E, D, color=RED, lw=3.6)
z.line(D, C, color=RED, lw=3.6)
z.north_arrow()
for n in ('C', 'D', 'E', 'V', 'W'):
    z.point(PTS[n], KIND[n])
    z.point_label(PTS[n], n, away=centroid(RO))
for p, n in [(G_M, 'G'), (F_M, 'F')]:
    z.point(p, 'dot', size=5, color=GRAY)
    z.point_label(p, n, away=centroid(N5_M), color=GRAY, fs=13)
z.callout((E + D) / 2, 'ED　今回 15.02（15.0181…）\n地積測量図 15.05　差 0.03m ＜ 35cm', dirs=(95, 80, 110, 70), color=RED,
          dists=(80, 105, 130))
z.callout((D + C) / 2, 'DC　今回 3.90（3.8989…）\n地積測量図 3.89　差 0.01m ＜ 27cm', dirs=(20, 0, 40, -20), color=RED,
          dists=(90, 115, 140))
z.free_text(centroid(N5_M), '100番5（模式）', fs=15, color=GRAY, offsets=((0, 70), (0, 90), (-80, 70)))
z.free_text(centroid(RO), '（ロ）', fs=15, color=GRAY, offsets=((0, -10), (-40, -10), (40, -10)))
z.free_text((G_M + F_M) / 2, 'G・Fは今回は測っていない', fs=14, color=GRAY, offsets=((0, 22), (0, 34)))
ALL_PROBLEMS += save(fig, [z], 'H26_dai21mon_zu09_kyori_kousa.png')

# =====================================================================
# 図10：（イ）（ロ）の面積
# =====================================================================
fig, (ax,) = new_figure('図10　問4の準備　（イ）と（ロ）の面積',
                        '（イ）A→B→W→Vは四角形なので、対角線どうしの Conjg(W − A) × (V − B) のiの係数628.9529が倍面積。314.47645 → 314㎡。\n'
                        '（ロ）C→D→E→V→Wは5点を順に回って 135.9084 ÷ 2 ＝ 67.9542 → 67㎡（雑種地は1㎡未満切捨て）。\n'
                        '切り捨てる前の合計 382.43065 は、本件土地全体の 382.4314 とほぼ同じ（差はV・Wの丸めの分）。')
z = Zu(ax)
fit(ax, HONKEN + [A + P(-2, -6), B + P(0, 6)], margin=0.08, pad_aspect=True)
z.poly(I_, fill=GREEN, alpha=0.25)
z.poly(RO, fill=RED, alpha=0.25)
z.line(A, W, color=GRAY, lw=1.2, ls=':')
z.line(B, V, color=GRAY, lw=1.2, ls=':')
z.north_arrow()
for n, p in PTS.items():
    z.point(p, KIND[n])
    z.point_label(p, n, away=CT)
z.free_text(centroid(I_), '（イ）\n314.47645 → 314㎡', fs=18, offsets=((0, -35), (0, -55), (0, 30)))
z.free_text(centroid(RO), '（ロ）67.9542 → 67㎡', fs=17, color=RED, offsets=((0, 0), (0, -8), (20, 0)))
z.free_text((A + W) / 2 + P(1.0, -2.0), '対角線AW', fs=14, color=GRAY, offsets=((0, 0), (0, 15), (0, -15)))
z.free_text((B + V) / 2 + P(1.0, 2.0), '対角線BV', fs=14, color=GRAY, offsets=((0, 0), (0, 15), (0, -15)))
ALL_PROBLEMS += save(fig, [z], 'H26_dai21mon_zu10_menseki.png')

# =====================================================================
# 図11：100番5の三斜と合筆後の地積（G・Fは模式）
# =====================================================================
def _foot(p, a, b):
    """点pから直線abへの垂線の足"""
    u = (b - a) / abs(b - a)
    return a + u * ((p - a) * u.conjugate()).real


H1, H2, H3 = _foot(E, G_M, D), _foot(D, G_M, F_M), _foot(D, F_M, C)
# 模式のG・Fでも、三斜の高さは地積測量図の値（8.37・9.25・3.78）とほぼ同じになる（位置の確かめ）
assert abs(abs(E - H1) - 8.37) < 0.02 and abs(abs(D - H2) - 9.25) < 0.02 and abs(abs(D - H3) - 3.78) < 0.02
fig, (ax,) = new_figure('図11　合筆後の100番5は254㎡（三斜の186.6334に（ロ）の67.9542を足す）',
                        '100番5の地積測量図は三斜法。①G・E・D（底辺GD 18.64、高さ8.37）、②G・D・F（底辺GF 19.40、高さ9.25）、③D・F・C（底辺FC 10.00、高さ3.78）。\n'
                        '合計186.6334の端数を切り捨てたのが登記記録の186㎡。合筆後の100番5は、切り捨てる前の186.6334に（ロ）の67.9542を足して254.5876 → 254㎡。\n'
                        '186 ＋ 67 ＝ 253 は、捨てた端数の0.6334と0.9542の合計1.5876の分だけ足りない。G・Fの位置は、地積測量図の辺長から描いた模式。')
z = Zu(ax)
BOX_AT = F_M + P(-6.5, 8.5)
fit(ax, [G_M, F_M, C, D, E, V, W, BOX_AT + P(0, 15), V + P(0, -3)], margin=0.07, pad_aspect=True)
z.poly(N5_M, color=BLACK, lw=1.6, ls='--', fill=BLUE, alpha=0.15)
z.poly(RO, color=BLACK, lw=1.6, fill=RED, alpha=0.20)
z.line(G_M, D, color=BLUE, lw=1.4, ls='-.')
z.line(D, F_M, color=BLUE, lw=1.4, ls='-.')
for p, q in [(E, H1), (D, H2), (D, H3)]:
    z.line(p, q, color=PURPLE, lw=1.4, ls=':')
z.right_angle(H1, D, E, size=0.7, color=PURPLE)
z.right_angle(H2, F_M, D, size=0.7, color=PURPLE)
z.right_angle(H3, C, D, size=0.7, color=PURPLE)
z.north_arrow()
for n in ('C', 'D', 'E', 'V', 'W'):
    z.point(PTS[n], KIND[n])
    z.point_label(PTS[n], n, away=centroid(N5_M) if n in ('C', 'D', 'E') else centroid(RO))
for p, n in [(G_M, 'G'), (F_M, 'F')]:
    z.point(p, 'dot', size=6, color=GRAY)
    z.point_label(p, n, away=centroid(N5_M), color=GRAY)
z.edge_label(G_M, D, '18.64', E, color=BLUE, fs=15, ts=(0.38, 0.3, 0.46), dists=(10, 16))
z.edge_label(G_M, F_M, '19.40', D, color=BLUE, fs=15, ts=(0.3, 0.22, 0.4))
z.edge_label(F_M, C, '10.00', G_M, color=BLUE, fs=15)
z.edge_label(E, H1, '8.37', G_M, color=PURPLE, fs=15, ts=(0.5, 0.4, 0.6), dists=(10, 16))
z.edge_label(D, H2, '9.25', F_M, color=PURPLE, fs=15, ts=(0.5, 0.6, 0.4), dists=(10, 16))
z.edge_label(D, H3, '3.78', C, color=PURPLE, fs=15, ts=(0.5, 0.4, 0.6), dists=(10, 16, 22), rotate=False)
z.free_text(centroid([G_M, E, D]), '①', fs=18, color=BLUE, offsets=((-10, -8), (-25, -8), (0, -20)))
z.free_text(centroid([G_M, D, F_M]), '②', fs=18, color=BLUE, offsets=((20, 15), (35, 15), (20, 30)))
z.free_text(centroid([D, F_M, C]), '③', fs=18, color=BLUE, offsets=((8, 10), (8, 25), (-8, 25)))
z.free_text(centroid(RO), '（ロ）67.9542', fs=16, color=RED, offsets=((0, -6), (-40, -6), (40, -6)))
z.free_text(BOX_AT, '① 18.64 × 8.37 ÷ 2 ＝ 78.0084\n② 19.40 × 9.25 ÷ 2 ＝ 89.725\n③ 10.00 × 3.78 ÷ 2 ＝ 18.9\n'
            '合計 186.6334 → 186㎡（登記記録）\n\n合筆後の100番5\n186.6334 ＋ 67.9542 ＝ 254.5876 → 254㎡\n（誤り）186 ＋ 67 ＝ 253',
            fs=15, ha='left', va='top', offsets=((0, 0), (0, 20), (20, 0)),
            bbox=dict(boxstyle='round,pad=0.5', fc='#f7f7f7', ec=BLACK, lw=1.0))
ALL_PROBLEMS += save(fig, [z], 'H26_dai21mon_zu11_gouhitsugo_254.png')


def box_figure(title, h_in, boxes, foot, name, label):
    """角丸の枠を並べる整理図（固定配置）。boxes：(左端, 上端, 幅, 見出し, 色, [(行, 赤か)])。枠の高さは行の数から決める"""
    setup_font()
    fig = plt.figure(figsize=(16, h_in), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=24, weight='bold', y=1 - 0.42 / h_in)
    ax = fig.add_axes([0.03, 0.75 / h_in, 0.94, 1 - 1.55 / h_in])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    u = (h_in - 1.55)          # 1目盛りあたりのピクセル数（縦）
    for x0, top, w, head, col, lines in boxes:
        hh = (85 + 58 * (len(lines) - 1) + 40) / u
        ax.add_patch(FancyBboxPatch((x0, top - hh), w, hh, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=col, lw=2.2))
        ax.text(x0 + 2, top - 30 / u, head, fontsize=18, weight='bold', va='center', color=col)
        for i, (t, red) in enumerate(lines):
            ax.text(x0 + 3.5, top - (85 + 58 * i) / u, t, fontsize=15.5, va='center', color=RED if red else BLACK)
    for i, t in enumerate(foot):
        fig.text(0.5, (0.38 + 0.3 * (len(foot) - 1 - i)) / h_in, t, ha='center', va='center', fontsize=15.5)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print(f'[重なり検査] {label}: 整理図（固定配置）\n  →', path)


# =====================================================================
# 図12：合筆できるか（不動産登記法第41条）と地役権設定の範囲（整理図）
# =====================================================================
box_figure('図12　合筆できるか（不動産登記法第41条）と地役権設定の範囲', 10.6, [
    (2, 97, 96, '不動産登記法第41条（合筆の登記の制限）を、100番1と100番5で1号ずつ確かめる', BLUE, [
        ('第1号　相互に接続していない土地 → CD・DEで接している（当たらない）', False),
        ('第2号　地目又は地番区域が異なる土地 → どちらも雑種地、字C（当たらない）', False),
        ('第3号　所有権の登記名義人が異なる土地 → どちらも乙野二郎・甲野明子・山川次郎（当たらない）', False),
        ('第4号　所有権の登記名義人の持分が異なる土地 → どちらも3分の1ずつ（当たらない）', False),
        ('第5号　所有権の登記がない土地とある土地 → どちらも所有権の登記がある（当たらない）', False),
        ('第6号　所有権の登記以外の権利に関する登記がある土地 → 100番1の乙区1番に地役権設定（要役地102番）', False),
        ('　かっこ書き：合筆後の登記記録に登記できるものとして法務省令で定めるものがある土地を除く', False),
        ('　→ 不動産登記規則第105条第1号「承役地についてする地役権の登記」→ 例外に当たり、合筆できる', True),
    ]),
    (2, 34, 96, '地役権設定の範囲が合筆後の土地の一部になる（不動産登記令別表9の項申請情報欄ロ）', PURPLE, [
        ('（ロ）の部分＝地役権の設定範囲が100番5に入り、合筆後の100番5の一部（南側）になる', False),
        ('申請情報に範囲を書く → 答案用紙の最下欄「地役権設定の範囲　100番5の土地　南側67平方メートル」', True),
        ('（添付情報は同じ別表9の項添付情報欄：地役権者が作成した範囲を証する情報と地役権図面。本問は答案用紙に（略））', False),
    ]),
], ['（誤り）「乙区に地役権があるから合筆できない」。第6号のかっこ書きを読み飛ばさない。',
    '分筆と合筆を一の申請情報で申請するので、登記の目的は土地分合筆登記（不動産登記規則第35条第1号）。'],
    'H26_dai21mon_zu12_gouhitsu_seigen.png', '図12')

# =====================================================================
# 図13：申請人の山川次郎（相続の登記は平成15年に済んでいる。時系列の整理図）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 11), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図13　申請人の山川次郎：相続の登記は平成15年に済んでいる', fontsize=24, weight='bold', y=0.962)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
ax.annotate('', xy=(97, 74), xytext=(3, 74), arrowprops=dict(arrowstyle='->', color=BLACK, lw=2.0))
EVENTS = [(14, '平成15年1月26日', ['山川一郎が死亡', '（相続の開始）'], GRAY),
          (46, '平成15年3月11日', ['相続による持分の移転の登記', '（甲区順位5番、受付第4602号）', '登記名義人は山川次郎に'], BLUE),
          (82, '平成26年8月22日', ['分合筆の申請', '山川次郎が登記名義人', '本人として申請する'], RED)]
for x, d, ls_, col in EVENTS:
    ax.plot([x, x], [71.5, 76.5], color=col, lw=3)
    ax.text(x, 80.5, d, fontsize=18, weight='bold', ha='center', va='center', color=col)
    for i, t in enumerate(ls_):
        ax.text(x, 66 - i * 5.0, t, fontsize=15.5, ha='center', va='center')
for x0, col, head, lines in [
        (2, GREEN, '本問：相続の登記が済んでいる',
         [('山川次郎は所有権の登記名義人本人', False), ('共有者の1人として申請するだけ', False),
          ('→ 相続を証する情報は要らない', True), ('（答案用紙の添付情報も「（略）」と印刷済み）', False)]),
        (51, GRAY, '比べる：登記名義人が亡くなったまま',
         [('相続の登記をせず、相続人が申請するとき', False), ('（不動産登記法第30条の一般承継人による申請）', False),
          ('→ 相続その他の一般承継を証する情報が要る', False), ('（不動産登記令第7条第1項第4号）', False)])]:
    ax.add_patch(FancyBboxPatch((x0, 4), 47, 38, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=col, lw=2.2))
    ax.text(x0 + 2, 37.5, head, fontsize=18, weight='bold', va='center', color=col)
    for i, (t, red) in enumerate(lines):
        ax.text(x0 + 3, 29.5 - i * 7.0, t, fontsize=15.5, va='center', color=RED if red else BLACK)
fig.text(0.5, 0.045, '相続を証する情報が要るかは、相続があったかではなく、申請の時に登記名義人が誰かで決まる。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H26_dai21mon_zu13_souzoku_jikeiretsu.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図13: 時系列の整理図（固定配置）\n  →', path)

# =====================================================================
# 図14：登録免許税は分合筆1件で金2,000円（整理図）
# =====================================================================
box_figure('図14　登録免許税は分合筆1件で金2,000円', 5.6, [
    (2, 96, 47, '1件の分合筆（不動産登記規則第35条第1号）', GREEN, [
        ('分合筆後の土地', False), ('（イ）100番1と合筆後の100番5', False), ('2個 × 1,000円', False),
        ('＝ 金2,000円', True),
    ]),
    (51, 96, 47, '分筆と合筆を別々に2件で申請すると', GRAY, [
        ('① 分筆：分筆後の2個（100番1と（ロ）の新しい土地）', False), ('　2個 × 1,000円 ＝ 2,000円', False),
        ('② 合筆：合筆後の1個（100番5）', False), ('　1個 × 1,000円 ＝ 1,000円', False),
        ('合計 3,000円（1,000円多い）', False),
    ]),
], ['登録免許税法別表第一の一の（十三）イ（分筆）・ロ（合筆）：分筆後・合筆後の土地の個数1個につき1,000円。',
    '（ロ）は100番1から切り離してすぐ100番5に入る部分で、それだけの登記記録は作られない。'],
    'H26_dai21mon_zu14_menkyozei.png', '図14')

# =====================================================================
# 図15：分合筆の前と後
# =====================================================================
fig, (ax1, ax2) = new_figure('図15　問4　分合筆の前と後（合筆後の100番5は254㎡）',
                             '左：申請前。100番1は登記記録380㎡、100番5は186㎡（地積測量図の三斜の面積186.6334）。（ロ）部分（67.9542）を100番5へ移す。\n'
                             '右：分合筆後。（イ）100番1は座標の314.47645 → 314㎡。100番5は 186.6334 ＋ 67.9542 ＝ 254.5876 → 254㎡\n'
                             '（186 ＋ 67 ＝ 253 は誤り）。地役権の範囲は100番5の南側（67平方メートル）。G・Fの位置は模式。',
                             ncols=2)
zs = []
for ax, after in [(ax1, False), (ax2, True)]:
    z = Zu(ax, fontsize=14)
    fit(ax, HONKEN + [G_M, F_M, B + P(0, 9), A + P(0, -3)], margin=0.08, pad_aspect=True)
    if after:
        z.poly([G_M, F_M, C, W, V, E], color='none', fill=BLUE, alpha=0.18)
        z.poly(RO, color=BLACK, lw=1.0, ls='--', fill=PURPLE, alpha=0.30)
        z.poly(I_, fill=GREEN)
        z.poly([W, C], closed=False)
        z.poly([V, E], closed=False)
        ax.set_title('分合筆の後', fontsize=18, weight='bold', color=RED, pad=6)
    else:
        z.poly(N5_M, color='none', fill=BLUE, alpha=0.18)
        z.poly(HONKEN, fill=GREEN)
        z.poly(RO, fill=RED, alpha=0.30, color=BLACK)
        z.line(V, W, color=RED, lw=2.4, ls='--')
        ax.set_title('分合筆の前（登記記録）', fontsize=18, weight='bold', pad=6)
    z.poly([E, G_M, F_M, C], color=GRAY, lw=1.6, ls='--', closed=False)
    z.north_arrow(length=0.07)
    for n, p in PTS.items():
        z.point(p, 'dot', size=5)
        z.point_label(p, n, away=CT, fs=12)
    for p, n in [(G_M, 'G'), (F_M, 'F')]:
        z.point(p, 'dot', size=5, color=GRAY)
        z.point_label(p, n, away=centroid(N5_M), fs=12, color=GRAY)
    zs.append(z)
zs[0].free_text(centroid(N5_M), '100番5　雑種地\n186㎡（186.6334）', fs=15)
zs[0].free_text(centroid(I_), '100番1　雑種地\n380㎡', fs=16, offsets=((0, -10), (0, -30), (0, 10)))
zs[0].callout((C + W) / 2, '（ロ）部分\n67.9542', dirs=(0, -15, 15), color=RED, dists=(40, 55, 70))
zs[1].free_text(centroid(N5_M) + P(1.0, 0), '100番5　雑種地\n254㎡\n（186.6334＋67.9542\n＝254.5876）', fs=14, color=RED)
zs[1].free_text(centroid(I_), '（イ）100番1　雑種地\n314㎡（314.47645）', fs=15, offsets=((0, -10), (0, -30), (0, 10)))
zs[1].callout((C + W) / 2, '地役権の範囲\n南側67平方\nメートル', dirs=(0, -15, 15), color=PURPLE, dists=(40, 55, 70))
ALL_PROBLEMS += save(fig, zs, 'H26_dai21mon_zu15_bungouhitsu.png')

# =====================================================================
# 図16：問3 100番5の甲区と乙区（整理図。固定配置）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図16　問3　分合筆の後、100番5の甲区と乙区に記録されること', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
BOXES = [
    (68, '100番5の甲区（不動産登記規則第107条第1項。分合筆は第108条第3項で準用）', BLUE,
     ['登記の目的：合併による所有権登記', '受付年月日・受付番号：平成26年8月22日第○号',
      '権利者その他の事項：共有者　B市K町213番地　持分3分の1　乙野二郎',
      '　B市L三丁目4番5号　3分の1　甲野明子　K市B町135番地　3分の1　山川次郎'], [0]),
    (38, '100番5の乙区（規則第107条第3項。第108条第3項で準用）', PURPLE,
     ['100番1の乙区1番の地役権の登記を移記する', '（地役権設定　平成20年10月10日受付第10000号　要役地 A市B町字C102番）',
      '移記した地役権の登記に、地役権設定の範囲（南側67平方メートル）と地役権図面番号を記録'], [0, 2]),
    (9, '100番1の乙区（第108条第3項が準用する第104条第5項・第3項）', GRAY,
     ['（イ）100番1には地役権がかからなくなった旨を付記登記で記録し、地役権の登記を抹消する記号を記録',
      '（誤り）「100番5は同じ共有者だから甲区に何も記録されない」「地役権は100番1に残る」'], []),
]
for y, head, col, lines, red in BOXES:
    ax.add_patch(FancyBboxPatch((3, y), 94, 23, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=col, lw=2.2))
    ax.text(5, y + 20.0, head, fontsize=19, weight='bold', va='center', color=col)
    for i, s in enumerate(lines):
        ax.text(7, y + 15.2 - i * 4.0, s, fontsize=16.5, va='center', color=RED if i in red else BLACK)
fig.text(0.5, 0.045, '（ロ）の部分が100番5に加わるので、甲区に合併による所有権登記が入り、地役権の登記も100番5の乙区へ移る。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H26_dai21mon_zu16_kouku_otsuku.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図16: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図17：問5 地積測量図（100番1）の完成見本
# =====================================================================
fig, (ax,) = new_figure('図17　問5　地積測量図（100番1）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm（本件土地は横約110mm・縦約69mm、基準点まで入れると横約159mm・縦約142mm）。\n'
                        '試験の答案用紙の第5欄の枠は横約30cm・縦約20cmなので、T1〜T3まで縮尺どおりに入る（波線で距離を省かなくてよい）。\n'
                        '辺長は小数第3位を四捨五入（CDは3.8989…なので3.90、WCは3.2156…なので3.22）。（ロ）には地番を付けない。\n'
                        '座標値・地積・求積方法・測量年月日は書かない（問題文の注5）。T1〜T3は位置と名称だけ（問題文の注6）。観測点Pと合筆先の100番5の形は描かない。')
z = Zu(ax)
fit(ax, HONKEN + [T1, T2, T3], margin=0.06, pad_aspect=True)
z.poly(HONKEN, lw=2.0)
z.line(V, W, lw=2.0)
z.line(E, E + (E - A) / abs(E - A) * 2.5, lw=1.2)
z.line(C, C + (C - B) / abs(C - B) * 2.5, lw=1.2)
z.line(W, W + P(0.8, 5.0), lw=1.2)
z.line(C, C + P(0.6, 4.0), lw=1.2)
z.north_arrow()
for n, (p, q, s) in SIDES.items():
    z.edge_label(p, q, s, CT, fs=16 if n not in ('WC', 'CD', 'EV') else 15)
z.edge_label(V, W, '20.46', centroid(I_), fs=16, outward=False, ts=(0.5, 0.6, 0.4))
z.free_text(centroid(I_), '（イ）\n100－1', fs=18)
z.free_text(centroid(RO), '（ロ）', fs=16, offsets=((0, 0), (-20, 0), (20, 0)))
for n, p in PTS.items():
    z.point(p, KIND[n], size=7 if KIND[n] == 'concrete' else 9)
    z.point_label(p, n, away=CT)
for p, n in [(T1, 'T1'), (T2, 'T2'), (T3, 'T3')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=CT)
z.edge_label(D, E, '100－5', CT, fs=16, dists=(40, 50), rotate=False)
z.free_text(C, '100－4', fs=16, offsets=((20, 50), (40, 45), (10, 60)))
z.edge_label(W, C, '102', CT, fs=16, dists=(38, 48), rotate=False)
z.edge_label(B, W, '101', CT, fs=16, dists=(38, 48), rotate=False)
z.edge_label(A, B, '道路', CT, fs=16, dists=(40, 50), rotate=False, ts=(0.5, 0.4, 0.6))
z.edge_label(A, E, '道路', CT, fs=16, dists=(40, 50), rotate=False, ts=(0.5, 0.4, 0.6))
z.free_text(P(252.5, 205.0), '（単位：ｍ）\n◎ コンクリート杭：A・C・D・W\n● 金属標：B・E・V\n△ A市基準点：T1・T2・T3', fs=13,
            ha='right', va='top', offsets=((0, 0), (0, -30), (-30, 0)))
ALL_PROBLEMS += save(fig, [z], 'H26_dai21mon_zu17_chiseki_sokuryouzu.png')

# =====================================================================
# 図18：本番で解く順番（整理図。固定配置）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図18　本番で解く順番（座標の連鎖がいちばん時間を食う）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.08, 0.94, 0.83])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
STEPS = [
    ('1', '共有者と最下欄の印（計算なし）', ['甲区の持分を1つずつ追い、乙野二郎・甲野明子・山川次郎の3人に決める',
                                     '答案用紙の土地の表示の最下欄に「地役権」と印を付ける'], GRAY),
    ('2', '座標なしで書ける欄を先に', ['問3：甲区（合併による所有権登記・共有者と持分）、乙区（地役権の移記・範囲・地役権図面番号）',
                                 '問4：登記の目的・申請人・登録免許税・（イ）（ロ）の行の原因・100番5の4行目（雑種地 186）'], GREEN),
    ('3', '座標の連鎖（問1・問2）', ['P（T3から放射）→ D・E（Pから放射。後視の向きを取り直す）→ V・W（直線上の点）',
                             '丸めた座標を記憶してから次へ。1つ間違えると後が全部やり直し'], RED),
    ('4', '公差の確認', ['本件土地 382.4314㎡と380㎡の差 2.4314㎡ ＜ 乙1の5.39㎡（地積更正は要らない）',
                      'ED 15.02・DC 3.90と100番5の地積測量図の15.05・3.89（15m 35cm・3m 27cmの中）'], BLUE),
    ('5', '面積と地積の欄', ['（イ）314.47645 → 314、（ロ）67.9542 → 67、100番5の三斜 186.6334',
                        '合筆後 186.6334 ＋ 67.9542 ＝ 254.5876 → 254、最下欄の「南側67平方メートル」'], ORANGE),
    ('6', '地積測量図（問5）', ['辺長8本・境界標・T1〜T3（第5欄の枠は横約30cm・縦約20cmで、縮尺どおりに入る）'], PURPLE),
]
y = 96
for num, head, lines, col in STEPS:
    h = 6.6 + 3.9 * len(lines)
    y -= h
    ax.add_patch(FancyBboxPatch((3, y), 94, h - 1.6, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=col, lw=2.2))
    ax.text(5, y + h - 4.4, f'{num}　{head}', fontsize=19, weight='bold', va='center', color=col)
    for i, t in enumerate(lines):
        ax.text(8, y + h - 8.6 - i * 3.9, t, fontsize=15.5, va='center')
    y -= 1.4
fig.text(0.5, 0.035, '1・2は計算なしで書ける。3〜5の座標と面積に時間を回し、計算が間に合わなくても登記記録と申請書の半分は点になる。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H26_dai21mon_zu18_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図18: 整理図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
