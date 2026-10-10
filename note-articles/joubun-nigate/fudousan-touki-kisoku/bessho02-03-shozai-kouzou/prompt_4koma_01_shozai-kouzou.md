# D1762 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記規則 別表二・別表三（建物の表題部の所在欄・構造欄）を主役にした4コマ（1本目）のプロンプトです。条文の中身が1枚で言えるように組み、構成表（文言の正本）を含みます。関連する肢（D1762）は、条文のどこで誤りやすいかを示す材料として使っています。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（ブランチ `claude/kind-bell-y3f106` の `tools/drill/manga/`）に従い、同ブランチの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-10）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。設計データは `src/spec_4koma_01.py` にあります。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。


- 肢：D1762（不動産登記法／建物の認定・個数・種類構造床面積、出典 R04-Q11ア）。正解＝〇（正しい記述）。誤解の型は、所在は所在欄に書くはずという思い込み（条文の側から別表二・別表三の欄の違いで整理する版）。
- 記事：`note-articles/r4-mondai/q11-tatemono-shozai.md` R04-Q11ア「区分建物である甲建物に区分建物でない附属建物があるときは、附属建物の所在は構造欄に記録される」。条文の側は、不動産登記規則第4条第2項・第3項、別表二・別表三（note-articles/laws/fudousan-touki-kisoku-1.md・fudousan-touki-kisoku-3.md）と不動産登記法第44条第1項。附属建物が区分建物の場合は、同じ分野の R04-Q14ウ（note-articles/r4-mondai/q14-fuzoku-tatemono.md）を使う
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文の『附属建物の表示欄の構造欄に附属建物の所在が記録される』という言い回し。『所在』は『所在欄』に書くものという常識があるので、構造欄に所在が書かれると読んだ瞬間に『おかしい、誤りだろう』と×にさせる。さらに、問題文は『区分建物である甲建物に区分建物でない附属建物』と、区分建物の登記記録（別表三）の話であることを示すだけで、別表三の専有部分の表示欄に所在欄がないことは書いていない。
- 【受験者の勘違い・定着していない点】①『所在は所在欄に書くもの』と固定して考え、別表三の専有部分の建物の表示欄には所在欄がない（所在は一棟の建物の表示欄にある）ことを知らない。②区分建物でない建物の別表二（所在欄に附属建物の所在も含める）の感覚のまま、別表三でも同じだと考える。③別表三の附属建物の構造欄に書くと定められているもの（附属建物の構造、附属建物が区分建物なら一棟の建物の所在・構造・床面積・名称）と、区分建物でない附属建物の所在（別表三に定めがなく、実務の取扱いで構造欄）を同じ規定の話として混ぜる。
- 【対比する制度】「別表二」⇔「別表三」：別表二（区分建物でない建物）は、主である建物の所在欄に附属建物の所在も含めて記録する。別表三（区分建物）は、専有部分の建物の表示欄に所在欄がなく（所在は一棟の建物の表示欄）、区分建物でない附属建物の所在は構造欄に記録する（実務の取扱い）。同じ『附属建物の所在』でも、書く欄が逆になる（結論が逆になる点）。別表二の根拠と別表三の欄の構成は記事にない整理（extra_refsに記録）。
- 【型の選び方】型：型2（しくみ図→押さえどころ）に型3の理由を足した混成。理由は条文の構造で示す。理解の壁＝『所在は所在欄に書くはずなのに、なぜ構造欄なのか』。条文の側から見ると、規則第4条が建物を別表二と別表三に振り分け、別表三には専有部分に所在欄がなく、区分建物でない附属建物の所在を書く欄の定めもないので、実務で構造欄になる、という順で言える。コマ1＝問いの場面と別表の振り分け、コマ2＝別表ごとに欄を並べた当てはめ表（非区分の建物／区分建物の専有部分／区分建物である附属建物）、コマ3＝ひっかかる所と正しい読み方（顔アイコンの会話）、コマ4＝暗記3点と結論。肢だけを理由で説明した先の版（tools/drill/manga/D1762_prompt.md）と結論は同じで、こちらは欄の名前を別表の側から並べるのが主題。
- 記事の範囲：R04-Q11ア（区分建物の専有部分に所在欄は存在しない。区分建物でない附属建物の所在は構造欄に記録される。別表三には書かれておらず実務の取扱い）。コマ2の表の第1行（別表二の所在欄）は規則別表二の原文と記事の冒頭文、第2行の『所在は一棟の建物の所在欄』は規則別表三の原文と法第44条第1項第1号、第3行は規則別表二・別表三の原文とR04-Q14ウの記事による。『情報の重複を避けるために専有部分に所在欄がない』という理由づけは、note-articles/topics/fuzoku-tatemono-shozai.md が学習上の説明として書くだけで条文で確認できないため、図に入れない。同じ topics の記事は『別表三が区分建物でない附属建物の所在を構造欄に記録すると定める』ように読める書き方をしているが、別表三の原文にそのような定めは見当たらないので、図は別表の原文と記事R04-Q11アの言い方に従った。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。マンションの一室（区分建物）、庭先の物置（区分建物でない附属建物）、登記記録の欄は、アイコンと文字ラベルで示す。
- 矢印の意味：矢印は使わない。コマ2は表、コマ3は上下2枚のカードとリボン。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラは通常の大きさで左右の端。図は中央）、コマ2＝none（キャラも吹き出しもない。当てはめ表が主役）、コマ3＝faces（左に上下2枚のカードとリボン、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝既定（暗記3点と結論）。
- 関連肢：同じ問の兄弟肢D1763（一棟の建物の所在欄に地番を加える変更登記）・D1764（またがる建物の所在欄の記録の順）は、いずれも『所在欄』の話で、区分建物の所在欄は一棟の建物の表示欄にあるという本図の整理とつながる。D1580・D1581（専有部分の構造欄は1階建）は専有部分の表示欄の構造欄の話。今回は図に入れず、別表三の『専有部分の建物の表示欄』に所在欄がないことだけを使った。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1762～R04-Q11ア～

