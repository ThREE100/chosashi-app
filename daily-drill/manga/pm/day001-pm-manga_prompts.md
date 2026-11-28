# 毎日ドリル 第1日（夜）記述式 PM-01 学習まんがの画像プロンプト

記事：`day001-pm-manga.md`。問題：`daily-drill/evening/problems/PM-01.json`（座標・答えはここから）。全20ページ、1ページ＝1枚（1024×1536）。
図は Claude が問題データから作った正確な図（`fig/`）。漫画の中にそのまま置かせ、画像生成AIに描き直させない。

ChatGPT・Codexには、キャラクターシート_トリ先生_01〜03 と キャラクターシート_I-01〜03 の6枚を添付する（シートはリポジトリにない）。「鳥が先生、女性が生徒です。名前は画像に書かないでください」と添えてから、1ページずつ貼る。2ページ目からは同じチャットで続ける。

ファイル名：`毎晩ドリル漫画_Day001_p01.png`〜`_p20.png`、見出し画像 `毎晩ドリル漫画_Day001_見出し_note.png`／`_見出し_IG.png`。

## 差し込む図（Claudeが作った正確な図。描き直させない）

| ページ | 図のファイル | 置く枠（x, y, 幅, 高さ px） | URL |
|---|---|---|---|
| 2 | `PM-01_mondai.png` | 40, 110, 944, 661 | https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_mondai.png |
| 4 | `PM-01_housha.png` | 158, 110, 708, 496 | https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_housha.png |
| 7 | `PM-01_vector.png` | 158, 110, 708, 496 | https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_vector.png |
| 13 | `PM-01_kouten.png` | 40, 380, 944, 661 | https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_kouten.png |
| 14 | `PM-01_zahyou.png` | 158, 110, 708, 496 | https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_zahyou.png |
| 19 | `PM-01_kotae.png` | 40, 110, 944, 661 | https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_kotae.png |

図のあるページは、その図のPNGも添付してから貼る。生成された画像で図が崩れたら、`tools/gakushu_manga/paste_fig.py` で正確な図を枠に貼り直す。

## 1ページ目：扉：3つの点と地積を出す

ねらい：問いを1枚の絵で見せ、生徒が自信満々で罠に向かう姿で興味を引く。

```
Draw page 1 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

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
Draw page 2 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

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
Draw page 3 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

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

## 4ページ目：放射①：後視の向きを出す

ねらい：放射の出発点になる「T1から見たT2の向き」を、引き算と arg で出す。

```
Draw page 4 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

ATTACHED FIGURE(S) FOR THIS PAGE: 「PM-01_housha.png」 (exact diagrams to be pasted in unchanged; they are not character sheets).

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: one large panel on top holding an exact figure, a wide whiteboard panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (large, top): A clean panel with only the attached exact figure in it.
      FIGURE SLOT (critical): the attached image 「PM-01_housha.png」 (the same file is at https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_housha.png) is an exact figure made in advance. Inside this panel, keep a white rectangle exactly 708x496 pixels with its top-left corner at x=158, y=110 of the page, and place that image into the rectangle exactly as it is, scaled to fit the rectangle. Do NOT redraw, retrace, simplify, translate, recolor, crop, flip, or rotate it; keep every line, dot, letter, and number in it unchanged; add nothing inside the rectangle. Characters, bubbles, and narration boxes must stay outside the rectangle.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「T1に据えてT2を見る。PとQはその先」
PANEL 2 (wide, middle): A clean whiteboard with two lines of formulas in dark navy; the angle result is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「T2 − T1 ＝ −1.38 − 21.49i」、「arg(T2 − T1) ＝ −93°40′27.32″」
PANEL 3 (short strip, bottom): The student taps the whiteboard with her pencil; the teacher nods.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「マイナスの角でいいんですか？」
      - speech bubble from the TEACHER (tail points at the teacher): 「266°19′32.68″と同じ向きよ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy. The text inside an attached figure image is part of that image: keep it exactly as it is and do not add to it.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; each attached figure sits unchanged in its rectangle with nothing drawn over it; fully opaque. Deliver the first image as it is.
