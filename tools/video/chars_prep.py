"""キャラクター画像の下ごしらえ。

assets/characters/ に置いた絵（例 Tori_01_closed.png と Tori_01_open.png）を、動画に使う前に次のように整える。
元の画像は書き換えず、整えた写しを out/_chars/ に作る（元の画像が新しくなったら作り直す）。

1. 切り出しのときに残った小さな破片（本体から離れた、本体の5%未満の塊）を消す。
2. 口を開いた絵を、口を閉じた絵にいちばん重なる大きさ・位置に合わせる
   （生成AIで別々に作った2枚は大きさや位置が少しずつ違い、そのままだと口パクのたびに体が伸び縮みする）。

    python3 chars_prep.py        # 全部を整えて、重なり具合を表示する
"""
from __future__ import annotations

import glob
import os
import re

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "characters")
DST = os.path.join(HERE, "out", "_chars")


def clean(im: Image.Image) -> Image.Image:
    """本体から離れた小さな塊（本体の5%未満）を消す。絵の端に接している塊（隣の絵の切れ端）は、本体の15%未満なら消す。"""
    from scipy import ndimage

    a = np.array(im)
    m = a[:, :, 3] > 20
    lab, n = ndimage.label(m)
    if n > 1:
        sizes = ndimage.sum(m, lab, range(1, n + 1))
        edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
        big = sizes.max()
        drop = [i + 1 for i, sz in enumerate(sizes)
                if sz < big and (sz < big * 0.05 or (i + 1 in edge and sz < big * 0.15))]
        a[np.isin(lab, drop), 3] = 0
    return Image.fromarray(a)


def common_box(key: str) -> tuple[int, int, int, int]:
    """そのキャラの全ポーズ（閉じた絵）を重ねた範囲。全ポーズを同じ範囲で切り詰め、大きさをそろえる。"""
    cache = os.path.join(DST, f"{key}_box.txt")
    ps = poses()[key]
    srcs = [p for pair in ps.values() for p in pair]
    if os.path.exists(cache) and os.path.getmtime(cache) >= max(map(os.path.getmtime, srcs + [__file__])):
        return tuple(map(int, open(cache).read().split()))
    boxes = [clean(Image.open(c).convert("RGBA")).getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox() for c, _ in ps.values()]
    m = 12
    w, h = Image.open(srcs[0]).size
    box = (max(0, min(b[0] for b in boxes) - m), max(0, min(b[1] for b in boxes) - m),
           min(w, max(b[2] for b in boxes) + m), min(h, max(b[3] for b in boxes) + m))
    os.makedirs(DST, exist_ok=True)
    open(cache, "w").write(" ".join(map(str, box)))
    return box


def _mask(im: Image.Image, scale: float, size) -> np.ndarray:
    w, h = im.size
    small = im.getchannel("A").resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.BILINEAR)
    canvas = Image.new("L", size, 0)
    canvas.paste(small, (0, 0))
    return (np.array(canvas) > 60).astype(np.float32)


def align(closed: Image.Image, opened: Image.Image) -> tuple[Image.Image, float]:
    """opened を拡大縮小・平行移動して closed に重ねる。戻り値は（合わせた絵, 重なりの割合）。"""
    k = 0.25  # 1/4 の大きさで探す
    W, H = closed.size
    size = (int(W * k), int(H * k))
    ref = _mask(closed, k, size)
    F = np.fft.rfft2(ref)
    best = (-1, 1.0, 0, 0)
    for s in np.arange(0.80, 1.251, 0.01):
        mov = _mask(opened, k * s, size)
        corr = np.fft.irfft2(F * np.conj(np.fft.rfft2(mov)), s=ref.shape)  # 循環相互相関で、ずらす量を一度に探す
        dy, dx = np.unravel_index(np.argmax(corr), corr.shape)
        dy = dy - ref.shape[0] if dy > ref.shape[0] // 2 else dy
        dx = dx - ref.shape[1] if dx > ref.shape[1] // 2 else dx
        shifted = np.roll(np.roll(mov, dy, 0), dx, 1)
        iou = (ref * shifted).sum() / max(1, ((ref + shifted) > 0).sum())
        if iou > best[0]:
            best = (iou, s, dx / k, dy / k)
    _, s, dx, dy = best
    w, h = opened.size
    resized = opened.resize((int(w * s), int(h * s)), Image.LANCZOS)
    out = Image.new("RGBA", closed.size, (0, 0, 0, 0))
    out.paste(resized, (int(round(dx)), int(round(dy))), resized)  # はみ出す分は切れる
    a, b = np.array(closed)[:, :, 3] > 20, np.array(out)[:, :, 3] > 20
    return out, float((a & b).sum() / max(1, (a | b).sum()))


def poses() -> dict[str, dict[int, tuple[str, str]]]:
    """assets/characters/ の絵を {キャラ: {ポーズ番号: (閉じた絵, 開いた絵)}} にまとめる。
    ファイル名は <キャラ>_<番号>_closed.png / _open.png（大文字小文字は問わない）。番号のない <キャラ>_closed.png はポーズ1。"""
    found: dict[str, dict[int, dict[str, str]]] = {}
    for p in glob.glob(os.path.join(SRC, "*")):
        m = re.match(r"(?i)([a-z]+)(?:_(\d+))?_(closed|open)\.(png|webp)$", os.path.basename(p))
        if m:
            found.setdefault(m.group(1).lower(), {}).setdefault(int(m.group(2) or 1), {})[m.group(3).lower()] = p
    return {k: {n: (d["closed"], d["open"]) for n, d in v.items() if "closed" in d and "open" in d} for k, v in found.items()}


def prepared(key: str, pose: int, verbose: bool = False) -> tuple[str, str] | None:
    """整えた（閉じた絵, 開いた絵）のパスを返す。そのキャラの絵がなければ None。"""
    ps = poses().get(key)
    if not ps:
        return None
    if pose not in ps:
        pose = min(ps)
    c_src, o_src = ps[pose]
    os.makedirs(DST, exist_ok=True)
    c_dst = os.path.join(DST, f"{key}_{pose:02d}_closed.png")
    o_dst = os.path.join(DST, f"{key}_{pose:02d}_open.png")
    newest = max(os.path.getmtime(c_src), os.path.getmtime(o_src), os.path.getmtime(__file__))
    if not (os.path.exists(o_dst) and os.path.getmtime(o_dst) >= newest):
        closed = clean(Image.open(c_src).convert("RGBA"))
        opened = clean(Image.open(o_src).convert("RGBA"))
        aligned, iou = align(closed, opened)
        box = common_box(key)
        closed.crop(box).save(c_dst)
        aligned.crop(box).save(o_dst)
        if verbose:
            print(f"{key}_{pose:02d}: 重なり {iou:.3f}")
    return c_dst, o_dst


if __name__ == "__main__":
    for key, ps in sorted(poses().items()):
        for n in sorted(ps):
            # 作り直して重なりを表示する
            for f in glob.glob(os.path.join(DST, f"{key}_{n:02d}_*.png")):
                os.remove(f)
            prepared(key, n, verbose=True)
