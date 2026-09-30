import re

with open('rebuild_hero_final.py', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'new_hero_css = \"\"\"(.*?)\"\"\"', content, flags=re.DOTALL)
perfect_hero = match.group(1)

with open('style_backup.css', 'r', encoding='utf-16') as f:
    backup_css = f.read()

# Strip any hero block that was injected previously
backup_css = re.sub(r'/\* =========================================\s*PIXEL-PERFECT HERO & NAVBAR \(Rebuild\)\s*========================================= \*/.*?/\* ── Reset ── \*/', '/* ── Reset ── */', backup_css, flags=re.DOTALL)
backup_css = re.sub(r'/\* ── Layout & Typography ── \*/.*?/\* ── Reset ── \*/', '/* ── Reset ── */', backup_css, flags=re.DOTALL)


reset_idx = backup_css.find('/* ── Reset ── */')
if reset_idx != -1:
    final_css = backup_css[:reset_idx] + perfect_hero + '\n' + backup_css[reset_idx:]
else:
    final_css = perfect_hero + '\n' + backup_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(final_css)

print('Restored styles and merged perfect hero!')
