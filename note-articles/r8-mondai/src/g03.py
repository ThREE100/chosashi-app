# -*- coding: utf-8 -*-
"""令和8年度 択一式 第11問〜第15問の「作図ガイド型」(⑤)インフォグラフィックのデータ。"""

GUIDE = {}

# ---------------------------------------------------------------- 第11問
GUIDE[11] = dict(
    desc="問題文を読んだ瞬間に、「何を床面積に入れるか」と「どの線で測るか」を見分ける5パネル構成。②の色分け（算入するかどうか＝緑、測り方と階の数え方＝青）を引き継いでいる。",
    field="建物の床面積",
    icons="isometric building floor-plan sheets with a ruler, a bay-window icon, a rooftop stair-tower icon, an elevator-shaft icon, and a two-story cross-section with a void (stairwell-like open space) - adapt the icon set to the topic of how floor area is counted.",
    shared=None,
    panels=[
        dict(
            h="出窓は1.5メートル以上かつ床面と同じ高さで算入",
            diag="A decision flowchart read from top to bottom. A small isometric bay-window icon at the top is labeled「出窓」. First diamond node:「高さが1.5メートル以上か」. Yes arrow goes down to a second diamond node:「下部が床面と同一の高さにあるか」. Yes arrow from the second diamond goes to a green conclusion node:「床面積に算入する」. The No arrow of the first diamond goes to its own red conclusion node:「床面積に算入しない」, and the No arrow of the second diamond goes to its own red conclusion node:「床面積に算入しない」 (a waist-high bay window sitting above the floor level is drawn beside it). No loop arrows anywhere; every branch ends in its own conclusion node.",
            callout="まず、出窓の高さが1.5メートル以上かを確認し、次にその下部が床面と同一の高さにあるかを確認します。両方を満たす出窓だけが床面積に算入されます。",
            tag="二条件そろえば算入",
            color="green",
        ),
        dict(
            h="屋上出入口だけの塔屋は床面積に算入しない",
            diag="A decision flowchart. A small isometric rooftop stair-tower icon labeled「塔屋」 sits at the top. A diamond node asks:「塔屋の一部が管理事務所や倉庫などとして実際に使われているか」. The Yes arrow goes to a green conclusion node:「塔屋全体を床面積に算入する」 (a tower with a small storage room drawn inside). The No arrow goes to its own red conclusion node:「床面積に算入しない」 (a tower that only holds the roof exit, a machine room, or a water tank). A small side note beside the diamond reads「外気分断性があるかどうかでは決まらない」. No loop arrows; each branch ends in its own conclusion node.",
            callout="まず、塔屋の一部が管理事務所や倉庫などとして実際に使われているかを確認します。使われていなければ、外気分断性があっても算入せず、使われていれば塔屋全体を算入します。",
            tag="出入口だけなら不算入",
            color="green",
        ),
        dict(
            h="一棟の建物の床面積は壁の中心線で測る",
            diag="A side-by-side comparison frame with two boxes. LEFT box (highlighted with a thick colored border, full color) labeled「区分建物が属する一棟の建物」: an isometric apartment-building floor plan with a single line drawn through the middle of the wall thickness, labeled「壁その他の区画の中心線」. RIGHT box (faded, greyed-out, dotted outline, since this panel is not about this branch) labeled「区分建物（専有部分）」: one room of the same plan with a line drawn along the inner face of the wall, labeled「内側線」.",
            callout="まず、測る対象が一棟の建物か区分建物の専有部分かを確認し、次に測る線を選びます。一棟の建物は壁その他の区画の中心線、区分建物は内側線で測ります。",
            tag="一棟は中心線で測る",
            color="blue",
        ),
        dict(
            h="吹抜は上階に算入せず1階には算入する",
            diag="An isometric cross-section of a two-story house without a basement. The living room on the first floor is open up to the ceiling of the second floor. The 2nd-floor part above the void is drawn as an empty dotted-outline area with a red ✕ and the label「上階には算入しない」. The 1st-floor floor area under the void is filled with color and a green check mark labeled「1階には算入する」. Two numbered check points are placed beside the drawing: ① the void part on the upper floor, ② the floor of the 1st floor below it.",
            callout="まず、吹抜の部分が上階か1階かを見分けます。次に床の有無を見て、上階には床がないので算入せず、1階には床があるので算入します。",
            tag="吹抜も1階には算入",
            color="blue",
        ),
        dict(
            h="エレベーター室は各階の床面積に算入する",
            diag="An isometric cross-section of a five-story building with one elevator shaft running through all floors. The elevator room on every floor from the 1st to the 5th floor is filled with color and has a green check mark. A small label beside the shaft reads「階段室などと同じく、床を有するものとみなす」. A faded drawing of only the 1st floor colored, with a red ✕, is shown in the corner to represent the wrong idea「1階だけ」.",
            callout="まず、エレベーター室が階段室などと同じく床を有するものとみなされることを確認し、次に各階の床面積に算入します。1階だけではありません。",
            tag="全階に算入する",
            color="blue",
        ),
    ],
    footer="不動産登記規則115条、不動産登記事務取扱手続準則82条6号・8号・11号に基づく整理です。",
)

