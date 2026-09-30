"""平成24年度 第21問（土地）会話形式note記事の解説図11枚を、座標値から作図する。

`../prompt_H24_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../H26/Q21/zu/draw_H26_dai21mon_kaisetsuzu.py`。

座標は世界測地系のマイナスの値（X −8000台、Y −2500台）だが、作図は座標どおり（横＝Y〈東〉、縦＝X〈北〉）に描く。
帯（ア・イ）は幅が1m前後で細いので、点を求める図は拡大パネルを使う。

実行: python3 note-articles-Kijyutsu/H24/Q21/zu/draw_H24_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, dms, to_dms, area, chiseki, fmt_num, disp  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の別紙4・別紙5の座標値と、記事で求めた点） ----------------------
A, B, C = P(-8030.50, -2530.30), P(-8041.69, -2518.63), P(-8034.17, -2510.92)
D, E, F = P(-8025.02, -2504.71), P(-8019.28, -2510.26), P(-8015.81, -2516.60)
G, H = P(-8031.92, -2528.82), P(-8024.15, -2521.37)
R1, R2, R3 = P(-8048.02, -2512.03), P(-8051.27, -2515.15), P(-8034.03, -2533.13)
R4, R5 = P(-8023.92, -2540.21), P(-8027.67, -2542.70)
K611, K612 = P(-8044.07, -2519.78), P(-8031.34, -2532.58)
I, J = P(-8032.59, -2528.12), P(-8024.82, -2520.67)               # 別紙5（法務太郎が算出済み）
KX = J + (J - I) / abs(J - I) * 0.65                                 # 問1 K（Jから延長線上へ0.65m）
K = r2(KX)
KW = r2(J - (J - I) / abs(J - I) * 0.65)                             # 誤り：JからIの向きへ0.65m
S_I = abs(((J - G).conjugate() * (I - H)).imag) / 2                  # 分割地イ 10.4305
TGT = 10.4305 * 1.087                                                # 分割地アの面積 11.3379535
S_KJC = abs(((J - K).conjugate() * (C - K)).imag) / 2                # 4.395
S_KCD = abs(((C - K).conjugate() * (D - K)).imag) / 2                # 73.0386
T = (TGT - 4.395) / 73.0386
LX = C + (D - C) * T
L = r2(LX)
LE = r2(C + (D - C) * (10.4305 - 4.395) / 73.0386)                   # 誤り：アとイを同じ面積にしたL
S_A = abs(((L - J).conjugate() * (K - C)).imag) / 2                  # 丸めたLで 11.3374
H_ = 2 * 6.9429535 / abs(C - K)                                      # 別解：KCからの高さ 1.0266…
M = C + H_ * cmath.rect(1, dms(46, 33, 28))                          # 別解の補助点M
S52 = abs(((C - I).conjugate() * (J - B)).imag) / 2                  # 5番2（イを分筆した後） 143.4704
S52_0 = abs(((C - G).conjugate() * (H - B)).imag) / 2                # 5番2（平成23年の分筆のとき） 153.9005
S_MRG = area([I, B, C, L, K])                                        # 誤り：合筆後を5点で回す 154.8103

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
assert K == P(-8024.35, -2520.22) and KW == P(-8025.29, -2521.12)
assert fmt_num(KX.real) == '−8024.3508…' and fmt_num(KX.imag) == '−2520.2201…'
assert to_dms(cmath.phase(J - I)) == '43°47′43.93″' and to_dms(cmath.phase(C - H)) == '133°47′47.77″'
assert f'{S_I:.4f}' == '10.4305' and f'{TGT:.7f}' == '11.3379535'
assert f'{S_KJC:.3f}' == '4.395' and f'{S_KCD:.4f}' == '73.0386'
assert L == P(-8033.30, -2510.33) and LE == P(-8033.41, -2510.41)
assert fmt_num(T, 4) == '0.0950…'
assert f'{S_A:.4f}' == '11.3374' and chiseki(S_A) == 11.33
assert fmt_num(abs(C - K)) == '13.5248…' and fmt_num(H_) == '1.0266…'
assert to_dms(cmath.phase(C - K)) == '136°33′28.33″'
assert r2(M) == P(-8033.46, -2510.17)
assert f'{S52:.4f}' == '143.4704' and chiseki(S52) == 143.47
assert f'{S52_0:.4f}' == '153.9005' and chiseki(S52_0) == 153.90
assert f'{S52 + S_A:.4f}' == '154.8078' and chiseki(S52 + S_A) == 154.80
assert f'{S_MRG:.4f}' == '154.8103' and chiseki(S_MRG) == 154.81
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'AG': (A, G, '2.05'), 'GH': (G, H, '10.76'), 'HJ': (H, J, '0.97'), 'JK': (J, K, '0.65'),
         'KL': (K, L, '13.34'), 'LD': (L, D, '10.01'), 'DE': (D, E, '7.98'), 'EF': (E, F, '7.23'),
         'FA': (F, A, '20.09'), 'JC': (J, C, '13.51'), 'CL': (C, L, '1.05')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert round(abs(K612 - A), 2) == 2.43 and round(abs(K611 - C), 2) == 13.29
print('数値の照合: すべて一致')


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


ALL_PROBLEMS = []
N51 = [A, G, H, J, C, D, E, F]            # 5番1（分筆前。JはHC上の点）
N52 = [G, B, C, J, H]                     # 5番2（平成23年の分筆のとき）
AA = [J, C, L, K]                         # 分割地ア（5番3）
II = [G, H, J, I]                         # 分割地イ（5番4）
KIND = {'A': 'metal', 'F': 'metal', 'B': 'metal', 'C': 'concrete', 'D': 'concrete', 'E': 'concrete',
        'G': 'concrete', 'H': 'concrete', 'I': 'concrete', 'J': 'concrete', 'K': 'concrete', 'L': 'concrete'}
PTS = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 'K': K, 'L': L}
CT = centroid([A, B, C, D, E, F])

# =====================================================================
# 図1：全体図
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体図',
                        '5番1（山川一郎）と5番2（海川二郎）の筆界は G→H→C の折れ線。交換する分割地ア（5番3予定）とイ（5番4予定）で、\n'
                        '新しい筆界を I→K→L の線にする。I・Jは法務太郎が算出済み（別紙5）。問1で K・L を求める。\n'
                        '基準点は申請地に最も近い 4-611・4-612 だけを描いた（地積測量図に書く2点）。')
z = Zu(ax)
fit(ax, [A, B, C, D, E, F + P(3.5, 0), K611, K612, R1, R4, R3, R2], margin=0.05, pad_aspect=True)
z.poly(N51, fill=BLUE, alpha=0.10)
z.poly(N52, fill=GREEN, alpha=0.12)
z.poly(AA, color=RED, lw=1.6, fill=RED, alpha=0.30)
z.poly(II, color=PURPLE, lw=1.6, fill=PURPLE, alpha=0.30)
z.poly([I, K, L], color=RED, lw=2.2, ls='--', closed=False)
z.poly([R4, A, G, I, B, R1], color=GRAY, lw=1.4, closed=False)
z.poly([R5, R3, R2], color=GRAY, lw=1.4, closed=False)
z.line(F, F + (F - E) / abs(F - E) * 2.0, lw=1.2)
z.line(F, F + (F - A) / abs(F - A) * 2.0, lw=1.2)
z.north_arrow()
z.free_text(CT + P(6.5, 1.5), '5番1\n山川一郎', fs=17)
z.free_text(centroid([I, B, C, J]), '5番2\n海川二郎', fs=17)
for n, p in PTS.items():
    z.point(p, KIND[n], size=6 if KIND[n] == 'concrete' else 8)
    z.point_label(p, n, away=CT if n not in ('K', 'J', 'H', 'I', 'G') else p + P(-1, 1), fs=14)
z.callout(K + (L - K) * 0.55, 'ア（5番3予定）', dirs=(70, 90, 50), color=RED, dists=(70, 95, 120))
z.callout(G + (H - G) * 0.55 + (I - G) * 0.5, 'イ（5番4予定）', dirs=(150, 165, 135, 120), color=PURPLE, dists=(90, 120, 150))
for p, n in [(K611, '4-611'), (K612, '4-612')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=CT, fs=14)
z.free_text(A + (F - A) * 0.6 + P(1.0, -4.5), '4－2', fs=15, color=GRAY, offsets=((0, 0), (-10, 0), (0, -15)))
z.free_text(F + P(2.6, -0.3), '9', fs=15, color=GRAY, offsets=((0, 0), (-12, 8), (10, 10)))
z.free_text(E + P(2.8, 1.5), '8', fs=15, color=GRAY, offsets=((0, 0), (10, 0), (0, 10)))
z.free_text(C + P(3.0, 3.5), '6', fs=15, color=GRAY, offsets=((0, 0), (12, 0), (0, 12)))
z.free_text(R3 + (R2 - R3) * 0.45, '道路', fs=15, color=GRAY, offsets=((0, 22), (0, 30), (-20, 22)))
for p, n in [(R1, 'R1'), (R2, 'R2'), (R3, 'R3'), (R4, 'R4'), (R5, 'R5')]:
    z.point(p, 'metal', size=5, color=GRAY)
    z.point_label(p, n, away=CT, fs=12, color=GRAY, weight='normal')
ALL_PROBLEMS += save(fig, [z], 'H24_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：覚書の登記の順序と地番（整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図2　覚書3の登記の順序（分筆 → 交換 → 合筆）')
STEPS = [
    ('①', '5番1の分筆（覚書3⑴・甲）', '分割地アを分けて5番3に。申請人は山川一郎。問2の地積測量図はこの申請（5番2の分筆より先）', BLUE),
    ('②', '5番2の分筆（覚書3⑴・乙）', '分割地イを分けて5番4に。申請人は海川二郎', GREEN),
    ('③', '交換による所有権の移転（覚書3⑵）', '5番4（イ）は山川一郎へ、5番3（ア）は海川二郎へ。持ち主がそろわないと合筆できない（法第41条第3号）', ORANGE),
    ('④', '5番1と5番4の合筆（覚書3⑶・甲）', '申請人は山川一郎', GRAY),
    ('⑤', '5番2と5番3の合筆（覚書3⑶・乙）', '申請人は海川二郎。問3の登記申請書はこの申請', RED),
]
y = 95
for num, head, line, col in STEPS:
    h = 15.2
    y -= h
    ax.add_patch(FancyBboxPatch((3, y), 94, h - 2.2, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=col, lw=2.2))
    ax.text(5, y + h - 6.0, f'{num}　{head}', fontsize=20, weight='bold', va='center', color=col)
    ax.text(8, y + h - 11.2, line, fontsize=15.5, va='center')
fig.text(0.5, 0.035, '問2（地積測量図）は①、問3（登記申請書）は⑤。①の時点では5番2はまだ分筆していないので、G・H・Jの南の隣接地は「5－2」。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H24_dai21mon_zu02_touki_junjo.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図2: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図3：注の仕分け（整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図3　注は2系統（問題文の注1〜5と、別紙図面の注1〜7）')
LEFT = [('問題文の注', BLUE, [
    ('1', '座標は小数第3位を四捨五入', '毎年の注'),
    ('2', '訂正・加入・削除の押印不要', '毎年の注'),
    ('3', '辺長は小数第3位を四捨五入。基準点は\n最も近い2点。座標値・系・測量年月日・\n地積と求積方法は省略してよい', '今年の注（問2）'),
    ('4', '書面を提出する方法で申請', '毎年の注'),
    ('5', '三角関数真数表', 'L点の別解のヒント'),
])]
RIGHT = [('別紙図面の注', RED, [
    ('1', '地図に準ずる図面に山川一郎が記入', ''),
    ('2', 'I点：AB上、Aから3.02m', '別紙5に座標あり'),
    ('3', 'J点：HC上の点', '別紙5に座標あり'),
    ('4', 'K点：JIの延長線上、Jから0.65m', '問1'),
    ('5', 'KIとHCは直角に交わる', '検算'),
    ('6', 'L点：CD上。アの面積＝イの面積×1.087\n（面積は小数第4位までで比べる）', '問1'),
    ('7', 'A〜Hは既存の地積測量図と符合', '筆界は動いていない'),
])]
for x0, groups in [(3, LEFT), (51, RIGHT)]:
    for head, col, items in groups:
        ax.add_patch(FancyBboxPatch((x0, 3), 46, 90, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=col, lw=2.2))
        ax.text(x0 + 2, 89, head, fontsize=21, weight='bold', color=col, va='center')
        yy = 82
        for num, body, tag in items:
            nl = body.count('\n') + 1
            ax.text(x0 + 2, yy, f'注{num}', fontsize=16, weight='bold', va='top', color=col)
            ax.text(x0 + 7.5, yy, body, fontsize=15, va='top', linespacing=1.35)
            if tag:
                ax.text(x0 + 44, yy - 3.3 * nl, tag, fontsize=13.5, va='top', ha='right', color=col)
            yy -= 3.4 * nl + 5.4
fig.text(0.5, 0.035, '記事では「問題文の注3」「別紙図面の注6」のように、どちらの注かを書き分ける。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H24_dai21mon_zu03_chu_shiwake.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図3: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図4：問1 K点（JIの延長線上、Jから0.65m）
# =====================================================================
fig, (ax1, ax2) = new_figure('図4　問1　K点はJから「延長線上」へ0.65m',
                             'K ＝ J ＋ (J − I) ÷ Abs(J − I) × 0.65。IからJへ向かう向き（方向角43°47′43.93″、真数表の43°47′44″）のまま、\n'
                             'Jを越えて0.65m進むと K（−8024.35, −2520.22）。Jから I の向きへ戻ると（−8025.29, −2521.12）で、HCの線より南西の\n'
                             'IJの線の上（5番2の側）に戻ってしまう。KIとHCが直角（別紙図面の注5）なのは、Conjg(C − H) × (J − I) の実部がほぼ0で確かめる。',
                             ncols=2, width_ratios=[0.8, 1.2])
za = Zu(ax1, fontsize=14)
fit(ax1, [A, G, H, C, B, I, J, K, L, D, E, F], margin=0.08, pad_aspect=True)
za.poly(N51, color=GRAY, lw=1.1)
za.poly([G, B, C], color=GRAY, lw=1.1, closed=False)
za.poly(II, color=PURPLE, lw=1.2, fill=PURPLE, alpha=0.25)
za.line(I, K, color=RED, lw=2.0)
za.north_arrow(length=0.07)
for n in ('I', 'J', 'H', 'C'):
    za.point(PTS[n], KIND[n], size=5)
za.point(K, 'dot', color=RED, size=8)
za.callout(J, '拡大の範囲', dirs=(120, 140, 100), color=GRAY, dists=(60, 80))
za.free_text(CT + P(6, 2), '5番1', fs=15, color=GRAY)
za.free_text(centroid([I, B, C, J]), '5番2', fs=15, color=GRAY)
ax1.set_title('全体', fontsize=17, weight='bold', pad=6)

zb = Zu(ax2, fontsize=15)
fit(ax2, [J + P(-1.4, -1.6), J + P(1.1, 2.4)], margin=0.0, pad_aspect=True)
zb.poly(II, color=PURPLE, lw=0.0, fill=PURPLE, alpha=0.18, check=False)
zb.line(H, H + (C - H) * 0.16, color=BLACK, lw=2.0)
zb.line(G + (H - G) * 0.82, H, color=BLACK, lw=2.0)
zb.line(J + (I - J) / abs(I - J) * 1.5, K, color=GRAY, lw=1.6, ls='--')
zb.line(J, K, color=RED, lw=3.0)
zb.north_arrow(length=0.08)
zb.point(H, 'concrete')
zb.point_label(H, 'H', away=H + P(-1, 1))
zb.point(J, 'concrete')
zb.point_label(J, 'J', away=J + P(-1, 1.5))
zb.point(K, 'dot', color=RED, size=10)
zb.point_label(K, 'K', away=K + P(-1, -1), color=RED)
zb.point(KW, 'dot', color=GRAY, size=9)
zb.edge_label(J, K, '0.65', J + P(1, -2), color=RED, fs=16)
zb.callout(K, 'K（−8024.35, −2520.22）', dirs=(60, 40, 80, 20), color=RED, dists=(70, 95, 120))
zb.callout(KW, '誤り：Iの向きへ0.65m\n（−8025.29, −2521.12）', dirs=(-60, -40, -80, -20), color=GRAY, dists=(60, 85, 110))
zb.callout(J + (I - J) / abs(I - J) * 1.3, 'Iへ（10.76m先）', dirs=(-100, -120, -80, -140), color=GRAY, dists=(30, 45, 60))
zb.callout(H + (C - H) * 0.12, 'Cへ（HC）', dirs=(30, 50, 10), color=BLACK, dists=(50, 70, 90))
zb.free_text(J + P(-0.75, -1.0), '分割地イ', fs=14, color=PURPLE, rotation=44, offsets=((0, 0), (-8, -8), (8, 8)))
ax2.set_title('Jのまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H24_dai21mon_zu04_K_encho.png')

# =====================================================================
# 図5：問1の準備 分割地イの面積と1.087倍
# =====================================================================
fig, (ax,) = new_figure('図5　分割地イの面積と、アの面積（1.087倍）',
                        'イ（G→H→J→I）は四角形なので、対角線どうしの式 Conjg(J − G) × (I − H) で倍面積 20.861、面積は 10.4305㎡。\n'
                        'アの面積は、別紙図面の注6のとおり 10.4305 × 1.087 ＝ 11.3379535㎡（交換でも同じ面積ではない）。\n'
                        '面積の比較は小数第4位まで（10.4305）の値で行う。')
z = Zu(ax, fontsize=15)
fit(ax, [G, H, J, I, G + P(-0.8, -1.8), J + P(0.8, 1.8)], margin=0.02, pad_aspect=True)
z.poly(II, color=PURPLE, lw=2.2, fill=PURPLE, alpha=0.22)
z.line(G, J, color=BLUE, lw=1.6, ls='--')
z.line(H, I, color=ORANGE, lw=1.6, ls='--')
z.north_arrow(length=0.08)
ci = centroid(II)
for n in ('G', 'H', 'J', 'I'):
    z.point(PTS[n], KIND[n])
    z.point_label(PTS[n], n, away=ci)
z.edge_label(G, H, '10.76', ci, fs=15)
z.edge_label(I, J, '10.76', ci, fs=15)
z.callout(G + (J - G) * 0.3, '対角線 G→J', dirs=(160, 180, 140), color=BLUE, dists=(60, 85))
z.callout(H + (I - H) * 0.7, '対角線 H→I', dirs=(-20, 0, -40), color=ORANGE, dists=(60, 85))
z.callout(ci, 'イ　10.4305㎡\n→ ア ＝ 10.4305 × 1.087\n　　 ＝ 11.3379535㎡', dirs=(-30, -10, -50, 20), color=PURPLE,
          dists=(120, 150, 180))
ALL_PROBLEMS += save(fig, [z], 'H24_dai21mon_zu05_I_menseki.png')

# =====================================================================
# 図6：問1 L点（三角形の比例）
# =====================================================================
fig, (ax1, ax2) = new_figure('図6　問1　L点は △KCD の比例で出す',
                             'ア（J→C→L→K）を KC で2つに分けると、△KJC 4.395㎡ ＋ △KCL。Lが CD 上にあるので △KCL ＝ △KCD × t（CL ＝ CD × t）。\n'
                             't ＝ (11.3379535 − 4.395) ÷ 73.0386 ＝ 0.0950…、L ＝ C ＋ (D − C) × t で L（−8033.30, −2510.33）。\n'
                             'アとイを同じ面積（10.4305㎡）にすると（−8033.41, −2510.41）にずれる。',
                             ncols=2, width_ratios=[1.0, 1.0])
za = Zu(ax1, fontsize=14)
fit(ax1, [K, C, D, J, L], margin=0.10, pad_aspect=True)
za.poly([K, C, D], color=ORANGE, lw=1.6, ls='--', fill=ORANGE, alpha=0.10)
za.poly([K, J, C], color=BLUE, lw=1.4, fill=BLUE, alpha=0.30)
za.poly([K, C, L], color=RED, lw=1.4, fill=RED, alpha=0.40)
za.line(C, D, color=BLACK, lw=2.2)
za.north_arrow(length=0.07)
for n in ('K', 'J', 'C', 'D'):
    za.point(PTS[n], KIND[n])
    za.point_label(PTS[n], n, away=centroid([K, C, D]))
za.point(L, 'dot', color=RED, size=8)
za.callout(centroid([K, C, D]), '△KCD　73.0386㎡', dirs=(90, 110, 70), color=ORANGE, dists=(40, 60, 80))
za.callout(K + (C - K) * 0.3 + (J - K) * 0.3, '△KJC　4.395㎡', dirs=(-120, -100, -140), color=BLUE, dists=(70, 95))
ax1.set_title('全体', fontsize=17, weight='bold', pad=6)

zb = Zu(ax2, fontsize=15)
fit(ax2, [C + P(-0.6, -2.1), C + P(2.2, 2.3)], margin=0.0, pad_aspect=True)
zb.line(C, C + (D - C) * 0.26, color=BLACK, lw=2.2)
zb.line(C, C + (K - C) * 0.20, color=BLACK, lw=1.4, ls='--')
zb.line(C, C + (J - C) * 0.20, color=BLACK, lw=2.0)
zb.line(L, L + (K - L) * 0.20, color=RED, lw=2.4)
zb.line(LE, LE + (K - LE) * 0.20, color=GRAY, lw=1.6, ls='--')
zb.north_arrow(length=0.08)
zb.point(C, 'concrete')
zb.point_label(C, 'C', away=C + P(1, -1))
zb.point(L, 'dot', color=RED, size=10)
zb.point_label(L, 'L', away=L + P(-1, 1), color=RED)
zb.point(LE, 'dot', color=GRAY, size=9)
zb.edge_label(C, L, 'CL 1.05', C + P(-2, 0), color=RED, fs=15)
zb.callout(L, 'L（−8033.30, −2510.33）', dirs=(60, 75, 45, 90), color=RED, dists=(90, 120, 150))
zb.callout(LE, '誤り：同じ面積にしたL\n（−8033.41, −2510.41）', dirs=(-150, -165, -135, 180), color=GRAY, dists=(90, 120, 150))
zb.callout(C + (D - C) * 0.17, 'Dへ（CD 11.06）', dirs=(-20, -40, 0, -60), color=BLACK, dists=(40, 60, 80))
zb.callout(C + (J - C) * 0.18, 'Jへ', dirs=(-120, -140, -100), color=BLACK, dists=(40, 60))
ax2.set_title('Cのまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H24_dai21mon_zu06_L_hirei.png')

# =====================================================================
# 図7：L点の別解（KCに平行な線。真数表の136°33′28″と46°33′28″）
# =====================================================================
fig, (ax,) = new_figure('図7　L点の別解　KCから高さ1.0266…の平行線とCDの交点',
                        '△KCL ＝ 11.3379535 − 4.395 ＝ 6.9429535㎡。KC（13.5248…）を底辺にすると高さは 2 × 6.9429535 ÷ 13.5248… ＝ 1.0266…。\n'
                        'CからKCに直角な向き（46°33′28″）へ1.0266…進んだ点Mを通り、KC（K→Cは136°33′28″）に平行な線とCDの交点がL。\n'
                        '真数表の136°33′28″と46°33′28″は、この解き方のための行。答えは本解と同じ L（−8033.30, −2510.33）。')
z = Zu(ax, fontsize=15)
fit(ax, [C + P(-0.8, -3.4), C + P(2.4, 1.8)], margin=0.0, pad_aspect=True)
KC_U = (C - K) / abs(C - K)
z.line(C - KC_U * 3.2, C, color=BLACK, lw=2.0)
z.line(M - KC_U * 3.2, M + KC_U * 0.6, color=RED, lw=1.8, ls='--')
z.line(C, C + (D - C) * 0.24, color=BLACK, lw=2.2)
z.line(C, M, color=BLUE, lw=2.0)
z.right_angle(C, C - KC_U, M, size=0.18, color=BLUE)
z.north_arrow(length=0.08)
z.point(C, 'concrete')
z.point_label(C, 'C', away=C + P(1, 1))
z.point(M, 'dot', color=BLUE, size=8)
z.point_label(M, 'M', away=M + P(-1, 1), color=BLUE)
z.point(L, 'dot', color=RED, size=10)
z.point_label(L, 'L', away=L + P(1, -1), color=RED)
z.edge_label(C, M, '1.0266…', C + P(1, -1), color=BLUE, fs=15, dists=(14, 20, 26))
z.callout(C - KC_U * 2.6, 'Kへ（KC 13.5248…）\nK→C 136°33′28″', dirs=(-150, -170, -130), color=BLACK, dists=(50, 70, 90))
z.callout(C + (M - C) * 0.3, 'KCに直角な向き\n46°33′28″', dirs=(-10, 10, -30), color=BLUE, dists=(110, 135, 160))
z.callout(M + KC_U * 0.5, 'Mを通りKCに平行な線', dirs=(-60, -40, -80), color=RED, dists=(40, 60, 80))
z.callout(L, 'L（−8033.30, −2510.33）', dirs=(165, 180, 150), color=RED, dists=(110, 140, 170))
z.callout(C + (D - C) * 0.22, 'Dへ', dirs=(20, 0, 40), color=BLACK, dists=(40, 60))
ALL_PROBLEMS += save(fig, [z], 'H24_dai21mon_zu07_L_betsukai.png')

# =====================================================================
# 図8：問2 地積測量図（5番1の分筆）の完成見本
# =====================================================================
fig, (ax,) = new_figure('図8　問2　地積測量図（5番1の分筆）の完成見本',
                        '5番1の分筆は5番2の分筆より先に申請するので、G・H・J・Cの南の隣接地は「5－2」（5－4ではない）。辺長は小数第3位を四捨五入（問題文の注3）。\n'
                        '座標値・平面直角座標系の番号又は記号・測量年月日・地積と求積方法は書かない（問題文の注3）。基準点は最も近い 4-611・4-612 の2点だけ、\n'
                        '位置と名称を描き、名称と座標値を用紙の適宜の場所に書く。縮尺1/250で 1m ＝ 4mm（基準点まで入れて横約111mm・縦約113mm）。')
z = Zu(ax, fontsize=15)
fit(ax, [A, G, H, J, C, D, E, F + P(4.5, 0), K611, K612, P(-8044.0, -2548.0)], margin=0.05, pad_aspect=True)
z.poly([A, G, H, J, K, L, D, E, F], lw=2.0)
z.poly([J, C, L], lw=2.0, closed=False)
z.line(A, A + (A - F) / abs(A - F) * 1.6, lw=1.2)
z.line(G, G + (G - H) / abs(G - H) * 1.6, lw=1.2)
z.line(F, F + (F - E) / abs(F - E) * 1.8, lw=1.2)
z.line(F, F + (F - A) / abs(F - A) * 1.8, lw=1.2)
z.line(D, D + (D - C) / abs(D - C) * 1.6, lw=1.2)
z.line(C, C + (C - D) / abs(C - D) * 1.6, lw=1.2)
z.line(C, C + (C - J) / abs(C - J) * 1.6, lw=1.2)
z.north_arrow()
C51 = centroid([A, G, H, J, K, L, D, E, F])
for n in ('A', 'G', 'H', 'J', 'K', 'L', 'D', 'E', 'F', 'C'):
    z.point(PTS[n], KIND[n], size=6 if KIND[n] == 'concrete' else 8)
for n in ('A', 'G', 'D', 'E', 'F'):
    z.point_label(PTS[n], n, away=C51, fs=14)
z.point_label(C, 'C', away=C + P(1, -1), fs=14)
z.point_label(L, 'L', away=L + P(-1, -1), fs=14)
for n, (p, q, s_) in SIDES.items():
    if n in ('HJ', 'JK', 'CL'):
        continue
    ref = K if n == 'JC' else (C if n == 'KL' else C51)
    z.edge_label(p, q, s_, ref, fs=15)
z.callout(H, 'H', dirs=(90, 105, 75), fs=14, dists=(45, 60, 75))
z.callout(J, 'J', dirs=(-100, -120, -80), fs=14, dists=(45, 60, 75))
z.callout(K, 'K', dirs=(60, 75, 45), fs=14, dists=(45, 60, 75))
z.callout(H + (J - H) * 0.5, 'HJ 0.97', dirs=(150, 160, 140, 170), fs=14, dists=(120, 145, 170))
z.callout(J + (K - J) * 0.5, 'JK 0.65', dirs=(20, 5, 35), fs=14, dists=(70, 90, 110))
z.callout(C + (L - C) * 0.5, 'CL 1.05', dirs=(-20, -35, -5), fs=14, dists=(50, 70, 90))
z.free_text(C51 + P(3.0, 2.5), '5－1\n（イ）', fs=18)
z.callout(K + (L - K) * 0.62 + (J - K) * 0.5, '5－3（ロ）', dirs=(-60, -80, -40), fs=16, dists=(80, 105, 130))
for p, n in [(K611, '4-611'), (K612, '4-612')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=C51, fs=14)
z.free_text(A + P(3.0, -3.5), '4－2', fs=15, color=GRAY, offsets=((0, 0), (-10, 0), (0, 10)))
z.free_text(F + P(1.8, -1.2), '9', fs=15, color=GRAY, offsets=((0, 0), (-8, 8), (8, 8)))
z.free_text(E + P(2.2, 1.8), '8', fs=15, color=GRAY, offsets=((0, 0), (10, 0), (0, 10)))
z.free_text(D + P(-4.5, 2.2), '6', fs=15, color=GRAY, offsets=((0, 0), (10, 0), (0, -10)))
z.free_text(centroid([G, B, C, J]) + P(1.5, -1.0), '5－2', fs=16, color=GRAY, offsets=((0, 0), (0, -20), (20, 0)))
z.free_text(A + (G - A) * 0.5 + P(-2.2, -2.2), '道路', fs=15, color=GRAY, offsets=((0, 0), (-15, -15), (-25, 0)))
z.free_text(P(-8037.5, -2547.5),
            '（単位：ｍ）\n◎ コンクリート杭：C・D・E・G・H・J・K・L\n● 金属標：A・F\n△ D市4級基準点\n'
            '　4-611（X −8044.07、Y −2519.78）\n　4-612（X −8031.34、Y −2532.58）',
            fs=13, ha='left', va='top', offsets=((0, 0), (0, -20), (0, 20)))
ALL_PROBLEMS += save(fig, [z], 'H24_dai21mon_zu08_chiseki_sokuryouzu.png')

# =====================================================================
# 図9：問3 合筆の地積（143.47 ＋ 11.33 ＝ 154.80）
# =====================================================================
fig, (ax1, ax2) = new_figure('図9　問3　合筆後の5番2は 154.80㎡',
                             '5番2はイ（5番4）を分筆した後の I→B→C→J で 143.4704 → 143.47（平成23年の分筆のときの153.90ではない）。\n'
                             '5番3（ア）は丸めたLで 11.3374 → 11.33。合筆後は 143.4704 ＋ 11.3374 ＝ 154.8078 → 154.80。\n'
                             '合筆後の区画を I→B→C→L→K の5点で回すと 154.8103 → 154.81（Kを丸めたぶん、I・J・Kがわずかに一直線でない）。',
                             ncols=2, width_ratios=[1.0, 1.0])
for axx, title, merged in [(ax1, '合筆前（2筆）', False), (ax2, '合筆後（5番2）', True)]:
    zz = Zu(axx, fontsize=14)
    fit(axx, [I, B, C, L, K, J, G, H, B + P(-2.0, 0)], margin=0.10, pad_aspect=True)
    zz.poly([G, H, J, I], color=GRAY, lw=1.1, ls='--')
    if merged:
        zz.poly([I, B, C, L, K], color=RED, lw=2.2, fill=RED, alpha=0.18)
        zz.free_text(centroid([I, B, C, J]), '5番2\n154.8078\n→ 154.80㎡', fs=17, color=RED)
    else:
        zz.poly([I, B, C, J], color=GREEN, lw=2.0, fill=GREEN, alpha=0.18)
        zz.poly(AA, color=BLUE, lw=2.0, fill=BLUE, alpha=0.30)
        zz.free_text(centroid([I, B, C, J]), '5番2\n143.4704\n→ 143.47㎡', fs=17, color=GREEN)
        zz.callout(K + (L - K) * 0.55, '5番3（ア）\n11.3374 → 11.33㎡', dirs=(60, 80, 40), color=BLUE, dists=(50, 70, 90))
    zz.north_arrow(length=0.07)
    for n in ('I', 'B', 'C', 'J', 'K', 'L'):
        zz.point(PTS[n], KIND[n], size=5 if KIND[n] == 'concrete' else 7)
        zz.point_label(PTS[n], n, away=centroid([I, B, C, J]), fs=13)
    zz.callout(centroid([G, H, J, I]), '5番4（イ）', dirs=(150, 170, 130), color=GRAY, dists=(40, 60, 80))
    axx.set_title(title, fontsize=17, weight='bold', pad=6)
    ALL_PROBLEMS += zz.check_overlaps('図9 ' + title)
path = os.path.join(OUT, 'H24_dai21mon_zu09_gappitsu_chiseki.png')
fig.savefig(path, dpi=100, facecolor='white')
print('  →', path)

# =====================================================================
# 図10：問4 地積更正では筆界は動かない（整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図10　問4　地積更正では筆界は動かない')
BOX = [
    (57, '地積の更正の登記（報告的な登記）', BLUE, [
        '登記記録の地積が、筆界で囲まれた実際の面積と違うときに、正しい地積に直す登記',
        '筆界の位置は変わらない。5番1と5番2の筆界は「G点、H点及びC点を順次直線で結んだ線」のまま',
        '平成23年の分筆で登記した地積は、この線で求めたもので誤りはない（直すものがない）',
    ]),
    (22, '分筆・交換・合筆（形成的な登記）', RED, [
        '分筆で新しい筆界を作り、交換で所有権を移し、合筆で1筆にする',
        'これで「I点、K点及びL点を順次直線で結んだ線」が新しい筆界になる',
        '筆界は公法上の境界で、所有者どうしの合意では動かない（法第123条第1号：登記された時の境）',
    ]),
]
for y0, head, col, lines in BOX:
    ax.add_patch(FancyBboxPatch((3, y0), 94, 31, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=col, lw=2.2))
    ax.text(5, y0 + 27, head, fontsize=21, weight='bold', va='center', color=col)
    for i, t in enumerate(lines):
        ax.text(7, y0 + 20 - i * 7, '・' + t, fontsize=16, va='center')
ax.text(50, 9, '結論：お互いの土地の地積を更正する方法による登記の手続をすることはできない',
        fontsize=19, weight='bold', ha='center', va='center', color=RED)
fig.text(0.5, 0.035, '理由は「G点、H点及びC点を順次直線で結んだ線」と「I点、K点及びL点を順次直線で結んだ線」の2つの語句を使って書く（問4の指定）。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H24_dai21mon_zu10_chiseki_kousei.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図10: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図11：本番で解く順番（整理図。固定配置）
# =====================================================================
fig, ax = fixed_figure('図11　本番で解く順番（L点と地積測量図がいちばん時間を食う）')
STEPS = [
    ('1', '問4（第3欄）　計算なし', ['結論「できない」と、2つの語句を使った理由を先に書く'], GRAY),
    ('2', '問3の申請書のうち計算なしで書ける欄', ['登記の目的・添付書類・登録免許税（1,000円）・申請人（海川二郎）・所在・地番と地目・原因'], GREEN),
    ('3', '5番2の地積 143.47', ['I・Jは別紙5に座標がある。I→B→C→Jの四角形（対角線の式）でK・Lがなくても出せる'], BLUE),
    ('4', 'K点 → イの面積 → L点（問1）', ['K ＝ J ＋ (J − I) ÷ Abs(J − I) × 0.65、イ 10.4305 × 1.087、△KJC・△KCDでtを出してL'], RED),
    ('5', '5番3の 11.33 と合筆後の 154.80', ['丸めたLで 11.3374、143.4704 ＋ 11.3374 ＝ 154.8078 → 154.80'], ORANGE),
    ('6', '地積測量図（問2）', ['辺長11本・境界標・4-611と4-612・隣接地（5－2）。答案用紙の枠に縮尺どおり入る'], PURPLE),
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
fig.text(0.5, 0.035, '1〜3はL点がなくても書ける。L点で詰まっても、第3欄と申請書の大部分は点になる。',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'H24_dai21mon_zu11_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図11: 整理図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
