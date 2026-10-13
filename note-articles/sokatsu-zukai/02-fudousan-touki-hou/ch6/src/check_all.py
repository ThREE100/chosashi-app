#!/usr/bin/env python3
"""総合記事②不動産登記法編 第6章の図解・4コマ・見出し画像プロンプトの機械チェック（標準ライブラリ＋リポジトリの check_prompt.py）。NG 0件が条件。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch6/src/check_all.py"""
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
if n4 != 6: NG(f"4コマのファイルが6本でない（{n4}本）")

# 2. 個人の演習結果・問題番号が図解・見出し画像・4コマの画像の文言に入っていない（4コマは結論帯の問題番号〈問題D…〉だけ許可）
bad_words = ["誤答", "★", "のべ", "履歴", "回間違", "正答率"]
id_pat = re.compile(r"\bD\d{4}\b|[HR]\d{1,2}-Q\d+")
for f in sorted(D.glob("prompt_infographic_*.md")) + [D / "prompt_midashi_sokatsu02_ch6.md"]:
    t = "\n".join(re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S)) if f.name != "prompt_midashi_sokatsu02_ch6.md" else f.read_text(encoding="utf8")
    for w in bad_words:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
    if id_pat.search(t): NG(f"{f.name}: 問題番号らしい文字列「{id_pat.search(t).group(0)}」がある")
for f in sorted(D.glob("prompt_4koma_*.md")):
    full = f.read_text(encoding="utf8")
    body = "\n".join(re.findall(r"```text\n(.*?)\n```", full, flags=re.S))
    body2 = re.sub(r"問題D[^」]*", "", body)  # 結論帯の問題番号だけ許可
    if id_pat.search(body2): NG(f"{f.name}: 画像の文言（結論帯を除く）に問題番号らしい文字列「{id_pat.search(body2).group(0)}」がある")
    if "肢D" in body2: NG(f"{f.name}: 画像の文言に「肢D…」のタグがある")
    for w in bad_words + ["誤解4回", "誤解3回", "誤解5回"]:
        if w in full.replace("改訂履歴", ""): NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
    if not re.search(r"問題D\d{4}", body): NG(f"{f.name}: 結論帯の問題番号がない")
OK("画像の文言に個人の演習結果・問題番号なし（4コマは結論帯の問題番号のみ。上にNGがなければ）")

# 2b. 禁止語：樹形図の意味の『決定木』『判定木』『ツリー』『木に当てはめる』『木では』（すべての生成物）
tree = re.compile(r"決定木|判定木|ツリー|木に当てはめ|木では|木の右")
for f in sorted(D.glob("prompt_*.md")):
    m = tree.search(f.read_text(encoding="utf8"))
    if m: NG(f"{f.name}: 禁止語「{m.group(0)}」がある")
OK("禁止語（決定木・判定木・ツリー など）なし（上にNGがなければ）")

# 3. 図解：表の行数・カード数の宣言とデータ行が合う／最終確認の漢字が本文にある／画像の中に図番がない／青・赤の使い方
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
        is_flow = "--- FLOWCHART ---" in body
        if not is_flow and re.search(r"\bBLUE\b|\bRED\b", body): NG(f"{f.name}: 分類中心の図に青・赤の指示がある")
        if is_flow:
            if re.search(r"label (?:\")?「(?:はい|いいえ)」", body): NG(f"{f.name}: フローチャートの矢印にはい／いいえのラベルがある（この図は中立のラベル）")
            if len(re.findall(r"^NODE DIAMOND", body, flags=re.M)) != 3 or len(re.findall(r"^NODE RESULT", body, flags=re.M)) != 4:
                NG(f"{f.name}: フローチャートの菱形3・結果の箱4の数が合わない")
    n = len(re.findall(r"^```text", t, flags=re.M))
    OK(f"{f.name}: プロンプト {n} 本")
if n_img != 10: NG(f"図解が10枚でない（{n_img}枚）")

# 3b. 見出し画像：タイトル2行は16字以内、サブタイトルにシリーズ名と丸数字
mid = (D / "prompt_midashi_sokatsu02_ch6.md").read_text(encoding="utf8")
m1 = re.search(r"タイトル1行目：(.+?)（", mid); m2 = re.search(r"タイトル2行目：(.+?)（", mid); ms = re.search(r"サブタイトル：(.+)", mid)
if not (m1 and m2 and ms): NG("見出し画像の文言（正本）が読み取れない")
else:
    for lbl, mm in (("1行目", m1), ("2行目", m2)):
        if len(mm.group(1)) > 16: NG(f"見出し画像のタイトル{lbl}が16字を超える: {mm.group(1)}")
    if not ms.group(1).startswith("苦手論点つぶし　不動産登記法編⑥　"): NG("見出し画像のサブタイトルが『苦手論点つぶし　不動産登記法編⑥　…』でない")
    for s in (m1.group(1), m2.group(1), ms.group(1)):
        if ("\n" + s + "\n") not in mid.split("## 見出し画像プロンプト本体")[1]: NG(f"見出し画像プロンプトに文言が独立した行として入っていない: {s}")
OK("見出し画像：タイトル2行・サブタイトルの形式を確認（上にNGがなければ）")

