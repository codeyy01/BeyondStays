import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Store allPackages globally
# Replace `const allPackages = [];` inside renderModernPackages with `window.allPackagesData = [];`
# Wait, let's just make sure allPackages inside renderModernPackages is accessible.
# Actually, I'll just change `const allPackages = [];` to `window.allPackagesData = [];` and `allPackages.push` to `window.allPackagesData.push`.
js = js.replace('const allPackages = [];', 'window.allPackagesData = [];\n    const allPackages = window.allPackagesData;')

# 2. Change onclick to openModal(i)
old_img = r'<div class="pkg-img-wrap" style="cursor:pointer;" onclick="bookPackageWa(\'${pkg.placeName}\', \'${pkg.name}\')">'
new_img = r'<div class="pkg-img-wrap" style="cursor:pointer;" onclick="openModal(${i})">'
js = js.replace(old_img, new_img)

old_arrow = r'<div class="pkg-arrow-btn" onclick="event.stopPropagation(); bookPackageWa(\'${pkg.placeName}\', \'${pkg.name}\')">&#8599;</div>'
new_arrow = r'<div class="pkg-arrow-btn" onclick="event.stopPropagation(); openModal(${i})">&#8599;</div>'
js = js.replace(old_arrow, new_arrow)

# 3. Modify openModal
old_openmodal = r'function openModal\(pkg, place\).*?// Book Now\s*// document\.getElementById\(\'bookBtn\'\)\.addEventListener.*?\}\);'

new_openmodal = '''function openModal(index) {
    const pkg = window.allPackagesData[index];
    if (!pkg) return;
    
    // Stop auto-slide
    if (window.packageAutoSlide) {
        clearInterval(window.packageAutoSlide);
    }
    
    // Populate Modal
    const modalTitle = document.getElementById('modalTitle');
    const modalBadges = document.getElementById('modalBadges');
    const modalMeta = document.getElementById('modalMeta');
    const modalDesc = document.getElementById('modalDesc');
    const modalHighlights = document.getElementById('modalHighlights');
    const modalInclusions = document.getElementById('modalInclusions');
    const modalExclusions = document.getElementById('modalExclusions');
    const modalBookBtn = document.getElementById('modalBookBtn');
    
    modalTitle.textContent = pkg.name;
    
    modalBadges.innerHTML = `
        <span class="modal-badge-place">${pkg.placeName}</span>
        ${pkg.region === 'International' ? '<span class="modal-badge-pop">Popular</span>' : ''}
    `;
    
    modalMeta.innerHTML = `
        <span class="modal-meta-item">⏱️ ${pkg.duration}</span>
        <span class="modal-meta-item">💰 ${pkg.price}</span>
    `;
    
    // Description (handle bolding and newlines)
    let desc = pkg.description || '';
    desc = desc.replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
    desc = desc.replace(/\\n/g, '<br/>');
    modalDesc.innerHTML = desc;
    
    // Highlights
    if (pkg.highlights && pkg.highlights.length > 0) {
        document.getElementById('modalHighlightsSec').style.display = 'block';
        modalHighlights.innerHTML = pkg.highlights.map(h => `<li>${h}</li>`).join('');
    } else {
        document.getElementById('modalHighlightsSec').style.display = 'none';
    }
    
    // Inclusions
    if (pkg.inclusions && pkg.inclusions.length > 0) {
        document.getElementById('modalInclusionsSec').style.display = 'block';
        modalInclusions.innerHTML = pkg.inclusions.map(i => `<li>${i}</li>`).join('');
    } else {
        document.getElementById('modalInclusionsSec').style.display = 'none';
    }
    
    // Exclusions
    if (pkg.exclusions && pkg.exclusions.length > 0) {
        document.getElementById('modalExclusionsSec').style.display = 'block';
        modalExclusions.innerHTML = pkg.exclusions.map(e => `<li>${e}</li>`).join('');
    } else {
        document.getElementById('modalExclusionsSec').style.display = 'none';
    }
    
    // Book Btn Action
    modalBookBtn.onclick = () => {
        bookPackageWa(pkg.placeName, pkg.name);
    };
    
    // Show Modal
    const overlay = document.getElementById('modalOverlay');
    overlay.classList.remove('hidden');
    requestAnimationFrame(() => {
        overlay.classList.add('visible');
        document.body.style.overflow = 'hidden'; // prevent background scrolling
    });
}
'''
js = re.sub(r'function openModal\(pkg, place\).*?(?=function renderPlaces)', new_openmodal + '\n', js, flags=re.DOTALL)

# Add logic to resume auto-slide when modal closes
js = js.replace("document.body.style.overflow = '';", '''document.body.style.overflow = '';
        // Restart auto-slide
        if (window.packageAutoSlide) clearInterval(window.packageAutoSlide);
        const slider = document.getElementById('packagesSlider');
        if (slider) {
            window.packageAutoSlide = setInterval(() => {
                const card = slider.querySelector('.pkg-card');
                if (!card) return;
                const cardWidth = card.offsetWidth + 24;
                const maxScroll = slider.scrollWidth - slider.clientWidth;
                if (slider.scrollLeft >= maxScroll - 10) {
                    slider.scrollTo({ left: 0, behavior: 'smooth' });
                } else {
                    slider.scrollBy({ left: cardWidth, behavior: 'smooth' });
                }
            }, 6000);
        }''')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
