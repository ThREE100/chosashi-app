# R7-Q21-02-08　ChatGPT用プロンプト（プロジェクトの指示を前提。このページ固有の内容だけ）

```text
PAGE: R7-Q21-02-08　（T05 計算ページ／B5+B6）
THIS PAGE'S ONE POINT: 甲土地の面積は559.8503㎡→559㎡で、登記記録の559㎡とぴったり合う

ZONES (top to bottom):
- ZONE z1: y=0, h=70 px, type=tab. Draw a thin dark-navy tab strip with small white text, flush left; text 「第2章：問1 D点は「時計回り」で出す」 (the inner 「」 marks are part of the text).
- ZONE z2: y=70, h=340 px, type=dialogue.
  - 「トリ先生」 appears at the RIGHT as FACES (tiny round face icon only, about 80 px across, no body, no hands); expression T2 (指し示す): explaining: a wing points at the card or figure, the other wing at the side.
  - Bubble 1 of 2 (トリ先生, right): 「A・B・C・D・Eの座標を記憶して、」.
  - Bubble 2 of 2 (トリ先生, right): 「倍面積の式で一気に計算するの」. The part 「倍面積の式」 is highlighted in yellow.
- ZONE z3: y=410, h=420 px, type=calc_card. PLACEHOLDER: one empty light-gray (#E6E6E6) rectangle at x=40, y=430, width=1000, height=380 px, and nothing else in this zone.
- ZONE z4: y=830, h=170 px, type=calc_card. PLACEHOLDER: one empty light-gray (#E6E6E6) rectangle at x=40, y=850, width=1000, height=130 px, and nothing else in this zone.
- ZONE z5: y=1000, h=620 px, type=dialogue.
  - 「藍子」 appears at the LEFT as MID (upper body, about 300 px tall); expression A5 (安堵・達成): relieved and pleased: a big smile, a small cheering fist. Hands: 両手を小さくガッツポーズ（手は2本）.
  - 「トリ先生」 appears at the RIGHT as SMALL (small full-body figure, about 110 px tall); expression T3 (感心): impressed: round eyes, a satisfied nod. SILENT: expression only, no speech bubble.
  - Bubble 1 of 5 (藍子, left): 「iの係数の絶対値を2で割って……」.
  - Bubble 2 of 5 (藍子, left): 「559.8503㎡。」. The part 「559.8503㎡」 is highlighted in yellow.
  - Bubble 3 of 5 (藍子, left): 「畑の地積は1㎡未満を切り捨てるので、」.
  - Bubble 4 of 5 (藍子, left): 「559㎡！」. The part 「559㎡！」 is highlighted in yellow.
  - Bubble 5 of 5 (藍子, left): 「登記記録とぴったりです！」. The part 「登記記録とぴったり」 is highlighted in yellow.
- ZONE z6: y=1620, h=300 px, type=answer_banner. PLACEHOLDER: one empty light-gray (#E6E6E6) rectangle at x=40, y=1640, width=1000, height=260 px, and nothing else in this zone.

FINAL CHECK before rendering: confirm there is exactly ONE page in one vertical column and every zone is in the given order and height; confirm every text string matches the given string exactly, with no extra text anywhere, and that no word or digit is dropped or altered; confirm that these characters are proper Japanese kanji forms: 地 対 登 記 録; confirm that every PLACEHOLDER is a completely empty flat light-gray rectangle of the given position and size, with nothing drawn inside or over it; confirm that no character or speech bubble overlaps a placeholder, and that every bubble tail points at its own speaker (藍子 left, トリ先生 right); confirm that characters are drawn at the specified appearance mode sizes (FACES are tiny face icons, not larger) and silent characters have no bubble; confirm that 藍子 has exactly two arms and two hands with five fingers each and the same hairstyle as in the reference images; confirm that no pink, green, or orange is used, that red appears only where marked, and that no calculator keys are drawn; confirm the background is fully opaque with no transparency or checkerboard.
```
