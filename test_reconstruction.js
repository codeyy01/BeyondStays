const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800 });
  await page.goto('file:///C:/Users/lenovo/OneDrive/Desktop/Beyondstays/index.html');
  await new Promise(r => setTimeout(r, 2000));
  await page.screenshot({ path: 'reconstructed_desktop.png' });
  
  await page.setViewport({ width: 375, height: 812 });
  await page.goto('file:///C:/Users/lenovo/OneDrive/Desktop/Beyondstays/index.html');
  await new Promise(r => setTimeout(r, 2000));
  await page.screenshot({ path: 'reconstructed_mobile.png' });
  
  await browser.close();
})();
