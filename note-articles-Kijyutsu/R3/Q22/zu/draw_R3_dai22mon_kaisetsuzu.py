"""令和3年度 第22問（建物）の解説図30枚を、頂点座標と固定配置から作図してPNGに書き出す。

`../prompt_R3_dai22mon_kaisetsuzu.md` の図1〜図30どおり（番号は記事の画像挿入の順。画像の中には図番を入れない）。
作図の共通部品は `tools/zu_helpers.py`（座標の図）と `tools/zu_cards.py`（比較カード・表などの固定配置の図）。
図10（建物図面）と図17（各階平面図）の完成形は、答案用紙の第3欄（A3横の用紙の1枚の枠。左半分が各階平面図、右半分が建物図面）を
原本（`../touan_youshi/R3_dai22mon_touan_youshi.pdf`）の罫線から測った寸法で、1/500・1/250の実際の大きさに描く
（2026-10-26。枠は横302.0mm×縦231.0mm、左右の境は枠の中央、1mm＝8px）。申請人・作成者は「（略）」、作成の日付は「（令和3年○月○日作成）」と印刷済み。
建物の座標は (東, 南) で持ち（原点は一棟の建物の北西の角の、壁の中心線の交点）、zu_helpers の (北, 東) には
B() で変換する（北 ＝ −南）。図28だけは（ロ）部分の北西の角（一棟の建物の座標では東8.00）を原点にする。
敷地は座標値一覧表がないので、図1の辺長から組み立てた座標（西側の線を東0、南側の線を北0）を使う。
実行: python3 note-articles-Kijyutsu/R3/Q22/zu/draw_R3_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Rectangle  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE, GREEN,  # noqa: E402
                        PURPLE)
from zu_cards import Cards  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []
YELLOW = '#e0b000'
INK = '#1a3a8f'   # 記入（濃い青）
C = Cards(OUT, PROBLEMS)
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


# ---- 建物（図3・図4の寸法線から。壁心は鉄骨の柱又は壁の中心、内法は中心から0.10内側） ----
WHOLE1 = [(0, 0), (6.5, 0), (6.5, 1), (9.5, 1), (9.5, 0), (16, 0), (16, 11), (0, 11)]   # 一棟の1階（壁心）
WHOLE2 = rect(0, 0, 16, 11)                                                                # 一棟の2階（壁心）
I1_WALL = [(0, 0), (6.5, 0), (6.5, 1), (8, 1), (8, 11), (0, 11)]                           # （イ）1階の壁心
I1 = [(0.1, 0.1), (6.4, 0.1), (6.4, 1.1), (7.9, 1.1), (7.9, 10.9), (0.1, 10.9)]            # （イ）1階の内法
I1_STRIPS = [rect(0.1, 0.1, 6.4, 1.1), rect(0.1, 1.1, 7.9, 10.9)]
I2 = rect(0.1, 0.1, 7.9, 10.9)                                                             # （イ）2階の内法
RO1_WALL = [(8, 1), (9.5, 1), (9.5, 0), (16, 0), (16, 11), (8, 11)]                        # （ロ）1階の壁心
# 図7：（ロ）部分の座標（原点は（ロ）部分の北西の角）
R1_WALL = [(0, 1), (1.5, 1), (1.5, 0), (8, 0), (8, 11), (0, 11)]
A_PART = [(0.1, 1.1), (1.6, 1.1), (1.6, 0.1), (7.9, 0.1), (7.9, 6.4), (5.2, 6.4), (5.2, 9.6), (5.9, 9.6),
          (5.9, 10.9), (0.1, 10.9)]
A_STRIPS = [rect(1.6, 0.1, 7.9, 1.1), rect(0.1, 1.1, 7.9, 6.4), rect(0.1, 6.4, 5.2, 9.6), rect(0.1, 9.6, 5.9, 10.9)]
MARU_A = [(5.4, 6.6), (7.9, 6.6), (7.9, 10.9), (6.1, 10.9), (6.1, 9.4), (5.4, 9.4)]
MARU_STRIPS = [rect(5.4, 6.6, 7.9, 9.4), rect(6.1, 9.4, 7.9, 10.9)]
MARU_A_WALL = [(5.3, 6.5), (8, 6.5), (8, 11), (6, 11), (6, 9.5), (5.3, 9.5)]
A_WALL = [(0, 1), (1.5, 1), (1.5, 0), (8, 0), (8, 6.5), (5.3, 6.5), (5.3, 9.5), (6, 9.5), (6, 11), (0, 11)]

assert area_es(WHOLE1) == 173.00 and area_es(WHOLE2) == 176.00
assert area_es(I1_WALL) == 86.50 and area_es(RO1_WALL) == 86.50
assert round(area_es(I1), 2) == 82.74 == round(sum(area_es(r) for r in I1_STRIPS), 2)
assert round(area_es(I2), 2) == 84.24
assert round(area_es(A_PART), 2) == 71.50 == round(sum(area_es(r) for r in A_STRIPS), 2)
assert round(area_es(MARU_A), 2) == 9.70 == round(sum(area_es(r) for r in MARU_STRIPS), 2)
assert round(area_es(MARU_A) + area_es(I2), 2) == 93.94

# ---- 敷地（図1の辺長。X＝北、Y＝東。西側の線を Y＝0、南側の線を X＝0） ----
S_NW, S_43, S_NE, S_SE = complex(18.70, 0), complex(18.70, 15.70), complex(18.70, 19.70), complex(0, 19.70)
S_CE, S_CN = complex(0, 2.12), complex(2.12, 0)      # 隅切りの東の端・北の端
SITE = [S_NW, S_43, S_NE, S_SE, S_CE, S_CN]
assert round(area(SITE), 4) == 366.1428


def to_site(p):
    """建物の点（B()で作った複素数）を敷地の座標へ（北の外壁が北側の筆界から1.00、西の外壁が西側の筆界から2.50）。"""
    return complex(17.70 + p.real, 2.50 + p.imag)


def dims(z, pts, labels, fs=14, ref=None):
    c = ref or centroid(pts)
    for i, t in enumerate(labels):
        if t:
            z.edge_label(pts[i], pts[(i + 1) % len(pts)], t, c, fs=fs)


def tri(z, p, color=BLACK, size=11):
    """△印（各階の重なる柱の位置）。重なり検査の点として登録する。"""
    a, b = xy(p)
    z.ax.plot(a, b, '^', ms=size, mfc='white', mec=color, mew=1.8, zorder=6)
    z.markers.append((a, b))


# ---- 図5：区分の全体像 ----
def zu05():
    fig, axes = new_figure('区分の全体像：縦割りの区分（問1）と、（ロ）部分の再区分（問2）',
                           '（イ）部分は1階から屋根まで続く西半分（玄関1つの居宅）。（ロ）部分は、将来（あ）部分と（い）部分等に分ける',
                           w=18, h=8.5, ncols=3)
    fig.subplots_adjust(top=0.82, bottom=0.14)
    off = 18.5   # 2階を東へずらして並べる
    titles = ['区分前：家屋番号5番2（共同住宅）', '問1：建物区分登記（縦割り）', '問2：（ロ）部分をさらに区分']
    zs = []
    for k, ax in enumerate(axes):
        z = Zu(ax, fontsize=12)
        ax.set_title(titles[k], fontsize=16, weight='bold')
        if k == 0:
            z.poly(P(WHOLE1), color=BLACK, lw=2, fill=GRAY, alpha=0.25)
            z.poly(P(WHOLE2, off), color=BLACK, lw=2, fill=GRAY, alpha=0.25)
            z.free_text(B(8, 6), '173.00㎡', fs=13)
            z.free_text(B(8 + off, 6), '176.00㎡', fs=13)
        elif k == 1:
            z.poly(P(I1_WALL), color=BLACK, lw=2, fill=BLUE, alpha=0.30)
            z.poly(P(RO1_WALL), color=BLACK, lw=2, fill=GREEN, alpha=0.25)
            z.poly(P(rect(0, 0, 8, 11), off), color=BLACK, lw=2, fill=BLUE, alpha=0.30)
            z.poly(P(rect(8, 0, 16, 11), off), color=BLACK, lw=2, fill=GREEN, alpha=0.25)
            for d in (0, off):
                z.free_text(B(4 + d, 6), '（イ）', fs=14, weight='bold', color=BLUE)
                z.free_text(B(12 + d, 6), '（ロ）', fs=14, weight='bold', color=GREEN)
        else:
            z.poly(P(A_WALL, 8), color=BLACK, lw=2, fill=YELLOW, alpha=0.35)
            z.poly(P(MARU_A_WALL, 8), color=BLACK, lw=2, fill=RED, alpha=0.30)
            z.poly(P(rect(0, 0, 8, 11), off), color=BLUE, lw=1.2, ls='--', check=False)
            z.poly(P(rect(8, 0, 16, 11), off), color=BLACK, lw=2, fill=RED, alpha=0.30)
            z.poly(P(I1_WALL), color=BLUE, lw=1.2, ls='--', check=False)
            z.free_text(B(11.2, 3.5), '（あ）', fs=14, weight='bold')
            z.free_text(B(14.6, 8.4), 'Ⓐ', fs=15, weight='bold', color=RED)
            z.free_text(B(12 + off, 6), '（い）', fs=14, weight='bold', color=RED)
            z.free_text(B(4, 6), '（イ）', fs=12, color=BLUE)
            z.free_text(B(4 + off, 6), '（イ）', fs=12, color=BLUE)
        fit(ax, P(WHOLE1) + P(WHOLE2, off), margin=0.06, extra=[xy(B(0, 18.5)), xy(B(34.5, -1.5))], pad_aspect=True)
        z.free_text(B(8, 12.4), '1階', fs=13, va='top')
        z.free_text(B(8 + off, 12.4), '2階', fs=13, va='top')
        if k == 1:
            z.free_text(B(16.25, 16.4), '（イ）＝5番2の1 居宅（玄関1つ）\n（ロ）＝5番2の2 共同住宅', fs=12)
        if k == 2:
            z.free_text(B(16.25, 16.4), '（い）部分等＝2階の（い）＋1階のⒶ\n（Ⓐは（い）専用の玄関・階段）', fs=12, color=RED)
        zs.append(z)
    axes[2].annotate('', xy=xy(B(12 + off - 2.5, 3.5)), xytext=xy(B(15.2, 7.4)),
                     arrowprops=dict(arrowstyle='-|>', lw=1.6, color=RED, mutation_scale=16, connectionstyle='arc3,rad=-0.3'),
                     zorder=6)
    zs[0].north_arrow()
    save(fig, zs, 'R3_dai22mon_zu05_kubun_zentaizou')


# ---- 図7：敷地の辺長確認図 ----
def zu07():
    fig, axes = new_figure('本件土地（5番2）の辺長確認図（作図チェック用）',
                           '隅切りの2辺は 18.70−16.58＝19.70−17.58＝2.12。19.70×18.70−2.12×2.12÷2＝366.14㎡（登記記録の地積と一致）。辺長は建物図面には書かない',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(SITE, color=BLACK, lw=2.4, fill=BLUE, alpha=0.08)
    z.line(S_CE, complex(0, 0), color=GRAY, lw=1.2, ls=':')
    z.line(complex(0, 0), S_CN, color=GRAY, lw=1.2, ls=':')
    z.line(S_43, complex(20.2, 15.70), color=BLACK, lw=1.4)
    fit(ax, SITE, margin=0.10, extra=[(-4.5, 24.5), (25.5, -3.8)], pad_aspect=True)
    z.north_arrow()
    c = complex(9, 10)
    dims(z, SITE, ['15.70', '4.00', '18.70', '17.58', '', '16.58'], fs=15, ref=c)
    z.callout((S_CE + S_CN) / 2, '隅切り 3.00', dirs=(225, 240, 210), fs=15, dists=(45, 60, 80))
    z.free_text(complex(23.4, 9.85), '北側全体 19.70（15.70＋4.00）', fs=14)
    z.callout(complex(0, 1.06), '2.12', dirs=(-100, -80, -120), fs=13, color=GRAY, dists=(35, 50, 65))
    z.callout(complex(1.06, 0), '2.12', dirs=(180, 200, 160), fs=13, color=GRAY, dists=(35, 50, 65))
    z.free_text(complex(10, 10), '本件土地（5－2）\n366.14㎡', fs=16)
    z.free_text(complex(21.6, 7.5), '4－3', fs=14, color=GRAY)
    z.free_text(complex(21.6, 17.7), '4－1', fs=14, color=GRAY)
    z.free_text(complex(9.3, 23.0), '5－1', fs=14, color=GRAY)
    z.free_text(complex(-2.4, 11), '道路（116）', fs=14, color=GRAY)
    z.free_text(complex(10.5, -3.6), '道路\n（115）', fs=14, color=GRAY)
    save(fig, [z], 'R3_dai22mon_zu07_shikichi_henchou')




# ======================================================================
# 2026-10-26追加：最新の基準（6-2）で、わなの会話の直後に専用の図がなかった箇所の図（固定配置の整理図）
# ======================================================================

def zu01():
    """事実関係の時系列メモ。"""
    fig, ax = C.fixed_figure('事実関係の時系列　今の所有者は栄一', w=17, h=9.5, rect=(0.02, 0.11, 0.96, 0.77))
    ev = [(10, '平成15年4月3日', '本件建物を新築\n（共同住宅として登記）', BLUE, 1),
          (30, '令和元年8月31日\n（事実関係2）', 'リフォーム工事\n（イ）部分の玄関が1つに', BLUE, -1),
          (50, '令和3年9月10日\n（事実関係4）', '栄一が遺言書を作成\n（まだ効力は生じない）', GRAY, 1),
          (70, '令和3年10月17日\n（事実関係6）', '本件登記申請\n建物区分登記（問1・問3）', RED, -1),
          (90, '将来\n（事実関係7）', '遺言の効力が生じ\n栄二が（ロ）部分を相続\n→ 問2の申請', GREEN, 1)]
    ax.annotate('', xy=(99, 50), xytext=(1, 50), arrowprops=dict(arrowstyle='-|>', lw=2.4, color=GRAY))
    for x, d, t, col, up in ev:
        ax.plot([x], [50], 'o', ms=14, color=col)
        yd = 66 if up > 0 else 34
        ax.plot([x, x], [50, yd - (2 if up > 0 else -2)], color=col, lw=1.6)
        ax.text(x, yd + (20 if up > 0 else -2), d, ha='center', va='center' if up > 0 else 'top',
                fontsize=16, weight='bold', color=col, linespacing=1.3)
        ax.text(x, yd + (6 if up > 0 else -18), t, ha='center', va='center', fontsize=15, linespacing=1.4)
    C.caption(fig, ['令和3年10月17日の時点で、所有権の登記名義人は栄一。遺言は書いた人が亡くなって初めて効力が生じる',
                    '問1・問3の申請人は田宮栄一（住所 A市B町三丁目5番1号）。問2は将来、（ロ）部分が栄二に相続されたあとの話'], fs=14)
    C.save_fixed(fig, 'R3_dai22mon_zu01_jikeiretsu')


def zu02():
    C.card_figure('R3_dai22mon_zu02_kubun_bunkatsu', '建物区分登記か、建物分割登記か',
                  [('建物区分登記（本件）\n不動産登記法第54条第1項第2号', BLUE,
                    ['*1個の建物を壁で切り分け', '*別々の建物にする', '', '区分前：5番2（1個の建物）', '　　　↓', '区分後：（イ）・（ロ）の2個\n（区分建物）', '',
                     '本件は附属建物のない1棟を\n壁で（イ）と（ロ）に切り分ける']),
                   ('建物分割登記（本件ではない）\n不動産登記法第54条第1項第1号', RED,
                    ['*附属建物を別の建物にする', '', '分割前：主である建物＋附属建物\n（1個の登記記録）', '　　　↓', '分割後：別々の登記記録', '',
                     'もともと別々の棟（例：母屋と物置）\nを分ける登記'])],
                  ['本件は1棟の建物そのものを壁を境に切り分けるので「区分」。分割ではない'])


def zu03():
    C.card_figure('R3_dai22mon_zu03_shinseinin', '申請人は、今の所有者',
                  [('誤り：長男・栄太', RED,
                    ['*遺言で（イ）部分を取得する人', '', '遺言書は、書いた人が亡くなって', 'はじめて効力が生じる', '', '栄一はまだ存命\n→ まだ栄太のものではない']),
                   ('正解：田宮栄一', GREEN,
                    ['*今の所有権の登記名義人', '', '本件建物は今も栄一の名義', '', '申請人の住所\nA市B町三丁目5番1号', '', '遺言は、この登記をする\n動機にすぎない'])],
                  ['申請人は「今の所有者」。遺言で将来取得する人ではない'])


def zu04():
    C.card_figure('R3_dai22mon_zu04_shurui', '区分後の種類は、玄関の数で見直す',
                  [('（イ）部分　→　居宅', BLUE,
                    ['1階も2階も同じ玄関を使う', '（リフォーム工事後・事実関係2）', '', '玄関は1つ', '→ 1世帯分の住まい', '', '*種類は「居宅」']),
                   ('（ロ）部分　→　共同住宅', GREEN,
                    ['1階の住戸・2階の住戸が', 'それぞれ自分の玄関を持つ', '', '玄関は住戸ごとに別', '→ 別々の世帯が暮らす', '', '*種類は「共同住宅」'])],
                  ['区分前の「共同住宅」を写さず、区分後の1個1個の使い方で決める'])


def zu06():
    C.card_figure('R3_dai22mon_zu06_chuu_shiwake', '注の番号は3か所でかぶる　書き分けて読む',
                  [('問題文の注1〜4', BLUE,
                    ['1 行為・書類は全て適法', '2 書面申請', '*3 建物図面1/500\n　各階平面図1/250', '*4 字は明確に。訂正は線を\n　引いて書く（押印・字数は不要）']),
                   ('図1の（注）1〜6', GREEN,
                    ['1 単位はメートル', '2 （　）内は地番', '3 ［　］内は敷地の辺長', '*4 距離は筆界から外壁まで', '*5 北は敷地西側の道路と平行', '6 隅切り以外は全て直角']),
                   ('図4の（注）1〜5', RED,
                    ['*1 測定値は柱・壁の中心\n　（壁心）からの距離', '*2 柱の中心から内壁まで\n　10センチメートル', '3 （ロ）1階＝（あ）＋Ⓐ\n　（ロ）2階＝（い）', '*4 △▲は各階の重なる柱', '5 Ⓐの詳細は詳細図のとおり'])],
                  ['会話では「問題文の注3」「図1の（注）5」「図4の（注）2」のように書き分ける', '太字は、この問題の解答に直接効く注'], fs=15)


def zu08():
    C.card_figure('R3_dai22mon_zu08_kaku_kakanai', '建物図面（イ）に書くもの・書かないもの',
                  [('書くもの', BLUE,
                    ['*（イ）部分の1階を実線', '*残りの1階（（ロ）部分）を点線', '', '*筆界から外壁までの距離\n（北 1.00　西 2.50・2.50）', '本件土地の地番（5－2）と\n周りの地番・道路', '方位・縮尺1/500',
                     '家屋番号（B町三丁目5番2の1）\n建物の所在（A市B町三丁目5番地2）']),
                   ('書かないもの', RED,
                    ['*敷地の辺長（作図チェック用）', '', '*「建物の存する部分」\n（（イ）部分は1階から始まるので要らない）', '', '申請人の氏名\n（「（略）」と印刷済み）', '', '各階の寸法・床面積\n（各階平面図に書く）'])],
                  ['建物図面に書くのは、位置が分かる情報。寸法や面積は各階平面図に書く'], fs=14)


def zu11():
    C.card_figure('R3_dai22mon_zu11_kensan_wana', '検算が「合った」のは、壁心のまま測ったから',
                  [('誤り：壁心のまま 86.50', RED,
                    ['区分前の1階 173.00 ÷ 2 ＝ 86.50', '', '検算：86.50 × 2 ＝ 173.00', '→ 登記記録の1階（173.00）と一致', '', '*合って当然', '区分前の測り方（壁心）を\n半分にしただけ']),
                   ('正解：内法で 82.74', GREEN,
                    ['区分後の（イ）部分は専有部分\n壁の内側の線（内法）で測る', '', '検算：82.74 × 2 ＝ 165.48', '→ 173.00とは合わなくてよい', '', '*壁の厚みの分だけ小さい', '（一棟の173.00は壁心のまま）'])],
                  ['区分前の測り方で計算すれば、合うのは当たり前。区分後の測り方では、合わないのが正しい'])


def zu12():
    C.table_figure('R3_dai22mon_zu12_hiroinaoshi', '図4の寸法（壁心）を、辺ごとに内法へ拾い直す',
                   ['辺（（イ）部分の1階）', '図4の寸法\n（壁の中心）', '引く長さ', '内法\n（求積に使う）'],
                   [['北側', '6.50', '0.10×2＝0.20', ('*6.30', GREEN, 0.12)],
                    ['南側', '8.00', '0.20', ('*7.80', GREEN, 0.12)],
                    ['西側', '11.00', '0.20', ('*10.80', GREEN, 0.12)],
                    ['東側', '10.00', '0.20', ('*9.80', GREEN, 0.12)],
                    ['北東の欠け\n（横×縦）', '1.50×1.00', '引かない（欠けを囲む壁も\n同じ向きに0.10ずつずれる）', ('*1.50×1.00', GREEN, 0.12)]],
                   [24, 20, 32, 24],
                   ['図4の（注）2：柱の中心から内壁まで10センチメートル → 両側で0.20ずつ引く',
                    '北の帯の縦1.00＋東側9.80＝西側10.80（内法でも辺どうしがつながる）'], fs=16)


def zu18():
    C.card_figure('R3_dai22mon_zu18_shikichiken', '敷地権の割合は、規約がなければ床面積の割合',
                  [('① 区分すると', BLUE,
                    ['*土地は「敷地権」になる', '栄一は土地（5番2）の所有者で、', '（イ）・（ロ）両方の', '専有部分の所有者', '土地の所有権は専有部分と', '切り離せなくなる', '（区分所有法第22条第1項', '本文・第3項）']),
                   ('② 割合は', GREEN,
                    ['*床面積の割合', '', '規約で別に定めなければ', '専有部分の床面積の割合', '（同法第22条第2項・第14条）', '', '（イ）82.74＋84.24＝166.98', '（ロ）82.74＋84.24＝166.98']),
                   ('③ 結論', RED,
                    ['*2分の1ずつ', '', '166.98：166.98 ＝ 1：1', '', '規約を定めなくても', '自然に2分の1になる', '', '*規約証明書は要らない'])],
                  ['規約証明書が要るのは、床面積の割合と違う割合にしたいとき（問2の③）'], fs=14)


def zu19():
    C.card_figure('R3_dai22mon_zu19_tenpu', '添付書類は3点　要るもの・要らないもの',
                  [('要るもの（3点）', GREEN,
                    ['*建物図面', '*各階平面図', '（区分後の建物のもの。\n不動産登記令別表16の項添付情報欄イ）', '', '*代理権限証書', '（調査士が代理するため）']),
                   ('要らないもの', RED,
                    ['*規約証明書', '（割合は床面積の割合のまま\n2分の1。規約で定め直さない）', '', '*所有権証明書', '（すでに栄一の名義で登記された\n建物を分けるだけで、\n所有者は変わらない）'])],
                  ['規約証明書を入れた4点は誤り。正解は、建物図面・各階平面図・代理権限証書の3点'])


def zu20():
    C.card_figure('R3_dai22mon_zu20_tourokumenkyozei', '登録免許税は、区分後の建物の個数で数える',
                  [('誤り：1,000円', RED,
                    ['書く（イ）部分の', '1個だけを数えた', '', '1個 × 1,000円']),
                   ('正解：2,000円', GREEN,
                    ['*区分後の建物は2個', '（イ）部分と（ロ）部分', '', '2個 × 1,000円 ＝ 2,000円', '（登録免許税法別表第一の一（十三）イ）', '', '問1で（ロ）部分の記載を省くのは書き方だけ', '申請は2個まとめて1件'])],
                  ['表示に関する登記は原則として非課税。建物の分割・区分・合併は例外で、区分後の建物1個につき1,000円'])


def zu21():
    C.card_figure('R3_dai22mon_zu21_ittou_kabe_uchinori', '一棟は壁心、専有部分は内法　同じ申請書の中で使い分ける',
                  [('一棟の建物の表示', BLUE,
                    ['*外側の壁の中心線（壁心）', '', '区分前の登記記録の数字を', 'そのまま写す', '', '1階 173.00㎡', '2階 176.00㎡', '', '内法で測り直さない']),
                   ('区分した建物（専有部分）の表示', GREEN,
                    ['*壁の内側の線（内法）', '', '1個1個の専有部分だけ', '測り直す', '', '（イ）1階 82.74㎡', '　　　2階 84.24㎡', '', '（不動産登記規則第115条）'])],
                  ['区分前の登記記録を写す欄と、区分後の建物を見て書き直す欄を分ける'])


def zu23():
    g = (GRAY, 0.18)
    C.table_figure('R3_dai22mon_zu23_kubun_hyouji', '区分した建物の表示（イ）　1行目は写す、2行目は書き直す',
                   ['', '家屋番号', '種類', '構造', '床面積', '原因及びその日付'],
                   [['1行目\n区分前の\n本件建物', ('5番2',) + g, ('共同住宅',) + g, ('鉄骨造スレートぶき\n2階建',) + g, ('1階 173.00\n2階 176.00',) + g,
                     ('*5番2の1、\n5番2の2に区分', BLUE, 0.12)],
                    ['2行目\n区分後の\n（イ）部分', ('*（イ）\nB町三丁目5番2の1', RED, 0.12), ('*居宅', RED, 0.12), ('*鉄骨造スレートぶき\n2階建', RED, 0.12),
                     ('*1階 82.74\n2階 84.24', RED, 0.12), ('*5番2から区分', RED, 0.12)]],
                   [12, 18, 10, 22, 16, 22],
                   ['灰色：登記記録を写す　赤：区分後の建物を見て書く（種類は居宅、床面積は内法、符号（イ）を付ける）', '原因は2行とも日付なし（区分は形成的登記）'],
                   fs=15, row_h=30)


def zu24():
    C.card_figure('R3_dai22mon_zu24_shikichiken_genin', '敷地権の表示の原因は「令和3年10月17日敷地権」',
                  [('誤り：「記載不要」', RED,
                    ['問1のただし書き：敷地権の表示に', '関する登記の申請が不要なら', '「記載不要」と書く', '', '*本件は申請が要る', '栄一は土地（5番2）の所有者で', '両方の専有部分の所有者', '→ 敷地権が生じる', '→「記載不要」は使わない']),
                   ('正解：日付を書く', GREEN,
                    ['*令和3年10月17日敷地権', '', '敷地権は、区分建物に', 'なったときに生じる権利', '本問では区分の登記を申請した', '令和3年10月17日に生じたもの', '', '区分の原因：日付なし（形成的）', '敷地権の原因：日付あり'])],
                  ['区分の原因には日付を書かない。敷地権の原因には日付を書く'])


def zu25():
    C.card_figure('R3_dai22mon_zu25_kubun_kubun', '分ける対象で、登記の目的の名前が変わる',
                  [('問1：建物区分登記', BLUE,
                    ['*分ける対象：普通の建物', '（区分建物ではない5番2）', '', '　　　↓', '（イ）・（ロ）の2個の', '区分建物にする', '', '登記の目的：建物区分登記']),
                   ('問2：区分建物区分登記', GREEN,
                    ['*分ける対象：（ロ）部分', '（すでに区分建物）', '', '　　　↓', '（あ）部分・（い）部分等に', 'さらに分ける', '', '登記の目的：区分建物区分登記'])],
                  ['「普通の建物を区分する」のか、「すでに区分建物のものをさらに区分する」のかを見る'])


def zu26():
    C.card_figure('R3_dai22mon_zu26_maruA_yukamenseki', 'Ⓐ部分は共用部分ではなく、（い）部分等の1階部分',
                  [('誤り：共用部分として外す', RED,
                    ['「玄関と階段だけなら', 'みんなで使う共用部分」（藍子）', '', '共用部分：数個の専有部分に通ずる', '廊下・階段室など', '（区分所有法第4条第1項）', '', 'Ⓐは（い）部分だけが使う', '玄関と階段']),
                   ('正解：床面積に入れる', GREEN,
                    ['*Ⓐ部分＋（い）部分＝（い）部分等', '', 'Ⓐの階段を上ると2階の（い）部分', '（あ）部分とは壁で仕切られ', '行き来できない（Ⓐ詳細図）', '', '1階：Ⓐ部分　2階：（い）部分', '→ 2階建の専有部分'])],
                  ['図4の（注）3：（あ）部分と（い）部分及びⒶ部分は、それぞれ構造上独立している'])


# ======================================================================
# 座標の図（敷地・建物）
# ======================================================================

def dim_line(z, p, q, text, offsets=((12, 0),), dirs=None):
    ax = z.ax
    ax.annotate('', xy=xy(q), xytext=xy(p),
                arrowprops=dict(arrowstyle='<->', lw=1.4, color=BLACK, shrinkA=0, shrinkB=0), zorder=4)
    z.segments.append((xy(p), xy(q)))
    m = (p + q) / 2
    if dirs:
        return z.callout(m, text, dirs=dirs, fs=15, dists=(40, 55, 70))
    return z.free_text(m, text, fs=15, offsets=offsets)


def zu09():
    """建物が5番2の筆の中に収まるか（所在の確認）。"""
    fig, axes = new_figure('建物は5番2の中だけに収まる（所在の確認）',
                           '東の壁：西側の筆界から 2.50＋16.00＝18.50 → 5番1との境（19.70）まで 1.20\n'
                           '南の壁：北側の筆界から 1.00＋11.00＝12.00 → 道路（116）との境（18.70）まで 6.70',
                           w=16, h=12.5)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(SITE, color=BLACK, lw=2.4, fill=BLUE, alpha=0.06)
    z.poly([to_site(p) for p in P(WHOLE1)], color=RED, lw=2.4, fill=RED, alpha=0.12)
    fit(ax, SITE, margin=0.10, extra=[(-4.5, 24.5), (25.5, -3.8)], pad_aspect=True)
    z.north_arrow()
    dim_line(z, complex(12.0, 18.5), complex(12.0, 19.7), '1.20', dirs=(0, 20, -20), )
    dim_line(z, complex(0, 14.5), complex(6.7, 14.5), '6.70', dirs=(0, 20, -20))
    z.callout(complex(1.0, 1.0), '隅切り（2.12）に\nかからない', dirs=(-135, -120, -150), fs=14, color=GRAY, dists=(45, 60, 80))
    z.free_text(complex(12.2, 9.3), '一棟の建物\n（5番2の中だけ）', fs=16, weight='bold', color=RED)
    z.free_text(complex(3.3, 7.0), '本件土地（5－2）', fs=15)
    z.free_text(complex(9.3, 22.2), '5－1', fs=14, color=GRAY)
    save(fig, [z], 'R3_dai22mon_zu09_shozai_kakunin')


def zu16():
    """各階平面図（イ）に書くもの（引き出しつきの拡大図。答案用紙の枠の中の実寸の図は図17）。"""
    fig, axes = new_figure('各階平面図（イ）に書くもの',
                           '内法の寸法で1階・2階を書き分け、符号（イ）を付ける。2階には1階の北東の欠けの位置を点線で示す',
                           w=18, h=10.5, ncols=2)
    fig.subplots_adjust(top=0.85, bottom=0.30)
    zs = []
    tables = ['求積表\n6.30×1.00＝6.3000\n7.80×9.80＝76.4400\n計　82.7400\n床面積　82.74㎡',
              '求積表\n7.80×10.80＝84.2400\n床面積　84.24㎡']
    for k, (pts, labels, name) in enumerate([
            (I1, ['6.30', '1.00', '', '9.80', '7.80', '10.80'], '1階'),
            (I2, ['7.80', '10.80', '7.80', '10.80'], '2階')]):
        ax = axes[k]
        z = Zu(ax, fontsize=13)
        ax.set_title(name, fontsize=17, weight='bold')
        fit(ax, P(I2), margin=0.22, pad_aspect=True)
        if k == 1:
            z.poly(P([(6.4, 0.1), (6.4, 1.1), (7.9, 1.1)]), color=BLACK, lw=1.4, ls=':', closed=False)
            z.callout(B(7.15, 1.1), '1階の欠けの位置\n（点線）', dirs=(-45, -30, -60), fs=13, color=GRAY)
        z.poly(P(pts), color=BLACK, lw=2.4)
        tri(z, B(0.1, 0.1))
        dims(z, P(pts), labels, fs=13)
        if k == 0:
            z.callout(B(7.15, 1.1), '1.50', dirs=(60, 80, 40), fs=13, dists=(30, 45, 60))
        z.callout(B(0.1, 0.1), '各階の重なる柱（△）', dirs=(135, 150, 120), fs=13, color=GRAY, dists=(40, 55, 70))
        z.free_text(B(4.0, 6.0), '（イ）', fs=16, weight='bold')
        zs.append(z)
        fig.text(0.25 + 0.5 * k, 0.185, tables[k], ha='center', va='center', fontsize=14, linespacing=1.5)
    assert round(area_es(I1), 4) == 82.74 and round(area_es(I2), 4) == 84.24
    save(fig, zs, 'R3_dai22mon_zu16_kakukai_kaku')


def zu22():
    """構造：縦割り（屋根まで書く）と階層的な区分（屋根の種類を書かない）。"""
    fig, ax = C.fixed_figure('構造は、縦割りなら屋根まで書く', w=17, h=9.5, rect=(0.02, 0.11, 0.96, 0.77))
    for x0, ttl, col in ((2, '本問：縦割りの区分', BLUE), (52, '階層的な区分（上下で分ける）', GREEN)):
        C.rbox(ax, x0, 4, 45, 80, col, alpha=0.06)
        ax.text(x0 + 22.5, 92, ttl, ha='center', va='center', fontsize=20, weight='bold', color=col)
    # 縦割り
    ax.add_patch(Rectangle((8, 26), 16, 30, facecolor=BLUE, alpha=0.22, edgecolor=BLACK, lw=2))
    ax.add_patch(Rectangle((24, 26), 16, 30, facecolor=GREEN, alpha=0.22, edgecolor=BLACK, lw=2))
    ax.add_patch(MPoly([(7, 56), (24, 56), (24, 66), (15.5, 66)], closed=True, facecolor=BLUE, alpha=0.40, edgecolor=BLACK, lw=2))
    ax.add_patch(MPoly([(24, 56), (41, 56), (32.5, 66), (24, 66)], closed=True, facecolor=GREEN, alpha=0.40, edgecolor=BLACK, lw=2))
    ax.plot([8, 40], [41, 41], color=BLACK, lw=1.2, ls='--')
    ax.text(16, 48.5, '（イ）2階', ha='center', va='center', fontsize=14)
    ax.text(16, 33.5, '（イ）1階', ha='center', va='center', fontsize=14)
    ax.text(32, 48.5, '（ロ）2階', ha='center', va='center', fontsize=14)
    ax.text(32, 33.5, '（ロ）1階', ha='center', va='center', fontsize=14)
    ax.text(24.5, 17, '*（イ）は1階から屋根まで丸ごと\n　＝専有部分にも屋根がある'.replace('*', ''), ha='center', va='center', fontsize=15, linespacing=1.4)
    ax.text(24.5, 8.5, '構造「鉄骨造スレートぶき2階建」', ha='center', va='center', fontsize=16, weight='bold', color=BLUE)
    # 階層的
    ax.add_patch(Rectangle((60, 26), 30, 15, facecolor=BLUE, alpha=0.22, edgecolor=BLACK, lw=2))
    ax.add_patch(Rectangle((60, 41), 30, 15, facecolor=GREEN, alpha=0.22, edgecolor=BLACK, lw=2))
    ax.add_patch(MPoly([(59, 56), (91, 56), (75, 66)], closed=True, facecolor=GREEN, alpha=0.40, edgecolor=BLACK, lw=2))
    ax.text(75, 33.5, '下の階の部分', ha='center', va='center', fontsize=14)
    ax.text(75, 48.5, '上の階の部分', ha='center', va='center', fontsize=14)
    ax.text(74.5, 17, '一部だけを1個の建物とするとき\n屋根の種類を記録することを要しない', ha='center', va='center', fontsize=15, linespacing=1.4)
    ax.text(74.5, 8.5, '構造「鉄骨造2階建」など（準則第81条第3項）', ha='center', va='center', fontsize=15, weight='bold', color=GREEN)
    C.caption(fig, ['藍子の誤答「鉄骨造2階建」は、階層的な区分の書き方。縦割りの（イ）部分は屋根まで書いて「鉄骨造スレートぶき2階建」'], fs=15)
    C.save_fixed(fig, 'R3_dai22mon_zu22_kouzou_tatewari')


# Ⓐ部分（Ⓐ詳細図。壁の中心線の寸法。東・南の順。原点は北西の角）
A_W = [(0, 0), (2.7, 0), (2.7, 4.5), (0.7, 4.5), (0.7, 3.0), (0, 3.0)]
A_I = [(0.1, 0.1), (2.6, 0.1), (2.6, 4.4), (0.8, 4.4), (0.8, 2.9), (0.1, 2.9)]
A_I_STRIPS = [rect(0.1, 0.1, 2.6, 2.9), rect(0.8, 2.9, 2.6, 4.4)]
assert round(area_es(A_I), 2) == 9.70 == round(sum(area_es(r) for r in A_I_STRIPS), 2)


def zu27():
    fig, axes = new_figure('Ⓐ部分の床面積：詳細図の寸法（壁心）を内法へ直して求積',
                           '北側 2.70−0.20＝2.50、東側 4.50−0.20＝4.30、南側 2.00−0.20＝1.80、西側の上 3.00−0.20＝2.80。欠け0.70×1.50は変わらない',
                           w=18, h=10.5, ncols=2)
    fig.subplots_adjust(top=0.85, bottom=0.22)
    z = Zu(axes[0], fontsize=13)
    z.poly(P(A_W), color=BLACK, lw=2.4)
    axes[0].set_title('Ⓐ詳細図の寸法（壁の中心から）', fontsize=16, weight='bold')
    fit(axes[0], P(A_W), margin=0.28, pad_aspect=True)
    dims(z, P(A_W), ['2.70\n（1.50＋1.20）', '4.50\n（2.30＋2.20）', '2.00', '1.50', '0.70', '3.00'], fs=12)
    z.free_text(B(1.4, 1.5), 'Ⓐ', fs=18, weight='bold', color=RED)
    z2 = Zu(axes[1], fontsize=13)
    for r, c in zip(A_I_STRIPS, [ORANGE, BLUE]):
        z2.poly(P(r), color=c, lw=0, fill=c, alpha=0.25, check=False)
    z2.line(B(0.1, 2.9), B(0.8, 2.9), color=GRAY, lw=1.0, ls='--')
    z2.poly(P(A_I), color=BLACK, lw=2.4)
    axes[1].set_title('内法（柱の中心から0.10内側）', fontsize=16, weight='bold', color=GREEN)
    fit(axes[1], P(A_W), margin=0.28, pad_aspect=True)
    dims(z2, P(A_I), ['2.50', '4.30', '1.80', '1.50', '0.70', '2.80'], fs=13)
    z2.free_text(B(1.35, 1.5), '2.50×2.80\n＝7.00', fs=13)
    z2.free_text(B(1.9, 3.7), '1.80×1.50\n＝2.70', fs=13)
    fig.text(0.5, 0.13, 'Ⓐ部分　7.00＋2.70＝9.70㎡', ha='center', va='center', fontsize=18, weight='bold')
    save(fig, [z, z2], 'R3_dai22mon_zu27_maruA_kyuuseki')


def zu29():
    """敷地権の割合：（ロ）の中の割合ではなく、土地全体に対する割合。"""
    fig, ax = C.fixed_figure('敷地権の割合は、土地全体に対する割合で書く', w=17, h=9.5, rect=(0.02, 0.11, 0.96, 0.77))
    ax.text(50, 94, '土地（5番2）の所有権＝33088分の33088', ha='center', va='center', fontsize=18, weight='bold')
    x0, w = 5, 90
    segs = [(16544, '（イ）部分（栄太）\n33088分の16544＝2分の1', BLUE), (7150, '（あ）部分\n33088分の7150', GREEN),
            (9394, '（い）部分等\n33088分の9394', RED)]
    x = x0
    for n, t, col in segs:
        wd = w * n / 33088
        ax.add_patch(Rectangle((x, 62), wd, 18, facecolor=col, alpha=0.25, edgecolor=BLACK, lw=2))
        ax.text(x + wd / 2, 71, t, ha='center', va='center', fontsize=14, linespacing=1.4)
        x += wd
    x1 = x0 + w * 16544 / 33088
    ax.annotate('', xy=(x0 + w, 56), xytext=(x1, 56), arrowprops=dict(arrowstyle='<->', lw=1.6, color=GREEN))
    ax.text((x1 + x0 + w) / 2, 52, '（ロ）部分＝2分の1（栄二が相続する分）', ha='center', va='center', fontsize=15, color=GREEN)
    C.rbox(ax, 2, 4, 46, 38, RED, alpha=0.06)
    C.rbox(ax, 52, 4, 46, 38, GREEN, alpha=0.06)
    ax.text(25, 37, '誤り：（ロ）の中での割合', ha='center', va='center', fontsize=17, weight='bold', color=RED)
    ax.text(25, 20, '（あ）71.50：（い）等93.94\n＝16544分の7150と16544分の9394\n（合計16544分の16544＝1になってしまう）',
            ha='center', va='center', fontsize=15, linespacing=1.5)
    ax.text(75, 37, '正解：土地全体に対する割合', ha='center', va='center', fontsize=17, weight='bold', color=GREEN)
    ax.text(75, 20, '16544分の7150 × 2分の1＝33088分の7150\n16544分の9394 × 2分の1＝33088分の9394\n（足すと33088分の16544＝2分の1）',
            ha='center', va='center', fontsize=15, linespacing=1.5)
    C.caption(fig, ['約分すると1504分の325・1504分の427だが、床面積の数字が見える形で書く'], fs=15)
    C.save_fixed(fig, 'R3_dai22mon_zu29_shikichiken_wariai')
# ---- 図13：誤り比較図（壁心／内法） ----
def zu13():
    fig, axes = new_figure('（イ）部分1階の床面積：壁心か、内法か',
                           '区分建物の床面積は壁その他の区画の内側線で囲まれた部分（不動産登記規則第115条）。欠けの大きさ1.50×1.00は変わらない',
                           w=18, h=9.5, ncols=3, width_ratios=[1, 0.72, 1])
    fig.subplots_adjust(top=0.84)
    # 誤り（壁心）
    z = Zu(axes[0], fontsize=13)
    z.poly(P(I1_WALL), color=RED, lw=2.4, fill=RED, alpha=0.18)
    axes[0].set_title('誤り：壁心のまま 86.50㎡（藍子）', fontsize=16, weight='bold', color=RED)
    fit(axes[0], P(I1_WALL), margin=0.2, pad_aspect=True)
    dims(z, P(I1_WALL), ['6.50', '1.00', '', '10.00', '8.00', '11.00'], fs=13)
    z.callout(B(7.25, 1), '1.50', dirs=(60, 80, 40), fs=13, dists=(30, 45, 60))
    z.free_text(B(4, 6), '6.50×1.00\n＋8.00×10.00\n＝86.50㎡', fs=13, color=RED)
    # 拡大（壁の断面：北西の角）
    z2 = Zu(axes[1], fontsize=12)
    wall = [complex(0.25, -0.25), complex(0.25, 0.9), complex(-0.1, 0.9), complex(-0.1, 0.1), complex(-0.9, 0.1),
            complex(-0.9, -0.25)]
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
    z2.callout(complex(-0.05, 0.55), '0.10（図4の（注）2）', dirs=(-60, -40, -80), fs=12, color=RED)
    z2.callout(complex(0.15, -0.0), '壁の中心線（壁心）', dirs=(90, 70, 110), fs=12)
    z2.callout(complex(-0.6, 0.1), '内壁の面（内法）', dirs=(-90, -110, -70), fs=12, color=GREEN)
    # 正解（内法）
    z3 = Zu(axes[2], fontsize=13)
    z3.poly(P(I1_WALL), color=GRAY, lw=1.0, ls=':', check=False)
    z3.poly(P(I1), color=GREEN, lw=2.4, fill=GREEN, alpha=0.20)
    axes[2].set_title('正解：内法で 82.74㎡', fontsize=16, weight='bold', color=GREEN)
    fit(axes[2], P(I1_WALL), margin=0.2, pad_aspect=True)
    dims(z3, P(I1), ['6.30', '1.00', '', '9.80', '7.80', '10.80'], fs=13)
    z3.callout(B(7.15, 1.1), '1.50', dirs=(60, 80, 40), fs=13, dists=(30, 45, 60))
    z3.free_text(B(4, 6), '6.30×1.00\n＋7.80×9.80\n＝82.74㎡', fs=13, color=GREEN)
    save(fig, [z, z2, z3], 'R3_dai22mon_zu13_ayamari_hikaku')


# ---- 図14・図15：（イ）部分の求積図 ----
def zu14():
    fig, axes = new_figure('（イ）部分1階の床面積求積図（内法）',
                           '6.30×1.00＋7.80×9.80＝82.74㎡。△印は各階の重なる柱の位置（図4の（注）4）',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    for r, c in zip(I1_STRIPS, [ORANGE, BLUE]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.25, check=False)
    z.line(B(0.1, 1.1), B(6.4, 1.1), color=GRAY, lw=1.0, ls='--')
    z.poly(P(I1), color=BLACK, lw=2.4)
    fit(ax, P(I1), margin=0.22, pad_aspect=True)
    z.north_arrow()
    tri(z, B(0.1, 0.1))
    dims(z, P(I1), ['6.30', '1.00', '1.50', '9.80', '7.80', '10.80'], fs=15)
    z.free_text(B(3.25, 0.6), '6.30×1.00', fs=14)
    z.free_text(B(4.0, 6.0), '7.80×9.80', fs=16)
    z.free_text(B(4.0, 12.3), '1階　床面積：82.74㎡', fs=17, weight='bold')
    save(fig, [z], 'R3_dai22mon_zu14_1kai_kyuuseki')


def zu15():
    fig, axes = new_figure('（イ）部分2階の床面積求積図（内法）',
                           '7.80×10.80＝84.24㎡。点線は1階の北東の欠け（1.50×1.00）の位置',
                           w=16, h=12)
    ax = axes[0]
    z = Zu(ax, fontsize=15)
    z.poly(P(I2), color=BLACK, lw=2.4, fill=BLUE, alpha=0.22)
    z.poly(P([(6.4, 0.1), (6.4, 1.1), (7.9, 1.1)]), color=BLACK, lw=1.4, ls='--', closed=False)
    fit(ax, P(I2), margin=0.22, pad_aspect=True)
    z.north_arrow()
    tri(z, B(0.1, 0.1))
    dims(z, P(I2), ['7.80', '10.80', '7.80', '10.80'], fs=15)
    z.free_text(B(4.0, 6.0), '7.80×10.80', fs=16)
    z.callout(B(7.15, 1.1), '1階の欠けの位置（点線）', dirs=(-45, -30, -60), fs=13)
    z.free_text(B(4.0, 12.3), '2階　床面積：84.24㎡', fs=17, weight='bold')
    save(fig, [z], 'R3_dai22mon_zu15_2kai_kyuuseki')


# ---- 図28：問2の求積図 ----
def zu28():
    fig, axes = new_figure('問2：（ロ）部分を（あ）部分と（い）部分等に分けたときの床面積（内法）',
                           '（あ）部分 71.50㎡、（い）部分等＝Ⓐ部分9.70＋（い）部分84.24＝93.94㎡。敷地権の割合は 33088分の7150・33088分の9394',
                           w=18, h=11, ncols=2)
    fig.subplots_adjust(top=0.85)
    z = Zu(axes[0], fontsize=12)
    z.poly(P(R1_WALL), color=GRAY, lw=1.0, ls=':', check=False)
    for r, c in zip(A_STRIPS, [ORANGE, YELLOW, BLUE, PURPLE]):
        z.poly(P(r), color=c, lw=0, fill=c, alpha=0.28, check=False)
    for r in MARU_STRIPS:
        z.poly(P(r), color=RED, lw=0, fill=RED, alpha=0.28, check=False)
    z.line(B(0.1, 1.1), B(1.6, 1.1), color=GRAY, lw=1.0, ls='--')
    z.line(B(1.6, 1.1), B(7.9, 1.1), color=GRAY, lw=1.0, ls='--')
    z.line(B(0.1, 6.4), B(5.2, 6.4), color=GRAY, lw=1.0, ls='--')
    z.line(B(0.1, 9.6), B(5.2, 9.6), color=GRAY, lw=1.0, ls='--')
    z.line(B(6.1, 9.4), B(7.9, 9.4), color=GRAY, lw=1.0, ls='--')
    z.poly(P(A_PART), color=BLACK, lw=2.2)
    z.poly(P(MARU_A), color=RED, lw=2.2)
    axes[0].set_title('1階：（あ）部分とⒶ部分', fontsize=16, weight='bold')
    fit(axes[0], P(R1_WALL), margin=0.22, pad_aspect=True)
    z.north_arrow()
    z.free_text(B(4.75, 0.6), '6.30×1.00', fs=12)
    z.free_text(B(4.0, 3.75), '7.80×5.30', fs=13)
    z.free_text(B(2.65, 8.0), '5.10×3.20', fs=13)
    z.free_text(B(3.0, 10.25), '5.80×1.30', fs=11)
    z.callout(B(6.65, 8.0), 'Ⓐ 2.50×2.80', dirs=(0, 20, -20), fs=12, color=RED)
    z.callout(B(7.0, 10.15), 'Ⓐ 1.80×1.50', dirs=(0, -20, -40), fs=12, color=RED)
    z.free_text(B(4.0, 12.6), '（あ）部分 71.50㎡　Ⓐ部分 9.70㎡', fs=14, weight='bold')
    z2 = Zu(axes[1], fontsize=13)
    z2.poly(P(R1_WALL), color=GRAY, lw=1.0, ls=':', check=False)
    z2.poly(P(I2), color=BLACK, lw=2.2, fill=RED, alpha=0.25)
    axes[1].set_title('2階：（い）部分', fontsize=16, weight='bold')
    fit(axes[1], P(R1_WALL), margin=0.22, pad_aspect=True)
    dims(z2, P(I2), ['7.80', '10.80', '', ''], fs=14)
    z2.free_text(B(4.0, 6.0), '7.80×10.80\n＝84.24㎡', fs=14)
    z2.free_text(B(4.0, 12.6), '（い）部分等 9.70＋84.24＝93.94㎡', fs=14, weight='bold', color=RED)
    save(fig, [z, z2], 'R3_dai22mon_zu28_toi2_kyuuseki')


# ---- 図30：本番で解く順番（固定配置の図なので重なり検査の対象外） ----
def zu30():
    setup_font()
    fig = plt.figure(figsize=(16, 8.5), dpi=100)
    fig.patch.set_facecolor('white')
    fig.suptitle('本番で解く順番　床面積のいらない欄を先に、求積と作図は後に', fontsize=24, weight='bold', y=0.965)
    ax = fig.add_axes([0.03, 0.22, 0.94, 0.66])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    steps = [
        ('①', '前文・注・\n問1〜問3を\n読む', '問1は（イ）部分\nだけ書く\n（問題文の注3\nの縮尺）', BLUE),
        ('②', '事実関係・\n登記記録', '建物区分登記\n玄関1つで居宅\n申請人は栄一', BLUE),
        ('③', '床面積の\nいらない欄', '第1欄の大部分\n問2の①③', BLUE),
        ('④', '寸法の\n累計メモ', '東へ6.50・8.00\n南へ1.00・11.00\n内法は0.10内側', RED),
        ('⑤', '（イ）部分の\n内法の求積', '82.74・84.24\n（第1欄の床面積）', RED),
        ('⑥', '第3欄の\n作図', '各階平面図と\n建物図面\n1.00・2.50・2.50', RED),
        ('⑦', '問2の②と\n見直し', '71.50・9.70\n→33088分の7150\n・9394', GRAY),
    ]
    w, h, gap = 12.4, 44, 1.9
    y0 = 36
    for i, (no, t, ran, col) in enumerate(steps):
        x = 1 + i * (w + gap)
        ax.add_patch(plt.Rectangle((x, y0), w, h, facecolor=col, alpha=0.16, edgecolor=col, lw=2))
        ax.text(x + w / 2, y0 + h - 3, no, ha='center', va='top', fontsize=24, color=col, weight='bold')
        ax.text(x + w / 2, y0 + h / 2 - 5, t, ha='center', va='center', fontsize=15, linespacing=1.35)
        ax.text(x + w / 2, y0 - 3, ran, ha='center', va='top', fontsize=13, color=col, linespacing=1.4)
        if i < len(steps) - 1:
            ax.annotate('', xy=(x + w + gap - 0.2, y0 + h / 2), xytext=(x + w + 0.2, y0 + h / 2),
                        arrowprops=dict(arrowstyle='-|>', lw=1.6, color=GRAY))
    ax.text(1 + 1.5 * (w + gap) - gap / 2, 91, '計算なしで書ける', ha='center', fontsize=15, color=BLUE, weight='bold')
    ax.annotate('', xy=(1 + 3 * (w + gap) - gap, 87), xytext=(1, 87), arrowprops=dict(arrowstyle='<->', lw=1.5, color=BLUE))
    ax.text(1 + 4.5 * (w + gap) - gap / 2, 91, 'いちばん時間を食う', ha='center', fontsize=15, color=RED, weight='bold')
    ax.annotate('', xy=(1 + 6 * (w + gap) - gap, 87), xytext=(1 + 3 * (w + gap), 87),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color=RED))
    fig.text(0.5, 0.085, '③で書ける欄：登記の目的・添付書類・登録免許税・申請人・一棟の建物の表示・敷地権の目的である土地の表示・\n'
             '区分前の行・区分後の行の家屋番号・種類・構造・原因・敷地権の表示、問2の①区分建物区分登記と③規約証明書。\n'
             '区分前の半分の86.50は2倍すると登記記録と合ってしまうので、④で内法に切り替えてから求積する',
             ha='center', va='center', fontsize=14, linespacing=1.5)
    path = os.path.join(OUT, 'R3_dai22mon_zu30_toku_junban.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    print('[重なり検査] 図30: 解く順番（固定配置）\n  →', path)




# ======================================================================
# 答案用紙の第3欄（A3横）を原本の罫線から測った寸法（mm）で、実際の大きさに描く（図10・図17）
# 原本：../touan_youshi/R3_dai22mon_touan_youshi.pdf の2ページ目。1枚の枠（x 80.58〜382.58、y 25.77〜256.77）の
# 左半分（〜231.58）が各階平面図（1/250）、右半分が建物図面（1/500）。座標は用紙の左上を原点にした mm（右へ x、下へ y）。
# ======================================================================
PX_PER_MM = 8                                      # 1mm を 8px（A4に印刷すると実寸）
PT = 72 / 25.4                                     # 1mm＝2.835pt
PAGE_RECTS = [(56.28, 12.22, 406.88, 274.82), (57.08, 13.02, 406.08, 274.02)]   # 用紙の外枠（二重線）
SHEET_LINES = [
    (382.58, 35.77, 382.58, 25.97, 1.13),
    (382.58, 246.77, 382.58, 35.77, 1.13),
    (382.58, 256.57, 382.58, 246.77, 1.13),
    (80.38, 256.77, 231.58, 256.77, 1.13),
    (231.58, 256.77, 382.78, 256.77, 1.13),
    (80.38, 25.77, 231.58, 25.77, 1.13),
    (80.58, 35.77, 80.58, 25.97, 1.13),
    (231.58, 25.77, 382.78, 25.77, 1.13),
    (80.58, 246.77, 80.58, 35.77, 1.13),
    (80.58, 256.57, 80.58, 246.77, 1.13),
    (231.58, 35.77, 231.58, 25.97, 1.13),
    (231.58, 256.57, 231.58, 246.77, 1.13),
    (240.38, 15.77, 264.58, 15.77, 1.13),
    (264.58, 15.77, 302.78, 15.77, 1.13),
    (240.58, 25.77, 240.58, 15.97, 1.13),
    (240.58, 35.57, 240.58, 25.77, 1.13),
    (240.38, 35.77, 264.58, 35.77, 1.13),
    (240.78, 25.77, 264.58, 25.77, 0.34),
    (264.58, 25.71, 264.58, 15.97, 0.34),
    (264.58, 25.77, 302.58, 25.77, 0.34),
    (264.58, 35.57, 264.58, 25.83, 0.34),
    (382.58, 35.57, 382.58, 25.97, 1.13),
    (264.58, 35.77, 302.58, 35.77, 1.13),
    (302.58, 35.77, 382.78, 35.77, 1.13),
    (302.58, 25.57, 302.58, 15.97, 1.13),
    (302.58, 25.77, 382.78, 25.77, 1.13),
    (189.58, 271.07, 189.58, 256.97, 1.7),
    (80.58, 271.07, 80.58, 256.97, 1.13),
    (80.38, 271.27, 99.58, 271.27, 1.13),
    (131.58, 271.27, 189.58, 271.27, 1.13),
    (80.38, 256.77, 99.58, 256.77, 1.13),
    (131.58, 256.77, 189.58, 256.77, 1.13),
    (199.58, 256.77, 223.78, 256.77, 1.13),
    (223.58, 271.07, 223.58, 256.97, 1.13),
    (199.58, 271.27, 223.78, 271.27, 1.13),
    (189.58, 256.77, 199.58, 256.77, 1.13),
    (189.58, 271.27, 199.58, 271.27, 1.13),
    (199.58, 271.07, 199.58, 256.97, 0.34),
    (189.34, 271.07, 189.34, 256.97, 0.34),
    (189.82, 271.07, 189.82, 256.97, 0.34),
    (99.58, 256.77, 131.58, 256.77, 1.13),
    (99.58, 271.27, 131.58, 271.27, 1.13),
    (99.58, 271.07, 99.58, 256.97, 0.34),
    (202.97, 269.22, 220.05, 258.81, 0.34),
    (239.58, 271.07, 239.58, 256.97, 1.13),
    (239.38, 271.27, 258.58, 271.27, 1.13),
    (258.58, 271.27, 348.58, 271.27, 1.13),
    (382.58, 271.07, 382.58, 256.97, 1.13),
    (348.58, 271.27, 358.58, 271.27, 1.13),
    (358.58, 271.27, 382.78, 271.27, 1.13),
    (258.58, 271.07, 258.58, 256.97, 0.34),
    (358.58, 271.07, 358.58, 256.97, 0.34),
    (348.34, 271.07, 348.34, 256.97, 0.34),
    (348.82, 271.07, 348.82, 256.97, 0.34),
    (239.38, 256.77, 258.58, 256.77, 1.13),
    (258.58, 256.77, 348.58, 256.77, 1.13),
    (348.58, 256.77, 358.58, 256.77, 1.13),
    (358.58, 256.77, 382.78, 256.77, 1.13),
    (361.97, 269.22, 379.05, 258.81, 0.34),
]
SHEET_TEXTS = [                                    # (左端x, 中央y, 文字の高さmm, 文字)
    (130.90, 23.0, 4.62, '各　階　平　面　図　（イ）'), (242.96, 21.4, 3.88, '家屋番号'), (312.51, 22.6, 4.62, '建　物　図　面　（イ）'),
    (242.96, 31.2, 3.88, '建物の所在'), (82.40, 264.6, 3.88, '作 成 者'), (109.79, 264.6, 3.88, '（略）'),
    (143.52, 268.4, 3.88, '（令和3年○月○日作成）'), (190.82, 264.6, 3.88, '縮尺'), (208.41, 261.5, 3.88, '1'),
    (212.67, 267.6, 3.88, '250'), (241.40, 264.6, 3.88, '申 請 人'), (297.64, 264.6, 3.88, '（略）'),
    (349.82, 264.6, 3.88, '縮尺'), (367.41, 261.5, 3.88, '1'), (371.66, 267.6, 3.88, '500')]


def sheet_canvas(x0, x1, y0, y1):
    """用紙の一部（x0〜x1 × y0〜y1 mm）を実寸（1mm＝8px）で描くキャンバスと、用紙の印刷済みの線・文字。"""
    setup_font()
    fig = plt.figure(figsize=((x1 - x0) / 25.4, (y1 - y0) / 25.4), dpi=PX_PER_MM * 25.4)
    fig.patch.set_facecolor('white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(x0, x1)
    ax.set_ylim(-y1, -y0)                          # 用紙は下向きが +y なので、−y を上向きに使う
    ax.axis('off')
    for r in PAGE_RECTS:
        ax.add_patch(Rectangle((r[0], -r[3]), r[2] - r[0], r[3] - r[1], fill=False, lw=1.13, ec=BLACK))
    for (a, b, c, d, w) in SHEET_LINES:
        ax.plot([a, c], [-b, -d], color=BLACK, lw=w, solid_capstyle='butt')
    for (x, y, mm, s) in SHEET_TEXTS:
        ax.text(x, -y, s, ha='left', va='center', fontsize=mm * PT, color=BLACK)
    return fig, ax


def S(x, y):
    """用紙の (x, y)mm を Zu の複素数（北＋東i）にする（北＝−y）。"""
    return complex(-y, x)


def save_sheet(fig, zs, name):
    for i, z in enumerate(zs):
        PROBLEMS.extend(z.check_overlaps(f'{name} パネル{i + 1}'))
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


# ---- 図10：建物図面（イ）の完成形（右半分・1/500。1m＝2mm） ----
SX0, SY0 = 288.0, 80.0         # 本件土地の北西の角の用紙上の位置（mm）。北側の線が y＝80、西側の線が x＝288


def site_xy(p):
    """敷地の座標（X北・Y東、m）→ 用紙の (x, y) mm。1/500 で 1m＝2mm。"""
    return (SX0 + 2.0 * p.imag, SY0 + 2.0 * (18.70 - p.real))


def zu10():
    fig, ax = sheet_canvas(222, 410, 2, 292)
    z = Zu(ax, fontsize=8.5)
    ax.text(316, -7.0, '建物図面（イ）の完成形（答案用紙の右半分・縮尺1/500の実際の大きさ）', ha='center', va='center',
            fontsize=5.2 * PT, weight='bold')

    def Z(p):
        return S(*site_xy(p))

    def line(p, q, lw=0.7, ls='-'):
        a, b = site_xy(p), site_xy(q)
        ax.plot([a[0], b[0]], [-a[1], -b[1]], color=INK, lw=lw, ls=ls, solid_capstyle='butt')
        z.segments.append((xy(S(*a)), xy(S(*b))))
    for i in range(len(SITE)):
        line(SITE[i], SITE[(i + 1) % len(SITE)], lw=0.8)
    line(S_43, complex(22.0, 15.70))                # 4-3と4-1の境
    line(S_NE, complex(22.0, 19.70))
    line(S_NE, complex(18.70, 23.0))                # 5-1の北側の線
    line(S_SE, complex(0, 23.0))
    i_site = [to_site(p) for p in P(I1_WALL)]
    ro_site = [to_site(p) for p in P(RO1_WALL)]
    for i in range(len(i_site)):
        line(i_site[i], i_site[(i + 1) % len(i_site)], lw=1.3)
    ro_pts = ro_site + [ro_site[0]]
    for i in range(len(ro_site) - 1):                  # （ロ）部分（（イ）との境の最後の辺は実線と重なるので描かない）
        line(ro_pts[i], ro_pts[i + 1], lw=0.7, ls=(0, (3.0 * PT / 0.7, 1.5 * PT / 0.7)))
    # 距離（北1.00、西2.50・2.50）：寸法線は敷地の中、数字は引き出し線で外に
    def dim(p, q, text, tp):
        a, b = site_xy(p), site_xy(q)
        ax.annotate('', xy=(b[0], -b[1]), xytext=(a[0], -a[1]), arrowprops=dict(arrowstyle='<->', lw=0.5, color=INK,
                                                                                 shrinkA=0, shrinkB=0, mutation_scale=6))
        z.segments.append((xy(S(*a)), xy(S(*b))))
        m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        ex = (tp[0] + 4.6, tp[1]) if tp[0] < m[0] - 3 else (tp[0], tp[1] + 2.0)
        ax.plot([m[0], ex[0]], [-m[1], -ex[1]], color=INK, lw=0.35)
        ax.text(tp[0], -tp[1], text, ha='center', va='center', fontsize=3.0 * PT, color=INK)
    dim(complex(18.70, 3.5), complex(17.70, 3.5), '1.00', (SX0 + 5.0, SY0 - 6.0))
    dim(complex(17.2, 0), complex(17.2, 2.5), '2.50', (SX0 - 12.0, site_xy(complex(17.2, 0))[1] - 2.0))
    dim(complex(7.2, 0), complex(7.2, 2.5), '2.50', (SX0 - 12.0, site_xy(complex(7.2, 0))[1] + 2.0))
    # 地番・道路・符号
    def label(p, s, mm=3.0, col=INK):
        a = site_xy(p)
        ax.text(a[0], -a[1], s, ha='center', va='center', fontsize=mm * PT, color=col, linespacing=1.2)
    label(complex(3.4, 11.0), '5－2')
    label(complex(20.2, 8.0), '4－3')
    label(complex(20.2, 17.7), '4－1', mm=2.6)
    label(complex(9.3, 22.0), '5－1')
    label(complex(-2.2, 11.0), '道路（116）')
    label(complex(11.2, -3.0), '道路\n（115）')
    label(complex(12.2, 6.5), '（イ）', mm=3.4)
    # 方位（右上）
    for (a, b, c, d) in ((345.57, 77.12, 345.57, 96.14), (338.33, 87.57, 352.31, 87.57), (345.57, 77.12, 342.85, 81.55),
                         (342.85, 81.55, 346.83, 84.12)):
        ax.plot([a, c], [-b, -d], color=INK, lw=0.5)
    ax.text(345.57, -73.5, 'N', ha='center', va='center', fontsize=3.0 * PT, color=INK)
    ax.text(264.58 + 19.0, -20.77, 'B町三丁目5番2の1', ha='center', va='center', fontsize=2.9 * PT, color=INK)
    ax.text(267.0, -30.9, 'A市B町三丁目5番地2', ha='left', va='center', fontsize=3.4 * PT, color=INK)
    for i, s in enumerate(['黒：答案用紙に印刷済み　青：記入するもの。（イ）部分の1階を実線、（ロ）部分の1階を点線。敷地の辺長は書かない',
                           'A4で印刷すると、縮尺1/500の大きさになる（1m＝2mm）']):
        ax.text(316, -(281.5 + 4.2 * i), s, ha='center', va='center', fontsize=3.3 * PT)
    save_sheet(fig, [z], 'R3_dai22mon_zu10_tatemono_zumen')


# ---- 図17：各階平面図（イ）の完成形（左半分・1/250。1m＝4mm） ----
def zu17():
    fig, ax = sheet_canvas(52, 240, 2, 292)
    z = Zu(ax, fontsize=8.5)
    ax.text(146, -7.0, '各階平面図（イ）の完成形（答案用紙の左半分・縮尺1/250の実際の大きさ）', ha='center', va='center',
            fontsize=5.2 * PT, weight='bold')
    k = 4.0

    def pl(e, s, ox, oy):
        return (ox + (e - 0.1) * k, oy + (s - 0.1) * k)

    def draw_floor(pts, ox, oy, ls_pts=None, labels=None):
        pp = [pl(e, s, ox, oy) for e, s in pts]
        for i in range(len(pp)):
            a, b = pp[i], pp[(i + 1) % len(pp)]
            ax.plot([a[0], b[0]], [-a[1], -b[1]], color=INK, lw=0.9, solid_capstyle='butt')
            z.segments.append((xy(S(*a)), xy(S(*b))))
        return pp

    def txt(x, y, s, mm=3.0, ha='center'):
        ax.text(x, -y, s, ha=ha, va='center', fontsize=mm * PT, color=INK, linespacing=1.35)

    def dims_floor(pp, labs):
        c = (sum(p[0] for p in pp) / len(pp), sum(p[1] for p in pp) / len(pp))
        for i, t in enumerate(labs):
            if not t:
                continue
            a, b = pp[i], pp[(i + 1) % len(pp)]
            m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
            dx, dy = b[0] - a[0], b[1] - a[1]
            n = (dy, -dx) if (dy * (m[0] - c[0]) - dx * (m[1] - c[1])) > 0 else (-dy, dx)
            L = (n[0] ** 2 + n[1] ** 2) ** 0.5
            off = 4.5
            txt(m[0] + n[0] / L * off, m[1] + n[1] / L * off, t, mm=2.9)

    # 1階
    ox, oy = 112.0, 55.0
    pp1 = draw_floor(I1, ox, oy)
    dims_floor(pp1, ['6.30', '', '', '9.80', '7.80', '10.80'])
    a, b = pp1[1], pp1[2]       # 北東の欠けの縦1.00（引き出して右に出す）と横1.50（上に出す）
    ax.plot([a[0] + 0.8, ox + 41.0], [-(a[1] + b[1]) / 2, -(a[1] + b[1]) / 2 + 3.0], color=INK, lw=0.3)
    txt(ox + 45.0, (a[1] + b[1]) / 2 - 3.0, '1.00', mm=2.9)
    c, d = pp1[2], pp1[3]
    txt((c[0] + d[0]) / 2, c[1] - 4.3, '1.50', mm=2.9)
    txt(ox + 15.6, oy + 24, '（イ）', mm=3.6)
    ax.plot([ox], [-oy], '^', ms=2.8 * PT * 1.0, mfc='white', mec=INK, mew=0.6)
    txt(ox - 22, oy + 20, '1階', mm=4.0)
    txt(ox + 55, oy + 22, '求　積　表\n6.30 × 1.00 ＝ 6.3000\n7.80 × 9.80 ＝ 76.4400\n　計　82.7400\n　床面積　82.74㎡', mm=3.1, ha='left')
    # 2階（1階の北東の欠けの位置を点線）
    ox2, oy2 = 112.0, 150.0
    pp2 = draw_floor(I2, ox2, oy2)
    notch = [pl(6.4, 0.1, ox2, oy2), pl(6.4, 1.1, ox2, oy2), pl(7.9, 1.1, ox2, oy2)]
    ax.plot([p[0] for p in notch], [-p[1] for p in notch], color=INK, lw=0.5, ls=(0, (2.0 * PT / 0.5, 1.2 * PT / 0.5)))
    dims_floor(pp2, ['7.80', '10.80', '7.80', '10.80'])
    txt(ox2 + 15.6, oy2 + 24, '（イ）', mm=3.6)
    ax.plot([ox2], [-oy2], '^', ms=2.8 * PT, mfc='white', mec=INK, mew=0.6)
    txt(ox2 - 22, oy2 + 20, '2階', mm=4.0)
    txt(ox2 + 55, oy2 + 22, '求　積　表\n7.80 × 10.80 ＝ 84.2400\n　床面積　84.24㎡', mm=3.1, ha='left')
    for i, s in enumerate(['黒：答案用紙に印刷済み　青：記入するもの', '内法の寸法で1階・2階を書き分け、符号（イ）と求積表を書く。',
                           '2階の点線は1階の北東の欠けの位置、△印は各階の重なる柱', 'A4で印刷すると、縮尺1/250の大きさになる（1m＝4mm）']):
        ax.text(146, -(280.5 + 3.9 * i), s, ha='center', va='center', fontsize=3.2 * PT)
    save_sheet(fig, [z], 'R3_dai22mon_zu17_kakukai_heimenzu')


if __name__ == '__main__':
    for f in (zu01, zu02, zu03, zu04, zu05, zu06, zu07, zu08, zu09, zu10, zu11, zu12, zu13, zu14, zu15, zu16, zu17, zu18,
              zu19, zu20, zu21, zu22, zu23, zu24, zu25, zu26, zu27, zu28, zu29, zu30):
        f()
    print('重なり合計:', len(PROBLEMS))
