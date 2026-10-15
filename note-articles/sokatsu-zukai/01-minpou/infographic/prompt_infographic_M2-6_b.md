# 【M2-6】袋地の通行権と付合の償金は、どんな場面で、どう認められるのか　追加の図解インフォグラフィック プロンプト（1枚）

総合記事 `note-articles/column/sokatsu-01-minpou-ch2.md`（民法編・第2章）の論点【M2-6】に差し込む、追加の図解のプロンプトです。既存の図解（`prompt_infographic_M2-6.md`＝一般の袋地と分割の袋地の対比表・付合の償金の流れ）は変更せず、表には言葉でしか書かれていない「袋地・公道側の土地・ほかの人の土地の位置関係」を、上から見た地図で補います。記事の「たとえば」（土地を二つに分けて公道側を売り、奥の土地が袋地になった例）と、中身の整理にある競売の場合、通行権の主張に登記が要らない点を、地図2枚とカード1枚で描きます。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。この図は、はい／いいえの分岐ではないため、青・赤は使いません。画像の中には、図の番号・問題番号・個人の演習結果を入れません。土地はラテン文字や甲乙丙を使わず、位置の語（公道側の土地・奥の土地・ほかの人の土地）で書きます。

| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |
|---|---|---|---|---|---|
| 図解1 | 分割・一部譲渡・競売で袋地ができたとき（通れる土地を上から見た図で示す） | 位置関係図型（2枚の地図パネル＋カード1枚） | 1080×2700 | 民法編2_M2-6_追加_分割で袋地ができたとき.png | 【M2-6】の「たとえば」の直後 |

画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。

## 図解1：分割・一部譲渡・競売で袋地ができたとき（通れる土地を上から見た図で示す）

- 型：位置関係図型（2枚の地図パネル＋カード1枚）　／　サイズ：1080×2700　／　保存名：`民法編2_M2-6_追加_分割で袋地ができたとき.png`
- 記事の挿入位置：【M2-6】の「たとえば」の直後

