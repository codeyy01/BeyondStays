import re

# 1. HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modal_html = """
    <!-- Package Details Modal -->
    <div id="pkgModal" class="pkg-modal">
        <div class="pkg-modal-overlay" id="pkgModalOverlay"></div>
        <div class="pkg-modal-content">
            <button class="pkg-modal-close" id="pkgModalClose">&times;</button>
            <div id="pkgModalBody" class="pkg-modal-body">
                <!-- Dynamic Content -->
            </div>
            <div class="pkg-modal-footer">
                <a href="#" id="pkgModalWaBtn" target="_blank" class="pkg-modal-wa-btn">
                    <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.487-1.761-1.66-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                    Book via WhatsApp
                </a>
            </div>
        </div>
    </div>
"""

# Insert modal before closing body tag
if 'id="pkgModal"' not in html:
    html = html.replace('</body>', modal_html + '\n</body>')

html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=16', html)
html = re.sub(r'script\.js\?v=[0-9]+', 'script.js?v=9997', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. CSS
css = """
/* =========================================
   PACKAGE MODAL SHOWCASE
   ========================================= */
.pkg-modal {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    z-index: 99999;
    display: flex; align-items: center; justify-content: center;
    opacity: 0; visibility: hidden;
    transition: opacity 0.3s ease, visibility 0.3s;
}
.pkg-modal.active {
    opacity: 1; visibility: visible;
}
.pkg-modal-overlay {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(10, 20, 10, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}
.pkg-modal-content {
    position: relative;
    background: var(--cream);
    width: 90%; max-width: 650px;
    max-height: 85vh;
    border-radius: 28px;
    z-index: 100000;
    display: flex; flex-direction: column;
    transform: translateY(30px) scale(0.95);
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 30px 60px rgba(0,0,0,0.3);
    overflow: hidden;
}
.pkg-modal.active .pkg-modal-content {
    transform: translateY(0) scale(1);
}
.pkg-modal-close {
    position: absolute;
    top: 20px; right: 20px;
    background: rgba(255,255,255,0.9);
    border: none;
    width: 44px; height: 44px;
    border-radius: 50%;
    font-size: 28px;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    z-index: 10;
    transition: transform 0.2s, background 0.2s;
    display: flex; align-items: center; justify-content: center;
    color: #111;
}
.pkg-modal-close:hover { transform: scale(1.1); background: #fff; }

.pkg-modal-body {
    padding: 40px;
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: var(--green) transparent;
}
.pkg-modal-body::-webkit-scrollbar { width: 6px; }
.pkg-modal-body::-webkit-scrollbar-thumb { background: var(--green); border-radius: 6px; }

.pkg-m-title { font-family: var(--font-display); font-size: 2.8rem; color: var(--green); margin-bottom: 8px; line-height: 1.1; }
.pkg-m-subtitle { font-family: var(--font-body); font-size: 1.2rem; color: var(--text-muted); margin-bottom: 20px; font-weight: 500; }
.pkg-m-desc { font-size: 1rem; color: #444; line-height: 1.6; margin-bottom: 24px; }

.pkg-m-meta { display: flex; gap: 20px; margin-bottom: 32px; font-weight: 600; color: #111; font-size: 1.05rem; background: #fff; padding: 16px 20px; border-radius: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); }
.pkg-m-meta span { display: flex; align-items: center; gap: 8px; }
.pkg-m-meta svg { width: 20px; height: 20px; fill: var(--green); }

.pkg-m-section { margin-bottom: 32px; }
.pkg-m-section h4 { font-family: var(--font-body); font-size: 1.3rem; color: #111; margin-bottom: 16px; border-bottom: 2px solid rgba(18, 53, 0, 0.08); padding-bottom: 8px; display: inline-block;}

.pkg-m-list { list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
@media (max-width: 600px) { .pkg-m-list { grid-template-columns: 1fr; } }
.pkg-m-list li { display: flex; align-items: flex-start; gap: 10px; font-size: 1rem; color: #333; line-height: 1.4; }
.pkg-m-list li svg { flex-shrink: 0; width: 18px; height: 18px; margin-top: 3px; }
.pkg-m-list li.incl svg { fill: #2e7d32; }
.pkg-m-list li.excl svg { fill: #d32f2f; }

.pkg-m-note { background: rgba(212, 168, 83, 0.15); border-left: 4px solid var(--gold); padding: 16px; margin-top: 24px; border-radius: 0 8px 8px 0; font-size: 0.95rem; color: #444; line-height: 1.6;}

.pkg-modal-footer {
    padding: 24px 40px;
    background: #fff;
    border-top: 1px solid rgba(0,0,0,0.05);
}
.pkg-modal-wa-btn {
    display: flex; align-items: center; justify-content: center; gap: 10px;
    width: 100%;
    background: #25D366;
    color: #fff;
    padding: 16px;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1.15rem;
    text-decoration: none;
    transition: background 0.3s, transform 0.2s;
    box-shadow: 0 8px 20px rgba(37, 211, 102, 0.3);
}
.pkg-modal-wa-btn:hover { background: #1ebe57; transform: translateY(-2px); box-shadow: 0 12px 25px rgba(37, 211, 102, 0.4); }

/* Force hide any stray scrollbars globally for sliders just in case */
.packages-slider::-webkit-scrollbar, .packages-slider-container::-webkit-scrollbar { display: none !important; }
"""

with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css + '\n')

# 3. JS
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# We need to hook the click event on `.pkg-btn` to open the modal.
# Since `.pkg-btn` are generated dynamically, we can use event delegation on `slider`.
js_addition = """
    // Package Modal Logic
    const pkgModal = document.getElementById('pkgModal');
    const pkgModalClose = document.getElementById('pkgModalClose');
    const pkgModalOverlay = document.getElementById('pkgModalOverlay');
    const pkgModalBody = document.getElementById('pkgModalBody');
    const pkgModalWaBtn = document.getElementById('pkgModalWaBtn');

    if (slider && pkgModal) {
        slider.addEventListener('click', (e) => {
            const btn = e.target.closest('.pkg-btn');
            if (btn) {
                e.preventDefault();
                const card = btn.closest('.pkg-card');
                const idx = Array.from(slider.children).indexOf(card);
                if (idx > -1 && window.allPackagesData[idx]) {
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

    function openPkgModal(pkg) {
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
        // If description contains "Condition:-" or "Heavy Snowfall", extract it as a note
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
            <h2 class="pkg-m-title">${pkg.placeName}</h2>
            <div class="pkg-m-subtitle">${pkg.name}</div>
            
            <div class="pkg-m-meta">
                <span><svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/><path d="M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg> ${pkg.duration}</span>
                <span><svg viewBox="0 0 24 24"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.41l9 9c.36.36.86.58 1.41.58s1.05-.22 1.41-.59l7-7c.36-.36.59-.86.59-1.41s-.23-1.06-.59-1.41zM5.5 7C4.67 7 4 6.33 4 5.5S4.67 4 5.5 4 7 4.67 7 5.5 6.33 7 5.5 7z"/></svg> from ${pkg.price}</span>
            </div>

            <p class="pkg-m-desc">${mainDesc}</p>
            ${noteHtml}
            ${highlightsHtml}
            ${incExcHtml}
        `;

        const waMsg = `Hi Beyondstays! I am interested in the ${pkg.name} package at ${pkg.placeName}. Can you share more details?`;
        pkgModalWaBtn.href = `https://wa.me/919999999999?text=${encodeURIComponent(waMsg)}`;

        pkgModal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
"""

if 'const pkgModal = document.getElementById' not in js:
    js += '\n' + js_addition

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Modal implemented successfully!")
