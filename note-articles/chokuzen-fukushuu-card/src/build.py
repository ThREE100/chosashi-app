#!/usr/bin/env python3
"""parts/<slug>.py（P）と work/<slug>_items.json から、論点ごとの 復習リスト＋原因＋理解のポイント（NN.md）と図解プロンプト（NN_prompts.md）を作る。
使い方: python3 note-articles/chokuzen-fukushuu-card/src/build.py [slug ...]"""
import sys, json, re, glob, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
sys.path.insert(0, str(HERE))
import cardlib
ROOT = next(p for p in HERE.parents if (p / "tools" / "drill").is_dir())
MANGA = sorted(p.name for p in (ROOT / "tools" / "drill" / "manga").glob("D*_prompt.md"))

def manga_for(iid):
    return [n for n in MANGA if iid in re.findall(r"D\d{4}", n)]

def load_part(slug):
    f = OUT / "parts" / f"{slug}.py"
    spec = importlib.util.spec_from_file_location(slug, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.P

def item_line(it, verdict=None):
    cls = "要復習" if it["cls"] == "must" else "チェック"
    tr = "正しい記述（〇）" if it["truth"] else "誤った記述（×）"
    d = "・".join(f"{k}{v}回" for k, v in it["wrong_dir"].items())
    s = f"- 【{cls}】**{it['id']}**（{tr}）{it['statement']}\n  - 履歴：{it['history']}（誤解・未習得 通算{it['W']}回、その後の連続正解{it['cons']}回）／間違いの向き：{d}"
    if verdict: s += f"\n  - 正しい結論：{verdict}"
    mg = manga_for(it["id"])
    if mg: s += "\n  - 既存の4コマ：" + "、".join(f"`tools/drill/manga/{n}`" for n in mg)
    return s

def build(slug):
    W = json.loads((OUT / "work" / f"{slug}_items.json").read_text(encoding="utf8"))
    P = load_part(slug); items = {i["id"]: i for i in W["items"]}
    must = sum(i["cls"] == "must" for i in W["items"]); chk = len(W["items"]) - must
    ncard = sum(len(c["cards"]) for c in P["clusters"])
    L = [f"# 直前復習カード｜{W['subject']}／{P['title']}", "",
         f"> 個人用の復習資料です（演習記録に基づくため、公開用の記事には使いません）。復習対象 {len(items)}肢（要復習{must}・チェック{chk}）／原因の整理 {len(P['clusters'])}グループ／図解カード {ncard}枚。図解のプロンプトは [{slug}_prompts.md]({slug}_prompts.md)。画像は生成していません。", "",
         f"主な根拠：{P['law']}", ""]
    if P.get("existing"):
        L += ["## 既存の教材", ""] + [f"- {x}" for x in P["existing"]] + [""]
    card_no = 0
    for k, c in enumerate(P["clusters"], 1):
        L += [f"## グループ{k}：{c['title']}（{len(c['ids'])}肢）", "", "**誤答の原因**", "", c["cause"], "", "**正しく理解するために必要なこと**", ""]
        L += [f"- {u}" for u in c["understand"]]
        L += ["", f"**根拠**：{c['law']}", "", "**復習リスト**", ""]
        for iid in c["ids"]: L += [item_line(items[iid], c["verdicts"].get(iid)), ""]
        if c["cards"]:
            L += ["**図解カード**", ""]
            for j, cd in enumerate(c["cards"], 1):
                card_no += 1
                L.append(f"- カード{card_no}「{cd['t1']}／{cd['t2']}」：{cd['memo']}（{slug}_prompts.md の「カード{card_no}」）")
            L.append("")
        elif c.get("existing_cards"):
            L += ["**図解カード（既存）**", ""] + [f"- {x}" for x in c["existing_cards"]] + [""]
    (OUT / f"{slug}.md").write_text("\n".join(L), encoding="utf8")
    if ncard:
        R = [f"# 直前復習カード｜{P['title']}　図解プロンプト", "",
             f"`{slug}.md` の図解カードのプロンプトです。カードは記事のグループ順に、カード1から番号を振っています（画像の中に番号は入りません）。画像は生成していません。ChatGPT（画像生成）に、各コードブロックをそのまま貼ります。", ""]
        card_no = 0
        for k, c in enumerate(P["clusters"], 1):
            for cd in c["cards"]:
                card_no += 1
                R += [f"## カード{card_no}：{cd['t1']}／{cd['t2']}（グループ{k}　{c['title']}）", "", cd["memo"], "", "```text", cardlib.card_prompt(cd), "```", ""]
        (OUT / f"{slug}_prompts.md").write_text("\n".join(R), encoding="utf8")
    print(slug, "肢", len(items), "グループ", len(P["clusters"]), "カード", ncard)

if __name__ == "__main__":
    slugs = sys.argv[1:] or [p.stem for p in sorted((OUT / "parts").glob("*.py"))]
    for s in slugs: build(s)
