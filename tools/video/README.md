# 解説動画の自動生成（KaisetsuScript）

会話形式のnote記事（トリ先生・藍子）と、作図済みの解説図（`note-articles-Kijyutsu/**/zu/*.png`）から、
YouTube用の解説動画（1920×1080のMP4）・サムネイル・概要欄（チャプターつき）・字幕（SRT）を自動で作る仕組み。

中嶋謙互さんのブログ記事「バイブなもの作りの時代」のやり方（MulmoScript / AvatarScript / JingleScript）にならって、
**LLM が書くための台本言語（KaisetsuScript）を人間が決め、LLM（Claude Code）がその言語で台本を書き、レンダラーが動画にする**
という分担にしてある。人間がやるのは「どの記事を動画にするか」と「出来上がりを見て直すかどうか」の判断だけ。

## 全体の流れ

```
note記事（会話形式）──article2script.py──▶ 台本の下書き（JSON）
                                              │  Claude Code が仕上げる（画像の割り当て・セリフの短縮・読み）
                                              ▼
                                   episodes/<id>.json（KaisetsuScript）
                                              │  render.py
                                              ▼
 out/<id>/<id>.mp4（動画） thumbnail.png（サムネイル） youtube.md（タイトル・概要欄・チャプター・タグ） <id>.srt（字幕）
```

| 部品 | ファイル | 役割（記事の対応物） |
|---|---|---|
| 台本言語 | `episodes/*.json` | KaisetsuScript。章・話者・セリフ・図・読みを書く（MulmoScript に当たる） |
| 口パク | `render.py` の `mouth_track` + `characters.py` | 音声の大きさで口を開閉（AvatarScript に当たる。今は仮のSVGアバター） |
| ジングル | `jingle.py` + `jingles/*.json` | JSONの楽譜から合成（JingleScript の簡易版。オープニング・章の切り替え・エンディング） |
| 音声合成 | `tts.py` + `voices.json` + `yomi_dict.json` | Open JTalk（オフライン）／VOICEVOX（ローカルPC） |
| 下書き変換 | `article2script.py` | 記事のセリフ・画像挿入マーカー・箇条書きを台本の形に並べる |

## 準備（1回だけ）

```bash
cd tools/video
./setup_voices.sh        # pyopenjtalk・Playwright・Pillow と、声データ（voices/）を取得
```

ffmpeg と Chromium（Playwright）が必要。クラウドのセッションには最初から入っている。

## 1本作る手順

1. **記事を選ぶ**：会話形式の記事（`note_*_kaiwa_kaisetsu.md`、第22問は `note_*_dai22mon_*.md`）から、1本4〜6分になるよう章を2〜3つ選ぶ。
   記事1本を3〜5回に分けるのが目安（第1回＝時系列と最大のワナ、以降＝計算、申請書、まとめ）。
2. **下書きを作る**：
   ```bash
   python3 article2script.py ../../note-articles-Kijyutsu/R7/Q21/note_R7_dai21mon_tochi_kaiwa_kaisetsu.md \
       --id R7_Q21_ep02 --chapters 2-3 > episodes/R7_Q21_ep02.json
   ```
3. **Claude Code に仕上げさせる**（依頼文の例）：
   > `tools/video/README.md` の「台本の仕上げのルール」に従って、`episodes/R7_Q21_ep02.json` を仕上げてください。
4. **プレビュー**（音声なし・数秒で終わる）で図の割り当てと字幕のはみ出しを確かめる：
   ```bash
   python3 render.py episodes/R7_Q21_ep02.json --preview   # out/R7_Q21_ep02/frames/ に場面ごとの静止画
   ```
5. **本番の書き出し**（4分の動画で約2分）：
   ```bash
   python3 render.py episodes/R7_Q21_ep02.json                 # クラウド・ローカルどちらでも（Open JTalk）
   python3 render.py episodes/R7_Q21_ep02.json --tts voicevox  # ローカルPCで VOICEVOX を起動しているとき（声の質が上がる）
   ```
6. **見て直す**：`out/<id>/<id>.mp4` を見て、読み間違いは `yomi`（その場面だけ）か `yomi_dict.json`（全体）に足して書き出し直す。
7. **公開**：YouTube Studio に MP4 をアップロードし、`youtube.md` のタイトル・概要欄（チャプター・クレジット込み）・タグを貼り、`thumbnail.png` をサムネイルに、`<id>.srt` を字幕に設定する。

複数回をまとめて作るときは、Claude Code に「サブエージェントを並列で走らせて、R6〜R7の第21問の第1回の台本を作り、書き出してプレビューを確認して」と頼めばよい（記事のサブエージェント量産と同じ）。

## KaisetsuScript の書き方

