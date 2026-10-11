#!/usr/bin/env python3
"""記述式解説漫画のページ構成表（JSON）の機械チェック。4コマの check_prompt.py の長編版（パイロット）。
使い方: python3 tools/drill/manga/kijutsu_pilot/check_pages.py <page_spec.json>
NG があれば終了コード1。WARN は目視で判断する。"""
import json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
ng, warn = [], []
def NG(m): ng.append(m)
def WARN(m): warn.append(m)
def norm(s): return re.sub(r"\s+", "", s)

def main():
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf8"))
    art = (ROOT / spec["meta"]["article"]).read_text(encoding="utf8"); art_n = norm(art)
    ch = re.search(r"^## 第2章：.*?(?=^## 第3章)", art, re.S | re.M).group(0); ch_n = norm(ch)
    pages = spec["pages"]; H = spec["global"]["canvas"]["h"]
    EMO = set(spec["global"]["emotion_ids"]); MODES = {"FULL", "MID", "SMALL", "FACES"}
    ids = [p["page_id"] for p in pages]
    if len(set(ids)) != len(ids): NG("page_id が重複している")

    seen_bub = {}   # turn -> [番号...]（ページ順）
    markers = []
    all_text = []
    for pi, p in enumerate(pages):
        pid = p["page_id"]; zs = p["zones"]
        # C01 区画の連続と合計
        y = 0
        for z in zs:
            if z["y"] != y: NG(f"{pid}/{z['zone_id']}: 区画が前の区画の下端（y={y}）から始まっていない（y={z['y']}）")
            y = z["y"] + z["h"]
        if y != H: NG(f"{pid}: 区画の高さの合計が{H}pxでない（{y}）")
        for z in zs:
            zid = f"{pid}/{z['zone_id']}"
            # C02 図の枠
            if z["type"] == "figure":
                f = spec["figures"].get(z.get("figure_ref"))
                if not f: NG(f"{zid}: figure_ref が figures にない"); continue
                if not (ROOT / f["file"]).exists(): NG(f"{zid}: 図のファイルが実在しない: {f['file']}")
                fr = z["frame"]; fw, fh = f["size"]
                if abs(fr["w"] / fr["h"] - fw / fh) > 0.01: NG(f"{zid}: 図の枠の縦横比が図と違う（{fr['w']}×{fr['h']} と {fw}×{fh}）")
                if fr["w"] < 900: NG(f"{zid}: 図の枠の幅が900px未満（文字が小さくなる）")
                if not (z["y"] <= fr["y"] and fr["y"] + fr["h"] <= z["y"] + z["h"]): NG(f"{zid}: 図の枠が区画からはみ出している")
                if z.get("fit") != "contain": NG(f"{zid}: fit が contain でない（図を切らない）")
                markers.append((pi, f["marker_index"]))
            # カード・帯の文言（C15）と、電卓操作（C16）
            for ln in z.get("card_lines", []) + ([z["text"]] if z.get("text") else []):
                all_text.append(ln)
                if norm(ln) not in art_n: NG(f"{zid}: カードの文言が記事にない（記事の文言の一部にする）: 「{ln}」")
                if re.search(r"\[(ALPHA|SHIFT|STO|Apps|∠|=|MODE|°′″)\]", ln): NG(f"{zid}: 電卓のキー操作が入っている: {ln}")
            if z.get("fit") and "frame" in z and z["type"] != "figure": pass
            if z.get("red_parts") and z["type"] != "wrong_card": NG(f"{zid}: 赤は誤り・訂正のカード（wrong_card）だけに使う")
            for rp in z.get("red_parts", []):
                if rp not in z.get("card_lines", []) + [z.get("card_title", "")]: NG(f"{zid}: red_parts の語がカードにない: {rp}")
            # キャラ
            who_in_zone = {b["speaker"] for b in z.get("bubbles", [])}
            for c in z.get("chars", []):
                if c["mode"] not in MODES: NG(f"{zid}: 未定義の chars モード {c['mode']}")
                if c["emotion"] not in EMO: NG(f"{zid}: 未定義の表情ID {c['emotion']}")
                if (c["who"] == "藍子") != (c["side"] == "left"): NG(f"{zid}: {c['who']} の位置が違う（藍子＝左・トリ先生＝右）")
                if c["who"] == "藍子" and c["mode"] != "FACES" and not c.get("hands"): NG(f"{zid}: 藍子（{c['mode']}）に手の割り当て（hands）がない")
                if "silent" in c.get("note", "") and c["who"] in who_in_zone: NG(f"{zid}: silent の {c['who']} の吹き出しが同じ区画にある")
            if z["type"] == "dialogue" or z.get("bubbles"):
                speakers = {c["who"] for c in z.get("chars", [])}
                for b in z.get("bubbles", []):
                    if b["speaker"] not in speakers: NG(f"{zid}: {b['id']} の話者 {b['speaker']} がこの区画に登場していない")
            # C26 区画の高さと、キャラ・吹き出しの数の釣り合い
            need = {"FULL": 520, "MID": 340, "SMALL": 140, "FACES": 100}
            for c in z.get("chars", []):
                if z["h"] < need.get(c["mode"], 0): NG(f"{zid}: 区画の高さ{z['h']}pxに{c['who']}（{c['mode']}）が収まらない（{need[c['mode']]}px以上）")
            if z.get("bubbles") and z["h"] < 100 * len(z["bubbles"]): NG(f"{zid}: 吹き出し{len(z['bubbles'])}個に区画の高さ{z['h']}pxでは足りない（1個100px以上）")
            # 吹き出し
            modes = {c["who"]: c["mode"] for c in z.get("chars", [])}
            for b in z.get("bubbles", []):
                n = len(b["text"]); all_text.append(b["text"])
                lim = 25
                if n > 32: NG(f"{zid}/{b['id']}: 吹き出しが長すぎる（{n}字）: {b['text']}")
                elif n > lim: WARN(f"{zid}/{b['id']}: 吹き出しが{lim}字を超える（{n}字）: {b['text']}")
                if b.get("highlight") and b["highlight"] not in b["text"]: NG(f"{zid}/{b['id']}: 強調語が文中にない: {b['highlight']}")
                if re.search(r"\[(ALPHA|SHIFT|STO|Apps)\]", b["text"]): NG(f"{zid}/{b['id']}: 電卓のキー操作が入っている")
                t, k = b["id"].split("-"); seen_bub.setdefault(t, []).append(int(k))
        # C27 仮枠どうしの間隔（隣り合う仮枠がくっつくと、画像から別々の枠として見つけられない）
        fr = []
        for z in zs:
            if z["type"] == "figure": f = z["frame"]; fr.append((z["zone_id"], f["y"], f["y"] + f["h"]))
            elif z.get("frame") or z["type"] in ("calc_card", "answer_banner", "note_card", "wrong_card", "obs_card", "point_card", "next_chapter_tag"):
                fr.append((z["zone_id"], z["y"] + 20, z["y"] + z["h"] - 20))
        for a, b in zip(fr, fr[1:]):
            if b[1] - a[2] < 30: NG(f"{pid}: 仮枠{a[0]}と{b[0]}の間隔が30px未満（{b[1]-a[2]}px）。画像から別々の枠として検出できない")
        # 区画ごとの吹き出し数（詰め込みすぎ）
        nb = sum(len(z.get("bubbles", [])) for z in zs)
        if nb > 12: WARN(f"{pid}: 吹き出しが{nb}個（多い。読みにくくないか）")
    # C04 セリフの結合＝記事、順序、網羅（C13）
    tids = [t["turn_id"] for t in spec["turns"]]
    for t in spec["turns"]:
        tid = t["turn_id"]; pcs = t["pieces"]
        if norm(t["text"]) != norm("".join(pcs)): NG(f"{tid}: 分割を結合すると記事のセリフと一致しない")
        if norm(t["text"]) not in ch_n: NG(f"{tid}: セリフが記事の第2章にない")
        got = seen_bub.get(tid, [])
        if got != list(range(1, len(pcs) + 1)): NG(f"{tid}: 吹き出しが全部・順番どおりに出ていない（出現：{got}／必要：1〜{len(pcs)}）")
    order = [b for p in pages for z in p["zones"] for b in z.get("bubbles", [])]
    last = -1
    for b in order:
        t = tids.index(b["id"].split("-")[0])
        if t < last: NG(f"{b['id']}: セリフの順番が記事と違う"); break
        last = t
    for b in order:
        if norm(b["text"]) != norm(next(t["pieces"][int(b["id"].split('-')[1]) - 1] for t in spec["turns"] if t["turn_id"] == b["id"].split("-")[0])):
            NG(f"{b['id']}: 吹き出しの文字列が分割の正本と違う")
    # C05 数値
    nums_ch = set(re.findall(r"\d+(?:\.\d+)?", ch))
    for tx in all_text:
        for n in re.findall(r"\d+(?:\.\d+)?", tx):
            if n not in nums_ch: NG(f"数値「{n}」が記事の第2章にない（出どころ不明）: 「{tx}」")
    # C14 図の順序（記事のマーカーの順）
    mk = [m for _, m in markers]
    if mk != sorted(mk): NG(f"図の順序が記事のマーカーの順でない: {mk}")
    n_markers = len(re.findall(r"【画像挿入】", ch))
    if len(mk) != n_markers: NG(f"図の数（{len(mk)}）が記事の第2章のマーカーの数（{n_markers}）と違う")
    # C07 リズム
    tpl = [p["template"].split(" ")[0] for p in pages]
    for i in range(len(tpl) - 2):
        if tpl[i] == tpl[i + 1] == tpl[i + 2]: WARN(f"{ids[i]}〜{ids[i+2]}: 同じテンプレート{tpl[i]}が3ページ連続")
    for i in range(len(pages) - 2):
        if all("計算" in pages[i + k]["template"] for k in range(3)): WARN(f"{ids[i]}〜: 計算ページが3ページ連続")
    # 色
    txt = json.dumps(spec["global"]["colors"], ensure_ascii=False)
    for bad in ("ピンク", "緑"):
        if bad in txt.replace("ピンク・緑・オレンジ。", "").replace("forbidden", ""): pass
    # 章の山場
    if not any("吹き出し" in "" for _ in []): pass
    for m in ng: print("NG  ", m)
    for m in warn: print("WARN", m)
    nb = len(order); np_ = len(pages)
    print(f"ページ{np_}枚・吹き出し{nb}個・図{len(mk)}枚")
    print(f"結果: NG {len(ng)}件 / WARN {len(warn)}件")
    sys.exit(1 if ng else 0)
main()
