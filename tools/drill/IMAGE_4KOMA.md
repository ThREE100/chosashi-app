# ドリル解説の4コマ画像：生成プロンプトと型

ドリルの1肢を、トリ先生と藍子の4コマ（縦長1枚）で解説する画像の型です。D0026（H17-Q06 肢1）で確定した形式を、ほかの肢にも当てはめます。
キャラクターは、別に渡すキャラクターシートに合わせます。

## 形式の決まり（D0026で確定、2026-10-07）

- 縦に4コマ：①よくある思い込み／②（論点の中身）／③（行き先・結果）／④結論は〇または×。
- 上端にタイトル帯（結論を1行で）。各コマの左に藍子、右にトリ先生、その間に小さな図。
- ④のコマには、3項目のチェックリスト（✓マーク可。苦手分析シリーズの「✓✕を使わない」決まりは、4コマには適用しない）。
- ④の下、フッターの上に、注記を1行入れる（「通常の場合の結論」に対する例外など）。
- フッターは2行：結論の1文、「問題D＿＿＿＿　正解〇または×（年度-Q問番号肢番号）」。内部IDを含めたままにする。
- 条文番号は、コマの中には入れない（文字数が過剰になるため）。注記に入れるのは、例外の条文だけ。
- 図の同じ対象は、コマをまたいで同じ見た目にする（②で消えた帯が③に出る、のような不一致を作らない）。
- 吹き出しの改行は、語の途中で切らず、文節の区切りで指定する。
- 小さな文字（書類の表記、A・Bの肩書き）は、そのままでよい。

## D0026の修正版プロンプト

```
Create a Japanese-language explanatory image in portrait layout, about 940x1670 pixels, made of exactly four stacked comic-style panels, with a title band at the top, a note line and a footer band at the bottom. Soft flat illustration, cream panel backgrounds, rounded frames, a dark navy header chip for each panel. Follow the supplied character sheet exactly: 藍子 (long wavy brown hair, blouse with thin blue vertical stripes, navy suit) on the left of every panel, トリ先生 (chubby bird teacher, round red glasses, blue shirt, red neckerchief) on the right of every panel. Between them, a small diagram.

CRITICAL TEXT REQUIREMENT: All text must be standard Japanese only (hiragana, katakana, Jōyō kanji). No Simplified or Traditional Chinese glyphs, no other scripts, no stray glyphs. Reproduce every string below verbatim. The English letters A and B are single capital letters; do not render any other Latin letters (in particular, do not render "BI" anywhere; write only the single letter B).

BACKGROUND: fully opaque from edge to edge, no transparency.

TITLE BAND (one line; the phrase 債権者の承諾は不要 has a yellow marker highlight):
仮差押えがあっても、分筆に債権者の承諾は不要

PANEL 1  header chip: ① よくある思い込み
 藍子 bubble (two lines): 仮差押えがあるなら、 / Bの承諾が要りますよね？
 トリ先生 bubble (two lines): 出たわね。承諾を証する / 情報が要ると思ったでしょ
 Diagram: a green plot of land with a red diagonal band labeled 仮差押え; person A (blue, holding a paper labeled 分筆の申請) on the left; person B (orange) on the right with a small bubble 承諾は要る？ . Labels: A（所有権の登記名義人） and B（仮差押債権者）

PANEL 2  header chip: ② 分筆とは
 藍子 bubble (two lines): 分筆すると、仮差押えの / 内容まで変わるんですか？
 トリ先生 bubble (three lines, break exactly here): いいえ。 / 一筆を複数に区分する / 物理的な変更にすぎないのよ
 Diagram: on the left a label 一筆 above one green plot WITH the red band 仮差押え; a navy arrow labeled 分筆; on the right a label 二筆 above TWO green plots, and BOTH of the two plots carry the same red diagonal band labeled 仮差押え (the band must not disappear). Caption under the arrow: 物理的に区分するだけ

PANEL 3  header chip: ③ 仮差押えの行き先
 藍子 bubble (two lines): 仮差押えは、分筆したら / どうなるんですか？
 トリ先生 bubble (two lines): 分筆後の各土地に、 / 当然に効力が及ぶのよ
 Diagram: a gray-suited figure labeled 登記官 at the top; two navy arrows down to two green plots, each with the red band 仮差押え. Arrow caption (one line): 各土地の登記記録に引き継ぐ（転写）

PANEL 4  header chip: ④ 結論は×
 藍子 bubble (two lines): 債権者の承諾を証する情報は、 / 提供しなくていいんですね！
 トリ先生 bubble (two lines): そのとおり。 / 承諾が必要という記述は×よ
 Checklist box with three rows and blue check marks, verbatim:
 分筆は一筆を区分する物理的な変更
 仮差押えは分筆後の各土地に及ぶ
 債権者の承諾を証する情報は不要

NOTE LINE (small text, a thin line of text between the panel 4 frame and the footer band, verbatim, one or two lines):
注）権利を分筆後の一方の土地だけで消滅させるときは、権利者の承諾を証する情報が必要（不動産登記法40条）

FOOTER BAND (navy, two lines, first line with yellow highlight):
仮差押えの効力は分筆後の各土地に及び、債権者の承諾は不要
問題D0026　正解×（H17-Q06肢1）

Do not add any other text. Keep each speech bubble's line breaks exactly as specified (never split a word across lines).

Final check before rendering: scan every kanji glyph and confirm it is standard Japanese form, paying special attention to 仮, 差, 押, 分, 筆, 債, 権, 承, 諾, 証, 区, 変, 効, 転, 写, 登, 記, 当, 然, 提, 供, 消, 滅. Confirm there is no "BI" or any stray Latin letters, that panel 2's right side shows the red 仮差押え band on both plots, that panel 3's caption reads 各土地の登記記録に引き継ぐ（転写）, that the note line and the footer are present, and that the canvas is fully opaque.
```

## ほかの肢に使うときの差し替え箇所

タイトル、①〜④の吹き出し、図の説明、チェックリスト3項目、注記、フッター（結論の1文、問題ID・正解・出典）。注記が要らない肢では、注記の行を外す。
