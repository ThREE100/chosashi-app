#!/usr/bin/env python3
"""直前復習カードの機械チェック。python3 note-articles/chokuzen-fukushuu-card/src/check_all.py [slug ...]  NGがあれば終了コード1"""
import sys, re, json, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
sys.path.insert(0, str(HERE))
RISKY = set("号録権地番建物登記所請還売買当初詐欺規対抗無過効張説解間違肢承諾譲渡押債抵援認届款占帯証代保")
TREE = re.compile(r"決定木|判定木|ツリー|(?<![立竹樹植苗])木(?:では|に当て|の右|の左|の枝|の根|の分岐|の図|を描|で見|と呼)")
ng = []
def NG(m): ng.append(m)
slugs = sys.argv[1:] or [p.stem for p in sorted((OUT / "parts").glob("*.py"))]
for slug in slugs:
    f = OUT / "parts" / f"{slug}.py"
    spec = importlib.util.spec_from_file_location(slug, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); P = m.P
    W = json.loads((OUT / "work" / f"{slug}_items.json").read_text(encoding="utf8"))
    truth = {i["id"]: i["truth"] for i in W["items"]}
    t = f"[{slug}]"
    for key in ("title", "law", "clusters"):
        if key not in P: NG(f"{t} P に {key} がない")
    cl_ids = [i for c in P["clusters"] for i in c["ids"]]
    if sorted(cl_ids) != sorted(truth): NG(f"{t} グループの肢が過不足 不足={sorted(set(truth)-set(cl_ids))} 余分={sorted(set(cl_ids)-set(truth))} 重複={sorted({i for i in cl_ids if cl_ids.count(i)>1})}")
    cards = []
    for k, c in enumerate(P["clusters"], 1):
        for key in ("title", "ids", "cause", "understand", "verdicts", "law", "cards"):
            if key not in c: NG(f"{t} グループ{k}：{key} がない")
        if len(c["title"]) > 28: NG(f"{t} グループ{k}：タイトルが28字超")
        if not (100 <= len(c["cause"]) <= 420): NG(f"{t} グループ{k}：誤答の原因が100〜420字でない（{len(c['cause'])}）")
        if not (3 <= len(c["understand"]) <= 7): NG(f"{t} グループ{k}：理解のポイントが3〜7項目でない")
        for u in c["understand"]:
            if len(u) > 130: NG(f"{t} グループ{k}：理解のポイントが130字超：{u[:20]}…")
        if set(c["verdicts"]) != set(c["ids"]): NG(f"{t} グループ{k}：verdicts と ids が違う")
        for v in c["verdicts"].values():
            if len(v) > 90: NG(f"{t} グループ{k}：正しい結論が90字超：{v[:20]}…")
        if len(c["cards"]) > 3: NG(f"{t} グループ{k}：カードが3枚超")
        for cd in c["cards"]: cards.append((k, cd))
    # 肢と図解の対応
    covered = set()
    for k, cd in cards:
        ids = [i for p in cd["pairs"] for i in p["ids"]] if cd["kind"] == "pairs" else cd.get("ids", [])
        covered |= set(ids)
        gids = set(P["clusters"][k - 1]["ids"])
        if not set(ids) <= gids: NG(f"{t} グループ{k}のカードに、別グループの肢が入っている: {sorted(set(ids)-gids)}")
    has_cards = any(c["cards"] for c in P["clusters"])
    if has_cards:
        for k, c in enumerate(P["clusters"], 1):
            if c["cards"] and not (set(c["ids"]) <= {i for kk, cd in cards if kk == k for i in ([x for p in cd["pairs"] for x in p["ids"]] if cd["kind"] == "pairs" else cd.get("ids", []))}):
                NG(f"{t} グループ{k}：カードの絵にならない肢がある")
            if not c["cards"] and not c.get("existing_cards"): NG(f"{t} グループ{k}：カードも既存カードの参照もない")
    # カードの中身
    for n, (k, cd) in enumerate(cards, 1):
        tg = f"{t} カード{n}"
        if len(cd["t1"]) > 16 or len(cd["t2"]) > 16 or len(cd["sub"]) > 28: NG(f"{tg}：タイトル/サブタイトルが長い")
        if cd["kind"] == "pairs":
            if not 1 <= len(cd["pairs"]) <= 3: NG(f"{tg}：pairが1〜3でない")
            labs = list(cd["state"].get("labels", []))
            if len(labs) != len(set(labs)): NG(f"{tg}：stateのラベルが重複")
            for p in cd["pairs"]:
                tr = [truth[i] for i in p["ids"] if i in truth]
                if not tr: NG(f"{tg}：pairの肢が論点にない {p['ids']}")
                elif len(set(tr)) != 1: NG(f"{tg}：pairに正しい肢と誤った肢が混在 {p['ids']}")
                elif (p["stmt"] == "right") != tr[0]: NG(f"{tg}：pair {p['ids']} の stmt が正誤と食い違う")
                for side in ("right", "wrong"):
                    l2 = p[side].get("labels", [])
                    if len(l2) != len(set(l2)): NG(f"{tg}：{side} のラベル重複")
        elif cd["kind"] == "table":
            if not 2 <= len(cd["cols"]) <= 4 or not 2 <= len(cd["rows"]) <= 8: NG(f"{tg}：表の大きさが範囲外")
            for r in cd["rows"]:
                if len(r) != len(cd["cols"]): NG(f"{tg}：行の列数が違う {r}")
                for cell in r:
                    if cell not in ("@yes", "@no") and len(cell) > 24: NG(f"{tg}：セルが24字超 {cell}")
            if not cd.get("ids"): NG(f"{tg}：table に ids がない")
        else: NG(f"{tg}：kind が pairs/table でない")
    # 生成物
    note = (OUT / f"{slug}.md").read_text(encoding="utf8") if (OUT / f"{slug}.md").exists() else NG(f"{t} .md がない") or ""
    prom_f = OUT / f"{slug}_prompts.md"
    blocks = []
    if cards:
        if not prom_f.exists(): NG(f"{t} _prompts.md がない")
        else:
            prom = prom_f.read_text(encoding="utf8"); blocks = re.findall(r"```text\n(.*?)\n```", prom, re.S)
            if len(blocks) != len(cards): NG(f"{t} プロンプトのコードブロック {len(blocks)} 個（期待 {len(cards)}）")
    for i, b in enumerate(blocks, 1):
        body, fin = b.split("Final check before rendering:")
        mm = re.search(r"special attention to the kanji ([^;]+);", fin)
        listed = set(mm.group(1).replace(" ", "").split(",")) if mm else set()
        actual = RISKY & set(re.findall(r"[一-鿿]", body))
        if listed != actual: NG(f"{t} カード{i}：Final checkの漢字リストが本文と違う 余分={sorted(listed-actual)} 不足={sorted(actual-listed)}")
        if re.search(r"緑|green", b, re.I): NG(f"{t} カード{i}：緑／green")
        if TREE.search(b): NG(f"{t} カード{i}：樹形図の『木』『ツリー』")
        if "BACKGROUND REQUIREMENT" not in b or "alpha" not in b: NG(f"{t} カード{i}：背景の不透明化の指示がない")
        if "注意：" in b or re.search(r"[✓✕✗]", b): NG(f"{t} カード{i}：独立した日本語の注意文か✓✕")
        if re.search(r"D\d{4}|問題\d|図解\d|カード\d|画像\d|(平成|令和)\d+年度|第\d+問|誤答|演習|復習|[HR]\d{1,2}-Q", b): NG(f"{t} カード{i}：画像に載る文言に問題番号・年度・個人の演習結果に関わる語がある")
        if not re.search(r"Title \(large, bold, 2 lines\):\n「[^」]+」\n「[^」]+」", b): NG(f"{t} カード{i}：タイトルが2行でない")
    # 記事
    for pat in (r"緑", r"決定木", r"判定木", r"ツリー"):
        if re.search(pat, note): NG(f"{t} 記事に禁止語: {pat}")
    for c in P["clusters"]:
        for fld in [c["cause"], *c["understand"], *c["verdicts"].values()]:
            if re.search(r"D\d{4}", fld): NG(f"{t} 原因・理解・結論の文に問題番号: {fld[:20]}…")
    print(f"{t} 肢{len(truth)} / グループ{len(P['clusters'])} / カード{len(cards)}")
for m in ng: print("NG  ", m)
print(f"結果: NG {len(ng)}件")
sys.exit(1 if ng else 0)
