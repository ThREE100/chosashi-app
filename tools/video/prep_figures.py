#!/usr/bin/env python3
"""解説図の描画スクリプトを、動画用に高解像度・大きな文字で実行し、図の中の文字の位置と大きさを記録する。

描画スクリプト（例: note-articles-Kijyutsu/R8/Q21/zu/draw_R8_dai21mon_kaisetsuzu.py）は書き換えない。
matplotlib を差し替えて、(1) 解像度を scale 倍にして保存し、(2) 図の中の文字の大きさを font-scale 倍にして描き直し、
(3) 文字の位置・大きさを <名前>.json に書く。元の図（zu/ のPNG）はそのまま残る。

文字を大きくすると、図によっては文字どうしが重なる。描画スクリプトの重なり検査（[重なり検査] の行）を読み、
**図ごとに、重なりが出ない最大の倍率**を自動で選ぶ（--font-scales の先頭から順に試す）。
重なりのない倍率が1つもない図は、1.0（元の大きさ）で書き出す。

    python3 prep_figures.py <描画スクリプト> [--scale 2] [--font-scales 1.5,1.35,1.2,1.0] [--out out/zu_hires/<名前>]
    python3 prep_figures.py <描画スクリプト> --scale 1 --font-scales 1.0 --report   # 今の図の文字の大きさだけを調べる（分析用）

記録するJSON: {"w": 幅px, "h": 高さpx, "scale": 解像度の倍率, "font_scale": 文字の倍率,
               "texts": [{"s": 文字列, "box": [x0,y0,x1,y1]（図の幅・高さに対する0〜1）, "px": 文字の高さ(px)}]}
動画のズーム範囲（view）に対して、文字が小さすぎないか・途中で切れていないかを check_shots.py が確かめる。
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import runpy
import shutil
import statistics
import sys

import matplotlib

matplotlib.use("Agg")
from matplotlib.figure import Figure  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402
from matplotlib.text import Text  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = re.compile(r"\[重なり検査\] (\S+\.png): (問題なし|(\d+)件)")


class _Tee(io.StringIO):
    def write(self, s):
        sys.__stdout__.write(s)
        return super().write(s)


def collect_texts(fig, save_dpi: float) -> list[dict]:
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    W, H = fig.bbox.width, fig.bbox.height
    texts = []
    for t in fig.findobj(Text):
        s = t.get_text().strip()
        if not s or not t.get_visible():
            continue
        bb = t.get_window_extent(r)
        if bb.width <= 0 or bb.height <= 0:
            continue
        texts.append({
            "s": s[:60],
            "box": [round(bb.x0 / W, 5), round(1 - bb.y1 / H, 5), round(bb.x1 / W, 5), round(1 - bb.y0 / H, 5)],
            "px": round(t.get_fontsize() * save_dpi / 72.0, 1),
        })
    return texts


def run_once(script: str, out: str, scale: float, font_scale: float, write: bool):
    """描画スクリプトを1回実行する。戻り値: ({図の名前: 記録}, {図の名前: 重なりの件数})"""
    os.makedirs(out, exist_ok=True)
    records: dict[str, dict] = {}
    orig_save = Figure.savefig
    orig_set_size = FontProperties.set_size

    def savefig(self, fname, *args, **kw):
        dpi = float(kw.get("dpi") or self.dpi) * scale
        kw["dpi"] = dpi
        name = os.path.basename(str(fname))
        w, h = self.get_size_inches()
        records[name] = {"w": int(round(w * dpi)), "h": int(round(h * dpi)), "scale": scale, "font_scale": font_scale,
                         "texts": collect_texts(self, dpi)}
        if write:
            orig_save(self, fname, *args, **kw)
            with open(os.path.splitext(str(fname))[0] + ".json", "w", encoding="utf-8") as f:
                json.dump(records[name], f, ensure_ascii=False)

    def set_size(self, size):  # 数値で指定された文字の大きさだけを倍にする（"small" などの名前はそのまま）
        if isinstance(size, (int, float)):
            size = size * font_scale
        return orig_set_size(self, size)

    Figure.savefig = savefig
    FontProperties.set_size = set_size
    argv = sys.argv
    buf = _Tee()
    try:
        sys.argv = [script, out]
        with contextlib.redirect_stdout(buf):
            runpy.run_path(script, run_name="__main__")
    finally:
        Figure.savefig = orig_save
        FontProperties.set_size = orig_set_size
        sys.argv = argv
    overlaps = {m.group(1): (0 if m.group(2) == "問題なし" else int(m.group(3))) for m in CHECK.finditer(buf.getvalue())}
    return records, overlaps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--scale", type=float, default=2.0, help="解像度の倍率（元の図は幅1600px。2なら3200px）")
    ap.add_argument("--font-scales", default="1.5,1.35,1.2,1.0", help="試す文字の倍率（大きい順）。図ごとに重なりのない最大のものを選ぶ")
    ap.add_argument("--out")
    ap.add_argument("--report", action="store_true", help="書き出さず、文字の大きさの一覧だけを表示する")
    a = ap.parse_args()
    script = os.path.abspath(a.script)
    out = os.path.abspath(a.out or os.path.join(HERE, "out", "zu_hires", os.path.splitext(os.path.basename(script))[0]))
    ks = [float(k) for k in a.font_scales.split(",")]
    trial = os.path.join(out, "_trial")
    results: dict[float, tuple[dict, dict]] = {}
    for k in ks:
        print(f"\n===== 文字 {k} 倍で描画 =====")
        results[k] = run_once(script, os.path.join(trial, f"k{k}"), a.scale, k, write=not a.report)
    chosen: dict[str, float] = {}
    names = list(results[ks[-1]][0])
    for n in names:
        chosen[n] = next((k for k in ks if results[k][1].get(n) == 0), ks[-1])
    if a.report:
        recs = {n: results[chosen[n]][0][n] for n in names}
        print(f"\n{'図':44s} {'大きさ':>10s} {'倍率':>5s} {'文字数':>5s} {'最小px':>6s} {'中央px':>6s}")
        for n, r in sorted(recs.items()):
            px = [t["px"] for t in r["texts"]]
            print(f"{n:44s} {r['w']:>5d}x{r['h']:<5d} {chosen[n]:>5.2f} {len(px):>5d} {min(px):>6.1f} {statistics.median(px):>6.1f}")
        return
    os.makedirs(out, exist_ok=True)
    for n in names:
        k = chosen[n]
        base = os.path.splitext(n)[0]
        for ext in (".png", ".json"):
            src = os.path.join(trial, f"k{k}", base + ext)
            if os.path.exists(src):
                shutil.copy(src, os.path.join(out, base + ext))
    shutil.rmtree(trial, ignore_errors=True)
    with open(os.path.join(out, "_font_scales.json"), "w", encoding="utf-8") as f:
        json.dump(chosen, f, ensure_ascii=False, indent=1)
    print("\n図ごとに選んだ文字の倍率:")
    for n, k in sorted(chosen.items()):
        print(f"  {n:46s} {k}")
    print(f"書き出し先: {out}")


if __name__ == "__main__":
    main()
