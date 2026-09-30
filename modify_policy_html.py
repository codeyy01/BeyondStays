import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_policy_html = '''
    <!-- ? REFUND POLICY ? -->
    <section class="policy section" id="policy">
        <div class="container">
            <div class="section-header policy-header">
                <div class="section-eyebrow policy-eyebrow">Transparency & Trust</div>
                <h2 class="section-title policy-title">Refund & <em>Cancellation Policy</em></h2>
            </div>

            <div class="policy-box">
                <ul>
                    <li>
                        <div class="policy-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                        </div>
                        <div class="policy-text">
                            <strong>Date Changes:</strong> Allowed based on availability.
                        </div>
                    </li>
                    <li>
                        <div class="policy-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg>
                        </div>
                        <div class="policy-text">
                            <strong>Cancellation Policy:</strong> Advance amount is strictly non-refundable under any circumstances.
                        </div>
                    </li>
                    <li>
                        <div class="policy-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.5 2v6h-6M2.5 22v-6h6M2 11.5a10 10 0 0 1 18.8-4.3M22 12.5a10 10 0 0 1-18.8 4.2"/></svg>
                        </div>
                        <div class="policy-text">
                            <strong>Policy Updates:</strong> Beyondstays reserves the right to modify this policy at any time without prior notice.
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </section>
'''

# Replace the existing policy section
html = re.sub(r'<!--.*?REFUND POLICY.*?-->\s*<section class="policy section" id="refund-policy">.*?</section>', new_policy_html.strip(), html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML replaced.")
