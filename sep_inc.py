import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Old logic block
old_logic = r'''    let incExcHtml = '';
    if \(\(pkg\.inclusions && pkg\.inclusions\.length > 0\) \|\| \(pkg\.exclusions && pkg\.exclusions\.length > 0\)\) \{
        incExcHtml = `<div class="pkg-m-section"><h4>✅ Inclusions & ❌ Exclusions</h4><ul class="pkg-m-list">`;
        if \(pkg\.inclusions\) \{
            pkg\.inclusions\.forEach\(inc => \{
                incExcHtml \+= `<li class="incl"><svg viewBox="0 0 24 24"><path d="M9 16\.17L4\.83 12l-1\.42 1\.41L9 19 21 7l-1\.41-1\.41z"/></svg> \$\{inc\.replace\(\/\^\[✓✔\] \/, ''\)\}</li>`;
            \}\);
        \}
        if \(pkg\.exclusions\) \{
            pkg\.exclusions\.forEach\(exc => \{
                incExcHtml \+= `<li class="excl"><svg viewBox="0 0 24 24"><path d="M19 6\.41L17\.59 5 12 10\.59 6\.41 5 5 6\.41 10\.59 12 5 17\.59 6\.41 19 12 13\.41 17\.59 19 19 17\.59 13\.41 12z"/></svg> \$\{exc\.replace\(\/\^\[✖✖\] \/, ''\)\}</li>`;
            \}\);
        \}
        incExcHtml \+= `</ul></div>`;
    \}'''

new_logic = '''    let incHtml = '';
    if (pkg.inclusions && pkg.inclusions.length > 0) {
        incHtml = `<div class="pkg-m-section">
                <h4>✅ What's Included</h4>
                <ul class="pkg-m-list">
                    ${pkg.inclusions.map(inc => `<li class="incl"><svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> <span>${inc.replace(/^[✓✔] /, '')}</span></li>`).join('')}
                </ul>
            </div>`;
    }

    let excHtml = '';
    if (pkg.exclusions && pkg.exclusions.length > 0) {
        excHtml = `<div class="pkg-m-section">
                <h4>❌ What's Excluded</h4>
                <ul class="pkg-m-list excl-list">
                    ${pkg.exclusions.map(exc => `<li class="excl"><svg viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg> <span>${exc.replace(/^[✖✖] /, '')}</span></li>`).join('')}
                </ul>
            </div>`;
    }'''

js = re.sub(old_logic, new_logic, js)
js = js.replace('${incExcHtml}', '${incHtml}\n            ${excHtml}')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'script\.js\?v=[0-9]+', 'script.js?v=10006', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
