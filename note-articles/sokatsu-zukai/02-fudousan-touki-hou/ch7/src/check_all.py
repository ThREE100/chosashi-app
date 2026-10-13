#!/usr/bin/env python3
"""総合記事② 不動産登記法編 第7章の図解・4コマ・見出し画像プロンプトの機械チェック（標準ライブラリ＋リポジトリの check_prompt.py）。NG 0件が条件。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch7/src/check_all.py"""
import re, sys, subprocess, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
D = HERE.parent
LAWS = ROOT / "note-articles" / "laws"
ng = []
def NG(msg): ng.append(msg); print("NG  ", msg)
def OK(msg): print("OK  ", msg)

# 1. 4コマ：設計データから作り直した内容とファイルが一致し、check_prompt.py が NG 0件・WARN 0件
r = subprocess.run([sys.executable, str(HERE / "build_4koma.py"), "--verify-sync"], capture_output=True, text=True)
if r.returncode != 0: NG("4コマの機械チェック／同期が NG：\n" + r.stdout)
else: OK("4コマ6本：生成元と一致、check_prompt.py NG 0件・WARN 0件")
n4 = len(list(D.glob("prompt_4koma_*.md")))
if n4 != 6: NG(f"4コマのプロンプトが6本でない（{n4}本）")

# 2. 個人の演習結果・問題番号が図解と見出し画像に入っていない（4コマは肢IDのタグと結論帯の問題番号だけ許可）
bad_words = ["誤答", "★", "のべ", "履歴", "回間違", "正答率"]
id_pat = re.compile(r"\bD\d{4}\b|[HR]\d{1,2}-Q\d+")
midashi = D / "prompt_midashi_sokatsu02_ch7.md"
for f in sorted(D.glob("prompt_infographic_*.md")) + [midashi]:
    t = "\n".join(re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S)) if f != midashi else f.read_text(encoding="utf8")
    for w in bad_words:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
    if id_pat.search(t): NG(f"{f.name}: 問題番号らしい文字列「{id_pat.search(t).group(0)}」がある")
for f in sorted(D.glob("prompt_4koma_*.md")):
    t = f.read_text(encoding="utf8").replace("改訂履歴", "")
    for w in bad_words + ["誤解4回", "誤解3回", "誤解5回"]:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
OK("図解・見出し画像に個人の演習結果・問題番号なし／4コマに演習結果の語なし（上にNGがなければ）")

# 2b. 禁止語：樹形図の意味の「決定木」「判定木」「ツリー」「木に当てはめる」（図解・見出し・4コマ・README）
tree = re.compile(r"決定木|判定木|ツリー|(?<![立竹樹植苗])木(?:では|に当て|の右|の左|の枝|の根|の分岐|の図|を描|で見|と呼)")
for f in sorted(D.glob("*.md")):
    m = tree.search(f.read_text(encoding="utf8"))
    if m: NG(f"{f.name}: 禁止語「{m.group(0)}」がある")
OK("禁止語（樹形図の意味の木・ツリー）なし（上にNGがなければ）")

# 3. 図解：表の行数・カード数の宣言とデータ行が合う／最終確認の漢字が本文にある／画像の中に図番がない／緑・簡体字の注意
n_img = 0
for f in sorted(D.glob("prompt_infographic_*.md")):
    t = f.read_text(encoding="utf8")
    for blk in re.findall(r"```text\n(.*?)\n```", t, flags=re.S):
        n_img += 1
        body = blk.split("--- FOOTER ---")[0]
        m = re.search(r"exactly (\d+) data rows", body)
        if m:
            rows = len(re.findall(r"^Row \d+:", body, flags=re.M))
            if rows != int(m.group(1)): NG(f"{f.name}: 表の行数の宣言 {m.group(1)} とデータ行 {rows} が違う")
        m = re.search(r"paying special attention to the kanji ([^;]+);", blk)
        if m:
            for k in re.findall(r"[一-鿿]", m.group(1)):
                if k not in body: NG(f"{f.name}: 最終確認の漢字「{k}」が本文にない")
        if re.search(r"図\s*\d|Figure", body.split("--- HEADER ---")[1] if "--- HEADER ---" in body else body):
            NG(f"{f.name}: 画像の中に図番らしい文字がある")
        if re.search(r"green|緑", blk, re.I): NG(f"{f.name}: 緑への言及がある")
        if "BACKGROUND REQUIREMENT" not in blk or "CRITICAL TEXT REQUIREMENT" not in blk: NG(f"{f.name}: 必須の段落（文字・背景）がない")
        # はい／いいえの色を使うのは判定の流れ図（FLOWCHART）だけ
        if "--- FLOWCHART ---" not in blk and re.search(r"COLOR RULE", blk): NG(f"{f.name}: 判定の流れ図でない図解に COLOR RULE（青・赤）がある")
        if "--- FLOWCHART ---" in blk and "COLOR RULE" not in blk: NG(f"{f.name}: 判定の流れ図に COLOR RULE がない")
    n = len(re.findall(r"^```text", t, flags=re.M))
    OK(f"{f.name}: プロンプト {n} 本")
