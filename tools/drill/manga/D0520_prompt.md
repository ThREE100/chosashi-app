# D0520 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D0520（民法／物権変動・対抗要件、出典 H22-Q02オ）。正解＝〇。誤解4回。
- 記事：`note-articles/h22-mondai/q02-taikou-youken-177.md` オ「未成年者の取消しは、その前に現れた善意の買主にも対抗できる」
- ルール：`MANGA_RULES.md`
- 使い方：ChatGPTに **添付画像1＝案内役（先生）、添付画像2＝生徒役** を添付し、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 未成年者の取消しは、善意のＢにも対抗できる | 「善意のＢにも対抗できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 | 生徒（左） | Ｂは未成年だと知らなかった。守られるよね？ | 「守られるよね？」 |
| コマ1 | 案内役（右） | Ａが取り消す前に、Ｂが買っていた場合だね | — |
| コマ1 | 図ラベル | Ａ（未成年者）→Ｄ→Ｂ（善意） | — |
| コマ2 見出し | ラベル | ②　流れを整理 | — |
| コマ2 | 図 | ①ＡがＤに売却（Ｃの同意なし） / ②ＤがＢに売却（Ｂは善意） / ③Ｃが取消し | — |
| コマ2 | 図の矢印ラベル | 取消しは当初にさかのぼる | 黄色マーカー |
| コマ2 | 案内役（右） | 取消しの効果は、当初にさかのぼるよ | 「当初にさかのぼる」 |
| コマ2 | 生徒（左） | えっ、Ｂが買う前にもどるの？ | — |
| コマ3 見出し | ラベル | ③　詐欺取消しとの違い | — |
| コマ3 左カード | 見出し | 詐欺取消し | — |
| コマ3 左カード | 本文／タグ | 善意無過失の第三者は守られる ／ 民法96条3項 | 青チェック✓ |
| コマ3 右カード | 見出し | 制限行為能力の取消し | — |
| コマ3 右カード | 本文 | 善意のＢでも守られない | 赤✕ |
| コマ3 | 生徒（左） | 同じ取消しでも、第三者の扱いが違うんだ | — |
| コマ3 | 案内役（右） | 違いは、第三者を守る規定があるかどうか | 「守る規定」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 | 生徒（左） | Ａは善意のＢにも所有権を主張できるんだ！ | — |
| コマ4 | 案内役（右） | そのとおり。取消し前に現れた善意の買主にも対抗できるよ | 「対抗できる」 |
| コマ4 チェック欄 | 3項目（青✓） | 取消しは当初にさかのぼる ／ 善意の第三者を守る規定がない ／ Ａは所有権をＢに主張できる | — |
| 結論帯 | 1行目 | 制限行為能力の取消しは、善意の第三者にも対抗できる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0520　正解〇（H22-Q02オ） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ Ｃ Ｄ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: Attached image 1 is the TEACHER (案内役). Attached image 2 is the STUDENT (生徒役). Treat both attachments as authoritative references and reproduce each character faithfully in every panel: same face, hair, clothing, colors, proportions, and drawing style. Only expression, gaze, hand position, and posture may change. Do not add any other character. The legal parties Ａ, Ｂ, Ｃ, Ｄ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels the STUDENT stands on the LEFT side of the panel and the TEACHER stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, student first, then teacher.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Affirmative marks (check marks) are BLUE. Negative marks (crosses) are RED. Do not use green.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「未成年者の取消しは、善意のＢにも対抗できる」 in large bold letters; the part 「善意のＢにも対抗できる」 has a yellow highlighter marker.

PANEL 1 (the common misconception; student confident, teacher listening calmly):
- Label tab: 「①　よくある思い込み」
- Student bubble (left): 「Ｂは未成年だと知らなかった。守られるよね？」 with the part 「守られるよね？」 highlighted in yellow.
- Teacher bubble (right): 「Ａが取り消す前に、Ｂが買っていた場合だね」
- Small diagram in the middle: three faceless pictograms in a row with arrows: a small young pictogram with tag 「Ａ」, then a pictogram with tag 「Ｄ」, then a pictogram with tag 「Ｂ」. Caption under the diagram: 「Ａ（未成年者）→Ｄ→Ｂ（善意）」.

PANEL 2 (the flow; student surprised, teacher explaining with a pointer):
- Label tab: 「②　流れを整理」
- A three-step horizontal timeline diagram with pictograms and arrows, the step texts exactly: 「①ＡがＤに売却（Ｃの同意なし）」, 「②ＤがＢに売却（Ｂは善意）」, 「③Ｃが取消し」. Include a small faceless pictogram tagged 「Ｃ」 near step ③.
- A curved return arrow from step ③ back to step ① with the label 「取消しは当初にさかのぼる」 highlighted in yellow.
- Teacher bubble (right): 「取消しの効果は、当初にさかのぼるよ」 with 「当初にさかのぼる」 highlighted in yellow.
- Student bubble (left): 「えっ、Ｂが買う前にもどるの？」

PANEL 3 (the contrast; both characters point together at the same comparison cards):
- Label tab: 「③　詐欺取消しとの違い」
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows a BLUE check mark; the right card shows a RED cross. Do not draw the same mark on both cards. The two cards also have clearly different texts; the two texts are NOT identical.
- Left card, heading 「詐欺取消し」, body 「善意無過失の第三者は守られる」, small tag 「民法96条3項」, with ONE blue check mark only (no cross on this card).
- Right card, heading 「制限行為能力の取消し」, body 「善意のＢでも守られない」, with ONE red cross only (no check mark on this card).
- Student bubble (left): 「同じ取消しでも、第三者の扱いが違うんだ」
- Teacher bubble (right): 「違いは、第三者を守る規定があるかどうか」 with 「守る規定」 highlighted in yellow.

PANEL 4 (the conclusion; student relieved, teacher smiling):
- Label tab: 「④　結論は〇」
- Student bubble (left): 「Ａは善意のＢにも所有権を主張できるんだ！」
- Teacher bubble (right): 「そのとおり。取消し前に現れた善意の買主にも対抗できるよ」 with 「対抗できる」 highlighted in yellow.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「取消しは当初にさかのぼる」, 「善意の第三者を守る規定がない」, 「Ａは所有権をＢに主張できる」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「制限行為能力の取消しは、善意の第三者にも対抗できる」 with a yellow highlighter marker.
- Line 2: 「問題D0520　正解〇（H22-Q02オ）」

EMOTIONAL ARC: confident (panel 1) -> surprised (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm the student is always on the left and the teacher always on the right and every bubble tail points at its own speaker; confirm both attached characters look identical in all panels; confirm the characters 権, 売, 買, 当, 初, 詐, 欺, 規, 対, 抗, 無, 過, 効, 張 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm the left comparison card in panel 3 has only a blue check mark and the right card only a red cross; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで生徒＝左・案内役＝右、全吹き出しの尾が話者へ向く
- [ ] 2人の外見が添付画像どおり・全コマで同一
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致（Ａ〜Ｄの取り違えなし）
- [ ] コマ3：左＝青✓のみ、右＝赤✕のみ。カード文言が別々
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）
