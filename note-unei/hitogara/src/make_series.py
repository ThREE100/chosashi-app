"""第4回〜第12回の数字（data.json）と本文の図を作る。数えた結果はすべてここに残す（手で数えない）。
使い方：python3 note-unei/hitogara/src/make_series.py [番号 ...]（省くと全部）。--nofig で図を作らない。
各回の data.json の "sources" は、本文の事実の出どころ（ファイルと、そこにあるはずの文字列）。check.py がその文字列が本当にあるかを確かめる。
"""
import os, re, sys, glob, json, collections, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from count_articles import PAT, LAWS, NAME, Z, YEARS, body as art_body
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(HERE))
E = html.escape
NOFIG = "--nofig" in sys.argv
KY = ["H20","H21","H22","H23","H24","H25","H26","H27","H28","H29","H30","R1","R2","R3","R4","R5","R6","R7","R8"]
def jp_year(y):
    if y == "R1": return "令和元年度"
    return ("平成" if y[0] == "H" else "令和") + y[1:] + "年度"
def rd(p): return open(f"{ROOT}/{p}", encoding="utf-8").read()
def save(d, data):
    os.makedirs(f"{HERE}/{d}", exist_ok=True)
    json.dump(data, open(f"{HERE}/{d}/data.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", d, "data.json")
def figs(fn, d, name, *a, **k):
    if NOFIG: return
    fs_ig = k.pop("fs_ig", None)
    fn(f"{HERE}/{d}/{name}_note.png", False, *a, **k)
    if fs_ig: k["fs"] = fs_ig
    fn(f"{HERE}/{d}/{name}_ig.png", True, *a, **k)

# ---------- 第4回：第22問（建物）19年度 ----------
Q22 = [  # 年度, 登記の目的（答案に書くもの。記事の本文にある語で書く）, 区分建物の登記か, 専有部分の床面積（内法）を扱うか
 ("H20", ["建物区分登記"], True, True), ("H21", ["建物表題登記"], False, False),
 ("H22", ["建物表題部変更登記", "合体による登記等"], True, False), ("H23", ["建物表題部変更登記"], True, True),
 ("H24", ["区分建物表題登記"], True, True), ("H25", ["建物表題部変更登記", "建物表題登記"], False, False),
 ("H26", ["区分建物表題部変更登記", "建物表題登記", "建物表題部変更・合併登記"], True, False),
 ("H27", ["建物区分登記"], True, True), ("H28", ["建物表題部変更登記"], False, False),
 ("H29", ["建物分割登記", "建物表題部変更登記"], False, False), ("H30", ["合体による登記等"], False, False),
 ("R1", ["区分建物表題登記", "区分建物表題部変更登記"], True, True), ("R2", ["建物滅失登記", "建物表題登記"], False, False),
 ("R3", ["建物区分登記", "区分建物区分登記"], True, True), ("R4", ["建物表題部変更登記"], False, False),
 ("R5", ["区分建物表題部変更・合併登記"], True, True), ("R6", ["建物表題登記"], False, False),
 ("R7", ["建物表題部変更登記"], False, False), ("R8", ["区分建物区分登記"], True, True)]
def q22path(y): return f"note-articles-Kijyutsu/{y}/Q22/note_{y}_dai22mon_tatemono_kaisetsu.md"
def d04():
    d = "04-dai22mon-19nenbun"; rows = []; src = []
    for y, moku, kubun, uchi in Q22:
        t = rd(q22path(y)); title = re.search(r"^# (.*)$", t, re.M).group(1)
        sub = re.search(r"〜(.*)〜", title).group(1)
        for m in moku:
            assert m in t, (y, m); src.append({"file": q22path(y), "text": m})
        if uchi: assert "内法" in t, y
        for w in ("登記の目的", "床面積", "建物図面", "所在"): assert w in t, (y, w)
        src.append({"file": q22path(y), "text": sub})
        rows.append({"year": y, "nendo": jp_year(y), "mokuteki": moku, "kubun": kubun, "uchinori": uchi, "subtitle": sub})
    kinds = collections.Counter(m for r in rows for m in r["mokuteki"])
    data = {"years": len(rows), "rows": rows, "kinds": kinds.most_common(), "kubun_years": sum(r["kubun"] for r in rows),
            "uchinori_years": sum(r["uchinori"] for r in rows),
            "multi_years": [r["year"] for r in rows if len(r["mokuteki"]) >= 2],
            "janai_years": [r["year"] for r in rows if re.search(r"じゃない|じゃなく", r["subtitle"])], "sources": src}
    save(d, data)
    from hlib import table_fig, bar_fig
    trs = [[f"<b>{r['nendo']}</b>", "<br>".join(E(m) for m in r["mokuteki"]), "○" if r["kubun"] else "", E(r["subtitle"])] for r in rows]
    figs(table_fig, d, "zu01_nenbetsu", "第22問（建物）は、毎年何の登記を書かせてきたか",
         f"このnoteの記述式の解説（平成20年度〜令和8年度の{len(rows)}年度）から、答案に書く登記の目的を並べた",
         ["年度", "登記の目的", "区分建物", "記事の副題（そこで問われた判断）"], trs,
         foot=f"区分建物の欄の○＝区分建物の登記を書かせた年度（{data['kubun_years']}年度）。合体による登記等の正式な目的は長いので略した。",
         hl=[i for i, r in enumerate(rows) if r["kubun"]], fs=17, fs_ig=19)
    figs(bar_fig, d, "zu02_mokuteki", "登記の目的ごとの年度の数",
         f"{len(rows)}年度で、同じ登記の目的が何年度に出てきたか（1年度に2つ以上書かせた年は、それぞれ数えた）",
         [(k, "", v, "#3b78c2" if "区分" not in k else "#e8a05c") for k, v in kinds.most_common()], max(kinds.values()), "年度",
         foot="青＝区分建物以外の建物の登記、橙＝区分建物・区分に関わる登記。", nmw=420)
    return data

# ---------- 第5回：年末年始に読み返す10本 ----------
def qpath(q):
    y, n = q.split("-"); y = y.lower()
    return glob.glob(f"{ROOT}/note-articles/{y}-mondai/q{n[1:]}-*.md")[0]
def d05():
    d = "05-nenmatsu-yomikaeshi-10"
    rank = json.load(open(f"{HERE}/01-joubun-best10/ranking.json", encoding="utf-8"))["ranking"][:10]
    hold = set(re.findall(r"^- ((?:H|R)\d+)_q(\d+)", open(f"{ROOT}/tools/drill/REVIEW_HOLD.md", encoding="utf-8").read(), re.M))
    hold = {f"{y.replace('R0','R')}-Q{n}" for y, n in hold}   # 一問一答で根拠が弱いとして保留・要確認にしている問は選ばない
    picks = []; src = []
    for i, r in enumerate(rank, 1):
        best = None
        for q in r["question_list"]:
            if q in hold: continue
            p = qpath(q); t = open(p, encoding="utf-8").read(); b = art_body(t)
            n = sum(1 for m in PAT.finditer(b) if NAME[dict(LAWS)[m.group(1)]] == r["law"] and
                    m.group(2).translate(Z) + ("の" + m.group(3).translate(Z) if m.group(3) else "") == r["article"])
            key = (n, q[:1] == "R", q)   # 引用の回数が多い問→同じなら令和→新しい年度
            if best is None or key > best[0]: best = (key, q, p, t)
        (n, _, _), q, p, t = best
        title = re.search(r"^##? (【.*)$", t, re.M).group(1)
        rel = os.path.relpath(p, ROOT)
        picks.append({"rank": i, "law": r["law"], "article": r["article"], "years": r["years"], "q": q, "cites": n, "title": title, "file": rel})
        src.append({"file": rel, "text": title})
    data = {"picks": picks, "rule": "その条文を法令名つきで引いた回数がいちばん多い問（同じなら令和の問、さらに同じなら新しい年度）。一問一答で根拠が弱いとして要確認にしている問（tools/drill/REVIEW_HOLD.md）は除く", "excluded": sorted(hold), "sources": src}
    save(d, data)
    from hlib import table_fig
    def short(t): return re.sub(r"^【[^】]*】", "", t)
    trs = [[f"<b>{x['rank']}</b>", E(f"{x['law']} 第{x['article'].replace('の','条の',1) if 'の' in x['article'] else x['article']}" + ("" if "の" in x["article"] else "条")), E(short(x["title"]))] for x in picks]
    figs(table_fig, d, "zu01_10hon", "条文ベスト10から選んだ、年末年始に読み返す10本",
         "第1回のベスト10の条文ごとに、その条文をいちばん多く引いた解説の問を1本ずつ選んだ",
         ["順位", "条文", "読み返す記事"], trs, foot="選び方：法令名つきの引用の回数がいちばん多い問。同じ回数なら令和の問、さらに同じなら新しい年度。記事が根拠の弱さを注記している問は除いた。", fs=19)
    return data


# ---------- 第6回：毎朝ドリルの作り方（ひっかけの型） ----------
def d06():
    d = "06-drill-no-tsukurikata"
    tx = json.load(open(f"{ROOT}/daily-drill/taxonomy.json", encoding="utf-8"))
    rg = json.load(open(f"{ROOT}/daily-drill/registry.json", encoding="utf-8"))
    am = [v for k, v in rg.items() if v["side"] == "morning"]; pm = [v for k, v in rg.items() if v["side"] != "morning"]
    traps = collections.Counter(t for v in am for t in v["traps"])
    arts = collections.Counter(a for v in am for a in v.get("articles", []))
    data = {"morning": len(am), "evening": len(pm),
            "traps": [{"id": k, "name": tx["traps_morning"][k], "count": traps[k]} for k in sorted(tx["traps_morning"], key=lambda k: -traps[k])],
            "fields": collections.Counter(v["field"] for v in am).most_common(), "styles": collections.Counter(v["style"] for v in am).most_common(),
            "levels": collections.Counter(v["level"] for v in am).most_common(), "traps_per_q": sorted(collections.Counter(len(v["traps"]) for v in am).items()),
            "articles_distinct": len(arts),
            "sources": [{"file": "daily-drill/RULES.md", "text": "誤り肢は、**条文の言葉を1か所だけ変える**"},
                        {"file": "daily-drill/RULES.md", "text": "**条文は原文で確認**"},
                        {"file": "daily-drill/RULES.md", "text": "過去問の出典・年度は問題・解説に入れない"}]}
    for t in data["traps"]: data["sources"].append({"file": "daily-drill/taxonomy.json", "text": t["name"]})
    save(d, data)
    from hlib import bar_fig
    figs(bar_fig, d, "zu01_hikkake", "朝の択一120問に使った、ひっかけの型",
         f"毎朝ドリルの朝の択一{len(am)}問で、誤りの肢を作るときに使った型の数（1問に2〜5個。登録簿から数えた）",
         [(t["name"], t["id"], t["count"], "#3b78c2") for t in data["traps"]], max(traps.values()), "問",
         foot="同じ問で同じ型を2つの肢に使っても1と数えた。M9は欠番。", nmw=470)
    return data

# ---------- 第7回：法改正で正誤が変わった肢 ----------
KAISEI = [  # 年度・問・肢, 何が変わったか, 改正, 出題当時→現行, 記事のファイル, 記事にある文字列
 ("平成17年度 第20問 ウ", "事件簿の保存期間", "土地家屋調査士法施行規則 第28条第2項（今は閉鎖後七年間）", "正しい → 誤り",
  "note-articles/h17-mondai/q20-chousashi-houjin.md", "事件簿は、閉鎖後5年間ではなく7年間保存しなければならない"),
 ("平成19年度 第12問 オ", "共有地の分筆を申請できる共有者", "令和5年4月1日施行の民法改正（共有物の変更・管理は持分の価格の過半数）", "誤り → 正しい",
  "note-articles/h19-mondai/q12-bunpitsu.md", "（出題当時は誤り）"),
 ("平成21年度 第20問", "未成年者は調査士になれない（成年の年齢）", "令和4年4月1日施行の民法改正（成年は十八歳）", "改題（判定の日を移した）",
  "note-articles/h21-mondai/q20-kekkaku-jiyuu.md", "判定の日を令和8年4月1日に移したため"),
 ("平成29年度 第20問 オ", "調査士法人を1人で設立できるか", "令和2年の土地家屋調査士法改正", "誤り → 正しい",
  "note-articles/h29-mondai/q20-chousashi-houjin.md", "出題当時は誤り・現行法では正しいという形で結論が反転します"),
 ("令和2年度 第5問 ア", "法定相続情報番号だけで、相続を証する情報に代えられるか", "令和6年4月1日施行の不動産登記規則の改正（第37条の3第1項）", "誤り → 正しい",
  "note-articles/r2-mondai/q05-houtei-souzoku-jouhou.md", "出題当時と結論が変わっています"),
]
ONAJI = [  # 言葉・条番号は変わったが、正誤は変わらない
 ("平成22年度 第20問", "「身体又は精神の衰弱」→「心身の故障」", "note-articles/h22-mondai/q20-chousashi-touroku.md", "結論自体は変わりません"),
 ("平成23年度 第3問", "保存行為の根拠が民法第252条ただし書→同条第5項", "note-articles/h23-mondai/q03-kyouyu.md", "同条5項に移っています"),
 ("平成25年度 第20問", "「懲役」→「拘禁刑」", "note-articles/h25-mondai/q20-chousashihou.md", "正誤判定・正解番号自体は変わらない"),
 ("平成28年度 第1問", "時効の「中断」→「更新」「完成猶予」（問題文を改めた）", "note-articles/h28-mondai/q01-shoumetsujikou.md", "改題（エ）"),
 ("令和3年度 第11問", "「相続財産管理人」→「相続財産清算人」", "note-articles/r3-mondai/q11-bunpitsu.md", "結論自体には影響しません"),
]
def d07():
    d = "07-houkaisei-de-kawatta-shi"
    hold = set(re.findall(r"^- ((?:H|R)\d+_q\d+)", rd("tools/drill/REVIEW_HOLD.md"), re.M))
    src = []
    for *_, f, t in KAISEI: assert t in rd(f), (f, t); src.append({"file": f, "text": t})
    for *_, f, t in ONAJI: assert t in rd(f), (f, t); src.append({"file": f, "text": t})
    assert "閉鎖後七年間" in rd("note-articles/laws/chousashi-hou-sekourule.md"); src.append({"file": "note-articles/laws/chousashi-hou-sekourule.md", "text": "閉鎖後七年間"})
    assert "年齢十八歳をもって、成年とする。" in rd("note-articles/laws/minpou-1-soukyoku-bukken.md")
    src.append({"file": "note-articles/laws/minpou-1-soukyoku-bukken.md", "text": "年齢十八歳をもって、成年とする。"})
    src.append({"file": "note-articles/laws/chousashi-hou.md", "text": "心身の故障により業務を行うことができないとき"})
    data = {"kawatta": [dict(zip(["q", "what", "law", "change", "file"], k[:5])) for k in KAISEI],
            "onaji": [dict(zip(["q", "what", "file"], k[:3])) for k in ONAJI],
            "hold_count": len(hold), "sources": src}
    save(d, data)
    from hlib import cards_fig
    c1 = [(k[0], [f"<b>{E(k[1])}</b>", E(k[2]), "出題当時 → 今：" + E(k[3])], "o") for k in KAISEI]
    c2 = [("正誤は同じ。言葉や条番号だけが変わった", [f"{E(k[0])}：{E(k[1])}" for k in ONAJI], "g")]
    figs(cards_fig, d, "zu01_kawatta", "法改正で、昔の過去問の答えが変わった肢",
         "このnoteの解説で、出題当時と今の法令で正誤が変わる（または問題を改めた）と書いた肢", c1 + c2,
         foot="どの記事も、正誤は今の法令で判断し、出題当時の扱いを注に書いている。", cols="1fr", fs=20, fs_ig=23)
    return data

# ---------- 第8回：令和9年度に向けて最初の1か月 ----------
def d08():
    d = "08-saisho-no-ikkagetsu"
    n_q = len([f for y in YEARS for f in glob.glob(f"{ROOT}/note-articles/{y}-mondai/q[0-9][0-9]-*.md")])
    n21 = len(glob.glob(f"{ROOT}/note-articles-Kijyutsu/*/Q21/note_*_kaiwa_kaisetsu.md"))
    n22 = len(glob.glob(f"{ROOT}/note-articles-Kijyutsu/*/Q22/note_*_tatemono_kaisetsu.md"))
    items = json.load(open(f"{ROOT}/tools/drill/data/items.json", encoding="utf-8"))
    items = items["items"] if isinstance(items, dict) else items
    rg = json.load(open(f"{ROOT}/daily-drill/registry.json", encoding="utf-8"))
    law = rd("note-articles/laws/chousashi-hou.md")
    for t in ["筆記試験に合格した者次回の第一項の試験の筆記試験及びその後に行われる第一項の試験における前号に定める筆記試験",
              "口述試験は、筆記試験に合格した者につき、前項第二号に掲げる事項に関する知識について行う。"]:
        assert t in law
    data = {"takuitsu_q": n_q, "q21": n21, "q22": n22, "ichimon": len(items),
            "asa": sum(1 for v in rg.values() if v["side"] == "morning"), "yoru": sum(1 for v in rg.values() if v["side"] != "morning"),
            "sources": [{"file": "note-articles/laws/chousashi-hou.md", "text": "筆記試験に合格した者次回の第一項の試験の筆記試験"},
                        {"file": "note-articles/laws/chousashi-hou.md", "text": "口述試験は、筆記試験に合格した者につき"}]}
    save(d, data)
    from hlib import cards_fig
    weeks = [("1週目：条文の地図を持つ", ["条文ベスト10（第1回）と11〜32位（第2回）を読む", "申請の義務と起算点（第3回）を1枚にまとめる"], ""),
             ("2週目：択一を年度で1周", [f"令和8年度の20問から。全{n_q}問の中の最新の年度", "間違えた肢は、その条文の原文に戻る"], ""),
             ("3週目：記述式の型を知る", [f"第22問（建物）は登記の目的の並び（第4回）", f"第21問（土地）は座標の5つの型（第9回）"], ""),
             ("4週目：毎日の型を作る", ["朝に択一1問、夜に記述式を15分", "解けなかった論点をメモに残す"], "")]
    figs(cards_fig, d, "zu01_4shuukan", "令和9年度に向けた、最初の4週間",
         "このnoteの記事と毎朝ドリルを使った、最初の1か月の進め方の例", weeks,
         foot="進め方は一つの例です。自分の弱い所から入れ替えてください。", fs=22, fs_ig=26)
    return data

# ---------- 第9回：第21問の座標計算は5つの型 ----------
def d09():
    d = "09-dai21mon-5tsu-no-kata"
    p = "note-articles-Kijyutsu/R8/Q21/note_R8_dai21mon_tochi_kaiwa_kaisetsu.md"
    t = rd(p)
    blk = t[t.index("第21問で座標が省略された点の決め方は"):]
    types = []
    for m in re.finditer(r"^- \*\*(.+?)\*\*：(.+)$", blk[:blk.index("**藍子**")], re.M):
        ex = [x.strip() for x in re.split(r"、(?=(?:令和|平成))", m.group(2))]
        types.append({"name": m.group(1), "examples": ex})
    assert len(types) == 5, types
    data = {"types": types, "examples": sum(len(x["examples"]) for x in types),
            "sources": [{"file": p, "text": x["name"]} for x in types] + [{"file": p, "text": "ほとんどがこの5つの型か、その組み合わせ"},
                {"file": p, "text": "①その点について書いた文を全部抜き出す、②図形の言葉に訳す、③条件を2つそろえる（足りなければ芋づるで先の点を出す）、④図を大きく描いて線を延ばし、補助線を引く、⑤5つの型のどれか、その組み合わせかを当てる、⑥見当をつけてから計算して、検算する"},
                {"file": p, "text": "ひねりがわなになる"},
                {"file": p, "text": "K ＝ J ＋ (L − J) × t"},
                {"file": "note-articles-Kijyutsu/H24/Q21/note_H24_dai21mon_tochi_kaiwa_kaisetsu.md", "text": "K ＝ J ＋ (J − I) ÷ Abs(J − I) × 0.65"},
                {"file": "note-articles-Kijyutsu/H29/Q21/note_H29_dai21mon_tochi_kaiwa_kaisetsu.md", "text": "1.00∠( arg(G − F) ＋ 90° )"},
                {"file": "note-articles-Kijyutsu/R1/Q21/note_R1_dai21mon_tochi_kaiwa_kaisetsu.md", "text": "G ＝ F ＋ (H − F) × ( w ＋ Conjg(w) ) ÷ 2"},
                {"file": "note-articles-Kijyutsu/H21/Q21/note_H21_dai21mon_tochi_kaiwa_kaisetsu.md", "text": "相似比"}]}
    save(d, data)
    from hlib import cards_fig
    cards = [(x["name"], [E(e) for e in x["examples"]], "") for x in types]
    figs(cards_fig, d, "zu01_5tsu", "座標が省略された点は、5つの型で決まる",
         "第21問（土地）で、問題文に座標がない点をどう決めたか。令和8年度の解説にまとめた過去の例", cards,
         foot="1つの点に2つの型が組み合わさることもある（例：令和8年度のL点は「直線上で決まった距離」に「軸方向」のひねり）。", fs=20, fs_ig=23)
    return data

# ---------- 第10回：関数電卓のキー操作を数える ----------
def keycount(path):
    lines = rd(path).splitlines(); blocks = []; inb = False; buf = []
    for l in lines:
        if l.strip().startswith("```"):
            if inb:
                s = " ".join(buf)
                if any(k in s for k in ("[ALPHA]", "[SHIFT]", "[=]")): blocks.append(s)
                buf = []
            inb = not inb; continue
        if inb: buf.append(l)
    keys = collections.Counter(); total = 0
    for s in blocks:
        for tk in re.findall(r"\[[^\]]+\]|[0-9]+(?:\.[0-9]+)?", s):
            if tk.startswith("["): keys[tk] += 1; total += 1
            else: keys["数字・小数点"] += len(tk); total += len(tk)
    return len(blocks), total, keys
def d10():
    d = "10-dentaku-key-kazoeru"
    rows = []; allk = collections.Counter(); src = []
    for y in KY:
        p = f"note-articles-Kijyutsu/{y}/Q21/note_{y}_dai21mon_tochi_kaiwa_kaisetsu.md"
        nb, tot, k = keycount(p); allk += k
        rows.append({"year": y, "nendo": jp_year(y), "blocks": nb, "keys": tot, "disp": rd(p).count("\n表示：")})
        src.append({"file": p, "text": "表示："})
    tot = sum(r["keys"] for r in rows); nb = sum(r["blocks"] for r in rows)
    data = {"rows": rows, "total_keys": tot, "total_blocks": nb, "avg_per_block": round(tot / nb, 1),
            "top_keys": allk.most_common(12), "sources": src}
    save(d, data)
    from hlib import bar_fig
    figs(bar_fig, d, "zu01_nendo", "第21問の解説に書いたキー操作の数（年度ごと）",
         f"会話形式の解説{len(rows)}年度分の、電卓操作のブロックのキーを数えた（数字は1けた＝1キー。別解・検算も含む）",
         [(r["nendo"], f"{r['blocks']}ブロック", r["keys"], "#3b78c2") for r in rows], max(r["keys"] for r in rows), "キー",
         foot=f"合計 {tot} キー・{nb} ブロック（1ブロック平均 {round(tot/nb,1)} キー）。電卓は記事で使っている関数電卓の複素数モード。", fs=19, fs_ig=21, nmw=330)
    top = [(k, "", v, "#e8a05c" if k == "数字・小数点" else "#3b78c2") for k, v in allk.most_common(10)]
    figs(bar_fig, d, "zu02_key", "いちばん押したキー", f"{len(rows)}年度分の合計で、多く押したキーの上位10",
         top, top[0][2], "回", foot="［ALPHA］はメモリの呼び出し、［SHIFT］［STO］はメモリへの記憶、［Apps］は複素数の関数（arg・Conjg）を呼ぶキー。", fs=21, fs_ig=24, nmw=300)
    return data

# ---------- 第11回：似ている用語の取り違え ----------
PAIRS = [  # (表示名A, 表示名B, Aの正規表現, Bの正規表現)。いつも一緒に出す組（建物図面と各階平面図など）は取り違えではないので入れない
 ("変更", "更正", r"変更の登記|表題部の変更", r"更正の登記|表題部の更正"),
 ("合体", "合併", r"合体", r"合併"),
 ("分筆", "合筆", r"分筆", r"合筆"),
 ("建物の分割", "建物の区分", r"建物の分割|分割の登記|建物分割", r"建物の区分|区分の登記|建物区分"),
 ("滅失", "取壊し", r"滅失", r"取壊し|取り壊"),
 ("表題登記", "所有権の保存の登記", r"表題登記", r"所有権の保存|所有権保存"),
 ("表題部所有者", "所有権の登記名義人", r"表題部所有者", r"所有権の登記名義人"),
 ("地図", "地図に準ずる図面", r"地図(?!に準ずる)", r"地図に準ずる図面"),
 ("地積測量図", "土地所在図", r"地積測量図", r"土地所在図"),
 ("敷地権", "敷地利用権", r"敷地権", r"敷地利用権"),
 ("法定敷地", "規約敷地", r"法定敷地", r"規約敷地"),
 ("法定共用部分", "規約共用部分", r"法定共用部分", r"規約共用部分"),
 ("筆界", "所有権の境", r"筆界", r"所有権界|所有権の範囲"),
 ("登記識別情報", "登記済証", r"登記識別情報", r"登記済証"),
 ("代位", "代理", r"代位", r"代理"),
 ("壁心", "内法", r"壁心|壁その他の区画の中心", r"内法|内側線"),
]
def d11():
    d = "11-niteiru-yougo-best10"
    arts = []
    for y in YEARS:
        for f in sorted(glob.glob(f"{ROOT}/note-articles/{y}-mondai/q[0-9][0-9]-*.md")):
            arts.append((y, art_body(open(f, encoding="utf-8").read())))
    rows = []
    for a, b, ra, rb in PAIRS:
        qs = [y for y, t in arts if re.search(ra, t) and re.search(rb, t)]
        rows.append({"a": a, "b": b, "questions": len(qs), "years": len(set(qs))})
    rows.sort(key=lambda r: (-r["questions"], -r["years"]))
    data = {"questions_total": len(arts), "pairs": rows, "top10": rows[:10],
            "rule": "同じ問の解説の本文に、AとBの両方の語が出てくる問の数（1問で何度出ても1）",
            "sources": [{"file": "note-articles/topics/zukai-kikaku/02-taihi-zukan.md", "text": "合体は事実、合併は手続"}]}
    save(d, data)
    from hlib import bar_fig
    figs(bar_fig, d, "zu01_pair", "同じ問の解説に並んで出てくる、似ている用語ベスト10",
         f"択一式{len(arts)}問の解説で、2つの用語が両方出てくる問の数",
         [(f"{r['a']}／{r['b']}", f"{r['years']}年度", r["questions"], "#3b78c2") for r in rows[:10]], rows[0]["questions"], "問",
         foot="同じ解説に両方が出る＝並べて比べられることが多い組。数え方は本文のとおり（語の拾い方で数は少し変わる）。", fs=21, fs_ig=24, nmw=430)
    return data

# ---------- 第12回：測量士補から調査士へ ----------
SOKURYOU = [("不動産登記事務取扱手続準則", "82", "建物の床面積の定め方"), ("不動産登記法", "123", "定義（筆界など）"),
            ("不動産登記法", "14", "地図等"), ("不動産登記規則", "10", "地図（縮尺・精度区分）"),
            ("不動産登記規則", "77", "地積測量図の内容"), ("不動産登記事務取扱手続準則", "72", "分筆の登記の申請（地積の誤差）")]
def d12():
    d = "12-sokuryoushiho-kara"
    law = rd("note-articles/laws/chousashi-hou.md")
    for t in ["一　土地及び家屋の調査及び測量", "二　申請手続及び審査請求の手続",
              "一　測量士若しくは測量士補又は一級建築士若しくは二級建築士となる資格を有する者第三項第一号に掲げる事項についての筆記試験"]:
        assert t in law, t
    rank = {(r["law"], r["article"]): (i, r) for i, r in enumerate(json.load(open(f"{HERE}/01-joubun-best10/ranking.json", encoding="utf-8"))["ranking"], 1)}
    pick = []
    for lw, a, nm in SOKURYOU:
        i, r = rank[(lw, a)]; pick.append({"law": lw, "article": a, "name": nm, "rank": i, "years": r["years"]})
    data = {"picks": pick, "sources": [{"file": "note-articles/laws/chousashi-hou.md", "text": "測量士若しくは測量士補又は一級建築士若しくは二級建築士となる資格を有する者"},
                                         {"file": "note-articles/laws/chousashi-hou.md", "text": "一　土地及び家屋の調査及び測量"},
                                         {"file": "note-articles/laws/fudousan-touki-kisoku-1.md", "text": "精度区分"}]}
    save(d, data)
    from hlib import table_fig
    trs = [[E(f"{x['law']} 第{x['article']}条"), E(x["name"]), f"{x['rank']}位", f"{x['years']}年度"] for x in pick]
    figs(table_fig, d, "zu01_joubun", "測量の知識がつながる、最初に読む6つの条文",
         "第1回・第2回の条文ランキング（択一式440問の解説で根拠に引いた年度の数）から、測量・図面・床面積の条文を選んだ",
         ["条文", "中身", "順位", "年度の数（22年度中）"], trs, foot="順位は第1回の数え方（法令名つきの引用だけ）による。", fs=21, fs_ig=24)
    return data
if __name__ == "__main__":
    want = [a for a in sys.argv[1:] if not a.startswith("--")]
    for k, f in sorted(globals().items()):
        if re.fullmatch(r"d\d\d", k) and (not want or k[1:] in want): f()
