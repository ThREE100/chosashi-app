"""令和6年度 第22問（建物）の解説図6枚を、座標値・頂点座標から作図してPNGに書き出す。

`../prompt_R6_dai22mon_kaisetsuzu.md` の図1〜図6どおり。作図の共通部品は `tools/zu_helpers.py`。
建物の座標は (東, 南) で持ち（原点は1階のウォークインクローゼットの西の壁と和室の北の壁の延長線の交点）、
zu_helpers の (北, 東) には B() で変換する（北 ＝ −南）。敷地は〔座標値一覧表〕の (X, Y) をそのまま使う。
実行: python3 note-articles-Kijyutsu/R6/Q22/zu/draw_R6_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Circle  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, BLACK, GRAY, RED, BLUE, ORANGE, GREEN,  # noqa: E402
                        PURPLE)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []


def B(e, s):
    """建物の (東, 南) を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(-s, e)


def rect(e0, s0, e1, s1):
    return [B(e0, s0), B(e1, s0), B(e1, s1), B(e0, s1)]


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


# ---- 建物（図2〔各階平面図〕の寸法線から。単位メートル、柱の中心線） ----
F1 = [B(0.9, 0), B(4.5, 0), B(4.5, 0.9), B(11.25, 0.9), B(11.25, 2.7), B(10.8, 2.7), B(10.8, 8.1),
      B(6.3, 8.1), B(6.3, 6.75), B(4.5, 6.75), B(4.5, 6.3), B(0, 6.3), B(0, 3.6), B(0.9, 3.6)]
F1_STRIPS = [rect(0, 3.6, 0.9, 6.3), rect(0.9, 0, 4.5, 6.3), rect(4.5, 0.9, 6.3, 6.75), rect(6.3, 0.9, 10.8, 8.1),
             rect(10.8, 0.9, 11.25, 2.7)]
F2 = [B(0.9, 0), B(4.5, 0), B(4.5, 0.9), B(7.65, 0.9), B(7.65, 2.7), B(10.8, 2.7), B(10.8, 8.1),
      B(7.2, 8.1), B(7.2, 6.3), B(0.9, 6.3)]
F2_STRIPS = [rect(0.9, 0, 4.5, 6.3), rect(4.5, 0.9, 7.2, 6.3), rect(7.2, 0.9, 7.65, 8.1), rect(7.65, 2.7, 10.8, 8.1)]
OTOSHI = rect(7.2, 0.9, 7.65, 2.7)             # 藍子が落とした部分 0.45×1.80
A_ROOM = rect(12.6, -0.9, 15.75, 3.6)          # （あ）部分の2階の洋室（1階は車庫） 3.15×4.50
OKUGAI = rect(10.8, 2.7, 12.6, 3.6)            # 屋外廊下
ROUKA2 = rect(4.5, 2.7, 10.8, 3.6)             # 母屋の2階の廊下
BALCONY = [B(0.9, 6.3), B(7.2, 6.3), B(7.2, 8.1), B(10.8, 8.1), B(10.8, 9), B(6.3, 9), B(6.3, 7.2), B(0.9, 7.2)]
DEMADO = rect(10.8, 5.4, 11.1, 7.2)            # 1階リビングダイニングの東の出窓（位置は模式）

assert round(area(F1), 2) == 68.85 == round(sum(area(r) for r in F1_STRIPS), 2)
assert round(area(F2), 2) == 57.51 == round(sum(area(r) for r in F2_STRIPS), 2)
assert round(area(A_ROOM), 3) == 14.175 and round(area(F2) + area(A_ROOM), 3) == 71.685
assert round(area(OTOSHI), 2) == 0.81

# ---- 敷地（〔座標値一覧表〕。X＝北、Y＝東） ----
PA, PB, PC, PD, PE = complex(50, 15), complex(50, 25), complex(50, 35), complex(37, 35), complex(37, 15)
SITE = [PA, PB, PC, PD, PE]
assert area(SITE) == 260.0


def to_site(p):
    """建物の点を敷地の座標へ（西の壁が辺EAから1.0、和室の北の壁が辺ABから1.5）。"""
    return complex(48.5 + p.real, 16.0 + p.imag)


def dims(z, pts, labels, fs=13, ref=None):
    c = ref or centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs)


