"""人柄が見える無料記事の機械チェック。使い方：python3 note-unei/hitogara/src/check.py [記事フォルダ ...]
フォルダを省くと、hitogara/ の下の NN-* をすべて確かめる。NG があれば終了コード1。
確かめること：
 1. 本文のランキングの行（N. 法令 第N条（見出し）…N年度）が ranking.json（あれば）のN位と一致し、順位が連番
 1b. 法令ごとの表の行と「第N条はM問のうちK問」が by_law.json（あれば）と一致する
 2. 「書かないこと」（senryaku.md 3.）と、個人の演習結果を思わせる語が本文にない
 3. 図のPNGがあり、Instagram用は 1080×1440
 4. 【要確認】が残っていれば警告（投稿前にユーザーが自分の言葉に直す印）
 5. 本文に出てくる「（法令名）第N条」が note-articles/laws/ の見出しにある
"""
import sys, os, re, json, glob
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(HERE))
NG_WORDS = ["合格するまで更新", "合格するまで追記", "予備校の解答例と照合", "教材としてまとめたものではな", "学習の過程の記録にすぎない",
            "誤答", "正答率", "回間違え", "回まちがえ", "回目で正解", "自己採点", "点数は"]
LAWFILES = {"不動産登記法":["fudousan-touki-hou.md"], "民法":["minpou-1-soukyoku-bukken.md","minpou-2-saiken.md","minpou-3-shinzoku-souzoku.md"],
            "不動産登記令":["fudousan-touki-rei.md"], "不動産登記規則":["fudousan-touki-kisoku-1.md","fudousan-touki-kisoku-2.md","fudousan-touki-kisoku-3.md"],
            "不動産登記事務取扱手続準則":["fudousan-touki-jimu-junsoku.md"], "区分所有法":["kubunshoyuu-hou.md"], "土地家屋調査士法":["chousashi-hou.md"]}
KAN = dict(zip("〇一二三四五六七八九", range(10)))
def kan2int(s):
    n, cur = 0, 0
    for ch in s:
        if ch in KAN: cur = KAN[ch]
        else:
            u = {"十":10,"百":100,"千":1000}[ch]; n += (cur or 1) * u; cur = 0
    return n + cur
def law_has(law, art):
    for f in LAWFILES.get(law, []):
        t = open(f"{ROOT}/note-articles/laws/{f}", encoding="utf-8").read()
        for m in re.finditer(r"^#+\s*第([0-9]+|[〇一二三四五六七八九十百千]+)条", t, re.M):
            v = m.group(1); v = int(v) if v.isdigit() else kan2int(v)
            if v == art: return True
    return False
def check(d):
    ng, warn = [], []
    art = open(f"{d}/article.md", encoding="utf-8").read()
    body = art.split("## 本文", 1)[-1]
    for w in NG_WORDS:
        if w in body: ng.append(f"書かない語「{w}」が本文にある")
    rj = f"{d}/ranking.json"
    if os.path.exists(rj):
        r = json.load(open(rj, encoding="utf-8"))["ranking"]
        lines = re.findall(r"^(\d+)\. (\S+) 第(\S+?)条（.*?）…(\d+)年度$", body, re.M)
        if not lines: ng.append("ranking.json があるのに、本文に「N. 法令 第N条（見出し）…N年度」の行がない")
        for no, law, a_, y in lines:
            i = int(no)
            row = r[i-1] if 0 < i <= len(r) else None
            if not row or (row["law"], row["article"], row["years"]) != (law, a_, int(y)):
                ng.append(f"ランキング{i}位の行（{law}第{a_}条・{y}年度）が ranking.json と合わない")
        nums = [int(x[0]) for x in lines]
        if nums and nums != list(range(nums[0], nums[0] + len(nums))): ng.append(f"ランキングの順位が連番でない：{nums}")
    bj = f"{d}/by_law.json"
    if os.path.exists(bj):
        for o in json.load(open(bj, encoding="utf-8"))["by_law"]:
            top = "・".join(f'第{t["article"]}条' for t in o["top"])
            if f'| {o["law"]} | {o["kinds"]} | {o["half_or_more"]} | {top} |' not in body:
                ng.append(f'法令ごとの表の「{o["law"]}」の行が by_law.json（{o["kinds"]}・{o["half_or_more"]}・{top}）と合わない')
            for h in o.get("half_rows", []):
                m = re.search(rf'第{h["article"]}条は(\d+)問のうち(\d+)問', body)
                if m and (int(m.group(1)), int(m.group(2))) != (h["questions"], h["outside_q01_03"]):
                    ng.append(f'{o["law"]}第{h["article"]}条の「{m.group(0)}」が by_law.json（{h["questions"]}問のうち{h["outside_q01_03"]}問）と合わない')
    for m in re.finditer(r"(不動産登記事務取扱手続準則|不動産登記法|不動産登記令|不動産登記規則|区分所有法|民法) 第([0-9]+)条", body):
        if not law_has(m.group(1), int(m.group(2))): ng.append(f"{m.group(1)}第{m.group(2)}条が laws/ の見出しに見つからない")
    for p in glob.glob(f"{d}/*.png"):
        from PIL import Image
        w, h = Image.open(p).size
        if p.endswith("_ig.png") and (w, h) != (1080, 1440): ng.append(f"{os.path.basename(p)} が {w}×{h}（1080×1440 のはず）")
    for m in re.finditer(r"（図：`([^`]+)`）", body):
        if not os.path.exists(f"{d}/{m.group(1)}"): ng.append(f"図 {m.group(1)} がない")
    k = body.count("【要確認】")
    if k: warn.append(f"【要確認】が{k}か所（投稿前に自分の言葉に直す）")
    return ng, warn
def main():
    dirs = sys.argv[1:] or sorted(glob.glob(f"{HERE}/[0-9][0-9]-*"))
    total = 0
    for d in dirs:
        ng, warn = check(d)
        total += len(ng)
        print(f"== {os.path.basename(d)}: NG {len(ng)}件")
        for x in ng: print("  NG", x)
        for x in warn: print("  注意", x)
    sys.exit(1 if total else 0)
if __name__ == "__main__":
    main()
