# D0642・D0643 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第3章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch3.md`）の、論点【PC-5】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PC-05_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0642・D0643（不動産登記法／土地の表題・地目・地積、出典 H23-Q07イ・ウ）。正解＝D0642＝〇（正しい記述）／D0643＝〇（正しい記述）。
- 記事：`note-articles/h23-mondai/q07-chiban.md` イ（H23：要役地についてする地役権の登記がある土地で地番に支号がないものを分筆するとき、地役権を分筆後のいずれかの土地について消滅させることを証する地役権者作成の情報が提供され、その土地の地役権を抹消するときは、分筆した土地について支号を用いない地番を存することができる。不動産登記事務取扱手続準則67条1項5号、不動産登記規則104条6項。どの土地に残すかは定めがない）・ウ（特別の事情があるときは、合筆前の首位の地番をもってその地番としなくても差し支えない。準則67条1項7号。原則は同6号）。章の記事 note-articles/column/sokatsu-02-fudousan-touki-hou-ch3.md 【PC-5】
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D0642は『要役地についてする地役権の登記がある土地で地番に支号がないもの』『当該地役権を分筆後のいずれかの土地について消滅させる』『支号を用いない地番を存する』と、長い前提を重ねる。分筆は支号を付けるものと覚えた受験者に、『支号を用いない』という結論が目に入った時点で×と読ませる。D0643は『特別の事情がある場合には』『合筆前の首位の地番をもってその地番としなくとも差し支えない』と書き、『合筆は首位の地番』という原則を知っている受験者に、例外を認める言い回しを誤りと見せる。
- 【受験者の勘違い・定着していない点】（推測）①分筆は『分筆前の地番に支号を付ける』、合筆は『合筆前の首位の地番とする』を、例外のない決まりと覚えている。例外は、分筆では規則104条6項の場面（準則67条1項5号）、合筆では特別の事情があるとき（同7号）に限られて認められることが定着していない。②地役権を消す分筆で、支号なしの地番をどの土地に残すかまで決まっていると思い込む（準則67条1項5号は定めていない）。
- 【対比する制度】「分筆の地番」⇔「合筆の地番」：分筆した土地は分筆前の地番に支号を付けて各筆の地番を定めるのが原則（準則67条1項4号）で、要役地の地役権を分筆後のいずれかの土地について消滅させるときは、支号を用いない地番を存することができる（同5号）／合筆した土地は合筆前の首位の地番とするのが原則（同6号）で、特別の事情があるときは、適宜の地番を定めて差し支えない（同7号）。どちらも原則と例外の2段で、原則だけ覚えると肢の結論が逆（〇を×）になる点。
- 【型の選び方】型：型4（複数肢の対比。コマ3の右に型5の整理カードを併用）。理由：2つの肢は共通の日付のない別々の場面（分筆と合筆）なので、時系列にはせず、コマ1は肢ごとのカード2枚（肢D0642・肢D0643）、コマ2は『分筆の地番』と『合筆の地番』の左右の対比カード（原則と例外を各カードに書く）、コマ3は両肢を『言い分』として並べ、右に『例外が使える場面』の整理カードを置いた。壁＝『原則だけを覚えていて、例外が肢で出ると×に見える』。既存の同章の4コマ（PC-4＝small→none→faces→既定の表と対比）と同じ型だが、コマ1を side（カード2枚を縦に並べる）にして見せ方を変えた。型1にしなかったのは、2肢とも〇で、ひっかけが『藍子の思い込み1つ』ではなく『分筆と合筆の両方に例外がある』ことだから。
- コマごとに読者が言えること：コマ1＝2つの肢（要役地の地役権を消す分筆／特別の事情がある合筆）が、原則に反するように見える言い分を書いている。コマ2＝分筆は支号が原則で地役権を消すなら支号なしも可、合筆は首位の地番が原則で特別の事情があれば適宜の地番も可。コマ3＝どちらの言い分も〇。地役権の例外を使える場面と、どの土地に支号なしを残すかは準則が定めていないこと。コマ4＝D0642は〇、D0643は〇。
- 記事の範囲：H23-Q07イ・ウ（準則67条1項4号〜7号、規則104条6項）。章の記事【PC-5】の中身の整理（分筆の原則と地役権の例外、合筆の原則と特別の事情）。合筆の制限（法41条）は、既存の4コマ（D0940）と図解8の範囲なので、この本には入れない。
- extra_refs：不動産登記事務取扱手続準則67条1項4号（『分筆した土地については、分筆前の地番に支号を付して各筆の地番を定める。ただし、本番に支号のある土地を分筆する場合には、その１筆には、従来の地番を存し、他の各筆には、本番の最終の支号を追い順次支号を付してその地番を定める』）・5号（『前号本文の規定にかかわらず、規則第１０４条第６項に規定する場合には、分筆した土地について支号を用いない地番を存することができる』）・6号（『合筆した土地については、合筆前の首位の地番をもってその地番とする』）・7号（『特別の事情があるときは、第３号、第４号及び第６号の規定にかかわらず、適宜の地番を定めて差し支えない』）は、法令DB note-articles/laws/fudousan-touki-jimu-junsoku.md の第67条で原文を確認。不動産登記規則104条6項（要役地についてする地役権の登記がある土地の分筆で、地役権者が作成した情報が提供されたとき、当該地役権が消滅した旨を登記）は note-articles/laws/fudousan-touki-kisoku-1.md の第百四条で原文を確認。
- 同じ論点の他の肢（図には肢として載せない）：D0940（接続する甲土地を乙土地に合筆する登記は申請できない。甲は宅地、乙は山林で地目が違う・〇。法41条2号）は既存の4コマ（tools/drill/manga/D0940_prompt.md）があるため、この本では扱わない。7号の特別の事情は準則では3号・4号・6号にかかる（分筆にも表題登記にも及ぶ）ので、図は『肢が問う場面』（合筆）に絞って書き、分筆では特別の事情が使えないとは書いていない。
- 登場人物：人型は使わず、肢・土地・条文の号は文字のカードで示す。事例の当事者は出さない。
- 矢印の意味：矢印は使わない。コマ1は縦2枚のカード、コマ2は左右のカード、コマ3は上下2枚のカードと右の整理カード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は2枚とも正しい言い分なので、青✓を1個ずつ（✕は使わない。2肢とも〇）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（通常サイズのキャラが左右の端、図は中央にカード2枚）、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 分筆は支号、合筆は首位。でも例外あり | 「例外あり」を黄色マーカー |
| コマ1 見出し | ラベル | ①　2つの肢を並べる | — |
| コマ1 図 | 図・カード | 分筆と合筆に、例外はある？ / 肢D0642 / 要役地の地役権を消す分筆 / 支号なしの地番を残せる / 肢D0643 / 特別の事情がある合筆 / 首位の地番でなくてよい | — |
| コマ1 | 藍子（左・先に話す） | 分筆は支号、合筆は首位。例外はないですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。準則が例外を認めているのよ | 「例外を認めている」 |
| コマ2 見出し | ラベル | ②　分筆の地番と、合筆の地番 | — |
| コマ2 図 | 図・カード | 地番の定め方 / どちらも、原則と例外の2段 / 分筆の地番 / 準則67条1項4号・5号 / 原則：分筆前の地番に支号を付ける / 例外：要役地の地役権を消すとき / 支号なしの地番を残せる / 合筆の地番 / 準則67条1項6号・7号 / 原則：合筆前の首位の地番 / 例外：特別の事情があるとき / 適宜の地番を定めて差し支えない | — |
| コマ3 見出し | ラベル | ③　例外が使える場面 | — |
| コマ3 図 | 図・カード | 肢D0642の言い分 / 地役権を消す分筆は、支号なしも可 / 肢D0643の言い分 / 特別の事情があれば、首位でなくてよい / 例外が使える場面 / 分筆：要役地の地役権を消す / 地役権者が作った情報を提供 / どの土地に残すかは定めなし / 合筆：特別の事情がある / 首位の地番によらなくてよい / ひっかけ：例外はない、と決めつける / 例外はない | — |
| コマ3 | 藍子（左・1番目） | 支号なしの地番は、どの土地に残るの？ | — |
| コマ3 | トリ先生（右・2番目） | 準則は定めていないわ。選べるの | 「定めていない」 |
| コマ4 見出し | ラベル | ④　結論は〇・〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 原則と例外を、セットで覚えるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。肢の言い分は、どちらも〇よ | 「どちらも〇」 |
| コマ4 チェック欄 | 3項目（青✓） | 分筆の原則は支号。要役地の地役権を消すなら、支号なしを残せる（肢D0642は〇） / 合筆の原則は首位の地番。特別の事情があれば、適宜の地番でよい（肢D0643は〇） / 支号なしの地番を、どの土地に残すかは定めがない | — |
| 結論帯 | 1行目 | 分筆は支号、合筆は首位。でも例外あり | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0642・D0643　正解〇・〇（H23-Q07イ・ウ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記事務取扱手続準則67条1項4号〜7号。法令DB note-articles/laws/fudousan-touki-jimu-junsoku.md の第67条で原文と照合済み。不動産登記規則104条6項は note-articles/laws/fudousan-touki-kisoku-1.md の第百四条で原文と照合済み。『どの土地に残すかの定めがない』は記事H23-Q07イの言い方にそろえた（図には『準則は定めていない』と書いた）

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

