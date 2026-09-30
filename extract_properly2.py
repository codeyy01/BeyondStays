import re

with open('fetchData_recovered_full3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\\r\\n', '\n').replace('\\n', '\n').replace('\\t', '\t')
text = re.sub(r'(?m)^\d+:\s?', '', text)

match = re.search(r'(async function fetchData\(\) \{[\s\S]*?)(?=function initTestimonials\(\))', text)
if match:
    block = match.group(1)
    
    # Let's clean up any weird artifacts at the end if it caught some transcript stuff
    # Wait, the match stops right before function initTestimonials(), so it should be perfect!
    with open('block_to_inject.js', 'w', encoding='utf-8') as f:
        f.write(block)
    print("Found exact boundaries! Wrote to block_to_inject.js")
else:
    print("Still could not find initTestimonials. Dumping full clean text.")
    with open('block_to_inject.js', 'w', encoding='utf-8') as f:
        f.write(text)
