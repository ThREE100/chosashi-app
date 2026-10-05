# 画像作成プロンプト：第22問（建物）解説用インフォグラフィック【共通・基本フォーム】

以下をそのまま貼り付けて使ってください。問題ごとに変えるのは、末尾の「差し替えデータ」の部分だけです。

新しい年度・問題を作るときは、このファイルをコピーして年度・問題のフォルダに置き（例：`R7/Q22/prompt_R7_dai22mon_kaisetsuzu.md`）、末尾の差し替えデータを埋めてください（このファイル自体は汎用のまま保つこと）。

※このプロンプトは DALL·E 3 / Midjourney など、英語の指示で動く画像生成AIにそのまま渡す前提です。座標どおりの正確な作図が必要な場合（辺の傾き・複雑な多角形など）は、土地（第21問）の共通・基本フォーム `prompt_kaisetsuzu-gazou_kihon-form_tochi.md` のようにPythonで座標から作図する方式に切り替えること（文字の配置ルール・重なりの自動検査もそちらに従う）。建物の床面積の求積図（長方形の分割）は形が単純なので、この方式で足りることが多い。（2026-10-05現在、R7〜H20の全年度の解説図は、この英語の指示ではなく、頂点座標から `tools/zu_helpers.py` で作図した。年度別のプロンプトは、その作図の仕様〈頂点座標・文言・図の順序〉を書いたものとして作る）

## 使い方の注意（生成後に必ず行うこと）

画像生成AIは寸法の数字や矢印の位置を指示どおりに描けないことがある。生成後、記事に書いた数値（例：4.60m、11.80m）と画像内の表示が一字一句一致しているか必ず目視で確認する。一致していなければ、プロンプトの数値を再確認したうえで作り直す。数値がどうしても安定して描画されない場合は、画像生成後に別途テキストラベルを重ねる（Pillow等での後処理）方式に切り替える。

**`tools/zu_helpers.py` で作図するときの注意（2026-09-29追加、R6/Q22）**：重なりの自動検査が対象にするのは、`Zu` の `poly`・`line`・`point`・文字の各関数で描いたものだけ。matplotlib の `Circle` などの図形を直接 `add_patch` で描いた記号（R6/Q22の車庫の柱の丸）は検査に入らず、吹き出しの箱がその上に重なっても「0件」になる（R6/Q22で柱の丸が2つ隠れていたのを目視で見つけた）。直接描いた記号は、中心を `z.markers` に、線を `z.segments` に登録してから文字を置く。

**へこみの辺と矢印（2026-09-29追加、H28/Q22）**：`edge_label` の「外側」は多角形の重心を基準に決めるので、外形に深いへこみがある階（H28/Q22の2階、既存建物と新館の間）は、へこみの辺の寸法がへこみの外や隣の区画の中に出ることがある。へこみの辺は `free_text` で「へこみの側」に置く。`ax.annotate` で直接描いた矢印（経路など）も、線分を `z.segments` に登録してから文字を置く（登録しないと文字を横切っても検査で見つからない）。

**囲みの枠の描き方（2026-09-29追加、R4/Q22）**：説明用の点線の枠（「家屋番号5番3（1個の建物）」など）を `Zu.poly` の閉じた多角形で描くと、区画として扱われ、方位記号を枠の中に置けなくなる。枠は `closed=False` の折れ線（始点を最後にもう一度加える）で描く。作図の環境に日本語フォントがIPAゴシックしかないときは、`apt-get install fonts-noto-cjk` で Noto Sans/Serif CJK JP を入れてから描く（申請書のHTMLの明朝体にも使う）。