# ---- 図1：（あ）部分への出入り経路 ----
def zu01():
    fig, axes = new_figure('（あ）部分への出入り経路（2階）',
                           '（あ）部分の2階に入るには、母屋の2階の廊下から屋外廊下を渡るしかない。1階の車庫には階段も周壁もない',
                           w=16, h=10)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(F2, color=BLACK, lw=2.2, fill=GRAY, alpha=0.18)
    z.poly(ROUKA2, color=BLACK, lw=0, fill='#f2c200', alpha=0.35, check=False)
    hatch(ax, OKUGAI)
    z.poly(OKUGAI, color=GRAY, lw=1.4, ls='--')
    z.poly(A_ROOM, color=BLACK, lw=2.2, fill=BLUE, alpha=0.25)
    route = [B(7.0, 4.0), B(7.0, 3.15), B(12.9, 3.15), B(13.6, 2.0)]
    for p, q in zip(route[:-1], route[1:]):
        ax.annotate('', xy=xy(q), xytext=xy(p),
                    arrowprops=dict(arrowstyle='-|>', lw=3.2, color=RED, mutation_scale=22, shrinkA=0, shrinkB=0),
                    zorder=6)
        z.segments.append((xy(p), xy(q)))
    fit(ax, F2 + A_ROOM, margin=0.06, extra=[xy(B(-1, 9.5)), xy(B(24.5, -2.5))], pad_aspect=True)
    z.north_arrow()
    z.free_text(B(2.7, 3.2), '母屋の2階', fs=15)
    z.callout(B(7.0, 4.0), '階段（1階から上がる）', dirs=(-100, -120, -80), fs=13)
    z.callout(B(6.0, 3.15), '母屋の2階の廊下', dirs=(110, 90, 130), fs=13)
    z.callout(B(11.7, 3.15), '屋外廊下（外気と分断されていない）', dirs=(-70, -90, -50), dists=(75, 100, 125), fs=13)
    z.callout(B(14.2, 0.2), '（あ）部分の2階の洋室\n1階は車庫（周壁なし・階段なし）', dirs=(90, 70, 110), fs=13, color=BLUE)
    z.free_text(B(20.3, 0.4), '構造上の独立性：あり\n（壁・屋根・床で外気と分断）', fs=15, color=GREEN, weight='bold')
    z.free_text(B(20.3, 2.9), '利用上の独立性：なし\n（母屋を通らないと入れない）', fs=15, color=RED, weight='bold')
    save(fig, [z], 'R6_dai22mon_zu01_a_bubun_keiro')


# ---- 図2：敷地の辺長確認図 ----
def zu02():
    fig, axes = new_figure('本件土地（16番13）の辺長確認図（作図チェック用）',
                           '座標値一覧表どおりに結ぶと東西20.0m・南北13.0mの長方形（A・B・Cは北側の一直線上）。辺長は建物図面には書かない',
                           w=16, h=10.5)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(SITE, color=BLACK, lw=2.4, fill=BLUE, alpha=0.08)
    fit(ax, SITE, margin=0.08, extra=[(25, 53.2), (25, 33.6)], pad_aspect=True)
    z.north_arrow()
    c = centroid(SITE)
    for p, n in zip(SITE, 'ABCDE'):
        z.point(p)
    for p, n in zip(SITE, 'ABCDE'):
        z.point_label(p, n, away=c if n != 'B' else complex(40, 25))
    dims(z, SITE, ['10.0m', '10.0m', '13.0m', '20.0m', '13.0m'], fs=15, ref=c)
    z.free_text(complex(43.5, 25), '本件土地（16番13）\n260.00㎡（登記記録の地積と一致）', fs=15)
    z.free_text(complex(51.8, 20), '16番11', fs=14, color=GRAY)
    z.free_text(complex(51.8, 30), '道（100番9）', fs=14, color=GRAY)
    z.free_text(complex(43.5, 36.2), '16番14', fs=14, color=GRAY, ha='left')
    z.free_text(complex(35.2, 25), '道（100番3）', fs=14, color=GRAY)
    z.free_text(complex(43.5, 13.8), '16番12', fs=14, color=GRAY, ha='right')
    save(fig, [z], 'R6_dai22mon_zu02_shikichi_henchou')


# ---- 図3：建物図面の完成形 ----
def dim_line(z, p, q, text, side_off=(12, 0), dirs=None):
    """筆界から外壁までの距離の寸法線。短くて文字が入らない寸法は dirs を指定して引き出し線で外に書く。"""
    ax = z.ax
    ax.annotate('', xy=xy(q), xytext=xy(p),
                arrowprops=dict(arrowstyle='<->', lw=1.4, color=BLACK, shrinkA=0, shrinkB=0), zorder=4)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    if dirs:
        return z.callout(m, text, dirs=dirs, fs=15, dists=(40, 55, 70))
    return z.free_text(m, text, fs=15, offsets=(side_off, (-side_off[0], -side_off[1]), (0, 14), (0, -14)))


