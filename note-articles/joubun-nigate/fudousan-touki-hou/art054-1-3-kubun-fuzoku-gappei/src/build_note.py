# note_template.md の {{LAW..}} を note-articles/laws/ の原文に差し替えて、記事（note_art054-1-3.md）を作る
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "common" / "law_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
import law_parts as lp
ROOT = next(p for p in _here.parents if (p / "note-articles").is_dir())

def fudo(head, title, with_list=True):
    b = lp.fudo_article(ROOT, head)
    first = b.split("\n\n")[1].split("\n- ")[0].strip()
    items = [l for l in b.split("\n") if l.startswith("- ")] if with_list else []
    out = [f"> **{title}**", ">", "> " + first] + ["> " + l for l in items]
    return "\n".join(out)

def junsoku():
    src = (ROOT / "note-articles/laws/fudousan-touki-jimu-junsoku.md").read_text(encoding="utf8")
    i = src.index("### 第86条"); blk = src[i:i + 600]
    lines = [l.strip() for l in blk.split("\n") if l.strip()][1:4]
    assert lines[0].startswith("法第５４条") and lines[1].startswith("(1)") and lines[2].startswith("(2)"), lines
    return "\n".join(["> **不動産登記事務取扱手続準則 第86条（合併の禁止）**", ">", "> " + lines[0], ">", "> " + lines[1], ">", "> " + lines[2]]), lines

t = (_here.parent / "note_template.md").read_text(encoding="utf8")
j, jl = junsoku()
t = (t.replace("{{LAW54_P}}", fudo("##### 第54条（建物の分割、区分又は合併の登記）", "第54条（建物の分割、区分又は合併の登記）"))
      .replace("{{LAW56_P}}", fudo("##### 第56条（建物の合併の登記の制限）", "第56条（建物の合併の登記の制限）"))
      .replace("{{JUNSOKU86}}", j))
_here.parent.parent.joinpath("note_art054-1-3.md").write_text(t, encoding="utf8")
print(len(t)); print(jl)
