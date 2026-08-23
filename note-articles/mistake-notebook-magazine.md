# 「間違いノート」マガジン（周回別）の見出し画像プロンプト・説明文

## これは何か

令和7年度〜平成20年度の解説記事で1周目の学習を終えたあと、2周目以降に**間違えた問題だけを集めて登録していくマガジン**（間違いノート）用の、見出し画像プロンプトとマガジン説明文のテンプレートである。

年度別マガジン（`magazine-descriptions.md`参照）が「年度ごとに1マガジン、基本デザインは同じで年度の数字だけが変わる」構成だったのと同じ考え方で、こちらは**「周回ごとに1マガジン、基本デザインは同じで周回数と差し色だけが変わる」**構成にする。同じ問題を何周も間違えているかどうかを周回ごとに見比べることで、自分の弱点をあぶり出し、補強していくための記録用マガジンという位置づけである。

## 周回ごとの色の割り当て

周回が増えるたびに、以下の順で差し色を変えていく（8周目以降はこの並びを再度繰り返す）。

| 周回 | 差し色 | 英語指定（プロンプト用） |
|---|---|---|
| 2周目 | 青 | soft pastel blue |
| 3周目 | 緑 | soft pastel green |
| 4周目 | オレンジ | soft pastel orange |
| 5周目 | 赤 | soft pastel red |
| 6周目 | 紫 | soft pastel purple |
| 7周目 | 黄 | soft pastel yellow |

## 見出し画像プロンプト（1280×670px、テンプレート）

年度別マガジンと同じく、note.comの見出し画像仕様（1280×670px、実際にマガジンヘッダーとして表示されるのは縦方向中央の1280×216px＝y=227〜443pxの帯のみ）に従う。`{ROUND}`（周回数、例：2）と`{COLOR}`（上表の英語指定）の2箇所だけを差し替えれば、そのまま次の周回にも使い回せる。

```
Create a landscape magazine header image, EXACTLY 1280×670 pixels,
clean flat-design isometric illustration style with soft pastel colors
(base palette: beige, gray, white; accent color: {COLOR}), consistent
with a modern explainer-graphic aesthetic used throughout this note.com
magazine series about the 土地家屋調査士 (Land and House Surveyor) exam.

CANVAS SAFE-ZONE REQUIREMENT (critical): Only the vertical center band
from y=227px to y=443px (a 216px-tall horizontal strip, centered in the
670px-tall canvas) will actually be visible when this image is displayed
as the magazine header on note.com. The title text and any other
essential readable content MUST be fully contained within this y=227–443
band, horizontally centered across the full 1280px width. Everything
above y=227px and below y=443px is decorative background only — treat
those areas as a soft, low-contrast extension of the scene so the image
still looks complete when the FULL 1280×670 canvas is shown (on the
magazine's own top page or when shared on X/Twitter), but do not place
any text or critical icon detail there.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Pay special attention to the kanji
間・違・周, which must be rendered in their standard Japanese (Jōyō) form,
stroke-for-stroke, not as Simplified Chinese variants. Reproduce the
exact text strings given below verbatim — do not paraphrase, translate,
or substitute any characters.

--- COMPOSITION ---
Background (spans the full 1280×670 canvas): a soft isometric desk scene
in beige/white/gray tones — a stack of past-exam notebooks, a red
correction pen resting on an open page with a few small red circle marks
and check marks on it (representing corrected mistakes), a magnifying
glass hovering over one of the circled items. A faint circular arrow
(周回・繰り返しを示す) loops gently in the background, rendered in
{COLOR} at low opacity. Keep the top ~150px and bottom ~150px of the
canvas soft and low-detail (outside the safe zone).

--- CENTER SAFE-ZONE CONTENT (y=227–443px, horizontally centered) ---
A large, bold, rounded-corner card or ribbon banner (soft white,
subtle drop shadow, a thin {COLOR} border) spanning most of the 1280px
width, positioned so it sits fully within y=227–443px. Inside this
banner, stacked and centered both horizontally and vertically:

Line 1 (large, bold):
間違いノート

Line 2 (smaller, directly below line 1, in a small rounded {COLOR}
pill-shaped badge):
{ROUND}周目

No other text anywhere on the canvas. A small decorative icon (a red
check mark or a circular arrow, isometric flat style) may sit beside
the text within the same banner, in {COLOR}.

Final check before rendering: confirm the canvas is exactly 1280×670
pixels. Confirm the text "間違いノート" and "{ROUND}周目" are rendered
verbatim, in standard Japanese Jōyō kanji (not Simplified Chinese), and
are fully contained within the y=227–443px horizontal band, centered
left-to-right. Confirm no other text appears anywhere on the canvas.
Confirm the accent color used for the badge, border, and background
loop-arrow is {COLOR}, and that the area above y=227px and below
y=443px contains only soft, low-detail background illustration with no
essential content.
```

### 使用例（2周目）

`{ROUND}` → `2`、`{COLOR}` → `soft pastel blue` を当てはめて生成する。3周目以降も同様に、上表の周回・色をそのまま差し替えるだけでよい。

## マガジン説明文（テンプレート）

年度別マガジン説明文（`magazine-descriptions.md`）と同じく「学習ノート」のトーンで統一する。`{ROUND}`（周回数）のみを差し替える。

```
土地家屋調査士試験の過去問を{ROUND}周目に解き直して間違えた問題だけを
集めた、学習ノートです。同じ問題を何周も間違えていないかを周回ごとに
見比べることで、自分の弱点をあぶり出し、補強していくために作成してい
ます。教材としてまとめたものではなく、学習の過程をそのまま記録した
マガジンです。
```

### 使用例（2周目）

```
土地家屋調査士試験の過去問を2周目に解き直して間違えた問題だけを集めた、
学習ノートです。同じ問題を何周も間違えていないかを周回ごとに見比べる
ことで、自分の弱点をあぶり出し、補強していくために作成しています。
教材としてまとめたものではなく、学習の過程をそのまま記録したマガジン
です。
```