def zu03():
    fig, axes = new_figure('建物図面の完成形（縮尺1/500で描く内容）',
                           '筆界から外壁までの距離は小数第1位（問題文の注4）。1階の外形として描くのは周壁のある母屋。敷地の辺長は書かない',
                           w=16, h=10.5)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(SITE, color=BLACK, lw=2.2)
    z.line(PB, complex(52.2, 25), color=BLACK, lw=1.6)     # B点から北へ：16-11と道100-9の境目
    bldg = [to_site(p) for p in F1]
    z.poly(bldg, color=BLACK, lw=2.4)
    assert round(area(bldg), 2) == 68.85
    fit(ax, SITE, margin=0.08, extra=[(25, 53.6), (25, 33.6)], pad_aspect=True)
    z.north_arrow()
    dim_line(z, complex(50, 16.9), complex(48.5, 16.9), '1.5', side_off=(-14, 0))
    dim_line(z, complex(50, 20.5), complex(48.5, 20.5), '1.5', side_off=(14, 0))
    dim_line(z, complex(44.9, 15), complex(44.9, 16.0), '1.0', dirs=(135, 120, 150, 110))
    z.free_text(complex(43.0, 30.5), '16－13', fs=16)
    z.free_text(complex(52.8, 20), '16－11', fs=15)
    z.free_text(complex(52.8, 30), '道（100－9）', fs=15)
    z.free_text(complex(43.5, 36.0), '16－14', fs=15, ha='left')
    z.free_text(complex(35.3, 25), '道（100－3）', fs=15)
    z.free_text(complex(43.5, 14.0), '16－12', fs=15, ha='right')
    save(fig, [z], 'R6_dai22mon_zu03_tatemono_zumen')


# ---- 図4：1階の誤り比較図 ----
def pillars(z, pts, color):
    """車庫の柱（丸印）。重なり検査の対象の点として登録する。"""
    for p in pts:
        z.ax.add_patch(Circle(xy(p), 0.22, fc='white', ec=color, lw=1.6, zorder=4))
        z.markers.append(xy(p))


def zu04():
    fig, axes = new_figure('1階の床面積：車庫と出窓は入るか',
                           '車庫は周壁がなく外気と分断されていない。出窓は下端が床から0.90m・高さ1.10mで、高さ1.5m以上かつ下端が床面と同じ高さ、を満たさない（出窓の位置は模式）',
                           w=18, h=8.5, ncols=2)
    fig.subplots_adjust(top=0.84)
    garage_cols = A_ROOM
    # 誤り
    z = Zu(axes[0], fontsize=13)
    z.poly(F1, color=BLACK, lw=2.2, fill=BLUE)
    z.poly(A_ROOM, color=RED, lw=0, fill=RED, alpha=0.30, check=False)
    pillars(z, garage_cols, RED)
    z.poly(DEMADO, color=RED, lw=1.6, fill=RED, alpha=0.45)
    axes[0].set_title('誤り：車庫と出窓まで入れる（藍子）', fontsize=17, weight='bold', color=RED)
    fit(axes[0], F1 + A_ROOM, margin=0.14, extra=[xy(B(8, 12))], pad_aspect=True)
    z.free_text(centroid(F1), '母屋', fs=14)
    z.callout(B(14.2, 1.35), '車庫（周壁なし）\n3.15×4.50', dirs=(-70, -90, -50), fs=13, color=RED)
    z.callout(B(11.1, 6.3), '出窓\n（下端0.90m・高さ1.10m）', dirs=(-40, -20, -60, 0), fs=13, color=RED)
    # 正解
    z2 = Zu(axes[1], fontsize=13)
    z2.poly(F1, color=BLACK, lw=2.2, fill=BLUE)
    pillars(z2, garage_cols, GRAY)
    z2.poly(DEMADO, color=GRAY, lw=1.2, ls='--')
    axes[1].set_title('正解：壁の中心線で囲まれた母屋だけ 68.85㎡', fontsize=17, weight='bold', color=GREEN)
    fit(axes[1], F1 + A_ROOM, margin=0.14, extra=[xy(B(8, 12))], pad_aspect=True)
    z2.free_text(centroid(F1), '母屋 68.85㎡', fs=14)
    z2.callout(B(14.2, 1.35), '車庫は床面積に入らない\n（外気と分断されていない）', dirs=(-70, -90, -50), fs=13, color=GRAY)
    z2.callout(B(11.1, 6.3), '出窓は床面積に入らない', dirs=(-40, -20, -60, 0), fs=13, color=GRAY)
    save(fig, [z, z2], 'R6_dai22mon_zu04_1kai_ayamari_hikaku')


# ---- 図5・図6：求積図 ----
COLORS = [ORANGE, BLUE, GREEN, PURPLE, RED]


