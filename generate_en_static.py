"""Generate English static pages: /en/index.html, /en/faq.html, /en/contact.html, /en/privacy.html"""
import os, sys, re as _re
from urllib.parse import quote_plus
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
import json

_tr_path = os.path.join(os.path.dirname(__file__), 'translations_en.json')
TR = json.load(open(_tr_path, encoding='utf-8')) if os.path.exists(_tr_path) else {}
def t(text): return TR.get(text, text)

def _ordinal(n):
    return {1:'1st',2:'2nd',3:'3rd'}.get(n, f'{n}th')

def en_name(name):
    """Replace Japanese parts in product names with English equivalents."""
    r = name
    # Generation markers
    r = _re.sub(r'（第(\d+)世代）', lambda m: f' ({_ordinal(int(m.group(1)))} Gen)', r)
    r = _re.sub(r'第(\d+)世代', lambda m: f'{_ordinal(int(m.group(1)))} Gen', r)
    # Units
    r = r.replace('インチ', '-inch').replace('キー', '-Key')
    r = r.replace('万画素', 'MP').replace('枚刃', '-blade')
    # Body/brackets
    r = r.replace('（ボディ）', ' (Body)').replace('ボディ', 'Body')
    r = r.replace('（', ' (').replace('）', ')')
    # Product-specific terms (longer strings first)
    r = r.replace('バックライトあり', 'with Backlight').replace('バックライト', 'Backlight')
    r = r.replace('ディスクエディション', 'Disc Edition')
    r = r.replace('急速調理器', 'Rapid Cooker')
    r = r.replace('ゲーミングチェア', 'Gaming Chair')
    r = r.replace('コードレス', 'Cordless')
    r = r.replace('充電器', 'Charger')
    r = r.replace('外付け', 'External')
    r = r.replace('ドック', 'Dock')
    r = r.replace('ハブ', 'Hub')
    # Brand/product names
    r = r.replace('ラムダッシュ', 'Lamdash').replace('ビストロ', 'Bistro')
    r = r.replace('ナノケア', 'NanoCare').replace('ドルツ', 'Doltz')
    r = r.replace('ヒーシオ', 'Healsio').replace('ヘルシオ', 'Healsio')
    r = r.replace('レプロナイザー', 'Repronizer').replace('ホットクック', 'Hotkook')
    r = r.replace('マグニフィカ', 'Magnifica').replace('エボ', 'Evo')
    r = r.replace('シャープ', 'Sharp').replace('シロカ', 'Siroca').replace('マキタ', 'Makita')
    r = r.replace('ポート', '-Port')
    r = r.replace('全自動コーヒーメーカー', 'Fully Automatic Coffee Maker')
    r = r.replace('スターターキット', 'Starter Kit').replace('ブリッジ', 'Bridge')
    r = _re.sub(r'\s+', ' ', r).strip()
    return r

