import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add a font-size fix to the mobile reset
font_fix = '''
    /* Fix giant title size for mobile */
    .hero-giant-title {
        font-size: clamp(4rem, 18vw, 6rem) !important;
    }
}'''

css = css.replace('}\n\n', '}\n') # cleanup
css = css.replace('    }\n}\n', font_fix)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
