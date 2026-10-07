# D0002 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D0002（民法／共有・所有権・占有、出典 H17-Q01イ）。正解＝×（誤った記述）。誤解3回。
- 記事：`note-articles/h17-mondai/q01-kyoyu-hozon-kanri.md` イ「共有者の一人が単独で占有していても、他の共有者は直ちには明渡請求できない」
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の5枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 登場人物：Ａ・Ｂ・Ｃ（甲建物を3分の1ずつ共有）をコマ1で紹介。
- 矢印の意味：コマ1の矢印は「明渡しの請求」（請求）。取引の矢印はない。
- 会話順：藍子の誤解（直ちに請求できる）→Ａにも使う権原がある→過半数でも直ちには請求できない→結論（記述は×）。
- 配色：コマ3の左カード（持分の過半数でも直ちには請求できない）だけ赤✕、右カードは印なし。
- 記事の範囲：単独占有する共有者も自己の持分に基づく使用収益の権原を有する／持分の過半数でも当然には明渡しを請求できない／明渡しを求めるには理由の主張・立証が必要／現行の民法でも結論は変わらない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 共有者の単独占有に、直ちに明渡請求はできない | 「直ちに明渡請求はできない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 図 | 図・カード | 甲建物 / 持分は各3分の1 / Ａ / 単独で占有 / Ｂ / Ｃ / 明渡しの請求 / Ａ・Ｂ・Ｃが甲建物を共有 | — |
| コマ1 | 藍子（左・先に話す） | ＢとＣは、Ａに直ちに明渡しを請求できますよね？ | 「直ちに明渡しを請求できますよね？」 |
| コマ1 | トリ先生（右・答える） | 出たわね、その思い込み。持分は3分の1ずつよ | — |
| コマ2 見出し | ラベル | ②　Ａにも使う権原がある | — |
| コマ2 図 | 図・カード | 甲建物 / Ａ / 持分に基づく使用収益の権原 | — |
| コマ2 | 藍子（左・先に話す） | Ａは了解を得ていないのに、使えるんですか？ | — |
| コマ2 | トリ先生（右・答える） | Ａも自分の持分に基づいて使う権原を持っているのよ | 「持分に基づいて使う権原」 |
| コマ3 見出し | ラベル | ③　過半数でも直ちには請求できない | — |
| コマ3 図 | 図・カード | 持分の過半数 / 直ちには請求できない / 明渡しの請求 / 理由の主張・立証が必要 / 現行の民法でも結論は同じ | — |
| コマ3 | 藍子（左・先に話す） | ＢとＣで過半数なのに、直ちには請求できないんですか？ | — |
| コマ3 | トリ先生（右・答える） | そう。明渡しを求めるには、理由の主張と立証が必要よ | 「理由の主張と立証」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 直ちに明渡しを請求できるという記述は、誤りなんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。Ａも使う権原を持つから、直ちには請求できないのよ | 「直ちには請求できない」 |
| コマ4 チェック欄 | 3項目（青✓） | Ａも持分に基づいて使う権原がある / 持分が過半数でも直ちには請求できない / 明渡しには理由の主張・立証が必要 | — |
| 結論帯 | 1行目 | 単独で占有する共有者に、他の共有者は直ちには明渡請求できない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0002　正解×（H17-Q01イ） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ Ｃ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a navy business suit over a blouse with thin blue vertical stripes; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ, Ｃ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「共有者の単独占有に、直ちに明渡請求はできない」 in large bold letters; the part 「直ちに明渡請求はできない」 has a yellow highlighter marker.

PANEL 1 (藍子 confident, トリ先生 exasperated but caring):
- Label tab: 「①　よくある思い込み」
- Small diagram in the middle: a flat house icon labeled 「甲建物」 with a small badge above it reading 「持分は各3分の1」. Inside the house stands a faceless pictogram with tag 「Ａ」 and a small label 「単独で占有」. Outside the house on the right stand two faceless pictograms with tags 「Ｂ」 and 「Ｃ」; a solid navy arrow from Ｂ and Ｃ toward Ａ carries the label 「明渡しの請求」. Caption under the diagram: 「Ａ・Ｂ・Ｃが甲建物を共有」.
- 藍子 bubble (left, spoken first): 「ＢとＣは、Ａに直ちに明渡しを請求できますよね？」 with the part 「直ちに明渡しを請求できますよね？」 highlighted in yellow.
- トリ先生 bubble (right, spoken as the answer): 「出たわね、その思い込み。持分は3分の1ずつよ」.

PANEL 2 (藍子 puzzled, トリ先生 explaining with a wing-pointer):
- Label tab: 「②　Ａにも使う権原がある」
- The house icon 「甲建物」 again, with pictogram 「Ａ」 inside holding a large key tagged 「持分に基づく使用収益の権原」.
- 藍子 bubble (left, spoken first): 「Ａは了解を得ていないのに、使えるんですか？」.
- トリ先生 bubble (right, spoken as the answer): 「Ａも自分の持分に基づいて使う権原を持っているのよ」 with the part 「持分に基づいて使う権原」 highlighted in yellow.

PANEL 3 (both characters point together at the same figure; 藍子 realizing):
- Label tab: 「③　過半数でも直ちには請求できない」
- Left card, heading 「持分の過半数」, body 「直ちには請求できない」, with ONE red cross only (no check mark on this card).
- Right card, heading 「明渡しの請求」, body 「理由の主張・立証が必要」, with no mark on this card.
- A small navy tag under the cards reads 「現行の民法でも結論は同じ」.
- 藍子 bubble (left, spoken first): 「ＢとＣで過半数なのに、直ちには請求できないんですか？」.
- トリ先生 bubble (right, spoken as the answer): 「そう。明渡しを求めるには、理由の主張と立証が必要よ」 with the part 「理由の主張と立証」 highlighted in yellow.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「直ちに明渡しを請求できるという記述は、誤りなんですね！」.
- トリ先生 bubble (right, spoken as the answer): 「そう。Ａも使う権原を持つから、直ちには請求できないのよ」 with the part 「直ちには請求できない」 highlighted in yellow.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「Ａも持分に基づいて使う権原がある」, 「持分が過半数でも直ちには請求できない」, 「明渡しには理由の主張・立証が必要」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「単独で占有する共有者に、他の共有者は直ちには明渡請求できない」 with a yellow highlighter marker.
- Line 2: 「問題D0002　正解×（H17-Q01イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 占, 建, 張, 権, 渡, 物, 解, 記, 証, 請, 過 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0002_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の「持分は各3分の1」と、コマ3の「持分の過半数」（ＢとＣで3分の2）の関係が、コマ3のカードの見出しで分かる
- [ ] 工程C：構成表の全文言を記事（H17-Q01イ）と突き合わせ：「使用収益の権原」「当然には請求できない」「主張・立証」「現行の民法でも結論は同じ」
- [ ] 工程C：結論が×（直ちに請求できるという記述が誤り）であることが、コマ4のラベル・台詞・結論帯から読み取れる

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致
- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている
- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）
