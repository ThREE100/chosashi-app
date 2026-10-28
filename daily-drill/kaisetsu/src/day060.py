D = dict(
    catch='建物の認定、個数、家屋番号、種類',
    intro='建物の認定、建物の個数、家屋番号、建物の種類を問う問題です（不動産登記事務取扱手続準則77条〜80条）。この問題は、**誤っているもの**の組合せを選びます。\n\nこの記事では、何が建物として扱われるか、何個の建物として登記するか、合併したときの家屋番号、用途が複数あるときの種類の書き方を、具体的な場面で確かめていきましょう。',
    sections={
        'ア': ('効用上一体として利用される数棟は、一つの建物として扱う',
               '効用上一体として利用される状態にある数棟の建物は、所有者の意思に反しない限り、1個の建物として取り扱います（不動産登記事務取扱手続準則78条1項）。\n\n問題文の甲建物と乙建物は、2階部分に同一の屋外階段を使うほかに出入りする方法がありません。互いに切り離しては使えない関係なので、効用上一体として利用される状態にあるといえます。本肢は正しいといえます。\n\n**たとえば**、二つの離れた建物の2階が、一本の屋外階段だけでつながっていて、その階段を使わないとどちらの2階にも出入りできない場合、Aさんの意思に反しない限り、1個の建物として扱います。'),
        'イ': ('機械の上の建造物も、基脚や支柱があれば建物になり得る',
               '機械の上に建設した建造物は、建物として取り扱いません。ただし、地上に基脚を有し、又は支柱を施したものは除かれます（不動産登記事務取扱手続準則77条2号イ）。\n\n問題文は「地上に基脚を有するものであっても、建物として取り扱わない」としているので、本肢は誤りです。ただし書を見落とすと、ひっかかります。\n\n**たとえば**、大きな機械の上に建てた小屋でも、その小屋が地面にしっかり基脚で固定されているなら、建物として取り扱われる可能性があります。'),
        'ウ': ('各室に通ずる廊下は、所有者の意思でも別の建物にできない',
               'アパートの各室に通ずる廊下や、階段室、エレベーター室、屋上など、構造上、区分所有者の全員又はその一部の共用に供されるべき部分は、各別に1個の建物として取り扱うことができません（不動産登記事務取扱手続準則78条3項）。\n\n問題文は、Aの意思により、廊下を別の建物として登記できるとしているので、本肢は誤りです。所有者の意思に左右されない場面です。\n\n**たとえば**、一棟の共同住宅の全部を一人で所有していても、各室に通ずる廊下だけを切り出して、別の建物として登記することはできません。'),
        'エ': ('主たる用途が複数のときは、用途を並べて種類を書く',
               '建物の主な用途が二以上の場合は、当該二以上の用途により建物の種類を定めます（不動産登記規則113条2項）。種類は、例えば「居宅・店舗」のように並べて表示します（不動産登記事務取扱手続準則80条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、1階が店舗、2階が事務所、3階が居宅の建物は、種類を「店舗・事務所・居宅」と書きます。用途をまとめる「多目的ビル」のような言い方は使いません。'),
        'オ': ('合併後の家屋番号は、原則として上位のもの',
               '建物の合併の登記をする場合には、合併前の建物の家屋番号のうち上位のものをもって、合併後の家屋番号とします。ただし、上位の家屋番号によることが相当でないと認められる場合には、他の番号を用いても差し支えありません（不動産登記事務取扱手続準則79条9号）。\n\n本肢は正しいといえます。\n\n**たとえば**、家屋番号が5番の1の建物と5番の2の建物を合併するときは、合併後は、上位の5番の1になります。'),
    },
    summary=[
        ('ア', '正', '効用上一体として利用される数棟は、所有者の意思に反しない限り、1個の建物とする'),
        ('イ', '誤', '機械上の建造物でも、地上に基脚を有し、又は支柱を施したものは建物になり得る'),
        ('ウ', '誤', '各室に通ずる廊下など共用部分は、所有者の意思でも、各別の建物にできない'),
        ('エ', '正', '主たる用途が二以上のときは、「店舗・事務所・居宅」のように用途を並べて種類とする'),
        ('オ', '正', '合併後の家屋番号は、原則として、合併前の上位のものとする'),
    ],
    summary_tail='イは「ただし書」、ウは「所有者の意思でも変えられない」点を、見落としやすい出題です。例外の部分を、条文の言葉とあわせて確かめましょう。',
    supplements=[
        '### 補足説明（イ）：機械の上の建造物は、基脚や支柱の有無で分かれる\n\n機械の上にある建造物は、原則として建物ではありません。ただし書で、例外が決まっています（準則77条2号イ）。\n\n| 機械の上の建造物 | 扱い |\n|---|---|\n| 地上に基脚がなく、支柱もない | 建物として取り扱わない |\n| 地上に基脚を有し、又は支柱を施したもの | 建物として取り扱われ得る |\n\n**たとえば**、機械の上に載っているだけの建造物は、建物ではありません。地面に基脚で固定されていれば、その土地に定着している建造物として、建物になり得ます。',
        '### 補足説明（ウ）：所有者の意思で決まる場合、決まらない場合\n\n一棟の建物をどう数えるかは、所有者の意思が関わる場合と、関わらない場合があります（準則78条2項・3項）。\n\n- 構造上区分された、独立して使える各部分：各別に1個の建物とするのが原則。ただし、所有者が同一なら、その意思に反しない限り、全部又は隣接する数個の部分を1個の建物として扱う。\n- 各室に通ずる廊下、階段室、エレベーター室、屋上など、共用に供されるべき部分：所有者の意思でも、各別に1個の建物としては扱えない。\n\n**たとえば**、アパートの全部を一人で持つ所有者が、各部屋をまとめて1個の建物として登記する選択はできます。しかし、共用の廊下だけを、独立した建物にすることはできません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第60日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記事務取扱手続準則77条2号イ・78条1項・3項・79条9号・80条2項、不動産登記規則113条2項は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの「同一の屋外階段を使うほかに出入りの方法がない二棟は、効用上一体として利用される状態にある」という当てはめは、準則78条1項の文言から導いた一般的な整理で、個別の先例・通達の確認はしていません。',
        'エの「多目的ビル」のような包括的な表現は用いないという点は、規則113条2項（二以上の用途により種類を定める）から導いた整理で、個別の先例・通達の原文は未確認です。',
    ],
    phrases=['数棟でも、一体なら一つの建物です', '機械の上でも、基脚があれば建物です', '共用の廊下は、別の建物にできません', '用途が複数なら、並べて種類にします', '合併後は、上位の家屋番号を使います'],
    header=dict(t1='建物かどうか、', t2='何個と数える？', topic='不動産登記法　建物の認定',
                kanji='登・記・毎・建・物・認・定'),
    poster_intro='建物の認定から家屋番号、種類までを、「建物として数える」（グループA：ア・イ・ウ）と「番号と種類の定め方」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の認定から種類までを整理', sub='不動産登記事務取扱手続準則 第77条〜第80条（毎日ドリル 第60日）',
        col_a='建物として数える', col_b='番号と種類', n_a=3,
        cards=[
            dict(h='効用上一体の数棟は一つの建物',
                 ill='two small buildings side by side connected by a single outdoor staircase between their second floors, with a green bracket around both buildings. A green check mark sits beside the bracket.',
                 words=[], tag='一個の建物'),
            dict(h='機械の上でも基脚があれば建物',
                 ill='a large machine with a small hut on top, and a green post-shaped support running from the hut down to the ground. A green check mark sits beside the support.',
                 words=[], tag='基脚は例外'),
            dict(h='共用の廊下は別の建物にできない',
                 ill='an apartment building with a corridor along its side. The corridor is highlighted in gray with a dotted outline and labeled 「共用」, with a hand trying to pull it away but a lock icon holding it in place. No check mark and no cross mark on this card.',
                 words=['共用'], tag='別個にできない'),
            dict(h='用途が複数なら並べて種類にする',
                 ill='a three-story building with a small sign on each floor labeled 「店舗」, 「事務所」 and 「居宅」, and a long banner below the building listing the same three words in a row. A green check mark sits beside the banner.',
                 words=['店舗', '事務所', '居宅'], tag='用途を並べる'),
            dict(h='合併後は上位の家屋番号',
                 ill='two house icons labeled 「五番の一」 and 「五番の二」 merging into one house icon labeled 「五番の一」. A green check mark sits beside the merged house.',
                 words=['五番の一', '五番の二'], tag='上位を使う'),
        ],
        kanji='共・用・店・舗・事・務・所・居・宅・五・番・一・二'.split('・')),
    nb_label='イ・ウ肢', nb_intro='イ・ウの補足説明に合わせた2枚です。1枚目は、機械の上の建造物が建物になる場合とならない場合を左右の対比で示します。2枚目は、所有者の意思で決まる場合と決まらない場合を示します。',
    notebooks=[
        dict(name='機械の上の建造物は、基脚で分かれる', args=dict(
            title='機械の上は、建物？', sub='機械上に建設した建造物（毎日ドリル 第60日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a red cross; the right side shows a green check mark. The two panel headers are different strings: 「基脚も支柱もない」 on the left and 「基脚や支柱がある」 on the right; draw them in different accent colors (gray and green).

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (gray accent):
Panel header: 基脚も支柱もない
Scene: an isometric scene of a large machine with a small hut resting on top of it, with no support reaching the ground.
Result badge with a red cross: 建物として取り扱わない

RIGHT PANEL (green accent):
Panel header: 基脚や支柱がある
Scene: an isometric scene of a large machine with a small hut on top and a post-shaped support running from the hut down to the ground.
Result badge with a green check mark: 建物になり得る""",
            callout='機械の上に建設した建造物は、建物として取り扱いません。\nただし、地上に基脚を有し、又は支柱を施したものは、この例外から除かれます。',
            footer='不動産登記事務取扱手続準則七十七条二号',
            kanji='機・械・建・物・基・脚・支・柱・取・扱・除'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (基脚も支柱もない on the left and 基脚や支柱がある on the right), that the left panel shows a red cross and the right panel shows a green check mark, ')),
        dict(name='所有者の意思で決まる場合、決まらない場合', args=dict(
            title='所有者の意思で、決められる？', sub='一棟の建物の数え方（毎日ドリル 第60日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「各部分」 on the left and 「共用部分」 on the right; draw them in different accent colors (blue and gray).

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 各部分
Scene: an isometric scene of an apartment building with its rooms, and a person figure labeled 所有者 choosing to group the rooms together.
Result badge with a green check mark: 意思に反しない限り一つにできる

RIGHT PANEL (gray accent):
Panel header: 共用部分
Scene: an isometric scene of an apartment building with its corridor and staircase highlighted, and a person figure labeled 所有者 trying to pull the corridor away, but a lock icon holds it in place.
Result badge with a red cross: 別の建物にできない""",
            callout='構造上区分された各部分は、所有者の意思が関わります。\n各室に通ずる廊下や階段室などの共用部分は、所有者の意思でも、各別の建物として扱えません。',
            footer='不動産登記事務取扱手続準則七十八条二項と三項',
            kanji='各・部・分・共・用・所・有・者・意・思・建・物・別・廊・下・階・段'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (各部分 on the left and 共用部分 on the right), that the left panel shows a green check mark and the right panel shows a red cross, ')),
    ],
)
