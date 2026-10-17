# プロンプトと記事の生成元（届出先・申請先の決め方：調査士法の届出先＋不動産登記法の申請先）

`../prompt_infographic_art014-034.md` と `../note_art014-034.md` は生成物です。直すときは、ここを直して再生成します（生成物を手で直さない）。

- `gen_infographic.py`：図解7枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は `../../../common/infographic_parts.py`）。実行すると `../prompt_infographic_art014-034.md` を書き出す。
- `note_template.md`：記事の本文の元。`{{LAW14}}`・`{{LAW34_2}}` を `note-articles/laws/chousashi-hou.md` の原文に、`{{LAW6}}`・`{{LAW124}}` を `note-articles/laws/fudousan-touki-hou.md` の原文に差し替えて `../note_art014-034.md` にする（`build_note.py`）。
- 4コマはこの回にはない（見出し画像のプロンプトは `../prompt_midashi_art014-034.md` を手で作成）。つまずき固定の4コマは `tools/drill/manga/D2096_prompt.md`（第三案）にある。

再生成のあとは、`python3 note-articles/joubun-nigate/common/check_article.py <このフォルダの親>` で NG 0件を確かめます。
