import glob, importlib, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import bank, build, OUT
B = bank(); rows = []
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'd[0-9][0-9].py'))):
    it = importlib.import_module(os.path.basename(f)[:-3]).ITEM
    title, md, pr, stem, truth = build(it, B)
    no = f"{it['no']:02d}"
    open(os.path.join(OUT, f"{no}-{it['slug']}.md"), 'w', encoding='utf-8').write(md)
    open(os.path.join(OUT, f"{no}-{it['slug']}_prompts.md"), 'w', encoding='utf-8').write(pr)
    rows.append((no, it['id'], title))
print("\n".join(" ".join(r) for r in rows))
