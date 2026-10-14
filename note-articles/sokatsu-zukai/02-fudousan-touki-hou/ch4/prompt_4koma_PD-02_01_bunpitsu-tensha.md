# D1666・D1750 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②不動産登記法編 第4章「土地の分筆・合筆・地積更正」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md`）の、論点【PD-2】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PD-02_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1666・D1750（不動産登記法／土地の分筆・合筆・地積更正、出典 R03-Q11イ／R04-Q08エ）。正解＝D1666＝〇（正しい記述）／D1750＝×（誤った記述）。
- 記事：`note-articles/r3-mondai/q11-bunpitsu.md` イ（R03：賃借権の設定の登記がある甲土地の分筆に、賃借権の登記名義人が承諾したことを証する情報は添付情報とされていない）。ほか、R04-Q08エ（r4-mondai/q08-bunpitsu.md。担保権の登記がある土地の分筆では、規則102条1項により原則として共同担保目録が作成されるが、根抵当権設定の仮登記がある土地の分筆では新たに共同担保目録を作成しない。条文に明記がなく、先例に基づく実務の取扱い）。章の記事 note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md 【PD-2】
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D1666は『賃借権の登記名義人が承諾したことを証する情報を提供することなく、分筆の登記を申請することができる』と、借主の承諾を抜いた形で問う。借主の権利が登記されている土地を分けるのだから承諾が要るはず、と読ませる。D1750は『根抵当権設定の仮登記がある土地』と、担保権（共同担保目録が作られる）の場面に見せかけて『新たに共同担保目録を作成しなければならない』と言い切る。仮登記という一語が例外の入口である。
- 【受験者の勘違い・定着していない点】（推測）①承諾が要るのは、分筆後の一方の土地で権利を消したいときだけ（法40条）という分かれ目が結びついておらず、権利者がいれば分筆に承諾が要ると考える。②分筆では、権利に関する登記が乙土地にもそのまま写される（転写）ことが、承諾が要らない理由だと結びついていない。③担保権の転写には共同担保目録が付くのが原則（規則102条1項）という覚え方を、根抵当権設定の仮登記にも広げる。
- 【対比する制度】「権利を残す分筆」⇔「権利を消す分筆」：権利を残す分筆は、賃借権などの登記が乙土地にも写されるだけで、借主の承諾は要らない（肢D1666）／権利を消す分筆は、分筆後の一方の土地で権利を消すので、権利者の承諾の情報を出す（法40条）（結論が逆になる点）。
- 【型の選び方】型：型4（複数肢の対比。場面が別々で共通の日付がない）に型5（整理カード併用）を組み合わせる。理由：2肢は別々の場面（賃借権／根抵当権設定の仮登記）で共通の日付がなく、読者は『分筆で権利がどう写るか』を自分で並べ直せない。壁＝『権利者がいるなら承諾が要る。担保権なら目録は必ず付く』という思い込み。コマ1＝2肢のカード、コマ2＝『権利を残す分筆』と『権利を消す分筆』の左右のカード、コマ3＝左は肢D1750の言い分（✕）と正しい整理（✓）の上下カード、右は会話1往復と、権利ごとの写され方の整理カード、コマ4＝〇・×の整理。既存の4コマ（D0026の承諾不要、D2053の共有物分割の判決）の焼き直しにせず、写され方の整理（転写）を主役にして区別した。
- コマごとに読者が言えること：コマ1＝賃借権の登記と根抵当権設定の仮登記がある土地を分筆するとき、何が問われるか（借主の承諾／共同担保目録）。コマ2＝権利を残す分筆は承諾が要らず、権利を消す分筆は権利者の承諾の情報を出す。コマ3＝担保権は共同担保目録が作られるのが原則だが、根抵当権設定の仮登記では新たに作られない（実務の取扱い）。コマ4＝D1666は〇、D1750は×。
- 記事の範囲：R03-Q11イ（分筆は表示に関する登記で、賃借権の登記名義人が承諾したことを証する情報は添付情報とされていない。賃借権に特化した一次資料はなく、条文レベルの断定は避けた、と記事が注記している）と、同ウ（法40条により、消滅を承諾した土地について権利が消滅した旨が登記される）。R04-Q08エ（規則102条1項により担保権は原則として共同担保目録が作成される。根抵当権設定の仮登記では新たに作成しないとされる。条文に明記なし・先例に基づく実務の取扱い）。章の記事【PD-2】の『中身の整理』（権利に関する登記は乙土地の登記記録に転写される）。
- extra_refs：不動産登記規則102条1項（乙土地の権利部に権利に関する登記を転写し、担保権については既にその権利についての共同担保目録が作成されているときを除き共同担保目録を作成する）・不動産登記法40条（分筆に伴う権利の消滅の登記）は、法令DB note-articles/laws/fudousan-touki-kisoku-1.md の第102条、note-articles/laws/fudousan-touki-hou.md の第40条で原文を確認した。規則102条1項は条文に仮登記を除く旨を書いておらず、根抵当権設定の仮登記で作成しない取扱いは条文に明記のない先例の整理なので、図にも『条文に明記なし・実務の取扱い』と添えた。
- 同じ論点の他の肢（図に肢として載せない）：D0026（仮差押えのある土地の分筆に承諾は要らない・×）とD2053（共有物分割の判決があっても、分筆では単独所有にならない・×）には既存の4コマがある。D0744（共有者を単独所有者に分ける情報を出しても、分筆では単独所有にならない・×）は、D2053と同じ『分筆では共有は共有のまま』が決め手なので、今回は扱わない。
- 登場人物：人型は使わず、権利と土地は文字のカードで示す。事例の当事者は出さない（借主と書く）。
- 矢印の意味：矢印は使わない。コマ1は縦2枚のカード、コマ2は左右のカード、コマ3は上下のカードと整理カード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（通常サイズのキャラが左右の端、図は中央の約56％）、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 分筆で、権利は乙土地へ写される | 「乙土地へ写される」を黄色マーカー |
| コマ1 見出し | ラベル | ①　権利がある土地を分筆すると？ | — |
| コマ1 図 | 図・カード | 肢D1666 / 賃借権の登記がある土地の分筆 / 借主の承諾の情報なしで、申請できる？ / 肢D1750 / 根抵当権設定の仮登記がある土地の分筆 / 新たに共同担保目録を作らなければならない？ / 権利がある土地を分筆すると？ | — |
| コマ1 | 藍子（左・先に話す） | 借主の承諾が、要りますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。分筆は権利を消さないの | 「権利を消さない」 |
| コマ2 見出し | ラベル | ②　権利を残す分筆と、消す分筆 | — |
| コマ2 図 | 図・カード | 分筆と権利者の承諾 / 権利を消すかどうかで、結論が変わる / 権利を残す分筆 / 転写されるだけ / 賃借権などは、乙土地にも写される / 借主の承諾は、要らない / 肢D1666は、こちらの場面 / 要らない / 権利を消す分筆 / 法40条 / 分筆後の一方の土地で、権利を消す / 権利者の承諾の情報を、出す / 肢D1666と逆の場面 / 消さない分筆なら、承諾は要らない | — |
| コマ3 見出し | ラベル | ③　担保権の転写と、共同担保目録 | — |
| コマ3 図 | 図・カード | 仮登記でも、目録を新しく作る / 肢D1750の言い分 / 仮登記では、新たには作らない / 条文に明記なし・実務の取扱い / 分筆で写される権利 / 賃借権など：写すだけ、承諾は不要 / 担保権：共同担保目録を作るのが原則 / 根抵当権設定の仮登記：目録は作らない / 仮登記の例外は実務の取扱い | — |
| コマ3 | 藍子（左・1番目） | 担保権なら、目録は必ず作りますよね？ | — |
| コマ3 | トリ先生（右・2番目） | 仮登記は別。実務では作らないの | 「実務では作らない」 |
| コマ4 見出し | ラベル | ④　結論は〇と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 写すだけなら、承諾は要らないんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。仮登記の目録は別よ | 「仮登記の目録は別」 |
| コマ4 チェック欄 | 3項目（青✓） | 賃借権の登記がある土地の分筆に、借主の承諾の情報は要らない（肢D1666は〇） / 根抵当権設定の仮登記がある土地の分筆では、新たに共同担保目録を作らない（肢D1750は×） / 承諾の情報を出すのは、分筆後の一方の土地で権利を消すとき（法40条） | — |
| 結論帯 | 1行目 | 分筆は権利を写すだけ。消さないなら承諾は要らない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1666・D1750　正解〇・×（R03-Q11イ／R04-Q08エ） | — |

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

