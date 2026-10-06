## 【土地家屋調査士受験生向け】何度も同じところで間違える人へ〜苦手分析シリーズ③床面積算入の判定フロー〜

**対象条文：不動産登記規則115条、不動産登記事務取扱手続準則81条4項・82条1号・6号・7号・8号**

この記事は、これまでの解答結果を分野別に振り返ったときに「一度ではなく複数の年度にわたって同じ論点で間違えている」と判明した分野を整理し直す苦手分析シリーズの第3回です。今回は、建物の床面積の算入・不算入の判定基準が定着しにくいという点を取り上げます。床面積の算定方法そのもの（不動産登記規則115条）は、`yukamenseki-sannyu.md`で算入する・しないの全ケースを号ごとに一覧化済みです。この記事では、過去に繰り返し間違えている4つの個別ケース（平成28年度第12問・天井高、平成29年度第16問・屋根裏部屋、平成30年度第13問・エレベーター室、令和5年度第12問・塔屋）を、実際に問題文を読んだときにたどる判定の順序として整理し直します。

---

### 手順1：算定の基準線を確認する

区分建物の専有部分は「内法」（壁その他の区画の内側線）、それ以外（一棟の建物全体を含む）は「壁芯」（壁その他の区画の中心線）で、各階ごとの水平投影面積を算定します（不動産登記規則115条）。

### 手順2：低い天井の部分は「独立した階」か「一室の一部」かを見分ける

天井の高さが1.5メートル未満の**地階・屋階そのもの（特殊階）は、その階全体を床面積に算入しません**（準則82条1号本文）。一方、天井高1.5メートル未満の部分が独立した階ではなく**通常の一室の中の一部にすぎない場合は、その低い部分を含めて一室全体を算入します**（同号ただし書）。

**注意（混同しやすいポイント）**：屋根裏部屋の高さが問題になる平成29年度第16問は、実は「床面積」ではなく「**階数**」への算入を問うものです。天井高1.5メートル未満の屋根裏部屋は建物の階数に算入されず（準則81条4項）、1.5メートル以上あれば独立した1つの階として階数に算入されます。同じ「1.5メートル」という数字でも、①床面積不算入の基準（準則82条1号）と②階数不算入の基準（準則81条4項）は根拠条文が異なる別の場面であり、この2つを混同しないことが重要です。

### 手順3：階段室・エレベーター室・吹抜けかどうかを確認する

階段室、エレベーター室またはこれに準ずるものは、床を有するものとみなして**各階の**床面積に算入します（準則82条6号）。「1階部分にだけ算入する」という扱いは誤りです。一方、建物の一部が上階まで吹抜けになっている場合、その吹抜け部分は**上階**の床面積には算入しませんが、吹抜けの起点となる床がある階（多くは1階）は通常どおり算入します（同条8号）。「吹抜けだから丸ごと不算入」ではなく、階ごとに床の有無で判断する点に注意してください。

### 手順4：外気分断性の有無を確認する（利用上の必要性では判断しない）

外気分断性のない屋外階段は、屋根や手すりの有無にかかわらず床面積に算入しません（準則82条7号。条文は「建物に附属する屋外の階段は、床面積に算入しない」と定めています）。玄関・車寄せ・ベランダも、外気と分断されていなければ建物の一部と認められず算入しない、と整理されます（条文に明記はなく、令和4年度第12問の記事の整理に従っています）。ここでの判断軸は「その場所が実際によく使われているか」ではなく、あくまで「外気と分断されているか」です。ガラス扉や壁で四方を囲んだ風除室のように、外気と分断されていれば算入します。

### 手順5：塔屋・PS等は「一部でも実用に供されているか」を確認する（逆方向の例外）

エレベーター機械室・階段室・高置水槽・冷却装置など、屋上に出入りするためだけの設備を収容する塔屋は、天井高が1.5メートル以上でも階数・床面積に算入しません（先例昭和38年10月22日民甲2933号）。**ただし、その塔屋の一部でも管理事務所や倉庫として実用に供されている場合は、未使用部分を含めた塔屋全体を建物の床面積に算入します**。他の論点の多くが「一部だけなら不算入部分に留める」方向であるのに対し、塔屋は「一部でも使えば全体が算入に転じる」という逆方向の例外である点が、間違いやすい理由です。

### まとめ

床面積の算入・不算入は、部位ごとに丸暗記するよりも「その部分は独立した空間か、それとも既にカウント対象になっている空間の一部か」という視点で判定すると整理しやすくなります。特に、天井高1.5メートルという同じ数字が床面積（準則82条1号）と階数（準則81条4項）という別の場面で使われている点、吹抜けは階ごとに床の有無で判断する点、外気分断性という判断軸そのものを見落としやすい点、塔屋だけは一部使用で全体が算入に転じる逆方向の例外である点の4つは、繰り返し間違えやすいポイントとして意識してください。

---

**確認事項**

- 床面積算入の判定フローは、`note-articles/h28-mondai/q12-tatemono-kouzou-yukamenseki.md`、`note-articles/h29-mondai/q16-tatemono-kouzou.md`、`note-articles/h30-mondai/q13-yukamenseki.md`、`note-articles/r5-mondai/q12-yukamenseki.md`、および既存の総合整理記事`note-articles/topics/yukamenseki-sannyu.md`の内容に基づいています。
- 塔屋の例外は条文本体ではなく先例（昭38.10.22民甲2933号）を根拠とする実務上の取扱いである点は、既存記事の記載どおりです。

- 【2026-10-05 条文再チェックで訂正】準則82条には項がないため、「82条1項○号」の表記を「82条○号」「同条8号」に統一しました。早見表の階段室・エレベーター室の行の「常に」「該当なし」を、屋上出入り専用の階段室（塔屋）は先例で不算入である旨に合わせました。
- 準則82条7号の原文は「建物に附属する屋外の階段は、床面積に算入しない」で、玄関・車寄せ・ベランダは条文にありません。これらを不算入とするのは、外気分断性による整理（令和4年度第12問の記事の整理）です。7号の文言は、ユーザーから受け取った準則第82条の全文（11号まで）と、`note-articles/laws/fudousan-touki-jimu-junsoku.md`で一致を確認しました（2026-10-05）。
- 条文（不動産登記規則115条、不動産登記事務取扱手続準則81条4項・82条1号・6号・7号・8号）は、`note-articles/laws/fudousan-touki-kisoku-1.md`と`note-articles/laws/fudousan-touki-jimu-junsoku.md`の原文と照合しました。準則82条7号の原文は「建物に附属する屋外の階段は、床面積に算入しない」だけです。会話式の項で玄関・車寄せ・ベランダを同じ考え方（外気と分断されていなければ算入しない）で述べた部分は、既存記事（令和4年度第12問の記事）の整理に従ったもので、条文の原文での直接確認はできていません（出典未確認）。また、本文の手順3の「同号8号」は、準則82条8号の意味です。
- 会話式の項で、屋上に出入りするためだけの階段室などは外気分断性があっても不算入のままとした点は、`note-articles/r4-mondai/q12-yukamenseki.md`の整理に従っています。塔屋の扱いが条文ではなく先例に基づく点は、本文と同じです。
- 会話式解説の項の、床面積算入の場面イメージ図と、誤解を正しい理解に変える図は、フローチャートではなく場面の絵です。機械点検の対象外で、画像生成AIでの生成・目視確認はまだ行っていません。

---

## 見出し画像用フレーズ

- 塔屋は一部使うと、全体が床面積に算入されるんです
- 同じ「1.5メートル」でも、床面積と階数では意味が違うんです
- 吹抜けは、階ごとに床の有無で判断するんです
- 外気分断性がなければ、屋根があっても算入されないんです

---

## 会話式の見出し画像プロンプト（キャラクターあり）

noteの見出し画像（アイキャッチ）用です。会話式の解説の記事に添える画像で、図解の画像とは違い、トリ先生と藍子を描きます。キャラクターは、別に渡すキャラクターシートに合わせます。サイズは1280x670pxです。

