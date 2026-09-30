import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the broken .mobile-menu block
new_mobile_menu = '''
/* Recreated Original Dropdown Mobile Menu */
.mobile-menu {
    position: fixed;
    top: 80px; /* Below navbar */
    left: 5%;
    width: 90%;
    background: var(--white);
    border-radius: 20px;
    padding: 30px 0;
    box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    z-index: 999;
    
    /* Animation states */
    opacity: 0;
    visibility: hidden;
    transform: translateY(-20px);
    transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
    
    display: flex;
    flex-direction: column;
    align-items: center;
}

.mobile-menu.open {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.mobile-menu ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 24px;
    width: 100%;
}

.mobile-menu ul li a {
    font-size: 1.1rem;
    font-weight: 700;
    font-family: var(--font-heading);
    color: var(--text-dark);
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 2px;
    transition: color 0.3s;
}

.mobile-menu ul li a:hover {
    color: var(--primary);
}
'''

# Delete my previous broken .mobile-menu rules using a regex from .mobile-menu { down to .mobile-menu ul li a { ... }
css = re.sub(r'\.mobile-menu\s*\{.*?(?=\/\* Global Responsive Fixes \*/)', new_mobile_menu + '\n\n', css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