def make_stars(score):
    if score >= 4.7: return '★★★★★'
    if score >= 4.3: return '★★★★☆'
    return '★★★☆☆'

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
    <div style="display:flex;align-items:center;gap:6px;">
      <a href="/" class="lang-btn">🇯🇵 JA</a>
      <span class="lang-btn active">🇬🇧 EN</span>
    </div>
    <button class="hamburger" id="hamburger" aria-label="Menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div class="mobile-drawer" id="mobile-drawer">
    <nav class="mobile-nav">
      <a href="/en/#ranking" class="mobile-nav-link">🏆 Rankings</a>
      <a href="/en/#reviews" class="mobile-nav-link">📝 Reviews</a>
      <div class="mobile-nav-sep">📋 Categories</div>
      <a href="/en/cat-smartphone.html" class="mobile-nav-link">📱 Smartphones</a>
      <a href="/en/cat-earphone.html" class="mobile-nav-link">🎧 Wireless Earbuds</a>
      <a href="/en/cat-laptop.html" class="mobile-nav-link">💻 Laptops</a>
      <a href="/en/cat-smartwatch.html" class="mobile-nav-link">⌚ Smartwatches</a>
      <a href="/en/cat-tablet.html" class="mobile-nav-link">📟 Tablets</a>
      <a href="/en/cat-camera.html" class="mobile-nav-link">📷 Cameras</a>
      <a href="/en/cat-gaming.html" class="mobile-nav-link">🎮 Gaming</a>
      <a href="/en/cat-tv.html" class="mobile-nav-link">📺 TVs</a>
      <a href="/en/cat-monitor.html" class="mobile-nav-link">🖥️ Monitors</a>
      <div class="mobile-nav-sep">🏠 Home Appliances</div>
      <a href="/en/cat-robotvacuum.html" class="mobile-nav-link">🤖 Robot Vacuums</a>
      <a href="/en/cat-cooking.html" class="mobile-nav-link">🍳 Kitchen Appliances</a>
      <a href="/en/cat-dryer.html" class="mobile-nav-link">💨 Hair Dryers</a>
      <a href="/en/cat-coffee.html" class="mobile-nav-link">☕ Coffee Makers</a>
      <a href="/en/cat-soundbar.html" class="mobile-nav-link">🔊 Soundbars</a>
      <a href="/en/cat-projector.html" class="mobile-nav-link">📽️ Projectors</a>
      <a href="/en/cat-network.html" class="mobile-nav-link">📡 Network Devices</a>
      <a href="/en/cat-gamingchair.html" class="mobile-nav-link">🪑 Gaming Chairs</a>
      <a href="/en/cat-cordlessvacuum.html" class="mobile-nav-link">🧹 Cordless Vacuums</a>
      <a href="/en/cat-peripherals.html" class="mobile-nav-link">🖱️ PC Peripherals</a>
      <a href="/en/cat-smarthome.html" class="mobile-nav-link">💡 Smart Home</a>
      <div class="mobile-nav-sep">🔗 Info</div>
      <a href="/en/faq.html" class="mobile-nav-link">❓ FAQ</a>
      <a href="/en/contact.html" class="mobile-nav-link">✉️ Contact</a>
    </nav>
  </div>
