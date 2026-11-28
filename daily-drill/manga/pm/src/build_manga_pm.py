"""毎日ドリル（夜）の学習まんが：台本（src/dayNNN.py）から、図（fig/）・note記事・画像プロンプト・Codex/ChatGPT用の貼り付け文を作る。
使い方：python3 daily-drill/manga/pm/src/build_manga_pm.py [日 ...]　（--nofig で図の書き出しを省く。生成物は手で直さない）"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import OUT, REL, problem, scripts, fig_rel, fig_url  # noqa: E402
from manga_core import prompts_md, figs_of  # noqa: E402
from manga_instr import instructions  # noqa: E402

KATA = 'daily-drill/manga/KATA.md'


def article(M, P):
    d = M['day']
    L = [f"## 【土地家屋調査士試験】Day{d:03d}-PM_漫画で解説～{M['catch']}～", '',
         f"**出題：毎日ドリル　第{d}日（夜）　記述式**", '', f"> {P['title']}", '', M['intro'], '',
         '問題（Day%03d-PM）を先に解いてから、漫画を読んでください。' % d, '', '---', '']
    for k, p in enumerate(M['pages'], 1):
        L += [f"> 【画像挿入】{k}ページ目：{p['caption']}", '']
    L += ['---', '', '### 答え（文字で確かめたい人へ）', '', '| 求めるもの | 答え |', '|---|---|']
    for a in P['answers']:
        v = f"X {a['value'][0]}　Y {a['value'][1]}" if a['kind'] == 'xy' else a['value']
        L.append(f"| {a['label']} | {v} |")
    L += ['', '### 解き方', ''] + [f"{i}. {s}" for i, s in enumerate(P['steps'], 1)] + ['']
    return '\n'.join(L)


def build(M, with_fig=True):
    P = problem(M['problem'])
    d = M['day']
    if with_fig:
        import figs
        figs.write_all({d})
    fp = f"毎晩ドリル漫画_Day{d:03d}"
    base = f"day{d:03d}-pm-manga"
    pr = prompts_md(f"毎日ドリル 第{d}日（夜）記述式 {M['problem']} 学習まんがの画像プロンプト",
                    [f"記事：`{base}.md`。問題：`daily-drill/evening/problems/{M['problem']}.json`（座標・答えはここから）。全{len(M['pages'])}ページ、1ページ＝1枚（1024×1536）。",
                     "図は Claude が問題データから作った正確な図（`fig/`）。漫画の中にそのまま置かせ、画像生成AIに描き直させない。"],
                    M['pages'], fp, M['header'], M['header_scene'], url_of=fig_url)
    figs_l = [(k, f['name'], fig_rel(f['name'])) for k, _, f in figs_of(M['pages'])]
    cx, gp = instructions(f"毎日ドリル 第{d}日（夜）", f"{REL}{base}_prompts.md", M['pages'], fp, KATA, figs=figs_l)
    out = {f"{base}.md": article(M, P), f"{base}_prompts.md": pr,
           f"{base}-codex-instructions.md": cx, f"{base}-chatgpt-github-instructions.md": gp}
    for k, v in out.items():
        open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
    return out


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if a != '--nofig']
    want = {int(x) for x in args}
    for M in scripts():
        if not want or M['day'] in want:
            build(M, with_fig='--nofig' not in sys.argv)
            print(f"Day{M['day']:03d}", M['problem'], len(M['pages']), 'ページ')
