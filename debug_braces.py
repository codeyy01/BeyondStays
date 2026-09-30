with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

level = 0
for i, line in enumerate(lines):
    for char in line:
        if char == '{':
            level += 1
        elif char == '}':
            level -= 1
    if level > 2:
        print(f"High level {level} at line {i+1}: {line.strip()}")