```
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky
(light blue, cream, fresh green), gentle clouds, clean outlines, consistent with
the supplied reference header image. Keep exactly the same overall layout:
the title block at the top center, the two characters at the bottom center,
and topic scenes fading softly into the left and right edges.

CHARACTERS (critical): follow the supplied character sheet exactly and do not
redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue
shirt, red neckerchief) standing at the lower left of center with one wing
raised as if explaining. 藍子 is the young woman exam candidate (long wavy
brown hair, blouse with thin blue vertical stripes) at the lower right of
center, resting her chin on one hand with a pen, looking up at トリ先生
with a curious smile, an open textbook on the desk in front of her. Keep
both characters facing each other and fully visible, with their faces
clear of the title text.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Within this English prompt text, use half-width
parentheses ( ) consistently — never open a parenthetical with a
full-width （ and close it with a half-width ), or vice versa.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the panels — with a solid or illustrated opaque background
(the pale beige/gray tone used elsewhere in this style is a good
default). There must be no checkerboard pattern, no partially transparent
area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese
title in two lines at the top center, over a soft white cloud-shaped glow
so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke
behind it:
床面積算入の判定を
Line 2 is larger; the phrase 5つの場面 is red-orange and the rest is dark navy:
5つの場面でつかむ
Below the title, a light blue rounded pill-shaped subtitle band with navy
text:
苦手分析シリーズ③ 床面積算入の判定
Do not write any other text anywhere in the image: no captions, no labels,
no signs with letters, no watermark, no panel numbers.

BACKGROUND SCENES (illustration only, no text on any object; keep them soft
and slightly faded so they never compete with the title or the characters):
Left side: a cross-section of a two-story house with a low sloped attic ceiling, and a measuring tape
Right side: an open stairwell void inside a building, an elevator shaft, and a rooftop tower on a small building

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep
the characters and the title away from the extreme edges so the image
survives center cropping. Do not draw any flowchart, diamond, arrow between
boxes, or ✓ or ✕ mark.

Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 分, 分, 床, 面, 積, 算, 入, which have visually similar but structurally different Simplified or Traditional Chinese counterparts. If any character renders as a Simplified or Traditional Chinese variant, redraw that character in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji, and remove it. Confirm the title and subtitle are reproduced exactly as written, that the image is 1280x670 landscape, that the characters match the supplied character sheet, and that the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

---

## インフォグラフィック プロンプト

### 画像1：床面積算入の判定フロー(1/2)〜天井高と階数の違い〜

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, red, beige, gray), rounded panel sections, consistent with a
modern explainer-graphic aesthetic (icons: a decision-diamond shape, a
room with a low ceiling nook, an attic room, a registrar figure, checkmarks
and X marks).

GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference
flowchart poster, NOT a text-heavy explainer document. There is NO intro
illustration and NO paragraph of prose anywhere on this poster — go
straight from the header to the flowchart nodes. Each node must
communicate its point almost entirely through the illustration (icons,
arrows, ✕/✓ marks, short embedded labels) plus one short label. Do NOT
render any full-sentence explanation or legal citation anywhere on the
poster, except the two short callout boxes explicitly specified below.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either. Reproduce the exact text strings
given below verbatim — do not paraphrase, translate, summarize, or
substitute any characters. Pay special attention to 準, 則, 号, 積, 段,
階, 床 — do not draw these as Simplified or Traditional Chinese variants.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances. Fill the full canvas — including every
corner and margin outside the flowchart — with a solid or illustrated
opaque background. There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image.

--- HEADER ---
Title (large, bold, 1行):
天井の低い部分、算入する?しない?

Subtitle (smaller, centered, 1行):
苦手分析シリーズ③床面積算入の判定フロー(1/2)

（タイトル・サブタイトルのすぐ下にフローチャートを続ける。導入イラスト・
導入文のブロックは置かない。）

--- FLOWCHART ---
Node 1 (start, isometric icon of a building cross-section showing a
low-ceiling area):
Label: "天井の高さ1.5メートル未満の部分がある"

Arrow down to Node 2 (diamond-shaped decision icon):
Label: "その部分は独立した地階・屋階(特殊階)そのものか、それとも一室の一部
にすぎないか?"

Left branch (labeled「特殊階そのもの」) arrow to Node 3A:
Label: "その階全体を床面積に算入しない"
Icon: a red ✕ mark over the entire low-ceiling floor, small footnote
"準則82条1号本文".

Right branch (labeled「一室の一部」) arrow to Node 3B:
Label: "低い部分を含めて一室全体を算入する"
Icon: a green checkmark covering the whole room including the low nook,
small footnote "準則82条1号ただし書".

--- CALLOUT: 混同注意 ---
同じ屋根裏部屋でも、天井高1.5メートル未満なら建物の「階数」には算入されず
(準則81条4項)、1.5メートル以上なら独立した1つの階として階数に算入され
ます。これは「床面積」ではなく「階数」の話であり、根拠条文も場面も別です。

--- FOOTER ---

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese. If any character renders as a Simplified or Traditional Chinese
variant, redraw that character in the correct Japanese form. Confirm the
flowchart has exactly the nodes described above with no duplicated or
missing nodes, confirm both branches from Node 2 lead to distinct
conclusion nodes with no looping arrow back to Node 2, confirm the
CALLOUT box text matches verbatim, confirm there is no intro illustration
or paragraph block between the header and the flowchart, confirm nothing
is rendered below the CALLOUT box other than the FOOTER's small footnote
text (no summary recap panel, no trophy or medal icon, and no additional
text block of any kind), and confirm the entire canvas, edge to edge, is
filled with a fully opaque background with no transparency or alpha
channel anywhere.
```

### 画像2：床面積算入の判定フロー(2/2)〜EV室・吹抜け・塔屋〜

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, red, beige, gray), rounded panel sections, consistent with a
modern explainer-graphic aesthetic (icons: a decision-diamond shape, an
isometric elevator shaft, a rooftop equipment room, checkmarks and X
marks).

GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference
flowchart poster, NOT a text-heavy explainer document. There is NO intro
illustration and NO paragraph of prose anywhere on this poster — go
straight from the header to the flowchart nodes. Each node must
communicate its point almost entirely through the illustration (icons,
arrows, ✕/✓ marks, short embedded labels) plus one short label. Do NOT
render any full-sentence explanation or legal citation anywhere on the
poster, except the one short callout box explicitly specified below.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either. Reproduce the exact text strings
given below verbatim — do not paraphrase, translate, summarize, or
substitute any characters. Pay special attention to 塔, 屋, 準, 則, 号,
断, 積 — do not draw these as Simplified or Traditional Chinese variants.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances. Fill the full canvas — including every
corner and margin outside the flowchart — with a solid or illustrated
opaque background. There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image.

--- HEADER ---
Title (large, bold, 1行):
エレベーター室・吹抜け・塔屋の判定

Subtitle (smaller, centered, 1行):
苦手分析シリーズ③床面積算入の判定フロー(2/2)

（タイトル・サブタイトルのすぐ下にフローチャートを続ける。導入イラスト・
導入文のブロックは置かない。）

--- FLOWCHART ---
Node 1 (start, diamond-shaped decision icon):
Label: "階段室・エレベーター室(またはこれに準ずるもの)か?"

Right branch (labeled「はい」) arrow to Node 2A:
Label: "床を有するものとみなし各階の床面積に算入する"
Icon: an isometric elevator shaft passing through multiple floors, every
floor shaded green with a checkmark, small footnote "準則82条6号".

Left branch (labeled「いいえ」) arrow to Node 2B (diamond-shaped decision
icon):
Label: "上階まで吹抜けになっている部分か?"

