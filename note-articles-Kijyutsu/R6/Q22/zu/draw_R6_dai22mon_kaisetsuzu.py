"""令和6年度 第22問（建物）の解説図8枚を、座標値・頂点座標から作図してPNGに書き出す。

`../prompt_R6_dai22mon_kaisetsuzu.md` の図1〜図8どおり（番号は記事の挿入順）。図3（建物図面）と図7（各階平面図）の完成形は、
答案用紙の第3欄の欄（家屋番号・建物の所在・申請人・作成者・縮尺。`public/kijutsu/R06-tatemono/a2.png` の形）の枠の中に描く。作図の共通部品は `tools/zu_helpers.py`。
建物の座標は (東, 南) で持ち（原点は1階のウォークインクローゼットの西の壁と和室の北の壁の延長線の交点）、
zu_helpers の (北, 東) には B() で変換する（北 ＝ −南）。敷地は〔座標値一覧表〕の (X, Y) をそのまま使う。
実行: python3 note-articles-Kijyutsu/R6/Q22/zu/draw_R6_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Circle, Rectangle  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN,  # noqa: E402
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


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.01
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


INK = '#1a3a8f'   # 記入（濃い青）


def zu03():
    """建物図面の完成形（答案用紙の第3欄の右側〈建物図面〉の枠の中。塗り分けはしない）。"""
    setup_font()
    fig = plt.figure(figsize=(16, 13), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面の完成形（答案用紙の第3欄・縮尺1/500で描く内容）', fontsize=22, weight='bold', y=0.985)
    # 答案用紙の欄（家屋番号は空欄〈登記所が付ける〉・建物の所在・申請人（略）・縮尺）
    cell(fig, 0.06, 0.880, 0.20, 0.932, '家屋番号', fs=15)
    cell(fig, 0.20, 0.880, 0.46, 0.932)
    fig.text(0.70, 0.906, '建　物　図　面', ha='center', va='center', fontsize=20)
    cell(fig, 0.06, 0.828, 0.20, 0.880, '建物の所在', fs=15)
    cell(fig, 0.20, 0.828, 0.94, 0.880, 'A市B町三丁目16番地13', fs=16, ha='left', color=INK)
    cell(fig, 0.06, 0.090, 0.94, 0.828, lw=1.8)
    cell(fig, 0.06, 0.036, 0.20, 0.090, '申　請　人', fs=15)
    cell(fig, 0.20, 0.036, 0.74, 0.090, '（略）', fs=15)
    cell(fig, 0.74, 0.036, 0.83, 0.090, '縮尺', fs=15)
    cell(fig, 0.83, 0.036, 0.94, 0.090, '1/500', fs=15)
    ax = fig.add_axes([0.08, 0.11, 0.84, 0.70])
    z = Zu(ax, fontsize=14)
    fit(ax, SITE, margin=0.08, extra=[(25, 53.6), (25, 33.6)], pad_aspect=True)
    z.north_arrow()
    z.poly(SITE, color=BLACK, lw=2.2)
    z.line(PB, complex(52.2, 25), color=BLACK, lw=1.6)     # B点から北へ：16-11と道100-9の境目
    bldg = [to_site(p) for p in F1]
    z.poly(bldg, color=BLACK, lw=2.4)
    assert round(area(bldg), 2) == 68.85
    dim_line(z, complex(50, 16.9), complex(48.5, 16.9), '1.5', side_off=(-14, 0))
    dim_line(z, complex(50, 20.5), complex(48.5, 20.5), '1.5', side_off=(14, 0))
    dim_line(z, complex(44.9, 15), complex(44.9, 16.0), '1.0', dirs=(135, 120, 150, 110))
    z.free_text(complex(43.0, 30.5), '16－13', fs=16)
    z.free_text(complex(52.8, 20), '16－11', fs=15)
    z.free_text(complex(52.8, 30), '道（100－9）', fs=15)
    z.free_text(complex(43.5, 36.0), '16－14', fs=15, ha='left')
    z.free_text(complex(35.3, 25), '道（100－3）', fs=15)
    z.free_text(complex(43.5, 14.0), '16－12', fs=15, ha='right')
    z.free_text(complex(34.6, 35.5), '（単位：m）', fs=13, offsets=((0, 0), (0, 14), (-20, 0)))
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


# ---- 図7：各階平面図の完成形（答案用紙の第3欄の左側〈各階平面図〉の枠の中） ----
# 2階の図に重ねる1階の位置（点線）：2階の外形と重ならない1階の外形の部分
F1_DOT = [[B(0.9, 3.6), B(0, 3.6), B(0, 6.3), B(0.9, 6.3)],
          [B(7.65, 0.9), B(11.25, 0.9), B(11.25, 2.7), B(10.8, 2.7)],
          [B(4.5, 6.3), B(4.5, 6.75), B(6.3, 6.75), B(6.3, 8.1), B(7.2, 8.1)]]
F1_LAB = ['3.60', '0.90', '6.75', '1.80', '0.45', '5.40', '4.50', '1.35', '1.80', '0.45', '4.50', '2.70', '0.90', '3.60']
F2_LAB = ['3.60', '0.90', '3.15', '1.80', '3.15', '5.40', '3.60', '1.80', '6.30', '6.30']
A_LAB = ['3.15', '4.50', '3.15', '4.50']


def edge_len(p, q):
    return round(abs(q - p), 2)


assert [f'{edge_len(F1[i], F1[(i + 1) % len(F1)]):.2f}' for i in range(len(F1))] == F1_LAB
assert [f'{edge_len(F2[i], F2[(i + 1) % len(F2)]):.2f}' for i in range(len(F2))] == F2_LAB
assert [f'{edge_len(A_ROOM[i], A_ROOM[(i + 1) % 4]):.2f}' for i in range(4)] == A_LAB


def zu07():
    """各階平面図の完成形。求積図（図5・図6）とちがい塗り分けはせず、辺長・1階の位置の点線・求積表だけ。"""
    setup_font()
    fig = plt.figure(figsize=(18, 13), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図の完成形（答案用紙の第3欄・縮尺1/250で描く内容）', fontsize=22, weight='bold', y=0.98)
    fig.text(0.5, 0.918, '各　階　平　面　図', ha='center', va='center', fontsize=20)
    cell(fig, 0.04, 0.12, 0.96, 0.895, lw=1.8)
    cell(fig, 0.04, 0.06, 0.14, 0.12, '作　成　者', fs=15)
    cell(fig, 0.14, 0.06, 0.78, 0.12, '（略）　　　　　　　　　　　　（令和6年○月○日作成）', fs=15)
    cell(fig, 0.78, 0.06, 0.86, 0.12, '縮尺', fs=15)
    cell(fig, 0.86, 0.06, 0.96, 0.12, '1/250', fs=15)
    fig.text(0.5, 0.025, '柱の中心線の寸法（小数第2位まで。問題文の注4）。2階には1階の位置を点線で重ね、（あ）部分の洋室は屋外廊下の分をあけて描く。'
             '車庫・屋外廊下・バルコニー・出窓は描かない', ha='center', va='center', fontsize=14)
    ax1 = fig.add_axes([0.06, 0.40, 0.36, 0.45])
    ax2 = fig.add_axes([0.47, 0.40, 0.48, 0.45])
    z1 = Zu(ax1, fontsize=12)
    ax1.set_title('1階', fontsize=17, weight='bold', loc='left')
    fit(ax1, F1, margin=0.08, extra=[xy(B(-1.6, -1.4)), xy(B(12.9, 9.4))], pad_aspect=True)
    z1.poly(F1, color=BLACK, lw=2.2)
    lab1 = list(F1_LAB)
    lab1[4] = lab1[9] = None          # 0.45の短い辺は、辺に平行に置くと隣の寸法と重なるので横に水平に書く
    dims(z1, F1, lab1, fs=12)
    z1.free_text(B(11.025, 2.7), '0.45', fs=12, offsets=((22, -14), (28, -18), (30, -10), (0, -16)))
    z1.free_text(B(4.5, 6.525), '0.45', fs=12, offsets=((-22, -12), (-26, -16), (-30, -8), (-24, 0)))
    z2 = Zu(ax2, fontsize=12)
    ax2.set_title('2階', fontsize=17, weight='bold', loc='left')
    fit(ax2, F2 + A_ROOM, margin=0.06, extra=[xy(B(-1.6, -1.6)), xy(B(17.4, 9.4))], pad_aspect=True)
    z2.north_arrow()
    for seg in F1_DOT:
        z2.poly(seg, color=BLACK, lw=1.3, ls=':', closed=False)
    z2.poly(F2, color=BLACK, lw=2.2)
    z2.poly(A_ROOM, color=BLACK, lw=2.2)
    dims(z2, F2, F2_LAB, fs=12)
    dims(z2, A_ROOM, A_LAB, fs=12)
    fig.text(0.13, 0.26, '1階 求積表\n0.90×2.70＝2.4300\n3.60×6.30＝22.6800\n1.80×5.85＝10.5300\n4.50×7.20＝32.4000\n'
             '0.45×1.80＝0.8100\n計　68.8500\n床面積　68.85㎡', ha='left', va='center', fontsize=14, linespacing=1.45)
    fig.text(0.58, 0.26, '2階 求積表\n3.60×6.30＝22.6800\n2.70×5.40＝14.5800\n0.45×7.20＝3.2400\n3.15×5.40＝17.0100\n'
             '3.15×4.50＝14.1750\n計　71.6850\n床面積　71.68㎡', ha='left', va='center', fontsize=14, linespacing=1.45)
    fig.text(0.80, 0.26, '点線＝1階の位置\n（2階の外形と重ならない部分）', ha='left', va='center', fontsize=13, color=GRAY)
    assert round(area(F1), 4) == 68.85 and round(area(F2) + area(A_ROOM), 4) == 71.685
    save(fig, [z1, z2], 'R6_dai22mon_zu07_kakukai_heimenzu')


# ---- 図8：本番で解く順番（固定配置の図なので重なり検査の対象外） ----
def zu08():
    setup_font()
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　計算のいらない問と欄を先に、寸法線と作図に時間を残す', fontsize=23, weight='bold', y=0.965)
    ax = fig.add_axes([0.02, 0.22, 0.96, 0.68])
    ax.set_xlim(0, 100)
    ax.set_ylim(14, 92)
    ax.axis('off')
    steps = [
        ('①', '問1\n（第1欄）', '準則第87条第1項\nアとイは順不同', BLUE),
        ('②', '前文・事実関係・\n問題文の注', '共有・持分・\n申請人は桜子', BLUE),
        ('③', '問4と\n（あ）部分の判断', '構造上はあり\n利用上はなし', BLUE),
        ('④', '申請書の\n床面積のいらない欄', '目的・添付書類・\n構造・原因・共有者', GREEN),
        ('⑤', '寸法線の累計と\n床面積', '0.45の幅・\n71.68は切り捨て', ORANGE),
        ('⑥', '第3欄の作図', '各階平面図と\n建物図面', RED),
        ('⑦', '見直し', '共有者の持分・\n出窓・車庫', GRAY),
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
    ax.text(1 + 1.5 * (w + gap) + w / 2, 84, '計算なしで先に書ける（①〜④）', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.text(1 + 4.5 * (w + gap) + w / 2, 84, 'いちばん時間を食う（⑤⑥）', ha='center', fontsize=15, color=RED, weight='bold')
    fig.text(0.5, 0.115, '寸法線のメモ：西の壁・北の壁を0にして上と下の寸法線を足す　上 3.60・5.40・6.75　／　下 2.70・4.50・5.40・6.30　→　6.75−6.30＝0.45',
             ha='center', va='center', fontsize=15, weight='bold',
             bbox=dict(boxstyle='round,pad=0.5', fc='#fff8e6', ec=ORANGE, lw=1.6))
    fig.text(0.5, 0.04, '1階と2階は同じ原点でそろえる。（あ）部分の結論（1個の建物の一部、2階は算入・1階の車庫は不算入）が、'
             '問2の床面積・問3の図面・問4の穴埋めを決める', ha='center', va='center', fontsize=14)
    path = os.path.join(OUT, 'R6_dai22mon_zu08_toku_junban.png')
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
