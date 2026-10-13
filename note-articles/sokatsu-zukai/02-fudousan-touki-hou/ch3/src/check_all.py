#!/usr/bin/env python3
"""総合記事②不動産登記法編 第3章の図解・4コマ・見出し画像プロンプトの機械チェック（標準ライブラリ＋リポジトリの check_prompt.py）。NG 0件が条件。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch3/src/check_all.py"""
import re, sys, subprocess, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
D = HERE.parent
LAWS = ROOT / "note-articles" / "laws"
ARTICLE = ROOT / "note-articles" / "column" / "sokatsu-02-fudousan-touki-hou-ch3.md"
MIDASHI = D / "prompt_midashi_sokatsu02_ch3.md"
ng = []
def NG(msg): ng.append(msg); print("NG  ", msg)
def OK(msg): print("OK  ", msg)

# 1. 4コマ：設計データから作り直した内容とファイルが一致し、check_prompt.py が NG 0件・WARN 0件
r = subprocess.run([sys.executable, str(HERE / "build_4koma.py"), "--verify-sync"], capture_output=True, text=True)
if r.returncode != 0: NG("4コマの機械チェック／同期が NG：\n" + r.stdout)
else: OK("4コマ6本：生成元と一致、check_prompt.py NG 0件・WARN 0件")

# 2. 図解の生成元との同期（gen_infographic.py から作り直した内容とファイルが一致）
sys.path.insert(0, str(HERE))
import importlib.util
sp = importlib.util.spec_from_file_location("gen_infographic", HERE / "gen_infographic.py"); gi = importlib.util.module_from_spec(sp); sp.loader.exec_module(gi)
for key in gi.FILES:
    fname, doc = gi.build_doc(key)
    f = D / fname
    if not f.exists() or f.read_text(encoding="utf8") != doc: NG(f"{fname}: gen_infographic.py から作り直した内容と違う（再生成する）")
OK("図解13ファイル：生成元と一致（上にNGがなければ）")

# 3. 個人の演習結果・問題番号が図解と見出し画像に入っていない（4コマは肢IDのタグと結論帯の問題番号だけ許可）
bad_words = ["誤答", "★", "のべ", "履歴", "回間違", "正答率"]
id_pat = re.compile(r"\bD\d{4}\b|[HR]\d{1,2}-Q\d+")
for f in sorted(D.glob("prompt_infographic_*.md")) + [MIDASHI]:
    t = "\n".join(re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S))
    for w in bad_words:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
    if id_pat.search(t): NG(f"{f.name}: 問題番号らしい文字列「{id_pat.search(t).group(0)}」がある")
for f in sorted(D.glob("prompt_4koma_*.md")):
    t = f.read_text(encoding="utf8").replace("改訂履歴", "")
    for w in bad_words + ["誤解4回", "誤解3回", "誤解5回"]:
        if w in t: NG(f"{f.name}: 個人の演習結果らしい語「{w}」がある")
OK("図解・見出し画像に個人の演習結果・問題番号なし／4コマに演習結果の語なし（上にNGがなければ）")

# 4. 禁止語（樹形図の意味の「木」「ツリー」）が全プロンプトにない
TREE = re.compile(r"決定木|判定木|ツリー|(?<![立竹樹植苗])木(?:では|に当て|の右|の左|の枝|の根|の分岐|の図|を描|で見|と呼)")
for f in sorted(D.glob("prompt_*.md")):
    m = TREE.search(f.read_text(encoding="utf8"))
    if m: NG(f"{f.name}: 禁止語「{m.group(0)}」がある（『判定の流れ図』『流れ図』『分かれ道』と書く）")
OK("禁止語（決定木・判定木・ツリー など）なし（上にNGがなければ）")

