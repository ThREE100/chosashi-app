# ChatGPTに貼る指示文（GitHubから直接読み込ませる形・毎日ドリル 第1日（夜） 学習まんが）

使い方：GitHubと接続したChatGPTに、キャラクターシート_トリ先生_01〜03 と キャラクターシート_I-01〜03 の6枚を添付し、「ここから」〜「ここまで」を貼る。1回の返事で1ページだけ作らせ、2ページ目からは同じチャットで下の1行を送る（全20ページ＋見出し画像2枚）。
ChatGPTがリポジトリを読めなかったときは、`daily-drill/manga/pm/day001-pm-manga_prompts.md` の該当ページのコードブロックの中身を、そのまま全文貼る（6枚の添付と一言はそのまま）。

**図のあるページ**（下の一覧）は、そのページの図のPNGを、上のURLから保存して一緒に添付する（ChatGPTに図を描かせない。添付した図をそのまま置かせる）。生成された画像で図が崩れていたら、手元で `python3 tools/gakushu_manga/paste_fig.py <生成した画像> daily-drill/manga/pm/day001-pm-manga_prompts.md <ページ番号>` を実行すると、正確な図が枠に貼り直される。

- 2ページ目：PM-01_mondai.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_mondai.png
- 4ページ目：PM-01_housha.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_housha.png
- 7ページ目：PM-01_vector.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_vector.png
- 13ページ目：PM-01_kouten.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_kouten.png
- 14ページ目：PM-01_zahyou.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_zahyou.png
- 19ページ目：PM-01_kotae.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_kotae.png

---ここから---

接続しているGitHubのリポジトリ ThREE100/chosashi-app（ブランチ main）から、次のファイルを読んでください。
https://github.com/ThREE100/chosashi-app/blob/main/daily-drill/manga/pm/day001-pm-manga_prompts.md

このファイルの見出し「## 1ページ目：扉：3つの点と地積を出す」の下にある ``` で囲まれたプロンプトを、1文字も変えずに（要約・翻訳・言い換えをせずに）使って、画像を1枚作ってください。コードブロックの外の説明文と、ほかの見出しのプロンプトは使いません。

- 添付した6枚のうち、鳥の3枚（キャラクターシート_トリ先生_01〜03）が先生、女性の3枚（キャラクターシート_I-01〜03）が生徒です。
- 名前・役割名は画像のどこにも書かないでください。話し手は、絵と吹き出しのしっぽで見分けます。
- 大きさは 1024×1536（縦長）。作るのはこの1ページだけです。
- プロンプトに「FIGURE SLOT」があるページでは、添付した図の画像を、指定の枠にそのまま置いてください。図を描き直したり、線・文字・数字を変えたりしないでください。
- 作る前に、読み込んだプロンプトの最初の1行（「Draw page 1 of 20 …」で始まる行）をそのまま返事に書いて、正しいプロンプトを読めたことを示してから画像を作ってください。読めなかったときは、画像を作らずに「読めなかった」と答えてください。

---ここまで---

2ページ目以降は、同じチャットで次の1行だけを送る（○に数字）。図のあるページは、その図のPNGを添付してから送る。
「同じファイルの『## ○ページ目：…』の見出しの下のプロンプトで、同じやり方で次の1枚を作ってください。最初の1行を書いてから作ってください。」

途中のページから作り直すとき（例：4ページ目から）は、上の「ここから」〜「ここまで」の『## 1ページ目：扉：3つの点と地積を出す』をそのページの見出しに、「Draw page 1 of 20」をそのページの番号に替えて貼る。

見出し画像は、次の1行を送る（大きさはプロンプトのとおり）。
「同じファイルの『## 見出し画像（note用 1280×670）』の見出しの下のプロンプトで、同じやり方で1枚作ってください。最初の1行を書いてから作ってください。」（Instagram用は見出しを『## 見出し画像（Instagram用 1080×1440）』に替える）

ページの見出し一覧（コピー用。図を添付するページに印）：

- ## 1ページ目：扉：3つの点と地積を出す
- ## 2ページ目：図で見る：求める3つの点　← 図を添付：PM-01_mondai.png
- ## 3ページ目：つまずき：観測角の向き
- ## 4ページ目：放射①：後視の向きを出す　← 図を添付：PM-01_housha.png
- ## 5ページ目：放射②：点Pの向きと座標
- ## 6ページ目：放射③：点Qと四捨五入
- ## 7ページ目：交点①：点Rの考え方　← 図を添付：PM-01_vector.png
- ## 8ページ目：交点②：3本の矢印を引き算で作る
- ## 9ページ目：交点③：たすき掛けで t を出す式
- ## 10ページ目：交点④：分子（w と v）
- ## 11ページ目：交点⑤：分母（u と v）
- ## 12ページ目：交点⑥：t と点R
- ## 13ページ目：交点⑦：点Rを図で確かめる　← 図を添付：PM-01_kouten.png
- ## 14ページ目：座標法①：順番と式　← 図を添付：PM-01_zahyou.png
- ## 15ページ目：座標法②：Yの差を4つ出す
- ## 16ページ目：座標法③：掛けて足す
- ## 17ページ目：座標法④：2で割って切り捨て
- ## 18ページ目：座標法⑤：電卓なら対角線で1回
- ## 19ページ目：答えの図　← 図を添付：PM-01_kotae.png
- ## 20ページ目：まとめ：この問題のポイント