"""令和7年度 第22問（建物）の解説図5枚を、辺長・頂点座標から作図してPNGに書き出す。

`../prompt_R7_dai22mon_kaisetsuzu.md` の図1〜図5どおり。作図の共通部品は `tools/zu_helpers.py`。
建物の座標は (東, 南) で持ち、zu_helpers の (北, 東) には P() で変換する（北 ＝ −南）。
実行: python3 note-articles-Kijyutsu/R7/Q22/zu/draw_R7_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, BLACK, GRAY, RED, BLUE, ORANGE, GREEN,  # noqa: E402
                        PURPLE)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []


def P(e, s):
    """(東, 南) の点を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(-s, e)


def rect(e0, s0, e1, s1):
    return [P(e0, s0), P(e1, s0), P(e1, s1), P(e0, s1)]


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


# ---- 敷地・建物の配置（調査図素図の距離から組み立てた模式。敷地の幅30.00は新築倉庫の2.5＋25.50＋2.0と一致） ----
SITE = rect(0, 0, 30, 27.5)
BOUNDARY = (P(0, 9.5), P(30, 9.5))              # 425番6（北）と425番5（南）の境
OLD_MAIN = rect(1.5, 13.0, 11.5, 26.0)          # 主である建物 10.00×13.00（西1.5、南1.5）
FUGOU2 = [P(2, 2), P(21, 2), P(21, 8.5), P(7, 8.5), P(7, 11.5), P(2, 11.5)]   # 符号2の1階（西2.0、北2.0）
NOTCH = rect(2, 8.5, 7, 11.5)                   # 取り壊した張り出し 5.00×3.00
FUGOU2_AFTER = rect(2, 2, 21, 8.5)
SHUEI = rect(24, 23.0, 28, 25.5)                # 守衛所 4.00×2.50（東2.0、南2.0）
SOUKO = [P(2.5, 11.5), P(28, 11.5), P(28, 20.5), P(18, 20.5), P(18, 18.0), P(2.5, 18.0)]  # 新築倉庫（西2.5、東2.0、南7.0）


def site_panel(ax, title):
    z = Zu(ax, fontsize=12)
    z.poly(SITE, color=BLACK, lw=1.6)
    z.line(*BOUNDARY, color=BLACK, lw=1.2, ls='--')
    ax.set_title(title, fontsize=16, weight='bold', pad=10)
    return z


def site_labels(z):
    z.free_text(P(31, 4.75), '425番6', fs=11, color=GRAY, ha='left')
    z.free_text(P(31, 18.5), '425番5', fs=11, color=GRAY, ha='left')
    z.free_text(P(15, 29.3), '道路（100－10）', fs=11, color=GRAY)
    z.free_text(P(15, -1.6), '（425－9）', fs=11, color=GRAY)
    z.free_text(P(-1.0, 13.75), '（425－3）', fs=11, color=GRAY, ha='right')


