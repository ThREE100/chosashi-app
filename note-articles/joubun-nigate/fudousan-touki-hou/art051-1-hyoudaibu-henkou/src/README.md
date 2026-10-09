# プロンプトの生成元（第51条第1項）

`../prompt_*.md` は生成物です。直すときは、ここの設計データを直して再生成します（生成物を手で直さない）。

- `specs_4koma.py`：4コマ4本の設計データ。`MANGA_RULES.md` の生成器 `gen_prompts.py`（ブランチ `claude/kind-bell-y3f106` の `tools/drill/manga/`）の `render(spec)` に渡して、`prompt_4koma_*.md` の本体を作る。機械チェックは同ブランチの `check_prompt.py`（`--no-article` なしでも NG 0件・WARN 0件）。
- `gen_infographic.py`：図解6枚のプロンプトを組み立てる（標準ライブラリのみ）。`python3 gen_infographic.py` で `prompt_infographic_art051-1.md` と同じ内容を作る。
- `note_template.md`：記事の本文の元。`{{LAW51_1}}`・`{{LAW44_1}}` を `note-articles/laws/fudousan-touki-hou.md` の原文に差し替えて `note_art051-1.md` にする。

再生成のあとは、`../check_art051-1.py` を実行して NG 0件を確かめます。
