with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- GLOBAL HIDDEN --- */
.hidden {
    display: none !important;
}

/* --- WHATSAPP POPUP MODAL --- */
.wa-popup {
    position: fixed !important;
    bottom: 100px !important;
    right: 32px !important;
    background: #fff !important;
    width: 320px !important;
    border-radius: 24px !important;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15) !important;
    padding: 24px !important;
    z-index: 1000 !important;
    animation: slideUpFade 0.4s cubic-bezier(0.25, 1, 0.5, 1) !important;
    border: 1px solid rgba(0,0,0,0.05) !important;
}

@keyframes slideUpFade {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

.wa-box h3 {
    font-size: 1.25rem !important;
    font-family: var(--font-body) !important;
    color: var(--text) !important;
    margin-bottom: 8px !important;
}

.wa-box p {
    font-size: 0.95rem !important;
    color: var(--text-muted) !important;
    margin-bottom: 20px !important;
}

.wa-opt {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
    padding: 14px !important;
    margin-bottom: 12px !important;
    background: #25d366 !important;
    color: #fff !important;
    text-decoration: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    transition: background 0.3s !important;
}
.wa-opt:hover {
    background: #1ebc59 !important;
}

.wa-cancel {
    display: block !important;
    width: 100% !important;
    padding: 12px !important;
    background: transparent !important;
    border: 1px solid rgba(0,0,0,0.1) !important;
    color: var(--text-muted) !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: background 0.3s !important;
    margin-top: 16px !important;
}
.wa-cancel:hover {
    background: rgba(0,0,0,0.03) !important;
}

@media (max-width: 768px) {
    .wa-popup {
        right: 16px !important;
        bottom: 80px !important;
        width: calc(100vw - 32px) !important;
    }
}
''')
print("WhatsApp CSS appended.")
