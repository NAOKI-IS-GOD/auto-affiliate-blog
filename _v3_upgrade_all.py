# -*- coding: utf-8 -*-
import os, sys

BASE = r"C:\Users\81804\OneDrive\デスクトップ\auto-affiliate-blog-main"
sys.path.append(BASE)

def upgrade_main_gen(filename, lang="ja"):
    path = os.path.join(BASE, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 比較データを読み込む
    from _v2_data import COMPARISONS
    comp_map = {}
    for c in COMPARISONS:
        asl, bsl = c['a']['slug'], c['b']['slug']
        for s in [asl, bsl]:
            if s not in comp_map: comp_map[s] = []
            other = c['b']['name'] if s == asl else c['a']['name']
            comp_map[s].append({'slug': c['slug'], 'other': other, 'emoji': c['emoji']})

    # Pythonコード内に comp_map を埋め込むか、実行時に計算させる
    # ここでは、各ページのHTML生成ループの直前に、比較リンクのHTMLを生成するコードを挿入する

    # 既存のHTMLテンプレート部分を探す (<footer> の手前など)
    insertion_point = "<!-- Related Reviews -->" if lang == "ja" else "<!-- Related Reviews -->"
    
    if insertion_point in content and "<!-- Compare Links -->" not in content:
        # このスクリプト自体が generate.py の中で実行されるように書き換えるのは複雑なので、
        # 生成された HTML ファイルを直接後処理する方式にする
        print(f"Post-processing reviews for {filename}...")
        return comp_map
    return None

# 全レビューHTMLを後処理して比較リンクを差し込む
def post_process_reviews(comp_map, lang="ja"):
    prefix = "" if lang == "ja" else "en/"
    for slug, comps in comp_map.items():
        file_path = os.path.join(BASE, prefix, f"{slug}.html")
        if not os.path.exists(file_path): continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        if "<!-- Compare Links -->" in html: continue

        title = "あわせて読みたい比較記事" if lang == "ja" else "Related Comparisons"
        label = "COMPARE"
        
        sec = f'<!-- Compare Links -->\n<section class="section" style="background:#f0f4f8;border-top:1px solid #e2e8f0">\n  <div class="container">\n    <div class="section-header">\n      <div class="section-label">■ {label}</div>\n      <h2>{title}</h2>\n    </div>\n    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px;">'
        
        for c in comps:
            href = f'/{c["slug"]}.html' if lang == "ja" else f'/en/{c["slug"]}.html'
            sec += f'<a href="{href}" class="card" style="display:flex;align-items:center;gap:12px;padding:16px;text-decoration:none;background:#fff;border:1px solid #cbd5e1;border-radius:8px;transition:all .2s;">'
            sec += f'<div style="font-size:1.5rem">{c["emoji"]}</div>'
            sec += f'<div><div style="font-size:.7rem;color:#64748b;font-weight:700">{"比較" if lang == "ja" else "COMPARE"}</div>'
            sec += f'<div style="font-size:.9rem;font-weight:700;color:#1e293b">vs {c["other"]}</div></div></a>'
        
        sec += '</div></div></section>\n'
        
        # Insert before footer or related section
        if '<!-- Related Reviews -->' in html:
            html = html.replace('<!-- Related Reviews -->', sec + '<!-- Related Reviews -->')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)

# 1. データ再生成 (具体的コンテンツへ)
print("Step 1: Regenerating data with specs...")
os.system(f"python {os.path.join(BASE, '_v2_data_gen.py')}")

# 2. 比較ページ再生成 (アフィリエイトID適用)
print("Step 2: Regenerating comparison pages...")
os.system(f"python {os.path.join(BASE, '_v2_gen.py')}")

# 3. メインレビューHTML生成
print("Step 3: Regenerating main reviews...")
os.system(f"python {os.path.join(BASE, 'generate.py')}")
os.system(f"python {os.path.join(BASE, 'generate_en.py')}")

# 4. 相互リンク差し込み (後処理)
print("Step 4: Adding internal links...")
from _v2_data import COMPARISONS
comp_map_ja = {}
for c in COMPARISONS:
    for s in [c['a']['slug'], c['b']['slug']]:
        if s not in comp_map_ja: comp_map_ja[s] = []
        other = c['b']['name'] if s == c['a']['slug'] else c['a']['name']
        comp_map_ja[s].append({'slug': c['slug'], 'other': other, 'emoji': c['emoji']})

post_process_reviews(comp_map_ja, "ja")
post_process_reviews(comp_map_ja, "en")

print("Upgrade complete!")
