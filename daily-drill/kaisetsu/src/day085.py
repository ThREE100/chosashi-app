def _k(*t, n=24):
    out = []
    for c in ''.join(t):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_T1, _T2, _TOP = '脱退と解散の違いは、', 'どこにある？', '土地家屋調査士法　調査士法人'
_cards = [
    dict(h='業務停止の処分で社員は脱退',
         ill='an isometric office desk with a nameplate on the left and a small stop sign beside it. A figure carrying a document tray steps out through a door on the right. A stamp labeled 「業務停止」 sits on the desk. A green check mark sits beside the door.',
         words=['業務停止'], tag='処分を受けると脱退'),
    dict(h='競業の利益は損害と推定',
         ill='an isometric scene: a figure at a side desk, outside the main office, receives a stack of coins, and a thin arrow carries the same stack to a small safe labeled 「推定」 inside the main office. A green check mark sits beside the safe.',
         words=['推定'], tag='損害の額と推定する'),
    dict(h='定款の変更は総社員の同意',
         ill='an isometric meeting table with several figures all raising their hands together around a document. A banner above the table is labeled 「総社員の同意」. A green check mark sits beside the document.',
         words=['総社員の同意'], tag='変更後二週間以内に届出'),
    dict(h='社員がゼロになったら解散',
         ill='an isometric office with one figure sitting at a desk in the middle, drawn in full color and still working. A faded empty office stands beside it with a closed sign. A tag labeled 「社員の欠亡」 is attached to the empty office. A green check mark sits beside the working figure.',
         words=['社員の欠亡'], tag='一人では解散しない'),
    dict(h='民間紛争解決は特定社員だけ',
         ill='an isometric table with two figures. The figure on the left wears a badge labeled 「特定社員」 and is highlighted with a green glow, holding a document. The figure on the right has no badge and stands faded in the background. A green check mark sits beside the highlighted figure.',
         words=['特定社員'], tag='業務を執行できるのは特定社員のみ'),
]

