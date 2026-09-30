async function fetchData() {
    try {
        const res = await fetch('data.json');
        if (!res.ok) throw new Error();
        travelData = await res.json();
    } catch {
        travelData = getFallbackData();
    }
    buildRegionFilters();
    renderPlaces();
}

function getFallbackData() {
    return [
        {
            place: 'Munnar', region: 'Resorts', tagline: 'Tea Gardens & Misty Hills',
            coverImage: 'https://images.pexels.com/photos/32262519/pexels-photo-32262519.jpeg',
            packages: []
        },
        {
            place: 'Goa', region: 'Domestic', tagline: 'Beaches, Bikes & Chill Vibes',
            coverImage: 'https://images.pexels.com/photos/35916755/pexels-photo-35916755.jpeg',
            packages: [{
                id: 'g1', name: 'Goa Budget Escape', price: '₹3,999', duration: '3 Days / 2 Nights',
                description: 'Sun, sand and everything in between.',
                features: ['A/C Rooms', 'Bike Rental', 'Breakfast'],
                images: ['https://images.pexels.com/photos/1604287/pexels-photo-1604287.jpeg']
            }]
        }
    ];
}

/* ══════════════════════════════════════
   REGION FILTERS
══════════════════════════════════════ */
function buildRegionFilters() {
    const regions = ['All', ...new Set(travelData.map(d => d.region))];
    const wrap = $('regionFilters');
    wrap.innerHTML = '';
    regions.forEach(r => {
        const btn = el('button', 'region-btn' + (r === 'All' ? ' active' : ''));
        btn.textContent = r;
        btn.addEventListener('click', () => {
            activeRegion = r;
            wrap.querySelectorAll('.region-btn').forEach(b => b.classList.toggle('active', b.textContent === r));
            renderPlaces();
            clearPackages();
        });
        wrap.appendChild(btn);
    });
}

/* ══════════════════════════════════════
   RENDER PLACES
══════════════════════════════════════ */
function renderPlaces() {
    const list = $('placesList');
    const filtered = activeRegion === 'All' ? travelData : travelData.filter(d => d.region === activeRegion);

    list.innerHTML = '';
    if (!filtered.length) {
        list.innerHTML = '<div style=\"padding:32px;text-align:center;color:rgba(255,255,255,0.4);font-size:0.85rem;\">No destinations found</div>';
        return;
    }

    filtered.forEach((item, i) => {
        const card = el('div', 'place-card');
        card.style.opacity = '0';
        card.style.transform = 'translateX(-12px)';
        card.innerHTML = `
      <div class=\"place-thumb\">
        <img src=\"${item.coverImage}?auto=compress&cs=tinysrgb&w=600\" alt=\"${item.place}\" loading=\"lazy\" />
      </div>
      <div class=\"place-info\">
        <div class=\"place-name\">${item.place}</div>
        <div class=\"place-region\">${item.tagline}</div>
      </div>
      <span class=\"place-badge\">${item.packages.length} pkg${item.packages.length !== 1 ? 's' : ''}</span>
    `;
        card.addEventListener('click', () => selectPlace(item.place, card));
        list.appendChild(card);
        setTimeout(() => {
            card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateX(0)';
        }, i * 55);
    });
}

function selectPlace(name, card) {
    document.querySelectorAll('.place-card').forEach(c => c.classList.remove('active'));
    card.classList.add('active');
    activePlace = name;
    const data = travelData.find(d => d.place === name);
    if (data) renderPackages(data);
}

/* ══════════════════════════════════════
   RENDER PACKAGES
══════════════════════════════════════ */
function renderPackages(data) {
    const content = $('packagesContent');
    const empty = $('packagesEmpty');
    const grid = $('packagesGrid');

    empty.classList.add('hidden');
    content.classList.remove('hidden');

    $('packagesHdr').innerHTML = `
    <h3>${data.place}</h3>
    <p>${data.packages.length} package${data.packages.length !== 1 ? 's' : ''} available · ${data.tagline}</p>
  `;

    grid.innerHTML = '';

    if (!data.packages || !data.packages.length) {
        const waMsg = `Hello, I want to enquire about a trip:\
\
📍 Destination: ${data.place}\
📝 ${data.tagline}\
\
Please share available packages and details.`;
        const cta = document.createElement('div');
        cta.className = 'no-pkg-cta';
        cta.innerHTML = `
      <h4>Packages Coming Soon</h4>
      <p>Contact us on WhatsApp for the latest packages, pricing, and a customised itinerary.</p>
      <button class=\"wa-enquire-btn\" id=\"noPkgWaBtn\">
        <svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z\"/></svg>
        Enquire on WhatsApp
      </button>
    `;
        grid.appendChild(cta);
        document.getElementById('noPkgWaBtn').addEventListener('click', () => openWaPage(waMsg));
        return;
    }

    data.packages.forEach((pkg, i) => {
        const card = el('div', 'pkg-card');
        card.style.animationDelay = `${i * 0.1}s`;
        card.innerHTML = `
      <div class=\"pkg-img\">
        <img src=\"${pkg.images[0]}\" alt=\"${pkg.name}\" loading=\"lazy\" />
        <span class=\"pkg-price\">${pkg.price}</span>
      </div>
      <div class=\"pkg-body\">
        <div class=\"pkg-name\">${pkg.name}</div>
        <div class=\"pkg-meta\">
          <span class=\"pkg-tag\">⏱ ${pkg.duration}</span>
          <span class=\"pkg-tag\">✦ ${pkg.features.length} incl.</span>
        </div>
        <p class=\"pkg-desc\">${pkg.description}</p>
      </div>
    `;
        card.addEventListener('click', () => openModal(pkg, data.place));
        grid.appendChild(card);
    });
}

