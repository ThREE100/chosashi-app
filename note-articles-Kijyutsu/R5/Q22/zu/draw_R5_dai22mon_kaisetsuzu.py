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


def zu07():
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
    save(fig, [z], 'R5_dai22mon_zu07_shikichi_henchou')


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


def zu11():
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
    save(fig, [z], 'R5_dai22mon_zu11_tatemono_zumen')


def zu14():
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
    save(fig, [z, z2], 'R5_dai22mon_zu14_ayamari_hikaku')


def zu16():
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
    save(fig, [z], 'R5_dai22mon_zu16_1kai_kyuuseki')


def zu17():
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
    save(fig, [z], 'R5_dai22mon_zu17_2kai_kyuuseki')


def zu21():
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
    save(fig, [z, z2], 'R5_dai22mon_zu21_2kai_kouji_zengo')


def zu19():
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
    save(fig, zs, 'R5_dai22mon_zu19_kakukai_heimenzu')


def zu06():
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
    path = os.path.join(OUT, 'R5_dai22mon_zu06_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図1: 解く順番（固定配置）\n  →', path)




# ======================================================================
# 2026-10-26追加：最新の基準（6-2・6-3）で、わなの会話の直後に専用の図がなかった20か所の図（zu01〜05・08〜10・12・13・15・18・20・22〜28）。
# 座標を使わない固定配置の図は R7/Q22 の `card_figure()` と同じ作りで、`check_fixed` で文字の重なり・はみ出しを調べる。
# ======================================================================
from matplotlib.patches import FancyBboxPatch  # noqa: E402
from matplotlib.colors import to_rgba  # noqa: E402
from decimal import Decimal  # noqa: E402


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
    """固定配置の図の重なり検査（文字どうしの重なりと、図の外へのはみ出し）。"""
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


def card_figure(name, title, cols, bottom, w=17, h=9.5, top=84.0, line_step=8.6, fs=15, ha='center'):
    """左右（2〜3列）に並べる固定配置の比較カード。cols: [(見出し, 色, [行...])]。行の先頭が '*' なら太字・色つき。
    bottom: 図の下に書く文（最大2行）。ha='left' なら行を左寄せにする（長い一覧用）。"""
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
            ax.text(x0 + (cw / 2 if ha == 'center' else 2.0), y, t, ha=ha, va='top', fontsize=fs,
                    weight='bold' if bold else 'normal', color=col if bold else BLACK, linespacing=1.4)
            y -= line_step * k * 0.78 + 2.4
    if n == 2:
        vline(fig, 0.5, 0.10, 0.90)
    for k, t in enumerate(bottom):
        fig.text(0.5, 0.065 - 0.04 * k, t, ha='center', va='center', fontsize=15)
    save_fixed(fig, name)


def table_figure(name, title, heads, rows, colw, bottom, w=17, h=9.0, fs=14, row_cols=None):
    """固定配置の表。heads: 見出し、rows: [[セル, ...]]（セルは文字列、または (文字列, 色, 太字)）、colw: 列の幅（合計98）。
    row_cols: 行ごとの枠の色（None なら灰色）。bottom: 図の下に書く文。"""
    fig, ax = fixed_figure(title, w=w, h=h, rect=(0.02, 0.12, 0.96, 0.76))
    xs = [1.0]
    for c in colw:
        xs.append(xs[-1] + c)
    hh = 9.0
    for j, hd in enumerate(heads):
        ax.add_patch(Rectangle((xs[j], 100 - hh), colw[j], hh, facecolor=to_rgba(GRAY, 0.18), edgecolor=BLACK, lw=1.4))
        ax.text(xs[j] + colw[j] / 2, 100 - hh / 2, hd, ha='center', va='center', fontsize=fs + 1, weight='bold')
    n = len(rows)
    rh = (100 - hh - 1.0) / n
    for i, row in enumerate(rows):
        y1 = 100 - hh - i * rh
        col = (row_cols or [GRAY] * n)[i]
        for j, cell_ in enumerate(row):
            t, c, b = (cell_, BLACK, False) if isinstance(cell_, str) else cell_
            ax.add_patch(Rectangle((xs[j], y1 - rh), colw[j], rh, facecolor=to_rgba(col, 0.07), edgecolor=BLACK, lw=1.2))
            ax.text(xs[j] + 1.0, y1 - rh / 2, t, ha='left', va='center', fontsize=fs, color=c,
                    weight='bold' if b else 'normal', linespacing=1.35)
    for k, t in enumerate(bottom):
        fig.text(0.5, 0.075 - 0.04 * k, t, ha='center', va='center', fontsize=15)
    save_fixed(fig, name)


