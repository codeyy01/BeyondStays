import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add the pseudo-element to desk-logo-box
logo_box_css = '''.desk-logo-box {
    background: #143505;
    border-radius: 0 24px 24px 0;
    padding: 24px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    /* Height must be exactly enough to match the top boundary naturally, flex will do this if not specified, but let's make it a fixed height */
    height: 140px;
    position: relative; /* ADDED */
}

.desk-logo-box::before {
    content: '';
    position: absolute;
    bottom: -24px;
    left: 0;
    width: 24px;
    height: 24px;
    background: radial-gradient(circle at bottom right, transparent 24px, #143505 24px);
    pointer-events: none;
}'''

css = re.sub(r'\.desk-logo-box\s*\{[\s\S]*?height:\s*140px;\n\}', logo_box_css, css)

# 2. Make the about section wider
wider_css = '''
#about .container {
    max-width: 1536px;
    padding: 0 60px;
}
'''
css += wider_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
