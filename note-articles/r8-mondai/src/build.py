# -*- coding: utf-8 -*-
"""令和8年度 択一式の記事（q01〜q20）を data（d*.py）から作る。

使い方（note-articles/r8-mondai で実行）:
    python3 src/build.py            # 全問を書き出す
    python3 src/build.py 3 14       # 指定した問だけ

- 問題文は exam-data/R08/takuitsu_R08_questions.json から読む。
- 各肢の「欄外メモ」（過去に作った関連記事）は、一問一答バンク（tools/drill/data/items.json）の出典から自動で拾う。
- 個人の解答結果の分析は、記事ではなく personal/ に書き出す（公開用の記事に個人の演習結果を入れない）。
"""
import glob
import importlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib  # noqa: E402
from lib import QS, ANSWER, WRONG_Q, LET, combo  # noqa: E402
from rel import REL_Q  # noqa: E402

DATA = {}
for p in sorted(glob.glob(os.path.join(HERE, "d[0-9][0-9]*.py"))):
    m = importlib.import_module(os.path.basename(p)[:-3])
    DATA.update(m.DATA)

ITEMS = {i["id"]: i for i in json.load(open(os.path.join(lib.REPO, "tools", "drill", "data", "items.json"), encoding="utf-8"))["items"]}

from relkw import REL_KW  # noqa: E402


def rel_paths(key, extra=()):
    n = int(re.match(r"\d+", key).group(0))
    allowed = set("note-articles/" + x if not x.startswith("note-articles") else x for x in REL_Q.get(n, []))
    kw = REL_KW.get(key)
    found = []
    if kw:
        scored = []
        for i, it in ITEMS.items():
            s = sum(w in it["statement"] for w in kw)
            if s == len(kw):
                for src in it["sources"]:
                    scored.append(src["note_path"])
        # 新しい年度から
        def yk(p):
            m = re.search(r"/([hr])(\d+)-mondai/", p)
            if not m:
                return (-1, 0)
            y = int(m.group(2))
            return (1 if m.group(1) == "r" else 0, y)
        uniq = sorted(set(scored), key=yk, reverse=True)
        found = [p for p in uniq if p in allowed][:4]
    for p in extra:
        if p not in found:
            found.append(p)
    # 実在するものだけ
    return [p for p in found if os.path.exists(os.path.join(lib.REPO, p))]


