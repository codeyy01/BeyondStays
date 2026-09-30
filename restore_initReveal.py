import re

initReveal_code = '''
/* SCROLL REVEAL */
function initReveal() {
    const obs = new IntersectionObserver(entries => {
        entries.forEach(en => {
            if (en.isIntersecting) {
                en.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right').forEach(el => obs.observe(el));
}
'''

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Insert it before fetchData
js = js.replace('async function fetchData()', initReveal_code + '\nasync function fetchData()')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
