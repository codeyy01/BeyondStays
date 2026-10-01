const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const html = fs.readFileSync('index.html', 'utf8');

const dom = new JSDOM(html);
const dest = dom.window.document.getElementById('destinations');

function traverse(el, indent) {
    if (el.tagName && el.tagName !== 'SVG' && el.tagName !== 'PATH' && !el.classList.contains('pkg-card')) {
        let classes = el.className || '';
        let id = el.id || '';
        let str = indent + '<' + el.tagName.toLowerCase();
        if (id) str += ' id="' + id + '"';
        if (classes) str += ' class="' + classes + '"';
        str += '>';
        console.log(str);
        for (let child of el.children) {
            traverse(child, indent + '  ');
        }
    }
}
traverse(dest, '');