# 5. 図解：表の行数・カード数の宣言とデータ行が合う／最終確認の漢字が本文にある／画像の中に図番がない／画像の文言に簡体字らしい字がない
SIMPL = set("这个们说话时门问间书车见观电发动长东风鸟马鱼关闭陆务经济纪组织资领导师县")   # 日本の常用漢字と同形の「体」「区」などは除く
for f in sorted(D.glob("prompt_infographic_*.md")):
    t = f.read_text(encoding="utf8")
    for blk in re.findall(r"```text\n(.*?)\n```", t, flags=re.S):
        body = blk.split("--- FOOTER ---")[0]
        m = re.search(r"exactly (\d+) data rows", body)
        if m:
            rows = len(re.findall(r"^Row \d+:", body, flags=re.M))
            if rows != int(m.group(1)): NG(f"{f.name}: 表の行数の宣言 {m.group(1)} とデータ行 {rows} が違う")
            cols = re.search(r"Exactly (\d+) columns", body)
            hdr = re.search(r"^Header row \(dark navy cells with white text\): (.+)\.$", body, flags=re.M)
            if cols and hdr:
                nh = len(re.findall(r"「", hdr.group(1)))
                if nh != int(cols.group(1)): NG(f"{f.name}: 列数の宣言 {cols.group(1)} と見出しの数 {nh} が違う")
            for rm in re.finditer(r"^Row \d+: (.+)$", body, flags=re.M):
                cells = rm.group(1).split(" | ")
                if cols and len(cells) != int(cols.group(1)): NG(f"{f.name}: データ行のセル数が列数と違う: {rm.group(0)[:50]}")
        m = re.search(r"paying special attention to the kanji ([^;]+);", blk)
        if m:
            for k in re.findall(r"[一-鿿]", m.group(1)):
                if k not in body: NG(f"{f.name}: 最終確認の漢字「{k}」が本文にない")
        if re.search(r"図\s*\d|Figure", body.split("--- HEADER ---")[1] if "--- HEADER ---" in body else body):
            NG(f"{f.name}: 画像の中に図番らしい文字がある")
        jp = "".join(re.findall(r"「([^」]+)」", body))
        bad = SIMPL & set(jp)
        if bad: NG(f"{f.name}: 画像の文言に簡体字らしい字 {sorted(bad)}")
        if "決定" in jp and "木" in jp: NG(f"{f.name}: 禁止語の疑い")
        # 流れ図以外の図解に、青・赤・チェック・バツを使う指示がない（NOCOLORが入っている）
        if "COLOR RULE" not in body and "use no blue or red anywhere" not in body: NG(f"{f.name}: 配色の規則（COLOR RULE か NOCOLOR）がない")
    n = len(re.findall(r"^```text", t, flags=re.M))
    OK(f"{f.name}: プロンプト {n} 本")


# 5b. 図解の画像に入る文字列（「」の中）は、かな・漢字・数字と、許可した記号（（）・：／、。？〜）だけ
ALLOWED = re.compile(r"^[ぁ-んァ-ヶー々一-鿿0-9（）・：／、。？〜 ]+$")
for f in sorted(D.glob("prompt_infographic_*.md")) + [MIDASHI]:
    for blk in re.findall(r"```text\n(.*?)\n```", f.read_text(encoding="utf8"), flags=re.S):
        body = blk.split("--- FOOTER ---")[0].split("Final check before rendering")[0]
        body = re.sub(r"CRITICAL TEXT REQUIREMENT:.*", "", body)
        for s in re.findall(r"「([^」]+)」", body):
            if not ALLOWED.match(s) and not re.fullmatch(r"[A-Za-z0-9 ,.]+", s): NG(f"{f.name}: 画像の文字列に許可外の記号がある: 「{s}」")
OK("図解の文字列：許可した文字だけ（上にNGがなければ）")

# 6. 論点との対応：論点PC-1〜PC-12の全部に図解が1枚以上ある／記事に論点の見出しがある／4コマの肢が記事の同じ論点の肢にある
art = ARTICLE.read_text(encoding="utf8")
secs = {}
for m in re.finditer(r"^### 【(PC-\d+)】.*?(?=^### |\Z)", art, flags=re.M | re.S):
    secs[m.group(1)] = m.group(0)
ids_in_sec = {k: set(re.findall(r"D\d{4}", re.search(r"\*\*この論点で出た肢\*\*：(.+)", v).group(1))) for k, v in secs.items()}
if len(secs) != 12: NG(f"記事に論点が {len(secs)} 個しかない（12個のはず）")
for k in ["PC-%d" % i for i in range(1, 13)]:
    if not list(D.glob(f"prompt_infographic_{k}.md")): NG(f"{k}: 図解のファイルがない")
