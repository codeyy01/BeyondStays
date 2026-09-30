const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('index.html', 'utf-8');
const testHtml = html.replace('</body>', <script>
    window.addEventListener('load', () => {
        setTimeout(() => {
            const slides = document.querySelectorAll('.hero-slide');
            console.log('Slides count:', slides.length);
            const activeIdx = Array.from(slides).findIndex(s => s.classList.contains('active'));
            console.log('Active index before click:', activeIdx);
            
            const nextBtn = document.getElementById('heroNext');
            if (nextBtn) {
                console.log('Clicking next button...');
                nextBtn.click();
                setTimeout(() => {
                    const newActiveIdx = Array.from(slides).findIndex(s => s.classList.contains('active'));
                    console.log('Active index after click:', newActiveIdx);
                }, 100);
            } else {
                console.log('heroNext not found');
            }
        }, 500);
    });
</script></body>);

const dom = new JSDOM(testHtml, { runScripts: "dangerously", resources: "usable" });
