# D0026 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D0026（不動産登記法／土地の分筆・合筆・地積更正、出典 H17-Q06肢1）。正解＝×（誤った記述）。誤解4回。
- 記事：`note-articles/h17-mondai/q06-bunpitsu-shinsei.md` 1「仮差押があっても、分筆に債権者の承諾は不要」
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の5枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 登場人物：Ａ（所有権の登記名義人）・Ｂ（仮差押債権者）をコマ1で紹介。登記官は人物ではなく「登記官」という文字ラベルの人型（コマ3）。
- 矢印の意味：コマ2の矢印は「分筆」という手続（物理的な区分）。コマ3の矢印は登記官による記録の引き継ぎ。取引の矢印はない。
- 会話順：藍子の誤解（承諾が要る）→分筆とは何か→仮差押えの行き先→結論（記述は×）。
- 配色：対比カードはなし。チェック欄は青。結論が×である旨はラベルと台詞の文字で示す。
- 記事の範囲：分筆は一筆を複数に区分する物理的な変更にすぎず権利内容を変更しない／仮差押えの効力は分筆後の各土地に当然に及ぶ／登記官が各土地の登記記録に引き継ぐ／承諾を証する情報は不要。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0026～H17-Q06肢1～

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 仮差押えがあっても、分筆に債権者の承諾は不要 | 「債権者の承諾は不要」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 図 | 図・カード | 仮差押え / Ａ / 分筆の申請 / Ｂ / 承諾は要る？ / Ａ（所有権の登記名義人）　Ｂ（仮差押債権者） | — |
| コマ1 | 藍子（左・先に話す） | 仮差押えがあるなら、Ｂの承諾が要りますよね？ | 「承諾が要りますよね？」 |
| コマ1 | トリ先生（右・答える） | 出たわね。承諾を証する情報が要ると思ったでしょ | — |
| コマ2 見出し | ラベル | ②　分筆とは | — |
| コマ2 図 | 図・カード | 一筆 / 仮差押え / 分筆 / 二筆 / 物理的に区分するだけ | — |
| コマ2 | 藍子（左・先に話す） | 分筆すると、仮差押えの内容まで変わるんですか？ | — |
| コマ2 | トリ先生（右・答える） | いいえ。一筆を複数に区分する物理的な変更にすぎないのよ | 「物理的な変更」 |
| コマ3 見出し | ラベル | ③　仮差押えの行き先 | — |
| コマ3 図 | 図・カード | 仮差押え / 登記官 / 各土地の登記記録に引き継ぐ | — |
| コマ3 | 藍子（左・先に話す） | 仮差押えは、分筆したらどうなるんですか？ | — |
| コマ3 | トリ先生（右・答える） | 分筆後の各土地に、当然に効力が及ぶのよ | 「当然に効力が及ぶ」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 債権者の承諾を証する情報は、提供しなくていいんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。承諾が必要という記述は×よ | 「承諾が必要という記述は×」 |
| コマ4 チェック欄 | 3項目（青✓） | 分筆は一筆を区分する物理的な変更 / 仮差押えは分筆後の各土地に及ぶ / 債権者の承諾を証する情報は不要 | — |
| 結論帯 | 1行目 | 仮差押えの効力は分筆後の各土地に及び、債権者の承諾は不要 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0026　正解×（H17-Q06肢1） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a navy business suit over a blouse with thin blue vertical stripes; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「仮差押えがあっても、分筆に債権者の承諾は不要」 in large bold letters; the part 「債権者の承諾は不要」 has a yellow highlighter marker.

PANEL 1 (藍子 confident, トリ先生 exasperated but caring):
- Label tab: 「①　よくある思い込み」
- Small diagram in the middle: a flat plot-of-land block drawn as one rectangle with a diagonal ribbon labeled 「仮差押え」 across it. A faceless pictogram with tag 「Ａ」 stands at the left of the plot holding a small document labeled 「分筆の申請」. A faceless pictogram with tag 「Ｂ」 stands at the right with a small question badge 「承諾は要る？」 (a question badge only, with no check mark and no cross). Caption under the diagram: 「Ａ（所有権の登記名義人）　Ｂ（仮差押債権者）」.
- 藍子 bubble (left, spoken first): 「仮差押えがあるなら、Ｂの承諾が要りますよね？」 with the part 「承諾が要りますよね？」 highlighted in yellow.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。承諾を証する情報が要ると思ったでしょ」.

PANEL 2 (藍子 puzzled, トリ先生 explaining with a wing-pointer):
- Label tab: 「②　分筆とは」
- On the left, one plot-of-land block labeled 「一筆」 with the diagonal ribbon 「仮差押え」. A navy arrow (this arrow means the procedure of dividing the land, not a sale) labeled 「分筆」 points to the right, where two plain plot blocks without ribbons are drawn side by side and labeled 「二筆」.
- Under the arrow, a dark navy tag reads 「物理的に区分するだけ」.
- 藍子 bubble (left, spoken first): 「分筆すると、仮差押えの内容まで変わるんですか？」.
- トリ先生 bubble (right, spoken as the answer): 「いいえ。一筆を複数に区分する物理的な変更にすぎないのよ」 with the part 「物理的な変更」 highlighted in yellow.

PANEL 3 (both characters point together at the same figure; 藍子 realizing):
- Label tab: 「③　仮差押えの行き先」
- Two plot-of-land blocks side by side, each carrying its own diagonal ribbon 「仮差押え」.
- A faceless clerk pictogram labeled 「登記官」 stands above them, with a navy arrow to both blocks labeled 「各土地の登記記録に引き継ぐ」.
- 藍子 bubble (left, spoken first): 「仮差押えは、分筆したらどうなるんですか？」.
- トリ先生 bubble (right, spoken as the answer): 「分筆後の各土地に、当然に効力が及ぶのよ」 with the part 「当然に効力が及ぶ」 highlighted in yellow.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「債権者の承諾を証する情報は、提供しなくていいんですね！」.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。承諾が必要という記述は×よ」 with the part 「承諾が必要という記述は×」 highlighted in yellow.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「分筆は一筆を区分する物理的な変更」, 「仮差押えは分筆後の各土地に及ぶ」, 「債権者の承諾を証する情報は不要」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「仮差押えの効力は分筆後の各土地に及び、債権者の承諾は不要」 with a yellow highlighter marker.
- Line 2: 「問題D0026　正解×（H17-Q06肢1）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 債, 効, 地, 当, 所, 承, 押, 権, 物, 登, 肢, 解, 記, 証, 請, 諾, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0026_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：「仮差押え」のリボンがコマ2では分筆前の土地にだけ付き、コマ3で分筆後の2筆の両方に付くことが、ラベルで説明されている
- [ ] 工程C：構成表の全文言を記事（H17-Q06肢1）と突き合わせ：「物理的な変更」「当然に及ぶ」「登記官によって引き継がれる」
- [ ] 工程C：結論が×（承諾が必要という記述が誤り）であることが、コマ4のラベル・台詞・結論帯から読み取れる

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致
- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている
- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）
