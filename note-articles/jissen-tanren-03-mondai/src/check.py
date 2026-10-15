# -*- coding: utf-8 -*-
"""実践答練 第3回 択一式の記事（q01〜q20）の機械チェック。

- 記事の体裁（format-template.md）、文体、禁止事項、まとめと正解の整合、
  インフォグラフィック／見出し画像プロンプトの雛形の文言を確認する。
- 使い方： python3 check.py   → NGを1件ごとに表示し、最後に件数を出す。
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from cards import Q  # noqa: E402

# 答練の正答表（問n → 選択肢番号）と、問題の種類（誤り選択=False／正しい選択=True）
ANSWER = {1: 4, 2: 4, 3: 2, 4: 3, 5: 3, 6: 5, 7: 2, 8: 4, 9: 4, 10: 5, 11: 1, 12: 5, 13: 1, 14: 3, 15: 4, 16: 3, 17: 5, 18: 2, 19: 5, 20: 3}
SELECT_CORRECT = {1: False, 2: True, 3: False, 4: False, 5: False, 6: False, 7: True, 8: False, 9: True, 10: True,
                  11: False, 12: False, 13: True, 14: True, 15: True, 16: True, 17: False, 18: True, 19: False, 20: True}
COMBOS = {1: "アウ", 2: "アオ", 3: "イウ", 4: "イエ", 5: "エオ"}

ng = []


def bad(f, msg):
    ng.append(f"NG {os.path.basename(f)}: {msg}")


def split_sections(s):
    """本文（確認事項より前）とそれ以降に分ける"""
    i = s.find("**このまま使える点／使う前に確認したい点**")
    return (s[:i], s[i:]) if i >= 0 else (s, "")


def check_article(n, d):
    f = os.path.join(ROOT, d["file"])
    s = open(f, encoding="utf-8").read()
    lines = s.split("\n")

    # --- タイトル
    m = re.match(r"^## 【土地家屋調査士受験生向け】実践答練 第3回 第%d問〜(.+)〜$" % n, lines[0])
    if not m:
        bad(f, "タイトル行の形が違う")
    else:
        catch = m.group(1)
        if len(catch) > 25:
            bad(f, f"キャッチフレーズが25字超（{len(catch)}字）")
        if re.search(r"(になる|できない|あった|する)$", catch):
            bad(f, "キャッチフレーズの語尾が常体の動詞")
    if not re.search(r"^\*\*出題：実践答練　第3回　択一式　第%d問\*\*$" % n, s, re.M):
        bad(f, "出典行がない／形が違う")

    body, rest = split_sections(s)

    # --- 問題文の引用
    qlines = [l for l in lines if l.startswith(">")]
    if not qlines:
        bad(f, "問題文の引用がない")
    for l in qlines:
        if l.strip() not in (">",) and not (l.endswith("  ") or l.startswith(">　")):
            # 最終行（選択肢）は行末スペース不要
            pass
    sep = [l for l in qlines if l == ">　  "]
    if len(sep) < 5:
        bad(f, "引用ブロックの区切り行（>　␠␠）が少ない")
    # 引用ブロックの直後に --- があるか
    idx_last_q = max(i for i, l in enumerate(lines) if l.startswith(">"))
    if not (lines[idx_last_q + 1] == "" and lines[idx_last_q + 2] == "---"):
        bad(f, "問題文の引用の直後に区切り線がない")
    # 引用内の各行の末尾（最終行を除く）
    for l in qlines[:-1]:
        if l != ">　  " and not l.endswith("  "):
            bad(f, f"引用行の行末に半角スペース2つがない: {l[:30]}")
            break

    # --- 各肢
    heads = re.findall(r"^### ([ア-オ])：(.+)$", body, re.M)
    if [h[0] for h in heads] != list("アイウエオ"):
        bad(f, f"肢の見出しが ア〜オ の順でない: {[h[0] for h in heads]}")
    for k, t in heads:
        if re.search(r"誤り|正しい|誤っ|正解", t):
            bad(f, f"見出しに判定語: {k}：{t}")
    # たとえば
    for k in "アイウエオ":
        mt = re.search(r"### %s：.*?(?=\n### |\n---\n)" % k, body, re.S)
        if not mt:
            bad(f, f"{k}の節が取れない")
            continue
        seg = mt.group(0)
        if "**たとえば**、" not in seg:
            bad(f, f"{k}に「**たとえば**、」の段落がない")
        if not re.search(r"本肢は[^\n]*(誤り|正しい)", seg):
            bad(f, f"{k}に「本肢は誤りです／正しい記述です」がない")

    # --- まとめ
    ms = re.search(r"### まとめ\n\n((?:- .*\n)+)", body)
    verdict = {}
    if not ms:
        bad(f, "まとめがない")
    else:
        for b in ms.group(1).strip().split("\n"):
            mm = re.match(r"- \*\*([ア-オ])（(正|誤)）\*\* (.+)", b)
            if not mm:
                bad(f, f"まとめの行の形が違う: {b[:30]}")
            else:
                verdict[mm.group(1)] = mm.group(2)
                if re.search(r"[（(]?(法|規則|令|準則|民法)\d+条", mm.group(3)):
                    bad(f, f"まとめの行に法令番号: {b[:40]}")
        if len(verdict) != 5:
            bad(f, "まとめが5行でない")
    # 正解の整合
    want = ANSWER[n]
    combo = COMBOS[want] if False else None
    # 選択肢番号から組合せを、問題文の最終行から取る
    mc = re.search(r"%d　(..)" % want, qlines[-1])
    combo = mc.group(1) if mc else None
    mans = re.search(r"\*\*正解：(.)・(.)の組合せ（選択肢(\d)番）\*\*", s)
    if not mans:
        bad(f, "正解の行がない／形が違う")
    else:
        if int(mans.group(3)) != want:
            bad(f, f"正解番号が答練の正答表と違う: {mans.group(3)} ≠ {want}")
        if combo and mans.group(1) + mans.group(2) != combo:
            bad(f, f"正解の組合せ {mans.group(1)+mans.group(2)} が選択肢{want}の {combo} と違う")
        if verdict:
            target = "正" if SELECT_CORRECT[n] else "誤"
            got = "".join(k for k in "アイウエオ" if verdict.get(k) == target)
            if combo and got != combo:
                bad(f, f"まとめの判定から導く組合せ {got} が正解 {combo} と違う")
    # 先出し禁止：最初の肢の解説より前（導入文）に「正解」「結論からいうと」
    intro_end = body.find("### ア：")
    if re.search(r"正解は|結論からいう|正しいのは", body[:intro_end].split("---", 2)[-1]):
        bad(f, "導入文に正解の先出し")

    # --- 文体・禁止事項（引用・コードブロック・まとめ・確認事項・フレーズを除く解説本文）
    pure = body
    pure = re.sub(r"^>.*$", "", pure, flags=re.M)
    pure = re.sub(r"### まとめ.*", "", pure, flags=re.S)
    for ln in pure.split("\n"):
        st = ln.strip()
        if not st or st.startswith("#") or st.startswith("- ") or st == "---":
            continue
        # 敬体：文末が「です。」「ます。」等でない文を検出
        for sent in re.findall(r"[^。]+。", st):
            sent = sent.strip()
            if re.search(r"(である|だ|いる|ない|する|れる|できる|ある|ない|なる|いう|もの|こと)。$", sent) \
                    and not re.search(r"(です|ます|でした|ました|ません|でしょう)。$", sent):
                bad(f, f"常体の文末: ……{sent[-25:]}")
    # 判例・先例・専門誌の番号（解説本文）
    if re.search(r"(最判|最大判|民甲|民三|民二|民事甲|登記研究|平\d+\.\d+\.\d+|昭\d+\.\d+\.\d+)", pure):
        bad(f, "解説本文に判例・先例等の番号")
    if re.search(r"(昭和|平成)\d+年\d+月\d+日", pure):
        bad(f, "解説本文に判例・先例の年月日らしき表記")
    # 肢ア表記
    if re.search(r"肢[ア-オ]", s.split("## インフォグラフィック")[0]):
        bad(f, "「肢ア」表記がある")
    # 半角括弧（URL・バッククォート内を除く）
    plain = re.sub(r"`[^`]*`", "", s.split("## インフォグラフィック")[0])
    plain = re.sub(r"https?://\S+", "", plain)
    if re.search(r"[ぁ-んァ-ヶ一-龠][^\n]{0,20}\([^\n)]*[ぁ-んァ-ヶ一-龠][^\n]*\)", plain):
        bad(f, "半角括弧が日本語本文にある")
    # 表
    if re.search(r"^\|.*\|$", s, re.M):
        bad(f, "Markdown表がある")
    # 樹形図の語
    if re.search(r"決定木|判定木|ツリー|木に当てはめ", s):
        bad(f, "禁止語（決定木・判定木・ツリー）")
    # 個人の演習結果等（条文別シリーズのルールを準用）
    if re.search(r"誤答の回数|何度も間違え|解答の回数", s):
        bad(f, "個人の演習結果らしい語")
    # 段落の長さ（解説本文のみ。1文だけの長い段落は許容）
    for para in re.split(r"\n\n", pure):
        p = para.strip()
        if not p or p.startswith("#") or p.startswith("-") or p == "---" or p.startswith("**"):
            continue
        if len(p) > 125 and p.count("。") >= 2:
            bad(f, f"段落が長い（{len(p)}字・{p.count('。')}文）: {p[:25]}…")
    # 民法の用語（第1〜3問）：簡易チェックは目視

    # --- 確認事項・フレーズ
    if "**このまま使える点／使う前に確認したい点**" not in s:
        bad(f, "確認事項ブロックがない")
    mph = re.search(r"## 見出し画像用フレーズ\n\n((?:- .*\n)+)", s)
    if not mph:
        bad(f, "見出し画像用フレーズがない")
    else:
        ph = mph.group(1).strip().split("\n")
        if len(ph) != 5:
            bad(f, f"見出し画像用フレーズが5つでない（{len(ph)}）")
        if "?" in mph.group(1):
            bad(f, "半角?がある")

    # --- プロンプト
    if "## インフォグラフィック プロンプト（問題全体）" not in s:
        bad(f, "②プロンプトがない")
    if "## 見出し画像プロンプト" not in s:
        bad(f, "見出し画像プロンプトがない")
    blocks = re.findall(r"```\n(.*?)```", s, re.S)
    if len(blocks) != 2:
        bad(f, f"コードブロックが2つでない（{len(blocks)}）")
        return
    info, hdr = blocks
    must_info = ["GLANCEABLE-POSTER REQUIREMENT", "CRITICAL TEXT REQUIREMENT", "BACKGROUND REQUIREMENT",
                 "Simplified Chinese", "Traditional Chinese", "alpha-channel", "Korean Hangul",
                 "nothing is rendered below the last card", "no intro illustration"]
    for w in must_info:
        if w not in info:
            bad(f, f"②に必須文言がない: {w}")
    for w in ["CRITICAL TEXT REQUIREMENT", "BACKGROUND REQUIREMENT", "Simplified Chinese", "Traditional Chinese",
              "alpha-channel", "1280x670"]:
        if w not in hdr:
            bad(f, f"見出し画像プロンプトに必須文言がない: {w}")
    ncards = len(re.findall(r"^--- COLUMN [AB], CARD \d+ ---$", info, re.M))
    if ncards != len(d["cards"]):
        bad(f, "カード数が合わない")
    msub = re.search(r"Subtitle \(smaller, centered, 1行\):\n(.+)\n", info)
    if not msub or not re.search(r"第3回 第%d問\)$" % n, msub.group(1)):
        bad(f, "サブタイトルに問題番号がない")
    if msub and re.search(r"正しい|誤っ|誤り", msub.group(1)):
        bad(f, "サブタイトルに正誤の結論")
    # Final check の漢字リストが本文に実在するか
    mk = re.search(r"paying special\nattention to (.+?) and any", info, re.S)
    if mk:
        body_wo_final = info.split("Final check before rendering")[0]
        for k in mk.group(1).split("・"):
            if k and k not in body_wo_final:
                bad(f, f"Final checkの漢字「{k}」がプロンプト本文にない")
    # 禁止語・メモの混入
    for w in ["hmm", "TODO", "決定木", "判定木", "ツリー"]:
        if w in info or w in hdr:
            bad(f, f"プロンプトに不要な語: {w}")
    # 見出し・結論タグの文字数
    for blk in re.split(r"\n--- COLUMN [AB], CARD \d+ ---\n", info)[1:]:
        mh = re.search(r"Heading \(bold, ONE line, ~20 characters or fewer\):\n(.+)\n", blk)
        mt = re.search(r"Conclusion tag \(.*?\):\n(.+)\n", blk)
        if not mh or not mt:
            bad(f, "カードの見出し／タグが取れない")
            continue
        if len(mh.group(1)) > 20 or not (5 <= len(mt.group(1)) <= 15):
            bad(f, f"見出し/タグの長さ: {mh.group(1)}/{mt.group(1)}")
    # 件数の確認（カード番号の連番）
    nums = [int(x) for x in re.findall(r"CARD (\d+) ---", info)]
    if nums != list(range(1, len(nums) + 1)):
        bad(f, "カード番号が連番でない")
    # 見出し画像のタイトルは結論を書かない（年度・問番号のみのサブタイトル）
    if re.search(r"正しい|誤り", hdr.split("TEXT (reproduce verbatim")[1].split("SCENE")[0]):
        bad(f, "見出し画像の文言に正誤の結論")


def main():
    for n, d in sorted(Q.items()):
        check_article(n, d)
    files = sorted(glob.glob(os.path.join(ROOT, "q[0-9][0-9]-*.md")))
    if len(files) != 20:
        ng.append(f"NG 記事ファイルが20本でない（{len(files)}）")
    for x in ng:
        print(x)
    print(f"--- NG {len(ng)} 件")
    return 1 if ng else 0


if __name__ == "__main__":
    sys.exit(main())
