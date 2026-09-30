import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the heart with the arrow, and add the sentence.
old_html = r'''                <div class="pkg-badges">
                    \$\{pkg\.region === 'International' \? '<span class="pkg-badge">Popular</span>' : ''\}
                    <div class="pkg-heart">♡</div>
                </div>
                
                <div class="pkg-title-area">
                    <div class="pkg-title">
                        <h3>\$\{pkg\.name\}</h3>
                        <div class="pkg-location">
                            <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                            \$\{pkg\.placeName\}
                        </div>
                    </div>
                </div>'''

new_html = r'''                <div class="pkg-badges">
                    ${pkg.region === 'International' ? '<span class="pkg-badge">Popular</span>' : ''}
                    <div class="pkg-arrow-btn" onclick="openModal('${pkg.id}', '${pkg.placeName}')">&#8599;</div>
                </div>
                
                <div class="pkg-title-area">
                    <div class="pkg-title">
                        <h3>${pkg.name}</h3>
                        <div class="pkg-location">
                            <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                            ${pkg.placeName}
                        </div>
                        <div class="pkg-desc-text">${pkg.description}</div>
                    </div>
                </div>'''

if re.search(old_html.replace('$', r'\$'), js):
    print("Found exact block to replace")
else:
    print("Could not find exact block")

# Let's just do string replace for safety
js = js.replace('''                <div class="pkg-badges">
                    ${pkg.region === 'International' ? '<span class="pkg-badge">Popular</span>' : ''}
                    <div class="pkg-heart">♡</div>
                </div>
                
                <div class="pkg-title-area">
                    <div class="pkg-title">
                        <h3>${pkg.name}</h3>
                        <div class="pkg-location">
                            <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                            ${pkg.placeName}
                        </div>
                    </div>
                </div>''', new_html)


with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
