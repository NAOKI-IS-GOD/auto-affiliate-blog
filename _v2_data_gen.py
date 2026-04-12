# -*- coding: utf-8 -*-
import os

# Slugs extracted from the project directory
SLUGS = [
    "compare-applewatchs10-vs-applewatchultra2",
    "compare-applewatchs10-vs-galaxywatch7",
    "compare-applewatchultra2-vs-garminfenix8",
    "compare-asusrogzephyrusg14-vs-razerblade15",
    "compare-boseSoundLinkMax-vs-marshallEmberton3",
    "compare-dellu2723d-vs-benqpd3205u",
    "compare-dreameX40ultra-vs-ecovacsX5pro",
    "compare-fujifilmxt5-vs-sonya7cii",
    "compare-galaxya55-vs-nothingphone3a",
    "compare-galaxybuds3pro-vs-sonywf1000xm5",
    "compare-galaxys25ultra-vs-xiaomi14ultra",
    "compare-garminfenix8-vs-garminvenu3",
    "compare-goprohero12-vs-djiosmoaction4",
    "compare-insta360x4-vs-goprohero12",
    "compare-ipadairm2-vs-ipadprom4",
    "compare-ipadmini7-vs-kindlepaperwhite",
    "compare-ipadprom4-vs-galaxytabs10ultra",
    "compare-iphone16-vs-galaxy-s25",
    "compare-iphone16-vs-pixel9a",
    "compare-iphone16plus-vs-galaxys25plus",
    "compare-iphone16promax-vs-galaxys25ultra",
    "compare-iphone16promax-vs-pixel9pro",
    "compare-iphonese4-vs-nothingphone3a",
    "compare-iroombaj9plus-vs-eufyrobovacx8",
    "compare-jblflip6-vs-boseSoundLinkMax",
    "compare-jbltourpro3-vs-sonywf1000xm5",
    "compare-lg27gp850b-vs-asusrogswiftpg279qm",
    "compare-lg45gr95qeb-vs-samsungodysseyg7",
    "compare-macbookairm3-vs-dellxps15",
    "compare-macbookairm3-vs-macbookprom4pro",
    "compare-macbookairm3-vs-surfacepro11",
    "compare-nintendoswitch2-vs-ps5slim",
    "compare-nintendoswitch2-vs-xboxseriesx",
    "compare-nothingear2-vs-ankerliberty4nc",
    "compare-oneplus13-vs-xiaomi15",
    "compare-oppofindx8pro-vs-xiaomi14ultra",
    "compare-pixel9a-vs-iphonese4",
    "compare-pixelwatch3-vs-galaxywatch7",
    "compare-ps5slim-vs-xboxseriesx",
    "compare-roborocks8maxv-vs-dreameX40ultra",
    "compare-samsungodysseyg7-vs-lg27gp850b",
    "compare-sennheisermomentum4-vs-boseqcearbuds2",
    "compare-sonywf1000xm5-vs-boseqcearbuds2",
    "compare-sonywf1000xm5-vs-technicseahaz80",
    "compare-sonywh1000xm5-vs-boseqc45",
    "compare-sonyzve10ii-vs-canoneosr50",
    "compare-surfacepro11-vs-ipadprom4",
    "compare-technicseahaz80-vs-boseqcearbuds2",
    "compare-thinkpadx1carbon-vs-dellxps15",
    "compare-xperia1vi-vs-galaxy-s25",
]

