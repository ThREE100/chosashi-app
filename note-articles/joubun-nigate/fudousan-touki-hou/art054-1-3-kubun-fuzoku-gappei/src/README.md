# プロンプトと記事の生成元（不動産登記法 第54条1項3号：区分合併と附属合併の使い分け）

`../prompt_infographic_art054-1-3.md` と `../note_art054-1-3.md` は生成物です。直すときは、ここを直して再生成します（生成物を手で直さない）。

- `gen_infographic.py`：図解5枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は `../../../common/infographic_parts.py`）。実行すると `../prompt_infographic_art054-1-3.md` を書き出す。
- `note_template.md`：記事の本文の元。`{{LAW54_P}}`・`{{LAW56_P}}`・`{{JUNSOKU86}}` を `note-articles/laws/` の原文（不動産登記法54条・56条、準則86条）に差し替えて `../note_art054-1-3.md` にする（`build_note.py`）。
- 4コマはこの回にはない。見出し画像のプロンプトは `../prompt_midashi_art054-1-3.md`（手で作成）。区分合併の主従・接続の4コマは `note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch9/` にある。

再生成のあとは、`python3 note-articles/joubun-nigate/common/check_article.py <このフォルダの親>` で NG 0件を確かめます。
