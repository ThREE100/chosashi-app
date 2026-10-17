# 区分建物の範囲：「出題文の状態」と「正しいイメージ／誤ったイメージ」の図解プロンプトを組み立てる
import sys, pathlib, re
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY

STATE_CAP = "出題文の状態"
RIGHT_CAP = "正しいイメージ"
PITFALL_CAP = "間違えやすいポイント"

def scene_prompt(sc):
    """sc: dict(t1, t2, sub, state=dict(draw, labels=[str..]),
                pairs=[dict(claim, right=dict(draw, labels, tag), pitfall)])
    2026-10-17の改訂：正解だけを描く。claim は『正しい内容を言い切る文』（見出し）。
    pitfall は、間違えやすい点を正しいイメージの下にテキストで添える短い文（見出しにはしない）。"""
    n = len(sc["pairs"])
    assert 1 <= n <= 3
    size = f"1080x{900 + 520 * n}"
    body = [lead(size, "This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows only the correct picture for each point, with a short text note about a common pitfall under each correct picture. It is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere except the one short pitfall note under each correct picture. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation or legal citation. Do not draw any person with a face; use faceless simple pictograms when a person is needed. Draw ONLY correct pictures: never draw a mistaken picture, a crossed-out picture, or a side-by-side correct/incorrect comparison.",
            TEXTREQ, BGREQ, COLOR,
            "--- HEADER ---", "Title (large, bold, 2 lines):", q(sc["t1"]), q(sc["t2"]), "Subtitle (smaller, centered, 1 line):", q(sc["sub"]),
            "--- SECTION 1: THE STATE (full width, dark navy frame) ---",
            "Section label (navy pill at the top-left of the frame):", q(STATE_CAP),
            "Illustration: " + sc["state"]["draw"]]
    if sc["state"].get("labels"):
        body.append("Short labels placed on the objects, each exactly once: " + ", ".join(q(l) for l in sc["state"]["labels"]) + ".")
    body.append("Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.")
    for k, p in enumerate(sc["pairs"], 1):
        body += [f"--- SECTION {k + 1}: POINT {k} (full-width row) ---",
                 "A slim pale-yellow banner across the top of the row, stating the correct content, with this text exactly:", q(p["claim"]),
                 f"Below the banner place one wide panel with a thick rounded BLUE frame. Panel label (blue pill): {q(RIGHT_CAP)}. Illustration: " + p["right"]["draw"]]
        if p["right"].get("labels"):
            body.append("Short labels on the panel, each exactly once: " + ", ".join(q(l) for l in p["right"]["labels"]) + ".")
        body.append("Conclusion tag at the bottom of the panel (blue banner, keyword phrase, not a sentence): " + q(p["right"]["tag"]))
        body.append(f"Directly under the blue panel, outside its frame, place a slim plain note strip (light gray background, dark navy text, NOT red) with the small heading {q(PITFALL_CAP)} followed by this text exactly: " + q(p["pitfall"]) + ". The note is plain text only, with no illustration and no cross mark.")
    txt = "\n".join(body)
    extra = (f"Confirm the poster has exactly 1 state section followed by exactly {n} point row(s), each with one blue correct panel and one gray pitfall note, with no duplicated or missing panels, "
             f"confirm that no mistaken picture, no red panel, and no side-by-side comparison is drawn anywhere, confirm every label appears exactly once and reads exactly as given, and confirm that no panel contains a full sentence of explanatory prose other than the single pitfall note under each correct picture.")
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

def flow_or_card_note():
    return ""

def midashi_prompt(m):
    """m: dict(t1, t2, hot=(強調語), sub, left, right, kanji=str)"""
    t1, t2, sub = m["t1"], m["t2"], m["sub"]
    hot = m["hot"]
    assert hot in t2
    kj = sorted(set(re.findall(r"[一-鿿]", t1 + t2 + sub)))
    digits = sorted(set(re.findall(r"[0-9]", t1 + t2 + sub)))
    dg = ("the Arabic numeral(s) " + ", ".join(digits)) if digits else "no digits"
    return f"""Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief), placed at the lower left of center. 藍子 is the young woman exam candidate (long wavy brown hair, pinstriped light-blue blouse with rolled sleeves, navy pencil skirt, no jacket), placed at the lower right of center. POSES ARE NOT FIXED: do not copy any pose from the attached images or from earlier header images; let each character take a free, natural pose of your own choosing that fits the topic and suits the character (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep both characters fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and {dg}; the only digits allowed are those in the text exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
{t1}
Line 2 is larger; the phrase {hot} is red-orange and the rest is dark navy:
{t2}
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
{sub}
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: {m['left']}
Right side: {m['right']}

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji {", ".join(kj)}; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere."""
