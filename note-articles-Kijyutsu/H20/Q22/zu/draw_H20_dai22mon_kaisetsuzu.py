"""平成20年度 第22問（建物）の解説図9枚を、頂点座標から作図してPNGに書き出す。

`../prompt_H20_dai22mon_kaisetsuzu.md` の図1〜図9どおり。作図の共通部品は `tools/zu_helpers.py`。
建物の座標は (東, 南) で持ち（原点は一棟の建物の北西の角の、壁の中心線の交点）、zu_helpers の (北, 東) には
B() で変換する（北 ＝ −南）。内法の図（図4〜図8）は、その区分建物の北西の角の内側の線を原点にした座標で描く。
敷地は座標値一覧表がないので、配置図の距離（外壁まで。図の（注）3）と壁厚15cm（図の（注）2）から組み立てた座標を使う。
実行: python3 note-articles-Kijyutsu/H20/Q22/zu/draw_H20_dai22mon_kaisetsuzu.py [出力フォルダ]
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
W = 0.075   # 壁厚15cmの半分（図の（注）2）


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
# 誤り：PSの欠けを1.00のまま
assert round(11.85 * 9.85 - 1.00 * 0.50, 4) == 116.2225 and round(5.35 + 1.00 + 5.35, 2) == 11.70

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


# ---- 図1：区分の全体像 ----
def zu01():
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
    save(fig, zs, 'H20_dai22mon_zu01_kubun_zentaizou')


# ---- 図2：敷地の辺長確認図 ----
def zu02():
    fig, axes = new_figure('本件土地（5番6）の辺長確認図（作図チェック用）',
                           '(18.15－2÷12.15＋19.15＋3÷12.15)÷2×17.15＝320.5532…→320.55㎡（登記記録の地積と一致）。\n'
                           '距離は外壁から（図の（注）3）、外壁は壁の中心線の0.075外側。辺長は建物図面には書かない',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(SITE, color=BLACK, lw=2.4, fill=BLUE, alpha=0.08)
    outer = [(-W, -W), (12 + W, -W), (12 + W, 10 + W), (5.5 + W, 10 + W), (5.5 + W, 12 + W), (-W, 12 + W)]
    z.poly(P(outer), color=GRAY, lw=1.6, fill=GRAY, alpha=0.25)
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
    save(fig, [z], 'H20_dai22mon_zu02_shikichi_henchou')


# ---- 図3：建物図面（ロ）の完成形 ----
def zu03():
    fig, axes = new_figure('（ロ）建物図面の完成形（縮尺1/500で描く内容）',
                           '（ロ）部分の地上の最低階（2階部分）を実線、一棟の建物の1階を点線（規則第82条第1項・準則第52条第2項）。\n'
                           '家屋番号 C町六丁目5番6の2、建物の所在 A市C町六丁目5番地6。敷地の辺長は書かない',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    site_frame(z)
    z.poly(P(F1), color=BLACK, lw=1.6, ls='--')
    z.poly(P(RO2_WALL), color=BLACK, lw=3.0)
    fit(ax, SITE, margin=0.10, extra=[xy(B(-7.5, -6.5)), xy(B(24.5, 21.5))], pad_aspect=True)
    z.north_arrow()
    dim_line(z, B(0, north_s(0)), B(0, 0), '2.00', dirs=(160, 180, 140))
    dim_line(z, B(E_W, 3.0), B(0, 3.0), '2.00', dirs=(90, 110, 70))
    dim_line(z, B(E_W, 11.0), B(0, 11.0), '2.00', dirs=(90, 110, 70))
    dim_line(z, B(1.5, 12), B(1.5, S_S), '4.00', dirs=(0, 20, -20))
    z.free_text(B(2.9, 5.5), '（ロ）', fs=17, weight='bold')
    z.free_text(B(9.5, 13.2), '5－6', fs=16)
    neighbours(z)
    z.free_text(B(6.5, S_S + 4.6), '建物の存する部分　2階、3階', fs=17, weight='bold')
    save(fig, [z], 'H20_dai22mon_zu03_tatemono_zumen')


# ---- 図4：（ロ）部分3階部分の誤り比較図 ----
def zu04():
    fig, axes = new_figure('（ロ）部分3階部分の床面積：登記記録の120.00か、内法か',
                           '区分建物の床面積は壁その他の区画の内側線で囲まれた部分（規則第115条）。PSは共用部分（図の（注）4）。\n'
                           '欠けを囲む壁の線も部屋の側へずれるので、PSの欠けの幅は1.00→1.15に広がる（奥行き0.50は変わらない）',
                           w=19, h=9.5, ncols=3)
    fig.subplots_adjust(top=0.84, bottom=0.15)
    ext = [xy(B(-2.2, -2.2)), xy(B(14.0, 13.5))]
    # 誤り①
    z = Zu(axes[0], fontsize=13)
    z.poly(P(F3), color=RED, lw=2.2, fill=RED, alpha=0.16)
    for ps in (PS_W, PS_E):
        z.poly(P(ps), color=RED, lw=1.2)
        hatch(axes[0], P(ps), RED)
    axes[0].set_title('誤り①：登記記録の120.00㎡', fontsize=16, weight='bold', color=RED)
    fit(axes[0], P(F3), margin=0.10, extra=ext, pad_aspect=True)
    dims(z, P(F3), ['12.00', '10.00', '12.00', '10.00'], fs=13)
    z.free_text(B(6, 4.5), '12.00×10.00\n＝120.00㎡\n（壁心・PSも入る）', fs=13, color=RED)
    z.callout(B(6, 9.75), 'PSは共用部分', dirs=(-60, -40, -80), fs=12, color=RED)
    # 誤り②
    z2 = Zu(axes[1], fontsize=13)
    bad = [(11.70, 9.85), (6.35, 9.85), (6.35, 9.35), (5.35, 9.35), (5.35, 9.85), (0, 9.85), (0, 0), (11.85, 0), (11.85, 9.85)]
    z2.poly(P(bad), color=ORANGE, lw=2.2, closed=False)
    z2.line(B(11.70, 9.85), B(11.85, 9.85), color=RED, lw=4)
    axes[1].set_title('誤り②：欠けを1.00のまま 116.22㎡', fontsize=16, weight='bold', color=ORANGE)
    fit(axes[1], P(RO3), margin=0.10, extra=ext, pad_aspect=True)
    z2.edge_label(B(0, 0), B(11.85, 0), '11.85', B(6, 5), fs=13)
    z2.edge_label(B(0, 9.85), B(0, 0), '9.85', B(6, 5), fs=13)
    z2.callout(B(2.7, 9.85), '5.35', dirs=(-90, -110, -70), fs=13, dists=(28, 40, 55))
    z2.callout(B(5.85, 9.35), '1.00', dirs=(-90, -110, -70), fs=13, dists=(45, 60, 75))
    z2.callout(B(9.0, 9.85), '5.35', dirs=(-90, -110, -70), fs=13, dists=(28, 40, 55))
    z2.callout(B(11.78, 9.85), '0.15 合わない', dirs=(-110, -125, -140), fs=13, color=RED, dists=(55, 70, 85))
    z2.free_text(B(6, 4.5), '南：5.35＋1.00＋5.35＝11.70\n北：11.85\n→ 形が閉じない', fs=13, color=ORANGE)
    # 正解
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
    save(fig, [z, z2, z3], 'H20_dai22mon_zu04_3kai_ayamari_hikaku')


# ---- 図5：（ロ）部分3階部分の求積図 ----
def zu05():
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
    save(fig, [z], 'H20_dai22mon_zu05_3kai_kyuuseki')


# ---- 図6：（ロ）部分2階部分の求積図 ----
def zu06():
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
    save(fig, [z], 'H20_dai22mon_zu06_2kai_kyuuseki')


# ---- 図7：各階平面図（ロ）の完成形 ----
def zu07():
    fig, axes = new_figure('（ロ）各階平面図の完成形（縮尺1/250で描く内容）',
                           '内法の辺長・求積・床面積を書く。\n3階部分には、（ロ）部分のいちばん下の階（2階部分）の位置を点線で重ねる（解答例どおり）',
                           w=18, h=11, ncols=2)
    fig.subplots_adjust(top=0.86, bottom=0.12)
    ext = [xy(B(-3.0, -1.5)), xy(B(21.0, 13.5))]
    z = Zu(axes[0], fontsize=13)
    z.poly(P(RO2), color=BLACK, lw=2.2)
    axes[0].set_title('2階部分', fontsize=17, weight='bold', loc='left')
    fit(axes[0], P(RO2), margin=0.06, extra=ext, pad_aspect=True)
    dims(z, P(RO2), ['5.85', '9.35', '', '2.50', '5.35', '11.85'], fs=13, ref=B(2.7, 6))
    z.callout(B(5.6, 9.35), '0.50', dirs=(-20, -35, -5), fs=13, dists=(40, 55, 70))
    z.free_text(B(15.0, 5.0), '求積\n5.35×11.85＝63.3975\n0.50× 9.35＝ 4.6750\n　　　計　68.0725\n床面積　68.07㎡', fs=13, ha='center',
                multialignment='left')
    z2 = Zu(axes[1], fontsize=13)
    z2.poly(P(RO3), color=BLACK, lw=2.2)
    z2.line(B(5.85, 0), B(5.85, 9.35), color=BLACK, lw=1.2, ls='--')
    z2.poly(P([(5.35, 9.85), (5.35, 11.85), (0, 11.85), (0, 9.85)]), color=BLACK, lw=1.2, ls='--', closed=False)
    axes[1].set_title('3階部分', fontsize=17, weight='bold', loc='left')
    fit(axes[1], P(RO3), margin=0.06, extra=ext, pad_aspect=True)
    dims(z2, P(RO3), ['11.85', '9.85', '5.35', '', '', '', '5.35', '9.85'], fs=13, ref=B(6, 4.5))
    notch(z2, 5.35, 6.50, 9.35, 9.85, '1.15', fs=13, down=(80, 95, 110), wdirs=(150, 135, 165))
    z2.free_text(B(17.0, 5.0), '求積\n5.35×9.85＝52.6975\n1.15×9.35＝10.7525\n5.35×9.85＝52.6975\n　　計　116.1475\n床面積　116.14㎡', fs=13,
                 ha='center', multialignment='left')
    save(fig, [z, z2], 'H20_dai22mon_zu07_kakukai_heimenzu')


# ---- 図8：（イ）部分の求積図（敷地権の割合のため） ----
def zu08():
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
    z.callout(B(5.925, 1.5), '住戸の間の壁\n（同じ専有部分の中の壁は引かない）', dirs=(60, 45, 75), fs=12, color=RED,
              dists=(90, 110, 130))
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
    save(fig, [z, z2], 'H20_dai22mon_zu08_i_bubun_kyuuseki')


# ---- 図9：本番で解く順番 ----
def zu09():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
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
    ax.text(1 + 4.5 * (w + gap) - gap / 2, 76, 'いちばん時間を食う（PSの欠けは1.15）', ha='center', fontsize=15, color=RED,
            weight='bold')
    ax.annotate('', xy=(1 + 6 * (w + gap) - gap, 72), xytext=(1 + 3 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '（イ）部分は答案に書かないが、敷地権の割合に必要。住戸の間の壁は引かず、184.21同士で2分の1。\n'
             '土地は平野大輔4分の3・平野友子4分の1の共有なので、敷地権の割合は4分の3×2分の1＝8分の3',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'H20_dai22mon_zu09_toku_junban.png')
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