**検査の対象にならないもの・各階の縮尺（2026-10-02追加、全年度の照らし直し）**：`callout` の引き出し線と `add_patch` で描いた図形（柱の四角など）は重なりの自動検査の対象にならないので、目視で確かめる（柱は中心を `markers` に登録する）。建物の一部の外形を `closed=False` の折れ線で描くときは、閉じる辺まで頂点を並べる。`new_figure` の説明文は日本語だと折り返されないので、長いときは自分で改行する。各階平面図の完成形は、各階・附属建物を同じ縮尺で描く（1つの作図範囲にずらして並べるか、同じ大きさのパネル・同じ表示範囲にする）。答案用紙の欄の枠は `public/kijutsu/{年度}-tatemono/a*.webp` の印刷どおりにし、ないときは仮の形と明記する

**`fit` は文字より先に呼ぶ（2026-09-30追加、H21/Q22）**：`edge_label`・`free_text`・`callout` は、置いた時点の表示範囲で重なりとはみ出しを評価して候補を選ぶ。文字を置いたあとに `fit` を呼ぶと、既定の表示範囲で評価された位置のまま拡大・縮小され、「重ならない位置が見つからない」の警告や、最終検査での線との重なりが出る。図形の範囲が決まったら、線を描く前（少なくとも文字を置く前）に `fit(..., pad_aspect=True)` を呼び、方位記号（`north_arrow`）もその直後に置く。断面図（ロフトの天井の高さなど）は (東, 高さ) を (北, 東) に読み替えて同じ部品で描ける

**内法の図形の辺長ラベル（2026-09-29追加、R1/Q22）**：区分建物の内法の長方形は、0.10ほど外側に壁の中心線がある。辺長ラベルを外側に置くと中心線に文字がかかるので、`edge_label(..., outward=False)` で内側に置く。3パネルの図の中央に壁の断面（拡大図）を置くときは、厚さを長さの方向より大きく拡大した模式にし、中央パネルの幅を左右の0.85倍程度にする（狭いと引き出しの文字がパネルの外にはみ出す）

**固定配置の図・文字が別の図形の内側に入る置き方（2026-10-05追加、H22・H25・H27・H23）**：枠と文字だけの図（`box_fig` など、座標を使わない固定配置の図）は重なりの自動検査の対象外で、1枚目に置くとフォントの設定が先に走らず日本語が豆腐になった（H22。`box_fig` の中でもフォントを設定する）。固定配置の図は、文字の重なりと枠からのはみ出しを機械で調べる関数（`check_fixed`。`H25/Q22/zu/draw_H25_dai22mon_kaisetsuzu.py` が見本）を作図スクリプトに入れ、目視でも確かめる。文字が別の図形（点線の四角など）の内側に入る置き方は、座標を使う図でも検査で見つからないので目視で見つける（H27）。実寸では差が見えない拡大図（壁の厚さ0.075など）は、厚さを誇張した模式図にし、題に「模式図・壁の厚さは誇張」と明記する（H27・H23・H30）

**図の見出し・記号・方位・番号（2026-10-05追加、全年度の照らし直し）**：図の見出しに「✕」「○」「✓」を使わず「誤り：」「正解：」と書く（作図のフォントで化ける。プロンプトにも文字の記号を書かない）。隣接地の地番を「北に〜、西に〜」とプロンプトに書くときは、見取図と、作図スクリプトで置いた位置の両方と照らす（H27で、作図は正しいのにプロンプトの文で南北を取り違えた）。敷地が座標の軸に対して傾いている年度は、解説図も答案用紙の方位記号と同じ向きに回して描き、方位記号を傾ける（H22）。標準セットの図を作らない年度（座標・辺長がない、問3で建物図面を求めない等）は、作らない理由をプロンプトの冒頭に書く（R7）。図の説明文（キャプション）や作図スクリプトの文字列にも、古い書き方（「左下」「注3」とだけ書く、など）が残るので、本文と同じ基準で確かめる（R7）。図の番号は記事の挿入順に振り直し、プロンプトには生成済みのファイル名を書く。作図スクリプト・プロンプト・照合スクリプトの番号をそろえ、既存の図は振り直し後に再生成して中身が変わっていないことを確かめる（H22〜H26）

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
