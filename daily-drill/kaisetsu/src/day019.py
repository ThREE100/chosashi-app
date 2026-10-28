D = dict(
    catch='代位できる場合とできない場合',
    intro='債権者代位権と、これを使った登記の申請について、「どんなときに代位できるか」「どんなときにできないか」を問う問題です（民法423条・423条の7）。\n\nこの記事では、買主が売主に代わって登記を申請する場面を中心に、代位の要件を具体例で確認していきましょう。問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('登記名義がAのままなら、買主Cは売主Bの登記請求権を代位できる',
               '登記をしなければ権利の得喪を第三者に対抗できない財産を譲り受けた者は、その譲渡人が第三者に対して有する登記手続を請求する権利を行使しないときは、その権利を行使することができます（民法423条の7）。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地がAからB、BからCへと売られたのに、登記はAのままで、Bが動かないとします。この場合、Cは、Bに代わって、Aに対して「Bへの移転の登記手続をしてください」と請求できます。'),
        'イ': ('土地の全部を買った人は、代位して分筆の登記を申請できない',
               '債権者が代位権を行使できるのは、自己の債権を保全するため必要があるときです（民法423条1項）。\n\n甲土地の全部を買ったBは、分筆をしなくても、そのまま所有権の移転の登記を受けられます。分筆をしなければ守れない権利はありません。保全の必要がないので、Aに代位して分筆の登記を申請することはできません。本肢は誤りです。\n\n**たとえば**、土地一筆を丸ごと買った人が、後で2筆に分けて使いたいと考えたとしても、それはまず所有権の移転の登記を受けてから、自分で分筆すればよいのです。'),
        'ウ': ('土地の一部を買った人は、代位して地積の更正の登記を申請できる',
               '甲土地の一部を買ったBが所有権の移転の登記を受けるには、先に分筆の登記が必要です。分筆のためには、登記記録の地積の錯誤を正す必要があります。Bは、自己の債権を保全するため、売主Aに代位して地積の更正の登記を申請できます（民法423条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、土地の一部を買ったのに、売主の登記記録の面積が実際と違っていて、そのままでは分筆の登記ができないとします。買主は、売主に代わって、面積を直す登記を申請できます。'),
        'エ': ('自分の債権の期限が来ていなければ、原則として代位できない',
               '債権者は、自分の債権の期限が到来しない間は、被代位権利を行使することができません。ただし、保存行為は、この限りでありません（民法423条2項）。\n\n本肢のBの貸金債権は、弁済期が来ていません。売買代金の取立ては保存行為ではないので、Bは代位して取り立てることができません。問題文は「できる」としているので、本肢は誤りです。\n\n**たとえば**、友人にお金を貸したものの返済日がまだ先なのに、その友人が他人に持っている代金を、先回りして取り立てることは認められません。'),
        'オ': ('差押えを禁じられた権利は、代位行使できない',
               '債務者の一身に専属する権利と、差押えを禁じられた権利は、代位行使することができません（民法423条1項ただし書）。\n\n問題文は「差押えを禁じられた権利であっても、代位行使することができる」としているので、本肢は誤りです。\n\n**たとえば**、法律で差押えが禁じられている権利（生活を支えるための給料の一部など）は、債権者がお金を回収するために代位して取り立てることはできません。'),
    },
    summary=[
        ('ア', '正', '登記又は登録をしなければ対抗できない財産の譲受人は、譲渡人の登記手続請求権を代位行使できる'),
        ('イ', '誤', '土地の全部を買った人は、保全の必要がないので、代位して分筆の登記を申請できない'),
        ('ウ', '正', '土地の一部を買った人は、売主に代位して地積の更正の登記を申請できる'),
        ('エ', '誤', '自分の債権の期限が到来しない間は、保存行為を除き、代位行使できない'),
        ('オ', '誤', '差押えを禁じられた権利は、代位行使できない'),
    ],
    summary_tail='イは「全部と一部の違い」、エは「期限未到来」、オは「ただし書の例外」を取り違えた出題です。代位は「保全の必要」と「期限が来ていること」と「行使できる権利であること」の3点を確認しましょう。',
    supplements=[
        '### 補足説明（イ・ウ）：全部を買った人と、一部を買った人\n\n同じ土地の買主でも、買った範囲によって、代位して分筆や地積の更正を申請できるかが変わります。\n\n- 土地の全部を買った人：分筆をしなくても、そのまま所有権の移転の登記を受けられる。保全の必要がないので、代位して分筆は申請できない。\n- 土地の一部を買った人：移転の登記の前に分筆が必要。地積の錯誤があれば、先に地積の更正も必要なので、代位して申請できる。\n\n**たとえば**、1000平方メートルの土地のうち400平方メートルだけを買った人は、その部分を別の土地にする分筆をしないと、移転の登記を受けられません。丸ごと買った人には、その必要がありません。',
        '### 補足説明（エ・オ）：代位行使ができない場合\n\n代位権は、債権者が債務者の権利を代わりに行使する強い手段なので、いくつかの制限があります（民法423条）。\n\n- 債務者の一身に専属する権利、差押えを禁じられた権利：代位できない（1項ただし書）。\n- 自己の債権の期限が到来しない間：保存行為を除き、代位できない（2項）。\n- 自己の債権が強制執行により実現できないもの：代位できない（3項）。\n\n**たとえば**、返済日がまだ先の貸金債権しか持たない人は、債務者が持つ売掛金を取り立てることができません。ただし、時効の完成を防ぐような保存行為なら、期限前でもできます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第19日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、民法423条（1項・2項・3項）と423条の7は、`note-articles/laws/` 配下の原文で確認しました。',
        'イ・ウの「全部を買った人は代位して分筆を申請できず、一部を買った人は代位して地積の更正を申請できる」という結論は、民法423条の要件（保全の必要）に当てはめた一般的な整理です。登記の実務上の取扱いを定めた不動産登記法の条文や通達は確認していません。',
        'オの具体例（給料の一部）は、差押えが禁じられた権利の一般的な例として挙げたもので、差押禁止債権を定める法令の条文は確認していません。エ・オの具体例は条文の文言から導いた一般的な説明です。',
    ],
    phrases=['買主は売主の登記請求権を代位できます', '全部を買った人は分筆を代位できません', '一部を買った人は地積更正を代位できます', '期限が来るまでは代位できません', '差押えが禁じられた権利は代位できません'],
    header=dict(t1='代位できる？', t2='できない？', topic='民法　債権者代位権と登記',
                kanji='代・位・民・法・債・権・者・登・記'),
    poster_intro='債権者代位権と登記の申請を、「登記手続の代位」（グループA：ア・イ・ウ）と「代位できない場合」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='債権者代位と登記を整理', sub='民法第423条と第423条の7（毎日ドリル 第19日）',
        col_a='登記手続の代位', col_b='代位できない場合', n_a=3,
        cards=[
            dict(h='買主は売主の登記請求権を代位できる',
                 ill='three person figures in a row connected by thin arrows, with a house at the far right. An extra long arrow from the right figure curves over the middle figure to the left figure, and a form labeled 「登記手続請求」 sits on that arrow. A green check mark sits beside the long arrow.',
                 words=['登記手続請求'], tag='買主が代わりに請求'),
            dict(h='全部を買った人は分筆を代位できない',
                 ill='an isometric whole land plot with a buyer figure holding a deed document labeled 「所有権移転」. A faded gray dotted split line across the plot is shown unused. A green check mark sits beside the deed document.',
                 words=['所有権移転'], tag='分筆しなくても移転'),
            dict(h='一部を買った人は地積更正も代位できる',
                 ill='an isometric land plot with a split line and a measuring tape along one side. A buyer figure holds a form labeled 「地積更正」 and stands behind a seller figure. A green check mark sits beside the buyer figure.',
                 words=['地積更正'], tag='一部の買主は代位可'),
            dict(h='期限が来ていないと代位できない',
                 ill='a calendar page labeled 「期限前」 in faded gray, and a person figure holding a bill document standing in front of a closed gate. No check mark and no cross mark on this card.',
                 words=['期限前'], tag='自分の債権の期限が先'),
            dict(h='差押えが禁じられた権利は代位できない',
                 ill='a wallet-shaped envelope with a padlock, labeled 「差押禁止」, and a faded gray person figure standing aside holding a bill document. No check mark and no cross mark on this card.',
                 words=['差押禁止'], tag='差押禁止は代位不可'),
        ],
        kanji='登・記・手・続・請・求・買・主・代・位・全・部・分・筆・所・有・権・移・転・地・積・更・正・期・限・前・差・押・禁・止'.split('・')),
    nb_label='イ・ウ・エ・オ肢', nb_intro='イ・ウ・エ・オの補足説明に合わせた2枚です。1枚目は、全部を買った人と一部を買った人の違いを左右の対比で示します。2枚目は、代位行使ができない場合を表で整理します。',
    notebooks=[
        dict(name='全部を買った人と、一部を買った人', args=dict(
            title='代位して申請できるのは、どっち？', sub='土地の全部と一部（毎日ドリル 第19日 イ・ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「一部を買った人」 on the left and 「全部を買った人」 on the right; draw them in different accent colors (blue and orange) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 一部を買った人
Scene: an isometric scene of a land plot with a split line and a buyer figure holding a form labeled 「地積更正」, standing behind a seller figure.
Reason line: 先に分筆が必要
Result badge with a green check mark: 代位して申請できる

RIGHT PANEL (orange accent):
Panel header: 全部を買った人
Scene: an isometric scene of a whole land plot, a buyer figure receiving a deed document labeled 「所有権移転」 directly.
Reason line: 分筆は不要
Result badge with a red cross: 代位して分筆できない""",
            callout='土地の一部を買った人は、移転の登記の前に分筆が必要なので、売主に代位して地積の更正を申請できます。\n土地の全部を買った人は、分筆をしなくても移転の登記を受けられるので、代位して分筆を申請できません。',
            footer='民法423条1項',
            kanji='一・部・全・買・人・分・筆・先・必・要・不・地・積・更・正・所・有・権・移・転・代・位・申・請'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (一部を買った人 on the left and 全部を買った人 on the right) drawn in different accent colors, and that the left panel shows a green check mark while the right panel shows a red cross, ')),
        dict(name='代位行使ができない場合', args=dict(
            title='代位行使ができない場合', sub='民法423条の制限（毎日ドリル 第19日 エ・オ）',
            req='a table',
            layout="""--- TABLE ---
Render as a clean table with 2 columns and 3 data rows, plus a header row. The column headers are exactly: 代位できない場合 / 根拠. Each row has a small isometric icon beside the first cell.
Row 1: first cell 一身専属権と差押えを禁じられた権利 (icon: a padlocked wallet); second cell 1項ただし書.
Row 2: first cell 自分の債権の期限が未到来 (icon: a calendar page); second cell 2項（保存行為を除く）.
Row 3: first cell 強制執行で実現できない債権 (icon: a stop sign shape with a bill document); second cell 3項.
Use exactly these strings, and no others, for the cell text. The three 根拠 cells are different strings; draw each of them in a different accent color (blue, green and orange).""",
            callout='代位は、自分の債権を保全するために必要なときだけ認められます。\n一身専属権や差押えを禁じられた権利、期限が来ていない債権などでは、代位行使はできません。',
            footer='民法423条',
            kanji='代・位・一・身・専・属・差・押・禁・期・限・未・到・来・強・制・執・行・実・現・債・権・保・存・為・根・拠'.split('・'), what='table',
            check='confirm the table has exactly 2 columns and 3 data rows, and confirm the three cells in the 根拠 column are different strings drawn in different accent colors, ')),
    ],
)
