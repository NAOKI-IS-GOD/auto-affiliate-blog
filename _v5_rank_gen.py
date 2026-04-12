# -*- coding: utf-8 -*-
import os, sys, pathlib
from urllib.parse import quote_plus
from config import AMAZON_TAG, RAKUTEN_ID, AMZ_URL, RKT_URL

BASE = pathlib.Path(r"C:\Users\81804\OneDrive\デスクトップ\auto-affiliate-blog-main")
sys.path.append(str(BASE))
from _v2_gen import SP, CAT_SLUG

# Category Config (補完)
CAT_INFO = {
    "スマートフォン": {"en": "Smartphones", "emoji": "📱"},
    "イヤホン": {"en": "Earphones", "emoji": "🎧"},
    "スマートウォッチ": {"en": "Smartwatches", "emoji": "⌚"},
    "タブレット": {"en": "Tablets", "emoji": "📟"},
    "ノートPC": {"en": "Laptops", "emoji": "💻"},
    "ゲーム機": {"en": "Game Consoles", "emoji": "🎮"},
    "モニター": {"en": "Monitors", "emoji": "🖥️"},
    "カメラ": {"en": "Cameras", "emoji": "📷"},
    "ロボット掃除機": {"en": "Robot Vacuums", "emoji": "🤖"},
    "スピーカー": {"en": "Speakers", "emoji": "🔊"},
}

