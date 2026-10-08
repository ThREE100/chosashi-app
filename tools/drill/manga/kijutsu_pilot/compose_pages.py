#!/usr/bin/env python3
"""ChatGPTが生成したページ画像の『空の灰色の仮枠』に、図・計算カード・答えバナーを貼り込んで完成させる（方式A′）。

- 仮枠は、画像から薄い灰色（#E6E6E6）の長方形を自動で見つけ、上から順に、構成表の枠（図・カードなど）と対応づける。
  ChatGPTが位置・大きさを少しずらしても貼れる。数が合わないときは止まる（--use-spec-coords で構成表の座標をそのまま使う）。
- 図（zu/のPNG）は、ローカルのリポジトリ、または GitHub のURLから読む。ChatGPTには図を添付しない。
    --figures-base <ローカルのリポジトリのルート | https://raw.githubusercontent.com/<owner>/<repo>/<branch>/>
  非公開リポジトリのURLは、環境変数 GITHUB_TOKEN を付けて読む。
- カード・帯の文言は構成表の正本そのまま（記事の文言。電卓のキー操作は入れない）。赤は『誤り』カードの誤り・訂正の箇所だけ。
使い方:
  python3 compose_pages.py <page_spec.json> <ChatGPTのページ画像のフォルダ> <出力フォルダ> [--figures-base BASE] [--font FONTFILE] [--use-spec-coords] [--only PAGE_ID]
  ページ画像のファイル名は <page_id>.png（.jpg/.webp可）。例: R7-Q21-02-01.png
"""
import argparse, collections, hashlib, io, json, os, pathlib, sys, urllib.parse, urllib.request
from PIL import Image, ImageDraw, ImageFont
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NAVY = (26, 43, 94); RED = (200, 30, 40); WHITE = (255, 255, 255); CARD = (240, 242, 247); GRAYPH = 230
CODE_TYPES = {"figure", "calc_card", "answer_banner", "note_card", "wrong_card", "obs_card", "point_card", "next_chapter_tag"}
FONT_CANDIDATES = [
    os.environ.get("MANGA_FONT", ""),
    "C:/Windows/Fonts/YuGothB.ttc", "C:/Windows/Fonts/meiryob.ttc", "C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc",
    "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc", "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf", "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
]

def find_font(arg):
    for f in ([arg] if arg else []) + FONT_CANDIDATES:
        if f and os.path.exists(f): return f
    sys.exit("日本語フォントが見つからない。--font でフォントファイルを指定する（例：Windowsなら C:/Windows/Fonts/YuGothB.ttc）")

def load_figure(base, rel, cache):
    if base.startswith(("http://", "https://")):
        url = base.rstrip("/") + "/" + urllib.parse.quote(rel)
        cache.mkdir(parents=True, exist_ok=True)
        cf = cache / (hashlib.sha1(url.encode()).hexdigest() + ".png")
        if not cf.exists():
            req = urllib.request.Request(url)
            if os.environ.get("GITHUB_TOKEN"): req.add_header("Authorization", "token " + os.environ["GITHUB_TOKEN"])
            with urllib.request.urlopen(req, timeout=60) as r: cf.write_bytes(r.read())
        return Image.open(cf).convert("RGB")
    return Image.open(pathlib.Path(base) / rel).convert("RGB")

# ---------------------------------------------------------------- 仮枠の検出
def detect_placeholders(img, tol=10, min_cells=3500):
    a = np.asarray(img.convert("RGB")).astype(int)
    m = (np.abs(a - GRAYPH).max(axis=2) <= tol) & ((a.max(axis=2) - a.min(axis=2)) <= 6)
    S = 4; sm = m[::S, ::S]; H, W = sm.shape
    seen = np.zeros_like(sm, bool); rects = []
    for y0 in range(H):
        for x0 in range(W):
            if sm[y0, x0] and not seen[y0, x0]:
                q = collections.deque([(y0, x0)]); seen[y0, x0] = True; cells = []
                while q:
                    y, x = q.popleft(); cells.append((y, x))
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < H and 0 <= nx < W and sm[ny, nx] and not seen[ny, nx]: seen[ny, nx] = True; q.append((ny, nx))
                if len(cells) < min_cells: continue
                ys = [c[0] for c in cells]; xs = [c[1] for c in cells]
                bx0, bx1, by0, by1 = min(xs), max(xs), min(ys), max(ys)
                fill = len(cells) / ((bx1 - bx0 + 1) * (by1 - by0 + 1))
                if fill < 0.85: continue
                # 実解像度で縁を詰める
                X0, X1, Y0, Y1 = max(0, bx0 * S - S), min(m.shape[1], bx1 * S + S + 1), max(0, by0 * S - S), min(m.shape[0], by1 * S + S + 1)
                win = m[Y0:Y1, X0:X1]; yy, xx = np.nonzero(win)
                rects.append((X0 + int(xx.min()), Y0 + int(yy.min()), int(xx.max() - xx.min()) + 1, int(yy.max() - yy.min()) + 1))
    return sorted(rects, key=lambda r: (r[1], r[0]))

# ---------------------------------------------------------------- 描画
def fit_text(draw, lines, font_path, w, h, max_size=54, min_size=22, bullet=""):
    """まず、与えられた行を折り返さずに収まる最大の字の大きさ（30px以上）を探す。式の途中で改行しないため。
    収まらなければ、折り返してよい（22px以上）。"""
    for size in range(max_size, 29, -2):
        font = ImageFont.truetype(font_path, size); lh = int(size * 1.35)
        if lh * len(lines) <= h and all(draw.textlength(bullet + ln, font=font) <= w for ln in lines):
            return font, [bullet + ln for ln in lines], lh
    for size in range(max_size, min_size - 1, -2):
        font = ImageFont.truetype(font_path, size); out = []
        for ln in lines:
            cur = bullet
            for ch in ln:
                if draw.textlength(cur + ch, font=font) > w and cur != bullet: out.append(cur); cur = ch
                else: cur += ch
            out.append(cur)
        lh = int(size * 1.35)
        if lh * len(out) <= h: return font, out, lh
    return font, out, lh

