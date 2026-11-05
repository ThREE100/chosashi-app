# 「数字の図鑑」（不動産登記法の期限・数字）

不動産登記法の期限・金額・年月・保存期間を、7つの引き出しに整理した記事と図解。2026-11-04 作成。「建て付けマップ」（`../tatekata-map/`）の姉妹編。

| ファイル | 中身 |
|---|---|
| `00-kousei.md` | 構成案（7つの引き出し、原文の確認、図の一覧） |
| `01-fudousan-touki-hou-kigen-suuji-zukan.md` | note記事の本文（画像挿入マーカー7か所） |
| `01-zukai-prompts.md` | 図解7枚の ChatGPT 用プロンプト（**note用とInstagram用の2種類**、計14本） |
| `02-header-image-prompts.md` | 見出し画像のプロンプト（note用1280×670・Instagram用1080×1350、MC1人） |
| `03-instagram-captions.md` | Instagramのキャプション案（カルーセル1投稿用A＋単独投稿用B-0〜B-7の9本） |
| `src/gen_prompts.py` | 01・02のプロンプトを作る（手で直さず、ここのデータを直して作り直す） |
| `check_article.py` | 原文（`../laws/`）との機械チェック。`python3 note-articles/kigen-suuji-zukan/check_article.py` で NG 0件にする |

- 画像の生成・目視確認は未実施（ユーザーがChatGPTで行う）。画像の中には図番を入れない。
- 色の約束：青＝表示の登記、薄い橙＝権利の登記、赤橙＝過料・罰則、灰緑＝保存期間、紫灰＝その他。
- 数字は条文の原文で確かめたものだけを載せる。法改正があれば記事と図の数字を見直す。