```jsonc
{
  "format": "kaisetsuscript/1",
  "id": "R7_Q21_ep01",                       // 書き出し先 out/<id>/ とファイル名
  "source": "元にした記事のパス（記録用）",
  "series": "画面上部の帯に出すシリーズ名",
  "base_dir": "../../../note-articles-Kijyutsu/R7/Q21/zu",   // image の基準（この台本ファイルからの相対パス）
  "tts": "openjtalk",                        // または voicevox
  "characters": {
    "aiko": {"name": "藍子", "side": "left", "voice": "aiko", "cls": ""},
    "tori": {"name": "トリ先生", "side": "right", "voice": "tori", "cls": "tori"}
    // 本物のキャラクター画像を使うときは "images": {"closed": "口を閉じた.png", "open": "口を開いた.png"} を足す
  },
  "intro":  {"jingle": "opening", "top": "小見出し", "title": "大見出し（\nで改行）", "bottom": "副題"},
  "chapters": [
    {"title": "章の名前（YouTubeのチャプターになる）",
     "beats": [
       {"speaker": "tori", "text": "セリフ", "image": "zu04.png", "crop": [0.04, 0.1, 0.92, 0.92], "yomi": {"325°": "さんびゃくにじゅうごど"}},
       {"speaker": "aiko", "text": "セリフ（図は前の場面のまま続く）"},
       {"speaker": "tori", "text": "…", "bullets": {"heading": "見出し", "items": ["箇条1", "箇条2"]}},
       {"speaker": "tori", "text": "…", "card": {"top": "", "title": "大きな文字", "bottom": ""}},
       {"image": "zu05.png", "seconds": 3}          // 話者なしで図だけを見せる
     ]}
  ],
  "outro": {"jingle": "ending", "seconds": 5, "top": "次回", "title": "…", "bottom": "…"},
  "thumbnail": {"top": "…", "title": "…", "bottom": "…"},
  "youtube": {"title": "…", "description": "…", "credits": ["…"], "tags": ["…"]}
}
```

- 画面（図・箇条書き・カード）は、次に指定するまで前の場面のものが続く。`"image": "none"` で空にする。
- 長いセリフは、文の切れ目で字幕のページ（84字まで）に自動で分かれ、ページごとに音声を作る。
- `crop` は図の一部を拡大する（左・上・右・下を0〜1の割合で）。白い余白は自動で切り落とす。

## 台本の仕上げのルール（Claude Code が下書きを仕上げるとき）

1. **数値・結論は記事のまま**。セリフを短くするのはよいが、答え・条文・数値を変えない。記事にない解説を足さない。
2. **電卓のキー列・長い式は読み上げない**。結論の座標だけを言い、式は図（zu/）か `bullets` に回す。
3. 画像挿入マーカー（`image_hint`）の説明に合う図を `_candidates` から選んで `image` に書く。図のない場面は `bullets` か `card` を使う。`image_hint` と `_candidates` と `_memo` は最後に消す。
4. 1つのセリフは2〜3文まで。話者が交互になるように（同じ話者が3回続かないように）する。
5. **読みを確かめる**：`python3 check_yomi.py episodes/<id>.json --words` で読みの一覧を出し、音読み・訓読みの取り違えを
   `yomi_dict.json`（全体）か beat の `yomi`（その場面だけ）にカタカナで足す（下の「読み間違い・間の直し方」）。
   小数・角度・アルファベットの点名は自動で読むので、`yomi` に書かない。
6. 冒頭の1場面目で「今回の問いと最大のワナ」を言い、最後の場面で次回の予告をする（視聴維持のため）。
7. 予備校の改題の要素・個人の演習結果は台本に入れない（記事のルールと同じ）。
8. `youtube.credits` に音声合成のクレジットを必ず書く（下の「ライセンス」）。

## 読み間違い・間の直し方

### 1. まず聞かずに一覧で確かめる
```bash
python3 check_yomi.py episodes/<id>.json --words   # 台本に出てくる漢字の語と、その読みの一覧（重複なし）
python3 check_yomi.py episodes/<id>.json           # 場面ごとの読み（カタカナ）と、間（⏸秒数）の入る位置
```
`--words` の一覧を上から眺めると、音読み・訓読みの取り違え（後視→アトシ、辺→アタリ、外→ガイ など）がすぐ見つかる。
読みの一覧は Open JTalk の読み。VOICEVOX で書き出すときも、同じ辞書が先に当たる。

### 2. 読み違いを直す
| 直したい範囲 | 書く場所 | 書き方 |
|---|---|---|
| 全部の台本で | `yomi_dict.json` | `"後視": "コウシ"` |
| その場面だけ | 台本の beat の `yomi` | `"yomi": {"甲野太郎": "コウノタロウ"}` |