def zu01():
    card_figure('R5_dai22mon_zu01_gattai_gappei',
                '区分建物を区分建物でなくする登記は「合体」ではなく「合併」',
                [('誤り：「合体」と考える', RED,
                  ['合体＝工事で2つの建物が\n構造上1個の建物になること', '（不動産登記法第49条）', '',
                   '今回の工事は、1階と2階の間に\n木製の扉を付けて行き来できるようにしただけ', '',
                   '*構造上の独立性は失われないので\n「合体した」とはみなせない']),
                 ('正解：区分建物の「合併」', GREEN,
                  ['壁や床で区切られた2つの区分建物のまま、\n木製の扉でつながっただけ', '所有者は同じで、互いに接続している', '',
                   '*区分建物の合併の登記', '（不動産登記法第54条第1項第3号）', '',
                   '登記の目的：\n区分建物表題部変更・合併登記'])],
                ['問1の答え：ア＝合併、イ＝構造上の独立性、ウ＝合体（「ウ」に「合併」を入れると説明の筋が逆になる）'], h=6.4)


def zu02():
    card_figure('R5_dai22mon_zu02_gappei_seigen',
                '合併できない場合に当たらないか、3つを確かめる',
                [('所有者が同じか\n（法第56条第2号）', BLUE,
                  ['3番9の1・3番9の2とも\n所有権の登記名義人は甲田栄一', '', '*相互に異ならない\n→ 制限に当たらない']),
                 ('所有権以外の権利の登記がないか\n（同条第5号）', BLUE,
                  ['甲区は所有権保存だけ', '乙区に登記は存在しない', '', '*所有権等の登記以外の\n権利に関する登記はない\n→ 制限に当たらない']),
                 ('互いに接続しているか\n（準則第86条第2号）', BLUE,
                  ['主たる建物と附属建物の\n関係にはないが、', '壁を共有して接続している', '', '*接続している\n→ 制限に当たらない'])],
                ['どれか1つでも当たると区分建物の合併はできない。本問は3つとも当たらないので、合併の登記ができる',
                 '問1の答え：エ＝権利、オ＝接続'], h=6.0, fs=14)


def zu04():
    table_figure('R5_dai22mon_zu04_kouji_shiwake',
                 '事実関係4の工事(1)〜(5)を、登記にどう響くかで仕分ける',
                 ['工事', '登記事項への響き', '申請書での扱い'],
                 [['(1) 施錠できる木製の扉を設置', '構造上の独立性は失われない', ('合併を選ぶ根拠（原因には書かない）', BLUE, False)],
                  ['(2) バルコニーの一部を増築して\n　　リビングを拡張（軽量鉄骨造）', '床面積が増える', ('③床面積の変更＝原因に「増築」', RED, True)],
                  ['(3) 2階の間取りの変更', '間取りは登記事項ではない', ('何も書かない', GRAY, False)],
                  ['(4) 陸屋根をスレートぶきの\n　　勾配屋根に変更', '構造（屋根の種類）が変わる', ('②構造の変更＝原因に「構造変更」', RED, True)],
                  ['(5) 屋根裏部屋の設置\n　　（天井の最高部1.40メートル）', '床面積にも階数にも入らない', ('何も書かない（描かない）', GRAY, False)]],
                 [30, 30, 38],
                 ['原因は「②③令和5年10月6日構造変更、増築、3番9の2を合併」。②構造と③床面積が変わり、(4)(2)が原因になる'],
                 h=8.6, fs=14, row_cols=[BLUE, RED, GRAY, RED, GRAY])


