# -*- coding: utf-8 -*-
"""実践答練 第3回 択一式 第1問〜第20問の、総論インフォグラフィック（②問題全体）と
見出し画像（①）のカードデータ。

- 図解するのは常に「正しいルール」（誤りの肢は正しい形に直してある）
- 見出し：20字以内、結論タグ：5〜15字（build.pyが機械チェックする）
- cols = [(列の見出し, 色), ...]、cards の col は列の番号（0 か 1）
- ill は画像生成AIへの描画指示（英語＋画像内に入れる日本語ラベルは「」で囲む）
"""

GREEN, BLUE = "green", "blue"

Q = {}

# ---------------------------------------------------------------- 第1問
Q[1] = dict(
    file="q01-ishihyouji.md",
    theme="意思表示の効力と錯誤",
    title=["意思表示は、いつ届いて", "誰に主張できる？"],
    cols=[("届いたかどうかのルール", GREEN), ("本人・相手の事情と錯誤", BLUE)],
    cards=[
        dict(col=0, h="受け取りを妨げたら届いたことに",
             ill="A mailbox whose slot is blocked by a person's hand, and a letter envelope shown arriving on a calendar day labelled 「届くはずだった日」. Short label 「通知」 on the envelope.",
             tag="届いたものとみなす"),
        dict(col=0, h="公示は過失があると届かない",
             ill="A court notice board with a newspaper-like gazette sheet and a calendar page labelled 「2週間」. Beside it a small speech label 「過失あり」 over the person who posted it, with the letter returned unarrived.",
             tag="過失があれば不到達"),
        dict(col=1, h="出した後に亡くなっても有効",
             ill="A letter flying from a faded person silhouette (labelled 「表意者」) toward a recipient who holds the letter. The sender silhouette is drawn pale; the letter itself is drawn bright and in full color.",
             tag="効力は妨げられない"),
        dict(col=1, h="未成年者でも親権者が知れば主張可",
             ill="A teenager with a letter, and a parent figure labelled 「親権者」 reading the same letter and nodding. A small label 「知った後」 near the parent.",
             tag="親権者が知った後なら主張可"),
        dict(col=1, h="事情の錯誤は表示が必要",
             ill="A buyer with a thought bubble 「新駅ができる」 who also says it to the seller in a speech bubble 「新駅ができるから買います」. A cancel-stamp icon beside the contract.",
             tag="表示していれば取消し可"),
    ],
    hdr=dict(l1="届く・届かない、", l2="誰に主張できる？",
             scene="a mailbox, a letter envelope with a small calendar, and a scale-of-justice icon, with a parent holding hands with a child"),
)

# ---------------------------------------------------------------- 第2問
Q[2] = dict(
    file="q02-shoyuuken.md",
    theme="所有権と対抗関係",
    title=["所有権の請求と登記、", "勝つのは誰？"],
    cols=[("誰に請求できるか", GREEN), ("登記で勝負が決まる場面", BLUE)],
    cards=[
        dict(col=0, h="未登記で譲った人は請求の相手外",
             ill="A land plot with a building on it. The land owner (labelled 「A」) points a request arrow at the current building owner (labelled 「C」). The previous owner (labelled 「B」) stands faded behind with a small tag 「譲渡済み」.",
             tag="相手は今の所有者"),
        dict(col=0, h="承諾のない転借人にも直接請求",
             ill="A chain of three people: owner 「A」, tenant 「B」, sub-tenant 「C」. The owner points a request arrow directly at sub-tenant C, skipping B. Label on the arrow 「明渡し」.",
             tag="解除なしで請求できる"),
        dict(col=1, h="共有持分の譲渡は登記が必要",
             ill="A land plot shared by two people 「A」 and 「B」. A buyer 「C」 holds a contract for A's share, but the registry-stamp slot is empty. B holds a signboard 「第三者」.",
             tag="登記なしでは対抗不可"),
        dict(col=1, h="解除の後の第三者とは早い者勝ち",
             ill="A timeline with three steps 「売買」 then 「解除」 then 「転売」. At the end two registry stamps race toward a land-register page; the second buyer 「C」 gets his stamp first.",
             tag="先に登記した方が優先"),
        dict(col=1, h="法定相続分を超える分は登記が必要",
             ill="Two heirs 「B」 and 「C」 and a division agreement document. A third party 「D」 holds a registered land-register page. Heir B holds only a half-pie chart labelled 「2分の1」 as what can be claimed.",
             tag="超える部分は対抗不可"),
    ],
    hdr=dict(l1="登記がないと", l2="主張できない場面",
             scene="a land plot with a registry stamp racing toward a land-register page, and two small house icons"),
)