def zu01():
    fig, axes = new_figure('建物の変遷（家屋番号425番５の中身の移り変わり）',
                           '配置は調査図素図の筆界からの距離をもとにした模式図。斜線は取り壊した部分。家屋番号425番５の登記記録は最後まで1つのまま続く',
                           w=18, h=7.6, ncols=3)
    fig.subplots_adjust(top=0.84)
    zs = []
    # 工事前
    z = site_panel(axes[0], '工事前')
    z.poly(OLD_MAIN, color=BLACK, fill=BLUE)
    z.poly(FUGOU2, color=BLACK, fill=ORANGE)
    z.poly(SHUEI, color=BLACK, fill=GREEN)
    z.free_text(centroid(OLD_MAIN), '主である建物\n事務所・倉庫', fs=11)
    z.free_text(P(12, 5.2), '符号2　倉庫', fs=11)
    z.callout(centroid(SHUEI), '符号4　守衛所', dirs=(120, 150, 90), fs=11)
    site_labels(z)
    zs.append(z)
    # 本件工事1の後
    z = site_panel(axes[1], '本件工事1の後（2月6日申請）')
    z.poly(OLD_MAIN, color=GRAY, ls='--', lw=1.4)
    hatch(axes[1], OLD_MAIN)
    hatch(axes[1], NOTCH, color=RED)
    z.poly(NOTCH, color=RED, ls='--', lw=1.4)
    z.poly(FUGOU2_AFTER, color=BLACK, fill=BLUE)
    z.poly(SHUEI, color=BLACK, fill=GREEN)
    z.free_text(centroid(OLD_MAIN), '1月21日\n取壊し', fs=11, color=GRAY,
                bbox=dict(boxstyle='round,pad=0.25', fc='white', ec='none'))
    z.free_text(P(11.5, 5.25), '主である建物（元の符号2）\n事務所・倉庫', fs=10)
    z.callout(centroid(NOTCH), '1月31日 一部取壊し', dirs=(-35, -50, -20, -65), dists=(70, 95, 120), fs=11, color=RED)
    z.callout(centroid(SHUEI), '符号4　守衛所', dirs=(120, 150, 90), fs=11)
    site_labels(z)
    zs.append(z)
    # 本件工事2の後
    z = site_panel(axes[2], '本件工事2の後（10月23日申請）')
    z.poly(FUGOU2_AFTER, color=BLACK, fill=BLUE)
    z.poly(SOUKO, color=BLACK, fill=ORANGE)
    z.poly(SHUEI, color=BLACK, fill=GREEN)
    z.free_text(P(12, 5.2), '主である建物\n（耐震補強は登記しない）', fs=11)
    z.free_text(P(12, 15.0), '符号5　新築倉庫\n10月7日新築', fs=11)
    z.callout(centroid(SHUEI), '符号4は9月25日取壊し\n符号6として10月17日新築', dirs=(150, 120, 170), fs=11)
    site_labels(z)
    zs.append(z)
    for ax in axes:
        fit(ax, SITE, margin=0.06, extra=[xy(P(-8, -3)), xy(P(37, 31))], pad_aspect=True)
    save(fig, zs, 'R7_dai22mon_zu01_hensen')


def dims(z, pts, labels, fs=13):
    """多角形の各辺に寸法（None は書かない）を外側に書く。"""
    c = centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs)


