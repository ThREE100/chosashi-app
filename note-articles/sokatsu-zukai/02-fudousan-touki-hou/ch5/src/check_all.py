#!/usr/bin/env python3
"""総合記事②不動産登記法編 第5章の図解・4コマ・見出し画像プロンプトの機械チェック（標準ライブラリ＋リポジトリの check_prompt.py）。NG 0件が条件。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch5/src/check_all.py"""
import re, sys, subprocess, pathlib, unicodedata
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

# 1b. 図解・見出し画像も、生成元から作り直した内容とファイルが一致する（手で直していない）
import importlib.util
for modname, fn in (("gen_infographic", None), ):
    spec = importlib.util.spec_from_file_location(modname, HERE / "gen_infographic.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for key in m.FILES:
        fname, doc = m.build_doc(key)
        if (D / fname).read_text(encoding="utf8") != doc: NG(f"{fname}: gen_infographic.py から作り直した内容と違う（手で直した、または再生成していない）")
OK("図解14ファイル：生成元と一致（上にNGがなければ）")

# 2. 個人の演習結果・問題番号が図解と見出し画像に入っていない（4コマは肢IDのタグと結論帯の問題番号だけ許可）
bad_words = ["誤答", "★", "のべ", "履歴", "回間違", "正答率"]
id_pat = re.compile(r"\bD\d{4}\b|[HR]\d{1,2}-Q\d+")
MID = D / "prompt_midashi_sokatsu02_ch5.md"
for f in sorted(D.glob("prompt_infographic_*.md")) + [MID]:
    t = "\n".join(re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S))
    for w in bad_words:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
    if id_pat.search(t): NG(f"{f.name}: 問題番号らしい文字列「{id_pat.search(t).group(0)}」がある")
for f in sorted(D.glob("prompt_4koma_*.md")):
    t = f.read_text(encoding="utf8").replace("改訂履歴", "")
    for w in bad_words + ["誤解4回", "誤解3回", "誤解5回"]:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
OK("図解・見出し画像に個人の演習結果・問題番号なし／4コマに演習結果の語なし（上にNGがなければ）")

# 2b. 禁止語（樹形図の意味の「木」「ツリー」）。実在の樹木は対象外
TREE = re.compile(r"決定木|判定木|ツリー|(?<![立竹樹植苗])木(?:では|に当て|の右|の左|の枝|の根|の分岐|の図|を描|で見|と呼)")
for f in sorted(D.glob("prompt_*.md")):
    for mm in TREE.finditer(f.read_text(encoding="utf8")): NG(f"{f.name}: 禁止語「{mm.group(0)}」がある")
OK("禁止語（決定木・判定木・ツリー）なし（上にNGがなければ）")

# 3. 図解：表の行数・列数・カード数の宣言とデータ行が合う／最終確認の漢字が本文にある／画像の中に図番がない／入れ子の「」がない
for f in sorted(D.glob("prompt_infographic_*.md")):
    t = f.read_text(encoding="utf8")
    for blk in re.findall(r"```text\n(.*?)\n```", t, flags=re.S):
        body = blk.split("--- FOOTER ---")[0]
        m = re.search(r"Exactly (\d+) columns and exactly (\d+) data rows", body)
        if m:
            ncol, nrow = int(m.group(1)), int(m.group(2))
            rows = re.findall(r"^Row \d+: (.*)$", body, flags=re.M)
            if len(rows) != nrow: NG(f"{f.name}: 表の行数の宣言 {nrow} とデータ行 {len(rows)} が違う")
            for rw in rows:
                cells = re.findall(r"「[^」]*」", rw)
                if len(cells) != ncol or " | ".join(cells) != rw: NG(f"{f.name}: 表の行の列数が違う（または「」が入れ子）: {rw[:50]}")
            hdr = re.search(r"Header row \(dark navy cells with white text\): (.*)\.$", body, flags=re.M)
            if hdr and len(re.findall(r"「[^」]*」", hdr.group(1))) != ncol: NG(f"{f.name}: 見出し行の列数が違う")
        m = re.search(r"paying special attention to the kanji ([^;]+);", blk)
        if m:
            for k in re.findall(r"[一-鿿]", m.group(1)):
                if k not in body: NG(f"{f.name}: 最終確認の漢字「{k}」が本文にない")
        h = body.split("--- HEADER ---")[1] if "--- HEADER ---" in body else body
        if re.search(r"図\s*\d|Figure", h): NG(f"{f.name}: 画像の中に図番らしい文字がある")
        for ln in body.splitlines():
            if re.search(r"「[^」]*「", ln): NG(f"{f.name}: 「」が入れ子になっている行がある: {ln[:60]}")
        m = re.search(r"Confirm the number of cards equals (\d+) exactly", blk)
        if m and len(re.findall(r"^--- CARD \d+ ---", body, flags=re.M)) != int(m.group(1)): NG(f"{f.name}: カード数の宣言とカードの数が違う")
        if "FLOWCHART" in body:
            if "「はい」" not in body or "「いいえ」" not in body: NG(f"{f.name}: 判定の流れ図に「はい」「いいえ」のラベルがない")
            nd = len(re.findall(r"^NODE DIAMOND", body, flags=re.M)); mm = re.search(r"Counts: .*?(\d+) diamonds?", body)
            if mm and nd != int(mm.group(1)): NG(f"{f.name}: ダイヤモンドの数の宣言 {mm.group(1)} と実際 {nd} が違う")
            nr = len(re.findall(r"^NODE RESULT", body, flags=re.M)); mm = re.search(r"Counts: .*?(\d+) result boxes", body)
            if mm and nr != int(mm.group(1)): NG(f"{f.name}: 結果の箱の数の宣言 {mm.group(1)} と実際 {nr} が違う")
        else:
            if "COLOR RULE" in blk: NG(f"{f.name}: 判定の流れ図でない図に、はい／いいえの配色規則が入っている")
    n = len(re.findall(r"^```text", t, flags=re.M))
    OK(f"{f.name}: プロンプト {n} 本")

