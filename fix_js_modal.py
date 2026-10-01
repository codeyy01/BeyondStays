import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# I will find the block starting with `// Package Modal Logic` and ending at the end of the file, and replace it completely!

modal_logic_start = js.find('// Package Modal Logic')
if modal_logic_start != -1:
    js = js[:modal_logic_start] # truncate everything from there to end

new_js = """
// Package Modal Logic
document.addEventListener('DOMContentLoaded', () => {
    const pkgModal = document.getElementById('pkgModal');
    const pkgModalClose = document.getElementById('pkgModalClose');
    const pkgModalOverlay = document.getElementById('pkgModalOverlay');
    const pkgModalBody = document.getElementById('pkgModalBody');
    const pkgModalWaBtn = document.getElementById('pkgModalWaBtn');
    const modalSlider = document.getElementById('packagesSlider');

    if (modalSlider && pkgModal) {
        modalSlider.addEventListener('click', (e) => {
            const btn = e.target.closest('.pkg-btn');
            if (btn) {
                e.preventDefault();
                const card = btn.closest('.pkg-card');
                const idx = Array.from(modalSlider.children).indexOf(card);
                if (idx > -1 && window.allPackagesData && window.allPackagesData[idx]) {
                    openPkgModal(window.allPackagesData[idx]);
                }
            }
        });

        const closeModal = () => {
            pkgModal.classList.remove('active');
            document.body.style.overflow = '';
        };

        pkgModalClose.addEventListener('click', closeModal);
        pkgModalOverlay.addEventListener('click', closeModal);
    }
});

function openPkgModal(pkg) {
    const pkgModal = document.getElementById('pkgModal');
    const pkgModalBody = document.getElementById('pkgModalBody');
    const pkgModalWaBtn = document.getElementById('pkgModalWaBtn');
    
    let highlightsHtml = '';
    if (pkg.highlights && pkg.highlights.length > 0) {
        highlightsHtml = `
            <div class="pkg-m-section">
                <h4>Highlights</h4>
                <ul class="pkg-m-list">
                    ${pkg.highlights.map(h => `<li class="incl"><svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> ${h.replace(/^[✓✔] /, '')}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    let incExcHtml = '';
    if ((pkg.inclusions && pkg.inclusions.length > 0) || (pkg.exclusions && pkg.exclusions.length > 0)) {
        incExcHtml = `<div class="pkg-m-section"><h4>Inclusions & Exclusions</h4><ul class="pkg-m-list">`;
        if (pkg.inclusions) {
            pkg.inclusions.forEach(inc => {
                incExcHtml += `<li class="incl"><svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> ${inc.replace(/^[✓✔] /, '')}</li>`;
            });
        }
        if (pkg.exclusions) {
            pkg.exclusions.forEach(exc => {
                incExcHtml += `<li class="excl"><svg viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg> ${exc.replace(/^[✖✖] /, '')}</li>`;
            });
        }
        incExcHtml += `</ul></div>`;
    }

    let noteHtml = '';
    let mainDesc = pkg.description || '';
    if (mainDesc.includes('Condition:-')) {
        const parts = mainDesc.split('Condition:-');
        mainDesc = parts[0];
        noteHtml = `<div class="pkg-m-note"><strong>Important Note:</strong><br>${parts[1]}</div>`;
    } else if (mainDesc.includes('Heavy Snowfall')) {
        const parts = mainDesc.split('Heavy Snowfall');
        mainDesc = parts[0];
        noteHtml = `<div class="pkg-m-note"><strong>Heavy Snowfall Condition:</strong><br>${parts[1]}</div>`;
    }

    pkgModalBody.innerHTML = `
        <h2 class="pkg-m-title">${pkg.placeName || pkg.name}</h2>
        <div class="pkg-m-subtitle">${pkg.name}</div>
        
        <div class="pkg-m-meta">
            <span><svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/><path d="M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg> ${pkg.duration || 'Custom Duration'}</span>
            <span><svg viewBox="0 0 24 24"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.41l9 9c.36.36.86.58 1.41.58s1.05-.22 1.41-.59l7-7c.36-.36.59-.86.59-1.41s-.23-1.06-.59-1.41zM5.5 7C4.67 7 4 6.33 4 5.5S4.67 4 5.5 4 7 4.67 7 5.5 6.33 7 5.5 7z"/></svg> from ${pkg.price || 'Ask Price'}</span>
        </div>

        <p class="pkg-m-desc">${mainDesc}</p>
        ${noteHtml}
        ${highlightsHtml}
        ${incExcHtml}
    `;

    const waMsg = `Hi Beyondstays! I am interested in the ${pkg.name} package. Can you share more details?`;
    pkgModalWaBtn.href = `https://wa.me/919999999999?text=${encodeURIComponent(waMsg)}`;

    pkgModal.classList.add('active');
    document.body.style.overflow = 'hidden';
}
"""

js += new_js

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'script\.js\?v=[0-9]+', 'script.js?v=9999', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
