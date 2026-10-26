"""令和3年度 第21問（土地）会話形式note記事の解説図26枚を、座標値から作図する。

`../prompt_R3_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。

2026-10-26：qa-checklist（6-2・6-3）で作り直した。画像の中の図番を消し、わな・計算過程の図を足して26枚（記事の挿入順にzu01〜zu26）。
地積測量図（zu25）は答案用紙の原本の第4欄の枠（横302mm・縦231mm）の中に縮尺1/250の実際の大きさで描く。

実行: python3 note-articles-Kijyutsu/R3/Q21/zu/draw_R3_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, area, chiseki, intersect  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402
import math  # noqa: E402,F401

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
T1, T2 = P(500.00, 500.00), P(496.77, 531.50)
B, D, E, F = P(498.29, 524.15), P(511.93, 530.00), P(504.63, 500.56), P(518.95, 505.48)
G, I, J, K = P(497.74, 526.20), P(502.14, 509.77), P(516.61, 513.65), P(499.94, 517.99)
A = r2(radial(T1, T2, 7.37, dms(227, 43, 36)))
Aw = r2(T1 + cmath.rect(7.37, cmath.phase(T2 - T1) - dms(227, 43, 36)))    # 反時計回りに測った誤り
C = r2(G + (D - G) / abs(D - G) * abs(B - G))
Cw = r2(G + (D - G) / abs(D - G) * 3.00)                                   # 隅切長3.00で進めた誤り
H = r2(intersect(F, E, A, B)[0])
L = r2(intersect(F, D, K, K + (J - I))[0])
Lw = r2(J + (K - I))                                                        # 平行四辺形と思い込んだ誤り


def dist_line(p, a, b):
    return abs(((b - a).conjugate() * (p - a)).imag) / abs(b - a)


# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
EXPECT = {'A': (A, P(505.93, 495.62)), 'C': (C, P(499.79, 526.75)), 'H': (H, P(504.61, 500.55)),
          'L': (L, P(514.27, 521.83)), 'Aw': (Aw, P(495.08, 494.51)), 'Cw': (Cw, P(500.64, 526.98)),
          'Lw': (Lw, P(514.41, 521.87))}
for n, (got, want) in EXPECT.items():
    assert abs(got - want) < 1e-9, (n, got, want)
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = {'HI': (H, I, '9.55'), 'IK': (I, K, '8.51'), 'KB': (K, B, '6.38'), 'BC': (B, C, '3.00'),
         'CD': (C, D, '12.57'), 'DL': (D, L, '8.50'), 'LJ': (L, J, '8.51'), 'JF': (J, F, '8.50'),
         'FH': (F, H, '15.16'), 'IJ': (I, J, '14.98'), 'KL': (K, L, '14.84')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert d2(B, G) == '2.12' and d2(B, Cw) == '3.68' and d2(E, F) == '15.14' and d2(E, H) == '0.02'
assert f'{dist_line(H, A, F):.2f}' == '4.73' and f'{dist_line(E, A, F):.2f}' == '4.72'
assert f'{dist_line(Lw, F, D):.2f}' == '0.15' and dist_line(Aw, I, B) > 10
assert Lw.real > F.real + (D.real - F.real) * (Lw.imag - F.imag) / (D.imag - F.imag)   # 誤りのLは筆界FDの北側
HEI, OTSU, KOU = [H, I, J, F], [I, K, L, J], [B, C, D, L, K]
ZEN = [H, B, C, D, F]
AREAS = {'丙': (HEI, 135.8455, 135.84), '乙': (OTSU, 126.8422, 126.84), '甲': (KOU, 123.2128, 123.21),
         '全体': (ZEN, 385.8952, 385.89)}
for n, (pts, raw, chi) in AREAS.items():
    assert abs(area(pts) - raw) < 5e-5 and chiseki(area(pts)) == chi, (n, area(pts))
assert abs(135.84 + 126.84 + 123.21 - 385.89) < 1e-9 and abs(386.30 - 385.89 - 0.41) < 1e-9
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
cz = centroid(ZEN)

# ---- 固定配置の整理図の部品（2026-10-26。R5/Q21の draw_*.py と同じ） -------------------
from matplotlib.patches import Rectangle  # noqa: E402
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
    print(f'[重なり検査] {name}: 整理図（固定配置。目視で確認する）\n  →', path)


def cell(ax, x, y, w, h, txt, fs=14, fc='white', ec=BLACK, color=BLACK, weight='normal', ha='center', lw=1.3):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, lw=lw))
    tx = x + w / 2 if ha == 'center' else x + 1.0
    ax.text(tx, y + h / 2, txt, ha=ha, va='center', fontsize=fs, color=color, weight=weight, linespacing=1.4)


def terms(pts):
    """倍面積の各項 Im(P_k × Conjg(P_k+1))（電卓の「iの係数」）"""
    n = len(pts)
    return [(pts[k] * pts[(k + 1) % n].conjugate()).imag for k in range(n)]


def box(x, y, w, h, ec, fc, lw=2.0):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.8', ec=ec, fc=fc, lw=lw))


# =====================================================================
# zu01 全体の時系列
# =====================================================================
# ---- zu01：全体の時系列（第1章） ----
fig, ax = board(8.5)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('全体の時系列　3月に死亡、8月に遺産分割、10月17日に申請（申請人は二郎だけ）', fontsize=24, weight='bold', y=0.965)
ax.annotate('', xy=(99, 70), xytext=(0.5, 70), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, d, tx_, col in [(12, '令和3年3月1日', '山田太郎が死亡\n相続人は一郎・二郎・三郎の\n3人だけ', GRAY),
                       (48, '8月1日', '遺産分割協議\n甲区画→一郎、乙区画→二郎\n丙区画→三郎', BLUE),
                       (86, '10月17日', '登記の申請（問3）\n申請人は二郎だけ', RED)]:
    ax.plot([x], [70], 'o', ms=13, color=col, zorder=5)
    ax.plot([x, x], [70, 78], color=col, lw=1.4)
    ax.text(x, 79, d, ha='center', va='bottom', fontsize=17, color=col, weight='bold')
    ax.text(x, 66.5, tx_, ha='center', va='top', fontsize=14, linespacing=1.5)
ax.add_patch(Rectangle((12, 44), 74, 8, color=GRAY, alpha=0.18, lw=0))
ax.text(49, 48, 'この間、本件土地の登記記録の甲区は「山田太郎」のまま（問題文の現在事項。相続の登記はまだされていない）',
        ha='center', va='center', fontsize=14, color=BLACK)
for x, nm, adr, ku, role, col, fc in [
        (2, '山田一郎', 'M市D町五丁目2番2号', '甲区画（東側）', '申請人ではない（被代位者）', GRAY, '#f4f4f4'),
        (35, '山田二郎', 'K市D町二丁目10番1号', '乙区画（中央）\n抵当権を設定して融資を受けたい', '申請人（聴取記録6「二郎のみが申請人」）', RED, '#fff1f1'),
        (68, '山田三郎', 'S市D町一丁目3番5号', '丙区画（西側）', '申請人ではない（被代位者）', GRAY, '#f4f4f4')]:
    ax.add_patch(Rectangle((x, 6), 30, 32, facecolor=fc, edgecolor=col, lw=1.8))
    ax.text(x + 15, 34, nm, ha='center', va='center', fontsize=19, weight='bold')
    ax.text(x + 15, 28.5, adr, ha='center', va='center', fontsize=14)
    ax.text(x + 15, 20.5, ku, ha='center', va='center', fontsize=13, linespacing=1.4)
    ax.text(x + 15, 10, role, ha='center', va='center', fontsize=14, color=col, weight='bold')
fig.text(0.5, 0.035, '申請人でない一郎・三郎の住所まで、問題文はわざわざ書いている。これが申請人の欄（代位）の合図になる（第8章）。',
         ha='center', fontsize=15)
put_board(fig, 'R3_dai21mon_zu01_jikeiretsu_zentai.png')

# =====================================================================
# zu02 全体像
# =====================================================================
fig, (ax,) = new_figure('北を上にして描き直した全体像（本件土地 10番1　宅地　登記記録386.30㎡）',
                        '道路境界（H・I・K・B）と北の筆界（F・J・L・D）は、どちらも真東から15°ほど南へ傾いた線。軸に平行な辺はない。\n'
                        'E点の杭はH点から0.02mの位置（この縮尺ではH点に重なる）。A・Gは道路境界の点で、本件土地の筆界点ではない。')
z = Zu(ax)
fit(ax, [A, B, C, D, F, T1, T2, G, F + (F - H) * 0.25, F + (F - D) * 0.20, D + (D - C) * 0.35], margin=0.08, pad_aspect=True)
z.poly(HEI, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.poly(KOU, fill=ORANGE)
z.line(A, H, color=BLACK, lw=1.4)
z.line(B, G, color=GRAY, lw=1.2, ls='--')
z.line(C, G, color=GRAY, lw=1.2, ls='--')
z.line(F, F + (F - H) * 0.25, color=BLACK, lw=1.2)
z.line(F, F + (F - D) * 0.20, color=BLACK, lw=1.2)
z.line(D, D + (D - C) * 0.35, color=BLACK, lw=1.2)
z.north_arrow()
z.free_text(centroid(HEI), '丙区画\n三郎', fs=17)
z.free_text(centroid(OTSU), '乙区画\n二郎', fs=17)
z.free_text(centroid(KOU), '甲区画\n一郎', fs=17)
for p, n, kind in [(A, 'A', 'metal'), (B, 'B', 'metal'), (C, 'C', 'metal'), (D, 'D', 'metal'), (F, 'F', 'concrete'),
                   (H, 'H', 'concrete'), (I, 'I', 'concrete'), (J, 'J', 'concrete'), (K, 'K', 'concrete'),
                   (L, 'L', 'concrete')]:
    z.point(p, kind, size=9)
    z.point_label(p, n, away=cz)
z.point(G, 'dot', color=GRAY)
z.point_label(G, 'G', away=cz, color=GRAY)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=cz)
z.edge_label(F, H, '10－2', cz, fs=16, dists=(40, 55), rotate=False)
z.edge_label(J, L, '10－4', cz, fs=16, dists=(34, 46), rotate=False)
z.edge_label(I, K, '道路', cz, fs=16, dists=(40, 55), rotate=False)
z.edge_label(C, D, '道路', cz, fs=16, dists=(40, 55), rotate=False)
z.free_text(F, '10－3', fs=16, offsets=((-45, 30), (-60, 20), (-60, 40)))
ALL_PROBLEMS += save(fig, [z], 'R3_dai21mon_zu02_zentaizu.png')

# =====================================================================
# zu03 注の仕分け
# =====================================================================
# ---- zu03：注の仕分け（第1章） ----
fig, ax = board(11.5)
fig.suptitle('注の仕分け　問題文の注・調査図素図の注・観測値の表の注は番号が別', fontsize=24, weight='bold', y=0.965)
xs, ws = [2, 9, 62], [7, 53, 36]


def chuu_rows(top, rows, hh=5.2):
    """top から下へ行を並べ、最後の行の下端を返す"""
    for r, (n, tx_, use, col) in enumerate(rows):
        y = top - (r + 1) * hh
        fc = '#f3f3f3' if col == GRAY else 'white'
        cell(ax, xs[0], y, ws[0], hh, n, fs=14, fc=fc, weight='bold', color=col)
        cell(ax, xs[1], y, ws[1], hh, tx_, fs=12.5, fc=fc, ha='left', color=GRAY if col == GRAY else BLACK)
        cell(ax, xs[2], y, ws[2], hh, use, fs=12.5, fc=fc, color=col, weight='bold')
    return top - len(rows) * hh


for x, w, tx_ in zip(xs, ws, ['注', '問題文の注（第21問の問題文の注1〜7）', 'どこで使うか']):
    cell(ax, x, 90.5, w, 5.5, tx_, fs=14, fc='#eeeeee', weight='bold')
end = chuu_rows(90.5, [('1', '行為・書類はすべて適法', '読み飛ばす', GRAY),
                       ('2', '登記の申請は書面申請', '読み飛ばす', GRAY),
                       ('3', '座標値は小数第3位を四捨五入（第2位まで）', '問1 A・C・H・L点', BLUE),
                       ('4', '地積測量図は250分の1。辺長は小数第3位を四捨五入', '問4 縮尺・辺長11本', BLUE),
                       ('5', '地積測量図に書かない：座標値・系の番号・地積と求積方法・測量年月日', '問4 書かないもの', RED),
                       ('6', 'K市基準点は点名を付けて書く（座標値は不要）', '問4 T1・T2', BLUE),
                       ('7', '字画を明確に（訂正・加入・削除の書き方）', '読み飛ばす', GRAY)])
ax.text(2, end - 3.4, '調査図素図の（注）', fontsize=15, weight='bold', color=PURPLE)
end = chuu_rows(end - 6.4, [
    ('1', 'B・C・D・F・Hは筆界点、実線は筆界線', '地積測量図に描く点・境界標', PURPLE),
    ('2', 'IJとKLは平行', 'L点（問1）', PURPLE),
    ('3', 'GはABの延長とDCの延長の交点。隅切長BC＝3.00、隅切剪除長GB＝GC', 'C点（問1）', PURPLE)])
ax.text(2, end - 3.4, '〔測量によって得られた観測値〕の表の下の（注）', fontsize=15, weight='bold', color=GREEN)
end = chuu_rows(end - 6.4, [
    ('1', '観測角は、時計回りの角度', 'A点（問1）。足す', GREEN),
    ('2', '北は、X軸正方向に一致する', 'A点（問1）。X＝北', GREEN)])
fig.text(0.5, 0.035, '記事では「問題文の注5」「調査図素図の注3」「観測値の表の下の注1」のように、どの注かを書き分ける。\n色：青＝計算・作図で使う、赤＝書き漏らしやすい、紫・緑＝点の条件、灰＝読み飛ばす。',
         ha='center', fontsize=14)
put_board(fig, 'R3_dai21mon_zu03_chuu_shiwake.png')

# =====================================================================
# zu04 問1 A点（放射）
# =====================================================================
fig, (ax,) = new_figure('問1　A点の求め方（T1から放射）',
                        'T1→T2の方向角 95°51′16.66″ に、時計回りの観測角 227°43′36″ を足す（323°34′52.66″）。その方向へ 7.37m 進んだ点がA。\n'
                        'A点は道路境界（L型側溝）の直線 I・K・B の延長の上に乗る。反時計回りに引くと、道路の向こう側に出てしまう。')
z = Zu(ax)
N_T2 = T1 + (T2 - T1) / abs(T2 - T1) * 9.0
fit(ax, [T1, A, Aw, H, I, I + (I - A) * 0.15, T1 + 7.5, N_T2, H + (F - H) * 0.25, I + (J - I) * 0.25], margin=0.08,
    pad_aspect=True)
z.line(H, H + (F - H) * 0.25, color=GRAY, lw=1.2)
z.line(I, I + (J - I) * 0.25, color=GRAY, lw=1.2)
z.line(A, I + (I - A) * 0.15, color=BLACK, lw=1.6)
z.line(T1, T1 + 7.5, color=GRAY, lw=1.2, ls='--')
z.free_text(T1 + 7.5, '北', color=GRAY, fs=14, offsets=((14, 8), (-14, 8), (0, 14)))
z.line(T1, N_T2, color=BLUE, lw=2.0)
z.line(T1, A, color=RED, lw=2.6)
z.line(T1, Aw, color=GRAY, lw=1.4, ls=':')
z.north_arrow()
z.angle_arc(T1, 2.6, 0, 95.855, color=BLUE)
z.angle_arc(T1, 1.6, 95.855, 323.581, color=RED)
z.point(T1, 'kijun')
z.point(A, 'metal', size=9, color=RED)
z.point(Aw, 'dot', color=GRAY)
for p, n in [(H, 'H'), (I, 'I')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=T1)
z.edge_label(T1, A, '7.37', T1 + P(0, 3), color=RED, fs=18, ts=(0.6, 0.7, 0.5), dists=(16, 24, 32))
z.callout(T1 + P(0.9, 2.45), '方向角 95°51′16.66″\n（北から時計回りにT2の方向）', dirs=(20, 0, 40), color=BLUE,
          dists=(90, 120, 150))
z.callout(T1 + P(-1.2, -0.9), '観測角 227°43′36″\n（T2の方向から時計回り）', dirs=(-20, -40, 0), color=RED,
          dists=(110, 140, 170))
z.callout(A, 'A（505.93, 495.62）', dirs=(120, 150, 90), color=RED)
z.callout(Aw, '反時計回りに測った誤り\n（495.08, 494.51）', dirs=(0, 20, -20), color=GRAY)
z.callout(T1, 'T1（500.00, 500.00）', dirs=(-100, -80, -120), color=BLACK, dists=(140, 170, 200))
z.free_text(N_T2, 'T2の方向（後視）', color=BLUE, fs=14, offsets=((0, 20), (0, -20)))
z.free_text(I + (I - A) * 0.12, '道路境界（L型側溝）', fs=14, offsets=((0, 22), (0, -22), (-40, 22)))
ALL_PROBLEMS += save(fig, [z], 'R3_dai21mon_zu04_A_housha.png')

# =====================================================================
# zu05 問1 C点（隅切り）
# =====================================================================
fig, (ax,) = new_figure('問1　C点の求め方（隅切り）',
                        'GはABの延長とDCの延長の交点。隅切長（BC）は3.00、隅切剪除長（GB＝GC）はGとBの距離 2.1224…。\n'
                        'C ＝ G ＋ (D − G) ÷ Abs(D − G) × Abs(B − G)。3.00でGから進めると、BCが3.68になり隅切長と合わない。')
z = Zu(ax)
fit(ax, [B, G, Cw, K + (B - K) * 0.3, C + (D - C) * 0.18], margin=0.10, pad_aspect=True)
z.poly([B, C, G], color=GRAY, lw=0, fill=ORANGE, alpha=0.25, check=False)
z.line(K + (B - K) * 0.3, B, color=BLACK, lw=2.2)
z.line(B, C, color=BLACK, lw=2.2)
z.line(C, C + (D - C) * 0.18, color=BLACK, lw=2.2)
z.line(B, G, color=GRAY, lw=1.4, ls='--')
z.line(G, C, color=GRAY, lw=1.4, ls='--')
z.line(B, Cw, color=GRAY, lw=1.2, ls=':')
z.north_arrow()
for p, n in [(B, 'B'), (C, None), (G, 'G')]:
    z.point(p, 'metal' if n != 'G' else 'dot', size=9, color=RED if n is None else (GRAY if n == 'G' else BLACK))
    if n:
        z.point_label(p, n, away=centroid([B, C, P(503, 520)]), color=GRAY if n == 'G' else BLACK)
z.point(Cw, 'dot', color=GRAY)
z.edge_label(B, C, 'BC ＝ 3.00（隅切長）', G, fs=15, dists=(14, 20, 28))
z.edge_label(G, B, 'GB ＝ 2.12', centroid([B, C, G]), fs=15)
z.edge_label(G, C, 'GC ＝ 2.12', centroid([B, C, G]), fs=15)
z.free_text(C + (D - C) * 0.16, 'Dの方向へ', fs=14, offsets=((-45, 0), (45, 0), (-55, -15)))
z.free_text(B + (K - B) * 0.22, 'Kの方向へ', fs=14, offsets=((0, 22), (0, -22), (0, 30)))
z.callout(C, 'C（499.79, 526.75）', dirs=(170, 150, 190), color=RED, dists=(90, 120, 150))
z.callout(Cw, 'Gから3.00進めた誤り\n（500.64, 526.98）　BC ＝ 3.68', dirs=(165, 150, 135, 180), color=GRAY,
          dists=(70, 90, 110))
z.callout(G, 'G（497.74, 526.20）', dirs=(-30, -10, -60), color=GRAY, dists=(45, 60, 80))
ALL_PROBLEMS += save(fig, [z], 'R3_dai21mon_zu05_C_sumikiri.png')

# =====================================================================
# zu06 H点の判断
# =====================================================================
# ---- zu06：H点が筆界点と判断される流れ（第4章。問題文の〔立会い等〕イの文を図にしたもの） ----
fig, ax = board(9)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('H点は、E点の杭ではなく「ABとFEの延長線の交点」（立会いの結果）', fontsize=24, weight='bold', y=0.965)
STEP = [('立会いで分かったこと', 'E点のコンクリート杭は、\n本件土地と道路の境界線の\n上になかった\n（E点を筆界点としても、\n公差の範囲は超えない）', GRAY, '#f4f4f4'),
        ('H点の定義', 'AとBを結ぶ直線と、\nFとEを結ぶ直線の延長線の\n交点をH点とすると、\n10番2の地積測量図の内容と\n一致する', BLUE, '#eef4fb'),
        ('判断', 'H点を、本件土地・10番2の\n土地・道路の筆界点と\n判断した', RED, '#fff1f1'),
        ('措置', '10番2の土地の所有者の\n合意のもと、E点の\nコンクリート杭を\nH点の位置に移設した', GREEN, '#f1faf2')]
for k, (hd, body, col, fc) in enumerate(STEP):
    x = 2 + k * 24.5
    ax.add_patch(Rectangle((x, 38), 21, 50, facecolor=fc, edgecolor=col, lw=2.0))
    ax.text(x + 10.5, 83, hd, ha='center', va='center', fontsize=17, weight='bold', color=col)
    ax.text(x + 10.5, 59, body, ha='center', va='center', fontsize=14, linespacing=1.6)
    if k < 3:
        ax.annotate('', xy=(x + 24.2, 63), xytext=(x + 21.3, 63),
                    arrowprops=dict(arrowstyle='-|>', color=BLACK, lw=2.0, mutation_scale=18))
ax.add_patch(Rectangle((2, 2), 45, 28, facecolor='#f4f4f4', edgecolor=GRAY, lw=1.6))
ax.text(24.5, 26, '誤り：「公差の範囲内だから、E点のままでよい」', ha='center', va='center', fontsize=16, weight='bold', color=GRAY)
ax.text(24.5, 14, '座標もわかっているE点（504.63, 500.56）を\nそのまま答えにする', ha='center', va='center', fontsize=14, color=GRAY,
        linespacing=1.5)
ax.add_patch(Rectangle((53, 2), 45, 28, facecolor='#fff1f1', edgecolor=RED, lw=2.0))
ax.text(75.5, 26, '正しい：筆界点は杭の位置ではなく、H点', ha='center', va='center', fontsize=16, weight='bold', color=RED)
ax.text(75.5, 14, 'H点（504.61, 500.55）を、ABとFEの延長線の交点として\n計算して答える（E点とは0.02m違う）', ha='center', va='center',
        fontsize=14, linespacing=1.5)
fig.text(0.5, 0.035, '問題文は、E点の杭をH点に移した理由まで書いている。「公差の範囲を超えない」は、E点でよいという意味ではない。', ha='center', fontsize=15)
put_board(fig, 'R3_dai21mon_zu06_H_hantei.png')

# =====================================================================
# zu07 H点の交点の比
# =====================================================================
# ---- zu07：H点の交点の比（計算過程。H ＝ F ＋ (E − F) × t） ----
cA = (A - F).conjugate() * (B - A)
cE = (E - F).conjugate() * (B - A)
assert f'{abs(cA.imag):.3f}' == '446.791' and f'{abs(cE.imag):.4f}' == '446.1384'
t_H = abs(cA.imag) / abs(cE.imag)
assert 1.001 < t_H < 1.002 and abs(F + (E - F) * t_H - P(504.6090, 500.5528)) < 5e-4
fig, ax = board(9)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('H点の交点の比　t ＝ ［FからABまでの高さ］÷［FからEへ進んでABに近づく高さ］', fontsize=23, weight='bold', y=0.965)
# 左：模式図（位置は模式）
ax.plot([3, 46], [18, 18], color=BLACK, lw=2.4)
ax.text(46.5, 18, 'B', fontsize=15, weight='bold', va='center')
ax.text(2.5, 18, 'A', fontsize=15, weight='bold', va='center', ha='right')
ax.text(24, 13.5, '道路境界（A→B）', fontsize=14, ha='center')
Fp, Ep, Hp = (8, 84), (33.3, 22.4), (35.6, 18)
ax.plot([Fp[0], Hp[0]], [Fp[1], Hp[1]], color=BLACK, lw=2.0)
for p_, n_, dx_, dy_ in [(Fp, 'F', -1.5, 2), (Ep, 'E', -2.5, 3.5), (Hp, 'H', 2.8, -3.5)]:
    ax.plot([p_[0]], [p_[1]], 'o', ms=9, color=RED if n_ == 'H' else BLACK, zorder=5)
    ax.text(p_[0] + dx_, p_[1] + dy_, n_, fontsize=16, weight='bold', ha='center', color=RED if n_ == 'H' else BLACK)
ax.plot([8, 8], [84, 18], color=BLUE, lw=1.4, ls='--')
ax.plot([16, 16], [84, 22.4], color=RED, lw=1.4, ls='--')
ax.plot([8, 16], [84, 84], color=GRAY, lw=1)
ax.text(5.8, 54, '分子\n446.791', fontsize=14, color=BLUE, ha='right', va='center', weight='bold')
ax.text(17.5, 33, '分母\n446.1384', fontsize=14, color=RED, ha='left', va='center', weight='bold')
ax.text(24, 6, '（位置は模式。E〜Hは実際は0.02mで、図では離して描いている）', fontsize=12.5, ha='center', color=GRAY)
# 右：式と結論
for y, hd, body, col, fc in [
        (72, '① 分子', 'Conjg(A − F) × (B − A) のiの係数 ＝ 446.791\n（FからABまでの高さに比例する数）', BLUE, '#eef4fb'),
        (51, '② 分母', 'Conjg(E − F) × (B − A) のiの係数 ＝ 446.1384\n（FからEへ進んで、ABに近づいた高さに比例する数）', RED, '#fff1f1')]:
    ax.add_patch(Rectangle((52, y), 46, 17, facecolor=fc, edgecolor=col, lw=1.8))
    ax.text(54, y + 13.5, hd, fontsize=15, weight='bold', color=col, va='center')
    ax.text(54, y + 6.5, body, fontsize=13.5, va='center', linespacing=1.5)
ax.add_patch(Rectangle((52, 22), 46, 24, facecolor='#f4f4f4', edgecolor=BLACK, lw=1.8))
ax.text(54, 40, 't ＝ ① ÷ ② ＝ 446.791 ÷ 446.1384 ＝ 1.0015…', fontsize=16, weight='bold', va='center')
ax.text(54, 31.5, '1より大きいので、HはEを通り越した先（FEの延長線上）\nH ＝ F ＋ (E − F) × t ＝ （504.61, 500.55）', fontsize=14,
        va='center', linespacing=1.5, color=RED)
ax.text(52, 14, '比が1より小さければFとEの間、1より大きければEの先。\n問題文の「延長線の交点」と一致する。', fontsize=13.5, va='top', linespacing=1.5)
fig.text(0.5, 0.035, '比の分子と分母は、どちらもiの係数。実部は使わない。符号が同じなので t は正で、FからEの向きに進む。', ha='center', fontsize=15)
put_board(fig, 'R3_dai21mon_zu07_H_hi.png')

# =====================================================================
# zu08 H点と10番2の地積測量図
# =====================================================================
fig, (ax1, ax2) = new_figure('問1　H点の求め方（ABとFEの延長の交点）と10番2の地積測量図による裏付け',
                             '左：H ＝ F ＋ (E − F) × 446.791 ÷ 446.1384（比が1を少し超えるので、FからEを通り越した延長線上）。\n'
                             '10番2の地積測量図の FH ＝ 15.16 と、底辺AF（16.32）への高さ 4.73 が一致するのはH点。右：E点では FE ＝ 15.14・高さ 4.72 で合わない。',
                             ncols=2, width_ratios=[1.35, 1])
za = Zu(ax1, fontsize=14)
foot = A + (F - A) * (((H - A) * (F - A).conjugate()).real / abs(F - A) ** 2)
fit(ax1, [A, F, H, I, F + (F - H) * 0.12, F + (F - J) * 0.30, F + (J - F) * 0.45], margin=0.10, pad_aspect=True)
za.poly([A, F, H], color=GRAY, lw=0, fill=BLUE, alpha=0.15, check=False)
za.line(A, I, color=BLACK, lw=2.0)
za.line(F, H, color=BLACK, lw=2.0)
za.line(F, F + (F - H) * 0.12, color=BLACK, lw=1.2)
za.line(F, F + (F - J) * 0.30, color=BLACK, lw=1.2)
za.line(F, F + (J - F) * 0.45, color=BLACK, lw=2.0)
za.line(A, F, color=GRAY, lw=1.4, ls='-.')
za.line(H, foot, color=RED, lw=1.6, ls='--')
za.right_angle(foot, F, H, size=0.45)
za.north_arrow(length=0.07)
for p, n, kind in [(A, 'A', 'metal'), (F, 'F', 'concrete'), (I, 'I', 'concrete')]:
    za.point(p, kind, size=8)
    za.point_label(p, n, away=centroid([A, F, H, I]))
za.point(H, 'concrete', size=8, color=RED)
za.point_label(H, 'H', away=P(510, 505), color=RED)
za.edge_label(F, H, 'FH ＝ 15.16', A, fs=14, outward=False, ts=(0.5, 0.4, 0.6))
za.edge_label(A, F, '底辺AF（図の16.32）', H, fs=13, color=GRAY, dists=(10, 16, 22))
za.edge_label(H, foot, '高さ 4.73', A, fs=13, color=RED, ts=(0.5, 0.4, 0.6), dists=(10, 16))
za.free_text(centroid([A, F, H]) + P(0, -2.5), '10番2', fs=16, offsets=((0, 0), (-20, 10)))
za.free_text(centroid(HEI), '本件土地\n（丙区画）', fs=15, offsets=((0, 0), (20, 0)))
za.edge_label(A, I, '道路', centroid([A, F, I]), fs=14, dists=(24, 32), rotate=False)

zb = Zu(ax2, fontsize=14)
fit(ax2, [E, H, H + (H - F) * 0.003, H - (H - F) * 0.007, H + (B - A) * 0.0035, H - (B - A) * 0.0035], margin=0.10,
    pad_aspect=True)
zb.line(H + (H - F) * 0.003, H - (H - F) * 0.007, color=BLACK, lw=2.0)
zb.line(H + (B - A) * 0.0035, H - (B - A) * 0.0035, color=BLACK, lw=2.0)
zb.north_arrow(length=0.08)
zb.point(E, 'concrete', size=9, color=GRAY)
zb.point(H, 'concrete', size=9, color=RED)
zb.callout(E, 'E（504.63, 500.56）\nFE ＝ 15.14　高さ 4.72\n→ 10番2の図と合わない', dirs=(100, 130, 70), color=GRAY,
           dists=(60, 80, 100))
zb.callout(H, 'H（504.61, 500.55）\nFH ＝ 15.16　高さ 4.73\n→ 10番2の図と一致', dirs=(-80, -110, -50), color=RED,
           dists=(60, 80, 100))
zb.edge_label(E, H, 'EH ＝ 0.02', P(504.62, 500.50), fs=14, dists=(22, 30, 40), rotate=False)
zb.edge_label(H + (B - A) * 0.0015, H + (B - A) * 0.0033, '道路境界AB', T1, fs=13, dists=(12, 18))
zb.edge_label(H - (H - F) * 0.004, H - (H - F) * 0.0068, '筆界FH（FEの延長）', A, fs=13, dists=(12, 18))
ALL_PROBLEMS += save(fig, [za, zb], 'R3_dai21mon_zu08_H_kousa.png')

# =====================================================================
# zu09 L点の交点の比
# =====================================================================
# ---- zu09：L点の交点の比（計算過程。L ＝ F ＋ (D − F) × t） ----
cK = (K - F).conjugate() * (J - I)
cD = (D - F).conjugate() * (J - I)
assert f'{abs(cK.imag):.4f}' == '254.7785' and f'{abs(cD.imag):.3f}' == '382.042'
t_L = abs(cK.imag) / abs(cD.imag)
assert 0.666 < t_L < 0.667 and abs(F + (D - F) * t_L - P(514.2684, 521.8320)) < 5e-4
fig, ax = board(9)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('L点の交点の比　t ＝ ［Fの平行線からKの平行線まで］÷［Fの平行線からDの平行線まで］', fontsize=23, weight='bold', y=0.965)
# 左：模式図（IJの平行線を3本引く。位置は模式）
xF, xD = 6, 42
xL = xF + t_L * (xD - xF)
dxs = 0.20
yt, yb = 80, 34
ax.plot([xF - 2, xD + 3], [yt, yt], color=BLACK, lw=2.2)
ax.text(xF + 4, yt - 4.5, '北の筆界（F・J・L・D）', fontsize=12.5, va='center')
for xp, col, nm in [(xF, GRAY, 'F'), (xL, RED, 'L'), (xD, GRAY, 'D')]:
    ax.plot([xp, xp + dxs * (yt - yb)], [yt, yb], color=col, lw=1.8, ls='--' if nm != 'L' else '-')
    ax.plot([xp], [yt], 'o', ms=9, color=col if nm == 'L' else BLACK, zorder=5)
    ax.text(xp, yt + 3.5, nm, fontsize=16, weight='bold', ha='center', color=RED if nm == 'L' else BLACK)
ax.plot([xL + dxs * (yt - yb)], [yb], 'o', ms=9, color=RED, zorder=5)
ax.text(xL + dxs * (yt - yb) + 1.5, yb - 3.5, 'K', fontsize=16, weight='bold', ha='center', color=RED)
for xa, xb, yy, txt_, col in [(xF, xL, yb - 9, '分子 254.7785', BLUE), (xF, xD, yb - 17, '分母 382.042', RED)]:
    ax.annotate('', xy=(xb + dxs * (yt - yb), yy), xytext=(xa + dxs * (yt - yb), yy),
                arrowprops=dict(arrowstyle='<->', color=col, lw=1.8))
    ax.text((xa + xb) / 2 + dxs * (yt - yb), yy - 3, txt_, fontsize=13.5, color=col, ha='center', va='top', weight='bold')
ax.text(24, 90, '各線はIJと平行（Fを通る線・Kを通る線・Dを通る線）', fontsize=13.5, ha='center', color=GRAY)
ax.text(24, 5.5, '（位置は模式。実際の間隔の比が 254.7785 : 382.042）', fontsize=12.5, ha='center', color=GRAY)
for y, hd, body, col, fc in [
        (72, '① 分子', 'Conjg(K − F) × (J − I) のiの係数 ＝ 254.7785\n（Fの平行線からKの平行線までの幅に比例する数）', BLUE, '#eef4fb'),
        (51, '② 分母', 'Conjg(D − F) × (J − I) のiの係数 ＝ 382.042\n（Fの平行線からDの平行線までの幅に比例する数）', RED, '#fff1f1')]:
    ax.add_patch(Rectangle((52, y), 46, 17, facecolor=fc, edgecolor=col, lw=1.8))
    ax.text(54, y + 13.5, hd, fontsize=15, weight='bold', color=col, va='center')
    ax.text(54, y + 6.5, body, fontsize=13.5, va='center', linespacing=1.5)
ax.add_patch(Rectangle((52, 22), 46, 24, facecolor='#f4f4f4', edgecolor=BLACK, lw=1.8))
ax.text(54, 40, 't ＝ ① ÷ ② ＝ 254.7785 ÷ 382.042 ＝ 0.6669…', fontsize=16, weight='bold', va='center')
ax.text(54, 31.5, '1より小さいので、LはFとDの間（筆界FDの上）\nL ＝ F ＋ (D − F) × t ＝ （514.27, 521.83）', fontsize=14,
        va='center', linespacing=1.5, color=RED)
ax.text(52, 14, 'IJとKLは平行（調査図素図の注2）。「Kを通るIJの平行線」の\n向きは J − I そのものなので、もう1点を作る必要はない。', fontsize=13.5,
        va='top', linespacing=1.5)
fig.text(0.5, 0.035, 'Hの交点の式と同じ形。分子と分母のiの係数の符号が同じなので、t は正になる。', ha='center', fontsize=15)
put_board(fig, 'R3_dai21mon_zu09_L_hi.png')

# =====================================================================
# zu10 L点（台形）
# =====================================================================
fig, (ax1, ax2) = new_figure('問1　L点の求め方（Kを通るIJの平行線と筆界FDの交点）',
                             '左：平行なのはIJとKLの1組だけ。IKとJLは平行でないので、乙区画は台形（IJ ＝ 14.98、KL ＝ 14.84）。\n'
                             'L ＝ F ＋ (D − F) × 254.7785 ÷ 382.042。右：L ＝ J ＋ (K − I)（平行四辺形の思い込み）では、筆界FDから0.15m北（10番4の側）に外れる。',
                             ncols=2, width_ratios=[1.4, 1])
za = Zu(ax1, fontsize=14)
fit(ax1, ZEN, margin=0.10, pad_aspect=True)
za.poly(ZEN, lw=1.6)
za.poly(OTSU, color=BLACK, lw=0, fill=BLUE, alpha=0.25, check=False)
za.line(I, J, color=BLACK, lw=2.2)
za.line(K, L, color=RED, lw=2.6)
za.parallel_marks(I, J, n=1)
za.parallel_marks(K, L, n=1)
za.north_arrow(length=0.07)
for p, n in [(H, 'H'), (I, 'I'), (J, 'J'), (K, 'K'), (F, 'F'), (D, 'D'), (B, 'B'), (C, 'C')]:
    za.point(p, 'dot', size=6)
    za.point_label(p, n, away=cz)
za.point(L, 'dot', size=8, color=RED)
za.edge_label(I, J, 'IJ ＝ 14.98', centroid(OTSU), fs=13, outward=False, dists=(12, 18))
za.edge_label(K, L, 'KL ＝ 14.84', centroid(OTSU), fs=13, outward=False, dists=(12, 18))
za.callout(L, 'L（514.27, 521.83）', dirs=(80, 60, 100), color=RED, dists=(50, 70, 90))
za.free_text(centroid(OTSU), '乙区画\n（台形）', fs=14, offsets=((0, 0), (0, 10)))

zb = Zu(ax2, fontsize=14)
fit(ax2, [L, Lw, F + (D - F) * 0.66, F + (D - F) * 0.675, L - (L - K) * 0.02, Lw - (Lw - K) * 0.02], margin=0.10,
    pad_aspect=True)
zb.line(F + (D - F) * 0.66, F + (D - F) * 0.675, color=BLACK, lw=2.2)
zb.line(L - (L - K) * 0.02, L, color=RED, lw=2.2)
zb.line(Lw - (Lw - K) * 0.02, Lw, color=GRAY, lw=1.6, ls=':')
zb.north_arrow(length=0.08)
zb.point(L, 'dot', size=9, color=RED)
zb.point(Lw, 'dot', size=9, color=GRAY)
zb.callout(L, 'L（514.27, 521.83）\n筆界FDの上', dirs=(-160, -140, -120, 180), color=RED, dists=(70, 90, 110))
zb.callout(Lw, '平行四辺形の誤り\n（514.41, 521.87）\n筆界から0.15m北に外れる', dirs=(180, 200, 160, 220), color=GRAY,
           dists=(60, 80, 110))
zb.edge_label(F + (D - F) * 0.669, F + (D - F) * 0.675, '筆界FD（ブロック塀）', K, fs=13, dists=(12, 18, 26))
zb.edge_label(L, L - (L - K) * 0.02, 'KL（IJと平行）', Lw, fs=13, color=RED, dists=(12, 18, 26), ts=(0.6, 0.7, 0.8))
ALL_PROBLEMS += save(fig, [za, zb], 'R3_dai21mon_zu10_L_heikousen.png')

# =====================================================================
# zu11・zu12 問2
# =====================================================================
# ---- zu11：問2 地図と地図に準ずる図面（（イ）〜（エ）の対） ----
fig, ax = board(9)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('問2　地図は「区画・地番」、地図に準ずる図面は「位置・形状・地番」', fontsize=24, weight='bold', y=0.965)
ax.add_patch(Rectangle((2, 40), 44, 50, facecolor='#f4f4f4', edgecolor=GRAY, lw=2.0))
ax.text(24, 85, '地図（法第14条第1項・第2項）', ha='center', va='center', fontsize=19, weight='bold', color=GRAY)
ax.text(4.5, 74, '・登記所に備え付ける', ha='left', va='center', fontsize=16)
ax.text(4.5, 64, '・一筆又は二筆以上の土地ごとに作成', ha='left', va='center', fontsize=16)
ax.text(4.5, 54, '・各土地の区画を明確にし、地番を表示', ha='left', va='center', fontsize=16, weight='bold')
ax.text(4.5, 45, '　→　精度の高い図面（区画まで明確）', ha='left', va='center', fontsize=14, color=GRAY)
ax.add_patch(Rectangle((54, 40), 44, 50, facecolor='#fff1f1', edgecolor=RED, lw=2.2))
ax.text(76, 85, '地図に準ずる図面（同条第4項・第5項）', ha='center', va='center', fontsize=19, weight='bold', color=RED)
ax.text(56.5, 74, '・地図が備え付けられるまでの間、', ha='left', va='center', fontsize=16)
ax.text(56.5, 68, '　（ア）登記所　に備え付ける', ha='left', va='center', fontsize=16, color=RED, weight='bold')
ax.text(56.5, 58, '・一筆又は二筆以上の土地の', ha='left', va='center', fontsize=16)
ax.text(56.5, 51.5, '　（イ）位置・（ウ）形状・（エ）地番', ha='left', va='center', fontsize=16, color=RED, weight='bold')
ax.text(56.5, 45, '　→　位置と形状まで（区画の明確さまでは求めない）', ha='left', va='center', fontsize=14, color=GRAY)
ax.annotate('', xy=(53.5, 65), xytext=(46.5, 65), arrowprops=dict(arrowstyle='<->', color=GRAY, lw=1.6))
ax.text(50, 69, '対で覚える', ha='center', va='bottom', fontsize=14, color=GRAY)
ax.add_patch(Rectangle((2, 4), 96, 28, facecolor='white', edgecolor=BLACK, lw=1.4))
ax.text(5, 28, '藍子の誤答：（イ）〜（エ）を「区画」「地番」と書く（それは第14条第2項、本物の地図の話）', ha='left', va='center', fontsize=15, color=GRAY)
ax.text(5, 20, '（ア）は「法務局」ではなく、条文の言葉の「登記所」', ha='left', va='center', fontsize=15, weight='bold')
ax.text(5, 11, '答案用紙の第2欄：ア 登記所　イ 位置　ウ 形状　エ 地番（イ〜エは順不同）', ha='left', va='center', fontsize=15, color=RED, weight='bold')
fig.text(0.5, 0.035, '本件土地の地域には法第14条第1項の地図がなく、地図に準ずる図面が備え付けられている（問題文の調査結果）。', ha='center', fontsize=15)
put_board(fig, 'R3_dai21mon_zu11_chizu_kukaku.png')

# ---- zu12：問2 閉鎖と保存期間（（オ）（カ）） ----
fig, ax = board(9)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('問2　閉鎖した地図に準ずる図面の保存期間は「永久」（閉鎖した地積測量図の30年間と区別）', fontsize=23, weight='bold', y=0.965)
for x, w, hd, body, col, fc, ref in [
        (2, 26, '登記官が新たな地図を\n備え付ける', '', BLACK, 'white', ''),
        (37, 26, '従前の地図に準ずる図面の\n全部又は一部を\n（オ）閉鎖', '', RED, '#fff1f1', '規則第12条第1項・第4項'),
        (72, 26, '閉鎖した図面の保存期間\n（カ）永久', '', RED, '#fff1f1', '規則第28条第2号')]:
    ax.add_patch(Rectangle((x, 52), w, 36, facecolor=fc, edgecolor=col, lw=2.2))
    ax.text(x + w / 2, 74, hd, ha='center', va='center', fontsize=18, weight='bold', color=col, linespacing=1.5)
    ax.text(x + w / 2, 58, ref, ha='center', va='center', fontsize=13, color=GRAY)
for x0, x1 in [(28.4, 36.6), (63.4, 71.6)]:
    ax.annotate('', xy=(x1, 70), xytext=(x0, 70), arrowprops=dict(arrowstyle='-|>', color=BLACK, lw=2.2, mutation_scale=22))
ax.add_patch(Rectangle((2, 6), 96, 36, facecolor='#f4f4f4', edgecolor=GRAY, lw=1.6))
ax.text(5, 36, '藍子の誤答：「閉鎖した日から30年間」', ha='left', va='center', fontsize=16, color=GRAY)
ax.text(5, 27, '30年間は、閉鎖した地積測量図・建物図面など（規則第28条第13号）の保存期間', ha='left', va='center', fontsize=16)
ax.text(5, 18, '地図及び地図に準ずる図面（閉鎖したものを含む）は永久（同条第2号）', ha='left', va='center', fontsize=16, weight='bold', color=RED)
ax.text(5, 10, '昔の土地の形を調べる大事な資料だから、閉鎖しても永久に保存される', ha='left', va='center', fontsize=14, color=GRAY)
fig.text(0.5, 0.035, '答案用紙の第2欄：オ 閉鎖　カ 永久。', ha='center', fontsize=15)
put_board(fig, 'R3_dai21mon_zu12_chizu_eikyuu.png')

# =====================================================================
# zu13〜15 3区画の面積
# =====================================================================
# ---- zu13〜15：問3 3つの区画の面積（座標法。電卓の各項） ----
AREA_I = {'丙': '271.691', '乙': '253.6844', '甲': '246.4256'}           # 記事の電卓の表示（iの係数）
AREA_HALF = {'丙': '135.8455', '乙': '126.8422', '甲': '123.2128'}       # 2で割った値
for nm, pts in [('丙', HEI), ('乙', OTSU), ('甲', KOU)]:
    tm = terms(pts)
    assert abs(abs(sum(tm)) - float(AREA_I[nm])) < 5e-4, (nm, sum(tm))
    assert abs(float(AREA_HALF[nm]) - AREAS[nm][1]) < 5e-5
    assert abs(abs(sum(tm)) / 2 - AREAS[nm][1]) < 5e-5


def area_figure(name, kubun, pts, names, ku_color, extra=None):
    tm = terms(pts)
    n = len(pts)
    sgn = 1 if sum(tm) > 0 else -1
    fig, (ax1, ax2) = new_figure(f'問3　{kubun}区画の面積（座標法）',
                                 f'左：{"→".join(names)}の順に回る（辺に①〜を振る）。右：電卓は各項の合計を表示する。実部は使わない。\n'
                                 f'iの係数の合計を2で割り、宅地なので小数第2位未満を切り捨てる。丸めた座標で計算する。',
                                 ncols=2, width_ratios=[1.0, 1.15])
    z = Zu(ax1, fontsize=14)
    fit(ax1, pts, margin=0.22, pad_aspect=True)
    z.poly(pts, fill=ku_color, lw=2.0)
    z.north_arrow(length=0.08)
    cc = centroid(pts)
    for k in range(n):
        p, q = pts[k], pts[(k + 1) % n]
        z.edge_label(p, q, '①②③④⑤'[k], cc, color=RED, fs=17, dists=(18, 26, 34), rotate=False)
    for p, nm in zip(pts, names):
        z.point(p, 'dot', size=7)
        z.point_label(p, nm, away=cc)
    z.free_text(cc, f'{kubun}区画', fs=18)
    ax2.axis('off')
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    rowh = min(9.0, 78.0 / (n + 4))
    top = 94
    cell(ax2, 0, top - rowh, 11, rowh, '辺', fs=14, fc='#eeeeee', weight='bold')
    cell(ax2, 11, top - rowh, 49, rowh, '各項（電卓の式）', fs=14, fc='#eeeeee', weight='bold')
    cell(ax2, 60, top - rowh, 40, rowh, 'iの係数', fs=14, fc='#eeeeee', weight='bold')
    for k in range(n):
        y = top - (k + 2) * rowh
        a_, b_ = names[k], names[(k + 1) % n]
        cell(ax2, 0, y, 11, rowh, '①②③④⑤'[k], fs=15, color=RED, weight='bold')
        cell(ax2, 11, y, 49, rowh, f'{a_}・Conjg({b_})', fs=14)
        v = tm[k] * sgn
        cell(ax2, 60, y, 40, rowh, f'{v:+.4f}'.replace('-', '−'), fs=14, ha='center')
    y = top - (n + 2) * rowh
    cell(ax2, 0, y, 60, rowh, '合計（電卓の表示のiの係数）', fs=14, fc='#fff1f1', weight='bold')
    cell(ax2, 60, y, 40, rowh, AREA_I[kubun], fs=15, fc='#fff1f1', color=RED, weight='bold')
    y -= rowh
    cell(ax2, 0, y, 60, rowh, '÷ 2', fs=14)
    cell(ax2, 60, y, 40, rowh, AREA_HALF[kubun] + '㎡', fs=14)
    y -= rowh
    cell(ax2, 0, y, 60, rowh, '小数第2位未満を切り捨て', fs=14, fc='#f1faf2', weight='bold')
    cell(ax2, 60, y, 40, rowh, f'{AREAS[kubun][2]}㎡', fs=16, fc='#f1faf2', color=RED, weight='bold')
    if extra:
        ax2.text(50, y - 5, extra, ha='center', va='top', fontsize=14, color=RED, weight='bold', linespacing=1.5)
    return save(fig, [z], name)


ALL_PROBLEMS += area_figure('R3_dai21mon_zu13_menseki_hei.png', '丙', HEI, ['H', 'I', 'J', 'F'], GREEN)
ALL_PROBLEMS += area_figure('R3_dai21mon_zu14_menseki_otsu.png', '乙', OTSU, ['I', 'K', 'L', 'J'], BLUE)
ALL_PROBLEMS += area_figure('R3_dai21mon_zu15_menseki_kou.png', '甲', KOU, ['B', 'C', 'D', 'L', 'K'], ORANGE,
                            extra='3区画の合計　135.84 ＋ 126.84 ＋ 123.21 ＝ 385.89㎡\n（登記記録は386.30㎡。差0.41㎡は次の図で判断）')

# =====================================================================
# zu16 精度区分
# =====================================================================
# ---- zu16：問3 精度区分は地域で決まる（市街地地域 → 甲2） ----
fig, ax = board(9)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('問3　精度区分は地域で決まる（市街地地域 → 甲2まで）。「乙区画」の乙とは関係ない', fontsize=23, weight='bold', y=0.965)
ax.text(2, 91, '不動産登記規則第10条第4項（地図を作る測量の誤差の限度。地積測量図は第77条第5項で準用）', fontsize=14.5, weight='bold', va='center')
for k, (reg, lim, col, fc) in enumerate([('第1号　市街地地域（主に宅地が占める地域など）', '精度区分 甲2まで', RED, '#fff1f1'),
                                          ('第2号　村落・農耕地域', '精度区分 乙1まで', GRAY, '#f4f4f4'),
                                          ('第3号　山林・原野地域', '精度区分 乙3まで', GRAY, '#f4f4f4')]):
    y = 76 - k * 12
    cell(ax, 2, y, 60, 10, reg, fs=14.5, fc=fc, ha='left', color=col, weight='bold' if col == RED else 'normal')
    cell(ax, 62, y, 30, 10, lim, fs=15, fc=fc, color=col, weight='bold')
ax.text(94, 81, '← 本件土地', fontsize=15, color=RED, weight='bold', va='center')
ax.text(2, 46, '問題文の表（地積386.30㎡の場合の公差）', fontsize=14.5, weight='bold', va='center')
LIM = [('甲1', '0.75㎡', GRAY), ('甲2', '1.85㎡', RED), ('甲3', '3.71㎡', GRAY), ('乙1', '5.45㎡', GRAY), ('乙2', '11.01㎡', GRAY),
       ('乙3', '22.03㎡', GRAY)]
cw = 15
for k, (nm, v, col) in enumerate(LIM):
    x = 2 + k * (cw + 1.2)
    fc = '#fff1f1' if col == RED else '#f4f4f4'
    cell(ax, x, 34, cw, 8, nm, fs=15, fc=fc, color=col, weight='bold')
    cell(ax, x, 26, cw, 8, v, fs=15, fc=fc, color=col, weight='bold')
ax.annotate('', xy=(2 + 1 * (cw + 1.2) + cw / 2, 24.5), xytext=(2 + 1 * (cw + 1.2) + cw / 2, 18),
            arrowprops=dict(arrowstyle='-|>', color=RED, lw=2.0, mutation_scale=18))
ax.text(2 + 1 * (cw + 1.2) + cw / 2, 16.5, '甲2の1.85㎡で\n公差を比べる', fontsize=14.5, color=RED, ha='center', va='top', weight='bold',
        linespacing=1.4)
ax.text(62, 14, '乙区画は区画の名前（二郎の区画）。精度区分の「乙1」を見て\n5.45㎡で比べると、地積更正が要るかの判断を誤る', fontsize=14, color=GRAY, va='top',
        linespacing=1.5)
fig.text(0.5, 0.035, '本件土地の地域は、問題文の調査結果で「不動産登記規則第10条第2項第1号の市街地地域に属する」とされている。', ha='center', fontsize=15)
put_board(fig, 'R3_dai21mon_zu16_seido_kubun.png')

# =====================================================================
# zu17 公差の判定
# =====================================================================
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問3　地積更正が必要かの判定（精度区分 甲2）', fontsize=24, weight='bold', y=0.96)
ax = fig.add_axes([0.06, 0.30, 0.88, 0.50])
ax.set_xlim(383.6, 389.0)
ax.set_ylim(-1.6, 2.4)
ax.axis('off')
ax.plot([383.8, 388.8], [0, 0], color=BLACK, lw=2)
for v in range(384, 389):
    ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1.2)
    ax.text(v, -0.28, f'{v}', ha='center', va='top', fontsize=13, color=GRAY)
ax.axvspan(386.30 - 1.85, 386.30 + 1.85, ymin=0.30, ymax=0.52, color=GREEN, alpha=0.25)
ax.text(386.30, 0.62, '公差の範囲（386.30 ± 1.85）', ha='center', va='bottom', fontsize=15, color=GREEN)
ax.plot([386.30], [0], 'o', ms=12, color=BLUE)
ax.text(386.55, -0.75, '登記記録\n386.30㎡', ha='left', va='top', fontsize=16, color=BLUE, weight='bold')
ax.plot([385.89], [0], 'o', ms=12, color=RED)
ax.text(385.64, -0.75, '分筆後の地積の合計\n385.89㎡', ha='right', va='top', fontsize=16, color=RED, weight='bold')
ax.annotate('', xy=(385.89, 1.55), xytext=(386.30, 1.55), arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
ax.text(386.1, 1.7, '差 0.41㎡ ≦ 公差 1.85㎡　→　範囲内なので地積更正は不要', ha='center', va='bottom', fontsize=17,
        color=RED, weight='bold')
fig.text(0.5, 0.15, '市街地地域（不動産登記規則第10条第2項第1号）の誤差の限度は精度区分 甲2 まで（同条第4項第1号、第77条第5項で準用）。\n'
         '問題文の表から 386.30㎡ の甲2の公差 1.85㎡ を読む（準則第72条第1項）。→ 申請するのは土地分筆登記だけ',
         ha='center', va='center', fontsize=16)
fig.text(0.5, 0.05, '分筆後の地積　丙区画135.84㎡ ＋ 乙区画126.84㎡ ＋ 甲区画123.21㎡ ＝ 385.89㎡（宅地は小数第2位未満切捨て）',
         ha='center', va='center', fontsize=15, color=GRAY)
path = os.path.join(OUT, 'R3_dai21mon_zu17_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図7: 数直線（固定配置）\n  →', path)

# =====================================================================
# zu18 申請人の関係図
# =====================================================================
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問3　申請人は「二郎が一郎と三郎に代位」', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
box(33, 84, 34, 11, BLACK, '#f4f4f4')
ax.text(50, 92, '被相続人　山田太郎', ha='center', va='center', fontsize=19, weight='bold')
ax.text(50, 87, '本件土地（10番1）の所有権の登記名義人　令和3年3月1日死亡', ha='center', va='center', fontsize=13)
for x in (17, 50, 83):
    ax.annotate('', xy=(x, 70), xytext=(50 if x == 50 else (40 if x < 50 else 60), 83),
                arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.6, mutation_scale=18))
ax.text(14, 80, '相続（相続人は3名のみ）', ha='center', va='center', fontsize=14, color=GRAY)
for x, name, addr, ku, role, col, fc in [
    (3, '山田一郎', 'M市D町五丁目2番2号', '甲区画 → 10番8', '被代位者', GRAY, '#f4f4f4'),
    (36, '山田二郎', 'K市D町二丁目10番1号', '乙区画 → 10番1', '申請人兼代位者', RED, '#fff1f1'),
    (69, '山田三郎', 'S市D町一丁目3番5号', '丙区画 → 10番9', '被代位者', GRAY, '#f4f4f4'),
]:
    box(x, 44, 28, 25, col, fc)
    ax.text(x + 14, 64, name, ha='center', va='center', fontsize=20, weight='bold')
    ax.text(x + 14, 58, addr, ha='center', va='center', fontsize=14)
    ax.text(x + 14, 52, f'遺産分割：{ku}', ha='center', va='center', fontsize=14)
    ax.text(x + 14, 46.5, role, ha='center', va='center', fontsize=17, weight='bold', color=col)
for x0, x1 in [(35.5, 32.0), (64.5, 68.0)]:
    ax.annotate('', xy=(x1, 56), xytext=(x0, 56), arrowprops=dict(arrowstyle='-|>', color=RED, lw=2.4,
                                                                    mutation_scale=22))
ax.text(33.8, 60, '代位', ha='center', va='bottom', fontsize=14, color=RED, weight='bold')
ax.text(66.2, 60, '代位', ha='center', va='bottom', fontsize=14, color=RED, weight='bold')
box(3, 6, 94, 30, RED, 'white', lw=1.6)
ax.text(6, 32, '申請書の申請人の欄', ha='left', va='center', fontsize=16, weight='bold', color=RED)
ax.text(10, 26, '（被相続人　山田太郎）', ha='left', va='center', fontsize=16)
ax.text(10, 20.5, '被代位者　　　　相続人　M市D町五丁目2番2号　山田一郎', ha='left', va='center', fontsize=16)
ax.text(10, 16, '　　　　　　　　　　　　S市D町一丁目3番5号　山田三郎', ha='left', va='center', fontsize=16)
ax.text(10, 11.5, '申請人兼代位者　　　　K市D町二丁目10番1号　山田二郎', ha='left', va='center', fontsize=16)
ax.text(10, 7.5, '代位原因　令和3年8月1日遺産分割の所有権移転登記請求権', ha='left', va='center', fontsize=16)
fig.text(0.5, 0.045, '分筆の申請人は登記名義人（法第39条第1項）→ 死亡したので相続人（法第30条）。二郎1人で申請するので一郎・三郎の分は代位。\n'
         '申請情報に代位者である旨・被代位者の氏名住所・代位原因（令第3条第4号）。添付：相続証明書（令第7条第1項第4号）・代位原因証書（同項第3号）',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R3_dai21mon_zu18_dai_kankei.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図8: 説明図（固定配置）\n  →', path)

# =====================================================================
# zu19 相続を証する情報
# =====================================================================
# ---- zu19：問3 相続を証する情報が要る理由（相続の登記が未了） ----
fig, ax = board(9)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('問3　相続を証する情報が要るか　相続による所有権の登記が申請より前に済んでいるか', fontsize=23, weight='bold', y=0.965)
ax.add_patch(Rectangle((30, 74), 40, 16, facecolor='#f4f4f4', edgecolor=BLACK, lw=2.0))
ax.text(50, 85, '本件土地（10番1）の登記名義人', ha='center', va='center', fontsize=16, weight='bold')
ax.text(50, 79, '山田太郎（令和3年3月1日死亡）', ha='center', va='center', fontsize=15)
ax.annotate('', xy=(22, 62), xytext=(40, 73.5), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=2.0, mutation_scale=20))
ax.annotate('', xy=(78, 62), xytext=(60, 73.5), arrowprops=dict(arrowstyle='-|>', color=RED, lw=2.4, mutation_scale=20))
ax.text(8, 67, '済んでいる場合', fontsize=15, color=GRAY, weight='bold')
ax.text(80, 68, '済んでいない場合\n（本問）', fontsize=15, color=RED, weight='bold', va='center')
ax.add_patch(Rectangle((2, 22), 44, 38, facecolor='#f4f4f4', edgecolor=GRAY, lw=1.8))
ax.text(24, 54, '名義人は相続人本人', ha='center', va='center', fontsize=17, weight='bold', color=GRAY)
ax.text(24, 41, '名義人本人の申請になるので、\n相続を証する情報は要らない', ha='center', va='center', fontsize=15, color=GRAY, linespacing=1.6)
ax.add_patch(Rectangle((54, 22), 44, 38, facecolor='#fff1f1', edgecolor=RED, lw=2.2))
ax.text(76, 54, '甲区は山田太郎のまま', ha='center', va='center', fontsize=17, weight='bold', color=RED)
ax.text(76, 40, '相続人が名義人の立場を引き継いで\n申請する（法第30条）ので、\n相続を証する情報が要る\n（令第7条第1項第4号）', ha='center', va='center', fontsize=15,
        linespacing=1.6)
ax.text(2, 12, '時系列：3月1日 死亡 → 8月1日 遺産分割 → 10月17日 申請。二郎が遺産分割に基づく登記（所有権の移転）を受けるのは、この分筆が済んでから。',
        fontsize=14.5, va='center')
ax.text(2, 5, '添付書類は「相続証明書」（答案用紙の欄の名前は「添付書類」なので「〜書」で書く）。', fontsize=14.5, va='center', color=RED, weight='bold')
fig.text(0.5, 0.035, '今は法定相続情報一覧図の写しか法定相続情報番号の提供で代えることもできる（不動産登記規則第37条の3第1項。出題当時は制度がなかった）。',
         ha='center', fontsize=14)
put_board(fig, 'R3_dai21mon_zu19_sozoku_hantei.png')

# =====================================================================
# zu20 区画と地番
# =====================================================================
fig, (ax,) = new_figure('問3　分筆後の区画と地番（10番1 → 10番1・10番8・10番9）',
                        '予定地番：乙区画が10番1のまま（イ）、甲区画が10番8（ロ）、丙区画が10番9（ハ）。\n'
                        '二郎の乙区画は地番が変わらない（10番1のまま）。甲区画と丙区画には新しい地番が付く（問題文の〔分筆の登記の予定地番〕）。')
z = Zu(ax)
fit(ax, ZEN, margin=0.12, pad_aspect=True)
z.poly(HEI, fill=GREEN)
z.poly(OTSU, fill=BLUE)
z.poly(KOU, fill=ORANGE)
z.north_arrow()
z.free_text(centroid(HEI), '（ハ）10番9\n135.84㎡\n三郎', fs=17)
z.free_text(centroid(OTSU), '（イ）10番1\n126.84㎡\n二郎', fs=17)
z.free_text(centroid(KOU), '（ロ）10番8\n123.21㎡\n一郎', fs=17)
for p, n in [(H, 'H'), (I, 'I'), (J, 'J'), (K, 'K'), (L, 'L'), (F, 'F'), (D, 'D'), (B, 'B'), (C, 'C')]:
    z.point(p, 'dot', size=6)
    z.point_label(p, n, away=cz)
ALL_PROBLEMS += save(fig, [z], 'R3_dai21mon_zu20_bunpitsu_chiban.png')

# =====================================================================
# zu21 分筆前の行の地積
# =====================================================================
# ---- zu21：問3 分筆前の行の地積は登記記録のまま（386.30） ----
fig, ax = board(8.5)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('問3　土地の表示の1行目（分筆前）の地積は、計算した385.89ではなく登記記録の386.30', fontsize=23, weight='bold', y=0.965)
ax.add_patch(Rectangle((2, 55), 40, 30, facecolor='#eef4fb', edgecolor=BLUE, lw=2.0))
ax.text(22, 80, '登記記録（問題文の現在事項）', ha='center', va='center', fontsize=16, weight='bold', color=BLUE)
ax.text(22, 69, '10番1　宅地　386.30㎡', ha='center', va='center', fontsize=19, weight='bold')
ax.text(22, 59.5, 'これを土地の表示の1行目に写す', ha='center', va='center', fontsize=14)
ax.add_patch(Rectangle((58, 55), 40, 30, facecolor='#f4f4f4', edgecolor=GRAY, lw=1.8))
ax.text(78, 80, '分筆後の3区画の面積の合計', ha='center', va='center', fontsize=16, weight='bold', color=GRAY)
ax.text(78, 69, '135.84 ＋ 126.84 ＋ 123.21 ＝ 385.89㎡', ha='center', va='center', fontsize=17, color=GRAY)
ax.text(78, 59.5, '公差の判断に使う数字（申請書には書かない）', ha='center', va='center', fontsize=14, color=GRAY)
ax.text(50, 70, '≠', ha='center', va='center', fontsize=30, color=RED, weight='bold')
ax.text(2, 46, '申請書の土地の表示（1行目と、各区画の行の地積の出どころ）', fontsize=15, weight='bold', va='center')
xs_, ws_ = [2, 26, 50, 74], [24, 24, 24, 24]
for x, w, t_, fc in zip(xs_, ws_, ['行', '③地積', '出どころ', '原因の欄'], ['#eeeeee'] * 4):
    cell(ax, x, 36, w, 7, t_, fs=14, fc=fc, weight='bold')
for r, (a_, b_, c_, d_, col) in enumerate([('1行目　10番1', '386.30', '登記記録', '空欄', RED),
                                            ('（イ）', '126.84', '座標法で計算', '③10番1、10番8、10番9に分筆', BLACK),
                                            ('（ロ）10番8', '123.21', '座標法で計算', '10番1から分筆', BLACK),
                                            ('（ハ）10番9', '135.84', '座標法で計算', '10番1から分筆', BLACK)]):
    y = 29 - r * 7
    fc = '#fff1f1' if col == RED else 'white'
    for x, w, t_ in zip(xs_, ws_, [a_, b_, c_, d_]):
        cell(ax, x, y, w, 7, t_, fs=13 if len(t_) < 14 else 11.5, fc=fc, color=col, weight='bold' if col == RED else 'normal')
fig.text(0.5, 0.035, '分筆前の行は、分筆する前の土地の表示（登記記録のまま）。地積更正をしない場合は、分筆前の地積を測量の値に直さない。', ha='center', fontsize=15)
put_board(fig, 'R3_dai21mon_zu21_chiseki_zenmae.png')

# =====================================================================
# zu22 辺長
# =====================================================================
# ---- zu22：問4 辺長11本の計算と端数処理（すべて Abs(p − q)。軸に平行な辺はない） ----
import math as _mm
fig, ax = board(11.5)
fig.suptitle('問4　辺長11本は、すべて Abs（点 − 点）で出して小数第3位を四捨五入', fontsize=24, weight='bold', y=0.965)
cols = [(2, 8, '辺'), (10, 30, '電卓の式'), (40, 24, '表示（小数第5位以下は略）'), (64, 14, '書く値'), (78, 20, '備考')]
for x, w, t_ in cols:
    cell(ax, x, 90, w, 6, t_, fs=13.5, fc='#eeeeee', weight='bold')
NOTE22 = {'DL': '切り上がる', 'JF': '切り上がる', 'BC': '切り捨て（隅切長3.00と一致）', 'IJ': '分筆線', 'KL': '分筆線', 'FH': '10番2の図と一致'}
for r, (nm, (p, q, want)) in enumerate(SIDES.items()):
    raw = abs(p - q)
    trunc = _mm.floor(raw * 1e4) / 1e4
    y = 83.6 - r * 6.4
    hi = nm in ('DL', 'JF', 'BC')
    fc = '#fff1f1' if hi else 'white'
    col = RED if hi else BLACK
    cell(ax, 2, y, 8, 6.4, nm, fs=14, fc=fc, color=col, weight='bold')
    cell(ax, 10, y, 30, 6.4, f'Abs({nm[0]} − {nm[1]})', fs=14, fc=fc)
    cell(ax, 40, y, 24, 6.4, f'{trunc:.4f}…', fs=14, fc=fc)
    cell(ax, 64, y, 14, 6.4, want, fs=15, fc=fc, color=col, weight='bold')
    cell(ax, 78, y, 20, 6.4, NOTE22.get(nm, ''), fs=11.5 if len(NOTE22.get(nm, '')) > 8 else 12.5, fc=fc, color=col)
assert f'{_mm.floor(abs(D - L) * 1e4) / 1e4:.4f}' == '8.4984' and f'{_mm.floor(abs(J - F) * 1e4) / 1e4:.4f}' == '8.4984'
assert f'{_mm.floor(abs(B - C) * 1e4) / 1e4:.4f}' == '3.0016'
fig.text(0.5, 0.035, '今年は軸に平行な辺がないので、引き算では出ない。座標は問題文の注3で丸めた値を使い、辺長は問題文の注4で小数第3位を四捨五入する。',
         ha='center', fontsize=14.5)
put_board(fig, 'R3_dai21mon_zu22_hencho.png')

# =====================================================================
# zu23 書くもの・書かないもの
# =====================================================================
# ---- zu23：問4 地積測量図に書くもの・書かないもの ----
fig, ax = board(10)
fig.suptitle('問4　地積測量図に書くもの・書かないもの・描かない点', fontsize=24, weight='bold', y=0.965)
for x, w, hd, col, fc, items in [
        (2, 31, '書く', BLUE, '#eef4fb',
         ['地番（10番1、10番8、10番9）', '土地の所在（K市D町二丁目）', '辺長11本（分筆線を含む）', '（イ）10－1　（ロ）10－8　（ハ）10－9', '境界標の記号',
          '方位（答案用紙に印刷がない）', '隣接地の地番（10－2・10－3・10－4）と道路', '基準点T1・T2の位置と点名', '「（単位：ｍ）」']),
        (35, 31, '書かない', RED, '#fff1f1',
         ['各筆界点の座標値', '平面直角座標系の番号', '地積とその求積方法', '測量年月日　（以上4つは問題文の注5）', 'T1・T2の座標値（問題文の注6）',
          '作成者・申請人（答案用紙に「（略）」の印刷）', '縮尺（答案用紙に1／250の印刷）']),
        (68, 30, '描かない点', GRAY, '#f4f4f4',
         ['A点：道路境界の点で、本件土地の筆界点ではない', 'G点：A・Bの延長とD・Cの延長の交点（仮想の点）', 'E点：杭はH点の位置に移した'])]:
    ax.add_patch(Rectangle((x, 8), w, 80, facecolor=fc, edgecolor=col, lw=2.0))
    ax.text(x + w / 2, 83, hd, ha='center', va='center', fontsize=20, weight='bold', color=col)
    for k, it in enumerate(items):
        ax.text(x + 1.5, 74 - k * 7.4, '・' + it, ha='left', va='center', fontsize=12.5 if len(it) > 16 else 14, linespacing=1.4)
fig.text(0.5, 0.035, '境界標：B・C・D はK市金属標（道路境界の調査の結果）、F・H・I・J・K・L はコンクリート杭（境界標の状況に関する調査、立会い等のウ）。', ha='center', fontsize=14.5)
put_board(fig, 'R3_dai21mon_zu23_kaku_kakanai.png')

# =====================================================================
# zu24 作図の範囲
# =====================================================================
# ---- zu24：問4 作図の範囲（T1・T2まで入れる。問題文の注5・注6） ----
PTS_ALL = [T1, T2, B, C, D, F, H, I, J, K, L]   # 地積測量図に描く点（A・G・Eは描かない）
ew = max(p.imag for p in PTS_ALL) - min(p.imag for p in PTS_ALL)
ns = max(p.real for p in PTS_ALL) - min(p.real for p in PTS_ALL)
assert round(ew * 4) == 126 and round(ns * 4) == 89, (ew, ns)
fig, ax = board(9)
ax.set_position([0.03, 0.10, 0.94, 0.80])
fig.suptitle('問4　今年だけの注（問題文の注5・問題文の注6）と、T1・T2まで入れた作図の範囲', fontsize=24, weight='bold', y=0.965)
ax.add_patch(Rectangle((2, 50), 46, 40, facecolor='#fff1f1', edgecolor=RED, lw=2.0))
ax.text(25, 85, '問題文の注5　書かないもの', ha='center', va='center', fontsize=18, weight='bold', color=RED)
ax.text(5, 69, '・各筆界点の座標値\n・平面直角座標系の番号\n・地積とその求積方法\n・測量年月日', ha='left', va='center', fontsize=16, linespacing=1.7)
ax.add_patch(Rectangle((52, 50), 46, 40, facecolor='#eef4fb', edgecolor=BLUE, lw=2.0))
ax.text(75, 85, '問題文の注6　K市基準点（T1・T2）', ha='center', va='center', fontsize=18, weight='bold', color=BLUE)
ax.text(55, 69, '・図に位置を明示して点名を付ける\n・座標値は書かなくてよい\n　→　T1・T2は省略せずに描く', ha='left', va='center', fontsize=16, linespacing=1.7)
ax.add_patch(Rectangle((2, 4), 96, 40, facecolor='white', edgecolor=BLACK, lw=1.6))
ax.text(50, 39, '作図の範囲（T1・T2まで入れて描く）', ha='center', va='center', fontsize=19, weight='bold')
ax.text(6, 29, f'東西：T1（Y 500.00）〜 T2（Y 531.50）　約{ew:.0f}m　→　1/250（1m ＝ 4mm）で約126mm', ha='left', va='center', fontsize=16)
ax.text(6, 20, f'南北：T2（X 496.77）〜 F（X 518.95）　約{ns:.0f}m　→　1/250で約89mm', ha='left', va='center', fontsize=16)
ax.text(6, 10, '答案用紙の第4欄の枠（横約30cm・縦約23cm）に収まるので、基準点を省略せずに描ける', ha='left', va='center', fontsize=16, color=RED, weight='bold')
fig.text(0.5, 0.035, '問題文の注1〜4と問題文の注7は毎年ほとんど同じ注（注の仕分けの図を参照）。今年だけの問題文の注5・問題文の注6が「書く・書かない」を決める。',
         ha='center', fontsize=15)
put_board(fig, 'R3_dai21mon_zu24_sakuzu_hanni.png')

# =====================================================================
# zu25 地積測量図
# =====================================================================
# ---- zu25：問4 地積測量図の完成見本（答案用紙の第4欄の枠の中に、縮尺1/250の実際の大きさで描く） ----
#   用紙の外枠・図を描く枠・地番と土地の所在の欄・作成者と申請人の欄・縮尺の欄の位置は、試験の答案用紙の原本（touan_youshi/）の
#   2ページ目のPDFの罫線から測った値（原本の用紙の左上が原点。mm）。黒は印刷済み、青は書き込み。画像の中に図番は入れない
ORIG_FRAME_MM = (80.6, 25.8, 382.6, 256.8)     # 図を描く枠（x0, y0, x1, y1。横302mm・縦231mm）
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
ftext(59.0, 17.6, '第4欄', fs=15, ha='left', weight='bold')
frect(*ORIG_FRAME_MM, lw=1.8)                                  # 図を描く枠（横302mm・縦231mm）
fline(231.6, 25.8, 231.6, 35.8)                                # 折り目の印（上・下）
fline(231.6, 246.8, 231.6, 256.8)
frect(240.6, 15.8, 302.6, 25.8)                                # 地番の欄
fline(264.6, 15.8, 264.6, 25.8)
ftext(252.6, 20.8, '地　　番', fs=12)
ftext(283.6, 20.8, '10番1、10番8、10番9', fs=10.5, color=INK, weight='bold')
frect(240.6, 25.8, 382.6, 35.8)                                # 土地の所在の欄
fline(264.6, 25.8, 264.6, 35.8)
ftext(252.6, 30.8, '土地の所在', fs=12)
ftext(268.0, 30.8, 'Ｋ市Ｄ町二丁目', fs=15, ha='left', color=INK, weight='bold')
ftext(342.6, 20.8, '地　積　測　量　図', fs=19)
frect(80.6, 256.8, 223.6, 271.3)                               # 作成者の欄
fline(99.6, 256.8, 99.6, 271.3)
ftext(90.1, 264.0, '作 成 者', fs=11)
ftext(161.6, 262.0, '（略）', fs=13)
ftext(221.0, 268.8, '（令和３年○月○日作成）', fs=11, ha='right')
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
         '書くもの：地番（10番1、10番8、10番9）、土地の所在（Ｋ市Ｄ町二丁目）、辺長11本、（イ）（ロ）（ハ）の符号と地番、境界標の記号、方位記号（印刷されていないので必ず描く）、\n'
         '隣接地の地番、基準点T1・T2の位置と点名（問題文の注6）。書かないもの：座標値・座標系の番号・地積と求積方法・測量年月日（問題文の注5）。A点・G点・E点は描かない。',
         ha='center', va='center', fontsize=13, linespacing=1.6)
ax = fig.add_axes([fx3(80.6), fy3(256.8), fx3(382.6) - fx3(80.6), fy3(25.8) - fy3(256.8)])
fw_m = (ORIG_FRAME_MM[2] - ORIG_FRAME_MM[0]) / 4               # 枠の中の東西（Y）の長さ（m）75.5
fh_m = (ORIG_FRAME_MM[3] - ORIG_FRAME_MM[1]) / 4               # 南北（X）の長さ（m）57.75
c3 = P((min(p.real for p in PTS_ALL) + max(p.real for p in PTS_ALL)) / 2, (min(p.imag for p in PTS_ALL) + max(p.imag for p in PTS_ALL)) / 2)
fit(ax, [c3 + P(-fh_m / 2, -fw_m / 2), c3 + P(fh_m / 2, fw_m / 2)], margin=0.0, pad_aspect=True)
assert abs(((ax.get_xlim()[1] - ax.get_xlim()[0]) - fw_m)) < 0.05, ax.get_xlim()
z = Zu(ax, fontsize=15)
fit(ax, [c3 + P(-fh_m / 2, -fw_m / 2), c3 + P(fh_m / 2, fw_m / 2)], margin=0.0, pad_aspect=True)
z.poly(ZEN, lw=2.0)
z.line(I, J, lw=2.0)
z.line(K, L, lw=2.0)
z.line(F, F + (F - H) * 0.20, color=BLACK, lw=1.2)
z.line(F, F + (F - D) * 0.15, color=BLACK, lw=1.2)
z.line(H, H + (H - B) * 0.12, color=BLACK, lw=1.2)
z.line(D, D + (D - C) * 0.25, color=BLACK, lw=1.2)
z.north_arrow()
for n, (p, q, s) in SIDES.items():
    if n == 'IJ':
        z.edge_label(p, q, s, centroid(HEI), fs=15, outward=True, ts=(0.25, 0.2, 0.3))
    elif n == 'KL':
        z.edge_label(p, q, s, centroid(OTSU), fs=15, outward=True, ts=(0.25, 0.2, 0.3))
    else:
        z.edge_label(p, q, s, cz, fs=15)
z.free_text(centroid(HEI), '（ハ）\n10－9', fs=17)
z.free_text(centroid(OTSU), '（イ）\n10－1', fs=17)
z.free_text(centroid(KOU), '（ロ）\n10－8', fs=17)
for p, n in [(F, 'F'), (H, 'H'), (I, 'I'), (J, 'J'), (K, 'K'), (L, 'L')]:
    z.point(p, 'concrete')
    z.point_label(p, n, away=cz)
for p, n in [(B, 'B'), (C, 'C'), (D, 'D')]:
    z.point(p, 'metal', size=9)
    z.point_label(p, n, away=cz)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=cz)
z.edge_label(F, H, '10－2', cz, fs=16, dists=(45, 58), rotate=False)
z.edge_label(J, L, '10－4', cz, fs=16, dists=(40, 52), rotate=False)
z.edge_label(I, K, '道路', cz, fs=16, dists=(45, 58), rotate=False)
z.edge_label(C, D, '道路', cz, fs=16, dists=(45, 58), rotate=False)
z.free_text(F, '10－3', fs=16, offsets=((-45, 30), (-60, 20), (-60, 40)))
z.free_text(P(c3.real - fh_m / 2 + 8.0, c3.imag - fw_m / 2 + 1.5), '（単位：ｍ）\n◎ コンクリート杭：F・H・I・J・K・L\n● 金属標：B・C・D\n△ 基準点：T1・T2', fs=13,
            ha='left', va='bottom', offsets=((0, 0), (0, 30), (0, 60)))
ALL_PROBLEMS += save(fig, [z], 'R3_dai21mon_zu25_chiseki_sokuryouzu.png')

# =====================================================================
# zu26 本番の解く順番
# =====================================================================
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('本番の解く順番（時間を食う計算を後ろへ）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.80])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
STEPS = [
    ('1', '問2の穴埋め', '条文の知識だけ（登記所・位置・形状・地番・閉鎖・永久）', GRAY, '#f4f4f4'),
    ('2', '申請書の計算の要らない欄', '登記の目的・添付書類・登録免許税・申請人の欄（代位）・所在・地番・地目・\n登記原因・分筆前の行の386.30', GRAY, '#f4f4f4'),
    ('3', 'A点 → H点', '放射（時計回り）と交点の比。FH 15.16・高さ 4.73 で検算　［時間を食う］', RED, '#fff1f1'),
    ('4', 'C点', '隅切り（GB＝GC＝2.1224…、BC＝3.00で検算）', GRAY, '#f4f4f4'),
    ('5', 'L点 → 3区画の面積 → 公差', '交点の比 → 135.84・126.84・123.21 → 差0.41 ≦ 1.85 → 地積の欄　［時間を食う］', RED, '#fff1f1'),
    ('6', '地積測量図', '辺長11本・境界標・T1とT2（1/250で約126mm×約89mm）', GRAY, '#f4f4f4'),
]
y = 92
for num, head, body, ec, fc in STEPS:
    box(4, y - 11, 92, 11, ec, fc, lw=2.0)
    ax.text(8, y - 5.5, num, ha='center', va='center', fontsize=26, weight='bold', color=ec)
    ax.text(12, y - 3.3, head, ha='left', va='center', fontsize=19, weight='bold')
    ax.text(12, y - 8.0, body, ha='left', va='center', fontsize=14, linespacing=1.3)
    if num != '6':
        ax.annotate('', xy=(50, y - 13.5), xytext=(50, y - 11.6),
                    arrowprops=dict(arrowstyle='-|>', color=BLACK, lw=1.8, mutation_scale=16))
    y -= 15.2
fig.text(0.5, 0.045, 'A点は本件土地の筆界点ではなく、H点を出すためだけに使う点。L点が出なくても、申請書は3つの地積以外を全部書ける\n'
         '（丙区画の地積はH点があれば出せる）。代位の申請人の欄を先に書いておけば、計算で詰まっても点が残る。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R3_dai21mon_zu26_kaku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 図12: 流れ図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
