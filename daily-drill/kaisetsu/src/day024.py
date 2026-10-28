D = dict(
    catch='筆界特定の公告と手続費用',
    intro='筆界特定の手続について、公告の期間、意見書の提出方法、記録の保存期間、手続費用の負担、判決が確定したときの取扱いを問う問題です（不動産登記法133条・146条・148条、不動産登記規則217条・220条・235条・237条）。\n\nこの記事では、数字の入れ替えと「できる」「しなければならない」の違いに注意しながら、具体例で確認していきましょう。問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('筆界特定の申請の公告は、二週間行う',
               '筆界特定の申請があったときの公告は、法務局又は地方法務局の掲示場その他公衆の見やすい場所に掲示する方法か、インターネットを使用する方法により、二週間行います（不動産登記規則217条1項）。\n\n問題文は「一週間」としているので、本肢は誤りです。\n\n**たとえば**、筆界特定の申請を受けた法務局が、その旨を掲示場やホームページに載せる場合です。載せておく期間は、一週間ではなく、二週間です。'),
        'イ': ('意見や資料を書面で出すときは、写し三部を提出する',
               '申請人又は関係人が、筆界特定について意見又は資料を書面で提出するときは、その書面の写し三部を提出しなければなりません（不動産登記規則220条1項）。筆界特定登記官は、必要と認めるときは、原本の提示を求めることができます（同条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、関係人が「この線が境のはずだ」という意見書を出すときは、原本とは別に、その写しを三部用意します。'),
        'ウ': ('筆界特定書の情報は永久保存。三十年間なのは、それ以外の記録',
               '筆界特定手続記録の保存期間は、記録の種類で違います。筆界特定書に記載された情報は永久です。筆界特定書以外の記録は、登記所が筆界特定手続記録の送付を受けた年の翌年から三十年間です（不動産登記規則235条1項）。\n\n問題文は、筆界特定書に記載された情報を「三十年間」としているので、本肢は誤りです。\n\n**たとえば**、境の位置を特定した結果を書いた筆界特定書は、ずっと残ります。申請書や調査の資料などの記録は、送付を受けた年の翌年から三十年間保存されます。'),
        'エ': ('一方の土地の一人と他方の土地の二人が申請したときの費用負担',
               '筆界特定の申請人が三人以上で、一人又は二人以上が一方の土地の所有権登記名義人等、他の一人又は二人以上が他方の土地の所有権登記名義人等であるときは、次のようになります（不動産登記法146条4項）。\n\n- 一方の土地の一人の申請人：手続費用の二分の一を負担する。\n- 他方の土地の二人以上の申請人：残りの二分の一を、持分の割合に応じて負担する。\n\n本肢は、甲土地のAが二分の一、乙土地の共有者B・Cが各二分の一ずつ持分を持つので、BとCが各四分の一を負担し、正しいといえます。\n\n**たとえば**、費用が100万円なら、Aが50万円、BとCが各25万円です。'),
        'オ': ('判決確定の旨を筆界特定書に明らかにするのは、義務ではない',
               '登記官は、保管する筆界特定手続記録に係る筆界特定がされた筆界について、筆界確定訴訟の判決（訴えを不適法として却下したものを除く）が確定したときは、判決が確定した旨と事件を特定する事項を、筆界特定書に明らかにすることができます（不動産登記規則237条）。\n\n問題文は「明らかにしなければならない」としていますが、条文は「できる」と定めています。本肢は誤りです。\n\n**たとえば**、筆界特定の後に裁判で境が確定したときは、登記官がその旨を筆界特定書に記載することは認められますが、記載は義務ではありません。'),
    },
    summary=[
        ('ア', '誤', '申請があった旨の公告は、一週間ではなく、二週間行う'),
        ('イ', '正', '意見や資料を書面で提出するときは、写し三部を提出しなければならない'),
        ('ウ', '誤', '筆界特定書の情報は永久保存。三十年間は筆界特定書以外の記録'),
        ('エ', '正', '一方の土地の一人は二分の一、他方の土地の二人は残りの二分の一を持分の割合で負担する'),
        ('オ', '誤', '判決が確定した旨を筆界特定書に明らかにするのは、義務ではなく「できる」規定'),
    ],
    summary_tail='アは「数字のすり替え」、ウは「範囲のすり替え」、オは「できる」と「しなければならない」の入れ替えです。筆界特定は、期間・部数・年数・割合の数字を、場面とセットで覚えましょう。',
    supplements=[
        '### 補足説明（ウ）：筆界特定手続記録の保存期間\n\n筆界特定手続記録は、記録の種類で保存期間が分かれます（不動産登記規則235条1項）。\n\n- 筆界特定書に記載され、又は記録された情報：永久。\n- 筆界特定書以外の筆界特定手続記録の情報：登記所が送付を受けた年の翌年から三十年間。\n\n**たとえば**、境をどこと特定したかという結果を記した筆界特定書は、ずっと残ります。手続の途中でやりとりした書類などの記録は、送付を受けた年の翌年から三十年間です。',
        '### 補足説明（エ）：手続費用の負担の分け方\n\n筆界特定の手続費用は、申請人の人数と、それぞれがどちらの土地の側かで負担の割合が変わります（不動産登記法146条）。\n\n- 申請人が二人で、一人ずつ別の土地の側：等しい割合で負担（2項）。\n- 申請人の全員が、対象土地の一方の側：持分の割合に応じて負担（3項）。\n- 申請人が三人以上で、両方の土地の側にいる：一方の土地の一人の申請人は二分の一、他方の土地の二人以上は残りの二分の一を持分の割合で負担（4項）。\n\n**たとえば**、甲土地の所有者一人と、乙土地の共有者二人（持分は各二分の一）が申請すると、甲の一人が二分の一、乙の二人が各四分の一を負担します。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第24日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法133条、146条、148条、不動産登記規則217条、220条、235条、237条は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの費用の例（100万円を50万円と25万円ずつに分ける）は、146条4項の割合を計算しただけの説明です。実際の手続費用の額は確認していません。',
        'ア・イ・ウ・オの具体例は、条文の文言から導いた一般的な説明です。オの記載が義務でない点は、規則237条が「できる」と定めていることによる整理で、運用上の取扱いは確認していません。',
    ],
    phrases=['公告の期間は二週間です', '意見書の写しは三部出します', '筆界特定書は永久に保存されます', '費用は申請人の側ごとに分けます', '判決確定の旨の記載はできる規定です'],
    header=dict(t1='公告は何週間？', t2='誰が費用を払う？', topic='不動産登記法　筆界特定の手続',
                kanji='公・告・週・間・筆・界・特・定・手・続・費・用'),
    poster_intro='筆界特定の手続を、「公告と意見書」（グループA：ア・イ）と「保存・費用・判決」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='筆界特定の手続を整理', sub='不動産登記法第146条ほか（毎日ドリル 第24日）',
        col_a='公告と意見書', col_b='保存・費用・判決', n_a=2,
        cards=[
            dict(h='公告の期間は二週間',
                 ill='a bulletin board with a notice sheet labeled 「公告」 pinned on it, and a calendar page labeled 「二週間」 beside the board. A green check mark sits beside the calendar.',
                 words=['公告', '二週間'], tag='期間は二週間'),
            dict(h='意見書の写しは三部提出する',
                 ill='a sheet labeled 「意見書」 with a stack of three copies behind it, and a small tag labeled 「三部」 on the stack. A green check mark sits beside the stack.',
                 words=['意見書', '三部'], tag='写し三部'),
            dict(h='筆界特定書は永久に保存される',
                 ill='a bound book labeled 「筆界特定書」 on a shelf with an infinity symbol beside it labeled 「永久」. A thinner folder beside it is labeled 「その他の記録」 with a small calendar page labeled 「三十年」. A green check mark sits beside the book.',
                 words=['筆界特定書', '永久', 'その他の記録', '三十年'], tag='他の記録は三十年'),
            dict(h='手続費用は申請人の側ごとに分ける',
                 ill='a horizontal bar split into three blocks. The left half block is labeled 「二分の一」, and the right half is split into two quarter blocks, each labeled 「四分の一」. A green check mark sits above the bar.',
                 words=['二分の一', '四分の一'], tag='一人の側が二分の一'),
            dict(h='判決確定の旨は明らかにできる',
                 ill='a courthouse building on the left and a bound book labeled 「筆界特定書」 on the right. A note tag labeled 「判決確定」 is clipped to the book. A green check mark sits beside the note tag.',
                 words=['筆界特定書', '判決確定'], tag='義務ではなくできる規定'),
        ],
        kanji='公・告・週・間・意・見・書・写・部・筆・界・特・定・永・久・手・続・費・用・申・請・人・判・決・確・定・義・務'.split('・')),
    nb_label='ウ・エ肢', nb_intro='ウ・エの補足説明に合わせた2枚です。1枚目は、筆界特定手続記録の保存期間を表で整理します。2枚目は、手続費用の負担の割合を図で示します。',
    notebooks=[
        dict(name='筆界特定手続記録の保存期間', args=dict(
            title='筆界特定の記録、何年保存？', sub='筆界特定書と、それ以外の記録（毎日ドリル 第24日 ウ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean table with 2 columns and 2 data rows, plus a header row. The column headers are exactly: 記録の種類 / 保存期間. Each row has a small isometric icon beside the first cell.
Row 1: first cell 筆界特定書に記載された情報 (icon: a bound book); second cell 永久.
Row 2: first cell 筆界特定書以外の記録 (icon: a stack of loose papers); second cell 送付を受けた年の翌年から三十年間.
Use exactly these strings, and no others, for the cell text. The two 保存期間 cells are different strings; draw 永久 in blue and 送付を受けた年の翌年から三十年間 in orange.""",
            callout='筆界特定書に記載された情報は、永久に保存されます。\n三十年間なのは、筆界特定書以外の記録で、登記所が送付を受けた年の翌年から数えます。',
            footer='不動産登記規則235条1項',
            kanji='筆・界・特・定・記・録・種・類・保・存・期・間・永・久・送・付・受・翌・年・書・載・情・報'.split('・'), what='table',
            check='confirm the table has exactly 2 columns and 2 data rows, and confirm the two cells in the 保存期間 column are different strings drawn in different accent colors, ')),
        dict(name='手続費用の負担の割合', args=dict(
            title='手続費用、だれがどれだけ？', sub='申請人が三人以上で両方の土地の側にいる場合（毎日ドリル 第24日 エ）',
            req='a diagram',
            layout="""--- DIAGRAM ---
Render as a clean flat-design diagram. In the upper part, one wide horizontal bar split into three blocks: the left half block, and the right half divided into two equal quarter blocks.
Under the left half block, a person figure with a label: 甲土地の申請人 (one person). Above the block, the label 二分の一.
Under the two quarter blocks, two person figures with the labels: 乙土地の共有者の一人 and 乙土地の共有者のもう一人. Above each quarter block, the label 四分の一.
A thin bracket joins the two right-hand quarter blocks and is labeled 持分の割合に応じて.
Use exactly these strings, and no others, for the labels.""",
            callout='申請人が三人以上で、両方の土地の側にいるときは、一方の土地の一人の申請人が費用の二分の一を負担します。\n他方の土地の二人以上の申請人は、残りの二分の一を、持分の割合に応じて負担します。',
            footer='不動産登記法146条4項',
            kanji='甲・乙・土・地・申・請・人・共・有・者・持・分・割・合・応・二・四・一'.split('・'), what='diagram',
            check='confirm the left block is labeled 二分の一 and each of the two right blocks is labeled 四分の一, ')),
    ],
)
