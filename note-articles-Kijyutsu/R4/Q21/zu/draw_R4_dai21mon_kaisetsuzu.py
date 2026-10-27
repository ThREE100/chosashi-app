"""令和4年度 第21問（土地）会話形式note記事の解説図を、座標値から作図する（2026-10-26 品質チェック6-2・6-3で作り直し）。

`../prompt_R4_dai21mon_kaiwa_kaisetsuzu.md`（基本フォーム `../../../prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作成）
の指示を、そのままPythonにしたもの。図に書く数値はすべて座標から計算し直し、記事の数値と一致しなければ止まる。
PNG名の番号（zu01〜）は記事の挿入順の管理用で、画像の中のタイトルには図番を入れない。
地積測量図の完成見本（zu31）は、試験の答案用紙の第4欄（`../touan_youshi/R4_dai21mon_touan_youshi.pdf` の2ページ目。A3横）の
枠・欄の位置と大きさを、PDFの罫線からmmで測ったとおりに描く（R5/Q21と同じ形。縮尺1/250で1m ＝ 4mm）。

実行: python3 note-articles-Kijyutsu/R4/Q21/zu/draw_R4_dai21mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from calc_helpers import P, r2, radial, dms, area, chiseki, disp, fmt_num  # noqa: E402
from zu_helpers import (Zu, new_figure, fit, centroid, xy, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)
import matplotlib.pyplot as plt  # noqa: E402
plt.rcParams['figure.max_open_warning'] = 0
from matplotlib.patches import Rectangle  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE

# ---- 座標（問題文の座標値と、記事で求めた点） ------------------------------
A, B, C, D = P(298.21, 273.89), P(279.30, 274.90), P(279.30, 303.07), P(301.13, 303.07)
E, F, G, H = P(298.09, 272.68), P(289.14, 272.74), P(279.30, 279.15), P(286.41, 274.52)
K, L = P(301.99, 311.25), P(296.75, 259.24)
T1, T2 = P(306.89, 305.35), P(303.64, 272.19)
Pp = r2(radial(T1, T2, 13.74, dms(338, 29, 30)))
Pw = r2(T1 + cmath.rect(13.74, cmath.phase(T2 - T1) - dms(338, 29, 30)))   # 反時計回りに測った誤り
J = P(C.real, Pp.imag)
I = r2(E + (D - E) * (Pp.imag - E.imag) / (D.imag - E.imag))
Dp = D + 1.49                                  # 拡幅前の道路の線の上の点（合成図）

# ---- 記事の数値との照合（一致しなければ作図しない） ------------------------
for n, (got, want) in {'P': (Pp, P(300.63, 293.12)), 'I': (I, P(300.13, 293.12)), 'J': (J, P(279.30, 293.12)),
                       '誤りのP': (Pw, P(310.66, 292.14))}.items():
    assert abs(got - want) < 1e-9, (n, got, want)
d2 = lambda p, q: f'{round(abs(p - q) + 1e-9, 2):.2f}'  # noqa: E731
SIDES = {'EA': (E, A, '1.22'), 'AI': (A, I, '19.33'), 'ID': (I, D, '10.00'), 'DC': (D, C, '21.83'),
         'CJ': (C, J, '9.95'), 'JG': (J, G, '13.97'), 'GH': (G, H, '8.48'), 'HF': (H, F, '3.26'),
         'FE': (F, E, '8.95'), 'IJ': (I, J, '20.83'), 'AH': (A, H, '11.82')}
for n, (p, q, want) in SIDES.items():
    assert d2(p, q) == want, (n, d2(p, q), want)
assert d2(Dp, F) == '33.19' and d2(Dp, G) == '33.41' and d2(Dp, B) == '36.57' and d2(Pp, I) == '0.50'
HON = [E, D, C, G, F]          # 本件土地（筆界E→F→G）
ABQ = [A, D, C, B]             # AB線で囲んだ四角形
I1 = [C, D, I, J]              # （イ）184番1
RO = [A, I, J, G, H]           # （ロ）184番3
HA = [E, A, H, F]              # （ハ）184番4
HBG = [H, B, G]                # 185番3の一部（悠人→春野）
AREAS = {'本件土地': (HON, 584.8248), 'AB線': (ABQ, 584.84705), '（イ）': (I1, 212.2335),
         '（ロ）': (RO, 357.44415), '（ハ）': (HA, 15.0604), 'HBG': (HBG, 15.10875)}
for n, (pts, want) in AREAS.items():
    assert abs(area(pts) - want) < 5e-6, (n, area(pts), want)
assert chiseki(area(RO), takuchi=False) == 357 and chiseki(area(I1)) == 212.23 and chiseki(area(HA)) == 15.06
assert abs(area(I1) + area(RO) + area(HA) - 584.73805) < 5e-6


def term(p, q):
    """座標法の1項（P・Conjg(次の点) の iの係数）"""
    return (p * q.conjugate()).imag


def terms(pts):
    return [term(pts[i], pts[(i + 1) % len(pts)]) for i in range(len(pts))]


assert abs(abs(sum(terms(ABQ))) - 1169.6941) < 1e-9
assert abs(abs(sum(terms(HON))) - 1169.6496) < 1e-9 and abs(abs(sum(terms(HA))) - 30.1208) < 1e-9
assert abs(abs(sum(terms(I1))) - 424.467) < 1e-9 and abs(abs(sum(terms(RO))) - 714.8883) < 1e-9
assert disp((B - H).conjugate() * (G - H)) == '52.3115 − 30.2175i'
print('数値の照合: すべて一致')

KUI = {'A': 'metal', 'C': 'metal', 'J': 'metal', 'D': 'concrete', 'E': 'concrete', 'F': 'concrete',
       'G': 'concrete', 'I': 'concrete', 'B': 'metal'}
ALL_PROBLEMS = []


def save(fig, zus, name):
    probs = []
    for z in zus:
        probs += z.check_overlaps(name)
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor='white')
    print('  →', path)
    return probs


def mark(z, p, n, away, color=BLACK):
    z.point(p, KUI.get(n, 'dot'), color=color)
    z.point_label(p, n, away=away, color=color)


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


def table_panel(ax2, head, rows, foot, foot_col=RED, step=10.5, fs=14.5):
    """右側の表（固定配置）。rows は (左の文字, 右の文字, 色)。左の文字が空で右も空の行は見出し行として使わない。"""
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.text(2, 97, head, ha='left', va='top', fontsize=17, weight='bold', color=BLUE)
    y = 86
    for lt, rt, col in rows:
        if rt is None:                                  # 小見出し
            ax2.text(2, y, lt, ha='left', va='center', fontsize=fs + 1, color=BLUE, weight='bold')
        else:
            ax2.add_patch(Rectangle((2, y - 4.5), 96, step - 1.5, facecolor='#f6f8fb', edgecolor='#c9d3e0', lw=1.0))
            ax2.text(5, y, lt, ha='left', va='center', fontsize=fs, color=col)
            ax2.text(95, y, rt, ha='right', va='center', fontsize=fs + 0.5, color=col, weight='bold')
        y -= step
    ax2.text(2, y + 2, foot, ha='left', va='top', fontsize=fs + 0.5, color=foot_col, weight='bold', linespacing=1.7)


CIRC = '①②③④⑤⑥⑦⑧'

# =====================================================================
# zu01：時系列（第1章）
# =====================================================================
fig, ax = board(10, '時系列　地目が変わった日が、申請の期限と登記の内容を決める')
EV = [(5, '平成16年', '狭あい道路の拡幅事業\n道路境界を確定\n184番2などを分筆', GRAY, 1),
      (17, '平成18年', '夏野涼が本件土地の\n西側にブロック塀', GRAY, -1),
      (29, '令和2年', '夏野涼が死亡\n悠人が185番3を相続', GRAY, 1),
      (41, '令和4年6月', '184番の建物を取壊し\n（月極駐車場にするため）', GRAY, -1),
      (54, '9月17日', '柵を撤去、I・J線に\nブロック塀を設置\n東側部分を売却（倉庫の敷地）', BLUE, 1),
      (68, '10月5日', 'A・B・J・Iの部分を\n月極駐車場にする\n→ 地目が変わる', RED, -1),
      (81, '10月14日', '登記の申請', RED, 1),
      (94, '11月5日', '地目変更の登記の\n申請の期限', ORANGE, -1)]
ax.annotate('', xy=(99, 58), xytext=(1, 58), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK))
for x, d, t, col, ud in EV:
    ax.plot([x], [58], 'o', ms=12, color=col, zorder=5)
    ax.plot([x, x], [58, 58 + ud * 7], color=col, lw=1.4)
    ax.text(x, 58 + ud * 8, d, ha='center', va='bottom' if ud > 0 else 'top', fontsize=13, color=col, weight='bold')
    ax.text(x, 58 + ud * 13.5, t, ha='center', va='bottom' if ud > 0 else 'top', fontsize=12, color=BLACK,
            linespacing=1.5)
rbox(ax, 1, 1, 48, 24, '地目が変わったのは10月5日の中央部分だけ',
     '・9月17日の東側部分は、倉庫の敷地になっても宅地のまま\n・10月5日から1か月以内（11月5日まで）に申請 ＝ 10月14日は期限内\n（不動産登記法第37条）', RED)
rbox(ax, 51, 1, 48, 24, '今回の申請に入らないもの',
     '・東側部分の売却（9月17日）の所有権の移転の登記\n・AB線に合わせる交換の所有権の移転の登記\n→ どちらも、その前提の表示の登記だけを今回申請する', BLUE)
put_board(fig, 'R4_dai21mon_zu01_jikeiretsu.png')

# =====================================================================
# zu02：注の仕分け（問題文の注1〜8・調査図素図の注1〜4・観測値の表の注1・2）
# =====================================================================
fig, ax = board(8.6, '注は3系統　問題文の注1〜8、調査図素図の注1〜4、観測値の表の注1・2')
BOX = [
    (1, 56, 31, 40, '毎年ほぼ同じ決まり文句', '問題文の注1　行為・書類は全て適法\n問題文の注2　書面申請\n問題文の注8　訂正・加入・削除の\n　仕方', GRAY),
    (34, 56, 31, 40, '計算の条件', '問題文の注3　座標値は小数第3位を\n　四捨五入して小数第2位まで\n問題文の注4　縮尺250分の1、筆界点間\n　の距離は小数第3位を四捨五入', BLUE),
    (67, 56, 32, 40, '地積測量図に書かないもの', '問題文の注5　座標値・座標系の番号・\n　地積と求積方法・測量年月日は不要\n問題文の注6　A市基準点は位置と点名\n　だけ（座標値は書かない）', GREEN),
    (1, 3, 31, 49, '今年の答えに効く指示', '問題文の注7　最も東の土地を184番1、\n　その余は184番3から東側から順に\n→ 分筆後の地番を決める', RED),
    (34, 3, 31, 49, '点の条件（調査図素図の注）', '調査図素図の注1　I点はE点とD点を\n　結ぶ直線上にある\n調査図素図の注2　J点はB点とC点を\n　結ぶ直線上にある\n調査図素図の注3　本件土地と183番1・\n　185番3との筆界は相談時に不明\n調査図素図の注4　点名は素図上の点', ORANGE),
    (67, 3, 32, 49, '観測値の表の注', '観測値の表の注1　観測角は時計回りの\n　角度を示す\n観測値の表の注2　北はX軸の正方向に\n　一致する\n→ P点を出す向き（足す）と、\n　X が北・Y が東の置き方', PURPLE),
]
for x, y, w, h, t, b, col in BOX:
    rbox(ax, x, y, w, h, t, b, col)
fig.text(0.5, 0.025, '記事では「問題文の注○」「調査図素図の注○」「観測値の表の注○」と言い分ける（番号だけでは、どの注か分からない）',
         ha='center', fontsize=14, color=GRAY)
put_board(fig, 'R4_dai21mon_zu02_chuu_shiwake.png')

# =====================================================================
# zu03：全体像
# =====================================================================
fig, (ax,) = new_figure('北を上にして描き直した全体像（令和4年10月14日の申請時）',
                        '問題の調査図素図は傾いている。座標どおりに北を上にすると、B・G・C は真東向き（X＝279.30）、C・D は真北向き（Y＝303.07）の直線。\n'
                        '春野朝子と夏野悠人が境だと思っていたAB線（灰色の破線）と、杭が見つかった筆界E→F→G（黒）の違いに注意。')
z = Zu(ax)
fit(ax, [L, K, B, C, T1, T2], margin=0.08, pad_aspect=True)
z.poly(HON, fill=BLUE)
z.line(L, K, color=BLACK, lw=1.4)
z.line(A, B, color=GRAY, lw=1.8, ls='--')
z.north_arrow()
co = centroid(HON)
z.free_text(co, '本件土地\n184番1　宅地\n584.75㎡', fs=17)
for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (H, 'H')]:
    mark(z, p, n, co)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
for p, n in [(K, 'K'), (L, 'L')]:
    z.point(p, 'dot', color=GRAY)
    z.point_label(p, n, away=co, color=GRAY)
z.callout(A + (B - A) * 0.35, 'AB線（2人の認識）', dirs=(180, 160, 200), color=GRAY, dists=(90, 120))
z.edge_label(D, C, '183番1', co, fs=15, rotate=False, dists=(40, 50))
z.edge_label(G, C, '196', co, fs=15, rotate=False, dists=(30, 40))
z.edge_label(F, E, '185番3', co, fs=15, rotate=False, dists=(45, 55))
z.edge_label(E, D, '道路（184番2）', co, fs=15, rotate=False, dists=(38, 48))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu03_zentaizu.png')

# =====================================================================
# zu04：座標法の計算過程　AB線の四角形と、E→F→Gで囲んだ本件土地（2つとも584㎡台）
# =====================================================================
TA, TH = terms(ABQ), terms(HON)
NA, NH = ['A', 'D', 'C', 'B'], ['E', 'D', 'C', 'G', 'F']
fig, ax = board(8.8, '座標法の計算過程　AB線で囲んでも、E→F→Gで囲んでも584㎡台')
for x0, head, nm, tm, tot, ar, col in [(1, 'AB線で囲む（A→D→C→B）', NA, TA, sum(TA), 584.84705, GRAY),
                                       (51, 'E→F→Gで囲む（E→D→C→G→F）', NH, TH, sum(TH), 584.8248, RED)]:
    rbox(ax, x0, 26, 48, 66, head, '', col)
    ax.text(x0 + 1.5, 83, '各項（P・Conjg(次の点) の iの係数）', ha='left', va='center', fontsize=13.5, color=col)
    y = 75
    n = len(nm)
    for i in range(n):
        ax.add_patch(Rectangle((x0 + 1.5, y - 3.3), 45, 6.4, facecolor='white', edgecolor='#c9d3e0', lw=1.0))
        ax.text(x0 + 3, y, f'{CIRC[i]}　{nm[i]}・Conjg({nm[(i + 1) % n]})', ha='left', va='center', fontsize=14)
        ax.text(x0 + 46, y, fmt_num(tm[i]), ha='right', va='center', fontsize=14.5, weight='bold')
        y -= 6.9
    ax.text(x0 + 3, 40.5, '合計（表示の iの係数）', ha='left', va='center', fontsize=14, color=col, weight='bold')
    ax.text(x0 + 46, 40.5, fmt_num(tot), ha='right', va='center', fontsize=15, color=col, weight='bold')
    ax.text(x0 + 3, 31.5, f'|合計| ÷ 2 ＝ {ar}㎡', ha='left', va='center', fontsize=16, color=col, weight='bold')
rbox(ax, 1, 1, 98, 21, '登記記録は584.75㎡ ── どちらで測っても近い（差は0.10㎡と0.07㎡）',
     '面積が登記記録と合っても、AB線とE→F→Gのどちらが筆界かは決められない。決め手は、次の図の西側と南西の2つの小さな部分と、合成図の辺長。\n'
     '合計の符号がマイナスなのは時計回りに回ったから（向きで符号が変わるだけ。面積は絶対値）', RED, fs_b=14)
put_board(fig, 'R4_dai21mon_zu04_zahyouhou_ab_efg.png')

# =====================================================================
# zu05：座標法の計算過程　西側E・A・H・F（4項）と△HBG
# =====================================================================
TW = terms(HA)
uv = (B - H).conjugate() * (G - H)
fig, (ax, ax2) = new_figure('西側の部分E・A・H・Fと△HBGの面積（AB線とE→F→Gで挟まれた2つの部分）',
                            '左：E・A・H・F（橙）と△HBG（紫）。H点はAB線とFGの交点。①〜④は記事の電卓の4行と同じ順。\n'
                            '右：どちらも約15㎡。西側ではみ出した分と南西でへこんだ分がほぼ同じなので、AB線でもE→F→Gでも合計がほとんど変わらない。',
                            ncols=2, width_ratios=[1.1, 1])
z = Zu(ax)
fit(ax, [E, A, B, G, F, H], margin=0.14, pad_aspect=True)
z.poly(HA, color=ORANGE, lw=2.0, fill=ORANGE, alpha=0.40)
z.poly(HBG, color=PURPLE, lw=2.0, fill=PURPLE, alpha=0.30)
z.line(F, G, color=BLACK, lw=1.6)
z.north_arrow()
cw = centroid(HA)
for i, n in enumerate('EAHF'):
    p, q = HA[i], HA[(i + 1) % 4]
    z.edge_label(p, q, CIRC[i], cw, color=RED, fs=16, rotate=False, dists=(14, 20, 28))
for p, n in [(E, 'E'), (A, 'A'), (H, 'H'), (F, 'F'), (B, 'B'), (G, 'G')]:
    mark(z, p, n, cw if n in 'EAHF' else centroid(HBG))
z.callout(centroid(HBG), 'u ＝ B − H\nv ＝ G − H', dirs=(-60, -30, -90), color=PURPLE, dists=(60, 85, 110), fs=13)
table_panel(ax2, 'E・A・H・F（4項）の iの係数',
            [(f'{CIRC[i]}　{"EAHF"[i]}・Conjg({"EAHF"[(i + 1) % 4]})', fmt_num(TW[i]), BLACK) for i in range(4)]
            + [('合計', fmt_num(sum(TW)), RED), ('|合計| ÷ 2', '15.0604㎡', RED),
               ('△HBG　Conjg(u) × v', '52.3115 − 30.2175i', PURPLE), ('|−30.2175| ÷ 2', '15.10875㎡', PURPLE)],
            '15.0604㎡ は（ハ）184番4の地積（宅地なので15.06㎡）になる')
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu05_nishigawa_hbg.png')

# =====================================================================
# zu06：AB線とE→F→Gの比較
# =====================================================================
fig, (ax1, ax2) = new_figure('面積では筆界を決められない（AB線とE→F→G）',
                             '左：AB線で囲むと584.84㎡、右：E→F→Gで囲むと584.82㎡。どちらも登記記録の584.75㎡に近い。\n'
                             '西側のE・A・H・F（15.06㎡）と△HBG（15.10㎡）がほぼ同じ面積なので、差し引きでほとんど変わらない。',
                             ncols=2)
zs = []
for ax, pts, head, s, col in [(ax1, ABQ, 'AB線で囲む（2人の認識）', '584.84㎡', GRAY),
                              (ax2, HON, 'E→F→Gで囲む（杭の位置）', '584.82㎡', RED)]:
    z = Zu(ax, fontsize=14)
    fit(ax, [E, D, C, B], margin=0.22, pad_aspect=True)
    z.poly(pts, fill=BLUE)
    if pts is HON:
        z.poly(HA, color=ORANGE, lw=0, fill=ORANGE, alpha=0.45, check=False)
        z.poly(HBG, color=PURPLE, lw=1.2, ls='--', fill=PURPLE, alpha=0.35)
        z.line(A, B, color=GRAY, lw=1.2, ls='--')
    else:
        z.poly(HON, color=GRAY, lw=1.0, ls=':')
    z.north_arrow(length=0.07)
    ax.set_title(head, fontsize=18, color=col, weight='bold', pad=6)
    z.free_text(centroid(pts), s, fs=18, color=col, weight='bold')
    for p, n in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (H, 'H')]:
        z.point(p, 'dot')
        z.point_label(p, n, away=centroid(pts))
    zs.append(z)
zs[1].callout(centroid(HA), 'E・A・H・F　15.06㎡', dirs=(-10, 10, -25), color=ORANGE, dists=(60, 80, 100))
zs[1].callout(centroid(HBG), '△HBG　15.10㎡', dirs=(-60, -40, -80), color=PURPLE, dists=(50, 70, 90))
ALL_PROBLEMS += save(fig, zs, 'R4_dai21mon_zu06_hikkai_hikaku.png')

# =====================================================================
# zu07：合成図の辺長で筆界を裏付ける
# =====================================================================
fig, (ax,) = new_figure('合成図の33.19・33.41で筆界E→F→Gを裏付ける',
                        '合成図の対角線は、拡幅前の道路の線の上の点D′（D点から真北へ1.49）から引かれている。\n'
                        'D′からF点まで33.19、G点まで33.41で合成図と一致。AB線の端のB点までは36.57で、合成図のどこにもない。\n'
                        '拡幅前の道路の線は、E点から北へ1.37の点とD′を結んだ模式（問題文に座標はない）。')
z = Zu(ax)
fit(ax, [E, Dp, C, B], margin=0.14, pad_aspect=True)
z.poly(HON, fill=BLUE)
z.line(D, Dp, color=BLACK, lw=1.4)
z.line(E + 1.37, Dp, color=GRAY, lw=1.2, ls='-.')
z.line(Dp, F, color=RED, lw=2.0, ls='--')
z.line(Dp, G, color=RED, lw=2.0, ls='--')
z.line(Dp, B, color=GRAY, lw=1.2, ls=':')
z.north_arrow()
co = centroid(HON)
for p, n in [(D, 'D'), (C, 'C'), (G, 'G'), (F, 'F'), (E, 'E'), (B, 'B')]:
    z.point(p, 'dot', color=GRAY if n == 'B' else BLACK)
    z.point_label(p, n, away=co, color=GRAY if n == 'B' else BLACK)
z.point(Dp, 'dot', color=RED)
z.point_label(Dp, 'D′', away=co, color=RED)
z.edge_label(Dp, F, '33.19', C, color=RED, fs=17, ts=(0.5, 0.38, 0.62))
z.edge_label(Dp, G, '33.41', F, color=RED, fs=17, ts=(0.5, 0.62, 0.38))
z.edge_label(Dp, B, '36.57（合成図にない）', C, color=GRAY, fs=13, ts=(0.62, 0.72, 0.5))
z.free_text(D + 0.745, '1.49', fs=14, ha='left', offsets=((10, 0), (16, -6), (16, 6), (24, 0)))
z.callout(E + 1.37 + (Dp - E - 1.37) * 0.3, '拡幅前の道路の線（位置は模式）', dirs=(90, 120, 60), color=GRAY, dists=(40, 60))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu07_gouseizu.png')

# =====================================================================
# zu08：筆界は合意では動かない（所有権界との違い）
# =====================================================================
fig, ax = board(8, '筆界は合意では動かない　AB線を所有権の境にするには分筆と交換が要る')
rbox(ax, 1, 54, 48, 38, '筆界（E→F→G）',
     '土地が登記されたときに決まった線\n・春野さんと悠人さんが合意しても動かない\n・杭が見つかったのはE・F・G\n・合成図の33.19・33.41とも一致', RED)
rbox(ax, 51, 54, 48, 38, '所有権界（AB線）',
     '所有権が及ぶ範囲の境。当事者の合意で決まる\n・2人が境だと思っていた線\n・ブロック塀もAB線に沿っている\n→ 所有権界をAB線にするのは、2人の交換', GRAY)
arrow(ax, 25, 52, 25, 44)
arrow(ax, 75, 52, 75, 44)
rbox(ax, 1, 3, 48, 38, '合意だけでは足りない',
     'AB線を境にしたくても、筆界の位置は動かない\n→ 土地の一部を分けて、所有者を入れ替えるしかない', RED)
rbox(ax, 51, 3, 48, 38, '分筆して交換の所有権の移転',
     '① 西側のE・A・H・Fを本件土地から分筆\n　（△HBGは悠人さんの185番3の側）\n② 交換による所有権の移転の登記\n→ 今回の申請は、その前提の表示の登記', BLUE)
put_board(fig, 'R4_dai21mon_zu08_shoyuukenkai_hikkai.png')

# =====================================================================
# zu09：問1 P点（放射）
# =====================================================================
fig, (ax,) = new_figure('問1　P点の求め方（T1から放射）',
                        'T1→T2の方向角は −95°35′51.58″（360°を足して 264°24′08.42″）。これに時計回りの観測角 338°29′30″ を足すと 242°53′38.42″。\n'
                        'その方向へ 13.74m 進んだ点がP。反時計回りに測ると、道路の北の向こう側に出てしまう。')
z = Zu(ax)
fit(ax, [T1 + P(1, 9), T2 + P(0, -2), Pp + P(-3, 0), Pw + P(1.5, 0)], margin=0.06, pad_aspect=True)
z.poly(HON, color=GRAY, lw=1.2)
z.line(L, K, color=GRAY, lw=1.2)
z.line(T1, T1 + 6, color=GRAY, lw=1.2, ls='--')
z.free_text(T1 + 6, '北', color=GRAY, fs=14, offsets=((0, 14), (14, 10), (-14, 10)))
z.line(T1, T2, color=BLUE, lw=2.0)
z.line(T1, Pp, color=RED, lw=2.6)
z.line(T1, Pw, color=GRAY, lw=1.4, ls=':')
z.north_arrow()
z.angle_arc(T1, 3.0, 0, 264.402, color=BLUE)
z.angle_arc(T1, 1.9, 264.402, 242.894 + 360, color=RED)
for p in (T1, T2):
    z.point(p, 'kijun')
z.point(Pp, 'dot', color=RED)
z.point(Pw, 'dot', color=GRAY)
z.edge_label(T1, Pp, '13.74', T1 + P(-10, 0), color=RED, fs=18, ts=(0.62, 0.72, 0.5), dists=(16, 22, 30))
z.callout(T1 + P(0.3, -3.0), '方向角 264°24′08.42″\n（北から時計回りにT2の方向）', dirs=(110, 130, 90), color=BLUE,
          dists=(90, 120, 150))
z.callout(T1 + P(-1.9, 0.2), '観測角 338°29′30″\n（T2の方向から時計回り）', dirs=(-20, -40, 0, -60), color=RED,
          dists=(90, 120, 150))
z.callout(Pp, 'P（300.63, 293.12）', dirs=(-120, -150, -100), color=RED)
z.callout(Pw, '反時計回りに測った誤り\n（310.66, 292.14）', dirs=(180, 160, 200), color=GRAY)
z.callout(T1, 'T1（306.89, 305.35）', dirs=(60, 40, 80), color=BLACK, dists=(90, 120, 150))
z.callout(T2, 'T2（303.64, 272.19）', dirs=(120, 150, 90), color=BLACK)
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu09_P_housha.png')

# =====================================================================
# zu10：問1 J点（BCに直交する線）
# =====================================================================
fig, (ax,) = new_figure('問1　J点は、P点の真南（BCに直交する線との交点）',
                        'BCは真東向き（X＝279.30）。直交する線は真北向きなので、Pを通る線は Y＝293.12 のまま。J ＝（279.30, 293.12）。\n'
                        '回転も交点の公式も要らない。調査図素図の注2「J点はB点とC点を結ぶ直線上にある」。J点の定め方は、問題文の立会い等のオ(イ)のとおり。')
z = Zu(ax)
fit(ax, [E, D, C, B, Pp], margin=0.14, pad_aspect=True)
z.poly(HON, color=BLACK, lw=1.6)
z.poly(I1, color=RED, lw=0, fill=GREEN, alpha=0.25, check=False)
z.line(Pp, J, color=RED, lw=2.4)
z.line(B, C, color=BLUE, lw=2.4)
z.right_angle(J, C, Pp, size=1.0, color=RED)
z.north_arrow()
co = centroid(HON)
for p, n in [(B, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (G, 'G'), (F, 'F')]:
    z.point(p, 'dot')
    z.point_label(p, n, away=co)
z.point(J, 'dot', color=RED)
z.point(Pp, 'dot', color=RED)
z.point_label(Pp, 'P', away=co, color=RED)
z.callout(J, 'J（279.30, 293.12）', dirs=(-100, -70, -130), color=RED, dists=(40, 55, 70))
z.callout(B + (C - B) * 0.2, 'BC　真東向き（X＝279.30）', dirs=(-100, -80, -120), color=BLUE, dists=(40, 55, 70), fs=14)
z.edge_label(Pp, J, '真北向き（Y＝293.12）', co, color=RED, fs=14, ts=(0.4, 0.3, 0.55))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu10_J_ten.png')

# =====================================================================
# zu11：問1 I点（ED上で Y＝293.12）。Pは側溝の北の目印
# =====================================================================
fig, (ax1, ax2) = new_figure('問1　I点は、ED上の点（P点はペンキの目印で道路の中）',
                             '左：I は直線ED上で Y＝293.12 の点。E→Dの間にY座標が30.39増え、Eから20.44増えた所なので I ＝ E ＋ (D − E) × 20.44 ÷ 30.39。\n'
                             '右（拡大）：Pは側溝の北側の目印。I点（ED上）はPの0.50m南。調査図素図の注1「I点は、E点とD点を結ぶ直線上にある」。',
                             ncols=2, width_ratios=[1, 1.1])
ax1.set_xlim(0, 100)
ax1.set_ylim(10, 62)
ax1.axis('off')
ax1.plot([6, 94], [30, 30], color=BLACK, lw=3)
for xx, nm, yv in [(6, 'E', '272.68'), (6 + 88 * 20.44 / 30.39, 'I', '293.12'), (94, 'D', '303.07')]:
    ax1.plot([xx], [30], 'o', ms=11, color=RED if nm == 'I' else BLACK)
    ax1.text(xx, 36, nm, ha='center', va='bottom', fontsize=18, weight='bold', color=RED if nm == 'I' else BLACK)
    ax1.text(xx, 24, f'Y＝{yv}', ha='center', va='top', fontsize=15, color=RED if nm == 'I' else BLACK)
xi = 6 + 88 * 20.44 / 30.39
ax1.annotate('', xy=(xi, 46), xytext=(6, 46), arrowprops=dict(arrowstyle='<->', lw=2, color=RED))
ax1.text((6 + xi) / 2, 48, '20.44', ha='center', va='bottom', fontsize=16, color=RED, weight='bold')
ax1.annotate('', xy=(94, 55), xytext=(6, 55), arrowprops=dict(arrowstyle='<->', lw=2, color=BLUE))
ax1.text(50, 57, '30.39（EからDまで）', ha='center', va='bottom', fontsize=16, color=BLUE, weight='bold')
ax1.text(50, 14, '比 20.44 ÷ 30.39 だけ、EからDへ進む', ha='center', va='center', fontsize=16, color=BLACK)
zb = Zu(ax2, fontsize=14)
Z1, Z2 = E + (D - E) * 0.60, E + (D - E) * 0.76
fit(ax2, [Z1, Z2, Pp + 0.9, I - 1.2], margin=0.05, pad_aspect=True)
zb.line(Z1, Z2, color=BLACK, lw=2.0)
zb.line(Z1 + 0.35, Z2 + 0.35, color=GRAY, lw=1.0)
zb.line(Z1 + 0.05, Z2 + 0.05, color=GRAY, lw=1.0)
zb.line(Pp + 0.6, I - 1.0, color=RED, lw=1.6, ls='--')
zb.north_arrow(length=0.08)
zb.point(Pp, 'dot', color=RED)
zb.point(I, 'concrete', color=RED)
zb.callout(Pp, 'P（300.63, 293.12）', dirs=(150, 180, 120), color=RED, dists=(60, 80))
zb.callout(I, 'I（300.13, 293.12）', dirs=(-30, -60, 0), color=RED, dists=(60, 80))
zb.free_text(I + (Pp - I) * 0.5, 'IP ＝ 0.50', color=RED, fs=15, ha='left', offsets=((20, 22), (30, 30), (20, 38), (40, 40)))
zb.callout(Z1 + (Z2 - Z1) * 0.12 + 0.35, '側溝（位置は模式）', dirs=(100, 120, 80), color=GRAY, dists=(70, 90, 110), fs=13)
zb.edge_label(Z1, Z2, '直線ED（道路境界）', Pp, fs=13, ts=(0.25, 0.35, 0.75))
ALL_PROBLEMS += save(fig, [zb], 'R4_dai21mon_zu11_I_ten.png')

# =====================================================================
# zu12：問2 筆界特定の定義
# =====================================================================
fig, (ax,) = new_figure('問2　筆界特定の定義（不動産登記法第123条）',
                        '筆界特定 ＝（ア：表題登記）がある一筆の土地及びこれに（イ：隣接）する他の土地について、筆界の現地における（ウ：位置）を特定すること\n'
                        '（その位置を特定することができないときは、その位置の（エ：範囲）を特定すること）。所有権界のAB線は、筆界特定で決めるものではない。')
z = Zu(ax)
fit(ax, [E, D, C, B, P(279.3, 262.0)], margin=0.10, pad_aspect=True)
z.poly(HON, color=GRAY, lw=1.2, check=False)
for s_ in [(E, D), (D, C), (C, G)]:
    z.segments.append((xy(s_[0]), xy(s_[1])))
ax.plot([xy(p)[0] for p in (E, F, G)], [xy(p)[1] for p in (E, F, G)], color=ORANGE, lw=38, alpha=0.25,
        solid_capstyle='round', solid_joinstyle='round', zorder=1)
z.poly([E, F, G], color=RED, lw=3.0, closed=False)
z.line(A, B, color=GRAY, lw=1.6, ls='--')
z.north_arrow()
co = centroid(HON)
for p, n in [(E, 'E'), (F, 'F'), (G, 'G'), (A, 'A'), (B, 'B')]:
    z.point(p, 'dot', color=RED if n in 'EFG' else GRAY)
    z.point_label(p, n, away=co, color=RED if n in 'EFG' else GRAY)
z.free_text(co, '184番1\n（ア：表題登記がある一筆の土地）', fs=15)
z.free_text(P(289.0, 267.3), '185番3\n（イ：隣接する他の土地）', fs=15)
z.callout(F + (G - F) * 0.5, 'ウ：筆界の「位置」（E→F→G）', dirs=(-150, 180, -120), color=RED, dists=(90, 120))
z.callout(E + (F - E) * 0.35 + P(0, 0.9), 'エ：決めきれないときは「位置の範囲」', dirs=(10, 25, -10), color=ORANGE,
          dists=(80, 110, 140))
z.callout(A + (B - A) * 0.62, 'AB線＝所有権界（筆界特定の対象外）', dirs=(0, 20, -20), color=GRAY, dists=(90, 120))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu12_hikkai_tokutei.png')

# =====================================================================
# zu13：問3 部分ごとの使い方と地目（地目が変わったのは中央部分だけ）
# =====================================================================
fig, (ax,) = new_figure('問3　どの部分の地目が変わったか（変わったのは中央部分だけ）',
                        '東側部分は9月17日から183番1の倉庫の敷地。西側部分は悠人さんの居宅・車庫の敷地と一体で使われている宅地。\n'
                        '建物の敷地として使い続ける土地は宅地のまま。10月5日から月極駐車場にした中央部分だけが、宅地でなくなる。',
                        )
z = Zu(ax)
fit(ax, [E, D, C, B, P(290.0, 262.0), P(290.0, 306.0)], margin=0.08, pad_aspect=True)
EAST, MID, WEST = I1, RO, HA
z.poly(EAST, fill=GREEN)
z.poly(MID, fill=ORANGE)
z.poly(WEST, fill=BLUE, alpha=0.4)
z.north_arrow()
z.free_text(centroid(EAST), '東側部分\n9月17日から倉庫の敷地\n宅地のまま（変更なし）', fs=14)
z.free_text(centroid(MID), '中央部分\n10月5日から月極駐車場\n宅地 → 雑種地\n（地目が変わる）', fs=15, color=RED, weight='bold')
z.callout(centroid(WEST), '西側部分\n悠人さんの居宅・車庫の\n敷地と一体　宅地のまま', dirs=(150, 180, 120), color=BLUE,
          dists=(90, 120), fs=14)
for p, n in [(A, 'A'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (H, 'H'), (I, 'I'), (J, 'J')]:
    z.point(p, 'dot')
    z.point_label(p, n, away=centroid(MID))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu13_chimoku_3bubun.png')

# =====================================================================
# zu14：問3 登記の目的（一部地目変更と分筆を一の申請情報で）
# =====================================================================
fig, ax = board(9, '問3　登記の目的は「土地一部地目変更・分筆登記」')
rbox(ax, 1, 56, 48, 36, '① 地目の変更の登記（不動産登記法第37条）',
     '地目が変わったら、変わった日から1か月以内に申請\n本件土地は、中央部分だけが雑種地になった\n→ 一筆の一部の地目変更（一部地目変更）', ORANGE)
rbox(ax, 51, 56, 48, 36, '② 分筆の登記（同法第39条第2項）',
     '一筆の土地の一部が別の地目になったら、その部分を分ける\n本件土地は、東側・中央・西側の3筆にする\n→ 分筆の登記', BLUE)
arrow(ax, 25, 54, 45, 44)
arrow(ax, 75, 54, 55, 44)
rbox(ax, 20, 22, 60, 20, '一の申請情報（不動産登記規則第35条第7号）',
     '表題部の変更の登記と、同じ土地の分筆の登記は、一の申請情報で申請できる\n問3：必要な土地の表示に関する登記が複数あるときは、一の申請情報で申請する', RED, fs_b=13)
arrow(ax, 50, 20, 50, 13)
rbox(ax, 20, 1, 60, 11, '登記の目的　土地一部地目変更・分筆登記', '', RED, fs_h=19)
put_board(fig, 'R4_dai21mon_zu14_mokuteki.png')

# =====================================================================
# zu15：問3 分筆後の地番（問題文の注7）
# =====================================================================
fig, (ax,) = new_figure('問3　分筆後の地番（問題文の注7）',
                        '問題文の注7：分筆後の土地のうち最も東側の土地を184番1とし、その余の土地は新地番を184番3から東側から順に付番する。\n'
                        '184番2は平成16年の拡幅で道路として分筆済み（使用済み）なので、新しい地番は184番3から。東側部分（イ）の地番は変わらない。')
z = Zu(ax)
fit(ax, [E, D, C, B, P(290.0, 262.0), P(290.0, 306.0)], margin=0.08, pad_aspect=True)
z.poly(I1, fill=GREEN)
z.poly(RO, fill=ORANGE)
z.poly(HA, fill=BLUE, alpha=0.4)
z.north_arrow()
z.free_text(centroid(I1), '（イ）184番1\n最も東', fs=16)
z.free_text(centroid(RO), '（ロ）184番3\n次に東', fs=16)
z.callout(centroid(HA), '（ハ）184番4\n最も西', dirs=(150, 180, 120), color=BLUE, dists=(90, 120), fs=16)
for p, n in [(A, 'A'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (H, 'H'), (I, 'I'), (J, 'J')]:
    z.point(p, 'dot')
    z.point_label(p, n, away=centroid(RO))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu15_chiban_chuu7.png')


# =====================================================================
# 座標法の計算過程の図（多角形＋各項の表）
# =====================================================================
def calc_poly_fig(title, caption, pts, names, head, rows_extra, foot, name, edge_ref=None, label_dists=(14, 20, 28),
                  tweak=None, margin=0.14):
    tm = terms(pts)
    n = len(pts)
    fig_, (ax_, ax2_) = new_figure(title, caption, ncols=2, width_ratios=[1.05, 1])
    z_ = Zu(ax_)
    fit(ax_, pts, margin=margin, pad_aspect=True)
    z_.poly(pts, lw=2.2, fill=BLUE)
    z_.north_arrow()
    ctr = centroid(pts)
    for i in range(n):
        z_.edge_label(pts[i], pts[(i + 1) % n], CIRC[i], edge_ref or ctr, color=RED, fs=16, rotate=False,
                      dists=label_dists)
    for p, nm in zip(pts, names):
        mark(z_, p, nm, ctr)
    if tweak:
        tweak(z_)
    rows = [(f'{CIRC[i]}　{names[i]}・Conjg({names[(i + 1) % n]})', fmt_num(tm[i]), BLACK) for i in range(n)]
    rows += [('合計（表示の iの係数）', fmt_num(sum(tm)), RED)] + rows_extra
    table_panel(ax2_, head, rows, foot)
    return save(fig_, [z_], name)


# zu16：（イ）の面積（座標法4項）
ALL_PROBLEMS += calc_poly_fig(
    '問3　（イ）184番1の面積（座標法　C→D→I→Jの4項）',
    '頂点を順に回り、P・Conjg(次の点) の iの係数だけを足す（実部は使わない）。①〜④は記事の電卓の4行と同じ順。\n'
    '合計の絶対値を2で割って 212.2335㎡。宅地は小数第2位未満を切り捨てて 212.23㎡。これが申請書の（イ）の行の地積。',
    I1, 'CDIJ', '各項（P・Conjg(次の点) の iの係数）',
    [('|合計| ÷ 2', '212.2335㎡', RED), ('宅地は小数第2位未満切り捨て', '212.23㎡', RED)],
    '東側部分は変数で B＝I点・Y＝J点を使う\n（第4章でB・Yに入れた点）', 'R4_dai21mon_zu16_i_menseki_4kou.png')

# =====================================================================
# zu17：（イ）の面積を対角線で出す別解
# =====================================================================
dz = (I - C).conjugate() * (D - J)
assert abs(dz - P(355.7164, 424.467)) < 1e-9 and abs(abs(dz.imag) / 2 - 212.2335) < 1e-9
dz_ha = (H - E).conjugate() * (F - A)
assert abs(abs(dz_ha.imag) / 2 - 15.0604) < 1e-9
fig, (ax,) = new_figure('問3　（イ）の面積を対角線で出す別解',
                        '4点を順に回る式 C・Conjg(D) ＋ D・Conjg(I) ＋ I・Conjg(J) ＋ J・Conjg(C) と同じ面積を、対角線2本で1回で出せる。\n'
                        'Conjg(I − C) × (D − J) ＝ 355.7164 ＋ 424.467i　→　iの係数 424.467 ÷ 2 ＝ 212.2335㎡\n'
                        '（ハ）も Conjg(H − E) × (F − A) で 15.0604㎡')
z = Zu(ax)
fit(ax, HON + [P(285.0, 313.0)], margin=0.08, pad_aspect=True)
z.poly(HON, color=GRAY, lw=1.2)
z.poly(I1, color=BLACK, lw=2.0, fill=GREEN)
z.line(C, I, color=RED, lw=2.2, ls='--')
z.line(J, D, color=ORANGE, lw=2.2, ls='--')
z.north_arrow()
for p, n in [(C, 'C'), (D, 'D'), (I, 'I'), (J, 'J')]:
    z.point(p, 'dot')
    z.point_label(p, n, away=centroid(I1))
for p, n in [(E, 'E'), (F, 'F'), (G, 'G')]:
    z.point(p, 'dot', color=GRAY)
    z.point_label(p, n, away=centroid(HON), color=GRAY)
z.free_text(centroid(RO), '（ロ）184番3', fs=15, color=GRAY)
z.callout(C + (I - C) * 0.8, '対角線1　I − C', dirs=(200, 190, 210), color=RED, dists=(90, 120, 150))
z.callout(J + (D - J) * 0.75, '対角線2　D − J', dirs=(-20, 0, -40), color=ORANGE, dists=(80, 100, 120))
z.callout(centroid(I1) + (C - centroid(I1)) * 0.35, '（イ）184番1　212.2335㎡', dirs=(-40, -30, -50), color=BLACK, fs=16,
          dists=(150, 180, 210))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu17_taikakusen.png')

# =====================================================================
# zu18：（ロ）の面積（座標法5項）
# =====================================================================
ALL_PROBLEMS += calc_poly_fig(
    '問3　（ロ）184番3の面積（座標法　A→I→J→G→Hの5項）',
    '頂点を順に回り、P・Conjg(次の点) の iの係数だけを足す。①〜⑤は記事の電卓の5行と同じ順。C点の変数にはH点を入れ直して使う。\n'
    '合計の絶対値を2で割って 357.44415㎡。地目は雑種地なので、端数の切り捨て方は次の図。',
    RO, 'AIJGH', '各項（P・Conjg(次の点) の iの係数）',
    [('|合計| ÷ 2', '357.44415㎡', RED)],
    '雑種地の地積は、小数第2位まで書かない\n→ 次の図で、1㎡未満の切り捨てを確かめる', 'R4_dai21mon_zu18_ro_menseki_5kou.png',
    label_dists=(16, 22, 30))

# =====================================================================
# zu19：地積の端数処理（宅地は小数第2位まで、雑種地は整数）
# =====================================================================
fig, ax = board(7.6, '問3　地積の端数処理　宅地は小数第2位未満、雑種地（10㎡超）は1㎡未満を切り捨てる')
rbox(ax, 1, 40, 48, 52, '宅地（（イ）と（ハ））', '小数第2位未満を切り捨てる\n（イ）212.2335 → 212.23㎡\n（ハ）15.0604 → 15.06㎡', BLUE, fs_b=15)
rbox(ax, 51, 40, 48, 52, '雑種地で10㎡を超える（（ロ））', '1㎡未満を切り捨てる（小数は書かない）\n（ロ）357.44415 → 357㎡\n誤り：357.44㎡（宅地の書き方）', RED, fs_b=15)
rbox(ax, 1, 3, 98, 32, '不動産登記規則第100条',
     '地積は、水平投影面積により、平方メートルを単位として定め、一平方メートルの百分の一\n'
     '（宅地及び鉱泉地以外の土地で十平方メートルを超えるものについては、一平方メートル）未満の端数は、切り捨てる。\n'
     '→ 地目が雑種地に変わった（ロ）は、分筆で生まれた瞬間から雑種地なので、整数で書く', RED, fs_b=14)
put_board(fig, 'R4_dai21mon_zu19_hasuu.png')

# =====================================================================
# zu20：精度区分は地域で決まる（規則第10条）
# =====================================================================
fig, ax = board(9.5, '問3　精度区分は地域で決まる（本件土地は村落地域なので乙1の7.17㎡）')
rbox(ax, 1, 40, 56, 52, '不動産登記規則第10条第4項（誤差の限度）', '', BLUE)
ROWS20 = [('市街地地域（主に宅地が占める地域及びその周辺）', '精度区分 甲2まで', GRAY),
          ('村落・農耕地域（主に田・畑・塩田が占める地域及びその周辺）', '精度区分 乙1まで', RED),
          ('山林・原野地域（主に山林・牧場・原野が占める地域及びその周辺）', '精度区分 乙3まで', GRAY)]
y = 77
for lt, rt, col in ROWS20:
    ax.add_patch(Rectangle((2.5, y - 6), 53, 12, facecolor='#fdecea' if col == RED else 'white',
                           edgecolor=col, lw=2.2 if col == RED else 1.2))
    ax.text(4, y + 2.5, lt, ha='left', va='center', fontsize=12.5, color=BLACK)
    ax.text(4, y - 3, rt, ha='left', va='center', fontsize=15, color=col, weight='bold')
    y -= 14.5
rbox(ax, 59, 40, 40, 52, '公差の表（問題文 584.75㎡）', '', BLUE)
TB = [('甲1', '0.96', GRAY), ('甲2', '2.39', GRAY), ('甲3', '4.79', GRAY), ('乙1', '7.17', RED), ('乙2', '14.36', GRAY),
      ('乙3', '28.73', GRAY)]
y = 77
for nm, v, col in TB:
    ax.add_patch(Rectangle((60.5, y - 3.4), 37, 6.4, facecolor='#fdecea' if col == RED else 'white',
                           edgecolor=col, lw=2.2 if col == RED else 1.0))
    ax.text(63, y, nm, ha='left', va='center', fontsize=15, color=col, weight='bold')
    ax.text(96, y, f'{v}㎡', ha='right', va='center', fontsize=15, color=col, weight='bold')
    y -= 7.2
rbox(ax, 1, 3, 98, 32, '本件土地は「村落地域」と問題文に書いてある（不動産登記規則第10条第2項第2号）',
     '地目が宅地だからといって、市街地地域の甲2（2.39㎡）にしない。精度区分は、その土地がどんな地域にあるかで決まる。\n'
     '村落・農耕地域の誤差の限度は乙1まで（同条第4項第2号）→ 公差は 7.17㎡。\n'
     '今年は甲2の2.39㎡で比べても範囲内だが、年度によっては地積更正が要るかどうかの結論が変わる。', RED, fs_b=14)
put_board(fig, 'R4_dai21mon_zu20_seido_kubun.png')

# =====================================================================
# zu21：地積更正が要るかの判定（数直線）
# =====================================================================
setup_font()
fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問3　地積更正が要るかの判定（精度区分 乙1）', fontsize=24, weight='bold', y=0.96)
ax = fig.add_axes([0.06, 0.30, 0.88, 0.50])
ax.set_xlim(575.5, 594.0)
ax.set_ylim(-1.8, 2.6)
ax.axis('off')
ax.plot([576, 593.5], [0, 0], color=BLACK, lw=2)
for v in range(576, 594, 2):
    ax.plot([v, v], [-0.08, 0.08], color=BLACK, lw=1.2)
    ax.text(v, -0.28, f'{v}', ha='center', va='top', fontsize=13, color=GRAY)
ax.axvspan(584.75 - 7.17, 584.75 + 7.17, ymin=0.34, ymax=0.50, color=GREEN, alpha=0.25)
ax.text(584.75, 1.05, '乙1の公差の範囲（584.75 ± 7.17）', ha='center', va='bottom', fontsize=15, color=GREEN)
ax.axvspan(584.75 - 2.39, 584.75 + 2.39, ymin=0.50, ymax=0.56, color=GRAY, alpha=0.25)
ax.text(584.75 + 2.6, 0.53, '（参考）甲2の範囲 ±2.39', ha='left', va='center', fontsize=12, color=GRAY)
ax.plot([584.75], [0], 'o', ms=12, color=BLUE)
ax.text(582.2, -0.75, '登記記録\n584.75㎡', ha='center', va='top', fontsize=16, color=BLUE, weight='bold')
ax.plot([584.8248], [0], 'o', ms=9, color=RED)
ax.plot([584.73805], [0], 'o', ms=9, color=PURPLE)
ax.text(587.6, -0.75, '分筆前の実測 584.8248㎡（差0.07）\n分筆後3筆の合計 584.73805㎡（差0.01）', ha='left', va='top',
        fontsize=14, color=RED, weight='bold')
ax.text(584.75, 1.8, '差はどちらも公差 7.17㎡ の範囲内　→　地積更正は不要', ha='center', va='bottom', fontsize=17,
        color=RED, weight='bold')
fig.text(0.5, 0.15, '分筆後の合計は 212.2335 ＋ 357.44415 ＋ 15.0604 ＝ 584.73805㎡。1筆で測った 584.8248㎡ との差は、丸めたI点がEDの直線からわずかにずれるため。\n'
         '問題文：座標法の求積値と登記記録の差が公差の範囲内なら、地積に関する表示の登記は申請しない（準則第72条第1項も、分筆後の地積の合計で比べる）。',
         ha='center', va='center', fontsize=15)
path = os.path.join(OUT, 'R4_dai21mon_zu21_kousa.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] R4_dai21mon_zu21_kousa.png: 数直線（固定配置）\n  →', path)

# =====================================================================
# zu22：土地の表示の1行目（分筆前の行）の地積は登記記録のまま
# =====================================================================
fig, ax = board(7.4, '問3　土地の表示の1行目（分筆前）は、登記記録の地積を書く')
rbox(ax, 1, 46, 48, 46, '誤り　実測の584.82をそのまま書く',
     '1行目　184番1　宅地　584.82\n座標法で出した 584.8248 を使うと、\n地積が変わった（地積更正）ように見える', GRAY, fs_b=15)
rbox(ax, 51, 46, 48, 46, '正しい　登記記録の584.75を書く',
     '1行目　184番1　宅地　584.75（原因の欄は空欄）\n実測との差は公差の範囲内 → 地積に関する表示の登記はしない\n→ 分筆前の行は、登記記録のとおりに写すだけ', RED, fs_b=15)
rbox(ax, 1, 3, 98, 38, '分筆後の3行は、分けた後の地積を書く',
     '（イ）の行：212.23（座標法の求積値。宅地）\n（ロ）の行：357（雑種地は1㎡未満切り捨て）　（ハ）の行：15.06\n'
     '（イ）〜（ハ）を足しても584.73805㎡で、登記記録の584.75㎡とは0.01㎡ちがう（公差の範囲内なので、そのまま）', BLUE, fs_b=14.5)
put_board(fig, 'R4_dai21mon_zu22_bunpitsumae_chiseki.png')

# =====================================================================
# zu23：（イ）の行の原因（一部地目変更は日付あり、分筆は日付なし）
# =====================================================================
fig, ax = board(8.2, '問3　（イ）の行の原因　一部地目変更は日付付き、分筆は日付なし')
rbox(ax, 1, 52, 48, 40, '一部地目変更（報告的な登記）',
     '現地で起きた事実を登記に報告する\n→ その事実が起きた日を書く\n「令和4年10月5日一部地目変更」', ORANGE, fs_b=15)
rbox(ax, 51, 52, 48, 40, '分筆（形成的な登記）',
     '登記をすることで初めて土地が分かれる\n→ 日付は書かない\n「③184番1、184番3、184番4に分筆」', BLUE, fs_b=15)
rbox(ax, 1, 3, 98, 42, '書く場所は（イ）の行（分筆前の184番1の行）',
     '10月5日に起きたのは、分筆前の184番1の一部の地目変更なので、184番1のまま残る（イ）の行に書く。\n'
     '（イ）の行の原因　　令和4年10月5日一部地目変更\n　　　　　　　　　③184番1、184番3、184番4に分筆\n'
     '（ロ）（ハ）の行の原因は「184番1から分筆」だけ（日付も一部地目変更も書かない）。この違いは建物の区分の登記と同じ', RED, fs_b=14.5)
put_board(fig, 'R4_dai21mon_zu23_i_gyou_genin.png')

# =====================================================================
# zu24：（ロ）の行は最初から雑種地
# =====================================================================
fig, ax = board(7.4, '問3　（ロ）184番3の行は、分筆で生まれた瞬間から雑種地')
rbox(ax, 1, 46, 48, 46, '誤り　宅地のまま、357.44',
     '（ロ）184番3　宅地　357.44\n分筆前と同じ宅地だと考え、小数第2位まで書いている', GRAY, fs_b=15)
rbox(ax, 51, 46, 48, 46, '正しい　雑種地、357',
     '（ロ）184番3　雑種地　357　184番1から分筆\n中央部分は10月5日から月極駐車場 → 新しい土地は最初から雑種地\n→ 地目の変更は（イ）の行で報告済み。（ロ）の行は結果の姿を書く', RED, fs_b=14.5)
rbox(ax, 1, 3, 98, 38, '地目が決める3つのこと',
     '① 地目の欄　雑種地\n② 地積の欄　1㎡未満切り捨ての357（宅地のように小数第2位まで書かない）\n'
     '③ 原因の欄　「184番1から分筆」だけ（一部地目変更の日付は（イ）の行）', BLUE, fs_b=14.5)
put_board(fig, 'R4_dai21mon_zu24_ro_gyou_chimoku.png')

# =====================================================================
# zu25：登録免許税は分筆後の個数
# =====================================================================
fig, (ax,) = new_figure('問3　登録免許税は分筆後の土地の個数（3個で金3,000円）',
                        '分筆の登録免許税は、分筆後の土地の個数1個につき1,000円（登録免許税法別表第一の一（十三）イ）。元の184番1も分筆後の土地の1つなので3個。\n'
                        '新しくできる2筆（184番3・184番4）だけで2,000円としない。一部地目変更には登録免許税はかからない。')
z = Zu(ax)
fit(ax, [E, D, C, B, P(290.0, 262.0), P(290.0, 306.0)], margin=0.08, pad_aspect=True)
z.poly(I1, fill=GREEN)
z.poly(RO, fill=ORANGE)
z.poly(HA, fill=BLUE, alpha=0.4)
z.north_arrow()
z.free_text(centroid(I1), '184番1\n① 1,000円', fs=16)
z.free_text(centroid(RO), '184番3\n② 1,000円', fs=16)
z.callout(centroid(HA), '184番4　③ 1,000円', dirs=(150, 180, 120), color=BLUE, dists=(90, 120), fs=16)
z.callout(centroid(RO) + P(-6, 0), '1,000円 × 3個 ＝ 金3,000円', dirs=(-100, -80, -120), color=RED, dists=(90, 120), fs=18,
          box_color='white')
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu25_tourokumenkyozei.png')

# =====================================================================
# zu26：添付書類は2つだけ
# =====================================================================
fig, ax = board(9.5, '問3　添付書類は「地積測量図」と「代理権限証書」の2つだけ')
rows26 = [('地積測量図', '要る', '分筆の登記には、分筆後の土地の区画を示す地積測量図を付ける（問4で作る）', RED),
          ('代理権限証書', '要る', '土地家屋調査士の法務太郎が、春野朝子さんの代理で申請する', RED),
          ('登記識別情報・印鑑証明書', '要らない', '合筆の登記や、権利に関する登記の書類。分筆と地目変更の申請には付けない（問5の合筆と区別）', GRAY),
          ('承諾書（抵当権者など）', '要らない', '乙区は登記事項なし。承諾をもらう相手の権利者がいない', GRAY),
          ('相続証明書・代位原因証書', '要らない', '春野朝子さんが所有権の登記名義人として自分で申請する（甲区のとおり）', GRAY)]
y = 82
for nm, yn, why, col in rows26:
    ax.add_patch(Rectangle((1, y - 6.4), 98, 13, facecolor='#fdecea' if col == RED else '#f6f8fb', edgecolor=col, lw=2))
    ax.text(3, y + 1.8, nm, ha='left', va='center', fontsize=17, color=col, weight='bold')
    ax.text(3, y - 3, why, ha='left', va='center', fontsize=13, color=BLACK)
    ax.text(97, y, yn, ha='right', va='center', fontsize=20, color=col, weight='bold')
    y -= 15.5
put_board(fig, 'R4_dai21mon_zu26_tenpu_shorui.png')

# =====================================================================
# zu27：辺長の端数処理（問題文の注4）
# =====================================================================
KEY = {'EA': (E, A), 'AI': (A, I), 'ID': (I, D), 'GH': (G, H), 'HF': (H, F), 'FE': (F, E), 'AH': (A, H)}
raw_txt = {n_: fmt_num(abs(q_ - p_)) for n_, (p_, q_) in KEY.items()}
assert raw_txt == {'EA': '1.2159…', 'AI': '19.3256…', 'ID': '10.0001…', 'GH': '8.4846…', 'HF': '3.2590…',
                   'FE': '8.9502…', 'AH': '11.8168…'}, raw_txt
third = {n_: str(int(abs(q_ - p_) * 1000 + 1e-9) % 10) for n_, (p_, q_) in KEY.items()}
fig, ax = board(10, '問4　辺長は小数第3位を四捨五入（問題文の注4）　AIは19.3256…なので19.33')
ax.text(2, 93, '辺', ha='left', va='center', fontsize=15, color=BLUE, weight='bold')
ax.text(14, 93, '求め方', ha='left', va='center', fontsize=15, color=BLUE, weight='bold')
ax.text(60, 93, '電卓の表示', ha='right', va='center', fontsize=15, color=BLUE, weight='bold')
ax.text(78, 93, '小数第3位', ha='center', va='center', fontsize=15, color=BLUE, weight='bold')
ax.text(94, 93, '書く値', ha='right', va='center', fontsize=15, color=BLUE, weight='bold')
ROWS27 = [('DC', '引き算（軸に平行な辺）', '301.13 − 279.30', '0', '21.83', GRAY), ('CJ', '引き算', '303.07 − 293.12', '0', '9.95', GRAY),
          ('JG', '引き算', '293.12 − 279.15', '0', '13.97', GRAY), ('IJ', '引き算', '300.13 − 279.30', '0', '20.83', GRAY)]
ROWS27 += [(n_, 'Abs（斜めの辺）', raw_txt[n_], third[n_], SIDES[n_][2], RED if n_ == 'AI' else BLACK)
           for n_ in ['EA', 'AI', 'ID', 'GH', 'HF', 'FE', 'AH']]
y = 85
for nm, how, disp_, d3, val, col in ROWS27:
    ax.add_patch(Rectangle((1, y - 3.4), 98, 6.6, facecolor='#fdecea' if col == RED else '#f6f8fb', edgecolor=col,
                           lw=2 if col == RED else 1.0))
    ax.text(2, y, nm, ha='left', va='center', fontsize=15, color=col, weight='bold')
    ax.text(14, y, how, ha='left', va='center', fontsize=14, color=BLACK)
    ax.text(60, y, disp_, ha='right', va='center', fontsize=15, color=col)
    ax.text(78, y, d3, ha='center', va='center', fontsize=15, color=col)
    ax.text(94, y, val, ha='right', va='center', fontsize=16, color=col, weight='bold')
    y -= 7.2
ax.text(2, 83 - 7.2 * len(ROWS27) - 1, '分筆線は IJ 20.83 と AH 11.82。AI は 19.3256… の小数第3位が5なので切り上げて 19.33（19.32は誤り）。',
        ha='left', va='top', fontsize=15, color=RED, weight='bold')
put_board(fig, 'R4_dai21mon_zu27_hencho_hasuu.png')

# =====================================================================
# zu28：分筆線はAからHまで（Bは描かない、Hに境界標はない）
# =====================================================================
fig, (ax,) = new_figure('問4　分筆線はA点からH点まで（B点は描かない、H点に境界標はない）',
                        'H→B→Gの三角形は悠人さんの185番3の土地。本件土地の地積測量図に描く分筆線は、A点からH点まで。\n'
                        'H点はAB線とFGの交点で、境界標を設置する必要がない（問題文の立会い等ウ）。A点には金属標を設置する。')
z = Zu(ax)
fit(ax, [E, D, C, B, P(290.0, 262.0)], margin=0.12, pad_aspect=True)
z.poly(HON, color=BLACK, lw=2.0)
z.line(A, H, color=RED, lw=3.0)
z.line(H, B, color=GRAY, lw=1.6, ls=':')
z.line(I, J, color=RED, lw=3.0)
z.poly(HBG, color=GRAY, lw=1.0, ls=':', fill=GRAY, alpha=0.18, check=False)
z.north_arrow()
co = centroid(HON)
for p, n in [(A, 'A'), (C, 'C'), (J, 'J'), (D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (I, 'I')]:
    mark(z, p, n, co)
z.point(H, 'dot', color=RED, size=5)
z.point_label(H, 'H', away=co, color=RED)
z.point(B, 'dot', color=GRAY)
z.point_label(B, 'B', away=centroid(HBG), color=GRAY)
z.callout(A + (H - A) * 0.55, '分筆線 AH（11.82）', dirs=(180, 200, 160), color=RED, dists=(90, 120, 150))
z.callout(centroid(HBG), '△HBG は185番3\n（描かない・B点も描かない）', dirs=(-60, -30, -90), color=GRAY, dists=(70, 95, 120), fs=14)
z.callout(H, 'H点　境界標なし', dirs=(-20, -40, 0), color=RED, dists=(60, 80, 100), fs=14)
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu28_bunpitsusen_AH.png')

# =====================================================================
# zu29：地積測量図に書くもの・書かないもの
# =====================================================================
fig, ax = board(10, '問4　地積測量図に書くもの・書かないもの')
rbox(ax, 1, 3, 54, 89, '書くもの', '', GREEN)
KAKU = ['各辺の長さ（11本）…小数第3位を四捨五入（問題文の注4）', '分筆線 IJ・AH', '地番（（イ）184－1・（ロ）184－3・（ハ）184－4）',
        '方位（答案用紙に印刷なし。自分で描く）', '隣接地の地番（183－1・183－2・184－2・185－6・185－3・196）と道路',
        '境界標（A・C・Jは金属標、D・E・F・G・Iはコンクリート杭）', '基準点T1・T2の位置と点名（問題文の注6）',
        '欄の記入：地番「184番1、184番3、184番4」・土地の所在「A市B字八幡」']
y = 82
for t in KAKU:
    ax.text(3, y, '・' + t, ha='left', va='center', fontsize=13.5)
    y -= 9.3
rbox(ax, 57, 3, 42, 89, '書かないもの', '', RED)
KAKANAI = ['各筆界点の座標値（問題文の注5）', '座標系の番号（問題文の注5）', '地積とその求積方法（問題文の注5）', '測量年月日（問題文の注5）',
           'T1・T2の座標値（問題文の注6）', 'B点（本件土地の筆界点ではない）', 'H点の境界標（設置不要）', '作成者・申請人（「（略）」と印刷済み）']
y = 82
for t in KAKANAI:
    ax.text(59, y, '・' + t, ha='left', va='center', fontsize=13.5)
    y -= 9.3
fig.text(0.5, 0.025, '縮尺1/250は答案用紙に印刷済み（問題文の注4）', ha='center', fontsize=14, color=GRAY)
put_board(fig, 'R4_dai21mon_zu29_kaku_kakanai.png')

# =====================================================================
# zu30：問4 地積測量図の完成見本（答案用紙の第4欄の枠の中に、縮尺1/250の実際の大きさで描く）
#   試験の答案用紙（原本 `../touan_youshi/R4_dai21mon_touan_youshi.pdf` の2ページ目。A3横）の枠・欄の位置と大きさを、
#   PDFの罫線からmmで測ったとおりに描く（2026-10-26）。黒は印刷済み、青は書き込み。画像の中に図番は入れない
# =====================================================================
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


def ftext(x, y, s_, fs=13, ha='center', color=BLACK, **kw):
    fig.text(fx3(x), fy3(y), s_, fontsize=fs, ha=ha, va='center', color=color, **kw)


frect(56.3, 12.2, 406.9, 274.8, lw=1.2)                      # 用紙の外枠（二重線）
frect(57.1, 13.0, 406.1, 274.0, lw=1.2)
ftext(58.6, 18.8, '第4欄', fs=15, ha='left', weight='bold')
frect(*ORIG_FRAME_MM, lw=1.8)                                  # 図を描く枠（横302mm・縦231mm）
fline(231.6, 25.8, 231.6, 35.8)                                # 折り目の印（上・下）
fline(231.6, 246.8, 231.6, 256.8)
frect(240.6, 15.8, 302.6, 25.8)                                # 地番の欄
fline(264.6, 15.8, 264.6, 25.8)
ftext(252.6, 20.8, '地　　番', fs=12)
ftext(283.6, 20.8, '184番1、184番3、184番4', fs=9.5, color=INK, weight='bold')
frect(240.6, 25.8, 382.6, 35.8)                                # 土地の所在の欄
fline(264.6, 25.8, 264.6, 35.8)
ftext(252.6, 30.8, '土地の所在', fs=12)
ftext(268.0, 30.8, 'Ａ市Ｂ字八幡', fs=15, ha='left', color=INK, weight='bold')
ftext(342.6, 20.8, '地　積　測　量　図', fs=19)
frect(80.6, 256.8, 223.6, 271.3)                               # 作成者の欄
fline(99.6, 256.8, 99.6, 271.3)
ftext(90.1, 263.9, '作 成 者', fs=11)
ftext(144.5, 263.9, '（略）', fs=13)
ftext(223.4, 267.7, '（令和４年○月○日作成）', fs=11, ha='right')
frect(239.6, 256.8, 382.6, 271.3)                              # 申請人の欄
fline(258.6, 256.8, 258.6, 271.3)
ftext(249.1, 263.9, '申 請 人', fs=11)
ftext(303.5, 263.9, '（略）', fs=13)
fline(348.5, 256.8, 348.5, 271.3)                              # 縮尺の欄（1/250は印刷済み）
fline(358.6, 256.8, 358.6, 271.3)
ftext(353.5, 263.9, '縮尺', fs=10)
fline(362.0, 269.2, 379.0, 258.8, lw=1.0)
ftext(368.4, 260.8, '1', fs=11)
ftext(374.5, 266.8, '250', fs=11)
fig.text(0.5, 0.60 / SH3,
         '黒は答案用紙に印刷済みのもの（枠、欄の見出し、作成者・申請人の「（略）」、作成日の欄、縮尺 1／250）。青は欄への記入。図は縮尺1/250（1m ＝ 4mm）で枠の中に描く。\n'
         '書くもの：地番（184番1、184番3、184番4）、土地の所在（Ａ市Ｂ字八幡）、辺長11本、（イ）（ロ）（ハ）の符号と地番、境界標の記号、方位記号（印刷されていないので必ず描く）、\n'
         '隣接地の地番、基準点T1・T2の位置と点名（問題文の注6）。書かないもの：座標値・座標系の番号・地積と求積方法・測量年月日（問題文の注5）、B点。H点には境界標がない。',
         ha='center', va='center', fontsize=13, linespacing=1.6)
ax = fig.add_axes([fx3(80.6), fy3(256.8), fx3(382.6) - fx3(80.6), fy3(25.8) - fy3(256.8)])
fw_m = (ORIG_FRAME_MM[2] - ORIG_FRAME_MM[0]) / 4               # 枠の中の東西（Y）の長さ（m）75.5
fh_m = (ORIG_FRAME_MM[3] - ORIG_FRAME_MM[1]) / 4               # 南北（X）の長さ（m）57.75
c3 = P(291.2, 288.9)
fit(ax, [c3 + P(-fh_m / 2, -fw_m / 2), c3 + P(fh_m / 2, fw_m / 2)], margin=0.0, pad_aspect=True)
assert abs(((ax.get_xlim()[1] - ax.get_xlim()[0]) - fw_m)) < 0.05, ax.get_xlim()
z = Zu(ax, fontsize=15)
fit(ax, [c3 + P(-fh_m / 2, -fw_m / 2), c3 + P(fh_m / 2, fw_m / 2)], margin=0.0, pad_aspect=True)
z.poly(HON, lw=2.0)
z.line(I, J, lw=2.0)
z.line(A, H, lw=2.0)
z.line(E, E + (E - D) * 0.10, lw=1.0)
z.line(D, D + (D - E) * 0.10, lw=1.0)
z.line(G, G + (G - C) * 0.25, lw=1.0)
z.line(C, C + (C - G) * 0.10, lw=1.0)
z.line(D, D + 1.8, lw=1.0)
z.line(C, C - 2.0, lw=1.0)
z.line(E, E + 1.8, lw=1.0)
z.north_arrow(pos=(0.07, 0.80))
co = centroid(HON)
for n, (p, q, s_) in SIDES.items():
    if n == 'EA':
        z.free_text(E + (A - E) * 0.5, s_, fs=14, offsets=((16, 24), (22, 30), (28, 36), (14, 40)))
        continue
    ref = {'IJ': centroid(I1), 'AH': centroid(RO)}.get(n, co)
    z.edge_label(p, q, s_, ref, fs=14, outward=(n not in ('IJ', 'AH')),
                 dists=(9, 15, 22), ts=(0.5, 0.38, 0.62, 0.28, 0.72))
z.free_text(centroid(I1), '（イ）\n184－1', fs=17)
z.free_text(centroid(RO), '（ロ）\n184－3', fs=17)
z.callout(centroid(HA), '（ハ）184－4', dirs=(225, 240, 210), fs=16, dists=(100, 130, 160))
for p, n in [(A, 'A'), (C, 'C'), (J, 'J')]:
    z.point(p, 'metal', size=9)
    if n != 'A':
        z.point_label(p, n, away=co)
for p, n in [(D, 'D'), (E, 'E'), (F, 'F'), (G, 'G'), (I, 'I')]:
    z.point(p, 'concrete')
    if n != 'E':
        z.point_label(p, n, away=co)
z.free_text(A, 'A', fs=15, weight='bold', offsets=((18, -12), (22, -16), (14, -22)))    # AとEは1.22mしか離れていないので、右下と左下に分ける
z.free_text(E, 'E', fs=15, weight='bold', offsets=((-14, -8), (-16, -14), (-18, 0)))
z.point_label(H, 'H', away=co)
for p, n in [(T1, 'T1'), (T2, 'T2')]:
    z.point(p, 'kijun')
    z.point_label(p, n, away=co)
z.edge_label(D, C, '１８３－１', co, fs=15, dists=(45, 55), rotate=False)
z.edge_label(G, C, '１９６', co, fs=15, dists=(40, 50), rotate=False)
z.free_text(F + (E - F) * 0.62, '１８５－３', fs=15, offsets=((-92, 0), (-100, 12), (-100, -12), (-110, 0)))
z.edge_label(E, D, '道路　１８４－２', co, fs=15, dists=(40, 50), rotate=False, ts=(0.4, 0.3))
z.free_text(D, '１８３－２', fs=15, offsets=((50, 22), (60, 30), (60, 10), (70, 45), (80, 55), (90, 20)))
z.free_text(E, '１８５－６', fs=15, offsets=((-70, 30), (-80, 40), (-80, 20)))
z.free_text(c3 + P(-fh_m / 2 + 2.5, -fw_m / 2 + 1.0), '（単位：ｍ）\n● 金属標：A・C・J\n◎ コンクリート杭：D・E・F・G・I\n△ 基準点：T1・T2',
            fs=13, ha='left', va='bottom', offsets=((0, 0), (0, 30), (0, -30)))
ALL_PROBLEMS += save(fig, [z], 'R4_dai21mon_zu30_chiseki_sokuryouzu.png')

# =====================================================================
# zu31：問5 本人確認情報
# =====================================================================
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('問5　本人確認情報に明らかにする事項（不動産登記規則第72条第1項）', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.12, 0.94, 0.78])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')


def box(x, y, w, h, text, ec=BLACK, fc='white', fs=17, color=BLACK, weight='normal'):
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.6', ec=ec, fc=fc, lw=2))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs, color=color, weight=weight)


box(20, 80, 60, 13, '第1号（必ず書く）\n面談した（①日時）、（②場所）及び（③その状況）', ec=RED, fc='#fdecea', fs=19, weight='bold')
ax.annotate('', xy=(30, 63), xytext=(45, 78), arrowprops=dict(arrowstyle='-|>', lw=2, color=GRAY))
ax.annotate('', xy=(70, 63), xytext=(55, 78), arrowprops=dict(arrowstyle='-|>', lw=2, color=GRAY))
ax.text(25, 71, '面識がある', ha='center', fontsize=17, color=GRAY)
ax.text(75, 71, '面識がない（本問）', ha='center', fontsize=17, color=RED, weight='bold')
box(4, 38, 40, 22, '第2号\n氏名を知り、かつ、面識がある旨\n及びその面識が生じた経緯', ec=GRAY, fs=17, color=GRAY)
box(52, 30, 44, 30, '第3号\n（④申請の権限）を有する（⑤登記名義人）\nであることを確認するために\n提示を受けた書類の内容\n及び（④申請の権限）を有する（⑤登記名義人）\nであると認めた理由', ec=RED, fc='#fdecea',
    fs=16)
box(52, 8, 44, 13, '本問：良夫から運転免許証の提示を受けた\n（第72条第2項第1号の書類）', ec=GRAY, fs=15, color=GRAY)
box(4, 8, 40, 20, '答え\n① 日時　② 場所　③ その状況（①〜③順不同）\n④ 申請の権限　⑤ 登記名義人', ec=BLUE, fc='#eaf1fb', fs=17,
    color=BLUE, weight='bold')
fig.text(0.5, 0.04, '合筆の登記には登記識別情報の提供が必要（不動産登記令第8条第1項第1号）。失念したときは、資格者代理人の本人確認情報を\n'
         '登記官が相当と認めれば、事前通知をしないで登記される（不動産登記法第23条第4項第1号）。', ha='center', va='bottom', fontsize=15)
path = os.path.join(OUT, 'R4_dai21mon_zu31_honnin_kakunin.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] R4_dai21mon_zu31_honnin_kakunin.png: 図式（固定配置）\n  →', path)

# =====================================================================
# zu32：本番で解く順番（座標を使わない整理図）
# =====================================================================
from matplotlib.patches import FancyBboxPatch  # noqa: E402
fig = plt.figure(figsize=(16, 12), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('本番で解く順番　座標がなくても書ける欄を先に', fontsize=24, weight='bold', y=0.965)
ax = fig.add_axes([0.03, 0.10, 0.94, 0.82])
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
STEPS = [
    ('① 問2・問5（計算なし）', '条文の穴埋め。問2 ア 表題登記・イ 隣接・ウ 位置・エ 範囲、問5 ① 日時〜⑤ 登記名義人', '#eef4fb', BLUE),
    ('② 読解　申請書の大部分', '10月5日に中央部分だけ雑種地、問題文の注7の地番 → 登記の目的・添付書類・申請人・登録免許税・所在、\n'
     '各行の地番・地目・登記原因（座標を1つも出さずに書ける）', '#eef4fb', BLUE),
    ('③ 計算　P点・J点・I点 → 面積・辺長（いちばん時間を食う）', 'P点は放射1回、J点・I点は比例だけ。重いのは（ロ）の5点の面積、11本の辺長、\n'
     '筆界の裏付け（本件土地の面積と合成図の33.19・33.41）', '#fdf1e4', ORANGE),
    ('④ 作図　地積測量図', 'F点の折れを描き、B点は描かない。T1・T2まで入れて縦約11cm・横約13cm', '#fdf1e4', ORANGE),
]
for i, (head, body, fc, ec) in enumerate(STEPS):
    y = 85 - i * 21
    ax.add_patch(FancyBboxPatch((6, y - 7.5), 88, 15, boxstyle='round,pad=0.6', ec=ec, fc=fc, lw=2))
    ax.text(9, y + 3.6, head, ha='left', va='center', fontsize=19, weight='bold', color=BLACK)
    ax.text(9, y - 2.6, body, ha='left', va='center', fontsize=15, color=BLACK, linespacing=1.5)
    if i < len(STEPS) - 1:
        ax.annotate('', xy=(50, y - 12.6), xytext=(50, y - 8.6), arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=2))
fig.text(0.5, 0.05, '青：座標がなくても書ける　／　橙：座標が要る（申請書の地積の3つと、地積測量図の辺長だけ）。\n'
         '計算で詰まっても、問2・問5と申請書の大部分の点は先に取っておける',
         ha='center', va='center', fontsize=16)
path = os.path.join(OUT, 'R4_dai21mon_zu32_kaku_junban.png')
fig.savefig(path, dpi=100, facecolor='white')
print('[重なり検査] R4_dai21mon_zu32_kaku_junban.png: 整理図（固定配置）\n  →', path)

print('重なりの合計:', len(ALL_PROBLEMS))
