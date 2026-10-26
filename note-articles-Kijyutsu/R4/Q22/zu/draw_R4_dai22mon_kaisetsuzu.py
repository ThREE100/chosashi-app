"""令和4年度 第22問（建物）の解説図8枚を、座標値・頂点座標から作図してPNGに書き出す。

`../prompt_R4_dai22mon_kaisetsuzu.md` の図1〜図8どおり（番号は記事の挿入順）。図3（建物図面）と図7（各階平面図）の完成形は、
答案用紙の第4欄の欄（家屋番号・建物の所在・申請人・作成者・縮尺）の形の枠の中に描く（欄の形は試験の答案用紙 `../touan_youshi/` で確かめた。プロンプトの図3を参照）。作図の共通部品は `tools/zu_helpers.py`。
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
from matplotlib.patches import Polygon as MPoly, Rectangle, FancyBboxPatch  # noqa: E402
from matplotlib.colors import to_rgba  # noqa: E402

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


def dist_arrow(z, p, q, text, color=BLACK, fs=15, side=(8, 0), text_pos=None, ha='center'):
    """筆界から外壁までの距離の矢印（両向き）と数値。"""
    ax = z.ax
    ax.annotate('', xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='<|-|>', color=color, lw=1.6,
                                                         mutation_scale=12, shrinkA=0, shrinkB=0), zorder=6)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2 if text_pos is None else text_pos
    if text_pos is not None:
        return z.free_text(m, text, fs=fs, color=color, offsets=((6, 0), (6, 8), (6, -8), (6, 16), (6, -16)), ha='left', va='center')
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


# ======================================================================
# 固定配置の図（座標を使わない整理図）の部品。R7/Q22の作図スクリプトと同じ形。
# 横軸・縦軸とも 0〜100 の作業座標。重なり検査は check_fixed で図の全部の文字を調べる。
# ======================================================================
def fixed_figure(title, w=16, h=10, rect=(0.02, 0.04, 0.96, 0.86)):
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
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    texts = list(fig.texts)
    if fig._suptitle is not None and fig._suptitle not in texts:
        texts.append(fig._suptitle)
    for a in fig.axes:
        texts += list(a.texts) + [a.title]
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
            probs.append(f'{name} 図の外へのはみ出し: {t.get_text()!r}')
        for t2, bb2 in zip(texts[i + 1:], bbs[i + 1:]):
            if bb.overlaps(bb2):
                probs.append(f'{name} 文字どうし: {t.get_text()!r} と {t2.get_text()!r}')
    print(f'[重なり検査] {name}（固定配置）: ' + ('問題なし' if not probs else f'{len(probs)}件'))
    for q in probs:
        print('   ', q)
    PROBLEMS.extend(probs)


def save_fixed(fig, name):
    check_fixed(fig, name)
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def rbox(ax, x, y, w, h, col, alpha=0.12, lw=1.8, ls='-'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.5', facecolor=to_rgba(col, alpha) if alpha else 'none',
                                edgecolor=col, lw=lw, ls=ls))


def vline(fig, x, y0=0.10, y1=0.86):
    fig.add_artist(plt.Line2D([x, x], [y0, y1], transform=fig.transFigure, color=GRAY, lw=1.2))


def card_figure(name, title, cols, bottom, w=17, h=9.5, top=84.0, line_step=8.6, fs=15):
    """左右（2〜3列）に並べる固定配置の比較カード。cols: [(見出し, 色, [行...])]。行の先頭が '*' なら太字・色つき。"""
    fig, ax = fixed_figure(title, w=w, h=h, rect=(0.02, 0.11, 0.96, 0.77))
    n = len(cols)
    cw = (98.0 - 2.0 * (n - 1)) / n
    for i, (head, col, lines) in enumerate(cols):
        x0 = 1.0 + i * (cw + 2.0)
        rbox(ax, x0, 4, cw, 80, col, alpha=0.08)
        ax.text(x0 + cw / 2, 92, head, ha='center', va='center', fontsize=fs + 3, weight='bold', color=col, linespacing=1.35)
        y = top - 4
        for ln in lines:
            bold = ln.startswith('*')
            t = ln[1:] if bold else ln
            k = t.count('\n') + 1
            if not t:
                y -= 3.5
                continue
            ax.text(x0 + cw / 2, y, t, ha='center', va='top', fontsize=fs, weight='bold' if bold else 'normal',
                    color=col if bold else BLACK, linespacing=1.4)
            y -= line_step * k * 0.78 + 2.4
    if n == 2:
        vline(fig, 0.5, 0.10, 0.90)
    for k, t in enumerate(bottom):
        fig.text(0.5, 0.065 - 0.04 * k, t, ha='center', va='center', fontsize=15)
    save_fixed(fig, name)


def table_box(ax, x0, ytop, colw, headers, rows, fs=11.5, line_h=3.1, pad=2.2, col_colors=None, head_h=5.5):
    """固定配置の表。rows: [(セル, ...)]。セルの改行は \\n。列の色 col_colors[i] があれば、その列の文字を太字・色つきにする。戻り値は表の下端。"""
    xs = [x0]
    for w in colw:
        xs.append(xs[-1] + w)
    ax.add_patch(Rectangle((x0, ytop - head_h), xs[-1] - x0, head_h, facecolor=to_rgba(GRAY, 0.18), edgecolor=BLACK, lw=1.4))
    for i, h in enumerate(headers):
        ax.text(xs[i] + colw[i] / 2, ytop - head_h / 2, h, ha='center', va='center', fontsize=fs + 1, weight='bold')
    y = ytop - head_h
    for r in rows:
        k = max(c.count('\n') + 1 for c in r)
        rh = k * line_h + pad
        ax.add_patch(Rectangle((x0, y - rh), xs[-1] - x0, rh, fill=False, edgecolor=BLACK, lw=1.0))
        for i, c in enumerate(r):
            colr = col_colors[i] if col_colors and col_colors[i] else None
            ax.text(xs[i] + 0.8, y - rh / 2, c, ha='left', va='center', fontsize=fs, linespacing=1.3,
                    color=colr or BLACK, weight='bold' if colr else 'normal')
        for xv in xs[1:-1]:
            ax.plot([xv, xv], [y, y - rh], color=BLACK, lw=1.0)
        y -= rh
    return y


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
    save(fig, [z, z2], 'R4_dai22mon_zu02_kouji_zengo')


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
    save(fig, [z], 'R4_dai22mon_zu04_shikichi_henchou')


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.01
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


INK = '#1a3a8f'   # 記入（濃い青）


def scale_cell(fig, x0, y0, x1, y1, denom, fs=15):
    """答案用紙の縮尺の欄の印刷（分子の1と分母を斜線で区切った分数の形）。"""
    cell(fig, x0, y0, x1, y1)
    w, h = x1 - x0, y1 - y0
    fig.add_artist(plt.Line2D([x0 + 0.22 * w, x0 + 0.78 * w], [y0 + 0.15 * h, y0 + 0.85 * h],
                              transform=fig.transFigure, color=BLACK, lw=1.2))
    fig.text(x0 + 0.40 * w, y0 + 0.74 * h, '1', ha='center', va='center', fontsize=fs)
    fig.text(x0 + 0.66 * w, y0 + 0.26 * h, str(denom), ha='center', va='center', fontsize=fs)


def zu03():
    """建物図面の完成形（答案用紙の第4欄の右側〈建物図面〉の枠の中。塗り分けはしない）。"""
    setup_font()
    fig = plt.figure(figsize=(16, 14), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面の完成形（答案用紙の第4欄・縮尺1/500で描く内容）', fontsize=22, weight='bold', y=0.985)
    # 答案用紙の欄（家屋番号・建物の所在・申請人・縮尺）。試験の答案用紙（../touan_youshi/）の第4欄の右半分の形：
    # 右上に家屋番号の欄（その右に「建物図面」の題）、枠の上端に建物の所在の欄、枠の下に申請人「（略）」と縮尺「1/500」（印刷）
    cell(fig, 0.06, 0.885, 0.20, 0.935, '家屋番号', fs=15)
    cell(fig, 0.20, 0.885, 0.46, 0.935, '5番3', fs=16, ha='left', color=INK)
    fig.text(0.70, 0.910, '建　物　図　面', ha='center', va='center', fontsize=20)
    cell(fig, 0.06, 0.835, 0.20, 0.885, '建物の所在', fs=15)
    cell(fig, 0.20, 0.835, 0.94, 0.885, 'A市B町一丁目5番地3', fs=16, ha='left', color=INK)
    cell(fig, 0.06, 0.085, 0.94, 0.835, lw=1.8)
    cell(fig, 0.06, 0.035, 0.20, 0.085, '申　請　人', fs=15)
    cell(fig, 0.20, 0.035, 0.74, 0.085, '（略）', fs=15)
    cell(fig, 0.74, 0.035, 0.83, 0.085, '縮尺', fs=15)
    scale_cell(fig, 0.83, 0.035, 0.94, 0.085, 500)
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
    save(fig, [z], 'R4_dai22mon_zu07_tatemono_zumen')


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
    save(fig, [z], 'R4_dai22mon_zu10_1kai_kyuuseki')


def zu05():
    """2階の床面積求積図。判断は「2階は元の附属建物の真上の5.00×5.00」だけ（1階の位置の点線は図12に分ける）。"""
    fig, axes = new_figure('2階の床面積求積図（元の附属建物の真上）',
                           '2階は元の附属建物の1階の真上にある5.00×5.00＝25.00㎡。図2の〇印は各階の重なる部分を示す（〔調査図〕の（注）6）',
                           w=16, h=9)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    f2 = [P(*v) for v in F2]
    z.poly(f2, color=BLACK, lw=2.6, fill=BLUE, alpha=0.25)
    dims(z, f2, ['5.00m', '5.00m', '5.00m', '5.00m'])
    z.free_text(P(2.5, 5.5), '2階\n5.00×5.00\n＝25.00', fs=16)
    z.point(P(0, 3), size=9, color=BLACK)
    z.callout(P(0, 3), '〇印（1階と重なる部分）', dirs=(150, 170, 130), fs=13)
    z.free_text(P(2.5, 11.0), '2階 床面積：25.00㎡', fs=18, weight='bold')
    fit(ax, f2, margin=0.5, extra=[xy(P(2.5, 11.8)), xy(P(-5, -1.5))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R4_dai22mon_zu11_2kai_kyuuseki')


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
    save(fig, [z, z2, z3], 'R4_dai22mon_zu13_shako_ayamari_hikaku')


def zu07():
    """各階平面図の完成形（答案用紙の第4欄の左側〈各階平面図〉の枠の中。求積図とちがい塗り分けはしない）。
    主である建物の1階は書かなくてよい（問題文の注4）が、2階の図の1階の位置（点線）は省略できない（同ただし書）。"""
    setup_font()
    fig = plt.figure(figsize=(18, 11), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図の完成形（答案用紙の第4欄・縮尺1/250で描く内容）', fontsize=22, weight='bold', y=0.975)
    fig.text(0.5, 0.905, '各　階　平　面　図', ha='center', va='center', fontsize=20)
    cell(fig, 0.04, 0.13, 0.96, 0.88, lw=1.8)
    # 答案用紙の各階平面図の欄の左上の印刷（試験の答案用紙 ../touan_youshi/ のとおり。主である建物の1階は（略））
    fig.text(0.075, 0.845, '主である建物', ha='left', va='center', fontsize=15)
    fig.text(0.078, 0.805, '1階', ha='left', va='center', fontsize=15)
    fig.text(0.24, 0.775, '（略）', ha='center', va='center', fontsize=15)
    cell(fig, 0.04, 0.06, 0.14, 0.13, '作　成　者', fs=15)
    cell(fig, 0.14, 0.06, 0.78, 0.13, '（略）　　　　　　　　　　　　（令和4年○月○日作成）', fs=15)
    cell(fig, 0.78, 0.06, 0.86, 0.13, '縮尺', fs=15)
    scale_cell(fig, 0.86, 0.06, 0.96, 0.13, 250)
    fig.text(0.5, 0.025, '左上の「主である建物　1階　（略）」は答案用紙の印刷（1階の形と求積表は書かない。問題文の注4）。'
             '2階の図には1階の位置を点線で示す（同ただし書）。車庫は柱の外面で測った5.00×4.00', ha='center', va='center', fontsize=14)
    ax1 = fig.add_axes([0.05, 0.16, 0.42, 0.55])
    ax2 = fig.add_axes([0.66, 0.36, 0.14, 0.34])
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
    fig.text(0.48, 0.43, '主である建物　2階\n5.00×5.00＝25.0000\n計　25.0000\n床面積　25.00㎡',
             ha='left', va='center', fontsize=15, linespacing=1.6)
    # 附属建物 符号2（車庫）
    z2 = Zu(ax2, fontsize=13)
    ax2.set_title('附属建物　符号2', fontsize=17, weight='bold')
    gar = [P(*v) for v in GAR]
    fit(ax2, gar, margin=0.3, pad_aspect=True)
    z2.poly(gar, color=BLACK, lw=2.4)
    dims(z2, gar, ['5.00', '4.00', '5.00', '4.00'], fs=13)
    fig.text(0.81, 0.53, '附属建物　符号2\n5.00×4.00＝20.0000\n計　20.0000\n床面積　20.00㎡',
             ha='left', va='center', fontsize=15, linespacing=1.6)
    assert round(area(f2), 4) == 25.00 and round(area(gar), 4) == 20.00
    save(fig, [z, z2], 'R4_dai22mon_zu15_kakukai_heimenzu')


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
    path = os.path.join(OUT, 'R4_dai22mon_zu22_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図8: 解く順番（固定配置）\n  →', path)


# ======================================================================
# 2026-10-26 品質チェック（qa-checklist-kijutsu.md 6-2）で足した図。番号は記事の挿入順（PNG名）
# ======================================================================
def zu_jikeiretsu():
    """図1：時系列。9月30日の工事完了から申請（10月17日）まで、期限は9月30日の翌日から1月以内＝10月31日。"""
    import datetime as dt
    d0 = dt.date(2022, 9, 25)

    def X(m, d):
        return 5 + (dt.date(2022, m, d) - d0).days * 90 / 42
    fig, ax = fixed_figure('時系列　9月30日の工事完了から、申請（10月17日）まで', w=16, h=7.6, rect=(0.02, 0.15, 0.96, 0.72))
    y0 = 40
    ax.plot([X(9, 25), X(11, 5)], [y0, y0], color=GRAY, lw=2)
    ax.add_patch(Rectangle((X(9, 30), y0 - 3), X(10, 31) - X(9, 30), 6, facecolor=to_rgba(RED, 0.2), edgecolor='none'))
    ax.text((X(9, 30) + X(10, 31)) / 2, y0 + 7, '9月30日の翌日から1月以内', ha='center', va='center', fontsize=14, color=RED)
    ax.text(2.0, 94, '令和4年9月30日', ha='left', va='center', fontsize=17, weight='bold', color=BLUE)
    for k, t in enumerate(['本件増築工事が完了し、本件建物が令子さんに引き渡される', '本件新築工事（車庫）が完了し、令子さんに引き渡される',
                           '工事代金を支払い、登記に必要な書類を受け取る']):
        ax.text(2.0, 85 - 8.5 * k, t, ha='left', va='center', fontsize=14)
    ax.plot([X(9, 30)] * 2, [y0, 59], color=BLUE, lw=2)
    ax.plot([X(9, 30)], [y0], 'o', color=BLUE, ms=11, zorder=5)
    ax.plot([X(10, 17)] * 2, [y0, 22], color=GREEN, lw=2)
    ax.plot([X(10, 17)], [y0], 'o', color=GREEN, ms=11, zorder=5)
    ax.text(X(10, 17), 14, '令和4年10月17日　申請\n（E地方法務局）', ha='center', va='center', fontsize=15, weight='bold', color=GREEN, linespacing=1.4)
    ax.plot([X(10, 31)] * 2, [y0 - 4, y0 + 4], color=RED, lw=3)
    ax.text(X(10, 31), 22, '期限　10月31日', ha='center', va='center', fontsize=15, weight='bold', color=RED)
    fig.text(0.5, 0.085, '変更があった日（9月30日）から1月以内に申請する（不動産登記法第51条第1項）。10月17日の申請は期限内',
             ha='center', va='center', fontsize=14)
    fig.text(0.5, 0.04, '増築も車庫の新築も同じ9月30日なので、期限も同じ。2つをまとめて1枚の申請書で申請する',
             ha='center', va='center', fontsize=14)
    save_fixed(fig, 'R4_dai22mon_zu01_jikeiretsu')


def zu_ikko_tatemono():
    """図3：問2の判断。種類が違っても1個の建物にできる。1個にできないのは所有者が違うとき。"""
    card_figure('R4_dai22mon_zu03_ikko_tatemono',
                '1個の建物として登記できなくなるのは、「種類」が違うときではなく「所有者」が違うとき',
                [('誤り：エ＝「種類」', RED,
                  ['令子さんの車庫の種類＝車庫', '令子さんの家の種類＝居宅', '', '種類が違っても、車庫は附属建物として\n同じ登記記録に入れた（事実関係5）', '',
                   '*種類は、1個の建物にできるかどうかの\n決め手ではない']),
                 ('正解：エ＝「所有者」', GREEN,
                  ['株式会社中山時計店が車庫を新築して\n持ち主になった場合', '↓', '持ち主（所有者）が令子さんと別の人（法人）', '↓',
                   '*数棟の建物の所有者が異なると、\n1個の建物として登記できない', '→ 本件建物とは別に、会社を所有者とする\n建物表題登記をする'])],
                ['準則第78条第1項：効用上一体として利用される状態にある数棟の建物は、所有者の意思に反しない限り、1個の建物として取り扱う',
                 '問2の答え：ア＝効用上一体、イ＝所有者の意思、ウ＝1個の建物、エ＝所有者'], h=8.4)


def zu_shahen_kyori():
    """図5：筆界が斜めなので、同じ東の外壁でも角ごとに辺BCまでの距離が違う。"""
    fig, axes = new_figure('斜めの辺BCまでの距離は、角ごとに違う',
                           '辺BCは北へ1m進むごとに東へ0.1m開く。建物図面に書くのは、問題の測定値（南東の角から測った2.0）',
                           w=16, h=10)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(SITE, color=BLACK, lw=2.4)
    z.poly([B_(*v) for v in F1], color=BLACK, lw=2.0, fill=ORANGE, alpha=0.2)
    z.poly([G_(*v) for v in GAR], color=BLACK, lw=2.0, fill=ORANGE, alpha=0.2)
    n_main = N0 + HALF
    for x, e, t, col in [(S_EXT, E_EXT, '2.0（南東の角）', BLACK), (n_main, E_EXT, '約2.8（北東の角）', RED),
                         (G_S_EXT, G_E_EXT, '2.0（南東の角）', BLACK), (G_N_EXT, G_E_EXT, '約2.4（北東の角）', RED)]:
        dist_arrow(z, complex(x, e), complex(x, bc_y(x)), t, color=col, fs=14, text_pos=complex(x, bc_y(x) + 0.4))
    assert round(bc_y(n_main) - E_EXT, 1) == 2.8 and round(bc_y(G_N_EXT) - G_E_EXT, 1) == 2.4
    z.free_text(B_(13.5, 4.0), '主である建物', fs=13)
    z.free_text(centroid([G_(*v) for v in GAR]), '車庫', fs=13)
    z.free_text(complex(56, 81.6), '道路\n（5-4）', fs=13, color=GRAY)
    fit(ax, [complex(50, 56), complex(70, 82)], margin=0.1, extra=[xy(complex(46, 54)), xy(complex(72, 87))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R4_dai22mon_zu05_shahen_kyori')


def zu_shozai_kakunin():
    """図6：建物と車庫の位置を座標で出して、どの角も敷地の内側＝所在は5番地3だけ。"""
    fig, axes = new_figure('座標で建物の位置を置いて、所在を確かめる',
                           '距離は筆界から外壁まで（〔調査図〕の（注）4）。外壁の位置から、壁の中心線・柱の外面との差を足し引きする',
                           w=18, h=9.5, ncols=2, width_ratios=[1.1, 1])
    fig.subplots_adjust(top=0.86, wspace=0.04)
    z = Zu(axes[0], fontsize=13)
    z.poly(SITE, color=BLACK, lw=2.2)
    bl = [B_(*v) for v in F1]
    gr = [G_(*v) for v in GAR]
    z.poly(bl, color=BLACK, lw=2.0, fill=BLUE, alpha=0.2)
    z.poly(gr, color=BLACK, lw=2.0, fill=BLUE, alpha=0.2)
    for p in bl + gr:
        z.point(p, size=5)
    w_ext = W0 - HALF
    dist_arrow(z, complex(57, w_ext), complex(57, 50), '8.15', fs=13, side=(0, 12))
    assert round(w_ext - 50, 2) == 8.15
    z.free_text(complex(66, 58), '5番3', fs=15)
    z.free_text(B_(13.5, 4.0), '主である建物', fs=12)
    z.free_text(centroid(gr), '車庫', fs=12)
    fit(axes[0], SITE, margin=0.08, extra=[xy(complex(47, 47)), xy(complex(72, 84))], pad_aspect=True)
    z.north_arrow()
    ax = axes[1]
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    lines = [('主である建物', BLUE, True), ('南の外壁　X＝50.00＋3.0＝53.00', BLACK, False),
             ('東の外壁　Y＝78.00＋(53.00−50.00)×0.1−2.0＝76.30', BLACK, False),
             ('西の外壁　Y＝76.30−18.00−0.15＝58.15', BLACK, False), ('　→ 西の辺DA（Y＝50.00）まで8.15', GRAY, False),
             ('', BLACK, False), ('車庫', BLUE, True), ('北の外壁　X＝70.00−1.0＝69.00', BLACK, False),
             ('南の外壁　X＝69.00−0.15−4.00−0.15＝64.70', BLACK, False),
             ('東の外壁　Y＝78.00＋(64.70−50.00)×0.1−2.0＝77.47', BLACK, False), ('', BLACK, False),
             ('どの角も本件土地の4つの辺の内側', GREEN, True), ('　→ 所在は「5番地3」だけ', GREEN, True)]
    y = 96
    for t, col, bold in lines:
        if t:
            ax.text(0, y, t, ha='left', va='top', fontsize=15, color=col, weight='bold' if bold else 'normal')
        y -= 7.4
    assert round(78 + (53 - 50) * 0.1 - 2.0, 2) == 76.30 and round(78 + (64.70 - 50) * 0.1 - 2.0, 2) == 77.47
    assert round(76.30 - 18.00 - 0.15, 2) == 58.15 and round(69.00 - 0.15 - 4.00 - 0.15, 2) == 64.70
    save(fig, [z], 'R4_dai22mon_zu06_shozai_kakunin')


def zu_chuu_shiwake():
    """図8：注の仕分け。問題文の注1〜5と、〔調査図〕の（注）1〜11は別物（番号が重なる）。"""
    fig, ax = fixed_figure('注の仕分け：問題文の注と、〔調査図〕の（注）は別物（番号が重なる）', w=18, h=12.5, rect=(0.02, 0.05, 0.96, 0.84))
    ax.text(1, 98, '問題文の注', ha='left', va='center', fontsize=17, weight='bold', color=BLUE)
    b1 = table_box(ax, 1, 95, [6.0, 21.0, 10.0], ['注', '内容', '使うところ'],
                   [('注1', '行為は全て適法で、\n書類も全て適法に作成', '―'),
                    ('注2', '登記の申請は書面申請', '―'),
                    ('注3', '建物図面は1/500、\n各階平面図は1/250', '第4欄の縮尺'),
                    ('注4', '距離は各階平面図が小数第2位、\n建物図面が小数第1位。主である\n建物の1階の形は書かなくてよい\n（1階の位置の表示は省略不可）', '距離の桁、\n2階の点線'),
                    ('注5', '文字は字画を明確に。\n訂正・加入・削除の書き方', '―')],
                   col_colors=[BLUE, None, GREEN])
    ax.text(41, 98, '〔調査図〕の（注）', ha='left', va='center', fontsize=17, weight='bold', color=ORANGE)
    b2 = table_box(ax, 41, 95, [7.0, 29.0, 22.0], ['（注）', '内容', '使うところ'],
                   [('1', '距離の単位はメートル', '―'),
                    ('2', '図1の（　）内は土地の地番。座標値は一覧表のとおり', '敷地の座標'),
                    ('3', '北はX軸の正方向', '図の上は北'),
                    ('4', '図1の筆界から建物までの距離は、全て外壁まで', '建物の位置、所在'),
                    ('5', '図2は増築後の本件建物、\n図3は新築した本件車庫の各階平面見取図', '―'),
                    ('6', '図2の〇印は、各階の重なる部分', '2階の位置'),
                    ('7', '増築部分の柱は木造で両面被覆。壁の厚さ0.15。\n図2の距離は柱の中心から', '壁心（0.15は引かない）'),
                    ('8', '図3の距離は胴縁の中心から。胴縁の厚さ0.10', '車庫の床面積'),
                    ('9', '図4は車庫の△部分の構造。\n鉄骨柱の外側は胴縁と被覆材で被覆', '車庫の床面積'),
                    ('10', '各建物の天井までの高さは全て2.5m以上', '―（屋根裏の論点なし）'),
                    ('11', '各建物の各隅部は全て直角', '―')],
                   col_colors=[ORANGE, None, GREEN])
    ax.text(1, min(b1, b2) - 4, '記事では「問題文の注4」「〔調査図〕の（注）7」のように、どちらの注かを必ず書き分ける',
            ha='left', va='center', fontsize=15, weight='bold', color=RED)
    save_fixed(fig, 'R4_dai22mon_zu08_chuu_shiwake')


def zu_hekishin():
    """図9：木造・柱の両面被覆は壁心。壁の厚さ0.15は引かない（内法は区分建物のとき）。"""
    card_figure('R4_dai22mon_zu09_hekishin',
                '本件建物は壁の中心線（壁心）で測る。壁の厚さ0.15は引かない',
                [('誤り：壁の厚さ0.15を引いて、\n壁の内側（内法）で測る', RED,
                  ['内法で測るのは、区分建物の専有部分', '', '本件建物は区分建物ではない\n（普通の建物）', '', '*図2の数字から壁の厚さ0.15を\n引いてはいけない']),
                 ('正解：壁の中心線（壁心）で測る', GREEN,
                  ['木造で、柱の両面が被覆されている', '↓', '柱の中心＝壁の中心', '↓', '*図2の数字（柱の中心からの距離）を\nそのまま使う', '例：5.00×5.00＝25.00'])],
                ['〔調査図〕の（注）7：壁の厚さは0.15、図2の距離は柱の中心から', '壁の厚さ0.15を使うのは、建物の位置を外壁から出すとき（外壁と壁の中心線の差0.075）だけ'],
                h=8.4)


def zu_tensen():
    """図12：2階の各階平面図には1階の位置を点線で重ねる（省略できない）。"""
    fig, axes = new_figure('2階の各階平面図には、1階の位置を点線で示す',
                           '問題文の注4：主である建物の1階の形と求積表は書かなくてよい。ただし、1階以外の階層を表示する場合における1階の位置の表示は省略できない',
                           w=17, h=8.4, ncols=2)
    fig.subplots_adjust(top=0.84, bottom=0.20)
    f2 = [P(*v) for v in F2]
    rest = [P(5, 3), P(5, 4), P(9, 4), P(9, 0), P(18, 0), P(18, 8), P(5, 8)]
    zs = []
    for k, (ax, ttl, col) in enumerate(zip(axes, ['誤り：1階の位置を書かない', '正解：1階の位置を点線で重ねる'], [RED, GREEN])):
        z = Zu(ax, fontsize=13)
        z.poly(f2, color=BLACK, lw=2.4, fill=BLUE, alpha=0.2)
        dims(z, f2, ['5.00', '5.00', '5.00', '5.00'], fs=12)
        if k:
            z.poly(rest, color=BLACK, lw=1.6, ls=':', closed=False)
            z.free_text(P(13.5, 4.0), '点線＝1階の位置\n（2階はない）', fs=13, color=GRAY)
        else:
            z.free_text(P(13.5, 4.0), '1階の位置が\n分からない', fs=13, color=RED)
        ax.set_title(ttl, fontsize=17, weight='bold', color=col, pad=10)
        fit(ax, [P(*v) for v in F1], margin=0.1, pad_aspect=True)
        zs.append(z)
    save(fig, zs, 'R4_dai22mon_zu12_tensen')


def zu_san_bon_no_sen():
    """図14：図4に出てくる3本の線のうち、床面積の区画は「柱の外面」の1本だけ。"""
    fig, axes = new_figure('図4の3本の線：床面積の区画になるのは「柱の外面」の1本だけ',
                           '図3の5.10×4.10は「胴縁の中心線」、図4の0.10・0.20は「鉄骨柱の中心線」から測った寸法。どちらも区画の線ではない',
                           w=18, h=9.5, ncols=2, width_ratios=[1.25, 1])
    fig.subplots_adjust(top=0.86, wspace=0.05)
    z = Zu(axes[0], fontsize=12)
    cov = [P(-0.15, 3.35), P(-0.10, 3.35), P(-0.10, 4.10), P(0.65, 4.10), P(0.65, 4.15), P(-0.15, 4.15)]
    dob = [P(-0.10, 3.35), P(0.0, 3.35), P(0.0, 4.0), P(0.65, 4.0), P(0.65, 4.10), P(-0.10, 4.10)]
    z.poly(cov, color=BLACK, lw=1.2, check=False)
    hatch(axes[0], cov, color=GRAY)
    z.poly(dob, color=BLACK, lw=1.2, fill=ORANGE, alpha=0.25, check=False)
    z.poly(rect(0.0, 3.6, 0.20, 4.0), color=GRAY, lw=0, fill=GRAY, alpha=0.18, check=False)
    for s_ in (4.0, 3.6):
        z.line(P(0.0, s_), P(0.20, s_), color=BLACK, lw=3.0)
    z.line(P(0.10, 3.6), P(0.10, 4.0), color=BLACK, lw=3.0)
    z.line(P(0.10, 3.40), P(0.10, 4.12), color=RED, lw=1.6, ls='--')       # 鉄骨柱の中心線（縦）
    z.line(P(-0.05, 3.80), P(0.65, 3.80), color=RED, lw=1.6, ls='--')      # 鉄骨柱の中心線（横）
    z.line(P(-0.05, 3.35), P(-0.05, 4.05), color=PURPLE, lw=1.6, ls='-.')  # 胴縁の中心線
    z.line(P(-0.05, 4.05), P(0.65, 4.05), color=PURPLE, lw=1.6, ls='-.')
    z.line(P(0.0, 3.35), P(0.0, 4.0), color=GREEN, lw=4.0)                 # 柱の外面
    z.line(P(0.0, 4.0), P(0.65, 4.0), color=GREEN, lw=4.0)
    z.callout(P(0.65, 3.80), '鉄骨柱の中心線（赤の破線）\n図4の0.10・0.20はここから', dirs=(0, 15, -15), dists=(40, 55, 70), fs=12, color=RED)
    z.callout(P(0.55, 4.05), '胴縁の中心線（紫の一点鎖線）\n図3の5.10×4.10はここから', dirs=(-90, -75, -105), dists=(40, 55, 70), fs=12, color=PURPLE)
    z.callout(P(-0.025, 3.7), '柱の外面（緑の太線）\n＝床面積の区画', dirs=(180, 165, 195), dists=(50, 65, 80), fs=13, color=GREEN)
    axes[0].set_title('図4の角（南西）の拡大', fontsize=16, weight='bold', pad=10)
    fit(axes[0], [P(-0.15, 3.3), P(0.65, 4.2)], margin=0.05, extra=[xy(P(-0.95, 3.1)), xy(P(1.6, 4.6))], pad_aspect=True)
    ax = axes[1]
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    rows = [('鉄骨柱の中心線', '図4の0.10・0.20', 'ひっかけ', RED), ('胴縁の中心線', '図3の5.10・4.10', '区画ではない', PURPLE),
            ('柱の外面', '胴縁の中心から0.05内側', '床面積の区画', GREEN)]
    ax.text(50, 94, '3本の線の見分け方', ha='center', va='center', fontsize=17, weight='bold')
    y = 84
    for name, where, ans, col in rows:
        rbox(ax, 2, y - 18, 96, 19, col, alpha=0.08)
        ax.text(5, y - 4, name, ha='left', va='center', fontsize=17, weight='bold', color=col)
        ax.text(5, y - 12, where, ha='left', va='center', fontsize=15)
        ax.text(95, y - 8, ans, ha='right', va='center', fontsize=17, weight='bold', color=col)
        y -= 25
    ax.text(50, 4, '区画は1本だけ。5.10→5.00、4.10→4.00（20.91→20.00）', ha='center', va='center', fontsize=15, color=GREEN, weight='bold')
    save(fig, [z], 'R4_dai22mon_zu14_san_bon_no_sen')


def zu_tenpu_shorui():
    """図16：添付書類の要否（令別表14の項・令第7条第1項第2号）。"""
    fig, ax = fixed_figure('添付書類は4点：建物図面・各階平面図・所有権証明書・代理権限証書', w=17, h=8.6, rect=(0.02, 0.05, 0.96, 0.84))
    table_box(ax, 1, 96, [17.0, 9.0, 70.0], ['書類', '要否', '理由・根拠'],
              [('建物図面', '必要', '床面積を変更し、附属建物を新築した\n（不動産登記令別表14の項添付情報欄ロ（1）・ハ）'),
               ('各階平面図', '必要', '建物図面と同じ（同欄ロ（1）・ハ）'),
               ('所有権証明書', '必要', '増築で増える床面積と、新築の車庫が令子さんのものであることを示す\n（同欄ロ（2）・ハ。工事をした乙川建設株式会社から受け取った書類）'),
               ('住所証明書', '不要', '令子さんは所有権の登記名義人で、住所は登記記録に載っている\n（新しく表題部所有者になる表題登記とは違う）'),
               ('代理権限証書', '必要', '土地家屋調査士が代理して申請する（不動産登記令第7条第1項第2号）')],
              fs=15, line_h=6.0, pad=5.5, head_h=8, col_colors=[None, BLUE, None])
    save_fixed(fig, 'R4_dai22mon_zu16_tenpu_shorui')


def zu_juusho_shozai():
    """図17：申請人の住所（住居表示の「号」）と建物の所在（地番の「番地」）の書き分け。"""
    card_figure('R4_dai22mon_zu17_juusho_shozai',
                '同じ「5の3」でも、申請人の住所と建物の所在は書き方が違う',
                [('申請人の住所（住居表示）', BLUE,
                  ['A市B町一丁目5番3号　和田令子', '', '*「番」のあとに「号」', '', '住居表示で書く']),
                 ('建物の所在（地番）', GREEN,
                  ['A市B町一丁目5番地3', '', '*「番地」のあとに数字', '', '土地の地番（5番3）で書く', '', '家屋番号は「5番3」（号も地も付けない）'])],
                ['本問の申請書で、申請人の欄は「5番3号」、建物の所在は「5番地3」、家屋番号は「5番3」と書き分ける'], h=7.4)


def zu_touroku_menkyozei():
    """図18：登録免許税。建物の表題部の変更の登記は別表第一に載っていないので税がかからない。"""
    card_figure('R4_dai22mon_zu18_touroku_menkyozei',
                '建物の表題部の変更の登記には、登録免許税がかからない',
                [('課税される登記（登録免許税法別表第一の一（十三））', ORANGE,
                  ['所有権の登記がある建物の', '分割・区分・合併', '', '*後の建物の個数×1,000円', '', '例：区分合併（R5）、建物区分（R3）']),
                 ('本問：建物表題部変更登記', GREEN,
                  ['増築・種類変更・構造変更・附属建物の新築', '↓', '別表第一に載っていない', '↓', '*税はかからない', '答案用紙にも欄がない'])],
                ['登録免許税法第2条：別表第一に掲げる登記について課税する（載っていない登記は課税の対象にならない）'], h=7.8)


def zu_fugou_tsukekata():
    """図19：符号の付け方。符号1は主である建物に合体して終わるので、新築の車庫は次の符号2。"""
    card_figure('R4_dai22mon_zu19_fugou_tsukekata',
                '符号1は使い終わる。新築の車庫は、次の番号の符号2',
                [('誤り：車庫を「符号1」にする', RED,
                  ['3行目：符号１　倉庫　…\n令和４年９月30日主である建物に合体', '4行目：符号１　車庫　…\n令和４年９月30日新築', '', '*同じ申請書で符号1が2回出てくる']),
                 ('正解：車庫は「符号2」', GREEN,
                  ['3行目：符号１　倉庫　…\n令和４年９月30日主である建物に合体', '4行目：符号２　車庫　…\n令和４年９月30日新築', '', '*符号1は、主である建物に合体して\n番号として使い終わっている'])],
                ['新しい附属建物には、次の番号を付ける（空いた符号を使い回さない）'], h=8.6)


def zu_kengen():
    """図20：問3④。権原（他人の不動産に物を附属させる法律上の根拠）と権限（行為をしてよい範囲）。"""
    card_figure('R4_dai22mon_zu20_kengen',
                '民法第242条ただし書の④は「権原」（「権限」ではない）',
                [('誤り：④権限', RED,
                  ['権限＝ある行為をしてよい範囲・資格', '', '例：代理人の権限', '', '*ここで問われているのは、\nこの意味ではない']),
                 ('正解：④権原', GREEN,
                  ['権原＝他人の不動産に物を附属させる\nことができる法律上の根拠', '', '例：地上権、賃借権', '', '*音は同じ。答案の漢字を取り違えない'])],
                ['民法第242条：不動産の所有者は、その不動産に従として付合した物の所有権を取得する。ただし、権原によってその物を附属させた他人の権利を妨げない',
                 '問3の答え：①所有者、②従、③付合、④権原'], h=8.2)


def zu_tsukou():
    """図21：裕太さんが費用を出しても、増築部分は付合して令子さんのものになる。"""
    fig, ax = fixed_figure('裕太さんが費用を出して増築しても、増築部分は令子さんのものになる', w=17, h=9, rect=(0.02, 0.10, 0.96, 0.78))
    steps = [('裕太さんが自分の\n費用で増築する', BLUE), ('増築部分は、主である\n建物と附属建物の間を\n埋め、壁を取り払い、\n全体が1つの居宅\nとして使われる', ORANGE),
             ('増築部分は独立して\n存在していない\n（独立性がない）', ORANGE), ('本件建物（令子さん\nの所有）に付合\n民法第242条本文', RED),
             ('増築部分の所有者は\n令子さん', GREEN)]
    w, gap = 16.0, 4.0
    for i, (t, col) in enumerate(steps):
        x = 2 + i * (w + gap)
        rbox(ax, x, 52, w, 36, col, alpha=0.10)
        ax.text(x + w / 2, 70, t, ha='center', va='center', fontsize=12.5, linespacing=1.4)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.4, 70), xytext=(x + w + 0.4, 70),
                        arrowprops=dict(arrowstyle='-|>', lw=1.8, color=GRAY))
    rbox(ax, 56, 8, 42, 30, GREEN, alpha=0.08)
    ax.text(77, 28, '裕太さんは、損をした分のお金（償金）を\n令子さんに請求できる（民法第248条）', ha='center', va='center', fontsize=14, linespacing=1.5)
    ax.text(77, 15, '→ 令子さんが、所有権の登記名義人として\n建物表題部変更登記を申請する', ha='center', va='center', fontsize=14, linespacing=1.5,
            weight='bold', color=GREEN)
    rbox(ax, 2, 8, 50, 30, ORANGE, alpha=0.08)
    ax.text(27, 28, 'ただし書（権原によって附属させた他人の権利を妨げない）が働くのは、\n附属させた物が独立して存在し続ける場合', ha='center', va='center',
            fontsize=13, linespacing=1.5)
    ax.text(27, 14, '本問の増築部分は独立性がまったくないので、ただし書は働かない', ha='center', va='center', fontsize=13, weight='bold', color=RED)
    save_fixed(fig, 'R4_dai22mon_zu21_tsukou')


if __name__ == '__main__':
    # 記事の挿入順（PNG名の番号順）
    zu_jikeiretsu()      # 01
    zu01()               # 02 工事前後
    zu_ikko_tatemono()   # 03
    zu02()               # 04 敷地
    zu_shahen_kyori()    # 05
    zu_shozai_kakunin()  # 06
    zu03()               # 07 建物図面
    zu_chuu_shiwake()    # 08
    zu_hekishin()        # 09
    zu04()               # 10 1階
    zu05()               # 11 2階
    zu_tensen()          # 12
    zu06()               # 13 車庫の誤り比較
    zu_san_bon_no_sen()  # 14
    zu07()               # 15 各階平面図
    zu_tenpu_shorui()    # 16
    zu_juusho_shozai()   # 17
    zu_touroku_menkyozei()  # 18
    zu_fugou_tsukekata()    # 19
    zu_kengen()          # 20
    zu_tsukou()          # 21
    zu08()               # 22 解く順番
    print('重なり合計:', len(PROBLEMS))
