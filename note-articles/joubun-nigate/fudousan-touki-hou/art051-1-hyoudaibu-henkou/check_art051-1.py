#!/usr/bin/env python3
"""第51条第1項（条文別『苦手克服』第1回）の機械チェック。
使い方: python3 note-articles/joubun-nigate/fudousan-touki-hou/art051-1-hyoudaibu-henkou/check_art051-1.py
標準ライブラリのみ。NGがあれば終了コード1。"""
import re, sys, pathlib, json

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]                      # リポジトリのルート（note-articles/ の親）
LAW = ROOT / "note-articles/laws/fudousan-touki-hou.md"
RISKY = set("号録権地番建物登記所請還売買当初詐欺規対抗無過効張説解間違肢承諾譲渡押債抵援認届款占帯証代保")
ng, warn, ok = [], [], []

def NG(m): ng.append(m)
def OK(m): ok.append(m)

def read(name): return (HERE / name).read_text(encoding="utf8")

note = read("note_art051-1.md"); info = read("prompt_infographic_art051-1.md")
mid = read("prompt_midashi_art051-1.md"); data = read("analysis_data_art051-1.md")
four = {n: read(f) for n, f in [("01", "prompt_4koma_01_henkou-no-hani.md"), ("02", "prompt_4koma_02_kyouyoububun.md"),
                                ("03", "prompt_4koma_03_shikichiken.md"), ("04", "prompt_4koma_04_kisanten.md")]}

# 1 条文の原文が laws/ と一致するか
law = LAW.read_text(encoding="utf8")
def block(head):
    i = law.index(head); return law[i:law.index("\n##### ", i + 5)]
p1 = block("##### 第51条（建物の表題部の変更の登記）").split("\n\n")[1].strip()
(OK if ("> " + p1) in note else NG)("51条1項の原文が laws/ と一致" if ("> " + p1) in note else "51条1項の原文が laws/ と一致しない")
a44 = [l for l in block("##### 第44条（建物の表示に関する登記の登記事項）").split("\n") if l.startswith("- ")]
miss = [l for l in a44 if ("> " + l) not in note]
(NG if miss else OK)(f"44条1項各号の原文が laws/ と一致しない: {len(miss)}行" if miss else f"44条1項の各号（{len(a44)}行）が laws/ と一致")

# 2 画像挿入マーカーと、プロンプトの対応
for n in range(1, 7):
    if f"図解{n}「" not in note: NG(f"記事に図解{n}の挿入マーカーがない")
    if not re.search(rf"^## 図解{n}：", info, re.M): NG(f"図解プロンプトに図解{n}がない")
for n in ("01", "02", "03", "04"):
    if f"prompt_4koma_{n}_" not in note: NG(f"記事に4コマ{int(n)}の挿入マーカーがない")
markers = re.findall(r"^> 【画像挿入】", note, re.M)
(OK if len(markers) == 10 else NG)(f"画像挿入マーカー{len(markers)}か所（図解6＋4コマ4＝10か所のはず）")
(OK if len(re.findall(r"^## 図解\d：", info, re.M)) == 6 else NG)("図解プロンプトが6枚")

# 3 図解プロンプト：簡体字対策の漢字リスト、緑の不使用、表の行数
blocks = re.findall(r"```text\n(.*?)\n```", info, re.S)
(OK if len(blocks) == 6 else NG)(f"図解プロンプトのコードブロック{len(blocks)}個")
for i, b in enumerate(blocks, 1):
    body, fin = b.split("Final check before rendering:")
    listed = set(re.search(r"special attention to the kanji ([^;]+);", fin).group(1).replace(" ", "").split(","))
    actual = RISKY & set(re.findall(r"[一-鿿]", body))
    if listed != actual:
        NG(f"図解{i}：Final checkの漢字リストと本文の漢字が違う（余分={sorted(listed-actual)}、不足={sorted(actual-listed)}）")
    if re.search(r"緑|green", b, re.I): NG(f"図解{i}：緑／greenの語が入っている")
    if "透過" in b and "transparent" not in b: NG(f"図解{i}：背景の不透明化の英文がない")
    if "BACKGROUND REQUIREMENT" not in b or "alpha" not in b: NG(f"図解{i}：背景の不透明化の指示がない")
    if "Jōyō" not in b: NG(f"図解{i}：日本語のみ・簡体字禁止の指示がない")
    # 独立した日本語の注意文（「注意：」）を置かない
    if "注意：" in b: NG(f"図解{i}：独立した日本語の注意文がある")
    if "✓" in b or "✕" in b or "✗" in b: NG(f"図解{i}：✓✕の記号の指示がある")
for i, want in ((2, 9), (5, 4), (6, 5)):
    got = len(re.findall(r"^Data row \d+:", blocks[i - 1], re.M))
    (OK if got == want else NG)(f"図解{i}の表の行数 {got}（期待 {want}）")
