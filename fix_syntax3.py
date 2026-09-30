import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# The string ends with Hello dY< ... 4 or something.
# We will just replace from modalBookBtn.onclick to the end of the block right before initTestimonials.
js = re.sub(r'// BOOK BUTTON[\s\S]*?(?=function initTestimonials\(\))', '''// BOOK BUTTON
    modalBookBtn.onclick = () => {
        openWaPage("Hello, I want to book " + pkg.name + " in " + place);
    };
}
''', js)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
