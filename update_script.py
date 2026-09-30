import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Pattern to remove renderPlaces, renderPackages, generatePackageHTML, renderFilters
pattern_remove_old = r'function renderPlaces.*?function\s+openModal'
js_before = re.split(pattern_remove_old, js, flags=re.DOTALL)[0]
js_after = 'function openModal' + re.split(pattern_remove_old, js, flags=re.DOTALL)[1]

new_js = '''
function renderModernPackages() {
    const slider = document.getElementById('packagesSlider');
    if (!slider) return;
    slider.innerHTML = '';
    
    // Flatten all packages
    let allPackages = [];
    travelData.forEach(placeObj => {
        if(placeObj.packages) {
            placeObj.packages.forEach(pkg => {
                allPackages.push({
                    ...pkg,
                    placeName: placeObj.place,
                    coverImage: placeObj.coverImage,
                    region: placeObj.region
                });
            });
        }
    });
    
    // If no packages, show message
    if (allPackages.length === 0) {
        slider.innerHTML = '<p style="color:#777; margin: auto;">No packages available.</p>';
        return;
    }
    
    // Generate cards
    allPackages.forEach((pkg, index) => {
        // Randomize rating and level slightly for aesthetic variety based on index
        const rating = (4.7 + (index % 4) * 0.1).toFixed(1);
        const levels = ['Easy Level', 'Moderate Level', 'Premium Level'];
        const levelClasses = ['easy', 'moderate', 'hard'];
        const levelIdx = index % 3;
        
        const card = document.createElement('div');
        card.className = 'pkg-card';
        card.innerHTML = `
            <!-- Top Image Section -->
            <div class="pkg-img-wrap">
                <img src="${pkg.coverImage}?auto=compress&cs=tinysrgb&w=600" alt="${pkg.name}" loading="lazy" />
                <div class="pkg-img-overlay"></div>
                
                <div class="pkg-badges">
                    ${pkg.region === 'International' ? '<span class="pkg-badge">Popular</span>' : ''}
                    <div class="pkg-heart">♡</div>
                </div>
                
                <div class="pkg-title-area">
                    <div class="pkg-title">
                        <h3>${pkg.name}</h3>
                        <div class="pkg-location">
                            <svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                            ${pkg.placeName}
                        </div>
                    </div>
                    <button class="pkg-route-btn" onclick="openModal('${pkg.id}', '${pkg.placeName}')">View Details ↗</button>
                </div>
            </div>
            
            <!-- Bottom Stats Section -->
            <div class="pkg-stats-grid">
                <div class="pkg-stat">
                    <span>Price</span>
                    <strong>${pkg.price}</strong>
                </div>
                <div class="pkg-stat">
                    <span>Duration</span>
                    <strong>${pkg.duration.split(' ')[0]} ${pkg.duration.split(' ')[1]}</strong>
                </div>
                <div class="pkg-stat">
                    <span>Type</span>
                    <strong>${pkg.region}</strong>
                </div>
                
                <div class="pkg-stat" style="grid-column: span 2;">
                    <span>${levels[levelIdx]}</span>
                    <div class="pkg-level-bar">
                        <div class="pkg-level-fill ${levelClasses[levelIdx]}" style="width: ${70 + (index*10)%30}%"></div>
                    </div>
                </div>
                <div class="pkg-stat">
                    <span>Rating</span>
                    <div class="pkg-rating">
                        ${rating} 
                        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                    </div>
                </div>
            </div>
        `;
        slider.appendChild(card);
    });
}

'''

final_js = js_before + new_js + '\n\n' + js_after

# Also need to replace the init calls!
final_js = final_js.replace('renderPlaces();', 'renderModernPackages();')
final_js = final_js.replace('renderFilters();', '')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(final_js)
