# -*- coding: utf-8 -*-
import os, sys

BASE = r"C:\Users\81804\OneDrive\デスクトップ\auto-affiliate-blog-main"

def update_index_with_ranks(path, lang="ja"):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Nav update
    if lang == "ja":
        old_nav = '<a href="#compare">比較</a>'
        new_nav = '<a href="#compare">比較</a>\n      <a href="#rank">ランキング</a>'
    else:
        old_nav = '<a href="#compare">Compare</a>'
        new_nav = '<a href="#compare">Compare</a>\n      <a href="#rank">Ranking</a>'
    
    if old_nav in content and '<a href="#rank">' not in content:
        content = content.replace(old_nav, new_nav)

    # Section update (insert before #compare)
    if '<section class="section" id="rank">' in content:
        return

    from _v2_gen import CAT_SLUG
    
    sec_title = "最新おすすめランキング" if lang == "ja" else "Top Rankings 2026"
    sec_sub = "各カテゴリーの頂点を決める、忖度なしの厳選ベストバイ。" if lang == "ja" else "The absolute best-buy gadgets, strictly selected by performance."
    
    sec_html = f'<section class="section" id="rank" style="background:#fff">\n'
    sec_html += f'  <div class="container">\n'
    sec_html += f'    <div class="section-header">\n'
    sec_html += f'      <div class="section-label">■ RANKING</div>\n'
    sec_html += f'      <h2>{sec_title}</h2>\n'
    sec_html += f'      <p>{sec_sub}</p>\n'
    sec_html += f'    </div>\n'
    
    sec_html += '    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;">\n'
    
    CAT_INFO = {
        "スマートフォン": "📱", "イヤホン": "🎧", "スマートウォッチ": "⌚",
        "タブレット": "📟", "ノートPC": "💻", "ゲーム機": "🎮",
        "モニター": "🖥️", "カメラ": "📷", "ロボット掃除機": "🤖", "スピーカー": "🔊"
    }

    for cat_ja, slug_ja in CAT_SLUG.items():
        emoji = CAT_INFO.get(cat_ja, "📦")
        rank_slug = slug_ja.replace("cat-", "rank-")
        href = f"/{rank_slug}" if lang == "ja" else f"/en/{rank_slug}"
        
        display_name = cat_ja if lang == "ja" else cat_ja # Simplified
        if lang == "en":
            en_names = {"スマートフォン":"Smartphones","イヤホン":"Earphones","スマートウォッチ":"Watches","タブレット":"Tablets","ノートPC":"Laptops","ゲーム機":"Gaming","モニター":"Monitors","カメラ":"Cameras"}
            display_name = en_names.get(cat_ja, cat_ja)

        sec_html += f'      <a href="{href}" style="display:block;padding:24px;background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:12px;text-align:center;text-decoration:none;transition:.2s;" onmouseover="this.style.borderColor=\'var(--primary)\';this.style.transform=\'translateY(-3px)\'" onmouseout="this.style.borderColor=\'#e2e8f0\';this.style.transform=\'none\'">\n'
        sec_html += f'        <div style="font-size:2.5rem;margin-bottom:12px;">{emoji}</div>\n'
        sec_html += f'        <div style="font-weight:900;color:var(--secondary);font-size:0.9rem;">{display_name}</div>\n'
        sec_html += f'        <div style="font-size:0.7rem;color:var(--primary);margin-top:4px;font-weight:700;">{"ランキングを見る" if lang=="ja" else "VIEW RANKING"} →</div>\n'
        sec_html += f'      </a>\n'
        
    sec_html += '    </div>\n  </div>\n</section>\n\n'

    content = content.replace('<section class="section" id="compare"', sec_html + '<section class="section" id="compare"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

update_index_with_ranks(os.path.join(BASE, "index.html"), "ja")
update_index_with_ranks(os.path.join(BASE, "en", "index.html"), "en")

# サイトマップ再生成
os.system(f"python {os.path.join(BASE, '_v4_full_sitemap.py')}")
print("Index and Sitemap updated.")
