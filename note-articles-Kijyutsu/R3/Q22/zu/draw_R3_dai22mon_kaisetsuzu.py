"""令和3年度 第22問（建物）の解説図7枚を、頂点座標から作図してPNGに書き出す。

`../prompt_R3_dai22mon_kaisetsuzu.md` の図1〜図7どおり。作図の共通部品は `tools/zu_helpers.py`。
建物の座標は (東, 南) で持ち（原点は一棟の建物の北西の角の、壁の中心線の交点）、zu_helpers の (北, 東) には
B() で変換する（北 ＝ −南）。図7だけは（ロ）部分の北西の角（一棟の建物の座標では東8.00）を原点にする。
敷地は座標値一覧表がないので、図1の辺長から組み立てた座標（西側の線を東0、南側の線を北0）を使う。
実行: python3 note-articles-Kijyutsu/R3/Q22/zu/draw_R3_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, BLACK, GRAY, RED, BLUE, ORANGE, GREEN,  # noqa: E402
                        PURPLE)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []
YELLOW = '#e0b000'


def B(e, s):
    """建物の (東, 南) を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(-s, e)


def P(pts, de=0.0, ds=0.0):
    return [B(e + de, s + ds) for e, s in pts]


def rect(e0, s0, e1, s1):
    return [(e0, s0), (e1, s0), (e1, s1), (e0, s1)]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


def area_es(pts):
    return area(P(pts))


def hatch(ax, pts, color=GRAY):
    ax.add_patch(MPoly([xy(p) for p in pts], closed=True, fill=False, hatch='///', edgecolor=color, lw=0, zorder=1))


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


# ---- 建物（図3・図4の寸法線から。壁心は鉄骨の柱又は壁の中心、内法は中心から0.10内側） ----
WHOLE1 = [(0, 0), (6.5, 0), (6.5, 1), (9.5, 1), (9.5, 0), (16, 0), (16, 11), (0, 11)]   # 一棟の1階（壁心）
WHOLE2 = rect(0, 0, 16, 11)                                                                # 一棟の2階（壁心）
I1_WALL = [(0, 0), (6.5, 0), (6.5, 1), (8, 1), (8, 11), (0, 11)]                           # （イ）1階の壁心
I1 = [(0.1, 0.1), (6.4, 0.1), (6.4, 1.1), (7.9, 1.1), (7.9, 10.9), (0.1, 10.9)]            # （イ）1階の内法
I1_STRIPS = [rect(0.1, 0.1, 6.4, 1.1), rect(0.1, 1.1, 7.9, 10.9)]
I2 = rect(0.1, 0.1, 7.9, 10.9)                                                             # （イ）2階の内法
RO1_WALL = [(8, 1), (9.5, 1), (9.5, 0), (16, 0), (16, 11), (8, 11)]                        # （ロ）1階の壁心
# 図7：（ロ）部分の座標（原点は（ロ）部分の北西の角）
R1_WALL = [(0, 1), (1.5, 1), (1.5, 0), (8, 0), (8, 11), (0, 11)]
A_PART = [(0.1, 1.1), (1.6, 1.1), (1.6, 0.1), (7.9, 0.1), (7.9, 6.4), (5.2, 6.4), (5.2, 9.6), (5.9, 9.6),
          (5.9, 10.9), (0.1, 10.9)]
A_STRIPS = [rect(1.6, 0.1, 7.9, 1.1), rect(0.1, 1.1, 7.9, 6.4), rect(0.1, 6.4, 5.2, 9.6), rect(0.1, 9.6, 5.9, 10.9)]
MARU_A = [(5.4, 6.6), (7.9, 6.6), (7.9, 10.9), (6.1, 10.9), (6.1, 9.4), (5.4, 9.4)]
MARU_STRIPS = [rect(5.4, 6.6, 7.9, 9.4), rect(6.1, 9.4, 7.9, 10.9)]
MARU_A_WALL = [(5.3, 6.5), (8, 6.5), (8, 11), (6, 11), (6, 9.5), (5.3, 9.5)]
A_WALL = [(0, 1), (1.5, 1), (1.5, 0), (8, 0), (8, 6.5), (5.3, 6.5), (5.3, 9.5), (6, 9.5), (6, 11), (0, 11)]

