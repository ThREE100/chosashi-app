# 「4コマで解説！調査士試験の間違えやすい肢」マガジン：タイトル・説明文・見出し画像プロンプト（案A採用・v01）

## マガジン設定（noteの入力欄へそのまま貼る）
- マガジンタイトル（30字以内・無料／有料共通）：`4コマで解説！調査士試験の間違えやすい肢`
- 見出し画像：下の「見出し画像」を無料版・有料版で共通に使う。
- どちらの版も、公開前に最新のnoteヘルプで価格設定・審査などの条件を確認する。

### 無料版（販売設定：無料）
- 種類：無料
- マガジンの説明（400字以内）：

```
土地家屋調査士試験の択一式で、何度も間違えてしまう肢（選択肢）を、トリ先生と藍子の4コマで解説するマガジンです。藍子が「つい信じてしまう思い込み」を出し、トリ先生がそれを正す流れで、①よくある誤解、②事案の整理、③似た制度との違い、④結論の4コマにまとめています。1枚ずつ見れば、どこでつまずいたのかがすぐ見返せます。解説は、このシリーズの解説記事（現行法令を基準）に沿っています。更新は不定期で、1つの肢につき4コマ漫画を追加していきます。択一式の復習や、直前期の「間違いノート」として使ってください。
```

### 有料版（販売設定：有料（単体）＝買い切り）
- 種類：有料（単体）。更新が不定期なので、月額・毎月の更新義務がある定期購読ではなく単体を選ぶ。
- 単体は、購入後に追加された記事も追加料金なしで読める（購入後に価格が変わっても買い直し不要）。このため説明文に、①更新は不定期　②追加分は追加料金なし　③現在の収録数、の3点を書く。
- 価格を後から上げる運用をするなら、「今後、記事が増えたら価格を見直すことがあります」の一文を【更新について】に足す。
- 参考：noteヘルプ「有料マガジンと定期購読マガジンの違い」https://www.help-note.com/hc/ja/articles/360000326262
- マガジンの説明（400字以内。「現在○本」は公開時の数に差し替える）：

```
土地家屋調査士試験の択一式で、何度も間違えてしまう肢（選択肢）を、トリ先生と藍子の4コマで解説するマガジンです。藍子が「つい信じてしまう思い込み」を出し、トリ先生がそれを正す流れで、①よくある誤解、②事案の整理、③似た制度との違い、④結論の4コマにまとめています。解説は、このシリーズの解説記事（現行法令を基準）に沿っています。

【更新について】更新は不定期で、1つの肢につき4コマ漫画を1つずつ追加していきます（現在○本）。買い切り（有料・単体）のため、購入後に追加された記事も追加料金なしで読めます。

【こんな方に】択一式の復習や、直前期の「間違いノート」として使いたい方へ。
```

## 見出し画像（1280×670px）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（トリ先生・藍子。`CHATGPT_MANGA_WORKFLOW.md` §3の6枚）** を添付して下のコードブロックを貼る。どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添える。
- 構成表（文言の正本。`check_prompt.py` が読む）：

| 領域 | 用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル1行目 | 見出し | 「4コマで解説！」 | 「4コマ」を黄色マーカー |
| タイトル2行目 | サブ | 「間違えやすい肢」 | — |

- 画像内の文字は次の2つだけ（正本）：1行目「4コマで解説！」（「4コマ」は半角数字＋カタカナ。「4コマ」全体に黄色マーカー）／2行目「間違えやすい肢」。
- マガジンヘッダーとして実際に表示されるのは縦中央の216px（y=227〜443）のみ。タイトルとキャラはこの帯に収める（既存の `note-articles/mistake-notebook-magazine.md` と同じ仕様）。
- ChatGPTが1280×670を出せない場合：横長（約1.91:1）で生成させ、1280×670へリサイズ・トリミングする。帯は画像の高さの約33.9%〜66.1%の範囲。トリミング後に帯の中の顔・文字が切れていないかを確認する。

