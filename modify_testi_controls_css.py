with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- TESTIMONIAL CONTROLS --- */
.testi-controls {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    gap: 40px !important;
    margin-top: 60px !important;
}

.testi-btn {
    width: 56px !important;
    height: 56px !important;
    border-radius: 50% !important;
    border: none !important;
    background: #fff !important;
    color: var(--green) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1) !important;
    outline: none !important;
}
.testi-btn:hover {
    background: var(--green) !important;
    color: #fff !important;
    transform: translateY(-3px) scale(1.05) !important;
    box-shadow: 0 8px 25px rgba(18, 53, 0, 0.2) !important;
}
.testi-btn:active {
    transform: translateY(0) scale(0.95) !important;
}
.testi-btn svg {
    width: 24px !important;
    height: 24px !important;
}

.testi-dots {
    display: flex !important;
    gap: 12px !important;
    align-items: center !important;
}
.testi-dot {
    width: 10px !important;
    height: 10px !important;
    border-radius: 50% !important;
    background: rgba(18, 53, 0, 0.15) !important;
    cursor: pointer !important;
    transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1) !important;
}
.testi-dot.active {
    width: 32px !important;
    background: var(--green) !important;
    border-radius: 10px !important;
}
.testi-dot:hover:not(.active) {
    background: rgba(18, 53, 0, 0.3) !important;
    transform: scale(1.2) !important;
}
''')
print("Testimonial controls CSS appended.")
