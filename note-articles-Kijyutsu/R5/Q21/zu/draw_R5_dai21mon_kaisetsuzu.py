"""令和5年度 第21問（土地）会話形式note記事の解説図21枚を、座標値から作図する。

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
fig, (ax,) = new_figure('北を上にして描き直した全体像（令和5年4月1日時点）',
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
ALL_PROBLEMS += save(fig, [z], 'R5_dai21mon_zu02_zentaizu.png')

# =====================================================================
# 図2：問1 筆界点の判断（G・I と F・J の比較）
# =====================================================================
fig, (ax1, ax2) = new_figure('問1　筆界点は金属標のGとIではなく、FとJ',
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
ALL_PROBLEMS += save(fig, zs, 'R5_dai21mon_zu05_hikkaiten_FJ.png')

# =====================================================================
# 図3：問2 B点
# =====================================================================
Braw = A + (C - A) * (Y_BH - A.imag) / (C.imag - A.imag)
fig, (ax1, ax2) = new_figure('問2　B点の求め方（CGから西へ1.00mの線とACの交点）',
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
ALL_PROBLEMS += save(fig, [za, zb], 'R5_dai21mon_zu06_B_heikou.png')

# =====================================================================
# 図4：問2 H点
# =====================================================================
fig, (ax,) = new_figure('問2　H点の求め方（GIとBHの交点）',
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
ALL_PROBLEMS += save(fig, [z], 'R5_dai21mon_zu08_H_kousa.png')

# =====================================================================
# 図5：問3の前提 8月10日の分筆の区画（誤りと正しい分け方）
# =====================================================================
fig, (ax1, ax2) = new_figure('問3　8月10日の分筆は、1番2＝西側部分（A・B・H・I）',
                             '左：1番4を斜線部分だけにすると、1番2に南の細長い部分まで入り、花山光司さんに西側部分だけを移転できない。\n'
                             '右：1番2（A・B・H・I）＝ (20.84 ＋ 22.03) ÷ 2 × 9.86 ＝ 211.3491 → 211.34㎡\n1番4（B・C・F・J・I・H）＝ 22.09 ＋ 3.5295 ＝ 25.6195 → 25.61㎡\n'
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
ALL_PROBLEMS += save(fig, zs, 'R5_dai21mon_zu09_bunpitsu_kukaku.png')

# =====================================================================
# zu14：問3 地積測量図（8月10日申請分）の完成見本
#   試験の答案用紙の第3欄（原本 `../touan_youshi/R5_dai21mon_touan_youshi.pdf` の2ページ目。A3横）の枠・欄の位置と大きさを、
#   PDFの罫線からmmで測ったとおりに描く（2026-10-26）。縮尺1/250（1m ＝ 4mm）の実際の大きさで、枠の中に図を描く。
#   黒は印刷済み、青は書き込み。画像の中に図番は入れない
# =====================================================================
from matplotlib.patches import Rectangle  # noqa: E402
setup_font()
ORIG_FRAME_MM = (80.6, 25.8, 382.6, 256.8)     # 図を描く枠（x0, y0, x1, y1。原本の用紙の左上が原点。横302mm・縦231mm）
ORIG_SHEET_MM = (56.3, 12.2, 406.9, 274.8)     # 用紙の外枠（二重線の外側）
INK = '#1a3a8f'
SW3, SH3, S3 = 16.0, 13.0, 0.0425               # 図の幅・高さ（インチ）、原本の1mmが図の何インチか


def fx3(x):
    return (0.55 + (x - ORIG_SHEET_MM[0]) * S3) / SW3


def fy3(y):
    return 1 - (0.30 + (y - ORIG_SHEET_MM[1]) * S3) / SH3


fig = plt.figure(figsize=(SW3, SH3), dpi=100)
fig.patch.set_facecolor('white')


def frect(x0, y0, x1, y1, lw=1.4):
    fig.add_artist(Rectangle((fx3(x0), fy3(y1)), fx3(x1) - fx3(x0), fy3(y0) - fy3(y1), transform=fig.transFigure,
                             fill=False, edgecolor=BLACK, lw=lw))


def fline(x0, y0, x1, y1, lw=1.2):
    fig.add_artist(plt.Line2D([fx3(x0), fx3(x1)], [fy3(y0), fy3(y1)], transform=fig.transFigure, color=BLACK, lw=lw))


def ftext(x, y, s, fs=13, ha='center', color=BLACK, **kw):
    fig.text(fx3(x), fy3(y), s, fontsize=fs, ha=ha, va='center', color=color, **kw)


frect(56.3, 12.2, 406.9, 274.8, lw=1.2)                      # 用紙の外枠（二重線）
frect(57.1, 13.0, 406.1, 274.0, lw=1.2)
ftext(59.0, 17.6, '第3欄', fs=15, ha='left', weight='bold')
frect(*ORIG_FRAME_MM, lw=1.8)                                  # 図を描く枠（横302mm・縦231mm）
fline(231.6, 25.8, 231.6, 35.8)                                # 折り目の印（上・下）
fline(231.6, 246.8, 231.6, 256.8)
frect(240.6, 15.8, 302.6, 25.8)                                # 地番の欄
fline(264.6, 15.8, 264.6, 25.8)
ftext(252.6, 20.8, '地　　番', fs=12)
ftext(283.6, 20.8, '1番2、1番4', fs=14, color=INK, weight='bold')
frect(240.6, 25.8, 382.6, 35.8)                                # 土地の所在の欄
fline(264.6, 25.8, 264.6, 35.8)
ftext(252.6, 30.8, '土地の所在', fs=12)
ftext(268.0, 30.8, 'Ａ市Ｂ町二丁目', fs=15, ha='left', color=INK, weight='bold')
ftext(342.6, 20.8, '地　積　測　量　図', fs=19)
frect(80.6, 256.8, 223.6, 271.3)                               # 作成者の欄
fline(99.6, 256.8, 99.6, 271.3)
ftext(90.1, 264.0, '作 成 者', fs=11)
ftext(161.6, 262.0, '（略）', fs=13)
ftext(221.0, 268.8, '（令和５年○月○日作成）', fs=11, ha='right')
frect(239.6, 256.8, 382.6, 271.3)                              # 申請人の欄
fline(258.6, 256.8, 258.6, 271.3)
ftext(249.1, 264.0, '申 請 人', fs=11)
ftext(303.0, 264.0, '（略）', fs=13)
fline(348.5, 256.8, 348.5, 271.3)                              # 縮尺の欄（1/250は印刷済み）
fline(358.6, 256.8, 358.6, 271.3)
ftext(353.5, 264.0, '縮尺', fs=10)
fline(360.6, 269.8, 380.6, 258.3, lw=1.0)
ftext(364.5, 260.4, '1', fs=11)
ftext(376.5, 268.2, '250', fs=11)
fig.text(0.5, 0.52 / SH3,
         '黒は答案用紙に印刷済みのもの（枠、欄の見出し、作成者・申請人の「（略）」、作成日の欄、縮尺 1／250）。青は欄への記入。図は縮尺1/250（1m ＝ 4mm）で枠の中に描く。\n'
         '書くもの：地番（1番2、1番4）、土地の所在（Ａ市Ｂ町二丁目）、辺長8本、（イ）（ロ）の符号と地番、境界標の記号、方位記号（印刷されていないので必ず描く）、\n'
         '隣接地の地番、基準点T1・T2の位置と点名（問題文の注6）。書かないもの：座標値・座標系の番号・地積と求積方法・測量年月日（問題文の注5）。G点は8月の時点では筆界点ではない。',
         ha='center', va='center', fontsize=13, linespacing=1.6)
ax = fig.add_axes([fx3(80.6), fy3(256.8), fx3(382.6) - fx3(80.6), fy3(25.8) - fy3(256.8)])
fw_m = (ORIG_FRAME_MM[2] - ORIG_FRAME_MM[0]) / 4               # 枠の中の東西（Y）の長さ（m）75.5
fh_m = (ORIG_FRAME_MM[3] - ORIG_FRAME_MM[1]) / 4               # 南北（X）の長さ（m）57.75
c3 = P(691.7, 697.3)
fit(ax, [c3 + P(-fh_m / 2, -fw_m / 2), c3 + P(fh_m / 2, fw_m / 2)], margin=0.0, pad_aspect=True)
assert abs(((ax.get_xlim()[1] - ax.get_xlim()[0]) - fw_m)) < 0.05, ax.get_xlim()
z = Zu(ax, fontsize=15)
fit(ax, [c3 + P(-fh_m / 2, -fw_m / 2), c3 + P(fh_m / 2, fw_m / 2)], margin=0.0, pad_aspect=True)
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
        z.callout((p + q) / 2, s, dirs=(150, 170, 130, 190), dists=(45, 60, 75, 95), fs=13)
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
z.free_text(P(684.5, 708.0), '（単位：ｍ）\n◎ コンクリート杭：A・B・H・J\n● 金属標：C・F・I\n△ 基準点：T1・T2', fs=13,
            ha='left', va='bottom', offsets=((0, 0), (0, 30), (0, 60)))
ALL_PROBLEMS += save(fig, [z], 'R5_dai21mon_zu14_chiseki_sokuryouzu.png')

# =====================================================================
# 図7：問4 10月16日の地目変更・分合筆
# =====================================================================
fig, (ax,) = new_figure('問4　登録免許税は分合筆後の2個（1番1・1番4）× 1,000円 ＝ 2,000円',
                        '分合筆の後に残る土地は、宅地になった1番1（357.59㎡）と、細長い部分の1番4（3.52㎡）の2個。1,000円 × 2個 ＝ 金2,000円。\n'
                        '1番2（西側部分）は変わらないので数えない。合筆で1筆になるからと1個で1,000円にしない。地目変更には登録免許税はかからない。\n'
                        '（登録免許税法別表第一の一（十三）イ・ロ。個数は分筆・合筆の後の土地の数）')
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
ALL_PROBLEMS += save(fig, [z], 'R5_dai21mon_zu18_tourokumenkyozei.png')

# =====================================================================
# 図8：問5 地図作成のための職権の分筆・合筆（流れ図。座標なし）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問5　地図作成のための職権の分筆・合筆（不動産登記法第39条第3項）', fontsize=24, weight='bold', y=0.95)
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
path = os.path.join(OUT, 'R5_dai21mon_zu20_shokken_bungouhitsu.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図8: 流れ図（固定配置）\n  →', path)

# =====================================================================
# 図9：問2 B点の別解（CGから西へ1.00mの点 C − 1i を通る南北の線とACの交点）
# 2026-10-02追加（予備校の解説と見比べて記事に足した別解の図）
# =====================================================================
M1 = C - 1j                                            # CGから西へ1.00mの点
assert abs(M1 - P(702.79, 702.62)) < 1e-9
assert r2(A + (C - A) * (M1.imag - A.imag) / (C.imag - A.imag)) == B
fig, (ax,) = new_figure('問2　B点の別解（CGから西へ1.00mの点を作って、ACとの交点を出す）',
                        'CGは真北向きなので、CGから西へ直角に1.00m離れた点は C − 1i ＝（702.79, 702.62）。この点を通る南北の線（Y＝702.62）と直線ACの交点がB。\n'
                        '結果は本解（B ＝ A ＋ (C − A) × 9.86 ÷ 10.86）と同じ（702.67, 702.62）。線が南北なら、Y座標の差の比で進むほうがキーが少ない。')
z = Zu(ax, fontsize=14)
Q1 = A + (C - A) * 0.55                                # 直線ACの途中（ここから西はAへ続く）
S1, S2 = P(700.6, C.imag), P(700.6, M1.imag)          # CGとBHの線を南へ伸ばした端
fit(ax, [Q1, C, M1, S1, S2], margin=0.16, pad_aspect=True)
z.line(Q1, C, lw=2.4)
z.line(C, S1, lw=2.4)
z.line(M1, S2, color=RED, lw=2.0, ls='--')
z.dim_line(M1, C, color=RED)
z.north_arrow(length=0.08)
z.point(C, 'metal')
z.point_label(C, 'C', away=C + P(-3, -3))
z.point(M1, 'dot', color=RED)
z.point(B, 'dot', color=RED)
z.callout(M1, 'C − 1i ＝（702.79, 702.62）\nCGから西へ直角に1.00m', dirs=(70, 50, 90, 110), color=RED, dists=(70, 95, 120))
z.callout(B, 'B（702.67, 702.62）\n直線ACとY＝702.62の交点', dirs=(-140, -120, -160, 160), color=RED, dists=(90, 115, 140))
z.free_text((M1 + C) / 2, '1.00', fs=15, color=RED, offsets=((0, -20), (0, -28), (0, 20)))
z.free_text(P(701.3, C.imag), 'CG（Y＝703.62）', fs=14, offsets=((70, 0), (80, 0)))
z.free_text(P(701.3, M1.imag), 'BHの線（Y＝702.62）', fs=14, color=RED, offsets=((-85, 0), (-95, 0)))
z.free_text((Q1 + B) / 2, '直線AC（北の筆界。西のAへ続く）', fs=14, offsets=((0, 24), (0, 34), (0, -24)))
ALL_PROBLEMS += save(fig, [z], 'R5_dai21mon_zu07_B_betsukai.png')

# =====================================================================
# 図10：本番で解く順番（いちばん重い問3の作図を最後に）
# 2026-10-02追加
# =====================================================================
fig = plt.figure(figsize=(16, 8), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('本番で解く順番　問3の作図は最後に回す', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
STEPS = [
    ('1', '問5と問1のア・イ\n（条文と定義）', '第5欄・第1欄', BLUE),
    ('2', '問1のウ・エ\n（X座標の引き算と\n辺長の足し算）', '第1欄', BLUE),
    ('3', '問2のB点・H点と\n辺長8本', '第2欄', BLUE),
    ('4', '問4の申請書\n（台形と問題文の注9）', '第4欄', GREEN),
    ('5', '問3の作図\n（点を落として線を引く）', '第3欄', RED),
]
w, h, gap = 17.6, 44, 2.5
for i, (no, t, ran, col) in enumerate(STEPS):
    x = 1 + i * (w + gap)
    ax.add_patch(FancyBboxPatch((x, 22), w, h, boxstyle='round,pad=0.4', facecolor=col, alpha=0.14, edgecolor=col,
                                lw=2))
    ax.text(x + w / 2, 22 + h - 3, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
    ax.text(x + w / 2, 22 + h / 2 - 4, t, ha='center', va='center', fontsize=16, linespacing=1.55)
    ax.text(x + w / 2, 17, ran, ha='center', va='top', fontsize=15, color=col, weight='bold')
    if i < len(STEPS) - 1:
        ax.annotate('', xy=(x + w + gap - 0.3, 44), xytext=(x + w + 0.3, 44),
                    arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
ax.text(1 + 1.5 * (w + gap) - gap / 2, 78, '電卓はB点と斜めの辺（AB・BC・FJ）だけ', ha='center', fontsize=15, color=BLUE,
        weight='bold')
ax.annotate('', xy=(1 + 3 * (w + gap) - gap, 74), xytext=(1, 74), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
ax.text(1 + 3 * (w + gap) + w / 2, 78, '地積測量図がなくても書ける', ha='center', fontsize=15, color=GREEN, weight='bold')
ax.text(1 + 4 * (w + gap) + w / 2, 78, 'いちばん重い', ha='center', fontsize=15, color=RED, weight='bold')
fig.text(0.5, 0.09, '問4の地積は、斜線部分22.09・細長い部分3.5295を台形で出し、1番1は 335.5096500 ＋ 22.09 ＝ 357.59965 → 357.59（問題文の注9）。\n'
         '作図に手間取っても、座標・穴埋め・申請書は取りこぼさない順番にする。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R5_dai21mon_zu21_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図10: 解く順番（固定配置）\n  →', path)

# =====================================================================
# 2026-10-26追加の図（品質チェック 6-2：藍子の誤答・トリ先生の判断の会話の直後に、その論点専用の図）。画像の中に図番は入れない
#   zu01 全体の時系列、zu03 注の仕分け、zu04 合筆で消えた点は足して比べる、zu10 台形の面積、zu11 公差、
#   zu12 書くもの・書かないもの、zu13 G点は書かない、zu15 分合筆の仕組み、zu16 10月の時系列、
#   zu17 地積の端数の援用、zu19 土地の表示の行ごとの書き方
# =====================================================================
import math as _m  # noqa: E402
from calc_helpers import chiseki as _chiseki  # noqa: E402,F401


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


def cell(ax, x, y, w, h, txt, fs=14, fc='white', ec=BLACK, color=BLACK, weight='normal', ha='center', lw=1.3):
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, lw=lw))
    tx = x + w / 2 if ha == 'center' else x + 1.0
    ax.text(tx, y + h / 2, txt, ha=ha, va='center', fontsize=fs, color=color, weight=weight, linespacing=1.4)


# ---- zu01：全体の時系列（第1章） ----
fig, ax = board(8)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('全体の時系列　8月の申請が問1〜問3、10月の申請が問4（問5は別の土地）', fontsize=24, weight='bold', y=0.965)
EV = [  # (x, 日付, 出来事, 色, 上下)
    (4, '4月1日', '桜ストアと売買契約\n花山とは8月31日までに\n移転登記する約束', GRAY, 1),
    (14, '5月31日', '既存店舗の\n解体工事が完了', GRAY, -1),
    (24, '6月1日', '本件工事・新店舗の\n新築工事に着手', GRAY, 1),
    (34, '8月7日', 'G点にコンクリート杭\nを設置（亡失のため）', GRAY, -1),
    (44, '8月10日', '乙土地の分筆を申請\n（問1〜問3）', BLUE, 1),
    (53, '8月21日', '同上 完了', BLUE, -1),
    (62, '8月31日', '花山への所有権の\n移転登記の期限', GRAY, 1),
    (71, '9月20日', '工事完了・営業開始\n抵当権の抹消を申請', GRAY, -1),
    (80, '9月29日', '抵当権の抹消\n完了', GRAY, 1),
    (92, '10月16日', '甲土地・斜線部分の\n登記を申請（問4）', RED, -1),
]
ax.annotate('', xy=(99, 50), xytext=(0.5, 50), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, d, tx_, col, ud in EV:
    ax.plot([x], [50], 'o', ms=12, color=col, zorder=5)
    ax.plot([x, x], [50, 50 + ud * 10], color=col, lw=1.4)
    ax.text(x, 50 + ud * 11, d, ha='center', va='bottom' if ud > 0 else 'top', fontsize=14, color=col, weight='bold')
    ax.text(x, 50 + ud * 18, tx_, ha='center', va='bottom' if ud > 0 else 'top', fontsize=12, color=BLACK, linespacing=1.5)
for x0, x1, tx_, col in [(40, 57, '8月の申請：問1〜問3', BLUE), (86, 99, '10月の申請：問4', RED)]:
    ax.add_patch(plt.Rectangle((x0, 2), x1 - x0, 9, color=col, alpha=0.18, lw=0))
    ax.text((x0 + x1) / 2, 6.5, tx_, ha='center', va='center', fontsize=14, color=col, weight='bold')
fig.text(0.5, 0.035, '8月の分筆では、甲土地にまだ抵当権があり、地目も雑種地のまま。10月16日の申請の日には、抵当権は消え、8月21日の登記で1番2・1番4ができている。',
         ha='center', fontsize=14)
put_board(fig, 'R5_dai21mon_zu01_jikeiretsu_zentai.png')

# ---- zu03：注の仕分け（第1章） ----
fig, ax = board(10.5)
fig.suptitle('注の仕分け　問題文の注1〜9と、調査図素図の注1〜3は番号が別', fontsize=24, weight='bold', y=0.965)
xs, ws = [2, 9, 62], [7, 53, 36]
for x, w, tx_ in zip(xs, ws, ['注', '問題文の注', 'どこで使うか']):
    cell(ax, x, 90, w, 6, tx_, fs=14, fc='#eeeeee', weight='bold')
CHUU = [('1', '適法に行われ、必要な書類はそろっている', '読み飛ばす', GRAY),
        ('2', '登記の申請は書面申請', '読み飛ばす', GRAY),
        ('3', '座標値は小数第3位を四捨五入', 'B点（問2）', BLUE),
        ('4', '地積測量図は250分の1。辺長は小数第3位を四捨五入', '問3 辺長8本・縮尺', BLUE),
        ('5', '地積測量図に書かない：座標値・系の番号・地積と求積方法・測量年月日', '問3 書かないもの', RED),
        ('6', '基準点T1・T2は点名を付けて描く（座標値は不要）', '問3 基準点', BLUE),
        ('7', '分筆後の地番は、西側が1番2、その余が1番4', '問3・問4（地番）', GREEN),
        ('8', '字画・訂正・加入・削除の書き方', '読み飛ばす', GRAY),
        ('9', '申請書の地積の端数は、提出済みの地積測量図から援用', '問4（357.59）', RED)]
for r, (n, tx_, use, col) in enumerate(CHUU):
    y = 84 - r * 6.0
    fc = '#f3f3f3' if col == GRAY else 'white'
    cell(ax, xs[0], y, ws[0], 6.0, n, fs=14, fc=fc, weight='bold', color=col)
    cell(ax, xs[1], y, ws[1], 6.0, tx_, fs=13, fc=fc, ha='left', color=GRAY if col == GRAY else BLACK)
    cell(ax, xs[2], y, ws[2], 6.0, use, fs=13, fc=fc, color=col, weight='bold')
ax.text(2, 28.5, '調査図素図（図の下）の注', fontsize=15, weight='bold', color=PURPLE)
for r, (n, tx_, use) in enumerate([('1', 'B点は、A点とC点を結ぶ直線上にある', 'B点（問2）'),
                                   ('2', 'H点は、G点とI点を結ぶ直線上にある', 'H点（問2）・分筆線'),
                                   ('3', 'I点は、A点とJ点を結ぶ直線上にある', '分筆線のI点')]):
    y = 21.5 - r * 6.0
    cell(ax, xs[0], y, ws[0], 6.0, n, fs=14, weight='bold', color=PURPLE)
    cell(ax, xs[1], y, ws[1], 6.0, tx_, fs=13, ha='left')
    cell(ax, xs[2], y, ws[2], 6.0, use, fs=13, color=PURPLE, weight='bold')
fig.text(0.5, 0.035, '記事では「問題文の注3」「調査図素図の注2」のように、どちらの注かを書き分ける。色：青＝計算・作図で使う、赤＝書き漏らしやすい、緑＝地番、灰＝読み飛ばす。',
         ha='center', fontsize=14)
put_board(fig, 'R5_dai21mon_zu03_chuu_shiwake.png')

# ---- zu04：合筆で消えた中間の点は2本を足して比べる（問1） ----
Wm = A + (J - A) * 10.33 / 20.99                       # 1番2と1番3の西側の境（平成25年の合筆で消えた）
Em = C + (F - C) * 11.64 / 22.65                       # 同・東側の境
assert abs(abs(Em - Wm) - 10.86) < 0.03, abs(Em - Wm)
assert f'{10.33 + 10.66:.2f}' == '20.99' and f'{11.64 + 11.01:.2f}' == '22.65'
fig, (ax1, ax2) = new_figure('問1　合筆で消えた中間の点は、2本の辺長を足して今回の距離と比べる',
                             '平成15年の地積測量図では、西の辺が10.33と10.66、1番1との境が11.64と11.01に分かれていた。\n平成25年9月1日の合筆で、間の筆界（約10.86）は消えている。\n'
                             '足した値が今回の座標の距離と一致するのは、C→F 22.65 とA→J 20.99（F点・J点）。\nG点・I点まででは、C→G 22.15・A→I 20.84で合わない。',
                             ncols=2)
zl = Zu(ax1, fontsize=14)
fit(ax1, OTSU, margin=0.45, pad_aspect=True)
zl.poly(OTSU, lw=2.0)
zl.line(Wm, Em, color=GRAY, lw=1.6, ls='--')
zl.north_arrow(length=0.07)
ax1.set_title('平成15年の地積測量図（合筆の前）', fontsize=17, weight='bold', pad=6)
co_ = centroid(OTSU)
zl.edge_label(A, Wm, '10.33', co_, fs=14, color=BLUE)
zl.edge_label(Wm, J, '10.66', co_, fs=14, color=BLUE)
zl.edge_label(C, Em, '11.64', co_, fs=14, color=BLUE)
zl.edge_label(Em, F, '11.01', co_, fs=14, color=BLUE)
zl.free_text(Wm + (Em - Wm) * 0.5 + P(2.5, 0), '1番2（北）\n―――\n1番3（南）', fs=14, color=GRAY)
zl.free_text(Wm + (Em - Wm) * 0.5 + P(-1.2, 0), '合筆で消えた線', fs=13, color=GRAY)
for p, n in [(A, 'A'), (C, 'C'), (F, 'F'), (J, 'J')]:
    zl.point(p, 'concrete' if n in 'AJ' else 'metal')
    zl.point_label(p, n, away=co_)
zl.point(Wm, 'dot', color=GRAY)
zl.point(Em, 'dot', color=GRAY)
zr = Zu(ax2, fontsize=14)
fit(ax2, OTSU, margin=0.45, pad_aspect=True)
zr.poly(OTSU, lw=2.0, fill=BLUE, alpha=0.18)
zr.north_arrow(length=0.07)
ax2.set_title('今回の座標から出した距離', fontsize=17, weight='bold', pad=6)
zr.edge_label(A, J, 'A→J ＝ 20.99', co_, fs=14, color=RED)
zr.edge_label(C, F, 'C→F ＝ 22.65', co_, fs=14, color=RED)
zr.free_text(co_, '10.33 ＋ 10.66 ＝ 20.99\n11.64 ＋ 11.01 ＝ 22.65\n→ 一致', fs=15, color=RED)
for p, n in [(A, 'A'), (C, 'C'), (F, 'F'), (J, 'J')]:
    zr.point(p, 'concrete' if n in 'AJ' else 'metal')
    zr.point_label(p, n, away=co_)
ALL_PROBLEMS += save(fig, [zl, zr], 'R5_dai21mon_zu04_gappitsu_tashizan.png')

# ---- zu10：面積は台形で（問3の計算過程） ----
fig, ax = board(9)
fig.suptitle('問3　面積は台形で　（平行な2辺の和 ÷ 2 × 平行な2辺の間の幅）', fontsize=24, weight='bold', y=0.965)
TRAP = [  # (見出し, 色, 左辺, 右辺, 幅, 式, 結果, 地積)
    ('1番2（A・B・H・I）', BLUE, 'AI 20.84', 'BH 22.03', '9.86', '(20.84 ＋ 22.03) ÷ 2 × 9.86', '＝ 211.3491', '→ 211.34㎡'),
    ('斜線部分（B・C・G・H）', PURPLE, 'BH 22.03', 'CG 22.15', '1.00', '(22.03 ＋ 22.15) ÷ 2 × 1.00', '＝ 22.09', '→ 22.09㎡'),
    ('細長い部分（I・H・G・F・J）', ORANGE, 'IJ 0.15', 'GF 0.50', '10.86', '(0.15 ＋ 0.50) ÷ 2 × 10.86', '＝ 3.5295', '→ 3.52㎡'),
]
assert abs(area(N2) - (20.84 + 22.03) / 2 * 9.86) < 1e-6 and abs((22.03 + 22.15) / 2 * 1.00 - 22.09) < 1e-9
assert abs((0.15 + 0.50) / 2 * 10.86 - 3.5295) < 1e-9
for k, (hd, col, la, ra, hh, fm, res, ch) in enumerate(TRAP):
    x0 = 3 + k * 32.5
    ax.add_patch(plt.Rectangle((x0, 35), 30, 52, facecolor='white', edgecolor=col, lw=2))
    ax.text(x0 + 15, 84, hd, ha='center', va='center', fontsize=15, weight='bold', color=col)
    if k < 2:
        L, R = (13, 15) if k == 0 else (15, 15.2)
    else:
        L, R = (2.5, 6.5)                              # 図は誇張（0.15と0.50の台形）
    mid = 61
    poly_ = [(x0 + 6, mid - L), (x0 + 24, mid - R), (x0 + 24, mid + R), (x0 + 6, mid + L)]
    ax.add_patch(plt.Polygon(poly_, closed=True, facecolor=col, alpha=0.30, edgecolor=col, lw=2))
    ax.text(x0 + 4.5, mid, la, rotation=90, ha='center', va='center', fontsize=12)
    ax.text(x0 + 25.8, mid, ra, rotation=90, ha='center', va='center', fontsize=12)
    ax.annotate('', xy=(x0 + 24, 41), xytext=(x0 + 6, 41), arrowprops=dict(arrowstyle='<->', lw=1.4, color=BLACK))
    ax.text(x0 + 15, 38, f'幅 {hh}（Y座標の差）', ha='center', va='center', fontsize=12)
    ax.text(x0 + 15, 28, fm, ha='center', va='center', fontsize=15)
    ax.text(x0 + 15, 22, res, ha='center', va='center', fontsize=17, weight='bold', color=col)
    ax.text(x0 + 15, 16, ch, ha='center', va='center', fontsize=17, weight='bold')
ax.text(3 + 2 * 32.5 + 15, 91.5, '', fontsize=12)
ax.text(3 + 2 * 32.5 + 15, 32.5, '（図は誇張。IJ 0.15 はごく細い）', ha='center', va='center', fontsize=11, color=GRAY)
ax.add_patch(plt.Rectangle((3, 3), 94.5, 9, facecolor='#f6f6f6', edgecolor=GRAY, lw=1.2))
ax.text(50, 7.5, '1番4 ＝ 22.09 ＋ 3.5295 ＝ 25.6195 → 25.61㎡　／　1番2 ＋ 1番4 ＝ 211.3491 ＋ 25.6195 ＝ 236.9686（乙土地の236.9652と0.0034違うのはB点を丸めたため）',
        ha='center', va='center', fontsize=13)
put_board(fig, 'R5_dai21mon_zu10_daikei_menseki.png')

# ---- zu11：公差の判定（問3の前提。数直線） ----
KOUSA = (0.05 + 0.01 * 236.81 ** 0.25) * _m.sqrt(236.81)
assert f'{KOUSA:.2f}' == '1.37'
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問3　地積更正は要らない　実測・分筆後の合計は、登記記録236.81㎡の公差の内側', fontsize=24, weight='bold', y=0.96)
ax = fig.add_axes([0.05, 0.30, 0.90, 0.50])
ax.set_xlim(232.8, 239.2)
ax.set_ylim(-2.6, 2.6)
ax.axis('off')
ax.plot([233.0, 239.0], [0, 0], color=BLACK, lw=2)
for v in range(233, 240):
    ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1.2)
    ax.text(v, -0.25, f'{v}', ha='center', va='top', fontsize=13, color=GRAY)
ax.axvspan(236.81 - KOUSA, 236.81 + KOUSA, ymin=0.45, ymax=0.60, color=GREEN, alpha=0.25)
ax.text(236.81, 0.55, f'公差の範囲（236.81 ± 約1.37）　市街地地域の甲2（参考）', ha='center', va='bottom', fontsize=14, color=GREEN)
ax.plot([236.81], [0], 'o', ms=12, color=BLUE)
ax.text(236.81, -0.75, '登記記録\n236.81㎡', ha='center', va='top', fontsize=15, color=BLUE, weight='bold')
ax.plot([236.9652], [0], 'o', ms=10, color=RED)
ax.text(237.35, 1.55, '実測 236.9652㎡\n（差 0.1552）', ha='left', va='bottom', fontsize=15, color=RED, weight='bold')
ax.plot([237.35, 236.9652], [1.55, 0.05], color=RED, lw=0.9)
ax.plot([236.95], [0], 'o', ms=10, color=GREEN)
ax.text(236.35, -1.65, '分筆後の合計 236.95㎡\n（211.34 ＋ 25.61。差 0.14）', ha='center', va='top', fontsize=15, color=GREEN, weight='bold')
ax.plot([236.35, 236.95], [-1.62, -0.05], color=GREEN, lw=0.9)
ax.plot([233.4357], [0], 'o', ms=12, color=GRAY)
ax.text(233.55, 1.1, 'G・Iを通した乙土地 233.4357㎡\n（差 3.3743 ＞ 約1.37 → 範囲の外）', ha='left', va='bottom', fontsize=14, color=GRAY, weight='bold')
fig.text(0.5, 0.17, '地域で決まる精度区分は、市街地地域なら甲2まで（不動産登記規則第10条第4項第1号、第77条第5項）。「乙土地」という呼び名につられて乙1にしない。\n'
         '問題文に公差の表はないので、ここは参考の計算。分筆後の合計と登記記録の差が公差の範囲内なら、地積更正の登記は要らない（準則第72条第1項）。\n'
         '8月10日の申請は、土地分筆登記だけ。', ha='center', va='center', fontsize=15, linespacing=1.7)
path = os.path.join(OUT, 'R5_dai21mon_zu11_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] zu11: 数直線（固定配置）\n  →', path)

# ---- zu12：地積測量図に書くもの・書かないもの（問題文の注5・注6） ----
fig, ax = board(9)
fig.suptitle('問3　地積測量図に書くもの・書かないもの・印刷済みのもの', fontsize=24, weight='bold', y=0.965)
COLS = [('書く', GREEN, ['辺長8本（単位：m）', '分筆線 B→H→I', '（イ）1－2・（ロ）1－4の\n符号と地番', '方位記号\n（印刷なし。自分で描く）',
                      '隣接地の地番\n（3－1・1－1・2－1）と道路', '境界標の記号（A・B・H・Jは\nコンクリート杭、C・F・Iは金属標）',
                      '基準点T1・T2の位置と点名\n（問題文の注6）']),
        ('書かない', RED, ['各筆界点の座標値\n（問題文の注5）', '平面直角座標系の番号\n（問題文の注5）', '地積とその求積方法\n（問題文の注5）', '測量の年月日\n（問題文の注5）',
                        'T1・T2の座標値\n（問題文の注6）', 'G点\n（8月の時点では筆界点ではない）']),
        ('印刷済み・欄に記入', BLUE, ['作成者・申請人の欄は\n「（略）」と印刷', '作成日の欄\n（令和5年○月○日作成）', '縮尺 1／250 の印刷',
                              '地番の欄に\n「1番2、1番4」と記入', '土地の所在の欄に\n「Ａ市Ｂ町二丁目」と記入'])]
for k, (hd, col, items) in enumerate(COLS):
    x0 = 3 + k * 32.5
    ax.add_patch(plt.Rectangle((x0, 4), 30, 86, facecolor='white', edgecolor=col, lw=2.2))
    ax.add_patch(plt.Rectangle((x0, 82), 30, 8, facecolor=col, alpha=0.18, edgecolor=col, lw=2.2))
    ax.text(x0 + 15, 86, hd, ha='center', va='center', fontsize=19, weight='bold', color=col)
    for r, it in enumerate(items):
        yy = 76 - r * 11.0
        wrap = it
        ax.text(x0 + 1.5, yy, '・' + wrap.replace('\n', '\n　'), ha='left', va='center', fontsize=13.5, linespacing=1.4)
fig.text(0.5, 0.035, '書き漏らしやすいのは、辺長の単位の表示・基準点の点名・方位記号。書かなくてよいものを書いても減点にはならないが、時間を食う。',
         ha='center', fontsize=14)
put_board(fig, 'R5_dai21mon_zu12_kaku_kakanai.png')

# ---- zu13：G点は8月の地積測量図に描かない（問3） ----
fig, (ax1, ax2) = new_figure('問3　G点は8月の地積測量図に描かない（筆界点になるのは10月）',
                             '8月の分筆：Gは筆界C→Fの途中にあるだけで、筆界の折れ点でも分筆線の端でもない。\n'
                             '地積測量図に書く境界標は筆界点にあるもの（不動産登記規則第77条第1項第9号）。\n'
                             '10月の分合筆：斜線部分（B・C・G・H）の南東の角がG。1番4から斜線部分を切り離すので、ここが新しい筆界点になる。',
                             ncols=2)
zl = Zu(ax1, fontsize=14)
fit(ax1, OTSU, margin=0.45, pad_aspect=True)
ax1.set_title('8月10日の地積測量図（1番2・1番4）', fontsize=17, weight='bold', pad=6)
zl.poly(OTSU, lw=2.0)
zl.poly([B, H, I], lw=2.0, closed=False)
zl.north_arrow(length=0.07)
for p, n in [(A, 'A'), (B, 'B'), (H, 'H'), (J, 'J')]:
    zl.point(p, 'concrete')
for p, n in [(C, 'C'), (F, 'F'), (I, 'I')]:
    zl.point(p, 'metal', size=8)
for p, n in [(A, 'A'), (C, 'C'), (F, 'F'), (J, 'J'), (B, 'B')]:
    zl.point_label(p, n, away=co_)
zl.point_label(H, 'H', away=centroid(N2))
zl.point(G, 'dot', color=GRAY)
zl.callout(G, 'G は描かない\n（C→Fの途中の点）', dirs=(-30, -50, -70, 0), color=GRAY, dists=(60, 80, 100))
zr = Zu(ax2, fontsize=14)
fit(ax2, OTSU, margin=0.45, pad_aspect=True)
ax2.set_title('10月16日の分合筆（斜線部分を1番1へ）', fontsize=17, weight='bold', pad=6)
zr.poly(OTSU, color=GRAY, lw=1.2)
zr.poly(SHA, fill=PURPLE, alpha=0.35)
zr.north_arrow(length=0.07)
for p, n in [(B, 'B'), (C, 'C'), (H, 'H')]:
    zr.point(p, 'concrete' if n != 'C' else 'metal')
    zr.point_label(p, n, away=co_)
zr.point(G, 'concrete', color=RED)
zr.callout(G, 'G は筆界点（角）\n8月7日に入れ直した杭', dirs=(-30, -50, -70, 0), color=RED, dists=(60, 80, 100))
ALL_PROBLEMS += save(fig, [zl, zr], 'R5_dai21mon_zu13_G_kakanai.png')

# ---- zu15：丸ごと合筆ではなく分合筆（問4） ----
fig, (ax1, ax2) = new_figure('問4　1番4を丸ごと合筆しない　斜線部分だけを分筆して、1番1に合筆する（分合筆）',
                             '左（誤り）：1番4は斜線部分のほかに、南の細長い部分も含む。\n丸ごと合筆すると、桜ストアに売らない細長い部分まで1番1に入ってしまう。\n'
                             '右（正しい）：1番4の一部（斜線部分）を分筆して1番1に合筆する。\n分筆の登記と合筆の登記は、一の申請情報で申請できる（不動産登記規則第35条第1号）。',
                             ncols=2)
for ax_, ok in [(ax1, False), (ax2, True)]:
    zz = Zu(ax_, fontsize=14)
    fit(ax_, OTSU + KOU, margin=0.16, pad_aspect=True)
    zz.poly(N2, color=GRAY, lw=1.2)
    zz.poly(KOU, fill=GREEN)
    zz.poly(SHA, fill=PURPLE, alpha=0.40)
    if ok:
        zz.poly(HOSO, fill=ORANGE, alpha=0.55)
    else:
        zz.poly(HOSO, fill=RED, alpha=0.45)
    zz.north_arrow(length=0.07)
    zz.free_text(centroid(KOU), '1番1', fs=19)
    zz.free_text(centroid(N2), '1番2\n（花山へ）', fs=15, color=GRAY)
    zz.callout(C + (G - C) * 0.55, '斜線部分 22.09㎡', dirs=(0, 15, -15), color=PURPLE, dists=(110, 140, 170))
    if ok:
        zz.callout(I + (G - I) * 0.25, '細長い部分 3.52㎡\n1番4に残る', dirs=(-80, -60, -100), color=ORANGE, dists=(60, 80, 100))
        ax_.set_title('分合筆（正しい）', fontsize=18, weight='bold', color=GREEN, pad=6)
    else:
        zz.callout(I + (G - I) * 0.25, '細長い部分も\n1番1に入ってしまう', dirs=(-80, -60, -100), color=RED, dists=(60, 80, 100))
        ax_.set_title('丸ごと合筆（誤り）', fontsize=18, weight='bold', color=RED, pad=6)
    for p, n in [(B, 'B'), (C, 'C'), (D, 'D'), (E, 'E')]:
        zz.point(p, 'dot')
        zz.point_label(p, n, away=centroid(KOU) if n in 'DE' else centroid(N2))
    if ok:
        zz.__dict__.setdefault('_z', None)
    if ok:
        zr15 = zz
    else:
        zl15 = zz
ALL_PROBLEMS += save(fig, [zl15, zr15], 'R5_dai21mon_zu15_bungouhitsu_shikumi.png')

# ---- zu16：10月16日の申請までの時系列と、地目変更を入れる理由（問4） ----
fig, ax = board(9)
fig.suptitle('問4　10月16日の申請までの時系列　地目が違う土地は合筆できないので、地目変更を同じ申請に入れる', fontsize=22, weight='bold', y=0.965)
EV2 = [(10, '8月21日', '乙土地の分筆\nの登記が完了\n（1番2・1番4）', BLUE, 1),
       (30, '9月20日', '工事完了・営業開始\n→ 甲土地と斜線部分\nは宅地になる', GREEN, -1),
       (45, '9月20日', '甲土地の抵当権の\n抹消を申請', GRAY, 1),
       (60, '9月29日', '抵当権の抹消\n完了', GRAY, -1),
       (76, '10月16日', '申請\n（問4）', RED, 1),
       (92, '10月20日', '地目変更の\n期限（1月以内）', ORANGE, -1)]
ax.annotate('', xy=(99, 70), xytext=(0.5, 70), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, d, tx_, col, ud in EV2:
    ax.plot([x], [70], 'o', ms=12, color=col, zorder=5)
    ax.plot([x, x], [70, 70 + ud * 8], color=col, lw=1.4)
    ax.text(x, 70 + ud * 9, d, ha='center', va='bottom' if ud > 0 else 'top', fontsize=14, color=col, weight='bold')
    ax.text(x, 70 + ud * 15, tx_, ha='center', va='bottom' if ud > 0 else 'top', fontsize=12, color=BLACK, linespacing=1.5)
BOX = [('地目が違う土地は合筆できない', '1番1は雑種地、1番4は宅地。\n不動産登記法第41条第2号', RED),
       ('地目変更を同じ申請情報に入れる', '1番1を宅地にする地目変更と分合筆は、\n一の申請情報でよい（規則第35条第7号）', GREEN),
       ('抵当権は消えている', '9月29日に抹消が完了。\n合筆の制限なし（法第41条第6号）', BLUE)]
for k, (hd, tx_, col) in enumerate(BOX):
    x0 = 3 + k * 32.5
    ax.add_patch(plt.Rectangle((x0, 4), 30, 24, facecolor='white', edgecolor=col, lw=2.2))
    ax.text(x0 + 15, 23.5, hd, ha='center', va='center', fontsize=14.5, weight='bold', color=col)
    ax.text(x0 + 15, 13, tx_, ha='center', va='center', fontsize=13, linespacing=1.6)
put_board(fig, 'R5_dai21mon_zu16_jikeiretsu_10gatsu.png')

# ---- zu17：地積の端数の援用（問題文の注9） ----
assert f'{335 + 22.09:.2f}' == '357.09'
assert f'{chiseki(area(KOU) + 22.09):.2f}' == '357.70'
fig, ax = board(9)
fig.suptitle('問4　1番1の地積　登記記録に足さない・座標で計算し直さない　地積測量図の端数を援用する', fontsize=22, weight='bold', y=0.965)
CARDS = [('誤り　登記記録に足す', RED, '335 ＋ 22.09 ＝ 357.09',
          '335は雑種地だから1㎡未満を切り捨てた値。\n宅地になれば小数第2位まで書くので、\n端数が足りない。'),
         ('誤り　座標で計算し直す', RED, '335.6129 ＋ 22.09 ＝ 357.70…',
          '甲土地（C・D・E・F）を座標で出し直した値。\n問題文の注9は「提出済みの地積測量図に\n記載された端数を援用する」と指示している。'),
         ('正しい　地積測量図の端数', GREEN, '335.5096500 ＋ 22.09\n＝ 357.59965 → 357.59',
          '平成15年の地積測量図の三斜求積表にある\n1番1の面積 335.5096500 を使う。\n宅地は小数第2位未満を切り捨てる。')]
for k, (hd, col, fm, note) in enumerate(CARDS):
    x0 = 3 + k * 32.5
    ax.add_patch(plt.Rectangle((x0, 12), 30, 74, facecolor='white', edgecolor=col, lw=2.4))
    ax.add_patch(plt.Rectangle((x0, 76), 30, 10, facecolor=col, alpha=0.16, edgecolor=col, lw=2.4))
    ax.text(x0 + 15, 81, hd, ha='center', va='center', fontsize=17, weight='bold', color=col)
    ax.text(x0 + 15, 58, fm, ha='center', va='center', fontsize=17 if k < 2 else 16.5, weight='bold', color=col, linespacing=1.5)
    ax.text(x0 + 15, 30, note, ha='center', va='center', fontsize=13, linespacing=1.7)
fig.text(0.5, 0.045, '分合筆後の1番1は宅地357.59㎡。登記記録の地積（335）は雑種地の表し方なので、足し算のもとにしない。',
         ha='center', fontsize=15)
put_board(fig, 'R5_dai21mon_zu17_chiseki_hasuu.png')

# ---- zu19：土地の表示の行ごとの書き方（問4） ----
fig, ax = board(9)
fig.suptitle('問4　土地の表示の5行　どの行が何を表すか', fontsize=24, weight='bold', y=0.965)
xs, ws = [2, 14, 25, 36, 60], [11, 10, 10, 23, 38]
for x, w, tx_ in zip(xs, ws, ['行', '①地番', '②地目', '③地積／原因', 'この行は何か']):
    cell(ax, x, 86, w, 6, tx_, fs=13.5, fc='#eeeeee', weight='bold')
ROWS5 = [('1行目', '1番4', '宅地', '25.61', '', '分合筆の前の1番4（登記記録の地積）', GRAY),
         ('2行目', '（イ）1番4', '宅地', '3.52', '③1番1に一部合併', '1番4に残る部分（細長い部分）', ORANGE),
         ('3行目', '（ロ）', '', '22.09', '1番4から分筆して1番1に合併する部分', '1番1に入る部分（地番は付けない。\n登記記録は作られない）', PURPLE),
         ('4行目', '1番1', '雑種地', '335', '', '分合筆の前の1番1（登記記録のとおり）', GRAY),
         ('5行目', '1番1', '宅地', '357.59', '②③令和5年9月20日地目変更\n③1番4から一部合併', '分合筆の後の1番1', GREEN)]
for r, (rn, c1, c2, c3, c4, note, col) in enumerate(ROWS5):
    y = 74 - r * 12
    fc = '#fafafa'
    cell(ax, xs[0], y, ws[0], 11, rn, fs=14, weight='bold', color=col)
    cell(ax, xs[1], y, ws[1], 11, c1, fs=14, color=INK)
    cell(ax, xs[2], y, ws[2], 11, c2, fs=14, color=INK)
    cell(ax, xs[3], y, ws[3], 11, (c3 + '\n' + c4) if c4 else c3, fs=13, color=INK)
    cell(ax, xs[4], y, ws[4], 11, note, fs=13, ha='left', color=col, weight='bold')
ax.text(2, 17, '一部合併の書き方（準則第76条）：', fontsize=15, weight='bold')
ax.text(2, 11, '分筆する側の1番4は「1番1に一部合併」、合筆される側の1番1は「1番4から一部合併」。5行目の②③は、地目が変わり、地積の表し方も変わるため。',
        fontsize=13.5)
ax.text(2, 5.5, '2行目の（イ）は地番を書き直さない（1番4のまま）が、地積と原因は変わるので行を立てる。', fontsize=13.5)
put_board(fig, 'R5_dai21mon_zu19_tochi_hyouji_gyou.png')

print('重なりの合計:', len(ALL_PROBLEMS))
