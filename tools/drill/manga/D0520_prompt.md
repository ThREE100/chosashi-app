# D0520 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

- 肢：D0520（民法／物権変動・対抗要件、出典 H22-Q02オ）。正解＝〇。誤解4回。
- 記事：`note-articles/h22-mondai/q02-taikou-youken-177.md` オ「未成年者の取消しは、その前に現れた善意の買主にも対抗できる」
- ルール：`MANGA_RULES.md`
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の5枚。トリ先生・藍子の基準画像）** を添付し、下のコードブロックを貼る。トリ先生の参照画像と藍子の参照画像が別ファイルの場合は、どちらがどちらかを貼り付けの冒頭に一言添える。サイズは 1080×1920（9:16）。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 未成年者の取消しは、善意のＢにも対抗できる | 「善意のＢにも対抗できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 | 藍子（左） | Ｂは未成年だと知らなかった。守られますよね？ | 「守られますよね？」 |
| コマ1 | トリ先生（右） | 出たわね、その思い込み。Ａが取り消す前にＢが買った場合よ | — |
| コマ1 | 図ラベル | Ａ（未成年者）→Ｄ→Ｂ（善意）／Ｃ（Ａの法定代理人）／矢印ラベル「Ｃの同意なし」 | — |
| コマ2 見出し | ラベル | ②　流れを整理 | — |
| コマ2 | 図（3つの別カード。取引の矢印はＡ→Ｄ、Ｄ→Ｂのみ） | ①ＡがＤに売却（Ｃの同意なし） / ②ＤがＢに売却（Ｂは善意） / ③Ｃが①の売買を取消し（スタンプ「取消し」） | — |
| コマ2 | 図ラベル | Ａの所有権が回復 | — |
| コマ2 | 図の矢印ラベル | 取消しは当初にさかのぼる | 黄色マーカー |
| コマ2 | 藍子（左・先に話す） | 取り消すと、どうなるんですか？ | — |
| コマ2 | トリ先生（右・答える） | 取消しの効果は、当初にさかのぼるのよ | 「当初にさかのぼる」 |
| コマ3 見出し | ラベル | ③　詐欺取消しとの違い | — |
| コマ3 左カード | 見出し | 詐欺取消し | — |
| コマ3 左カード | 本文／タグ | 善意無過失の第三者は守られる ／ 民法96条3項 | 青チェック✓ |
| コマ3 右カード | 見出し | 制限行為能力の取消し | — |
| コマ3 右カード | 本文 | 善意のＢでも守られない | 赤✕ |
| コマ3 | 藍子（左・先に話す） | 詐欺取消しだと、第三者は守られるのに… | — |
| コマ3 | トリ先生（右・答える） | 違いは、第三者を守る規定があるかどうかよ | 「守る規定」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 | 藍子（左） | Ａは善意のＢにも所有権を主張できるんですね！ | — |
| コマ4 | トリ先生（右） | そのとおり。取消し前に現れた善意の買主にも対抗できるのよ | 「対抗できる」 |
| コマ4 チェック欄 | 3項目（青✓） | 取消しは当初にさかのぼる ／ 善意の第三者を守る規定がない ／ Ａは所有権をＢに主張できる | — |
| 結論帯 | 1行目 | 制限行為能力の取消しは、善意の第三者にも対抗できる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0520　正解〇（H22-Q02オ） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ Ｃ Ｄ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a navy business suit over a blouse with thin blue vertical stripes; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ, Ｃ, Ｄ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「未成年者の取消しは、善意のＢにも対抗できる」 in large bold letters; the part 「善意のＢにも対抗できる」 has a yellow highlighter marker.

PANEL 1 (the common misconception; 藍子 confident, トリ先生 exasperated but caring):
- Label tab: 「①　よくある思い込み」
- 藍子 bubble (left): 「Ｂは未成年だと知らなかった。守られますよね？」 with the part 「守られますよね？」 highlighted in yellow.
- トリ先生 bubble (right): 「出たわね、その思い込み。Ａが取り消す前にＢが買った場合よ」
- Small diagram in the middle: three faceless pictograms in a row with arrows: a small young pictogram with tag 「Ａ」, then a pictogram with tag 「Ｄ」, then a pictogram with tag 「Ｂ」. The arrow from Ａ to Ｄ carries the small label 「Ｃの同意なし」. Standing right behind 「Ａ」 is a taller adult pictogram with tag 「Ｃ」 and the small label 「Ｃ（Ａの法定代理人）」, so that Ｃ is introduced here. Caption under the diagram: 「Ａ（未成年者）→Ｄ→Ｂ（善意）」.

