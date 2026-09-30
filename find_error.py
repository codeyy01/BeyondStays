with open('script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(len(lines)):
    with open('temp.js', 'w', encoding='utf-8') as temp:
        temp.writelines(lines[:i])
    import subprocess
    result = subprocess.run(['node', '-c', 'temp.js'], capture_output=True, text=True)
    if "Unexpected end of input" not in result.stderr:
        pass
    else:
        print(f"Error starts at line {i-1}")
        break
