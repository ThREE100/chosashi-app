# D0443・D0441 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②不動産登記法編 第4章「土地の分筆・合筆・地積更正」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md`）の、論点【PD-11】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PD-11_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0443・D0441（不動産登記法／土地の分筆・合筆・地積更正、出典 H21-Q07ウ／H21-Q07ア）。正解＝D0443＝×（誤った記述）／D0441＝〇（正しい記述）。
- 記事：`note-articles/h21-mondai/q07-chiseki-kousei.md` ウ（地積更正は表示に関する登記であり、判決を得て代位申請する方法によることはできない）。ほか、ア（土地の一部の所有権を取得した者は、所有権を証する情報を提供して代位し、地積の更正と分筆を申請できる）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D0443は『利害関係人』が『更正の登記手続を命ずる判決を得て』代位する、と書く。判決を得れば権利の登記で単独申請や代位ができるのと同じ流れに見せ、表示の登記でも通ると思わせる。D0441は『土地の一部について所有権を取得した者』と『所有権を証する情報を提供して』と、代位できる者と根拠を具体的に書く。判決の肢と並ぶと、どちらも『代位』なので同じ扱いに見える。
- 【受験者の勘違い・定着していない点】（推測）①表示の登記でも、判決を得れば権利の登記と同じように代位して申請できると考える（D0443）。②利害関係人であれば誰でも代位できると考える。③土地の一部の所有権を取得した者が代位できるのは、自らの所有権という実体的な権利に基づくからだという区別が結びついていない（D0441）。
- 【対比する制度】「判決を得ての代位」⇔「一部の所有権取得者の代位」：判決を得て代位して地積の更正を申請する方法は認められない（表示の登記は、判決で共同申請を代わりに行う仕組みになじまない）／土地の一部の所有権を取得した者は、所有権を証する情報を提供して代位し、地積の更正と分筆を申請できる（自らの所有権という実体的な権利に基づく代位）（結論が逆になる点）。
- 【型の選び方】型：型3（理由説明）＋型4の2肢の対比。理由：結論（判決は不可、一部の所有権取得者は可）だけ覚えても、『判決があればできるはず』という感覚が残ると崩れる。なぜそうなるか（表示の登記は判決による共同申請の仕組みになじまない／実体的な権利に基づく代位）を、コマ3の左の3枚のカード（印なし）に置いた。コマ2は2つの代位の左右の対比。壁＝『表示の登記を権利の登記と同じに扱う思い込み』。
- コマごとに読者が言えること：コマ1＝地積の更正を代位して申請できるかを問う2つの肢（判決を得た利害関係人／土地の一部の所有権取得者）。コマ2＝判決を得ての代位は認められず、一部の所有権取得者の代位は認められる。コマ3＝理由（表示の登記は判決による共同申請になじまない／実体的な権利に基づく代位）と、名義人が動かないときの実務（登記官に更正を促す）。コマ4＝D0443は×、D0441は〇。
- 記事の範囲：H21-Q07ウ（地積の更正は表示に関する登記で、判決による代位申請は認められない。名義人が協力しないときは、実測図などを添えて登記所に情報提供し、登記官自身に調査のうえ更正をしてもらう）、H21-Q07ア（土地の一部の所有権を取得した者は、当該部分の所有権を証する情報を提供して代位し、地積の更正と当該部分の分筆を申請できる。実体的な権利に基づく代位）。
- 登場人物：人型は使わず、申請する者は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は縦2枚のカード、コマ2は左右のカード、コマ3は左の縦3枚のカードと右の会話。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side、コマ2＝none（図が主役）、コマ3＝faces（左に縦3枚のカード、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 地積更正は、判決では代位できない | 「判決では代位できない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　判決があれば、代位できる？ | — |
| コマ1 図 | 図・カード | D0443 / 地積に誤りがある土地の利害関係人 / 更正を命ずる判決を得て、代位できる？ / D0441 / 土地の一部の所有権を取得した者 / 所有権を証する情報で、代位できる？ / 代位して、地積の更正を申請できる？ | — |
| コマ1 | 藍子（左・先に話す） | 判決があれば、代位できますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。権利の登記と混ぜてるわよ | 「権利の登記と混ぜてる」 |
| コマ2 見出し | ラベル | ②　判決と一部の所有権取得者 | — |
| コマ2 図 | 図・カード | 地積の更正の代位申請 / 何に基づく代位か、で結論が変わる / 判決を得ての代位 / 認められない / 表示の登記になじまない / 一部の所有権取得者の代位 / 認められる / 自らの所有権に基づく | — |
| コマ3 見出し | ラベル | ③　なぜ、そう分かれる？ | — |
| コマ3 図 | 図・カード | 判決による代位が認められない理由 / 表示の登記は、判決で共同申請を代わりに行う仕組みになじまない / 一部の所有権取得者が代位できる理由 / 自らの所有権という実体的な権利に基づく代位 / 名義人が動かないとき / 実測図などを添えて登記所に伝え、更正を促す | — |
| コマ3 | 藍子（左・1番目） | では、名義人が動かないときは？ | — |
| コマ3 | トリ先生（右・2番目） | 資料を添えて、登記所に伝えるのよ | 「登記所に伝える」 |
| コマ3 | 藍子（左・3番目） | 登記官が調べてくれるんですか？ | — |
| コマ3 | トリ先生（右・4番目） | ええ。登記官が自ら更正できるの | 「登記官が自ら」 |
| コマ4 見出し | ラベル | ④　結論は×と〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 判決ではなく、実体の所有権なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。判決は使えないのよ | 「判決は使えない」 |
| コマ4 チェック欄 | 3項目（青✓） | 地積の更正を、判決を得て代位して申請する方法は認められない（肢D0443は×） / 土地の一部の所有権を取得した者は、所有権を証する情報で代位し、更正と分筆を申請できる（肢D0441は〇） / 名義人が動かないときは、実測図などを添えて登記所に伝え、登記官の調査による更正を促す | — |
| 結論帯 | 1行目 | 判決では代位できない。一部の所有権取得者ならできる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0443・D0441　正解×・〇（H21-Q07ウ／H21-Q07ア） | — |

