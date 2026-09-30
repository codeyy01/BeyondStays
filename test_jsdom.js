const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('index.html', 'utf-8');
const dom = new JSDOM(html, { runScripts: "dangerously", resources: "usable" });

dom.window.addEventListener('load', () => {
    try {
        console.log('DOM loaded. Checking hero slides...');
        const slides = dom.window.document.querySelectorAll('.hero-slide');
        console.log('Slides found:', slides.length);
        const next = dom.window.document.getElementById('heroNext');
        if (next) {
            console.log('Clicking next...');
            next.click();
            console.log('Active slide index:', Array.from(slides).findIndex(s => s.classList.contains('active')));
        }
    } catch (e) {
        console.error('Error during execution:', e);
    }
});