</header>'''

HAMBURGER_JS = '''  const hamburger = document.getElementById('hamburger');
  const drawer = document.getElementById('mobile-drawer');
  if (hamburger && drawer) {
    hamburger.addEventListener('click', () => {
      const open = hamburger.classList.toggle('is-open');
      drawer.classList.toggle('is-open', open);
      hamburger.setAttribute('aria-expanded', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    drawer.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        hamburger.classList.remove('is-open');
        drawer.classList.remove('is-open');
        hamburger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }'''

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
top3 = sorted(PRODUCTS, key=lambda x: x['score'], reverse=True)[:3]
all_sorted = sorted(PRODUCTS, key=lambda x: x['score'], reverse=True)
cat_map = defaultdict(list)
for p in PRODUCTS:
    cat_map[p['cat']].append(p)

RANK_LABELS = ['🥇 Editor\'s Top Pick', '🥈 Best Value', '🥉 Great Pick']
RANK_CLASSES = ['gold', 'silver', 'bronze']

def make_rank_card(i, p):
    pname = en_name(p['name'])
    cls = RANK_CLASSES[i]
    label = RANK_LABELS[i]
    stars_str = make_stars(p['score'])
    tags_html = ''.join([f'\n            <span class="tag">{t(pro)}</span>' for pro in p['pros'][:3]])
    amazon_q = quote_plus(pname)
    return f'''      <div class="rank-card {cls}">
        <div class="rank-badge-num"><span class="rank-num-text">{i+1}</span></div>
        <div class="rank-thumb" style="background:linear-gradient(135deg,{p['bg']});">{p['emoji']}</div>
        <div class="rank-info">
          <div class="rank-label">{label}</div>
          <div class="rank-name">{pname}</div>
          <div class="rank-stars"><span class="stars">{stars_str}</span><span class="rating-val">{p['score']}</span><span class="rating-count">/ 5.0</span></div>
          <div class="rank-tags">{tags_html}
          </div>
        </div>
        <div class="rank-cta">
          <div class="rank-price-label">Best Price on Amazon</div>
          <div class="rank-price">{p['price']}</div>
          <a href="https://www.amazon.co.jp/s?k={amazon_q}" class="btn-buy" target="_blank" rel="noopener">🛒 View on Amazon</a>
          <a href="/en/{p['slug']}.html" class="btn-review-link">Read Full Review →</a>
        </div>
      </div>'''

ranking_cards_html = '\n'.join([make_rank_card(i, p) for i, p in enumerate(top3)])

def make_review_card(p):
    pname = en_name(p['name'])
    cat_en_str = CAT_EN.get(p['cat'], p['cat'])
    desc = t(p['desc'])
    desc_short = desc[:80] + '…' if len(desc) > 80 else desc
    return f'''      <article class="review-card">
        <div class="review-thumb" style="background:linear-gradient(135deg,{p['bg']});">{p['emoji']}</div>
        <div class="review-body">
          <div class="review-cat">{cat_en_str}</div>
          <h3>{pname} Review</h3>
          <p>{desc_short}</p>
          <div class="review-footer"><div class="review-score"><span class="score-star">★</span><span class="score-num">{p['score']}</span></div><a href="/en/{p['slug']}.html" class="read-link">Read more →</a></div>
        </div>
      </article>'''

review_cards_html = '\n'.join([make_review_card(p) for p in all_sorted])

index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <title>Best Gadgets 2026 — Rankings &amp; Expert Reviews | GadgetNavi</title>
  <meta name="description" content="Expert reviews and rankings for smartphones, earbuds, smartwatches, laptops and more. {len(PRODUCTS)} products reviewed in 2026.">
  <link rel="canonical" href="{BASE_URL}en/">
  <link rel="alternate" hreflang="ja" href="{BASE_URL}">
  <link rel="alternate" hreflang="en" href="{BASE_URL}en/">
  <link rel="alternate" hreflang="x-default" href="{BASE_URL}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Best Gadgets 2026 — Rankings &amp; Expert Reviews | GadgetNavi">
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
  <style>body {{ font-family: 'Inter','Segoe UI',sans-serif; }}</style>
</head>
<body>
{EN_HEADER}

<section class="hero">
  <div class="hero-inner">
    <div class="hero-pill">✦ Updated April 2026</div>
    <h1>Find Your Perfect<br><em>Gadget.</em></h1>
    <p>Smartphones, earbuds, smartwatches &amp; more —<br>specs, scores and honest verdicts</p>
    <a href="#ranking" class="hero-cta">See Rankings ↓</a>
  </div>
</section>

<div class="with-sidebar">

<aside class="sidebar" id="sidebar">
  <div class="sidebar-inner">
    <div class="sidebar-section">
      <div class="sidebar-title">📋 Categories</div>
      <ul class="sidebar-list">
        <li><a href="/en/cat-smartphone.html">📱 Smartphones</a></li>
        <li><a href="/en/cat-earphone.html">🎧 Wireless Earbuds</a></li>
        <li><a href="/en/cat-smartwatch.html">⌚ Smartwatches</a></li>
        <li><a href="/en/cat-laptop.html">💻 Laptops</a></li>
        <li><a href="/en/cat-tablet.html">📟 Tablets</a></li>
        <li><a href="/en/cat-camera.html">📷 Cameras</a></li>
        <li><a href="/en/cat-gaming.html">🎮 Gaming</a></li>
        <li><a href="/en/cat-monitor.html">🖥️ Monitors</a></li>
        <li><a href="/en/cat-peripherals.html">🖱️ PC Peripherals</a></li>
        <li><a href="/en/cat-charger.html">⚡ Chargers</a></li>
        <li><a href="/en/cat-battery.html">🔋 Power Banks</a></li>
      </ul>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-title">🏠 Home Appliances</div>
      <ul class="sidebar-list">
        <li><a href="/en/cat-tv.html">📺 TVs</a></li>
        <li><a href="/en/cat-robotvacuum.html">🤖 Robot Vacuums</a></li>
        <li><a href="/en/cat-cordlessvacuum.html">🧹 Cordless Vacuums</a></li>
        <li><a href="/en/cat-cooking.html">🍳 Kitchen Appliances</a></li>
        <li><a href="/en/cat-coffee.html">☕ Coffee Makers</a></li>
        <li><a href="/en/cat-dryer.html">💨 Hair Dryers</a></li>
        <li><a href="/en/cat-toothbrush.html">🪥 Electric Toothbrushes</a></li>
        <li><a href="/en/cat-shaver.html">🪒 Electric Shavers</a></li>
      </ul>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-title">🎵 AV &amp; Other</div>
      <ul class="sidebar-list">
        <li><a href="/en/cat-soundbar.html">🔊 Soundbars</a></li>
        <li><a href="/en/cat-speaker2.html">🔊 Speakers</a></li>
        <li><a href="/en/cat-projector.html">📽️ Projectors</a></li>
        <li><a href="/en/cat-network.html">📡 Network Devices</a></li>
        <li><a href="/en/cat-gamingchair.html">🪑 Gaming Chairs</a></li>
        <li><a href="/en/cat-smarthome.html">💡 Smart Home</a></li>
        <li><a href="/en/cat-vrar.html">🥽 VR/AR</a></li>
        <li><a href="/en/cat-ereader.html">📖 E-Readers</a></li>
      </ul>
    </div>
    <div class="sidebar-section">
      <div class="sidebar-title">🔗 Links</div>
      <ul class="sidebar-list">
        <li><a href="/en/faq.html">❓ FAQ</a></li>
        <li><a href="/en/contact.html">✉️ Contact</a></li>
        <li><a href="/en/privacy.html">🔒 Privacy Policy</a></li>
      </ul>
    </div>
  </div>
</aside>

<div class="main-content">

<section class="section" id="ranking">
  <div class="container">
    <div class="section-header">
      <div class="section-label">■ RANKING</div>
      <h2>Top Gadget Rankings 2026</h2>
      <p>Our expert picks based on specs, testing and user feedback</p>
    </div>

    <div class="ranking-list">
{ranking_cards_html}
    </div>

    <div class="rank-see-more-wrap">
      <a href="/en/cat-smartphone.html" class="rank-see-more">See All Smartphone Reviews →</a>
    </div>
  </div>
</section>

<section class="section" id="reviews">
  <div class="container">
    <div class="section-header">
      <div class="section-label">■ REVIEW</div>
      <h2>All Reviews</h2>
      <p>Specs, features and honest assessments for every product</p>
    </div>

    <div class="search-wrap">
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Search by product name or category..." autocomplete="off">
        <button class="search-clear" id="searchClear" aria-label="Clear">✕</button>
      </div>
      <div class="search-count" id="searchCount"></div>
    </div>

    <div class="reviews-grid" id="reviewsGrid">
{review_cards_html}
    </div>
  </div>
</section>

</div><!-- main-content -->
</div><!-- with-sidebar -->

{EN_FOOTER}
<button class="back-to-top" id="backToTop" aria-label="Back to top">↑</button>
<script>
  const bttBtn = document.getElementById('backToTop');
  window.addEventListener('scroll', () => {{ bttBtn.classList.toggle('visible', window.scrollY > 400); }});
  bttBtn.addEventListener('click', () => {{ window.scrollTo({{top:0,behavior:'smooth'}}); }});

  const searchInput = document.getElementById('searchInput');
  const searchClear = document.getElementById('searchClear');
  const searchCount = document.getElementById('searchCount');
  const grid = document.getElementById('reviewsGrid');
  const allCards = Array.from(grid.querySelectorAll('.review-card'));

  function doSearch(q) {{
    const kw = q.trim().toLowerCase();
    searchClear.style.display = kw ? 'block' : 'none';
    let shown = 0;
    allCards.forEach(card => {{
      const text = card.textContent.toLowerCase();
      const match = !kw || text.includes(kw);
      card.style.display = match ? '' : 'none';
      if (match) shown++;
    }});
    searchCount.textContent = kw ? shown + ' results' : '';
    searchCount.style.display = kw ? 'block' : 'none';
  }}

  searchInput.addEventListener('input', e => doSearch(e.target.value));
  searchClear.addEventListener('click', () => {{ searchInput.value = ''; doSearch(''); searchInput.focus(); }});

{HAMBURGER_JS}
</script>
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
{HAMBURGER_JS}
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
<script>
{HAMBURGER_JS}
</script>
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
<script>
{HAMBURGER_JS}
</script>
</body>
</html>'''

with open(os.path.join(OUTPUT_DIR, 'privacy.html'), 'w', encoding='utf-8') as f:
    f.write(privacy_html)
print("Generated: en/privacy.html")
print("All English static pages done.")
