# 毎日ドリル 第1日（夜）記述式 PM-01 学習まんがの画像プロンプト

記事：`day001-pm-manga.md`。問題：`daily-drill/evening/problems/PM-01.json`（座標・答えはここから）。全8ページ、1ページ＝1枚（1024×1536）。
図は Claude が問題データから作った正確な図（`fig/`）。漫画の中にそのまま置かせ、画像生成AIに描き直させない。

ChatGPT・Codexには、キャラクターシート_トリ先生_01〜03 と キャラクターシート_I-01〜03 の6枚を添付する（シートはリポジトリにない）。「鳥が先生、女性が生徒です。名前は画像に書かないでください」と添えてから、1ページずつ貼る。2ページ目からは同じチャットで続ける。

ファイル名：`毎晩ドリル漫画_Day001_p01.png`〜`_p08.png`、見出し画像 `毎晩ドリル漫画_Day001_見出し_note.png`／`_見出し_IG.png`。

## 差し込む図（Claudeが作った正確な図。描き直させない）

| ページ | 図のファイル | 置く枠（x, y, 幅, 高さ px） | URL |
|---|---|---|---|
| 2 | `PM-01_mondai.png` | 40, 110, 944, 661 | https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_mondai.png |
| 5 | `PM-01_kouten.png` | 40, 380, 944, 661 | https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_kouten.png |
| 7 | `PM-01_kotae.png` | 40, 110, 944, 661 | https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_kotae.png |

図のあるページは、その図のPNGも添付してから貼る。生成された画像で図が崩れたら、`tools/gakushu_manga/paste_fig.py` で正確な図を枠に貼り直す。

## 1ページ目：扉：3つの点と地積を出す

ねらい：問いを1枚の絵で見せ、生徒が自信満々で罠に向かう姿で興味を引く。

```
Draw page 1 of 8 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Two panels: one very large title panel filling the top three quarters of the page, and one wide short strip panel across the bottom.

## 3. Panels
PANEL 1 (very large, top three quarters): Title page. The student sits at a study desk holding a big question card, smiling confidently. The bird teacher peeks in from the right edge with narrowed eyes. Large title lettering at the top in dark navy with the key word on a yellow highlighter band; the question is written on the card.
      characters: student at center-left (large), teacher peeking from the right edge
      words inside the drawing (exactly these, nothing else): 「3つの点と地積を出す」、「点P・Q・Rの座標と、12番の地積は？」
PANEL 2 (wide short strip across the bottom): The student gives a confident thumbs-up; the teacher crosses his wings, unimpressed.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「放射で全部出せます！」
      - speech bubble from the TEACHER (tail points at the teacher): 「……Rも放射で？」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 2 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 2ページ目：図で見る：求める3つの点

ねらい：問題の図（正確な図）で、与えられた点と求める点を見分ける。

```
Draw page 2 of 8 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

ATTACHED FIGURE(S) FOR THIS PAGE: 「PM-01_mondai.png」 (exact diagrams to be pasted in unchanged; they are not character sheets).

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: one tall panel filling the top 60 percent of the page holding an exact figure, a wide panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (tall, top 60 percent): A clean panel with only the attached exact figure in it.
      FIGURE SLOT (critical): the attached image 「PM-01_mondai.png」 (the same file is at https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_mondai.png) is an exact figure made in advance. Inside this panel, keep a white rectangle exactly 944x661 pixels with its top-left corner at x=40, y=110 of the page, and place that image into the rectangle exactly as it is, scaled to fit the rectangle. Do NOT redraw, retrace, simplify, translate, recolor, crop, flip, or rotate it; keep every line, dot, letter, and number in it unchanged; add nothing inside the rectangle. Characters, bubbles, and narration boxes must stay outside the rectangle.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「12番の土地と、求める3つの点」
PANEL 2 (wide, middle): The teacher points up at the figure with one wing; the student leans in.
      characters: student left, teacher right
      - speech bubble from the TEACHER (tail points at the teacher): 「黒丸が与えられた点、赤い白丸が求める点」
      - speech bubble from the STUDENT (tail points at the student): 「PとQはT1から観測した点ですね」
PANEL 3 (short strip, bottom): The teacher holds up one feather like a pointer.
      characters: teacher only
      - speech bubble from the TEACHER (tail points at the teacher): 「Rは2本の直線の交点。順に出すわ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy. The text inside an attached figure image is part of that image: keep it exactly as it is and do not add to it.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; each attached figure sits unchanged in its rectangle with nothing drawn over it; fully opaque. Deliver the first image as it is.
```

## 3ページ目：つまずき：観測角の向き

ねらい：生徒が誤答し、先生が止める。読者も一緒に立ち止まる。

```
Draw page 3 of 8 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: two small panels side by side on top, and one very large panel filling the bottom two thirds.

## 3. Panels
PANEL 1 (small, top left): The student points at the question card confidently.
      characters: student only
      - speech bubble from the STUDENT (tail points at the student): 「T2から反時計回りに引きます！」
