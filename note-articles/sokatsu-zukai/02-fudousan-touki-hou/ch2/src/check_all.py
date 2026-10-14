#!/usr/bin/env python3
"""総合記事②不動産登記法編 第2章の図解・4コマ・見出し画像プロンプトの機械チェック（標準ライブラリ＋リポジトリの check_prompt.py）。NG 0件が条件。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch2/src/check_all.py"""
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
else: OK("4コマ14本：生成元と一致、check_prompt.py NG 0件・WARN 0件")
n4 = len(list(D.glob("prompt_4koma_*.md")))
if n4 != 14: NG(f"4コマのファイルが14本でない（{n4}本）")

# 2. 個人の演習結果・問題番号が図解と見出し画像に入っていない（4コマは肢IDのタグと結論帯の問題番号だけ許可）
bad_words = ["誤答", "★", "のべ", "履歴", "回間違", "正答率"]
id_pat = re.compile(r"\bD\d{4}\b|[HR]\d{1,2}-Q\d+")
midashi = D / "prompt_midashi_sokatsu02_ch2.md"
for f in sorted(D.glob("prompt_infographic_*.md")) + [midashi]:
    t = f.read_text(encoding="utf8") if f == midashi else "\n".join(re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S))
    for w in bad_words:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
    if id_pat.search(t): NG(f"{f.name}: 問題番号らしい文字列「{id_pat.search(t).group(0)}」がある")
for f in sorted(D.glob("prompt_4koma_*.md")):
    t = f.read_text(encoding="utf8").replace("改訂履歴", "")
    for w in bad_words + ["誤解4回", "誤解3回", "誤解5回"]:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
OK("図解・見出し画像に個人の演習結果・問題番号なし／4コマに演習結果の語なし（上にNGがなければ）")

# 2b. 禁止語：樹形図の意味の「木」「ツリー」（図・台詞・ラベル・指示文のどこにも書かない）
tree = re.compile(r"決定木|判定木|ツリー|(?<![立竹樹植苗])木(?:では|に当て|の右|の左|の枝|の根|の分岐|の図|を描|で見|と呼)")
for f in sorted(D.glob("prompt_*.md")):
    m = tree.search(f.read_text(encoding="utf8"))
    if m: NG(f"{f.name}: 樹形図の意味の語「{m.group(0)}」がある")
OK("樹形図の意味の「木」「ツリー」なし")

# 3. 図解：表の行数・カード数の宣言とデータ行が合う／最終確認の漢字が本文にある／画像の中に図番がない／全21枚がそろう
total = 0
for f in sorted(D.glob("prompt_infographic_*.md")):
    t = f.read_text(encoding="utf8")
    for blk in re.findall(r"```text\n(.*?)\n```", t, flags=re.S):
        total += 1
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
        # 青・赤を使ってよいのは判定の流れ図（FLOWCHART）だけ
        if "--- FLOWCHART ---" not in body and not re.search(r"use no blue or red", body): NG(f"{f.name}: 流れ図でないのに、青・赤を使わない指示がない")
        if "--- FLOWCHART ---" in body and "BLUE" not in body: NG(f"{f.name}: 流れ図に はい＝青 の指示がない")
        if re.search(r"green|緑", body, re.I): NG(f"{f.name}: 緑への言及がある")
    n = len(re.findall(r"^```text", t, flags=re.M))
    OK(f"{f.name}: プロンプト {n} 本")
if total != 21: NG(f"図解のプロンプトが21本でない（{total}本）")

# 3b. 見出し画像：文言が独立した行で入り、漢字リストが一致、タイトル1行16字以内
mt = midashi.read_text(encoding="utf8")
rows = dict(re.findall(r"^- (タイトル1行目|タイトル2行目|サブタイトル)：(.+?)(?:（.*)?$", mt, flags=re.M))
if len(rows) != 3: NG("見出し画像の文言（正本）の3行が読めない")
else:
    t1, t2, sb = rows["タイトル1行目"], rows["タイトル2行目"], rows["サブタイトル"]
    blk = re.search(r"```text\n(.*?)```", mt, re.S).group(1)
    for t in (t1, t2, sb):
        if ("\n" + t + "\n") not in blk: NG(f"見出し画像プロンプトに文言が独立した行として入っていない: {t}")
    for t in (t1, t2):
        if len(t) > 16: NG(f"見出し画像のタイトルが16字を超える: {t}")
    km = re.search(r"special attention to the kanji ([^;]+);", blk)
    ks = set(re.findall(r"[一-鿿]", t1 + t2 + sb))
    if not km or set(re.findall(r"[一-鿿]", km.group(1))) != ks: NG("見出し画像のFinal checkの漢字リストが文言の漢字と一致しない")
    if "1280x670" not in blk or "fully opaque" not in blk: NG("見出し画像プロンプトに 1280x670／fully opaque がない")
    OK("見出し画像：文言・漢字リスト・サイズ")

