# D1831 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第5章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md`）の、論点【PE-1】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PE-01_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1831（不動産登記法／建物の分割・合併・合体・滅失・変更、出典 R5-Q05イ）。正解＝×（誤った記述）。
- 記事：`note-articles/r5-mondai/q05-hyoudaibu-kiroku.md` イ（R5：先取特権保存済みの建物が完成して表題登記がされるとき、表題部の登記記録は新たに作成されず、保存の登記の際に作られた既存の登記記録が使われる。設計書による事項が抹消され、実際の事項と表題部所有者・新築の原因日付が記録される）。オ（区分建物が区分建物でない建物になった場合は、様式が異なるので新たに登記記録を作成する。規則140条4項）。章の記事 note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md 【PE-1】
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢は『建物の表題登記を申請し、当該登記がされるときは、当該建物の表題部の登記記録が新たに作成される』と書く。『表題登記』という語から、登記記録が起こされる＝新規作成だと読ませる。肢の前半の『不動産工事の先取特権の保存の登記がされている建物』が、すでに表題部ができている前提であることを見落とさせる。
- 【受験者の勘違い・定着していない点】（推測）①『表題登記＝その建物の登記記録を初めて作る登記』と考え、完成前に先取特権の保存の登記をすると『設計書による』旨の表題部が先に作られること（法86条2項1号）を知らない。②『既存の記録が使われる場合』と『新たな記録が作られる場合』を、場面ごとに切り分けていない（この問のオ：区分建物が区分建物でない建物になるときは、様式が異なるので新たに作成する）。
- 【対比する制度】「完成の前から、記録がある」⇔「区分建物が区分建物でない建物になる」：前者（先取特権の保存済みの建物の表題登記）は、保存の登記のときに作られた既存の記録を使う（設計書による事項を抹消して実際の事項を記録する）／後者（その登記）は、様式が異なるので新たに登記記録を作成する（規則140条4項）（結論が逆になる点）。
- 【型の選び方】型：型3（理由説明）。理由：壁＝『表題登記なら新規作成』という思い込みと、なぜ既存の記録が使えるのかが分からないこと。結論（新たには作成されない）だけ覚えても、完成前に表題部がすでにある理由と、新たに作られる場面（区分建物が区分建物でなくなる）が分からないと別の肢で崩れる。コマ1で肢と藍子の思い込みを出し、コマ2で完成前と完成後の左右のカードを並べて時系列を示し、コマ3を理由コマ（記録は完成前からある／新たに作成されるのは別物になるとき）にし、コマ4で暗記3点にした。第一案（思い込み→押さえどころ→違い→結論）の焼き直しにならないよう、『違い』のコマを時系列の対比と理由に分けた。既存の4コマ（D1222の穴埋め、D2058・D0783の区分建物の記録単位）は用語と記録の単位の話で、この肢とは型も題材も重ならない。
- コマごとに読者が言えること：コマ1＝先取特権の保存の登記がされている建物が完成して表題登記がされるとき、表題部は新規に作られるかが問われている。コマ2＝完成前の保存の登記のときに『設計書による』旨の表題部が作られ、完成後の表題登記ではそれが実際の事項に書き換わる。コマ3＝記録は完成前からあるので新たには作られない。新たに作られるのは区分建物が区分建物でない建物になるような別物のとき。コマ4＝D1831は×。
- 記事の範囲：R5-Q05イ（先取特権保存済みの建物の表題登記。平21.2.20民二500号、記事の根拠）、R5-Q05オ（規則140条4項）。同じ記事の肢ア（1個の従前地に1個の換地）・ウ（分筆して合筆する部分）・エ（解体移転）は、この肢の対比に必要な範囲を超えるので図に入れない。
- extra_refs：不動産登記法86条（1項：建物を新築する場合の不動産工事の先取特権の保存の登記は、建物の所有者となるべき者を登記義務者とみなす。2項1号：新築する建物並びに当該建物の種類、構造及び床面積は設計書による旨が登記事項）は法令DB note-articles/laws/fudousan-touki-hou.md の第86条で原文を確認。不動産登記規則140条4項（区分合併以外の原因により区分建物である建物が区分建物でない建物となったときは、1項〜3項〔新たな登記記録の作成、変更前の記録の閉鎖〕を準用）は note-articles/laws/fudousan-touki-kisoku-1.md の第百四十条で原文を確認。『表題登記では既存の記録が使われる』という点は、条文に直接の定めが見つからず、記事（先例 平21.2.20民二500号）の取扱いである。そのため図には『先例』と添える。先例そのものは法令DBにないので、条番号のように断定せず、記事の言い方に合わせた。
- 同じ論点の他の肢（図に入れない理由）：D1222（空欄の語『登記事項』と『登記情報』の入れ替え）には既存の4コマがある。D1224（甲区と乙区に区分して記録されるとした記述・×、正しくは表題部と権利部）は、D1222の4コマのコマ2が登記記録の入れ物と中身を扱うので、今回は扱わない。D0783（区分建物は一棟ごとに登記記録が作成されるとした記述・×）は【PE-3】の4コマ2（D2058・D0783）が扱う。
- 登場人物：当事者の人型は使わず、登記記録・図面は文字のカードで示す。事例の当事者は出さない。
- 矢印の意味：矢印は使わない。コマ1は縦3枚のカード、コマ2は左右のカード（左が完成の前、右が完成の後。時系列は見出しの文字で示す）、コマ3は縦3枚のカード。
- 配色：コマ1〜3は印（✓✕）を付けない（コマ2・コマ3のカードはどれも正しい取扱いで、〇×の対比ではない。肢の言い分のカードも印を付けない）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（通常サイズのキャラが左右の端、図は中央）、コマ2＝none（図が主役）、コマ3＝faces（左に縦3枚のカード、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 完成しても、表題部は新しく作られない | 「新しく作られない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　表題登記で、新しく作られる？ | — |
| コマ1 図 | 図・カード | 肢D1831：表題部の登記記録は、新たに作成される？ / 不動産工事の先取特権の保存の登記がされている / その建物の建築が完了した / 建物の表題登記を申請し、登記がされる | — |
| コマ1 | 藍子（左・先に話す） | 表題登記だから、新しく作られますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。表題部は、もうあるのよ | 「もうある」 |
| コマ2 見出し | ラベル | ②　完成の前と後で、何が起きる？ | — |
| コマ2 図 | 図・カード | 表題部の登記記録 / 完成の前と後を、順に見る / 完成の前：保存の登記のとき / 法86条2項1号 / 表題部が作られる / 種類・構造・床面積は設計書による旨 / 完成の後：表題登記のとき / 先例 / 設計書による事項が抹消される / 実際の事項が記録される / 肢D1831は、右の話 | — |
| コマ3 見出し | ラベル | ③　なぜ、新しく作られないのか | — |
| コマ3 図 | 図・カード | 肢D1831の言い分 / 表題登記だから、新規作成 / 完成後に、表題部が新たに作られる / 正しくは / 完成の前から、記録がある / 保存の登記のときに / 表題部が作られている / 完成の前から / 規則140条4項 / 新たに作成されるのは、別物のとき / 区分建物が区分建物でない建物になる / 様式が異なるので作り直す | — |
| コマ3 | 藍子（左・1番目） | 新築なのに、なぜ記録があるんですか？ | — |
| コマ3 | トリ先生（右・2番目） | 保存の登記で、表題部が先に作られるの | 「先に作られる」 |
| コマ3 | 藍子（左・3番目） | 新たに作られるのは、どんなときですか？ | — |
| コマ3 | トリ先生（右・4番目） | 別物になるとき。様式が違うのよ | 「別物」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 完成しても、記録は引き続き使うんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。表題登記でも、新規作成とは限らないわ | 「限らない」 |
| コマ4 チェック欄 | 3項目（青✓） | 保存の登記のときに、設計書による旨の表題部が先に作られる / 完成後の表題登記では、既存の記録を使う（肢D1831は×） / 新たに作成されるのは、区分建物が区分建物でない建物になるときなど | — |
| 結論帯 | 1行目 | 先取特権の保存済みの建物は、既存の記録を使う | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1831　正解×（R5-Q05イ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法86条（法令DB note-articles/laws/fudousan-touki-hou.md の第86条）と不動産登記規則140条4項（note-articles/laws/fudousan-touki-kisoku-1.md の第百四十条）で原文と照合済み。『既存の記録が使われる』は記事（R5-Q05イ）が引く先例の取扱いで、条文に明記はない

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

