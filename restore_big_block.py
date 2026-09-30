import re

with open('fetchData_recovered_full2.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Strip out line numbers
lines = text.split('\n')
clean_lines = []
for line in lines:
    clean_line = re.sub(r'^\d+:\s?', '', line)
    clean_lines.append(clean_line)

clean_text = '\n'.join(clean_lines)

# Find the exact boundaries: from 'async function fetchData()' up to just before 'function initTestimonials()'
match = re.search(r'(async function fetchData\(\) \{[\s\S]*?)(?=function initTestimonials\(\))', clean_text)

if match:
    recovered_code = match.group(1)
    
    with open('script.js', 'r', encoding='utf-8') as f:
        js = f.read()
    
    # Inject it before initTestimonials
    if 'async function fetchData()' not in js:
        js = js.replace('function initTestimonials() {', recovered_code + '\nfunction initTestimonials() {')
        with open('script.js', 'w', encoding='utf-8') as f:
            f.write(js)
        print("Recovered block successfully injected!")
    else:
        print("fetchData is already there? Something is wrong.")
else:
    print("Could not find block boundaries.")