# 4. 条文の確認：画像に載せた主な条文の語が、法令DBの原文にある
hou = (LAWS / "fudousan-touki-hou.md").read_text(encoding="utf8")
rei = (LAWS / "fudousan-touki-rei.md").read_text(encoding="utf8")
rei_b = (LAWS / "fudousan-touki-rei-betsuhyou.md").read_text(encoding="utf8")
kis = (LAWS / "fudousan-touki-kisoku-1.md").read_text(encoding="utf8")
jun = (LAWS / "fudousan-touki-jimu-junsoku.md").read_text(encoding="utf8")
tmz = (LAWS / "touroku-menkyozei-hou.md").read_text(encoding="utf8")
checks = [
    (hou, "法56条", ["共用部分である旨の登記又は団地共用部分である旨の登記がある建物の合併の登記", "表題部所有者又は所有権の登記名義人が相互に異なる建物の合併の登記",
                     "表題部所有者又は所有権の登記名義人が相互に持分を異にする建物の合併の登記", "所有権の登記がない建物と所有権の登記がある建物との建物の合併の登記",
                     "所有権等の登記以外の権利に関する登記がある建物"]),
    (hou, "法41条2号", ["地目又は地番区域が相互に異なる土地の合筆の登記"]),
    (hou, "法54条", ["建物の合併の登記（表題登記がある建物を登記記録上他の表題登記がある建物の附属建物とする登記又は表題登記がある区分建物を登記記録上これと接続する他の区分建物である表題登記がある建物若しくは附属建物に合併して一個の建物とする登記をいう。",
                     "第四十条の規定は、所有権等の登記以外の権利に関する登記がある建物についての建物の分割の登記又は建物の区分の登記をするときについて準用する"]),
    (hou, "法40条", ["当該権利を分筆後のいずれかの土地について消滅させることを承諾したことを証する情報", "当該第三者が承諾したことを証する情報が併せて提供されたときに限る"]),
    (kis, "規則131条", ["担保権の登記であって、登記の目的、申請の受付の年月日及び受付番号並びに登記原因及びその日付が同一のもの", "信託の登記であって、法第九十七条第一項各号に掲げる登記事項が同一のもの"]),
    (kis, "規則35条", ["甲建物の登記記録から甲建物の附属建物を分割して、これを乙建物の附属建物としようとする場合において、建物の分割の登記及び建物の合併の登記の申請をするとき",
                      "乙建物又は乙建物の附属建物が甲建物の附属建物と接続する区分建物である場合に限る", "甲建物を区分して、その一部を乙建物の附属建物としようとする場合において、建物の区分の登記及び建物の合併の登記の申請をするとき",
                      "乙建物又は乙建物の附属建物が当該一部と接続する区分建物である場合に限る",
                      "同一の不動産について申請する二以上の登記が、いずれも不動産の表題部の登記事項に関する変更の登記又は更正の登記であるとき",
                      "同一の不動産について申請する二以上の登記が、不動産の表題部の登記事項に関する変更の登記又は更正の登記及び土地の分筆の登記若しくは合筆の登記又は建物の分割の登記、建物の区分の登記若しくは建物の合併の登記であるとき"]),
    (kis, "規則127条3項", ["変更後の不動産所在事項、分割により変更した旨及び変更前の不動産所在事項を抹消する記号を記録しなければならない"]),
    (kis, "規則128条", ["現に効力を有する所有権の登記がされた後当該分割に係る附属建物の新築による当該分割前の建物の表題部の登記事項に関する変更の登記がされていたときは", "分割による所有権の登記をする旨",
                       "所有権の登記名義人の氏名又は名称及び住所並びに登記名義人が二人以上であるときは当該所有権の登記名義人ごとの持分", "登記の年月日"]),
    (kis, "規則133条1項", ["区分建物である甲建物を乙建物又は乙建物の附属建物に合併する建物の合併（乙建物又は乙建物の附属建物が甲建物と接続する区分建物である場合に限る。以下「区分合併」という。）"]),
    (jun, "準則78条1項", ["効用上一体として利用される状態にある数棟の建物は、所有者の意思に反しない限り"]),
    (rei_b, "令別表16の項", ["当該分割後、区分後又は合併後の建物図面及び各階平面図"]),
    (rei, "令8条", ["所有権の登記がある建物の合併の登記", "当該合併に係る建物のうちいずれか一個の建物の所有権の登記名義人の登記識別情報"]),
    (tmz, "登録免許税法別表第一", ["分筆又は分割若しくは区分後の不動産の個数", "合筆又は合併後の不動産の個数", "一個につき千円"]),
]
for text, label, words in checks:
    for w in words:
        if w not in text: NG(f"法令DBに原文が見つからない（{label}）：{w}")
OK("条文の語：法令DBの原文と照合（上にNGがなければ一致）")

# 5. 画像の文言で使う条番号が、法令DBの号数と合っている（規則35条の号の並び）
m35 = re.search(r"###### 第三十五条.*?(?=###### 第三十六条)", kis, flags=re.S)
if m35:
    items = re.findall(r"^\s+- (一|二|三|四|五|六|七|八|九|十) (.+)$", m35.group(0), flags=re.M)
    d = {k: v for k, v in items}
    if not d["二"].startswith("甲建物の登記記録から甲建物の附属建物を分割して、これを乙建物の附属建物としようとする"): NG("規則35条2号の内容が図解7の2号と合わない")
    if "区分建物に限る" not in d["三"]: NG("規則35条3号の内容が図解7の3号と合わない")
    if not d["四"].startswith("甲建物を区分して、その一部を乙建物の附属建物"): NG("規則35条4号の内容が図解7の4号と合わない")
    if not d["五"].startswith("甲建物を区分して、その一部を乙建物又は乙建物の附属建物に合併"): NG("規則35条5号の内容が図解7の5号と合わない")
    if not d["六"].startswith("同一の不動産について申請する二以上の登記が、いずれも不動産の表題部"): NG("規則35条6号の内容が図解7の6号と合わない")
    if "建物の分割の登記" not in d["七"]: NG("規則35条7号の内容が図解7の7号と合わない")
OK("規則35条の号の並びを確認（上にNGがなければ一致）")

print(f"\n結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
