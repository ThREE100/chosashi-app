# 【M3-3】順次譲渡（A→B→C）で、相続人・債権者・他人物売買をどう扱うか　図解インフォグラフィック プロンプト（1枚）

民法編の総合記事（`note-articles/column/sokatsu-01-minpou.md`）の【M3-3】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。配色は、肯定＝青、否定＝赤、中立＝濃紺で統一していますが、この図解は対比表なので、○×・青・赤は使いません。画像の中には、図の番号を入れません。4コマ（`4koma/prompt_4koma_M3-3_D0722-D0723-D1209.md`）が3つの肢を並べ直す形なのに対し、この図解は、場面ごとに『問われること・引かれやすい言葉・見る点・答え』を1枚で見比べる早見表です。

- 図解1：売主の周りに出てくる三つの場面（相続人・債権者・他人物売買）
  - 型：対比表型（3列・4行）
  - サイズ：1080×2000
  - 保存名：図解1_売主の周りに出てくる三つの場面.png
  - 記事の挿入位置：【M3-3】の『中身の整理』の直後

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：売主の周りに出てくる三つの場面（相続人・債権者・他人物売買）

- 型：対比表型（3列・4行）　／　サイズ：1080×2000　／　保存名：`図解1_売主の周りに出てくる三つの場面.png`
- 記事の挿入位置：【M3-3】の『中身の整理』の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2000 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a comparison table poster with three scene columns (対比表型).
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「売主の周りに出てくる三つの場面」
「場面ごとに、見る点が違う」
Subtitle (smaller, centered, 1 line):
「民法 第177条・第423条・第561条」
--- STRIP (directly below the header, one row, no paragraph) ---
A short horizontal strip with three faceless flat person pictograms in exactly the same single light gray-blue color, from left to right, each with a dark navy name tag: 「元の所有者」, 「売主」, 「買主」. Between the pictograms are two plain thin dark navy arrows, each with a small label 「譲渡」 (both arrows mean the same thing). Under the strip, one small light-gray tag: 「登記は、元の所有者の名義のまま」.
--- TABLE ---
Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns (one row-label column and three scene columns) and exactly 4 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.
Header row (dark navy cells with white text), from left to right, with a small light-gray tag under each of the three scene headers: the first cell is empty; the second header 「売主の相続人が出てきた」 with the tag 「民法177条」; the third header 「売主の債権者が出てきた」 with the tag 「民法423条」; the fourth header 「他人物売買だった」 with the tag 「民法561条」.
The three scene headers are NOT identical; copy each one exactly as given.
Data row 1 (row label cell, dark navy, white text: 「問われること」): second column 「買主は、相続人に登記なしで主張できるか」; third column 「合意をしても、債権者は代位できるか」; fourth column 「買主に所有権が移るのは、いつか」.
Data row 2 (row label cell, dark navy, white text: 「引かれやすい言葉」): second column 「登記名義人が元の所有者のまま」; third column 「直接登記名義を移転する旨の合意」; fourth column 「売主への所有権の移転の登記がされた時点」.
Data row 3 (row label cell, dark navy, white text: 「見る点」): second column 「相続人は、売主の権利義務を包括的に承継する」; third column 「合意は、登記を移す経路の取決めにとどまる」; fourth column 「他人の物の売買も、債権契約としては有効」.
Data row 4 (row label cell, dark navy, white text: 「答え」; every cell of this row has a pale yellow highlighter marker behind its text): second column 「登記なしで主張できる」; third column 「売主の登記請求権は消えず、債権者は代位できる」; fourth column 「売主が所有権を取得した時に移る」.
At the bottom, one small light-gray tag centered across the table: 「中間省略登記の扱いは、判例の整理による」
Every cell has its own text exactly as given; no two cells share the same text.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 代, 債, 効, 売, 対, 張, 所, 承, 権, 渡, 物, 登, 記, 請, 譲, 買, 違, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the table has exactly 4 columns and exactly 4 data rows, that the three scene headers read 売主の相続人が出てきた, 売主の債権者が出てきた and 他人物売買だった in this order, that every cell reads exactly as given, that the strip above the table has three pictograms and two arrows labeled 譲渡, and that no check mark, cross mark, blue or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 検品チェック（生成後）

- [ ] 表が4列（行の見出し＋3つの場面）・4行で、場面の見出しが左から『売主の相続人が出てきた』『売主の債権者が出てきた』『他人物売買だった』の順になっている
- [ ] 各セルの文字がプロンプトと一字一句同じ（『登記なしで主張できる』『売主の登記請求権は消えず、債権者は代位できる』『売主が所有権を取得した時に移る』など）
- [ ] 上の帯に人型が3つ（元の所有者・売主・買主）と矢印2本（どちらも『譲渡』）がある。人型は全部同じ色
- [ ] 『答え』の行の文字だけに黄色のマーカーがある。○×・青・赤が一つもない
- [ ] 簡体字・繁体字・英字・ハングルの混入がない。背景が不透明（透過・チェッカーボードなし）
- [ ] 表の下に、まとめのパネル・トロフィー・追加の文章がない

## 記事・条文との照合（設計メモ）

- 相続人は包括承継人で、177条の『第三者』ではない（記事【M3-3】中身の整理、H24-Q03イ）
- 中間省略登記の合意があってもBの登記請求権は消えず、債権者は民法423条1項で代位できる（記事が『個別の判例の番号までは確認できていない』と注記しているため、図の下に『判例の整理による』の小さな札を付けた）
- 他人物売買は契約として有効で、売主が取得した時点で買主に移る（民法561条：売主は、その権利を取得して買主に移転する義務を負う。法令DB `note-articles/laws/minpou-2-saiken.md` で確認）
- 『引かれやすい言葉』は、元の肢の問題文からの引用（H24-Q03イ・ウ、H29-Q02ア）
