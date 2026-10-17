# 区分建物の範囲（8／10）区分・接続・合体・合併・分割　画像プロンプト

記事 `08-setsuzoku-gattai.md` の画像プロンプトです。図解の画像は、記事に出てくる順に、図解1から番号を振っています（画像の中に番号は入りません）。画像は生成していません。ChatGPT（画像生成）に、各コードブロックをそのまま貼ります。

どの図解も、1枚の中で「出題文の状態」→「正しいイメージ」（青）と「誤ったイメージ」（赤）の順に並べます。「出題文の内容」の札は、問われている記述が描かれている側のパネルに付きます。

## 図解1：非区分建物が接続して区分建物に

D1289（正しい）：表題登記がある非区分建物の甲・乙が増築で接続して区分建物になった。変更登記は一括申請。D0334（誤り）：独立性のない増築部分は付合して既存建物の所有者のものになる。

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows the correct picture and the mistaken picture side by side. It is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face; use faceless simple pictograms when a person is needed.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「別々の2棟が」
「増築でつながった」
Subtitle (smaller, centered, 1 line):
「区分建物の範囲　状態と正誤のイメージ」
--- SECTION 1: THE STATE (full width, dark navy frame) ---
Section label (navy pill at the top-left of the frame):
「出題文の状態」
Illustration: Isometric illustration of two separate small buildings, one on the left and one on the right, each with its own registry sheet beside it. Between them, a newly built connecting passage joins them into one block; a construction crane and a worker (faceless pictogram) stand at the front. A third faceless person at the front holds a stack of banknotes next to the new passage.
Short labels placed on the objects, each exactly once: 「甲建物」, 「乙建物」, 「増築部分」, 「登記記録」, 「費用を出した人」.
Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.
--- SECTION 2: CLAIM 1 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「接続したら、変更登記は一括で申請する」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: two registry sheets for the left and right buildings are bundled together by a binder clip and handed over a counter in one single hand-over by a faceless person; a faceless clerk receives the bundle. A soft blue glow around the bundle.
Short labels on the left panel, each exactly once: 「甲の書類」, 「乙の書類」, 「一括で提出」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「一括して申請」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: two faceless people at two separate counters on different days (a calendar between them showing two separate dates), each handing over one registry sheet alone. A soft red glow around the separation line.
Short labels on the right panel, each exactly once: 「甲だけ提出」, 「乙だけ提出」, 「別の日」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「別々に申請」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the LEFT (blue) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- SECTION 3: CLAIM 2 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「独立性のない増築部分は共有になる」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: the new passage merges into the existing building owned by one faceless owner (shown with a key); the faceless person with banknotes stands aside and receives nothing. A soft blue glow on the merged building.
Short labels on the left panel, each exactly once: 「既存の所有者」, 「付合する」, 「費用だけ出した人」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「既存の所有者のもの」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: the new passage is split in half with a dividing line; two faceless people stand on either side, each holding a half share token. A soft red glow.
Short labels on the right panel, each exactly once: 「所有者」, 「費用を出した人」, 「共有になる」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「共有者になる」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the RIGHT (red) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 所, 物, 登, 記, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the poster has exactly 1 state section followed by exactly 2 claim row(s), each with a blue left panel and a red right panel, with no duplicated or missing panels, confirm every label appears exactly once and reads exactly as given, confirm the 「出題文の内容」 tag appears exactly 2 time(s), and confirm that no panel contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解2：区分建物の隔壁を取り壊して1個に

