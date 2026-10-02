"""平成27年度 第22問（建物）の解説図9枚を、頂点座標から作図してPNGに書き出す。

`../prompt_H27_dai22mon_kaisetsuzu.md` の図1〜図9どおり。作図の共通部品は `tools/zu_helpers.py`。
建物の座標は (東, 南) で持ち（原点は一棟の建物の1階の北西の角の、壁〈柱〉の中心線の交点。各階はA点で重ねる）、
zu_helpers の (北, 東) には B() で変換する（北 ＝ −南）。
敷地は座標値一覧表がないので、〔見取図〕の距離と1階の寸法から組み立てた座標（西側の線を東0、南側の線を北0）を使う。
図3（建物図面）と図8（各階平面図）は、試験の答案用紙の第3欄の欄（家屋番号・建物の所在・申請人〈略〉・作成者〈略〉・縮尺）
の枠の中に描く。
実行: python3 note-articles-Kijyutsu/H27/Q22/zu/draw_H27_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []


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


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


# ---- 建物（別紙2の4の各階平面図。壁心＝軽量鉄骨の柱の中心、内法＝中心から0.075内側〈別紙2の3の（2）〉） ----
F1 = [(0, 0), (10.92, 0), (10.92, 1.82), (11.83, 1.82), (11.83, 6.37), (6.37, 6.37), (6.37, 7.28), (4.55, 7.28),
      (4.55, 8.19), (0, 8.19)]
GEN = rect(9.1, 0, 10.92, 1.82)                                     # 居宅部分専用玄関（壁心）
RO_WALL = [(0, 0), (9.1, 0), (9.1, 1.82), (11.83, 1.82), (11.83, 6.37), (6.37, 6.37), (6.37, 7.28), (4.55, 7.28),
           (4.55, 8.19), (0, 8.19)]                                 # （ロ）部分（壁心）
F2 = [(0, 0), (11.83, 0), (11.83, 6.37), (7.28, 6.37), (7.28, 7.28), (5.46, 7.28), (5.46, 8.19), (0, 8.19)]
F3 = [(0, 1.82), (2.73, 1.82), (2.73, 2.73), (8.19, 2.73), (8.19, 1.82), (11.83, 1.82), (11.83, 6.37), (7.28, 6.37),
      (7.28, 7.28), (0, 7.28)]
I1 = rect(9.175, 0.075, 10.845, 1.745)                              # （イ）1階部分（内法）
I2 = [(0.075, 0.075), (11.755, 0.075), (11.755, 6.295), (7.205, 6.295), (7.205, 7.205), (5.385, 7.205),
      (5.385, 8.115), (0.075, 8.115)]
I3 = [(0.075, 1.895), (2.655, 1.895), (2.655, 2.805), (8.265, 2.805), (8.265, 1.895), (11.755, 1.895),
      (11.755, 6.295), (7.205, 6.295), (7.205, 7.205), (0.075, 7.205)]
RO = [(0.075, 0.075), (9.025, 0.075), (9.025, 1.895), (11.755, 1.895), (11.755, 6.295), (6.295, 6.295),
      (6.295, 7.205), (4.475, 7.205), (4.475, 8.115), (0.075, 8.115)]
I2_R = [rect(0.075, 0.075, 11.755, 6.295), rect(0.075, 6.295, 7.205, 7.205), rect(0.075, 7.205, 5.385, 8.115)]
I3_R = [rect(0.075, 1.895, 2.655, 2.805), rect(8.265, 1.895, 11.755, 2.805), rect(0.075, 2.805, 11.755, 6.295),
        rect(0.075, 6.295, 7.205, 7.205)]
RO_R = [rect(0.075, 0.075, 9.025, 1.895), rect(0.075, 1.895, 11.755, 6.295), rect(0.075, 6.295, 6.295, 7.205),
        rect(0.075, 7.205, 4.475, 8.115)]

assert round(area_es(F1), 4) == 83.6381 and round(area_es(F2), 4) == 86.9505 and round(area_es(F3), 4) == 55.4827
assert round(area_es(GEN) + area_es(RO_WALL), 4) == 83.6381
assert round(area_es(I1), 4) == 2.7889
assert round(area_es(I2), 4) == 83.97 == round(sum(area_es(r) for r in I2_R), 4)
assert round(area_es(I3), 4) == 52.7752 == round(sum(area_es(r) for r in I3_R), 4)
assert round(area_es(RO), 4) == 77.3452 == round(sum(area_es(r) for r in RO_R), 4)

# ---- 敷地（X＝北、Y＝東。西側の線を Y＝0、南側の線を X＝0） ----
EW, NS = round(2.00 + 10.92 + 5.00, 2), round(2.50 + 6.37 + 4.50, 2)
SITE = [complex(0, 0), complex(0, EW), complex(NS, EW), complex(NS, 0)]
assert (EW, NS) == (17.92, 13.37) and round(area(SITE), 4) == 239.5904


def to_site(p):
    """建物の点（B()で作った複素数）を敷地の座標へ（北の外壁が北側の筆界から2.50、西の外壁が西側の筆界から2.00）。"""
    return complex(NS - 2.50 + p.real, 2.00 + p.imag)


def dims(z, pts, labels, fs=14, ref=None, color=BLACK):
    c = ref or centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs, color=color)


def pt_mark(z, p, name, away):
    z.point(p, size=8)
    z.point_label(p, name, away=away, fs=14)


def dim_line(z, p, q, text, dirs):
    z.ax.annotate('', xy=xy(q), xytext=xy(p),
                  arrowprops=dict(arrowstyle='<->', lw=1.4, color=BLACK, shrinkA=0, shrinkB=0), zorder=4)
    z.segments.append((xy(p), xy(q)))
    return z.callout((p + q) / 2, text, dirs=dirs, fs=15, dists=(40, 55, 70))


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.01
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


INK = '#1a3a8f'   # 記入（濃い青）


# ---- 図1：区分の全体図 ----
def zu01():
    fig, axes = new_figure('区分の全体図：階層的な区分と、分離処分可能規約（問1）',
                           '（イ）部分＝1階の居宅部分専用玄関＋2階＋3階（5番27の1 居宅）、（ロ）部分＝1階の残り（5番27の2 共同住宅）。\n'
                           '公正証書で分離処分可能規約を設定するので、本件土地の所有権は敷地権にならず、乙山一郎の名義のまま残る',
                           w=18, h=8.5, ncols=3)
    fig.subplots_adjust(top=0.84, bottom=0.17)
    zs = []
    for k, ax in enumerate(axes):
        z = Zu(ax, fontsize=12)
        ax.set_title(['1階', '2階', '3階'][k], fontsize=17, weight='bold')
        fit(ax, P(F2), margin=0.06, extra=[xy(B(-1.0, -3.2)), xy(B(12.8, 11.4))], pad_aspect=True)
        if k == 0:
            z.poly(P(RO_WALL), color=BLACK, lw=2, fill=GREEN, alpha=0.25)
            z.poly(P(GEN), color=BLACK, lw=2, fill=BLUE, alpha=0.40)
            z.line(B(4.55, 0), B(4.55, 7.28), color=GRAY, lw=1.0, ls='--', check=False)
            z.free_text(B(2.3, 4.0), '102号室', fs=12, color=GREEN)
            z.free_text(B(7.6, 4.0), '101号室', fs=12, color=GREEN)
            z.callout(B(10.0, 0.9), '（イ）の玄関', dirs=(90, 110, 70), fs=12, color=BLUE, dists=(30, 45, 60))
            z.free_text(B(5.9, 9.7), '（ロ）共同住宅 → 会社へ譲渡', fs=13, weight='bold', color=GREEN)
        else:
            z.poly(P(F2 if k == 1 else F3), color=BLACK, lw=2, fill=BLUE, alpha=0.30)
            z.free_text(B(5.9, 4.3), '（イ）居宅', fs=15, weight='bold', color=BLUE)
        zs.append(z)
    zs[2].north_arrow()
    save(fig, zs, 'H27_dai22mon_zu01_kubun_zentaizu')


# ---- 図2：敷地の辺長確認図 ----
def zu02():
    fig, axes = new_figure('本件土地（5番27）の辺長確認図（作図チェック用）',
                           '東西 2.00＋10.92＋5.00＝17.92、南北 2.50＋6.37＋4.50＝13.37。17.92×13.37＝239.5904→239.59㎡（登記記録の地積と一致）。'
                           '辺長は建物図面には書かない', w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    fit(ax, SITE, margin=0.10, extra=[(-3.8, -3.2), (22.0, 16.8)], pad_aspect=True)
    z.north_arrow()
    z.poly(SITE, color=BLACK, lw=2.4, fill=BLUE, alpha=0.08)
    z.poly([to_site(p) for p in P(F1)], color=GRAY, lw=1.2, check=False)
    dims(z, SITE, ['17.92', '13.37', '17.92', '13.37'], fs=16, ref=complex(6.7, 9.0))
    z.free_text(complex(-2.3, 8.96), '（2.00＋10.92＋5.00）', fs=13, color=GRAY)
    z.free_text(complex(6.685, 20.6), '（2.50＋6.37＋4.50）', fs=13, color=GRAY, rotation=90)
    z.free_text(complex(6.2, 8.2), '本件土地（5－27）\n239.59㎡', fs=16)
    z.free_text(complex(15.0, 8.96), '5－26', fs=14, color=GRAY)
    z.free_text(complex(6.685, -2.0), '5－11', fs=14, color=GRAY)
    z.free_text(complex(-1.4, 3.5), '5－28', fs=14, color=GRAY)
    z.free_text(complex(15.0, -2.0), '5－10', fs=14, color=GRAY)
    z.free_text(complex(-1.7, -2.0), '5－12', fs=14, color=GRAY)
    z.free_text(complex(10.5, 19.4), '道路\n（42）', fs=14, color=GRAY)
    save(fig, [z], 'H27_dai22mon_zu02_shikichi_henchou')


# ---- 図3：建物図面（イ）の完成形（答案用紙の第3欄の形） ----
def zu03():
    setup_font()
    fig = plt.figure(figsize=(16, 14), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面（イ）の完成形（答案用紙の第3欄・縮尺1/500で描く内容）', fontsize=22, weight='bold', y=0.985)
    # 答案用紙の欄
    cell(fig, 0.06, 0.885, 0.20, 0.935, '家屋番号', fs=15)
    cell(fig, 0.20, 0.885, 0.46, 0.935, 'B町二丁目5番27の1', fs=16, color=INK)
    fig.text(0.70, 0.910, '建　物　図　面　（イ）', ha='center', va='center', fontsize=20)
    cell(fig, 0.06, 0.835, 0.20, 0.885, '建物の所在', fs=15)
    cell(fig, 0.20, 0.835, 0.94, 0.885, 'A市B町二丁目5番地27', fs=16, ha='left', color=INK)
    cell(fig, 0.06, 0.085, 0.94, 0.835, lw=1.8)
    cell(fig, 0.06, 0.035, 0.20, 0.085, '申　請　人', fs=15)
    cell(fig, 0.20, 0.035, 0.74, 0.085, '（略）', fs=15)
    cell(fig, 0.74, 0.035, 0.83, 0.085, '縮尺', fs=15)
    cell(fig, 0.83, 0.035, 0.94, 0.085, '1/500', fs=15)
    ax = fig.add_axes([0.08, 0.10, 0.84, 0.72])
    z = Zu(ax, fontsize=14)
    fit(ax, SITE, margin=0.10, extra=[(-4.0, -3.8), (22.8, 17.0)], pad_aspect=True)
    z.north_arrow()
    z.poly(SITE, color=BLACK, lw=2.2)
    z.line(complex(NS, 0), complex(NS + 2.2, 0), color=BLACK, lw=1.6)        # 西側の線を北へ
    z.line(complex(0, 0), complex(-2.2, 0), color=BLACK, lw=1.6)             # 西側の線を南へ
    z.line(complex(NS, 0), complex(NS, -2.6), color=BLACK, lw=1.6)           # 北側の線を西へ
    z.line(complex(0, 0), complex(0, -2.6), color=BLACK, lw=1.6)             # 南側の線を西へ
    z.line(complex(-2.2, EW + 3.0), complex(NS + 2.2, EW + 3.0), color=BLACK, lw=1.6)   # 道路の向こう側の線
    f1 = [to_site(p) for p in P(F1)]
    gen = [to_site(p) for p in P(GEN)]
    z.poly(f1, color=BLACK, lw=1.6, ls='--')
    z.poly(gen, color=BLACK, lw=2.8)
    assert round(area(f1), 4) == 83.6381 and round(area(gen), 4) == 3.3124
    assert round(NS - max(p.real for p in f1), 2) == 2.50 and round(min(p.imag for p in f1), 2) == 2.00
    assert round(EW - max(p.imag for p in gen), 2) == 5.00 and round(min(p.real for p in f1), 2) == 2.68
    dim_line(z, complex(NS, 2.0), complex(NS - 2.5, 2.0), '2.50', dirs=(200, 215, 185, 160))
    dim_line(z, complex(NS, 12.92), complex(NS - 2.5, 12.92), '2.50', dirs=(160, 145, 175, 130))
    dim_line(z, complex(NS - 2.5, 12.92), complex(NS - 2.5, EW), '5.00', dirs=(-60, -75, -45, -90))
    z.free_text(complex(1.25, 10.8), '建物の存する部分　1階、2階、3階', fs=15)
    z.callout(complex(9.96, 12.01), '（イ）', dirs=(-120, -135, -105), fs=15, dists=(45, 60, 75))
    z.free_text(complex(6.0, 15.9), '5－27', fs=16)
    z.free_text(complex(15.0, 8.96), '5－26', fs=15)
    z.free_text(complex(6.685, -1.3), '5－11', fs=15)
    z.free_text(complex(-1.3, 8.96), '5－28', fs=15)
    z.free_text(complex(15.0, -1.4), '5－10', fs=15)
    z.free_text(complex(-1.4, -1.4), '5－12', fs=15)
    z.free_text(complex(3.5, 19.4), '道路\n42', fs=15)
    z.free_text(complex(-3.2, 16.3), '（単位：m）', fs=13)
    save(fig, [z], 'H27_dai22mon_zu03_tatemono_zumen')


# ---- 図4：（イ）部分2階の求積図 ----
def zu04():
    fig, axes = new_figure('（イ）部分2階部分の床面積求積図（内法）',
                           '11.68×6.22＋7.13×0.91＋5.31×0.91＝83.97㎡。段差0.91・1.82・0.91とB点からA点の4.55は壁心と同じ。'
                           '点線は1階の位置（居宅部分専用玄関）', w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    fit(ax, P(I2), margin=0.20, extra=[xy(B(5.9, 11.0))], pad_aspect=True)
    z.north_arrow()
    for r, c in zip(I2_R, [BLUE, ORANGE, PURPLE]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.25, check=False)
    z.line(B(0.075, 6.295), B(7.205, 6.295), color=GRAY, lw=1.0, ls='--')
    z.line(B(0.075, 7.205), B(5.385, 7.205), color=GRAY, lw=1.0, ls='--')
    z.poly(P(I2), color=BLACK, lw=2.4)
    z.poly(P(I1), color=BLACK, lw=1.4, ls='--')
    pt_mark(z, B(11.755, 6.295), 'A点', centroid(P(I2)))
    pt_mark(z, B(7.205, 6.295), 'B点', B(6.0, 3.0))
    dims(z, P(I2), ['11.68', '6.22', '4.55', '0.91', '1.82', '0.91', '5.31', '8.04'], fs=15)
    z.free_text(B(5.9, 3.6), '11.68×6.22', fs=16)
    z.free_text(B(3.6, 6.75), '7.13×0.91', fs=13)
    z.free_text(B(2.7, 7.66), '5.31×0.91', fs=13)
    z.callout(B(10.0, 0.9), '1階の位置（点線）', dirs=(-100, -120, -80), fs=13, dists=(60, 80, 100))
    z.free_text(B(5.9, 10.4), '2階部分　床面積：83.97㎡', fs=17, weight='bold')
    save(fig, [z], 'H27_dai22mon_zu04_2kai_kyuuseki')


# ---- 図5：3階の誤り比較図（欠けの幅） ----
def zu05():
    fig, axes = new_figure('3階部分の内法：欠けの幅は変わらない？広がる？',
                           '内側の線は部屋の側にずれる。欠けをはさむ2つの壁は、欠けから離れる向きに0.075ずつずれるので、欠けの幅は5.46＋0.15＝5.61に広がる',
                           w=18, h=8, ncols=3, width_ratios=[1, 0.9, 1])
    fig.subplots_adjust(top=0.84)
    # 誤り
    z = Zu(axes[0], fontsize=13)
    axes[0].set_title('誤り：欠けの幅を5.46のまま（藍子）', fontsize=16, weight='bold', color=RED)
    fit(axes[0], P(F3), margin=0.18, extra=[xy(B(6, -0.6)), xy(B(6, 9.6))], pad_aspect=True)
    z.poly(P(F3), color=GRAY, lw=1.0, ls=':', check=False)
    wrong = [(0.075, 1.895), (2.655, 1.895), (2.655, 2.805), (8.115, 2.805), (8.115, 1.895), (11.605, 1.895)]
    right_side = [(11.755, 1.895), (11.755, 6.295), (7.205, 6.295), (7.205, 7.205), (0.075, 7.205), (0.075, 1.895)]
    z.poly(P(wrong), color=RED, lw=2.4, closed=False)
    z.poly(P(right_side), color=BLACK, lw=2.0, closed=False)
    z.edge_label(B(0.075, 1.895), B(2.655, 1.895), '2.58', B(6, 5), fs=13)
    z.edge_label(B(2.655, 2.805), B(8.115, 2.805), '5.46', B(6, 1.0), fs=14, color=RED, outward=False)
    z.edge_label(B(8.115, 1.895), B(11.605, 1.895), '3.49', B(6, 5), fs=13)
    z.edge_label(B(0.075, 7.205), B(7.205, 7.205), '7.13', B(6, 3), fs=13)
    z.edge_label(B(7.205, 6.295), B(11.755, 6.295), '4.55', B(6, 3), fs=13)
    z.callout(B(11.68, 1.895), '0.15足りない', dirs=(60, 80, 40), fs=13, color=RED, dists=(35, 50, 65))
    z.free_text(B(5.9, 4.6), '北：2.58＋5.46＋3.49＝11.53\n南：7.13＋4.55＝11.68', fs=13, color=RED)
    # 拡大（欠けの両側の壁）。壁の厚さを誇張した模式図（d＝壁の中心線から内壁の面まで。実際は0.075）
    z2 = Zu(axes[1], fontsize=12)
    axes[1].set_title('北側の欠け（模式図・壁の厚さは誇張）', fontsize=15, weight='bold')
    fit(axes[1], P(rect(-0.3, -0.6, 8.3, 5.4)), margin=0.02, pad_aspect=True)
    d = 0.45
    cl = [(0, 1), (1.6, 1), (1.6, 3), (6.4, 3), (6.4, 1), (8, 1)]
    inner = [(0, 1 + d), (1.6 - d, 1 + d), (1.6 - d, 3 + d), (6.4 + d, 3 + d), (6.4 + d, 1 + d), (8, 1 + d)]
    outer = [(0, 1 - d), (1.6 + d, 1 - d), (1.6 + d, 3 - d), (6.4 - d, 3 - d), (6.4 - d, 1 - d), (8, 1 - d)]
    band = inner + outer[::-1]
    z2.poly(P(band), color=GRAY, lw=0, fill=GRAY, alpha=0.30, check=False)
    axes[1].add_patch(MPoly([xy(p) for p in P(band)], closed=True, fill=False, hatch='///', edgecolor=GRAY, lw=0, zorder=1))
    z2.poly(P(cl), color=BLACK, lw=1.4, ls='-.', closed=False)
    z2.poly(P(inner), color=GREEN, lw=3.2, closed=False)
    for e0, e1 in [(1.6, 1.6 - d), (6.4, 6.4 + d)]:
        axes[1].annotate('', xy=xy(B(e1, 2.0)), xytext=xy(B(e0, 2.0)),
                         arrowprops=dict(arrowstyle='-|>', lw=1.8, color=RED, shrinkA=0, shrinkB=0, mutation_scale=14))
        z2.segments.append((xy(B(e0, 2.0)), xy(B(e1, 2.0))))
    for y_, txt, col in [(2.45, '壁心 5.46', BLACK), (4.25, '内法 5.61', GREEN)]:
        e0, e1 = (1.6, 6.4) if col == BLACK else (1.6 - d, 6.4 + d)
        axes[1].annotate('', xy=xy(B(e1, y_)), xytext=xy(B(e0, y_)),
                         arrowprops=dict(arrowstyle='<->', lw=1.3, color=col, shrinkA=0, shrinkB=0))
        z2.segments.append((xy(B(e0, y_)), xy(B(e1, y_))))
        z2.free_text(B(4.0, y_), txt, fs=14, color=col, weight='bold', offsets=((0, 11), (0, -11)))
    z2.callout(B(1.6 - d / 2, 2.0), '0.075', dirs=(200, 180, 220), fs=12, color=RED, dists=(30, 45))
    z2.callout(B(6.4 + d / 2, 2.0), '0.075', dirs=(-20, 0, -40), fs=12, color=RED, dists=(30, 45))
    z2.free_text(B(4.0, 0.9), '欠け（建物の外）', fs=13, color=GRAY)
    z2.free_text(B(0.5, 3.4), '部屋', fs=13, color=GRAY)
    z2.free_text(B(7.5, 3.4), '部屋', fs=13, color=GRAY)
    z2.callout(B(7.4, 1.0), '壁の中心線', dirs=(90, 70, 110), fs=12, dists=(30, 45))
    z2.callout(B(4.0, 3 + d), '内壁の面（内法）', dirs=(-45, -30, -60, -135), fs=12, color=GREEN, dists=(55, 70, 85))
    # 正解
    z3 = Zu(axes[2], fontsize=13)
    axes[2].set_title('正解：欠けの幅は5.61に広がる', fontsize=16, weight='bold', color=GREEN)
    fit(axes[2], P(F3), margin=0.18, extra=[xy(B(6, -0.6)), xy(B(6, 9.6))], pad_aspect=True)
    z3.poly(P(F3), color=GRAY, lw=1.0, ls=':', check=False)
    z3.poly(P(I3), color=GREEN, lw=2.4, fill=GREEN, alpha=0.20)
    z3.edge_label(B(0.075, 1.895), B(2.655, 1.895), '2.58', B(6, 5), fs=13)
    z3.edge_label(B(2.655, 2.805), B(8.265, 2.805), '5.61', B(6, 1.0), fs=14, color=GREEN, outward=False)
    z3.edge_label(B(8.265, 1.895), B(11.755, 1.895), '3.49', B(6, 5), fs=13)
    z3.edge_label(B(0.075, 7.205), B(7.205, 7.205), '7.13', B(6, 3), fs=13)
    z3.edge_label(B(7.205, 6.295), B(11.755, 6.295), '4.55', B(6, 3), fs=13)
    z3.free_text(B(5.9, 4.6), '北：2.58＋5.61＋3.49＝11.68\n南：7.13＋4.55＝11.68', fs=13, color=GREEN)
    save(fig, [z, z2, z3], 'H27_dai22mon_zu05_3kai_ayamari_hikaku')


# ---- 図6：（イ）部分3階の求積図 ----
def zu06():
    fig, axes = new_figure('（イ）部分3階部分の床面積求積図（内法）',
                           '2.58×0.91＋3.49×0.91＋11.68×3.49＋7.13×0.91＝52.77㎡。欠けの幅は5.61。点線は1階の位置（3階の外形の北に出る）',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    fit(ax, P(I3) + P(I1), margin=0.18, extra=[xy(B(5.9, 10.2))], pad_aspect=True)
    z.north_arrow()
    for r, c in zip(I3_R, [ORANGE, PURPLE, BLUE, GREEN]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.25, check=False)
    z.line(B(0.075, 2.805), B(2.655, 2.805), color=GRAY, lw=1.0, ls='--')
    z.line(B(8.265, 2.805), B(11.755, 2.805), color=GRAY, lw=1.0, ls='--')
    z.line(B(0.075, 6.295), B(7.205, 6.295), color=GRAY, lw=1.0, ls='--')
    z.poly(P(I3), color=BLACK, lw=2.4)
    z.poly(P(I1), color=BLACK, lw=1.4, ls='--')
    pt_mark(z, B(11.755, 6.295), 'A点', centroid(P(I3)))
    pt_mark(z, B(7.205, 6.295), 'B点', B(6.0, 4.0))
    dims(z, P(I3), ['2.58', '0.91', '', '0.91', '', '4.40', '4.55', '0.91', '7.13', '5.31'], fs=15)
    z.callout(B(11.3, 1.895), '3.49', dirs=(30, 15, 45), fs=15, dists=(40, 55, 70))
    z.edge_label(B(2.655, 2.805), B(8.265, 2.805), '5.61', B(5.46, 1.0), fs=16, color=RED, outward=False)
    z.free_text(B(1.365, 2.35), '2.58×0.91', fs=11)
    z.free_text(B(10.01, 2.35), '3.49×0.91', fs=11)
    z.free_text(B(5.9, 4.55), '11.68×3.49', fs=16)
    z.free_text(B(3.64, 6.75), '7.13×0.91', fs=13)
    z.callout(B(10.0, 0.9), '1階の位置（点線）', dirs=(170, 190, 150), fs=13, dists=(60, 80, 100))
    z.free_text(B(5.9, 9.3), '3階部分　床面積：52.77㎡', fs=17, weight='bold')
    save(fig, [z], 'H27_dai22mon_zu06_3kai_kyuuseki')


# ---- 図7：1階の求積図（（イ）部分の玄関と（ロ）部分） ----
def zu07():
    fig, axes = new_figure('1階の床面積求積図（内法）：（イ）部分の玄関と（ロ）部分',
                           '（イ）部分1階部分 1.67×1.67＝2.78㎡。（ロ）部分1階部分 8.95×1.82＋11.68×4.40＋6.22×0.91＋4.40×0.91＝77.34㎡'
                           '（101号室と102号室の間の仕切りは引かない）', w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    fit(ax, P(F1), margin=0.20, extra=[xy(B(5.9, 10.9))], pad_aspect=True)
    z.north_arrow()
    z.poly(P(F1), color=GRAY, lw=1.0, ls=':', check=False)
    for r, c in zip(RO_R, [GREEN, ORANGE, PURPLE, RED]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.22, check=False)
    z.line(B(0.075, 1.895), B(9.025, 1.895), color=GRAY, lw=1.0, ls='--')
    z.line(B(0.075, 6.295), B(6.295, 6.295), color=GRAY, lw=1.0, ls='--')
    z.line(B(0.075, 7.205), B(4.475, 7.205), color=GRAY, lw=1.0, ls='--')
    z.line(B(4.55, 0.075), B(4.55, 8.115), color=GREEN, lw=1.0, ls=(0, (1, 3)), check=False)   # 101・102の仕切り（引かない）
    z.poly(P(RO), color=BLACK, lw=2.4)
    z.poly(P(I1), color=BLUE, lw=2.4, fill=BLUE, alpha=0.35)
    z.edge_label(B(9.025, 0.075), B(9.025, 1.895), '1.82', centroid(P(RO)), fs=15, outward=False)
    dims(z, P(RO), ['8.95', '', '', '4.40', '5.46', '0.91', '1.82', '0.91', '4.40', '8.04'], fs=15)
    z.callout(B(10.39, 1.895), '2.73', dirs=(-30, -50, -15), fs=15, dists=(35, 50, 65))
    z.free_text(B(4.55, 0.985), '8.95×1.82', fs=14)
    z.free_text(B(5.9, 4.1), '11.68×4.40', fs=16)
    z.free_text(B(3.2, 6.75), '6.22×0.91', fs=13)
    z.free_text(B(2.3, 7.66), '4.40×0.91', fs=13)
    z.callout(B(10.01, 0.91), '（イ）1.67×1.67', dirs=(90, 70, 110), fs=14, color=BLUE, dists=(40, 55, 70))
    z.free_text(B(5.9, 10.2), '（ロ）部分1階部分：77.34㎡　（イ）部分1階部分：2.78㎡', fs=16, weight='bold')
    save(fig, [z], 'H27_dai22mon_zu07_1kai_kyuuseki')


# ---- 図8：各階平面図（イ）の完成形（答案用紙の第3欄の形） ----
def zu08():
    setup_font()
    fig = plt.figure(figsize=(18, 10), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図（イ）の完成形（答案用紙の第3欄・縮尺1/250で描く内容）', fontsize=22, weight='bold', y=0.975)
    fig.text(0.5, 0.905, '各　階　平　面　図', ha='center', va='center', fontsize=20)
    cell(fig, 0.04, 0.13, 0.96, 0.88, lw=1.8)
    cell(fig, 0.04, 0.06, 0.14, 0.13, '作　成　者', fs=15)
    cell(fig, 0.14, 0.06, 0.78, 0.13, '（略）　　　　　　　　　　　　（平成何年何月何日作成）', fs=15)
    cell(fig, 0.78, 0.06, 0.86, 0.13, '縮尺', fs=15)
    cell(fig, 0.86, 0.06, 0.96, 0.13, '1/250', fs=15)
    fig.text(0.5, 0.025, '内法の寸法で「1階部分」「2階部分」「3階部分」を書き分け、1階以外の階には1階の位置を点線で示す。'
             '問3のなお書きどおり、求積方法と床面積は書かない', ha='center', va='center', fontsize=14)
    axes = [fig.add_axes([0.05, 0.16, 0.16, 0.64]), fig.add_axes([0.23, 0.16, 0.35, 0.64]),
            fig.add_axes([0.60, 0.16, 0.35, 0.64])]
    zs = []
    z = Zu(axes[0], fontsize=13)
    axes[0].set_title('1階部分', fontsize=17, weight='bold')
    fit(axes[0], P(I1), margin=0.9, pad_aspect=True)
    z.poly(P(I1), color=BLACK, lw=2.4)
    dims(z, P(I1), ['1.67', '1.67', '1.67', '1.67'], fs=13)
    zs.append(z)
    for k, (pts, labels, name) in enumerate([
            (I2, ['11.68', '6.22', '4.55', '0.91', '1.82', '0.91', '5.31', '8.04'], '2階部分'),
            (I3, ['2.58', '0.91', '5.61', '0.91', '3.49', '4.40', '4.55', '0.91', '7.13', '5.31'], '3階部分')]):
        ax = axes[k + 1]
        z = Zu(ax, fontsize=13)
        ax.set_title(name, fontsize=17, weight='bold')
        fit(ax, P(I2), margin=0.18, pad_aspect=True)
        z.poly(P(pts), color=BLACK, lw=2.4)
        z.poly(P(I1), color=BLACK, lw=1.3, ls='--')
        ref = B(5.9, 4.5)
        for i, t in enumerate(labels):
            if name == '3階部分' and i == 4:
                z.callout(B(11.3, 1.895), t, dirs=(30, 15, 45), fs=13, dists=(35, 50, 65))
                continue
            z.edge_label(P(pts)[i], P(pts)[(i + 1) % len(pts)], t, ref, fs=13,
                         outward=not (name == '3階部分' and i == 2))
        zs.append(z)
    zs[2].north_arrow()
    save(fig, zs, 'H27_dai22mon_zu08_kakukai_heimenzu')


# ---- 図9：本番で解く順番 ----
def zu09():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    setup_font()
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　依頼人の希望から問1・問2の筋を先に決める', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '前文・問1〜3・\n問題文の注', '何を答えるか\n先に読む', BLUE),
        ('②', '事実関係4で\n筋を決める', '規約証明情報・\n記載不要をメモ', BLUE),
        ('③', '床面積の\nいらない欄', '目的・添付情報・\n1行目・種類・原因', BLUE),
        ('④', '内法の\n累計メモ', '北西の角から\n東へ・南へ', RED),
        ('⑤', '各階平面図\n→建物図面', '第3欄の左、\n右の順', RED),
        ('⑥', '床面積を\n申請書へ', '2.78・83.97・\n52.77・77.34', GREEN),
        ('⑦', '第1欄の文章\nと見直し', '問1と問2が\n食い違わないか', GRAY),
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
    ax.text(1 + 1.5 * (w + gap) - gap / 2, 76, '求積をしなくても書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 3 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 4 * (w + gap) - gap / 2, 76, 'いちばん時間を食う（欠けの幅に注意）', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 5 * (w + gap) - gap, 72), xytext=(1 + 3 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '「土地は自分の名義のまま」の一言で、問1（公正証書の分離処分可能規約）、添付情報の規約証明情報、敷地権の表示の「記載不要」が決まる。\n'
             '第1欄の文章は、結論（規約の設定）と理由（区分すると敷地権になる）の2点が入れば足りる。練りすぎて作図の時間を削らない',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'H27_dai22mon_zu09_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図9: 解く順番（固定配置）\n  →', path)


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
    print('重なり合計:', len(PROBLEMS))
