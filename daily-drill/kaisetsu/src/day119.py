D = dict(
    catch='建物かどうか、1個かどうか、何番か',
    intro='建物の登記では、まず「それは登記上の建物か」「何個の建物として数えるか」「家屋番号は何番か」が問題になります。この問題は、その判断の基準を定めた不動産登記事務取扱手続準則77条〜79条から出題されています。\n\nこの問題は、正しい肢の組合せを選ぶ形式です。ただし書きや条件に注目して、一つずつ確かめていきましょう。',
    sections={
        'ア': ('乗降場は、上屋のある部分だけが建物',
               '停車場の乗降場又は荷物積卸場は、上屋を有する部分に限り、建物として取り扱います（不動産登記事務取扱手続準則77条1号ア）。\n\n問題文は、上屋を有しない部分を含めて、その全体を建物として取り扱うとしているので、本肢は誤りです。\n\n**たとえば**、駅のホームのうち、屋根（上屋）がかかっている部分だけが建物の扱いになります。屋根のない部分は、建物には当たりません。'),
        'イ': ('機械上の建造物も、基脚があれば建物となり得る',
               '機械上に建設した建造物は、建物として取り扱わないものの例とされています。ただし、地上に基脚を有し、又は支柱を施したものは、除かれます（不動産登記事務取扱手続準則77条2号イ）。\n\n本肢は正しいといえます。地上に基脚を有するものは、「建物として取り扱わないもの」から除かれるので、建物として取り扱われ得ます。\n\n**たとえば**、機械の上に組み立てた建造物でも、地面にしっかりと基礎（基脚）を据えて支えているなら、建物として登記される余地があります。'),
        'ウ': ('効用上一体の建物を1個とするのは、所有者の意思に反しないとき',
               '効用上一体として利用される状態にある数棟の建物は、所有者の意思に反しない限り、1個の建物として取り扱います（不動産登記事務取扱手続準則78条1項）。\n\n問題文は、Aが別個の建物として登記することを希望している場合でも、1個の建物として取り扱わなければならないとしているので、本肢は誤りです。\n\n**たとえば**、居宅と物置を持つAが「物置は別の建物として登記したい」と望んでいるなら、所有者の意思に反するので、物置を居宅と1個の建物として扱うことはしません。別個の建物として登記できます。'),
        'エ': ('アパートの廊下だけを、1個の建物にはできない',
               '数個の専有部分に通ずる廊下（例えば、アパートの各室に通ずる廊下）、階段室、エレベーター室、屋上など、構造上区分所有者の全員又はその一部の共用に供されるべき建物の部分は、各別に1個の建物として取り扱うことができません（不動産登記事務取扱手続準則78条3項）。\n\n本肢は正しいといえます。\n\n**たとえば**、各室が区分建物として登記されているアパートで、各室に通ずる廊下だけを切り取って、それを一つの建物として登記することはできません。'),
        'オ': ('二つの土地にまたがる建物の家屋番号は、床面積の多い土地の地番',
               '2筆以上の土地にまたがって1個の建物が存する場合の家屋番号は、附属建物がないときは、床面積の多い部分の存する敷地の地番と同一の番号で定めます（不動産登記事務取扱手続準則79条3号）。\n\n問題文は、地番の若い5番と同一の番号とするとしているので、本肢は誤りです。基準は地番の若さではなく、床面積の多い部分です。\n\n**たとえば**、5番と6番の土地にまたがる建物で、附属建物がなく、床面積の多い部分が6番の上にあるなら、家屋番号は6番です。'),
    },
    summary=[
        ('ア', '誤', '停車場の乗降場又は荷物積卸場は、上屋を有する部分に限り建物として取り扱う'),
        ('イ', '正', '機械上に建設した建造物でも、地上に基脚を有し、又は支柱を施したものは、建物として取り扱われ得る'),
        ('ウ', '誤', '効用上一体の数棟の建物を1個とするのは、所有者の意思に反しない限りである。別個の登記の希望があれば別個にできる'),
        ('エ', '正', '数個の専有部分に通ずる廊下は、各別に1個の建物として取り扱うことができない'),
        ('オ', '誤', '二つの土地にまたがる建物の家屋番号は、地番の若さではなく、床面積の多い部分の存する敷地の地番で定める'),
    ],
    summary_tail='アは「上屋のある部分に限る」、ウは「所有者の意思に反しない限り」、オは「床面積の多い部分」という限定・条件・基準を外した出題です。建物の登記では、ただし書きと条件が点数の分かれ目になります。',
    supplements=[
        '### 補足説明（ウ）：数棟の建物を1個として扱うかは、所有者の意思しだい\n\n効用上一体として利用される数棟の建物は、1個の建物（主である建物と附属建物）として取り扱うのが基本です。ただし、「所有者の意思に反しない限り」という条件が付いています（不動産登記事務取扱手続準則78条1項）。\n\n- 所有者が反対していないとき：1個の建物として取り扱う。\n- 所有者が別個の登記を希望しているとき：別個の建物として登記できる。\n\n**たとえば**、居宅と物置がある場合、所有者が「物置も居宅と一緒に登記したい」と望めば、物置は居宅の附属建物になります。「物置は別の建物として登記したい」と望めば、別個の建物として登記できます。',
        '### 補足説明（オ）：建物が二つの土地にまたがるときの家屋番号\n\n1個の建物が2筆以上の土地にまたがって存するときの家屋番号は、次のように決まります（不動産登記事務取扱手続準則79条3号）。\n\n- 附属建物がある場合：主たる建物の存する敷地の地番と同一の番号。\n- 附属建物がない場合：床面積の多い部分の存する敷地の地番と同一の番号。\n- 主たる建物が2筆以上にまたがる場合：その主たる建物の床面積の多い部分の存する敷地の地番と同一の番号。\n\n地番の若い方が基準になるわけではありません。\n\n**たとえば**、5番と6番の土地にまたがり、附属建物のない建物で、床面積の多い部分が6番の上にあれば、家屋番号は6番です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第119日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記事務取扱手続準則77条1号ア・2号イ、78条1項・3項、79条3号は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの「屋根のない部分は建物に当たらない」、イの「地面に基礎を据えて支えているなら建物として登記される余地がある」は、準則の文言からの一般的な整理で、個別の先例は確認していません。',
        '具体例（駅のホーム、機械の上の建造物、居宅と物置、アパートの廊下、5番と6番にまたがる建物）は、条文の文言を日常の場面に置き換えた仮の設定です。',
    ],
    phrases=['乗降場は上屋のある部分だけが建物です', '機械上の建造物も基脚があれば建物のことも', '物置を別の建物にするかは所有者しだい', 'アパートの廊下だけでは建物になりません', '家屋番号は床面積の多い土地の地番です'],
    header=dict(t1='建物かどうか、', t2='何番になる？', topic='不動産登記　建物の認定',
                kanji='建・物・認・定・登・記・番・毎'),
    poster_intro='建物の認定・個数・家屋番号を、「建物の認定と個数」（グループA：ア・イ・ウ）と「共用部分と家屋番号」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の認定と家屋番号を整理', sub='不動産登記事務取扱手続準則 第77条〜第79条（毎日ドリル 第119日）',
        col_a='建物の認定と個数', col_b='共用部分と家屋番号', n_a=3,
        cards=[
            dict(h='乗降場は上屋のある部分が建物',
                 ill='an isometric train platform. The roofed section of the platform is highlighted in green with a small label on the roof reading 「上屋」, and the open section without a roof is drawn in gray. A green check mark sits beside the roofed section.',
                 words=['上屋'], tag='上屋のある部分に限る'),
            dict(h='機械上の建造物も基脚なら建物',
                 ill='an isometric machine with a small structure built on top of it, and a separate sturdy structure standing on the ground with a visible foundation block labeled 「基脚」. A green check mark sits beside the grounded structure.',
                 words=['基脚'], tag='基脚があれば建物となり得る'),
            dict(h='効用上一体の建物は意思次第',
                 ill='an isometric house and a storage shed on one plot, linked by a thin path. An owner figure carrying a name tag labeled 「所有者の意思」 stands between them. A green check mark sits beside the owner.',
                 words=['所有者の意思'], tag='意思に反しなければ1個'),
            dict(h='アパートの廊下は建物にならない',
                 ill='an isometric apartment building with several doors opening onto a shared corridor, the corridor outlined in a dashed line and labeled 「廊下」. A green check mark sits beside the building as a whole.',
                 words=['廊下'], tag='共用部分は別個にならない'),
            dict(h='家屋番号は床面積の多い土地の地番',
                 ill='a building straddling two adjacent land plots labeled 「5番」 on the left and 「6番」 on the right. The larger part of the building lies on the right plot, which is highlighted in green. A green check mark sits beside the right plot.',
                 words=['5番', '6番'], tag='床面積の多い方の地番'),
        ],
        kanji='上・屋・基・脚・所・有・者・意・思・廊・下・番'.split('・')),
    nb_label='ウ・オ肢', nb_intro='ウ・オの補足説明に合わせた2枚です。1枚目は、数棟の建物を1個として扱うかが所有者の意思で変わることを左右の対比で示します。2枚目は、二つの土地にまたがる建物の家屋番号の決まり方を表で示します。',
    notebooks=[
        dict(name='数棟の建物を1個とするか、別個とするか', args=dict(
            title='効用上一体の建物は、1個か別個か', sub='所有者の意思しだい（毎日ドリル 第119日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「反対がないとき」 on the left and 「別個の登記を希望するとき」 on the right. Draw them in different accent colors (blue and green) so they can never be confused or duplicated. Do not draw any check mark or cross mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 反対がないとき
Scene: an isometric scene of a house and a storage shed on one plot enclosed by one outline, with an owner figure nodding.
Result badge: 1個の建物として取り扱う

RIGHT PANEL (green accent):
Panel header: 別個の登記を希望するとき
Scene: an isometric scene of the same house and storage shed each enclosed by its own outline, with an owner figure holding a form.
Result badge: 別個の建物として登記できる""",
            callout='効用上一体として利用される数棟の建物を1個の建物として取り扱うのは、所有者の意思に反しない限りです。\n所有者が別個の登記を希望すれば、別個の建物として登記できます。',
            footer='不動産登記事務取扱手続準則78条1項',
            kanji='反・対・別・個・登・記・希・望・建・物・取・扱・所・有・者'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (反対がないとき on the left and 別個の登記を希望するとき on the right) drawn in different accent colors, and that no check mark or cross mark appears, ')),
        dict(name='二つの土地にまたがる建物の家屋番号', args=dict(
            title='またがる建物の家屋番号は、何番？', sub='家屋番号の定め方（毎日ドリル 第119日 オ）',
            req='a three-row table',
            layout="""--- TABLE ---
Render as a clean flat-design table with three data rows and two columns, with a header row. Header row: 場合 | 家屋番号の基準.
Row 1 (blue accent): left cell with the label 附属建物がある; right cell with the label 主たる建物の存する敷地の地番.
Row 2 (green accent): left cell with the label 附属建物がない; right cell with the label 床面積の多い部分の存する敷地の地番.
Row 3 (orange accent): left cell with the label 主たる建物が二つの土地にまたがる; right cell with the label 主たる建物の床面積の多い部分の存する敷地の地番.
Add a small illustration under the table: a building straddling a plot labeled 5番 and a plot labeled 6番, with the larger part on 6番 and a tag 家屋番号 6番.
Use exactly these strings, and no others. The three right cells are different strings; draw them in different accent colors.""",
            callout='家屋番号の基準は、地番の若さではありません。\n附属建物がなければ、床面積の多い部分の存する敷地の地番と同じ番号になります。',
            footer='不動産登記事務取扱手続準則79条3号',
            kanji='場・合・家・屋・番・号・基・準・附・属・建・物・存・敷・地・床・面・積・多・部・分・主'.split('・'), what='table',
            check='confirm there are exactly three data rows and that the three right cells are different strings in different accent colors, ')),
    ],
)
