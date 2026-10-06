"""平成22年度 第21問（土地）会話形式note記事の解説図23枚を、座標値から作図する。

`../prompt_H22_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../H23/Q21/zu/draw_H23_dai21mon_kaisetsuzu.py`。

建物・7番1・7番2・5番1・道路の形は座標がないので描かない（隣接地の地番と「道　路」を文字で示すだけ）。
F点の鉄鋲は `tools/zu_helpers.py` の `point(p, 'byou')`（白抜きの丸に十字。2026-09-30、この年度で追加）で描く。

実行: python3 note-articles-Kijyutsu/H22/Q21/zu/draw_H22_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, dms, to_dms, area, chiseki, radial, intersect  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Polygon  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文のA市基準点成果表・測量によって得られた座標・地積測量図のメモ、記事で求めた点） ----------
T1, T2, T3 = P(510.94, 507.05), P(510.98, 464.24), P(510.51, 482.27)
A, B, E, H, I, M = P(513.27, 465.77), P(533.99, 466.99), P(531.51, 504.65), P(532.42, 503.38), P(514.61, 502.57), P(532.88, 477.98)
MEMO = {'A1': P(212.45, 161.82), 'A2': P(193.23, 183.97), 'A3': P(211.47, 184.61), 'A4': P(214.63, 180.20),
        'A6': P(213.95, 146.95), 'A8': P(193.23, 145.73), 'A10': P(193.23, 164.12)}
G = r2(radial(T3, T2, 3.345, dms(122, 54, 34)))
L = r2(radial(T3, T2, 12.323, dms(165, 33, 52)))
F = r2(radial(T1, T3, 3.830, dms(38, 27, 45)))
J = r2(radial(T1, T3, 6.511, dms(21, 57, 44)))
N = r2(radial(T3, T2, 3.414, dms(52, 26, 32)))
SHIFT = A - MEMO['A8']
C = r2(MEMO['A1'] + SHIFT)
D = r2(MEMO['A4'] + SHIFT)
K = r2(C + (D - C) / abs(D - C) * 10.18)
# 誤りの点
ccw = lambda st, bs, d, a: r2(st + cmath.rect(d, cmath.phase(bs - st) - a))  # noqa: E731
GW = ccw(T3, T2, 3.345, dms(122, 54, 34))
LW = ccw(T3, T2, 12.323, dms(165, 33, 52))
FW = ccw(T1, T3, 3.830, dms(38, 27, 45))
JW = ccw(T1, T3, 6.511, dms(21, 57, 44))
KW = C + 10.18j                                   # 北の辺も真東と決めつけて、Yだけ10.18足した誤り

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('G', G, P(513.27, 484.16)), ('L', L, P(513.27, 494.28)), ('F', F, P(513.27, 504.01)),
                     ('J', J, P(513.27, 500.97)), ('C', C, P(532.49, 481.86)), ('D', D, P(534.67, 500.24)),
                     ('K', K, P(533.69, 491.97)), ('GW', GW, P(507.66, 484.01)), ('LW', LW, P(507.13, 494.12)),
                     ('FW', FW, P(508.51, 504.09)), ('JW', JW, P(508.40, 501.05)), ('KW', KW, P(532.49, 492.04)),
                     ('SHIFT', SHIFT, P(320.04, 320.04))]:
    assert abs(got - want) < 1e-9, (n, got, want)
assert abs((E - A) / (MEMO['A3'] - MEMO['A8']) - 1) < 1e-12              # 比は1（平行移動だけ）
assert r2(MEMO['A10'] + SHIFT) == G and r2(MEMO['A2'] + SHIFT) == F and r2(MEMO['A6'] + SHIFT) == B
assert all(abs(p.real - 513.27) < 1e-9 for p in (A, N, G, L, J, F))     # 南の辺は X＝513.27
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = [(C, K, '10.18'), (K, D, '8.33'), (D, E, '5.43'), (E, F, '18.25'), (F, L, '9.73'), (L, G, '10.12'),
         (G, C, '19.36')]
for p, q, want in SIDES + [(K, L, '20.55')]:
    assert d2(p, q) == want, (p, q, d2(p, q), want)
PB = [C, K, L, G]                      # (B)部分
PC = [K, D, E, F, L]                   # (C)部分
P62 = [C, D, E, F, G]                  # 分筆前の6番2（地積測量図の線）
P62_CITY = [C, D, H, I, J, G]          # 道路管理図の線で囲んだ誤り
P61 = [B, C, G, A]                     # 6番1
STRIP = [H, E, F, J, I]                # 拡幅で道路になる予定の帯
assert f'{area(PB):.4f}' == '201.8623' and chiseki(area(PB)) == 201.86
assert f'{area(PC):.2f}' == '230.91' and chiseki(area(PC)) == 230.91
assert f'{area(P62):.4f}' == '432.7642' and chiseki(area(P62)) == 432.76
assert f'{area(P62_CITY):.5f}' == '405.48785' and chiseki(area(P62_CITY)) == 405.48
assert abs(area([MEMO[k] for k in ('A1', 'A4', 'A3', 'A2', 'A10')]) - area(P62)) < 1e-6
assert d2(H, E) == '1.56' and d2(H, I) == '17.83' and d2(I, J) == '2.09'
assert to_dms(cmath.phase(T2 - T3) + 2 * math.pi) == '271°29′35.62″'
assert to_dms(cmath.phase(T3 - T1) + 2 * math.pi) == '269°00′21.11″'
assert to_dms(cmath.phase(D - C)) == '83°14′09.27″'
# 誤りの点の向き：反時計回りの点はどれも T2・T3 より南（道路の向こう）。KW は直線CDより南へ1.20m
assert all(p.real < T3.real for p in (GW, LW, FW, JW))
dist_kw = abs(((D - C).conjugate() * (KW - C)).imag) / abs(D - C)
assert f'{dist_kw:.2f}' == '1.20' and KW.real < (C + (D - C) * ((KW.imag - C.imag) / (D - C).imag)).real
INNER = centroid(P62)
print('数値の照合: すべて一致')


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


def fixed_figure(title, caption, h=12):
    setup_font()
    f = plt.figure(figsize=(16, h), dpi=100)
    f.patch.set_facecolor('white')
    f.suptitle(title, fontsize=24, weight='bold', y=0.965)
    a = f.add_axes([0.03, 0.10, 0.94, 0.80])
    a.set_xlim(0, 100)
    a.set_ylim(0, 100)
    a.axis('off')
    f.text(0.5, 0.035, caption, ha='center', va='center', fontsize=16)
    return f, a


def bearing(p, q):
    """pからqへの方向角（北から時計回り、度。0〜360）。"""
    b = math.degrees(cmath.phase(q - p))
    return b + 360 if b < 0 else b


KIND = {'A': 'metal', 'B': 'concrete', 'C': 'concrete', 'D': 'concrete', 'E': 'concrete', 'F': 'byou', 'G': 'concrete',
        'H': 'concrete', 'I': 'concrete', 'J': 'concrete', 'K': 'metal', 'L': 'metal', 'M': 'metal', 'N': 'metal'}
PTS = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 'K': K, 'L': L, 'M': M, 'N': N}
ALL_PROBLEMS = []

# =====================================================================
# 図1：全体像（北を上にして座標どおりに描き直した見取図）
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像',
                        '南の辺のA・N・G・L・J・Fは、どれもX座標が513.27（真東西の一直線）。H・I・J（灰色）はA市の道路拡幅の杭で、\n'
                        'H→E→F→J→Iの帯（斜線）が、拡幅で道路になる予定の部分。点線K→LとM→Nが遺産分割の分割線。')
z = Zu(ax, fontsize=14)
fit(ax, [T1, T2, T3, A, B, C, D, E, F, P(536.0, 470.0), P(524.0, 461.3)], margin=0.05, pad_aspect=True)
z.poly(P61, fill=BLUE)
z.poly(P62, fill=ORANGE, lw=2.6)
z.ax.add_patch(Polygon([xy(p) for p in STRIP], closed=True, facecolor='none', edgecolor=GRAY, hatch='///', lw=0, zorder=1))
z.poly([H, I, J], color=GRAY, lw=1.6, ls='--', closed=False)
z.line(K, L, color=RED, lw=1.8, ls=':')
z.line(M, N, color=GRAY, lw=1.6, ls=':')
z.line(C, C + P(3.0, 0.35), color=BLACK, lw=1.4)
z.line(A, A + P(-1.2, -2.0), color=GRAY, lw=1.0)
z.line(F, F + P(0, 2.2), color=GRAY, lw=1.0)
z.line(E, E + P(3.2, 0.1), color=GRAY, lw=1.0)
z.north_arrow()
for n in 'ABCDEFGKLMN':
    z.point(PTS[n], KIND[n], color=RED if n in 'CDK' else BLACK)
for n in 'HIJ':
    z.point(PTS[n], KIND[n], color=GRAY)
for p, n in [(T1, 'T1'), (T2, 'T2'), (T3, 'T3')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=p + P(1, 0))
for n in 'ABCDEFGKLMN':
    z.point_label(PTS[n], n, away=INNER if n in 'CDEFKL' else centroid(P61), color=RED if n in 'CDK' else BLACK)
for n in 'HIJ':
    z.point_label(PTS[n], n, away=INNER, color=GRAY)
z.free_text(centroid(P61), '6番1\n(A)(D)', fs=15, offsets=((0, 0), (0, -16), (16, 0)))
z.free_text(centroid(PC) + P(1.5, -1.5), '6番2（本件土地）\n(B)(C)', fs=15, offsets=((0, 0), (0, 16), (-16, 0)))
z.free_text(P(535.8, 473.0), '7－1', fs=14, color=GRAY, offsets=((0, 0), (0, 12), (12, 0)))
z.free_text(P(537.3, 492.0), '7－2', fs=14, color=GRAY, offsets=((0, 0), (0, 12), (12, 0)))
z.free_text(P(524.0, 463.4), '5－1', fs=14, color=GRAY, offsets=((0, 0), (-12, 0), (0, 12)))
z.free_text(P(511.9, 474.0), '道　路', fs=15, color=GRAY, offsets=((0, 0), (0, -12), (20, 0)))
z.free_text(P(524.0, 507.2), '道\n路', fs=15, color=GRAY, offsets=((0, 0), (12, 0), (-12, 0)))
z.callout(A + (N - A) * 0.5, 'X＝513.27（真東西）', dirs=(-100, -80, -120), color=GRAY, dists=(40, 55, 70))
z.callout((E + F) / 2 + P(0, -0.6), '帯H→E→F→J→I', dirs=(160, 180, 140), color=GRAY, dists=(60, 80, 100))
ALL_PROBLEMS += save(fig, [z], 'H22_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図3：問1 整理図（固定配置）
# =====================================================================
fig, ax = fixed_figure('図3　問1　東の道路境界は地積測量図の線（筆界は登記された時の線）',
                       '協議・埋標・道路境界承諾書・道路管理図は、どれも道路拡幅の予定線の話。分筆も所有権の移転もされていないので、筆界はD→E→Fのまま。')
TL = [(7, '平成8年3月6日', '6番2の分筆\n地積測量図で\n筆界D→E→F', RED), (27, '平成20年12月15日', '拡幅の協議\n（計画・買収金額）', BLACK),
      (47, '平成21年3月10日', '市コンクリート杭\nH・I・Jを埋標\n道路境界承諾書', BLACK),
      (67, '平成21年4月10日', 'A市の\n道路管理図', BLACK), (88, '今', '北側と交渉中\n工事は未着工\n代金は未払い', GRAY)]
ax.annotate('', xy=(97, 86), xytext=(3, 86), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, head, body, col in TL:
    ax.plot([x], [86], 'o', ms=12, color=col)
    ax.text(x, 90.5, head, ha='center', fontsize=16, weight='bold', color=col)
    ax.text(x, 80, body, ha='center', va='top', fontsize=15, color=BLACK)
BOX2 = [
    (4, 6, 44, 50, '地積測量図の線 D→E→F（採用）', RED,
     ['平成8年の分筆で登記された時の境', '＝ 筆界（不動産登記法第123条第1号の定義）', '現地の境界標と座標が整合',
      '遺産分割の図面にもH・I・Jはない', '→ 地積測量図の道路境界線を採用'], [0, 1, 4]),
    (52, 6, 44, 50, '道路管理図の線 H→I→J（採用しない）', GRAY,
     ['道路拡幅の位置に打った杭の線', '協議・承諾書では筆界は動かない', '帯H→E→F→J→Iは分筆も移転もまだ',
      '工事は未着工 → 今は宅地のまま', '（一部地目変更も要らない）'], [1, 2]),
]
for x, y, w, hh, head, col, lines, red in BOX2:
    ax.add_patch(FancyBboxPatch((x, y), w, hh, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=col, lw=2.0))
    ax.text(x + 2, y + hh - 4, head, fontsize=19, weight='bold', va='center', color=col)
    for i, t in enumerate(lines):
        ax.text(x + 3, y + hh - 12 - i * 7.6, t, fontsize=16, va='center', color=RED if i in red else BLACK)
path = os.path.join(OUT, 'H22_dai21mon_zu03_mon1_seiri.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図3: 整理図（固定配置）\n  →', path)


# =====================================================================
# 図5〜図8：放射（点ごとに1枚）
# =====================================================================
def housha_figure(title, caption, station, back, pt, wrong, dist, obs, st_name, bk_name, pt_name, r,
                  wrong_dirs, pt_dirs, back_txt, obs_txt, zoom, others=(), obs_dirs=(90, 120, 60, 150, 30)):
    """左：後視点まで入れた全体、右：器械点のまわりの拡大（弧・角度・距離・座標の吹き出し）。
    後視点が十数m〜25m、求点が3〜12mなので、1枚に収めると弧と吹き出しが器械点のまわりに集まる（基本フォームの2パネル）。"""
    fig, (ax1, ax2) = new_figure(title, caption, ncols=2, width_ratios=[0.8, 1.2])
    ys = [back.imag, station.imag, pt.imag, wrong.imag]
    s0, s1 = P(513.27, min(ys) - 1.0), P(513.27, max(ys) + 1.0)
    za = Zu(ax1, fontsize=13)
    fit(ax1, [station, back, pt, wrong, s0, s1], margin=0.10, pad_aspect=True)
    za.line(s0, s1, color=GRAY, lw=1.4)
    za.line(station, back, color=BLUE, lw=1.8)
    za.line(station, pt, color=RED, lw=2.6)
    za.line(station, wrong, color=GRAY, lw=1.3, ls='--')
    za.north_arrow()
    za.point(station, 'kijun')
    za.point(back, 'kijun')
    za.point(pt, 'dot', color=RED, size=9)
    za.point(wrong, 'dot', color=GRAY, size=7)
    for q, qn in others:
        za.point(q, KIND[qn], color=GRAY)
    za.point_label(back, bk_name, away=station)
    za.point_label(station, st_name, away=pt)
    za.point_label(pt, pt_name, away=station, color=RED)
    za.point_label(wrong, '誤り', away=station, color=GRAY, weight='normal')
    for q, qn in others:
        za.point_label(q, qn, away=q + P(-1, 0), color=GRAY)
    za.free_text((s0 + s1) / 2, '南の辺 X＝513.27', color=GRAY, fs=12, offsets=((0, 12), (0, -12), (40, 12), (-40, 12)))
    ax1.set_title('全体（後視点まで）', fontsize=17, weight='bold', pad=6)
    zb = Zu(ax2, fontsize=14)
    fit(ax2, [station + P(zoom[0], zoom[1]), station + P(zoom[2], zoom[3])], margin=0.0, pad_aspect=True)
    x0, x1 = ax2.get_xlim()
    zb.line(P(513.27, x0), P(513.27, x1), color=GRAY, lw=1.4)
    b_back = bearing(station, back)
    reach = min(abs(zoom[1]), abs(zoom[3]), abs(zoom[0]), abs(zoom[2])) * 0.95
    zb.line(station, station + (back - station) / abs(back - station) * reach, color=BLUE, lw=1.8)
    zb.line(station, station + P(r * 1.45, 0), color=GRAY, lw=1.2, ls='--')
    zb.line(station, pt, color=RED, lw=2.8)
    zb.line(station, wrong, color=GRAY, lw=1.4, ls='--')
    zb.angle_arc(station, r * 0.55, 0, b_back, color=BLUE)
    zb.angle_arc(station, r, b_back, b_back + obs, color=RED)
    zb.north_arrow()
    zb.point(station, 'kijun')
    zb.point(pt, 'dot', color=RED, size=11)
    zb.point(wrong, 'dot', color=GRAY, size=9)
    zb.point_label(station, st_name, away=pt)
    zb.callout(pt, f'{pt_name}（{pt.real:.2f}, {pt.imag:.2f}）', dirs=pt_dirs, color=RED, dists=(45, 60, 80, 100))
    zb.callout(wrong, f'反時計回りの誤り\n（{wrong.real:.2f}, {wrong.imag:.2f}）', dirs=wrong_dirs, color=GRAY,
               dists=(40, 55, 75, 95))
    zb.edge_label(station, pt, f'{dist}', station + (back - station) * 0.3, color=RED, fs=15)
    mid_b = station + cmath.rect(r * 0.55, math.radians(b_back / 2))
    mid_o = station + cmath.rect(r, math.radians(b_back + obs / 2))
    zb.callout(mid_b, back_txt, dirs=(-135, -45, -90, 180, 0), color=BLUE, dists=(45, 65, 85, 110))
    zb.callout(mid_o, obs_txt, dirs=obs_dirs, color=RED, dists=(40, 60, 80, 100))
    ax2.set_title(f'器械点{st_name}のまわりの拡大', fontsize=17, weight='bold', pad=6)
    return fig, (za, zb)


fig, z = housha_figure(
    '図4　G点の求め方（T3からT2を後視して放射）',
    'T3→T2の方向角 −88°30′24.38″（360°を足して271°29′35.62″）に、時計回りの観測角 122°54′34″ を足して 394°24′09.62″ ＝ 34°24′09.62″\n'
    '（真数表の34°24′10″）。3.345m進んでG（513.27, 484.16）。反時計回りに引くと（507.66, 484.01）で、道路の向こうに出る。',
    T3, T2, G, GW, '3.345', 122 + 54 / 60 + 34 / 3600, 'T3', 'T2', 'G', 1.4,
    (-60, -30, -90, 0), (0, 30, -30, 60), '方向角 271°29′35.62″', '観測角 122°54′34″（時計回り）', (-4.6, -4.0, 4.4, 4.5),
    others=[(A, 'A')])
ALL_PROBLEMS += save(fig, list(z), 'H22_dai21mon_zu04_G_housha.png')

fig, z = housha_figure(
    '図5　L点の求め方（T3からT2を後視して放射）',
    'T3→T2の方向角 271°29′35.62″ ＋ 観測角 165°33′52″ ＝ 437°03′27.62″ ＝ 77°03′27.62″（真数表の77°03′28″）。\n'
    '12.323m進んでL（513.27, 494.28）。GもLも南の辺のX＝513.27に並ぶ。反時計回りだと（507.13, 494.12）で道路の向こう。',
    T3, T2, L, LW, '12.323', 165 + 33 / 60 + 52 / 3600, 'T3', 'T2', 'L', 2.2,
    (-60, -30, -90, 0), (60, 30, 90, 0), '方向角 271°29′35.62″', '観測角 165°33′52″（時計回り）', (-5.5, -4.5, 5.0, 14.0),
    others=[(A, 'A'), (G, 'G')])
ALL_PROBLEMS += save(fig, list(z), 'H22_dai21mon_zu05_L_housha.png')

fig, z = housha_figure(
    '図6　F点の求め方（T1からT3を後視して放射）',
    'T1→T3の方向角 −90°59′38.89″（269°00′21.11″）＋ 観測角 38°27′45″ ＝ 307°28′06.11″。真数表の127°28′06″は、その180°逆の角。\n'
    '3.830m進んでF（513.27, 504.01）。器械点が変わったら後視の向きは arg(T3 − T1) で取り直す。反時計回りだと（508.51, 504.09）。',
    T1, T3, F, FW, '3.830', 38 + 27 / 60 + 45 / 3600, 'T1', 'T3', 'F', 1.4,
    (-120, -150, -90, 180), (90, 120, 60, 150), '方向角 269°00′21.11″', '観測角 38°27′45″（時計回り）', (-4.4, -5.0, 4.4, 3.4),
    others=[(L, 'L'), (G, 'G')])
ALL_PROBLEMS += save(fig, list(z), 'H22_dai21mon_zu06_F_housha.png')

fig, z = housha_figure(
    '図7　J点の求め方（T1からT3を後視して放射。問1の裏付けに使う参考の点）',
    'T1→T3の方向角 269°00′21.11″ ＋ 観測角 21°57′44″ ＝ 290°58′05.11″（真数表の110°58′05″はその180°逆）。\n'
    '6.511m進んでJ（513.27, 500.97）。LとFの間の南の辺に乗る。A市の杭なので、6番2の筆界点ではない（答えには要らない）。',
    T1, T3, J, JW, '6.511', 21 + 57 / 60 + 44 / 3600, 'T1', 'T3', 'J', 1.6,
    (-120, -150, -90, 180), (90, 120, 60, 150), '方向角 269°00′21.11″', '観測角 21°57′44″（時計回り）', (-4.4, -8.0, 4.4, 3.4),
    others=[(L, 'L'), (F, 'F')], obs_dirs=(-160, 180, -140, 160, -120))
ALL_PROBLEMS += save(fig, list(z), 'H22_dai21mon_zu07_J_housha.png')

# =====================================================================
# 図8：座標変換の確かめ（地積測量図のメモ ⇔ 今回の座標）
# =====================================================================
fig, (ax1, ax2) = new_figure('図8　座標変換の確かめ（共通点2つで比が1＝平行移動だけ）',
                             '左の地積測量図のメモ（任意座標）のA8→A3と、右の今回の座標のA→Eは、どちらも 18.24 ＋ 38.88i。比 (E − A) ÷ (A3 − A8) ＝ 1 なので、\n'
                             '回転も縮尺の違いもない。ずれは A − A8 ＝ 320.04 ＋ 320.04i。A10・A2・A6をずらすと、今回のG・F・Bと一致する。',
                             ncols=2)
m = MEMO
memo62 = [m['A1'], m['A4'], m['A3'], m['A2'], m['A10']]
memo61 = [m['A6'], m['A1'], m['A10'], m['A8']]
for axx, pts62, pts61, lab, v0, v1, names, title in [
        (ax1, memo62, memo61, 'メモ', m['A8'], m['A3'], [('A1', m['A1']), ('A4', m['A4']), ('A3', m['A3']), ('A2', m['A2']),
                                                           ('A10', m['A10']), ('A6', m['A6']), ('A8', m['A8'])], '地積測量図のメモ（任意座標）'),
        (ax2, P62, P61, '今回', A, E, [('C', C), ('D', D), ('E', E), ('F', F), ('G', G), ('B', B), ('A', A)], '今回の測量の座標')]:
    zz = Zu(axx, fontsize=14)
    fit(axx, pts62 + pts61, margin=0.18, pad_aspect=True)
    zz.poly(pts61, fill=BLUE)
    zz.poly(pts62, fill=ORANGE)
    zz.line(v0, v1, color=RED, lw=2.4)
    zz.north_arrow()
    cen = centroid(pts62 + pts61[:1])
    for n, p in names:
        zz.point(p, 'dot', size=7)
    for n, p in names:
        zz.point_label(p, n, away=centroid(pts61 + pts62), weight='bold')
    zz.edge_label(v0, v1, '18.24 ＋ 38.88i', v0 + P(10, -5), color=RED, fs=15, ts=(0.5, 0.4, 0.6, 0.3), dists=(12, 20, 30))
    axx.set_title(title, fontsize=18, weight='bold', pad=6)
    ALL_PROBLEMS += zz.check_overlaps(f'図8 {lab}')
path = os.path.join(OUT, 'H22_dai21mon_zu08_zahyou_henkan.png')
fig.savefig(path, dpi=100, facecolor='white')
print('  →', path)


# =====================================================================
# 図9・図10：C点・D点（A8から見た向きと長さはメモも今回も同じ）
# =====================================================================
def heikou_figure(title, caption, pt, key, vec_txt, name, dirs, extra_checks=()):
    fig, (ax,) = new_figure(title, caption)
    z = Zu(ax, fontsize=14)
    fit(ax, P62 + P61 + [T3, P(537.6, 496.0)], margin=0.08, pad_aspect=True)
    z.poly(P61, fill=BLUE)
    z.poly(P62, fill=ORANGE)
    z.line(A, pt, color=RED, lw=2.4, ls='--')
    z.north_arrow()
    for n in 'ABEFG':
        z.point(PTS[n], KIND[n])
    z.point(pt, 'dot', color=RED, size=11)
    z.callout(pt, f'{name}（{pt.real:.2f}, {pt.imag:.2f}）\n＝ {key} ＋ ずれ', dirs=dirs, color=RED, dists=(50, 70, 90))
    z.edge_label(A, pt, vec_txt, P(510, 490), color=RED, fs=14, ts=(0.5, 0.4, 0.6, 0.3), dists=(12, 20, 30))
    for q, txt, qdirs in extra_checks:
        z.callout(q, txt, dirs=qdirs, color=GREEN, dists=(50, 70, 90))
    for n in 'ABEFG':
        z.point_label(PTS[n], n, away=centroid(P62 + P61))
    other = D if pt == C else C
    z.point(other, 'concrete', color=GRAY)
    z.point_label(other, 'D' if pt == C else 'C', away=INNER, color=GRAY)
    z.free_text(centroid(P61) + P(-5.0, -3.0), '6番1', fs=15, offsets=((0, 0), (0, -16), (-16, 0), (0, -32)))
    z.free_text(centroid(PC), '6番2', fs=15, offsets=((0, 0), (0, -16), (16, 0)))
    return fig, z


fig, z = heikou_figure('図9　問2　C点の求め方（A1を平行移動）',
                       'C ＝ A1 ＋ (A − A8) ＝ 212.45 ＋ 161.82i ＋ 320.04 ＋ 320.04i ＝ 532.49 ＋ 481.86i。\n'
                       'A→Cの差（19.22 ＋ 16.09i）は、メモのA8→A1の差と同じ。Cは7－1と7－2の境の南の端（6番1と6番2の境の北の端）。',
                       C, 'A1', 'A1 − A8 ＝ 19.22 ＋ 16.09i', 'C', (150, 120, 170))
ALL_PROBLEMS += save(fig, [z], 'H22_dai21mon_zu09_C_heikou.png')

fig, z = heikou_figure('図10　問2　D点の求め方（A4を平行移動）',
                       'D ＝ A4 ＋ (A − A8) ＝ 214.63 ＋ 180.20i ＋ 320.04 ＋ 320.04i ＝ 534.67 ＋ 500.24i。\n'
                       '検算：A10・A2をずらすと（513.27, 484.16）（513.27, 504.01）で、放射のG・Fとぴったり一致する。',
                       D, 'A4', 'A4 − A8 ＝ 21.40 ＋ 34.47i', 'D', (60, 30, 90),
                       extra_checks=[(G, 'A10 ＋ ずれ ＝ G', (-110, -130, -90)), (F, 'A2 ＋ ずれ ＝ F', (-60, -80, -40))])
ALL_PROBLEMS += save(fig, [z], 'H22_dai21mon_zu10_D_heikou.png')

# =====================================================================
# 図11：問2 K点（CからDの向きに10.18m）。右は拡大
# =====================================================================
fig, (ax1, ax2) = new_figure('図11　問2　K点の求め方（Cが出発点、D − C の向きに10.18m）',
                             'K ＝ C ＋ (D − C) ÷ Abs(D − C) × 10.18 ＝（533.69, 491.97）。D − C ＝ 2.18 ＋ 18.38i で、北の辺は真東ではない（方向角83°14′09.27″）。\n'
                             '南の辺につられてYだけ10.18足すと（532.49, 492.04）で、直線CDより1.20m南の6番2の中に落ちる。',
                             ncols=2, width_ratios=[1.1, 0.9])
za = Zu(ax1, fontsize=14)
fit(ax1, P62 + [L], margin=0.10, pad_aspect=True)
za.poly(P62, fill=ORANGE)
za.line(C, D, color=RED, lw=2.8)
za.line(K, L, color=RED, lw=1.6, ls=':')
za.north_arrow()
for n in 'CDEFGL':
    za.point(PTS[n], KIND[n])
za.point(K, 'dot', color=RED, size=11)
za.callout(K, 'K（533.69, 491.97）', dirs=(90, 60, 120), color=RED, dists=(45, 60, 80))
za.edge_label(C, K, '10.18', INNER, color=RED, fs=15)
za.edge_label(C, D, 'CD 18.5088…', INNER, color=GRAY, fs=13, outward=False, ts=(0.75, 0.8, 0.7))
for n in 'CDEFGL':
    za.point_label(PTS[n], n, away=INNER)
zb = Zu(ax2, fontsize=14)
fit(zb.ax, [K + P(-1.8, -1.4), K + P(0.6, 1.4)], margin=0.02, pad_aspect=True)
u = (D - C) / abs(D - C)
zb.line(K - u * 1.6, K + u * 1.4, color=RED, lw=2.4)
zb.line(KW, KW + P(0, -1.2), color=GRAY, lw=1.2, ls='--')
zb.north_arrow()
zb.point(K, 'dot', color=RED, size=11)
zb.callout(K, 'K（533.69, 491.97）', dirs=(90, 60, 120), color=RED, dists=(40, 55, 70))
zb.point(KW, 'dot', color=GRAY, size=10)
zb.callout(KW, 'Yだけ足した誤り\n（532.49, 492.04）', dirs=(-90, -60, -120), color=GRAY, dists=(40, 55, 70))
foot = C + u * ((u.conjugate() * (KW - C)).real)
zb.line(KW, foot, color=GRAY, lw=1.4, ls=':')
zb.free_text((KW + foot) / 2, '1.20m', color=GRAY, fs=15, offsets=((34, 0), (-34, 0), (40, 16)))
zb.free_text(K + u * 1.0, '直線CD', color=RED, fs=14, offsets=((0, 18), (0, -18), (20, 20)))
ax2.set_title('Kのまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H22_dai21mon_zu11_K_ten.png')

# =====================================================================
# 図12：(B)(C)の面積の求め方（2パネル）
# =====================================================================
fig, (ax1, ax2) = new_figure('図12　問3　(B)部分と(C)部分の面積の求め方',
                             '左：(B)は四角形C→K→L→G。対角線どうしの Conjg(L − C) × (G − K) ＝ 295.4722 ＋ 403.7246i で、201.8623 → 201.86㎡。\n'
                             '右：(C)は五角形K→D→E→F→L。Lを原点にずらした3つの三角形の和 976.2617 − 461.82i で、230.91㎡。',
                             ncols=2)
za = Zu(ax1, fontsize=14)
fit(ax1, P62, margin=0.12, pad_aspect=True)
za.poly(PC, color=GRAY, lw=1.4)
za.poly(PB, fill=BLUE, lw=2.4)
za.line(C, L, color=BLUE, lw=1.8, ls='--')
za.line(K, G, color=BLUE, lw=1.8, ls='--')
za.north_arrow()
for n in 'CKLG':
    za.point(PTS[n], KIND[n])
    za.point_label(PTS[n], n, away=centroid(PB))
OB = intersect(C, L, K, G)[0]
za.free_text(centroid([G, L, OB]), '(B)\n201.8623㎡', fs=16, color=BLUE, weight='bold', offsets=((0, 0), (0, -12), (0, 12)))
zb = Zu(ax2, fontsize=14)
fit(ax2, P62, margin=0.12, pad_aspect=True)
zb.poly(PB, color=GRAY, lw=1.4)
tri_cols = [ORANGE, GREEN, PURPLE]
for (p, q), col in zip([(K, D), (D, E), (E, F)], tri_cols):
    zb.poly([L, p, q], color=col, lw=1.2, fill=col, alpha=0.25)
zb.poly(PC, lw=2.4)
zb.north_arrow()
for n in 'KDEFL':
    zb.point(PTS[n], KIND[n])
    zb.point_label(PTS[n], n, away=centroid(PC))
zb.callout(L, 'L（原点にずらす）', dirs=(-100, -80, -120), color=RED, dists=(40, 55, 70))
zb.free_text(centroid([L, K, D]), '(C)\n230.91㎡', fs=16, color=BLACK, weight='bold', offsets=((0, 0), (0, -14), (-14, 0), (10, 10)))
ALL_PROBLEMS += save(fig, [za, zb], 'H22_dai21mon_zu12_menseki.png')

# =====================================================================
# 図15：東の道路境界の比較（地積測量図の線 ⇔ 道路管理図の線）
# =====================================================================
fig, (ax1, ax2) = new_figure('図15　問1の数字の裏付け（地積測量図の線 ⇔ 道路管理図の線）',
                             '左：D→E→Fで囲むと432.7642 → 432.76㎡で、平成8年の地積測量図（登記記録）と一致。\n'
                             '右：道路管理図のH→I→J（HE 1.56・HI 17.83・IJ 2.09は道路管理図の数字と一致）で囲むと405.48785 → 405.48㎡で、27.28㎡足りない（誤差の限度2.01㎡を大きく超える）。',
                             ncols=2)
for axx, poly, lab, col, ttl in [(ax1, P62, '432.7642㎡\n→ 432.76㎡', GREEN, '地積測量図の線（採用）'),
                                 (ax2, P62_CITY, '405.48785㎡\n→ 405.48㎡', GRAY, '道路管理図の線（採用しない）')]:
    zz = Zu(axx, fontsize=14)
    fit(axx, P62 + [H, I, J], margin=0.12, pad_aspect=True)
    if poly is P62_CITY:
        zz.ax.add_patch(Polygon([xy(p) for p in STRIP], closed=True, facecolor='none', edgecolor=RED, hatch='///', lw=0, zorder=1))
        zz.poly([D, E, F, J], color=GRAY, lw=1.2, ls=':', closed=False)
    zz.poly(poly, fill=col, lw=2.4)
    zz.north_arrow()
    names = 'CDEFG' if poly is P62 else 'CDHIJG'
    for n in names:
        zz.point(PTS[n], KIND[n], color=GRAY if n in 'HIJ' else BLACK)
    if poly is P62_CITY:
        zz.edge_label(H, E, '1.56', centroid(P62), fs=13, color=RED)
        zz.edge_label(H, I, '17.83', centroid(P62), fs=13, color=RED, outward=False)
        zz.edge_label(I, J, '2.09', centroid(P62), fs=13, color=RED, outward=False, dists=(12, 18, 26))
        zz.callout((H + I) / 2 + P(0, 0.4), 'H→E→F→J→I\nの帯（27.27635㎡）', dirs=(150, 170, 130, 190), color=RED, dists=(60, 80, 100, 130))
    for n in names:
        zz.point_label(PTS[n], n, away=centroid(poly), color=GRAY if n in 'HIJ' else BLACK)
    zz.free_text(centroid(poly), lab, fs=17, weight='bold', color=BLACK, offsets=((0, 0), (-14, 0), (0, -16)))
    axx.set_title(ttl, fontsize=18, weight='bold', pad=6, color=RED if poly is P62 else GRAY)
    ALL_PROBLEMS += zz.check_overlaps(f'図15 {ttl}')
path = os.path.join(OUT, 'H22_dai21mon_zu15_kyoukai_hikaku.png')
fig.savefig(path, dpi=100, facecolor='white')
print('  →', path)

# =====================================================================
# 図14：誤差の限度の判定（数直線。固定配置）。0.01㎡の結論の直後に置く
# =====================================================================
fig, ax = fixed_figure('図14　問3　誤差の限度の判定（6番2は2.01㎡）',
                       '比べるのは、分筆前の地積（登記記録432.76）と分筆後の地積の合計（201.86 ＋ 230.91 ＝ 432.77）。\n'
                       '差0.01㎡は、問題文の注5の誤差の限度2.01㎡（範囲430.75〜434.77）の内側なので、地積の更正は要らない。', h=9)
lo, hi, y0 = 430, 435.5, 46
sx = lambda v: 6 + (v - lo) / (hi - lo) * 88  # noqa: E731
ax.plot([6, 94], [y0, y0], color=BLACK, lw=2)
for tv in [430, 431, 432, 433, 434, 435]:
    ax.plot([sx(tv), sx(tv)], [y0 - 1.5, y0 + 1.5], color=BLACK, lw=1.2)
    ax.text(sx(tv), y0 - 5, f'{tv}', ha='center', va='top', fontsize=13, color=GRAY)
ax.add_patch(plt.Rectangle((sx(430.75), y0 - 3), sx(434.77) - sx(430.75), 6, color=GREEN, alpha=0.25, lw=0))
ax.plot([sx(432.76)], [y0], 'o', ms=12, color=BLACK)
ax.plot([sx(432.77)], [y0], 'o', ms=12, color=BLUE)
ax.text(sx(432.76) - 1, y0 + 8, '登記記録 432.76', ha='right', va='bottom', fontsize=16, color=BLACK)
ax.text(sx(432.77) + 1, y0 + 8, '分筆後の合計 432.77（差0.01）', ha='left', va='bottom', fontsize=16, color=BLUE)
ax.text(sx(430.75), y0 - 14, '432.76 − 2.01 ＝ 430.75', ha='center', va='top', fontsize=15, color=GREEN)
ax.text(sx(434.77), y0 - 14, '432.76 ＋ 2.01 ＝ 434.77', ha='center', va='top', fontsize=15, color=GREEN)
ax.text(50, 80, '誤差の限度の範囲（緑）の内側 → 地積の更正は要らない（不動産登記事務取扱手続準則第72条第1項）',
        ha='center', fontsize=17, weight='bold', color=GREEN)
ax.text(50, 14, '合計が432.77で1つ多いのは、丸めたKとそれぞれの切り捨ての分', ha='center', fontsize=15, color=GRAY)
path = os.path.join(OUT, 'H22_dai21mon_zu14_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図14: 判定図（固定配置）\n  →', path)

# =====================================================================
# 図17：問3 分筆後の区画と地番
# =====================================================================
fig, (ax,) = new_figure('図17　問3　分筆後の区画と地番（(B)＝6番2、(C)＝6番4）',
                        'どちらに元の6番2を残すかを決めた規定はない。(B)には敏夫さんの建物（6番1と6番2にまたがる建物）がかかるので、\n'
                        '(B)に6番2を残して(C)を6番4にすれば、建物の所在の地番とも食い違わない。(B)201.86 ＋ (C)230.91 ＝ 432.77。')
z = Zu(ax, fontsize=14)
fit(ax, P62 + [T3, T1, P(538.2, 474.0)], margin=0.06, pad_aspect=True)
z.poly(PB, fill=BLUE, lw=2.4)
z.poly(PC, fill=ORANGE, lw=2.4)
z.line(K, L, color=RED, lw=2.8)
z.line(C, C + P(3.0, 0.35), color=BLACK, lw=1.4)
z.north_arrow()
for n in 'CKDEFLG':
    z.point(PTS[n], KIND[n])
    z.point_label(PTS[n], n, away=INNER)
z.free_text(centroid(PB), '(B)\n6番2\n201.86㎡', fs=17, weight='bold', color=BLUE, offsets=((0, 0), (0, -16), (-16, 0)))
z.free_text(centroid(PC) + P(0.5, -1.0), '(C)\n6番4\n230.91㎡', fs=17, weight='bold', color=ORANGE, offsets=((0, 0), (0, -16), (16, 0)))
z.callout((K + L) / 2, '分割線 K→L（20.55）', dirs=(-60, -40, -80), color=RED, dists=(60, 80, 100))
z.callout(C + (G - C) * 0.35, '敏夫さんの建物は\n6番1と(B)にまたがる', dirs=(180, 160, -160), color=GRAY, dists=(60, 80, 100))
z.free_text(P(536.2, 474.0), '7－1', fs=14, color=GRAY, offsets=((0, 0), (0, 12), (12, 0)))
z.free_text(P(537.5, 490.5), '7－2', fs=14, color=GRAY, offsets=((0, 0), (0, 12), (12, 0)))
z.free_text(P(522.0, 478.8), '6－1', fs=14, color=GRAY, offsets=((0, 0), (-14, 0), (0, 12)))
z.free_text(P(511.6, 490.0), '道　路', fs=15, color=GRAY, offsets=((0, 0), (0, -12), (20, 0)))
z.free_text(P(522.0, 507.0), '道\n路', fs=15, color=GRAY, offsets=((0, 0), (12, 0), (-12, 0)))
ALL_PROBLEMS += save(fig, [z], 'H22_dai21mon_zu17_bunpitsu_chiban.png')

# =====================================================================
# 図19：問3 成年被後見人の良子は成年後見人が代表する（申請人の欄の書き方。固定配置）
# =====================================================================
fig, ax = fixed_figure('図19　問3　成年被後見人の良子は、成年後見人の木村光江が代表して申請する',
                       '成年後見人は被後見人の財産に関する法律行為について被後見人を代表する（民法第859条第1項）。代理人によって申請するときは、\n'
                       '代理人の氏名・住所も申請情報になる（不動産登記令第3条第3号）。問題文が木村光江の住所まで書いているのが、書かせる合図。')
ax.add_patch(FancyBboxPatch((6, 62), 30, 26, boxstyle='round,pad=0.6', fc='#fff5f5', ec=RED, lw=2.0))
ax.text(21, 82, '杉山良子', ha='center', va='center', fontsize=20, weight='bold', color=RED)
ax.text(21, 74, '成年被後見人・相続人', ha='center', va='center', fontsize=15, color=BLACK)
ax.text(21, 67, '6番2の(B)を取得', ha='center', va='center', fontsize=15, color=BLACK)
ax.add_patch(FancyBboxPatch((64, 62), 30, 26, boxstyle='round,pad=0.6', fc='#fff5f5', ec=RED, lw=2.0))
ax.text(79, 82, '木村光江', ha='center', va='center', fontsize=20, weight='bold', color=RED)
ax.text(79, 74, '成年後見人', ha='center', va='center', fontsize=15, color=BLACK)
ax.text(79, 67, 'E市G町四丁目2番1号', ha='center', va='center', fontsize=15, color=BLACK)
ax.annotate('', xy=(37.5, 75), xytext=(62.5, 75), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=RED))
ax.text(50, 79, '代表して申請', ha='center', va='bottom', fontsize=16, weight='bold', color=RED)
ax.text(50, 70, '（遺産分割協議にも\n後見人として押印）', ha='center', va='top', fontsize=13, color=GRAY)
ax.add_patch(FancyBboxPatch((6, 6), 88, 44, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=RED, lw=2.0))
ax.text(9, 45, '申請人の枠の書き方', fontsize=19, weight='bold', va='center', color=RED)
for i, (t_, c_) in enumerate([('申請人（被相続人　杉山太郎）', BLACK), ('　相続人　C市D町二丁目5番6号　杉山良子', BLACK),
                               ('　上記成年後見人　E市G町四丁目2番1号　木村光江', RED), ('　相続人　C市D町三丁目4番6号　杉山健二', BLACK)]):
    ax.text(11, 36 - i * 7.6, t_, fontsize=17, va='center', color=c_)
path = os.path.join(OUT, 'H22_dai21mon_zu19_kouken.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図19: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図22：問4 地積測量図の完成見本（黒、塗りなし）
# =====================================================================
fig, (ax,) = new_figure('図22　問4　地積測量図の完成見本（縮尺1／250）',
                        '1／250で1m ＝ 4mm。辺長は小数第3位を四捨五入（DE 5.4252…→5.43、KD 8.3278…→8.33）。座標値・求積の方法・地積は書かない（問題文の注3）。\n'
                        'T1・T3は位置・名称・座標値を書く（問題文の注4）。H・J（A市の杭）は筆界点ではないので描かない。')
z = Zu(ax, fontsize=13)
fit(ax, P62 + [T1, T3, P(536.8, 479.0), P(508.2, 490.0)], margin=0.05, pad_aspect=True)
z.poly(P62, lw=2.4)
z.line(K, L, lw=2.0)
z.line(C, C + (G - C) * -0.14, lw=1.4)
z.line(C, C + (M - C) / abs(M - C) * 1.8, lw=1.4)
z.line(G, G + P(0, -1.6), lw=1.4)
z.line(F, F + P(0, 1.6), lw=1.4)
z.line(E, E + P(2.2, 0.08), lw=1.4)
z.north_arrow()
for n in 'CKDEFLG':
    z.point(PTS[n], KIND[n])
for p, q, n in SIDES:
    z.edge_label(p, q, n, INNER, fs=13)
z.edge_label(K, L, '20.55', centroid(PC), fs=13, outward=False)
for n in 'CKDEFLG':
    z.point_label(PTS[n], n, away=INNER, weight='normal')
for p, n in [(T1, 'T1'), (T3, 'T3')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=p + P(1, 0), weight='normal')
z.free_text(centroid(PB), '6－2\n(B)', fs=15, offsets=((0, 0), (0, -14), (14, 0)))
z.free_text(centroid(PC), '6－4\n(C)', fs=15, offsets=((0, 0), (0, -14), (14, 0)))
z.free_text(P(535.0, 478.6), '7－1', fs=13, offsets=((0, 0), (0, 12), (-12, 0)))
z.free_text(P(537.0, 491.0), '7－2', fs=13, offsets=((0, 0), (0, 12), (12, 0)))
z.free_text(P(523.0, 478.6), '6－1', fs=13, offsets=((0, 0), (-12, 0), (0, 12)))
z.free_text(P(511.8, 492.0), '道　路', fs=13, offsets=((0, 0), (0, -12), (20, 0)))
z.free_text(P(522.5, 506.6), '道\n路', fs=13, offsets=((0, 0), (12, 0), (-12, 0)))
z.free_text(P(528.5, 510.3), 'C・D・E・G：コンクリート杭\nK・L：金属標\nF：鉄鋲\n（単位：m）', fs=12, ha='left',
            offsets=((0, 0), (0, -12), (-12, 0), (-30, 0)))
z.free_text(P(508.9, 494.0), '基本三角点等の名称及び座標値\nT1　A市基準点T1　X 510.94　Y 507.05\nT3　A市基準点T3　X 510.51　Y 482.27',
            fs=12, offsets=((0, 0), (0, -10), (10, 0), (-20, 0)))
ALL_PROBLEMS += save(fig, [z], 'H22_dai21mon_zu22_sokuryouzu.png')

# =====================================================================
# 図23：本番で解く順番（固定配置）
# =====================================================================
fig, ax = fixed_figure('図23　本番で解く順番（いちばん重いのは(C)の面積と地積測量図）',
                       '座標がなくても、問1の全部と申請書の多くの欄は書ける。1行目の432.76はメモの座標だけで出る。N・Jの放射は答えに要らない。')
STEPS = [('①', '問1を書き切る', '計算なし。結論はD→E→F、理由は「筆界は登記された時の線」「予定線で分筆も移転もまだ」「境界標と整合」', BLACK),
         ('②', '申請書の(B)(C)の地積以外の欄', '土地分筆登記・申請人（良子〈成年後見人木村光江〉と健二）・6番4・原因。1行目の432.76はメモで', BLACK),
         ('③', 'G・L・Fの放射', '時計回りで足す。どれもX＝513.27の南の辺に並ぶ', BLACK),
         ('④', 'C・Dの平行移動とK', '2点で比が1を確かめて、ずれ320.04 ＋ 320.04i。Kは D − C の向きに10.18m', BLACK),
         ('⑤', '(B)(C)の面積と誤差の限度', '201.86・230.91。合計432.77と432.76の差0.01は2.01の範囲内', RED),
         ('⑥', '辺長8本と地積測量図', '10.18・8.33・5.43・18.25・9.73・10.12・19.36・20.55。T1・T3の座標、H・Jは描かない', RED)]
for k, (no, head, body, col) in enumerate(STEPS):
    y = 90 - k * 15.4
    ax.add_patch(FancyBboxPatch((5, y - 5.4), 90, 10.8, boxstyle='round,pad=0.5', fc='#fff5f5' if col == RED else '#f7f7f7',
                                ec=col, lw=2.0))
    ax.text(8, y + 2.0, f'{no}　{head}', fontsize=19, weight='bold', va='center', color=col)
    ax.text(12, y - 2.7, body, fontsize=15, va='center', color=BLACK)
    if k < len(STEPS) - 1:
        ax.annotate('', xy=(50, y - 9.2), xytext=(50, y - 6.3), arrowprops=dict(arrowstyle='-|>', lw=2.0, color=GRAY))
path = os.path.join(OUT, 'H22_dai21mon_zu23_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図23: 整理図（固定配置）\n  →', path)


# =====================================================================
# 図2：問1 帯H→E→F→J→Iは宅地のまま（一部地目変更は要らない）
# =====================================================================
fig, (ax1, ax2) = new_figure('図2　問1　帯H→E→F→J→Iは、工事の前なので宅地のまま',
                             '道路管理図の帯は、拡幅工事に着工しておらず、買収代金も未払い。道路用地の分筆も所有権の移転もされていないので、\n'
                             '今は6番2（杉山太郎の土地）の一部で、家の敷地のまま宅地。一部地目変更も要らない。', ncols=2, width_ratios=[1.0, 1.0])
za = Zu(ax1, fontsize=14)
fit(ax1, P62 + [H, I, J], margin=0.10, pad_aspect=True)
za.poly(P62, fill=ORANGE, lw=2.4)
za.ax.add_patch(Polygon([xy(p) for p in STRIP], closed=True, facecolor='none', edgecolor=GRAY, hatch='///', lw=0, zorder=1))
za.poly([H, I, J], color=GRAY, lw=1.6, ls='--', closed=False)
za.north_arrow()
for n in 'CDEFG':
    za.point(PTS[n], KIND[n])
for n in 'HIJ':
    za.point(PTS[n], KIND[n], color=GRAY)
for n in 'CDEFG':
    za.point_label(PTS[n], n, away=INNER)
for n in 'HIJ':
    za.point_label(PTS[n], n, away=INNER, color=GRAY)
za.callout((H + I) / 2 + P(0, 0.4), '帯H→E→F→J→I\n＝ 6番2の一部・宅地', dirs=(150, 170, 130, 190), color=BLACK, dists=(60, 80, 100, 130))
za.free_text(centroid(P62) + P(0, -2), '6番2（宅地）', fs=17, weight='bold', offsets=((0, 0), (0, -16), (-16, 0)))
ax1.set_title('今の6番2（筆界はD→E→F）', fontsize=17, weight='bold', pad=6)
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 100)
ax2.axis('off')
for x, y, w, hh, head, col, lines in [
        (4, 52, 92, 40, '今（平成22年8月）', RED, ['工事は未着工・買収代金は未払い', '道路用地の分筆も所有権の移転もまだ',
                                              '→ 6番2の一部で、地目は宅地のまま', '→ 一部地目変更は要らない']),
        (4, 6, 92, 36, 'これから（A市の予定）', GRAY, ['北側の土地所有者との協議がまとまったら工事に着工', '工事が完成したら土地の買収代金を支払う',
                                                    '道路として使われるようになってからの話'])]:
    ax2.add_patch(FancyBboxPatch((x, y), w, hh, boxstyle='round,pad=0.6', fc='#fff5f5' if col == RED else '#f7f7f7', ec=col, lw=2.0))
    ax2.text(x + 3, y + hh - 5, head, fontsize=19, weight='bold', va='center', color=col)
    for i, s in enumerate(lines):
        ax2.text(x + 5, y + hh - 13 - i * 7.2, s, fontsize=16, va='center', color=RED if (col == RED and i >= 2) else BLACK)
ALL_PROBLEMS += save(fig, [za], 'H22_dai21mon_zu02_obi_chimoku.png')

# =====================================================================
# 図13：問3 伏せてある6番2の地積（平成8年の地積測量図のメモから）
# =====================================================================
fig, (ax1, ax2) = new_figure('図13　問3　伏せてある6番2の地積は、平成8年の地積測量図から432.76㎡',
                             '登記記録の地積は「××.××」と伏せてある。分筆で登記された6番2の地積は、平成8年の地積測量図のメモ（左）で求積した値。\n'
                             'メモは今の座標を320.04 ＋ 320.04i ずらしただけ（平行移動では面積は変わらない）なので、今の座標でGを原点にした式（右）でも\n'
                             '1500.8657 − 865.5284i → 432.7642 → 432.76㎡。', ncols=2)
memo62 = [MEMO['A1'], MEMO['A4'], MEMO['A3'], MEMO['A2'], MEMO['A10']]
za = Zu(ax1, fontsize=14)
fit(ax1, memo62, margin=0.16, pad_aspect=True)
za.poly(memo62, fill=ORANGE, lw=2.4)
za.north_arrow()
for n, p in zip(['A1', 'A4', 'A3', 'A2', 'A10'], memo62):
    za.point(p, 'dot', size=7)
    za.point_label(p, n, away=centroid(memo62))
za.free_text(centroid(memo62), '6番2\n432.7642㎡', fs=17, weight='bold', offsets=((0, 0), (0, -16), (-16, 0)))
ax1.set_title('地積測量図のメモ（任意座標）', fontsize=17, weight='bold', pad=6)
zb = Zu(ax2, fontsize=14)
fit(ax2, P62, margin=0.16, pad_aspect=True)
for (p, q), col in zip([(C, D), (D, E), (E, F)], [ORANGE, GREEN, PURPLE]):
    zb.poly([G, p, q], color=col, lw=1.2, fill=col, alpha=0.25)
zb.poly(P62, lw=2.4)
zb.north_arrow()
for n in 'CDEFG':
    zb.point(PTS[n], KIND[n])
    zb.point_label(PTS[n], n, away=centroid(P62))
zb.callout(G, 'G（原点にずらす）', dirs=(-100, -80, -120), color=RED, dists=(40, 55, 70))
zb.free_text(centroid([G, C, D]) + P(1.5, 0), '432.7642㎡\n→ 432.76㎡', fs=16, weight='bold', offsets=((0, 0), (0, -16), (16, 0)))
ax2.set_title('今回の測量の座標', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H22_dai21mon_zu13_bunpitsumae_chiseki.png')

# =====================================================================
# 図16：問3 新しい地番は6番4（6番3は使用済み。固定配置）
# =====================================================================
fig, ax = fixed_figure('図16　問3　新しい地番は6番4（最終の支号6番3は使用済み）',
                       '本番に支号のある土地を分筆するときは、1筆に従来の地番を残し、他の筆には本番の最終の支号を追って支号を付ける\n'
                       '（不動産登記事務取扱手続準則第67条第1項第4号ただし書）。「最終の支号は6番3」は、6番3がもう使われているという意味。')
for k, (no, note_, col) in enumerate([('6番1', '使用中（6番1の土地）', GRAY), ('6番2', '使用中（本件土地）', BLACK), ('6番3', '使用済み（最終の支号）', GRAY)]):
    x = 6 + k * 22
    ax.add_patch(FancyBboxPatch((x, 66), 18, 18, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=col, lw=2.0))
    ax.text(x + 9, 78, no, ha='center', va='center', fontsize=22, weight='bold', color=col)
    ax.text(x + 9, 70, note_, ha='center', va='center', fontsize=13, color=BLACK)
ax.add_patch(FancyBboxPatch((72, 66), 22, 18, boxstyle='round,pad=0.6', fc='#fff5f5', ec=RED, lw=2.4))
ax.text(83, 78, '6番4', ha='center', va='center', fontsize=24, weight='bold', color=RED)
ax.text(83, 70, '新しい地番（次の支号）', ha='center', va='center', fontsize=13, color=RED)
ax.annotate('', xy=(71, 75), xytext=(67, 75), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=RED))
ax.add_patch(FancyBboxPatch((6, 8), 88, 46, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=BLACK, lw=2.0))
ax.text(9, 48, '6番2を(B)と(C)に分筆すると', fontsize=19, weight='bold', va='center')
for i, (s, c_) in enumerate([('1筆（(B)）には、従来の地番の「6番2」を残す', BLACK),
                             ('もう1筆（(C)）には、最終の支号6番3の次の「6番4」を付ける', RED),
                             ('誤り：「6番3」（もう使われている地番。地番は重複しない。準則第67条第1項第1号）', GRAY)]):
    ax.text(11, 38 - i * 9.5, s, fontsize=17, va='center', color=c_)
path = os.path.join(OUT, 'H22_dai21mon_zu16_chiban_6ban4.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図16: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図18：問3 申請人は遺産分割で6番2を取得した相続人（固定配置）
# =====================================================================
fig, ax = fixed_figure('図18　問3　申請人は、遺産分割で6番2を取得した相続人だけ',
                       '分筆の申請人は所有権の登記名義人（不動産登記法第39条第1項）→ 死亡したので相続人（同法第30条）。遺産分割は相続開始の時に\n'
                       'さかのぼって効力を生じる（民法第909条）ので、6番2は良子（(B)）と健二（(C)）が取得した。敏夫・文子は6番2の土地を取得していない。')
ax.add_patch(FancyBboxPatch((30, 84), 40, 10, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=BLACK, lw=2.0))
ax.text(50, 89, '被相続人　杉山太郎（平成22年6月12日死亡）', ha='center', va='center', fontsize=17, weight='bold')
HEIRS = [(4, '杉山良子', '6番1の(A)、6番2の(B)', RED, '申請人'),
         (28, '杉山敏夫', '6番1と6番2に\nまたがる建物', GRAY, '6番2の土地は\n取得していない'),
         (52, '杉山健二', '6番2の(C)', RED, '申請人'),
         (76, '田中文子', '6番1の(D)、\n6番1の上の建物', GRAY, '6番2の土地は\n取得していない')]
for x, name, get, col, role in HEIRS:
    ax.annotate('', xy=(x + 10, 71), xytext=(50, 83), arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.add_patch(FancyBboxPatch((x, 36), 20, 34, boxstyle='round,pad=0.6', fc='#fff5f5' if col == RED else '#f7f7f7', ec=col, lw=2.0))
    ax.text(x + 10, 64, name, ha='center', va='center', fontsize=19, weight='bold', color=col)
    ax.text(x + 10, 54, get, ha='center', va='center', fontsize=14, color=BLACK)
    ax.text(x + 10, 43, role, ha='center', va='center', fontsize=16, weight='bold', color=col)
ax.add_patch(FancyBboxPatch((6, 6), 88, 20, boxstyle='round,pad=0.6', fc='#fff5f5', ec=RED, lw=2.0))
ax.text(50, 20, '申請人：杉山良子と杉山健二（6番2を取得した相続人）', ha='center', va='center', fontsize=19, weight='bold', color=RED)
ax.text(50, 11, '誤り：相続人4人を全員並べる（敏夫・田中文子は6番2について何も取得していない）', ha='center', va='center', fontsize=15, color=GRAY)
path = os.path.join(OUT, 'H22_dai21mon_zu18_souzokunin.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図18: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図20：問3 土地の表示の書き方（行ごとの原因。固定配置）
# =====================================================================
fig, ax = fixed_figure('図20　問3　土地の表示は行ごとに書くものが違う（原因は「③6番2、6番4に分筆」）',
                       '2行目の(B)は地番・地目が変わらないので空欄にし、原因は分筆後の地番を元の地番から並べる。3行目の(C)は新しい登記記録になるので\n'
                       '地番・地目・地積を全部書き、原因は元の地番から「6番2から分筆」。2行目を「③6番4を分筆」と書くのは誤り。')
COLS = [(4, 14, '①地番'), (18, 12, '②地目'), (30, 14, '③地積 m²'), (44, 30, '登記原因及びその日付'), (74, 22, '何を書くか')]
ROWS20 = [('6番2', '宅地', '432.76', '（空欄）', '分筆前の登記記録のまま', BLACK),
          ('(B)（空欄）', '（空欄）', '201.86', '③6番2、6番4に分筆', '地番・地目は変わらない', RED),
          ('(C) 6番4', '宅地', '230.91', '6番2から分筆', '新しい登記記録なので全部', RED)]
y_head = 84
for x, w, head in COLS:
    ax.add_patch(plt.Rectangle((x, y_head), w, 8, fc='#eeeeee', ec=BLACK, lw=1.4))
    ax.text(x + w / 2, y_head + 4, head, ha='center', va='center', fontsize=15, weight='bold')
for r, (c1, c2, c3, c4, c5, col) in enumerate(ROWS20):
    y = y_head - 13 * (r + 1)
    for (x, w, _), s in zip(COLS, [c1, c2, c3, c4, c5]):
        ax.add_patch(plt.Rectangle((x, y), w, 13, fc='white', ec=BLACK, lw=1.2))
        is_note = (x == 74)
        ax.text(x + w / 2, y + 6.5, s, ha='center', va='center', fontsize=13 if is_note else 16,
                color=GRAY if (s == '（空欄）' or '（空欄）' in s and s.startswith('(B)')) and not is_note else (col if x == 44 or is_note else BLACK))
    ax.text(2.5, y + 6.5, f'{r + 1}行目', ha='center', va='center', fontsize=12, color=GRAY, rotation=90)
ax.add_patch(FancyBboxPatch((6, 6), 88, 22, boxstyle='round,pad=0.6', fc='#f7f7f7', ec=GRAY, lw=2.0))
ax.text(10, 22, '誤り：2行目の原因「③6番4を分筆」', fontsize=17, va='center', color=GRAY)
ax.text(10, 12, '正しくは：分筆後の地番を元の地番から並べて「③6番2、6番4に分筆」（③は地積が変わる印）', fontsize=17, va='center', color=RED)
path = os.path.join(OUT, 'H22_dai21mon_zu20_genin.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図20: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図21：問4 H・Jは筆界点ではない（筆界D→E・F→Lの線の上の杭）
# =====================================================================
fig, (ax,) = new_figure('図21　問4　H・Jは6番2の筆界の線の上にあるだけで、筆界点ではない',
                        'HはD→Eの線の上、JはF→Lの線の上（X＝513.27の南の辺）にあるA市の杭で、筆界の折れ点ではない。地積測量図に描くのは、\n'
                        '筆界点C・D・E・F・Gと分割点K・Lだけ。H・Jは遺産分割協議書の図面にもない（見取図の（注））。')
z = Zu(ax, fontsize=14)
fit(ax, P62 + [T3, T1], margin=0.06, pad_aspect=True)
z.poly(P62, lw=2.6)
z.line(K, L, lw=2.2)
z.line(H, I, color=GRAY, lw=1.4, ls='--')
z.line(I, J, color=GRAY, lw=1.4, ls='--')
z.north_arrow()
for n in 'CKDEFLG':
    z.point(PTS[n], KIND[n], color=RED)
for n in 'HIJ':
    z.point(PTS[n], KIND[n], color=GRAY)
z.callout(H, 'H：D→Eの線の上（描かない）', dirs=(60, 90, 30, 120), color=GRAY, dists=(50, 70, 90))
z.callout(J, 'J：F→Lの線の上（描かない）', dirs=(-90, -120, -60), color=GRAY, dists=(50, 70, 90))
z.callout(I, 'I：6番2の中（描かない）', dirs=(150, 180, 120), color=GRAY, dists=(60, 80, 100))
for n in 'CKDEFLG':
    z.point_label(PTS[n], n, away=INNER, color=RED)
z.free_text(centroid(PB), '描く：筆界点と分割点\nC・K・D・E・F・L・G', fs=16, color=RED, weight='bold', offsets=((0, 0), (0, -16), (16, 0)))
ALL_PROBLEMS += save(fig, [z], 'H22_dai21mon_zu21_HJ.png')

print('重なりの合計:', len(ALL_PROBLEMS))
