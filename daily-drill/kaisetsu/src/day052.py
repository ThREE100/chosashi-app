D = dict(
    catch='原本の還付は調査完了後、委任状は返らない',
    intro='登記を申請したあとの手続を問う問題です（不動産登記法17条、不動産登記規則38条・39条・55条）。出した書類は返してもらえるのか、返してもらえるならいつか、申請が却下されたり取り下げられたりしたときはどうなるのかを確かめます。\n\nこの問題は、誤っている記述の組合せを選ぶ形です。誤りの肢は、原本の還付の例外と時期を取り違えさせています。',
    sections={
        'ア': ('その申請のためだけの委任状は、返してもらえない',
               '書面で申請した人は、申請書に添付した書面の原本の還付を請求できます。ただし、その申請のためにのみ作成された委任状などは、請求できません（不動産登記規則55条1項）。\n\n問題文は、調査士への委任状について原本の還付を請求できるとしているので、本肢は誤りです。\n\n**たとえば**、調査士に頼むためだけに書いた委任状は、申請書に添付したまま登記所に残ります。他の手続にも使う書類とは扱いが違います。'),
        'イ': ('原本の還付は、調査完了後に行われる',
               '登記官は、原本の還付の請求があったときは、調査完了後に、原本を還付します（不動産登記規則55条3項）。原本と相違ない旨を書いた謄本は、登記完了後に申請書類つづり込み帳につづり込みます（同条4項）。\n\n問題文は、登記完了後に原本を還付するとしているので、本肢は誤りです。\n\n**たとえば**、原本の還付を請求した書類は、登記が完了するのを待たずに、調査が終わった時点で戻ってきます。登記完了後に残るのは、控えとして出した謄本のほうです。'),
        'ウ': ('取り下げたときは、申請書と添付書面が返される',
               '申請の取下げは、登記完了後はすることができません（不動産登記規則39条2項）。書面申請の取下げがあったときは、登記官は、申請書及びその添付書面を還付します（同条3項）。\n\n本肢は正しい記述です。\n\n**たとえば**、申請書に書き間違いを見つけて、登記が完了する前に申請を取り下げたときは、出した申請書と添付した書類が返されます。'),
        'エ': ('却下の決定書は、代理人に渡せば足りる',
               '登記官は、申請を却下するときは、決定書を作成して、申請人ごとに交付します。ただし、代理人によって申請がされた場合は、その代理人に交付すれば足ります（不動産登記規則38条1項）。\n\n本肢は正しい記述です。\n\n**たとえば**、依頼者から委任を受けた調査士Bが分筆の登記を申請して却下されたときは、決定書は依頼者ではなく、調査士Bに渡されます。'),
        'オ': ('本人が死亡しても、委任による代理権は消えない',
               '登記の申請をする者の委任による代理人の権限は、本人の死亡によっては消滅しません（不動産登記法17条1号）。\n\n本肢は正しい記述です。\n\n**たとえば**、分筆の登記を調査士Bに頼んだ依頼者Aが、申請の前に亡くなったとします。それでもBの代理権は消えず、Bは続けて申請できます。民法の一般的な代理では、本人が死亡すると代理権が消えるのと、違うところです。'),
    },
    summary=[
        ('ア', '誤', 'その申請のためにのみ作成された委任状は、原本の還付を請求できない'),
        ('イ', '誤', '原本は、登記完了後ではなく、調査完了後に還付される'),
        ('ウ', '正', '書面申請を取り下げたときは、申請書及びその添付書面が還付される'),
        ('エ', '正', '代理人が申請した場合の却下の決定書は、その代理人に交付すれば足りる'),
        ('オ', '正', '委任による代理人の権限は、本人の死亡によっては消滅しない'),
    ],
    summary_tail='アとイは、原本の還付の「例外」と「時期」を取り違えさせる出題です。ウとエは、取下げと却下の扱いが問われています。何が返り、いつ返るのかを、場面ごとに整理しましょう。',
    supplements=[
        '### 補足説明（ア・イ）：原本の還付の請求\n\n書面申請では、添付した書面の原本の還付を請求できる場合があります（不動産登記規則55条）。\n\n| 項目 | 内容 |\n|---|---|\n| 請求できるか | 原則として請求できる |\n| 請求できないもの | その申請のためにのみ作成された委任状など |\n| 請求するときに出すもの | 原本と相違ない旨を書いた謄本 |\n| 原本が返される時期 | 調査完了後 |\n| 謄本の扱い | 登記完了後に申請書類つづり込み帳につづり込む |\n\n**たとえば**、他の手続にも使う書類は、謄本を添えて原本の還付を請求し、調査が終わったら原本を返してもらいます。その申請のためだけの委任状は、返してもらえません。',
        '### 補足説明（ウ・エ）：取下げと却下の扱い\n\n申請が完了しないで終わる二つの場合は、扱いが違います。\n\n| | 取下げ | 却下 |\n|---|---|---|\n| だれが決めるか | 申請人 | 登記官 |\n| できる時期 | 登記完了前に限る（39条2項） | 申請に問題があるとき |\n| 返される書類 | 申請書及び添付書面（39条3項） | 添付書面（38条3項） |\n| 決定書 | 作られない | 申請人ごとに交付。代理人が申請したときは代理人に交付（38条1項） |\n\n**たとえば**、自分から取り下げたときは、出した申請書も返ってきます。登記官に却下されたときは、返ってくるのは添付書面で、決定書が代理人に渡されます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第52日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法17条1号と、不動産登記規則38条1項・3項、39条2項・3項、55条1項・3項・4項は、`note-articles/laws/` 配下の原文で確認しました。',
        'オは、17条の文言（登記の申請をする者の委任による代理人の権限は、本人の死亡によって消滅しない）に基づきます。民法の一般的な代理との違いの説明は、条文からの一般的な整理で、民法の条文は今回確認していません。',
        'アの「他の手続にも使う書類」やイの「控えとして出した謄本」は、規則55条の言葉を場面に置き換えた説明です。具体例は、場面を思い描くための例です。',
    ],
    phrases=['その申請だけの委任状は返りません', '原本は調査完了後に返ります', '取り下げると申請書が返ります', '決定書は代理人に渡せば足ります', '本人が亡くなっても代理権は残ります'],
    header=dict(t1='申請の書類、', t2='いつ返る？', topic='不動産登記　申請の手続',
                kanji='申・請・書・類・返・手・続'),
    poster_intro='登記申請後の手続を、「書類の還付と取下げ」（グループA：ア・イ・ウ）と「却下と代理権」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='申請後の手続を整理', sub='不動産登記規則 第55条と第39条ほか（毎日ドリル 第52日）',
        col_a='書類の還付と取下げ', col_b='却下と代理権', n_a=3,
        cards=[
            dict(h='その申請だけの委任状は返らない',
                 ill='a power-of-attorney sheet labeled 「委任状」 clipped to an application sheet inside a folder at a registry counter, staying in the folder. A green check mark sits beside the folder.',
                 words=['委任状'], tag='原本還付の対象外'),
            dict(h='原本が返るのは調査完了後',
                 ill='a horizontal timeline with two flags labeled 「調査完了」 and 「登記完了」. An original document is handed back to an applicant figure at the first flag. The second flag has nothing handed back. A green check mark sits beside the first flag.',
                 words=['調査完了', '登記完了'], tag='登記完了を待たない'),
            dict(h='取り下げると書類が返る',
                 ill='an applicant figure receiving a stack of application papers across a registry counter, with a round stamp labeled 「取下げ」 on the counter. A green check mark sits beside the stack of papers.',
                 words=['取下げ'], tag='登記完了前に限る'),
            dict(h='却下の決定書は代理人に交付',
                 ill='a registry officer figure handing a decision sheet labeled 「決定書」 to a surveyor figure with a tripod, while an applicant figure stands faded in the background. A green check mark sits beside the surveyor.',
                 words=['決定書'], tag='代理人に渡せば足りる'),
            dict(h='本人が死亡しても代理権は消えない',
                 ill='a surveyor figure holding an application form and a sign labeled 「代理権」, standing next to a faded gray client figure drawn in outline. A green check mark sits beside the surveyor.',
                 words=['代理権'], tag='委任による代理人'),
        ],
        kanji='委・任・状・調・査・完・了・登・記・取・下・決・定・書・代・理・権'.split('・')),
    nb_label='ア・イ・ウ肢', nb_intro='ア・イ・ウの補足説明に合わせた2枚です。1枚目は、原本の還付の請求について、できるものとできないもの、時期を図で示します。2枚目は、取下げと却下の違いを左右の対比で示します。',
    notebooks=[
        dict(name='原本の還付の請求', args=dict(
            title='原本は、いつ返る？', sub='添付書面の原本の還付（毎日ドリル 第52日 ア・イ）',
            req='a flow diagram',
            layout="""--- FLOW ---
Render as a clean flat-design vertical flow in two blocks.
Block 1 (blue accent), block header: 原本の還付を請求するとき. Three rows stacked vertically, each with a small icon: a copy sheet with the label 原本と相違ない旨を書いた謄本を出す | a document returned to an applicant with the label 調査完了後に原本を返す | a copy sheet filed in a binder with the label 謄本は登記完了後につづり込む
Between the rows, draw small downward arrows with no text.
Block 2 (orange accent), block header: 請求できないもの. A single row with a power-of-attorney sheet and the label: その申請のためにのみ作成された委任状など
Use exactly these strings, and no others, for the labels. The 調査完了後 label and the 登記完了後 label are different strings; draw them in different accent colors (blue and orange).""",
            callout='原本の還付は、調査完了後に行われます。登記完了後に残るのは、控えとして出した謄本のほうです。\nその申請のためにのみ作成された委任状は、還付を請求できません。',
            footer='不動産登記規則55条',
            kanji='原・本・還・付・請・求・調・査・完・了・後・謄・委・任・状・登・記'.split('・'), what='flow diagram',
            check='confirm the labels 調査完了後 and 登記完了後 are different strings in different accent colors, ')),
        dict(name='取下げと却下の違い', args=dict(
            title='取下げと却下は、どう違う？', sub='申請が完了しないで終わる場合（毎日ドリル 第52日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings. The left header is 取下げ and the right header is 却下. Draw them in different accent colors (blue on the left and orange on the right) so they can never be confused or duplicated. Neither panel uses a cross mark.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 取下げ
Scene: an isometric scene of an applicant figure handing a withdrawal sheet to a registry officer figure, and receiving back a stack of papers.
Result badges (stacked): 申請人が行う | 登記完了前に限る | 申請書及び添付書面が返る

RIGHT PANEL (orange accent):
Panel header: 却下
Scene: an isometric scene of a registry officer figure handing a decision sheet to a surveyor figure standing in for the applicant.
Result badges (stacked): 登記官が行う | 添付書面が返る | 決定書は代理人に交付""",
            callout='取下げは申請人が登記完了前に行い、申請書も添付書面も返されます。\n却下は登記官が行い、返されるのは添付書面で、決定書は代理人が申請したときは代理人に渡されます。',
            footer='不動産登記規則38条・39条',
            kanji='取・下・却・申・請・登・記・完・了・前・書・面・決・定・代・理・人'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (取下げ on the left and 却下 on the right) in different accent colors, ')),
    ],
)
