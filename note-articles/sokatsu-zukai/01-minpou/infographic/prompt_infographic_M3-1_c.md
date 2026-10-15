# 【M3-1】単純悪意者や背信的悪意者の転得者に、登記なしで勝てるか　追加の図解インフォグラフィック プロンプト（1枚）

総合記事『直前期の苦手論点つぶし総合記事①民法編』の第3章（`note-articles/column/sokatsu-01-minpou-ch3.md`）の【M3-1】の「中身の整理」の直後（第三者に当たる者と当たらない者の早見表）に差し込む、追加の図解のプロンプトです。作成済みの図解（`infographic/prompt_infographic_M3-?.md`）は変えず、記事の要点のうち図がなかった部分を補います。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、はい／いいえの配色、アウトロブロック禁止）に従いました。画像の中には、図の番号・問題番号・年度・判例番号・個人の演習結果を入れません。当事者はラテン文字ではなく役割名で書いています。キャラクターは描かないので、参照画像は不要です。

既存の図解（判定の流れ図）との違い：既存の図解は、あとで買った人が背信的悪意者かどうかの流れを見せます。この図解は、記事の『中身の整理』にある、177条の『第三者』に当たる者と当たらない者を、1枚の早見表で並べ直したものです。

- 図解1：第三者に当たるのは、誰？（当たる者・当たらない者の早見表）（型：早見表型（3列・8行）／サイズ：1080×2100）
  - 保存名：`民法編3_1_追加_第三者に当たる者の早見表.png`
  - 記事の挿入位置：【M3-1】の「中身の整理」の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：第三者に当たるのは、誰？（当たる者・当たらない者の早見表）

- 型：早見表型（3列・8行）　／　サイズ：1080×2100　／　保存名：`民法編3_1_追加_第三者に当たる者の早見表.png`
- 記事の挿入位置：【M3-1】の「中身の整理」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a reference table poster with three columns (早見表).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter.
--- HEADER ---
Title (large, bold, 2 lines):
「第三者に当たるのは、誰？」
「知っているだけでは外れない」
Subtitle (smaller, centered, 1 line):
「民法　第177条」
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 8 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text): 「だれか」, 「第三者か」, 「見るポイント」.
Data rows, one per line, in this order (column 1 | column 2 | column 3):
Row 1: 「二重に買った人」 | 「当たる」 | 「登記の先後で決まる」
Row 2: 「知っていただけの悪意者」 | 「当たる」 | 「知っていることと、信義則に反することは別」
Row 3: 「背信的悪意者から買った転得者」 | 「当たる」 | 「転得者自身が背信的悪意者でない限り」
Row 4: 「当事者」 | 「当たらない」 | 「売った人と、買った人の間」
Row 5: 「包括承継人（相続人など）」 | 「当たらない」 | 「当事者の地位を、そのまま承継する」
Row 6: 「前主・後主の関係にある者」 | 「当たらない」 | 「権利を渡した側と、受けた側」
Row 7: 「不法占拠者」 | 「当たらない」 | 「登記がないことを主張する正当な利益がない」
Row 8: 「背信的悪意者本人」 | 「当たらない」 | 「自由競争の範囲を逸脱し、もっぱら害する目的」
Highlighting: the strings 「知っていただけの悪意者」 in row 2 and 「背信的悪意者から買った転得者」 in row 3 have a pale yellow highlighter marker; all other cells are plain. Copy each cell exactly as given. The strings 「当たる」 and 「当たらない」 repeat on purpose in the second column (3 rows and 5 rows), and the strings 「当たる」 and 「当たらない」 are NOT identical, so copy each exactly.
Under the table, one wide dark navy band with large white text 「知っているだけでは、第三者から外れない」.
Under the band, one small light-gray tag: 「第三者の範囲は、判例による整理」.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 占, 地, 売, 張, 当, 承, 権, 渡, 登, 記, 買, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 3 columns and exactly 8 data rows, that rows 1 to 3 read 当たる and rows 4 to 8 read 当たらない in the second column, that every cell reads exactly as given, that only the two cells in rows 2 and 3 of the first column are highlighted, and that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

### 検品チェック（生成後）

- [ ] 表が3列・8行で、第2列が上から『当たる』3つ→『当たらない』5つ。各セルの文字がプロンプトと一字一句同じ
- [ ] 黄色のマーカーは、1列目の2行目『知っていただけの悪意者』と3行目『背信的悪意者から買った転得者』だけ
- [ ] 表の下に濃紺の帯『知っているだけでは、第三者から外れない』と灰色の小さな札。それ以外のまとめ・追加の文章がない
- [ ] 簡体字・繁体字・英字・余計な文字がない。背景が不透明。✓・✕・青・赤がどこにもない

### 記事・条文との照合

- 第三者に当たる者（二重譲受人・単純悪意者・背信的悪意者から買った転得者）と、外れる者（当事者・包括承継人・前主後主の関係にある者・不法占拠者・背信的悪意者）：記事【M3-1】の『中身の整理』の列挙のとおり
- 『見るポイント』の列：行1〜3と行8は記事の本文（『知っていることと、信義則に反することは別です』『背信的悪意者本人でない限り保護』『自由競争の範囲を逸脱し、もっぱら相手を害する目的』）の範囲。行4〜6は定義的な言い換え、行7『登記がないことを主張する正当な利益がない』は、第三者を『登記の欠缺を主張する正当な利益を有する者』とする判例の一般的な説明で、記事に明記はない（図の下の札『第三者の範囲は、判例による整理』で添えた）
- 民法177条の原文：`note-articles/laws/minpou-1-soukyoku-bukken.md` で確認済み（登記をしなければ、第三者に対抗することができない）。『第三者』の範囲は条文に定義がなく、判例による
