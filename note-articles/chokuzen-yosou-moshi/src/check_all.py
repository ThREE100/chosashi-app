#!/usr/bin/env python3
"""直前予想模試20問の記事（../qNN-*.md）とデータ（qNN.py）の機械チェック。NG（直すべき）とWARN（目視で確認）を出す。

使い方: python3 note-articles/chokuzen-yosou-moshi/src/check_all.py
format-template.md・qa-checklist.md・infographic-prompt-template.md の固定ルールのうち、機械で確かめられるものを検査する。
"""
import importlib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

KEY = {1: 3, 2: 4, 3: 2, 4: 3, 5: 1, 6: 4, 7: 1, 8: 3, 9: 4, 10: 2, 11: 5, 12: 5, 13: 3, 14: 3, 15: 2, 16: 2, 17: 4, 18: 5, 19: 4, 20: 4}
NG, WARN = [], []


def ng(n, msg):
    NG.append(f"Q{n:02d} NG  {msg}")


def warn(n, msg):
    WARN.append(f"Q{n:02d} WARN {msg}")


def sentences(text):
    t = re.sub(r"\*\*たとえば\*\*、", "", text)
    for s in re.split(r"(?<=。)", t):
        s = s.strip()
        if s:
            yield s


def keitai_ok(s):
    s = s.rstrip("。").rstrip()
    while s.endswith("）"):  # 文末の括弧書き（入れ子を含む）を外す
        depth, i = 0, len(s) - 1
        while i >= 0:
            if s[i] == "）":
                depth += 1
            elif s[i] == "（":
                depth -= 1
                if depth == 0:
                    break
            i -= 1
        if i < 0:
            break
        s = s[:i].rstrip()
    s = s.rstrip("」』").rstrip()
    return bool(re.search(r"(です|ます|ません|ました|でした|でしょう|ください|ましょう|ですか|ますか|ません)$", s))