def zu03():
    fig, ax = fixed_figure('屋根裏部屋は天井の最高部1.40メートルなので、床面積にも階数にも入れない', w=17, h=8.2,
                           rect=(0.02, 0.12, 0.96, 0.76))
    # 左：屋根裏部屋の断面の模式（事実関係4(5)の断面図）
    rbox(ax, 1, 4, 46, 90, GRAY, alpha=0.06)
    ax.text(24, 88, '屋根裏部屋（断面の模式）', ha='center', va='center', fontsize=17, weight='bold')
    ax.add_patch(MPoly([(6, 20), (42, 20), (24, 68)], closed=True, fill=False, ec=BLACK, lw=2.2))
    ax.add_patch(Rectangle((16, 20), 16, 17, facecolor=to_rgba(ORANGE, 0.25), edgecolor=ORANGE, lw=2))
    ax.text(24, 28.5, '屋根\n裏部屋', ha='center', va='center', fontsize=14)
    ax.annotate('', xy=(35, 37), xytext=(35, 20), arrowprops=dict(arrowstyle='<|-|>', color=RED, lw=2, shrinkA=0, shrinkB=0))
    ax.text(36.5, 28.5, '1.40', ha='left', va='center', fontsize=17, color=RED, weight='bold',
            bbox=dict(fc='white', ec='none', pad=1.5))
    ax.text(24, 11, '床面から天井の最高部までの高さ＝1.40メートル', ha='center', va='center', fontsize=13)
    # 右：判定
    rbox(ax, 51, 4, 48, 90, GREEN, alpha=0.08)
    ax.text(75, 88, '判定', ha='center', va='center', fontsize=17, weight='bold', color=GREEN)
    ax.text(75, 74, '1.40メートル ＜ 1.50メートル', ha='center', va='center', fontsize=20, weight='bold', color=RED)
    ax.text(75, 58, '床面積に算入しない\n（不動産登記事務取扱手続準則第82条第1号）', ha='center', va='center', fontsize=15, linespacing=1.5)
    ax.text(75, 40, '階数にも算入しない\n（同準則第81条第4項）', ha='center', va='center', fontsize=15, linespacing=1.5)
    ax.text(75, 20, '2階建のまま。各階平面図にも描かない', ha='center', va='center', fontsize=15, weight='bold', color=GREEN)
    fig.text(0.5, 0.06, '3階として数えたり、屋根裏部屋の面積を足したりしたら、床面積も構造（階数）も誤りになる', ha='center', fontsize=15)
    save_fixed(fig, 'R5_dai22mon_zu03_yaneura_fusanyuu')


def zu05():
    card_figure('R5_dai22mon_zu05_chuu_shiwake',
                '注は2種類。番号がかぶるので「問題文の注」「〔調査図〕の（注）」と言い分ける',
                [('問題文の注1〜5', BLUE,
                  ['注1　適法に行われた', '注2　書面申請', '注3　縮尺：建物図面1/500、各階平面図1/250',
                   '*注4　距離の桁：各階平面図は小数点以下第2位、\n　　　建物図面は小数点第1位まで', '注5　字画を明瞭に、訂正の仕方']),
                 ('〔調査図〕の（注）1〜10', GREEN,
                  ['（注）1　距離の単位はメートル',
                   '*（注）2　配置図の数値＝筆界から外壁まで、\n　　　　平面図の数値＝柱又は壁の中心間',
                   '*（注）3　鉄骨は両側が被覆、壁の厚さ0.15',
                   '（注）4　隅部は全て直角', '（注）5　△・○印＝各階の重なっている部分',
                   '（注）6　括弧内は地番　（注）7　A〜Dは筆界点', '（注）8　北はX軸の正方向',
                   '（注）9　工事前の寸法は備付けの図面と合致', '（注）10　工事完了後の各階平面図'])],
                ['太字が決め手：問題文の注4（桁）、〔調査図〕の（注）2（外壁まで／中心間）と（注）3（両側被覆）'],
                h=9.0, fs=13, line_step=6.4, ha='left')


def zu08():
    card_figure('R5_dai22mon_zu08_kyori_keta',
                '距離の桁は図面で違う：建物図面は第1位、各階平面図は第2位（問題文の注4）',
                [('建物図面（縮尺 1/500）', BLUE,
                  ['調査図の距離　2.00・2.00・2.90', '', '*小数点第1位まで', '', '2.0　　2.0　　2.9', '',
                   '「2.00」「2.90」のまま書くと\n問題文の注4に反する']),
                 ('各階平面図（縮尺 1/250）', GREEN,
                  ['寸法は壁の中心線の間', '', '*小数点以下第2位まで', '',
                   '1階：6.40　2.80　0.90　9.00　7.30　11.80', '2階：7.30　12.70　2.70　0.90　4.60　11.80', '',
                   '「7.3」「9」と省いて書くと\n問題文の注4に反する'])],
                ['同じ「距離」でも、図面ごとに桁を使い分ける（問題文の注4）'], h=6.4)