- **読みはカタカナで書く**（ひらがなで書いても自動でカタカナに直す）。ひらがなのままだと Open JTalk が漢字に直して解析し直し、「はちいち」を「八一＝ハチジューイチ」と読んでしまう。
- 前後の語ごと登録すると、ほかの場所に影響しにくい（例：「外」ではなく「の外」、「曲がり」ではなく「曲がり点」）。
- 長い語が先に当たる（「地積測量図」は「地積」より先）。
- 次のものは自動で直るので、登録しなくてよい：小数（25.81→ニジューゴテンハチイチ）、角度（325°06′51″ と 325度06分51秒→「ゼロ」を読まない）、アルファベット1文字ずつの点名（AB→エービー、C→シイ）、「問1」（トイイチ）、＝・→・〜・−。

### 3. 間（ま）を入れる
自動で入る間：文の終わり「。」0.35秒、「！」「？」0.4秒、「……」「・・・」「――」0.65秒（言いよどみとして、読み上げずに黙る）。
それ以外のところに間を入れたいときは、セリフ（text）か読み（yomi）に記号を書く。字幕には出ない。

| 記号 | 長さ | 例 |
|---|---|---|
| `\|` | 0.3秒 | `"text": "観測角は、\|時計回りの角度。"` |
| `\|\|` | 0.7秒 | `"text": "答えは……\|\|C、D、Eの折れ線。"` |

間の秒数を全体で変えるときは `tts.py` の `PAUSES` を直す。読点「、」では音声を切らない（Open JTalk が自然な短い間を入れる）。

### 声の加工（ボイスチェンジャー）
`voices.json` の各声に `fx` を書くと、音声合成のあとに声を加工する。トリ先生は、成人男性の声を高くしてマスコットキャラクター風にしている
（ラジオやWEB番組のマスコットのような「機械で変換した声」の作り方。特定のキャラクターの声のまねではない）。

```json
"tori": {"htsvoice": "...", "speed": 1.25, "fx": {"pitch": 1.4, "bright": 3}}
```

| 項目 | 意味 | 目安 |
|---|---|---|
| `pitch` | 声の高さの倍率（声の通り道ごと上げるので「変換した声」になる。話す速さは変わらない） | 1.25 少し高め／1.4 マスコット風／1.6 かなり高め |
| `tempo` | 話す速さの倍率（加工のあと） | 1.0〜1.1 |
| `bright` | 高い音を持ち上げる量（dB）。こもりを取って軽くする | 2〜3 |

聞き比べ用の見本は `out/voice_samples/` に書き出す（README の作り方は会話のログ参照。`fx` を変えて `render.py` で書き出し直せば全編に反映）。
VOICEVOX でも同じ `fx` が使える。元の声が自然なぶん、加工した声も聞きやすい。

### 4. 確かめて書き出し直す
`check_yomi.py` で読みと⏸の位置を確かめてから `render.py` を実行する。気になった箇所は、`out/<id>/<id>.srt`（字幕）の時刻で動画を頭出しすると探しやすい。

## 声とライセンス

| 用途 | 声 | ライセンス・表記 |
|---|---|---|
| トリ先生（Open JTalk） | nitech_jp_atr503_m001（名古屋工業大学） | 修正BSD |
| 藍子（Open JTalk） | tohoku-f01（東北大学 伊藤・能勢研究室） | CC BY 4.0 → 概要欄にクレジット必須 |
| 本番の推奨（VOICEVOX） | `voices.json` の `voicevox` で speaker ID を指定 | キャラクターごとの規約に従い「VOICEVOX:キャラ名」を概要欄に書く |

Open JTalk の声は機械的なので、公開する本番はローカルPCで VOICEVOX を使うのがよい（`--tts voicevox`）。
VOICEVOX は https://voicevox.hiroshiba.jp/ から入れて起動しておくだけで、`render.py` から呼べる。

## これからの改良の候補

- **アバター**：今は仮のSVG。キャラクターシートから「口を閉じた・開いた」の2枚を作り、`assets/characters/` に置けば全台本に反映される（置き方は `assets/characters/README.md`）。目パチ用の絵の対応は今後の候補。
- **図の読みやすさ**：zu/ の図はnote用（4:3）で文字が小さい。動画用に16:9・大きい文字で描き出す設定を作図スクリプトに足すと見やすくなる。
- **ショート動画**：同じ台本から縦1080×1920のショート（1つのワナだけ・60秒）を書き出すレイアウト。
- **択一式**：一問一答ドリル・4コマの肢を「藍子の誤答→トリ先生の訂正」の60秒動画にする。
