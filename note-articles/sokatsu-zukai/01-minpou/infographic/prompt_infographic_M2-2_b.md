# 【M2-2】占有の善意・悪意と占有の移転は、誰を基準に、いつから考えるのか　追加の図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch2.md`（民法編・第2章）の論点【M2-2】に差し込む、追加の図解のプロンプトです。既存の図解（`prompt_infographic_M2-2.md`＝いつから・誰を・誰がの3列の対比表）は変更せず、表の小さなイラストでは見えない「指図による占有移転で、本人・代理人・第三者の関係が前と後でどう変わるか」を、記事の「たとえば」（預けている相手に、以後は第三者のために持つよう命じ、第三者が承諾する例）に沿って4コマ分の流れで補います。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この図は、はい／いいえの分岐ではないため、青・赤は使いません。画像の中には、図の番号・問題番号・個人の演習結果を入れません。当事者はラテン文字を使わず、役割（本人・代理人・第三者）で書きます。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解1 | 指図による占有移転の流れ（命じる→承諾→占有権の取得） | 番号つきの流れ（カードポスター型）＋補足カード | 1080×2500 | 民法編2_M2-2_追加_指図による占有移転の流れ.png | 【M2-2】の「たとえば」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：指図による占有移転の流れ（命じる→承諾→占有権の取得）

- 型：番号つきの流れ（カードポスター型）＋補足カード　／　サイズ：1080×2500　／　保存名：`民法編2_M2-2_追加_指図による占有移転の流れ.png`
- 記事の挿入位置：【M2-2】の「たとえば」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a step-by-step flow poster with four numbered cards in one column and a side note card at the bottom.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
Use neutral dark navy outlines only on this poster; draw no check mark and no cross mark anywhere, and use no blue or red. All person pictograms are faceless and drawn in ONE single identical light gray-blue color, the very same shade for every one of them (they differ only by their name tags). Between the cards draw small dark navy down-pointing arrows that all mean the same thing (the next step); inside the illustrations draw only the arrows and lines described.
--- HEADER ---
Title (large, bold, 2 lines):
「指図による占有移転の流れ」
「承諾するのは、新たな占有者」
Subtitle (smaller, centered, 1 line):
「民法 第181条・第184条」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「はじめ：代理人が本人のために占有」
Illustration: Every card shows the same three faceless pictograms in the same positions: 「本人」 at the left, 「代理人」 in the middle holding a small box icon, and 「第三者」 at the right. A plain dark navy line joins 本人 and 代理人 and carries the label 「代理占有」. The 第三者 pictogram is drawn with a thin dotted outline, not yet involved.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「物は代理人の手元にある」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「本人が代理人に命じる」
Illustration: Every card shows the same three faceless pictograms in the same positions: 「本人」 at the left, 「代理人」 in the middle holding a small box icon, and 「第三者」 at the right. One dark navy arrow runs from 本人 to 代理人 and carries the speech tag 「以後は第三者のために占有せよ」. The 第三者 pictogram is still drawn with a thin dotted outline.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「命じるのは本人」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「第三者が承諾する」
Illustration: Every card shows the same three faceless pictograms in the same positions: 「本人」 at the left, 「代理人」 in the middle holding a small box icon, and 「第三者」 at the right. The 第三者 pictogram is now drawn with a solid outline and a small speech tag 「承諾」 beside it. The dark navy arrow from the previous card is drawn faintly in light gray.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「承諾するのは第三者」
--- CARD 4 ---
Badge: a filled dark navy circle containing the number 4 (numbers run 1 to 4 in order).
Heading (bold, ONE line):
「第三者が占有権を取得する」
Illustration: Every card shows the same three faceless pictograms in the same positions: 「本人」 at the left, 「代理人」 in the middle holding a small box icon, and 「第三者」 at the right. The plain dark navy line labeled 「代理占有」 now joins 代理人 and 第三者; the 本人 pictogram is drawn with a thin dotted outline. The box icon is still in the hands of 代理人. A small tag 「占有権を取得」 beside 第三者.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「占有権は第三者に移る」
In CARD 3 only, the conclusion tag 「承諾するのは第三者」 has a pale yellow highlighter marker over the words 「第三者」.
--- SIDE NOTE CARD (below the cards, a wide card with a dashed dark navy outline) ---
Heading 「取り違えやすい点」, body 「承諾するのは代理人ではなく、第三者」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 占, 承, 権, 物, 諾, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm that every card shows the same three pictograms 本人, 代理人 and 第三者 in the same left-to-right positions, that the 代理占有 line joins 本人 and 代理人 in cards 1 and 2 and joins 代理人 and 第三者 in card 4, that the box icon stays with 代理人 in every card, that the side note card is the last element, and confirm that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 検品チェック（生成後）

- カードがちょうど4枚で、1〜4の順に並び、カードの間の矢印がすべて下向きの濃紺か。4枚とも、本人・代理人・第三者の3人が同じ左→右の位置にいるか。
- 「代理占有」の線が、カード1・2では本人と代理人、カード4では代理人と第三者を結んでいるか。箱の絵はどのカードでも代理人の手元にあるか。
- カード3の結論タグだけ「第三者」に黄色いマーカーが付いているか。いちばん下の補足カード（破線の枠）のあとに何も描かれていないか。
- 見出し・タグの文字を、上のコードブロックの文言と一字ずつ突き合わせた（「指図」「占有」「承諾」「代理」「取得」が簡体字・別字になっていない）。
- 青・赤・○×の印がどこにもない。図の番号・問題番号・個人の演習結果がない。背景は完全に不透明。

## 記事・条文との照合（作成者用）

- 民法184条（指図による占有移転：代理人によって占有をする場合において、本人がその代理人に対して以後第三者のためにその物を占有することを命じ、その第三者がこれを承諾したときは、その第三者は占有権を取得する）、181条（占有権は代理人によって取得できる）を `note-articles/laws/minpou-1-soukyoku-bukken.md` の原文で確認。
- カード1の「物は代理人の手元にある」・カード4の箱の絵が代理人の手元に残る点は、184条の文言（代理人が占有している物について、以後は第三者のために占有することを命じる）から導いた整理で、記事の本文に直接の記述はない。条文の構造に合わせた図であり、実務上の物の動きを述べるものではない。
- 「命じるのは本人、承諾するのは第三者」は、記事の「判断のしかた」3と肢の判定（承諾するのは第三者）による。
