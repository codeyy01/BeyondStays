import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the goTesti interval and next button logic
new_js = '''
    tPrev.addEventListener('click', () => {
        const maxIndex = total - (window.innerWidth < 768 ? 1 : 2);
        goTesti(testiIdx > 0 ? testiIdx - 1 : maxIndex);
    });
    tNext.addEventListener('click', () => {
        const maxIndex = total - (window.innerWidth < 768 ? 1 : 2);
        goTesti(testiIdx < maxIndex ? testiIdx + 1 : 0);
    });

    buildDots();
    setInterval(() => {
        const maxIndex = total - (window.innerWidth < 768 ? 1 : 2);
        goTesti(testiIdx < maxIndex ? testiIdx + 1 : 0);
    }, 5000);
'''

# Use regex to replace the old event listeners and interval
js = re.sub(
    r"\$\('tPrev'\)\.addEventListener.*?setInterval\(\(\) => goTesti.*?5000\);",
    new_js.strip(),
    js,
    flags=re.DOTALL
)

# Also fix the maxIndex logic inside goTesti itself to be responsive
js = re.sub(
    r'const visibleCards = 2;\s*const maxIndex = total - visibleCards;',
    r'const visibleCards = window.innerWidth < 768 ? 1 : 2;\n        const maxIndex = Math.max(0, total - visibleCards);',
    js
)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("JS slider logic fixed.")
