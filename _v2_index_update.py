# -*- coding: utf-8 -*-
import os

def update_index(path, lang="ja"):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Nav update
    if lang == "ja":
        old_nav = '<a href="#reviews">レビュー</a>'
        new_nav = '<a href="#reviews">レビュー</a>\n      <a href="#compare">比較</a>'
    else:
        old_nav = '<a href="#reviews">Reviews</a>'
        new_nav = '<a href="#reviews">Reviews</a>\n      <a href="#compare">Compare</a>'
    
    if old_nav in content and '<a href="#compare">' not in content:
        content = content.replace(old_nav, new_nav)

    # Section update
    if '<section class="section" id="compare">' in content:
        return # Already exists

    from _v2_data import COMPARISONS
    
    # Group by category
    cats = {}
    for c in COMPARISONS:
        cat = c["cat_en"] if lang == "en" else c["cat"]
        if cat not in cats: cats[cat] = []
        cats[cat].append(c)

    section_html = f'<section class="section" id="compare" style="background:#f9f9f9">\n'
    section_html += f'  <div class="container">\n'
    section_header = '比較記事' if lang == "ja" else 'Comparisons'
    section_sub = '2026年最新ガジェットを徹底比較。後悔しない選び方を提案。' if lang == "ja" else 'In-depth 2026 gadget comparisons to help you choose right.'
    section_html += f'    <div class="section-header">\n'
    section_html += f'      <div class="section-label">■ COMPARE</div>\n'
    section_html += f'      <h2>{section_header}</h2>\n'
    section_html += f'      <p>{section_sub}</p>\n'
    section_html += f'    </div>\n'

    section_html += '    <style>\n'
    section_html += '      .cmp-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px;margin-bottom:32px}\n'
    section_html += '      .cmp-card{display:flex;align-items:center;gap:12px;background:#fff;border:1.5px solid var(--border);border-radius:var(--radius-sm);padding:14px;text-decoration:none;transition:all .2s}\n'
    section_html += '      .cmp-card:hover{border-color:var(--primary);transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,.05)}\n'
    section_html += '      .cmp-emoji{font-size:1.4rem}\n'
    section_html += '      .cmp-info{flex:1}\n'
    section_html += '      .cmp-name{font-size:.84rem;font-weight:700;color:#222;line-height:1.4}\n'
    section_html += '      .cmp-cat{font-size:.72rem;color:var(--text-light);margin-bottom:2px}\n'
    section_html += '    </style>\n'

    for cat, items in cats.items():
        section_html += f'    <h3 style="font-size:1rem;font-weight:800;margin:24px 0 12px;color:var(--secondary);border-bottom:2px solid var(--border);padding-bottom:6px">{cat}</h3>\n'
        section_html += f'    <div class="cmp-grid">\n'
        for i in items[:8]: # Show up to 8 per category
            href = f'/{i["slug"]}.html' if lang == "ja" else f'/en/{i["slug"]}.html'
            section_html += f'      <a href="{href}" class="cmp-card">\n'
            section_html += f'        <div class="cmp-emoji">{i["emoji"]}</div>\n'
            section_html += f'        <div class="cmp-info">\n'
            section_html += f'          <div class="cmp-cat">{cat}</div>\n'
            section_html += f'          <div class="cmp-name">{i["a"]["name"]} <span style="color:var(--primary)">vs</span> {i["b"]["name"]}</div>\n'
            section_html += f'        </div>\n'
            section_html += f'      </a>\n'
        section_html += f'    </div>\n'

    section_html += '  </div>\n</section>\n\n'

    content = content.replace('<section class="section" id="features">', section_html + '<section class="section" id="features">')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

BASE = r"C:\Users\81804\OneDrive\デスクトップ\auto-affiliate-blog-main"
update_index(os.path.join(BASE, "index.html"), "ja")
update_index(os.path.join(BASE, "en", "index.html"), "en")
print("Updated index files.")