D0496（正しい）・D1783（誤り）：隣り合う区分建物の隔壁を除去し、区分建物でない1個の建物にした。所有権の登記名義人が合体による登記等を申請する。

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows the correct picture and the mistaken picture side by side. It is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face; use faceless simple pictograms when a person is needed.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「隣り合う2室の」
「壁を取り払った」
Subtitle (smaller, centered, 1 line):
「区分建物の範囲　状態と正誤のイメージ」
--- SECTION 1: THE STATE (full width, dark navy frame) ---
Section label (navy pill at the top-left of the frame):
「出題文の状態」
Illustration: Isometric illustration of a cutaway condominium floor with two adjacent rooms side by side. The wall between them is half removed with rubble and a worker (faceless pictogram) holding a sledgehammer; the two rooms now form one big space. Beside the building, two registry sheets each marked with an ownership stamp, one for each former room.
Short labels placed on the objects, each exactly once: 「甲区分建物」, 「乙区分建物」, 「隔壁」, 「登記名義人」.
Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.
--- SECTION 2: CLAIM 1 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「区分の要件を欠いたら合体の登記等を申請する」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: one big room with no partition, a faceless owner handing a document folder to a clerk at a counter; a calendar page marked within one month. A new single registry sheet appears, and the two old sheets are stamped as cancelled.
Short labels on the left panel, each exactly once: 「1個の建物」, 「新しい記録」, 「抹消した記録」, 「一月以内」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「合体の登記等を申請」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: the same big room with no partition, but the registry still shows two separate room sheets unchanged on a shelf; the faceless owner walks away without filing anything.
Short labels on the right panel, each exactly once: 「そのまま」, 「2室の記録」, 「申請しない」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「申請せず放置」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the LEFT (blue) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- SECTION 3: CLAIM 2 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「登記名義人は合体の登記等を申請できない」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: two faceless owners standing side by side at a counter, both holding their ownership registry sheets, and the clerk accepts their joint filing document with an open stamp. Soft blue glow.
Short labels on the left panel, each exactly once: 「名義人」, 「もう一人の名義人」, 「申請できる」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「申請できる」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: two faceless owners at a counter blocked by a closed gate sign; the clerk shows a crossed-out filing document. Soft red glow.
Short labels on the right panel, each exactly once: 「名義人」, 「もう一人の名義人」, 「閉まった窓口」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「申請できない」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the RIGHT (red) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 物, 登, 記, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the poster has exactly 1 state section followed by exactly 2 claim row(s), each with a blue left panel and a red right panel, with no duplicated or missing panels, confirm every label appears exactly once and reads exactly as given, confirm the 「出題文の内容」 tag appears exactly 2 time(s), and confirm that no panel contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解3：所有権の登記がない2棟が合体

D1279（正しい）：いずれも表題登記はあるが所有権の登記がない二以上の建物が合体して1個の建物になった。表題部所有者が一月以内に合体による登記等を申請する。

