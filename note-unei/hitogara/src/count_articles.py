"""年度別の択一記事（H17〜R8、各20問）から、法令名つきで引用された条文を数える。
1問の中で同じ条文が何度出ても1回と数え、「何年度で出たか」「何問で出たか」を出す。
法令名のない「法第○条」「第○条」は、どの法令か機械的に決められないので数えない（控えめな数え方）。
使い方：python3 note-unei/hitogara/src/count_articles.py [--top 30] [--json 出力先]
"""
import re, glob, json, os, sys, collections, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
LAWS = [("不動産登記規則","規則"),("不動産登記令","令"),("不動産登記事務取扱手続準則","準則"),("準則","準則"),
        ("不動産登記法","法"),("建物の区分所有等に関する法律","区分所有法"),("区分所有法","区分所有法"),
        ("土地家屋調査士法施行規則","調査士法施行規則"),("土地家屋調査士法","調査士法"),("調査士法","調査士法"),("民法","民法")]
NUM = r"[0-9０-９]+(?:条の[0-9０-９]+)?"
PAT = re.compile("(" + "|".join(re.escape(a) for a,_ in LAWS) + r")第?(" + r"[0-9０-９]+" + r")条(?:の([0-9０-９]+))?")
NAME = {"法":"不動産登記法","令":"不動産登記令","規則":"不動産登記規則","準則":"不動産登記事務取扱手続準則",
        "区分所有法":"区分所有法","調査士法":"土地家屋調査士法","調査士法施行規則":"土地家屋調査士法施行規則","民法":"民法"}
Z = str.maketrans("０１２３４５６７８９","0123456789")
YEARS = ["h17","h18","h19","h20","h21","h22","h23","h24","h25","h26","h27","h28","h29","h30","r1","r2","r3","r4","r5","r6","r7","r8"]

def body(text):
    # 解説の本文だけを使う（プロンプト・確認事項・欄外メモなどの付録は除く）
    for cut in ["## 確認事項","## 見出し画像","インフォグラフィック","※欄外メモ","## 作図ガイド"]:
        i = text.find(cut)
        if i > 0: text = text[:i]
    return text

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--top", type=int, default=30); ap.add_argument("--json")
    a = ap.parse_args()
    by_year = collections.defaultdict(set); by_q = collections.Counter(); qlist = collections.defaultdict(list)
    nq = 0
    for y in YEARS:
        for f in sorted(glob.glob(f"{ROOT}/note-articles/{y}-mondai/q[0-9][0-9]-*.md")):
            nq += 1
            q = os.path.basename(f)[:3]
            found = set()
            for m in PAT.finditer(body(open(f, encoding="utf-8").read())):
                law = dict(LAWS)[m.group(1)]
                art = m.group(2).translate(Z) + ("の" + m.group(3).translate(Z) if m.group(3) else "")
                found.add((NAME[law], art))
            for k in found:
                by_year[k].add(y); by_q[k] += 1; qlist[k].append(f"{y.upper()}-{q.upper()}")
    rows = sorted(by_year, key=lambda k: (-len(by_year[k]), -by_q[k], k))
    out = [{"law":k[0],"article":k[1],"years":len(by_year[k]),"questions":by_q[k],
            "year_list":[y for y in YEARS if y in by_year[k]],"question_list":qlist[k]} for k in rows]
    print(f"対象：{nq}問（{len(YEARS)}年度）")
    for i,r in enumerate(out[:a.top],1):
        print(f"{i:2d}. {r['law']}第{r['article']}条  {r['years']}年度／{r['questions']}問")
    if a.json:
        json.dump({"questions_total":nq,"years_total":len(YEARS),"ranking":out}, open(a.json,"w",encoding="utf-8"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
