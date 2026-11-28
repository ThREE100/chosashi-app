const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const out = process.argv[2]; const script = JSON.parse(fs.readFileSync(process.argv[3]));
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 1100, height: 1400 } });
  await ctx.grantPermissions(['clipboard-read', 'clipboard-write']);
  const p = await ctx.newPage();
  await p.route('**/*', r => new URL(r.request().url()).hostname === 'localhost' ? r.continue() : r.abort());
  await p.goto('http://localhost:4173/learning-manga-generator/');
  await p.evaluate(s => localStorage.setItem('learning-manga-storage', JSON.stringify({ state: { script: s, pageCount: 4 }, version: 0 })), script);
  await p.reload(); await p.waitForTimeout(1500);
  console.log((await p.locator('body').innerText()).slice(0, 600));
  for (const label of ['漫画を生成', '画像にする']) { const l = p.getByText(label).last(); if (await l.count()) { await l.click().catch(()=>{}); await p.waitForTimeout(1000); } }
  await p.screenshot({ path: out + '/03_ours.png', fullPage: true });
  const txt = await p.locator('body').innerText(); fs.writeFileSync(out + '/03_ours_text.txt', txt);
  const copies = p.getByText('まとめて', { exact: false });
  console.log('まとめて count', await copies.count());
  const pres = await p.locator('pre, textarea').allInnerTexts().catch(()=>[]);
  const vals = await p.locator('textarea').evaluateAll(es => es.map(e => e.value));
  fs.writeFileSync(out + '/03_prompt_areas.txt', [...pres, ...vals].join('\n\n=====\n\n'));
  console.log('areas', pres.length, vals.length);
  const bundle = p.getByText('をまとめてコピー', { exact: false }).first();
  await bundle.click(); await p.waitForTimeout(500);
  fs.writeFileSync(out + '/04_bundle_prompt_for_chatgpt.txt', await p.evaluate(() => navigator.clipboard.readText()));
  await b.close();
})();