From Node 2B, right branch (labeled「はい」) arrow to Node 3A:
Label: "吹抜けの上階部分は算入しない(起点の階は算入する)"
Icon: an isometric building cross-section with an open void from floor 1
to floor 3, floor 1 shaded green (counted) and floors 2-3 void area shaded
gray with a red ✕, small footnote "準則82条8号".

From Node 2B, left branch (labeled「いいえ」) arrow to Node 4 (diamond-
shaped decision icon):
Label: "屋上の塔屋・PS等(設備室)か?"

From Node 4, right branch (labeled「はい」) arrow to Node 5 (diamond-
shaped decision icon, highlighted with a thick border):
Label: "その塔屋の一部でも管理事務所・倉庫として実用に供されているか?"

From Node 5, left branch (labeled「いいえ」) arrow to Node 6A:
Label: "階数・床面積に算入しない"
Icon: a rooftop equipment room icon (elevator machine room, water tank)
shaded gray with a red ✕, small footnote "先例昭38.10.22民甲2933号".

From Node 5, right branch (labeled「はい」) arrow to Node 6B:
Label: "未使用部分を含め塔屋全体を床面積に算入する"
Icon: the same rooftop equipment room icon, but the entire tower shaded
green with a checkmark, including a small unused corner section, small
footnote "一部使用で全体算入".

--- CALLOUT: 逆方向の例外 ---
多くの論点は「一部だけなら不算入部分にとどめる」方向ですが、塔屋だけは
「一部でも実用に供されれば全体が算入に転じる」逆方向の例外です。

--- FOOTER ---

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese. If any character renders as a Simplified or Traditional Chinese
variant, redraw that character in the correct Japanese form. Confirm the
flowchart has exactly the nodes described above (Node 1, 2A, 2B, 3A, 4, 5,
6A, 6B) with no duplicated or missing nodes, confirm every diamond
decision node shows both its はい and いいえ branches leading to distinct
destinations with no looping arrow back to an earlier node, confirm the
CALLOUT box text matches verbatim, confirm there is no intro illustration
or paragraph block between the header and the flowchart, confirm nothing
is rendered below the CALLOUT box other than the FOOTER's small footnote
text (no summary recap panel, no trophy or medal icon, and no additional
text block of any kind), and confirm the entire canvas, edge to edge, is
filled with a fully opaque background with no transparency or alpha
channel anywhere.
```

### 画像3：4つの判定ポイントまとめ（早見表型）

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded card sections, consistent with a
modern explainer-graphic aesthetic (icons: low-ceiling room, elevator
shaft, atrium void, rooftop equipment room).

GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference poster,
NOT a text-heavy explainer document. There is NO intro illustration and NO
paragraph of prose anywhere on this poster — go straight from the header
to the table. Each table row must communicate its point through a small
icon plus the short text specified for that row. Do NOT add any
explanation, illustration, or text beyond what is explicitly listed below.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either. Reproduce the exact text strings
given below verbatim — do not paraphrase, translate, summarize, or
substitute any characters. Pay special attention to 準, 則, 号, 積, 段,
階, 床, 塔, 屋, 断 — do not draw these as Simplified or Traditional
Chinese variants.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances. Fill the full canvas — including every
corner and margin outside the table — with a solid or illustrated opaque
background. There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image.

--- HEADER ---
Title (large, bold, 1行):
4つの判定ポイント、まとめて確認

Subtitle (smaller, centered, 1行):
苦手分析シリーズ③床面積算入の早見表

（タイトル・サブタイトルのすぐ下に表を続ける。導入イラスト・導入文の
ブロックは置かない。）

--- TABLE ---
Render as a clean flat-design table with alternating row background colors
(light green / white), Japanese sans-serif font, no monospace font. Each
row has a small isometric icon on the left, followed by the columns below.

Header row (4 columns, verbatim):
部位・ケース ｜ 算入する場合 ｜ 算入しない場合 ｜ 根拠

Data rows (numbered 1-4 in this exact order; reproduce every row exactly
as written; do not omit, duplicate, merge, reorder, or paraphrase any
row):

1. 部位・ケース: 天井高1.5メートル未満の部分
   算入する場合: 一室の一部にすぎない場合(低い部分を含め一室全体を算入)
   算入しない場合: 独立した地階・屋階(特殊階)そのものの場合
   根拠: 準則82条1号
   Icon: a room with a partially lowered ceiling nook, the nook shaded the
   same green as the rest of the room.

2. 部位・ケース: 階段室・エレベーター室
   算入する場合: 各階の床面積に算入する(床を有するものとみなす)
   算入しない場合: 屋上に出入りするためだけの階段室(塔屋)は先例で不算入
   根拠: 準則82条6号
   Icon: an isometric elevator shaft passing through multiple floors, every
   floor shaded green.

3. 部位・ケース: 上階までの吹抜け部分
   算入する場合: 起点となる床がある階(多くは1階)
   算入しない場合: 吹抜けの上階部分
   根拠: 準則82条8号
   Icon: an isometric building cross-section with an open void, the bottom
   floor shaded green and the void above shaded gray.

4. 部位・ケース: 塔屋・PS等(屋上の設備室)
   算入する場合: 一部でも管理事務所・倉庫として実用に供されている場合
    (未使用部分を含め全体を算入)
   算入しない場合: 設備収容のみで実用に供されていない場合
   根拠: 先例昭38.10.22民甲2933号
   Icon: a rooftop equipment room icon, half shaded green (in use) and half
   shaded gray (unused), both halves outlined the same to show the whole
   tower counts together.

Self-check instruction to embed in the image generation reasoning (not
rendered as visible text): confirm the table has exactly 4 data rows
corresponding to the list above, in the same order, with no row omitted,
duplicated, merged, or reworded.

--- FOOTER ---

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese. If any character renders as a Simplified or Traditional Chinese
variant, redraw that character in the correct Japanese form. Confirm the
table has exactly 4 data rows exactly matching the list above, with no
duplicated or missing rows, confirm there is no intro illustration or
paragraph block between the header and the table, and confirm that no row
contains any text beyond what is specified for that row.
```

---

## 会話でつかむ床面積算入の判定：天井・階段室・吹抜け・屋外・塔屋を具体的な場面で

フローチャートだとピンとこない人向けに、場面を頭に思い浮かべて、床面積に入れるか入れないかを見分ける練習をします。舞台は、2階建ての家を持つAさん、吹抜けのある家を持つBさん、5階建てのCビルを持つ会社、玄関ポーチのあるDさんの家、屋上に塔屋のあるFビルです。ここからは、トリ先生と藍子の会話です。

---

【登場人物】

**トリ先生**：見た目はぽっちゃりした鳥のキャラクター。調査士試験の要点と受験生の弱点を熟知している。口調は辛辣だが、初学者への愛は深い。

**藍子（アイコ）**：ブルーの細い縦じまが入ったブラウスにネイビーのスーツをパリッと着こなす受験生。まじめで素直だが、問題作成者の仕掛けたワナに見事に引っかかる猪突猛進な面も。

---

### 場面1：天井が低い部分は、「階そのもの」なのか「部屋の一部」なのか

**藍子**  
「トリ先生、床面積って、壁の外側で測るんですか、内側ですか？ それから、天井の高さが1.5メートル未満の部分は、床面積に入れないんですよね。Aさんの家の2階の洋室は勾配天井で、壁ぎわの1メートルくらいだけ、天井が1.4メートルしかありません。その壁ぎわは引いて計算しますよね？」

**トリ先生**  
「質問を2つ同時に投げてくるんじゃないわよ。順番にいくわ。まず線の引き方。床面積は、各階ごとに、壁その他の区画の中心線で囲まれた部分の水平投影面積よ（規則115条）。区分建物の専有部分だけは、中心線ではなく内側線。ここは最初に決めておきなさい。

次、天井の低い部分。あんた、『1.5メートル未満は不算入』と、数字だけ覚えて、何が不算入なのかを見ていないでしょ。不算入なのは、天井の高さが1.5メートル未満の『地階と屋階』、つまり特殊階。階そのものの話よ（準則82条1号）。

