import json

with open(r'C:\Users\lenovo\.gemini\antigravity\brain\83b01f36-1797-4155-a46a-f3533e362465\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        try:
            obj = json.loads(line)
            if 'tool_calls' in obj:
                for call in obj['tool_calls']:
                    # We are looking for where the entire script.js was read or written previously.
                    # Or we can just search 'content' in any PLANNER_RESPONSE
                    pass
        except:
            pass

# Let's just find the text block that contains 'async function fetchData()' and evaluate its string literal
with open('fetchData_recovered_full2.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace literal \r\n with actual newlines
text = text.replace('\\r\\n', '\n').replace('\\n', '\n').replace('\\t', '\t')

# Also remove line numbers if they exist like 195: 
import re
text = re.sub(r'(?m)^\d+:\s?', '', text)

with open('clean_recovered.js', 'w', encoding='utf-8') as f:
    f.write(text)
