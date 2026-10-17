#!/usr/bin/env python3
"""区分建物の範囲シリーズの機械チェック。python3 note-articles/joubun-nigate/kubun-tatemono-hani/src/check_all.py [N ...]  NGがあれば終了コード1"""
import sys, re, json, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
sys.path.insert(0, str(HERE))
ROOT = next(p for p in HERE.parents if (p / "note-articles").is_dir())
RISKY = set("号録権地番建物登記所請還売買当初詐欺規対抗無過効張説解間違肢承諾譲渡押債抵援認届款占帯証代保")
TREE = re.compile(r"決定木|判定木|ツリー|(?<![立竹樹植苗])木(?:では|に当て|の右|の左|の枝|の根|の分岐|の図|を描|で見|と呼)")
ng, okc = [], 0
def NG(m): ng.append(m)
ns = [int(a) for a in sys.argv[1:]] or list(range(1, 11))
for n in ns:
    f = OUT / "parts" / f"part{n}.py"
    if not f.exists(): NG(f"part{n}.py がない"); continue
    spec = importlib.util.spec_from_file_location(f"part{n}", f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); P = m.P
    W = json.loads((OUT / "work" / f"part{n}_items.json").read_text(encoding="utf8"))
    truth = {i["id"]: i["truth"] for i in W["items"]}
    tag = f"[{n}]"
    note = (OUT / f"{n:02d}-{P['slug']}.md").read_text(encoding="utf8")
    prom = (OUT / f"{n:02d}-{P['slug']}_prompts.md").read_text(encoding="utf8")
    # 1 肢の網羅と正誤
    ex_ids = [e[0] for p in P["points"] for e in p["examples"] if e[0]]
    miss = set(truth) - set(ex_ids); extra = set(ex_ids) - set(truth)
    if miss: NG(f"{tag} 「たとえば」にない肢: {sorted(miss)}")
    if extra: NG(f"{tag} この回にない肢が入っている: {sorted(extra)}")
    for p in P["points"]:
        for iid, kind, text, why in p["examples"]:
            if iid in truth and (kind == "正しい") != truth[iid]: NG(f"{tag} {iid} の正誤が、バンクの値（{'正' if truth[iid] else '誤'}）と食い違う")
            if kind not in ("正しい", "誤り"): NG(f"{tag} {iid} の判定は『正しい』か『誤り』")
    pair_ids = [i for s in P["scenes"] for p in s.get("pairs", []) for i in p["ids"]]
    miss = set(truth) - set(pair_ids)
    if miss: NG(f"{tag} 図解のpairにない肢: {sorted(miss)}")
    for s in P["scenes"]:
        for p in s.get("pairs", []):
            tr = [truth[i] for i in p["ids"] if i in truth]
            if tr and len(set(tr)) != 1: NG(f"{tag} 1つのpairに、正しい肢と誤った肢が混ざっている: {p['ids']}")
            elif tr and (p["stmt"] == "right") != tr[0]: NG(f"{tag} pair {p['ids']} の stmt（出題文の内容の側）が正誤と食い違う")
    # 2 マーカーと図解
    nsc = len(P["scenes"]); marks = re.findall(r"^> 【画像挿入】図解(\d+)「", note, re.M)
    if sorted(set(int(x) for x in marks)) != list(range(1, nsc + 1)): NG(f"{tag} 画像挿入マーカーと図解の数が合わない（マーカー {sorted(set(marks))} / 図解 {nsc}）")
    if [int(x) for x in marks] != sorted(int(x) for x in marks): NG(f"{tag} 画像挿入マーカーが図解の番号順に並んでいない")
    blocks = re.findall(r"```text\n(.*?)\n```", prom, re.S)
    if len(blocks) != nsc + 1: NG(f"{tag} プロンプトのコードブロックが {len(blocks)} 個（期待 {nsc + 1}＝図解{nsc}＋見出し1）")
    for i, b in enumerate(blocks, 1):
        body, fin = b.split("Final check before rendering:")
        mm = re.search(r"special attention to the kanji ([^;]+);", fin)
        listed = set(mm.group(1).replace(" ", "").split(",")) if mm else set()
        actual = (RISKY & set(re.findall(r"[一-鿿]", body))) if i <= nsc else set(re.findall(r"[一-鿿]", body.split("TEXT (reproduce verbatim")[1].split("TOPIC SCENES")[0]))
        if i <= nsc and listed != actual: NG(f"{tag} 図解{i}：Final checkの漢字リストが本文と違う 余分={sorted(listed-actual)} 不足={sorted(actual-listed)}")
        if re.search(r"緑|green", b, re.I): NG(f"{tag} 図{i}：緑／green")
        if TREE.search(b): NG(f"{tag} 図{i}：樹形図の『木』『ツリー』")
        if "BACKGROUND REQUIREMENT" not in b or "alpha" not in b: NG(f"{tag} 図{i}：背景の不透明化の指示がない")
        if "注意：" in b or re.search(r"[✓✕✗]", b): NG(f"{tag} 図{i}：独立した日本語の注意文か✓✕")
        if re.search(r"D\d{4}|問題\d|図解\d|画像\d|(平成|令和)\d+年度|第\d+問", b): NG(f"{tag} 図{i}：画像に載る文言に問題番号か図の番号か年度がある")
        if i <= nsc and not re.search(r"Title \(large, bold, 2 lines\):\n「[^」]+」\n「[^」]+」", b): NG(f"{tag} 図解{i}：タイトルが2行でない")
    # 3 記事の体裁
    if re.search(r"^\|", note, re.M): NG(f"{tag} 記事に表がある")
    for pat in (r"D\d{4}", r"第\d+問", r"[HR]\d{1,2}-Q", r"(平成|令和)\d+年度", r"一問一答", r"筆者", r"誤答", r"演習", r"\d+回のうち", r"復習", r"要復習", r"苦手分析"):
        mm = re.search(pat, note)
        if mm: NG(f"{tag} 記事に個人の演習結果・問題番号に関わる語: {mm.group(0)}")
    for pat in (r"緑", r"決定木", r"判定木", r"ツリー"):
        if re.search(pat, note): NG(f"{tag} 記事に禁止語: {pat}")
    for para in note.split("\n"):
        if para and not para.startswith((">", "#", "-", "---", "*", " ")) and len(para) > 125: NG(f"{tag} 125字を超える段落: {para[:24]}…")
        if para.startswith("- ") and len(para) > 190: NG(f"{tag} 190字を超える箇条書き: {para[:24]}…")
    for need in ("確認事項", "まとめ", "前提"):
        if need not in note: NG(f"{tag} 記事に『{need}』がない")
    mt = P["midashi"]
    for s in (mt["t1"], mt["t2"]):
        if len(s) > 16: NG(f"{tag} 見出し画像の行が16字を超える: {s}")
    if mt["hot"] not in mt["t2"]: NG(f"{tag} 見出し画像の強調語がタイトル2行目にない")
    for s in (mt["t1"], mt["t2"], mt["sub"]):
        if s not in prom: NG(f"{tag} 見出し画像プロンプトに『{s}』がない")
    # 4 禁止：画像のタイトル／ラベルに結論や問題番号は入れない（labels 重複）
    for k, s in enumerate(P["scenes"], 1):
        if "pairs" not in s: continue
        labs = list(s["state"].get("labels", []))
        if len(labs) != len(set(labs)): NG(f"{tag} 図解{k}：state のラベルが重複")
        for p in s["pairs"]:
            for side in ("right", "wrong"):
                l2 = p[side].get("labels", [])
                if len(l2) != len(set(l2)): NG(f"{tag} 図解{k}：{side} のラベルが重複")
    print(f"[{n}] 肢{len(truth)} / 図解{nsc}枚 / pair{len(pair_ids)}")
for m in ng: print("NG  ", m)
print(f"結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
