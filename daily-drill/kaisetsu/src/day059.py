D = dict(
    catch='地図の訂正は、相続人も申し出られる',
    intro='地図又は地図に準ずる図面の訂正の申出を問う問題です（不動産登記規則16条）。地図は、一つ一つの土地の区画を示す法務局の図面です。地図に準ずる図面は、地図が備え付けられるまでの間、これに代わって備え付けられる図面です。\n\nこの記事では、だれが申し出られるか、何を一度に申し出られるか、地積の更正との関係、地番の誤りのときの添付情報を、具体的な場面で確かめていきましょう。',
    sections={
        'ア': ('相続人も、相続の登記をしなくても申し出られる',
               '地図に表示された土地の区画に誤りがあるときは、表題部所有者や所有権の登記名義人のほか、その相続人その他の一般承継人も、訂正の申出をすることができます。相続人が申し出るときは、相続があったことを証する情報を提供します（不動産登記規則16条1項・5項3号）。\n\n本肢は正しいといえます。条文は、相続による所有権の移転の登記を先にすることを、申出の条件にしていません。\n\n**たとえば**、父の名義の土地を子が単独で相続したが、相続の登記はまだ、という場面でも、子は、相続を証する戸籍などの情報を添えて、区画の誤りの訂正を申し出ることができます。'),
        'イ': ('複数の土地は、まとめて一の申出情報で申し出られない',
               '地図の訂正の申出は、登記の申請とは違い、複数の土地をまとめて一の申出情報で行うことはできません。土地ごとに申し出ます（登記実務の取扱い）。\n\n問題文は、甲土地と乙土地の区画を一の申出情報で申し出られるとしているので、本肢は誤りです。\n\n**たとえば**、隣り合う甲土地と乙土地の両方の区画が地図で間違っているときは、同じ人が申し出る場合でも、甲土地の申出と乙土地の申出に分けて行います。'),
        'ウ': ('地積にも錯誤があるときは、更正の登記と併せて申し出る',
               '地図に準ずる図面に表示された土地の位置、形状に誤りがあるときも、訂正の申出ができます（不動産登記規則16条1項後段）。その土地の登記記録の地積に錯誤があるときは、申出は、地積に関する更正の登記の申請と併せてしなければなりません（同条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、図面に描かれた土地の形が実際と違い、しかも登記記録の面積も実際より小さかったとします。この場合、形の訂正の申出だけをするのではなく、面積の更正の登記の申請と一緒にします。'),
        'エ': ('分筆線の誤りは、地図の訂正ではなく、分筆の更正で直す',
               '分筆の登記が、誤った分筆線のまま、地図にも記録されたときは、分筆の錯誤による更正の登記で是正します。地図の訂正の申出で、分筆線を正しい位置に直すことはできません（登記実務の取扱い）。\n\n問題文は「地図の訂正の申出によって訂正することができる」としているので、本肢は誤りです。\n\n**たとえば**、提出した図面の分筆線が実際とずれていたために、地図に間違った線が載ったときは、図面の誤りの大もとである分筆の登記そのものを、更正の登記で直します。'),
        'オ': ('地番だけの誤りなら、土地所在図や地積測量図は要らない',
               '土地所在図又は地積測量図を提供するのは、地図又は地図に準ずる図面に表示された土地の区画又は位置若しくは形状に誤りがあるときです（不動産登記規則16条5項2号）。地番だけに誤りがあるときは、誤りがあることを証する情報を提供すれば足ります（同項1号）。\n\n問題文は、地番の誤りの場合にも土地所在図又は地積測量図を提供しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、図面の土地の形は合っていて、地番の数字だけが違っている場合、形を示す図面を新たにつくる必要はありません。'),
    },
    summary=[
        ('ア', '正', '相続人も、相続の登記をしなくても、相続を証する情報を付けて申し出られる'),
        ('イ', '誤', '複数の土地の訂正を、まとめて一の申出情報で申し出ることはできない'),
        ('ウ', '正', '登記記録の地積に錯誤があるときは、地積の更正の登記の申請と併せて申し出る'),
        ('エ', '誤', '分筆線の誤りは、地図の訂正ではなく、分筆の錯誤による更正の登記で直す'),
        ('オ', '誤', '土地所在図又は地積測量図が要るのは、区画、位置、形状の誤りのときで、地番だけなら要らない'),
    ],
    summary_tail='オは「何の誤りか」で、添付する情報が変わる出題でした。誤りの内容を、区画・位置・形状と、地番に分けて覚えましょう。',
    supplements=[
        '### 補足説明（ウ）：地積にも誤りがあるときの進め方\n\n地図の訂正の申出をする土地について、登記記録の地積にも錯誤があるときは、二つを別々にせず、併せて行います（不動産登記規則16条2項）。\n\n- 地図又は地図に準ずる図面の誤り：訂正の申出。\n- 登記記録の地積の誤り：地積に関する更正の登記の申請。\n- 地積にも錯誤があるとき：二つを併せてします。\n\n**たとえば**、図面の土地の形と、登記記録の面積の両方が実際と合わないときは、形の訂正の申出と、面積の更正の登記の申請を、同時に行います。',
        '### 補足説明（オ）：誤りの内容と、添付する情報\n\n訂正の申出には、地図訂正申出情報と併せて、次の情報を提供します（不動産登記規則16条5項）。\n\n| 誤りの内容 | 提供する情報 |\n|---|---|\n| 区画、位置又は形状の誤り | 誤りがあることを証する情報、土地所在図又は地積測量図 |\n| 地番の誤り | 誤りがあることを証する情報 |\n\n**たとえば**、隣の土地との境目の位置が違っているなら、正しい位置を示す土地所在図又は地積測量図が必要です。一方、地番の数字が違っているだけなら、誤りがあることを証する情報だけで足ります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第59日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則16条1項・2項・5項は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの「複数の土地をまとめて一の申出情報ですることはできない」と、エの「分筆線の誤りは分筆の錯誤による更正の登記で直し、地図の訂正の申出では直せない」は、登記実務の取扱いで、手元の法令集には条文の収録がなく、原文は未確認です。',
        'ア、ウ、エの具体例（相続の場面、形と面積の誤り、分筆線のずれ）は、条文の文言をかみ砕いた一般的な説明です。',
    ],
    phrases=['相続の登記がなくても、相続人は申し出られます', '地図の訂正は、土地ごとに申し出ます', '地積の錯誤は、更正の登記と一緒に', '分筆線の誤りは、更正の登記で直します', '地番だけの誤りなら、図面は要りません'],
    header=dict(t1='地図の間違いは、', t2='だれが直せる？', topic='不動産登記規則　地図の訂正',
                kanji='登・記・毎・地・図・訂・正'),
    poster_intro='地図等の訂正の申出を、「申出の仕方」（グループA：ア・イ・ウ）と「訂正できる範囲と添付情報」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='地図等の訂正の申出を整理', sub='不動産登記規則 第16条（毎日ドリル 第59日）',
        col_a='申出の仕方', col_b='範囲と添付情報', n_a=3,
        cards=[
            dict(h='相続人も相続の登記なしで申出',
                 ill='a heir figure at a counter holding a map sheet and a family register paper labeled 「相続証明」. A faded gray house icon with a small registration stamp stands aside in the background. A green check mark sits beside the heir.',
                 words=['相続証明'], tag='相続登記は不要'),
            dict(h='複数の土地は土地ごとに申出',
                 ill='two neighboring land plots, each with its own separate form labeled 「申出」 attached to it by a thin line. A green check mark sits beside each form.',
                 words=['申出'], tag='土地ごと'),
            dict(h='地積に錯誤があれば更正と併せて',
                 ill='a land plot drawing on the left and a record sheet labeled 「地積」 on the right, joined by a green bracket. A pencil icon corrects the record sheet. A green check mark sits beside the bracket.',
                 words=['地積'], tag='更正の登記と併せて'),
            dict(h='分筆線の誤りは更正の登記で直す',
                 ill='a land plot split by a dividing line, with a pencil correcting the dividing line, and a round stamp labeled 「更正」 beside it. A green check mark sits beside the stamp.',
                 words=['更正'], tag='分筆の更正'),
            dict(h='地番だけの誤りなら図面は要らない',
                 ill='a map sheet where only the lot number tag on one plot is highlighted with a pencil mark, while a plain survey drawing sheet is drawn faded in gray at the side. A green check mark sits beside the highlighted tag.',
                 words=[], tag='証する情報だけ'),
        ],
        kanji='相・続・証・明・申・出・地・積・更・正・分・筆・図・面'.split('・')),
    nb_label='ウ・オ肢', nb_intro='ウ・オの補足説明に合わせた2枚です。1枚目は、地積にも錯誤があるときの進め方を流れで示します。2枚目は、誤りの内容によって添付する情報が変わることを、左右の対比で示します。',
    notebooks=[
        dict(name='地積にも錯誤があるときの進め方', args=dict(
            title='地積にも誤りがあるときは？', sub='地図の訂正の申出と地積の更正（毎日ドリル 第59日 ウ）',
            req='a flow diagram',
            layout="""--- FLOW ---
Render as a clean flat-design vertical flow diagram. Top box (gray): 地図に準ずる図面の形状に誤りがある. Below it, a small diamond labeled 登記記録の地積にも錯誤がある？.
LEFT BRANCH (blue accent), arrow label: ない. Box: 訂正の申出だけ. Result badge with a green check mark: 申出ができる
RIGHT BRANCH (green accent), arrow label: ある. Box: 訂正の申出 と 地積の更正の登記の申請. Result badge with a green check mark: 併せてする
Use exactly these strings, and no others.""",
            callout='地積にも錯誤があるときは、地図等の訂正の申出を、地積に関する更正の登記の申請と併せてしなければなりません。\n地積に錯誤がなければ、訂正の申出だけで足ります。',
            footer='不動産登記規則十六条二項',
            kanji='地・図・準・形・状・誤・登・記・積・錯・訂・正・申・出・更・請・併'.split('・'), what='flow',
            check='confirm the diamond has exactly two branches, 左 labeled ない and 右 labeled ある, each ending with a green check mark, ')),
        dict(name='誤りの内容と、添付する情報', args=dict(
            title='何の誤りで、何を付ける？', sub='地図等の訂正の申出の添付情報（毎日ドリル 第59日 オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「区画・位置・形状の誤り」 on the left and 「地番の誤り」 on the right. Draw them in different accent colors (blue and orange). The right panel must NOT show the drawing sheet.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 区画・位置・形状の誤り
Scene: an isometric scene of two neighboring land plots with a boundary line drawn in the wrong position, and a survey drawing sheet beside them.
Items with green check marks, stacked: 誤りがあることを証する情報 | 土地所在図又は地積測量図

RIGHT PANEL (orange accent):
Panel header: 地番の誤り
Scene: an isometric scene of one land plot with a small lot-number sign.
Items with a green check mark: 誤りがあることを証する情報""",
            callout='区画、位置又は形状の誤りのときは、土地所在図又は地積測量図も提供します。\n地番だけの誤りなら、誤りがあることを証する情報だけで足ります。',
            footer='不動産登記規則十六条五項',
            kanji='区・画・位・置・形・状・誤・地・番・証・情・報・土・所・在・図・積・測・量'.split('・'), what='panels',
            check='confirm the left panel lists two items and the right panel lists exactly one item and shows no drawing sheet, ')),
    ],
)
