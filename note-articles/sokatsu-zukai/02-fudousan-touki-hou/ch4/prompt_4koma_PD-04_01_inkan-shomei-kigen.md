# D1940・D2056 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②不動産登記法編 第4章「土地の分筆・合筆・地積更正」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md`）の、論点【PD-4】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PD-04_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1940・D2056（不動産登記法／土地の分筆・合筆・地積更正、出典 R06-Q08ア／R07-Q11エ）。正解＝D1940＝〇（正しい記述）／D2056＝×（誤った記述）。
- 記事：`note-articles/r6-mondai/q08-bunpitsu-touki.md` ア（R6：会社法人等番号を提供すれば、要役地の地役権の登記がある土地を分筆する株式会社の印鑑証明書は不要。不動産登記規則50条2項）。ほか、R07-Q11エ（r7-mondai/q11-bunpitsu.md。第三者の承諾書に添付する印鑑証明書に、3か月の作成期限はない。不動産登記令16条3項・18条3項に対し、19条2項には期限の定めがない）。章の記事 note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md 【PD-4】
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D2056は、承諾書に添える印鑑証明書に『作成後3月以内のものでなければならない』と、申請書・委任状の印鑑証明書の要件（令16条3項・18条3項）をそのまま持ち込む。D1940は、『地役権を消滅させることを証する書面』『会社法人等番号を申請情報として提供』と長く書き、印鑑証明書が省けるのは申請人の会社についてだけなのか、承諾する側についても省けるのかを迷わせる。
- 【受験者の勘違い・定着していない点】（推測）①印鑑証明書の『3月以内』を、申請書・委任状・承諾書のどれにも共通の要件と一般化する。承諾書の印鑑証明書について定める令19条2項には期限の定めがないことが結びついていない。②会社なら会社法人等番号を提供すれば印鑑証明書は不要（規則48条1号）という特例が、承諾書の側にも準用されている（規則50条2項）ことが定着していない。③その特例は、登記官が証明を作成できる場合に限る。
- 【対比する制度】「申請書・委任状の印鑑証明書」⇔「承諾書の印鑑証明書」：申請書（令16条2項・3項）・委任状（令18条2項・3項）に付ける印鑑証明書は、作成後3月以内のものでなければならない／承諾書に付ける印鑑証明書（令19条2項）には、その期限の定めがない（結論が逆になる点）。どちらも、会社法人等番号の提供で省けることがある。
- 【型の選び方】型：型4（複数肢の対比）に型5（整理カード）を併用。理由：壁＝『印鑑証明書は、どの書類でも3月以内で、いつも取り寄せる』という一般化。2つの肢が同じ『印鑑証明書』の扱いを違う軸（期限／省略）で問うので、コマ1で2つの肢を並べ、コマ2で『申請書・委任状』と『承諾書』の期限の有無を左右のカードで対比し、コマ3は左に2肢の言い分、右に会話1往復と『承諾書の印鑑証明書の扱い』の整理カード（令19条の条文の流れと、会社法人等番号による省略）を置いた。時系列の事例がないので、型4のコマ1は日付カードでなく、2肢の並置にした。
- コマごとに読者が言えること：コマ1＝分筆の登記の添付情報のうち、印鑑証明書の扱いを問う2つの肢（会社の印鑑証明書は省けるか／承諾書の印鑑証明書は3月以内か）。コマ2＝申請書・委任状の印鑑証明書は3月以内、承諾書の印鑑証明書には期限の定めがない。コマ3＝承諾書は作成者が記名押印して印鑑証明書を添付する（官庁・公署の作成なら要らない）、会社法人等番号の提供で省ける（登記官が証明を作成できる場合に限る）。コマ4＝D1940は〇、D2056は×。
- 記事の範囲：R06-Q08ア（規則50条2項。会社法人等番号を提供すれば、地役権者でもある株式会社の印鑑証明書は不要）、R07-Q11エ（令16条3項・18条3項の『作成後3月以内』は申請書・委任状の側。令19条2項には期限がなく、半年前・1年前に取ったものでも使える）。章の記事【PD-4】の中身の整理にも同じ記述がある。
- extra_refs：不動産登記令16条2項・3項、18条2項・3項、19条1項・2項（法令DB note-articles/laws/fudousan-touki-rei.md の第16条・第18条・第19条で原文を確認。16条3項・18条3項は『作成後三月以内のものでなければならない』、19条2項は『官庁又は公署の作成に係る場合その他法務省令で定める場合を除き、…印鑑に関する証明書を添付しなければならない』で期限の文言なし）。不動産登記規則48条1号・50条2項（法令DB note-articles/laws/fudousan-touki-kisoku-1.md の第48条・第50条で原文を確認。48条1号『法人の代表者又は代理人が記名押印した者である場合において、その会社法人等番号を申請情報の内容としたとき。ただし、登記官が記名押印した者の印鑑に関する証明書を作成することが可能である場合に限る』、50条2項『第48条第1号から第3号までの規定は、令第19条第2項の法務省令で定める場合について準用する』）。整理カードの『官庁・公署の作成なら要らない』は令19条2項の文言による
- 同じ論点の他の肢（図には肢として載せない）：D0375（敷地権付き区分建物の敷地の分筆に、分離処分を可能とする規約を証する情報は要らない。×）は、既存の4コマがあるので今回は扱わない。分筆の添付情報の柱が地積測量図であること（令別表8の項）も、この4コマは印鑑証明書の扱いに絞って入れていない。
- 登場人物：当事者の人型は使わず、書類は文字のカードで示す。事例の当事者は、株式会社・抵当権者・地役権者など役割の日本語で書く。
- 矢印の意味：矢印は使わない。コマ1は縦2枚のカード、コマ2は左右のカード、コマ3は上下のカードと整理カード。
- 配色：コマ1〜3は印（✓✕）を付けない（コマ2の左右はどちらも条文どおりの取扱いで、〇×の対比ではない）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（通常サイズのキャラが左右の端、図は中央）、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 承諾書の印鑑証明書に、3か月の期限はない | 「期限はない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　印鑑証明書は、いつも3か月？ | — |
| コマ1 図 | 図・カード | 分筆の登記の添付情報 / 肢D1940 / 地役権のある土地を、株式会社が分筆 / 会社法人等番号を提供すれば、印鑑証明書は不要？ / 肢D2056 / 抵当権者の承諾書に付ける印鑑証明書 / 作成後3月以内でなければならない？ | — |
| コマ1 | 藍子（左・先に話す） | 印鑑証明書は、いつも3か月以内ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。どの書類に付くか見なさい | 「どの書類」 |
| コマ2 見出し | ラベル | ②　付く書類で、期限の有無が違う | — |
| コマ2 図 | 図・カード | 不動産登記令 / 書類ごとに、期限の定めが違う / 申請書・委任状の印鑑証明書 / 16条3項・18条3項 / 作成後3月以内のもの / 期限がある / 承諾書の印鑑証明書 / 19条2項 / 期限の定めがない / 半年前に取ったものでも使える | — |
| コマ3 見出し | ラベル | ③　承諾書の印鑑証明書の扱い | — |
| コマ3 図 | 図・カード | 肢D1940の言い分 / 会社法人等番号を提供すれば、会社の印鑑証明書は要らない / 肢D2056の言い分 / 承諾書の印鑑証明書は、作成後3月以内でなければならない / 承諾書の印鑑証明書 / 作成者が記名押印する / 印鑑証明書を添付する / 官庁・公署の作成なら要らない / 会社法人等番号の提供で省ける / 登記官が証明を作成できる場合に限る | — |
| コマ3 | 藍子（左・1番目） | 会社なら、番号の提供で省けますか？ | — |
| コマ3 | トリ先生（右・2番目） | ええ。登記官が作れる場合に限るわ | 「限る」 |
| コマ4 見出し | ラベル | ④　結論は〇と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 期限があるのは、申請書と委任状なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。承諾書の方に、期限はないわ | 「期限はない」 |
| コマ4 チェック欄 | 3項目（青✓） | 承諾書の印鑑証明書に、作成後3月以内の定めはない（令19条2項。肢D2056は×） / 作成後3月以内が要るのは、申請書・委任状の印鑑証明書（令16条3項・18条3項） / 会社法人等番号を提供すれば、会社の印鑑証明書は要らない（規則50条2項。肢D1940は〇） | — |
| 結論帯 | 1行目 | 承諾書の印鑑証明書に、3か月の期限はない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1940・D2056　正解〇・×（出典 R06-Q08ア／R07-Q11エ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記令16条3項・18条3項・19条2項、不動産登記規則48条1号・50条2項。法令DB note-articles/laws/fudousan-touki-rei.md の第16条・第18条・第19条、同 fudousan-touki-kisoku-1.md の第48条・第50条で原文と照合済み。記事（R06-Q08ア・R07-Q11エ）が規則50条2項、令16条3項・18条3項・19条2項を引いている。整理カードの『官庁・公署の作成なら要らない』は令19条2項の文言から。記事にない規則48条1号の引用は、50条2項の準用の中身を確かめたもの

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