```text
Create a landscape magazine header image, EXACTLY 1280x670 pixels (aspect ratio about 1.91:1), in a clean, warm, flat digital illustration style (simple outlines, soft pastel colors) for a note.com magazine of four-panel comic explanations about the Japanese 土地家屋調査士 (land and house surveyor) exam.

CANVAS SAFE-ZONE REQUIREMENT (critical): Only the vertical center band from y=227px to y=443px (a 216px-tall strip across the full 1280px width) is visible when this image is shown as the magazine header. The title text, both characters' faces and upper bodies, and all four comic frames MUST be fully contained inside this band. Everything above y=227px and below y=443px is a soft, low-contrast, low-detail decorative background only (no text, no characters, no important detail), but the whole 1280x670 canvas must still look complete and balanced.

CRITICAL TEXT REQUIREMENT: The ONLY text in the whole image is the two strings below. All text must be standard Japanese (katakana, hiragana, joyo kanji, and the Arabic numeral 4). Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Reproduce the strings verbatim; do not paraphrase, shorten, or add any other text, signs, labels, captions, logos, or watermarks anywhere.
  Line 1: 「4コマで解説！」
  Line 2: 「間違えやすい肢」

BACKGROUND REQUIREMENT (critical): The entire 1280x670 canvas is fully opaque from edge to edge, in a soft warm cream/beige tone. Do NOT generate a transparent or alpha-channel background; no checkerboard, no partially transparent area, no unpainted edge.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters; reproduce them faithfully (same face, body shape, clothing, colors, proportions, drawing style) and do not redesign them. (1) 「藍子」: a serious, earnest young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil. (2) 「トリ先生」: a plump, round bird character who is a sharp-tongued but caring exam teacher. Do not add any other character.

COMPOSITION (inside the safe band y=227-443): Draw a horizontal four-panel comic strip as if on white manuscript paper: FOUR white rectangular panel frames in one row, evenly spaced across the width with thin dark outlines and narrow gutters, each frame about 290px wide and 190px tall, vertically centered in the band.
- Panel 1 (leftmost): 藍子, upper body, looking confident and a little smug (chin up, small proud smile, one hand on her chest). Above her, on her side of the frame, a round speech bubble containing only a large BLUE circle mark (symbol only, no text); the bubble tail points to 藍子's mouth.
- Panels 2 and 3 (middle): both are quiet and light. Panel 2 holds a small flat icon of a document with a sparkle; panel 3 holds a small flat icon of a notebook with a magnifying glass. No text inside them. A large, soft-white rounded title ribbon with a thin warm-yellow border and a subtle drop shadow lies across the center, overlapping panels 2 and 3 but staying fully inside the band, containing the two title lines stacked and centered: Line 1 「4コマで解説！」 in very large, bold, dark navy Japanese letters with a bright yellow highlighter-marker stripe behind the whole of 「4コマ」 only; Line 2 「間違えやすい肢」 directly below, smaller but still bold and easily readable, in dark navy. The title text must be crisp and large enough to read on a phone.
- Panel 4 (rightmost): トリ先生, exasperated and a little weary (half-closed eyes, a wing pressed to the forehead or on the hip, a small sweat-drop). Above him, on his side of the frame, a round speech bubble containing only a large RED cross mark (symbol only, no text); the bubble tail points to トリ先生's mouth.
Speech bubbles stay on the same side as their speaker and each tail points at its own speaker only. Color rule: affirmative marks and check marks are BLUE, and negative marks and crosses are RED; use dark navy for neutral outlines and text. Keep the characters' size consistent with each other and do not let the title ribbon cover either character's face.

Final check before rendering: confirm the image contains exactly two text strings, 「4コマで解説！」 and 「間違えやすい肢」, and nothing else; confirm the kanji 解, 説, 間, 違, 肢 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm exactly four comic panels in one horizontal row; confirm the title, both faces and all four frames are inside the y=227-443 band; confirm both characters match the attached references and each speech-bubble tail points at its own speaker; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 生成後の検品
- [ ] 文字は「4コマで解説！」「間違えやすい肢」の2つだけ。誤字・簡体字・余計な文字なし
- [ ] 黄色マーカーは「4コマ」だけにかかっている
- [ ] 4コマの枠が横一列に4つ、帯（y=227〜443）の中に収まっている
- [ ] 藍子（左・自信満々＋青○）、トリ先生（右・呆れ顔＋赤×）、吹き出しの尾が各話者を向く
- [ ] 2キャラが参照画像どおり、背景が不透明
- [ ] 1280×670にした後も、顔・タイトルが帯から切れていない（一覧ページでは1280×454の範囲が表示されることも考慮）
