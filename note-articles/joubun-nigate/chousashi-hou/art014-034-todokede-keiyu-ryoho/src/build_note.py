# note_template.md の {{LAW..}} を note-articles/laws/chousashi-hou.md の原文に差し替えて、記事（note_art014-034.md）を作る
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "common" / "law_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
import law_parts as lp
ROOT = next(p for p in _here.parents if (p / "note-articles").is_dir())

def quote(n, paras=None):
    cap, items = lp.kubun_article(ROOT, n, paras, "chousashi-hou.md")
    lines = [f"> **{n}{cap}**", ">"]
    for i, it in enumerate(items):
        lines += ([">"] if i else []) + ["> " + it]
    return "\n".join(lines)

def fudo_all(head, title):
    b = lp.fudo_article(ROOT, head)
    paras = [x.strip() for x in b.split("\n\n")[1:] if x.strip()]
    out = [f"> **{title}**"]
    for x in paras:
        out += [">", "> " + x]
    return "\n".join(out)

t = (_here.parent / "note_template.md").read_text(encoding="utf8")
t = t.replace("{{LAW14}}", quote("第14条")).replace("{{LAW34_2}}", quote("第34条", ["２"]))\
     .replace("{{LAW6}}", fudo_all("##### 第6条（登記所）", "不動産登記法 第6条（登記所）"))\
     .replace("{{LAW124}}", fudo_all("##### 第124条（筆界特定の事務）", "不動産登記法 第124条（筆界特定の事務）"))
_here.parent.parent.joinpath("note_art014-034.md").write_text(t, encoding="utf8")
print(len(t))