```text
Create a Japanese-language infographic, portrait layout, 1080x1500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows the correct picture and the mistaken picture side by side. It is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face; use faceless simple pictograms when a person is needed.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「表題登記だけの」
「2棟がくっついた」
Subtitle (smaller, centered, 1 line):
「区分建物の範囲　状態と正誤のイメージ」
--- SECTION 1: THE STATE (full width, dark navy frame) ---
Section label (navy pill at the top-left of the frame):
「出題文の状態」
Illustration: Isometric illustration of two small buildings that have been joined by an extension into one building. Each of the two former buildings has a registry sheet with only the title section filled in and an owner's name column on it. A faceless owner stands in front holding both sheets.
Short labels placed on the objects, each exactly once: 「甲建物」, 「乙建物」, 「表題部だけ」, 「表題部所有者」.
Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.
--- SECTION 2: CLAIM 1 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「表題部所有者が一月以内に申請する」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: the faceless owner at a counter hands a folder to a clerk; the calendar shows a page marked within one month; one new registry sheet appears and the two old sheets are stamped as cancelled.
Short labels on the left panel, each exactly once: 「表題部所有者」, 「一月以内」, 「新しい記録」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「一月以内に申請」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: the faceless owner leaves the two registry sheets unchanged on the shelf and the calendar pages turn over many times; a faint red glow over the calendar.
Short labels on the right panel, each exactly once: 「表題部所有者」, 「放置のまま」, 「何か月も経過」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「申請せず放置」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the LEFT (blue) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 所, 物, 登, 記, 請, 過, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the poster has exactly 1 state section followed by exactly 1 claim row(s), each with a blue left panel and a red right panel, with no duplicated or missing panels, confirm every label appears exactly once and reads exactly as given, confirm the 「出題文の内容」 tag appears exactly 1 time(s), and confirm that no panel contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解4：登記の状態が違う2棟が合体

D1638（誤り）：所有権の登記がある甲建物と、所有権の登記はないが表題登記がある乙建物が増築で合体した。乙建物の検査済証を所有権を証する情報として提供できる、は誤り。

```text
Create a Japanese-language infographic, portrait layout, 1080x1500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows the correct picture and the mistaken picture side by side. It is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face; use faceless simple pictograms when a person is needed.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「登記の状態が」
「違う2棟が合体」
Subtitle (smaller, centered, 1 line):
「区分建物の範囲　状態と正誤のイメージ」
--- SECTION 1: THE STATE (full width, dark navy frame) ---
Section label (navy pill at the top-left of the frame):
「出題文の状態」
Illustration: Isometric illustration of two buildings joined by a newly built extension into one building. The left building has a registry sheet with a title section and an ownership section filled in. The right building has a registry sheet with only the title section filled in, the owner column already showing a name. A faceless person at the front holds a certificate of inspection.
Short labels placed on the objects, each exactly once: 「甲建物」, 「乙建物」, 「表題部だけ」, 「検査済証」.
Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.
--- SECTION 2: CLAIM 1 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「乙の検査済証は所有権を証する情報として付けられる」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: a document folder on the counter containing the registry-based items; the right building's registry sheet shows the owner already listed, so a faceless clerk points at the sheet and the inspection certificate is placed aside, not required. The left building's owner uses a small identification key card.
Short labels on the left panel, each exactly once: 「所有者は記録済」, 「不要な書類」, 「登記識別情報」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「乙は証明不要」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: a faceless person attaches the inspection certificate to the filing folder as proof of ownership for the right building, pointing at the right building's registry sheet. Soft red glow.
Short labels on the right panel, each exactly once: 「検査済証」, 「乙にも付ける」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「検査済証を付ける」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the RIGHT (red) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 所, 権, 物, 登, 記, 証, 違, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the poster has exactly 1 state section followed by exactly 1 claim row(s), each with a blue left panel and a red right panel, with no duplicated or missing panels, confirm every label appears exactly once and reads exactly as given, confirm the 「出題文の内容」 tag appears exactly 1 time(s), and confirm that no panel contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解5：敷地権付きの2室が合体

D1082（正しい）・D1579（誤り）：いずれも敷地権付き区分建物の甲・乙が合体し、合体後も敷地権付き区分建物になる。敷地権の割合を合算したものが合体後の割合になるとき、規約証明情報は不要。

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows the correct picture and the mistaken picture side by side. It is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face; use faceless simple pictograms when a person is needed.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「敷地権付きの2室」
「が1室になった」
Subtitle (smaller, centered, 1 line):
「区分建物の範囲　状態と正誤のイメージ」
--- SECTION 1: THE STATE (full width, dark navy frame) ---
Section label (navy pill at the top-left of the frame):
「出題文の状態」
Illustration: Isometric illustration of a condominium cutaway with two adjacent rooms, each with a small land plot shown beneath it as a pie-shaped share (one tenth each), joined into one big room whose land share is the sum (two tenths). Faceless owner standing beside the building.
Short labels placed on the objects, each exactly once: 「甲の持分」, 「乙の持分」, 「合体後の持分」.
Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.
--- SECTION 2: CLAIM 1 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「合算で決まるなら規約証明情報は不要」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: a folder on the counter with only the basic drawings; a separate pile of rule-certificate documents is shown crossed out and set aside, and a faceless clerk nods. Soft blue glow.
Short labels on the left panel, each exactly once: 「基本の書類」, 「不要な書類」, 「足し算で決まる」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「規約証明は不要」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: a folder on the counter with the basic drawings and a pile of rule-certificate documents added on top; a faceless person carries the pile to a clerk. Soft red glow.
Short labels on the right panel, each exactly once: 「基本の書類」, 「規約の書類」, 「追加で提出」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「規約証明を提出」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the LEFT (blue) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- SECTION 3: CLAIM 2 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「合算で決まっても規約証明情報が要る」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: two land-share tokens are added together on a small scale into a single larger token; no extra document appears, and a faceless clerk accepts the filing. Soft blue glow.
Short labels on the left panel, each exactly once: 「持分の足し算」, 「追加書類なし」, 「受理される」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「足し算なら不要」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: the faceless clerk holds up a stop sign at the counter while a stack of rule-certificate documents sits on the desk waiting to be attached. Soft red glow.
Short labels on the right panel, each exactly once: 「規約の書類」, 「待たされる」, 「必ず提出」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「必ず規約証明」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the RIGHT (red) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 権, 物, 規, 証; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the poster has exactly 1 state section followed by exactly 2 claim row(s), each with a blue left panel and a red right panel, with no duplicated or missing panels, confirm every label appears exactly once and reads exactly as given, confirm the 「出題文の内容」 tag appears exactly 2 time(s), and confirm that no panel contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解6：接続する2室を1室にまとめる