# 4. 条文の確認：画像に載せた主な条文の語が、法令DBの原文にある
def read(n): return (LAWS / n).read_text(encoding="utf8")
rei, kis1, kis2, kis3 = read("fudousan-touki-rei.md"), read("fudousan-touki-kisoku-1.md"), read("fudousan-touki-kisoku-2.md"), read("fudousan-touki-kisoku-3.md")
hou, bessho, menkyo, junsoku = read("fudousan-touki-hou.md"), read("fudousan-touki-rei-betsuhyou.md"), read("touroku-menkyozei-hou.md"), read("fudousan-touki-jimu-junsoku.md")
must = {
    "令": (rei, ["申請人が法人であるときは、その代表者の氏名", "会社法人等番号", "作成後三月以内のものでなければならない", "電子署名が行われているものでなければならない",
                "登記官が定めた相当の期間内に、登記官に当該書面を提示しなければならない", "いずれか一筆の土地の所有権の登記名義人の登記識別情報", "登記名義人が同一である所有権の登記がある建物の合体による登記等",
                "登記事項証明書の提供に代えて、登記官が電気通信回線による登記情報の提供", "不動産識別事項", "所有権の登記がある土地の合筆の登記", "所有権の登記がある建物の合併の登記",
                "土地所在図、地積測量図、地役権図面、建物図面及び各階平面図"]),
    "規則1": (kis1, ["その作成後三月以内のものでなければならない", "同一の登記所に対して同時に二以上の申請をする場合", "申請の取下げは、登記完了後は、することができない", "決定書を作成して、これを申請人ごとに交付",
                    "申請書及びその添付書面を還付するものとする", "書面申請をした申請人は、申請に係る登記が完了するまでの間", "申請書の内容と同一の内容を記載した書面", "原本と相違ない旨を記載した謄本",
                    "調査完了後", "書留郵便又は信書便", "三十日以内に", "三月以内に登記識別情報を記載した書面を受領しない", "作成の年の翌年から五年間", "閉鎖した日から三十年間", "閉鎖した日から五十年間",
                    "永久（閉鎖したものにあっては、閉鎖した日から三十年間）", "登記識別情報の通知を受けるための特別の委任を受けた代理人", "失効の申出", "通知されていないこと又は失効していること",
                    "登記の申請の代理を業とすることができる者であることを証する情報", "登記識別情報の通知を希望しない旨の申出", "当該申請のためにのみ作成された委任状その他の書面",
                    "偽造された書面その他の不正な登記の申請のために用いられた疑いがある書面", "乙登記所に移送"]),
    "規則2": (kis2, ["被相続人の本籍地若しくは最後の住所地、申出人の住所地又は被相続人を表題部所有者若しくは所有権の登記名義人とする不動産の所在地", "再交付の申出をする場合", "請求書を登記所に提出する方法", "電子情報処理組織を使用して登記所に提供する方法",
                    "登記簿の附属書類の閲覧の請求をするとき", "何区何番事項証明書", "一棟建物現在事項証明書", "戸籍法（昭和二十二年法律第二百二十四号）第十条の二第三項に掲げる者"]),
    "規則3": (kis3, ["令附則第五条第一項の規定による書面の提出について", "申請書の添付書面」とあるのは、「当該書面」", "第三十八条第三項及び第三十九条第三項の規定は、令附則第五条第一項の規定により書面を提出する方法により添付情報を提供した場合について準用する"]),
    "法": (hou, ["申請人自らが登記名義人となる場合", "正当な理由があるときは", "区分建物が属する一棟の建物が新築された場合", "公証人"]),
    "別表": (bessho, ["他の登記所の管轄区域内にあるときは、当該土地の登記事項証明書", "共用部分である旨の登記", "当該権利に関する登記に係る権利の登記名義人", "地役権図面", "当該事由を証する情報"]),
    "登免税法": (menkyo, ["分筆又は分割若しくは区分後の不動産の個数", "合筆又は合併後の不動産の個数", "墳墓地に関する登記", "国又は別表第二に掲げる者がこれらの者以外の者に代位してする"]),
    "準則": (junsoku, ["発行後３月以内のものであることを要する", "職印に関する証明書"]),
}
for name, (text, words) in must.items():
    for w in words:
        if w not in text: NG(f"法令DB（{name}）に原文が見つからない：{w}")
OK("条文の語：法令DBの原文と照合（上にNGがなければ一致）")

print(f"\n結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