def paste_content(page, z, rect, spec, font_path, args, cache):
    x, y, w, h = rect; pad = 2
    d = ImageDraw.Draw(page)
    d.rectangle([x - pad, y - pad, x + w + pad - 1, y + h + pad - 1], fill=WHITE)   # 仮枠（と縁の残り）を消す
    t = z["type"]
    if t == "figure":
        fig = load_figure(args.figures_base, spec["figures"][z["figure_ref"]]["file"], cache)
        s = min(w / fig.width, h / fig.height); nw, nh = int(fig.width * s), int(fig.height * s)
        page.paste(fig.resize((nw, nh), Image.LANCZOS), (x + (w - nw) // 2, y + (h - nh) // 2))
        d.rectangle([x, y, x + w - 1, y + h - 1], outline=(190, 190, 190), width=2); return
    lines = z.get("card_lines", [])
    if t == "answer_banner":
        d.rounded_rectangle([x, y, x + w - 1, y + h - 1], radius=16, fill=NAVY)
        font, out, lh = fit_text(d, lines, font_path, w - 60, h - 30, max_size=60)
        top = y + (h - lh * len(out)) // 2
        for i, ln in enumerate(out): d.text((x + w // 2, top + i * lh), ln, font=font, fill=WHITE, anchor="mt")
        return
    red = t == "wrong_card"; edge = RED if red else NAVY
    d.rounded_rectangle([x, y, x + w - 1, y + h - 1], radius=16, fill=CARD, outline=edge, width=4)
    ty = y + 14
    if z.get("card_title"):
        tf = ImageFont.truetype(font_path, 30); tw = int(d.textlength(z["card_title"], font=tf)) + 36
        d.rounded_rectangle([x + 18, ty, x + 18 + tw, ty + 46], radius=12, fill=edge)
        d.text((x + 36, ty + 23), z["card_title"], font=tf, fill=WHITE, anchor="lm"); ty += 62
    bullet = "・" if (t in ("obs_card", "point_card") and len(lines) > 1) else ""
    font, out, lh = fit_text(d, lines, font_path, w - 70, y + h - ty - 18, max_size=50, bullet=bullet)
    if t == "next_chapter_tag": ty = y + (h - lh * len(out)) // 2
    reds = [r for r in z.get("red_parts", [])]
    for i, ln in enumerate(out):
        col = RED if (red and any(r.strip("（）") in ln for r in reds if r != z.get("card_title"))) else NAVY
        d.text((x + 36, ty + i * lh), ln, font=font, fill=col)

def spec_rects(p):
    out = []
    for z in p["zones"]:
        if z["type"] in CODE_TYPES:
            if z["type"] == "figure": f = z["frame"]; out.append((f["x"], f["y"], f["w"], f["h"]))
            else: f = z.get("frame", {"x": 40, "w": 1000}); out.append((f["x"], z["y"] + 20, f["w"], z["h"] - 40))
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("spec"); ap.add_argument("pages_dir"); ap.add_argument("out_dir")
    ap.add_argument("--figures-base", default=str(ROOT)); ap.add_argument("--font", default=""); ap.add_argument("--use-spec-coords", action="store_true"); ap.add_argument("--only", default="")
    args = ap.parse_args()
    spec = json.loads(pathlib.Path(args.spec).read_text(encoding="utf8")); font_path = find_font(args.font)
    out = pathlib.Path(args.out_dir); out.mkdir(parents=True, exist_ok=True); cache = out / ".figcache"
    ok = bad = 0
    for p in spec["pages"]:
        pid = p["page_id"]
        if args.only and pid != args.only: continue
        src = next((c for e in ("png", "jpg", "jpeg", "webp") if (c := pathlib.Path(args.pages_dir) / f"{pid}.{e}").exists()), None)
        if not src: print(f"SKIP {pid}: ページ画像がない"); continue
        page = Image.open(src).convert("RGB"); W, H = spec["global"]["canvas"]["w"], spec["global"]["canvas"]["h"]
        if abs(page.width / page.height - W / H) > 0.02: print(f"WARN {pid}: 縦横比が{W}:{H}と違う（{page.width}×{page.height}）。リサイズして続ける")
        if page.size != (W, H): page = page.resize((W, H), Image.LANCZOS)
        zs = [z for z in p["zones"] if z["type"] in CODE_TYPES]
        found = spec_rects(p) if args.use_spec_coords else detect_placeholders(page)
        if len(found) != len(zs):
            print(f"NG   {pid}: 仮枠の数が合わない（画像から{len(found)}個、構成表は{len(zs)}個）。ChatGPTが仮枠を描いていない／余計な灰色の四角を描いた。生成し直す"); bad += 1; continue
        for z, r in zip(zs, found):
            exp = spec_rects(p)[zs.index(z)]
            if abs(r[2] - exp[2]) > 120 or abs(r[3] - exp[3]) > 120 or abs(r[1] - exp[1]) > 200:
                print(f"WARN {pid}/{z['zone_id']}: 仮枠の位置・大きさが構成表とずれている（検出{r}／構成表{exp}）")
            paste_content(page, z, r, spec, font_path, args, cache)
        page.save(out / f"{pid}.png"); ok += 1; print(f"OK   {pid}: {len(zs)}枠を貼り込んだ")
    print(f"完成 {ok}枚 / NG {bad}枚")
    sys.exit(1 if bad else 0)
main()
