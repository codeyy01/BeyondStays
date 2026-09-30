import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix windowif
js = re.sub(r'window(if\(\)\s*)+\.addEventListener', 'window.addEventListener', js)

# Fix hamburgerif
js = re.sub(r'hamburger(if\(\)\s*)+\.addEventListener', 'hamburger.addEventListener', js)

# Replace all .addEventListener with if() protection
js = js.replace("contactForm.addEventListener", "if(contactForm) contactForm.addEventListener")
js = js.replace("modalClose.addEventListener", "if(modalClose) modalClose.addEventListener")
js = js.replace("modalOverlay.addEventListener", "if(modalOverlay) modalOverlay.addEventListener")
js = js.replace("waClose.addEventListener", "if(waClose) waClose.addEventListener")
js = js.replace("waPopup.addEventListener", "if(waPopup) waPopup.addEventListener")
js = js.replace("waFab.addEventListener", "if(waFab) waFab.addEventListener")
js = js.replace("btt.addEventListener", "if(btt) btt.addEventListener")

# Clean up any duplicated if(...)
js = re.sub(r'(if\(\$\(\'[^\']+\'\)\)\s*){2,}', lambda m: m.group(1), js)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
