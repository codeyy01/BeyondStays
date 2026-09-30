with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()
print("Backticks:", js.count('`'))
