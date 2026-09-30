import re

with open('rebuild_hero_final.py', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'new_hero_css = \"\"\"(.*?)\"\"\"', content, flags=re.DOTALL)
perfect_hero = match.group(1)

with open('style_git.css', 'r', encoding='utf-8', errors='ignore') as f:
    backup = f.read()

# Extract :root
root_match = re.search(r'(:root\s*\{.*?\})', backup, flags=re.DOTALL)
root_vars = root_match.group(1) if root_match else ''

# Find the start of the loader
loader_idx = backup.find('#loader {')
if loader_idx != -1:
    # Get the line before it (which has the comment)
    comment_idx = backup.rfind('/*', 0, loader_idx)
    if comment_idx != -1:
        loader_idx = comment_idx

rest_of_css = backup[loader_idx:] if loader_idx != -1 else backup

# Assemble
final_css = '/* ===== Beyondstays style.css ===== */\n' + root_vars + '\n\n' + perfect_hero + '\n\n' + rest_of_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(final_css)

print('Successfully assembled perfect style.css from git!')
