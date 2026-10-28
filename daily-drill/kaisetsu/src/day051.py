D = dict(
    catch='閉鎖記録は土地五十年、建物三十年',
    intro='登記記録などの保存期間と、登記事項証明書や附属書類の閲覧について問う問題です（不動産登記規則28条・196条、不動産登記法121条、不動産登記令21条）。数字の取り違えや、「正当な理由が要るかどうか」の線引きが狙われます。\n\nこの記事では、土地と建物で保存期間が違う点と、図面の閲覧が自由にできる理由を、具体的な場面で確かめます。この問題は、正しい記述の組合せを選ぶ形です。',
    sections={
        'ア': ('土地の閉鎖登記記録は、五十年間保存される',
               '土地に関する閉鎖登記記録の保存期間は、閉鎖した日から五十年間です（不動産登記規則28条4号）。\n\n甲土地を乙土地に合筆すると、甲土地の登記記録は閉鎖されます。その閉鎖した日から五十年間、保存されます。本肢は正しい記述です。\n\n**たとえば**、隣り合う二筆の土地を一筆にまとめたとき、なくなった側の土地の記録は消えてしまうのではなく、閉鎖された状態で長く保存されます。'),
        'イ': ('建物の閉鎖登記記録は、三十年間保存される',
               '建物に関する閉鎖登記記録の保存期間は、閉鎖した日から三十年間です（不動産登記規則28条5号）。五十年間は、土地に関する閉鎖登記記録の期間です（同条4号）。\n\n問題文は、取り壊された乙建物の閉鎖登記記録を五十年間保存されるとしているので、本肢は誤りです。\n\n**たとえば**、古い家を取り壊して滅失の登記をしたとき、その建物の記録は閉鎖から三十年間保存されます。同じ「なくなった」でも、土地より短い期間です。'),
        'ウ': ('表示に関する登記の申請情報は、受付から三十年間',
               '表示に関する登記の申請情報及びその添付情報の保存期間は、受付の日から三十年間です（不動産登記規則28条9号）。\n\n書面で申請した丙建物の表題登記の申請情報及び添付情報も、受付の日から三十年間保存されます。本肢は正しい記述です。\n\n**たとえば**、新築した建物の表題登記を申請したとき、提出した申請書や添付した書類は、受け付けた日から三十年間、登記所に残ります。'),
        'エ': ('図面の閲覧には、正当な理由は要らない',
               '何人も、登記官に対し、手数料を納付して、地積測量図などの政令で定める図面の閲覧を請求することができます（不動産登記法121条2項、不動産登記令21条1項）。正当な理由が必要なのは、これらの図面以外の附属書類の閲覧です（法121条3項）。\n\n問題文は、地積測量図の閲覧に正当な理由を要するとしているので、本肢は誤りです。\n\n**たとえば**、隣の土地の所有者は、境界の位置を知るために、分筆の際に提出された地積測量図を、理由を示さずに閲覧できます。'),
        'オ': ('閉鎖登記記録の現在事項証明書は請求できない',
               '登記事項証明書の記載事項の規定は、閉鎖登記記録については一部だけが準用されます。準用されるのは、全部事項証明書、何区何番事項証明書、一棟建物全部事項証明書です（不動産登記規則196条2項）。現在事項証明書は、準用されません。\n\n問題文は、閉鎖登記記録の現在事項証明書を請求できるとしているので、本肢は誤りです。\n\n**たとえば**、合筆で閉鎖された甲土地の記録を調べたいときは、記録の全部を写した全部事項証明書を請求します。現に効力のある部分だけを写す現在事項証明書は、閉鎖された記録にはなじまないので、請求できません。'),
    },
    summary=[
        ('ア', '正', '土地に関する閉鎖登記記録は、閉鎖した日から五十年間保存される'),
        ('イ', '誤', '建物に関する閉鎖登記記録は、閉鎖した日から三十年間保存される'),
        ('ウ', '正', '表示に関する登記の申請情報及び添付情報は、受付の日から三十年間保存される'),
        ('エ', '誤', '地積測量図などの図面の閲覧は、正当な理由がなくても請求できる'),
        ('オ', '誤', '閉鎖登記記録については、現在事項証明書の交付は請求できない'),
    ],
    summary_tail='イは土地と建物の数字の取り違え、エは図面と図面以外の附属書類の取り違え、オは証明書の種類の取り違えを狙った出題です。土地は五十年、建物は三十年と、まず数字を押さえましょう。',
    supplements=[
        '### 補足説明（イ）：登記記録などの保存期間\n\n保存期間は、対象ごとに決まっています（不動産登記規則28条）。\n\n| 対象 | 保存期間 |\n|---|---|\n| 閉鎖していない登記記録 | 永久 |\n| 土地に関する閉鎖登記記録 | 閉鎖した日から五十年間 |\n| 建物に関する閉鎖登記記録 | 閉鎖した日から三十年間 |\n| 表示に関する登記の申請情報及び添付情報 | 受付の日から三十年間 |\n\n**たとえば**、合筆で閉鎖された土地の記録は五十年間、取り壊された建物の記録は三十年間残ります。土地の記録のほうが長く保存されます。',
        '### 補足説明（エ・オ）：閲覧や証明書でできること、できないこと\n\n図面の閲覧と、閉鎖登記記録の証明書には、それぞれ決まりがあります。\n\n| 請求するもの | 条件や範囲 | 根拠 |\n|---|---|---|\n| 地積測量図などの図面の閲覧 | 何人も請求でき、正当な理由は不要 | 法121条2項、令21条1項 |\n| 図面以外の附属書類の閲覧 | 正当な理由が必要 | 法121条3項 |\n| 閉鎖登記記録の証明書 | 全部事項、何区何番事項、一棟建物全部事項の三種。現在事項は不可 | 規則196条2項 |\n\n**たとえば**、隣地の測量図は理由なしに見られますが、申請書そのものの閲覧には正当な理由が必要です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第51日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則28条4号・5号・9号と196条1項・2項、不動産登記法121条2項・3項、不動産登記令21条1項は、`note-articles/laws/` 配下の原文で確認しました。',
        'オの「現在事項証明書が閉鎖登記記録になじまない」という理由は、規則196条2項が現在事項証明書を準用していないことからの一般的な整理で、条文に理由が書かれているわけではありません。',
        'エ・ウの具体例（隣地の所有者が測量図を閲覧する、新築の表題登記の申請書）は、場面を思い描くための例です。申請書の閲覧に正当な理由が必要であることは、法121条3項の文言に基づきます。',
    ],
    phrases=['土地の閉鎖記録は五十年保存です', '建物の閉鎖記録は三十年保存です', '表示の申請情報は三十年保存です', '図面の閲覧は誰でもできるんです', '閉鎖記録に現在事項証明書はありません'],
    header=dict(t1='閉鎖した記録、', t2='いつまで保存？', topic='不動産登記　保存期間と閲覧',
                kanji='閉・鎖・保・存・閲・覧'),
    poster_intro='登記記録などの保存期間と閲覧・証明書を、「保存期間」（グループA：ア・イ・ウ）と「閲覧と証明書」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='保存期間と閲覧を整理', sub='不動産登記規則 第28条と第196条（毎日ドリル 第51日）',
        col_a='保存期間', col_b='閲覧と証明書', n_a=3,
        cards=[
            dict(h='土地の閉鎖記録は五十年保存',
                 ill='an isometric land plot record sheet stamped 「閉鎖」 placed in a storage box, with a calendar page beside the box labeled 「五十年」. A green check mark sits beside the calendar page.',
                 words=['閉鎖', '五十年'], tag='土地は五十年'),
            dict(h='建物の閉鎖記録は三十年保存',
                 ill='an isometric building record sheet stamped 「閉鎖」 placed in a storage box, with a calendar page beside the box labeled 「三十年」. A green check mark sits beside the calendar page.',
                 words=['閉鎖', '三十年'], tag='建物は三十年'),
            dict(h='表示の申請情報は受付から三十年',
                 ill='a stack of application papers stamped 「受付」 next to a calendar page labeled 「三十年」. A green check mark sits beside the calendar page.',
                 words=['受付', '三十年'], tag='受付の日から数える'),
            dict(h='図面の閲覧は誰でもできる',
                 ill='a neighboring owner figure looking at a drawing sheet labeled 「地積測量図」 at a counter, with no document held up as a reason. A green check mark sits beside the drawing sheet.',
                 words=['地積測量図'], tag='正当な理由は不要'),
            dict(h='閉鎖記録の証明書は全部事項など',
                 ill='a closed record sheet stamped 「閉鎖」 beside a certificate sheet labeled 「全部事項証明書」. A green check mark sits beside the certificate sheet.',
                 words=['閉鎖', '全部事項証明書'], tag='現在事項は対象外'),
        ],
        kanji='閉・鎖・五・十・年・三・受・付・地・積・測・量・図・全・部・事・項・証・明・書'.split('・')),
    nb_label='イ・エ・オ肢', nb_intro='イ・エ・オの補足説明に合わせた2枚です。1枚目は、保存期間を対象ごとの表で示します。2枚目は、閲覧や証明書で請求できるものと条件を、表で整理します。',
    notebooks=[
        dict(name='登記記録などの保存期間', args=dict(
            title='どれだけ保存される？', sub='保存期間の整理（毎日ドリル 第51日 イ）',
            req='a table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table in the upper half, with four rows and two columns, and a small isometric icon at the left of each row.
Column headers: 対象 | 保存期間
Row 1 (gray accent), icon: a record sheet with an infinity-like loop mark. Cells: 閉鎖していない登記記録 | 永久
Row 2 (blue accent), icon: a land plot with a closed stamp. Cells: 土地に関する閉鎖登記記録 | 閉鎖した日から五十年間
Row 3 (orange accent), icon: a building with a closed stamp. Cells: 建物に関する閉鎖登記記録 | 閉鎖した日から三十年間
Row 4 (green accent), icon: a stack of application papers. Cells: 表示に関する登記の申請情報及び添付情報 | 受付の日から三十年間
Use exactly these strings, and no others, for the table text. The 五十年間 cell is drawn in blue and the 三十年間 cells in orange and green, so they can never be confused or duplicated.""",
            callout='閉鎖した登記記録は、土地が五十年間、建物が三十年間保存されます。\n土地と建物で数字が違うので、取り違えないようにしましょう。',
            footer='不動産登記規則28条',
            kanji='対・象・保・存・期・間・登・記・録・土・地・建・物・閉・鎖・表・示・申・請・情・報・添・付・受・付・日・永・久'.split('・'), what='table',
            check='confirm the 五十年間 cell appears only once in row 2 while 三十年間 appears in rows 3 and 4 in different accent colors, ')),
        dict(name='閲覧と証明書でできること', args=dict(
            title='請求できる？できない？', sub='閲覧と証明書の請求（毎日ドリル 第51日 エ・オ）',
            req='a table diagram',
            layout="""--- TABLE ---
Render as a clean flat-design table in the upper half, with three rows and two columns, and a small isometric icon at the left of each row.
Column headers: 請求するもの | 条件や範囲
Row 1 (blue accent), icon: a drawing sheet at a counter. Cells: 地積測量図などの図面の閲覧 | 何人も請求できる（正当な理由は不要）
Row 2 (orange accent), icon: a stack of application papers with a lock. Cells: 図面以外の附属書類の閲覧 | 正当な理由が必要
Row 3 (green accent), icon: a closed record sheet with a certificate. Cells: 閉鎖登記記録の証明書 | 全部事項、何区何番事項、一棟建物全部事項の三種
Use exactly these strings, and no others, for the table text. Each row has its own accent color so the rows are never confused or duplicated.""",
            callout='地積測量図などの図面は、だれでも理由なしに閲覧できます。\n図面以外の附属書類の閲覧には正当な理由が必要で、閉鎖登記記録の証明書は三種類に限られます。',
            footer='不動産登記法121条、不動産登記規則196条2項',
            kanji='請・求・地・積・測・量・図・面・閲・覧・附・属・書・類・正・当・理・由・閉・鎖・登・記・録・証・明・全・部・事・項・棟・建・物'.split('・'), what='table',
            check='confirm the three rows carry three different condition strings in different accent colors, ')),
    ],
)
