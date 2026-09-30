import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

bad_btt = '''btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));'''

good_btt = '''const btt = btt;
if (btt) {
    btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}'''

js = js.replace(bad_btt, good_btt)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
