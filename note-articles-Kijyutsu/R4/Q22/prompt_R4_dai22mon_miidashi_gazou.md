# 画像作成プロンプト：令和4年度 第22問（建物）note見出し画像

note記事「【土地家屋調査士受験生向け】令和4年度問題22（建物）〜主と附属がつながっても合体登記じゃない〜」の**見出し画像（サムネイル）**用プロンプト。サイズ・スタイルの前提は、択一式（`note-articles/infographic-prompt-template.md`）で確立済みの house style をそのまま踏襲している（詳細はそちらの「サイズ・アスペクト比」「スタイル」の章を参照）。R7/Q22の見出し画像プロンプトと同じ構成。

- **サイズ**：`1280×670px`（アスペクト比1.91:1）。より高精細にしたい場合は同じ比率のまま`1920×1006px`でもよい
- 根拠：note公式ヘルプ「登録画像の推奨サイズ一覧」（https://www.help-note.com/hc/ja/articles/360000231642 ）。この比率からずれると note側で中央部分だけ自動トリミングされるため、必ずこの比率で生成すること
- 一覧ページでは`1280×454px`の範囲だけが表示されるため、キャラクター・タイトル文字などの主要な要素は画像の**中央付近**に収まる構図にする

画像生成AI（ChatGPTのGPT Image、Google の画像生成AI等）にそのまま貼り付けて使えるプロンプトです。

---

```
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: Clean flat-design isometric illustration style with soft pastel
colors (blue, green, beige, gray), consistent with a modern explainer-
graphic aesthetic (same visual language as an isometric infographic
poster — rounded shapes, soft drop shadows, no photorealistic rendering).

SCENE: A single humorous, eye-catching scene (not a multi-card poster —
just one illustrated moment) depicting a study-comic duo for a Japanese
land-and-house surveyor (土地家屋調査士) exam prep series.

- Left/center character: a plump, round bird-teacher character
  ("トリ先生"), standing with one wing on hip in a scolding, exasperated
  pose, mouth open as if lecturing.
- Right character: a young female exam-taker ("藍子"), wearing a navy
  business suit over a blue thin-pinstripe blouse, with a startled or
  flustered expression (eyes wide, a small sweat-drop icon near her
  head), holding a pencil or clipboard.
- Between or around them: a small isometric icon of one wooden house
  made of three connected blocks in a row — a small two-story block on
  the left, a small newly built one-story block in the middle glowing
  with a soft golden highlight (representing the new extension that
  joins the other two), and a larger one-story block on the right — all
  sitting together inside one soft dotted outline with a single blank
  house-number plate (no legible text), representing that the joined
  blocks were already one registered building. Next to the house, a
  small gray steel-frame garage with a corrugated metal roof. Keep the
  icon purely graphical/iconic: no readable numbers, no Japanese
  sentences, no measurement text inside it.
- Background: a soft pastel beige/gray gradient, flat and clean, no
  photographic texture.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters either. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image — no
Chinese-only characters, no Korean Hangul, no other non-Japanese script,
and no stray or decorative glyphs of any kind. Reproduce the exact text
strings given below verbatim — do not paraphrase, translate, summarize,
or substitute any characters.

Label text (small, placed directly above the title, 1 line):
土地家屋調査士受験生向け

Title text (large, bold, centered near the top-center of the image, 1
line):
令和4年度問題22（建物）

Subtitle text (smaller, centered directly below the title, 1 line):
〜主と附属がつながっても合体登記じゃない〜

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin — with a solid or illustrated opaque background (the pale
beige/gray gradient described above is the background). There must be no
checkerboard pattern, no partially transparent area, and no unpainted
canvas edge anywhere in the final image.

COMPOSITION REQUIREMENT: Because note.com's article list view only shows
the central 1280x454px band of this 1280x670px image, keep both
characters, the label text, the title text, and the subtitle text within the vertical
center of the canvas (roughly the middle 454px band), with only
background decoration allowed to extend into the top/bottom margins.

Final check before rendering: scan every kanji glyph — including 土・地・
家・屋・調・査・士・受・験・生・向・令・和・年・度・問・題・建・物・主・附・
属・合・体・登・記 — and confirm each
is in standard Japanese (Jōyō) form, not Simplified Chinese and not
Traditional Chinese. If any character renders as a Simplified or
Traditional Chinese variant, redraw that character in the correct
Japanese form. Also scan the entire canvas for any character that is not
standard Japanese hiragana, katakana, or Jōyō kanji — including any
Chinese-only character, Korean Hangul, other non-Japanese script, or
stray decorative glyph — and remove or redraw it so that only standard
Japanese text appears anywhere in the image. Confirm the building icon
contains no legible numbers or sentences (icon only). Confirm both
characters, the label, the title, and the subtitle are positioned within the
central 1280x454px safe area. Confirm the entire canvas, edge to edge, is
filled with a fully opaque background with no transparency or alpha
channel anywhere.
```

## 生成後の確認項目

- サイズが1280×670px（またはその倍率で同比率）になっているか
- ラベル「土地家屋調査士受験生向け」、タイトル「令和4年度問題22（建物）」、サブタイトル「〜主と附属がつながっても合体登記じゃない〜」の文字が一字一句正しいか（note記事のタイトル「【土地家屋調査士受験生向け】令和4年度問題22（建物）〜主と附属がつながっても合体登記じゃない〜」と同じ文言を3行に分けたもの）（簡体字・繁体字・日本語以外の文字が混ざっていないか。特に「附」「属」「体」）
- トリ先生・藍子の2キャラクターと、ラベル・タイトル・サブタイトルの文字が、画像中央の1280×454pxの範囲内に収まっているか（note一覧ページでの見切れ防止）
- 背景が完全に不透明か（透過・アルファチャンネルがないか、別の背景色の上に置いて確認する）
- 建物アイコンの中に、読めてしまう数値・文章が入っていないか（アイコンとしてのみ使う）

## 出力

- PNG画像（1280×670px、またはより高精細な1920×1006px）1枚