# Map slug parts to full names and categories
MAPPING = {
    "iphone16promax": ("iPhone 16 Pro Max", "スマートフォン", "Smartphone", "📱"),
    "galaxys25ultra": ("Galaxy S25 Ultra", "スマートフォン", "Smartphone", "📱"),
    "iphone16": ("iPhone 16", "スマートフォン", "Smartphone", "📱"),
    "pixel9a": ("Pixel 9a", "スマートフォン", "Smartphone", "📱"),
    "galaxys25": ("Galaxy S25", "スマートフォン", "Smartphone", "📱"),
    "iphonese4": ("iPhone SE4", "スマートフォン", "Smartphone", "📱"),
    "nothingphone3a": ("Nothing Phone 3a", "スマートフォン", "Smartphone", "📱"),
    "pixel9pro": ("Pixel 9 Pro", "スマートフォン", "Smartphone", "📱"),
    "xiaomi14ultra": ("Xiaomi 14 Ultra", "スマートフォン", "Smartphone", "📱"),
    "xperia1vi": ("Xperia 1 VI", "スマートフォン", "Smartphone", "📱"),
    "oneplus13": ("OnePlus 13", "スマートフォン", "Smartphone", "📱"),
    "xiaomi15": ("Xiaomi 15", "スマートフォン", "Smartphone", "📱"),
    "oppofindx8pro": ("OPPO Find X8 Pro", "スマートフォン", "Smartphone", "📱"),
    "galaxya55": ("Galaxy A55", "スマートフォン", "Smartphone", "📱"),
    "iphone16plus": ("iPhone 16 Plus", "スマートフォン", "Smartphone", "📱"),
    "galaxys25plus": ("Galaxy S25+", "スマートフォン", "Smartphone", "📱"),
    "applewatchs10": ("Apple Watch Series 10", "スマートウォッチ", "Smartwatch", "⌚"),
    "applewatchultra2": ("Apple Watch Ultra 2", "スマートウォッチ", "Smartwatch", "⌚"),
    "galaxywatch7": ("Galaxy Watch 7", "スマートウォッチ", "Smartwatch", "⌚"),
    "pixelwatch3": ("Pixel Watch 3", "スマートウォッチ", "Smartwatch", "⌚"),
    "garminfenix8": ("Garmin Fenix 8", "スマートウォッチ", "Smartwatch", "⌚"),
    "garminvenu3": ("Garmin Venu 3", "スマートウォッチ", "Smartwatch", "⌚"),
    "macbookairm3": ("MacBook Air M3", "ノートPC", "Laptop", "💻"),
    "macbookprom4pro": ("MacBook Pro M4 Pro", "ノートPC", "Laptop", "💻"),
    "dellxps15": ("Dell XPS 15", "ノートPC", "Laptop", "💻"),
    "surfacepro11": ("Surface Pro 11", "ノートPC", "Laptop", "💻"),
    "thinkpadx1carbon": ("ThinkPad X1 Carbon", "ノートPC", "Laptop", "💻"),
    "asusrogzephyrusg14": ("ASUS ROG Zephyrus G14", "ノートPC", "Laptop", "💻"),
    "razerblade15": ("Razer Blade 15", "ノートPC", "Laptop", "💻"),
    "ipadprom4": ("iPad Pro M4", "タブレット", "Tablet", "📟"),
    "ipadairm2": ("iPad Air M2", "タブレット", "Tablet", "📟"),
    "ipadmini7": ("iPad Mini 7", "タブレット", "Tablet", "📟"),
    "galaxytabs10ultra": ("Galaxy Tab S10 Ultra", "タブレット", "Tablet", "📟"),
    "kindlepaperwhite": ("Kindle Paperwhite", "タブレット", "Tablet", "📖"),
    "sonywf1000xm5": ("Sony WF-1000XM5", "イヤホン", "Earphones", "🎧"),
    "boseqcearbuds2": ("Bose QC Earbuds II", "イヤホン", "Earphones", "🎧"),
    "galaxybuds3pro": ("Galaxy Buds 3 Pro", "イヤホン", "Earphones", "🎧"),
    "jbltourpro3": ("JBL Tour Pro 3", "イヤホン", "Earphones", "🎧"),
    "nothingear2": ("Nothing Ear 2", "イヤホン", "Earphones", "🎧"),
    "ankerliberty4nc": ("Anker Liberty 4 NC", "イヤホン", "Earphones", "🎧"),
    "sennheisermomentum4": ("Sennheiser MOMENTUM TW4", "イヤホン", "Earphones", "🎧"),
    "technicseahaz80": ("Technics EAH-AZ80", "イヤホン", "Earphones", "🎧"),
    "sonywh1000xm5": ("Sony WH-1000XM5", "イヤホン", "Earphones", "🎧"),
    "boseqc45": ("Bose QC45", "イヤホン", "Earphones", "🎧"),
    "jblflip6": ("JBL Flip 6", "スピーカー", "Speaker", "🔊"),
    "boseSoundLinkMax": ("Bose SoundLink Max", "スピーカー", "Speaker", "🔊"),
    "marshallEmberton3": ("Marshall Emberton III", "スピーカー", "Speaker", "🔊"),
    "goprohero12": ("GoPro HERO12 Black", "アクションカム", "Action Cam", "📹"),
    "djiosmoaction4": ("DJI Osmo Action 4", "アクションカム", "Action Cam", "📹"),
    "insta360x4": ("Insta360 X4", "アクションカム", "Action Cam", "📹"),
    "sonyzve10ii": ("Sony ZV-E10 II", "カメラ", "Camera", "📷"),
    "canoneosr50": ("Canon EOS R50", "カメラ", "Camera", "📷"),
    "fujifilmxt5": ("Fujifilm X-T5", "カメラ", "Camera", "📷"),
    "sonya7cii": ("Sony α7C II", "カメラ", "Camera", "📷"),
    "lg27gp850b": ("LG 27GP850B", "モニター", "Monitor", "🖥️"),
    "asusrogswiftpg279qm": ("ASUS ROG Swift PG279QM", "モニター", "Monitor", "🖥️"),
    "samsungodysseyg7": ("Samsung Odyssey G7 28\"", "モニター", "Monitor", "🖥️"),
    "lg45gr95qeb": ("LG 45GR95QEB", "モニター", "Monitor", "🖥️"),
    "benqpd3205u": ("BenQ PD3205U", "モニター", "Monitor", "🖥️"),
    "dellu2723d": ("Dell U2723D", "モニター", "Monitor", "🖥️"),
    "iroombaj9plus": ("iRobot Roomba J9+", "ロボット掃除機", "Robot Vacuum", "🤖"),
    "eufyrobovacx8": ("Eufy RoboVac X8", "ロボット掃除機", "Robot Vacuum", "🤖"),
    "roborocks8maxv": ("Roborock S8 MaxV", "ロボット掃除機", "Robot Vacuum", "🤖"),
    "dreameX40ultra": ("Dreame X40 Ultra", "ロボット掃除機", "Robot Vacuum", "🤖"),
    "ecovacsX5pro": ("Ecovacs X5 Pro", "ロボット掃除機", "Robot Vacuum", "🤖"),
    "nintendoswitch2": ("Nintendo Switch 2", "ゲーム機", "Game Console", "🎮"),
    "ps5slim": ("PS5 Slim", "ゲーム機", "Game Console", "🎮"),
    "xboxseriesx": ("Xbox Series X", "ゲーム機", "Game Console", "🎮"),
    "galaxy-s25": ("Galaxy S25", "スマートフォン", "Smartphone", "📱"),
}

