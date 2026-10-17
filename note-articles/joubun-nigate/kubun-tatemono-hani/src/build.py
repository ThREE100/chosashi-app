#!/usr/bin/env python3
"""parts/partN.py（記事と図解の元データ）から、記事（NN-slug.md）と画像プロンプト（NN-slug_prompts.md）を作る。
使い方: python3 note-articles/joubun-nigate/kubun-tatemono-hani/src/build.py [N ...]"""
import sys, re, importlib.util, pathlib
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
ROOT = next(p for p in HERE.parents if (p / "note-articles").is_dir())
sys.path.insert(0, str(HERE))
import scene_lib as sl

TOTAL = 10
def load(n):
    f = HERE.parent / "parts" / f"part{n}.py"
    spec = importlib.util.spec_from_file_location(f"part{n}", f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.P

def quote_block(file, head, only=None):
    """note-articles/laws/<file> の見出し行 head（行頭一致）から次の見出しまでを、引用形式の行リストにして返す。"""
    t = (ROOT / "note-articles" / "laws" / file).read_text(encoding="utf8").split("\n")
    idx = [i for i, l in enumerate(t) if l.strip() == head.strip()]
    if not idx: raise SystemExit(f"法令の見出しが見つからない: {file} / {head}")
    i = idx[0]; out = []
    for l in t[i + 1:]:
        if l.startswith("#"): break
        if l.strip(): out.append(l.strip())
    while out and re.match(r"^（.*）$", out[-1]): out.pop()   # 次の条の見出し行（括弧書き）を落とす
    if only: out = [l for l in out if any(l.startswith(o) for o in only)]
    return out

def render_law(entry):
    file, head, label = entry[0], entry[1], entry[2]
    only = entry[3] if len(entry) > 3 else None
    ls = quote_block(file, head, only)
    res = [f"> **{label}**", ">"]
    for l in ls:
        res += [f"> {l}", ">"]
    res.pop()
    return res

def build_note(P):
    n = P["no"]; L = []
    L.append(f"## 【土地家屋調査士受験生向け】苦手克服〜区分建物の範囲（{n}／{TOTAL}）{P['title']}〜")
    L += ["", f"**対象：{P['target']}**", ""]
    L += P["intro"]
    L += ["", "この記事では、次の順に書きます。", ""]
    L += [f"- {p['h']}" for p in P["points"]]
    L += ["", "画像は、まず「出題文の状態」を絵にして、そのうえで「正しいイメージ」と「誤ったイメージ」を並べて見せる形です。文章だけだと頭に浮かびにくい配置を、絵でつなげます。", "", "---", ""]
    L.append("### 前提：この記事で使う言葉と条文"); L.append("")
    for h, paras, laws in P["premise"]:
        L += [f"**{h}**", ""]
        for p in paras: L += [p, ""]
        for e in laws: L += render_law(e) + [""]
    L += ["---", ""]
    for k, p in enumerate(P["points"], 1):
        L += [f"### {p['h']}", ""]
        if p["wrong"]: L += ["**よくある勘違い**", ""] + [x for x in sum(([s, ""] for s in p["wrong"]), [])]
        L += ["**正しい整理**", ""] + [x for x in sum(([s, ""] for s in p["right"]), [])]
        if p["how"]: L += ["**見分け方**", ""] + [f"- {s}" for s in p["how"]] + [""]
        L += ["**たとえば**", ""]
        for _iid, kind, text, why in p["examples"]:
            L.append(f"- {text}　→　**{kind}**。{why}")
        L.append("")
        for si in p["scenes"]:
            sc = P["scenes"][si]
            L += [f"> 【画像挿入】図解{si + 1}「{sc['title']}」を入れます。{sc['note']}", ""]
        L += ["---", ""]
    L += ["### まとめ", ""] + [f"- {s}" for s in P["summary"]] + ["", "---", "", "### 確認事項", ""]
    L += [f"- {s}" for s in P["notes"]]
    L += ["- 図解と見出し画像は、プロンプトを作ったところまでです。画像の生成と目視確認は、まだ行っていません。", ""]
    return "\n".join(L)

def build_prompts(P):
    n = P["no"]; L = [f"# 区分建物の範囲（{n}／{TOTAL}）{P['title']}　画像プロンプト", "",
        "記事 `" + f"{n:02d}-{P['slug']}.md" + "` の画像プロンプトです。図解の画像は、記事に出てくる順に、図解1から番号を振っています（画像の中に番号は入りません）。画像は生成していません。ChatGPT（画像生成）に、各コードブロックをそのまま貼ります。", "",
        "どの図解も、1枚の中で「出題文の状態」→「正しいイメージ」（青）と「誤ったイメージ」（赤）の順に並べます。「出題文の内容」の札は、問われている記述が描かれている側のパネルに付きます。", ""]
    for k, sc in enumerate(P["scenes"], 1):
        L += [f"## 図解{k}：{sc['title']}", "", sc["memo"], "", "```text", (sl.scene_prompt(sc) if "pairs" in sc else sc["raw"]), "```", ""]
    L += ["## 見出し画像", "", "note見出し画像（1280×670px）です。ChatGPTに、キャラクターの参照画像（トリ先生と藍子の基準画像。`CHATGPT_MANGA_WORKFLOW.md` §3の6枚）を添付し、どちらがトリ先生でどちらが藍子かを一言添えて、下のコードブロックを貼ります。", "",
          f"- タイトル1行目：{P['midashi']['t1']}", f"- タイトル2行目：{P['midashi']['t2']}（「{P['midashi']['hot']}」を赤みのあるオレンジ）", f"- サブタイトル：{P['midashi']['sub']}", "",
          "```text", sl.midashi_prompt(P["midashi"]), "```", ""]
    return "\n".join(L)

def main():
    ns = [int(a) for a in sys.argv[1:]] or list(range(1, TOTAL + 1))
    for n in ns:
        f = HERE.parent / "parts" / f"part{n}.py"
        if not f.exists(): print("skip", n); continue
        P = load(n)
        (OUT / f"{n:02d}-{P['slug']}.md").write_text(build_note(P), encoding="utf8")
        (OUT / f"{n:02d}-{P['slug']}_prompts.md").write_text(build_prompts(P), encoding="utf8")
        print("built", n, P["slug"], len(P["scenes"]), "scenes")
main()