```

## 5ページ目：放射②：点Pの向きと座標

ねらい：後視の向きに観測角を足し、その向きに距離だけ進んで点Pを出す。

```
Draw page 5 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a wide whiteboard panel on top, a wide whiteboard panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (wide, top): A whiteboard: a clockwise arrow turning from the T2 direction, with the angle sum written beside it in dark navy.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「向き＝後視の向き＋観測角」
      words inside the drawing (exactly these, nothing else): 「−93°40′27.32″ ＋ 339°02′24″」、「＝ 245°21′56.68″」
PANEL 2 (wide, middle): The same whiteboard style; the result line is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「P ＝ T1 ＋ 10.22∠245°21′56.68″」、「＝ 541.0200… ＋ 400.3501…i」、「X 541.02　Y 400.35」
PANEL 3 (short strip, bottom): The student writes in her notebook; the teacher raises one wing.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「∠は、その向きに進むって意味？」
      - speech bubble from the TEACHER (tail points at the teacher): 「そう。10.22m進んだ先がPよ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 6ページ目：放射③：点Qと四捨五入

ねらい：点Qも同じ手順で出し、座標を小数第2位にそろえる。

```
Draw page 6 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a wide whiteboard panel on top, a wide whiteboard panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (wide, top): A whiteboard with the angle sum for the second point in dark navy.
      words inside the drawing (exactly these, nothing else): 「−93°40′27.32″ ＋ 220°13′50″」、「＝ 126°33′22.68″」
PANEL 2 (wide, middle): The same whiteboard style; the rounded result is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「Q ＝ T1 ＋ 8.04∠126°33′22.68″」、「＝ 540.4912… ＋ 416.0983…i」、「X 540.49　Y 416.10」
PANEL 3 (short strip, bottom): The student points at the last digit; the teacher nods.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「416.0983…は416.10ですね」
      - speech bubble from the TEACHER (tail points at the teacher): 「【注】の2、小数第3位で四捨五入」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 7ページ目：交点①：点Rの考え方

ねらい：点Rを「K1からK2の向きに t 本分進んだ点」と考え、t を求めればよいことをつかむ。

```
Draw page 7 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

ATTACHED FIGURE(S) FOR THIS PAGE: 「PM-01_vector.png」 (exact diagrams to be pasted in unchanged; they are not character sheets).

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: one large panel on top holding an exact figure, a wide whiteboard panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (large, top): A clean panel with only the attached exact figure in it.
      FIGURE SLOT (critical): the attached image 「PM-01_vector.png」 (the same file is at https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_vector.png) is an exact figure made in advance. Inside this panel, keep a white rectangle exactly 708x496 pixels with its top-left corner at x=158, y=110 of the page, and place that image into the rectangle exactly as it is, scaled to fit the rectangle. Do NOT redraw, retrace, simplify, translate, recolor, crop, flip, or rotate it; keep every line, dot, letter, and number in it unchanged; add nothing inside the rectangle. Characters, bubbles, and narration boxes must stay outside the rectangle.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「3本の矢印 u・v・w で考える」
PANEL 2 (wide, middle): A whiteboard with one formula in dark navy; the letter t is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「R ＝ K1 ＋ t × (K2 − K1)」、「t ＝ K1からK2の何本分か」
PANEL 3 (short strip, bottom): The student tilts her head; the teacher points at the letter t.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「tさえ分かれば、Rが出る？」
      - speech bubble from the TEACHER (tail points at the teacher): 「そう。tを2つの量の比で出すの」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy. The text inside an attached figure image is part of that image: keep it exactly as it is and do not add to it.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; each attached figure sits unchanged in its rectangle with nothing drawn over it; fully opaque. Deliver the first image as it is.
```

## 8ページ目：交点②：3本の矢印を引き算で作る

ねらい：u・v・w を、X と Y を別々に引き算して作る。

```
Draw page 8 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a wide whiteboard panel on top, a wide whiteboard panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (wide, top): A whiteboard: the first subtraction worked out in two lines, X and Y separately, in dark navy.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「uはK1からK2へ。Xの差とYの差」
      words inside the drawing (exactly these, nothing else): 「X：527.28 − 534.83 ＝ −7.55」、「Y：416.37 − 416.21 ＝ 0.16」、「u ＝ −7.55 ＋ 0.16i」