def split_para(text, limit=125):
    """1段落が125字を超え、2文以上あるときは、文（。）の区切りで段落に分ける（かぎ括弧・かっこの中では分けない）。"""
    plain = text.replace("**", "")
    if len(plain) <= limit or plain.count("。") < 2:
        return [text]
    sents, cur, depth = [], "", 0
    for ch in text:
        cur += ch
        if ch in "「（":
            depth += 1
        elif ch in "」）":
            depth = max(0, depth - 1)
        elif ch == "。" and depth == 0:
            sents.append(cur)
            cur = ""
    if cur:
        sents.append(cur)
    lens = [len(x.replace("**", "")) for x in sents]
    n = len(sents)
    total = sum(lens)
    best = None
    for k in range(max(2, -(-total // limit)), n + 1):
        # n文をk個の連続した群に分け、最も長い群をなるべく短くする（動的計画法）
        INF = 10 ** 9
        pre = [0]
        for L in lens:
            pre.append(pre[-1] + L)
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        cut = [[0] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for j in range(1, k + 1):
            for i in range(j, n + 1):
                for m in range(j - 1, i):
                    v = max(dp[j - 1][m], pre[i] - pre[m])
                    if v < dp[j][i]:
                        dp[j][i] = v
                        cut[j][i] = m
        if dp[k][n] <= limit or k == n:
            best = (k, cut)
            break
    k, cut = best
    idx, i = [], n
    for j in range(k, 0, -1):
        m = cut[j][i]
        idx.append((m, i))
        i = m
    return ["".join(sents[m:i]) for m, i in reversed(idx)]


def truth(n, letter):
    inc = letter in combo(n)
    return (not inc) if n in WRONG_Q else inc


def build_article(n, d):
    q = QS[n]
    L = []
    a = L.append
    a("## 【土地家屋調査士受験生向け】令和8年度 第{}問〜{}〜".format(n, d["catch"]))
    a("")
    a("**出題年度：令和8年度　午後の部　第{}問**".format(n))
    a("")
    a(lib.quote_block(n))
    a("")
    a("---")
    a("")
    for ip in d["intro"].split("\n\n"):
        for x in split_para(ip):
            a(x)
            a("")
    qp = [p for p in (("note-articles/" + x) if not x.startswith("note-articles") else x for x in REL_Q.get(n, [])) if os.path.exists(os.path.join(lib.REPO, p))]
    if qp:
        a("※欄外メモ（note投稿時は削除）　この問題の論点に関する、過去に作成した記事：" + "、".join("`{}`".format(p) for p in qp))
        a("")
    for i, c in enumerate(d["ch"]):
        letter = LET[i]
        a("### {}：{}".format(letter, c["h"]))
        a("")
        for p in c["paras"]:
            for x in split_para(p):
                a(x)
                a("")
        for x in split_para("**たとえば**、{}".format(c["eg"])):
            a(x)
            a("")
        if "rel" in c:
            paths = [p for p in c["rel"] if os.path.exists(os.path.join(lib.REPO, p))]
        else:
            paths = rel_paths("{}{}".format(n, letter), c.get("rel_extra", ()))
        if paths:
            a("※欄外メモ（note投稿時は削除）　関連する過去の記事：" + "、".join("`{}`".format(p) for p in paths))
        else:
            fb = [p for p in qp[:3]]
            a("※欄外メモ（note投稿時は削除）　この記述に近い肢を扱った記事は見つかりませんでした。同じ論点を扱う記事：" + "、".join("`{}`".format(p) for p in fb))
        a("")
    a("---")
    a("")
    a("### まとめ")
    a("")
    for i, s in enumerate(d["summ"]):
        a("- **{}（{}）** {}".format(LET[i], "正" if truth(n, LET[i]) else "誤", s))
    a("")
    a(d["closing"])
    a("")
    cb = combo(n)
    a("**正解：{}・{}の組合せ（選択肢{}番）**".format(cb[0], cb[1], ANSWER[n]))
    a("")
    a("---")
    a("")
    a("**このまま使える点／使う前に確認したい点**")
    a("")
    a("- 文章としては、各肢の「※欄外メモ」の行を除いて、このままnoteに貼り付けて投稿できる内容です。")
    a("- 出題番号は、受験者が持ち帰った令和8年度の問題用紙の写真から転記して確認しました。正解番号（{}番＝{}・{}）は、予備校の解答速報（2026年10月18日公開）で確認した暫定のものです。法務省の公式の正答が公表されたら、照合してください。".format(ANSWER[n], cb[0], cb[1]))
    for b in d["confirm"]:
        a("- " + b)
    a("- 各肢の「※欄外メモ」は、過去に作成した記事のうち、同じ論点の肢を扱ったものを一問一答バンクの出典から拾った参考情報です。")
    a("")
    a("---")
    a("")
    a("## 見出し画像用フレーズ")
    a("")
    for p in d["phrases"]:
        a("- " + p)
    a("")
    a("---")
    a("")
    a("## 見出し画像プロンプト")
    a("")
    a("noteの見出し画像（アイキャッチ、1280x670px）用です。年度別の解説記事の見出し画像は、女性のMCキャラクター1人だけを使います（トリ先生・藍子は入れません）。ChatGPTに、基準画像（キャラクターシート_MC-01〜MC-04の4枚）を添付し、下のコードブロックを貼ります。画像は生成していません。タイトルの文字は結論を書かず、問いかけにしています。")
    a("")
    a("```text")
    a(lib.header_prompt(n, d))
    a("```")
    a("")
    a("---")
    a("")
    a("## インフォグラフィック プロンプト（問題全体）")
    a("")
    a(d["desc"])
    a("")
    a("```")
    a(lib.infographic(n, d))
    a("```")
    a("")
    if d.get("mistakes"):
        for i, letter in enumerate(LET):
            m = d["mistakes"][letter]
            a("---")
            a("")
            a("## インフォグラフィック プロンプト（{}肢・間違いノート）".format(letter))
            a("")
            a("{}の記述を、正しいルールの側から理解するための解説図解です。{}".format(letter, m.get("note", "")))
            a("")
            a("```")
            a(lib.mistake_prompt(n, letter, m))
            a("```")
            a("")
    return "\n".join(L).rstrip() + "\n"


def build_personal(n, d):
    p = d["personal"]
    L = []
    a = L.append
    a("# 令和8年度 第{}問 解答結果の分析（個人用・noteには載せない）".format(n))
    a("")
    a("あなたの解答：{}　／　正解：{}　（正解は予備校の解答速報で確認した暫定のもの）".format(p["picked"], p["correct"]))
    a("")
    a("印は、答案の写真から読み取った、各肢についてのあなたの判断です。読み取りに自信がない箇所は「迷いの印」と書いています。")
    a("")
    a("## 肢ごとの分析")
    a("")
    for i, letter in enumerate(LET):
        it = p["items"][letter]
        a("### {}".format(letter))
        a("")
        a("- あなたの判断：{}".format(it["mark"]))
        a("- 実際：{}（{}）".format("正しい記述" if truth(n, letter) else "誤った記述", it["verdict"]))
        a("- 分析：{}".format(it["cause"]))
        a("- 次に確認すること：{}".format(it["fix"]))
        a("- 図解：`{}` の「インフォグラフィック プロンプト（{}肢・間違いノート）」".format(d["file"], letter))
        a("")
    a("## 全体として")
    a("")
    a(p["summary"])
    a("")
    return "\n".join(L)


def main():
    only = [int(x) for x in sys.argv[1:]]
    for n in sorted(DATA):
        if only and n not in only:
            continue
        d = DATA[n]
        open(os.path.join(lib.ROOT, d["file"]), "w", encoding="utf-8").write(build_article(n, d))
        print("wrote", d["file"])
        if d.get("personal"):
            pf = os.path.join(lib.ROOT, "personal", "q{:02d}-analysis.md".format(n))
            open(pf, "w", encoding="utf-8").write(build_personal(n, d))
            print("wrote", os.path.relpath(pf, lib.ROOT))


if __name__ == "__main__":
    main()
