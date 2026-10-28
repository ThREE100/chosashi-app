D = dict(
    catch='面識がなければ、有効な身分証で確認',
    intro='登記識別情報を提供できないときの、事前通知と、資格者代理人（土地家屋調査士など）による本人確認情報を問う問題です（不動産登記法23条、不動産登記規則70条・72条）。\n\nこの記事では、本人確認情報を作るときの「面識があるといえる場合」「確認に使える書類」「面談の相手」と、事前通知の申出の期間を、具体的な場面で確かめていきましょう。',
    sections={
        'ア': ('面識がなければ、免許証は提示を受ける日に有効なものを',
               '資格者代理人が申請人の氏名を知らず、又は面識がないときは、運転免許証などの書類の提示を受けて確認します。この書類のうち運転免許証などは、提示を受ける日において有効なものに限られます（不動産登記規則72条1項3号・2項ただし書）。\n\n本肢は正しいといえます。\n\n**たとえば**、初めて会った依頼者が、有効期限の切れた運転免許証を見せたとします。期限が切れた免許証は、確認のための書類として使えません。有効期限内の書類を見せてもらう必要があります。'),
        'イ': ('「面識あり」となるのは、前の申請が3月以上前のとき',
               '前に本人確認情報を提供して申請したことを理由に「面識がある」といえるのは、その登記の申請の3月以上前に提供して申請していた場合です（不動産登記事務取扱手続準則49条1項1号）。\n\n問題文は2か月前としているので、本肢は誤りです。2か月前では、まだ面識があるものとして扱えません。\n\n**たとえば**、2か月前に依頼者Aさんの本人確認情報を作って申請した調査士が、今回もAさんの申請を受けたとします。この場合でも、今回は面識ありとはできず、運転免許証などの書類の提示を受けて確認することになります。'),
        'ウ': ('法人の場合の面談の相手は、代表者又はこれに代わるべき者',
               '申請人が法人であるときの面談の相手は、「代表者又はこれに代わるべき者」です（不動産登記規則72条1項1号）。\n\n問題文は「代表者本人と面談しなければならず、代わるべき者では足りない」としているので、本肢は誤りです。\n\n**たとえば**、申請人が株式会社のとき、代表者本人でなくても、条文のいう「これに代わるべき者」と面談すれば、面談の要件を満たします。代表者本人に限られるわけではありません。'),
        'エ': ('外国に住所があるときの申出の期間は、発送の日から四週間',
               '事前通知を受けた登記義務者が、申請の内容が真実であると申し出る期間は、通知を発送した日から二週間です。ただし、登記義務者が外国に住所を有するときは、四週間になります（不動産登記規則70条8項）。\n\n本肢は正しいといえます。\n\n**たとえば**、外国に住んでいる所有権の登記名義人に事前通知を発送した場合、数えはじめは発送した日で、申出ができる期間は四週間です。国内に住む人の二週間より長くなります。'),
        'オ': ('本人確認情報を相当と認められないときは、事前通知の手続',
               '登記官は、本人確認情報の内容を相当と認めることができない場合には、事前通知の手続を採ります（不動産登記事務取扱手続準則49条4項）。\n\n問題文は「申請を却下しなければならない」としているので、本肢は誤りです。\n\n**たとえば**、提出された本人確認情報だけでは本人かどうか確かめきれないとき、登記官はすぐに申請を断るのではなく、本人あてに通知を出して確かめる方法に切り替えます。'),
    },
    summary=[
        ('ア', '正', '面識がないとき、運転免許証などは、提示を受ける日に有効なものに限る'),
        ('イ', '誤', '「面識がある」といえるのは、前の申請が3月以上前の場合である'),
        ('ウ', '誤', '法人の面談の相手は、代表者又はこれに代わるべき者でよい'),
        ('エ', '正', '外国に住所を有する登記義務者の申出の期間は、発送の日から四週間である'),
        ('オ', '誤', '本人確認情報を相当と認められないときは、却下ではなく事前通知の手続を採る'),
    ],
    summary_tail='イは「3月以上前」を2か月前にすり替え、ウは面談の相手を代表者本人に絞り、オは事前通知を却下に入れ替えた出題です。数字と、だれが誰と会うのかを、一つずつ確かめましょう。',
    supplements=[
        '### 補足説明（イ）：「面識がある」といえる二つの場合\n\n資格者代理人が申請人の氏名を知り、かつ、面識があるといえる場合は、準則49条1項に二つ挙げられています。\n\n- 前の申請から数える場合：当該登記の申請の3月以上前に、その申請人について本人確認情報を提供して申請したことがあるとき。\n- 日ごろの関係から数える場合：依頼を受ける以前から氏名と住所を知っていて、親族関係、1年以上にわたる取引関係その他の安定した継続的な関係があるとき。\n\n**たとえば**、4か月前にも同じ依頼者の本人確認情報を作って申請していれば、前者に当たります。2か月前では、前者には当たりません。この場合は、書類の提示で確認する方法をとります。',
        '### 補足説明（オ）：本人確認情報が認められなかったときの流れ\n\n登記識別情報を提供できないときは、登記官は原則として事前通知をします（不動産登記法23条1項）。ただし、資格者代理人が、申請人が登記義務者であることを確認するために必要な情報を提供し、登記官がそれを相当と認めたときは、事前通知をしません（同条4項1号）。\n\n- 本人確認情報を相当と認めたとき：事前通知をせず、登記が進みます。\n- 相当と認められないとき：却下ではなく、事前通知の手続に戻ります（準則49条4項）。\n\n**たとえば**、面談の状況の説明が足りず、登記官が本人確認に不安を持った場合は、申請が断られるのではなく、本人あての通知で確かめる手続に移ります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第55日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法23条、不動産登記規則70条8項・72条、不動産登記事務取扱手続準則49条は、`note-articles/laws/` 配下の原文で確認しました。',
        '具体例（有効期限の切れた免許証、外国に住む登記名義人、面談が不十分な場合の流れ）は、条文の文言をかみ砕いた一般的な説明で、個別の先例・通達の確認はしていません。',
        'エは、問題文の設例が建物の合併の登記ですが、期間の定めは規則70条8項の文言（原則二週間、登記義務者が外国に住所を有するときは四週間）に基づいて説明しています。',
    ],
    phrases=['面識がなければ、有効な書類で確認します', '面識ありは、三月以上前の申請から', '法人の面談は、代わるべき者でもよいんです', '外国に住所があれば、四週間です', '認められなければ、却下ではなく事前通知です'],
    header=dict(t1='本人かどうか、', t2='どう確かめる？', topic='不動産登記法　本人確認情報',
                kanji='登・記・毎・本・人・確・認'),
    poster_intro='本人確認情報（グループA：ア・イ・ウ）と、事前通知（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='本人確認情報と事前通知を整理', sub='不動産登記規則 第70条・第72条（毎日ドリル 第55日）',
        col_a='本人確認情報', col_b='事前通知', n_a=3,
        cards=[
            dict(h='免許証は提示の日に有効なもの',
                 ill='a surveyor figure at a desk looking at a driver license card held by a client figure. A small calendar beside the card shows a green check mark. A green check mark sits beside the card.',
                 words=[], tag='提示の日に有効'),
            dict(h='面識ありは三月以上前の申請から',
                 ill='a horizontal timeline. On the left a flag labeled 「前の申請」; further right a flag labeled 「今回」. A green bracket labeled 「三月以上」 spans the distance between the two flags. A green check mark sits above the bracket.',
                 words=['前の申請', '今回', '三月以上'], tag='三月以上前'),
            dict(h='法人の面談は代わるべき者でもよい',
                 ill='a company building on the left and two figures standing in front of it: one with a name tag labeled 「代表者」 and one with a name tag labeled 「代わるべき者」. A green check mark sits above each figure.',
                 words=['代表者', '代わるべき者'], tag='どちらでもよい'),
            dict(h='外国に住所があれば四週間',
                 ill='a globe on the left and a letter with a postmark on the right, with a thin arrow between them. A calendar page labeled 「四週間」 sits above the arrow. A green check mark sits beside the calendar.',
                 words=['四週間'], tag='発送の日から'),
            dict(h='認められなければ事前通知へ',
                 ill='a registrar figure at a counter holding a sheet, with a thin arrow leading to a letter in an envelope labeled 「事前通知」. A green check mark sits beside the envelope.',
                 words=['事前通知'], tag='却下ではない'),
        ],
        kanji='免・許・証・提・示・面・識・前・申・請・今・回・月・以・上・法・人・代・表・者・外・国・週・間・通・知'.split('・')),
    nb_label='イ・オ肢', nb_intro='イ・オの補足説明に合わせた2枚です。1枚目は、面識があるといえるかどうかを、時間の流れで示します。2枚目は、本人確認情報が認められなかったときの流れを示します。',
    notebooks=[
        dict(name='「面識がある」といえるのはいつ？', args=dict(
            title='面識があるといえるのは？', sub='前に本人確認情報を提供した申請（毎日ドリル 第55日 イ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half, with two lanes stacked vertically. A common timeline axis runs left to right with two flags: the left flag labeled 前の申請 (with an icon of a signed document) and the right flag labeled 今回の申請 (with an icon of a new form).
Upper lane (green accent), lane label: 前の申請が四か月前. A green bracket spans from the left flag to the right flag, labeled 三月以上前. At its right end, a result badge with a green check mark: 面識ありとして扱える
Lower lane (orange accent), lane label: 前の申請が二か月前. An orange bracket spans a shorter distance from a point near the right flag back to the left, labeled 三月に足りない. At its right end, a result badge with a red cross: 面識ありとはいえない
The two bracket labels are different strings; draw them in different accent colors (green and orange). Use exactly these strings, and no others, for the labels.""",
            callout='前に本人確認情報を提供して申請したことで、面識があるといえるのは、今回の登記の申請の三月以上前の場合です。\n二か月前では足りず、書類の提示で確認します。',
            footer='不動産登記事務取扱手続準則四十九条一項',
            kanji='登・記・本・人・確・認・面・識・前・申・請・月・今・回・以・上・足・書・類・提・示'.split('・'), what='timeline',
            check='confirm the two lanes carry different bracket labels in different accent colors, with a green check mark only in the upper lane and a red cross only in the lower lane, ')),
        dict(name='本人確認情報が認められなかったときの流れ', args=dict(
            title='認められなければ、どうなる？', sub='本人確認情報と事前通知（毎日ドリル 第55日 オ）',
            req='a flow diagram',
            layout="""--- FLOW ---
Render as a clean flat-design vertical flow diagram. Top box (gray): 登記識別情報を提供できない. Below it, an arrow to a box (blue): 資格者代理人が本人確認情報を提供.
Below that, the flow splits into two branches with a small diamond in the middle labeled 登記官の判断.
LEFT BRANCH (green accent), arrow label: 相当と認める. Box: 事前通知をしない. Result badge with a green check mark: 登記が進む
RIGHT BRANCH (blue accent), arrow label: 相当と認められない. Box: 事前通知の手続. Result badge with a green check mark: 本人あてに通知して確かめる
Between the diamond and the right branch, show a separate small side box in gray with a red cross and the label 却下ではない.
Use exactly these strings, and no others.""",
            callout='本人確認情報を相当と認められないときは、申請が却下されるのではありません。\n登記官は、事前通知の手続に戻って、本人あてに通知をして確かめます。',
            footer='不動産登記法二十三条、不動産登記事務取扱手続準則四十九条四項',
            kanji='登・記・識・別・情・報・提・供・資・格・者・代・理・本・人・確・認・相・当・事・前・通・知・手・続・却・下'.split('・'), what='flow',
            check='confirm the left branch ends with 登記が進む, the right branch ends with 本人あてに通知して確かめる, and the red cross appears only on the small side box labeled 却下ではない, ')),
    ],
)
