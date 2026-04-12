# -*- coding: utf-8 -*-
import os, sys

BASE = r"C:\Users\81804\OneDrive\デスクトップ\auto-affiliate-blog-main"

def clean_index_html(path, lang="ja"):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 汚いインラインスタイルやCSSを削除
    import re
    content = re.sub(r'<style>\s*\.cmp-grid.*?<\/style>', '', content, flags=re.DOTALL)
    
    # 2. Ranking Section のHTMLを再生成 (Clean version)
    from _v2_gen import CAT_SLUG
    CAT_INFO = {
        "スマートフォン": "📱", "イヤホン": "🎧", "スマートウォッチ": "⌚",
        "タブレット": "📟", "ノートPC": "💻", "ゲーム機": "🎮",
        "モニター": "🖥️", "カメラ": "📷", "ロボット掃除機": "🤖", "スピーカー": "🔊"
    }
    
    sec_title = "最新おすすめランキング" if lang == "ja" else "Top Rankings 2026"
    sec_sub = "各カテゴリーの頂点を決める、忖度なしの厳選ベストバイ。" if lang == "ja" else "The absolute best-buy gadgets, strictly selected by performance."
    
    rank_html = f'<section class="section" id="rank" style="background:#fff">\n'
    rank_html += f'  <div class="container">\n'
    rank_html += f'    <div class="section-header">\n'
    rank_html += f'      <div class="section-label">■ RANKING</div>\n'
    rank_html += f'      <h2>{sec_title}</h2>\n'
    rank_html += f'      <p>{sec_sub}</p>\n'
    rank_html += f'    </div>\n'
    rank_html += '    <div class="cat-rank-grid">\n'
    
    for cat_ja, slug_ja in CAT_SLUG.items():
        emoji = CAT_INFO.get(cat_ja, "📦")
        rank_slug = slug_ja.replace("cat-", "rank-")
        href = f"/{rank_slug}" if lang == "ja" else f"/en/{rank_slug}"
        
        display_name = cat_ja if lang == "ja" else cat_ja
        if lang == "en":
            en_names = {"スマートフォン":"Smartphones","イヤホン":"Earphones","スマートウォッチ":"Watches","タブレット":"Tablets","ノートPC":"Laptops","ゲーム機":"Gaming","モニター":"Monitors","カメラ":"Cameras","ロボット掃除機":"Vacuums","スピーカー":"Speakers"}
            display_name = en_names.get(cat_ja, cat_ja)

        rank_html += f'      <a href="{href}" class="cat-rank-card">\n'
        rank_html += f'        <span class="cat-rank-emoji">{emoji}</span>\n'
        rank_html += f'        <div class="cat-rank-name">{display_name}</div>\n'
        rank_html += f'        <div class="cat-rank-link">{"ランキングを見る" if lang=="ja" else "VIEW RANKING"} →</div>\n'
        rank_html += f'      </a>\n'
    rank_html += '    </div>\n  </div>\n</section>\n'

    # 3. Compare Section のHTMLもクリーンにする
    from _v2_data import COMPARISONS
    comp_html = f'<section class="section" id="compare" style="background:#f9f9f9">\n'
    comp_html += f'  <div class="container">\n'
    comp_title = '比較記事' if lang == "ja" else 'Comparisons'
    comp_sub = '2026年最新ガジェットを徹底比較。後悔しない選び方を提案。' if lang == "ja" else 'In-depth 2026 gadget comparisons to help you choose right.'
    comp_html += f'    <div class="section-header">\n'
    comp_html += f'      <div class="section-label">■ COMPARE</div>\n'
    comp_html += f'      <h2>{comp_title}</h2>\n'
    comp_html += f'      <p>{comp_sub}</p>\n'
    comp_html += f'    </div>\n'
    comp_html += '    <div class="cmp-grid">\n'
    
    # 既存のロジックと同様に各カテゴリーから抽出
    cats = {}
    for c in COMPARISONS:
        cat = c["cat_en"] if lang == "en" else c["cat"]
        if cat not in cats: cats[cat] = []
        cats[cat].append(c)
    
    # 表示する比較ペアを絞る（多すぎると重いので各2件程度）
    for cat, items in cats.items():
        for i in items[:2]:
            href = f'/{i["slug"]}.html' if lang == "ja" else f'/en/{i["slug"]}.html'
            comp_html += f'      <a href="{href}" class="cmp-card">\n'
            comp_html += f'        <div class="cmp-emoji">{i["emoji"]}</div>\n'
            comp_html += f'        <div class="cmp-info">\n'
            comp_html += f'          <div class="cmp-cat">{cat}</div>\n'
            comp_html += f'          <div class="cmp-name">{i["a"]["name"]} <span style="color:var(--primary)">vs</span> {i["b"]["name"]}</div>\n'
            comp_html += f'        </div>\n'
            comp_html += f'      </a>\n'
    comp_html += '    </div>\n  </div>\n</section>\n'

    # 4. コンテンツ置換
    # 既存の rank と compare セクションを削除して新しいものを入れる
    content = re.sub(r'<section class="section" id="rank".*?<\/section>', '', content, flags=re.DOTALL)
    content = re.sub(r'<section class="section" id="compare".*?<\/section>', '', content, flags=re.DOTALL)
    
    # #features の手前に挿入
    content = content.replace('<section class="section" id="features">', rank_html + comp_html + '<section class="section" id="features">')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

clean_index_html(os.path.join(BASE, "index.html"), "ja")
clean_index_html(os.path.join(BASE, "en", "index.html"), "en")
print("Index files cleaned and layouts fixed.")
