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


def zu04():
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
    save(fig, [z], 'H22_dai22mon_zu04_shikichi_henchou')


INK = '#1a3a8f'   # 記入（濃い青）


SHOZAI = 'A市D町一丁目21番地、22番地'
SHINSEININ = '大面太郎　大面健一郎'
SAKUSEISHA = 'A市F町二丁目6番8号　土地家屋調査士　波臼良子'   # 答案用紙（その3）に印刷済み（職印・作成日つき）


# ---- 答案用紙（その3）（各階平面図・建物図面）。2026-10-26、試験の答案用紙の寸法どおりの1枚の枠に描き直した ----
# 寸法は試験の答案用紙（その3）の画像（public/kijutsu/H22-tatemono/a3.webp。A3横 420mm × 297mm を 1400px × 989px。
# 1mm ＝ 3.333px）の罫線の位置から mm に直した値。作図は用紙の左下を原点とする mm の座標で行い、図面の中身は
# 建物図面が縮尺1/500（1m ＝ 2mm）、各階平面図が縮尺1/250（1m ＝ 4mm）の実際の大きさで描く。
# （その3）は1枚の枠の左半分が各階平面図、右半分が建物図面（中央の上下に短い仕切りの線だけが印刷）。枠の上の「家屋番号」の箱と、
# 枠の中の上端の「建物の所在」の欄は、建物図面の側に1組だけ。下に「作成者（A市F町二丁目6番8号 土地家屋調査士 波臼良子 職印
# （平成22年8月10日作成））」「縮尺 1/250」と、「申請人」（（略）の印刷なし）「縮尺 1/500」。方位記号は建物図面の側に印刷済み。
FR_L, FR_R, FR_B, FR_T = 20.3, 342.3, 61.4, 253.9      # 図を描く枠
MID = 181.5                                           # 中央の仕切り
SH_X0, SH_X1, SH_Y0, SH_Y1 = 14.0, 348.0, 24.0, 276.0   # 画像に入れる範囲（mm）
SHEET_MM = dict(frame=(FR_L, FR_R, FR_B, FR_T), mid=MID, kaoku=(190.1, 254.9, FR_T, 266.7), kaoku_div=217.8,
                shozai=(190.1, FR_R, 241.6, FR_T), sakusei=(FR_L, 170.9, 45.1, FR_B), sakusei_div=(45.6, 134.7, 146.4),
                shinsei=(191.7, FR_R, 45.1, FR_B), shinsei_div=(217.1, 306.3, 317.7),
                north=((194.4, 198.0), (213.9, 233.1)))
SHEET_PX = 1400 / 420                                 # 答案用紙の画像の 1mm あたりの画素数（照合スクリプトで測り直す）


def M(x, y):
    """用紙の mm の位置（x：右向き、y：上向き）を zu_helpers の複素数（縦, 横）にする。"""
    return complex(y, x)


ZX0, ZY0 = 232.0, 134.0                               # 建物図面：敷地の図面の座標の原点（E点）を置く用紙の位置（mm）


def Z500(p):
    """建物図面（縮尺1/500）：図面の座標 complex(v, u) [m] を用紙の mm に置く。1m ＝ 2mm。"""
    return M(ZX0 + 2 * p.imag, ZY0 + 2 * p.real)


def H250(x, s, x0, y0):
    """各階平面図（縮尺1/250）：建物の (x, s) [m] を用紙の mm に置く。原点（1階の北北西の辺と西南西の辺の線の交点）を (x0, y0) mm に。"""
    return M(x0 + 4 * x, y0 - 4 * s)


