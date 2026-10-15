# 【M2-3】占有回収の訴えを起こせるのは誰か　追加の図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch2.md`（民法編・第2章）の論点【M2-3】に差し込む、追加の図解のプロンプトです。既存の図解（`prompt_infographic_M2-3.md`＝5枚のカード）は変更せず、そこでは小さな絵にとどまる「転貸人（間接占有者）・転借人（直接占有者）・奪った人」の三者の位置関係を、記事の「たとえば」（賃借人が又貸ししていて、転借人が追い出された例）に沿って1枚の関係図で補います。「実際に追い出されたのは転借人だけなのに、なぜ転貸人も訴えられるのか」という主体の取り違えを、図で防ぐ狙いです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この図は、はい／いいえの分岐ではないため、青・赤は使いません。画像の中には、図の番号・問題番号・個人の演習結果を入れません。当事者はラテン文字を使わず、役割（転貸人・転借人・奪った人）で書きます。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解1 | 又貸しの部屋を奪われたとき（転借人も転貸人も占有回収の訴えができる） | 関係図型（2枚のカード＋帯） | 1080×2400 | 民法編2_M2-3_追加_又貸しの部屋を奪われたとき.png | 【M2-3】の「たとえば」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：又貸しの部屋を奪われたとき（転借人も転貸人も占有回収の訴えができる）

- 型：関係図型（2枚のカード＋帯）　／　サイズ：1080×2400　／　保存名：`民法編2_M2-3_追加_又貸しの部屋を奪われたとき.png`
- 記事の挿入位置：【M2-3】の「たとえば」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a relationship-diagram poster with two big cards in one column and a bottom band; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Each card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
Use neutral dark navy outlines only on this poster; draw no check mark and no cross mark anywhere, and use no blue or red. All person pictograms are faceless and drawn in ONE single identical light gray-blue color, the very same shade for every one of them (they differ only by their name tags). The only lines and arrows are the ones described below.
--- HEADER ---
Title (large, bold, 2 lines):
「又貸しの部屋を奪われたとき」
「転借人も転貸人も提起できる」
Subtitle (smaller, centered, 1 line):
「民法 第181条・第197条・第200条」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 2 in order).
Heading (bold, ONE line):
「部屋を奪われた場面」
Illustration (a wide relationship diagram inside the card): a flat house icon at the center-right with a closed door. At the left, two faceless pictograms stacked in a column: the upper one tagged 「転貸人」 with the small light-gray label 「間接占有者」, the lower one tagged 「転借人」 with the small light-gray label 「直接占有者」, standing at the door of the house. A plain dark navy vertical line joins the two, carrying the label 「代理占有（民法181条）」. At the right of the house, a third faceless pictogram tagged 「奪った人」 holding a small key icon, with one dark navy arrow pointing to the door of the house carrying the label 「占有を奪う」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「追い出されたのは転借人」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 2 in order).
Heading (bold, ONE line):
「占有回収の訴えができる人」
Illustration: two faceless pictograms side by side, tagged 「転借人」 and 「転貸人」, each holding a small document sheet labeled 「占有回収の訴え」, and above them one small light-gray label 「他人のために占有する者も、同様（民法197条）」.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「どちらも提起できる」
Under the two cards, one wide dark navy band with large white text 「見るのは、追い出された人だけではない」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 占, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 2 exactly, numbered 1 and 2, that card 1 shows the stacked pictograms 転貸人 above 転借人 joined by a plain line labeled 代理占有, the house icon, and the pictogram 奪った人 with an arrow to the door, that card 2 shows both 転借人 and 転貸人 each holding a document sheet labeled 占有回収の訴え, that the dark navy band is the last element, and confirm that no check mark, cross mark, blue, or red appears anywhere and that the three pictogram tags 転貸人, 転借人 and 奪った人 are all different. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 検品チェック（生成後）

- カードがちょうど2枚（番号1・2）で、いちばん下に濃紺の帯が1本あり、そのあとに何も描かれていないか。
- カード1：転貸人が上、転借人が下に縦に並び、2人を結ぶ線に「代理占有（民法181条）」とあるか。奪った人が家の戸口へ矢印で向かっているか。人物のタグ（転貸人・転借人・奪った人）がすべて違うか。
- カード2：転借人と転貸人の2人がそれぞれ「占有回収の訴え」の書類を持っているか。
- 見出し・タグの文字を、上のコードブロックの文言と一字ずつ突き合わせた（「又貸」「転貸」「転借」「占有」「奪」「回収」が簡体字・別字になっていない）。
- 青・赤・○×の印がどこにもない。図の番号・問題番号・個人の演習結果がない。背景は完全に不透明。

## 記事・条文との照合（作成者用）

- 民法181条（占有権は代理人によって取得できる）、197条（占有者は占有の訴えを提起できる。他人のために占有をする者も、同様とする）、200条1項（占有者がその占有を奪われたときは占有回収の訴えにより物の返還及び損害の賠償を請求できる）を `note-articles/laws/minpou-1-soukyoku-bukken.md` の原文で確認。
- 「転貸人は転借人を占有代理人として代理占有しており、転借人が占有を奪われたとき転貸人も占有回収の訴えを提起できる」は、記事の中身の整理・肢の判定による判例の整理で、条文に直接の記述はない。図は記事の結論の範囲にとどめ、物の返還の相手方などは描いていない。
- 「間接占有者」「直接占有者」は、記事の本文にある語（間接占有者）と、それに対応する通常の語である。