PANEL 2 (wide, middle): The same whiteboard style with two more results, each highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「v ＝ M − S ＝ −0.07 ＋ 7.03i」、「w ＝ S − K1 ＝ −13.05 − 15.35i」
PANEL 3 (short strip, bottom): The student counts on her fingers; the teacher nods.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「後ろの点から前の点を引く」
      - speech bubble from the TEACHER (tail points at the teacher): 「向きを逆にすると符号が逆よ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 9ページ目：交点③：たすき掛けで t を出す式

ねらい：Conjg(a) × b の i の係数（たすき掛け）の意味と、t の式を見せる。

```
Draw page 9 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a wide whiteboard panel on top, a wide whiteboard panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (wide, top): A whiteboard: two arrows a and b drawn from one point with a light parallelogram between them, and the formula in dark navy.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「たすき掛け＝2本の矢印の平行四辺形の面積」
      words inside the drawing (exactly these, nothing else): 「Conjg(a) × b の i の係数」、「＝ aのX × bのY − aのY × bのX」、「平行なら 0」
PANEL 2 (wide, middle): The same whiteboard style with the formula for t; the fraction is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「t ＝ (wとvのたすき掛け) ÷ (uとvのたすき掛け)」
PANEL 3 (short strip, bottom): The student looks surprised; the teacher explains with one wing raised.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「どうして割り算でtになるの？」
      - speech bubble from the TEACHER (tail points at the teacher): 「SMまでの遠さ÷1本で縮む量よ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 10ページ目：交点④：分子（w と v）

ねらい：分子のたすき掛けを、掛け算2つと引き算で手計算し、電卓の表示と照らす。

```
Draw page 10 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a wide whiteboard panel on top, a wide whiteboard panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (wide, top): A whiteboard: two multiplications and one subtraction written step by step in dark navy.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「wのXとvのY、wのYとvのXを掛ける」
      words inside the drawing (exactly these, nothing else): 「(−13.05) × 7.03 ＝ −91.7415」、「(−15.35) × (−0.07) ＝ 1.0745」、「−91.7415 − 1.0745 ＝ −92.816」
PANEL 2 (wide, middle): A calculator display drawn as a plain rectangle showing one line; the part after the minus sign before i is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「Conjg(S − K1) × (M − S)」、「−106.997 − 92.816i」
PANEL 3 (short strip, bottom): The student compares her notebook with the display; the teacher nods.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「iの係数が手計算と同じ！」
      - speech bubble from the TEACHER (tail points at the teacher): 「実数の部分は使わないのよ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 11ページ目：交点⑤：分母（u と v）

ねらい：分母のたすき掛けも同じ手順で出し、電卓の表示と照らす。

```
Draw page 11 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a wide whiteboard panel on top, a wide whiteboard panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (wide, top): A whiteboard: two multiplications and one subtraction written step by step in dark navy.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「uのXとvのY、uのYとvのXを掛ける」
      words inside the drawing (exactly these, nothing else): 「(−7.55) × 7.03 ＝ −53.0765」、「0.16 × (−0.07) ＝ −0.0112」、「−53.0765 − (−0.0112) ＝ −53.0653」
PANEL 2 (wide, middle): A calculator display drawn as a plain rectangle showing one line; the part before i is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「Conjg(K2 − K1) × (M − S)」、「1.6533 − 53.0653i」
PANEL 3 (short strip, bottom): The student underlines a minus sign twice; the teacher raises one wing.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「マイナスを引くと足し算だ」
      - speech bubble from the TEACHER (tail points at the teacher): 「符号の取り違えが一番多いわ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 12ページ目：交点⑥：t と点R

ねらい：t を割り算で出し、u に掛けて K1 に足し、点Rを出す。

```
Draw page 12 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a wide whiteboard panel on top, a wide whiteboard panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (wide, top): A whiteboard: the division and the two multiplications in dark navy; the value of t is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「t ＝ −92.816 ÷ −53.0653 ＝ 1.7490…」、「X：−7.55 × t ＝ −13.2056…」、「Y：0.16 × t ＝ 0.2798…」
PANEL 2 (wide, middle): The same whiteboard style; the final rounded result is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「R ＝ K1 ＋ t × u」、「＝ 521.6243… ＋ 416.4898…i」、「X 521.62　Y 416.49」
PANEL 3 (short strip, bottom): The student writes the answer; the teacher nods.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「マイナスどうしの割り算で正」
      - speech bubble from the TEACHER (tail points at the teacher): 「K1の座標に足すのを忘れないで」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 13ページ目：交点⑦：点Rを図で確かめる

