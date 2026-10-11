# D0333・D0688・D1491 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第51条第1項の記事に差し込む4コマ（1本目）のプロンプトです。類似の誤解をまとめて、1本の4コマにしました。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`（mainブランチ））に従い、同フォルダの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-09）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0333・D0688・D1491（不動産登記法／建物の分割・合併・合体・滅失・変更、出典 H20-Q05ア／H23-Q16ウ／R01-Q16エ）。正解＝D0333＝×（誤った記述）／D0688・D1491＝〇。
- 記事：`note-articles/h20-mondai/q05-tatemono-taiwa.md` ア「外壁・屋根の改修だけでは、変更登記は必要ない」。ほか、H23-Q16ウ（q16-hyouji-touki-gimu.md）、R01-Q16エ（q16-hyouji-touki-shinsei.md）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【型の選び方】型：型1（第一案・定型）の流れで、コマ2に判定の基準と、コマ1の2つの建物への当てはめを置く。理由：誤解の型（大きな工事＝変更登記が要る／工事をしていない＝要らない）がはっきりしていて、思い込み→押さえどころ→違い→結論で足りるため。壁は『何で見分けるか』と『なぜ張り替えは要らず、分筆は要るのか』なので、コマ2を基準＋当てはめにした。
- 【出題者のひっかけ】D0333は『大規模な改修工事を行ったので』という工事の大きさ、D0688・D1491は『分筆』という土地側の出来事に目を向けさせ、建物の登記事項が変わったかどうかから目を逸らさせる（記事 H20-Q05ア、H23-Q16ウ、R01-Q16エ）。
- 【受験者の勘違い・定着していない点】受験者が陥りやすい勘違いは、変更の登記が要るかを『建物に工事をしたか』『工事が大きいか』で決めてしまうこと。実際は、法44条1項各号の登記事項（所在・種類・構造・床面積など）に変更があったかで決まる。外壁・屋根の材料の張り替えだけでは登記事項は変わらず（屋根の種類が変わらないとき）、逆に工事をしていなくても、敷地の分筆で地番が変われば所在が変わる。
- 【対比する制度】「大きな工事をしたから、変更の登記が要る」⇔「登記事項が変わったときに要る」：工事をしても登記事項が変わらなければ変更の登記は要らない（D0333）／工事をしていなくても、分筆で地番が変われば所在が変わり、1か月以内に要る（D0688・D1491）。結論が逆になる点。
- 登場人物：当事者の記号は使わない。建物は『甲建物』『乙建物』の文字タグで示す。
- 矢印の意味：矢印は使わない（取引も手続も流れもない）。コマ2は基準のカードと当てはめの左右2枚、コマ3は左右の別カード。
- 会話順：藍子の誤解（工事をした乙建物のほうが変更）→トリ先生の訂正（工事の大きさは関係ない）→工事なしでも要る場合→結論。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3は左（よくある勘違い）＝赤✕1つ、右（正しい整理）＝青✓1つ。コマ4の暗記3点は青✓。
- コマの使い方（キャラの大きさ）：コマ1＝side（通常サイズ。図は中央に建物2つで量が少ないので小さくする必要がない）、コマ2＝none（図が主役。基準のカードと当てはめの2枚）、コマ3＝faces（左にカードと例の帯、右に会話4つ。量が多いので顔アイコンにして場所を確保）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。
- 記事の範囲：法51条1項／法44条1項各号の登記事項／規則114条（構造は構成材料・屋根の種類・階数。条文は法令DB fudousan-touki-kisoku-1.md の第114条で確認）／外壁材は登記事項ではない（記事 H20-Q05ア）／分筆で建物の所在する土地の地番が変わると所在の変更の登記（記事 H23-Q16ウ、R01-Q16エ）。『屋根の種類が変わるときは構造の変更』は記事 H20-Q05ア の本文。たとえばの一文（リフォームしても登記の中身が同じなら登記をやり直す必要はない）は記事 H20-Q05ア の例による。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 変更の登記は、工事の大きさでなく登記事項で決まる | 「登記事項で決まる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | 甲建物 / 建物は工事していない / 敷地の分筆で土地の地番が変わった / 乙建物 / 外壁と屋根の材料を張り替えた / 屋根の種類は同じ / 変更の登記が要るのは、どちら？ | — |
| コマ1 | 藍子（左・先に話す） | 工事をした乙建物のほうが、変更ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。工事の大きさに引かれたわね | 「工事の大きさ」 |
| コマ2 見出し | ラベル | ②　出題者のねらい | — |
| コマ2 図 | 図・カード | 出題者のねらい / 変更の登記が要るかを、何で見分けるか / 登記事項に変更があったか（法51条1項） / 所在・種類・構造・床面積など（法44条1項各号） / 構造は構成材料・屋根の種類・階数（規則114条） / 甲建物：1か月以内に申請 / 分筆で土地の地番が変わった / だから建物の所在が変わる / 乙建物：変更の登記は要らない / 外壁材は登記事項ではない / 屋根の種類が同じなら構造も同じ | — |
| コマ3 見出し | ラベル | ③　ひっかけと勘違い | — |
| コマ3 図 | 図・カード | よくある勘違い / 大きな工事をしたから、変更の登記が要る / ひっかけ：外壁と屋根を全面的に張り替える大工事 / 正しい整理 / 登記事項が変わったときに要る / たとえば：外壁と屋根をリフォームしても、登記の中身が同じなら、登記をやり直す必要はない | — |
| コマ3 | 藍子（左・1番目） | 大規模な改修だから、要りますよね？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠よ。工事の大きさは関係ないの | 「関係ない」 |
| コマ3 | 藍子（左・3番目） | 工事なしでも要る場合があるんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 分筆で地番が変われば、所在が変わるわ | 「所在が変わる」 |
| コマ4 見出し | ラベル | ④　結論は登記事項 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 工事の大きさでは決まらないんですね！ | — |
| コマ4 | トリ先生（右・答える） | 登記事項が変わったかを見るのよ | 「登記事項が変わったか」 |
| コマ4 チェック欄 | 3項目（青✓） | 変更の登記が要るかは、工事の大きさでなく、登記事項に変更があったかで決まる（法51条1項） / 外壁・屋根の材料の張り替えだけなら、登記事項は変わらない（屋根の種類が同じとき） / 工事をしなくても、敷地の分筆で地番が変われば、建物の所在の変更の登記が要る | — |
| 結論帯 | 1行目 | 変更の登記は、登記事項が変わったときに要る | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0333・D0688・D1491　D0333＝×、D0688・D1491＝〇 | — |

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