# ---------------------------------------------------------------- 第3問
Q[3] = dict(
    file="q03-haigusha-kyojuuken.md",
    theme="配偶者居住権",
    title=["配偶者居住権は、", "どんな場面で成り立つ？"],
    cols=[("成立するかどうか", GREEN), ("権利の中身", BLUE)],
    cards=[
        dict(col=0, h="配偶者との共有でも成立する",
             ill="A house shared by a husband icon (labelled 「亡くなった人」, drawn pale) and a wife icon (labelled 「配偶者」). A key icon is handed to the wife.",
             tag="配偶者との共有は成立"),
        dict(col=0, h="配偶者以外との共有では不成立",
             ill="A house shared by the deceased (pale) and a son icon labelled 「子」. The key icon cannot be handed to the wife; a small red ✕ is drawn on the key.",
             tag="配偶者以外とは不成立"),
        dict(col=1, h="期間を定めたら更新できない",
             ill="A calendar showing a long span labelled 「10年」 ending at a stop line, with a circular renew-arrow drawn with a red ✕ over it.",
             tag="満了で終了し更新不可"),
        dict(col=1, h="所有者は登記を備えさせる義務",
             ill="A son icon (owner, labelled 「所有者」) handing a registry certificate to the wife icon. A small stamp labelled 「登記」.",
             tag="登記を備えさせる義務"),
        dict(col=1, h="承諾があっても譲渡はできない",
             ill="A wife icon holding a key, a friend icon beside her, and a red ✕ over an arrow labelled 「譲渡」. The owner's approval seal 「承諾」 is shown but does not open the arrow.",
             tag="譲渡は承諾でも不可"),
    ],
    hdr=dict(l1="配偶者居住権は", l2="どこまでできる？",
             scene="a cozy house with a key, an elderly couple icon, and a calendar page"),
)

# ---------------------------------------------------------------- 第4問
Q[4] = dict(
    file="q04-genpon-kanpu.md",
    theme="添付書類の原本還付",
    title=["提出した書類は、", "返してもらえる？"],
    cols=[("返してもらえるもの", GREEN), ("返してもらえないもの", BLUE)],
    cards=[
        dict(col=0, h="還付には謄本の提出が必要",
             ill="An original document being returned from a desk, with a photocopy stamped 「原本と相違ない」 attached to the application.",
             tag="謄本を付けて請求"),
        dict(col=0, h="遺産分割協議書の印鑑証明書は返る",
             ill="An inheritance-division agreement paper with a seal-certificate card, and a returning arrow going back to the applicant. Label 「遺産分割協議書」.",
             tag="還付を請求できる"),
        dict(col=0, h="複数の登記所用の委任状は返る",
             ill="One power-of-attorney sheet with two arrows going to two registry-office buildings labelled 「甲」 and 「乙」, and a returning arrow back to the applicant.",
             tag="その申請専用ではない"),
        dict(col=1, h="承諾書の印鑑証明書は返らない",
             ill="A consent paper from a bank labelled 「抵当権者の承諾書」 with a seal-certificate card. The return arrow is drawn with a red ✕.",
             tag="還付を請求できない"),
        dict(col=1, h="申請書に押した印鑑の証明書も返らない",
             ill="An application form for merging two buildings with a seal-certificate card attached. The return arrow is drawn with a red ✕.",
             tag="還付を請求できない"),
    ],
    hdr=dict(l1="登記の添付書類、", l2="返してもらえる？",
             scene="a desk with a stack of documents, a returning arrow, and seal-certificate cards"),
)

