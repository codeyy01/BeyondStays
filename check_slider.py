with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('class="packages-slider-container"')
end = text.find('</section>', start)
print(text[start:end])
