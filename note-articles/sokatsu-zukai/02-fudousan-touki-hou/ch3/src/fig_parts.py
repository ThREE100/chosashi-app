"""総合記事②不動産登記法編 第3章：4コマの設計データ（spec_4koma_PC-*.py）が共通で使う、コマごとの図の指示文の部品。
土地家屋調査士法編（note-articles/sokatsu-zukai/03-chousashi-hou/src/spec_4koma_C1-*.py）で check_prompt.py を通った文面と同じ書き方にそろえてある。
標準ライブラリのみ。画像の中に入る文言は、すべて「」で囲んだ引数だけ（文言の正本は構成表）。"""

NUM = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}
DOT = ("a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers)")


def q(t):
    return f"「{t}」"


def cards_stack(cards, badge):
    """コマ1（chars=side）：中央に縦に積んだカード2〜4枚と、上の疑問バッジ。矢印・印なし。"""
    n = len(cards)
    return [
        f"A diagram in the center, about 56 percent of the panel width: {NUM[n]} SEPARATE cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, {DOT}, and one dark navy text line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.",
        " ".join(f"Card {i}: {q(c)}." for i, c in enumerate(cards, 1)),
        f"At the top, a small question badge in a gray fill with dark navy text {q(badge)} (a question badge only, with no check mark and no cross).",
        "There is no check mark and no cross anywhere in this panel.",
    ]


def two_cards(tag, line, left, right, band):
    """コマ2（chars=none）：左右2枚の同じ大きさのカード（見出し・小さなタグ・本文1〜3行）と、下の帯。印なし。
    left / right = (見出し, タグ, [本文の行]) 。band は None 可。"""
    def card(side, c):
        h, t, bl = c
        n = NUM[len(bl)]
        return f"{side} card, heading {q(h)}, a small tag {q(t)}, {n} body line{'s' if len(bl) > 1 else ''}: " + ", ".join(q(b) for b in bl) + "."
    out = [
        f"A small dark navy tag {q(tag)} at the top left, with one line beside it: {q(line)}.",
        "Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.",
        card("Left", left),
        card("Right", right),
    ]
    if band:
        out.append(f"Under the two cards, one wide dark navy band with large white text {q(band)}.")
    out.append("The two cards have clearly different texts; the texts are NOT identical.")
    return out


def stack_and_list(top, bottom, list_head, rows, ribbon, ribbon_hl, hl_rows=()):
    """コマ3（chars=faces, opposite=lx）：左に上下2枚（上＝赤✕1個・下＝青✓1個）、右に会話の下の整理カード。
    top / bottom = (見出し, 本文)。rows = 整理カードの行（2〜6行）。hl_rows = 黄色マーカーを付ける行の番号（1始まり）。"""
    n = NUM[len(rows)]
    ordw = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth"}
    hl_txt = ""
    if hl_rows:
        if len(hl_rows) == 1:
            hl_txt = f", with the {ordw[hl_rows[0]]} row highlighted with a yellow marker"
        else:
            hl_txt = ", with the " + " and ".join(ordw[i] for i in hl_rows) + " rows highlighted with a yellow marker"
    return [
        "LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.",
        f"Top card, heading {q(top[0])}, body {q(top[1])}, and ONE red cross only at the bottom of this card (no check mark on this card).",
        f"Bottom card, heading {q(bottom[0])}, body {q(bottom[1])}, and ONE blue check mark only at the bottom of this card (no cross on this card).",
        f"RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading {q(list_head)}, with the same pale gray fill and a dark navy outline, containing exactly {n} short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: "
        + ", ".join(q(r) for r in rows) + f"{hl_txt}. Under the {n} rows, one small dark navy ribbon tag with white text {q(ribbon)}"
        + (f", with the text {q(ribbon_hl)} highlighted with a yellow marker." if ribbon_hl else "."),
        "The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.",
    ]


def stack_only(top, bottom):
    """コマ3（chars=faces, opposite=lx）で、右は会話4つだけ（整理カードなし）。左に上下2枚（上＝赤✕・下＝青✓）。"""
    return [
        "LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.",
        f"Top card, heading {q(top[0])}, body {q(top[1])}, and ONE red cross only at the bottom of this card (no check mark on this card).",
        f"Bottom card, heading {q(bottom[0])}, body {q(bottom[1])}, and ONE blue check mark only at the bottom of this card (no cross on this card).",
        "The left cards have clearly different texts; the texts are NOT identical.",
    ]


def step_cards(steps, ribbon=None, ribbon_step=None):
    """コマ3（chars=faces、印なし）：左に3枚のステップカード（見出し＋本文）。ribbon_step のカードに、濃紺のリボンを1つ付ける。"""
    n = NUM[len(steps)]
    out = [f"{n.capitalize()} step cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading, with no check mark and no cross. The step cards are separated only by a small empty gap, with nothing drawn between them."]
    for i, (h, b) in enumerate(steps, 1):
        extra = f", a dark navy ribbon tag with large white text {q(ribbon)}" if (ribbon and ribbon_step == i) else ""
        out.append(f"Step card {i}: heading {q(h)}{extra}, body {q(b)}.")
    out.append("There is no check mark and no cross anywhere in this panel.")
    return out
