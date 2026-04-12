# -*- coding: utf-8 -*-
from datetime import datetime

SITE = "https://auto-affiliate-blog-mauve.vercel.app/"
today = datetime.now().strftime("%Y-%m-%d")

with open('C:/Users/81804/OneDrive/デスクトップ/auto-affiliate-blog-main/sitemap.xml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if '</urlset>' in line:
        continue
    new_lines.append(line)

from _v2_data import COMPARISONS

for c in COMPARISONS:
    # JA
    new_lines.append(f"  <url>\n")
    new_lines.append(f"    <loc>{SITE}{c['slug']}.html</loc>\n")
    new_lines.append(f"    <lastmod>{today}</lastmod>\n")
    new_lines.append(f"    <changefreq>weekly</changefreq>\n")
    new_lines.append(f"    <priority>0.7</priority>\n")
    new_lines.append(f"  </url>\n")
    # EN
    new_lines.append(f"  <url>\n")
    new_lines.append(f"    <loc>{SITE}en/{c['slug']}.html</loc>\n")
    new_lines.append(f"    <lastmod>{today}</lastmod>\n")
    new_lines.append(f"    <changefreq>weekly</changefreq>\n")
    new_lines.append(f"    <priority>0.7</priority>\n")
    new_lines.append(f"  </url>\n")

new_lines.append("</urlset>\n")

with open('C:/Users/81804/OneDrive/デスクトップ/auto-affiliate-blog-main/sitemap.xml', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Updated sitemap.xml with comparison URLs.")