洋室の壁ぎわは、階じゃなくて、一室の一部にすぎない。一室の一部が1.5メートル未満でも、その部分を含めた一室全体を面積に入れるの（同号ただし書）。引いたら、あんたの答えは小さくなって、不正解よ」

**藍子**  
「階そのものと、一室の一部。どうやって見分けるんですか？」

**トリ先生**  
「想像のしかたを教えるわ。その低い部分に『何階』と名前をつけて呼べるかを考えなさい。Bさんの建物は、2階建ての天井の上に、一番高い所でも天井が1.4メートルの屋根裏があって、物置にしている。これは『屋根裏という階』の話だから、階ごと床面積に入らない。

Aさんの洋室の壁ぎわには、階の名前がつかない。『洋室のすみっこ』でしょ。すみっこの話か、階の話か。ここを分けるの。すみっこなら、低くても部屋ごと算入。階ごと低いなら、階ごと不算入よ」

> 【画像挿入】場面イメージ図の、パネル1（天井の低い部分は、階そのものか、部屋の一部か）。画像のプロンプトは、この下の「図解プロンプト（床面積算入の場面イメージ図1枚）」にあります。この場面だけを1枚で使う画像のプロンプトは、下の「図解プロンプト（場面ごとに1枚ずつ使う場合）」の場面1。

---

### 場面2：同じ1.5メートルでも、屋根裏部屋は「階数」の話

**藍子**  
「Aさんの家は2階建てで、天井の上に、収納式のはしごで上がる屋根裏物置があります。床から天井までは1.5メートルちょうどです。建物の構造の表示を聞かれたら、屋根裏は床面積に入らないから、2階建てのままですよね？」

**トリ先生**  
「ほら、1.5メートルという数字を見た瞬間に、頭の中の『床面積』のスイッチが入ったでしょ。問われているのは、構造欄の『階数』よ。床面積じゃない。同じ1.5メートルでも、使う場面が2つあるの。

1つ目は床面積。天井高1.5メートル未満の地階・屋階は、床面積に算入しない（準則82条1号）。2つ目は階数。天井高1.5メートル未満の地階・屋階は、階数に算入しない（準則81条4項）。根拠の条文が違う、別の場面なの。問いの最後の一文を読んで、床面積を聞かれているのか、階数を聞かれているのかを、まず確かめなさい」

**藍子**  
「では、この屋根裏は、結局どうなりますか？」

**トリ先生**  
「1.5メートルちょうどは、『未満』じゃない。だから特殊階にならず、階数に算入される。2階建てに屋根裏が1つ足されて、3階建てよ。『ちょうど』に引っかかる受験生が毎年いるの。

もし天井が1.4メートルなら、特殊階だから階数に算入しなくて、2階建てのまま。想像のしかたは、『未満』という言葉に線を引いて、1.5メートルそのものは線の内側に入っていないと、心の中でつぶやくこと。ちなみに、1.5メートルちょうどなら、床面積のほうでも特殊階ではないから、不算入の対象にならないわ」

> 【画像挿入】場面イメージ図の、パネル2（屋根裏部屋の天井高と階数）。この場面だけを1枚で使う画像のプロンプトは、下の「図解プロンプト（場面ごとに1枚ずつ使う場合）」の場面2。

---

### 場面3：エレベーター室は各階、吹抜けは階ごとに床の有無を見る

**藍子**  
「5階建てのCビルで考えます。エレベーターは、乗り場のある1階に床があるので、エレベーター室の床面積は1階だけに入れるんですよね？」

**トリ先生**  
「出たわね、『見えている床しか数えない』病。階段室、エレベーター室、またはこれに準ずるものは、床を有するものとみなして、各階の床面積に算入するの（準則82条6号）。昇降路は1階から5階までを貫いているでしょ。5階建てなら、5つの階すべてに入れる。1階だけは誤りよ」

**藍子**  
「それなら、吹抜けも、空洞だから丸ごと不算入ですか？」

**トリ先生**  
「今度は急に、何でも不算入に振れたわね。その極端さが藍子の悪いところ。吹抜けは、階ごとに床があるかどうかで見るの。

Bさんの家で、玄関ホールが1階から2階の天井まで吹抜けだとする。1階には床があるから、ふつうに算入。2階の吹抜けの部分には床がないから、2階の床面積には入れない（準則82条8号）。外すのは『上階の吹抜けの部分』だけ。起点の階まで不算入にしないこと」

**藍子**  
「エレベーターと吹抜けで、考え方が逆に見えて混乱します」

**トリ先生**  
「どっちも、階ごとに床があるかを問うているのよ。エレベーター室は、床を有するものとみなすから、各階に床があるの。吹抜けは、上の階に床が実際にないから、上の階には入れない。階ごとに『床があるか』と問う癖をつけなさい」

> 【画像挿入】場面イメージ図の、パネル3（エレベーター室と吹抜け）。この場面だけを1枚で使う画像のプロンプトは、下の「図解プロンプト（場面ごとに1枚ずつ使う場合）」の場面3。

---

### 場面4：屋根があっても、よく使っても、決め手は外気分断性

**藍子**  
「Dさんの家の玄関ポーチは、屋根も手すりもついていて、毎日必ず通る場所です。屋根まであるし、よく使うから、床面積に入ると思います」

**トリ先生**  
「理由を2つ並べたけど、どっちも判断軸じゃないの。屋根があるかどうかも、よく使うかどうかも、関係ない。見るのは、外気と分断されているかどうか。壁や扉で囲って外と切り離されていれば、建物の中。吹きさらしなら、外よ。

屋外の階段は、明文で床面積に算入しないとされているわ（準則82条7号）。玄関、車寄せ、ベランダは、条文には書いていないけれど、同じ考え方で、外気と分断されていなければ算入しないと整理するの。屋根と手すりがあっても、結論は変わらない」

**藍子**  
「Eさんのアパートの外階段は、鉄製で、上らないと2階の部屋に行けません。これは、必要な設備だから算入ですよね？」

**トリ先生**  
「必要かどうかは、また別の話。壁と屋根で囲まれていない屋外階段は、必要でも不算入。逆に、Dさんが玄関ポーチを壁とサッシで囲って、外気と遮断した玄関ホールにしたら、外と分断されるから、算入の方向に変わる。想像のしかたは、冬にそこに立ったとき、風が吹き抜けるかどうか。吹き抜けるなら外気とつながっている。判断軸は『外気分断性』だけ、と唱えなさい」

> 【画像挿入】場面イメージ図の、パネル4（外気分断性）。この場面だけを1枚で使う画像のプロンプトは、下の「図解プロンプト（場面ごとに1枚ずつ使う場合）」の場面4。

---

### 場面5：塔屋だけは、「一部でも使えば全体」が逆向きに働く

**藍子**  
「屋上の塔屋は、エレベーターの機械室や階段室だけなら、天井が2.5メートルあっても算入しないと覚えました。Fビルは、その塔屋の一角を管理事務所と倉庫に使っています。使っていない所は機械室のままだから、使っている所だけ算入するんですよね？」

**トリ先生**  
「ここまで『一部なら不算入にとどめる』を習ってきたから、同じ癖で切り分けようとしたわね。塔屋だけは逆向きなの。一部でも管理事務所や倉庫として実用に供されていれば、使っていない部分も含めて、塔屋全体を床面積に算入する。切り分けは禁止よ。

この塔屋の扱いは、条文の本体には明記が見当たらなくて、先例に基づく実務上の取扱いなの。条文を探しても出てこないから、整理して覚えなさい」

**藍子**  
「機械室だけの塔屋なら、不算入で間違いないですよね。壁で囲まれていて、外気とも分断されていますけど、それでも不算入ですか？」

