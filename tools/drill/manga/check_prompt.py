#!/usr/bin/env python3
"""4コマ図解プロンプトの機械チェック（画像生成の前に必ず実行する）。

使い方: python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0520_prompt.md [--no-article]
- 構成表（Markdownの表）と、最初の ```text ブロック（ChatGPT貼付用プロンプト）を照合する。
- NG があれば終了コード1。WARN は目視で判断する。
MANGA_RULES.md の「プロンプト作成の品質ゲート」の機械化できる部分。
"""
import re, subprocess, sys, itertools, difflib, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
RISKY = set("号録権地番建物登記所請還売買当初詐欺規対抗無過効張説解間違肢承諾譲渡押債抵援認届款占帯証代保")
LEFT, RIGHT = "藍子", "トリ先生"
ng, warn = [], []

def NG(m): ng.append(m)
def WARN(m): warn.append(m)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); sys.exit(2)
    path = pathlib.Path(args[0]); src = path.read_text(encoding="utf8")
    m = re.search(r"```text\n(.*?)```", src, re.S)
    if not m: NG("```text のプロンプト本体が見つからない"); return report()
    body = m.group(1)
    final_i = body.find("Final check before rendering")
    if final_i < 0: NG("Final check before rendering の段落がない"); final = ""; main_body = body
    else: main_body, final = body[:final_i], body[final_i:]
    table = "\n".join(l for l in src.splitlines() if l.startswith("|"))

    # 0 記事タイトル（設計メモ（工程A）と構成表の間に置く）
    tm = re.search(r"^## 記事タイトル\n\n(【土地家屋調査士受験生向け】4コマ解説図解(D\d{4})～(.+?)～)\n", src, re.M)
    if not tm: NG("「## 記事タイトル」がない、または形式が違う（【土地家屋調査士受験生向け】4コマ解説図解<ID>～<出典>～）")
    else:
        if tm.group(2) not in path.name: NG(f"記事タイトルのIDがファイル名と違う: {tm.group(2)}")
        if f"出典 {tm.group(3)}" not in src: NG(f"記事タイトルの出典が冒頭の出典と違う: {tm.group(3)}")
        pos = {k: src.find(k) for k in ("## 設計メモ", "## 記事タイトル", "## 構成表")}
        if pos["## 設計メモ"] >= 0 and not (pos["## 設計メモ"] < pos["## 記事タイトル"] < pos["## 構成表"]):
            NG("記事タイトルの位置が、設計メモ（工程A）と構成表の間にない")
        elif pos["## 設計メモ"] < 0 and not (pos["## 記事タイトル"] < pos["## 構成表"]):
            NG("記事タイトルが構成表より前にない")

    # 1 必須セクション
    for key in ["CRITICAL TEXT REQUIREMENT", "BACKGROUND REQUIREMENT", "Final check before rendering"]:
        if key not in body: NG(f"必須の段落がない: {key}")
    for key in ["transparen", "alpha", "checkerboard"]:
        if key not in final: NG(f"Final check に背景不透明の語がない: {key}")
    if re.search(r"exactly four|EXACTLY four", body, re.I) is None and "four-panel" not in body:
        WARN("4コマ（exactly four）の明記が見当たらない")

    # 2 色：緑に触れない、「A or B」の色選択をしない、否定形の色指定をしない
    for pat, why in [(r"green|緑", "緑への言及（禁止・選択指示とも書かない）"),
                     (r"\b(blue|red|navy|yellow)\s+or\s+\w+", "色の二者択一の指示"),
                     (r"\bnot\s+(blue|red|navy|yellow|green)\b", "否定形の色指定（使う色だけを肯定形で書く）"),
                     (r"[青赤黄]か[青赤緑黄]|青または|赤または", "色の二者択一の指示")]:
        for mm in re.finditer(pat, body, re.I):
            NG(f"配色: {why}: …{body[max(0,mm.start()-25):mm.end()+25]!r}")
    if "NO branch" not in body and re.search(r"flowchart|分岐", body, re.I):
        WARN("フローチャート/分岐があるのに Yes=青・No=赤 の定型文（Color rule）がない")
    if "Color rule" not in body: WARN("Color rule の定型文がない（MANGA_RULES.md参照）")

    # 3 文言：本体の「」と構成表の突き合わせ
    quoted = re.findall(r"「([^」]+)」", main_body)
    names = {"トリ先生", "藍子"}
    tbl_norm = re.sub(r"\s+", "", table)
    for q in dict.fromkeys(quoted):
        if q in names: continue
        if re.sub(r"\s+", "", q) not in tbl_norm:
            NG(f"プロンプトの文言が構成表にない: 「{q}」")
    tbl_strings = []
    for line in table.splitlines():
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) >= 4 and cols[0] not in ("領域", "---") and not set(cols[0]) <= set("-"):
            tbl_strings.append((cols[0], cols[2]))
    qn = [re.sub(r"\s+", "", q) for q in quoted]
    joined = "".join(qn)
    for area, text in tbl_strings:
        for part in re.split(r"\s*[/／]\s*", text):
            part = part.strip()
            if not part or part in ("—",): continue
            part = re.sub(r"（[^）]*(先に話す|答える|左|右)[^）]*）", "", part)
            if "「" in part:
                inner = re.findall(r"「([^」]+)」", part)
                outer = re.sub(r"（[^（）]*「[^」]*」[^（）]*）", "", part)
                outer = re.sub(r"[^／/]*「[^」]*」", "", outer) if outer == part else outer
                checks = inner + ([outer] if outer.strip() and outer != part else [])
                for c in checks:
                    if re.sub(r"\s+", "", c) not in re.sub(r"\s+", "", main_body):
                        NG(f"構成表の文言がプロンプトにない（{area}）: {c}")
                continue
            if re.sub(r"\s+", "", part) not in joined and re.sub(r"\s+", "", part) not in re.sub(r"\s+", "", main_body):
                NG(f"構成表の文言がプロンプトにない（{area}）: {part}")

    # 4 簡体字対策の漢字リスト＝本文に実在する字と一致
    lst = re.search(r"confirm the (?:characters|kanji) (.+?) are drawn", final)
    listed = set(re.findall(r"[一-鿿]", lst.group(1))) if lst else set()
    if not lst: WARN("Final check に漢字の注意喚起リストがない")
    text_only = "".join(re.findall(r"[一-鿿]", main_body))
    for k in listed:
        if k not in text_only: NG(f"Final checkの漢字リストに本文にない字: {k}")
    for k in sorted(RISKY & set(text_only)):
        if lst and k not in listed: WARN(f"本文に頻出の誤りやすい漢字がリストにない: {k}")

    # 5 話者・位置・会話順
    for pm in re.finditer(r"(PANEL \d.*?)(?=\nPANEL \d|\nCONCLUSION|\Z)", main_body, re.S):
        blk = pm.group(1); order = []
        for bm in re.finditer(rf"- ({LEFT}|{RIGHT}) bubble \(([^)]*)\)", blk):
            who, pos = bm.group(1), bm.group(2)
            need = "left" if who == LEFT else "right"
            if need not in pos: NG(f"{blk[:8]}: {who} の吹き出しの位置が {need} でない: ({pos})")
            order.append(who)
        if order and order[0] != LEFT: WARN(f"{blk[:8]}: 先に読まれる吹き出しが{LEFT}でない（会話の順序を確認: 質問→答え）")
    for bm in re.finditer(rf"- ({LEFT}|{RIGHT}) bubble[^:]*: 「([^」]+)」", main_body):
        if len(bm.group(2)) > 32: WARN(f"吹き出しが長い（{len(bm.group(2))}字）: {bm.group(2)}")

    # 6 登場人物（Ａ〜Ｄ）の初出：使う前に tag 「Ｘ」 で紹介されているか
    seen = set()
    for pm in re.finditer(r"(PANEL \d.*?)(?=\nPANEL \d|\nCONCLUSION|\Z)", main_body, re.S):
        blk = pm.group(1)
        tag_lines = re.findall(r"[^\n]*(?:pictogram|tag)[^\n]*", blk)
        seen |= set(re.findall(r"「([Ａ-Ｚ])」", "\n".join(tag_lines)))
        used = set(re.findall(r"[Ａ-Ｚ]", "".join(re.findall(r"「([^」]+)」", blk))))
        for u in sorted(used - seen):
            NG(f"{blk[:8]}: 「{u}」が人型タグで紹介される前に文言に登場している")

    # 7 近い文字列の複製対策
    uniq = [q for q in dict.fromkeys(quoted) if len(q) >= 6]
    for a, b in itertools.combinations(uniq, 2):
        if difflib.SequenceMatcher(None, a, b).ratio() > 0.86 and "NOT identical" not in body and "NOT identical" not in main_body:
            WARN(f"1〜2字しか違わない文字列の組に『NOT identical』の注意がない: 「{a}」/「{b}」")

    # 8 同じ箱に○と×
    for line in main_body.splitlines():
        if line.lstrip().startswith("-") and re.search(r"card|box", line, re.I):
            chk = len(re.findall(r"(?<!no )(?<!no\s)check mark", line)); crs = len(re.findall(r"(?<!no )cross", line))
            if chk and crs and "OPPOSITE" not in line and "Do not draw the same" not in line:
                NG(f"同じ箱に check と cross の両方を指示: {line[:80]}")

    # 9 条文の出典照合（任意）
    iid = re.search(r"\b(D\d{4})\b", src)
    if iid and "--no-article" not in sys.argv:
        out = subprocess.run([sys.executable, str(ROOT / "tools/drill/drill.py"), "explain", iid.group(1)],
                             capture_output=True, text=True, cwd=ROOT).stdout
        if not out: WARN("drill.py explain の出力が取れず、条文の出典照合をスキップ")
        else:
            for ref in dict.fromkeys(re.findall(r"民法\d+条(?:の\d+)?(?:\d+項)?|不動産登記法\d+条", main_body)):
                if ref not in out: NG(f"条文「{ref}」が記事の解説（drill.py explain {iid.group(1)}）にない。記事の範囲を超えている")
    report()

def report():
    for m in ng: print("NG  ", m)
    for m in warn: print("WARN", m)
    print(f"結果: NG {len(ng)}件 / WARN {len(warn)}件")
    sys.exit(1 if ng else 0)

main()
