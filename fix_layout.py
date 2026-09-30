import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

scroll_html = '''
                <div class="hero-giant-title">DISCOVER<br>INDIA</div>
                
                <!-- NEW SCROLL INDICATOR -->
                <div class="scroll-indicator">
                    <div class="scroll-line"></div>
                </div>

                <div class="hero-ui-layer">'''

html = html.replace('''
                <div class="hero-giant-title">DISCOVER<br>INDIA</div>
  
                <div class="hero-ui-layer">''', scroll_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
