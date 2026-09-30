const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({headless: 'new'});
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', error => console.log('PAGE ERROR:', error.message));

  await page.goto('http://localhost:8080', { waitUntil: 'networkidle0' });
  
  console.log('Testing next button...');
  const activeIdx1 = await page.evaluate(() => {
      const slides = document.querySelectorAll('#heroSlides .hero-slide');
      return Array.from(slides).findIndex(s => s.classList.contains('active'));
  });
  console.log('Active index 1:', activeIdx1);

  await page.click('#heroNext');
  await page.waitForTimeout(500);

  const activeIdx2 = await page.evaluate(() => {
      const slides = document.querySelectorAll('#heroSlides .hero-slide');
      return Array.from(slides).findIndex(s => s.classList.contains('active'));
  });
  console.log('Active index 2:', activeIdx2);

  await browser.close();
})();
