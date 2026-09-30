with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- LUXURY FAQ REDESIGN --- */
#faq {
    background: #fff !important;
    padding: 100px 0 !important;
}
.text-center { text-align: center !important; }
.section-title.text-center { margin-bottom: 60px !important; }

.faq-list {
    max-width: 800px !important;
    margin: 0 auto !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 16px !important;
}

.faq-item {
    background: rgba(18, 53, 0, 0.03) !important;
    border: 1px solid rgba(0, 0, 0, 0.02) !important;
    border-radius: 40px !important;
    padding: 24px 32px !important;
    cursor: pointer !important;
    transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1) !important;
    overflow: hidden !important;
}
.faq-item:hover {
    background: rgba(18, 53, 0, 0.05) !important;
}
.faq-item.active {
    background: #fff !important;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.05) !important;
    border-color: rgba(0, 0, 0, 0.05) !important;
}

.faq-question {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    font-weight: 700 !important;
    font-size: 1.15rem !important;
    color: var(--text) !important;
    gap: 20px !important;
    font-family: var(--font-body) !important;
}

.faq-icon {
    width: 36px !important;
    height: 36px !important;
    border-radius: 50% !important;
    background: #fff !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    font-size: 1.5rem !important;
    font-weight: 400 !important;
    color: var(--green) !important;
    transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1), background 0.4s ease, color 0.4s ease !important;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important;
    flex-shrink: 0 !important;
}
.faq-item.active .faq-icon {
    transform: rotate(45deg) !important;
    background: var(--green) !important;
    color: #fff !important;
    box-shadow: 0 4px 15px rgba(18, 53, 0, 0.2) !important;
}

.faq-answer {
    max-height: 0 !important;
    opacity: 0 !important;
    margin-top: 0 !important;
    color: var(--text-muted) !important;
    line-height: 1.7 !important;
    transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1) !important;
    font-size: 1.05rem !important;
}
.faq-item.active .faq-answer {
    max-height: 400px !important;
    opacity: 1 !important;
    margin-top: 16px !important;
}

@media (max-width: 768px) {
    #faq { padding: 60px 0 !important; }
    .faq-list { gap: 12px !important; }
    .faq-item { padding: 20px 24px !important; border-radius: 30px !important; }
    .faq-question { font-size: 1.05rem !important; }
    .faq-icon { width: 32px !important; height: 32px !important; font-size: 1.3rem !important; }
    .faq-answer { font-size: 0.95rem !important; }
}
''')
print("FAQ CSS appended.")