**トリ先生**  
「いい質問。屋上に出入りするためだけの階段室や、設備を収容するだけの塔屋は、外気分断性があっても不算入のまま。外気分断性で決める場面と、塔屋の場面を混ぜないこと。

想像のしかたは、塔屋は『屋上に出入りするためだけ、設備を入れるだけの箱』と考えること。一角でも人が働いたり、物を保管したりする部屋になった瞬間、ただの設備の箱ではなくなる。箱ごと扱いが変わる、と覚えなさい」

> 【画像挿入】場面イメージ図の、パネル5（塔屋）。この場面だけを1枚で使う画像のプロンプトは、下の「図解プロンプト（場面ごとに1枚ずつ使う場合）」の場面5。

---

### 誤解を正しい理解に変える

**藍子**  
「今のお話で、私が思い込んでいたことが何なのか、整理したいです」

**トリ先生**  
「いい心がけよ。あんたは、数字や見た目に引っ張られて、判断軸を取り違えてるの。1つずつ直しなさい。

『天井が1.5メートル未満の部分は不算入』は、階そのものの話。一室の一部なら、一室全体を算入する。『1.5メートルは床面積の話』も、思い込み。階数の話は別の条文で、1.5メートルちょうどなら階数に算入される。『エレベーター室は1階だけ』は誤りで、各階に算入する。『吹抜けは丸ごと不算入』も誤りで、上階の吹抜けの部分だけを外す。

『屋根があるから、よく使うから算入』は、判断軸が違う。決め手は外気分断性。最後に、塔屋は設備だけなら不算入だけど、一部でも実用に供せば、全体を算入。ここだけ逆向きよ」

> 【画像挿入】誤解を正しい理解に変える図（5つの思い込みと、その訂正）。画像のプロンプトは、この下の「図解プロンプト（誤解を正しい理解に変える図1枚）」にあります。

---

### 床面積算入の判定のまとめ

**藍子**  
「自分の言葉でまとめます。まず、線は壁の中心線で、区分建物の専有部分だけ内側線です。天井が1.5メートル未満の部分は、階そのもの、つまり地階や屋階なら不算入です。でも、一室の一部なら、その部分も含めて一室全体を算入します。

同じ1.5メートルでも、屋根裏部屋の階数は別の話で、1.5メートル未満なら階数に算入せず、1.5メートルちょうどなら算入します。エレベーター室は各階に算入し、吹抜けは上階の吹抜けの部分だけ外します。

外気と分断されていない屋外階段などは、屋根や手すりがあっても算入しません。塔屋は、設備だけなら不算入ですが、一部でも実用に供されていれば、全体を算入します」

**トリ先生**  
「合格点よ。ほめてるの、ちゃんと。迷ったら、『何の話か（床面積か階数か）』『階か、一室の一部か』『階ごとに床があるか』『外気と分断されているか』『塔屋は一部でも使っているか』の順に問いなさい。次の過去問で、ちゃんと絵を描きなさいよ」

---

### 図解プロンプト（床面積算入の場面イメージ図1枚）

この図は、フローチャートではなく、場面のイメージを5つ並べる構成です。上のインフォグラフィック3枚とは別で、機械点検の対象ではありません。

```
Create a Japanese-language infographic, portrait layout, 1080x3400 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded panel sections, consistent with a
modern explainer-graphic aesthetic, built as a set of 5 panels (a "scene illustrations that make the floor area inclusion rules easy to picture" study reference). Each panel is one scene illustration, not a
flowchart.

SCENE-ILLUSTRATION REQUIREMENT (critical): Do NOT draw any flowchart, any
diamond-shaped branch node, or any arrows that connect boxes to each other.
Each panel shows concrete everyday scenes drawn as isometric illustrations,
with only the short captions written below, verbatim. Do not draw any recurring guide characters, mascots or portrait characters
(no bird character, no woman exam candidate) in any panel; show only the scenes and captions. Reproduce every caption exactly as written. Do not draw ✓ or ✕
marks anywhere in this image. Do not include case or precedent numbers.
Keep the text inside each panel to the captions and labels given below;
make each caption fully visible and not covered by any shape.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Within this English prompt text, use half-width
parentheses ( ) consistently — never open a parenthetical with a
full-width （ and close it with a half-width ), or vice versa.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the panels — with a solid or illustrated opaque background
(the pale beige/gray tone used elsewhere in this style is a good
default). There must be no checkerboard pattern, no partially transparent
area, and no unpainted canvas edge anywhere in the final image.

--- HEADER ---
Title (large, bold, 2行):
床面積に入れるか、入れないか
5つの場面でつかむ

Subtitle (smaller, centered, 1行):
苦手分析シリーズ③ 床面積算入の判定 場面1〜5

（タイトル・サブタイトルのすぐ下にパネル群を続ける。導入イラスト・導入文の
ブロックは置かない。）

--- PANEL 1 ---
Badge: a filled circle in blue containing the number 1.
Heading (bold, ONE line):
天井の低い部分は、階か部屋の一部か
Scene: two scenes side by side inside one panel. Left: a cutaway of a Western-style room in Mr. A's house with a sloped ceiling, where only the strip along one wall is low, and the whole room floor is shaded green. Caption (verbatim): 部屋のすみっこなら一室全体を算入 . Right: a cutaway of a whole attic floor above the second floor in Mr. B's house, where the ceiling is low everywhere, and the whole attic floor is shaded gray. Caption (verbatim): 階ごと低いなら階ごと不算入
Conclusion tag (a short blue banner, 5-15 Japanese characters):
すみっこか、階か

--- PANEL 2 ---
Badge: a filled circle in green containing the number 2.
Heading (bold, ONE line):
屋根裏部屋の天井高と階数
Scene: a 2-scene row, each a cross-section of a two-story house with an attic reached by a fold-down ladder. Scene 1: a ruler beside the attic reading 1.5メートル exactly, and the attic counted as a third floor with a small number tag 3階建 . Caption (verbatim): 1.5メートルちょうどは階数に算入する . Scene 2: a ruler beside the attic reading 1.4メートル, and the attic shaded gray, the house keeping a number tag 2階建 . Caption (verbatim): 1.5メートル未満は階数に算入しない
Conclusion tag (a short green banner, 5-15 Japanese characters):
ちょうどは未満ではない

--- PANEL 3 ---
Badge: a filled circle in orange containing the number 3.
Heading (bold, ONE line):
エレベーター室と吹抜け
Scene: a 2-scene row. Scene 1: a cross-section of Company C's five-story building with an elevator shaft running from the first to the fifth floor, each floor's shaft section shaded green. Caption (verbatim): エレベーター室は各階に算入する . Scene 2: a cross-section of Mr. B's house with an entrance hall open from the first floor up through the second floor, the first floor shaded green and the open part on the second floor shaded gray. Caption (verbatim): 吹抜けは上階の吹抜けの部分だけ外す
Conclusion tag (a short orange banner, 5-15 Japanese characters):
階ごとに床があるかを問う

--- PANEL 4 ---
Badge: a filled circle in blue containing the number 4.
Heading (bold, ONE line):
外気分断性
Scene: a 2-scene row. Scene 1: Mr. D's house with an entrance porch that has a roof and a handrail but no walls, and a gentle wind line passing through it, shaded gray. Caption (verbatim): 屋根があっても外気分断性がなければ算入しない . Scene 2: the same porch now enclosed with walls and a window sash into an entrance hall, no wind line passing through, shaded green. Caption (verbatim): 壁で囲んで外気と分断すれば算入の方向
Conclusion tag (a short blue banner, 5-15 Japanese characters):
決め手は外気分断性

--- PANEL 5 ---
Badge: a filled circle in green containing the number 5.
Heading (bold, ONE line):
塔屋は一部でも使えば全体
Scene: a 2-scene row, each a building rooftop with a small tower room. Scene 1: Building F's tower room containing only an elevator machine room and a stairwell, shaded gray. Caption (verbatim): 設備だけの塔屋は算入しない . Scene 2: the same tower room where one corner is a small management office with a desk and another corner a storage room, the whole tower shaded green with a thick outline around the entire tower. Caption (verbatim): 一部でも使えば塔屋全体を算入する
Conclusion tag (a short green banner, 5-15 Japanese characters):
一部使用で全体算入

--- FOOTER ---
Small footnote text (bottom of the image, small font, verbatim):
規則115条 準則81条4項 準則82条1号 6号 7号 8号

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, paying special attention to the kanji 床, 算, 入, 階, 屋, 裏, 吹, 抜, 塔, 断, 室, 外, 分, 気, which have visually
similar but structurally different Simplified or Traditional Chinese
counterparts. If any character renders as a Simplified or Traditional
Chinese variant, redraw that character in the correct Japanese form. Also
scan the entire canvas for any character that is not standard Japanese
hiragana, katakana, or Jōyō kanji — including any Chinese-only character,
Korean Hangul, other non-Japanese script, or stray decorative glyph — and
remove or redraw it so that only standard Japanese text appears anywhere in
the image. Confirm the panel count equals 5 exactly, badge numbers run 1-5 continuously, that every panel is a scene illustration, and that no flowchart, diamond or connecting arrow between boxes appears anywhere. Confirm there is no intro illustration or paragraph
block between the header and the panels, that no ✓ or ✕ mark appears
anywhere, that each 着眼点 callout states a checking order rather than only
a conclusion, confirm nothing is rendered below the footnote text (no
summary recap panel, no trophy or medal icon, and no additional text block
of any kind), and confirm the entire canvas, edge to edge, is filled with a
fully opaque background with no transparency or alpha channel anywhere.
```