if n_img != 10: NG(f"図解のプロンプトが10本でない（{n_img}本）")

# 4. 条文の確認：画像に載せた主な条文の語が、法令DBの原文にある
hou = (LAWS / "fudousan-touki-hou.md").read_text(encoding="utf8")
rei = (LAWS / "fudousan-touki-rei-betsuhyou.md").read_text(encoding="utf8")
kis = (LAWS / "fudousan-touki-kisoku-1.md").read_text(encoding="utf8")
zei = (LAWS / "touroku-menkyozei-hou.md").read_text(encoding="utf8")
must = {
    "法49条": (hou, ["合体後の建物についての建物の表題登記及び合体前の建物についての建物の表題部の登記の抹消（以下「合体による登記等」と総称する。）",
                    "当該合体の日から一月以内に", "その持分の取得の日から一月以内に", "更正の登記又は所有権の登記があった日から一月以内に",
                    "第四十七条並びに前条第一項及び第二項の規定は、二以上の建物が合体して一個の建物となった場合において合体前の建物がいずれも表題登記がない建物であるとき",
                    "をそれぞれ当該合体後の建物の登記名義人とする所有権の登記を併せて申請しなければならない",
                    "合体前の三以上の建物が表題登記がない建物、表題登記がある建物及び所有権の登記がある建物のみであるとき"]),
    "法50条": (hou, ["当該権利を消滅させることについて承諾したことを証する情報"]),
    "法60条": (hou, ["権利に関する登記の申請は、法令に別段の定めがある場合を除き、登記権利者及び登記義務者が共同してしなければならない"]),
    "令別表13の項": (rei, ["合体前の建物についてされた所有権の登記以外の所有権に関する登記又は先取特権、質権若しくは抵当権に関する登記であって合体後の建物について存続することとなるもの",
                         "合体前の二以上の建物がいずれも敷地権の登記がない区分建物であり、かつ、合体後の建物も敷地権の登記がない区分建物となるときを除く",
                         "表題部所有者となる者が所有権を有することを証する情報", "表題部所有者となる者の住所を証する市町村長",
                         "二以上の存続登記の登記の目的、申請の受付の年月日及び受付番号、登記原因及びその日付並びに登記名義人がいずれも同一であるときの",
                         "これらの者が同一の者でないものとみなした場合における持分",
                         "合体後の建物の持分について存続登記と同一の登記をするときは、当該存続登記に係る権利の登記名義人が当該登記を承諾したことを証する",
                         "当該抵当証券", "登記名義人となる者の住所を証する市町村長", "区分所有法第二十二条第一項ただし書の規約における別段の定めがあること"]),
    "規則35条": (kis, ["令第四条ただし書の法務省令で定めるときは、次に掲げるときとする。"]),
    "登録免許税法": (zei, ["土地の分筆又は建物の分割若しくは区分による登記事項の変更の登記", "土地の合筆又は建物の合併による登記事項の変更の登記"]),
}
for name, (txt, words) in must.items():
    for w in words:
        if w not in txt: NG(f"法令DB（{name}）に原文が見つからない：{w}")
# 規則35条の列挙に、建物の分割と合体による登記等の組合せがない
i = kis.find("令第四条ただし書の法務省令で定めるときは"); seg = kis[i:i + 3500]
if "合体" in seg.split("第三十六条")[0]: NG("規則35条の列挙に『合体』の語がある（図の『分割と合体の組合せはない』を見直す）")
OK("条文の語：法令DBの原文と照合（上にNGがなければ一致）")

print(f"\n結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
