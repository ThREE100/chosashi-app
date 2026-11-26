"""ranking.json（count_articles.py の出力）を法令ごとにまとめる。
法令ごとに「解説に出てきた条文の種類の数」「22年度のうち11年度以上（半分以上）で出た条文の数」「上位の条文」と、半分以上の年度で出た条文ごとに「問1〜問3（民法の問題）以外の問題で引いた数」を出す。
使い方：python3 note-unei/hitogara/src/count_by_law.py <ranking.json> [--json 出力先] [--half 11]
"""
import json, argparse, collections
ORDER = ["不動産登記法","不動産登記令","不動産登記規則","不動産登記事務取扱手続準則","民法","区分所有法","土地家屋調査士法","土地家屋調査士法施行規則"]
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("--json"); ap.add_argument("--half", type=int, default=11)
    a = ap.parse_args()
    d = json.load(open(a.src, encoding="utf-8")); r = d["ranking"]
    out = []
    for law in ORDER:
        rows = [x for x in r if x["law"] == law]
        if not rows: continue
        out.append({"law": law, "kinds": len(rows), "half_or_more": sum(1 for x in rows if x["years"] >= a.half),
                    "max_years": rows[0]["years"], "top": [{"article": x["article"], "years": x["years"]} for x in rows[:3]],
                    # 半分以上の年度で出た条文が、何問のうち何問を問1〜問3（毎年の民法の問題）以外で引かれているか
                    "half_rows": [{"article": x["article"], "years": x["years"], "questions": x["questions"],
                                   "outside_q01_03": sum(1 for q in x["question_list"] if q.split("-Q")[1] not in ("01","02","03"))}
                                  for x in rows if x["years"] >= a.half]})
    for o in out:
        print(f'{o["law"]}: 条文{o["kinds"]}種類、{a.half}年度以上{o["half_or_more"]}条、最多{o["max_years"]}年度、上位 ' +
              "・".join(f'第{t["article"]}条({t["years"]})' for t in o["top"]))
        if o["law"] == "民法":
            for h in o["half_rows"]: print(f'   民法第{h["article"]}条：{h["questions"]}問のうち問4以降が{h["outside_q01_03"]}問')
    if a.json:
        json.dump({"years_total": d["years_total"], "half": a.half, "by_law": out}, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
if __name__ == "__main__":
    main()
