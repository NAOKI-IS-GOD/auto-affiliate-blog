"""
English page generator for ガジェットナビ
Generates /en/ subdirectory with English versions of all pages
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))

# Import PRODUCTS, CAT_SLUGS, CAT_SVG_DECO from generate.py by exec
_gen_path = os.path.join(os.path.dirname(__file__), 'generate.py')
_ns = {}
exec(open(_gen_path, encoding='utf-8').read(), _ns)
PRODUCTS = _ns['PRODUCTS']
CAT_SLUGS = _ns['CAT_SLUGS']
BASE_URL = _ns['BASE_URL']
REVIEW_STYLE = _ns['REVIEW_STYLE']

from urllib.parse import quote_plus
from collections import defaultdict
import datetime, json

# Load translations
_tr_path = os.path.join(os.path.dirname(__file__), 'translations_en.json')
TR = json.load(open(_tr_path, encoding='utf-8')) if os.path.exists(_tr_path) else {}

def t(text):
    """Return English translation, fallback to original."""
    return TR.get(text, text)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'en')
os.makedirs(OUTPUT_DIR, exist_ok=True)

TODAY = datetime.date.today().isoformat()

# Category name → English
CAT_EN = {
    "スマートフォン": "Smartphones",
    "PC周辺機器": "PC Peripherals",
    "ワイヤレスイヤホン": "Wireless Earbuds",
    "スマートウォッチ": "Smartwatches",
    "ノートPC": "Laptops",
    "カメラ": "Cameras",
    "タブレット": "Tablets",
    "ゲーミング": "Gaming",
    "モニター": "Monitors",
    "充電器": "Chargers",
    "モバイルバッテリー": "Power Banks",
    "スマートスピーカー": "Smart Speakers",
    "スピーカー": "Speakers",
    "VR/AR": "VR/AR",
    "電子書籍リーダー": "E-Readers",
    "スマートホーム": "Smart Home",
    "エンタメ": "Entertainment",
    "家電": "Home Appliances",
    "テレビ": "TVs",
    "ドライヤー": "Hair Dryers",
    "電動歯ブラシ": "Electric Toothbrushes",
    "シェーバー": "Electric Shavers",
    "ロボット掃除機": "Robot Vacuums",
    "コーヒーメーカー": "Coffee Makers",
    "プロジェクター": "Projectors",
    "サウンドバー": "Soundbars",
    "ネットワーク機器": "Network Devices",
    "ゲーミングチェア": "Gaming Chairs",
    "コードレス掃除機": "Cordless Vacuums",
    "調理家電": "Kitchen Appliances",
    "電子書籍": "E-Books",
}

# Score label → English
SCORE_EN = {
    "カメラ": "Camera", "パフォーマンス": "Performance", "バッテリー": "Battery",
    "デザイン": "Design", "コスパ": "Value", "ディスプレイ": "Display",
    "音質": "Sound Quality", "ノイキャン": "ANC", "装着感": "Comfort",
    "通話品質": "Call Quality", "防水": "Water Resistance", "接続性": "Connectivity",
    "健康機能": "Health Features", "睡眠追跡": "Sleep Tracking", "Apple連携": "Apple Integration",
    "Galaxy AI": "Galaxy AI", "Wear OS": "Wear OS", "GPS精度": "GPS Accuracy",
    "軽量性": "Lightweight", "5K解像度": "5K Resolution", "Mac連携": "Mac Integration",
    "Thunderbolt": "Thunderbolt", "ゲーム性能": "Gaming Performance", "携帯性": "Portability",
    "OLED画質": "OLED Display", "QD-OLED画質": "QD-OLED Display", "応答速度": "Response Time",
    "色精度": "Color Accuracy", "HDR": "HDR", "クリエイター向け": "Creator Features",
    "AI機能": "AI Features", "センサー精度": "Sensor Accuracy", "ボタン配置": "Button Layout",
    "重量調整": "Weight Adjustment", "スポーツ向け": "Sports Performance",
    "外音認識": "Ambient Sound", "骨伝導音質": "Bone Conduction", "装着安定性": "Fit Stability",
    "フィルムシミュレーション": "Film Simulation", "コンパクト性": "Compactness",
    "防塵防滴": "Weather Sealing", "手ブレ補正": "Image Stabilization",
    "アクション性能": "Action Performance", "スタイリング多機能": "Styling Versatility",
    "髪へのやさしさ": "Hair Safety", "仕上がり": "Finish Quality", "時短性能": "Time Efficiency",
    "ゴミ自動収集": "Auto Dustbin", "障害物回避": "Obstacle Avoidance",
    "清掃能力": "Cleaning Power", "アプリ連携": "App Integration",
    "コーヒー品質": "Coffee Quality", "手軽さ": "Ease of Use", "カプセル種類": "Capsule Variety",
    "Dolby Atmos": "Dolby Atmos", "Trueplay自動調整": "Trueplay Auto-Tuning",
    "骨伝導": "Bone Conduction", "4K画質": "4K Picture Quality",
    "短焦点": "Short Throw", "ゲーミング": "Gaming", "ストリーミング": "Streaming",
    "Wi-Fi 7速度": "Wi-Fi 7 Speed", "メッシュ安定性": "Mesh Stability",
    "設定簡単さ": "Easy Setup", "セキュリティ": "Security",
    "座り心地": "Comfort", "腰サポート": "Lumbar Support", "耐久性": "Durability",
    "M4性能": "M4 Performance", "薄さ": "Thinness", "Apple Pencil Pro": "Apple Pencil Pro",
    "2-in-1設計": "2-in-1 Design", "音質": "Sound Quality",
    "充電速度": "Charging Speed", "Snapdragon 8 Elite": "Snapdragon 8 Elite",
    "Tensor G4": "Tensor G4", "A18 Pro": "A18 Pro",
    "センサー": "Sensor", "動画": "Video", "手ぶれ補正": "Image Stabilization",
    "AF": "Autofocus", "解像度": "Resolution", "明るさ": "Brightness",
    "焦点距離": "Focal Length", "コンパクト": "Compactness", "操作性": "Usability",
    "エコシステム": "Ecosystem", "発熱": "Heat Management", "価格": "Price",
    "コスト": "Cost", "サイズ感": "Size", "液晶": "LCD Quality",
    "タッチ感度": "Touch Sensitivity", "スピーカー": "Speakers", "振動": "Haptics",
    "生体認証": "Biometrics", "指紋": "Fingerprint", "顔認証": "Face ID",
    "処理速度": "Processing Speed", "発熱管理": "Thermal Management",
    "ゲーム": "Gaming", "音楽": "Music", "通話": "Call Quality",
    "メモリ": "Memory", "ストレージ速度": "Storage Speed",
}

SPEC_EN = {
    "ディスプレイ": "Display", "チップ": "Chip/Processor", "カメラ": "Camera",
    "バッテリー": "Battery", "重量": "Weight", "防水": "Water Resistance",
    "RAM": "RAM", "ストレージ": "Storage", "CPU": "CPU", "GPU": "GPU",
    "解像度": "Resolution", "パネル": "Panel", "サイズ": "Size",
    "接続": "Connectivity", "特徴": "Features", "特徴2": "Features 2",
    "センサー": "Sensor", "ドライバー": "Driver", "ノイキャン": "ANC",
    "再生時間": "Playback Time", "充電": "Charging", "コーデック": "Codecs",
    "方式": "Type", "出力": "Output", "防塵防滴": "Weather Sealing",
    "連写": "Burst Shooting", "焦点距離": "Focal Length",
    "コントラスト": "Contrast", "レンズシフト": "Lens Shift",
    "対応": "Compatibility", "OS": "OS", "電力": "Power",
    "付属品": "Included", "動画": "Video", "AF": "Autofocus",
    "手ぶれ補正": "Image Stabilization", "手ブレ補正": "Image Stabilization",
    "明るさ": "Brightness", "コントロール": "Controls", "操作": "Operation",
    "インターフェース": "Interface", "端子": "Ports", "入力": "Input",
    "出力2": "Output 2", "モード": "Mode", "センサーサイズ": "Sensor Size",
    "マウント": "Mount", "連写速度": "Burst Rate", "ISO": "ISO",
    "シャッター": "Shutter", "ファインダー": "Viewfinder", "液晶": "LCD",
    "メモリ": "Memory", "インターフェイス": "Interface",
    "メモリ": "Memory", "ストレージ速度": "Storage Speed",
    # Additional spec keys
    "USB-C単独": "USB-C Only", "アタッチメント": "Attachment", "アプリ": "App",
    "アームレスト": "Armrest", "カスタマイズ": "Customization",
    "カップサイズ": "Cup Size", "カバー範囲": "Coverage", "カラー": "Color",
    "キャリブレーション": "Calibration", "キー数": "Keys",
    "グラインダー": "Grinder", "ケーブル長": "Cable Length",
    "ゲーミング": "Gaming", "ゲーム": "Games", "スイッチ": "Switch",
    "スピーカー": "Speaker", "スポーツ": "Sports", "ソフト": "Software",
    "チャンネル": "Channels", "デザイン": "Design", "ドック": "Dock",
    "ドック出力": "Dock Output", "ノズル": "Nozzle", "ハードウェア": "Hardware",
    "バックホール": "Backhaul", "バックライト": "Backlight", "バンド": "Band",
    "フィルター": "Filter", "フィルムシミュレーション": "Film Simulation",
    "プロセッサー": "Processor", "ボタン": "Buttons", "ポート": "Ports",
    "ポーリングレート": "Polling Rate", "マイク": "Microphone",
    "マッピング": "Mapping", "マルチペアリング": "Multi-pairing",
    "メッシュ": "Mesh", "メニュー": "Menu", "モーション": "Motion",
    "モーター": "Motor", "リクライニング": "Reclining",
    "リフレッシュレート": "Refresh Rate", "リモコン": "Remote",
    "レンズ": "Lens", "レーザー": "Laser", "レーザー寿命": "Laser Lifespan",
    "予熱": "Preheat", "互換": "Compatibility", "保温": "Keep Warm",
    "入力遅延": "Input Latency", "刃": "Blade", "制御": "Control",
    "厚さ": "Thickness", "吸引力": "Suction Power", "周波数": "Frequency",
    "周波数特性": "Frequency Response", "回転": "Rotation",
    "国内規格": "Japan Standard", "圧力": "Pressure", "安全": "Safety",
    "容量": "Capacity", "対応OS": "Compatible OS",
    "対応アプリ": "Compatible Apps", "対応カプセル": "Compatible Capsules",
    "対応バッテリー": "Compatible Battery", "対応フォーマット": "Supported Formats",
    "対応体重": "Supported Weight", "対応台数": "Supported Devices",
    "応答速度": "Response Time", "急速充電": "Fast Charging",
    "感度": "Sensitivity", "技術": "Technology", "折りたたみ": "Foldable",
    "振動": "Vibration", "振動数": "Vibration Frequency",
    "接続台数": "Connected Devices", "日本メーカー": "Japanese Brand",
    "映像": "Video", "映像出力": "Video Output", "暗号化": "Encryption",
    "最大出力": "Max Output", "極性パターン": "Polar Pattern",
    "構成": "Configuration", "機能": "Features", "水拭き": "Wet Mopping",
    "洗浄": "Cleaning", "消費電力": "Power Consumption",
    "温度": "Temperature", "温度制御": "Temperature Control",
    "温湿度": "Temp/Humidity", "生産": "Manufacturing",
    "空間オーディオ": "Spatial Audio", "素材": "Material",
    "給電": "Power Supply", "耐荷重": "Load Capacity",
    "耐衝撃": "Shock Resistance", "腰サポート": "Lumbar Support",
    "自動収集": "Auto Collection", "色域": "Color Gamut",
    "色温度": "Color Temperature", "薄さ": "Thinness", "規格": "Standard",
    "視野角": "Viewing Angle", "設定": "Settings", "認定": "Certification",
    "認証": "Authentication", "調理方式": "Cooking Method",
    "調理時間": "Cooking Time", "赤外線": "Infrared",
    "転送速度": "Transfer Speed", "輝度": "Brightness", "速度": "Speed",
    "連携": "Integration", "遅延": "Latency",
    "障害物回避": "Obstacle Avoidance", "障害物検知": "Obstacle Detection",
    "電源": "Power Source", "電球": "Bulb Type", "音場補正": "Room Correction",
    "音声": "Voice", "音声アシスタント": "Voice Assistant",
    "風量": "Airflow", "騒音": "Noise Level",
}

EN_EXTRA_STYLE = """
    body { font-family: 'Inter', 'Segoe UI', sans-serif; }
    .related-articles { margin-top: 48px; }
    .related-articles h3 { font-size: 1.1rem; font-weight: 800; margin-bottom: 16px; }
    .related-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
    .related-card { background: var(--white); border-radius: var(--radius); padding: 16px; text-decoration: none; box-shadow: var(--shadow-sm); transition: transform 0.2s; display: flex; flex-direction: column; gap: 6px; }
    .related-card:hover { transform: translateY(-3px); }
    .related-thumb { font-size: 2rem; }
    .related-cat { font-size: 0.72rem; color: var(--text-muted); }
    .related-title { font-size: 0.82rem; font-weight: 700; color: var(--text); line-height: 1.4; }
    .related-score { font-size: 0.8rem; color: var(--primary); font-weight: 700; }
    .related-score span { color: #f59e0b; }
    .btn-affiliate { display: inline-block; padding: 12px 28px; background: var(--primary); color: #fff; border-radius: 50px; font-weight: 700; font-size: 0.9rem; text-decoration: none; }
    @media (max-width: 768px) {
      .related-grid { grid-template-columns: 1fr; }
    }
"""

import re as _re

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
    r = r.replace('全自動', 'Fully Automatic')
    r = r.replace('充電ステーション', 'Charging Station')
    r = r.replace('スロークッカー', 'Slow Cooker')
    r = r.replace('アロマフレッシュ', 'AromaFresh')
    r = r.replace('ノンフライヤー', 'Air Fryer')
    r = r.replace('スターターキット', 'Starter Kit').replace('ブリッジ', 'Bridge')
    r = r.replace('\u30fb', '/').replace('・', '/')  # Japanese middle dot
    r = _re.sub(r'\s+', ' ', r).strip()
    return r

def _ordinal(n):
    return {1:'1st',2:'2nd',3:'3rd'}.get(n, f'{n}th')

def get_en_score_label(label):
    return SCORE_EN.get(label, label)

def get_en_spec_key(key):
    return SPEC_EN.get(key, key)

def get_brand(name):
    bm = {"iphone":"Apple","ipad":"Apple","airpods":"Apple","macbook":"Apple","apple":"Apple",
          "galaxy":"Samsung","samsung":"Samsung","xperia":"Sony","playstation":"Sony",
          "pixel":"Google","google":"Google","kindle":"Amazon","echo":"Amazon","amazon":"Amazon",
          "sony":"Sony","logicool":"Logicool","bose":"Bose","anker":"Anker","dyson":"Dyson",
          "jabra":"Jabra","razer":"Razer","asus":"ASUS","dell":"Dell","hp":"HP","lenovo":"Lenovo",
          "lg":"LG","panasonic":"Panasonic","fujifilm":"Fujifilm","nikon":"Nikon","canon":"Canon",
          "gopro":"GoPro","jbl":"JBL","marshall":"Marshall","steelseries":"SteelSeries",
          "corsair":"Corsair","hyperx":"HyperX","garmin":"Garmin","elgato":"Elgato",
          "benq":"BenQ","shokz":"Shokz","xiaomi":"Xiaomi","oppo":"OPPO","oneplus":"OnePlus",
          "nothing":"Nothing","aquos":"Sharp","secretlab":"Secretlab","ninja":"Ninja",
          "nespresso":"Nespresso","irobot":"iRobot","roomba":"iRobot","sonos":"Sonos",
          "epson":"Epson","sennheiser":"Sennheiser","keychron":"Keychron","withings":"Withings",
          "amazfit":"Amazfit","eufy":"Eufy","motorola":"Motorola","philips":"Philips","dji":"DJI",
          "insta360":"Insta360","om":"OM SYSTEM","siroca":"siroca","melitta":"Melitta",
          "dreame":"Dreame","roborock":"Roborock","ecovacs":"Ecovacs","sharp":"Sharp",
          "hisense":"Hisense","tcl":"TCL","braun":"Braun","oral-b":"Oral-B","oralb":"Oral-B",
    }
    nl = name.lower().replace("-","").replace(" ","")
    result = next((v for k,v in bm.items() if nl.startswith(k)), None)
    if result:
        return result
    return en_name(name.split()[0])

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
      <a href="/" class="lang-btn" onclick="localStorage.setItem('gadgetnavi_lang','ja')">🇯🇵 JA</a>
      <span class="lang-btn active">🇬🇧 EN</span>
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

def generate_en_review(p):
    pname = en_name(p['name'])
    cat_en = CAT_EN.get(p['cat'], p['cat'])
    cat_slug = CAT_SLUGS.get(p['cat'], 'cat-other')
    brand = get_brand(p['name'])
    bg1, bg2 = p['bg'].split(',')
    amazon_url = f"https://www.amazon.co.jp/s?k={quote_plus(p['name'])}"
    rakuten_url = f"https://search.rakuten.co.jp/search/mall/{quote_plus(p['name'])}/"

    score_items_html = "\n".join([
        f'''        <div class="score-item">
          <span class="score-item-label">{t(label) if t(label) != label else get_en_score_label(label)}</span>
          <div class="score-bar-wrap"><div class="score-bar" style="width:{w}%;"></div></div>
          <span class="score-item-val">{val}</span>
        </div>''' for label, w, val in p['scores']
    ])
    specs_html = "\n".join([
        f'        <tr><th>{get_en_spec_key(k)}</th><td>{t(v).replace(chr(0x30fb), "/").replace("・", "/")}</td></tr>'
        for k, v in p['specs']
    ])
    # Use translated pros/cons
    en_pros = [t(x) for x in p['pros']]
    en_cons = [t(x) for x in p['cons']]

    pros_html = "\n".join([f"            <li>{x}</li>" for x in en_pros])
    cons_html = "\n".join([f"            <li>{x}</li>" for x in en_cons])
    related_html = "\n".join([
        f'''        <a href="/en/{slug}.html" class="related-card">
          <div class="related-thumb">{emoji}</div>
          <div class="related-cat">{CAT_EN.get(cat, cat)}</div>
          <div class="related-title">{en_name(title.replace(" レビュー", "").replace("レビュー", ""))} Review</div>
          <div class="related-score"><span>★</span> {score} / 5.0</div>
        </a>''' for slug, emoji, cat, title, score in p['related']
    ])

    # Use translated description, fallback to auto-generated
    en_desc_translated = t(p['desc'])
    top_score = max(p['scores'], key=lambda x: x[2])
    en_desc_auto = (f"The {pname} is a top-rated {cat_en} from {brand}, "
                    f"scoring {p['score']}/5.0. "
                    f"Particularly outstanding in {get_en_score_label(top_score[0])} ({top_score[2]}/5.0).")
    en_desc = en_desc_translated if en_desc_translated != p['desc'] else en_desc_auto

    pros_faq = ", ".join(en_pros[:3])
    cons_faq = ", ".join(en_cons[:2])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <title>{pname} Review [2026] Specs & Verdict | GadgetNavi</title>
  <meta name="description" content="{pname} review: specs, features, pros & cons. Expert score {p["score"]}/5.0. Best {cat_en} pick for 2026?">
  <link rel="canonical" href="{BASE_URL}en/{p["slug"]}.html">
  <link rel="alternate" hreflang="ja" href="{BASE_URL}{p["slug"]}.html">
  <link rel="alternate" hreflang="en" href="{BASE_URL}en/{p["slug"]}.html">
  <link rel="alternate" hreflang="x-default" href="{BASE_URL}{p["slug"]}.html">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{pname} Review [2026] | GadgetNavi">
  <meta property="og:description" content="Expert review of {pname}. Score: {p["score"]}/5.0.">
  <meta property="og:url" content="{BASE_URL}en/{p["slug"]}.html">
  <meta property="og:site_name" content="GadgetNavi">
  <meta property="og:image" content="{BASE_URL}ogp-default.svg">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Review",
    "name": "{pname} Review [2026]",
    "author": {{ "@type": "Organization", "name": "GadgetNavi Editorial" }},
    "datePublished": "2026-04-05",
    "dateModified": "{TODAY}",
    "description": "{en_desc}",
    "reviewRating": {{
      "@type": "Rating",
      "ratingValue": "{p["score"]}",
      "bestRating": "5",
      "worstRating": "1"
    }},
    "itemReviewed": {{
      "@type": "Product",
      "name": "{pname}",
      "description": "{en_desc}",
      "image": "{BASE_URL}favicon.svg",
      "brand": {{ "@type": "Brand", "name": "{brand}" }},
      "offers": {{
        "@type": "Offer",
        "priceCurrency": "JPY",
        "price": "{p["price"].replace("¥","").replace(",","")}",
        "availability": "https://schema.org/InStock",
        "url": "{BASE_URL}en/{p["slug"]}.html",
        "shippingDetails": {{
          "@type": "OfferShippingDetails",
          "shippingRate": {{ "@type": "MonetaryAmount", "value": "0", "currency": "JPY" }},
          "shippingDestination": {{ "@type": "DefinedRegion", "addressCountry": "JP" }},
          "deliveryTime": {{
            "@type": "ShippingDeliveryTime",
            "handlingTime": {{ "@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY" }},
            "transitTime": {{ "@type": "QuantitativeValue", "minValue": 1, "maxValue": 3, "unitCode": "DAY" }}
          }}
        }},
        "hasMerchantReturnPolicy": {{
          "@type": "MerchantReturnPolicy",
          "applicableCountry": "JP",
          "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
          "merchantReturnDays": 30,
          "returnMethod": "https://schema.org/ReturnByMail",
          "returnFees": "https://schema.org/FreeReturn"
        }}
      }},
      "aggregateRating": {{
        "@type": "AggregateRating",
        "ratingValue": "{p["score"]}",
        "bestRating": "5",
        "worstRating": "1",
        "reviewCount": "1"
      }}
    }},
    "publisher": {{ "@type": "Organization", "name": "GadgetNavi", "url": "{BASE_URL}" }}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "What are the pros of the {pname}?",
        "acceptedAnswer": {{ "@type": "Answer", "text": "{pros_faq}" }}
      }},
      {{
        "@type": "Question",
        "name": "What are the cons of the {pname}?",
        "acceptedAnswer": {{ "@type": "Answer", "text": "{cons_faq}" }}
      }},
      {{
        "@type": "Question",
        "name": "What is the price of the {pname}?",
        "acceptedAnswer": {{ "@type": "Answer", "text": "The {pname} is priced from {p["price"]} (JPY) on Amazon Japan." }}
      }},
      {{
        "@type": "Question",
        "name": "Is the {pname} worth buying?",
        "acceptedAnswer": {{ "@type": "Answer", "text": "GadgetNavi rates the {pname} {p["score"]}/5.0. {en_desc}" }}
      }}
    ]
  }}
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2054301472533985" crossorigin="anonymous"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-ERDKSGNEWS');</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://pagead2.googlesyndication.com">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
  <style>{REVIEW_STYLE}{EN_EXTRA_STYLE}</style>
</head>
<body>
{EN_HEADER}

<div style="background:var(--white); padding: 12px 20px; border-bottom:1px solid var(--border);">
  <div class="review-page" style="padding:0;">
    <div class="breadcrumb">
      <a href="/en/">Home</a><span>›</span>
      <a href="/en/{cat_slug}.html">{cat_en}</a><span>›</span>
      {pname} Review
    </div>
  </div>
</div>

<div style="background:var(--bg); padding: 20px;">
  <div class="review-page">

    <div class="article-header">
      <div class="article-category">{p["emoji"]} {cat_en}</div>
      <h1>[2026] {pname} Review — Specs, Features & Verdict</h1>
      <div class="article-meta">
        <div class="author"><div class="avatar">👤</div><span>GadgetNavi Editorial</span></div>
        <span>📅 April 5, 2026</span>
        <span>🕐 6 min read</span>
        <a href="{BASE_URL}{p["slug"]}.html" style="color:var(--primary);font-size:0.8rem;" onclick="localStorage.setItem('gadgetnavi_lang','ja')">🇯🇵 JP</a>
      </div>
    </div>

    <div class="article-hero" style="background:linear-gradient(135deg,{bg1.strip()},{bg2.strip()});">
      <div class="hero-illust">
        <span class="hero-illust-emoji">{p["emoji"]}</span>
        <span class="hero-illust-cat">{cat_en.upper()}</span>
      </div>
    </div>

    <div class="score-box">
      <div class="total-score">
        <div class="score-number">{p["score"]}</div>
        <div style="color:var(--accent); font-size:1.5rem;">{"★" * round(p["score"])}</div>
        <div class="score-label">Overall Score (out of 5)</div>
      </div>
      <div class="score-breakdown">
{score_items_html}
      </div>
    </div>

    <div class="affiliate-box">
      <div class="prod-name">{p["emoji"]} {pname}</div>
      <div class="prod-price">From {p["price"]}</div>
      <div class="affiliate-btns">
        <a href="{amazon_url}" class="btn-amazon" target="_blank" rel="noopener">🛒 Buy on Amazon Japan</a>
        <a href="{rakuten_url}" class="btn-rakuten" target="_blank" rel="noopener">🛒 Buy on Rakuten</a>
      </div>
      <p style="font-size:0.75rem; color:#999; margin-top:12px;">※ Prices as of April 2026. Check the retailer for the latest price.</p>
    </div>

    <div class="article-body">

      <div class="info-box">
        📌 This review covers the {pname} — specs, key features, pros & cons, and our expert verdict to help you decide before buying.
      </div>

      <h2>Key Features of the {pname}</h2>
      <p>{en_desc}</p>
      <p>In our testing, the standout feature was <strong>{en_pros[0]}</strong>. On the downside, <strong>{en_cons[0]}</strong> is worth keeping in mind before purchasing.</p>

      <h2>Specs</h2>
      <table class="spec-table">
{specs_html}
      </table>

      <h2>Pros & Cons</h2>
      <div class="pros-cons">
        <div class="pros">
          <h4>Pros</h4>
          <ul>
{pros_html}
          </ul>
        </div>
        <div class="cons">
          <h4>Cons</h4>
          <ul>
{cons_html}
          </ul>
        </div>
      </div>

      <h2>Who Should Buy This?</h2>
      <p><strong>Recommended for:</strong> Those who prioritize {en_pros[0]} and want the best {cat_en} in 2026.</p>
      <p><strong>Not recommended for:</strong> Those who find {en_cons[0]} a dealbreaker.</p>

      <h2>Verdict</h2>
      <p>{en_desc}</p>
      <p><strong>{en_pros[0]}</strong> sets this product apart from the competition and makes it worth serious consideration.</p>

    </div>

    <!-- AdSense in-article -->
    <ins class="adsbygoogle" style="display:block; text-align:center; margin:32px 0;"
         data-ad-layout="in-article" data-ad-format="fluid"
         data-ad-client="ca-pub-2054301472533985" data-ad-slot="AUTO"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>

    <div class="affiliate-box" style="margin-top:40px;">
      <div class="prod-name">{p["emoji"]} {pname}</div>
      <div class="prod-price">From {p["price"]}</div>
      <div class="affiliate-btns">
        <a href="{amazon_url}" class="btn-amazon" target="_blank" rel="noopener">🛒 Buy on Amazon Japan</a>
        <a href="{rakuten_url}" class="btn-rakuten" target="_blank" rel="noopener">🛒 Buy on Rakuten</a>
      </div>
    </div>

    <div class="cta-bottom">
      <h3>Explore More {cat_en}</h3>
      <p>See rankings, comparisons and more reviews for {cat_en}</p>
      <a href="/en/" class="btn-affiliate">Browse All Reviews →</a>
    </div>

    <div class="related-articles">
      <h3>Related Reviews</h3>
      <div class="related-grid">
{related_html}
      </div>
    </div>

  </div>
</div>

<button class="back-to-top" id="backToTop" aria-label="Back to top">↑</button>

{EN_FOOTER}
<script>
  const btn = document.getElementById('backToTop');
  window.addEventListener('scroll', () => {{ btn.classList.toggle('visible', window.scrollY > 400); }});
  btn.addEventListener('click', () => {{ window.scrollTo({{top:0,behavior:'smooth'}}); }});
</script>
</body>
</html>'''

def generate_en_category(cat_name, products):
    from generate import CAT_IMAGES
    cat_en = CAT_EN.get(cat_name, cat_name)
    slug = CAT_SLUGS.get(cat_name, "cat-other")
    cards_html = "\n".join([f'''      <a href="/en/{p['slug']}.html" class="cat-card">
        <div class="cat-card-thumb" style="background:linear-gradient(135deg,{p['bg'].split(',')[0].strip()},{p['bg'].split(',')[1].strip()})">
          <div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:3rem;">{p['emoji']}</div>
        </div>
        <div class="cat-card-body">
          <div class="cat-card-name">{en_name(p['name'])}</div>
          <div class="cat-card-score">★ {p['score']} / 5.0</div>
          <div class="cat-card-price">From {p['price']}</div>
          <div class="cat-card-desc">{t(p['desc'])[:80]}…</div>
        </div>
      </a>''' for p in products])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <title>Best {cat_en} 2026 — Rankings & Reviews | GadgetNavi</title>
  <meta name="description" content="Top {len(products)} {cat_en} ranked by experts in 2026. Compare specs, prices & reviews to find the best {cat_en} for your needs.">
  <link rel="canonical" href="{BASE_URL}en/{slug}.html">
  <link rel="alternate" hreflang="ja" href="{BASE_URL}{slug}.html">
  <link rel="alternate" hreflang="en" href="{BASE_URL}en/{slug}.html">
  <link rel="alternate" hreflang="x-default" href="{BASE_URL}{slug}.html">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-ERDKSGNEWS');</script>
  <style>
    .cat-page {{ max-width: 1100px; margin: 0 auto; padding: 40px 20px 80px; }}
    .cat-hero {{ background: var(--secondary); color: var(--white); border-radius: var(--radius); padding: 40px 32px; margin-bottom: 32px; }}
    .cat-hero h1 {{ font-size: clamp(1.5rem, 3vw, 2.2rem); font-weight: 900; margin-bottom: 8px; }}
    .cat-hero p {{ color: rgba(255,255,255,0.7); font-size: 0.95rem; }}
    .cat-intro {{ background: var(--white); border-radius: var(--radius); padding: 24px 28px; margin-bottom: 32px; border: 1px solid var(--border); line-height: 1.85; font-size: 0.93rem; color: #444; }}
    .cat-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }}
    .cat-card {{ background: var(--white); border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow-sm); transition: transform 0.2s; display: flex; flex-direction: column; text-decoration: none; }}
    .cat-card:hover {{ transform: translateY(-4px); }}
    .cat-card-thumb {{ height: 160px; overflow: hidden; }}
    .cat-card-body {{ padding: 16px; flex: 1; display: flex; flex-direction: column; gap: 6px; }}
    .cat-card-name {{ font-size: 0.95rem; font-weight: 700; color: var(--text); }}
    .cat-card-score {{ font-size: 0.85rem; color: var(--primary); font-weight: 700; }}
    .cat-card-price {{ font-size: 1rem; font-weight: 900; color: var(--primary); }}
    .cat-card-desc {{ font-size: 0.8rem; color: var(--text-muted); line-height: 1.6; }}
    .breadcrumb {{ font-size: 0.8rem; color: var(--text-light); margin-bottom: 20px; display: flex; gap: 8px; flex-wrap: wrap; }}
    .breadcrumb a {{ color: var(--primary); text-decoration: none; }}
  </style>
</head>
<body>
{EN_HEADER}
<div style="background:var(--bg); padding:20px; min-height:80vh;">
  <div class="cat-page">
    <div class="breadcrumb">
      <a href="/en/">Home</a><span>›</span>
      <span>{cat_en}</span>
    </div>
    <div class="cat-hero">
      <h1>Best {cat_en} Rankings [2026]</h1>
      <p>Expert reviews of {len(products)} top {cat_en} — specs, prices & verdicts compared</p>
    </div>
    <div class="cat-intro">
      <p>Looking for the best <strong>{cat_en}</strong> in 2026? We've reviewed {len(products)} models in detail, comparing specs, features, pricing and real-world performance. Click any product to read the full review.</p>
    </div>
    <div class="cat-grid">
{cards_html}
    </div>
  </div>
</div>
{EN_FOOTER}
</body>
</html>'''

# ---- Generate ----
count = 0
for p in PRODUCTS:
    html = generate_en_review(p)
    path = os.path.join(OUTPUT_DIR, f"{p['slug']}.html")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1

print(f"Generated {count} English review pages")

cat_map = defaultdict(list)
for p in PRODUCTS:
    cat_map[p['cat']].append(p)

cat_count = 0
for cat_name, prods in cat_map.items():
    slug = CAT_SLUGS.get(cat_name, "cat-other")
    html = generate_en_category(cat_name, prods)
    path = os.path.join(OUTPUT_DIR, f"{slug}.html")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    cat_count += 1

print(f"Generated {cat_count} English category pages")
print(f"Output: {OUTPUT_DIR}")
