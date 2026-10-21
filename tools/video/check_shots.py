#!/usr/bin/env python3
"""台本の「図の場面」を点検する。図の中の文字が、動画で見たときに小さすぎないか・途中で切れていないかを確かめる。

    python3 check_shots.py episodes/R8_Q21_ep01.json            # 点検の一覧（問題があれば終了コード1）
    python3 check_shots.py episodes/R8_Q21_ep01.json --png      # 場面ごとの確認画像を out/<id>/shotcheck/ に書く

点検の基準（実寸は 1920×1080 の動画の上での大きさ。YOUTUBE_VISUAL_SPEC.md）:
    - 図の中の文字は 28px 以上（満たさないものは「小さい」）。32px 未満は「注意」。
    - 見えている範囲の端で文字が半分以上切れているものは「切れ」。
図の文字の位置・大きさは prep_figures.py が書く <図>.json から読む。
確認画像: 緑＝十分な大きさ、橙＝注意、赤＝小さい、青＝切れ。
"""
from __future__ import annotations

import argparse
import json
import os
import sys

from render import Renderer

SW, SH = 1440, 810
MIN_PX, WARN_PX = 28, 32


def analyze(info: dict, view: list[float]):
    """図の画像 info（nw, nh, json の文字一覧）と表示範囲 view から、画面に見える文字を調べる。"""
    nw, nh = info["nw"], info["nh"]
    vw, vh = (view[2] - view[0]) * nw, (view[3] - view[1]) * nh
    k = min(SW / vw, SH / vh)                      # 図の1pxが画面で何pxになるか
    cx, cy = (view[0] + view[2]) / 2 * nw, (view[1] + view[3]) / 2 * nh
    x0, x1, y0, y1 = cx - SW / k / 2, cx + SW / k / 2, cy - SH / k / 2, cy + SH / k / 2   # 画面に見える範囲（画像のpx）
    rows = []
    for t in info["texts"]:
        bx0, by0, bx1, by1 = t["box"][0] * nw, t["box"][1] * nh, t["box"][2] * nw, t["box"][3] * nh
        ix0, ix1, iy0, iy1 = max(bx0, x0), min(bx1, x1), max(by0, y0), min(by1, y1)
        if ix1 <= ix0 or iy1 <= iy0:
            continue
        frac = (ix1 - ix0) * (iy1 - iy0) / max(1e-9, (bx1 - bx0) * (by1 - by0))
        rows.append({"s": t["s"], "px": t["px"] * k, "frac": frac, "box": (bx0, by0, bx1, by1)})
    return k, (x0, y0, x1, y1), rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--png", action="store_true")
    a = ap.parse_args()
    r = Renderer(a.script, None, True, check_only=True)
    out = os.path.join(r.out, "shotcheck")
    if a.png:
        os.makedirs(out, exist_ok=True)
    stage = {"kind": "none"}
    bad = 0
    n = 0
    seen = set()
    ov_views: set = set()   # 「全体を見せる」と書いた場面の表示範囲（同じ範囲のあとの場面も全体として扱う）
    for ch in r.sc["chapters"]:
        for bi, beat in enumerate(ch["beats"]):
            stage = r.stage_of(beat, stage)
            if stage.get("kind") != "image":
                continue
            vk = (stage["src"], tuple(round(v, 4) for v in stage["view"]))
            if beat.get("overview"):
                ov_views.add(vk)
            overview = vk in ov_views
            key = vk + (overview,)
            if key in seen:
                continue
            seen.add(key)
            n += 1
            jp = os.path.splitext(stage["src"][len("file://"):])[0] + ".json"
            if not os.path.exists(jp):
                print(f"[{n:02d}] {ch['title'][:14]} #{bi}: {os.path.basename(stage['src'])} 文字の記録（.json）がありません → 点検できません")
                continue
            info = {**stage, **json.load(open(jp, encoding="utf-8"))}
            info["nw"], info["nh"] = stage["nw"], stage["nh"]
            k, vis, rows = analyze(info, stage["view"])
            main_rows = [x for x in rows if x["frac"] >= 0.5]
            small = [] if overview else [x for x in main_rows if x["px"] < MIN_PX]   # 全体を見せる場面は、文字の大きさを問わない
            warn = [x for x in main_rows if MIN_PX <= x["px"] < WARN_PX]
            cut = [x for x in rows if 0.04 < x["frac"] < 0.9]
            mn = min((x["px"] for x in main_rows), default=0)
            flag = "NG " if (small or cut) else ("全体" if overview else ("注意" if warn else "OK "))
            bad += bool(small or cut)
            print(f"[{n:02d}] {flag} {os.path.basename(stage['src'])[14:40]:26s} 拡大{k / (SW / stage['nw']):.2f}倍 図1px→{k:.2f}px "
                  f"文字{len(main_rows):2d}個 最小{mn:5.1f}px 小さい{len(small)} 注意{len(warn)} 切れ{len(cut)}   ({ch['title'][:12]} #{bi})")
            for x in small[:4]:
                print(f"       小さい {x['px']:.0f}px 「{x['s'][:20]}」")
            for x in cut[:4]:
                print(f"       切れ   {x['frac']:.0%}しか見えない 「{x['s'][:20]}」")
            if a.png:
                from PIL import Image, ImageDraw

                im = Image.open(stage["src"][len("file://"):]).convert("RGB")
                x0, y0, x1, y1 = vis
                pad = Image.new("RGB", (int(x1 - x0), int(y1 - y0)), (255, 255, 255))
                pad.paste(im, (int(-x0), int(-y0)))
                d = ImageDraw.Draw(pad)
                for x in rows:
                    c = (0, 160, 0) if x["frac"] >= 0.9 and x["px"] >= WARN_PX else (230, 140, 0) if x["frac"] >= 0.9 and x["px"] >= MIN_PX else \
                        (200, 0, 0) if x["frac"] >= 0.9 else (0, 80, 220)
                    b = x["box"]
                    d.rectangle([b[0] - x0, b[1] - y0, b[2] - x0, b[3] - y0], outline=c, width=max(3, int(3 / k)))
                pad.resize((SW, SH)).save(os.path.join(out, f"{n:02d}.png"))
    print(f"\n図の場面 {n}件、NG {bad}件")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
