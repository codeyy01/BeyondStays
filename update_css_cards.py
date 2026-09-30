import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .pkg-title and .pkg-title h3
css = re.sub(
    r'\.pkg-title \{\s*color: #fff;\s*max-width: 60%;\s*\}',
    r'.pkg-title {\n    color: #fff;\n    width: 100%;\n    max-width: 100%;\n}',
    css
)

css = re.sub(
    r'\.pkg-title h3 \{\s*margin: 0 0 4px 0;\s*font-size: 1\.25rem;\s*font-weight: 700;\s*white-space: nowrap;\s*overflow: hidden;\s*text-overflow: ellipsis;\s*\}',
    r'.pkg-title h3 {\n    margin: 0 0 4px 0;\n    font-size: 1.25rem;\n    font-weight: 700;\n    line-height: 1.3;\n}',
    css
)

# Add CSS for the new short sentence
new_desc_css = '''
.pkg-desc-text {
    font-size: 0.75rem;
    color: rgba(255,255,255,0.9);
    margin-top: 6px;
    line-height: 1.4;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
'''
css = css.replace('.pkg-location svg {', new_desc_css + '\n.pkg-location svg {')

# Rename pkg-heart to pkg-arrow (or just keep the class and change contents, let's keep class but add hover)
arrow_css = '''
.pkg-arrow-btn {
    width: 36px;
    height: 36px;
    background: rgba(255,255,255,0.9);
    backdrop-filter: blur(4px);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #111;
    cursor: pointer;
    font-size: 1.2rem;
    transition: transform 0.3s ease, background 0.3s ease;
}
.pkg-arrow-btn:hover {
    background: #fff;
    transform: scale(1.1);
}
'''
css = css.replace('.pkg-heart {', arrow_css + '\n.pkg-heart-old {')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
