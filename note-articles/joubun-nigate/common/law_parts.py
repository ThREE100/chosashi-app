# 条文の原文を note-articles/laws/ から取り出す部品（記事の作成と、機械チェックの両方が使う）
import re, pathlib

def laws_dir(root):
    return pathlib.Path(root) / "note-articles" / "laws"

def kubun_article(root, n, paras=None):
    """区分所有法（kubunshoyuu-hou.md）の第n条（例 '第5条'）から、(見出し, [項の本文...]) を返す。
    paras に ['５', '６'] のように項の頭の数字を指定すると、その項だけ返す（第1項は '1'）。"""
    t = (laws_dir(root) / "kubunshoyuu-hou.md").read_text(encoding="utf8")
    m = re.search(r"^### " + re.escape(n) + r"\n", t, re.M)
    e = re.search(r"^### 第", t[m.end():], re.M)
    body = t[m.end():m.end() + e.start()]
    lines = [l.strip() for l in body.split("\n")]
    while lines and (not lines[-1] or re.match(r"^（.*）$", lines[-1]) or lines[-1].startswith("#")):
        lines.pop()
    items = [l for l in lines if l and not l.startswith("#")]
    prev = t[:m.start()].rstrip().split("\n")
    cap = next((l for l in reversed(prev) if re.match(r"^（.*）$", l.strip())), "")
    if paras:
        keep = []
        for p in items:
            head = p[0] if re.match(r"^[２-９]", p) else "1"
            if head in paras or (p[0] in paras): keep.append(p)
        items = keep
    return cap, items

def fudo_article(root, head):
    t = (laws_dir(root) / "fudousan-touki-hou.md").read_text(encoding="utf8")
    i = t.index(head)
    return t[i:t.index("\n##### ", i + 5)]
