#!/usr/bin/env python3
"""総合記事② 不動産登記法編 第9章の図解・4コマ・見出し画像プロンプトの機械チェック（標準ライブラリ＋リポジトリの check_prompt.py）。NG 0件が条件。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch9/src/check_all.py"""
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

# 2. 個人の演習結果・問題番号が図解と見出し画像に入っていない（4コマは肢IDのタグと結論帯の問題番号だけ許可）
bad_words = ["誤答", "★", "のべ", "履歴", "回間違", "正答率"]
id_pat = re.compile(r"D\d{4}(?!\d)|[HR]\d{1,2}-Q\d+")
MID = "prompt_midashi_sokatsu02_ch9.md"
for f in sorted(D.glob("prompt_infographic_*.md")) + [D / MID]:
    t = "\n".join(re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S)) if f.name != MID else f.read_text(encoding="utf8")
    for w in bad_words:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
    if id_pat.search(t): NG(f"{f.name}: 問題番号らしい文字列「{id_pat.search(t).group(0)}」がある")
for f in sorted(D.glob("prompt_4koma_*.md")):
    t = f.read_text(encoding="utf8").replace("改訂履歴", "")
    for w in bad_words + ["誤解4回", "誤解3回", "誤解5回"]:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
OK("図解・見出し画像に個人の演習結果・問題番号なし／4コマに演習結果の語なし（上にNGがなければ）")

# 2b. 禁止語：樹形図の意味の木・ツリー（すべてのプロンプト）
tree = re.compile(r"決定木|判定木|ツリー|(?<![立竹樹植苗])木(?:では|に当て|の右|の左|の枝|の根|の分岐|の図|を描|で見|と呼)")
for f in sorted(D.glob("prompt_*.md")):
    m = tree.search(f.read_text(encoding="utf8"))
    if m: NG(f"{f.name}: 禁止語（樹形図の意味の『木』『ツリー』）「{m.group(0)}」がある")
OK("禁止語（決定木・判定木・ツリーなど）なし（上にNGがなければ）")

# 3. 図解：表の行数・カード数の宣言とデータ行が合う／最終確認の漢字が本文にある／画像の中に図番がない／色（青・赤）を指示していない
for f in sorted(D.glob("prompt_infographic_*.md")):
    t = f.read_text(encoding="utf8")
    for blk in re.findall(r"```text\n(.*?)\n```", t, flags=re.S):
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
        if "Draw no check mark and no cross mark" not in body: NG(f"{f.name}: 色の規則（青・赤を使わない）の文がない")
    n = len(re.findall(r"^```text", t, flags=re.M))
    OK(f"{f.name}: プロンプト {n} 本")

# 4. 条文の確認：画像に載せた主な条文の語が、法令DBの原文にある
def rd(name): return (LAWS / name).read_text(encoding="utf8")
law = rd("fudousan-touki-hou.md"); rei = rd("fudousan-touki-rei-betsuhyou.md"); kisoku = rd("fudousan-touki-kisoku-1.md")
junsoku = rd("fudousan-touki-jimu-junsoku.md"); kubun = rd("kubunshoyuu-hou.md")
must = {
    "法": [
        "新築した建物又は区分建物以外の表題登記がない建物の所有権を取得した者は、その所有権の取得の日から一月以内に、表題登記を申請しなければならない",
        "被承継人を表題部所有者とする当該建物についての表題登記を申請することができる",
        "表題登記がない建物に接続して区分建物が新築されて一棟の建物となった場合",
        "表題登記がある建物（区分建物を除く。）に接続して区分建物が新築された場合",
        "当該合体の日から一月以内に、合体後の建物についての建物の表題登記及び合体前の建物についての建物の表題部の登記の抹消",
        "合体前の二以上の建物がいずれも表題登記がある建物であるとき。　当該建物の表題部所有者",
        "合体前の二以上の建物がいずれも所有権の登記がある建物であるとき。　当該建物の所有権の登記名義人",
        "当該変更があった日から一月以内に、当該登記事項に関する変更の登記を申請しなければならない",
        "第四十四条第一項各号（第二号及び第六号を除く。）",
        "共用部分である旨の登記又は団地共用部分である旨の登記がある建物の場合にあっては、所有者",
        "その者に係る表題部所有者についての更正の登記又は所有権の登記があった日から一月以内に",
        "増築その他の工事により相互に接続して区分建物になった場合",
        "一括してしなければならない",
        "表題部所有者又は所有権の登記名義人以外の者は、申請することができない",
        "団地共用部分を共用すべき者の所有する建物",
    ],
    "令別表": [
        "法第四十七条第二項の規定による申請にあっては、相続その他の一般承継があったことを証する",
        "表題部所有者となる者が所有権を有することを証する情報",
        "共用部分である旨を定めた規約を設定したことを証する情報",
        "当該区分所有者が所有する建物の家屋番号",
        "変更後又は更正後の建物図面及び各階平面図",
        "床面積が増加した部分について表題部所有者又は所有権の登記名義人が所有権を有することを証する情報",
        "当該建物の所有者を証する情報",
        "団地共用部分である旨の登記",
    ],
    "規則": [
        "壁その他の区画の中心線（区分建物にあっては、壁その他の区画の内側線）",
        "区分前の建物の登記記録から権利に関する登記を移記",
    ],
    "準則": [
        "附属合併にあっては、合併しようとする建物が主たる建物と附属建物の関係にないとき",
        "区分合併にあっては、区分された建物が互いに接続していないとき",
        "地下何階付き平家建（又は何階建）",
    ],
    "区分所有法": [
        "第四条第二項、第五条第一項並びに第二十二条第一項ただし書及び第二項ただし書",
        "規約により共用部分とすることができる",
        "規約でこの割合と異なる割合が定められているときは、その割合による",
        "前三項の規定は、規約で別段の定めをすることを妨げない",
    ],
}
srcs = {"法": law, "令別表": rei, "規則": kisoku, "準則": junsoku, "区分所有法": kubun}
def norm(s): return re.sub(r"\s+", "", s)
for k, ws in must.items():
    base = norm(srcs[k])
    for w in ws:
        if norm(w) not in base: NG(f"法令DB（{k}）に原文が見つからない：{w}")
OK("条文の語：法令DBの原文と照合（上にNGがなければ一致）")

# 5. 既存（再利用）の4コマが存在する
reuse = [ROOT / "tools/drill/manga/D1289_prompt.md", ROOT / "tools/drill/manga/D1291_prompt.md", ROOT / "tools/drill/manga/D2077_prompt.md",
         ROOT / "note-articles/joubun-nigate/fudousan-touki-hou/art051-1-hyoudaibu-henkou/prompt_4koma_02_kyouyoububun.md"]
for p in reuse:
    if not p.exists(): NG(f"再利用する既存の4コマが見つからない：{p.relative_to(ROOT)}")
OK("既存（再利用）の4コマ4本：存在を確認")

# 6. 章の肢19本がすべて、4コマ・既存の4コマ・図解のどれかで扱われている（README の対応表の肢IDで確認）
readme = (D / "README.md").read_text(encoding="utf8") if (D / "README.md").exists() else ""
ids = "D0378 D0379 D1080 D0584 D1794 D1181 D1291 D1289 D1991 D1279 D0885 D0886 D1890 D1700 D1701 D0538 D2077 D1702 D0797".split()
for i in ids:
    if i not in readme: NG(f"README に肢 {i} の扱い（4コマ／既存／図解）が書かれていない")
OK("章の19肢：README の対応表で全部扱われている")

print(f"\n結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
