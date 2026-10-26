"""令和6年度 第21問（土地）会話形式note記事の解説図28枚を、座標値から作図する。

`../prompt_R6_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../R7/Q21/zu/draw_R7_dai21mon_kaisetsuzu.py`。

実行: python3 note-articles-Kijyutsu/R6/Q21/zu/draw_R6_dai21mon_kaisetsuzu.py [出力フォルダ]

2026-10-26：最新の品質チェック（`qa-checklist-kijutsu.md` の6-2・6-3）で照らし直した。
- 旧版の12枚は、画像の中に作成時の図番（「図1」〜「図12」）が焼き込まれたままだった（照合スクリプトも図番を要求する逆向きの検査だった）。
  全図のタイトルから図番を消して描き直した。番号はPNG名（zu01〜zu28が記事の挿入順）・下のコメント・記事のマーカー・プロンプトの図の一覧の管理用だけ
- 誤答の会話の直後に専用の図がなかった論点に図を足して28枚にした：zu01 全体の時系列、zu04 観測角の向き、zu07 合意は筆界の根拠にならない、
  zu08 残地の地積測量図、zu09 A・B・Dは一直線、zu11 Cのまま分けると面積が増える、zu13 分筆するのは乙土地、zu14 地図訂正も地積更正も要らない、
  zu18 添付書類、zu19 登録免許税、zu20 土地の表示の行ごとの書き方、zu21 辺長の端数処理、zu22 書くもの・書かないもの、zu23 C点は描かない、
  zu25 地図は区画・準ずる図面は位置と形状、zu26 申出権者と職権、zu27 第5項第1号・第2号。旧zu09（問5の整理図）は zu25〜27 に分けた。zu15 は図形の重複（zu13と同じ形）をやめ、分筆→移転→合筆の流れ図に作り直した
- zu24 の地積測量図は、試験の答案用紙の第4欄（原本 `../touan_youshi/R6_dai21mon_touan_youshi.pdf` の2ページ目）の枠を get_drawings で測ったとおりに描き、
  枠の中に縮尺1/250（1m ＝ 4mm）の実際の大きさで描いた（実寸の図は細かいので、文字の余白の検査値だけ2pxにした）
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, to_dms, area, chiseki, intersect  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
INK = '#1a3a8f'      # 記入（濃い青）

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
T1, T2 = P(16.63, 61.67), P(26.91, 64.19)
A, C, E, F, G = P(25.09, 48.35), P(27.49, 60.92), P(35.40, 60.81), P(35.40, 50.15), P(33.82, 48.35)
H, I, J, K = P(21.83, 54.17), P(21.83, 60.90), P(19.83, 60.93), P(19.83, 48.35)
B = r2(radial(T2, T1, 10.03, dms(78, 58, 8)))
D = r2(radial(T2, T1, 4.60, dms(118, 24, 27)))
PP = r2(intersect(B, C, D, J)[0])          # P点（ブロック塀の線BCと道路境界DJの交点）

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('B', B, P(27.39, 54.17)), ('D', D, P(30.00, 60.78)), ('P', PP, P(27.49, 60.82))]:
    assert abs(got - want) < 1e-9, (n, got, want)
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'BP': (B, PP, '6.65'), 'PD': (PP, D, '2.51'), 'DB': (D, B, '7.11'), 'PI': (PP, I, '5.66'),
         'IH': (I, H, '6.73'), 'HB': (H, B, '5.56')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
for n, (p, q, want) in {'AB': (A, B, '6.26'), 'DJ': (D, J, '10.17')}.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
KOU = [A, B, D, E, F, G]            # 甲土地（2番1）の筆界
OTSU = [B, D, I, H]                 # 乙土地（3番1）の筆界（残地）
N32 = [A, K, J, I, H, B]            # 3番2
KOU_USE = [A, B, C, D, E, F, G]     # 甲土地の利用状況（ブロック塀 A→B→C）
OTSU_USE = [B, H, I, C]             # 乙土地の利用状況
I_31 = [B, PP, I, H]                # 分筆後の（イ）3番1
RO_33 = [B, D, PP]                  # 分筆後の（ロ）3番3
fl = lambda v: f'{chiseki(v):.2f}'  # noqa: E731  地積・比較用の面積（小数第2位未満切捨て）
AREAS = {'甲土地（筆界）': (KOU, '96.29'), '乙土地（筆界）': (OTSU, '45.86'), '甲土地（利用状況）': (KOU_USE, '104.76'),
         '乙土地（利用状況）': (OTSU_USE, '37.81'), '（イ）3番1': (I_31, '37.53'), '（ロ）3番3': (RO_33, '8.34'),
         '3番2': (N32, '50.79')}
for n, (pts, want) in AREAS.items():
    assert fl(area(pts)) == want, (n, fl(area(pts)), want)
assert f'{area([A, B, D]):.4f}' == '0.0064'
assert to_dms(cmath.phase(T1 - T2) + 2 * math.pi) == '193°46′25.18″'
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
BRG_T1 = math.degrees(cmath.phase(T1 - T2)) + 360          # T2→T1の方向角（北から時計回り）193.77°
BRG_B = BRG_T1 + 78 + 58 / 60 + 8 / 3600
BRG_D = BRG_T1 + 118 + 24 / 60 + 27 / 3600

# =====================================================================
# 図1：全体像（北を上にして座標どおりに描き直した調査図素図）
# =====================================================================
fig, (ax,) = new_figure('北を上にして描き直した全体像（令和6年10月の調査時点）',
                        'ブロック塀（A→B→C）と金属標Cは、測量によらず二人が合意した位置に設置したもの。\n'
                        '地図に準ずる図面では、甲土地と乙土地の境はAのあたりからDまで1本の直線（A→B→D）に描かれている。')
z = Zu(ax)
fit(ax, [A, G, F, E, D, J, K, T1, T2], margin=0.10, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.poly(N32, fill=ORANGE, alpha=0.15)
z.line(A, B, color=RED, lw=5.0)
z.line(B, C, color=RED, lw=5.0)
z.line(C, D, color=GRAY, lw=1.0, ls=':')
z.north_arrow()
cg, co, c32 = centroid(KOU), centroid(OTSU), centroid(N32)
z.free_text(cg, '甲土地\n2番1　宅地\n97.00㎡\n山田太郎', fs=16)
z.free_text(co + P(-1.2, 0.2), '乙土地\n3番1　宅地\n45.88㎡\n野原花子', fs=14)
z.free_text(P(20.9, 51.3), '3番2', fs=15)
for p, n, ref in [(A, 'A', cg), (B, 'B', cg), (D, 'D', co), (E, 'E', cg), (F, 'F', cg), (G, 'G', cg),
                  (H, 'H', c32), (I, 'I', c32), (J, 'J', c32), (K, 'K', c32)]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=ref)
z.point(C, 'metal', size=9)
z.point_label(C, 'C', away=cg)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.callout(A + (B - A) * 0.5, 'ブロック塀（A→B→C）', dirs=(-120, -140, -100), color=RED, dists=(70, 95, 120))
z.callout(B + (D - B) * 0.85, '地図に準ずる図面の境\n（A→B→Dの直線）', dirs=(25, 40, 10, -10), color=BLACK,
          dists=(90, 120, 150, 180))
z.edge_label(F, E, '2－2', cg, fs=15, dists=(22, 30), rotate=False)
z.edge_label(E, D, '1－1', cg, fs=15, dists=(26, 34), rotate=False)
z.edge_label(G, A, '5', cg, fs=15, dists=(22, 30), rotate=False)
z.edge_label(A, K, '5', c32, fs=15, dists=(22, 30), rotate=False)
z.edge_label(K, J, '道路', c32, fs=15, dists=(22, 30), rotate=False)
z.edge_label(I, J, '道路', c32, fs=15, dists=(28, 36), rotate=False, ts=(0.5, 0.3, 0.7))
z.edge_label(G, F, '道路', cg, fs=15, dists=(22, 30), rotate=False)
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu03_zentaizu.png')

# =====================================================================
# 図2：問2 B点（T2から放射）
# =====================================================================
fig, (ax,) = new_figure('問2　B点の求め方（T2から放射）',
                        'T2→T1の方向角 193°46′25.18″（電卓の表示は −166°13′34.82″）に、時計回りの観測角 78°58′08″ を足し、10.03m 進む。\n'
                        '観測角の向き（時計回りに足す理由）は別の図。\n'
                        '検算：BH＝5.56、AB＝6.26（昭和50年の地積測量図の辺長と一致）。')
z = Zu(ax)
fit(ax, [T1, T2, B, H, A, D, T2 + P(3.5, 0), P(24.0, 70.5)], margin=0.08, pad_aspect=True)
z.poly([A, B, D], color=GRAY, lw=1.1, closed=False)   # 甲土地は乙土地との境だけ（北側まで描くと端が切れる）
z.poly(OTSU, color=GRAY, lw=1.1)
z.poly(N32, color=GRAY, lw=1.1)
z.line(T2, T2 + 3.5, color=GRAY, lw=1.2, ls='--')
z.free_text(T2 + 3.5, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(T2, T1, color=BLUE, lw=2.0)
z.line(T2, B, color=RED, lw=2.6)
z.north_arrow()
z.angle_arc(T2, 1.6, 0, BRG_T1, color=BLUE)
z.angle_arc(T2, 2.6, BRG_T1, BRG_B, color=RED)
for p, kind in [(T1, 'kijun'), (T2, 'kijun'), (B, 'concrete'), (H, 'concrete'), (A, 'concrete')]:
    z.point(p, kind)
for p, n in [(H, 'H'), (A, 'A')]:
    z.point_label(p, n, away=centroid(N32))
z.edge_label(T2, T1, '後視（T1の方向）', T2 + P(0, -5), color=BLUE, fs=14, ts=(0.55, 0.65, 0.45), dists=(16, 22))
z.edge_label(T2, B, '10.03', T2 + P(-5, 0), color=RED, fs=17, ts=(0.62, 0.7, 0.55, 0.8), dists=(14, 20, 26))
z.edge_label(B, H, 'BH ＝ 5.56', centroid(OTSU), color=BLACK, fs=14, outward=False, dists=(16, 22))
z.edge_label(A, B, 'AB ＝ 6.26', centroid(N32), color=BLACK, fs=14, dists=(14, 20))
z.callout(T2 + P(0.3, 1.57), '方向角 193°46′25.18″\n（北から時計回りにT1の方向）', dirs=(110, 125, 95, 70, 140), color=BLUE,
          dists=(110, 140, 170, 200))
z.callout(T2 + P(-2.55, -0.5), '観測角 78°58′08″\n（T1の方向から時計回り）', dirs=(-110, -130, -90, -60), color=RED,
          dists=(60, 85, 110))
z.callout(B, 'B（27.39, 54.17）', dirs=(120, 100, 140, 160), color=RED)
z.callout(T2, 'T2（26.91, 64.19）', dirs=(10, -5, 25), color=BLACK, dists=(110, 140, 170))
z.callout(T1, 'T1（16.63, 61.67）', dirs=(0, -20, 20), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu05_B_housha.png')

# =====================================================================
# 図3：問2 D点（T2から放射）
# =====================================================================
fig, (ax,) = new_figure('問2　D点の求め方（T2から放射）',
                        'B点と同じ器械点T2・同じ後視T1。T2→T1の方向角 193°46′25.18″ に、時計回りの観測角 118°24′27″ を足し、4.60m 進む。\n'
                        '検算：DJ＝10.17（道路境界確認図のK1K2の10.17と一致。D＝K1、J＝K2）。')
z = Zu(ax)
fit(ax, [T1, T2, D, J, B, T2 + P(3.5, 0)], margin=0.08, pad_aspect=True)
z.poly([A, B, D], color=GRAY, lw=1.1, closed=False)   # 甲土地は乙土地との境だけ（北側まで描くと端が切れる）
z.poly(OTSU, color=GRAY, lw=1.1)
z.poly(N32, color=GRAY, lw=1.1)
z.line(T2, T2 + 3.5, color=GRAY, lw=1.2, ls='--')
z.free_text(T2 + 3.5, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(T2, T1, color=BLUE, lw=2.0)
z.line(T2, D, color=RED, lw=2.6)
z.north_arrow()
z.angle_arc(T2, 1.6, 0, BRG_T1, color=BLUE)
z.angle_arc(T2, 1.1, BRG_T1, BRG_D, color=RED)
for p, kind in [(T1, 'kijun'), (T2, 'kijun'), (D, 'concrete'), (J, 'concrete'), (B, 'concrete')]:
    z.point(p, kind)
for p, n in [(J, 'J'), (B, 'B')]:
    z.point_label(p, n, away=centroid(OTSU) if n == 'B' else centroid(N32))
z.edge_label(T2, T1, '後視（T1の方向）', T2 + P(0, -5), color=BLUE, fs=14, ts=(0.55, 0.65, 0.45), dists=(16, 22))
z.edge_label(T2, D, '4.60', T2 + P(0, 5), color=RED, fs=17, ts=(0.5, 0.62, 0.4), dists=(14, 20, 26))
z.edge_label(D, J, 'DJ ＝ 10.17', centroid(OTSU), color=BLACK, fs=14, ts=(0.5, 0.62, 0.38), dists=(16, 22, 30))
z.callout(T2 + P(-1.2, 1.03), '方向角 193°46′25.18″\n（北から時計回りにT1の方向）', dirs=(-20, -40, 0, -60), color=BLUE,
          dists=(90, 120, 150, 180))
z.callout(T2 + P(-0.9, -0.6), '観測角 118°24′27″\n（T1の方向から時計回り）', dirs=(-100, -120, -80, -60), color=RED,
          dists=(90, 120, 150))
z.callout(D, 'D（30.00, 60.78）', dirs=(120, 100, 140, 80), color=RED)
z.callout(T2, 'T2（26.91, 64.19）', dirs=(10, -5, 25), color=BLACK, dists=(120, 150, 180))
z.callout(T1, 'T1（16.63, 61.67）', dirs=(0, -20, 20), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu06_D_housha.png')

# =====================================================================
# 図4：問1（ア）筆界の判断（利用状況と地図に準ずる図面の比較）
# =====================================================================
fig, (ax1, ax2) = new_figure('問1（ア）　筆界はブロック塀ではなく、地図に準ずる図面の直線',
                             '左：ブロック塀（A→B→C）を境にすると、甲土地104.76㎡・乙土地37.81㎡で、登記記録の97.00㎡・45.88㎡と合わない。\n'
                             '右：地図に準ずる図面の直線（A→B→D。A・B・Dは一直線で△ABDは0.0064㎡）なら、甲土地96.29㎡・乙土地45.86㎡で合う。\n'
                             '残地の地積測量図が測っているのは3番2の周り（A・B・H・I・J・K）だけで、B→Dの長さは書かれていない。',
                             ncols=2)
zs = []
for ax, pk, po, sk, so, head, col in [
    (ax1, KOU_USE, OTSU_USE, '104.76㎡', '37.81㎡', '利用状況（ブロック塀 A→B→C）', GRAY),
    (ax2, KOU, OTSU, '96.29㎡', '45.86㎡', '地図に準ずる図面の形（A→B→D）', RED),
]:
    z = Zu(ax, fontsize=14)
    fit(ax, [A, G, F, E, D, J, K], margin=0.20, pad_aspect=True)
    z.poly(pk, fill=GREEN)
    z.poly(po, fill=BLUE)
    z.poly(N32, color=GRAY, lw=1.0)
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=18, color=col, weight='bold', pad=6)
    z.free_text(centroid(pk), f'甲土地\n{sk}', fs=16)
    z.callout(centroid(po), f'乙土地 {so}', dirs=(-60, -40, -80), color=BLACK, dists=(80, 100, 120))
    for p, n in [(A, 'A'), (B, 'B'), (D, 'D'), (H, 'H'), (I, 'I')]:
        z.point(p, 'concrete')
        z.point_label(p, n, away=centroid(pk) if n in 'AB' else centroid(N32))
    if pk is KOU_USE:
        z.point(C, 'metal', size=9)
        z.point_label(C, 'C', away=centroid(pk))
    zs.append(z)
zs[0].free_text(centroid(KOU_USE), '→ 登記記録の\n97.00㎡・45.88㎡と合わない', color=GRAY, fs=14,
                offsets=((0, 60), (0, 75), (0, -70), (0, -85), (-20, 60), (20, 60)))
zs[1].free_text(centroid(KOU), '→ 登記記録の\n97.00㎡・45.88㎡と合う', color=RED, fs=14,
                offsets=((0, 60), (0, 75), (0, -70), (0, -85), (-20, 60), (20, 60)))
ALL_PROBLEMS += save(fig, zs, 'R6_dai21mon_zu10_hikkai_handan.png')

# =====================================================================
# 図5：問2 P点（ブロック塀の線BCと道路境界DJの交点）
# =====================================================================
fig, (ax1, ax2) = new_figure('問2　P点の求め方（ブロック塀の線と道路境界の交点）',
                             'P ＝ B ＋ (C − B) × t、t ＝ 67.6152 ÷ 68.6625（Conjgの積のiの係数の比）。\n'
                             'C点の金属標は道路境界D→Jから道路側に0.10mはみ出していた。Cのまま分けると2筆の合計が46.28㎡になり、元の45.88㎡より増える。',
                             ncols=2, width_ratios=[1.3, 1])
za = Zu(ax1)
fit(ax1, [B, D, I, H, J, C, C + P(0, 3.5)], margin=0.12, pad_aspect=True)
za.poly(OTSU, fill=BLUE)
za.line(I, J, color=BLACK, lw=2.0)
za.line(B, C, color=RED, lw=4.0)
za.north_arrow()
for p, n in [(B, 'B'), (D, 'D'), (I, 'I'), (H, 'H'), (J, 'J')]:
    za.point(p, 'concrete')
    za.point_label(p, n, away=centroid(OTSU))
za.point(PP, 'dot', color=RED, size=9)
za.callout(PP, 'P（27.49, 60.82）', dirs=(-30, -10, -50), color=RED)
za.callout(B + (C - B) * 0.45, 'ブロック塀の線（B→C）', dirs=(-110, -130, -90), color=RED, dists=(60, 80, 100))
za.edge_label(D, J, '道路境界（D→J）', centroid(OTSU), fs=14, ts=(0.75, 0.85, 0.65), dists=(16, 24))

zb = Zu(ax2)
lo, hi = PP + P(-0.30, -0.35), PP + P(0.30, 0.35)
ax2.set_xlim(lo.imag, hi.imag)
ax2.set_ylim(lo.real, hi.real)
t_lo, t_hi = (lo.real - D.real) / (J.real - D.real), (hi.real - D.real) / (J.real - D.real)
zb.line(D + (J - D) * t_hi, D + (J - D) * t_lo, color=BLACK, lw=2.0)
zb.line(B + (C - B) * 0.955, C, color=RED, lw=4.0)
zb.north_arrow()
zb.point(C, 'metal', size=11)
zb.point(PP, 'dot', color=RED, size=11)
zb.callout(C, 'C（27.49, 60.92）\n移設前の金属標', dirs=(45, 30, 60, 20), color=GRAY, dists=(60, 80, 100))
zb.callout(PP, 'P（27.49, 60.82）', dirs=(-120, -140, -100), color=RED)
zb.edge_label(PP, C, '0.10', PP + P(-0.2, 0), color=RED, fs=17, dists=(14, 20), rotate=False)
zb.free_text(PP + P(-0.22, 0.22), '道路', fs=18, color=GRAY, offsets=((0, 0), (0, 10), (10, 0)))
zb.free_text(PP + P(-0.22, -0.2), '乙土地', fs=18, color=BLUE, offsets=((0, 0), (0, 10), (-10, 0)))
ax2.set_title('Pのまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'R6_dai21mon_zu12_P_kousa.png')

# =====================================================================
# 図7：問3 分筆後の区画と地番
# =====================================================================
fig, (ax,) = new_figure('問3　分筆後の区画と地番（3番1 → （イ）3番1 ＋ （ロ）3番3）',
                        '問題文の注8により、面積の小さい三角形B・D・P（8.34㎡）が（ロ）3番3、残る四角形B・P・I・H（37.53㎡）が（イ）3番1のまま。\n'
                        '切り捨て前の合計 8.34775 ＋ 37.5329 ＝ 45.88065 で登記記録の45.88㎡と一致。申請書の1行目の地積は登記記録の45.88（計算値の45.86ではない）。')
z = Zu(ax)
fit(ax, OTSU + [H + P(0, -2.5), D + P(1.6, 0)], margin=0.16, pad_aspect=True)
z.poly(I_31, fill=BLUE)
z.poly(RO_33, fill=PURPLE, alpha=0.30)
z.north_arrow()
z.free_text(centroid(I_31), '（イ）3番1\n37.53㎡', fs=18)
z.callout(centroid(RO_33), '（ロ）3番3　8.34㎡', dirs=(100, 80, 120), color=PURPLE, dists=(70, 90, 110))
for p, n in [(B, 'B'), (D, 'D'), (H, 'H'), (I, 'I')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=centroid(OTSU))
z.point(PP, 'metal', size=9)
z.point_label(PP, 'P', away=centroid(OTSU))
z.edge_label(B, D, '2番1（甲土地）', centroid(OTSU), fs=15, color=GRAY, dists=(34, 44), rotate=False,
             ts=(0.3, 0.2, 0.4))
z.edge_label(H, B, '3番2', centroid(OTSU), fs=15, color=GRAY, dists=(30, 40), rotate=False)
z.edge_label(I, H, '3番2', centroid(OTSU), fs=15, color=GRAY, dists=(26, 36), rotate=False)
z.edge_label(PP, I, '道路', centroid(OTSU), fs=15, color=GRAY, dists=(30, 40), rotate=False)
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu17_bunpitsu_chiban.png')

# =====================================================================
# 問4 地積測量図（3番1・3番3）の完成見本
#   試験の答案用紙の第4欄（原本 `../touan_youshi/R6_dai21mon_touan_youshi.pdf` の2ページ目。A3横）の枠・欄の位置と大きさを、
#   PDFの罫線からmmで測ったとおりに描く（2026-10-26）。縮尺1/250（1m ＝ 4mm）の実際の大きさで、枠の中に図を描く。
#   黒は印刷済み、青は書き込み。画像の中に図番は入れない
# =====================================================================
ORIG_FRAME_MM = (80.6, 25.8, 382.6, 256.8)     # 図を描く枠（x0, y0, x1, y1。原本の用紙の左上が原点）
ORIG_SHEET_MM = (56.3, 12.2, 406.9, 274.8)     # 用紙の外枠（二重線の外側）
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
ftext(59.0, 17.6, '第4欄', fs=15, ha='left', weight='bold')
frect(*ORIG_FRAME_MM, lw=1.8)                                  # 図を描く枠（横302mm・縦231mm）
fline(231.6, 25.8, 231.6, 35.8)                                # 折り目の印（上・下）
fline(231.6, 246.8, 231.6, 256.8)
frect(240.6, 15.8, 302.6, 25.8)                                # 地番の欄
fline(264.6, 15.8, 264.6, 25.8)
ftext(252.6, 20.8, '地　　番', fs=12)
ftext(283.6, 20.8, '3番1、3番3', fs=13, color=INK, weight='bold')
frect(240.6, 25.8, 382.6, 35.8)                                # 土地の所在の欄
fline(264.6, 25.8, 264.6, 35.8)
ftext(252.6, 30.8, '土地の所在', fs=12)
ftext(268.0, 30.8, 'Ａ市Ｂ町一丁目', fs=15, ha='left', color=INK, weight='bold')
ftext(342.6, 20.8, '地　積　測　量　図', fs=19)
frect(80.6, 256.8, 223.6, 271.3)                               # 作成者の欄
fline(99.6, 256.8, 99.6, 271.3)
ftext(90.1, 264.0, '作 成 者', fs=11)
ftext(161.6, 262.0, '（略）', fs=13)
ftext(221.0, 268.8, '（令和６年○月○日作成）', fs=11, ha='right')
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
         '書くもの：地番（3番1、3番3）、土地の所在（Ａ市Ｂ町一丁目）、辺長6本、（イ）（ロ）の符号と地番、境界標の記号、方位記号（印刷されていないので必ず描く）、\n'
         '隣接地の地番と道路、基準点T1・T2の位置と点名（問題文の注6）。書かないもの：座標値・座標系の番号・地積と求積方法・測量年月日（問題文の注5）。',
         ha='center', va='center', fontsize=13, linespacing=1.6)
ax = fig.add_axes([fx3(80.6), fy3(256.8), fx3(382.6) - fx3(80.6), fy3(25.8) - fy3(256.8)])
fw_m = (ORIG_FRAME_MM[2] - ORIG_FRAME_MM[0]) / 4               # 枠の中の東西（Y）の長さ（m）75.5
fh_m = (ORIG_FRAME_MM[3] - ORIG_FRAME_MM[1]) / 4               # 南北（X）57.75
c3 = P(23.3, 59.2)
fit(ax, [c3 + P(-fh_m / 2, -fw_m / 2), c3 + P(fh_m / 2, fw_m / 2)], margin=0.0, pad_aspect=True)
assert abs(((ax.get_xlim()[1] - ax.get_xlim()[0]) - fw_m)) < 0.05, ax.get_xlim()
z = Zu(ax, fontsize=10)
z.PAD = 2.0     # 実寸（1/250）の図は細かい。文字の周りの余白を2pxにして検査する（目視でも確認）
fit(ax, [c3 + P(-fh_m / 2, -fw_m / 2), c3 + P(fh_m / 2, fw_m / 2)], margin=0.0, pad_aspect=True)
z.poly([B, D, PP, I, H], lw=2.0)
z.line(B, PP, lw=2.0)
z.north_arrow()
co = centroid(OTSU)
for n, (p, q, s) in SIDES.items():
    if n == 'BP':
        z.edge_label(p, q, s, centroid(I_31), fs=10.5, outward=False)
    elif n == 'PD':
        z.edge_label(p, q, s, co, fs=10.5, dists=(24, 32), rotate=False)
    elif n == 'DB':
        z.edge_label(p, q, s, co, fs=10.5, dists=(22, 30, 38), ts=(0.2, 0.12, 0.3), rotate=False)
    else:
        z.edge_label(p, q, s, co, fs=10.5)
z.free_text(centroid(I_31), '（イ）\n3－1', fs=11.5)
z.free_text(P(28.1, 59.0), '（ロ）3－3', fs=7.5, offsets=((0, 0), (0, 1), (1, 0), (-1, 0), (0, -1)))
for p, n in [(B, 'B'), (D, 'D'), (H, 'H'), (I, 'I')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=co)
z.point(PP, 'metal', size=9)
z.point_label(PP, 'P', away=co)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.edge_label(D, B, '２－１', co, fs=10.5, dists=(40, 50), rotate=False, ts=(0.3, 0.2, 0.4))
z.free_text(D, '１－１', fs=10.5, offsets=((40, 28), (50, 20), (55, 35), (65, 42), (80, 30), (80, 48), (95, 38)))
z.edge_label(H, B, '３－２', co, fs=10.5, dists=(40, 50), rotate=False)
z.edge_label(I, H, '３－２', co, fs=10.5, dists=(36, 46), rotate=False)
z.edge_label(PP, I, '道路', co, fs=10.5, dists=(44, 54), rotate=False)
z.free_text(P(-3.0, 28.5), '（単位：ｍ）\n◎ コンクリート杭：B・D・H・I\n● 金属標：P\n△ 基準点：T1・T2', fs=9.5,
            ha='left', va='bottom', offsets=((0, 0), (0, 30), (30, 0)))
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu24_chiseki_sokuryouzu.png')

# =====================================================================
# 図10：問題文の注の仕分け（毎年同じ注と今年だけの注、調査図素図の注。整理図。固定配置）
# 2026-10-02追加（予備校の解説と見比べて記事に足した読み方の図）
# =====================================================================
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問題文の注の仕分け（毎年同じ注と、今年だけの注）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.14, 0.94, 0.76])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
COLS = [
    (1, '毎年ほぼ同じ決まり文句', GRAY,
     ['注1　行為は全て適法、書類も適法', '注2　書面申請', '注3　座標値は小数第3位を四捨五入',
      '注4　地積測量図は250分の1、\n　　　筆界点間の距離は小数第3位を四捨五入', '注9　答案用紙の字画・訂正の方法']),
    (34, '今年だけ①　地積測量図に書かないもの', BLUE,
     ['注5　座標値、平面直角座標系の番号又は記号、\n　　　地積及びその求積方法、測量年月日', '注6　A市基準点は位置と点名だけ\n　　　（座標値は書かない）']),
    (67, '今年だけ②　分筆後の地番', RED,
     ['注7　甲土地を分筆する場合は\n　　　面積の小さい土地を2番3', '注8　乙土地を分筆する場合は\n　　　面積の小さい土地を3番3',
      '→ 両方あるのは、どちらを分筆するかを\n　 迷わせるため（分筆するのは乙土地）']),
]
for x0, head, col, items in COLS:
    ax.add_patch(FancyBboxPatch((x0, 22), 31, 70, boxstyle='round,pad=0.5', fc='white', ec=col, lw=2.2))
    ax.text(x0 + 15.5, 88, head, ha='center', va='center', fontsize=16, color=col, weight='bold')
    for k, it in enumerate(items):
        ax.text(x0 + 1.5, 79 - k * 12.5, it, ha='left', va='top', fontsize=14, linespacing=1.4,
                color=RED if it.startswith('→') else BLACK)
ax.add_patch(FancyBboxPatch((1, 2), 97, 12, boxstyle='round,pad=0.5', fc='white', ec=PURPLE, lw=2.2))
ax.text(49.5, 8, '調査図素図の（注）：D点からJ点は直線であり、I点はその直線上にある（P点を求める直線D→Jの根拠）',
        ha='center', va='center', fontsize=15, color=PURPLE, weight='bold')
fig.text(0.5, 0.06, '問題文の注と調査図素図の（注）は別物なので、記事では「問題文の注7」「調査図素図の注」と言い分ける。', ha='center',
         va='center', fontsize=16)
path = os.path.join(OUT, 'R6_dai21mon_zu02_chuu_shiwake.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] zu02 注の仕分け: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図11：問3　四角形B・P・I・Hの面積を対角線で出す別解
# 2026-10-02追加（予備校の解説と見比べて記事に足した別解の図）
# =====================================================================
dd = (B - I).conjugate() * (PP - H)
assert f'{dd.real:.4f}' == '-13.2849' and f'{dd.imag:.4f}' == '75.0658'
assert abs(dd.imag / 2 - area(I_31)) < 1e-9
fig, (ax,) = new_figure('問3　四角形B・P・I・Hの面積を対角線で出す（別解）',
                        '倍面積 ＝ Conjg(B − I) × (P − H) のiの係数 75.0658（4点を順に回る式と同じ）。75.0658 ÷ 2 ＝ 37.5329 → （イ）37.53㎡\n'
                        '分筆後の地積の合計 37.53 ＋ 8.34 ＝ 45.87㎡。登記記録の45.88㎡との差 0.01㎡は、参考の甲2の公差（約0.51㎡）の範囲内。')
z = Zu(ax)
XD = intersect(B, I, PP, H)[0]                         # 対角線の交点
fit(ax, [B, D, PP, I, H, P(24.6, 50.2)], margin=0.12, pad_aspect=True)
z.poly(I_31, fill=BLUE)
z.poly(RO_33, fill=ORANGE)
z.line(B, I, color=RED, lw=2.2, ls='--')
z.line(PP, H, color=RED, lw=2.2, ls='--')
z.north_arrow()
for p_, n_ in [(B, 'B'), (D, 'D'), (PP, 'P'), (I, 'I'), (H, 'H')]:
    z.point(p_, 'dot')
    z.point_label(p_, n_, away=centroid([B, D, I, H]))
z.free_text(centroid([B, H, XD]), '（イ）3番1\n37.5329\n→ 37.53㎡', fs=14, offsets=((0, 0), (-10, 0), (-10, 10)))
z.callout(centroid(RO_33), '（ロ）3番3　8.34775 → 8.34㎡', dirs=(60, 40, 80, 20), color=ORANGE, dists=(70, 95, 120))
z.callout((B + I) / 2 + (I - B) * 0.18, '対角線 B − I', dirs=(-150, -130, -170), color=RED, dists=(70, 95))
z.callout(H + (PP - H) * 0.12, '対角線 P − H', dirs=(-150, -170, -130), color=RED, dists=(60, 90))
z.free_text(P(24.6, 51.6), 'Conjg(B − I) × (P − H)\n＝ −13.2849 ＋ 75.0658i', fs=15, color=RED,
            offsets=((0, 0), (0, -20), (20, 0), (-20, 0)))
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu16_taikakusen.png')

# =====================================================================
# 図12：本番で解く順番（P点と面積がいちばん重い）
# 2026-10-02追加
# =====================================================================
fig = plt.figure(figsize=(16, 8), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('本番で解く順番　P点と（イ）（ロ）の面積は後に回す', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
STEPS = [
    ('①', '問1と問5\n（計算なし）', '第1欄・第5欄', BLUE),
    ('②', 'B点・D点の\n放射', '第2欄 B・D', BLUE),
    ('③', '申請書の\n地積以外の欄', '第3欄\n（1行目の45.88も）', GREEN),
    ('④', 'P点の交点', '第2欄 P', RED),
    ('⑤', '（イ）（ロ）の\n面積', '第3欄の地積', RED),
    ('⑥', '地積測量図の\n辺長と作図', '第4欄', ORANGE),
]
w, h, gap = 14.2, 42, 2.2
for i, (no, t, ran, col) in enumerate(STEPS):
    x = 1 + i * (w + gap)
    ax.add_patch(FancyBboxPatch((x, 22), w, h, boxstyle='round,pad=0.4', facecolor=col, alpha=0.14, edgecolor=col,
                                lw=2))
    ax.text(x + w / 2, 22 + h - 3, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
    ax.text(x + w / 2, 22 + h / 2 - 4, t, ha='center', va='center', fontsize=17, linespacing=1.5)
    ax.text(x + w / 2, 17, ran, ha='center', va='top', fontsize=14, color=col, weight='bold', linespacing=1.4)
    if i < len(STEPS) - 1:
        ax.annotate('', xy=(x + w + gap - 0.3, 43), xytext=(x + w + 0.3, 43),
                    arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
ax.text(1 + 1.5 * (w + gap) - gap / 2, 76, 'P点がなくても書ける', ha='center', fontsize=15, color=GREEN, weight='bold')
ax.annotate('', xy=(1 + 3 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=GREEN))
ax.text(1 + 4 * (w + gap) - gap / 2, 76, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
ax.annotate('', xy=(1 + 5 * (w + gap) - gap, 72), xytext=(1 + 3 * (w + gap), 72),
            arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
fig.text(0.5, 0.09, '申請書は、登記の目的・添付書類・申請人・登録免許税・所在・1行目の45.88・（ロ）の地番と地目・2つの登記原因を先に書ける。\n'
         '途中で時間が切れても、書ける欄は全部埋まっているようにする。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R6_dai21mon_zu28_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] zu28 解く順番: 固定配置\n  →', path)


# =====================================================================
# 2026-10-26追加：品質チェック（qa-checklist-kijutsu.md 6-2・6-3）で照らし直した図。
#   画像の中に図番は入れない（番号はPNG名・このコメント・記事のマーカー・プロンプトの図の一覧の管理用だけ）。
#   zu01 全体の時系列、zu04 観測角の向き、zu07 合意は筆界の根拠にならない、zu08 残地の地積測量図、zu09 A・B・Dは一直線、
#   zu11 Cのまま分けると面積が増える、zu13 分筆するのは乙土地、zu14 地図訂正も地積更正も要らない、
#   zu18 添付書類、zu19 登録免許税、zu20 土地の表示の行ごとの書き方、zu21 辺長の端数処理、zu22 C点は描かない、
#   zu23 地積測量図に書くもの・書かないもの、zu25 地図は区画・準ずる図面は位置と形状、zu26 申出権者と職権、zu27 第5項第1号・第2号
# =====================================================================
import math as _m  # noqa: E402
setup_font()


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


def cell(ax, x, y, w, h, txt, fs=15, fc='white', ec=BLACK, color=BLACK, weight='normal', ha='center', lw=1.4, ls=1.4):
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, lw=lw))
    tx = x + w / 2 if ha == 'center' else x + 1.2
    ax.text(tx, y + h / 2, txt, ha=ha, va='center', fontsize=fs, color=color, weight=weight, linespacing=ls)


# ---- zu01：全体の時系列（第1章） ----
fig, ax = board(8)
ax.set_position([0.03, 0.14, 0.94, 0.76])
fig.suptitle('全体の時系列　合意した位置にブロック塀を作り、令和6年に形の違いに気づいた', fontsize=24, weight='bold', y=0.965)
EV = [  # (x, 日付, 出来事, 色, 上下)
    (9, '昭和50年', '3番を3番1・3番2に分筆\n（乙土地を残地とする\n地積測量図）', GRAY, 1),
    (31, '平成27年', '山田太郎が費用を出して\nブロック塀を設置\n（合意した位置。測量なし）', RED, -1),
    (55, '令和6年7月1日', '野原花子が地図に準ずる\n図面を見て、形が違うと\n気づく（山田太郎も確認）', BLUE, 1),
    (78, '令和6年10月18日', '法務一郎が\n登記を申請', BLUE, -1),
]
ax.annotate('', xy=(99, 50), xytext=(0.5, 50), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, d, t, col, ud in EV:
    ax.plot([x], [50], 'o', ms=13, color=col, zorder=5)
    ax.plot([x, x], [50, 50 + ud * 10], color=col, lw=1.4)
    ax.text(x, 50 + ud * 11, d, ha='center', va='bottom' if ud > 0 else 'top', fontsize=16, color=col, weight='bold')
    ax.text(x, 50 + ud * 20, t, ha='center', va='bottom' if ud > 0 else 'top', fontsize=14, color=BLACK, linespacing=1.5)
fig.text(0.5, 0.075, '山田太郎と野原花子の合意（聴取結果5）：利用状況に筆界を合致させて解決する。表示に関する登記は、手続が必要になる土地の所有者が行い、'
         'もう一方が協力する。\n'
         '調査・測量の結果（令和6年）：C点の金属標は道路との境界線上になかったため、同種の標を入れ直してP点とした。',
         ha='center', va='center', fontsize=15, linespacing=1.7)
put_board(fig, 'R6_dai21mon_zu01_jikeiretsu_zentai.png')

# =====================================================================
# zu04：観測角の向き（時計回りに足す。反時計回りだと道路の向こう）
# =====================================================================
Bw = r2(radial(T2, T1, 10.03, -dms(78, 58, 8)))
assert abs(Bw - P(22.70, 73.29)) < 1e-9, Bw
fig, (ax,) = new_figure('観測角の向きの注がないときは、後視の方向から時計回りに足す',
                        '求めた点が調査図素図の位置に出るかで確かめる。時計回りに足したBは（27.39, 54.17）で、乙土地の北西の角に合う。\n'
                        '反時計回りに引くと（22.70, 73.29）で、乙土地から東へ約19m、道路を越えた向こう側に出てしまう。')
z = Zu(ax)
fit(ax, [T1, T2, B, Bw, H, A, D, J, T2 + P(3.5, 0), P(14.0, 77.0), P(36.5, 66.0)], margin=0.06, pad_aspect=True)
z.poly([A, B, D], color=GRAY, lw=1.1, closed=False)
z.poly(OTSU, color=GRAY, lw=1.1)
z.poly(N32, color=GRAY, lw=1.1)
z.line(D, J, color=GRAY, lw=2.2)
z.line(T2, T2 + 3.5, color=GRAY, lw=1.2, ls='--')
z.free_text(T2 + 3.5, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(T2, T1, color=BLUE, lw=2.0)
z.line(T2, B, color=RED, lw=2.6)
z.line(T2, Bw, color=GRAY, lw=1.8, ls=':')
z.north_arrow()
z.angle_arc(T2, 1.6, 0, BRG_T1, color=BLUE)
z.angle_arc(T2, 2.6, BRG_T1, BRG_B, color=RED)
z.angle_arc(T2, 3.6, BRG_T1 - (78 + 58 / 60 + 8 / 3600), BRG_T1, color=GRAY, arrow=False)
for p, kind in [(T1, 'kijun'), (T2, 'kijun'), (B, 'concrete'), (H, 'concrete'), (A, 'concrete'), (D, 'concrete'), (J, 'concrete')]:
    z.point(p, kind)
z.point(Bw, 'dot', color=GRAY, size=9)
z.callout(B, 'B（27.39, 54.17）\n時計回りに足した点（正）', dirs=(130, 110, 150, 160), color=RED, dists=(70, 95, 120))
z.callout(Bw, 'B′（22.70, 73.29）\n反時計回りに78°58′08″引いた点（誤）', dirs=(-60, -90, -30, 20), color=GRAY, dists=(70, 95, 120))
z.callout(T2 + P(0.3, 1.57), '方向角 193°46′25.18″\n（北から時計回りにT1の方向）', dirs=(110, 125, 95, 70, 140), color=BLUE, dists=(110, 140, 170, 200))
z.callout(T2 + P(-2.55, -0.5), '観測角 78°58′08″\n（T1の方向から時計回り）', dirs=(-110, -130, -90, -60), color=RED, dists=(60, 85, 110))
z.free_text(P(18.6, 67.5), '道路', fs=16, color=GRAY, offsets=((0, 0), (0, 14), (14, 0)))
for p_, n_ in [(D, 'D'), (J, 'J')]:
    z.point_label(p_, n_, away=centroid(OTSU))
z.callout(T2, 'T2', dirs=(10, -5, 25), color=BLACK, dists=(110, 140))
z.callout(T1, 'T1', dirs=(0, -20, 20), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu04_kansokukaku_muki.png')

# ---- zu07：合意で置いたブロック塀・金属標は筆界の根拠にならない ----
fig, ax = board(9)
fig.suptitle('問1（ア）　ブロック塀と金属標Cは「合意した位置」。筆界の根拠にならない', fontsize=24, weight='bold', y=0.965)
FACTS = [('聴取結果6', '山田太郎が平成27年に費用を出してブロック塀を設置した（以前は同じ位置に生垣があった）'),
         ('聴取結果7', '塀は測量の結果に基づかず、二人が合意した位置に設置した。そのとき筆界の確認はしていなかった'),
         ('聴取結果8', 'C点の金属標も、測量の結果に基づかず、二人が合意した位置に設置したもの'),
         ('調査結果2(2)', '永続性があると確認されたのは「C点以外」の境界標（C点だけ永続性の確認がない）')]
for k, (a, b) in enumerate(FACTS):
    y = 78 - k * 16
    cell(ax, 3, y, 15, 12, a, fs=15, fc='#eeeeee', weight='bold')
    cell(ax, 18, y, 79, 12, b, fs=14, ha='left')
ax.annotate('', xy=(50, 8.5), xytext=(50, 13.5), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=RED))
ax.add_patch(plt.Rectangle((3, 0.5), 94, 9.5, facecolor='#fff5f5', edgecolor=RED, lw=2.2))
ax.text(50, 5.3, '二人が合意しても筆界そのものは動かない。選択肢1（現地の境界標・構造物）は誤り', ha='center', va='center',
        fontsize=18, color=RED, weight='bold')
put_board(fig, 'R6_dai21mon_zu07_goui_konkyo.png')

# ---- zu08：残地の地積測量図が測っているのは3番2の周りだけ ----
fig, (ax,) = new_figure('問1（ア）　乙土地を残地とする地積測量図が測ったのは「3番2」の周りだけ',
                        '昭和50年の分筆で、残地は乙土地（Ⓐ3-1）、新しくできたのが3番2（Ⓑ3-2）。三斜求積表に載っているのは地番Ⓑ3-2（50.79㎡）だけ。\n'
                        '辺長が書かれているのは3番2の周り（A・K・J・I・H・B）で、甲乙の境B→Dは線が引いてあっても長さがない（測っていない）。')
z = Zu(ax)
fit(ax, [A, K, J, I, H, B, D, G, F, E], margin=0.10, pad_aspect=True)
z.poly(N32, fill=ORANGE, alpha=0.20, lw=3.0)
z.poly(OTSU, color=GRAY, lw=1.2)
z.line(B, D, color=RED, lw=2.6, ls='--')
z.poly([A, G, F, E, D], color=GRAY, lw=1.0, closed=False)
z.north_arrow()
co, c32 = centroid(OTSU), centroid(N32)
z.free_text(P(24.6, 51.2), '3番2（Ⓑ）\n求積表あり\n50.79㎡', fs=14, offsets=((0, 0), (0, 12), (0, -12)))
z.free_text(co + P(0, 0), '乙土地（残地Ⓐ）\n3番1', fs=14, color=BLUE)
for p, n, ref in [(A, 'A', c32), (K, 'K', c32), (J, 'J', c32), (I, 'I', c32), (H, 'H', c32), (B, 'B', c32), (D, 'D', co)]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=ref)
for n, (p, q, s) in {'AB': (A, B, '6.26'), 'BH': (B, H, '5.56'), 'HI': (H, I, '6.73'), 'IJ': (I, J, '2.00'),
                     'JK': (J, K, '12.58'), 'KA': (K, A, '5.26')}.items():
    assert d2(p, q) == s, (n, d2(p, q))
    z.edge_label(p, q, s, c32, fs=15, color=BLACK, outward=False if n in ('AB', 'IJ') else True)
z.callout(B + (D - B) * 0.55, 'B→Dは長さの記載なし\n（測っていない）', dirs=(60, 40, 80), color=RED, dists=(70, 95, 120))
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu08_zanchi_sokuryouzu.png')

# ---- zu09：A・B・Dは一直線（三角形ABDの面積はほぼ0） ----
dd_abd = (B - A).conjugate() * (D - A)
assert f'{dd_abd.real:.4f}' == '83.6356' and f'{dd_abd.imag:.4f}' == '0.0128'
h_off = dd_abd.imag / abs(D - A)
fig, (ax1, ax2) = new_figure('問1（ア）　A・B・Dは一直線（三角形ABDの面積はほぼ0）',
                             '地図に準ずる図面の甲乙の境は西のAから東のDまで1本の直線。Bが直線ADの上にあるかを、三角形ABDの面積で確かめる。',
                             ncols=2, width_ratios=[1.25, 1])
z = Zu(ax1)
fit(ax1, [A, B, D, H, I], margin=0.14, pad_aspect=True)
z.poly(OTSU, color=GRAY, lw=1.0)
z.line(A, D, color=RED, lw=2.0, ls='--')
z.line(A, B, color=BLACK, lw=2.4)
z.line(B, D, color=BLACK, lw=2.4)
z.north_arrow(length=0.07)
for p, n in [(A, 'A'), (B, 'B'), (D, 'D')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=centroid(KOU))
z.callout(A + (D - A) * 0.35, '直線A→D', dirs=(-100, -120, -80), color=RED, dists=(70, 95))
ax2.axis('off')
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 100)
ax2.text(3, 94, '三角形ABDの倍面積', fontsize=18, weight='bold', va='top')
ax2.text(3, 84, 'Conjg(B − A) × (D − A)\n＝ 83.6356 ＋ 0.0128i', fontsize=17, va='top', color=RED, linespacing=1.6)
ax2.text(3, 62, '読むのは i の係数だけ（実部は使わない）\n面積 ＝ 0.0128 ÷ 2 ＝ 0.0064㎡', fontsize=16, va='top', linespacing=1.6)
ax2.text(3, 38, f'AからDまでは約{abs(D - A):.2f}m。\nBが直線ADから離れているのは\n0.0128 ÷ {abs(D - A):.2f} ＝ 約0.001m（約1mm）', fontsize=16,
         va='top', linespacing=1.6)
ax2.add_patch(plt.Rectangle((2, 2), 96, 15, facecolor='#fff5f5', edgecolor=RED, lw=2))
ax2.text(50, 9.5, 'ほぼ0 → A・B・Dは一直線　→　筆界はB→Dの直線', ha='center', va='center', fontsize=17, color=RED, weight='bold')
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu09_ichokusen_ABD.png')

# ---- zu11：Cのまま分けると面積が増える ----
C_KOU = [B, H, I, C]
C_RO = [B, C, D]
assert fl(area(C_KOU)) == '37.81' and fl(area(C_RO)) == '8.47', (fl(area(C_KOU)), fl(area(C_RO)))
fig, (ax1, ax2) = new_figure('問2　C点のまま分けると、道路を取り込んで面積が増える',
                             '左：Cは道路境界D→Jより0.10m道路側にはみ出している。B→H→I→Cが37.81㎡、B→C→Dが8.47㎡で、合計46.28㎡。\n'
                             '右：Pに入れ直すと37.53㎡と8.34㎡で、切り捨て前の合計45.88065㎡が登記記録の45.88㎡と合う。元の乙土地より増えることはない。',
                             ncols=2)
zs11 = []
for ax, parts, head, col, tot in [
        (ax1, [(C_KOU, '37.81㎡', BLUE), (C_RO, '8.47㎡', ORANGE)], 'Cのまま（誤）', GRAY, '合計 46.28㎡\n元の45.88㎡より0.40㎡増える'),
        (ax2, [(I_31, '37.53㎡', BLUE), (RO_33, '8.34㎡', ORANGE)], 'Pに入れ直す（正）', RED, '合計 45.87㎡\n切捨て前 45.88065 ＝ 登記記録45.88')]:
    z = Zu(ax, fontsize=14)
    fit(ax, [B, D, I, H, C, J, P(21.0, 66.5)], margin=0.12, pad_aspect=True)
    for pts, lab, c in parts:
        z.poly(pts, fill=c, alpha=0.25)
    z.line(D, J, color=BLACK, lw=2.2)
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=19, color=col, weight='bold', pad=6)
    for p, n in [(B, 'B'), (D, 'D'), (H, 'H'), (I, 'I')]:
        z.point(p, 'concrete')
        z.point_label(p, n, away=centroid(OTSU))
    z.free_text(centroid(parts[0][0]), parts[0][1], fs=17, color=BLUE, offsets=((0, 0), (0, 14)))
    z.free_text(centroid(parts[1][0]) + P(-0.4, -0.5), parts[1][1], fs=14, color=ORANGE, offsets=((0, 0), (0, 12), (0, -12)))
    z.free_text(P(19.4, 57.6), tot, fs=14, color=col, offsets=((0, 0), (0, -16), (0, 16)))
    if ax is ax1:
        z.point(C, 'metal', size=9)
        z.callout(C, 'C\n道路に0.10mはみ出し', dirs=(20, 0, 40), color=GRAY, dists=(60, 85, 110))
    else:
        z.point(PP, 'metal', size=9)
        z.callout(PP, 'P', dirs=(20, 0, 40), color=RED, dists=(50, 70))
    zs11.append(z)
ALL_PROBLEMS += save(fig, zs11, 'R6_dai21mon_zu11_C_mama_menseki.png')

# ---- zu13：分筆するのは乙土地、申請人は野原花子 ----
fig, (ax,) = new_figure('問1（イ）〜（エ）　三角形B・P・Dを切り離すには、乙土地を分筆する',
                        '筆界（A→B→D）の上では、三角形B・P・Dは乙土地（野原花子）。利用状況の境（A→B→P）で見ると、山田太郎が使っている。\n'
                        '甲土地は筆界どおりなら北側のA・B・D・E・F・G全部が山田太郎の土地で、分けるものがない。分筆の申請人は分筆する土地の所有者。\n'
                        '問題文の注7（甲土地を分筆する場合）は、注8（乙土地を分筆する場合）と対になったわな。')
z = Zu(ax)
fit(ax, [A, G, F, E, D, I, H], margin=0.14, pad_aspect=True)
z.poly(KOU, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.poly(RO_33, color=RED, lw=0, fill=RED, alpha=0.40, check=False)
z.line(B, PP, color=RED, lw=3.0, ls='--')
z.north_arrow()
z.free_text(centroid(KOU), '甲土地（2番1）\n山田太郎\n全部が山田太郎の土地\n→ 分けるものがない', fs=15)
z.free_text(centroid(I_31), '乙土地（3番1）\n野原花子', fs=15)
z.callout(centroid(RO_33), '三角形B・P・D\n筆界の上では乙土地\n→ 乙土地を分筆する\n（申請人は野原花子）', dirs=(-20, 0, -40, 20), color=RED, dists=(120, 150, 180))
for p, n in [(A, 'A'), (B, 'B'), (D, 'D'), (H, 'H'), (I, 'I'), (E, 'E'), (F, 'F'), (G, 'G')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=centroid(KOU) if n in 'EFGA' else centroid(OTSU))
z.point(PP, 'metal', size=9)
z.point_label(PP, 'P', away=centroid(OTSU))
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu13_bunpitsu_otsu.png')

# ---- zu14：（エ）地図訂正も地積更正も要らない ----
KOUSA_O = (0.05 + 0.01 * 45.88 ** 0.25) * _m.sqrt(45.88)
assert f'{KOUSA_O:.2f}' == '0.51'
fig, ax = board(9)
fig.suptitle('問1（エ）　要るのは分筆の登記だけ（地図訂正も地積更正も要らない）', fontsize=24, weight='bold', y=0.965)
CARDS = [(2, BLUE, 'ずれているのは何か', ['「筆界」と「利用状況」', '（ブロック塀の線）', '', '→ 筆界に利用状況を合わせる', '＝ 乙土地の分筆（6）']),
         (35, GREEN, '地図に準ずる図面は？', ['A・B・Dは一直線で、', '図面の形＝筆界そのもの', '', '→ 図面は正しい', '＝ 地図訂正は要らない']),
         (68, ORANGE, '地積は？', ['筆界どおりに測ると45.86㎡', '登記記録は45.88㎡、差0.02㎡', f'（参考：甲2の公差は約{KOUSA_O:.2f}㎡）', '→ 公差の範囲内', '＝ 地積更正は要らない'])]
for x, col, head, lines in CARDS:
    ax.add_patch(plt.Rectangle((x, 24), 30, 64, facecolor='white', edgecolor=col, lw=2.4))
    ax.text(x + 15, 83, head, ha='center', va='center', fontsize=18, color=col, weight='bold')
    for k, s in enumerate(lines):
        ax.text(x + 15, 72 - k * 9.5, s, ha='center', va='center', fontsize=14.5,
                color=RED if s.startswith('→') or s.startswith('＝') else BLACK, weight='bold' if s.startswith('＝') else 'normal')
ax.add_patch(plt.Rectangle((2, 4), 96, 14, facecolor='#fff5f5', edgecolor=RED, lw=2.2))
ax.text(50, 11, '（エ）は 6（分筆の登記の申請）。選択肢7「地積に関する更正の登記の申請及び地図訂正の申出」は誤り', ha='center', va='center',
        fontsize=17, color=RED, weight='bold')
put_board(fig, 'R6_dai21mon_zu14_chizu_teisei_fuyou.png')

# ---- zu18：添付書類 ----
fig, ax = board(8)
fig.suptitle('問3　添付書類は「何の登記か」と「申請の日の登記記録」で決まる', fontsize=24, weight='bold', y=0.965)
ROWS = [('○', '地積測量図', '分筆後の土地を表示した図面（不動産登記令別表8の項）', GREEN),
        ('○', '代理権限証書', '土地家屋調査士の法務一郎が代理人として申請する（代理人の欄は「（略）」）', GREEN),
        ('×', '抵当権者などの承諾書', '甲土地・乙土地とも乙区は「登記事項なし」。権利者がいないので承諾は要らない', RED),
        ('×', '登記識別情報・印鑑証明書', '分筆の登記だけを申請する（合筆の登記を申請するときに付けるもの）', RED)]
for k, (mark, name, why, col) in enumerate(ROWS):
    y = 76 - k * 17.5
    fc = '#e8f5ea' if col == GREEN else '#fbeeee'
    cell(ax, 3, y, 6, 14, mark, fs=26, fc=fc, ec=col, color=col, weight='bold', lw=2)
    cell(ax, 9, y, 27, 14, name, fs=16, fc=fc, ec=col, weight='bold', lw=2)
    cell(ax, 36, y, 61, 14, why, fs=13, fc='white', ec=col, ha='left', lw=2)
ax.text(50, 2, '答案用紙の「添付書類」の欄に書くのは「地積測量図　代理権限証書」の2つだけ', ha='center', va='center', fontsize=18, color=BLUE,
        weight='bold')
put_board(fig, 'R6_dai21mon_zu18_tenpu_shorui.png')

# ---- zu19：登録免許税は分筆後の個数で数える（「不要」とは書かない） ----
fig, ax = board(8)
fig.suptitle('問3　登録免許税は「分筆後の土地の個数」で数える　「不要」とは書かない', fontsize=24, weight='bold', y=0.965)
for x0, col, head2, boxes, calc, mk in [
        (2, GREEN, '正しい：分筆後の2個', [('（イ）3番1', GREEN), ('（ロ）3番3', GREEN)], '1,000円 × 2個 ＝ 金2,000円', '○'),
        (35, RED, '誤り：「不要」と書く', [('（イ）3番1', GRAY), ('（ロ）3番3', GRAY)], '分筆の登記は課税される\n問題文の「納付を要しない場合は不要」は\nこの申請には当たらない', '×'),
        (68, RED, '誤り：新しい土地だけ', [('（イ）3番1', GRAY), ('（ロ）3番3', RED)], '1,000円 × 1個 ＝ 金1,000円\n元の3番1も分筆後の土地に数える', '×')]:
    ax.add_patch(plt.Rectangle((x0, 12), 30, 72, facecolor='white', edgecolor=col, lw=2.4))
    ax.text(x0 + 15, 80, head2, ha='center', va='center', fontsize=17, color=col, weight='bold')
    for j, (t, c2) in enumerate(boxes):
        cell(ax, x0 + 2 + j * 14, 50, 12.5, 18, t, fs=12.5, fc='#f3f3f3', ec=c2, color=c2, weight='bold', lw=2.2)
    ax.text(x0 + 15, 33, calc, ha='center', va='center', fontsize=14, color=col, weight='bold', linespacing=1.6)
    ax.text(x0 + 15, 19, mk, ha='center', va='center', fontsize=30, color=col, weight='bold')
ax.text(50, 6, '登録免許税法別表第一の一（十三）イ：分筆後の不動産の個数 ×（1個につき千円）', ha='center', va='center', fontsize=15)
put_board(fig, 'R6_dai21mon_zu19_tourokumenkyozei.png')

# ---- zu20：土地の表示の行ごとの書き方 ----
fig, ax = board(9)
fig.suptitle('問3　土地の表示の欄は「行ごと」に書くものが違う', fontsize=24, weight='bold', y=0.965)
cx = [3, 24, 35, 50, 62]
cw2 = [21, 11, 15, 12, 35]
for x, w, t in zip([cx[0], cx[1], cx[2], cx[4]], [cw2[0], cw2[1], cw2[2] + cw2[3], cw2[4]],
                   ['①地番', '②地目', '③地積（m²）', '登記原因及びその日付']):
    cell(ax, x, 80, w, 7, t, fs=13, fc='#eeeeee')
ax.text(4, 91, '所在：Ａ市Ｂ町一丁目', fontsize=14, ha='left', va='center', color=INK, weight='bold')
LINES = [('1行目', '3番１', '宅地', '45.88', '（空欄）'),
         ('2行目', '（イ）', '（空欄）', '37.53', '③3番１、3番３に分筆'),
         ('3行目', '（ロ）3番３', '宅地', '8.34', '3番１から分筆')]
NOTES = ['（分筆前）地積は登記記録の45.88。計算した45.86ではない。原因は書かない',
         '（イ）は3番1のまま。地番の欄は「（イ）」だけ、地目も空欄。地積が変わったので原因に③を付ける',
         '（ロ）は新しい地番3番3と地目を書き、原因は「3番1から分筆」']
for k, ((nm, a, b, c, d), note) in enumerate(zip(LINES, NOTES)):
    y = 66 - k * 24
    cell(ax, cx[0], y, cw2[0], 10, a, fs=15, color=INK)
    cell(ax, cx[1], y, cw2[1], 10, b, fs=15, color=INK)
    cell(ax, cx[2], y, cw2[2] + cw2[3], 10, c, fs=15, color=INK)
    cell(ax, cx[4], y, cw2[4], 10, d, fs=14, color=INK)
    ax.text(3, y - 4.5, f'{nm}：{note}', fontsize=13, ha='left', va='center', color=RED)
ax.text(50, 3, '地積の欄は分筆後の2行（（イ）（ロ））も書く。答案用紙に「（略）」は印刷されていない', ha='center', va='center', fontsize=14, color=GRAY)
put_board(fig, 'R6_dai21mon_zu20_tochi_hyouji_gyou.png')

# ---- zu21：辺長の端数処理（小数第3位だけを見る。二度丸めない） ----
fig, ax = board(9)
fig.suptitle('問4　辺長は小数第3位を四捨五入（問題文の注4）　見るのは第3位だけ', fontsize=24, weight='bold', y=0.965)
head = ['辺', '計算した長さ', '小数第3位', '答え（小数第2位まで）']
xs, ws = [3, 11, 32, 49], [8, 21, 17, 22]
for x, w, t in zip(xs, ws, head):
    cell(ax, x, 80, w, 8, t, fs=13, fc='#eeeeee', weight='bold')
for r, (n, (p, q, want)) in enumerate(SIDES.items()):
    raw = abs(q - p)
    d3 = int(_m.floor(raw * 1000 + 1e-9)) % 10
    assert d2(p, q) == want
    rawtxt = f'{raw:.2f}' if abs(raw - round(raw, 2)) < 1e-9 else f'{_m.floor(raw * 10000 + 1e-9) / 10000:.4f}…'
    y = 72 - r * 8
    bad = (n == 'DB')
    fc = '#fbe3e3' if bad else 'white'
    col = RED if bad else BLACK
    cell(ax, xs[0], y, ws[0], 8, n, fs=15, fc=fc, color=col, weight='bold' if bad else 'normal')
    cell(ax, xs[1], y, ws[1], 8, rawtxt, fs=15, fc=fc, color=col)
    cell(ax, xs[2], y, ws[2], 8, f'{d3}（{"切り上げ" if d3 >= 5 else "切り捨て"}）', fs=14, fc=fc, color=col)
    cell(ax, xs[3], y, ws[3], 8, want, fs=16, fc=fc, color=col, weight='bold')
ax.add_patch(plt.Rectangle((74, 24), 24, 64, facecolor='#fff5f5', edgecolor=RED, lw=2))
ax.text(86, 85, '落とし穴', ha='center', va='top', fontsize=16, color=RED, weight='bold')
ax.text(86, 76, '第4位まで見て\n7.1066 → 7.107 → 7.11\n5.6605 → 5.661 → 5.66\nと二度丸めるのは誤り\n\n第3位だけを見て\n一度で決める', ha='center', va='top', fontsize=12.5,
        color=RED, linespacing=1.7)
ax.text(3, 10, '丸めるのは1回だけ。第3位が5以上なら切り上げ、4以下なら切り捨て（DBだけ切り上げ）。IH・HBは割り切れる。\n'
        'BP・PD・PIは第3位が0なので、第4位の数字は結果に関係しない。', fontsize=14, ha='left', va='center', linespacing=1.7)
put_board(fig, 'R6_dai21mon_zu21_hensuu_hasuu.png')

# ---- zu22：地積測量図にC点は描かない ----
fig, (ax1, ax2) = new_figure('問4　地積測量図にC点は描かない（描くのは分筆後の2筆の周りの点）',
                             '金属標はCからPに入れ直した。C点を描くと、道路にはみ出した移設前の図になってしまう。',
                             ncols=2, width_ratios=[1.15, 1])
z = Zu(ax1)
fit(ax1, OTSU + [T1, T2], margin=0.14, pad_aspect=True)
z.poly([B, D, PP, I, H], lw=2.2)
z.line(B, PP, lw=2.2)
z.north_arrow(length=0.07)
co = centroid(OTSU)
for p, n in [(B, 'B'), (D, 'D'), (H, 'H'), (I, 'I')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=co)
z.point(PP, 'metal', size=9)
z.point_label(PP, 'P', away=co, dists=(16, 22, 30))
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.callout(PP, 'Pを描く（金属標）', dirs=(-30, -10, -50), color=BLACK, dists=(80, 110, 140))
ax1.set_title('描く点：B・D・H・I（杭）とP（金属標）', fontsize=16, weight='bold', pad=6)
ax2.axis('off')
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 100)
ax2.text(3, 94, 'C点を描かない理由', fontsize=19, weight='bold', va='top', color=RED)
ax2.text(3, 82, '① 金属標は道路境界の線上になかったので、\n　　Pに入れ直した（調査結果2(3)ウ）', fontsize=15, va='top', linespacing=1.6)
ax2.text(3, 60, '② Cは分筆後の乙土地の筆界点でもない\n　　（（イ）はB・P・I・H、（ロ）はB・D・P）', fontsize=15, va='top', linespacing=1.6)
ax2.text(3, 38, '③ Cを描くと、道路に0.10mはみ出した\n　　移設前の図になる', fontsize=15, va='top', linespacing=1.6)
ax2.add_patch(plt.Rectangle((2, 4), 96, 18, facecolor='#fff5f5', edgecolor=RED, lw=2))
ax2.text(50, 13, 'C・P間は0.10m。250分の1では0.4mm\n図の上ではほぼ重なるから、混ぜないこと', ha='center', va='center', fontsize=15, color=RED, weight='bold', linespacing=1.6)
ALL_PROBLEMS += save(fig, [z], 'R6_dai21mon_zu23_C_kakanai.png')

# ---- zu23：地積測量図に書くもの・書かないもの ----
fig, ax = board(9)
fig.suptitle('問4　地積測量図に「書くもの」「書かないもの」「印刷済みのもの」', fontsize=24, weight='bold', y=0.965)
COLS3 = [(2, GREEN, '書くもの',
          ['各辺の長さ（6本）', '分筆線B→P', '地番：（イ）3－1・（ロ）3－3', '方位（印刷されていない）', '隣接地の地番\n（2－1・1－1・3－2）と道路',
           '境界標の記号\n（B・D・H・Iは杭、Pは金属標）', '基準点T1・T2の位置と点名']),
         (35, RED, '書かないもの',
          ['各筆界点の座標値', '平面直角座標系の番号又は記号', '地積及びその求積方法', '測量年月日（以上は問題文の注5）',
           'T1・T2の座標値（問題文の注6）', 'C点（移設前の金属標）']),
         (68, GRAY, '印刷済みなので書かない',
          ['作成者の欄の「（略）」', '申請人の欄の「（略）」', '縮尺 250分の1', '作成日の欄の印刷'])]
for x, col, head, items in COLS3:
    ax.add_patch(plt.Rectangle((x, 6), 30, 82, facecolor='white', edgecolor=col, lw=2.4))
    ax.text(x + 15, 83, head, ha='center', va='center', fontsize=18, color=col, weight='bold')
    yy = 74
    for it in items:
        ax.text(x + 1.5, yy, '・' + it, ha='left', va='top', fontsize=13.5, linespacing=1.4)
        yy -= 7.5 + 4.2 * it.count('\n')
put_board(fig, 'R6_dai21mon_zu22_kaku_kakanai.png')

# ---- zu25：地図は「区画」、地図に準ずる図面は「位置・形状」 ----
fig, ax = board(8)
fig.suptitle('問5（ア）　地図は「区画」、地図に準ずる図面は「位置・形状」　（ア）は地番', fontsize=24, weight='bold', y=0.965)
for x0, col, head2, lines in [
        (3, GRAY, '地図（不動産登記法第14条第1項）', ['訂正の申出ができる誤り：', '土地の 区画 又は 地番']),
        (52, RED, '地図に準ずる図面', ['訂正の申出ができる誤り：', '土地の 位置、形状 又は 地番'])]:
    ax.add_patch(plt.Rectangle((x0, 30), 45, 55, facecolor='white', edgecolor=col, lw=2.4))
    ax.text(x0 + 22.5, 79, head2, ha='center', va='center', fontsize=18, color=col, weight='bold')
    ax.text(x0 + 22.5, 62, lines[0], ha='center', va='center', fontsize=16)
    ax.text(x0 + 22.5, 48, lines[1], ha='center', va='center', fontsize=22, color=col, weight='bold')
ax.text(74.5, 36, '問題文：「位置、形状又は（ア）」→ （ア）＝ 地番', ha='center', va='center', fontsize=16, color=RED, weight='bold')
ax.add_patch(plt.Rectangle((3, 4), 94, 16, facecolor='#fff5f5', edgecolor=RED, lw=2.2))
ax.text(50, 12, '「区画」と答えるのは地図の言い方の混ぜ合わせ。位置と形状はすでに問題文にあるので、残るのは地番', ha='center', va='center', fontsize=16, color=RED,
        weight='bold')
put_board(fig, 'R6_dai21mon_zu25_chizu_kubun.png')

# ---- zu26：申出権者と、権限のない者からの申出の扱い ----
fig, ax = board(9)
fig.suptitle('問5①・（イ）　申出ができる者と、権限のない者の申出の扱い', fontsize=24, weight='bold', y=0.965)
ax.add_patch(plt.Rectangle((3, 62), 94, 26, facecolor='#f7f7f7', edgecolor=BLACK, lw=1.6))
ax.text(5, 84, '①　申出ができる者（不動産登記規則第16条第1項）', fontsize=18, weight='bold', va='center')
ax.text(8, 74, '土地の表題部所有者若しくは所有権の登記名義人\n又はこれらの相続人その他の一般承継人', fontsize=17, va='center', color=RED, linespacing=1.5)
ax.add_patch(plt.Rectangle((3, 4), 94, 52, facecolor='#f7f7f7', edgecolor=BLACK, lw=1.6))
ax.text(5, 52, '（イ）　申出をする権限のない者から申出があったとき', fontsize=18, weight='bold', va='center')
cell(ax, 8, 28, 40, 16, '訂正の申出の趣旨であるとき', fs=15, fc='white', weight='bold')
cell(ax, 52, 28, 40, 16, 'そうでないとき', fs=15, fc='white', weight='bold')
ax.annotate('', xy=(28, 20), xytext=(28, 27.5), arrowprops=dict(arrowstyle='-|>', lw=2, color=BLACK))
ax.annotate('', xy=(72, 20), xytext=(72, 27.5), arrowprops=dict(arrowstyle='-|>', lw=2, color=RED))
cell(ax, 8, 8, 40, 11.5, '却下する（第13項第2号）', fs=15, fc='white')
cell(ax, 52, 8, 40, 11.5, '登記官の 職権 （イ）の発動を促す\n申出として扱える（第15項）', fs=14.5, fc='#fff5f5', ec=RED, color=RED, weight='bold', ls=1.5)
put_board(fig, 'R6_dai21mon_zu26_shokken_shuttai.png')

# ---- zu27：併せて提供する情報（第5項の第1号と第2号） ----
fig, ax = board(8)
fig.suptitle('問5（ウ）　併せて提供する情報は、第5項の第1号と第2号', fontsize=24, weight='bold', y=0.965)
for x0, col, head2, body in [
        (3, GRAY, '第1号（どの訂正の申出にも付ける）', '誤りがあることを証する情報'),
        (52, RED, '第2号（位置又は形状に誤りがあるとき）', '土地所在図又は地積測量図　（ウ）')]:
    ax.add_patch(plt.Rectangle((x0, 38), 45, 46, facecolor='white', edgecolor=col, lw=2.4))
    ax.text(x0 + 22.5, 76, head2, ha='center', va='center', fontsize=16, color=col, weight='bold')
    ax.text(x0 + 22.5, 56, body, ha='center', va='center', fontsize=20, color=col, weight='bold')
ax.text(50, 30, '問題文：「位置又は形状に誤りがある場合には、地図訂正申出情報と併せて（ウ）を提供する」', ha='center', va='center', fontsize=16)
ax.add_patch(plt.Rectangle((3, 4), 94, 18, facecolor='#fff5f5', edgecolor=RED, lw=2.2))
ax.text(50, 13, '場合を絞っている文なので、答えは第2号の「土地所在図又は地積測量図」。第1号は両方とも必要だが、ここでは問われていない', ha='center', va='center',
        fontsize=15.5, color=RED, weight='bold')
put_board(fig, 'R6_dai21mon_zu27_dai5kou_gou.png')

# ---- zu15：分筆した三角形を山田太郎へ移し、2番1と合筆する流れ（今回の申請は①だけ） ----
fig, ax = board(8)
fig.suptitle('問1（イ）〜（エ）　分筆した三角形は、山田太郎へ移してから2番1と合筆する', fontsize=24, weight='bold', y=0.965)
FLOW = [(2, BLUE, '①　乙土地を分筆する', '表示に関する登記', '申請人：野原花子\n（今回の申請。問3）'),
        (35, ORANGE, '②　三角形B・D・Pを\n　　山田太郎へ移す', '権利に関する登記', '所有権の移転の登記\n（野原花子 → 山田太郎）'),
        (68, GREEN, '③　山田太郎の2番1と\n　　合筆する', '表示に関する登記', '所有者が同じになってから\nできる（法第41条第3号）')]
for x, col, head2, kind, note in FLOW:
    ax.add_patch(plt.Rectangle((x, 28), 30, 52, facecolor='white', edgecolor=col, lw=2.6))
    ax.text(x + 15, 72, head2, ha='center', va='center', fontsize=17, color=col, weight='bold', linespacing=1.5)
    ax.text(x + 15, 52, kind, ha='center', va='center', fontsize=15, color=BLACK)
    ax.text(x + 15, 38, note, ha='center', va='center', fontsize=14, color=BLACK, linespacing=1.6)
for x in (32.3, 65.3):
    ax.annotate('', xy=(x + 2.4, 54), xytext=(x - 0.3, 54), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=GRAY))
ax.add_patch(plt.Rectangle((2, 4), 96, 14, facecolor='#fff5f5', edgecolor=RED, lw=2.2))
ax.text(50, 11, '今回の申請（10月18日）は①だけ。持ち主が違う土地どうしは合筆できないので、②の後に③の順番になる', ha='center', va='center',
        fontsize=16, color=RED, weight='bold')
ax.text(50, 92, '聴取結果5：二人は、表示に関する登記手続・権利に関する登記手続が必要になった場合には、お互いに協力してその手続をすることも合意した。',
        ha='center', va='center', fontsize=14)
put_board(fig, 'R6_dai21mon_zu15_hitsuyou_touki.png')

print('重なりの合計:', len(ALL_PROBLEMS))