PANEL 2 (the flow; 藍子 surprised, トリ先生 explaining with a wing-pointer):
- Label tab: 「②　流れを整理」
- Three SEPARATE numbered cards in a row, left to right. Do NOT connect the cards with arrows, and do NOT draw any arrow from Ｂ to Ｃ. Arrows exist only inside card 1 (Ａ to Ｄ) and card 2 (Ｄ to Ｂ).
  - Card 1: pictograms 「Ａ」 and 「Ｄ」 with one arrow from Ａ to Ｄ; text 「①ＡがＤに売却（Ｃの同意なし）」.
  - Card 2: pictograms 「Ｄ」 and 「Ｂ」 with one arrow from Ｄ to Ｂ; text 「②ＤがＢに売却（Ｂは善意）」.
  - Card 3: NOT a sale. It shows the adult pictogram 「Ｃ」 holding a large dark navy round stamp that reads 「取消し」; text 「③Ｃが①の売買を取消し」.
- One curved dark navy arrow starts at the stamp in card 3 and points back to the Ａ-to-Ｄ arrow in card 1 (cancelling that sale). Its label 「取消しは当初にさかのぼる」 has a yellow highlighter marker. Next to the pictogram 「Ａ」 in card 1 add the small label 「Ａの所有権が回復」.
- 藍子 bubble (left, spoken first): 「取り消すと、どうなるんですか？」
- トリ先生 bubble (right, spoken as the answer): 「取消しの効果は、当初にさかのぼるのよ」 with 「当初にさかのぼる」 highlighted in yellow.

PANEL 3 (the contrast; both characters point together at the same comparison cards):
- Label tab: 「③　詐欺取消しとの違い」
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows a BLUE check mark; the right card shows a RED cross. Do not draw the same mark on both cards. The two cards also have clearly different texts; the two texts are NOT identical.
- Left card, heading 「詐欺取消し」, body 「善意無過失の第三者は守られる」, small tag 「民法96条3項」, with ONE blue check mark only (no cross on this card).
- Right card, heading 「制限行為能力の取消し」, body 「善意のＢでも守られない」, with ONE red cross only (no check mark on this card).
- 藍子 bubble (left, spoken first): 「詐欺取消しだと、第三者は守られるのに…」
- トリ先生 bubble (right, spoken as the answer): 「違いは、第三者を守る規定があるかどうかよ」 with 「守る規定」 highlighted in yellow.

PANEL 4 (the conclusion; 藍子 relieved, トリ先生 smiling proudly):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left): 「Ａは善意のＢにも所有権を主張できるんですね！」
- トリ先生 bubble (right): 「そのとおり。取消し前に現れた善意の買主にも対抗できるのよ」 with 「対抗できる」 highlighted in yellow.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「取消しは当初にさかのぼる」, 「善意の第三者を守る規定がない」, 「Ａは所有権をＢに主張できる」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「制限行為能力の取消しは、善意の第三者にも対抗できる」 with a yellow highlighter marker.
- Line 2: 「問題D0520　正解〇（H22-Q02オ）」

