with open('script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
with open('debug_lines.txt', 'w', encoding='utf-8') as f:
    f.write('Line 30 context:\n')
    f.write(''.join(lines[10:45]))
    f.write('\nLine 536 context:\n')
    f.write(''.join(lines[516:550]))
