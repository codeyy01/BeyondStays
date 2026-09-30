import re

with open('fetchData_recovered_full2.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# The text contains line numbers like '195: ', we need to strip them
lines = text.split('\n')
clean_lines = []
for line in lines:
    clean_line = re.sub(r'^\d+:\s?', '', line)
    clean_lines.append(clean_line)

clean_text = '\n'.join(clean_lines)

# Find from async function fetchData() to just before function initTestimonials()
match = re.search(r'(async function fetchData\(\) \{[\s\S]*?)(?=function initTestimonials\(\))', clean_text)
if match:
    recovered_code = match.group(1)
    with open('recovered_block.js', 'w', encoding='utf-8') as f:
        f.write(recovered_code)
    print("Recovered block successfully!")
else:
    print("Could not find block boundaries.")
