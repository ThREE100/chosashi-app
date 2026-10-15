#!/usr/bin/env python3
"""README.md（入口）と grouping.md（肢のグループ分けの作業用一覧）を作る。"""
import json, pathlib, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent; OUT = HERE.parent
sys.path.insert(0, str(HERE))
def load(n):
    f = OUT / "parts" / f"part{n}.py"
    spec = importlib.util.spec_from_file_location(f"part{n}", f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.P
G = ["# 区分建物の範囲　肢のグループ分け（作業用の一覧・記事ではない）", "",
     "一問一答で復習・チェックの対象になっている肢のうち、区分建物（敷地権・規約敷地・共用部分を含む）に関わる肢を、論点ごとにグループ分けした一覧です。記事・画像には肢の番号や演習結果を載せないので、対応はこのファイルで確かめます。",
     "抽出の条件は、論点「区分建物・敷地権・共用部分」の肢のうち復習の区分が要復習またはチェックのもの全部と、他の論点の肢のうち区分建物に関わるもの（2026-10-15時点）です。区分建物でない建物の肢は除きました。", ""]
R = ["# 区分建物の範囲　苦手克服シリーズ（全9回）", "",
     "択一式の一問一答で、復習・チェックの対象になっている区分建物の肢を、論点ごとの9つのグループにまとめた苦手克服の記事です（2026-10-15作成）。",
     "敷地権や規約敷地は、出題文の状態そのものが頭に浮かびにくいのが弱点です。そこで各回の図解は、「①出題文の状態の絵 → ②正しいイメージ（青）→ ③誤ったイメージ（赤）」の順で、確かめる記述1つにつき1組の絵を並べる形にしました。文章の知識と絵をつなげるための図です。", "",
     "## 構成", ""]
tot_i = tot_s = tot_p = 0
for n in range(1, 10):
    f = OUT / "parts" / f"part{n}.py"
    if not f.exists(): continue
    P = load(n); W = json.loads((OUT / "work" / f"part{n}_items.json").read_text(encoding="utf8"))
    ns = len(P["scenes"]); npair = sum(len(s["pairs"]) for s in P["scenes"])
    tot_i += len(W["items"]); tot_s += ns; tot_p += npair
    R.append(f"{n}. [{P['title']}]({n:02d}-{P['slug']}.md)　（肢{len(W['items'])}／図解{ns}枚／見出し画像1枚。画像プロンプトは [{n:02d}-{P['slug']}_prompts.md]({n:02d}-{P['slug']}_prompts.md)）")
    G += [f"## {n}. {P['title']}（{len(W['items'])}肢）", ""]
    iid = {i["id"]: i for i in W["items"]}
    for k, p in enumerate(P["points"], 1):
        G += [f"### {p['h']}", ""]
        for e in p["examples"]:
            it = iid[e[0]]
            G.append(f"- {e[0]}（{it['q']}{it['label']}／{'要復習' if it['rc']=='must' else 'チェック'}／{'正' if it['truth'] else '誤'}）{it['statement'][:60].replace(chr(10),' ')}…")
        G.append("")
R += ["", f"合計：肢{tot_i}、図解{tot_s}枚（正誤を確かめる記述の組 {tot_p}）、見出し画像{len([1 for n in range(1,10) if (OUT/'parts'/f'part{n}.py').exists()])}枚。", "",
      "## 読み方・使い方", "",
      "- 記事は、1回につき「前提（用語と条文）→ ポイントごとの整理（よくある勘違い／正しい整理／見分け方／たとえば）→ まとめ → 確認事項」の順です。ポイントのあとに「画像挿入」の指示があり、対応する図解のプロンプトが `NN-…_prompts.md` にあります。",
      "- 図解の画像は、プロンプトをChatGPT（画像生成）に貼って作ります。画像の生成と目視確認は未実施です。",
      "- 肢の番号と、どの肢がどのポイントに入っているかは、作業用の [grouping.md](grouping.md) にあります（記事・画像には載せていません）。",
      "- 作り方：`src/build.py`（記事とプロンプトを生成）、`src/check_all.py`（機械チェック）、`parts/partN.py`（元データ）、`work/`（肢の抽出結果）。", "",
      "## このシリーズの位置づけ", "",
      "条文を主役にした「条文別『苦手克服』シリーズ」（`note-articles/joubun-nigate/`）の一つで、条文ではなく**区分建物の範囲**を主役にした回です。個別の条文（区分所有法第5条など）は、同シリーズの各回を参照してください。"]
(OUT / "README.md").write_text("\n".join(R) + "\n", encoding="utf8")
(OUT / "grouping.md").write_text("\n".join(G) + "\n", encoding="utf8")
print("index ok", tot_i, tot_s, tot_p)
