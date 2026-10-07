"""平成25年度 第21問（土地）会話形式note記事の解説図21枚を、座標値から作図する。

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
from zu_helpers import (Zu, new_figure, fit, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

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
# 真数表の別解（表の値で計算。複素数を使わない）
T_SIN8, T_COS8 = 0.14201, 0.98986          # 8°9′52″
T_SIN7, T_COS7 = 0.13271, 0.99115          # 7°37′35″
T_SIN5, T_SIN13 = 0.10057, 0.23172         # 5°46′21″、13°23′56″（＝180°−166°36′04″）
assert f'{0.18 / 16.24:.5f}' == '0.01108'                      # tan 0°38′6″（A101→A100の真南からのずれ）
dXB, dYB = 11.76 * T_SIN8, 11.76 * T_COS8
GF_T = 19.27 * T_SIN5 / T_SIN13
dXF, dYF = GF_T * T_SIN7, GF_T * T_COS7
assert (f'{dXB:.4f}', f'{dYB:.4f}') == ('1.6700', '11.6408') and str(dYB).startswith('11.6407')
assert str(GF_T).startswith('8.3634') and str(dXF).startswith('1.1099') and str(dYF).startswith('8.2894')
assert r2(P(153.30 - dXB, 159.78 + dYB)) == B and r2(P(139.19 - dXF, 162.08 + dYF)) == F
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


def fixed_figure(title):
    """整理図（文字の位置を固定して並べる図）の土台。"""
    setup_font()
    fig = plt.figure(figsize=(16, 12), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.08, 0.94, 0.83])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    return fig, ax


def box(ax, x, y, w, h, head, lines, col, fs_head=19, fs=15.5, fc='#f7f7f7', step=4.2, head_gap=5.0):
    """整理図の角丸の枠（左上に見出し、その下に本文の行）。座標は 0〜100 の固定配置。"""
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.5', fc=fc, ec=col, lw=2.2))
    ax.text(x + 1.5, y + h - 2.6, head, fontsize=fs_head, weight='bold', va='center', color=col)
    for i, (s, c) in enumerate(lines):
        ax.text(x + 2.5, y + h - 2.6 - head_gap - i * step, s, fontsize=fs, va='center', color=c)


def arrow(ax, x1, y1, x2, y2, col=BLACK, lw=2.2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='-|>', color=col, lw=lw, mutation_scale=22))


def side_panel(ax, blocks):
    """右側の説明パネル（図形の横に、計算と判断を上から並べる。固定配置）。blocks: [(見出し, [(行, 色)], 枠の色)]"""
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    y = 98
    for head, lines, col in blocks:
        h = 7.5 + 5.2 * len(lines)
        y -= h
        box(ax, 2, y, 96, h - 1.5, head, lines, col, fs_head=16, fs=14, step=5.2, head_gap=5.6)
        y -= 2.0


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
# 図2：注の仕分け（整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図2　注は2系統（問題文の注1〜8と、調査素図の注1〜5）')
LEFT = ('問題文の注', BLUE, [
    ('1', '本問の行為・書類は全て適法', '毎年の注'),
    ('2', '書面申請の方法で申請', '毎年の注'),
    ('3', '座標値は小数第3位を四捨五入', '毎年の注（問1）'),
    ('4', '地積測量図の辺長は小数第3位を四捨五入', '毎年の注（問4）'),
    ('5', '筆界点の座標値・系の番号・地積と\n求積方法は書かない（測量年月日は入っていない）', '毎年の注（問4）'),
    ('6', 'A市の基準点は位置と名称を書き、\n座標値は書かない', '今年の注（問4）'),
    ('7', '三角関数真数表の値を使う', '別解・検算のヒント'),
    ('8', '訂正・加入・削除のしかた', '毎年の注'),
])
RIGHT = ('調査素図の注', RED, [
    ('1', 'A100・A101・A102は許容誤差内', '確かめるだけ'),
    ('2', 'BはAとCを結ぶ直線上、\nFはEとGを結ぶ直線上', 'C点・E点（延長）'),
    ('3', '夾角 G・D・F ＝ 5°46′21″、\nD・F・G ＝ 166°36′04″', '問1　F点'),
    ('4', 'B・C・D・E・F・Bの面積は\n141.69730㎡', '（イ）の地積141と検算'),
    ('5', '距離の補正計算は行わない', '確かめるだけ'),
])
for x0, (head, col, items) in [(3, LEFT), (51, RIGHT)]:
    ax.add_patch(FancyBboxPatch((x0, 3), 46, 90, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=col, lw=2.2))
    ax.text(x0 + 2, 89, head, fontsize=21, weight='bold', color=col, va='center')
    yy = 83
    for num, body, tag in items:
        nl = body.count('\n') + 1
        ax.text(x0 + 2, yy, f'注{num}', fontsize=16, weight='bold', va='top', color=col)
        ax.text(x0 + 7.5, yy, body, fontsize=15, va='top', linespacing=1.35)
        ax.text(x0 + 44, yy - 3.3 * nl, tag, fontsize=13.5, va='top', ha='right', color=col)
        yy -= 3.4 * nl + 5.0
fig.text(0.5, 0.035, '番号がどちらにもあるので、記事では「問題文の注3」「調査素図の注3」のように書き分ける。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H25_dai21mon_zu02_chu_shiwake.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図2: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図3：C点は A→B の向きのまま 19.22m 延ばす（Yに足すだけの誤り C′ と比べる。右は拡大パネル）
# =====================================================================
U = (B - A) / abs(B - A)                        # A→B の向きの長さ1mの矢印（1mの物差し）
Cw = A + 19.22j                                 # Y座標だけに 19.22 を足した誤り C′
assert f'{abs(B - A):.4f}' == '9.3421' and str(U.real).startswith('0.0214') and str(U.imag).startswith('0.9997')
assert str((U * 19.22).real).startswith('0.4114') and str((U * 19.22).imag).startswith('19.2155')
assert str((A + U * 19.22).real).startswith('151.8414') and str((A + U * 19.22).imag).startswith('181.2955')
assert abs(Cw - P(151.43, 181.30)) < 1e-9 and f'{C.real - Cw.real:.2f}' == '0.41' and abs(C.imag - Cw.imag) < 1e-9
assert f'{19.22 / abs(B - A):.4f}' == '2.0573'
fig, (ax, ax2) = new_figure('図3　C点は、A→Bの向きのまま19.22m延ばす（Yに足すだけは誤り）',
                            '① B−A＝0.20＋9.34i（AからBへの矢印。長さ Abs(B−A)＝9.3421…）　'
                            '② (B−A)÷Abs(B−A)＝0.0214…＋0.9997…i（向きはA→Bのまま、長さ1mの物差し）\n'
                            '③ ×19.22 で 0.4114…＋19.2155…i（同じ向きの19.22mの矢印）　'
                            '④ 根元をAに置く：C＝A＋③＝151.8414…＋181.2955…i →（151.84, 181.30）\n'
                            'Yだけに19.22を足したC′（151.43, 181.30）は、1mごとに北へ0.0214…上がる分（19.22mで0.41）を落とした点。'
                            'Cより0.41m南（本件土地の内側）。',
                            ncols=2, width_ratios=[1.45, 1])
z = Zu(ax)
fit(ax, [A, B, C, D, G, A + P(2.0, 0)], margin=0.08, pad_aspect=True)
z.poly(LOT, color=GRAY, lw=1.1)
z.line(A, B, color=RED, lw=3.0)
z.line(B, C, color=RED, lw=2.0, ls='--')
z.line(A, Cw, color=GRAY, lw=1.6, ls=':')
z.line(A, A + U * 1.0, color=ORANGE, lw=5.0)
z.north_arrow()
marks(z, [(A, 'A'), (B, 'B'), (D, 'D'), (G, 'G')], cl)
z.point(C, 'concrete')
z.point(Cw, 'dot', color=GRAY)
z.callout(A + U * 0.5, '長さ1mの物差し\n(B−A)÷Abs(B−A)\n＝0.0214…＋0.9997…i', dirs=(-60, -45, -75), color=ORANGE,
          dists=(90, 115, 140))
z.callout(A + (B - A) * 0.55, 'B−A＝0.20＋9.34i\n（長さ 9.3421…）', dirs=(-70, -55, -85), color=RED, dists=(80, 105, 130))
z.edge_label(A, C, 'A～C ＝ 19.22（物差し×19.22）', cl, color=RED, fs=16, dists=(26, 36, 46), ts=(0.62, 0.7, 0.55),
             rotate=False)
z.point_label(C, 'C', away=cl)
z.callout(C, 'C（151.84, 181.30）', dirs=(115, 130, 100), color=RED, dists=(70, 95, 120))
z.callout(Cw, 'C′（151.43, 181.30）\nYに足すだけの誤り', dirs=(-120, -135, -105), color=GRAY, dists=(110, 140, 170))
z.free_text(A + (D - A) * 0.5, '本件土地', color=GRAY, fs=16)
# 右：C 点のまわりの拡大パネル（0.41m のずれ）
z2 = Zu(ax2)
fit(ax2, [C - U * 0.9, C + P(0.3, 0.3), Cw + P(-0.7, 0.3)], margin=0.08, pad_aspect=True)
z2.line(C - U * 0.9, C, color=RED, lw=3.0)
z2.line(Cw - 0.9j, Cw, color=GRAY, lw=1.6, ls=':')
z2.dim_line(Cw, C, color=BLUE)
z2.point(C, 'concrete')
z2.point(Cw, 'dot', color=GRAY)
z2.point_label(C, 'C', away=C + P(-1, 0))
z2.point_label(Cw, 'C′', away=Cw + P(1, 0), color=GRAY)
z2.edge_label(Cw, C, '0.41', C + P(0, -1), color=BLUE, fs=18, dists=(16, 24, 32), rotate=False)
z2.callout(C - U * 0.6, 'A→Bの向き（北へ少しずつ上がる）', dirs=(100, 120, 80), color=RED, dists=(60, 80, 100))
z2.callout(Cw - 0.6j, '真東（Yだけ足した線）', dirs=(-100, -120, -80), color=GRAY, dists=(60, 80, 100))
z2.free_text(C + P(0.3, -0.2), '道路（北）', color=GRAY, fs=15)
z2.free_text(Cw + P(-0.3, -0.45), '本件土地の内側', color=GRAY, fs=15)
ax2.set_title('C点のまわりの拡大', fontsize=17)
ALL_PROBLEMS += save(fig, [z, z2], 'H25_dai21mon_zu03_C_enchou.png')

# =====================================================================
# 図4：問1 B点（A101から放射）とC点の検算
# =====================================================================
fig, (ax,) = new_figure('図4　問1　B点の求め方（A101から放射）',
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
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu04_B_housha.png')

# =====================================================================
# 図5：問1 F点（三角形G・D・Fの正弦定理）
# =====================================================================
fig, (ax,) = new_figure('図5　問1　F点の求め方（三角形G・D・Fの正弦定理）',
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
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu05_F_seigen.png')

# =====================================================================
# 図6：問1 B点・F点の別解（三角関数真数表の値で計算する）
# =====================================================================
setup_font()
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図6　問1　B点・F点の別解（三角関数真数表の値で計算する）', fontsize=24, weight='bold', y=0.975)
fig.text(0.5, 0.025, '上：A101→A100は真南から東へ0°38′06″（tan＝0.18÷16.24＝0.01108）なので方向角179°21′54″。278°47′58″を足すと98°09′52″＝東から南へ8°09′52″。\n'
         'B＝（153.30 − 11.76×0.14201, 159.78 ＋ 11.76×0.98986）＝（151.6299…, 171.4207…）→（151.63, 171.42）\n'
         '下：sin166°36′04″＝sin13°23′56″＝0.23172 なので GF＝19.27×0.10057÷0.23172＝8.3634…。GDは真東なので、東から南へ7°37′35″。\n'
         'F＝（139.19 − 8.3634…×0.13271, 162.08 ＋ 8.3634…×0.99115）＝（138.0800…, 170.3694…）→（138.08, 170.37）',
         ha='center', va='bottom', fontsize=16)
fig.subplots_adjust(left=0.03, right=0.97, top=0.90, bottom=0.20, hspace=0.25)
zs = []
# 上：B点
z = Zu(ax1, fontsize=15)
QB = A101 + P(0, dYB)
fit(ax1, [A101, B, QB, A101 + P(2.2, 0), A101 + P(-2.4, -1.5), QB + P(0, 2.0)], margin=0.06, pad_aspect=True)
ax1.set_title('B点（A101から放射）', fontsize=18, weight='bold', pad=6)
z.line(A101, A101 + P(2.0, 0), color=GRAY, lw=1.2, ls='--')
z.free_text(A101 + P(2.0, 0), '北', color=GRAY, fs=14, offsets=((14, 0), (0, 14), (-14, 0)))
z.line(A101, QB, color=GRAY, lw=1.4, ls='--')
z.line(QB, B, color=BLUE, lw=2.4)
z.line(A101, B, color=RED, lw=2.8)
z.line(A101, A101 + (A100 - A101) / abs(A100 - A101) * 1.8, color=BLUE, lw=2.0)
z.angle_arc(A101, 4.0, 90, BRG_B - 360, color=RED)
z.point(A101, 'kijun')
z.point(B, 'metal', size=9)
z.point_label(A101, 'A101', away=A101 + P(-1, 3))
z.point_label(B, 'B', away=A101)
z.edge_label(A101, B, '11.76', QB, color=RED, fs=17, dists=(14, 20, 26), ts=(0.65, 0.75, 0.55))
z.edge_label(A101, QB, '東へ 11.6407…', B, color=GRAY, fs=16, dists=(14, 20, 26), ts=(0.6, 0.7, 0.5))
z.callout(QB + (B - QB) * 0.5, '南へ 1.6700…', dirs=(0, 20, -20), color=BLUE, dists=(60, 80, 100))
z.callout(A101 + P(4.0 * math.cos(math.radians(94)), 4.0 * math.sin(math.radians(94))), '8°09′52″（東から南へ）',
          dirs=(-60, -80, -40, -100), color=RED, dists=(60, 80, 100))
z.callout(A101 + (A100 - A101) / abs(A100 - A101) * 1.4, 'A100の方向（真南から東へ0°38′06″）', dirs=(-20, 0, -40, 20),
          color=BLUE, dists=(60, 80, 100))
zs.append(z)
# 下：F点
z = Zu(ax2, fontsize=15)
QF = G + P(0, dYF)
fit(ax2, [G, F, QF, D, G + P(1.6, 0), G + P(-1.8, 0)], margin=0.05, pad_aspect=True)
ax2.set_title('F点（Gから。三角形G・D・Fの正弦定理）', fontsize=18, weight='bold', pad=6)
z.line(G, D, color=GRAY, lw=1.4, ls=':')
z.line(G, QF, color=GRAY, lw=1.4, ls='--')
z.line(QF, F, color=BLUE, lw=2.4)
z.line(G, F, color=RED, lw=2.8)
z.line(F, D, color=GRAY, lw=1.2, ls='--')
z.angle_arc(G, 3.0, 90, 90 + 7 + 37 / 60 + 35 / 3600, color=RED)
z.point(G, 'concrete')
z.point(D, 'stone')
z.point(F, 'metal', size=9)
z.point_label(G, 'G', away=G + P(1, 3))
z.point_label(D, 'D', away=G)
z.point_label(F, 'F', away=G + P(2, 4))
z.edge_label(G, F, 'GF 8.3634…', QF, color=RED, fs=17, dists=(14, 20, 26), ts=(0.6, 0.7, 0.5))
z.edge_label(G, D, 'GD ＝ 19.27（真東）', F, color=GRAY, fs=15, dists=(14, 20, 26), ts=(0.75, 0.82, 0.68))
z.callout(G + (QF - G) * 0.55, '東へ 8.2894…', dirs=(70, 90, 50), color=GRAY, dists=(50, 70, 90))
z.callout(QF + (F - QF) * 0.5, '南へ 1.1099…', dirs=(10, 30, -10), color=BLUE, dists=(60, 80, 100))
z.callout(G + P(3.0 * math.cos(math.radians(93.8)), 3.0 * math.sin(math.radians(93.8))), '7°37′35″（東から南へ）',
          dirs=(-60, -80, -40, -100), color=RED, dists=(60, 80, 100))
zs.append(z)
ALL_PROBLEMS += save(fig, zs, 'H25_dai21mon_zu06_shinsuuhyou_betsukai.png')

# =====================================================================
# 図7：C点・E点を延長で求め、観測距離で裏付ける
# =====================================================================
fig, (ax,) = new_figure('図7　C点とE点を延長で求め、観測の距離で裏付ける',
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
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu07_C_E_uradzuke.png')

# =====================================================================
# 図8：問2 一筆に地目は一つ（登記記録と現況の比較）
# =====================================================================
fig, (ax1, ax2) = new_figure('図8　問2　一筆の土地に地目は一つ（一部地目変更・分筆）',
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
ALL_PROBLEMS += save(fig, zs, 'H25_dai21mon_zu08_ippitsu_ichimoku.png')

# =====================================================================
# 図9：問2 「わずかな差異」ではない（西側は区画された一部が別の地目）
# =====================================================================
PCT_RO, PCT_I = area(RO) / area(LOT) * 100, area(I_) / area(LOT) * 100
assert round(PCT_RO) == 45 and round(PCT_I) == 55
fig, (ax, axr) = new_figure('図9　問2　「部分的にわずかな差異」ではない（一部が別の地目になった）',
                            '不動産登記事務取扱手続準則第68条の「部分的にわずかな差異の存するときでも、土地全体としての状況を観察して定める」は、\n'
                            '一つの用途の土地の中のわずかな違いの話。本件は西側の約45%をブロック塀で区画し、建物の敷地として使っている。\n'
                            '一筆の土地の一部が別の地目になった場面なので、登記官が職権で分筆しなければならないほど（不動産登記法第39条第2項）。',
                            ncols=2, width_ratios=[1.25, 1])
z = Zu(ax)
fit(ax, LOT, margin=0.14, pad_aspect=True)
z.poly(RO, fill=ORANGE, alpha=0.25)
z.poly(I_, fill=GREEN, alpha=0.25)
z.line(B, F, color=RED, lw=5.0)
z.north_arrow()
z.free_text(centroid(RO), '西側\n建物の敷地\n113.9083㎡\n全体の約45%', fs=16)
z.free_text(centroid(I_), '東側\n資材置場\n141.6973㎡\n約55%', fs=16)
for p, n in ALL7:
    z.point(p, 'dot', size=6)
    z.point_label(p, n, away=cl)
z.callout(B + (F - B) * 0.25, 'ブロック塀で区画', dirs=(15, 30, 0), color=RED, dists=(60, 80, 100))
side_panel(axr, [
    ('わずかな差異（全体として観察）', [('一つの用途の土地の中の、', BLACK), ('ごく一部の違い', BLACK), ('→ 一筆に一つの地目のまま', GRAY)], GRAY),
    ('本件（一部が別の地目）', [('西側の約45%が建物の敷地（宅地）', BLACK), ('ブロック塀で区画して利用', BLACK),
                            ('→ 分筆して一部の地目を変更', RED), ('（法第39条第2項の場面）', RED)], RED),
])
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu09_wazuka_sai.png')

# =====================================================================
# 図10：問2 申請人は誰か（関係図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図10　問2　申請人は所有権の登記名義人の海川二郎')
box(ax, 26, 78, 48, 13, '本件土地　A市B町二丁目5番', [('雑種地　255㎡（甲区3番　所有権　海川二郎）', BLACK)], BLACK)
box(ax, 2, 38, 30, 30, '海川二郎', [('A市B町三丁目4番5号', BLACK), ('所有権の登記名義人', BLACK), ('（土地の所有者）', BLACK),
                                 ('→ 申請人になる', GREEN)], GREEN)
box(ax, 35, 38, 30, 30, '山川一郎', [('平成8年10月から借りている', BLACK), ('建物（家屋番号5番）の所有者', BLACK),
                                 ('今回の依頼者', BLACK), ('→ 申請人にならない', RED)], RED)
box(ax, 68, 38, 30, 30, '甲信用金庫', [('乙区5番　抵当権者', BLACK), ('（共同担保 目録（や）第7061号）', BLACK), ('',BLACK),
                                    ('→ 申請人にならない', RED)], RED)
for x in (17, 50, 83):
    arrow(ax, 50 + (x - 50) * 0.3, 77, x, 69.5, GRAY)
box(ax, 2, 5, 96, 25, '根拠', [
    ('不動産登記法第37条第1項：地目に変更があったときは、表題部所有者又は所有権の登記名義人が、', BLACK),
    ('　　変更があった日から1月以内に、地目に関する変更の登記を申請しなければならない', BLACK),
    ('不動産登記法第39条第1項：分筆の登記は、表題部所有者又は所有権の登記名義人以外の者は申請できない', BLACK),
], BLUE, step=5.0)
path = os.path.join(OUT, 'H25_dai21mon_zu10_shinseinin.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図10: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図11：問2 時系列と申請の期限（整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図11　問2　時系列と申請の期限（地目が変わったのは6月21日）')
import datetime as _dt  # noqa: E402
D0 = _dt.date(2013, 1, 1)
xd = lambda m, d: 22 + 72 * (_dt.date(2013, m, d) - D0).days / 243  # noqa: E731  平成25年1月1日〜9月1日を x＝22〜94 に
assert (_dt.date(2013, 7, 21) - _dt.date(2013, 6, 21)).days == 30
YL = 52
ax.plot([5, 15], [YL, YL], color=GRAY, lw=3)
ax.plot([15.6, 16.6], [YL - 2, YL + 2], color=GRAY, lw=2)
ax.plot([16.6, 17.6], [YL - 2, YL + 2], color=GRAY, lw=2)
ax.annotate('', xy=(97, YL), xytext=(18, YL), arrowprops=dict(arrowstyle='-|>', color=BLACK, lw=3, mutation_scale=24))
ax.add_patch(plt.Rectangle((xd(6, 21), YL - 3), xd(7, 21) - xd(6, 21), 6, color=ORANGE, alpha=0.30, lw=0))
ax.text((xd(6, 21) + xd(7, 21)) / 2, YL - 6.5, '1か月', fontsize=14, ha='center', va='center', color=ORANGE, weight='bold')
EV = [  # (x, 上下, ラベル, 色, 行の高さ)
    (8, -1, '平成8年10月\n山川一郎が借りる\n（資材置場）', GRAY, 24),
    (xd(1, 15), 1, '平成25年1月\n建物を建てることにした\n（地目はまだ雑種地）', GRAY, 22),
    (xd(6, 21), 1, '6月21日　建物の新築\n西側が建物の敷地（宅地）に\n＝ 地目が変わった日', RED, 34),
    (xd(7, 21), -1, '7月21日\n1か月の期限\n（法第37条第1項）', ORANGE, 30),
    (xd(8, 19), -1, '8月19日\n測量', BLUE, 18),
    (xd(8, 23), 1, '8月23日　申請\n期限は過ぎても義務は残る\n（法第164条第1項）', GREEN, 20),
]
for x, s, lab, col, dy in EV:
    ax.plot([x], [YL], 'o', ms=12, color=col, zorder=5)
    ax.plot([x, x], [YL + s * 2, YL + s * (dy - 1)], color=col, lw=1.4)
    ha = 'right' if x > 85 else ('left' if x < 12 else 'center')
    ax.text(x, YL + s * dy, lab, fontsize=15, ha=ha, va='bottom' if s > 0 else 'top', color=col, linespacing=1.3)
fig.text(0.5, 0.035, '地目の変更の日は、建物を建てることにした1月ではなく、建物ができて敷地になった6月21日（建物の登記記録の新築の日付）。\n'
         '1か月の期限（7月21日）を過ぎても申請の義務はなくならない。正当な理由なく怠ると10万円以下の過料。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H25_dai21mon_zu11_jikeiretsu_kigen.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図11: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図12：問3 （ロ）の面積（座標法・対角線。登記記録から引き算しない）
# =====================================================================
S_RO = sum(p * q.conjugate() for p, q in zip(RO, RO[1:] + RO[:1]))
S_DG = (A - F).conjugate() * (B - G)
assert f'{abs(S_RO.imag):.4f}' == '227.8166' and f'{S_DG.imag:.4f}' == '227.8166' and f'{S_DG.real:.4f}' == '88.6454'
assert f'{255 - 141.69730:.4f}' == '113.3027' and f'{area(RO) - (255 - 141.69730):.4f}' == '0.6056'
fig, (ax, axr) = new_figure('図12　問3　（ロ）5番2の面積は座標法で（登記記録から引き算しない）',
                            '問3のただし書き「地積は測量成果である座標値を用いて座標法により求積する」。（ロ）はA・B・F・Gの座標法で113.9083㎡。\n'
                            '255 − 141.69730 ＝ 113.3027 は、登記記録の255㎡と今回の実測255.6056㎡の差0.6056の分だけ小さくなる。\n'
                            '四角形は、対角線AF・BGを使った Conjg(A − F) × (B − G) のiの係数でも同じ227.8166が出る（検算）。',
                            ncols=2, width_ratios=[1.25, 1])
z = Zu(ax)
fit(ax, LOT, margin=0.14, pad_aspect=True)
z.poly(I_, color=GRAY, lw=1.1, fill=GRAY, alpha=0.10)
z.poly(RO, fill=ORANGE, alpha=0.28)
z.line(A, F, color=BLUE, lw=1.6, ls='--')
z.line(B, G, color=BLUE, lw=1.6, ls='--')
z.north_arrow()
z.free_text(centroid(RO), '（ロ）\n113.9083㎡', fs=17, offsets=((0, 70), (0, -70), (0, 85), (0, -85), (-60, 0)))
z.free_text(centroid(I_), '（イ）\n141.69730㎡\n（調査素図の注4）', fs=14, color=GRAY)
for p, txt, dirs in [(A, 'A（151.43, 162.08）', (80, 60, 100)), (B, 'B（151.63, 171.42）', (70, 90, 50)),
                     (F, 'F（138.08, 170.37）', (-80, -60, -100)), (G, 'G（139.19, 162.08）', (-80, -60, -100))]:
    z.point(p, 'dot', size=7)
    z.callout(p, txt, dirs=dirs, color=BLACK, dists=(45, 65, 85))
side_panel(axr, [
    ('座標法（A→B→F→G）', [('表示：195067.3732 − 227.8166i', BLACK), ('227.8166 ÷ 2 ＝ 113.9083', BLACK),
                         ('宅地 → 113.90㎡', ORANGE)], ORANGE),
    ('対角線で検算', [('Conjg(A − F) × (B − G)', BLACK), ('表示：88.6454 ＋ 227.8166i', BLACK), ('iの係数が同じ227.8166', BLUE)], BLUE),
    ('誤り：登記記録から引き算', [('255 − 141.69730 ＝ 113.3027', GRAY), ('→ 113.30（0.6056小さい）', RED)], RED),
])
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu12_ro_menseki.png')

# =====================================================================
# 図13：問3 （イ）の面積と地積の端数（地目で決まる）
# =====================================================================
S_I = sum(p * q.conjugate() for p, q in zip(I_, I_[1:] + I_[:1]))
assert f'{abs(S_I.imag):.4f}' == '283.3946'
fig, (ax, axr) = new_figure('図13　問3　（イ）5番1の面積と、地目で決まる地積の端数',
                            '（イ）はB・C・D・E・Fの座標法で141.6973㎡。調査素図の注4の141.69730と一致する（E点が合っていることの検算にもなる）。\n'
                            '地積の端数は地目で決まる（不動産登記規則第100条）。宅地は小数第2位未満、宅地・鉱泉地以外で10㎡を超える土地は1㎡未満を切り捨てる。\n'
                            '雑種地の（イ）は141（141.69ではない）、宅地の（ロ）は113.90。',
                            ncols=2, width_ratios=[1.25, 1])
z = Zu(ax)
fit(ax, LOT, margin=0.14, pad_aspect=True)
z.poly(RO, color=GRAY, lw=1.1, fill=GRAY, alpha=0.10)
z.poly(I_, fill=GREEN, alpha=0.28)
z.north_arrow()
z.free_text(centroid(I_), '（イ）5番1\n雑種地\n141.6973㎡', fs=17)
z.free_text(centroid(RO), '（ロ）5番2\n宅地\n113.9083㎡', fs=14, color=GRAY)
for p, n in [(B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F')]:
    z.point(p, 'dot', size=7)
    z.point_label(p, n, away=centroid(I_))
side_panel(axr, [
    ('座標法（B→C→D→E→F）', [('表示：257780.102 − 283.3946i', BLACK), ('283.3946 ÷ 2 ＝ 141.6973', BLACK),
                           ('＝ 調査素図の注4の141.69730', GREEN)], GREEN),
    ('雑種地（10㎡を超える）', [('1㎡未満を切り捨て', BLACK), ('141.6973 → 141', GREEN), ('141.69 と書くのは誤り', RED)], GREEN),
    ('宅地', [('小数第2位未満を切り捨て', BLACK), ('113.9083 → 113.90', ORANGE)], ORANGE),
])
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu13_i_menseki_hasuu.png')

# =====================================================================
# 図14：問3 地積更正が要るか（参考の判定。数直線）
# =====================================================================
KOU = (0.05 + 0.01 * 255 ** 0.25) * math.sqrt(255)
assert f'{KOU:.2f}' == '1.44' and str(KOU).startswith('1.4365')
fig, ax = fixed_figure('図14　問3　地積更正が要るか（参考の判定）')
xv = lambda v: 10 + (v - 253.0) * 20  # noqa: E731  253㎡〜257㎡を x＝10〜90 に
YN = 55
ax.annotate('', xy=(93, YN), xytext=(7, YN), arrowprops=dict(arrowstyle='-|>', color=BLACK, lw=2.4, mutation_scale=22))
for v in range(253, 258):
    ax.plot([xv(v), xv(v)], [YN - 1.2, YN + 1.2], color=BLACK, lw=1.4)
    ax.text(xv(v), YN - 3.2, f'{v}', fontsize=14, ha='center', va='top', color=GRAY)
ax.add_patch(plt.Rectangle((xv(255 - 1.44), YN - 2.5), xv(255 + 1.44) - xv(255 - 1.44), 5, color=BLUE, alpha=0.18, lw=0))
ax.text(xv(255 - 1.44), YN + 13, '253.56', fontsize=15, ha='center', color=BLUE)
ax.text(xv(255 + 1.44), YN + 13, '256.44', fontsize=15, ha='center', color=BLUE)
for v in (255 - 1.44, 255 + 1.44):
    ax.plot([xv(v), xv(v)], [YN - 2.5, YN + 11], color=BLUE, lw=1.2, ls='--')
ax.text(xv(255), YN + 27, '公差の範囲　255 ± 1.44（参考：市街地地域の甲2）', fontsize=17, ha='center', color=BLUE, weight='bold')
PTS = [(255, '登記記録\n255㎡', BLACK, 'o', 9), (255.6056, '全体の実測\n255.6056㎡\n（差 0.6056）', RED, 'v', 9),
       (254.90, '分筆後の合計\n113.90 ＋ 141 ＝ 254.90㎡\n（差 0.10）', GREEN, '^', -9)]
for v, lab, col, mk, dy in PTS:
    ax.plot([xv(v)], [YN], mk, ms=15, color=col, zorder=6)
    if v != 255:
        ax.plot([xv(v), xv(v) + (1.5 if v == 255.6056 else -1.5)], [YN + (2.5 if dy > 0 else -2.5),
                                                                  YN + dy + (1 if dy > 0 else -7)], color=col, lw=1.2)
    ax.text(xv(v) + (2 if v == 255.6056 else (-2 if v == 254.90 else 0)), YN + dy + (0 if dy > 0 else -6), lab,
            fontsize=15, ha='left' if v == 255.6056 else ('right' if v == 254.90 else 'center'),
            va='bottom' if dy > 0 else 'top', color=col, linespacing=1.3)
fig.text(0.5, 0.06, '問題文に公差の表も地域の区分もないので、あくまで参考。甲2の式 (0.05 ＋ 0.01 × Fの4乗根) × √F に F＝255 を入れると 1.4365…（約1.44㎡）。\n'
         'どちらの差も範囲内で、問題文も「1件の申請で行い」と言っているので、地積更正は入れない（不動産登記事務取扱手続準則第72条第1項）。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H25_dai21mon_zu14_kousa_sankou.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図14: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図15：問3 分筆後の区画と地番・地目・地積
# =====================================================================
fig, (ax,) = new_figure('図15　問3　分筆後の区画と地番（5番 → （イ）5番1 ＋ （ロ）5番2）',
                        '本番の5番を分筆するので、分筆前の地番に支号を付けて5番1・5番2にする（不動産登記事務取扱手続準則第67条第1項第4号）。\n'
                        '地目が変わらない東側（資材置場）を元の登記記録に残して（イ）5番1・雑種地141㎡、\n'
                        '宅地になった西側（建物の敷地）を新しい登記記録の（ロ）5番2・宅地113.90㎡にする。')
z = Zu(ax)
fit(ax, LOT, margin=0.18, pad_aspect=True)
z.poly(RO, fill=ORANGE, alpha=0.25)
z.poly(I_, fill=GREEN, alpha=0.25)
z.line(B, F, color=RED, lw=3.0)
z.north_arrow()
z.free_text(centroid(RO), '（ロ）5番2\n宅地\n113.90㎡', fs=18)
z.free_text(centroid(I_), '（イ）5番1\n雑種地\n141㎡', fs=18)
marks(z, ALL7, cl)
z.edge_label(A, C, '道路', cl, fs=15, color=GRAY, dists=(30, 40), rotate=False)
z.edge_label(G, A, '道路', cl, fs=15, color=GRAY, dists=(34, 44), rotate=False, ts=(0.7, 0.8, 0.6))
z.edge_label(C, D, '6', cl, fs=15, color=GRAY, dists=(30, 40), rotate=False)
z.edge_label(D, E, '3', cl, fs=15, color=GRAY, dists=(30, 40), rotate=False)
z.edge_label(F, G, '2', cl, fs=15, color=GRAY, dists=(30, 40), rotate=False)
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu15_bunpitsu_chiban.png')

# =====================================================================
# 図16：問3 登記記録の行き先（（イ）の原因は①③。整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図16　問3　5番の登記記録は（イ）5番1として続く（原因は①③）')
box(ax, 2, 47, 27, 34, '分筆前', [('5番の登記記録', BLACK), ('①地番　5番', BLACK), ('②地目　雑種地', BLACK), ('③地積　255', BLACK)], BLACK)
box(ax, 37, 52, 61, 40, '（イ）5番1　同じ登記記録が続く', [
    ('①地番　5番 → 5番1（変わる）', RED), ('②地目　雑種地のまま（変わらない → 書かない）', GRAY),
    ('③地積　255 → 141（変わる）', RED), ('原因：平成25年6月21日一部地目変更', BLACK),
    ('　　　①③5番1、5番2に分筆', RED)], GREEN, step=4.8)
box(ax, 37, 18, 61, 28, '（ロ）5番2　新しい登記記録', [
    ('①地番　5番2　②地目　宅地　③地積　113.90', BLACK), ('原因：5番から分筆（元の地番）', BLACK),
    ('分筆で生まれた時から宅地', ORANGE)], ORANGE, step=4.8)
arrow(ax, 30, 70, 36, 74, GREEN)
arrow(ax, 30, 58, 36, 36, ORANGE)
box(ax, 2, 2, 96, 12, '比べる場合', [('支号のある土地（例：10番1）を分筆して10番1が残るときは、地番が変わらないので③だけ', GRAY)],
    GRAY, step=4.6)
fig.text(0.5, 0.045, '本番の5番を分筆すると、分筆前の地番に支号を付けるので元の土地も5番1に変わる（不動産登記事務取扱手続準則第67条第1項第4号）。\n'
         '変わった欄の番号を冠記する（同準則第73条）ので、（イ）の原因は「①③」。（イ）の行は変わる事項だけを書き、地目の欄は空欄にする。',
         ha='center', va='center', fontsize=15.5)
path = os.path.join(OUT, 'H25_dai21mon_zu16_touki_kiroku_yukisaki.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図16: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図17：問3 登録免許税（分筆後の土地の個数で数える）
# =====================================================================
fig, (ax, axr) = new_figure('図17　問3　登録免許税は分筆後の土地の個数 × 1,000円',
                            '登録免許税法別表第一の一の（十三）イ：分筆による登記事項の変更の登記は、分筆後の不動産の個数1個につき1,000円。\n'
                            '元の地番の5番1も分筆後の土地の1つなので、5番1と5番2の2個で金2,000円。新しくできた5番2だけ数えた1,000円は誤り。\n'
                            '一部地目変更（表示の変更）には登録免許税はかからない。',
                            ncols=2, width_ratios=[1.25, 1])
z = Zu(ax)
fit(ax, LOT, margin=0.14, pad_aspect=True)
z.poly(RO, fill=ORANGE, alpha=0.25)
z.poly(I_, fill=GREEN, alpha=0.25)
z.line(B, F, color=RED, lw=3.0)
z.north_arrow()
z.free_text(centroid(RO), '（ロ）5番2\n1個', fs=20)
z.free_text(centroid(I_), '（イ）5番1\n1個', fs=20)
side_panel(axr, [
    ('正しい数え方', [('5番1（1個）＋ 5番2（1個）＝ 2個', BLACK), ('2個 × 1,000円 ＝ 金2,000円', GREEN)], GREEN),
    ('誤り', [('新しくできた5番2だけ数える', BLACK), ('→ 金1,000円', RED)], RED),
    ('一部地目変更', [('登録免許税はかからない', GRAY)], GRAY),
])
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu17_tourokumenkyozei.png')

# =====================================================================
# 図18：問3 抵当権は分筆後の両方に残る（承諾を証する情報は要らない。整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図18　問3　抵当権は5番1・5番2の両方に残る（承諾書は添付しない）')
box(ax, 2, 50, 30, 38, '分筆前　5番', [('甲区3番　所有権', BLACK), ('　海川二郎', BLACK), ('乙区5番　抵当権', BLACK),
                                    ('　甲信用金庫', BLACK), ('　共同担保 目録（や）第7061号', BLACK)], BLACK, step=5.2)
box(ax, 40, 70, 58, 20, '分筆後　（イ）5番1', [('乙区5番の抵当権（甲信用金庫）はそのまま', BLACK)], GREEN)
box(ax, 40, 44, 58, 20, '分筆後　（ロ）5番2', [('抵当権が転写され、共同担保目録（や）第7061号に記録される', BLACK)], ORANGE)
arrow(ax, 33, 74, 39, 80, GREEN)
arrow(ax, 33, 64, 39, 54, ORANGE)
box(ax, 2, 5, 96, 33, '添付情報', [
    ('分筆の登記：分筆後の土地の地積測量図（不動産登記令別表8の項）', BLACK),
    ('承諾を証する情報が要るのは、分筆後の一方の土地で抵当権を消滅させるとき（不動産登記法第40条）', BLACK),
    ('本件はそのような話がないので、甲信用金庫の承諾書は添付しない', RED),
    ('問題文の「利害関係人から、申請すべき登記をすることの承諾が得られた」につられない', GRAY),
], BLUE, step=5.6)
fig.text(0.5, 0.04, '転写と共同担保目録への記録は、登記官が行う（不動産登記規則第102条第1項・第2項）。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H25_dai21mon_zu18_teitouken.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図18: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図19：問4 地積測量図に書くもの・書かないもの（不動産登記規則第77条第1項。整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図19　問4　地積測量図に書くもの・書かないもの（不動産登記規則第77条第1項）')
ROWS77 = [
    ('第1号', '地番区域の名称', '書く', '土地の所在の欄に「A市B町二丁目」'),
    ('第2号', '方位', '書く', ''),
    ('第3号', '縮尺', '書く', '1/250（答案用紙に印刷済み）'),
    ('第4号', '地番（隣接地の地番を含む）', '書く', '（イ）5－1・（ロ）5－2、隣接地2・3・6（地番の欄は（略））'),
    ('第5号', '地積及びその求積方法', '書かない', '問題文の注5'),
    ('第6号', '筆界点間の距離', '書く', '辺長8本（AB 9.34 … BF 13.59）'),
    ('第7号', '平面直角座標系の番号又は記号', '書かない', '問題文の注5'),
    ('第8号', '筆界点の座標値', '書かない', '問題文の注5'),
    ('第9号', '境界標', '書く', 'コンクリート杭・石杭・金属標'),
    ('第10号', '測量の年月日', '書く', '平成25年8月19日（問題文の注5に入っていない）'),
]
y = 90
for no, item, yn, note in ROWS77:
    col = GREEN if yn == '書く' else RED
    ax.add_patch(FancyBboxPatch((2, y - 3.2), 96, 6.4, boxstyle='round,pad=0.3',
                                fc='#eef7ef' if yn == '書く' else '#fbeeee', ec=col, lw=1.2))
    ax.text(4, y, no, fontsize=15, va='center', weight='bold')
    ax.text(13, y, item, fontsize=15, va='center')
    ax.text(47, y, yn, fontsize=15, va='center', color=col, weight='bold')
    ax.text(57, y, note, fontsize=13.5, va='center', color=BLACK if yn == '書く' else GRAY)
    y -= 8.0
fig.text(0.5, 0.035, '問題文の注5で省くのは第5号・第7号・第8号だけ。第10号の測量の年月日は書く。\n'
         '基準点A100・A101・A102は位置と名称を書き、座標値は書かない（問題文の注6）。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H25_dai21mon_zu19_chiseki_kisaijikou.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図19: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図20：問4 地積測量図（5番1・5番2）の完成見本
# =====================================================================
fig, (ax,) = new_figure('図20　問4　地積測量図（5番1・5番2）の完成見本',
                        '縮尺1/250で1m＝4mm。本件土地は横約77mm・縦約57mm、基準点まで入れて横約92mm・縦約67mm（第4欄の枠は横約29cm・縦約21cm）。\n'
                        '辺長は小数第3位を四捨五入（FG は 8.3639… なので 8.36）。座標値・平面直角座標系の番号・地積と求積方法は書かない（問題文の注5）。\n'
                        '基準点A100・A101・A102は位置と名称だけ（問題文の注6）。測量年月日（平成25年8月19日）は注で省かれていないので書く。\n'
                        '土地の所在「A市B町二丁目」・申請人「海川二郎」は欄に書く。')
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
ALL_PROBLEMS += save(fig, [z], 'H25_dai21mon_zu20_chiseki_sokuryouzu.png')


# =====================================================================
# 図21：本番で解く順番（整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図21　本番で解く順番（F点と地積測量図がいちばん時間を食う）')
STEPS = [
    ('①', '問を先に読み、注を仕分ける', ['問3のただし書き「1件の申請」「座標法で求積」と、調査素図の注4の141.69730に印を付ける'], GRAY),
    ('②', '問2（第2欄）　計算なし', ['一筆に地目は一つ → 一部が宅地 → 分筆して地目変更、申請人は所有者の海川二郎'], GREEN),
    ('③', '問3の申請書のうち（ロ）の地積以外', ['目的・添付書類・申請人・登録免許税2,000円・所在・1行目・（イ）の141（調査素図の注4から）・原因'], BLUE),
    ('④', 'B点（A101から放射）', ['時計回りに足す。C点を延長で出してA102から2.50で検算'], ORANGE),
    ('⑤', 'F点（三角形G・D・Fの正弦定理）', ['GFに向かい合うのはD点の角。G→Dから時計回り。DF 11.04で検算'], RED),
    ('⑥', '（ロ）の地積 113.90', ['A・B・F・Gの座標法（対角線でも検算）。宅地は小数第2位未満を切り捨て'], PURPLE),
    ('⑦', 'E点・辺長8本・地積測量図（問4）', ['基準点まで入れて横約92mm・縦約67mm。第4欄の枠（横約29cm・縦約21cm）に十分入る'], BLACK),
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
fig.text(0.5, 0.035, '①〜③は座標がなくても書ける。F点で詰まっても、第2欄と申請書の大部分は点になる。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H25_dai21mon_zu21_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図21: 整理図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
