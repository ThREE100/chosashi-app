"""平成28年度 第22問（建物）の解説図8枚を、辺長・頂点座標から作図してPNGに書き出す。

`../prompt_H28_dai22mon_kaisetsuzu.md` の図1〜図8どおり。作図の共通部品は `tools/zu_helpers.py`。
- 図1・図2：南側立面図の模式図。横＝東、縦＝高さ（zu_helpers の (北, 東) に E_(東, 高さ) で置く）
- 図3・図4：敷地。座標値一覧表はないので、配置図の辺長から、敷地の南西の角を原点に (北, 東) で置く
- 図5〜図7：建物の平面。(東, 南)（原点＝既存建物の北西の角の柱の中心）で持ち、P() で (北, 東) に変換する
- 図8：本番で解く順番（固定配置。重なり検査の対象外）
実行: python3 note-articles-Kijyutsu/H28/Q22/zu/draw_H28_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402

from zu_helpers import Zu, new_figure, fit, xy, centroid, BLACK, GRAY, RED, BLUE, ORANGE, GREEN, PURPLE  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []
YELLOW = '#e3b505'


def P(e, s):
    """建物の平面の (東, 南) を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(-s, e)


def E_(e, h):
    """立面の模式図の (東, 高さ) を (北 + 東i) にする（縦軸＝高さ）。"""
    return complex(h, e)


def rect(e0, s0, e1, s1, f=P):
    return [f(e0, s0), f(e1, s0), f(e1, s1), f(e0, s1)]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


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
                       offsets=(side, (-side[0], -side[1]), (0, 14), (0, -14), (side[0] * 2, side[1] * 2),
                                (-side[0] * 2, -side[1] * 2)), ha='center', va='center')


# ---- 各階の形（柱の中心線。(東, 南)） ----
F1 = [(0, 0), (9, 0), (9, 9), (4.5, 9), (4.5, 10.8), (0, 10.8)]
F2 = [(0, 0), (9, 0), (9, 5.68), (12.39, 5.68), (12.39, 0.57), (19.32, 0.57), (19.32, 3.62), (19.93, 3.62),
      (19.93, 7.2), (0, 7.2)]
F3 = [(12.39, 0.57), (19.93, 0.57), (19.93, 3.62), (19.02, 3.62), (19.02, 7.2), (12.39, 7.2)]
DOT2 = [(0, 7.2), (9, 7.2), (9, 9), (4.5, 9), (4.5, 10.8), (0, 10.8)]   # 1階のうち2階の外の部分
assert round(5.68 - 5.11, 2) == 0.57 and round(9 + 3.39 + 7.54, 2) == 19.93
assert round(area([P(*v) for v in F1]), 4) == 89.1
assert round(area([P(*v) for v in F2]), 4) == 118.0825
assert round(area([P(*v) for v in F3]), 4) == 46.7324
assert round(area([P(*v) for v in DOT2]), 4) == round(89.1 - 64.8, 4)
assert min(e for e, _ in F3) > max(e for e, _ in F1)      # 3階の真下に1階はない

# ---- 敷地（配置図の辺長。南西の角を原点に (北, 東)） ----
SW, SE, NE, NW = complex(0, 0), complex(0, 23.43), complex(12.72, 23.43), complex(12.72, 0)
SITE = [SW, SE, NE, NW]
assert round(area(SITE), 4) == 298.0296
# 建物図面の1階（既存建物の1階）：西の辺を筆界から0.90、南の張り出しの南の辺を筆界から0.80に置く
# （距離は外壁まで、寸法は柱の中心から。差の0.10程度は500分の1の図には表れない）
BLD = [complex(11.6, 0.9), complex(11.6, 9.9), complex(2.6, 9.9), complex(2.6, 5.4), complex(0.8, 5.4), complex(0.8, 0.9)]
assert round(area(BLD), 4) == 89.1
# 所在の確認：東西 0.90＋19.93＋2.40＝23.23（敷地23.43より0.20短い＝両端の外壁までの分）→ 建物全体が5番27の中
assert round(0.90 + 19.93 + 2.40, 2) == 23.23 and round(23.43 - 23.23, 2) == 0.20