D1080（誤り）・D1172（正しい）：所有権の登記名義人が同一で接続している甲・乙の区分建物。主従の関係・効用上の一体は要件でない。

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows the correct picture and the mistaken picture side by side. It is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face; use faceless simple pictograms when a person is needed.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「同じ人が持つ」
「隣り合う2室」
Subtitle (smaller, centered, 1 line):
「区分建物の範囲　状態と正誤のイメージ」
--- SECTION 1: THE STATE (full width, dark navy frame) ---
Section label (navy pill at the top-left of the frame):
「出題文の状態」
Illustration: Isometric illustration of a condominium floor with two adjacent rooms touching along one wall, owned by the same faceless owner (shown with the same name tag on both registry sheets). One room is a living room and the other is a storage room, used separately. A small tag marks the shared wall.
Short labels placed on the objects, each exactly once: 「甲区分建物」, 「乙区分建物」, 「同じ名義人」, 「接する壁」.
Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.
--- SECTION 2: CLAIM 1 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「効用上一体でなくても区分合併できる」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: the two registry sheets are merged by a faceless clerk into one sheet; the two rooms touch along a wall, with a blue check-like soft glow.
Short labels on the left panel, each exactly once: 「接している」, 「同じ名義人」, 「合併できる」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「接続で足りる」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: a faceless clerk shakes his head, holding a sign asking for the rooms to be used as one unit, while the rooms are used separately; a red glow.
Short labels on the right panel, each exactly once: 「別々に利用」, 「一体を要求」, 「断られる」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「一体利用が必要」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the LEFT (blue) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- SECTION 3: CLAIM 2 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「主従の関係がなければ区分合併できない」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: the two rooms touching along a wall are drawn as equal-sized peers with no main or accessory building arrow; the registry sheets are merged by a faceless clerk. Soft blue glow.
Short labels on the left panel, each exactly once: 「対等な2室」, 「接している」, 「合併できる」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「主従は不要」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: a faceless clerk rejects the merge, pointing to a missing arrow marking one room as main and one as accessory. Soft red glow.
Short labels on the right panel, each exactly once: 「主従の矢印なし」, 「断られる」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「主従が必要」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the RIGHT (red) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 効, 対, 建, 物; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the poster has exactly 1 state section followed by exactly 2 claim row(s), each with a blue left panel and a red right panel, with no duplicated or missing panels, confirm every label appears exactly once and reads exactly as given, confirm the 「出題文の内容」 tag appears exactly 2 time(s), and confirm that no panel contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解7：敷地権付き2室を合併したあと

D1290（誤り）：所有権が敷地権として登記されている主である甲・乙の区分建物を区分合併し、一棟の建物が区分建物でなくなる場合。敷地権の表示抹消の変更登記を併せて申請する必要はない。

