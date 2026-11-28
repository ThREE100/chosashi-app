"""毎日ドリル 第1日（夜）記述式（PM-01：放射・地積測量図の直線の交点・地積）の学習まんがの台本。
座標・角・距離・答えは evening/problems/PM-01.json から（漫画の数は照合スクリプトがデータと突き合わせる）。
図は figs.py が問題データから作る（fig の kind：mondai＝問題の図、kotae＝答えの図、sub＝一部）。"""
from manga_kata import S, T, tobira, tsumazuki, matome

FIG_W, FIG_H = 944, 661   # 図の枠（縦横比は図の viewBox 1000×700 と同じ）

MANGA = dict(
    day=1, problem='PM-01', catch='観測角は時計回り、地積は切り捨て',
    intro='放射で2点、地積測量図の直線の交点で1点、最後に座標法で地積。ドリルの解き方を、正確な図を入れた漫画で追えるようにしました。',
    header=('毎晩ドリル　漫画で解説', '放射と交点で筆界点を出す', '観測角は時計回り　地積は切り捨て'),
    header_scene='a surveying instrument on a tripod, boundary stakes, and a plot of land seen from above',
    # わざと間違いとして見せる数（データにない数）。答えと同じ数は入れない
    wrong_values=['298.82'],
    # 漫画が名指しする問題文の箇所と、そこに書いてある語（照合スクリプトが確かめる）
    refs=[('conditions', 2, '時計回り'), ('notes', 2, '切り捨て'), ('notes', 3, 'ブロック塀の位置は、筆界の判断に用いない')],
    pages=[
        tobira('3つの点と地積を出す', '点P・Q・Rの座標と、12番の地積は？', '放射で全部出せます！', '……Rも放射で？'),
        dict(caption='図で見る：求める3つの点', aim='問題の図（正確な図）で、与えられた点と求める点を見分ける。',
             layout='Three panels: one tall panel filling the top 60 percent of the page holding an exact figure, a wide panel in the middle, and a short strip at the bottom.',
             panels=[
                 dict(size='tall, top 60 percent', art='A clean panel with only the attached exact figure in it.',
                      narration='12番の土地と、求める3つの点',
                      fig=dict(name='PM-01_mondai', kind='mondai', rect=(40, 110, FIG_W, FIG_H))),
                 dict(size='wide, middle', art='The teacher points up at the figure with one wing; the student leans in.', chars='student left, teacher right',
                      talk=[(T, '黒丸が与えられた点、赤い白丸が求める点'), (S, 'PとQはT1から観測した点ですね')]),
                 dict(size='short strip, bottom', art='The teacher holds up one feather like a pointer.', chars='teacher only',
                      talk=[(T, 'Rは2本の直線の交点。順に出すわ')]),
             ]),
        tsumazuki('T2から反時計回りに引きます！', '待ちなさい！', '【条件】の2を読んで。どっち回り？', '時計回り……足すんだ！',
                  ['水平角は後視T2から時計回り', '足す'],
                  'On the card, an instrument at T1 with an arrow from T2 turning clockwise, drawn in blue; a crossed-out counterclockwise arrow in red.',
                  '観測角の向き'),
        dict(caption='放射で点Pと点Q', aim='放射の式を、表の観測値どおりに書いて答えを出す。',
             layout='Three panels: a wide panel on top, a wide panel in the middle, and a short strip at the bottom.',
             panels=[
                 dict(size='wide, top', art='A clean whiteboard with the formula and its result written in dark navy; the result is highlighted in yellow.',
                      words=['点P ＝ T1 ＋ 10.22∠(arg(T2 − T1) ＋ 339°02′24″)', '541.02 ＋ 400.35i']),
                 dict(size='wide, middle', art='The same whiteboard style with the second formula and its result highlighted in yellow.',
                      words=['点Q ＝ T1 ＋ 8.04∠(arg(T2 − T1) ＋ 220°13′50″)', '540.49 ＋ 416.10i']),
                 dict(size='short strip, bottom', art='The student writes the results; the teacher nods.', chars='student left, teacher right',
                      talk=[(S, '後視の向きに、角を足すだけ！'), (T, '距離と角は表のとおりにね')]),
             ]),
        dict(caption='点Rは2本の直線の交点', aim='ブロック塀ではなく地積測量図の直線で筆界を決め、交点として点Rを出す。',
             layout='Three panels: a short strip on top, one large panel in the middle holding an exact figure, and a wide panel at the bottom.',
             panels=[
                 dict(size='short strip, top', art='The student points at a drawing of a block wall; the teacher shakes his head.', chars='student left, teacher right',
                      talk=[(S, '東の筆界はブロック塀の線ですね？'), (T, '塀は筆界の根拠にしないの')]),
                 dict(size='large, middle', art='A clean panel with only the attached exact figure in it.',
                      narration='直線K1K2と直線SMの交点が点R',
                      fig=dict(name='PM-01_kouten', kind='sub', rect=(40, 380, FIG_W, FIG_H),
                               points=['P', 'Q', 'R', 'S', 'K1', 'K2', 'M'], kinds={'P': 'given', 'Q': 'given'},
                               lines=[dict(a='Q', b='K1', style='solid'), dict(a='K1', b='K2', style='solid'), dict(a='K2', b='R', style='bold'),
                                      dict(a='S', b='M', style='solid'), dict(a='M', b='R', style='bold')])),
                 dict(size='wide, bottom', art='A whiteboard with the result highlighted in yellow; the teacher stands small at the right.', chars='teacher small at right',
                      talk=[(T, '11番と13番・14番の地積測量図の線よ')], words=['点R ＝ 521.62 ＋ 416.49i']),
             ]),
        dict(caption='地積は切り捨て', aim='座標法の結果から地積を出すときの端数の処理を、誤答で確かめる。',
             layout='Three panels: a wide panel on top, two medium panels side by side in the middle, and a wide panel at the bottom.',
             panels=[
                 dict(size='wide, top', art='A whiteboard showing the four points connected in order and the area result.',
                      words=['P→Q→R→Sの順に座標法', '298.8177 ㎡']),
                 dict(size='medium, middle left', art='The student raises her hand confidently.', chars='student only',
                      talk=[(S, '四捨五入して298.82㎡です！')]),
                 dict(size='medium, middle right', art='The bird teacher flaps both wings in a STOP gesture with speed lines; a red cross over 298.82.', chars='teacher only',
                      talk=[(T, '待ちなさい！ 地積は切り捨てよ')], words=['298.82']),
                 dict(size='wide, bottom', art='A clean result card with a blue check mark.', narration='【注】の2：小数第2位未満は切り捨て',
                      words=['地積 298.81 ㎡']),
             ]),
        dict(caption='答えの図', aim='求めた3つの点を、正確な答えの図と座標で確かめる。',
             layout='Two panels: one large panel filling the top 70 percent holding an exact figure, and a wide panel at the bottom.',
             panels=[
                 dict(size='large, top 70 percent', art='A clean panel with only the attached exact figure in it.',
                      narration='赤丸が求めた点（X, Y）',
                      fig=dict(name='PM-01_kotae', kind='kotae', rect=(40, 110, FIG_W, FIG_H),
                               coord_pos={'P': (-24, 52), 'Q': (30, 14), 'R': (30, 52)})),
                 dict(size='wide, bottom', art='The student holds up her answer sheet happily; the teacher gives a wing thumbs-up.', chars='student left, teacher right',
                      talk=[(S, 'Qは直線K1K2の延長上にもある！'), (T, 'そう、それが検算になるの')]),
             ]),
        matome('この問題のポイント',
               ['観測角は後視から時計回りに足す', 'ブロック塀は筆界の根拠にしない', '点Rは2本の地積測量図の直線の交点', '地積は切り捨てて298.81㎡'],
               '向き、根拠、端数。3つを確かめます！', 'それで本番の点の計算も怖くないわ'),
    ],
)
