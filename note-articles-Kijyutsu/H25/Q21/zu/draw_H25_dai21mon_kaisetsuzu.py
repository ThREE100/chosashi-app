"""平成25年度 第21問（土地）会話形式note記事の解説図7枚を、座標値から作図する。

`../prompt_H25_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../R6/Q21/zu/draw_R6_dai21mon_kaisetsuzu.py`。

実行: python3 note-articles-Kijyutsu/H25/Q21/zu/draw_H25_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, chiseki  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
A100, A101, A102 = P(137.06, 159.96), P(153.30, 159.78), P(153.81, 182.84)
A, D, G = P(151.43, 162.08), P(139.19, 181.35), P(139.19, 162.08)
B = r2(radial(A101, A100, 11.76, dms(278, 47, 58)))
C = r2(A + (B - A) / abs(B - A) * 19.22)
GF_LEN = abs(D - G) * math.sin(dms(5, 46, 21)) / math.sin(dms(166, 36, 4))
F = r2(G + (D - G) * math.sin(dms(5, 46, 21)) / math.sin(dms(166, 36, 4)) * cmath.rect(1, dms(7, 37, 35)))
E = r2(G + (F - G) / abs(F - G) * 12.58)
Bw = r2(radial(A101, A100, 11.76, -dms(278, 47, 58)))          # 反時計回りに引いた誤り
GFw = abs(D - G) * math.sin(dms(7, 37, 35)) / math.sin(dms(166, 36, 4))
Fw = r2(G + (D - G) / abs(D - G) * GFw * cmath.rect(1, dms(7, 37, 35)))   # G点の角のsinで計算した誤り

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('B', B, P(151.63, 171.42)), ('C', C, P(151.84, 181.30)), ('F', F, P(138.08, 170.37)),
                     ('E', E, P(137.52, 174.55)), ('Bw', Bw, P(151.37, 148.18)), ('Fw', Fw, P(137.73, 173.02))]:
    assert abs(got - want) < 1e-9, (n, got, want)
assert Bw.imag < A101.imag - 11                        # 誤りのBは西の道路を越えた先（A101より11m以上西）
assert Fw.imag - F.imag > 2.6 and Fw.imag < E.imag       # 誤りのFは本当のFより約2.7m東、E点の手前
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'AB': (A, B, '9.34'), 'BC': (B, C, '9.88'), 'CD': (C, D, '12.65'), 'DE': (D, E, '7.00'),
         'EF': (E, F, '4.22'), 'FG': (F, G, '8.36'), 'GA': (G, A, '12.24')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert d2(B, F) == '13.59' and d2(G, D) == '19.27' and d2(D, F) == '11.04' and f'{GF_LEN:.2f}' == '8.36'
assert d2(C, A102) == '2.50' and d2(E, A100) == '14.60' and f'{GFw:.2f}' == '11.04'
LOT = [A, B, C, D, E, F, G]
RO = [A, B, F, G]                   # （ロ）5番2 西側・宅地
I_ = [B, C, D, E, F]                # （イ）5番1 東側・雑種地
assert f'{area(RO):.4f}' == '113.9083' and f'{chiseki(area(RO)):.2f}' == '113.90'
assert f'{area(I_):.4f}' == '141.6973' and chiseki(area(I_), takuchi=False) == 141
assert f'{area(LOT):.4f}' == '255.6056'
assert f'{255 - 141.69730:.2f}' == '113.30'
BRG_A100 = math.degrees(cmath.phase(A100 - A101))                # A101→A100の方向角 179.36°
assert to_dms(math.radians(BRG_A100)) == '179°21′53.91″'
BRG_B = BRG_A100 + 278 + 47 / 60 + 58 / 3600                      # 458.16°（＝98.16°）
assert to_dms(math.radians(BRG_B - 360)) == '98°09′51.91″'
print('数値の照合: すべて一致')


def marks(z, pts_labels, away):
    """境界標の記号と点名（A・C・G＝コンクリート杭、D・E＝石杭、B・F＝金属標）。"""
    for p, n in pts_labels:
        if n in 'ACG':
            z.point(p, 'concrete')
        elif n in 'DE':
            z.point(p, 'stone')
        else:
            z.point(p, 'metal', size=9)
        z.point_label(p, n, away=away)


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


ALL_PROBLEMS = []
ALL7 = [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (G, 'G')]

# =====================================================================
# 図1：全体像（北を上にして座標どおりに描き直した調査素図）
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像（平成25年8月19日の測量時点）',
                        '本件土地（5番・雑種地・登記記録255㎡）。ブロック塀B→Fの西側は建物（家屋番号5番）の敷地、東側は資材置場。\n'
                        'A・GはY座標が同じ（西の辺は真南北）、G・DはX座標が同じ（点線GDは真東西の補助線で、筆界ではない）。')
z = Zu(ax)
fit(ax, LOT + [A100, A101, A102], margin=0.10, pad_aspect=True)
z.poly(RO, fill=ORANGE, alpha=0.18)
z.poly(I_, fill=GREEN, alpha=0.18)
z.line(B, F, color=RED, lw=5.0)
z.line(G, D, color=GRAY, lw=1.2, ls=':')
z.north_arrow()
cl = centroid(LOT)
z.free_text(centroid(RO), '建物の敷地\n（家屋番号5番）', fs=16)
z.free_text(centroid(I_), '資材置場', fs=16)
marks(z, ALL7, cl)
for p, n in [(A100, 'A100'), (A101, 'A101'), (A102, 'A102')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=cl)
z.callout(B + (F - B) * 0.35, 'ブロック塀（B→F）', dirs=(20, 35, 5), color=RED, dists=(70, 95, 120))
z.callout(G + (D - G) * 0.75, '補助線GD（真東西）', dirs=(80, 60, 100), color=GRAY, dists=(40, 55, 70))
z.edge_label(A, C, '道路', cl, fs=16, dists=(34, 44), rotate=False)
z.edge_label(G, A, '道路', cl, fs=16, dists=(40, 52), rotate=False)
z.edge_label(C, D, '6', cl, fs=16, dists=(30, 40), rotate=False)
z.edge_label(D, E, '3', cl, fs=16, dists=(30, 40), rotate=False)
z.edge_label(F, G, '2', cl, fs=16, dists=(30, 40), rotate=False)
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：問1 B点（A101から放射）とC点の検算
# =====================================================================
fig, (ax,) = new_figure('図2　問1　B点の求め方（A101から放射）',
                        'A101→A100の方向角 179°21′53.91″ に、時計回りの水平角 278°47′58″ を足す（458°09′51.91″＝98°09′51.91″）。11.76m 進む。\n'
                        '反時計回りに引くと、西の道路を越えた（151.37, 148.18）に出てしまう。\n'
                        '検算：C＝A＋(B−A)÷Abs(B−A)×19.22 で出したC点は、A102から2.50（水平角が省略された観測の距離と一致）。')
z = Zu(ax)
fit(ax, [A101, A100 + P(10, 0), B, Bw, C, A102, A], margin=0.10, pad_aspect=True)
z.poly(LOT, color=GRAY, lw=1.1)
z.line(A101, A101 + 3.0, color=GRAY, lw=1.2, ls='--')
z.free_text(A101 + 3.0, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(A101, A101 + (A100 - A101) / abs(A100 - A101) * 5.0, color=BLUE, lw=2.0)
z.line(A101, B, color=RED, lw=2.6)
z.line(A101, Bw, color=GRAY, lw=1.4, ls=':')
z.line(B, C, color=RED, lw=1.6, ls='--')
z.line(C, A102, color=BLUE, lw=1.6, ls='--')
z.north_arrow()
z.angle_arc(A101, 1.3, 0, BRG_A100, color=BLUE)
z.angle_arc(A101, 2.1, BRG_A100, BRG_B, color=RED)
z.point(A101, 'kijun')
z.point(A102, 'kijun')
z.point(B, 'metal', size=9)
z.point(A, 'concrete')
z.point(C, 'concrete')
z.point(Bw, 'dot', color=GRAY)
z.point_label(A, 'A', away=cl)
z.point_label(A102, 'A102', away=cl)
z.callout(A101 + (A100 - A101) / abs(A100 - A101) * 4.2, '後視（A100の方向）', dirs=(-160, -140, -180, -120), color=BLUE,
          dists=(60, 80, 100))
z.edge_label(A101, B, '11.76', A101 + P(-5, 0), color=RED, fs=17, ts=(0.62, 0.72, 0.52), dists=(14, 20, 26))
z.edge_label(C, A102, '2.50', cl, color=BLUE, fs=16, dists=(14, 20, 26), rotate=False)
z.callout(A101 + P(1.3 * math.cos(math.radians(60)), 1.3 * math.sin(math.radians(60))),
          '方向角 179°21′53.91″\n（北から時計回りにA100の方向）', dirs=(100, 120, 80, 140), color=BLUE,
          dists=(80, 110, 140))
z.callout(A101 + P(2.1 * math.cos(math.radians(-110)), 2.1 * math.sin(math.radians(-110))),
          '水平角 278°47′58″\n（A100の方向から時計回り）', dirs=(-120, -140, -100, -160), color=RED, dists=(60, 85, 110))
z.callout(B, 'B（151.63, 171.42）', dirs=(-60, -80, -40, -100), color=RED, dists=(70, 95, 120))
z.callout(C, 'C（151.84, 181.30）', dirs=(115, 130, 100, 150), color=BLACK, dists=(90, 120, 150))
z.callout(Bw, '反時計回りに引いた誤り\n（151.37, 148.18）', dirs=(-90, -60, -120, 90), color=GRAY)
z.callout(A101, 'A101（153.30, 159.78）', dirs=(150, 130, 170, 110), color=BLACK, dists=(110, 140, 170))
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu02_B_housha.png')

# =====================================================================
# 図3：問1 F点（三角形G・D・Fの正弦定理）
# =====================================================================
fig, (ax,) = new_figure('図3　問1　F点の求め方（三角形G・D・Fの正弦定理）',
                        '∠G＝180°−5°46′21″−166°36′04″＝7°37′35″。GF＝GD×sin(∠D)÷sin(∠F)＝19.27×sin5°46′21″÷sin166°36′04″＝8.3638…\n'
                        'GFに向かい合うのはD点の角。G点の角で計算すると11.04（＝DFの長さ）になり、F点が約2.7m東の（137.73, 173.02）にずれる。\n'
                        'F点は点線GDの南なので、G→Dの向きから時計回りに7°37′35″回す。検算：DF＝11.04（GD×sin∠G÷sin∠F と一致）。')
z = Zu(ax)
fit(ax, [G, D, F, E, G + P(-1.0, 0), D + P(1.0, 0)], margin=0.06, pad_aspect=True)
z.line(G, D, color=GRAY, lw=1.6, ls=':')
z.line(G, F, color=RED, lw=3.0)
z.line(F, D, color=BLUE, lw=3.0)
z.line(F, E, color=GRAY, lw=1.2, ls='--')
z.north_arrow()
BRG_GF = math.degrees(math.atan2((F - G).imag, (F - G).real))
BRG_DF = math.degrees(math.atan2((F - D).imag, (F - D).real)) % 360
BRG_FD = math.degrees(math.atan2((D - F).imag, (D - F).real)) % 360
BRG_FG = math.degrees(math.atan2((G - F).imag, (G - F).real)) % 360
z.angle_arc(G, 3.2, 90, BRG_GF, color=GREEN, arrow=False)
z.angle_arc(D, 3.2, BRG_DF, 270, color=RED, arrow=False)
z.angle_arc(F, 0.55, BRG_FG, BRG_FD + 360, color=BLUE, arrow=False)
z.point(G, 'concrete')
z.point(D, 'stone')
z.point(E, 'stone')
z.point(F, 'metal', size=9)
z.point(Fw, 'dot', color=GRAY)
ctri = centroid([G, D, F])
z.point_label(G, 'G', away=ctri)
z.point_label(D, 'D', away=ctri)
z.point_label(E, 'E', away=ctri)
z.edge_label(G, D, 'GD ＝ 19.27（Y座標の差）', F, color=GRAY, fs=15, dists=(16, 24, 32), ts=(0.3, 0.25, 0.7))
z.edge_label(G, F, 'GF ＝ 8.36', D + P(3, 0), color=RED, fs=16, dists=(16, 24))
z.edge_label(F, D, 'DF ＝ 11.04', G + P(3, 0), color=BLUE, fs=16, dists=(16, 24), ts=(0.5, 0.62, 0.38))
z.callout(G + P(0.1, 3.2), '∠G ＝ 7°37′35″\n（DFと向かい合う）', dirs=(100, 120, 80), color=GREEN, dists=(70, 95, 120))
z.callout(D + P(-0.15, -3.2), '∠D ＝ 5°46′21″\n（GFと向かい合う）', dirs=(80, 100, 60), color=RED, dists=(70, 95, 120))
z.callout(F + P(0.55, 0), '∠F ＝ 166°36′04″\n（GDと向かい合う）', dirs=(95, 110, 75), color=BLUE, dists=(90, 115, 140))
z.callout(F, 'F（138.08, 170.37）', dirs=(-100, -120, -80), color=RED, dists=(60, 80, 100))
z.callout(Fw, 'G点の角で計算した誤り\n（137.73, 173.02）', dirs=(-80, -60, -100), color=GRAY, dists=(90, 115, 140))
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu03_F_seigen.png')

# =====================================================================
# 図4：C点・E点を延長で求め、観測距離で裏付ける
# =====================================================================
fig, (ax,) = new_figure('図4　C点とE点を延長で求め、観測の距離で裏付ける',
                        'C＝A＋(B−A)÷Abs(B−A)×19.22（調査素図の注2：BはAC上、A～C 19.22）、E＝G＋(F−G)÷Abs(F−G)×12.58（調査素図の注2：FはEG上、E～G 12.58）。\n'
                        'C点・E点の観測は水平角が省略され、距離だけ（A102から2.50、A100から14.60）。求めた点で距離が合うことを確かめる。\n'
                        'CD＝12.65・DE＝7.00は調査素図の数値とも一致する。')
z = Zu(ax)
fit(ax, LOT + [A100, A102], margin=0.10, pad_aspect=True)
z.poly(LOT, color=GRAY, lw=1.1)
z.line(A, C, color=RED, lw=2.6)
z.line(G, E, color=RED, lw=2.6)
z.line(C, A102, color=BLUE, lw=1.8, ls='--')
z.line(E, A100, color=BLUE, lw=1.8, ls='--')
z.north_arrow()
marks(z, [(A, 'A'), (B, 'B'), (D, 'D'), (F, 'F'), (G, 'G')], cl)
z.point(C, 'concrete')
z.point(E, 'stone')
for p, n in [(A100, 'A100'), (A102, 'A102')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=cl)
z.edge_label(A, C, 'A～C ＝ 19.22', cl, color=RED, fs=16, dists=(16, 24), ts=(0.5, 0.4, 0.6))
z.edge_label(G, E, 'E～G ＝ 12.58', cl, color=RED, fs=16, dists=(16, 24), ts=(0.3, 0.4, 0.2))
z.edge_label(C, A102, '2.50', cl, color=BLUE, fs=16, dists=(14, 20, 26), rotate=False)
z.edge_label(E, A100, '14.60', cl, color=BLUE, fs=16, dists=(14, 20, 26), ts=(0.5, 0.6, 0.4))
z.edge_label(C, D, 'CD ＝ 12.65', cl, fs=15, dists=(16, 24))
z.edge_label(D, E, 'DE ＝ 7.00', cl, fs=15, dists=(16, 24))
z.callout(C, 'C（151.84, 181.30）', dirs=(-30, -50, -10), color=RED, dists=(70, 95, 120))
z.callout(E, 'E（137.52, 174.55）', dirs=(-60, -80, -40), color=RED, dists=(60, 80, 100))
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu04_C_E_uradzuke.png')

# =====================================================================
# 図5：問2 一筆に地目は一つ（登記記録と現況の比較）
# =====================================================================
fig, (ax1, ax2) = new_figure('図5　問2　一筆の土地に地目は一つ（一部地目変更・分筆）',
                             '左：登記記録では5番は一筆で雑種地255㎡。右：平成25年6月21日に建物が完成し、ブロック塀の西は建物の敷地（宅地）、東は資材置場（雑種地）。\n'
                             '一筆の土地の一部が別の地目になったので、西側部分を分筆してその部分の地目を宅地に変更する（土地一部地目変更・分筆登記）。\n'
                             '申請人は所有権の登記名義人の海川二郎（不動産登記法第37条第1項・第39条第1項）。借主の山川一郎は申請できない。',
                             ncols=2)
zs = []
for ax, head in [(ax1, '登記記録（5番　雑種地　255㎡）'), (ax2, '現況（ブロック塀で区画して利用）')]:
    z = Zu(ax, fontsize=14)
    fit(ax, LOT, margin=0.16, pad_aspect=True)
    ax.set_title(head, fontsize=18, weight='bold', pad=6)
    if ax is ax1:
        z.poly(LOT, fill=GRAY, alpha=0.25)
        z.free_text(centroid(LOT), '5番\n雑種地\n255㎡', fs=18)
    else:
        z.poly(RO, fill=ORANGE, alpha=0.25)
        z.poly(I_, fill=GREEN, alpha=0.25)
        z.line(B, F, color=RED, lw=5.0)
        z.free_text(centroid(RO), '宅地\n（建物の敷地）', fs=16, color=ORANGE)
        z.free_text(centroid(I_), '雑種地\n（資材置場）', fs=16, color=GREEN)
    z.north_arrow(length=0.07)
    for p, n in [(A, 'A'), (C, 'C'), (D, 'D'), (E, 'E'), (G, 'G')]:
        z.point(p, 'dot', size=6)
        z.point_label(p, n, away=centroid(LOT))
    if ax is ax2:
        for p, n in [(B, 'B'), (F, 'F')]:
            z.point(p, 'dot', size=6)
            z.point_label(p, n, away=centroid(LOT))
    zs.append(z)
zs[1].callout(B + (F - B) * 0.5, 'ブロック塀', dirs=(-100, -80, -120), color=RED, dists=(120, 140, 160))
ALL_PROBLEMS += save(fig, zs, 'H25_dai21mon_zu05_ippitsu_ichimoku.png')

# =====================================================================
# 図6：問3 分筆後の区画と地番・地目・地積
# =====================================================================
fig, (ax,) = new_figure('図6　問3　分筆後の区画と地番（5番 → （イ）5番1 ＋ （ロ）5番2）',
                        '（ロ）5番2（A・B・F・G）は座標法で113.9083 → 宅地なので小数第2位未満を切り捨てて113.90㎡。255−141.69730＝113.30 と引き算しない。\n'
                        '（イ）5番1（B・C・D・E・F）は調査素図の注4の141.69730と一致 → 雑種地なので1㎡未満を切り捨てて141㎡。\n'
                        '参考：全体の実測255.6056㎡と登記記録255㎡の差0.6056㎡、分筆後の合計254.90㎡との差0.10㎡（甲2の公差の約1.44㎡の範囲内）。')
z = Zu(ax)
fit(ax, LOT, margin=0.18, pad_aspect=True)
z.poly(RO, fill=ORANGE, alpha=0.25)
z.poly(I_, fill=GREEN, alpha=0.25)
z.line(B, F, color=RED, lw=3.0)
z.north_arrow()
z.free_text(centroid(RO), '（ロ）5番2\n宅地\n113.90㎡', fs=18)
z.free_text(centroid(I_), '（イ）5番1\n雑種地\n141㎡', fs=18)
marks(z, ALL7, cl)
z.free_text(centroid(RO) + P(-3.6, 0), '誤り：255 − 141.69730 ＝ 113.30\n（登記記録から引き算しない）', color=GRAY, fs=14,
            offsets=((0, 0), (0, -15), (0, 15)))
z.edge_label(A, C, '道路', cl, fs=15, color=GRAY, dists=(30, 40), rotate=False)
z.edge_label(G, A, '道路', cl, fs=15, color=GRAY, dists=(34, 44), rotate=False, ts=(0.7, 0.8, 0.6))
z.edge_label(C, D, '6', cl, fs=15, color=GRAY, dists=(30, 40), rotate=False)
z.edge_label(D, E, '3', cl, fs=15, color=GRAY, dists=(30, 40), rotate=False)
z.edge_label(F, G, '2', cl, fs=15, color=GRAY, dists=(30, 40), rotate=False)
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu06_bunpitsu_chiban.png')

# =====================================================================
# 図7：問4 地積測量図（5番1・5番2）の完成見本
# =====================================================================
fig, (ax,) = new_figure('図7　問4　地積測量図（5番1・5番2）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm（横約77mm・縦約57mm）。辺長は小数第3位を四捨五入（FG は 8.3639… なので 8.36）。\n'
                        '座標値・平面直角座標系の番号・地積と求積方法は書かない（注5）。基準点A100・A101・A102は位置と名称だけ（注6）。\n'
                        '測量年月日（平成25年8月19日）は注で省かれていないので書く。土地の所在「A市B町二丁目」・申請人「海川二郎」は欄に書く。')
z = Zu(ax)
fit(ax, LOT + [A100, A101, A102, P(133.0, 160.0)], margin=0.08, pad_aspect=True)
z.poly(LOT, lw=2.0)
z.line(B, F, lw=2.0)
z.north_arrow()
for n, (p, q, s) in SIDES.items():
    z.edge_label(p, q, s, cl, fs=16)
z.edge_label(B, F, '13.59', centroid(RO), fs=16, outward=False)
z.free_text(centroid(RO), '（ロ）\n5－2', fs=18)
z.free_text(centroid(I_), '（イ）\n5－1', fs=18)
marks(z, ALL7, cl)
for p, n in [(A100, 'A100'), (A101, 'A101'), (A102, 'A102')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=cl)
z.edge_label(A, C, '道　路', cl, fs=16, dists=(40, 50), rotate=False, ts=(0.5, 0.4, 0.6))
z.edge_label(G, A, '道路', cl, fs=16, dists=(50, 60), rotate=False, ts=(0.5, 0.6, 0.4))
z.edge_label(C, D, '6', cl, fs=16, dists=(40, 50), rotate=False)
z.edge_label(D, E, '3', cl, fs=16, dists=(40, 50), rotate=False)
z.edge_label(F, G, '2', cl, fs=16, dists=(40, 50), rotate=False)
z.free_text(P(133.2, 172.5), '（単位：ｍ）\n◎ コンクリート杭：A・C・G\n□ 石杭：D・E\n● 金属標：B・F\n△ 基準点：A100・A101・A102\n'
            '測量年月日：平成25年8月19日', fs=13, ha='left', va='bottom', offsets=((0, 0), (0, 30), (-40, 0), (0, 60)))
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu07_chiseki_sokuryouzu.png')

print('重なりの合計:', len(ALL_PROBLEMS))
