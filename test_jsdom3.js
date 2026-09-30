const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('index.html', 'utf-8');
const dom = new JSDOM(html, { runScripts: "dangerously", resources: "usable" });

dom.window.addEventListener('load', () => {
    setTimeout(() => {
        try {
            console.log('Is window.requestIdleCallback polyfilled?', !!dom.window.requestIdleCallback);
            console.log('Is window.heroIdx defined?', typeof dom.window.heroIdx !== 'undefined' ? dom.window.heroIdx : 'no');
            const next = dom.window.document.getElementById('heroNext');
            console.log('Next button exists?', !!next);
            // manually trigger the logic inside script.js if possible
            // But we can just check if heroTimer exists on window
            console.log('heroTimer exists?', typeof dom.window.heroTimer !== 'undefined' ? dom.window.heroTimer !== null : 'no');
        } catch (e) {
            console.error('Error during execution:', e);
        }
    }, 500);
});