TITLE BANNER: text 「変更の登記は、工事の大きさでなく登記事項で決まる」 in large bold letters; the part 「登記事項で決まる」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A comparison diagram is drawn large in the center region: two simple building icons side by side, each with a dark navy tag above it.
- The left building has the tag 「甲建物」 and a white note card under it with two short lines: 「建物は工事していない」 and 「敷地の分筆で土地の地番が変わった」.
- The right building has the tag 「乙建物」 and a white note card under it with two short lines: 「外壁と屋根の材料を張り替えた」 and 「屋根の種類は同じ」.
- A small question badge 「変更の登記が要るのは、どちら？」 sits above the two buildings (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「工事をした乙建物の
ほうが、変更ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
工事の大きさに
引かれたわね」 with the part 「工事の大きさ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　出題者のねらい」
- A full-width explanation panel fills the whole panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「変更の登記が要るかを、何で見分けるか」.
- In the top center, one wide white card with a dark navy outline and the heading 「登記事項に変更があったか（法51条1項）」, and under the heading two small gray lines: 「所在・種類・構造・床面積など（法44条1項各号）」 and 「構造は構成材料・屋根の種類・階数（規則114条）」.
- Under that card, two white cards side by side, both exactly the same size and top-aligned, each with a dark navy outline, its dark navy heading placed fully INSIDE the card, and two short body lines (no arrows and no connectors, no check mark and no cross).
- Left card, heading 「甲建物：1か月以内に申請」, body 「分筆で土地の地番が変わった」 and 「だから建物の所在が変わる」.
- Right card, heading 「乙建物：変更の登記は要らない」, body 「外壁材は登記事項ではない」 and 「屋根の種類が同じなら構造も同じ」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (surprised then convinced mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　ひっかけと勘違い」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- Two large cards side by side, with a wide example strip under them.
- Left card, heading 「よくある勘違い」, body 「大きな工事をしたから、変更の登記が要る」, with ONE red cross only (no check mark on this card); a dark navy ribbon tag under the body, with large white text, reads 「ひっかけ：外壁と屋根を全面的に張り替える大工事」.
- Right card, heading 「正しい整理」, body 「登記事項が変わったときに要る」, with ONE blue check mark only (no cross on this card).
- Example strip under the two cards: 「たとえば：外壁と屋根をリフォームしても、登記の中身が同じなら、登記をやり直す必要はない」.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「大規模な改修だから、
要りますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠よ。
工事の大きさは
関係ないの」 with the part 「関係ない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「工事なしでも要る
場合があるんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「分筆で地番が変われば、
所在が変わるわ」 with the part 「所在が変わる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (relieved and convinced mood; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は登記事項」
- 藍子 bubble (left, spoken first): 「工事の大きさでは
決まらないんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「登記事項が
変わったかを
見るのよ」 with the part 「登記事項が変わったか」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「変更の登記が要るかは、工事の大きさでなく、登記事項に変更があったかで決まる（法51条1項）」, 「外壁・屋根の材料の張り替えだけなら、登記事項は変わらない（屋根の種類が同じとき）」, 「工事をしなくても、敷地の分筆で地番が変われば、建物の所在の変更の登記が要る」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「変更の登記は、登記事項が変わったときに要る」 with a yellow highlighter marker.
- Line 2: 「問題D0333・D0688・D1491　D0333＝×、D0688・D1491＝〇」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 建, 張, 所, 物, 番, 登, 規, 記, 請, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`4コマ1_変更は登記事項で決まる.png`
- 途中の版・不採用の版：`4コマ1_変更は登記事項で決まる_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0333-D0688-D1491_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『甲建物（工事なし・分筆）と乙建物（張り替え・屋根の種類は同じ）のどちらに変更の登記が要るか』、コマ2で『登記事項に変更があったかで決まる。甲は所在が変わるので要る、乙は外壁材は登記事項でなく屋根の種類が同じなら構造も同じなので要らない』、コマ3で『大工事だから要る、は罠』が言える
- [ ] 工程C：肝の確認：コマ2に『登記事項に変更があったか』の基準と甲・乙への当てはめ、コマ3に『工事の大きさ』⇔『登記事項の変更』の対比、コマ4の暗記3点に『張り替えだけなら不要』『工事なしでも分筆なら要る』が入っている
- [ ] 工程C：構成表の全文言を記事（H20-Q05ア、H23-Q16ウ、R01-Q16エ）・法令DB（法51条1項、法44条1項、規則114条）と突き合わせ：『屋根の種類は同じ』の限定が入っている
- [ ] 工程C：コマの使い方が隣り合うコマで同じにならない（side→none→faces→両方）。結論は D0333＝×、D0688・D1491＝〇 の別を結論帯で示す

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

- 2026-10-09 v01：初版（条文別『苦手克服』シリーズ 第51条第1項 用。類似の誤解を問う3肢を1本にまとめた。ChatGPTでの生成・検品はまだ）
- 2026-10-11 v02：最新ルールで作り直し。コマ2を、判定の基準（法51条1項・44条1項・規則114条）とコマ1の甲・乙建物への当てはめの2枚（結論が逆）に変え、乙建物が要らない理由を図に入れた。コマ3の例を、コマ2と重ならないリフォームの例（記事）に変え、藍子の台詞を問題文の語（大規模な改修）に結びつけた。個人の演習結果は記載しない
