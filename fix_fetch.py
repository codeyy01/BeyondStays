import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace fetchFAQ with a hardcoded synchronous function
new_fetchFAQ = '''
function fetchFAQ() {
    faqData = [
      {
        "question": "How do I book a trip?",
        "answer": "You can explore packages and click 'Book Now' to connect with us on WhatsApp. Our team will assist you with the complete booking process."
      },
      {
        "question": "Can I customize my travel package?",
        "answer": "Yes, all our packages can be customized based on your preferences, budget, and travel dates."
      },
      {
        "question": "What payment methods do you accept?",
        "answer": "We accept UPI, bank transfer, and other secure payment methods. Details will be shared during booking."
      },
      {
        "question": "Do you provide group discounts?",
        "answer": "Yes, we offer special discounts for group bookings. Contact us for details."
      }
    ];
    renderFAQ();
}
'''

js = re.sub(r'async function fetchFAQ\(\) \{.*?\n\}', new_fetchFAQ.strip(), js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("fetchFAQ replaced with hardcoded data.")
