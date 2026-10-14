# D0348 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②不動産登記法編 第4章「土地の分筆・合筆・地積更正」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md`）の、論点【PD-5】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PD-05_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0348（不動産登記法／土地の分筆・合筆・地積更正、出典 H20-Q08ア）。正解＝D0348＝〇（正しい記述）。
- 記事：`note-articles/h20-mondai/q08-bungappitsu.md` ア（H20：甲土地に要役地についてする地役権の登記がある場合に、乙土地に合筆しようとする部分について地役権を消滅させることを証する地役権者の作成した情報を提供して、本件分合筆の登記を申請できる。分筆の登記の申請情報と併せて権利を消滅させる情報が提供されたときは、合筆する部分の地役権を消滅させれば法41条6号の障害がなくなる）。記事の導入部（法41条6号と規則105条の例外は承役地の地役権の登記など）。章の記事 note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md 【PD-5】
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢は『要役地についてする地役権の登記がある場合』と、権利の登記が付いた土地であることを先に見せ、『…消滅させることを証する地役権者の作成した情報を提供して』と、地役権者の作成した情報という具体的な書類まで書いて、本当にそれで足りるのかと迷わせる。問題の前提の『各記述中の条件のほかに合筆の登記を妨げる要件はない』は、合筆の制限のうち地役権だけを判断させるための文。
- 【受験者の勘違い・定着していない点】（推測）①地役権も所有権以外の権利の登記なので、あれば合筆できない（法41条6号）と一括りにして、消して合筆する手があることに結びつかない。②合筆の例外（規則105条）は『承役地についてする地役権の登記』であり、要役地についてする地役権の登記は入っていないことが定着していない。例外が地役権だと覚えていると、要役地も消さずに合筆できると考えて迷う。③消すための情報は、分筆の登記の申請情報と併せて出す地役権者の作成した情報だと結びつかない。
- 【対比する制度】「承役地の地役権」⇔「要役地の地役権」：承役地についてする地役権の登記は、規則105条1号の例外に当たるので、あっても合筆の障害にならない（消す必要がない）／要役地についてする地役権の登記は例外にないので合筆の障害になるが、合筆する部分の地役権を消滅させる情報を分筆の申請情報と併せて出せば、障害が外れる（規則104条6項）（扱いが分かれる点）。
- 【型の選び方】型：型3（理由説明）＋型1の対比（承役地⇔要役地）。理由：壁は、要役地の地役権は例外にないのに、なぜ合筆できる肢が〇になるのかが結びつかないこと。結論（〇）だけ覚えても、『合筆の例外は承役地』『要役地は消してから』が混ざると崩れるので、コマ2に承役地と要役地の左右の対比、コマ3に『消す情報を出す→合筆する部分の地役権が消える→障害が外れる』の理由の3枚を置いた。既存の4コマ（D0597・D0599／D0646・D0743／D0957・D0600）は型4（複数肢の対比）＋型3で、この肢は単独の肢なので型4にせず、型3の流れにした。
- コマごとに読者が言えること：コマ1＝要役地の地役権の登記がある甲土地の一部を分筆して乙土地に合筆するとき、地役権を消す情報を添えて申請できるかを問う肢。コマ2＝法41条6号が権利の登記のある土地の合筆を止め、承役地の地役権は例外（規則105条1号）で消さなくてよいが、要役地の地役権は例外にないので消さないと合筆できない。コマ3＝分筆の申請情報と併せて地役権を消滅させる情報を出すと、合筆する部分に地役権が残らず障害が外れる。出すのは地役権者の作成した情報。コマ4＝D0348は〇。
- 記事の範囲：H20-Q08ア（分筆の申請情報と併せて権利を消滅させる情報が提供されたとき、登記官は消滅した旨を登記する。この方法で合筆する部分の地役権を消滅させれば法41条6号の障害がなくなる）。記事の導入部（法41条6号、規則105条が定める例外には承役地についてする地役権の登記がある）。記事は消滅の根拠に法40条を引いているが、要役地の地役権を消す場合の情報（地役権者の作成した情報）を直接定めているのは規則104条6項なので、図には規則104条6項を載せた（法40条は『権利の登記名義人の承諾を証する情報』、規則104条6項は『要役地についてする地役権の登記がある土地』の別の規定。法令DBで確認）。
- extra_refs：不動産登記規則104条6項（法令DB note-articles/laws/fudousan-touki-kisoku-1.md 第百四条第6項：登記官は、要役地についてする地役権の登記がある土地について分筆の登記をする場合において、当該分筆の登記の申請情報と併せて当該地役権を分筆後のいずれかの土地について消滅させることを証する地役権者が作成した情報が提供されたときは、当該土地について当該地役権が消滅した旨を登記しなければならない）。規則105条1号（同第百五条：法41条6号の合筆後の土地の登記記録に登記することができる権利に関する登記は、1号 承役地についてする地役権の登記、2号 担保権の登記であって…が同一のもの、3号 信託の登記…、4号 鉱害賠償登録…）。法41条6号（同 fudousan-touki-hou.md 第41条：所有権の登記以外の権利に関する登記がある土地〔…法務省令で定めるものがある土地を除く〕の合筆の登記はすることができない）。記事に規則104条6項は書かれていないが、同じ章の記事の【PD-5】（中身の整理の最後の箇条）に規則104条6項が引かれている。
- 同じ論点の他の肢（図に入れない理由）：D0743（要役地の地役権を消す分筆で、土地に抵当権があれば抵当権者の承諾情報も要る・〇）は同じ規則104条6項の括弧書の話で、既存の4コマ（D0646・D0743）がある。この肢の図には、第三者の承諾は入れない（消す側の情報だけに絞る）。D0597・D0599・D0957・D0600・D0646にも既存の4コマがあり、今回は扱わない。同じ問のイ（敷地権・規約）、ウ（地目変更）、エ（敷地権の対象の土地どうし）、オ（期間経過の地上権）は別の論点で、図には入れない。
- 登場人物：人型は使わず、土地・登記・情報は文字のカードで示す。事例の当事者は甲土地・乙土地。
- 矢印の意味：矢印は使わない。コマ1は縦2枚のカード、コマ2は左右のカード、コマ3は左の縦3枚のカードと右の会話。
- 配色：コマ1〜3は印（✓✕）を付けない（コマ2の左右のカードは、どちらも正しい取扱いの対比で、〇×の対比ではない）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（通常サイズのキャラが左右の端、図は中央）、コマ2＝none（図が主役）、コマ3＝faces（左に縦3枚のカード、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 要役地の地役権は、消せば合筆できる | 「消せば合筆できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　地役権があっても、合筆？ | — |
| コマ1 図 | 図・カード | 肢D0348：要役地の地役権を消せば、分合筆できる？ / 甲土地 / 要役地の地役権の登記がある / 一部を分筆して、乙土地に合筆したい / 添える情報 / 地役権者の作成した情報 / 合筆する部分の地役権を消滅させる | — |
| コマ1 | 藍子（左・先に話す） | 地役権の登記があるなら、合筆はムリですよね？ | — |
| コマ1 | トリ先生（右・答える） | 半分だけ正解よ。消す手があるの | 「消す手」 |
| コマ2 見出し | ラベル | ②　承役地と要役地で、扱いが違う | — |
| コマ2 図 | 図・カード | 法41条6号 / 権利の登記があると、合筆できない / 承役地の地役権は、そのまま合筆できる / 規則105条1号 / 例外に当たり、合筆の障害にならない / 地役権を消す必要はない / 要役地の地役権は、消さないと合筆できない / 例外に入っていない / 合筆の障害になる / 消滅を証する情報で、障害が外れる | — |
| コマ3 見出し | ラベル | ③　なぜ、合筆できる？ | — |
| コマ3 図 | 図・カード | 分筆の申請情報と併せて出す / 地役権を消滅させることを証する情報 / その土地について、地役権が消える / 規則104条6項 / 合筆の障害が外れる / 合筆する部分に地役権が残らない | — |
| コマ3 | 藍子（左・1番目） | 要役地は、例外にないですよね？ | — |
| コマ3 | トリ先生（右・2番目） | ええ。だから地役権を消すの | 「地役権を消す」 |
| コマ3 | 藍子（左・3番目） | 誰の情報で、消せますか？ | — |
| コマ3 | トリ先生（右・4番目） | 地役権者の作成した情報よ | 「地役権者」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 要役地の地役権は、消せば合筆できるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。承役地との混同は禁物よ | 「承役地との混同」 |
| コマ4 チェック欄 | 3項目（青✓） | 要役地の地役権は、消滅を証する地役権者の作成した情報を出せば、合筆できる（肢D0348は〇） / 承役地の地役権の登記は、規則105条1号の例外で、消さなくても合筆できる / 消す情報は、分筆の登記の申請情報と併せて出す（規則104条6項） | — |
| 結論帯 | 1行目 | 要役地の地役権は、消せば合筆できる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0348　正解〇（H20-Q08ア） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記規則104条6項・105条1号、不動産登記法41条6号。法令DB note-articles/laws/fudousan-touki-kisoku-1.md の第百四条・第百五条、fudousan-touki-hou.md の第41条で原文と照合済み。記事の導入部（法41条6号と規則105条の例外）と、同じ章の記事【PD-5】の中身の整理（規則104条6項）が引いている

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