# ---- 立面の模式図（東, 高さ） ----
EX1, EX2 = rect(0, 0, 9, 3, E_), rect(0, 3, 9, 6, E_)
COR = rect(9, 3, 12.39, 6, E_)
NW1, NW2 = rect(12.39, 3, 19.93, 6, E_), rect(12.39, 6, 19.93, 9, E_)
GROUND = [E_(-4.5, 0), E_(9.6, 0), E_(11.2, 3), E_(24.5, 3)]


def elev_base(z, fills=None, labels=True):
    """立面の模式図の地面・擁壁・建物の外形。fills は塗りの色の辞書。"""
    z.poly(GROUND, color=BLACK, lw=2.4, closed=False)
    z.line(E_(9.6, 0), E_(11.2, 3), color=BLACK, lw=4.0)          # 擁壁
    for key, pts in [('ex1', EX1), ('ex2', EX2), ('cor', COR), ('nw1', NW1), ('nw2', NW2)]:
        col = (fills or {}).get(key)
        z.poly(pts, color=BLACK, lw=2.0, fill=col, alpha=0.3 if col else 0)


def zu01():
    fig, axes = new_figure('新館から外へ出る経路：構造上の独立性はあるが、利用上の独立性がない',
                           '新館には勝手口がなく、道路へ出るには渡り廊下 → 木製ドア → 既存建物の2階の居間 → 1階の玄関を通るしかない（事実関係2）。\n'
                           'だから新館は区分建物にならず、既存建物の増築（建物表題部変更登記）になる',
                           w=16, h=10.5)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    elev_base(z, fills={'ex1': BLUE, 'ex2': BLUE, 'cor': ORANGE, 'nw1': GREEN, 'nw2': GREEN})
    z.free_text(E_(6.9, 1.6), '既存建物 1階', fs=14)
    z.free_text(E_(3.2, 5.0), '既存建物 2階（居間）', fs=14)
    z.free_text(E_(10.7, 5.3), '渡り\n廊下', fs=13)
    z.free_text(E_(16.2, 5.2), '新館 1階', fs=14)
    z.free_text(E_(16.2, 7.6), '新館 2階', fs=14)
    z.free_text(E_(-2.4, 0.9), '道路', fs=15, color=GRAY)
    z.free_text(E_(22.5, 3.7), '4-12側', fs=13, color=GRAY)
    z.free_text(E_(10.0, 0.9), '擁壁', fs=13, color=GRAY, offsets=((30, 0), (34, 8)))
    # 木製ドア（既存建物と渡り廊下の境）と玄関
    z.line(E_(9, 3.1), E_(9, 5.0), color='#8b5a2b', lw=6.0)
    z.line(E_(0, 0.1), E_(0, 2.0), color='#8b5a2b', lw=6.0)
    # 経路（赤い矢印。重なり検査の線には登録しない）
    route = [E_(15.0, 4.0), E_(10.7, 4.0), E_(7.6, 4.0), E_(5.8, 4.0), E_(3.8, 1.2), E_(-1.4, 1.2)]
    for a, b in zip(route, route[1:]):
        ax.annotate('', xy(b), xytext=xy(a), arrowprops=dict(arrowstyle='-|>', color=RED, lw=3.0, mutation_scale=22),
                    zorder=7)
        z.segments.append((xy(a), xy(b)))
    z.callout(E_(9, 4.9), '木製ドアで仕切られている\n→ 構造上の独立性 あり', dirs=(105, 120, 90), dists=(95, 120, 145),
              fs=14, color=GREEN)
    z.callout(E_(4.8, 2.6), '勝手口なし。外へ出るには\n既存建物の居間と玄関を\n通るしかない\n→ 利用上の独立性 なし',
              dirs=(-60, -45, -75), dists=(80, 110, 140), fs=14, color=RED)
    fit(ax, GROUND + NW2, margin=0.06, extra=[xy(E_(-5, -4.5)), xy(E_(25, 10.5))], pad_aspect=True)
    save(fig, [z], 'H28_dai22mon_zu01_deiri_keiro')


