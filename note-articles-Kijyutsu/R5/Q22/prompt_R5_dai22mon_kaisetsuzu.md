# 図の作成プロンプト：令和5年度 第22問（建物）解説用インフォグラフィック

`prompt_kaisetsuzu-gazou_kihon-form_tatemono.md`（共通フォーム）の差し替え版。note記事「令和5年度のわなを見抜け！〜区分合併と床面積の恐怖〜」第3章に挿入する、2階の床面積求積図。

---

**Subject:** An educational infographic showing a 2D architectural floor plan diagram for calculating floor area, designed for a Japanese real estate exam study guide.

**Style:** Clean, flat vector illustration, blueprint style but modern and highly readable. White background with clear black outlines.

**Details & Composition:**
1. The image shows a geometric shape composed of two adjacent rectangles side-by-side.
2. **Left Rectangle (West side):** A standard vertical rectangle. Inside, text says "4.60m" (width) and "11.80m" (height). Outline is black.
3. **Right Rectangle (East side):** A taller vertical rectangle attached directly to the right side of the left rectangle. It extends further down than the left rectangle.
4. Inside the Right Rectangle, text says "2.70m" (width) and "12.70m" (height).
5. **Highlighting (Crucial):** The bottom extended section of the Right Rectangle must be shaded in a noticeable **translucent bright red or pink color**, or outlined with a thick red dashed line, to emphasize that this area was "expanded".
6. Add a red arrow pointing to the highlighted extended area with a small label box (representing the "Living Room Expansion").
7. **Overall Vibe:** Professional textbook illustration, easy to understand for beginners, neat typography, no cluttered backgrounds.

**Aspect Ratio:** 16:9 or 4:3 (Landscape orientation is preferred for note articles).

---

## 差し替えデータ（記入済み）

- **対象の図**：2階のリビング拡張部分の床面積求積図
- **分割した長方形の数・配置**：西側と東側に隣接する縦長の長方形2つ
- **区画ごとの辺長**：西側＝横4.60m×縦11.80m／東側＝横2.70m×縦12.70m
- **強調する区画と理由**：東側区画の下端が西側（＝1階の外形11.80m）より張り出している部分。工事(2)のリビング拡張で2階だけ東側が延びたことを示す
- **強調部分のラベル文言**：Living Room Expansion
- **記事内の数値との対応確認**：はい（`note_R5_dai22mon_tatemono_kaisetsu.md` 第3章の求積表と一致）

## ダブルチェック結果（2026-09-28、アガルートの解答例・試験問題本文と照合）

`qa-checklist-kijutsu.md` に沿って、アガルートアカデミーの解答例（第22問 解答例）と試験問題本文（令和5年度 問題22）を用いて照合した。

- 登記の目的（合併／合体の判別）、原因及びその日付（構造変更、増築、3番9の2を合併）、構造（軽量鉄骨造スレートぶき2階建）、屋根裏部屋の床面積不算入（天井高1.40m）、添付書類（規約証明書）：いずれも解答例と一致
- 床面積の求積：1階83.62㎡（0.90×9.00＝8.1000、6.40×11.80＝75.5200）、2階88.57㎡（2.70×12.70＝34.2900、4.60×11.80＝54.2800）は、解答例の第3欄・求積表と分割方法まで完全に一致
- 敷地（本件土地）の辺長（AB18.0、BC14.5、CD16.1、DA13.2）は、試験問題本文の〔座標値一覧表〕（A・B・C・D）から検算し一致
- `verify_R5_dai22mon.py` を作成し、上記の表示値がすべて記事本文と一致すること（NG 0件）を確認済み
- 記事冒頭に「本記事の数値はアガルートアカデミーの解答例と照合済みです」を追記した

## 未実施の項目（引き継ぎ）

- 実際の画像生成（本ファイルはプロンプトのみで、生成・検品は未実施）
- 登記申請書画像プロンプト（`prompt_toukishinseisho-gazou_kihon-form_tatemono.md` の記入済み版）は未作成