def get_mapping(slug_part):
    return MAPPING.get(slug_part, (slug_part, "その他", "Other", "📦"))

COMPARISONS = []

for slug in SLUGS:
    parts = slug.replace("compare-", "").split("-vs-")
    a_part = parts[0]
    b_part = parts[1]
    
    a_name, cat, cat_en, emoji = get_mapping(a_part)
    b_name, _, _, _ = get_mapping(b_part)
    
    # Simple logic for backgrounds
    bg = "#000,#333" if cat == "スマートフォン" else "#222,#555"
    if cat == "ゲーム機": bg = "#555,#888"
    if cat == "カメラ": bg = "#777,#aaa"
    
    entry = {
        "slug": slug,
        "cat": cat, "cat_en": cat_en, "emoji": emoji, "bg": bg,
        "a": {"name": a_name, "score": 4.8, "slug": f"review-{a_part}"},
        "b": {"name": b_name, "score": 4.7, "slug": f"review-{b_part}"},
        "verdict_ja": f"{a_name}と{b_name}の徹底比較。あなたのライフスタイルに合うのはどっち？",
        "verdict_en": f"Comprehensive comparison of {a_name} and {b_name}. Which one fits your lifestyle?",
        "summary_ja": f"2026年最新の{cat}比較。両者のスペック、デザイン、使い勝手の違いを詳細に解説します。",
        "summary_en": f"In-depth {cat_en} comparison. We analyze specs, design, and usability differences between the two.",
        "pa": ["優れたパフォーマンス", "洗練されたデザイン", "高い信頼性"],
        "ca": ["価格がやや高め", "サイズが大きい"],
        "pa_en": ["Excellent performance", "Sleek design", "High reliability"],
        "ca_en": ["Relatively expensive", "Large physical footprint"],
        "pb": ["多機能で使いやすい", "美しいディスプレイ", "充実のサポート"],
        "cb": ["バッテリー持ちが改善の余地あり", "一部の機能が限定的"],
        "pb_en": ["Feature-rich and user-friendly", "Beautiful display", "Excellent support"],
        "cb_en": ["Battery life could be better", "Certain features are limited"],
        "wa": "最高峰の性能とブランド力を求めるユーザー",
        "wa_en": "Users seeking peak performance and brand prestige",
        "wb": "コストパフォーマンスと実用的な機能を重視するユーザー",
        "wb_en": "Users prioritizing value and practical features",
    }
    COMPARISONS.append(entry)

# Write to _v2_data.py
import reprlib
with open('C:/Users/81804/OneDrive/デスクトップ/auto-affiliate-blog-main/_v2_data.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\nCOMPARISONS = [\n")
    for c in COMPARISONS:
        f.write(f"    {repr(c)},\n")
    f.write("]\n")

print(f"Generated {len(COMPARISONS)} entries in _v2_data.py")