```text
Create a Japanese-language infographic, portrait layout, 1080x1500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows the correct picture and the mistaken picture side by side. It is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face; use faceless simple pictograms when a person is needed.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「敷地権付きの2室」
「を区分合併する」
Subtitle (smaller, centered, 1 line):
「区分建物の範囲　状態と正誤のイメージ」
--- SECTION 1: THE STATE (full width, dark navy frame) ---
Section label (navy pill at the top-left of the frame):
「出題文の状態」
Illustration: Isometric illustration of a small building that contains exactly two adjacent rooms, each carrying a small land-right mark, with a dashed arrow showing the two rooms will be merged into one ordinary house. Beside it, a land plot whose registry sheet shows a land-right note. A faceless owner stands at the building and a faceless clerk stands near the land's registry sheet.
Short labels placed on the objects, each exactly once: 「甲区分建物」, 「乙区分建物」, 「土地の記録」, 「登記官」.
Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.
--- SECTION 2: CLAIM 1 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「敷地権の抹消の変更登記を併せて申請する」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: the faceless clerk himself stamps the land's registry sheet to remove the land-right note, while the faceless owner submits only the merge filing. Soft blue glow.
Short labels on the left panel, each exactly once: 「合併の申請」, 「登記官が記録」, 「敷地権の抹消」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「登記官が記録する」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: the faceless owner carries two stacks of filing papers to the counter, the merge filing and an extra change filing for removing the land-right note. Soft red glow.
Short labels on the right panel, each exactly once: 「合併の申請」, 「変更登記も」, 「二つ提出」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「併せて申請」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the RIGHT (red) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 権, 物, 登, 記, 請, 録; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the poster has exactly 1 state section followed by exactly 1 claim row(s), each with a blue left panel and a red right panel, with no duplicated or missing panels, confirm every label appears exactly once and reads exactly as given, confirm the 「出題文の内容」 tag appears exactly 1 time(s), and confirm that no panel contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解8：敷地権の違う2室を合併

D0890（正しい）：甲・乙の区分建物で、甲にだけ敷地権の登記。D1694（誤り）：敷地権の割合が相互に異なるときは合併できない。

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows the correct picture and the mistaken picture side by side. It is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face; use faceless simple pictograms when a person is needed.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「敷地権が違う」
「隣り合う2室」
Subtitle (smaller, centered, 1 line):
「区分建物の範囲　状態と正誤のイメージ」
--- SECTION 1: THE STATE (full width, dark navy frame) ---
Section label (navy pill at the top-left of the frame):
「出題文の状態」
Illustration: Isometric illustration of two adjacent condominium rooms touching along a wall. The left room's registry sheet has a land-right entry in its title section; the right room's sheet has none. Beneath the building, the shared land plot shows two different pie-shaped shares for the two rooms.
Short labels placed on the objects, each exactly once: 「甲区分建物」, 「乙区分建物」, 「敷地権あり」, 「敷地権なし」.
Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.
--- SECTION 2: CLAIM 1 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「片方だけ敷地権でも合併できる」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: a faceless clerk merges the two registry sheets, with a checklist of five restrictions all showing no match. Blue glow.
Short labels on the left panel, each exactly once: 「制限に当たらない」, 「合併できる」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「合併できる」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: a faceless clerk rejects the merge and points at the land-right entry as the reason. Red glow.
Short labels on the right panel, each exactly once: 「敷地権の有無」, 「断られる」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「敷地権で断られる」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the LEFT (blue) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- SECTION 3: CLAIM 2 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「敷地権の割合が違えば合併できない」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: two different-sized pie-shaped shares of the same land plot sit side by side, and a faceless clerk merges the two registry sheets regardless. Blue glow.
Short labels on the left panel, each exactly once: 「大きい持分」, 「小さい持分」, 「合併できる」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「割合が違っても可」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: a faceless clerk shakes his head while pointing at two different-sized pie-shaped shares; a red glow.
Short labels on the right panel, each exactly once: 「大きい持分」, 「小さい持分」, 「断られる」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「割合が違うと不可」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the RIGHT (red) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 当, 権, 無, 物, 違; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the poster has exactly 1 state section followed by exactly 2 claim row(s), each with a blue left panel and a red right panel, with no duplicated or missing panels, confirm every label appears exactly once and reads exactly as given, confirm the 「出題文の内容」 tag appears exactly 2 time(s), and confirm that no panel contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解9：共用部分の登記がある建物

D1982（正しい）：甲・乙のいずれにも共用部分である旨の登記がある場合、乙を甲の附属建物とする合併の登記はできない。

```text
Create a Japanese-language infographic, portrait layout, 1080x1500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows the correct picture and the mistaken picture side by side. It is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face; use faceless simple pictograms when a person is needed.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「共用部分とされた」
「2つの建物」
Subtitle (smaller, centered, 1 line):
「区分建物の範囲　状態と正誤のイメージ」
--- SECTION 1: THE STATE (full width, dark navy frame) ---
Section label (navy pill at the top-left of the frame):
「出題文の状態」
Illustration: Isometric illustration of two small meeting-room buildings standing side by side near a condominium building. Each building has a registry sheet whose rights section is blanked out and stamped with a common-area mark, and the owner section is empty. A faceless person stands between them.
Short labels placed on the objects, each exactly once: 「甲建物」, 「乙建物」, 「共用部分の印」, 「権利部なし」.
Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.
--- SECTION 2: CLAIM 1 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「共用部分の登記がある建物は合併できない」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: a faceless clerk holds a stop sign in front of the two sheets with the common-area mark, rejecting a proposed merge. Blue glow.
Short labels on the left panel, each exactly once: 「共用部分の印」, 「合併はできない」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「合併できない」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: a faceless clerk merges the two sheets with the common-area mark into one; red glow with a warning mark.
Short labels on the right panel, each exactly once: 「共用部分の印」, 「合併している」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「合併できてしまう」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the LEFT (blue) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 権, 物, 登, 記; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the poster has exactly 1 state section followed by exactly 1 claim row(s), each with a blue left panel and a red right panel, with no duplicated or missing panels, confirm every label appears exactly once and reads exactly as given, confirm the 「出題文の内容」 tag appears exactly 1 time(s), and confirm that no panel contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解10：附属建物の分割と合併

