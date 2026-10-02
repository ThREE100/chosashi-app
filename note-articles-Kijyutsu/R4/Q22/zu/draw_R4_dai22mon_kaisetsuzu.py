"""令和4年度 第22問（建物）の解説図8枚を、座標値・頂点座標から作図してPNGに書き出す。

`../prompt_R4_dai22mon_kaisetsuzu.md` の図1〜図8どおり（番号は記事の挿入順）。図3（建物図面）と図7（各階平面図）の完成形は、
答案用紙の第4欄の欄（家屋番号・建物の所在・申請人・作成者・縮尺）の形の枠の中に描く（欄の形は仮。プロンプトの図3を参照）。作図の共通部品は `tools/zu_helpers.py`。
敷地は〔座標値一覧表〕の (X＝北, Y＝東)。建物の平面は (東, 南)（原点＝建物全体の北西の角の壁の中心）で持ち、
zu_helpers の (北, 東) には P()・B_() で変換する。
建物図面の建物の位置は、筆界から外壁までの距離（〔調査図〕の（注）4）から、壁の中心線（壁厚0.15の半分＝0.075内側）、
車庫は柱の外面（外側の胴縁0.10＋被覆材0.05＝0.15内側）へずらして出す。
実行: python3 note-articles-Kijyutsu/R4/Q22/zu/draw_R4_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle  # noqa: E402

from zu_helpers import Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN, PURPLE  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []

# ---- 敷地（〔座標値一覧表〕。北はX軸の正方向＝〔調査図〕の（注）3） ----
A, B, C, D = complex(50, 50), complex(50, 78), complex(70, 80), complex(70, 50)
SITE = [A, B, C, D]
B_NORTH = complex(70, 78)   # 辺BCを真北向きの線だと思い込んだときのC点


def bc_y(x):
    """辺BC上で、X座標がxの点のY座標（Y＝78＋（X−50）×0.1）。"""
    return 78 + (x - 50) * 0.1


# ---- 建物の位置（筆界から外壁まで：南3.0・東2.0〈南東の角〉、車庫：北1.0・東2.0〈南東の角〉） ----
HALF = 0.075                       # 木造の壁厚0.15の半分（〔調査図〕の（注）7）
COVER = 0.15                       # 車庫の柱の外面から被覆材の外側まで（胴縁0.10＋被覆材0.05。図4）
S_EXT = 50 + 3.0                   # 主である建物の南の外壁 X＝53.00
E_EXT = bc_y(S_EXT) - 2.0          # 南東の角の東の外壁 Y＝76.30
N0 = S_EXT + HALF + 8.00           # 元の主である建物の北の壁の中心 X＝61.075
W0 = E_EXT - HALF - 18.00          # 元の附属建物の西の壁の中心 Y＝58.225
G_N_EXT = 70 - 1.0                 # 車庫の北の外壁 X＝69.00
G_N = G_N_EXT - COVER              # 車庫の北の柱の外面 X＝68.85
G_S = G_N - 4.00                   # 南の柱の外面 X＝64.85
G_S_EXT = G_S - COVER              # 南の外壁 X＝64.70
G_E_EXT = bc_y(G_S_EXT) - 2.0      # 南東の角の東の外壁 Y＝77.47
G_E = G_E_EXT - COVER              # 東の柱の外面 Y＝77.32
G_W = G_E - 5.00                   # 西の柱の外面 Y＝72.32
assert (round(N0, 3), round(W0, 3), round(G_N, 2), round(G_S_EXT, 2), round(G_E_EXT, 2), round(G_W, 2)) == \
    (61.075, 58.225, 68.85, 64.7, 77.47, 72.32)
assert round(bc_y(G_N_EXT) - G_E_EXT, 1) == 2.4   # 車庫の北東の角から辺BCまでは約2.4


def B_(e, s):
    """建物の平面の (東, 南) を zu_helpers の複素数 (北 + 東i) にする（建物図面用：敷地の座標に置く）。"""
    return complex(N0 - s, W0 + e)


def G_(e, s):
    """車庫の平面の (東, 南)（原点＝柱の外面の北西の角）を敷地の座標に置く。"""
    return complex(G_N - s, G_W + e)


def P(e, s):
    """求積図用：建物の北西の角を原点にした (東, 南) を (北 + 東i) にする。"""
    return complex(-s, e)


def rect(e0, s0, e1, s1, f=P):
    return [f(e0, s0), f(e1, s0), f(e1, s1), f(e0, s1)]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


def hatch(ax, pts, color=GRAY):
    ax.add_patch(MPoly([xy(p) for p in pts], closed=True, fill=False, hatch='///', edgecolor=color, lw=0, zorder=1))


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def dims(z, pts, labels, fs=14):
    """多角形の各辺に寸法（None は書かない）を外側に書く。"""
    c = centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs)


def dist_arrow(z, p, q, text, color=BLACK, fs=15, side=(8, 0)):
    """筆界から外壁までの距離の矢印（両向き）と数値。"""
    ax = z.ax
    ax.annotate('', xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='<|-|>', color=color, lw=1.6,
                                                         mutation_scale=12, shrinkA=0, shrinkB=0), zorder=6)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    return z.free_text(m, text, fs=fs, color=color,
                       offsets=(side, (-side[0], -side[1]), (0, 12), (0, -12), (side[0] * 2, side[1] * 2),
                                (-side[0] * 2, -side[1] * 2)),
                       ha='center', va='center')


# ---- 1階・2階・車庫の形（壁の中心線／柱の外面。(東, 南)） ----
F1 = [(0, 3), (5, 3), (5, 4), (9, 4), (9, 0), (18, 0), (18, 8), (0, 8)]
F2 = [(0, 3), (5, 3), (5, 8), (0, 8)]
GAR = [(0, 0), (5, 0), (5, 4), (0, 4)]
GAR_WRONG = [(-0.05, -0.05), (5.05, -0.05), (5.05, 4.05), (-0.05, 4.05)]
assert round(area([P(*v) for v in F1]), 2) == 113.00
assert round(area([P(*v) for v in F2]), 2) == 25.00
assert round(area([P(*v) for v in GAR]), 2) == 20.00
assert round(area([P(*v) for v in GAR_WRONG]), 2) == 20.91
assert round(area([B_(*v) for v in F1]), 2) == 113.00 and round(area([G_(*v) for v in GAR]), 2) == 20.00
# 建物・車庫は敷地（辺AB・BC・CD・DAの内側）に収まる＝所在は5番地3だけ
for p in [B_(*v) for v in F1] + [G_(*v) for v in GAR]:
    assert 50 < p.real < 70 and 50 < p.imag < bc_y(p.real)
# 図1の車庫の位置（建物の平面の座標に置き直したもの）
GAR_IN_PLAN = [(G_W - W0 + e, N0 - G_N + s) for e, s in GAR]


def zu01():
    fig, axes = new_figure('工事前と工事後：家屋番号5番3は1個の建物のまま',
                           '主である建物と符号1の附属建物は、もともと同じ登記記録（1個の建物）。間を増築してつながっても、合体の登記ではなく建物表題部変更登記',
                           w=16, h=10, ncols=2)
    fig.subplots_adjust(top=0.84)
    main, ann, ext = rect(9, 0, 18, 8), rect(0, 3, 5, 8), rect(5, 4, 9, 8)
    gar = [P(*v) for v in GAR_IN_PLAN]
    frame = rect(-1.2, -9.2, 20.4, 9.3)
    # 工事前
    z = Zu(axes[0], fontsize=14)
    z.poly(frame + [frame[0]], color=PURPLE, lw=1.6, ls='--', closed=False)   # 枠は区画扱いにしない（方位記号を置けるように）
    z.poly(main, color=BLACK, lw=2.2, fill=BLUE, alpha=0.18)
    z.poly(ann, color=BLACK, lw=2.2, fill=GREEN, alpha=0.2)
    z.free_text(P(13.5, 4.0), '主である建物\n事務所・平家建\n72.00㎡', fs=14)
    z.free_text(P(2.5, 5.5), '符号1\n倉庫\n2階建', fs=13)
    z.free_text(P(7.0, 6.0), '（空き地）', fs=12, color=GRAY)
    z.free_text(P(9.6, -9.2), '家屋番号5番3（1個の建物）', fs=15, color=PURPLE, offsets=((0, 12), (0, 18)))
    axes[0].set_title('工事前（登記記録）', fontsize=18, weight='bold', pad=12)
    fit(axes[0], frame, margin=0.06, extra=[xy(P(9.6, -11.5))], pad_aspect=True)
    # 工事後
    z2 = Zu(axes[1], fontsize=14)
    z2.poly(frame + [frame[0]], color=PURPLE, lw=1.6, ls='--', closed=False)
    z2.poly(main, color=BLUE, lw=0, fill=BLUE, alpha=0.18, check=False)
    z2.poly(ann, color=GREEN, lw=0, fill=GREEN, alpha=0.2, check=False)
    z2.poly(ext, color=ORANGE, lw=0, fill=ORANGE, alpha=0.45, check=False)
    z2.line(P(5, 4), P(5, 8), color=GRAY, lw=1.2, ls='--')
    z2.line(P(9, 4), P(9, 8), color=GRAY, lw=1.2, ls='--')
    z2.poly([P(*v) for v in F1], color=BLACK, lw=2.4)
    z2.poly(gar, color=BLACK, lw=2.2, fill=GRAY, alpha=0.3)
    z2.free_text(P(13.5, 4.0), '主である建物\n居宅・2階建', fs=14)
    z2.free_text(P(7.0, 6.0), '増築\n部分', fs=13, color=ORANGE, weight='bold')
    z2.free_text(P(2.5, 5.5), '元の\n符号1', fs=13)
    z2.free_text(centroid(gar), '車庫\n（新築）\n→符号2', fs=13)
    z2.free_text(P(9.6, -9.2), '家屋番号5番3のまま', fs=15, color=PURPLE, offsets=((0, 12), (0, 18)))
    axes[1].set_title('工事後（令和4年9月30日）', fontsize=18, weight='bold', pad=12)
    fit(axes[1], frame, margin=0.06, extra=[xy(P(9.6, -11.5))], pad_aspect=True)
    z2.north_arrow()
    save(fig, [z, z2], 'R4_dai22mon_zu01_kouji_zengo')


def zu02():
    fig, axes = new_figure('本件土地（敷地）の辺長確認図（作図チェック用）',
                           '東側の辺BCだけが斜め（B点とC点のYが78.00と80.00）。辺長は作図が正しいかを確かめるためのもので、建物図面には書かない',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=16)
    z.line(B, B_NORTH, color=GRAY, lw=1.4, ls='--')
    z.poly(SITE, color=BLACK, lw=2.6, fill=BLUE, alpha=0.12)
    for p in SITE:
        z.point(p)
    z.point(B_NORTH, color=GRAY, size=5)
    c = centroid(SITE)
    for p, n in zip(SITE, 'ABCD'):
        z.point_label(p, n, away=c, fs=19)
    z.edge_label(A, B, 'AB 28.0m', c, fs=16, outward=False)
    z.edge_label(B, C, 'BC 20.1m', c, fs=16)
    z.edge_label(C, D, 'CD 30.0m', c, fs=16, outward=False)
    z.edge_label(D, A, 'DA 20.0m', c, fs=16, outward=False)
    z.callout(C, 'C点（70.00, 80.00）\nB点のYは78.00\n→ 辺BCは北へ行くほど東へ開く', dirs=(-10, 0, 10), dists=(70, 95, 120),
              fs=15, color=RED)
    z.callout(complex(56, 78), '点線＝B点から真北の線', dirs=(180, 195, 165), dists=(70, 90, 110), fs=14, color=GRAY)
    OFFS = ((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0))
    for p, t in [(complex(48.2, 64), '道路（102）'), (complex(60, 86.5), '道路\n（5-4）'), (complex(71.8, 65), '5-2'),
                 (complex(60, 46.8), '5-1')]:
        z.free_text(p, t, fs=15, color=GRAY, offsets=OFFS)
    z.free_text(complex(62, 62), '本件土地（5番3）', fs=17)
    fit(ax, SITE, margin=0.12, extra=[xy(complex(46, 44)), xy(complex(74, 96))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R4_dai22mon_zu02_shikichi_henchou')


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.01
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


INK = '#1a3a8f'   # 記入（濃い青）


def zu03():
    """建物図面の完成形（答案用紙の第4欄の右側〈建物図面〉の枠の中。塗り分けはしない）。"""
    setup_font()
    fig = plt.figure(figsize=(16, 14), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面の完成形（答案用紙の第4欄・縮尺1/500で描く内容）', fontsize=22, weight='bold', y=0.985)
    # 答案用紙の欄（家屋番号・建物の所在・申請人・縮尺）。欄の形は仮（プロンプトの図3を参照）
    cell(fig, 0.06, 0.885, 0.20, 0.935, '家屋番号', fs=15)
    cell(fig, 0.20, 0.885, 0.46, 0.935, '5番3', fs=16, ha='left', color=INK)
    fig.text(0.70, 0.910, '建　物　図　面', ha='center', va='center', fontsize=20)
    cell(fig, 0.06, 0.835, 0.20, 0.885, '建物の所在', fs=15)
    cell(fig, 0.20, 0.835, 0.94, 0.885, 'A市B町一丁目5番地3', fs=16, ha='left', color=INK)
    cell(fig, 0.06, 0.085, 0.94, 0.835, lw=1.8)
    cell(fig, 0.06, 0.035, 0.20, 0.085, '申　請　人', fs=15)
    cell(fig, 0.20, 0.035, 0.74, 0.085, '（略）', fs=15)
    cell(fig, 0.74, 0.035, 0.83, 0.085, '縮尺', fs=15)
    cell(fig, 0.83, 0.035, 0.94, 0.085, '1/500', fs=15)
    ax = fig.add_axes([0.08, 0.10, 0.84, 0.72])
    z = Zu(ax, fontsize=15)
    fit(ax, SITE, margin=0.1, extra=[xy(complex(46, 44)), xy(complex(74, 90))], pad_aspect=True)
    z.north_arrow()
    z.poly(SITE, color=BLACK, lw=2.2)
    bldg = [B_(*v) for v in F1]
    gar = [G_(*v) for v in GAR]
    z.poly(bldg, color=BLACK, lw=2.4)
    z.poly(gar, color=BLACK, lw=2.2)
    assert round(area(bldg), 2) == 113.00 and round(area(gar), 2) == 20.00
    # 主である建物：南の2か所（南西の角・南東の角）は辺ABまで、南東の角から辺BCまで（東西方向）
    w_ext = W0 - HALF
    dist_arrow(z, complex(S_EXT, w_ext), complex(50, w_ext), '3.0', side=(-16, 0))
    dist_arrow(z, complex(S_EXT, E_EXT), complex(50, E_EXT), '3.0', side=(-16, 0))
    dist_arrow(z, complex(S_EXT, E_EXT), complex(S_EXT, bc_y(S_EXT)), '2.0', side=(0, 14))
    # 車庫：北の2か所は辺CDまで、南東の角から辺BCまで
    gw_ext = G_W - COVER
    dist_arrow(z, complex(G_N_EXT, gw_ext), complex(70, gw_ext), '1.0', side=(-14, 28))   # 寸法が短いので筆界の北に書く
    dist_arrow(z, complex(G_N_EXT, G_E_EXT), complex(70, G_E_EXT), '1.0', side=(-14, 28))
    dist_arrow(z, complex(G_S_EXT, G_E_EXT), complex(G_S_EXT, bc_y(G_S_EXT)), '2.0', side=(0, -14))
    circ = dict(bbox=dict(boxstyle='circle,pad=0.25', fc='white', ec=BLACK, lw=1.2))
    z.free_text(B_(13.5, 4.0), '主', fs=16, **circ)
    z.free_text(centroid(gar), '附2', fs=14, bbox=dict(boxstyle='round,pad=0.25', fc='white', ec=BLACK, lw=1.2))
    OFFS = ((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0))
    z.free_text(complex(66, 58), '5-3', fs=17, offsets=OFFS)
    for p, t in [(complex(71.8, 65), '5-2'), (complex(60, 46.8), '5-1'), (complex(60, 82.8), '5-4\n（道路）'),
                 (complex(48.0, 64), '102（道路）')]:
        z.free_text(p, t, fs=15, offsets=OFFS)
    z.free_text(complex(47.2, 86), '（単位：m）', fs=13, offsets=OFFS)
    save(fig, [z], 'R4_dai22mon_zu03_tatemono_zumen')


def zu04():
    fig, axes = new_figure('1階の床面積求積図（壁の中心線）',
                           '西から 5.00×5.00＝25.00（元の附属建物）＋ 4.00×4.00＝16.00（増築部分）＋ 9.00×8.00＝72.00（元の主である建物）＝ 113.00㎡',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    r1, r2, r3 = rect(0, 3, 5, 8), rect(5, 4, 9, 8), rect(9, 0, 18, 8)
    z.poly(r1, color=GREEN, lw=0, fill=GREEN, alpha=0.25, check=False)
    z.poly(r2, color=ORANGE, lw=0, fill=ORANGE, alpha=0.4, check=False)
    z.poly(r3, color=BLUE, lw=0, fill=BLUE, alpha=0.2, check=False)
    z.line(P(5, 4), P(5, 8), color=GRAY, lw=1.2, ls='--')
    z.line(P(9, 4), P(9, 8), color=GRAY, lw=1.2, ls='--')
    f1 = [P(*v) for v in F1]
    z.poly(f1, color=BLACK, lw=2.4)
    dims(z, f1, ['5.00m', None, '4.00m', '4.00m', '9.00m', '8.00m', '18.00m', '5.00m'])
    z.free_text(P(5, 3.5), '1.00m', fs=14, offsets=((-28, 0), (-32, 6), (-28, -6)))   # 短い段差は横に水平に書く
    z.free_text(P(2.5, 5.5), '元の附属建物\n5.00×5.00\n＝25.00', fs=14)
    z.free_text(P(7.0, 6.1), '増築部分\n4.00×4.00\n＝16.00', fs=14)
    z.free_text(P(13.5, 4.0), '元の主である建物\n9.00×8.00\n＝72.00', fs=16)
    z.point(P(0, 3), size=9, color=BLACK)
    z.callout(P(0, 3), '〇印（2階と重なる部分）', dirs=(150, 170, 130), fs=13)
    z.free_text(P(9, 10.2), '1階 床面積：113.00㎡', fs=18, weight='bold')
    fit(ax, f1, margin=0.18, extra=[xy(P(9, 11)), xy(P(-6, -1.5))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R4_dai22mon_zu04_1kai_kyuuseki')


def zu05():
    fig, axes = new_figure('2階の床面積求積図（1階の位置を点線で重ねる）',
                           '2階は元の附属建物の真上の5.00×5.00＝25.00㎡。1階の位置の表示は省略できない（問題文の注4のただし書）ので、1階の残りを点線で示す',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    f2 = [P(*v) for v in F2]
    z.poly(f2, color=BLACK, lw=2.6, fill=BLUE, alpha=0.25)
    rest = [P(5, 3), P(5, 4), P(9, 4), P(9, 0), P(18, 0), P(18, 8), P(5, 8)]
    z.poly(rest, color=BLACK, lw=1.6, ls=':', closed=False)
    dims(z, f2, ['5.00m', '5.00m', '5.00m', '5.00m'])
    z.free_text(P(2.5, 5.5), '2階\n5.00×5.00\n＝25.00', fs=16)
    z.free_text(P(12.5, 4.0), '点線＝1階の位置\n（2階はない）', fs=15, color=GRAY)
    z.point(P(0, 3), size=9, color=BLACK)
    z.callout(P(0, 3), '〇印（1階と重なる部分）', dirs=(150, 170, 130), fs=13)
    z.free_text(P(9, 10.2), '2階 床面積：25.00㎡', fs=18, weight='bold')
    fit(ax, [P(*v) for v in F1], margin=0.18, extra=[xy(P(9, 11)), xy(P(-6, -1.5))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R4_dai22mon_zu05_2kai_kyuuseki')


def zu06():
    fig, axes = new_figure('車庫（符号2）の床面積：胴縁の中心ではなく、鉄骨柱の外面で測る',
                           '図3の5.10・4.10は胴縁の中心からの寸法（〔調査図〕の（注）8）。柱の外側は胴縁と被覆材で覆われている（同（注）9）ので、\n胴縁の中心から0.05ずつ内側の柱の外面で測る：5.10×4.10＝20.91ではなく、5.00×4.00＝20.00㎡',
                           w=16, h=9.5, ncols=3, width_ratios=[0.8, 1.4, 0.8])
    fig.subplots_adjust(top=0.84, wspace=0.12)
    # 左：誤り
    z = Zu(axes[0], fontsize=14)
    wrong = [P(*v) for v in GAR_WRONG]
    z.poly(wrong, color=RED, lw=2.2, fill=RED, alpha=0.15)
    dims(z, wrong, ['5.10m', '4.10m', None, None])
    z.free_text(P(2.5, 2.0), '5.10×4.10\n＝20.91㎡', fs=16, color=RED)
    axes[0].set_title('誤り：胴縁の中心で測る（藍子）', fontsize=16, weight='bold', color=RED, pad=12)
    fit(axes[0], wrong, margin=0.3, pad_aspect=True)
    # 中央：図4の角（車庫の南西の角）の拡大。(東, 南) で、柱の西の外面が東0、南の外面が南4.00
    z2 = Zu(axes[1], fontsize=12)
    ax2 = axes[1]
    cov = [P(-0.15, 3.35), P(-0.10, 3.35), P(-0.10, 4.10), P(0.60, 4.10), P(0.60, 4.15), P(-0.15, 4.15)]
    dob = [P(-0.10, 3.35), P(0.0, 3.35), P(0.0, 4.0), P(0.60, 4.0), P(0.60, 4.10), P(-0.10, 4.10)]
    z2.poly(cov, color=BLACK, lw=1.2, check=False)
    hatch(ax2, cov, color=GRAY)
    z2.poly(dob, color=BLACK, lw=1.2, fill=ORANGE, alpha=0.25, check=False)
    z2.line(P(-0.05, 3.35), P(-0.05, 4.05), color=PURPLE, lw=1.4, ls='-.')
    z2.line(P(-0.05, 4.05), P(0.60, 4.05), color=PURPLE, lw=1.4, ls='-.')
    # 鉄骨柱（H形）：フランジは東0〜0.20、南4.00と3.60。ウェブは東0.10。柱の外形を薄い灰色で塗る
    z2.poly(rect(0.0, 3.6, 0.20, 4.0), color=GRAY, lw=0, fill=GRAY, alpha=0.18, check=False)
    for s_ in (4.0, 3.6):
        z2.line(P(0.0, s_), P(0.20, s_), color=BLACK, lw=3.0)
    z2.line(P(0.10, 3.6), P(0.10, 4.0), color=BLACK, lw=3.0)
    z2.line(P(0.0, 3.35), P(0.0, 4.0), color=GREEN, lw=4.0)
    z2.line(P(0.0, 4.0), P(0.60, 4.0), color=GREEN, lw=4.0)
    z2.callout(P(-0.125, 3.45), '被覆材 0.05', dirs=(180, 165, 195), dists=(45, 60, 75), fs=12)
    z2.callout(P(0.45, 4.05), '胴縁 0.10\n（一点鎖線＝胴縁の中心）', dirs=(-90, -75, -105), dists=(30, 40, 50), fs=12,
               color=PURPLE)
    z2.callout(P(-0.025, 3.8), '胴縁の中心から柱の外面まで 0.05', dirs=(180, 195, 165), dists=(45, 60, 75), fs=12, color=RED)
    z2.callout(P(0.40, 4.0), '柱の外面＝床面積の区画', dirs=(60, 75, 45), dists=(45, 60, 80), fs=13, color=GREEN)
    z2.free_text(P(0.30, 3.62), '鉄骨柱（H形）', fs=12, ha='left', offsets=((4, 0), (4, 10), (4, -10)))
    axes[1].set_title('図4の角（南西）の拡大', fontsize=16, weight='bold', pad=12)
    fit(axes[1], [P(-0.15, 3.3), P(0.6, 4.2)], margin=0.05, extra=[xy(P(-0.95, 3.2)), xy(P(0.75, 4.6))],
        pad_aspect=True)
    # 右：正解
    z3 = Zu(axes[2], fontsize=14)
    ok = [P(*v) for v in GAR]
    z3.poly(wrong, color=GRAY, lw=1.2, ls=':', check=False)
    z3.poly(ok, color=GREEN, lw=2.4, fill=GREEN, alpha=0.18)
    dims(z3, ok, ['5.00m', '4.00m', None, None])
    z3.free_text(P(2.5, 2.0), '5.00×4.00\n＝20.00㎡', fs=16, color=GREEN)
    axes[2].set_title('正解：柱の外面で測る', fontsize=16, weight='bold', color=GREEN, pad=12)
    fit(axes[2], wrong, margin=0.3, pad_aspect=True)
    assert round(5.10 - 2 * 0.05, 2) == 5.00 and round(4.10 - 2 * 0.05, 2) == 4.00
    assert round(5.10 * 4.10 - 5.00 * 4.00, 2) == 0.91
    save(fig, [z, z2, z3], 'R4_dai22mon_zu06_shako_ayamari_hikaku')


def zu07():
    """各階平面図の完成形（答案用紙の第4欄の左側〈各階平面図〉の枠の中。求積図とちがい塗り分けはしない）。
    主である建物の1階は書かなくてよい（問題文の注4）が、2階の図の1階の位置（点線）は省略できない（同ただし書）。"""
    setup_font()
    fig = plt.figure(figsize=(18, 11), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図の完成形（答案用紙の第4欄・縮尺1/250で描く内容）', fontsize=22, weight='bold', y=0.975)
    fig.text(0.5, 0.905, '各　階　平　面　図', ha='center', va='center', fontsize=20)
    cell(fig, 0.04, 0.13, 0.96, 0.88, lw=1.8)
    cell(fig, 0.04, 0.06, 0.14, 0.13, '作　成　者', fs=15)
    cell(fig, 0.14, 0.06, 0.78, 0.13, '（略）　　　　　　　　　　　　（令和4年○月○日作成）', fs=15)
    cell(fig, 0.78, 0.06, 0.86, 0.13, '縮尺', fs=15)
    cell(fig, 0.86, 0.06, 0.96, 0.13, '1/250', fs=15)
    fig.text(0.5, 0.025, '主である建物の1階の形と求積表は書かない（問題文の注4）。2階の図には1階の位置を点線で示す（同ただし書）。'
             '車庫は柱の外面で測った5.00×4.00', ha='center', va='center', fontsize=14)
    ax1 = fig.add_axes([0.05, 0.17, 0.42, 0.62])
    ax2 = fig.add_axes([0.66, 0.40, 0.14, 0.36])
    # 主である建物 2階
    z = Zu(ax1, fontsize=13)
    ax1.set_title('主である建物　2階', fontsize=17, weight='bold')
    fit(ax1, [P(*v) for v in F1], margin=0.14, pad_aspect=True)
    rest = [P(5, 3), P(5, 4), P(9, 4), P(9, 0), P(18, 0), P(18, 8), P(5, 8)]
    z.poly(rest, color=BLACK, lw=1.4, ls=':', closed=False)        # 1階の位置（点線）
    f2 = [P(*v) for v in F2]
    z.poly(f2, color=BLACK, lw=2.4)
    dims(z, f2, ['5.00', '5.00', '5.00', '5.00'], fs=13)
    z.free_text(P(13.5, 4.0), '点線＝1階の位置', fs=13, color=GRAY)
    z.north_arrow()
    fig.text(0.48, 0.47, '主である建物　2階\n5.00×5.00＝25.0000\n計　25.0000\n床面積　25.00㎡',
             ha='left', va='center', fontsize=15, linespacing=1.6)
    # 附属建物 符号2（車庫）
    z2 = Zu(ax2, fontsize=13)
    ax2.set_title('附属建物　符号2', fontsize=17, weight='bold')
    gar = [P(*v) for v in GAR]
    fit(ax2, gar, margin=0.3, pad_aspect=True)
    z2.poly(gar, color=BLACK, lw=2.4)
    dims(z2, gar, ['5.00', '4.00', '5.00', '4.00'], fs=13)
    fig.text(0.81, 0.58, '附属建物　符号2\n5.00×4.00＝20.0000\n計　20.0000\n床面積　20.00㎡',
             ha='left', va='center', fontsize=15, linespacing=1.6)
    assert round(area(f2), 4) == 25.00 and round(area(gar), 4) == 20.00
    save(fig, [z, z2], 'R4_dai22mon_zu07_kakukai_heimenzu')


def zu08():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    setup_font()
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　計算のいらない欄を先に埋めて、第4欄の作図に時間を残す', fontsize=23, weight='bold', y=0.965)
    ax = fig.add_axes([0.02, 0.22, 0.96, 0.68])
    ax.set_xlim(0, 100)
    ax.set_ylim(14, 92)
    ax.axis('off')
    steps = [
        ('①', '前文・問題文の注・\n問1〜問4', '申請書は1枚\n→車庫は附属建物', BLUE),
        ('②', '問2・問3\n（第2欄・第3欄）', '準則と民法の\n知識だけで埋まる', BLUE),
        ('③', '調査図・事実関係・\n登記記録', '〔調査図〕の（注）\n7・8・9を図と照らす', BLUE),
        ('④', '申請書の\n計算のいらない欄', '目的・添付書類・\n申請人・原因・符号', GREEN),
        ('⑤', '床面積', '113.00・25.00・\n20.00（柱の外面）', ORANGE),
        ('⑥', '第4欄の作図', '各階平面図と\n建物図面', RED),
        ('⑦', '見直し', '①②③・符号2・\n権原の漢字', GRAY),
    ]
    w, h, gap = 12.4, 44, 1.8
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 30), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 30 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
        ax.text(x + w / 2, 30 + h / 2 - 4, t, ha='center', va='center', fontsize=14)
        ax.text(x + w / 2, 26, ran, ha='center', va='top', fontsize=13, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.1, 52), xytext=(x + w + 0.1, 52),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    x6 = 1 + 5 * (w + gap)
    ax.text(x6 + w / 2, 84, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.text(1 + 1.5 * (w + gap) + w / 2, 84, '計算なしで先に書ける（①〜④）', ha='center', fontsize=15, color=BLUE, weight='bold')
    fig.text(0.5, 0.115, '作図の前のメモ：建物の北西の角を原点に、寸法線を足した累計　東西 0・5・9・18　／　南北 0・3・4・8',
             ha='center', va='center', fontsize=16, weight='bold',
             bbox=dict(boxstyle='round,pad=0.5', fc='#fff8e6', ec=ORANGE, lw=1.6))
    fig.text(0.5, 0.04, '申請書で計算がいるのは主である建物の1階113.00・2階25.00と車庫20.00の3か所だけ。'
             '建物図面は座標で台形の敷地を描いてから、南東の角から測った2.0で建物と車庫を置く',
             ha='center', va='center', fontsize=14)
    path = os.path.join(OUT, 'R4_dai22mon_zu08_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図8: 解く順番（固定配置）\n  →', path)


if __name__ == '__main__':
    zu01()
    zu02()
    zu03()
    zu04()
    zu05()
    zu06()
    zu07()
    zu08()
    print('重なり合計:', len(PROBLEMS))