assert area_es(WHOLE1) == 173.00 and area_es(WHOLE2) == 176.00
assert area_es(I1_WALL) == 86.50 and area_es(RO1_WALL) == 86.50
assert round(area_es(I1), 2) == 82.74 == round(sum(area_es(r) for r in I1_STRIPS), 2)
assert round(area_es(I2), 2) == 84.24
assert round(area_es(A_PART), 2) == 71.50 == round(sum(area_es(r) for r in A_STRIPS), 2)
assert round(area_es(MARU_A), 2) == 9.70 == round(sum(area_es(r) for r in MARU_STRIPS), 2)
assert round(area_es(MARU_A) + area_es(I2), 2) == 93.94

# ---- 敷地（図1の辺長。X＝北、Y＝東。西側の線を Y＝0、南側の線を X＝0） ----
S_NW, S_43, S_NE, S_SE = complex(18.70, 0), complex(18.70, 15.70), complex(18.70, 19.70), complex(0, 19.70)
S_CE, S_CN = complex(0, 2.12), complex(2.12, 0)      # 隅切りの東の端・北の端
SITE = [S_NW, S_43, S_NE, S_SE, S_CE, S_CN]
assert round(area(SITE), 4) == 366.1428


def to_site(p):
    """建物の点（B()で作った複素数）を敷地の座標へ（北の外壁が北側の筆界から1.00、西の外壁が西側の筆界から2.50）。"""
    return complex(17.70 + p.real, 2.50 + p.imag)


def dims(z, pts, labels, fs=14, ref=None):
    c = ref or centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs)


def tri(z, p, color=BLACK, size=11):
    """△印（各階の重なる柱の位置）。重なり検査の点として登録する。"""
    a, b = xy(p)
    z.ax.plot(a, b, '^', ms=size, mfc='white', mec=color, mew=1.8, zorder=6)
    z.markers.append((a, b))


# ---- 図1：区分の全体像 ----
def zu01():
    fig, axes = new_figure('区分の全体像：縦割りの区分（問1）と、（ロ）部分の再区分（問2）',
                           '（イ）部分は1階から屋根まで続く西半分（玄関1つの居宅）。（ロ）部分は、将来（あ）部分と（い）部分等に分ける',
                           w=18, h=8.5, ncols=3)
    fig.subplots_adjust(top=0.82, bottom=0.14)
    off = 18.5   # 2階を東へずらして並べる
    titles = ['区分前：家屋番号5番2（共同住宅）', '問1：建物区分登記（縦割り）', '問2：（ロ）部分をさらに区分']
    zs = []
    for k, ax in enumerate(axes):
        z = Zu(ax, fontsize=12)
        ax.set_title(titles[k], fontsize=16, weight='bold')
        if k == 0:
            z.poly(P(WHOLE1), color=BLACK, lw=2, fill=GRAY, alpha=0.25)
            z.poly(P(WHOLE2, off), color=BLACK, lw=2, fill=GRAY, alpha=0.25)
            z.free_text(B(8, 6), '173.00㎡', fs=13)
            z.free_text(B(8 + off, 6), '176.00㎡', fs=13)
        elif k == 1:
            z.poly(P(I1_WALL), color=BLACK, lw=2, fill=BLUE, alpha=0.30)
            z.poly(P(RO1_WALL), color=BLACK, lw=2, fill=GREEN, alpha=0.25)
            z.poly(P(rect(0, 0, 8, 11), off), color=BLACK, lw=2, fill=BLUE, alpha=0.30)
            z.poly(P(rect(8, 0, 16, 11), off), color=BLACK, lw=2, fill=GREEN, alpha=0.25)
            for d in (0, off):
                z.free_text(B(4 + d, 6), '（イ）', fs=14, weight='bold', color=BLUE)
                z.free_text(B(12 + d, 6), '（ロ）', fs=14, weight='bold', color=GREEN)
        else:
            z.poly(P(A_WALL, 8), color=BLACK, lw=2, fill=YELLOW, alpha=0.35)
            z.poly(P(MARU_A_WALL, 8), color=BLACK, lw=2, fill=RED, alpha=0.30)
            z.poly(P(rect(0, 0, 8, 11), off), color=BLUE, lw=1.2, ls='--', check=False)
            z.poly(P(rect(8, 0, 16, 11), off), color=BLACK, lw=2, fill=RED, alpha=0.30)
            z.poly(P(I1_WALL), color=BLUE, lw=1.2, ls='--', check=False)
            z.free_text(B(11.2, 3.5), '（あ）', fs=14, weight='bold')
            z.free_text(B(14.6, 8.4), 'Ⓐ', fs=15, weight='bold', color=RED)
            z.free_text(B(12 + off, 6), '（い）', fs=14, weight='bold', color=RED)
            z.free_text(B(4, 6), '（イ）', fs=12, color=BLUE)
            z.free_text(B(4 + off, 6), '（イ）', fs=12, color=BLUE)
        fit(ax, P(WHOLE1) + P(WHOLE2, off), margin=0.06, extra=[xy(B(0, 18.5)), xy(B(34.5, -1.5))], pad_aspect=True)
        z.free_text(B(8, 12.4), '1階', fs=13, va='top')
        z.free_text(B(8 + off, 12.4), '2階', fs=13, va='top')
        if k == 1:
            z.free_text(B(16.25, 16.4), '（イ）＝5番2の1 居宅（玄関1つ）\n（ロ）＝5番2の2 共同住宅', fs=12)
        if k == 2:
            z.free_text(B(16.25, 16.4), '（い）部分等＝2階の（い）＋1階のⒶ\n（Ⓐは（い）専用の玄関・階段）', fs=12, color=RED)
        zs.append(z)
    axes[2].annotate('', xy=xy(B(12 + off - 2.5, 3.5)), xytext=xy(B(15.2, 7.4)),
                     arrowprops=dict(arrowstyle='-|>', lw=1.6, color=RED, mutation_scale=16, connectionstyle='arc3,rad=-0.3'),
                     zorder=6)
    zs[0].north_arrow()
    save(fig, zs, 'R3_dai22mon_zu01_kubun_zentaizou')


