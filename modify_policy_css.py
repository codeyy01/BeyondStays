with open('style_ultimate.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- POLICY SECTION --- */
.policy {
    background-color: var(--cream);
    padding: 100px 0;
}
.policy-header {
    text-align: left;
    margin-bottom: 40px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
}
.policy-eyebrow {
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--green);
    display: flex;
    align-items: center;
    gap: 16px;
}
.policy-eyebrow::before {
    content: '';
    display: block;
    width: 32px;
    height: 1.5px;
    background-color: var(--green);
}
.policy-title {
    font-family: var(--font-display);
    font-size: 3.5rem;
    color: var(--text);
    margin: 0;
    line-height: 1.1;
}
.policy-title em {
    font-style: italic;
    font-weight: 400;
    color: var(--green);
}

.policy-box {
    background: rgba(18, 53, 0, 0.02); /* Extremely subtle green tint */
    border: 1px solid rgba(18, 53, 0, 0.1);
    border-radius: 24px;
    overflow: hidden; /* So hover effects stay inside corners */
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.02);
}
.policy-box ul {
    list-style: none;
    padding: 0;
    margin: 0;
}
.policy-box li {
    padding: 32px 40px;
    border-bottom: 1px solid rgba(18, 53, 0, 0.06);
    display: flex;
    align-items: flex-start;
    gap: 24px;
    transition: background 0.3s ease;
}
.policy-box li:last-child {
    border-bottom: none;
}
.policy-box li:hover {
    background: rgba(18, 53, 0, 0.05); /* Subtle highlight */
}

.policy-icon {
    flex-shrink: 0;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: rgba(18, 53, 0, 0.05);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--green);
}

.policy-text {
    font-size: 1.15rem;
    line-height: 1.6;
    color: var(--text-muted);
    padding-top: 10px; /* Aligns text visually with center of icon */
}
.policy-text strong {
    color: var(--text);
    font-weight: 700;
    margin-right: 8px;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
    .policy { padding: 60px 0; }
    .policy-title { font-size: 2.5rem; }
    .policy-box li { padding: 24px 20px; gap: 16px; flex-direction: column; }
    .policy-icon { width: 40px; height: 40px; }
    .policy-text { padding-top: 0; font-size: 1rem; }
}
''')
print("CSS appended.")
