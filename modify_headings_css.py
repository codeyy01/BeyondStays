with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- BEAUTIFY REVIEWS & FAQ HEADINGS --- */
#testimonials .section-eyebrow, 
#faq .section-eyebrow {
    color: var(--green) !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    letter-spacing: 2px !important;
}
#testimonials .section-eyebrow::before, 
#faq .section-eyebrow::before {
    height: 1.5px !important;
    background-color: var(--green) !important;
}

/* Make the centered FAQ eyebrow look like a luxury sandwiched badge */
#faq .section-eyebrow.text-center {
    justify-content: center !important;
}
#faq .section-eyebrow.text-center::after {
    content: "" !important; 
    display: block !important; 
    width: 40px !important; 
    height: 1.5px !important; 
    background-color: var(--green) !important;
}

/* Enhance the titles themselves */
#testimonials .section-title,
#faq .section-title {
    color: #000 !important;
    margin-bottom: 50px !important;
}
#testimonials .section-title em,
#faq .section-title em {
    color: var(--green) !important;
}
''')
print("Heading styles appended.")
