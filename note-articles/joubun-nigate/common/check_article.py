#!/usr/bin/env python3
"""条文別『苦手克服』シリーズ 1回分（1フォルダ）の機械チェック。
使い方: python3 note-articles/joubun-nigate/common/check_article.py <フォルダ>   （フォルダに check_config.json が要る）
標準ライブラリのみ。NGがあれば終了コード1。
確かめること：①条文の原文が note-articles/laws/ と一致 ②画像挿入マーカーとプロンプトの対応 ③図解プロンプトの簡体字対策・
配色・表の行数・フローの構成 ④4コマの設計メモと構成表 ⑤見出し画像の文言 ⑥記事に、個人の演習結果・問題番号が入っていない"""
import re, sys, json, pathlib

folder = pathlib.Path(sys.argv[1]).resolve()
cfg = json.loads((folder / "check_config.json").read_text(encoding="utf8"))
ROOT = next(p for p in folder.parents if (p / "note-articles").is_dir() or p.name == "note-articles")
ROOT = ROOT if (ROOT / "note-articles").is_dir() else ROOT.parent
RISKY = set("号録権地番建物登記所請還売買当初詐欺規対抗無過効張説解間違肢承諾譲渡押債抵援認届款占帯証代保")
ng, ok = [], []
def NG(m): ng.append(m)
def OK(m): ok.append(m)
def chk(cond, good, bad): (OK if cond else NG)(good if cond else bad)
def read(n): return (folder / n).read_text(encoding="utf8")

note, info, mid = read(cfg["note"]), read(cfg["infographic"]), read(cfg["midashi"])
four = [read(f) for f in cfg["fourkoma"]]

# 1 条文の原文
law = (ROOT / "note-articles/laws/fudousan-touki-hou.md").read_text(encoding="utf8")
def block(head):
    i = law.index(head); return law[i:law.index("\n##### ", i + 5)]
for qd in cfg["law_quotes"]:
    b = block(qd["head"])
    if qd["kind"] == "first_paragraph":
        t = b.split("\n\n")[1].strip(); chk(("> " + t) in note, f"{qd['head']}の原文が laws/ と一致", f"{qd['head']}の原文が laws/ と一致しない")
    else:
        items = [l for l in b.split("\n") if l.startswith("- ")]
        miss = [l for l in items if ("> " + l) not in note]
        chk(not miss, f"{qd['head']}の各号（{len(items)}行）が laws/ と一致", f"{qd['head']}の各号が laws/ と一致しない: {len(miss)}行")

# 2 マーカーとプロンプトの対応
ni, nf = cfg["n_infographic"], len(four)
for n in range(1, ni + 1):
    if f"図解{n}「" not in note: NG(f"記事に図解{n}の挿入マーカーがない")
    if not re.search(rf"^## 図解{n}：", info, re.M): NG(f"図解プロンプトに図解{n}がない")
for f in cfg["fourkoma"]:
    if f not in note: NG(f"記事に {f} の挿入マーカーがない")
chk(len(re.findall(r"^> 【画像挿入】", note, re.M)) == ni + nf, f"画像挿入マーカー{ni + nf}か所", f"画像挿入マーカーの数が{ni + nf}か所でない")