PANEL 2 (small, top right): The bird teacher flaps both wings in a dramatic STOP gesture, with speed lines.
      characters: teacher only
      - speech bubble from the TEACHER (tail points at the teacher): 「待ちなさい！」
PANEL 3 (very large, bottom two thirds): The teacher holds up a giant card toward the reader; the student, on the left, sweats and leans back in surprise. On the card, an instrument at T1 with an arrow from T2 turning clockwise, drawn in blue; a crossed-out counterclockwise arrow in red.
      characters: student left, teacher right, both medium size
      - speech bubble from the TEACHER (tail points at the teacher): 「【条件】の2を読んで。どっち回り？」
      - speech bubble from the STUDENT (tail points at the student): 「時計回り……足すんだ！」
      words inside the drawing (exactly these, nothing else): 「水平角は後視T2から時計回り」、「足す」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 4ページ目：放射で点Pと点Q

ねらい：放射の式を、表の観測値どおりに書いて答えを出す。

```
Draw page 4 of 8 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a wide panel on top, a wide panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (wide, top): A clean whiteboard with the formula and its result written in dark navy; the result is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「点P ＝ T1 ＋ 10.22∠(arg(T2 − T1) ＋ 339°02′24″)」、「541.02 ＋ 400.35i」
PANEL 2 (wide, middle): The same whiteboard style with the second formula and its result highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「点Q ＝ T1 ＋ 8.04∠(arg(T2 − T1) ＋ 220°13′50″)」、「540.49 ＋ 416.10i」
PANEL 3 (short strip, bottom): The student writes the results; the teacher nods.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「後視の向きに、角を足すだけ！」
      - speech bubble from the TEACHER (tail points at the teacher): 「距離と角は表のとおりにね」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 5ページ目：点Rは2本の直線の交点

ねらい：ブロック塀ではなく地積測量図の直線で筆界を決め、交点として点Rを出す。

```
Draw page 5 of 8 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

ATTACHED FIGURE(S) FOR THIS PAGE: 「PM-01_kouten.png」 (exact diagrams to be pasted in unchanged; they are not character sheets).

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a short strip on top, one large panel in the middle holding an exact figure, and a wide panel at the bottom.

## 3. Panels
PANEL 1 (short strip, top): The student points at a drawing of a block wall; the teacher shakes his head.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「東の筆界はブロック塀の線ですね？」
      - speech bubble from the TEACHER (tail points at the teacher): 「塀は筆界の根拠にしないの」
PANEL 2 (large, middle): A clean panel with only the attached exact figure in it.
      FIGURE SLOT (critical): the attached image 「PM-01_kouten.png」 (the same file is at https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_kouten.png) is an exact figure made in advance. Inside this panel, keep a white rectangle exactly 944x661 pixels with its top-left corner at x=40, y=380 of the page, and place that image into the rectangle exactly as it is, scaled to fit the rectangle. Do NOT redraw, retrace, simplify, translate, recolor, crop, flip, or rotate it; keep every line, dot, letter, and number in it unchanged; add nothing inside the rectangle. Characters, bubbles, and narration boxes must stay outside the rectangle.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「直線K1K2と直線SMの交点が点R」
PANEL 3 (wide, bottom): A whiteboard with the result highlighted in yellow; the teacher stands small at the right.
      characters: teacher small at right
      - speech bubble from the TEACHER (tail points at the teacher): 「11番と13番・14番の地積測量図の線よ」
      words inside the drawing (exactly these, nothing else): 「点R ＝ 521.62 ＋ 416.49i」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy. The text inside an attached figure image is part of that image: keep it exactly as it is and do not add to it.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; each attached figure sits unchanged in its rectangle with nothing drawn over it; fully opaque. Deliver the first image as it is.
```

## 6ページ目：地積は切り捨て

ねらい：座標法の結果から地積を出すときの端数の処理を、誤答で確かめる。

```
Draw page 6 of 8 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a wide panel on top, two medium panels side by side in the middle, and a wide panel at the bottom.

## 3. Panels
PANEL 1 (wide, top): A whiteboard showing the four points connected in order and the area result.
      words inside the drawing (exactly these, nothing else): 「P→Q→R→Sの順に座標法」、「298.8177 ㎡」
PANEL 2 (medium, middle left): The student raises her hand confidently.
      characters: student only
      - speech bubble from the STUDENT (tail points at the student): 「四捨五入して298.82㎡です！」
PANEL 3 (medium, middle right): The bird teacher flaps both wings in a STOP gesture with speed lines; a red cross over 298.82.
      characters: teacher only
      - speech bubble from the TEACHER (tail points at the teacher): 「待ちなさい！ 地積は切り捨てよ」
      words inside the drawing (exactly these, nothing else): 「298.82」