### 図解プロンプト（誤解を正しい理解に変える図1枚）

この図は、フローチャートではなく、「思い込み」と「正しくは」を左右に並べる構成です。上の図とは別で、機械点検の対象ではありません。

```
Create a Japanese-language infographic, portrait layout, 1080x3600 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded panel sections, consistent with a
modern explainer-graphic aesthetic, built as a set of 5 panels (a "corrections that turn five easy misunderstandings about floor area inclusion into correct understanding" study reference). Each panel is one scene illustration, not a
flowchart.

SCENE-ILLUSTRATION REQUIREMENT (critical): Do NOT draw any flowchart, any
diamond-shaped branch node, or any arrows that connect boxes to each other.
Each panel shows concrete everyday scenes drawn as isometric illustrations,
with only the short captions written below, verbatim. Do not draw any recurring guide characters, mascots or portrait characters
(no bird character, no woman exam candidate) in any panel; show only the scenes and captions. Reproduce every caption exactly as written. Do not draw ✓ or ✕
marks anywhere in this image. Do not include case or precedent numbers.
Keep the text inside each panel to the captions and labels given below;
make each caption fully visible and not covered by any shape.
Each panel is divided into a left half and a right half. The left half is drawn in a muted gray tone and carries a caption beginning with the word 思い込み. The right half is drawn in a fresh green tone and carries a caption beginning with the word 正しくは. Do not draw any arrow between the two halves.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Within this English prompt text, use half-width
parentheses ( ) consistently — never open a parenthetical with a
full-width （ and close it with a half-width ), or vice versa.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the panels — with a solid or illustrated opaque background
(the pale beige/gray tone used elsewhere in this style is a good
default). There must be no checkerboard pattern, no partially transparent
area, and no unpainted canvas edge anywhere in the final image.

--- HEADER ---
Title (large, bold, 2行):
数字や見た目の思い込みを
正しい理解に直す

Subtitle (smaller, centered, 1行):
苦手分析シリーズ③ 床面積算入の判定 誤解を正す

（タイトル・サブタイトルのすぐ下にパネル群を続ける。導入イラスト・導入文の
ブロックは置かない。）

--- PANEL 1 ---
Badge: a filled circle in blue containing the number 1.
Heading (bold, ONE line):
1.5メートル未満は全部不算入という思い込み
Scene: left half (gray): a Western-style room cutaway where a low strip along one wall is cut off and left blank, the rest of the room shaded. Caption (verbatim): 思い込み　天井が低い部分は不算入 . Right half (green): the same room cutaway with the whole room including the low strip shaded green. Caption (verbatim): 正しくは　一室の一部なら一室全体を算入
Conclusion tag (a short blue banner, 5-15 Japanese characters):
階か部屋の一部か

--- PANEL 2 ---
Badge: a filled circle in green containing the number 2.
Heading (bold, ONE line):
1.5メートルは床面積の話という思い込み
Scene: left half (gray): a ruler reading 1.5メートル beside an attic with a floor-plan icon above it. Caption (verbatim): 思い込み　1.5メートルは床面積の話 . Right half (green): the same ruler beside the attic with a stack of floors icon above it showing a third floor added. Caption (verbatim): 正しくは　階数の話は別で1.5メートルちょうどは算入
Conclusion tag (a short green banner, 5-15 Japanese characters):
床面積と階数は別

--- PANEL 3 ---
Badge: a filled circle in orange containing the number 3.
Heading (bold, ONE line):
エレベーターと吹抜けの思い込み
Scene: left half (gray): an elevator shaft where only the first floor is shaded, and an open hall where the whole hall column is blank. Caption (verbatim): 思い込み　エレベーターは1階だけ、吹抜けは丸ごと不算入 . Right half (green): an elevator shaft shaded on every floor, and an open hall with the first floor shaded and only the second floor opening blank. Caption (verbatim): 正しくは　各階に算入し吹抜けは上階の部分だけ外す
Conclusion tag (a short orange banner, 5-15 Japanese characters):
階ごとに床を見る

--- PANEL 4 ---
Badge: a filled circle in blue containing the number 4.
Heading (bold, ONE line):
屋根や使用頻度で決めるという思い込み
Scene: left half (gray): a porch with a roof and a handrail and a daily footprint trail. Caption (verbatim): 思い込み　屋根があって使うから算入 . Right half (green): the same porch with a wind line passing through the open sides. Caption (verbatim): 正しくは　外気と分断されていなければ算入しない
Conclusion tag (a short blue banner, 5-15 Japanese characters):
決め手は外気分断性

--- PANEL 5 ---
Badge: a filled circle in green containing the number 5.
Heading (bold, ONE line):
塔屋は何があっても不算入という思い込み
Scene: left half (gray): a rooftop tower room with a small office in one corner but the tower drawn entirely gray. Caption (verbatim): 思い込み　塔屋は常に不算入 . Right half (green): the same tower with the office corner and the whole tower shaded green. Caption (verbatim): 正しくは　一部でも使えば塔屋全体を算入
Conclusion tag (a short green banner, 5-15 Japanese characters):
一部使用で全体算入

--- FOOTER ---
Small footnote text (bottom of the image, small font, verbatim):
規則115条 準則81条4項 準則82条1号 6号 7号 8号

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, paying special attention to the kanji 床, 積, 算, 入, 階, 屋, 吹, 抜, 塔, 断, 室, 外, 分, 気, which have visually
similar but structurally different Simplified or Traditional Chinese
counterparts. If any character renders as a Simplified or Traditional
Chinese variant, redraw that character in the correct Japanese form. Also
scan the entire canvas for any character that is not standard Japanese
hiragana, katakana, or Jōyō kanji — including any Chinese-only character,
Korean Hangul, other non-Japanese script, or stray decorative glyph — and
remove or redraw it so that only standard Japanese text appears anywhere in
the image. Confirm the panel count equals 5 exactly, badge numbers run 1-5 continuously, that every panel is a scene illustration, and that no flowchart, diamond or connecting arrow between boxes appears anywhere. Confirm there is no intro illustration or paragraph
block between the header and the panels, that no ✓ or ✕ mark appears
anywhere, that each 着眼点 callout states a checking order rather than only
a conclusion, confirm nothing is rendered below the footnote text (no
summary recap panel, no trophy or medal icon, and no additional text block
of any kind), and confirm the entire canvas, edge to edge, is filled with a
fully opaque background with no transparency or alpha channel anywhere.
```

