"""令和元年度 第22問（建物）の解説図8枚を、頂点座標から作図してPNGに書き出す。

`../prompt_R1_dai22mon_kaisetsuzu.md` の図1〜図8どおり（番号は記事の挿入順）。作図の共通部品は `tools/zu_helpers.py`。
図3（建物図面）と図7（各階平面図）の完成形は、答案用紙の第3欄の欄の形の枠の中に描く。令和元年度の答案用紙はリポジトリにないため、
欄の形（家屋番号（略）・建物の所在・申請人（略）・縮尺、作成者（略）・縮尺）は、前年の平成30年度の答案用紙
（`public/kijutsu/H30-tatemono/a2.webp`）にならった仮のもの（試験の答案用紙で確かめたら直す）。
- 建物の座標は (東, 南) で持ち（原点は一棟の建物の北西の角の壁の中心線どうしの交点）、zu_helpers の (北, 東) には B() で変換する
- 敷地の座標は (北, 東)。原点は23番1の南西の角（西側道路と南側道路の角）
- 図1（構成図）は立面の模式図で、(東, 高さ) を E() で変換する（高さを図の上方向に取る）
実行: python3 note-articles-Kijyutsu/R1/Q22/zu/draw_R1_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
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


def B(e, s):
    """建物の (東, 南) を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(-s, e)


def P(n, e):
    """敷地の (北, 東)。"""
    return complex(n, e)


def E(e, h):
    """立面の模式図の (東, 高さ)。"""
    return complex(h, e)


def rect(e0, s0, e1, s1):
    return [B(e0, s0), B(e1, s0), B(e1, s1), B(e0, s1)]


def srect(e0, n0, e1, n1):
    """敷地の座標の長方形（東 e0〜e1、北 n0〜n1）。"""
    return [P(n0, e0), P(n0, e1), P(n1, e1), P(n1, e0)]


def area(pts):
    v = [xy(p) for p in pts]
    return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2