D0969（誤り）・D1690（正しい）：甲建物の附属建物（区分建物）を分割して乙建物の附属建物に合併する。接続していれば一の申請情報で申請できる。接続していなければできない。

```text
Create a Japanese-language infographic, portrait layout, 1080x2100 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows the correct picture and the mistaken picture side by side. It is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face; use faceless simple pictograms when a person is needed.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「附属建物を切り離」
「別の建物に移す」
Subtitle (smaller, centered, 1 line):
「区分建物の範囲　状態と正誤のイメージ」
--- SECTION 1: THE STATE (full width, dark navy frame) ---
Section label (navy pill at the top-left of the frame):
「出題文の状態」
Illustration: Isometric illustration of a main building A with an accessory condominium unit on its side, and another main building B with its own accessory condominium unit. The unit of A is shown being detached on a dashed outline and moved toward B's accessory unit, which stands close beside it. Registry sheets for A and B sit in front.
Short labels placed on the objects, each exactly once: 「甲建物」, 「乙建物」, 「甲の附属」, 「乙の附属」.
Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.
--- SECTION 2: CLAIM 1 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「接続していなければ分割・合併はできない」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: the two accessory units are separated by an empty plot with a gap marked, and a faceless clerk holds a stop sign. Blue glow.
Short labels on the left panel, each exactly once: 「間が空いている」, 「できない」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「接続していないとできない」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: the two accessory units are separated by an empty plot, yet a faceless clerk stamps an approval. Red glow with a warning mark.
Short labels on the right panel, each exactly once: 「間が空いている」, 「受理される」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「離れていても受理」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the LEFT (blue) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- SECTION 3: CLAIM 2 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「接続していても一の申請はできない」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: the two accessory units touching along a wall, and a single combined filing sheet carrying both the split and merge stamps is accepted by a faceless clerk. Blue glow.
Short labels on the left panel, each exactly once: 「壁で接続」, 「一の申請」, 「受理される」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「一の申請でできる」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: the two accessory units touching along a wall, but the faceless person must submit two separate filing sheets at two separate counters. Red glow.
Short labels on the right panel, each exactly once: 「壁で接続」, 「二つの窓口」, 「別々に申請」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「別々でなければならない」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the RIGHT (red) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 建, 物, 請, 間; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the poster has exactly 1 state section followed by exactly 2 claim row(s), each with a blue left panel and a red right panel, with no duplicated or missing panels, confirm every label appears exactly once and reads exactly as given, confirm the 「出題文の内容」 tag appears exactly 2 time(s), and confirm that no panel contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 図解11：再区分と分筆の登録免許税

D1606（正しい）：2筆の土地の所有権を敷地権とする1個の区分建物を2個にする再区分と、国と私人が共有する土地を2筆にする分筆の登録免許税は、いずれも2,000円。

```text
Create a Japanese-language infographic, portrait layout, 1080x1500 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a scene-illustration poster: it first draws the situation described in a question (the state), then shows the correct picture and the mistaken picture side by side. It is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro paragraph and no prose anywhere. Every panel communicates through the isometric illustration plus short labels placed directly on or beside the objects. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Do not draw any person with a face; use faceless simple pictograms when a person is needed.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
--- HEADER ---
Title (large, bold, 2 lines):
「1つを2つに」
「分けたら税は」
Subtitle (smaller, centered, 1 line):
「区分建物の範囲　状態と正誤のイメージ」
--- SECTION 1: THE STATE (full width, dark navy frame) ---
Section label (navy pill at the top-left of the frame):
「出題文の状態」
Illustration: Isometric illustration with two scenes side by side. On the left, one condominium unit sitting above two land plots is divided by a dotted line into two units. On the right, one shared land plot owned by a government building and a private person is divided into two plots. Coin stacks on a tax counter in front.
Short labels placed on the objects, each exactly once: 「再区分」, 「分筆」, 「2個分」, 「2筆分」.
Below this frame draw one short plain dark navy arrow pointing down; this arrow means only 'next', carries no text, and is NOT a YES or NO arrow.
--- SECTION 2: CLAIM 1 (full-width row) ---
A slim pale-yellow banner across the top of the row, with this claim text exactly:
「どちらも2個分で、2,000円になる」
Below the banner place two panels side by side, equal width, each with a thick rounded frame.
LEFT PANEL (BLUE frame). Panel label (blue pill): 「正しいイメージ」. Illustration: Isometric illustration: two coins of one thousand each stacked beside each divided result on both scenes, totaling two thousand on a faceless clerk's tax counter. Blue glow.
Short labels on the left panel, each exactly once: 「1個千円」, 「もう1個千円」, 「合計二千円」.
Conclusion tag at the bottom of the left panel (blue banner, keyword phrase, not a sentence): 「どちらも2,000円」
RIGHT PANEL (RED frame). Panel label (red pill): 「誤ったイメージ」. Illustration: Isometric illustration: an extra coin pile is added for each land plot beneath the divided unit, making a tall stack of coins at the tax counter. Red glow with a warning mark.
Short labels on the right panel, each exactly once: 「土地の筆数も」, 「高い税額」.
Conclusion tag at the bottom of the right panel (red banner, keyword phrase, not a sentence): 「土地分も数える」
Put a small dark navy tag reading 「出題文の内容」 on the top edge of the LEFT (blue) panel only (the other panel carries no such tag); it marks the panel that depicts what the question statement says.
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 建, 物; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the poster has exactly 1 state section followed by exactly 1 claim row(s), each with a blue left panel and a red right panel, with no duplicated or missing panels, confirm every label appears exactly once and reads exactly as given, confirm the 「出題文の内容」 tag appears exactly 1 time(s), and confirm that no panel contains a full sentence of explanatory prose. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 見出し画像

