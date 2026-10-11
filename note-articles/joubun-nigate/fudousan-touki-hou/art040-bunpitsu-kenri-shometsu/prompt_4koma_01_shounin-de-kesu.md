# D0026・D0597・D0599 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第40条の記事に差し込む4コマ（1本目）のプロンプトです。類似の誤解をまとめて、1本の4コマにしました。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`（mainブランチ））に従い、同フォルダの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-09）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0026・D0597・D0599（不動産登記法／土地の分筆・合筆・地積更正、出典 H17-Q06肢1／H22-Q18イ・エ）。正解＝D0026・D0597＝×（誤った記述）／D0599＝〇。
- 記事：`note-articles/h22-mondai/q18-bunpitsu.md` イ「仮登記権利者が消滅を承諾すれば、分筆後の土地に仮登記は転写されない」・エ「差押えの登記は、承諾があっても分筆の手続では抹消できない」。ほか、H17-Q06肢1（q06-bunpitsu-shinsei.md。仮差押えに債権者の承諾は不要）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【型の選び方】型：型4（複数肢の対比）＋型3（理由）。理由：3肢が同じ『分筆と承諾の情報』の事案から枝分かれし、仮差押え（承諾は要らない）・仮登記（承諾すれば転写されない）・差押え（承諾があっても消せない）で結論の向きが違う。読者は『どこで分かれるか』を自分で並べ直せないので、コマ1で3肢を並べ、コマ2で『原則（承諾は要らない）』と『消せる／消せない』の対比、コマ3で理由を示す。
- 【出題者のひっかけ】3肢とも『承諾』を前に出して、承諾の効き方を取り違えさせる。D0026は『承諾したことを証する情報を…提供しなければならない』と書いて、承諾が要るように見せる。D0597は『承諾…が提供されたときであっても…転写される』と書いて、承諾が効かないように見せる。D0599は同じ『…であっても…抹消することはできない』の形で、正しい記述なのに、承諾が効くと思う人には誤りに見える。
- 【受験者の勘違い・定着していない点】（推測）①分筆には権利者の承諾が要ると思う（実際は要らず、登記は分筆後の各土地に引き継がれる）。②承諾の情報を添えれば、どの登記も分筆の中で消せる（または、仮登記でも承諾があっても転写される）と、登記の種類を見ずに考える。③差押えを、抵当権や仮登記のような権利の登記と同じ扱いにする（差押えは処分の制限の登記で、法40条の対象にならないと整理される）。
- 【対比する制度】「権利の登記は、承諾の情報で消せる」⇔「差押えの登記は、承諾があっても消せない」：前者は抵当権・仮登記など（法40条。承諾に係る土地で権利が消える）／後者は処分の制限の登記で、法40条の対象にならないと整理される（結論が逆になる点）。その前提として、原則は『分筆に承諾は要らない』（仮差押えもそのまま引き継がれる）。
- コマごとに読者が言えること：コマ1＝3肢は、仮差押え・仮登記・差押えと登記が違い、どれも『承諾』を前に出している。コマ2＝原則は承諾が要らず、引き継がれる。承諾の情報で消せるのは権利の登記で、差押えは承諾があっても消せない。コマ3＝分筆は土地を分けるだけだから承諾は要らない。消せるのは権利そのもの。差押えは権利ではなく処分の制限。コマ4＝消せるのは権利の登記だけ。D0026・D0597は×、D0599は〇。
- 記事の範囲：法40条（権利の登記名義人が、権利を分筆後のいずれかの土地について消滅させることを承諾したことを証する情報を、分筆の申請情報と併せて提供したとき、承諾に係る土地について権利が消滅した旨を登記する）／規則102条1項（権利に関する登記は分筆後の土地に転写される）／仮差押えに承諾は不要で、分筆後の各土地に引き継がれる（記事 H17-Q06肢1）／仮登記は、権利の消滅を承諾した情報が提供されれば乙土地に転写されない（記事 H22-Q18イ）／差押えの登記は、承諾があっても分筆の手続では抹消できない（記事 H22-Q18エ。『処分の制限の登記は法40条の対象にならないと整理される』は条文に明記がなく、解釈・登記実務の取扱いと記事が書いている。図も断定せず、記事の言い方にそろえた）。
- 登場人物：当事者の記号は使わない。土地は『仮差押えの登記がある土地』などの文字ラベルで示す。
- 矢印の意味：矢印は使わない。コマ1は縦3枚のカード、コマ2は上の帯と下の左右のカード、コマ3は縦3枚のカード。
- 配色：コマ1〜3は印（✓✕）を付けない（消せる・消せないは文字で書く。肢の〇×と印の向きが重なって紛らわしくなるのを避ける）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（通常サイズのキャラが左右の端、図は中央に3枚のカードと疑問バッジ）、コマ2＝none（帯と左右のカードが主役）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 承諾の情報で消せるのは、権利の登記だけ | 「権利の登記だけ」を黄色マーカー |
| コマ1 見出し | ラベル | ①　3つの肢は、登記が違う | — |
| コマ1 図 | 図・カード | 分筆するとき、承諾の情報は効く？ / 肢D0026 / 仮差押えの登記がある土地 / 承諾の情報を提供しなければならない / 肢D0597 / 仮登記がある土地 / 承諾が提供されても、転写される / 肢D0599 / 差押えの登記がある土地 / 承諾が提供されても、抹消できない | — |
| コマ1 | 藍子（左・先に話す） | どれも、承諾すれば消せますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。登記の種類を見なさい | 「登記の種類」 |
| コマ2 見出し | ラベル | ②　原則と、承諾の効き方 | — |
| コマ2 図 | 図・カード | 原則：分筆に承諾は要らない / 登記は、分筆後の各土地に引き継がれる（規則102条1項） / 肢D0026は、この場面 / 権利の登記は、承諾の情報で消せる / 抵当権や仮登記など（法40条） / 承諾に係る土地では、権利が消える / 肢D0597は、この場面 / 差押えの登記は、承諾があっても消せない / 処分の制限の登記は、 / 法40条の対象にならないと整理される / 肢D0599は、この場面 | — |
| コマ3 見出し | ラベル | ③　なぜ、そう分かれる？ | — |
| コマ3 図 | 図・カード | 分筆に、承諾は要らない / 土地を分けるだけで、権利は変わらない / 登記は、分筆後の各土地に引き継がれる / 消せるのは、権利そのものの登記 / ひっかけ：承諾が提供されたときであっても / たとえば：仮登記権利者が乙土地の / 消滅を承諾すれば、転写されない / 差押えは、権利そのものの登記ではない / 差押えは処分の制限の登記で、 / 承諾があっても分筆では抹消できない | — |
| コマ3 | 藍子（左・1番目） | 承諾を提供しなければ、分筆できない？ | — |
| コマ3 | トリ先生（右・2番目） | いいえ。承諾は権利を消すときよ | 「権利を消すとき」 |
| コマ3 | 藍子（左・3番目） | 差押えも、承諾すれば消せますか？ | — |
| コマ3 | トリ先生（右・4番目） | 消せないわ。権利ではなく処分の制限よ | 「処分の制限」 |
| コマ4 見出し | ラベル | ④　結論は権利の登記だけ | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 消せるのは、権利の登記だけなんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。登記の種類で決まるのよ | 「登記の種類」 |
| コマ4 チェック欄 | 3項目（青✓） | 分筆に承諾は要らない。仮差押えの登記も、各土地に引き継がれる / 権利の登記は、承諾の情報で消せる。仮登記も転写されない（法40条） / 差押えの登記は、承諾があっても、分筆の手続では消せない | — |
| 結論帯 | 1行目 | 承諾の情報で消せるのは、権利の登記だけ | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0026・D0597・D0599　正解×・×・〇（H17-Q06肢1／H22-Q18イ・エ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法40条／不動産登記規則102条1項・104条2項（法令DB note-articles/laws/fudousan-touki-hou.md 第40条、fudousan-touki-kisoku-1.md 第102条・第104条で原文を確認）：コマ2の『分筆後の各土地に引き継がれる（規則102条1項）』『承諾に係る土地で権利が消える（法40条）』の根拠。規則102条1項は記事 H22-Q18 には出ないが、同じ第40条の記事（note_art040.md）に書かれている。
- 『仮差押え』を処分の制限の登記と分類する記述は、記事にないので図に入れない（仮差押えは『承諾は要らず、引き継がれる』とだけ書く）。『差押えは処分の制限の登記で、法40条の対象にならないと整理される』は、記事 H22-Q18エの言い方（条文に明記なし、解釈・登記実務）。

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

