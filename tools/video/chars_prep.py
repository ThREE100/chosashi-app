"""キャラクター画像の下ごしらえ。

assets/characters/ に置いた絵（例 Tori_01_closed.png と Tori_01_open.png）を、動画に使う前に次のように整える。
元の画像は書き換えず、整えた写しを out/_chars/ に作る（元の画像が新しくなったら作り直す）。

1. 切り出しのときに残った小さな破片（本体から離れた、本体の5%未満の塊）を消す。
2. 口を開いた絵を、口を閉じた絵にいちばん重なる大きさ・位置に合わせる
   （生成AIで別々に作った2枚は大きさや位置が少しずつ違い、そのままだと口パクのたびに体が伸び縮みする）。
   もともと重なっている絵（重なり99%以上）は、そのまま使う。
4. poses.json でそのキャラに "mirror": true を書くと、左右を反転する（画面の右にいるキャラを中央に向かせる）。
3. poses.json でそのキャラに "mouth": {"method": "patch"} を書くと、閉じた絵をそのまま使い、
   口のまわりだけを開いた絵から貼り込む（口以外の描き方が違い、合わせても体が揺れるキャラ用。トリ先生）。

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
    if os.path.exists(cache) and os.path.getmtime(cache) >= max(map(os.path.getmtime, srcs + [__file__, os.path.join(HERE, "poses.json")])):
        return tuple(map(int, open(cache).read().split()))
    ims = [clean(Image.open(c).convert("RGBA")) for c, _ in ps.values()]
    if character_cfg(key).get("mirror"):
        ims = [im.transpose(Image.FLIP_LEFT_RIGHT) for im in ims]
    boxes = [im.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox() for im in ims]
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


def _iou(a: Image.Image, b: Image.Image) -> float:
    x, y = np.array(a)[:, :, 3] > 20, np.array(b)[:, :, 3] > 20
    return float((x & y).sum() / max(1, (x | y).sum()))


def _search(closed, opened, k, scales):
    """縮小した輪郭どうしで、拡大率ごとに一番重なるずらし量を探す（循環相互相関）。"""
    W, H = closed.size
    size = (int(W * k), int(H * k))
    ref = _mask(closed, k, size)
    F = np.fft.rfft2(ref)
    best = (-1, 1.0, 0.0, 0.0)
    for s in scales:
        mov = _mask(opened, k * s, size)
        corr = np.fft.irfft2(F * np.conj(np.fft.rfft2(mov)), s=ref.shape)
        dy, dx = np.unravel_index(np.argmax(corr), corr.shape)
        dy = dy - ref.shape[0] if dy > ref.shape[0] // 2 else dy
        dx = dx - ref.shape[1] if dx > ref.shape[1] // 2 else dx
        shifted = np.roll(np.roll(mov, dy, 0), dx, 1)
        iou = (ref * shifted).sum() / max(1, ((ref + shifted) > 0).sum())
        if iou > best[0]:
            best = (iou, float(s), dx / k, dy / k)
    return best


def _place(closed, opened, s, dx, dy):
    w, h = opened.size
    resized = opened.resize((max(1, round(w * s)), max(1, round(h * s))), Image.LANCZOS) if s != 1.0 else opened
    out = Image.new("RGBA", closed.size, (0, 0, 0, 0))
    out.paste(resized, (int(round(dx)), int(round(dy))), resized)  # はみ出す分は切れる
    return out


def align(closed: Image.Image, opened: Image.Image) -> tuple[Image.Image, float]:
    """opened を拡大縮小・平行移動して closed に重ねる。戻り値は（合わせた絵, 重なりの割合）。
    もともと重なっている絵（重なり99%以上）は、そのまま返す（余計な拡大縮小は、かえって口パクのたびの揺れになる）。"""
    raw = _iou(closed, opened)
    if raw >= 0.99:
        return opened, raw
    _, s, _, _ = _search(closed, opened, 0.25, np.arange(0.80, 1.251, 0.01))            # 粗く
    _, s, dx, dy = _search(closed, opened, 0.5, np.arange(s - 0.012, s + 0.0121, 0.002))  # 細かく
    out = _place(closed, opened, s, dx, dy)
    iou = _iou(closed, out)
    return (out, iou) if iou > raw else (opened, raw)


def _mouth_box(im: Image.Image, find: str) -> tuple[int, int, int, int] | None:
    """口（くちばし）の場所を色で探す。find="orange" は、絵の上半分にあるいちばん大きなオレンジ色の塊（足は下半分なので除く）。"""
    from scipy import ndimage

    a = np.array(im).astype(int)
    alpha = a[:, :, 3] > 20
    ys, _ = np.nonzero(alpha)
    R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    if find != "orange":
        raise SystemExit(f"口の探し方「{find}」には対応していません（poses.json の mouth.find）")
    m = (R > 200) & (G > 110) & (G < 210) & (B < 110) & alpha
    m[int(ys.min() + (ys.max() - ys.min()) * 0.5):] = False
    lab, n = ndimage.label(m)
    if n == 0:
        return None
    k = int(np.argmax(ndimage.sum(m, lab, range(1, n + 1)))) + 1
    yy, xx = np.nonzero(lab == k)
    return int(xx.min()), int(yy.min()), int(xx.max()), int(yy.max())


def mouth_patch(closed: Image.Image, opened: Image.Image, cfg: dict) -> Image.Image:
    """閉じた絵をそのまま使い、口のまわりだけを開いた絵から貼り込む（ぼかしたふちで重ねる）。
    閉じた絵と開いた絵で口以外の描き方が違うキャラ（体ごと入れ替わって揺れる）に使う。"""
    from PIL import ImageDraw, ImageFilter

    b1, b2 = _mouth_box(closed, cfg.get("find", "orange")), _mouth_box(opened, cfg.get("find", "orange"))
    if not b1 or not b2:
        return opened
    l, t, r, b = cfg.get("margin", [16, 14, 16, 26])  # 開いた口は下へ広がるので、下を広めに
    box = (min(b1[0], b2[0]) - l, min(b1[1], b2[1]) - t, max(b1[2], b2[2]) + r, max(b1[3], b2[3]) + b)
    mask = Image.new("L", closed.size, 0)
    ImageDraw.Draw(mask).ellipse(box, fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(cfg.get("feather", 5)))
    return Image.composite(opened, closed, mask)


def character_cfg(key: str) -> dict:
    import json

    with open(os.path.join(HERE, "poses.json"), encoding="utf-8") as f:
        return json.load(f).get(key, {})


def mouth_cfg(key: str) -> dict:
    return character_cfg(key).get("mouth", {})


def poses() -> dict[str, dict[int, tuple[str, str]]]:
    """assets/characters/ の絵を {キャラ: {ポーズ番号: (閉じた絵, 開いた絵)}} にまとめる。
    ファイル名は <キャラ>_<番号>_closed.png / _open.png（大文字小文字は問わない）。番号のない <キャラ>_closed.png はポーズ1。
    キャラと番号の間に Aiko_upper_01_closed.png のような語をはさんでもよい（読み飛ばす）。"""
    found: dict[str, dict[int, dict[str, str]]] = {}
    for p in glob.glob(os.path.join(SRC, "*")):
        # 名前の途中の語（Aiko_upper_01_closed.png の upper など。絵の種類のメモ）は読み飛ばす
        m = re.match(r"(?i)([a-z]+)(?:_[a-z]+)*?(?:_(\d+))?_(closed|open)\.(png|webp)$", os.path.basename(p))
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
    newest = max(os.path.getmtime(c_src), os.path.getmtime(o_src), os.path.getmtime(__file__),
                 os.path.getmtime(os.path.join(HERE, "poses.json")))
    if not (os.path.exists(o_dst) and os.path.getmtime(o_dst) >= newest):
        closed = clean(Image.open(c_src).convert("RGBA"))
        opened = clean(Image.open(o_src).convert("RGBA"))
        if character_cfg(key).get("mirror"):  # 左右を反転（画面の中央を向かせる）
            closed, opened = closed.transpose(Image.FLIP_LEFT_RIGHT), opened.transpose(Image.FLIP_LEFT_RIGHT)
        aligned, iou = align(closed, opened)
        mc = mouth_cfg(key)
        if mc.get("method") == "patch":
            aligned = mouth_patch(closed, aligned, mc)
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