# ---------------------------------------------------------------- 第5問
Q[5] = dict(
    file="q05-touki-shinsei-chousa.md",
    theme="登記官による実地調査",
    title=["登記官の実地調査、", "どこまでできる？"],
    cols=[("登記官ができること", GREEN), ("実地調査の進め方", BLUE)],
    cards=[
        dict(col=0, h="積極的に調査し職権で登記する",
             ill="A registry officer with a clipboard standing at a building, discovering an unregistered building and stamping a registration form by himself.",
             tag="職権で表示登記"),
        dict(col=0, h="質問と文書の提示を求めることができる",
             ill="A registry officer asking a building owner a question (speech bubble) and receiving a document. A sun icon at the top and a moon icon at the bottom of the day, labelled 「日出から日没まで」.",
             tag="質問も文書の提示も可"),
        dict(col=0, h="調査後に必要なら図面を作成する",
             ill="A registry officer drawing a plan on a desk after the visit, with floor-plan and land-map sheets.",
             tag="図面を作成する"),
        dict(col=1, h="隣地の立会いは必要なときだけ",
             ill="An owner standing at a plot of land, with a neighbor figure drawn faded behind a dotted line labelled 「必要があると認めるとき」.",
             tag="隣地は必要なときだけ"),
        dict(col=1, h="身分・氏名・趣旨を明らかにする",
             ill="A registry officer showing an ID card to an owner at the door, with a speech bubble 「調査のためです」.",
             tag="名乗って目的を告げる"),
    ],
    hdr=dict(l1="登記官の実地調査", l2="ここがポイント",
             scene="a registry officer with a clipboard, a land plot with boundary stakes, and a building icon"),
)

# ---------------------------------------------------------------- 第6問
Q[6] = dict(
    file="q06-ichi-no-shinsei-jouhou.md",
    theme="一の申請情報による申請",
    title=["まとめて申請できる組合せは", "どれ？"],
    cols=[("一の申請情報にできる", GREEN), ("別々に申請する", BLUE)],
    cards=[
        dict(col=0, h="所有権の登記も併せるなら一緒に",
             ill="Two buildings merging into one building with an arrow, and two forms clipped together into a single application sheet labelled 「合体」 and 「所有権」.",
             tag="一の申請情報で申請する"),
        dict(col=0, h="地目変更と分筆は一緒に申請",
             ill="A land plot being split by a dashed line with a change of land category tag, and the two forms clipped together as one application.",
             tag="同じ申請書でできる"),
        dict(col=0, h="区分と接続する区分建物への合併",
             ill="A building divided into parts and one part merging into the adjoining unit, with the two forms clipped together as one application.",
             tag="まとめて申請できる"),
        dict(col=1, h="分割と合体は別々の申請",
             ill="Two separate application sheets, one labelled 「分割」 and one labelled 「合体」, with a red ✕ over a paper clip between them.",
             tag="別々に申請する"),
        dict(col=1, h="表題登記と共用部分の登記も別々",
             ill="Two separate application sheets, one labelled 「表題登記」 and one labelled 「共用部分」, with a red ✕ over a paper clip between them.",
             tag="一括の規定はない"),
    ],
    hdr=dict(l1="申請書は", l2="まとめられる？",
             scene="paper clips joining some application forms, and building and land-plot icons"),
)

# ---------------------------------------------------------------- 第7問
Q[7] = dict(
    file="q07-ichifudousan-ichitouki.md",
    theme="一不動産一登記記録主義",
    title=["1個の建物は、", "どう数える？"],
    cols=[("建物を1個と数える場面", GREEN), ("登記記録のやり直し", BLUE)],
    cards=[
        dict(col=0, h="区分所有の意思がなければ全体で1個",
             ill="A row-house building with three doors, a single owner icon holding one key ring, and one big bracket around the whole building labelled 「1個」.",
             tag="全体で1個の建物"),
        dict(col=0, h="一体利用の数棟は意思に反しなければ1個",
             ill="A main house and a small annex joined by a dotted line, with an owner icon. A speech label 「別々に登記したい」 is shown faded beside the owner.",
             tag="所有者の意思次第"),
        dict(col=1, h="初めから区分なしは滅失と表題登記",
             ill="A single undivided building wrongly labelled as two units; the wrong registry page is crossed by a stamp 「滅失」, and a new page labelled 「表題登記」 is made.",
             tag="滅失の登記からやり直す"),
        dict(col=1, h="二重登記は後の登記を抹消する",
             ill="Two registry pages of the same building, the older one kept in color and the newer one drawn faded and crossed by an eraser stamp 「抹消」.",
             tag="後の登記を抹消"),
        dict(col=1, h="地番区域が違えば職権で分筆",
             ill="A land plot split by a thick district border line, with a registry officer stamping a new registry page for the part on the other side. Label 「地番区域」.",
             tag="新たな登記記録を作る"),
    ],
    hdr=dict(l1="1個の建物、", l2="どう数える？",
             scene="a row house with several doors, a single large bracket around it, and a registry page"),
)