def sheet_figure(title):
    setup_font()
    w_mm, h_mm = SH_X1 - SH_X0, SH_Y1 - SH_Y0
    fig = plt.figure(figsize=(22, 22 * h_mm / w_mm), dpi=100)
    fig.patch.set_facecolor('white')
    ax = fig.add_axes([0, 0, 1, 1])
    z = Zu(ax, fontsize=10)
    ax.set_xlim(SH_X0, SH_X1)
    ax.set_ylim(SH_Y0, SH_Y1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.text((SH_X0 + SH_X1) / 2, 272.0, title, ha='center', va='center', fontsize=21, weight='bold')
    return fig, ax, z


def sheet3(ax, z):
    """答案用紙（その3）の印刷（試験の答案用紙どおり）と、建物の所在・申請人の記入。"""
    def rect(x0, x1, y0, y1, lw=1.3):
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, lw=lw, ec=BLACK, zorder=3))

    def ln(x0, y0, x1, y1, lw=1.0):
        ax.plot([x0, x1], [y0, y1], color=BLACK, lw=lw, zorder=3)

    def txt(x, y, s, fs=12, ha='center', **kw):
        ax.text(x, y, s, ha=ha, va='center', fontsize=fs, zorder=4, family='Noto Serif CJK JP', **kw)

    S = SHEET_MM
    txt(22.0, 264.6, '問２', fs=12, ha='left', weight='bold')
    txt(22.0, 258.4, '(2)', fs=10, ha='left')
    txt(106.5, 260.1, '各　階　平　面　図', fs=15)
    txt(300.0, 260.4, '建　　物　　図　　面', fs=15)
    rect(FR_L, FR_R, FR_B, FR_T, lw=1.6)                         # 図を描く枠
    ln(MID, FR_T, MID, 249.9, lw=1.6)                            # 中央の仕切り（上下の短い線だけが印刷）
    ln(MID, FR_B, MID, 65.8, lw=1.6)
    rect(*S['kaoku'])                                            # 家屋番号の箱（枠の外の上）
    ln(S['kaoku_div'], FR_T, S['kaoku_div'], 266.7)
    txt(203.9, 260.3, '家屋番号', fs=11)                           # 合体後の建物の家屋番号は登記官が付けるので空欄
    rect(*S['shozai'])                                           # 建物の所在の欄（枠の中の上端）
    ln(S['kaoku_div'], 241.6, S['kaoku_div'], FR_T)
    txt(203.9, 247.75, '建物の所在', fs=11)
    ax.text(221.0, 247.75, SHOZAI, ha='left', va='center', fontsize=12, color=INK, zorder=4)
    (tx, ty), (hx, hy) = S['north']                              # 方位記号（印刷）
    ax.annotate('', xy=(hx, hy), xytext=(tx, ty), arrowprops=dict(arrowstyle='-|>', lw=1.8, color=BLACK, mutation_scale=16),
                zorder=4)
    ax.add_patch(plt.Circle((tx + (hx - tx) * 0.2, ty + (hy - ty) * 0.2), 2.6, fill=False, lw=1.0, ec=BLACK, zorder=4))
    z.segments.append(((tx, ty), (hx, hy)))
    x0, x1, y0, y1 = S['sakusei']                                # 作成者・縮尺 1/250（作成者は印刷済み）
    rect(x0, x1, y0, y1)
    for x in S['sakusei_div']:
        ln(x, y0, x, y1)
    txt(32.9, 53.2, '作　成　者', fs=11)
    txt(48.0, 58.3, 'A市F町二丁目6番8号', fs=10, ha='left')
    txt(48.0, 53.3, '土地家屋調査士　波臼良子', fs=10, ha='left')
    txt(112.0, 53.3, '職印', fs=8.5, ha='left', bbox=dict(boxstyle='square,pad=0.15', fc='white', ec=BLACK, lw=0.8))
    txt(132.5, 48.3, '（平成22年8月10日作成）', fs=10, ha='right')
    txt(140.5, 53.2, '縮尺', fs=10)
    ln(148.5, 46.4, 169.5, 59.9, lw=0.9)
    txt(155.4, 57.0, '1', fs=10)
    txt(162.5, 49.3, '250', fs=10)
    x0, x1, y0, y1 = S['shinsei']                                # 申請人・縮尺 1/500
    rect(x0, x1, y0, y1)
    for x in S['shinsei_div']:
        ln(x, y0, x, y1)
    txt(204.4, 53.2, '申　請　人', fs=11)
    ax.text(222.0, 53.2, SHINSEININ, ha='left', va='center', fontsize=12, color=INK, zorder=4)
    txt(312.0, 53.2, '縮尺', fs=10)
    ln(319.5, 47.1, 339.6, 59.9, lw=0.9)
    txt(325.5, 57.0, '1', fs=10)
    txt(333.0, 50.7, '500', fs=10)
    txt(321.0, 65.0, '（単位：m）', fs=10)


