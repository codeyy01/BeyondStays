import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Anoop Kumar
html = re.sub(r'src=\".*?\" alt=\"Anoop Kumar\"', 'src=\"https://ui-avatars.com/api/?name=Anoop+Kumar&background=2e7d32&color=fff&size=128&bold=true\" alt=\"Anoop Kumar\"', html)

# Replace Jasmine
html = re.sub(r'src=\".*?\" alt=\"Jasmine\"', 'src=\"https://ui-avatars.com/api/?name=Jasmine&background=1565c0&color=fff&size=128&bold=true\" alt=\"Jasmine\"', html)

# Replace Ajith G Shankar
html = re.sub(r'src=\".*?\" alt=\"Ajith G Shankar\"', 'src=\"https://ui-avatars.com/api/?name=Ajith+G+Shankar&background=ef6c00&color=fff&size=128&bold=true\" alt=\"Ajith G Shankar\"', html)

# Replace Muraleedharan
html = re.sub(r'src=\".*?\" alt=\"Muraleedharan\"', 'src=\"https://ui-avatars.com/api/?name=Muraleedharan&background=d32f2f&color=fff&size=128&bold=true\" alt=\"Muraleedharan\"', html)

# Replace Misthah Shareef
html = re.sub(r'src=\".*?\" alt=\"Misthah Shareef\"', 'src=\"https://ui-avatars.com/api/?name=Misthah+Shareef&background=6a1b9a&color=fff&size=128&bold=true\" alt=\"Misthah Shareef\"', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed Avatars!')
