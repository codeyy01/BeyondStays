with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
with open('dump.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines):
        if 'id="policy"' in line:
            start = max(0, i-25)
            out.write(''.join(lines[start:i+5]))