## 記事に無い条文（ユーザー指示で追加）

- この4コマの図は、肢の記事（H21-Q07ウ・ア）の範囲だけで作った。条番号は載せていない（総合記事②第4章【PD-11】が引く不動産登記法38条・民法423条・不動産登記令3条4号は図に入れない）

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed (cartoon expression marks such as ！ and ？ beside a character's face are decoration, not text, and are allowed).

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below.

CHARACTER SIZE POLICY: draw 藍子 and トリ先生 as large and as clear as the layout allows, at the size given in each PANEL line. Never shrink a character just to make it small or to leave empty space, and never draw a character at the smallest possible size by default (this happens most often in panel 1). Reduce a character's size ONLY when the diagram, the cards, or the speech bubbles of that panel genuinely do not fit otherwise, and then reduce it only as much as needed, keeping the face large enough to read the expression. Characters become icon-sized only in a panel whose PANEL line explicitly asks for face icons.

EXPRESSION MARKS (allowed): small cartoon expression marks and effects around the characters, such as ！, ？, sweat drops, sparkles, anger marks, hearts, surprise lines, and thought dots, may appear whenever they match a character's emotion, in any soft color (these marks are exempt from the color rule for YES/NO marks). They are decoration: they are not part of the given text and not part of the YES/NO mark system, so they are NEVER counted as extra text, extra marks, or errors, and nothing is deleted, redrawn, or regenerated because of them. They must stay small, must not cover any given text or diagram, and must not be drawn as a check mark or a cross on a card.

SINGLE PASS: generate the image once. The checklists in this prompt, including the final check at the end, are guides to apply silently while drawing. After the image is produced, do not audit it again, do not list or announce defects (for example an extra or unexpected mark or symbol), and do not delete, redo, or regenerate any part of it; deliver the first image as it is.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both smaller than normal; in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「地積更正は、判決では代位できない」 in large bold letters; the part 「判決では代位できない」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　判決があれば、代位できる？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: two SEPARATE cards stacked from top to bottom, both the same size, each with the same pale gray fill, a dark navy outline, a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers), and two short dark navy text lines. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1 with a small gray tag 「D0443」: 「地積に誤りがある土地の利害関係人」 and 「更正を命ずる判決を得て、代位できる？」. Card 2 with a small gray tag 「D0441」: 「土地の一部の所有権を取得した者」 and 「所有権を証する情報で、代位できる？」.
- At the top, a small question badge in a gray fill with dark navy text 「代位して、地積の更正を申請できる？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「判決があれば、
代位できますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
権利の登記と
混ぜてるわよ」 with the part 「権利の登記と混ぜてる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　判決と一部の所有権取得者」
- A small dark navy tag 「地積の更正の代位申請」 at the top left, with one line beside it: 「何に基づく代位か、で結論が変わる」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「判決を得ての代位」, two body lines: 「認められない」, 「表示の登記になじまない」.
- Right card, heading 「一部の所有権取得者の代位」, two body lines: 「認められる」, 「自らの所有権に基づく」, with the text 「認められる」 highlighted with a yellow marker.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、そう分かれる？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- LEFT SIDE: three stacked reason cards of the same size, from top to bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card and one or two short body lines, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Card 1, heading 「判決による代位が認められない理由」, body 「表示の登記は、判決で共同申請を代わりに行う仕組みになじまない」.
- Card 2, heading 「一部の所有権取得者が代位できる理由」, body 「自らの所有権という実体的な権利に基づく代位」.
- Card 3, heading 「名義人が動かないとき」, body 「実測図などを添えて登記所に伝え、更正を促す」.
- The three cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、名義人が
動かないときは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「資料を添えて、
登記所に
伝えるのよ」 with the part 「登記所に伝える」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「登記官が調べて
くれるんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「ええ。登記官が
自ら更正できるの」 with the part 「登記官が自ら」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×と〇」
- 藍子 bubble (left, spoken first): 「判決ではなく、
実体の所有権
なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
判決は使えない
のよ」 with the part 「判決は使えない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「地積の更正を、判決を得て代位して申請する方法は認められない（肢D0443は×）」, 「土地の一部の所有権を取得した者は、所有権を証する情報で代位し、更正と分筆を申請できる（肢D0441は〇）」, 「名義人が動かないときは、実測図などを添えて登記所に伝え、登記官の調査による更正を促す」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「判決では代位できない。一部の所有権取得者ならできる」 with a yellow highlighter marker.
- Line 2: 「問題D0443・D0441　正解×・〇（H21-Q07ウ／H21-Q07ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 地, 所, 権, 登, 肢, 解, 記, 証, 認, 請 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編4章_4コマ7_地積更正は、判決では代位できない.png`
- 途中の版・不採用の版：`不動産登記法編4章_4コマ7_地積更正は、判決では代位できない_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch4/prompt_4koma_PD-11_01_daii-hanketsu.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で2つの肢の問い、コマ2で判決を得ての代位と一部の所有権取得者の代位の対比、コマ3でその理由と名義人が動かないときの実務、が言える
- [ ] 工程C：構成表の全文言を記事（H21-Q07ウ・ア）と突き合わせ済み。条番号は図に入れていない
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①地積の更正は表示に関する登記で、判決を得ての代位は認められない②土地の一部の所有権取得者は、所有権を証する情報を提供して代位し、地積の更正と分筆を申請できる③名義人が動かないときは、登記官の調査による更正を促す④肢D0443は×、D0441は〇

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致
- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている
- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）
- [ ] 顔アイコン・小さなキャラが指定の大きさ。キャラなしのコマにキャラ・吹き出しがない
- [ ] 図の部品（人物・バー・領域・タグ）の色が指定どおり（意味のない青・赤・緑・ピンクがない）。人物の頭の上に余計な印がない
- [ ] 台詞の綴りが一字一句正本どおり（特に「原則」「まとめて」など崩れやすい語）

## 改訂履歴（このファイルは `src/spec_4koma_PD-11_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第4章【PD-11】用。型3の理由説明＋型4の2肢の対比。判決を得ての代位と一部の所有権取得者の代位の対比に絞った。D1939〔変更と更正の期限〕は別の4コマ）
