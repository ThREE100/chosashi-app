# 図解企画6本（zukai-kikaku）

2026-11-05 作成。構成案は `00-kousei.md`。画像の生成と目視確認はChatGPTで行う（未実施）。

| 回 | 記事 | 図解プロンプト（note用・Instagram用） |
|---|---|---|
| 1 | `01-tochi-tatemono-isshou.md` | `zukai-prompts-01.md`（2枚） |
| 2 | `02-taihi-zukan.md` | `zukai-prompts-02.md`（3枚） |
| 3 | `03-tenpu-jouhou-hayami.md` | `zukai-prompts-03.md`（2枚） |
| 4 | `04-joubun-no-yomikata.md` | `zukai-prompts-04.md`（3枚） |
| 5 | `05-kijutsu-tokujunban.md` | `zukai-prompts-05.md`（2枚） |
| 6 | `06-ichinichi-no-touki-story.md` | `06-yonkoma-prompt.md`（四コマ。1080×1920）、`06-reel-storyboard.md`（リールの絵コンテ） |

共通：
- 見出し画像のプロンプト（note用1280×670・Instagram用1080×1350。MC1人）：`header-image-prompts.md`
- Instagramのキャプション案（企画ごとにカルーセル用と単発用）：`instagram-captions.md`
- 原文との機械チェック：`check_article.py`（NG 0件）

## 作り方

- 図・見出し・キャプションの生成物は手で直さず、`src/data.py` を直して `python3 note-articles/topics/zukai-kikaku/src/gen_prompts.py` で作り直す。
- 直したら `python3 note-articles/topics/zukai-kikaku/check_article.py` でNG 0件にする。
- 四コマ（第6回）だけは手書きのプロンプト。`python3 tools/drill/manga/check_prompt.py note-articles/topics/zukai-kikaku/06-yonkoma-prompt.md --no-article` で確かめる。残る2件のNGは、ドリルの肢（D＋4けた）用の記事タイトルの形式と、トリ先生・藍子の見出し画像（この企画の見出し画像はMC1人）に関するもので、この企画には当てはまらない。

## 画像のファイル名

- 図解：note用 `kzNN_zu01.png` から、Instagram用 `kzNN_ig01.png` から（NNは回の番号）。
- 四コマ：`四コマ図解～ある一日の登記ストーリー～.png`。
- 見出し：`kzNN_header_note.png`、`kzNN_header_ig.png`。

## 使い方の目安

- 1回の記事を出す週に、Instagramは「見出し画像（表紙）→図→まとめ」のカルーセル（キャプションA）を1回、続く日に単発（B）を1枚ずつ出す。
- 投稿は `note-unei/instagram/README.md` のつなぎの枠（F2：個別テーマ）に当てる使い方も想定している。