D = dict(
    catch='業務停止で脱退、利益は損害と推定',
    intro='土地家屋調査士法人（調査士法人）の社員について、脱退・競業の禁止・定款の変更・解散・業務の執行を問う問題です（土地家屋調査士法28条・34条・35条・37条から39条）。この問題は、正しいものの組合せを選びます。\n\nこの記事では、「脱退する場合」と「解散する場合」の違い、そして「推定する」と「みなす」の違いを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('業務の停止の処分を受けた社員は、脱退する',
               '調査士法人の社員は、調査士の業務の停止の処分を受け、その停止の期間を経過しない者になったときは、社員となることができません（土地家屋調査士法28条2項1号）。そして、社員がこれに当たることになったときは、その社員は脱退します（同法38条4号）。\n\n本肢は正しいといえます。\n\n**たとえば**、調査士法人Xの社員Aが、懲戒処分として業務の停止を受けたとします。Aは、停止の期間中も社員のままでいることはできず、Xを脱退することになります。'),
        'イ': ('競業で得た利益は、損害の額と「推定」される',
               '社員が、自己や第三者のために法人の業務の範囲に属する業務を行ったときは、その業務で社員や第三者が得た利益の額は、法人に生じた損害の額と推定されます（土地家屋調査士法37条2項）。\n\n問題文は「みなされる」としていますが、条文は「推定する」です。本肢は誤りです。\n\n**たとえば**、社員Bが、法人に内緒で自分の名前で測量の仕事を受け、100万円の利益を得たとします。この100万円は、法人の損害の額と推定されます。ただし「推定」なので、Bは、実際の損害は違うと反論することができます。'),
        'ウ': ('定款の変更は、総社員の同意が必要',
               '調査士法人は、定款に別段の定めがある場合を除き、総社員の同意によって、定款の変更をすることができます（土地家屋調査士法34条1項）。\n\n問題文は「総社員の過半数の同意」としているので、本肢は誤りです。\n\n**たとえば**、社員が3人いて、2人が賛成でも、1人が反対していれば、定款に別段の定めがない限り、定款の変更はできません。なお、定款を変更したときは、変更の日から二週間以内に、調査士会と調査士会連合会に届け出ます（同条2項）。'),
        'エ': ('社員が一人になっても、解散しない',
               '調査士法人が解散する理由の一つは、「社員の欠亡」です（土地家屋調査士法39条1項7号）。欠亡とは、社員が一人もいなくなることをいいます。社員が一人になっただけでは、解散の理由に当たりません。\n\n問題文は「社員がAのみとなった場合には、Xは解散する」としているので、本肢は誤りです。\n\n**たとえば**、社員がAとBの2人の法人で、Bが亡くなったとしても、Aが残っている限り、Xは解散せず、Aの一人の法人として続けることができます。'),
        'オ': ('民間紛争解決手続の代理に関する業務は、特定社員だけが執行する',
               '調査士法人の社員は、原則としてすべて、業務を執行する権利を有し、義務を負います（土地家屋調査士法35条1項）。\n\nただし、民間紛争解決手続代理関係業務については、法3条2項に規定する調査士である社員（特定社員）のみが、業務を執行する権利を有し、義務を負います（同法35条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、社員のCは研修を修了して法務大臣の認定を受けた調査士で、Dはそうでない調査士だとします。境界をめぐる紛争の民間紛争解決手続に関する業務は、Cだけが執行し、Dは執行する立場にありません。'),
    },
    summary=[
        ('ア', '正', '業務の停止の処分を受け、その期間を経過しない者に当たることになった社員は、脱退する'),
        ('イ', '誤', '競業で得た利益の額は、損害の額と「推定」される（「みなす」ではない）'),
        ('ウ', '誤', '定款の変更は、別段の定めがない限り、総社員の同意による（過半数ではない）'),
        ('エ', '誤', '解散の理由は「社員の欠亡」で、社員が一人になっただけでは解散しない'),
        ('オ', '正', '民間紛争解決手続代理関係業務は、特定社員のみが業務を執行する'),
    ],
    summary_tail='イは「推定」と「みなす」、ウは「総社員」と「過半数」、エは「欠亡」と「一人になった」を入れ替えた出題です。脱退の理由（38条）と解散の理由（39条）を、別々の表として覚えておきましょう。',
    supplements=[
        '### 補足説明（イ）：「推定する」と「みなす」は別の言葉\n\n37条2項は、社員が競業の禁止に違反したときの利益の額を、法人の損害の額と「推定する」と定めています。\n\n- 推定する：一応そのとおりに扱うが、違うことを証明すれば覆せる。\n- みなす：違うことを証明しても覆せない。\n\n**たとえば**、社員Bが得た利益が100万円のとき、法人は「損害は100万円」と一応扱えます。しかしBが「実際の損害は30万円だった」と証明できれば、その結果が優先されます。「みなす」であれば、この反論は認められません。',
        '### 補足説明（ア・エ）：脱退の理由と解散の理由は別の表\n\n社員が抜けることと、法人がなくなることは、別の問題です。条文も、脱退の理由（38条）と解散の理由（39条1項）を別々に定めています。\n\n- 脱退の理由（38条）：調査士の登録の取消し／定款に定める理由の発生／総社員の同意／業務の停止の処分など社員となれない事由に当たること／除名。\n- 解散の理由（39条1項）：定款に定める理由の発生／総社員の同意／他の調査士法人との合併／破産手続開始の決定／解散を命ずる裁判／解散の処分／社員の欠亡。\n\n**たとえば**、社員の一人が業務の停止の処分を受けると、その社員は脱退します（ア）。しかし、それだけで法人が解散するわけではありません。法人が解散するのは、社員が一人もいなくなったとき（欠亡）などです（エ）。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第85日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、土地家屋調査士法28条2項1号、34条、35条、37条、38条4号、39条1項7号は、`note-articles/laws/` 配下の原文で確認しました。42条の「二年以内の業務の停止」も同じ原文で確認しています。',
        'イの補足説明の「推定する」と「みなす」の説明は、法律用語の一般的な整理（条文からの一般的な整理）で、調査士法の条文そのものに書かれているわけではありません。',
        'エの「欠亡とは、社員が一人もいなくなること」という説明は、条文の用語の一般的な整理です。調査士法39条の2（社員の死亡により欠亡となった場合の継続）の詳細は、この記事では扱っていません。',
    ],
    phrases=['業務の停止で社員は脱退します', '競業の利益は損害と推定されます', '定款の変更は総社員の同意です', '社員が一人でも解散しません', '紛争解決の業務は特定社員だけです'],
    header=dict(t1=_T1, t2=_T2, topic=_TOP, kanji='・'.join(_k(_T1, _T2, _TOP))),
    poster_intro='調査士法人の社員と法人の運営を、「社員の脱退と競業」（グループA：ア・イ）と「法人の運営の決まり」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='調査士法人の社員の決まりを整理', sub='土地家屋調査士法 第28条・第34条・第35条・第37条・第38条・第39条（毎日ドリル 第85日）',
        col_a='社員の脱退と競業', col_b='法人の運営の決まり', n_a=2,
        cards=_cards,
        kanji=_k(*[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards], '調査士法人の社員の決まりを整理社員の脱退と競業法人の運営の決まり', n=24)),
    nb_label='イ・エ肢', nb_intro='イ・エの補足説明に合わせた2枚です。1枚目は、「推定する」と「みなす」の違いを左右の対比で示します。2枚目は、脱退の理由と解散の理由を左右の表で整理します。',
    notebooks=[
        dict(name='「推定する」と「みなす」の違い', args=dict(
            title='「推定」と「みなす」の違い', sub='社員の競業の禁止（毎日ドリル 第85日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「推定する」 on the left and 「みなす」 on the right; draw them in different accent colors (blue and gray) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 推定する
Scene: an isometric scene of a figure holding a stack of coins at a side desk, and a scale on which a small weight labeled 「反論」 is placed on the other side and tips the balance.
Result badge with a green check mark: 反論できる

RIGHT PANEL (gray accent):
Panel header: みなす
Scene: an isometric scene of the same figure holding a stack of coins, with a locked box beside it. A small weight labeled 「反論」 lies outside the box and cannot be placed on the scale.
Result badge with a red cross: 反論できない""",
            callout='土地家屋調査士法37条2項は、社員が得た利益の額を、法人に生じた損害の額と「推定する」と定めています。\n「推定」なので、実際の損害は違うという反論が認められます。「みなす」であれば、反論は認められません。',
            footer='土地家屋調査士法37条2項',
            kanji='・'.join(_k('推定みなす反論できる土地家屋調査士法社員競業禁止損害利益額')), what='panels',
            check='confirm the two panel headers are different strings (推定する on the left and みなす on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')),
        dict(name='脱退の理由と解散の理由', args=dict(
            title='脱退の理由と解散の理由', sub='調査士法人の社員と法人（毎日ドリル 第85日 ア・エ）',
            req='a two-column table',
            layout="""--- TWO-COLUMN TABLE ---
Two panels side by side (left and right), same height. The two panel headers are different strings; draw them in different accent colors (blue on the left, green on the right). Some item names appear in both panels on purpose; keep each item exactly as written.

LEFT PANEL (blue accent):
Panel header: 社員が脱退する理由
Items (a plain list, one per row):
調査士の登録の取消し
定款に定める理由の発生
総社員の同意
業務の停止の処分を受けたこと
除名
A highlighted row marker beside 「業務の停止の処分を受けたこと」.

RIGHT PANEL (green accent):
Panel header: 法人が解散する理由
Items (a plain list, one per row):
定款に定める理由の発生
総社員の同意
他の調査士法人との合併
破産手続開始の決定
解散を命ずる裁判
解散の処分
社員の欠亡
A highlighted row marker beside 「社員の欠亡」.""",
            callout='社員が抜ける「脱退」と、法人がなくなる「解散」は、別の問題で、理由も別々に定められています。\n業務の停止を受けた社員は脱退しますが、法人が解散するのは、社員が一人もいなくなる「欠亡」などのときです。',
            footer='土地家屋調査士法38条、39条',
            kanji='・'.join(_k('脱退解散理由調査士登録取消定款発生総社員同意業務停止処分除名合併破産手続開始決定命令裁判欠亡土地家屋法人')), what='panels',
            check='confirm the two panel headers are different strings (社員が脱退する理由 on the left and 法人が解散する理由 on the right) and that both lists are copied verbatim, ')),
    ],
)
