import re

with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will find the two specific blocks I added recently and change 768px to 1024px
# Block 1: /* --- NEW MOBILE HERO REDESIGN --- */
css = css.replace('/* --- NEW MOBILE HERO REDESIGN --- */\n@media (max-width: 768px) {', '/* --- NEW MOBILE HERO REDESIGN --- */\n@media (max-width: 1024px) {')

# Block 2: /* --- MOBILE FIXES BASED ON USER FEEDBACK --- */
css = css.replace('/* --- MOBILE FIXES BASED ON USER FEEDBACK --- */\n@media (max-width: 768px) {', '/* --- MOBILE FIXES BASED ON USER FEEDBACK --- */\n@media (max-width: 1024px) {')

# Block 3: Strict bottom left (from fix_final_polish.py)
# Wait, in fix_final_polish.py, it was appended as:
# @media (max-width: 768px) {
#     /* Strict bottom-left positioning */
# Let's just blindly replace @media (max-width: 768px) { if it's near these comments.
# To be safe, I'll use regex to target the specific block containing 'Strict bottom-left positioning'
css = re.sub(
    r'@media \(max-width: 768px\) \{\s*/\* Strict bottom-left positioning \*/',
    r'@media (max-width: 1024px) {\n    /* Strict bottom-left positioning */',
    css
)

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Tablet breakpoints updated.")
