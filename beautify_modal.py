import re

# ================================
# 1. Update script.js
# ================================
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# I need to completely replace the innerHTML injection in `openPkgModal`
# Wait, I'll just write a script to replace the entire `openPkgModal` function!
new_openPkgModal = '''function openPkgModal(pkg) {
    const pkgModal = document.getElementById('pkgModal');
    const pkgModalBody = document.getElementById('pkgModalBody');
    const pkgModalWaBtn = document.getElementById('pkgModalWaBtn');
    
    if (window.packageAutoSlide) clearInterval(window.packageAutoSlide);
    
    let highlightsHtml = '';
    if (pkg.highlights && pkg.highlights.length > 0) {
        highlightsHtml = `
            <div class="pkg-m-section">
                <h4>✨ Trip Highlights</h4>
                <ul class="pkg-m-list">
                    ${pkg.highlights.map(h => `<li class="incl"><svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> ${h.replace(/^[✓✔] /, '')}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    let incExcHtml = '';
    if ((pkg.inclusions && pkg.inclusions.length > 0) || (pkg.exclusions && pkg.exclusions.length > 0)) {
        incExcHtml = `<div class="pkg-m-section"><h4>✅ Inclusions & ❌ Exclusions</h4><ul class="pkg-m-list">`;
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
        noteHtml = `<div class="pkg-m-note"><svg viewBox="0 0 24 24"><path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/></svg> <div><strong>Important Note:</strong><br>${parts[1]}</div></div>`;
    } else if (mainDesc.includes('Heavy Snowfall')) {
        const parts = mainDesc.split('Heavy Snowfall');
        mainDesc = parts[0];
        noteHtml = `<div class="pkg-m-note"><svg viewBox="0 0 24 24"><path d="M12 2L1 21h22L12 2zm1 14h-2v-2h2v2zm0-4h-2v-4h2v4z"/></svg> <div><strong>Heavy Snowfall Condition:</strong><br>${parts[1]}</div></div>`;
    }

    let imgUrl = 'https://images.pexels.com/photos/1371360/pexels-photo-1371360.jpeg';
    if (pkg.images && pkg.images.length > 0) {
        imgUrl = pkg.images[0];
    } else if (pkg.coverImage) {
        imgUrl = pkg.coverImage;
    } else if (pkg.placeName && pkg.placeName.toLowerCase().includes('goa')) {
        imgUrl = 'https://images.pexels.com/photos/1032650/pexels-photo-1032650.jpeg';
    } else if (pkg.placeName && pkg.placeName.toLowerCase().includes('kashmir')) {
        imgUrl = 'https://images.pexels.com/photos/5409673/pexels-photo-5409673.jpeg';
    } else if (pkg.placeName && pkg.placeName.toLowerCase().includes('kasol')) {
        imgUrl = 'https://images.pexels.com/photos/258421/pexels-photo-258421.jpeg';
    } else if (pkg.placeName && pkg.placeName.toLowerCase().includes('manali')) {
        imgUrl = 'https://images.pexels.com/photos/1032650/pexels-photo-1032650.jpeg';
    }

    pkgModalBody.innerHTML = `
        <div class="pkg-m-hero" style="background-image: url('${imgUrl}');">
            <div class="pkg-m-hero-overlay"></div>
            <div class="pkg-m-hero-content">
                <h2 class="pkg-m-title">${pkg.placeName || pkg.name}</h2>
                <div class="pkg-m-subtitle">${pkg.name}</div>
            </div>
        </div>
        
        <div class="pkg-m-details">
            <div class="pkg-m-meta-row">
                <div class="pkg-m-meta-item">
                    <div class="icon-wrap"><svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/><path d="M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg></div>
                    <div>
                        <small>Duration</small>
                        <strong>${pkg.duration || 'Custom'}</strong>
                    </div>
                </div>
                <div class="pkg-m-meta-item">
                    <div class="icon-wrap"><svg viewBox="0 0 24 24"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.41l9 9c.36.36.86.58 1.41.58s1.05-.22 1.41-.59l7-7c.36-.36.59-.86.59-1.41s-.23-1.06-.59-1.41zM5.5 7C4.67 7 4 6.33 4 5.5S4.67 4 5.5 4 7 4.67 7 5.5 6.33 7 5.5 7z"/></svg></div>
                    <div>
                        <small>Starting from</small>
                        <strong>${pkg.price || 'Ask Price'}</strong>
                    </div>
                </div>
            </div>

            <p class="pkg-m-desc">${mainDesc}</p>
            ${noteHtml}
            ${highlightsHtml}
            ${incExcHtml}
        </div>
    `;

    const waMsg = `Hi Beyondstays! I am interested in the ${pkg.name} package. Can you share more details?`;
    pkgModalWaBtn.href = `https://wa.me/919999999999?text=${encodeURIComponent(waMsg)}`;

    pkgModal.classList.add('active');
    document.body.style.overflow = 'hidden';
}'''

