#!/usr/bin/env python3
"""実践答練 第2回の記事（../qNN-*.md）の機械チェック。NG があれば終了コード1。

  python3 check_all.py          全20問
  python3 check_all.py 3 7      指定した問だけ
"""
import os
import re
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from specs import SPECS  # noqa: E402

OUT = os.path.dirname(HERE)
LABELS = "アイウエオ"
NG = []
WARN = []


def ng(n, msg):
    NG.append("NG  Q%02d: %s" % (n, msg))


def warn(n, msg):
    WARN.append("WARN Q%02d: %s" % (n, msg))


def split_sections(text):
    """記事を (本文, 確認事項以降, 見出し画像プロンプト, インフォグラフィック) に分ける"""
    i_mid = text.index("\n## 見出し画像 プロンプト")
    i_info = text.index("\n## インフォグラフィック プロンプト（問題全体）")
    head = text[:i_mid]
    mid = text[i_mid:i_info]
    info = text[i_info:]
    return head, mid, info


def check_article(n):
    s = SPECS[n]
    files = glob.glob(os.path.join(OUT, "q%02d-*.md" % n))
    if len(files) != 1:
        ng(n, "記事ファイルが見つからない／複数ある: %s" % files)
        return
    text = open(files[0], encoding="utf-8").read()
    head, mid, info = split_sections(text)
    lines = head.split("\n")

    # 1 タイトル
    m = re.match(r"^## 【土地家屋調査士受験生向け】実践答練第2回 第(\d+)問〜(.+)〜$", lines[0])
    if not m or int(m.group(1)) != n:
        ng(n, "タイトル行の形が違う: " + lines[0])
    else:
        cp = m.group(2)
        if len(cp) > 25:
            ng(n, "キャッチフレーズが25字を超える(%d字): %s" % (len(cp), cp))
        if not (cp.endswith("です") or cp.endswith("んです") or not re.search(r"(る|い|た|ない|する)$", cp)):
            ng(n, "キャッチフレーズの語尾が常体: " + cp)
    # 2 出典行
    if "**出題年度：実践答練　第2回　択一式　第%d問**" % n not in head:
        ng(n, "出典行がない")
    # 3 引用ブロック
    qlines = [l for l in lines if l.startswith(">")]
    if not qlines or "1　" not in qlines[-1]:
        ng(n, "引用ブロックの末尾に選択肢がない")
    if "\n---\n" not in head.split("\n### ア")[0]:
        ng(n, "引用ブロックの直後に区切り線(---)がない")

    # 4 肢の見出し
    heads = re.findall(r"^### ([アイウエオ])：(.+)$", head, re.M)
    if [h[0] for h in heads] != list(LABELS):
        ng(n, "肢の見出しがア〜オの順にそろっていない: %s" % [h[0] for h in heads])
    for lab, t in heads:
        if re.search(r"誤り|正しい|誤っ", t):
            ng(n, "見出しに正誤の判定語: %s：%s" % (lab, t))
        if "肢" in t:
            ng(n, "見出しに「肢」: " + t)
    # 5 各肢に「たとえば」
    secs = re.split(r"^### [アイウエオ]：.+$", head, flags=re.M)[1:]
    for i, sec in enumerate(secs[:5]):
        body = sec.split("\n---\n")[0]
        if "**たとえば**、" not in body:
            ng(n, "%sに「**たとえば**、」の段落がない" % LABELS[i])

    # 6 まとめと正解
    ms = re.findall(r"^- \*\*([アイウエオ])（(正|誤)）\*\*　(.+)$", head, re.M)
    if [x[0] for x in ms] != list(LABELS):
        ng(n, "まとめの箇条書きがア〜オの順にそろっていない")
    else:
        got = {x[0]: (x[1] == "正") for x in ms}
        if got != s["truth"]:
            ng(n, "まとめの正誤が specs の truth と違う: %s" % got)
        for lab, ok, pt in ms:
            if re.search(r"[（(][^）)]*(条|号|項|最判|大判|民三|民二|登記研究)[^）)]*[）)]", pt):
                ng(n, "まとめの行末に法令番号などの付記: " + pt)
    # 正解の整合
    want_true = s["ask"] == "correct"
    combo = "".join(l for l in LABELS if s["truth"][l] == want_true)
    if s["ask"] == "count":
        want = "%d個" % sum(s["truth"].values())
        ok = s["choices"][s["answer"]] == want
    else:
        want = combo
        ok = s["choices"][s["answer"]] == combo
    if not ok:
        ng(n, "specs の正解番号と、正誤から導いた答えが合わない: %s / %s" % (s["choices"][s["answer"]], want))
    if s["ask"] == "count":
        ans_line = "**正解：%s（選択肢%d番）**" % (want, s["answer"])
    else:
        ans_line = "**正解：%sの組合せ（選択肢%d番）**" % (want, s["answer"])
    if ans_line not in head:
        ng(n, "正解の行がない／違う: " + ans_line)
    # 先出し禁止：正解の行より前に「正解」「正しいのは」を書かない
    pre = head.split("### まとめ")[0]
    if re.search(r"正解は|正しいのは|結論からいうと", pre):
        ng(n, "正解の先出しの疑い")

    # 7 本文（確認事項より前）の書式チェック
    main = head.split("**このまま使える点／使う前に確認したい点**")[0]
    if "**このまま使える点／使う前に確認したい点**" not in head:
        ng(n, "確認事項ブロックがない")
    prose = []
    for l in main.split("\n")[4:]:
        if l.startswith(">") or l.startswith("#") or l.startswith("- ") or l.strip() in ("", "---"):
            continue
        prose.append(l)
    for l in prose:
        if re.search(r"肢[アイウエオ]", l):
            ng(n, "「肢ア」等の表記: " + l[:30])
        if re.search(r"(最判|最大判|大判|最決|民三|民二|民甲|登記研究|質疑応答)", l):
            ng(n, "本文に判例・先例・専門誌の番号: " + l[:40])
        if re.search(r"[A-Za-z0-9ァ-ヶ一-龥ぁ-ん]\(|\)[、。]", l) and "http" not in l:
            ng(n, "半角括弧: " + l[:40])
        if re.search(r"(である|だ)。", l.replace("というものである。", "")):
            warn(n, "常体の疑い: " + l[:50])
        if len(l) > 150 and l.count("。") >= 2 and "**たとえば**" not in l[:8]:
            warn(n, "段落が150字超(%d字): %s" % (len(l), l[:24]))
        elif len(l) > 150 and l.count("。") >= 2:
            warn(n, "たとえば段落が150字超(%d字): %s" % (len(l), l[:24]))
    if re.search(r"\|\s*-+\s*\|", main):
        ng(n, "Markdownの表がある")
    # 8 見出し画像用フレーズ
    ph = head.split("## 見出し画像用フレーズ")[1] if "## 見出し画像用フレーズ" in head else ""
    phl = [l for l in ph.split("\n") if l.startswith("- ")]
    if len(phl) != 5:
        ng(n, "見出し画像用フレーズが5つでない(%d)" % len(phl))
    for l in phl:
        if "?" in l:
            ng(n, "半角?: " + l)
    # 9 プロンプト
    for name, blk in (("見出し画像", mid), ("インフォグラフィック", info)):
        codes = re.findall(r"```\n(.*?)\n```", blk, re.S)
        if len(codes) != 1:
            ng(n, "%sのコードブロックが1つでない" % name)
            continue
        c = codes[0]
        for key in ("CRITICAL TEXT REQUIREMENT", "BACKGROUND REQUIREMENT", "Final check before rendering",
                    "Simplified Chinese", "Traditional Chinese", "transparent"):
            if key not in c:
                ng(n, "%sのプロンプトに %s がない" % (name, key))
        if re.search(r"決定木|判定木|ツリー|木に当てはめ|木では", c):
            ng(n, "%sのプロンプトに禁止語（決定木・ツリー）" % name)
        # Final check の漢字リストが本文に実在するか
        mm = re.search(r"especially\s+(\S+?)\. If any", c) or re.search(r"attention to the kanji ([^;]+);", c)
        if mm:
            body_part = c.split("Final check before rendering")[0]
            # カード・タイトル部分だけ（CRITICALの注意喚起リストを除く）
            body_part = re.sub(r"Pay special attention to the\s+kanji .*?always draw the standard Japanese \(Jōyō\) form\.", "", body_part, flags=re.S)
            for k in re.findall(r"[^\W\d_・]", mm.group(1)):
                if k not in body_part:
                    ng(n, "%sの漢字リストに本文にない字: %s" % (name, k))
    ic = re.findall(r"```\n(.*?)\n```", info, re.S)
    if ic:
        c = ic[0]
        cards = re.findall(r"^--- (?:COLUMN [AB], )?CARD (\d+) ---$", c, re.M)
        if len(cards) != len(s["info"]["cards"]) or not (4 <= len(cards) <= 6):
            ng(n, "カード枚数が合わない: %d" % len(cards))
        if "第%d問" % n not in c.split("Subtitle")[1].split("\n")[1]:
            ng(n, "サブタイトルに問題番号がない")
        sub = c.split("Subtitle (smaller, centered, 1行):\n")[1].split("\n")[0]
        if re.search(r"正しい|誤っ|誤り", sub):
            ng(n, "サブタイトルに正誤の結論")
        for card in s["info"]["cards"]:
            if len(card["heading"]) > 20:
                ng(n, "カード見出しが20字超(%d字): %s" % (len(card["heading"]), card["heading"]))
            if not (5 <= len(card["tag"]) <= 15):
                ng(n, "結論タグが5〜15字でない(%d字): %s" % (len(card["tag"]), card["tag"]))
            if "✓" in card["illust"] and "✕" in card["illust"]:
                warn(n, "1枚のカードに ✓ と ✕ の両方（別の箱か要確認）: " + card["heading"])
    # 10 本文に教材名
    if re.search(r"アガルート", text):
        ng(n, "教材名（アガルート）が記事に出ている")


def main():
    ns = [int(a) for a in sys.argv[1:]] or sorted(SPECS)
    for n in ns:
        if not glob.glob(os.path.join(OUT, "q%02d-*.md" % n)):
            continue
        check_article(n)
    for w in WARN:
        print(w)
    for g in NG:
        print(g)
    print("NG %d件 / WARN %d件" % (len(NG), len(WARN)))
    sys.exit(1 if NG else 0)


if __name__ == "__main__":
    main()
