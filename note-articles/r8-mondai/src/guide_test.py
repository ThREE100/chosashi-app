# -*- coding: utf-8 -*-
"""作図ガイドのデータ（g*.py）の確認用。使い方: python3 src/guide_test.py 1 2 3
各問の作図ガイドのプロンプトを組み立て、形式を確かめて、プロンプトを標準出力に出す（--quiet で出さない）。"""
import importlib
import re
import sys
import os
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib  # noqa: E402

ns = [int(x) for x in sys.argv[1:] if x.isdigit()]
quiet = "--quiet" in sys.argv
GUIDE = {}
for p in sorted(glob.glob(os.path.join(HERE, "g[0-9][0-9]*.py"))):
    GUIDE.update(importlib.import_module(os.path.basename(p)[:-3]).GUIDE)
import build  # noqa: E402

bad = 0
for n in ns:
    d = build.DATA[n]
    d["guide"] = GUIDE[n]
    g = d["guide"]
    pr = lib.guide_prompt(n, d)
    errs = []
    if len(g["panels"]) != 5:
        errs.append("パネルが5枚でない")
    for i, p in enumerate(g["panels"]):
        for k in ("h", "diag", "callout", "tag", "color"):
            if not p.get(k):
                errs.append("パネル%d: %sがない" % (i + 1, k))
        if p.get("color") not in ("blue", "green"):
            errs.append("パネル%d: colorはblue/green" % (i + 1))
        if not 5 <= len(p["tag"]) <= 15:
            errs.append("パネル%d: 結論タグが5〜15字でない(%d字)" % (i + 1, len(p["tag"])))
        if re.search(r"(ない|る|た|い)と確認$", p["h"]):
            errs.append("パネル%d: 見出しが『〜と確認』" % (i + 1))
        if len(p["h"]) > 28:
            errs.append("パネル%d: 見出しが長い(%d字)" % (i + 1, len(p["h"])))
        if "まず" not in p["callout"]:
            errs.append("パネル%d: 着眼点に『まず』（確認の順序）がない" % (i + 1))
        if re.search(r"[0-9０-９]+年.*(号|判)|最判|大判|民集|先例", p["callout"] + p["h"] + p["tag"]):
            errs.append("パネル%d: 判例・先例番号らしい語" % (i + 1))
        if re.search(r"決定木|判定木|ツリー|樹形", p["h"] + p["callout"] + p["tag"] + p["diag"] + g["footer"]):
            errs.append("パネル%d: 禁止語（決定木・ツリー）" % (i + 1))
    if g["field"].count("ア") or "ア〜オ" in g["field"]:
        errs.append("fieldに肢の範囲")
    # 固定文（テンプレート由来）に閉じ括弧が1つ余分にあるため、差は-1が正常
    if (pr.count("(") - pr.count(")")) != -1:
        errs.append("半角括弧の開閉の不一致 %d" % (pr.count("(") - pr.count(")") + 1))
    if "```" in pr:
        errs.append("コードフェンスを含む")
    for i in range(1, 6):
        if "--- PANEL %d（" % i not in pr:
            errs.append("PANEL %dがない" % i)
    print("Q%d: %s" % (n, "OK" if not errs else "NG " + " / ".join(errs)))
    bad += bool(errs)
    if not quiet:
        print(pr)
sys.exit(1 if bad else 0)
