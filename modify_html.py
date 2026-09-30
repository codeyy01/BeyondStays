import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add hamburger to navbar-scrolled
hamburger_html = '''
                    <button class="hamburger" aria-label="Menu">
                        <span></span><span></span>
                    </button>
                </div>
            </nav>'''
html = re.sub(r'</ul>\s*</div>\s*</nav>', '</ul>\n' + hamburger_html, html, count=1)

# Add mobile-break to hero title
html = re.sub(r'<div class="hero-giant-title">\s*DISCOVER\s*INDIA\s*</div>', '<div class="hero-giant-title">DISCOVER<br class="mobile-break">INDIA</div>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML modified.")
