D = dict(
    catch='分筆の地番、申請人、権利の消滅の承諾',
    intro='土地の分筆の登記を問う問題です。分筆とは、一筆の土地を複数の土地に分ける登記のことです（不動産登記法39条・40条、不動産登記事務取扱手続準則67条・72条）。\n\nこの記事では、分筆後の地番の付け方、分筆を申請できる人、地積の差があっても更正が要らない場合、抵当権を消すときの承諾、地積測量図の便宜省略を、具体的な場面で確かめていきましょう。',
    sections={
        'ア': ('支号のある土地を分筆するときは、最終の支号の次から付ける',
               '本番（支号のない元の番号）に支号のある土地を分筆する場合、その一筆には従来の地番を残し、他の各筆には、本番の最終の支号に続けて順に支号を付けます（不動産登記事務取扱手続準則67条1項4号ただし書）。\n\n本肢は正しいといえます。5番からは5番1から5番6までが分筆されているので、最終の支号は6です。5番3を3筆に分けると、1筆は5番3のまま、あとの2筆は5番7と5番8になります。\n\n**たとえば**、5番3の土地を三つに分けるとき、5番3の1や5番3の2のように、支号に支号を付けることはしません。'),
        'イ': ('分筆を申請できるのは、登記名義人だけ',
               '分筆の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができません（不動産登記法39条1項）。\n\n問題文のBは、甲土地を買い受けましたが、所有権の移転の登記がまだされていません。登記名義人ではないBが、所有権を取得したことを示す書類を付けても、自分で申請人になることはできないので、本肢は誤りです。\n\n**たとえば**、売買契約をして代金を払ったBさんでも、登記記録の名義がまだAさんのままなら、Bさん自身の名前で分筆の登記を申請することはできません。'),
        'ウ': ('分筆前後の地積の差が誤差の限度内なら、更正は要らない',
               '分筆の登記を申請する場合に、分筆前の地積と分筆後の地積の差が、分筆前の地積を基準にして地積測量図の誤差の限度内であるときは、地積に関する更正の登記の申請は要りません（不動産登記事務取扱手続準則72条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、登記記録では300.00平方メートルだった土地を測って分筆したら、分けた後の合計が300.50平方メートルになったとします。この差が誤差の限度内なら、別に更正の登記を申請しなくてかまいません。'),
        'エ': ('転抵当があるときは、転抵当権者の承諾も必要',
               '分筆の際に抵当権が消えた旨を登記してもらうには、抵当権者の承諾を証する情報を、分筆の登記の申請情報と併せて提供します。その抵当権を目的とする第三者の権利の登記があるときは、その第三者が承諾したことを証する情報も、併せて提供しなければなりません（不動産登記法40条）。\n\n問題文は、転抵当権者Dの承諾がなくてもよいとしているので、本肢は誤りです。\n\n**たとえば**、Cの抵当権にDの転抵当がついているときは、乙土地の抵当権を消すには、CとDの両方の承諾が必要です。'),
        'オ': ('地積は、便宜省略できない',
               '分筆前の土地が広大で、分筆後の土地の一方がわずかであるなど、特別の事情があるときは、分筆後の土地のうち一筆について、地積測量図に記録する事項の一部を便宜省略して差し支えありません。ただし、省略できないのは地積です（不動産登記事務取扱手続準則72条2項かっこ書）。\n\n問題文は「地積を含めて省略して差し支えない」としているので、本肢は誤りです。\n\n**たとえば**、広い甲土地から、ごく小さい乙土地を分けるときでも、省略できる事項の中に地積は入りません。'),
    },
    summary=[
        ('ア', '正', '支号のある土地の分筆は、一筆に従来の地番を残し、他は最終の支号の次から付ける'),
        ('イ', '誤', '分筆を申請できるのは登記名義人だけで、移転の登記を受けていない買主は申請できない'),
        ('ウ', '正', '分筆前後の地積の差が誤差の限度内なら、地積の更正の登記は要らない'),
        ('エ', '誤', '転抵当があるときは、転抵当権者の承諾を証する情報も併せて提供する'),
        ('オ', '誤', '地積測量図の記録事項のうち、地積は便宜省略できない'),
    ],
    summary_tail='エは「承諾が必要な人」、オは「省略できない事項」のかっこ書きを外した出題です。例外やかっこ書きにこそ、問われる点があります。',
    supplements=[
        '### 補足説明（ア）：分筆後の地番の付け方\n\n分筆後の地番は、分けられる土地の地番に支号があるかどうかで、付け方が変わります（準則67条1項4号）。\n\n| 分筆する土地 | 分筆後の地番 |\n|---|---|\n| 支号のない土地（例：5番） | 分筆前の地番に支号を付ける（5番1、5番2…） |\n| 支号のある土地（例：5番3） | 一筆は従来の地番（5番3）、他は本番の最終の支号の次から（5番7、5番8…） |\n\n**たとえば**、5番からすでに5番1から5番6までが分筆されているなら、最終の支号は6です。5番3を分けるときは、新しい土地に5番7、5番8を付けます。5番3の1のような、支号の支号は使いません。',
        '### 補足説明（エ）：権利を消すには、関係する人の承諾がそろう必要がある\n\n分筆に伴って、抵当権を一方の土地から消す登記をしてもらうには、承諾が必要です（不動産登記法40条）。\n\n- 抵当権者の承諾：必要です。\n- その抵当権を目的とする第三者（転抵当権者など）がいるとき：その第三者の承諾も必要です。\n\n**たとえば**、Cが抵当権者で、その抵当権にDの転抵当がついている場合、乙土地の抵当権を消す登記を求めるなら、CとDの両方が承諾したことを証する情報をそろえます。Cの承諾だけでは足りません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第58日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法39条1項・40条、不動産登記事務取扱手続準則67条1項4号・72条は、`note-articles/laws/` 配下の原文で確認しました。',
        '具体例（買主が申請人になれない場面、転抵当の場面、広い土地から小さい土地を分ける場面）は、条文の文言をかみ砕いた一般的な説明で、個別の先例・通達の確認はしていません。',
        'ウの「誤差の限度」の具体的な数値（不動産登記規則77条5項と10条4項の表）は、この記事では扱っていません。設例が「限度内であるとき」と明示している前提で説明しています。',
    ],
    phrases=['支号のある土地は、最終の支号の次から付けます', '分筆を申請できるのは、登記名義人だけです', '誤差の限度内なら、更正は要りません', '転抵当権者の承諾も、必要なんです', '地積は、省略できません'],
    header=dict(t1='分筆の登記、', t2='地番はどうなる？', topic='不動産登記法　土地の分筆',
                kanji='登・記・毎・分・筆・土・地'),
    poster_intro='土地の分筆の登記を、「分筆の準備と手続」（グループA：ア・イ・ウ）と「権利と図面」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='土地の分筆の登記を整理', sub='不動産登記法 第39条・第40条（毎日ドリル 第58日）',
        col_a='分筆の準備と手続', col_b='権利と図面', n_a=3,
        cards=[
            dict(h='支号のある土地は最終の支号の次から',
                 ill='a land plot labeled 「五番三」 on the left that splits into three plots on the right labeled 「五番三」, 「五番七」 and 「五番八」. A green check mark sits beside the three plots.',
                 words=['五番三', '五番七', '五番八'], tag='従来の地番を残す'),
            dict(h='申請できるのは登記名義人だけ',
                 ill='an owner figure at a counter holding a form, highlighted with a green glow and carrying a name tag labeled 「名義人」. A faded gray buyer figure with a contract paper stands aside at the back. A green check mark sits beside the owner.',
                 words=['名義人'], tag='申請人は限定'),
            dict(h='誤差の限度内なら更正は不要',
                 ill='a land plot splitting into two plots, with a measuring tape along the edge and a small scale icon beside it. A green bracket labeled 「限度内」 sits over the scale. A green check mark sits beside the bracket.',
                 words=['限度内'], tag='更正は要らない'),
            dict(h='転抵当があれば承諾も必要',
                 ill='two stacked house icons: the upper one labeled 「転抵当」 and the lower one labeled 「抵当権」, with two hands signing two consent papers, one for each house. A green check mark sits beside each paper.',
                 words=['転抵当', '抵当権'], tag='二人の承諾'),
            dict(h='地積は便宜省略できない',
                 ill='a survey drawing sheet with several lines of entries, one entry line highlighted with a green glow and labeled 「地積」, while the other lines are drawn in faded gray. A green check mark sits beside the highlighted line.',
                 words=['地積'], tag='地積は記録する'),
        ],
        kanji='五・番・三・七・八・名・義・人・限・度・内・転・抵・当・権・地・積'.split('・')),
    nb_label='ア・エ肢', nb_intro='ア・エの補足説明に合わせた2枚です。1枚目は、分筆後の地番の付け方を左右の対比で示します。2枚目は、抵当権を消すために必要な承諾を、重なりの図で示します。',
    notebooks=[
        dict(name='分筆後の地番の付け方', args=dict(
            title='分筆後の地番は、どう付く？', sub='支号のない土地と、支号のある土地（毎日ドリル 第58日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「支号のない土地」 on the left and 「支号のある土地」 on the right. Draw them in different accent colors (blue and green). The two panels show different results, so write each result exactly as given.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 支号のない土地
Scene: a land plot labeled 五番 splitting into two plots labeled 五番一 and 五番二.
Result badge with a green check mark: 支号を付ける

RIGHT PANEL (green accent):
Panel header: 支号のある土地
Scene: a land plot labeled 五番三 splitting into three plots labeled 五番三, 五番七 and 五番八. Beneath the scene, a small note: 五番の最終の支号は六
Result badge with a green check mark: 従来の地番を残して最終の支号の次から""",
            callout='支号のある土地を分けるときは、一筆に従来の地番を残し、他の各筆には、本番の最終の支号の次から順に付けます。\n支号の支号は使いません。',
            footer='不動産登記事務取扱手続準則六十七条一項',
            kanji='支・号・土・地・五・番・三・七・八・最・終・従・来・分・付・残'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (支号のない土地 on the left and 支号のある土地 on the right) and that the right panel shows exactly the three plots 五番三, 五番七 and 五番八, ')),
        dict(name='抵当権を消すために必要な承諾', args=dict(
            title='抵当権を消すには、だれの承諾？', sub='分筆に伴う権利の消滅（毎日ドリル 第58日 エ）',
            req='a layered diagram',
            layout="""--- LAYERED DIAGRAM ---
Render as a clean flat-design vertical diagram with two stacked rows connected by a small downward arrow.
Row 1 (blue accent), a house icon labeled 乙土地 with a ribbon labeled 抵当権, and a person figure labeled 抵当権者 signing a paper labeled 承諾. A green check mark sits beside the paper.
Row 2 (orange accent), the same house icon with a second smaller ribbon labeled 転抵当, and a person figure labeled 転抵当権者 signing a paper labeled 承諾. A green check mark sits beside the paper.
Beneath both rows, a result badge with a green check mark: 二つの承諾がそろって、抵当権が消えた旨の登記
Use exactly these strings, and no others.""",
            callout='抵当権を消す登記には、抵当権者の承諾が要ります。\nその抵当権に転抵当がついているときは、転抵当権者の承諾も、併せて提供しなければなりません。',
            footer='不動産登記法四十条',
            kanji='抵・当・権・者・土・地・承・諾・転・消・登・記'.split('・'), what='rows',
            check='confirm there are exactly two rows, each with exactly one signing figure and a green check mark, ')),
    ],
)
