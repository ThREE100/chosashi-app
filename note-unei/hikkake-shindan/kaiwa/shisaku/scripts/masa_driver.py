"""100-times-ai-manga-drawing を模擬API（mock）で動かし、第1回の3ページを登録→生成→書き出しまで通す。
実APIへは送らない（Config の provider は mock、キーなし）。"""
import json, shutil, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from manga_drawing.config import Config
from manga_drawing.db import connect, initialize, transaction
from manga_drawing import projects, planning
from manga_drawing.worker import Worker
from manga_drawing.web import create_app
from manga_drawing.common import uid, timestamp
from fastapi.testclient import TestClient

S = Path(sys.argv[1]); OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
NEME = S / 'work/neme'
sys.path.insert(0, str(S / 'scripts')); from source import ITEM
inp = S / 'work/masa-input'; shutil.rmtree(inp, ignore_errors=True); inp.mkdir()
for i in range(1, 4):
    shutil.copy(NEME / f'name{i:02d}.png', inp / f'name{i:02d}.png')
    shutil.copy(NEME / f'instructions{i:02d}.png', inp / f'instructions{i:02d}.png')
# キャラクターシートはリポジトリにないので、仮の白紙（ユーザーが実物のシートに差し替える）
F = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc', 28)
for key, label in (('Teacher', '先生のシート（差し替え）'), ('Student', '生徒のシート（差し替え）')):
    im = Image.new('RGB', (600, 800), 'white'); ImageDraw.Draw(im).text((30, 380), label, font=F, fill='red')
    im.save(inp / f'{key}.png')
manifest = {
  'schema_version': 1, 'title': 'ひっかけ診断ノート_01（試作）',
  'characters': [
    {'key': 'Teacher', 'name': 'Teacher', 'images': ['Teacher.png']},
    {'key': 'Student', 'name': 'Student', 'height_cm': 160, 'images': ['Student.png']}],
  'pages': [
    {'number': i + 1, 'name': f'name{i+1:02d}.png', 'instructions': f'instructions{i+1:02d}.png',
     'characters': ['Teacher', 'Student'],
     'directions': [{'marker': '①②③'[j], 'text': f"{pn['mood']}。図：{pn['fig']}"} for j, pn in enumerate(p['panels'])]}
    for i, p in enumerate(ITEM['pages'])]}
(inp / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))

cfg = Config(S / 'work/masa-data', provider='mock', mock_delay=0)
shutil.rmtree(cfg.root, ignore_errors=True); initialize(cfg)
token = projects.create_import(cfg)
for path in inp.glob('*.png'):
    projects.upload(cfg, token, path.name, path.read_bytes())
report = projects.validate_import(cfg, token, manifest)
print('validate:', json.dumps(report, ensure_ascii=False)[:400])
pid = projects.commit_import(cfg, token)['project_id']
# 参照画像の採用（テストと同じ手順。実運用では画面で採用する）
with connect(cfg) as db:
    for ref in projects.references(db, pid):
        if ref['kind'] == 'character':
            db.execute('INSERT OR REPLACE INTO character_reference_selections VALUES(?,?,?,?,?)',
                       (ref['id'], ref['current_revision_id'], None, ref['images'][0], timestamp()))
with transaction(cfg) as db:
    plan = planning.make_plan(cfg, db, pid, {})
for pg in plan['pages']:
    (OUT / f"request_prompt_page{pg['number']}.txt").write_text(pg['snapshot']['prompt'])
print('plan: jobs', plan['jobs'])
planning.start(cfg, pid, plan['plan_token'], uid())
class Clock:
    v = 1_800_000_000.0
    def __call__(self): return self.v
clock = Clock(); w = Worker(cfg, clock)
for _ in range(8):
    w.tick(); clock.v += 3
with TestClient(create_app(cfg), base_url='http://127.0.0.1') as c:
    c.get('/'); c.headers['X-CSRF-Token'] = c.get('/api/session').json()['data']['csrf']
    pages = c.get(f'/api/projects/{pid}/pages').json()
    (OUT / 'pages.json').write_text(json.dumps(pages, ensure_ascii=False, indent=2))
    for pg in pages['data']['items']:
        print(pg['number'], pg['status'], pg['generation_label'])
        r = c.get(f"/api/assets/{pg['thumbnail']}")
        (OUT / f"mock_output_page{pg['number']}.png").write_bytes(r.content)
print('done; data at', cfg.root)
