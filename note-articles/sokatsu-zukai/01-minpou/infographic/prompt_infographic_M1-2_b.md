# 【M1-2】制限行為能力者：追加の図解「追認できるのは、いつか」　図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-2】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-2.md`）のカード3が原則と「同意を得た追認」の2行だけなので、法定代理人・保佐人・補助人が自ら追認する場合と成年被後見人の除外を、判定の流れ図で補います。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、はい＝青、いいえ＝赤、中立＝濃紺で統一しています。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。

- 図解1：追認できるのは、いつか（だれが追認するかで分かれる判定フロー）
  - 型：フローチャート型　／　サイズ：1080×2300　／　保存名：`民法編1_M1-2_追加_追認はいつできるか.png`
  - 記事の挿入位置：【M1-2】の「判断のしかた」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：追認できるのは、いつか（だれが追認するかで分かれる判定フロー）

```text
Create a Japanese-language infographic, portrait layout, 1080x2300 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a flowchart poster (判定の流れ).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「追認できるのは、いつ？」
「だれが追認するかで分かれる」
Subtitle (smaller, centered, 1 line):
「民法 第124条」
--- FLOWCHART ---
Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, SMALL NOTE, DIAMOND 1, DIAMOND 2, RESULT 3. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row and RESULT 2 sits to the RIGHT of DIAMOND 2 on the same row, with at least 60 px of empty space between each diamond and its box so that the arrow label stays visible. The wide note card sits at the very bottom. All arrows are straight or have at most one right-angle bend and never cross each other. Do not draw any arrow that returns to an earlier node.
NODE START (rounded pill, dark navy): 「取り消すことができる行為を追認する」
NODE SMALL NOTE (a small gray card directly below START, with no arrow of its own): 「状況とは、取消しの原因となっていた状況のこと」.
NODE DIAMOND 1: 「追認するのは、法定代理人・保佐人・補助人か？」 The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.
  - Arrow right to RESULT 1 with the BLUE label 「はい」.
  - Arrow down to DIAMOND 2 with the RED label 「いいえ」.
NODE DIAMOND 2: 「同意を得て追認する、成年被後見人以外の制限行為能力者か？」 The text is placed inside the diamond on 4 lines; enlarge the diamond so that all text stays inside it.
  - Arrow right to RESULT 2 with the BLUE label 「はい」.
  - Arrow down to RESULT 3 with the RED label 「いいえ」.
NODE RESULT 1 (blue box): 「状況の消滅後でなくてよい」 on the first line and 「法定代理人らが自ら追認する場合」 on the next line, with the small gray tag 「124条2項1号」 under the text.
NODE RESULT 2 (blue box): 「状況の消滅後でなくてよい」 on the first line and 「同意を得た追認は、成年前でもできる」 on the next two lines, with the small gray tag 「124条2項2号」 under the text.
NODE RESULT 3 (red box): 「原則どおり」 on the first line and 「状況が消え、取消権を知った後でなければ追認できない」 on the next three lines, with the small gray tag 「124条1項」 under the text.
Counts: 1 start node, 1 small note, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The first lines of RESULT 1 and RESULT 2 are the same string on purpose; the second lines of the three result boxes are NOT identical, so copy each exactly as given.
--- NOTE CARD AT THE BOTTOM (one wide separate card below RESULT 3, pale gray fill, dark navy outline, neutral dark navy text, with NO arrow) ---
Heading (bold, ONE line): 「成年被後見人は、同意を得ても例外にならない」.
Body (ONE line): 「どの場合も、取消権を有することを知った後であることは必要」, with the small gray tag 「124条」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 保, 号, 権, 認; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 1 start node, 1 small note, 2 diamonds and 3 result boxes, that each diamond shows a blue 「はい」 on the arrow to the right and a red 「いいえ」 on the arrow going down, that RESULT 1 and RESULT 2 are blue and RESULT 3 is red, that no text overflows its box, that no arrow label is hidden, and that the note card at the bottom is one separate card with no arrow. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

保存名：`民法編1_M1-2_追加_追認はいつできるか.png`

## 検品チェック

- 開始の楕円が1つ、その下に灰色の小さな注記が1つ、ひし形が2つ、結果の箱が3つ（青2・赤1）か。ひし形ごとに青の「はい」（右向き）と赤の「いいえ」（下向き）が付いているか。
- 結果1と結果2の1行目が同じ文字列（状況の消滅後でなくてよい）で、2行目が別の文言か。条番号（124条2項1号・124条2項2号・124条1項・124条）が指定どおりか。
- 結果の箱のあとに矢印が出ていないか。下の注記のカードが1枚だけで、矢印でつながれていないか。
- 簡体字・余計な文字・透過・図番がないか。