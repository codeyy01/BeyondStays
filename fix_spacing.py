with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- FIX UNWANTED SPACE BETWEEN POLICY AND REVIEWS --- */
.policy {
    padding-bottom: 40px !important;
}
#testimonials {
    padding-top: 40px !important;
}
@media (max-width: 768px) {
    .policy { padding-bottom: 20px !important; }
    #testimonials { padding-top: 20px !important; }
}
''')
print("Padding CSS appended.")