def save(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def dim_line(z, p, q, text, offsets=((12, 0), (-12, 0), (0, 12), (0, -12)), dirs=None, fs=15):
    """寸法線（両矢印）と数値。短い寸法は dirs を指定して引き出し線で外に書く。"""
    z.ax.annotate('', xy=xy(q), xytext=xy(p),
                  arrowprops=dict(arrowstyle='<->', lw=1.4, color=BLACK, shrinkA=0, shrinkB=0), zorder=4)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    if dirs:
        return z.callout(m, text, dirs=dirs, fs=fs, dists=(40, 55, 70, 90))
    return z.free_text(m, text, fs=fs, offsets=offsets)


# ---- 本件建物（図3〔平面図〕の寸法線。壁の中心間の距離、壁の厚さ0.20） ----
ITTO = rect(0, 0, 33.6, 26.8)                  # 一棟の建物の1階・2階（壁心）
ITTO_UP = rect(15.0, 0, 33.6, 26.8)            # 3〜8階（東端を1・2階にそろえる。△○の位置）
A_WC = rect(5.6, 3.6, 26.1, 23.2)              # （あ）の壁の中心線 20.50×19.60
A_IN = rect(5.7, 3.7, 26.0, 23.1)              # （あ）の壁の内側線 20.30×19.40
assert round(area(ITTO), 2) == 900.48 and round(area(ITTO_UP), 2) == 498.48
assert round(area(A_WC), 2) == 401.80 and round(area(A_IN), 2) == 393.82
# ---- 本件駐車場（壁の中心間 7.50×6.30、壁の厚さ0.10） ----
PK_WC = rect(0, 0, 7.5, 6.3)
PK_IN = rect(0.05, 0.05, 7.45, 6.25)
assert round(area(PK_WC), 2) == 47.25 and round(area(PK_IN), 2) == 45.88
# ---- 敷地（配置図の〔 〕の辺長。隅部はすべて直角） ----
S1 = srect(0, 0, 35.5, 35)
S2 = srect(35.5, 0, 55.5, 35)
assert area(S1) == 1242.5 and area(S2) == 700.0
ITTO_S = srect(11.6, 4.1, 45.2, 30.9)           # 一棟の1階（壁の中心線。西の外壁11.50＋0.10、南の外壁4.00＋0.10）
A_S = srect(17.3, 7.8, 37.6, 27.2)              # 甲区分建物（（あ）の内側線）
PK_S = srect(46.45, 23.05, 53.95, 29.35)        # 本件駐車場（壁の中心線。東の外壁55.50−1.50、南の外壁23.00）
assert round(area(ITTO_S), 2) == 900.48 and round(area(A_S), 2) == 393.82 and round(area(PK_S), 2) == 47.25
assert round(45.2 - 37.6, 2) == 7.60 and round(30.9 - 27.2, 2) == 3.70


# ---- 図1：本件建物・本件駐車場の構成図（立面の模式図） ----
def zu01():
    fig, axes = new_figure('本件建物と本件駐車場の構成（南から見た模式図）',
                           '区分建物（甲・乙・丙）の床面積は内法、一棟の建物と本件駐車場は壁心。塔屋は階数・床面積に入れない（寸法は模式）',
                           w=16, h=11)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    fl = 3.0   # 1階分の高さ（模式）
    kyo = [E(0, 0), E(5.6, 0), E(5.6, 2 * fl), E(0, 2 * fl)]
    kou = [E(5.6, 0), E(26.1, 0), E(26.1, 2 * fl), E(5.6, 2 * fl)]
    otsu = [E(26.1, 0), E(33.6, 0), E(33.6, 2 * fl), E(26.1, 2 * fl)]
    hei = [E(15.0, 2 * fl), E(33.6, 2 * fl), E(33.6, 8 * fl), E(15.0, 8 * fl)]
    tou = [E(27.6, 8 * fl), E(31.6, 8 * fl), E(31.6, 9 * fl), E(27.6, 9 * fl)]
    park = [E(38.0, 0), E(45.6, 0), E(45.6, 7 * fl), E(38.0, 7 * fl)]
    z.poly(kyo, color=BLACK, lw=1.6, fill=GRAY, alpha=0.25)
    z.poly(kou, color=BLACK, lw=1.6, fill=BLUE, alpha=0.35)
    z.poly(otsu, color=BLACK, lw=1.6, fill=GREEN, alpha=0.35)
    z.poly(hei, color=BLACK, lw=1.6, fill=ORANGE, alpha=0.30)
    z.poly(tou, color=GRAY, lw=1.4, ls='--', fill=GRAY, alpha=0.15)
    z.poly(park, color=BLACK, lw=1.8, fill='#f2c200', alpha=0.30)
    z.line(E(0, fl), E(33.6, fl), color=GRAY, lw=1.0, ls=':')
    for k in range(3, 8):
        z.line(E(15.0, k * fl), E(33.6, k * fl), color=GRAY, lw=1.0, ls=':')
    z.line(E(-3, 0), E(49, 0), color=BLACK, lw=2.0)
    fit(ax, kyo + park + tou, margin=0.06, extra=[xy(E(-4, -4)), xy(E(58, 30))], pad_aspect=True)
    z.free_text(E(15.85, 1.5 * fl), '甲区分建物（あ）1階・2階\nB町行政センター', fs=14)
    z.free_text(E(29.85, 1.5 * fl), '乙（い）\n1階・2階', fs=13)
    z.free_text(E(24.3, 4.5 * fl), '丙区分建物（う）3〜8階\nABレジデンス', fs=14)
    z.callout(E(2.8, 1.5 * fl), '共用部分\n（エスカレーター・ホール）', dirs=(120, 135, 105), fs=12, color=GRAY)
    z.callout(E(29.6, 8.5 * fl), '塔屋（屋上に出るためだけ）\n→ 階数・床面積に入れない', dirs=(160, 170, 150), fs=13, color=RED)
    z.callout(E(41.8, 5 * fl), '本件駐車場（符号1）\n回転式で人が使う階なし\n→ 平家建・壁心', dirs=(20, 0, 40), fs=13, color=BLACK)
    z.free_text(E(16.8, -2.2), '一棟の建物　Aランドマークタウン　鉄筋コンクリート造陸屋根8階建', fs=14, weight='bold')
    z.free_text(E(41.8, -2.2), '区分されていない普通の建物', fs=13)
    save(fig, [z], 'R1_dai22mon_zu01_kousei')


# ---- 図2：敷地の確認図（作図チェック用） ----
def zu02():
    fig, axes = new_figure('敷地の確認図（作図チェック用）',
                           '配置図の〔 〕の辺長から出した面積が、登記記録の地積と一致する。辺長は建物図面には書かない',
                           w=16, h=10.5)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(S1, color=BLACK, lw=2.4, fill=BLUE, alpha=0.10)
    z.poly(S2, color=BLACK, lw=2.4, fill=GREEN, alpha=0.10)
    fit(ax, S1 + S2, margin=0.10, extra=[xy(P(41, 27)), xy(P(-6, 27)), xy(P(17, -9)), xy(P(17, 64))], pad_aspect=True)
    z.north_arrow()
    c1, c2 = centroid(S1), centroid(S2)
    z.edge_label(S1[0], S1[1], '35.50m', c1)
    z.edge_label(S1[2], S1[3], '35.50m', c1)
    z.edge_label(S1[3], S1[0], '35.00m', c1)
    z.edge_label(S2[0], S2[1], '20.00m', c2)
    z.edge_label(S2[2], S2[3], '20.00m', c2)
    z.edge_label(S2[1], S2[2], '35.00m', c2)
    z.free_text(c1, '23番1\n35.50×35.00＝1242.50㎡\n（登記記録の地積と一致）', fs=15)
    z.free_text(c2, '23番2\n20.00×35.00\n＝700.00㎡\n（登記記録の\n地積と一致）', fs=15)
    z.free_text(P(38.5, 17.75), '24', fs=15, color=GRAY)
    z.free_text(P(38.5, 45.5), '25', fs=15, color=GRAY)
    z.free_text(P(17.5, 61.0), '26', fs=15, color=GRAY)
    z.free_text(P(17.5, -6.0), '道路', fs=15, color=GRAY)
    z.free_text(P(-4.2, 27.75), '道路', fs=15, color=GRAY)
    save(fig, [z], 'R1_dai22mon_zu02_shikichi_kakunin')


def cell(fig, x0, y0, x1, y1, text='', fs=14, ha='center', lw=1.6, color=BLACK):
    """答案用紙の欄（図の座標 0〜1）。"""
    fig.add_artist(Rectangle((x0, y0), x1 - x0, y1 - y0, transform=fig.transFigure, fill=False, lw=lw, ec=BLACK))
    if text:
        x = (x0 + x1) / 2 if ha == 'center' else x0 + 0.01
        fig.text(x, (y0 + y1) / 2, text, ha=ha, va='center', fontsize=fs, color=color)


INK = '#1a3a8f'   # 記入（濃い青）


# ---- 図3：建物図面の完成形（答案用紙の第3欄の形の枠の中。欄の形は平成30年度にならった仮のもの） ----
def zu03():
    setup_font()
    fig = plt.figure(figsize=(16, 13), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('建物図面の完成形（答案用紙の第3欄・縮尺1/500で描く内容）', fontsize=22, weight='bold', y=0.985)
    cell(fig, 0.06, 0.880, 0.20, 0.930, '家屋番号', fs=15)
    cell(fig, 0.20, 0.880, 0.46, 0.930, '（略）', fs=15)
    fig.text(0.70, 0.905, '建　物　図　面', ha='center', va='center', fontsize=20)
    cell(fig, 0.06, 0.830, 0.20, 0.880, '建物の所在', fs=15)
    cell(fig, 0.20, 0.830, 0.94, 0.880, 'A市B町一丁目23番地1、23番地2', fs=16, ha='left', color=INK)
    cell(fig, 0.06, 0.110, 0.94, 0.830, lw=1.8)
    cell(fig, 0.06, 0.060, 0.20, 0.110, '申　請　人', fs=15)
    cell(fig, 0.20, 0.060, 0.74, 0.110, '（略）', fs=15)
    cell(fig, 0.74, 0.060, 0.83, 0.110, '縮尺', fs=15)
    cell(fig, 0.83, 0.060, 0.94, 0.110, '1/500', fs=15)
    fig.text(0.5, 0.025, '一棟の建物の1階は点線、甲区分建物（1階の（あ））と附属建物は実線。3.70・7.60は一棟の壁の中心線から（あ）の内側線まで。'
             '敷地の辺長は書かない', ha='center', va='center', fontsize=13)
    ax = fig.add_axes([0.08, 0.125, 0.84, 0.69])
    z = Zu(ax, fontsize=14)
    fit(ax, S1 + S2, margin=0.08, extra=[xy(P(40, 27)), xy(P(-9, 27))], pad_aspect=True)
    z.north_arrow()
    z.poly(S1 + [], color=BLACK, lw=2.2)
    z.poly(S2, color=BLACK, lw=2.2)
    z.poly(ITTO_S, color=BLACK, lw=1.8, ls='--')
    z.poly(A_S, color=BLACK, lw=2.6)
    z.poly(PK_S, color=BLACK, lw=2.6)
    dim_line(z, P(26.0, 0), P(26.0, 11.6), '11.50', offsets=((0, 12), (0, -12)))
    dim_line(z, P(8.0, 0), P(8.0, 11.6), '11.50', offsets=((0, 12), (0, -12)))
    dim_line(z, P(0, 13.5), P(4.1, 13.5), '4.00', offsets=((26, 0), (-26, 0), (30, 0)))
    dim_line(z, P(30.9, 20.0), P(27.2, 20.0), '3.70', offsets=((26, 0), (-26, 0), (30, 0)))
    dim_line(z, P(24.0, 37.6), P(24.0, 45.2), '7.60', offsets=((0, 12), (0, -12)))
    dim_line(z, P(11.0, 37.6), P(11.0, 45.2), '7.60', offsets=((0, 12), (0, -12)))
    dim_line(z, P(29.35, 53.95), P(29.35, 55.5), '1.50', dirs=(60, 45, 75))
    dim_line(z, P(23.05, 53.95), P(23.05, 55.5), '1.50', dirs=(-60, -45, -75))
    dim_line(z, P(0, 51.5), P(23.05, 51.5), '23.00', offsets=((-30, 0), (30, 0), (-36, 0)))
    z.free_text(centroid(A_S), '主', fs=18, bbox=dict(boxstyle='circle,pad=0.3', fc='white', ec=BLACK, lw=1.4))
    z.free_text(centroid(PK_S), '附1', fs=14, bbox=dict(boxstyle='circle,pad=0.25', fc='white', ec=BLACK, lw=1.4))
    z.free_text(P(2.2, 25.0), '23－1', fs=15)
    z.free_text(P(2.2, 41.0), '23－2', fs=15)
    z.free_text(P(37.5, 17.75), '24', fs=15)
    z.free_text(P(37.5, 45.5), '25', fs=15)
    z.free_text(P(12.0, 58.0), '26', fs=15)
    z.free_text(P(17.5, -3.4), '道路', fs=15)
    z.free_text(P(-2.8, 27.75), '道路', fs=15)
    z.free_text(P(-6.5, 27.75), '主である建物の存する部分　1階、2階', fs=16, weight='bold')
    z.free_text(P(-6.5, 57.5), '（単位：m）', fs=13)
    save(fig, [z], 'R1_dai22mon_zu03_tatemono_zumen')


# ---- 図4：甲区分建物の誤り比較図（壁心／内法） ----
def wall_detail(ax, left_text, right_text, note, color_in=GREEN):
    """壁の断面の拡大図（壁の厚さ0.20を、長さ方向より大きく拡大した模式）。北＝上、下側が専有部分。"""
    z = Zu(ax, fontsize=13)
    band = [complex(1.0, 0), complex(1.0, 3), complex(0, 3), complex(0, 0)]
    z.poly(band, color=BLACK, lw=1.6, fill=GRAY, alpha=0.35)
    z.line(complex(0.5, -0.2), complex(0.5, 3.2), color=BLACK, lw=1.4, ls='-.')
    z.line(complex(0, -0.2), complex(0, 3.2), color=color_in, lw=3.2)
    fit(ax, band, margin=0.2, extra=[xy(complex(-2.6, 1.5)), xy(complex(2.6, 1.5)), xy(complex(0.5, -1.6)),
                                     xy(complex(0.5, 5.6))], pad_aspect=True)
    for n0, n1, e, t, col in [(0, 1.0, -0.5, '0.20', BLACK), (0, 0.5, 3.6, '0.10', RED)]:
        z.ax.annotate('', xy=xy(complex(n1, e)), xytext=xy(complex(n0, e)),
                      arrowprops=dict(arrowstyle='<->', lw=1.4, color=col, shrinkA=0, shrinkB=0), zorder=4)
        z.segments.append((xy(complex(n0, e)), xy(complex(n1, e))))
        z.free_text(complex((n0 + n1) / 2, e), t, fs=15, color=col,
                    offsets=((-26, 0), (26, 0)) if e < 0 else ((26, 0), (32, 0)))
    z.free_text(complex(1.9, 1.5), right_text, fs=13, color=GRAY)
    z.free_text(complex(-1.0, 1.5), left_text, fs=14, color=color_in, weight='bold')
    z.free_text(complex(-2.1, 1.5), note, fs=13, weight='bold')
    z.callout(complex(0.5, 2.4), '壁の中心線', dirs=(60, 45, 75), fs=12, dists=(35, 50, 65))
    z.callout(complex(0, 2.4), '壁の内側線', dirs=(-60, -45, -75), fs=12, color=color_in, dists=(35, 50, 65))
    return z


def zu04():
    fig, axes = new_figure('甲区分建物（（あ）専有部分）の床面積：壁心か内法か',
                           '区分建物は壁その他の区画の内側線で囲まれた部分で測る（不動産登記規則第115条）。両側から壁の厚さの半分0.10ずつ引く',
                           w=19, h=9, ncols=3, width_ratios=[1, 0.85, 1])
    fig.subplots_adjust(top=0.84)
    z = Zu(axes[0], fontsize=14)
    z.poly(A_WC, color=RED, lw=2.4, fill=RED, alpha=0.28)
    axes[0].set_title('誤り：壁の中心線で測る（藍子）', fontsize=17, weight='bold', color=RED)
    fit(axes[0], A_WC, margin=0.25, pad_aspect=True)
    c = centroid(A_WC)
    z.edge_label(A_WC[0], A_WC[1], '20.50m', c)
    z.edge_label(A_WC[1], A_WC[2], '19.60m', c)
    z.free_text(c, '20.50×19.60\n＝401.80㎡', fs=16, color=RED)
    z2 = wall_detail(axes[1], '専有部分（あ）', '廊下（共用部分）', '区分建物は内側線で測る')
    axes[1].set_title('壁の断面（拡大）', fontsize=17, weight='bold')
    z3 = Zu(axes[2], fontsize=14)
    z3.poly(A_WC, color=GRAY, lw=1.2, ls='--')
    z3.poly(A_IN, color=GREEN, lw=2.4, fill=GREEN, alpha=0.25)
    axes[2].set_title('正解：壁の内側線で測る（内法）', fontsize=17, weight='bold', color=GREEN)
    fit(axes[2], A_WC, margin=0.25, pad_aspect=True)
    c3 = centroid(A_IN)
    z3.edge_label(A_IN[0], A_IN[1], '20.30m', c3, outward=False, dists=(12, 18, 24))
    z3.edge_label(A_IN[1], A_IN[2], '19.40m', c3, outward=False, dists=(12, 18, 24))
    z3.free_text(c3, '20.30×19.40\n＝393.82㎡', fs=16, color=GREEN)
    save(fig, [z, z2, z3], 'R1_dai22mon_zu04_kou_ayamari_hikaku')


# ---- 図5：甲区分建物の求積図 ----
def zu05():
    fig, axes = new_figure('甲区分建物の床面積求積図（1階部分・2階部分　各階同型）',
                           '20.30×19.40＝393.82㎡（1階部分・2階部分とも）。灰色の共用部分と乙区分建物は甲の床面積に入らない。\n'
                           '黒い細線は壁の中心線、青い線は（あ）の内側線（0.10内側）',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    z.poly(ITTO, color=BLACK, lw=2.4, fill=GRAY, alpha=0.20)
    for a, b in [((0, 3.6), (30.7, 3.6)), ((0, 23.2), (26.1, 23.2)), ((26.1, 3.6), (26.1, 26.8)),
                 ((5.6, 3.6), (5.6, 23.2))]:
        z.line(B(*a), B(*b), color=BLACK, lw=1.2)
    z.poly(rect(27.6, 3.6, 33.6, 7.2), color=BLACK, lw=1.2)
    z.poly(rect(30.7, 0, 33.6, 3.6), color=BLACK, lw=1.2)
    z.poly(A_IN, color=BLUE, lw=0, fill=BLUE, alpha=0.40, check=False)
    z.poly(A_IN, color=BLUE, lw=2.4)
    fit(ax, ITTO, margin=0.10, extra=[xy(B(16.8, 30.5)), xy(B(16.8, -3.0))], pad_aspect=True)
    z.north_arrow()
    c = centroid(A_IN)
    z.edge_label(A_IN[0], A_IN[1], '20.30m', c, outward=False, dists=(12, 18, 24))
    z.edge_label(A_IN[1], A_IN[2], '19.40m', c, outward=False, dists=(12, 18, 24))
    z.edge_label(A_IN[2], A_IN[3], '20.30m', c, outward=False, dists=(12, 18, 24))
    z.edge_label(A_IN[3], A_IN[0], '19.40m', c, outward=False, dists=(12, 18, 24))
    z.free_text(c, '甲区分建物（あ）\n393.82㎡', fs=17, weight='bold')
    z.free_text(B(14.0, 1.8), 'ホール（廊下）', fs=13, color=GRAY)
    z.free_text(B(13.0, 25.0), 'ホール（廊下）', fs=13, color=GRAY)
    z.free_text(B(2.8, 13.4), 'エスカ\nレーター\n出入口', fs=12, color=GRAY)
    z.free_text(B(29.85, 17.0), '乙区分\n建物（い）', fs=13, color=GRAY)
    z.free_text(B(30.6, 5.4), '階段室', fs=12, color=GRAY)
    z.free_text(B(32.15, 1.8), 'EV', fs=12, color=GRAY)
    for (e, s), mk in [((33.6, 0), '^'), ((33.6, 26.8), 'o')]:
        a, b = xy(B(e, s))
        ax.plot(a, b, mk, ms=13, mfc='white', mec=BLACK, mew=1.6, zorder=6)
        z.markers.append((a, b))
    z.free_text(B(16.8, 28.6), '一棟の建物の1階（壁の中心線 33.60m×26.80m）', fs=13)
    save(fig, [z], 'R1_dai22mon_zu05_kou_kyuuseki')


# ---- 図6：本件駐車場の誤り比較図（内法／壁心） ----
def zu06():
    fig, axes = new_figure('本件駐車場（符号1）の床面積：内法か壁心か',
                           '内法で測るのは区分建物だけ。本件駐車場は一棟の外に建つ区分されていない建物なので、被覆材ではない壁の中心線で測る',
                           w=19, h=9, ncols=3, width_ratios=[1, 0.85, 1])
    fig.subplots_adjust(top=0.84)
    z = Zu(axes[0], fontsize=14)
    z.poly(PK_WC, color=GRAY, lw=1.2, ls='--')
    z.poly(PK_IN, color=RED, lw=2.4, fill=RED, alpha=0.28)
    axes[0].set_title('誤り：区分建物と同じ内法（藍子）', fontsize=17, weight='bold', color=RED)
    fit(axes[0], PK_WC, margin=0.25, pad_aspect=True)
    c = centroid(PK_IN)
    z.edge_label(PK_IN[0], PK_IN[1], '7.40m', c, outward=False, dists=(12, 18, 24))
    z.edge_label(PK_IN[1], PK_IN[2], '6.20m', c, outward=False, dists=(12, 18, 24))
    z.free_text(c, '7.40×6.20\n＝45.88㎡', fs=16, color=RED)
    # 中央：主である建物と附属建物の測り方の違い、壁の断面
    ax = axes[1]
    z2 = Zu(ax, fontsize=13)
    band = [complex(1.0, 0), complex(1.0, 3), complex(0, 3), complex(0, 0)]      # 壁（北＝上が外、下が内）
    z2.poly(band, color=BLACK, lw=1.6, fill=GRAY, alpha=0.35)
    z2.line(complex(0.5, -0.2), complex(0.5, 3.2), color=GREEN, lw=3.0, ls='-.')
    col = [complex(0, 1.1), complex(0, 1.9), complex(-0.8, 1.9), complex(-0.8, 1.1)]   # 柱は壁の内側に接する
    z2.poly(col, color=BLACK, lw=1.6, fill=BLACK, alpha=0.55)
    fit(ax, band, margin=0.2, extra=[xy(complex(-2.9, 1.5)), xy(complex(3.9, 1.5)), xy(complex(0.5, -1.8)),
                                     xy(complex(0.5, 5.4))], pad_aspect=True)
    z2.free_text(complex(3.3, 1.5), '主である建物（甲区分建物）→ 内法', fs=13)
    z2.free_text(complex(2.3, 1.5), '附属建物（本件駐車場）→ 壁心', fs=14, color=GREEN, weight='bold')
    z2.callout(complex(0.75, 2.6), '軽量気泡コンクリートパネルの壁\n（厚さ0.10、被覆材ではない＝区画）', dirs=(-90, -110, -70),
               fs=12, dists=(95, 115, 135))
    z2.callout(complex(-0.4, 1.5), '鉄骨の柱', dirs=(-100, -80, -120), fs=12, dists=(30, 45, 60))
    z2.callout(complex(0.5, 0.3), '壁の中心線で測る', dirs=(-120, -135, -150), fs=12, color=GREEN, dists=(50, 65, 80))
    axes[1].set_title('測り方を決めるのは建物自体', fontsize=17, weight='bold')
    z3 = Zu(axes[2], fontsize=14)
    z3.poly(PK_WC, color=GREEN, lw=2.4, fill=GREEN, alpha=0.25)
    axes[2].set_title('正解：壁の中心線で測る（壁心）', fontsize=17, weight='bold', color=GREEN)
    fit(axes[2], PK_WC, margin=0.25, pad_aspect=True)
    c3 = centroid(PK_WC)
    z3.edge_label(PK_WC[0], PK_WC[1], '7.50m', c3)
    z3.edge_label(PK_WC[1], PK_WC[2], '6.30m', c3)
    z3.free_text(c3, '7.50×6.30\n＝47.25㎡', fs=16, color=GREEN)
    save(fig, [z, z2, z3], 'R1_dai22mon_zu06_chuushajou_ayamari_hikaku')


# ---- 図7：各階平面図の完成形（答案用紙の第3欄の形の枠の中。欄の形は平成30年度にならった仮のもの） ----
def zu07():
    setup_font()
    fig = plt.figure(figsize=(18, 11), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('各階平面図の完成形（答案用紙の第3欄・縮尺1/250で描く内容）', fontsize=22, weight='bold', y=0.975)
    fig.text(0.5, 0.905, '各　階　平　面　図', ha='center', va='center', fontsize=20)
    cell(fig, 0.04, 0.13, 0.96, 0.88, lw=1.8)
    cell(fig, 0.04, 0.06, 0.14, 0.13, '作　成　者', fs=15)
    cell(fig, 0.14, 0.06, 0.78, 0.13, '（略）　　　　　　　　　　　　（令和何年何月何日作成）', fs=15)
    cell(fig, 0.78, 0.06, 0.86, 0.13, '縮尺', fs=15)
    cell(fig, 0.86, 0.06, 0.96, 0.13, '1/250', fs=15)
    fig.text(0.5, 0.025, '甲区分建物は内法（壁の内側線）、附属建物（符号1）は壁心。甲区分建物は1階部分と2階部分が同じ形なので1つの図に「各階同型」と書く。'
             '求積表と床面積も書く（不動産登記規則第83条第1項）', ha='center', va='center', fontsize=13)
    axes = [fig.add_axes([0.05, 0.36, 0.42, 0.46]), fig.add_axes([0.53, 0.36, 0.42, 0.46])]
    kou = [B(0, 0), B(20.3, 0), B(20.3, 19.4), B(0, 19.4)]
    pk = [B(0, 0), B(7.5, 0), B(7.5, 6.3), B(0, 6.3)]
    assert round(area(kou), 2) == 393.82 and round(area(pk), 2) == 47.25
    half_e, half_s = 20.3 / 2, 19.4 / 2   # 2つの図を同じ縮尺にするため、同じ大きさの範囲で表示する
    zs = []
    for k, (pts, labels, name, mark, c) in enumerate([
            (kou, ['20.30', '19.40', '20.30', '19.40'], '1階部分、2階部分（各階同型）', '主', (10.15, 9.7)),
            (pk, ['7.50', '6.30', '7.50', '6.30'], '附属建物（符号1）　1階', '附1', (3.75, 3.15))]):
        ax = axes[k]
        z = Zu(ax, fontsize=14)
        ax.set_title(name, fontsize=17, weight='bold')
        fit(ax, [B(c[0] - half_e, c[1] - half_s), B(c[0] + half_e, c[1] + half_s)], margin=0.16, pad_aspect=True)
        z.poly(pts, color=BLACK, lw=2.4)
        cc = centroid(pts)
        for i, t in enumerate(labels):
            z.edge_label(pts[i], pts[(i + 1) % 4], t, cc, fs=14)
        z.free_text(cc, mark, fs=16 if k == 0 else 13,
                    bbox=dict(boxstyle='circle,pad=0.3', fc='white', ec=BLACK, lw=1.4))
        zs.append(z)
    zs[1].north_arrow()
    fig.text(0.07, 0.315, '甲区分建物（主）　1階部分・2階部分\n20.30×19.40＝393.8200\n床面積　1階部分　393.82㎡\n　　　　2階部分　393.82㎡',
             ha='left', va='top', fontsize=15, linespacing=1.5)
    fig.text(0.55, 0.315, '附属建物（符号1）\n7.50×6.30＝47.2500\n床面積　47.25㎡', ha='left', va='top', fontsize=15, linespacing=1.5)
    save(fig, zs, 'R1_dai22mon_zu07_kakukai_heimenzu')


# ---- 図8：本番で解く順番 ----
def zu08():
    """本番で解く順番。固定配置の図なので重なり検査の対象外。"""
    fig = plt.figure(figsize=(16, 8), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　知識で書ける問2と申請書の欄を先に', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.20, 0.94, 0.70])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '問2', '第2欄\n（別紙を読まずに\n知識で書ける）', BLUE),
        ('②', '時系列\nメモ', '事実関係・\n登記記録', BLUE),
        ('③', '申請書の\n床面積以外', '目的・添付書類・\n所在・構造・\n敷地権', BLUE),
        ('④', '床面積の\n求積', '甲は内法\n一棟・駐車場は\n壁心', RED),
        ('⑤', '第3欄の\n作図', '建物図面・\n各階平面図', RED),
        ('⑥', '見直し', '内法と壁心・塔屋・\n敷地権の日付・\n「番地」と「番」', GRAY),
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
    ax.text(1 + 1.5 * (w + gap) - gap / 2, 76, '床面積を出さなくても書ける', ha='center', fontsize=15, color=BLUE,
            weight='bold')
    ax.annotate('', xy=(1 + 3 * (w + gap) - gap, 72), xytext=(1, 72), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 4 * (w + gap) - gap / 2, 76, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 5 * (w + gap) - gap, 72), xytext=(1 + 3 * (w + gap), 72),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.09, '床面積は、図3の寸法を拾って、甲区分建物は内法・一棟の建物と本件駐車場は壁心に切り替えるので時間がかかる。\n'
             '先に問2と申請書の大部分を書いておけば、作図で時間が足りなくなっても点は取れている。',
             ha='center', va='center', fontsize=15)
    path = os.path.join(OUT, 'R1_dai22mon_zu08_toku_junban.png')
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
