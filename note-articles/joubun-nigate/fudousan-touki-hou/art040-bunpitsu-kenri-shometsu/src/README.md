# プロンプトの生成元（第40条）

`../prompt_*.md` は生成物です。直すときは、ここの設計データを直して再生成します（生成物を手で直さない）。

- `specs_4koma.py`：4コマ4本の設計データ。`MANGA_RULES.md` の生成器 `gen_prompts.py`（ブランチ `claude/kind-bell-y3f106` の `tools/drill/manga/`）の `render(spec)` に渡して、`prompt_4koma_*.md` の本体を作る。機械チェックは同ブランチの `check_prompt.py`（NG 0件・WARN 0件）。単独のnote記事用の節（記事タイトル・冒頭文・見出し画像・画像ファイル名）は、画像に問題番号が載らないよう、外してある。
- `gen_infographic.py`：図解6枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は `../../../common/infographic_parts.py`）。
- `note_template.md`：記事の本文の元。`{{LAW40}}` を `note-articles/laws/fudousan-touki-hou.md` の原文に差し替えて `note_art040.md` にする。

再生成のあとは、`python3 note-articles/joubun-nigate/common/check_article.py <このフォルダの親>` で NG 0件を確かめます。
