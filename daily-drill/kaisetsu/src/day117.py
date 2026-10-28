D = dict(
    catch='強迫は常に取消し、詐欺は条件つき',
    intro='土地を売る契約で、意思表示に問題があったときの扱いを問う問題です（民法93条〜96条）。真意ではない意思表示、錯誤、詐欺、強迫は、それぞれ無効になるか取り消せるかの条件が違い、転売を受けた第三者がどこまで守られるかも違います。\n\nこの問題は、正しい肢の組合せを選ぶ形式です。相手方と第三者の事情に注目して、一つずつ確かめていきましょう。',
    sections={
        'ア': ('心裡留保の無効は、善意の第三者に対抗できない',
               '意思表示は、表意者が真意ではないことを知ってしたときでも、原則として有効です。ただし、相手方が真意ではないことを知り、又は知ることができたときは、無効となります（民法93条1項）。\n\nこの無効は、善意の第三者に対抗することができません（同条2項）。第三者の過失は問われません。\n\n本肢は正しいといえます。Bは真意でないことを知っていたので、AB間の売買は無効ですが、転売を受けたCが善意であれば、Cに過失があっても、Aは無効をCに対抗できません。\n\n**たとえば**、Aが売るつもりもないのに「売る」と言い、Bもそれを知っていたとします。Bから甲土地を買ったCが、Aの真意に気づかなかった（過失はあった）としても、Aは「契約は無効だ」とCに主張できません。'),
        'イ': ('第三者の強迫は、相手方が善意無過失でも取り消せる',
               '詐欺又は強迫による意思表示は、取り消すことができます（民法96条1項）。相手方が知っていたか、知ることができたかを条件にするのは、第三者が詐欺を行った場合です（同条2項）。\n\n問題文は、第三者の強迫で、Bが善意無過失なら取り消せないとしているので、本肢は誤りです。強迫の場合は、相手方が善意無過失でも、取り消すことができます。\n\n**たとえば**、Aが第三者Cに脅されて、甲土地をBに売ることにしたとします。Bが脅しのことをまったく知らず、知ることもできなかったとしても、Aは売買の意思表示を取り消せます。'),
        'ウ': ('相手方も同一の錯誤なら、重大な過失があっても取り消せる',
               '錯誤が表意者の重大な過失によるものであったときは、原則として取り消すことができません。ただし、相手方が表意者と同一の錯誤に陥っていたときなどは、重大な過失があっても取り消すことができます（民法95条3項）。\n\n問題文は、Bも同一の錯誤に陥っていても取り消せないとしているので、本肢は誤りです。\n\n**たとえば**、Aが「この土地の近くに道路が通る」と思い込み、ろくに確かめずに売ると決めたとします（重大な過失）。その事情が契約の前提としてBにも伝わっていて、Bも同じ思い込みをしていたなら、Aは錯誤を理由に取り消せます。'),
        'エ': ('第三者の詐欺は、相手方が知ることができたときも取り消せる',
               '第三者が詐欺を行った場合、相手方がその事実を知り、又は知ることができたときに限り、その意思表示を取り消すことができます（民法96条2項）。\n\n問題文は、Bが詐欺を知らなかったが、知ることができたときは取り消せないとしているので、本肢は誤りです。「知ることができた」場合も、取り消すことができます。\n\n**たとえば**、Aが第三者Cにだまされて、甲土地を売る決心をしたとします。Bは詐欺に気づきませんでしたが、少し確かめれば分かる状況だったなら、Aは取り消せます。'),
        'オ': ('詐欺の取消しは、過失のある第三者には対抗できる',
               '詐欺による意思表示の取消しは、善意でかつ過失がない第三者に対抗することができません（民法96条3項）。\n\n本肢は正しいといえます。Cは善意でも過失があるため、この規定では保護されません。Aは、取消しをCに対抗できます。\n\n**たとえば**、AがBにだまされて甲土地を売り、BがCに転売したとします。Cは詐欺を知りませんでしたが、確かめれば気づけた場合、Aは「契約を取り消したから、土地を返してほしい」とCに主張できます。'),
    },
    summary=[
        ('ア', '正', '心裡留保の無効は、善意の第三者に対抗できず、第三者の過失は問われない'),
        ('イ', '誤', '第三者の強迫による意思表示は、相手方が善意無過失でも取り消せる'),
        ('ウ', '誤', '重大な過失による錯誤でも、相手方が同一の錯誤に陥っていたときは取り消せる'),
        ('エ', '誤', '第三者の詐欺は、相手方が知り、又は知ることができたときに取り消せる'),
        ('オ', '正', '詐欺の取消しは、善意でかつ過失がない第三者に対抗できない。過失のある第三者には対抗できる'),
    ],
    summary_tail='イは「詐欺」と「強迫」、ウは「例外の見落とし」、エは「知ることができた」も含む点がひっかけです。保護される第三者の要件も、意思表示の種類ごとに違うと覚えておきましょう。',
    supplements=[
        '### 補足説明（イ・エ）：第三者が行った詐欺と強迫の違い\n\n相手方ではない第三者が、詐欺や強迫をした場合の取消しの条件は、次のように違います。\n\n- 第三者の詐欺：相手方が、詐欺の事実を知り、又は知ることができたときに限り、取り消せる（民法96条2項）。\n- 第三者の強迫：相手方が善意無過失でも、取り消せる（同条1項）。\n\n**たとえば**、Cにだまされた場合は、Bが事情を知らず、知ることもできなかったなら、Aは取り消せません。Cに脅された場合は、Bが何も知らなくても、Aは取り消せます。',
        '### 補足説明（ア・オ）：保護される第三者の要件の違い\n\n転売を受けた第三者が保護されるための要件は、意思表示の種類によって違います。\n\n- 心裡留保の無効：善意であればよい。過失は問われない（民法93条2項）。\n- 虚偽表示の無効：善意であればよい（同法94条2項）。\n- 錯誤の取消し：善意でかつ過失がない（同法95条4項）。\n- 詐欺の取消し：善意でかつ過失がない（同法96条3項）。\n\n**たとえば**、同じ「事情を知らなかったが、確かめれば気づけた」第三者Cでも、心裡留保の場合は保護されて、Aは無効を対抗できません。詐欺の場合は保護されず、Aは取消しを対抗できます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第117日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法93条1項・2項、94条2項、95条1項〜4項、96条1項〜3項は、`note-articles/laws/` 配下の原文で確認しました。',
        '強迫の取消しが、96条3項の「善意でかつ過失がない第三者」の規定に含まれていない点は、条文の文言からの一般的な整理です。強迫の取消しと第三者の関係の判例・学説は確認していません。',
        '具体例（売るつもりのない売買、脅された売主、道路が通ると思い込んだ売主など）は、条文の文言を日常の場面に置き換えた説明で、事実を創作したものではなく仮の設定です。',
    ],
    phrases=['心裡留保は善意の第三者に対抗できません', '第三者の強迫は善意でも取り消せます', '重過失でも同じ錯誤なら取り消せます', '第三者の詐欺は知ることができれば取消し', '詐欺の取消しは過失ある第三者に対抗できます'],
    header=dict(t1='無効と取消し、', t2='第三者は？', topic='民法　意思表示と第三者',
                kanji='無・効・取・消・第・三・者・意・思・表・示・民・法・毎'),
    poster_intro='意思表示の無効と取消しを、「無効と取消しの条件」（グループA：ア・イ・ウ）と「詐欺と第三者」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='意思表示の無効と取消しを整理', sub='民法 第93条〜第96条（毎日ドリル 第117日）',
        col_a='無効と取消しの条件', col_b='詐欺と第三者', n_a=3,
        cards=[
            dict(h='心裡留保は善意の第三者に対抗できない',
                 ill='three figures in a row: a seller figure on the left, a buyer figure in the middle, and a third-party figure on the right carrying a name tag labeled 「善意」. A small house model passes from left to right. A shield sits in front of the right figure. A green check mark sits beside the right figure.',
                 words=['善意'], tag='過失は問われない'),
            dict(h='第三者の強迫は取り消せる',
                 ill='a shadowy figure labeled 「強迫」 behind a seller figure who is signing a paper, while a calm buyer figure stands on the other side. A stamp labeled 「取消し」 sits beside the seller. A green check mark sits beside the stamp.',
                 words=['強迫', '取消し'], tag='相手方が善意でも取消し可'),
            dict(h='同一の錯誤なら重過失でも取り消せる',
                 ill='a seller figure and a buyer figure side by side, each with an identical thought bubble containing a plain land plot icon, joined by a thin link line labeled 「同一の錯誤」. A stamp labeled 「取消し」 sits beside them. A green check mark sits beside the stamp.',
                 words=['同一の錯誤', '取消し'], tag='相手方も同じ錯誤なら可'),
            dict(h='第三者の詐欺は有過失でも取り消せる',
                 ill='a third-party figure labeled 「詐欺」 whispering to a seller figure. The buyer figure holds a magnifying glass over a document, with a speech bubble labeled 「知ることができた」. A green check mark sits beside the seller.',
                 words=['詐欺', '知ることができた'], tag='知ることができたら取消し可'),
            dict(h='詐欺の取消しは過失ある第三者に対抗できる',
                 ill='a seller figure, a buyer figure and a third-party figure carrying a name tag labeled 「過失あり」. A green arrow with a stamp labeled 「取消し」 goes from the seller to the third-party figure. A green check mark sits beside the seller.',
                 words=['過失あり', '取消し'], tag='善意無過失でないと保護なし'),
        ],
        kanji='無・効・善・意・第・三・者・強・迫・錯・誤・詐・欺・取・消・過・失・同・一・知'.split('・')),
    nb_label='ア・イ・エ・オ肢', nb_intro='イ・エ、ア・オの補足説明に合わせた2枚です。1枚目は、第三者の詐欺と第三者の強迫を左右の対比で示します。2枚目は、保護される第三者の要件の違いを表で示します。',
    notebooks=[
        dict(name='第三者の詐欺と、第三者の強迫の違い', args=dict(
            title='詐欺と強迫、取り消せる条件は？', sub='第三者が行った場合（毎日ドリル 第117日 イ・エ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「第三者の詐欺」 on the left and 「第三者の強迫」 on the right. Draw them in different accent colors (blue and orange) so they can never be confused or duplicated. Both result badges carry a green check mark, but the two badge texts are different strings.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 第三者の詐欺
Scene: an isometric scene of a third-party figure whispering to a seller figure, with a buyer figure standing on the other side.
Result badge with a green check mark: 相手方が知り、又は知ることができたときに取り消せる

RIGHT PANEL (orange accent):
Panel header: 第三者の強迫
Scene: an isometric scene of a shadowy figure pressuring a seller figure, with a buyer figure standing on the other side holding nothing.
Result badge with a green check mark: 相手方が善意無過失でも取り消せる""",
            callout='第三者の詐欺は、相手方が知り、又は知ることができたときに限り、取り消せます。\n第三者の強迫は、相手方が善意無過失でも、取り消せます。',
            footer='民法96条1項・2項',
            kanji='第・三・者・詐・欺・強・迫・相・手・方・知・取・消・善・意・無・過・失'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (第三者の詐欺 on the left and 第三者の強迫 on the right) drawn in different accent colors, and that the two result badges are different strings, ')),
        dict(name='保護される第三者の要件の違い', args=dict(
            title='保護される第三者の要件', sub='転売を受けた第三者（毎日ドリル 第117日 ア・オ）',
            req='a four-row comparison table',
            layout="""--- TABLE ---
Render as a clean flat-design table with four data rows and two columns, with a header row. Header row: 意思表示 | 保護される第三者.
Row 1 and Row 2 are tinted green (the requirement is lighter), Row 3 and Row 4 are tinted blue (the requirement is stricter).
Row 1: 心裡留保の無効 | 善意の第三者
Row 2: 虚偽表示の無効 | 善意の第三者
Row 3: 錯誤の取消し | 善意でかつ過失がない第三者
Row 4: 詐欺の取消し | 善意でかつ過失がない第三者
Add a small house icon with a seller, a buyer and a third-party figure in a chain on the left side of the table.
Use exactly these strings, and no others. Row 1 and Row 2 share the same right-cell string, and Row 3 and Row 4 share the same right-cell string; that is correct and intended.""",
            callout='心裡留保と虚偽表示の無効は、善意の第三者であれば保護され、過失は問われません。\n錯誤と詐欺の取消しは、善意でかつ過失がない第三者でないと保護されません。',
            footer='民法93条2項、94条2項、95条4項、96条3項',
            kanji='心・裡・留・保・虚・偽・表・示・無・効・錯・誤・詐・欺・取・消・善・意・過・失・第・三・者'.split('・'), what='table',
            check='confirm there are exactly four data rows with the exact strings above, ')),
    ],
)
