"""
Translate Japanese product text to English using Google Translate (free, no API key).
Saves results to translations_en.json for use by generate_en.py.
"""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(__file__))
from deep_translator import GoogleTranslator

_ns = {}
exec(open('generate.py', encoding='utf-8').read(), _ns)
PRODUCTS = _ns['PRODUCTS']

CACHE_FILE = os.path.join(os.path.dirname(__file__), 'translations_en.json')

# Load existing cache
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        cache = json.load(f)
else:
    cache = {}

tr = GoogleTranslator(source='ja', target='en')

def translate(text):
    if not text or not text.strip():
        return text
    if text in cache:
        return cache[text]
    try:
        result = tr.translate(text)
        if not result:
            cache[text] = text
            return text
        cache[text] = result
        return result
    except Exception as e:
        print(f"  SKIP: {repr(text[:40])}")
        cache[text] = text  # keep original if translation fails
        return text

total = len(PRODUCTS)
for i, p in enumerate(PRODUCTS):
    slug = p['slug']
    print(f"[{i+1}/{total}] {p['name']}")

    # desc
    translate(p['desc'])

    # pros
    for pro in p['pros']:
        translate(pro)

    # cons
    for con in p['cons']:
        translate(con)

    # Save after each product
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    time.sleep(0.3)  # be polite to Google

print(f"\nDone. {len(cache)} strings translated → translations_en.json")