TITLE BANNER: text 「承諾の情報で消せるのは、権利の登記だけ」 in large bold letters; the part 「権利の登記だけ」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　3つの肢は、登記が違う」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: a small question badge 「分筆するとき、承諾の情報は効く？」 at the top (a question badge only, with no check mark and no cross), and under it three SEPARATE cards stacked from top to bottom, all exactly the same size, each with the same pale gray fill and a dark navy outline, with no check mark, no cross, and no arrow anywhere. The cards are separated only by a small empty gap, with nothing drawn between them.
- Each card has a small dark navy tag at its top left, one bold dark navy heading line, and one body line (each text at least 24 px high).
- Card 1: tag 「肢D0026」, heading 「仮差押えの登記がある土地」, body 「承諾の情報を提供しなければならない」.
- Card 2: tag 「肢D0597」, heading 「仮登記がある土地」, body 「承諾が提供されても、転写される」.
- Card 3: tag 「肢D0599」, heading 「差押えの登記がある土地」, body 「承諾が提供されても、抹消できない」.
- The three cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「どれも、承諾すれば
消せますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
登記の種類を
見なさい」 with the part 「登記の種類」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　原則と、承諾の効き方」
- One wide dark navy band across the top of the panel with white text in two lines: 「原則：分筆に承諾は要らない」 and 「登記は、分筆後の各土地に引き継がれる（規則102条1項）」, and a small pale gray tag with dark navy text 「肢D0026は、この場面」 at the right end of the band.
- Under the band, two cards of the same size side by side, left and right, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed fully INSIDE the card, with no check mark, no cross, and no arrow anywhere in this panel. Only a small empty gap separates the two cards, with nothing drawn between them.
- Left card: heading 「権利の登記は、承諾の情報で消せる」, two body lines 「抵当権や仮登記など（法40条）」 and 「承諾に係る土地では、権利が消える」, and a small dark navy tag 「肢D0597は、この場面」.
- Right card: heading 「差押えの登記は、承諾があっても消せない」, two body lines 「処分の制限の登記は、」 and 「法40条の対象にならないと整理される」, and a small dark navy tag 「肢D0599は、この場面」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、そう分かれる？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed INSIDE the card, with no check mark and no cross. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1, heading 「分筆に、承諾は要らない」, two body lines 「土地を分けるだけで、権利は変わらない」 and 「登記は、分筆後の各土地に引き継がれる」.
- Card 2, heading 「消せるのは、権利そのものの登記」, a dark navy ribbon tag with large white text 「ひっかけ：承諾が提供されたときであっても」, two body lines 「たとえば：仮登記権利者が乙土地の」 and 「消滅を承諾すれば、転写されない」.
- Card 3, heading 「差押えは、権利そのものの登記ではない」, two body lines 「差押えは処分の制限の登記で、」 and 「承諾があっても分筆では抹消できない」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「承諾を提供しなければ、
分筆できない？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「いいえ。
承諾は権利を
消すときよ」 with the part 「権利を消すとき」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「差押えも、
承諾すれば消せますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「消せないわ。
権利ではなく
処分の制限よ」 with the part 「処分の制限」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は権利の登記だけ」
- 藍子 bubble (left, spoken first): 「消せるのは、
権利の登記だけ
なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
登記の種類で
決まるのよ」 with the part 「登記の種類」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「分筆に承諾は要らない。仮差押えの登記も、各土地に引き継がれる」, 「権利の登記は、承諾の情報で消せる。仮登記も転写されない（法40条）」, 「差押えの登記は、承諾があっても、分筆の手続では消せない」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「承諾の情報で消せるのは、権利の登記だけ」 with a yellow highlighter marker.
- Line 2: 「問題D0026・D0597・D0599　正解×・×・〇（H17-Q06肢1／H22-Q18イ・エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 効, 地, 対, 当, 承, 抵, 押, 権, 登, 肢, 規, 解, 記, 諾, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the word 「原則」 is spelled exactly like this everywhere (never 「思則」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1, panel 2 and panel 3 contain no check mark and no cross anywhere, and that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the three cards of panel 1 are in the order 肢D0026 (仮差押え), 肢D0597 (仮登記), 肢D0599 (差押え), never swapped; confirm that the left card of panel 2 has the heading 「権利の登記は、承諾の情報で消せる」 with the tag 「肢D0597は、この場面」 and the right card has the heading 「差押えの登記は、承諾があっても消せない」 with the tag 「肢D0599は、この場面」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`4コマ1_承諾で消せるのは権利の登記だけ.png`
- 途中の版・不採用の版：`4コマ1_承諾で消せるのは権利の登記だけ_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0026-D0597-D0599_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で3肢が『仮差押え・仮登記・差押えの土地を分筆するとき、承諾の情報がどう効くか』を問うていると分かり、コマ2で『原則は承諾が要らない／権利の登記は承諾で消せる／差押えは承諾があっても消せない』が言える
- [ ] 工程C：肝の確認：①分筆に承諾は要らない（仮差押えも引き継がれる） ②権利の登記（仮登記など）は承諾の情報で消せる（法40条） ③差押えは承諾があっても分筆の手続では消せない ④D0026・D0597は×、D0599は〇
- [ ] 工程C：構成表の全文言を記事（H17-Q06肢1、H22-Q18イ・エ）と法令DBに突き合わせ：『承諾に係る土地で権利が消える』は法40条（承諾に係る土地について権利が消滅した旨を登記）の言い方。差押えの扱いは記事の『整理される』にそろえた
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（side→none→faces→既定）。結論は D0026・D0597＝×、D0599＝〇 を結論帯で示す

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

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-09 v01：初版（条文別『苦手克服』シリーズ（note-articles/joubun-nigate/）の第40条用。分筆で承諾の情報が効く登記の範囲を問う3肢を1本にまとめた。ChatGPTでの生成・検品はまだ）
- 2026-10-11 v02：最新の作成ルールで組み直し。①コマ1を3肢の比較（肢・登記・肢の言い分）にして、3肢の対応を明示 ②コマ2を『原則：承諾は要らない』の帯と、『消せる／消せない』の左右のカードに（仮差押えと差押えを同じ『承諾の対象にならない』に混ぜない） ③コマ3の✕✓の比較カードをやめ、理由のカード3枚（印なし）にして、コマ4の暗記3点だけ青✓ ④コマ1は通常サイズ（side）のまま、小さくしない
