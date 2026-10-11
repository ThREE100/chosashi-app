#!/usr/bin/env python3
"""ChatGPTが生成したページ画像の代わりになる『模擬ページ』を作る（合成の動作確認用。キャラの絵はない）。
仮枠は、構成表の位置から少しずらし、角を丸めて描く（ChatGPTのずれを想定）。
使い方: python3 mock_chatgpt_pages.py <page_spec.json> <出力フォルダ>"""
import json, pathlib, random, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
FONT = next(f for f in ("/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf", "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf") if pathlib.Path(f).exists())
spec = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf8")); out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
random.seed(7)
f30 = ImageFont.truetype(FONT, 30); f36 = ImageFont.truetype(FONT, 36)
for p in spec["pages"]:
    im = Image.new("RGB", (1080, 1920), (253, 247, 230)); d = ImageDraw.Draw(im)
    for z in p["zones"]:
        y, h, t = z["y"], z["h"], z["type"]
        if t in ("tab", "chapter_header"):
            d.rectangle([0, y, 1080, y + h - 8], fill=(26, 43, 94)); d.text((30, y + h // 2 - 4), z["text"], font=f36, fill="white", anchor="lm")
        elif t == "figure" or t in ("calc_card", "answer_banner", "note_card", "wrong_card", "obs_card", "point_card", "next_chapter_tag"):
            if t == "figure": f = z["frame"]; x, yy, w, hh = f["x"], f["y"], f["w"], f["h"]
            else: x, yy, w, hh = 40, y + 20, 1000, h - 40
            x += random.randint(-8, 8); yy += random.randint(-10, 10); w += random.randint(-10, 6); hh += random.randint(-8, 8)
            d.rounded_rectangle([x, yy, x + w, yy + hh], radius=6, fill=(230, 230, 230))
        else:
            ytop = y + 10
            for k, b in enumerate(z.get("bubbles", [])):
                side = b["speaker"] == "藍子"; bx = 200 if side else 420; by = ytop + k * min(120, (h - 20) // max(1, len(z["bubbles"])))
                d.rounded_rectangle([bx, by, bx + 460, by + 70], radius=24, fill="white", outline=(26, 43, 94), width=3)
                d.text((bx + 16, by + 35), b["text"][:16], font=f30, fill=(26, 43, 94), anchor="lm")
            for c in z.get("chars", []):
                cx = 100 if c["who"] == "藍子" else 980; r = {"FULL": 120, "MID": 90, "SMALL": 40, "FACES": 40}[c["mode"]]
                d.ellipse([cx - r, y + h - 2 * r - 20, cx + r, y + h - 20], fill=(240, 200, 170) if c["who"] == "藍子" else (200, 170, 120))
    im.save(out / f"{p['page_id']}.png")
print("mock pages →", out)