# ---------------------------------------------------------------- 第12問
GUIDE[12] = dict(
    desc="問題文を読んだ瞬間に、「図面は要るか」「記録はどう書くか」「新築や区分建物に制限はあるか」を見分ける5パネル構成。②の色分け（図面と記録の仕方＝緑、制限と区分建物＝青）を引き継いでいる。",
    field="附属建物",
    icons="isometric icons of a main house with a small storage shed next to it, a building-drawing sheet, a registry-book page with a column for the attached building, a mortgage tag, and an apartment-building icon - adapt the icon set to the topic of attached buildings.",
    shared=None,
    panels=[
        dict(
            h="附属建物の取壊しは建物図面を省略できる",
            diag="A decision flowchart. Top node: an icon of a main house and a storage shed labeled「附属建物を取り壊した」. A diamond node asks:「変更の内容は、所在の地番の変更・更正、床面積の変更・更正、附属建物の新築のどれかか」. The Yes arrow goes to a red conclusion node:「建物図面を添付する」 (shown faded because it is not this panel's case). The No arrow goes to a green conclusion node:「建物図面の提供を省略できる」, with a small note「残る建物の位置や形状は変わらない」 and a main house drawing that stays the same. No loop arrows; every branch ends in its own conclusion node.",
            callout="まず、申請する変更が所在の地番の変更・更正、床面積の変更・更正、附属建物の新築のどれかにあたるかを確認します。附属建物の取壊しはどれにもあたらないので、建物図面の提供を省略できます。",
            tag="図面の提供は省略可",
            color="green",
        ),
        dict(
            h="床面積の変更では符号以外を全部抹消して書き直す",
            diag="A before-and-after registry-book page of the attached-building column. BEFORE: the 符号 cell is kept in full color; the old 種類, 構造 and 床面積 cells are crossed out with lines. AFTER: new 種類, 構造 and 床面積 cells are all written again. A note beside the 種類 and 構造 cells reads「変わらなくても書き直す」. Three numbered check points run top to bottom: ① what changed (種類, 構造 or 床面積), ② the new 種類・構造・床面積 are all recorded, ③ everything old except the 符号 is erased.",
            callout="まず、変更の対象が附属建物の種類、構造又は床面積のどれかを確認し、次に変更後の種類・構造・床面積の全部を記録し、従前の事項は符号を除いて全部抹消します。種類や構造が変わらなくても同じです。",
            tag="全部書き直す",
            color="green",
        ),
        dict(
            h="同じ種類でも「同上」と略さず全部書く",
            diag="A registry-book page of the attached-building column with two rows. Row 1: 種類「物置」, 構造, 床面積 written out. Row 2, WRONG version drawn faded with a red ✕: a cell containing「同上」. Row 2, CORRECT version drawn in full color with a green check mark: the same 種類「物置」, 構造 and 床面積 written out again in full. A small label beside it reads「直前の記録と同じでも略記しない」.",
            callout="まず、直前に記録された附属建物と同じ種類かどうかを確認します。次に、同じ種類でも「同上」と略さず、種類・構造・床面積をそのまま記録します。",
            tag="同上と略記しない",
            color="green",
        ),
        dict(
            h="抵当権があっても附属建物の新築を登記できる",
            diag="A two-step check drawn from top to bottom with numbered points. ① A main house (甲建物) and a newly built shed (乙建物) next to it, joined by a bracket labeled「効用上一体として利用される」, so that they are treated as one building. ② A mortgage tag labeled「抵当権の設定の登記」 is attached to the main house; the tag sits beside the arrow and does not block it. The arrow continues to a green conclusion node:「附属建物の新築による変更の登記を申請できる」. A faded red ✕ stamp reading「申請できない」 is shown only as the wrong idea.",
            callout="まず、新築した乙建物が甲建物と効用上一体として利用されるかを確認し、次に甲建物に抵当権の登記があっても附属建物の新築を制限する定めがないことを確認します。",
            tag="抵当権は制限にならない",
            color="blue",
        ),
        dict(
            h="附属建物が敷地権付きなら構造欄に記録する",
            diag="A two-step check drawn with numbered points. ① A detached house (区分建物でない甲建物) and a small condominium unit (乙建物) labeled「敷地権付き区分建物」 are shown side by side. ② A registry-book page of the main building: in the attached-building column, the 構造 cell is highlighted with a thick border and contains small items labeled「一棟の建物の所在など」 and「敷地権の内容」. A green check mark is placed on the 構造 cell.",
            callout="まず、甲建物が区分建物でなく、乙建物が敷地権付き区分建物であることを確認します。次に、記録される場所が甲建物の附属建物の表示欄の構造欄であることを確認します。",
            tag="構造欄に敷地権の事項",
            color="blue",
        ),
    ],
    footer="不動産登記令別表の十四の項、不動産登記事務取扱手続準則78条1項・92条・94条1項、不動産登記規則別表二に基づく整理です。",
)