# Replace the old function
js = re.sub(r'function openPkgModal\(pkg\).*?document\.body\.style\.overflow = \'hidden\';\n}', new_openPkgModal, js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

# ================================
# 2. Update style_ultimate.css
# ================================
with open('style_ultimate.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace modal CSS completely
old_modal_css = r'/\* =========================================\n   PACKAGE MODAL SHOWCASE\n   ========================================= \*/.*?/\* Force hide any stray scrollbars globally for sliders just in case \*/'

new_modal_css = '''/* =========================================
   PACKAGE MODAL SHOWCASE (BEAUTIFIED & LAG-FREE)
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
    background: rgba(0, 0, 0, 0.85); /* Removed backdrop-filter to fix massive lag */
}
.pkg-modal-content {
    position: relative;
    background: #ffffff;
    width: 92%; max-width: 600px;
    max-height: 85vh;
    border-radius: 24px;
    z-index: 100000;
    display: flex; flex-direction: column;
    transform: translateY(40px) scale(0.95);
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.15);
    box-shadow: 0 40px 80px rgba(0,0,0,0.4);
    overflow: hidden;
    will-change: transform, opacity;
}
.pkg-modal.active .pkg-modal-content {
    transform: translateY(0) scale(1);
}
.pkg-modal-close {
    position: absolute;
    top: 16px; right: 16px;
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255,255,255,0.4);
    color: #fff;
    width: 36px; height: 36px;
    border-radius: 50%;
    font-size: 24px;
    cursor: pointer;
    z-index: 10;
    display: flex; align-items: center; justify-content: center;
    transition: background 0.3s, transform 0.3s;
}
.pkg-modal-close:hover { background: #fff; color: #111; transform: scale(1.1); }

.pkg-modal-body {
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: var(--green) transparent;
}
.pkg-modal-body::-webkit-scrollbar { width: 6px; }
.pkg-modal-body::-webkit-scrollbar-thumb { background: var(--green); border-radius: 6px; }

.pkg-m-hero {
    position: relative;
    height: 240px;
    background-size: cover;
    background-position: center;
    display: flex; align-items: flex-end;
    padding: 30px;
}
.pkg-m-hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.2) 60%, transparent 100%);
}
.pkg-m-hero-content {
    position: relative;
    z-index: 2;
    color: #fff;
}
.pkg-m-title { font-family: var(--font-display); font-size: 2.5rem; color: #fff; margin-bottom: 4px; line-height: 1.1; letter-spacing: -0.5px;}
.pkg-m-subtitle { font-family: var(--font-body); font-size: 1.1rem; color: rgba(255,255,255,0.8); font-weight: 500; }

.pkg-m-details {
    padding: 30px;
}

.pkg-m-meta-row {
    display: flex;
    gap: 16px;
    margin-bottom: 24px;
}
.pkg-m-meta-item {
    flex: 1;
    background: #f8f9fa;
    border-radius: 16px;
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 12px;
    border: 1px solid rgba(0,0,0,0.04);
}
.pkg-m-meta-item .icon-wrap {
    width: 40px; height: 40px;
    background: rgba(18, 53, 0, 0.08);
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
}
.pkg-m-meta-item svg { width: 20px; height: 20px; fill: var(--green); }
.pkg-m-meta-item small { display: block; font-size: 0.8rem; color: #666; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;}
.pkg-m-meta-item strong { display: block; font-size: 1.1rem; color: #111; font-weight: 700; margin-top: 2px;}

.pkg-m-desc { font-size: 1rem; color: #444; line-height: 1.7; margin-bottom: 32px; }

.pkg-m-section { margin-bottom: 32px; }
.pkg-m-section h4 { font-family: var(--font-body); font-size: 1.25rem; color: #111; margin-bottom: 16px; font-weight: 700;}

.pkg-m-list { list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
@media (max-width: 600px) { .pkg-m-list { grid-template-columns: 1fr; } }
.pkg-m-list li { display: flex; align-items: flex-start; gap: 10px; font-size: 0.95rem; color: #333; line-height: 1.5; font-weight: 500;}
.pkg-m-list li svg { flex-shrink: 0; width: 20px; height: 20px; margin-top: 2px; }
.pkg-m-list li.incl svg { fill: #2e7d32; }
.pkg-m-list li.excl svg { fill: #d32f2f; }

.pkg-m-note { 
    background: #fff4e5; 
    border-left: 4px solid #ff9800; 
    padding: 16px; 
    margin-bottom: 32px; 
    border-radius: 8px; 
    font-size: 0.95rem; 
    color: #b26a00; 
    line-height: 1.6;
    display: flex;
    gap: 12px;
}
.pkg-m-note svg { width: 24px; height: 24px; fill: #ff9800; flex-shrink: 0; margin-top: 2px;}
.pkg-m-note strong { color: #8a5200; font-size: 1rem; display: block; margin-bottom: 4px;}

.pkg-modal-footer {
    padding: 20px 30px;
    background: #fff;
    border-top: 1px solid rgba(0,0,0,0.05);
}
.pkg-modal-wa-btn {
    display: flex; align-items: center; justify-content: center; gap: 10px;
    width: 100%;
    background: #25D366;
    color: #fff;
    padding: 18px;
    border-radius: 16px;
    font-weight: 700;
    font-size: 1.1rem;
    text-decoration: none;
    transition: background 0.3s, transform 0.2s;
}
.pkg-modal-wa-btn:hover { background: #1ebe57; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(37, 211, 102, 0.3); }

/* Force hide any stray scrollbars globally for sliders just in case */'''

css = re.sub(old_modal_css, new_modal_css, css, flags=re.DOTALL)

with open('style_ultimate.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'script\.js\?v=[0-9]+', 'script.js?v=10005', html)
html = re.sub(r'style_ultimate\.css\?v=[0-9]+', 'style_ultimate.css?v=22', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
