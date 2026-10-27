"""平成20年度 第22問（建物）の解説図を、頂点座標・固定配置から作図してPNGに書き出す。

作図の共通部品は `tools/zu_helpers.py`。建物の座標は (東, 南) で持ち（原点は一棟の建物の北西の角の、壁の中心線の交点）、
zu_helpers の (北, 東) には B() で変換する（北 ＝ −南）。内法の図は、その区分建物の北西の角の内側の線を原点にした座標で描く。
敷地は座標値一覧表がないので、配置図の距離（外壁まで。図の（注）3）と壁厚15cm（図の（注）2）から組み立てた座標を使う。
建物図面（図13）と各階平面図（図20）は、試験の答案用紙（その3）（touan_youshi/H20_dai22mon_touan_youshi_p3.png。A3横 420mm × 297mm）の
罫線から測った mm の位置に、縮尺1/500（1m ＝ 2mm）・1/250（1m ＝ 4mm）の実際の大きさで描く。
図の画像の中には図番を入れない（番号はPNGファイル名とプロンプトの一覧だけ）。

実行: python3 note-articles-Kijyutsu/H20/Q22/zu/draw_H20_dai22mon_kaisetsuzu.py [出力フォルダ [図の名前の一部 ...]]
      図の名前の一部（例 zu08）を指定すると、その図だけ書き出す。指定がなければ全部（作成済みの図もバイトが変わるので、
      照らし直しでは描き直す図だけを指定して別のフォルダに出し、必要なものだけ写すこと）。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN,  # noqa: E402
                        PURPLE)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
ONLY = sys.argv[2:]
PROBLEMS = []
W = 0.075   # 壁厚15cmの半分（図の（注）2）
INK = '#1a3a8f'   # 記入（濃い青）
LIGHT = '#dddddd'


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


def trunc2(v):
    return int(v * 100 + 1e-9) / 100


def hatch(ax, pts, color=GRAY):
    ax.add_patch(MPoly([xy(p) for p in pts], closed=True, fill=False, hatch='///', edgecolor=color, lw=0, zorder=1))


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def notch(z, x0, x1, top, bot, wtxt, fs=14, down=(70, 85, 100), wdirs=(-125, -140, -110)):
    """PSの欠け（幅 x0〜x1、奥行き top〜bot）の短い3辺の長さを、引き出し線付きで欠けの外（南）に置く。"""
    z.callout(B(x0, (top + bot) / 2), '0.50', dirs=wdirs, fs=fs, dists=(45, 60, 75))
    z.callout(B((x0 + x1) / 2, top), wtxt, dirs=(-90, -100, -80), fs=fs, dists=down)
    z.callout(B(x1, (top + bot) / 2), '0.50', dirs=(-55, -40, -70), fs=fs, dists=(45, 60, 75))


def dims(z, pts, labels, fs=14, ref=None, outward=True):
    c = ref or centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs, outward=outward)


# ---- 壁心（平面図の寸法。図の（注）1）----
F1 = [(0, 0), (12, 0), (12, 10), (5.5, 10), (5.5, 12), (0, 12)]                    # 一棟の1階・2階の外形
F3 = rect(0, 0, 12, 10)                                                             # 一棟の3階の外形
PS_W, PS_E = rect(5.5, 9.5, 6, 10), rect(6, 9.5, 6.5, 10)                          # PS（共用部分。図の（注）4）
ROUKA = rect(5.5, 10, 12, 12)                                                       # 1階・2階の開放廊下（床面積に入らない）
ROUKA3 = rect(0, 10, 12, 12)                                                        # 3階の開放廊下・開放バルコニー
RO2_WALL = [(0, 0), (6, 0), (6, 9.5), (5.5, 9.5), (5.5, 12), (0, 12)]              # （ロ）2階部分（2階の西の部屋）
I2_WALL = [(6, 0), (12, 0), (12, 10), (6.5, 10), (6.5, 9.5), (6, 9.5)]             # （イ）2階部分（2階の東の住戸）
RO3_WALL = [(0, 0), (12, 0), (12, 10), (6.5, 10), (6.5, 9.5), (5.5, 9.5), (5.5, 10), (0, 10)]
I1_WALL = [(0, 0), (12, 0), (12, 10), (6.5, 10), (6.5, 9.5), (5.5, 9.5), (5.5, 12), (0, 12)]
assert area_es(F1) == 131.00 and area_es(F3) == 120.00                               # 登記記録の1階・2階・3階と一致
assert round(12 * 9.5 + 12 * 0.5 + 5.5 * 2.0, 2) == 131.00 and 12 * 12 - area_es(ROUKA) == 131.00
assert round(area_es(RO2_WALL) + area_es(I2_WALL) + area_es(PS_W) + area_es(PS_E), 2) == 131.00
assert round(area_es(RO3_WALL) + area_es(PS_W) + area_es(PS_E), 2) == 120.00
assert round(area_es(F1) - area_es(PS_W) - area_es(PS_E), 2) == 130.50

# ---- 内法（壁の中心線から0.075内側。原点は各区分建物の北西の角の内側の線）----
RO2 = [(0, 0), (5.85, 0), (5.85, 9.35), (5.35, 9.35), (5.35, 11.85), (0, 11.85)]
RO3 = [(0, 0), (11.85, 0), (11.85, 9.85), (6.50, 9.85), (6.50, 9.35), (5.35, 9.35), (5.35, 9.85), (0, 9.85)]
I1 = [(0, 0), (11.85, 0), (11.85, 9.85), (6.50, 9.85), (6.50, 9.35), (5.35, 9.35), (5.35, 11.85), (0, 11.85)]
I2 = [(0, 0), (5.85, 0), (5.85, 9.85), (0.50, 9.85), (0.50, 9.35), (0, 9.35)]
RO2_S = [rect(0, 0, 5.35, 11.85), rect(5.35, 0, 5.85, 9.35)]
RO3_S = [rect(0, 0, 5.35, 9.85), rect(5.35, 0, 6.50, 9.35), rect(6.50, 0, 11.85, 9.85)]
I1_S = [rect(0, 0, 5.35, 11.85), rect(5.35, 0, 6.50, 9.35), rect(6.50, 0, 11.85, 9.85)]
I2_S = [rect(0, 0, 0.50, 9.35), rect(0.50, 0, 5.85, 9.85)]
assert round(area_es(RO2), 4) == 68.0725 == round(sum(area_es(r) for r in RO2_S), 4) and trunc2(68.0725) == 68.07
assert round(area_es(RO3), 4) == 116.1475 == round(sum(area_es(r) for r in RO3_S), 4) and trunc2(116.1475) == 116.14
assert round(area_es(I1), 4) == 126.8475 == round(sum(area_es(r) for r in I1_S), 4) and trunc2(126.8475) == 126.84
assert round(area_es(I2), 4) == 57.3725 == round(sum(area_es(r) for r in I2_S), 4) and trunc2(57.3725) == 57.37
assert round(68.07 + 116.14, 2) == 184.21 == round(126.84 + 57.37, 2)
# 誤り：PSの欠けを1.00のまま／（イ）の1階を住戸ごとに測る
assert round(11.85 * 9.85 - 1.00 * 0.50, 4) == 116.2225 and round(5.35 + 1.00 + 5.35, 2) == 11.70
assert round(68.07 + 57.37, 2) == 125.44 and round(125.44 + 57.37, 2) == 182.81

# ---- 敷地（配置図の距離は外壁から。外壁は壁の中心線より0.075外側）----
SLOPE = 1.00 / 12.15                        # 北の筆界：外壁から外壁までの12.15で1.00北へ上がる
E_W, E_E, S_S = -2.075, 15.075, 16.075       # 西の筆界・東の筆界（道路との境）・南の筆界（建物の座標）


def north_s(e):
    """北の筆界の南方向の座標（北西の角の外壁の位置で北の外壁から2.00、北東の角の位置で3.00）。"""
    return -2.075 - (e + 0.075) * SLOPE


SITE_ES = [(E_W, north_s(E_W)), (E_E, north_s(E_E)), (E_E, S_S), (E_W, S_S)]
SITE = P(SITE_ES)
assert round(north_s(12.075), 3) == -3.075 and round(north_s(-0.075), 3) == -2.075
assert trunc2(area(SITE)) == 320.55 and round(area(SITE), 4) == 320.5533
assert round(E_E - E_W, 2) == 17.15 and round(S_S - north_s(E_W), 2) == 17.99 and round(S_S - north_s(E_E), 2) == 19.40
assert round(abs(SITE[1] - SITE[0]), 2) == 17.21
assert round(12.075 + 4.00, 3) == S_S == round(10.075 + 6.00, 3)   # 南の筆界は真東西
# 壁の厚みを落として距離を壁の中心線から測ると（東西17.00）
S_WRONG = ((18 - 2 / 12) + (19 + 3 / 12)) / 2 * 17.00
assert trunc2(S_WRONG) == 315.20 and round(S_WRONG, 1) == 315.2

OUTER = [(-W, -W), (12 + W, -W), (12 + W, 10 + W), (5.5 + W, 10 + W), (5.5 + W, 12 + W), (-W, 12 + W)]   # 一棟1階の外壁の外形


def dim_line(z, p, q, text, dirs, fs=15):
    z.ax.annotate('', xy=xy(q), xytext=xy(p),
                  arrowprops=dict(arrowstyle='<->', lw=1.4, color=BLACK, shrinkA=0, shrinkB=0), zorder=4)
    z.segments.append((xy(p), xy(q)))
    return z.callout((p + q) / 2, text, dirs=dirs, fs=fs, dists=(38, 52, 68))


def site_frame(z, lw=2.2):
    """本件土地と、隣接地の境の線（北の筆界の延長・道路の東の線）。"""
    z.poly(SITE, color=BLACK, lw=lw)
    z.line(B(E_W - 3.0, north_s(E_W - 3.0)), B(E_W, north_s(E_W)), color=BLACK, lw=1.4)   # 4-5と4-6の境の北の筆界の延長
    z.line(B(E_W, S_S), B(E_W - 3.0, S_S), color=BLACK, lw=1.4)                           # 6-5と6-6の境の南の線の延長
    z.line(B(E_W, north_s(E_W)), B(E_W, north_s(E_W) - 2.5), color=BLACK, lw=1.4)         # 4-5と4-6の境
    z.line(B(E_W, S_S), B(E_W, S_S + 2.5), color=BLACK, lw=1.4)                            # 6-5と6-6の境
    z.line(B(E_E + 8, north_s(E_E) - 1.5), B(E_E + 8, S_S + 2.5), color=GRAY, lw=1.4)      # 道路の東の線
    z.line(B(E_E, north_s(E_E)), B(E_E, north_s(E_E) - 1.5), color=BLACK, lw=1.4)
    z.line(B(E_E, S_S), B(E_E, S_S + 2.5), color=BLACK, lw=1.4)


def neighbours(z, fs=15):
    z.free_text(B(6.5, north_s(6.5) - 2.8), '4－6', fs=fs)
    z.free_text(B(E_W - 2.0, north_s(E_W) - 1.6), '4－5', fs=fs)
    z.free_text(B(E_W - 2.0, 7.0), '5－5', fs=fs)
    z.free_text(B(E_W - 2.0, S_S + 1.6), '6－5', fs=fs)
    z.free_text(B(6.5, S_S + 2.8), '6－6', fs=fs)
    z.free_text(B(E_E + 4.0, 7.0), '道\n\n路', fs=fs)


# =====================================================================================
# 固定配置の図（card_fig）：座標は 横0〜100、縦0〜YH（縦横の縮尺は同じ）。重なり検査の対象外なので目視で確認する
# =====================================================================================
def card_fig(title, name, draw, note, w=16, h=11.6):
    setup_font()
    fig = plt.figure(figsize=(w, h), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=23, weight='bold', y=0.965)
    aw, ah = 0.96 * w, 0.74 * h
    ax = fig.add_axes([0.02, 0.16, 0.96, 0.74])
    yh = 100.0 * ah / aw
    ax.set_xlim(0, 100)
    ax.set_ylim(0, yh)
    ax.set_aspect('equal')
    ax.axis('off')
    draw(ax, yh)
    fig.text(0.5, 0.075, note, ha='center', va='center', fontsize=14.5, linespacing=1.5)
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print(f'[固定配置] {name}\n  →', path)


def box(ax, x, y, w, h, text, col=BLACK, fs=13.5, alpha=0.12, weight='normal', tc=BLACK, ha='center', lw=2.0):
    """箱（左下 x, y、幅 w、高さ h）。"""
    ax.add_patch(Rectangle((x, y), w, h, facecolor=col, alpha=alpha, edgecolor='none'))
    ax.add_patch(Rectangle((x, y), w, h, facecolor='none', edgecolor=col, lw=lw))
    tx = x + w / 2 if ha == 'center' else x + 1.0
    ax.text(tx, y + h / 2, text, ha=ha, va='center', fontsize=fs, color=tc, weight=weight, linespacing=1.5)


def arrow(ax, p, q, col=GRAY, lw=2.0):
    ax.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle='-|>', lw=lw, color=col, mutation_scale=18))


def txt(ax, x, y, s, fs=13.5, ha='center', va='center', col=BLACK, weight='normal'):
    ax.text(x, y, s, ha=ha, va=va, fontsize=fs, color=col, weight=weight, linespacing=1.5)


def plan(ax, pts, ox, oy, k, fc=None, ec=BLACK, lw=1.8, ls='-', alpha=0.28, closed=True, z=2):
    """平面の頂点（東, 南 [m]）を、図の位置（ox, oy は北西の角。1m ＝ k 単位）に描く。"""
    v = [(ox + e * k, oy - s * k) for e, s in pts]
    if fc:
        ax.add_patch(MPoly(v, closed=True, facecolor=fc, alpha=alpha, edgecolor='none', zorder=z))
    vv = v + [v[0]] if closed else v
    ax.plot([a for a, _ in vv], [b for _, b in vv], color=ec, lw=lw, ls=ls, zorder=z + 1, solid_capstyle='round')


def xyp(ox, oy, k, e, s):
    return ox + e * k, oy - s * k


def elev(ax, ox, oy, k, floors, fs=13, floor_h=1.0):
    """立面の断面（南から見る）。floors：下から [(階の名前, [(左端e, 右端e, 区分の名前, 色), ...])]。幅は m、高さは floor_h × k。"""
    for i, (name, parts) in enumerate(floors):
        y = oy + i * floor_h * k
        txt(ax, ox - 1.2, y + floor_h * k / 2, name, fs=fs, ha='right')
        for a, b, label, col in parts:
            ax.add_patch(Rectangle((ox + a * k, y), (b - a) * k, floor_h * k, facecolor=col, alpha=0.30, edgecolor=BLACK, lw=1.8))
            if label:
                txt(ax, ox + (a + b) / 2 * k, y + floor_h * k / 2, label, fs=fs, weight='bold')


ELEV_H20 = [('1階', [(0, 6, '（イ）', BLUE), (6, 12, '（イ）', BLUE)]),
            ('2階', [(0, 6, '（ロ）', GREEN), (6, 12, '（イ）', BLUE)]),
            ('3階', [(0, 12, '（ロ）', GREEN)])]


# ---- 図1：建物区分登記か建物分割登記か（第1章、藍子が「建物区分登記です」と答えたトリ先生の確認） ----
def zu01():
    def draw(ax, yh):
        k = 2.6
        box(ax, 2, yh - 8, 46, 7, '建物区分登記（本問）', col=BLUE, fs=17, weight='bold')
        box(ax, 52, yh - 8, 46, 7, '建物分割登記（本問ではない）', col=GRAY, fs=17, weight='bold')
        top = yh - 11
        # 左：1個の建物の中を区分
        plan(ax, [(0, 0), (12, 0), (12, 8), (0, 8)], 10, top, k, fc=BLUE)
        ax.plot([10 + 6 * k] * 2, [top, top - 8 * k], color=BLACK, lw=2.2, ls='--', zorder=5)
        txt(ax, 10 + 3 * k, top - 4 * k, '（イ）', fs=17, weight='bold', col=BLUE)
        txt(ax, 10 + 9 * k, top - 4 * k, '（ロ）', fs=17, weight='bold', col=BLUE)
        txt(ax, 24, 17, '1個の建物の中の、構造上も利用上も\n独立した部分を、登記の上でも別々の\n区分建物にする（不動産登記法第54条第1項第2号）', fs=13.5)
        # 右：主である建物と附属建物
        plan(ax, [(0, 0), (8, 0), (8, 8), (0, 8)], 56, top, k, fc=GRAY)
        plan(ax, [(10, 3), (14, 3), (14, 8), (10, 8)], 56, top, k, fc=GRAY, ls='--')
        txt(ax, 56 + 4 * k, top - 4 * k, '主である建物', fs=15)
        txt(ax, 56 + 12 * k, top - 6.5 * k, '附属\n建物', fs=13)
        arrow(ax, (56 + 14 * k + 1, top - 5.5 * k), (56 + 14 * k + 6, top - 5.5 * k), col=GRAY)
        txt(ax, 76, 17, '主である建物と附属建物のように、別の棟を\n切り離して別の1個の建物にする\n（同項第1号）', fs=13.5)
        box(ax, 12, 3.5, 76, 6, '本問は附属建物がなく、一棟の中の2つの部分を分ける　→　建物区分登記', col=RED, fs=15.5, weight='bold')
    card_fig('建物区分登記か、建物分割登記か', 'H20_dai22mon_zu01_kubun_bunkatsu', draw,
             '登記の目的は、一棟の中の部分を分けるなら区分、主である建物と附属建物を切り離すなら分割。\n'
             '建物の区分の登記も、表題部所有者又は所有権の登記名義人しか申請できない（同法第54条第1項）')


# ---- 図2：区分の全体像 ----
def zu02():
    fig, axes = new_figure('区分の全体像：（イ）部分と（ロ）部分、共用部分のPS',
                           '（イ）部分＝1階の2住戸＋2階の東の住戸（共同住宅）、（ロ）部分＝2階の西の部屋＋3階全部（居宅）。\nPSは共用部分、開放廊下は床面積に入らない。'
                           '1階131.00＝12.00×9.50＋12.00×0.50＋5.50×2.00、3階120.00＝12.00×9.50＋12.00×0.50（登記記録と一致）',
                           w=18, h=8.5, ncols=3)
    fig.subplots_adjust(top=0.84, bottom=0.16)
    zs = []
    for k, ax in enumerate(axes):
        z = Zu(ax, fontsize=12)
        if k == 0:
            z.poly(P(I1_WALL), color=BLACK, lw=2, fill=BLUE, alpha=0.28)
            z.line(B(6, 0), B(6, 9.5), color=BLACK, lw=1.2)
            z.free_text(B(3, 5), '（イ）', fs=14, weight='bold', color=BLUE)
            z.free_text(B(9, 5), '（イ）', fs=14, weight='bold', color=BLUE)
            ax.set_title('1階（登記記録 131.00㎡）', fontsize=16, weight='bold')
        elif k == 1:
            z.poly(P(RO2_WALL), color=BLACK, lw=2, fill=GREEN, alpha=0.30)
            z.poly(P(I2_WALL), color=BLACK, lw=2, fill=BLUE, alpha=0.28)
            z.free_text(B(3, 5), '（ロ）', fs=14, weight='bold', color=GREEN)
            z.free_text(B(9, 5), '（イ）', fs=14, weight='bold', color=BLUE)
            ax.set_title('2階（登記記録 131.00㎡）', fontsize=16, weight='bold')
        else:
            z.poly(P(RO3_WALL), color=BLACK, lw=2, fill=GREEN, alpha=0.30)
            z.free_text(B(6, 5), '（ロ）', fs=14, weight='bold', color=GREEN)
            ax.set_title('3階（登記記録 120.00㎡）', fontsize=16, weight='bold')
        for ps in (PS_W, PS_E):
            z.poly(P(ps), color=RED, lw=1.4, fill=RED, alpha=0.45)
        rk = ROUKA3 if k == 2 else ROUKA
        z.poly(P(rk), color=GRAY, lw=1.0, ls='--', check=False)
        hatch(ax, P(rk))
        fit(ax, P(F1), margin=0.10, extra=[xy(B(-1.5, 16.5)), xy(B(13.5, -2.0))], pad_aspect=True)
        z.callout(B(6, 9.75), 'PS（共用部分）', dirs=(-90, -110, -70), fs=12, color=RED, dists=(60, 75, 90))
        z.free_text(B(6, 14.6), '開放廊下（床面積に入らない）' if k < 2 else '開放廊下・開放バルコニー\n（床面積に入らない）', fs=12,
                    color=GRAY)
        zs.append(z)
    zs[0].north_arrow()
    save(fig, zs, 'H20_dai22mon_zu02_kubun_zentaizou')


# ---- 図3：注の仕分け ----
def zu03():
    def draw(ax, yh):
        cols = [(2, '調査結果の（注）\n（土地の登記記録の下。番号なし）', ORANGE,
                 ['各専有部分に係る敷地利用権の', '割合を定める規約はなく、', '分離処分を可能とする規約もない', '',
                  '→ 規約証明書は要らない', '→ 敷地権の割合は専有部分の', '　床面積の割合（第14条）']),
                (35, '図の（注）1〜8\n（配置図・平面図の下）', BLUE,
                 ['1　測定値は壁心間', '2　壁厚は15cm', '3　筆界までの距離は外壁から', '4　PSは共用部分（0.50×0.50）',
                  '5　（　）内の数字は土地の地番', '6　建物の隅部は直角', '7　北は道路に平行', '8　天井までの高さは2.5m以上']),
                (68, '問題文の注1〜5\n（問1〜問3の下）', GREEN,
                 ['1　縮尺は建物図面500分の1、', '　　各階平面図250分の1', '2　不動産番号を書いても所在・', '　　家屋番号等は省略しない',
                  '3　訂正等は押印・字数不要', '4　書面で申請する', '5　問3の解答欄は問1の下'])]
        for x, head, col, lines in cols:
            box(ax, x, yh - 12, 30, 11, head, col=col, fs=13.5, weight='bold')
            ax.add_patch(Rectangle((x, 12), 30, yh - 26, facecolor=col, alpha=0.08, edgecolor=col, lw=2))
            for i, ln in enumerate(lines):
                txt(ax, x + 1.2, yh - 18.5 - i * 3.45, ln, fs=12.2, ha='left')
        box(ax, 8, 1.2, 84, 8.5, '番号がかぶる：図の（注）4（PS）と問題文の注4（書面申請）は別物 → 「問題文の注4」「図の（注）4」と書き分ける',
            col=RED, fs=14, weight='bold')
    card_fig('注の仕分け：番号のない注・図の（注）・問題文の注', 'H20_dai22mon_zu03_chuu_shiwake', draw,
             '注は3系統。調査結果の（注）は敷地権の割合と規約証明書の要否、図の（注）は寸法の読み方、問題文の注は答案の書き方を決める。')


# ---- 図4：1階131.00の検算と開放廊下 ----
def zu04():
    def draw(ax, yh):
        k = 2.9
        ox, oy = 6, yh - 3
        for r, c in [(rect(0, 0, 12, 9.5), BLUE), (rect(0, 9.5, 12, 10), ORANGE), (rect(0, 10, 5.5, 12), GREEN)]:
            plan(ax, r, ox, oy, k, fc=c, ec=BLACK, lw=1.4, alpha=0.30)
        plan(ax, rect(5.5, 10, 12, 12), ox, oy, k, fc=GRAY, ec=GRAY, lw=1.6, ls='--', alpha=0.20)
        txt(ax, ox + 6 * k, oy - 4.75 * k, '12.00×9.50＝114.00', fs=14.5, weight='bold')
        ax.annotate('12.00×0.50＝6.00\n（壁で囲まれた細い帯）', xy=(ox + 12 * k, oy - 9.75 * k), xytext=(ox + 12 * k + 4, oy - 9.75 * k + 7.0),
                    fontsize=12.5, ha='left', va='center', arrowprops=dict(arrowstyle='-', color=BLACK, lw=1.2))
        txt(ax, ox + 2.75 * k, oy - 11 * k, '5.50×2.00＝11.00', fs=12.5)
        txt(ax, ox + 8.75 * k, oy - 11 * k, '開放廊下\n6.50×2.00＝13.00', fs=13, col=GRAY)
        box(ax, 54, yh - 22, 44, 17, '壁で囲まれた部分だけ足す\n114.00＋6.00＋11.00＝131.00㎡\n（登記記録の1階131.00と一致）', col=BLUE, fs=15, weight='bold')
        box(ax, 54, yh - 41, 44, 15, '開放廊下は壁で囲まれていないので床面積に入らない\n12.00×12.00＝144.00 から 13.00 を引いても\n144.00−13.00＝131.00', col=GRAY, fs=14)
        txt(ax, 76, yh - 48, '3階は 12.00×9.50＋12.00×0.50＝120.00（南の帯は開放廊下・開放バルコニーだけ）', fs=13.5)
    card_fig('登記記録の床面積を平面図で検算：開放廊下は床面積に入らない', 'H20_dai22mon_zu04_kairou_kensan', draw,
             '区分する前に、登記記録の床面積（1階131.00・3階120.00）が平面図と合っているかを確かめる。壁心の寸法で、壁で囲まれた部分だけを足す。')


# ---- 図5：PSは一棟の床面積に入る ----
def zu05():
    def draw(ax, yh):
        plan(ax, F1, 6, yh - 3, 2.6, fc=BLUE, ec=BLACK, lw=1.4, alpha=0.18)
        for ps in (PS_W, PS_E):
            plan(ax, ps, 6, yh - 3, 2.6, fc=RED, ec=RED, lw=1.6, alpha=0.6)
        ax.annotate('PS 0.50×0.50が2つ', xy=xyp(6, yh - 3, 2.6, 6.0, 9.75), xytext=(12, 3.5), fontsize=14, color=RED, weight='bold',
                    arrowprops=dict(arrowstyle='-', color=RED, lw=1.4), ha='left', va='center')
        # 右：棒で比べる
        txt(ax, 66, yh - 3, 'PSを入れると', fs=15, weight='bold', col=GREEN, ha='left')
        ax.add_patch(Rectangle((52, yh - 11), 40.2, 4.5, facecolor=BLUE, alpha=0.30, edgecolor=BLACK, lw=1.5))
        ax.add_patch(Rectangle((92.2, yh - 11), 0.31 * 4, 4.5, facecolor=RED, alpha=0.7, edgecolor=RED, lw=1.5))
        txt(ax, 72, yh - 8.75, '130.50', fs=15, weight='bold')
        txt(ax, 95, yh - 14.5, '＋0.50', fs=14.5, col=RED, weight='bold')
        txt(ax, 66, yh - 20, '＝ 131.00㎡（登記記録の1階と一致）', fs=15, weight='bold', col=GREEN, ha='left')
        txt(ax, 66, yh - 28, 'PSを入れないと', fs=15, weight='bold', col=RED, ha='left')
        ax.add_patch(Rectangle((52, yh - 36), 40.2, 4.5, facecolor=BLUE, alpha=0.30, edgecolor=BLACK, lw=1.5))
        txt(ax, 72, yh - 33.75, '130.50', fs=15, weight='bold')
        txt(ax, 66, yh - 41, '＝ 130.50㎡　登記記録と合わない', fs=15, weight='bold', col=RED, ha='left')
    card_fig('PSは一棟の建物の床面積には入る', 'H20_dai22mon_zu05_ps_ittou', draw,
             'PSは共用部分でも一棟の建物の一部なので、一棟の床面積（登記記録の131.00）には入っている。入れずに数えると1階は130.50になって合わない。\n'
             '専有部分（（イ）・（ロ））には入らない（第3章）')


# ---- 図6：時系列と権利関係 ----
def zu06():
    def draw(ax, yh):
        y0 = yh - 12
        ax.plot([4, 96], [y0, y0], color=GRAY, lw=3)
        for x, d, t, col in [(18, '平成19年5月4日', '抵当権の設定\n（建物と、土地の大輔さんの持分に\n同じ抵当権。受付第13239号）', BLACK),
                             (60, '平成20年8月24日', '区分することにして\n同じ日に申請\n（答案用紙に印刷）', RED)]:
            ax.plot(x, y0, 'o', ms=13, color=col)
            txt(ax, x, y0 + 3.5, d, fs=16, weight='bold', col=col)
            txt(ax, x, y0 - 8, t, fs=13.5)
        box(ax, 2, 2, 46, 15, '土地（5番6、宅地、320.55㎡）は共有\n平野大輔さん　持分4分の3\n平野友子さん　持分4分の1', col=BLUE, fs=14.5)
        box(ax, 52, 2, 46, 15, '建物（家屋番号5番6）は平野大輔さんだけが\n所有権の登記名義人。区分の登記に\n申請の期限はない（任意の登記）', col=GREEN, fs=14.5)
        box(ax, 20, 19, 60, 6.5, '調査結果の（注）：敷地利用権の割合を定める規約も、分離処分を可能とする規約もない', col=ORANGE, fs=13.5)
    card_fig('時系列と権利関係のメモ', 'H20_dai22mon_zu06_jikeiretsu', draw,
             '抵当権は建物と土地の持分の両方に、同じ日・同じ受付番号で付いている。土地は共有で建物は大輔さん単独。\n'
             'この3つが、第4章（敷地権の割合）と第5章（問3）でそのまま効く。')


# ---- 図7：敷地の辺長確認図（作図チェック用） ----
def zu07():
    fig, axes = new_figure('本件土地（5番6）の辺長確認図（作図チェック用）',
                           '(18.15－2÷12.15＋19.15＋3÷12.15)÷2×17.15＝320.5532…→320.55㎡（登記記録の地積と一致）。\n'
                           '距離は外壁から（図の（注）3）、外壁は壁の中心線の0.075外側。辺長は建物図面には書かない',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(SITE, color=BLACK, lw=2.4, fill=BLUE, alpha=0.08)
    z.poly(P(OUTER), color=GRAY, lw=1.6, fill=GRAY, alpha=0.25)
    fit(ax, SITE, margin=0.10, extra=[xy(B(-7.5, -6.5)), xy(B(20.5, 19.5))], pad_aspect=True)
    z.north_arrow()
    c = centroid(SITE)
    dims(z, SITE, ['北 17.21', '東 19.40', '南 17.15', '西 17.99'], fs=15, ref=c)
    dim_line(z, B(E_W, 2.0), B(-W, 2.0), '2.00', dirs=(90, 110, 70))
    dim_line(z, B(E_W, 11.0), B(-W, 11.0), '2.00', dirs=(90, 110, 70))
    dim_line(z, B(-W, north_s(-W)), B(-W, -W), '2.00', dirs=(160, 180, 140))
    dim_line(z, B(12 + W, north_s(12 + W)), B(12 + W, -W), '3.00', dirs=(20, 0, 40))
    dim_line(z, B(12 + W, 1.0), B(E_E, 1.0), '3.00', dirs=(-90, -70, -110))
    dim_line(z, B(12 + W, 8.8), B(E_E, 8.8), '3.00', dirs=(90, 70, 110))
    dim_line(z, B(-W, 12 + W), B(-W, S_S), '4.00', dirs=(160, 180, 200))
    dim_line(z, B(12 + W, 10 + W), B(12 + W, S_S), '6.00', dirs=(20, 0, -20))
    z.free_text(B(6.0, 3.0), '外壁から外壁まで　東西 12.15', fs=13)
    z.free_text(B(6.0, 6.5), '南北　西の外壁で 18.15\n　　　東の外壁で 19.15', fs=13)
    z.free_text(B(6.5, 14.4), '本件土地（5－6）320.55㎡', fs=15, weight='bold')
    neighbours(z, fs=14)
    save(fig, [z], 'H20_dai22mon_zu07_shikichi_henchou')


# ---- 図8：壁の厚みを落とすと地積が合わない ----
def zu08():
    def draw(ax, yh):
        def bar(y, parts, col_total, label_total, area_text, ok):
            x = 6
            for wd, lab, col in parts:
                ax.add_patch(Rectangle((x, y), wd, 6, facecolor=col, alpha=0.30, edgecolor=BLACK, lw=1.8))
                txt(ax, x + wd / 2, y + 3, lab, fs=14.5, weight='bold')
                x += wd
            txt(ax, 6 + 88 / 2, y + 9.5, label_total, fs=15.5, weight='bold', col=col_total)
            txt(ax, 6 + 88 / 2, y - 3.5, area_text, fs=15, weight='bold', col=col_total)
        k = 5.0   # 1m ＝ 5単位（東西の長さ）
        bar(yh - 17, [(2.0 * k, '2.00', GRAY), (12.0 * k, '壁の中心線から 12.00', ORANGE), (3.0 * k, '3.00', GRAY)], RED,
            '誤り：距離を壁の中心線から測ったと思い込む　東西 2.00＋12.00＋3.00＝17.00', '面積はおよそ315.2㎡　→　登記記録の320.55と合わない', False)
        bar(yh - 38, [(2.0 * k, '2.00', GRAY), (12.15 * k, '外壁から外壁まで 12.15', GREEN), (3.0 * k, '3.00', GRAY)], GREEN,
            '正解：距離は外壁から（図の（注）3）。壁厚15cmの半分0.075を両側に足す　東西 2.00＋12.15＋3.00＝17.15', '面積は320.5532…→320.55㎡　→　登記記録と一致', True)
        txt(ax, 50, 2.2, '外壁から外壁まで ＝ 壁の中心線の寸法12.00 ＋ 0.075×2 ＝ 12.15', fs=14, col=BLACK)
    card_fig('壁の厚みを落とすと、地積が合わない', 'H20_dai22mon_zu08_kabeatsu_ochi', draw,
             '地積との一致は、配置図の距離（外壁から）と壁の厚みの読み方が両方正しいことの裏付け。\n'
             '壁の厚みを落とすと東西が17.00になり、面積が約315.2㎡になって合わない。')


# ---- 図9：所在は5番6の1筆 ----
def zu09():
    fig, axes = new_figure('所在の確認：建物は5番6の中に収まっている',
                           '建物の外壁から筆界までの距離が、東西南北のどの方向もいちばん狭い所で2.00以上ある（西2.00・北2.00・東3.00・南4.00）。'
                           '\n隣の筆（4－5・4－6・5－5・6－5・6－6）にかからないので、所在は「A市C町六丁目5番地6」の1筆',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    site_frame(z)
    z.poly(P(OUTER), color=BLACK, lw=2.2, fill=GRAY, alpha=0.25)
    fit(ax, SITE, margin=0.06, extra=[xy(B(-7.5, -6.0)), xy(B(24.5, 21.5))], pad_aspect=True)
    z.north_arrow()
    dim_line(z, B(E_W, 11.0), B(-W, 11.0), '西 2.00', dirs=(-135, -150, -120))
    dim_line(z, B(-W, north_s(-W)), B(-W, -W), '北 2.00', dirs=(160, 180, 140))
    dim_line(z, B(12 + W, 8.8), B(E_E, 8.8), '東 3.00', dirs=(90, 70, 110))
    dim_line(z, B(-W, 12 + W), B(-W, S_S), '南 4.00', dirs=(160, 180, 200))
    z.free_text(B(6.0, 5.0), '一棟の建物', fs=16, weight='bold')
    z.free_text(B(9.5, 13.2), '5－6', fs=16)
    neighbours(z)
    save(fig, [z], 'H20_dai22mon_zu09_shozai_kakunin')


# ---- 図10：（ロ）部分の地上の最低階は2階 ----
def zu10():
    def draw(ax, yh):
        k = 2.2
        fh = 3.4
        oy = yh - 32
        txt(ax, 25, yh - 3, '南から見た断面（模式）', fs=15, weight='bold')
        elev(ax, 12, oy, k, ELEV_H20, floor_h=fh)
        ax.add_patch(Rectangle((12, oy + fh * k), 6 * k, fh * k, facecolor='none', edgecolor=RED, lw=4, zorder=6))
        txt(ax, 25, oy - 4, '赤枠＝（ロ）の地上の最低階（2階）', fs=14, weight='bold', col=RED)
        txt(ax, 75, yh - 3, '建物図面（北から見た平面）', fs=15, weight='bold')
        plan(ax, F1, 62, yh - 9, 2.1, ec=BLACK, lw=1.5, ls='--')
        plan(ax, RO2_WALL, 62, yh - 9, 2.1, fc=GREEN, ec=BLACK, lw=3.0, alpha=0.30)
        txt(ax, 62 + 3 * 2.1, yh - 9 - 5 * 2.1, '（ロ）\n2階部分', fs=14, weight='bold')
        txt(ax, 62 + 9 * 2.1, yh - 9 - 5 * 2.1, '一棟の\n1階', fs=13, col=GRAY)
        box(ax, 2, 4, 96, 8, '2階部分を実線（規則第82条第1項）、一棟の建物の1階を点線（準則第52条第2項）で描く', col=RED, fs=14, weight='bold')
    card_fig('建物図面に実線で描くのは、（ロ）部分の地上の最低階（2階部分）', 'H20_dai22mon_zu10_saiteikai', draw,
             '区分建物の建物図面は、その区分建物の地上の最低階の位置と形状を描く。（ロ）部分には1階がないので、最低階は2階。\n'
             '「建物は1階を描くもの」と決めつけない。')


# ---- 図11：建物の存する部分 ----
def zu11():
    def draw(ax, yh):
        oy = yh - 32
        txt(ax, 25, yh - 3, '令和3年度の（イ）部分（縦割り）', fs=15, weight='bold', col=GRAY)
        elev(ax, 12, oy, 1.9, [('1階', [(0, 8, '（イ）', BLUE), (8, 16, '（ロ）', GRAY)]), ('2階', [(0, 8, '（イ）', BLUE), (8, 16, '（ロ）', GRAY)])],
             floor_h=4.0)
        txt(ax, 27, oy - 6, '1階から始まる専有部分\n→ 建物の存する部分は書かない', fs=13.5, col=GRAY)
        txt(ax, 75, yh - 3, '本問の（ロ）部分', fs=15, weight='bold', col=RED)
        elev(ax, 62, oy, 1.7, ELEV_H20, floor_h=3.0)
        txt(ax, 75, oy - 6, '1階以外の部分にだけ存する（2階と3階）', fs=13.5, col=RED)
        box(ax, 50, 4, 48, 8, '「建物の存する部分　2階、3階」を書く', col=RED, fs=15, weight='bold')
    card_fig('「建物の存する部分」を書くのは、1階以外にだけ存する区分建物', 'H20_dai22mon_zu11_sonsuru_bubun', draw,
             '建物図面は1階（地上の最低階）の形しか描かないので、2階・3階にしかない専有部分は、図から階が読めない。\n'
             'そこで存する階層を書き添える（不動産登記事務取扱手続準則第52条第2項後段）。1階から始まる専有部分には書かない。')


# ---- 図12：一点鎖線は要らない ----
def zu12():
    def draw(ax, yh):
        txt(ax, 25, yh - 3, '本問：一棟の2階は1階と同じ形', fs=15, weight='bold', col=GREEN)
        plan(ax, F1, 5, yh - 9, 2.0, ec=BLACK, lw=1.5, ls='--')
        plan(ax, F1, 5, yh - 9, 2.0, ec=BLUE, lw=1.0, ls='-', fc=BLUE, alpha=0.12)
        txt(ax, 5 + 12 * 2.0 + 1.2, yh - 9 - 6.5 * 2.0, '1階 131.00㎡\n2階 131.00㎡\n（同じ形）', fs=12.5, ha='left')
        txt(ax, 25, 16, '一点鎖線は描かない\n（実線の（ロ）と、点線の一棟の1階だけ）', fs=14, col=GREEN, weight='bold')
        txt(ax, 75, yh - 3, '例（本問ではない）：2階の形が1階と違う', fs=15, weight='bold', col=GRAY)
        plan(ax, F1, 56, yh - 9, 1.7, ec=BLACK, lw=1.5, ls='--')
        plan(ax, rect(0, 0, 12, 7.5), 56, yh - 9, 1.7, ec=ORANGE, lw=2.2, ls='-.')
        txt(ax, 56 + 12 * 1.7 + 1.0, yh - 9 - 3.7 * 1.7, '橙の一点鎖線＝\n違う形の2階', fs=12.5, col=ORANGE, ha='left')
        txt(ax, 76, 16, '区分建物がある階の一棟の形が\n1階と違うときだけ、一点鎖線でその階の形も描く\n（準則第52条第3項）', fs=13, col=GRAY)
    card_fig('一点鎖線は要らない：一棟の2階は1階と同じ形', 'H20_dai22mon_zu12_itten_sasen', draw,
             '準則第52条第3項は、区分建物の存する階（2階以上にわたるときはいちばん下の階）の一棟の形が、一棟の1階の形と異なるときだけ。\n'
             '本問の一棟の2階は、1階と同じ形で同じ131.00㎡。')


# =====================================================================================
# 答案用紙（その3）の実寸の図（建物図面・各階平面図）
# =====================================================================================
FR_L, FR_R, FR_B, FR_T = 26.0, 348.0, 60.3, 254.4      # 図を描く枠
MID = 187.0                                           # 中央の仕切り（上下の短い線だけが印刷）
SH_X0, SH_X1, SH_Y0, SH_Y1 = 18.0, 356.0, 38.0, 276.0   # 画像に入れる範囲（mm）
SHEET_MM = dict(frame=(FR_L, FR_R, FR_B, FR_T), mid=MID, kaoku=(195.4, 260.8, FR_T, 267.1), kaoku_div=223.1,
                shozai=(195.4, FR_R, 241.7, FR_T), sakusei=(FR_L, 176.1, 44.5, FR_B), sakusei_div=(51.6, 140.3, 151.8),
                shinsei=(196.9, 347.6, 44.5, FR_B), shinsei_div=(222.9, 311.7, 323.3))
SHEET_PX = 1400 / 420                                 # 答案用紙の画像の 1mm あたりの画素数（照合スクリプトで測り直す）


def M(x, y):
    """用紙の mm の位置（x：右向き、y：上向き）を zu_helpers の複素数（縦, 横）にする。"""
    return complex(y, x)


ZX0, ZY0 = 254.5, 160.0                               # 建物図面：建物の北西の角（壁の中心線の交点）を置く用紙の位置（mm）


def Z500(e, s):
    """建物図面（縮尺1/500、1m ＝ 2mm）：建物の (東, 南) [m] を用紙の mm に置く。"""
    return M(ZX0 + 2 * e, ZY0 - 2 * s)


def H250(e, s, x0, y0):
    """各階平面図（縮尺1/250、1m ＝ 4mm）：区分建物の内法の (東, 南) [m] を用紙の mm に置く。原点を (x0, y0) mm に。"""
    return M(x0 + 4 * e, y0 - 4 * s)


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
    ax.text((SH_X0 + SH_X1) / 2, 271.0, title, ha='center', va='center', fontsize=20, weight='bold')
    return fig, ax, z


def sheet3(ax, z):
    """答案用紙（その3）の印刷（試験の答案用紙どおり）と、家屋番号・建物の所在の記入。
    作成者・申請人の欄は（略）と印刷されているので何も書かない。方位記号は印刷されていない。"""
    def rrect(x0, x1, y0, y1, lw=1.3):
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, lw=lw, ec=BLACK, zorder=3))

    def ln(x0, y0, x1, y1, lw=1.0):
        ax.plot([x0, x1], [y0, y1], color=BLACK, lw=lw, zorder=3)

    def tt(x, y, s, fs=12, ha='center', **kw):
        ax.text(x, y, s, ha=ha, va='center', fontsize=fs, zorder=4, family='Noto Serif CJK JP', **kw)

    S = SHEET_MM
    tt(26.7, 265.3, '問２', fs=12, ha='left', weight='bold')
    tt(107.0, 261.0, '各　階　平　面　図', fs=15)
    tt(304.4, 261.0, '建　物　図　面', fs=15)
    rrect(FR_L, FR_R, FR_B, FR_T, lw=1.6)                         # 図を描く枠
    ln(MID, FR_T, MID, 249.9, lw=1.6)                            # 中央の仕切り（上下の短い線だけが印刷）
    ln(MID, FR_B, MID, 64.8, lw=1.6)
    rrect(*S['kaoku'])                                           # 家屋番号の箱（枠の外の上）
    ln(S['kaoku_div'], FR_T, S['kaoku_div'], 267.1)
    tt(209.2, 260.8, '家屋番号', fs=11)
    rrect(*S['shozai'])                                          # 建物の所在の欄（枠の中の上端）
    ln(S['kaoku_div'], 241.7, S['kaoku_div'], FR_T)
    tt(209.2, 248.0, '建物の所在', fs=11)
    ax.text(226.0, 260.8, 'C町六丁目5番6の2', ha='left', va='center', fontsize=12, color=INK, zorder=4)
    ax.text(226.0, 248.0, 'A市C町六丁目5番地6', ha='left', va='center', fontsize=12, color=INK, zorder=4)
    x0, x1, y0, y1 = S['sakusei']                                # 作成者・縮尺 1/250（（略）と平成20年8月24日作成は印刷済み）
    rrect(x0, x1, y0, y1)
    for x in S['sakusei_div']:
        ln(x, y0, x, y1)
    tt(38.8, 52.4, '作　成　者', fs=11)
    tt(95.9, 56.3, '（略）', fs=10.5)
    tt(138.0, 48.5, '（平成20年8月24日作成）', fs=10, ha='right')
    tt(145.9, 52.4, '縮尺', fs=10)
    ln(155.0, 46.4, 174.0, 59.0, lw=0.9)
    tt(160.0, 56.5, '1', fs=10)
    tt(169.0, 48.5, '250', fs=10)
    x0, x1, y0, y1 = S['shinsei']                                # 申請人・縮尺 1/500
    rrect(x0, x1, y0, y1)
    for x in S['shinsei_div']:
        ln(x, y0, x, y1)
    tt(209.9, 52.4, '申　請　人', fs=11)
    tt(267.3, 52.4, '（略）', fs=10.5)
    tt(317.5, 52.4, '縮尺', fs=10)
    ln(327.0, 46.4, 346.0, 59.0, lw=0.9)
    tt(332.0, 56.5, '1', fs=10)
    tt(341.0, 48.5, '500', fs=10)


def zumen_content(z):
    """右半分：建物図面（縮尺1/500、1m ＝ 2mm）。敷地、（ロ）部分の2階部分（実線）、一棟の1階（点線）、筆界から外壁までの距離、地番・道路、方位。"""
    ax = z.ax
    site = [Z500(e, s) for e, s in SITE_ES]
    z.poly(site, lw=1.4)
    z.line(Z500(E_W - 3.0, north_s(E_W - 3.0)), Z500(E_W, north_s(E_W)), lw=1.0)       # 4-5と4-6の境の北の筆界の延長
    z.line(Z500(E_W, S_S), Z500(E_W - 3.0, S_S), lw=1.0)
    z.line(Z500(E_W, north_s(E_W)), Z500(E_W, north_s(E_W) - 2.5), lw=1.0)
    z.line(Z500(E_W, S_S), Z500(E_W, S_S + 2.5), lw=1.0)
    z.line(Z500(E_E + 8, north_s(E_E) - 1.5), Z500(E_E + 8, S_S + 2.5), color=GRAY, lw=0.9)   # 道路の向こう側（幅員8.00）
    z.line(Z500(E_E, north_s(E_E)), Z500(E_E, north_s(E_E) - 1.5), lw=1.0)
    z.line(Z500(E_E, S_S), Z500(E_E, S_S + 2.5), lw=1.0)
    z.poly([Z500(e, s) for e, s in F1], lw=1.2, ls='--')                                 # 一棟の建物の1階（点線）
    z.poly([Z500(e, s) for e, s in RO2_WALL], lw=2.2)                                   # （ロ）部分の2階部分（実線）
    for (e0, s0), (e1, s1), t, dirs in [((E_W, north_s(0)), (0, north_s(0)), '', ()),]:
        pass
    ext = [((0, north_s(0)), (0, 0), '2.00', (100, 115, 85)),             # 北西の角：北の筆界から北の外壁
           ((E_W, 3.0), (0, 3.0), '2.00', (110, 125, 95)),                # 西の筆界から西の外壁（北の部分）
           ((E_W, 11.0), (0, 11.0), '2.00', (-110, -125, -95)),           # 西の筆界から西の外壁（南西の張り出し）
           ((1.5, 12.0), (1.5, S_S), '4.00', (30, 15, 45))]               # 南西の角から南の筆界
    for p, q, t, dirs in ext:
        z.dim_line(Z500(*p), Z500(*q), lw=1.1)
        z.callout((Z500(*p) + Z500(*q)) / 2, t, dirs=dirs, fs=9.5, dists=(26, 36, 48, 60))
    z.free_text(Z500(2.9, 5.5), '（ロ）', fs=11, weight='bold')
    for (e, s), t in [((6.5, north_s(6.5) - 2.6), '4－6'), ((E_W - 2.6, north_s(E_W) - 1.8), '4－5'), ((E_W - 2.6, 7.0), '5－5'),
                      ((E_W - 2.6, S_S + 1.8), '6－5'), ((6.5, S_S + 2.6), '6－6'), ((10.0, 13.0), '5－6'), ((E_E + 4.0, 7.0), '道路')]:
        z.free_text(Z500(e, s), t, fs=10, offsets=((0, 0), (0, 8), (0, -8), (10, 0), (-10, 0)))
    ax.text(*(xy(Z500(6.0, S_S + 9.0))), '建物の存する部分　2階、3階', ha='center', va='center', fontsize=11.5, color=INK, weight='bold', zorder=4)
    # 方位（答案用紙には印刷されていないので書く。規則第82条第2項）
    nx, ny = 335.0, 215.0
    ax.annotate('', xy=(nx, ny + 14), xytext=(nx, ny), arrowprops=dict(arrowstyle='-|>', lw=1.8, color=BLACK, mutation_scale=15), zorder=4)
    ax.text(nx, ny + 17.5, 'N', ha='center', va='center', fontsize=12, weight='bold', zorder=4)
    z.segments.append(((nx, ny), (nx, ny + 14)))


HX0, HY2, HY3 = 36.0, 224.0, 150.0                    # 各階平面図：2階部分・3階部分の北西の角（内側の線）を置く用紙の位置（mm）


def heimen_content(z):
    """左半分：各階平面図（縮尺1/250、1m ＝ 4mm）。内法の辺長、階の別、求積と床面積、3階部分には2階部分の位置を点線で。
    （ロ）部分にも一棟にも1階の図はなく、いちばん下の階（2階部分）の位置を点線で重ねる（解答例どおり）。方位は書かない（規則第83条第1項）。"""
    ax = z.ax
    z.free_text(M(32.0, 236.0), '２階部分', fs=12, ha='left', weight='bold')
    f2 = [H250(e, s, HX0, HY2) for e, s in RO2]
    z.poly(f2, lw=1.6)
    c2 = H250(2.7, 6.0, HX0, HY2)
    for i, t in enumerate(['5.85', '9.35', None, '2.50', '5.35', '11.85']):
        if t:
            z.edge_label(f2[i], f2[(i + 1) % len(f2)], t, c2, fs=9.5, dists=(7, 11, 15))
    z.callout(H250(5.6, 9.35, HX0, HY2), '0.50', dirs=(-15, -30, 0), fs=9.5, dists=(24, 32, 42))
    ax.text(*xy(M(78.0, 205.0)), '求積\n5.35×11.85＝63.3975\n0.50× 9.35＝ 4.6750\n　　　　計　68.0725\n床面積　68.07㎡', ha='left', va='center',
            fontsize=10.5, color=INK, zorder=4, linespacing=1.5)
    z.segments.append((xy(M(78.0, 213.0)), xy(M(110.0, 213.0))))
    z.free_text(M(32.0, 162.0), '３階部分', fs=12, ha='left', weight='bold')
    f3 = [H250(e, s, HX0, HY3) for e, s in RO3]
    z.poly(f3, lw=1.6)
    z.line(H250(5.85, 0, HX0, HY3), H250(5.85, 9.35, HX0, HY3), lw=1.0, ls='--')              # 2階部分の東の辺
    z.poly([H250(e, s, HX0, HY3) for e, s in [(5.35, 9.85), (5.35, 11.85), (0, 11.85), (0, 9.85)]], lw=1.0, ls='--', closed=False)
    c3 = H250(5.9, 4.9, HX0, HY3)
    for i, t in enumerate(['11.85', '9.85', None, None, None, None, '5.35', '9.85']):
        if t:
            z.edge_label(f3[i], f3[(i + 1) % len(f3)], t, c3, fs=9.5, dists=(7, 11, 15))
    notch(z, 5.35, 6.50, 9.35, 9.85, '1.15', fs=9.5, down=(30, 38, 46), wdirs=(150, 135, 165)) if False else None
    z.callout(H250(5.35, 9.60, HX0, HY3), '0.50', dirs=(150, 135, 165), fs=9.5, dists=(26, 34, 44))
    z.callout(H250(5.925, 9.35, HX0, HY3), '1.15', dirs=(-70, -85, -55), fs=9.5, dists=(34, 44, 54))
    z.callout(H250(6.50, 9.60, HX0, HY3), '0.50', dirs=(-30, -15, -45), fs=9.5, dists=(26, 34, 44))
    ax.text(*xy(M(96.0, 142.0)), '求積\n5.35×9.85＝52.6975\n1.15×9.35＝10.7525\n5.35×9.85＝52.6975\n　　　　計　116.1475\n床面積　116.14㎡',
            ha='left', va='center', fontsize=10.5, color=INK, zorder=4, linespacing=1.5)
    z.segments.append((xy(M(96.0, 150.0)), xy(M(130.0, 150.0))))
    z.free_text(M(100.0, 114.0), '点線は２階部分の位置', fs=9.5, ha='left', color=GRAY)


def zu13():
    fig, ax, z = sheet_figure('建物図面の完成形（答案用紙（その3）の建物図面の側・縮尺1/500の実際の大きさ）')
    sheet3(ax, z)
    zumen_content(z)
    ax.text((SH_X0 + SH_X1) / 2, 42.0 - 11, '（ロ）部分の地上の最低階（2階部分）を実線、一棟の建物の1階を点線で描き、外壁までの距離（北2.00、西2.00・2.00、南4.00）と「建物の存する部分　2階、3階」を書く。',
            ha='center', va='center', fontsize=12.5)
    ax.text((SH_X0 + SH_X1) / 2, 42.0 - 17, '申請人の欄は（略）と印刷済みで書かない。敷地の辺長（17.15など）は書かない。方位記号は印刷されていないので書き添える。各階平面図の側（左半分）は第3章で描く',
            ha='center', va='center', fontsize=11.5, color=GRAY)
    save(fig, [z], 'H20_dai22mon_zu13_tatemono_zumen')


def zu20():
    fig, ax, z = sheet_figure('各階平面図の完成形（答案用紙（その3）の各階平面図の側・縮尺1/250の実際の大きさ）')
    sheet3(ax, z)
    heimen_content(z)
    ax.text((SH_X0 + SH_X1) / 2, 42.0 - 11, '内法の辺長・求積・床面積を書く。3階部分には、（ロ）部分のいちばん下の階（2階部分）の位置を点線で重ねる（解答例どおり）。',
            ha='center', va='center', fontsize=12.5)
    ax.text((SH_X0 + SH_X1) / 2, 42.0 - 17, '作成者の欄は（略）と平成20年8月24日作成が印刷済みで書かない。方位は書かない（不動産登記規則第83条第1項）。建物図面の側（右半分）は第2章で描いた',
            ha='center', va='center', fontsize=11.5, color=GRAY)
    save(fig, [z], 'H20_dai22mon_zu20_kakukai_heimenzu')


# =====================================================================================
# 床面積の計算（第3章）
# =====================================================================================
def zu14():
    fig, axes = new_figure('壁心から内法へ：区分建物の床面積は、壁の内側線で囲んで測る',
                           '区分した瞬間に、専有部分の測り方は壁心（壁の中心線）から内法（壁の内側線。不動産登記規則第115条）に切り替わる。\n'
                           '登記記録の3階120.00は壁心の数字なので、そのまま（ロ）部分の床面積にしない。壁厚15cmの半分0.075ずつ部屋の側へ入る',
                           w=19, h=9.5, ncols=3, width_ratios=[1, 0.78, 1])
    fig.subplots_adjust(top=0.84, bottom=0.15)
    ext = [xy(B(-2.2, -2.2)), xy(B(14.0, 12.5))]
    z = Zu(axes[0], fontsize=13)
    z.poly(P(F3), color=RED, lw=2.2, fill=RED, alpha=0.14)
    axes[0].set_title('登記記録の120.00㎡（壁心）', fontsize=16, weight='bold', color=RED)
    fit(axes[0], P(F3), margin=0.10, extra=ext, pad_aspect=True)
    dims(z, P(F3), ['12.00', '10.00', '12.00', '10.00'], fs=13)
    z.free_text(B(6, 5), '12.00×10.00＝120.00\n（壁の中心線で囲む）', fs=13, color=RED)
    z2 = Zu(axes[1], fontsize=12)
    wall = [complex(0.25, -0.25), complex(0.25, 0.9), complex(-0.1, 0.9), complex(-0.1, 0.1), complex(-0.9, 0.1), complex(-0.9, -0.25)]
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
    z2.callout(complex(-0.05, 0.55), '0.075（壁厚15cmの半分）', dirs=(-60, -40, -80), fs=12, color=RED)
    z2.callout(complex(0.15, 0.0), '壁の中心線（壁心）', dirs=(90, 70, 110), fs=12)
    z2.callout(complex(-0.6, 0.1), '内側の線（内法）', dirs=(-90, -110, -70), fs=12, color=GREEN)
    z3 = Zu(axes[2], fontsize=13)
    z3.poly(P([(e - W, s - W) for e, s in F3]), color=GRAY, lw=1.0, ls=':', check=False)
    z3.poly(P([(0, 0), (11.85, 0), (11.85, 9.85), (0, 9.85)]), color=GREEN, lw=2.4, fill=GREEN, alpha=0.20)
    axes[2].set_title('内法：外まわりは両側で0.15短くなる', fontsize=16, weight='bold', color=GREEN)
    fit(axes[2], P(F3), margin=0.10, extra=ext, pad_aspect=True)
    dims(z3, P([(0, 0), (11.85, 0), (11.85, 9.85), (0, 9.85)]), ['11.85', '9.85', '11.85', '9.85'], fs=13)
    z3.free_text(B(6, 5), '12.00−0.15＝11.85\n10.00−0.15＝9.85', fs=13, color=GREEN)
    save(fig, [z, z2, z3], 'H20_dai22mon_zu14_kabeshin_uchinori')


def zu15():
    fig, axes = new_figure('PSは専有部分には入らない：内側線で囲むと、南の壁にくい込んだ欠けになる',
                           'PS（パイプスペース）は共用部分（図の（注）4）。一棟の床面積（120.00・131.00）には入っているが、（ロ）部分にも（イ）部分にも入らない。\n'
                           '（ロ）部分の3階部分は、PSを除いた形の内側線で囲む',
                           w=17, h=9, ncols=2)
    fig.subplots_adjust(top=0.84, bottom=0.15)
    ext = [xy(B(-2.2, -2.2)), xy(B(14.0, 12.0))]
    z = Zu(axes[0], fontsize=13)
    z.poly(P(F3), color=BLACK, lw=2.0, fill=BLUE, alpha=0.12)
    for ps in (PS_W, PS_E):
        z.poly(P(ps), color=RED, lw=1.6, fill=RED, alpha=0.6)
    axes[0].set_title('一棟の建物の3階（壁心 120.00㎡）', fontsize=16, weight='bold')
    fit(axes[0], P(F3), margin=0.10, extra=ext, pad_aspect=True)
    z.callout(B(6, 9.75), 'PS（共用部分）\n一棟の床面積には入る', dirs=(-90, -105, -75), fs=12.5, color=RED, dists=(55, 70, 85))
    z.free_text(B(6, 4.5), '12.00×10.00＝120.00', fs=14)
    z2 = Zu(axes[1], fontsize=13)
    z2.poly(P([(e - W, s - W) for e, s in F3]), color=GRAY, lw=1.0, ls=':', check=False)
    z2.poly(P(RO3), color=GREEN, lw=2.4, fill=GREEN, alpha=0.22)
    for ps in (PS_W, PS_E):
        z2.poly(P([(e - W, s - W) for e, s in ps]), color=RED, lw=1.0, ls=':', check=False)
    axes[1].set_title('（ロ）部分の3階部分（内法 116.14㎡）', fontsize=16, weight='bold', color=GREEN)
    fit(axes[1], P(F3), margin=0.10, extra=ext, pad_aspect=True)
    z2.callout(B(5.925, 9.6), 'PSは含めない\n（欠けになる）', dirs=(-90, -105, -75), fs=12.5, color=RED, dists=(55, 70, 85))
    z2.free_text(B(6, 4.5), '内側線で囲んだ形\n5.35×9.85＋1.15×9.35＋5.35×9.85', fs=13)
    save(fig, [z, z2], 'H20_dai22mon_zu15_ps_senyuu')


def zu16():
    fig, axes = new_figure('PSの欠けは、1.00のままではなく1.15に広がる',
                           '欠けを囲む壁の内側の線は、部屋の側（西側の壁は西へ、東側の壁は東へ）へ0.075ずつずれるので、欠けの幅は1.00＋0.15＝1.15。'
                           '\n奥行き0.50は、PSの北の壁と部屋の南の壁の線が同じ北向きにずれるので変わらない',
                           w=19, h=9.5, ncols=3, width_ratios=[1, 1.0, 1])
    fig.subplots_adjust(top=0.84, bottom=0.15)
    ext = [xy(B(-2.2, -2.2)), xy(B(14.0, 13.5))]
    z2 = Zu(axes[0], fontsize=13)
    bad = [(11.70, 9.85), (6.35, 9.85), (6.35, 9.35), (5.35, 9.35), (5.35, 9.85), (0, 9.85), (0, 0), (11.85, 0), (11.85, 9.85)]
    z2.poly(P(bad), color=ORANGE, lw=2.2, closed=False)
    z2.line(B(11.70, 9.85), B(11.85, 9.85), color=RED, lw=4)
    axes[0].set_title('誤り：欠けを1.00のまま 116.22㎡', fontsize=16, weight='bold', color=ORANGE)
    fit(axes[0], P(RO3), margin=0.10, extra=ext, pad_aspect=True)
    z2.edge_label(B(0, 0), B(11.85, 0), '11.85', B(6, 5), fs=13)
    z2.edge_label(B(0, 9.85), B(0, 0), '9.85', B(6, 5), fs=13)
    z2.callout(B(2.7, 9.85), '5.35', dirs=(-90, -110, -70), fs=13, dists=(28, 40, 55))
    z2.callout(B(5.85, 9.35), '1.00', dirs=(-90, -110, -70), fs=13, dists=(45, 60, 75))
    z2.callout(B(9.0, 9.85), '5.35', dirs=(-90, -110, -70), fs=13, dists=(28, 40, 55))
    z2.callout(B(11.78, 9.85), '0.15 合わない', dirs=(-110, -125, -140), fs=13, color=RED, dists=(55, 70, 85))
    z2.free_text(B(6, 4.5), '南：5.35＋1.00＋5.35＝11.70\n北：11.85\n→ 形が閉じない', fs=13, color=ORANGE)
    # 中央：PSの欠けの拡大（壁の内側の線のずれ）
    z1 = Zu(axes[1], fontsize=12)
    walls = [rect(-0.075, 9.575, 0.075, 10.0), rect(0.925, 9.575, 1.075, 10.0), rect(-1.0, 10.0 - 0.075, 2.1, 10.0 + 0.075)]
    # 横軸＝東（m）、縦軸＝南（m）。PSの西の壁の中心 e=0、東の壁の中心 e=1.0（壁心の欠けの幅1.00）、部屋の南の壁の中心 s=10.0
    z1.poly([B(-0.075, 9.5), B(0.075, 9.5), B(0.075, 10.0), B(-0.075, 10.0)], color=GRAY, lw=0, fill=GRAY, alpha=0.30, check=False)
    z1.poly([B(0.925, 9.5), B(1.075, 9.5), B(1.075, 10.0), B(0.925, 10.0)], color=GRAY, lw=0, fill=GRAY, alpha=0.30, check=False)
    z1.line(B(0, 9.5), B(0, 10.0), color=BLACK, lw=1.2, ls='-.')
    z1.line(B(1.0, 9.5), B(1.0, 10.0), color=BLACK, lw=1.2, ls='-.')
    z1.line(B(-1.2, 9.5), B(2.2, 9.5), color=BLACK, lw=1.2, ls='-.')
    z1.line(B(-1.2, 9.425), B(-0.075, 9.425), color=GREEN, lw=3)
    z1.line(B(-0.075, 9.425), B(-0.075, 10.0), color=GREEN, lw=3)
    z1.line(B(1.075, 10.0), B(1.075, 9.425), color=GREEN, lw=3)
    z1.line(B(1.075, 9.425), B(2.2, 9.425), color=GREEN, lw=3)
    z1.line(B(-0.075, 10.0), B(1.075, 10.0), color=GREEN, lw=1.2, ls=':')
    axes[1].set_title('PSの欠けの拡大（内側の線のずれ）', fontsize=16, weight='bold')
    fit(axes[1], [B(-1.2, 9.2), B(2.2, 10.3)], margin=0.12, pad_aspect=True)
    z1.callout(B(0.5, 9.75), '壁心 1.00 → 内法 1.15', dirs=(-90, -110, -70), fs=13, color=GREEN, dists=(45, 60, 75))
    z1.callout(B(-0.075, 9.7), '西の壁の内側の線\n西へ0.075', dirs=(180, 200, 160), fs=11.5, dists=(40, 55, 70))
    z1.callout(B(1.075, 9.7), '東の壁の内側の線\n東へ0.075', dirs=(0, 20, -20), fs=11.5, dists=(40, 55, 70))
    z1.callout(B(-0.6, 9.425), '奥行き0.50は変わらない', dirs=(110, 90, 130), fs=11.5, color=RED, dists=(40, 55, 70))
    z3 = Zu(axes[2], fontsize=13)
    z3.poly(P([(e - W, s - W) for e, s in F3]), color=GRAY, lw=1.0, ls=':', check=False)
    z3.poly(P(RO3), color=GREEN, lw=2.4, fill=GREEN, alpha=0.20)
    axes[2].set_title('正解：欠けは1.15に広がる 116.14㎡', fontsize=16, weight='bold', color=GREEN)
    fit(axes[2], P(RO3), margin=0.10, extra=ext, pad_aspect=True)
    z3.edge_label(B(0, 0), B(11.85, 0), '11.85', B(6, 5), fs=13)
    z3.edge_label(B(0, 9.85), B(0, 0), '9.85', B(6, 5), fs=13)
    z3.edge_label(B(11.85, 0), B(11.85, 9.85), '9.85', B(6, 5), fs=13)
    z3.callout(B(2.7, 9.85), '5.35', dirs=(-90, -110, -70), fs=13, dists=(28, 40, 55))
    z3.callout(B(5.925, 9.35), '1.15', dirs=(-90, -110, -70), fs=13, dists=(45, 60, 75))
    z3.callout(B(9.2, 9.85), '5.35', dirs=(-90, -110, -70), fs=13, dists=(28, 40, 55))
    z3.callout(B(6.5, 9.6), '0.50', dirs=(0, 20, -20), fs=13, dists=(40, 55, 70))
    z3.free_text(B(6, 4.5), '南：5.35＋1.15＋5.35＝11.85\n＝北の11.85', fs=13, color=GREEN)
    save(fig, [z2, z1, z3], 'H20_dai22mon_zu16_kake_ichi_ichigo')


def zu17():
    fig, axes = new_figure('（ロ）部分3階部分の床面積求積図（内法）',
                           '5.35×9.85＋1.15×9.35＋5.35×9.85＝116.1475→116.14㎡。\n点線は（ロ）部分の2階部分の位置（東の辺は西から5.85、南西の5.35×2.00ははみ出す部分）',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    for r, c in zip(RO3_S, [ORANGE, BLUE, PURPLE]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.25, check=False)
    z.line(B(5.35, 0), B(5.35, 9.35), color=GRAY, lw=1.0, ls=':')
    z.line(B(6.50, 0), B(6.50, 9.35), color=GRAY, lw=1.0, ls=':')
    z.poly(P(RO3), color=BLACK, lw=2.4)
    z.line(B(5.85, 0), B(5.85, 9.35), color=BLACK, lw=1.4, ls='--')
    z.poly(P([(5.35, 9.85), (5.35, 11.85), (0, 11.85), (0, 9.85)]), color=BLACK, lw=1.4, ls='--', closed=False)
    fit(ax, P(RO3), margin=0.18, extra=[xy(B(0, 13.8))], pad_aspect=True)
    z.north_arrow()
    z.free_text(B(2.675, 4.5), '5.35×9.85', fs=15)
    z.free_text(B(9.175, 4.5), '5.35×9.85', fs=15)
    z.free_text(B(2.675, 11.1), '2階部分の位置（点線）', fs=12)
    z.free_text(B(9.5, 13.3), '3階部分　床面積：116.14㎡', fs=17, weight='bold')
    dims(z, P(RO3), ['11.85', '9.85', '5.35', '', '', '', '5.35', '9.85'], fs=15, ref=B(6, 4.5))
    notch(z, 5.35, 6.50, 9.35, 9.85, '1.15', fs=15, down=(95, 110, 125), wdirs=(150, 135, 165))
    z.callout(B(6.2, 2.0), '1.15×9.35', dirs=(10, 0, 25), fs=14, dists=(70, 90, 110))
    save(fig, [z], 'H20_dai22mon_zu17_3kai_kyuuseki')


def zu18():
    def draw(ax, yh):
        k = 28.0   # 1m ＝ 28単位（壁の断面を大きく）
        def wall(cx, y, h):
            ax.add_patch(Rectangle((cx - 0.075 * k, y), 0.15 * k, h, facecolor=GRAY, alpha=0.35, edgecolor='none'))
            ax.plot([cx, cx], [y - 0.8, y + h + 0.8], color=BLACK, lw=1.4, ls='-.', zorder=4)
        def inner(x, y, h, col=GREEN):
            ax.plot([x, x], [y, y + h], color=col, lw=3.2, zorder=5)
        # 左：段差（同じ向きにずれる）
        x0 = 4
        txt(ax, 25, yh - 2.5, '段差：両端の壁の線が同じ向きにずれる', fs=15, weight='bold')
        y = 14
        c1, c2 = x0 + 8, x0 + 8 + 0.5 * k          # 壁心：東西の壁の中心（西から 5.50・6.00）
        wall(c1, y, 24); wall(c2, y, 24)
        # 北の部屋（西）：内側の線は、どちらも壁の西側（部屋の側＝西）へ0.075
        inner(c1 - 0.075 * k, y, 24); inner(c2 - 0.075 * k, y, 24)
        ax.annotate('', xy=(c1 - 0.075 * k, y + 31), xytext=(c2 - 0.075 * k, y + 31), arrowprops=dict(arrowstyle='<->', lw=1.6, color=GREEN))
        txt(ax, (c1 + c2) / 2 - 0.075 * k, y + 34, '壁心 0.50 ＝ 内法 0.50', fs=14.5, weight='bold', col=GREEN)
        txt(ax, c1 - 0.075 * k - 0.4, y - 4.5, '5.50の壁', fs=12.5, ha='right')
        txt(ax, c2 - 0.075 * k + 0.4, y - 4.5, '6.00の壁', fs=12.5, ha='left')
        # 右：欠け（反対向きにずれる）
        txt(ax, 75, yh - 2.5, '欠け：両端の壁の線が反対向きにずれる', fs=15, weight='bold')
        d1, d2 = 56 + 8, 56 + 8 + 1.0 * k
        wall(d1, y, 24); wall(d2, y, 24)
        inner(d1 - 0.075 * k, y, 24); inner(d2 + 0.075 * k, y, 24)
        ax.annotate('', xy=(d1 - 0.075 * k, y + 31), xytext=(d2 + 0.075 * k, y + 31), arrowprops=dict(arrowstyle='<->', lw=1.6, color=RED))
        txt(ax, (d1 + d2) / 2, y + 34, '壁心 1.00 → 内法 1.15', fs=14.5, weight='bold', col=RED)
        txt(ax, d1 - 0.075 * k - 0.4, y - 4.5, 'PSの西の壁', fs=12.5, ha='right')
        txt(ax, d2 + 0.075 * k + 0.4, y - 4.5, 'PSの東の壁', fs=12.5, ha='left')
    card_fig('2階部分の段差0.50と東の2.50は、壁心のまま変わらない', 'H20_dai22mon_zu18_dansa_kawaranai', draw,
             '段差0.50は、西の部屋と東の部屋の間の壁（中心6.00）とPSの西の壁（中心5.50）の差。どちらの内側の線も西へ0.075ずれるので、0.50のまま。\n'
             '3階の欠けは、欠けをはさむ2つの壁の内側の線が、お互いから離れる向きにずれるので広がる。')


def zu19():
    fig, axes = new_figure('（ロ）部分2階部分の床面積求積図（内法）',
                           '5.35×11.85＋0.50×9.35＝68.0725→68.07㎡。\n段差0.50と東の2.50は、両端の線が同じ向きにずれるので壁心のまま',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    for r, c in zip(RO2_S, [GREEN, ORANGE]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.25, check=False)
    z.line(B(5.35, 0), B(5.35, 9.35), color=GRAY, lw=1.0, ls=':')
    z.poly(P(RO2), color=BLACK, lw=2.4)
    fit(ax, P(RO2), margin=0.22, extra=[xy(B(-4.0, 0)), xy(B(10.0, 0))], pad_aspect=True)
    z.north_arrow()
    dims(z, P(RO2), ['5.85', '9.35', '', '2.50', '5.35', '11.85'], fs=15, ref=B(2.7, 6))
    z.callout(B(5.6, 9.35), '0.50', dirs=(-20, -35, -5), fs=15, dists=(45, 60, 75))
    z.free_text(B(2.675, 6.0), '5.35×11.85', fs=15)
    z.callout(B(5.6, 2.0), '0.50×9.35', dirs=(15, 30, 0), fs=14, dists=(50, 65, 80))
    z.free_text(B(2.9, 13.5), '2階部分　床面積：68.07㎡', fs=17, weight='bold')
    save(fig, [z], 'H20_dai22mon_zu19_2kai_kyuuseki')


# =====================================================================================
# 登記申請書（第4章）
# =====================================================================================
def zu21():
    def draw(ax, yh):
        txt(ax, 25, yh - 2.5, '登記識別情報（不動産登記令第8条第1項）', fs=15, weight='bold')
        rows = [('第1号', '所有権の登記がある土地の合筆', '必要', RED), ('第2号', '所有権の登記がある建物の合体による登記等', '必要', RED),
                ('第3号', '所有権の登記がある建物の合併', '必要', RED), ('', '建物の分割・区分（本問）\n→ この条文に載っていない', '不要', GREEN)]
        for i, (no, t, v, col) in enumerate(rows):
            y = yh - 8.5 - i * 8.2
            box(ax, 2, y - 3.6, 12, 7.2, no, col=GRAY, fs=13)
            box(ax, 14, y - 3.6, 25, 7.2, t, col=GRAY, fs=11.5, ha='left')
            box(ax, 39, y - 3.6, 8, 7.2, v, col=col, fs=14.5, weight='bold', tc=col)
        txt(ax, 75, yh - 2.5, '印鑑証明書（不動産登記規則第47条第3号イ（6））', fs=15, weight='bold')
        rows = [('合筆の登記', '必要', RED), ('合体による登記等', '必要', RED), ('建物の合併の登記', '必要', RED), ('建物の区分の登記（本問）', '不要', GREEN)]
        for i, (t, v, col) in enumerate(rows):
            y = yh - 8.5 - i * 8.2
            box(ax, 53, y - 3.6, 33, 7.2, t, col=GRAY, fs=13.5, ha='left')
            box(ax, 86, y - 3.6, 11, 7.2, v, col=col, fs=14.5, weight='bold', tc=col)
        box(ax, 6, 3, 88, 6.5, '区分は、名義人が自分の建物を登記の上で分けるだけ → 添付書類は 建物図面・各階平面図・代理権限証書の3つ', col=BLUE, fs=14, weight='bold')
    card_fig('登記識別情報と印鑑証明書は、合筆・合体・合併のときだけ', 'H20_dai22mon_zu21_shikibetsu_inkan', draw,
             '「所有権の登記がある建物だから登記識別情報と印鑑証明書が要る」は、合併の話。建物の区分には要らない。')


def zu22():
    def draw(ax, yh):
        txt(ax, 27, yh - 2.5, '区分する（本問）：両方に移記される', fs=15, weight='bold', col=GREEN)
        box(ax, 8, yh - 18, 38, 9, '区分前の甲建物\n（E銀行の抵当権　受付第13239号）', col=GRAY, fs=13.5)
        arrow(ax, (20, yh - 18), (14, yh - 24), col=GREEN)
        arrow(ax, (34, yh - 18), (40, yh - 24), col=GREEN)
        box(ax, 2, yh - 36, 24, 11, '（イ）\n抵当権も移記', col=BLUE, fs=13.5)
        box(ax, 28, yh - 36, 24, 11, '（ロ）\n抵当権も移記', col=GREEN, fs=13.5)
        txt(ax, 27, yh - 40.5, '登記官が移記する（不動産登記規則第130条第1項）\n→ 抵当権者の承諾は要らない', fs=13.5, col=GREEN, weight='bold')
        txt(ax, 76, yh - 2.5, '承諾が要る場合（本問ではない）', fs=15, weight='bold', col=GRAY)
        box(ax, 56, yh - 18, 40, 9, '抵当権のある建物を分筆するなど、\n抵当権を片方についてだけ消滅させたいとき', col=GRAY, fs=13)
        arrow(ax, (76, yh - 18), (76, yh - 24), col=GRAY)
        box(ax, 56, yh - 36, 40, 11, '抵当権者の承諾を証する情報を\n添付して、承諾に係る方だけ\n消滅した旨を登記する', col=GRAY, fs=13)
        txt(ax, 76, yh - 40.5, '（不動産登記法第54条第3項で準用する第40条）', fs=13, col=GRAY)
    card_fig('区分しても抵当権は両方に移記される：抵当権者の承諾書は要らない', 'H20_dai22mon_zu22_teitouken_shoudaku', draw,
             '承諾書が出てくるのは、抵当権をどちらかの建物について消滅させるときだけ。本問は、建物の抵当権が区分後の2個の建物にそのまま移記される。')


def zu23():
    def draw(ax, yh):
        for x, t, col in [(8, '（イ）部分', BLUE), (40, '（ロ）部分', GREEN)]:
            plan(ax, rect(0, 0, 8, 6), x, yh - 4, 2.6, fc=col, ec=BLACK, lw=1.6, alpha=0.30)
            txt(ax, x + 4 * 2.6, yh - 4 - 3 * 2.6, t, fs=14.5, weight='bold')
            txt(ax, x + 4 * 2.6, yh - 4 - 6 * 2.6 - 3, '1,000円', fs=17, weight='bold', col=col)
        txt(ax, 33, yh - 14, '＋', fs=30)
        txt(ax, 71, yh - 14, '＝', fs=30)
        box(ax, 74, yh - 20, 24, 12, '金2,000円', col=RED, fs=22, weight='bold', tc=RED)
        box(ax, 5, 3, 90, 12.5, '建物の分割・区分・合併の登記は、登記後の建物1個につき1,000円（登録免許税法別表第一の一（十三）イ・ロ）\n'
            '問1で申請書に書くのは（ロ）部分だけでも、この申請で生まれる区分建物は（イ）と（ロ）の2個', col=BLUE, fs=14)
        txt(ax, 50, 20, '誤り：（ロ）部分だけ数えて1,000円', fs=14, col=RED, weight='bold')
    card_fig('登録免許税は、区分後の建物の個数×1,000円', 'H20_dai22mon_zu23_touroku_menkyozei', draw,
             '表示に関する登記は原則として登録免許税がかからないが、建物の分割・区分・合併は課税される。個数は、申請書に書く行の数ではなく区分後の建物の数。')


def zu24():
    def draw(ax, yh):
        box(ax, 3, yh - 20, 44, 17, '建物（家屋番号5番6）\n所有権の登記名義人\n平野大輔さん（単独）', col=BLUE, fs=15.5, weight='bold')
        txt(ax, 25, yh - 24, '区分の登記の申請人になれる（不動産登記法第54条第1項）', fs=13.5, col=BLUE, weight='bold')
        txt(ax, 25, yh - 30, '申請人：A市C町六丁目2番3号　平野大輔', fs=14.5, weight='bold')
        box(ax, 53, yh - 12, 22, 9, '大輔さん\n持分4分の3', col=BLUE, fs=14)
        box(ax, 75, yh - 12, 22, 9, '友子さん\n持分4分の1', col=GRAY, fs=14)
        txt(ax, 75, yh - 15.5, '土地（5番6）の共有者', fs=13.5)
        box(ax, 53, yh - 31, 44, 12, '友子さんは、土地の共有者であって\n建物の所有権の登記名義人ではない\n→ 申請人にならない', col=RED, fs=14, tc=RED, weight='bold')
        arrow(ax, (86, yh - 19), (86, yh - 24), col=RED)
    card_fig('申請人は建物の所有権の登記名義人だけ：土地の共有者は申請人にならない', 'H20_dai22mon_zu24_shinseinin', draw,
             '敷地権で土地も関係するが、申請するのは建物の区分の登記。建物の登記名義人（大輔さん）だけが申請人。\n住所は住居表示の「2番3号」、建物の所在は地番の「5番地6」と書き分ける。')


def zu25():
    def draw(ax, yh):
        txt(ax, 25, yh - 2.5, '一棟の建物の表示：壁心のまま転写', fs=15.5, weight='bold', col=GREEN)
        plan(ax, F1, 8, yh - 7, 1.9, fc=BLUE, ec=BLACK, lw=1.6, alpha=0.18)
        txt(ax, 8 + 6 * 1.9, yh - 7 - 6 * 1.9, '1階 131.00\n2階 131.00\n3階 120.00', fs=14.5, weight='bold')
        txt(ax, 25, 13.5, '登記記録の床面積（壁の中心線で囲む）を\nそのまま書き写す。内法で測り直さない', fs=13.5, col=GREEN)
        txt(ax, 75, yh - 2.5, '区分した建物の表示：内法で測り直す', fs=15.5, weight='bold', col=RED)
        plan(ax, RO3, 58, yh - 7, 1.9, fc=GREEN, ec=BLACK, lw=1.6, alpha=0.25)
        txt(ax, 58 + 6 * 1.9, yh - 7 - 4.5 * 1.9, '2階部分 68.07\n3階部分 116.14', fs=14.5, weight='bold')
        txt(ax, 75, 13.5, '専有部分だけが壁の内側線で囲んだ面積', fs=13.5, col=RED)
        box(ax, 12, 1.2, 76, 7.2, '区分建物でも、一棟の建物の床面積は一棟全体の壁心（共用部分を含む外形）で測る', col=BLUE, fs=14, weight='bold')
    card_fig('内法で測るのは専有部分だけ：一棟の建物の表示は登記記録の壁心のまま', 'H20_dai22mon_zu25_ittou_hyouji', draw,
             '同じ申請書の中で、一棟の建物の表示は壁心（登記記録の転写）、区分した建物の表示は内法。\n区分前の数字を半分にして書いても、専有部分の内法とは違う。')


def zu26():
    def draw(ax, yh):
        box(ax, 30, yh - 10, 40, 8, '敷地の地番　5番6（1筆）', col=GRAY, fs=16, weight='bold')
        arrow(ax, (50, yh - 10), (50, yh - 16))
        box(ax, 22, yh - 24, 56, 8, '1筆の土地の上に2個以上の建物 → 地番に支号を付ける\n（不動産登記事務取扱手続準則第79条第2号・第8号）', col=BLUE, fs=13.5)
        arrow(ax, (36, yh - 24), (26, yh - 30), col=BLUE)
        arrow(ax, (64, yh - 24), (74, yh - 30), col=GREEN)
        box(ax, 8, yh - 40, 36, 9, '（イ）部分　5番6の1', col=BLUE, fs=16, weight='bold')
        box(ax, 56, yh - 40, 36, 9, '（ロ）部分　5番6の2', col=GREEN, fs=16, weight='bold')
        txt(ax, 74, 3.0, '申請書：『（ロ）C町六丁目5番6の2』（図面の符号と地番区域を冠する）', fs=14, col=GREEN, weight='bold')
        txt(ax, 26, 3.0, '問題には予定の家屋番号が書かれていない', fs=14, col=GRAY)
    card_fig('家屋番号は、敷地の地番に支号を付けて決める', 'H20_dai22mon_zu26_kaoku_bangou', draw,
             '区分建物の家屋番号は、問題に予定が書かれていなければ、1筆の土地の上に2個の建物があるので「5番6の1」「5番6の2」とする。\n'
             '土地の地番「5番6」・建物の所在「5番地6」・家屋番号「5番6の2」は別の書き方。')


def zu27():
    def draw(ax, yh):
        txt(ax, 25, yh - 2.5, '一棟の建物：3階建', fs=15.5, weight='bold')
        elev(ax, 8, 10, 2.9, ELEV_H20, floor_h=3.4)
        txt(ax, 25, 5.2, '鉄筋コンクリート造合金メッキ鋼板ぶき3階建', fs=13)
        txt(ax, 75, yh - 2.5, '（ロ）部分：2階と3階の2つの階', fs=15.5, weight='bold', col=GREEN)
        elev(ax, 58, 10, 2.9, [('1階', []), ('2階', [(0, 6, '（ロ）', GREEN)]), ('3階', [(0, 12, '（ロ）', GREEN)])], floor_h=3.4)
        ax.add_patch(Rectangle((58, 10), 12 * 2.9, 3.4, facecolor='none', edgecolor=GRAY, lw=1.2, ls='--'))
        txt(ax, 58 + 6 * 2.9, 10 + 1.7, '1階はない', fs=12.5, col=GRAY)
        txt(ax, 75, 5.2, '構造の階数は専有部分そのものの階の数　→　2階建', fs=14, col=RED, weight='bold')
    card_fig('専有部分の構造の階数は、（ロ）部分そのものの階の数（2階建）', 'H20_dai22mon_zu27_kaisuu', draw,
             '一棟の「3階建」を写さない。（ロ）部分は2階と3階にだけあるので「2階建」で、床面積も「2階部分」「3階部分」と書く。')


def zu28():
    def draw(ax, yh):
        oy = yh - 36
        txt(ax, 25, yh - 3, '縦割り（令和3年度の（イ）部分）', fs=15, weight='bold', col=GRAY)
        elev(ax, 10, oy, 1.9, [('1階', [(0, 8, '（イ）', BLUE), (8, 16, '（ロ）', GRAY)]), ('2階', [(0, 8, '（イ）', BLUE), (8, 16, '（ロ）', GRAY)])],
             floor_h=4.0)
        top = oy + 2 * 4.0 * 1.9
        ax.add_patch(MPoly([(10, top), (10 + 8 * 1.9, top), (10 + 4 * 1.9, top + 5)], closed=True, facecolor=BLUE, alpha=0.3, edgecolor=BLACK, lw=1.8))
        txt(ax, 25, oy - 7, '1階から屋根まで丸ごと　→　屋根の種類まで書く\n「鉄骨造スレートぶき2階建」', fs=13.5, col=GRAY)
        txt(ax, 75, yh - 3, '階層的な区分（本問の（ロ）部分）', fs=15, weight='bold', col=GREEN)
        elev(ax, 60, oy, 1.7, ELEV_H20, floor_h=3.0)
        txt(ax, 75, oy - 7, '上下の区分が入っている　→　屋根の種類は書かない\n「鉄筋コンクリート造2階建」（準則第81条第3項）', fs=13.5, col=GREEN, weight='bold')
    card_fig('屋根の種類を書くのは縦割り、書かないのは階層的な区分', 'H20_dai22mon_zu28_yane', draw,
             '準則第81条第3項は「建物を階層的に区分してその一部を1個の建物とする場合」は屋根の種類を記録しなくてよい、と定める。\n'
             '一棟の「合金メッキ鋼板ぶき」を（ロ）部分の構造に写さない。')


def zu29():
    def draw(ax, yh):
        items = [(2, '報告的登記\n（新築・増築・滅失など）', '現地で起きた事実を届け出る', '日付を書く\n「（工事完了の日）新築」', BLUE),
                 (35, '形成的登記\n（区分・分割・合併）', '登記されて初めて効果が生じる', '日付を書かない\n「5番6から区分」', RED),
                 (68, '敷地権の表示の原因', '区分建物になったときに生じる権利', '日付を書く\n「平成20年8月24日敷地権」', GREEN)]
        for x, h, why, ans, col in items:
            box(ax, x, yh - 11, 30, 10, h, col=col, fs=14, weight='bold')
            arrow(ax, (x + 15, yh - 11), (x + 15, yh - 15), col=col)
            box(ax, x, yh - 24, 30, 9, why, col=col, fs=12.5)
            arrow(ax, (x + 15, yh - 24), (x + 15, yh - 28), col=col)
            box(ax, x, yh - 40, 30, 11, ans, col=col, fs=14, weight='bold', tc=col)
        txt(ax, 50, 3, '誤り：『平成20年8月24日5番6から区分』　→　日付を消して『5番6から区分』', fs=14.5, col=RED, weight='bold')
    card_fig('区分の原因には日付を書かない：区分は形成的登記', 'H20_dai22mon_zu29_genin_hizuke', draw,
             '登記より前に「区分した日」という事実はないので、区分の原因は日付なし。敷地権の表示の原因は、敷地権が生じた日（区分の登記を申請した日）を書く。')


def zu30():
    fig, axes = new_figure('（イ）部分の床面積（敷地権の割合を出すため。申請書には書かない）',
                           '1階の2つの住戸の間の壁は、同じ（イ）部分の中の壁なので引かない（住戸ごとに引くと 68.07＋57.37＝125.44 の誤り）。\n'
                           '（イ）部分 126.84＋57.37＝184.21㎡＝（ロ）部分 68.07＋116.14＝184.21㎡ → 床面積の割合は2分の1ずつ',
                           w=19, h=10.5, ncols=2, width_ratios=[1.35, 0.8])
    fig.subplots_adjust(top=0.85, bottom=0.15)
    z = Zu(axes[0], fontsize=13)
    for r, c in zip(I1_S, [ORANGE, BLUE, PURPLE]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.25, check=False)
    z.line(B(5.35, 0), B(5.35, 9.35), color=GRAY, lw=1.0, ls=':')
    z.line(B(6.50, 0), B(6.50, 9.35), color=GRAY, lw=1.0, ls=':')
    z.poly(P(I1), color=BLACK, lw=2.4)
    z.line(B(5.925, 0), B(5.925, 9.35), color=RED, lw=1.8, ls='--')
    axes[0].set_title('1階部分：126.84㎡', fontsize=17, weight='bold')
    fit(axes[0], P(I1), margin=0.10, extra=[xy(B(-1.5, 13.8))], pad_aspect=True)
    z.north_arrow()
    dims(z, P(I1), ['11.85', '9.85', '5.35', '', '', '2.50', '5.35', '11.85'], fs=13, ref=B(6, 4.5))
    z.callout(B(6.50, 9.60), '0.50', dirs=(-40, -25, -55), fs=13, dists=(45, 60, 75))
    z.callout(B(5.925, 9.35), '1.15', dirs=(-80, -70, -90), fs=13, dists=(60, 75, 90))
    z.free_text(B(2.675, 7.0), '5.35×11.85', fs=13)
    z.callout(B(6.2, 3.5), '1.15×9.35', dirs=(20, 35, 5), fs=12, dists=(70, 90, 110))
    z.free_text(B(9.175, 7.0), '5.35×9.85', fs=13)
    z.free_text(B(2.7, 3.0), '赤の点線＝住戸の間の壁\n同じ専有部分の中の壁は\n引かない', fs=12.5, color=RED)
    z2 = Zu(axes[1], fontsize=13)
    for r, c in zip(I2_S, [ORANGE, BLUE]):
        z2.poly(P(r), color=c, lw=0, fill=c, alpha=0.25, check=False)
    z2.line(B(0.50, 0), B(0.50, 9.35), color=GRAY, lw=1.0, ls=':')
    z2.poly(P(I2), color=BLACK, lw=2.4)
    axes[1].set_title('2階部分（東の住戸）：57.37㎡', fontsize=17, weight='bold')
    fit(axes[1], P(I1), margin=0.10, extra=[xy(B(-1.5, 13.8))], pad_aspect=True)
    dims(z2, P(I2), ['5.85', '9.85', '5.35', '', '', '9.35'], fs=13, ref=B(3.2, 4.5))
    z2.callout(B(0.50, 9.60), '0.50', dirs=(-55, -40, -70), fs=13, dists=(40, 55, 70))
    z2.callout(B(0.25, 9.35), '0.50', dirs=(-125, -140, -110), fs=13, dists=(40, 55, 70))
    z2.free_text(B(3.175, 4.5), '5.35×9.85', fs=13)
    z2.callout(B(0.25, 3.0), '0.50×9.35', dirs=(20, 35, 5), fs=12, dists=(45, 60, 75))
    save(fig, [z, z2], 'H20_dai22mon_zu30_i_bubun_kyuuseki')


def zu31():
    def draw(ax, yh):
        txt(ax, 50, yh - 2.5, '土地（5番6）の所有権 ＝ 1', fs=16, weight='bold')
        ax.add_patch(Rectangle((8, yh - 14), 60, 8, facecolor=BLUE, alpha=0.30, edgecolor=BLACK, lw=2))
        ax.add_patch(Rectangle((68, yh - 14), 20, 8, facecolor=GRAY, alpha=0.30, edgecolor=BLACK, lw=2))
        txt(ax, 38, yh - 10, '平野大輔さん　4分の3', fs=16, weight='bold')
        txt(ax, 78, yh - 10, '平野友子さん　4分の1', fs=14.5)
        txt(ax, 78, yh - 17.5, '専有部分を持たない\n→ 敷地権にならない', fs=12.5, col=RED)
        arrow(ax, (38, yh - 14), (38, yh - 20), col=BLUE)
        txt(ax, 38, yh - 21.5, '区分すると、専有部分と分離して処分できない敷地権になる', fs=13.5, col=BLUE)
        txt(ax, 38, yh - 25.5, '（建物の区分所有等に関する法律第22条第1項本文・共有の場合）', fs=12.5, col=BLUE)
        ax.add_patch(Rectangle((8, yh - 38), 30, 8, facecolor=BLUE, alpha=0.30, edgecolor=BLACK, lw=2))
        ax.add_patch(Rectangle((38, yh - 38), 30, 8, facecolor=GREEN, alpha=0.30, edgecolor=BLACK, lw=2))
        txt(ax, 23, yh - 34, '（イ）部分　8分の3', fs=15.5, weight='bold')
        txt(ax, 53, yh - 34, '（ロ）部分　8分の3', fs=15.5, weight='bold')
        txt(ax, 38, yh - 41.5, '4分の3 × 床面積の割合2分の1（184.21：184.21）＝ 8分の3', fs=15, weight='bold', col=RED)
        txt(ax, 85, yh - 34, '8分の3＋8分の3＋4分の1＝1', fs=12.5)
    card_fig('敷地権になるのは、土地の共有持分のうち大輔さんの4分の3だけ', 'H20_dai22mon_zu31_shikichiken_mochibun', draw,
             '敷地権の割合は、土地全体に対する割合。「2分の1」と書くのは、土地を大輔さん1人で持っているときの答え。\n'
             '床面積の数字のまま書くなら147368分の55263（4分の3に36842分の18421をかけたもの）で、約分すれば8分の3と同じ。')


def zu34():
    def draw(ax, yh):
        box(ax, 22, yh - 11, 56, 9, '建物の抵当権の登記と、敷地権になった土地の持分の抵当権の登記が\n『登記の目的・受付年月日と受付番号・登記原因とその日付』すべて同一か', col=PURPLE, fs=13.5, weight='bold')
        arrow(ax, (36, yh - 11), (24, yh - 19), col=BLUE)
        txt(ax, 24, yh - 15, 'はい（同一）', fs=14, col=BLUE, weight='bold', ha='right')
        arrow(ax, (64, yh - 11), (76, yh - 19), col=RED)
        txt(ax, 76, yh - 15, 'いいえ（別物）', fs=14, col=RED, weight='bold', ha='left')
        box(ax, 2, yh - 33, 44, 13, '土地の側の抵当権の登記を\n職権で抹消する\n（不動産登記規則第123条第1項ただし書・第2項）', col=BLUE, fs=14.5, weight='bold')
        box(ax, 54, yh - 33, 44, 13, '建物の抵当権の登記に\n『建物のみに関する旨』を付記する\n（同条第1項本文）', col=RED, fs=14.5)
        txt(ax, 24, yh - 37.5, '本問：平成19年5月4日受付第13239号、原因は平成19年5月4日金銭消費貸借同日設定\n→ 全部同じ → 抹消', fs=13.5, col=BLUE, weight='bold')
        txt(ax, 76, yh - 37.5, '藍子の誤答：付記（本問は同一なので付記はしない）', fs=13.5, col=RED)
    card_fig('土地の乙区：「建物のみに関する旨」の付記ではなく、同一なら抹消', 'H20_dai22mon_zu34_fuki_massho', draw,
             '建物の区分の登記には、同規則第130条第3項で第123条が準用される。抹消されても抵当権は消えず、敷地権付き区分建物の抵当権の登記が\n'
             '敷地権についてされた登記としての効力を持つ（不動産登記法第73条第1項）。')


def zu35():
    def draw(ax, yh):
        txt(ax, 25, yh - 2.5, '区分の登記の前', fs=16, weight='bold', col=GRAY)
        txt(ax, 75, yh - 2.5, '区分の登記の後', fs=16, weight='bold', col=GREEN)
        box(ax, 2, yh - 21, 46, 17, '権利部（甲区）\n所有権　共有者\n平野大輔　持分4分の3\n平野友子　持分4分の1', col=GRAY, fs=13.5)
        box(ax, 2, yh - 40, 46, 17, '権利部（乙区）\n抵当権（平野大輔持分について）\n平成19年5月4日受付第13239号\nE銀行　共同担保目録（へ）第80号', col=GRAY, fs=13.5)
        arrow(ax, (49, yh - 12), (51, yh - 12), col=GREEN)
        box(ax, 52, yh - 21, 46, 17, '権利部（甲区）\n平野大輔持分4分の3が敷地権である旨\n（一棟の建物の所在・構造・床面積、\n登記の年月日とともに記録）', col=GREEN, fs=13.5, weight='bold')
        box(ax, 52, yh - 40, 46, 17, '権利部（乙区）\n抵当権の登記を職権で抹消\n（抹消する旨とその年月日を記録）\n→ 建物の抵当権の登記が、敷地権の分も公示', col=RED, fs=13.5)
        arrow(ax, (49, yh - 31), (51, yh - 31), col=RED)
    card_fig('問3：区分の登記がされると、土地の登記記録はこう変わる', 'H20_dai22mon_zu35_tochi_kiroku', draw,
             '甲区には敷地権である旨の登記（不動産登記法第46条、規則第119条第1項）。乙区には、建物の抵当権と同一の抵当権の登記の職権抹消\n'
             '（規則第130条第3項で準用する第123条第2項）。')


# ---- 本番で解く順番 ----
def zu37():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    setup_font()
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　床面積のいらない欄と問3を先に、作図は（ロ）部分の求積の直後に', fontsize=22, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '問1〜3と\n問題文の注', '（ロ）部分のみ・\n土地の登記記録', BLUE),
        ('②', '床面積の\nいらない欄\nと問3', '目的・添付・申請人・\n一棟・構造・原因', BLUE),
        ('③', '地積で\n距離を確認', '320.5532…\n→320.55', GREEN),
        ('④', '寸法の\n累計メモ', '内法は\n0.075内側', RED),
        ('⑤', '（ロ）部分\nの求積', '68.07・\n116.14', RED),
        ('⑥', '各階平面図\n→建物図面', '（その3）の\n左→右', RED),
        ('⑦', '（イ）部分と\n敷地権の割合', '184.21＝184.21\n→8分の3', GRAY),
    ]
    w, h, gap = 12.2, 42, 1.8
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 22), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 22 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
        ax.text(x + w / 2, 22 + h / 2 - 4, t, ha='center', va='center', fontsize=15)
        ax.text(x + w / 2, 18, ran, ha='center', va='top', fontsize=13, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, 43), xytext=(x + w + 0.2, 43),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + (w + gap) - gap / 2, 76, '求積をしなくても書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 2 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 4.5 * (w + gap) - gap / 2, 76, 'いちばん時間を食う（PSの欠けは1.15）', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 6 * (w + gap) - gap, 72), xytext=(1 + 3 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '（イ）部分は答案に書かないが、敷地権の割合に必要。住戸の間の壁は引かず、184.21同士で2分の1。\n'
             '土地は平野大輔4分の3・平野友子4分の1の共有なので、敷地権の割合は4分の3×2分の1＝8分の3',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'H20_dai22mon_zu37_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[固定配置] 解く順番\n  →', path)


FIGS = [zu01, zu02, zu03, zu04, zu05, zu06, zu07, zu08, zu09, zu10, zu11, zu12, zu13, zu14, zu15, zu16, zu17, zu18, zu19, zu20,
        zu21, zu22, zu23, zu24, zu25, zu26, zu27, zu28, zu29, zu30, zu31, zu34, zu35, zu37]

if __name__ == '__main__':
    for f in FIGS:
        if not ONLY or any(o in f.__name__ for o in ONLY):
            f()
    print('重なり合計（座標の図）:', len(PROBLEMS))
