#!/usr/bin/env python3
"""総合記事②不動産登記法編 第8章（敷地権）の図解・4コマ・見出し画像プロンプトの機械チェック（標準ライブラリ＋リポジトリの check_prompt.py）。NG 0件が条件。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch8/src/check_all.py"""
import re, sys, json, subprocess, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
D = HERE.parent
LAWS = ROOT / "note-articles" / "laws"
ARTICLE = ROOT / "note-articles" / "column" / "sokatsu-02-fudousan-touki-hou-ch8.md"
ng = []
def NG(msg): ng.append(msg); print("NG  ", msg)
def OK(msg): print("OK  ", msg)
sys.path.insert(0, str(HERE))

TREE_WORDS = re.compile(r"決定木|判定木|ツリー|(?<![立竹樹植苗])木(?:では|に当て|の右|の左|の枝|の根|の分岐|の図|を描|で見|と呼)")
bad_words = ["誤答", "★", "のべ", "履歴", "回間違", "正答率", "誤解4回", "誤解3回", "誤解5回"]
id_pat = re.compile(r"\bD\d{4}\b|[HR]\d{1,2}-Q\d+")

# 1. 4コマ：設計データから作り直した内容とファイルが一致し、check_prompt.py が NG 0件・WARN 0件
r = subprocess.run([sys.executable, str(HERE / "build_4koma.py"), "--verify-sync"], capture_output=True, text=True)
if r.returncode != 0: NG("4コマの機械チェック／同期が NG：\n" + r.stdout)
else: OK("4コマ：生成元と一致、check_prompt.py NG 0件・WARN 0件")

# 2. 個人の演習結果・問題番号が図解と見出し画像に入っていない。4コマは結論帯（問題D…）以外の画像内の文言に問題番号が入っていない
def text_blocks(f):
    return "\n".join(re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S))
for f in sorted(D.glob("prompt_infographic_*.md")) + [D / "prompt_midashi_sokatsu02_ch8.md"]:
    t = text_blocks(f)
    for w in bad_words:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
    if id_pat.search(t): NG(f"{f.name}: 問題番号らしい文字列「{id_pat.search(t).group(0)}」がある")
for f in sorted(D.glob("prompt_4koma_*.md")):
    t = text_blocks(f)
    # 結論帯の2行目（「問題D…　正解…（出典）」）だけは問題番号を載せる
    t2 = re.sub(r"「問題D[^」]*」", "", t)
    if id_pat.search(t2): NG(f"{f.name}: 結論帯以外の画像内の文言に問題番号らしい文字列「{id_pat.search(t2).group(0)}」がある")
    body = f.read_text(encoding="utf8").replace("改訂履歴", "")
    for w in bad_words:
        if w in body: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
OK("図解・見出し画像に個人の演習結果・問題番号なし／4コマは結論帯以外の画像内の文言に問題番号なし（上にNGがなければ）")

# 2b. 樹形図の意味の『木』『ツリー』が全プロンプトにない
for f in sorted(D.glob("prompt_*.md")) + [p for p in sorted(HERE.glob("*.py")) if p.name != "check_all.py"]:
    for m in TREE_WORDS.finditer(f.read_text(encoding="utf8")):
        NG(f"{f.name}: 禁止語「{m.group(0)}」がある")
OK("禁止語（樹形図の意味の木・ツリー）なし（上にNGがなければ）")

# 3. 図解：表の行数の宣言とデータ行が合う／最終確認の漢字が本文にある／画像の中に図番がない
n_img = 0
for f in sorted(D.glob("prompt_infographic_*.md")):
    t = f.read_text(encoding="utf8")
    for blk in re.findall(r"```text\n(.*?)\n```", t, flags=re.S):
        n_img += 1
        body = blk.split("--- FOOTER ---")[0]
        m = re.search(r"(?i)exactly (\d+) columns and exactly (\d+) data rows", body)
        if m:
            rows = len(re.findall(r"^Row \d+:", body, flags=re.M))
            if rows != int(m.group(2)): NG(f"{f.name}: 表の行数の宣言 {m.group(2)} とデータ行 {rows} が違う")
            hdr = re.search(r"^Header row[^\n]*:(.*)$", body, flags=re.M)
            ncol = len(re.findall(r"「[^」]*」", hdr.group(1))) if hdr else -1
            if ncol != int(m.group(1)): NG(f"{f.name}: 表の列数の宣言 {m.group(1)} と見出し行の列 {ncol} が違う")
            for rr in re.findall(r"^Row \d+: (.*)$", body, flags=re.M):
                if len(re.findall(r"「[^」]*」", rr)) != int(m.group(1)): NG(f"{f.name}: データ行の列数が {m.group(1)} でない: {rr[:40]}")
        m = re.search(r"paying special attention to the kanji ([^;]+);", blk)
        if m:
            for k in re.findall(r"[一-鿿]", m.group(1)):
                if k not in body: NG(f"{f.name}: 最終確認の漢字「{k}」が本文にない")
        head = body.split("--- HEADER ---")[1] if "--- HEADER ---" in body else body
        if re.search(r"図\s*\d|Figure", head): NG(f"{f.name}: 画像の中に図番らしい文字がある")
        # 青・赤は判定の流れ図（COLOR RULE を入れたもの）以外で使わない
        if "COLOR RULE" not in body and re.search(r"BLUE|RED", body): NG(f"{f.name}: 流れ図でない図解で青・赤の指定がある")
        if "COLOR RULE" in body and "NO branch" not in body and "RED" not in body: NG(f"{f.name}: 流れ図の配色の規則が不完全")
    OK(f"{f.name}: プロンプト {len(re.findall(r'^```text', t, flags=re.M))} 本")
