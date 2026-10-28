D = dict(
    catch='家屋番号は、敷地の地番をもとに決まる',
    intro='建物の家屋番号の定め方と、建物の所在の記録のしかたを問う問題です（不動産登記規則112条、不動産登記事務取扱手続準則79条・88条）。この問題は「誤っているもの」を選びます。\n\nこの記事では、一筆の土地に建物が複数あるとき、建物が二筆以上にまたがるとき、あとから同じ敷地に建物を建てるときの家屋番号と、所在の書き方を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('一筆に二個の建物があれば、地番に支号を付ける',
               '家屋番号は、地番区域ごとに、建物の敷地の地番と同じ番号で定めるのが原則です。ただし、二個以上の建物が一筆の土地の上に存するときは、敷地の地番と同一の番号に支号を付けて定めます（不動産登記規則112条1項）。\n\n地番が「6番1」であれば、「6番1の1」「6番1の2」の例により定めます（準則79条2号）。本肢は正しいといえます。\n\n**たとえば**、6番1の土地の上に母屋と別棟の2個の建物が建っていて、それぞれ表題登記をするとします。家屋番号は、母屋が「6番1の1」、別棟が「6番1の2」のように定めます。'),
        'イ': ('二筆にまたがる建物は、床面積の多い部分の敷地の地番で決める',
               '二筆以上の土地にまたがって一個の建物が存するときは、附属建物がない場合、床面積の多い部分の存する敷地の地番と同一の番号で定めます（準則79条3号）。\n\n問題文は「地番の若い5番と同一の番号」としていますが、決め手は地番の若さではありません。床面積の多い部分は6番の土地にあるので、家屋番号は「6番」です。本肢は誤りです。\n\n**たとえば**、5番と6番の土地にまたがる建物が建っていて、床面積の多い部分が6番の側にあれば、家屋番号は「6番」になります。5番の側が小さいなら、5番は選びません。'),
        'ウ': ('連続する地番は、「ないし」で略記できる',
               '建物の所在を記録するとき、原則として、「6番地、4番地、8番地」のように記録します。「6、4、8番地」のように略記してはいけません（準則88条3項本文）。\n\nただし、連続する地番（支号のあるものを除く。）があるときは、「5番地ないし7番地」のように略記してかまいません（同項ただし書）。5番地、6番地、7番地は連続しているので、本肢は正しいといえます。\n\n**たとえば**、5番、6番、7番の三筆にまたがる大きな倉庫の所在は、「5番地ないし7番地」とまとめて書けます。一方、「5番1」「5番2」のように支号がある地番は、この方法で略記できません。'),
        'エ': ('あとから建てた建物は「8番の2」。既存の建物は変えなくてよい',
               '家屋番号が敷地の地番と同一の建物がある敷地に、他の建物を登記するときは、あとの建物に「2、3」の支号を付けて定めます。この場合、最初に登記された建物の家屋番号は、必ずしも変更する必要がありません（準則79条7号）。\n\n問題文は「既に登記されている建物の家屋番号を『8番の1』に変更しなければならない」としているので、本肢は誤りです。\n\n**たとえば**、8番の土地に、家屋番号「8番」の建物がすでにあります。同じ敷地にAさんが新しく建物を建てたときは、新しい建物の家屋番号を「8番の2」とします。既存の「8番」はそのままでかまいません。'),
        'オ': ('二筆にまたがる建物の所在は、床面積の多い地番を先に書く',
               '二筆以上の土地にまたがる建物の所在を記録するときは、床面積の多い部分又は主である建物の所在する土地の地番を先に記録し、他の土地の地番を後に記録します（準則88条2項）。本肢は正しいといえます。\n\n**たとえば**、5番と3番の土地にまたがる建物で、床面積の多い部分が3番の土地にあるときは、表題部の所在には「3番地、5番地」と書きます。地番の小さい順や、並び順ではなく、床面積が決め手です。'),
    },
    summary=[
        ('ア', '正', '一筆の土地に二個以上の建物があるときは、地番に支号を付けて定める'),
        ('イ', '誤', '二筆にまたがる建物の家屋番号は、地番の若い方ではなく、床面積の多い部分の地番で定める'),
        ('ウ', '正', '支号のない連続する地番は、「5番地ないし7番地」のように略記できる'),
        ('エ', '誤', '同じ敷地にあとから建てた建物は「8番の2」とし、既存の家屋番号を変える必要はない'),
        ('オ', '正', '二筆にまたがる建物の所在は、床面積の多い部分の地番を先に記録する'),
    ],
    summary_tail='イは「床面積の多い部分」を「地番の若い方」にすり替え、エは「最初の建物の家屋番号を変更しなければならない」とした出題です。家屋番号も所在の順序も、床面積と敷地の地番で決まります。',
    supplements=[
        '### 補足説明（イ・オ）：二筆にまたがる建物の家屋番号と所在\n\n二筆以上の土地にまたがる建物は、家屋番号と所在の書き方で、決め手が同じです。\n\n| 場面 | 決め方 |\n|---|---|\n| 家屋番号（附属建物なし） | 床面積の多い部分の存する敷地の地番と同一（準則79条3号） |\n| 家屋番号（附属建物あり） | 主である建物の存する敷地の地番と同一（同号） |\n| 所在の記録の順序 | 床面積の多い部分又は主である建物の所在する土地の地番を先に記録する（準則88条2項） |\n\n**たとえば**、5番と6番にまたがる建物で、床面積の多い部分が6番の側にあれば、家屋番号は「6番」、所在は「6番地、5番地」と書きます。',
        '### 補足説明（ア・エ）：同じ敷地に建物が複数あるとき\n\n同じ敷地の上に建物が複数あるときの家屋番号の決め方は、次のとおりです。\n\n| 場面 | 家屋番号 |\n|---|---|\n| 一筆の土地の上に一個の建物 | 敷地の地番と同一（準則79条1号） |\n| 同時に二個以上の建物 | 敷地の地番に1、2、3の支号を付ける。「5番の1」「5番の2」など（同条2号） |\n| 家屋番号が敷地の地番と同一の建物の敷地に、あとから他の建物 | あとの建物に2、3の支号を付ける。最初の建物の家屋番号は変更しなくてよい（同条7号） |\n\n**たとえば**、5番の土地に最初の建物が1個だけのときの家屋番号は「5番」、同時に2個の建物を登記するときは「5番の1」「5番の2」、あとから建てた建物は「5番の2」と区別して覚えておきましょう。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第42日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則112条1項、不動産登記事務取扱手続準則79条（1号・2号・3号・7号）、88条2項・3項は、`note-articles/laws/` 配下の原文で確認しました。',
        '各肢の具体例（6番1の2棟、5番と6番にまたがる建物、5番から7番までの倉庫、8番にあとから建てた建物）は、条文の文言をかみ砕いた一般的な説明で、個別の先例・通達の確認はしていません。',
        '補足説明（ア・エ）の最後の例で、あとから建てた建物を「5番の2」とした点は、準則79条7号の「2、3の支号」の例を、同条2号の例と並べて示したもので、実際の番号は個別の事情で決まります。',
    ],
    phrases=['同じ敷地に二棟なら支号を付けます', '二筆にまたがる建物は床面積の多い側で決めます', '連続する地番はないしで略記できます', 'あとの建物は二の支号で既存はそのままです', '所在は床面積の多い地番を先に書きます'],
    header=dict(t1='家屋番号の付け方、', t2='どう決まる？', topic='不動産登記規則　家屋番号',
                kanji='家・屋・番・号・規・則'),
    poster_intro='家屋番号と所在の記録を、「建物の数と地番の数」（グループA：ア・イ・ウ）と「あとから建てた建物と所在の順序」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='家屋番号と所在の書き方を整理', sub='不動産登記規則 第112条、準則 第79条と第88条（毎日ドリル 第42日）',
        col_a='建物の数と地番の数', col_b='あとから建てた建物と所在の順序', n_a=3,
        cards=[
            dict(h='一筆に二個の建物は支号を付ける',
                 ill='one isometric land plot with two small house models on it. Each house has a small house-number plate: the left plate is labeled 「六番一の一」 and the right plate is labeled 「六番一の二」. A green check mark sits beside the plot.',
                 words=['六番一の一', '六番一の二'], tag='地番に支号を付ける'),
            dict(h='二筆にまたがる建物は床面積の多い側',
                 ill='two adjacent isometric land plots, the left labeled 「五番」 and the right labeled 「六番」. One house model straddles the boundary; its larger part sits on the right plot, which is highlighted with a green glow. A green check mark sits beside the right plot.',
                 words=['五番', '六番'], tag='多い側の地番と同じ'),
            dict(h='連続する地番はないしで略記できる',
                 ill='three isometric land plots in a row with no labels on them. A wide green bracket spans all three plots and carries a label 「五番地ないし七番地」. A green check mark sits beside the bracket.',
                 words=['五番地ないし七番地'], tag='支号なしの連続だけ'),
            dict(h='あとの建物は二の支号、既存はそのまま',
                 ill='one isometric land plot with an existing house model carrying a plate labeled 「八番」, and a newly built house model carrying a plate labeled 「八番の二」. A small padlock icon sits beside the existing house plate to show it stays unchanged. A green check mark sits beside the new house.',
                 words=['八番', '八番の二'], tag='既存は変更しない'),
            dict(h='所在は床面積の多い地番を先に',
                 ill='two adjacent isometric land plots labeled 「三番」 on the left and 「五番」 on the right. One house model straddles the boundary with its larger part on the left plot. Above the house, a title strip labeled 「三番地、五番地」. A green check mark sits beside the title strip.',
                 words=['三番', '五番', '三番地、五番地'], tag='多い方が先'),
        ],
        kanji='番・地・支・号・床・面・積・連・続・略・記・既・存・所・在・建・物・家・屋'.split('・')),
    nb_label='ア・イ・エ・オ肢', nb_intro='ア・イ・エ・オの補足説明に合わせた2枚です。1枚目は、二筆にまたがる建物の家屋番号と所在の決め方を整理します。2枚目は、同じ敷地に建物が複数あるときの家屋番号の決め方を整理します。',
    notebooks=[
        dict(name='二筆にまたがる建物の家屋番号と所在', args=dict(
            title='二筆にまたがる建物の書き方', sub='家屋番号と所在（毎日ドリル 第42日 イ・オ）',
            req='a three-row table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table with three rows stacked vertically, each row with a small icon on the left, a blue label cell in the middle, and a green answer cell on the right.
Row 1 icon: a house straddling two plots, larger part on the right plot. Label cell: 家屋番号（附属建物なし）. Answer cell: 床面積の多い部分の敷地の地番と同一
Row 2 icon: a main house with a small annex straddling two plots. Label cell: 家屋番号（附属建物あり）. Answer cell: 主である建物の敷地の地番と同一
Row 3 icon: a title strip with two plot numbers. Label cell: 所在の記録. Answer cell: 床面積の多い部分の地番を先に記録
Above the table, a header band with the label: 二筆にまたがる建物
Use exactly these strings, and no others. Do not draw any check mark or cross mark.""",
            callout='二筆以上の土地にまたがる建物は、地番の若い順ではなく、床面積の多い部分の地番で決めます。\n家屋番号も、所在の記録の順序も、決め手は床面積の多い部分です。',
            footer='不動産登記事務取扱手続準則79条3号・88条2項',
            kanji='二・筆・建・物・家・屋・番・号・附・属・床・面・積・敷・地・主・所・在・記・録'.split('・'), what='table',
            check='confirm there are exactly three table rows, and that no check mark and no cross mark is drawn, ')),
        dict(name='同じ敷地に建物が複数あるとき', args=dict(
            title='同じ敷地に建物が複数あるとき', sub='家屋番号の支号（毎日ドリル 第42日 ア・エ）',
            req='a three-row table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table with three rows stacked vertically, each row with a small icon on the left, a blue label cell in the middle, and a green answer cell on the right.
Row 1 icon: one land plot with one house. Label cell: 一筆に建物が一個. Answer cell: 5番
Row 2 icon: one land plot with two houses at the same time. Label cell: 同時に二個以上. Answer cell: 5番の1、5番の2
Row 3 icon: one land plot with an existing house and a new house. Label cell: あとから建物を追加. Answer cell: あとの建物は5番の2（既存の5番は変更しなくてよい）
Above the table, a header band with the label: 家屋番号の決め方
Use exactly these strings, and no others. Do not draw any check mark or cross mark.""",
            callout='一筆の土地に建物が一個なら、地番と同じ番号です。\nあとから建物を追加するときは、あとの建物に2、3の支号を付け、既存の建物の家屋番号は変更しなくてかまいません。',
            footer='不動産登記事務取扱手続準則79条1号・2号・7号',
            kanji='家・屋・番・号・決・同・時・追・加・既・存・変・更・建・物・筆・土・地・個'.split('・'), what='table',
            check='confirm there are exactly three table rows, and that no check mark and no cross mark is drawn, ')),
    ],
)
