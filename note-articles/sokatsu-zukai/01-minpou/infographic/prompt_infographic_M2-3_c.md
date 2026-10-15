# 【M2-3】占有回収の訴えを起こせるのは誰か　追加の図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch2.md`（民法編・第2章）の論点【M2-3】に差し込む、追加の図解のプロンプトです。既存の図解（`prompt_infographic_M2-3.md`＝5枚のカード）は変更せず、そのカード5（代表者）は「個人としても提起できる」の結論だけで、機関としての占有と個人としての占有が別々に数えられ、特段の事情があるときに併存することが見えないため、記事の中身の整理（法人の代表者が建物を法人の機関として占有しつつ、特段の事情により個人のためにも占有している場合）に沿って、2つの占有を1枚の関係図で補います。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この図は、はい／いいえの分岐ではないため、青・赤は使いません。画像の中には、図の番号・問題番号・個人の演習結果を入れません。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解1 | 法人の代表者の二つの占有（機関としての占有と個人としての占有） | 関係図型（2枚のカード＋帯） | 1080×2100 | 民法編2_M2-3_追加_法人の代表者の二つの占有.png | 【M2-3】の「判断のしかた」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：法人の代表者の二つの占有（機関としての占有と個人としての占有）

- 型：関係図型（2枚のカード＋帯）　／　サイズ：1080×2100　／　保存名：`民法編2_M2-3_追加_法人の代表者の二つの占有.png`
- 記事の挿入位置：【M2-3】の「判断のしかた」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a relationship-diagram poster with two big cards in one column and a bottom band; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Each card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
Use neutral dark navy outlines only on this poster; draw no check mark and no cross mark anywhere, and use no blue or red. All person pictograms are faceless and drawn in ONE single identical light gray-blue color, the very same shade for every one of them (they differ only by their name tags). The only lines and arrows are the ones described below.
--- HEADER ---
Title (large, bold, 2 lines):
「法人の代表者が建物を奪われたとき」
「機関の占有と個人の占有は別に数える」
Subtitle (smaller, centered, 1 line):
「民法 第200条（判例）」
--- CARD 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 2 in order).
Heading (bold, ONE line):
「代表者の占有は二つありうる」
Illustration (a wide relationship diagram inside the card): a flat office building icon at the right. At the left, one faceless pictogram tagged 「代表者」, and above it a small company icon tagged 「法人」. Two dark navy lines run from the 代表者 pictogram to the building. The upper line carries the label 「機関としての占有」 with the small light-gray label 「法人のため」. The lower line carries the label 「個人としての占有」 with the small light-gray label 「特段の事情があるとき」. The two lines are drawn clearly separate and never merge.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「両方の占有が併存する」
--- CARD 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 2 in order).
Heading (bold, ONE line):
「占有を奪われたとき」
Illustration: one faceless pictogram tagged 「代表者」 holding a small document sheet labeled 「占有回収の訴え」, with a thin plain dark navy line from the sheet to a small badge labeled 「個人としての占有」, and a small light-gray label 「判例の立場」 beside the sheet.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「個人としても提起できる」
Under the two cards, one wide dark navy band with large white text 「機関として持っていても、個人の占有は別にある」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 占, 建, 物; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of cards equals 2 exactly, numbered 1 and 2, that card 1 shows exactly two separate lines from the 代表者 pictogram to the building, one labeled 機関としての占有 and one labeled 個人としての占有, that card 2 shows the 代表者 pictogram holding a document sheet labeled 占有回収の訴え, that the dark navy band is the last element, and confirm that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 検品チェック（生成後）

- カードがちょうど2枚（番号1・2）で、いちばん下に濃紺の帯が1本あり、そのあとに何も描かれていないか。
- カード1：代表者から建物へ向かう線がちょうど2本で、上が「機関としての占有（法人のため）」、下が「個人としての占有（特段の事情があるとき）」か。2本が1本に合流していないか。
- 見出し・タグの文字を、上のコードブロックの文言と一字ずつ突き合わせた（「機関」「占有」「併存」「奪」「代表者」「法人」が簡体字・別字になっていない）。
- 青・赤・○×の印がどこにもない。図の番号・問題番号・個人の演習結果がない。背景は完全に不透明。

## 記事・条文との照合（作成者用）

- 民法200条1項（占有者がその占有を奪われたときは占有回収の訴えにより物の返還及び損害の賠償を請求できる）を `note-articles/laws/minpou-1-soukyoku-bukken.md` の原文で確認。
- 「機関としての占有と個人としての占有が併存し得る」「特段の事情により個人のためにも占有している場合」「個人として占有回収の訴えを提起できる」は、記事の中身の整理・結論による判例の整理で、条文に直接の記述はない。そのため図に小さく「判例の立場」と添え、断定を条文の効果のようには見せていない。
- 記事は「機関としての占有とは別に個人としての占有があれば」と書き、機関としてのみ占有している場合の結論までは述べていない。図もその場合の結論（個人の占有はない等）は描かず、併存するときだけを描いた。
