with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()
start = text.rfind('mobile-pill-card')
end = text.find('id="destinations"')
print(text[start:end])
