import re

base_css = '''
/* ── Layout & Typography ── */
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.section { padding: 100px 0; }
.section-green { background: var(--green); color: var(--white); }
.section-light { background: var(--cream); }
.section-eyebrow { font-size: 0.9rem; letter-spacing: 2px; text-transform: uppercase; font-weight: 600; color: var(--text-muted); margin-bottom: 16px; display: flex; align-items: center; gap: 12px; }
.section-eyebrow::before { content: ""; display: block; width: 40px; height: 1px; background: currentColor; }
.section-title { font-family: var(--font-display); font-size: 3.5rem; line-height: 1.1; font-weight: 700; margin-bottom: 24px; color: var(--text); }
.section-title em { font-style: italic; font-weight: 400; color: var(--green); }

/* ── Hero Section ── */
.hero-wrapper { position: relative; width: 100%; height: 100vh; overflow: hidden; background: #000; }
.hero-frame { position: absolute; inset: 0; }
.hero { position: absolute; inset: 0; width: 100%; height: 100%; }
.hero-slides { position: absolute; inset: 0; width: 100%; height: 100%; }
.hero-slide { position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0; transition: opacity 1.2s cubic-bezier(0.4, 0, 0.2, 1); background-size: cover; background-position: center; }
.hero-slide::after { content: ""; position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.1) 50%, rgba(0,0,0,0.6) 100%); }
.hero-slide.active { opacity: 1; z-index: 1; }
.hero-giant-title { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 2; color: #fff; font-family: var(--font-display); font-size: 10vw; font-weight: 800; line-height: 0.9; text-align: center; text-transform: uppercase; letter-spacing: -2px; pointer-events: none; mix-blend-mode: overlay; opacity: 0.9; }

.hero-ui-layer { position: absolute; bottom: 0; left: 0; width: 100%; z-index: 3; display: flex; justify-content: space-between; align-items: flex-end; padding: 40px; pointer-events: none; }
.hero-left-content { pointer-events: auto; color: #fff; max-width: 400px; }
.hero-left-content h1 { font-family: var(--font-display); font-size: 2.5rem; line-height: 1.1; margin-bottom: 16px; font-weight: 600; }
.hero-left-content p { font-size: 1.1rem; opacity: 0.9; margin-bottom: 32px; }
.hero-btn-pill { display: inline-flex; align-items: center; gap: 12px; padding: 16px 32px; background: #fff; color: #000; border-radius: 40px; font-weight: 700; font-size: 1rem; transition: var(--transition); }
.hero-btn-pill:hover { background: var(--accent); transform: translateY(-2px); }

.hero-right-glass-card { pointer-events: auto; background: rgba(255,255,255,0.1); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.2); padding: 24px; border-radius: 20px; color: #fff; width: 280px; }
.hero-right-glass-card p { font-size: 0.9rem; line-height: 1.5; opacity: 0.9; margin-bottom: 16px; }
.hero-nav { position: absolute; top: 50%; transform: translateY(-50%); z-index: 4; cursor: pointer; color: #fff; font-size: 1.5rem; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); backdrop-filter: blur(8px); border-radius: 50%; transition: var(--transition); }
.hero-nav:hover { background: rgba(255,255,255,0.3); }
.hero-nav.prev { left: 30px; }
.hero-nav.next { right: 30px; }

.scroll-indicator { position: absolute; bottom: 40px; left: 50%; transform: translateX(-50%); z-index: 4; color: #fff; display: flex; flex-direction: column; align-items: center; gap: 8px; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; font-weight: 600; }
.scroll-line { width: 1px; height: 40px; background: rgba(255,255,255,0.2); position: relative; overflow: hidden; }
.scroll-line::after { content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 50%; background: #fff; animation: scrollLine 2s ease-in-out infinite; }
@keyframes scrollLine { 0% { transform: translateY(-100%); } 100% { transform: translateY(200%); } }

/* ── Marquee ── */
.marquee-wrap { background: var(--green); padding: 24px 0; overflow: hidden; white-space: nowrap; border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); }
.marquee-track { display: inline-block; animation: marquee 30s linear infinite; font-family: var(--font-display); font-size: 1.5rem; font-style: italic; color: #fff; }
.marquee-track span { display: inline-block; padding: 0 20px; }
.marquee-track .sep { color: var(--accent); }
@keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

/* ── About Section Base ── */
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }

/* ── Buttons ── */
.btn { display: inline-flex; align-items: center; gap: 12px; padding: 16px 32px; border-radius: 40px; font-weight: 700; font-size: 1rem; cursor: pointer; transition: var(--transition); border: none; }
.btn-primary { background: var(--green); color: #fff; }
.btn-primary:hover { background: var(--green-light); transform: translateY(-2px); box-shadow: var(--shadow); }
.btn-outline { background: transparent; border: 1px solid var(--green); color: var(--green); }
.btn-outline:hover { background: var(--green); color: #fff; }
.desk-btn { background: var(--green); color: #fff; padding: 14px 28px; border-radius: 40px; font-weight: 700; display: inline-block; margin-top: 20px; transition: var(--transition); }
.desk-btn:hover { background: var(--green-light); transform: translateY(-2px); }

/* ── Utilities ── */
.reveal-left { opacity: 0; transform: translateX(-40px); transition: 0.8s cubic-bezier(0.25, 1, 0.5, 1); }
.reveal-right { opacity: 0; transform: translateX(40px); transition: 0.8s cubic-bezier(0.25, 1, 0.5, 1); }
.reveal-up { opacity: 0; transform: translateY(40px); transition: 0.8s cubic-bezier(0.25, 1, 0.5, 1); }
.reveal-left.active, .reveal-right.active, .reveal-up.active { opacity: 1; transform: translate(0, 0); }

/* ── Contact Section ── */
.contact-layout { display: grid; grid-template-columns: 1fr 1.2fr; gap: 60px; align-items: center; }
.contact-left h2 { font-family: var(--font-display); font-size: 3.5rem; color: #fff; margin-bottom: 24px; line-height: 1.1; }
.contact-left p { color: rgba(255,255,255,0.8); font-size: 1.1rem; margin-bottom: 40px; line-height: 1.6; max-width: 400px; }
.contact-items { display: flex; flex-direction: column; gap: 24px; }
.contact-items p { margin: 0; display: flex; align-items: center; gap: 16px; color: #fff; font-size: 1.1rem; }
.contact-form { background: #fff; padding: 40px; border-radius: 24px; box-shadow: var(--shadow-lg); }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }
.form-group { display: flex; flex-direction: column; gap: 8px; }
.form-group label { font-size: 0.85rem; font-weight: 700; color: var(--text); letter-spacing: 1px; text-transform: uppercase; }
.form-group input, .form-group select, .form-group textarea { padding: 16px; border: 1px solid rgba(0,0,0,0.1); border-radius: 12px; font-family: inherit; font-size: 1rem; background: var(--cream); transition: var(--transition); }
.form-group input:focus, .form-group select:focus, .form-group textarea:focus { outline: none; border-color: var(--green); background: #fff; box-shadow: 0 0 0 4px rgba(0, 69, 38, 0.1); }
.contact-form button { width: 100%; padding: 18px; background: var(--green); color: #fff; border-radius: 12px; font-size: 1.1rem; font-weight: 700; cursor: pointer; transition: var(--transition); display: flex; align-items: center; justify-content: center; gap: 12px; border: none; margin-top: 10px; }
.contact-form button:hover { background: var(--green-light); transform: translateY(-2px); }

/* ── Footer ── */
.footer { background: var(--green-dark); color: #fff; padding: 80px 0 40px; margin-top: 100px; }
.footer-top { display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr; gap: 60px; margin-bottom: 60px; }
.footer-logo { max-width: 200px; margin-bottom: 24px; }
.footer-desc { color: rgba(255,255,255,0.7); line-height: 1.7; }
.footer h4 { font-family: var(--font-display); font-size: 1.4rem; margin-bottom: 24px; }
.footer-links { display: flex; flex-direction: column; gap: 16px; }
.footer-links a { color: rgba(255,255,255,0.7); transition: var(--transition); }
.footer-links a:hover { color: var(--accent); padding-left: 8px; }
.footer-bottom { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 32px; display: flex; justify-content: space-between; align-items: center; color: rgba(255,255,255,0.5); font-size: 0.9rem; }
.social-links { display: flex; gap: 16px; }
.social-links a { display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; background: rgba(255,255,255,0.1); border-radius: 50%; color: #fff; transition: var(--transition); }
.social-links a:hover { background: var(--accent); color: var(--green-dark); transform: translateY(-4px); }

/* WhatsApp FAB */
.wa-fab { position: fixed; bottom: 24px; right: 24px; width: 60px; height: 60px; background: #25d366; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; text-decoration: none; box-shadow: 0 4px 12px rgba(37, 211, 102, 0.4); z-index: 1000; transition: transform 0.3s; }
.wa-fab:hover { transform: scale(1.1); }
.wa-fab svg { width: 32px; height: 32px; fill: currentColor; }

@media (max-width: 768px) {
    .hero-ui-layer { flex-direction: column; padding: 20px; padding-bottom: 100px; }
    .hero-right-glass-card { display: none; }
    .hero-giant-title { font-size: 15vw; }
    .section-title { font-size: 2.5rem; }
}
'''

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will append this base CSS right before `/* ── Mobile Menu ── */` which is around line 300
idx = css.find('/* ── Mobile Menu ── */')
if idx != -1:
    css = css[:idx] + base_css + '\n' + css[idx:]
else:
    css = css + '\n' + base_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