def main():
    for n in range(1, 21):
        mod = importlib.import_module(f"q{n:02d}")
        q = mod.Q
        path = next(OUT.glob(f"q{n:02d}-*.md"), None)
        if path is None:
            ng(n, "記事ファイルがない")
            continue
        md = path.read_text(encoding="utf-8")
        # --- コードブロックを外した本文
        body_lines, in_code = [], False
        for ln in md.split("\n"):
            if ln.startswith("```"):
                in_code = not in_code
                continue
            if not in_code:
                body_lines.append(ln)
        body = "\n".join(body_lines)
        code_blocks = re.findall(r"```(?:text)?\n(.*?)```", md, re.S)

        # --- タイトル
        if len(q["catch"]) > 25:
            ng(n, f"キャッチフレーズが25字超（{len(q['catch'])}字）")
        if re.search(r"(ない|する|なる|ある|いる|できる|れる|ぎる|った)$", q["catch"]):
            warn(n, "キャッチフレーズの語尾が常体の言い切りに見える: " + q["catch"])
        title = md.split("\n")[0]
        exp = f"## 【土地家屋調査士受験生向け】直前予想模試 第{n}問{'（改）' if q.get('kaidai') else ''}〜{q['catch']}〜"
        if title != exp:
            ng(n, "タイトル行の形式が違う")

        # --- 問題文
        if len(q["items"]) not in (5, 10):
            ng(n, f"問題文の記述の数が5でも10（対話）でもない: {len(q['items'])}")
        # --- 肢の見出し・たとえば
        marks = [s["mark"] for s in q["sections"]]
        if marks != list("アイウエオ"):
            ng(n, f"肢の見出しの順序: {marks}")
        for s in q["sections"]:
            if not s["tatoeba"].startswith("**たとえば**、"):
                ng(n, f"{s['mark']}: たとえばの書き出しが違う")
            if re.search(r"誤り|正しい|──|正解", s["head"]):
                ng(n, f"{s['mark']}: 見出しに判定語がある: {s['head']}")
            if len(s["head"]) > 50:
                warn(n, f"{s['mark']}: 見出しが長い（{len(s['head'])}字）")
            if "本肢" not in "".join(s["body"]) and "学生" not in "".join(s["body"]):
                warn(n, f"{s['mark']}: 結論文「本肢は誤りです／正しいといえます」がない")
        # --- 文体・段落
        texts = [("導入", pp) for pp in build.split_paragraph(q["intro"])] + [("導入リスト", t) for t in q.get("intro_list", [])] + [("結論", pp) for pp in build.split_paragraph(q["closing"])]
        for s in q["sections"]:
            for i, p in enumerate(s["body"]):
                for pp in build.split_paragraph(p):
                    texts.append((f"{s['mark']}本文{i+1}", pp))
            for pp in build.split_paragraph(s["tatoeba"]):
                texts.append((f"{s['mark']}たとえば", pp))
        for label, t in texts:
            L = len(t)
            if L > 150:
                ng(n, f"{label}: 段落が長い（{L}字）。分ける")
            elif L > 125:
                warn(n, f"{label}: 段落がやや長い（{L}字。1文だけなら可）")
            for sent in sentences(t):
                if not keitai_ok(sent):
                    ng(n, f"{label}: 敬体でない文: 「{sent[:40]}…」")
        # --- 判例・先例・専門誌の番号（確認事項以外）
        sec_text = "\n".join(t for _, t in texts) + "\n".join(x[2] for x in q["summary"])
        for pat in (r"最判|最大決|最決|大判", r"民二|民三|民甲|民事[二三一]", r"号通達|号回答|号通知", r"登記研究", r"[昭平令]\d+\.\d+\.\d+"):
            if re.search(pat, sec_text):
                ng(n, f"本文に判例・先例・専門誌の番号がある: {pat}")
        # --- 括弧・表・肢表記
        if re.search(r"[()]", body.replace("](", "]")) and not re.search(r"https?://", body):
            ng(n, "コードブロックの外に半角括弧がある")
        if re.search(r"^\s*\|.*\|\s*$", body, re.M):
            ng(n, "Markdownの表がある")
        if re.search(r"肢[アイウエオ]", body):
            ng(n, "「肢ア」等の表記がある")
        # --- まとめと正解
        if [m for m, _, _ in q["summary"]] != list("アイウエオ"):
            ng(n, "まとめの肢の並び")
        want = "誤" if "誤っているもの" in q["stem"] else "正"
        got = "".join(m for m, j, _ in q["summary"] if j == want)
        am = re.match(r"(.+?)の組合せ（選択肢(\d)番）", q["answer"])
        if not am:
            ng(n, "正解の書式")
        else:
            letters = am.group(1).replace("・", "")
            if letters != got:
                ng(n, f"正解（{letters}）がまとめの判定（{want}={got}）と合わない")
            m2 = re.search(rf"(\d)　{letters}(?:　|$)", q["choices"])
            if not m2 or int(m2.group(1)) != int(am.group(2)):
                ng(n, "正解の番号が選択肢の並びと合わない")
            if int(am.group(2)) != KEY[n]:
                ng(n, f"正解番号が提供資料の採点基準（{KEY[n]}）と違う")
        if "正解" in sec_text.replace("正解は", "X正解は") and re.search(r"正解は|正解：", sec_text):
            ng(n, "本文に正解の先出しがある")
        # --- 総論インフォグラフィック
        g = q["info"]
        cards = g["cards"]
        if not (4 <= len(cards) <= 6):
            ng(n, f"カードの数が4〜6でない: {len(cards)}")
        for c in cards:
            if len(c["head"]) > 20:
                warn(n, f"カード見出しが20字超（{len(c['head'])}字）: {c['head']}")
            if not (5 <= len(c["tag"]) <= 15):
                ng(n, f"結論タグが5〜15字でない（{len(c['tag'])}字）: {c['tag']}")
            if re.search(r"checkmark|crossed|✕|✓|×|○", c["illus"]):
                warn(n, f"図の説明に○×の語: {c['head']}")
        if "決定木" in md or "判定木" in md or "ツリー" in md:
            ng(n, "禁止語（決定木・判定木・ツリー）")
        ib = code_blocks[0]
        for need in ("Traditional Chinese", "BACKGROUND REQUIREMENT", "Final check before rendering", "CRITICAL TEXT REQUIREMENT",
                     "nothing is rendered below the last card", "GLANCEABLE-POSTER REQUIREMENT"):
            if need not in ib:
                ng(n, f"総論プロンプトに「{need}」がない")
        if f"equals {len(cards)} exactly" not in ib:
            ng(n, "総論プロンプトのカード数の確認文が合わない")
        m = re.search(r"kanji ([^\n]+?) — these", ib.replace("\n", " "))
        kj = set(re.findall(r"[一-鿿]", m.group(1))) if m else set()
        text_part = ib.split("--- HEADER ---")[1] if "--- HEADER ---" in ib else ib
        if not kj <= set(re.findall(r"[一-鿿]", text_part)):
            ng(n, "総論プロンプトの注意漢字に、本文にない字がある")
        if "Subtitle (smaller, centered, 1行):\n直前予想模試" not in ib:
            ng(n, "サブタイトルが直前予想模試の問題番号でない")
        if re.search(r"正しい肢|誤っている肢", ib.split("--- HEADER ---")[1].split("--- COLUMN")[0]):
            ng(n, "サブタイトルに結論がある")
        # --- 見出し画像
        mm = q["midashi"]
        hb = code_blocks[1]
        for field in ("l1", "l2", "sub"):
            if re.search(r"[0-9０-９A-Za-z]", mm[field]):
                ng(n, f"見出し画像の{field}に数字・英字がある: {mm[field]}")
        if len(mm["l1"]) > 16 or len(mm["l2"]) > 16:
            ng(n, f"見出し画像のタイトルが1行16字超: {len(mm['l1'])}/{len(mm['l2'])}")
        if mm["hi"] not in mm["l2"]:
            ng(n, "見出し画像の強調語が2行目にない")
        for need in ("1280x670", "CHARACTERS (critical)", "BACKGROUND REQUIREMENT", "Final check before rendering", "Traditional Chinese"):
            if need not in hb:
                ng(n, f"見出し画像プロンプトに「{need}」がない")
        # --- 見出し画像用フレーズ・確認事項
        if len(q["phrases"]) != 5:
            ng(n, "見出し画像用フレーズが5つでない")
        for p in q["phrases"]:
            if "?" in p:
                ng(n, "フレーズに半角?")
            if len(p) > 26:
                warn(n, f"フレーズが長い（{len(p)}字）: {p}")
        if len(q["kakunin"]) < 4:
            warn(n, "確認事項が少ない")
        if q.get("kaidai") and not q["kaidai"].startswith("※本記事は改題です。"):
            ng(n, "改題の注記の書き出し")
        # --- 区切り線の位置
        if md.count("\n---\n") < 5:
            warn(n, "区切り線が少ない")
        order = [md.find(x) for x in ("### まとめ", "**正解：", "**このまま使える点", "## 見出し画像用フレーズ", "## インフォグラフィック プロンプト（問題全体）", "## 見出し画像 プロンプト")]
        if order != sorted(order) or -1 in order:
            ng(n, "節の順序が違う")

    for line in NG + WARN:
        print(line)
    print(f"\nNG {len(NG)} 件 / WARN {len(WARN)} 件")
    return 1 if NG else 0


if __name__ == "__main__":
    sys.exit(main())
