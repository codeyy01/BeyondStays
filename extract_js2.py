import re

with open('fetchData_recovered_full2.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
clean_lines = []
for line in lines:
    clean_line = re.sub(r'^\d+:\s?', '', line)
    clean_lines.append(clean_line)

clean_text = '\n'.join(clean_lines)

with open('recovered_block.js', 'w', encoding='utf-8') as f:
    f.write(clean_text)
