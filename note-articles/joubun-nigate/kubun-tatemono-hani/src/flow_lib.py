# 判定の流れ図（縦の一本道＋右に「いいえ」の結果）のプロンプトを組み立て、構造を機械的に点検する
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def check_spine(start, diamonds, ok):
    """構造の点検：全ダイヤにはい／いいえの出口が1つずつ、全結果ノードに入口が1つ、結果ノードから矢印が出ない、経路数＝ダイヤ数＋1"""
    assert start and ok
    assert 2 <= len(diamonds) <= 6
    paths = 0
    for i, d in enumerate(diamonds, 1):
        assert set(d) >= {"text", "yes", "no", "no_result"}, f"ダイヤ{i}に出口が足りない"
        assert d["yes"] != d["no"], f"ダイヤ{i}のはい／いいえのラベルが同じ"
        paths += 1
    return paths + 1

def spine_flow(t1, t2, sub, start, diamonds, ok, ok_tag, footer_tag=None, size="1080x2400"):
    npaths = check_spine(start, diamonds, ok)
    n = len(diamonds)
    L = [lead(size, "This is a flowchart poster (判定の流れ図)."), TEXTREQ, BGREQ, COLOR,
         "--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub),
         "--- FLOWCHART ---",
         f"Layout: a single vertical main line down the center. START at the top, then DIAMOND 1 to DIAMOND {n} stacked from top to bottom with equal spacing, then the final RESULT box (the blue one) at the bottom. "
         "Every diamond has exactly two exits: the YES arrow goes straight down to the next element on the main line, and the NO arrow goes horizontally to the right to its own red result box placed to the right of that diamond. Keep all result boxes in one column on the right, aligned with their diamonds.",
         "Color: every YES arrow and its label " + q("はい") + " are BLUE; every NO arrow and its label " + q("いいえ") + " are RED; the main-line final result box is BLUE; every right-hand result box is RED; START and diamond outlines are dark navy. Every label is placed beside its arrow, never on top of a box.",
         "NODE START (rounded pill, dark navy): " + q(start)]
    for i, d in enumerate(diamonds, 1):
        L.append(f"NODE DIAMOND {i}: " + q(d["text"]) + " The text is placed inside the diamond on 3 or 4 lines; enlarge the diamond so that all text stays inside it.")
        L.append(f"  - Arrow down with the label " + q(d["yes"]) + (f" to DIAMOND {i + 1}." if i < n else " to the final RESULT box."))
        L.append(f"  - Arrow right with the label " + q(d["no"]) + f" to RESULT {i}.")
    for i, d in enumerate(diamonds, 1):
        L.append(f"NODE RESULT {i} (red box on the right): " + q(d["no_result"]))
    L.append("NODE FINAL RESULT (blue box at the bottom of the main line): " + q(ok))
    L.append(f"Counts: 1 start node, {n} diamonds, {n + 1} result boxes ({n} red and 1 blue), {npaths} distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box.")
    L.append("Under the final blue box, one small light-gray tag centered: " + q(ok_tag))
    if footer_tag:
        L.append("At the very bottom, one small light-gray tag centered: " + q(footer_tag))
    txt = "\n".join(L)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), f"Confirm there are exactly 1 start node, {n} diamonds and {n + 1} result boxes, that every YES arrow is blue and every NO arrow is red, that no arrow leaves a result box, and that no box contains a full sentence of prose.")
