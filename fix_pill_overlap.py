import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update image width
css = re.sub(r'\.mob-pill-img\s*\{[^}]*width:\s*65%;[^}]*\}', 
             lambda m: m.group(0).replace('width: 65%;', 'width: 56%;'), css)

# Update content width
css = re.sub(r'\.mob-pill-content\s*\{[^}]*width:\s*35%;[^}]*\}', 
             lambda m: m.group(0).replace('width: 35%;', 'width: 44%;'), css)

# Update pill-left content
css = re.sub(r'\.mob-pill\.pill-left\s+\.mob-pill-content\s*\{[^}]*\}',
             '''.mob-pill.pill-left .mob-pill-content {
    right: 0;
    padding-right: 24px;
    padding-left: 16px;
    align-items: flex-end;
    text-align: right;
}''', css)

# Update pill-right content
css = re.sub(r'\.mob-pill\.pill-right\s+\.mob-pill-content\s*\{[^}]*\}',
             '''.mob-pill.pill-right .mob-pill-content {
    left: 0;
    padding-left: 24px;
    padding-right: 16px;
    align-items: flex-start;
    text-align: left;
}''', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