ねらい：求めた点Rが2本の直線の交点にあることを、正確な図と t の大きさで確かめる。

```
Draw page 13 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

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
      - speech bubble from the STUDENT (tail points at the student): 「東の筆界はブロック塀の線？」
      - speech bubble from the TEACHER (tail points at the teacher): 「塀は筆界の根拠にしないの」
PANEL 2 (large, middle): A clean panel with only the attached exact figure in it.
      FIGURE SLOT (critical): the attached image 「PM-01_kouten.png」 (the same file is at https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_kouten.png) is an exact figure made in advance. Inside this panel, keep a white rectangle exactly 944x661 pixels with its top-left corner at x=40, y=380 of the page, and place that image into the rectangle exactly as it is, scaled to fit the rectangle. Do NOT redraw, retrace, simplify, translate, recolor, crop, flip, or rotate it; keep every line, dot, letter, and number in it unchanged; add nothing inside the rectangle. Characters, bubbles, and narration boxes must stay outside the rectangle.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「直線K1K2と直線SMの交点が点R」
PANEL 3 (wide, bottom): The teacher points at the figure with one wing; the student nods.
      characters: student left, teacher right
      - speech bubble from the TEACHER (tail points at the teacher): 「tが1より大きい＝K2の先」
      - speech bubble from the STUDENT (tail points at the student): 「だからRはK2より南なんだ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy. The text inside an attached figure image is part of that image: keep it exactly as it is and do not add to it.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; each attached figure sits unchanged in its rectangle with nothing drawn over it; fully opaque. Deliver the first image as it is.
```

## 14ページ目：座標法①：順番と式

ねらい：座標法の式の形と、点を回る順番（P→Q→R→S→P）を正確な図で見せる。

```
Draw page 14 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

ATTACHED FIGURE(S) FOR THIS PAGE: 「PM-01_zahyou.png」 (exact diagrams to be pasted in unchanged; they are not character sheets).

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: one large panel on top holding an exact figure, a wide whiteboard panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (large, top): A clean panel with only the attached exact figure in it.
      FIGURE SLOT (critical): the attached image 「PM-01_zahyou.png」 (the same file is at https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_zahyou.png) is an exact figure made in advance. Inside this panel, keep a white rectangle exactly 708x496 pixels with its top-left corner at x=158, y=110 of the page, and place that image into the rectangle exactly as it is, scaled to fit the rectangle. Do NOT redraw, retrace, simplify, translate, recolor, crop, flip, or rotate it; keep every line, dot, letter, and number in it unchanged; add nothing inside the rectangle. Characters, bubbles, and narration boxes must stay outside the rectangle.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「P→Q→R→Sと回って、Pに戻る」
PANEL 2 (wide, middle): A whiteboard with the formula in dark navy; the words next point and previous point are highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「倍面積 ＝ 各点の X ×（次の点の Y − 前の点の Y）の合計」、「使うのは小数第2位の座標」
PANEL 3 (short strip, bottom): The student traces the loop with her finger; the teacher nods.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「Pの前の点はSですね」
      - speech bubble from the TEACHER (tail points at the teacher): 「そう。1周つながっているの」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy. The text inside an attached figure image is part of that image: keep it exactly as it is and do not add to it.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; each attached figure sits unchanged in its rectangle with nothing drawn over it; fully opaque. Deliver the first image as it is.
```

## 15ページ目：座標法②：Yの差を4つ出す

ねらい：各点について「次の点の Y − 前の点の Y」を出し、合計が0になる検算を見せる。

