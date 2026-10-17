#!/usr/bin/env python3
"""f01〜f12・m01〜m07 の直前復習カードの見出し画像プロンプトを、1つのファイル（00-midashi-prompts.md）にまとめる。
使い方: python3 note-articles/chokuzen-fukushuu-card/src/make_midashi.py"""
import sys, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
sys.path.insert(0, str(HERE))
import cardlib
sl = cardlib.sl

S = [  # (ファイル名, 論点名, t1, t2, hot, サブタイトル, 左の絵, 右の絵)
 ("f01-shinsei-souron", "不動産登記法／申請総論", "申請の入口で", "迷わないために", "迷わない", "直前復習カード　申請総論",
  "A desk with a stack of application forms, a rubber stamp, an inkpad and a brown envelope, with a faceless pictogram clerk beside it.",
  "A laptop showing an online filing screen with an attached document icon and a paper clip, with a small calendar next to it."),
 ("f02-tatemono-bunkatsu-gappei", "不動産登記法／建物の分割・合併・合体・滅失・変更", "つなぐ・分ける・消す", "建物の登記を整理", "整理", "直前復習カード　建物の分割・合併・合体",
  "Two small isometric houses joined by a short corridor into one house, with a pale ledger page beside them.",
  "One house split into two by a thin line, and a third small house with a crossed-out ledger page beside it."),
 ("f03-kubun-tatemono", "不動産登記法／区分建物・敷地権・共用部分", "マンションの部屋と", "土地はセット？", "セット", "直前復習カード　区分建物と敷地権",
  "An isometric apartment building with one unit highlighted by a blue outline, standing on a pale beige land plot.",
  "A registry ledger page with a small land plot icon and a building icon joined by a thin line, and a rubber stamp."),
 ("f04-tochi-bunpitsu-gappitsu", "不動産登記法／土地の分筆・合筆・地積更正", "分ける・くっつける", "土地の登記の落とし穴", "落とし穴", "直前復習カード　分筆・合筆・地積更正",
  "One land plot divided by a dotted line into two plots, with small boundary stakes at the corners.",
  "Two neighboring land plots merged into one, with a measuring tape and a pale ledger page beside them."),
 ("f05-tatemono-nintei", "不動産登記法／建物の認定・個数・種類構造床面積", "それは建物？", "床面積はいくつ？", "床面積", "直前復習カード　建物の認定と床面積",
  "An isometric house with a floor plan drawn as a flat outline beside it, and a measuring tape across the floor.",
  "A small shed, a garage and a house side by side, with a faceless pictogram surveyor holding a clipboard."),
 ("f06-chizu-sokuryozu", "不動産登記法／土地の滅失・地図・地積測量図・土地所在図", "地図と図面は", "何が違う？", "違う", "直前復習カード　地図・地積測量図",
  "A rolled land map with plot outlines and numbers drawn on it, beside a magnifying glass.",
  "A survey drawing sheet with boundary lines, small corner markers and a ruler, beside a surveying tripod."),
 ("f07-hyodaibu-shoyusha", "不動産登記法／表題部所有者・所有権の登記", "表題部の所有者は", "だれが直せる？", "直せる", "直前復習カード　表題部所有者・所有権の登記",
  "A registry ledger page with an owner name box on its title section, and a faceless pictogram person pointing at it.",
  "Two faceless pictogram people shaking hands over a signed paper, with a small house and a land plot behind them."),
 ("f08-tochi-hyodai-chimoku", "不動産登記法／土地の表題・地目・地積", "地目と地積は", "現況で決まる", "現況", "直前復習カード　土地の表題・地目・地積",
  "A land plot seen from above, half crop field with plants and half building lot, divided by a thin line.",
  "A pale ledger page with category labels and a measuring tape lying across it."),
 ("f09-touki-seido-souron", "不動産登記法／登記制度・総則", "保存期間と管轄", "数字と場所を確認", "確認", "直前復習カード　登記制度の総則",
  "A shelf of document boxes with calendar pages on them, and a faceless pictogram clerk placing one box.",
  "A small map with two registry office buildings and an arrow between them, beside a rubber stamp."),
 ("f10-hikkai-tokutei", "不動産登記法／筆界特定・境界", "筆界特定は", "だれが何をする？", "だれが", "直前復習カード　筆界特定・境界",
  "Two neighboring land plots with a boundary line between them and boundary stakes, and a question-mark shaped signpost.",
  "A faceless pictogram officer holding a document, with a small notice envelope and a surveying tripod."),
 ("f11-tatemono-zumen", "不動産登記法／建物図面・各階平面図", "図面が要る登記", "要らない登記", "要らない", "直前復習カード　建物図面・各階平面図",
  "A building drawing sheet showing the house outline on a site plot, with a ruler.",
  "A floor plan sheet showing rooms and walls, stacked over a second floor plan sheet."),
 ("f12-tourokumenkyozei", "不動産登記法／登録免許税", "登録免許税は", "あとの個数で計算", "個数", "直前復習カード　登録免許税",
  "A small calculator and a stack of coins beside a pale ledger page with two land plot icons.",
  "A rubber stamp, a revenue-stamp style paper sheet and a small cash tray with a few coins."),
 ("m01-kyoyu-shoyuken-senyu", "民法／共有・所有権・占有", "共有・占有で", "できることの範囲", "範囲", "直前復習カード　民法の共有・占有",
  "A house shared by three faceless pictogram people standing around it, each holding a small share card.",
  "A faceless pictogram person standing at a gate of a land plot with a small lock and a key."),
 ("m02-ishi-hyoji", "民法／意思表示・無効取消", "だまされた・勘違い", "守られるのはだれ？", "だれ", "直前復習カード　民法の意思表示",
  "Two faceless pictogram people facing each other over a contract paper, one of them with a question mark above the head.",
  "A third faceless pictogram person holding a small shield beside a house and a signed paper."),
 ("m03-bukken-hendo", "民法／物権変動・対抗要件", "登記がないと", "勝てない相手は？", "勝てない", "直前復習カード　民法の物権変動",
  "A house with two faceless pictogram buyers on both sides, each holding a contract paper, and a ledger page in the middle.",
  "A rubber stamp pressing on a ledger page, with a small ribbon tag marking the first registered name."),
 ("m04-jikou", "民法／時効・条件期限", "時効の更新と", "完成猶予の整理", "整理", "直前復習カード　民法の時効",
  "A large calendar with a few pages flipping, a sand timer and a land plot beside it.",
  "A faceless pictogram person holding a letter, with a small clock that shows the timer being reset."),
 ("m05-youeki-tanpo", "民法／用益権・担保物権", "地上権と質権の", "ルールを確かめる", "ルール", "直前復習カード　用益権・担保物権",
  "A house standing on a rented land plot, with a small signboard at the plot edge.",
  "A pledged item box with a ribbon tag and a faceless pictogram lender holding a key."),
 ("m06-dairi", "民法／代理", "無権代理と相続", "地位の重なりで決まる", "重なり", "直前復習カード　民法の代理",
  "A faceless pictogram agent handing a contract paper to a faceless pictogram buyer, with the owner standing behind.",
  "Two overlapping circles drawn on a sheet, with small figure icons placed in each circle."),
 ("m07-souzoku", "民法／相続・親族", "遺産共有の解消は", "遺産分割で行う", "遺産分割", "直前復習カード　民法の相続",
  "A family house with several faceless pictogram relatives sitting around a table with a document.",
  "A will paper with a ribbon and a ledger page showing a name being written in."),
]

