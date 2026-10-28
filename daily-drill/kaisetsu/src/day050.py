D = dict(
    catch='合筆は合筆後、分筆は分筆後の個数で数える',
    intro='表示に関する登記の登録免許税を問う問題です（登録免許税法2条・3条・5条10号、別表第一の一の（十三））。表示に関する登記の大半は課税されませんが、分筆や合筆などは、所有権の登記がある不動産について、一個につき千円が課されます。\n\nこの記事では、何個で数えるのか、課税されない場合はいつか、だれが納めるのかを確かめましょう。この問題は、誤っている記述の組合せを選ぶ形です。',
    sections={
        'ア': ('合筆の税は、合筆前ではなく合筆後の個数で数える',
               '土地の合筆による登記事項の変更の登記は、合筆後の不動産の個数について、一個につき千円が課されます（登録免許税法別表第一の一の（十三）ロ）。\n\n三筆を合筆すると、合筆後は一筆です。税額は1,000円になります。問題文の合筆前の個数3個で3,000円は誤りです。\n\n**たとえば**、隣り合う甲土地、乙土地、丙土地の三筆を一筆にまとめるときは、できあがる土地は一つなので、1,000円です。'),
        'イ': ('分筆の税は、分筆後の個数で数える',
               '土地の分筆による登記事項の変更の登記は、分筆後の不動産の個数について、一個につき千円が課されます（登録免許税法別表第一の一の（十三）イ）。\n\n甲土地を分筆して三筆にすると、分筆後は三個で、税額は3,000円です。本肢は正しい記述です。\n\n**たとえば**、広い一筆の土地を三つに切り分けるときは、できあがる土地が三つなので、1,000円の三つ分で3,000円になります。'),
        'ウ': ('所有権の登記がない建物の分割は、課税されない',
               '登録免許税は、別表第一に掲げる登記について課されます（登録免許税法2条）。分筆や分割などの税は、所有権の登記のある不動産に限って課されます（同法別表第一の一の（十三））。\n\n表題登記だけがされていて所有権の登記がない甲建物の分割の登記には、登録免許税は課されません。本肢は正しい記述です。\n\n**たとえば**、新築して表題登記だけを済ませた建物の附属建物を切り離すときは、まだ所有権の登記がないので、税はかかりません。'),
        'エ': ('墳墓地の分筆は、非課税',
               '墳墓地に関する登記には、登録免許税を課さないとされています（登録免許税法5条10号）。\n\n所有権の登記がある墳墓地を分筆して二筆の墳墓地にするときは、どちらも墳墓地なので、分筆の登記に登録免許税は課されません。本肢は正しい記述です。\n\n**たとえば**、墓地として使っている土地を二つに分けるときは、分けた後も墓地のままなので、税はかかりません。'),
        'オ': ('共有者は連帯して納付する義務を負う',
               '登記等を受ける者は、登録免許税を納める義務があります。登記等を受ける者が二人以上あるときは、これらの者は、連帯して納付する義務を負います（登録免許税法3条）。\n\n問題文は、持分に応じて納付する義務を負い、連帯して納付する義務は負わないとしているので、本肢は誤りです。\n\n**たとえば**、AとBが共有する土地を分筆して二筆にすると、税額は2,000円です。AもBも、この全額について納める義務を負います。'),
    },
    summary=[
        ('ア', '誤', '合筆の税は、合筆後の個数について一個につき千円で、三筆を合筆すると1,000円'),
        ('イ', '正', '分筆の税は、分筆後の個数について一個につき千円で、三筆にすると3,000円'),
        ('ウ', '正', '所有権の登記がない建物の分割の登記には、登録免許税は課されない'),
        ('エ', '正', '墳墓地に関する登記は非課税なので、墳墓地を二筆にする分筆にも課されない'),
        ('オ', '誤', '登記等を受ける者が二人以上あるときは、連帯して納付する義務を負う'),
    ],
    summary_tail='アは、個数を数える時点を取り違えさせる出題です。オは、連帯を持分に応じた分担にすり替えています。分筆と合筆は、できあがる土地の個数で数える、と覚えましょう。',
    supplements=[
        '### 補足説明（ア）：分筆と合筆は、どの時点の個数で数えるか\n\n分筆も合筆も、税額は一個につき千円ですが、数える個数は「できあがる不動産」の個数です（登録免許税法別表第一の一の（十三））。\n\n| 登記 | 数える個数 | 例 | 税額 |\n|---|---|---|---|\n| 合筆 | 合筆後の個数 | 三筆が一筆になる | 一個で1,000円 |\n| 分筆 | 分筆後の個数 | 一筆が三筆になる | 三個で3,000円 |\n\nどちらも、所有権の登記のある不動産が対象です。\n\n**たとえば**、三筆を一筆にまとめるのと、一筆を三筆に分けるのとでは、元の筆数が逆でも、数える個数は「できあがる側」なので、税額は1,000円と3,000円で違います。',
        '### 補足説明（オ）：連帯して納付する義務\n\n登記等を受ける者が二人以上あるときは、連帯して納付する義務を負います（登録免許税法3条）。\n\n- 連帯：全員が、税額の全部について納付の義務を負う。\n- 持分に応じた分担：各自が、自分の持分の分だけ納付の義務を負う（本肢の問題文の書き方）。\n\n**たとえば**、AとBが共有する土地を分筆して2,000円の税がかかるとき、Aは自分の持分の半分の1,000円だけを負うのではなく、2,000円の全額について納める義務を負います。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第50日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、登録免許税法2条・3条・5条10号と、別表第一の一の（十三）イ・ロは、`note-articles/laws/` 配下の原文で確認しました。',
        'ウについて、所有権の登記がない建物の分割の登記が別表第一に掲げられていないため課税されない、という説明は、別表第一の（十三）が「所有権の登記のある不動産」を対象としていることからの整理です。',
        'オの連帯の効果（全員が全額について納付の義務を負う）は、条文の「連帯して納付する義務を負う」という言葉の一般的な意味に基づく説明です。具体例の金額は、場面を思い描くための例です。',
    ],
    phrases=['合筆の税は合筆後の個数で数えます', '分筆の税は分筆後の個数で数えます', '所有権の登記がなければ課税されません', '墳墓地の登記は非課税です', '共有者は連帯して納めるんです'],
    header=dict(t1='登録免許税は、', t2='何個で数える？', topic='登録免許税法　表示の登記',
                kanji='登・録・免・許・税・表・示・数'),
    poster_intro='表示に関する登記の登録免許税を、「税額の数え方」（グループA：ア・イ・ウ）と「非課税と納付義務」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='表示に関する登記の税を整理', sub='登録免許税法 第2条と第3条ほか（毎日ドリル 第50日）',
        col_a='税額の数え方', col_b='非課税と納付義務', n_a=3,
        cards=[
            dict(h='合筆の税は合筆後の個数で数える',
                 ill='three neighboring land plots on the left merging into one land plot on the right, with a thin arrow between them. A single coin icon labeled 「千円」 sits beside the one merged plot. A green check mark sits beside the coin.',
                 words=['千円'], tag='合筆後の個数で数える'),
            dict(h='分筆の税は分筆後の個数で数える',
                 ill='one land plot on the left being split into three land plots on the right, with a thin arrow between them. Each of the three plots has its own coin icon labeled 「千円」. A green check mark sits beside the three plots.',
                 words=['千円'], tag='分筆後の個数で数える'),
            dict(h='所有権の登記がなければ課税されない',
                 ill='a record sheet that has only a title section labeled 「表題部」 and no owner section, beside a building being divided into two parts by a thin line. No coin icon appears. A green check mark sits beside the record sheet.',
                 words=['表題部'], tag='分割でも課税なし'),
            dict(h='墳墓地に関する登記は非課税',
                 ill='an isometric cemetery plot with two gravestones, split into two plots by a thin line. A sign beside it is labeled 「墳墓地」. No coin icon appears. A green check mark sits beside the sign.',
                 words=['墳墓地'], tag='税はかからない'),
            dict(h='共有者は連帯して納付する',
                 ill='two owner figures linked by a thick chain, both holding the same single tax bill labeled 「連帯」. A green check mark sits beside the bill.',
                 words=['連帯'], tag='全員が全額の責任'),
        ],
        kanji='合・筆・千・円・分・割・表・題・部・墳・墓・地・連・帯'.split('・')),
    nb_label='ア・オ肢', nb_intro='ア・オの補足説明に合わせた2枚です。1枚目は、分筆と合筆で個数を数える時点の違いを左右の対比で示します。2枚目は、連帯と持分に応じた分担の違いを、図で示します。',
    notebooks=[
        dict(name='分筆と合筆の個数の数え方', args=dict(
            title='何個で数える？', sub='分筆と合筆の登録免許税（毎日ドリル 第50日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings. The left header is 合筆 and the right header is 分筆. Draw them in different accent colors (blue on the left and orange on the right) so they can never be confused or duplicated. Neither panel uses a cross mark.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 合筆
Scene: an isometric scene of three land plots on the left merging into one land plot on the right.
Result badges (stacked): 合筆後の個数で数える | 一個で1,000円

RIGHT PANEL (orange accent):
Panel header: 分筆
Scene: an isometric scene of one land plot on the left splitting into three land plots on the right.
Result badges (stacked): 分筆後の個数で数える | 三個で3,000円""",
            callout='税額は、どちらも一個につき千円ですが、数えるのは「できあがる土地」の個数です。\n三筆を一筆にする合筆は1,000円、一筆を三筆にする分筆は3,000円です。',
            footer='登録免許税法別表第一の一の（十三）',
            kanji='合・筆・分・個・数・土・地・一・三・円・税・額'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (合筆 on the left and 分筆 on the right) in different accent colors, ')),
        dict(name='連帯して納付する義務', args=dict(
            title='共有者は、どこまで納める？', sub='登録免許税の納付義務（毎日ドリル 第50日 オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings. The left header is 連帯して納付する and the right header is 持分に応じて分担する. Draw them in different accent colors (green on the left and gray on the right) so they can never be confused or duplicated. The left panel shows a green check mark and the right panel shows a red cross.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (green accent):
Panel header: 連帯して納付する
Scene: an isometric scene of two owner figures, A and B, linked by a chain, each one holding the whole tax bill of 2,000円.
Result badge with a green check mark: 全員が全額について義務を負う

RIGHT PANEL (gray accent):
Panel header: 持分に応じて分担する
Scene: an isometric scene of two owner figures, A and B, each holding half of a torn tax bill of 1,000円.
Result badge with a red cross: 登録免許税法3条の定めとは違う""",
            callout='登記等を受ける者が二人以上いるときは、連帯して納付する義務を負います。\n持分の分だけを負うのではなく、各自が税額の全部について義務を負います。',
            footer='登録免許税法3条',
            kanji='連・帯・納・付・持・分・応・担・全・額・義・務・税・定'.split('・'), what='panels',
            check='confirm the two panel headers are different strings (連帯して納付する on the left and 持分に応じて分担する on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')),
    ],
)
