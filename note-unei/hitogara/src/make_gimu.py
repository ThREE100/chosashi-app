"""第3回「申請の義務がある登記」の数字と図を作る。
1. 不動産登記法 第164条が挙げる申請の義務（項ごと）を、各項の原文で「起算点」「期間」の語が本当にあるか確かめて gimu.json に書く。
2. 第1回の ranking.json から、その条文が440問の解説で何年度出てきたかを足す。
3. 図（起算点ごとの整理、条文ごとの年度数）を note用・Instagram用（1080×1440）で書き出す。
使い方：python3 note-unei/hitogara/src/make_gimu.py <記事フォルダ>
"""
import json, os, re, sys, glob, html
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(HERE))
LAW = open(f"{ROOT}/note-articles/laws/fudousan-touki-hou.md", encoding="utf-8").read().split("\n# 附則")[0]
PN = {1:"",2:"2. ",3:"3. ",4:"4. ",5:"5. ",6:"6. ",7:"7. "}

def jo(a): return f"第{a.replace('の','条の',1)}" if "の" in a else f"第{a}条"

def para(art, p):
    m = re.search(rf"^##### {jo(art)}（[^）]*）\n(.*?)(?=^##### |\Z)", LAW, re.S | re.M)
    assert m, art
    paras, cur = [], []
    for line in m.group(1).strip().split("\n"):
        if re.match(r"^\d+\. ", line): paras.append("\n".join(cur)); cur = [line]
        else: cur.append(line)
    paras.append("\n".join(cur))
    return paras[p-1]

# (条, 項, 期間, 起算点のまとまり, 原文の起算点の語, 誰が, 何を)
ROWS = [
 ("36",1,"一月","所有権の取得の日","その所有権の取得の日から一月以内","新たに生じた土地・表題登記がない土地の所有権を取得した者","土地の表題登記"),
 ("37",1,"一月","変更があった日","その変更があった日から一月以内","表題部所有者・所有権の登記名義人","地目・地積の変更の登記"),
 ("37",2,"一月","後から名義人になった日","更正の登記又は所有権の登記があった日から一月以内","変更の後に表題部所有者・所有権の登記名義人になった者","地目・地積の変更の登記"),
 ("42",1,"一月","滅失の日","その滅失の日から一月以内","表題部所有者・所有権の登記名義人","土地の滅失の登記"),
 ("47",1,"一月","所有権の取得の日","その所有権の取得の日から一月以内","新築した建物・区分建物以外の表題登記がない建物の所有権を取得した者","建物の表題登記"),
 ("49",1,"一月","合体の日","当該合体の日から一月以内","第1項各号に定める者","合体による登記等"),
 ("49",2,"一月","所有権の取得の日","第四十七条並びに前条第一項及び第二項の規定は","いずれも表題登記がない建物が合体したときの所有者など（第47条第1項を準用）","合体後の建物の表題登記"),
 ("49",3,"一月","持分の取得の日","その持分の取得の日から一月以内","合体の後に、表題登記がない建物の所有権に相当する持分を取得した者","合体による登記等"),
 ("49",4,"一月","後から名義人になった日","更正の登記又は所有権の登記があった日から一月以内","合体の後に表題部所有者・所有権の登記名義人になった者","合体による登記等"),
 ("51",1,"一月","変更があった日","当該変更があった日から一月以内","表題部所有者・所有権の登記名義人（共用部分である旨の登記がある建物は所有者）","建物の表題部の変更の登記"),
 ("51",2,"一月","後から名義人になった日","更正の登記又は所有権の登記があった日から一月以内","変更の後に表題部所有者・所有権の登記名義人になった者","建物の表題部の変更の登記"),
 ("51",3,"一月","共用部分である旨の登記がされた日","登記がされた日から一月以内","変更の後に共用部分である旨の登記があった建物の所有者","建物の表題部の変更の登記"),
 ("51",4,"一月","所有権の取得の日","その所有権の取得の日から一月以内","共用部分である旨の登記がある建物を、変更の後に取得した者","建物の表題部の変更の登記"),
 ("57",1,"一月","滅失の日","その滅失の日から一月以内","表題部所有者・所有権の登記名義人（共用部分である旨の登記がある建物は所有者）","建物の滅失の登記"),
 ("58",6,"一月","規約の廃止の日","当該規約の廃止の日から一月以内","共用部分である旨の登記がある建物の所有者","建物の表題登記"),
 ("58",7,"一月","所有権の取得の日","その所有権の取得の日から一月以内","規約の廃止の後に所有権を取得した者","建物の表題登記"),
 ("76の2",1,"三年","知った日","所有権を取得したことを知った日から三年以内","相続（相続人への遺贈を含む）で所有権を取得した者","相続による所有権の移転の登記"),
 ("76の2",2,"三年","遺産の分割の日","当該遺産の分割の日から三年以内","法定相続分での登記の後、遺産の分割で相続分を超えて取得した者","所有権の移転の登記"),
 ("76の3",4,"三年","遺産の分割の日","当該遺産の分割の日から三年以内","相続人である旨の申出をした後、遺産の分割で取得した者","所有権の移転の登記"),
 ("76の5",1,"二年","変更があった日","その変更があった日から二年以内","所有権の登記名義人","氏名・名称・住所の変更の登記"),
]