def zu02():
    fig, axes = new_figure('階の数え方：見取図の表記ではなく、1個の建物として通して数える',
                           '誤りと正解で、床面積の合計はどちらも253.91㎡（全体の合計では誤りに気づけない）',
                           w=16, h=8, ncols=2)
    fig.subplots_adjust(top=0.84, bottom=0.22)
    PINK = '#e377c2'
    # 左：誤り（各棟の地盤面から数える）
    z = Zu(axes[0], fontsize=14)
    elev_base(z, fills={'ex1': PINK, 'cor': PINK, 'nw1': PINK, 'ex2': YELLOW, 'nw2': YELLOW})
    for p, t in [(E_(4.5, 1.5), '1階'), (E_(4.5, 4.5), '2階'), (E_(16.2, 4.5), '1階'), (E_(16.2, 7.5), '2階')]:
        z.free_text(p, t, fs=17, weight='bold')
    axes[0].set_title('誤り：見取図の表記どおり（藍子）', fontsize=17, weight='bold', color=RED, pad=12)
    fit(axes[0], GROUND + NW2, margin=0.06, extra=[xy(E_(-5, -1)), xy(E_(25, 10))], pad_aspect=True)
    fig.text(0.26, 0.12, '2階建　1階142.38㎡・2階111.53㎡', ha='center', fontsize=17, color=RED, weight='bold')
    # 右：正解
    z2 = Zu(axes[1], fontsize=14)
    elev_base(z2, fills={'ex1': BLUE, 'ex2': GREEN, 'cor': GREEN, 'nw1': GREEN, 'nw2': PURPLE})
    for p, t in [(E_(4.5, 1.5), '1階'), (E_(4.5, 4.5), '2階'), (E_(16.2, 4.5), '2階'), (E_(16.2, 7.5), '3階')]:
        z2.free_text(p, t, fs=17, weight='bold')
    axes[1].set_title('正解：建物全体で通して数える', fontsize=17, weight='bold', color=GREEN, pad=12)
    fit(axes[1], GROUND + NW2, margin=0.06, extra=[xy(E_(-5, -1)), xy(E_(25, 10))], pad_aspect=True)
    fig.text(0.74, 0.12, '渡廊下付き3階建　1階89.10㎡・2階118.08㎡・3階46.73㎡', ha='center', fontsize=16,
             color=GREEN, weight='bold')
    assert round(142.3825 + 111.5324, 4) == round(89.1 + 118.0825 + 46.7324, 4) == 253.9149
    save(fig, [z, z2], 'H28_dai22mon_zu02_kai_ayamari_hikaku')


def site_labels(z):
    OFFS = ((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0))
    for p, t in [(complex(6.36, -1.6), '道路'), (complex(14.0, 11.7), '5-26'), (complex(-1.3, 11.7), '5-28'),
                 (complex(6.36, 25.0), '4-12'), (complex(14.0, 25.2), '4-11'), (complex(-1.3, 25.2), '4-13')]:
        z.free_text(p, t, fs=15, color=GRAY, offsets=OFFS)


