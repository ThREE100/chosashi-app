"""令和元年度 第21問（土地）会話形式note記事の解説図13枚を、座標値から作図する。

`../prompt_R1_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../R6/Q21/zu/draw_R6_dai21mon_kaisetsuzu.py`。

実行: python3 note-articles-Kijyutsu/R1/Q21/zu/draw_R1_dai21mon_kaisetsuzu.py [出力フォルダ]
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
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
T1, T2 = P(285.36, 297.00), P(285.50, 312.00)
A, B, C = P(300.00, 300.00), P(302.00, 318.00), P(289.22, 318.00)
E, F, H = P(301.18, 310.62), P(290.00, 300.00), P(290.30, 318.00)
D = r2(radial(T1, T2, 4.72, dms(310, 1, 45)))                  # 問1 D点（T1から放射、時計回り）
w = (E - F) / (H - F)
G = r2(F + (H - F) * (w + w.conjugate()) / 2)                 # 問1 G点（EからFHへの垂線の足）
Dw = r2(radial(T1, T2, 4.72, -dms(310, 1, 45)))               # 反時計回りに測った誤りの点
Gw = P(290.18, 310.62)                                         # Eから真南に下ろした誤りの点

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('D', D, P(289.00, 300.00)), ('G', G, P(290.18, 310.80)), ('Dw', Dw, P(281.77, 300.07))]:
    assert abs(got - want) < 1e-9, (n, got, want)
assert abs(Gw.real - r2(F + (H - F) * (Gw.imag - F.imag) / (H.imag - F.imag)).real) < 1e-9   # 誤りの点もFH上
assert Gw.imag < G.imag and f'{G.imag - Gw.imag:.2f}' == '0.18'                          # 誤りの点は0.18m西
assert Dw.real < T1.real                                                                  # 誤りのDはT1より南
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'AE': (A, E, '10.69'), 'EB': (E, B, '7.43'), 'BH': (B, H, '11.70'), 'HC': (H, C, '1.08'),
         'CD': (C, D, '18.00'), 'DF': (D, F, '1.00'), 'FA': (F, A, '10.00'), 'EG': (E, G, '11.00'),
         'FG': (F, G, '10.80'), 'GH': (G, H, '7.20')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
HONKEN = [A, B, C, D, F]           # 本件土地（5番）
KOU = [A, E, G, F]                 # 甲区画 → （イ）5番1
OTSU = [C, D, F, G, H]             # 乙区画 → （ロ）5番2
HEI = [B, H, G, E]                 # 丙区画 → （ハ）5番3
fl = lambda v: f'{chiseki(v):.2f}'  # noqa: E731  地積・比較用の面積（小数第2位未満切捨て）
AREAS = {'本件土地': (HONKEN, '214.02'), '甲区画': (KOU, '112.51'), '乙区画': (OTSU, '18.72'), '丙区画': (HEI, '82.78'),
         '甲区画（誤りのG）': ([A, E, Gw, F], '111.51'), '丙区画（誤りのG）': ([B, H, Gw, E], '83.76')}
for n, (pts, want) in AREAS.items():
    assert fl(area(pts)) == want, (n, fl(area(pts)), want)
assert f'{chiseki(area(KOU)) + chiseki(area(OTSU)) + chiseki(area(HEI)):.2f}' == '214.01'
assert to_dms(cmath.phase(T2 - T1)) == '89°27′54.92″'
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
BRG_T2 = math.degrees(cmath.phase(T2 - T1))              # T1→T2の方向角（北から時計回り）89.47°
BRG_D = BRG_T2 + 310 + 1 / 60 + 45 / 3600                # 399.49°（＝39.49°）
KIND = {'A': 'stone', 'B': 'stone', 'C': 'concrete', 'D': 'concrete', 'F': 'concrete', 'G': 'concrete',
        'H': 'concrete', 'E': 'metal'}
PTS = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H}


def neighbors(z, ref, fs=15, color=GRAY):
    """隣接地の地番・道路（水平に、辺長より外側へ）"""
    z.edge_label(A, B, '2－32', ref, fs=fs, color=color, dists=(34, 44, 54), rotate=False, ts=(0.3, 0.2, 0.4))
    z.free_text(A, '1－25', fs=fs, color=color, offsets=((-38, 26), (-48, 32), (-30, 38)))
    z.free_text(B, '3－3', fs=fs, color=color, offsets=((34, 22), (44, 28), (30, 36)))
    z.edge_label(F, A, '4－1', ref, fs=fs, color=color, dists=(40, 50, 60), rotate=False)
    z.free_text(F + (D - F) * 0.5, '4－2', fs=fs, color=color, offsets=((-78, 0), (-88, -6), (-96, 4)))
    z.edge_label(B, H, '6－1', ref, fs=fs, color=color, dists=(40, 50, 60), rotate=False)
    z.free_text(H + (C - H) * 0.5, '6－2', fs=fs, color=color, offsets=((78, 0), (88, -6), (96, 4)))
    z.edge_label(D, C, '道路　100', ref, fs=fs, color=color, dists=(40, 50, 60), rotate=False, ts=(0.5, 0.4, 0.6))


# =====================================================================
# 図2：全体像（北を上にして座標どおりに描き直した調査図素図）
# =====================================================================
fig, (ax,) = new_figure('図2　北を上にして描き直した全体像（令和元年10月の調査時点）',
                        'A・F・D（Y＝300.00）とB・H・C（Y＝318.00）は、それぞれ真北向きの一直線。\n'
                        'F→HはXが290.00→290.30で、わずかに東へ上がる（真東向きではない）。\n'
                        '甲区画に建物（家屋番号5番）、丙区画は柵や囲いのない家庭菜園、乙区画は出入口。')
z = Zu(ax)
fit(ax, HONKEN + [T1, T2], margin=0.10, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(HEI, fill=ORANGE)
z.poly(OTSU, fill=BLUE)
z.north_arrow()
ck, ch = centroid(KOU), centroid(HEI)
cz = centroid(HONKEN)
z.free_text(ck, '甲区画\n建物（家屋番号5番）', fs=16)
z.free_text(ch, '丙区画\n家庭菜園', fs=16)
z.callout(F + (H - F) * 0.35 + P(-0.5, 0), '乙区画（出入口）', dirs=(-100, -80, -120), color=BLUE, dists=(55, 75, 95))
for n, p in PTS.items():
    z.point(p, KIND[n])
    z.point_label(p, n, away=cz)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=cz)
neighbors(z, cz)
z.free_text(P(287.2, 309.0), '5番　宅地　212.70㎡（登記記録）　山川一郎', fs=15, color=BLACK, offsets=((0, 0), (0, -12), (0, 12)))
ALL_PROBLEMS += save(fig, [z], 'R1_dai21mon_zu02_zentaizu.png')

# =====================================================================
# 図3：問1 D点（T1から放射）
# =====================================================================
fig, (ax,) = new_figure('図3　問1　D点の求め方（T1から放射）',
                        'T1→T2の方向角 89°27′54.92″ に、時計回りの観測角 310°01′45″ を足す（399°29′39.92″＝39°29′39.92″の向き）。\n'
                        '4.72m 進むと、Fの真南1.00mのD点。反時計回りに測ると（281.77, 300.07）で、T1よりさらに南に出てしまう。')
z = Zu(ax)
fit(ax, [T1 + P(0, -6.5), T2 + P(0, 2.5), D, Dw + P(-1.2, 0), F, C, B], margin=0.05, pad_aspect=True)
z.poly(HONKEN, color=GRAY, lw=1.1)
z.line(T1, T1 + 3.0, color=GRAY, lw=1.2, ls='--')
z.free_text(T1 + 3.0, '北', color=GRAY, fs=14, offsets=((0, 14), (-14, 10), (14, 10)))
z.line(T1, T2, color=BLUE, lw=2.0)
z.line(T1, D, color=RED, lw=2.6)
z.line(T1, Dw, color=GRAY, lw=1.4, ls=':')
z.north_arrow()
z.angle_arc(T1, 1.5, 0, BRG_T2, color=BLUE)
z.angle_arc(T1, 0.8, BRG_T2, BRG_D, color=RED)
for p, kind in [(T1, 'kijun'), (T2, 'kijun'), (D, 'concrete'), (F, 'concrete'), (C, 'concrete')]:
    z.point(p, kind)
z.point(Dw, 'dot', color=GRAY)
for p, n in [(F, 'F'), (C, 'C')]:
    z.point_label(p, n, away=cz)
z.edge_label(T1, T2, '後視（T2の方向）', T1 + P(5, 0), color=BLUE, fs=14, ts=(0.6, 0.7, 0.5), dists=(16, 22))
z.edge_label(T1, D, '4.72', T1 + P(0, 5), color=RED, fs=17, ts=(0.6, 0.7, 0.5), dists=(14, 20, 26))
z.edge_label(D, F, 'DF ＝ 1.00', cz, color=BLACK, fs=14, dists=(75, 90, 105), rotate=False)
z.callout(T1 + P(1.06, 1.06), '方向角 89°27′54.92″\n（北から時計回りにT2の方向）', dirs=(20, 0, 35, -10), color=BLUE,
          dists=(110, 140, 170))
z.callout(T1 + P(0, -0.8), '観測角 310°01′45″\n（T2の方向から時計回り）', dirs=(170, 150, -170, -150), color=RED,
          dists=(60, 85, 110))
z.callout(D, 'D（289.00, 300.00）', dirs=(150, 170, 130, -170), color=RED)
z.callout(Dw, '反時計回りに測った誤り\n（281.77, 300.07）', dirs=(0, -20, 20, -40), color=GRAY)
z.callout(T1, 'T1（285.36, 297.00）', dirs=(-120, -100, -140, -80), color=BLACK, dists=(70, 95, 120))
z.callout(T2, 'T2（285.50, 312.00）', dirs=(-20, 0, -40), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'R1_dai21mon_zu03_D_housha.png')

# =====================================================================
# 図4：問1 G点（EからFHへの垂線の足）
# =====================================================================
fig, (ax1, ax2) = new_figure('図4　問1　G点の求め方（EからFHへの垂線の足）',
                             'w ＝ (E − F) ÷ (H − F) ＝ 0.6001… − 0.6111…i。実部の0.6001…が「FからHまでのどこにGがあるか」の割合。\n'
                             'G ＝ F ＋ (H − F) × (w ＋ Conjg(w)) ÷ 2（wと共役の平均で実部だけを残す）。\n'
                             'Eから真南に下ろした（290.18, 310.62）はFHと直角にならず、0.18m西にずれる（甲区画111.51㎡・丙区画83.76㎡に狂う）。',
                             ncols=2, width_ratios=[1.35, 1])
za = Zu(ax1, fontsize=14)
fit(ax1, HONKEN, margin=0.08, pad_aspect=True)
za.poly(KOU, fill=GREEN)
za.poly(HEI, fill=ORANGE)
za.poly(OTSU, color=BLACK, lw=1.2)
za.line(E, G, color=RED, lw=3.0)
za.line(E, Gw, color=GRAY, lw=1.4, ls=':')
za.north_arrow(length=0.08)
za.right_angle(G, F, E, size=0.7, color=RED)
for n in 'ABCDEFH':
    za.point(PTS[n], KIND[n])
    za.point_label(PTS[n], n, away=cz)
za.point(G, 'concrete')
za.callout(G, 'G（290.18, 310.80）', dirs=(-60, -80, -40), color=RED, dists=(60, 80, 100))
za.free_text(centroid(KOU), '甲区画\n112.51㎡', fs=15)
za.free_text(centroid(HEI), '丙区画\n82.78㎡', fs=15)
za.edge_label(E, G, 'EG ⊥ FH', centroid(HEI), color=RED, fs=14, outward=False, ts=(0.6, 0.7, 0.5), dists=(16, 24))

zb = Zu(ax2, fontsize=14)
lo, hi = G + P(-0.30, -0.42), G + P(0.45, 0.30)
ax2.set_xlim(lo.imag, hi.imag)
ax2.set_ylim(lo.real, hi.real)
zb.line(F + (H - F) * 0.57, F + (H - F) * 0.63, color=BLACK, lw=2.0)
zb.line(G, G + (E - G) * 0.045, color=RED, lw=3.0)
zb.line(Gw, Gw + (E - Gw) * 0.045, color=GRAY, lw=1.6, ls=':')
zb.north_arrow(length=0.08)
zb.right_angle(G, H, E, size=0.06, color=RED)
zb.point(G, 'dot', color=RED, size=11)
zb.point(Gw, 'dot', color=GRAY, size=11)
zb.callout(G, 'G（290.18, 310.80）\nFHへの垂線の足', dirs=(-60, -80, -40), color=RED, dists=(60, 80, 100))
zb.callout(Gw, '真南に下ろした誤り\n（290.18, 310.62）', dirs=(-120, -100, -140), color=GRAY, dists=(60, 80, 100))
zb.free_text(G + (Gw - G) * 0.5, '0.18', fs=18, color=RED, offsets=((0, -18), (0, -26), (0, 18)))
zb.free_text(G + (E - G) * 0.035, 'Eの方向（北）', fs=15, color=GRAY, offsets=((75, 0), (85, 10), (75, -10)))
zb.free_text(F + (H - F) * 0.585, 'F→H', fs=15, color=BLACK, offsets=((0, -16), (0, -24), (0, 16)))
ax2.set_title('Gのまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'R1_dai21mon_zu04_G_suisen.png')

# =====================================================================
# 図6：問2（1）（2）対象土地と関係土地（地図に準ずる図面の写しの模式図）
# =====================================================================
# 5番は座標どおり。6番・7番・3番2・3番3などは、地図に準ずる図面の写しの形を見て置いた模式の位置（座標ではない）。
slope_n = (B - A) / (B.imag - A.imag)          # 北側の線（AB）の東へ1mあたりの変化
slope_s = (C - D) / (C.imag - D.imag)          # 南側の線（DC）の東へ1mあたりの変化
N = lambda y: A + slope_n * (y - A.imag)       # noqa: E731  北側の線の上の、Y＝yの点
S = lambda y: D + slope_s * (y - D.imag)       # noqa: E731  南側の線の上の、Y＝yの点
B6, C6 = N(325.2), S(325.2)                    # 6番と7番の境
B7, C7 = N(331.0), S(331.0)                    # 7番の東（図の端）
N32 = N(323.2)                                 # 3番3と3番2の境
W0 = 295.0                                     # 西の端（図の端）
UP = P(4.0, 0)                                 # 北側の土地の奥行き（模式）
DN = P(-3.5, 0)                                # 道路の幅（模式）
L5 = [A, B, C, D, F]
L6 = [B, B6, C6, C]
L7 = [B6, B7, C7, C6]
L232 = [A, B, B + UP, A + UP]
L33 = [B, N32, N32 + UP, B + UP]
L32 = [N32, B7, B7 + UP, N32 + UP]
L125 = [N(W0), A, A + UP, N(W0) + UP]
L41 = [F + P(0, W0 - 300), F, A, N(W0)]
L42 = [S(W0), D, F, F + P(0, W0 - 300)]
L100 = [S(W0), C7, C7 + DN, S(W0) + DN]
SC = S(316.0)                                  # 申請人の主張線の南の端（模式）
fig, (ax,) = new_figure('図6　問2（1）（2）　対象土地と関係土地（平成18年9月の筆界特定の申請の時点）',
                        '対象の筆界は5番と6番の境（B→C）。対象土地は5番と6番（6番1・6番2への分筆は筆界特定の後）。\n'
                        '関係土地は、筆界の両端のB点・C点に接する2番32・3番3・100番。3番2・7番・4番1・4番2・1番25は、\n'
                        'B点・C点を含む筆界で対象土地と接していないので関係土地ではない。\n'
                        '模式図：5番は座標どおり。6番・7番・3番2・3番3などの形と大きさは、地図に準ずる図面の写しを見て置いたもの（座標ではない）。')
z = Zu(ax, fontsize=14)
fit(ax, L125 + L7 + L100 + L32 + [P(309.0, 296.0), P(287.0, 292.0)], margin=0.02, pad_aspect=True)
for pg in (L5, L6):
    z.poly(pg, fill=BLUE, alpha=0.25, lw=1.4)
for pg in (L232, L33, L100):
    z.poly(pg, fill=ORANGE, alpha=0.25, lw=1.4)
for pg in (L7, L32, L125, L41, L42):
    z.poly(pg, color=GRAY, lw=1.2)
z.line(B, C, color=RED, lw=4.5)
z.line(B, SC, color=RED, lw=1.8, ls='--')
z.north_arrow(length=0.07)
z.free_text(centroid(L5), '5番（対象土地）\n山川一郎', fs=15)
z.free_text(centroid(L6), '6番\n（対象土地）\n北冬男・北冬子', fs=13)
z.free_text(centroid(L232), '2番32（関係土地）\n東春男・東春子', fs=14)
z.free_text(centroid(L33), '3番3\n（関係土地）\n西秋男', fs=12)
z.free_text(centroid(L100), '100番（関係土地）　道路　A市', fs=14)
z.free_text(centroid(L32), '3番2　南夏男\n（関係土地ではない）', fs=13, color=GRAY)
z.free_text(centroid(L7), '7番\n中太郎\n（関係土地\nではない）', fs=12, color=GRAY)
z.free_text(centroid(L125), '1番25', fs=14, color=GRAY)
z.free_text(centroid(L41), '4番1', fs=14, color=GRAY)
z.callout(centroid(L42), '4番2', dirs=(170, 160, 180), color=GRAY, fs=13, dists=(70, 90, 110))
for p, n in [(B, 'B'), (C, 'C')]:
    z.point(p, 'dot', color=RED, size=10)
z.callout(B, 'B：筆界の北の端（2番32・3番3が接する）', dirs=(120, 100, 140), color=RED, dists=(70, 95, 120))
z.callout(C, 'C：筆界の南の端（100番が接する）', dirs=(-60, -40, -80), color=RED, dists=(60, 80, 100))
z.callout(B + (SC - B) * 0.55, '北冬男の主張線', dirs=(180, 160, -160), color=RED, dists=(60, 80, 100))
ALL_PROBLEMS += save(fig, [z], 'R1_dai21mon_zu06_taishou_kankei_tochi.png')

# =====================================================================
# 図7：問2（3）関係人の整理図（固定配置）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図7　問2（3）　関係人は「対象土地の申請人以外」＋「関係土地の全員」（不動産登記法第133条第1項）',
             fontsize=22, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.12, 0.94, 0.78])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
BOXES = [
    (70, '第1号　対象土地の所有権登記名義人等であって、筆界特定の申請人以外のもの',
     [('5番', '山川一郎', RED, ''), ('6番', '北冬子', RED, '（共有者のうち申請していない方）'),
      ('6番', '北冬男', GRAY, '← 筆界特定の申請人なので関係人ではない')]),
    (38, '第2号　関係土地の所有権登記名義人等（全員）',
     [('2番32', '東春男・東春子', RED, '（共有者の2人とも）'), ('3番3', '西秋男', RED, ''),
      ('100番', 'A市', RED, '（「名称」で書く）')]),
    (6, '関係人にならない人（関係土地ではない土地の所有者）',
     [('3番2', '南夏男', GRAY, '← 6番と接するが、B点・C点を含む筆界ではない'),
      ('7番', '中太郎', GRAY, '← 6番と接するが、B点・C点を含む筆界ではない')]),
]
for y, head, rows in BOXES:
    ax.add_patch(FancyBboxPatch((3, y), 94, 24, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=BLACK, lw=1.4))
    ax.text(5, y + 21, head, fontsize=19, weight='bold', va='center')
    for i, (lot, name, col, note) in enumerate(rows):
        yy = y + 14.5 - i * 6.0
        ax.text(9, yy, lot, fontsize=18, va='center', color=BLACK)
        ax.text(22, yy, name, fontsize=19, va='center', color=col, weight='bold')
        ax.text(42, yy, note, fontsize=16, va='center', color=GRAY if col == GRAY else BLACK)
fig.text(0.5, 0.06, '（3）の答え：北冬子、山川一郎、東春男、東春子、西秋男、A市',
         ha='center', va='center', fontsize=21, color=RED, weight='bold')
fig.text(0.5, 0.025, '筆界特定を申請したのは、6番の共有者の一人の北冬男（問題文）。第1号から外れるのは申請人だけで、共有者の北冬子は関係人。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R1_dai21mon_zu07_kankeinin.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図7: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図8：問3 分筆後の区画と地積
# =====================================================================
fig, (ax,) = new_figure('図8　問3　分筆後の区画と地積（5番 → 5番1・5番2・5番3）',
                        '座標法で求積し、宅地なので小数第2位未満を切り捨て：112.5162→112.51、18.72、82.7838→82.78。合計 214.01㎡。\n'
                        '本件土地全体（A→B→C→D→F）は 214.02㎡。0.01㎡の差は、3筆をそれぞれ切り捨てたため。')
z = Zu(ax)
fit(ax, HONKEN, margin=0.14, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(HEI, fill=ORANGE)
z.poly(OTSU, fill=BLUE)
z.north_arrow()
z.free_text(centroid(KOU), '（イ）5番1\n甲区画\n112.51㎡', fs=19)
z.free_text(centroid(HEI), '（ハ）5番3\n丙区画\n82.78㎡', fs=19)
z.callout(F + (H - F) * 0.45 + P(-0.5, 0), '（ロ）5番2　乙区画　18.72㎡', dirs=(-90, -110, -70), color=BLUE,
          dists=(60, 80, 100))
for n, p in PTS.items():
    z.point(p, KIND[n])
    z.point_label(p, n, away=cz)
z.free_text(cz + P(8.3, 0), '合計 112.51 ＋ 18.72 ＋ 82.78 ＝ 214.01㎡', fs=17, color=RED,
            offsets=((0, 0), (0, 14), (0, 28)))
ALL_PROBLEMS += save(fig, [z], 'R1_dai21mon_zu08_bunpitsu_chiseki.png')

# =====================================================================
# 図10：問3 地積更正が必要かの判定（数直線）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図10　問3　地積更正が必要かの判定（精度区分 甲2）', fontsize=24, weight='bold', y=0.96)
ax = fig.add_axes([0.06, 0.30, 0.88, 0.52])
ax.set_xlim(209.6, 215.8)
ax.set_ylim(-1.7, 2.6)
ax.axis('off')
ax.plot([209.8, 215.6], [0, 0], color=BLACK, lw=2)
for v in range(210, 216):
    ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1.2)
    ax.text(v, -0.28, f'{v}', ha='center', va='top', fontsize=13, color=GRAY)
ax.axvspan(212.70 - 2.57, 212.70 + 2.57, ymin=0.651, ymax=0.698, color=GRAY, alpha=0.30)
ax.text(215.27, 1.35, '甲3なら ± 2.57（市街地地域では使わない）', ha='right', va='bottom', fontsize=13, color=GRAY)
ax.axvspan(212.70 - 1.28, 212.70 + 1.28, ymin=0.407, ymax=0.558, color=GREEN, alpha=0.30)
ax.text(212.70, 0.75, '甲2の公差の範囲（212.70 ± 1.28）', ha='center', va='bottom', fontsize=15, color=GREEN)
ax.plot([212.70], [0], 'o', ms=12, color=BLUE)
ax.text(212.70, -0.75, '登記記録\n212.70㎡', ha='center', va='top', fontsize=16, color=BLUE, weight='bold')
ax.plot([214.01], [0], 'o', ms=12, color=RED)
ax.text(214.01, -0.75, '分筆後の合計\n214.01㎡', ha='center', va='top', fontsize=16, color=RED, weight='bold')
ax.plot([212.70 + 1.28, 212.70 + 1.28], [-0.15, 0.7], color=GREEN, lw=1.5, ls='--')
ax.text(214.06, 0.30, '上限 213.98', ha='left', va='bottom', fontsize=12, color=GREEN)
ax.annotate('', xy=(214.01, 1.85), xytext=(212.70, 1.85), arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
ax.text(213.35, 2.0, '差 1.31㎡ ＞ 公差 1.28㎡　→　範囲を超えている（わずか0.03㎡）', ha='center', va='bottom', fontsize=17,
        color=RED, weight='bold')
fig.text(0.5, 0.15, '市街地地域（不動産登記規則第10条第2項第1号）の地積測量図の誤差の限度は精度区分 甲2 まで（同条第4項第1号）。\n'
         '分筆前の地積（登記記録 212.70㎡）と分筆後の地積の合計（214.01㎡）の差で判断する（不動産登記事務取扱手続準則第72条第1項）。\n'
         '→ 錯誤を原因とする地積更正の登記が必要。分筆と一の申請情報で申請する（不動産登記規則第35条第7号）',
         ha='center', va='center', fontsize=16)
fig.text(0.5, 0.05, '本件土地全体の実測 214.02㎡ で比べても差は 1.32㎡ で、やはり公差を超える', ha='center',
         va='center', fontsize=15, color=GRAY)
path = os.path.join(OUT, 'R1_dai21mon_zu10_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図10: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図11：問3 地目の判断（家庭菜園も乙区画も宅地）
# =====================================================================
fig, (ax,) = new_figure('図11　問3　地目の判断（3筆とも宅地。一部地目変更は要らない）',
                        '家庭菜園と建物の敷地を区切る柵や囲いはなく、家庭菜園は住んでいる建物の庭の一角（建物の効用を果たすための土地。準則第68条第3号）。\n'
                        '「平成25年5月1日から栽培」の日付につられて「一部地目変更（畑）」にしない。乙区画も道路になるのは将来の予定で、今は出入口のある建物の敷地。\n'
                        '→ 登記の目的は「土地地積更正・分筆登記」（地目の変更の登記はない）')
z = Zu(ax)
fit(ax, HONKEN, margin=0.14, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(HEI, fill=GREEN)
z.poly(OTSU, fill=GREEN)
z.line(E, G, color=BLACK, lw=1.2, ls='--')
z.north_arrow()
z.free_text(centroid(KOU), '甲区画（5番1）\n建物の敷地\n→ 宅地', fs=18)
z.free_text(centroid(HEI), '丙区画（5番3）\n家庭菜園\n（柵・囲いなし）\n→ 宅地', fs=18)
z.callout(F + (H - F) * 0.45 + P(-0.5, 0), '乙区画（5番2）出入口・ブロック塀 → 宅地（公衆用道路ではない）',
          dirs=(-90, -110, -70), color=BLACK, dists=(60, 80, 100))
z.callout(E + (G - E) * 0.4, '敷地と菜園の間に柵や囲いはない', dirs=(160, 180, 140), color=RED, dists=(90, 120, 150))
for n, p in PTS.items():
    z.point(p, KIND[n])
    z.point_label(p, n, away=cz)
ALL_PROBLEMS += save(fig, [z], 'R1_dai21mon_zu11_chimoku.png')

# =====================================================================
# 図12：問4（第4欄）地積測量図（5番1・5番2・5番3）の完成見本（答案用紙の第4欄の印刷は ../touan_youshi/ で確かめた）
# =====================================================================
fig, (ax,) = new_figure('図12　問4（第4欄）地積測量図（5番1・5番2・5番3）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm（本件土地は横約72mm・縦約52mm、T1・T2まで入れると横約84mm・縦約67mm）。\n'
                        '第4欄の枠は横約30cm・縦約23cm。地番の欄は「5番1、5番2、5番3」、土地の所在の欄は「A市B町一丁目」。\n'
                        '作成者・申請人の「（略）」と縮尺1/250は印刷済み。方位記号は印刷がないので描く。\n'
                        '辺長は小数第3位を四捨五入（EB 7.4254→7.43、AE 10.6853→10.69、CD 18.0013→18.00）。\n'
                        '座標値・平面直角座標系の番号・地積と求積方法・測量年月日は書かない（問題文の注5）。基準点T1・T2は位置と点名だけ（問題文の注6）。')
z = Zu(ax)
fit(ax, HONKEN + [T1, T2], margin=0.10, pad_aspect=True)
z.poly(HONKEN, lw=2.0)
z.line(E, G, lw=2.0)
z.line(F, H, lw=2.0)
z.north_arrow()
for n, (p, q, s) in SIDES.items():
    if n == 'EG':
        z.edge_label(p, q, s, centroid(KOU), fs=16, outward=False)
    elif n in ('FG', 'GH'):
        z.edge_label(p, q, s, centroid(KOU if n == 'FG' else HEI), fs=16, outward=False)
    elif n == 'DF':
        z.free_text(p + (q - p) * 0.5, s, fs=15, offsets=((-30, -6), (-34, -14), (-30, 10)))
    elif n == 'HC':
        z.free_text(p + (q - p) * 0.5, s, fs=15, offsets=((30, 6), (34, 14), (30, -10)))
    else:
        z.edge_label(p, q, s, cz, fs=16)
z.free_text(centroid(KOU), '（イ）5－1', fs=17)
z.free_text(centroid(HEI), '（ハ）5－3', fs=17)
z.callout(F + (H - F) * 0.55 + P(-0.5, 0), '（ロ）5－2', dirs=(-90, -110, -70), color=BLACK, dists=(55, 70, 85))
for n, p in PTS.items():
    z.point(p, KIND[n])
    z.point_label(p, n, away=cz)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=cz)
neighbors(z, cz, fs=15, color=BLACK)
z.free_text(T2 + P(0.2, 3.2), '（単位：ｍ）\n□ 石杭：A・B\n◎ コンクリート杭：C・D・F・G・H\n● 金属標：E\n△ 基準点：T1・T2', fs=13,
            ha='left', va='bottom', offsets=((0, 0), (20, 0), (40, 0), (0, -30)))
ALL_PROBLEMS += save(fig, [z], 'R1_dai21mon_zu12_chiseki_sokuryouzu.png')

# =====================================================================
# 図5：問1 G点の別解（Eを通るFHに直角な直線とFHの交点）
# =====================================================================
num = (E - F).conjugate() * (H - F) * 1j
den = (H - F).conjugate() * (H - F) * 1j
t_g = num.imag / den.imag
assert f'{num.real:.3f}' == '-198.054' and f'{num.imag:.3f}' == '194.514' and f'{den.imag:.2f}' == '324.09'
assert r2(F + (H - F) * 194.514 / 324.09) == G
fig, (ax,) = new_figure('図5　問1　G点の別解（Eを通りFHに直角な直線と、FHの交点）',
                        'Eを通りFHに直角な直線の向きは (H − F) × i（FHの方向角に90°を足した向き）。この直線とFHの交点をConjgの積のiの係数の比で出す。\n'
                        't ＝ 194.514 ÷ 324.09 ＝ 0.6001…（wの実部と同じ）、G ＝ F ＋ (H − F) × t ＝ 290.1800… ＋ 310.8033…i → G（290.18, 310.80）。')
z = Zu(ax)
Fx, Hx = F + (F - H) * 0.06, H + (H - F) * 0.06
Pe = E + (H - F) * 1j / abs(H - F) * 1.6                 # 直角な直線をEの北へ少し延ばした点
Ps = G + (G - E) * 0.12                                   # Gの南へ少し延ばした点
fit(ax, [Fx, Hx, E, Pe, Ps, A, B], margin=0.06, pad_aspect=True)
z.poly([F, A, B, H], color=GRAY, lw=1.0, closed=False)   # 本件土地の西・北・東の辺（EGは描かない）
z.line(Fx, Hx, color=BLACK, lw=2.4)
z.line(Pe, Ps, color=RED, lw=2.4, ls='--')
z.north_arrow()
z.right_angle(G, H, E, size=0.8, color=RED)
for n in 'FHE':
    z.point(PTS[n], KIND[n])
    z.point_label(PTS[n], n, away=G + P(4, 0) if n != 'E' else G)
z.point(G, 'dot', color=RED, size=10)
z.callout(G, 'G（290.18, 310.80）', dirs=(-60, -40, -80), color=RED, dists=(60, 80, 100))
z.callout(E + (G - E) * 0.45, '向き (H − F) × i\n（FHを90°回した向き）', dirs=(170, 190, 150), color=RED, dists=(80, 110, 140))
z.callout(F + (H - F) * 0.3, 'F→H：向き H − F ＝ 0.30 ＋ 18.00i', dirs=(-100, -120, -80), color=BLACK, dists=(50, 70, 90))
z.free_text(P(295.0, 314.5), 't ＝ 194.514 ÷ 324.09 ＝ 0.6001…\nFからHまでの 0.6001… の位置', fs=16, color=RED,
            offsets=((0, 0), (20, 0), (0, 20), (0, -20)))
ALL_PROBLEMS += save(fig, [z], 'R1_dai21mon_zu05_G_betsukai.png')

# =====================================================================
# 図9：問3 四角形の面積を対角線で出す別解（甲区画・丙区画）
# =====================================================================
dk = (A - G).conjugate() * (E - F)
dh = (E - H).conjugate() * (B - G)
assert f'{dk.imag:.4f}' == '225.0324' and f'{dh.imag:.4f}' == '165.5676'
fig, (ax1, ax2) = new_figure('図9　問3　四角形の面積を対角線で出す別解（甲区画・丙区画）',
                             '四角形は、向かい合う頂点を結んだ2本の対角線 u・v で、倍面積 ＝ Conjg(u) × v のiの係数。4点を順に回る式と同じ値になる。\n'
                             '甲区画：Conjg(A − G) × (E − F) ＝ −4.9084 ＋ 225.0324i → 112.5162 → 112.51㎡。\n'
                             '丙区画：Conjg(E − H) × (B − G) ＝ 75.4656 ＋ 165.5676i → 82.7838 → 82.78㎡。\n'
                             '乙区画（C・D・F・G・Hの5点）は四角形ではないので、順に回る式のまま。',
                             ncols=2)
zs = []
for ax, pg, (u0, u1), (v0, v1), fill, head, im in [
        (ax1, KOU, (A, G), (E, F), GREEN, '甲区画（5番1）　対角線 A−G と E−F', '225.0324'),
        (ax2, HEI, (E, H), (B, G), ORANGE, '丙区画（5番3）　対角線 E−H と B−G', '165.5676')]:
    z = Zu(ax, fontsize=14)
    fit(ax, pg, margin=0.22, pad_aspect=True)
    z.poly(pg, fill=fill)
    z.line(u0, u1, color=RED, lw=2.2, ls='--')
    z.line(v0, v1, color=BLUE, lw=2.2, ls='--')
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=17, weight='bold', pad=6)
    for p in pg:
        n = [k for k, v in PTS.items() if v == p][0]
        z.point(p, KIND[n])
        z.point_label(p, n, away=centroid(pg))
    lo = min(q.real for q in pg)
    z.free_text(P(lo - 1.3, centroid(pg).imag), f'iの係数 {im}', fs=16, color=BLACK, offsets=((0, 0), (0, -14), (0, 14)))
    zs.append(z)
ALL_PROBLEMS += save(fig, zs, 'R1_dai21mon_zu09_taikakusen.png')


def seiri_zu(title, caption, boxes, name, fs_head=19, fs_line=16):
    """固定配置の整理図（角丸の枠を上から並べる）。boxes: [(見出し, [(文字, 色)], 枠の色)]"""
    setup_font()
    fig = plt.figure(figsize=(16, 12), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=22, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.12, 0.94, 0.78])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    n = len(boxes)
    h = 100 / n
    for k, (head, lines, ec) in enumerate(boxes):
        y = 100 - (k + 1) * h + 1.5
        ax.add_patch(FancyBboxPatch((3, y), 94, h - 4.5, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=ec, lw=1.8))
        ax.text(5, y + h - 8, head, fontsize=fs_head, weight='bold', va='center', color=ec)
        for i, (txt, col) in enumerate(lines):
            ax.text(8, y + h - 8 - (i + 1) * 5.6, txt, fontsize=fs_line, va='center', color=col)
    fig.text(0.5, 0.05, caption, ha='center', va='center', fontsize=16)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print(f'[重なり検査] {name}: 整理図（固定配置）\n  →', path)


# =====================================================================
# 図1：注の仕分け（固定配置）
# =====================================================================
seiri_zu('図1　注の仕分け（問題文の注・調査図素図の注・観測値の表の注）',
         '問題文の注と、調査図素図の注・観測値の表の注は番号が別々。記事では「問題文の注3」「観測値の表の注1」のように呼び分ける。',
         [('問題文の注1〜4・注7　毎年ほぼ同じ決まり文句（読み流してよい）',
           [('注1 行為は適法、書類はそろっている　　注2 書面申請', GRAY),
            ('注3 座標値は小数第3位を四捨五入　　注4 地積測量図の筆界点間の距離も小数第3位を四捨五入', GRAY),
            ('注7 訂正・加入・削除の方法', GRAY)], GRAY),
          ('今年だけの指示（印を付ける）',
           [('問題文の注5：地積測量図に、各筆界点の座標値・平面直角座標系の番号又は記号・地積及びその求積方法・測量年月日は書かない', RED),
            ('問題文の注6：A市基準点（T1・T2）は、位置を描いて点名を付ける（座標値は書かない）', RED),
            ('問3のただし書き：分筆以外に必要な表示の登記は一の申請情報で。地積は座標値から座標法で求積', RED)], RED),
          ('計算の条件（問1で使う）',
           [('調査図素図の注：A・B・C・D・F・Hは筆界点。EはAとBを結ぶ直線上、GはFとHを結ぶ直線上', BLUE),
            ('観測値の表の注1：観測角は時計回り（足す）　　注2：北はX軸の正の向き', BLUE),
            ('聴取記録の5：EGはF・G・Hの直線の垂線（G点の条件）', BLUE)], BLUE)],
         'R1_dai21mon_zu01_chuu_shiwake.png', fs_line=15)

# =====================================================================
# 図13：解く順番と時間配分（固定配置）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図13　解く順番と時間配分（いちばん重いのはG点と3筆の面積）', fontsize=22, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.12, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
STEPS = [('① 問題文を読み、注を仕分ける', BLACK), ('② 問1 D点（T1から放射。1回だけ）', BLACK),
         ('③ 問1 G点（FHへの垂線の足）　← いちばん重い', RED), ('④ 3筆の面積と公差の判定（差1.31㎡ ＞ 1.28㎡）　← 重い', RED),
         ('⑤ 問3 登記申請書', BLACK), ('⑥ 問4 地積測量図（辺長10本、T1・T2も描く）', BLACK),
         ('⑦ 問2 筆界特定（計算なし。条文の定義で関係人を数える）', BLACK)]
for k, (txt, col) in enumerate(STEPS):
    y = 92 - k * 13
    ax.add_patch(FancyBboxPatch((3, y - 4.2), 52, 8.4, boxstyle='round,pad=0.5', fc='#fff5f5' if col == RED else '#f7f7f7',
                                ec=col, lw=1.8))
    ax.text(5, y, txt, fontsize=16, va='center', color=col, weight='bold' if col == RED else 'normal')
    if k < len(STEPS) - 1:
        ax.annotate('', xy=(29, y - 8.2), xytext=(29, y - 5.0), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.8))
SIDE = [(88, 'G点がなくても書ける欄（手が止まったら先に）', BLUE,
         ['問2の全部', '添付書類：地積測量図　代理権限証書', '登録免許税：金3,000円（分筆後3個）', '申請人・所在',
          '1行目：5番　宅地　212.70', '（ロ）（ハ）の地番・地目・原因']),
        (40, '面積と公差の後でないと書けない欄', RED,
         ['登記の目的（地積更正が要るか）', '（イ）の原因（③錯誤）', '（イ）（ロ）（ハ）の地積', '地積測量図の辺長（D・Gが要る）'])]
for y0, head, col, items in SIDE:
    hgt = 7 + 5.2 * len(items)
    ax.add_patch(FancyBboxPatch((60, y0 - hgt), 37, hgt, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=col, lw=1.8))
    ax.text(62, y0 - 3.5, head, fontsize=16, weight='bold', va='center', color=col)
    for i, it in enumerate(items):
        ax.text(63, y0 - 9 - i * 5.2, '・' + it, fontsize=15, va='center', color=BLACK)
fig.text(0.5, 0.05, '問2は計算がいらないので最後に落ち着いて。登記の目的と各筆の地積は、面積を出して公差と比べるまで書かない。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'R1_dai21mon_zu13_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図13: 整理図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
