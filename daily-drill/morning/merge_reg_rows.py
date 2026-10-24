"""morning/reg_rows/AM-NNN.json（作成の担当が書いた登録簿の行）を registry.json に取り込む（並行して作るとき registry.json の書き換えが衝突しないように）。
使い方: python3 daily-drill/morning/merge_reg_rows.py"""
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
rp = os.path.join(ROOT, 'registry.json')
reg = json.load(open(rp, encoding='utf-8'))
n = 0
for fp in sorted(glob.glob(os.path.join(HERE, 'reg_rows', 'AM-*.json'))):
    row = json.load(open(fp, encoding='utf-8'))
    row['side'] = 'morning'
    reg[os.path.basename(fp)[:-5]] = row
    n += 1
json.dump(reg, open(rp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{n}行を registry.json に取り込み')
