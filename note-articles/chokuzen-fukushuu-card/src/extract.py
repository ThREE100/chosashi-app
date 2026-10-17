#!/usr/bin/env python3
"""復習・チェック扱いの肢を論点ごとに抽出し、work/<slug>_items.json と work/_all.json を作る（個人の演習記録を含む作業用データ。公開しない）。
使い方: python3 note-articles/chokuzen-fukushuu-card/src/extract.py"""
import sys, json, pathlib, collections, re
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "tools" / "drill").is_dir())
sys.path.insert(0, str(ROOT / "tools" / "drill"))
import drill

SLUGS = {
 ("不動産登記法", "申請総論（申請情報・添付情報・代理・却下取下・還付・電子申請・登記識別情報）"): "f01-shinsei-souron",
 ("不動産登記法", "建物の分割・合併・合体・滅失・変更"): "f02-tatemono-bunkatsu-gappei",
 ("不動産登記法", "区分建物・敷地権・共用部分"): "f03-kubun-tatemono",
 ("不動産登記法", "土地の分筆・合筆・地積更正"): "f04-tochi-bunpitsu-gappitsu",
 ("不動産登記法", "建物の認定・個数・種類構造床面積"): "f05-tatemono-nintei",
 ("不動産登記法", "土地の滅失・地図・地積測量図・土地所在図"): "f06-chizu-sokuryozu",
 ("不動産登記法", "表題部所有者・所有権の登記"): "f07-hyodaibu-shoyusha",
 ("不動産登記法", "土地の表題・地目・地積"): "f08-tochi-hyodai-chimoku",
 ("不動産登記法", "登記制度・総則（登記官・図面・保存期間・管轄・通知）"): "f09-touki-seido-souron",
 ("不動産登記法", "筆界特定・境界"): "f10-hikkai-tokutei",
 ("不動産登記法", "建物図面・各階平面図"): "f11-tatemono-zumen",
 ("不動産登記法", "登録免許税"): "f12-tourokumenkyozei",
 ("民法", "共有・所有権・占有"): "m01-kyoyu-shoyuken-senyu",
 ("民法", "意思表示・無効取消"): "m02-ishi-hyoji",
 ("民法", "物権変動・対抗要件"): "m03-bukken-hendo",
 ("民法", "時効・条件期限"): "m04-jikou",
 ("民法", "用益権・担保物権"): "m05-youeki-tanpo",
 ("民法", "代理"): "m06-dairi",
 ("民法", "相続・親族"): "m07-souzoku",
 ("土地家屋調査士法", "調査士会・資格・その他"): "c01-chousashikai-shikaku",
 ("土地家屋調査士法", "調査士法人"): "c02-chousashi-houjin",
}
def main():
    bank = drill.load_bank(); st = drill.item_state(drill.read_log())
    logs = collections.defaultdict(list)
    for r in drill.read_log(): logs[r["id"]].append(r)
    out = collections.defaultdict(list)
    for iid, s in st.items():
        if iid not in bank: continue
        cl = drill.review_class(s)
        if cl not in ("must", "check"): continue
        b = bank[iid]
        seq = logs[iid]
        wrong_dir = collections.Counter()
        for r in seq:
            if r["res"] == "known": continue
            wrong_dir["不明(?)" if r["ans"] == "?" else ("正しい記述を×" if r["truth"] else "誤った記述を〇")] += 1
        out[(b["subject"], b["topic"])].append(dict(
            id=iid, subject=b["subject"], topic=b["topic"], statement=b["statement"], truth=b["truth"],
            cls=cl, W=drill.wrong_total(s), cons=s["cons"], n=s["n"], miscon=s["miscon"], unknown=s["unknown"],
            wrong_dir=dict(wrong_dir), history="".join({"known": "○", "miscon": "✗", "unknown": "？"}[r["res"]] for r in seq),
            sources=[dict(label=x.get("label"), q=x.get("q"), note_path=x.get("note_path")) for x in b.get("sources", [])]))
    wdir = pathlib.Path(HERE.parent / "work"); wdir.mkdir(exist_ok=True)
    allm = {}
    for key, items in out.items():
        slug = SLUGS[key]
        items.sort(key=lambda x: (x["cls"] != "must", -x["W"], x["id"]))
        (wdir / f"{slug}_items.json").write_text(json.dumps(dict(slug=slug, subject=key[0], topic=key[1], items=items), ensure_ascii=False, indent=1), encoding="utf8")
        allm[slug] = dict(subject=key[0], topic=key[1], must=sum(i["cls"] == "must" for i in items), check=sum(i["cls"] == "check" for i in items))
    (wdir / "_all.json").write_text(json.dumps(allm, ensure_ascii=False, indent=1), encoding="utf8")
    for k, v in sorted(allm.items()): print(k, v["must"], v["check"], v["topic"][:20])
    print("計", sum(v["must"] + v["check"] for v in allm.values()))
main()