```
Draw page 15 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Two panels: one large whiteboard panel filling the top 75 percent, and a short strip at the bottom.

## 3. Panels
PANEL 1 (large, top 75 percent): A whiteboard table with four rows, one per point, in dark navy; each result is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「P：416.10 − 400.86 ＝ 15.24」、「Q：416.49 − 400.35 ＝ 16.14」、「R：400.86 − 416.10 ＝ −15.24」、「S：400.35 − 416.49 ＝ −16.14」
PANEL 2 (short strip, bottom): The student adds the four results; the teacher smiles.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「4つ足すと0になる！」
      - speech bubble from the TEACHER (tail points at the teacher): 「それがYの差の検算よ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 2 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 16ページ目：座標法③：掛けて足す

ねらい：各点の X に Y の差を掛け、4つを足して倍面積を出す。

```
Draw page 16 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Two panels: one large whiteboard panel filling the top 75 percent, and a short strip at the bottom.

## 3. Panels
PANEL 1 (large, top 75 percent): A whiteboard with four multiplication lines and a total line under a ruled line, in dark navy; the total is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「541.02 × 15.24 ＝ 8245.1448」、「540.49 × 16.14 ＝ 8723.5086」、「521.62 × (−15.24) ＝ −7949.4888」、「521.78 × (−16.14) ＝ −8421.5292」、「合計 597.6354」
PANEL 2 (short strip, bottom): The student circles the total; the teacher raises one wing.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「これで面積？」
      - speech bubble from the TEACHER (tail points at the teacher): 「まだ倍面積。2で割るのよ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 2 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 17ページ目：座標法④：2で割って切り捨て

ねらい：倍面積を2で割り、地積の端数を【注】の2どおり切り捨てる。誤答で確かめる。

```
Draw page 17 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a wide panel on top, two medium panels side by side in the middle, and a wide panel at the bottom.

## 3. Panels
PANEL 1 (wide, top): A whiteboard showing the division in dark navy.
      words inside the drawing (exactly these, nothing else): 「597.6354 ÷ 2 ＝ 298.8177 ㎡」
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

## 18ページ目：座標法⑤：電卓なら対角線で1回

ねらい：四角形の倍面積を、対角線2本のたすき掛け1回で出す別解を見せ、同じ数になることを確かめる。

```
Draw page 18 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

## 1. Art style and characters
Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, its characters, gadgets, or logos.
THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.
THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big (confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.
Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.
NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is shown only by the character and the tail of the bubble.

## 2. Page layout
Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. Three panels: a wide whiteboard panel on top, a wide calculator panel in the middle, and a short strip at the bottom.

## 3. Panels
PANEL 1 (wide, top): A whiteboard: a quadrilateral with its two diagonals drawn as arrows, and the two subtractions in dark navy.
      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「対角線は R − P と S − Q」
      words inside the drawing (exactly these, nothing else): 「R − P ＝ −19.40 ＋ 16.14i」、「S − Q ＝ −18.71 − 15.24i」
PANEL 2 (wide, middle): A calculator display drawn as a plain rectangle showing one line; the part before i is highlighted in yellow.
      words inside the drawing (exactly these, nothing else): 「Conjg(R − P) × (S − Q)」、「117.0004 ＋ 597.6354i」
PANEL 3 (short strip, bottom): The student points at the display, delighted; the teacher nods.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「iの係数が、さっきの合計と同じ」
      - speech bubble from the TEACHER (tail points at the teacher): 「四角形ならこれが速いわ」

## 4. Text rules
The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.

## 5. Quality check (apply silently while drawing)
Exactly 3 panels in the described layout; every string exactly as written and nothing else; no name or role word; every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is.
```

## 19ページ目：答えの図

ねらい：求めた3つの点を、正確な答えの図と座標で確かめる。

```
Draw page 19 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

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

## 20ページ目：まとめ：この問題のポイント

ねらい：結論・覚え方を1ページにまとめ、生徒が自分の言葉で言い直す。

```
Draw page 20 of 20 of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly 1024x1536 pixels (2:3 portrait), full color, fully opaque background.

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
      words inside the drawing (exactly these, nothing else): 「この問題のポイント」、「観測角は後視の向きに時計回りに足す」、「交点は t ＝ たすき掛けの比」、「R ＝ K1 ＋ t × (K2 − K1)」、「座標法は小数第2位の座標で」、「地積は切り捨てて298.81㎡」
PANEL 2 (wide, bottom): The student, relieved and determined, holds her pencil up; the teacher smiles warmly with wings on hips.
      characters: student left, teacher right
      - speech bubble from the STUDENT (tail points at the student): 「式の形と符号、もう迷いません！」
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
