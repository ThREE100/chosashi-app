"""令和6年度 第22問（建物）の解説図を、座標値・辺長・頂点座標から作図してPNGに書き出す。

`../prompt_R6_dai22mon_kaisetsuzu.md` の図の一覧どおり（番号は記事の挿入順。番号は管理用で、画像の中には書かない）。
作図の共通部品は `tools/zu_helpers.py`。固定配置の図（座標を使わない整理図）は `check_fixed` で文字の重なりと図の外へのはみ出しを調べ、目視でも確かめる。
2026-10-26：最新の基準（qa-checklist-kijutsu.md の6-2・6-3）で、わなの会話の直後に専用の図がなかった箇所に図を足し、記事の挿入順に振り直した
（旧図 zu01→zu05、zu02→zu07、zu05→zu14、zu06→zu16、zu08→zu24。作成済みの図は、環境が違うと再生成でバイトが変わるので、`git mv` でPNG名だけ付け替え、
このスクリプトで再生成した同じ図は使わない）。旧 zu03（建物図面）・zu04（車庫と出窓を1枚に詰めた誤り比較図）・zu07（各階平面図）は、
答案用紙の第3欄の実寸（1/500・1/250）の図と、車庫・出窓の2枚に分けた図に置き換えた。
建物の座標は (東, 南) で持ち（原点は1階のウォークインクローゼットの西の壁と和室の北の壁の延長線の交点）、
zu_helpers の (北, 東) には B() で変換する（北 ＝ −南）。敷地は〔座標値一覧表〕の (X, Y) をそのまま使う。
第3欄の図（zu11・zu19）は、試験の答案用紙（`../touan_youshi/R6_dai22mon_touan_youshi.pdf` の2ページ目）の罫線を `get_drawings()` で測ったpt座標で、
枠の左半分（各階平面図）・右半分（建物図面）を 1pt ＝ 2.4px で描く（縮尺1/250は1m＝11.339pt、1/500は1m＝5.669pt）。
実行: python3 note-articles-Kijyutsu/R6/Q22/zu/draw_R6_dai22mon_kaisetsuzu.py [出力フォルダ]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon as MPoly, Circle, Rectangle, FancyBboxPatch  # noqa: E402
from matplotlib.colors import to_rgba  # noqa: E402

from zu_helpers import (Zu, new_figure, fit, xy, centroid, setup_font, BLACK, GRAY, RED, BLUE, ORANGE,  # noqa: E402
                        GREEN, PURPLE)

OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
PROBLEMS = []
INK = '#1a3a8f'   # 答案用紙に書き込む線・文字（濃い青）


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
A_ROOM = rect(12.6, -0.9, 15.75, 3.6)          # （あ）部分の2階の洋室（1階は車庫） 3.15×4.50
OKUGAI = rect(10.8, 2.7, 12.6, 3.6)            # 屋外廊下
ROUKA2 = rect(4.5, 2.7, 10.8, 3.6)             # 母屋の2階の廊下
BALCONY = [B(0.9, 6.3), B(7.2, 6.3), B(7.2, 8.1), B(10.8, 8.1), B(10.8, 9), B(6.3, 9), B(6.3, 7.2), B(0.9, 7.2)]
DEMADO = rect(10.8, 5.4, 11.1, 7.2)            # 1階リビングダイニングの東の出窓（位置は模式）
ONLY1F = [rect(0, 3.6, 0.9, 6.3), rect(4.5, 6.3, 6.3, 6.75), rect(6.3, 6.3, 7.2, 8.1), rect(7.65, 0.9, 11.25, 2.7)]   # 1階にだけある部分
MARUS = [(0.9, 0), (4.5, 0), (0.9, 6.3), (10.8, 2.7), (10.8, 8.1)] + [(12.6, -0.9), (15.75, -0.9), (12.6, 3.6), (15.75, 3.6)]  # 〇印の位置

assert round(area(F1), 2) == 68.85 == round(sum(area(r) for r in F1_STRIPS), 2)
assert round(area(F2), 2) == 57.51 == round(sum(area(r) for r in F2_STRIPS), 2)
assert round(area(A_ROOM), 3) == 14.175 and round(area(F2) + area(A_ROOM), 3) == 71.685
assert round(sum(area(r) for r in ONLY1F), 2) == 11.34 == round(area(F1) - area(F2), 2)   # 2階の母屋は1階の中に収まる
assert round(0.45 * 1.80, 2) == 0.81

# ---- 敷地（〔座標値一覧表〕。X＝北、Y＝東） ----
PA, PB, PC, PD, PE = complex(50, 15), complex(50, 25), complex(50, 35), complex(37, 35), complex(37, 15)
SITE = [PA, PB, PC, PD, PE]
assert area(SITE) == 260.0


# ======================================================================
# 固定配置の図（座標を使わない整理図）。H20/Q22・R7/Q22の作図スクリプトと同じ部品
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
    """固定配置の図の重なり検査（文字どうしの重なりと、図の外へのはみ出し）。"""
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


def card_figure(name, title, cols, bottom, w=17, h=9.5, top=84.0, line_step=8.6, fs=15):
    """左右（2〜3列）に並べる固定配置の比較カード。cols: [(見出し, 色, [行...])]。行の先頭が '*' なら太字・色つき。
    bottom: 図の下に書く文（最大2行）。check_fixed で文字の重なり・はみ出しを調べる。"""
    fig, ax = fixed_figure(title, w=w, h=h, rect=(0.02, 0.11, 0.96, 0.77))
    n = len(cols)
    cw = (98.0 - 2.0 * (n - 1)) / n
    for i, (head, col, lines) in enumerate(cols):
        x0 = 1.0 + i * (cw + 2.0)
        rbox(ax, x0, 4, cw, 80, col, alpha=0.08)
        ax.text(x0 + cw / 2, 92, head, ha='center', va='center', fontsize=fs + 3, weight='bold', color=col, linespacing=1.35)
        y = top - 4
        for ln in lines:
            bold = ln.startswith('*')
            t = ln[1:] if bold else ln
            k = t.count('\n') + 1
            if not t:
                y -= 3.5
                continue
            ax.text(x0 + cw / 2, y, t, ha='center', va='top', fontsize=fs, weight='bold' if bold else 'normal',
                    color=col if bold else BLACK, linespacing=1.4)
            y -= line_step * k * 0.78 + 2.4
    if n == 2:
        vline(fig, 0.5, 0.10, 0.90)
    for k, t in enumerate(bottom):
        fig.text(0.5, 0.065 - 0.04 * k, t, ha='center', va='center', fontsize=15)
    save_fixed(fig, name)


def tbox(ax, x, y, w, h, text, col, fs=15, alpha=0.10, weight='normal', lw=1.8):
    rbox(ax, x - w / 2, y - h / 2, w, h, col, alpha=alpha, lw=lw)
    ax.text(x, y, text, ha='center', va='center', fontsize=fs, weight=weight, linespacing=1.4,
            color=col if weight == 'bold' else BLACK)


def arrow(ax, p, q, col=GRAY, lw=2.0):
    ax.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle='-|>', lw=lw, color=col, mutation_scale=20, shrinkA=0, shrinkB=0))


# ======================================================================
# 第1章
# ======================================================================

def zu01():
    """完成日・申請日・申請の期限（1月以内）の時系列。"""
    fig, ax = fixed_figure('完成日・申請日・申請の期限を、日付で並べる', w=17, h=7.6, rect=(0.02, 0.11, 0.96, 0.77))
    ax.plot([5, 95], [46, 46], color=GRAY, lw=3, solid_capstyle='round')
    pts = [(14, '令和6年9月30日', '建物が完成し、同じ日に引渡し\n（事実関係2）', '＝新築の日（所有権の取得の日）', BLUE),
           (52, '令和6年10月18日', '申請の日\n（答案用紙に印刷）', '申請は期限内', GREEN),
           (88, '令和6年10月31日', '申請の期限\n（1月以内の最後の日）', '', RED)]
    for x, d, l1, l2, col in pts:
        ax.plot([x], [46], 'o', ms=15, color=col, zorder=5)
        ax.text(x, 66, d, ha='center', va='center', fontsize=19, weight='bold', color=col)
        ax.text(x, 29, l1, ha='center', va='center', fontsize=15, linespacing=1.4)
        if l2:
            ax.text(x, 14, l2, ha='center', va='center', fontsize=14, color=col, weight='bold')
    ax.annotate('', xy=(88, 82), xytext=(14, 82), arrowprops=dict(arrowstyle='<->', lw=2.2, color=ORANGE, shrinkA=0, shrinkB=0))
    ax.text(51, 90, '所有権を取得した日から1月以内に申請（不動産登記法第47条第1項）', ha='center', va='center', fontsize=16,
            weight='bold', color=ORANGE)
    for k, t in enumerate(['期間は初日（9月30日）を数えず10月1日から数え、応当日の11月1日の前日（10月31日）で満了（民法第140条・第143条第2項）']):
        fig.text(0.5, 0.065, t, ha='center', va='center', fontsize=15)
    save_fixed(fig, 'R6_dai22mon_zu01_jikeiretsu')


def zu02():
    card_figure('R6_dai22mon_zu02_chuu_shiwake',
                '同じ「注2」でも別もの：問題文の注と、図面の注',
                [('問題文の注（問題文の末尾）', BLUE,
                  ['注1　行為・書類はすべて適法', '*注2　書面申請。申請人は甲野桜子', '注3　建物図面は1/500、各階平面図は1/250',
                   '*注4　距離は各階平面図が小数第2位、\n建物図面が小数第1位', '注5　文字は明瞭に。押印と字数は不要']),
                 ('図面の注（【登記記録】の下の（注））', ORANGE,
                  ['注1　距離の単位はメートル', '*注2　図1の数値は筆界から外壁まで、\n図2の数値は柱の中心間', '*注3　隅は直角。図2の〇印は各階の重なり部分',
                   '注4　図1の（　）内は地番', '注5　A〜Eは筆界点（座標は表のとおり）', '注6　北はX軸の正の方向'])],
                ['会話では「問題文の注2」「図面の注2」のように書き分ける。太字は、この記事で使う注'], w=17.5, h=8.4, line_step=8.2)


def zu03():
    fig, ax = fixed_figure('土地の持ち主と建物の持ち主は別', w=17, h=7.6, rect=(0.02, 0.11, 0.96, 0.77))
    rbox(ax, 4, 18, 38, 62, BLUE, alpha=0.08)
    ax.text(23, 72, '土地（A市B町三丁目16番13）', ha='center', va='center', fontsize=17, weight='bold', color=BLUE)
    ax.text(23, 55, '登記記録（甲区）の所有者', ha='center', va='center', fontsize=15)
    ax.text(23, 42, '甲野梅子', ha='center', va='center', fontsize=26, weight='bold', color=BLUE)
    ax.text(23, 27, '松雄さんの母（事実関係1）', ha='center', va='center', fontsize=15)
    rbox(ax, 58, 18, 38, 62, GREEN, alpha=0.08)
    ax.text(77, 72, '本件建物（これから表題登記）', ha='center', va='center', fontsize=17, weight='bold', color=GREEN)
    ax.text(77, 55, '共有者2人（費用を出した割合）', ha='center', va='center', fontsize=15)
    ax.text(77, 43, '甲野桜子　持分5分の2', ha='center', va='center', fontsize=19, weight='bold', color=GREEN)
    ax.text(77, 32, '甲野松雄　持分5分の3', ha='center', va='center', fontsize=19, weight='bold', color=GREEN)
    ax.text(77, 24, '（事実関係3）', ha='center', va='center', fontsize=14)
    arrow(ax, (58, 49), (43, 49), col=GRAY)
    ax.text(50.5, 56, '建物は\n土地の上に\n建っている', ha='center', va='center', fontsize=13, linespacing=1.4)
    fig.text(0.5, 0.065, '土地が梅子さんのものでも、建物の持ち主は費用を出して建てた2人。建物の登記では建物の持ち主だけを考える',
             ha='center', va='center', fontsize=15)
    save_fixed(fig, 'R6_dai22mon_zu03_mochinushi')


def zu04():
    card_figure('R6_dai22mon_zu04_shinseinin',
                '申請人は1人でも、登記記録に載る所有者は共有者全員',
                [('申請人＝申請の手続をする人', BLUE,
                  ['*甲野桜子さん　1人', '（問題文の注2）', '', '共有者の1人からでも申請できる', '共有物の保存行為にあたる',
                   '（民法第252条第5項）']),
                 ('登記記録に載る人（表題部所有者）', GREEN,
                  ['*共有者全員', '甲野松雄　持分5分の3', '甲野桜子　持分5分の2', '', '持分は事実関係3の', '費用を出した割合のとおり'])],
                ['答案用紙の最下段「共有者」の欄には、申請人ではなく、共有者全員と持分を書く'], h=7.4)


def zu06():
    """別の建物にできるか、1個の建物の一部か：判定の流れ。"""
    fig, ax = fixed_figure('（あ）部分は、別の建物か、1個の建物の一部か：判定の流れ', w=17, h=9.6, rect=(0.02, 0.11, 0.96, 0.77))
    tbox(ax, 36, 85, 56, 14, 'Q1  （あ）部分の2階は、壁・屋根・床で\n外気と分断されている？（構造上の独立性）', BLUE, fs=15)
    tbox(ax, 36, 53, 56, 14, 'Q2  （あ）部分だけで、母屋を通らずに\n出入りして使える？（利用上の独立性）', BLUE, fs=15)
    tbox(ax, 36, 17, 56, 14, '別の建物（区分建物など）として\n登記できる', GRAY, fs=15)
    arrow(ax, (36, 78), (36, 60), col=BLUE)
    ax.text(38, 69, 'はい', color=BLUE, fontsize=17, weight='bold', va='center')
    arrow(ax, (36, 46), (36, 24), col=BLUE)
    ax.text(38, 35, 'はい', color=BLUE, fontsize=17, weight='bold', va='center')
    tbox(ax, 86, 69, 24, 18, '1個の建物の\n一部\n（附属建物にも\nならない）', ORANGE, fs=15, weight='bold', alpha=0.15)
    ax.plot([64, 86], [85, 85], color=RED, lw=2.4)
    arrow(ax, (86, 85), (86, 78.3), col=RED)
    ax.text(70, 88.5, 'いいえ', color=RED, fontsize=17, weight='bold', va='center')
    ax.plot([64, 86], [53, 53], color=RED, lw=2.4)
    arrow(ax, (86, 53), (86, 59.7), col=RED)
    ax.text(70, 56.5, 'いいえ', color=RED, fontsize=17, weight='bold', va='center')
    ax.text(46, 69, '本問：はい（壁・屋根・床がある）', color=BLUE, fontsize=14, ha='left', va='center', weight='bold')
    ax.text(66, 46, '本問：いいえ（屋外廊下を通るしかない）', color=RED, fontsize=14, ha='left', va='center', weight='bold')
    fig.text(0.5, 0.065, '全体を1個の建物として、松雄さんと桜子さんの共有で登記する（準則第78条第2項。構造上区分され、独立して用途に供せるものだけが各別の建物）',
             ha='center', va='center', fontsize=14)
    save_fixed(fig, 'R6_dai22mon_zu06_kubun_hantei')


# ======================================================================
# 第2章
# ======================================================================

def zu08():
    fig, ax = fixed_figure('北側の辺は、B点で相手方が切り替わる', w=17, h=7.0, rect=(0.02, 0.11, 0.96, 0.77))
    ax.plot([8, 92], [40, 40], color=BLACK, lw=3)
    ax.plot([50, 50], [40, 70], color=BLACK, lw=3)
    for x, n in [(8, 'A'), (50, 'B'), (92, 'C')]:
        ax.plot([x], [40], 'o', ms=14, color=BLACK, zorder=5)
        ax.text(x, 30, n, ha='center', va='center', fontsize=22, weight='bold')
    ax.text(29, 55, '16番11（隣地）', ha='center', va='center', fontsize=20, weight='bold', color=BLUE)
    ax.text(71, 55, '道（100番9）', ha='center', va='center', fontsize=20, weight='bold', color=ORANGE)
    ax.text(29, 46, 'A〜B　10.0m', ha='center', va='center', fontsize=15)
    ax.text(71, 46, 'B〜C　10.0m', ha='center', va='center', fontsize=15)
    ax.text(50, 76, 'B点から北へ短い線を引いて、境目を示す', ha='center', va='center', fontsize=16, weight='bold', color=RED)
    ax.text(50, 14, 'B点は、北側の相手方（16番11と道100番9）が切り替わる筆界点。一直線上にあるが、飾りではない', ha='center', va='center', fontsize=15)
    save_fixed(fig, 'R6_dai22mon_zu08_b_ten')


def zu09():
    card_figure('R6_dai22mon_zu09_kakikata',
                '建物図面に「書くもの」と「書かないもの」',
                [('書くもの', GREEN,
                  ['方位（北向きの矢印）', '敷地の地番と形状\n（16番13、座標どおりの長方形）', '隣接地の地番と道路\n（16番11・16番12・16番14、道100番9・道100番3）',
                   '1階の位置と形状（周壁のある母屋）', '筆界から外壁までの距離\n（1.5・1.5・1.0）', '縮尺1/500・B点の境目の線']),
                 ('書かないもの', RED,
                  ['敷地の辺長（10.0・13.0・20.0）\n＝作図が合っているかのチェック用', '車庫\n（周壁がなく、1階の外形に入らない）', '2階にだけある部分\n（建物図面は1階を描く）',
                   '床面積・求積表\n＝各階平面図に書く'])],
                ['不動産登記規則第82条：建物図面は、建物の敷地とその一階の位置・形状を明確にし、方位・縮尺・敷地の地番と形状・隣接地の地番を記録する'],
                w=17.5, h=9.6, line_step=8.6)


def zu10():
    card_figure('R6_dai22mon_zu10_keta_shukushaku',
                '距離の桁数と縮尺は、図面によって変わる',
                [('建物図面', BLUE,
                  ['縮尺 1/500（問題文の注3）', '距離は小数第1位まで（問題文の注4）', '', '*1.5　　1.5　　1.0', '', '「1.50」と書くと誤り']),
                 ('各階平面図', ORANGE,
                  ['縮尺 1/250（問題文の注3）', '距離は小数第2位まで（問題文の注4）', '', '*3.60　　0.90　　6.75', '', '「3.6」と書くと誤り'])],
                ['同じ長さでも、建物図面は小数第1位、各階平面図は小数第2位。縮尺も違うので、取り違えない'], h=7.4)


# ======================================================================
# 第3章
# ======================================================================

def pillars(z, pts, color):
    """車庫の柱（丸印）。重なり検査の対象の点として登録する。"""
    for p in pts:
        z.ax.add_patch(Circle(xy(p), 0.22, fc='white', ec=color, lw=1.6, zorder=4))
        z.markers.append(xy(p))


def zu12():
    fig, axes = new_figure('車庫は周壁がなく外気と分断されていないので、1階の床面積に入らない',
                           '車庫の柱（丸印）の間に壁がない。屋根があっても、壁で囲まれていなければ床面積にならない。68.85＋3.15×4.50＝68.85＋14.175＝83.025は誤り',
                           w=18, h=8.5, ncols=2)
    fig.subplots_adjust(top=0.84)
    z = Zu(axes[0], fontsize=13)
    z.poly(F1, color=BLACK, lw=2.2, fill=BLUE)
    z.poly(A_ROOM, color=RED, lw=0, fill=RED, alpha=0.30, check=False)
    pillars(z, A_ROOM, RED)
    axes[0].set_title('誤り：車庫まで入れる（藍子）', fontsize=17, weight='bold', color=RED)
    fit(axes[0], F1 + A_ROOM, margin=0.14, extra=[xy(B(8, 12))], pad_aspect=True)
    z.free_text(centroid(F1), '母屋', fs=14)
    z.callout(B(14.2, 1.35), '車庫（周壁なし）\n3.15×4.50＝14.175', dirs=(-70, -90, -50), fs=13, color=RED)
    z2 = Zu(axes[1], fontsize=13)
    z2.poly(F1, color=BLACK, lw=2.2, fill=BLUE)
    pillars(z2, A_ROOM, GRAY)
    axes[1].set_title('正解：壁の中心線で囲まれた母屋だけ 68.85㎡', fontsize=17, weight='bold', color=GREEN)
    fit(axes[1], F1 + A_ROOM, margin=0.14, extra=[xy(B(8, 12))], pad_aspect=True)
    z2.free_text(centroid(F1), '母屋 68.85㎡', fs=14)
    z2.callout(B(14.2, 1.35), '車庫は床面積に入らない\n（外気と分断されていない）', dirs=(-70, -90, -50), fs=13, color=GRAY)
    save(fig, [z, z2], 'R6_dai22mon_zu12_shako')


def zu13():
    """出窓は、高さ1.5メートル以上で下部が床面と同じ高さにあるものだけ算入（準則第82条第11号）。"""
    fig, ax = fixed_figure('出窓は「高さ1.5m以上」かつ「下部が床面と同じ高さ」のときだけ算入', w=17, h=8.4, rect=(0.02, 0.11, 0.96, 0.77))
    # 左：出窓の断面（縮尺は模式だが、0.90と1.10の比は合わせる）
    u = 22.0        # 1mあたりの作業座標
    x0, y0 = 3, 10  # 床面の位置
    ax.add_patch(Rectangle((x0, y0 - 2), 34, 2, fc=to_rgba(GRAY, 0.25), ec=GRAY))
    ax.text(x0 + 17, y0 - 5.2, '床面', ha='center', va='center', fontsize=14)
    ax.add_patch(Rectangle((x0 + 20, y0), 4, 3.0 * u, fc=to_rgba(GRAY, 0.18), ec=BLACK, lw=1.6))
    ax.add_patch(Rectangle((x0 + 24, y0 + 0.90 * u), 8, 1.10 * u, fc=to_rgba(BLUE, 0.20), ec=BLUE, lw=2.0))
    ax.text(x0 + 28, y0 + 0.90 * u + 0.55 * u, '出窓', ha='center', va='center', fontsize=15, weight='bold', color=BLUE)
    ax.add_patch(Rectangle((x0 + 24, y0), 8, 0.90 * u, fc='none', ec=GRAY, ls='--'))
    ax.text(x0 + 4, y0 + 3.0 * u - 3, '室内', ha='center', va='center', fontsize=14, color=GRAY)
    ax.annotate('', xy=(x0 + 34, y0), xytext=(x0 + 34, y0 + 0.90 * u), arrowprops=dict(arrowstyle='<->', lw=1.8, color=RED))
    ax.text(x0 + 35.5, y0 + 0.45 * u, '0.90m', ha='left', va='center', fontsize=16, weight='bold', color=RED)
    ax.annotate('', xy=(x0 + 34, y0 + 0.90 * u), xytext=(x0 + 34, y0 + 2.0 * u), arrowprops=dict(arrowstyle='<->', lw=1.8, color=RED))
    ax.text(x0 + 35.5, y0 + 1.45 * u, '1.10m', ha='left', va='center', fontsize=16, weight='bold', color=RED)
    # 右：2つの条件
    ax.text(72, 91, '算入する出窓は、次の2つをどちらも満たすものだけ', ha='center', va='center', fontsize=17, weight='bold')
    tbox(ax, 72, 72, 48, 14, '条件1　出窓の高さが1.5メートル以上\n本問の窓の高さ 1.10m → 満たさない', RED, fs=15, alpha=0.10)
    tbox(ax, 72, 50, 48, 14, '条件2　下部が床面と同じ高さにある\n本問は床面から0.90m上 → 満たさない', RED, fs=15, alpha=0.10)
    tbox(ax, 72, 26, 48, 12, '2つとも満たさない → 1階・2階とも\n出窓は床面積に算入しない', GREEN, fs=16, weight='bold', alpha=0.12)
    fig.text(0.5, 0.065, '不動産登記事務取扱手続準則第82条第11号。出窓は図の位置が模式（1階のリビングダイニングの東側と、2階の洋室）', ha='center', va='center', fontsize=15)
    save_fixed(fig, 'R6_dai22mon_zu13_demado')


def zu15():
    """上の寸法線と下の寸法線を、西の洋室の西の壁から足していく。"""
    fig, ax = fixed_figure('上の寸法線と下の寸法線を、同じ原点から足して突き合わせる', w=17, h=8.0, rect=(0.02, 0.11, 0.96, 0.77))
    k = 5.8          # 1mあたりの作業座標
    x0 = 6.0
    top = [3.60, 1.80, 1.35, 3.15, 1.80, 3.15]
    bot = [2.70, 1.80, 0.90, 0.90, 2.25, 1.35]

    def scale(y, vals, col, label, hl=None):
        ax.plot([x0, x0 + sum(vals) * k], [y, y], color=BLACK, lw=2.4)
        c = 0.0
        ax.plot([x0 + c * k] * 2, [y - 2, y + 2], color=BLACK, lw=2)
        for v in vals:
            ax.text(x0 + (c + v / 2) * k, y + 4.5, f'{v:.2f}', ha='center', va='center', fontsize=13)
            c += v
            ax.plot([x0 + c * k] * 2, [y - 2, y + 2], color=BLACK, lw=2)
        ax.text(x0 - 1, y + 12, label, ha='left', va='center', fontsize=16, weight='bold', color=col)

    scale(78, top, BLUE, '2階の上の寸法線（西の洋室の西の壁から）')
    scale(40, bot, ORANGE, '2階の下の寸法線（同じ壁から）')
    for c, col in [(3.60, BLUE), (5.40, BLUE), (6.75, RED)]:
        ax.text(x0 + c * k, 67, f'{c:.2f}', ha='center', va='center', fontsize=14, weight='bold', color=col)
        ax.plot([x0 + c * k] * 2, [70, 76], color=col, lw=1.2, ls=':')
    ax.text(x0 + 3.5 * k, 62, '累計：3.60　5.40　6.75', ha='left', va='center', fontsize=14, color=BLUE)
    for c, col in [(2.70, ORANGE), (4.50, ORANGE), (5.40, ORANGE), (6.30, RED)]:
        ax.text(x0 + c * k, 29, f'{c:.2f}', ha='center', va='center', fontsize=14, weight='bold', color=col)
        ax.plot([x0 + c * k] * 2, [32, 38], color=col, lw=1.2, ls=':')
    ax.text(x0 + 6.4 * k, 22, '累計：2.70　4.50　5.40　6.30', ha='left', va='center', fontsize=14, color=ORANGE)
    # 0.45のずれ
    ax.add_patch(Rectangle((x0 + 6.30 * k, 40), 0.45 * k, 38, fc=to_rgba(RED, 0.25), ec=RED, lw=1.5))
    ax.annotate('トイレの東の壁＝6.75\n東の洋室の西の壁＝6.30\n差 0.45m', xy=(x0 + 6.5 * k, 58), xytext=(60, 56), fontsize=16,
                weight='bold', color=RED, va='center', arrowprops=dict(arrowstyle='-', color=RED, lw=1.4), linespacing=1.5)
    fig.text(0.5, 0.065, '0.45の幅は、どの寸法線にも直接は書かれていない。上と下の寸法線を引き算して初めて出てくる（藍子が落とした部分は、この幅×1.80m＝0.81㎡）',
             ha='center', va='center', fontsize=15)
    save_fixed(fig, 'R6_dai22mon_zu15_sunpousen')


def zu17():
    card_figure('R6_dai22mon_zu17_hasuu',
                '71.6850は、四捨五入せず切り捨てる',
                [('誤り：四捨五入する', RED,
                  ['合計　71.6850', '↓', '小数第3位の5を切り上げ', '*71.69', '', '2階の床面積としては誤り']),
                 ('正解：100分の1未満を切り捨てる', GREEN,
                  ['合計　71.6850', '↓', '小数第3位以下を切り捨て', '*71.68', '', '（1階の68.8500は端数がなく 68.85）'])],
                ['不動産登記規則第115条：床面積は、1平方メートルの100分の1未満の端数を切り捨てる'], h=7.4)


def zu18():
    fig, axes = new_figure('〇印をそろえて、2階の図に1階の位置を重ねる',
                           '図面の注3：図2の〇印は各階の重なり部分。不動産登記規則第83条第1項：各階平面図には「一階の位置」を記録する',
                           w=16, h=8.8)
    ax = axes[0]
    z = Zu(ax, fontsize=14)
    for r in ONLY1F:
        z.poly(r, color=GRAY, lw=1.6, ls='--', fill=GRAY, alpha=0.12, check=False)
    z.poly(F2, color=BLACK, lw=2.4, fill=BLUE)
    z.poly(A_ROOM, color=BLACK, lw=2.4, fill=BLUE)
    for m in MARUS:
        ax.add_patch(Circle(xy(B(*m)), 0.30, fc='white', ec=RED, lw=2.4, zorder=6))
        z.markers.append(xy(B(*m)))
    fit(ax, F1 + A_ROOM, margin=0.10, extra=[xy(B(-1.5, 11.5)), xy(B(19, -2.5))], pad_aspect=True)
    z.north_arrow()
    z.callout(B(0.45, 4.95), '1階にだけある部分（点線）\n（ウォークインクローゼット）', dirs=(-120, -100, -140), fs=13, color=GRAY)
    z.callout(B(9.4, 1.8), '1階にだけある部分（点線）\n（浴室の東寄り）', dirs=(80, 60, 100), fs=13, color=GRAY)
    z.callout(B(6.75, 7.2), '1階にだけある部分（点線）', dirs=(-80, -100, -60), fs=13, color=GRAY)
    z.callout(B(3.0, 3.2), '2階（実線）', dirs=(120, 100), fs=14, color=BLACK)
    z.callout(B(14.2, 1.35), '（あ）部分：1階の車庫の\n4本の柱の真上に2階の洋室', dirs=(0, 20, -20), fs=13, color=BLUE)
    z.free_text(B(8.0, 10.2), '赤い丸＝〇印（各階の重なり部分）', fs=14, color=RED, weight='bold')
    save(fig, [z], 'R6_dai22mon_zu18_marujirushi')


# ======================================================================
# 第3欄（答案用紙の実寸）：枠の左半分＝各階平面図（1/250）、右半分＝建物図面（1/500）。1pt＝S px
# ======================================================================
S = 2.4
K250 = 1000 / 250 * 72 / 25.4        # 1m ＝ 4mm ＝ 11.339pt
K500 = 1000 / 500 * 72 / 25.4        # 1m ＝ 2mm ＝ 5.669pt


def page_fig(x0, y0, x1, y1):
    setup_font()
    fig = plt.figure(figsize=((x1 - x0) * S / 100, (y1 - y0) * S / 100), dpi=100)
    fig.patch.set_facecolor('white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(x0, x1)
    ax.set_ylim(-y1, -y0)
    ax.axis('off')
    return fig, ax


def fsz(pt):
    """答案用紙の上のpt表記の文字の大きさ → matplotlibのfontsize"""
    return pt * S * 0.72


def PT(ax, x, y, s, size=8.0, ha='center', va='center', color=BLACK, weight='normal', rot=0, **kw):
    return ax.text(x, -y, s, fontsize=fsz(size), ha=ha, va=va, color=color, weight=weight, rotation=rot, **kw)


def PL(ax, pts, lw=0.5, color=BLACK, ls='-'):
    ax.plot([p[0] for p in pts], [-p[1] for p in pts], color=color, lw=lw * S * 0.72, ls=ls, solid_capstyle='butt')


def PR(ax, x0, y0, x1, y1, lw=0.5, color=BLACK):
    PL(ax, [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], lw=lw, color=color)


def PG(px, py):
    """答案用紙のpt座標（右が+、下が+）を zu_helpers の複素数 (北 + 東i) にする。"""
    return complex(-py, px)


def scale_box(ax, x0, y0, x1, y1, denom):
    PR(ax, x0, y0, x1, y1, lw=0.34)
    PL(ax, [(x0, y1), (x1, y0)], lw=0.34)
    PT(ax, x0 + 10, y0 + 8, '1', 10)
    PT(ax, x1 - 12, y1 - 8, str(denom), 10)


def frame_right(ax):
    """第3欄の枠の右半分（建物図面）の印刷"""
    PL(ax, [(655.9, 73.0), (1083.9, 73.0), (1083.9, 727.8), (655.9, 727.8)], lw=1.134)
    PL(ax, [(655.9, 73.0), (655.9, 101.4)], lw=1.134)
    PL(ax, [(655.9, 699.5), (655.9, 727.8)], lw=1.134)
    PR(ax, 682.8, 44.7, 860.0, 73.0, lw=1.134)
    PL(ax, [(749.4, 44.7), (749.4, 73.0)], lw=0.34)
    PR(ax, 682.8, 73.0, 1083.9, 101.4, lw=1.134)
    PL(ax, [(749.4, 73.0), (749.4, 101.4)], lw=0.34)
    PT(ax, 716.1, 58.9, '家屋番号', 9)
    PT(ax, 804.7, 58.9, '（略）', 9)
    PT(ax, 716.1, 87.2, '建物の所在', 9)
    PT(ax, 757, 87.2, 'Ａ市Ｂ町三丁目16番地13', 9, ha='left', color=INK)
    PT(ax, 948, 60.0, '建　物　図　面', 12, )
    PR(ax, 677.1, 727.8, 1083.9, 768.9, lw=1.134)
    for x_ in (733.8, 988.9, 990.4, 1018.7):
        PL(ax, [(x_, 727.8), (x_, 768.9)], lw=0.34)
    PT(ax, 705.4, 748.3, '申　請　人', 9)
    PT(ax, 861.0, 748.3, '（略）', 9)
    PT(ax, 1004.6, 748.3, '縮尺', 9)
    scale_box(ax, 1024.6, 733.6, 1073.1, 763.2, 500)
    PT(ax, 660, 36.5, '第3欄', 7, ha='left', weight='bold')


def frame_left(ax):
    """第3欄の枠の左半分（各階平面図）の印刷"""
    PL(ax, [(655.9, 73.0), (227.8, 73.0), (227.8, 727.8), (655.9, 727.8)], lw=1.134)
    PL(ax, [(655.9, 73.0), (655.9, 101.4)], lw=1.134)
    PL(ax, [(655.9, 699.5), (655.9, 727.8)], lw=1.134)
    PR(ax, 227.8, 727.8, 634.6, 768.9, lw=1.134)
    for x_ in (284.5, 539.7, 541.1, 569.4):
        PL(ax, [(x_, 727.8), (x_, 768.9)], lw=0.34)
    PT(ax, 256.1, 748.3, '作　成　者', 9)
    PT(ax, 327, 745.0, '（略）', 9)
    PT(ax, 473, 759.0, '（令和6年○月○日作成）', 8)
    PT(ax, 555.3, 748.3, '縮尺', 9)
    scale_box(ax, 575.3, 733.6, 623.8, 763.2, 250)
    PT(ax, 433, 60.0, '各　階　平　面　図', 12)
    PT(ax, 232, 36.5, '第3欄', 7, ha='left', weight='bold')


def edge_labels(z, ax, P_, labels, spec, name):
    """辺の中点から (dx, dy) ずらして辺長を書く（P_ は page座標の複素数 (−y, x)）。spec の各要素は (dx, dy, 回転角, 水平方向の寄せ)。
    縦の辺は90度回して書く。短い辺（0.45・0.90）は自動配置では線や隣の文字に重なるので、1つずつ手で決める。"""
    n = len(P_)
    for i, (txt, sp) in enumerate(zip(labels, spec)):
        dx, dy, rot = sp[:3]
        ha = sp[3] if len(sp) > 3 else 'center'
        a, b = P_[i], P_[(i + 1) % n]
        mx, my = (a.imag + b.imag) / 2, -(a.real + b.real) / 2
        z.labels.append(PT(ax, mx + dx, my + dy, txt, 7, color=INK, rot=rot, ha=ha))


def zu11():
    """建物図面の完成形（答案用紙の第3欄の右半分。縮尺1/500の実寸）"""
    fig, ax = page_fig(645.9, 30.0, 1093.9, 779.0)
    frame_right(ax)
    z = Zu(ax, fontsize=fsz(7))
    ox, oy = 826.0, 365.0            # 敷地のA点（北西の角）のpt座標

    def site_pt(Y, X):
        return PG(ox + (Y - 15.0) * K500, oy + (50.0 - X) * K500)

    site = [site_pt(p.imag, p.real) for p in SITE]
    z.poly(site, color=INK, lw=fsz(0.9))
    bldg = [site_pt(16.0 + p.imag, 48.5 + p.real) for p in F1]      # 建物の(北=-南, 東) → 敷地の(Y, X)
    assert round(area(bldg) / K500 ** 2, 2) == 68.85
    z.poly(bldg, color=INK, lw=fsz(0.9))
    z.line(site_pt(25, 50), site_pt(25, 56), color=INK, lw=fsz(0.9))      # B点から北へ：16-11と道100-9の境目

    def dim(p, q, text, dirs):
        ax.annotate('', xy=xy(q), xytext=xy(p), arrowprops=dict(arrowstyle='<->', lw=fsz(0.5), color=INK, shrinkA=0, shrinkB=0), zorder=4)
        z.segments.append((xy(p), xy(q)))
        z.callout((p + q) / 2, text, dirs=dirs, fs=fsz(7), dists=(14, 20, 28, 36), color=INK)

    dim(site_pt(16.9, 50), site_pt(16.9, 48.5), '1.5', (150, 120, 180))
    dim(site_pt(20.5, 50), site_pt(20.5, 48.5), '1.5', (30, 60, 0))
    dim(site_pt(15.0, 44.9), site_pt(16.0, 44.9), '1.0', (180, 200, 160))
    for (Y, X, t, rot) in [(20, 50 + 3.0, '16－11', 0), (31, 50 + 3.0, '道（100－9）', 0), (25, 37 - 3.0, '道（100－3）', 0)]:
        c = site_pt(Y, X)
        ax.text(xy(c)[0], xy(c)[1], t, fontsize=fsz(7), ha='center', va='center', color=INK)
    for (Y, X, t, ha) in [(12.4, 40.5, '16－12', 'right'), (37.2, 43.5, '16－14', 'left'), (31.0, 43.5, '16－13', 'center')]:
        c = site_pt(Y, X)
        ax.text(xy(c)[0], xy(c)[1], t, fontsize=fsz(7), ha=ha, va='center', color=INK)
    # 方位（北向きの矢印）と単位
    nx, ny = 1030, 235
    ax.annotate('', xy=(nx, -(ny - 28)), xytext=(nx, -(ny + 12)), arrowprops=dict(arrowstyle='-|>', lw=fsz(0.8), color=INK, mutation_scale=18))
    PT(ax, nx, ny - 38, 'N', 8, color=INK, weight='bold')
    PT(ax, 1040, 704, '（単位：m）', 7, color=INK)
    PROBLEMS.extend(z.check_overlaps('zu11 建物図面'))
    path = os.path.join(OUT, 'R6_dai22mon_zu11_tatemono_zumen.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


def zu19():
    """各階平面図の完成形（答案用紙の第3欄の左半分。縮尺1/250の実寸）"""
    fig, ax = page_fig(217.8, 30.0, 665.9, 779.0)
    frame_left(ax)
    z = Zu(ax, fontsize=fsz(7))
    px0 = 300.0

    def pt1(p, py):                                    # 建物の点 → 答案用紙のpt（x＝px0＋東×K、y＝py＋南×K）
        return PG(px0 + p.imag * K250, py + (-p.real) * K250)

    def draw_floor(py, pts, solid=True, dashed=()):
        P_ = [pt1(p, py) for p in pts]
        z.poly(P_, color=INK, lw=fsz(0.9))
        for r in dashed:
            R_ = [pt1(p, py) for p in r]
            z.poly(R_, color=INK, lw=fsz(0.5), ls='--', check=False)
        return P_

    PT(ax, 240, 98, '1階', 9, ha='left', color=INK)
    P1 = draw_floor(125.0, F1)
    lab1 = ['3.60', '0.90', '6.75', '1.80', '0.45', '5.40', '4.50', '1.35', '1.80', '0.45', '4.50', '2.70', '0.90', '3.60']
    # 辺の並びは F1：(0.9,0)→(4.5,0)=3.60、→(4.5,0.9)=0.90、→(11.25,0.9)=6.75、→(11.25,2.7)=1.80、→(10.8,2.7)=0.45、→(10.8,8.1)=5.40、
    # →(6.3,8.1)=4.50、→(6.3,6.75)=1.35、→(4.5,6.75)=1.80、→(4.5,6.3)=0.45、→(0,6.3)=4.50、→(0,3.6)=2.70、→(0.9,3.6)=0.90、→(0.9,0)=3.60
    # 辺ごとの文字の位置（辺の中点からのずれ dx, dy〈pt〉、縦の辺は90度回す）。短い辺（0.45・0.90）が自動配置では線に重なるので手で決める
    spec1 = [(0, -6.5, 0), (-2.0, 2.5, 0, 'right'), (0, -6.5, 0), (7.5, 0, 90), (5.55, 5.0, 0, 'left'), (7.5, 0, 90), (0, 6.5, 0),
             (9.0, -4.5, 90), (0, 6.5, 0), (-3.0, 9.0, 0, 'right'), (-9.0, 6.5, 0), (-7.5, 0, 90), (1.5, -6.5, 0, 'right'), (-7.5, 0, 90)]
    edge_labels(z, ax, P1, lab1, spec1, 'zu19 1階')

    def kyuuseki(y0, rows, total, name):
        PT(ax, 363, y0, '求　積　表', 8, color=INK)
        yy = y0 + 14
        for a, b, c in rows:
            PT(ax, 330, yy, a, 8, ha='right', color=INK)
            PT(ax, 341, yy, '×', 8, color=INK)
            PT(ax, 372, yy, b, 8, ha='right', color=INK)
            PT(ax, 387, yy, '＝', 8, color=INK)
            PT(ax, 428, yy, c, 8, ha='right', color=INK)
            yy += 11.5
        PL(ax, [(318, yy - 5), (430, yy - 5)], lw=0.34, color=INK)
        PT(ax, 397, yy + 3, '合　計', 8, ha='right', color=INK)
        PT(ax, 428, yy + 3, total[0], 8, ha='right', color=INK)
        PT(ax, 397, yy + 14.5, '床面積', 8, ha='right', color=INK)
        PT(ax, 430, yy + 14.5, total[1], 8, ha='right', color=INK)
    kyuuseki(248, [('0.90', '2.70', '2.4300'), ('3.60', '6.30', '22.6800'), ('1.80', '5.85', '10.5300'), ('4.50', '7.20', '32.4000'),
                   ('0.45', '1.80', '0.8100')], ('68.8500', '68.85㎡'), '1階')
    PT(ax, 240, 392, '2階', 9, ha='left', color=INK)
    P2 = draw_floor(430.0, F2, dashed=ONLY1F)
    lab2 = ['3.60', '0.90', '3.15', '1.80', '3.15', '5.40', '3.60', '1.80', '6.30', '6.30']
    # F2：(0.9,0)→(4.5,0)=3.60、→(4.5,0.9)=0.90、→(7.65,0.9)=3.15、→(7.65,2.7)=1.80、→(10.8,2.7)=3.15、→(10.8,8.1)=5.40、
    # →(7.2,8.1)=3.60、→(7.2,6.3)=1.80、→(0.9,6.3)=6.30、→(0.9,0)=6.30
    spec2 = [(0, -6.5, 0), (-2.0, 2.5, 0, 'right'), (8.0, -6.5, 0), (-7.5, 0, 90), (0, 6.5, 0), (7.5, 0, 90), (0, 6.5, 0),
             (7.5, 0, 90), (0, -6.5, 0), (-17.0, 0, 90)]
    edge_labels(z, ax, P2, lab2, spec2, 'zu19 2階')
    PA_ = [pt1(p, 430.0) for p in A_ROOM]
    z.poly(PA_, color=INK, lw=fsz(0.9))
    edge_labels(z, ax, PA_, ['3.15', '4.50', '3.15', '4.50'], [(0, -6.5, 0), (7.5, 0, 90), (0, 6.5, 0), (-7.5, 0, 90)], 'zu19 あ')
    kyuuseki(560, [('3.15', '5.40', '17.0100'), ('0.45', '7.20', '3.2400'), ('2.70', '5.40', '14.5800'), ('3.60', '6.30', '22.6800'),
                   ('3.15', '4.50', '14.1750')], ('71.6850', '71.68㎡'), '2階')
    PT(ax, 500, 500, '点線＝1階の位置', 7, color=INK, ha='left')
    PROBLEMS.extend(z.check_overlaps('zu19 各階平面図'))
    path = os.path.join(OUT, 'R6_dai22mon_zu19_kakukai_heimenzu.png')
    fig.savefig(path, facecolor='white')
    plt.close(fig)
    print('書き出し:', path)


# ======================================================================
# 第4章
# ======================================================================

def zu20():
    card_figure('R6_dai22mon_zu20_tenpu_shorui',
                '表題登記の添付書類は5点。登記識別情報は付けない',
                [('付けるもの（5点）', GREEN,
                  ['建物図面・各階平面図\n＝位置・形状と、床面積の求め方', '所有権証明書\n＝建物の持ち主が誰かを示す', '住所証明書\n＝共有者2人とも分',
                   '代理権限証書\n＝調査士が代理で申請するため']),
                 ('付けないもの', RED,
                  ['*登記識別情報', '所有権の登記をして初めて\n登記名義人に通知される（法第21条）', '', 'この建物は、所有権の登記どころか\n表題登記もまだ',
                   '→ 持っていない（付けられない）'])],
                ['不動産登記令別表の十二の項：建物図面・各階平面図・所有権を証する情報・表題部所有者となる者の住所を証する情報（代理権限は令第7条第1項第2号）'],
                w=17.5, h=8.6)


def zu21():
    card_figure('R6_dai22mon_zu21_zeikin_chigai',
                '問1のエは「固定資産税」の納付証明。登録免許税ではない',
                [('正解：固定資産税', GREEN,
                  ['固定資産税＝建物の所有者として\n扱われる人に課される税金', '↓', '*納付証明を見れば、誰が持ち主として\n扱われているかがわかる', '', '→ 所有権を証する情報の例になる']),
                 ('誤り：登録免許税', RED,
                  ['登録免許税＝登記を受けるときに\n納める税金', '↓', '*表題登記では、そもそも\n課されない', '', '→ 所有者を示す資料にならない'])],
                ['準則第87条第1項：建築基準法の確認・検査のあったことを証する情報、建築請負人又は敷地所有者の証明情報、固定資産税の納付証明などがある'],
                w=17.5, h=7.8)


def zu22():
    card_figure('R6_dai22mon_zu22_inshi_ran',
                '答案用紙で、書く欄・印刷済みの欄・空けておく欄',
                [('書く欄', GREEN,
                  ['登記の目的', '添付書類', '所在', '種類・構造・床面積', '登記原因及びその日付', '共有者（全員と持分）']),
                 ('印刷済みで書かない欄', GRAY,
                  ['申請の日付・提出先\n（令和6年10月18日　A地方法務局）', '申請人（甲野桜子）', '代理人（略）', '家屋番号（略）', '※押印・字数は不要（問題文の注5）']),
                 ('空けておく欄', BLUE,
                  ['主である建物又は附属建物\n（附属建物がない）', '所在の2段目\n（変更がない）', '記入行の2行目・3行目'])],
                ['印刷済みの欄に書き足すと、かえって減点のもとになる。書く欄だけを手早く埋める'], w=18, h=8.4, fs=14)


def zu23():
    card_figure('R6_dai22mon_zu23_touroku_menkyozei',
                '表題登記は登録免許税がかからない（答案用紙にも欄がない）',
                [('課税される表示の登記（例）', ORANGE,
                  ['*登録免許税法第2条：別表第一に\n掲げる登記等に課税', '所有権の登記がある不動産の表示の変更で', '・土地の分筆　・建物の分割・区分', '・土地の合筆　・建物の合併',
                   '（別表第一の一（十三））']),
                 ('本問：建物の表題登記', GREEN,
                  ['*別表第一に項がない', '→ 課税されない', '', '答案用紙に登録免許税の欄はない', '→ 何も書かない'])],
                ['問1のエで、登録免許税の納付証明が所有権を示す資料にならないと考えたのと、同じ理由'], w=17.5, h=7.8)


if __name__ == '__main__':
    zu01()
    zu02()
    zu03()
    zu04()
    zu06()
    zu08()
    zu09()
    zu10()
    zu11()
    zu12()
    zu13()
    zu15()
    zu17()
    zu18()
    zu19()
    zu20()
    zu21()
    zu22()
    zu23()
    print('重なり合計:', len(PROBLEMS))
