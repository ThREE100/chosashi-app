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
GARBLED = {"原則": "思則", "まとめて": "まとかて"}   # 過去に画像で字が崩れた語（崩れた形）。本文にあれば Final check で綴りを確認させる
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
    tm = re.search(r"^## 記事タイトル\n\n(【土地家屋調査士受験生向け】4コマ解説図解(D\d{4}(?:・D\d{4})*)～(.+?)～)\n", src, re.M)
    if not tm: NG("「## 記事タイトル」がない、または形式が違う（【土地家屋調査士受験生向け】4コマ解説図解<ID>～<出典>～）")
    else:
        if tm.group(2).split("・")[0] not in path.name: NG(f"記事タイトルのIDがファイル名と違う: {tm.group(2)}")
        if f"出典 {tm.group(3)}" not in src: NG(f"記事タイトルの出典が冒頭の出典と違う: {tm.group(3)}")
        pos = {k: src.find(k) for k in ("## 設計メモ", "## 記事タイトル", "## 構成表")}
        if pos["## 設計メモ"] >= 0 and not (pos["## 設計メモ"] < pos["## 記事タイトル"] < pos["## 構成表"]):
            NG("記事タイトルの位置が、設計メモ（工程A）と構成表の間にない")
        elif pos["## 設計メモ"] < 0 and not (pos["## 記事タイトル"] < pos["## 構成表"]):
            NG("記事タイトルが構成表より前にない")

    # 0b note記事の冒頭文（定型：問いかけの段落＋案内の段落。記事タイトルの後、構成表の前）
    lm = re.search(r"^## note記事の冒頭文\n\n(.+?)\n\n## ", src, re.M | re.S)
    if not lm: NG("「## note記事の冒頭文」がない")
    else:
        paras = [p for p in lm.group(1).split("\n\n") if p.strip()]
        if len(paras) != 3: NG(f"冒頭文は3段落（問いかけ／案内／促し）にする（今は{len(paras)}段落）")
        else:
            p1, p2, p3 = paras
            if tm:
                sm = re.match(r"([HR])(\d+)-Q(\d+)(.+)$", tm.group(3))
                if sm:
                    era = "平成" if sm.group(1) == "H" else "令和"; yy = int(sm.group(2))
                    lab = f"{era}{'元' if (era == '令和' and yy == 1) else yy}年度　第{int(sm.group(3))}問　{sm.group(4)}"
                    want2 = f"択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（{lab}）。"
                    if p2 != want2: NG(f"冒頭文の2段落目が定型と違う。期待：{want2}")
                    if p3 != "先に〇か×かを考えてから、読み進めてみてください。": NG("冒頭文の3段落目が定型と違う。期待：先に〇か×かを考えてから、読み進めてみてください。")
            if not re.search(r"(でしょうか|ますか)。$", p1): NG("冒頭文の1段落目は、問いかけ（〜でしょうか。）で終える")
            if re.search(r"正解|誤り|正しい|結論|できません。$|できます。$", p1): NG("冒頭文の1段落目で結論を先出ししない（正解・誤り・正しい・結論・「〜できます／できません。」）")
            if len(p1) > 110: WARN(f"冒頭文の1段落目が長い（{len(p1)}字。目安110字以内）")
            for sent in re.findall(r"[^。]+。", p1 + p2 + p3):
                ss = re.sub(r"（[^）]*）。$", "。", sent.strip())
                if not re.search(r"(ます|です|ました|でした|でしょうか|ください|ません)。$", ss): NG(f"冒頭文は敬体（です・ます調）にする: {sent.strip()}")
        pos2 = {k: src.find(k) for k in ("## 記事タイトル", "## note記事の冒頭文", "## 構成表")}
        if not (pos2["## 記事タイトル"] < pos2["## note記事の冒頭文"] < pos2["## 構成表"]): NG("冒頭文の位置が、記事タイトルと構成表の間にない")

    # 0c 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）
    hm = re.search(r"^## 見出し画像プロンプト[^\n]*\n(.*?)(?=^## |\Z)", src, re.M | re.S)
    if not hm: NG("「## 見出し画像プロンプト」がない")
    else:
        hs = hm.group(1)
        rows = {}
        for ln in hs.splitlines():
            cols = [x.strip() for x in ln.strip().strip("|").split("|")]
            if ln.startswith("|") and len(cols) == 3 and cols[0] in ("タイトル1行目", "タイトル2行目", "サブタイトル"): rows[cols[0]] = cols[1]
        if len(rows) != 3: NG("見出し画像の文言（正本）の表に、タイトル1行目・2行目・サブタイトルの3行がない")
        else:
            t1, t2, sb = rows["タイトル1行目"], rows["タイトル2行目"], rows["サブタイトル"]
            if tm and sb != f"4コマ解説図解　{tm.group(2)}　{tm.group(3)}": NG(f"見出し画像のサブタイトルが記事タイトルのID・出典と違う: {sb}")
            for t in (t1, t2):
                if len(t) > 16: WARN(f"見出し画像のタイトル行が長い（{len(t)}字）: {t}")
            bl_all = re.findall(r"```text\n(.*?)```", hs, re.S)
            if len(bl_all) != 1: NG(f"見出し画像プロンプトのコードブロックは1つにする（背景は水彩の空に統一。今は{len(bl_all)}個）")
            blocks = {"A": bl_all[0]} if bl_all else {}
            kset = set(re.findall(r"[一-鿿]", t1 + t2 + sb))
            for o, bl in blocks.items():
                for must in ("1280x670", "CRITICAL TEXT REQUIREMENT", "BACKGROUND REQUIREMENT", "Final check before rendering", "fully opaque"):
                    if must not in bl: NG(f"見出し画像プロンプトに必須の記述がない: {must}")
                for t in (t1, t2, sb):
                    if ("\n" + t + "\n") not in bl: NG(f"見出し画像プロンプトに文言が独立した行として入っていない: {t}")
                if re.search(r"green|緑", bl, re.I): NG(f"見出し画像プロンプトに緑への言及がある")
                if re.search(r"✓|✕|\bnot (blue|red|navy|yellow)\b", bl): NG(f"見出し画像プロンプトに記号・否定形の色指定がある")
                km = re.search(r"special attention to the kanji ([^,.;]+(?:, [^,.;]+)*?)(?:,? which|;|\.|$)", bl)
                lk = set(re.findall(r"[一-鿿]", km.group(1))) if km else set()
                if lk != kset: NG(f"見出し画像プロンプトのFinal checkの漢字リストが文言の漢字と一致しない（過不足: {sorted(lk ^ kset)}）")
                hk = re.search(r"the phrase (.+?) is red-orange", bl)
                if not hk or hk.group(1) not in t2: NG(f"見出し画像プロンプトの強調語（red-orange）がタイトル2行目に含まれない")
            texts = {o: re.search(r"TEXT \(reproduce verbatim.*?Do not write any other text", bl, re.S).group(0) for o, bl in blocks.items() if "TEXT (reproduce verbatim" in bl}

    # 0d 画像ファイル名（名づけルール）
    fm = re.search(r"^## 画像ファイル名[^\n]*\n(.*?)(?=^## |\Z)", src, re.M | re.S)
    if not fm: NG("「## 画像ファイル名」がない")
    elif tm:
        base = f"4コマ解説図解{tm.group(2)}～{tm.group(3)}～"
        for need in (f"| {base}.png |", f"| {base}_見出し.png |", f"{base}_v01.png"):
            if need not in fm.group(1): NG(f"画像ファイル名の表に次がない: {need}")

    # 1 必須セクション
    for key in ["CRITICAL TEXT REQUIREMENT", "BACKGROUND REQUIREMENT", "Final check before rendering"]:
        if key not in body: NG(f"必須の段落がない: {key}")
    for key in ["transparen", "alpha", "checkerboard"]:
        if key not in final: NG(f"Final check に背景不透明の語がない: {key}")
    if re.search(r"exactly four|EXACTLY four", body, re.I) is None and "four-panel" not in body:
        WARN("4コマ（exactly four）の明記が見当たらない")

    # 1b 藍子の人体構造（2026-10-07）：段落と手の割り当て（3本目の手を防ぐ）
    if "4コマ" in src[:200] or "four-panel" in body:
        for key in ("ANATOMY (critical", "HAND COUNT RULE", "exactly two arms", "five fingers"):
            if key not in main_body: NG(f"藍子の人体構造の指示がない: {key}")
        for pm in re.finditer(r"(PANEL \d[^\n]*)", main_body):
            if "ONLY トリ先生" in pm.group(1) or "face icons" in pm.group(1) or "NO character" in pm.group(1): continue
            if "hands" not in pm.group(1): NG(f"{pm.group(1)[:8]}: 藍子の手の割り当て（hands:）がPANEL行にない")
        if "exactly two arms" not in final: WARN("Final checkに藍子の腕・手の確認がない")

    # 1c 連続性・吹き出しの改行（2026-10-07 v2ルール。CONTINUITY の段落がある版に適用）
    if "CONTINUITY:" in main_body:
        for bm in re.finditer(rf"- ({LEFT}|{RIGHT}) bubble[^:]*: 「([^」]+)」", main_body):
            t = bm.group(2)
            if "\n" not in t and len(t) > 16: NG(f"吹き出しが17字以上なのに改行位置の指定がない（文節の区切りで改行する）: {t}")
            for line in t.split("\n"):
                if len(line) > 15: WARN(f"吹き出しの1行が長い（{len(line)}字）: {line}")

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
        if len(set(order)) > 1 and order[0] != LEFT: WARN(f"{blk[:8]}: 先に読まれる吹き出しが{LEFT}でない（会話の順序を確認: 質問→答え）")
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

    # 10 一発合格チェック（2026-10-07。D0413・D0624・D1621の画像検品で見つかった不具合の再発防止）
    STRICT = "一発合格ルール" in src and "適用済み" in src   # 新規・改修済みのプロンプトは NG、旧版は WARN（改修時に直す）
    def R(m): (NG if STRICT else WARN)(m if STRICT else "（旧版・改修時に直す）" + m)
    COLOR = re.compile(r"gr[ae]y|navy|white|yellow|pale|light|dark|cream|beige", re.I)
    for pm in re.finditer(r"(PANEL \d.*?)(?=\nPANEL \d|\nCONCLUSION|\Z)", main_body, re.S):
        blk = pm.group(1); tag = blk[:8]; head1 = blk.split("\n", 1)[0]
        for ln in blk.splitlines():
            # 10a 人物・領域・バー・壁の色は必ず指定する（指定がないと意味のない青・赤・緑・ピンクで塗られる）
            if re.search(r"pictogram", ln) and "legend" not in ln.lower() and not COLOR.search(ln):
                R(f"{tag}: 人型ピクトグラムの色の指定がない（同じ色・濃紺のタグなどを書く）: {ln[:70]}")
            if re.search(r"\b(segments?|areas?|wall|ribbon)\b", ln, re.I) and not COLOR.search(ln):
                R(f"{tag}: バー・領域・壁・リボンの色の指定がない: {ln[:70]}")
            # 10b 青・赤・緑・ピンクを使ってよいのは、チェック・クロス・はい・いいえの矢印とラベルだけ
            if re.search(r"\b(pink|green|orange|purple)\b", ln, re.I):
                R(f"{tag}: 使ってよい色以外（ピンク・緑など）の指定: {ln[:70]}")
            if re.search(r"(?<![-\w])(red|blue)\b", ln, re.I) and not re.search(r"check mark|cross|「はい」|「いいえ」|OPPOSITE|opposite|no check", ln, re.I) and "- A checklist" not in ln:
                WARN(f"{tag}: 青・赤を○×・はい／いいえ以外に使っていないか確認: {ln[:70]}")
        # 10c キャラの大きさは数値（px）で指定する
        if ("face icons" in head1 or "VERY SMALL" in head1) and "px" not in head1:
            R(f"{tag}: 顔アイコン・小さなキャラの大きさが数値（px）で指定されていない")
        # 10d キャラなしのコマに吹き出しを置かない
        if "NO character" in head1 and re.search(r"bubble", blk.split("\n", 1)[1]):
            R(f"{tag}: キャラなしのコマに吹き出しがある")
        # 10e 顔アイコンの会話ラリーは1回20字以内
        if "face icons" in head1:
            for bm in re.finditer(r"- (?:%s|%s) bubble[^:]*: 「([^」]+)」" % (LEFT, RIGHT), blk):
                if len(bm.group(1).replace("\n", "")) > 25: WARN(f"{tag}: 顔アイコンの吹き出しが長い（{len(bm.group(1).replace(chr(10), ''))}字。20字前後に）: {bm.group(1)[:30]}")
        # 10f 人物タグが3つ以上並ぶコマは「1列」「左から」の指定を書く
        tags = set(re.findall(r"tags? 「([Ａ-Ｚ])」|「([Ａ-Ｚ])」", blk))
        if len({x for t in tags for x in t if x}) >= 3 and not re.search(r"\bONE row\b|left to right", blk):
            WARN(f"{tag}: 人物が3人以上いるのに、並べ方（ONE row / left to right）の指定がない")
    # 10g 強調語（黄色マーカー）が吹き出しの文中にある（改行は除いて照合）
    for bm in re.finditer(r"bubble[^:]*: 「([^」]+)」 with the part 「([^」]+)」 highlighted", main_body):
        if bm.group(2) not in bm.group(1).replace("\n", ""): NG(f"強調語が吹き出しの文中にない: 「{bm.group(2)}」 / 「{bm.group(1).replace(chr(10), '/')}」")
    # 10h 過去に字が崩れた語は、Final check で綴りを確認させる
    for w, bad in GARBLED.items():
        if w in main_body and f"「{w}」" not in final:
            R(f"過去に「{bad}」と崩れた語「{w}」が本文にあるのに、Final checkで綴りを確認していない（final_extra か生成器の GARBLED）")

    # 9 条文の出典照合（任意）
    iids = re.findall(r"D\d{4}", tm.group(2)) if tm else []
    iid = re.search(r"\b(D\d{4})\b", src)
    if iid and "--no-article" not in sys.argv:
        out = "".join(subprocess.run([sys.executable, str(ROOT / "tools/drill/drill.py"), "explain", x],
                             capture_output=True, text=True, cwd=ROOT).stdout for x in (iids or [iid.group(1)]))
        if not out: WARN("drill.py explain の出力が取れず、条文の出典照合をスキップ")
        else:
            em = re.search(r"^## 記事に無い条文（ユーザー指示で追加）\n\n(.*?)(?=^## )", src, re.M | re.S)
            allowed = set(re.findall(r"^- (.+)$", em.group(1), re.M)) if em else set()
            for ref in dict.fromkeys(re.findall(r"民法\d+条(?:の\d+)?(?:\d+項)?|不動産登記法\d+条", main_body)):
                if ref in allowed: WARN(f"条文「{ref}」は記事に無いが、ユーザー指示で追加された（「記事に無い条文」の節）"); continue
                if ref not in out: NG(f"条文「{ref}」が記事の解説（drill.py explain {iid.group(1)}）にない。記事の範囲を超えている")
    report()

def report():
    for m in ng: print("NG  ", m)
    for m in warn: print("WARN", m)
    print(f"結果: NG {len(ng)}件 / WARN {len(warn)}件")
    sys.exit(1 if ng else 0)

main()