def zumen_content(z):
    """右半分：建物図面（縮尺1/500、1m ＝ 2mm）。敷地（21番・22番）と1階の位置・形状、筆界から外壁までの距離、地番・道路。"""
    z.poly([Z500(p) for p in LOT21], lw=1.4)
    z.poly([Z500(p) for p in LOT22], lw=1.4)
    z.line(Z500(D), Z500(complex(D.real, D.imag - 6.0)), lw=1.0)             # 12番と13番の境
    z.line(Z500(complex(0.0, -6.0)), Z500(E), lw=1.0)                       # 道路との境の延長
    z.line(Z500(G), Z500(complex(0.0, 36.0)), lw=1.0)
    z.line(Z500(complex(-8.0, -6.0)), Z500(complex(-8.0, 36.0)), color=GRAY, lw=0.9)   # 道路の向こう側（幅員8m）
    z.poly([Z500(S(*v)) for v in F1], lw=2.0)
    wu = U0 - 0.10                       # 西南西の外壁（境から4.40）
    for p, q, t, dirs in [(complex(V0 - 4.50, wu), complex(V0 - 4.50, 0.0), '4.40', (100, 115, 85)),
                          (complex(12.00, wu), complex(12.00, 0.0), '4.40', (-110, -125, -95)),
                          (complex(12.00, wu), complex(0.0, wu), '12.00', (170, 155, 185))]:
        z.dim_line(Z500(p), Z500(q), lw=1.1)
        z.callout(Z500((p + q) / 2), t, dirs=dirs, fs=10, dists=(26, 36, 48, 60))
    for p, t in [(complex(4.5, 9.0), '21'), (complex(4.5, 24.0), '22')]:
        z.free_text(Z500(p), t, fs=11, offsets=((0, 0), (0, 8), (0, -8)))
    for p, t in NEIGHBORS:
        z.free_text(Z500(p), t, fs=10, offsets=((0, 0), (0, 8), (0, -8), (10, 0), (-10, 0)))


HX0, HY1, HY2 = 55.0, 228.0, 150.0                    # 各階平面図：1階・2階の原点を置く用紙の位置（mm）


def heimen_content(z):
    """左半分：各階平面図（縮尺1/250、1m ＝ 4mm）。柱の中心線の辺長、各階の別、2階には1階の位置を点線で。
    問2(2)のなお書きで求積とその方法・床面積の表示は省略。方位は書かない（不動産登記規則第83条第1項）。"""
    z.free_text(M(30.0, 238.0), '1階', fs=12, ha='left')
    f1 = [H250(x, s, HX0, HY1) for x, s in F1]
    z.poly(f1, lw=1.6)
    c1 = H250(11.5, 4.5, HX0, HY1)
    for i, t in enumerate(['21.20', '5.40', None, '3.60', '21.65', '4.50', '1.80', '4.50']):
        if t:
            z.edge_label(f1[i], f1[(i + 1) % len(f1)], t, c1, fs=10, dists=(7, 11, 15))
    z.callout(H250(22.325, 5.40, HX0, HY1), '1.35', dirs=(-30, -15, -45), fs=10, dists=(24, 32, 42))
    z.free_text(M(30.0, 160.0), '2階', fs=12, ha='left')
    f2 = [H250(x, s, HX0, HY2) for x, s in F2]
    rest = [H250(x, s, HX0, HY2) for x, s in [(9.00, 0), (23.00, 0), (23.00, 5.40), (21.65, 5.40), (21.65, 9.00), (0, 9.00),
                                             (0, 4.50), (1.80, 4.50), (1.80, 7.20)]]
    z.poly(rest, lw=1.0, ls=':', closed=False)
    z.poly(f2, lw=1.6)
    c2 = H250(5.4, 3.6, HX0, HY2)
    for i in range(4):
        z.edge_label(f2[i], f2[(i + 1) % 4], '7.20', c2, fs=10, dists=(7, 11, 15))
    z.free_text(M(120.0, 106.0), '点線は1階の位置', fs=10, ha='left', color=GRAY)


def zu07():
    fig, ax, z = sheet_figure('建物図面の完成形（答案用紙（その3）の建物図面の側・縮尺1/500の実際の大きさ）')
    sheet3(ax, z)
    zumen_content(z)
    assert round(area([S(*v) for v in F1]), 4) == 194.04
    ax.text((SH_X0 + SH_X1) / 2, 38.0, '1階の形を、21番の部分の外壁までの距離（西南西の境から4.40が2か所、道路から12.00）で置く。'
            '1階は21番の上が113.40㎡・22番の上が80.64㎡なので所在は「21番地、22番地」', ha='center', va='center', fontsize=13)
    ax.text((SH_X0 + SH_X1) / 2, 31.5, '家屋番号は登記官が付けるので空欄、申請人の欄は（略）と印刷されていないので2人の氏名を書く。'
            '敷地の辺長と東北東の3.85は書かない。方位記号は印刷済み。各階平面図の側（左半分）は第4章で描く',
            ha='center', va='center', fontsize=12, color=GRAY)
    save(fig, [z], 'H22_dai22mon_zu07_tatemono_zumen')