TITLE BANNER: text 「完成しても、表題部は新しく作られない」 in large bold letters; the part 「新しく作られない」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　表題登記で、新しく作られる？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: a small question badge 「肢D1831：表題部の登記記録は、新たに作成される？」 at the top (a question badge only, with no check mark and no cross), and under it three SEPARATE cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers), and one dark navy text line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: 「不動産工事の先取特権の保存の登記がされている」. Card 2: 「その建物の建築が完了した」. Card 3: 「建物の表題登記を申請し、登記がされる」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「表題登記だから、
新しく作られますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
表題部は、
もうあるのよ」 with the part 「もうある」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　完成の前と後で、何が起きる？」
- A small dark navy tag 「表題部の登記記録」 at the top left, with one line beside it: 「完成の前と後を、順に見る」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「完成の前：保存の登記のとき」, a small tag 「法86条2項1号」, two body lines: 「表題部が作られる」, 「種類・構造・床面積は設計書による旨」.
- Right card, heading 「完成の後：表題登記のとき」, a small tag 「先例」, two body lines: 「設計書による事項が抹消される」, 「実際の事項が記録される」, with the string 「実際の事項が記録される」 highlighted with a yellow marker.
- Under the two cards, one wide dark navy band with large white text 「肢D1831は、右の話」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、新しく作られないのか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a small dark navy tag at its top left and a dark navy heading placed INSIDE the card, with no check mark, no cross, no arrow, and no connector. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1, tag 「肢D1831の言い分」, heading 「表題登記だから、新規作成」, one body line 「完成後に、表題部が新たに作られる」.
- Card 2, tag 「正しくは」, heading 「完成の前から、記録がある」, two body lines 「保存の登記のときに」 and 「表題部が作られている」, with the string 「完成の前から」 highlighted with a yellow marker.
- Card 3, tag 「規則140条4項」, heading 「新たに作成されるのは、別物のとき」, two body lines 「区分建物が区分建物でない建物になる」 and 「様式が異なるので作り直す」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「新築なのに、
なぜ記録が
あるんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「保存の登記で、
表題部が
先に作られるの」 with the part 「先に作られる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「新たに作られるのは、
どんなときですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「別物になるとき。
様式が違うのよ」 with the part 「別物」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「完成しても、
記録は引き続き
使うんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。表題登記でも、
新規作成とは
限らないわ」 with the part 「限らない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「保存の登記のときに、設計書による旨の表題部が先に作られる」, 「完成後の表題登記では、既存の記録を使う（肢D1831は×）」, 「新たに作成されるのは、区分建物が区分建物でない建物になるときなど」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「先取特権の保存済みの建物は、既存の記録を使う」 with a yellow highlighter marker.
- Line 2: 「問題D1831　正解×（R5-Q05イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 保, 号, 建, 権, 物, 登, 肢, 規, 解, 記, 請, 違, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panels 1, 2 and 3 contain no check mark and no cross anywhere, that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the left card of panel 2 has the heading 「完成の前：保存の登記のとき」 and the right card has the heading 「完成の後：表題登記のとき」, never swapped; confirm that card 1 of panel 3 has the tag 「肢D1831の言い分」, card 2 has the tag 「正しくは」 and card 3 has the tag 「規則140条4項」, in that order from top to bottom confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編⑤_4コマ1_完成しても、表題部は新しく作られない.png`
- 途中の版・不採用の版：`不動産登記法編⑤_4コマ1_完成しても、表題部は新しく作られない_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch5/prompt_4koma_PE-01_01_hyoudaibu-kiroku-shinki.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『先取特権の保存の登記がされた建物の表題登記で、表題部が新規に作られるか』を問う肢だと分かり、コマ2で完成前の保存の登記のときに『設計書による』旨の表題部がすでに作られていること、コマ3で新たに作られるのは区分建物が区分建物でなくなるような別物のときだと言える
- [ ] 工程C：構成表の全文言を記事（R5-Q05イ・オ）と法令DB（法86条2項1号、規則140条4項）に突き合わせ済み。『既存の記録が使われる』は条文に直接の定めがなく記事の取扱いなので、図では『先例』と添えた。先例の番号は図に入れていない
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①完成前の保存の登記のときに『設計書による』旨の表題部が作られる ②完成後の表題登記では既存の記録が使われ、新たには作成されない ③区分建物が区分建物でない建物になるときは、様式が異なるので新たに作成される（規則140条4項） ④D1831は×

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

## 改訂履歴（このファイルは `src/spec_4koma_PE-01_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第5章【PE-1】用。型3（理由説明）。完成前の保存の登記で表題部が先に作られていること、完成後は既存の記録を使うこと、新たに作成されるのは区分建物が区分建物でなくなるような別物のときに絞った）
