"""固定配置の整理図（比較カード・表・時系列・棒グラフ）の共通部品。

座標を使わない図（誤答と正解の比較、書く・書かないの一覧、表、時系列など）を、0〜100 の作業座標で描く。
R7/Q22 の作図スクリプトで作った `fixed_figure`・`check_fixed`・`card_figure` を共通化したもの（2026-10-26、R3/Q22 の品質チェックで切り出し）。

使い方:
    from zu_cards import Cards
    C = Cards(OUT, PROBLEMS)          # OUT は出力フォルダ、PROBLEMS は重なり検査の結果を集めるリスト
    C.card_figure('R3_dai22mon_zu02_kubun_bunkatsu', 'タイトル', [(見出し, 色, [行...]), ...], ['図の下の文'])
    C.table_figure(name, title, header, rows, widths, bottom)   # 表。各セルは (文字, 色) か 文字
    fig, ax = C.fixed_figure(title)  → 自由に描いて C.save_fixed(fig, name)

check_fixed は、図の全部の文字について、文字どうしの重なりと図の外へのはみ出しを調べる（座標の図用の Zu は使わない）。
行の先頭が '*' なら太字・色つき。caption（図の下の文）は最大2行。
"""
import os

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.colors import to_rgba

from zu_helpers import setup_font, BLACK, GRAY, RED, BLUE, GREEN


class Cards:
    def __init__(self, out, problems):
        self.out = out
        self.problems = problems

    # ---------------------------------------------------------------- 基本
    def fixed_figure(self, title, w=16, h=10, rect=(0.02, 0.04, 0.96, 0.86)):
        """固定配置の図。横軸・縦軸とも 0〜100 の作業座標。"""
        setup_font()
        fig = plt.figure(figsize=(w, h), dpi=100)
        fig.patch.set_facecolor('white')
        fig.suptitle(title, fontsize=24, weight='bold', y=0.975)
        ax = fig.add_axes(list(rect))
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        return fig, ax

    def check_fixed(self, fig, name):
        """文字どうしの重なりと、図の外へのはみ出しを調べる。"""
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
            if t.get_bbox_patch() is not None:
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
        self.problems.extend(probs)

    def save_fixed(self, fig, name):
        self.check_fixed(fig, name)
        path = os.path.join(self.out, name + '.png')
        fig.savefig(path, facecolor='white')
        plt.close(fig)
        print('書き出し:', path)

    @staticmethod
    def rbox(ax, x, y, w, h, col, alpha=0.12, lw=1.8, ls='-'):
        """角の丸い枠（alpha は塗りの濃さ。0 なら塗らない）。"""
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.5',
                                    facecolor=to_rgba(col, alpha) if alpha else 'none', edgecolor=col, lw=lw, ls=ls))

    @staticmethod
    def vline(fig, x, y0=0.10, y1=0.86):
        fig.add_artist(plt.Line2D([x, x], [y0, y1], transform=fig.transFigure, color=GRAY, lw=1.2))

    @staticmethod
    def caption(fig, bottom, fs=15, y=0.065):
        for k, t in enumerate(bottom):
            fig.text(0.5, y - 0.04 * k, t, ha='center', va='center', fontsize=fs)

    # ---------------------------------------------------------------- 比較カード
    def card_figure(self, name, title, cols, bottom, w=17, h=9.5, top=84.0, line_step=9.0, fs=17):
        """左右（2〜3列）に並べる固定配置の比較カード。cols: [(見出し, 色, [行...])]。
        行の先頭が '*' なら太字・色つき。bottom: 図の下に書く文（最大2行）。"""
        fig, ax = self.fixed_figure(title, w=w, h=h, rect=(0.02, 0.11, 0.96, 0.77))
        n = len(cols)
        cw = (98.0 - 2.0 * (n - 1)) / n
        for i, (head, col, lines) in enumerate(cols):
            x0 = 1.0 + i * (cw + 2.0)
            self.rbox(ax, x0, 4, cw, 80, col, alpha=0.08)
            ax.text(x0 + cw / 2, 92, head, ha='center', va='center', fontsize=fs + 3, weight='bold', color=col,
                    linespacing=1.35)
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
            self.vline(fig, 0.5, 0.10, 0.90)
        self.caption(fig, bottom)
        self.save_fixed(fig, name)

    # ---------------------------------------------------------------- 表
    def table_figure(self, name, title, header, rows, widths, bottom, w=17, h=8.5, fs=15, row_h=None, top=86.0):
        """表の図。header: [見出し...]、rows: [[セル...]]。セルは 文字 か (文字, 色, 塗りの濃さ)。widths は列の幅（合計100）。
        行の高さは row_h（省略時は行数で割る）。セルの中の改行は \\n。"""
        fig, ax = self.fixed_figure(title, w=w, h=h, rect=(0.02, 0.11, 0.96, 0.77))
        n = len(rows)
        hh = 11.0
        rh = row_h or (top - hh - 4) / n
        xs = [1.0]
        scale = 98.0 / sum(widths)
        for wd in widths:
            xs.append(xs[-1] + wd * scale)
        y = top
        for j, hd in enumerate(header):
            ax.add_patch(Rectangle((xs[j], y - hh), xs[j + 1] - xs[j], hh, facecolor=to_rgba(BLACK, 0.10), edgecolor=BLACK, lw=1.4))
            ax.text((xs[j] + xs[j + 1]) / 2, y - hh / 2, hd, ha='center', va='center', fontsize=fs, weight='bold',
                    linespacing=1.3)
        y -= hh
        for r in rows:
            for j, cell in enumerate(r):
                txt, col, al = (cell, BLACK, 0.0) if isinstance(cell, str) else (cell + (BLACK, 0.0)[len(cell) - 1:])[:3]
                bold = txt.startswith('*')
                txt = txt[1:] if bold else txt
                ax.add_patch(Rectangle((xs[j], y - rh), xs[j + 1] - xs[j], rh,
                                       facecolor=to_rgba(col, al) if al else 'none', edgecolor=BLACK, lw=1.2))
                ax.text((xs[j] + xs[j + 1]) / 2, y - rh / 2, txt, ha='center', va='center', fontsize=fs,
                        color=col if bold else BLACK, weight='bold' if bold else 'normal', linespacing=1.4)
            y -= rh
        self.caption(fig, bottom)
        self.save_fixed(fig, name)
