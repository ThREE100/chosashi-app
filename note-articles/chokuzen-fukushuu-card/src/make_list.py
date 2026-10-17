#!/usr/bin/env python3
"""全論点の復習リスト（00-fukushuu-list.md）と、既存教材を参照する論点（f03・c01・c02）の .md を作る。
使い方: python3 note-articles/chokuzen-fukushuu-card/src/make_list.py"""
import sys, json, re, glob, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
sys.path.insert(0, str(HERE))
import build as B

ORDER = ["f01-shinsei-souron", "f02-tatemono-bunkatsu-gappei", "f03-kubun-tatemono", "f04-tochi-bunpitsu-gappitsu", "f05-tatemono-nintei", "f06-chizu-sokuryozu",
         "f07-hyodaibu-shoyusha", "f08-tochi-hyodai-chimoku", "f09-touki-seido-souron", "f10-hikkai-tokutei", "f11-tatemono-zumen", "f12-tourokumenkyozei",
         "m01-kyoyu-shoyuken-senyu", "m02-ishi-hyoji", "m03-bukken-hendo", "m04-jikou", "m05-youeki-tanpo", "m06-dairi", "m07-souzoku",
         "c01-chousashikai-shikaku", "c02-chousashi-houjin"]
REF = {"f03-kubun-tatemono", "c01-chousashikai-shikaku", "c02-chousashi-houjin"}
KUBUN = OUT.parent / "joubun-nigate" / "kubun-tatemono-hani"

def load_work(slug): return json.loads((OUT / "work" / f"{slug}_items.json").read_text(encoding="utf8"))

def short(s, n=78):
    s = re.sub(r"\s+", " ", s)
    return s if len(s) <= n else s[:n] + "…"

def kubun_parts():
    res = {}
    for f in sorted(glob.glob(str(KUBUN / "work" / "part*_items.json"))):
        n = int(re.search(r"part(\d+)_", f).group(1))
        ids = [i["id"] for i in json.loads(pathlib.Path(f).read_text(encoding="utf8"))["items"]]
        pf = KUBUN / "parts" / f"part{n}.py"
        spec = importlib.util.spec_from_file_location(f"kp{n}", pf); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        res[n] = dict(title=m.P["title"], slug=m.P["slug"], ids=set(ids))
    return res

def make_ref_f03():
    W = load_work("f03-kubun-tatemono"); items = {i["id"]: i for i in W["items"]}; kp = kubun_parts()
    L = ["# 直前復習カード｜不動産登記法／区分建物・敷地権・共用部分", "",
         f"> 個人用の復習資料です（演習記録に基づくため、公開用の記事には使いません）。復習対象 {len(items)}肢。この論点は、すでに作ってある『苦手克服〜区分建物の範囲』シリーズ（全9回）が全肢をカバーしているため、新しい図解は作らず、肢ごとに既存の回と図解プロンプトを案内します（誤答の原因・理解のポイント・図解カードは、各回の記事と `_prompts.md` にあります）。", "",
         f"シリーズの入口：`note-articles/joubun-nigate/kubun-tatemono-hani/README.md`", ""]
    used = set()
    for n, p in sorted(kp.items()):
        ids = [i for i in items if i in p["ids"]]
        if not ids: continue
        used |= set(ids)
        L += [f"## 第{n}回：{p['title']}（{len(ids)}肢）", "",
              f"- 記事：`note-articles/joubun-nigate/kubun-tatemono-hani/{n:02d}-{p['slug']}.md`　図解プロンプト：`{n:02d}-{p['slug']}_prompts.md`", ""]
        for iid in ids: L += [B.item_line(items[iid]), ""]
    rest = [i for i in items if i not in used]
    if rest:
        L += ["## 既存シリーズにない肢", ""] + [B.item_line(items[i]) + "\n" for i in rest]
    (OUT / "f03-kubun-tatemono.md").write_text("\n".join(L), encoding="utf8")

def make_ref_c():
    note = {
        "c01-chousashikai-shikaku": ["総合記事③『土地家屋調査士法編』の図解・4コマ：`note-articles/sokatsu-zukai/03-chousashi-hou/README.md`（依頼応諾義務の図解は `prompt_infographic_C1-1.md`、会則の認可は `prompt_infographic_C1-3.md`）",
                                     "条文別『苦手克服』（依頼応諾義務）：`note-articles/joubun-nigate/chousashi-hou/art022-041-irai-ouyou-gimu/`"],
        "c02-chousashi-houjin": ["総合記事③『土地家屋調査士法編』の図解・4コマ：`note-articles/sokatsu-zukai/03-chousashi-hou/README.md`（法人の届出先の図解は `prompt_infographic_C1-3.md` の図解10）"]}
    for slug in ("c01-chousashikai-shikaku", "c02-chousashi-houjin"):
        W = load_work(slug)
        L = [f"# 直前復習カード｜{W['subject']}／{W['topic']}", "",
             f"> 個人用の復習資料です（演習記録に基づくため、公開用の記事には使いません）。復習対象 {len(W['items'])}肢。この論点は、すでに作ってある土地家屋調査士法の図解・4コマが肢をカバーしているため、新しい図解は作らず、既存教材を案内します。", ""]
        L += ["## 既存の教材", ""] + [f"- {x}" for x in note[slug]] + [""]
        L += ["## 復習リスト", ""]
        for it in W["items"]: L += [B.item_line(it), ""]
        (OUT / f"{slug}.md").write_text("\n".join(L), encoding="utf8")

def make_master():
    rows, body = [], []
    tot_m = tot_c = 0
    for slug in ORDER:
        W = load_work(slug); its = W["items"]
        m = sum(i["cls"] == "must" for i in its); c = len(its) - m; tot_m += m; tot_c += c
        cards = ""
        pf = OUT / "parts" / f"{slug}.py"
        if pf.exists():
            spec = importlib.util.spec_from_file_location(slug, pf); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
            cards = f"{sum(len(g['cards']) for g in mod.P['clusters'])}枚（{len(mod.P['clusters'])}グループ）"
        elif slug in REF: cards = "既存教材を参照"
        else: cards = "（作成中）"
        rows.append(f"| {W['subject']}／{W['topic']} | {m} | {c} | {m + c} | [{slug}.md]({slug}.md) | {cards} |")
        body += [f"## {W['subject']}／{W['topic']}（要復習{m}・チェック{c}）", "", f"詳細：[{slug}.md]({slug}.md)", ""]
        for it in its:
            mark = "要復習" if it["cls"] == "must" else "チェック"
            tr = "〇" if it["truth"] else "×"
            body.append(f"- {it['id']}｜{mark}｜正解{tr}｜履歴 {it['history']}｜{short(it['statement'])}")
        body.append("")
    L = ["# 復習リスト（論点別）", "",
         "> 個人用の復習資料です。一問一答ドリルで『要復習』『チェック』になっている肢を、論点ごとに並べ直しました。要復習は誤解・未習得の回数が多い順、そのあとにチェックを並べています。履歴は ○正解・✗誤解・？わからない の順（古い順）です。",
         "", f"合計：要復習 {tot_m}肢・チェック {tot_c}肢（計 {tot_m + tot_c}肢）", "",
         "| 論点 | 要復習 | チェック | 計 | 詳細（原因・理解のポイント・図解） | 図解カード |", "|---|---|---|---|---|---|"] + rows + [""] + body
    (OUT / "00-fukushuu-list.md").write_text("\n".join(L), encoding="utf8")

make_ref_f03(); make_ref_c(); make_master()
print("ok")