# ---------------------------------------------------------------- 第8問
Q[8] = dict(
    file="q08-ikisoku-tenshya.md",
    theme="登記記録の移記・転写",
    title=["閉鎖される記録は移記、", "残る記録は転写"],
    cols=[("閉鎖される記録は移記", GREEN), ("残る記録は転写", BLUE)],
    cards=[
        dict(col=0, h="合筆では甲土地から乙土地へ移記",
             ill="Two land plots, 「甲」 faded with a closed-folder icon, merging into 「乙」. An easement entry page moves by an arrow from 甲 to 乙. Label 「地役権」.",
             tag="地役権の登記を移記"),
        dict(col=0, h="合体の存続登記は移記する",
             ill="Two buildings merging into one; the old building's registry page is closed (folder icon), and an entry page moves by an arrow to the merged building's page. Label 「存続登記」.",
             tag="存続登記を移記"),
        dict(col=0, h="非区分建物の区分は新しい記録へ移記",
             ill="One ordinary building divided into two; its old registry page is closed, and the mortgage entry moves to both new pages. Label 「抵当権」.",
             tag="新しい記録へ移記"),
        dict(col=1, h="区分建物の区分は元が残るので転写",
             ill="A condominium unit divided into two; the old registry page stays open, and a copy of the mortgage entry is copied to the new unit's page. Label 「抵当権」.",
             tag="乙建物へ転写"),
        dict(col=1, h="敷地権でなくなったら建物から土地へ転写",
             ill="A condominium building page that stays open, and a copy of the mortgage entry copied to the land's registry page. Label 「抵当権」.",
             tag="土地の記録へ転写"),
    ],
    hdr=dict(l1="閉鎖されたら移記、", l2="残るなら転写",
             scene="two registry pages, one closed in a folder and one open, with an arrow copying an entry"),
)

# ---------------------------------------------------------------- 第9問
Q[9] = dict(
    file="q09-touki-kiroku-heisa.md",
    theme="登記記録の閉鎖",
    title=["登記記録が", "閉鎖されないのはどれ？"],
    cols=[("更正・規約廃止などでは閉鎖されない", GREEN), ("保存登記が錯誤で抹消されたとき", BLUE)],
    cards=[
        dict(col=0, h="表題部の更正は抹消記号で処理",
             ill="A registry page with the old owner name struck through by a line and the new name written below. The page stays open.",
             tag="記録は閉鎖されない"),
        dict(col=0, h="敷地権の不存在でも土地の記録は残る",
             ill="A land registry page where only a small entry labelled 「敷地権」 is erased while the page stays open.",
             tag="土地の記録は残る"),
        dict(col=0, h="共用部分の規約を廃止しても記録は残る",
             ill="A shared-facility building page where the label 「共用部分」 is struck through and the owner's name is written. The page stays open.",
             tag="表題登記で足りる"),
        dict(col=1, h="相続人名義の保存登記が消えても残る",
             ill="A registry page where the heir's preservation entry is erased, and the original owner's name is restored. Label 「相続人」.",
             tag="表題部所有者を回復"),
        dict(col=1, h="直接譲渡を受けた人の保存登記も同じ",
             ill="A registry page for a condominium unit where the buyer's preservation entry is erased and the seller's name 「表題部所有者」 is restored.",
             tag="閉鎖せず記録を残す"),
    ],
    hdr=dict(l1="閉鎖される？", l2="されない？",
             scene="a registry page with a struck-through line, a folder icon, and an eraser"),
)

# ---------------------------------------------------------------- 第10問
Q[10] = dict(
    file="q10-hyoudaibu-shoyuusha.md",
    theme="表題部所有者の更正と変更",
    title=["表題部所有者を直すとき、", "誰が・何が必要？"],
    cols=[("更正の登記のルール", GREEN), ("名義が変わる場面", BLUE)],
    cards=[
        dict(col=0, h="新しい所有者の住所を証する情報",
             ill="A new owner figure holding a residence certificate card labelled 「住所を証する情報」 attached to an application form.",
             tag="住所の証明が必要"),
        dict(col=0, h="真正な所有者はどちらも申請できる",
             ill="Two real owners 「A」 and 「C」 both holding application forms for a registry page that lists 「A」 and 「B」.",
             tag="AもCも申請できる"),
        dict(col=0, h="持分の更正は増える人の承諾も必要",
             ill="Three co-owners; the one whose share decreases and the one whose share increases both hold consent papers. Labels 「減る」 and 「増える」.",
             tag="持分が変わる全員の承諾"),
        dict(col=1, h="相続人なしは亡A相続財産へ変更",
             ill="A registry page where the owner name changes to 「亡A相続財産」, with a liquidator figure labelled 「相続財産清算人」 holding the application.",
             tag="氏名変更の登記を申請"),
        dict(col=1, h="吸収合併はB法人名義で保存登記",
             ill="Company 「A」 merging into company 「B」 with an arrow, and a new preservation-registration form in the name of 「B」.",
             tag="名称変更では対応不可"),
    ],
    hdr=dict(l1="表題部所有者の", l2="更正と変更",
             scene="an owner name board being replaced, a registry page, and a residence certificate card"),
)