TITLE BANNER: text 「分筆は支号、合筆は首位。でも例外あり」 in large bold letters; the part 「例外あり」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　2つの肢を並べる」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: a small question badge 「分筆と合筆に、例外はある？」 at the top (a question badge only, with no check mark and no cross), and under it two SEPARATE cards stacked from top to bottom, both exactly the same size, each with the same pale gray fill and a dark navy outline, with no check mark, no cross, and no arrow anywhere. The two cards are separated only by a small empty gap, with nothing drawn between them.
- Each card has a small dark navy tag at its top left, one bold dark navy heading line, and one body line (each text at least 24 px high).
- Card 1: tag 「肢D0642」, heading 「要役地の地役権を消す分筆」, body 「支号なしの地番を残せる」.
- Card 2: tag 「肢D0643」, heading 「特別の事情がある合筆」, body 「首位の地番でなくてよい」.
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「分筆は支号、
合筆は首位。
例外はないですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
準則が
例外を認めているのよ」 with the part 「例外を認めている」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　分筆の地番と、合筆の地番」
- A small dark navy tag 「地番の定め方」 at the top left, with one line beside it: 「どちらも、原則と例外の2段」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「分筆の地番」, a small tag 「準則67条1項4号・5号」, three body lines: 「原則：分筆前の地番に支号を付ける」, 「例外：要役地の地役権を消すとき」, 「支号なしの地番を残せる」.
- Right card, heading 「合筆の地番」, a small tag 「準則67条1項6号・7号」, three body lines: 「原則：合筆前の首位の地番」, 「例外：特別の事情があるとき」, 「適宜の地番を定めて差し支えない」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　例外が使える場面」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「肢D0642の言い分」, body 「地役権を消す分筆は、支号なしも可」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- Bottom card, heading 「肢D0643の言い分」, body 「特別の事情があれば、首位でなくてよい」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「例外が使える場面」, with the same pale gray fill and a dark navy outline, containing exactly five short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「分筆：要役地の地役権を消す」, 「地役権者が作った情報を提供」, 「どの土地に残すかは定めなし」, 「合筆：特別の事情がある」, 「首位の地番によらなくてよい」, with the fifth row highlighted with a yellow marker. Under the five rows, one small dark navy ribbon tag with white text 「ひっかけ：例外はない、と決めつける」, with the text 「例外はない」 highlighted with a yellow marker.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「支号なしの地番は、
どの土地に残るの？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「準則は
定めていないわ。
選べるの」 with the part 「定めていない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇・〇」
- 藍子 bubble (left, spoken first): 「原則と例外を、
セットで覚える
んですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
肢の言い分は、
どちらも〇よ」 with the part 「どちらも〇」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「分筆の原則は支号。要役地の地役権を消すなら、支号なしを残せる（肢D0642は〇）」, 「合筆の原則は首位の地番。特別の事情があれば、適宜の地番でよい（肢D0643は〇）」, 「支号なしの地番を、どの土地に残すかは定めがない」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「分筆は支号、合筆は首位。でも例外あり」 with a yellow highlighter marker.
- Line 2: 「問題D0642・D0643　正解〇・〇（H23-Q07イ・ウ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 権, 番, 肢, 解, 認 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the word 「原則」 is spelled exactly like this everywhere (never 「思則」); confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不登法第3章_4コマ5_分筆は支号、合筆は首位。でも例外あり.png`
- 途中の版・不採用の版：`不登法第3章_4コマ5_分筆は支号、合筆は首位。でも例外あり_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch3/prompt_4koma_PC-05_01_chiban-genritsu-reigai.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で2つの肢の言い分（支号なしの地番／首位でない地番）が言え、コマ2で分筆と合筆の原則と例外、コマ3で地役権の例外が使える場面とどの土地に残すかの定めがないことが言える
- [ ] 工程C：構成表の全文言を記事（H23-Q07イ・ウ）・法令DB（準則67条1項4号〜7号、規則104条6項）に突き合わせ済み。合筆の制限・D0940は、この本の範囲外
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は青✓1個ずつ（2肢とも〇）、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①分筆の原則は分筆前の地番に支号を付ける（準則67条1項4号） ②要役地の地役権を分筆後のいずれかの土地について消滅させるときは、支号を用いない地番を存することができる（同5号。どの土地に残すかは定めがない） ③合筆の原則は合筆前の首位の地番（同6号）、特別の事情があれば適宜の地番（同7号） ④D0642は〇、D0643は〇

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

## 改訂履歴（このファイルは `src/spec_4koma_PC-05_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第3章【PC-5】用。型4（複数肢の対比。＋型5の整理カード）。D0940には既存の4コマがあるため、地番の付け方の2肢に絞った。2肢の言い分、分筆の地番と合筆の地番の原則と例外の対比、例外が使える場面の整理カードを組んだ）
