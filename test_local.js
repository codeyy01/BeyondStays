const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  await page.setViewport({ width: 1280, height: 800 });
  await page.goto('http://localhost:8080/index.html');
  await new Promise(r => setTimeout(r, 3000));
  await page.screenshot({ path: 'reconstructed_desktop_local.png' });
  
  await page.setViewport({ width: 375, height: 812 });
  await page.goto('http://localhost:8080/index.html');
  await new Promise(r => setTimeout(r, 3000));
  await page.screenshot({ path: 'reconstructed_mobile_local.png' });
  
  await browser.close();
})();