def zu08():
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
    save(fig, [z, z3], 'H22_dai22mon_zu08_1kai_ayamari_hikaku')


def zu09():
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
    save(fig, [z], 'H22_dai22mon_zu09_1kai_kyuuseki')


def zu11():
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
    save(fig, [z], 'H22_dai22mon_zu11_2kai_kyuuseki')


def zu12():
    fig, ax, z = sheet_figure('各階平面図の完成形（答案用紙（その3）の各階平面図の側・縮尺1/250の実際の大きさ）')
    sheet3(ax, z)
    heimen_content(z)
    zumen_content(z)
    assert round(area([P(*v) for v in F1]), 4) == 194.04 and round(area([P(*v) for v in F2]), 4) == 51.84
    ax.text((SH_X0 + SH_X1) / 2, 38.0, '柱の中心線の寸法で「1階」「2階」を書き分け、2階の図には1階の位置を点線で示す。問2(2)のなお書きどおり、'
            '求積とその方法、床面積の表示は書かない。形が閉じているかの検算：21.20＋1.80＝21.65＋1.35＝23.00、4.50＋4.50＝5.40＋3.60＝9.00',
            ha='center', va='center', fontsize=12.5)
    ax.text((SH_X0 + SH_X1) / 2, 31.5, '方位は建物図面だけに書く（不動産登記規則第82条第2項。各階平面図の第83条第1項には方位がない）。'
            '作成者の欄と縮尺は印刷済み', ha='center', va='center', fontsize=12, color=GRAY)
    save(fig, [z], 'H22_dai22mon_zu12_kakai_heimenzu')


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


def zu19():
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
    box_fig('課税価格と登録免許税の組み立て（所有権の保存の登記）', 'H22_dai22mon_zu19_touroku_menkyozei', draw,
            '工事費の370万円は建物の価額ではない（1,200＋530＋370＝2,100万円で計算しない）。\n'
            '課税価格 2,000万円×10分の6＝1,200万円、登録免許税 1,200万円×1000分の4＝4万8,000円（登録免許税法別表第一の一（一）・第10条）')