```text
Create a Japanese-language infographic, portrait layout, 1080x2700 pixels, clean flat-design isometric illustration style with soft pastel colors (light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). This is a map-diagram poster with two map panels and one small card in one column; it is NOT a text-heavy document.
GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the panels. Each panel communicates its point through the map plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.
CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.
BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.
COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.
Use neutral dark navy outlines only on this poster; draw no check mark and no cross mark anywhere, and use no blue or red. All person pictograms are faceless and drawn in ONE single identical light gray-blue color, the very same shade for every one of them (they differ only by their name tags). The two map panels use exactly the same map layout (same plots in the same positions); they differ only in the labels given below.
--- HEADER ---
Title (large, bold, 2 lines):
「分割で袋地ができたとき」
「通れるのは、分けた相手の土地だけ」
Subtitle (smaller, centered, 1 line):
「民法 第213条」
--- PANEL 1 ---
Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「一筆を分けて譲渡したとき」
Illustration: The map is a flat top-down view (NOT isometric) inside the panel: a thin light-gray strip along the bottom edge labeled 「公道」. Directly above the road strip, one rectangular land plot labeled 「公道側の土地」 (pale cream fill). Directly above that plot, touching it, a second rectangular plot of the same width labeled 「奥の土地」 (pale blue fill) with the small light-gray label 「袋地」. The 奥の土地 does not touch the road. At the left of both plots, a tall plot labeled 「ほかの人の土地」 (pale gray fill) that touches the road and the 奥の土地. A solid dark navy path line starts inside the 奥の土地, runs straight down through the 公道側の土地, and ends at the road strip, carrying the label 「通れる」 in a pale yellow highlighter marker. A short dotted dark navy line from the 奥の土地 toward the ほかの人の土地 stops at a small dark navy bar drawn across it, carrying the small light-gray label 「通れない」. A thin dotted line between the 公道側の土地 and the 奥の土地 carries the small label 「分筆」, and a small rubber stamp icon on the 公道側の土地 carries the label 「譲渡した土地」.
Under the map, two small light-gray tags side by side: 「償金は要らない」 and 「民法213条1項・2項」.
Conclusion tag (a short pale-yellow banner directly below the map, a keyword phrase, not a sentence):
「分けた相手の土地だけ」
--- PANEL 2 ---
Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「抵当権の実行で競落されたとき」
Illustration: The map is a flat top-down view (NOT isometric) inside the panel: a thin light-gray strip along the bottom edge labeled 「公道」. Directly above the road strip, one rectangular land plot labeled 「公道側の土地」 (pale cream fill). Directly above that plot, touching it, a second rectangular plot of the same width labeled 「奥の土地」 (pale blue fill) with the small light-gray label 「袋地」. The 奥の土地 does not touch the road. At the left of both plots, a tall plot labeled 「ほかの人の土地」 (pale gray fill) that touches the road and the 奥の土地. A solid dark navy path line starts inside the 奥の土地, runs straight down through the 公道側の土地, and ends at the road strip, carrying the label 「通れる」 in a pale yellow highlighter marker. A short dotted dark navy line from the 奥の土地 toward the ほかの人の土地 stops at a small dark navy bar drawn across it, carrying the small light-gray label 「通れない」. Here the 公道側の土地 carries a small rubber stamp icon labeled 「抵当権」 and a small gavel icon labeled 「競落」, and a small light-gray label 「他人の土地になった」. Above both plots a thin bracket carries the small label 「もとは同じ持ち主の土地」.
Under the map, one small light-gray tag: 「分割に準じて扱う（判例）」.
Conclusion tag (a short pale-yellow banner directly below the map, a keyword phrase, not a sentence):
「競売でも、同じ扱い」
--- CARD 3 ---
Badge: a filled dark navy circle containing the number 3 (numbers run 1 to 3 in order).
Heading (bold, ONE line):
「通行権の主張に、登記は要らない」
Illustration: a faceless pictogram tagged 「奥の土地を買った人」 beside a registry ledger icon drawn with a thin dotted outline and the small label 「名義は前の持ち主のまま」, and a plain dark navy path line leading from the pictogram to a road strip.
Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):
「法律上当然に生じる（判例）」
--- FOOTER ---
Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 地, 売, 張, 当, 抵, 権, 渡, 登, 記, 譲, 買; if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. Confirm the number of panels and cards equals 3 exactly, numbered 1 to 3 in order, that panel 1 and panel 2 use the same map layout with the 公道 strip at the bottom, the 公道側の土地 above it, the 奥の土地 above that, and the ほかの人の土地 at the left, that the solid path line goes through the 公道側の土地 to the road in both panels, that the dotted line toward the ほかの人の土地 ends at a small dark navy bar labeled 通れない in both panels, that card 3 is the last element, and confirm that no check mark, cross mark, blue, or red appears anywhere. Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

## 検品チェック（生成後）

- パネルとカードがちょうど3つ（番号1・2・3）で、カード3のあとに何も描かれていないか。
- パネル1とパネル2の地図が同じ配置か（下から順に、公道・公道側の土地・奥の土地、左側にほかの人の土地）。実線の道が公道側の土地を通って公道へ出ているか。ほかの人の土地へ向かう点線が、棒で止まって「通れない」とあるか。
- パネル2に「抵当権」「競落」「他人の土地になった」「もとは同じ持ち主の土地」があり、パネル1に「分筆」「譲渡した土地」があるか。
- 見出し・タグの文字を、上のコードブロックの文言と一字ずつ突き合わせた（「袋」「譲渡」「分筆」「競落」「抵当」「償」「登記」が簡体字・別字になっていない）。
- 青・赤・○×の印がどこにもない。図の番号・問題番号・個人の演習結果がない。背景は完全に不透明。

## 記事・条文との照合（作成者用）

- 民法210条1項（他の土地に囲まれて公道に通じない土地の所有者は、公道に至るため、その土地を囲んでいる他の土地を通行できる）、212条（210条の通行権者は、通行する他の土地の損害に対して償金を支払う）、213条1項（分割によって公道に通じない土地が生じたときは、他の分割者の所有地のみを通行でき、償金を支払うことを要しない）・2項（土地の一部を譲り渡した場合に準用）を `note-articles/laws/minpou-1-soukyoku-bukken.md` の原文で確認。
- パネル1の地図は213条1項2項の構造（分けた相手の土地だけが通れる）を、記事の『たとえば』の位置関係として描いた。『ほかの人の土地』は通れない（213条は他の分割者の所有地のみ）。
- パネル2の競売は、記事が『判例の立場』とする整理で、条文に明記はない。図は『分割に準じて扱う（判例）』と添えた。記事は『一筆の土地の一部に設定された抵当権が実行されて競落された場合』と書くが、取り上げられた事案は、同じ持ち主の二つの土地のうち一方に抵当権が付いていたものなので、図は『もとは同じ持ち主の土地』とし、一筆か二筆かは断定していない。
- カード3の『法律上当然に生じる』『登記は要らない』は、記事の中身の整理（袋地の通行権は法律上当然に生じ、所有権の移転の登記がなくても主張できる〔判例〕）による。条文に直接の記述はないので『（判例）』と添えた。
- 一般の袋地（210条・212条）は既存の図解の左列に任せ、この図には描いていない。