def gen_rank_page(cat_name_ja, products, lang="ja"):
    is_en = (lang == "en")
    info = CAT_INFO.get(cat_name_ja, {"en": "Gadgets", "emoji": "📦"})
    cat_display = info["en"] if is_en else cat_name_ja
    emoji = info["emoji"]
    
    title = f"【2026年最新】{cat_display}おすすめランキングTOP{len(products)}選 | ガジェットナビ"
    if is_en: title = f"Best {cat_display} 2026 - Top {len(products)} Picks | GadgetNavi"
    
    desc = f"2026年最新の{cat_display}を徹底比較。性能、コスパ、評判から厳選したおすすめランキングを紹介。"
    if is_en: desc = f"Discover the best {cat_display} of 2026. Top picks based on performance, value, and expert reviews."

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="stylesheet" href="/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap" rel="stylesheet">
  <style>
    .rank-card {{ background: #fff; border: 2px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 32px; position: relative; transition: .3s; }}
    .rank-card:hover {{ border-color: var(--primary); transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0,0,0,0.1); }}
    .rank-num {{ position: absolute; top: -15px; left: -15px; width: 45px; height: 45px; background: var(--secondary); color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 1.3rem; border: 4px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }}
    .rank-1 {{ background: #ffd700; color: #000; }}
    .score-tag {{ background: #f1f5f9; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 700; color: var(--primary); margin-bottom: 12px; display: inline-block; }}
    .spec-box {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; background: #f8fafc; padding: 16px; border-radius: 8px; margin: 16px 0; font-size: 0.85rem; }}
    .btn-row {{ display: flex; gap: 10px; margin-top: 20px; }}
    .btn {{ flex: 1; padding: 12px; border-radius: 8px; text-decoration: none; text-align: center; font-weight: 700; transition: .2s; }}
    .btn-amz {{ background: #ff9900; color: #fff; }}
    .btn-rev {{ background: #f1f5f9; color: #333; border: 1px solid #cbd5e1; }}
  </style>
</head>
<body>
<header><div class="container"><a href="{"/" if not is_en else "/en/"}" class="logo">GADGET<span>NAVI</span></a></div></header>
<main class="container" style="max-width:800px; margin-top:60px;">
  <div style="text-align:center; margin-bottom:60px;">
    <div style="font-size:3.5rem; margin-bottom:15px;">{emoji}</div>
    <h1 style="font-size:2.2rem; font-weight:900; line-height:1.3;">{title}</h1>
    <p style="color:#64748b; margin-top:10px;">{desc}</p>
  </div>
"""
    for i, p in enumerate(products):
        rank = i + 1
        n_class = "rank-1" if rank == 1 else ""
        stars = "★" * int(p['score']) + "☆" * (5 - int(p['score']))
        amz = AMZ_URL.format(kw=quote_plus(p['name']))
        rev = f"/{p['slug']}.html" if not is_en else f"/en/{p['slug']}.html"
        
        html += f"""
  <div class="rank-card">
    <div class="rank-num {n_class}">{rank}</div>
    <div class="score-tag">SCORE: {p['score']} {stars}</div>
    <h2 style="font-size:1.6rem; margin-bottom:12px;">{p['name']}</h2>
    <div class="spec-box">
      <div><strong>Chip:</strong> {p['specs'][2]}</div>
      <div><strong>Display:</strong> {p['specs'][1]}</div>
      <div><strong>Battery:</strong> {p['specs'][6]}</div>
      <div><strong>Price:</strong> {p['specs'][11] if not is_en else p['specs'][12]}</div>
    </div>
    <p style="color:#475569; line-height:1.6; font-size:0.95rem;">{p['specs'][12] if is_en else "2026年最高クラスの性能を誇る一台。圧倒的な処理能力と使い勝手の良さで、多くのユーザーに支持されています。"}</p>
    <div class="btn-row">
      <a href="{amz}" class="btn btn-amz" target="_blank">Amazonでチェック</a>
      <a href="{rev}" class="btn btn-rev">詳細レビューを読む</a>
    </div>
  </div>
"""
    html += """</main>
<footer style="background:#1e293b; color:#fff; padding:60px 0; margin-top:100px; text-align:center;">
  <div class="container"><p>© 2026 GadgetNavi All Rights Reserved.</p></div>
</footer>
</body></html>"""
    return html

# Generate logic
cat_map = {}
for name, specs in SP.items():
    # Detect category (We need a mapping or check the SP structure)
    # Since we don't have cat in SP directly, let's use the first 10 articles category
    # Or rely on the fact that some categories are known.
    # For now, let's use the cat name directly if we can match it.
    pass

# Simplified: We'll use the Category Slugs we already have
for cat_ja, slug_ja in CAT_SLUG.items():
    prods = []
    # This is a bit manual but accurate for the current project
    for name, specs in SP.items():
        # Match products to category (Smartphone products contain "iPhone", "Galaxy", "Pixel", etc.)
        is_match = False
        if cat_ja == "スマートフォン" and any(x in name for x in ["iPhone", "Galaxy S", "Pixel", "Xperia 1", "Xiaomi", "Nothing Phone"]): is_match = True
        elif cat_ja == "イヤホン" and any(x in name for x in ["WF-", "QC", "Buds", "Tour", "Ear", "Liberty", "MOMENTUM", "EAH-", "WH-"]): is_match = True
        elif cat_ja == "スマートウォッチ" and any(x in name for x in ["Watch", "Fenix", "Venu"]): is_match = True
        elif cat_ja == "タブレット" and any(x in name for x in ["iPad", "Tab S", "Kindle"]): is_match = True
        elif cat_ja == "ノートPC" and any(x in name for x in ["MacBook", "XPS", "Surface", "ThinkPad", "Zephyrus", "Blade"]): is_match = True
        elif cat_ja == "ゲーム機" and any(x in name for x in ["Switch", "PS5", "Xbox"]): is_match = True
        elif cat_ja == "モニター" and any(x in name for x in ["GP850", "PG279", "Odyssey", "GR95", "PD32", "U2723"]): is_match = True
        elif cat_ja == "カメラ" and any(x in name for x in ["ZV-", "EOS", "X-T", "α7", "HERO", "Action", "X4"]): is_match = True
        
        if is_match:
            try:
                raw_score = specs[0].replace("型","").split("〜")[0].split(" ")[0].strip()
                score = float(raw_score) if "." in raw_score else 4.8
            except:
                score = 4.8
            
            prods.append({
                "name": name, "score": score,
                "specs": specs,
                "slug": "review-" + name.lower().replace(" ", "").replace("-", "").replace("α", "a")
            })
    
    # Adjust scores based on specific products (Manual boost for top ones)
    for p in prods:
        if "Pro Max" in p['name'] or "Ultra" in p['name'] or "M4" in p['name']: p['score'] = 4.9
        if "SE" in p['name'] or "9a" in p['name']: p['score'] = 4.5
        
    prods.sort(key=lambda x: x['score'], reverse=True)
    if not prods: continue

    # Write JA
    (BASE / slug_ja.replace("cat-", "rank-")).write_text(gen_rank_page(cat_ja, prods[:10], "ja"), encoding="utf-8")
    # Write EN
    (BASE / "en" / slug_ja.replace("cat-", "rank-")).write_text(gen_rank_page(cat_ja, prods[:10], "en"), encoding="utf-8")
    print(f"Rankings for {cat_ja} done.")

print("All rankings complete!")
