"""令和7年度 第22問（建物）の解説図11枚を、辺長・頂点座標から作図してPNGに書き出す。

`../prompt_R7_dai22mon_kaisetsuzu.md` の図1〜図11どおり（番号は記事の挿入順。番号は管理用で、画像の中には書かない）。
作図の共通部品は `tools/zu_helpers.py`。
2026-10-08、最新の執筆指示書との照らし直しで、本文に対して足りなかった4枚（図1 滅失登記と表題部変更登記の比較、
図2 建物ごとの時系列メモ、図4 注の仕分け、図6 符号の付け方）を足し、図の番号を記事の挿入順に振り直した
（旧図1→図3、旧図2→図5、旧図3→図7、旧図4→図8、旧図5→図9、旧図6→図10、旧図7→図11。中身は変えていない。
図10だけは、答案用紙の第3欄の左上の「第3欄」の印刷を描き足した）。
新しい4枚は座標を使わない固定配置の図なので、check_fixed で文字の重なりと図の外へのはみ出しを調べ、目視でも確かめる。
図10（各階平面図の完成形）は、答案用紙の第3欄の枠の中に、符号5・符号6を同じ縮尺で描く。
枠の形は試験の答案用紙（`../touan_youshi/R7_dai22mon_touan_youshi.pdf` の2ページ目）で確かめた形：1枚の枠の左半分・右半分とも
各階平面図（右の「建物図面」の文字は二重線で消されている）、家屋番号（「（略）」と印刷）と建物の所在の欄は右上に1つだけ、
枠の下に作成者（略）・（令和7年○月○日作成）・縮尺1/250と、申請人（略）・縮尺1/250。
建物の座標は (東, 南) で持ち、zu_helpers の (北, 東) には P() で変換する（北 ＝ −南）。
実行: python3 note-articles-Kijyutsu/R7/Q22/zu/draw_R7_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle, FancyBboxPatch  # noqa: E402
from matplotlib.colors import to_rgba  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)

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


def zu03():
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
    save(fig, zs, 'R7_dai22mon_zu03_hensen')


def dims(z, pts, labels, fs=13):
    """多角形の各辺に寸法（None は書かない）を外側に書く。"""
    c = centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs)


def zu05():
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
    save(fig, [z, z2], 'R7_dai22mon_zu05_fugou2_ichibu_torikowashi')


# ---- 新築倉庫（符号5） ----
F1 = [P(0, 0), P(25.5, 0), P(25.5, 9), P(15.5, 9), P(15.5, 6.5), P(0, 6.5)]
F1_W, F1_E = rect(0, 0, 15.5, 6.5), rect(15.5, 0, 25.5, 9)
HASHIRA = [P(0.3, 0.3), P(25.2, 0.3), P(25.2, 8.7), P(15.8, 8.7), P(15.8, 6.2), P(0.3, 6.2)]
F2 = [P(0, 0), P(25.5, 0), P(25.5, 9), P(23.5, 9), P(23.5, 6.5), P(7, 6.5), P(7, 4.5), P(0, 4.5)]
F2_A, F2_B, F2_C = rect(23.5, 0, 25.5, 9), rect(7, 0, 23.5, 6.5), rect(0, 0, 7, 4.5)
VOID_SW, VOID_SE = rect(0, 4.5, 7, 6.5), rect(15.5, 6.5, 23.5, 9)
assert round(area(F1), 2) == 190.75 and round(area(F2), 2) == 156.75 and round(area(HASHIRA), 2) == 170.41
assert round(area(VOID_SW) + area(VOID_SE), 2) == 34.00


def zu07():
    fig, axes = new_figure('新築倉庫1階：柱の中心の寸法だけで測る誤り',
                           '〔調査・測量〕の（注）3：数値は柱の中心間の距離と壁の中心間の距離。\nA部分拡大図のとおり柱の中心と壁の中心は0.30ずれるので、両端に0.30を足して壁の中心線で測る',
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
    # 柱の四角は add_patch で直接描くので、重なり検査に入るよう中心を markers に登録してから文字を置く（基本フォームの注意）
    for e, s in [(0.3, 0.3), (25.2, 0.3), (25.2, 8.7), (15.8, 8.7), (15.8, 6.2), (0.3, 6.2)]:
        axes[1].add_patch(Rectangle((e - 0.3, -s - 0.3), 0.6, 0.6, fill=False, ec=BLACK, lw=1.2, zorder=4))
        z2.markers.append(xy(P(e, s)))
    dims(z2, F1, ['25.50m', '9.00m', '10.00m', None, '15.50m', '6.50m'])
    z2.free_text(P(12, 3.2), '壁の中心線で囲んだ形\n190.75㎡', fs=14, color=BLUE)
    z2.callout(P(25.2, 0.3), '□＝柱。柱の中心と壁の中心は0.30ずれる', dirs=(110, 125, 95, 140), fs=12)
    axes[1].set_title('正解：両端に0.30を足す（25.50m）', fontsize=17, weight='bold', color=GREEN)
    fit(axes[1], F1, margin=0.2, extra=[xy(P(12, -9))], pad_aspect=True)
    save(fig, [z, z2], 'R7_dai22mon_zu07_hashirashin_ayamari')


def zu08():
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
    save(fig, [z], 'R7_dai22mon_zu08_souko_1kai_kyuuseki')


def zu09():
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
    save(fig, [z], 'R7_dai22mon_zu09_souko_2kai_kyuuseki')


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.01
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


INK = '#1a3a8f'   # 記入（濃い青）
FW, FH = 18, 13   # 図10の大きさ（インチ）
SCALE = 0.19      # 図10の縮尺（1メートルあたりのインチ）。符号5と符号6を同じ縮尺で描く（縮尺1/250の図の中の大きさの比をそろえる）


def same_scale(ax, center):
    """パネルの大きさと SCALE から表示範囲を決める（パネルが違っても1メートルの長さが同じになる）。"""
    pos = ax.get_position()
    w, h = pos.width * FW / SCALE, pos.height * FH / SCALE
    c = xy(center)
    fit(ax, [center], margin=0, extra=[(c[0] - w / 2, c[1] - h / 2), (c[0] + w / 2, c[1] + h / 2)], pad_aspect=True)


def zu10():
    """各階平面図の完成形（答案用紙の第3欄の枠の中。求積図とちがい塗り分けはしない）。"""
    setup_font()
    fig = plt.figure(figsize=(FW, FH), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図の完成形（答案用紙の第3欄・縮尺1/250で描く内容）', fontsize=22, weight='bold', y=0.975)
    # 答案用紙の第3欄（試験の答案用紙 ../touan_youshi/ の2ページ目の形）：1枚の大きな枠の左半分・右半分とも各階平面図
    # （右の「建物図面」の文字は二重線で消され、下に「各階平面図」）。家屋番号（印刷の「（略）」）の欄は枠の上の右寄り、
    # 建物の所在の欄は枠の中の右上に1つだけ。左右の境は枠の上下の短い目印だけ。
    # 枠の下に、左は作成者（略）・（令和7年○月○日作成）・縮尺1/250、右は申請人（略）・縮尺1/250
    FL, FR, FB, FT = 0.04, 0.96, 0.135, 0.86
    MID = 0.50
    cell(fig, FL, FB, FR, FT, lw=1.8)
    for y0, y1 in ((FT - 0.045, FT), (FB, FB + 0.045)):   # 左右の境の目印（上下の短い線）
        fig.add_artist(plt.Line2D([MID, MID], [y0, y1], transform=fig.transFigure, lw=1.8, color=BLACK))
    fig.text(FL + 0.003, FT + 0.045, '第3欄', ha='left', va='center', fontsize=16, weight='bold')   # 答案用紙の左上の印刷
    fig.text(0.27, FT + 0.018, '各　階　平　面　図', ha='center', va='center', fontsize=19)
    cell(fig, 0.529, FT, 0.601, FT + 0.045, '家屋番号', fs=15)
    cell(fig, 0.601, FT, 0.720, FT + 0.045, '（略）', fs=15)
    cell(fig, 0.529, FT - 0.045, 0.601, FT, '建物の所在', fs=15)
    cell(fig, 0.601, FT - 0.045, FR, FT, 'Y市K区A町三丁目425番地６、425番地５', fs=16, ha='left', color=INK)
    fig.text(0.815, FT + 0.038, '建　物　図　面', ha='center', va='center', fontsize=17)
    for dy in (0.0025, -0.0025):   # 「建物図面」の文字を二重線で消してある（答案用紙の印刷どおり）
        fig.add_artist(plt.Line2D([0.755, 0.875], [FT + 0.038 + dy, FT + 0.038 + dy], transform=fig.transFigure,
                                  lw=1.2, color=BLACK))
    fig.text(0.815, FT + 0.016, '各　階　平　面　図', ha='center', va='center', fontsize=17)

    def scale_cell(x0, x1):   # 縮尺の分数（1 と 250 を斜線で分ける印刷）
        fig.add_artist(plt.Line2D([x0 + 0.012, x1 - 0.012], [FB - 0.048, FB - 0.010], transform=fig.transFigure,
                                  lw=1.0, color=BLACK))
        fig.text(x0 + 0.030, FB - 0.016, '1', ha='center', va='center', fontsize=13)
        fig.text(x1 - 0.030, FB - 0.042, '250', ha='center', va='center', fontsize=13)
    BB = FB - 0.055
    cell(fig, FL, BB, 0.100, FB, '作　成　者', fs=14)
    cell(fig, 0.100, BB, 0.376, FB)
    fig.text(0.16, FB - 0.022, '（略）', ha='center', va='center', fontsize=14)
    fig.text(0.37, FB - 0.042, '（令和7年○月○日作成）', ha='right', va='center', fontsize=13)
    cell(fig, 0.376, BB, 0.407, FB, '縮尺', fs=13)
    cell(fig, 0.407, BB, 0.477, FB)
    scale_cell(0.407, 0.477)
    cell(fig, 0.523, BB, 0.584, FB, '申　請　人', fs=14)
    cell(fig, 0.584, BB, 0.859, FB, '（略）', fs=14)
    cell(fig, 0.859, BB, 0.890, FB, '縮尺', fs=13)
    cell(fig, 0.890, BB, FR, FB)
    scale_cell(0.890, FR)
    fig.text(0.5, 0.035, '壁の中心線の寸法（小数第2位まで。問題文の注4）で、符号5は1階・2階を書き分け、2階に1階の位置を点線で示す。'
             '各階の横に求積と床面積を書く。\n主である建物は問3のとおり省略してよい。枠と印刷の文字は試験の答案用紙の第3欄の形'
             '（家屋番号・作成者・申請人は「（略）」と印刷済み）',
             ha='center', va='center', fontsize=14, linespacing=1.6)
    A1 = fig.add_axes([0.05, 0.50, 0.30, 0.27])
    A2 = fig.add_axes([0.05, 0.17, 0.30, 0.29])
    A6 = fig.add_axes([0.52, 0.56, 0.16, 0.21])
    zs = []
    tables = [(A1, '符号5　1階', F1, ['25.50', '9.00', '10.00', '2.50', '15.50', '6.50'],
               '符号5　1階\n10.00×9.00＝90.0000\n15.50×6.50＝100.7500\n計　190.7500\n床面積　190.75㎡', (0.355, 0.635)),
              (A2, '符号5　2階', F2, ['25.50', '9.00', '2.00', '2.50', '16.50', None, '7.00', '4.50'],
               '符号5　2階\n2.00×9.00＝18.0000\n16.50×6.50＝107.2500\n7.00×4.50＝31.5000\n計　156.7500\n床面積　156.75㎡',
               (0.355, 0.315))]
    for ax, name, pts, labels, table, tpos in tables:
        z = Zu(ax, fontsize=12)
        ax.set_title(name, fontsize=16, weight='bold')
        same_scale(ax, P(12.75, 4.5))
        if name.endswith('2階'):
            z.poly(F1, color=BLACK, lw=1.3, ls='--')   # 1階の位置（点線）。重なり検査にも入れる
        z.poly(pts, color=BLACK, lw=2.4)
        dims(z, pts, labels, fs=12)
        if name.endswith('2階'):   # 南西の吹き抜けの東の辺（2.00）は、外側だと点線の1階の線にかかるので床の側に書く
            z.edge_label(pts[5], pts[6], '2.00', centroid(pts), fs=12, outward=False)
        zs.append(z)
        fig.text(tpos[0], tpos[1], table, ha='left', va='center', fontsize=14, linespacing=1.55)
    z = Zu(A6, fontsize=12)
    A6.set_title('符号6', fontsize=16, weight='bold')
    shuei = rect(0, 0, 4, 2.5)
    same_scale(A6, P(2, 1.25))
    z.poly(shuei, color=BLACK, lw=2.4)
    dims(z, shuei, ['4.00', '2.50', '4.00', '2.50'], fs=12)
    zs.append(z)
    fig.text(0.69, 0.665, '符号6\n4.00×2.50＝10.0000\n床面積　10.00㎡', ha='left', va='center', fontsize=14, linespacing=1.55)
    fig.text(0.52, 0.42, '・符号5と符号6は同じ縮尺（1/250）で描く\n'
             '・2階の点線は1階の位置（南西の吹き抜けと、\n　南東の吹き抜け＋階段の下にある1階の床）\n'
             '・主である建物（元の符号2）は省略してよい\n'
             '　（問3）', ha='left', va='center', fontsize=14, linespacing=1.6, color=GRAY)
    zs[0].north_arrow()
    assert round(area(F1), 4) == 190.75 and round(area(F2), 4) == 156.75 and round(area(shuei), 4) == 10.00
    save(fig, zs, 'R7_dai22mon_zu10_kakukai_heimenzu')


def zu11():
    """本番で解く順番（どこまで倉庫の求積なしで書けるか）。固定配置の図なので重なり検査の対象外。"""
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　倉庫の求積と作図は後に回す', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '問4の穴埋め', '第4欄 ア〜エ', BLUE),
        ('②', '建物ごとの\n時系列メモ', '事実関係を整理', BLUE),
        ('③', '問1の申請書', '第1欄\n（符号2は\n138.50−15.00）', BLUE),
        ('④', '問2の申請書', '第2欄\n（符号5の床面積\nだけ空ける）', GREEN),
        ('⑤', '倉庫の\n1階・2階の求積', '第2欄 符号5の\n床面積', RED),
        ('⑥', '問3の\n各階平面図', '第3欄\n符号5・符号6', RED),
        ('⑦', '見直し', '所在の順序・\n欄番号・符号', GRAY),
    ]
    w, h, gap = 12.2, 42, 1.8
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 22), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, 22 + h - 4, no, ha='center', va='top', fontsize=26, color=col, weight='bold')
        ax.text(x + w / 2, 22 + h / 2 - 3, t, ha='center', va='center', fontsize=17)
        ax.text(x + w / 2, 18, ran, ha='center', va='top', fontsize=14, color=col)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, 43), xytext=(x + w + 0.2, 43),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 2 * (w + gap) - gap / 2, 76, '倉庫の求積をしなくても書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 4 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 5 * (w + gap) - gap / 2, 76, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 6 * (w + gap) - gap, 72), xytext=(1 + 4 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '倉庫の2階は、吹き抜け・腰高壁・格子手すりの階段を図面で1つずつ確かめるので時間がかかる。\n'
             '先に第1欄・第2欄の大部分と第4欄を書いておけば、倉庫で時間が足りなくなっても申請書の点は取れている。',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'R7_dai22mon_zu11_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 解く順番（固定配置）\n  →', path)


# ======================================================================
# 2026-10-08追加：本文で説明しているのに図がなかった4枚（図1・図2・図4・図6）。座標を使わない固定配置の図
# ======================================================================

def fixed_figure(title, w=16, h=10, rect=(0.02, 0.04, 0.96, 0.86)):
    """固定配置の図（座標を使わない整理図）。横軸・縦軸とも 0〜100 の作業座標。"""
    setup_font()
    fig = plt.figure(figsize=(w, h), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle(title, fontsize=24, weight='bold', y=0.975)
    ax = fig.add_axes(list(rect))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    return fig, ax


def check_fixed(fig, name):
    """固定配置の図の重なり検査（文字どうしの重なりと、図の外へのはみ出し）。H25/Q22の作図スクリプトと同じ方法。
    zu_helpers の Zu は座標の図のためのもので、固定配置の図の文字は登録されないので、ここで図の全部の文字を調べる。"""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    texts = list(fig.texts)
    if fig._suptitle is not None and fig._suptitle not in texts:
        texts.append(fig._suptitle)
    for ax in fig.axes:
        texts += list(ax.texts) + [ax.title]
    texts = [t for t in texts if t.get_visible() and t.get_text().strip()]
    bbs = []
    for t in texts:
        bb = t.get_window_extent(r)
        if hasattr(t, 'get_bbox_patch') and t.get_bbox_patch() is not None:
            bb = t.get_bbox_patch().get_window_extent(r)
        bbs.append(bb)
    W, H = fig.bbox.width, fig.bbox.height
    probs = []
    for i, (t, bb) in enumerate(zip(texts, bbs)):
        if bb.x0 < 2 or bb.y0 < 2 or bb.x1 > W - 2 or bb.y1 > H - 2:
            probs.append(f'{name} 図の外へのはみ出し: {t.get_text()!r}')
        for t2, bb2 in zip(texts[i + 1:], bbs[i + 1:]):
            if bb.overlaps(bb2):
                probs.append(f'{name} 文字どうし: {t.get_text()!r} と {t2.get_text()!r}')
    print(f'[重なり検査] {name}（固定配置）: ' + ('問題なし' if not probs else f'{len(probs)}件'))
    for q in probs:
        print('   ', q)
    PROBLEMS.extend(probs)


def save_fixed(fig, name):
    check_fixed(fig, name)
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def rbox(ax, x, y, w, h, col, alpha=0.12, lw=1.8, ls='-'):
    """角の丸い枠（alpha は塗りの濃さ。0 なら塗らない）。"""
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.5', facecolor=to_rgba(col, alpha) if alpha else 'none',
                                edgecolor=col, lw=lw, ls=ls))


def vline(fig, x, y0=0.10, y1=0.86):
    fig.add_artist(plt.Line2D([x, x], [y0, y1], transform=fig.transFigure, color=GRAY, lw=1.2))


def _kiroku(ax, x, y, w, title, rows):
    """登記記録（表題部）の模式。rows: [(見出し, 中身, 状態, 色)]"""
    h = 9 + 13 * len(rows)
    ax.add_patch(Rectangle((x, y - h), w, h, fill=False, lw=2.0, ec=BLACK))
    ax.text(x + w / 2, y - 4.5, title, ha='center', va='center', fontsize=15, weight='bold')
    ax.plot([x, x + w], [y - 9, y - 9], color=BLACK, lw=1.2)
    for k, (head, body, state, col) in enumerate(rows):
        yy = y - 9 - 13 * k
        if k:
            ax.plot([x, x + w], [yy, yy], color=GRAY, lw=1.0)
        ax.text(x + 1.5, yy - 3.6, head, ha='left', va='center', fontsize=14)
        ax.text(x + 1.5, yy - 9.0, body, ha='left', va='center', fontsize=13, color=GRAY)
        ax.text(x + w - 1.5, yy - 6.5, state, ha='right', va='center', fontsize=14, color=col, weight='bold')
    return y - h


def zu01():
    """滅失登記と表題部変更登記の比較（この問題最大のわな）。固定配置の図。"""
    fig, ax = fixed_figure('主である建物がなくなっても、附属建物が残れば滅失登記ではない', w=17, h=11,
                           rect=(0.02, 0.11, 0.96, 0.77))
    cols = [(1, '誤り：建物滅失登記\n（不動産登記法第57条）', RED),
            (52, '正解：建物表題部変更登記\n（不動産登記法第51条第1項）', GREEN)]
    for x, t, col in cols:
        ax.text(x + 23.5, 95, t, ha='center', va='center', fontsize=18, weight='bold', color=col, linespacing=1.4)
    w = 47
    _kiroku(ax, 1, 86, w, '家屋番号425番５の登記記録',
            [('主である建物', '事務所・倉庫', '1月21日取壊し', RED), ('附属建物　符号2', '倉庫', '（見落とす）', GRAY),
             ('附属建物　符号4', '守衛所', '（見落とす）', GRAY)])
    _kiroku(ax, 52, 86, w, '家屋番号425番５の登記記録',
            [('主である建物', '事務所・倉庫', '1月21日取壊し', RED), ('附属建物　符号2', '倉庫', '主である建物に変更', GREEN),
             ('附属建物　符号4', '守衛所', '残る', GREEN)])
    res = [(1, RED, ['主である建物がなくなったから', '建物の全部がなくなったと考えて、建物滅失登記', '（符号2・符号4はまだ建っている）']),
           (52, GREEN, ['登記記録はそのまま続く（家屋番号も同じ）', '主である建物の欄：取壊し ＋ 符号2を書き起こして\n「主である建物に変更」',
                        '符号2の欄にも「主である建物に変更」\n（不動産登記事務取扱手続準則第102条）'])]
    for x, col, lines in res:
        rbox(ax, x + 0.5, 3, w - 1, 33, col, alpha=0.10)
        for k, t in enumerate(lines):
            ax.text(x + w / 2, 30 - 10.5 * k, t, ha='center', va='center', fontsize=14, weight='bold' if k == 1 else 'normal',
                    color=col if k == 1 else BLACK, linespacing=1.35)
    vline(fig, 0.5, 0.10, 0.90)
    fig.text(0.5, 0.06, '建物滅失登記は「1個の建物」の全部がなくなったときの登記。家屋番号425番５の建物は、主である建物と附属建物をまとめた1個の建物',
             ha='center', va='center', fontsize=15)
    fig.text(0.5, 0.025, '主である建物だけが消えたのは、その建物の登記事項（不動産登記法第44条第1項）が変わったということ → 表題部の変更の登記',
             ha='center', va='center', fontsize=15)
    save_fixed(fig, 'R7_dai22mon_zu01_messhitsu_hikaku')


def zu02():
    """建物ごとの時系列メモ（申請の期限つき）。固定配置の図。1月〜2月と9月〜11月だけを描き、間は省略する。"""
    import datetime as dt
    fig, ax = fixed_figure('建物ごとの時系列メモ　期限は「変更があった日から1月以内」', w=18, h=10.5,
                           rect=(0.02, 0.12, 0.96, 0.76))
    A0, A1, AX0, AX1 = dt.date(2025, 1, 14), dt.date(2025, 3, 4), 17.0, 55.0
    B0, B1, BX0, BX1 = dt.date(2025, 9, 20), dt.date(2025, 11, 22), 60.0, 99.0

    def X(m, d):
        t = dt.date(2025, m, d)
        if t <= A1:
            return AX0 + (t - A0).days * (AX1 - AX0) / (A1 - A0).days
        return BX0 + (t - B0).days * (BX1 - BX0) / (B1 - B0).days
    rows = [('主である建物', 80), ('符号2\n（1月21日から主）', 64), ('符号4（守衛所）', 48), ('新築倉庫（符号5）', 32),
            ('守衛所（符号6）', 16)]
    for t, y in rows:
        ax.text(0.5, y, t, ha='left', va='center', fontsize=14, weight='bold', linespacing=1.3)
        ax.plot([AX0, AX1], [y, y], color=GRAY, lw=0.8, alpha=0.5)
        ax.plot([BX0, BX1], [y, y], color=GRAY, lw=0.8, alpha=0.5)
    for (m, d), lab in [((2, 1), '2月'), ((3, 1), '3月'), ((10, 1), '10月'), ((11, 1), '11月')]:
        ax.plot([X(m, d)] * 2, [8, 88], color=GRAY, lw=0.8, ls=':')
        ax.text(X(m, d) + 0.4, 5, lab + '1日', ha='left', va='center', fontsize=12, color=GRAY)
    ax.text((AX0 + X(2, 1)) / 2, 5, '1月', ha='center', va='center', fontsize=12, color=GRAY)
    ax.text((BX0 + X(10, 1)) / 2, 5, '9月', ha='center', va='center', fontsize=12, color=GRAY)
    ax.text(57.5, 48, '3月〜9月は省略', ha='center', va='center', fontsize=12, color=GRAY, rotation=90)
    for (m, d), lab in [((2, 6), '2月6日 申請（問1）'), ((10, 23), '10月23日 申請（問2）')]:
        ax.plot([X(m, d)] * 2, [8, 90], color=BLUE, lw=2.0, ls='--')
        ax.text(X(m, d), 94, lab, ha='center', va='center', fontsize=15, weight='bold', color=BLUE)
    box = dict(boxstyle='round,pad=0.15', fc='white', ec='none')

    def event(m, d, y, text, col, below=False, deadline=None):
        x = X(m, d)
        if deadline:
            x2 = X(*deadline)
            ax.plot([x, x2], [y, y], color=col, lw=5, alpha=0.35, solid_capstyle='butt')
            ax.plot([x2, x2], [y - 2.2, y + 2.2], color=col, lw=2)
            ax.text(x2, y + 4.6, f'期限 {deadline[0]}月{deadline[1]}日', ha='right', va='center', fontsize=12, color=col, bbox=box)
        ax.plot([x], [y], 'o', color=col, ms=9, zorder=5)
        ax.text(x - 0.6, y - 4.6 if below else y + 4.6, text, ha='left', va='center', fontsize=13, color=col, bbox=box,
                weight='bold')
    event(1, 21, 80, '1月21日 取壊し', RED, deadline=(2, 21))
    event(1, 21, 64, '1月21日 主である建物に変更', ORANGE)
    event(1, 31, 64, '1月31日 種類変更・一部取壊し', ORANGE, below=True, deadline=(2, 28))
    event(10, 1, 64, '10月1日 耐震補強（登記しない）', GRAY, below=True)
    ax.text(AX0 + 1, 48 + 4.6, '本件工事1では変わらない', ha='left', va='center', fontsize=12, color=GRAY)
    event(9, 25, 48, '9月25日 取壊し', RED, deadline=(10, 25))
    event(10, 7, 32, '10月7日 新築', BLUE, deadline=(11, 7))
    event(10, 17, 16, '10月17日 新築', BLUE, deadline=(11, 17))
    fig.text(0.5, 0.065, '期限は不動産登記法第51条第1項の「変更があった日から1月以内」。初日は数えない（1月21日の取壊しは2月21日まで、1月31日の工事は2月28日まで）',
             ha='center', va='center', fontsize=14)
    fig.text(0.5, 0.025, '2件目の申請（10月23日）は、いちばん早い9月25日の取壊しの期限（10月25日）に間に合っている。全部終わるまで待つと1件目は期限切れ',
             ha='center', va='center', fontsize=14)
    save_fixed(fig, 'R7_dai22mon_zu02_jikeiretsu')


CHUU_MONDAI = [('注1', '行為は全て適法、書類も全て適法に作成', None),
               ('注2', '登記の申請は書面申請', '申請書の欄の名前どおり「添付書類」で書く'),
               ('注3', '各階平面図は250分の1の縮尺', '問3の各階平面図の縮尺'),
               ('注4', '各階平面図の距離は小数第2位まで', '問3の辺長（25.50・9.00 など）'),
               ('注5', '字画を明確に、訂正・加入・削除の書き方', None)]
CHUU_CHOUSA = [('（注）1', '距離の単位はメートル', None),
               ('（注）2', '調査図素図の（　）内は土地の地番', None),
               ('（注）3', '調査図素図の数値は筆界から外壁まで\n平面詳細図の数値は柱の中心間・壁の中心間',
                '倉庫は両端に0.30を足して壁の中心線で測る'),
               ('（注）4', '平面詳細図の隅は全て直角\n丸印は各階の重なる部分', '2階を1階に重ねる位置（各階平面図の点線）')]


def zu04():
    """注の仕分け図。固定配置の図。"""
    fig, ax = fixed_figure('注は2か所。番号がかぶるので「どちらの注か」を言い分ける', w=17, h=12.5,
                           rect=(0.02, 0.10, 0.96, 0.80))
    rbox(ax, 1, 3, 46, 85, BLUE, alpha=0.06)
    rbox(ax, 51, 3, 48, 85, ORANGE, alpha=0.06)
    ax.text(24, 96.5, '問題文の注1〜注5', ha='center', va='center', fontsize=20, weight='bold', color=BLUE)
    ax.text(24, 92.0, '（問4の語句群の後ろ。答案の作り方の決まり）', ha='center', va='center', fontsize=13, color=BLUE)
    ax.text(75, 96.5, '【調査・測量】の（注）1〜4', ha='center', va='center', fontsize=20, weight='bold', color=ORANGE)
    ax.text(75, 92.0, '（平面詳細図の後ろ。図面の読み方）', ha='center', va='center', fontsize=13, color=ORANGE)

    def rows(items, x, y0, col, wrap):
        y = y0
        for no, body, use in items:
            n = body.count('\n') + 1
            c = BLACK if use else GRAY
            ax.text(x, y, no, ha='left', va='top', fontsize=15, weight='bold', color=col if use else GRAY)
            ax.text(x + wrap, y, body, ha='left', va='top', fontsize=14, color=c, linespacing=1.4)
            y -= 4.4 * n
            if use:
                ax.text(x + wrap, y, '→ ' + use, ha='left', va='top', fontsize=14, color=col, weight='bold')
                y -= 4.4
            y -= 2.6
        return y
    rows(CHUU_MONDAI, 2.5, 85, BLUE, 4.5)
    y = rows(CHUU_CHOUSA, 52.5, 85, ORANGE, 7.0)
    # 建物配置図1の横の番号のない注
    ax.text(52.5, y - 1, '建物配置図1の（注）', ha='left', va='top', fontsize=15, weight='bold', color=PURPLE)
    ax.text(59.5, y - 5.4, '斜線部分は本件工事1で取り壊した部分', ha='left', va='top', fontsize=14)
    ax.text(59.5, y - 9.8, '→ 主である建物の全部と、符号2の南西の張り出し', ha='left', va='top', fontsize=14, weight='bold',
            color=PURPLE)
    # 同じ番号でも別の注になる例
    rbox(ax, 3.5, 7, 41, 24, RED, alpha=0.05, lw=1.4)
    ax.text(24, 27.5, '同じ「3」でも別の注', ha='center', va='center', fontsize=16, weight='bold', color=RED)
    ax.text(5, 20.5, '問題文の注3', ha='left', va='center', fontsize=15, weight='bold', color=BLUE)
    ax.text(21, 20.5, '縮尺（250分の1）', ha='left', va='center', fontsize=14)
    ax.text(5, 12.0, '〔調査・測量〕の（注）3', ha='left', va='center', fontsize=15, weight='bold', color=ORANGE)
    ax.text(27.5, 12.0, '寸法の測り方', ha='left', va='center', fontsize=14)
    fig.text(0.5, 0.055, '記事では「問題文の注4」「〔調査・測量〕の（注）3」のように、どちらの注かを必ず言い分ける',
             ha='center', va='center', fontsize=16, color=RED, weight='bold')
    fig.text(0.5, 0.02, '色付き＝この問題の答えに使う注（→の先が使う場面）、灰色＝本文では取り上げない注',
             ha='center', va='center', fontsize=14)
    save_fixed(fig, 'R7_dai22mon_zu04_chuu_shiwake')


def zu06():
    """符号の付け方（使い回さない・工事完了の順）。固定配置の図。"""
    fig, ax = fixed_figure('附属建物の符号は使い回さない。新しい附属建物は工事完了の順に5・6', w=17, h=9.5,
                           rect=(0.02, 0.13, 0.96, 0.74))
    cards = [('符号1', '取壊しの登記\nが済んだ番号', '使わない', GRAY),
             ('符号2', '1月21日\n主である建物\nに変更', '主である建物\nになった', ORANGE),
             ('符号3', '取壊しの登記\nが済んだ番号', '使わない', GRAY),
             ('符号4', '守衛所\n9月25日\n取壊し', '建て直しても\n使わない', RED),
             ('符号5', '新築倉庫\n10月7日\n完成', '新しく付ける', BLUE),
             ('符号6', '守衛所\n10月17日\n完成', '新しく付ける', BLUE)]
    w, gap = 14.5, 2.4
    for i, (no, body, state, col) in enumerate(cards):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, 30), w, 58, facecolor=col, alpha=0.14, edgecolor=col, lw=2))
        ax.text(x + w / 2, 82, no, ha='center', va='center', fontsize=22, weight='bold', color=col)
        ax.text(x + w / 2, 60, body, ha='center', va='center', fontsize=15, linespacing=1.45)
        ax.text(x + w / 2, 38, state, ha='center', va='center', fontsize=14, weight='bold', color=col, linespacing=1.3)
    x5 = 1 + 4 * (w + gap) + w / 2
    x6 = 1 + 5 * (w + gap) + w / 2
    ax.annotate('', xy=(x6, 24), xytext=(x5, 24), arrowprops=dict(arrowstyle='-|>', lw=2.0, color=BLUE))
    ax.text((x5 + x6) / 2, 17, '工事完了の順（事実関係10）', ha='center', va='center', fontsize=14, color=BLUE, weight='bold')
    ax.text(1, 17, '誤り：守衛所を符号4のまま書く、空いている1・3に入れる', ha='left', va='center', fontsize=15, color=RED,
            weight='bold')
    ax.text(1, 7, '取り壊した建物は滅失している。同じ姿で建て直しても別の建物なので、これまでで一番大きい4の次の5から付ける',
            ha='left', va='center', fontsize=15)
    fig.text(0.5, 0.05, '問2の申請書：符号4の行は「令和7年9月25日取壊し」だけ、符号5・符号6の行はそれぞれ「新築」',
             ha='center', va='center', fontsize=15)
    save_fixed(fig, 'R7_dai22mon_zu06_fugou_tsukekata')


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
    print('重なり合計:', len(PROBLEMS))