TITLE BANNER: text 「要役地の地役権は、消せば合筆できる」 in large bold letters; the part 「消せば合筆できる」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　地役権があっても、合筆？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: a small question badge 「肢D0348：要役地の地役権を消せば、分合筆できる？」 at the top (a question badge only, with no check mark and no cross), and under it two SEPARATE cards stacked from top to bottom, both exactly the same size, each with the same pale gray fill and a dark navy outline, with no check mark, no cross, and no arrow anywhere. The two cards are separated only by a small empty gap, with nothing drawn between them.
- Each card has a small dark navy tag at its top left, one bold dark navy heading line, and one body line (each text at least 24 px high).
- Card 1: tag 「甲土地」, heading 「要役地の地役権の登記がある」, body 「一部を分筆して、乙土地に合筆したい」.
- Card 2: tag 「添える情報」, heading 「地役権者の作成した情報」, body 「合筆する部分の地役権を消滅させる」.
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「地役権の登記が
あるなら、合筆は
ムリですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「半分だけ正解よ。
消す手があるの」 with the part 「消す手」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　承役地と要役地で、扱いが違う」
- A small dark navy tag 「法41条6号」 at the top left, with one line beside it: 「権利の登記があると、合筆できない」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「承役地の地役権は、そのまま合筆できる」, a small tag 「規則105条1号」, two body lines: 「例外に当たり、合筆の障害にならない」, 「地役権を消す必要はない」.
- Right card, heading 「要役地の地役権は、消さないと合筆できない」, a small tag 「例外に入っていない」, two body lines: 「合筆の障害になる」, 「消滅を証する情報で、障害が外れる」, with the heading highlighted with a yellow marker.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、合筆できる？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- LEFT SIDE: three stacked reason cards of the same size, from top to bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card and one short body line, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Card 1, heading 「分筆の申請情報と併せて出す」, body 「地役権を消滅させることを証する情報」.
- Card 2, heading 「その土地について、地役権が消える」, body 「規則104条6項」.
- Card 3, heading 「合筆の障害が外れる」, body 「合筆する部分に地役権が残らない」.
- The three cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「要役地は、例外に
ないですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「ええ。だから
地役権を消すの」 with the part 「地役権を消す」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「誰の情報で、
消せますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「地役権者の作成した
情報よ」 with the part 「地役権者」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「要役地の地役権は、
消せば合筆できる
んですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。承役地との
混同は禁物よ」 with the part 「承役地との混同」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「要役地の地役権は、消滅を証する地役権者の作成した情報を出せば、合筆できる（肢D0348は〇）」, 「承役地の地役権の登記は、規則105条1号の例外で、消さなくても合筆できる」, 「消す情報は、分筆の登記の申請情報と併せて出す（規則104条6項）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「要役地の地役権は、消せば合筆できる」 with a yellow highlighter marker.
- Line 2: 「問題D0348　正解〇（H20-Q08ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 当, 承, 権, 物, 登, 肢, 規, 解, 記, 証, 請, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panels 1, 2 and 3 contain no check mark and no cross anywhere, that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the left card of panel 2 has the heading 「承役地の地役権は、そのまま合筆できる」 and the right card has the heading 「要役地の地役権は、消さないと合筆できない」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編4章_4コマ5_要役地の地役権は、消せば合筆できる.png`
- 途中の版・不採用の版：`不動産登記法編4章_4コマ5_要役地の地役権は、消せば合筆できる_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch4/prompt_4koma_PD-05_01_yoekichi-chieki-gappitsu.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『要役地の地役権の登記がある土地の分合筆で、地役権を消す情報を添えればよいか』を問う肢だと分かり、コマ2で承役地は例外・要役地は消さないと合筆できない、コマ3で消す情報を出すと合筆する部分に地役権が残らず障害が外れること、が言える
- [ ] 工程C：構成表の全文言を記事（H20-Q08ア）と法令DB（法41条6号・規則104条6項・規則105条1号）に突き合わせ済み。記事が根拠に引く法40条ではなく、要役地の地役権を直接定める規則104条6項を図に載せた（記事との食い違いとして報告する）
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない。肢D0743（第三者の承諾）は図に入れていない
- [ ] 工程C：肝の確認：①承役地の地役権の登記は規則105条1号の例外で、消さなくても合筆できる②要役地の地役権の登記は例外にない③分筆の申請情報と併せて地役権を消滅させることを証する地役権者の作成した情報を出す（規則104条6項）④合筆する部分に地役権が残らず、法41条6号の障害が外れる⑤肢D0348は〇

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

## 改訂履歴（このファイルは `src/spec_4koma_PD-05_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第4章【PD-5】用。型3の理由説明＋型1の対比。承役地の地役権〔規則105条1号の例外〕と要役地の地役権〔消せば障害が外れる。規則104条6項〕の対比に絞った。既存の4コマ〔D0597・D0599／D0646・D0743／D0957・D0600〕とは別の肢D0348）