# ---------------------------------------------------------------- 第13問
GUIDE[13] = dict(
    desc="問題文を読んだ瞬間に、「誰が申請するか」「何を申請情報にするか」を見分ける5パネル構成。②の色分け（誰が申請するか＝緑、どう申請するか＝青）を引き継いでいる。",
    field="建物の表題登記",
    icons="isometric icons of a newly built apartment building, a family tree style timeline of owners, an application form with name and share fields, a house with a key icon for a right of residence, and a registry-book page being closed and reopened - adapt the icon set to the topic of who files a building's first registration.",
    shared=None,
    panels=[
        dict(
            h="区分建物は売却後も新築した人が表題部所有者",
            diag="A left-to-right timeline of three steps. ① Person「A」builds an apartment unit and obtains ownership; a registry-book page shows「表題部所有者：A」 with a green check mark. ② A sells the unit to「B」 (an arrow from A to B). ③ B applies for「所有権の保存の登記」 (a second registry-book page with B as the owner). Below step ①, a faded registry-book page with「表題部所有者：B」 and a red ✕ shows the wrong idea.",
            callout="まず、誰が新築して所有権を取得したかを確認し、次にその人を表題部所有者として表題登記をします。その後の売却で所有者が変わっても、買主Bの名義は所有権の保存の登記で取得します。",
            tag="買主の名義は保存登記",
            color="green",
        ),
        dict(
            h="共有の建物の表題登記は共有者1人で申請できる",
            diag="An illustrative diagram. Two brothers「A」 and「B」 stand in front of a jointly owned house. Only A holds an application form that lists both A and B as owners, each with a share field (持分). A faded box labeled「A及びBが共同して申請」 with a red ✕ is shown beside it as the wrong idea. A small note reads「共有物の保存行為にあたる」.",
            callout="まず、建物が共有かどうかを確認し、次に申請人を確認します。共有者の1人が単独で、共有者全員を表題部所有者として申請でき、申請情報には各共有者の持分を記載します。",
            tag="共有者1人で申請可",
            color="green",
        ),
        dict(
            h="配偶者居住権だけの取得者に申請義務はない",
            diag="A decision flowchart for an unregistered house after the owner's death. Two persons stand at the top: son「B」 (obtains the ownership) and mother「C」 (obtains the right of residence by division agreement, shown with a key icon). A diamond node asks for each of them:「建物の所有権を取得した者か」. B's Yes arrow goes to a green conclusion node:「表題登記の申請義務を負う」. C's No arrow goes to its own conclusion node:「申請義務を負わない」. No loop arrows; every branch ends in its own conclusion node.",
            callout="まず、その人が建物の所有権を取得した者かを確認し、次に取得したのが所有権か配偶者居住権かを見分けます。所有権を取得したBが申請義務を負い、配偶者居住権だけのCは負いません。",
            tag="所有権の取得者が義務",
            color="green",
        ),
        dict(
            h="一棟の建物の表示だけの表題登記はできない",
            diag="An isometric apartment building with a one-building card labeled「一棟の建物の表示」 and several unit cards labeled「各区分建物の表示（種類・構造・床面積）」. The two kinds of cards are bound together by one clip labeled「併せて申請」. A faded copy shows only the one-building card being submitted alone, stopped with a red ✕ and a small note「種類が定まらない区分建物があっても、一棟の表示だけの申請はない」.",
            callout="まず、区分建物の表題登記が一棟の建物の表示と各区分建物の表示を合わせて登記するものであることを確認します。次に、同じ一棟に属する他の区分建物の申請と併せて申請します。",
            tag="一棟と区分を併せる",
            color="blue",
        ),
        dict(
            h="保存登記が錯誤で抹消されたら改めて表題登記",
            diag="A top-to-bottom timeline of five numbered steps. ① A person without rights「A」 is registered as the title holder in the 表題部. ② A's 所有権の保存の登記 is made. ③ The 保存の登記 is erased because of a mistake. ④ The registry record is closed (a closed registry-book icon), because A is not restored as the title holder. ⑤ A final green conclusion node:「真実の所有者Bの申請又は職権で、改めて表題登記がされる」.",
            callout="まず、保存の登記が錯誤で抹消されたことを確認し、次にAを表題部所有者に戻さず登記記録が閉鎖されることを確認します。建物は現に存在するので、真実の所有者Bの申請か職権で、改めて表題登記がされます。",
            tag="真の所有者か職権で",
            color="blue",
        ),
    ],
    footer="不動産登記法44条1項・47条1項・48条1項・74条2項、不動産登記令3条9号、民法252条5項に基づく整理です。",
)

