D = dict(
    catch='敷地権の登記は、記録場所と主体に注意',
    intro='マンションなどの区分建物と、その敷地の権利（敷地権）に関する登記を問う問題です（不動産登記規則118条・119条・123条、不動産登記法46条、区分所有法22条）。敷地権の登記は、建物の登記記録と土地の登記記録の両方にかかわります。\n\nこの記事では、敷地権が「どこに」「だれによって」記録されるのかと、抵当権があるときの処理、分離処分の禁止を、具体的な場面で確認していきましょう。なお、この問題は「誤っているもの」を選ぶ問題です。',
    sections={
        'ア': ('建物の表題部には、土地の表示と敷地権の種類・割合を記録する',
               '区分建物の登記記録の表題部に敷地権を記録するときは、敷地権の登記原因及びその日付のほか、次の事項を記録します（不動産登記規則118条）。\n\n- 敷地権の目的である土地の不動産所在事項、地目、地積。\n- 敷地権の種類。\n- 敷地権の割合。\n\n本肢は正しいといえます。\n\n**たとえば**、マンションの一室の表題部には、「敷地権の表示」の欄があります。そこに、土地の所在や地番、地目、地積、そして「所有権」という種類と、持分の割合が記録されます。'),
        'イ': ('敷地権である旨は、土地の権利部に登記する',
               '区分建物の敷地権について、表題部に最初に登記をしたときは、敷地権の目的である土地の登記記録に、敷地権である旨の登記をします（不動産登記法46条）。\n\nこの登記は、土地の登記記録の「権利部の相当区」に記録します（不動産登記規則119条1項）。所有権が敷地権なら甲区、地上権や賃借権などなら乙区です。\n\n問題文は「土地の登記記録の表題部に」としているので、本肢は誤りです。\n\n**たとえば**、マンションの敷地が所有権だとします。敷地権である旨は、土地の登記記録の表題部ではなく、権利部の甲区に記録されます。'),
        'ウ': ('敷地権である旨の登記は、登記官が職権でする',
               '敷地権である旨の登記は、登記官が職権でします（不動産登記法46条）。申請人が申請するものではありません。\n\n敷地権の目的である土地が他の登記所の管轄区域内にあるときは、建物の登記を担当した登記官が、遅滞なく、その登記所に通知します。通知を受けた登記所の登記官が、土地の登記記録に記録します（不動産登記規則119条2項・3項）。\n\n問題文は「申請人は…申請しなければならない」としているので、本肢は誤りです。\n\n**たとえば**、マンションの敷地が別の法務局の管轄にあっても、申請人が土地側の法務局へ別に申請する必要はありません。登記官どうしの通知で、土地の登記記録にも記録されます。'),
        'エ': ('同じ内容の抵当権は、土地側の登記を職権で抹消する',
               '建物の表題部の変更の登記で新たに敷地権の登記をした場合、建物に抵当権の登記があれば、原則として、その抵当権の登記に「建物のみに関する旨」を付記します（不動産登記規則123条1項本文）。\n\nただし、建物の抵当権と土地の敷地権についての抵当権が、登記の目的、申請の受付の年月日及び受付番号、登記原因及びその日付までそっくり同じときは、付記をしません。この場合、登記官は、土地の抵当権の登記を職権で抹消します（同条1項ただし書・2項）。本肢は正しいといえます。\n\n**たとえば**、B銀行の同じ抵当権が、マンションの一室と敷地の両方に付いていたとします。敷地権の登記をすると、建物の登記が敷地権についての登記としての効力を持つ（不動産登記法73条1項本文）ため、土地側の抵当権の登記は抹消されます。'),
        'オ': ('専有部分の全部を持つ人も、規約がなければ分離して処分できない',
               '敷地利用権が数人で有する権利である場合、区分所有者は、規約に別段の定めがなければ、専有部分と敷地利用権を分離して処分できません（区分所有法22条1項）。\n\nこの規定は、専有部分の全部を所有する者の敷地利用権が、単独で有する所有権その他の権利である場合にも準用されます（同条3項）。本肢は正しいといえます。\n\n**たとえば**、一棟のマンションの全部の部屋をAさんが一人で所有し、敷地もAさんの単独所有だとします。規約に別段の定めがなければ、Aさんは、部屋だけを売ったり、土地だけを売ったりすることはできません。'),
    },
    summary=[
        ('ア', '正', '表題部には、土地の表示、敷地権の種類と割合、原因日付を記録する'),
        ('イ', '誤', '敷地権である旨の登記は、土地の表題部ではなく権利部の相当区に記録する'),
        ('ウ', '誤', '敷地権である旨の登記は、申請人ではなく登記官が職権でし、他の登記所には通知する'),
        ('エ', '正', '登記の目的などが同一の抵当権は、土地側の抵当権の登記を職権で抹消する'),
        ('オ', '正', '専有部分の全部を所有する者の単独の敷地利用権にも、分離処分の禁止が準用される'),
    ],
    summary_tail='イは「記録する場所」、ウは「だれがするか」を入れ替えた出題です。敷地権は、建物の表題部に記録され、土地の権利部には登記官が「敷地権である旨」を記録する、と整理しておきましょう。',
    supplements=[
        '### 補足説明（イ・ウ）：敷地権の登記は、建物と土地の二か所に載る\n\n敷地権に関する登記は、建物の登記記録と土地の登記記録の両方に記録されます。\n\n| 場所 | 記録する内容 | 記録のしかた |\n|---|---|---|\n| 区分建物の表題部 | 土地の表示、敷地権の種類と割合、原因日付（不動産登記規則118条） | 建物の登記として記録する |\n| 土地の登記記録の権利部の相当区 | 敷地権である旨（同規則119条1項） | 登記官が職権でする（不動産登記法46条）。他の登記所の土地は、通知を受けた登記官が記録する（同規則119条2項・3項） |\n\n**たとえば**、所有権が敷地権のマンションでは、建物の表題部に敷地権の表示があり、土地の甲区にも「敷地権である旨」が記録されます。',
        '### 補足説明（エ）：建物と土地の抵当権が同じ内容かどうか\n\n建物の表題部の変更の登記で新たに敷地権の登記をするときの、抵当権の扱いは、次のとおりです。\n\n| 建物の抵当権と土地の抵当権 | 登記官の処理 |\n|---|---|\n| 登記の目的、申請の受付の年月日及び受付番号、登記原因及びその日付が同一 | 土地の抵当権の登記を職権で抹消する（不動産登記規則123条1項ただし書・2項） |\n| 同一でない | 建物の抵当権の登記に、「建物のみに関する旨」を付記登記で記録する（同条1項本文） |\n\n**たとえば**、同じ日に同じ原因で設定された、同じ受付番号の抵当権が建物と土地にあれば、土地側が抹消されます。一方、設定の日が違うなど内容が同一でない抵当権は、建物の抵当権の登記に「建物のみに関する旨」が付記されます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第38日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法46条・73条、不動産登記規則118条・119条・123条、区分所有法22条は、`note-articles/laws/` 配下の原文で確認しました。',
        '各肢の具体例（敷地権の表示の欄、別の法務局の敷地、B銀行の抵当権、全部の部屋を持つ人）は、条文の文言をかみ砕いた一般的な説明で、個別の先例・通達の確認はしていません。',
        '補足説明（イ・ウ）の表は、不動産登記法46条と規則119条を並べた整理です。エの「建物の登記が敷地権についての登記としての効力を持つので、土地側が抹消される」という説明は、法73条1項本文と規則123条を結び付けた条文からの一般的な整理です。',
    ],
    phrases=['表題部に敷地権の種類と割合を記録します', '敷地権である旨は土地の権利部に載ります', '敷地権の登記は登記官の職権です', '同じ抵当権は土地側が職権で抹消されます', '専有部分と敷地は規約がなければ一体です'],
    header=dict(t1='敷地権のしくみ、', t2='どこに記録する？', topic='不動産登記法　敷地権',
                kanji='敷・地・権・記・録'),
    poster_intro='敷地権を、「敷地権の記録と登記」（グループA：ア・イ・ウ）と「抵当権と分離処分」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='敷地権のしくみを整理', sub='不動産登記規則 第118条・第119条・第123条（毎日ドリル 第38日）',
        col_a='敷地権の記録と登記', col_b='抵当権と分離処分', n_a=3,
        cards=[
            dict(h='表題部に土地の表示と割合を記録',
                 ill='an isometric apartment building model and, beside it, a record sheet whose upper section is labeled 「表題部」. In the upper section, a line shows a small land plot icon and a line shows a fraction bar labeled 「割合」. A green check mark sits beside the sheet.',
                 words=['表題部', '割合'], tag='種類と割合も記録'),
            dict(h='敷地権である旨は土地の権利部に',
                 ill='an isometric land plot with a record sheet beside it. The sheet has an upper section labeled 「表題部」 drawn in gray and a lower section labeled 「甲区」 highlighted in green with a round stamp labeled 「敷地権」. A green check mark sits beside the lower section.',
                 words=['表題部', '甲区', '敷地権'], tag='権利部の相当区'),
            dict(h='敷地権である旨は登記官が職権で登記',
                 ill='two small office buildings connected by an arrow carrying an envelope labeled 「通知」. A registrar figure sits at a desk in the right building. An applicant figure on the left waves with empty hands and holds no form. A green check mark sits beside the registrar.',
                 words=['通知'], tag='申請は不要'),
            dict(h='同じ抵当権なら土地側を職権で抹消',
                 ill='an apartment building model and a land plot, each with an identical record sheet labeled 「抵当権」. A single thin horizontal line, not an X shape, is drawn through the land plot sheet only. A registrar figure with a stamp stands beside the land plot. A green check mark sits beside the registrar.',
                 words=['抵当権'], tag='土地側を抹消'),
            dict(h='専有部分の全部を持つ人も分離できない',
                 ill='a single owner figure holding an apartment building model in one hand and a land plot model in the other, with a chain link connecting the two models. A green check mark sits beside the chain. No text on any object.',
                 words=[], tag='規約がなければ一体'),
        ],
        kanji='敷・地・権・表・題・部・割・合・甲・区・登・記・官・職・通・知・抵・当・抹・消・専・有・分・離・規・約'.split('・')),
    nb_label='イ・ウ・エ肢', nb_intro='イ・ウ・エの補足説明に合わせた2枚です。1枚目は、敷地権の登記が建物の登記記録と土地の登記記録のどこに載るかを左右の対比で示します。2枚目は、建物と土地の抵当権が同一かどうかで登記官の処理が分かれることを左右の対比で示します。',
    notebooks=[
        dict(name='敷地権の登記が載る場所', args=dict(
            title='敷地権の登記は、どこに載る？', sub='建物の表題部と土地の権利部（毎日ドリル 第38日 イ・ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「区分建物の表題部」 on the left and 「土地の権利部」 on the right. Draw them large and in different accent colors (blue and orange). Do not draw any check mark or cross mark on this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 区分建物の表題部
Scene: an isometric apartment building model with a record sheet beside it. The sheet's upper section lists three small rows with these exact labels: 土地の表示 | 敷地権の種類と割合 | 原因日付
Result badge: 建物の登記として記録

RIGHT PANEL (orange accent):
Panel header: 土地の権利部
Scene: an isometric land plot with a record sheet beside it. The sheet's lower section, labeled 甲区, carries a round stamp labeled 敷地権である旨. A registrar figure with a stamp stands beside the sheet.
Result badge: 登記官が職権で記録""",
            callout='敷地権の登記は、建物の表題部と、土地の権利部の相当区の二か所に載ります。\n土地側の「敷地権である旨」の登記は、申請ではなく、登記官が職権でします。',
            footer='不動産登記規則118条・119条、不動産登記法46条',
            kanji='敷・地・権・登・記・建・物・表・題・部・原・因・日・付・種・類・割・合・甲・区・官・職'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (区分建物の表題部 on the left and 土地の権利部 on the right) in different accent colors, and that no check mark and no cross mark is drawn, ')),
        dict(name='建物と土地の抵当権が同一かどうか', args=dict(
            title='抵当権が同じ内容かどうかで分かれる', sub='敷地権の登記をするとき（毎日ドリル 第38日 エ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「同一のとき」 on the left and 「同一でないとき」 on the right. Draw them large and in different accent colors (blue and orange). Do not draw any check mark or cross mark on this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 同一のとき
Scene: an apartment building model and a land plot, each with an identical record sheet labeled 抵当権. A single thin horizontal line, not an X shape, is drawn through the land plot's sheet only. A small caption under the scene: 登記の目的、受付、原因日付が同じ
Result badge: 土地の抵当権を職権で抹消

RIGHT PANEL (orange accent):
Panel header: 同一でないとき
Scene: an apartment building model with a record sheet labeled 抵当権, and under the main entry line a small indented sub-line marked with a round stamp labeled 付記.
Result badge: 建物のみに関する旨を付記""",
            callout='建物と土地の抵当権が、登記の目的や受付、原因日付まで同一のときは、土地の抵当権の登記を職権で抹消します。\n同一でないときは、建物の抵当権の登記に「建物のみに関する旨」を付記します。',
            footer='不動産登記規則123条',
            kanji='抵・当・権・建・物・土・地・同・一・登・記・目・的・受・付・原・因・日・職・抹・消'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (同一のとき on the left and 同一でないとき on the right) in different accent colors, and that no check mark and no cross mark is drawn, ')),
    ],
)