def zu10():
    card_figure('R5_dai22mon_zu10_kakumono_kakanaimono',
                '建物図面に書くもの・書かないもの',
                [('書くもの', GREEN,
                  ['建物の所在　A市B町一丁目3番地9', '本件土地の地番（3-9）と、隣接地・道路の地番', '1階の外形（座標どおりの敷地の中）',
                   '筆界から外壁までの距離　2.0・2.0・2.9', '方位']),
                 ('書かないもの', RED,
                  ['敷地の辺長（AB18.0mなど。作図チェック用）', '家屋番号（合併後の建物は登記所が付ける）\n→ 欄は空欄', '',
                   '申請人の氏名と縮尺\n（「（略）」「1／500」は印刷済み）'])],
                ['建物図面は第3欄の1枚の用紙の右半分。家屋番号と建物の所在の欄は各階平面図と兼用'], h=6.2)


def zu09():
    """所在の確認：建物の外壁の位置を座標で出し、3番9の中におさまることを確かめる。"""
    fig, axes = new_figure('建物は3番9の中におさまる（所在は3番地9だけ）',
                           '外壁の位置＝筆界から外壁までの距離（調査図の図1）。外壁は壁の中心線から0.075外側。余白の距離は座標から計算した概数',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(SITE, color=BLACK, lw=2.4, fill=BLUE, alpha=0.08)
    ext = [(-HALF, -HALF), (6.4 + HALF, -HALF), (6.4 + HALF, 2.8 - HALF), (7.3 + HALF, 2.8 - HALF), (7.3 + HALF, 11.8 + HALF),
           (-HALF, 11.8 + HALF)]
    bld = [B_(*v) for v in ext]
    z.poly(bld, color=BLACK, lw=2.4, fill=ORANGE, alpha=0.35)
    # 外壁の位置（座標）
    x_n, x_s = N0 + HALF, S_EXT                       # 北・南の外壁のX
    y_w, y_e = W0 - HALF, Y_CD - 2.90                 # 西・南東の角の東の外壁のY
    assert abs(x_n - 66.00) < 1e-9 and abs(x_s - 54.05) < 1e-9
    # 余白（辺ABまで、辺ADまで）
    gap_w = y_w - 75.00                               # 辺ABまで
    # 辺ADはA(50,75)→D(52,88)：南東の角の東西位置 y_e での辺AD上のX
    x_ad = 50 + (y_e - 75) * (52 - 50) / (88 - 75)
    gap_s = x_s - x_ad                                # 南東の角から辺ADまで（いちばん狭い）
    assert 2.4 < gap_s < 2.6 and 2.8 < gap_w < 2.9
    dist_arrow(z, complex(x_n, y_w + 0.3), complex(68, y_w + 0.3), '2.0', side=(-16, 0))
    dist_arrow(z, complex(x_n, y_e - 0.9), complex(68, y_e - 0.9), '2.0', side=(16, 0))
    dist_arrow(z, complex(x_s, y_e), complex(x_s, Y_CD), '2.9', side=(0, -14))
    dist_arrow(z, complex(60.0, y_w), complex(60.0, 75.0), f'約{gap_w:.1f}', side=(0, 14), fs=14)
    dist_arrow(z, complex(x_s, y_e), complex(x_ad, y_e), f'約{gap_s:.1f}', side=(-30, 0), fs=14)
    c = centroid(SITE)
    for p, n in zip(SITE, 'ABCD'):
        z.point_label(p, n, away=c, fs=18)
    z.free_text(complex(60.0, 81.5), '1階', fs=16)
    fit(ax, SITE, margin=0.08, extra=[xy(complex(48, 72)), xy(complex(70, 91))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R5_dai22mon_zu09_shozai_kakunin')


def zu12():
    fig, ax = fixed_figure('区分建物でなくなると、床面積の測り方が「壁の内側」から「壁の中心線」に変わる', w=17, h=8.8,
                           rect=(0.02, 0.12, 0.96, 0.76))
    # 左：壁の断面（内法と壁心）
    rbox(ax, 1, 4, 46, 90, GRAY, alpha=0.06)
    ax.text(24, 88, '壁の断面（壁の厚さ0.15）', ha='center', va='center', fontsize=17, weight='bold')
    ax.add_patch(Rectangle((19, 22), 10, 56, facecolor=to_rgba(GRAY, 0.35), edgecolor=BLACK, lw=2))
    ax.plot([24, 24], [18, 82], color=RED, lw=2, ls='--')
    ax.plot([19, 19], [18, 82], color=BLUE, lw=2, ls=':')
    ax.text(24, 13, '壁の中心線\n（壁心）', ha='center', va='center', fontsize=13, color=RED, linespacing=1.3)
    ax.text(8, 50, '室内\n（壁の内側）', ha='center', va='center', fontsize=14)
    ax.text(39, 50, '外', ha='center', va='center', fontsize=14)
    ax.annotate('', xy=(24, 70), xytext=(19, 70), arrowprops=dict(arrowstyle='<|-|>', color=BLACK, lw=1.6, shrinkA=0, shrinkB=0))
    ax.text(21.5, 73.5, '0.075', ha='center', va='center', fontsize=13)
    ax.text(10, 83, '壁の内側線（内法）', ha='center', va='center', fontsize=13, color=BLUE)
    # 右：数値
    rbox(ax, 51, 4, 48, 90, GREEN, alpha=0.08)
    ax.text(75, 88, '登記記録と、合併後の床面積', ha='center', va='center', fontsize=17, weight='bold', color=GREEN)
    ax.text(75, 74, '区分建物（壁の内側線）', ha='center', va='center', fontsize=15, weight='bold', color=BLUE)
    ax.text(75, 64, '3番9の1　1階部分 4.61　2階部分 70.21\n3番9の2　1階部分 74.72', ha='center', va='center', fontsize=15, linespacing=1.5)
    ax.text(75, 49, '合併後の建物（壁の中心線）', ha='center', va='center', fontsize=15, weight='bold', color=RED)
    ax.text(75, 40, '1階 83.62　2階 88.57', ha='center', va='center', fontsize=18, weight='bold')
    ax.text(75, 24, '区分建物の床面積は壁の内側線、区分建物でない建物は壁の中心線\n（不動産登記規則第115条）', ha='center', va='center',
            fontsize=14, linespacing=1.5)
    fig.text(0.5, 0.06, '登記記録の4.61・70.21・74.72を足したり引いたりして83.62・88.57を出すことはできない。図面の寸法から壁心で測り直す',
             ha='center', fontsize=15)
    save_fixed(fig, 'R5_dai22mon_zu12_uchinori_kabeshin')


def zu13():
    fig, ax = fixed_figure('鉄骨が両側とも被覆されていれば、図面の数値＝壁の中心線の寸法（〔調査図〕の（注）2・3）', w=17, h=8.8,
                           rect=(0.02, 0.12, 0.96, 0.76))
    for x0, ttl, col, off in [(1, '本問：鉄骨は両側が被覆', GREEN, 0), (51, '（参考）片側だけが被覆なら', RED, 3.0)]:
        rbox(ax, x0, 4, 48, 90, col, alpha=0.07)
        ax.text(x0 + 24, 88, ttl, ha='center', va='center', fontsize=17, weight='bold', color=col)
        cx = x0 + 24
        ax.add_patch(Rectangle((cx - 9, 32), 18, 40, facecolor=to_rgba(GRAY, 0.30), edgecolor=BLACK, lw=2))      # 壁（被覆を含む）
        ax.add_patch(Rectangle((cx - 3 + off, 40), 6, 24, facecolor=to_rgba(BLUE, 0.55), edgecolor=BLUE, lw=1.5))  # 鉄骨
        ax.plot([cx + off, cx + off], [25, 77], color=BLUE, lw=2, ls='--')
        ax.plot([cx, cx], [25, 77], color=RED, lw=2, ls=':')
        ax.text(cx - 11, 52, '被覆', ha='right', va='center', fontsize=13)
        ax.text(cx + 11, 52, '被覆', ha='left', va='center', fontsize=13)
        ax.text(cx + off, 20.5, '鉄骨の中心', ha='center', va='center', fontsize=12, color=BLUE)
        if off:
            ax.text(cx - 3, 80.5, '壁の中心', ha='center', va='center', fontsize=12, color=RED)
    ax.text(25, 11, '鉄骨の中心＝壁の中心\n→ 図面の数値がそのまま壁の中心線の寸法', ha='center', va='center', fontsize=14,
            weight='bold', color=GREEN, linespacing=1.4)
    ax.text(75, 11, '鉄骨の中心と壁の中心がずれる\n→ ずれの分を直す必要がある', ha='center', va='center', fontsize=14,
            weight='bold', color=RED, linespacing=1.4)
    fig.text(0.5, 0.06, '壁の厚さ0.15は被覆を含む壁全体の厚さ。本問は両側被覆なので、0.15や0.075を足し引きせず、図面の数値を足すだけ',
             ha='center', fontsize=15)
    save_fixed(fig, 'R5_dai22mon_zu13_ryougawa_hifuku')


def zu15():
    fig, axes = new_figure('2階の寸法は、4辺とも自分で足し算してから拾う',
                           '東側だけ3.71＋3.59＋5.40＝12.70で、西側の11.80より0.90長い。「1階と同じ枠」と思い込むと2階の形を間違える',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    f2 = [P(*v) for v in F2]
    z.poly(f2, color=BLACK, lw=2.6, fill=BLUE, alpha=0.10)
    chains = {'北': ('3.64＋3.66', '7.30', (3.64, 3.66), 7.30), '南': ('2.73＋1.87＋2.70', '7.30', (2.73, 1.87, 2.70), 7.30),
              '西': ('2.80＋4.50＋4.50', '11.80', (2.80, 4.50, 4.50), 11.80), '東': ('3.71＋3.59＋5.40', '12.70', (3.71, 3.59, 5.40), 12.70)}
    for k, (_, tot, parts, want) in chains.items():
        assert sum(Decimal(str(x)) for x in parts) == Decimal(str(want)), k
    z.free_text(P(3.65, -1.25), '北　3.64＋3.66＝7.30', fs=15)
    z.free_text(P(3.65, 13.6), '南　2.73＋1.87＋2.70＝7.30', fs=15)
    z.free_text(P(-2.0, 5.9), '西\n2.80\n＋4.50\n＋4.50\n＝11.80', fs=15)
    z.free_text(P(9.8, 6.35), '東\n3.71\n＋3.59\n＋5.40\n＝12.70', fs=15, color=RED, weight='bold')
    z.callout(P(5.95, 12.25), '東側だけ南へ0.90\n張り出している', dirs=(-20, -40, 10), fs=14, color=RED)
    fit(ax, f2, margin=0.2, extra=[xy(P(-4.5, -2)), xy(P(12.5, 14.6))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R5_dai22mon_zu15_2kai_sunpou_tashizan')


def zu18():
    fig, axes = new_figure('2階の図に重ねる1階の位置（点線）は2か所',
                           '重ね方の基準は○（北西の角）と△（南西の角）＝各階の重なっている部分（〔調査図〕の（注）5）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    f2 = [P(*v) for v in F2]
    z.poly(f2, color=BLACK, lw=2.6)
    z.line(P(6.4, 0), P(6.4, 2.8), color=RED, lw=2.4, ls=':')
    z.line(P(6.4, 2.8), P(7.3, 2.8), color=RED, lw=2.4, ls=':')
    z.line(P(4.6, 11.8), P(7.3, 11.8), color=RED, lw=2.4, ls=':')
    z.callout(P(6.85, 1.4), '①北東の欠け\n（1階は玄関前）', dirs=(20, 40, 0), fs=14, color=RED)
    z.callout(P(6.0, 11.8), '②1階の南の壁\n（2階の東側は0.90南へ張り出す）', dirs=(-20, -40, 20), fs=14, color=RED)
    ax.plot(*xy(P(0, 0)), marker='o', ms=16, mfc='none', mec=BLACK, mew=2.2, zorder=7)
    ax.plot(*xy(P(0, 11.8)), marker='^', ms=16, mfc='none', mec=BLACK, mew=2.2, zorder=7)
    z.free_text(P(-1.3, 0), '○', fs=15)
    z.free_text(P(-1.3, 11.8), '△', fs=15)
    fit(ax, f2, margin=0.2, extra=[xy(P(-3.0, -2)), xy(P(14.5, 14.6))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R5_dai22mon_zu18_1kai_no_ichi')


def zu20():
    fig, ax = fixed_figure('一棟の建物の表示は「工事前」の登記記録を写し、省略された床面積は自分で出す', w=17, h=8.8,
                           rect=(0.02, 0.12, 0.96, 0.76))
    rbox(ax, 1, 4, 46, 90, GRAY, alpha=0.06)
    ax.text(24, 88, '登記記録（一棟の建物の表示）', ha='center', va='center', fontsize=17, weight='bold')
    rows = [('所在', 'A市B町一丁目3番地9', 'そのまま写す', BLUE), ('①構造', '軽量鉄骨造陸屋根2階建', 'スレートぶきに直さない', BLUE),
            ('②床面積', '1階　省略\n2階　省略', '自分で計算して埋める', RED)]
    y = 76
    for head, body, state, col in rows:
        k = body.count('\n') + 1
        h = 8 + 7 * k
        ax.add_patch(Rectangle((3, y - h), 42, h, fill=False, ec=GRAY, lw=1.2))
        ax.text(5, y - 5, head, ha='left', va='center', fontsize=14)
        ax.text(5, y - h + 3, body, ha='left', va='bottom', fontsize=14, color=GRAY, linespacing=1.4)
        ax.text(43, y - 5, state, ha='right', va='center', fontsize=13, color=col, weight='bold')
        y -= h + 3
    rbox(ax, 51, 4, 48, 90, GREEN, alpha=0.08)
    ax.text(75, 88, '申請書に書く値', ha='center', va='center', fontsize=17, weight='bold', color=GREEN)
    ax.text(75, 74, '1階　83.62', ha='center', va='center', fontsize=20, weight='bold')
    ax.text(75, 64, '1階は形が変わらないので\n工事完了後の求積と同じ', ha='center', va='center', fontsize=14, linespacing=1.4)
    ax.text(75, 47, '2階　73.99', ha='center', va='center', fontsize=20, weight='bold', color=RED)
    ax.text(75, 37, '増築の前の図（図2【工事前】）の寸法で\n7.30×7.30＋4.60×4.50', ha='center', va='center', fontsize=14,
            linespacing=1.4)
    ax.text(75, 20, '工事完了後の88.57ではない', ha='center', va='center', fontsize=15, weight='bold', color=RED)
    fig.text(0.5, 0.06, '一棟の建物の表示の「原因及びその日付」の欄は書かない（解答例どおり）', ha='center', fontsize=15)
    assert Decimal('7.30') * Decimal('7.30') + Decimal('4.60') * Decimal('4.50') == Decimal('73.99')
    save_fixed(fig, 'R5_dai22mon_zu20_ittou_hyouji')


def zu22():
    table_figure('R5_dai22mon_zu22_tenpu_shorui',
                 '添付書類は6点。それぞれ何のために要るか',
                 ['書類', '根拠', '本問で要る理由'],
                 [['建物図面', '令別表14の項添付情報欄ロ、\n16の項添付情報欄イ', '床面積が変わる表題部の変更の登記にも、\n合併の登記にも要る'],
                  ['各階平面図', '同上', '同上'],
                  ['登記識別情報', '不動産登記令第8条第1項第3号', '所有権の登記がある建物の合併だから'],
                  ['印鑑証明書', '令第16条第2項、\n不動産登記規則第47条第3号イ（6）', '合併の登記を申請する所有権の登記名義人が\n申請書に記名押印するから'],
                  ['所有権証明書', '令別表14の項添付情報欄ロ（2）', '増えた床面積の部分も甲田栄一のものだと\n証明するため（乙山建設が書類一式を交付）'],
                  ['代理権限証書', '令第7条第1項第2号', '土地家屋調査士法務太郎が代理して申請するから']],
                 [16, 38, 44],
                 ['6点そろえて「建物図面　各階平面図　登記識別情報　印鑑証明書　所有権証明書　代理権限証書」と書く'],
                 h=9.6, fs=13, row_cols=[BLUE, BLUE, GREEN, GREEN, RED, GRAY])


def zu23():
    card_figure('R5_dai22mon_zu23_toukishikibetsu',
                '登記識別情報は、合併する建物のうち1個の分で足りる',
                [('誤り：2つとも出す', RED,
                  ['3番9の1の登記識別情報', '3番9の2の登記識別情報', '', '*2通ぶん付けなくてもよい']),
                 ('正解：どれか1個の分で足りる', GREEN,
                  ['合併に係る建物のうち、\nどれか1個の建物の分でよい', '（不動産登記令第8条第2項第3号）', '',
                   '事実関係6：本件各区分建物の\n登記識別情報を保有している', '',
                   '*申請書には「登記識別情報」とだけ書く'])],
                ['1通で足りるかどうかに迷っても、保有しているので本問では困らない。書き方は「登記識別情報」だけ'], h=6.2)


def zu24():
    card_figure('R5_dai22mon_zu24_touroku_menkyozei',
                '登録免許税は「不要」ではなく「金1,000円」',
                [('誤り：表示に関する登記だから「不要」', RED,
                  ['問2のただし書きの「不要」は、', '納付が要らない場合の書き方の指示', '',
                   '本問は納付が要るので、使わない']),
                 ('正解：合併後の建物1個につき1,000円', GREEN,
                  ['表題部の変更の登記：かからない', '所有権の登記のある建物の合併の登記：', '合併後の不動産の個数 × 1,000円',
                   '（登録免許税法別表第一の一（十三）ロ）', '', '合併後の建物は1個', '*→ 金1,000円'])],
                ['申請人は所有権の登記名義人本人（甲田栄一）。合併後は1個なので、1,000円×1個'], h=6.4)


def zu25():
    card_figure('R5_dai22mon_zu25_kubun_3gyou',
                '「区分した建物の表示」は3行。消える2行は壁心に直さず、登記記録のとおりに写す',
                [('1行目　3番9の1', BLUE,
                  ['家屋番号　B町一丁目3番9の1', '①居宅', '②軽量鉄骨造2階建', '③1階部分 4.61　2階部分 70.21', '', '*内法のまま写す', '原因：空欄']),
                 ('2行目　合併後の建物', GREEN,
                  ['家屋番号：書かない（印刷の「（省略）」）', '①居宅', '②軽量鉄骨造スレートぶき2階建', '③1階 83.62　2階 88.57', '',
                   '*壁心・「1階」「2階」', '原因：②③令和5年10月6日\n構造変更、増築、3番9の2を合併']),
                 ('3行目　3番9の2', BLUE,
                  ['家屋番号　B町一丁目3番9の2', '①居宅', '②軽量鉄骨造1階建', '③1階部分 74.72', '', '*内法のまま写す',
                   '原因：3番9の1に合併'])],
                ['1行目・3行目は登記記録の行を写すだけ。壁心に直すのは2行目（合併後の建物）だけ'], h=8.4, fs=13)


def zu26():
    card_figure('R5_dai22mon_zu26_shurui_kyotaku',
                '種類は「共同住宅」ではなく「居宅」',
                [('誤り：二世帯住宅＝共同住宅', RED,
                  ['ふた家族が住んでいるから', '「共同住宅」', '', '*住んでいる世帯の数で\n決めるのではない']),
                 ('正解：主な用途で決めて「居宅」', GREEN,
                  ['建物の種類は主な用途で決める\n（不動産登記規則第113条第1項）', '',
                   '共同住宅＝玄関が別々の独立した住戸が\nいくつも入っている建物', '',
                   '合併後は、木製の扉で行き来できる\n甲田さん一家の1つの住まい', '', '*居宅'])],
                ['合併後の建物の「①種類」は居宅のまま。構造は「軽量鉄骨造スレートぶき2階建」と屋根の種類まで書く'], h=6.6)


def zu27():
    card_figure('R5_dai22mon_zu27_shikichiken_fuyou',
                '敷地権の登記がないので、敷地権の2つの欄は「記載不要」',
                [('登記記録の事実', BLUE,
                  ['本件土地は甲田栄一が1人で所有', '本来は専有部分と敷地利用権は\n分離して処分できず、敷地権になる',
                   '（区分所有法第22条第1項本文・第3項）', '', '登記記録に敷地権の記録がない\n＝規約で分離処分できるとした',
                   '（同条第1項ただし書）']),
                 ('申請書の書き方', GREEN,
                  ['敷地権の表示に関する登記の申請が\n不要な場合（問2のただし書き）', '', '*「敷地権の目的である土地の表示」と\n「敷地権の表示」の\n「原因及びその日付」の欄に',
                   '*「記載不要」と書く', '', '他の欄（符号・地目・地積・種類・割合）は空欄'])],
                ['答案用紙の2つの欄の「原因及びその日付」に、それぞれ「記載不要」と書く'], h=6.8)


def zu28():
    card_figure('R5_dai22mon_zu28_kiyaku_shoumeisho',
                '問4：敷地権のない状態で表題登記をするなら、規約証明書を提供する',
                [('分離処分できないはずの原則', RED,
                  ['敷地利用権が数人で有する権利なら、\n専有部分と敷地利用権は分離して処分できない', '（区分所有法第22条第1項本文）', '',
                   '単独所有でも専有部分の全部を所有する者に準用', '（同条第3項）', '', '*原則どおりなら敷地権として登記される']),
                 ('敷地権が記録されていない理由', GREEN,
                  ['規約に別段の定め（同条第1項ただし書）', '＝専有部分と敷地利用権を\n分離して処分することができる', '',
                   '*その規約を証する「規約証明書」を\n表題登記の申請時に提供していた',
                   '（不動産登記令別表12の項添付情報欄ホ）'])],
                ['問4の答え：①規約証明書、②敷地権、③敷地利用権、④分離、⑤処分'], h=6.8)


if __name__ == '__main__':
    for f in (zu01, zu02, zu03, zu04, zu05, zu06, zu07, zu08, zu09, zu10, zu11, zu12, zu13, zu14, zu15, zu16, zu17, zu18,
              zu19, zu20, zu21, zu22, zu23, zu24, zu25, zu26, zu27, zu28):
        f()
    print('重なり合計:', len(PROBLEMS))