# ---------------------------------------------------------------- 第11問
Q[11] = dict(
    file="q11-chiseki-sokuryouzu.md",
    theme="地積測量図の作成と記録事項",
    title=["地積測量図、", "電子と書面で何が違う？"],
    cols=[("作成方式のルール", GREEN), ("記録事項と作図", BLUE)],
    cards=[
        dict(col=0, h="電子申請は土地所在図を兼ねられる",
             ill="A digital land-survey drawing on a laptop screen with two small labels 「地積測量図」 and 「土地所在図」 merged into one sheet.",
             tag="縮尺を問わず兼ねる"),
        dict(col=0, h="書面は申請人が記名、作成者が署名",
             ill="A paper survey drawing with two signature fields; the applicant field shows a printed name labelled 「申請人 記名」, and the maker field shows a handwritten signature labelled 「作成者 署名」.",
             tag="署名・押印は作成者"),
        dict(col=0, h="電子申請も年月日と氏名を記録",
             ill="A digital drawing with a date field and two name fields, labelled 「作成年月日」 and 「申請人・作成者」.",
             tag="年月日と氏名を記録"),
        dict(col=1, h="近くに基準点がなければ地物を基準に",
             ill="A remote hillside land plot with no survey marker, and a stone wall labelled 「恒久的な地物」 used as the reference point for coordinates.",
             tag="座標系の記録は不要"),
        dict(col=1, h="方位を変え縮図にして作成できる",
             ill="A long narrow land plot drawn rotated and shrunk to fit on one sheet of paper. Labels 「方位」 and 「縮図」.",
             tag="作成方法の工夫が可能"),
    ],
    hdr=dict(l1="地積測量図の", l2="ルールまとめ",
             scene="a survey drawing sheet, a measuring tape, a tripod instrument, and a laptop"),
)

# ---------------------------------------------------------------- 第12問
Q[12] = dict(
    file="q12-chiekiken-zumen.md",
    theme="地役権図面",
    title=["地役権図面は、", "いつ要る？誰が署名する？"],
    cols=[("提供が必要かどうか", GREEN), ("作成のルール", BLUE)],
    cards=[
        dict(col=0, h="範囲が全部なら地役権図面は不要",
             ill="A servient land plot split into two; the right-of-way covers one whole plot (fully shaded). No drawing sheet is attached.",
             tag="一部のときだけ必要"),
        dict(col=0, h="承役地の合筆は範囲が必ず一部",
             ill="Two land plots merging; only the original plot is shaded as right-of-way, and a drawing sheet 「地役権図面」 is attached.",
             tag="地役権図面が必要"),
        dict(col=0, h="要役地の分筆では提供しない",
             ill="A dominant land plot (labelled 「要役地」) being split by a dashed line, with no drawing sheet attached.",
             tag="承役地のための図面"),
        dict(col=1, h="署名するのは作成者でなく地役権者",
             ill="A drawing sheet with a signature field filled by a person labelled 「地役権者」, while the maker figure labelled 「作成者」 does not sign.",
             tag="地役権者が署名"),
        dict(col=1, h="縮尺は適宜でよい",
             ill="Two drawing sheets at different scales side by side, one labelled 「地役権図面」 and one labelled 「地積測量図」, both accepted.",
             tag="縮尺を合わせなくてよい"),
    ],
    hdr=dict(l1="地役権図面は", l2="いつ必要？",
             scene="a narrow path across a land plot, a signboard, and a drawing sheet"),
)

