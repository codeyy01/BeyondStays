with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- LUXURY PILL FOOTER REDESIGN --- */
.footer-section {
    background: rgba(18, 53, 0, 0.015) !important;
    position: relative !important;
    padding: 100px 0 !important;
    overflow: hidden !important;
    margin-top: 0 !important;
}

.footer-pill {
    background: #fff !important;
    border-radius: 40px !important;
    padding: 60px !important;
    box-shadow: 0 20px 60px rgba(0,0,0,0.03) !important;
    border: 1px solid rgba(0,0,0,0.02) !important;
}

.footer-top {
    display: flex !important;
    justify-content: space-between !important;
    gap: 60px !important;
    margin-bottom: 60px !important;
}

.footer-brand {
    max-width: 320px !important;
}
.footer-brand p {
    font-size: 0.95rem !important;
    line-height: 1.7 !important;
    color: var(--text-muted) !important;
    margin: 24px 0 !important;
}

.footer-socials {
    display: flex !important;
    gap: 20px !important;
}
.footer-socials a {
    color: var(--text-muted) !important;
    transition: color 0.3s, transform 0.3s !important;
    display: flex !important;
}
.footer-socials a:hover {
    color: var(--green) !important;
    transform: translateY(-2px) !important;
}

.footer-links-wrap {
    display: flex !important;
    gap: 80px !important;
}
.footer-col h5 {
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    color: var(--text) !important;
    margin-bottom: 24px !important;
    font-family: var(--font-body) !important;
}
.footer-col ul {
    list-style: none !important;
    padding: 0 !important;
    margin: 0 !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 16px !important;
}
.footer-col a {
    color: var(--text-muted) !important;
    text-decoration: none !important;
    font-size: 0.95rem !important;
    transition: color 0.3s !important;
}
.footer-col a:hover {
    color: var(--green) !important;
}

.footer-bottom {
    border-top: 1px solid rgba(0,0,0,0.05) !important;
    padding-top: 32px !important;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    color: var(--text-muted) !important;
    font-size: 0.85rem !important;
}
.footer-legal {
    display: flex !important;
    gap: 32px !important;
}
.footer-legal a {
    color: var(--text-muted) !important;
    text-decoration: none !important;
    transition: color 0.3s !important;
}
.footer-legal a:hover {
    color: var(--green) !important;
}

.footer-watermark {
    position: absolute !important;
    bottom: -6vw !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    font-family: var(--font-display) !important;
    font-size: 18vw !important;
    font-weight: 700 !important;
    color: rgba(18, 53, 0, 0.03) !important;
    white-space: nowrap !important;
    z-index: 1 !important;
    pointer-events: none !important;
    line-height: 1 !important;
}

@media (max-width: 1024px) {
    .footer-top { flex-direction: column !important; }
    .footer-links-wrap { justify-content: space-between !important; gap: 40px !important; }
    .footer-bottom { flex-direction: column !important; gap: 24px !important; text-align: center !important; }
    .footer-legal { justify-content: center !important; flex-wrap: wrap !important; }
    .footer-watermark { font-size: 25vw !important; bottom: -8vw !important; }
}
@media (max-width: 768px) {
    .footer-pill { padding: 40px 32px !important; border-radius: 32px !important; }
    .footer-links-wrap { flex-direction: column !important; gap: 40px !important; }
    .footer-watermark { display: none !important; }
}
''')
print("Footer CSS appended.")
