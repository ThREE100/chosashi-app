"""D1795・D1798・D1799 の4コマ解説図解の設計データ（SPEC）と見出し画像の設定（HEADER）。v02（2026-10-11）。
R04-Q18ア・エ・オ（区分所有法 第5条の規約敷地の記事用。note-articles/joubun-nigate/kubunshoyuu-hou/art005-kiyaku-shikichi/ の4コマ5）。
既存版（prompt_4koma_05_bunri-shobun.md、v01）の構成（規約→抹消→移転の3枚カード＋理由）は保ち、最新ルールで整えた：
①コマ3を「勘違い⇔正しい整理」の左右カードから、理由（共有持分がなぜ敷地権か／なぜ土地だけ移せないか）の2枚カードに作り替え、
 理由を『条文の言い直し』ではなく、法73条1項（建物の登記が敷地権の登記としての効力を持つ）→2項（だから土地には移転の登記ができない）につないだ
②同じ文（共有持分も敷地権になる）が4か所に重なっていたのを整理 ③コマ2のカード・コマ4のチェック欄の文を短くした
④設計メモに回答履歴などの個人の記述は入れていない。"""

SPEC = dict(
    ippatsu=True, purpose=True,
    id="D1795・D1798・D1799", fid="D1795-D1798-D1799", topic="不動産登記法／区分建物・敷地権・共用部分", src="R04-Q18ア・エ・オ",
    truth="D1795＝×（誤った記述）・D1798＝〇（正しい記述）・D1799＝×（誤った記述）",
    miscon="共有持分と敷地権、持分だけ売るときの手順（規約、敷地権の登記の抹消、移転の順）",
    article="note-articles/r4-mondai/q18-shikichiken.md",
    art_head="R04-Q18のア（共有持分権を敷地権として丁区分建物の表題登記を申請できる）・エ（一部の区分建物についてのみ分離処分可能規約を設定できる）・オ（分離して処分するには前提として敷地権登記の抹消が必要）を、規約、抹消、移転の手順として1枚に整理",
    letters="",
    design=[
        "【出題者のひっかけ】『共有持分権を敷地権として』『敷地権である旨の登記がされた後の売買を原因とする共有持分権の移転の登記』と、持分と売買の話にして、敷地権と分離処分の原則が見えにくい書き方をする（記事 R04-Q18ア・オ）。エは『丁区分建物についてのみ』と、一部だけの規約を問う。",
        "【受験者の勘違い・定着していない点】（推測）①共有持分は敷地権にならないと思う。②敷地権である旨の登記がある土地の持分も、そのまま売買で移転できると思う。③分離処分可能規約は、区分所有者全員にそろえて設定しなければならないと思う。実際は、敷地利用権が数人で有する所有権なども分離処分できず（区分所有法22条1項）共有持分も敷地権になる／持分だけ移すには先に敷地権の登記を抹消する（法73条2項）／規約は一部の区分建物についてだけでも設定できる。",
        "【対比する制度】「原則：分離処分できない」⇔「分離処分を可能にする」：原則は専有部分と敷地利用権を分離して処分できない／規約に別段の定めを設ければ分離して処分でき、持分だけの移転登記ができる。持分だけ売るには、規約、敷地権の登記の抹消、移転の順になる（結論が逆になる点）。",
        "【型の選び方】型：型3（理由説明）。理由：結論（共有持分も敷地権／持分だけ売るには先に敷地権を抹消）を覚えても、『なぜ共有持分でも敷地権なのか』『なぜ土地だけ移せないのか』が分からないと崩れるため。コマ2で『原則→分離処分を可能にする→移転』の3枚（型2の当てはめ）を置き、コマ3は理由の2枚カードに作り替えた。理由は、条文の言い直し（敷地権の土地には移転できない）で止めず、法73条1項（建物の登記が敷地権の登記も兼ねる）→2項（だから土地だけの移転はできない）につないだ。",
        "記事の範囲：R04-Q18ア・エ・オ（区分所有法22条1項〈敷地利用権が数人で有する所有権などのとき、専有部分と一体で分離して処分できない。規約に別段の定めがあれば別〉、法73条2項〈敷地権である旨の登記をした土地には、敷地権の移転の登記ができない〉、一部の区分建物についてだけ分離処分可能規約を設定できる〈エ〉）。たとえば：Ａ・Ｂ共有の土地の上のマンションのＡの部屋（丁区分建物）で、Ａが持分だけを売るときは、まず分離処分可能規約を設定し、敷地権の登記を抹消する表題部の変更の登記を済ませる。",
        "extra_refs：①法73条1項『敷地権付き区分建物についての所有権又は担保権に係る権利に関する登記は、第四十六条の規定により敷地権である旨の登記をした土地の敷地権についてされた登記としての効力を有する』は、法令DB note-articles/laws/fudousan-touki-hou.md の第73条で確認した。コマ3の理由『建物の登記が、敷地権の登記も兼ねる→だから土地だけの移転の登記はできない』は、この1項と2項（記事オ）をつなぐ整理で、記事にはない（兄弟記事 art005 の部品7も1項には触れていない）。『兼ねる』は『敷地権についてされた登記としての効力を有する』の言い直し。立法趣旨としては断定していない。②共有が『数人で有する所有権』にあたるという当てはめは、区分所有法22条1項の文言（法令DB kubunshoyuu-hou.md）による。",
        "登場人物：当事者の記号は、事案の登場人物Ａ・Ｂだけ（コマ1の図の凡例で紹介してから使う）。建物・土地はアイコンと文字ラベルで示す。ピクトグラムは使わない。",
        "矢印の意味：矢印は使わない（取引も手続も流れもない）。コマ1は1枚の図と注記カード、コマ2は3枚の別カード、コマ3は上下2枚のカードとリボン。",
        "配色：コマ1〜3は印（✓✕）を付けない（できる・できないは文字で書く）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。",
        "コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（通常サイズのキャラが左右の端、図は中央。図は土地と建物のアイコンと注記だけで少ないので、小さくする必要がない）、コマ2＝none（3枚の幅広カードが主役）、コマ3＝faces（左に理由の2枚のカード、右に会話4つの縦並び。カードと会話の量が多いので顔アイコンにして場所を確保）、コマ4＝既定（両方・通常サイズ、暗記3点）。隣り合うコマで同じ見せ方が続かない。",
    ],
    review=[
        "初見の読者：コマ1で『Ａ・Ｂ共有の土地の上にＡの部屋（丁区分建物）があり、Ａは土地の持分だけを売りたい。共有持分は敷地権になるのか、持分だけ売れるのか』、コマ2で『原則は分離処分できない→規約で別段の定め→持分を移転（前提に敷地権の抹消）の3段』、コマ3で『共有は数人で有する所有権だから敷地権になる／建物の登記が敷地権の登記も兼ねるので、土地だけの移転の登記はできない』が言える",
        "肝の確認：①共有持分も敷地権になる（区分所有法22条1項） ②持分だけ移すには、規約→敷地権の登記の抹消（表題部の変更）→移転の順 ③敷地権の土地には移転の登記ができない（法73条2項）。その理由は建物の登記が敷地権の登記を兼ねる点（法73条1項） ④規約は一部の区分建物（丁）についてだけでもよい ⑤D1795＝×、D1798＝〇、D1799＝×",
        "構成表の全文言を記事・法令DBと突き合わせ：『数人で有する所有権』『専有部分と分離して処分できない』『規約に別段の定め』『一部の区分建物についてだけ』『敷地権の登記を抹消する表題部の変更の登記』『敷地権の移転の登記ができない』。法73条1項は記事にない（extra_refsに出典を書いた）",
        "コマ1〜3に印がなく、コマ4だけ青✓の暗記3点。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラは、図や会話が入らないコマ（コマ3の顔アイコンのみ）だけ小さくしている",
    ],
    extra_refs=[
        "不動産登記法73条1項・2項（法令DB note-articles/laws/fudousan-touki-hou.md 第73条）：1項＝敷地権付き区分建物についての所有権又は担保権に係る権利に関する登記は、敷地権である旨の登記をした土地の敷地権についてされた登記としての効力を有する（ただし書あり）。2項＝敷地権である旨の登記をした土地には、敷地権の移転の登記又は敷地権を目的とする担保権に係る権利に関する登記をすることができない（ただし書あり）。2項は記事のオの解説にあり、1項は記事にない",
        "『建物の登記が、敷地権の登記も兼ねる→だから土地だけの移転の登記はできない』：法73条1項と2項をつなぐ整理（記事にない）。『兼ねる』は1項の『敷地権についてされた登記としての効力を有する』の言い直しで、立法趣旨としては断定しない",
        "『共有は、数人で有する所有権』：区分所有法22条1項の文言（法令DB note-articles/laws/kubunshoyuu-hou.md）による当てはめ。記事アは『A・B共有かつ所有権登記済みのため、専有部分と共有持分権が一体化する』と書く",
    ],
    lead1="Ａ・Ｂが共有する土地の上に、Ａの部屋（丁区分建物）があります。Ａは、その土地の持分だけを売りたいと考えています。共有の持分は敷地権になるのでしょうか。また、持分だけを売るためには、何をしておく必要があるのでしょうか。",
    title="共有持分も敷地権になる。持分だけ売るには先に敷地権を抹消", title_hl="先に敷地権を抹消",
    panels=[
        dict(label="①　問いの事案", chars="side", mood="curious, calm mood",
             bubbles=[("藍子", "共有持分は、敷地権にならないのでは？", None, "共有持分は、\n敷地権にならないのでは？"),
                      ("トリ先生", "出たわね。『共有持分』に引かれたわね", "共有持分", "出たわね。\n『共有持分』に\n引かれたわね")],
             fig=["A diagram in the center region (about 56 percent of the panel width), with no arrow, no check mark, and no cross: one land plot icon with a pale gray fill and a dark navy outline, carrying a dark navy tag 「Ａ・Ｂ共有の土地」 and two small dark navy tags 「Ａ」 and 「Ｂ」 side by side on it that mark the two co-owners, and standing on it one apartment building icon in the same pale gray fill, carrying a dark navy tag 「丁区分建物（Ａの部屋）」. No person is drawn; the owners appear only as these letter tags.",
                  "A white note card with a dark navy outline beside the plot reads 「Ａは、土地の持分だけを売りたい」.",
                  "A small question badge 「敷地権になる？　持分だけ売れる？」 with a pale gray fill and a dark navy outline sits above the diagram (a question badge only, with no check mark and no cross)."]),
        dict(label="②　出題者のねらい", chars="none", mood="clear, calm infographic mood",
             bubbles=[],
             fig=["A full-width explanation panel fills the whole panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「分離処分の原則と、例外までの手順」.",
                  "Three wide cards stacked top to bottom, all exactly the same size, each with the same pale gray fill and a dark navy outline, and each with its dark navy heading placed fully INSIDE the card; the cards are separated only by a small empty gap, with nothing drawn between them (no arrow, no connector).",
                  "Card 1, heading 「原則：分離処分できない」, body 「専有部分と敷地利用権は、一体（区分所有法22条1項）」.",
                  "Card 2, heading 「分離処分を可能にする」, body 「規約に別段の定めを設定する。一部の区分建物についてだけでもよい」.",
                  "Card 3, heading 「持分だけを移転する」, body 「前提として、敷地権の登記を抹消する表題部の変更の登記が要る」.",
                  "The three cards have clearly different texts; the texts are NOT identical. There is no check mark and no cross anywhere in this panel."]),
        dict(label="③　なぜ、先に抹消が要る？", chars="faces", mood="thoughtful then confident mood",
             bubbles=[("藍子", "共有持分を、売買で移すだけですよね？", None, "共有持分を、売買で\n移すだけですよね？"),
                      ("トリ先生", "それが罠。共有持分も敷地権になるのよ", "共有持分も敷地権", "それが罠。\n共有持分も敷地権に\nなるのよ"),
                      ("藍子", "では、なぜ持分だけ移せないんですか？", None, "では、なぜ持分だけ\n移せないんですか？"),
                      ("トリ先生", "建物の登記が、敷地権の登記も兼ねるのよ", "敷地権の登記も兼ねる", "建物の登記が、\n敷地権の登記も\n兼ねるのよ")],
             fig=["Two cards stacked from top to bottom, both the same size, each with the same pale gray fill and a dark navy outline, each with its dark navy heading placed fully INSIDE the card and two short body lines, with no arrow, no connector, no check mark, and no cross. The two cards are separated only by a small empty gap, with nothing drawn between them.",
                  "Card 1, heading 「共有持分も、敷地権になる」, two body lines: 「共有は、数人で有する所有権」, 「だから専有部分と一体になる」.",
                  "Card 2, heading 「敷地権の土地には、移転できない」, two body lines: 「建物の登記が、敷地権の登記も兼ねる（法73条1項）」, 「だから土地の持分だけの移転はできない（法73条2項）」.",
                  "Under the two cards, a dark navy ribbon tag with large white text 「ひっかけ：共有持分、売買という言葉」, the same size as the card body text.",
                  "The two cards have clearly different texts; the texts are NOT identical."]),
        dict(label="④　結論は先に抹消",
             bubbles=[("藍子", "規約、抹消、移転の順なんですね！", None, "規約、抹消、移転の\n順なんですね！"),
                      ("トリ先生", "そのとおり。丁だけでもできるのよ", "丁だけでも", "そのとおり。\n丁だけでも\nできるのよ")],
             fig=[],
             checklist=["共有持分も敷地権。専有部分と分離して処分できない（区分所有法22条1項）",
                        "規約に別段の定めで、分離処分できる。丁区分建物だけでもよい",
                        "持分だけ売るには、先に敷地権の登記を抹消する（法73条2項）"]),
    ],
    band1="持分だけ売るには、規約、敷地権の抹消、移転の順", band2="問題D1795・D1798・D1799　正解×・〇・×（R04-Q18ア・エ・オ）",
    ver="v02",
    qa=["v02：既存版（prompt_4koma_05_bunri-shobun.md、v01）を最新ルールで作り直し（2026-10-11）。構成（規約→抹消→移転、コマ1 side→コマ2 none→コマ3 faces→コマ4 既定）は保ち、コマ3の理由を2枚カードに作り替えた。ChatGPTでの画像生成・検品はまだ。"],
    rev=["2026-10-09 v01：初版（条文別『苦手克服』シリーズ（note-articles/joubun-nigate/）の規約敷地用。共有持分の敷地権と分離処分の手順を問う3肢を1本にまとめた）",
         "2026-10-11 v02：最新の作成ルールで作り直し（ユーザー指示）。①コマ3の『勘違い⇔正しい整理』の左右カードと理由の帯を、理由の2枚カード（共有は数人で有する所有権／建物の登記が敷地権の登記も兼ねるので土地だけの移転はできない）に作り替え、法73条1項→2項の理由につないだ ②同じ文が重なっていたので整理し、コマ2・コマ4の文を短くした ③設計メモに個人の記述は入れていない ④キャラは必要以上に小さくしない（コマ1はside）"],
)

HEADER = dict(h1="共有持分を売るなら", h2="先に何をする？", hkey="先に何をする？",
              scene_l="a small apartment building standing on a shared plot of land, with a faint dotted line dividing the plot in two, no text",
              scene_r="a registry book with a bookmark and an eraser, beside a small signpost board, no text")
