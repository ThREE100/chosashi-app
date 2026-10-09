"""D1578・D0198・D1085 の4コマ解説図解の設計データ（SPEC）と見出し画像の設定（HEADER）。

使い方（ブランチ claude/kind-bell-y3f106 の tools/drill/manga/ で）:
  1. manga_specs.py に次の2行を足す（SPECS の定義と HEADERS の定義のあとに）。
       from D1578_D0198_D1085_spec import SPEC, HEADER
       SPEC["header"] = HEADER; SPECS[SPEC["fid"]] = SPEC
     もしくは SPEC の内容をそのまま manga_specs.py の SPECS["D1578-D0198-D1085"] = dict(...) に貼り、HEADER は HEADERS["D1578-D0198-D1085"] に入れる。
  2. python3 tools/drill/manga/gen_prompts.py D1578-D0198-D1085 && python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1578-D0198-D1085_prompt.md
このリポジトリには、生成済みの D1578-D0198-D1085_prompt.md（ChatGPT貼付用）を置いてある。"""

SPEC = dict(
    ippatsu=True, purpose=True,
    id="D1578・D0198・D1085", fid="D1578-D0198-D1085", topic="不動産登記法／区分建物・敷地権・共用部分", src="R02-Q14エ／H18-Q19イ／H27-Q16ア",
    truth="D1578＝×・D0198＝〇・D1085＝〇（D1578は『要しない』と言い切る誤った記述）",
    miscon="D1578は3回とも〇と答えて誤解（2026-10-05・10-08・10-09）。D0198は〇で正解",
    article="note-articles/r2-mondai/q14-shikichiken.md",
    art_head="R02-Q14エ（分離処分可能規約で敷地権にしないなら、規約の定めを証する情報が必要）を軸に、H18-Q19イ（敷地権とならない事由を証する情報）・H27-Q16ア（分離処分可能規約があるときは規約を証する情報が必要）を対比",
    letters="",
    design=[
        "【出題者のひっかけ】D1578は、場面の説明（所有者が同じ・規約で分離処分を可能と定めた・敷地権とならない）をD1085と一字違わずに並べ、最後の一句だけを『提供することを要しない』に変える。『敷地権とならない』という前提から、『敷地権の書類はいらない』と読ませる。",
        "【受験者の勘違い・定着していない点】①『敷地権にならない＝敷地権の登記がない＝敷地権に関する書類は要らない』と考える。②『規約を証する情報』を、敷地権が生じるとき・規約敷地の書類として覚えているため、敷地権にならない場面に結びつかない。③D0198のように『事由を証する情報』と抽象的に書かれていれば〇と答えられるのに、D1578のように『規約の定めを証する情報』と具体的に書かれ、末尾が否定形（要しない）になると、同じ内容だと気づけない。（①〜③は、ユーザーの回答記録から立てた推測。D1578は3回とも〇、D1577は3回とも×で、規約の証明が要る場面と要らない場面を取り違えている形が両方に出ている）",
        "【対比する制度】「敷地権になるとき」⇔「敷地権にならないとき」：どちらの場面でも添付情報は要るが、書類が違う（結論が逆になるのは、『ならないから要らない』という推論のほう）。敷地権になるときは、規約敷地の規約や割合の規約などを証する情報（令別表12項ヘ）。ならないときは、その事由を証する情報（同項ホ）で、分離処分可能規約が事由なら、その規約の定めを証する情報。",
        "【型の選び方】型：型4（＋型3の理由）。D1085とD1578は、場面の説明が同じで、最後の一句だけが逆の双子の肢（D0198は同じことを抽象的に問う）。型4でコマ1に3肢を並べて『どこで結論が分かれるか』を示し、同じ型でも、1肢が3回とも同じ誤りなので、結論だけでなく『なぜ、ならないときにも書類が要るのか』をコマ2の理由カードで示す。",
        "記事の範囲：R02-Q14エ（敷地権とならないときも、規約の定めを証する情報が必要。不動産登記令別表12項）、H18-Q19イ（令別表12項添付情報欄ホ。敷地権とならない事由を証する情報。分離処分可能規約が代表例）、H27-Q16ア（本来なら敷地権になるはずの土地の所有権について、分離処分を可能とする規約を定めたことにより敷地権とならない場合は、規約の定めを証する情報。令別表12項添付情報ホ）。『本来なら敷地権になるはず』『例外』という整理は、H27-Q16アの記事の言い方による。",
        "extra_refs：令別表12項添付情報欄ヘ（敷地権が存するとき：規約敷地の規約、割合の規約、他の登記所の土地の登記事項証明書）は、法令DB（note-articles/laws/fudousan-touki-rei-betsuhyou.md）で確認した。区分所有法22条1項本文・ただし書も法令DB（kubunshoyuu-hou.md）で確認した。いずれも、3肢の記事には書いていない対比で、ユーザーに『記事にない整理』と伝える。図には、令別表12項以外の条文番号を入れない（ホ・ヘの枝番は、ステップ2のカードにだけ入れる）。",
        "同系統で今回は図に入れない肢：D1924（地上権版。所有権でなく地上権でも同じ書類が要る。×）、D1577（規約敷地の分筆では規約を設定したことを証する情報は要しない。〇）。D1577と合わせて『規約の証明が要る場面』を整理すると、取り違えの根本が直る（別の4コマ D0402-D0405-D1577-D1796 と合わせて読む）。",
        "登場人物：当事者の記号（Ａ〜Ｚ）は使わない。建物・土地・書類はアイコンと文字ラベルで示す。",
        "矢印の意味：矢印は使わない。コマ1は表、コマ2は左右のカード、コマ3は3枚のステップカード。",
        "配色：コマ1〜3は印（✓✕）を付けない（書類が要る・要らないは文字で書く）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。",
        "コマの使い方：コマ1＝small（表が横いっぱいに要るので、キャラは極小）、コマ2＝既定（通常キャラ・台詞2つ。左右のカード）、コマ3＝faces（左に3枚のカード、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝既定（暗記3点と結論）。",
    ],
    review=[
        "初見の読者：コマ1の表で、D1085とD1578が『最後の一句だけが違う』こと、D0198が同じ内容の抽象的な言い方であることが言える",
        "肝の確認：①敷地権になるときも、ならないときも、添付情報は要る（書類が違う） ②ならないときは、その事由を証する情報（令別表12項ホ）。分離処分可能規約なら、その規約の定めを証する情報 ③『要しない』と言い切るD1578は×、D0198とD1085は〇",
        "構成表の全文言を記事と突き合わせ：『敷地権とならない事由』『規約の定めを証する情報』『提供しなければならない』『提供することを要しない』『本来なら敷地権になる（例外）』。記事にない対比（ヘの書類）は、法令DBで確認した旨を設計メモに書いてある",
        "コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（small→既定→faces→既定）。コマ4のチェックに、3肢の〇×を別に示す",
    ],
    lead1="区分建物の表題登記で、敷地の所有権が敷地権にならないとき、添付情報はどうなるのでしょうか。「敷地権にならないのだから、書類は要らない」と考えてよいのでしょうか。",
    title="敷地権にならなくても、事由を証する情報は要る", title_hl="事由を証する情報は要る",
    panels=[
        dict(label="①　3つの肢は、同じ場面", chars="small", mood="curious, calm mood",
             bubbles=[("藍子", "ならないなら、書類は要しませんよね？", None, "ならないなら、\n書類は要しませんよね？"),
                      ("トリ先生", "そこが罠。3肢を並べて見るのよ", "そこが罠", "そこが罠。\n3肢を並べて見るのよ")],
             fig=["A wide table that fills the full panel width. The header row is dark navy with white text and has three columns: 「肢」, 「敷地権とならない理由の書き方」, 「添付情報の言い方」. The three body rows have the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow.",
                  "Body row 1: 「肢D0198」, 「敷地権とならない事由」, 「提供しなければならない」.",
                  "Body row 2: 「肢D1085」, 「分離処分を可能とする規約」, 「提供しなければならない」.",
                  "Body row 3: 「肢D1578」, 「分離処分を可能とする規約」, 「提供することを要しない」.",
                  "Above the table, one wide card of the same pale gray fill and dark navy outline with the dark navy heading 「3肢に共通の場面」 and one body line 「敷地の所有権の登記名義人が、区分建物の所有者で、所有権が敷地権とならない」.",
                  "The rows have clearly different texts; the texts are NOT identical, so copy each character exactly as given."]),
        dict(label="②　どちらも書類は要る",
             bubbles=[("藍子", "ならないなら、書類は要らないのでは？", None, "ならないなら、\n書類は要らないのでは？"),
                      ("トリ先生", "ならなくても、事由の書類が要るのよ", "事由の書類", "ならなくても、\n事由の書類が\n要るのよ")],
             fig=["Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.",
                  "Left card, heading 「敷地権になるとき」, two body lines: 「基本：所有者が同じなら、敷地権になる」, 「書類：規約敷地や割合の規約など」.",
                  "Right card, heading 「敷地権にならないとき」, small tag 「肢D0198・肢D1085・肢D1578」, two body lines: 「例外：分離処分を可能とする規約など」, 「書類：ならない事由を証する情報」.",
                  "The two cards have clearly different texts; the texts are NOT identical."]),
        dict(label="③　本番での読み方3ステップ", chars="faces", mood="thoughtful then confident mood",
             bubbles=[("藍子", "ならないなら要しない、と読みました", None, "ならないなら要しない、\nと読みました"),
                      ("トリ先生", "それが罠。事由を証する情報が要るのよ", "事由を証する情報", "それが罠。事由を\n証する情報が要るのよ"),
                      ("藍子", "事由って、規約の定めのことですか？", None, "事由って、規約の\n定めのことですか？"),
                      ("トリ先生", "そう。規約で分離処分を可能にした場合よ", "規約で分離処分を可能", "そう。規約で分離処分を\n可能にした場合よ")],
             fig=["Three step cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading, with no check mark and no cross. The step cards are separated only by a small empty gap, with nothing drawn between them.",
                  "Step card 1: heading 「ステップ1　場面を読む」, body 「敷地権になるのか、ならないのか」.",
                  "Step card 2: heading 「ステップ2　ならないなら事由を探す」, body 「規約で分離処分を可能にしたなら、規約の定めを証する情報（令別表12項ホ）」.",
                  "Step card 3: heading 「ステップ3　言い切りの語を見る」, a dark navy ribbon tag with large white text 「ひっかけ：ならないから要しない」, body 「この場面で、要しないは誤り」.",
                  "There is no check mark and no cross anywhere in this panel."]),
        dict(label="④　3肢の答え",
             bubbles=[("藍子", "ならなくても、書類は要るんですね！", None, "ならなくても、\n書類は要るんですね！"),
                      ("トリ先生", "そう。事由の書類を忘れないことよ", "事由の書類", "そう。事由の書類を\n忘れないことよ")],
             fig=[], checklist=["敷地権にならなくても、その事由を証する情報は要る", "規約で分離処分を可能にしたなら、規約の定めを証する情報", "D0198は〇、D1085は〇、D1578は×（要しないは誤り）"]),
    ],
    band1="敷地権にならなくても、事由の書類は要る", band2="問題D1578・D0198・D1085　正解×・〇・〇（R02-Q14エ／H18-Q19イ／H27-Q16ア）",
    ver="v01",
    rev=["2026-10-09 v01：新規作成（ユーザー指示。D1578を3回続けて誤答していることから、D0198・D1085と対比して、敷地権にならなくても事由を証する情報が要ることを4コマにした。型は型4＋型3の理由）"],
)

HEADER = dict(h1="敷地権にならないとき", h2="書類は要らない？", hkey="要らない？",
              scene_l="a condominium building standing on a plot of land with an empty signpost board",
              scene_r="two blank document sheets and a rubber stamp beside a small registry book")