### 図解プロンプト（場面ごとに1枚ずつ使う場合）

上の「場面のイメージ図1枚」は、場面を1枚に並べた図です。会話式の記事に、場面ごとの画像を1枚ずつ差し入れるときは、次のプロンプトを使います。場面の番号は、記事の「画像挿入」の指示にある「パネル」の番号と同じです。図の中の事実と文言は、上の1枚の図と同じです。キャラクターは描きません。

**場面1：天井の低い部分は、階か部屋の一部か**

```
Create a Japanese-language explanatory illustration, landscape layout,
1280x720 pixels, clean flat-design isometric illustration style with soft
pastel colors (blue, green, beige, gray), rounded card frame, consistent
with a modern explainer-graphic aesthetic. This is a single standalone scene
illustration (one scene only, no other panels), meant to be inserted
directly below one passage of the article text. It belongs to the series
苦手分析シリーズ③ 床面積算入の判定 場面1〜5.

SCENE-ILLUSTRATION REQUIREMENT (critical): Do NOT draw any flowchart, any
diamond-shaped branch node, or any arrows that connect boxes to each other.
Draw concrete everyday scenes as isometric illustrations, with only the
short captions written below, verbatim. Do not draw any recurring guide
characters, mascots or portrait characters (no bird character, no woman exam
candidate); show only the scene and the captions. Reproduce every caption
exactly as written. Do not draw ✓ or ✕ marks anywhere in this image. Do not
include case or precedent numbers. Keep the text inside the image to the
heading, the captions and the conclusion tag given below; make each caption
fully visible and not covered by any shape.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Within this English prompt text, use half-width
parentheses ( ) consistently — never open a parenthetical with a
full-width （ and close it with a half-width ), or vice versa.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the panels — with a solid or illustrated opaque background
(the pale beige/gray tone used elsewhere in this style is a good
default). There must be no checkerboard pattern, no partially transparent
area, and no unpainted canvas edge anywhere in the final image.

--- SCENE ---
Heading (bold, ONE line):
天井の低い部分は、階か部屋の一部か
Scene: two scenes side by side in the illustration. Left: a cutaway of a Western-style room in Mr. A's house with a sloped ceiling, where only the strip along one wall is low, and the whole room floor is shaded green. Caption (verbatim): 部屋のすみっこなら一室全体を算入 . Right: a cutaway of a whole attic floor above the second floor in Mr. B's house, where the ceiling is low everywhere, and the whole attic floor is shaded gray. Caption (verbatim): 階ごと低いなら階ごと不算入
Conclusion tag (a short blue banner below the illustration, 5-15 Japanese characters, a keyword phrase, not a sentence):
すみっこか、階か

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, paying special attention to the kanji 分, 体, 算, 入, 天, 井, 屋, 階, which have visually
similar but structurally different Simplified or Traditional Chinese
counterparts. If any character renders as a Simplified or Traditional
Chinese variant, redraw that character in the correct Japanese form. Also
scan the entire canvas for any character that is not standard Japanese
hiragana, katakana, or Jōyō kanji — including any Chinese-only character,
Korean Hangul, other non-Japanese script, or stray decorative glyph — and
remove or redraw it so that only standard Japanese text appears anywhere in
the image.  Confirm the image contains one scene only, that no flowchart, diamond or connecting arrow between boxes appears anywhere, that no ✓ or ✕ mark appears, that nothing is rendered below the conclusion tag, and that the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

**場面2：屋根裏部屋の天井高と階数**

```
Create a Japanese-language explanatory illustration, landscape layout,
1280x720 pixels, clean flat-design isometric illustration style with soft
pastel colors (blue, green, beige, gray), rounded card frame, consistent
with a modern explainer-graphic aesthetic. This is a single standalone scene
illustration (one scene only, no other panels), meant to be inserted
directly below one passage of the article text. It belongs to the series
苦手分析シリーズ③ 床面積算入の判定 場面1〜5.

SCENE-ILLUSTRATION REQUIREMENT (critical): Do NOT draw any flowchart, any
diamond-shaped branch node, or any arrows that connect boxes to each other.
Draw concrete everyday scenes as isometric illustrations, with only the
short captions written below, verbatim. Do not draw any recurring guide
characters, mascots or portrait characters (no bird character, no woman exam
candidate); show only the scene and the captions. Reproduce every caption
exactly as written. Do not draw ✓ or ✕ marks anywhere in this image. Do not
include case or precedent numbers. Keep the text inside the image to the
heading, the captions and the conclusion tag given below; make each caption
fully visible and not covered by any shape.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Within this English prompt text, use half-width
parentheses ( ) consistently — never open a parenthetical with a
full-width （ and close it with a half-width ), or vice versa.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the panels — with a solid or illustrated opaque background
(the pale beige/gray tone used elsewhere in this style is a good
default). There must be no checkerboard pattern, no partially transparent
area, and no unpainted canvas edge anywhere in the final image.

--- SCENE ---
Heading (bold, ONE line):
屋根裏部屋の天井高と階数
Scene: a 2-scene row, each a cross-section of a two-story house with an attic reached by a fold-down ladder. Scene 1: a ruler beside the attic reading 1.5メートル exactly, and the attic counted as a third floor with a small number tag 3階建 . Caption (verbatim): 1.5メートルちょうどは階数に算入する . Scene 2: a ruler beside the attic reading 1.4メートル, and the attic shaded gray, the house keeping a number tag 2階建 . Caption (verbatim): 1.5メートル未満は階数に算入しない
Conclusion tag (a short green banner below the illustration, 5-15 Japanese characters, a keyword phrase, not a sentence):
ちょうどは未満ではない

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, paying special attention to the kanji 建, 算, 入, 天, 井, 屋, 階, which have visually
similar but structurally different Simplified or Traditional Chinese
counterparts. If any character renders as a Simplified or Traditional
Chinese variant, redraw that character in the correct Japanese form. Also
scan the entire canvas for any character that is not standard Japanese
hiragana, katakana, or Jōyō kanji — including any Chinese-only character,
Korean Hangul, other non-Japanese script, or stray decorative glyph — and
remove or redraw it so that only standard Japanese text appears anywhere in
the image.  Confirm the image contains one scene only, that no flowchart, diamond or connecting arrow between boxes appears anywhere, that no ✓ or ✕ mark appears, that nothing is rendered below the conclusion tag, and that the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

**場面3：エレベーター室と吹抜け**

