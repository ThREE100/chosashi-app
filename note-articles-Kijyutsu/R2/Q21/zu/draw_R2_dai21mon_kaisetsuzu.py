"""令和2年度 第21問（土地）会話形式note記事の解説図7枚を、座標値から作図する。

`../prompt_R2_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。

実行: python3 note-articles-Kijyutsu/R2/Q21/zu/draw_R2_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, area, chiseki  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
A, C, D, E, F = P(16.78, -2.92), P(34.00, 10.35), P(24.45, 19.50), P(16.18, 14.48), P(8.93, 7.23)
A_, B_, C_ = P(109.23, 133.26), P(117.63, 141.66), P(126.45, 146.53)   # 任意座標
K1, K2 = P(3.24, 2.76), P(19.39, 24.16)                                 # A市基準点1・2
B = r2(A + (B_ - A_) * (C - A) / (C_ - A_))
S4 = area([B, C, D, E])
BH = (156.53 - S4) / abs(E - B)
H = r2(B + (A - B) / abs(A - B) * BH)
G = r2(E + (F - E) / abs(F - E) * BH)

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('B', B, P(25.18, 5.48)), ('H', H, P(23.34, 3.64)), ('G', G, P(14.34, 12.64))]:
    assert abs(got - want) < 1e-9, (n, got, want)
assert abs((C - A) / (C_ - A_) - 1) < 1e-12                     # 回転も縮尺もない
assert abs((A - A_) - (C - C_)) < 1e-9                          # 移動量が同じ
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'AH': (A, H, '9.28'), 'HB': (H, B, '2.60'), 'BE': (B, E, '12.73'), 'EG': (E, G, '2.60'),
         'GF': (G, F, '7.65'), 'FA': (F, A, '12.83'), 'HG': (H, G, '12.73')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
AREAS = {'32番4': (S4, 123.41075), '32番5': (area([A, B, E, F]), 140.85), '甲区画': (area([B, C, D, E, G, H]), 156.53075),
         '（イ）': (area([A, H, G, F]), 107.73), '（ロ）': (area([B, E, G, H]), 33.12)}
for n, (got, want) in AREAS.items():
    assert abs(got - want) < 5e-6, (n, got, want)
assert chiseki(area([B, C, D, E, G, H])) == 156.53 and chiseki(area([A, H, G, F])) == 107.73
assert round(123.00 + chiseki(area([B, E, G, H])), 2) == 156.12
print('数値の照合: すべて一致')

N4 = [B, C, D, E]           # 32番4（今）
N5 = [A, B, E, F]           # 32番5（今）
KOU = [B, C, D, E, G, H]    # 甲区画
OTSU = [A, H, G, F]         # 乙区画＝（イ）
RO = [B, E, G, H]           # （ロ）
KUI = {'A': 'concrete', 'B': 'metal', 'C': 'concrete', 'D': 'concrete', 'E': 'metal', 'F': 'concrete',
       'G': 'concrete', 'H': 'concrete'}


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


ALL = []


# =====================================================================
# 図1：全体像
# =====================================================================
fig, (ax,) = new_figure('図1　北を上にして描き直した全体像（依頼を受けた時点）',
                        '問題の調査図素図は北が左上を向いている。座標どおりに北を上にすると、ABとEFは北東向きの平行な直線、BEはそれに直角だとわかる。\n'
                        '今の筆界はBとEを結ぶ直線。依頼は、GとHを結ぶ直線（赤の破線）まで32番4を南へ広げること。')
z = Zu(ax)
fit(ax, [A, B, C, D, E, F, G, H, K1, K2], margin=0.10, pad_aspect=True)
z.poly(N4, fill=GREEN)
z.poly(N5, fill=BLUE)
z.line(H, G, color=RED, lw=1.8, ls='--')
z.north_arrow()
c4, c5 = centroid(N4), centroid(N5)
z.free_text(c4, '32番4（本件土地1）\n宅地　123.00㎡', fs=16)
z.free_text(c5 + P(-1.2, -1.2), '32番5（本件土地2）\n宅地　140.80㎡', fs=16, offsets=((0, 0), (0, -15)))
for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F')]:
    z.point(p, KUI[n])
    z.point_label(p, n, away=centroid([A, C, D, F]))
for p, n in [(H, 'H'), (G, 'G')]:
    z.point(p, 'dot', color=RED)
    z.point_label(p, n, away=c5, color=RED)
for p, n in [(K1, 'A市基準点1'), (K2, 'A市基準点2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=c5, dists=(30, 40, 50))
z.callout(H + (G - H) * 0.3, '希望する新しい境（HとGを結ぶ直線）', dirs=(-150, -170, -130), color=RED, dists=(120, 150, 180))
z.edge_label(C, D, '32-13', c4, fs=15, dists=(20, 28), rotate=False)
z.edge_label(F, A, '32-1', c5, fs=15, dists=(22, 30), rotate=False)
z.edge_label(B, C, '道路', c4, fs=15, dists=(30, 40), rotate=False)
z.edge_label(A, B, '道路', c5, fs=15, dists=(30, 40), rotate=False)
z.edge_label(D, E, '道路', c4, fs=15, dists=(30, 40), rotate=False)
z.edge_label(E, F, '道路', c5, fs=15, dists=(30, 40), rotate=False)
ALL += save(fig, [z], 'R2_dai21mon_zu01_zentaizu.png')

# =====================================================================
# 図2：問1 B点（座標変換）
# =====================================================================
fig, axes = new_figure('図2　問1　B点の求め方（任意座標から測量の座標へ変換）',
                       '(C − A) ÷ (C′ − A′) ＝ 1：回転も縮尺もない。A′→A と C′→C の移動量はどちらも（−92.45, −136.18）で、平行移動だけで重なる。\n'
                       'B ＝ A ＋ (B′ − A′) × (C − A) ÷ (C′ − A′) ＝ 25.18 ＋ 5.48i　→　B点（25.18, 5.48）',
                       ncols=2)
zs = []
for ax, pts, names, ttl, col in [(axes[0], (A_, B_, C_), ('A′', 'B′', 'C′'), '道路境界確認図の任意座標', GRAY),
                                 (axes[1], (A, B, C), ('A', 'B', 'C'), '測量で得た座標', RED)]:
    z = Zu(ax)
    pa, pb, pc = pts
    fit(ax, [pa, pb, pc], margin=0.55, pad_aspect=True)
    z.line(pa, pb, lw=2.2)
    z.line(pb, pc, lw=2.2)
    z.line(pa, pc, color=GRAY, lw=1.2, ls='--')
    z.north_arrow()
    ax.set_title(ttl, fontsize=19, color=col, weight='bold', pad=4)
    ref = pa + (pc - pa) * 0.5 + P(-3, 3)
    for p, n in zip(pts, names):
        z.point(p, 'dot', color=(RED if n == 'B' else BLACK))
    z.callout(pa, f'{names[0]}（{pa.real:.2f}, {pa.imag:.2f}）', dirs=(-60, -90, -30), dists=(60, 80))
    z.callout(pb, f'{names[1]}（{pb.real:.2f}, {pb.imag:.2f}）', dirs=(170, 150, 190), color=(RED if col == RED else BLACK),
              dists=(70, 90, 110))
    z.callout(pc, f'{names[2]}（{pc.real:.2f}, {pc.imag:.2f}）', dirs=(60, 90, 30), dists=(60, 80))
    ax.text(0.5, 1.0, f'{names[1]} − {names[0]} ＝ 8.40 ＋ 8.40i\n{names[2]} − {names[0]} ＝ 17.22 ＋ 13.27i（破線）',
            transform=ax.transAxes, ha='center', va='top', fontsize=15, color=BLUE)
    zs.append(z)
ALL += save(fig, zs, 'R2_dai21mon_zu02_B_henkan.png')

# =====================================================================
# 図3：問1 G点・H点（長方形BEGH）
# =====================================================================
fig, (ax,) = new_figure('図3　問1　G点・H点の求め方（GH ∥ BE、甲区画 156.53㎡）',
                        '32番4（今）の実測 123.41075㎡ に足りない 156.53 − 123.41075 ＝ 33.11925㎡ を32番5から持ってくる。\n'
                        'BE ⊥ AB、BE ⊥ EF なので B・E・G・H は長方形。BH ＝ 33.11925 ÷ 12.7279… ＝ 2.6020…　→　面積 18 × 1.84 ＝ 33.12㎡')
z = Zu(ax)
fit(ax, [A, B, C, D, E, F, G, H], margin=0.14, pad_aspect=True)
z.poly(N4, color=BLACK, lw=2.0, fill=BLUE)
z.poly(RO, color=RED, lw=0, fill=ORANGE, alpha=0.35, check=False)
z.poly(OTSU, color=GRAY, lw=1.4)
z.line(H, G, color=RED, lw=2.6)
z.north_arrow()
z.right_angle(B, A, E, size=0.7, color=BLACK)
z.right_angle(E, F, B, size=0.7, color=BLACK)
z.parallel_chevron(B, E)
z.parallel_chevron(H, G, color=RED)
z.free_text(centroid(N4), '32番4（今）\n実測 123.41075㎡', fs=16, offsets=((0, 40), (0, 60), (20, 60)))
z.edge_label(H, G, '33.12㎡', centroid(RO), color=RED, fs=15, outward=False, dists=(34, 30, 38),
             ts=(0.62, 0.68, 0.72))
z.free_text(centroid(OTSU), '乙区画\n107.73㎡', fs=15, color=GRAY)
z.edge_label(H, B, '2.60', centroid(KOU), color=RED, fs=15, dists=(16, 22, 28))
z.edge_label(E, G, '2.60', centroid(KOU), color=RED, fs=15, dists=(16, 22, 28))
for p, n in [(A, 'A'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (B, 'B')]:
    z.point(p, KUI[n])
    z.point_label(p, n, away=(E - P(0, 1) if n == 'E' else centroid([A, C, D, F])))
z.point(H, 'dot', color=RED)
z.point(G, 'dot', color=RED)
z.callout(H, 'H（23.34, 3.64）', dirs=(180, 200, 160), color=RED)
z.callout(G, 'G（14.34, 12.64）', dirs=(-60, -45, -75), color=RED)
z.edge_label(B, E, 'BE ＝ 12.7279…', centroid(RO), fs=15, dists=(18, 24, 30), ts=(0.25, 0.2, 0.3))
ALL += save(fig, [z], 'R2_dai21mon_zu03_GH_chouhoukei.png')

# =====================================================================
# 図4：問2 公差の判定（2本の数直線）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図4　問2　地積更正が必要かの判定（市街地地域なので精度区分 甲2）', fontsize=24, weight='bold', y=0.96)
for i, (name, reg, meas, k2, k1) in enumerate([('32番4', 123.00, 123.41075, 0.91, 0.38),
                                                ('32番5', 140.80, 140.85, 1.00, 0.41)]):
    ax = fig.add_axes([0.06, 0.55 - i * 0.33, 0.88, 0.27])
    ax.set_xlim(reg - 1.6, reg + 1.6)
    ax.set_ylim(-1.6, 2.0)
    ax.axis('off')
    ax.plot([reg - 1.5, reg + 1.5], [0, 0], color=BLACK, lw=2)
    for j in range(-6, 7):
        v = reg + j * 0.25
        ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1.0)
        if j % 2 == 0:
            ax.text(v, -0.3, f'{v:.2f}', ha='center', va='top', fontsize=12, color=GRAY)
    ax.axvspan(reg - k2, reg + k2, ymin=0.40, ymax=0.52, color=GREEN, alpha=0.30)
    ax.text(reg - 1.55, 0.55, f'{name}', ha='left', va='center', fontsize=20, weight='bold')
    ax.text(reg - k2, 0.62, f'甲2 の公差の範囲 ±{k2:.2f}', ha='left', va='bottom', fontsize=14, color=GREEN)
    if name == '32番4':
        ax.plot([reg - k1, reg + k1], [1.25, 1.25], color=GRAY, lw=3, ls='--')
        ax.text(reg - k1, 1.4, f'甲1 なら ±{k1:.2f}（この外に出てしまう）', ha='left', va='bottom', fontsize=13,
                color=GRAY)
    ax.plot([reg], [0], 'o', ms=12, color=BLUE)
    ax.text(reg, -0.75, f'登記記録 {reg:.2f}㎡', ha='right', va='top', fontsize=15, color=BLUE, weight='bold')
    ax.plot([meas], [0], 'o', ms=12, color=RED)
    ax.text(meas + 0.03, -0.75, f'実測 {meas:.5f}'.rstrip('0') + '㎡', ha='left', va='top', fontsize=15, color=RED,
            weight='bold')
    ax.text(reg + 1.5, 0.62, f'差 {meas - reg:.2f}㎡ ≦ {k2:.2f}㎡　→ 範囲内', ha='right',
            va='bottom', fontsize=15, color=RED, weight='bold')
fig.text(0.5, 0.06, '本件土地の地域は市街地地域（不動産登記規則第10条第2項第1号）。誤差の限度は精度区分 甲2 まで（同条第4項第1号）。\n'
         '問題文の表の甲2（123.00㎡は0.91、140.80㎡は1.00）で比べると、どちらも範囲内 → 地積更正の登記は申請しない。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R2_dai21mon_zu04_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図4: 数直線（固定配置）\n  →', path)

# =====================================================================
# 図5：問2 分合筆の流れ（申請書の土地の表示）
# =====================================================================
fig, axes = new_figure('図5　問2　分合筆の流れ（申請書の地積はどれか）',
                       '（イ）32番5 は座標で求めた 107.73㎡（140.80 − 33.12 ＝ 107.68 ではない）。（ロ）は 33.12㎡。\n'
                       '合筆後の32番4 は、登記記録の 123.00 ＋（ロ）33.12 ＝ 156.12㎡。甲区画の座標の面積 156.53㎡ は書かない。',
                       ncols=2)
zs = []
for ax, after in [(axes[0], False), (axes[1], True)]:
    z = Zu(ax, fontsize=14)
    fit(ax, [A, B, C, D, E, F, G, H], margin=0.16, pad_aspect=True)
    if not after:
        ax.set_title('申請前（登記記録）', fontsize=19, weight='bold')
        z.poly(N4, fill=GREEN)
        z.poly(N5, fill=BLUE)
        z.line(H, G, color=RED, lw=1.8, ls='--')
        z.free_text(centroid(N4), '32番4\n123.00㎡', fs=16)
        z.free_text(centroid(N5) + P(-1.5, -1.5), '32番5\n140.80㎡', fs=16)
        z.callout(H + (G - H) * 0.5, '分筆線 HG', dirs=(-150, -170, -130), color=RED, dists=(70, 90))
    else:
        ax.set_title('分合筆の後', fontsize=19, weight='bold')
        z.poly(KOU, fill=GREEN)
        z.poly(OTSU, fill=BLUE)
        z.poly(RO, color=RED, lw=1.6, ls='--', fill=ORANGE, alpha=0.30, check=False)
        z.free_text(centroid(N4), '32番4（合筆後）\n123.00 ＋ 33.12\n＝ 156.12㎡', fs=15)
        z.free_text(centroid(OTSU), '（イ）32番5\n107.73㎡', fs=15)
        z.callout(centroid(RO), '（ロ）33.12㎡\n32番5から分割して\n32番4に合併する部分', dirs=(-165, 180, -150, 150), color=RED,
                  dists=(150, 180, 210))
    z.north_arrow()
    zs.append(z)
ALL += save(fig, zs, 'R2_dai21mon_zu05_bungoppitsu.png')

# =====================================================================
# 図6：問3 登記識別情報の整理（固定配置）
# =====================================================================
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図6　問3　登記識別情報の整理（ア〜オ）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')


def box(x, y, w, h, text, ec=BLACK, fc='white', fs=16, weight='normal', color=BLACK):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.6', ec=ec, fc=fc, lw=1.8))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs, weight=weight, color=color)


box(3, 76, 94, 17, '登記識別情報は、アラビア数字その他の符号の組合せで\n（ア）不動産 及び（イ）登記名義人 となった申請人ごとに定める（不動産登記規則第61条）',
    ec=BLUE, fc='#eef4fb', fs=18)
box(3, 45, 44, 22, '電子申請\n電子計算機のファイルに記録する方法\n＋ 申出により（ウ）書面 の交付', fs=17)
box(53, 45, 44, 22, '書面申請\n登記識別情報を記載した（ウ）書面 を交付\n（規則第63条第1項第2号）', fs=17)
box(3, 8, 58, 28, '表示に関する登記で、登記名義人の登記識別情報を\n提供する登記（不動産登記令第8条第1項第1号〜第3号）\n'
    '・所有権の登記がある土地の（エ）合筆\n・所有権の登記がある建物の合体による登記等\n・所有権の登記がある建物の（オ）合併', ec=RED, fc='#fdeeee', fs=16)
box(67, 8, 30, 28, '分筆は提供不要\n（1筆を分けるだけ）\n\n今回の分合筆は\n合筆を含むので\n登記済証で提供', ec=GRAY, fc='#f4f4f4', fs=16,
    color=BLACK)
fig.text(0.5, 0.04, '答え　ア：不動産　イ：登記名義人　ウ：書面　エ：合筆　オ：合併', ha='center', va='center', fontsize=19,
         weight='bold', color=RED)
path = os.path.join(OUT, 'R2_dai21mon_zu06_shikibetsu.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図6: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図7：問4 地積測量図の完成見本
# =====================================================================
fig, (ax,) = new_figure('図7　問4　地積測量図（32番5）の完成見本',
                        '縮尺1/250で答案用紙に描くと 1m ＝ 4mm。辺長は小数第3位を四捨五入（HB は 2.6021… なので 2.60、AH は 9.2772… なので 9.28）。\n'
                        '分筆前の32番5を描き、分筆線HGで（イ）（ロ）に分ける（規則第78条）。座標値・地積・求積方法は書かない（問題文の注5）。基準点は位置と点名だけ（問題文の注6）。')
z = Zu(ax)
fit(ax, [A, B, E, F, G, H, K1, K2], margin=0.10, pad_aspect=True)
z.poly([A, H, B, E, G, F], lw=2.0)
z.line(H, G, lw=2.0)
z.north_arrow()
c5 = centroid(N5)
for n, (p, q, s) in SIDES.items():
    ref = c5 if n != 'HG' else centroid(OTSU)
    z.edge_label(p, q, s, ref, fs=16, outward=(n != 'HG'))
z.free_text(centroid(OTSU), '（イ）\n32－5', fs=17)
z.free_text(centroid(RO), '（ロ）', fs=16)
for p, n in [(A, 'A'), (H, 'H'), (B, 'B'), (E, 'E'), (G, 'G'), (F, 'F')]:
    z.point(p, 'metal' if KUI[n] == 'metal' else 'concrete', size=(9 if KUI[n] == 'metal' else 7))
    z.point_label(p, n, away=c5)
for p, n in [(K1, 'A市基準点1'), (K2, 'A市基準点2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=c5, dists=(30, 40, 50))
z.edge_label(B, E, '32－4', c5, fs=16, dists=(40, 50), rotate=False)
z.edge_label(F, A, '32－1', c5, fs=16, dists=(40, 50), rotate=False)
z.edge_label(A, H, '道路', c5, fs=16, dists=(44, 54), rotate=False)
z.edge_label(G, F, '道路', c5, fs=16, dists=(44, 54), rotate=False)
z.free_text(P(7.0, 17.0), '（単位：ｍ）\n◎ コンクリート杭：A・F・G・H\n● 金属標：B・E\n△ 基準点：A市基準点1・2', fs=13,
            ha='left', va='top', offsets=((0, 0), (0, -30), (20, 0)))
ALL += save(fig, [z], 'R2_dai21mon_zu07_chiseki_sokuryouzu.png')

# =====================================================================
# 図8：問1 四角形の面積を対角線で出す別解（32番4）
#       （2026-09-29追加。アガルートの解説と照らし合わせて記事に足した別解用）
# =====================================================================
dz = (B - D).conjugate() * (C - E)
assert abs(dz - P(70.9112, 246.8215)) < 1e-9 and abs(abs(dz.imag) / 2 - S4) < 1e-9
fig, (ax,) = new_figure('図8　問1　四角形の面積を対角線で出す別解（32番4）',
                        '4点を順に回る式 B・Conjg(C) ＋ C・Conjg(D) ＋ D・Conjg(E) ＋ E・Conjg(B) と同じ面積を、対角線2本で1回で出せる。\n'
                        'Conjg(B − D) × (C − E) ＝ 70.9112 ＋ 246.8215i　→　iの係数 246.8215 ÷ 2 ＝ 123.41075㎡（（イ）も Conjg(H − F) × (G − A) で 107.73㎡）')
z = Zu(ax)
fit(ax, [A, B, C, D, E, F], margin=0.12, pad_aspect=True)
z.poly(N5, color=GRAY, lw=1.2)
z.poly(N4, color=BLACK, lw=2.0, fill=BLUE)
z.line(B, D, color=RED, lw=2.2, ls='--')
z.line(C, E, color=ORANGE, lw=2.2, ls='--')
z.north_arrow()
for p, n in [(B, 'B'), (C, 'C'), (D, 'D'), (E, 'E')]:
    z.point(p, KUI[n])
    z.point_label(p, n, away=centroid(N4))
for p, n in [(A, 'A'), (F, 'F')]:
    z.point(p, KUI[n], color=GRAY)
    z.point_label(p, n, away=centroid(N5), color=GRAY)
z.free_text(centroid(N5), '32番5', fs=15, color=GRAY)
z.callout(B + (D - B) * 0.3, '対角線1　B − D', dirs=(150, 170, 130), color=RED, dists=(80, 100, 120))
z.callout(C + (E - C) * 0.25, '対角線2　C − E', dirs=(30, 10, 50), color=ORANGE, dists=(80, 100, 120))
z.callout((C + D + centroid(N4)) / 3, '32番4\n123.41075㎡', dirs=(10, 30, -10), color=BLACK, fs=16, dists=(150, 180, 210))
ALL += save(fig, [z], 'R2_dai21mon_zu08_taikakusen.png')

# =====================================================================
# 図9：本番で解く順番（座標を使わない整理図。2026-09-29追加）
# =====================================================================
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('図9　本番で解く順番　G点・H点がなくても書ける欄を先に', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.82])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
STEPS = [
    ('① 問3　登記識別情報の穴埋め', '別紙を読まなくても答えられる（不動産・登記名義人・書面・合筆・合併）', '#eef4fb', BLUE),
    ('② 問1　B点', '(C − A) ÷ (C′ − A′) ＝ 1 を確かめて、25.18 ＋ 5.48i', '#eef4fb', BLUE),
    ('③ 問2　申請書の書ける欄', '登記の目的・添付書類・登録免許税・申請人・所在・1行目140.80・4行目123.00・原因の文言', '#eef4fb', BLUE),
    ('④ 問1　G点・H点（いちばん時間を食う）', '32番4の面積123.41075 → 33.11925 ÷ BE → H（23.34, 3.64）・G（14.34, 12.64）', '#fdf1e4', ORANGE),
    ('⑤ 問2　G点・H点が要る地積', '（イ）107.73・（ロ）33.12・合筆後の32番4 156.12', '#fdf1e4', ORANGE),
    ('⑥ 問4　地積測量図', '辺長7本（G点・H点が要る）。基準点まで入れて約88mm × 108mm', '#fdf1e4', ORANGE),
]
for i, (head, body, fc, ec) in enumerate(STEPS):
    y = 88 - i * 15.5
    ax.add_patch(FancyBboxPatch((6, y - 5.5), 88, 11, boxstyle='round,pad=0.6', ec=ec, fc=fc, lw=2))
    ax.text(9, y + 1.8, head, ha='left', va='center', fontsize=19, weight='bold', color=BLACK)
    ax.text(9, y - 2.6, body, ha='left', va='center', fontsize=15, color=BLACK)
    if i < len(STEPS) - 1:
        ax.annotate('', xy=(50, y - 9.2), xytext=(50, y - 6.6), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=2))
fig.text(0.5, 0.05, '青：G点・H点がなくても書ける　／　橙：G点・H点が要る。G点・H点で手間取っても、青の欄の点は先に取っておける',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'R2_dai21mon_zu09_kaku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図9: 整理図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL))