SPEC4 = {"PC-1": ["D1433", "D1847"], "PC-2": ["D1544", "D0689", "D1546"], "PC-6": ["D0190", "D1265", "D2019", "D1495"],
         "PC-8": ["D0752", "D1047"], "PC-9": ["D1159", "D2046"], "PC-12": ["D0371", "D1801"]}
for k, ids in SPEC4.items():
    for i in ids:
        if i not in ids_in_sec.get(k, set()): NG(f"{k}: 4コマの肢 {i} が記事の同じ論点の『この論点で出た肢』にない")
# 最優先で潰す肢（付録の6肢）は、新作か既存のどれかの4コマでカバーされている
EXIST = {"D1996": "tools/drill/manga/D1996_prompt.md", "D0363": "tools/drill/manga/D0363_prompt.md", "D0473": "tools/drill/manga/D0473_prompt.md",
         "D0686": "tools/drill/manga/D0686_prompt.md", "D0939": "tools/drill/manga/D0939_prompt.md", "D1058": "tools/drill/manga/D1058_prompt.md",
         "D0687": "note-articles/joubun-nigate/fudousan-touki-hou/art051-1-hyoudaibu-henkou/prompt_4koma_03_shikichiken.md",
         "D0688": "note-articles/joubun-nigate/fudousan-touki-hou/art051-1-hyoudaibu-henkou/prompt_4koma_01_henkou-no-hani.md",
         "D0940": "tools/drill/manga/D0940_prompt.md"}
for i, pth in EXIST.items():
    if not (ROOT / pth).exists(): NG(f"既存の4コマが見つからない: {i} {pth}")
appendix = set(re.findall(r"^- (D\d{4}) [〇×]", art.split("### 付録")[1], flags=re.M)) if "### 付録" in art else set()
new_ids = {i for ids in SPEC4.values() for i in ids}
for i in sorted(appendix):
    if i not in new_ids and i not in EXIST: NG(f"付録の最優先肢 {i} がどの4コマにもカバーされていない")
OK(f"論点12個・最優先肢{len(appendix)}個の対応を確認（上にNGがなければ）")

