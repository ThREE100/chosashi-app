# -*- coding: utf-8 -*-
"""令和8年度 択一式の記事20本の機械チェック。

使い方（note-articles/r8-mondai で実行）:  python3 src/check_articles.py
format-template.md・qa-checklist.md・infographic-prompt-template.md の、機械的に確かめられる項目を点検する。
NGが1件でもあれば終了コード1。
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib  # noqa: E402
from lib import QS, ANSWER, WRONG_Q, LET, combo  # noqa: E402

ROOT = lib.ROOT
REPO = lib.REPO
ng = []


def bad(f, msg):
    ng.append("{}: {}".format(f, msg))


def strip_code(text):
    return re.sub(r"```.*?```", "", text, flags=re.S)


files = sorted(glob.glob(os.path.join(ROOT, "q*.md")))
if len(files) != 20:
    ng.append("記事が20本ない: {}".format(len(files)))

for path in files:
    f = os.path.basename(path)
    n = int(re.match(r"q(\d+)-", f).group(1))
    text = open(path, encoding="utf-8").read()
    body = strip_code(text)
    lines = body.split("\n")
    cb = combo(n)

    # 1 タイトル
    m = re.match(r"## 【土地家屋調査士受験生向け】令和8年度 第{}問〜(.+)〜$".format(n), lines[0])
    if not m:
        bad(f, "タイトル行の形式")
    else:
        catch = m.group(1)
        if len(catch) > 25:
            bad(f, "キャッチ{}字>25: {}".format(len(catch), catch))
        if re.search(r"(になる|できない|あった|する)$", catch):
            bad(f, "キャッチ語尾が常体: " + catch)
    # 2 出題行
    if not re.search(r"^\*\*出題年度：令和8年度　午後の部　第{}問\*\*$".format(n), body, re.M):
        bad(f, "出題年度行")
    # 3 引用ブロックが、保存した問題文と一致するか
    qlines = [l for l in lines if l.startswith(">")]
    for l in qlines:
        if l.startswith(">　") and l != ">　  ":
            bad(f, "引用の区切り行の形式: " + repr(l))
        if l.startswith("> ") and not l.endswith("  ") and not re.match(r"> 1　", l):
            bad(f, "引用行末にハードブレークなし: " + l[:30])
    idx = max(i for i, l in enumerate(lines) if l.startswith(">"))
    rest = [l for l in lines[idx + 1:] if l.strip()]
    if not rest or rest[0] != "---":
        bad(f, "引用の直後に---がない")
    q = QS[n]
    qtxt = "\n".join(l[2:].rstrip() for l in qlines if l.startswith("> "))
    if q["stem"] not in qtxt:
        bad(f, "設問文が問題文データと一致しない")
    for a in q["alts"]:
        if "{}　{}".format(a["label"], a["text"]) not in qtxt:
            bad(f, "肢{}が問題文データと一致しない".format(a["label"]))
    chs = [l for l in qlines if l.startswith("> 1　")]
    combos = dict((int(a), b) for a, b in re.findall(r"(\d)　([アイウエオ]{2})", chs[0])) if chs else {}
    if combos.get(ANSWER[n]) != cb:
        bad(f, "選択肢{}の組合せが{}と一致しない: {}".format(ANSWER[n], cb, combos))

    # 4 見出し
    heads = [l for l in lines if l.startswith("### ")]
    letters = [re.match(r"### ([アイウエオ])：", h).group(1) if re.match(r"### ([アイウエオ])：", h) else None for h in heads]
    if letters[:5] != list(LET) or heads[5] != "### まとめ":
        bad(f, "見出し構造: {}".format(heads))
    for h in heads[:5]:
        if re.search(r"：誤り|誤り──|として正しい|正しいのは|：正しい", h) or "肢" in h:
            bad(f, "見出しに判定語/肢: " + h)
    # 5 たとえば・結論句
    sec = re.split(r"^### ", body, flags=re.M)
    for s in sec[1:6]:
        if "**たとえば**" not in s:
            bad(f, "たとえばがない: " + s[:10])
        if not re.search(r"本肢は(誤りです|正しいといえます)", s):
            bad(f, "肢の結論句がない: " + s[:6])
        if "※欄外メモ" not in s:
            bad(f, "欄外メモがない: " + s[:6])
    expl = "\n".join(sec[1:6])
    if "この肢は誤りです" in expl:
        bad(f, "結論句の表記が混在")
    # 6 まとめ判定
    mm = re.search(r"### まとめ\n\n((?:- \*\*[アイウエオ]（[正誤]）\*\*.*\n){5})", body)
    if not mm:
        bad(f, "まとめの箇条書き5行が見つからない")
    else:
        wrong = n in WRONG_Q
        for k, j in re.findall(r"\*\*([アイウエオ])（([正誤])）", mm.group(1)):
            inc = k in cb
            stmt_true = (not inc) if wrong else inc
            if (j == "正") != stmt_true:
                bad(f, "まとめ判定が正解と矛盾: {}（{}）".format(k, j))
    # 7 正解行
    ml = re.search(r"^\*\*正解：(.)・(.)の組合せ（選択肢(\d)番）\*\*$", body, re.M)
    if not ml:
        bad(f, "正解行の形式")
    else:
        if ml.group(1) + ml.group(2) != cb or int(ml.group(3)) != ANSWER[n]:
            bad(f, "正解行が正解表と不一致")
        pre = body[: body.index("**正解：")]
        if re.search(r"正解は|正解：", pre):
            bad(f, "正解の先出し")
    # 8 禁止表現
    scope = body.split("**このまま使える点")[0]
    scope = "\n".join(l for l in scope.split("\n") if not l.startswith(">"))
    for pat, name in [(r"\|.*\|.*\|", "Markdown表"), (r"肢[アイウエオ]", "「肢ア」表記"), (r"登記研究", "専門誌"),
                      (r"最判|最大判|最決", "判例番号"), (r"民[二三]第?\d+号|民事[甲乙]第?\d+号|号通達|依命通知", "先例番号(本文)")]:
        if re.search(pat, scope):
            bad(f, "本文に" + name)
    scope2 = re.sub(r"`[^`]*`", "", body)
    scope2 = re.sub(r"https?://\S+", "", scope2)
    for l in scope2.split("\n"):
        if l.startswith(">"):
            continue
        if re.search(r"[()]", l):
            bad(f, "半角括弧: " + l[:40])
    cut = body.split("### まとめ")[0]
    for pat in (r"である。", r"ではない。", r"[^な]だ。"):
        for l in cut.split("\n"):
            if l.startswith(">") or l.startswith("#"):
                continue
            if re.search(pat, l):
                bad(f, "常体: " + l[:50])
    for l in cut.split("\n"):
        if l.startswith((">", "#", "**出題", "---", "※欄外")) or not l.strip():
            continue
        plain = l.replace("**", "")
        if len(plain) > 125 and plain.count("。") >= 2:
            bad(f, "長い段落{}字: {}".format(len(plain), plain[:30]))
    # 9 見出し画像用フレーズ
    mphr = re.search(r"## 見出し画像用フレーズ\n\n((?:- .*\n)+)", body)
    if not mphr:
        bad(f, "見出し画像用フレーズなし")
    else:
        ph = [l[2:] for l in mphr.group(1).strip().split("\n")]
        if len(ph) != 5:
            bad(f, "フレーズが5つでない")
        for p in ph:
            if re.search(r"[?]", p) or not (10 <= len(p) <= 28):
                bad(f, "フレーズの長さ/半角？: " + p)
    # 10 確認事項と順序
    if "**このまま使える点／使う前に確認したい点**" not in body:
        bad(f, "確認事項ブロックなし")
    order = [body.find(k) for k in ("### まとめ", "**正解：", "**このまま使える点", "## 見出し画像用フレーズ",
                                  "## 見出し画像プロンプト", "## インフォグラフィック プロンプト（問題全体）")]
    if order != sorted(order) or min(order) < 0:
        bad(f, "セクションの順序: {}".format(order))
    # 11 プロンプト
    codes = re.findall(r"```[a-z]*\n(.*?)```", text, flags=re.S)
    expect = 2 + (5 if n in (3, 4, 13, 14, 17, 18) else 0)
    if len(codes) != expect:
        bad(f, "コードブロックが{}個でない: {}".format(expect, len(codes)))
    else:
        for i, c in enumerate(codes):
            name = ["見出し画像", "インフォグラフィック"][i] if i < 2 else "間違いノート" + LET[i - 2]
            for need in ("Traditional Chinese", "transparent", "alpha"):
                if need not in c:
                    bad(f, name + "に必須文言なし: " + need)
            if i >= 2 and re.search(r"あなた|誤答|ドリル|演習|正答率|回目|解答履歴|令和\d+年度 午後", c.replace("令和8年度 第", "")):
                bad(f, name + "に個人の演習結果らしい語")
            if "誤答" in c or "ドリル" in c:
                bad(f, name + "に個人の演習結果らしい語")
        ip = codes[1]
        if len(re.findall(r"CARD \d+ ---", ip)) != 5:
            bad(f, "カードが5枚でない")
        hp = codes[0]
        tl = re.search(r"dark navy with a pale yellow marker stroke behind it:\n(.*?)\nLine 2 is larger[^\n]*:\n(.*?)\nBelow the title[^\n]*:\n(.*?)\nDo not write", hp, flags=re.S)
        if not tl:
            bad(f, "見出し画像のタイトル行が見つからない")
        elif re.search(r"[0-9A-Za-z０-９]", "".join(tl.groups())):
            bad(f, "見出し画像の文字に数字・英字")
    if re.search(r"決定木|判定木|ツリー|木に当て|木では", text):
        bad(f, "禁止語（樹形図）")
    # 12 リンク先
    for p in re.findall(r"`(note-articles[^`]*\.md)`", text):
        if not os.path.exists(os.path.join(REPO, p)):
            bad(f, "リンク先が存在しない: " + p)
    if len(re.findall(r"※欄外メモ", text)) < 6:
        bad(f, "欄外メモが6か所未満")
    # 13 個人用の分析ファイル（誤答の問題のみ）
    if n in (3, 4, 13, 14, 17, 18):
        pf = os.path.join(ROOT, "personal", "q{:02d}-analysis.md".format(n))
        if not os.path.exists(pf):
            bad(f, "個人用の分析ファイルがない")
    # 14 記事に個人の演習結果が入っていないか
    for pat in ("あなたの解答", "あなたの判断", "自信あり", "迷いの印"):
        if pat in text:
            bad(f, "記事に個人の演習結果の語: " + pat)

SIMPL = "权记录证请变观严东书图说订认检关产续义"
for path in sorted(glob.glob(os.path.join(ROOT, "*.md")) + glob.glob(os.path.join(ROOT, "personal", "*.md"))):
    t = open(path, encoding="utf-8").read()
    for ch in SIMPL:
        if ch in t:
            bad(os.path.basename(path), "簡体字の疑い: " + ch)

print("checked", len(files), "files")
for x in ng:
    print("NG", x)
print("NG count:", len(ng))
sys.exit(1 if ng else 0)
