import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

burger_fix = '''
/* Ensure hamburger is green to match the green logo on mobile */
@media (max-width: 768px) {
    .hamburger span {
        background: var(--green) !important;
    }
}
'''
css += burger_fix

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
