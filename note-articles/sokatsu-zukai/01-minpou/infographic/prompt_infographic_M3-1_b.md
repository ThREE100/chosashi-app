# 【M3-1】単純悪意者や背信的悪意者の転得者に、登記なしで勝てるか　追加の図解インフォグラフィック プロンプト（1枚）

総合記事『直前期の苦手論点つぶし総合記事①民法編』の第3章（`note-articles/column/sokatsu-01-minpou-ch3.md`）の【M3-1】の「たとえば」の直後（登場人物と登記の動きの図）に差し込む、追加の図解のプロンプトです。作成済みの図解（`infographic/prompt_infographic_M3-?.md`）は変えず、記事の要点のうち図がなかった部分を補います。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、はい／いいえの配色、アウトロブロック禁止）に従いました。画像の中には、図の番号・問題番号・年度・判例番号・個人の演習結果を入れません。当事者はラテン文字ではなく役割名で書いています。キャラクターは描かないので、参照画像は不要です。

既存の図解（判定の流れ図）との違い：既存の図解は、上から順に答えにたどり着く流れ図です。この図解は、同じ二重売買の登場人物（元の所有者・先の買主・あとの買主・転得者）を3つの場面で並べ、誰が登記をしていて誰が勝つのかを見せる関係図です。

- 図解1：二重に買われたら、誰が勝つ？（登場人物と登記の関係図）（型：関係図ポスター型（3場面）／サイズ：1080×2400）
  - 保存名：`民法編3_1_追加_二重に買われたら誰が勝つ.png`
  - 記事の挿入位置：【M3-1】の「たとえば」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：二重に買われたら、誰が勝つ？（登場人物と登記の関係図）

- 型：関係図ポスター型（3場面）　／　サイズ：1080×2400　／　保存名：`民法編3_1_追加_二重に買われたら誰が勝つ.png`
- 記事の挿入位置：【M3-1】の「たとえば」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2400 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a poster of three stacked scene panels, each a small relationship diagram of people (関係図); it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the first element. Every element communicates its point through the illustration plus short labels. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text beyond the short strings listed below.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「二重に買われたら、誰が勝つ？」
「あとの買主の中身で決まる」
Subtitle (smaller, centered, 1 line):
「民法　第177条」
--- PANEL 1 ---
Panel heading bar (dark navy with white bold text, ONE line):
「あとの買主が、知っていただけの悪意者」
Diagram: On the left, one pictogram tagged 「元の所有者」. Two dark navy arrows leave it to the right, both labeled 「売る」 (both arrows mean the same thing). The upper arrow ends at a pictogram tagged 「先の買主」 with a small light-gray tag 「未登記」 beside it. The lower arrow ends at a pictogram tagged 「あとの買主」 with a small rubber-stamp icon labeled 「登記」 beside it and a small light-gray tag 「知っていただけ」 under it. Three pictograms in total in this panel.
Result banner directly below the diagram: a RED box with the text 「先の買主は、登記がないと負ける」.
--- PANEL 2 ---
Panel heading bar (dark navy with white bold text, ONE line):
「あとの買主が、害する目的の背信的悪意者」
Diagram: On the left, one pictogram tagged 「元の所有者」. Two dark navy arrows leave it to the right, both labeled 「売る」 (both arrows mean the same thing). The upper arrow ends at a pictogram tagged 「先の買主」 with a small light-gray tag 「未登記」 beside it. The lower arrow ends at a pictogram tagged 「あとの買主」 with a small rubber-stamp icon labeled 「登記」 beside it and a small light-gray tag 「もっぱら害する目的」 under it. Three pictograms in total in this panel.
Result banner directly below the diagram: a BLUE box with the text 「先の買主は、登記なしで勝てる」.
--- PANEL 3 ---
Panel heading bar (dark navy with white bold text, ONE line):
「背信的悪意者から買った転得者が出てきた」
Diagram: On the left, one pictogram tagged 「元の所有者」. Two dark navy arrows leave it to the right, both labeled 「売る」 (both arrows mean the same thing). The upper arrow ends at a pictogram tagged 「先の買主」 with a small light-gray tag 「未登記」 beside it. The lower arrow ends at a pictogram tagged 「あとの買主」 with a small rubber-stamp icon labeled 「登記」 beside it and a small light-gray tag 「背信的悪意者」 under it. From the pictogram 「あとの買主」, a third dark navy arrow labeled 「転売」 leads further to the right to a fourth pictogram tagged 「転得者」 with a small rubber-stamp icon labeled 「登記」 beside it and a small light-gray tag 「自身は背信的でない」 under it. Four pictograms in total in this panel.
Result banner directly below the diagram: a RED box with the text 「先の買主は、転得者には負ける」.
Under the red box, one small light-gray tag: 「転得者自身が背信的悪意者なら、勝てる」.
Counts: 3 panels, with 3, 3 and 4 pictograms; the pictogram 「先の買主」 never has a rubber-stamp icon; the rubber-stamp icon appears once in panel 1, once in panel 2 and twice in panel 3. The three result banners have different texts; do not copy one into another.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 売, 所, 登, 記, 買; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm there are exactly 3 panels, that panel 1 and panel 2 have 3 pictograms and panel 3 has 4 pictograms, that the pictogram 先の買主 never carries a 登記 stamp, that the banner of panel 1 is red, the banner of panel 2 is blue and the banner of panel 3 is red, that the arrows are dark navy and carry no はい or いいえ, that no text overflows its box, and that all person names are role names with no Latin letters. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

### 検品チェック（生成後）

- [ ] 場面パネルがちょうど3つで、人型が3体・3体・4体。『先の買主』には登記の印がない（登記の印は、場面1に1つ、場面2に1つ、場面3に2つ）
- [ ] 結果の箱は、場面1が赤『先の買主は、登記がないと負ける』、場面2が青『先の買主は、登記なしで勝てる』、場面3が赤『先の買主は、転得者には負ける』（3つの文言が別々）
- [ ] 矢印は濃紺で『売る』『転売』だけ。『はい』『いいえ』が矢印にない。人型は全員同じ色で、役割名の名札（英字なし）
- [ ] 簡体字・繁体字・英字・余計な文字がない。背景が不透明。文字が箱からはみ出していない

### 記事・条文との照合

- 場面1・2：民法177条。単純悪意者も第三者に含まれ、害する目的の背信的悪意者本人は第三者から外れる（記事【M3-1】の結論・中身の整理）。背信的悪意かどうかを人ごとに判断する扱い（相対的構成）は判例の考え方で、条文に直接の定めはない
- 場面3：記事の『たとえば』（嫌がらせ目的で買って登記した者から、事情を知らない者が転得し登記）と『判断のしかた』3（転得者自身が背信的かを見る）。小さな札『転得者自身が背信的悪意者なら、勝てる』は、判断のしかた3と既存の判定の流れ図（ひし形1）の裏返し
- 『登記』の印が先の買主にないこと：先の買主が『登記をしていない人』という記事の前提（結論の冒頭）
