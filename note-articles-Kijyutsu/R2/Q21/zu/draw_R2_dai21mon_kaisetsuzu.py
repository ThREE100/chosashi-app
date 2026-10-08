"""令和2年度 第21問（土地）会話形式note記事の解説図18枚を、座標値から作図する。

2026-10-08：最新の執筆指示書に合わせて、ワナごとの図・時系列・注の仕分けの9枚を足し、地積測量図を答案用紙の第4欄の枠ごと
描き直した。PNG名の番号（zu01〜zu18）は記事の挿入順の管理用で、画像の中のタイトルには図番を入れない（全18枚）。

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
# zu02：全体像
# =====================================================================
fig, (ax,) = new_figure('北を上にして描き直した全体像（依頼を受けた時点）',
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
ALL += save(fig, [z], 'R2_dai21mon_zu02_zentaizu.png')

# =====================================================================
# zu04：問1 B点（座標変換）
# =====================================================================
fig, axes = new_figure('問1　B点の求め方（任意座標から測量の座標へ変換）',
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
ALL += save(fig, zs, 'R2_dai21mon_zu04_B_henkan.png')

# =====================================================================
# zu05：問1 四角形の面積を対角線で出す別解（32番4）
#       （2026-09-29追加。アガルートの解説と照らし合わせて記事に足した別解用）
# =====================================================================
dz = (B - D).conjugate() * (C - E)
assert abs(dz - P(70.9112, 246.8215)) < 1e-9 and abs(abs(dz.imag) / 2 - S4) < 1e-9
fig, (ax,) = new_figure('問1　四角形の面積を対角線で出す別解（32番4）',
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
ALL += save(fig, [z], 'R2_dai21mon_zu05_taikakusen.png')

# =====================================================================
# zu07：問1 G点・H点（長方形BEGH）
# =====================================================================
fig, (ax,) = new_figure('問1　G点・H点の求め方（GH ∥ BE、甲区画 156.53㎡）',
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
ALL += save(fig, [z], 'R2_dai21mon_zu07_GH_chouhoukei.png')

# =====================================================================
# zu08：問2 公差の判定（2本の数直線）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問2　地積更正が必要かの判定（市街地地域なので精度区分 甲2）', fontsize=24, weight='bold', y=0.96)
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
path = os.path.join(OUT, 'R2_dai21mon_zu08_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] zu08: 数直線（固定配置）\n  →', path)

# =====================================================================
# zu14：問2 分合筆の流れ（申請書の土地の表示）
# =====================================================================
fig, axes = new_figure('問2　分合筆の流れ（申請書の地積はどれか）',
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
ALL += save(fig, zs, 'R2_dai21mon_zu14_bungoppitsu.png')

# =====================================================================
# zu15：問3 登記識別情報の整理（固定配置）
# =====================================================================
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問3　登記識別情報の整理（ア〜オ）', fontsize=24, weight='bold', y=0.965)
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
path = os.path.join(OUT, 'R2_dai21mon_zu15_shikibetsu.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] zu15: 整理図（固定配置）\n  →', path)

# =====================================================================
# zu18：本番で解く順番（座標を使わない整理図。2026-09-29追加）
# =====================================================================
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('本番で解く順番　G点・H点がなくても書ける欄を先に', fontsize=24, weight='bold', y=0.965)
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
path = os.path.join(OUT, 'R2_dai21mon_zu18_kaku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] zu18: 整理図（固定配置）\n  →', path)


# =====================================================================
# 2026-10-08追加の図（最新の執筆指示書で照らし直し）。画像の中に図番は入れない
#   zu01 時系列と人の関係、zu03 注の仕分け、zu06 差し引く面積、zu09 申請件数と登録免許税、zu10 地目、
#   zu11 合筆の制限、zu12 申請人、zu13 （イ）の地積、zu16 地積測量図に描く範囲、zu17 第4欄の地積測量図（枠ごと描き直し）
# =====================================================================
from matplotlib.patches import Rectangle  # noqa: E402


def board(h=9, title=''):
    setup_font()
    f = plt.figure(figsize=(16, h), dpi=100)
    f.patch.set_facecolor('white')
    f.suptitle(title, fontsize=24, weight='bold', y=0.965)
    a = f.add_axes([0.03, 0.08, 0.94, 0.82])
    a.set_xlim(0, 100)
    a.set_ylim(0, 100)
    a.axis('off')
    return f, a


def put_board(f, name):
    path = os.path.join(OUT, name)
    f.savefig(path, dpi=100, facecolor='white')
    print(f'[重なり検査] {name}: 整理図（固定配置）\n  →', path)


def rbox(a, x, y, w, h, head, body, col, fs_h=16, fs_b=13.5, fc_alpha=0.10):
    a.add_patch(Rectangle((x, y), w, h, facecolor=col, alpha=fc_alpha, edgecolor=col, lw=2))
    a.add_patch(Rectangle((x, y), w, h, fill=False, edgecolor=col, lw=2))
    a.text(x + 1.5, y + h - 2.5, head, ha='left', va='top', fontsize=fs_h, color=col, weight='bold')
    if body:
        a.text(x + 1.5, y + h - 10, body, ha='left', va='top', fontsize=fs_b, linespacing=1.6, color=BLACK)


def arrow(a, x0, y0, x1, y1, col=GRAY):
    a.annotate('', xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=col))


# ---- zu01：時系列と人の関係（第1章） ----
fig, ax = board(9, '時系列と人の関係　登記名義人の山川一郎は死亡、申請するのは相続人2人')
EV = [(6, '平成30年12月25日', '一郎の妻が死亡', GRAY, 1),
      (30, '令和2年1月1日', '山川一郎が死亡\n（32番4・32番5の\n登記名義人）', RED, -1),
      (58, '依頼・調査・測量', '相続の登記はしていない\n（登記名義人は一郎のまま）', GRAY, 1),
      (90, '令和2年10月18日', '相続人2人が\n分合筆を申請', BLUE, -1)]
ax.annotate('', xy=(99, 62), xytext=(1, 62), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, d, t, col, ud in EV:
    ax.plot([x], [62], 'o', ms=12, color=col, zorder=5)
    ax.plot([x, x], [62, 62 + ud * 8], color=col, lw=1.4)
    ax.text(x, 62 + ud * 9, d, ha='center', va='bottom' if ud > 0 else 'top', fontsize=15, color=col, weight='bold')
    ax.text(x, 62 + ud * 15, t, ha='center', va='bottom' if ud > 0 else 'top', fontsize=13, color=BLACK)
rbox(ax, 2, 2, 46, 30, '相続人（聴取記録の5、相続関係調査の結果）',
     '妻が先に死亡しているので、相続人は子の2人だけ\n・山川小太郎（Ａ市Ｂ町一丁目32番地4）\n　本件建物1に居住\n・香川浪子（Ａ市Ｂ町一丁目32番地5）\n　本件建物2に居住', BLUE)
rbox(ax, 52, 2, 46, 30, '申請書に効くこと',
     '・申請人は相続人2人（不動産登記法第30条）\n　「（被相続人　山川一郎）」と2人の住所・氏名\n・添付書類に相続証明書\n・合筆を含むので登記済証・印鑑証明書も', RED)
put_board(fig, 'R2_dai21mon_zu01_jikeiretsu.png')

# ---- zu03：注の仕分け（第1章） ----
fig, ax = board(11, '注は4か所　問題文の注1〜7、調査図素図の注1〜4、表の下の2つの注')
BOX = [
    (1, 55, 31, 41, '毎年ほぼ同じ決まり文句', '問題文の注1　行為・書類は全て適法\n問題文の注2　書面申請\n問題文の注7　訂正・加入・削除の仕方', GRAY),
    (34, 55, 31, 41, '計算の条件', '問題文の注3　座標値は小数第3位を\n　四捨五入\n問題文の注4　縮尺250分の1、\n　距離は小数第3位を四捨五入', BLUE),
    (67, 55, 32, 41, '地積測量図に書かないもの', '問題文の注5　座標値・座標系の番号・\n　地積と求積方法・測量年月日は不要\n問題文の注6　A市基準点は位置と\n　点名だけ（座標値は書かない）', GREEN),
    (1, 3, 52, 47, '今年の答えに効く指示（調査図素図の注）', '調査図素図の注1　A〜Fは筆界点、実線は筆界線\n調査図素図の注2　G点はEとFを結ぶ直線上\n調査図素図の注3　H点はAとBを結ぶ直線上\n調査図素図の注4　32番4と32番5の筆界は聴取の時点で不明\n　→ 立会いでBとEを結ぶ直線と確認', RED),
    (55, 3, 44, 47, '表の下の注（番号なし）', 'A市基準点成果表の注\n　北はX軸の正方向 → Z ＝ X ＋ Yi\n任意座標の表の注\n　A′はA、B′はB、C′はCと同一の点\n　→ 2点（A・C）で座標変換', ORANGE),
]
for x, y, w, h, t, b, col in BOX:
    rbox(ax, x, y, w, h, t, b, col)
fig.text(0.5, 0.025, '記事では「問題文の注○」「調査図素図の注○」と言い分ける（「注3」だけでは、どちらの注か分からない）', ha='center',
         fontsize=14, color=GRAY)
put_board(fig, 'R2_dai21mon_zu03_chuu_shiwake.png')

# ---- zu06：差し引く面積は座標の123.41075（登記記録の123.00ではない） ----
BWr = (156.53 - 123.00) / abs(E - B)
Hw, Gw = r2(B + (A - B) / abs(A - B) * BWr), r2(E + (F - E) / abs(F - E) * BWr)
assert Hw == P(23.32, 3.62) and Gw == P(14.32, 12.62)
KOUw = [B, C, D, E, Gw, Hw]
assert chiseki(area(KOUw)) == 156.89 and abs(area(KOUw) - 156.89075) < 5e-6
fig, (ax1, ax2) = new_figure('問1　甲区画156.53㎡から差し引くのは、座標で求めた32番4の面積',
                             '「〔調査及び測量によって得られた座標値〕による甲区画の面積」は座標の面積。引く方も座標の123.41075㎡でないと、つじつまが合わない。\n'
                             '登記記録の123.00㎡で引くと 33.53㎡ になり、H（23.32, 3.62）・G（14.32, 12.62）、甲区画は156.89㎡で依頼の156.53㎡にならない。',
                             ncols=2)
zs = []
for ax, hh, gg, col, head, need_t, kou_t in [
        (ax1, Hw, Gw, GRAY, '登記記録の123.00で引く（誤り）', '156.53 − 123.00\n＝ 33.53㎡', '甲区画 156.89㎡'),
        (ax2, H, G, RED, '座標の123.41075で引く（正しい）', '156.53 − 123.41075\n＝ 33.11925㎡', '甲区画 156.53㎡')]:
    z = Zu(ax, fontsize=14)
    fit(ax, [A, B, C, D, E, F, hh, gg], margin=0.16, pad_aspect=True)
    z.poly(N4, fill=BLUE)
    z.poly([B, E, gg, hh], color=col, lw=0, fill=ORANGE, alpha=0.35, check=False)
    z.poly([A, hh, gg, F], color=GRAY, lw=1.2)
    z.line(hh, gg, color=col, lw=2.4)
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=18, color=col, weight='bold', pad=6)
    z.free_text(centroid(N4), kou_t, fs=15)
    z.callout((B + E + gg + hh) / 4, need_t, dirs=(-150, -165, -135), color=col, dists=(150, 180, 210), fs=14)
    for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F')]:
        z.point(p, 'dot')
        z.point_label(p, n, away=centroid([A, C, D, F]))
    z.point(hh, 'dot', color=col)
    z.point(gg, 'dot', color=col)
    z.callout(hh, f'H（{hh.real:.2f}, {hh.imag:.2f}）', dirs=(180, 200, 160), color=col, dists=(60, 80, 100), fs=14)
    z.callout(gg, f'G（{gg.real:.2f}, {gg.imag:.2f}）', dirs=(-60, -45, -75), color=col, dists=(60, 80, 100), fs=14)
    zs.append(z)
ALL += save(fig, zs, 'R2_dai21mon_zu06_hikizan.png')

# ---- zu09：申請件数と登録免許税（分合筆1件で2,000円） ----
fig, ax = board(9, '問2　申請件数と登録免許税　分合筆の1件なら2,000円')
rbox(ax, 1, 52, 48, 40, '分筆してから合筆（2件）', '① 32番5の分筆：分筆後2筆 × 1,000円 ＝ 2,000円\n② 32番4への合筆：合筆後1筆 × 1,000円 ＝ 1,000円\n合計 3,000円', GRAY)
rbox(ax, 51, 52, 48, 40, '合筆してから分筆（2件）', '① 32番4と32番5の合筆：合筆後1筆 × 1,000円 ＝ 1,000円\n② 甲区画・乙区画への分筆：2筆 × 1,000円 ＝ 2,000円\n合計 3,000円', GRAY)
rbox(ax, 14, 4, 72, 40, '分合筆（1件）＝ 正解', '32番5の一部（B・E・G・H）を分筆して、そのまま32番4に合筆する\n一の申請情報で申請できる（不動産登記規則第35条第1号）\n分合筆の後に残るのは（イ）32番5と合筆後の32番4の2筆 × 1,000円 ＝ 2,000円\n（登録免許税法別表第一の一の（十三））', RED)
fig.text(0.5, 0.03, '聴取記録の10「申請件数が最も少なく、かつ、登録免許税の額が最も低額となるように」→ 登記の目的は「土地分合筆登記」', ha='center',
         fontsize=14)
put_board(fig, 'R2_dai21mon_zu09_kensuu.png')

# ---- zu10：地目（自宅の敷地の駐車場は宅地） ----
fig, ax = board(8, '問2　自宅の敷地の中の駐車場は宅地　地目変更は要らない')
rbox(ax, 1, 40, 47, 50, '問題文の事実（聴取記録の9）', '本件建物1（小太郎の居宅）の敷地に、\nアスファルトで舗装した駐車場がある\n停めているのは小太郎の自家用車', BLUE)
rbox(ax, 52, 40, 47, 50, '地目の判断', '建物の敷地と、その維持・効用を果たすために\n必要な土地は宅地\n（不動産登記事務取扱手続準則第68条第3号）\n→ 32番4は全体として宅地のまま', GREEN)
arrow(ax, 48.5, 65, 51.5, 65)
rbox(ax, 14, 3, 72, 30, 'ワナ', '「舗装した駐車場だから雑種地」として地目変更・一部地目変更を付けない\n（自宅の駐車場は建物の効用のための土地。月極の貸駐車場とは違う）', RED)
put_board(fig, 'R2_dai21mon_zu10_chimoku.png')

# ---- zu11：合筆の制限（不動産登記法第41条） ----
fig, ax = board(10, '問2　合筆の制限（不動産登記法第41条）に当たるか　32番4と32番5')
ROWS = [('第1号', '相互に接続していない土地', '接している（BEが共通の筆界）', '当たらない'),
        ('第2号', '地目又は地番区域が相互に異なる', 'どちらも宅地、Ａ市Ｂ町一丁目', '当たらない'),
        ('第3号', '所有権の登記名義人が相互に異なる', 'どちらも山川一郎', '当たらない'),
        ('第4号', '所有権の登記名義人の持分が異なる', '共有ではない', '当たらない'),
        ('第5号', '所有権の登記がない土地とある土地', 'どちらも所有権の登記あり', '当たらない'),
        ('第6号', '所有権の登記以外の権利の登記がある土地', '土地の乙区はどちらも登記事項なし', '当たらない')]
xs_ = [1, 12, 47, 79]
ws_ = [11, 35, 32, 20]
for j, hd in enumerate(['号', '合筆できない土地', '32番4・32番5', '判定']):
    ax.add_patch(Rectangle((xs_[j], 86), ws_[j], 9, facecolor='#eeeeee', edgecolor=BLACK, lw=1.2))
    ax.text(xs_[j] + ws_[j] / 2, 90.5, hd, ha='center', va='center', fontsize=15, weight='bold')
for i, row in enumerate(ROWS):
    y = 86 - (i + 1) * 10
    for j, t in enumerate(row):
        fc = '#fdeeee' if i == 5 else 'white'
        ax.add_patch(Rectangle((xs_[j], y), ws_[j], 10, facecolor=fc, edgecolor=BLACK, lw=1.0))
        ax.text(xs_[j] + (ws_[j] / 2 if j in (0, 3) else 1.2), y + 5, t, ha='center' if j in (0, 3) else 'left', va='center',
                fontsize=13.5, color=(GREEN if j == 3 else BLACK), weight=('bold' if j == 3 else 'normal'))
ax.text(50, 12, '法務信用金庫の抵当権は「本件建物2」（家屋番号32番5の建物）の乙区。土地の乙区ではないので第6号に当たらない', ha='center',
        va='center', fontsize=14.5, color=RED, weight='bold')
ax.text(50, 4, '→ 32番4と32番5（の一部）は合筆できる', ha='center', va='center', fontsize=15, weight='bold')
put_board(fig, 'R2_dai21mon_zu11_goppitsu_seigen.png')

# ---- zu12：申請人（相続の登記をせず、相続人が法第30条で申請） ----
fig, ax = board(10, '問2　申請人は相続人　相続の登記をせずに分合筆を申請する')
rbox(ax, 1, 50, 48, 42, '先に相続の登記をする（誤り）', '① 相続による所有権の移転の登記\n　（別の申請。登録免許税もかかる）\n② 小太郎・浪子の名義で分合筆を申請\n→ 聴取記録の10（件数・登録免許税を最少に）に反する', GRAY)
rbox(ax, 51, 50, 48, 42, '相続人がそのまま申請（正しい）', '登記名義人の山川一郎のまま、相続人が\n分合筆を申請できる（不動産登記法第30条）\n→ 申請は分合筆の1件だけ\n添付書類に相続証明書（不動産登記令第7条第1項第4号）', RED)
ax.add_patch(Rectangle((14, 4), 72, 38, facecolor='white', edgecolor=BLUE, lw=2))
ax.text(16, 38, '申請人の欄', ha='left', va='top', fontsize=16, color=BLUE, weight='bold')
ax.text(18, 28, '（被相続人　山川一郎）\n相続人　Ａ市Ｂ町一丁目32番地４　山川小太郎\n　　　　Ａ市Ｂ町一丁目32番地５　香川浪子', ha='left', va='top',
        fontsize=16, color='#1a3a8f', linespacing=1.7)
put_board(fig, 'R2_dai21mon_zu12_shinseinin.png')

# ---- zu13：（イ）の地積は座標で求めた107.73（引き算の107.68ではない） ----
assert chiseki(area(OTSU)) == 107.73 and round(140.80 - 33.12, 2) == 107.68 and round(107.73 + 33.12, 2) == 140.85
fig, (ax,) = new_figure('問2　（イ）32番5の地積は、座標で求めた107.73㎡',
                        '分筆後の各土地の地積は、それぞれ座標で求めた面積。登記記録の140.80から（ロ）33.12を引いた残り（107.68）ではない。\n'
                        '（イ）107.73 ＋（ロ）33.12 ＝ 140.85㎡。登記記録の140.80㎡との差0.05㎡は、甲2の公差1.00㎡の範囲内（地積更正は要らない）。')
z = Zu(ax)
fit(ax, [A, B, E, F, G, H], margin=0.14, pad_aspect=True)
z.poly(OTSU, fill=BLUE)
z.poly(RO, color=RED, lw=1.6, ls='--', fill=ORANGE, alpha=0.30, check=False)
z.north_arrow()
for p, n in [(A, 'A'), (H, 'H'), (G, 'G'), (F, 'F'), (B, 'B'), (E, 'E')]:
    z.point(p, 'dot', color=(RED if n in 'GH' else BLACK))
    z.point_label(p, n, away=centroid(N5))
z.free_text(centroid(OTSU), '（イ）32番5\nA・H・G・Fを座標で求積\n107.73㎡', fs=16, linespacing=1.6)
z.callout(centroid(RO), '（ロ）33.12㎡', dirs=(30, 45, 15), color=RED, dists=(120, 150, 180))
z.callout(A + (F - A) * 0.45, '140.80 − 33.12 ＝ 107.68 は書かない', dirs=(-120, -135, -105), color=GRAY,
          dists=(70, 90, 110), fs=15)
ALL += save(fig, [z], 'R2_dai21mon_zu13_i_chiseki.png')

# ---- zu16：地積測量図に描く範囲（分筆前の32番5だけ） ----
fig, (ax1, ax2) = new_figure('問4　地積測量図に描くのは、分筆前の32番5だけ',
                             '分筆の登記の地積測量図は、分筆前の土地を描き、分筆線を明らかにして分筆後の各土地に符号を付ける（不動産登記規則第78条）。\n'
                             '分筆するのは32番5なので、A・H・B・E・G・Fと分筆線HG。32番4（甲区画）は合筆を受けるだけなので描かない。',
                             ncols=2)
zs = []
for ax, ok in [(ax1, False), (ax2, True)]:
    z = Zu(ax, fontsize=14)
    fit(ax, [A, B, C, D, E, F, G, H], margin=0.16, pad_aspect=True)
    z.north_arrow(length=0.07)
    if not ok:
        ax.set_title('甲区画と乙区画の両方を描く（誤り）', fontsize=18, color=GRAY, weight='bold', pad=6)
        z.poly(KOU, color=GRAY, lw=2.0, fill=GREEN)
        z.poly(OTSU, color=GRAY, lw=2.0, fill=BLUE)
        z.free_text(centroid(KOU), '甲区画', fs=16, color=GRAY)
        z.free_text(centroid(OTSU), '乙区画', fs=16, color=GRAY)
    else:
        ax.set_title('分筆前の32番5を描く（正しい）', fontsize=18, color=RED, weight='bold', pad=6)
        z.poly(N4, color=GRAY, lw=1.0, ls=':')
        z.poly([A, H, B, E, G, F], lw=2.2)
        z.line(H, G, color=RED, lw=2.2)
        z.free_text(centroid(OTSU), '（イ）\n32－5', fs=16)
        z.callout(centroid(RO), '（ロ）', dirs=(40, 55, 25), color=RED, dists=(70, 90, 110))
        z.free_text(centroid(N4), '32番4は描かない', fs=14, color=GRAY)
        z.callout(H + (G - H) * 0.75, '分筆線 HG', dirs=(-30, -45, -15), color=RED, dists=(90, 110, 130))
    for p, n in [(A, 'A'), (B, 'B'), (E, 'E'), (F, 'F'), (G, 'G'), (H, 'H')]:
        z.point(p, 'dot')
        z.point_label(p, n, away=centroid(N5))
    zs.append(z)
ALL += save(fig, zs, 'R2_dai21mon_zu16_chiseki_hani.png')

# =====================================================================
# zu17：問4 地積測量図（32番5）の完成見本　※2026-10-08に、試験の答案用紙の第4欄の書式で描き直した
#   （../touan_youshi/R2_dai21mon_touan_youshi_p2.png：左上の「第4欄」、上の「地番」「土地の所在」の欄と「地積測量図」の表題、
#     図を描く枠と上下の折り目の印、下の「作成者（略）（令和2年○月○日作成）」「申請人（略）」「縮尺 1/250」は印刷済み）。
#   画像の中に図番は入れない
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 13), dpi=100)
fig.patch.set_facecolor('white')
FL = dict(transform=fig.transFigure, fill=False, edgecolor=BLACK)


def frect(x0, y0, x1, y1, lw=1.6):
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, lw=lw, **FL))


def fline(x0, y0, x1, y1, lw=1.4):
    fig.add_artist(plt.Line2D([x0, x1], [y0, y1], transform=fig.transFigure, color=BLACK, lw=lw))


SH = 0.215   # 答案用紙の枠の下端
frect(0.015, SH, 0.985, 0.99, lw=1.2)                       # 外枠（二重線）
frect(0.020, SH + 0.005, 0.980, 0.985, lw=2.2)
fig.text(0.03, 0.965, '第4欄', fontsize=17, weight='bold', va='center')
IL, IR, IT, IB = 0.085, 0.935, 0.905, 0.315                  # 図を描く枠
frect(IL, IB, IR, IT, lw=1.8)
fline(0.51, IT, 0.51, IT - 0.035)                            # 折り目の印（上・下）
fline(0.51, IB, 0.51, IB + 0.035)
frect(0.535, IT, 0.71, 0.955)                                # 地番の欄
fline(0.605, IT, 0.605, 0.955)
fig.text(0.570, 0.93, '地　　番', fontsize=15, ha='center', va='center')
fig.text(0.6575, 0.93, '32番5', fontsize=16, ha='center', va='center', weight='bold', color='#1a3a8f')
frect(0.535, IT - 0.045, IR, IT)                             # 土地の所在の欄
fline(0.605, IT - 0.045, 0.605, IT)
fig.text(0.570, IT - 0.0225, '土地の所在', fontsize=15, ha='center', va='center')
fig.text(0.625, IT - 0.0225, 'Ａ市Ｂ町一丁目', fontsize=16, ha='left', va='center', weight='bold', color='#1a3a8f')
fig.text(0.825, 0.93, '地　積　測　量　図', fontsize=19, ha='center', va='center')
BB, BT = IB - 0.065, IB                                      # 下の作成者・申請人・縮尺の欄
frect(IL, BB, 0.48, BT)
fline(0.135, BB, 0.135, BT)
fig.text(0.110, (BB + BT) / 2, '作 成 者', fontsize=14, ha='center', va='center')
fig.text(0.30, (BB + BT) / 2 + 0.01, '（略）', fontsize=14, ha='center', va='center')
fig.text(0.475, BB + 0.012, '（令和２年○月○日作成）', fontsize=13, ha='right', va='center')
frect(0.525, BB, IR, BT)
fline(0.575, BB, 0.575, BT)
fig.text(0.550, (BB + BT) / 2, '申 請 人', fontsize=14, ha='center', va='center')
fig.text(0.71, (BB + BT) / 2, '（略）', fontsize=14, ha='center', va='center')
fline(0.845, BB, 0.845, BT)
fline(0.875, BB, 0.875, BT)
fig.text(0.860, (BB + BT) / 2, '縮尺', fontsize=14, ha='center', va='center')
fline(0.885, BB + 0.01, 0.925, BT - 0.01, lw=1.0)
fig.text(0.892, BT - 0.016, '1', fontsize=13, ha='center', va='center')
fig.text(0.915, BB + 0.016, '250', fontsize=13, ha='center', va='center')
fig.text(0.5, 0.115,
         '印刷済み：「第4欄」「地積測量図」、地番・土地の所在の欄の枠、作成者と申請人の「（略）」、作成日の欄、縮尺 1/250（作成者・申請人・縮尺は書かない）\n'
         '書くもの：地番（32番5）、土地の所在（Ａ市Ｂ町一丁目）、図（縮尺1/250で 1m ＝ 4mm）、辺長7本、分筆線HG、（イ）32－5・（ロ）の符号、\n'
         '境界標の記号と凡例、「（単位：ｍ）」、方位記号（印刷されていないので必ず描く）、隣接地の地番、A市基準点1・2の位置と点名（問題文の注6）\n'
         '書かないもの：座標値・座標系の番号・地積と求積方法・測量年月日（問題文の注5）。辺長は小数第3位を四捨五入（HB は 2.6021… なので 2.60）',
         ha='center', va='center', fontsize=14, linespacing=1.6)
ax = fig.add_axes([IL + 0.01, IB + 0.01, IR - IL - 0.02, IT - IB - 0.065])
z = Zu(ax)
fit(ax, [A, B, E, F, G, H, K1, K2], margin=0.12, pad_aspect=True)
z.poly([A, H, B, E, G, F], lw=2.0)
z.line(H, G, lw=2.0)
z.north_arrow()
c5 = centroid(N5)
for n, (p, q, s) in SIDES.items():
    ref = c5 if n != 'HG' else centroid(OTSU)
    if n == 'BE':   # （ロ）の引き出し線が辺長の文字を横切らないよう、BEの辺長はB寄りに置く
        z.edge_label(p, q, s, ref, fs=16, ts=(0.28, 0.24, 0.32))
    else:
        z.edge_label(p, q, s, ref, fs=16, outward=(n != 'HG'))
z.free_text(centroid(OTSU) + P(-1.0, -1.0), '（イ）\n32－5', fs=17)
z.callout(centroid(RO) + (E - B) * 0.18, '（ロ）', dirs=(30, 45, 15), dists=(60, 80, 100), fs=16)
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
            ha='left', va='top', offsets=((0, 0), (0, -30), (20, 0), (0, 30)))
ALL += save(fig, [z], 'R2_dai21mon_zu17_chiseki_sokuryouzu.png')

print('重なりの合計:', len(ALL))
