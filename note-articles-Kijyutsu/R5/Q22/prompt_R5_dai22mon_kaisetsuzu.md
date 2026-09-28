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

## 未実施の項目（引き継ぎ）

- 実際の画像生成（本ファイルはプロンプトのみで、生成・検品は未実施）
- `verify_R5_dai22mon.py` による数値の再検算（未作成）
- `qa-checklist-kijutsu.md` に沿った予備校解答例とのダブルチェック（本記事は会話形式ワークフローの参考例として先に記録したもので、解答例との照合は未実施）
- 登記申請書画像プロンプト（`prompt_toukishinseisho-gazou_kihon-form_tatemono.md` の記入済み版）は未作成