if n_img != 12: NG(f"図解の枚数が12でない: {n_img}")

# 4. 条文の確認：画像に載せた主な条文の語が、法令DBの原文にある
def norm(s): return re.sub(r"\s+", "", s)
law = norm((LAWS / "fudousan-touki-hou.md").read_text(encoding="utf8"))
kubun = norm((LAWS / "kubunshoyuu-hou.md").read_text(encoding="utf8"))
rei = norm((LAWS / "fudousan-touki-rei-betsuhyou.md").read_text(encoding="utf8"))
kisoku = norm((LAWS / "fudousan-touki-kisoku-1.md").read_text(encoding="utf8"))
must = [
    (law, "区分所有法第四条第二項の規定により共用部分とされたものを含む"),
    (law, "登記されたものに限る"),
    (law, "職権で、当該登記記録中の所有権、地上権その他の権利が敷地権である旨の登記をしなければならない"),
    (law, "当該区分建物についての表題登記の申請は、当該新築された一棟の建物又は当該区分建物が属することとなった一棟の建物に属する他の区分建物についての表題登記の申請と併せてしなければならない"),
    (law, "当該区分建物の所有者は、他の区分建物の所有者に代わって、当該他の区分建物についての表題登記を申請することができる"),
    (law, "当該変更があった日から一月以内に、当該登記事項に関する変更の登記を申請しなければならない"),
    (law, "当該承諾に係る建物又は土地について当該特定登記に係る権利が消滅した旨を登記しなければならない"),
    (law, "特定登記（所有権等の登記以外の権利に関する登記であって、第七十三条第一項の規定により敷地権についてされた登記としての効力を有するものをいう"),
    (law, "敷地権である旨の登記をした土地には、敷地権の移転の登記又は敷地権を目的とする担保権に係る権利に関する登記をすることができない"),
    (law, "敷地権付き区分建物には、当該建物のみの所有権の移転を登記原因とする所有権の登記又は当該建物のみを目的とする担保権に係る権利に関する登記をすることができない"),
    (law, "所有権の登記以外の権利に関する登記がある土地"),
    (kubun, "数個の専有部分に通ずる廊下又は階段室その他構造上区分所有者の全員又はその一部の共用に供されるべき建物の部分は、区分所有権の目的とならない"),
    (kubun, "規約により共用部分とすることができる"),
    (kubun, "区分所有者が建物及び建物が所在する土地と一体として管理又は使用をする庭、通路その他の土地は、規約により建物の敷地とすることができる"),
    (kubun, "分離して処分することができない。ただし、規約に別段の定めがあるときは、この限りでない"),
    (kubun, "出席した区分所有者及びその議決権の各四分の三以上の多数による決議"),
    (kubun, "区分所有者（議決権を有しないものを除く。以下この項前段において同じ。）の過半数"),
    (rei, "当該規約を設定したことを証する情報"),
    (rei, "当該規約を廃止したことを証する情報"),
    (rei, "当該事由を証する情報"),
    (rei, "当該土地の登記事項証明書"),
    (rei, "敷地権とならないときは、当該事由を証する情報"),
    (rei, "合体前の建物のすべての敷地権の割合を合算した敷地権の割合が合体後の建物の敷地権の割合となる場合に限る"),
    (rei, "分筆後の土地の地積測量図"),
    (kisoku, "区分合併に係る建物の合併の登記をする場合において、区分合併後の建物が敷地権のない建物となるときについて準用する"),
    (kisoku, "敷地権の登記原因及びその日付のほか"),
    (kisoku, "特定登記に係る権利が消滅した場合の登記は、敷地権の変更の登記の申請情報と併せて次に掲げる情報が提供された場合にするものとする"),
]
for src, w in must:
    if norm(w) not in src: NG(f"法令DBに原文が見つからない：{w[:50]}")
