"""平成25年度 第22問（建物）の解説図10枚を、座標成果・各階平面見取図の寸法から作図してPNGに書き出す。

`../prompt_H25_dai22mon_kaisetsuzu.md` の図1〜図10どおり（番号は記事の挿入順）。作図の共通部品は `tools/zu_helpers.py`。
図4（建物図面）と図8（各階平面図）の完成形は、答案用紙の第4欄（建物図面及び各階平面図）の欄の形
（家屋番号・建物の所在、建物図面の側は「申請人」〈（略）の印刷なし〉と縮尺1/500、各階平面図の側は「作成者（略）
（平成何年何月何日作成）」と縮尺1/250）の枠の中に描く。答案用紙は `public/kijutsu/H25-tatemono/a2.webp`（試験の答案用紙）で確かめた。
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


def dist_arrow(z, p, q, text, fs=15, offs=((14, 0), (-14, 0), (0, 12), (0, -12))):
    """筆界から外壁までの距離の矢印（両向き）と数値。"""
    z.ax.annotate('', xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='<|-|>', color=BLACK, lw=1.6,
                                                           mutation_scale=14, shrinkA=0, shrinkB=0), zorder=6)
    z.segments.append((xy(p), xy(q)))
    return z.free_text((p + q) / 2, text, fs=fs, offsets=offs)


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.012
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


def sheet_header(fig, title):
    """第4欄の上の欄：家屋番号（空欄。登記所が付ける）と建物の所在。"""
    cell(fig, 0.06, 0.885, 0.20, 0.935, '家屋番号', fs=15)
    cell(fig, 0.20, 0.885, 0.46, 0.935)
    fig.text(0.70, 0.910, title, ha='center', va='center', fontsize=20)
    cell(fig, 0.06, 0.835, 0.20, 0.885, '建物の所在', fs=15)
    cell(fig, 0.20, 0.835, 0.94, 0.885, 'C市D町一丁目11番地、10番地', fs=16, ha='left', color=INK)


OFFS = ((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0), (24, 12), (-24, -12))


# ---- 図1：時系列と、3つの建物の行き先 ----
def zu01():
    """固定配置の図なので重なり検査の対象外（目視で確認）。"""
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
    path = os.path.join(OUT, 'H25_dai22mon_zu01_jikeiretsu.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図1: 時系列（固定配置）\n  →', path)


# ---- 図2：敷地の辺長確認図（作図チェック用） ----
def zu02():
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
    save(fig, [z], 'H25_dai22mon_zu02_shikichi_henchou')


# ---- 図3：所在の誤り比較図（左：概略図の見た目、中：座標で描いた実際、右：南西の角の拡大） ----
ZOOM = [complex(24.6, 73.6), complex(24.6, 82.6), complex(28.0, 82.6), complex(28.0, 73.6)]


def zu03():
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
    save(fig, zs, 'H25_dai22mon_zu03_shozai_ayamari_hikaku')


# ---- 図4：建物図面の完成形（答案用紙の第4欄の右半分の形） ----
def zu04():
    setup_font()
    fig = plt.figure(figsize=(16, 14), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面の完成形（答案用紙の第4欄の右側・縮尺1/500で描く内容）', fontsize=22, weight='bold', y=0.985)
    sheet_header(fig, '建　物　図　面')
    cell(fig, 0.06, 0.085, 0.94, 0.835, lw=1.8)
    fig.text(0.925, 0.10, '（単位：m）', ha='right', va='bottom', fontsize=13)
    cell(fig, 0.06, 0.035, 0.20, 0.085, '申　請　人', fs=15)
    cell(fig, 0.20, 0.035, 0.74, 0.085, '甲野春男　甲野冬子', fs=16, ha='left', color=INK)
    cell(fig, 0.74, 0.035, 0.83, 0.085, '縮尺', fs=15)
    cell(fig, 0.83, 0.035, 0.94, 0.085, '1/500', fs=15)
    ax = fig.add_axes([0.08, 0.12, 0.84, 0.70])
    z = Zu(ax, fontsize=15)
    fit(ax, OUTER, margin=0.06, extra=[xy(complex(41.6, 70.0)), xy(complex(15.0, 99.0))], pad_aspect=True)
    z.north_arrow()
    # 隣接地との境（11番・10番に接する部分だけ）
    z.line(complex(39.24, 69.5), A, color=BLACK, lw=1.4)
    z.line(B, complex(39.24, 97.6), color=BLACK, lw=1.4)
    z.line(complex(17.07, 72.5), F, color=BLACK, lw=1.4)
    z.line(E, complex(17.07, 97.6), color=BLACK, lw=1.4)
    z.poly(LOT11, color=BLACK, lw=2.2)
    z.poly(LOT10, color=BLACK, lw=2.2)
    bldg = [B_(*v) for v in F1]
    z.poly(bldg, color=BLACK, lw=2.6)
    assert round(area(bldg), 4) == 148.2299
    # 距離（外壁まで）：北西・北東の角から北の道路境A-Bまで2.60、南西の角から西の筆界D-Fまで2.56
    w_ext, e_ext = W0 - HALF, W0 + 14.56 + HALF
    dist_arrow(z, complex(N_EXT, w_ext), complex(39.24, w_ext), '2.60', offs=((-18, 0), (-22, 6), (18, 0)))
    dist_arrow(z, complex(N_EXT, e_ext), complex(39.24, e_ext), '2.60', offs=((-18, 0), (-22, 6), (-22, -6)))
    dist_arrow(z, complex(S_EXT, w_ext), complex(S_EXT, Y_DF), '2.56', offs=((0, -13), (0, -17), (0, 13)))
    for p, t in [(complex(24.6, 90.6), '11'), (centroid(LOT10), '10')]:
        z.free_text(p, t, fs=18, offsets=OFFS)
    for p, t in [(complex(40.5, 84.0), '道路　51'), (complex(30.0, 96.9), '9-1'), (complex(16.0, 86.0), '16-1'),
                 (complex(16.0, 74.0), '15-1'), (complex(30.0, 71.0), '12-1')]:
        z.free_text(p, t, fs=15, offsets=OFFS)
    save(fig, [z], 'H25_dai22mon_zu04_tatemono_zumen')


# ---- 図5：1階の求積図 ----
def zu05():
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
    save(fig, [z], 'H25_dai22mon_zu05_1kai_kyuuseki')


# ---- 図6：2階の誤り比較図 ----
def zu06():
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
    save(fig, zs, 'H25_dai22mon_zu06_2kai_ayamari_hikaku')


# ---- 図7：2階の求積図 ----
def zu07():
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
    save(fig, [z], 'H25_dai22mon_zu07_2kai_kyuuseki')


# ---- 図8：各階平面図の完成形（答案用紙の第4欄の左側の形） ----
def zu08():
    setup_font()
    fig = plt.figure(figsize=(18, 11.5), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図の完成形（答案用紙の第4欄の左側・縮尺1/250で描く内容）', fontsize=22, weight='bold', y=0.98)
    cell(fig, 0.04, 0.875, 0.16, 0.92, '家屋番号', fs=15)
    cell(fig, 0.16, 0.875, 0.40, 0.92)
    fig.text(0.70, 0.897, '各　階　平　面　図', ha='center', va='center', fontsize=20)
    cell(fig, 0.04, 0.83, 0.16, 0.875, '建物の所在', fs=15)
    cell(fig, 0.16, 0.83, 0.96, 0.875, 'C市D町一丁目11番地、10番地', fs=16, ha='left', color=INK)
    cell(fig, 0.04, 0.13, 0.96, 0.83, lw=1.8)
    cell(fig, 0.04, 0.06, 0.14, 0.13, '作　成　者', fs=15)
    cell(fig, 0.14, 0.06, 0.78, 0.13, '（略）　　　　　　　　　　　　（平成何年何月何日作成）', fs=15)
    cell(fig, 0.78, 0.06, 0.86, 0.13, '縮尺', fs=15)
    cell(fig, 0.86, 0.06, 0.96, 0.13, '1/250', fs=15)
    fig.text(0.5, 0.025, '壁の中心線の寸法（柱の両面被覆。別紙1の（注）5）で「1階」「2階」を書き分け、2階の図には1階の位置を点線で示す。'
             '求積の式と床面積を各階の横に書く', ha='center', va='center', fontsize=14)
    axes = [fig.add_axes([0.05, 0.16, 0.26, 0.62]), fig.add_axes([0.50, 0.16, 0.26, 0.62])]
    tables = ['1階\n8.19×10.92＝89.4348\n1.82×10.01＝18.2182\n0.91×8.19＝7.4529\n3.64×9.10＝33.1240\n'
              '計　148.2299\n床面積　148.22㎡',
              '2階\n10.92×10.92＝119.2464\n計　119.2464\n床面積　119.24㎡']
    zs = []
    f1 = [P(*v) for v in F1]
    for k, name in enumerate(['1階', '2階']):
        ax = axes[k]
        z = Zu(ax, fontsize=13)
        ax.set_title(name, fontsize=17, weight='bold')
        fit(ax, f1, margin=0.18, pad_aspect=True)
        if name == '1階':
            z.poly(f1, color=BLACK, lw=2.4)
            dims(z, f1, ['8.19', None, '2.73', None, '3.64', '9.10', '4.55', None, '10.01', '10.92'], fs=13, ref=P(7.0, 5.5))
            z.free_text(P(10.01, 10.01), '1.82', fs=13, offsets=((-14, 0), (-17, 0), (-20, 0)), rotation=90)
            z.free_text(P(8.19, 0.455), '0.91', fs=12, offsets=((-17, 0), (-20, 7), (-20, -7)))
            z.free_text(P(10.92, 0.455), '0.91', fs=12, offsets=((17, 0), (20, 7), (20, -7)))
        else:
            for a, b in [((3.64, 0), (0, 0)), ((0, 0), (0, 10.92)), ((0, 10.92), (3.64, 10.92)),
                         ((8.19, 0), (8.19, 0.91)), ((8.19, 0.91), (10.92, 0.91)), ((10.92, 0.91), (10.92, 0)),
                         ((14.56, 9.1), (10.01, 9.1)), ((10.01, 9.1), (10.01, 10.92))]:
                z.line(P(*a), P(*b), color=BLACK, lw=1.4, ls=':')
            f2 = [P(*v) for v in F2]
            z.poly(f2, color=BLACK, lw=2.4)
            dims(z, f2, ['10.92', '10.92', '10.92', '10.92'], fs=13, ref=P(9.1, 5.46))
        zs.append(z)
        fig.text(0.32 + 0.45 * k, 0.47, tables[k], ha='left', va='center', fontsize=14, linespacing=1.6)
    zs[1].north_arrow()
    save(fig, zs, 'H25_dai22mon_zu08_kakukai_heimenzu')


# ---- 図9：附属建物の増改築の前後比較図 ----
def zu09():
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
    save(fig, zs, 'H25_dai22mon_zu09_fuzoku_zoukaichiku')


# ---- 図10：本番で解く順番 ----
def zu10():
    """本番で解く順番。固定配置の図なので重なり検査の対象外（目視で確認）。"""
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
    path = os.path.join(OUT, 'H25_dai22mon_zu10_toku_junban.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図10: 解く順番（固定配置）\n  →', path)


if __name__ == '__main__':
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
    print('重なり合計:', len(PROBLEMS))
