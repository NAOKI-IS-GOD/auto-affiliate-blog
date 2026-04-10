"""Generate English static pages: /en/index.html, /en/faq.html, /en/contact.html, /en/privacy.html"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))

_gen_path = os.path.join(os.path.dirname(__file__), 'generate.py')
_ns = {}
exec(open(_gen_path, encoding='utf-8').read(), _ns)
PRODUCTS = _ns['PRODUCTS']
CAT_SLUGS = _ns['CAT_SLUGS']
BASE_URL = _ns['BASE_URL']

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'en')
os.makedirs(OUTPUT_DIR, exist_ok=True)

from collections import defaultdict

CAT_EN = {
    "スマートフォン": "Smartphones", "PC周辺機器": "PC Peripherals",
    "ワイヤレスイヤホン": "Wireless Earbuds", "スマートウォッチ": "Smartwatches",
    "ノートPC": "Laptops", "カメラ": "Cameras", "タブレット": "Tablets",
    "ゲーミング": "Gaming", "モニター": "Monitors", "充電器": "Chargers",
    "モバイルバッテリー": "Power Banks", "スマートスピーカー": "Smart Speakers",
    "スピーカー": "Speakers", "VR/AR": "VR/AR", "電子書籍リーダー": "E-Readers",
    "スマートホーム": "Smart Home", "エンタメ": "Entertainment", "家電": "Home Appliances",
    "テレビ": "TVs", "ドライヤー": "Hair Dryers", "電動歯ブラシ": "Electric Toothbrushes",
    "シェーバー": "Electric Shavers", "ロボット掃除機": "Robot Vacuums",
    "コーヒーメーカー": "Coffee Makers", "プロジェクター": "Projectors",
    "サウンドバー": "Soundbars", "ネットワーク機器": "Network Devices",
    "ゲーミングチェア": "Gaming Chairs", "コードレス掃除機": "Cordless Vacuums",
    "調理家電": "Kitchen Appliances",
}

EN_HEADER = '''<header>
  <div class="header-inner">
    <div class="logo"><a href="/en/" style="color:inherit;">📱 Gadget<span class="logo-dot">Navi</span></a></div>
    <nav id="main-nav">
      <a href="/en/#ranking">Rankings</a>
      <a href="/en/#reviews">Reviews</a>
      <a href="/en/faq.html">FAQ</a>
      <a href="/en/privacy.html">Privacy</a>
    </nav>
    <div style="display:flex;align-items:center;gap:8px;">
      <a href="/" style="font-size:0.8rem;padding:5px 10px;border:1px solid var(--border);border-radius:50px;color:var(--text);text-decoration:none;">🇯🇵 JA</a>
      <span style="font-size:0.8rem;padding:5px 10px;background:var(--primary);color:#fff;border-radius:50px;">🇬🇧 EN</span>
    </div>
  </div>
</header>'''

EN_FOOTER = '''<footer>
  <div class="footer-inner">
    <div class="footer-disclaimer">
      ⚠️ This site participates in affiliate programs. We may earn commissions from purchases made through links. This does not affect our editorial reviews.
    </div>
    <div class="footer-bottom">
      <p>© 2026 GadgetNavi All Rights Reserved.</p>
      <p>
        <a href="/en/privacy.html" style="color:rgba(255,255,255,0.5);">Privacy Policy</a> ／
        <a href="/en/faq.html" style="color:rgba(255,255,255,0.5);">FAQ</a> ／
        <a href="/en/contact.html" style="color:rgba(255,255,255,0.5);">Contact</a>
      </p>
    </div>
  </div>
</footer>'''

# ---- /en/index.html ----
top_products = sorted(PRODUCTS, key=lambda x: x['score'], reverse=True)[:12]
cat_map = defaultdict(list)
for p in PRODUCTS:
    cat_map[p['cat']].append(p)

ranking_cards = "\n".join([f'''  <a href="/en/{p['slug']}.html" class="rank-card">
    <div class="rank-num">#{i+1}</div>
    <div class="rank-thumb" style="background:linear-gradient(135deg,{p['bg'].split(',')[0].strip()},{p['bg'].split(',')[1].strip()})">
      <span style="font-size:2rem;">{p['emoji']}</span>
    </div>
    <div class="rank-body">
      <div class="rank-cat">{CAT_EN.get(p['cat'], p['cat'])}</div>
      <div class="rank-name">{p['name']}</div>
      <div class="rank-score">★ {p['score']} / 5.0</div>
      <div class="rank-price">From {p['price']}</div>
    </div>
  </a>''' for i, p in enumerate(top_products)])

cat_nav = "\n".join([f'  <a href="/en/{CAT_SLUGS.get(cn,"cat-other")}.html" class="cat-pill">{emoji} {CAT_EN.get(cn,cn)} ({len(ps)})</a>'
    for cn, ps in list(cat_map.items())[:15]
    for emoji in [ps[0]['emoji']]])

review_cards = "\n".join([f'''  <a href="/en/{p['slug']}.html" class="review-card">
    <div class="review-thumb" style="background:linear-gradient(135deg,{p['bg'].split(',')[0].strip()},{p['bg'].split(',')[1].strip()})">
      <span style="font-size:2.5rem;">{p['emoji']}</span>
    </div>
    <div class="review-body">
      <span class="review-cat">{CAT_EN.get(p['cat'],p['cat'])}</span>
      <h3 class="review-name">{p['name']}</h3>
      <div class="review-score">★ {p['score']} / 5.0</div>
      <div class="review-price">From {p['price']}</div>
    </div>
  </a>''' for p in sorted(PRODUCTS, key=lambda x: x['score'], reverse=True)[:24]])

index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <title>Best Gadgets 2026 — Rankings & Expert Reviews | GadgetNavi</title>
  <meta name="description" content="Expert reviews and rankings for smartphones, earbuds, smartwatches, laptops and more. {len(PRODUCTS)} products reviewed in 2026.">
  <link rel="canonical" href="{BASE_URL}en/">
  <link rel="alternate" hreflang="ja" href="{BASE_URL}">
  <link rel="alternate" hreflang="en" href="{BASE_URL}en/">
  <link rel="alternate" hreflang="x-default" href="{BASE_URL}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Best Gadgets 2026 — Rankings & Expert Reviews | GadgetNavi">
  <meta property="og:description" content="Expert reviews and rankings for {len(PRODUCTS)} gadgets.">
  <meta property="og:url" content="{BASE_URL}en/">
  <meta property="og:site_name" content="GadgetNavi">
  <meta property="og:image" content="{BASE_URL}ogp-default.svg">
  <meta name="twitter:card" content="summary_large_image">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2054301472533985" crossorigin="anonymous"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-ERDKSGNEWS');</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter','Segoe UI',sans-serif; }}
    .hero {{ background: linear-gradient(135deg, var(--secondary), #0f3460); color: #fff; padding: 60px 20px; text-align: center; }}
    .hero h1 {{ font-size: clamp(1.6rem,4vw,2.8rem); font-weight: 900; margin-bottom: 12px; }}
    .hero p {{ font-size: 1rem; color: rgba(255,255,255,0.75); margin-bottom: 28px; }}
    .hero-stats {{ display: flex; justify-content: center; gap: 32px; flex-wrap: wrap; }}
    .stat {{ text-align: center; }}
    .stat-num {{ font-size: 2rem; font-weight: 900; color: var(--primary); }}
    .stat-label {{ font-size: 0.8rem; color: rgba(255,255,255,0.6); }}
    .section {{ max-width: 1100px; margin: 0 auto; padding: 48px 20px; }}
    .section-title {{ font-size: 1.5rem; font-weight: 900; margin-bottom: 24px; }}
    .cat-pills {{ display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; }}
    .cat-pill {{ padding: 8px 16px; background: var(--white); border: 1px solid var(--border); border-radius: 50px; font-size: 0.85rem; text-decoration: none; color: var(--text); transition: all 0.2s; font-weight: 600; }}
    .cat-pill:hover {{ background: var(--primary); color: #fff; border-color: var(--primary); }}
    .rank-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 16px; }}
    .rank-card {{ background: var(--white); border-radius: var(--radius); overflow: hidden; display: flex; text-decoration: none; box-shadow: var(--shadow-sm); transition: transform 0.2s; align-items: center; }}
    .rank-card:hover {{ transform: translateY(-3px); }}
    .rank-num {{ font-size: 1.5rem; font-weight: 900; color: var(--primary); padding: 0 16px; min-width: 50px; text-align: center; }}
    .rank-thumb {{ width: 64px; height: 64px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
    .rank-body {{ padding: 12px; flex: 1; }}
    .rank-cat {{ font-size: 0.72rem; color: var(--text-muted); }}
    .rank-name {{ font-size: 0.88rem; font-weight: 700; color: var(--text); line-height: 1.3; }}
    .rank-score {{ font-size: 0.82rem; color: var(--primary); font-weight: 700; }}
    .rank-price {{ font-size: 0.82rem; color: var(--text-muted); }}
    .review-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 20px; }}
    .review-card {{ background: var(--white); border-radius: var(--radius); overflow: hidden; text-decoration: none; box-shadow: var(--shadow-sm); transition: transform 0.2s; display: flex; flex-direction: column; }}
    .review-card:hover {{ transform: translateY(-4px); }}
    .review-thumb {{ height: 120px; display: flex; align-items: center; justify-content: center; }}
    .review-body {{ padding: 14px; flex: 1; display: flex; flex-direction: column; gap: 4px; }}
    .review-cat {{ font-size: 0.72rem; color: var(--text-muted); }}
    .review-name {{ font-size: 0.9rem; font-weight: 700; color: var(--text); line-height: 1.3; }}
    .review-score {{ font-size: 0.83rem; color: var(--primary); font-weight: 700; }}
    .review-price {{ font-size: 0.83rem; color: var(--text-muted); }}
    .cta-band {{ background: linear-gradient(135deg, var(--primary), #ff8c42); color: #fff; padding: 40px 20px; text-align: center; }}
    .cta-band h2 {{ font-size: 1.5rem; font-weight: 900; margin-bottom: 8px; }}
    .cta-band p {{ color: rgba(255,255,255,0.8); margin-bottom: 20px; }}
    .btn-white {{ display: inline-block; padding: 12px 32px; background: #fff; color: var(--primary); border-radius: 50px; font-weight: 800; text-decoration: none; }}
  </style>
</head>
<body>
{EN_HEADER}

<div class="hero">
  <h1>Find the Best Gadgets for 2026</h1>
  <p>Expert reviews and rankings — no BS, just honest specs, scores & verdicts</p>
  <div class="hero-stats">
    <div class="stat"><div class="stat-num">{len(PRODUCTS)}</div><div class="stat-label">Products Reviewed</div></div>
    <div class="stat"><div class="stat-num">{len(cat_map)}</div><div class="stat-label">Categories</div></div>
    <div class="stat"><div class="stat-num">5.0</div><div class="stat-label">Max Score</div></div>
  </div>
</div>

<div class="section" id="ranking">
  <h2 class="section-title">Browse by Category</h2>
  <div class="cat-pills">
{cat_nav}
  </div>

  <h2 class="section-title">Top Ranked Gadgets</h2>
  <div class="rank-grid">
{ranking_cards}
  </div>
</div>

<div class="cta-band">
  <h2>Honest Reviews You Can Trust</h2>
  <p>Our team tests every product and rates it across multiple criteria.</p>
  <a href="/en/faq.html" class="btn-white">How We Review →</a>
</div>

<div class="section" id="reviews">
  <h2 class="section-title">All Reviews</h2>
  <div class="review-grid">
{review_cards}
  </div>
</div>

{EN_FOOTER}
</body>
</html>'''

with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)
print("Generated: en/index.html")

# ---- /en/faq.html ----
faq_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FAQ — GadgetNavi</title>
  <meta name="description" content="Frequently asked questions about GadgetNavi's review process, affiliate policy, and how we rate gadgets.">
  <link rel="canonical" href="{BASE_URL}en/faq.html">
  <link rel="alternate" hreflang="ja" href="{BASE_URL}faq.html">
  <link rel="alternate" hreflang="en" href="{BASE_URL}en/faq.html">
  <link rel="alternate" hreflang="x-default" href="{BASE_URL}faq.html">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-ERDKSGNEWS');</script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{"@type":"Question","name":"How do you score products?","acceptedAnswer":{{"@type":"Answer","text":"We evaluate each product across 4–6 criteria (e.g., camera, battery, design) on a 1–5 scale, then compute a weighted average for the Overall Score."}}}},
      {{"@type":"Question","name":"Do you accept paid reviews?","acceptedAnswer":{{"@type":"Answer","text":"No. All reviews are independently written by our editorial team. We are not paid by manufacturers and do not accept sponsored content."}}}},
      {{"@type":"Question","name":"Do you earn commissions from affiliate links?","acceptedAnswer":{{"@type":"Answer","text":"Yes. GadgetNavi participates in affiliate programs (Amazon Associates, Rakuten Affiliate). We may earn a commission when you purchase via our links, at no extra cost to you. This does not influence our scores or recommendations."}}}},
      {{"@type":"Question","name":"How current are your reviews?","acceptedAnswer":{{"@type":"Answer","text":"All reviews are based on information as of early 2026. We update pages when major firmware changes or price drops occur."}}}},
      {{"@type":"Question","name":"Can I request a product review?","acceptedAnswer":{{"@type":"Answer","text":"Yes! Send your request via the Contact page and we will consider it for an upcoming review cycle."}}}},
      {{"@type":"Question","name":"Are prices accurate?","acceptedAnswer":{{"@type":"Answer","text":"Prices shown are approximate as of April 2026. Actual prices change frequently — always check the retailer for the latest price."}}}},
      {{"@type":"Question","name":"Which stores do you link to?","acceptedAnswer":{{"@type":"Answer","text":"We primarily link to Amazon Japan and Rakuten Ichiba. These are among the most popular online retailers in Japan with reliable shipping."}}}},
      {{"@type":"Question","name":"Do you review products outside Japan?","acceptedAnswer":{{"@type":"Answer","text":"Currently our primary market is Japan. Most products are available internationally; links point to Amazon Japan and Rakuten."}}}}
    ]
  }}
  </script>
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter','Segoe UI',sans-serif; }}
    .faq-wrap {{ max-width: 800px; margin: 0 auto; padding: 48px 20px 80px; }}
    .faq-wrap h1 {{ font-size: 2rem; font-weight: 900; margin-bottom: 8px; }}
    .faq-wrap .subtitle {{ color: var(--text-muted); margin-bottom: 40px; }}
    .faq-item {{ border: 1px solid var(--border); border-radius: var(--radius); margin-bottom: 12px; overflow: hidden; }}
    .faq-q {{ padding: 18px 20px; font-weight: 700; cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: var(--white); }}
    .faq-q:hover {{ background: #f9f9f9; }}
    .faq-a {{ padding: 0 20px; max-height: 0; overflow: hidden; transition: max-height 0.3s, padding 0.3s; background: var(--bg); font-size: 0.93rem; line-height: 1.8; color: #444; }}
    .faq-a.open {{ max-height: 300px; padding: 16px 20px; }}
    .arrow {{ transition: transform 0.3s; }}
    .faq-item.open .arrow {{ transform: rotate(180deg); }}
  </style>
</head>
<body>
{EN_HEADER}
<div style="background:var(--bg);padding:20px;min-height:80vh;">
<div class="faq-wrap">
  <h1>Frequently Asked Questions</h1>
  <p class="subtitle">Learn how GadgetNavi reviews, rates, and recommends gadgets.</p>

  <div class="faq-item">
    <div class="faq-q">How do you score products? <span class="arrow">▼</span></div>
    <div class="faq-a">We evaluate each product across 4–6 criteria (e.g., camera, battery, design) on a 1–5 scale, then compute a weighted average for the Overall Score.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">Do you accept paid reviews? <span class="arrow">▼</span></div>
    <div class="faq-a">No. All reviews are independently written by our editorial team. We are not paid by manufacturers and do not accept sponsored content.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">Do you earn commissions from affiliate links? <span class="arrow">▼</span></div>
    <div class="faq-a">Yes. GadgetNavi participates in affiliate programs (Amazon Associates, Rakuten Affiliate). We may earn a commission when you purchase via our links, at no extra cost to you. This does not influence our scores or recommendations.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">How current are your reviews? <span class="arrow">▼</span></div>
    <div class="faq-a">All reviews are based on information as of early 2026. We update pages when major firmware changes or price drops occur.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">Can I request a product review? <span class="arrow">▼</span></div>
    <div class="faq-a">Yes! Send your request via the <a href="/en/contact.html">Contact page</a> and we will consider it for an upcoming review cycle.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">Are prices accurate? <span class="arrow">▼</span></div>
    <div class="faq-a">Prices shown are approximate as of April 2026. Actual prices change frequently — always check the retailer for the latest price.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">Which stores do you link to? <span class="arrow">▼</span></div>
    <div class="faq-a">We primarily link to Amazon Japan and Rakuten Ichiba. These are among the most popular online retailers in Japan with reliable shipping.</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">Do you review products outside Japan? <span class="arrow">▼</span></div>
    <div class="faq-a">Currently our primary market is Japan. Most products are available internationally; links point to Amazon Japan and Rakuten.</div>
  </div>
</div>
</div>
{EN_FOOTER}
<script>
  document.querySelectorAll('.faq-q').forEach(q => {{
    q.addEventListener('click', () => {{
      const item = q.parentElement;
      const ans = item.querySelector('.faq-a');
      item.classList.toggle('open');
      ans.classList.toggle('open');
    }});
  }});
</script>
</body>
</html>'''

with open(os.path.join(OUTPUT_DIR, 'faq.html'), 'w', encoding='utf-8') as f:
    f.write(faq_html)
print("Generated: en/faq.html")

# ---- /en/contact.html ----
contact_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact — GadgetNavi</title>
  <meta name="description" content="Contact GadgetNavi editorial team for review requests, corrections or general inquiries.">
  <link rel="canonical" href="{BASE_URL}en/contact.html">
  <link rel="alternate" hreflang="ja" href="{BASE_URL}contact.html">
  <link rel="alternate" hreflang="en" href="{BASE_URL}en/contact.html">
  <link rel="alternate" hreflang="x-default" href="{BASE_URL}contact.html">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-ERDKSGNEWS');</script>
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter','Segoe UI',sans-serif; }}
    .contact-wrap {{ max-width: 640px; margin: 0 auto; padding: 48px 20px 80px; }}
    .contact-wrap h1 {{ font-size: 2rem; font-weight: 900; margin-bottom: 8px; }}
    .contact-wrap p {{ color: var(--text-muted); margin-bottom: 32px; line-height: 1.7; }}
    .contact-form label {{ display: block; font-weight: 700; font-size: 0.88rem; margin-bottom: 6px; }}
    .contact-form input, .contact-form textarea, .contact-form select {{
      width: 100%; padding: 12px 16px; border: 1px solid var(--border); border-radius: var(--radius-sm);
      font-size: 0.95rem; font-family: inherit; background: var(--white); color: var(--text); margin-bottom: 20px;
    }}
    .contact-form textarea {{ resize: vertical; min-height: 140px; }}
    .contact-form button {{ background: var(--primary); color: #fff; padding: 13px 36px; border: none; border-radius: 50px; font-size: 1rem; font-weight: 800; cursor: pointer; transition: opacity 0.2s; }}
    .contact-form button:hover {{ opacity: 0.85; }}
  </style>
</head>
<body>
{EN_HEADER}
<div style="background:var(--bg);padding:20px;min-height:80vh;">
<div class="contact-wrap">
  <h1>Contact Us</h1>
  <p>Have a question, review request or found an error? We read every message and typically reply within 3 business days.</p>
  <form class="contact-form" action="https://formspree.io/f/xlgokalq" method="POST">
    <label for="name">Your Name</label>
    <input type="text" id="name" name="name" placeholder="John Smith" required>
    <label for="email">Email Address</label>
    <input type="email" id="email" name="email" placeholder="john@example.com" required>
    <label for="subject">Subject</label>
    <select id="subject" name="subject">
      <option value="review-request">Review Request</option>
      <option value="correction">Correction / Error Report</option>
      <option value="affiliate">Affiliate / Partnership</option>
      <option value="other">Other</option>
    </select>
    <label for="message">Message</label>
    <textarea id="message" name="message" placeholder="Please describe your inquiry..." required></textarea>
    <button type="submit">Send Message →</button>
  </form>
</div>
</div>
{EN_FOOTER}
</body>
</html>'''

with open(os.path.join(OUTPUT_DIR, 'contact.html'), 'w', encoding='utf-8') as f:
    f.write(contact_html)
print("Generated: en/contact.html")

# ---- /en/privacy.html ----
privacy_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy — GadgetNavi</title>
  <meta name="description" content="GadgetNavi privacy policy — how we collect, use and protect your data.">
  <link rel="canonical" href="{BASE_URL}en/privacy.html">
  <link rel="alternate" hreflang="ja" href="{BASE_URL}privacy.html">
  <link rel="alternate" hreflang="en" href="{BASE_URL}en/privacy.html">
  <link rel="alternate" hreflang="x-default" href="{BASE_URL}privacy.html">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-ERDKSGNEWS');</script>
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter','Segoe UI',sans-serif; }}
    .privacy-wrap {{ max-width: 760px; margin: 0 auto; padding: 48px 20px 80px; }}
    .privacy-wrap h1 {{ font-size: 2rem; font-weight: 900; margin-bottom: 8px; }}
    .privacy-wrap .updated {{ color: var(--text-muted); font-size: 0.85rem; margin-bottom: 40px; }}
    .privacy-wrap h2 {{ font-size: 1.2rem; font-weight: 800; margin: 32px 0 10px; padding-left: 12px; border-left: 4px solid var(--primary); }}
    .privacy-wrap p, .privacy-wrap li {{ font-size: 0.93rem; line-height: 1.85; color: #444; margin-bottom: 12px; }}
    .privacy-wrap ul {{ padding-left: 20px; }}
  </style>
</head>
<body>
{EN_HEADER}
<div style="background:var(--bg);padding:20px;min-height:80vh;">
<div class="privacy-wrap">
  <h1>Privacy Policy</h1>
  <p class="updated">Last updated: April 2026</p>

  <h2>1. Overview</h2>
  <p>GadgetNavi ("we", "our", "us") respects your privacy. This policy explains what data we collect, how we use it, and your rights.</p>

  <h2>2. Data We Collect</h2>
  <ul>
    <li><strong>Analytics data</strong> — via Google Analytics 4 (GA4). We collect anonymised usage data such as page views, session duration and country. No personally identifiable information is stored.</li>
    <li><strong>Contact form data</strong> — name and email address you submit via our contact form (processed by Formspree).</li>
    <li><strong>Advertising data</strong> — Google AdSense may collect cookie data for ad personalisation. You can opt out via <a href="https://adssettings.google.com/" target="_blank" rel="noopener">Google Ad Settings</a>.</li>
  </ul>

  <h2>3. Affiliate Links</h2>
  <p>This site contains affiliate links to Amazon Japan and Rakuten. When you click a link and make a purchase, we may earn a commission at no extra cost to you. This does not influence our editorial reviews or scores.</p>

  <h2>4. Cookies</h2>
  <p>We use cookies for analytics (GA4) and advertising (AdSense). You can disable cookies in your browser settings. Some site features may not function correctly if cookies are disabled.</p>

  <h2>5. Third-Party Services</h2>
  <ul>
    <li>Google Analytics 4 — <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Privacy Policy</a></li>
    <li>Google AdSense — <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Privacy Policy</a></li>
    <li>Formspree — <a href="https://formspree.io/legal/privacy-policy" target="_blank" rel="noopener">Formspree Privacy Policy</a></li>
  </ul>

  <h2>6. Your Rights</h2>
  <p>You may request access to, correction of, or deletion of any personal data we hold. Contact us via the <a href="/en/contact.html">Contact page</a>.</p>

  <h2>7. Changes to This Policy</h2>
  <p>We may update this policy from time to time. The latest version will always be posted on this page with an updated date.</p>
</div>
</div>
{EN_FOOTER}
</body>
</html>'''

with open(os.path.join(OUTPUT_DIR, 'privacy.html'), 'w', encoding='utf-8') as f:
    f.write(privacy_html)
print("Generated: en/privacy.html")
print("All English static pages done.")
