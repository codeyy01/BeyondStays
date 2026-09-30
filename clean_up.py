import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Completely remove ALL if() if() garbage
js = re.sub(r'(if\(\)\s*)+', '', js)

# Now manually add protections for specific elements safely
js = js.replace("$('contactForm').addEventListener", "if($('contactForm')) $('contactForm').addEventListener")
js = js.replace("$('modalClose').addEventListener", "if($('modalClose')) $('modalClose').addEventListener")
js = js.replace("$('modalOverlay').addEventListener", "if($('modalOverlay')) $('modalOverlay').addEventListener")
js = js.replace("$('waClose').addEventListener", "if($('waClose')) $('waClose').addEventListener")
js = js.replace("$('waPopup').addEventListener", "if($('waPopup')) $('waPopup').addEventListener")
js = js.replace("$('waFab').addEventListener", "if($('waFab')) $('waFab').addEventListener")
js = js.replace("$('btt').addEventListener", "if($('btt')) $('btt').addEventListener")
js = js.replace("$('hamburger').addEventListener", "if($('hamburger')) $('hamburger').addEventListener")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
