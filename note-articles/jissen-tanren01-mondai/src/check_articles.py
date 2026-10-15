# -*- coding: utf-8 -*-
"""実践答練 第1回（択一式）の記事20本の機械チェック。

使い方（jissen-tanren01-mondai で実行）:  python3 -I src/check_articles.py
format-template.md・qa-checklist.md・infographic-prompt-template.md の機械的に確かめられる項目を点検する。
NGが1件でもあれば終了コード1。
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from prompts_data import DATA  # noqa: E402

ROOT = os.path.dirname(HERE)
REPO = os.path.dirname(ROOT)  # note-articles

# 採点基準（正解表）の正解番号と、各選択肢の組合せ（問題文より）
ANSWER = {1: 3, 2: 3, 3: 5, 4: 5, 5: 4, 6: 4, 7: 3, 8: 3, 9: 1, 10: 3,
          11: 2, 12: 3, 13: 5, 14: 4, 15: 3, 16: 5, 17: 4, 18: 3, 19: 5, 20: 2}
COMBO = {  # 正解の組合せ
    1: "イウ", 2: "イウ", 3: "ウオ", 4: "エオ", 5: "ウオ", 6: "ウエ", 7: "イエ", 8: "イウ", 9: "アイ", 10: "イウ",
    11: "アエ", 12: "イエ", 13: "エオ", 14: "ウオ", 15: "イオ", 16: "エオ", 17: "ウオ", 18: "イオ", 19: "ウオ", 20: "アエ"}
# 設問が「誤っているもの」を問うか
WRONG_Q = {1, 4, 7, 8, 9, 10, 15, 16, 18}
LET = "アイウエオ"

ng = []


def bad(f, msg):
    ng.append("{}: {}".format(f, msg))


def strip_code(text):
    return re.sub(r"```.*?```", "", text, flags=re.S)


def split_sections(text):
    """問題文の引用・解説・まとめ以降に分ける。"""
    i_quote_end = None
    lines = text.split("\n")
    # 最後の引用行
    for i, l in enumerate(lines):
        if l.startswith(">"):
            i_quote_end = i
    return lines, i_quote_end


for path in sorted(glob.glob(os.path.join(ROOT, "q*.md"))):
    f = os.path.basename(path)
    n = int(re.match(r"q(\d+)-", f).group(1))
    text = open(path, encoding="utf-8").read()
    body = strip_code(text)
    lines = body.split("\n")

    # 1 タイトル
    m = re.match(r"## 【土地家屋調査士受験生向け】実践答練 第1回 第{}問〜(.+)〜$".format(n), lines[0])
    if not m:
        bad(f, "タイトル行の形式")
    else:
        catch = m.group(1)
        if len(catch) > 25:
            bad(f, "キャッチ{}字>25: {}".format(len(catch), catch))
        if re.search(r"(になる|できない|あった|する)$", catch):
            bad(f, "キャッチ語尾が常体: " + catch)
    # 2 出題行
    if not re.search(r"^\*\*出題年度：アガルートアカデミー　土地家屋調査士講座　実践答練　第1回（択一式）　第{}問\*\*$".format(n), body, re.M):
        bad(f, "出題年度行")
    # 3 引用ブロック
    qlines = [l for l in lines if l.startswith(">")]
    if not qlines:
        bad(f, "引用ブロックなし")
    for l in qlines:
        if l.startswith(">　") and l != ">　  ":
            bad(f, "引用の区切り行の形式: " + repr(l))
        if l.startswith("> ") and not l.endswith("  ") and "選択肢" not in l and not re.match(r"> 1　", l):
            bad(f, "引用行末にハードブレークなし: " + l[:30])
    # 引用の直後の区切り線
    idx = max(i for i, l in enumerate(lines) if l.startswith(">"))
    rest = [l for l in lines[idx + 1:] if l.strip()]
    if not rest or rest[0] != "---":
        bad(f, "引用の直後に---がない")
    # 引用中の肢が転記と一致するか（ア〜オの各記述の連番）
    qs = [l[2:].rstrip() for l in qlines if l.startswith("> ")]
    alts = {}
    for l in qs:
        mm = re.match(r"(?:学生：)?([アイウエオ])　(.*)", l)
        if mm:
            alts[mm.group(1)] = mm.group(2)
    if sorted(alts) != list(LET):
        bad(f, "引用にア〜オがそろっていない: {}".format(sorted(alts)))
    # 選択肢行
    ch = [l for l in qs if l.startswith("1　")]
    if not ch or "5　" not in ch[0]:
        bad(f, "選択肢行なし")
    else:
        combos = dict((int(a), b) for a, b in re.findall(r"(\d)　([アイウエオ]{2})", ch[0]))
        if combos.get(ANSWER[n]) != COMBO[n]:
            bad(f, "選択肢{}の組合せが{}と一致しない: {}".format(ANSWER[n], COMBO[n], combos))

    # 4 見出し
    heads = [l for l in lines if l.startswith("### ")]
    letters = [re.match(r"### ([アイウエオ])：", h).group(1) if re.match(r"### ([アイウエオ])：", h) else None for h in heads]
    if letters[:5] != list(LET) or heads[5] != "### まとめ":
        bad(f, "見出し構造: {}".format(heads))
    for h in heads[:5]:
        if re.search(r"：誤り|誤り──|として正しい|正しいのは|：正しい", h) or "肢" in h:
            bad(f, "見出しに判定語/肢: " + h)
    # 5 「たとえば」
    sec = re.split(r"^### ", body, flags=re.M)
    for s in sec[1:6]:
        if "**たとえば**" not in s:
            bad(f, "たとえばがない: " + s[:10])
    # 6 本肢の結論句の統一
    expl = "\n".join(sec[1:6])
    pos_forms = [p for p in ("本肢は正しいといえます", "本肢は正しい内容です") if p in expl]
    if len(pos_forms) > 1:
        bad(f, "正しい肢の結論句が混在: {}".format(pos_forms))
    if "この肢は誤りです" in expl and "本肢は誤りです" in expl:
        bad(f, "誤りの結論句が混在")
    if n != 20:
        for s in sec[1:6]:
            if not re.search(r"本肢は(誤りです|正しいといえます|正しい内容です)", s):
                bad(f, "肢の結論句がない: " + s[:6])
    # 7 まとめ判定
    mm = re.search(r"### まとめ\n\n((?:- \*\*[アイウエオ]（[正誤]）\*\*.*\n){5})", body)
    if not mm:
        bad(f, "まとめの箇条書き5行が見つからない")
    else:
        judges = re.findall(r"\*\*([アイウエオ])（([正誤])）", mm.group(1))
        wrong = n in WRONG_Q
        for k, j in judges:
            inc = k in COMBO[n]
            stmt_true = (not inc) if wrong else inc
            if (j == "正") != stmt_true:
                bad(f, "まとめ判定が正解と矛盾: {}（{}）".format(k, j))
    # 8 正解行
    ml = re.search(r"^\*\*正解：(.)・(.)の組合せ（選択肢(\d)番）\*\*$", body, re.M)
    if not ml:
        bad(f, "正解行の形式")
    else:
        if ml.group(1) + ml.group(2) != COMBO[n] or int(ml.group(3)) != ANSWER[n]:
            bad(f, "正解行が正解表と不一致")
        # 先出し禁止: 正解行より前（引用と解説）に「正解」の語がないか
        pre = body[: body.index("**正解：")]
        if re.search(r"正解は|正解：", pre):
            bad(f, "正解の先出し")
    # 9 禁止表現
    prose = body
    for pat, name in [(r"\|.*\|.*\|", "Markdown表"), (r"肢[アイウエオ]", "「肢ア」表記"), (r"登記研究", "専門誌"),
                      (r"最判|最大判|最決", "判例番号"), (r"民[二三]第?\d+号|民事[甲乙]第?\d+号|号通達|依命通知", "先例番号(本文)")]:
        # 先例・判例番号は確認事項ブロック以降は可
        scope = prose.split("**このまま使える点")[0]
        # 引用ブロックは除く
        scope = "\n".join(l for l in scope.split("\n") if not l.startswith(">"))
        if re.search(pat, scope):
            bad(f, "本文に" + name)
    # 半角括弧（本文。バッククォート・URL・コードを除く）
    scope = re.sub(r"`[^`]*`", "", body)
    scope = re.sub(r"https?://\S+", "", scope)
    for l in scope.split("\n"):
        if l.startswith(">"):
            continue
        if re.search(r"[()]", l):
            bad(f, "半角括弧: " + l[:40])
    # 常体（本文）。まとめ・引用・見出し・確認事項は除く
    cut = body.split("### まとめ")[0]
    for l in cut.split("\n"):
        if l.startswith(">") or l.startswith("#") or l.startswith("**出題") or not l.strip():
            continue
        # 敬体のはずの文末が「である。」「だ。」
        for s in re.split(r"(?<=。)", l):
            if re.search(r"(である|だ|ある|ない|できる|される|する|ている)。$", s) and not re.search(r"[」）]。$", s):
                # 文中に「」で囲まれた引用や条文の言い回しは除外しない（目視用に警告のみ）
                pass
    for pat in (r"である。", r"ではない。", r"[^な]だ。"):
        for l in cut.split("\n"):
            if l.startswith(">") or l.startswith("#"):
                continue
            if re.search(pat, l):
                bad(f, "常体: " + l[:50])
    # 10 段落の長さ（複数文で125字超）
    for l in cut.split("\n"):
        if l.startswith((">", "#", "**出題", "---")) or not l.strip():
            continue
        plain = l.replace("**", "")
        if len(plain) > 125 and plain.count("。") >= 2:
            bad(f, "長い段落{}字: {}".format(len(plain), plain[:30]))
    # 11 見出し画像用フレーズ
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
    # 12 確認事項ブロック
    if "**このまま使える点／使う前に確認したい点**" not in body:
        bad(f, "確認事項ブロックなし")
    # 13 順序
    order = [body.find(k) for k in ("### まとめ", "**正解：", "**このまま使える点", "## 見出し画像用フレーズ",
                                  "## 見出し画像プロンプト", "## インフォグラフィック プロンプト（問題全体）")]
    if order != sorted(order) or min(order) < 0:
        bad(f, "セクションの順序: {}".format(order))
    # 14 プロンプトのコードブロック
    codes = re.findall(r"```[a-z]*\n(.*?)```", text, flags=re.S)
    if len(codes) != 2:
        bad(f, "コードブロックが2つでない")
    else:
        hp, ip = codes
        for name, c in (("見出し画像", hp), ("インフォグラフィック", ip)):
            for need in ("Traditional Chinese", "transparent", "alpha"):
                if need not in c:
                    bad(f, name + "に必須文言なし: " + need)
            mk = re.search(r"kanji (.+?)(?: — these|;| if any| \. )", c, flags=re.S)
        # 注意漢字がそのプロンプトに登場するか
        for name, c in (("見出し画像", hp), ("インフォグラフィック", ip)):
            m2 = re.search(r"attention to (?:the kanji )?([^.;]+?)(?:\. Also| — these|;)", c.replace("\n", " "))
            if not m2:
                m2 = re.search(r"kanji ([^—]+) — these", c.replace("\n", " "))
            if not m2:
                bad(f, name + "の注意漢字リストが見つからない")
                continue
            ks = [k for k in re.split(r"[・、\s]+", m2.group(1)) if len(k) == 1 and "一" <= k <= "鿿"]
            # リスト以外の部分に登場するか
            rest_txt = c.replace(m2.group(1), "")
            for k in ks:
                if k not in rest_txt:
                    bad(f, name + "の注意漢字が本文に登場しない: " + k)
        # カード数
        if len(re.findall(r"CARD \d+ ---", ip)) != 5:
            bad(f, "カードが5枚でない")
        tl = re.search(r"dark navy with a pale yellow marker stroke behind it:\n(.*?)\nLine 2 is larger[^\n]*:\n(.*?)\nBelow the title[^\n]*:\n(.*?)\nDo not write", hp, flags=re.S)
        if not tl:
            bad(f, "見出し画像のタイトル行が見つからない")
        elif re.search(r"[0-9A-Za-z０-９]", "".join(tl.groups())):
            bad(f, "見出し画像の文字に数字・英字")
        # 結論を書いていないか（簡易）: 見出し画像タイトル
        # 禁止語（樹形図）
        if re.search(r"決定木|判定木|ツリー|木に当て|木では", text):
            bad(f, "禁止語（樹形図）")
        # 簡体字の混入チェック（代表的な簡体字）
        if re.search(r"[权记录证请变观严东书图说订认检关产续义裁]", text.replace("裁", "")):
            pass
    # 15 リンク先
    for p in re.findall(r"`((?:[a-z0-9\-]+/)[a-z0-9\-]+\.md)`", text):
        if not os.path.exists(os.path.join(REPO, p)):
            bad(f, "リンク先が存在しない: " + p)
    for p in re.findall(r"`(note-articles/laws/[a-z0-9\-]+\.md)`", text):
        if not os.path.exists(os.path.join(os.path.dirname(REPO), p)):
            bad(f, "法令DBのパスが存在しない: " + p)

# 簡体字の簡易検出（全ファイル）
SIMPL = "权记录证请变观严东书图说订认检关产续义"
for path in sorted(glob.glob(os.path.join(ROOT, "*.md"))):
    t = open(path, encoding="utf-8").read()
    for ch in SIMPL:
        if ch in t:
            bad(os.path.basename(path), "簡体字の疑い: " + ch)

print("checked", len(glob.glob(os.path.join(ROOT, "q*.md"))), "files")
for x in ng:
    print("NG", x)
print("NG count:", len(ng))
sys.exit(1 if ng else 0)