# ---------------------------------------------------------------- 第14問
GUIDE[14] = dict(
    desc="問題文を読んだ瞬間に、合体前の建物の登記の状態（表題登記のみか、所有権の登記があるか、名義人は同じか）を見分けて、申請人・登記識別情報・持分を判定する5パネル構成。②の色分け（申請人と識別情報＝緑、持分・附属建物・住所＝青）を引き継いでいる。",
    field="建物の合体による登記等",
    icons="isometric icons of two small buildings merging into one building with a bold arrow, application forms, registry-book pages for each building, a document labeled with an identification-information slip, mortgage tags, and a moving-house icon with an address card - adapt the icon set to the topic of building merger (合体).",
    shared=None,
    panels=[
        dict(
            h="合体の申請人は表題部所有者か登記名義人の一方",
            diag="Two buildings merge into one building by a bold arrow. LEFT building「甲建物」 has a registry-book page marked「表題登記のみ（表題部所有者A）」. RIGHT building「乙建物」 has a registry-book page marked「所有権の登記あり（登記名義人B）」. Below the merged building, one application form box is shown with a label「表題部所有者又は所有権の登記名義人」 and the choice「AかBのどちらか一方」 highlighted with a green check mark. A faded box「AとBが共同して申請」 with a red ✕ is shown as the wrong idea.",
            callout="まず、合体前の建物がそれぞれ表題登記のみか、所有権の登記があるかを確認し、次に申請人を確認します。申請人は「表題部所有者又は所有権の登記名義人」と定められ、どちらか一方で足りるので共同申請ではありません。",
            tag="共同申請ではない",
            color="green",
        ),
        dict(
            h="登記識別情報が1個で足りるのは名義人が同一のとき",
            diag="A decision flowchart. Top node: two buildings with registry-book pages that have merged. A diamond node asks:「合体前の各建物の所有権の登記名義人は同一か」. The Yes arrow goes to a green conclusion node:「いずれか1個の建物の登記識別情報で足りる」 (one identification-information slip). The No arrow goes to its own conclusion node:「それぞれの建物の登記識別情報が必要」 (two slips, labeled A and B). No loop arrows; every branch ends in its own conclusion node.",
            callout="まず、合体前の各建物の所有権の登記名義人が同一かを確認します。次に、同一ならば登記識別情報はいずれか1個で足り、違えばそれぞれの建物の登記識別情報が必要です。",
            tag="名義人が同一なら1個",
            color="green",
        ),
        dict(
            h="存続する抵当権が全て同一なら持分は不要",
            diag="A decision flowchart in a vertical chain. Top box: two buildings of the same owner merge, and the mortgage registrations of the old buildings continue on the merged building. Then four diamond nodes in a row going down, each asking whether the item is the same for all continuing mortgages: ①「登記の目的は同一か」, ②「受付の年月日及び受付番号は同一か」, ③「登記原因及びその日付は同一か」, ④「登記名義人は同一か」. Each Yes arrow goes down to the next diamond; the last Yes arrow goes to a green conclusion node:「持分は申請情報に不要」. Each No arrow goes sideways into one shared conclusion node:「原則どおり、同一でないとみなした場合の持分を申請情報にする」. No loop arrows.",
            callout="まず、合体前の建物の抵当権の登記が合体後も存続するかを確認し、次に登記の目的、受付の年月日及び受付番号、登記原因及びその日付、登記名義人の四つがすべて同一かを確認します。すべて同一なら持分を申請情報にしなくて構いません。",
            tag="持分は書かなくてよい",
            color="blue",
        ),
        dict(
            h="主である建物と附属建物がつながっても合体ではない",
            diag="A main house with its attached shed, both enclosed in one bracket labeled「すでに1個の建物」, then joined by a newly built connecting corridor. Next to the corridor, a faded「合体」 stamp with a red ✕. A bold arrow leads to a green conclusion node:「建物の表題部の変更の登記」 (a registry-book page where the floor area is rewritten).",
            callout="まず、つながった建物がすでに主である建物と附属建物として1個の建物かを確認します。1個の建物なら合体にはならず、増築した床面積などは表題部の変更の登記として申請します。",
            tag="変更の登記で足りる",
            color="blue",
        ),
        dict(
            h="住所変更の登記なしで合体の登記等を申請できる",
            diag="A left-to-right flow. LEFT: a registry-book page showing an old address and a resident certificate showing a new address. A dotted bypass arrow skips a faded box「住所の変更の登記」 (marked as not needed, with a red ✕). The main arrow goes to the right: an application form for「合体による登記等」 with an attached document labeled「変更があったことを証する情報」 and a green check mark.",
            callout="まず、所有権の登記名義人の住所に変更があるかを確認し、次に変更があったことを証する情報を添付情報として提供します。住所の変更の登記を先にする必要はありません。",
            tag="変更を証する情報を添付",
            color="blue",
        ),
    ],
    footer="不動産登記法49条1項・51条、不動産登記令8条・別表の十三の項に基づく整理です。",
)

