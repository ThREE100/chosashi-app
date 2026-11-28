# 漫画コンテンツに使えそうなGitHubの公開ツール（調査メモ・2026-11-28）

導入・実行はしていない。候補の提示だけ。生成はChatGPT（キャラクターシートを添付）で行う前提で、GPUがなくても使えるかを重く見た。

**注意**：`CLAUDE.md` の4コマ解説図解の節に「文字を固定フォントで描く試作は1本だけ、他の肢では使わない（誤字はプロンプトの修正で対処）」というユーザーの決まりがある。吹き出しの文字を後から重ねる道具（下の1・2・5・6）を4コマに使うときは、改めて決める。この会話編は4コマとは別の企画だが、同じ考え方で揃えるかも決めてほしい。

| # | リポジトリ | できること | ライセンス | 導入のしやすさ | 評価 |
|---|---|---|---|---|---|
| 1 | [zyddnys/manga-image-translator](https://github.com/zyddnys/manga-image-translator) | 漫画の文字の検出・消去・写植（縦書き・横書き）。API・Dockerあり | GPL-3.0 | Python・Docker。CPUで動く | ○ AIが崩した吹き出しの文字を消して打ち直す前処理に。別プロセスの道具として使う |
| 2 | [dmMaze/BallonsTranslator](https://github.com/dmMaze/BallonsTranslator) | GUIで吹き出しの写植を見たまま直せる | 未確認（GPLと思われる） | Python・GUI。GPUなしでも動く | ○ 手直し用 |
| 3 | [dmMaze/comic-text-detector](https://github.com/dmMaze/comic-text-detector) | 漫画の文字の枠・マスクの検出（1・2の中核） | GPL-3.0 | Python（PyTorch） | △ 単体では写植しない |
| 4 | koharu（Rust製の漫画翻訳） | 検出・OCR・消去・縦書きの描画 | GPL-3.0 | 検出と消去はGPU前提 | △ |
| 5 | [google/budoux](https://github.com/google/budoux) | 日本語の文節で改行位置を決める（吹き出しで語の途中で折れない） | Apache-2.0 | Python・JS。とても軽い | ◎ 今のHTML＋Playwrightにすぐ足せる |
| 6 | tategaki（npm） | HTMLを縦書きに整える（約物の詰め） | MIT | JS | ○ CSSの `writing-mode` の補強 |
| 7 | [abuseofnotation/comic-web-markup](https://github.com/abuseofnotation/comic-web-markup) | テキストでコマ・台詞を書いてSVGに描く | MIT | JS（小さい） | △ 台本をコードで書く参考 |
| 8 | kierangilliam/storyboard | YAML（キャラ・場面・テンプレート）から絵コンテを一括生成するCLI | 記載なし | CLI。生成はAPI | ○ 台本→コマの管理の設計の参考（コードは流用しない） |
| 9 | [gramener/comicgen](https://github.com/gramener/comicgen) | SVGのキャラと場面の合成 | MIT | JS | △ 自前のSVGキャラ前提でAI画像と合わない |
| 10 | [hvision-nku/StoryDiffusion](https://github.com/hvision-nku/storydiffusion) | 同じキャラを複数コマで一貫して生成 | Apache-2.0 | GPU必須 | △ ChatGPT運用では使わない |
| 11 | ComfyUI-PanelForge | ComfyUIのノードでコマ割りのページを組む | MIT | ComfyUI（GPU）前提 | △ |

補足：キャラの一貫性の道具（IP-Adapter・LoRA）はどれもGPUのローカル生成が前提。ChatGPTで作るなら、キャラクターシートを毎回添付する今のやり方が現実的。GPUなしで使えるコマ割りの有力な道具は見つからず、HTML/CSS Grid で自作するのが確実。

## 最初に試すなら

1. **BudouX**（＋CSSの縦書き）：吹き出しの改行を正しくする。軽くてライセンスも緩い。
2. **manga-image-translator**：生成画像の吹き出しの位置を出す・崩れた文字を消す前処理。GPLなので取り込まず外の道具として。
3. **storyboard の構成**：台本（このフォルダの `src/dNN.py`）からコマを作る管理の参考。今の仕組みはすでにこれに近い。
