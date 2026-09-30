const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', error => console.log('PAGE ERROR:', error.message));
  
  await page.setViewport({ width: 1280, height: 800 });
  await page.goto('file:///C:/Users/lenovo/OneDrive/Desktop/Beyondstays/index.html', {waitUntil: 'networkidle0'});
  
  await new Promise(r => setTimeout(r, 4000));
  await page.screenshot({ path: 'reconstructed_desktop2.png' });
  
  await browser.close();
})();
