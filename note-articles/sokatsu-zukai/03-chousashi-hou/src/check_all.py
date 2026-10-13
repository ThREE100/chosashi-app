#!/usr/bin/env python3
"""総合記事③ 土地家屋調査士法編の図解・4コマ・見出し画像プロンプトの機械チェック（標準ライブラリ＋リポジトリの check_prompt.py）。NG 0件が条件。
使い方: python3 note-articles/sokatsu-zukai/03-chousashi-hou/src/check_all.py"""
import re, sys, subprocess, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
D = HERE.parent
LAWS = ROOT / "note-articles" / "laws"
ng = []
def NG(msg): ng.append(msg); print("NG  ", msg)
def OK(msg): print("OK  ", msg)

# 1. 4コマ：設計データから作り直した内容とファイルが一致し、check_prompt.py が NG 0件・WARN 0件
r = subprocess.run([sys.executable, str(HERE / "build_4koma.py"), "--verify-sync"], capture_output=True, text=True)
if r.returncode != 0: NG("4コマの機械チェック／同期が NG：\n" + r.stdout)
else: OK("4コマ5本：生成元と一致、check_prompt.py NG 0件・WARN 0件")

# 2. 個人の演習結果・問題番号が図解と見出し画像に入っていない（4コマは肢IDのタグと結論帯の問題番号だけ許可）
bad_words = ["誤答", "★", "のべ", "履歴", "回間違", "正答率"]
id_pat = re.compile(r"\bD\d{4}\b|[HR]\d{1,2}-Q\d+")
for f in sorted(D.glob("prompt_infographic_*.md")) + [D / "prompt_midashi_sokatsu03.md"]:
    t = "\n".join(re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S)) if f.name != "prompt_midashi_sokatsu03.md" else f.read_text(encoding="utf8")
    for w in bad_words:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
    if id_pat.search(t): NG(f"{f.name}: 問題番号らしい文字列「{id_pat.search(t).group(0)}」がある")
for f in sorted(D.glob("prompt_4koma_*.md")):
    t = f.read_text(encoding="utf8").replace("改訂履歴", "")
    for w in bad_words + ["誤解4回", "誤解3回", "誤解5回"]:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
OK("図解・見出し画像に個人の演習結果・問題番号なし／4コマに演習結果の語なし（上にNGがなければ）")

# 3. 図解：表の行数・カード数の宣言とデータ行が合う／最終確認の漢字が本文にある／画像の中に図番がない
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
    n = len(re.findall(r"^```text", t, flags=re.M))
    OK(f"{f.name}: プロンプト {n} 本")

# 4. 条文の確認：画像に載せた主な条文の語が、法令DBの原文にある
law = (LAWS / "chousashi-hou.md").read_text(encoding="utf8")
rule = (LAWS / "chousashi-hou-sekourule.md").read_text(encoding="utf8")
must_law = ["二年以内の業務の停止", "二年以内の業務の全部又は一部の停止", "聴聞の期日の一週間前までにしなければならない", "公開により行わなければならない",
            "変更の日から二週間以内に", "成立の日から二週間以内に", "解散の日から二週間以内に", "主たる事務所の所在地の調査士会及び調査士会連合会",
            "上級行政庁とみなす", "引き続き二年以上業務を行わないとき", "心身の故障により業務を行うことができないとき", "その業務を廃止したとき",
            "ただし、第三号及び第七号に掲げる事件については", "第一条、第二条、第二十条から第二十二条まで及び第二十四条の規定は、調査士法人について準用する",
            "前条第一号及び第七号から第十一号までに掲げる事項に係る会則の変更については、この限りでない",
            "入会及び退会に関する規定（入会金その他の入会についての特別の負担に関するものを含む。）", "司法書士法（昭和二十五年法律第百九十七号）第四十七条の規定により業務の禁止の処分を受け、その処分の日から三年を経過しない者"]
for w in must_law:
    if w not in law: NG(f"法令DB（chousashi-hou.md）に原文が見つからない：{w}")
if "聴聞" not in rule or "第三十五条の八" not in rule and "35条の8" not in rule: NG("施行規則35条の8が chousashi-hou-sekourule.md に見つからない")
OK("条文の語：法令DBの原文と照合（上にNGがなければ一致）")

print(f"\n結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
