import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_init = '''document.addEventListener('DOMContentLoaded', () => {
    requestIdleCallback(() => {
        initHero();
        initTestimonials();
        fetchData();
        fetchFAQ();
        initReveal();
    });
});'''

new_init = '''document.addEventListener('DOMContentLoaded', () => {
    // Fallback for Safari which doesn't support requestIdleCallback
    const runInit = () => {
        initHero();
        initTestimonials();
        fetchData();
        fetchFAQ();
        initReveal();
    };
    if (window.requestIdleCallback) {
        requestIdleCallback(runInit);
    } else {
        setTimeout(runInit, 1);
    }
});'''

js = js.replace(old_init, new_init)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