def zu05():
    fig, axes = new_figure('1階の床面積求積図（西から東へ5つの列）',
                           '0.90×2.70＋3.60×6.30＋1.80×5.85＋4.50×7.20＋0.45×1.80＝68.85㎡',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    for r, c in zip(F1_STRIPS, COLORS):
        z.poly(r, color=c, lw=0, fill=c, alpha=0.25, check=False)
    for e, s0, s1 in [(0.9, 3.6, 6.3), (4.5, 0.9, 6.3), (6.3, 0.9, 6.75), (10.8, 0.9, 2.7)]:
        z.line(B(e, s0), B(e, s1), color=GRAY, lw=1.0, ls='--')
    z.poly(F1, color=BLACK, lw=2.4)
    fit(ax, F1, margin=0.16, extra=[xy(B(-3, -1)), xy(B(15, 9.5))], pad_aspect=True)
    z.north_arrow()
    z.callout(B(0.45, 4.95), '0.90m×2.70m\n（ウォークインクローゼット）', dirs=(-120, -100, -140), fs=13)
    z.free_text(B(2.7, 3.15), '3.60m\n×\n6.30m', fs=14)
    z.free_text(B(5.4, 4.2), '1.80m\n×\n5.85m', fs=14)
    z.free_text(B(8.55, 4.8), '4.50m × 7.20m', fs=14)
    z.callout(B(11.02, 1.8), '0.45m×1.80m\n（浴室の東の出っ張り）', dirs=(-30, -10, -50), fs=13)
    z.free_text(B(5.6, -1.2), '1階 床面積：68.85㎡', fs=16, weight='bold')
    save(fig, [z], 'R6_dai22mon_zu05_1kai_kyuuseki')


def zu06():
    fig, axes = new_figure('2階の床面積求積図（母屋4列＋（あ）部分の洋室）',
                           '3.60×6.30＋2.70×5.40＋0.45×7.20＋3.15×5.40＋3.15×4.50＝71.685 → 切り捨てて71.68㎡。0.45は上下の寸法線の差（6.75−6.30）',
                           w=17, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    for r, c in zip(F2_STRIPS, COLORS):
        z.poly(r, color=c, lw=0, fill=c, alpha=0.25, check=False)
    z.poly(A_ROOM, color=BLUE, lw=0, fill=BLUE, alpha=0.25, check=False)
    z.poly(OTOSHI, color=RED, lw=0, fill=RED, alpha=0.55, check=False)
    hatch(ax, OKUGAI)
    hatch(ax, BALCONY)
    z.poly(OKUGAI, color=GRAY, lw=1.2, ls='--')
    z.poly(BALCONY, color=GRAY, lw=1.2, ls='--')
    for e, s0, s1 in [(4.5, 0.9, 6.3), (7.2, 0.9, 6.3), (7.65, 2.7, 8.1)]:
        z.line(B(e, s0), B(e, s1), color=GRAY, lw=1.0, ls='--')
    z.poly(F2, color=BLACK, lw=2.4)
    z.poly(A_ROOM, color=BLACK, lw=2.4)
    fit(ax, F2 + A_ROOM, margin=0.12, extra=[xy(B(-2, 11.5)), xy(B(20, -3.5))], pad_aspect=True)
    z.north_arrow()
    z.free_text(B(2.7, 3.15), '3.60m\n×\n6.30m', fs=14)
    z.free_text(B(5.85, 4.2), '2.70m\n×\n5.40m', fs=14)
    z.callout(B(7.425, 5.5), '0.45m×7.20m', dirs=(-100, -120, -80), fs=13)
    z.callout(B(7.425, 1.8), '赤＝藍子が落とした部分\n0.45m×1.80m（上下の寸法線の差）', dirs=(100, 120, 80), dists=(70, 95, 120), fs=13,
              color=RED)
    z.free_text(B(9.225, 5.4), '3.15m\n×\n5.40m', fs=14)
    z.free_text(B(14.175, 1.35), '（あ）部分\n3.15m×4.50m', fs=14)
    z.callout(B(11.7, 3.15), '屋外廊下（入らない）', dirs=(-70, -50, -90), fs=12, color=GRAY)
    z.callout(B(3.6, 6.75), 'バルコニー（入らない）', dirs=(-110, -130, -90), fs=12, color=GRAY)
    z.free_text(B(15.5, 8.0), '2階 床面積：71.68㎡\n（合計71.685を切り捨て）', fs=16, weight='bold')
    save(fig, [z], 'R6_dai22mon_zu06_2kai_kyuuseki')


if __name__ == '__main__':
    zu01()
    zu02()
    zu03()
    zu04()
    zu05()
    zu06()
    print('重なり合計:', len(PROBLEMS))