# 7. 条文の確認：画像に載せた主な条文の語が、法令DBの原文にある
hou = (LAWS / "fudousan-touki-hou.md").read_text(encoding="utf8")
k1 = (LAWS / "fudousan-touki-kisoku-1.md").read_text(encoding="utf8")
k2 = (LAWS / "fudousan-touki-kisoku-2.md").read_text(encoding="utf8")
jn = (LAWS / "fudousan-touki-jimu-junsoku.md").read_text(encoding="utf8")
rei = (LAWS / "fudousan-touki-rei.md").read_text(encoding="utf8")
must = {
    "法": ["その変更があった日から一月以内に、当該地目又は地積に関する変更の登記を申請しなければならない", "その者に係る表題部所有者についての更正の登記又は所有権の登記があった日から一月以内に",
          "相互に接続していない土地の合筆の登記", "地目又は地番区域が相互に異なる土地の合筆の登記", "表題部所有者又は所有権の登記名義人が相互に異なる土地の合筆の登記",
          "表題部所有者又は所有権の登記名義人が相互に持分を異にする土地の合筆の登記", "所有権の登記がない土地と所有権の登記がある土地との合筆の登記", "所有権の登記以外の権利に関する登記がある土地",
          "その滅失の日から一月以内に、当該土地の滅失の登記を申請しなければならない", "河川管理者は、遅滞なく、その旨の登記を登記所に嘱託しなければならない",
          "共用部分である旨の登記又は団地共用部分である旨の登記がされた日から一月以内に", "その所有権の取得の日から一月以内に", "第四十四条第一項各号（第二号及び第六号を除く。）に掲げる登記事項について変更があったとき",
          "表題登記がない土地にあっては所有者", "土地の所有権登記名義人等は、筆界特定登記官に対し", "既に筆界特定登記官による筆界特定がされているとき。ただし、対象土地について更に筆界特定をする特段の必要があると認められる場合を除く",
          "前項の規定による筆界特定の申請の却下は、登記官の処分とみなす", "あらかじめ、その旨並びにその日時及び場所を当該土地の占有者に通知しなければならない",
          "何人も、登記官に対し、手数料を納付して、筆界特定手続記録のうち筆界特定書", "当該登記官を監督する法務局又は地方法務局の長に審査請求をすることができる", "行政不服審査法第十三条、第十五条第六項、第十八条"],
    "規則1": ["地図に表示された土地の区画又は地番に誤りがあるときは、当該土地の表題部所有者若しくは所有権の登記名義人又はこれらの相続人その他の一般承継人は、その訂正の申出をすることができる",
            "当該土地の登記記録の地積に錯誤があるときは、同項の申出は、地積に関する更正の登記の申請と併せてしなければならない", "登記官は、地図等に誤りがあると認めるときは、職権で、その訂正をすることができる",
            "甲二まで", "精度区分乙一まで", "精度区分乙三まで", "各筆界点の座標値を記録するものとする",
            "同一の不動産について申請する二以上の登記が、いずれも不動産の表題部の登記事項に関する変更の登記又は更正の登記であるとき",
            "当該申請人の現在の住所を証する情報の提供に代えることができる", "その作成者が署名し、又は記名押印しなければならない", "二 方位", "八 基本三角点等に基づく測量の成果による筆界点の座標値",
            "滅失の登記又は表題部の抹消をした場合", "土地改良法（昭和二十四年法律第百九十五号）又は土地区画整理法", "地役権の登記の抹消をしたとき",
            "訂正後の土地所在図、地積測量図、建物図面又は各階平面図を提供してしなければならない", "ただし、表題部の登記事項に関する更正の登記（土地所在図、地積測量図、建物図面又は各階平面図を添付情報とするものに限る。）をすることができる場合は、この限りでない",
            "第十六条第三項、第四項、第五項第三号及び第六項から第十四項までの規定は、第一項の申出について準用する"],
    "規則2": ["申請人が一筆の土地の一部の所有権を取得した者であるときは、その旨", "工作物、囲障又は境界標の有無その他の対象土地の状況", "図面を利用する等の方法により、現地の状況及び筆界として主張されている線の位置を具体的に明示する",
            "申請人が表題登記がない土地の所有者であるときは、当該申請人が当該土地の所有権を有することを証する情報", "申請人が一筆の土地の一部の所有権を取得した者であるときは、当該申請人が当該一筆の土地の一部について所有権を取得したことを証する情報"],
    "準則": ["分筆した土地については、分筆前の地番に支号を付して各筆の地番を定める", "合筆した土地については、合筆前の首位の地番をもってその地番とする", "特別の事情があるときは、第３号、第４号及び第６号の規定にかかわらず、適宜の地番を定めて差し支えない",
           "(5) 水力発電のための水路又は排水路は、雑種地とする。", "(16) 用悪水路かんがい用又は悪水はいせつ用の水路", "(17) ため池耕地かんがい用の用水貯留池", "(8) 池沼かんがい用水でない水の貯留池",
           "その全部を一団として雑種地とする", "同項第５号の地積を除く", "規則第７７条第１項第５号から第８号までに掲げる事項"],
    "令": ["申請情報を記載した書面には、法務省令で定める場合を除き、同項の規定により記名押印した者（委任による代理人を除く。）の印鑑に関する証明書"],
}
src = {"法": hou, "規則1": k1, "規則2": k2, "準則": jn, "令": rei}
for k, lst in must.items():
    for w in lst:
        if w not in src[k]: NG(f"法令DB（{k}）に原文が見つからない：{w[:60]}")
# 規則85条2項・87条1項・10条4項の見出しの存在
for w in ["第八十五条 （土地所在図の管理及び閉鎖等）", "第八十七条 （地役権図面の閉鎖）", "第八十八条 （土地所在図の訂正等）", "第七十七条 （地積測量図の内容）"]:
    if w not in k1: NG(f"規則の見出しが見つからない：{w}")
OK("条文の語：法令DBの原文と照合（上にNGがなければ一致）")

print(f"\n結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
