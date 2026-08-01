import re
import sys
from pathlib import Path

TABLE_RE = re.compile(r"^### まとめ表\s*\n\n((?:\|.*\|\n?)+)", re.M)


def convert_table(match):
    block = match.group(1)
    rows = [r for r in block.strip().split("\n") if r.strip()]
    # rows[0] = header, rows[1] = separator, rows[2:] = data
    data_rows = rows[2:]
    bullets = []
    for row in data_rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        shi, hantei, point = cells[0], cells[1], cells[2]
        bullets.append(f"- **{shi}（{hantei}）**　{point}")
    return "### まとめ\n\n" + "\n".join(bullets) + "\n"


def fix_blank_line(text):
    # ensure a blank line after the last bullet before the next paragraph
    return re.sub(r"(^- \*\*.+?\*\*.+$)\n(?!\n)(?!- \*\*)", r"\1\n\n", text, flags=re.M)


def convert_file(path):
    text = path.read_text(encoding="utf-8")
    if "### まとめ表" not in text:
        return False
    new_text = TABLE_RE.sub(convert_table, text)
    new_text = fix_blank_line(new_text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main():
    targets = sys.argv[1:]
    if not targets:
        print("usage: table_to_bullets.py <dir-or-file> [...]")
        sys.exit(1)
    changed = []
    for t in targets:
        p = Path(t)
        files = [p] if p.is_file() else sorted(p.glob("*.md"))
        for f in files:
            if convert_file(f):
                changed.append(str(f))
    print(f"converted {len(changed)} files")
    for c in changed:
        print(c)


if __name__ == "__main__":
    main()