OK("条文の語：法令DB（不動産登記法・区分所有法・令別表・規則）の原文と照合（上にNGがなければ一致）")

# 5. 4コマの正誤が、一問一答のバンク（tools/drill/data/items.json）と一致する
bank = {i["id"]: i for i in json.load(open(ROOT / "tools/drill/data/items.json", encoding="utf8"))["items"]}
from specs_4koma import SPECS
for fid, sp in SPECS.items():
    for m in re.finditer(r"(D\d{4})＝([〇×])", sp["truth"] if "＝" in sp["truth"] else ""):
        i, mark = m.group(1), m.group(2)
        if i not in bank: NG(f"バンクにない肢: {i}"); continue
        if (mark == "〇") != bool(bank[i]["truth"]): NG(f"{fid}: {i} の正誤がバンクと違う（設計データ {mark}、バンク {bank[i]['truth']}）")
    if "＝" not in sp["truth"]:
        i = sp["id"]; mark = sp["truth"][0]
        if (mark == "〇") != bool(bank[i]["truth"]): NG(f"{fid}: {i} の正誤がバンクと違う")
OK("4コマの正誤：バンクと照合（上にNGがなければ一致）")

# 6. README：記事の付録の最優先肢が全部カバーされ、既存（再利用）の4コマのファイルが実在する。論点【PG1-1】〜【PG1-9】がそろう
readme = (D / "README.md").read_text(encoding="utf8")
art = ARTICLE.read_text(encoding="utf8")
app = art.split("### 付録")[1] if "### 付録" in art else ""
priority = re.findall(r"^- (D\d{4}) ", app, flags=re.M)
if len(priority) != 12: NG(f"付録の最優先肢が12でない: {len(priority)}")
cover_zone = readme.split("## 成果物")[1].split("### 見出し画像")[0] if "## 成果物" in readme else ""
for i in priority:
    if i not in cover_zone: NG(f"README の成果物に最優先肢 {i} がない（新作か既存〈再利用〉として載せる）")
for pg in range(1, 10):
    if f"PG1-{pg}" not in cover_zone: NG(f"README の成果物に論点【PG1-{pg}】がない")
for p in re.findall(r"`(tools/drill/manga/[^`]+\.md)`|`(note-articles/joubun-nigate/[^`]+\.md)`", readme):
    path = p[0] or p[1]
    if "*" in path or "{" in path: continue
    if not (ROOT / path).exists(): NG(f"README に書いたファイルが実在しない: {path}")
OK(f"README：最優先肢 {len(priority)} 肢の網羅と、既存ファイルの実在を確認（上にNGがなければ問題なし）")

# 7. 見出し画像：タイトル1行16字以内、サブタイトルが『苦手論点つぶし　不動産登記法編⑧　…』
mid = (D / "prompt_midashi_sokatsu02_ch8.md").read_text(encoding="utf8")
m1 = re.search(r"- タイトル1行目：(.+?)（", mid); m2 = re.search(r"- タイトル2行目：(.+?)（", mid); ms = re.search(r"- サブタイトル：(.+)", mid)
if not (m1 and m2 and ms): NG("見出し画像の文言（正本）が読めない")
else:
    for t in (m1.group(1), m2.group(1)):
        if len(t) > 16: NG(f"見出し画像のタイトル行が16字を超える: {t}")
    if not ms.group(1).startswith("苦手論点つぶし　不動産登記法編⑧　"): NG(f"見出し画像のサブタイトルの形が違う: {ms.group(1)}")
    for t in (m1.group(1), m2.group(1), ms.group(1)):
        if ("\n" + t + "\n") not in mid.split("```text")[1]: NG(f"見出し画像プロンプトに文言が独立した行として入っていない: {t}")
    kset = set(re.findall(r"[一-鿿]", m1.group(1) + m2.group(1) + ms.group(1)))
    km = re.search(r"special attention to the kanji ([^;]+);", mid)
    if not km or set(re.findall(r"[一-鿿]", km.group(1))) != kset: NG("見出し画像のFinal checkの漢字リストが文言の漢字と一致しない")
    if re.search(r"green|緑", mid): NG("見出し画像プロンプトに緑への言及がある")
OK("見出し画像：文言の形・字数・漢字リスト")

print(f"\n結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