TITLE BANNER: text 「分筆で、権利は乙土地へ写される」 in large bold letters; the part 「乙土地へ写される」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　権利がある土地を分筆すると？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: two SEPARATE cards stacked from top to bottom, both the same size, each with the same pale gray fill, a dark navy outline, a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers), and two short dark navy text lines. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1 with a small gray tag 「肢D1666」: 「賃借権の登記がある土地の分筆」 and 「借主の承諾の情報なしで、申請できる？」. Card 2 with a small gray tag 「肢D1750」: 「根抵当権設定の仮登記がある土地の分筆」 and 「新たに共同担保目録を作らなければならない？」.
- At the top, a small question badge in a gray fill with dark navy text 「権利がある土地を分筆すると？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「借主の承諾が、
要りますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
分筆は権利を
消さないの」 with the part 「権利を消さない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　権利を残す分筆と、消す分筆」
- A small dark navy tag 「分筆と権利者の承諾」 at the top left, with one line beside it: 「権利を消すかどうかで、結論が変わる」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「権利を残す分筆」, a small tag 「転写されるだけ」, two body lines: 「賃借権などは、乙土地にも写される」, 「借主の承諾は、要らない」, and a small dark navy tag 「肢D1666は、こちらの場面」, with the text 「要らない」 highlighted with a yellow marker.
- Right card, heading 「権利を消す分筆」, a small tag 「法40条」, two body lines: 「分筆後の一方の土地で、権利を消す」, 「権利者の承諾の情報を、出す」, and a small dark navy tag 「肢D1666と逆の場面」.
- Under the two cards, one wide dark navy band with large white text 「消さない分筆なら、承諾は要らない」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　担保権の転写と、共同担保目録」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「仮登記でも、目録を新しく作る」, body 「肢D1750の言い分」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「仮登記では、新たには作らない」, body 「条文に明記なし・実務の取扱い」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「分筆で写される権利」, with the same pale gray fill and a dark navy outline, containing exactly three short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「賃借権など：写すだけ、承諾は不要」, 「担保権：共同担保目録を作るのが原則」, 「根抵当権設定の仮登記：目録は作らない」, with the third row highlighted with a yellow marker. Under the three rows, one small dark navy ribbon tag with white text 「仮登記の例外は実務の取扱い」.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「担保権なら、
目録は必ず
作りますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「仮登記は別。
実務では
作らないの」 with the part 「実務では作らない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇と×」
- 藍子 bubble (left, spoken first): 「写すだけなら、
承諾は要らない
んですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
仮登記の目録は
別よ」 with the part 「仮登記の目録は別」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「賃借権の登記がある土地の分筆に、借主の承諾の情報は要らない（肢D1666は〇）」, 「根抵当権設定の仮登記がある土地の分筆では、新たに共同担保目録を作らない（肢D1750は×）」, 「承諾の情報を出すのは、分筆後の一方の土地で権利を消すとき（法40条）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「分筆は権利を写すだけ。消さないなら承諾は要らない」 with a yellow highlighter marker.
- Line 2: 「問題D1666・D1750　正解〇・×（R03-Q11イ／R04-Q08エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 保, 地, 当, 承, 抵, 権, 登, 肢, 解, 記, 請, 諾, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the word 「原則」 is spelled exactly like this everywhere (never 「思則」); confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1 and panel 2 contain no check mark and no cross anywhere, that panel 3 has exactly one red cross (on the top-left card) and exactly one blue check mark (on the bottom-left card) and no other mark, and that the only blue check marks outside panel 3 are the three in the checklist of panel 4; confirm that the left card of panel 2 has the heading 「権利を残す分筆」 with the tag 「肢D1666は、こちらの場面」 and the right card has the heading 「権利を消す分筆」 with the tag 「肢D1666と逆の場面」, never swapped; confirm that in panel 1 the card with the tag 「肢D1666」 is on top and the card with the tag 「肢D1750」 is below it confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編4章_4コマ2_分筆で、権利は乙土地へ写される.png`
- 途中の版・不採用の版：`不動産登記法編4章_4コマ2_分筆で、権利は乙土地へ写される_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch4/prompt_4koma_PD-02_01_bunpitsu-tensha.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で2肢の問い（借主の承諾／共同担保目録）、コマ2で権利を残す分筆と権利を消す分筆の対比、コマ3で担保権の目録の原則と仮登記の例外（実務の取扱い）が言える
- [ ] 工程C：構成表の全文言を記事（R03-Q11イ・ウ、R04-Q08エ）・総合記事【PD-2】・法令DB（法40条、規則102条1項）と突き合わせ済み。仮登記の例外は『条文に明記なし・実務の取扱い』と添えた。条番号は肢の記事にあるものだけを図に入れた
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①分筆では権利の登記は乙土地にも写され、権利を消さないなら承諾は要らない（肢D1666は〇）②権利を消すときだけ、権利者の承諾の情報を出す（法40条）③担保権の転写には共同担保目録が作られるのが原則（規則102条1項）④根抵当権設定の仮登記では新たに作らない（条文に明記なし・実務の取扱い。肢D1750は×）

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

## 改訂履歴（このファイルは `src/spec_4koma_PD-02_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第4章【PD-2】用。型4（複数肢の対比）に型5（整理カード併用）を組み合わせた。権利を残す分筆〔転写されるだけ。承諾は不要〕と権利を消す分筆〔法40条〕の対比と、担保権の共同担保目録の原則と根抵当権設定の仮登記の例外〔実務の取扱い〕を整理した。既存の4コマのD0026・D2053とは別の肢。D0744はD2053と同じ決め手なので扱わない）
