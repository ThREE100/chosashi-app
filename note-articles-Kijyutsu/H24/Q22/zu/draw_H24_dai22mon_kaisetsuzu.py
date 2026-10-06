"""平成24年度 第22問（建物）の解説図14枚を、頂点座標から作図してPNGに書き出す。

`../prompt_H24_dai22mon_kaisetsuzu.md` の図1〜図14どおり。作図の共通部品は `tools/zu_helpers.py`。
建物の座標は (東, 南) で持ち（原点は一棟の建物の北西の角の、壁の中心線の交点）、zu_helpers の (北, 東) には
B() で変換する（北 ＝ −南）。敷地は問題の筆界点の座標成果（X＝北、Y＝東）をそのまま使い、建物は
配置図及び平面図の（注）7のとおり、ⒶとⒷの障壁の中心線をC-F線（Y＝160.00）に合わせて置く
（西の壁の中心 Y＝152.00、北の壁の中心 X＝170.00。配置図の距離〈外壁まで〉とは数センチの差があるが、1/500では見えない）。
図1の右・図7・図11・図12・図13・図14は、箱と矢印・表の固定配置の図（自動の重なり検査の対象外。PNGを目で確かめる）。
図4（建物図面）と図9（各階平面図）は、試験の答案用紙（その2）の欄（右半分が建物図面：家屋番号・建物の所在・申請人・縮尺1/500、
左半分が各階平面図：作成者〈略〉〈平成何年何月何日作成〉・縮尺1/250。リポジトリの public/kijutsu/H24-tatemono/a2.webp）の枠の中に描く。
実行: python3 note-articles-Kijyutsu/H24/Q22/zu/draw_H24_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, FancyBboxPatch, Rectangle  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN,  # noqa: E402
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


# ---- 建物（平面図の寸法線から。壁心は柱及び壁の中心線、内法は中心から0.075内側〈壁の厚さ15cmの半分〉） ----
A1_WALL = [(0, 0), (8, 0), (8, 6.5), (5.5, 6.5), (5.5, 10), (0, 10)]                  # Ⓐ1階（壁心）
B1_WALL = [(8, 0), (16, 0), (16, 6.5), (13.5, 6.5), (13.5, 10), (8, 10)]              # Ⓑ1階（壁心）
WHOLE1 = [(0, 0), (16, 0), (16, 6.5), (13.5, 6.5), (13.5, 10), (8, 10), (8, 6.5), (5.5, 6.5), (5.5, 10), (0, 10)]
WHOLE2 = rect(0, 0, 16, 7.5)
A2_WALL = rect(0, 0, 8, 7.5)
A1 = [(0.075, 0.075), (7.925, 0.075), (7.925, 6.425), (5.425, 6.425), (5.425, 9.925), (0.075, 9.925)]   # Ⓐ1階（内法）
A1_STRIPS = [rect(0.075, 0.075, 7.925, 6.425), rect(0.075, 6.425, 5.425, 9.925)]
A2 = rect(0.075, 0.075, 7.925, 7.425)                                                   # Ⓐ2階（内法）
WHOLE1_STRIPS = [rect(0, 0, 16, 6.5), rect(0, 6.5, 5.5, 10), rect(8, 6.5, 13.5, 10)]

assert area_es(A1_WALL) == 71.25 == area_es(B1_WALL) and area_es(A2_WALL) == 60.00
assert area_es(WHOLE1) == 142.50 == sum(area_es(r) for r in WHOLE1_STRIPS) and area_es(WHOLE2) == 120.00
assert round(area_es(A1), 4) == 68.5725 == round(sum(area_es(r) for r in A1_STRIPS), 4)
assert round(area_es(A2), 4) == 57.6975

# ---- 敷地（筆界点の座標成果。X＝北、Y＝東） ----
A, Bp, C, D, E, F = complex(150, 150), complex(171, 150), complex(171.5, 160), complex(172, 170), complex(150, 169), complex(150, 160)
LOT1 = [A, Bp, C, F]
LOT2 = [F, C, D, E]
assert area(LOT1) == 212.50 and area(LOT2) == 206.50


def S(p):
    """建物の点（B()で作った複素数）を敷地の座標へ。北の壁の中心 X＝170.00、西の壁の中心 Y＝152.00。"""
    return complex(170 + p.real, 152 + p.imag)


def dims(z, pts, labels, fs=14, ref=None, outward=True):
    c = ref or centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs, outward=outward)


def star(z, p, color=BLACK, size=17):
    a, b = xy(p)
    z.ax.plot(a, b, '*', ms=size, color=color, zorder=6)
    z.markers.append((a, b))


def neighbors(z, fs=15):
    z.free_text(complex(174.2, 146.0), '98', fs=fs)
    z.free_text(complex(174.6, 160.0), '97', fs=fs)
    z.free_text(complex(175.0, 172.6), '96－3', fs=fs)
    z.free_text(complex(160.5, 145.3), '119', fs=fs)
    z.free_text(complex(160.5, 173.8), '121－2', fs=fs)
    z.free_text(complex(146.6, 160.0), '道路（43）', fs=fs)


def site_lines(z, lw=2.0):
    """敷地の筆界と隣接地の境の線（建物図面・辺長確認図で共通）。"""
    z.poly(LOT1, color=BLACK, lw=lw)
    z.poly([F, C, D, E], color=BLACK, lw=lw, closed=False)
    z.line(E, F, color=BLACK, lw=lw)
    z.line(Bp, complex(174.5, 150), color=BLACK, lw=1.4)          # 98と119の境の延長（A-B線の北）
    z.line(D, complex(174.5, 170 + 2.5 / 22), color=BLACK, lw=1.4)   # D-E線の北への延長
    z.line(Bp, complex(170.9, 148.0), color=BLACK, lw=1.4)         # B-C-D線の西への延長
    z.line(D, complex(172.1, 172.0), color=BLACK, lw=1.4)          # B-C-D線の東への延長
    z.line(complex(150, 146.5), complex(150, 173.5), color=BLACK, lw=1.6)   # 道路の北の線


# ---- 図1：全体像（土地と専有部分、代位の関係） ----
def zu01():
    fig, axes = new_figure('全体像：兄妹が自分の土地の上にⒶⒷを建て、兄がⒶの表題登記を代位で申請',
                           'C-F線（120番1と120番2の境）＝ⒶとⒷの障壁の中心線（配置図及び平面図の（注）7）。区分建物の表題登記は一棟の全部をあわせて申請（不動産登記法第48条第1項・第2項）',
                           w=18, h=10, ncols=2, width_ratios=[1, 1.05])
    fig.subplots_adjust(top=0.86, bottom=0.12)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(LOT1, color=BLACK, lw=2.0, fill=BLUE, alpha=0.07)
    z.poly(LOT2, color=BLACK, lw=2.0, fill=GREEN, alpha=0.07)
    z.poly([S(p) for p in P(A1_WALL)], color=BLUE, lw=2.4, fill=BLUE, alpha=0.35)
    z.poly([S(p) for p in P(B1_WALL)], color=GREEN, lw=2.4, fill=GREEN, alpha=0.35)
    ax.set_title('配置（1階）', fontsize=17, weight='bold')
    fit(ax, LOT1 + LOT2, margin=0.08, extra=[(146, 146.5), (175, 175)], pad_aspect=True)
    z.north_arrow()
    z.free_text(complex(166.7, 155.4), 'Ⓐ\n乙川夏子', fs=15, weight='bold', color=BLUE)
    z.free_text(complex(166.7, 164.0), 'Ⓑ\n甲野春男', fs=15, weight='bold', color=GREEN)
    z.free_text(complex(157.0, 155.2), '120－1\n（乙川夏子の土地）', fs=13)
    z.free_text(complex(157.0, 164.6), '120－2\n（甲野春男の土地）', fs=13)
    z.callout(complex(152.2, 160), 'C-F線＝障壁の中心線', dirs=(-20, -35, 200, 215), fs=13, color=RED, dists=(30, 45, 60))
    z.point_label(C, 'C', away=complex(160, 160))
    z.point_label(F, 'F', away=complex(160, 160))
    z.free_text(complex(147.6, 160), '道路（43）', fs=13, color=GRAY)
    # 右：代位の関係（固定配置）
    ax2 = axes[1]
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 100)
    ax2.axis('off')
    ax2.set_title('問1：代位による申請の関係', fontsize=17, weight='bold')

    def box(x, y, w, h, text, col, fs=14):
        ax2.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.6', fc=col, ec=col, alpha=0.15, lw=2))
        ax2.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.6', fc='none', ec=col, lw=2))
        ax2.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs)

    box(4, 64, 40, 24, '甲野春男（兄）\nⒷの所有者\n申請人（代位者）', GREEN)
    box(56, 64, 40, 24, '乙川夏子（妹）\nⒶの所有者\n所有者（被代位者）\n海外に長期滞在中', BLUE)
    ax2.annotate('', xy=(55, 76), xytext=(45, 76), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=RED, mutation_scale=22))
    ax2.text(50, 90.5, '代わって申請', ha='center', fontsize=14, color=RED, weight='bold')
    box(4, 30, 92, 20, 'Ⓐの表題登記とⒷの表題登記は「あわせて」申請（第48条第1項）\n'
        'Ⓑの所有者はⒶの所有者に代わって申請できる（第48条第2項）\n→ 代位原因「不動産登記法第48条第2項」', RED, fs=14)
    box(4, 4, 92, 14, '申請書は別々（問1のなお書き）。問1で書くのはⒶの申請書だけ\n乙川夏子の委任状は間に合わない（聴取内容等の（11）（13））', GRAY, fs=13)
    save(fig, [z], 'H24_dai22mon_zu01_zentaizou')


# ---- 図2：敷地の辺長確認図 ----
def zu02():
    fig, axes = new_figure('敷地（120番1・120番2）の辺長確認図（作図チェック用）',
                           '筆界点の座標成果から。北側B-C-Dは一直線（C−B＝D−C＝0.50＋10.00i）、東側D-Eは斜め。辺長は建物図面には書かない',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(LOT1, color=BLACK, lw=2.4, fill=BLUE, alpha=0.08)
    z.poly(LOT2, color=BLACK, lw=2.4, fill=GREEN, alpha=0.08)
    fit(ax, LOT1 + LOT2, margin=0.10, extra=[(144, 145.5), (178, 176.5)], pad_aspect=True)
    z.north_arrow()
    for p, n in [(A, 'A'), (Bp, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F')]:
        z.point(p, 'dot', size=6)
        z.point_label(p, n, away=complex(160.5, 160))
    dims(z, LOT1, ['21.00', '10.01', '', '10.00'], fs=15)
    dims(z, LOT2, ['', '10.01', '22.02', '9.00'], fs=15)
    z.free_text(complex(161.5, 160), '21.50', fs=15, rotation=90, offsets=((-14, 0), (14, 0)))
    z.free_text(complex(162.0, 155.0), '120番1\n212.50㎡\n（登記記録\n212.50㎡）', fs=14)
    z.free_text(complex(162.0, 164.6), '120番2\n座標法 206.50㎡\n（登記記録\n206.60㎡）', fs=14)
    z.free_text(complex(176.0, 146.0), '98', fs=14, color=GRAY)
    z.free_text(complex(176.0, 160.0), '97', fs=14, color=GRAY)
    z.free_text(complex(176.0, 173.0), '96－3', fs=14, color=GRAY)
    z.free_text(complex(160.5, 145.2), '119', fs=14, color=GRAY)
    z.free_text(complex(160.5, 174.6), '121－2', fs=14, color=GRAY)
    z.free_text(complex(146.6, 160.0), '道路（43）', fs=14, color=GRAY)
    save(fig, [z], 'H24_dai22mon_zu02_shikichi_henchou')


# ---- 図4：建物図面の完成形（答案用紙（その2）の右半分の欄の枠の中） ----
INK = '#1a3a8f'   # 記入（濃い青）
SHOZAI = 'A市B町三丁目120番地1、120番地2'


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.012
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


def dim_line(z, p, q, text, dirs=None, offsets=((12, 0),)):
    ax = z.ax
    ax.annotate('', xy=xy(q), xytext=xy(p),
                arrowprops=dict(arrowstyle='<->', lw=1.4, color=BLACK, shrinkA=0, shrinkB=0), zorder=4)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    if dirs:
        return z.callout(m, text, dirs=dirs, fs=15, dists=(40, 55, 70))
    return z.free_text(m, text, fs=15, offsets=offsets)


def zu04():
    setup_font()
    fig = plt.figure(figsize=(16, 17), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面（Ⓐの申請書に付ける）の完成形（答案用紙（その2）の右半分・縮尺1/500で描く内容）', fontsize=21,
                 weight='bold', y=0.985)
    # 答案用紙（その2）の右半分の欄（家屋番号・建物の所在は、左半分の各階平面図と共通の欄）
    cell(fig, 0.06, 0.900, 0.20, 0.945, '家屋番号', fs=15)
    cell(fig, 0.20, 0.900, 0.50, 0.945, '', fs=15)                        # 家屋番号は登記所が付けるので空欄
    fig.text(0.74, 0.935, '建　物　図　面', ha='center', va='center', fontsize=19)
    fig.text(0.74, 0.910, '各　階　平　面　図', ha='center', va='center', fontsize=19)
    cell(fig, 0.06, 0.855, 0.20, 0.900, '建物の所在', fs=15)
    cell(fig, 0.20, 0.855, 0.94, 0.900, SHOZAI, fs=16, ha='left', color=INK)
    cell(fig, 0.06, 0.095, 0.94, 0.855, lw=1.8)
    cell(fig, 0.06, 0.045, 0.20, 0.095, '申　請　人', fs=15)
    cell(fig, 0.20, 0.045, 0.74, 0.095, '甲野春男', fs=16, color=INK)
    cell(fig, 0.74, 0.045, 0.83, 0.095, '縮尺', fs=15)
    cell(fig, 0.83, 0.045, 0.94, 0.095, '1/500', fs=15)
    fig.text(0.5, 0.018, 'Ⓐの1階を実線、Ⓑの1階を点線（不動産登記事務取扱手続準則第52条第2項）。距離は配置図の測定値（外壁まで）。'
             '敷地の辺長は書かない', ha='center', va='center', fontsize=14)
    ax = fig.add_axes([0.08, 0.11, 0.84, 0.73])
    z = Zu(ax, fontsize=14)
    fit(ax, LOT1 + LOT2, margin=0.08, extra=[(144.5, 145.0), (177.5, 176.0)], pad_aspect=True)
    z.north_arrow()
    site_lines(z, lw=2.0)
    a_site = [S(p) for p in P(A1_WALL)]
    b_site = [S(p) for p in P(B1_WALL)]
    z.poly(a_site, color=BLACK, lw=2.8)
    z.poly(b_site[:-1] + [b_site[-1]], color=BLACK, lw=1.6, ls='--', closed=False)   # 西の辺（障壁）はⒶの実線と重なるので描かない
    assert round(area(a_site), 2) == 71.25 and round(area(a_site) + area(b_site), 2) == 142.50
    x_nw = 170.0
    dim_line(z, complex(x_nw - 0.8, 150), complex(x_nw - 0.8, 152), '2.00', dirs=(180, 165, 195))
    dim_line(z, complex(160.8, 150), complex(160.8, 152), '2.00', dirs=(180, 195, 165))
    y_n = 153.2
    dim_line(z, complex(170.0, y_n), complex(171 + 0.05 * (y_n - 150), y_n), '1.00', dirs=(120, 135, 105, 150))
    z.free_text(complex(166.0, 155.2), 'Ⓐ', fs=17, weight='bold')
    z.free_text(complex(155.0, 155.0), '120－1', fs=16)
    z.free_text(complex(155.0, 164.5), '120－2', fs=16)
    neighbors(z)
    z.free_text(complex(146.0, 172.5), '（単位：m）', fs=13)
    save(fig, [z], 'H24_dai22mon_zu04_tatemono_zumen')


# ---- 図5：誤り比較図（壁心／内法） ----
def zu05():
    fig, axes = new_figure('Ⓐ区画1階の床面積：壁心か、内法か',
                           '区分建物の床面積は壁その他の区画の内側線で囲まれた部分（不動産登記規則第115条）。外まわりの辺は0.15短くなり、欠けの2.50×3.50は変わらない',
                           w=18, h=9.5, ncols=3, width_ratios=[1, 0.8, 1])
    fig.subplots_adjust(top=0.84)
    z = Zu(axes[0], fontsize=13)
    z.poly(P(A1_WALL), color=RED, lw=2.4, fill=RED, alpha=0.18)
    axes[0].set_title('誤り：壁心のまま 71.25㎡（藍子）', fontsize=16, weight='bold', color=RED)
    fit(axes[0], P(A1_WALL), margin=0.24, pad_aspect=True)
    dims(z, P(A1_WALL), ['8.00', '6.50', '2.50', '3.50', '5.50', '10.00'], fs=13)
    z.free_text(B(3.0, 5.0), '8.00×6.50\n＋5.50×3.50\n＝71.25㎡', fs=13, color=RED)
    # 拡大（壁の断面：北西の角）
    z2 = Zu(axes[1], fontsize=12)
    wall = [complex(0.25, -0.25), complex(0.25, 0.9), complex(-0.1, 0.9), complex(-0.1, 0.1), complex(-0.9, 0.1),
            complex(-0.9, -0.25)]
    z2.poly(wall, color=GRAY, lw=0, fill=GRAY, alpha=0.30, check=False)
    hatch(axes[1], wall)
    z2.line(complex(0.075, -0.25), complex(0.075, 0.9), color=BLACK, lw=1.2, ls='-.')
    z2.line(complex(-0.9, -0.075), complex(0.25, -0.075), color=BLACK, lw=1.2, ls='-.')
    z2.line(complex(-0.1, 0.1), complex(-0.1, 0.9), color=GREEN, lw=3)
    z2.line(complex(-0.1, 0.1), complex(-0.9, 0.1), color=GREEN, lw=3)
    axes[1].set_title('北西の角（拡大・模式）', fontsize=16, weight='bold')
    fit(axes[1], wall, margin=0.25, pad_aspect=True)
    axes[1].annotate('', xy=xy(complex(-0.1, 0.55)), xytext=xy(complex(0.075, 0.55)),
                     arrowprops=dict(arrowstyle='<->', lw=1.4, color=RED, shrinkA=0, shrinkB=0))
    z2.segments.append((xy(complex(-0.1, 0.55)), xy(complex(0.075, 0.55))))
    z2.callout(complex(-0.012, 0.55), '0.075（壁の厚さ15cmの半分）', dirs=(-60, -40, -80), fs=12, color=RED)
    z2.callout(complex(0.16, 0.5), '壁の中心線（壁心）', dirs=(90, 70, 110), fs=12)
    z2.callout(complex(-0.6, 0.1), '内壁の面（内法）', dirs=(-90, -110, -70), fs=12, color=GREEN)
    # 正解（内法）
    z3 = Zu(axes[2], fontsize=13)
    z3.poly(P(A1_WALL), color=GRAY, lw=1.0, ls=':', check=False)
    z3.poly(P(A1), color=GREEN, lw=2.4, fill=GREEN, alpha=0.20)
    axes[2].set_title('正解：内法で 68.57㎡', fontsize=16, weight='bold', color=GREEN)
    fit(axes[2], P(A1_WALL), margin=0.24, pad_aspect=True)
    dims(z3, P(A1), ['7.85', '6.35', '2.50', '3.50', '5.35', '9.85'], fs=13)
    z3.free_text(B(3.0, 5.0), '7.85×6.35\n＋5.35×3.50\n＝68.5725\n→ 68.57㎡', fs=13, color=GREEN)
    save(fig, [z, z2, z3], 'H24_dai22mon_zu05_ayamari_hikaku')


# ---- 図6・図8：Ⓐ区画の求積図 ----
def zu06():
    fig, axes = new_figure('Ⓐ区画1階の床面積求積図（内法）',
                           '7.85×6.35＋5.35×3.50＝68.5725、切り捨てて68.57㎡。南東の角の欠け（2.50×3.50）は床面積に入れない',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    for r, c in zip(A1_STRIPS, [ORANGE, BLUE]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.25, check=False)
    z.line(B(0.075, 6.425), B(5.425, 6.425), color=GRAY, lw=1.0, ls='--')
    z.poly(P(A1), color=BLACK, lw=2.4)
    fit(ax, P(A1), margin=0.22, pad_aspect=True)
    z.north_arrow()
    star(z, B(0.075, 0.075))
    dims(z, P(A1), ['7.85', '6.35', '2.50', '3.50', '5.35', '9.85'], fs=15)
    z.free_text(B(4.0, 3.2), '7.85×6.35\n＝49.8475', fs=16)
    z.free_text(B(2.75, 8.2), '5.35×3.50\n＝18.7250', fs=15)
    z.free_text(B(6.9, 8.9), '欠け\n（入れない）', fs=13, color=GRAY, offsets=((0, 0), (10, -10), (14, -18), (18, -24)))
    z.free_text(B(4.0, 11.4), '1階　床面積：68.57㎡（68.5725）', fs=17, weight='bold')
    save(fig, [z], 'H24_dai22mon_zu06_1kai_kyuuseki')


def zu08():
    fig, axes = new_figure('Ⓐ区画2階の床面積求積図（内法）',
                           '7.85×7.35＝57.6975、切り捨てて57.69㎡（四捨五入の57.70ではない）。点線は1階の外形。★は1階と2階の重なる位置',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(P(A2), color=BLACK, lw=2.4, fill=BLUE, alpha=0.22)
    z.poly(P([(5.425, 7.425), (5.425, 9.925), (0.075, 9.925), (0.075, 7.425)]), color=BLACK, lw=1.4, ls='--',
           closed=False)
    z.poly(P([(5.425, 7.425), (5.425, 6.425), (7.925, 6.425)]), color=BLACK, lw=1.4, ls='--', closed=False)
    fit(ax, P(A1), margin=0.22, pad_aspect=True)
    z.north_arrow()
    star(z, B(0.075, 0.075))
    dims(z, P(A2), ['7.85', '7.35', '7.85', '7.35'], fs=15)
    z.free_text(B(3.2, 3.4), '7.85×7.35\n＝57.6975', fs=16)
    z.callout(B(0.075, 8.7), '1階の南西の帯（2階より南へ2.50）', dirs=(200, 180, 220), fs=13)
    z.callout(B(6.675, 6.425), '1階の欠けの上に1.00張り出す', dirs=(20, 0, 40), fs=13)
    z.free_text(B(4.0, 11.3), '2階　床面積：57.69㎡（57.6975）', fs=17, weight='bold')
    save(fig, [z], 'H24_dai22mon_zu08_2kai_kyuuseki')


# ---- 図9：各階平面図の完成形 ----
def zu09():
    """各階平面図の完成形。答案用紙（その2）の左半分の欄（作成者〈略〉・縮尺1/250）の枠の中に、1階を上・2階を下に描く。"""
    setup_font()
    fig = plt.figure(figsize=(16, 17), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図（Ⓐ区画）の完成形（答案用紙（その2）の左半分・縮尺1/250で描く内容）', fontsize=21,
                 weight='bold', y=0.985)
    fig.text(0.5, 0.925, '（家屋番号・建物の所在の欄は、建物図面の側の上に1つだけ。両方の図面に共通〈図4〉）', ha='center', va='center',
             fontsize=15)
    cell(fig, 0.06, 0.095, 0.94, 0.900, lw=1.8)
    cell(fig, 0.06, 0.045, 0.20, 0.095, '作　成　者', fs=15)
    cell(fig, 0.20, 0.045, 0.74, 0.095, '（略）　　　　　　　（平成何年何月何日作成）', fs=15)
    cell(fig, 0.74, 0.045, 0.83, 0.095, '縮尺', fs=15)
    cell(fig, 0.83, 0.045, 0.94, 0.095, '1/250', fs=15)
    fig.text(0.5, 0.018, '「1階」「2階」を書き分け、辺長は内法。2階には1階の位置を点線（不動産登記事務取扱手続準則第53条）。'
             '求積方法と床面積を添える', ha='center', va='center', fontsize=14)
    ax1 = fig.add_axes([0.08, 0.50, 0.84, 0.37])
    ax2 = fig.add_axes([0.08, 0.11, 0.84, 0.37])
    z = Zu(ax1, fontsize=15)
    fit(ax1, P(A1), margin=0.12, extra=[xy(B(17.5, 5))], pad_aspect=True)
    ax1.set_title('1階', fontsize=18, weight='bold', loc='left')
    z.poly(P(A1), color=BLACK, lw=2.4)
    dims(z, P(A1), ['7.85', '6.35', '2.50', '3.50', '5.35', '9.85'], fs=16)
    z.free_text(B(13.3, 4.5), '求積\n7.85×6.35＝49.8475\n5.35×3.50＝18.7250\n　　　計　68.5725\n床面積　68.57㎡', fs=16,
                ha='center')
    z2 = Zu(ax2, fontsize=15)
    fit(ax2, P(A1), margin=0.12, extra=[xy(B(17.5, 5))], pad_aspect=True)
    ax2.set_title('2階', fontsize=18, weight='bold', loc='left')
    z2.poly(P(A2), color=BLACK, lw=2.4)
    z2.poly(P([(5.425, 7.425), (5.425, 9.925), (0.075, 9.925), (0.075, 7.425)]), color=BLACK, lw=1.3, ls='--',
            closed=False)
    z2.poly(P([(5.425, 7.425), (5.425, 6.425), (7.925, 6.425)]), color=BLACK, lw=1.3, ls='--', closed=False)
    dims(z2, P(A2), ['7.85', '7.35', '7.85', '7.35'], fs=16)
    z2.free_text(B(13.3, 4.0), '求積\n7.85×7.35＝57.6975\n床面積　57.69㎡', fs=16, ha='center')
    save(fig, [z, z2], 'H24_dai22mon_zu09_kakai_heimenzu')


# ---- 図12：敷地権になるかどうかの比較（固定配置） ----
def zu12():
    setup_font()
    fig = plt.figure(figsize=(18, 10), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('敷地権になるか：土地をどう持っているかで決まる（区分所有法第22条）', fontsize=24, weight='bold', y=0.965)
    cases = [
        ('①土地を数人で共有', '第22条第1項本文', '敷地権になる', GREEN,
         [('Ⓐ', 'Ⓑ')], '土地：Ⓐの所有者とⒷの所有者の共有', '数人で有する所有権\n→ 分離して処分できない'),
        ('②1人が専有部分の全部と\n土地を持つ（R3・H27）', '第22条第3項', '敷地権になる', GREEN,
         [('Ⓐ', 'Ⓑ')], '土地：専有部分の全部を持つ人の単独所有', '専有部分の全部を所有する者の\n単独の所有権 → 準用'),
        ('③本件：分有', '第1項も第3項も当たらない', '敷地権にならない', RED,
         [('Ⓐ', 'Ⓑ')], '120番1：乙川夏子の単独所有\n120番2：甲野春男の単独所有',
         '相手の土地の無償の使用（使用貸借）は\n登記できない（不動産登記法第3条）'),
    ]
    for k, (title, law, res, col, _, land, note) in enumerate(cases):
        ax = fig.add_axes([0.03 + k * 0.325, 0.08, 0.30, 0.78])
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        ax.add_patch(FancyBboxPatch((2, 2), 96, 96, boxstyle='round,pad=0.5', fc=col, alpha=0.06, ec=col, lw=2))
        ax.text(50, 92, title, ha='center', va='top', fontsize=17, weight='bold')
        # 建物（ⒶⒷ）と土地
        ax.add_patch(plt.Rectangle((14, 52), 36, 18, fc=BLUE, alpha=0.35, ec=BLACK, lw=1.8))
        ax.add_patch(plt.Rectangle((50, 52), 36, 18, fc=GREEN, alpha=0.35, ec=BLACK, lw=1.8))
        ax.text(32, 61, 'Ⓐ', ha='center', va='center', fontsize=18, weight='bold')
        ax.text(68, 61, 'Ⓑ', ha='center', va='center', fontsize=18, weight='bold')
        if k == 2:
            ax.add_patch(plt.Rectangle((8, 40), 42, 10, fc=BLUE, alpha=0.12, ec=BLACK, lw=1.6))
            ax.add_patch(plt.Rectangle((50, 40), 42, 10, fc=GREEN, alpha=0.12, ec=BLACK, lw=1.6))
            ax.text(29, 45, '120番1', ha='center', va='center', fontsize=13)
            ax.text(71, 45, '120番2', ha='center', va='center', fontsize=13)
        else:
            ax.add_patch(plt.Rectangle((8, 40), 84, 10, fc=GRAY, alpha=0.15, ec=BLACK, lw=1.6))
            ax.text(50, 45, '土地（1筆）', ha='center', va='center', fontsize=13)
        ax.text(50, 35, land, ha='center', va='top', fontsize=13)
        ax.text(50, 24, law, ha='center', va='top', fontsize=14, color=col, weight='bold')
        ax.text(50, 18.5, note, ha='center', va='top', fontsize=12)
        ax.text(50, 80, res, ha='center', va='center', fontsize=19, color=col, weight='bold')
    path = os.path.join(OUT, 'H24_dai22mon_zu12_shikichiken.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図12: 敷地権の比較（固定配置）\n  →', path)


# ---- 図14：本番で解く順番（固定配置） ----
def zu14():
    setup_font()
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　知識で書ける問3と申請書の欄を先に', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '問1〜問3\nを先に読む', '「代位」「図面」\n「敷地権」を\n探す目を作る', BLUE),
        ('②', '問3', '敷地権の説明\n（聴取内容等の\n（1）（4）（14））', BLUE),
        ('③', '申請書の\n床面積以外', '目的・添付書類・\n代位の3欄・所在・\n構造・一棟の壁心', BLUE),
        ('④', 'Ⓐの内法\nの求積', '68.57\n57.69（切り捨て）', RED),
        ('⑤', '作図', '建物図面・\n各階平面図', RED),
        ('⑥', '見直し', '内法と壁心・\n所在の2筆・屋根・\n代位原因・\n代理権限証書', GRAY),
    ]
    w, h, gap = 14.4, 42, 2.4
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 22), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 22 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
        ax.text(x + w / 2, 22 + h / 2 - 3, t, ha='center', va='center', fontsize=17)
        ax.text(x + w / 2, 18, ran, ha='center', va='top', fontsize=14, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, 43), xytext=(x + w + 0.2, 43),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 1.5 * (w + gap) - gap / 2, 76, '内法の求積をしなくても書ける', ha='center', fontsize=15, color=BLUE,
            weight='bold')
    ax.annotate('', xy=(1 + 3 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 4 * (w + gap) - gap / 2, 76, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 5 * (w + gap) - gap, 72), xytext=(1 + 3 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.07, '一棟の建物の床面積（壁心の142.50・120.00）は平面図の寸法そのままで出るので、③で書いてしまう。\n'
             'Ⓐの内法（0.075ずつ内側）の求積と作図を後にすれば、時間が足りなくなっても申請書と問3の点は取れている。',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'H24_dai22mon_zu14_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図14: 解く順番（固定配置）\n  →', path)


# ======== 2026-10-05追加：本文に対して足りなかった図（図3・図7・図10・図11・図13） ========
HALF = 0.075                                       # 壁の厚さ15cmの半分
bcd_x = lambda y: 171 + 0.05 * (y - 150)           # B-C-D線のX（東へ行くほど北へ上がる）
de_y = lambda x: 169 + (x - 150) / 22              # D-E線のY（北へ行くほど東へ開く）
W_FACE, E_FACE, N_FACE = 152.00 - HALF, 168.00 + HALF, 170.00 + HALF
S2_FACE = 170.00 - 7.50 - HALF                     # 2階の南の外壁（Ⓑの2階の南東の角）
S1_FACE = 170.00 - 10.00 - HALF                    # 1階の南西の帯の南の外壁
MARGINS = {'西（A-B線まで）': W_FACE - 150, '北西の角（B-C線まで）': bcd_x(W_FACE) - N_FACE,
           '北東の角（C-D線まで）': bcd_x(E_FACE) - N_FACE, '東・北の端（D-E線まで）': de_y(N_FACE) - E_FACE,
           '東・2階の南東の角（D-E線まで）': de_y(S2_FACE) - E_FACE, '南（道路まで）': S1_FACE - 150}
assert round(MARGINS['西（A-B線まで）'], 3) == 1.925
assert [round(v, 1) for v in list(MARGINS.values())[1:5]] == [1.0, 1.8, 1.8, 1.5] and round(MARGINS['南（道路まで）']) == 10
assert round(2.00 + HALF + 8.00, 3) == 10.075 and abs(F - A) == 10.00          # 7.5センチの食い違い


def mdim(z, p, q, text, dirs):
    """寸法線（両矢印）と値の吹き出し。線分は重なり検査に登録する。"""
    z.ax.annotate('', xy=xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='<->', lw=1.4, color=RED, shrinkA=0, shrinkB=0),
                  zorder=4)
    z.segments.append((xy(p), xy(q)))
    return z.callout((p + q) / 2, text, dirs=dirs, fs=13, color=RED, dists=(35, 50, 65, 80))


# ---- 図3：建物の位置と所在の確認図（2筆だけにかかるか、7.5センチの食い違い） ----
def zu03():
    fig, axes = new_figure('建物の位置と所在の確認：一棟の建物は120番1と120番2の2筆だけにかかる',
                           '障壁の中心をC-F線に合わせて置く（配置図及び平面図の（注）7）。外壁から筆界までの間隔はどこも0より大きい\n'
                           '西の外壁までは計算で1.925。配置図の2.00と7.5センチ違うが、1/500では0.15mmで見えない',
                           w=18, h=11, ncols=2, width_ratios=[1.45, 1])
    fig.subplots_adjust(top=0.86)
    ax = axes[0]
    z = Zu(ax, fontsize=13)
    ax.set_title('配置（1階を実線、2階の外形を点線）', fontsize=16, weight='bold')
    z.poly(LOT1, color=BLACK, lw=2.0, fill=BLUE, alpha=0.06)
    z.poly(LOT2, color=BLACK, lw=2.0, fill=GREEN, alpha=0.06)
    z.poly([S(p) for p in P(A1_WALL)], color=BLUE, lw=2.2, fill=BLUE, alpha=0.30)
    z.poly([S(p) for p in P(B1_WALL)], color=GREEN, lw=2.2, fill=GREEN, alpha=0.30)
    z.poly([S(p) for p in P(WHOLE2)], color=BLACK, lw=1.2, ls='--', check=False)
    fit(ax, LOT1 + LOT2, margin=0.06, extra=[(145.5, 147.0), (176.0, 175.5)], pad_aspect=True)
    z.north_arrow()
    for p_, n in [(A, 'A'), (Bp, 'B'), (C, 'C'), (D, 'D'), (E, 'E'), (F, 'F')]:
        z.point_label(p_, n, away=complex(160.5, 160), fs=13)
    mdim(z, complex(166.0, 150), complex(166.0, W_FACE), '1.925', dirs=(180, 200, 160))
    mdim(z, complex(N_FACE, 153.0), complex(bcd_x(153.0), 153.0), '約1.0', dirs=(110, 130, 90))
    mdim(z, complex(N_FACE, 166.6), complex(bcd_x(166.6), 166.6), '約1.8', dirs=(100, 80, 120))
    mdim(z, complex(169.0, E_FACE), complex(169.0, de_y(169.0)), '約1.8', dirs=(0, 20, -20))
    mdim(z, complex(S2_FACE, E_FACE), complex(S2_FACE, de_y(S2_FACE)), '約1.5（2階の南東の角）', dirs=(0, -20, 20))
    mdim(z, complex(S1_FACE, 153.2), complex(150, 153.2), '約10', dirs=(0, 20, -20))
    z.free_text(complex(165.5, 155.6), 'Ⓐ', fs=17, weight='bold', color=BLUE)
    z.free_text(complex(165.5, 164.4), 'Ⓑ', fs=17, weight='bold', color=GREEN)
    z.free_text(complex(151.8, 156.4), '120－1\n（乙川夏子）', fs=13)
    z.free_text(complex(151.8, 164.6), '120－2\n（甲野春男）', fs=13)
    z.callout(complex(161.0, 160), '障壁の中心＝C-F線', dirs=(-60, -80, -40), fs=13, dists=(40, 55, 70))
    # 右：西の外壁の拡大（模式ではなく実寸の座標で拡大）
    ax2 = axes[1]
    z2 = Zu(ax2, fontsize=13)
    ax2.set_title('西の外壁の拡大（実寸）', fontsize=16, weight='bold')
    y0, y1 = 149.55, 152.45
    xa, xb = 164.2, 166.6
    z2.line(complex(xa, 150), complex(xb, 150), color=BLACK, lw=3.0)
    wall = [complex(xa, W_FACE), complex(xb, W_FACE), complex(xb, 152.0 + HALF), complex(xa, 152.0 + HALF)]
    z2.poly(wall, color=GRAY, lw=0, fill=GRAY, alpha=0.35, check=False)
    hatch(ax2, wall)
    z2.line(complex(xa, W_FACE), complex(xb, W_FACE), color=BLUE, lw=2.2)
    z2.line(complex(xa, 152.0), complex(xb, 152.0), color=BLACK, lw=1.2, ls='-.')
    fit(ax2, [complex(xa, y0), complex(xb, y1)], margin=0.08, pad_aspect=True)
    z2.callout(complex(166.3, 150), 'A-B線（筆界）', dirs=(20, 40, 0), fs=12)
    z2.callout(complex(166.4, 152.0), '壁の中心 Y＝152.00\n（＝C-F線の8.00西）', dirs=(160, 145, 175), fs=12, dists=(30, 45, 60))
    z2.callout(complex(164.5, W_FACE), '外壁の面 151.925', dirs=(-150, -130, -170), fs=12, color=BLUE)
    p1, q1 = complex(165.0, 150), complex(165.0, W_FACE)
    ax2.annotate('', xy=xy(q1), xytext=xy(p1), arrowprops=dict(arrowstyle='<->', lw=1.4, color=BLUE, shrinkA=0, shrinkB=0))
    z2.segments.append((xy(p1), xy(q1)))
    z2.callout((p1 + q1) / 2, '計算 1.925', dirs=(-100, -80, -120), fs=13, color=BLUE, dists=(30, 45, 60))
    p2, q2 = complex(165.8, 150), complex(165.8, 152.0)
    ax2.annotate('', xy=xy(q2), xytext=xy(p2), arrowprops=dict(arrowstyle='<->', lw=1.4, color=RED, shrinkA=0, shrinkB=0))
    z2.segments.append((xy(p2), xy(q2)))
    z2.callout((p2 + q2) / 2, '配置図 2.00（外壁まで）', dirs=(-80, -60, -100), fs=13, color=RED, dists=(25, 35, 45))
    z2.free_text(complex(163.6, 151.0), '差 0.075（7.5センチ）\n1/500 で 0.15mm', fs=13, color=RED)
    save(fig, [z, z2], 'H24_dai22mon_zu03_ichi_kakunin')


# ---- 図7：床面積の端数（切り捨て／四捨五入）（固定配置） ----
def zu07():
    setup_font()
    fig = plt.figure(figsize=(16, 9), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('床面積の端数：1平方メートルの100分の1未満は切り捨て（不動産登記規則第115条）', fontsize=22, weight='bold',
                 y=0.955)
    ax = fig.add_axes([0.03, 0.12, 0.94, 0.74])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    def bx(x, y, w, h, text, col, fs=17, weight='normal'):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.4', fc=col, alpha=0.13, ec=col, lw=2))
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.4', fc='none', ec=col, lw=2))
        ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs, weight=weight)

    rows = [(60, '1階', '7.85×6.35＋5.35×3.50\n＝68.5725', '68.57', '68.57', GRAY, GRAY,
             'どちらでも68.57\n（違いが出ないので\n気づきにくい）'),
            (14, '2階', '7.85×7.35\n＝57.6975', '57.69', '57.70', GREEN, RED,
             '切り捨ての57.69が正しい\n（四捨五入の57.70は誤り）')]
    for y, kai, shiki, kiri, shisha, c1, c2, note in rows:
        bx(1, y, 8, 22, kai, BLACK, fs=20, weight='bold')
        bx(12, y, 26, 22, shiki, BLACK, fs=17)
        ax.annotate('', xy=(46, y + 16), xytext=(39.5, y + 13), arrowprops=dict(arrowstyle='-|>', lw=1.8, color=GRAY))
        ax.annotate('', xy=(46, y + 6), xytext=(39.5, y + 9), arrowprops=dict(arrowstyle='-|>', lw=1.8, color=GRAY))
        bx(47, y + 12.5, 22, 9.5, f'切り捨て　{kiri}', c1, fs=17, weight='bold')
        bx(47, y + 0.5, 22, 9.5, f'四捨五入　{shisha}', c2, fs=17, weight='bold')
        ax.text(72, y + 11, note, ha='left', va='center', fontsize=15, color=(c2 if c2 != GRAY else BLACK))
    fig.text(0.5, 0.05, '57.6975 の 0.0075 は、四捨五入なら繰り上がるが、床面積は切り捨てる。求積表の合計ごとに、どちらで変わるかを確かめる',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'H24_dai22mon_zu07_hasuu.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図7: 端数の処理（固定配置）\n  →', path)


# ---- 図10：一棟の建物の床面積求積図（壁心） ----
def zu10():
    fig, axes = new_figure('一棟の建物の床面積求積図（壁心）',
                           '一棟の建物は区分建物ではないので壁心で外形全体を測る。1階 104.00＋19.25×2＝142.50㎡、2階 120.00㎡'
                           '（Ⓐの内法の2倍137.14・115.38は誤り）',
                           w=18, h=10.5, ncols=2)
    fig.subplots_adjust(top=0.85)
    z = Zu(axes[0], fontsize=13)
    for r, c in zip(WHOLE1_STRIPS, [ORANGE, BLUE, BLUE]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.25, check=False)
    z.line(B(0, 6.5), B(5.5, 6.5), color=GRAY, lw=1.0, ls='--')
    z.line(B(8, 6.5), B(13.5, 6.5), color=GRAY, lw=1.0, ls='--')
    z.line(B(8, 0), B(8, 6.5), color=GRAY, lw=1.0, ls=':')
    z.poly(P(WHOLE1), color=BLACK, lw=2.4)
    axes[0].set_title('1階', fontsize=18, weight='bold')
    fit(axes[0], P(WHOLE1), margin=0.16, extra=[xy(B(8, 12.6))], pad_aspect=True)
    z.north_arrow()
    dims(z, P(WHOLE1), ['16.00', '6.50', '', '', '5.50', '', '', '', '5.50', '10.00'], fs=14)
    z.free_text(B(4.0, 3.25), '16.00×6.50＝104.00', fs=15)
    z.free_text(B(2.75, 8.25), '5.50×3.50\n＝19.25', fs=13)
    z.free_text(B(10.75, 8.25), '5.50×3.50\n＝19.25', fs=13)
    z.free_text(B(6.75, 8.4), '欠け', fs=12, color=GRAY)
    z.free_text(B(14.75, 8.4), '欠け', fs=12, color=GRAY)
    z.free_text(B(8.0, 12.3), '104.00＋19.25＋19.25＝142.50㎡', fs=16, weight='bold')
    z2 = Zu(axes[1], fontsize=13)
    z2.poly(P(WHOLE2), color=BLACK, lw=2.4, fill=ORANGE, alpha=0.22)
    z2.line(B(8, 0), B(8, 7.5), color=GRAY, lw=1.0, ls=':')
    axes[1].set_title('2階', fontsize=18, weight='bold')
    fit(axes[1], P(WHOLE1), margin=0.16, extra=[xy(B(8, 12.6))], pad_aspect=True)
    dims(z2, P(WHOLE2), ['16.00', '7.50', '', ''], fs=14)
    z2.free_text(B(4.0, 3.75), '16.00×7.50＝120.00', fs=15)
    z2.free_text(B(8.0, 12.3), '120.00㎡', fs=16, weight='bold')
    save(fig, [z, z2], 'H24_dai22mon_zu10_ittou_kyuuseki')


# ---- 図11：縦割りと階層的な区分（構造の屋根の種類）（固定配置） ----
def zu11():
    setup_font()
    fig = plt.figure(figsize=(18, 10), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('区分建物の構造に屋根の種類を書くか：区分のしかたで決まる（不動産登記事務取扱手続準則第81条第3項）', fontsize=21,
                 weight='bold', y=0.965)
    for k in range(2):
        ax = fig.add_axes([0.03 + k * 0.49, 0.06, 0.45, 0.82])
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        if k == 0:
            ax.text(50, 95, '階層的な区分（例：マンションの部屋）', ha='center', fontsize=18, weight='bold')
            ax.add_patch(Rectangle((20, 30), 60, 45, fc='white', ec=BLACK, lw=2))
            for yy in (45, 60):
                ax.plot([20, 80], [yy, yy], color=BLACK, lw=1.4)
            for xx in (40, 60):
                ax.plot([xx, xx], [30, 75], color=BLACK, lw=1.0)
            ax.add_patch(Rectangle((40, 45), 20, 15, fc=PURPLE, alpha=0.35, ec=PURPLE, lw=2.5))
            ax.plot([16, 84], [76.5, 76.5], color=BLACK, lw=4)
            ax.text(86, 77, '屋根', ha='left', va='center', fontsize=14)
            ax.text(50, 52.5, '専有部分', ha='center', va='center', fontsize=14, weight='bold')
            ax.text(12, 37.5, '1階', ha='center', va='center', fontsize=13)
            ax.text(12, 52.5, '2階', ha='center', va='center', fontsize=13)
            ax.text(12, 67.5, '3階', ha='center', va='center', fontsize=13)
            ax.text(50, 22, '下の階と上の階で持ち主が違う。\nその専有部分には屋根がない', ha='center', va='top', fontsize=15)
            ax.text(50, 8, '屋根の種類を書かなくてよい', ha='center', va='center', fontsize=17, color=PURPLE, weight='bold')
        else:
            ax.text(50, 95, '縦割りの区分（本件）', ha='center', fontsize=18, weight='bold')
            ax.add_patch(Rectangle((20, 30), 30, 36, fc=BLUE, alpha=0.35, ec=BLUE, lw=2.5))
            ax.add_patch(Rectangle((50, 30), 30, 36, fc=GREEN, alpha=0.18, ec=BLACK, lw=1.6))
            ax.add_patch(MPoly([(20, 66), (35, 82), (50, 82), (50, 66)], closed=True, fc=BLUE, alpha=0.35, ec=BLUE, lw=2.5))
            ax.add_patch(MPoly([(50, 66), (50, 82), (65, 82), (80, 66)], closed=True, fc=GREEN, alpha=0.18, ec=BLACK, lw=1.6))
            ax.plot([20, 80], [48, 48], color=BLACK, lw=1.0, ls=':')
            ax.plot([50, 50], [30, 82], color=BLACK, lw=2.4)
            ax.text(35, 48, 'Ⓐ\n乙川夏子', ha='center', va='center', fontsize=15, weight='bold')
            ax.text(65, 48, 'Ⓑ\n甲野春男', ha='center', va='center', fontsize=15, weight='bold')
            ax.text(86, 74, 'かわら', ha='left', va='center', fontsize=14)
            ax.text(12, 39, '1階', ha='center', va='center', fontsize=13)
            ax.text(12, 57, '2階', ha='center', va='center', fontsize=13)
            ax.text(50, 22, 'Ⓐは1階の床から屋根まで丸ごと乙川夏子のもの\n（障壁の中心線＝C-F線で縦に分かれる）', ha='center', va='top',
                    fontsize=15)
            ax.text(50, 8, '屋根の種類まで書く：木造かわらぶき2階建', ha='center', va='center', fontsize=17, color=BLUE,
                    weight='bold')
    path = os.path.join(OUT, 'H24_dai22mon_zu11_tatewari_kaisou.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図11: 縦割りと階層的な区分（固定配置）\n  →', path)


# ---- 図13：敷地権の要件の当てはめ表（固定配置） ----
ATEHAME = [
    ('敷地利用権か\n（区分所有法第2条第6項）', ('当たる', '一棟の建物の敷地（建物が\n所在する土地）の権利'), ('当たる', '一棟の建物は120番2の上\nにも建っている')),
    ('登記されたものか\n（不動産登記法第44条第1項第9号）', ('当たる', '登記された所有権'), ('当たらない', '使用貸借の権利は登記\nできない（同法第3条）')),
    ('数人で有する権利か\n（区分所有法第22条第1項本文）', ('当たらない', '乙川夏子1人の所有権\n（共有ではない）'), ('当たらない', '乙川夏子1人の権利')),
    ('専有部分の全部を所有する者の\n単独の権利か（同条第3項）', ('当たらない', 'Ⓑは甲野春男のもの'), ('当たらない', 'Ⓑは甲野春男のもの')),
]


def zu13():
    setup_font()
    fig = plt.figure(figsize=(18, 11), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('敷地権の定義の要件を本件に当てはめる（Ⓐ＝乙川夏子の専有部分の敷地利用権）', fontsize=22, weight='bold', y=0.965)
    ax = fig.add_axes([0.02, 0.07, 0.96, 0.82])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    cols = [(0, 34), (34, 67), (67, 100)]
    heads = ['敷地権の要件', '120番1\n（乙川夏子の所有権）', '120番2\n（無償で使う合意＝使用貸借）']
    top, hh, rh = 100, 12, 15
    for (x0, x1), h in zip(cols, heads):
        ax.add_patch(Rectangle((x0, top - hh), x1 - x0, hh, fc=GRAY, alpha=0.18, ec=BLACK, lw=1.6))
        ax.text((x0 + x1) / 2, top - hh / 2, h, ha='center', va='center', fontsize=16, weight='bold')
    for i, (req, c1, c2) in enumerate(ATEHAME):
        y1 = top - hh - i * rh
        y0 = y1 - rh
        ax.add_patch(Rectangle((0, y0), 34, rh, fc='white', ec=BLACK, lw=1.4))
        ax.text(17, (y0 + y1) / 2, req, ha='center', va='center', fontsize=15)
        for (x0, x1), (res, why) in zip(cols[1:], (c1, c2)):
            col = BLUE if res == '当たる' else RED
            ax.add_patch(Rectangle((x0, y0), x1 - x0, rh, fc=col, alpha=0.06, ec=BLACK, lw=1.4))
            ax.text(x0 + 2, (y0 + y1) / 2, res, ha='left', va='center', fontsize=17, color=col, weight='bold')
            ax.text(x0 + 12.5, (y0 + y1) / 2, why, ha='left', va='center', fontsize=14)
    y1 = top - hh - len(ATEHAME) * rh
    y0 = y1 - 14
    ax.add_patch(Rectangle((0, y0), 34, 14, fc=GRAY, alpha=0.18, ec=BLACK, lw=1.6))
    ax.text(17, (y0 + y1) / 2, '結論', ha='center', va='center', fontsize=17, weight='bold')
    for (x0, x1), txt in zip(cols[1:], ['分離処分が禁止されない\n→ 敷地権にならない', '登記できず、分離処分も禁止されない\n→ 敷地権にならない']):
        ax.add_patch(Rectangle((x0, y0), x1 - x0, 14, fc=RED, alpha=0.10, ec=BLACK, lw=1.6))
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, txt, ha='center', va='center', fontsize=16, color=RED, weight='bold')
    fig.text(0.5, 0.035, 'Ⓑ（甲野春男）も同じ形（120番2の所有権・120番1の無償の使用）で、敷地権にならない。'
             '答案用紙の敷地権の目的である土地の表示に斜線が印刷されているのはこのため',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'H24_dai22mon_zu13_atehame.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図13: 敷地権の要件の当てはめ表（固定配置）\n  →', path)


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
    print('重なり合計:', len(PROBLEMS))
