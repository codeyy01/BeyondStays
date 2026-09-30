const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('index.html', 'utf-8');
const dom = new JSDOM(html, { runScripts: "dangerously", resources: "usable" });

dom.window.onerror = function(msg) {
    console.log('GLOBAL ERROR:', msg);
};

dom.window.addEventListener('load', () => {
    setTimeout(() => {
        console.log('Script loaded? heroIdx:', dom.window.heroIdx);
    }, 1000);
});
