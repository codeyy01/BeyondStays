# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_footer = '''
<footer class="footer-section">
    <div class="container" style="position: relative; z-index: 2;">
        <div class="footer-pill">
            <div class="footer-top">
                <div class="footer-brand">
                    <a href="#" class="nav-logo">
                        <img src="./assets/nav-logo-green.png" alt="Beyondstays Logo" style="height: 32px;" />
                    </a>
                    <p>Beyondstays empowers travelers to explore raw nature, transforming normal trips into beautiful, lifelong memories.</p>
                    <div class="footer-socials">
                        <a href="#"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4l11.733 16h4.267l-11.733 -16z" /><path d="M4 20l6.768 -6.768m2.46 -2.46l6.772 -6.772" /></svg></a>
                        <a href="#"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
                        <a href="#"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
                        <a href="#"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg></a>
                    </div>
                </div>
                
                <div class="footer-links-wrap">
                    <div class="footer-col">
                        <h5>Explore</h5>
                        <ul>
                            <li><a href="#destinations">Packages</a></li>
                            <li><a href="#destinations">Destinations</a></li>
                            <li><a href="#testimonials">Reviews</a></li>
                            <li><a href="#policy">Policy</a></li>
                        </ul>
                    </div>
                    <div class="footer-col">
                        <h5>Resources</h5>
                        <ul>
                            <li><a href="#faq">FAQ</a></li>
                            <li><a href="#contact">Contact Support</a></li>
                            <li><a href="#">Blog</a></li>
                            <li><a href="#">Guides</a></li>
                        </ul>
                    </div>
                    <div class="footer-col">
                        <h5>Company</h5>
                        <ul>
                            <li><a href="#about">About Us</a></li>
                            <li><a href="#">Careers</a></li>
                            <li><a href="#">Partners</a></li>
                            <li><a href="#">Privacy</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <span>&copy; 2026 Beyondstays. All rights reserved.</span>
                <div class="footer-legal">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms of Service</a>
                    <a href="https://www.instagram.com/razi_vayalkara" target="_blank" style="text-decoration: underline;">Developed by Razi</a>
                </div>
            </div>
        </div>
    </div>
    <div class="footer-watermark">BEYONDSTAYS</div>
</footer>
'''

html = re.sub(r'<footer>.*?</footer>', new_footer.strip(), html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Footer HTML replaced.")
