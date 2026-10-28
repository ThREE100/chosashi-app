D = dict(
    catch='筆界特定書は永久、取下げは通知の発送まで',
    intro='筆界特定の手続と、その記録の扱いを問う問題です（不動産登記法148条、不動産登記規則234条・235条・245条・246条）。筆界特定とは、土地と土地の筆界（境目）の位置を、筆界特定登記官が明らかにする手続のことです。\n\nこの記事では、記録の保存期間、取下げができなくなる時点、登記記録への記録、書面の更正、判決との関係を、具体的な場面で確かめていきましょう。',
    sections={
        'ア': ('筆界特定書の情報の保存期間は、永久',
               '筆界特定書に記載され、又は記録された情報の保存期間は、永久です。送付を受けた年の翌年から三十年間とされているのは、筆界特定書以外の筆界特定手続記録です（不動産登記規則235条1項1号・2号）。\n\n問題文は筆界特定書の情報を三十年間としているので、本肢は誤りです。\n\n**たとえば**、筆界の位置の結論を書いた筆界特定書は、いつまでも残ります。一方、手続の途中で集めた資料などの記録は、三十年間の保存です。'),
        'イ': ('取下げができなくなるのは、申請人への通知を発送した後',
               '筆界特定の申請の取下げは、申請人に対する通知を発送した後は、することができません（不動産登記規則245条2項）。\n\n問題文は「関係人に対する通知がされるまでは、取り下げることができる」としているので、本肢は誤りです。取下げの締切りは、関係人への通知の時ではなく、申請人への通知を発送した時です。\n\n**たとえば**、Aさんの筆界特定の申請について、Aさんあての通知が発送されたあとは、まだ隣の人への通知が済んでいなくても、取り下げることはできません。'),
        'ウ': ('筆界特定がされた旨は、対象土地の登記記録に記録される',
               '筆界特定がされた筆界特定手続記録の送付を受けた登記所の登記官は、対象土地の登記記録に、筆界特定がされた旨を記録しなければなりません（不動産登記規則234条）。\n\n対象土地は、筆界の両側の土地です。甲土地と乙土地の間の筆界であれば、両方の登記記録に記録します。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地と乙土地の間の筆界について筆界特定がされたら、甲土地の登記記録にも、乙土地の登記記録にも、「筆界特定がされた」と記録されます。'),
        'エ': ('筆界特定書の誤記は、いつでも、長の許可を得て更正できる',
               '筆界特定書に誤記その他これに類する明白な誤りがあるときは、筆界特定登記官は、いつでも、監督する法務局又は地方法務局の長の許可を得て、更正することができます（不動産登記規則246条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、筆界特定書の中に、土地の地番の書き間違いが見つかったとします。この場合、期限を気にせず、長の許可を得て直すことができます。直したときは、申請人への通知や公告などもします（同条2項）。'),
        'オ': ('判決が確定すると、抵触する範囲で筆界特定は効力を失う',
               '筆界特定がされた筆界について、筆界確定訴訟の判決が確定したときは、その筆界特定は、判決と抵触する範囲において、効力を失います（不動産登記法148条）。\n\n問題文は「抵触する範囲でも、効力を失わない」としているので、本肢は誤りです。\n\n**たとえば**、筆界特定では線Aの位置とされたのに、確定した判決では線Bの位置とされた場合、食い違う部分については判決が優先し、筆界特定の効力はなくなります。'),
    },
    summary=[
        ('ア', '誤', '筆界特定書の情報の保存期間は永久で、三十年間は筆界特定書以外の記録'),
        ('イ', '誤', '取下げができなくなるのは、申請人への通知を発送した後である'),
        ('ウ', '正', '筆界特定がされた旨は、対象土地（両側の土地）の登記記録に記録する'),
        ('エ', '正', '筆界特定書の誤記は、いつでも、長の許可を得て更正できる'),
        ('オ', '誤', '判決が確定すると、筆界特定は、判決と抵触する範囲で効力を失う'),
    ],
    summary_tail='アは「永久」と「三十年間」の入れ替え、イは通知の相手のすり替え、オは判決との関係を逆にした出題です。何が、いつまで、だれにという点を、一つずつ確かめましょう。',
    supplements=[
        '### 補足説明（ア）：筆界特定の記録の保存期間\n\n筆界特定の手続の記録は、種類によって保存期間が違います（不動産登記規則235条1項）。\n\n| 記録の種類 | 保存期間 |\n|---|---|\n| 筆界特定書に記載され、又は記録された情報 | 永久 |\n| 筆界特定書以外の筆界特定手続記録 | 送付を受けた年の翌年から三十年間 |\n\n**たとえば**、筆界の位置を示す結論の書面（筆界特定書）は、ずっと見られるように残されます。手続の途中で出された資料などは、登記所が送付を受けた年の翌年から三十年間の保存です。',
        '### 補足説明（イ）：取下げの締切りは、申請人への通知の発送\n\n筆界特定の申請は、取り下げることができる期間が決まっています（不動産登記規則245条2項）。\n\n- 申請人への通知を発送する前：取り下げることができます。\n- 申請人への通知を発送した後：取り下げることはできません。\n- 関係人への通知は、締切りの基準ではありません。\n\n**たとえば**、Aさんあての通知が10日に発送され、隣の人への通知が12日になったとします。10日の発送以後は、Aさんは取り下げられません。締切りは、隣の人への通知の12日ではありません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第56日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法148条、不動産登記規則234条・235条・245条・246条は、`note-articles/laws/` 配下の原文で確認しました。',
        '具体例（地番の書き間違い、通知の日付の例、線Aと線Bの例）は、条文の文言をかみ砕いた一般的な説明で、個別の先例・通達の確認はしていません。',
        'ウでいう「対象土地」が筆界の両側の土地であることは、不動産登記法123条の定義による一般的な整理です。',
    ],
    phrases=['筆界特定書の情報は、永久に残ります', '取下げは、申請人への通知の発送まで', '筆界特定の旨は、両方の土地に記録されます', '誤記は、いつでも長の許可で更正できます', '判決が確定すれば、抵触する範囲は失効です'],
    header=dict(t1='筆界特定の記録、', t2='いつまで残る？', topic='不動産登記法　筆界特定',
                kanji='登・記・毎・筆・界・特・定'),
    poster_intro='筆界特定の手続と記録を、「保存と手続」（グループA：ア・イ）と「記録と効力」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='筆界特定の手続と記録を整理', sub='不動産登記規則 第234条・第235条・第245条・第246条（毎日ドリル 第56日）',
        col_a='保存と手続', col_b='記録と効力', n_a=2,
        cards=[
            dict(h='筆界特定書の情報は永久に保存',
                 ill='a bound document labeled 「筆界特定書」 placed on a shelf, with an infinity-shaped ribbon around it. A green check mark sits beside the document.',
                 words=['筆界特定書'], tag='永久保存'),
            dict(h='取下げは申請人への通知の発送まで',
                 ill='a horizontal timeline. On the left a flag labeled 「通知の発送」; a green section of the line before the flag labeled 「取下げ可」; a gray section after the flag labeled 「取下げ不可」. A green check mark sits beside the green section.',
                 words=['通知の発送', '取下げ可', '取下げ不可'], tag='発送の前まで'),
            dict(h='両側の土地の登記記録に記録',
                 ill='two neighboring land plots with a dotted boundary line between them. Above each plot a record sheet carries a small stamp labeled 「特定」. A green check mark sits between the two sheets.',
                 words=['特定'], tag='両方に記録'),
            dict(h='誤記は長の許可でいつでも更正',
                 ill='a document with one line corrected by a pencil, and an approval stamp labeled 「許可」 beside it. A green check mark sits beside the stamp.',
                 words=['許可'], tag='いつでも更正'),
            dict(h='判決が確定すれば抵触部分は失効',
                 ill='two overlapping boundary lines between two land plots, one labeled 「特定」 and one labeled 「判決」, with a gavel icon beside the second line. The area where the two lines differ is highlighted in light gray. A green check mark sits beside the line labeled 「判決」.',
                 words=['特定', '判決'], tag='判決が優先'),
        ],
        kanji='筆・界・特・定・書・取・下・通・知・発・送・可・不・判・決・永・久・保・存・両・側・土・地・許・正・誤・更'.split('・')),
    nb_label='ア・イ肢', nb_intro='ア・イの補足説明に合わせた2枚です。1枚目は、筆界特定の記録の保存期間を左右の対比で示します。2枚目は、取下げができる時期を時間の流れで示します。',
    notebooks=[
        dict(name='筆界特定の記録の保存期間', args=dict(
            title='記録は、いつまで残る？', sub='筆界特定の記録の保存期間（毎日ドリル 第56日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「筆界特定書」 on the left and 「それ以外の記録」 on the right. Draw them in different accent colors (blue and gray). The two result badges are also different strings: 「永久」 on the left and 「三十年間」 on the right.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 筆界特定書
Scene: an isometric scene of a bound document on a shelf, with an infinity-shaped ribbon around it.
Result badge with a green check mark: 永久

RIGHT PANEL (gray accent):
Panel header: それ以外の記録
Scene: an isometric scene of a box of loose papers on a shelf with a small calendar beside it. Beneath the scene, a small note: 送付を受けた年の翌年から
Result badge with a green check mark: 三十年間""",
            callout='筆界の位置の結論を書いた筆界特定書の情報は、永久に保存されます。\n三十年間とされるのは、筆界特定書以外の記録で、送付を受けた年の翌年から数えます。',
            footer='不動産登記規則二百三十五条一項',
            kanji='筆・界・特・定・書・記・録・永・久・年・間・三・十・送・付・受・翌'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (筆界特定書 on the left and それ以外の記録 on the right) and that the two result badges read 永久 on the left and 三十年間 on the right, each with a green check mark, ')),
        dict(name='取下げができる時期', args=dict(
            title='取下げは、いつまでできる？', sub='筆界特定の申請の取下げ（毎日ドリル 第56日 イ）',
            req='a timeline diagram',
            layout="""--- TIMELINE ---
Render as a clean flat-design horizontal timeline in the upper half. A common timeline axis runs left to right with two flags: the left flag labeled 申請人への通知の発送 (with an icon of an envelope sent to a person figure) and the right flag labeled 関係人への通知 (with an icon of an envelope sent to another person figure).
Before the left flag, the axis is drawn in green with a bracket labeled 取り下げることができる and a green check mark.
After the left flag, the axis is drawn in gray with a bracket labeled 取り下げることはできない and a red cross. The right flag lies inside the gray part; beside it a small note: 締切りの基準ではない
Use exactly these strings, and no others, for the labels.""",
            callout='取下げができなくなるのは、申請人に対する通知を発送した後です。\n関係人への通知は、取下げの締切りの基準ではありません。',
            footer='不動産登記規則二百四十五条二項',
            kanji='筆・界・特・定・申・請・人・通・知・発・送・関・係・取・下・締・切・基・準'.split('・'), what='timeline',
            check='confirm the green section with a green check mark lies only before the left flag and the gray section with a red cross lies only after it, ')),
    ],
)
