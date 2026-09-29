"""令和5年度 第21問（土地）会話形式note記事の解説図8枚を、座標値から作図する。

`../prompt_R5_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。

実行: python3 note-articles-Kijyutsu/R5/Q21/zu/draw_R5_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, area, chiseki  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
T1, T2 = P(680.04, 690.97), P(703.30, 691.02)
A, C, D, E = P(701.48, 692.76), P(702.79, 703.62), P(704.50, 717.76), P(679.68, 717.76)
F, G, I, J = P(680.14, 703.62), P(680.64, 703.62), P(680.64, 692.76), P(680.49, 692.76)
Y_BH = C.imag - 1.00                                   # CGから西へ1.00m
B = r2(A + (C - A) * (Y_BH - A.imag) / (C.imag - A.imag))
H = P(G.real, Y_BH)                                    # 直線GI（X＝680.64）との交点
Bw_raw = C + (A - C) / abs(A - C) * 1.00               # ACに沿って1.00m測った誤り
Bw = r2(Bw_raw)

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
assert abs(B - P(702.67, 702.62)) < 1e-9 and abs(H - P(680.64, 702.62)) < 1e-9
assert abs(Bw - P(702.67, 702.63)) < 1e-9
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'AB': (A, B, '9.93'), 'BC': (B, C, '1.01'), 'CF': (C, F, '22.65'), 'FJ': (F, J, '10.87'),
         'JI': (J, I, '0.15'), 'IA': (I, A, '20.84'), 'BH': (B, H, '22.03'), 'HI': (H, I, '9.86')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
for n, (p, q, want) in {'CG': (C, G, '22.15'), 'AJ': (A, J, '20.99'), 'GI': (G, I, '10.86'), 'HG': (H, G, '1.00'),
                        'GF': (G, F, '0.50'), 'AC': (A, C, '10.94')}.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert f'{C.imag - Bw_raw.imag:.2f}' == '0.99'
OTSU = [A, C, F, J]                  # 乙土地（1番2）
KOU = [C, D, E, F]                   # 甲土地（1番1）
N2 = [A, B, H, I]                    # 分筆後の1番2（西側部分）
N4 = [B, C, F, J, I, H]              # 分筆後の1番4
SHA = [B, C, G, H]                   # 斜線部分
HOSO = [I, H, G, F, J]               # 細長い部分
AREAS = {'乙土地': (area(OTSU), 236.9652), '1番2': (area(N2), 211.3491), '1番4': (area(N4), 25.6195),
         'G・Iを通した乙土地': (area([A, C, G, I]), 233.4357), '斜線部分': (area(SHA), 22.09), '細長い部分': (area(HOSO), 3.5295), '甲土地': (area(KOU), 335.6129)}
for n, (got, want) in AREAS.items():
    assert abs(got - want) < 5e-5, (n, got, want)
assert chiseki(area(N2)) == 211.34 and chiseki(area(N4)) == 25.61 and chiseki(area(HOSO)) == 3.52
assert chiseki(335.5096500 + 22.09) == 357.59
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
# 図1：全体像
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像（令和5年4月1日時点）',
                        'C・F・G は Y＝703.62、A・I・J は Y＝692.76、D・E は Y＝717.76 で、どれも真北向きの直線の上にある。\n'
                        '本件借地（A・C・G・I）の南の線より、乙土地の筆界（J・F）は少し南にある。B・Hは問2で求める分割点。')
z = Zu(ax, fontsize=14)
fit(ax, [A, C, D, E, F, J, T1, T2], margin=0.10, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.poly([A, C, G, I], color=GRAY, lw=1.4, ls='--', check=True)
z.poly(SHA, color=RED, lw=0, fill=RED, alpha=0.25, check=False)
z.north_arrow()
z.free_text(centroid(KOU), '甲土地\n1番1　雑種地\n335㎡', fs=17)
z.free_text(centroid(N2), '乙土地\n1番2　宅地\n236.81㎡', fs=17)
z.callout(centroid(SHA), '斜線部分（B・C・G・H）', dirs=(0, 20, -20), color=RED, dists=(160, 190, 220))
z.callout(I + (G - I) * 0.20, '本件借地（A・C・G・I）の線', dirs=(60, 75, 45, 90), color=GRAY,
          dists=(90, 120, 150, 180))
for p, n, kind in [(A, 'A', 'concrete'), (C, 'C', 'metal'), (D, 'D', 'concrete'), (E, 'E', 'concrete')]:
    z.point(p, kind)
    z.point_label(p, n, away=centroid(OTSU + KOU))
z.point(B, 'dot', color=GRAY)
z.point_label(B, 'B', away=centroid(KOU), color=GRAY)
for p, n, kind in [(F, 'F', 'metal'), (G, 'G', 'metal'), (I, 'I', 'metal'), (J, 'J', 'concrete')]:
    z.point(p, kind, size=6)
z.point(H, 'dot', color=GRAY, size=5)
z.callout(G, 'G（金属標）', dirs=(70, 50, 90), dists=(60, 80, 100))
z.callout(F, 'F（金属標）', dirs=(-70, -50, -90), dists=(55, 75, 95))
z.callout(H, 'H', dirs=(110, 130, 95), dists=(55, 75), color=GRAY)
z.callout(I, 'I（金属標）', dirs=(120, 140, 100), dists=(60, 80, 100))
z.callout(J, 'J（コンクリート杭）', dirs=(-110, -130, -90), dists=(60, 80, 100))
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=centroid(OTSU))
z.edge_label(A, C, '3－1', centroid(OTSU), fs=15, dists=(30, 40), rotate=False)
z.edge_label(C, D, '3－1', centroid(KOU), fs=15, dists=(30, 40), rotate=False)
z.edge_label(D, E, '道路', centroid(KOU), fs=15, dists=(30, 40), rotate=False)
z.edge_label(F, E, '2－1', centroid(KOU), fs=15, dists=(40, 50), rotate=False)
z.edge_label(J, A, '道路', centroid(OTSU), fs=15, dists=(40, 55), ts=(0.5, 0.62, 0.38), rotate=False)
ALL_PROBLEMS += save(fig, [z], 'R5_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：問1 筆界点の判断（G・I と F・J の比較）
# =====================================================================
fig, (ax1, ax2) = new_figure('図2　問1　筆界点は金属標のGとIではなく、FとJ',
                             '平成15年の地積測量図：1番1の西の辺 11.64＋11.01＝22.65、1番2・1番3の西の辺 10.33＋10.66＝20.99（合筆で消えた中間の点は足して比べる）。\n'
                             '左：C→G 22.15、A→I 20.84 で合わない。右：C→F 22.65、A→J 20.99 で一致（南の辺 FJ も 10.87 で一致）。\n'
                             'ア 一筆　イ 測量　ウ F点　エ J点', ncols=2)
zs = []
for ax, pts, lab_c, lab_a, head, col, ok in [
    (ax1, [A, C, G, I], ('C→G ＝ 22.15', G), ('A→I ＝ 20.84', I), 'G・I（金属標・借地の角）を通すと', GRAY, False),
    (ax2, [A, C, F, J], ('C→F ＝ 22.65', F), ('A→J ＝ 20.99', J), 'F・J を通すと', RED, True),
]:
    z = Zu(ax, fontsize=14)
    fit(ax, [A, C, F, J], margin=0.30, pad_aspect=True)
    z.poly(OTSU, color=GRAY, lw=1.0, check=True)
    z.poly(pts, color=col, lw=2.4, fill=BLUE if ok else None, alpha=0.18)
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=18, color=col, weight='bold', pad=6)
    z.edge_label(C, lab_c[1], lab_c[0], centroid(pts), color=col, fs=15, dists=(12, 20))
    z.edge_label(A, lab_a[1], lab_a[0], centroid(pts), color=col, fs=15, dists=(12, 20))
    for p, n in [(A, 'A'), (C, 'C')]:
        z.point(p, 'concrete' if n == 'A' else 'metal')
        z.point_label(p, n, away=centroid(OTSU))
    for p, n in ([(G, 'G'), (I, 'I')] if not ok else [(F, 'F'), (J, 'J')]):
        z.point(p, 'metal' if n in 'GIF' else 'concrete', color=col)
        z.point_label(p, n, away=centroid(OTSU), color=col)
    if ok:
        z.edge_label(F, J, 'FJ ＝ 10.87', centroid(pts), color=col, fs=14, dists=(14, 22))
    zs.append(z)
zs[0].free_text(centroid(OTSU), '地積測量図の\n22.65・20.99と\n合わない\n\n面積 233.43㎡\n（登記記録236.81と\n3.37㎡違う）', color=GRAY, fs=16)
zs[1].free_text(centroid(OTSU), '地積測量図の\n22.65・20.99と\n一致\n\n面積 236.96㎡\n（登記記録236.81と\n0.16㎡の差）', color=RED, fs=16)
ALL_PROBLEMS += save(fig, zs, 'R5_dai21mon_zu02_hikkaiten_FJ.png')

# =====================================================================
# 図3：問2 B点
# =====================================================================
Braw = A + (C - A) * (Y_BH - A.imag) / (C.imag - A.imag)
fig, (ax1, ax2) = new_figure('図3　問2　B点の求め方（CGから西へ1.00mの線とACの交点）',
                             'CGは真北向き（Y＝703.62）なので、西へ1.00mの線は Y＝702.62。BはAC上でY座標が702.62の点：B ＝ A ＋ (C − A) × 9.86 ÷ 10.86\n'
                             '右の拡大図：ACに沿って1.00m測った点（702.67, 702.63）は、CGから0.99m（0.9928…）しか離れない。ACが斜めのため。BC は 1.01 になる。',
                             ncols=2, width_ratios=[1.15, 1])
za = Zu(ax1, fontsize=14)
fit(ax1, OTSU, margin=0.20, pad_aspect=True)
za.poly(OTSU, lw=2.0)
za.line(C, G, lw=2.0, check=False)
za.line(B, H, color=RED, lw=2.0, ls='--')
za.line(I, G, color=GRAY, lw=1.2, ls='--')
za.north_arrow(length=0.07)
for p, n, kind in [(A, 'A', 'concrete'), (C, 'C', 'metal'), (F, 'F', 'metal'), (J, 'J', 'concrete')]:
    za.point(p, kind)
    za.point_label(p, n, away=centroid(OTSU))
za.point(B, 'dot', color=RED)
za.point(H, 'dot', color=RED, size=5)
za.point_label(H, 'H', away=centroid(OTSU) + P(0, 5), color=RED)
za.callout(B, 'B（702.67, 702.62）', dirs=(150, 130, 170), color=RED, dists=(70, 90, 110))
za.line(P(697.0, Y_BH), P(697.0, C.imag), color=RED, lw=1.2)
za.callout(P(697.0, (Y_BH + C.imag) / 2), '1.00', dirs=(0, 15, -15, 30, -30), color=RED, dists=(30, 40, 50))
za.free_text(P(697.5, 697.7), 'A→B のY座標の差\n702.62 − 692.76 ＝ 9.86\nA→C のY座標の差\n703.62 − 692.76 ＝ 10.86', fs=14)
za.callout(P(686.0, Y_BH), 'BHの線（Y＝702.62）', dirs=(180, 170, 190), color=RED, dists=(60, 80, 100))
zb = Zu(ax2, fontsize=14)
ax2.set_title('Bの付近の拡大（約0.07m四方）', fontsize=17, pad=6)
fit(ax2, [P(702.64, 702.585), P(702.70, 702.655)], margin=0.02, pad_aspect=True)
zb.line(Braw + (A - C) / abs(A - C) * 0.03, Braw + (C - A) / abs(A - C) * 0.045, lw=2.2)
zb.line(P(702.695, Y_BH), P(702.645, Y_BH), color=RED, lw=1.8, ls='--')
zb.line(P(702.695, Bw_raw.imag), P(702.645, Bw_raw.imag), color=GRAY, lw=1.4, ls=':')
zb.north_arrow(length=0.08)
zb.point(Braw, 'dot', color=RED)
zb.point(Bw_raw, 'dot', color=GRAY)
zb.callout(Braw, 'B（702.67, 702.62）\nCGから直角に1.00m', dirs=(-120, -140, -100), color=RED, dists=(80, 105))
zb.callout(Bw_raw, 'ACに沿って1.00mの点\n（702.67, 702.63）\nCGから0.99m', dirs=(-60, -40, -80), color=GRAY,
           dists=(80, 105, 130))
zb.free_text(P(702.690, Y_BH), 'Y＝702.62', fs=13, color=RED, offsets=((-45, 0), (-45, 14)))
zb.free_text(P(702.690, Bw_raw.imag), 'Y＝702.6271…', fs=13, color=GRAY, offsets=((55, 0), (55, 14)))
zb.free_text(Braw + (A - C) / abs(A - C) * 0.022, '直線AC', fs=13, offsets=((0, 16), (0, 24)))
ALL_PROBLEMS += save(fig, [za, zb], 'R5_dai21mon_zu03_B_heikou.png')

# =====================================================================
# 図4：問2 H点
# =====================================================================
fig, (ax,) = new_figure('図4　問2　H点の求め方（GIとBHの交点）',
                        'G・I はどちらも X＝680.64 なので、GI は真東向きの直線。BH は Y＝702.62 の南北の線なので、H は（680.64, 702.62）。\n'
                        'I・H・G は一直線。その南に、乙土地の細長い部分（I・H・G・F・J。IJ 0.15、GF 0.50 の台形）が残る。')
z = Zu(ax, fontsize=14)
fit(ax, [P(678.8, 689.6), P(682.6, 706.8)], margin=0.02, pad_aspect=True)
z.line(J, F, lw=2.2)
z.line(J, P(682.2, 692.76), lw=2.2)
z.line(F, P(682.2, 703.62), lw=2.2)
z.line(I, G, color=GRAY, lw=1.6, ls='--')
z.line(H, P(682.2, Y_BH), color=RED, lw=1.8, ls='--')
z.poly(HOSO, color=ORANGE, lw=0, fill=ORANGE, alpha=0.35, check=False)
z.north_arrow(length=0.08)
z.point(H, 'dot', color=RED)
for p, n, kind in [(I, 'I', 'metal'), (G, 'G', 'metal'), (F, 'F', 'metal'), (J, 'J', 'concrete')]:
    z.point(p, kind)
z.callout(H, 'H（680.64, 702.62）', dirs=(150, 135, 165), color=RED, dists=(90, 115, 140))
for p, txt, dirs in [(I, 'I（680.64, 692.76）', (160, 145, 175)), (J, 'J（680.49, 692.76）', (-160, -145, -175)),
                     (G, 'G（680.64, 703.62）', (20, 35, 5)), (F, 'F（680.14, 703.62）', (-20, -35, -5))]:
    z.callout(p, txt, dirs=dirs, dists=(55, 75, 95))
z.edge_label(I, H, 'IH ＝ 9.86', centroid(HOSO), fs=14, dists=(12, 18), ts=(0.4, 0.3, 0.55))
z.edge_label(H, G, '1.00', centroid(HOSO), fs=14, dists=(12, 18))
z.free_text(P(682.2, Y_BH), 'BHの線（Y＝702.62）', fs=13, color=RED, offsets=((0, 14), (0, 22)), va='bottom')
z.free_text(P(681.2, 697.5), '本件借地の南の線（I・G）', fs=13, color=GRAY, offsets=((0, 0), (0, 15)))
z.free_text(P(679.9, 697.0), '乙土地の筆界（J・F）', fs=13, color=BLACK, offsets=((0, 0), (0, -12)))
z.callout(centroid(HOSO) + P(0, 1.0), '細長い部分　3.5295㎡', dirs=(-80, -60, -100), color=ORANGE, dists=(70, 90))
ALL_PROBLEMS += save(fig, [z], 'R5_dai21mon_zu04_H_kousa.png')

# =====================================================================
# 図5：問3の前提 8月10日の分筆の区画（誤りと正しい分け方）
# =====================================================================
fig, (ax1, ax2) = new_figure('図5　問3　8月10日の分筆は、1番2＝西側部分（A・B・H・I）',
                             '左：1番4を斜線部分だけにすると、1番2に南の細長い部分まで入り、花山光司さんに西側部分だけを移転できない。\n'
                             '右：1番2（A・B・H・I）＝ (20.84 ＋ 22.03) ÷ 2 × 9.86 ＝ 211.3491 → 211.34㎡、1番4（B・C・F・J・I・H）＝ 22.09 ＋ 3.5295 ＝ 25.6195 → 25.61㎡\n'
                             '乙土地の実測 236.9652㎡と登記記録 236.81㎡の差 0.1552㎡ は甲2の公差（参考 約1.37㎡）の範囲内なので、地積更正は不要。',
                             ncols=2)
zs = []
for ax, p2, p4, head, col, t2, t4 in [
    (ax1, [A, B, H, G, F, J], SHA, '1番4＝斜線部分だけ（誤り）', GRAY, '1番2\n（細長い部分まで入る）', '1番4'),
    (ax2, N2, N4, '1番2＝西側部分、1番4＝残り（正しい）', RED, '（イ）1番2\n211.34㎡', '（ロ）1番4\n25.61㎡'),
]:
    z = Zu(ax, fontsize=14)
    fit(ax, OTSU, margin=0.28, pad_aspect=True)
    z.poly(p2, fill=BLUE)
    z.poly(p4, fill=ORANGE, alpha=0.4)
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=18, color=col, weight='bold', pad=6)
    z.free_text(centroid(N2), t2, fs=16)
    z.callout(C + (G - C) * 0.45, t4, dirs=(0, 20, -20), dists=(40, 60, 80))
    for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (F, 'F'), (J, 'J')]:
        z.point(p, 'dot')
        z.point_label(p, n, away=centroid(OTSU))
    zs.append(z)
zs[0].callout(I + (G - I) * 0.5, '細長い部分（I・H・G・F・J）\nも1番2に入ってしまう', dirs=(-90, -70, -110), color=RED,
              dists=(50, 70, 90))
zs[1].callout(I + (G - I) * 0.5, '細長い部分は1番4の側\n（斜線部分22.09＋細長い部分3.5295）', dirs=(-90, -70, -110), color=RED,
              dists=(50, 70, 90))
for z in zs:
    for p, n in [(H, 'H'), (I, 'I')]:
        z.point(p, 'dot', size=5)
ALL_PROBLEMS += save(fig, zs, 'R5_dai21mon_zu05_bunpitsu_kukaku.png')

# =====================================================================
# 図6：問3 地積測量図の完成見本
# =====================================================================
fig, (ax,) = new_figure('図6　問3　地積測量図（1番2・1番4）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm（JI 0.15 は 0.6mm）。辺長は小数第3位を四捨五入（FJ は 10.8656 なので 10.87）。\n'
                        '座標値・地積・求積方法・測量年月日は書かない（問題文の注5）。A市基準点T1・T2は位置と点名だけ（問題文の注6）。G は8月の時点では筆界点ではない。')
z = Zu(ax, fontsize=15)
fit(ax, OTSU + [T1, T2], margin=0.12, pad_aspect=True)
z.poly(OTSU, lw=2.0)
z.poly([B, H, I], lw=2.0, closed=False)
z.north_arrow()
co = centroid(OTSU)
for n, (p, q, s) in SIDES.items():
    if n in ('BH', 'HI'):
        z.edge_label(p, q, s, centroid(N2), fs=15, outward=False)
    elif n == 'BC':
        z.edge_label(p, q, s, co, fs=14, dists=(22, 30, 38), ts=(0.5,))
    elif n == 'JI':
        z.edge_label(p, q, s, co, fs=14, dists=(24, 32, 40), ts=(0.5,))
    else:
        z.edge_label(p, q, s, co, fs=15)
z.free_text(centroid(N2), '（イ）\n1－2', fs=18)
z.callout(C + (F - C) * 0.35, '（ロ）\n1－4', dirs=(180, 160, 200), dists=(60, 80, 100), box_color='white')
for p, n in [(A, 'A'), (B, 'B'), (H, 'H'), (J, 'J')]:
    z.point(p, 'concrete')
for p, n in [(C, 'C'), (F, 'F'), (I, 'I')]:
    z.point(p, 'metal', size=8)
for p, n in [(A, 'A'), (C, 'C'), (F, 'F'), (J, 'J')]:
    z.point_label(p, n, away=co)
z.point_label(B, 'B', away=centroid(N2) + P(0, 3))
z.point_label(H, 'H', away=centroid(N2))
z.point_label(I, 'I', away=centroid(N2) + P(-3, 0))
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.edge_label(A, C, '３－１', co, fs=16, dists=(34, 44), ts=(0.35, 0.3), rotate=False)
z.edge_label(C, F, '１－１', co, fs=16, dists=(40, 50), rotate=False)
z.edge_label(F, J, '２－１', co, fs=16, dists=(36, 46), rotate=False)
z.edge_label(I, A, '道路', co, fs=16, dists=(40, 50), rotate=False)
z.free_text(P(684.5, 706.0), '（単位：ｍ）\n◎ コンクリート杭：A・B・H・J\n● 金属標：C・F・I\n△ 基準点：T1・T2', fs=13,
            ha='left', va='bottom', offsets=((0, 0), (0, 30), (0, 60)))
ALL_PROBLEMS += save(fig, [z], 'R5_dai21mon_zu06_chiseki_sokuryouzu.png')

# =====================================================================
# 図7：問4 10月16日の地目変更・分合筆
# =====================================================================
fig, (ax,) = new_figure('図7　問4　10月16日の地目変更・分合筆（1番4の一部を1番1へ）',
                        '1番1は令和5年9月20日に雑種地から宅地へ（新店舗と一体の駐車場・展示販売所）。1番4のうち斜線部分（ロ）22.09㎡を1番1に合筆し、\n'
                        '細長い部分（イ）3.52㎡が1番4として残る（3.52 ＋ 22.09 ＝ 25.61）。1番1の地積は問題文の注9で端数を援用：335.5096500 ＋ 22.09 ＝ 357.59965 → 357.59㎡\n'
                        '登録免許税は分合筆後の2個（1番1・1番4）× 1,000円 ＝ 2,000円。地目変更には登録免許税はかからない。')
z = Zu(ax, fontsize=14)
fit(ax, OTSU + KOU, margin=0.08, pad_aspect=True)
z.poly(N2, color=GRAY, lw=1.2)
z.poly(KOU, fill=GREEN)
z.poly(SHA, fill=PURPLE, alpha=0.35)
z.poly(HOSO, fill=ORANGE, alpha=0.45)
z.north_arrow()
z.free_text(centroid(KOU), '1番1\n雑種地 335㎡ → 宅地\n分合筆後 357.59㎡', fs=17)
z.free_text(centroid(N2), '1番2\n（西側部分・花山光司へ）\n変わらない', fs=15, color=GRAY)
z.callout(C + (G - C) * 0.55, '（ロ）斜線部分 22.09㎡\n→ 1番1に合併', dirs=(0, 15, -15), color=PURPLE, dists=(110, 140, 170))
z.callout(I + (G - I) * 0.25, '（イ）1番4　3.52㎡\n（細長い部分が残る）', dirs=(-150, -165, -135), color=ORANGE,
          dists=(40, 55, 70))
for p, n in [(B, 'B'), (C, 'C'), (D, 'D'), (E, 'E')]:
    z.point(p, 'dot')
    z.point_label(p, n, away=centroid(KOU) if n in 'DE' else centroid(N2))
ALL_PROBLEMS += save(fig, [z], 'R5_dai21mon_zu07_bungouhitsu.png')

# =====================================================================
# 図8：問5 地図作成のための職権の分筆・合筆（流れ図。座標なし）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図8　問5　地図作成のための職権の分筆・合筆（不動産登記法第39条第3項）', fontsize=24, weight='bold', y=0.95)
ax = fig.add_axes([0.03, 0.22, 0.94, 0.62])
ax.set_xlim(0, 100)
ax.set_ylim(0, 40)
ax.axis('off')
boxes = [(2, '法第14条第1項の地図を\n作成するため\n必要があると認める', BLACK),
         (27, '（①）表題部所有者又は\n（②）所有権の登記名義人の\n（③）異議がない', RED),
         (52, '登記官が（④）職権で\n分筆又は合筆の登記', BLUE),
         (77, '道路の部分が分かれ\n利用状況と登記記録が\n一致する', GREEN)]
for x0, txt, col in boxes:
    ax.add_patch(FancyBboxPatch((x0, 12), 21, 18, boxstyle='round,pad=0.6', fc='white', ec=col, lw=2.2))
    ax.text(x0 + 10.5, 21, txt, ha='center', va='center', fontsize=16, color=col, weight='bold')
for x0 in (23.8, 48.8, 73.8):
    ax.annotate('', xy=(x0 + 2.6, 21), xytext=(x0, 21), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=GRAY))
ax.text(50, 5, '「承諾があるとき」ではなく「異議がないとき」に限る', ha='center', va='center', fontsize=17,
        color=RED, weight='bold')
fig.text(0.5, 0.10, '第39条第2項（1筆の一部が別の地目・別の地番区域になったとき）は「職権で分筆の登記をしなければならない」。\n'
         '第3項（地図作成のため）は「異議がないときに限り、職権で分筆又は合筆の登記をすることができる」。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'R5_dai21mon_zu08_shokken_bungouhitsu.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図8: 流れ図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
