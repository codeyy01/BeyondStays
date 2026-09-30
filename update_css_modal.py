import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_modal_css = '''
/* --- NEW MODERN MODAL --- */
.modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.4s ease;
}
.modal-overlay.visible {
    opacity: 1;
    pointer-events: auto;
}
.modal-overlay.hidden {
    display: none;
}
.modal {
    background: #fff;
    border-radius: 24px;
    max-width: 600px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
    transform: translateY(40px) scale(0.95);
    transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    padding: 32px;
}
.modal-overlay.visible .modal {
    transform: translateY(0) scale(1);
}
.modal-close {
    position: absolute;
    top: 20px;
    right: 20px;
    background: #f0f0f0;
    border: none;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    font-size: 1.5rem;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #333;
    transition: background 0.2s;
}
.modal-close:hover {
    background: #e0e0e0;
}

/* Typography & Layout */
.modal-badges {
    display: flex;
    gap: 8px;
    margin-bottom: 12px;
}
.modal-badges span {
    padding: 4px 12px;
    border-radius: 16px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
}
.modal-badge-place {
    background: #e6f0e9;
    color: #2b6e46;
}
.modal-badge-pop {
    background: #fef0db;
    color: #c47600;
}

.modal-title {
    font-size: 2rem;
    font-weight: 900;
    font-family: var(--font-heading);
    color: #111;
    margin: 0 0 16px 0;
    line-height: 1.2;
}
.modal-meta {
    display: flex;
    gap: 16px;
    margin-bottom: 24px;
    border-bottom: 1px solid #eee;
    padding-bottom: 24px;
}
.modal-meta-item {
    font-size: 0.9rem;
    font-weight: 600;
    color: #444;
}
.modal-desc {
    font-size: 0.95rem;
    color: #555;
    line-height: 1.6;
    margin-bottom: 32px;
}
.modal-desc strong {
    color: #111;
}

/* Sections */
.modal-grid {
    display: flex;
    flex-direction: column;
    gap: 24px;
    margin-bottom: 32px;
}
.modal-section h4 {
    font-size: 1.1rem;
    font-weight: 800;
    margin: 0 0 16px 0;
    color: #222;
}
.modal-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 12px;
}
.modal-list li {
    position: relative;
    padding-left: 28px;
    font-size: 0.9rem;
    color: #444;
    line-height: 1.4;
}
.modal-list li::before {
    position: absolute;
    left: 0;
    top: 0;
    font-weight: 900;
    font-size: 1.1rem;
}

.highlight-list li::before {
    content: '✓';
    color: #2b6e46; /* Green */
}
.inclusion-list li::before {
    content: '✔';
    color: #16a34a; /* Light Green */
}
.exclusion-list li::before {
    content: '✖';
    color: #dc2626; /* Red */
}

/* Sticky Button */
.modal-book-btn {
    width: 100%;
    padding: 16px;
    background: #25D366; /* WhatsApp Green */
    color: #fff;
    border: none;
    border-radius: 12px;
    font-size: 1.1rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    position: sticky;
    bottom: 0;
    box-shadow: 0 -10px 20px rgba(255,255,255,0.9);
}
.modal-book-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 -5px 25px rgba(37, 211, 102, 0.4);
}
'''

# Delete old modal CSS
css = re.sub(r'\.modal-overlay\s*\{.*?(?=\/\* --- NEW |\Z)', '', css, flags=re.DOTALL)

css = css + '\n' + new_modal_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
