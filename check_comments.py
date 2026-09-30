with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

starts = css.count('/*')
ends = css.count('*/')
print(f"/* count: {starts}, */ count: {ends}")
