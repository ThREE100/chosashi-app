# 画像作成プロンプト：第22問（建物）解説用インフォグラフィック【共通・基本フォーム】

以下をそのまま貼り付けて使ってください。問題ごとに変えるのは、末尾の「差し替えデータ」の部分だけです。

新しい年度・問題を作るときは、このファイルをコピーして年度・問題のフォルダに置き（例：`R7/Q22/prompt_R7_dai22mon_kaisetsuzu.md`）、末尾の差し替えデータを埋めてください（このファイル自体は汎用のまま保つこと）。

※このプロンプトは DALL·E 3 / Midjourney など、英語の指示で動く画像生成AIにそのまま渡す前提です。座標どおりの正確な作図が必要な場合（辺の傾き・複雑な多角形など）は、土地（第21問）の共通・基本フォーム `prompt_kaisetsuzu-gazou_kihon-form_tochi.md` のようにPythonで座標から作図する方式に切り替えること（文字の配置ルール・重なりの自動検査もそちらに従う）。建物の床面積の求積図（長方形の分割）は形が単純なので、この方式で足りることが多い。

## 使い方の注意（生成後に必ず行うこと）

画像生成AIは寸法の数字や矢印の位置を指示どおりに描けないことがある。生成後、記事に書いた数値（例：4.60m、11.80m）と画像内の表示が一字一句一致しているか必ず目視で確認する。一致していなければ、プロンプトの数値を再確認したうえで作り直す。数値がどうしても安定して描画されない場合は、画像生成後に別途テキストラベルを重ねる（Pillow等での後処理）方式に切り替える。

**「誤りやすい思い込み」と「正しいルール」を対比させる図（○×を左右または上下に並べる構成）を今後この求積図に追加する場合**は、`note-articles/infographic-prompt-template.md`の「正誤対比カードの○×指示の統一ルール」を必ず確認すること。1つの箱に○と×を両方指示する矛盾（画像生成モデルが混乱し左右が同じマークになる不具合）や、1〜2文字しか違わない数値・文字列を左右に並べたときに複製されてしまう不具合が、note-articles配下の同種プロンプトで実際に発生している。

---

**Subject:** An educational infographic showing a 2D architectural floor plan diagram for calculating floor area, designed for a Japanese real estate exam study guide.

**Style:** Clean, flat vector illustration, blueprint style but modern and highly readable. White background with clear black outlines.

**Details & Composition:**
1. The image shows a geometric shape composed of 【分割した長方形の数・配置：例＝two adjacent rectangles side-by-side】.
2. **【区画1の名前：例＝Left Rectangle (West side)】:** 【形状の説明：例＝A standard vertical rectangle】. Inside, text says "【辺長1】" (width) and "【辺長2】" (height). Outline is black.
3. **【区画2の名前：例＝Right Rectangle (East side)】:** 【区画1との位置関係：例＝A taller vertical rectangle attached directly to the right side of the left rectangle. It extends further down than the left rectangle.】
4. Inside 【区画2の名前】, text says "【辺長3】" (width) and "【辺長4】" (height).
5. **Highlighting (Crucial):** 【強調したい部分：例＝The bottom extended section of the Right Rectangle】 must be shaded in a noticeable **translucent bright red or pink color**, or outlined with a thick red dashed line, to emphasize that 【強調する理由：例＝this area was "expanded"】.
6. Add a red arrow pointing to the highlighted area with a small label box (representing "【強調部分のラベル：例＝Living Room Expansion】").
7. **Overall Vibe:** Professional textbook illustration, easy to understand for beginners, neat typography, no cluttered backgrounds.

**Aspect Ratio:** 16:9 or 4:3 (Landscape orientation is preferred for note articles).

---

## 差し替えデータ（問題ごとにここを埋める）

埋めた完成版は、共通テンプレートである本ファイルには残さず、年度・問題のフォルダ（例：`R7/Q22/`）に別名（`prompt_{年度}_dai22mon_kaisetsuzu.md`）で保存すること。

- **対象の図**：【例：2階のリビング拡張部分の床面積求積図】
- **分割した長方形の数・配置**：【例：西側と東側に隣接する縦長の長方形2つ】
- **区画ごとの辺長**：【区画名：横○○m×縦○○m、を区画の数だけ】
- **強調する区画と理由**：【例：東側区画の下端が1階より張り出している部分。増築でリビングが拡張されたことを示す】
- **強調部分のラベル文言**：【例：Living Room Expansion】
- **記事内の数値との対応確認**：この図に書く数値が、note記事本文の求積表の数値と一字一句一致することを確認済みか【はい／いいえ】
