"""第1回の台本から、ネーム（ラフなコマ割り）と作画指示書の画像を作る。
ネームは「下書きの指示」で、完成画像に文字を重ねるものではない。"""
from PIL import Image, ImageDraw, ImageFont
from source import ITEM
F = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
def font(n): return ImageFont.truetype(F, n)
def wrap(t, n):
    return [t[i:i+n] for i in range(0, len(t), n)]
def page(pi, instructions=False, W=1080, H=1920):
    p = ITEM['pages'][pi]
    im = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(im)
    if instructions:
        d.text((24, 12), '指示書', font=font(36), fill='red')
    top, gap = 70, 24; ph = (H - top - 40 - gap*2) // 3
    for j, pn in enumerate(p['panels']):
        y0 = top + j*(ph+gap); x0, x1 = 40, W-40
        d.rectangle((x0, y0, x1, y0+ph), outline='black', width=6)
        # 人物の位置：左＝生徒、右＝先生
        d.ellipse((x0+40, y0+ph-300, x0+220, y0+ph-120), outline='black', width=3)
        d.rectangle((x0+70, y0+ph-120, x0+190, y0+ph-10), outline='black', width=3)
        d.ellipse((x1-240, y0+ph-280, x1-40, y0+ph-60), outline='black', width=3)
        # 中央：図の枠
        d.rectangle((x0+260, y0+ph-230, x1-280, y0+ph-40), outline='gray', width=2)
        for k, (who, t) in enumerate(pn['talk']):
            bx = x0+30 if who == 'S' else W//2 + 10
            by = y0+20 + k*130
            bw = W//2 - 70
            d.rounded_rectangle((bx, by, bx+bw, by+110), radius=40, outline='black', width=3, fill='white')
            tx = x0+130 if who == 'S' else x1-140
            d.line((bx+bw//2, by+110, tx, y0+ph-300), fill='black', width=3)
            for li, line in enumerate(wrap(t, 16)[:3]):
                d.text((bx+24, by+14+li*30), line, font=font(26), fill='black')
        if instructions:
            d.text((x0+50, y0+ph-340), 'Student（左）', font=font(26), fill='red')
            d.text((x1-250, y0+ph-320), 'Teacher（右）', font=font(26), fill='red')
            for li, line in enumerate(wrap('図：' + pn['fig'], 40)[:7]):
                d.text((x0+270, y0+ph-225+li*26), line, font=font(19), fill='blue')
            for li, line in enumerate(wrap(pn['mood'], 48)[:2]):
                d.text((x0+250, y0+ph-300+li*28), line, font=font(21), fill='red')
            d.text((W-120, y0+8), f'{"①②③"[j]}', font=font(40), fill=(230, 80, 160))
    return im
if __name__ == '__main__':
    import sys
    out = sys.argv[1]
    for i in range(3):
        page(i).save(f'{out}/name{i+1:02d}.png')
        page(i, True).save(f'{out}/instructions{i+1:02d}.png')