def zu20():
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
    box_fig('本番で解く順番　計算のいらない欄を先に', 'H22_dai22mon_zu20_toku_junban', draw,
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


def zu05():
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
    save(fig, [z], 'H22_dai22mon_zu05_touhokutou_kenzan')


def zu06():
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
    save(fig, [z], 'H22_dai22mon_zu06_shozai_kakunin')


def zu10():
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
    save(fig, [z], 'H22_dai22mon_zu10_gattaizen_kenzan')


def zu13():
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
    box_fig('合体後の甲区（所有権の登記）の行き先：表題登記だけの22番がある', 'H22_dai22mon_zu13_kouku_yukisaki', draw,
            '所有権の登記がある21番の分は登記官が合体による所有権の登記として記録し、表題登記だけの22番の分は、\n'
            '健一郎さんを登記名義人とする所有権の保存の登記を併せて申請する（持分は合意どおり10分の4・10分の6）')


def zu16():
    """存続登記に当たるか（第5章、永野さんの賃借権。A銀行は前の図で外した）。"""
    def draw(ax):
        box(ax, 1, 74, 98, 20, '存続登記（不動産登記令別表13の項申請情報欄ハ）＝ 所有権の登記以外の所有権に関する登記、又は\n'
            '先取特権・質権・抵当権に関する登記であって、合体後の建物について存続することとなるもの', col=PURPLE, fs=15)
        rows = [('2番　抵当権設定\nB信用金庫', '抵当権に関する登記で、存続する\n→ 当たる。大面太郎の持分10分の4の上に移される\n（不動産登記規則第120条第4項）',
                 '書く（目的とする権利\n「大面太郎持分」。\n承諾証明情報を付ける）', RED),
                ('3番　賃借権設定\n永野達也', '所有権に関する登記でも、先取特権・質権・\n抵当権に関する登記でもない\n→ 当たらない', '書かない', GRAY)]
        for i, (a_, b_, c_, col) in enumerate(rows):
            y = 40 - i * 32
            box(ax, 1, y, 26, 26, a_, col=BLUE, fs=15)
            box(ax, 31, y, 42, 26, b_, col=col, fs=13.5)
            box(ax, 77, y, 22, 26, c_, col=col, fs=13.5, tc=RED if col == RED else BLACK, weight='bold' if col == RED else 'normal')
            arrow(ax, (27, y + 13), (30.5, y + 13))
            arrow(ax, (73, y + 13), (76.5, y + 13))
    box_fig('存続登記に当たるか：賃借権は条文に入っていない', 'H22_dai22mon_zu16_sonzoku_hani', draw,
            'A銀行の抵当権は消滅の承諾で外れ（前の図）、賃借権は存続登記の範囲の外。3行の表に書くのは\n'
            '「21番　乙区2番　抵当権設定　昭和51年2月17日第1113号　B信用金庫　大面太郎持分」の1行だけ')


def zu18():
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
    box_fig('添付情報9つと根拠（答案用紙の欄の名前どおり「〜情報」で書く）', 'H22_dai22mon_zu18_tenpu_jouhou', draw,
            '印鑑証明書は、合体による登記等を申請する所有権の登記名義人（太郎さん）の分。表題部所有者で、所有権の保存の登記で\n'
            '登記識別情報の通知を受ける健一郎さんの分は要らない。登記済証は、登記識別情報の代わりに出す')


def zu03():
    """問1の添付情報（第2章、藍子が「住所証明情報と登記識別情報も要りますか？」と迷ったところ）。"""
    def draw(ax):
        ax.text(25, 97, '要る（4つ）', ha='center', va='top', fontsize=18, weight='bold', color=BLUE)
        ax.text(76, 97, '要らない（藍子の迷い）', ha='center', va='top', fontsize=18, weight='bold', color=RED)
        for i, t in enumerate(['建物図面・各階平面図\n床面積が変わる（不動産登記令別表14の項添付情報欄ロ（1））',
                               '所有権証明情報\n床面積が増えた部分を健一郎さんが持っている（同欄ロ（2））',
                               '代理権限証明情報\n波臼さんに頼む（不動産登記令第7条第1項第2号）']):
            box(ax, 1, 66 - i * 25, 48, 21, t, col=BLUE, fs=14)
        box(ax, 52, 54, 47, 33, '住所証明情報\n表題登記で新しく表題部所有者になる人の\n住所を示すもの。表題部の変更の登記では出てこない',
            col=RED, fs=14)
        box(ax, 52, 16, 47, 33, '登記識別情報\n22番は権利部が記録事項なしで、\nそもそも所有権の登記がない', col=RED, fs=14)
    box_fig('問1の添付情報：表題部の変更の登記（不動産登記令別表14の項）で要るもの', 'H22_dai22mon_zu03_toi1_tenpu', draw,
            '答案用紙の欄の名前が「添付情報」なので「〜情報」で書く：建物図面　各階平面図　所有権証明情報　代理権限証明情報。\n'
            '住所証明情報は表題登記（合体後の建物の表題登記を含む問2）で出てくる情報')


def zu14():
    """原因及びその日付（第5章、「欄の番号は付けないのね？」）。"""
    def draw(ax):
        rows = [('合体前　21番の行', '平成22年7月30日22番と合体'), ('合体前　22番の行', '平成22年7月30日21番と合体'),
                ('合体後の建物の行（家屋番号は空欄）', '平成22年7月30日21番、22番を合体')]
        for i, (a, b) in enumerate(rows):
            y = 72 - i * 20
            box(ax, 1, y, 36, 15, a, col=GRAY, fs=15)
            box(ax, 40, y, 59, 15, b, col=BLUE, fs=17, weight='bold', tc=BLUE)
            arrow(ax, (37, y + 7.5), (39.5, y + 7.5))
        box(ax, 1, 6, 47, 24, '欄の番号（①②③）を頭に付けるのは、\n表題部の変更の登記・更正の登記の書き方\n（不動産登記事務取扱手続準則第94条第2項\n「③令和何年何月何日増築」）',
            col=GRAY, fs=13.5)
        box(ax, 52, 6, 47, 24, '誤り：「①②③平成22年7月30日21番、22番を合体」\n→ 合体後の建物は新しく表題登記をする建物なので、\n変更した欄の番号は付けない',
            col=RED, fs=13.5, tc=RED)
    box_fig('原因及びその日付：合体の3行には欄の番号を付けない', 'H22_dai22mon_zu14_genin_ranbangou', draw,
            '合体前の2行は「相手の家屋番号と合体」、合体後の行は「21番、22番を合体」。日付は工事が完了した合体の日の平成22年7月30日')


def zu15():
    """A銀行の抵当権（第5章、問2のなお書きを読み直したところ）。"""
    def draw(ax):
        box(ax, 1, 66, 30, 22, '21番の乙区1番\n抵当権設定\nA銀行', col=BLUE, fs=16)
        box(ax, 35, 66, 30, 22, '問2のなお書き\n「抵当権を消滅させることに\n同意している」', col=GRAY, fs=15)
        box(ax, 69, 66, 30, 22, '抵当権消滅承諾証明情報\nを申請情報と併せて提供\n（不動産登記規則第120条第5項）', col=GRAY, fs=14)
        arrow(ax, (31, 77), (34.5, 77))
        arrow(ax, (65, 77), (68.5, 77))
        box(ax, 18, 33, 64, 22, '登記官が、合体後の建物について\nその抵当権が消滅した旨を登記する（不動産登記法第50条）\n→ 合体後の建物には残らない（存続しない）',
            col=PURPLE, fs=15)
        arrow(ax, (84, 66), (70, 55.5))
        box(ax, 1, 4, 98, 20, '誤り：「表が3行、21番の乙区もちょうど3件。全部書く」\n'
            '→ A銀行の抵当権は存続しないので、「二　抵当権等の登記で合体後の登記建物につき存続すべきものの表示」の表に書かない',
            col=RED, fs=14, tc=RED)
    box_fig('A銀行の抵当権：消滅の承諾があるので、存続登記の表に書かない', 'H22_dai22mon_zu15_a_ginkou_shoumetsu', draw,
            '書かない代わりに、添付情報に「抵当権消滅承諾証明情報」を入れる。残りの2件（B信用金庫の抵当権・永野さんの賃借権）は、\n'
            '存続登記に当たるかを次の図で確かめる')


def zu17():
    """印鑑証明書の要否（第5章、「印鑑証明書は？」）。"""
    def draw(ax):
        ax.text(25, 97, '大面太郎（21番）', ha='center', va='top', fontsize=18, weight='bold', color=BLUE)
        ax.text(76, 97, '大面健一郎（22番）', ha='center', va='top', fontsize=18, weight='bold', color=GREEN)
        box(ax, 1, 58, 48, 30, '21番の所有権の登記名義人で、\n合体による登記等を申請する人\n（不動産登記規則第47条第3号イ（6））', col=BLUE, fs=14.5)
        box(ax, 52, 58, 47, 30, '22番の表題部所有者。所有権の保存の登記で\n登記識別情報の通知を受ける申請人\n（不動産登記規則第47条第3号ホ、不動産登記法第21条本文）',
            col=GREEN, fs=14)
        arrow(ax, (25, 58), (25, 51.5), col=BLUE)
        arrow(ax, (75.5, 58), (75.5, 51.5), col=GREEN)
        box(ax, 1, 22, 48, 29, '書面申請なら申請書・委任状に記名押印して\n印鑑証明書を付ける\n（不動産登記令第16条第2項・第18条第2項）\n→ 要る',
            col=BLUE, fs=14.5, weight='bold')
        box(ax, 52, 22, 47, 29, '印鑑証明書は要らない\n（不動産登記規則第48条第1項第4号・\n第49条第2項第4号）\n→ 要らない',
            col=GREEN, fs=14.5, weight='bold')
        box(ax, 1, 3, 98, 14, '申請書の添付情報には「印鑑証明書」を1つ書く（太郎さんの分）。登記識別情報は、太郎さんの登記済証で代える（不動産登記法附則第7条）',
            col=GRAY, fs=14)
    box_fig('印鑑証明書は太郎さんの分だけ（健一郎さんは要らない）', 'H22_dai22mon_zu17_inkan_shoumei', draw,
            '同じ申請人でも、所有権の登記名義人として合体による登記等を申請する太郎さんと、\n'
            '所有権の保存の登記で登記識別情報の通知を受ける健一郎さんとで、扱いが分かれる')


if __name__ == '__main__':
    for fn in (zu01, zu02, zu03, zu04, zu05, zu06, zu07, zu08, zu09, zu10, zu11, zu12, zu13, zu14, zu15, zu16, zu17, zu18,
               zu19, zu20):
        fn()
    print('重なり合計:', len(PROBLEMS))