# ---- 図2：敷地の辺長確認図 ----
def zu02():
    fig, axes = new_figure('本件土地（5番2）の辺長確認図（作図チェック用）',
                           '隅切りの2辺は 18.70−16.58＝19.70−17.58＝2.12。19.70×18.70−2.12×2.12÷2＝366.14㎡（登記記録の地積と一致）。辺長は建物図面には書かない',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(SITE, color=BLACK, lw=2.4, fill=BLUE, alpha=0.08)
    z.line(S_CE, complex(0, 0), color=GRAY, lw=1.2, ls=':')
    z.line(complex(0, 0), S_CN, color=GRAY, lw=1.2, ls=':')
    z.line(S_43, complex(20.2, 15.70), color=BLACK, lw=1.4)
    fit(ax, SITE, margin=0.10, extra=[(-4.5, 24.5), (25.5, -3.8)], pad_aspect=True)
    z.north_arrow()
    c = complex(9, 10)
    dims(z, SITE, ['15.70', '4.00', '18.70', '17.58', '', '16.58'], fs=15, ref=c)
    z.callout((S_CE + S_CN) / 2, '隅切り 3.00', dirs=(225, 240, 210), fs=15, dists=(45, 60, 80))
    z.free_text(complex(23.4, 9.85), '北側全体 19.70（15.70＋4.00）', fs=14)
    z.callout(complex(0, 1.06), '2.12', dirs=(-100, -80, -120), fs=13, color=GRAY, dists=(35, 50, 65))
    z.callout(complex(1.06, 0), '2.12', dirs=(180, 200, 160), fs=13, color=GRAY, dists=(35, 50, 65))
    z.free_text(complex(10, 10), '本件土地（5－2）\n366.14㎡', fs=16)
    z.free_text(complex(21.6, 7.5), '4－3', fs=14, color=GRAY)
    z.free_text(complex(21.6, 17.7), '4－1', fs=14, color=GRAY)
    z.free_text(complex(9.3, 23.0), '5－1', fs=14, color=GRAY)
    z.free_text(complex(-2.4, 11), '道路（116）', fs=14, color=GRAY)
    z.free_text(complex(10.5, -3.6), '道路\n（115）', fs=14, color=GRAY)
    save(fig, [z], 'R3_dai22mon_zu02_shikichi_henchou')


# ---- 図3：建物図面（イ）の完成形 ----
def dim_line(z, p, q, text, offsets=((12, 0),), dirs=None):
    ax = z.ax
    ax.annotate('', xy=xy(q), xytext=xy(p),
                arrowprops=dict(arrowstyle='<->', lw=1.4, color=BLACK, shrinkA=0, shrinkB=0), zorder=4)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    if dirs:
        return z.callout(m, text, dirs=dirs, fs=15, dists=(40, 55, 70))
    return z.free_text(m, text, fs=15, offsets=offsets)


def zu03():
    fig, axes = new_figure('建物図面（イ）の完成形（縮尺1/500で描く内容）',
                           '（イ）部分の1階を実線、一棟の建物の残りの1階（（ロ）部分）を点線。距離は図1の数値どおり。敷地の辺長は書かない',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(SITE, color=BLACK, lw=2.2)
    z.line(S_43, complex(20.4, 15.70), color=BLACK, lw=1.6)      # 4-3と4-1の境
    z.line(S_NE, complex(20.4, 19.70), color=BLACK, lw=1.6)
    z.line(S_NE, complex(18.70, 23.0), color=BLACK, lw=1.6)      # 5-1の北側の線
    z.line(S_SE, complex(0, 23.0), color=BLACK, lw=1.6)
    i_site = [to_site(p) for p in P(I1_WALL)]
    ro_site = [to_site(p) for p in P(RO1_WALL)]
    z.poly(i_site, color=BLACK, lw=2.6)
    z.poly(ro_site, color=BLACK, lw=1.6, ls='--', closed=False)   # 最後の辺（（イ）との境）は実線と重なるので描かない
    assert round(area(i_site), 2) == 86.50 and round(area(i_site) + area(ro_site), 2) == 173.00
    fit(ax, SITE, margin=0.10, extra=[(-4.5, 25.0), (23.5, -4.2)], pad_aspect=True)
    z.north_arrow()
    dim_line(z, complex(18.70, 2.5), complex(17.70, 2.5), '1.00', dirs=(150, 135, 165, 120))
    dim_line(z, complex(17.2, 0), complex(17.2, 2.5), '2.50', dirs=(200, 215, 185))
    dim_line(z, complex(7.2, 0), complex(7.2, 2.5), '2.50', dirs=(200, 215, 185))
    z.free_text(complex(12.2, 6.5), '（イ）', fs=15, weight='bold')
    z.free_text(complex(3.4, 11.0), '5－2', fs=16)
    z.free_text(complex(20.1, 7.5), '4－3', fs=15)
    z.free_text(complex(20.1, 18.0), '4－1', fs=15)
    z.free_text(complex(9.3, 21.5), '5－1', fs=15)
    z.free_text(complex(-2.4, 11), '道路（116）', fs=15)
    z.free_text(complex(10.5, -2.7), '道路\n（115）', fs=15)
    save(fig, [z], 'R3_dai22mon_zu03_tatemono_zumen')


# ---- 図4：誤り比較図（壁心／内法） ----
def zu04():
    fig, axes = new_figure('（イ）部分1階の床面積：壁心か、内法か',
                           '区分建物の床面積は壁その他の区画の内側線で囲まれた部分（不動産登記規則第115条）。欠けの大きさ1.50×1.00は変わらない',
                           w=18, h=9.5, ncols=3, width_ratios=[1, 0.72, 1])
    fig.subplots_adjust(top=0.84)
    # 誤り（壁心）
    z = Zu(axes[0], fontsize=13)
    z.poly(P(I1_WALL), color=RED, lw=2.4, fill=RED, alpha=0.18)
    axes[0].set_title('誤り：壁心のまま 86.50㎡（藍子）', fontsize=16, weight='bold', color=RED)
    fit(axes[0], P(I1_WALL), margin=0.2, pad_aspect=True)
    dims(z, P(I1_WALL), ['6.50', '1.00', '', '10.00', '8.00', '11.00'], fs=13)
    z.callout(B(7.25, 1), '1.50', dirs=(60, 80, 40), fs=13, dists=(30, 45, 60))
    z.free_text(B(4, 6), '6.50×1.00\n＋8.00×10.00\n＝86.50㎡', fs=13, color=RED)
    # 拡大（壁の断面：北西の角）
    z2 = Zu(axes[1], fontsize=12)
    wall = [complex(0.25, -0.25), complex(0.25, 0.9), complex(-0.1, 0.9), complex(-0.1, 0.1), complex(-0.9, 0.1),
            complex(-0.9, -0.25)]
    z2.poly(wall, color=GRAY, lw=0, fill=GRAY, alpha=0.30, check=False)
    hatch(axes[1], wall)
    z2.line(complex(0, -0.25), complex(0, 0.9), color=BLACK, lw=1.2, ls='-.')
    z2.line(complex(-0.9, 0), complex(0.25, 0), color=BLACK, lw=1.2, ls='-.')
    z2.line(complex(-0.1, 0.1), complex(-0.1, 0.9), color=GREEN, lw=3)
    z2.line(complex(-0.1, 0.1), complex(-0.9, 0.1), color=GREEN, lw=3)
    axes[1].set_title('北西の角（拡大）', fontsize=16, weight='bold')
    fit(axes[1], wall, margin=0.25, pad_aspect=True)
    axes[1].annotate('', xy=xy(complex(-0.1, 0.55)), xytext=xy(complex(0, 0.55)),
                     arrowprops=dict(arrowstyle='<->', lw=1.4, color=RED, shrinkA=0, shrinkB=0))
    z2.segments.append((xy(complex(-0.1, 0.55)), xy(complex(0, 0.55))))
    z2.callout(complex(-0.05, 0.55), '0.10（図4の（注）2）', dirs=(-60, -40, -80), fs=12, color=RED)
    z2.callout(complex(0.15, -0.0), '壁の中心線（壁心）', dirs=(90, 70, 110), fs=12)
    z2.callout(complex(-0.6, 0.1), '内壁の面（内法）', dirs=(-90, -110, -70), fs=12, color=GREEN)
    # 正解（内法）
    z3 = Zu(axes[2], fontsize=13)
    z3.poly(P(I1_WALL), color=GRAY, lw=1.0, ls=':', check=False)
    z3.poly(P(I1), color=GREEN, lw=2.4, fill=GREEN, alpha=0.20)
    axes[2].set_title('正解：内法で 82.74㎡', fontsize=16, weight='bold', color=GREEN)
    fit(axes[2], P(I1_WALL), margin=0.2, pad_aspect=True)
    dims(z3, P(I1), ['6.30', '1.00', '', '9.80', '7.80', '10.80'], fs=13)
    z3.callout(B(7.15, 1.1), '1.50', dirs=(60, 80, 40), fs=13, dists=(30, 45, 60))
    z3.free_text(B(4, 6), '6.30×1.00\n＋7.80×9.80\n＝82.74㎡', fs=13, color=GREEN)
    save(fig, [z, z2, z3], 'R3_dai22mon_zu04_ayamari_hikaku')


# ---- 図5・図6：（イ）部分の求積図 ----
def zu05():
    fig, axes = new_figure('（イ）部分1階の床面積求積図（内法）',
                           '6.30×1.00＋7.80×9.80＝82.74㎡。△印は各階の重なる柱の位置（図4の（注）4）',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    for r, c in zip(I1_STRIPS, [ORANGE, BLUE]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.25, check=False)
    z.line(B(0.1, 1.1), B(6.4, 1.1), color=GRAY, lw=1.0, ls='--')
    z.poly(P(I1), color=BLACK, lw=2.4)
    fit(ax, P(I1), margin=0.22, pad_aspect=True)
    z.north_arrow()
    tri(z, B(0.1, 0.1))
    dims(z, P(I1), ['6.30', '1.00', '1.50', '9.80', '7.80', '10.80'], fs=15)
    z.free_text(B(3.25, 0.6), '6.30×1.00', fs=14)
    z.free_text(B(4.0, 6.0), '7.80×9.80', fs=16)
    z.free_text(B(4.0, 12.3), '1階　床面積：82.74㎡', fs=17, weight='bold')
    save(fig, [z], 'R3_dai22mon_zu05_1kai_kyuuseki')


def zu06():
    fig, axes = new_figure('（イ）部分2階の床面積求積図（内法）',
                           '7.80×10.80＝84.24㎡。点線は1階の北東の欠け（1.50×1.00）の位置',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(P(I2), color=BLACK, lw=2.4, fill=BLUE, alpha=0.22)
    z.poly(P([(6.4, 0.1), (6.4, 1.1), (7.9, 1.1)]), color=BLACK, lw=1.4, ls='--', closed=False)
    fit(ax, P(I2), margin=0.22, pad_aspect=True)
    z.north_arrow()
    tri(z, B(0.1, 0.1))
    dims(z, P(I2), ['7.80', '10.80', '7.80', '10.80'], fs=15)
    z.free_text(B(4.0, 6.0), '7.80×10.80', fs=16)
    z.callout(B(7.15, 1.1), '1階の欠けの位置（点線）', dirs=(-45, -30, -60), fs=13)
    z.free_text(B(4.0, 12.3), '2階　床面積：84.24㎡', fs=17, weight='bold')
    save(fig, [z], 'R3_dai22mon_zu06_2kai_kyuuseki')


# ---- 図7：問2の求積図 ----
def zu07():
    fig, axes = new_figure('問2：（ロ）部分を（あ）部分と（い）部分等に分けたときの床面積（内法）',
                           '（あ）部分 71.50㎡、（い）部分等＝Ⓐ部分9.70＋（い）部分84.24＝93.94㎡。敷地権の割合は 33088分の7150・33088分の9394',
                           w=18, h=11, ncols=2)
    fig.subplots_adjust(top=0.85)
    z = Zu(axes[0], fontsize=12)
    z.poly(P(R1_WALL), color=GRAY, lw=1.0, ls=':', check=False)
    for r, c in zip(A_STRIPS, [ORANGE, YELLOW, BLUE, PURPLE]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.28, check=False)
    for r in MARU_STRIPS:
        z.poly(P(r), color=RED, lw=0, fill=RED, alpha=0.28, check=False)
    z.line(B(0.1, 1.1), B(1.6, 1.1), color=GRAY, lw=1.0, ls='--')
    z.line(B(1.6, 1.1), B(7.9, 1.1), color=GRAY, lw=1.0, ls='--')
    z.line(B(0.1, 6.4), B(5.2, 6.4), color=GRAY, lw=1.0, ls='--')
    z.line(B(0.1, 9.6), B(5.2, 9.6), color=GRAY, lw=1.0, ls='--')
    z.line(B(6.1, 9.4), B(7.9, 9.4), color=GRAY, lw=1.0, ls='--')
    z.poly(P(A_PART), color=BLACK, lw=2.2)
    z.poly(P(MARU_A), color=RED, lw=2.2)
    axes[0].set_title('1階：（あ）部分とⒶ部分', fontsize=16, weight='bold')
    fit(axes[0], P(R1_WALL), margin=0.22, pad_aspect=True)
    z.north_arrow()
    z.free_text(B(4.75, 0.6), '6.30×1.00', fs=12)
    z.free_text(B(4.0, 3.75), '7.80×5.30', fs=13)
    z.free_text(B(2.65, 8.0), '5.10×3.20', fs=13)
    z.free_text(B(3.0, 10.25), '5.80×1.30', fs=11)
    z.callout(B(6.65, 8.0), 'Ⓐ 2.50×2.80', dirs=(0, 20, -20), fs=12, color=RED)
    z.callout(B(7.0, 10.15), 'Ⓐ 1.80×1.50', dirs=(0, -20, -40), fs=12, color=RED)
    z.free_text(B(4.0, 12.6), '（あ）部分 71.50㎡　Ⓐ部分 9.70㎡', fs=14, weight='bold')
    z2 = Zu(axes[1], fontsize=13)
    z2.poly(P(R1_WALL), color=GRAY, lw=1.0, ls=':', check=False)
    z2.poly(P(I2), color=BLACK, lw=2.2, fill=RED, alpha=0.25)
    axes[1].set_title('2階：（い）部分', fontsize=16, weight='bold')
    fit(axes[1], P(R1_WALL), margin=0.22, pad_aspect=True)
    dims(z2, P(I2), ['7.80', '10.80', '', ''], fs=14)
    z2.free_text(B(4.0, 6.0), '7.80×10.80\n＝84.24㎡', fs=14)
    z2.free_text(B(4.0, 12.6), '（い）部分等 9.70＋84.24＝93.94㎡', fs=14, weight='bold', color=RED)
    save(fig, [z, z2], 'R3_dai22mon_zu07_toi2_kyuuseki')


if __name__ == '__main__':
    zu01()
    zu02()
    zu03()
    zu04()
    zu05()
    zu06()
    zu07()
    print('重なり合計:', len(PROBLEMS))
