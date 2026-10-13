#!/usr/bin/env python3
"""総合記事②不動産登記法編 第4章の図解・4コマ・見出し画像プロンプトの機械チェック（標準ライブラリ＋リポジトリの check_prompt.py）。NG 0件が条件。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch4/src/check_all.py"""
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
else: OK("4コマ8本：生成元と一致、check_prompt.py NG 0件・WARN 0件")

# 2. 個人の演習結果・問題番号が図解と見出し画像に入っていない（4コマは肢IDのタグと結論帯の問題番号だけ許可）
bad_words = ["誤答", "★", "のべ", "履歴", "回間違", "正答率"]
id_pat = re.compile(r"\bD\d{4}\b|[HR]\d{1,2}-Q\d+")
for f in sorted(D.glob("prompt_infographic_*.md")) + [D / "prompt_midashi_sokatsu02_ch4.md"]:
    t = "\n".join(re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S)) if f.name != "prompt_midashi_sokatsu02_ch4.md" else f.read_text(encoding="utf8")
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
law = (LAWS / "fudousan-touki-hou.md").read_text(encoding="utf8")
rule = (LAWS / "fudousan-touki-kisoku-1.md").read_text(encoding="utf8")
rei = (LAWS / "fudousan-touki-rei.md").read_text(encoding="utf8")
bet = (LAWS / "fudousan-touki-rei-betsuhyou.md").read_text(encoding="utf8")
must_law = [
    "分筆又は合筆の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができない",   # 法39条1項
    "その変更があった日から一月以内に、当該地目又は地積に関する変更の登記を申請しなければならない",   # 法37条1項
    "表題部所有者又は所有権の登記名義人以外の者は、申請することができない",                         # 法38条
    "相互に接続していない土地の合筆の登記", "地目又は地番区域が相互に異なる土地の合筆の登記",
    "表題部所有者又は所有権の登記名義人が相互に異なる土地の合筆の登記", "表題部所有者又は所有権の登記名義人が相互に持分を異にする土地の合筆の登記",
    "所有権の登記がない土地と所有権の登記がある土地との合筆の登記", "所有権の登記以外の権利に関する登記がある土地",   # 法41条1〜6号
    "抹消された登記（権利に関する登記に限る。）の回復",                                               # 法72条
]
for w in must_law:
    if w not in law: NG(f"法令DB（fudousan-touki-hou.md）に原文が見つからない：{w}")
must_rule = [
    "一平方メートルの百分の一（宅地及び鉱泉地以外の土地で十平方メートルを超えるものについては、一平方メートル）未満の端数は、切り捨てる",   # 規則100条
    "分筆後の甲土地の登記記録の当該権利に関する登記についてする付記登記によって乙土地について当該権利が消滅した旨を記録しなければならない",   # 規則104条2項
    "分筆後の甲土地について権利が消滅した旨の登記をするときは", "当該権利に関する登記を抹消する記号を記録しなければならない",              # 規則104条3項
    "前号の権利を目的とする第三者の権利に関する登記があるときは", "当該第三者が承諾したことを証する当該第三者が作成した情報",                    # 規則104条1項2号
    "要役地についてする地役権の登記がある土地について分筆の登記をする場合において", "地役権者が作成した情報",                              # 規則104条6項
    "承役地についてする地役権の登記", "登記の目的、申請の受付の年月日及び受付番号並びに登記原因及びその日付が同一のもの",
    "信託の登記であって、法第九十七条第一項各号に掲げる登記事項が同一のもの", "鉱害賠償登録令（昭和三十年政令第二十七号）第二十六条に規定する鉱害賠償登録に関する登記であって",   # 規則105条
    "登記識別情報の通知を受けるための特別の委任を受けた代理人がある場合には",                                                         # 規則62条2項
    "分筆後の甲土地について従前の地番と同一の地番を付すことができる",
]
for w in must_rule:
    if w not in rule: NG(f"法令DB（fudousan-touki-kisoku-1.md）に原文が見つからない：{w}")
if "同一の不動産について申請する二以上の登記が、不動産の表題部の登記事項に関する変更の登記又は更正の登記及び土地の分筆の登記若しくは合筆の登記" not in rule: NG("規則35条7号が fudousan-touki-kisoku-1.md に見つからない")
if "所有権の登記がある土地の合筆の登記" not in rei or "当該合筆に係る土地のうちいずれか一筆の土地の所有権の登記名義人の登記識別情報" not in rei: NG("令8条（合筆の登記識別情報）が fudousan-touki-rei.md に見つからない")
if "同意又は承諾を証する情報を記載した書面には" not in rei or "記名押印した者の印鑑に関する証明書" not in rei: NG("令19条が fudousan-touki-rei.md に見つからない")
if rei.count("作成後三月以内") < 2: NG("令16条3項・18条3項（作成後三月以内）が fudousan-touki-rei.md に見つからない")
if "同条ただし書の規定により登記識別情報を提供することができないとき" not in rei: NG("令3条12号が fudousan-touki-rei.md に見つからない")
for w in ["分筆後の土地の地積測量図", "当該地役権設定の範囲を証する地役権者が作成した情報", "区分所有法第二十二条第一項ただし書の規約における別段の定めがあること"]:
    if w not in bet: NG(f"令別表（fudousan-touki-rei-betsuhyou.md）に原文が見つからない：{w}")
OK("条文の語：法令DBの原文と照合（上にNGがなければ一致）")

# 5. 禁止語：樹形図の意味の「決定木」「判定木」「ツリー」「木に当てはめる」「木では」を、図解・4コマ・見出し画像のどこにも書いていない
tree = ["決定木", "判定木", "ツリー", "木に当てはめ", "木では", "木の右"]
for f in sorted(D.glob("prompt_*.md")):
    t = f.read_text(encoding="utf8")
    for w in tree:
        if w in t: NG(f"{f.name}: 禁止語「{w}」がある")
OK("禁止語（決定木・判定木・ツリー など）なし（上にNGがなければ）")

# 6. 図解の配色：判定の流れ図以外は青・赤を使わない指示（NOCOLOR）が入っている／流れ図は COLOR RULE が入っている
for f in sorted(D.glob("prompt_infographic_*.md")):
    t = f.read_text(encoding="utf8")
    for blk in re.findall(r"```text\n(.*?)\n```", t, flags=re.S):
        flow = "--- FLOWCHART ---" in blk
        if flow and "COLOR RULE" not in blk: NG(f"{f.name}: 流れ図に COLOR RULE がない")
        if not flow and "use no blue or red anywhere" not in blk and "no blue or red" not in blk: NG(f"{f.name}: 分類中心の図に『青・赤を使わない』指示がない")
OK("図解の配色指示（流れ図のみ青・赤）")

# 7. 成果物の数：図解14枚・4コマ8本・見出し1枚
n_img = sum(len(re.findall(r"^```text", f.read_text(encoding="utf8"), flags=re.M)) for f in D.glob("prompt_infographic_*.md"))
n_4k = len(list(D.glob("prompt_4koma_*.md")))
n_mid = len(list(D.glob("prompt_midashi_*.md")))
if (n_img, n_4k, n_mid) != (14, 8, 1): NG(f"成果物の数が想定と違う：図解{n_img}・4コマ{n_4k}・見出し{n_mid}")
else: OK("成果物：図解14枚・4コマ8本・見出し1枚")

print(f"\n結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
