D = dict(
    catch='図面は、何ごとに作るかを押さえる',
    intro='土地所在図、地積測量図、建物図面、各階平面図の作成のしかたを問う問題です（不動産登記規則75条・76条・78条・81条・82条、不動産登記事務取扱手続準則51条〜53条）。この問題は「正しいもの」を選びます。\n\nこの記事では、図面を「何ごとに」作るのか、土地所在図を地積測量図で兼ねられる条件、区分建物の建物図面と各階平面図に描く線の種類を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('分筆後の地積測量図は、分筆前の土地ごとに作る',
               '分筆の登記を申請するときの分筆後の土地の地積測量図は、分筆前の土地ごとに作成します（不動産登記規則75条2項）。分筆前の土地を図示し、分筆線を明らかにして、分筆後の各土地に符号を付けます（同規則78条）。\n\n問題文は「甲土地と乙土地のそれぞれについて、各別に作成しなければならない」としているので、本肢は誤りです。\n\n**たとえば**、甲土地を二つに分ける分筆の場合は、もとの甲土地の形を1枚の図面に描き、そこに分筆線を引いて、分かれた各部分に符号を付けます。分かれた土地ごとに図面を2枚作るわけではありません。'),
        'イ': ('縮尺が同じなら、地積測量図で土地所在図を兼ねられる',
               '土地所在図は、近傍類似の土地についての地図と同じ縮尺で作成します（不動産登記規則76条2項）。\n\n地積測量図の縮尺が土地所在図の縮尺と同じで、地積測量図によって土地の所在を明確に表示できるときは、地積測量図をもって土地所在図を兼ねることができます。この場合、図面の標記は「土地所在図兼地積測量図」と書きます（準則51条4項）。本肢は正しいといえます。\n\n**たとえば**、周辺の地図の縮尺が250分の1の地域で、250分の1で作った地積測量図によって土地の位置がはっきり分かるなら、土地所在図を別に作る必要はありません。1枚で済み、その標記を「土地所在図兼地積測量図」とします。'),
        'ウ': ('区分建物の建物図面は、最低階を描き、一棟の1階を点線で示す',
               '建物図面は、建物の敷地と、その1階の位置と形状を明確にするものです。区分建物の場合は、「地上の最低階」の位置と形状を明確にします（不動産登記規則82条1項）。\n\n区分建物では、点線でその建物が属する一棟の建物の1階の形状も明確にし、1階以外の部分に存するときは「建物の存する部分3階」のように記録します（準則52条2項）。本肢は正しいといえます。\n\n**たとえば**、マンションの3階のみにある1室の建物図面には、その3階の部分を実線で描き、一棟の1階の形を点線で示します。そして、「建物の存する部分3階」と書き添えます。'),
        'エ': ('各階平面図で、1階の位置は点線で示す',
               '各階平面図で1階以外の階層を表示するときは、1階の位置を点線で表示します（準則53条1項）。\n\n問題文は「一点鎖線をもって」としているので、本肢は誤りです。一点鎖線は、区分建物の建物図面で、存する階層の形状が一棟の建物の1階の形状と異なるときに使う線です（準則52条3項）。\n\n**たとえば**、2階建の居宅の各階平面図で、2階の平面を描くときは、その2階の図に、1階の位置を点線で重ねて示します。'),
        'オ': ('建物図面は、主である建物と附属建物をあわせて一個ごとに作る',
               '建物図面と各階平面図は、一個の建物ごとに作成します。附属建物があるときは、主である建物と附属建物を合わせて一個の建物とします（不動産登記規則81条）。\n\nそのうえで、図面には、主である建物か附属建物かの別と、附属建物の符号を記録します（同規則82条2項）。\n\n問題文は「それぞれ各別に作成しなければならない」としているので、本肢は誤りです。\n\n**たとえば**、新築した母屋と、その附属建物の車庫を一つの申請で登記する場合は、1枚の建物図面に母屋と車庫の両方を描きます。そして、母屋と車庫のどちらが主か附属かを書き分けます。'),
    },
    summary=[
        ('ア', '誤', '分筆後の地積測量図は、分筆後の土地ごとではなく、分筆前の土地ごとに作る'),
        ('イ', '正', '縮尺が同じで所在を明確に表示できるなら、地積測量図で土地所在図を兼ねられる'),
        ('ウ', '正', '区分建物の建物図面は、地上の最低階を描き、一棟の1階を点線で示す'),
        ('エ', '誤', '各階平面図で1階以外を表示するときの1階の位置は、一点鎖線ではなく点線'),
        ('オ', '誤', '建物図面は、主である建物と附属建物を合わせて一個の建物ごとに作る'),
    ],
    summary_tail='アとオは「図面を何ごとに作るか」、エは「線の種類」を入れ替えた出題です。図面は、作る単位と描く線をセットで整理しましょう。',
    supplements=[
        '### 補足説明（ア・オ）：図面を作る単位\n\n土地と建物の図面は、作る単位が決まっています。\n\n| 図面 | 作成の単位 |\n|---|---|\n| 土地所在図・地積測量図 | 一筆の土地ごと（不動産登記規則75条1項） |\n| 分筆後の地積測量図 | 分筆前の土地ごと（同条2項） |\n| 建物図面・各階平面図 | 一個の建物ごと。附属建物があれば、あわせて一個（同規則81条） |\n\n**たとえば**、分筆の図面は、分筆後の土地の数ではなく、もとの土地の数で数えます。建物の図面は、母屋と車庫を別々ではなく、まとめて一個として数えます。',
        '### 補足説明（ウ・エ）：点線と一点鎖線の使い分け\n\n建物の図面で一棟の建物の1階などを示す線には、点線と一点鎖線があります。\n\n| 場面 | 線 |\n|---|---|\n| 区分建物の建物図面で、一棟の建物の1階の形状を示す | 点線（準則52条2項） |\n| 区分建物の建物図面で、存する階層の形状が一棟の1階の形状と異なるときの、その階層の形状 | 一点鎖線（同条3項） |\n| 各階平面図で、1階以外の階層を表示するときの、1階の位置 | 点線（準則53条1項） |\n\n**たとえば**、各階平面図の1階の位置は、常に点線です。一点鎖線は、区分建物の建物図面で、階ごとに形が違うときの特別な場面で使います。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第41日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則75条・76条・78条・81条・82条、不動産登記事務取扱手続準則51条・52条・53条は、`note-articles/laws/` 配下の原文で確認しました。準則52条の線の凡例と図の例示は、原文の図表が文字として取り込めていないため、図そのものは確認していません。',
        'イの地積測量図による土地所在図の兼用（準則51条4項）は、前の3項の「規則74条3項の用紙で地積測量図を作成する場合」を前提にした規定です。本文では、問題文の「書面の地積測量図」に合わせて説明しています。',
        '各肢の具体例（甲土地の分筆、250分の1の地域、マンションの3階、2階建の居宅、母屋と車庫）は、条文の文言をかみ砕いた一般的な説明で、個別の先例・通達の確認はしていません。',
    ],
    phrases=['分筆の地積測量図は分筆前の土地ごとです', '縮尺が同じなら一枚で兼ねられます', '区分建物は最低階と一棟の一階を描きます', '各階平面図の一階の位置は点線です', '主と附属は合わせて一個の建物です'],
    header=dict(t1='土地と建物の図面、', t2='作り方は？', topic='不動産登記規則　図面の作成',
                kanji='土・地・建・物・図・面'),
    poster_intro='登記所に提供する図面を、「土地の図面」（グループA：ア・イ）と「建物の図面」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='登記所の図面の作り方を整理', sub='不動産登記規則 第75条から第82条、準則 第51条から第53条（毎日ドリル 第41日）',
        col_a='土地の図面', col_b='建物の図面', n_a=2,
        cards=[
            dict(h='分筆の地積測量図は分筆前の土地ごと',
                 ill='one drawing sheet showing a single land plot outline divided by a dashed line labeled 「分筆線」 into two parts, each part marked with a small circle symbol. A surveyor figure holds the sheet. A green check mark sits beside the sheet.',
                 words=['分筆線'], tag='一枚に分筆線を描く'),
            dict(h='縮尺が同じなら一枚で兼ねられる',
                 ill='a surveyor figure holding a single drawing sheet whose title band is labeled 「土地所在図兼地積測量図」. Two smaller sheets fade into the single sheet with a small arrow. A green check mark sits beside the sheet.',
                 words=['土地所在図兼地積測量図'], tag='一枚で兼ねる'),
            dict(h='区分建物は最低階と一棟の一階を描く',
                 ill='an apartment building cross-section on the left and a drawing sheet on the right. On the sheet, the upper floor outline is drawn as a solid line and the lowest-floor outline of the whole building is drawn as a dotted line. A caption bar on the sheet is labeled 「建物の存する部分三階」. A green check mark sits beside the sheet.',
                 words=['建物の存する部分三階'], tag='一階は点線'),
            dict(h='各階平面図の一階の位置は点線',
                 ill='a two-story house model on the left and a drawing sheet on the right. On the sheet, the second floor outline is drawn as a solid line and the first floor outline is drawn as a dotted line. No text on any object. A green check mark sits beside the sheet.',
                 words=[], tag='一階の位置は点線'),
            dict(h='主と附属は一枚にまとめて作成',
                 ill='one drawing sheet showing a main house outline labeled 「主」 and a small garage outline labeled 「附属」. An arrow gathers the two outlines onto the one sheet. A green check mark sits beside the sheet.',
                 words=['主', '附属'], tag='一個の建物ごとに作成'),
        ],
        kanji='分・筆・線・土・地・所・在・図・兼・積・測・量・建・物・存・部・階・点・平・面・附・属・主'.split('・')),
    nb_label='ア・ウ・エ・オ肢', nb_intro='ア・ウ・エ・オの補足説明に合わせた2枚です。1枚目は、図面を作る単位を整理します。2枚目は、点線と一点鎖線の使い分けを整理します。',
    notebooks=[
        dict(name='図面を作る単位', args=dict(
            title='図面は、何ごとに作る？', sub='図面の作成単位（毎日ドリル 第41日 ア・オ）',
            req='a three-row table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table with three rows stacked vertically, each row with a small icon on the left, a blue label cell in the middle, and a green answer cell on the right.
Row 1 icon: a single land plot. Label cell: 土地所在図・地積測量図. Answer cell: 一筆の土地ごと
Row 2 icon: a land plot divided by a dashed line. Label cell: 分筆後の地積測量図. Answer cell: 分筆前の土地ごと
Row 3 icon: a main house and a small garage drawn together inside one frame. Label cell: 建物図面・各階平面図. Answer cell: 一個の建物ごと（附属建物とあわせて一個）
Above the table, a header band with the label: 作成の単位
Use exactly these strings, and no others. Do not draw any check mark or cross mark.""",
            callout='分筆後の地積測量図は、分筆前の土地ごとに作ります。\n建物図面と各階平面図は、主である建物と附属建物をあわせて一個の建物ごとに作ります。',
            footer='不動産登記規則75条・81条',
            kanji='作・成・単・位・土・地・所・在・図・積・測・量・分・筆・前・建・物・面・各・階・平・附・属'.split('・'), what='table',
            check='confirm there are exactly three table rows, and that no check mark and no cross mark is drawn, ')),
        dict(name='点線と一点鎖線の使い分け', args=dict(
            title='点線と一点鎖線の使い分け', sub='建物図面と各階平面図の線（毎日ドリル 第41日 ウ・エ）',
            req='a three-row table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table with three rows stacked vertically, each row with a small line sample on the left (a dotted line for rows 1 and 3, a dash-dot line for row 2, no text on the samples), a blue label cell in the middle, and a green answer cell on the right. The words 点線 and 一点鎖線 are drawn large and in different accent colors (blue for 点線, orange for 一点鎖線) so they can never be confused or swapped.
Row 1 Label cell: 区分建物の建物図面で、一棟の建物の一階の形状. Answer cell: 点線
Row 2 Label cell: 区分建物の建物図面で、存する階層の形状が一棟の一階と異なるとき. Answer cell: 一点鎖線
Row 3 Label cell: 各階平面図で、一階以外を表示するときの一階の位置. Answer cell: 点線
Above the table, a header band with the label: 描く線の種類
Use exactly these strings, and no others. Do not draw any check mark or cross mark.""",
            callout='各階平面図の1階の位置は、常に点線です。\n一点鎖線は、区分建物の建物図面で、存する階層の形状が一棟の建物の1階の形状と異なるときに使います。',
            footer='不動産登記事務取扱手続準則52条・53条',
            kanji='点・線・一・鎖・区・分・建・物・図・面・棟・形・状・階・各・平・位・置'.split('・'), what='table',
            check='confirm there are exactly three table rows, that 点線 and 一点鎖線 are drawn in different accent colors, and that no check mark and no cross mark is drawn, ')),
    ],
)
