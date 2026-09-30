import re

# 1. Get the perfect hero css
with open('rebuild_hero_final.py', 'r', encoding='utf-8') as f:
    content = f.read()
hero_match = re.search(r'new_hero_css = \"\"\"(.*?)\"\"\"', content, flags=re.DOTALL)
perfect_hero = hero_match.group(1)

# 2. Get the backup CSS (which has the loader, mobile menu, and rest of site)
with open('style_backup.css', 'r', encoding='utf-8', errors='ignore') as f:
    backup = f.read()

# Fix mangled comments
backup = backup.replace('I"A AI"A A', '──')
backup = backup.replace('I"A A', '─')
backup = backup.replace('I"A', '─')
backup = backup.replace('?"?"', '──')

# Extract :root
root_match = re.search(r'(:root\s*\{.*?\})', backup, flags=re.DOTALL)
root_vars = root_match.group(1) if root_match else ''

# Extract everything from Loader onwards
loader_idx = backup.find('/* ── Loader')
if loader_idx == -1:
    # Try finding alternative corrupted comment
    loader_idx = backup.find('Loader')
    if loader_idx != -1:
        loader_idx = backup.rfind('/*', 0, loader_idx)
if loader_idx == -1:
    loader_idx = backup.find('#loader {')

rest_of_css = backup[loader_idx:] if loader_idx != -1 else backup

# Assemble
final_css = '/* ===== Beyondstays style.css ===== */\n' + root_vars + '\n\n' + perfect_hero + '\n\n' + rest_of_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(final_css)

print('Successfully assembled perfect style.css!')
