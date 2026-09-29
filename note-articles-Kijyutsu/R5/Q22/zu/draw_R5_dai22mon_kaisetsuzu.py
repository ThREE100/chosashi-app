"""令和5年度 第22問（建物）の解説図6枚を、座標値・頂点座標から作図してPNGに書き出す。

`../prompt_R5_dai22mon_kaisetsuzu.md` の図1〜図6どおり。作図の共通部品は `tools/zu_helpers.py`。
敷地は〔座標値一覧表〕の (X＝北, Y＝東)。建物の平面は (東, 南)（原点＝建物の北西の角の壁の中心）で持ち、
zu_helpers の (北, 東) には B() で変換する。
実行: python3 note-articles-Kijyutsu/R5/Q22/zu/draw_R5_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly  # noqa: E402

from zu_helpers import Zu, new_figure, fit, xy, centroid, BLACK, GRAY, RED, BLUE, ORANGE, GREEN  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []

# ---- 敷地（〔座標値一覧表〕） ----
A, B, C, D = complex(50, 75), complex(68, 75), complex(68, 89.5), complex(52, 88)
SITE = [A, B, C, D]
D_RECT = complex(50, 89.5)   # 図1の見た目のまま長方形と思い込んだときのD点

# ---- 建物の位置（壁厚0.15、筆界からの距離は外壁まで〈注2・注3〉。壁の中心線は外壁から0.075内側） ----
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


def zu01():
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
    save(fig, [z], 'R5_dai22mon_zu01_shikichi_henchou')


def zu02():
    fig, axes = new_figure('建物図面（縮尺500分の1）の完成形',
                           '敷地は座標どおり（辺AD・辺CDは斜め）。建物は1階の形。距離は外壁まで、小数点第1位（注4）。敷地の辺長は書かない',
                           w=16, h=11.5)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(SITE, color=BLACK, lw=2.2)
    bldg = [B_(*v) for v in F1]
    z.poly(bldg, color=BLACK, lw=2.4, fill=ORANGE, alpha=0.25)
    # 距離（外壁まで）：北の2か所（西端・東端）は辺BCまで、南東の角は辺CDまで（東西方向）
    n_ext = N0 + HALF
    for e in (0, 6.4):
        y = W0 + e + (-HALF if e == 0 else HALF)
        dist_arrow(z, complex(n_ext, y), complex(68, y), '2.0', side=(-16 if e == 0 else 16, 0))
    se = complex(S_EXT, W0 + 7.3 + HALF)
    dist_arrow(z, se, complex(S_EXT, Y_CD), '2.9', side=(0, -14))
    z.free_text(complex(60, (W0 + W0 + 7.3) / 2), '本件各区分建物\n（1階）', fs=15)
    OFFS = ((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0))
    z.free_text(complex(52.55, 79.5), '3-9', fs=17, offsets=OFFS)
    for p, t in [(complex(69.6, 73.2), '3-12'), (complex(69.4, 82.0), '3-11'), (complex(60.0, 73.2), '3-10'),
                 (complex(60.0, 90.6), '1-1\n道路'), (complex(49.6, 81.5), '3-1　道路')]:
        z.free_text(p, t, fs=15, color=GRAY, offsets=OFFS)
    fit(ax, SITE, margin=0.1, extra=[xy(complex(48, 71)), xy(complex(71, 92))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R5_dai22mon_zu02_tatemono_zumen')


def zu03():
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
    save(fig, [z, z2], 'R5_dai22mon_zu03_ayamari_hikaku')


def zu04():
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
    z.callout(P(6.85, 7.3), '東側（和室・LDK側）\n0.90×9.00＝8.10', dirs=(0, -20, 20), fs=15)
    z.callout(P(6.85, 1.4), '玄関前（建物の外）', dirs=(20, 40, 0), fs=14, color=GRAY)
    z.free_text(P(3.65, -2.2), '1階 床面積：83.62㎡', fs=18, weight='bold')
    fit(ax, f1, margin=0.2, extra=[xy(P(3.65, -2.8)), xy(P(14, 12))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R5_dai22mon_zu04_1kai_kyuuseki')


def zu05():
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
    save(fig, [z], 'R5_dai22mon_zu05_2kai_kyuuseki')


def zu06():
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
    save(fig, [z, z2], 'R5_dai22mon_zu06_2kai_kouji_zengo')


if __name__ == '__main__':
    zu01()
    zu02()
    zu03()
    zu04()
    zu05()
    zu06()
    print('重なり合計:', len(PROBLEMS))