# ---------------------------------------------------------------- 第13問
Q[13] = dict(
    file="q13-tatemono-hyoudaibu-henkou.md",
    theme="建物の表題部の変更・更正",
    title=["新築か変更か、", "どの手続になる？"],
    cols=[("何をどう申請するか", GREEN), ("例外的な扱い", BLUE)],
    cards=[
        dict(col=0, h="新築の表題登記には③を付けない",
             ill="A newly built building with a completed-construction flag, and an application form where a circled-number tag 「③」 is not written. Label 「新築」.",
             tag="変更ではない"),
        dict(col=0, h="解体移転は滅失と表題登記の2件",
             ill="A building being demolished at one plot (labelled 「滅失」) and a new building at another plot (labelled 「表題登記」), with a residence card icon labelled 「住民票コード」.",
             tag="申請は2件"),
        dict(col=0, h="建物の分割は所有者の希望で申請",
             ill="A building with an annex being divided by a dashed line, with an owner icon who decides by himself. Label 「分割」.",
             tag="義務ではない"),
        dict(col=1, h="所有権登記の後の附属建物だけ記録される",
             ill="A timeline with 「所有権の登記」 first and 「附属建物の新築」 second, leading to a new registry page labelled 「分割による所有権の登記」.",
             tag="後に登記された附属建物"),
        dict(col=1, h="えい行移転でまたがっても管轄は元のまま",
             ill="A building being pulled across a border between two registry offices labelled 「甲」 and 「乙」, with the application going to 「甲」.",
             tag="管轄は甲登記所のまま"),
    ],
    hdr=dict(l1="新築？変更？", l2="手続の見分け方",
             scene="a building under construction, a building being dragged on rollers, and a registry page"),
)

# ---------------------------------------------------------------- 第14問
Q[14] = dict(
    file="q14-tatemono-bunkatsu-gappei.md",
    theme="建物の分割・合併の登記",
    title=["建物の分割と合併、", "手続のポイントは？"],
    cols=[("申請のしかた", GREEN), ("記録と税金", BLUE)],
    cards=[
        dict(col=0, h="識別情報を出せない名義人にだけ事前通知",
             ill="Two co-owners 「A」 and 「B」; A hands over a registry-ID slip, and a notification letter goes only to B who has none.",
             tag="通知を受けるのはBだけ"),
        dict(col=0, h="別々の建物の分割も一の申請情報で",
             ill="Two buildings each with an annex being divided, and the two forms clipped together into one application sheet.",
             tag="目的が同じならまとめる"),
        dict(col=0, h="合併の登記は代位で申請できない",
             ill="A buyer 「B」 reaching for a merge application form that belongs to owner 「A」, stopped by a red ✕. Label 「代位」.",
             tag="代位申請は不可"),
        dict(col=1, h="担保権のある建物の分割は共同担保目録",
             ill="A building with a mortgage entry divided into two, and a joint-collateral list sheet linking both new pages. Label 「共同担保目録」.",
             tag="共同担保目録を作る"),
        dict(col=1, h="表題登記だけの建物は課税されない",
             ill="A building whose registry page has only a title part, and a blank tax receipt with a red ✕ drawn over a coin icon (no amount of money is written).",
             tag="登録免許税はかからない"),
    ],
    hdr=dict(l1="建物の分割・合併、", l2="どこに気をつける？",
             scene="two buildings being divided and joined by dashed lines, and a coin icon"),
)

# ---------------------------------------------------------------- 第15問
Q[15] = dict(
    file="q15-tatemono-shozai.md",
    theme="建物の所在の書き方",
    title=["建物の所在、", "どう書く？"],
    cols=[("書き方のルール", GREEN), ("特殊な場合", BLUE)],
    cards=[
        dict(col=0, h="他の県の名前だけを冠記する",
             ill="A map with two prefectures. The application goes to the registry office of the first prefecture, and only the second prefecture's name is added in front of the address.",
             tag="冠記は他の県だけ"),
        dict(col=0, h="支号があると「ないし」で略せない",
             ill="Four land plots in a row, one of them with a branch number; the shortened phrase 「ないし」 is stopped by a red ✕ at that plot.",
             tag="支号付きは略記不可"),
        dict(col=0, h="浮船やさん橋の建物は何番地先",
             ill="A floating restaurant moored beside a pier near a land plot sign 「8番」, with the address written as 「8番地先」.",
             tag="最も近い地番に先を付ける"),
        dict(col=1, h="区分建物の附属建物は構造欄に記録",
             ill="A detached house with a condominium unit attached as an annex, and a registry-page field labelled 「構造欄」 receiving the condominium building's address.",
             tag="一棟の所在は構造欄へ"),
        dict(col=1, h="仮換地の建物は底地の地番に予定地番",
             ill="A house on a temporary replacement plot; the address uses the underlying existing plot number, with the planned replacement-plot number in parentheses. Label 「底地」 and 「予定地番」.",
             tag="従前地の地番ではない"),
    ],
    hdr=dict(l1="建物の所在、", l2="どう書く？",
             scene="a map with a district border, a floating building beside a pier, and a house on a plot"),
)