TITLE BANNER: text 「承諾書の印鑑証明書に、3か月の期限はない」 in large bold letters; the part 「期限はない」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　印鑑証明書は、いつも3か月？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: a small question badge 「分筆の登記の添付情報」 at the top (a question badge only, with no check mark and no cross), and under it two SEPARATE cards stacked from top to bottom, both exactly the same size, each with the same pale gray fill and a dark navy outline, with no check mark, no cross, and no arrow anywhere. The two cards are separated only by a small empty gap, with nothing drawn between them.
- Each card has a small gray tag at its top left, one bold dark navy heading line, and one body line (each text at least 24 px high).
- Card 1: tag 「肢D1940」, heading 「地役権のある土地を、株式会社が分筆」, body 「会社法人等番号を提供すれば、印鑑証明書は不要？」.
- Card 2: tag 「肢D2056」, heading 「抵当権者の承諾書に付ける印鑑証明書」, body 「作成後3月以内でなければならない？」.
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「印鑑証明書は、
いつも3か月以内
ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
どの書類に付くか
見なさい」 with the part 「どの書類」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　付く書類で、期限の有無が違う」
- A small dark navy tag 「不動産登記令」 at the top left, with one line beside it: 「書類ごとに、期限の定めが違う」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「申請書・委任状の印鑑証明書」, a small tag 「16条3項・18条3項」, two body lines: 「作成後3月以内のもの」, 「期限がある」.
- Right card, heading 「承諾書の印鑑証明書」, a small tag 「19条2項」, two body lines: 「期限の定めがない」, 「半年前に取ったものでも使える」, with the heading highlighted with a yellow marker.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　承諾書の印鑑証明書の扱い」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Top card, heading 「肢D1940の言い分」, body 「会社法人等番号を提供すれば、会社の印鑑証明書は要らない」.
- Bottom card, heading 「肢D2056の言い分」, body 「承諾書の印鑑証明書は、作成後3月以内でなければならない」.
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「承諾書の印鑑証明書」, with the same pale gray fill and a dark navy outline, containing exactly four short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots, so that they cannot be confused with the circled panel numbers), with no arrow and no check mark and no cross: 「作成者が記名押印する」, 「印鑑証明書を添付する」, 「官庁・公署の作成なら要らない」, 「会社法人等番号の提供で省ける」, with the row 「会社法人等番号の提供で省ける」 highlighted with a yellow marker. Under the four rows, one small dark navy ribbon tag with white text 「登記官が証明を作成できる場合に限る」.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「会社なら、番号の
提供で省けますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「ええ。
登記官が作れる
場合に限るわ」 with the part 「限る」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇と×」
- 藍子 bubble (left, spoken first): 「期限があるのは、
申請書と委任状
なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。承諾書の方に、
期限はないわ」 with the part 「期限はない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「承諾書の印鑑証明書に、作成後3月以内の定めはない（令19条2項。肢D2056は×）」, 「作成後3月以内が要るのは、申請書・委任状の印鑑証明書（令16条3項・18条3項）」, 「会社法人等番号を提供すれば、会社の印鑑証明書は要らない（規則50条2項。肢D1940は〇）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「承諾書の印鑑証明書に、3か月の期限はない」 with a yellow highlighter marker.
- Line 2: 「問題D1940・D2056　正解〇・×（出典 R06-Q08ア／R07-Q11エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 当, 承, 抵, 押, 権, 無, 番, 登, 肢, 規, 解, 記, 証, 請, 諾, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編4章_4コマ4_承諾書の印鑑証明書に、3か月の期限はない.png`
- 途中の版・不採用の版：`不動産登記法編4章_4コマ4_承諾書の印鑑証明書に、3か月の期限はない_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch4/prompt_4koma_PD-04_01_inkan-shomei-kigen.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で印鑑証明書の扱いを問う2つの肢、コマ2で申請書・委任状の印鑑証明書は3月以内で承諾書の印鑑証明書は期限なしという対比、コマ3で承諾書の印鑑証明書は会社法人等番号の提供で省けること（登記官が証明を作成できる場合に限る）が言える
- [ ] 工程C：構成表の全文言を記事（R06-Q08ア、R07-Q11エ）と法令DB（令16条・18条・19条、規則48条1号・50条2項）に突き合わせ済み。整理カードの『官庁・公署の作成なら要らない』は令19条2項の文言どおり
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない。D0375は肢として扱わない
- [ ] 工程C：肝の確認：①申請書・委任状の印鑑証明書は作成後3月以内（令16条3項・18条3項）②承諾書の印鑑証明書（令19条2項）には期限の定めがない③会社法人等番号を提供すれば、承諾書の印鑑証明書も省ける（規則50条2項。登記官が証明を作成できる場合に限る）④肢D1940は〇、D2056は×

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

## 改訂履歴（このファイルは `src/spec_4koma_PD-04_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第4章【PD-4】用。型4に型5の整理カードを併用。申請書・委任状の印鑑証明書の3月の期限と、承諾書の印鑑証明書に期限がないこと、会社法人等番号による省略に絞った。D0375〔規約証明〕は既存の4コマ）
