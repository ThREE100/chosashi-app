# 直前復習カード：図解インフォグラフィックのプロンプトを組み立てる（pairs＝状態→正しい/誤ったイメージ、table＝比較表）
import sys, pathlib, re
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY
sys.path.insert(0, str(_here.parents[2] / "joubun-nigate" / "kubun-tatemono-hani" / "src"))
import scene_lib as sl

def pairs_prompt(c):
    return sl.scene_prompt(dict(t1=c["t1"], t2=c["t2"], sub=c["sub"], state=c["state"], pairs=c["pairs"]))

def table_prompt(c):
    cols, rows = c["cols"], c["rows"]
    size = f"1080x{700 + 190 * len(rows) + (150 if c.get('takeaway') else 0)}"
    body = [lead(size, "This is a comparison-table poster: a clean table that sorts the confusing points into rows so they can be reviewed at a glance. It is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Use only the short cell texts given below. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face.",
            TEXTREQ, BGREQ, COLOR,
            "--- HEADER ---", "Title (large, bold, 2 lines):", q(c["t1"]), q(c["t2"]), "Subtitle (smaller, centered, 1 line):", q(c["sub"]),
            "--- TABLE ---",
            "Render as a clean flat-design table with rounded corners, alternating row background colors (cream and pale blue), Japanese sans-serif font, no monospace font. "
            f"The table has exactly {len(cols)} columns and exactly {len(rows)} data rows, plus one header row. Do not add, drop, merge, or reorder any rows or columns.",
            "Header row (dark navy bar, white text), columns from left to right, each text exactly once: " + ", ".join(f"{k}. {q(h)}" for k, h in enumerate(cols, 1)) + "."]
    for r, row in enumerate(rows, 1):
        cells = []
        for k, cell in enumerate(row, 1):
            if cell == "@yes": cells.append(f"column {k}: a BLUE filled circle mark with no text")
            elif cell == "@no": cells.append(f"column {k}: a RED cross mark with no text")
            else: cells.append(f"column {k}: {q(cell)}")
        body.append(f"Data row {r}: " + "; ".join(cells) + ".")
    body.append("Make the first column slightly bolder than the others; every cell text appears exactly once, verbatim, in its own cell.")
    if c.get("takeaway"):
        body += ["Under the table inside the same section, one slim pale-yellow banner (the last element of the poster), keyword phrase, not a sentence:", q(c["takeaway"])]
    txt = "\n".join(body)
    extra = (f"Confirm the table has exactly {len(cols)} columns and exactly {len(rows)} data rows, every cell reads exactly as given, no cell text is duplicated into another cell, "
             "and that no sentence-long explanatory prose appears anywhere.")
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

def card_prompt(c):
    return pairs_prompt(c) if c["kind"] == "pairs" else table_prompt(c)
