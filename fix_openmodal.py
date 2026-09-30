import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

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

# Replace openModal
js = re.sub(r'function openModal\(pkg, place\).*?(?=function closeModal\(\))', new_openmodal + '\n\n', js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
