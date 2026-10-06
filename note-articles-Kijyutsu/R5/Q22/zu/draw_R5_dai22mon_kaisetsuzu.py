"""令和5年度 第22問（建物）の解説図8枚を、座標値・頂点座標から作図してPNGに書き出す。

`../prompt_R5_dai22mon_kaisetsuzu.md` の図1〜図8どおり（番号は記事の挿入順）。作図の共通部品は `tools/zu_helpers.py`。
図3（建物図面）と図7（各階平面図）の完成形は、試験の答案用紙（`../touan_youshi/`）の第3欄の形（1枚の左半分が各階平面図、
右半分が建物図面。家屋番号・建物の所在の欄は建物図面の側に1つ、申請人・作成者は「（略）」、作成の日付と縮尺は印刷済み）の枠の中に描く。
敷地は〔座標値一覧表〕の (X＝北, Y＝東)。建物の平面は (東, 南)（原点＝建物の北西の角の壁の中心）で持ち、
zu_helpers の (北, 東) には B() で変換する。
実行: python3 note-articles-Kijyutsu/R5/Q22/zu/draw_R5_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle  # noqa: E402

from zu_helpers import Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []

# ---- 敷地（〔座標値一覧表〕） ----
A, B, C, D = complex(50, 75), complex(68, 75), complex(68, 89.5), complex(52, 88)
SITE = [A, B, C, D]
D_RECT = complex(50, 89.5)   # 図1の見た目のまま長方形と思い込んだときのD点

# ---- 建物の位置（壁厚0.15、筆界からの距離は外壁まで〈〔調査図〕の（注）2・（注）3〉。壁の中心線は外壁から0.075内側） ----
HALF = 0.075
N0 = 68 - 2.0 - HALF                       # 北の壁の中心線 X＝65.925（辺BCから外壁まで2.0）
S_EXT = N0 - 11.80 - HALF                  # 南の外壁 X＝54.05
Y_CD = 88 + (S_EXT - 52) * 1.5 / 16        # 南の外壁の高さでの辺CD上の点 Y＝88.1921875
W0 = Y_CD - 2.90 - HALF - 7.30             # 西の壁の中心線 Y＝77.9171875（南東の角から辺CDまで2.9）


def B_(e, s):
    """建物の平面の (東, 南) を zu_helpers の複素数 (北 + 東i) にする（建物図面用：敷地の座標に置く）。"""
    return complex(N0 - s, W0 + e)


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
                                                         mutation_scale=14, shrinkA=0, shrinkB=0), zorder=6)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    return z.free_text(m, text, fs=fs, color=color, offsets=(side, (-side[0], -side[1]), (0, 12), (0, -12)),
                       ha='center', va='center')


STEP_OFFS = ((26, 0), (30, 4), (26, -6), (34, 0))


def step_label(z, p, text='0.90m', fs=13, offsets=STEP_OFFS):
    """短い段差（0.90）の寸法。辺に平行に置くと隣の寸法と重なるので、段差の横に水平に書く。"""
    return z.free_text(p, text, fs=fs, offsets=offsets)


# ---- 1階・2階の形（壁の中心線。(東, 南)） ----
F1 = [(0, 0), (6.4, 0), (6.4, 2.8), (7.3, 2.8), (7.3, 11.8), (0, 11.8)]
F2 = [(0, 0), (7.3, 0), (7.3, 12.7), (4.6, 12.7), (4.6, 11.8), (0, 11.8)]
F2_OLD = [(0, 0), (7.3, 0), (7.3, 7.3), (4.6, 7.3), (4.6, 11.8), (0, 11.8)]
assert round(area([P(*v) for v in F1]), 2) == 83.62
assert round(area([P(*v) for v in F2]), 2) == 88.57
assert round(area([P(*v) for v in F2_OLD]), 2) == 73.99


def zu02():
    fig, axes = new_figure('本件土地（敷地）の辺長確認図（作図チェック用）',
                           '辺AD・辺CDは斜め（A点とD点のX、C点とD点のYが違う）。辺長は作図が正しいかを確かめるためのもので、建物図面には書かない',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=16)
    z.line(C, D_RECT, color=GRAY, lw=1.4, ls='--')
    z.line(D_RECT, A, color=GRAY, lw=1.4, ls='--')
    z.poly(SITE, color=BLACK, lw=2.6, fill=BLUE, alpha=0.12)
    for p in SITE:
        z.point(p)
    z.point(D_RECT, color=GRAY, size=5)
    ax.annotate('', xy(D), xytext=xy(D_RECT), arrowprops=dict(arrowstyle='-|>', color=RED, lw=2.2, mutation_scale=18),
                zorder=6)
    z.segments.append((xy(D_RECT), xy(D)))
    c = centroid(SITE)
    for p, n in zip(SITE, 'ABCD'):
        z.point_label(p, n, away=c, fs=19)
    z.edge_label(A, B, 'AB 18.0m', c, fs=16)
    z.edge_label(B, C, 'BC 14.5m', c, fs=16)
    z.edge_label(C, D, 'CD 16.1m', c, fs=16, outward=False)
    z.edge_label(D, A, 'DA 13.2m', c, fs=16, outward=False)
    z.callout(D, 'D点（52.00, 88.00）\nA点のXは50.00、C点のYは89.50\n→ 辺AD・辺CDは斜め', dirs=(15, 30, 0), dists=(90, 120, 150),
              fs=15, color=RED)
    z.callout(D_RECT, '点線＝長方形だと思い込んだ形', dirs=(-20, -35, -10), dists=(60, 80, 100), fs=14, color=GRAY)
    z.free_text(complex(60.5, 81.5), '本件土地（3-9）', fs=17)
    fit(ax, SITE, margin=0.12, extra=[xy(complex(46, 104)), xy(complex(70, 71))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R5_dai22mon_zu02_shikichi_henchou')


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.01
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


INK = '#1a3a8f'   # 記入（濃い青）


# ---- 答案用紙の第3欄（試験の答案用紙 `../touan_youshi/R5_dai22mon_touan_youshi_p2.png` で確かめた形） ----
# 第3欄はA3横の1枚で、外枠の中が1つの大きな枠になっており、上下の中央に短い区切りの線があるだけ。
# 左半分が各階平面図（枠の上に題「各階平面図」、枠の下に作成者の欄：（略）と（令和5年〇月〇日作成）が印刷、縮尺 1／250 が印刷）、
# 右半分が建物図面（枠の右上に家屋番号・建物の所在の欄が1つずつ〈各階平面図と兼用〉、家屋番号の欄は枠の上に出ている、
# 枠の下に申請人の欄：（略）が印刷、縮尺 1／500 が印刷）。
# 下の座標は、答案用紙を150dpiで書き出したPNG（横2481px）を横2000pxに縮めたときの位置（px、y は下向き）。
SHEET = {
    'frame': (383, 122, 1820, 1222),           # 大きな枠（左, 上, 右, 下）
    'center': 1101,                             # 中央の区切り（上 122〜170、下 1175〜1222 の短い線）
    'kaoku': (1147, 75, 1258, 1443, 122),       # 家屋番号の欄（左, 上, 見出しの右, 右, 下）
    'shozai': (1147, 122, 1258, 1820, 170),     # 建物の所在の欄
    'sakusei': (383, 1222, 478, 907, 955, 1065, 1290),   # 作成者の欄（左, 上, 見出しの右, 縮尺の左, 縮尺の見出しの右, 右, 下）
    'shinsei': (1137, 1222, 1232, 1663, 1710, 1820, 1290),  # 申請人の欄
}
PRINT_SAKUSEI = ('（略）', '（令和5年〇月〇日作成）', '250')
PRINT_SHINSEI = ('（略）', '500')


class SheetMap:
    """答案用紙の位置（px）を、図（figure）の座標 0〜1 に写す。"""

    def __init__(self, fig, s, sx0, sy0, left_px, top_px):
        self.fig = fig
        self.W, self.H = fig.get_size_inches() * fig.dpi
        self.s, self.sx0, self.sy0, self.left, self.top = s, sx0, sy0, left_px, top_px

    def __call__(self, x, y):
        return ((self.left + (x - self.sx0) * self.s) / self.W, 1 - (self.top + (y - self.sy0) * self.s) / self.H)

    def line(self, x0, y0, x1, y1, lw=1.8, color=BLACK, ls='-'):
        (a, b), (c, d) = self(x0, y0), self(x1, y1)
        self.fig.add_artist(Line2D([a, c], [b, d], transform=self.fig.transFigure, lw=lw, color=color, ls=ls))

    def box(self, x0, y0, x1, y1, lw=1.6):
        for seg in ((x0, y0, x1, y0), (x1, y0, x1, y1), (x1, y1, x0, y1), (x0, y1, x0, y0)):
            self.line(*seg, lw=lw)

    def text(self, x, y, t, fs=15, ha='center', color=BLACK, **kw):
        a, b = self(x, y)
        self.fig.text(a, b, t, ha=ha, va='center', fontsize=fs, color=color, **kw)

    def axes(self, x0, y0, x1, y1):
        (a, b), (c, d) = self(x0, y1), self(x1, y0)
        return self.fig.add_axes([a, b, c - a, d - b])

    def frac(self, x0, y0, x1, y1, denom, fs=15):
        """縮尺の印刷「1／250」（斜線の分数）。"""
        self.line(x0 + (x1 - x0) * 0.15, y1 - (y1 - y0) * 0.15, x1 - (x1 - x0) * 0.15, y0 + (y1 - y0) * 0.15, lw=1.2)
        self.text(x0 + (x1 - x0) * 0.36, y0 + (y1 - y0) * 0.30, '1', fs=fs)
        self.text(x0 + (x1 - x0) * 0.70, y0 + (y1 - y0) * 0.76, denom, fs=fs)


def sheet_frame(m, side):
    """第3欄の半分（side＝'left' 各階平面図／'right' 建物図面）の枠と印刷文字を描く。中央の切れ目は灰色の一点鎖線で示す。"""
    L, T, R, Bm = SHEET['frame']
    c = SHEET['center']
    x0, x1 = (L, c) if side == 'left' else (c, R)
    m.line(x0, T, x1, T)
    m.line(x0, Bm, x1, Bm)
    m.line(L if side == 'left' else R, T, L if side == 'left' else R, Bm)
    m.line(c, T, c, 170)                       # 中央の区切りの短い線（印刷）
    m.line(c, 1175, c, Bm)
    m.line(c, 170, c, 1175, lw=1.0, color='#999999', ls='-.')   # 用紙の続き（ここで切って見せている）
    if side == 'left':
        m.text(730, 104, '各　階　平　面　図', fs=20)
        a, t, lab, sk, skl, r, b = SHEET['sakusei']
        m.box(a, t, r, b)
        m.line(lab, t, lab, b, lw=1.4)
        m.line(sk - 4, t, sk - 4, b, lw=1.2)
        m.line(sk, t, sk, b, lw=1.2)               # 縮尺の前の二重線
        m.line(skl, t, skl, b, lw=1.4)
        m.text((a + lab) / 2, (t + b) / 2, '作　成　者', fs=15)
        m.text(552, 1250, PRINT_SAKUSEI[0], fs=15)
        m.text(893, 1274, PRINT_SAKUSEI[1], fs=14, ha='right')
        m.text((sk + skl) / 2, (t + b) / 2, '縮尺', fs=14)
        m.frac(skl, t, r, b, PRINT_SAKUSEI[2])
        m.text(c - 6, 1150, '（用紙の中央。右半分は建物図面）', fs=11, ha='right', color='#888888')
    else:
        a, t, lab, r, b = SHEET['kaoku']
        m.box(a, t, r, b)
        m.line(lab, t, lab, b, lw=1.4)
        m.text((a + lab) / 2, (t + b) / 2, '家屋番号', fs=14)
        m.text(1570, 104, '建　物　図　面', fs=20)
        a, t, lab, r, b = SHEET['shozai']
        m.box(a, t, r, b)
        m.line(lab, t, lab, b, lw=1.4)
        m.text((a + lab) / 2, (t + b) / 2, '建物の所在', fs=14)
        a, t, lab, sk, skl, r, b = SHEET['shinsei']
        m.box(a, t, r, b)
        m.line(lab, t, lab, b, lw=1.4)
        m.line(sk - 4, t, sk - 4, b, lw=1.2)
        m.line(sk, t, sk, b, lw=1.2)
        m.line(skl, t, skl, b, lw=1.4)
        m.text((a + lab) / 2, (t + b) / 2, '申　請　人', fs=15)
        m.text(1440, 1250, PRINT_SHINSEI[0], fs=15)
        m.text((sk + skl) / 2, (t + b) / 2, '縮尺', fs=14)
        m.frac(skl, t, r, b, PRINT_SHINSEI[1])
        m.text(c + 6, 1150, '（用紙の中央。左半分は各階平面図）', fs=11, ha='left', color='#888888')


def sheet_inset(fig, rect, side):
    """第3欄の1枚全体の縮図（見せている半分に色を付ける）。固定配置なので重なり検査の対象外。"""
    ax = fig.add_axes(rect)
    ax.set_xlim(370, 1835)
    ax.set_ylim(1300, 60)
    ax.set_aspect('equal')
    ax.axis('off')
    L, T, R, Bm = SHEET['frame']
    c = SHEET['center']
    hx = (L, c) if side == 'left' else (c, R)
    ax.add_patch(Rectangle((hx[0], T), hx[1] - hx[0], Bm - T, facecolor=BLUE, alpha=0.15, lw=0))
    ax.add_patch(Rectangle((L, T), R - L, Bm - T, fill=False, lw=1.2, ec=BLACK))
    ax.plot([c, c], [T, 170], color=BLACK, lw=1.0)
    ax.plot([c, c], [1175, Bm], color=BLACK, lw=1.0)
    for key in ('kaoku', 'shozai'):
        a, t, _, r, b = SHEET[key]
        ax.add_patch(Rectangle((a, t), r - a, b - t, fill=False, lw=0.8, ec=BLACK))
    for key in ('sakusei', 'shinsei'):
        a, t, _, _, _, r, b = SHEET[key]
        ax.add_patch(Rectangle((a, t), r - a, b - t, fill=False, lw=0.8, ec=BLACK))
    ax.text((L + c) / 2, 680, '各階平面図\n1／250', ha='center', va='center', fontsize=11)
    ax.text((c + R) / 2, 680, '建物図面\n1／500', ha='center', va='center', fontsize=11)
    return ax


def zu03():
    setup_font()
    fig = plt.figure(figsize=(12, 21), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面の完成形（答案用紙の第3欄の右半分・縮尺1/500）', fontsize=21, weight='bold', y=0.988)
    m = SheetMap(fig, 1.40, 1080, 60, 70, 70)
    sheet_frame(m, 'right')
    # 記入：家屋番号は空欄（登記所が付ける）、建物の所在
    m.text(1270, 146, 'A市B町一丁目3番地9', fs=16, ha='left', color=INK)
    ax = m.axes(1112, 182, 1808, 1205)
    z = Zu(ax, fontsize=15)
    fit(ax, SITE, margin=0.1, extra=[xy(complex(47, 71)), xy(complex(71, 92))], pad_aspect=True)
    z.north_arrow()
    z.poly(SITE, color=BLACK, lw=2.2)
    bldg = [B_(*v) for v in F1]
    z.poly(bldg, color=BLACK, lw=2.4)
    assert round(area(bldg), 2) == 83.62
    # 距離（外壁まで）：北の2か所（西端・東端）は辺BCまで、南東の角は辺CDまで（東西方向）
    n_ext = N0 + HALF
    for e in (0, 6.4):
        y = W0 + e + (-HALF if e == 0 else HALF)
        dist_arrow(z, complex(n_ext, y), complex(68, y), '2.0', side=(-16 if e == 0 else 16, 0))
    se = complex(S_EXT, W0 + 7.3 + HALF)
    dist_arrow(z, se, complex(S_EXT, Y_CD), '2.9', side=(0, -14))
    OFFS = ((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0))
    z.free_text(complex(52.55, 79.5), '3-9', fs=17, offsets=OFFS)
    for p, t in [(complex(69.6, 73.2), '3-12'), (complex(69.4, 82.0), '3-11'), (complex(60.0, 73.2), '3-10'),
                 (complex(60.0, 90.6), '1-1\n道路'), (complex(48.6, 81.5), '3-1　道路')]:
        z.free_text(p, t, fs=15, offsets=OFFS)
    z.free_text(complex(47.6, 90.2), '（単位：m）', fs=13, offsets=OFFS)
    sheet_inset(fig, [0.03, 0.012, 0.27, 0.11], 'right')
    fig.text(0.33, 0.067, '第3欄は1枚（A3横）の左半分が各階平面図、右半分が建物図面。\n'
             '家屋番号・建物の所在の欄は建物図面の側に1つだけ（各階平面図と兼用）。\n'
             '申請人の欄の「（略）」と縮尺「1／500」は印刷済みなので書かない。', ha='left', va='center',
             fontsize=13, linespacing=1.6)
    save(fig, [z], 'R5_dai22mon_zu03_tatemono_zumen')


def zu04():
    fig, axes = new_figure('2階の求積：藍子の「全体から引く」と、正しい「分割して足す」',
                           '左は7.30×11.80−2.70×4.50＝73.99。これは工事前の2階の形。リビング拡張で東側が南へ0.90張り出したので、正しくは88.57',
                           w=16, h=9.5, ncols=2)
    fig.subplots_adjust(top=0.85)
    full = rect(0, 0, 7.3, 11.8)
    notch = rect(4.6, 7.3, 7.3, 11.8)
    z = Zu(axes[0], fontsize=14)
    z.poly(full, color=BLACK, lw=2.0)
    z.poly(notch, color=RED, lw=1.6, ls='--', fill=RED, alpha=0.12)
    hatch(axes[0], notch, color=RED)
    dims(z, full, ['7.30m', '11.80m', None, '11.80m'])
    z.callout(centroid(notch), '2.70×4.50を引く', dirs=(-30, -50, -10), fs=14, color=RED)
    z.free_text(P(3.0, 4.0), '7.30×11.80\n−2.70×4.50\n＝73.99㎡', fs=16)
    axes[0].set_title('誤り：全体の枠から引く（藍子）', fontsize=18, weight='bold', color=RED, pad=12)
    fit(axes[0], full + [P(7.3, 12.7)], margin=0.22, extra=[xy(P(11.5, 13.5))], pad_aspect=True)
    z2 = Zu(axes[1], fontsize=14)
    w, e = rect(0, 0, 4.6, 11.8), rect(4.6, 0, 7.3, 12.7)
    z2.poly(w, color=BLUE, lw=0, fill=BLUE, check=False)
    z2.poly(e, color=ORANGE, lw=0, fill=ORANGE, alpha=0.35, check=False)
    z2.line(P(4.6, 0), P(4.6, 11.8), color=GRAY, lw=1.2, ls='--')
    f2 = [P(*v) for v in F2]
    z2.poly(f2, color=BLACK, lw=2.2)
    step_label(z2, P(4.6, 12.25))
    dims(z2, f2, ['7.30m', '12.70m', '2.70m', None, '4.60m', '11.80m'])
    z2.free_text(P(2.3, 5.9), '4.60×11.80\n＝54.28', fs=15)
    z2.free_text(P(5.95, 6.35), '2.70\n×\n12.70\n＝\n34.29', fs=14)
    axes[1].set_title('正解：2つの長方形に分けて足す（88.57㎡）', fontsize=18, weight='bold', color=GREEN, pad=12)
    fit(axes[1], f2, margin=0.22, extra=[xy(P(11.5, 13.5))], pad_aspect=True)
    save(fig, [z, z2], 'R5_dai22mon_zu04_ayamari_hikaku')


def zu05():
    fig, axes = new_figure('1階の床面積求積図（壁の中心線）',
                           '西側6.40×11.80＝75.52　＋　東側0.90×9.00＝8.10　＝　83.62㎡（北東の角の玄関前0.90×2.80は建物の外）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    w, e = rect(0, 0, 6.4, 11.8), rect(6.4, 2.8, 7.3, 11.8)
    z.poly(w, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(e, color=ORANGE, lw=0, fill=ORANGE, alpha=0.4, check=False)
    z.line(P(6.4, 2.8), P(6.4, 11.8), color=GRAY, lw=1.2, ls='--')
    f1 = [P(*v) for v in F1]
    z.poly(f1, color=BLACK, lw=2.4)
    step_label(z, P(7.3, 2.8), offsets=((30, 12), (36, 18), (30, -12)))
    dims(z, f1, ['6.40m', '2.80m', None, '9.00m', '7.30m', '11.80m'])
    z.free_text(P(3.2, 6.0), '西側\n6.40×11.80\n＝75.52', fs=16)
    z.callout(P(6.85, 9.6), '東側（和室・LDK側）\n0.90×9.00＝8.10', dirs=(-30, -45, -20), fs=15)
    z.callout(P(6.85, 1.4), '玄関前（建物の外）', dirs=(20, 40, 0), fs=14, color=GRAY)
    z.free_text(P(3.65, -2.2), '1階 床面積：83.62㎡', fs=18, weight='bold')
    fit(ax, f1, margin=0.2, extra=[xy(P(3.65, -2.8)), xy(P(14, 12))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R5_dai22mon_zu05_1kai_kyuuseki')


def zu06():
    fig, axes = new_figure('2階の床面積求積図（壁の中心線）',
                           '西側4.60×11.80＝54.28　＋　東側2.70×12.70＝34.29　＝　88.57㎡。点線は1階の位置（北東の欠けと、南の0.90の張り出し）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    w, e = rect(0, 0, 4.6, 11.8), rect(4.6, 0, 7.3, 12.7)
    added = rect(4.6, 7.3, 7.3, 12.7)
    z.poly(w, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(e, color=ORANGE, lw=0, fill=ORANGE, alpha=0.35, check=False)
    z.poly(added, color=RED, lw=0, fill=RED, alpha=0.25, check=False)
    z.line(P(4.6, 0), P(4.6, 11.8), color=GRAY, lw=1.2, ls='--')
    f2 = [P(*v) for v in F2]
    z.poly(f2, color=BLACK, lw=2.4)
    # 1階の位置（点線）：北東の欠けと、1階の南の壁
    z.line(P(6.4, 0), P(6.4, 2.8), color=BLACK, lw=1.6, ls=':')
    z.line(P(6.4, 2.8), P(7.3, 2.8), color=BLACK, lw=1.6, ls=':')
    z.line(P(4.6, 11.8), P(7.3, 11.8), color=BLACK, lw=1.6, ls=':')
    step_label(z, P(4.6, 12.25))
    dims(z, f2, ['7.30m', '12.70m', '2.70m', None, '4.60m', '11.80m'])
    z.free_text(P(2.3, 5.5), '西側\n4.60×11.80\n＝54.28', fs=16)
    z.free_text(P(5.95, 5.0), '東側\n2.70\n×12.70\n＝34.29', fs=14)
    z.callout(P(5.95, 10.0), 'リビング拡張で増えた部分\n2.70×5.40（南へ0.90張り出す）', dirs=(-10, 10, -30), fs=14, color=RED)
    z.callout(P(6.85, 1.4), '点線＝1階の位置', dirs=(20, 40, 0), fs=14)
    z.free_text(P(3.65, -2.2), '2階 床面積：88.57㎡', fs=18, weight='bold')
    fit(ax, f2, margin=0.2, extra=[xy(P(3.65, -2.8)), xy(P(16, 12))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R5_dai22mon_zu06_2kai_kyuuseki')


def zu08():
    fig, axes = new_figure('2階の形：工事前と工事完了後',
                           '工事前の2階（73.99㎡）は一棟の建物の表示に書く床面積。南東のバルコニーの一部を囲んで、東側が南へ5.40伸びた（増えた部分2.70×5.40＝14.58）',
                           w=16, h=9.5, ncols=2)
    fig.subplots_adjust(top=0.85)
    z = Zu(axes[0], fontsize=14)
    n, s = rect(0, 0, 7.3, 7.3), rect(0, 7.3, 4.6, 11.8)
    z.poly(n, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(s, color=BLUE, lw=0, fill=BLUE, check=False)
    z.line(P(0, 7.3), P(4.6, 7.3), color=GRAY, lw=1.2, ls='--')
    old = [P(*v) for v in F2_OLD]
    z.poly(old, color=BLACK, lw=2.2)
    balc = rect(4.6, 7.3, 7.3, 11.8)
    z.poly(balc, color=GRAY, lw=1.2, ls='--', check=False)
    dims(z, old, ['7.30m', '7.30m', '2.70m', '4.50m', '4.60m', '11.80m'])
    z.free_text(P(3.65, 3.65), '北側\n7.30×7.30＝53.29', fs=15)
    z.free_text(P(2.3, 9.55), '南西側\n4.60×4.50\n＝20.70', fs=14)
    z.callout(P(5.95, 9.55), 'バルコニー', dirs=(0, -20, 20), fs=13, color=GRAY)
    axes[0].set_title('【工事前】2階：73.99㎡', fontsize=18, weight='bold', pad=12)
    fit(axes[0], old + [P(7.3, 12.7)], margin=0.22, extra=[xy(P(10.5, 13.5))], pad_aspect=True)
    z2 = Zu(axes[1], fontsize=14)
    w, e = rect(0, 0, 4.6, 11.8), rect(4.6, 0, 7.3, 12.7)
    added = rect(4.6, 7.3, 7.3, 12.7)
    z2.poly(w, color=BLUE, lw=0, fill=BLUE, check=False)
    z2.poly(e, color=BLUE, lw=0, fill=BLUE, check=False)
    z2.poly(added, color=RED, lw=0, fill=RED, alpha=0.35, check=False)
    f2 = [P(*v) for v in F2]
    z2.poly(f2, color=BLACK, lw=2.2)
    step_label(z2, P(4.6, 12.25))
    dims(z2, f2, ['7.30m', '12.70m', '2.70m', None, '4.60m', '11.80m'])
    z2.free_text(P(5.95, 10.0), '増築\n2.70\n×5.40', fs=14, color=RED)
    z2.free_text(P(2.3, 5.9), '4.60×11.80\n＋2.70×12.70', fs=14)
    axes[1].set_title('【工事完了後】2階：88.57㎡', fontsize=18, weight='bold', pad=12)
    fit(axes[1], f2, margin=0.22, extra=[xy(P(10.5, 13.5))], pad_aspect=True)
    assert round(2.70 * 5.40, 2) == round(88.57 - 73.99, 2) == 14.58
    save(fig, [z, z2], 'R5_dai22mon_zu08_2kai_kouji_zengo')


def zu07():
    """各階平面図の完成形（答案用紙の第3欄の左半分の枠の中。求積図とちがい塗り分けはしない）。"""
    setup_font()
    fig = plt.figure(figsize=(12, 21), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図の完成形（答案用紙の第3欄の左半分・縮尺1/250）', fontsize=21, weight='bold', y=0.988)
    m = SheetMap(fig, 1.40, 360, 60, 70, 70)
    sheet_frame(m, 'left')
    axes = [m.axes(395, 150, 742, 860), m.axes(750, 150, 1092, 860)]
    zs = []
    tables = ['1階\n0.90×9.00＝8.1000\n6.40×11.80＝75.5200\n計　83.6200\n床面積　83.62㎡',
              '2階\n2.70×12.70＝34.2900\n4.60×11.80＝54.2800\n計　88.5700\n床面積　88.57㎡']
    for k, (pts, labels, name) in enumerate([
            (F1, ['6.40', None, None, '9.00', '7.30', '11.80'], '1階'),
            (F2, ['7.30', '12.70', '2.70', None, '4.60', '11.80'], '2階')]):
        ax = axes[k]
        z = Zu(ax, fontsize=13)
        ax.set_title(name, fontsize=17, weight='bold')
        fit(ax, [P(*v) for v in F2], margin=0.25, pad_aspect=True)
        poly = [P(*v) for v in pts]
        z.poly(poly, color=BLACK, lw=2.4)
        if name == '1階':
            z.edge_label(poly[1], poly[2], '2.80', P(3.0, 6.0), fs=13, outward=False)
            z.free_text(P(7.85, 2.35), '0.90', fs=13, offsets=((0, 0), (6, 0), (0, -6)))
        else:
            z.line(P(6.4, 0), P(6.4, 2.8), color=BLACK, lw=1.4, ls=':')       # 1階の位置（北東の欠け）
            z.line(P(6.4, 2.8), P(7.3, 2.8), color=BLACK, lw=1.4, ls=':')
            z.line(P(4.6, 11.8), P(7.3, 11.8), color=BLACK, lw=1.4, ls=':')   # 1階の南の壁
            step_label(z, P(4.6, 12.25), text='0.90', fs=13)
        dims(z, poly, labels, fs=13)
        zs.append(z)
        m.text(430 + 355 * k, 990, tables[k], fs=15, ha='left', linespacing=1.6)
    zs[1].north_arrow()
    assert round(area([P(*v) for v in F1]), 4) == 83.62 and round(area([P(*v) for v in F2]), 4) == 88.57
    sheet_inset(fig, [0.03, 0.012, 0.27, 0.11], 'left')
    fig.text(0.33, 0.067, '壁の中心線の寸法（小数点以下第2位まで。問題文の注4）で\n1階・2階を書き分け、2階には1階の位置を点線で示し、\n'
             '求積表と床面積を各階の下に書く。屋根裏部屋（天井の最高部1.40）は描かない。\n'
             '作成者の「（略）」・作成の日付・縮尺「1／250」は印刷済み。\n家屋番号の欄は右半分（建物図面の側）に1つだけ（兼用）。',
             ha='left', va='center', fontsize=13, linespacing=1.6)
    save(fig, zs, 'R5_dai22mon_zu07_kakukai_heimenzu')


def zu01():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    setup_font()
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　問2のただし書きを先に読み、図面→申請書→穴埋め', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '問1〜問4と\n問2のただし書き', '一の申請・\n不要・記載不要', BLUE),
        ('②', '事実関係・\n登記記録', '合併（合体ではない）・\n構造変更・増築', BLUE),
        ('③', '第3欄\n各階平面図', '壁心で求積\n83.62・88.57', RED),
        ('④', '第3欄\n建物図面', '座標で敷地、\n2.0・2.0・2.9', RED),
        ('⑤', '第2欄\n申請書', '工事前の2階\n73.99も計算', GREEN),
        ('⑥', '第1欄・第4欄\nと見直し', 'ア〜オ、\n①〜⑤', GRAY),
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
    ax.text(1 + 3 * (w + gap) - gap / 2, 76, '床面積を出してから申請書へ', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 4 * (w + gap) - gap, 72), xytext=(1 + 2 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '屋根裏部屋（天井の最高部1.40）は床面積にも階数にも入れない。2階は東側が南へ0.90張り出すので、1階と同じ形と思い込まない。\n'
             '第1欄（ア〜オ）と第4欄（①〜⑤）は短い穴埋めなので最後に回し、作図の時間を削らない',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'R5_dai22mon_zu01_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図1: 解く順番（固定配置）\n  →', path)


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