# 3 図解プロンプト
blocks = re.findall(r"```text\n(.*?)\n```", info, re.S)
chk(len(blocks) == ni, f"図解プロンプトのコードブロック{ni}個", f"図解プロンプトのコードブロックが{len(blocks)}個")
for i, b in enumerate(blocks, 1):
    body, fin = b.split("Final check before rendering:")
    listed = set(re.search(r"special attention to the kanji ([^;]+);", fin).group(1).replace(" ", "").split(","))
    actual = RISKY & set(re.findall(r"[一-鿿]", body))
    if listed != actual: NG(f"図解{i}：Final checkの漢字リストと本文の漢字が違う（余分={sorted(listed-actual)}、不足={sorted(actual-listed)}）")
    if re.search(r"緑|green", b, re.I): NG(f"図解{i}：緑／greenの語が入っている")
    if "BACKGROUND REQUIREMENT" not in b or "alpha" not in b: NG(f"図解{i}：背景の不透明化の指示がない")
    if "Jōyō" not in b: NG(f"図解{i}：日本語のみ・簡体字禁止の指示がない")
    if "注意：" in b: NG(f"図解{i}：独立した日本語の注意文がある")
    if re.search(r"[✓✕✗]", b): NG(f"図解{i}：✓✕の記号の指示がある")
    if re.search(r"D\d{4}|問題\d|図解\d|画像\d", body.split("--- HEADER ---")[1] if "--- HEADER ---" in body else body): NG(f"図解{i}：画像に載る文言に、問題番号か図の番号がある")
for k, want in cfg.get("table_rows", {}).items():
    got = len(re.findall(r"^Data row \d+(?::| \()", blocks[int(k) - 1], re.M)); chk(got == want, f"図解{k}の表の行数 {got}", f"図解{k}の表の行数 {got}（期待 {want}）")
fl = cfg.get("flow")
if fl:
    b = blocks[fl["image"] - 1]
    chk(len(re.findall(r"^NODE DIAMOND \d", b, re.M)) == fl["diamonds"] and len(re.findall(r"^NODE RESULT \d", b, re.M)) == fl["results"],
        f"図解{fl['image']}：ダイヤ{fl['diamonds']}個・結果{fl['results']}個", f"図解{fl['image']}：ダイヤ・結果の数が違う")

# 4 4コマ
for n, (f, t) in enumerate(zip(cfg["fourkoma"], four), 1):
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
    chk(not bad, f"4コマ{n}：構成表の文言（全部）がプロンプト本体にある", f"4コマ{n}：構成表の文言がプロンプト本体にない: {bad[:3]}")
    if "Final check before rendering" not in body or "BACKGROUND REQUIREMENT" not in body: NG(f"4コマ{n}：Final checkか背景の不透明化の指示がない")
    if re.search(r"D\d{4}|問題[DＤ]", body): NG(f"4コマ{n}：画像に載る本文に、問題番号がある")
    if "## 見出し画像プロンプト" in t or "## note記事の冒頭文" in t: NG(f"4コマ{n}：単独記事用の節（見出し・冒頭文）が残っている")

# 5 見出し画像
for s in cfg["midashi_texts"]:
    if s not in mid: NG(f"見出し画像のプロンプトに「{s}」がない")
for s in cfg["midashi_texts"][:2]:
    if len(s) > 16: NG(f"見出し画像の行が16字を超える: {s}")
if "Arabic numeral 4;" in mid and cfg.get("midashi_digit_fix"): NG("見出し画像：4コマ用の数字の指示が残っている")

# 6 記事：表を使わない、個人の演習結果・問題番号が入っていない
if re.search(r"^\|", note, re.M): NG("記事にMarkdownの表がある（シリーズは表を使わない）")
for pat in (r"D\d{4}", r"第\d+問", r"[HR]\d{1,2}-Q", r"(平成|令和)\d+年度", r"一問一答", r"筆者", r"誤答", r"演習", r"\d+回のうち", r"復習"):
    mm = re.search(pat, note)
    if mm: NG(f"記事に、個人の演習結果・問題番号に関わる語がある: {mm.group(0)}")
for p_ in cfg["note_required"]:
    if p_ not in note: NG(f"記事に「{p_}」がない")
for para in note.split("\n"):
    if para and not para.startswith((">", "#", "-", "---", "|", "*", " ")) and len(para) > 125 and not para.startswith("**"):
        NG(f"記事に125字を超える段落がある: {para[:30]}…")

for m in ok: print("OK  ", m)
for m in ng: print("NG  ", m)
print(f"結果: NG {len(ng)}件 / OK {len(ok)}件")
sys.exit(1 if ng else 0)
