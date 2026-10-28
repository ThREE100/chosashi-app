D = dict(
    catch='合併の制限、区分合併、分割の承諾',
    intro='建物の合併の登記と、建物の分割の登記を問う問題です（不動産登記法21条・30条・54条・56条、不動産登記規則128条・131条・133条）。合併とは、複数の建物を一つの建物としてまとめる登記、分割とは、附属建物を切り離して別の建物にする登記のことです。\n\nこの記事では、合併できない場合、相続人による申請、区分合併の要件、分割のときの抵当権の消滅、登記識別情報の通知を、具体的な場面で確かめていきましょう。',
    sections={
        'ア': ('所有権の移転の仮登記があると、合併できない',
               '所有権等の登記以外の権利に関する登記がある建物の合併の登記は、することができません（不動産登記法56条5号）。例外として合併できるのは、登記の目的や受付などが同一の担保権の登記と、登記事項が同一の信託の登記だけです（不動産登記規則131条）。\n\n所有権の移転の仮登記は、この例外に入りません。内容が同一でも、合併できないので、本肢は誤りです。\n\n**たとえば**、甲建物と乙建物の両方に、Bさんを権利者とする同じ内容の所有権の移転の仮登記があっても、二つを一つの建物にまとめる合併の登記は、申請できません。'),
        'イ': ('相続人は、相続の登記をしなくても、合併の登記を申請できる',
               '表題部所有者又は所有権の登記名義人について相続があったときは、相続人は、その人が申請できた表示に関する登記を申請することができます（不動産登記法30条）。建物の合併の登記は、表示に関する登記です。\n\n本肢は正しいといえます。相続があったことを証する情報を提供すれば、Aの名義のままで申請できます。\n\n**たとえば**、Aさんが亡くなり、相続人のBさんとCさんが相続の登記をまだしていなくても、二人は、相続を証する情報を添えて、乙建物を甲建物の附属建物にする合併の登記を申請できます。'),
        'ウ': ('区分合併に、効用上一体であることは要件ではない',
               '区分合併とは、区分建物である甲建物を、これと接続する区分建物である乙建物などに合併することです（不動産登記規則133条1項）。ここで定められている要件は、接続する区分建物であることです。効用上一体として利用される状態にあることは、挙げられていません。\n\n問題文は、効用上一体でないから合併できないとしているので、本肢は誤りです。\n\n**たとえば**、隣り合って接続する二つの区分建物の所有者が同じAさんなら、二つが別々の用途で使われていても、法56条の制限に触れない限り、合併の登記を申請できます。'),
        'エ': ('分割のときは、抵当権者の承諾で、抵当権が消えた旨の登記ができる',
               '建物の分割の登記には、法40条（分筆に伴う権利の消滅）の規定が準用されます（不動産登記法54条3項）。\n\n分割の登記の申請情報と併せて、抵当権者が抵当権を消滅させることを承諾したことを証する情報を提供すれば、分割後の建物について抵当権が消えた旨が登記されます（不動産登記規則128条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、Cさんの抵当権がついた甲建物から附属建物を分割して乙建物とするとき、Cさんが乙建物についての抵当権の消滅を承諾した書類を付ければ、乙建物について抵当権が消滅した旨が登記されます。'),
        'オ': ('分割では、登記識別情報は通知されない',
               '登記識別情報が通知されるのは、その登記をすることによって、申請人自らが登記名義人となる場合です（不動産登記法21条）。\n\n建物の分割の登記が完了しても、Aが新たに登記名義人となるわけではありません。分割後の乙建物について、登記識別情報が通知されることはないので、本肢は誤りです。\n\n**たとえば**、新築した建物の所有権の保存の登記を受けた人には、登記識別情報が通知されます。しかし、すでに登記名義人であるAさんが、持っている建物から附属建物を分ける登記をしても、新しく通知を受ける場面ではありません。'),
    },
    summary=[
        ('ア', '誤', '所有権の移転の仮登記がある建物は、内容が同一でも、合併できない'),
        ('イ', '正', '相続人は、相続の登記をしなくても、相続を証する情報を付けて合併の登記を申請できる'),
        ('ウ', '誤', '区分合併に、効用上一体であることは要件でなく、接続する区分建物であればよい'),
        ('エ', '正', '分割の登記に併せて抵当権者の承諾を証する情報を提供すれば、抵当権が消えた旨が登記される'),
        ('オ', '誤', '分割の登記では、申請人が新たに登記名義人にならないので、登記識別情報は通知されない'),
    ],
    summary_tail='アは「例外に入るものの範囲」、ウは別の場面の要件の持ち込み、オは通知される場面の取り違えを誘う出題です。それぞれの条文がどの場面の話かを分けて覚えましょう。',
    supplements=[
        '### 補足説明（ア）：合併できない場合と、その例外\n\n建物の合併の登記ができない場合は、次の五つです（不動産登記法56条）。\n\n- 共用部分である旨の登記がある建物。\n- 表題部所有者又は所有権の登記名義人が、相互に異なる建物。\n- 表題部所有者又は所有権の登記名義人の持分が、相互に異なる建物。\n- 所有権の登記がない建物と、所有権の登記がある建物。\n- 所有権等の登記以外の権利に関する登記がある建物。\n\nただし、最後の場合には例外があります。登記の目的、申請の受付の年月日及び受付番号、登記原因及びその日付が同一の担保権の登記や、登記事項が同一の信託の登記は、合併後の登記記録に登記できるので、あっても合併できます（不動産登記規則131条）。\n\n**たとえば**、両方の建物に、同じ受付で同じ原因の抵当権の登記があるときは合併できます。しかし、所有権の移転の仮登記は、内容が同じでも、この例外に入りません。',
        '### 補足説明（ウ）：「効用上一体」と「接続」は、別の場面の話\n\n似た言葉ですが、条文の場面が違います。\n\n- 効用上一体として利用される状態にある数棟の建物：登記をするときに、何個の建物として数えるかの基準です（準則78条1項）。\n- 接続する区分建物：区分合併ができる場合の要件です（不動産登記規則133条1項）。\n\n**たとえば**、二つの区分建物が、隣り合って接続していれば、日ごろ別々の用途に使っていても、区分合併の要件は満たします。「一体として使っているか」は、区分合併を申請できるかどうかの条件ではありません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第62日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法21条・30条・54条・56条、不動産登記規則128条・131条・133条は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウの「区分合併に効用上一体は要件でない」は、規則133条1項が挙げている要件（接続する区分建物であること）と、準則78条1項が個数の判断の基準であることからの一般的な整理で、個別の先例・通達の確認はしていません。',
        'イの具体例（相続人の申請）、エ・オの具体例は、条文の文言をかみ砕いた一般的な説明です。イで相続を証する情報を提供することは、不動産登記令7条1項4号によるものですが、令の原文は今回は確認していません。',
    ],
    phrases=['仮登記があれば、合併できません', '相続人は、名義のままで合併を申請できます', '区分合併は、接続していればよいんです', '分割は、抵当権者の承諾で権利を消せます', '分割では、登記識別情報は通知されません'],
    header=dict(t1='合併できる？', t2='分割したらどうなる？', topic='不動産登記法　建物の合併と分割',
                kanji='登・記・毎・建・物・合・併・分・割'),
    poster_intro='建物の合併と分割を、「合併の登記」（グループA：ア・イ・ウ）と「分割の登記」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の合併と分割を整理', sub='不動産登記法 第54条・第56条（毎日ドリル 第62日）',
        col_a='合併の登記', col_b='分割の登記', n_a=3,
        cards=[
            dict(h='仮登記があれば合併できない',
                 ill='two house icons side by side, each with a small tag labeled 「仮登記」, and a dotted bracket trying to join them but a lock icon holding the bracket apart. No check mark and no cross mark on this card.',
                 words=['仮登記'], tag='合併の制限'),
            dict(h='相続人は相続の登記なしで申請',
                 ill='two heir figures at a counter holding a form and a paper labeled 「相続証明」, with a faded gray house icon in the background. A green check mark sits beside the heirs.',
                 words=['相続証明'], tag='名義のままで申請'),
            dict(h='区分合併は接続していればよい',
                 ill='two adjoining condominium rooms sharing one wall, with a green bracket around both rooms labeled 「接続」. A green check mark sits beside the bracket.',
                 words=['接続'], tag='要件は接続'),
            dict(h='分割は抵当権者の承諾で権利を消せる',
                 ill='a house on the left splitting off a small annex on the right, with a consent paper labeled 「承諾」 held by a lender figure. A green check mark sits beside the paper.',
                 words=['承諾'], tag='承諾で消える'),
            dict(h='分割では識別情報は通知されない',
                 ill='a house icon split into two with an owner figure standing in front of them, and a letter in an envelope drawn faded in gray at the side. No check mark and no cross mark on this card.',
                 words=[], tag='通知なし'),
        ],
        kanji='仮・登・記・相・続・証・明・接・続・承・諾'.split('・')),
    nb_label='ア・ウ肢', nb_intro='ア・ウの補足説明に合わせた2枚です。1枚目は、合併できない場合の仕分けを示します。2枚目は、効用上一体と接続の違いを、左右の対比で示します。',
    notebooks=[
        dict(name='合併できる権利の登記、できない権利の登記', args=dict(
            title='権利の登記があると、合併は？', sub='建物の合併の制限と例外（毎日ドリル 第62日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「合併できる」 on the left and 「合併できない」 on the right; draw them in different accent colors (green and gray).

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (green accent):
Panel header: 合併できる
Scene: an isometric scene with two stacked items, each with a house icon: 同一の担保権の登記 and 同一の信託の登記.
Result badge with a green check mark: 規則の例外

RIGHT PANEL (gray accent):
Panel header: 合併できない
Scene: an isometric scene with one item, a house icon with a tag: 所有権の移転の仮登記.
Result badge with a red cross: 内容が同一でも不可""",
            callout='権利に関する登記がある建物の合併は、できません。\n例外は、同一の担保権の登記と、登記事項が同一の信託の登記で、仮登記は例外に入りません。',
            footer='不動産登記法五十六条五号、不動産登記規則百三十一条',
            kanji='合・併・担・保・権・信・託・同・一・仮・登・記・例・外'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (合併できる on the left and 合併できない on the right), that the left panel shows a green check mark and the right panel shows a red cross, ')),
        dict(name='効用上一体と接続の違い', args=dict(
            title='「一体」と「接続」の違い', sub='個数の判断と区分合併（毎日ドリル 第62日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「効用上一体」 on the left and 「接続」 on the right. Draw them in different accent colors (blue and green). The two panels answer different questions, so each carries its own question line.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 効用上一体
Question line: 何個の建物と数える？
Scene: an isometric scene of two small buildings used together as one set.
Result badge with a green check mark: 個数の判断の基準

RIGHT PANEL (green accent):
Panel header: 接続
Question line: 区分合併ができる？
Scene: an isometric scene of two adjoining condominium rooms sharing one wall.
Result badge with a green check mark: 区分合併の要件""",
            callout='効用上一体として利用されているかどうかは、何個の建物として数えるかの基準です。\n区分合併の要件は、接続する区分建物であることで、一体として使っているかどうかではありません。',
            footer='不動産登記事務取扱手続準則七十八条一項、不動産登記規則百三十三条一項',
            kanji='効・用・上・一・体・接・続・区・分・合・併・個・数・建・物'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (効用上一体 on the left and 接続 on the right) and each panel carries its own question line, ')),
    ],
)
