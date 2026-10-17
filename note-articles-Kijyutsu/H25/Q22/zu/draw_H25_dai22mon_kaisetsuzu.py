"""平成25年度 第22問（建物）の解説図20枚を、座標成果・各階平面見取図の寸法から作図してPNGに書き出す。

`../prompt_H25_dai22mon_kaisetsuzu.md` の図1〜図20どおり（番号は記事の挿入順）。作図の共通部品は `tools/zu_helpers.py`。
2026-10-05、本文で説明しているのに図がなかった7か所の図（注の仕分け、解体移転とえい行移転、主である建物の滅失と附属建物、
建物の位置の計算、鉄骨柱の測り方、12番の分筆と所在の変更、形成的登記と報告的登記）を加えた。
2026-10-16、最新の執筆ルールでの照らし直しで、所在の順序の誤り比較図（図8）、第1欄・第2欄の添付情報の当てはめ表（図17・図18）を加え、
番号を記事の挿入順に振り直した（旧図8→図9、旧図9→図10、旧図10→図11、旧図11→図12、旧図12→図13、旧図13→図14、旧図14→図15、
旧図15→図16、旧図16→図19、旧図17→図20。描き直していない図は中身を変えていない）。あわせて、図9（建物図面）と図14（各階平面図）の
完成形を、試験の答案用紙の第4欄の枠の寸法（mm）どおりの1枚の枠の中に、建物図面は縮尺1/500・各階平面図は縮尺1/250の実際の大きさで
描き直した（各階平面図には方位を描かない。不動産登記規則第83条第1項）。画像の中に図の番号は書かない。
固定配置の図は check_fixed で文字の重なりとはみ出しを調べる。
第4欄の形は試験の答案用紙の原本（`../touan_youshi/H25_dai22mon_touan_youshi.pdf` の2ページ目。`public/kijutsu/H25-tatemono/a2.webp`
と同じもの）で確かめた：1枚の枠の左半分が各階平面図、右半分が建物図面。家屋番号・建物の所在は建物図面の側に1組、
建物図面の側の下は「申請人」（（略）の印刷なし）と縮尺1/500、各階平面図の側の下は「作成者（略）（平成何年何月何日作成）」と縮尺1/250。
敷地は〔筆界点の座標成果〕の (X＝北, Y＝東)。建物の平面は (東, 南)（原点＝建物の1階の北西の角の壁の中心線）で持ち、
zu_helpers の (北, 東) には P()（求積図）・B_()（敷地の上に置く）で変換する。
実行: python3 note-articles-Kijyutsu/H25/Q22/zu/draw_H25_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle, FancyBboxPatch  # noqa: E402
from matplotlib.colors import to_rgba  # noqa: E402

from zu_helpers import Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN, PURPLE  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []
INK = '#1a3a8f'   # 答案用紙への記入（濃い青）

# ---- 敷地（〔筆界点の座標成果〕。複素数 X＋Yi） ----
A, B, C, D = complex(39.24, 73.39), complex(39.24, 93.96), complex(21.64, 94.91), complex(27.15, 74.86)
E, F, G, H = complex(17.07, 95.16), complex(17.07, 76.09), complex(39.24, 66.57), complex(17.07, 66.57)
LOT11 = [A, B, C, D]
LOT10 = [D, C, E, F]
LOT12_1 = [G, A, D, F, H]
OUTER = [A, B, C, E, F, D]

# ---- 本件新建物の位置（別紙1の（注）4：距離は外壁まで、（注）5：柱の中心＝壁の中心線、（注）6：壁厚20cm → 0.10ずらす） ----
HALF = 0.10
N_EXT = round(39.24 - 2.60, 2)            # 北の外壁 36.64
N0 = round(N_EXT - HALF, 2)               # 北の壁の中心線 36.54
S0 = round(N0 - 10.92, 2)                 # 1階の西側の南の壁の中心線 25.62
S_EXT = round(S0 - HALF, 2)               # 南の外壁 25.52
Y_DF = 74.86 + (27.15 - S_EXT) * (76.09 - 74.86) / (27.15 - 17.07)   # 南西の角の高さでのD-F線 75.0589…
W_EXT = Y_DF + 2.56                       # 西の外壁 77.6189…
W0 = round(W_EXT + HALF, 2)               # 西の壁の中心線 77.72
assert (N_EXT, N0, S0, S_EXT, W0) == (36.64, 36.54, 25.62, 25.52, 77.72) and round(Y_DF, 2) == 75.06


def P(e, s):
    """求積図用：建物の北西の角を原点にした (東, 南) を (北 + 東i) にする。"""
    return complex(-s, e)


def B_(e, s):
    """敷地の上に置く：(東, 南) を敷地の座標 (北 + 東i) にする。"""
    return complex(N0 - s, W0 + e)


def rect(e0, s0, e1, s1, f=P):
    return [f(e0, s0), f(e1, s0), f(e1, s1), f(e0, s1)]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


# ---- 1階・2階・附属建物の形（壁の中心線。(東, 南)） ----
F1 = [(0, 0), (8.19, 0), (8.19, 0.91), (10.92, 0.91), (10.92, 0), (14.56, 0), (14.56, 9.1), (10.01, 9.1),
      (10.01, 10.92), (0, 10.92)]
F2 = [(3.64, 0), (14.56, 0), (14.56, 10.92), (3.64, 10.92)]
F2_NG = [(0, 0), (10.92, 0), (10.92, 10.92), (0, 10.92)]
AN0 = [(0, 0), (4.5, 0), (4.5, 5), (0, 5)]
AN1 = [(0, 0), (4.5, 0), (4.5, 8.5), (0, 8.5)]
assert round(area([P(*v) for v in F1]), 4) == 148.2299
assert round(area([P(*v) for v in F2]), 4) == round(area([P(*v) for v in F2_NG]), 4) == 119.2464
assert round(area([P(*v) for v in AN0]), 2) == 22.50 and round(area([P(*v) for v in AN1]), 2) == 38.25
assert round(area(LOT11), 4) == 298.1684 and round(area(LOT10), 4) == 141.2383


def dc_x(y):
    """D-Cの線の、Y（東）での X（北）。"""
    return D.real + (y - D.imag) * (C.real - D.real) / (C.imag - D.imag)


def dc_y(x):
    return D.imag + (x - D.real) * (C.imag - D.imag) / (C.real - D.real)


TRI10 = [complex(dc_x(W0), W0), complex(S0, W0), complex(S0, dc_y(S0))]   # 1階のうち10番に入る三角形
assert round(dc_x(W0), 2) == 26.36 and round(dc_y(S0), 2) == 80.43 and round(area(TRI10), 1) == 1.0


def hatch(ax, pts, color=GRAY, pattern='///'):
    ax.add_patch(MPoly([xy(p) for p in pts], closed=True, fill=False, hatch=pattern, edgecolor=color, lw=0, zorder=1))


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def dims(z, pts, labels, fs=14, ref=None, outward=True):
    c = ref if ref is not None else centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs, outward=outward)


OFFS = ((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0), (24, 12), (-24, -12))


# ---- 図1：時系列と、3つの建物の行き先 ----
def zu01():
    """固定配置の図。check_fixed で文字の重なりとはみ出しを調べ、目視でも確認する。"""
    setup_font()
    fig = plt.figure(figsize=(16, 10.5), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('3つの建物に、3種類の登記　日付を並べてから行き先を決める', fontsize=24, weight='bold', y=0.975)
    ax = fig.add_axes([0.02, 0.06, 0.96, 0.84])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    # 時間軸
    ax.annotate('', xy=(98, 86), xytext=(2, 86), arrowprops=dict(arrowstyle='-|>', lw=2.2, color=BLACK, mutation_scale=20))
    events = [(8, '7月26日', '主である建物・\n本件取壊建物の\n解体完了', BLACK),
              (28, '8月5日', '12番を12番1・\n12番2に分筆', BLACK),
              (48, '8月18日', '附属建物の\n増改築完了\n（美容院）', BLACK),
              (68, '8月22日', '本件新建物の\n再築完了', BLACK),
              (88, '8月23日', '申請', BLUE)]
    ax.text(2, 96, '平成25年', fontsize=16, weight='bold')
    for x, d, t, col in events:
        ax.plot(x, 86, 'o', ms=12, color=col, zorder=5)
        ax.text(x, 90, d, ha='center', va='bottom', fontsize=17, weight='bold', color=col)
        ax.text(x, 82, t, ha='center', va='top', fontsize=14, color=col, linespacing=1.3)
    # 3列の箱
    cols = [
        (17, ['本件旧建物の\n主である建物（倉庫）', '解体して隣地へ\n（解体移転＝滅失と新築。\n準則第85条第1項）',
              '本件新建物：\n建物表題登記（問2）'], GREEN,
         'えい行移転なら所在の変更\n（準則第85条第2項）', GRAY),
        (50, ['本件旧建物の\n附属建物（物置）', '主である建物に変更、\n増改築で店舗に',
              '本件旧建物：\n建物表題部変更登記（問1）'], BLUE,
         '主である建物がなくても附属建物が\n残る＝滅失登記ではない（準則第102条）', RED),
        (83, ['本件取壊建物\n（店舗）', '取壊し',
              '建物滅失登記（問3。\n報告的登記・保存行為）'], ORANGE, '', GRAY),
    ]
    w, hbox = 28, 11
    ys = [56, 37, 18]
    for cx, boxes, col, note, ncol in cols:
        for k, (y, t) in enumerate(zip(ys, boxes)):
            last = k == len(boxes) - 1
            ax.add_patch(FancyBboxPatch((cx - w / 2, y - hbox / 2), w, hbox, boxstyle='round,pad=0.6',
                                        facecolor=col, alpha=0.30 if last else 0.12, edgecolor=col, lw=2.4 if last else 1.6))
            ax.text(cx, y, t, ha='center', va='center', fontsize=15, weight='bold' if last else 'normal', linespacing=1.3)
            if not last:
                ax.annotate('', xy=(cx, ys[k + 1] + hbox / 2 + 1.2), xytext=(cx, y - hbox / 2 - 1.2),
                            arrowprops=dict(arrowstyle='-|>', lw=1.8, color=col, mutation_scale=18))
        if note:
            ax.text(cx, 4.5, note, ha='center', va='center', fontsize=13, color=ncol, linespacing=1.3)
    check_fixed(fig, 'H25_dai22mon_zu01_jikeiretsu')
    path = os.path.join(OUT, 'H25_dai22mon_zu01_jikeiretsu.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


# ---- 図5：敷地の辺長確認図（作図チェック用） ----
def zu05():
    fig, axes = new_figure('敷地（11番・10番）の辺長確認図（作図チェック用）',
                           '作図チェック用（建物図面には辺長を書かない）。斜めの辺はF-789SGの複素数モードの[Abs]で検算',
                           w=16, h=12.5)
    ax = axes[0]
    z = Zu(ax, fontsize=16)
    fit(ax, OUTER + [G, H], margin=0.10, extra=[xy(complex(41.5, 98.5)), xy(complex(15.0, 64.5))], pad_aspect=True)
    z.north_arrow()
    z.poly(LOT12_1, color=GRAY, lw=1.4, fill=GRAY, alpha=0.08)
    z.poly(LOT11, color=BLACK, lw=2.6, fill=BLUE, alpha=0.12)
    z.poly(LOT10, color=BLACK, lw=2.6, fill=ORANGE, alpha=0.14)
    pts = dict(A=A, B=B, C=C, D=D, E=E, F=F, G=G, H=H)
    for p in pts.values():
        z.point(p)
    c_all = centroid(OUTER)
    for n, p in pts.items():
        away = centroid(LOT12_1) if n in 'GH' else c_all
        z.point_label(p, n, away=away, fs=19)
    c11, c10 = centroid(LOT11), centroid(LOT10)
    z.edge_label(A, B, '20.57', c11, fs=16)
    z.edge_label(B, C, '17.63', c11, fs=16)
    z.edge_label(C, D, '20.79', c11, fs=16, outward=False)
    z.edge_label(D, A, '12.18', c11, fs=16, outward=False)
    z.edge_label(C, E, '4.58', c10, fs=16)
    z.edge_label(E, F, '19.07', c10, fs=16)
    z.edge_label(F, D, '10.15', c10, fs=16, outward=False)
    z.free_text(c11, '11', fs=22, offsets=OFFS, weight='bold')
    z.free_text(c10, '10', fs=22, offsets=OFFS, weight='bold')
    z.free_text(centroid(LOT12_1), '12-1', fs=18, offsets=OFFS, color=GRAY)
    for p, t in [(complex(40.6, 84.0), '道路（51）'), (complex(30.0, 97.3), '9-1'), (complex(15.9, 86.0), '16-1'),
                 (complex(15.9, 71.0), '15-1')]:
        z.free_text(p, t, fs=16, offsets=OFFS)
    save(fig, [z], 'H25_dai22mon_zu05_shikichi_henchou')


# ---- 図7：所在の誤り比較図（左：概略図の見た目、中：座標で描いた実際、右：南西の角の拡大） ----
ZOOM = [complex(24.6, 73.6), complex(24.6, 82.6), complex(28.0, 82.6), complex(28.0, 73.6)]


def zu07():
    fig, axes = new_figure('所在の誤り比較：概略図の見た目と、座標で描いた実際',
                           '概略図は簡易な図（別紙1の（注）1）でD-Cの線がない。座標で引くと南西の角の約1.0㎡が10番に入る。\n'
                           '所在は床面積の多い順に「11番地、10番地」（準則第88条第2項）',
                           w=18, h=10.5, ncols=3, width_ratios=[1, 1, 1.15])
    fig.subplots_adjust(top=0.86, bottom=0.16, wspace=0.08)
    bldg = [B_(*v) for v in F1]
    zs = []
    ext = [xy(complex(40.5, 71.5)), xy(complex(16.0, 97.0))]
    # 左：概略図の見た目
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    fit(ax, OUTER, margin=0.05, extra=ext, pad_aspect=True)
    z.poly(OUTER, color=BLACK, lw=2.4)
    z.poly(bldg, color=RED, lw=2.0, fill=RED, alpha=0.18)
    z.free_text(centroid(bldg), '11番地だけ？', fs=18, color=RED, offsets=OFFS, weight='bold')
    z.free_text(complex(31.0, 75.9), '11', fs=17, offsets=OFFS)
    z.free_text(complex(19.5, 86.0), '10', fs=17, offsets=OFFS)
    ax.set_title('誤り：概略図の見た目\n（D-Cの線がない）', fontsize=17, weight='bold', color=RED, pad=10)
    zs.append(z)
    # 中：座標で描いた実際
    ax = axes[1]
    z = Zu(ax, fontsize=15)
    fit(ax, OUTER, margin=0.05, extra=ext, pad_aspect=True)
    z.north_arrow()
    z.poly(OUTER, color=BLACK, lw=2.4)
    z.poly(bldg, color=GREEN, lw=2.0, fill=GREEN, alpha=0.20)
    z.poly(TRI10, color=RED, lw=0, fill=RED, alpha=0.85, check=False)
    z.line(D, C, color=BLACK, lw=2.8)
    z.poly(ZOOM + [ZOOM[0]], color=RED, lw=1.4, ls='--', closed=False)
    z.point(D)
    z.point(C)
    z.point_label(D, 'D', away=complex(27.15, 80.0), fs=16)
    z.point_label(C, 'C', away=complex(21.64, 88.0), fs=16)
    z.free_text(complex(31.5, 86.5), '約147.2㎡\nが11番', fs=15, color=GREEN, offsets=OFFS, weight='bold')
    z.callout(complex(24.6, 80.0), '右に拡大', dirs=(-60, -75, -45), dists=(40, 55, 70), fs=14, color=RED)
    z.free_text(complex(31.0, 75.9), '11', fs=17, offsets=OFFS)
    z.free_text(complex(19.5, 86.0), '10', fs=17, offsets=OFFS)
    ax.set_title('正しい：座標で描いた実際\n（D-Cの線を引く）', fontsize=17, weight='bold', color=GREEN, pad=10)
    zs.append(z)
    # 右：南西の角の拡大
    ax = axes[2]
    z = Zu(ax, fontsize=15)
    fit(ax, ZOOM, margin=0.04, pad_aspect=True)
    z.line(complex(28.0, D.imag - (28.0 - D.real) * (74.86 - 73.39) / (39.24 - 27.15)), D, color=BLACK, lw=2.2)
    z.line(D, complex(24.6, 74.86 + (27.15 - 24.6) * 1.23 / 10.08), color=BLACK, lw=2.2)
    z.line(D, complex(dc_x(82.6), 82.6), color=BLACK, lw=2.8)
    z.line(complex(28.0, W0), complex(S0, W0), color=GREEN, lw=2.4)
    z.line(complex(S0, W0), complex(S0, 82.6), color=GREEN, lw=2.4)
    z.poly(TRI10, color=RED, lw=0, fill=RED, alpha=0.85, check=False)
    z.point(D)
    z.point_label(D, 'D', away=complex(27.15, 79.0), fs=17)
    # D点の高さと南の壁の中心線の差 1.53
    yd = 76.3
    z.line(complex(D.real, D.imag), complex(D.real, yd + 0.5), color=GRAY, lw=1.1, ls='--')
    z.line(complex(S0, yd - 0.3), complex(S0, W0), color=GRAY, lw=1.1, ls='--')
    z.dim_line(complex(S0, yd), complex(D.real, yd))
    z.free_text(complex((S0 + D.real) / 2, yd), '1.53', fs=15, offsets=((-22, 0), (-26, 8), (22, 0)))
    z.callout(complex(25.85, 78.4), '約1.0㎡が10番\n（東西約2.71×南北約0.74÷2）', dirs=(-60, -40, -80), dists=(45, 65, 85), fs=14,
              color=RED)
    z.free_text(complex(27.3, 80.6), '建物（1階）', fs=15, color=GREEN, offsets=OFFS, weight='bold')
    z.free_text(complex(27.1, 77.0), '11', fs=17, offsets=OFFS)
    z.free_text(complex(25.0, 81.8), '10', fs=17, offsets=OFFS)
    z.free_text(complex(25.6, 74.25), '12-1', fs=14, color=GRAY, offsets=OFFS)
    ax.set_title('南西の角の拡大\n（南の壁の中心線はD点より1.53南）', fontsize=17, weight='bold', pad=10)
    zs.append(z)
    for x in (0.355, 0.665):
        fig.add_artist(plt.Line2D([x, x], [0.17, 0.86], transform=fig.transFigure, color=GRAY, lw=1.0))
    save(fig, zs, 'H25_dai22mon_zu07_shozai_ayamari_hikaku')


# ---- 答案用紙の第4欄（建物図面及び各階平面図）。2026-10-16、試験の答案用紙の寸法どおりに描き直した ----
# 寸法は試験の答案用紙の原本（`../touan_youshi/H25_dai22mon_touan_youshi_p2.png`、A3横 420mm × 297mm を 2481px × 1754px で
# 画像にしたもの。1mm ＝ 5.907px）の罫線の位置から mm に直した値。作図は用紙の左下を原点とする mm の座標で行い、図面の中身は
# 建物図面が縮尺1/500（1m ＝ 2mm）、各階平面図が縮尺1/250（1m ＝ 4mm）の実際の大きさで描く。
# 第4欄は1枚の枠の左半分が各階平面図、右半分が建物図面（中央の上下に短い仕切りの線だけが印刷）。枠の上の「家屋番号」の箱と、
# 枠の中の上端の「建物の所在」の欄は、建物図面の側に1組だけ。下に「作成者（略）（平成何年何月何日作成）」「縮尺 1/250」と
# 「申請人」（（略）の印刷なし）「縮尺 1/500」。縮尺は分数の形で印刷。「（単位：m）」は枠の中の右下。
FR_L, FR_R, FR_B, FR_T = 46.4, 359.2, 45.6, 259.4     # 図を描く枠
MID = 202.8                                          # 中央の仕切り
SH_X0, SH_X1, SH_Y0, SH_Y1 = 38.0, 367.0, 14.0, 282.0  # 画像に入れる範囲（mm）
SHEET_MM = dict(frame=(FR_L, FR_R, FR_B, FR_T), mid=MID, kaoku=(210.8, 276.1, FR_T, 270.4), kaoku_div=236.0,
                shozai=(210.8, FR_R, 248.2, FR_T), sakusei=(FR_L, 195.5, 31.0, FR_B), sakusei_div=(69.4, 157.4, 158.0, 172.7),
                shinsei=(211.8, FR_R, 30.3, FR_B), shinsei_div=(241.1, 321.8, 322.5, 337.2))


def M(x, y):
    """用紙の mm の位置（x：右向き、y：上向き）を zu_helpers の複素数（北＝縦、東＝横）にする。"""
    return complex(y, x)


ZUMEN_X0, ZUMEN_Y0, ZUMEN_E0, ZUMEN_N0 = 281.0, 150.0, 84.3, 28.2


def S500(p):
    """建物図面（縮尺1/500）：敷地の座標 X＋Yi [m] を用紙の mm に置く。1m ＝ 2mm。"""
    return M(ZUMEN_X0 + 2 * (p.imag - ZUMEN_E0), ZUMEN_Y0 + 2 * (p.real - ZUMEN_N0))


def S250(e, s, x0, y0):
    """各階平面図（縮尺1/250）：建物の (東, 南) [m] を用紙の mm に置く。原点（1階の北西の角）を (x0, y0) mm に。1m ＝ 4mm。"""
    return M(x0 + 4 * e, y0 - 4 * s)


def sheet_figure(title):
    setup_font()
    w_mm, h_mm = SH_X1 - SH_X0, SH_Y1 - SH_Y0
    fig = plt.figure(figsize=(22, 22 * h_mm / w_mm), dpi=100)
    fig.patch.set_facecolor('white')
    ax = fig.add_axes([0, 0, 1, 1])
    z = Zu(ax, fontsize=10)
    ax.set_xlim(SH_X0, SH_X1)
    ax.set_ylim(SH_Y0, SH_Y1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.text((SH_X0 + SH_X1) / 2, 277.5, title, ha='center', va='center', fontsize=21, weight='bold')
    return fig, ax, z


def sheet4(ax):
    """第4欄の印刷（試験の答案用紙どおり）と、建物の所在・申請人の記入。"""
    def rect(x0, x1, y0, y1, lw=1.3):
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, lw=lw, ec=BLACK, zorder=3))

    def ln(x0, y0, x1, y1, lw=1.0):
        ax.plot([x0, x1], [y0, y1], color=BLACK, lw=lw, zorder=3)

    def txt(x, y, s, fs=12, ha='center', **kw):
        ax.text(x, y, s, ha=ha, va='center', fontsize=fs, zorder=4, family='Noto Serif CJK JP', **kw)

    S = SHEET_MM
    ax.text(FR_L + 1.0, 265.5, '第4欄　建物図面及び各階平面図', ha='left', va='center', fontsize=13, weight='bold', zorder=4)
    rect(FR_L, FR_R, FR_B, FR_T, lw=1.6)                         # 図を描く枠
    ln(MID, FR_T, MID, 249.6, lw=1.6)                            # 中央の仕切り（上下の短い線だけが印刷）
    ln(MID, FR_B, MID, 55.5, lw=1.6)
    rect(*S['kaoku'])                                            # 家屋番号の箱（枠の外の上）
    ln(S['kaoku_div'], FR_T, S['kaoku_div'], 270.4)
    txt(223.4, 264.9, '家 屋 番 号', fs=11)
    txt(311.5, 270.7, '建　　物　　図　　面', fs=14)
    txt(311.5, 263.4, '各　階　平　面　図', fs=14)
    rect(*S['shozai'])                                           # 建物の所在の欄（枠の中の上端）
    ln(S['kaoku_div'], 248.2, S['kaoku_div'], FR_T)
    txt(223.4, 253.8, '建物の所在', fs=11)
    ax.text(240.0, 253.8, 'C市D町一丁目11番地、10番地', ha='left', va='center', fontsize=12, color=INK, zorder=4)
    x0, x1, y0, y1 = S['sakusei']                                # 作成者・縮尺 1/250
    rect(x0, x1, y0, y1)
    for x in S['sakusei_div']:
        ln(x, y0, x, y1)
    txt(57.7, 38.3, '作　成　者', fs=11)
    txt(84.6, 41.6, '（略）', fs=11)
    txt(156.2, 34.4, '（平成何年何月何日作成）', fs=10, ha='right')
    txt(165.0, 38.3, '縮尺', fs=10)
    ln(175.0, 32.3, 194.0, 44.3, lw=0.9)
    txt(180.5, 42.3, '1', fs=10)
    txt(189.0, 34.0, '250', fs=10)
    x0, x1, y0, y1 = S['shinsei']                                # 申請人・縮尺 1/500
    rect(x0, x1, y0, y1)
    for x in S['shinsei_div']:
        ln(x, y0, x, y1)
    txt(226.4, 38.0, '申　請　人', fs=11)
    ax.text(246.0, 38.0, '甲野春男　甲野冬子', ha='left', va='center', fontsize=12, color=INK, zorder=4)
    txt(329.6, 38.0, '縮尺', fs=10)
    ln(339.0, 31.8, 358.0, 43.8, lw=0.9)
    txt(344.0, 42.0, '1', fs=10)
    txt(353.0, 33.6, '500', fs=10)
    txt(339.0, 50.8, '（単位：m）', fs=10)


def zumen_content(z):
    """右半分：建物図面（縮尺1/500、1m ＝ 2mm）。敷地（11番・10番）と1階の位置・形状、筆界から外壁までの距離、地番・道路・方位。"""
    for a, b in [(complex(39.24, 69.5), A), (B, complex(39.24, 97.6)), (complex(17.07, 72.5), F), (E, complex(17.07, 97.6))]:
        z.line(S500(a), S500(b), lw=1.0)
    z.poly([S500(p) for p in LOT11], lw=1.4)
    z.poly([S500(p) for p in LOT10], lw=1.4)
    bldg = [S500(B_(*v)) for v in F1]
    z.poly(bldg, lw=2.0)
    z.north_arrow(pos=(0.86, 0.62), length=0.05)
    w_ext, e_ext = W0 - HALF, W0 + 14.56 + HALF
    for p, q, dirs in [(complex(N_EXT, w_ext), complex(39.24, w_ext), (200, 215, 185)),
                       (complex(N_EXT, e_ext), complex(39.24, e_ext), (-20, -35, -5)),
                       (complex(S_EXT, w_ext), complex(S_EXT, Y_DF), (-120, -135, -105))]:
        z.dim_line(S500(p), S500(q), lw=1.1)
        z.callout(S500((p + q) / 2), {True: '2.60'}.get(abs(p.imag - q.imag) < 1e-9, '2.56'), dirs=dirs, fs=10,
                  dists=(30, 40, 52, 64))
    z.free_text(S500(complex(37.9, 85.0)), '11', fs=10, offsets=((0, 0), (8, 0), (-8, 0), (16, 0)))
    z.free_text(S500(centroid(LOT10)), '10', fs=11)
    for p, t in [(complex(41.4, 84.0), '道路（51）'), (complex(30.0, 98.6), '9-1'), (complex(15.3, 86.0), '16-1'),
                 (complex(15.3, 73.8), '15-1'), (complex(30.0, 70.6), '12-1')]:
        z.free_text(S500(p), t, fs=10)


def heimen_content(z):
    """左半分：各階平面図（縮尺1/250、1m ＝ 4mm）。壁の中心線の辺長（小数第2位）、各階の別、2階には1階の位置を点線で。方位は書かない。"""
    x0, y1, y2 = 66.0, 232.0, 160.0
    z.free_text(M(58.0, 240.5), '1階', fs=12, ha='left')
    f1 = [S250(e, s, x0, y1) for e, s in F1]
    z.poly(f1, lw=1.6)
    c1 = S250(7.0, 5.5, x0, y1)
    for i, t in enumerate(['8.19', None, '2.73', None, '3.64', '9.10', '4.55', None, '10.01', '10.92']):
        if t:
            z.edge_label(f1[i], f1[(i + 1) % len(f1)], t, c1, fs=10, dists=(7, 11, 15))
    z.callout(S250(8.19, 0.455, x0, y1), '0.91', dirs=(-150, -165, -135), fs=9, dists=(24, 32, 42))
    z.callout(S250(10.92, 0.455, x0, y1), '0.91', dirs=(-30, -15, -45), fs=9, dists=(24, 32, 42))
    z.callout(S250(10.01, 10.01, x0, y1), '1.82', dirs=(-20, -35, -5), fs=9, dists=(24, 32, 42))
    z.free_text(M(136.0, 211.0), '1階\n8.19×10.92＝89.4348\n1.82×10.01＝18.2182\n0.91×8.19＝7.4529\n3.64×9.10＝33.1240\n'
                '計　148.2299\n床面積　148.22㎡', fs=11, ha='left', linespacing=1.6)
    z.free_text(M(58.0, 168.5), '2階', fs=12, ha='left')
    for a, b in [((3.64, 0), (0, 0)), ((0, 0), (0, 10.92)), ((0, 10.92), (3.64, 10.92)),
                 ((8.19, 0), (8.19, 0.91)), ((8.19, 0.91), (10.92, 0.91)), ((10.92, 0.91), (10.92, 0)),
                 ((14.56, 9.1), (10.01, 9.1)), ((10.01, 9.1), (10.01, 10.92))]:
        z.line(S250(*a, x0, y2), S250(*b, x0, y2), lw=1.0, ls=':')
    f2 = [S250(e, s, x0, y2) for e, s in F2]
    z.poly(f2, lw=1.6)
    c2 = S250(9.1, 5.46, x0, y2)
    for i, t in enumerate(['10.92', '10.92', '10.92', '10.92']):
        z.edge_label(f2[i], f2[(i + 1) % 4], t, c2, fs=10, dists=(7, 11, 15))
    z.free_text(M(136.0, 141.0), '2階\n10.92×10.92＝119.2464\n計　119.2464\n床面積　119.24㎡', fs=11, ha='left', linespacing=1.6)
    z.free_text(M(66.0, 106.0), '点線は1階の位置', fs=10, ha='left', color=GRAY)


# ---- 図9：建物図面の完成形（答案用紙の第4欄の建物図面の側。用紙の大きさと縮尺1/500の実際の大きさ） ----
def zu09():
    fig, ax, z = sheet_figure('建物図面の完成形（答案用紙の第4欄の建物図面の側・縮尺1/500の実際の大きさ）')
    sheet4(ax)
    zumen_content(z)
    assert round(area([B_(*v) for v in F1]), 4) == 148.2299
    ax.text((SH_X0 + SH_X1) / 2, 22.0, '距離は外壁まで（別紙1の（注）4）：北西・北東の角から北の道路（51）との境まで2.60、南西の角から西の12番1との境まで2.56。'
            'D-Cの線は建物の南西の角を切る', ha='center', va='center', fontsize=13)
    ax.text((SH_X0 + SH_X1) / 2, 16.5, '家屋番号は登記官が付けるので空欄。各階平面図の側（左半分）は床面積を求めてから描く（第3章）。敷地の辺長は書かない',
            ha='center', va='center', fontsize=12, color=GRAY)
    save(fig, [z], 'H25_dai22mon_zu09_tatemono_zumen')


# ---- 図11：1階の求積図 ----
def zu11():
    fig, axes = new_figure('本件新建物1階の求積図（壁の中心線）',
                           '1階 床面積：148.22㎡（8.19×10.92＋1.82×10.01＋0.91×8.19＋3.64×9.10＝148.2299）',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    f1 = [P(*v) for v in F1]
    fit(ax, f1, margin=0.16, extra=[xy(P(18.5, 12.0))], pad_aspect=True)
    z.north_arrow()
    parts = [((0, 0, 8.19, 10.92), BLUE, '8.19×10.92'), ((8.19, 0.91, 10.01, 10.92), ORANGE, '1.82×10.01'),
             ((10.01, 0.91, 10.92, 9.1), PURPLE, '0.91×8.19'), ((10.92, 0, 14.56, 9.1), GREEN, '3.64×9.10')]
    for (e0, s0, e1, s1), col, _ in parts:
        z.poly(rect(e0, s0, e1, s1), color=col, lw=0, fill=col, alpha=0.30, check=False)
    for e in (8.19, 10.01, 10.92):
        s_top = 0 if e == 8.19 else 0.91
        s_bot = 10.92 if e == 8.19 else (10.92 if e == 10.01 else 9.1)
        z.line(P(e, s_top), P(e, s_bot), color=GRAY, lw=1.2, ls='--')
    z.poly(f1, color=BLACK, lw=2.6)
    c = P(7.0, 5.5)
    dims(z, f1, ['8.19', None, '2.73', None, '3.64', '9.10', '4.55', '1.82', '10.01', '10.92'], fs=15, ref=c)
    z.free_text(P(8.19, 0.455), '0.91', fs=13, offsets=((13, 0), (15, 0)), rotation=90)
    z.free_text(P(10.92, 0.455), '0.91', fs=13, offsets=((-13, 0), (-15, 0)), rotation=90)
    z.free_text(P(4.1, 5.46), '①\n8.19×10.92', fs=16, offsets=OFFS)
    z.free_text(P(9.1, 6.0), '②\n1.82\n×\n10.01', fs=14, offsets=OFFS)
    z.free_text(P(10.465, 5.0), '③ 0.91×8.19', fs=14, offsets=((0, 0), (0, 20), (0, -20)), rotation=90)
    z.free_text(P(12.74, 4.55), '④\n3.64×9.10', fs=15, offsets=OFFS)
    z.callout(P(12.3, 10.0), '南東の欠け（4.55×1.82）\nは建物の外', dirs=(-20, -35, -5), dists=(40, 60, 80), fs=14, color=GRAY)
    z.callout(P(9.55, 0.3), '北の欠け（2.73×0.91）', dirs=(70, 55, 85), dists=(55, 75, 95), fs=14, color=GRAY)
    save(fig, [z], 'H25_dai22mon_zu11_1kai_kyuuseki')


# ---- 図12：2階の誤り比較図 ----
def zu12():
    fig, axes = new_figure('2階の位置：北西の角で合わせるか、東の辺でそろえるか',
                           '床面積はどちらも119.24㎡で同じ。丸印（別紙1の（注）9）で重ねると、2階の西の端は14.56−10.92＝3.64東',
                           w=16, h=10, ncols=2)
    fig.subplots_adjust(top=0.86, wspace=0.10)
    f1 = [P(*v) for v in F1]
    zs = []
    for k, (pts, col, title, tcol) in enumerate([
            (F2_NG, RED, '誤り：北西の角で1階に合わせた', RED),
            (F2, GREEN, '正しい：東の辺で1階にそろえる', GREEN)]):
        ax = axes[k]
        z = Zu(ax, fontsize=14)
        fit(ax, f1, margin=0.22, extra=[xy(P(7.3, 14.2))], pad_aspect=True)
        z.poly(f1, color=BLACK, lw=1.6, ls=':')
        f2 = [P(*v) for v in pts]
        z.poly(f2, color=BLACK, lw=2.4, fill=col, alpha=0.25)
        ax.set_title(title, fontsize=18, weight='bold', color=tcol, pad=10)
        if k == 0:
            z.free_text(P(5.46, 5.46), '2階\n10.92×10.92', fs=16, offsets=OFFS)
            z.free_text(P(7.28, 12.6), '1階の位置が違う', fs=16, color=RED, offsets=OFFS, weight='bold')
        else:
            for e, s in [(14.56, 0), (14.56, 9.1)]:
                z.ax.plot(*xy(P(e, s)), 'o', ms=16, mfc='none', mec=BLACK, mew=2.0, zorder=6)
                z.markers.append(xy(P(e, s)))
            z.free_text(P(9.1, 5.46), '2階\n10.92×10.92', fs=16, offsets=OFFS)
            z.dim_line(P(0, 12.0), P(3.64, 12.0))
            z.line(P(0, 10.92), P(0, 12.4), color=GRAY, lw=1.0)
            z.line(P(3.64, 10.92), P(3.64, 12.4), color=GRAY, lw=1.0)
            z.free_text(P(1.82, 12.0), '3.64', fs=15, offsets=((0, -14), (0, -18)))
            z.callout(P(14.56, 9.1), '丸印（重なる部分）', dirs=(-110, -125, -95), dists=(55, 75, 95), fs=14)
            z.free_text(P(4.5, -1.6), '点線＝1階', fs=14, offsets=OFFS)
        zs.append(z)
    zs[1].north_arrow()
    fig.add_artist(plt.Line2D([0.5, 0.5], [0.13, 0.86], transform=fig.transFigure, color=GRAY, lw=1.2))
    save(fig, zs, 'H25_dai22mon_zu12_2kai_ayamari_hikaku')


# ---- 図13：2階の求積図 ----
def zu13():
    fig, axes = new_figure('本件新建物2階の求積図（1階の外形を点線で重ねる）',
                           '2階 床面積：119.24㎡（10.92×10.92＝119.2464）。北の欠け・南東の欠けの上にも2階が張り出す',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    f1 = [P(*v) for v in F1]
    fit(ax, f1, margin=0.16, extra=[xy(P(18.5, 12.0))], pad_aspect=True)
    z.north_arrow()
    f2 = [P(*v) for v in F2]
    z.poly(f2, color=BLACK, lw=0, fill=GREEN, alpha=0.22, check=False)
    # 1階の外形のうち、2階の外形と重ならない線を点線で
    for a, b in [((3.64, 0), (0, 0)), ((0, 0), (0, 10.92)), ((0, 10.92), (3.64, 10.92)),
                 ((8.19, 0), (8.19, 0.91)), ((8.19, 0.91), (10.92, 0.91)), ((10.92, 0.91), (10.92, 0)),
                 ((14.56, 9.1), (10.01, 9.1)), ((10.01, 9.1), (10.01, 10.92))]:
        z.line(P(*a), P(*b), color=BLACK, lw=1.6, ls=':')
    z.poly(f2, color=BLACK, lw=2.6)
    dims(z, f2, ['10.92', '10.92', '10.92', '10.92'], fs=15, ref=P(9.1, 5.46))
    z.free_text(P(9.1, 4.2), '10.92×10.92\n＝119.2464', fs=17, offsets=OFFS)
    z.callout(P(0, 3.0), '点線＝1階の位置', dirs=(180, 165, 195), dists=(30, 45, 60), fs=14)
    save(fig, [z], 'H25_dai22mon_zu13_2kai_kyuuseki')


# ---- 図14：問4の完成形（答案用紙の第4欄：各階平面図と建物図面を実際の大きさで） ----
def zu14():
    fig, ax, z = sheet_figure('各階平面図の完成形（答案用紙の第4欄の各階平面図の側・縮尺1/250の実際の大きさ）')
    sheet4(ax)
    heimen_content(z)
    zumen_content(z)
    assert round(area([P(*v) for v in F1]), 4) == 148.2299 and round(area([P(*v) for v in F2]), 4) == 119.2464
    ax.text((SH_X0 + SH_X1) / 2, 22.0, '各階平面図は壁の中心線の寸法（柱の両面被覆。別紙1の（注）5）で「1階」「2階」を書き分け、2階の図には1階の位置を点線で示す。'
            '求積の式と床面積を各階の横に書く', ha='center', va='center', fontsize=13)
    ax.text((SH_X0 + SH_X1) / 2, 16.5, '方位は建物図面だけに書く（不動産登記規則第82条第2項。各階平面図の第83条第1項には方位がない）。'
            '作成者の「（略）」と縮尺は印刷済み', ha='center', va='center', fontsize=12, color=GRAY)
    save(fig, [z], 'H25_dai22mon_zu14_kakukai_heimenzu')


# ---- 図15：附属建物の増改築の前後比較図 ----
def zu15():
    fig, axes = new_figure('附属建物の増改築（工事前の物置 → 工事後の店舗）',
                           '所在　12番地 → 12番地1（平成25年8月5日分筆により変更）。構造は鉄骨造陸屋根平家建のまま（別紙1の2）',
                           w=16, h=10, ncols=2)
    fig.subplots_adjust(top=0.86, wspace=0.10)
    zs = []
    big = [P(*v) for v in AN1]
    for k, (pts, title) in enumerate([(AN0, '工事前（附属建物符号1・物置）'), (AN1, '工事後（主である建物・店舗〈美容院〉）')]):
        ax = axes[k]
        z = Zu(ax, fontsize=15)
        fit(ax, big, margin=0.35, extra=[xy(P(9.5, 9.5))], pad_aspect=True)
        if k == 1:
            z.north_arrow()
        old = rect(0, 0, 4.5, 5)
        z.poly(old, color=GRAY, lw=0, fill=GRAY, alpha=0.25, check=False)
        if k == 1:
            add = rect(0, 5, 4.5, 8.5)
            z.poly(add, color=ORANGE, lw=1.2, ls='--', fill=ORANGE, alpha=0.30, check=False)
            hatch(ax, add, color=ORANGE)
            z.callout(P(2.25, 6.75), '増築部分\n4.50×3.50＝15.75㎡', dirs=(0, -20, 20), dists=(110, 130, 150), fs=15, color=ORANGE)
        poly = [P(*v) for v in pts]
        z.poly(poly, color=BLACK, lw=2.4)
        h = '5.00' if k == 0 else '8.50'
        dims(z, poly, ['4.50', h, '4.50', h], fs=15)
        z.free_text(P(2.25, -1.6) if k == 0 else P(2.25, -1.6), '物置　4.50×5.00＝22.50㎡' if k == 0 else '店舗　4.50×8.50＝38.25㎡',
                    fs=16, offsets=OFFS, weight='bold')
        ax.set_title(title, fontsize=18, weight='bold', pad=10)
        zs.append(z)
    fig.add_artist(plt.Line2D([0.5, 0.5], [0.13, 0.86], transform=fig.transFigure, color=GRAY, lw=1.2))
    save(fig, zs, 'H25_dai22mon_zu15_fuzoku_zoukaichiku')


# ---- 図20：本番で解く順番 ----
def zu20():
    """本番で解く順番。固定配置の図。check_fixed で文字の重なりとはみ出しを調べ、目視でも確認する。"""
    setup_font()
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　所在だけは座標を出すまで書かない', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '問1〜問4・\n別紙・注を読む', '3つの建物の登記\nと時系列メモ', BLUE),
        ('②', '第3欄\n（問3）の説明', '計算なし。\n報告的登記・保存行為', BLUE),
        ('③', '第1欄・第2欄の\n床面積と所在以外', '目的・添付情報・\n申請人・持分・原因', BLUE),
        ('④', '1階・2階の\n求積', '148.22・119.24\n→第1欄・第2欄へ', RED),
        ('⑤', '座標で建物の\n位置と所在', 'D-Cの線で\n11番地、10番地', RED),
        ('⑥', '第4欄の作図\nと見直し', '建物図面1/500・\n各階平面図1/250', GREEN),
    ]
    w, h, gap = 14.4, 42, 2.0
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 22), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 22 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
        ax.text(x + w / 2, 22 + h / 2 - 3, t, ha='center', va='center', fontsize=16)
        ax.text(x + w / 2, 18, ran, ha='center', va='top', fontsize=14, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, 43), xytext=(x + w + 0.2, 43),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 1.5 * (w + gap) - gap / 2, 76, '計算なしで書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 3 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 4 * (w + gap) - gap / 2, 76, '時間を食う（位置の計算と作図）', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 6 * (w + gap) - gap, 72), xytext=(1 + 3 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '第2欄の所在の欄は、③では空けておき、⑤でD-Cの線を引いてから書く（概略図の見た目で「11番地」と書かない）。\n'
             '求積は問2だけでなく、第1欄の取り壊した主である建物の行（登記記録の抜粋に床面積がない）にも入る',
             ha='center', va='center', fontsize=15)
    check_fixed(fig, 'H25_dai22mon_zu20_toku_junban')
    path = os.path.join(OUT, 'H25_dai22mon_zu20_toku_junban.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


# ======================================================================
# 2026-10-05追加：本文で説明しているのに図がなかった7か所の図（図2・図3・図4・図6・図9・図15・図16）
# ======================================================================

def fixed_figure(title, w=16, h=10, rect=(0.02, 0.04, 0.96, 0.86)):
    """固定配置の図（座標を使わない整理図）。横軸・縦軸とも 0〜100 の作業座標。"""
    setup_font()
    fig = plt.figure(figsize=(w, h), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=24, weight='bold', y=0.975)
    ax = fig.add_axes(list(rect))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    return fig, ax


def check_fixed(fig, name):
    """固定配置の図の重なり検査（文字どうしの重なりと、図の外へのはみ出し）。
    zu_helpers の Zu は座標の図のためのもので、固定配置の図の文字は登録されないので、ここで図の全部の文字を調べる。"""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    texts = list(fig.texts)
    if fig._suptitle is not None and fig._suptitle not in texts:
        texts.append(fig._suptitle)
    for ax in fig.axes:
        texts += list(ax.texts) + [ax.title]
    texts = [t for t in texts if t.get_visible() and t.get_text().strip()]
    bbs = []
    for t in texts:
        bb = t.get_window_extent(r)
        if hasattr(t, 'get_bbox_patch') and t.get_bbox_patch() is not None:
            bb = t.get_bbox_patch().get_window_extent(r)
        bbs.append(bb)
    W, H = fig.bbox.width, fig.bbox.height
    probs = []
    for i, (t, bb) in enumerate(zip(texts, bbs)):
        if bb.x0 < 2 or bb.y0 < 2 or bb.x1 > W - 2 or bb.y1 > H - 2:
            probs.append(f'図の外へのはみ出し: {t.get_text()!r}')
        for t2, bb2 in zip(texts[i + 1:], bbs[i + 1:]):
            if bb.overlaps(bb2):
                probs.append(f'文字どうし: {t.get_text()!r} と {t2.get_text()!r}')
    print(f'[重なり検査] {name}（固定配置）: ' + ('問題なし' if not probs else f'{len(probs)}件'))
    for p in probs:
        print('   ', p)
    PROBLEMS.extend(probs)


def save_fixed(fig, name):
    check_fixed(fig, name)
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def rbox(ax, x, y, w, h, col, alpha=0.12, lw=1.8, ls='-'):
    """角の丸い枠（alpha は塗りの濃さ。0 なら塗らない）。"""
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.5', facecolor=to_rgba(col, alpha) if alpha else 'none',
                                edgecolor=col, lw=lw, ls=ls))


def vline(fig, x, y0=0.10, y1=0.86):
    fig.add_artist(plt.Line2D([x, x], [y0, y1], transform=fig.transFigure, color=GRAY, lw=1.2))


# ---- 図2：注の仕分け（問題文の注1〜注4と、別紙1の（注）1〜9） ----
CHUU_MONDAI = [('注1', '行為は全て適法、書類も全て適法に作成', None),
               ('注2', '登記の申請は書面申請', None),
               ('注3', '建物図面は500分の1、各階平面図は250分の1', '第4欄の縮尺（建物図面・各階平面図）'),
               ('注4', '訂正・加入・削除の書き方', None)]
CHUU_BESSHI = [('（注）1', '概略図は、現地調査のときに簡易に作成したもの', '所在は概略図の見た目でなく座標で決める'),
               ('（注）2', '概略図の［ ］内の数字は土地の地番', None),
               ('（注）3', '数値の単位は全てメートル', None),
               ('（注）4', '概略図の敷地境界からの距離は、全部外壁まで', '建物の位置（2.60・2.56は外壁まで）'),
               ('（注）5', '鉄骨柱の両面は被覆、測定値は柱の中心から', '柱の中心線＝壁の中心線。測定値のまま求積'),
               ('（注）6', '壁厚は全て20センチ', '外壁は壁の中心線から0.10外側'),
               ('（注）7', '天井までの高さは全て2.5メートル以上', '床面積から除く部分はない'),
               ('（注）8', '隅角部は全て直角', None),
               ('（注）9', '見取図1の丸印は、各階の重なる部分', '2階は1階の東の辺にそろえて重ねる')]


def zu02():
    """注の仕分け図。固定配置の図なので check_fixed で文字の重なりを調べ、目視でも確認する。"""
    fig, ax = fixed_figure('注は2か所。番号がかぶるので「どちらの注か」を言い分ける', w=16, h=12.5,
                           rect=(0.02, 0.10, 0.96, 0.80))
    rbox(ax, 1, 3, 36, 85, BLUE, alpha=0.06)
    rbox(ax, 41, 3, 58, 85, ORANGE, alpha=0.06)
    ax.text(19, 96.5, '問題文の注1〜注4', ha='center', va='center', fontsize=20, weight='bold', color=BLUE)
    ax.text(19, 92.0, '（問題文の最後。答案を作るときの前提と決まり）', ha='center', va='center', fontsize=13, color=BLUE)
    ax.text(70, 96.5, '別紙1の（注）1〜9', ha='center', va='center', fontsize=20, weight='bold', color=ORANGE)
    ax.text(70, 92.0, '（各階平面見取図2の下。概略図と見取図の読み方）', ha='center', va='center', fontsize=13, color=ORANGE)

    def rows(items, x, y0, step, col, wrap):
        for k, (no, body, use) in enumerate(items):
            y = y0 - k * step
            c = BLACK if use else GRAY
            ax.text(x, y, no, ha='left', va='center', fontsize=15, weight='bold', color=col if use else GRAY)
            ax.text(x + wrap, y, body, ha='left', va='center', fontsize=14, color=c)
            if use:
                ax.text(x + wrap, y - 3.6, '→ ' + use, ha='left', va='center', fontsize=14, color=col, weight='bold')
    rows(CHUU_MONDAI, 2.5, 83, 9.2, BLUE, 4.5)
    rows(CHUU_BESSHI, 42.5, 83, 9.2, ORANGE, 7.0)
    # 同じ番号でも別の注になる例
    rbox(ax, 3.5, 8, 31, 31, RED, alpha=0.05, lw=1.4)
    ax.text(19, 35.5, '同じ「3」でも別の注', ha='center', va='center', fontsize=16, weight='bold', color=RED)
    ax.text(5, 27.5, '問題文の注3', ha='left', va='center', fontsize=15, weight='bold', color=BLUE)
    ax.text(5, 22.8, '縮尺（500分の1・250分の1）', ha='left', va='center', fontsize=14)
    ax.text(5, 16.0, '別紙1の（注）3', ha='left', va='center', fontsize=15, weight='bold', color=ORANGE)
    ax.text(5, 11.3, '数値の単位はメートル', ha='left', va='center', fontsize=14)
    fig.text(0.5, 0.055, '1〜4の番号はどちらにもある。記事では「問題文の注3」「別紙1の（注）4」のように、どちらの注かを必ず言い分ける',
             ha='center', va='center', fontsize=16, color=RED, weight='bold')
    fig.text(0.5, 0.02, '色付き＝この問題の答えに使う注（→の先が使う場面）、灰色＝本文では取り上げない注',
             ha='center', va='center', fontsize=14)
    save_fixed(fig, 'H25_dai22mon_zu02_chuu_shiwake')


# ---- 図3：解体移転とえい行移転の誤り比較図 ----
def _lots(ax, x0, y0, w12, w11, h):
    """12番（西）と11番（東）を模式で並べる。"""
    ax.add_patch(Rectangle((x0, y0), w12, h, fill=False, lw=1.8, ec=BLACK))
    ax.add_patch(Rectangle((x0 + w12, y0), w11, h, fill=False, lw=1.8, ec=BLACK))
    ax.text(x0 + w12 / 2, y0 + h - 3.2, '12番', ha='center', va='center', fontsize=15)
    ax.text(x0 + w12 + w11 / 2, y0 + h - 3.2, '11番（隣地）', ha='center', va='center', fontsize=15)


def zu03():
    """解体移転とえい行移転。固定配置の模式図（位置・大きさは模式）。"""
    fig, ax = fixed_figure('同じ建材・同じ形でも、一度ばらせば別の建物（準則第85条）', w=16, h=10.5,
                           rect=(0.02, 0.10, 0.96, 0.78))
    for k, (x0, title, tcol) in enumerate([(2, '誤り：本問をえい行移転と同じに扱う', RED),
                                            (52, '正しい：解体移転（本問）', GREEN)]):
        ax.text(x0 + 23, 99, title, ha='center', va='center', fontsize=19, weight='bold', color=tcol)
        _lots(ax, x0, 50, 22, 24, 38)
        old = Rectangle((x0 + 5, 58), 12, 18, fill=False, lw=2.0, ec=GRAY, ls='--')
        ax.add_patch(old)
        new = Rectangle((x0 + 28, 58), 12, 18, facecolor=(GREEN if k else RED), alpha=0.22, ec=BLACK, lw=2.2)
        ax.add_patch(new)
        ax.add_patch(Rectangle((x0 + 28, 58), 12, 18, fill=False, ec=BLACK, lw=2.2))
        ax.annotate('', xy=(x0 + 27.3, 67), xytext=(x0 + 17.7, 67),
                    arrowprops=dict(arrowstyle='-|>', lw=2.4, color=BLACK, mutation_scale=20))
        if k == 0:
            ax.text(x0 + 11, 67, 'もとの\n位置', ha='center', va='center', fontsize=13, color=GRAY)
            ax.text(x0 + 34, 67, '同じ建物', ha='center', va='center', fontsize=14, weight='bold')
            ax.text(x0 + 23, 93.0, '建物をばらさずに、そのまま引っ張って動かす', ha='center', va='center', fontsize=14)
            res = ['所在の変更として扱う（準則第85条第2項）', '同じ建物のまま、所在を変える', '建物表題部変更登記']
            col = RED
        else:
            for dx, dy, ww, hh in [(6.0, 60.5, 4.5, 1.6), (11.5, 63.0, 1.6, 6.5), (6.5, 66.0, 1.6, 6.0), (10.0, 72.0, 5.5, 1.6)]:
                ax.add_patch(Rectangle((x0 + dx, dy), ww, hh, facecolor=ORANGE, alpha=0.7, ec=ORANGE))
            ax.text(x0 + 11, 54.5, '取壊し（滅失）', ha='center', va='center', fontsize=13, color=RED, weight='bold')
            ax.text(x0 + 34, 67, '新築', ha='center', va='center', fontsize=15, weight='bold')
            ax.text(x0 + 34, 54.5, '本件新建物', ha='center', va='center', fontsize=13, weight='bold', color=GREEN)
            ax.text(x0 + 23, 93.0, 'いったんばらして、その建材で隣地に建て直す', ha='center', va='center', fontsize=14)
            res = ['既存の建物の滅失と、新たな建物の建築（準則第85条第1項）', '主である建物は取壊し → 問1（本件旧建物）',
                   '本件新建物は新築 → 建物表題登記（問2）']
            col = GREEN
        rbox(ax, x0 + 0.5, 4, 45, 34, col, alpha=0.10)
        ax.text(x0 + 23, 31.5, res[0], ha='center', va='center', fontsize=14 if k else 15, weight='bold')
        ax.text(x0 + 23, 21.0, res[1], ha='center', va='center', fontsize=15)
        ax.text(x0 + 23, 11.0, res[2], ha='center', va='center', fontsize=16, weight='bold', color=col)
    vline(fig, 0.5, 0.08, 0.90)
    fig.text(0.5, 0.05, '本問は、主である建物を「解体した上でその建材を用いて隣地に再築」（問題文の前文）＝解体移転',
             ha='center', va='center', fontsize=16)
    fig.text(0.5, 0.015, '敷地・建物の位置と大きさは模式', ha='center', va='center', fontsize=13, color=GRAY)
    save_fixed(fig, 'H25_dai22mon_zu03_kaitai_eikou_hikaku')


# ---- 図4：主である建物の滅失と附属建物の誤り比較図 ----
def _kiroku(ax, x, y, w, title, rows):
    """登記記録（表題部）の模式。rows: [(見出し, 中身, 状態, 色)]"""
    h = 9 + 13 * len(rows)
    ax.add_patch(Rectangle((x, y - h), w, h, fill=False, lw=2.0, ec=BLACK))
    ax.text(x + w / 2, y - 4.5, title, ha='center', va='center', fontsize=15, weight='bold')
    ax.plot([x, x + w], [y - 9, y - 9], color=BLACK, lw=1.2)
    for k, (head, body, state, col) in enumerate(rows):
        yy = y - 9 - 13 * k
        if k:
            ax.plot([x, x + w], [yy, yy], color=GRAY, lw=1.0)
        ax.text(x + 1.5, yy - 3.6, head, ha='left', va='center', fontsize=13)
        ax.text(x + 1.5, yy - 9.0, body, ha='left', va='center', fontsize=13, color=GRAY)
        ax.text(x + w - 1.5, yy - 6.5, state, ha='right', va='center', fontsize=13, color=col, weight='bold')
    return y - h


def zu04():
    """主である建物の滅失と附属建物。固定配置の図。"""
    fig, ax = fixed_figure('主である建物がなくなっても、附属建物が残れば滅失登記ではない', w=18, h=10.5,
                           rect=(0.015, 0.10, 0.97, 0.78))
    cols = [(1, '誤り：主である建物がない\n→ 12番の1は建物滅失登記', RED),
            (35, '正しい：附属建物が残る\n→ 建物表題部変更登記（問1）', GREEN),
            (69, '比べる：本件取壊建物（12番の2）\n附属建物がない → 建物滅失登記（問3）', BLUE)]
    for x, t, col in cols:
        ax.text(x + 15, 96, t, ha='center', va='center', fontsize=16, weight='bold', color=col, linespacing=1.4)
    w = 30
    _kiroku(ax, 1, 86, w, '家屋番号12番の1（本件旧建物）',
            [('主である建物', '倉庫', '7月26日取壊し', RED), ('附属建物符号1', '物置', '（見落とす）', GRAY)])
    _kiroku(ax, 35, 86, w, '家屋番号12番の1（本件旧建物）',
            [('主である建物', '倉庫', '7月26日取壊し', RED), ('附属建物符号1', '物置', '残る', GREEN)])
    _kiroku(ax, 69, 86, w, '家屋番号12番の2（本件取壊建物）',
            [('主である建物（附属建物なし）', '店舗', '7月26日取壊し', RED)])
    res = [(1, RED, ['建物の全部がなくなったと考えて', '建物滅失登記を申請する', '（附属建物がまだ建っている）']),
           (35, GREEN, ['主である建物の欄：「取壊し」', '附属建物を主である建物に変更', '主である建物の欄と附属建物の欄の両方に\n「主である建物に変更」（準則第102条）']),
           (69, BLUE, ['1個の建物の全部がなくなった', '建物滅失登記（不動産登記法第57条）', '共有者の1人で申請できるか → 問3'])]
    for x, col, lines in res:
        rbox(ax, x + 0.5, 5, w - 1, 41, col, alpha=0.10)
        for k, t in enumerate(lines):
            ax.text(x + 15, 38 - 11.5 * k, t, ha='center', va='center', fontsize=14, weight='bold' if k == 1 else 'normal',
                    color=col if k == 1 else BLACK, linespacing=1.4)
    for x in (0.34, 0.66):
        vline(fig, x, 0.08, 0.90)
    fig.text(0.5, 0.05, '家屋番号12番の1の登記記録は、主である建物と附属建物をまとめて1個の建物として扱う。附属建物が残っている限り滅失していない',
             ha='center', va='center', fontsize=15)
    save_fixed(fig, 'H25_dai22mon_zu04_shu_messhitsu_fuzoku')


# ---- 図6：座標と距離から建物の位置を出す図（計算の手順） ----
ZOOM6 = (24.55, 28.15, 73.0, 83.2)   # 右のパネルの範囲 (X0, X1, Y0, Y1)


def zu06():
    fig, axes = new_figure('座標と距離から、本件新建物の位置を出す（計算の手順）',
                           '①北の外壁 39.24−2.60＝36.64、壁の中心線 36.54　②南の壁の中心線 36.54−10.92＝25.62（D点27.15より1.53南）\n'
                           '③西の壁：D-Fの線 Y＝約75.06＋2.56＝約77.62（外壁）、壁の中心線 約77.72　④D-Cの線は西の壁で X＝約26.36（南の壁より約0.74北）、\n'
                           '南の壁と Y＝約80.43（西の壁から約2.71東）で交わる → 約1.0㎡が10番、残り約147.2㎡が11番',
                           w=18, h=12, ncols=2, width_ratios=[1, 1.3])
    fig.subplots_adjust(top=0.88, bottom=0.17, wspace=0.05)
    for t in fig.texts:
        if t is not fig._suptitle:
            t.set_fontsize(15)
    bldg = [B_(*v) for v in F1]
    w_ext = W0 - HALF
    zs = []

    def df_y(x):
        return D.imag + (D.real - x) * (F.imag - D.imag) / (D.real - F.real)

    def ce_y(x):
        return C.imag + (C.real - x) * (E.imag - C.imag) / (C.real - E.real)
    # 左：全体（①②）
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fit(ax, [complex(41.6, 67.5), complex(20.0, 104.0)], margin=0.0, pad_aspect=True)
    z.north_arrow()
    z.poly(LOT11, color=BLACK, lw=2.0)
    z.line(D, complex(20.0, df_y(20.0)), color=BLACK, lw=2.0)
    z.line(C, complex(20.0, ce_y(20.0)), color=BLACK, lw=2.0)
    z.poly(bldg, color=GREEN, lw=2.2, fill=GREEN, alpha=0.18)
    z.poly(TRI10, color=RED, lw=0, fill=RED, alpha=0.85, check=False)
    X0, X1, Y0, Y1 = ZOOM6
    z.poly([complex(X0, Y0), complex(X0, Y1), complex(X1, Y1), complex(X1, Y0), complex(X0, Y0)], color=RED, lw=1.3, ls='--',
           closed=False)
    for p in (A, D, C):
        z.point(p)
    z.point_label(A, 'A', away=complex(30, 85), fs=15)
    z.point_label(D, 'D', away=complex(31, 85), fs=15)
    z.point_label(C, 'C', away=complex(30, 85), fs=15)
    # ① 2.60（北の道路境界 X＝39.24 → 北の外壁 36.64）
    yv = W0 + 5.0
    z.dim_line(complex(39.24, yv), complex(N_EXT, yv))
    z.free_text(complex((39.24 + N_EXT) / 2, yv), '①2.60', fs=14, offsets=((26, 0), (30, 0), (-26, 0)))
    # ② 10.92（北の壁の中心線 → 南の壁の中心線。建物の中で西の壁に沿って）
    yv2 = W0 + 2.2
    z.dim_line(complex(N0, yv2), complex(S0, yv2))
    z.free_text(complex((N0 + S0) / 2, yv2), '②10.92', fs=14, offsets=((28, 0), (32, 0)))
    z.callout(complex(39.24, 88.0), '北の道路境界 X＝39.24', dirs=(60, 75, 45), dists=(30, 45), fs=13)
    z.callout(complex(N0, 91.0), '北の外壁 X＝36.64\n壁の中心線 X＝36.54', dirs=(-15, -30, 0, 15), dists=(55, 70, 90), fs=13, color=GREEN)
    z.callout(complex(S0, 84.0), '南の壁の中心線\nX＝25.62', dirs=(-80, -65, -95), dists=(45, 65), fs=13, color=GREEN)
    z.callout(D, 'D点 X＝27.15', dirs=(150, 165, 135, 120), dists=(40, 55, 70), fs=13)
    z.free_text(complex(33.5, 80.6), '11', fs=18, offsets=OFFS)
    z.free_text(complex(23.5, 90.5), '10', fs=18, offsets=OFFS)
    z.free_text(complex(27.0, 98.0), '9-1', fs=14, offsets=OFFS, color=GRAY)
    z.free_text(complex(36.5, 70.5), '12-1', fs=14, offsets=OFFS, color=GRAY)
    ax.set_title('①②　北から X座標を出す（赤い点線の枠を右に拡大）', fontsize=16, weight='bold', pad=10)
    zs.append(z)
    # 右：南西の角の拡大（③④）
    ax = axes[1]
    z = Zu(ax, fontsize=14)
    fit(ax, [complex(X0, Y0), complex(X1, Y1)], margin=0.0, pad_aspect=True)
    z.north_arrow()
    xl, xh = ax.get_ylim()
    z.line(complex(xh, D.imag - (xh - D.real) * (D.imag - A.imag) / (A.real - D.real)), D, color=BLACK, lw=2.2)
    z.line(D, complex(xl, df_y(xl)), color=BLACK, lw=2.2)
    z.line(D, complex(dc_x(Y1), Y1), color=BLACK, lw=2.8)
    z.point(D)
    z.point_label(D, 'D', away=complex(27.6, 76.5), fs=16)
    # 西の外壁・南の外壁（点線）と、壁の中心線（実線）
    z.line(complex(xh, w_ext), complex(S_EXT, w_ext), color=GREEN, lw=1.2, ls='--')
    z.line(complex(S_EXT, w_ext), complex(S_EXT, Y1), color=GREEN, lw=1.2, ls='--')
    z.line(complex(xh, W0), complex(S0, W0), color=GREEN, lw=2.6)
    z.line(complex(S0, W0), complex(S0, Y1), color=GREEN, lw=2.6)
    z.poly(TRI10, color=RED, lw=0, fill=RED, alpha=0.85, check=False)
    p1, p2 = TRI10[0], TRI10[2]
    z.point(p1, color=RED)
    z.point(p2, color=RED)
    # ③ 2.56（D-Fの線 → 西の外壁。南の外壁の高さで）
    xd = S_EXT - 0.35
    z.dim_line(complex(xd, Y_DF), complex(xd, w_ext))
    z.line(complex(S_EXT, Y_DF), complex(xd - 0.12, Y_DF), color=GRAY, lw=1.0)
    z.line(complex(S_EXT, w_ext), complex(xd - 0.12, w_ext), color=GRAY, lw=1.0)
    z.free_text(complex(xd, (Y_DF + w_ext) / 2), '③2.56', fs=14, offsets=((0, -13), (0, -16)))
    # ④ 約2.71（南の壁の中心線の上で、西の壁から交点まで）
    xs = S_EXT - 0.75
    z.dim_line(complex(xs, W0), complex(xs, p2.imag))
    z.line(complex(S0, W0), complex(xs - 0.12, W0), color=GRAY, lw=1.0)
    z.line(p2, complex(xs - 0.12, p2.imag), color=GRAY, lw=1.0)
    z.free_text(complex(xs, (W0 + p2.imag) / 2), '④約2.71', fs=14, offsets=((0, -13), (0, -16)))
    # ④ 約0.74（西の壁の中心線のところで、D-Cの線と南の壁の差）
    yv = W0 - 0.55
    z.dim_line(complex(p1.real, yv), complex(S0, yv))
    z.line(p1, complex(p1.real, yv - 0.12), color=GRAY, lw=1.0)
    z.line(complex(S0, W0), complex(S0, yv - 0.12), color=GRAY, lw=1.0)
    z.free_text(complex((p1.real + S0) / 2, yv), '④約0.74', fs=14, offsets=((-36, 0), (-38, 0), (-36, -5)))
    # ② 1.53（D点の高さと南の壁の中心線の差）
    yd = 75.95
    z.dim_line(complex(D.real, yd), complex(S0, yd))
    z.line(D, complex(D.real, yd + 0.15), color=GRAY, lw=1.0)
    z.line(complex(S0, W0), complex(S0, yd - 0.15), color=GRAY, lw=1.0)
    z.free_text(complex((D.real + S0) / 2, yd), '②1.53', fs=14, offsets=((-28, 0), (-24, 0)))
    z.callout(complex(23.6, df_y(23.6)), 'D-Fの線 Y＝約75.06\n（南の外壁 X＝25.52の高さで）', dirs=(-20, -35, -5), dists=(45, 65, 85), fs=13)
    z.callout(complex(27.7, w_ext), '西の外壁 Y＝約77.62（点線）\n壁の中心線 Y＝約77.72', dirs=(25, 40, 10), dists=(50, 70, 90), fs=13,
              color=GREEN)
    z.callout(p1, 'D-Cの線 X＝約26.36', dirs=(20, 35, 5), dists=(80, 100, 120), fs=13, color=RED)
    z.callout(p2, '交点 Y＝約80.43', dirs=(30, 45, 15, 60), dists=(55, 75, 95), fs=13, color=RED)
    z.callout(complex(25.75, 78.4), '約1.0㎡が10番', dirs=(-100, -115, -85), dists=(80, 100, 120), fs=14, color=RED)
    z.callout(complex(S0, 82.4), '南の壁の中心線 X＝25.62', dirs=(-110, -125, -95), dists=(40, 55, 70), fs=13, color=GREEN)
    z.free_text(complex(27.2, 80.6), '建物（1階）', fs=15, color=GREEN, offsets=OFFS, weight='bold')
    z.free_text(complex(26.5, 74.2), '12-1', fs=14, color=GRAY, offsets=OFFS)
    z.free_text(complex(23.7, 81.6), '10', fs=17, offsets=OFFS)
    z.free_text(complex(27.6, 79.0), '11', fs=17, offsets=OFFS)
    ax.set_title('③④　南西の角の拡大（西の壁とD-Cの線）', fontsize=16, weight='bold', pad=10)
    zs.append(z)
    fig.add_artist(plt.Line2D([0.44, 0.44], [0.18, 0.88], transform=fig.transFigure, color=GRAY, lw=1.0))
    save(fig, zs, 'H25_dai22mon_zu06_tatemono_ichi_keisan')


# ---- 図10：鉄骨柱の測り方の誤り比較図（建物の北西の角の詳細。柱の大きさは模式） ----
COL = 0.07     # 柱の半分の幅（模式）
L9E, L9S = 1.30, 0.95   # 描く範囲：角から東へ・南へ


def zu10():
    fig, axes = new_figure('鉄骨柱の両面が被覆されているときは、柱の中心線で測る',
                           '別紙1の（注）5：鉄骨柱の両面は被覆、測定値は柱の中心から。別紙1の（注）6：壁厚は20センチ。\n'
                           '両面被覆なら柱の中心線＝壁の中心線なので、測定値（8.19・10.92など）をそのまま使う（不動産登記規則第115条）。'
                           '建物の北西の角の詳細で、柱の大きさは模式',
                           w=16, h=10.5, ncols=2)
    fig.subplots_adjust(top=0.86, bottom=0.17, wspace=0.08)
    for t in fig.texts:
        if t is not fig._suptitle:
            t.set_fontsize(15)
    zs = []
    for k, (title, tcol) in enumerate([('誤り：外側だけ被覆と思い、柱の外面で測る', RED),
                                        ('正しい：両面被覆なので、柱の中心線で測る', GREEN)]):
        ax = axes[k]
        z = Zu(ax, fontsize=14)
        fit(ax, [complex(0.55, -0.80), complex(-L9S, L9E)], margin=0.0, pad_aspect=True)
        z.north_arrow()
        if k == 1:      # 被覆（壁）は中心線の両側に0.10ずつ
            wall = [complex(0.10, -0.10), complex(0.10, L9E), complex(-0.10, L9E), complex(-0.10, 0.10), complex(-L9S, 0.10),
                    complex(-L9S, -0.10)]
        else:           # 誤り：柱の外側だけに被覆があると思い込む
            wall = [complex(0.10, -0.10), complex(0.10, L9E), complex(COL, L9E), complex(COL, -COL), complex(-L9S, -COL),
                    complex(-L9S, -0.10)]
        z.poly(wall, color=GRAY, lw=1.4, fill=GRAY, alpha=0.30)
        colp = [complex(COL, -COL), complex(COL, COL), complex(-COL, COL), complex(-COL, -COL)]
        z.poly(colp, color=BLACK, lw=1.8, fill=BLACK, alpha=0.75)
        if k == 0:
            z.line(complex(COL, -COL), complex(COL, L9E), color=RED, lw=3.0)
            z.line(complex(COL, -COL), complex(-L9S, -COL), color=RED, lw=3.0)
            z.callout(complex(COL, 0.60), '柱の外面を区画の線にする\n（柱の外側だけが被覆のときの測り方）', dirs=(-100, -115, -85), dists=(80, 100, 120),
                      fs=14, color=RED)
            z.callout(complex(-0.55, -COL), 'でも本問の測定値は\n柱の中心から（別紙1の（注）5）', dirs=(0, -15, 15), dists=(60, 80, 100),
                      fs=14, color=RED)
        else:
            z.line(complex(0, 0), complex(0, L9E), color=GREEN, lw=3.0)
            z.line(complex(0, 0), complex(-L9S, 0), color=GREEN, lw=3.0)
            z.callout(complex(0, 0.60), '柱の中心線＝壁の中心線\n（測定値8.19・10.92はここから）', dirs=(-100, -115, -85), dists=(80, 100, 120),
                      fs=14, color=GREEN)
            z.callout(complex(0.10, 0.62), '外壁（中心線から0.10外側）', dirs=(80, 95, 65), dists=(55, 75, 95), fs=14)
            z.dim_line(complex(-0.10, 1.12), complex(0.10, 1.12))
            z.free_text(complex(0.10, 1.12), '壁厚0.20', fs=14, offsets=((0, 16), (0, 20)))
        z.callout(complex(-COL, -COL), '鉄骨柱', dirs=(-150, -165, -135), dists=(45, 60), fs=14)
        z.callout(complex(-0.75, -0.10 if k else -0.085), '被覆（両面）' if k else '被覆（外側だけ）', dirs=(-150, -135, -165), dists=(35, 50, 65), fs=14)
        z.free_text(complex(-0.80, 0.85), '建物の中', fs=16, offsets=OFFS, color=GRAY)
        z.free_text(complex(0.32, -0.32), '外', fs=16, offsets=OFFS, color=GRAY)
        ax.set_title(title, fontsize=17, weight='bold', color=tcol, pad=10)
        zs.append(z)
    vline(fig, 0.5, 0.17, 0.86)
    save(fig, zs, 'H25_dai22mon_zu10_hashira_hikaku')


# ---- 図16：12番の分筆と附属建物の所在の変更（12番2の西の端と附属建物の位置は模式） ----
W12 = 58.57    # 12番2の西の端（道路との境）。問題に座標がないので模式
FZ_W = 66.57 + 1.40 + 0.10     # 附属建物の西の壁の中心線（概略図の1.40を目安にした模式）
FZ_N = 39.24 - 1.00 - 0.10     # 附属建物の北の壁の中心線（模式）


def zu16():
    fig, axes = new_figure('12番の分筆（8月5日）で、附属建物の所在が「12番地」から「12番地1」に変わる',
                           '原因「平成25年8月5日分筆により変更」（不動産登記法第51条第1項で1月以内に申請）。家屋番号は、申請書には今の「12番の1」を書き、\n'
                           '登記官が変える（不動産登記事務取扱手続準則第79条第10号）。G・H・A・D・Fは座標どおり、12番2の西の端と附属建物の位置は模式',
                           w=16, h=11, ncols=2)
    fig.subplots_adjust(top=0.86, bottom=0.16, wspace=0.06)
    zs = []
    W_ = complex(39.24, W12)
    S_ = complex(17.07, W12)
    lot12 = [W_, A, D, F, S_]
    lot12_2 = [W_, G, H, S_]
    for k, (title, h_) in enumerate([('8月5日まで（分筆の前）：12番（1筆）', 5.0), ('分筆の後：12番1・12番2（申請時）', 8.5)]):
        ax = axes[k]
        z = Zu(ax, fontsize=14)
        fit(ax, [complex(42.0, W12 - 1.5), complex(13.6, 80.5)], margin=0.0, pad_aspect=True)
        z.north_arrow()
        if k == 0:
            z.poly(lot12, color=BLACK, lw=2.4, fill=GRAY, alpha=0.10)
            z.line(G, H, color=GRAY, lw=1.6, ls='--')
            z.free_text(complex(28.5, 63.0), '12', fs=22, offsets=OFFS, weight='bold')
            z.callout(complex(22.0, 66.57), '道路拡幅予定線（G-H）', dirs=(-20, -35, -5), dists=(40, 60, 80), fs=13, color=GRAY)
        else:
            z.poly(lot12_2, color=BLACK, lw=2.2, fill=GRAY, alpha=0.18)
            z.poly(LOT12_1, color=BLACK, lw=2.4, fill=BLUE, alpha=0.10)
            z.free_text(complex(28.0, 62.6), '12-2\n（道路拡幅用地）', fs=14, offsets=OFFS)
            z.free_text(complex(23.0, 70.5), '12-1', fs=22, offsets=OFFS, weight='bold', color=BLUE)
            z.callout(complex(22.0, 66.57), '分筆線（G-H）', dirs=(-20, -35, -5), dists=(40, 60, 80), fs=13)
        z.line(D, complex(dc_x(80.5), 80.5), color=BLACK, lw=1.4)
        for p, n in [(G, 'G'), (H, 'H'), (A, 'A'), (D, 'D'), (F, 'F')]:
            z.point(p)
        for p, n in [(G, 'G'), (H, 'H'), (A, 'A'), (D, 'D'), (F, 'F')]:
            z.point_label(p, n, away=complex(28, 66.57 if n in 'GH' else 72.0), fs=15)
        bld = rect(0, 0, 4.5, h_, f=lambda e, s: complex(FZ_N - s, FZ_W + e))
        z.poly(bld, color=BLACK, lw=2.2, fill=ORANGE, alpha=0.35)
        z.callout(complex(FZ_N - h_ / 2, FZ_W + 4.5), '附属建物' + ('（物置）' if k == 0 else '\n（主である建物・店舗）'),
                  dirs=(-20, -35, -5), dists=(40, 60, 80), fs=13)
        z.free_text(complex(40.6, 70.0), '道路（51）', fs=14, offsets=OFFS)
        z.free_text(complex(30.0, 77.5), '11', fs=16, offsets=OFFS)
        z.free_text(complex(19.5, 78.4), '10', fs=16, offsets=OFFS)
        shozai = '本件旧建物の所在：C市D町一丁目12番地' if k == 0 else '本件旧建物の所在：C市D町一丁目12番地1'
        z.free_text(complex(15.6, 66.0), shozai, fs=16, offsets=((0, -14), (0, -20), (0, -26)), weight='bold', color=BLACK if k == 0 else BLUE)
        ax.set_title(title, fontsize=17, weight='bold', pad=10)
        zs.append(z)
    vline(fig, 0.5, 0.16, 0.86)
    save(fig, zs, 'H25_dai22mon_zu16_bunpitsu_shozai')


# ---- 図19：形成的登記と報告的登記の比較図 ----
def zu19():
    fig, ax = fixed_figure('共有の建物の滅失登記は、共有者の1人で申請できる', w=16, h=10.5, rect=(0.02, 0.10, 0.96, 0.78))
    blocks = [(2, '誤り：共有物の登記だから共有者全員で', RED,
               ['形成的登記の考え方', '合併・分割のように、登記で建物の\n個数や範囲を新しく作り変える', 'その考え方を滅失登記にも\nあてはめてしまう',
                '共有者全員（甲野春男・甲野冬子）で申請']),
              (52, '正しい：滅失登記は報告的登記', GREEN,
               ['報告的登記', '建物が取り壊された事実を、\nそのまま登記記録に反映させる', '共有物の処分・変更ではなく、\n共有物の保存行為（民法第252条第5項）',
                '共有者の1人（甲野春男）が単独で申請できる'])]
    for x0, title, col, lines in blocks:
        ax.text(x0 + 23, 98, title, ha='center', va='center', fontsize=19, weight='bold', color=col)
        ys = [84, 63, 42, 18]
        for k, (y, t) in enumerate(zip(ys, lines)):
            last = k == len(lines) - 1
            rbox(ax, x0 + 1, y - 6.5, 44, 13, col, alpha=0.28 if last or k == 0 else 0.10, lw=2.4 if last else 1.6)
            ax.text(x0 + 23, y, t, ha='center', va='center', fontsize=17 if k == 0 else 15,
                    weight='bold' if (k == 0 or last) else 'normal', linespacing=1.35)
            if not last:
                ax.annotate('', xy=(x0 + 23, ys[k + 1] + 8.0), xytext=(x0 + 23, y - 7.5),
                            arrowprops=dict(arrowstyle='-|>', lw=1.8, color=col, mutation_scale=18))
    vline(fig, 0.5, 0.08, 0.90)
    fig.text(0.5, 0.05, '本件取壊建物の建物滅失登記：滅失の日から1月以内に申請（不動産登記法第57条）。怠ると10万円以下の過料（同法第164条第1項）',
             ha='center', va='center', fontsize=15)
    save_fixed(fig, 'H25_dai22mon_zu19_keiseiteki_houkokuteki')


# ======================================================================
# 2026-10-16追加：本文に対して図がなかった所在の順序（図8）と、添付情報の各号の当てはめ表（図17・図18）
# ======================================================================

# ---- 図8：所在の順序の誤り比較図（地番の順ではなく床面積の多い順） ----
def zu08():
    """所在の順序。固定配置の図なので check_fixed で文字の重なりを調べ、目視でも確認する。"""
    on11, on10 = 147.2, 1.0          # 1階のうち11番の上・10番の上（記事の約147.2㎡・約1.0㎡。照合スクリプトで多角形を切って確かめる）
    fig, ax = fixed_figure('2筆にまたがる建物の所在は、地番の順ではなく床面積の多い順', w=16, h=10,
                           rect=(0.02, 0.10, 0.96, 0.78))
    for x0, title, col in [(2, '誤り：地番の順に書く', RED), (52, '正しい：床面積の多い部分の地番が先', GREEN)]:
        ax.text(x0 + 23, 99, title, ha='center', va='center', fontsize=19, weight='bold', color=col)
        rbox(ax, x0 + 0.5, 4, 45, 86, col, alpha=0.06)
    # 左：番号の小さい順
    ax.text(25, 80, '番号の小さい10番地を先に', ha='center', va='center', fontsize=15)
    for k, (no, t) in enumerate([('1番目', '10番地'), ('2番目', '11番地')]):
        ax.text(10, 62 - 16 * k, no, ha='left', va='center', fontsize=15, color=GRAY)
        ax.text(26, 62 - 16 * k, t, ha='left', va='center', fontsize=20, weight='bold', color=RED)
    rbox(ax, 4, 9, 42, 17, RED, alpha=0.10, lw=1.4)
    ax.text(25, 21.5, 'C市D町一丁目10番地、11番地', ha='center', va='center', fontsize=16, weight='bold', color=RED)
    ax.text(25, 13.0, '（番号の順にしてしまう誤り）', ha='center', va='center', fontsize=14, color=RED)
    # 右：床面積の棒
    ax.text(75, 80, '本件新建物の1階のうち、どちらの土地の上が多いか', ha='center', va='center', fontsize=15)
    full = 30.0
    for k, (lot, v, c) in enumerate([('11番の上', on11, GREEN), ('10番の上', on10, ORANGE)]):
        y = 64 - 15 * k
        ax.text(56, y, lot, ha='left', va='center', fontsize=15)
        bar = max(full * v / on11, 0.6)
        ax.add_patch(Rectangle((66, y - 3.2), bar, 6.4, facecolor=c, alpha=0.55, edgecolor=c))
        if k == 0:     # 長い棒は棒の中に白抜きで
            ax.text(66 + bar - 1.0, y, f'約{v:.1f}㎡', ha='right', va='center', fontsize=15, weight='bold', color='white')
        else:          # 短い棒は棒の右に
            ax.text(68 + bar, y, f'約{v:.1f}㎡', ha='left', va='center', fontsize=15, weight='bold')
    rbox(ax, 54, 9, 42, 17, GREEN, alpha=0.12, lw=1.4)
    ax.text(75, 21.5, 'C市D町一丁目11番地、10番地', ha='center', va='center', fontsize=16, weight='bold', color=GREEN)
    ax.text(75, 13.0, '（不動産登記事務取扱手続準則第88条第2項）', ha='center', va='center', fontsize=14, color=GREEN)
    vline(fig, 0.5, 0.08, 0.90)
    fig.text(0.5, 0.05, '10番の上は南西の角の約1.0㎡だけでも所在に書く。順序は床面積の多い11番地が先（第2欄の所在、建物図面・各階平面図の建物の所在も同じ）',
             ha='center', va='center', fontsize=15)
    save_fixed(fig, 'H25_dai22mon_zu08_shozai_junjo')


def tekiyou_table(name, title, caption, rows):
    """各号・本問の事実・結果の3列の当てはめ表（固定配置）。rows：[(各号, 事実, 結果, 色)]"""
    fig, ax = fixed_figure(title, w=16, h=12, rect=(0.02, 0.12, 0.96, 0.78))
    cols = [(1, 30, '各号（添付情報欄など）'), (30, 77, '本問の事実'), (77, 99, '結果')]
    top = 99.0
    rh = (top - 9 - 1.0) / len(rows)
    for x0, x1, t in cols:
        ax.add_patch(Rectangle((x0, top - 9), x1 - x0, 9, facecolor=to_rgba(BLACK, 0.06), edgecolor=BLACK, lw=1.4))
        ax.text((x0 + x1) / 2, top - 4.5, t, ha='center', va='center', fontsize=15, weight='bold')
    for j, (a, b, c, col) in enumerate(rows):
        y1 = top - 9 - j * rh
        y0 = y1 - rh
        for x0, x1, _ in cols:
            ax.add_patch(Rectangle((x0, y0), x1 - x0, rh, fill=False, edgecolor=BLACK, lw=1.1))
        ym = (y0 + y1) / 2
        ax.text(2.2, ym, a, ha='left', va='center', fontsize=13.5, weight='bold', linespacing=1.6)
        ax.text(31.2, ym, b, ha='left', va='center', fontsize=13, linespacing=1.6)
        ax.text(88, ym, c, ha='center', va='center', fontsize=14, weight='bold', color=col, linespacing=1.6)
    fig.text(0.5, 0.065, caption[0], ha='center', va='center', fontsize=14.5)
    fig.text(0.5, 0.025, caption[1], ha='center', va='center', fontsize=13.5, color=GRAY)
    save_fixed(fig, name)


# ---- 図17：第1欄（建物表題部変更登記）の添付情報の当てはめ表 ----
def zu17():
    tekiyou_table(
        'H25_dai22mon_zu17_tenpu_dai1ran', '第1欄の添付情報：不動産登記令別表14の項の各号を事実に当てはめる',
        ('入れるのは建物図面・各階平面図・所有権証明情報・代理権限証明情報の4つ（答案用紙の欄の名前が「添付情報」なので「〜情報」で書く）',
         '登録免許税は答案用紙に欄がない（表題部の変更の登記は登録免許税法別表第一の一（十三）に当たらない）'),
        [('イ　所在を変更するとき', '12番の分筆（8月5日）で、所在が\n12番地 → 12番地1', '建物図面', GREEN),
         ('ロ（1）　床面積を変更するとき', '主である建物の取壊し（7月26日）、\n附属建物の増築（22.50 → 38.25）', '建物図面・\n各階平面図', GREEN),
         ('ロ（2）　床面積が増加するとき', '南へ4.50×3.50＝15.75㎡増えた部分が\n甲野春男・甲野冬子のものであること', '所有権証明情報', GREEN),
         ('ハ　附属建物を新築したとき', '新築した附属建物はない', '当たらない', GRAY),
         ('ニ　共用部分である旨の登記', '共用部分である旨の登記はない', '当たらない', GRAY),
         ('種類の変更（物置 → 店舗）', '別表14の項の添付情報欄に定めがない', '足すものなし', GRAY),
         ('令第7条第1項第2号　代理人', '土地家屋調査士が代理して申請する', '代理権限証明情報', GREEN),
         ('住所証明情報', '表題登記の別表12の項ニの情報。\n別表14の項にはない', '入れない', GRAY)])


# ---- 図18：第2欄（建物表題登記）の添付情報の当てはめ表 ----
def zu18():
    tekiyou_table(
        'H25_dai22mon_zu18_tenpu_dai2ran', '第2欄の添付情報：不動産登記令別表12の項の各号を事実に当てはめる',
        ('入れるのは建物図面・各階平面図・所有権証明情報・住所証明情報・代理権限証明情報の5つ',
         '登録免許税は答案用紙に欄がない（建物の表題登記は登録免許税法別表第一に載っていない）'),
        [('イ　建物図面', '本件新建物の敷地と1階の位置・形状', '建物図面', GREEN),
         ('ロ　各階平面図', '1階148.22㎡・2階119.24㎡', '各階平面図', GREEN),
         ('ハ　所有権を有することを証する情報', '材料を出した乙川建設ではなく、代金を払い終えた\n2人が所有者（準則第87条第1項：建築請負人の証明情報など）',
          '所有権証明情報', GREEN),
         ('ニ　住所を証する情報', '表題部所有者になる甲野春男・甲野冬子の2人の分', '住所証明情報', GREEN),
         ('ホ・ヘ　区分建物・敷地権', '区分建物ではない', '当たらない', GRAY),
         ('ト　法第47条第2項（一般承継人）', '所有者本人の2人が申請する', '当たらない', GRAY),
         ('令第7条第1項第2号　代理人', '土地家屋調査士が代理して申請する', '代理権限証明情報', GREEN)])


if __name__ == '__main__':
    # 記事の挿入順（図1〜図20）
    zu01()
    zu02()
    zu03()
    zu04()
    zu05()
    zu06()
    zu07()
    zu08()
    zu09()
    zu10()
    zu11()
    zu12()
    zu13()
    zu14()
    zu15()
    zu16()
    zu17()
    zu18()
    zu19()
    zu20()
    print('重なり合計:', len(PROBLEMS))
