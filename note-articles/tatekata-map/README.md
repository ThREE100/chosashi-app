# 「建て付け」マップ（不動産登記法）

条文を番号順に読む前に持つ「地図」の記事と図解。2026-11-04 作成。

| ファイル | 中身 |
|---|---|
| `00-kousei.md` | 構成案（8つの棚、記事の構成、図の一覧） |
| `01-fudousan-touki-hou-tatekata-map.md` | note記事の本文（画像挿入マーカー7か所） |
| `01-zukai-prompts.md` | 図解7枚・Instagram用（図1の3:4版・4:5版）のChatGPT用プロンプト |
| `02-header-image-prompts.md` | note用（1280×670）とInstagram用（1080×1440）の見出し画像プロンプト（MC1人） |
| `03-instagram-captions.md` | Instagramのキャプション案（カルーセル1投稿用A＋単独投稿用B-0〜B-7の9本） |
| `check_article.py` | 原文（`../laws/fudousan-touki-hou.md`）との機械チェック。`python3 note-articles/tatekata-map/check_article.py` で NG 0件にする |

- 画像の生成・目視確認は未実施（ユーザーがChatGPTで行う）。画像の中には図番を入れない。
- 記事は、条文の位置関係を示す地図で、各条の細部は原文または `law-commentary/` で確かめる。
- 他の法令（不動産登記令・規則、区分所有法）に広げるときは、この構成（棚に分ける→棚ごとの図→探し方クイズ）を使う。
