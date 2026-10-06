"""平成22年度 第22問（建物）の解説図16枚を、座標値・寸法から作図してPNGに書き出す。

`../prompt_H22_dai22mon_kaisetsuzu.md` の図1〜図16どおり（図番号は記事の挿入順）。作図の共通部品は `tools/zu_helpers.py`。

座標の約束：
- 敷地の点A〜Gは〔調査結果〕1の表1（X＝北、Y＝東）。敷地は座標の軸に対して傾いているので、
  答案用紙（その3）の建物図面と同じ向き（道路が横、方位記号は右上へ30度傾く）で描くため、
  E点を原点に、道路の向き（E→F、北から東へ約60度）を横軸 u、それと直角に24番の側を縦軸 v とした「図面の座標」に回して使う。
  zu_helpers の点（北, 東）には、縦＝v、横＝u を入れる（complex(v, u)）。方位記号は自前で傾けて描く（tilted_north）。
- 建物の寸法は、1階の床面積の線（柱の中心線＝壁の中心線。〔見取図〕の（注）1）で、原点＝1階の西南西の辺と北北西の辺の延長の交点、
  横 x（東北東へ）・縦 s（南南東へ、道路の向き）で持つ。建物図面では、西南西の外壁が境から4.40・道路から12.00
  （21番の建物図面の距離。〔調査結果〕3で外壁まで。柱の中心は外壁から0.10内側〈〔見取図〕の（注）2〉）に置く。
- 図3（建物図面）と図7（各階平面図）の完成形は、試験の答案用紙（その3）の欄（家屋番号・建物の所在、
  建物図面の申請人・縮尺1/500、各階平面図の作成者〈印刷済み〉・縮尺1/250）の形の枠の中に描く
  （答案用紙はリポジトリの public/kijutsu/H22-tatemono/a3.webp）。
実行: python3 note-articles-Kijyutsu/H22/Q22/zu/draw_H22_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import cmath
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN,  # noqa: E402
                        PURPLE)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []

# ---- 敷地（表1。X＋Yi）→ 図面の座標 ----
SV = {'A': complex(186.65, 163.48), 'B': complex(180.65, 153.09), 'C': complex(171.65, 137.50),
      'D': complex(167.32, 140.00), 'E': complex(150.00, 150.00), 'F': complex(159.00, 165.59),
      'G': complex(165.00, 175.98)}
ANG = cmath.phase(SV['F'] - SV['E'])            # 道路の向き（北から東へ 60°00′08.84″）


def site(p):
    """表1の点（X＋Yi）を図面の座標 complex(v, u) にする。"""
    w = (p - SV['E']) / cmath.rect(1, ANG)
    return complex(-w.imag, w.real)


A, B, C, D, E, F, G = (site(SV[k]) for k in 'ABCDEFG')
LOT21, LOT22 = [C, B, F, E, D], [B, A, G, F]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


assert round(math.degrees(ANG), 4) == 60.0025
assert round(abs(F - E), 2) == 18.00 and round(abs(C - E), 2) == 25.00 and round(abs(A - B), 2) == 12.00
assert round(abs(D - E), 2) == 20.00 and round(abs(C - D), 2) == 5.00 and round(abs(G - A), 2) == 25.00
assert round(area(LOT21), 2) == 450.02 and round(area(LOT22), 2) == 299.94     # 登記記録は449.00・301.00
c_ = (SV['F'] - SV['E']).conjugate() * (SV['C'] - SV['E'])                       # 直角の確認
assert (round(c_.real, 3), round(c_.imag, 4)) == (-0.025, -450.0235)

# ---- 建物（床面積の線。(x, s)） ----
B21 = [(1.80, 0), (9.90, 0), (9.90, 9.00), (0, 9.00), (0, 4.50), (1.80, 4.50)]
EXT = [(9.90, 0), (14.90, 0), (14.90, 9.00), (9.90, 9.00)]
B22 = [(14.90, 0), (23.00, 0), (23.00, 5.40), (21.65, 5.40), (21.65, 9.00), (14.90, 9.00)]
F1 = [(1.80, 0), (23.00, 0), (23.00, 5.40), (21.65, 5.40), (21.65, 9.00), (0, 9.00), (0, 4.50), (1.80, 4.50)]
F1_WRONG = [(1.80, 0), (23.00, 0), (23.00, 3.60), (21.65, 3.60), (21.65, 9.00), (0, 9.00), (0, 4.50), (1.80, 4.50)]
F2 = [(1.80, 0), (9.00, 0), (9.00, 7.20), (1.80, 7.20)]


def P(x, s):
    """求積図用：(x, s) を complex(縦, 横) にする（上＝北北西）。"""
    return complex(-s, x)


U0, V0 = 4.40 + 0.10, 12.00 + 0.10 + 9.00       # 1階の床面積の線の原点（西南西の辺の線 u、北北西の辺の線 v）


def S(x, s):
    """建物図面用：(x, s) を図面の座標に置く。"""
    return complex(V0 - s, U0 + x)


for pts, want in [(B21, 81.00), (EXT, 45.00), (B22, 68.04), (F1, 194.04), (F1_WRONG, 191.61), (F2, 51.84)]:
    assert round(area([P(*v) for v in pts]), 4) == want
assert round(81.00 + 45.00 + 68.04, 2) == 194.04
assert round(23.00 * 9.00 - 1.80 * 4.50 - 1.35 * 3.60, 2) == 194.04 and round(23.00 * 9.00 - 1.80 * 4.50 - 1.35 * 5.40, 2) == 191.61
BLDG = [S(*v) for v in F1]
assert round(area(BLDG), 4) == 194.04
# 所在：21番と22番の境（B－F、u≒18.00）で1階を分ける
LINE = 18.00 - U0                                 # 境は建物の原点から13.50
on21 = round(81.00 + (LINE - 9.90) * 9.00, 2)
assert (round(LINE, 2), on21, round(194.04 - on21, 2)) == (13.50, 113.40, 80.64)
# 東北東の境まで：4.40＋0.10＋21.65＋0.10＝26.25 → 30.00との差は3.75（22番の古い建物図面は3.85）
assert round(30.00 - (4.40 + 0.10 + 21.65 + 0.10), 2) == 3.75


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def dims(z, pts, labels, fs=14, outward=True):
    c = centroid(pts)
    for i, t in enumerate(labels):
        if isinstance(t, tuple):     # 短い辺（欠けの段の1.35など）は引き出し線で外へ出す
            m = (pts[i] + pts[(i + 1) % len(pts)]) / 2
            z.callout(m, t[0], dirs=t[1], dists=(35, 50, 65, 80), fs=fs, color=BLACK)
        elif t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs, outward=outward)


def dist_arrow(z, p, q, text, color=BLACK, fs=15, side=(8, 0)):
    """筆界から外壁までの距離の矢印（両向き）と数値。"""
    z.ax.annotate('', xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='<|-|>', color=color, lw=1.6,
                                                           mutation_scale=12, shrinkA=0, shrinkB=0), zorder=6)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    return z.free_text(m, text, fs=fs, color=color,
                       offsets=(side, (-side[0], -side[1]), (0, 12), (0, -12), (side[0] * 2, side[1] * 2)),
                       ha='center', va='center')


def tilted_north(z, pos=(0.90, 0.72), length=0.13):
    """方位記号。北は図面の上から時計回りに約30度（答案用紙の印刷の方位記号と同じ向き）。"""
    ax = z.ax
    fig = ax.figure
    fig.canvas.draw()
    bb = ax.get_window_extent()
    tilt = 90 - math.degrees(ANG)                    # 図面の上から時計回りの角（29°59′51″）
    assert abs(tilt - 30) < 0.01
    dx, dy = math.sin(math.radians(tilt)) * length, math.cos(math.radians(tilt)) * length
    dx *= bb.height / bb.width                       # 軸の縦横比の補正（見た目の長さをそろえる）
    x0, y0 = pos
    ax.annotate('', xy=(x0 + dx, y0 + dy), xytext=(x0, y0), xycoords='axes fraction',
                arrowprops=dict(arrowstyle='-|>', lw=2.2, color=BLACK, mutation_scale=22))
    t = ax.text(x0 + dx * 1.35, y0 + dy * 1.35, 'N', transform=ax.transAxes, ha='center', va='center',
                fontsize=z.fs + 3, weight='bold')
    z.labels.append(t)
    to_data = (ax.transAxes + ax.transData.inverted()).transform
    z.segments.append((tuple(to_data((x0, y0))), tuple(to_data((x0 + dx, y0 + dy)))))


NEIGHBORS = [(complex(28.5, 6.0), '24'), (complex(12.0, 33.5), '23'), (complex(23.0, -4.5), '13'),
             (complex(10.0, -4.5), '12'), (complex(-4.0, 15.0), '道　路')]
OFFS = ((0, 0), (0, 14), (0, -14), (18, 0), (-18, 0), (26, 0), (-26, 0))


def zu02():
    fig, axes = new_figure('問1と問2：障壁1枚で、申請する登記が変わる',
                           '同じ増改築工事（平成22年7月30日完了）でも、21番と増築部分の間の障壁（イ・ロの線）を残せば区分建物、\n'
                           '取り払えば合体。問1は建物表題部変更登記の一括申請（不動産登記法第52条第3項）、\n'
                           '問2は合体による登記等（同法第49条第1項）',
                           w=16, h=10, ncols=2)
    fig.subplots_adjust(top=0.84, bottom=0.2)
    ext = [P(0, -3.2), P(23, 13.5)]
    # 問1
    z = Zu(axes[0], fontsize=13)
    fit(axes[0], ext, margin=0.04, pad_aspect=True)
    z.poly([P(*v) for v in B21], color=BLACK, lw=2.2, fill=BLUE, alpha=0.2)
    z.poly([P(*v) for v in EXT] , color=GREEN, lw=0, fill=GREEN, alpha=0.22, check=False)
    z.poly([P(*v) for v in B22], color=GREEN, lw=0, fill=GREEN, alpha=0.22, check=False)
    z.poly([P(9.90, 0), P(23.00, 0), P(23.00, 5.40), P(21.65, 5.40), P(21.65, 9.00), P(9.90, 9.00)],
           color=BLACK, lw=2.2, closed=False)
    z.line(P(9.90, 0), P(9.90, 9.00), color=RED, lw=4.0)
    z.line(P(14.90, 0), P(14.90, 9.00), color=GRAY, lw=1.6, ls='--')
    z.free_text(P(5.2, 6.3), '21番\n大面太郎', fs=13)
    z.free_text(P(17.5, 3.0), '22番＋増築部分\n大面健一郎', fs=13)
    z.callout(P(9.90, 4.5), '障壁を残す\n（イ・ロの線）', dirs=(-90, -80, -100), dists=(70, 90, 110), fs=12, color=RED)
    z.callout(P(14.90, 7.0), '障壁を除去', dirs=(-60, -50, -70), dists=(60, 80), fs=12, color=GRAY)
    z.free_text(P(11.5, 11.7), '一棟の建物の中の2個の区分建物\n→ 建物表題部変更登記を一括で', fs=14, color=PURPLE,
                offsets=((0, 0), (0, -8)))
    axes[0].set_title('問1：障壁を残す', fontsize=18, weight='bold', pad=12)
    # 問2
    z2 = Zu(axes[1], fontsize=13)
    fit(axes[1], ext, margin=0.04, pad_aspect=True)
    z2.poly([P(*v) for v in F1], color=BLACK, lw=2.6, fill=ORANGE, alpha=0.25)
    z2.line(P(9.90, 0), P(9.90, 9.00), color=RED, lw=1.6, ls='--')
    z2.line(P(14.90, 0), P(14.90, 9.00), color=RED, lw=1.6, ls='--')
    z2.free_text(P(5.2, 6.3), '元の21番', fs=13)
    z2.free_text(P(12.4, 4.5), '元の\n増築\n部分', fs=12)
    z2.free_text(P(18.2, 3.0), '元の22番', fs=13)
    z2.callout(P(9.90, 8.0), '障壁を除去', dirs=(-100, -110, -90), dists=(55, 75), fs=12, color=RED)
    z2.callout(P(14.90, 8.0), '障壁を除去', dirs=(-80, -70, -60), dists=(55, 75), fs=12, color=RED)
    z2.free_text(P(11.5, 12.2), '1個の居宅（家屋番号は新しく付く）\n→ 合体による登記等', fs=14, color=PURPLE,
                 offsets=((0, 0), (0, -8)))
    axes[1].set_title('問2：障壁を除く', fontsize=18, weight='bold', pad=12)
    save(fig, [z, z2], 'H22_dai22mon_zu02_toi1_toi2')


def road(z):
    """道路との境（E－G）の延長と、道路の向こう側の線（幅員8m。〔調査結果〕10）。"""
    z.line(complex(0.0, -6.0), E, color=BLACK, lw=1.6)
    z.line(G, complex(0.0, 36.0), color=BLACK, lw=1.6)
    z.line(complex(-8.0, -6.0), complex(-8.0, 36.0), color=GRAY, lw=1.2)


def zu03():
    fig, axes = new_figure('21番・22番（敷地）の辺長確認図（作図チェック用）',
                           '座標の軸に対して傾いた長方形（21番18.00×25.00、22番12.00×25.00）。C・D・Eは一直線。\n'
                           '答案用紙の方位記号と同じ向き（道路が横）に回して描いた。座標から出す面積は21番450.02㎡・22番299.94㎡\n'
                           '（登記記録449.00・301.00）。辺長は作図のチェック用で、建物図面には書かない',
                           w=16, h=11.5)
    fig.subplots_adjust(bottom=0.17)
    ax = axes[0]
    z = Zu(ax, fontsize=16)
    fit(ax, LOT21 + LOT22, margin=0.1, extra=[xy(complex(-9, -8)), xy(complex(30, 38))], pad_aspect=True)
    tilted_north(z)
    z.poly(LOT21, color=BLACK, lw=2.6, fill=BLUE, alpha=0.12)
    z.poly(LOT22, color=BLACK, lw=2.6, fill=GREEN, alpha=0.12)
    z.line(D, complex(D.real, D.imag - 6.0), color=BLACK, lw=1.6)
    road(z)
    for p in [A, B, C, D, E, F, G]:
        z.point(p)
    cc = complex(12.5, 15.0)
    for p, n in zip([A, B, C, D, E, F, G], 'ABCDEFG'):
        z.point_label(p, n, away=cc, fs=19)
    c1, c2 = centroid(LOT21), centroid(LOT22)
    z.edge_label(C, B, '18.00m', c1, fs=16, outward=False)
    z.edge_label(B, A, '12.00m', c2, fs=16, outward=False)
    z.edge_label(A, G, '25.00m', c2, fs=16, outward=True)
    z.edge_label(G, F, '12.00m', c2, fs=16, outward=False)
    z.edge_label(F, E, '18.00m', c1, fs=16, outward=False)
    z.edge_label(E, D, '20.00m', c1, fs=16, outward=False)
    z.edge_label(D, C, '5.00m', c1, fs=16, outward=False)
    z.edge_label(B, F, '25.00m', c1, fs=16, outward=False)
    z.free_text(complex(12.5, 9.0), '21番\n18.00×25.00', fs=18, offsets=OFFS)
    z.free_text(complex(12.5, 24.0), '22番\n12.00×25.00', fs=16, offsets=OFFS)
    for p, t in NEIGHBORS:
        z.free_text(p, t, fs=15, color=GRAY, offsets=OFFS)
    save(fig, [z], 'H22_dai22mon_zu03_shikichi_henchou')


INK = '#1a3a8f'   # 記入（濃い青）


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.01
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


SHOZAI = 'A市D町一丁目21番地、22番地'
SHINSEININ = '大面太郎　大面健一郎'
SAKUSEISHA = 'A市F町二丁目6番8号　土地家屋調査士　波臼良子'   # 答案用紙（その3）に印刷済み（職印・作成日つき）


def zu06():
    setup_font()
    fig = plt.figure(figsize=(16.5, 14), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面の完成形（答案用紙（その3）の欄・縮尺1/500で描く内容）', fontsize=22, weight='bold', y=0.985)
    # 答案用紙（その3）の建物図面の欄（家屋番号・建物の所在は用紙の上、申請人・縮尺は下）
    cell(fig, 0.06, 0.885, 0.20, 0.935, '家屋番号', fs=15)
    cell(fig, 0.20, 0.885, 0.46, 0.935)                       # 合体後の家屋番号は登記官が付けるので空欄
    fig.text(0.70, 0.910, '建　物　図　面', ha='center', va='center', fontsize=20)
    cell(fig, 0.06, 0.835, 0.20, 0.885, '建物の所在', fs=15)
    cell(fig, 0.20, 0.835, 0.94, 0.885, SHOZAI, fs=16, ha='left', color=INK)
    cell(fig, 0.06, 0.125, 0.94, 0.835, lw=1.8)
    cell(fig, 0.06, 0.075, 0.20, 0.125, '申　請　人', fs=15)
    cell(fig, 0.20, 0.075, 0.74, 0.125, SHINSEININ, fs=16, color=INK)
    cell(fig, 0.74, 0.075, 0.83, 0.125, '縮尺', fs=15)
    cell(fig, 0.83, 0.075, 0.94, 0.125, '1/500', fs=15)
    fig.text(0.92, 0.140, '（単位：m）', ha='right', va='center', fontsize=13)
    fig.text(0.5, 0.035, '1階の形を、21番の部分の外壁までの距離（境から4.40が2か所、道路から12.00）で置く。1階は21番の上が113.40㎡・'
             '22番の上が80.64㎡なので所在は「21番地、22番地」。\n家屋番号は登記官が付けるので空欄、申請人の欄は（略）と印刷されていないので2人の氏名を書く。'
             '敷地の辺長と東北東の3.85は書かない。方位記号は答案用紙に印刷済み', ha='center', va='center', fontsize=13,
             linespacing=1.6)
    ax = fig.add_axes([0.08, 0.16, 0.84, 0.66])
    z = Zu(ax, fontsize=15)
    fit(ax, LOT21 + LOT22, margin=0.1, extra=[xy(complex(-9, -8)), xy(complex(30, 38))], pad_aspect=True)
    tilted_north(z, pos=(0.06, 0.72))
    z.poly(LOT21, color=BLACK, lw=2.2)
    z.poly(LOT22, color=BLACK, lw=2.2)
    z.line(D, complex(D.real, D.imag - 6.0), color=BLACK, lw=1.6)
    road(z)
    z.poly(BLDG, color=BLACK, lw=2.4)
    wu = U0 - 0.10                       # 西南西の外壁（境から4.40）
    dist_arrow(z, complex(V0 - 4.50, wu), complex(V0 - 4.50, 0.0), '4.40', side=(0, 14))
    dist_arrow(z, complex(12.00, wu), complex(12.00, 0.0), '4.40', side=(0, -14))
    dist_arrow(z, complex(12.00, wu), complex(0.0, wu), '12.00', side=(-28, 0))
    for p, t in [(complex(4.5, 9.0), '21'), (complex(4.5, 24.0), '22')]:
        z.free_text(p, t, fs=17, offsets=OFFS)
    for p, t in NEIGHBORS:
        z.free_text(p, t, fs=15, offsets=OFFS)
    save(fig, [z], 'H22_dai22mon_zu06_tatemono_zumen')


def zu07():
    fig, axes = new_figure('1階の誤り比較図：22番の欠けの奥行きは3.60（5.40ではない）',
                           '全体の長方形23.00×9.00＝207.00から欠けを引くと、どの寸法が欠けの辺かを取り違えやすい。\n'
                           '誤り：207.00－8.10－1.35×5.40＝191.61　／　正解：欠けは東南東の角の1.35×3.60。\n'
                           '長方形に分けて足す：1.80×4.50＋19.85×9.00＋1.35×5.40＝194.04㎡',
                           w=16, h=9.5, ncols=2)
    fig.subplots_adjust(top=0.85, bottom=0.2, wspace=0.10)
    z = Zu(axes[0], fontsize=13)
    fit(axes[0], [P(*v) for v in F1], margin=0.10, pad_aspect=True)
    wrong = [P(*v) for v in F1_WRONG]
    z.poly(wrong, color=RED, lw=2.2, fill=RED, alpha=0.15)
    dims(z, wrong, ['21.20', '3.60', '1.35', '5.40', '21.65', '4.50', '1.80', '4.50'], fs=13)
    z.free_text(P(11.0, 4.6), '207.00－8.10－7.29\n＝191.61㎡', fs=15, color=RED)
    axes[0].set_title('誤り：欠けの奥行きを5.40と取り違え', fontsize=16, weight='bold', color=RED, pad=12)
    z3 = Zu(axes[1], fontsize=13)
    ok = [P(*v) for v in F1]
    fit(axes[1], ok, margin=0.10, pad_aspect=True)
    z3.poly(ok, color=GREEN, lw=2.4, fill=GREEN, alpha=0.18)
    dims(z3, ok, ['21.20', '5.40', '1.35', '3.60', '21.65', '4.50', '1.80', '4.50'], fs=13)
    z3.free_text(P(11.0, 4.6), '194.04㎡', fs=16, color=GREEN)
    axes[1].set_title('正解：欠けは東南東の角の1.35×3.60', fontsize=16, weight='bold', color=GREEN, pad=12)
    save(fig, [z, z3], 'H22_dai22mon_zu07_1kai_ayamari_hikaku')


def zu08():
    fig, axes = new_figure('1階の床面積求積図（柱の中心線＝壁の中心線）',
                           '① 1.80×4.50＝8.1000 ＋ ② 19.85×9.00＝178.6500 ＋ ③ 1.35×5.40＝7.2900\n'
                           '＝ 194.0400 → 194.04㎡。'
                           '検算：元の21番81.00＋増築部分45.00＋元の22番68.04＝194.04',
                           w=16, h=10.5)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    fit(ax, [P(*v) for v in F1], margin=0.14, extra=[xy(P(11.5, 13.0)), xy(P(-9, 9)), xy(P(32, -3.5))], pad_aspect=True)
    r1, r2, r3 = [P(0, 4.50), P(1.80, 4.50), P(1.80, 9.00), P(0, 9.00)], \
        [P(1.80, 0), P(21.65, 0), P(21.65, 9.00), P(1.80, 9.00)], [P(21.65, 0), P(23.00, 0), P(23.00, 5.40), P(21.65, 5.40)]
    z.poly(r1, color=ORANGE, lw=0, fill=ORANGE, alpha=0.4, check=False)
    z.poly(r2, color=BLUE, lw=0, fill=BLUE, alpha=0.2, check=False)
    z.poly(r3, color=GREEN, lw=0, fill=GREEN, alpha=0.3, check=False)
    z.line(P(1.80, 4.50), P(1.80, 9.00), color=GRAY, lw=1.2, ls='--')
    z.line(P(21.65, 0), P(21.65, 5.40), color=GRAY, lw=1.2, ls='--')
    f1 = [P(*v) for v in F1]
    z.poly(f1, color=BLACK, lw=2.4)
    dims(z, f1, ['21.20', '5.40', ('1.35', (-30, -15, -45)), '3.60', '21.65', '4.50', '1.80', '4.50'], fs=15)
    z.free_text(P(11.7, 4.5), '②中央\n19.85×9.00＝178.6500', fs=16)
    z.callout(P(0.9, 6.75), '①西南西の端\n1.80×4.50＝8.1000', dirs=(255, 265, 245, 235), dists=(90, 110, 130), fs=13)
    z.callout(P(22.3, 2.7), '③東北東の端\n1.35×5.40＝7.2900', dirs=(20, 30, 10, 40), dists=(110, 140, 170), fs=13)
    z.free_text(P(11.5, 12.2), '1階 床面積：194.04㎡', fs=18, weight='bold', offsets=OFFS)
    save(fig, [z], 'H22_dai22mon_zu08_1kai_kyuuseki')


def zu10():
    fig, axes = new_figure('2階の床面積求積図（1階の位置を点線で重ねる）',
                           '2階は元の21番の2階だけ：7.20×7.20＝51.84㎡。1階の北北西の辺にそろい、\n'
                           '西南西の辺は欠けの奥の壁の線（1.80）にそろう。元の21番の東北東の壁より0.90、道路側の壁より1.80内側',
                           w=16, h=10.5)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    fit(ax, [P(*v) for v in F1], margin=0.14, extra=[xy(P(11.5, 13.0))], pad_aspect=True)
    f2 = [P(*v) for v in F2]
    z.poly(f2, color=BLACK, lw=2.6, fill=BLUE, alpha=0.25)
    rest = [P(9.00, 0), P(23.00, 0), P(23.00, 5.40), P(21.65, 5.40), P(21.65, 9.00), P(0, 9.00), P(0, 4.50), P(1.80, 4.50),
            P(1.80, 7.20)]
    z.poly(rest, color=BLACK, lw=1.6, ls=':', closed=False)
    dims(z, f2, ['7.20', '7.20', '7.20', '7.20'], fs=15)
    z.free_text(P(5.4, 3.6), '2階\n7.20×7.20\n＝51.8400', fs=15)
    z.free_text(P(16.0, 4.5), '点線＝1階の位置（2階はない）', fs=15, color=GRAY)
    z.free_text(P(11.5, 12.2), '2階 床面積：51.84㎡', fs=18, weight='bold', offsets=OFFS)
    save(fig, [z], 'H22_dai22mon_zu10_2kai_kyuuseki')


def zu11():
    setup_font()
    fig = plt.figure(figsize=(18, 10.5), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図の完成形（答案用紙（その3）の欄・縮尺1/250で描く内容）', fontsize=22, weight='bold', y=0.975)
    fig.text(0.5, 0.905, '各　階　平　面　図', ha='center', va='center', fontsize=20)
    cell(fig, 0.04, 0.17, 0.96, 0.88, lw=1.8)
    cell(fig, 0.04, 0.10, 0.14, 0.17, '作　成　者', fs=15)
    cell(fig, 0.14, 0.10, 0.80, 0.17)
    fig.text(0.16, 0.135, SAKUSEISHA, ha='left', va='center', fontsize=14)
    fig.text(0.535, 0.135, '職印', ha='center', va='center', fontsize=13,
             bbox=dict(boxstyle='square,pad=0.25', fc='white', ec=BLACK, lw=1.0))
    fig.text(0.78, 0.135, '（平成22年8月10日作成）', ha='right', va='center', fontsize=14)
    cell(fig, 0.80, 0.10, 0.87, 0.17, '縮尺', fs=15)
    cell(fig, 0.87, 0.10, 0.96, 0.17, '1/250', fs=15)
    fig.text(0.5, 0.045, '柱の中心線の寸法で「1階」「2階」を書き分け、2階には1階の位置を点線で重ねる。問2(2)のなお書きどおり、求積とその方法、'
             '床面積の表示は書かない（作成者の欄は印刷済み）。\n形が閉じているかの検算：21.20＋1.80＝21.65＋1.35＝23.00、'
             '4.50＋4.50＝5.40＋3.60＝9.00', ha='center', va='center', fontsize=14, linespacing=1.6)
    # 1階と2階は同じ縮尺（1/250）で描くので、同じ大きさのパネルに同じ表示範囲で描く
    axes = [fig.add_axes([0.05, 0.20, 0.44, 0.60]), fig.add_axes([0.51, 0.20, 0.44, 0.60])]
    ext7 = [xy(P(23.0, -4.5))]
    z = Zu(axes[0], fontsize=13)
    f1 = [P(*v) for v in F1]
    fit(axes[0], f1, margin=0.08, extra=ext7, pad_aspect=True)
    z.poly(f1, color=BLACK, lw=2.4)
    dims(z, f1, ['21.20', '5.40', ('1.35', (-30, -15, -45)), '3.60', '21.65', '4.50', '1.80', '4.50'], fs=13)
    axes[0].set_title('1階', fontsize=18, weight='bold', pad=12)
    z2 = Zu(axes[1], fontsize=13)
    f2 = [P(*v) for v in F2]
    fit(axes[1], f1, margin=0.08, extra=ext7, pad_aspect=True)
    tilted_north(z2, pos=(0.86, 0.72), length=0.12)
    z2.poly(f2, color=BLACK, lw=2.4)
    rest = [P(9.00, 0), P(23.00, 0), P(23.00, 5.40), P(21.65, 5.40), P(21.65, 9.00), P(0, 9.00), P(0, 4.50), P(1.80, 4.50),
            P(1.80, 7.20)]
    z2.poly(rest, color=BLACK, lw=1.4, ls=':', closed=False)
    dims(z2, f2, ['7.20', '7.20', '7.20', '7.20'], fs=13)
    axes[1].set_title('2階', fontsize=18, weight='bold', pad=12)
    save(fig, [z, z2], 'H22_dai22mon_zu11_kakai_heimenzu')


def box_fig(title, name, draw, note):
    """固定配置の図（重なり検査の対象外。目視で確認する）。"""
    setup_font()                     # 最初に描く図でも日本語フォントを使う（図1は固定配置の図）
    fig = plt.figure(figsize=(16, 9), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.02, 0.16, 0.96, 0.74])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    draw(ax)
    fig.text(0.5, 0.07, note, ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print(f'[重なり検査] {name}（固定配置）\n  →', path)


def zu15():
    v21, v22, vext = 1200, 530, 45 * 6
    total = v21 + v22 + vext
    kazei = total * 6 // 10
    tax = kazei * 10000 * 4 // 1000
    assert (vext, total, kazei, tax) == (270, 2000, 1200, 48000)

    def draw(ax):
        items = [(4, '元の21番', '固定資産税の\n課税標準額', '1,200万円', BLUE),
                 (27, '元の22番', '固定資産税の\n課税標準額', '530万円', BLUE),
                 (50, '増築部分', '45.00㎡×6万円\n（認定基準表）', '270万円', ORANGE)]
        for x, t, s, v, col in items:
            ax.add_patch(plt.Rectangle((x, 58), 20, 30, facecolor=col, alpha=0.15, edgecolor=col, lw=2))
            ax.text(x + 10, 84, t, ha='center', va='top', fontsize=17, weight='bold')
            ax.text(x + 10, 73, s, ha='center', va='center', fontsize=13)
            ax.text(x + 10, 62, v, ha='center', va='bottom', fontsize=19, weight='bold', color=col)
        ax.text(25.5, 73, '＋', ha='center', va='center', fontsize=26)
        ax.text(48.5, 73, '＋', ha='center', va='center', fontsize=26)
        ax.add_patch(plt.Rectangle((74, 58), 23, 30, facecolor=PURPLE, alpha=0.12, edgecolor=PURPLE, lw=2))
        ax.text(72, 73, '＝', ha='center', va='center', fontsize=26)
        ax.text(85.5, 84, '合体後の建物の価額', ha='center', va='top', fontsize=15, weight='bold')
        ax.text(85.5, 68, '2,000万円', ha='center', va='center', fontsize=24, weight='bold', color=PURPLE)
        steps = [(4, '健一郎さんの持分', '× 10分の6', GREEN), (37, '課税価格', '1,200万円', GREEN),
                 (70, '登録免許税（1000分の4）', '4万8,000円', RED)]
        for x, t, v, col in steps:
            ax.add_patch(plt.Rectangle((x, 12), 27, 30, facecolor=col, alpha=0.13, edgecolor=col, lw=2))
            ax.text(x + 13.5, 37, t, ha='center', va='top', fontsize=16, weight='bold')
            ax.text(x + 13.5, 22, v, ha='center', va='center', fontsize=22, weight='bold', color=col)
        ax.annotate('', xy=(36.5, 27), xytext=(31.5, 27), arrowprops=dict(arrowstyle='-|>', lw=2, color=GRAY))
        ax.annotate('', xy=(69.5, 27), xytext=(64.5, 27), arrowprops=dict(arrowstyle='-|>', lw=2, color=GRAY))
        ax.annotate('', xy=(17.5, 43), xytext=(85.5, 57), arrowprops=dict(arrowstyle='-|>', lw=2, color=GRAY))
        ax.text(4, 96, '所有権の登記がなかったのは22番（健一郎さん）だけ。健一郎さんの所有権の登記（不動産登記法第49条第1項後段）に登録免許税がかかる',
                fontsize=14, va='top')
    box_fig('課税価格と登録免許税の組み立て（所有権の保存の登記）', 'H22_dai22mon_zu15_touroku_menkyozei', draw,
            '工事費の370万円は建物の価額ではない（1,200＋530＋370＝2,100万円で計算しない）。\n'
            '課税価格 2,000万円×10分の6＝1,200万円、登録免許税 1,200万円×1000分の4＝4万8,000円（登録免許税法別表第一の一（一）・第10条）')


def zu16():
    memo = [('昭和51年2月17日', '21番 所有権保存\n抵当権（A銀行・B信用金庫）'), ('平成7年6月14日', '21番 賃借権'),
            ('平成22年7月30日', '工事完了（合体の日）'), ('8月10日', '図面の作成'), ('8月22日', '申請（1月以内）')]
    steps = [('①', '問を\n先に読む', '問1と問2の\n前提の違い', BLUE),
             ('②', '問1', '別紙の数字は\nいらない', BLUE),
             ('③', '時系列\nメモ', '登記記録の\n権利部を見比べる', BLUE),
             ('④', '申請書の\n床面積以外', '目的・申請人・\n所有権・存続登記', BLUE),
             ('⑤', '求積', '合体前の2つ・\n増築・合体後', RED),
             ('⑥', '課税価格', '2,000万×6/10', RED),
             ('⑦', '（その3）\nの作図', '各階平面図と\n建物図面', RED),
             ('⑧', '見直し', '瓦葺の転写・\n存続は1件', GRAY)]

    def draw(ax):
        ax.text(1, 97, '時系列メモ', fontsize=17, weight='bold', va='top')
        ax.plot([2, 98], [84, 84], color=GRAY, lw=2)
        for i, (d, t) in enumerate(memo):
            x = 6 + i * 22
            hot = i == 2
            ax.plot(x, 84, 'o', ms=10, color=RED if hot else GRAY)
            ax.text(x, 88, d, ha='center', va='bottom', fontsize=14, weight='bold', color=RED if hot else BLACK)
            ax.text(x, 80, t, ha='center', va='top', fontsize=12.5)
        w, h, gap = 10.8, 28, 1.6
        for i, (no, t, ran, col) in enumerate(steps):
            x = 1 + i * (w + gap)
            ax.add_patch(plt.Rectangle((x, 24), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
            ax.text(x + w / 2, 24 + h - 3, no, ha='center', va='top', fontsize=22, color=col, weight='bold')
            ax.text(x + w / 2, 24 + h / 2 - 4, t, ha='center', va='center', fontsize=15)
            ax.text(x + w / 2, 20, ran, ha='center', va='top', fontsize=12, color=col)
            if i < len(steps) - 1:
                ax.annotate('', xy=(x + w + gap - 0.1, 38), xytext=(x + w + 0.1, 38),
                            arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
        ax.annotate('', xy=(1 + 4 * (w + gap) - gap, 58), xytext=(1, 58), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
        ax.text(1 + 2 * (w + gap) - gap / 2, 61, '計算しなくても書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
        ax.annotate('', xy=(1 + 7 * (w + gap) - gap, 58), xytext=(1 + 4 * (w + gap), 58),
                    arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
        ax.text(1 + 5.5 * (w + gap) - gap / 2, 61, '時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    box_fig('本番で解く順番　計算のいらない欄を先に', 'H22_dai22mon_zu16_toku_junban', draw,
            '問1は別紙の数字を読まずに書ける。問2も、登記の目的・申請人・所有権登記の表示・存続登記・添付情報は床面積なしで書ける。\n'
            'いちばん時間を食うのは⑦の作図（傾いた敷地を答案用紙の方位記号の向きで描く）。先に埋めておけば、作図で時間が足りなくなっても点は取れている。')


# ---- 2026-10-05追加：本文で説明しているのに図がなかった箇所（図1・4・5・9・12・13・14） ----
def box(ax, x, y, w, h, text, col=BLACK, fs=14, alpha=0.12, weight='normal', tc=BLACK, ha='center', lw=2.0):
    """固定配置の図の箱（左下 x, y、幅 w、高さ h。座標は0〜100）。"""
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=col, alpha=alpha, edgecolor=col, lw=lw))
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor='none', edgecolor=col, lw=lw))
    tx = x + w / 2 if ha == 'center' else x + 1.2
    ax.text(tx, y + h / 2, text, ha=ha, va='center', fontsize=fs, color=tc, weight=weight, linespacing=1.45)


def arrow(ax, p, q, col=GRAY, lw=2.0):
    ax.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle='-|>', lw=lw, color=col, mutation_scale=18))


def zu01():
    """問1の考え方の流れ（第1章、藍子の誤答「22番の増築だけ」の訂正の直後）。"""
    def draw(ax):
        box(ax, 22, 86, 56, 10, '表題登記がある2個の建物（21番・22番）の間を、増築でつないだ', col=GRAY, fs=15)
        arrow(ax, (50, 86), (50, 80))
        box(ax, 30, 70, 40, 10, '21番と増築部分の間の障壁は？', col=PURPLE, fs=16, weight='bold')
        # 問1：残す
        arrow(ax, (38, 70), (25, 62), col=BLUE)
        ax.text(27, 67.5, '残す（問1）', ha='right', fontsize=14, color=BLUE, weight='bold')
        box(ax, 2, 49, 46, 13, '一棟の建物の中に、構造上も利用上も独立した部分が2つ\n'
            '→ 21番も、22番＋増築部分も区分建物になった\n（建物の区分所有等に関する法律第1条）', col=BLUE, fs=13.5)
        arrow(ax, (25, 49), (25, 43), col=BLUE)
        box(ax, 2, 30, 46, 13, '2つとも表題部の登記事項が変わる\n→ 建物表題部変更登記を、21番と22番で一括して申請\n'
            '（不動産登記法第52条第3項）', col=BLUE, fs=13.5)
        arrow(ax, (25, 30), (25, 24), col=BLUE)
        box(ax, 2, 3, 46, 21, '太郎さんが21番の登記を申請しないとき\n→ 健一郎さんが代わって申請できる（同条第4項）\n'
            '代位原因「不動産登記法第52条第4項」\n（債権者代位の「民法第423条」ではない）', col=BLUE, fs=13.5)
        # 問2：除く
        arrow(ax, (62, 70), (76, 62), col=GRAY)
        ax.text(73, 67.5, '除く（問2）', ha='left', fontsize=14, color=GRAY, weight='bold')
        box(ax, 54, 49, 44, 13, '仕切りのない1個の居宅\n→ 合体による登記等（不動産登記法第49条第1項）\n（第5章で）',
            col=GRAY, fs=13.5)
        # 誤答
        box(ax, 54, 14, 44, 26, '誤り：「健一郎さんは22番の増築だけ。\n21番は工事をしていないから登記はいらない」\n\n'
            '→ 21番も区分建物になって表題部の登記事項が\n変わるので、21番の表題部の変更も要る', col=RED, fs=13.5, tc=RED)
    box_fig('問1の考え方：障壁が残ると、工事をしていない21番も区分建物になる', 'H22_dai22mon_zu01_toi1_nagare', draw,
            '22番の増築だけではない。一棟の建物の中の2個の区分建物になったので、21番と22番の表題部の変更の登記を一括して申請する。\n'
            '相手が申請しないときの代位は、不動産登記法が認めた代位（第52条第4項）')


def zu04():
    """東北東の境までの距離の検算（第3章、3.85と3.75の食い違い）。"""
    fig, axes = new_figure('東北東の境までの距離の検算：22番の古い図面の3.85は0.10合わない',
                           '西南西の境から外壁まで4.40、柱の中心まで0.10、1階の道路側の辺（西南西の端から22番の欠けの角まで）21.65、外壁まで0.10。\n'
                           '4.40＋0.10＋21.65＋0.10＝26.25、21番と22番の幅18.00＋12.00＝30.00から引くと3.75（古い図面は3.85）。\n'
                           '建物の位置は、動いていない21番の側の距離（4.40・4.40・12.00）で決め、3.85は建物図面に書かない',
                           w=16, h=11)
    fig.subplots_adjust(bottom=0.19)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    fit(ax, LOT21 + LOT22, margin=0.06, extra=[xy(complex(-9, -8)), xy(complex(30, 38))], pad_aspect=True)
    tilted_north(z)
    z.poly(LOT21, color=BLACK, lw=2.0)
    z.poly(LOT22, color=BLACK, lw=2.0)
    road(z)
    z.poly(BLDG, color=BLACK, lw=2.2, fill=ORANGE, alpha=0.18)
    yv = 7.0                                    # 寸法の鎖を描く高さ（道路と建物の間）
    xs = [0.0, 4.40, 4.50, 26.15, 26.25, 30.00]
    for u in [4.40, 26.25]:                     # 外壁の位置から寸法線まで引き出す
        z.line(complex(12.00, u), complex(yv - 0.8, u), color=GRAY, lw=1.0, ls=':')
    for (a, b), t, col, side in [((0.0, 4.40), '4.40', BLACK, (0, 14)), ((4.50, 26.15), '21.65', BLACK, (-30, 14)),
                                 ((26.25, 30.00), '3.75', RED, (0, 14))]:
        dist_arrow(z, complex(yv, a), complex(yv, b), t, color=col, side=side)
    z.callout(complex(yv, 4.45), '外壁から柱の中心まで\n0.10（両端とも）', dirs=(-100, -80, -120), dists=(55, 75, 95), fs=13)
    z.callout(complex(yv, 28.1), '22番の古い建物図面は3.85\n→ 0.10食い違う', dirs=(-80, -60, -100), dists=(60, 80, 100), fs=13,
              color=RED)
    z.free_text(complex(16.0, -3.6), '西南西\nの境', fs=14, color=GRAY, offsets=OFFS)
    z.free_text(complex(16.0, 33.6), '東北東\nの境', fs=14, color=GRAY, offsets=OFFS)
    for p, t in [(complex(4.5, 9.0), '21'), (complex(4.5, 24.0), '22')]:
        z.free_text(p, t, fs=17, offsets=OFFS)
    assert round(4.40 + 0.10 + 21.65 + 0.10, 2) == 26.25 and round(30.00 - 26.25, 2) == 3.75 and xs[-1] == 30.00
    save(fig, [z], 'H22_dai22mon_zu04_touhokutou_kenzan')


def zu05():
    """所在の確認（第3章、境B－Fが増築部分の中を通る）。"""
    fig, axes = new_figure('所在の確認：21番と22番の境は増築部分の中を通る',
                           '境B－Fは西南西の境から18.00。柱の中心線は西南西の端4.50、元の21番の東北東の壁14.40、増築部分の東北東の端19.40。\n'
                           '増築部分5.00のうち3.60が21番、1.40が22番の上。1階は21番の上81.00＋3.60×9.00＝113.40、22番の上1.40×9.00＋68.04＝80.64、\n'
                           '2階51.84は全部21番の上 → 床面積の多い21番地が先「A市D町一丁目21番地、22番地」（不動産登記事務取扱手続準則第88条第2項）',
                           w=16, h=11)
    fig.subplots_adjust(bottom=0.19)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    fit(ax, LOT21 + LOT22, margin=0.06, extra=[xy(complex(-9, -8)), xy(complex(30, 38))], pad_aspect=True)
    tilted_north(z)
    z.poly(LOT21, color=BLACK, lw=2.0)
    z.poly(LOT22, color=BLACK, lw=2.0)
    road(z)
    left = [(1.80, 0), (LINE, 0), (LINE, 9.00), (0, 9.00), (0, 4.50), (1.80, 4.50)]
    right = [(LINE, 0), (23.00, 0), (23.00, 5.40), (21.65, 5.40), (21.65, 9.00), (LINE, 9.00)]
    assert round(area([S(*v) for v in left]), 2) == 113.40 and round(area([S(*v) for v in right]), 2) == 80.64
    z.poly([S(*v) for v in left], color=BLUE, lw=0, fill=BLUE, alpha=0.25, check=False)
    z.poly([S(*v) for v in right], color=GREEN, lw=0, fill=GREEN, alpha=0.28, check=False)
    z.poly(BLDG, color=BLACK, lw=2.2)
    z.line(S(9.90, 0), S(9.90, 9.00), color=GRAY, lw=1.2, ls='--')
    z.line(S(14.90, 0), S(14.90, 9.00), color=GRAY, lw=1.2, ls='--')
    z.line(B, F, color=RED, lw=2.6)
    yv = V0 + 2.0                                # 増築部分の寸法を描く高さ（建物の北北西）
    dist_arrow(z, complex(yv, U0 + 9.90), complex(yv, U0 + LINE), '3.60', color=BLUE, side=(-6, 14))
    z.ax.annotate('', xy(complex(yv, U0 + 14.90)), xytext=xy(complex(yv, U0 + LINE)),
                  arrowprops=dict(arrowstyle='<|-|>', color=GREEN, lw=1.6, mutation_scale=12, shrinkA=0, shrinkB=0), zorder=6)
    z.segments.append((xy(complex(yv, U0 + LINE)), xy(complex(yv, U0 + 14.90))))
    z.callout(complex(yv, U0 + 14.20), '1.40', dirs=(40, 55, 25), dists=(40, 55, 70), fs=14, color=GREEN)
    z.free_text(S(5.4, 6.4), '21番の上\n113.40㎡', fs=14, color=BLUE, offsets=OFFS)
    z.free_text(S(18.2, 3.6), '22番の上\n80.64㎡', fs=14, color=GREEN, offsets=OFFS)
    z.callout(complex(4.0, 18.0), '21番と22番の境B－F\n（西南西の境から18.00）', dirs=(-60, -120, -45), dists=(50, 70, 90), fs=13,
              color=RED)
    z.callout(S(11.6, 8.0), '増築部分（5.00）', dirs=(-120, -135, -105), dists=(70, 90, 110), fs=13, color=GRAY)
    z.free_text(complex(V0 - 3.0, 33.6), '2階51.84㎡は\n全部21番の上', fs=13, color=BLUE, offsets=OFFS)
    for p, t in [(complex(1.5, 9.0), '21'), (complex(1.5, 24.0), '22')]:
        z.free_text(p, t, fs=17, offsets=OFFS)
    save(fig, [z], 'H22_dai22mon_zu05_shozai_kakunin')


def zu09():
    """合体前の2つと増築部分の検算（第4章。申請書の合体前の行の床面積）。"""
    fig, axes = new_figure('合体前の2つと増築部分で検算（申請書の合体前の行の床面積）',
                           '元の21番 9.90×4.50＋8.10×4.50＝81.00（2階51.84）、増築部分 5.00×9.00＝45.00、元の22番 6.75×9.00＋1.35×5.40＝68.04。\n'
                           '81.00＋45.00＋68.04＝194.04＝合体後の1階。登記記録の抜粋に床面積がないので、合体前の行（81.00・51.84、68.04）もここで出す',
                           w=16, h=10.5)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    f1 = [P(*v) for v in F1]
    fit(ax, f1, margin=0.16, extra=[xy(P(11.5, 13.0))], pad_aspect=True)
    parts = [([(1.80, 0), (9.90, 0), (9.90, 4.50), (1.80, 4.50)], BLUE, 0.16),
             ([(0, 4.50), (9.90, 4.50), (9.90, 9.00), (0, 9.00)], BLUE, 0.30),
             (EXT, ORANGE, 0.35),
             ([(14.90, 0), (21.65, 0), (21.65, 9.00), (14.90, 9.00)], GREEN, 0.30),
             ([(21.65, 0), (23.00, 0), (23.00, 5.40), (21.65, 5.40)], GREEN, 0.16)]
    for pts, col, al in parts:
        z.poly([P(*v) for v in pts], color=col, lw=0, fill=col, alpha=al, check=False)
    z.line(P(1.80, 4.50), P(9.90, 4.50), color=GRAY, lw=1.0, ls='--')
    z.line(P(21.65, 0), P(21.65, 5.40), color=GRAY, lw=1.0, ls='--')
    z.line(P(9.90, 0), P(9.90, 9.00), color=BLACK, lw=1.6)
    z.line(P(14.90, 0), P(14.90, 9.00), color=BLACK, lw=1.6)
    z.poly(f1, color=BLACK, lw=2.4)
    c = centroid(f1)
    for (a, b, t) in [((1.80, 0), (9.90, 0), '8.10'), ((9.90, 0), (14.90, 0), '5.00'), ((14.90, 0), (23.00, 0), '8.10'),
                      ((9.90, 9.00), (0, 9.00), '9.90'), ((14.90, 9.00), (9.90, 9.00), '5.00'),
                      ((21.65, 9.00), (14.90, 9.00), '6.75')]:
        z.edge_label(P(*a), P(*b), t, c, fs=14)
    z.free_text(P(5.85, 2.25), '8.10×4.50\n＝36.45', fs=13)
    z.free_text(P(4.95, 6.75), '9.90×4.50＝44.55', fs=13)
    z.free_text(P(12.40, 4.50), '増築部分\n5.00×9.00\n＝45.00', fs=13)
    z.free_text(P(18.28, 4.50), '6.75×9.00\n＝60.75', fs=13)
    z.callout(P(22.33, 2.70), '1.35×5.40\n＝7.29', dirs=(20, 35, 10), dists=(70, 90, 110), fs=13)
    z.free_text(P(4.95, 11.2), '元の21番　81.00', fs=16, weight='bold', color=BLUE, offsets=OFFS)
    z.free_text(P(12.40, 11.2), '45.00', fs=16, weight='bold', color=ORANGE, offsets=OFFS)
    z.free_text(P(18.95, 11.2), '元の22番　68.04', fs=16, weight='bold', color=GREEN, offsets=OFFS)
    assert round(36.45 + 44.55, 2) == 81.00 and round(60.75 + 7.29, 2) == 68.04 and round(81.00 + 45.00 + 68.04, 2) == 194.04
    save(fig, [z], 'H22_dai22mon_zu09_gattaizen_kenzan')


def zu12():
    """合体後の甲区（所有権の登記）の行き先（第5章、登記の目的の訂正の直後）。"""
    def draw(ax):
        ax.text(14, 97, '合体前（登記記録）', ha='center', va='top', fontsize=17, weight='bold')
        ax.text(76, 97, '合体後の建物の登記記録', ha='center', va='top', fontsize=17, weight='bold')
        box(ax, 1, 72, 30, 18, '21番の建物\n表題部：居宅　木造瓦葺2階建\n甲区1番：所有権保存　大面太郎\n（所有権の登記がある建物）',
            col=BLUE, fs=13)
        box(ax, 1, 40, 30, 18, '22番の建物\n表題部：居宅　木造セメント瓦葺平家建\n所有者　大面健一郎\n権利部：記録事項なし（表題登記だけ）',
            col=GREEN, fs=13)
        box(ax, 52, 76, 47, 14, '表題部：居宅　木造スレートぶき2階建\n家屋番号は登記官が付ける。表題部所有者は記録しない\n'
            '（不動産登記規則第120条第1項）', col=GRAY, fs=13)
        box(ax, 52, 56, 47, 15, '甲区①：合体による所有権の登記　大面太郎　持分10分の4\n登記官が記録する（同条第2項）\n→ 登録免許税はかからない',
            col=BLUE, fs=13)
        box(ax, 52, 34, 47, 17, '甲区②：所有権の保存　大面健一郎　持分10分の6\n合体による登記等と併せて申請する\n'
            '（不動産登記法第49条第1項第4号・後段、不動産登記令第5条第1項）\n→ 登録免許税がかかる（1000分の4）', col=RED, fs=13)
        arrow(ax, (31, 79), (51.5, 63.5), col=BLUE)
        arrow(ax, (31, 49), (51.5, 42.5), col=RED)
        box(ax, 1, 6, 98, 18, '登記の目的：合体後の建物の表題登記及び合体前の建物の表題部の登記の抹消並びに所有権の保存の登記\n'
            '誤り：「並びに所有権の保存の登記」を落とす（22番は表題登記だけで、健一郎さんの所有権の登記がないまま残ってしまう）\n'
            '答案用紙（その2）の「法第74条第1項第1号の規定による新築建物のためにする所有権保存の登記」の欄が合図',
            col=PURPLE, fs=13.5, ha='left')
    box_fig('合体後の甲区（所有権の登記）の行き先：表題登記だけの22番がある', 'H22_dai22mon_zu12_kouku_yukisaki', draw,
            '所有権の登記がある21番の分は登記官が合体による所有権の登記として記録し、表題登記だけの22番の分は、\n'
            '健一郎さんを登記名義人とする所有権の保存の登記を併せて申請する（持分は合意どおり10分の4・10分の6）')


def zu13():
    """乙区の3件の振り分け（第5章、存続登記の表）。"""
    def draw(ax):
        ax.text(1, 97, '21番の乙区（3件）', fontsize=17, weight='bold', va='top')
        ax.text(42, 97, '合体後の建物では', fontsize=17, weight='bold', va='top')
        ax.text(80, 97, '存続登記の表', fontsize=17, weight='bold', va='top')
        rows = [('1番　抵当権設定\nA銀行', '消滅の承諾がある → 登記官が\n権利が消滅した旨を登記する\n（不動産登記法第50条、\n不動産登記規則第120条第5項）',
                 '書かない\n（抵当権消滅承諾\n証明情報を付ける）', GRAY),
                ('2番　抵当権設定\nB信用金庫', '存続登記（不動産登記令別表13の項\n申請情報欄ハ）→ 大面太郎の\n持分10分の4の上に移される\n（不動産登記規則第120条第4項）',
                 '書く（目的とする権利\n「大面太郎持分」。\n承諾証明情報を付ける）', RED),
                ('3番　賃借権設定\n永野達也', '存続登記に当たらない（同欄ハは\n所有権の登記以外の所有権に関する登記\n又は先取特権・質権・抵当権に関する登記）',
                 '書かない', GRAY)]
        for i, (a, b, c, col) in enumerate(rows):
            y = 64 - i * 28
            box(ax, 1, y, 30, 22, a, col=BLUE, fs=14)
            box(ax, 36, y, 38, 22, b, col=col, fs=12.5)
            box(ax, 79, y, 20, 22, c, col=col, fs=13, tc=RED if col == RED else BLACK, weight='bold' if col == RED else 'normal')
            arrow(ax, (31, y + 11), (35.5, y + 11))
            arrow(ax, (74, y + 11), (78.5, y + 11))
    box_fig('存続登記の表：乙区は3件、答案用紙の表も3行。でも書くのは1行', 'H22_dai22mon_zu13_otsuku_furiwake', draw,
            '表の行数と乙区の件数が同じでも、全部は埋めない。A銀行は消滅の承諾、賃借権は存続登記の範囲の外。\n'
            '書くのは「21番　乙区2番　抵当権設定　昭和51年2月17日第1113号　B信用金庫　大面太郎持分」の1行だけ')


def zu14():
    """添付情報9つと根拠（第5章、藍子が9つを挙げた直後）。"""
    rows = [('建物図面', '合体後の建物', '不動産登記令別表13の項添付情報欄イ'),
            ('各階平面図', '合体後の建物', '同欄ロ'),
            ('所有権証明情報', '増築部分を健一郎さんが出資したこと・持分の合意', '（合体後の建物の所有を示す）'),
            ('住所証明情報', '健一郎さん（所有権の登記名義人になる）', '同欄リ'),
            ('登記済証', '太郎さん（21番の所有権の登記名義人）', '令第8条第1項第2号、不動産登記法附則第7条'),
            ('印鑑証明書', '太郎さんだけ（健一郎さんは登記識別情報の\n通知を受ける人〈規則第47条第3号ホ〉なので不要\n〈規則第48条第1項第4号・第49条第2項第4号〉）',
             '令第16条第2項・第18条第2項、\n不動産登記規則第47条第3号イ（6）'),
            ('承諾証明情報', 'B信用金庫（太郎さんの持分の上に存続）', '令別表13の項添付情報欄ト'),
            ('抵当権消滅承諾証明情報', 'A銀行', '不動産登記法第50条、規則第120条第5項第1号'),
            ('代理権限証明情報', '波臼さんへの委任状', '令第7条第1項第2号')]

    def draw(ax):
        cols = [(1, 22, '添付情報'), (23, 42, '誰の・何のため'), (65, 34, '根拠')]
        y = 96
        for x, w, t in cols:
            box(ax, x, y - 6, w, 6, t, col=GRAY, fs=14, weight='bold', alpha=0.25)
        y -= 6
        for name, who, law in rows:
            h = 13 if '\n' in who else 9.2
            box(ax, cols[0][0], y - h, cols[0][1], h, name, col=BLUE, fs=13.5, weight='bold', alpha=0.10, lw=1.2)
            box(ax, cols[1][0], y - h, cols[1][1], h, who, col=GRAY, fs=12.5, alpha=0.04, lw=1.2, ha='left')
            box(ax, cols[2][0], y - h, cols[2][1], h, law, col=GRAY, fs=12, alpha=0.04, lw=1.2, ha='left')
            y -= h
        assert y > -2, y
    box_fig('添付情報9つと根拠（答案用紙の欄の名前どおり「〜情報」で書く）', 'H22_dai22mon_zu14_tenpu_jouhou', draw,
            '印鑑証明書は、合体による登記等を申請する所有権の登記名義人（太郎さん）の分。表題部所有者で、所有権の保存の登記で\n'
            '登記識別情報の通知を受ける健一郎さんの分は要らない。登記済証は、登記識別情報の代わりに出す')


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
    zu11()
    zu12()
    zu13()
    zu14()
    zu15()
    zu16()
    print('重なり合計:', len(PROBLEMS))