def zu03():
    fig, axes = new_figure('本件土地（5番27）の辺長確認図（作図チェック用）',
                           '座標値一覧表はない。配置図の（23.43）（12.72）の長方形で、23.43×12.72＝298.0296が登記記録の地積298.03とほぼ合う。\n'
                           '辺長は作図が正しいかを確かめるためのもので、建物図面には書かない',
                           w=16, h=10.5)
    ax = axes[0]
    z = Zu(ax, fontsize=16)
    z.poly(SITE, color=BLACK, lw=2.6, fill=BLUE, alpha=0.12)
    c = centroid(SITE)
    z.edge_label(SW, SE, '23.43m', c, fs=16, outward=False)
    z.edge_label(SE, NE, '12.72m', c, fs=16, outward=False)
    z.free_text(complex(6.36, 11.7), '5-27\n23.43×12.72＝298.0296\n（登記記録 298.03㎡）', fs=16)
    site_labels(z)
    fit(ax, SITE, margin=0.1, extra=[xy(complex(-3, -3)), xy(complex(16, 27))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H28_dai22mon_zu03_shikichi_henchou')


def zu04():
    fig, axes = new_figure('建物図面（縮尺500分の1）の完成形',
                           '描くのはこの建物の1階（既存建物の1階）だけ（不動産登記規則第82条第1項）。新館・渡り廊下は1階がないので描かない。\n'
                           '距離は外壁まで、配置図どおり小数第2位。配置図の1.48・2.40（新館までの距離）と敷地の辺長は書かない',
                           w=16, h=10.5)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(SITE, color=BLACK, lw=2.2)
    z.poly(BLD, color=BLACK, lw=2.4, fill=ORANGE, alpha=0.25)
    dist_arrow(z, complex(11.2, 0), complex(11.2, 0.9), '0.90', side=(-46, 0))
    dist_arrow(z, complex(1.3, 0), complex(1.3, 0.9), '0.90', side=(-46, 0))
    dist_arrow(z, complex(0, 5.0), complex(0.8, 5.0), '0.80', side=(0, -22))
    z.free_text(complex(6.36, 16.0), '5-27', fs=17)
    site_labels(z)
    z.free_text(complex(-2.6, 21.5), '（単位：m）', fs=13)
    z.free_text(complex(15.2, 8.0), '家屋番号 5番27　建物の所在 A市B町二丁目5番地27', fs=14,
                offsets=((0, 0), (0, 10), (0, 20)))
    fit(ax, SITE, margin=0.1, extra=[xy(complex(-3.5, -3)), xy(complex(16.5, 27))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H28_dai22mon_zu04_tatemono_zumen')


def zu05():
    fig, axes = new_figure('1階の床面積求積図（柱の中心線＝区画の中心線）',
                           '1階は既存建物の1階だけ：9.00×9.00＝81.0000 ＋ 4.50×1.80＝8.1000 ＝ 89.1000 → 89.10㎡（登記記録と同じ）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(rect(0, 0, 9, 9), color=BLUE, lw=0, fill=BLUE, alpha=0.2, check=False)
    z.poly(rect(0, 9, 4.5, 10.8), color=ORANGE, lw=0, fill=ORANGE, alpha=0.4, check=False)
    z.line(P(0, 9), P(4.5, 9), color=GRAY, lw=1.2, ls='--')
    f1 = [P(*v) for v in F1]
    z.poly(f1, color=BLACK, lw=2.4)
    dims(z, f1, ['9.00', '9.00', '4.50', '1.80', '4.50', '10.80'])
    z.free_text(P(4.5, 4.5), '北側\n9.00×9.00\n＝81.0000', fs=16)
    z.free_text(P(2.25, 9.9), '4.50×1.80\n＝8.1000', fs=13)
    fit(ax, f1, margin=0.2, extra=[xy(P(-3, 13.5))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H28_dai22mon_zu05_1kai_kyuuseki')


def zu06():
    fig, axes = new_figure('2階の床面積求積図（既存建物の2階・渡り廊下・新館の1階）',
                           '64.8000 ＋ 5.1528 ＋ 45.9459 ＋ 2.1838 ＝ 118.0825 → 118.08㎡。南の辺は一直線の19.93（9.00＋3.39＋7.54）。\n'
                           '新館の北の辺は既存建物より0.57南（5.68−5.11）。点線は1階のうち2階の外にある部分（1階の位置）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    for r, col in [(rect(0, 0, 9, 7.2), BLUE), (rect(9, 5.68, 12.39, 7.2), ORANGE),
                   (rect(12.39, 0.57, 19.32, 7.2), GREEN), (rect(19.32, 3.62, 19.93, 7.2), PURPLE)]:
        z.poly(r, color=col, lw=0, fill=col, alpha=0.28, check=False)
    z.line(P(9, 5.68), P(9, 7.2), color=GRAY, lw=1.2, ls='--')
    z.line(P(19.32, 3.62), P(19.32, 7.2), color=GRAY, lw=1.2, ls='--')
    f2 = [P(*v) for v in F2]
    z.poly([P(*v) for v in DOT2], color=BLACK, lw=1.5, ls=':', closed=False)
    z.poly(f2, color=BLACK, lw=2.4)
    dims(z, f2, ['9.00', None, None, None, '6.93', '3.05', '0.61', '3.58', '19.93', '7.20'], fs=13)
    # へこみ（既存建物と新館の間、渡り廊下の北）の3辺は、へこみの側に書く
    z.free_text(P(9, 2.84), '5.68', fs=13, rotation=90, offsets=((12, 0), (16, 0)))
    z.free_text(P(12.39, 3.12), '5.11', fs=13, rotation=90, offsets=((-12, 0), (-16, 0)))
    z.free_text(P(10.7, 5.68), '3.39', fs=13, offsets=((0, 12), (0, 16)))
    z.free_text(P(4.5, 3.3), '既存建物の2階\n9.00×7.20\n＝64.8000', fs=14)
    z.free_text(P(10.7, 6.44), '渡り廊下\n3.39×1.52', fs=11)
    z.free_text(P(15.85, 3.9), '新館の1階\n6.93×6.63\n＝45.9459', fs=14)
    z.callout(P(19.62, 5.4), '0.61×3.58\n＝2.1838', dirs=(0, 15, -15), dists=(50, 65, 80), fs=12, color=PURPLE)
    z.free_text(P(2.25, 9.4), '点線＝1階の位置', fs=12, color=GRAY)
    fit(ax, [P(-1, -1), P(22, 11.5)], margin=0.06, pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H28_dai22mon_zu06_2kai_kyuuseki')


def zu07():
    fig, axes = new_figure('3階の床面積求積図（新館の2階）',
                           '6.63×6.63＝43.9569 ＋ 0.91×3.05＝2.7755 ＝ 46.7324 → 46.73㎡。〇印は新館の1階と重なる角（事実関係8（6））。\n'
                           '3階の真下に1階はないので、西に離れた1階の外形を丸ごと点線で描く（不動産登記規則第83条第1項）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(rect(12.39, 0.57, 19.02, 7.2), color=GREEN, lw=0, fill=GREEN, alpha=0.25, check=False)
    z.poly(rect(19.02, 0.57, 19.93, 3.62), color=PURPLE, lw=0, fill=PURPLE, alpha=0.3, check=False)
    z.line(P(19.02, 0.57), P(19.02, 3.62), color=GRAY, lw=1.2, ls='--')
    f3 = [P(*v) for v in F3]
    z.poly([P(*v) for v in F1], color=BLACK, lw=1.5, ls=':')
    z.poly(f3, color=BLACK, lw=2.4)
    dims(z, f3, ['7.54', '3.05', '0.91', '3.58', '6.63', '6.63'], fs=13)
    z.free_text(P(15.7, 4.5), '6.63×6.63\n＝43.9569', fs=15)
    z.callout(P(19.47, 2.1), '0.91×3.05\n＝2.7755', dirs=(0, 15, -15), dists=(50, 65, 80), fs=12, color=PURPLE)
    for v in [(12.39, 0.57), (12.39, 7.2)]:
        ax.plot(*xy(P(*v)), 'o', ms=16, mfc='none', mec=BLACK, mew=1.6, zorder=6)
        z.markers.append(xy(P(*v)))
    z.free_text(P(4.5, 5.4), '点線＝1階の位置\n（既存建物の1階）', fs=13, color=GRAY)
    fit(ax, [P(-1, -1), P(22, 11.5)], margin=0.06, pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'H28_dai22mon_zu07_3kai_kyuuseki')


def zu08():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　2階・3階の求積と作図は後に回す', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '前文・注・\n問を読む', '登記の目的は\n前文にある', BLUE),
        ('②', '事実関係の\n3つの一文に印', '事実関係2・\n6（4）・8（5）', BLUE),
        ('③', '問2の理由', '第2欄', BLUE),
        ('④', '申請書の\n床面積以外', '第1欄（構造・\n原因・1階まで）', BLUE),
        ('⑤', '寸法の累計\nメモと求積', '2階・3階の\n床面積', RED),
        ('⑥', '各階平面図と\n建物図面', '第3欄（左に\n各階平面図）', RED),
        ('⑦', '見直し', '渡廊下付き・\n1階・②③・点線', GRAY),
    ]
    w, h, gap = 12.2, 42, 1.8
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 22), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 22 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
        ax.text(x + w / 2, 22 + h / 2 - 3, t, ha='center', va='center', fontsize=16)
        ax.text(x + w / 2, 18, ran, ha='center', va='top', fontsize=14, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, 43), xytext=(x + w + 0.2, 43),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 2 * (w + gap) - gap / 2, 76, '2階・3階の求積をしなくても書ける', ha='center', fontsize=15, color=BLUE,
            weight='bold')
    ax.annotate('', xy=(1 + 4 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 5 * (w + gap) - gap / 2, 76, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 6 * (w + gap) - gap, 72), xytext=(1 + 4 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '2階は既存建物・渡り廊下・新館の寸法線をつなぎ、3階は1階と離れた位置に描くので時間がかかる。\n'
             '階の数え方（3階建）さえ決めれば、第1欄は2階・3階の床面積を除いて先に書ける。1階89.10は登記記録から写せる。',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'H28_dai22mon_zu08_toku_junban.png')
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
