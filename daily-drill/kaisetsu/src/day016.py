D = dict(
    catch='登記識別情報と事前通知の数字',
    intro='登記識別情報の通知と、登記識別情報を提供できないときの事前通知について、「だれに」「いつまでに」を問う問題です（不動産登記法21条・23条、不動産登記規則62条・64条・70条・71条）。\n\nこの記事では、通知の相手方、書面を受け取る期限、事前通知の申出期間、前の住所地への通知の例外を、具体的な場面で確認していきましょう。問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('法定代理人が申請したときは、登記識別情報は法定代理人に通知される',
               '登記官は、登記をすることによって申請人自らが登記名義人となる場合に、登記が完了したときは、その申請人に登記識別情報を通知します（不動産登記法21条）。ただし、法定代理人によって申請しているときは、通知は法定代理人に対してします（不動産登記規則62条1項1号）。\n\n本肢は正しいといえます。\n\n**たとえば**、未成年者の土地2筆について、親権者が未成年者の代理人として合筆の登記を申請したとします。合筆の登記が終わると、登記識別情報は、未成年者本人ではなく、申請した親権者に通知されます。'),
        'イ': ('共有の合筆では、共有者の一人ひとりに通知される',
               '登記識別情報は、登記によって自らが登記名義人となる申請人に通知されます（不動産登記法21条）。共有の土地を合筆したときは、AもBも登記名義人となる申請人なので、それぞれに通知されます。\n\n問題文は「AまたはBのいずれか一方に通知すれば足りる」としているので、本肢は誤りです。\n\n**たとえば**、AさんとBさんが共有する甲土地と乙土地を、二人で合筆の登記を申請したとします。完了後、登記識別情報はAさんの分とBさんの分が、別々に通知されます。'),
        'ウ': ('書面で受け取る期限は、登記完了の時から三月以内',
               '書面の交付を受ける方法で登記識別情報の通知を受けるべき者が、登記完了の時から三月以内にその書面を受領しない場合は、登記官は登記識別情報を通知することを要しません（不動産登記規則64条1項3号）。\n\n問題文は「一月以内」としていますが、正しくは「三月以内」です。本肢は誤りです。\n\n**たとえば**、法務局の窓口で登記識別情報の書面を受け取る予定の人が、登記が完了してもしばらく取りに行かず、三月がたってしまったとします。この場合、登記官は通知する必要がなくなります。'),
        'エ': ('事前通知の申出期間は、外国に住所があれば四週間',
               '登記義務者が登記識別情報を提供できないとき、登記官は、登記義務者に対して、申請があった旨と、内容が真実であれば申出をすべき旨を通知します。これが事前通知です（不動産登記法23条1項）。\n\n申出をすべき期間は、通知を発送した日から二週間です。ただし、登記義務者が外国に住所を有する場合は、四週間とされています（不動産登記規則70条8項）。本肢は正しいといえます。\n\n**たとえば**、売主が海外で暮らしている場合は、手紙が届いて返事をするまでに日数がかかるので、期間が二週間から四週間に延びています。'),
        'オ': ('住所変更から三月を過ぎていれば、前の住所地への通知はしない',
               '所有権に関する登記の申請で、登記義務者の住所について変更の登記がされているときは、登記官は、事前通知のほか、登記記録上の前の住所にあてても通知をします。ただし、法務省令で定める場合は、通知をしません（不動産登記法23条2項）。\n\nその除外の一つが、申請の日が、最後の住所の変更の登記の受付の日から三月を経過している場合です（不動産登記規則71条2項2号）。本肢は6か月前の変更なので、前の住所地への通知は不要です。本肢は誤りです。\n\n**たとえば**、半年前に引っ越して住所の変更の登記をした売主の場合、前の住所地には通知は届きません。'),
    },
    summary=[
        ('ア', '正', '法定代理人によって申請した場合、登記識別情報は法定代理人に通知される'),
        ('イ', '誤', '共有の合筆では、A又はBの一方ではなく、AにもBにもそれぞれ通知される'),
        ('ウ', '誤', '書面で通知を受けるべき者が受領しなくてよくなるのは、登記完了の時から三月以内（一月ではない）'),
        ('エ', '正', '事前通知の申出期間は、発送した日から二週間。外国に住所があるときは四週間'),
        ('オ', '誤', '最後の住所の変更の登記の受付日から三月を経過していれば、前の住所地への通知は不要'),
    ],
    summary_tail='イは「通知を受ける人の範囲」、ウは「数字（一月と三月）」、オは「通知の例外」のすり替えです。登記識別情報と事前通知は、期間の数字を、場面とセットで覚えておきましょう。',
    supplements=[
        '### 補足説明（ウ）：登記識別情報の通知を受ける期限\n\n登記識別情報は、通知を受ける人が期限内に受け取らないと、登記官は通知する必要がなくなります（不動産登記規則64条1項2号・3号）。期限は、通知の方法によって違います。\n\n- 電子情報処理組織を使う方法：送信が可能になった時から三十日以内。\n- 書面の交付を受ける方法：登記完了の時から三月以内。\n\n**たとえば**、書面を受け取る方法を選んだ人が、三月たっても窓口に取りに来ない場合、登記官は、その登記識別情報を記載した書面を廃棄することができます（同条3項）。',
        '### 補足説明（エ・オ）：事前通知まわりの数字\n\n事前通知とそれに続く手続には、似た数字がいくつか出てきます。\n\n- 事前通知の申出期間：通知を発送した日から二週間。登記義務者が外国に住所を有するときは四週間（不動産登記規則70条8項）。\n- 前の住所地への通知：申請の日が、最後の住所の変更の登記の受付の日から三月を経過していれば、しない（同規則71条2項2号）。\n\n**たとえば**、引っ越して間もない1か月前に住所の変更の登記をした売主が、登記識別情報なしで売却の登記を申請する場合は、ほかの除外にあたらない限り、前の住所地にも通知が届きます。半年前の変更なら、届きません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第16日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法21条、23条、不動産登記規則62条、64条、70条、71条は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの合筆で登記識別情報が通知される点（登記によって申請人自らが登記名義人となる場合の扱い）は、問題データの正誤に従って書いたもので、条文からの一般的な整理です。通達・先例の確認はしていません。',
        'ウ・エ・オの具体例（窓口で受け取らない人、海外在住の売主、半年前に引っ越した売主）は、条文の文言から導いた一般的な説明です。オの前の住所地への通知には、71条2項の別の除外事由（法人であるときなど）もあります。',
    ],
    phrases=['法定代理人が申請なら代理人に通知です', '共有なら一人ひとりに通知されます', '書面の受領期限は三月以内です', '外国に住所があれば四週間です', '三月を過ぎたら前の住所へは通知しません'],
    header=dict(t1='三月、二週間、', t2='四週間の使い分け', topic='不動産登記法　登記識別情報と事前通知',
                kanji='三・週・間・登・記・識・別・事・前・通・知'),
    poster_intro='登記識別情報と事前通知を、「登記識別情報の通知」（グループA：ア・イ・ウ）と「事前通知」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='登記識別情報と事前通知を整理', sub='不動産登記法 第21条・第23条（毎日ドリル 第16日）',
        col_a='登記識別情報の通知', col_b='事前通知', n_a=3,
        cards=[
            dict(h='法定代理人が申請したら代理人に通知',
                 ill='a small child figure standing in the back, and a parent figure in front holding an envelope labeled 「登記識別情報」. A green check mark sits beside the parent figure.',
                 words=['登記識別情報'], tag='通知先は法定代理人'),
            dict(h='共有の合筆は一人ずつに通知',
                 ill='two person figures side by side, each holding their own envelope labeled 「登記識別情報」. A merged land plot sits behind them. A green check mark sits above the two figures.',
                 words=['登記識別情報'], tag='ひとり一通ずつ'),
            dict(h='書面の受領は三月以内',
                 ill='a counter window with an envelope labeled 「登記識別情報」 on the counter, and a calendar page labeled 「三月以内」 beside it. A green check mark sits beside the calendar.',
                 words=['登記識別情報', '三月以内'], tag='書面の期限は三月'),
            dict(h='外国に住所があれば四週間',
                 ill='a person figure beside a globe, holding a notice sheet, with a calendar page labeled 「四週間」 beside the globe. A green check mark sits beside the calendar.',
                 words=['四週間'], tag='外国なら四週間'),
            dict(h='三月たてば前の住所へは通知しない',
                 ill='an old house in faded gray on the left with no envelope, and a new house on the right. A calendar page labeled 「三月」 sits between them. A green check mark sits beside the calendar.',
                 words=['三月'], tag='前の住所へは不要'),
        ],
        kanji='登・記・識・別・情・報・事・前・通・知・法・定・代・理・人・共・有・合・筆・書・面・受・領・月・外・国・住・所・四・週・間'.split('・')),
    nb_label='ウ・エ・オ肢', nb_intro='ウ・エ・オの補足説明に合わせた2枚です。1枚目は、登記識別情報の通知を受ける期限を、方法ごとに表で整理します。2枚目は、事前通知まわりの数字を表で整理します。',
    notebooks=[
        dict(name='登記識別情報の通知を受ける期限', args=dict(
            title='登記識別情報、いつまでに受け取る？', sub='通知の方法ごとの期限（毎日ドリル 第16日 ウ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean table with 3 columns and 2 data rows, plus a header row. The column headers are exactly: 通知の方法 / 数え始め / 期限. Each row has a small isometric icon beside the first cell.
Row 1: first cell 電子情報処理組織 (icon: a laptop with an envelope); second cell 送信が可能になった時; third cell 三十日以内.
Row 2: first cell 書面の交付 (icon: a paper envelope on a counter); second cell 登記完了の時; third cell 三月以内.
Use exactly these strings, and no others, for the cell text. The two 期限 cells are different strings; draw 三十日以内 in blue and 三月以内 in green.""",
            callout='期限内に受け取らないと、登記官は登記識別情報を通知することを要しなくなります。\n書面の場合の期限は、一月ではなく、登記完了の時から三月以内です。',
            footer='不動産登記規則64条1項',
            kanji='通・知・方・法・数・始・期・限・電・子・情・報・処・理・組・織・送・信・可・能・書・面・交・付・記・完・了・日・月'.split('・'), what='table',
            check='confirm the table has exactly 3 columns and 2 data rows, and confirm the two cells in the 期限 column are different strings drawn in different accent colors, ')),
        dict(name='事前通知まわりの数字', args=dict(
            title='事前通知の数字を整理しよう', sub='申出期間と前の住所地への通知（毎日ドリル 第16日 エ・オ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean table with 3 columns and 3 data rows, plus a header row. The column headers are exactly: 場面 / 数え始め / 結論. Each row has a small isometric icon beside the first cell.
Row 1: first cell 事前通知の申出期間 (icon: a letter with a calendar); second cell 通知を発送した日; third cell 二週間.
Row 2: first cell 外国に住所がある場合 (icon: a globe with a letter); second cell 通知を発送した日; third cell 四週間.
Row 3: first cell 前の住所地への通知 (icon: an old house with a letter); second cell 最後の変更の登記の受付の日; third cell 三月を経過すれば通知しない.
Use exactly these strings, and no others, for the cell text. The three 結論 cells are different strings; draw 二週間 in blue, 四週間 in green and 三月を経過すれば通知しない in orange.""",
            callout='事前通知の申出期間は、発送した日から二週間です。外国に住所があるときは四週間です。\n最後の住所の変更の登記の受付の日から三月を経過していれば、前の住所地には通知しません。',
            footer='不動産登記規則70条8項、71条2項',
            kanji='事・前・通・知・申・出・期・間・外・国・住・所・変・更・登・記・受・付・最・後・発・送・週・月・結・論'.split('・'), what='table',
            check='confirm the table has exactly 3 columns and 3 data rows, and confirm the three cells in the 結論 column are different strings drawn in different accent colors, ')),
    ],
)