EMOTIONAL ARC: confident (panel 1) -> surprised (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels; confirm the characters 権, 所, 売, 買, 当, 初, 詐, 欺, 規, 対, 抗, 無, 過, 効, 張, 解, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm the left comparison card in panel 3 has only a blue check mark and the right card only a red cross; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0520_prompt.md` が NG 0件・WARN 0件（2026-10-06）
- [x] 工程C：登場人物Ｃは1コマ目で紹介／取消しは売買の鎖の外（別カード）／藍子の質問→トリ先生の答えの順／青＝はい・赤＝いいえ・ネイビー＝中立

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く
- [ ] 2人の外見が添付画像どおり・全コマで同一
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致（Ａ〜Ｄの取り違えなし）
- [ ] コマ3：左＝青✓のみ、右＝赤✕のみ。カード文言が別々
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）

## v01の検品結果と修正（2026-10-06）
- v01（生成画像）の問題：①Ｃが初出なのにコマ2で突然登場し、Ｂ→Ｃの矢印で「ＢがＣに売った」ように見える。②赤い戻り矢印の起点がＣの人物で、「取消し」という出来事の矢印になっていない。③コマ1で藍子の吹き出しの文言が構成表と違った（表を現状の画像に合わせた）。④コマ2・3で藍子の反応が先に読まれ、トリ先生の説明より前に「気づき」が来る順序のずれ。⑤コマ2の「Ｂが買う前にもどる」は遡及の説明として不正確。
- 修正：Ｃをコマ1で「Ａの法定代理人」として登場させる。コマ2は3つの独立したカードにし、③は売買ではなく「取消し」のスタンプとして描く。藍子は質問、トリ先生は答えの順にする。

### ChatGPTへの修正依頼文（v01の画像を基準に貼る）
```text
直前に表示された最新版（v01）を基準に、以下の修正だけ行ってください。
1. コマ1：Ａ→Ｄの矢印に小さなラベル「Ｃの同意なし」を付ける。Ａの後ろに、背の高い大人のピクトグラム（タグ「Ｃ」）を立たせ、小さなラベル「Ｃ（Ａの法定代理人）」を付ける。
2. コマ2の流れ図を、矢印でつながない3つの別カードに描き直す。矢印はカード1の中のＡ→Ｄ、カード2の中のＤ→Ｂだけにし、Ｂ→Ｃの矢印は描かない。カード1「①ＡがＤに売却（Ｃの同意なし）」、カード2「②ＤがＢに売却（Ｂは善意）」、カード3は売買ではなく、ピクトグラム「Ｃ」がネイビーの丸い「取消し」のスタンプを持つ図にして、文言は「③Ｃが①の売買を取消し」。ネイビーの曲がった矢印はカード3のスタンプからカード1のＡ→Ｄの矢印へ戻し、ラベル「取消しは当初にさかのぼる」（黄色マーカー）を付ける。カード1のＡの横に小さなラベル「Ａの所有権が回復」を足す。
3. コマ2の藍子（左）の吹き出し全体を、「えっ、Ｂが買う前にもどるんですか？」から「取り消すと、どうなるんですか？」へ変更する。
4. コマ3の藍子（左）の吹き出し全体を、「同じ取消しなのに、第三者の扱いが違うんですね」から「詐欺取消しだと、第三者は守られるのに…」へ変更する。

変更しない箇所：上記以外のすべての文字・色・人物・表情・背景・吹き出しの位置と形、タイトル帯、コマ3の比較カード、コマ4、結論帯。
指定文言を一字ずつ正確に入れ、指定外の文字を追加しないでください。完成画像全体を1枚で表示してください。
```

## v02の検品結果（2026-10-06）→ 採用
採用版：`images/D0520_v02_adopted.webp`（v01は不採用。画像は9:16の縦長）。
- 合格：①Ｃはコマ1で「Ｃ（Ａの法定代理人）」として登場し、コマ2では3つの独立カードになった（Ｂ→Ｃの矢印なし、③は「取消し」のスタンプ）。②藍子（左）の質問→トリ先生（右）の答えの順になり、尾は各話者を向いている。③コマ2の戻り矢印・スタンプはネイビー、コマ3は左＝青✓・右＝赤✕で極性が逆、コマ4のチェックは青。④タイトル・全セリフ・ラベル・結論帯は構成表と一致。簡体字・余計な文字なし、背景は不透明。⑤法的内容は記事（H22-Q02オ）の範囲内（民法96条3項は記事に記載あり）。
- 軽微（採用に影響しない）：(a) 「Ａ・Ｂ・Ｃ・Ｄ」が半角で描かれた（構成表は全角）。意味は同じなので許容とし、規則は全角・半角どちらも可に改めた。(b) コマ2の「取消し」スタンプがカードの右端からはみ出し、トリ先生の指し棒に近い。(c) コマ2の藍子の前髪が他のコマと少し違う。(d) コマ3でトリ先生がカードを指さしていない（藍子だけが指さす）。
- 次回以降のプロンプトに反映：スタンプ・矢印・ラベルは各カードの枠の内側に収める。
- 限定修正（v03）の依頼文：`D0520_v03_fix_request.md`（(b)(c)(d)の3点だけを直す。(a)は許容）。
