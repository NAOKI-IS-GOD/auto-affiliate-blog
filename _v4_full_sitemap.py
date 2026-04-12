# -*- coding: utf-8 -*-
import os, glob

BASE = r"C:\Users\81804\OneDrive\デスクトップ\auto-affiliate-blog-main"
SITE = "https://auto-affiliate-blog-mauve.vercel.app/"
from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")

# 1. 現存する全HTMLファイルをスキャン
# ルート (JA)
ja_files = [f for f in os.listdir(BASE) if f.endswith('.html') and f != 'sitemap-page.html']
# en/ (EN)
en_files = [f for f in os.listdir(os.path.join(BASE, 'en')) if f.endswith('.html')]

all_urls = []

# ルートのURLを追加
for f in ja_files:
    all_urls.append(f"{SITE}{f}")

# en/のURLを追加
for f in en_files:
    all_urls.append(f"{SITE}en/{f}")

# 2. sitemap.xml を再構築
xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'

for url in sorted(list(set(all_urls))):
    # 優先度設定
    priority = "1.0" if "index.html" in url else "0.8"
    if "compare-" in url: priority = "0.7"
    if "cat-" in url: priority = "0.9"
    
    xml += f'  <url>\n'
    xml += f'    <loc>{url}</loc>\n'
    xml += f'    <lastmod>{today}</lastmod>\n'
    xml += f'    <changefreq>weekly</changefreq>\n'
    xml += f'    <priority>{priority}</priority>\n'
    xml += f'  </url>\n'

xml += '</urlset>\n'

with open(os.path.join(BASE, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(xml)

# 3. robots.txt を作成
robots = f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n"
with open(os.path.join(BASE, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots)

print(f"Updated sitemap.xml with {len(all_urls)} URLs and created robots.txt")
