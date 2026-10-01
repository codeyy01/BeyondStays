import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the cloudflare obfuscation
html = re.sub(r'<a href=\"/cdn-cgi/l/email-protection[^\"]+\"><span><span class=\"__cf_email__\"[^>]+>\[email&#160;protected\]</span></span></a>', '<a href=\"mailto:hello.beyondstays@gmail.com\">hello.beyondstays@gmail.com</a>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed cloudflare email!')
