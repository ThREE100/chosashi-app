const { chromium } = require('playwright');
(async () => {
  const out = process.argv[2];
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1100, height: 1400 } });
  const blocked = new Set();
  await p.route('**/*', r => { const u = new URL(r.request().url()); if (u.hostname === 'localhost') return r.continue(); blocked.add(u.hostname); return r.abort(); });
  await p.goto('http://localhost:4173/learning-manga-generator/');
  await p.waitForTimeout(1500);
  await p.screenshot({ path: out + '/01_top.png', fullPage: true });
  const btns = await p.locator('button').allInnerTexts(); console.log('buttons:', btns.join(' | ').slice(0, 800));
  const s = p.getByText('サンプル', { exact: false }).first();
  if (await s.count()) { await s.click(); await p.waitForTimeout(1500); await p.screenshot({ path: out + '/02_sample.png', fullPage: true }); }
  console.log('blocked external hosts:', [...blocked].join(', '));
  console.log((await p.locator('body').innerText()).slice(0, 1500));
  await b.close();
})();