function clearPackages() {
    $('packagesEmpty').classList.remove('hidden');
    $('packagesContent').classList.add('hidden');
    activePlace = null;
}

/* ══════════════════════════════════════
   MODAL
══════════════════════════════════════ */
// function openModal(pkg) {
//     carouselImages = pkg.images;
//     currentCarouselIdx = 0;

//     const body = $('modalBody');
//     body.innerHTML = `
//     <div class=\"modal-carousel\">
//       <div class=\"carousel-main\">
//         <img id=\"carMain\" src=\"${pkg.images[0]}\" alt=\"${pkg.name}\" />
//       </div>
//       <div class=\"carousel-thumbs\" id=\"carThumbs\">
//         ${pkg.images.map((img, i) => `
//           <div class=\"c-thumb${i === 0 ? ' active' : ''}\" data-idx=\"${i}\">
//             <img src=\"${img}\" alt=\"\" loading=\"lazy\" />
//           </div>
//         `).join('')}
//       </div>
//     </div>
//     <div class=\"modal-details\">
//       <h2 class=\"modal-title\">${pkg.name}</h2>
//       <div class=\"modal-meta\">
//         <span class=\"modal-badge price\">${pkg.price}</span>
//         <span class=\"modal-badge\">⏱ ${pkg.duration}</span>
//         <span class=\"modal-badge\">📦 ${pkg.features.length} inclusions</span>
//       </div>
//       <p class=\"modal-desc\">${pkg.description}</p>
//       <div class=\"modal-feats\">
//         <h4>What's Included</h4>
//         <div class=\"feat-list\">
//           ${pkg.features.map(f => `<div class=\"feat-item\">${f}</div>`).join('')}
//         </div>
//       </div>
//       <button class=\"modal-cta\" id=\"bookBtn\">
//         <svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z\"/></svg>
//         Book Now on WhatsApp
//       </button>
//     </div>
//   `;

//     // Book Now
//     document.getElementById('bookBtn').addEventListener('click', () => {
//         const msg = `Hello, I want to book a package:\
\
📍 Destination: ${activePlace}\
📦 Package: ${pkg.name}\
💰 Price: ${pkg.price}\
⏱ Duration: ${pkg.duration}\
\
📝 ${pkg.description}\
\
Please share more details.`;
//         openWaPage(msg);
//     });

//     // Thumbnails
//     document.querySelectorAll('.c-thumb').forEach(t => {
//         t.addEventListener('click', () => setCarousel(+t.dataset.idx));
//     });

//     const overlay = $('modalOverlay');
//     overlay.classList.remove('hidden');
//     requestAnimationFrame(() => {
//         overlay.classList.add('visible');
//         document.body.style.overflow = 'hidden';
//     });
// }

// let currentCarouselIdx = 0;
// let carouselImages = [];

function openModal(pkg, place) {
    carouselImages = pkg.images || [];
    currentCarouselIdx = 0;

    // BASIC INFO
    modalTitle.textContent = pkg.name;

    modalBadges.innerHTML = `
        <span>${place}</span>
        <span>Featured</span>
    `;

    modalMeta.innerHTML = `
        <span class=\"modal-badge\">${pkg.duration}</span>
        <span class=\"modal-badge\">${pkg.price}</span>
    `;

    // DESCRIPTION FORMATTER
    const formatInline = (text) => {
        return text
            .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
            .replace(/\\*(.*?)\\*/g, '<em>$1</em>')
            .replace(/\\|\\|(.*?)\\|\\|/g, '<u>$1</u>');
    };

    const formattedDesc = (pkg.description || '')
        .split('\
')
        .map(line => {
            if (line.startsWith('> ')) {
                return `
                <div class=\"quote-line\">
                    ${formatInline(line.slice(2))}
                </div>
                `;
            }
            return `<div>${formatInline(line)}</div>`;
        })
        .join('');

    modalDesc.innerHTML = formattedDesc;

    // FEATURES
    modalFeatures.innerHTML = `
        <h3>Highlights</h3>
        ${(pkg.features || []).map(f => `<p>✓ ${f}</p>`).join('')}
    `;

    // INCLUSIONS
    modalInclusions.innerHTML = `
        <h3>Inclusions</h3>
        ${(pkg.inclusions || []).map(i => `<p>✔ ${i}</p>`).join('')}
    `;

    // EXCLUSIONS
    modalExclusions.innerHTML = `
        <h3>Exclusions</h3>
        ${(pkg.exclusions || []).map(e => `<p>✖ ${e}</p>`).join('')}
    `;

    // BUILD CAROUSEL
    buildCarousel(carouselImages);

    // OPEN MODAL
    modalOverlay.classList.remove('hidden');

    requestAnimationFrame(() => {
        modalOverlay.classList.add('visible');
        document.body.style.overflow = 'hidden'; // 🔥 ADD THIS
    });

    // BOOK BUTTON
    modalBookBtn.onclick = () => {
        const message = `Hello 👋

I want to book a package:

📍 Destination: ${place}
📦 Package: ${pkg.name}
💰 Price: ${pkg.price}
4