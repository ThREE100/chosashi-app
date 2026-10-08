# 記述式解説漫画（長編）パイロット：R7/Q21 第2章

| ファイル | 役割 |
|---|---|
| `r7_q21_ch02.py` | ページ構成表の設計データ（セリフの分割、図・カードの文言、区画、キャラの出し方）。実行すると下の2つを生成 |
| `R7-Q21-ch02_page_spec.json` | 文言の正本（機械が読む） |
| `R7-Q21-ch02_kouseihyou.md` | 読むための構成表 |
| `check_pages.py` | 構成表の機械チェック（NG 0件・WARN 0件にしてから次へ） |
| `gen_pages.py` | ChatGPT用のプロンプトを生成（`prompts/`）。`00_project_instructions.md` は、ChatGPTのプロジェクトの指示に1回だけ貼る共通ルール |
| `compose_pages.py` | ChatGPTのページ画像の灰色の仮枠に、図・計算カード・答えバナーを貼って完成 |
| `mock_chatgpt_pages.py` | ChatGPTの代わりの模擬ページ（合成の動作確認用） |

## 図をChatGPTに添付しない方法（方式A′）
ChatGPTには**図を渡さない**。図・計算カード・答えバナーは、ChatGPTには『何も書かれていない薄い灰色（#E6E6E6）の長方形』だけを描かせる。
`compose_pages.py` が、画像から灰色の長方形を自動で見つけ、構成表の順（上から）に図やカードを貼り込む。
図は、ローカルのリポジトリ、または GitHub のURLから読む：

```
# ローカルのリポジトリ（既定）
python3 tools/drill/manga/kijutsu_pilot/compose_pages.py <page_spec.json> <ChatGPTのページ画像> <出力>
# GitHub のURL（図のPNGを随時GitHubに置く場合）。非公開リポジトリは環境変数 GITHUB_TOKEN が必要
python3 .../compose_pages.py <page_spec.json> <ChatGPTのページ画像> <出力> --figures-base https://raw.githubusercontent.com/ThREE100/chosashi-app/main/
```

## 手順（1ページずつ）
1. `python3 r7_q21_ch02.py` → `python3 check_pages.py R7-Q21-ch02_page_spec.json`（NG 0件）→ `python3 gen_pages.py R7-Q21-ch02_page_spec.json`
2. ChatGPTで「プロジェクト」を作り、キャラ仕様書の画像5枚と `女性キャラクター_統一仕様書.md`（最新版は `tools/drill/manga/女性キャラクター_統一仕様書.md`）を**ファイル**に1回だけ入れ、`prompts/00_project_instructions.md` の ```text の中身を**指示**に貼る（以後、キャラ画像の添付は不要）。
3. ページごとに `prompts/R7-Q21-02-NN_prompt.md` の ```text の中身を貼って、画像を1枚生成する（図の添付は不要）。生成された画像は、実際に表示されたか・文言・キャラの同一性を目視で確認（`CHATGPT_MANGA_WORKFLOW.md` §4）。
4. 生成した画像を `R7-Q21-02-NN.png` の名前で1つのフォルダに保存する。
5. `compose_pages.py` で図・カードを貼って完成。仮枠の数が合わないページは `NG` で止まるので、そのページだけ生成し直す。

## 日本語フォント
`compose_pages.py` は、Windows（游ゴシック・メイリオ）、Mac（ヒラギノ）、Linux（Noto Sans CJK・IPAゴシック）を順に探す。見つからないときは `--font <フォントファイル>`。