PANEL 4 (wide, bottom): A clean result card with a blue check mark.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「【注】の2：小数第2位未満は切り捨て」
      words inside the drawing (exactly these, nothing else): 「地積 298.81 ㎡」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 4 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 7ページ目：答えの図

ねらい：求めた3つの点を、正確な答えの図と座標で確かめる。

```
Draw page 7 of 8 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

ATTACHED FIGURE(S) FOR THIS PAGE: 「PM-01_kotae.png」 (exact diagrams to be pasted in unchanged; they are not character sheets).

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Two panels: one large panel filling the top 70 percent holding an exact figure, and a wide panel at the bottom.

## 3. Panels
PANEL 1 (large, top 70 percent): A clean panel with only the attached exact figure in it.
      FIGURE SLOT (critical): the attached image 「PM-01_kotae.png」 (the same file is at https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_kotae.png) is an exact figure made in advance. Inside this panel, keep a white rectangle exactly 944x661 pixels with its top-left corner at x=40, y=110 of the page, and place that image into the rectangle exactly as it is, scaled to fit the rectangle. Do NOT redraw, retrace, simplify, translate, recolor, crop, flip, or rotate it; keep every line, dot, letter, and number in it unchanged; add nothing inside the rectangle. Characters, bubbles, and narration boxes must stay outside the rectangle.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「赤丸が求めた点（X, Y）」
PANEL 2 (wide, bottom): The student holds up her answer sheet happily; the teacher gives a wing thumbs-up.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「Qは直線K1K2の延長上にもある！」
      - speech bubble from the TEACHER (tail points at the teacher): 「そう、それが検算になるの」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy. The text inside an attached figure image is part of that image: keep it exactly as it is and do not add to it.

## 5. Quality check (apply silently while drawing)
Exactly 2 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; each attached figure sits unchanged in its rectangle with nothing drawn over it; fully opaque. Deliver the first image as it is.
```

## 8ページ目：まとめ：この問題のポイント

ねらい：結論・覚え方を1ページにまとめ、生徒が自分の言葉で言い直す。

```
Draw page 8 of 8 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Two panels: one large panel filling the top two thirds, and one wide panel at the bottom.

## 3. Panels
PANEL 1 (large, top two thirds): A large summary board. At the top the heading この問題のポイント on a yellow highlighter band. Below, a checklist with blue check marks, one line each.
      words inside the drawing (exactly these, nothing else): 「この問題のポイント」、「観測角は後視から時計回りに足す」、「ブロック塀は筆界の根拠にしない」、「点Rは2本の地積測量図の直線の交点」、「地積は切り捨てて298.81㎡」
PANEL 2 (wide, bottom): The student, relieved and determined, holds her pencil up; the teacher smiles warmly with wings on hips.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「向き、根拠、端数。3つを確かめます！」
      - speech bubble from the TEACHER (tail points at the teacher): 「それで本番の点の計算も怖くないわ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 2 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 見出し画像（note用 1280×670）

```
Create a landscape note.com header image for a Japanese educational comic article, exactly 1280x670 pixels, fully opaque.

TEXT (only these three strings, exactly): line 1 on a pale yellow marker band 「毎晩ドリル　漫画で解説」; line 2 large, the key word in reddish orange 「放射と交点で筆界点を出す」; subtitle in a light-blue rounded band 「観測角は時計回り　地積は切り捨て」. No other words, digits, or Latin letters.

CHARACTERS: exactly two. THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions. Place him lower right of center. THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each. Place her lower left of center. Free, natural poses that fit the topic, different each time; both fully visible, faces clear of the title. No names or role words anywhere.

STYLE: the bird teacher's flat pastel style; the topic scene (a surveying instrument on a tripod, boundary stakes, and a plot of land seen from above) fades softly into the left and right edges with no text in it. Do not imitate any existing manga series.

Final check: only the three strings; standard Japanese kanji; exactly two characters; fully opaque. Deliver the first image as it is.
```

## 見出し画像（Instagram用 1080×1440）

```
Create a portrait Instagram (3:4) header image for a Japanese educational comic article, exactly 1080x1440 pixels, fully opaque.

TEXT (only these three strings, exactly): line 1 on a pale yellow marker band 「毎晩ドリル　漫画で解説」; line 2 large, the key word in reddish orange 「放射と交点で筆界点を出す」; subtitle in a light-blue rounded band 「観測角は時計回り　地積は切り捨て」. No other words, digits, or Latin letters.

CHARACTERS: exactly two. THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions. Place him lower right of center. THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each. Place her lower left of center. Free, natural poses that fit the topic, different each time; both fully visible, faces clear of the title. No names or role words anywhere.

STYLE: the bird teacher's flat pastel style; the topic scene (a surveying instrument on a tripod, boundary stakes, and a plot of land seen from above) fades softly into the left and right edges with no text in it. Do not imitate any existing manga series.

Final check: only the three strings; standard Japanese kanji; exactly two characters; fully opaque. Deliver the first image as it is.
```
