with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# simple brace counter
level = 0
for i, char in enumerate(css):
    if char == '{':
        level += 1
    elif char == '}':
        level -= 1
    if level < 0:
        print(f"Error: Too many closing braces at index {i}")
        break
        
if level > 0:
    print(f"Error: Missing {level} closing braces!")
elif level == 0:
    print("Braces are balanced.")