def zu02():
    fig, axes = new_figure('符号2の1階：取り壊した張り出し部分を読み取る',
                           '配置図の斜線（取り壊した部分）は、符号2の1階の南西の張り出し5.00×3.00にぴったり重なる。138.50−15.00＝123.50（2階と同じ）',
                           w=16, h=7, ncols=2)
    fig.subplots_adjust(top=0.84)
    before = [P(0, 0), P(19, 0), P(19, 6.5), P(5, 6.5), P(5, 9.5), P(0, 9.5)]
    main = rect(0, 0, 19, 6.5)
    notch = rect(0, 6.5, 5, 9.5)
    assert round(area(before), 2) == 138.50 and round(area(notch), 2) == 15.00
    z = Zu(axes[0], fontsize=14)
    z.poly(main, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(notch, color=RED, lw=0, fill=RED, alpha=0.35, check=False)
    z.poly(before, color=BLACK, lw=2.2)
    dims(z, before, ['19.00m', '6.50m', '14.00m', None, '5.00m', '9.50m'])
    z.free_text(P(5.5, 9.2), '3.00m', fs=14, ha='left')
    z.free_text(centroid(main), '工事前 1階：138.50㎡', fs=14)
    z.callout(centroid(notch), 'この部分を取り壊す\n5.00×3.00＝15.00㎡', dirs=(-30, -60, 0), fs=13, color=RED)
    axes[0].set_title('【工事前】', fontsize=17, weight='bold')
    fit(axes[0], before, margin=0.2, extra=[xy(P(30, 16))], pad_aspect=True)
    z2 = Zu(axes[1], fontsize=14)
    z2.poly(main, color=BLACK, lw=2.2, fill=BLUE)
    z2.poly(notch, color=GRAY, lw=1.4, ls='--')
    dims(z2, main, ['19.00m', '6.50m', None, None])
    z2.free_text(centroid(main), '工事後 1階：123.50㎡\n（2階と同じ）', fs=14)
    z2.callout(centroid(notch), '撤去済み', dirs=(-30, -60, 0), fs=13, color=GRAY)
    axes[1].set_title('【工事後】', fontsize=17, weight='bold')
    fit(axes[1], before, margin=0.2, extra=[xy(P(30, 16))], pad_aspect=True)
    save(fig, [z, z2], 'R7_dai22mon_zu02_fugou2_ichibu_torikowashi')


# ---- 新築倉庫（符号5） ----
F1 = [P(0, 0), P(25.5, 0), P(25.5, 9), P(15.5, 9), P(15.5, 6.5), P(0, 6.5)]
F1_W, F1_E = rect(0, 0, 15.5, 6.5), rect(15.5, 0, 25.5, 9)
HASHIRA = [P(0.3, 0.3), P(25.2, 0.3), P(25.2, 8.7), P(15.8, 8.7), P(15.8, 6.2), P(0.3, 6.2)]
F2 = [P(0, 0), P(25.5, 0), P(25.5, 9), P(23.5, 9), P(23.5, 6.5), P(7, 6.5), P(7, 4.5), P(0, 4.5)]
F2_A, F2_B, F2_C = rect(23.5, 0, 25.5, 9), rect(7, 0, 23.5, 6.5), rect(0, 0, 7, 4.5)
VOID_SW, VOID_SE = rect(0, 4.5, 7, 6.5), rect(15.5, 6.5, 23.5, 9)
assert round(area(F1), 2) == 190.75 and round(area(F2), 2) == 156.75 and round(area(HASHIRA), 2) == 170.41
assert round(area(VOID_SW) + area(VOID_SE), 2) == 34.00


def zu03():
    fig, axes = new_figure('新築倉庫1階：柱の中心の寸法だけで測る誤り',
                           '注3：数値は柱の中心間の距離と壁の中心間の距離。A部分拡大図のとおり柱の中心と壁の中心は0.30ずれているので、両端に0.30を足して壁の中心線で測る',
                           w=16, h=7, ncols=2)
    fig.subplots_adjust(top=0.84)
    z = Zu(axes[0], fontsize=13)
    z.poly(F1, color=GRAY, lw=1.2, ls='--')
    z.poly(HASHIRA, color=RED, lw=2.4, fill=RED, alpha=0.15)
    dims(z, HASHIRA, ['24.90m', '8.40m', '9.40m', None, '15.50m', '5.90m'])
    z.free_text(P(12, 3.2), '柱の中心で囲んだ形\n170.41㎡', fs=14, color=RED)
    axes[0].set_title('誤り：柱芯の寸法だけを足す（24.90m）', fontsize=17, weight='bold', color=RED)
    fit(axes[0], F1, margin=0.2, extra=[xy(P(12, -9))], pad_aspect=True)
    z2 = Zu(axes[1], fontsize=13)
    z2.poly(HASHIRA, color=GRAY, lw=1.2, ls='--')
    z2.poly(F1, color=BLUE, lw=2.4, fill=BLUE, alpha=0.15)
    dims(z2, F1, ['25.50m', '9.00m', '10.00m', None, '15.50m', '6.50m'])
    for e, s in [(0.3, 0.3), (25.2, 0.3), (25.2, 8.7), (15.8, 8.7), (15.8, 6.2), (0.3, 6.2)]:
        axes[1].add_patch(Rectangle((e - 0.3, -s - 0.3), 0.6, 0.6, fill=False, ec=BLACK, lw=1.2, zorder=4))
    z2.free_text(P(12, 3.2), '壁の中心線で囲んだ形\n190.75㎡', fs=14, color=BLUE)
    z2.callout(P(25.2, 0.3), '□＝柱。柱の中心と壁の中心は0.30ずれる', dirs=(110, 125, 95, 140), fs=12)
    axes[1].set_title('正解：両端に0.30を足す（25.50m）', fontsize=17, weight='bold', color=GREEN)
    fit(axes[1], F1, margin=0.2, extra=[xy(P(12, -9))], pad_aspect=True)
    save(fig, [z, z2], 'R7_dai22mon_zu03_hashirashin_ayamari')


def zu04():
    fig, axes = new_figure('新築倉庫（符号5）1階の床面積求積図',
                           '西側15.50×6.50＝100.75　＋　東側10.00×9.00＝90.00　＝　190.75㎡（東側が南へ2.50m深いL字形）',
                           w=16, h=8)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(F1_W, color=BLUE, lw=0, fill=BLUE, check=False)
    z.poly(F1_E, color=ORANGE, lw=0, fill=ORANGE, alpha=0.35, check=False)
    z.line(P(15.5, 0), P(15.5, 6.5), color=GRAY, lw=1.2, ls='--')
    z.poly(F1, color=BLACK, lw=2.4)
    dims(z, F1, ['25.50m', '9.00m', '10.00m', '2.50m', '15.50m', '6.50m'])
    z.free_text(P(7.75, 3.25), '西側\n15.50×6.50＝100.75', fs=15)
    z.free_text(P(20.5, 4.5), '東側\n10.00×9.00＝90.00', fs=15)
    z.free_text(P(12.75, 11.6), '新築倉庫 1階 床面積：190.75㎡', fs=16, weight='bold')
    fit(ax, F1, margin=0.12, extra=[xy(P(12.75, 12.8))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R7_dai22mon_zu04_souko_1kai_kyuuseki')


def zu05():
    fig, axes = new_figure('新築倉庫（符号5）2階の床面積求積図',
                           '腰高壁は壁なので吹き抜けとの境はその中心線。片面が格子手すりの階段は階段室といえず、吹き抜けと一体で床面積に入れない（190.75−34.00＝156.75）',
                           w=16, h=8.5)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(F1, color=GRAY, lw=1.2, ls='--', check=False)
    for pts, c in [(F2_A, ORANGE), (F2_B, BLUE), (F2_C, GREEN)]:
        z.poly(pts, color=c, lw=0, fill=c, alpha=0.28, check=False)
    hatch(ax, VOID_SW)
    hatch(ax, VOID_SE)
    z.line(P(7, 0), P(7, 4.5), color=GRAY, lw=1.0, ls=':')
    z.line(P(23.5, 0), P(23.5, 6.5), color=GRAY, lw=1.0, ls=':')
    z.poly(F2, color=BLACK, lw=2.4)
    z.line(P(0, 4.5), P(7, 4.5), color=PURPLE, lw=4.0)
    z.line(P(7, 4.5), P(7, 6.5), color=PURPLE, lw=4.0)
    z.line(P(15.5, 6.5), P(23.5, 6.5), color=PURPLE, lw=4.0)
    z.line(P(23.5, 6.5), P(23.5, 9), color=PURPLE, lw=4.0)
    z.edge_label(P(0, 0), P(25.5, 0), '25.50m', centroid(F2))
    z.free_text(P(3.5, 2.25), 'C\n7.00×4.50\n＝31.50', fs=13)
    z.free_text(P(15.25, 3.25), 'B\n16.50×6.50＝107.25', fs=14)
    z.callout(P(24.5, 7.5), 'A（東端の廊下の列）\n2.00×9.00＝18.00', dirs=(-20, 0, -40), fs=13)
    z.free_text(P(3.5, 5.5), '吹き抜け 7.00×2.00', fs=12, color=BLACK,
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none'))
    z.free_text(P(19.5, 7.75), '吹き抜け＋階段 8.00×2.50', fs=12, color=BLACK,
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none'))
    z.free_text(P(11.25, 7.9), '紫の線＝腰高壁', fs=12, color=PURPLE)
    z.free_text(P(12.75, 11.8), '新築倉庫 2階 床面積：156.75㎡', fs=16, weight='bold')
    fit(ax, F1, margin=0.12, extra=[xy(P(12.75, 13.0)), xy(P(33, 5))], pad_aspect=True)
    z.north_arrow()
    save(fig, [z], 'R7_dai22mon_zu05_souko_2kai_kyuuseki')


if __name__ == '__main__':
    zu01()
    zu02()
    zu03()
    zu04()
    zu05()
    print('重なり合計:', len(PROBLEMS))