# 4. 条文の確認：画像に載せた主な条文の語が、法令DBの原文にある（全角数字・空白をそろえて照合）
def norm(s): return re.sub(r"[\s　]+", "", unicodedata.normalize("NFKC", s))
def rd(n): return norm((LAWS / n).read_text(encoding="utf8"))
hou, rei, bet = rd("fudousan-touki-hou.md"), rd("fudousan-touki-rei.md"), rd("fudousan-touki-rei-betsuhyou.md")
kis = rd("fudousan-touki-kisoku-1.md"); jun = rd("fudousan-touki-jimu-junsoku.md"); min1 = rd("minpou-1-soukyoku-bukken.md"); min2 = rd("minpou-2-saiken.md")
checks = {
  "法2条5号": (hou, "一筆の土地又は一個の建物ごとに"), "法12条": (hou, "登記記録は、表題部及び権利部に区分して作成する"),
  "法2条6号": (hou, "この法律の規定により登記記録として登記すべき事項をいう"),
  "法2条23号": (hou, "表題登記がある建物に附属する建物であって、当該表題登記がある建物と一体のものとして一個の建物として登記されるもの"),
  "法44条1項3号": (hou, "三建物の種類、構造及び床面積"), "法44条1項7号": (hou, "当該建物又は附属建物が属する一棟の建物の構造及び床面積"),
  "法44条1項8号": (hou, "当該建物又は附属建物が属する一棟の建物の名称があるときは、その名称"),
  "法44条1項5号": (hou, "区分建物である附属建物にあっては、当該附属建物が属する一棟の建物の所在する市、区、郡、町、村、字及び土地の地番）並びに種類、構造及び床面積"),
  "法45条": (hou, "一個の建物ごとに家屋番号を付さなければならない"),
  "法47条": (hou, "新築した建物又は区分建物以外の表題登記がない建物の所有権を取得した者"),
  "法48条3項": (hou, "表題登記がある建物（区分建物を除く。）に接続して区分建物が新築された場合"),
  "法51条1項": (hou, "当該変更があった日から一月以内に、当該登記事項に関する変更の登記を申請しなければならない"),
  "法54条1項": (hou, "表題部所有者又は所有権の登記名義人以外の者は、申請することができない"),
  "法55条4項": (hou, "特定登記がある建物の滅失の登記について準用する"),
  "法56条5号": (hou, "所有権等の登記以外の権利に関する登記がある建物"),
  "法57条": (hou, "その滅失の日から一月以内に、当該建物の滅失の登記を申請しなければならない"),
  "法58条4項": (hou, "職権で、当該建物について表題部所有者の登記又は権利に関する登記を抹消しなければならない"),
  "令3条8号ロ": (rei, "ロ家屋番号"), "令4条ただし書": (rei, "同一の登記所の管轄区域内にある二以上の不動産について申請する登記の目的並びに登記原因及びその日付が同一であるとき"),
  "令6条2項4号": (rei, "別表の十九の項申請情報欄イに掲げる当該建物の所在する市、区、郡、町、村、字及び土地の地番並びに当該建物の家屋番号"),
  "令別表14項イ": (bet, "建物の所在する市、区、郡、町、村、字及び土地の地番を変更し、又は更正するときは、変更後又は更正後の建物図面"),
  "令別表14項ロ": (bet, "床面積を変更し、又は更正するときは"), "令別表14項ハ": (bet, "附属建物を新築したときは、変更後の建物図面及び各階平面図並びに附属建物について表題部所有者又は所有権の登記名義人が所有権を有することを証する情報"),
  "令別表16項イ": (bet, "当該分割後、区分後又は合併後の建物図面及び各階平面図"), "令別表16項ロ": (bet, "建物の分割の登記又は建物の区分の登記を申請するときは、当該建物の所有者を証する情報"),
  "令別表17項": (bet, "共用部分である旨の登記又は団地共用部分である旨の登記がある建物の滅失の登記"), "令別表19項": (bet, "団地共用部分である旨の登記"),
  "令別表21項": (bet, "共用部分である旨又は団地共用部分である旨を定めた規約を廃止したことを証する情報"),
  "規則28条9号": (kis, "表示に関する登記の申請情報及びその添付情報"), "規則28条13号": (kis, "永久（閉鎖したものにあっては、閉鎖した日から三十年間）"),
  "規則35条7号": (kis, "不動産の表題部の登記事項に関する変更の登記又は更正の登記及び土地の分筆の登記若しくは合筆の登記又は建物の分割の登記、建物の区"),
  "規則73条2項": (kis, "作成の年月日並びに申請人及び作成者の氏名又は名称を記録しなければならない"),
  "規則113条": (kis, "建物の主な用途が二以上の場合には、当該二以上の用途により建物の種類を定める"),
  "規則114条": (kis, "建物の主な部分の構成材料、屋根の種類及び階数により"),
  "規則115条": (kis, "壁その他の区画の中心線（区分建物にあっては、壁その他の区画の内側線）で囲まれた部分の水平投影面積により"),
  "規則115条端数": (kis, "一平方メートルの百分の一未満の端数は、切り捨てるものとする"),
  "準則78条1項": (jun, "効用上一体として利用される状態にある数棟の建物は、所有者の意思に反しない限り、1個の建物として取り扱うものとする"),
  "準則78条2項": (jun, "一棟の建物の全部又は隣接する数個の部分を1個の建物として取り扱うものとする"),
  "準則82条1号": (jun, "天井の高さ1.5メートル未満の地階及び屋階（特殊階）は、床面積に算入しない。ただし、1室の一部が天井の高さ1.5メートル未満であっても、その部分は、当該1室の面積に算入する"),
  "準則82条3号": (jun, "観覧席は、屋根の設備のある部分の面積を床面積として計算する"),
  "準則83条": (jun, "既存の建物が滅失し、新たな建物が建築されたものとして取り扱うものとする"),
  "準則88条2項": (jun, "床面積の多い部分又は主たる建物の所在する土地の地番を先に記録し、他の土地の地番は後に記録する"),
  "準則89条": (jun, "その一棟の建物の所在する市、区、郡、町、村、字及び土地の地番並びに構造及び床面積を記録することを要しない"),
  "準則91条": (jun, "地階があるときは、その床面積は、地上階の床面積の記録の次に記録する"), "準則91条2": (jun, "平方メートル未満の表示として、「00」と記録する"),
  "準則91条3": (jun, "各階の床面積の合計を記録することを要しない"),
  "準則94条1項": (jun, "変更後又は更正後の種類、構造及び床面積の全部を記録し、従前の登記事項（符号を除く。）の全部を抹消する"),
  "民法242条": (min1, "不動産の所有者は、その不動産に従として付合した物の所有権を取得する"), "民法252条5項": (min1, "各共有者は、前各項の規定にかかわらず、保存行為をすることができる"),
  "民法423条": (min2, "債権者は、自己の債権を保全するため必要があるときは、債務者に属する権利"),
}
for k, (src, w) in checks.items():
    if norm(w) not in src: NG(f"法令DBに原文が見つからない（{k}）：{w}")
OK(f"条文の語：法令DB（法・令・令別表・規則・準則・民法）の原文と照合 {len(checks)} 項目（上にNGがなければ一致）")

# 5. 記事の用語：画像の用語が記事の用語（主である建物）と一致する（準則の「主たる建物」を画像に使っていない）
art = (ROOT / "note-articles" / "column" / "sokatsu-02-fudousan-touki-hou-ch5.md").read_text(encoding="utf8")
for f in sorted(D.glob("prompt_infographic_*.md")):
    for blk in re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S):
        if "主たる建物" in blk.split("--- FOOTER ---")[0]: NG(f"{f.name}: 画像の中の用語が記事（主である建物）と違う「主たる建物」")
OK("画像の用語：記事の用語（主である建物）にそろえた")

print(f"\n結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