# ---------------------------------------------------------------- 第16問
Q[16] = dict(
    file="q16-shikichiken.md",
    theme="敷地権",
    title=["敷地権は、", "いつ・どれだけ生まれる？"],
    cols=[("割合と発生", GREEN), ("転写と抹消", BLUE)],
    cards=[
        dict(col=0, h="敷地権の割合は規約で定められる",
             ill="A condominium building and a rulebook labelled 「規約」 that sets a ratio different from the floor-area ratio.",
             tag="規約の証明情報を提供"),
        dict(col=0, h="持分3分の2を床面積の等しい2戸で分ける",
             ill="A land plot owned by 「A」 and 「B」; A owns two equal units. A pie of A's share is split into two equal halves, each labelled 「6分の2」. B has no unit.",
             tag="各戸6分の2"),
        dict(col=0, h="単独所有地に使用貸借の人がいる場合",
             ill="A land owner 「A」 and a second unit owner 「B」 who only holds a free-use right (labelled 「使用貸借」) on A's land, both in the same building. A land-right badge is shown unavailable with a red ✕.",
             tag="敷地権は発生しない"),
        dict(col=1, h="建物のみの抵当権は土地に転写されない",
             ill="A mortgage entry tagged 「建物のみ」 stays on the building page; the arrow to the land page is crossed by a red ✕.",
             tag="特定登記ではない"),
        dict(col=1, h="地目変更だけでは敷地権は消えない",
             ill="A tennis court plot changed into a parking lot (label 「地目変更」), while the land-right badge 「敷地権」 remains attached.",
             tag="敷地権の抹消は不要"),
    ],
    hdr=dict(l1="敷地権の", l2="割合と発生",
             scene="a condominium building on a shared land plot with a pie chart"),
)

# ---------------------------------------------------------------- 第17問
Q[17] = dict(
    file="q17-kubun-tatemono-hyouji.md",
    theme="区分建物の専有部分",
    title=["専有部分とは、", "どこまでをいう？"],
    cols=[("区分所有と構造上の区分", GREEN), ("共用設備と専有部分", BLUE)],
    cards=[
        dict(col=0, h="区分所有は構造上区分された部分が対象",
             ill="A building with a shop on the first floor and an apartment on the second floor, each owned by a different person.",
             tag="各部分を所有権の目的に"),
        dict(col=0, h="隔壁や階層で遮断され範囲が明確",
             ill="One room in a condominium floor with walls, floor and ceiling clearly outlining its range.",
             tag="範囲が明確なこと"),
        dict(col=0, h="周囲が完全に遮蔽されていなくてよい",
             ill="A shop space whose one side is closed only by a shutter instead of a solid wall, but the range is clearly outlined by a dotted boundary line.",
             tag="完全な遮蔽は不要"),
        dict(col=1, h="共用に供される設備は共用設備",
             ill="A condominium with a ventilation pipe and a drainage manhole, labelled 「共用設備」.",
             tag="排気管やマンホール"),
        dict(col=1, h="共用設備が少しあっても専有部分のことも",
             ill="A room with a small exhaust pipe in one corner, the rest of the room used exclusively by the owner. A badge 「専有部分」 is attached to the room.",
             tag="小さな部分にとどまれば専有部分"),
    ],
    hdr=dict(l1="専有部分、", l2="どこまで？",
             scene="a condominium building cross-section with rooms, a pipe and a manhole"),
)

