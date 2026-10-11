#!/usr/bin/env python3
"""案の型（MANGA_RULES.md の「型の一覧」）の使用状況と、構成の知見ログの整理の時期を表示する。
使い方: python3 tools/drill/manga/pattern_audit.py
- 型ごとの使用数：各 *_prompt.md の設計メモ（第二案・第三案の設計メモ2・3も含む）の「【型の選び方】型：型N」を集計する。
- 未登録の型名・廃止された型の使用・型の行がないファイル（旧版）を表示する。
- 知見ログの件数が8件を超える、または型の一覧に「状態＝現行」でない型がある場合、整理の時期として通知する（整理の手順は MANGA_RULES.md「型の登録と整理の仕組み」）。"""
import re, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
LOG_LIMIT = 8

def registry(text):
    sec = re.search(r"### 型の一覧.*?\n((?:\|.*\n)+)", text)
    reg = {}
    if sec:
        for l in sec.group(1).splitlines():
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            if len(c) >= 6 and re.fullmatch(r"型\d+", c[0]):
                reg[c[0]] = dict(alias=c[1], gist=c[2], sample=c[3], date=c[4], state=c[5])
    return reg

def main():
    rules = (HERE / "MANGA_RULES.md").read_text(encoding="utf8")
    reg = registry(rules)
    use = collections.defaultdict(list); noline = []; unknown = collections.defaultdict(list)
    for f in sorted(HERE.glob("*_prompt.md")):
        if f.name.startswith("MAGAZINE"): continue
        src = f.read_text(encoding="utf8")
        sections = re.findall(r"^- 【型の選び方】(.*)$", src, re.M)
        if not sections: noline.append(f.name); continue
        for sec in sections:
            m = re.search(r"型：(型\d+)", sec)
            if not m: unknown[f.name].append("（型の名前なし）"); continue
            if m.group(1) in reg: use[m.group(1)].append(f.name)
            else: unknown[f.name].append(m.group(1))
    print("== 型の一覧と使用数（設計メモの【型の選び方】の集計。第二案・第三案の節も数える）")
    for k, v in reg.items():
        print(f"{k}（{v['alias']}・{v['state']}・登録 {v['date']}）：{len(use.get(k, []))}件  {v['gist']}")
        if use.get(k): print("    " + "、".join(sorted(set(x.replace('_prompt.md', '') for x in use[k]))))
    if unknown:
        print("\n== 未登録・不明な型名（先に型の一覧へ登録する）")
        for f, t in unknown.items(): print(f"  {f}: {t}")
    print(f"\n== 型の行がないファイル（旧版。改修時に足す）：{len(noline)}件")
    print("  " + "、".join(x.replace("_prompt.md", "") for x in noline))
    log = re.search(r"### 構成の知見ログ.*?\n(.*?)(?=\n#### 整理済みの知見)", rules, re.S)
    n = len(re.findall(r"^- 20\d\d-\d\d-\d\d", log.group(1), re.M)) if log else 0
    print(f"\n== 構成の知見ログ：{n}件（整理の目安 {LOG_LIMIT}件）")
    notes = []
    if n > LOG_LIMIT: notes.append(f"知見ログが {LOG_LIMIT} 件を超えた")
    odd = [k for k, v in reg.items() if v["state"] not in ("現行",)]
    if odd: notes.append("現行でない型がある：" + "、".join(odd))
    print("【整理の時期です】" + "／".join(notes) + "。MANGA_RULES.md「型の登録と整理の仕組み」の手順で整理する。" if notes else "整理の時期ではありません。")

main()