def check(t1, t2, hot, sub):
    assert len(t1) <= 16 and len(t2) <= 16, (t1, t2)
    assert hot in t2, (hot, t2)
    assert len(sub) <= 28, sub
    for s in (t1, t2, sub):
        assert not re.search(r"緑|木|ツリー|D\d{4}|誤答|復習対象", s.replace("直前復習カード", "")), s

L = ["# 直前復習カード　各回の見出し画像プロンプト（f01〜f12・m01〜m07）", "",
     "直前復習カードの各論点（不動産登記法12・民法7）に付ける、note用の見出し画像のプロンプトを1つにまとめたファイルです。トリ先生と藍子を描きます。画像は生成していません。", "",
     "## 使い方", "",
     "1. ChatGPT（画像生成）に、キャラクターの参照画像（トリ先生と藍子の基準画像。`CHATGPT_MANGA_WORKFLOW.md` §3の6枚）を添付します。",
     "2. 「左がトリ先生（ずんぐりした鳥の先生）、右が藍子（若い女性の受験生）」と一言添えます。",
     "3. 下のコードブロックを、論点ごとにそのまま貼ります。大きさは1280×670pxです（noteの見出し画像の推奨比率1.91:1）。",
     "4. 生成後は、タイトルとサブタイトルの文字が一字ずつ合っていること、漢字が日本の字形であること、藍子の手・指が正しいこと、背景が透過していないことを目視で確かめます。誤字が出たときは、プロンプトを直して作り直します。", "",
     "画像の中に載る文字は、タイトル2行とサブタイトル1行だけです。個人の演習結果・肢の番号・年度・図番は入れません。区分建物（f03）にも見出し画像を用意しました。調査士法（c01・c02）は対象外です。", "",
     "## 一覧", "", "| 論点 | 資料 | タイトル | サブタイトル |", "|---|---|---|---|"]
for slug, name, t1, t2, hot, sub, left, right in S:
    check(t1, t2, hot, sub)
    L.append(f"| {name} | [{slug}.md]({slug}.md) | {t1}／{t2} | {sub} |")
L.append("")
for k, (slug, name, t1, t2, hot, sub, left, right) in enumerate(S, 1):
    p = sl.midashi_prompt(dict(t1=t1, t2=t2, hot=hot, sub=sub, left=left, right=right))
    L += [f"## {k}．{name}（{slug}）", "",
          f"- タイトル1行目：{t1}", f"- タイトル2行目：{t2}（「{hot}」を赤みのあるオレンジ）", f"- サブタイトル：{sub}", "",
          "```text", p, "```", ""]
(OUT / "00-midashi-prompts.md").write_text("\n".join(L), encoding="utf8")
print("ok", len(S))
