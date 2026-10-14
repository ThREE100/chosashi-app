#!/usr/bin/env python3
"""総合記事②不動産登記法編 第1章の図解・4コマ・見出し画像プロンプトの機械チェック（標準ライブラリ＋リポジトリの check_prompt.py）。NG 0件が条件。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch1/src/check_all.py"""
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
else: OK("4コマ13本：生成元と一致、check_prompt.py NG 0件・WARN 0件")

# 2. 個人の演習結果・問題番号が図解と見出し画像に入っていない（4コマは肢IDのタグと結論帯の問題番号だけ許可）
bad_words = ["誤答", "★", "のべ", "履歴", "回間違", "正答率"]
id_pat = re.compile(r"\bD\d{4}\b|[HR]\d{1,2}-Q\d+")
for f in sorted(D.glob("prompt_infographic_*.md")) + [D / "prompt_midashi_sokatsu02_ch1.md"]:
    t = "\n".join(re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S)) if f.name != "prompt_midashi_sokatsu02_ch1.md" else f.read_text(encoding="utf8")
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
def rd(name): return (LAWS / name).read_text(encoding="utf8")
checks = {
    "fudousan-touki-hou.md": [
        "表題部所有者又はその持分についての変更は、当該不動産について所有権の保存の登記をした後において、その所有権の移転の登記の手続をするのでなければ、登記することができない",
        "表題部所有者の氏名若しくは名称又は住所についての変更の登記又は更正の登記は、表題部所有者以外の者は、申請することができない",
        "当該不動産の所有者以外の者は、申請することができない",
        "不動産の表題部所有者である共有者の持分についての更正の登記は、当該共有者以外の者は、申請することができない",
        "当該更正の登記によってその持分を更正することとなる他の共有者の承諾があるときでなければ、申請することができない",
        "表題登記がある建物（区分建物を除く。）に接続して区分建物が新築された場合における当該区分建物についての表題登記の申請は、当該表題登記がある建物についての表題部の変更の登記の申請と併せてしなければならない",
        "当該区分建物の所有者は、他の区分建物の所有者に代わって、当該他の区分建物についての表題登記を申請することができる",
        "当該表題登記がある建物の表題部所有者又は所有権の登記名義人は、当該新築に係る区分建物の所有者に代わって、当該新築に係る区分建物についての表題登記を申請することができる",
        "相続人その他の一般承継人も、被承継人を表題部所有者とする当該建物についての表題登記を申請することができる",
        "分筆又は合筆の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができない",
        "新たに生じた土地又は表題登記がない土地の所有権を取得した者は、その所有権の取得の日から一月以内に、表題登記を申請しなければならない",
        "申請人となるべき者以外の者が申請していると疑うに足りる相当な理由があると認めるときは、次条の規定により当該申請を却下すべき場合を除き",
        "表示に関する登記は、登記官が、職権ですることができる",
        "十万円以下の過料に処する",
        "所有権の保存の登記は、次に掲げる者以外の者は、申請することができない",
    ],
    "fudousan-touki-rei.md": [
        "申請人が法人であるときは、その代表者の氏名",
        "申請人の氏名又は名称及び住所",
        "申請人又はその代表者若しくは代理人は、法務省令で定める場合を除き、申請情報を記載した書面に記名押印しなければならない",
        "登記の目的並びに登記原因及びその日付が同一であるときその他法務省令で定めるとき",
        "申請人又はその代表者若しくは代理人が作成したもの並びに土地所在図、地積測量図、地役権図面、建物図面及び各階平面図を除く",
    ],
    "fudousan-touki-kisoku-1.md": [
        "不動産の表題部の登記事項に関する変更の登記又は更正の登記及び土地の分筆の登記若しくは合筆の登記又は建物の分割の登記、建物の区分の登記若しくは建物の合併の登記であるとき",
        "土地の一部を分筆して、これを他の土地に合筆しようとする場合において、分筆の登記及び合筆の登記の申請をするとき",
        "合筆の登記、合体による登記等又は建物の合併の登記",
        "委任による代理人が申請書に署名した場合",
    ],
    "fudousan-touki-kisoku-2.md": [
        "表題部所有者（表題部所有者の更正の登記又は表題部所有者である共有者の持分の更正の登記にあっては、更正前の表題部所有者）又は所有権の登記名義人",
        "その一人に対し通知すれば足りる",
    ],
    "fudousan-touki-rei-betsuhyou.md": [
        "当該表題部所有者となる者が所有権を有することを証する情報",
        "持分を更正することとなる他の共有者の承諾を証する当該他の共有者が作成した情報又は当該他の共有者に対抗することができる裁判があったことを証する情報",
        "床面積が増加した部分について表題部所有者又は所有権の登記名義人が所有権を有することを証する情報",
    ],
    "fudousan-touki-jimu-junsoku.md": [
        "不正登記防止申出は、登記名義人若しくはその相続人その他の一般承継人又はその代表者若しくは代理人（委任による代理人を除く。）が登記所に出頭してしなければならない",
        "直ちに職権でその登記をすることなく",
    ],
    "minpou-1-soukyoku-bukken.md": ["各共有者は、前各項の規定にかかわらず、保存行為をすることができる"],
}
for fn, phrases in checks.items():
    t = rd(fn)
    for w in phrases:
        if w not in t: NG(f"法令DB（{fn}）に原文が見つからない：{w[:48]}…")
OK("条文の語：法令DBの原文と照合（上にNGがなければ一致）")

print(f"\n結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
