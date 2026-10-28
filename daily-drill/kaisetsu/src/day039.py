D = dict(
    catch='登記識別情報は、提供・通知・失効を整理',
    intro='登記識別情報（登記名義人が自ら登記を申請していることを確認するために用いられる符号その他の情報。不動産登記法2条14号）に関する問題です（同法22条、不動産登記令8条、不動産登記規則62条・64条・65条・67条）。\n\nこの記事では、合体のときに提供する範囲、通知の相手、通知が不要になる場合、失効の申出ができる人、同時に申請するときの特例を、具体的な場面で確認していきましょう。なお、この問題は「誤っているもの」を選ぶ問題です。',
    sections={
        'ア': ('名義人が同じ建物の合体は、いずれか一個分の識別情報で足りる',
               '所有権の登記がある建物の合体による登記等は、登記名義人が登記識別情報を提供して申請します（不動産登記法22条、不動産登記令8条1項2号）。\n\nただし、登記名義人が同一であるときは、合体する建物のうちいずれか一個の建物の所有権の登記名義人の登記識別情報を提供すれば足ります（同条2項2号）。\n\n問題文は「甲建物及び乙建物の双方の」としているので、本肢は誤りです。\n\n**たとえば**、Aさん名義の甲建物と乙建物が合体して、Aさんが申請するとします。Aさんは、甲建物か乙建物のどちらか一方の登記識別情報を提供すれば足ります。両方そろえる必要はありません。'),
        'イ': ('法人の申請人には、代表者に登記識別情報を通知する',
               '申請人が法人である場合の登記識別情報の通知は、その法人の代表者に対してします（不動産登記規則62条1項2号）。通知を受けるための特別の委任を受けた代理人がいるときは、その代理人に対してします（同条2項）。本肢は正しいといえます。\n\n**たとえば**、株式会社Bが、代理人を使わずに所有権の保存の登記を申請したとします。登記が完了したときの登記識別情報は、会社そのものではなく、会社の代表者に通知されます。'),
        'ウ': ('書面による通知は、登記完了から三月で不要になる',
               '登記識別情報を記載した書面で通知を受けるべき者が、登記完了の時から三月以内にその書面を受領しないときは、登記官は通知することを要しません（不動産登記規則64条1項3号）。\n\n問題文は「三十日以内」としています。三十日は、電子情報処理組織で通知を受けるべき者が、送信が可能になった時から三十日以内にファイルに記録しない場合の期間です（同項2号）。本肢は誤りです。\n\n**たとえば**、書面で申請して、登記が完了したのに法務局へ受け取りに行かないまま三月が過ぎたとします。この場合、登記官は通知しなくてかまいません。'),
        'エ': ('相続人も、登記識別情報の失効の申出ができる',
               '登記識別情報の失効の申出は、登記名義人のほか、その相続人その他の一般承継人もすることができます（不動産登記規則65条1項）。相続人が申し出るときは、相続があったことを証する情報も提供します（同条5項）。本肢は正しいといえます。\n\n**たとえば**、登記名義人のAさんが亡くなり、Aさん宛ての登記識別情報が通知されていたとします。相続人のCさんは、その登記識別情報を使えなくするために、失効の申出をすることができます。'),
        'オ': ('前後を明らかにした同時申請では、提供したものとみなす',
               '同一の不動産について二以上の権利に関する登記を、前後を明らかにして同時に申請する場合で、前の登記で登記名義人となる者が後の登記の登記義務者となるときは、後の登記の申請情報と併せて提供すべき登記識別情報は、提供されたものとみなされます（不動産登記規則67条）。\n\n本肢は正しいといえます。\n\n**たとえば**、AからBへの所有権の移転の登記と、Bを登記義務者とする抵当権の設定の登記を、前後を明らかにして同時に申請したとします。Bは移転の登記で名義人になる人で、まだ登記識別情報の通知を受けていません。\n\nそのため、抵当権の設定の登記では、Bの登記識別情報は提供したものとして扱われます。'),
    },
    summary=[
        ('ア', '誤', '名義人が同一の建物の合体では、いずれか一個の建物の登記識別情報を提供すれば足りる'),
        ('イ', '正', '法人が申請人のときは、登記識別情報を代表者に通知する'),
        ('ウ', '誤', '書面による通知は、登記完了から三十日ではなく三月以内に受領しないと不要になる'),
        ('エ', '正', '登記名義人の相続人も、登記識別情報の失効の申出ができる'),
        ('オ', '正', '前後を明らかにした同時申請では、後の登記の登記識別情報は提供したものとみなされる'),
    ],
    summary_tail='アは「提供する範囲」、ウは「期間（三月と三十日）」を入れ替えた出題です。登記識別情報は、提供、通知、失効の三つの場面に分けて整理しましょう。',
    supplements=[
        '### 補足説明（ア）：いずれか一つ分で足りる場合\n\n次の登記は、登記名義人が登記識別情報を提供して申請しますが、まとめて一つ分で足ります（不動産登記令8条2項）。\n\n| 登記 | 提供する登記識別情報 |\n|---|---|\n| 所有権の登記がある土地の合筆 | いずれか一筆の土地の登記名義人のもの |\n| 登記名義人が同一である所有権の登記がある建物の合体による登記等 | いずれか一個の建物の登記名義人のもの |\n| 所有権の登記がある建物の合併 | いずれか一個の建物の登記名義人のもの |\n\n**たとえば**、三筆の土地を合筆するときも、三筆分の登記識別情報をそろえる必要はなく、いずれか一筆分で足ります。',
        '### 補足説明（ウ）：登記識別情報を通知しなくてよい場合\n\n登記識別情報の通知を受けるべき者がいても、次の場合は通知を要しません（不動産登記規則64条1項）。\n\n| 場合 | 内容 |\n|---|---|\n| 希望しない旨の申出 | あらかじめ、通知を希望しない旨を申し出た |\n| 電子で通知を受けるとき | 送信が可能になった時から三十日以内に、自己のファイルに記録しない |\n| 書面で通知を受けるとき | 登記完了の時から三月以内に、書面を受領しない |\n| 官庁又は公署 | あらかじめ通知を希望する旨を申し出た場合を除く |\n\n**たとえば**、電子申請で通知が送られてきたのに三十日間ダウンロードしなかったときと、書面を三月間受け取りに行かなかったときは、どちらも通知は不要になります。期間が違う点に注意しましょう。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第39日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法22条、不動産登記令8条、不動産登記規則62条・64条・65条・67条、および導入で引いた法2条14号は、`note-articles/laws/` 配下の原文で確認しました。',
        '各肢の具体例（三筆の合筆、株式会社の保存登記、受け取りに行かない場合、相続人の失効の申出）は、条文の文言をかみ砕いた一般的な説明で、個別の先例・通達の確認はしていません。',
        'オの「Bはまだ通知を受けていないので、提供したものとして扱われる」という理由づけは、条文からの一般的な整理で、条文そのものの文言ではありません。',
    ],
    phrases=['同じ名義人なら一個分で足ります', '法人への通知は代表者に届きます', '書面の通知は三月で不要になります', '相続人も失効の申出ができます', '同時申請なら提供したとみなされます'],
    header=dict(t1='登記識別情報、', t2='いつ必要？', topic='不動産登記法　登記識別情報',
                kanji='登・記・識・別・情・報'),
    poster_intro='登記識別情報を、「提供と通知」（グループA：ア・イ・ウ）と「失効と提供の省略」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='登記識別情報を整理', sub='不動産登記令 第8条・不動産登記規則 第62条ほか（毎日ドリル 第39日）',
        col_a='提供と通知', col_b='失効と提供の省略', n_a=3,
        cards=[
            dict(h='同じ名義人の合体は一個分で足りる',
                 ill='two house models merging into one house model. Two small ticket cards labeled 「識別情報」 sit beside the two houses; only one ticket is highlighted in green and moves toward an application form, and the other ticket is drawn in faded gray. A green check mark sits beside the form.',
                 words=['識別情報'], tag='いずれか一個分'),
            dict(h='法人への通知は代表者に',
                 ill='an isometric company building. A figure with a name tag labeled 「代表者」 stands at the entrance and receives an envelope from a registrar figure. A green check mark sits beside the envelope.',
                 words=['代表者'], tag='通知の相手は代表者'),
            dict(h='書面の通知は完了から三月で不要',
                 ill='a counter scene with an unclaimed envelope left on the counter, covered by a light dust. A calendar page labeled 「三月」 stands beside the envelope. A green bracket arcs from the envelope to the calendar. A green check mark sits beside the calendar.',
                 words=['三月'], tag='受け取らないと不要'),
            dict(h='相続人も失効の申出ができる',
                 ill='a heir figure with a name tag labeled 「相続人」 at a counter, holding a form labeled 「失効」. A green check mark sits beside the form.',
                 words=['相続人', '失効'], tag='相続人もできる'),
            dict(h='同時申請なら提供したとみなす',
                 ill='two application forms stacked vertically: the upper one labeled 「移転」 and the lower one labeled 「抵当権」, joined by a green bracket labeled 「同時」. A small ticket card on the lower form is drawn with a dotted outline, as if already provided. A green check mark sits beside the bracket.',
                 words=['移転', '抵当権', '同時'], tag='提供したとみなす'),
        ],
        kanji='識・別・情・報・代・表・者・通・知・書・面・三・月・相・続・失・効・移・転・抵・当・権・同・時・合・体・提・供'.split('・')),
    nb_label='ア・ウ肢', nb_intro='ア・ウの補足説明に合わせた2枚です。1枚目は、登記識別情報がいずれか一つ分で足りる三つの登記を整理します。2枚目は、登記識別情報の通知を要しない場合を整理します。',
    notebooks=[
        dict(name='いずれか一つ分で足りる三つの登記', args=dict(
            title='いずれか一つ分で足りる登記', sub='登記識別情報の提供（毎日ドリル 第39日 ア）',
            req='a three-row table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table with three rows stacked vertically, each row with a small icon on the left, a blue label cell in the middle, and a green answer cell on the right.
Row 1 icon: three land plots merging into one. Label cell: 所有権の登記がある土地の合筆. Answer cell: いずれか一筆の登記名義人のもの
Row 2 icon: two house models merging into one. Label cell: 登記名義人が同一の建物の合体. Answer cell: いずれか一個の建物の登記名義人のもの
Row 3 icon: two house models joined by a plus sign. Label cell: 所有権の登記がある建物の合併. Answer cell: いずれか一個の建物の登記名義人のもの
Above the table, a header band with the label: 提供する登記識別情報
Use exactly these strings, and no others. Do not draw any check mark or cross mark.""",
            callout='合筆、登記名義人が同一の建物の合体、建物の合併では、いずれか一つ分の登記識別情報を提供すれば足ります。\n合体では、登記名義人が同一であることが条件です。',
            footer='不動産登記令8条2項',
            kanji='登・記・識・別・情・報・提・供・所・有・権・土・地・合・筆・建・物・体・併・名・義・人'.split('・'), what='table',
            check='confirm there are exactly three table rows, and that no check mark and no cross mark is drawn, ')),
        dict(name='登記識別情報の通知を要しない場合', args=dict(
            title='通知を要しない場合', sub='登記識別情報の通知（毎日ドリル 第39日 ウ）',
            req='a four-row table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table with four rows stacked vertically, each row with a small icon on the left, a blue label cell in the middle, and a green condition cell on the right. The period words in rows 2 and 3 must be drawn large and in different accent colors (orange for 三十日, green for 三月) so they can never be confused or swapped.
Row 1 icon: a person raising a hand. Label cell: 希望しない旨の申出. Condition cell: あらかじめ申し出た
Row 2 icon: a computer screen with an envelope. Label cell: 電子で通知を受けるとき. Condition cell: 送信可能になった時から三十日以内に記録しない
Row 3 icon: a paper envelope on a counter. Label cell: 書面で通知を受けるとき. Condition cell: 登記完了の時から三月以内に受領しない
Row 4 icon: a government building. Label cell: 官庁又は公署. Condition cell: 通知を希望する旨を申し出た場合を除く
Above the table, a header band with the label: 通知を要しない場合
Use exactly these strings, and no others. Do not draw any check mark or cross mark.""",
            callout='電子で通知を受けるときは三十日、書面で通知を受けるときは三月です。\n期間が違うので、通知の方法とセットで覚えておきましょう。',
            footer='不動産登記規則64条1項',
            kanji='登・記・識・別・情・報・通・知・希・望・申・出・電・子・送・信・書・面・受・領・官・庁・公・署'.split('・'), what='table',
            check='confirm there are exactly four table rows, that 三十日 and 三月 are drawn in different accent colors, and that no check mark and no cross mark is drawn, ')),
    ],
)
