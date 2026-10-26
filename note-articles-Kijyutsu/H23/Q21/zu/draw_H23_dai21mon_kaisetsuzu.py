"""平成23年度 第21問（土地）会話形式note記事の解説図25枚を、座標値から作図する。

`../prompt_H23_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
参照実装は `../../../H28/Q21/zu/draw_H28_dai21mon_kaisetsuzu.py`。

B点は問題文で座標が「省略」されている（計算には使わない）。51番3の形を示す図だけ、51番3の地積測量図の三斜
（21.70 × 14.51）とABとEMの平行から逆算した参考の位置 B_REF に置き、図の中で「参考の位置」と明記する。
神楽殿・参道・社殿・社務所は座標がないので描かない（文字で示すだけ）。

実行: python3 note-articles-Kijyutsu/H23/Q21/zu/draw_H23_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, dms, to_dms, area, chiseki, radial  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文のA市基準点成果表・測量によって得られた座標、記事で求めた点） ------------------
T1, T2, T3 = P(309.14, 292.20), P(300.12, 306.99), P(299.47, 333.78)
D, E, F, G = P(320.31, 309.24), P(326.52, 315.34), P(323.58, 334.66), P(302.56, 332.88)
I, J, L = P(312.05, 313.06), P(303.18, 315.34), P(303.65, 302.14)
A = r2(radial(T1, T2, 15.120, dms(150, 21, 44)))
M = r2(radial(T1, T2, 6.613, dms(324, 2, 29)))
K = r2(radial(T2, T3, 5.067, dms(319, 7, 54)))
C = r2(M + (E - M) * 157.3309 / 364.4865)
PX = E - 9.732                                             # E→J（真南）とD→Hの交点
H = r2(PX + cmath.rect(6.836, dms(120)))
B_REF = A + (E - M) * 314.867 / 364.4865                   # B点（座標は省略。三斜から逆算した参考の位置）
# 誤りの点
AW = r2(T1 + cmath.rect(15.120, cmath.phase(T2 - T1) - dms(150, 21, 44)))   # 反時計回り
MW = r2(T1 + cmath.rect(6.613, cmath.phase(T2 - T1) - dms(324, 2, 29)))
KW = r2(T2 + cmath.rect(5.067, cmath.phase(T3 - T2) - dms(319, 7, 54)))
CW = r2(M + (E - M) / abs(E - M) * 10.05)                  # ブロック塀の10.05mで置いた誤り
HW = r2(D + cmath.rect(6.836, dms(120)))                   # Dから6.836mと読んだ誤り

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, got, want in [('A', A, P(309.60, 277.09)), ('M', M, P(309.67, 298.79)), ('K', K, P(303.34, 310.90)),
                     ('C', C, P(316.94, 305.93)), ('H', H, P(313.37, 321.26)), ('AW', AW, P(322.37, 284.87)),
                     ('MW', MW, P(303.04, 294.75)), ('KW', KW, P(296.71, 310.74)), ('CW', CW, P(316.84, 305.83)),
                     ('HW', HW, P(316.89, 315.16))]:
    assert abs(got - want) < 1e-9, (n, got, want)
assert abs(PX - P(316.788, 315.34)) < 1e-9
assert f'{abs(M - A):.2f}' == '21.70' and f'{abs(B_REF - M):.2f}' == '16.27'
assert f'{abs(((M - A).conjugate() * (B_REF - A)).imag) / abs(M - A):.2f}' == '14.51'
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731  辺長（小数第3位四捨五入）
SIDES = [(C, D, '4.72'), (D, H, '13.88'), (H, J, '11.78'), (J, K, '4.44'), (K, I, '8.97'), (I, C, '8.65')]
for p, q, want in SIDES:
    assert d2(p, q) == want, (p, q, d2(p, q), want)
assert f'{abs(C - M):.4f}'[:7] == '10.1898'
HONKEN = [C, D, H, J, K, I]                  # 本件土地（申請地）
# 本件土地はくの字（Iが凹んだ角）なので、重心が区画の外（Iの近く）に来る。内側の代表点はIとHの中点にする
INNER = (I + H) / 2
N51_3 = [A, B_REF, C, M]                     # 51番3（Bは参考の位置）
N51_2 = [M, C, I, K, L]                      # 51番2
N50_1 = [E, F, G, J, H, D]                   # 50番1
assert f'{area(HONKEN):.3f}' == '113.875' and chiseki(area(HONKEN), False) == 113
assert f'{area([CW, D, H, J, K, I]):.3f}' == '114.479' and chiseki(area([CW, D, H, J, K, I]), False) == 114
assert f'{abs(((E - M).conjugate() * (A - M)).imag):.4f}' == '364.4865'
BRG_T2_T1 = math.degrees(cmath.phase(T2 - T1))             # T1→T2 121°22′40.17″
BRG_T3_T2 = math.degrees(cmath.phase(T3 - T2))             # T2→T3 91°23′23.58″
assert to_dms(math.radians(BRG_T2_T1)) == '121°22′40.17″' and to_dms(math.radians(BRG_T3_T2)) == '91°23′23.58″'
assert to_dms(cmath.phase(E - M)) == '44°29′07.37″' and to_dms(cmath.phase(M - A)) == '89°48′54.63″'
assert to_dms(cmath.phase(PX - D)) == '120°00′04.14″'
assert f'{abs(HW - PX):.2f}' == '0.21'
# 誤りの点の向き：AWは直線ABより西（51番3の北西の外）、KWはT2より南、MWはA→Mの線より6m以上南
t = (AW.real - A.real) / (B_REF.real - A.real)
assert AW.imag < (A + (B_REF - A) * t).imag
assert KW.real < T2.real and M.real - MW.real > 6
print('数値の照合: すべて一致')


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


def wrap_caption(text, n=60):
    """説明文は1行 n 字までにし、「。」「、」の後ろで折り返す（図の端に接しないように）。"""
    out = []
    for line in text.split('\n'):
        while len(line) > n:
            cut = max(line.rfind('。', 0, n), line.rfind('、', 0, n))
            cut = cut + 1 if cut > 20 else n
            out.append(line[:cut])
            line = line[cut:]
        out.append(line)
    return '\n'.join(out)


_new_figure = new_figure


def new_figure(title, caption, *args, **kwargs):   # noqa: F811  座標の図の説明文も、図の端に接しないように折り返す
    return _new_figure(title, wrap_caption(caption, 66), *args, **kwargs)


def fixed_figure(title, caption):
    setup_font()
    f = plt.figure(figsize=(16, 12), dpi=100)
    f.patch.set_facecolor('white')
    f.suptitle(title, fontsize=24, weight='bold', y=0.965)
    a = f.add_axes([0.03, 0.10, 0.94, 0.80])
    a.set_xlim(0, 100)
    a.set_ylim(0, 100)
    a.axis('off')
    f.text(0.5, 0.04, wrap_caption(caption), ha='center', va='center', fontsize=16, linespacing=1.5)
    return f, a


def bearing(p, q):
    """pからqへの方向角（北から時計回り、度。0〜360）。"""
    b = math.degrees(cmath.phase(q - p))
    return b + 360 if b < 0 else b


def box(ax, x, y, w, hh, head, col, lines, red=(), fs=16, step=5.4, fc='#f7f7f7'):
    """整理図の枠（左上に見出し、その下に行）。red の番号の行は赤で書く。"""
    ax.add_patch(FancyBboxPatch((x, y), w, hh, boxstyle='round,pad=0.6', fc=fc, ec=col, lw=2.0))
    ax.text(x + 2, y + hh - 4, head, fontsize=20, weight='bold', va='center', color=col)
    for i, t in enumerate(lines):
        ax.text(x + 3, y + hh - 11 - i * step, t, fontsize=fs, va='center', color=RED if i in red else BLACK)


KIND = {'A': 'metal', 'L': 'metal', 'J': 'metal', 'K': 'metal', 'B': 'stone', 'E': 'stone', 'F': 'stone', 'G': 'stone',
        'M': 'stone', 'C': 'concrete', 'D': 'concrete', 'H': 'concrete', 'I': 'concrete'}
ALL_PROBLEMS = []

# =====================================================================
# 時系列（第1章。固定配置）
# =====================================================================
fig, ax = fixed_figure('全体の時系列（日付の順）',
                       '昭和26年8月19日に買い受けて所有の意思をもって占有を始め、20年後の昭和46年8月19日に取得時効が完成。申請は平成23年8月21日（答案用紙に印刷済み）。')
JIKEIRETSU = [
    ('大正以前', '今の社殿より20mほど南に小さな社があり、周りは一面の畑', GRAY),
    ('昭和初期から', '本件土地も含めて神社の敷地として維持・管理し、一般に開放\n（50番1・51番2を買い受けるまでは、地主から借りて使っていた）', GRAY),
    ('昭和26年8月19日', '雨堤天満宮が50番1と51番2を吉川仁志から買い受ける\n（その後、神楽殿を建て、参道を整備した）', RED),
    ('昭和46年8月19日', '取得時効が完成（A財務事務所の書面の「時効完成年月日」）', RED),
    ('平成23年6月10日', '代表役員がA財務事務所に取得時効の手続をする\n（後日、所有権を有することを証する書面が交付された）', BLACK),
    ('平成23年8月10日', '測量', BLACK),
    ('平成23年8月21日', '申請（答案用紙に印刷済み）', BLACK)]
ax.plot([29, 29], [8, 92], color=GRAY, lw=3, zorder=1)
for k, (d, ev, col) in enumerate(JIKEIRETSU):
    y = 90 - k * 13.2
    ax.plot([29], [y], 'o', ms=13, color=col, zorder=3)
    ax.text(26.5, y, d, ha='right', va='center', fontsize=19, weight='bold', color=col)
    ax.text(32, y, ev, ha='left', va='center', fontsize=16, color=BLACK, linespacing=1.5)
path = os.path.join(OUT, 'H23_dai21mon_zu01_jikeiretsu.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 時系列: 整理図（固定配置）\n  →', path)

# =====================================================================
# 注の仕分け（第1章。固定配置）
# =====================================================================
fig, ax = fixed_figure('注の仕分け（問題文の注1〜7と、番号のない説明文）',
                       '毎年ほとんど同じ注は流し読みでよい。今年だけの問題文の注4〜6は、答案のどこかに必ず効く。番号のない説明文も注として拾う。')
box(ax, 3, 4, 46, 88, '毎年ほとんど同じ注（流し読み）', GRAY,
    ['問題文の注1', '座標値は小数第3位を四捨五入し、小数第2位まで', '', '問題文の注2', '訂正・加入・削除をしたときは、押印や字数を書かない', '',
     '問題文の注3', '地積測量図の辺長は小数第3位を四捨五入し、小数第2位まで', '（各筆界点の座標値・系の番号・求積方法・地積は省略してよい）', '',
     '問題文の注7', '申請は書面を提出する方法で行う'], fs=15, step=5.6)
box(ax, 52, 36, 45, 56, '今年だけの注（答案に効く）', RED,
    ['問題文の注4　T2・T3を地積測量図に描き、', '　名称と座標値を書く　→　問4の地積測量図', '',
     '問題文の注5　申請を受ける登記所と法人の登記を', '　受けた登記所は同一　→　問3の添付書類', '　（今の法令では会社法人等番号）', '',
     '問題文の注6　近傍類似の地図の縮尺は500分の1', '　→　問4の土地所在図'], red=[1, 4, 5, 8], fs=15, step=5.2, fc='#fff5f5')
box(ax, 52, 4, 45, 28, '番号のない説明文', BLUE,
    ['見取図の下：A点からM点までは境界標、', '　T1〜T3はA市基準点', '51番3の地積測量図の「※」：', '　辺長の記載はあるが省略している'], fs=15, step=5.2)
path = os.path.join(OUT, 'H23_dai21mon_zu02_chuu_shiwake.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 注の仕分け: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図1：全体像（北を上にして座標どおりに描き直した見取図）
# =====================================================================
fig, (ax,) = new_figure('北を上にして描き直した全体像',
                        'E→Jは真南（Y座標が同じ315.34）。C・DはE→Mの直線の上、J・KはG→Lの直線の上。ABとEMは平行。\n'
                        'B点は座標が省略されているので、51番3の地積測量図の三斜から逆算した参考の位置（灰色の破線）に置いた。')
z = Zu(ax, fontsize=14)
fit(ax, [T1, T2, T3, A, B_REF, E, F, G, L, M], margin=0.06, pad_aspect=True)
z.poly(N50_1, fill=BLUE)
z.poly(N51_2, fill=ORANGE)
z.poly(HONKEN, fill=GREEN, lw=2.6)
z.poly([M, A, B_REF, C], color=GRAY, lw=1.6, ls='--', fill=PURPLE, closed=False)
z.line(D, E, color=BLACK, lw=2.0)
z.line(E, J, color=GRAY, lw=1.3, ls=':')
z.line(A, M, color=BLACK, lw=2.0)
z.north_arrow()
z.callout(INNER + P(-4.0, -0.8), '本件土地（無番地）', dirs=(-100, -80, -120), color=GREEN, fs=15, dists=(160, 185, 210))
z.free_text(centroid(N50_1) + P(2, 3), '50番1\n雨堤天満宮', fs=15, offsets=((0, 0), (0, 16), (16, 0)))
z.free_text(centroid(N51_2), '51番2', fs=15, offsets=((0, 0), (0, -14), (-14, 0)))
z.free_text(centroid(N51_3), '51番3\n（駐車場）', fs=15, offsets=((0, 0), (0, -14), (14, 0)))
for p, n, ref in [(A, 'A', centroid(N51_3)), (M, 'M', centroid(N51_2)), (L, 'L', centroid(N51_2)),
                  (C, 'C', INNER), (D, 'D', INNER), (H, 'H', INNER),
                  (J, 'J', INNER), (K, 'K', INNER), (I, 'I', INNER),
                  (E, 'E', centroid(N50_1)), (F, 'F', centroid(N50_1)), (G, 'G', centroid(N50_1))]:
    z.point(p, KIND[n], color=RED if n in 'CH' else BLACK)
    z.point_label(p, n, away=ref, color=RED if n in 'CH' else BLACK)
z.point(B_REF, 'stone', color=GRAY)
z.callout(B_REF, 'B（参考の位置）', dirs=(90, 60, 120), color=GRAY, dists=(40, 55, 70))
for p, n in [(T1, 'T1'), (T2, 'T2'), (T3, 'T3')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=p + P(1, 0))
z.free_text(P(301.3, 322.0), '道　路', fs=15, color=GRAY, offsets=((0, 0), (0, -12), (20, 0)))
z.free_text(P(327.5, 305.0), '50－2', fs=14, color=GRAY, offsets=((0, 0), (0, 14), (-16, 0)))
z.free_text(P(327.8, 326.0), '48－5', fs=14, color=GRAY, offsets=((0, 0), (0, 14), (16, 0)))
z.free_text(P(313.0, 336.4), '49－1', fs=14, color=GRAY, offsets=((0, 0), (16, 0), (0, 14)))
z.callout(E + (J - E) * 0.5, 'E→Jは真南', dirs=(0, 20, -20), color=GRAY, dists=(55, 75, 95))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu03_zentaizu.png')


# =====================================================================
# 図2〜図4：放射（点ごとに1枚）
# =====================================================================
def housha_figure(no, name, title, caption, station, back, pt, wrong, dist, obs, fit_pts, bg_lines, st_name, bk_name,
                  pt_name, r, wrong_dirs, pt_dirs, extra=None):
    fig, (ax,) = new_figure(title, caption)
    z = Zu(ax, fontsize=14)
    fit(ax, fit_pts, margin=0.10, pad_aspect=True)
    for p, q in bg_lines:
        z.line(p, q, color=GRAY, lw=1.4)
    b_back = bearing(station, back)
    z.line(station, back, color=BLUE, lw=1.8)
    z.line(station, station + P(r * 1.45, 0), color=GRAY, lw=1.2, ls='--')
    z.line(station, pt, color=RED, lw=2.8)
    z.line(station, wrong, color=GRAY, lw=1.4, ls='--')
    z.angle_arc(station, r * 0.55, 0, b_back, color=BLUE)
    z.angle_arc(station, r, b_back, b_back + obs, color=RED)
    if extra:
        extra(z)
    z.north_arrow()
    z.point(station, 'kijun')
    z.point(back, 'kijun')
    z.point_label(back, bk_name, away=station)
    z.point_label(station, st_name, away=pt)
    z.point(pt, 'dot', color=RED, size=10)
    z.callout(pt, f'{pt_name}（{pt.real:.2f}, {pt.imag:.2f}）', dirs=pt_dirs, color=RED, dists=(50, 70, 90, 110))
    z.point(wrong, 'dot', color=GRAY, size=8)
    z.callout(wrong, f'反時計回りの誤り（{wrong.real:.2f}, {wrong.imag:.2f}）', dirs=wrong_dirs, color=GRAY,
              dists=(45, 65, 85, 105))
    z.edge_label(station, pt, f'{dist}', station + (back - station) * 0.3, color=RED, fs=15)
    return fig, z


fig, z = housha_figure(
    2, 'A', 'A点の求め方（T1からT2を後視して放射）',
    'T1→T2の方向角 121°22′40.17″ に、T2の方向から時計回りの観測角 150°21′44″ を足して 271°44′24.17″（真数表の1°44′24″＝271°44′24″ − 270°）。\n'
    '15.120m進んでA（309.60, 277.09）。反時計回りに引くと（322.37, 284.87）で、51番3のA→Bの線より北西の外に出る。',
    T1, T2, A, AW, '15.12', 150 + 21 / 60 + 44 / 3600, [T1, T2, A, AW, M, B_REF, P(304.5, 292.2)],
    [(A, M), (A, B_REF)], 'T1', 'T2', 'A', 3.2, (60, 30, 90, 120), (-100, -130, -70, -150))
z.free_text(T1 + P(1.4, 1.2), '方向角 121°22′40.17″', color=BLUE, fs=14, ha='left', offsets=((10, 10), (20, 30), (30, 0)))
z.free_text(T1 + P(-3.4, -2.0), '観測角 150°21′44″（時計回り）', color=RED, fs=14, offsets=((0, -20), (0, -40), (-40, -20)))
z.free_text(A + (B_REF - A) * 0.5 + (M - A) * 0.25, '51番3', color=GRAY, fs=14, offsets=((0, 0), (20, -10), (-20, 10), (30, -30)))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu04_A_housha.png')


def extra_m(z):
    z.line(A, M, color=GREEN, lw=2.2)
    z.point(A, 'metal')
    z.point_label(A, 'A', away=A + P(1, 1))
    z.edge_label(A, M, 'AM ＝ 21.70（51番3の地積測量図の底辺と一致）', A + P(5, 5), color=GREEN, fs=14,
                 ts=(0.32, 0.4, 0.25), dists=(12, 18, 26))


fig, z = housha_figure(
    3, 'M', 'M点の求め方（T1からT2を後視して放射）',
    'T1→T2の方向角 121°22′40.17″ ＋ 観測角 324°02′29″ ＝ 445°25′09.17″（360°を引いた85°25′09.17″と同じ向き。真数表の85°25′09″）。\n'
    '6.613m進んでM（309.67, 298.79）。AM ＝ 21.70 で51番3の地積測量図の底辺と一致。反時計回りだと（303.04, 294.75）でA→Mの線より6m以上南。',
    T1, T2, M, MW, '6.613', 324 + 2 / 60 + 29 / 3600, [T1, T2, M, MW, A, P(313.5, 299.0)],
    [], 'T1', 'T2', 'M', 2.4, (-60, -30, -90, 180), (60, 30, 90), extra=extra_m)
z.free_text(T1 + P(1.3, 1.6), '方向角\n121°22′40.17″', color=BLUE, fs=14, ha='left', offsets=((12, 10), (24, 24), (30, 0)))
z.free_text(T1 + P(2.8, -1.8), '観測角 324°02′29″（時計回り）', color=RED, fs=14, offsets=((0, 18), (0, 36), (-30, 20)))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu05_M_housha.png')


def extra_k(z):
    z.line(L, G, color=BLACK, lw=1.8)
    for p, n in [(L, 'L'), (J, 'J'), (G, 'G')]:
        z.point(p, KIND[n])
        z.point_label(p, n, away=p + P(-1, 0))
    z.free_text(L + (G - L) * 0.70, 'G→Lの直線（道路境界）', fs=14, offsets=((0, 18), (0, 30), (0, -18)))


fig, z = housha_figure(
    4, 'K', 'K点の求め方（T2からT3を後視して放射）',
    '器械点が変わったので、後視の向きはT2→T3の 91°23′23.58″ で取り直す。観測角 319°07′54″ を足して 410°31′17.58″（＝50°31′17.58″。真数表の50°31′18″）。\n'
    '5.067m進んでK（303.34, 310.90）。Conjg(L − G) × (K − G) ＝ 676.5154 ＋ 0.019i で、KはG→Lの直線の上。反時計回りだと（296.71, 310.74）で道路の向こう。',
    T2, T3, K, KW, '5.067', 319 + 7 / 60 + 54 / 3600, [T2, T3, K, KW, L, G, P(305.5, 306.0)],
    [], 'T2', 'T3', 'K', 2.2, (-60, -30, -90, 180), (60, 90, 120), extra=extra_k)
z.free_text(T2 + P(1.6, 2.6), '方向角 91°23′23.58″', color=BLUE, fs=14, ha='left', offsets=((12, 6), (26, 20), (40, 0)))
z.free_text(T2 + P(-2.4, -1.8), '観測角 319°07′54″（時計回り）', color=RED, fs=14, offsets=((0, -16), (-20, -30), (0, -40)))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu06_K_housha.png')

# =====================================================================
# 図5：問2 C点（高さが同じ三角形の面積の比）
# =====================================================================
fig, (ax,) = new_figure('問2　C点の求め方（51番3の地積測量図の三斜と、ABとEMの平行）',
                        'BはA→Bの直線、CはM→Eの直線の上。ABとEMは平行なので、△BMC（底辺MC）と△AME（底辺ME）の高さは同じ h。\n'
                        'MC ÷ ME ＝ △BMCの倍面積 ÷ △AMEの倍面積 ＝ (16.27 × 9.67) ÷ 364.4865 ＝ 157.3309 ÷ 364.4865。\n'
                        'C ＝ M ＋ (E − M) × 157.3309 ÷ 364.4865 ＝ （316.94, 305.93）。検算：BM ＝ 16.2681… → 16.27（三斜の対角線と一致）')
z = Zu(ax, fontsize=14)
fit(ax, [A, B_REF, E, M, C, D], margin=0.08, pad_aspect=True)
z.poly([A, M, E], color=BLUE, lw=1.2, fill=BLUE, alpha=0.14)
z.poly([B_REF, M, C], color=RED, lw=1.2, fill=RED, alpha=0.22)
z.line(A, B_REF, color=BLACK, lw=2.2)
z.line(M, E, color=BLACK, lw=2.2)
z.line(B_REF, C, color=BLACK, lw=1.6, ls='--')
z.parallel_chevron(A, B_REF, size=0.9)
z.parallel_chevron(M, E, size=0.9)
foot_h = M + (E - M) * (((E - M).conjugate() * (B_REF - M)).real / abs(E - M) ** 2)   # BからMEへの垂線の足（MとEの間）
assert 0 < ((E - M).conjugate() * (B_REF - M)).real / abs(E - M) ** 2 < 1
z.line(B_REF, foot_h, color=PURPLE, lw=1.6, ls='--')
z.right_angle(foot_h, E, B_REF, size=0.7, color=PURPLE)
foot_c = M + (B_REF - M) * (((B_REF - M).conjugate() * (C - M)).real / abs(B_REF - M) ** 2)
z.line(C, foot_c, color=GRAY, lw=1.4, ls=':')
foot_b = A + (M - A) * (((M - A).conjugate() * (B_REF - A)).real / abs(M - A) ** 2)
z.line(B_REF, foot_b, color=GRAY, lw=1.4, ls=':')
z.north_arrow()
for p, n in [(A, 'A'), (M, 'M'), (E, 'E'), (D, 'D')]:
    z.point(p, KIND[n])
    z.point_label(p, n, away=centroid([A, M, E]))
z.point(B_REF, 'stone', color=GRAY)
z.point_label(B_REF, 'B（参考）', away=centroid([A, M, E]), color=GRAY)
z.point(C, 'dot', color=RED, size=10)
z.callout(C, 'C（316.94, 305.93）', dirs=(-40, -20, -60, 0), color=RED, dists=(60, 80, 100))
z.edge_label(A, M, '21.70', centroid([A, B_REF, M]), fs=14)
z.edge_label(B_REF, M, '16.27', A, fs=14, outward=True)
z.callout(foot_h + (B_REF - foot_h) * 0.7, 'h（ABとEMの間の幅）', dirs=(60, 80, 40, 100), color=PURPLE, dists=(60, 80, 100))
z.edge_label(C, foot_c, '9.67', M, color=GRAY, fs=13, outward=False, ts=(0.5, 0.35, 0.65))
z.edge_label(B_REF, foot_b, '14.51', M, color=GRAY, fs=13, outward=True, ts=(0.5, 0.35, 0.65))
z.callout(centroid([B_REF, M, C]), '△BMC　16.27 × 9.67 ＝ 157.3309', dirs=(-25, -35, -45, -15), color=RED, dists=(260, 300, 340, 380))
z.callout(centroid([A, M, E]) + P(-1.5, -2.5), '△AMEの倍面積\n364.4865', dirs=(-100, -120, -80), color=BLUE, dists=(70, 90, 110))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu07_C_menseki_hi.png')

# =====================================================================
# 図6：C点の比較（ブロック塀の10.05m ⇔ 地積測量図から出したC）
# =====================================================================
fig, (ax1, ax2) = new_figure('問2　C点はブロック塀の10.05mで置かない',
                             'ブロック塀・賃貸借契約書の図面の10.05mで置いたC′（316.84, 305.83）は、51番3の地積測量図から出したC（316.94, 305.93）よりMに0.14m寄る。\n'
                             '本件土地の面積：Cなら113.875 → 113㎡、C′なら114.479 → 114㎡（境内地は1㎡未満切捨て）。',
                             ncols=2, width_ratios=[1.1, 0.9])
za = Zu(ax1, fontsize=14)
fit(ax1, [M, E, C, D, H, J, K, I, L], margin=0.08, pad_aspect=True)
za.poly(HONKEN, fill=GREEN)
za.line(M, C, color=BLACK, lw=2.0)
za.line(D, E, color=BLACK, lw=2.0)
za.poly([M, L, K], color=BLACK, lw=1.4, closed=False)
za.north_arrow()
for p, n in [(M, 'M'), (E, 'E'), (D, 'D'), (H, 'H'), (J, 'J'), (K, 'K'), (I, 'I'), (L, 'L')]:
    za.point(p, KIND[n])
    za.point_label(p, n, away=INNER if n not in 'ML' else centroid(N51_2))
za.point(C, 'dot', color=RED, size=9)
za.point_label(C, 'C', away=INNER, color=RED)
za.callout(P(313.8, 316.0), '本件土地\nCなら 113.875 → 113㎡\nC′なら 114.479 → 114㎡', dirs=(60, 45, 75, 30), fs=14, dists=(110, 130, 150, 170))
za.edge_label(M, C, 'MC ＝ 10.19', centroid(N51_2), fs=14, color=RED)
za.free_text(centroid(N51_2), '51番2', fs=14, color=GRAY, offsets=((0, -20), (0, -34), (-20, -20)))
zb = Zu(ax2, fontsize=14)
ctr = (C + CW) / 2
fit(ax2, [ctr + P(-0.35, -0.35), ctr + P(0.35, 0.35)], margin=0.02, pad_aspect=True)
u = (E - M) / abs(E - M)
zb.line(ctr - u * 0.45, ctr + u * 0.45, color=BLACK, lw=2.0)
zb.north_arrow()
zb.point(C, 'dot', color=RED, size=12)
zb.callout(C, 'C（316.94, 305.93）\n地積測量図から', dirs=(-40, -20, -60), color=RED, dists=(55, 75, 95))
zb.point(CW, 'dot', color=GRAY, size=12)
zb.callout(CW, 'C′（316.84, 305.83）\nブロック塀の10.05m', dirs=(140, 160, 120), color=GRAY, dists=(55, 75, 95))
zb.free_text((C + CW) / 2, '0.14m', color=RED, fs=16, offsets=((-30, 18), (-40, 24), (30, -18)))
zb.free_text(ctr + u * 0.38, 'Eへ', fs=14, offsets=((14, -6), (20, -14)))
zb.free_text(ctr - u * 0.38, 'Mへ', fs=14, offsets=((14, -6), (20, -14)))
ax2.set_title('Cのまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H23_dai21mon_zu08_C_hikaku.png')

# =====================================================================
# 図7：C点の別解（真数表の45°19′48″・三斜の角度）
# =====================================================================
fig, (ax,) = new_figure('問2　C点の別解（真数表の角度と三斜の角度）',
                        '真数表：M→E 44°29′07″、A→M 89°48′55″、その差45°19′48″が直線AMと直線MEのはさむ角。\n'
                        'h ＝ 21.70 × 0.71116 ＝ 15.4321…、MC ＝ 157.3309 ÷ 15.4321… ＝ 10.1949…。\n'
                        '三斜の角度：∠AMB 約63°06′（14.51 ÷ 16.27 から）、∠AME ＝ 180° − 45°19′48″ ＝ 134°40′12″、∠BMC 約71°34′。\n'
                        'MC ＝ 9.67 ÷ sin 約71°34′ ＝ 10.1929…。'
                        'どの解き方でも、丸めるとC（316.94, 305.93）。本番は Conjg の面積の比がいちばん速い。')
z = Zu(ax, fontsize=14)
fit(ax, [M + P(-3.2, -9.5), M + P(9.5, 9.0), C, B_REF], margin=0.05, pad_aspect=True)
z.line(M, M + (A - M) / abs(A - M) * 9.0, color=BLACK, lw=2.0)
z.line(M, M + (E - M) / abs(E - M) * 12.0, color=BLACK, lw=2.0)
z.line(M, B_REF, color=GRAY, lw=1.6, ls='--')
z.line(C, foot_c, color=RED, lw=1.6, ls='--')
z.right_angle(foot_c, M, C, size=0.5, color=RED)
b_ma, b_mb, b_me = bearing(M, A), bearing(M, B_REF), bearing(M, E) + 360
z.angle_arc(M, 1.4, b_ma, b_mb, color=BLUE)
z.angle_arc(M, 2.3, b_mb, b_me, color=RED)
z.angle_arc(M, 3.3, b_ma, b_me, color=PURPLE, arrow=False)
z.north_arrow()
z.point(M, 'stone')
z.point_label(M, 'M', away=M + P(1, 1))
z.point(C, 'dot', color=RED, size=10)
z.callout(C, 'C（316.94, 305.93）', dirs=(0, -20, 20), color=RED, dists=(55, 75, 95))
z.point(B_REF, 'stone', color=GRAY)
z.point_label(B_REF, 'B（参考）', away=M, color=GRAY)
z.free_text(M + (A - M) / abs(A - M) * 7.5, 'Aへ（A→M 89°48′55″）', fs=14, offsets=((0, 18), (0, 30), (20, 18)))
z.free_text(M + (E - M) / abs(E - M) * 11.0, 'Eへ（M→E 44°29′07″）', fs=14, ha='right', offsets=((-16, 6), (-24, 14), (-16, -12)))
z.callout(M + cmath.rect(1.4, math.radians(90 - (b_ma + b_mb) / 2)).conjugate() * 1j, '∠AMB 約63°06′', dirs=(-150, -170, -130),
          color=BLUE, dists=(60, 80, 100))
z.callout(M + cmath.rect(2.3, math.radians(90 - (b_mb + b_me) / 2)).conjugate() * 1j, '∠BMC 約71°34′', dirs=(100, 120, 80),
          color=RED, dists=(60, 80, 100))
z.callout(M + cmath.rect(3.3, math.radians(90 - (b_ma + b_me) / 2 - 20)).conjugate() * 1j, '∠AME 134°40′12″\n（180° − 45°19′48″）',
          dirs=(160, 180, 140), color=PURPLE, dists=(60, 80, 100))
z.edge_label(C, foot_c, '9.67', M, color=RED, fs=14, outward=False)
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu09_C_betsukai.png')

# =====================================================================
# 図8：問2 H点（E→Jは真南、交点から120°の向きに6.836m）
# =====================================================================
fig, (ax1, ax2) = new_figure('問2　H点の求め方（E→Jの真南の線とD→Hの交点から6.836m）',
                             'E − J ＝ 23.34（iの係数0）でE→Jは真南。交点はEのX座標から9.732引いた（316.788, 315.34）。arg(交点 − D) ＝ 120°00′04.14″ で120°の線の上。\n'
                             'H ＝ E − 9.732 ＋ 6.836∠120° ＝ （313.37, 321.26）。6.836mをDから測った誤りの点は（316.89, 315.16）で、交点から0.21mしか離れない。',
                             ncols=2, width_ratios=[1.25, 0.75])
za = Zu(ax1, fontsize=14)
fit(ax1, [C, D, E, H, J, K, I], margin=0.08, pad_aspect=True)
za.poly(HONKEN, color=GRAY, lw=1.4, fill=GREEN, alpha=0.12)
za.line(E, J, color=BLUE, lw=1.8, ls='--')
za.line(D, E, color=BLACK, lw=1.8)
za.line(D, H, color=RED, lw=2.6)
za.line(D, D + P(3.2, 0), color=GRAY, lw=1.2, ls='--')
za.angle_arc(D, 1.6, 0, 120, color=RED)
za.north_arrow()
for p, n in [(D, 'D'), (E, 'E'), (J, 'J'), (C, 'C'), (K, 'K'), (I, 'I')]:
    za.point(p, KIND[n])
    za.point_label(p, n, away=INNER)
za.point(PX, 'dot', color=BLUE, size=8)
za.callout(PX, '交点（316.788, 315.34）', dirs=(20, 40, 0), color=BLUE, dists=(60, 80, 100))
za.point(H, 'dot', color=RED, size=10)
za.callout(H, 'H（313.37, 321.26）', dirs=(-60, -80, -40, -100), color=RED, dists=(45, 60, 75, 90))
za.edge_label(E, PX, '9.732', D, color=BLUE, fs=14, outward=True)
za.edge_label(PX, H, '6.836', J, color=RED, fs=14, outward=True)
za.free_text(D + P(1.9, 0.6), '120°', color=RED, fs=15, offsets=((14, 8), (24, 14), (30, 0), (20, 26)))
za.callout(E + (J - E) * 0.8, 'E→Jは真南\nE − J ＝ 23.34', dirs=(0, 20, -20), color=BLUE, dists=(55, 75, 95))
zb = Zu(ax2, fontsize=14)
fit(ax2, [PX + P(-0.55, -0.55), PX + P(0.55, 0.55)], margin=0.02, pad_aspect=True)
zb.line(PX + P(0.5, 0), PX + P(-0.5, 0), color=BLUE, lw=1.8, ls='--')
u = cmath.rect(1, dms(120))
zb.line(PX - u * 0.9, PX + u * 0.5, color=RED, lw=2.2)
zb.north_arrow()
zb.point(PX, 'dot', color=BLUE, size=10)
zb.callout(PX, '交点', dirs=(40, 60, 20), color=BLUE, dists=(50, 70))
zb.point(HW, 'dot', color=GRAY, size=11)
zb.callout(HW, 'Dから6.836mと\n読んだ誤り\n（316.89, 315.16）', dirs=(-100, -120, -80, -140), color=GRAY, dists=(60, 80, 100, 120))
zb.free_text((HW + PX) / 2, '0.21m', color=RED, fs=15, offsets=((0, 28), (-10, 36), (10, 40), (0, 50)))
zb.free_text(PX + u * 0.42, 'Hへ', color=RED, fs=14, offsets=((10, 10), (18, 16)))
ax2.set_title('交点のまわりの拡大', fontsize=17, weight='bold', pad=6)
ALL_PROBLEMS += save(fig, [za, zb], 'H23_dai21mon_zu10_H_kousa.png')

# =====================================================================
# 図9：問1 民法第162条第1項（20年）か第2項（10年）か（固定配置）
# =====================================================================
fig, ax = fixed_figure('問1　民法第162条第1項の20年か、第2項の10年か',
                       '時効完成年月日は占有開始年月日からちょうど20年。善意・無過失を裏付ける事実は問題文にないので、民法第162条第1項で書く。')
box(ax, 4, 52, 44, 40, '第1項（20年）　本問はこちら', RED,
    ['二十年間、所有の意思をもって、', '平穏に、かつ、公然と', '他人の物を占有した者', '→ 善意・無過失は要らない'], red=[3])
box(ax, 52, 52, 44, 40, '第2項（10年）', GRAY,
    ['十年間、所有の意思をもって、', '平穏に、かつ、公然と他人の物を占有', '＋ 占有の開始の時に、善意であり、', '　 かつ、過失がなかった'])
box(ax, 4, 6, 44, 40, '問題文の事実', RED,
    ['A財務事務所の書面', '占有開始年月日　昭和26年8月19日', '時効完成年月日　昭和46年8月19日', '→ ちょうど20年（第1項に当てはまる）'], red=[3],
    fc='#fff5f5')
box(ax, 52, 6, 44, 40, '問題文にない事実', GRAY,
    ['善意・無過失を裏付ける事実は', '問題文のどこにも書いていない', '→ 書いていない事実を答案で作らない', '→ 第2項（10年）では書かない'])
for xx, col in [(26, RED), (74, GRAY)]:
    ax.annotate('', xy=(xx, 51.0), xytext=(xx, 47.5), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=col))
path = os.path.join(OUT, 'H23_dai21mon_zu11_jikou_1kou_2kou.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 整理図（固定配置）\n  →', path)

# =====================================================================
# 占有の開始（第5章。固定配置）
# =====================================================================
fig, ax = fixed_figure('問1　占有の開始は昭和26年8月19日（借りて使っていた間は所有の意思がない）',
                       '時効の起算日は、所有の意思をもって占有を始めた昭和26年8月19日。昭和初期から数えると20年を超えるが、借りていた間は他人の物として使う占有。')
TL = [(10, '昭和初期〜', '地主から借りて\n神社の敷地に使う', GRAY), (36, '昭和26年8月19日', '50番1・51番2を買い受け\n占有開始（起算日）', RED),
      (62, '昭和46年8月19日', '取得時効の完成', RED), (86, '平成23年6月10日', '時効取得の手続\n（A財務事務所）', BLACK)]
ax.annotate('', xy=(97, 84), xytext=(3, 84), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, head, body, col in TL:
    ax.plot([x], [84], 'o', ms=12, color=col)
    ax.text(x, 90, head, ha='center', fontsize=17, weight='bold', color=col)
    ax.text(x, 77, body, ha='center', va='top', fontsize=15, color=BLACK)
ax.annotate('', xy=(61, 66), xytext=(37, 66), arrowprops=dict(arrowstyle='<|-|>', lw=2.0, color=RED))
ax.text(49, 62.5, '20年間', ha='center', fontsize=17, color=RED, weight='bold')
box(ax, 4, 6, 44, 42, '昭和初期〜昭和26年8月18日', GRAY,
    ['地主から借りて、神社の敷地として使う', '→ 他人の物として使う占有', '→ 「所有の意思」がない', '→ 20年に数えない'], red=[2])
box(ax, 52, 6, 44, 42, '昭和26年8月19日〜', RED,
    ['50番1と51番2を買い受ける', '自分の神社の敷地として本件土地も使う', '→ 所有の意思をもつ占有の開始', '→ ここから20年（起算日）'], red=[2, 3], fc='#fff5f5')
path = os.path.join(OUT, 'H23_dai21mon_zu12_senyu_kaishi.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 占有の開始: 整理図（固定配置）\n  →', path)

# =====================================================================
# 要件と問題文の事実（第5章。固定配置）
# =====================================================================
fig, ax = fixed_figure('問1　答案は「要件の言葉」と「問題文の事実」を4組そろえる',
                       '要件の言葉だけ、事実だけでは点にならない。4つの要件のどれにも、問題文の事実を添えて書く（民法第162条第1項）。')
REQ = [('他人の物', '本件土地は国有財産で、雨堤天満宮の物ではない（A財務事務所で確認）'),
       ('所有の意思', '50番1と51番2を買い受けてから、神社の敷地（神楽殿の敷地・参道）として\n維持・管理している'),
       ('平穏かつ公然', '一般に開放し、神楽殿を建て、参道を整備した。\n土地の所有に関する問合せや、それに伴う測量もなかった'),
       ('20年間の継続', '昭和26年8月19日から昭和46年8月19日まで、20年間占有を続けた')]
ax.text(4, 93, '要件の言葉', fontsize=19, weight='bold', color=RED, va='center')
ax.text(30, 93, '問題文の事実', fontsize=19, weight='bold', color=BLACK, va='center')
for k, (req, fact) in enumerate(REQ):
    y = 78 - k * 20
    ax.add_patch(FancyBboxPatch((3, y - 8), 94, 16, boxstyle='round,pad=0.5', fc='#f7f7f7', ec=RED, lw=2.0))
    ax.text(6, y, req, fontsize=21, weight='bold', va='center', color=RED)
    ax.text(30, y, fact, fontsize=17, va='center', color=BLACK, linespacing=1.6)
path = os.path.join(OUT, 'H23_dai21mon_zu13_jikou_youken.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 要件と事実: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図11：問3 申請する登記（地積の更正ではなく土地表題登記）
# =====================================================================
fig, (ax1, ax2) = new_figure('問3　50番1の地積の更正ではなく、土地表題登記',
                             '50番1の筆界はD→H→J。本件土地はその外にある国有の無番地の土地なので、地積の更正では50番1に取り込めない。\n'
                             '本件土地だけで1筆の土地として土地表題登記（不動産登記法第36条）をし、所有権の保存の登記（同法第74条第1項第1号）につなげる。',
                             ncols=2, width_ratios=[1.0, 1.0])
z = Zu(ax1, fontsize=14)
fit(ax1, N50_1 + HONKEN + N51_2, margin=0.08, pad_aspect=True)
z.poly(N50_1, fill=BLUE)
z.poly(N51_2, fill=ORANGE)
z.poly(HONKEN, fill=GREEN, lw=2.2)
z.poly([D, H, J], color=RED, lw=4.0, closed=False)
z.north_arrow()
for p, n in [(D, 'D'), (H, 'H'), (J, 'J')]:
    z.point(p, KIND[n], color=RED)
    z.point_label(p, n, away=INNER, color=RED)
for p, n in [(C, 'C'), (K, 'K'), (I, 'I')]:
    z.point(p, KIND[n])
    z.point_label(p, n, away=INNER)
z.free_text(centroid(N50_1) + P(1.5, 2.0), '50番1\n雨堤天満宮', fs=15, offsets=((0, 0), (0, 16), (16, 0)))
z.free_text(centroid(N51_2), '51番2', fs=15, offsets=((0, 0), (0, -14), (-14, 0)))
z.callout(INNER + P(-3.5, -0.8), '本件土地\n国有・無番地・登記なし', dirs=(-125, -115, -135), color=GREEN, fs=15,
          dists=(150, 170, 190))
z.callout(D + (H - D) * 0.45, '50番1の筆界 D→H→J', dirs=(60, 40, 80), color=RED, fs=15, dists=(90, 110, 130))
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 100)
ax2.axis('off')
box(ax2, 4, 56, 92, 38, '50番1の地積の更正　→　誤り', GRAY,
    ['筆界はそのままで、', '登記記録の地積の誤りを直す登記', '筆界D→H→Jの外の本件土地は', '50番1に入らない'], step=6.4)
box(ax2, 4, 4, 92, 46, '土地表題登記　→　正しい', RED,
    ['表題登記がない土地の所有権を', '取得した者が申請（不動産登記法第36条）', '雨堤天満宮が表題部所有者になり、', '所有権の保存の登記へ',
     '（同法第74条第1項第1号）'], red=[0, 1], step=6.4, fc='#fff5f5')
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu14_hyoudai_touki.png')

# =====================================================================
# 図12：問3 地目は境内地（固定配置）
# =====================================================================
fig, ax = fixed_figure('問3　地目は境内地（宅地・公衆用道路ではない）',
                       '神楽殿の敷地も参道も、神社の境内に属する土地なので境内地（不動産登記事務取扱手続準則第68条第13号）。')
box(ax, 3, 50, 29, 42, '宅地（第3号）', GRAY, ['建物の敷地及び', 'その維持若しくは効用を', '果すために必要な土地'])
box(ax, 35.5, 50, 29, 42, '公衆用道路（第21号）', GRAY, ['一般交通の用に供する道路', '（道路法による道路で', 'あるかどうかを問わない）'])
box(ax, 68, 50, 29, 42, '境内地（第13号）', RED, ['境内に属する土地であって、', '宗教法人法第3条第2号', '及び第3号に掲げる土地'], red=[0],
    fc='#fff5f5')
ax.text(50, 96.5, '不動産登記事務取扱手続準則第68条（地目の定め方）', ha='center', va='center', fontsize=18, color=BLACK)
box(ax, 3, 6, 94, 36, '本件土地は？', GREEN,
    ['神楽殿（神社の建物）がある一画の土地と、参道 → どちらも神社の境内に属する土地', '→ 地目は境内地（1筆の土地に地目は1つ）',
     '神楽殿が建っていても宅地にしない。神社の参道を公衆用道路にしない'], red=[1], step=7.0)
path = os.path.join(OUT, 'H23_dai21mon_zu15_chimoku_keidaichi.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 整理図（固定配置）\n  →', path)

# =====================================================================
# 図13：問3 本件土地の面積と地目
# =====================================================================
fig, (ax,) = new_figure('問3　本件土地の面積と地目（境内地・1㎡未満切捨て）',
                        'C→D→H→J→K→Iを座標法で：倍面積 227.75 → 113.875㎡。境内地（準則第68条第13号）は宅地ではないので1㎡未満を切り捨てて113㎡。\n'
                        '宅地と誤ると113.87、ブロック塀の10.05mでCを置くと114.479 → 114㎡。')
z = Zu(ax, fontsize=14)
fit(ax, HONKEN + [T2, P(322.5, 322.0)], margin=0.08, pad_aspect=True)
z.poly(HONKEN, fill=GREEN, lw=2.6)
z.line(D, E, color=GRAY, lw=1.4)
z.line(M, C, color=GRAY, lw=1.4)
z.line(K, L, color=GRAY, lw=1.4)
z.line(J, G + (J - G) * 0.6, color=GRAY, lw=1.4)
z.north_arrow()
for p, n in [(C, 'C'), (D, 'D'), (H, 'H'), (J, 'J'), (K, 'K'), (I, 'I')]:
    z.point(p, KIND[n])
    z.point_label(p, n, away=INNER)
z.free_text(INNER, '本件土地\n113.875㎡\n→ 113㎡', fs=17, color=GREEN, weight='bold',
            offsets=((0, 0), (0, -16), (10, 0)))
z.callout(I + (K - I) * 0.3, '神楽殿の敷地と参道\n＝ 境内地', dirs=(180, 160, -160), color=BLACK, dists=(90, 110, 130))
z.callout(H + (J - H) * 0.5, '宅地なら 113.87（誤り）', dirs=(0, 20, -20), color=GRAY, dists=(70, 90, 110))
z.callout(C, 'C′（ブロック塀）なら\n114.479 → 114㎡（誤り）', dirs=(150, 170, 130), color=GRAY, dists=(70, 90, 110))
for p, q, n in SIDES:
    z.edge_label(p, q, n, INNER, fs=13)
z.free_text(P(301.5, 316.0), '道　路', fs=15, color=GRAY, offsets=((0, 0), (0, -12), (20, 0)))
z.free_text(P(318.0, 322.5), '50－1', fs=14, color=GRAY, offsets=((0, 0), (0, 14), (16, 0)))
ALL_PROBLEMS += save(fig, [z], 'H23_dai21mon_zu16_menseki_chimoku.png')

# =====================================================================
# 図14：問3 登記原因は不詳（取得原因と登記原因）（固定配置）
# =====================================================================
fig, ax = fixed_figure('問3　登記原因は「不詳」（取得原因の「時効取得」ではない）',
                       '取得原因（時効取得）と表題登記の登記原因（土地が生じた原因）を一緒にしない。時効取得は所有権証明書で示す。')
box(ax, 4, 38, 44, 54, '表題登記の登記原因及びその日付', RED,
    ['＝ 土地が生じた原因とその日付', '例：公有水面を埋め立てた土地は', '　「何年何月何日公有水面埋立」', '本件土地は大正より前からある土地。',
     'いつ・どうしてできたか分からない', '→「不詳」'], red=[5])
box(ax, 52, 38, 44, 54, '所有権の取得原因', BLUE,
    ['昭和26年8月19日時効取得', '（時効の効力は起算日にさかのぼる。', '　民法第144条）', '→ 申請書の登記原因には書かない',
     '→ 所有権を有することを証する情報', '　（不動産登記令別表4の項添付情報欄ハ）'], red=[3])
box(ax, 4, 6, 92, 24, '申請書では', GREEN,
    ['登記原因及びその日付：不詳', '添付書類：所有権証明書（A財務事務所の「取得時効が成立し、所有権を有することを証する書面」）'],
    red=[0], step=6.0)
path = os.path.join(OUT, 'H23_dai21mon_zu17_touki_genin.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 整理図（固定配置）\n  →', path)

# =====================================================================
# 添付書類（第6章。固定配置）
# =====================================================================
fig, ax = fixed_figure('問3　添付書類は今の法令で会社法人等番号（資格証明書・住所証明書は付けない）',
                       '会社法人等番号を提供すると、代表者の資格を証する情報も住所を証する情報も要らない。本試験の年の問題文の注5が今の法令でも意味を持つかを確かめてから書く。')
box(ax, 3, 52, 46, 41, '今の法令の答え（赤）', RED,
    ['土地所在図　地積測量図', '所有権証明書　会社法人等番号', '代理権限証書'], red=[1], step=6.5, fc='#fff5f5')
box(ax, 51, 52, 46, 41, '会社法人等番号を提供すると', BLUE,
    ['代表者の資格を証する情報は要らない', '（不動産登記令第7条第1項第1号イ）', '住所を証する情報も要らない',
     '（不動産登記令第9条、不動産登記規則第36条第4項）'], step=6.5)
box(ax, 3, 6, 46, 41, '藍子の誤答（住所証明書・資格証明書）', GRAY,
    ['住所証明書を付ける', '資格証明書を付ける', '→ 出題当時の法令の書き方', '→ 今の法令では付けない'], red=[3], step=6.5)
box(ax, 51, 6, 46, 41, '出題当時（平成27年11月施行の前）', GRAY,
    ['会社法人等番号の制度がなく、', '住所証明書を付けた', '資格証明書は、問題文の注5', '（登記所が同一）で付けなくてよかった'], step=6.5)
for xx in (26, 74):
    ax.annotate('', xy=(xx, 49.5), xytext=(xx, 51.5), arrowprops=dict(arrowstyle='-|>', lw=2.0, color=GRAY))
path = os.path.join(OUT, 'H23_dai21mon_zu18_tenpu_shorui.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 添付書類: 整理図（固定配置）\n  →', path)

# =====================================================================
# 申請書の残りの欄（第6章。固定配置）
# =====================================================================
fig, ax = fixed_figure('問3　残りの欄の書き方（地番・所在・申請人・登録免許税）',
                       '地番は登記官が付けるので空欄、所在は地番区域まで。申請人は法人なので代表者の氏名も書く。登録免許税の欄がないのは、表題登記が課税されないから。')
box(ax, 4, 54, 44, 40, '地番', RED,
    ['空欄にする', '地番は登記官が付ける', '土地の表題登記の申請情報に', '地番は要らない（不動産登記令第3条第7号ロ）'], red=[0], step=6.5)
box(ax, 52, 54, 44, 40, '所在', BLACK,
    ['A市B町五丁目（地番区域まで）', '無番地なので、地番は書かない', '「50番地1」などを足さない'], red=[0], step=6.5)
box(ax, 4, 6, 44, 42, '申請人', BLACK,
    ['A市B町五丁目50番地1', '宗教法人雨堤天満宮', '代表役員　荒牧英雄', '法人は主たる事務所・名称のほか', '代表者の氏名も書く（令第3条第2号）'], red=[2], step=6.3)
box(ax, 52, 6, 44, 42, '登録免許税', BLACK,
    ['答案用紙に欄がない', '表題登記は登録免許税法別表第一に', '掲げる登記ではないので課税されない', '（登録免許税法第2条）'], red=[0], step=6.5)
path = os.path.join(OUT, 'H23_dai21mon_zu19_shinseisho_seiri.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 申請書の残りの欄: 整理図（固定配置）\n  →', path)

# =====================================================================
# 図16：問4 縮尺の決まり（兼用にしない）（固定配置）
# =====================================================================
fig, ax = fixed_figure('問4　縮尺が違うので兼用にしない（土地所在図1／500・地積測量図1／250）',
                       '答案用紙の印刷の「1／250」は地積測量図の縮尺。土地所在図は問題文の注6の500分の1で、地積測量図の用紙の余白に描く。')
box(ax, 4, 60, 44, 32, '土地所在図', BLUE,
    ['近傍類似の土地の地図と同一の縮尺', '（不動産登記規則第76条第2項）', '問題文の注6：500分の1　→　1／500'], red=[2])
box(ax, 52, 60, 44, 32, '地積測量図', BLUE,
    ['250分の1の縮尺', '（不動産登記規則第77条第4項）', '→　1／250'], red=[2])
box(ax, 4, 34, 92, 18, '縮尺が同じなら兼用できる（準則第51条第4項）', GRAY,
    ['本問は1／500と1／250で違う　→　「土地所在図兼地積測量図」にはできない'], red=[0])
box(ax, 4, 4, 92, 24, '地積測量図の用紙の余白に土地所在図を描く（準則第51条第3項）', RED,
    ['枠の右に地積測量図（1／250）、左の余白に土地所在図（1／500）', '土地所在図のそばに「縮尺　1／500」と自分で書く。印刷の「1／250」は地積測量図の縮尺'],
    step=6.0, fc='#fff5f5')
for xx in (26, 74):
    ax.annotate('', xy=(xx, 53.5), xytext=(xx, 58.5), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=GRAY))
ax.annotate('', xy=(50, 29.5), xytext=(50, 33.0), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=RED))
path = os.path.join(OUT, 'H23_dai21mon_zu20_shukushaku.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 整理図（固定配置）\n  →', path)

# =====================================================================
# 辺長6本の端数処理（第7章。固定配置）
# =====================================================================
fig, ax = fixed_figure('問4　辺長6本は小数第3位を四捨五入（ICは8.6457…で8.65）',
                       '問題文の注3：辺長は小数第3位を四捨五入。ICは小数第3位が5なので繰り上げる（切り捨てた8.64は誤り）。')
SIDE_NAMES = [('CD', 'Abs(D − C)', C, D), ('DH', 'Abs(H − D)', D, H), ('HJ', 'Abs(J − H)', H, J),
              ('JK', 'Abs(K − J)', J, K), ('KI', 'Abs(I − K)', K, I), ('IC', 'Abs(C − I)', I, C)]
for k, hd in enumerate(['辺', '電卓の式', '表示（小数第4位まで）', '図に書く値']):
    ax.text([8, 22, 52, 82][k], 90, hd, fontsize=18, weight='bold', va='center', color=GRAY)
for k, (nm, ex, p, q) in enumerate(SIDE_NAMES):
    y = 80 - k * 10.5
    ok = nm == 'IC'
    ax.add_patch(FancyBboxPatch((4, y - 4.2), 92, 8.4, boxstyle='round,pad=0.3', fc='#fff5f5' if ok else '#f7f7f7',
                                ec=RED if ok else GRAY, lw=2.0))
    v = math.floor(abs(q - p) * 1e4) / 1e4
    ax.text(8, y, nm, fontsize=20, weight='bold', va='center', color=RED if ok else BLACK)
    ax.text(22, y, ex, fontsize=17, va='center', color=BLACK)
    ax.text(52, y, f'{v:.4f}…', fontsize=18, va='center', color=RED if ok else BLACK)
    ax.text(82, y, d2(p, q), fontsize=20, weight='bold', va='center', color=RED if ok else BLACK)
    ax.annotate('', xy=(79, y), xytext=(71, y), arrowprops=dict(arrowstyle='-|>', lw=2.0, color=RED if ok else GRAY))
assert [d2(p, q) for _, _, p, q in SIDE_NAMES] == ['4.72', '13.88', '11.78', '4.44', '8.97', '8.65']
assert f'{math.floor(abs(C - I) * 1e4) / 1e4:.4f}' == '8.6457'
ax.text(50, 12, '8.6457… は小数第3位が5 → 繰り上げて 8.65（8.64は誤り）', fontsize=17, ha='center', va='center', color=RED)
ax.text(50, 5, 'DH 13.8796… も第3位が9なので 13.88。ほかの4本は第3位が4以下なので切り捨てた形', fontsize=15, ha='center', va='center', color=BLACK)
path = os.path.join(OUT, 'H23_dai21mon_zu21_henchou_hasuu.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 辺長の端数: 整理図（固定配置）\n  →', path)

# =====================================================================
# 地積測量図に書くもの・書かないもの（第7章。固定配置）
# =====================================================================
fig, ax = fixed_figure('問4　地積測量図に書くもの・書かないもの',
                       '座標値・系の番号・求積方法・地積は書かない（問題文の注3）。T2・T3は位置・名称・座標値を書く（問題文の注4）。')
box(ax, 3, 34, 46, 60, '地積測量図に書く', BLUE,
    ['各辺の長さ（辺長6本）', '方位、土地の所在（A市B町五丁目）', '隣接地の地番・道路、区画の中に「申請地」',
     'C・D・H・I：コンクリート杭', 'J：市金属標　K：金属標', 'T2・T3の位置・名称・座標値（問題文の注4）',
     '測量年月日（平成23年8月10日）', '申請人・作成者（単位 m は印刷済み）'], step=5.4, fs=15)
box(ax, 51, 34, 46, 60, '地積測量図に書かない', RED,
    ['各筆界点の座標値（問題文の注3）', '平面直角座標系の番号又は記号（問題文の注3）', '求積の方法（問題文の注3）', '地積の表示（問題文の注3）',
     '本件土地の筆界点でない点', '　B・E・F・G・M（石標）', '　A・L（市金属標）', '　T1（位置も名称も書かない）'], red=[0, 1, 2, 3], step=5.4, fs=15, fc='#fff5f5')
box(ax, 3, 4, 94, 26, '土地所在図に書く／地番の欄', GREEN,
    ['土地所在図：方位、縮尺（1／500）、申請地、隣地の地番（50－1・50－2・51－2・51－3）と道路（規則第76条第1項）',
     '地番の欄：空欄（まだ地番がない。地番は表題登記のときに登記官が付ける）'], red=[1], step=6.5, fs=15)
path = os.path.join(OUT, 'H23_dai21mon_zu22_kaku_kakanai.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 書く／書かない: 整理図（固定配置）\n  →', path)

# =====================================================================
# 地番の欄は空欄（第7章。固定配置）
# =====================================================================
fig, ax = fixed_figure('問4　地番の欄は空欄、土地の所在はA市B町五丁目',
                       '本件土地は無番地の土地で、まだ地番がない。区画の中には「申請地」と書く（50番1などの隣地の地番を写さない）。')
for (x0, y0, w, hh, lab, val, wr) in [(8, 74, 24, 11, '地　番', '', False), (8, 59, 62, 11, '土地の所在', 'Ａ市Ｂ町五丁目', True)]:
    ax.add_patch(plt.Rectangle((x0, y0), w, hh, fill=False, ec=BLACK, lw=2.0))
    ax.plot([x0 + 10, x0 + 10], [y0, y0 + hh], color=BLACK, lw=2.0)
    ax.text(x0 + 5, y0 + hh / 2, lab, fontsize=14, ha='center', va='center', rotation=0)
    if wr:
        ax.text(x0 + 12, y0 + hh / 2, val, fontsize=17, weight='bold', va='center', color='#1a3a8f')
ax.text(21, 79.5, '空欄', fontsize=22, weight='bold', va='center', ha='center', color=RED)
ax.text(40, 79.5, '← 答案用紙の問4の枠の上の右側（印刷済みの欄）', fontsize=14, va='center', color=GRAY)
box(ax, 4, 6, 44, 44, '地番の欄を空欄にする理由', RED,
    ['本件土地にはまだ地番がない', '地番は表題登記のときに登記官が付ける', '書くものがないので空欄のまま',
     '区画の中は「申請地」と書く'], red=[0], step=6.5, fs=15, fc='#fff5f5')
box(ax, 52, 6, 44, 44, '土地の所在の欄', BLACK,
    ['地番区域の名称まで書く', '　→ A市B町五丁目', '無番地なので「50番地1」などを', '足さない（隣の50番1の地番ではない）'], red=[1], step=6.5, fs=15)
path = os.path.join(OUT, 'H23_dai21mon_zu23_chiban_ran.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 地番の欄: 整理図（固定配置）\n  →', path)

# =====================================================================
# 問4 土地所在図（1/500）と地積測量図（1/250）の完成見本
#   答案用紙（その2）の問4の枠（A3横の用紙の1400×988pxを0.3mm/pxとして測った。横約32cm・縦約19cm）に、
#   用紙の位置・大きさのまま描く。黒は印刷済み、青は書き込み。左に土地所在図（1/500・1m ＝ 2mm）、右に地積測量図（1/250・1m ＝ 4mm）
# =====================================================================
setup_font()
SW, SHH, TOPM = 16.0, 12.9, 0.6
S_IN = 15.5 / 1110                       # 答案用紙の1px（0.3mm）あたりの図のインチ数
INK = '#1a3a8f'


def fx(px):
    return (0.25 + (px - 60) * S_IN) / SW


def fy(py):
    return 1 - (TOPM + (py - 85) * S_IN) / SHH


fig = plt.figure(figsize=(SW, SHH), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問4　土地所在図（1／500）と地積測量図（1／250）の完成見本', fontsize=24, weight='bold', y=1 - 0.3 / SHH, va='center')


def frect(x0, y0, x1, y1, lw=1.4):
    fig.add_artist(Rectangle((fx(x0), fy(y1)), fx(x1) - fx(x0), fy(y0) - fy(y1), transform=fig.transFigure,
                             fill=False, edgecolor=BLACK, lw=lw))


def fline(x0, y0, x1, y1, lw=1.2):
    fig.add_artist(plt.Line2D([fx(x0), fx(x1)], [fy(y0), fy(y1)], transform=fig.transFigure, color=BLACK, lw=lw))


def ftext(px, py, s, fs=13, ha='center', color=BLACK, **kw):
    fig.text(fx(px), fy(py), s, fontsize=fs, ha=ha, va='center', color=color, **kw)


ftext(78, 120, '問4', fs=15, ha='left', weight='bold')
ftext(347, 120, '土　地　所　在　図', fs=19)
ftext(1004, 120, '地　積　測　量　図', fs=19)
frect(78, 142, 1151, 782, lw=1.8)                                  # 図を描く枠（横約32cm・縦約19cm）
frect(641, 99, 857, 142)                                           # 地番の欄（空欄）
fline(735, 99, 735, 142)
ftext(688, 120, '地　　番', fs=13)
frect(641, 142, 1151, 184)                                         # 土地の所在の欄
fline(735, 142, 735, 184)
ftext(688, 163, '土地の所在', fs=13)
ftext(745, 163, 'Ａ市Ｂ町五丁目', fs=16, ha='left', color=INK, weight='bold')
frect(78, 782, 579, 845)                                           # 作成者の欄
fline(162, 782, 162, 845)
ftext(120, 813, '作　成　者', fs=13)
ftext(167, 802, 'A市B町三丁目1番2号　中村容子', fs=12, ha='left', color=INK)
ftext(167, 826, '土地家屋調査士', fs=11, ha='left')
frect(418, 815, 458, 836)
ftext(438, 826, '職印', fs=10)
ftext(463, 836, '（平成23年8月21日作成）', fs=8.5, ha='left')
frect(648, 782, 1032, 845)                                         # 申請人の欄
fline(733, 782, 733, 845)
ftext(690, 813, '申　請　人', fs=13)
ftext(742, 813, '宗教法人雨堤天満宮　代表役員　荒牧英雄', fs=12, ha='left', color=INK)
frect(1032, 782, 1151, 845)                                        # 縮尺の欄（1/250は印刷済み）
fline(1068, 782, 1068, 845)
ftext(1050, 813, '縮尺', fs=11)
fline(1078, 837, 1142, 795, lw=1.0)
ftext(1097, 801, '1', fs=11)
ftext(1122, 828, '250', fs=11)
ftext(1026, 771, '（単位：m）', fs=10, ha='left')
fig.text(0.5, 0.72 / SHH,
         '黒は印刷済み（枠、地番・土地の所在・作成者・申請人・縮尺の欄、「土地家屋調査士」「職印」「平成23年8月21日作成」、1／250、単位）、青は書き込み。\n'
         '地番の欄は空欄（まだ地番がない）。印刷の「1／250」は地積測量図の縮尺なので、土地所在図には「縮尺　1／500」と自分で書く（準則第51条第3項）。\n'
         '座標値・系の番号・求積方法・地積は書かない（問題文の注3）。T2・T3は位置・名称・座標値を書く（問題文の注4）。',
         ha='center', va='center', fontsize=14, linespacing=1.6)


def put_axes(x0, y0, x1, y1):
    return fig.add_axes([fx(x0), fy(y1), fx(x1) - fx(x0), fy(y0) - fy(y1)])


M250 = 4 / 0.3 * S_IN                    # 1/250で1mが図の上で何インチか（4mm）
M500 = M250 / 2
ax2 = put_axes(625, 190, 1146, 765)
ax1 = put_axes(86, 150, 610, 765)


def exact_limits(ax, c, m_in):
    pos = ax.get_position()
    hw = pos.width * SW / m_in / 2           # 東西（Y）の半分の幅（m）
    hh = pos.height * SHH / m_in / 2         # 南北（X）の半分の高さ（m）
    fit(ax, [c + P(-hh, -hw), c + P(hh, hw)], margin=0.0, pad_aspect=True)
    return hw * 2, hh * 2


ext = lambda p, q, k: p + (q - p) / abs(q - p) * k  # noqa: E731
w2, h2 = exact_limits(ax2, P(310.5, 320.6), M250)
w1, h1 = exact_limits(ax1, P(311.0, 314.0), M500)
print(f'  地積測量図の枠の中：東西{w2:.1f}m×南北{h2:.1f}m（1/250）、土地所在図：東西{w1:.1f}m×南北{h1:.1f}m（1/500）')
assert 38 < w2 < 41 and 42 < h2 < 45 and 78 < w1 < 82 and 90 < h1 < 95
LEFT_LINES = [(C, M, 9), (D, E, 9), (C, B_REF, 9), (D, D + (D - H), 7), (J, G, 11), (K, L, 8)]
for p, q, k in LEFT_LINES:   # 描く線の端点がすべて表示範囲に入ること
    e = ext(p, q, k)
    assert ax1.get_xlim()[0] < e.imag < ax1.get_xlim()[1] and ax1.get_ylim()[0] < e.real < ax1.get_ylim()[1]
za = Zu(ax1, fontsize=12)
za.poly(HONKEN, lw=1.8)
for p, q, k in LEFT_LINES:
    za.line(p, ext(p, q, k), lw=1.0)
za.north_arrow()
za.callout(INNER, '申請地', dirs=(-20, 0, -40), fs=12, dists=(40, 55, 70))
za.free_text(ext(D, D + (D - H), 4) + P(2.0, 2.0), '50－2', fs=12, offsets=((0, 0), (0, 12), (12, 0)))
za.free_text(H + P(4.0, 2.0), '50－1', fs=12, offsets=((0, 0), (0, 12), (12, 0)))
za.free_text(ext(C, M, 4) + P(3.0, -4.0), '51－3', fs=12, offsets=((0, 0), (-12, 0), (0, 12)))
za.free_text(I + P(-5.0, -5.0), '51－2', fs=12, offsets=((0, 0), (0, -12), (-12, 0)))
za.free_text(P(299.0, 314.0), '道　路', fs=12, offsets=((0, 0), (0, -12), (20, 0)))
za.free_text(P(291.0, 312.0), '縮尺　1／500', fs=14, weight='bold', color=INK, offsets=((0, 0), (0, -14), (20, 0)))
zb = Zu(ax2, fontsize=13)
zb.poly(HONKEN, lw=2.2)
for p, q, k in [(C, M, 1.5), (D, E, 1.5), (C, B_REF, 1.3), (D, D + (D - H), 1.3), (J, G, 2.0), (K, L, 1.5)]:
    zb.line(p, ext(p, q, k), lw=1.3)
zb.north_arrow()
for p, n in [(C, 'C'), (D, 'D'), (H, 'H'), (J, 'J'), (K, 'K'), (I, 'I')]:
    zb.point(p, KIND[n])
for p, q, n in SIDES:
    zb.edge_label(p, q, n, INNER, fs=13)
for p, n in [(C, 'C'), (D, 'D'), (H, 'H'), (J, 'J'), (K, 'K'), (I, 'I')]:
    zb.point_label(p, n, away=INNER, weight='normal')
for p, n in [(T2, 'T2'), (T3, 'T3')]:
    zb.point(p, 'kijun')
    zb.point_label(p, n, away=p + P(-1, 0), weight='normal')
zb.free_text(INNER, '申\n請\n地', fs=14, offsets=((0, 0), (10, 0), (-10, 0)))
zb.free_text(D + P(1.2, -1.8), '50－2', fs=13, offsets=((0, 0), (-10, 10), (0, 16)))
zb.free_text(H + P(2.5, 1.5), '50－1', fs=13, offsets=((0, 0), (12, 0), (0, 12)))
zb.free_text(C + P(0.2, -1.8), '51－3', fs=13, offsets=((0, 0), (-12, 0), (0, -12)))
zb.free_text(P(306.5, 307.8), '51－2', fs=13, offsets=((0, 0), (0, -12), (-12, 0)))
zb.free_text(P(301.5, 318.5), '道　路', fs=13, offsets=((0, 0), (0, -12), (20, 0)))
zb.free_text(P(297.2, 309.0), 'T2　A市基準点T2\nX 300.12　Y 306.99', fs=12, offsets=((0, 0), (0, -10), (10, 0)))
zb.free_text(P(297.2, 330.0), 'T3　A市基準点T3\nX 299.47　Y 333.78', fs=12, offsets=((0, 0), (0, -10), (-10, 0)))
zb.free_text(P(292.2, 322.0), 'C・D・H・I：コンクリート杭\nJ：市金属標　K：金属標\n測量年月日：平成23年8月10日',
             fs=12, offsets=((0, 0), (0, -12), (-12, 0)))
ALL_PROBLEMS += save(fig, [za, zb], 'H23_dai21mon_zu24_shozaizu_sokuryouzu.png')

# =====================================================================
# 図18：本番で解く順番（固定配置）
# =====================================================================
fig, ax = fixed_figure('本番で解く順番（いちばん重いのはC点と2つの作図）',
                       'C点がなくても、問1の全部と、申請書の地積以外の欄は書ける。重い計算と作図は後ろに回し、先に点を積む。')
STEPS = [('①', '問1を書き切る', '計算なし。要件の言葉と問題文の事実を4組（他人の物・所有の意思・平穏かつ公然・20年間）', BLACK),
         ('②', '問3の申請書の地積以外の欄', '土地表題登記・添付書類・申請人・所在・地番は空欄・境内地・不詳', BLACK),
         ('③', 'A点・M点・K点の放射', '時計回りで足す。AM ＝ 21.70 で51番3の地積測量図を確かめる', BLACK),
         ('④', 'H点', 'E→Jは真南。交点（316.788, 315.34）から120°の向きに6.836m', BLACK),
         ('⑤', 'C点', '面積の比 157.3309 ÷ 364.4865（ブロック塀の10.05mは使わない）', RED),
         ('⑥', '面積と地積', 'C→D→H→J→K→I で113.875 → 113㎡（境内地は1㎡未満切捨て）', RED),
         ('⑦', '辺長6本と2つの作図', '4.72・13.88・11.78・4.44・8.97・8.65。土地所在図1／500、地積測量図1／250', RED)]
for k, (no, head, body, col) in enumerate(STEPS):
    y = 90 - k * 13.2
    ax.add_patch(FancyBboxPatch((5, y - 4.8), 90, 9.6, boxstyle='round,pad=0.5', fc='#fff5f5' if col == RED else '#f7f7f7',
                                ec=col, lw=2.0))
    ax.text(8, y + 1.7, f'{no}　{head}', fontsize=19, weight='bold', va='center', color=col)
    ax.text(12, y - 2.4, body, fontsize=15, va='center', color=BLACK)
    if k < len(STEPS) - 1:
        ax.annotate('', xy=(50, y - 8.2), xytext=(50, y - 5.6), arrowprops=dict(arrowstyle='-|>', lw=2.0, color=GRAY))
path = os.path.join(OUT, 'H23_dai21mon_zu25_toku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] 整理図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