(OK if "第51条1項の対象外" in blocks[2] and "いいえ" in blocks[2] else NG)("図解3のフローに「いいえ」と対象外のノードがある")
fl = blocks[2]
(OK if len(re.findall(r"^NODE DIAMOND \d", fl, re.M)) == 3 and len(re.findall(r"^NODE RESULT \d", fl, re.M)) == 4 else NG)("図解3：ダイヤ3個・結果4個")

# 4 4コマ：3行の設計メモ、構成表の文言がプロンプト本体にあるか
for n, t in four.items():
    for key in ("【出題者のひっかけ】", "【受験者の勘違い・定着していない点】", "【対比する制度】", "【型の選び方】"):
        if key not in t: NG(f"4コマ{n}：設計メモに{key}がない")
    m = re.search(r"## 構成表（文言の正本）\n\n(?:\|.*\n){2}((?:\|.*\n)+)", t)
    body = re.search(r"## プロンプト本体\n\n```text\n(.*?)```", t, re.S).group(1)
    bad = []
    for row in m.group(1).strip().split("\n"):
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        for s in re.split(r" / ", cells[2]):
            s = s.strip()
            if s and s not in body.replace("\n", ""): bad.append(s)
    (NG if bad else OK)(f"4コマ{n}：構成表の文言がプロンプト本体にない: {bad[:3]}" if bad else f"4コマ{n}：構成表の文言（全部）がプロンプト本体にある")
    if t.count("```text") < 2: NG(f"4コマ{n}：コードブロックが2つ未満（本体・見出し画像）")
    if not re.search(r"Final check before rendering", t): NG(f"4コマ{n}：Final checkがない")
    if "BACKGROUND REQUIREMENT" not in t: NG(f"4コマ{n}：背景の不透明化の指示がない")

# 5 見出し画像
for s in ("建物の表示が変わったら", "1か月以内に何をする？", "苦手克服　不動産登記法　第51条第1項"):
    if s not in mid: NG(f"見出し画像のプロンプトに「{s}」がない")
for s in ("建物の表示が変わったら", "1か月以内に何をする？"):
    if len(s) > 16: NG(f"見出し画像の行が16字を超える: {s}")
(OK if "何をする？" in "1か月以内に何をする？" else NG)("強調語が2行目に含まれる")
if "Arabic numeral 4" in mid: NG("見出し画像：4コマ用の数字（4）の指示が残っている")

# 6 記事：表を使わない、数字が分析データと一致する
if re.search(r"^\|", note, re.M): NG("記事にMarkdownの表がある（シリーズは表を使わない）")
nums = re.findall(r"26回の解答があり、\*\*誤答（誤解または「わからない」）は14回\*\*", note)
(OK if nums else NG)("記事の26回／14回の記述がある")
for pat in ("10回のうち8回が誤答", "6回のうち3回が誤答", "4回のうち0回が誤答", "7回ありました"):
    if pat not in note: NG(f"記事に「{pat}」がない")
for pat in ("合計\n\n26回のうち14回が誤答", "10回のうち8回が誤答", "4回のうち0回が誤答", "回です"):
    if pat not in data: NG(f"分析データに「{pat}」がない")
for lab in ("平成20年度 第5問ア", "平成22年度 第6問イ", "平成23年度 第16問ア", "令和5年度 第17問ウ", "令和4年度 第18問イ", "平成24年度 第13問イ"):
    if lab not in note: NG(f"記事に出典「{lab}」がない")

# 7 一問一答の記録が手元にあれば、数字を再計算して照合する（任意）
try:
    sys.path.insert(0, str(ROOT / "tools/drill")); import drill, collections
    logs = drill.read_log()
    if logs:
        hist = collections.defaultdict(list)
        for r in logs: hist[r["id"]].append((r.get("ans"), r["res"]))
        ids = "D0333 D0688 D1491 D0687 D1796 D1763 D0884 D1278 D0537 D1890 D1093 D0686 D0772 D0988 D1280 D0771 D1369 D1654 D0690".split()
        tot = sum(len(hist[i]) for i in ids); wr = sum(1 for i in ids for _, r in hist[i] if r != "known")
        (OK if (tot, wr) == (26, 14) else warn.append)(f"記録の再計算：{tot}回のうち{wr}回が誤答" if (tot, wr) == (26, 14) else f"WARN 記録の再計算が26/14と違う：{tot}/{wr}（記録が増えた可能性。記事の日付を確認）")
except Exception as e:
    pass

for m in ok: print("OK  ", m)
for m in warn: print(m if isinstance(m, str) and m.startswith("WARN") else "WARN " + str(m))
for m in ng: print("NG  ", m)
print(f"結果: NG {len(ng)}件 / OK {len(ok)}件")
sys.exit(1 if ng else 0)