# ---------------------------------------------------------------- 第15問
GUIDE[15] = dict(
    desc="問題文を読んだ瞬間に、「何を併せて申請するか」「誰が」「いつまでに」「何を添えて」申請するかを見分ける5パネル構成。『誤っているもの』を選ぶ問題だが、各パネルは肢の正しいルールを示している。②の色分け（申請の組合せと添付情報＝緑、申請人・期限・承諾＝青）を引き継いでいる。",
    field="建物の表題部の変更の登記",
    icons="isometric icons of an existing shop building with a newly built unit on top, a paper clip binding two application forms, a demolition-and-extension building drawing, an application form with applicant fields, a calendar, and a mortgage tag - adapt the icon set to the topic of changes in a building's 表題部.",
    shared="Every panel teaches the correct rule of its own choice. Do not mark any panel with a 正 or 誤 stamp, and do not draw an overall answer.",
    panels=[
        dict(
            h="区分建物になる変更は新築の表題登記と併せて申請",
            diag="An isometric drawing: an existing one-story shop (a building that is not a section of a divided building) with a newly built unit attached to it, forming one building. Below, two application forms,「既存の建物の表題部の変更の登記」 and「新築した区分建物の表題登記」, are held together by one clip labeled「併せて申請」. A green check mark sits on the clip.",
            callout="まず、既存の建物に接続して区分建物が新築され、既存の建物が区分建物になったかを確認します。次に、既存の建物の表題部の変更の登記を、新築した区分建物の表題登記と併せて申請します。",
            tag="併せて申請する",
            color="green",
        ),
        dict(
            h="取壊しと増築を同時にしたら増築部分の所有権を証明",
            diag="Four numbered steps from left to right. ① A building with a part being demolished (dotted outline, 10 square meters). ② A new part being added (colored, 6 square meters). ③ The total floor area decreases as a result (a down arrow). ④ A document stack labeled「増築部分の所有権を証する情報」 (examples drawn as small icons: 確認済証, 検査済証, 工事完了引渡証明書) with a green check mark, attached only to the new part.",
            callout="まず、増築した部分があるかを確認し、次に全体の床面積が減っていても、増築部分について所有権を有することを証する情報が要ることを確認します。",
            tag="床面積が減っても必要",
            color="green",
        ),
        dict(
            h="代理人が申請しても未成年者の氏名と住所を書く",
            diag="An application form drawn large. The applicant field is highlighted with a thick border and filled with「未成年者の氏名・住所」 (a child icon), with a green check mark. Below it, a separate field labeled「代理人の氏名・住所」 (a surveyor icon, with a note that the parents are the ones who entrusted the agent). A small arrow shows that the agent files on behalf of the applicant, but the applicant field stays with the minor.",
            callout="まず、申請人は誰かを確認します。申請人は所有権の登記名義人である未成年者なので、その氏名と住所を申請情報にし、次に代理人の氏名と住所も別に記載します。",
            tag="申請人は未成年者",
            color="blue",
        ),
        dict(
            h="期限は所有権の登記名義人になった日から1か月",
            diag="A decision flowchart. Top: a timeline with a building partly demolished, then a purchase by the buyer. A diamond node asks:「自分への所有権の移転の登記がされたか」. The Yes arrow goes to a green conclusion node:「その登記があった日から1か月以内に変更の登記を申請」 (a calendar with the registration day circled). The No arrow goes to its own conclusion node:「まだ登記名義人ではなく、申請義務は生じていない」. A faded calendar on the purchase day with a red ✕ and a note「取得した日から1か月ではない」 is placed beside the timeline. No loop arrows; every branch ends in its own conclusion node.",
            callout="まず、自分への所有権の移転の登記がされて所有権の登記名義人になったかを確認します。次に、名義人になった日から1か月以内かを数え、取得した日は起算日にしません。",
            tag="登記の日から1か月",
            color="blue",
        ),
        dict(
            h="床面積が減る変更の登記に抵当権者の承諾は要らない",
            diag="A building with a mortgage tag labeled「抵当権の登記」, part of it demolished (dotted outline, floor area decreases). Beside it, a checklist of the attached information for a 表題部's change of registration (令別表の十四の項), with items such as 図面 and 所有権を証する情報 ticked. A slot labeled「抵当権者の承諾を証する情報」 is drawn faded and empty with a red ✕, to show that this item is not in the list.",
            callout="まず、建物の表題部の変更の登記の添付情報を定める令別表の十四の項に、抵当権者の承諾を証する情報が含まれているかを確認します。含まれていないので、床面積が減少しても承諾は要りません。",
            tag="承諾は要らない",
            color="blue",
        ),
    ],
    footer="不動産登記法51条2項・52条1項、不動産登記令3条・別表の十四の項に基づく整理です。",
)