note見出し画像（1280×670px）です。ChatGPTに、キャラクターの参照画像（トリ先生と藍子の基準画像。`CHATGPT_MANGA_WORKFLOW.md` §3の6枚）を添付し、どちらがトリ先生でどちらが藍子かを一言添えて、下のコードブロックを貼ります。

- タイトル1行目：つながった？
- タイトル2行目：壁を取った？（「壁を取った」を赤みのあるオレンジ）
- サブタイトル：苦手克服　区分建物の範囲（7）

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief), placed at the lower left of center. 藍子 is the young woman exam candidate (long wavy brown hair, pinstriped light-blue blouse with rolled sleeves, navy pencil skirt, no jacket), placed at the lower right of center. POSES ARE NOT FIXED: do not copy any pose from the attached images or from earlier header images; let each character take a free, natural pose of your own choosing that fits the topic and suits the character (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep both characters fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral(s) 7; the only digits allowed are those in the text exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
つながった？
Line 2 is larger; the phrase 壁を取った is red-orange and the rest is dark navy:
壁を取った？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
苦手克服　区分建物の範囲（7）
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: Isometric scene of a condominium cutaway with the wall between two rooms removed and a faceless worker with a sledgehammer
Right side: Isometric scene of two small separate buildings joined by a newly built passage with a crane

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 克, 分, 区, 取, 囲, 壁, 建, 手, 服, 物, 範, 苦; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