# ---------------------------------------------------------------- 第18問
Q[18] = dict(
    file="q18-danchi-kyouyoububun.md",
    theme="団地共用部分",
    title=["団地共用部分の登記、", "ここに注意"],
    cols=[("共有と規約のルール", GREEN), ("登記手続のルール", BLUE)],
    cards=[
        dict(col=0, h="団地共用部分は全員の共有",
             ill="Two apartment buildings labelled 「1号館」 and 「2号館」 and a community hall icon. All unit owners of both buildings (drawn as small owner icons) hold hands around the hall.",
             tag="一部共用はない"),
        dict(col=0, h="全部の所有者の規約は公正証書で",
             ill="A single owner of all buildings signing a notarized document at a notary desk, labelled 「公正証書」.",
             tag="公正証書が必要"),
        dict(col=1, h="区分建物は一棟の建物の表示を提供",
             ill="An application form listing an address and a building name for each building, plus an empty house-number field with a red ✕ over it.",
             tag="一棟の建物の表示を書く"),
        dict(col=1, h="抵当権者の承諾に代わる裁判でもよい",
             ill="A bank figure holding a mortgage entry, and a court judgment paper that substitutes for the bank's consent paper.",
             tag="承諾か裁判の情報"),
        dict(col=1, h="規約の廃止後は1か月以内に表題登記",
             ill="A calendar page labelled 「1か月」 and a new-owner figure submitting a title registration form for the hall.",
             tag="申請するのは表題登記"),
    ],
    hdr=dict(l1="団地共用部分", l2="登記のポイント",
             scene="two apartment buildings and a small community hall between them"),
)

# ---------------------------------------------------------------- 第19問
Q[19] = dict(
    file="q19-hikkai-tokutei.md",
    theme="筆界特定の手続",
    title=["筆界特定の手続、", "ここが出る"],
    cols=[("申請と特定のルール", GREEN), ("手続の進み方", BLUE)],
    cards=[
        dict(col=0, h="官庁・公署は所有権の証明を省略できる",
             ill="A city office figure submitting an application form with no ownership-proof paper attached. Label 「官庁・公署」.",
             tag="所有権の証明は省略可"),
        dict(col=0, h="表題登記のない土地は何番地先で特定",
             ill="A plot without a land number, labelled 「何番地先」 beside a neighboring plot signboard.",
             tag="地番は不要"),
        dict(col=0, h="判決の有無が不明でも却下されない",
             ill="A registry officer asking a question with a speech bubble about a past court judgment; nobody answers, and a big forward arrow shows the procedure continuing.",
             tag="手続を進めてよい"),
        dict(col=1, h="資料は定められた期間内に提出する",
             ill="A calendar with a deadline circled, and a person handing a document before the deadline.",
             tag="期間内に提出する"),
        dict(col=1, h="参考人への質問にも許可が必要",
             ill="A boundary investigator figure asking a witness (labelled 「参考人」) a question, with a permission seal 「許可」 from the registry officer.",
             tag="登記官の許可を得る"),
    ],
    hdr=dict(l1="筆界特定の手続、", l2="覚えておこう",
             scene="two neighboring land plots with boundary stakes, a magnifying glass, and an officer"),
)

# ---------------------------------------------------------------- 第20問
Q[20] = dict(
    file="q20-chousashi-gyoumu-seigen.md",
    theme="調査士・調査士法人の業務制限",
    title=["相手方の依頼、", "受けていい場面は？"],
    cols=[("受任できない場面", GREEN), ("受任できる場面", BLUE)],
    cards=[
        dict(col=0, h="同じ事件の相手方は同意でも不可",
             ill="A surveyor figure between two neighbors 「A」 and 「B」 in the same boundary dispute, with a red ✕ over the seat on B's side even though A gives an approval seal.",
             tag="同意があっても不可"),
        dict(col=0, h="関与した事件の相手方は辞めた後も不可",
             ill="A surveyor who left a firm building, walking toward the opposing party of the case he worked on, stopped by a red ✕.",
             tag="関与した事実は残る"),
        dict(col=1, h="元社員が関与なしなら別の事件は可",
             ill="A former partner figure standing outside the firm building, taking a different, unrelated case from neighbor 「B」.",
             tag="同意なしで受任可"),
        dict(col=1, h="書類作成だけの受任なら同意は不要",
             ill="A surveyor preparing documents only (labelled 「書類作成のみ」) accepting a separate case from neighbor 「B」 without any approval seal.",
             tag="同意は要らない"),
        dict(col=1, h="書類作成の受任なら使用人も同意不要",
             ill="A surveyor employed by a firm (labelled 「使用人」), who handles document preparation only (labelled 「書類作成のみ」), accepting a separate case from neighbor 「B」 without any approval seal.",
             tag="使用人でも同意不要"),
    ],
    hdr=dict(l1="相手方の依頼、", l2="受けていい？",
             scene="a surveyor with a tripod instrument between two neighbors' land plots, and a firm building"),
)