## note記事の冒頭文

マンションの一室のような区分建物に、庭先の物置のような区分建物でない附属建物が付いています。その物置の所在は、登記記録のどの欄に記録されるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和4年度　第11問　ア）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 区分建物の附属建物の所在は、構造欄に書く | 「構造欄に書く」を黄色マーカー |
| コマ1 見出し | ラベル | ①　所在は、どの別表で見る？ | — |
| コマ1 図 | 図・カード | 区分建物の一室 / 区分建物でない附属建物 / 規則第4条　登記記録の編成 / 区分建物でない建物は、別表二 / 区分建物は、別表三 / 別表三 / 附属建物の所在は、どの欄？ | — |
| コマ1 | 藍子（左・先に話す） | 所在は、所在欄に書きますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。区分建物は別表三を見なさい | 「別表三」 |
| コマ2 見出し | ラベル | ②　別表で、書く欄が決まる | — |
| コマ2 図 | 図・カード | 場面 / 所在などを書く欄 / 区分建物でない建物 / 別表二 / 主である建物の所在欄に、附属建物の所在も含めて記録 / 区分建物 / 別表三 / 所在は一棟の建物の所在欄。専有部分の表示欄に所在欄はない / 附属建物が区分建物 / 別表二・別表三 / 附属建物の構造欄に、一棟の建物の所在・構造・床面積・名称も記録 / 同じ所在でも、別表二と別表三で書く欄が違う / 書く欄が違う | — |
| コマ3 見出し | ラベル | ③　別表三の読み方 | — |
| コマ3 図 | 図・カード | 別表三の専有部分 / 専有部分の表示欄に、所在欄はない / 所在は、一棟の建物の表示欄にある / 区分建物でない附属建物の所在 / 登記事項だが、別表三に欄の定めなし / 実務の取扱いで、構造欄に記録 / ひっかけ：所在なのに、構造欄 | — |
| コマ3 | 藍子（左・1番目） | 構造欄に所在なんて、変ですよね？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。専有部分に所在欄はないのよ | 「所在欄はない」 |
| コマ3 | 藍子（左・3番目） | では、物置の所在はどこですか？ | — |
| コマ3 | トリ先生（右・4番目） | 別表三に定めはなく、実務で構造欄に書くのよ | 「構造欄」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 欄は、別表で決まるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。まず別表二か三かを見るのよ | 「別表二か三か」 |
| コマ4 チェック欄 | 3項目（青✓） | 区分建物でない建物は別表二。所在欄に附属建物の所在も含む / 区分建物は別表三。専有部分の表示欄に所在欄はない / 区分建物でない附属建物の所在は、構造欄に記録される | — |
| 注記 | 小さな注記（コマ4の下） | 区分建物でない附属建物の所在を構造欄に書く点は、別表三に定めがなく実務の取扱い | — |
| 結論帯 | 1行目 | 区分建物の附属建物の所在は、構造欄に記録される | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1762　正解〇（R04-Q11ア） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記規則第4条第2項・第3項（note-articles/laws/fudousan-touki-kisoku-1.md）：区分建物でない建物の登記記録の表題部は別表二、区分建物である建物の登記記録の表題部は別表三の欄に区分して記録する。肢アの記事（R04-Q11）は第4条第3項別表三だけに触れ、第2項と別表二には触れていないため、法令DBで確認した出典。
- 不動産登記規則別表二（区分建物でない建物の登記記録。note-articles/laws/fudousan-touki-kisoku-3.md）：主である建物の表示欄の所在欄は『所在（附属建物の所在を含む。）』。附属建物の表示欄の構造欄は『附属建物の構造』『附属建物が区分建物である場合における当該附属建物が属する一棟の建物の所在、構造、床面積及び名称』『附属建物が区分建物である場合における敷地権の内容』。記事にない整理。
- 不動産登記規則別表三（区分建物である建物の登記記録。同ファイル）：所在欄があるのは『一棟の建物の表示欄』で、『専有部分の建物の表示欄』に所在欄はない。附属建物の表示欄の構造欄は『附属建物の構造』『附属建物が区分建物である場合におけるその一棟の建物の所在、構造、床面積及び名称』『附属建物が区分建物である場合における敷地権の内容』で、区分建物でない附属建物の所在を書く欄の定めは見当たらない（記事アの『実務の取扱い』のとおり）。
- 不動産登記法第44条第1項第1号・第5号（note-articles/laws/fudousan-touki-hou.md）：第1号は、区分建物である建物の所在を『当該建物が属する一棟の建物の所在する…土地の地番』とする。第5号は、附属建物があるときその所在する…土地の地番（区分建物である附属建物は、その属する一棟の建物の所在する…地番）並びに種類、構造及び床面積を登記事項とする。記事にない整理。
- R04-Q14ウ（note-articles/r4-mondai/q14-fuzoku-tatemono.md）：附属建物が別の一棟に属する区分建物のときは、一棟の建物の所在地番・構造・床面積・名称・敷地権などを附属建物の構造欄に加えて記録する。同じ記事に準則第89条（同一の一棟に属するときは記録を要しない）の記述があるため、図の第3の行は『別の一棟の建物に属する区分建物』と限定した。

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both very small; in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall). Between panel 4 and the conclusion banner, a thin one-line note strip (about 50 px tall) with small text, as given in the NOTE LINE below.

