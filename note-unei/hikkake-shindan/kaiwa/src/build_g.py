import glob, importlib, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import bank
from gakushu import build, instructions, OUT
B = bank()
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'g[0-9][0-9].py'))):
    it = importlib.import_module(os.path.basename(f)[:-3]).ITEM
    title, md, pr, stem, truth = build(it, B); no = f"{it['no']:02d}"
    open(os.path.join(OUT, f"{no}-{it['slug']}.md"), 'w', encoding='utf-8').write(md)
    open(os.path.join(OUT, f"{no}-{it['slug']}_prompts.md"), 'w', encoding='utf-8').write(pr)
    cx, gp = instructions(it)
    open(os.path.join(OUT, f"{no}-codex-instructions.md"), 'w', encoding='utf-8').write(cx)
    open(os.path.join(OUT, f"{no}-chatgpt-github-instructions.md"), 'w', encoding='utf-8').write(gp)
    print(no, it['id'], title, len(it['pages']), 'ページ')

# 順位リストの「記事」欄と README の進み具合を、できた回から作り直す
import re
done = {}
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'g[0-9][0-9].py'))):
    it = importlib.import_module(os.path.basename(f)[:-3]).ITEM
    done[it['id']] = it
jl = os.path.join(OUT, '00-junni-list.md'); L = open(jl, encoding='utf-8').read().split('\n'); rank = {}
for k, l in enumerate(L):
    m = re.match(r'\| (\d+) \| (D\d+) \|', l)
    if m:
        c = l.split('|'); rank[m.group(2)] = int(m.group(1))
        c[-2] = f" {done[m.group(2)]['no']:02d} " if m.group(2) in done else ' '
        L[k] = '|'.join(c)
open(jl, 'w', encoding='utf-8').write('\n'.join(L))
rp = os.path.join(OUT, 'README.md'); R = open(rp, encoding='utf-8').read()
head = '## 進み具合\n\n| 回 | 順位 | ID | 出典 | ページ | 状態 |\n|---|---|---|---|---|---|\n'
rows = ''.join(f"| {it['no']:02d} | {rank.get(i, '')} | {i} | {it['q']}{it['label']} | {len(it['pages'])} | {'画像はユーザーが生成済み・良好' if it['no'] == 1 else '画像は未生成'} |\n" for i, it in sorted(done.items(), key=lambda x: x[1]['no']))
R = re.sub(r'## 進み具合\n.*\Z', head + rows, R, flags=re.S)
open(rp, 'w', encoding='utf-8').write(R)
