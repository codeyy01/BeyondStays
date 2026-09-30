import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# We need to find the card.innerHTML assignment in renderModernPackages
start_str = "card.innerHTML = `"
end_str = "        `;"

start_idx = js.find(start_str)
end_idx = js.find(end_str, start_idx)

if start_idx != -1 and end_idx != -1:
    new_html = """card.innerHTML = `
            <img class="pkg-bg-img" src="${pkg.images && pkg.images.length > 0 ? pkg.images[0] : (pkg.coverImage || 'https://images.pexels.com/photos/1371360/pexels-photo-1371360.jpeg')}" alt="${pkg.name}" loading="lazy">
            <div class="pkg-gradient"></div>
            
            <div class="pkg-content">
                <h3 class="pkg-title">${pkg.placeName}</h3>
                <div class="pkg-subtitle">${pkg.name}</div>
                
                <p class="pkg-desc">${pkg.description || 'Explore the breathtaking beauty of ' + pkg.placeName + ' with our highly exclusive and beautifully curated package.'}</p>
                <div class="pkg-read-more">Read more</div>
                
                <div class="pkg-tags">
                    <div class="pkg-tag">
                        <svg viewBox="0 0 24 24" fill="#fff"><path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.41l9 9c.36.36.86.58 1.41.58s1.05-.22 1.41-.59l7-7c.36-.36.59-.86.59-1.41s-.23-1.06-.59-1.41zM5.5 7C4.67 7 4 6.33 4 5.5S4.67 4 5.5 4 7 4.67 7 5.5 6.33 7 5.5 7z"/></svg>
                        from ${pkg.price}
                    </div>
                    <div class="pkg-tag">
                        <svg viewBox="0 0 24 24" fill="#fff"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z"/><path d="M12.5 7H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
                        ${pkg.duration}
                    </div>
                </div>
                
                <div class="pkg-action-row">
                    <a href="#" class="pkg-btn">View Package</a>
                    <div class="pkg-heart">
                        <svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
                    </div>
                </div>
            </div>
        `;"""
    js = js[:start_idx] + new_html + js[end_idx + len(end_str):]
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("JS Updated successfully!")
else:
    print("Could not find the block in script.js.")
