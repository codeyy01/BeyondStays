import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the trailing backslash or corrupted template strings
# I will just replace the specific broken message blocks completely.
bad_msg1 = '''//         const msg = Hello, I want to book a package:\
\
dY"? Destination: \\
dY" Package: \\
dY' Price: \\
? Duration: \\
\
dY"? \\
\
Please share more details.;'''

good_msg1 = '''//         const msg = Hello, I want to book a package:\\n\\nDestination: \\\nPackage: \\\nPrice: \\\nDuration: \\\n\\n\\\n\\nPlease share more details.;'''

js = js.replace(bad_msg1, good_msg1)

# Also fix the un-commented modalBookBtn.onclick
# The text from transcript got truncated around "dY' Price: \n4"
# I will just use a regex to replace everything from "modalBookBtn.onclick = () => {" to the end of that function.
js = re.sub(r'modalBookBtn\.onclick\s*=\s*\(\)\s*=>\s*\{[^}]*\}', 'modalBookBtn.onclick = () => { openWaPage("Hello, I want to book " + pkg.name); };', js)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