TITLE BANNER: text 「区分建物の附属建物の所在は、構造欄に書く」 in large bold letters; the part 「構造欄に書く」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　所在は、どの別表で見る？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center region: one flat apartment-building icon with one room window highlighted, labeled 「区分建物の一室」, and beside it one small flat garden-shed icon labeled 「区分建物でない附属建物」, side by side with a clear gap between them. No arrow and no connecting line between the two icons.
- Under the two icons, one wide white card with a dark navy outline and a dark navy heading 「規則第4条　登記記録の編成」, with two body lines: 「区分建物でない建物は、別表二」 and 「区分建物は、別表三」, the part 「別表三」 with a yellow highlighter marker.
- A small question badge 「附属建物の所在は、どの欄？」 with a pale gray fill and a dark navy outline sits at the top of the center region (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「所在は、所在欄に
書きますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。区分建物は
別表三を見なさい」 with the part 「別表三」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　別表で、書く欄が決まる」
- A full-width concept diagram fills the whole panel. At the top, a three-row table with a dark navy header row with white text: left column 「場面」, right column 「所在などを書く欄」. All body cells have the same pale gray fill and a dark navy outline, each text at least 24 px high; there is no check mark, no cross, and no arrow anywhere in this panel.
- Row 1: left cell 「区分建物でない建物」 with a small dark navy tag 「別表二」, right cell 「主である建物の所在欄に、附属建物の所在も含めて記録」.
- Row 2: left cell 「区分建物」 with a small dark navy tag 「別表三」, right cell 「所在は一棟の建物の所在欄。専有部分の表示欄に所在欄はない」.
- Row 3: left cell 「附属建物が区分建物」 with a small dark navy tag 「別表二・別表三」, right cell 「附属建物の構造欄に、一棟の建物の所在・構造・床面積・名称も記録」.
- The three rows have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- At the bottom, one wide dark navy band with white text 「同じ所在でも、別表二と別表三で書く欄が違う」, the part 「書く欄が違う」 in a yellow highlighter marker.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　別表三の読み方」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Two cards stacked from top to bottom, both the same size, each with a pale gray fill, a dark navy outline, and a dark navy heading, with no check mark and no cross. The two cards are separated only by a small empty gap, with nothing drawn between them.
- Top card, heading 「別表三の専有部分」, two body lines: 「専有部分の表示欄に、所在欄はない」, 「所在は、一棟の建物の表示欄にある」.
- Bottom card, heading 「区分建物でない附属建物の所在」, two body lines: 「登記事項だが、別表三に欄の定めなし」, 「実務の取扱いで、構造欄に記録」. Under the two cards, a dark navy ribbon tag with large white text 「ひっかけ：所在なのに、構造欄」.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「構造欄に所在なんて、
変ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。専有部分に
所在欄はないのよ」 with the part 「所在欄はない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、物置の所在は
どこですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「別表三に定めはなく、
実務で構造欄に書くのよ」 with the part 「構造欄」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「欄は、別表で
決まるんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。まず別表二か
三かを見るのよ」 with the part 「別表二か三か」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「区分建物でない建物は別表二。所在欄に附属建物の所在も含む」, 「区分建物は別表三。専有部分の表示欄に所在欄はない」, 「区分建物でない附属建物の所在は、構造欄に記録される」.

NOTE LINE (small text on a thin strip between panel 4 and the conclusion banner, one line, fully legible): 「区分建物でない附属建物の所在を構造欄に書く点は、別表三に定めがなく実務の取扱い」

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「区分建物の附属建物の所在は、構造欄に記録される」 with a yellow highlighter marker.
- Line 2: 「問題D1762　正解〇（R04-Q11ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 建, 所, 物, 登, 規, 解, 記, 違, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 附属建物の所在は | 薄い黄色のマーカー |
| タイトル2行目 | どの欄に書く？ | 「どの欄に書く？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1762　R04-Q11ア | — |

### 見出し画像プロンプト本体

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief), placed at the lower left of center. 藍子 is the young woman exam candidate (long wavy brown hair, pinstriped light-blue blouse with rolled sleeves, navy pencil skirt, no jacket), placed at the lower right of center. POSES ARE NOT FIXED: do not copy any pose from the attached images or from earlier header images; let each character take a free, natural pose of your own choosing that fits the topic and suits the character (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep both characters fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
附属建物の所在は
Line 2 is larger; the phrase どの欄に書く？ is red-orange and the rest is dark navy:
どの欄に書く？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1762　R04-Q11ア
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a condominium building with a small garden shed beside it
Right side: an open registry book with blank form fields and a magnifying glass

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 附, 属, 建, 物, 所, 在, 欄, 書, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

### 見出し画像の検品
- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の表と一字一句一致、簡体字・余計な文字なし
- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり
- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない
- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない

## 画像ファイル名（名づけルール）

ChatGPTで生成した画像は、保存するときに次の名前へ変更する（拡張子は生成された形式のまま：png・webp など）。`MANGA_RULES.md` の「画像ファイル名」に従う。

| 画像 | ファイル名 |
|---|---|
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1762～R04-Q11ア～.png |
| 見出し画像（採用版） | 4コマ解説図解D1762～R04-Q11ア～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1762～R04-Q11ア～_v01.png ／ 4コマ解説図解D1762～R04-Q11ア～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1762_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の図で、マンションの一室（区分建物）に庭先の物置（区分建物でない附属建物）が付いていて、規則第4条により区分建物は別表三を見ることが言える。コマ2の表で、別表二（所在欄に附属建物の所在も含める）と別表三（専有部分に所在欄がなく、所在は一棟の建物の所在欄）の違いと、附属建物が区分建物のときの構造欄の中身が言える
- [ ] 工程C：肝の確認：①区分建物でない建物は別表二で、主である建物の所在欄に附属建物の所在も含める ②区分建物は別表三で、専有部分の建物の表示欄に所在欄がなく、所在は一棟の建物の表示欄 ③区分建物でない附属建物の所在は、別表三に書く欄の定めがなく、実務の取扱いで構造欄 ④附属建物が区分建物なら、構造欄に一棟の建物の所在・構造・床面積・名称も記録 ⑤したがって本肢は〇
- [ ] 工程C：構成表の全文言を、記事R04-Q11アと法令DB（規則第4条、別表二、別表三、法第44条第1項）に照らして確認：『所在（附属建物の所在を含む。）』『専有部分の建物の表示欄に所在欄はない』『附属建物が区分建物である場合におけるその一棟の建物の所在、構造、床面積及び名称』『実務の取扱い』。条文番号は規則第4条（第2項・第3項）と別表二・別表三だけを図に入れた
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（side→none→faces→既定）

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

- 2026-10-10 v02：条文（規則別表二・別表三）を主役にして作り直し（先の版〈肢の理由中心〉と結論は同じ。コマ1で規則第4条の振り分け、コマ2で別表二・別表三の欄の当てはめ表を主題にした。型は型2＋型3の理由）
