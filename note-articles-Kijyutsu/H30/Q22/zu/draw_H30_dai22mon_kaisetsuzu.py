"""平成30年度 第22問（建物）の解説図7枚を、座標値・頂点座標から作図してPNGに書き出す。

`../prompt_H30_dai22mon_kaisetsuzu.md` の図1〜図7どおり。作図の共通部品は `tools/zu_helpers.py`。
敷地・建物の外壁の点は〔座標一覧表〕の (X＝北, Y＝東)（〔見取図〕の（注）4）。
建物の平面（床面積の線＝外壁から0.07内側の柱の中心を結ぶ線。事実関係8）は (東, 南)（原点＝1階の北西の角）で持ち、
zu_helpers の (北, 東) には P()・B_() で変換する。
建物図面の建物は、床面積の線（外壁のG点〈20.00, −8.00〉から0.07内側の北西の角〈19.93, −7.93〉を原点）で描き、
距離の矢印は外壁の点G・H・Lから筆界までとする。
実行: python3 note-articles-Kijyutsu/H30/Q22/zu/draw_H30_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402

from zu_helpers import Zu, new_figure, fit, xy, centroid, BLACK, GRAY, RED, BLUE, ORANGE, GREEN, PURPLE  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []

# ---- 敷地（〔座標一覧表〕） ----
A, B, C, D, E, F = complex(0, -15), complex(29, -15), complex(29, 0), complex(29, 15), complex(0, 15), complex(0, 0)
LOT301, LOT302 = [A, B, C, F], [F, C, D, E]
# ---- 建物の外壁の点 ----
G, H, I, J, K, L = complex(20, -8), complex(20, 12), complex(11, 12), complex(11, -3), complex(8, -3), complex(8, -8)
M, N, O = complex(20, 3), complex(11, 3), complex(20, -3)
OUTER = [G, H, I, J, K, L]
P_OUT = [G, O, K, L]             # P部分（G・O・J・K・L。O・J・Kは一直線）
Q_OUT = [M, H, I, N]
EXT_OUT = [O, M, N, J]           # 増築部分
T = 0.07                         # 外壁から柱の中心を結ぶ線まで（事実関係8）
N0, W0 = G.real - T, G.imag + T  # 床面積の線の北西の角（19.93, −7.93）


def P(e, s):
    """求積図用：床面積の線の北西の角を原点にした (東, 南) を (北 + 東i) にする。"""
    return complex(-s, e)


def B_(e, s):
    """建物図面用：(東, 南) を敷地の座標 (北 + 東i) に置く。"""
    return complex(N0 - s, W0 + e)


def rect(e0, s0, e1, s1, f=P):
    return [f(e0, s0), f(e1, s0), f(e1, s1), f(e0, s1)]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


# ---- 1階・2階の形（床面積の線。(東, 南)） ----
F1 = [(0, 0), (19.86, 0), (19.86, 8.86), (4.86, 8.86), (4.86, 11.86), (0, 11.86)]
F1_WRONG = [(0, 0), (19.86, 0), (19.86, 8.86), (4.86, 8.86), (4.86, 11.72), (0, 11.72)]
F2 = [(11, 0), (19.86, 0), (19.86, 8.86), (11, 8.86)]
assert round(area([P(*v) for v in F1]), 4) == 190.5396
assert round(area([P(*v) for v in F1_WRONG]), 4) == 189.8592
assert round(area([P(*v) for v in F2]), 4) == 78.4996
assert round(area(OUTER), 2) == 195.00 and round(area(LOT301), 2) == round(area(LOT302), 2) == 435.00
assert round(area(P_OUT), 2) == 60.00 and round(area(Q_OUT), 2) == 81.00 and round(area(EXT_OUT), 2) == 54.00
# 床面積の線を敷地に置くと、外壁の点から0.07内側にそろう
BLDG = [B_(*v) for v in F1]
assert (round(BLDG[1].imag, 2), round(BLDG[2].real, 2), round(BLDG[4].real, 2)) == (11.93, 11.07, 8.07)
assert round(area(BLDG), 4) == 190.5396
# 所在：境（Y＝0）の東（302番）と西（301番）の1階の床面積。302番が多い
on302 = round(area([B_(*v) for v in [(7.93, 0), (19.86, 0), (19.86, 8.86), (7.93, 8.86)]]), 4)
assert on302 == 105.6998 and round(190.5396 - on302, 4) == 84.8398
# 2階の西の端は北西の角から東へ11.00（Q部分の西の外壁Y＝3.00から0.07内側）
assert round((3 + T) - W0, 2) == 11.00


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def dims(z, pts, labels, fs=14, outward=True):
    """多角形の各辺に寸法（None は書かない）を書く。"""
    c = centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs, outward=outward)


def dist_arrow(z, p, q, text, color=BLACK, fs=15, side=(8, 0)):
    """筆界から外壁までの距離の矢印（両向き）と数値。"""
    z.ax.annotate('', xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='<|-|>', color=color, lw=1.6,
                                                           mutation_scale=12, shrinkA=0, shrinkB=0), zorder=6)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    return z.free_text(m, text, fs=fs, color=color,
                       offsets=(side, (-side[0], -side[1]), (0, 12), (0, -12), (side[0] * 2, side[1] * 2),
                                (-side[0] * 2, -side[1] * 2)), ha='center', va='center')


OFFS = ((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0), (26, 0), (-26, 0))
NEIGHBORS = [(complex(31.2, -7.5), '314'), (complex(31.2, 7.5), '315'), (complex(31.2, -18.5), '312'),
             (complex(31.2, 18.5), '316-2'), (complex(14.5, -18.8), '300-2'), (complex(14.5, 17.8), '303'),
             (complex(-3.0, 7.5), '道路（200）')]


def zu01():
    fig, axes = new_figure('工事前と工事後：別々に登記された2個が構造上1個に＝合体',
                           '301番（P部分）と302番（Q部分）は別々の家屋番号の建物。間を増築し、P部分の東の壁・Q部分の西の壁（隔壁）を取り払って構造上1個になった。\n'
                           '登記の上だけまとめる合併ではなく、合体による登記等（不動産登記法第49条）',
                           w=16, h=10, ncols=2)
    fig.subplots_adjust(top=0.84, bottom=0.16)
    extent = [complex(4, -11), complex(24, 16)]
    # 工事前
    z = Zu(axes[0], fontsize=14)
    z.line(complex(4, 0), complex(10, 0), color=GRAY, lw=1.2, ls='--')   # 301番と302番の境（建物の南だけ描く）
    z.poly(P_OUT, color=BLACK, lw=2.2, fill=BLUE, alpha=0.18)
    z.poly(Q_OUT, color=BLACK, lw=2.2, fill=GREEN, alpha=0.2)
    z.free_text(complex(14, -5.5), '301番\nP部分\n平家建\nスレートぶき\n抵当権あり', fs=12)
    z.free_text(complex(15.5, 7.5), '302番\nQ部分\n2階建\nかわらぶき', fs=13)
    z.free_text(complex(15.5, 0), '空き\n地', fs=12, color=GRAY)
    a_, b_ = complex(21.2, -3), complex(21.2, 3)
    z.ax.annotate('', xy(b_), xytext=xy(a_), arrowprops=dict(arrowstyle='<|-|>', color=BLACK, lw=1.4,
                                                             mutation_scale=11, shrinkA=0, shrinkB=0))
    z.segments.append((xy(a_), xy(b_)))
    z.free_text(complex(21.2, 0), '6.00m', fs=13, offsets=((0, 12), (0, 18)))
    z.free_text(complex(6.5, -6), '301番の土地', fs=12, color=GRAY, offsets=((0, -10), (0, -18)))
    z.free_text(complex(6.5, 6), '302番の土地', fs=12, color=GRAY, offsets=((0, -10), (0, -18)))
    axes[0].set_title('工事前（登記記録：2個の建物）', fontsize=18, weight='bold', pad=12)
    fit(axes[0], extent, margin=0.04, pad_aspect=True)
    # 工事後
    z2 = Zu(axes[1], fontsize=14)
    z2.line(complex(4, 0), complex(10, 0), color=GRAY, lw=1.2, ls='--')
    z2.poly(P_OUT, color=BLUE, lw=0, fill=BLUE, alpha=0.18, check=False)
    z2.poly(Q_OUT, color=GREEN, lw=0, fill=GREEN, alpha=0.2, check=False)
    z2.poly(EXT_OUT, color=ORANGE, lw=0, fill=ORANGE, alpha=0.45, check=False)
    z2.line(O, J, color=RED, lw=2.0, ls='--')
    z2.line(M, N, color=RED, lw=2.0, ls='--')
    z2.poly(OUTER, color=BLACK, lw=2.6)
    z2.free_text(complex(15.5, 0), '増築\n部分', fs=13, color=ORANGE, weight='bold')
    z2.free_text(complex(14, -5.5), '元の\nP部分', fs=13)
    z2.free_text(complex(15.5, 7.5), '元の\nQ部分', fs=13)
    z2.callout(complex(18, -3), '隔壁を除去', dirs=(110, 120, 100), dists=(45, 60, 75), fs=13, color=RED)
    z2.callout(complex(18, 3), '隔壁を除去', dirs=(70, 60, 80), dists=(45, 60, 75), fs=13, color=RED)
    z2.free_text(complex(6.5, 7.5), '構造上1個の建物\n（家屋番号は新しく付く）', fs=14, color=PURPLE,
                 offsets=((0, 0), (0, -10), (30, 0)))
    axes[1].set_title('工事後（平成30年10月1日）', fontsize=18, weight='bold', pad=12)
    fit(axes[1], extent, margin=0.04, pad_aspect=True)
    z2.north_arrow()
    save(fig, [z, z2], 'H30_dai22mon_zu01_kouji_zengo')


def zu02():
    fig, axes = new_figure('301番・302番（敷地）の辺長確認図（作図チェック用）',
                           'すべての辺が南北か東西（座標の軸に平行）なので、辺長は座標の差で出る。面積435.00㎡は登記記録の地積と一致。\n'
                           '辺長は作図が正しいかを確かめるためのもので、建物図面には書かない',
                           w=16, h=11.5)
    fig.subplots_adjust(bottom=0.14)
    ax = axes[0]
    z = Zu(ax, fontsize=16)
    z.poly(LOT301, color=BLACK, lw=2.6, fill=BLUE, alpha=0.12)
    z.poly(LOT302, color=BLACK, lw=2.6, fill=GREEN, alpha=0.12)
    for p in [A, B, C, D, E, F]:
        z.point(p)
    cc = complex(14.5, 0)
    for p, n in zip([A, B, C, D, E, F], 'ABCDEF'):
        z.point_label(p, n, away=cc, fs=19)
    c1, c2 = centroid(LOT301), centroid(LOT302)
    z.edge_label(A, B, '29.00m', c1, fs=16, outward=False)
    z.edge_label(B, C, '15.00m', c1, fs=16, outward=False)
    z.edge_label(D, E, '29.00m', c2, fs=16, outward=False)
    z.edge_label(E, F, '15.00m', c2, fs=16, outward=False)
    z.free_text(complex(15, -7.5), '301番\n435.00㎡', fs=18)
    z.free_text(complex(15, 7.5), '302番\n435.00㎡', fs=18)
    for p, t in NEIGHBORS:
        z.free_text(p, t, fs=15, color=GRAY, offsets=OFFS)
    fit(ax, LOT301 + LOT302, margin=0.1, extra=[xy(complex(-4, -22)), xy(complex(33, 22))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H30_dai22mon_zu02_shikichi_henchou')


def zu03():
    fig, axes = new_figure('建物図面（縮尺500分の1）の完成形',
                           '1階の形を座標どおりに置き、G・H・Lの点から筆界までの距離を書く（問3のなお書き）。建物は301番と302番にまたがり、\n'
                           '床面積の多い302番地が先（所在「A市B町一丁目302番地、301番地」）。敷地の辺長は書かない',
                           w=16, h=11.5)
    fig.subplots_adjust(bottom=0.14)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(LOT301, color=BLACK, lw=2.2)
    z.poly(LOT302, color=BLACK, lw=2.2)
    z.poly(BLDG, color=BLACK, lw=2.4, fill=ORANGE, alpha=0.25)
    dist_arrow(z, G, complex(G.real, A.imag), '7.00', side=(0, 14))
    dist_arrow(z, H, complex(B.real, H.imag), '9.00', side=(-20, 0))
    dist_arrow(z, L, complex(A.real, L.imag), '8.00', side=(-20, 0))
    for p, t in [(complex(24.5, -9.5), '301'), (complex(24.5, 6.0), '302')]:
        z.free_text(p, t, fs=17, offsets=OFFS)
    for p, t in NEIGHBORS:
        z.free_text(p, t, fs=15, color=GRAY, offsets=OFFS)
    z.free_text(complex(-4.5, 17), '（単位：m）', fs=13, offsets=OFFS)
    fit(ax, LOT301 + LOT302, margin=0.1, extra=[xy(complex(-6, -22)), xy(complex(33, 22))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H30_dai22mon_zu03_tatemono_zumen')


def zu04():
    fig, axes = new_figure('1階の誤り比較図：入り隅に端がある3.00・15.00は0.14減らない',
                           '座標は外壁の点。床面積の線は外壁から0.07内側。張り出しの南北3.00は、両端の壁（北側の部分の南の壁・張り出しの南の壁）が\n'
                           'どちらも北へ0.07ずれるので長さが変わらない：19.86×8.86＋4.86×2.86＝189.85ではなく、19.86×8.86＋4.86×3.00＝190.53㎡',
                           w=16, h=10, ncols=3, width_ratios=[1.05, 0.9, 1.05])
    fig.subplots_adjust(top=0.84, bottom=0.17, wspace=0.10)
    # 左：誤り
    z = Zu(axes[0], fontsize=13)
    wrong = [P(*v) for v in F1_WRONG]
    z.poly(wrong, color=RED, lw=2.2, fill=RED, alpha=0.15)
    dims(z, wrong, ['19.86', '8.86', None, '2.86', '4.86', None], fs=13)
    z.free_text(P(9.5, 4.4), '189.85㎡', fs=16, color=RED)
    axes[0].set_title('誤り：全部の寸法から0.14', fontsize=16, weight='bold', color=RED, pad=12)
    fit(axes[0], [P(*v) for v in F1], margin=0.12, pad_aspect=True)
    # 中央：張り出しの北東の入り隅（模式。壁の厚さは拡大して描く）
    z2 = Zu(axes[1], fontsize=12)
    d = 0.35   # 外壁と床面積の線の間（実際は0.07）を、見えるように拡大した模式
    e0, s1, s2 = 4.86, 8.86, 11.86
    outer = [P(e0 + 3.0, s1 + d), P(e0 + d, s1 + d), P(e0 + d, s2 + d), P(e0 - 2.2, s2 + d)]
    inner = [P(e0 + 3.0, s1), P(e0, s1), P(e0, s2), P(e0 - 2.2, s2)]
    z2.poly(outer, color=BLACK, lw=3.0, closed=False)
    z2.poly(inner, color=GREEN, lw=3.0, closed=False)
    # 南の端の寸法補助線（張り出しの南の壁の線を東へのばす）
    z2.line(P(e0, s2), P(e0 + 1.1, s2), color=GREEN, lw=1.0, ls=':')
    z2.line(P(e0 + d, s2 + d), P(e0 + 2.8, s2 + d), color=BLACK, lw=1.0, ls=':')
    for ea, s_ in ((e0 + 2.0, s1), (e0 - 1.4, s2)):
        a, b = P(ea, s_ + d), P(ea, s_)
        z2.ax.annotate('', xy(b), xytext=xy(a), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.8, mutation_scale=14))
        z2.segments.append((xy(a), xy(b)))
    z2.free_text(P(e0 + 2.0, s1 - 0.35), '北へ0.07', fs=12, color=RED, offsets=((0, 6), (0, 12)))
    z2.free_text(P(e0 - 1.4, s2 - 0.35), '北へ0.07', fs=12, color=RED, offsets=((0, 6), (0, 12)))
    # 3.00の寸法（中心線どうし・外壁どうし）
    for e_, s0_, t_, col in [(e0 + 0.9, s1, '中心線\nどうし\n3.00', GREEN), (e0 + 2.6, s1 + d, '外壁\nどうし\n3.00', BLACK)]:
        a, b = P(e_, s0_), P(e_, s0_ + 3.0)
        z2.ax.annotate('', xy(b), xytext=xy(a), arrowprops=dict(arrowstyle='<|-|>', color=col, lw=1.4,
                                                               mutation_scale=11, shrinkA=0, shrinkB=0))
        z2.segments.append((xy(a), xy(b)))
        z2.free_text(P(e_, s0_ + 1.5), t_, fs=12, color=col, ha='left', offsets=((6, 0), (6, 14), (6, -14)))
    z2.free_text(P(e0 + 1.5, s1 - 1.1), '北側の部分', fs=12, color=GRAY, offsets=((0, 0), (0, 8)))
    z2.free_text(P(e0 - 1.1, s1 + 1.2), '張り出し', fs=12, color=GRAY, offsets=((0, 0), (0, -8)))
    axes[1].set_title('入り隅の拡大（模式）', fontsize=16, weight='bold', pad=12)
    fit(axes[1], [P(e0 - 2.5, s1 - 1.6), P(e0 + 3.7, s2 + 0.9)], margin=0.04, pad_aspect=True)
    # 右：正解
    z3 = Zu(axes[2], fontsize=13)
    ok = [P(*v) for v in F1]
    z3.poly(ok, color=GREEN, lw=2.4, fill=GREEN, alpha=0.18)
    dims(z3, ok, ['19.86', '8.86', '15.00', '3.00', '4.86', '11.86'], fs=13)
    z3.free_text(P(9.5, 4.4), '190.53㎡', fs=16, color=GREEN)
    axes[2].set_title('正解：3.00・15.00はそのまま', fontsize=16, weight='bold', color=GREEN, pad=12)
    fit(axes[2], ok, margin=0.12, pad_aspect=True)
    assert round(19.86 * 8.86 + 4.86 * 2.86, 4) == 189.8592 and round(19.86 * 8.86 + 4.86 * 3.00, 4) == 190.5396
    save(fig, [z, z2, z3], 'H30_dai22mon_zu04_1kai_ayamari_hikaku')


def zu05():
    fig, axes = new_figure('1階の床面積求積図（壁の中心線）',
                           '北側の部分 19.86×8.86＝175.9596 ＋ 南西の張り出し 4.86×3.00＝14.5800 ＝ 190.5396 → 190.53㎡（切り捨て）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    r1, r2 = rect(0, 0, 19.86, 8.86), rect(0, 8.86, 4.86, 11.86)
    z.poly(r1, color=BLUE, lw=0, fill=BLUE, alpha=0.2, check=False)
    z.poly(r2, color=ORANGE, lw=0, fill=ORANGE, alpha=0.4, check=False)
    z.line(P(0, 8.86), P(4.86, 8.86), color=GRAY, lw=1.2, ls='--')
    f1 = [P(*v) for v in F1]
    z.poly(f1, color=BLACK, lw=2.4)
    dims(z, f1, ['19.86', '8.86', '15.00', '3.00', '4.86', '11.86'], fs=15)
    z.free_text(P(9.93, 4.43), '①北側の部分\n19.86×8.86＝175.9596', fs=16)
    z.free_text(P(2.43, 10.36), '②張り出し\n4.86×3.00\n＝14.5800', fs=13)
    z.free_text(P(12.5, 11.5), '1階 床面積：190.53㎡', fs=18, weight='bold')
    fit(ax, f1, margin=0.14, extra=[xy(P(12.5, 12.6))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H30_dai22mon_zu05_1kai_kyuuseki')


def zu06():
    fig, axes = new_figure('2階の床面積求積図（1階の位置を点線で重ねる）',
                           '2階はQ部分の上だけ（事実関係9）：8.86×8.86＝78.4996 → 78.49㎡（四捨五入の78.50ではない）。1階の残りの部分を点線で示す',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    f2 = [P(*v) for v in F2]
    z.poly(f2, color=BLACK, lw=2.6, fill=BLUE, alpha=0.25)
    rest = [P(11, 0), P(0, 0), P(0, 11.86), P(4.86, 11.86), P(4.86, 8.86), P(11, 8.86)]
    z.poly(rest, color=BLACK, lw=1.6, ls=':', closed=False)
    dims(z, f2, ['8.86', '8.86', '8.86', '8.86'], fs=15)
    z.free_text(P(15.43, 4.43), '2階\n8.86×8.86\n＝78.4996', fs=16)
    z.free_text(P(4.5, 4.4), '点線＝1階の位置\n（2階はない）', fs=15, color=GRAY)
    z.free_text(P(5.5, 0), '11.00', fs=13, color=GRAY, offsets=((0, 12), (0, 20)))
    z.free_text(P(12.5, 11.5), '2階 床面積：78.49㎡', fs=18, weight='bold')
    fit(ax, [P(*v) for v in F1], margin=0.14, extra=[xy(P(12.5, 12.6))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H30_dai22mon_zu06_2kai_kyuuseki')


def zu07():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    fig = plt.figure(figsize=(16, 9), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　計算のいらない欄を先に', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.02, 0.16, 0.96, 0.74])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    # 時系列メモ
    memo = [('昭和60年3月12日', '302番の所有権の登記'), ('平成29年1月20日', '301番の所有権の登記・抵当権'),
            ('平成30年10月1日', '工事完了（合体の日）'), ('10月10日', '登記記録の調査'), ('10月19日', '申請')]
    ax.text(1, 97, '時系列メモ', fontsize=17, weight='bold', va='top')
    ax.plot([2, 98], [84, 84], color=GRAY, lw=2)
    for i, (d, t) in enumerate(memo):
        x = 6 + i * 22
        ax.plot(x, 84, 'o', ms=10, color=RED if i == 2 else GRAY)
        ax.text(x, 88, d, ha='center', va='bottom', fontsize=14, weight='bold', color=RED if i == 2 else BLACK)
        ax.text(x, 80, t, ha='center', va='top', fontsize=13)
    steps = [
        ('①', '問を\n先に読む', '問1の穴埋め＝\n申請すべき登記\nの理由', BLUE),
        ('②', '問2', '第2欄\n（知識で書ける）', BLUE),
        ('③', '時系列\nメモ', '事実関係・\n登記記録', BLUE),
        ('④', '申請書の\n床面積以外', '目的・添付書類・\n持分（あ）（い）・\n所有権・存続登記', BLUE),
        ('⑤', '累計メモ\nと求積', '東0・4.86・19.86\n南0・8.86・11.86\n合体前の2つも', RED),
        ('⑥', '第3欄の\n作図', '左に各階平面図\n右に建物図面', RED),
        ('⑦', '見直し', '持分・識別情報1つ・\n切り捨て3つ・\n302番地が先', GRAY),
    ]
    w, h, gap = 12.4, 30, 1.6
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 26), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 26 + h - 3, no, ha='center', va='top', fontsize=24, color=col, weight='bold')
        ax.text(x + w / 2, 26 + h / 2 - 4, t, ha='center', va='center', fontsize=16)
        ax.text(x + w / 2, 22, ran, ha='center', va='top', fontsize=12.5, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.1, 41), xytext=(x + w + 0.1, 41),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.annotate('', xy=(1 + 4 * (w + gap) - gap, 62), xytext=(1, 62), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 2 * (w + gap) - gap / 2, 65, '計算しなくても書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 6 * (w + gap) - gap, 62), xytext=(1 + 4 * (w + gap), 62),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    ax.text(1 + 5 * (w + gap) - gap / 2, 65, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    fig.text(0.5, 0.07, '床面積は、外壁の座標から0.07内側へ直し、入り隅の3.00・15.00は減らさない。合体前の57.63・78.49も申請書に書く。\n'
             '先に問2と申請書の大部分を書いておけば、作図で時間が足りなくなっても点は取れている。',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'H30_dai22mon_zu07_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図7: 解く順番（固定配置）\n  →', path)


if __name__ == '__main__':
    zu01()
    zu02()
    zu03()
    zu04()
    zu05()
    zu06()
    zu07()
    print('重なり合計:', len(PROBLEMS))