```
Create a Japanese-language explanatory illustration, landscape layout,
1280x720 pixels, clean flat-design isometric illustration style with soft
pastel colors (blue, green, beige, gray), rounded card frame, consistent
with a modern explainer-graphic aesthetic. This is a single standalone scene
illustration (one scene only, no other panels), meant to be inserted
directly below one passage of the article text. It belongs to the series
苦手分析シリーズ③ 床面積算入の判定 場面1〜5.

SCENE-ILLUSTRATION REQUIREMENT (critical): Do NOT draw any flowchart, any
diamond-shaped branch node, or any arrows that connect boxes to each other.
Draw concrete everyday scenes as isometric illustrations, with only the
short captions written below, verbatim. Do not draw any recurring guide
characters, mascots or portrait characters (no bird character, no woman exam
candidate); show only the scene and the captions. Reproduce every caption
exactly as written. Do not draw ✓ or ✕ marks anywhere in this image. Do not
include case or precedent numbers. Keep the text inside the image to the
heading, the captions and the conclusion tag given below; make each caption
fully visible and not covered by any shape.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Within this English prompt text, use half-width
parentheses ( ) consistently — never open a parenthetical with a
full-width （ and close it with a half-width ), or vice versa.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the panels — with a solid or illustrated opaque background
(the pale beige/gray tone used elsewhere in this style is a good
default). There must be no checkerboard pattern, no partially transparent
area, and no unpainted canvas edge anywhere in the final image.

--- SCENE ---
Heading (bold, ONE line):
エレベーター室と吹抜け
Scene: a 2-scene row. Scene 1: a cross-section of Company C's five-story building with an elevator shaft running from the first to the fifth floor, each floor's shaft section shaded green. Caption (verbatim): エレベーター室は各階に算入する . Scene 2: a cross-section of Mr. B's house with an entrance hall open from the first floor up through the second floor, the first floor shaded green and the open part on the second floor shaded gray. Caption (verbatim): 吹抜けは上階の吹抜けの部分だけ外す
Conclusion tag (a short orange banner below the illustration, 5-15 Japanese characters, a keyword phrase, not a sentence):
階ごとに床があるかを問う

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, paying special attention to the kanji 分, 上, 床, 算, 入, 吹, 抜, 階, which have visually
similar but structurally different Simplified or Traditional Chinese
counterparts. If any character renders as a Simplified or Traditional
Chinese variant, redraw that character in the correct Japanese form. Also
scan the entire canvas for any character that is not standard Japanese
hiragana, katakana, or Jōyō kanji — including any Chinese-only character,
Korean Hangul, other non-Japanese script, or stray decorative glyph — and
remove or redraw it so that only standard Japanese text appears anywhere in
the image.  Confirm the image contains one scene only, that no flowchart, diamond or connecting arrow between boxes appears anywhere, that no ✓ or ✕ mark appears, that nothing is rendered below the conclusion tag, and that the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

**場面4：外気分断性**

```
Create a Japanese-language explanatory illustration, landscape layout,
1280x720 pixels, clean flat-design isometric illustration style with soft
pastel colors (blue, green, beige, gray), rounded card frame, consistent
with a modern explainer-graphic aesthetic. This is a single standalone scene
illustration (one scene only, no other panels), meant to be inserted
directly below one passage of the article text. It belongs to the series
苦手分析シリーズ③ 床面積算入の判定 場面1〜5.

SCENE-ILLUSTRATION REQUIREMENT (critical): Do NOT draw any flowchart, any
diamond-shaped branch node, or any arrows that connect boxes to each other.
Draw concrete everyday scenes as isometric illustrations, with only the
short captions written below, verbatim. Do not draw any recurring guide
characters, mascots or portrait characters (no bird character, no woman exam
candidate); show only the scene and the captions. Reproduce every caption
exactly as written. Do not draw ✓ or ✕ marks anywhere in this image. Do not
include case or precedent numbers. Keep the text inside the image to the
heading, the captions and the conclusion tag given below; make each caption
fully visible and not covered by any shape.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Within this English prompt text, use half-width
parentheses ( ) consistently — never open a parenthetical with a
full-width （ and close it with a half-width ), or vice versa.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the panels — with a solid or illustrated opaque background
(the pale beige/gray tone used elsewhere in this style is a good
default). There must be no checkerboard pattern, no partially transparent
area, and no unpainted canvas edge anywhere in the final image.

--- SCENE ---
Heading (bold, ONE line):
外気分断性
Scene: a 2-scene row. Scene 1: Mr. D's house with an entrance porch that has a roof and a handrail but no walls, and a gentle wind line passing through it, shaded gray. Caption (verbatim): 屋根があっても外気分断性がなければ算入しない . Scene 2: the same porch now enclosed with walls and a window sash into an entrance hall, no wind line passing through, shaded green. Caption (verbatim): 壁で囲んで外気と分断すれば算入の方向
Conclusion tag (a short blue banner below the illustration, 5-15 Japanese characters, a keyword phrase, not a sentence):
決め手は外気分断性

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, paying special attention to the kanji 分, 算, 入, 屋, 方, which have visually
similar but structurally different Simplified or Traditional Chinese
counterparts. If any character renders as a Simplified or Traditional
Chinese variant, redraw that character in the correct Japanese form. Also
scan the entire canvas for any character that is not standard Japanese
hiragana, katakana, or Jōyō kanji — including any Chinese-only character,
Korean Hangul, other non-Japanese script, or stray decorative glyph — and
remove or redraw it so that only standard Japanese text appears anywhere in
the image.  Confirm the image contains one scene only, that no flowchart, diamond or connecting arrow between boxes appears anywhere, that no ✓ or ✕ mark appears, that nothing is rendered below the conclusion tag, and that the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

**場面5：塔屋は一部でも使えば全体**

```
Create a Japanese-language explanatory illustration, landscape layout,
1280x720 pixels, clean flat-design isometric illustration style with soft
pastel colors (blue, green, beige, gray), rounded card frame, consistent
with a modern explainer-graphic aesthetic. This is a single standalone scene
illustration (one scene only, no other panels), meant to be inserted
directly below one passage of the article text. It belongs to the series
苦手分析シリーズ③ 床面積算入の判定 場面1〜5.

SCENE-ILLUSTRATION REQUIREMENT (critical): Do NOT draw any flowchart, any
diamond-shaped branch node, or any arrows that connect boxes to each other.
Draw concrete everyday scenes as isometric illustrations, with only the
short captions written below, verbatim. Do not draw any recurring guide
characters, mascots or portrait characters (no bird character, no woman exam
candidate); show only the scene and the captions. Reproduce every caption
exactly as written. Do not draw ✓ or ✕ marks anywhere in this image. Do not
include case or precedent numbers. Keep the text inside the image to the
heading, the captions and the conclusion tag given below; make each caption
fully visible and not covered by any shape.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Within this English prompt text, use half-width
parentheses ( ) consistently — never open a parenthetical with a
full-width （ and close it with a half-width ), or vice versa.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the panels — with a solid or illustrated opaque background
(the pale beige/gray tone used elsewhere in this style is a good
default). There must be no checkerboard pattern, no partially transparent
area, and no unpainted canvas edge anywhere in the final image.

--- SCENE ---
Heading (bold, ONE line):
塔屋は一部でも使えば全体
Scene: a 2-scene row, each a building rooftop with a small tower room. Scene 1: Building F's tower room containing only an elevator machine room and a stairwell, shaded gray. Caption (verbatim): 設備だけの塔屋は算入しない . Scene 2: the same tower room where one corner is a small management office with a desk and another corner a storage room, the whole tower shaded green with a thick outline around the entire tower. Caption (verbatim): 一部でも使えば塔屋全体を算入する
Conclusion tag (a short green banner below the illustration, 5-15 Japanese characters, a keyword phrase, not a sentence):
一部使用で全体算入

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, paying special attention to the kanji 用, 体, 算, 入, 塔, 屋, which have visually
similar but structurally different Simplified or Traditional Chinese
counterparts. If any character renders as a Simplified or Traditional
Chinese variant, redraw that character in the correct Japanese form. Also
scan the entire canvas for any character that is not standard Japanese
hiragana, katakana, or Jōyō kanji — including any Chinese-only character,
Korean Hangul, other non-Japanese script, or stray decorative glyph — and
remove or redraw it so that only standard Japanese text appears anywhere in
the image.  Confirm the image contains one scene only, that no flowchart, diamond or connecting arrow between boxes appears anywhere, that no ✓ or ✕ mark appears, that nothing is rendered below the conclusion tag, and that the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

---

## 参考記事（この記事のもとになった過去問・既存記事）

- [床面積に算入する・しない、全ケース整理](../topics/yukamenseki-sannyu.md)
- [平成28年度午後の部第12問(天井高1.5メートル)](../h28-mondai/q12-tatemono-kouzou-yukamenseki.md)
- [平成29年度午後の部第16問(屋根裏部屋の階数算入)](../h29-mondai/q16-tatemono-kouzou.md)
- [平成30年度午後の部第13問(エレベーター室の床面積)](../h30-mondai/q13-yukamenseki.md)
- [令和5年度午後の部第12問(塔屋の床面積)](../r5-mondai/q12-yukamenseki.md)
