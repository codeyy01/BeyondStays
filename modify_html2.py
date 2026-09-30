import re

desktop_html = '''
<div class="about-desktop hide-on-mobile">
    <div class="about-desk-left reveal-left">
        <div class="desk-eyebrow">&bull; ABOUT BEYONDSTAYS</div>
        <h2 class="desk-title">NOT JUST TRAVEL.<br/>A FEELING.</h2>
        
        <div class="desk-frame-small">
            <!-- Frame for image later -->
        </div>
        
        <p class="desk-body">Beyondstays transforms everyday journeys into curated experiences - thoughtfully shaped, and made to bring warmth to every travel.</p>
        
        <a href="#contact" class="desk-btn">
            DISCOVER BEYONDSTAYS
            <span class="desk-btn-icon">&#8599;</span>
        </a>
    </div>

    <div class="about-desk-right reveal-right">
        <div class="desk-green-card">
            <div class="desk-green-top">
                <div class="desk-frame-main">
                    <div class="desk-frame-dots">
                        <span></span><span></span><span></span><span></span>
                    </div>
                </div>
                <div class="desk-logo-wrap">
                    <img src="./assets/nav-logo-white.png" alt="Beyondstays" />
                </div>
            </div>
            <div class="desk-green-bottom">
                <div class="desk-line"></div>
                <div class="desk-line" style="width: 60%;"></div>
                <div class="desk-line" style="width: 80%;"></div>
            </div>
        </div>
        <div class="desk-sidebar">
            <div class="desk-side-box"></div>
            <div class="desk-side-box"></div>
            <div class="desk-side-box"></div>
            <div class="desk-side-box"></div>
        </div>
    </div>
</div>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacement = desktop_html + '\n' + '<div class="about-mobile hide-on-desktop">\n<div class="about-layout">'
html = html.replace('<div class="about-layout">', replacement)

html = html.replace('</div>\n        </div>\n    </section>\n\n    <section class="section">', '</div>\n        </div>\n        </div>\n    </section>\n\n    <section class="section">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
