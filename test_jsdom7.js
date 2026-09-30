const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('index.html', 'utf-8');
const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on('log', function (message) {
  console.log('BROWSER LOG:', message);
});
virtualConsole.on('error', function (message) {
  console.error('BROWSER ERROR:', message);
});

const dom = new JSDOM(html, { runScripts: "dangerously", resources: "usable", virtualConsole });

dom.window.addEventListener('load', () => {
    setTimeout(() => {
        try {
            console.log('Manually calling initHero...');
            dom.window.eval('initHero()');
            const next = dom.window.document.getElementById('heroNext');
            if (next) {
                console.log('Clicking next...');
                next.click();
            }
        } catch (e) {
            console.error('Error during execution:', e);
        }
    }, 1000);
});
