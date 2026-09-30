with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to find all occurrences of `<div class="about-mobile-cards">`
# and its closing tag, and remove all but the first one.

start_marker = '            <!-- Mobile About Cards (Visible only on max-width: 768px) -->'
end_marker = '            </div>\n' # The closing tag of about-mobile-cards

# Let's use string splitting!
parts = html.split(start_marker)

# parts[0] is everything before the FIRST mobile cards block.
# parts[1] is the FIRST mobile cards block onwards.
# parts[2] is the SECOND mobile cards block onwards...

if len(parts) > 2:
    print(f"Found {len(parts) - 1} occurrences. Cleaning up...")
    
    # We want to keep parts[0] + start_marker + parts[1]
    # But for parts[2], parts[3], etc., we need to remove the block!
    
    new_html = parts[0] + start_marker + parts[1]
    
    for i in range(2, len(parts)):
        # parts[i] starts with the content of the mobile cards block.
        # We need to find where this block ends.
        # Looking at my injected HTML, the block ends with `            </div>`
        # But `parts[i]` might contain multiple `</div>`.
        # Let's find the exact string that follows the block in my injection:
        # My injection was `</div>\n` + html_mobile_cards + `\n        </div>\n    </section>`
        # Actually, the block itself ends with `<div class="mobile-pill-text">...</div>\n                </div>\n            </div>`
        
        # A safer way: I know EXACTLY what I injected. Let's just find the substring and replace it from the right!
        pass

# Better approach: Regex to find the whole block
import re
# The block starts with <!-- Mobile About Cards and ends with the last </div> of the cards.
# Since it contains exactly 5 inner cards, we can just match it non-greedily up to the ` Authentic Backwaters ` card's closing tags.
block_regex = r'(\s*<!-- Mobile About Cards \(Visible only on max-width: 768px\) -->.*?Tranquil Kerala backwaters\.</p>\s*</div>\s*</div>\s*</div>)'

matches = re.findall(block_regex, html, flags=re.DOTALL)
print(f"Found {len(matches)} blocks via regex.")

if len(matches) > 1:
    # Keep the first match, remove the rest!
    # We can do this by splitting the html by the exact first match.
    first_match = matches[0]
    
    # Replace all occurrences with empty string
    html_cleaned = html.replace(first_match, '')
    
    # Wait! If I replace ALL occurrences, I lose the first one too!
    # I need to insert it back into the right place.
    # Where was it? Right after the closing tag of `.about-right`.
    # Let's find the about section.
    
    # Actually, a simpler way is `html.replace(first_match, '', html.count(first_match) - 1)`
    # Wait, python string replace takes `count` as max replacements from the LEFT!
    # So `html.replace(first_match, '', len(matches) - 1)` will replace the FIRST N-1 occurrences!
    # That deletes the one in the About section and leaves the one in the Contact section! We want the OPPOSITE!
    pass

# BEST APPROACH:
# Split the string using the regex.
splits = re.split(block_regex, html, flags=re.DOTALL)
# splits will be: [text_before_1, match_1, text_between_1_and_2, match_2, text_between_2_and_3, ...]
if len(splits) > 3:
    new_html = splits[0] + splits[1] # Keep the first one!
    for i in range(2, len(splits)):
        if i % 2 == 0:
            # text between matches
            new_html += splits[i]
        else:
            # match itself - DO NOT ADD IT!
            pass
    
    # Update cache
    new_html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=9', new_html)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Cleanup successful!")
else:
    print("Regex failed to find multiple blocks.")
