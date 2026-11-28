"""毎日ドリル（朝）の学習まんが：台本（src/dayNNN.py）から、note記事・画像プロンプト・Codex/ChatGPT用の貼り付け文を作る。
使い方：python3 daily-drill/manga/am/src/build_manga_am.py [日 ...]　（生成物は手で直さない）"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, REL, problem, scripts, answer  # noqa: E402
from manga_core import prompts_md  # noqa: E402
from manga_instr import instructions  # noqa: E402

KATA = 'daily-drill/manga/KATA.md'


def stem_md(P):
    L = [f"> {P['stem']}", '>　  ']
    L += [f"> {s['label']}　{s['text']}  " for s in P['statements']]
    L += ['>　  '] + [f"> {i}　{'・'.join(c)}  " for i, c in enumerate(P['choices'], 1)]
    return L


def article(M, P):
    d = M['day']
    n, pick = answer(P)
    L = [f"## 【土地家屋調査士試験】Day{d:03d}-AM_漫画で解説～{M['catch']}～", '',
         f"**出題：毎日ドリル　第{d}日（朝）　択一**", ''] + stem_md(P) + ['', '---', '', M['intro'], '',
         '答えの番号を紙に書いてから、漫画を読んでください。', '', '---', '']
    for k, p in enumerate(M['pages'], 1):
        L += [f"> 【画像挿入】{k}ページ目：{p['caption']}", '']
    L += ['---', '', '### 答え（文字で確かめたい人へ）', '', f"**正解：{'・'.join(pick)}の組合せ（選択肢{n}番）**", '']
    L += [f"- **{s['label']}（{'正' if s['truth'] else '誤'}）** {s['note']}" for s in P['statements']]
    L += ['', f"くわしい解説は、毎朝ドリル Day{d:03d} の択一解説の記事にあります。", '']
    return '\n'.join(L)


def with_nomark(pages):
    """最後のページ（答え）のほかは、正誤の印を描かせない（2026-11-28 ユーザー指示）。"""
    return [dict(p, nomark=True) if k < len(pages) - 1 else p for k, p in enumerate(pages)]


def build(M):
    P = problem(M['problem'])
    M = dict(M, pages=with_nomark(M['pages']))
    d = M['day']
    fp = f"毎朝ドリル漫画_Day{d:03d}"
    base = f"day{d:03d}-am-manga"
    pr = prompts_md(f"毎日ドリル 第{d}日（朝）択一 {M['problem']} 学習まんがの画像プロンプト",
                    [f"記事：`{base}.md`。問題：`daily-drill/morning/problems/{M['problem']}.json`（肢の文・正誤はここから）。全{len(M['pages'])}ページ、1ページ＝1枚（1024×1536）。"],
                    M['pages'], fp, M['header'], M['header_scene'])
    cx, gp = instructions(f"毎日ドリル 第{d}日（朝）", f"{REL}{base}_prompts.md", M['pages'], fp, KATA)
    out = {f"{base}.md": article(M, P), f"{base}_prompts.md": pr,
           f"{base}-codex-instructions.md": cx, f"{base}-chatgpt-github-instructions.md": gp}
    for k, v in out.items():
        open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
    return out


if __name__ == '__main__':
    want = {int(x) for x in sys.argv[1:]}
    for M in scripts():
        if not want or M['day'] in want:
            build(M)
            print(f"Day{M['day']:03d}", M['problem'], len(M['pages']), 'ページ')