def build(d):
    t164 = para("164", 1)
    # 第164条第1項が挙げる条・項を確かめる
    for art, p, per, *_ in ROWS:
        if art == "76の5":
            assert "第七十六条の五" in para("164", 2)
    rank = {r["article"]: r for r in json.load(open(f"{HERE}/01-joubun-best10/ranking.json", encoding="utf-8"))["ranking"] if r["law"] == "不動産登記法"}
    out = []
    for art, p, per, grp, phrase, who, what in ROWS:
        txt = para(art, p)
        assert phrase in txt, (art, p, phrase)
        r = rank.get(art)
        out.append(dict(article=art, para=p, period=per, group=grp, who=who, what=what,
                        fine="五万円以下" if art == "76の5" else "十万円以下",
                        years=r["years"] if r else 0, questions=r["questions"] if r else 0))
    arts = []
    for o in out:
        if o["article"] not in arts: arts.append(o["article"])
    by_art = [dict(article=a, years=next(o["years"] for o in out if o["article"] == a)) for a in arts]
    # 義務のない近い条文（比較用）。原文に「一月以内」「三年以内」「二年以内」がないことを確かめる
    none = []
    for a, name in [("38","土地の表題部の更正の登記"),("39","分筆・合筆の登記"),("53","建物の表題部の更正の登記"),("54","建物の分割・区分・合併の登記")]:
        m = re.search(rf"^##### 第{a}条（[^）]*）\n(.*?)(?=^##### )", LAW, re.S | re.M).group(1)
        assert not re.search("一月以内|三年以内|二年以内", m), a
        r = rank.get(a); none.append(dict(article=a, name=name, years=r["years"] if r else 0))
    data = dict(source="不動産登記法 第164条・各条の原文（note-articles/laws/fudousan-touki-hou.md）、年度数は01-joubun-best10/ranking.json",
                duties=out, by_article=by_art, no_duty=none,
                count_total=len(out), count_ikkagetsu=sum(o["period"] == "一月" for o in out))
    json.dump(data, open(f"{d}/gimu.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return data

def shot(doc, out, W, H):
    from playwright.sync_api import sync_playwright
    hp = os.path.splitext(out)[0] + ".html"; open(hp, "w", encoding="utf-8").write(doc)
    with sync_playwright() as p:
        exe = (sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome')) or [None])[0]
        b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H or 800}, device_scale_factor=1)
        pg.goto("file://" + os.path.abspath(hp)); pg.wait_for_timeout(300)
        if H:
            sh = pg.evaluate("document.querySelector('.wrap').scrollHeight")
            if sh > H: print(f"  警告：{os.path.basename(out)} の中身が {sh}px で {H}px に収まらない")
        pg.screenshot(path=out, full_page=not H); b.close()
    print("wrote", out)

CSS = '''body{{margin:0;background:#fbf8f1;font-family:"Noto Sans CJK JP";color:#1f2d3d}}
.wrap{{width:{W}px;{HH}box-sizing:border-box;padding:{pad};display:flex;flex-direction:column}}
h1{{font-size:{h1}px;margin:0 0 8px;line-height:1.3}} .sub{{font-size:{sub}px;color:#55606e;margin-bottom:22px;line-height:1.5}}'''

def fig1(data, out, ig):
    W, H = (1080, 1440) if ig else (1280, None)
    fs = 25 if ig else 24
    groups = []
    for o in data["duties"]:
        if o["period"] != "一月": continue
        g = next((g for g in groups if g[0] == o["group"]), None)
        if not g: g = (o["group"], []); groups.append(g)
        g[1].append(o)
    cards = ""
    for name, items in groups:
        li = "".join(f'<li><b>{jo(o["article"])}{"第"+str(o["para"])+"項" if o["para"]>1 or o["article"] in ("37","47","49","51","58") else ""}</b>　{html.escape(o["what"])}</li>' for o in items)
        cards += f'<div class="card"><div class="k">{html.escape(name)}から</div><ul>{li}</ul></div>'
    other = "".join(f'<li><b>{jo(o["article"])}{"第"+str(o["para"])+"項" if o["article"]!="76の5" else ""}</b>　{html.escape(o["what"])}（{html.escape(o["group"])}から{o["period"]}以内）</li>' for o in data["duties"] if o["period"] != "一月")
    pad = "72px 54px" if ig else "44px 52px"
    css = CSS.format(W=W, HH=f"height:{H}px;" if H else "", pad=pad, h1=fs+20, sub=fs-2)
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:{16 if ig else 14}px;flex:1;align-content:{"stretch" if ig else "start"}}}
.card{{background:#fff;border:2px solid #3b78c2;border-radius:14px;padding:{10 if ig else 12}px 16px}}
.k{{font-size:{fs+2}px;font-weight:700;color:#1d4f91;margin-bottom:4px}}
ul{{margin:0;padding-left:1.1em;font-size:{fs-3}px;line-height:1.45}} li b{{color:#1f2d3d}}
.oth{{margin-top:{14 if ig else 16}px;background:#fff4e6;border:2px solid #e8a05c;border-radius:14px;padding:10px 16px}}
.oth .k{{color:#a8561a}} .foot{{margin-top:12px;font-size:{fs-5}px;color:#55606e;line-height:1.5}}
</style></head><body><div class="wrap"><h1>「一月以内」は、いつから数えるか</h1>
<div class="sub">不動産登記法 第164条が過料の対象に挙げる申請の義務{data["count_total"]}か所のうち、一月以内の{data["count_ikkagetsu"]}か所を起算点で分けた</div>
<div class="grid">{cards}</div>
<div class="oth"><div class="k">一月ではないもの（権利の登記）</div><ul>{other}</ul></div>
<div class="foot">怠ったときは十万円以下の過料（第164条第1項）。ただし第76条の5だけは五万円以下（同条第2項）。第49条第2項は第47条第1項の準用。</div>
</div></body></html>'''
    shot(doc, out, W, H)

def fig2(data, out, ig):
    W, H = (1080, 1440) if ig else (1280, None)
    fs = 30 if ig else 27
    rows = data["by_article"] + [dict(article=n["article"], years=n["years"], none=n["name"]) for n in data["no_duty"]]
    rows = sorted(data["by_article"], key=lambda r: -r["years"]) + sorted([dict(article=n["article"], years=n["years"], none=True) for n in data["no_duty"]], key=lambda r: -r["years"])
    body = ""
    for r in rows:
        c = "#b9b2a4" if r.get("none") else "#3b78c2"
        body += f'''<div class="row"><div class="nm">{jo(r["article"])}{"<small>（義務なし）</small>" if r.get("none") else ""}</div>
<div class="bw"><div class="bar" style="width:{r["years"]/22*100:.1f}%;background:{c}"></div></div><div class="v"><b>{r["years"]}</b>年度</div></div>'''
    pad = "72px 54px" if ig else "44px 52px"
    css = CSS.format(W=W, HH=f"height:{H}px;" if H else "", pad=pad, h1=fs+14, sub=fs-5)
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}
.rows{{flex:1;display:flex;flex-direction:column;justify-content:space-around}}
.row{{display:flex;align-items:center;gap:14px;margin:6px 0}}
.nm{{width:{300 if ig else 300}px;font-size:{fs}px;font-weight:700;flex:none}} .nm small{{font-size:{fs-8}px;color:#7a7266;font-weight:400}}
.bw{{flex:1;height:{30 if ig else 28}px;background:#eee8dc;border-radius:8px;position:relative}} .bar{{height:100%;border-radius:8px}}
.v{{width:120px;text-align:right;font-size:{fs-4}px;flex:none}} .v b{{font-size:{fs+2}px}}
.foot{{margin-top:18px;font-size:{fs-9}px;color:#55606e;line-height:1.6}}
</style></head><body><div class="wrap"><h1>申請の義務がある条文は、どれだけ出てきたか</h1>
<div class="sub">平成17年度〜令和8年度の択一式440問の解説で、根拠に引いた年度の数（22年度中）</div>
<div class="rows">{body}</div>
<div class="foot">青＝第164条が挙げる申請の義務がある条文（不動産登記法）。灰色＝比べるために並べた、申請の義務がない近い条文。数え方は第1回と同じ（法令名つきの引用だけ。1問で何度出ても1回）。第58条は共用部分である旨の登記そのものの解説を含む。</div>
</div></body></html>'''
    shot(doc, out, W, H)

if __name__ == "__main__":
    d = sys.argv[1]
    data = build(d)
    fig1(data, f"{d}/zu01_kisanten_note.png", False); fig1(data, f"{d}/zu01_kisanten_ig.png", True)
    fig2(data, f"{d}/zu02_nendo_note.png", False); fig2(data, f"{d}/zu02_nendo_ig.png", True)
