#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_compare.py
比較記事50本を生成するスクリプト
"""

import os
from datetime import date

BASE_URL = "https://auto-affiliate-blog-mauve.vercel.app/"
OUTPUT_DIR = r"C:\Users\81804\OneDrive\デスクトップ\auto-affiliate-blog-main"
TODAY = date.today().isoformat()

# カテゴリごとのグラデーション・絵文字設定
CATEGORY_CONFIG = {
    "スマートフォン": {
        "gradient": "linear-gradient(135deg,#1a1a2e,#16213e)",
        "emoji": "📱",
        "cat_label": "SMARTPHONE",
        "cat_page": "cat-smartphone.html",
    },
    "イヤホン": {
        "gradient": "linear-gradient(135deg,#1a1a2e,#0f3460)",
        "emoji": "🎧",
        "cat_label": "EARPHONE",
        "cat_page": "cat-earphone.html",
    },
    "スマートウォッチ": {
        "gradient": "linear-gradient(135deg,#0d1b2a,#1b4332)",
        "emoji": "⌚",
        "cat_label": "SMARTWATCH",
        "cat_page": "cat-smartwatch.html",
    },
    "タブレット": {
        "gradient": "linear-gradient(135deg,#1a1a2e,#2d3748)",
        "emoji": "📱",
        "cat_label": "TABLET",
        "cat_page": "cat-tablet.html",
    },
    "ノートPC": {
        "gradient": "linear-gradient(135deg,#1a1a2e,#2c3e50)",
        "emoji": "💻",
        "cat_label": "LAPTOP",
        "cat_page": "cat-laptop.html",
    },
    "ゲーム機": {
        "gradient": "linear-gradient(135deg,#0d0d1a,#1a0033)",
        "emoji": "🎮",
        "cat_label": "GAMING",
        "cat_page": "cat-gaming.html",
    },
    "モニター": {
        "gradient": "linear-gradient(135deg,#0d1b2a,#16213e)",
        "emoji": "🖥️",
        "cat_label": "MONITOR",
        "cat_page": "cat-monitor.html",
    },
    "カメラ": {
        "gradient": "linear-gradient(135deg,#1a0a00,#2d1a00)",
        "emoji": "📷",
        "cat_label": "CAMERA",
        "cat_page": "cat-camera.html",
    },
    "ロボット掃除機": {
        "gradient": "linear-gradient(135deg,#0a1628,#1a2744)",
        "emoji": "🤖",
        "cat_label": "ROBOT VACUUM",
        "cat_page": "cat-robotvacuum.html",
    },
    "スピーカー": {
        "gradient": "linear-gradient(135deg,#1a1a2e,#2d2d44)",
        "emoji": "🔊",
        "cat_label": "SPEAKER",
        "cat_page": "cat-speaker.html",
    },
}

# スペック比較データ（カテゴリ別）
SPEC_TEMPLATES = {
    "スマートフォン": [
        ("OS", lambda a, b: ("iOS", "Android")),
        ("画面サイズ", None),
        ("プロセッサ", None),
        ("バッテリー", None),
        ("カメラ", None),
    ],
    "イヤホン": [
        ("ノイキャン", None),
        ("連続再生時間", None),
        ("Bluetooth", None),
        ("防水規格", None),
        ("重量", None),
    ],
    "スマートウォッチ": [
        ("OS", None),
        ("バッテリー", None),
        ("防水", None),
        ("GPS", None),
        ("画面", None),
    ],
    "タブレット": [
        ("OS", None),
        ("プロセッサ", None),
        ("画面", None),
        ("ストレージ", None),
        ("バッテリー", None),
    ],
    "ノートPC": [
        ("OS", None),
        ("プロセッサ", None),
        ("メモリ", None),
        ("ストレージ", None),
        ("バッテリー", None),
    ],
    "ゲーム機": [
        ("プレイスタイル", None),
        ("解像度", None),
        ("ストレージ", None),
        ("対応ソフト", None),
        ("オンライン", None),
    ],
    "モニター": [
        ("サイズ", None),
        ("解像度", None),
        ("リフレッシュレート", None),
        ("パネル", None),
        ("入力端子", None),
    ],
    "カメラ": [
        ("センサー", None),
        ("動画", None),
        ("手ブレ補正", None),
        ("防水", None),
        ("バッテリー", None),
    ],
    "ロボット掃除機": [
        ("吸引力", None),
        ("マッピング", None),
        ("水拭き", None),
        ("自動ゴミ収集", None),
        ("バッテリー", None),
    ],
    "スピーカー": [
        ("防水", None),
        ("連続再生時間", None),
        ("Bluetooth", None),
        ("重量", None),
        ("360°サウンド", None),
    ],
}

# 比較記事50本の定義
ARTICLES = [
    # スマートフォン
    {
        "slug": "compare-iphone16promax-vs-galaxys25ultra",
        "category": "スマートフォン",
        "product_a": {"name": "iPhone 16 Pro Max", "price": "¥194,800", "score": 4.9, "slug": "review-iphone16promax"},
        "product_b": {"name": "Galaxy S25 Ultra", "price": "¥189,800", "score": 4.7, "slug": "review-galaxys25ultra"},
        "verdict": "カメラ最強を求めるならiPhone 16 Pro Max、Androidで最高峰を選ぶならGalaxy S25 Ultra",
        "specs": [
            ("OS", "iOS 18", "Android 15"),
            ("プロセッサ", "A18 Pro", "Snapdragon 8 Elite"),
            ("バッテリー", "4685mAh", "5000mAh"),
            ("メインカメラ", "48MP+48MP+12MP", "200MP+50MP+10MP+12MP"),
            ("画面サイズ", "6.9インチ", "6.9インチ"),
        ],
        "summary_a": "Apple生態系との連携、映画品質の動画撮影、A18 Proの圧倒的パフォーマンスが魅力。長期サポートも安心。",
        "summary_b": "Sペンによる手書き機能、超高倍率ズーム、大型バッテリーでAndroidユーザーに最高のフラグシップ体験を提供。",
    },
    {
        "slug": "compare-iphone16-vs-pixel9a",
        "category": "スマートフォン",
        "product_a": {"name": "iPhone 16", "price": "¥124,800", "score": 4.4, "slug": "review-iphone16"},
        "product_b": {"name": "Pixel 9a", "price": "¥79,800", "score": 4.4, "slug": "review-pixel9a"},
        "verdict": "iPhone生態系に慣れた人にはiPhone 16、コスパ重視でAI機能を使いたい人にはPixel 9a",
        "specs": [
            ("OS", "iOS 18", "Android 15"),
            ("プロセッサ", "A18", "Tensor G4"),
            ("メインカメラ", "48MP", "48MP"),
            ("バッテリー", "3561mAh", "5100mAh"),
            ("価格差", "¥124,800", "¥79,800"),
        ],
        "summary_a": "Apple Intelligenceとシームレスな生態系連携が魅力。写真品質も優秀で長期サポートに安心感。",
        "summary_b": "4万円以上安い価格でGoogleのAI機能が使い放題。Pixel専用カメラ処理で夜景撮影も強い。",
    },
    {
        "slug": "compare-iphone16-vs-galaxy-s25",
        "category": "スマートフォン",
        "product_a": {"name": "iPhone 16", "price": "¥124,800", "score": 4.4, "slug": "review-iphone16"},
        "product_b": {"name": "Galaxy S25", "price": "¥124,800", "score": 4.6, "slug": "review-galaxy-s25"},
        "verdict": "Apple生態系ユーザーにはiPhone 16、Androidでコンパクトなフラグシップを求めるならGalaxy S25",
        "specs": [
            ("OS", "iOS 18", "Android 15"),
            ("プロセッサ", "A18", "Snapdragon 8 Elite"),
            ("メインカメラ", "48MP", "50MP"),
            ("RAM", "8GB", "12GB"),
            ("バッテリー", "3561mAh", "4000mAh"),
        ],
        "summary_a": "完成度の高いiOS体験とApple Intelligenceが強み。カメラ動画品質も業界トップクラス。",
        "summary_b": "同価格帯でSnapdragon 8 Eliteを搭載し、より多くのRAMとバッテリーを提供。Galaxyシリーズの完成度も高い。",
    },
    {
        "slug": "compare-iphonese4-vs-nothingphone3a",
        "category": "スマートフォン",
        "product_a": {"name": "iPhone SE4", "price": "¥74,800", "score": 4.3, "slug": "review-iphonese4"},
        "product_b": {"name": "Nothing Phone 3a", "price": "¥49,800", "score": 4.2, "slug": "review-nothingphone3a"},
        "verdict": "iOSが使いたい低価格帯ならiPhone SE4、個性的なデザインと大画面を求めるならNothing Phone 3a",
        "specs": [
            ("OS", "iOS 18", "Android 15"),
            ("プロセッサ", "A16 Bionic", "Snapdragon 7s Gen 3"),
            ("画面サイズ", "6.1インチ", "6.77インチ"),
            ("バッテリー", "3279mAh", "5000mAh"),
            ("特徴", "Apple Intelligence", "Glyphインターフェース"),
        ],
        "summary_a": "iPhone SE4はA16 Bionicで処理性能が高く、Apple Intelligenceも使用可能。コンパクトで持ちやすい。",
        "summary_b": "Nothing Phone 3aはGlyphデザインが個性的で大画面・大容量バッテリー。価格は2.5万円安い。",
    },
    {
        "slug": "compare-iphone16promax-vs-pixel9pro",
        "category": "スマートフォン",
        "product_a": {"name": "iPhone 16 Pro Max", "price": "¥194,800", "score": 4.9, "slug": "review-iphone16promax"},
        "product_b": {"name": "Pixel 9 Pro", "price": "¥159,800", "score": 4.7, "slug": "review-pixel9pro"},
        "verdict": "最高のiOS体験を求めるならiPhone 16 Pro Max、GoogleのAI機能とコスパを重視するならPixel 9 Pro",
        "specs": [
            ("OS", "iOS 18", "Android 15"),
            ("プロセッサ", "A18 Pro", "Tensor G4"),
            ("カメラ", "48MP+48MP+12MP", "50MP+48MP+48MP"),
            ("バッテリー", "4685mAh", "4700mAh"),
            ("価格差", "¥194,800", "¥159,800"),
        ],
        "summary_a": "映画品質のProRes動画、空間ビデオ撮影など映像クリエイターに最適。Appleシリコンの優位性は揺るぎない。",
        "summary_b": "3.5万円安くてもTensor G4のAI機能は充実。Googleフォトとの連携や純正AIアシスタントが強み。",
    },
    {
        "slug": "compare-galaxys25ultra-vs-xiaomi14ultra",
        "category": "スマートフォン",
        "product_a": {"name": "Galaxy S25 Ultra", "price": "¥189,800", "score": 4.7, "slug": "review-galaxys25ultra"},
        "product_b": {"name": "Xiaomi 14 Ultra", "price": "¥159,800", "score": 4.5, "slug": "review-xiaomi14ultra"},
        "verdict": "Sペンと生産性を重視するならGalaxy S25 Ultra、カメラ性能にこだわるならXiaomi 14 Ultra",
        "specs": [
            ("OS", "Android 15 (One UI 7)", "Android 14 (HyperOS)"),
            ("プロセッサ", "Snapdragon 8 Elite", "Snapdragon 8 Gen 3"),
            ("メインカメラ", "200MP (Samsung)", "50MP (Leica)"),
            ("バッテリー", "5000mAh", "5000mAh"),
            ("Sペン", "付属", "なし"),
        ],
        "summary_a": "Sペン付きで生産性が高い。Samsung生態系との連携も魅力。ビジネスユーザーに最適なフラグシップ。",
        "summary_b": "Leica共同開発カメラで写真品質が突出。3万円安い価格でフラグシップ性能を手に入れられる。",
    },
    {
        "slug": "compare-xperia1vi-vs-galaxy-s25",
        "category": "スマートフォン",
        "product_a": {"name": "Xperia 1 VI", "price": "¥189,700", "score": 4.4, "slug": "review-xperia1vi"},
        "product_b": {"name": "Galaxy S25", "price": "¥124,800", "score": 4.6, "slug": "review-galaxy-s25"},
        "verdict": "高音質・高画質にこだわるなら Xperia 1 VI、バランス重視で6万円節約するならGalaxy S25",
        "specs": [
            ("OS", "Android 14", "Android 15"),
            ("プロセッサ", "Snapdragon 8 Gen 3", "Snapdragon 8 Elite"),
            ("画面", "6.5インチ 4K", "6.2インチ FHD+"),
            ("オーディオ", "3.5mmジャック搭載", "なし"),
            ("カメラ", "52MP Zeiss", "50MP"),
        ],
        "summary_a": "4K有機EL、3.5mmイヤホンジャック、Zeissカメラで音楽・映像体験を重視する人に最適。",
        "summary_b": "最新Snapdragon 8 Eliteで性能は上。65000円安く、One UI 7の使いやすさが人気。",
    },
    {
        "slug": "compare-oneplus13-vs-xiaomi15",
        "category": "スマートフォン",
        "product_a": {"name": "OnePlus 13", "price": "¥109,800", "score": 4.4, "slug": "review-oneplus13"},
        "product_b": {"name": "Xiaomi 15", "price": "¥129,800", "score": 4.7, "slug": "review-xiaomi15"},
        "verdict": "充電速度と価格を重視するならOnePlus 13、総合性能の高さを求めるならXiaomi 15",
        "specs": [
            ("OS", "Android 15 (OxygenOS)", "Android 15 (HyperOS 2)"),
            ("プロセッサ", "Snapdragon 8 Elite", "Snapdragon 8 Elite"),
            ("充電速度", "100W有線+50W無線", "90W有線+50W無線"),
            ("カメラ", "50MP (Hasselblad)", "50MP (Leica)"),
            ("バッテリー", "6000mAh", "5400mAh"),
        ],
        "summary_a": "100W超急速充電と6000mAh大容量バッテリーが強み。Hasselbladカメラも優秀。コスパが非常に高い。",
        "summary_b": "Leica共同開発カメラと最新SoCで総合性能が高い。2万円高いがXiaomiの完成度が光る一台。",
    },
    {
        "slug": "compare-pixel9a-vs-iphonese4",
        "category": "スマートフォン",
        "product_a": {"name": "Pixel 9a", "price": "¥79,800", "score": 4.4, "slug": "review-pixel9a"},
        "product_b": {"name": "iPhone SE4", "price": "¥74,800", "score": 4.3, "slug": "review-iphonese4"},
        "verdict": "GoogleのAIと大画面を求めるならPixel 9a、iOSと小型ボディを好むならiPhone SE4",
        "specs": [
            ("OS", "Android 15", "iOS 18"),
            ("プロセッサ", "Tensor G4", "A16 Bionic"),
            ("画面", "6.34インチ", "6.1インチ"),
            ("バッテリー", "5100mAh", "3279mAh"),
            ("AI機能", "Google AI", "Apple Intelligence"),
        ],
        "summary_a": "5000mAh超のバッテリーとGoogle AIで日常使いに優れる。5,000円高いが価値は十分ある。",
        "summary_b": "5,000円安くてコンパクト。A16 BionicはTensor G4より高性能でApple Intelligenceも使える。",
    },
    {
        "slug": "compare-iphone16plus-vs-galaxys25plus",
        "category": "スマートフォン",
        "product_a": {"name": "iPhone 16 Plus", "price": "¥149,800", "score": 4.5, "slug": "review-iphone16plus"},
        "product_b": {"name": "Galaxy S25+", "price": "¥159,800", "score": 4.6, "slug": "review-galaxys25plus"},
        "verdict": "大画面iPhoneを求めるならiPhone 16 Plus、Androidで大画面フラグシップならGalaxy S25+",
        "specs": [
            ("OS", "iOS 18", "Android 15"),
            ("プロセッサ", "A18", "Snapdragon 8 Elite"),
            ("画面", "6.7インチ Super Retina XDR", "6.7インチ Dynamic AMOLED"),
            ("バッテリー", "4674mAh", "4900mAh"),
            ("RAM", "8GB", "12GB"),
        ],
        "summary_a": "Apple生態系と美しいSuper Retina XDR画面が魅力。A18の処理性能は業界最高水準。",
        "summary_b": "1万円高いがSnapdragon 8 EliteとAIエコシステムが充実。Galaxy AI機能が日常をサポート。",
    },
    {
        "slug": "compare-oppofindx8pro-vs-xiaomi14ultra",
        "category": "スマートフォン",
        "product_a": {"name": "OPPO Find X8 Pro", "price": "¥119,800", "score": 4.3, "slug": "review-oppofindx8pro"},
        "product_b": {"name": "Xiaomi 14 Ultra", "price": "¥159,800", "score": 4.5, "slug": "review-xiaomi14ultra"},
        "verdict": "バランス重視でコスパを求めるならOPPO Find X8 Pro、カメラ性能最重視ならXiaomi 14 Ultra",
        "specs": [
            ("OS", "Android 15 (ColorOS)", "Android 14 (HyperOS)"),
            ("プロセッサ", "Dimensity 9400", "Snapdragon 8 Gen 3"),
            ("メインカメラ", "50MP (Hasselblad)", "50MP (Leica)"),
            ("バッテリー", "5910mAh", "5000mAh"),
            ("価格差", "¥119,800", "¥159,800"),
        ],
        "summary_a": "Dimensity 9400搭載で高性能、Hasselbladカメラ、大容量バッテリー。4万円安くコスパ優秀。",
        "summary_b": "Leicaカメラが圧倒的。写真クオリティに最大限こだわるユーザーへの最適解。",
    },
    {
        "slug": "compare-galaxya55-vs-nothingphone3a",
        "category": "スマートフォン",
        "product_a": {"name": "Galaxy A55", "price": "¥59,800", "score": 4.1, "slug": "review-galaxya55"},
        "product_b": {"name": "Nothing Phone 3a", "price": "¥49,800", "score": 4.2, "slug": "review-nothingphone3a"},
        "verdict": "Samsungブランドの信頼性を求めるならGalaxy A55、個性的デザインとコスパを求めるならNothing Phone 3a",
        "specs": [
            ("OS", "Android 14 (One UI 6)", "Android 15"),
            ("プロセッサ", "Exynos 1480", "Snapdragon 7s Gen 3"),
            ("メインカメラ", "50MP", "50MP"),
            ("バッテリー", "5000mAh", "5000mAh"),
            ("特徴", "Samsung生態系", "Glyphインターフェース"),
        ],
        "summary_a": "Samsungの安心感と長期サポートが強み。防水・防塵もIP67対応で日常使いに安心。",
        "summary_b": "1万円安くGlyphインターフェースで差別化。Snapdragon 7s Gen 3の性能も十分。",
    },
    # イヤホン
    {
        "slug": "compare-sonywf1000xm5-vs-boseqcearbuds2",
        "category": "イヤホン",
        "product_a": {"name": "Sony WF-1000XM5", "price": "¥39,600", "score": 4.7, "slug": "review-sonywf1000xm5"},
        "product_b": {"name": "Bose QC Earbuds II", "price": "¥38,500", "score": 4.6, "slug": "review-boseqcearbuds2"},
        "verdict": "高音質と強力なNCを両立するならSony WF-1000XM5、装着感とNCの快適さを最優先するならBose QC Earbuds II",
        "specs": [
            ("ノイキャン", "業界最高水準", "Bose独自CustomTune"),
            ("連続再生", "8時間(NC ON)", "6時間(NC ON)"),
            ("Bluetooth", "5.3 / LDAC対応", "5.3 / SBC/AAC"),
            ("防水", "IPX4", "IPX4"),
            ("重量", "5.9g/片耳", "6.2g/片耳"),
        ],
        "summary_a": "LDACによる高音質再生と最高水準のANCを両立。Sonyのオーディオ技術の結晶で音楽ファンに強く推薦。",
        "summary_b": "CustomTuneが耳に最適化。装着感と会話モードの自然さはBoseが上。長時間使用でも疲れにくい。",
    },
    {
        "slug": "compare-sonywf1000xm5-vs-technicseahaz80",
        "category": "イヤホン",
        "product_a": {"name": "Sony WF-1000XM5", "price": "¥39,600", "score": 4.7, "slug": "review-sonywf1000xm5"},
        "product_b": {"name": "Technics EAH-AZ80", "price": "¥44,000", "score": 4.6, "slug": "review-technicseahaz80"},
        "verdict": "NC性能を最重視するならSony WF-1000XM5、3台マルチポイントと高音質を求めるならTechnics EAH-AZ80",
        "specs": [
            ("ノイキャン", "業界最高水準", "高性能ANC"),
            ("マルチポイント", "2台", "3台"),
            ("連続再生", "8時間", "7時間"),
            ("コーデック", "LDAC/AAC/SBC", "LDAC/AAC/SBC"),
            ("価格差", "¥39,600", "¥44,000"),
        ],
        "summary_a": "NC性能・音質・バッテリーのバランスが優秀。4400円安くてスペックは互角以上。",
        "summary_b": "3台同時マルチポイントが便利。PC・スマホ・タブレット使い分けする人に最適な一台。",
    },
    {
        "slug": "compare-galaxybuds3pro-vs-sonywf1000xm5",
        "category": "イヤホン",
        "product_a": {"name": "Galaxy Buds 3 Pro", "price": "¥29,800", "score": 4.5, "slug": "review-galaxybuds3pro"},
        "product_b": {"name": "Sony WF-1000XM5", "price": "¥39,600", "score": 4.7, "slug": "review-sonywf1000xm5"},
        "verdict": "Galaxy端末ユーザーなら Galaxy Buds 3 Pro、音質とNCにこだわるならSony WF-1000XM5",
        "specs": [
            ("ノイキャン", "高性能ANC", "業界最高水準"),
            ("連続再生", "6時間", "8時間"),
            ("コーデック", "SSC/AAC", "LDAC/AAC/SBC"),
            ("Galaxy連携", "最高", "標準"),
            ("価格差", "¥29,800", "¥39,600"),
        ],
        "summary_a": "Galaxy端末との連携が最高で1万円安い。Samsung生態系ユーザーには最適の選択肢。",
        "summary_b": "LDACと強力ANCで音楽体験が上回る。Galaxy以外のAndroid/iPhoneユーザーにも対応。",
    },
    {
        "slug": "compare-jbltourpro3-vs-sonywf1000xm5",
        "category": "イヤホン",
        "product_a": {"name": "JBL Tour Pro 3", "price": "¥34,800", "score": 4.4, "slug": "review-jbltourpro3"},
        "product_b": {"name": "Sony WF-1000XM5", "price": "¥39,600", "score": 4.7, "slug": "review-sonywf1000xm5"},
        "verdict": "スマートケースの利便性と価格を重視するならJBL Tour Pro 3、音質とNCの頂点を求めるならSony WF-1000XM5",
        "specs": [
            ("ノイキャン", "高性能ANC", "業界最高水準"),
            ("連続再生", "11時間", "8時間"),
            ("スマートケース", "タッチスクリーン搭載", "通常ケース"),
            ("コーデック", "AAC/SBC", "LDAC/AAC/SBC"),
            ("価格差", "¥34,800", "¥39,600"),
        ],
        "summary_a": "タッチスクリーン付きスマートケースが便利で長時間再生が可能。5,000円安くコスパも良い。",
        "summary_b": "音質はLDACで頭一つ抜けた存在。NC性能も業界トップクラスで音楽没入感が最高。",
    },
    {
        "slug": "compare-nothingear2-vs-ankerliberty4nc",
        "category": "イヤホン",
        "product_a": {"name": "Nothing Ear 2", "price": "¥18,800", "score": 4.3, "slug": "review-nothingear2"},
        "product_b": {"name": "Anker Liberty 4 NC", "price": "¥9,990", "score": 4.3, "slug": "review-ankerliberty4nc"},
        "verdict": "デザインと音質バランスを求めるならNothing Ear 2、コスパ最優先ならAnker Liberty 4 NC",
        "specs": [
            ("ノイキャン", "高性能ANC", "ANC対応"),
            ("連続再生", "6時間", "10時間"),
            ("コーデック", "LDAC/AAC", "LDAC/AAC"),
            ("デザイン", "透明筐体", "標準"),
            ("価格差", "¥18,800", "¥9,990"),
        ],
        "summary_a": "半透明デザインが個性的でLDAC対応の高音質。コスパも良く独自のデザイン哲学が魅力。",
        "summary_b": "約1万円でLDAC対応・ANC搭載は驚異的コスパ。Nothing Ear 2より半額近い価格で同等機能。",
    },
    {
        "slug": "compare-sennheisermomentum4-vs-boseqcearbuds2",
        "category": "イヤホン",
        "product_a": {"name": "Sennheiser MOMENTUM TW4", "price": "¥44,000", "score": 4.5, "slug": "review-sennheisermomentum4"},
        "product_b": {"name": "Bose QC Earbuds II", "price": "¥38,500", "score": 4.6, "slug": "review-boseqcearbuds2"},
        "verdict": "Sennheiserの音質にこだわるならMOMENTUM TW4、装着感とNC快適性を最優先するならBose QC Earbuds II",
        "specs": [
            ("ノイキャン", "高性能ANC", "Bose独自CustomTune"),
            ("連続再生", "7.5時間", "6時間"),
            ("コーデック", "aptX/AAC/SBC", "SBC/AAC"),
            ("装着感", "良好", "最高水準"),
            ("価格差", "¥44,000", "¥38,500"),
        ],
        "summary_a": "Sennheiserらしい自然で音楽的なサウンド。aptX対応でAndroidとの相性が良く音楽鑑賞に最適。",
        "summary_b": "5,500円安くてCustomTuneで耳に最適化。長時間の装着でも疲れにくいBoseの装着設計が優秀。",
    },
    {
        "slug": "compare-sonywh1000xm5-vs-boseqc45",
        "category": "イヤホン",
        "product_a": {"name": "Sony WH-1000XM5", "price": "¥49,500", "score": 4.8, "slug": "review-sonywh1000xm5"},
        "product_b": {"name": "Bose QC45", "price": "¥44,000", "score": 4.6, "slug": "review-boseqc45"},
        "verdict": "最高峰の音質とNCを求めるならSony WH-1000XM5、軽量で快適な長時間リスニングならBose QC45",
        "specs": [
            ("ノイキャン", "業界最高水準(8マイク)", "効果的なANC"),
            ("連続再生", "30時間(NC ON)", "24時間(NC ON)"),
            ("コーデック", "LDAC/DSEE Extreme", "AAC/SBC"),
            ("重量", "250g", "238g"),
            ("価格差", "¥49,500", "¥44,000"),
        ],
        "summary_a": "オーバーイヤー型ヘッドホンの頂点。8マイクANCとLDACで没入感が段違い。長時間快適リスニング。",
        "summary_b": "5,500円安く軽量で長時間でも疲れにくい。ANCも十分強力でBoseの快適性は健在。",
    },
    {
        "slug": "compare-technicseahaz80-vs-boseqcearbuds2",
        "category": "イヤホン",
        "product_a": {"name": "Technics EAH-AZ80", "price": "¥44,000", "score": 4.6, "slug": "review-technicseahaz80"},
        "product_b": {"name": "Bose QC Earbuds II", "price": "¥38,500", "score": 4.6, "slug": "review-boseqcearbuds2"},
        "verdict": "3台マルチポイントと高音質を求めるならTechnics EAH-AZ80、装着感とNCの快適さを優先するならBose QC Earbuds II",
        "specs": [
            ("ノイキャン", "高性能ANC", "Bose CustomTune"),
            ("マルチポイント", "3台", "2台"),
            ("連続再生", "7時間", "6時間"),
            ("コーデック", "LDAC/AAC/SBC", "SBC/AAC"),
            ("価格差", "¥44,000", "¥38,500"),
        ],
        "summary_a": "3台同時接続が便利でLDAC高音質。Panasonicグループの音響技術が光る高品位イヤホン。",
        "summary_b": "5,500円安くて装着感が最高水準。CustomTuneで自分の耳に最適化されるBoseの強みが際立つ。",
    },
    # スマートウォッチ
    {
        "slug": "compare-applewatchs10-vs-galaxywatch7",
        "category": "スマートウォッチ",
        "product_a": {"name": "Apple Watch S10", "price": "¥59,800", "score": 4.8, "slug": "review-applewatchs10"},
        "product_b": {"name": "Galaxy Watch 7", "price": "¥44,800", "score": 4.6, "slug": "review-galaxywatch7"},
        "verdict": "iPhoneユーザーならApple Watch S10一択、Android/Galaxyユーザーにコスパ重視ならGalaxy Watch 7",
        "specs": [
            ("対応OS", "iOS専用", "Android(Galaxy最適化)"),
            ("バッテリー", "最大18時間", "最大40時間"),
            ("健康機能", "血中酸素+心電図", "血中酸素+心電図+体温"),
            ("防水", "50m防水", "5ATM防水"),
            ("価格差", "¥59,800", "¥44,800"),
        ],
        "summary_a": "iPhoneとのシームレス連携が圧倒的。watchOSのアプリ生態系とApple Payの使いやすさが最高。",
        "summary_b": "1.5万円安くバッテリーが倍以上持つ。Androidユーザーに十分すぎるスマートウォッチ機能。",
    },
    {
        "slug": "compare-applewatchultra2-vs-garminfenix8",
        "category": "スマートウォッチ",
        "product_a": {"name": "Apple Watch Ultra 2", "price": "¥139,800", "score": 4.9, "slug": "review-applewatchultra2"},
        "product_b": {"name": "Garmin Fenix 8", "price": "¥139,800", "score": 4.7, "slug": "review-garminfenix8"},
        "verdict": "iPhoneと連携した高機能アウトドアウォッチならApple Watch Ultra 2、本格的スポーツ・長期バッテリーならGarmin Fenix 8",
        "specs": [
            ("バッテリー", "最大60時間(低電力)", "最大16日間(通常)"),
            ("GPS", "L1/L5 デュアルバンド", "マルチバンドGPS"),
            ("防水", "100m防水", "100m防水"),
            ("チタン素材", "グレードTi", "航空宇宙グレードTi"),
            ("対応OS", "iOS専用", "iOS/Android両対応"),
        ],
        "summary_a": "Apple生態系との統合が最高。デザインも洗練されており日常使いからアウトドアまでカバー。",
        "summary_b": "16日間バッテリーと本格的なスポーツ追跡が強み。iOS/Android両対応でランナー・登山家に最適。",
    },
    {
        "slug": "compare-pixelwatch3-vs-galaxywatch7",
        "category": "スマートウォッチ",
        "product_a": {"name": "Pixel Watch 3", "price": "¥59,800", "score": 4.5, "slug": "review-pixelwatch3"},
        "product_b": {"name": "Galaxy Watch 7", "price": "¥44,800", "score": 4.6, "slug": "review-galaxywatch7"},
        "verdict": "PixelスマホユーザーならPixel Watch 3、Galaxyユーザーやコスパ重視ならGalaxy Watch 7",
        "specs": [
            ("対応OS", "Android(Pixel最適化)", "Android(Galaxy最適化)"),
            ("バッテリー", "最大24時間", "最大40時間"),
            ("健康機能", "心電図+血中酸素", "心電図+血中酸素+体温"),
            ("Wear OS", "Wear OS 4", "Wear OS 4"),
            ("価格差", "¥59,800", "¥44,800"),
        ],
        "summary_a": "GoogleのAIと深く統合。Pixel端末との組み合わせでGoogleアシスタントが最大限活躍。",
        "summary_b": "1.5万円安くバッテリーが長持ち。Galaxy端末との組み合わせでSamsung Health機能が充実。",
    },
    {
        "slug": "compare-garminfenix8-vs-garminvenu3",
        "category": "スマートウォッチ",
        "product_a": {"name": "Garmin Fenix 8", "price": "¥139,800", "score": 4.7, "slug": "review-garminfenix8"},
        "product_b": {"name": "Garmin Venu 3", "price": "¥69,800", "score": 4.5, "slug": "review-garminvenu3"},
        "verdict": "本格アウトドア・スポーツ派にはGarmin Fenix 8、日常使い重視でスタイリッシュさを求めるならGarmin Venu 3",
        "specs": [
            ("バッテリー", "最大16日間", "最大14日間"),
            ("素材", "チタン/サファイアガラス", "アルミ/強化ガラス"),
            ("GPS", "マルチバンドGPS", "GPS"),
            ("スピーカー", "搭載", "搭載"),
            ("価格差", "¥139,800", "¥69,800"),
        ],
        "summary_a": "チタンボディとマルチバンドGPSで過酷な環境にも対応。登山・トレランの本格ユーザーに最適。",
        "summary_b": "7万円安くスタイリッシュ。日常のフィットネストラッキングとスマートウォッチ機能のバランスが優秀。",
    },
    {
        "slug": "compare-applewatchs10-vs-applewatchultra2",
        "category": "スマートウォッチ",
        "product_a": {"name": "Apple Watch S10", "price": "¥59,800", "score": 4.8, "slug": "review-applewatchs10"},
        "product_b": {"name": "Apple Watch Ultra 2", "price": "¥139,800", "score": 4.9, "slug": "review-applewatchultra2"},
        "verdict": "日常使いにはApple Watch S10で十分、アウトドア・プロスポーツ用途にはApple Watch Ultra 2",
        "specs": [
            ("バッテリー", "最大18時間", "最大60時間(低電力)"),
            ("防水", "50m防水", "100m防水"),
            ("素材", "アルミ/チタン", "グレードTiチタン"),
            ("GPS", "L1/L5 デュアル", "L1/L5 デュアル"),
            ("価格差", "¥59,800", "¥139,800"),
        ],
        "summary_a": "日常使いに十分な機能で8万円安い。薄型軽量設計で普段使いの快適さが向上。",
        "summary_b": "バッテリーが3倍以上、防水も2倍強化。8万円の追加投資に見合うアウトドア性能を持つ。",
    },
    # タブレット
    {
        "slug": "compare-ipadprom4-vs-galaxytabs10ultra",
        "category": "タブレット",
        "product_a": {"name": "iPad Pro M4", "price": "¥218,800", "score": 4.9, "slug": "review-ipadprom4"},
        "product_b": {"name": "Galaxy Tab S10 Ultra", "price": "¥189,800", "score": 4.6, "slug": "review-galaxytabs10ultra"},
        "verdict": "Apple生態系でクリエイティブ作業を行うならiPad Pro M4、Android大画面体験を求めるならGalaxy Tab S10 Ultra",
        "specs": [
            ("OS", "iPadOS 17", "Android 14 (One UI 6)"),
            ("プロセッサ", "M4チップ", "Snapdragon 8 Gen 3"),
            ("画面", "11/13インチ Ultra Retina XDR", "14.6インチ Dynamic AMOLED"),
            ("Sペン", "Apple Pencil Pro対応", "Sペン付属"),
            ("価格差", "¥218,800", "¥189,800"),
        ],
        "summary_a": "M4チップとUltra Retina XDRディスプレイが業界最高峰。Pro App対応でプロクリエイターの必需品。",
        "summary_b": "3万円安くSペン付属で即使える。14.6インチの大画面とDeX機能でPC代替にも対応可能。",
    },
    {
        "slug": "compare-ipadairm2-vs-ipadprom4",
        "category": "タブレット",
        "product_a": {"name": "iPad Air M2", "price": "¥98,800", "score": 4.5, "slug": "review-ipadairm2"},
        "product_b": {"name": "iPad Pro M4", "price": "¥218,800", "score": 4.9, "slug": "review-ipadprom4"},
        "verdict": "コスパ重視の普段使いにはiPad Air M2、プロレベルの創作・業務用途にはiPad Pro M4",
        "specs": [
            ("プロセッサ", "M2チップ", "M4チップ"),
            ("画面", "11/13インチ Liquid Retina", "11/13インチ Ultra Retina XDR"),
            ("ProMotion", "なし(60Hz)", "あり(最大120Hz)"),
            ("Apple Pencil", "第2世代対応", "Apple Pencil Pro対応"),
            ("価格差", "¥98,800", "¥218,800"),
        ],
        "summary_a": "M2でも十分高性能。12万円安くほとんどの用途で不満なし。コスパ最強のiPad。",
        "summary_b": "ProMotionとUltra Retina XDRでプロ用途に最適。M4の性能差はヘビーユーザーには明確。",
    },
    {
        "slug": "compare-ipadmini7-vs-kindlepaperwhite",
        "category": "タブレット",
        "product_a": {"name": "iPad mini 7", "price": "¥78,800", "score": 4.4, "slug": "review-ipadmini7"},
        "product_b": {"name": "Kindle Paperwhite", "price": "¥21,980", "score": 4.6, "slug": "review-kindlepaperwhite"},
        "verdict": "電子書籍以外も使いたい多目的利用にはiPad mini 7、読書専用で目に優しさを求めるならKindle Paperwhite",
        "specs": [
            ("OS", "iPadOS 17", "専用OS(Kindle)"),
            ("画面", "8.3インチ Liquid Retina", "6.8インチ E-ink"),
            ("バッテリー", "最大10時間", "最大12週間"),
            ("用途", "多目的", "電子書籍専用"),
            ("価格差", "¥78,800", "¥21,980"),
        ],
        "summary_a": "A15 Bionicで高性能。ゲーム・動画・読書・仕事と何でもこなせる万能コンパクトタブレット。",
        "summary_b": "57,000円安く目に優しいE-inkで長時間読書が快適。防水・軽量でベッドやお風呂でも安心。",
    },
    {
        "slug": "compare-surfacepro11-vs-ipadprom4",
        "category": "タブレット",
        "product_a": {"name": "Surface Pro 11", "price": "¥228,800", "score": 4.5, "slug": "review-surfacepro11"},
        "product_b": {"name": "iPad Pro M4", "price": "¥218,800", "score": 4.9, "slug": "review-ipadprom4"},
        "verdict": "Windows環境が必要なビジネスユーザーにはSurface Pro 11、創作・iPadOS生態系ならiPad Pro M4",
        "specs": [
            ("OS", "Windows 11", "iPadOS 17"),
            ("プロセッサ", "Snapdragon X Elite", "M4チップ"),
            ("Office対応", "ネイティブ Windows", "iPad版"),
            ("外部接続", "USB-A/USB-C/Surface", "Thunderbolt/USB-C"),
            ("価格差", "¥228,800", "¥218,800"),
        ],
        "summary_a": "フル Windows 11でデスクトップアプリが全て動く。ビジネスシーンでの互換性が最高。",
        "summary_b": "M4の処理性能とUltra Retina XDRが光る。クリエイティブ用途ではiPad Pro M4が上回る。",
    },
    # ノートPC
    {
        "slug": "compare-macbookairm3-vs-macbookprom4pro",
        "category": "ノートPC",
        "product_a": {"name": "MacBook Air M3", "price": "¥198,800", "score": 4.8, "slug": "review-macbookairm3"},
        "product_b": {"name": "MacBook Pro M4 Pro", "price": "¥298,800", "score": 4.9, "slug": "review-macbookprom4pro"},
        "verdict": "普段使いや軽作業にはMacBook Air M3、本格的なプロ向け高負荷作業にはMacBook Pro M4 Pro",
        "specs": [
            ("プロセッサ", "M3(8コアCPU)", "M4 Pro(12コアCPU)"),
            ("冷却", "ファンレス", "アクティブ冷却"),
            ("バッテリー", "最大18時間", "最大24時間"),
            ("画面", "13/15インチ Liquid Retina", "14/16インチ Liquid Retina XDR"),
            ("価格差", "¥198,800", "¥298,800"),
        ],
        "summary_a": "ファンレスで静音。10万円安く一般的な作業なら十分すぎる性能。軽くて薄くて持ち運びやすい。",
        "summary_b": "M4 Proで重い動画編集・3D作業も快適。長時間バッテリーとMiniLEDの高品質ディスプレイが魅力。",
    },
    {
        "slug": "compare-macbookairm3-vs-dellxps15",
        "category": "ノートPC",
        "product_a": {"name": "MacBook Air M3", "price": "¥198,800", "score": 4.8, "slug": "review-macbookairm3"},
        "product_b": {"name": "Dell XPS 15", "price": "¥289,800", "score": 4.6, "slug": "review-dellxps15"},
        "verdict": "macOSと長時間バッテリーを重視するならMacBook Air M3、Windows環境と大画面を求めるならDell XPS 15",
        "specs": [
            ("OS", "macOS", "Windows 11"),
            ("プロセッサ", "M3チップ", "Intel Core Ultra 9"),
            ("バッテリー", "最大18時間", "最大13時間"),
            ("画面", "13/15インチ", "15.6インチ 有機EL"),
            ("価格差", "¥198,800", "¥289,800"),
        ],
        "summary_a": "9万円安くバッテリーが5時間以上長い。M3の効率性でファンレス静音動作。macOS生産性も高い。",
        "summary_b": "Windowsで有機EL大画面が美しい。Intel Core Ultra 9でx86アプリが全て動く互換性の高さが魅力。",
    },
    {
        "slug": "compare-macbookairm3-vs-surfacepro11",
        "category": "ノートPC",
        "product_a": {"name": "MacBook Air M3", "price": "¥198,800", "score": 4.8, "slug": "review-macbookairm3"},
        "product_b": {"name": "Surface Pro 11", "price": "¥228,800", "score": 4.5, "slug": "review-surfacepro11"},
        "verdict": "薄型軽量ノートPCを求めるならMacBook Air M3、タブレット兼用の2-in-1ならSurface Pro 11",
        "specs": [
            ("OS", "macOS", "Windows 11"),
            ("プロセッサ", "M3チップ", "Snapdragon X Elite"),
            ("形状", "クラムシェル", "2-in-1タブレット"),
            ("バッテリー", "最大18時間", "最大14時間"),
            ("価格差", "¥198,800", "¥228,800"),
        ],
        "summary_a": "3万円安くバッテリーが長い。macOSとM3チップの組み合わせはクリエイティブ作業の定番。",
        "summary_b": "タブレット・ノートPCの2役をこなす。Surfaceペンで手書き入力ができる独自の利便性が高い。",
    },
    {
        "slug": "compare-asusrogzephyrusg14-vs-razerblade15",
        "category": "ノートPC",
        "product_a": {"name": "ROG Zephyrus G14", "price": "¥249,800", "score": 4.5, "slug": "review-asusrogzephyrusg14"},
        "product_b": {"name": "Razer Blade 15", "price": "¥339,800", "score": 4.5, "slug": "review-razerblade15"},
        "verdict": "コスパ重視のゲーミングノートにはROG Zephyrus G14、プレミアムな薄型ゲーミングにはRazer Blade 15",
        "specs": [
            ("プロセッサ", "AMD Ryzen 9 8945HS", "Intel Core i9-14900HK"),
            ("GPU", "RX 7900S / RTX 4070", "RTX 4080"),
            ("画面", "14インチ 165Hz OLED", "15.6インチ 240Hz QHD"),
            ("重量", "1.65kg", "2.01kg"),
            ("価格差", "¥249,800", "¥339,800"),
        ],
        "summary_a": "9万円安くて軽量。AMDのコスパが高くOLED画面も美しい。持ち運びゲーミングの最適解。",
        "summary_b": "RTX 4080の処理性能と金属ユニボディの高品質感。予算があるプレミアムゲーマーに最適。",
    },
    {
        "slug": "compare-thinkpadx1carbon-vs-dellxps15",
        "category": "ノートPC",
        "product_a": {"name": "ThinkPad X1 Carbon", "price": "¥289,800", "score": 4.7, "slug": "review-thinkpadx1carbon"},
        "product_b": {"name": "Dell XPS 15", "price": "¥289,800", "score": 4.6, "slug": "review-dellxps15"},
        "verdict": "ビジネス用途・軽量性を重視するならThinkPad X1 Carbon、大画面有機ELでクリエイティブ作業ならDell XPS 15",
        "specs": [
            ("OS", "Windows 11 Pro", "Windows 11"),
            ("重量", "約1.12kg〜", "約1.86kg"),
            ("画面", "14インチ IPS", "15.6インチ 有機EL"),
            ("バッテリー", "最大15時間", "最大13時間"),
            ("セキュリティ", "TPM/指紋/顔認証", "指紋認証"),
        ],
        "summary_a": "業界最軽量クラスで長時間バッテリー。ThinkPadの打鍵感とセキュリティ機能がビジネスに最適。",
        "summary_b": "有機EL大画面で映像・写真編集に優秀。デザイナー・クリエイターに向いたスタイリッシュさが魅力。",
    },
    # ゲーム機
    {
        "slug": "compare-nintendoswitch2-vs-ps5slim",
        "category": "ゲーム機",
        "product_a": {"name": "Nintendo Switch 2", "price": "¥49,980", "score": 4.8, "slug": "review-nintendoswitch2"},
        "product_b": {"name": "PS5 Slim", "price": "¥74,980", "score": 4.7, "slug": "review-ps5slim"},
        "verdict": "携帯・据置両用でNintendoタイトルを楽しむならSwitch 2、4K高画質ゲームを楽しむならPS5 Slim",
        "specs": [
            ("プレイスタイル", "携帯・据置両対応", "据置専用"),
            ("解像度", "1080p (TV時)", "4K"),
            ("マリオ/ゼルダ", "対応", "非対応"),
            ("価格差", "¥49,980", "¥74,980"),
            ("オンライン", "Nintendo Switch Online", "PlayStation Plus"),
        ],
        "summary_a": "2.5万円安くて持ち運び可能。任天堂タイトルの独占性と携帯ゲームの自由さが最大の強み。",
        "summary_b": "4K・60fps以上のグラフィックで没入感が圧倒的。PS独占タイトルのクオリティが一線を画す。",
    },
    {
        "slug": "compare-ps5slim-vs-xboxseriesx",
        "category": "ゲーム機",
        "product_a": {"name": "PS5 Slim", "price": "¥74,980", "score": 4.7, "slug": "review-ps5slim"},
        "product_b": {"name": "Xbox Series X", "price": "¥69,978", "score": 4.6, "slug": "review-xboxseriesx"},
        "verdict": "PS独占タイトルと没入感のDualSenseを求めるならPS5 Slim、Game Pass価値とMicrosoft生態系ならXbox Series X",
        "specs": [
            ("解像度", "4K / 8K対応", "4K / 8K対応"),
            ("ストレージ", "1TB SSD", "1TB SSD"),
            ("サブスク", "PlayStation Plus", "Game Pass Ultimate"),
            ("独占タイトル", "Spider-Man/Horizon等", "Halo/Forza等"),
            ("価格差", "¥74,980", "¥69,978"),
        ],
        "summary_a": "DualSenseの触覚フィードバックとアダプティブトリガーが革新的。PS独占タイトルの完成度が高い。",
        "summary_b": "5,000円安くGame Pass月額でゲームが遊び放題。Xbox Game Studioの多くのタイトルが含まれる。",
    },
    {
        "slug": "compare-nintendoswitch2-vs-xboxseriesx",
        "category": "ゲーム機",
        "product_a": {"name": "Nintendo Switch 2", "price": "¥49,980", "score": 4.8, "slug": "review-nintendoswitch2"},
        "product_b": {"name": "Xbox Series X", "price": "¥69,978", "score": 4.6, "slug": "review-xboxseriesx"},
        "verdict": "携帯ゲームと任天堂タイトルを楽しむならSwitch 2、4K高品質グラフィックとGame PassならXbox Series X",
        "specs": [
            ("プレイスタイル", "携帯・据置両対応", "据置専用"),
            ("解像度", "1080p (TV時)", "4K"),
            ("ストレージ", "256GB", "1TB SSD"),
            ("Nintendo IP", "対応", "非対応"),
            ("価格差", "¥49,980", "¥69,978"),
        ],
        "summary_a": "2万円安くて携帯モードで旅行・通勤でもゲームできる。マリオ・ゼルダ・ポケモンのIPが強み。",
        "summary_b": "2万円高いが1TB SSDと4K解像度、Game Passで100本以上のゲームが遊び放題。",
    },
    # モニター
    {
        "slug": "compare-lg27gp850b-vs-asusrogswiftpg279qm",
        "category": "モニター",
        "product_a": {"name": "LG 27GP850B", "price": "¥44,800", "score": 4.6, "slug": "review-lg27gp850b"},
        "product_b": {"name": "ASUS ROG Swift PG279QM", "price": "¥89,800", "score": 4.7, "slug": "review-asusrogswiftpg279qm"},
        "verdict": "コスパ重視のゲーミングモニターにはLG 27GP850B、最高のゲーミング体験を求めるASUS ROG Swift PG279QM",
        "specs": [
            ("サイズ", "27インチ", "27インチ"),
            ("解像度", "2560x1440 (QHD)", "2560x1440 (QHD)"),
            ("リフレッシュレート", "180Hz", "240Hz"),
            ("パネル", "Nano IPS", "IPS"),
            ("価格差", "¥44,800", "¥89,800"),
        ],
        "summary_a": "4.5万円でNano IPS・180Hz・1msを実現。コスパ最高でFPSゲーマーに人気の定番モニター。",
        "summary_b": "4.5万円高いが240Hz対応で動きが滑らか。ROGブランドの信頼性と高リフレッシュレートが光る。",
    },
    {
        "slug": "compare-dellu2723d-vs-benqpd3205u",
        "category": "モニター",
        "product_a": {"name": "Dell U2723D", "price": "¥89,800", "score": 4.7, "slug": "review-dellu2723d"},
        "product_b": {"name": "BenQ PD3205U", "price": "¥79,800", "score": 4.6, "slug": "review-benqpd3205u"},
        "verdict": "USB-Cハブ機能と色精度を重視するならDell U2723D、大画面4Kでクリエイティブ作業ならBenQ PD3205U",
        "specs": [
            ("サイズ", "27インチ", "32インチ"),
            ("解像度", "2560x1440 (QHD)", "3840x2160 (4K UHD)"),
            ("パネル", "IPS Black", "IPS"),
            ("USB-Cハブ", "90W PD対応", "65W PD対応"),
            ("色域", "99% sRGB", "95% DCI-P3"),
        ],
        "summary_a": "IPS Blackパネルで黒の再現性が高い。USB-Cで90W給電できるオフィス・在宅に最適なモニター。",
        "summary_b": "1万円安くて32インチ4Kの大画面。DCI-P3対応でクリエイターに必要な色域をカバー。",
    },
    {
        "slug": "compare-samsungodysseyg7-vs-lg27gp850b",
        "category": "モニター",
        "product_a": {"name": "Samsung Odyssey G7", "price": "¥59,800", "score": 4.6, "slug": "review-samsungodysseyg7"},
        "product_b": {"name": "LG 27GP850B", "price": "¥44,800", "score": 4.6, "slug": "review-lg27gp850b"},
        "verdict": "曲面モニターとVA高コントラストを求めるならSamsung Odyssey G7、フラットNano IPSのコスパならLG 27GP850B",
        "specs": [
            ("サイズ", "27/32インチ 曲面", "27インチ フラット"),
            ("解像度", "2560x1440 (QHD)", "2560x1440 (QHD)"),
            ("パネル", "VA (曲率1000R)", "Nano IPS"),
            ("リフレッシュレート", "240Hz", "180Hz"),
            ("価格差", "¥59,800", "¥44,800"),
        ],
        "summary_a": "曲面1000Rで没入感が高い。VAパネルの高コントラストで暗い場面の映像が鮮明に見える。",
        "summary_b": "1.5万円安くてNano IPSの色再現性が優秀。フラット画面でマルチモニターにも向いている。",
    },
    {
        "slug": "compare-lg45gr95qeb-vs-samsungodysseyg7",
        "category": "モニター",
        "product_a": {"name": "LG 45GR95QEB", "price": "¥149,800", "score": 4.5, "slug": "review-lg45gr95qeb"},
        "product_b": {"name": "Samsung Odyssey G7", "price": "¥59,800", "score": 4.6, "slug": "review-samsungodysseyg7"},
        "verdict": "ウルトラワイドの没入ゲーミングを求めるならLG 45GR95QEB、コスパと実用性を重視するならSamsung Odyssey G7",
        "specs": [
            ("サイズ", "45インチ 800R曲面", "27/32インチ 1000R曲面"),
            ("解像度", "3440x1440 (UWQHD)", "2560x1440 (QHD)"),
            ("パネル", "OLED", "VA"),
            ("リフレッシュレート", "240Hz", "240Hz"),
            ("価格差", "¥149,800", "¥59,800"),
        ],
        "summary_a": "45インチOLEDウルトラワイドで究極の没入感。黒の締まりと反応速度がゲーミングに最高。",
        "summary_b": "9万円安く実用的なサイズ感。VA曲面でコンパクトながら没入感ある体験が可能。",
    },
    # カメラ
    {
        "slug": "compare-goprohero12-vs-djiosmoaction4",
        "category": "カメラ",
        "product_a": {"name": "GoPro HERO12", "price": "¥54,800", "score": 4.5, "slug": "review-goprohero12"},
        "product_b": {"name": "DJI Osmo Action 4", "price": "¥49,800", "score": 4.6, "slug": "review-djiosmoaction4"},
        "verdict": "アクセサリー豊富なGoProエコシステムを求めるならHERO12、低照度性能と長時間録画ならDJI Osmo Action 4",
        "specs": [
            ("動画解像度", "5.3K/60fps", "4K/120fps"),
            ("手ブレ補正", "HyperSmooth 6.0", "RockSteady 3.0"),
            ("低照度", "標準", "優秀"),
            ("バッテリー", "1720mAh (約70min)", "1770mAh (約160min)"),
            ("防水", "10m(ケースなし)", "18m(ケースなし)"),
        ],
        "summary_a": "5.3K対応と豊富なアクセサリーエコシステムが強み。GoProの品質と信頼性は業界標準。",
        "summary_b": "5,000円安くバッテリーが2倍長持ち。低照度性能と防水18mでアウトドアアクションに最適。",
    },
    {
        "slug": "compare-sonyzve10ii-vs-canoneosr50",
        "category": "カメラ",
        "product_a": {"name": "Sony ZV-E10 II", "price": "¥79,800", "score": 4.8, "slug": "review-sonyzve10ii"},
        "product_b": {"name": "Canon EOS R50", "price": "¥89,800", "score": 4.6, "slug": "review-canoneosr50"},
        "verdict": "動画制作・Vlog中心の用途にはSony ZV-E10 II、写真と動画のバランスを求めるならCanon EOS R50",
        "specs": [
            ("センサー", "26MP APS-C", "24MP APS-C"),
            ("動画", "4K/60fps", "4K/30fps"),
            ("手ブレ補正", "電子補正", "電子補正"),
            ("AF", "リアルタイムトラッキング", "デュアルPixel CMOS AF II"),
            ("価格差", "¥79,800", "¥89,800"),
        ],
        "summary_a": "1万円安くて4K/60fps対応。Vlog特化設計で製品レビュー・料理動画などに最適。被写体追尾AFが優秀。",
        "summary_b": "デュアルPixel CMOS AFの精度が高くCanonの色再現性が美しい。写真・動画バランスが取れた一台。",
    },
    {
        "slug": "compare-fujifilmxt5-vs-sonya7cii",
        "category": "カメラ",
        "product_a": {"name": "Fujifilm X-T5", "price": "¥299,800", "score": 4.7, "slug": "review-fujifilmxt5"},
        "product_b": {"name": "Sony α7C II", "price": "¥389,800", "score": 4.8, "slug": "review-sonya7cii"},
        "verdict": "フィルムシミュレーションと高解像APS-Cを求めるならFujifilm X-T5、フルサイズ高性能を求めるならSony α7C II",
        "specs": [
            ("センサー", "40MP APS-C", "33MP フルサイズ"),
            ("手ブレ補正", "7段IBIS", "7段IBIS"),
            ("AF", "リアルタイム追尾AF", "AI AF(被写体認識)"),
            ("動画", "6.2K/30fps", "4K/60fps"),
            ("価格差", "¥299,800", "¥389,800"),
        ],
        "summary_a": "9万円安くて40MPの超高解像度。フジのフィルムシミュレーションは他に代えられない写真表現。",
        "summary_b": "フルサイズセンサーの高感度性能と優秀なAIオートフォーカスが強み。動体撮影に特に強い。",
    },
    {
        "slug": "compare-insta360x4-vs-goprohero12",
        "category": "カメラ",
        "product_a": {"name": "Insta360 X4", "price": "¥69,800", "score": 4.5, "slug": "review-insta360x4"},
        "product_b": {"name": "GoPro HERO12", "price": "¥54,800", "score": 4.5, "slug": "review-goprohero12"},
        "verdict": "360度映像を活用したクリエイティブ表現にはInsta360 X4、従来型アクションカメラの信頼性ならGoPro HERO12",
        "specs": [
            ("映像", "360度 8K30fps", "5.3K通常映像"),
            ("手ブレ補正", "FlowState 360度", "HyperSmooth 6.0"),
            ("防水", "10m(ケースなし)", "10m(ケースなし)"),
            ("バッテリー", "2290mAh", "1720mAh"),
            ("価格差", "¥69,800", "¥54,800"),
        ],
        "summary_a": "360度映像で後から構図を決められるユニークな表現力。1.5万円高いが新しい映像体験が得られる。",
        "summary_b": "1.5万円安くて5.3K高画質。GoProの定番アクセサリーと豊富なマウント類が使えるエコシステム。",
    },
    # ロボット掃除機
    {
        "slug": "compare-roborocks8maxv-vs-dreameX40ultra",
        "category": "ロボット掃除機",
        "product_a": {"name": "Roborock S8 MaxV Ultra", "price": "¥159,800", "score": 4.9, "slug": "review-roborocks8maxv"},
        "product_b": {"name": "Dreame X40 Ultra", "price": "¥149,800", "score": 4.7, "slug": "review-dreameX40ultra"},
        "verdict": "障害物回避と全自動メンテナンスを求めるならRoborock S8 MaxV Ultra、コスパと水拭き性能を重視するならDreame X40 Ultra",
        "specs": [
            ("吸引力", "10000Pa", "12000Pa"),
            ("障害物回避", "ReactiveAI 3.0", "標準"),
            ("水拭き", "ビブロニック 3D", "MopExtend"),
            ("自動ゴミ収集", "対応", "対応"),
            ("価格差", "¥159,800", "¥149,800"),
        ],
        "summary_a": "ReactiveAI 3.0で障害物を精密回避。全自動洗浄・乾燥・ゴミ収集でほぼノーメンテナンス。",
        "summary_b": "1万円安くて吸引力が上。MopExtendで家具下に潜り込んで水拭きする独自機能が便利。",
    },
    {
        "slug": "compare-dreameX40ultra-vs-ecovacsX5pro",
        "category": "ロボット掃除機",
        "product_a": {"name": "Dreame X40 Ultra", "price": "¥149,800", "score": 4.7, "slug": "review-dreameX40ultra"},
        "product_b": {"name": "Ecovacs X5 Pro", "price": "¥139,800", "score": 4.6, "slug": "review-ecovacsX5pro"},
        "verdict": "吸引力と水拭き拡張機能を重視するならDreame X40 Ultra、AIカメラとコスパを求めるならEcovacs X5 Pro",
        "specs": [
            ("吸引力", "12000Pa", "10000Pa"),
            ("水拭き拡張", "MopExtend対応", "なし"),
            ("カメラ", "障害物回避", "AIカメラ(見守り)"),
            ("自動ゴミ収集", "対応", "対応"),
            ("価格差", "¥149,800", "¥139,800"),
        ],
        "summary_a": "吸引力が高くMopExtendで家具下も水拭きできる。1万円高いが水拭き性能の差は明確。",
        "summary_b": "1万円安くてAIカメラ搭載。留守中の見守りカメラとして兼用できる独自の価値がある。",
    },
    {
        "slug": "compare-iroombaj9plus-vs-eufyrobovacx8",
        "category": "ロボット掃除機",
        "product_a": {"name": "iRobot Roomba j9+", "price": "¥129,800", "score": 4.7, "slug": "review-iroombaj9plus"},
        "product_b": {"name": "Eufy RoboVac X8", "price": "¥79,800", "score": 4.4, "slug": "review-eufyrobovacx8"},
        "verdict": "自動ゴミ収集と使いやすさを重視するならRoomba j9+、5万円節約したいコスパ派ならEufy RoboVac X8",
        "specs": [
            ("吸引力", "高性能", "2000Pa×2 デュアル"),
            ("自動ゴミ収集", "対応(CleanBase)", "非対応"),
            ("AI障害物回避", "PrecisionVision", "なし"),
            ("マッピング", "Imprint Smart Mapping", "標準マッピング"),
            ("価格差", "¥129,800", "¥79,800"),
        ],
        "summary_a": "CleanBase自動ゴミ収集で60日間ゴミ捨て不要。PrecisionVisionで靴下・コードを回避する賢さが光る。",
        "summary_b": "5万円安くてデュアルターボで吸引力が高い。価格を抑えて自動掃除の便利さを体験したい人向け。",
    },
    # スピーカー
    {
        "slug": "compare-boseSoundLinkMax-vs-marshallEmberton3",
        "category": "スピーカー",
        "product_a": {"name": "Bose SoundLink Max", "price": "¥29,700", "score": 4.7, "slug": "review-boseSoundLinkMax"},
        "product_b": {"name": "Marshall Emberton III", "price": "¥18,700", "score": 4.5, "slug": "review-marshallEmberton3"},
        "verdict": "音質とBose独自の低音を求めるならBose SoundLink Max、クラシックなデザインとコスパならMarshall Emberton III",
        "specs": [
            ("防水", "IP67", "IP67"),
            ("連続再生", "20時間", "30時間"),
            ("Bluetooth", "5.3", "5.3"),
            ("重量", "590g", "708g"),
            ("価格差", "¥29,700", "¥18,700"),
        ],
        "summary_a": "Boseらしい豊かな低音と大音量。防水IP67でアウトドアにも対応。接続の安定性も優秀。",
        "summary_b": "1.1万円安くてバッテリーが10時間長持ち。Marshallレトロデザインがインテリアとしても映える。",
    },
    {
        "slug": "compare-jblflip6-vs-boseSoundLinkMax",
        "category": "スピーカー",
        "product_a": {"name": "JBL Flip 6", "price": "¥14,800", "score": 4.5, "slug": "review-jblflip6"},
        "product_b": {"name": "Bose SoundLink Max", "price": "¥29,700", "score": 4.7, "slug": "review-boseSoundLinkMax"},
        "verdict": "コンパクトなポータブルスピーカーを安く求めるならJBL Flip 6、より高音質な大型サウンドならBose SoundLink Max",
        "specs": [
            ("防水", "IP67", "IP67"),
            ("連続再生", "12時間", "20時間"),
            ("出力", "30W", "大出力"),
            ("重量", "550g", "590g"),
            ("価格差", "¥14,800", "¥29,700"),
        ],
        "summary_a": "1.5万円で防水IP67・12時間バッテリー。JBLらしいドンシャリサウンドがアウトドアに映える。",
        "summary_b": "1.5万円高いがバッテリーが8時間長く音圧・音質が上。自宅でもアウトドアでも使える万能機。",
    },
]


def make_stars(score):
    """スコアを星表示に変換"""
    full = int(score)
    half = 1 if (score - full) >= 0.3 else 0
    empty = 5 - full - half
    return "★" * full + ("½" if half else "") + "☆" * empty


def score_bar_width(score):
    return int(score / 5.0 * 100)


def make_amazon_search_url(name):
    import urllib.parse
    return f"https://www.amazon.co.jp/s?k={urllib.parse.quote(name)}&tag=gadgetnavi-22"


def make_rakuten_search_url(name):
    import urllib.parse
    return f"https://search.rakuten.co.jp/search/mall/{urllib.parse.quote(name)}/"


def generate_html(article):
    slug = article["slug"]
    cat = article["category"]
    pa = article["product_a"]
    pb = article["product_b"]
    verdict = article["verdict"]
    specs = article["specs"]
    summary_a = article["summary_a"]
    summary_b = article["summary_b"]

    cfg = CATEGORY_CONFIG.get(cat, CATEGORY_CONFIG["スマートフォン"])
    gradient = cfg["gradient"]
    emoji = cfg["emoji"]
    cat_label = cfg["cat_label"]
    cat_page = cfg["cat_page"]

    title = f"{pa['name']} vs {pb['name']} 徹底比較【2026年版】｜ガジェットナビ"
    canonical = f"{BASE_URL}{slug}.html"
    desc = f"{pa['name']}と{pb['name']}を徹底比較。価格・スペック・使い勝手を詳しく解説します。どちらを買うべきかを明確にします。"

    winner = pa["name"] if pa["score"] >= pb["score"] else pb["name"]
    score_diff = abs(pa["score"] - pb["score"])

    # スコア判定
    if score_diff == 0:
        score_comment = f"両機種とも同スコアで甲乙つけがたい。用途によって選択を。"
    else:
        w = pa if pa["score"] > pb["score"] else pb
        l = pb if pa["score"] > pb["score"] else pa
        score_comment = f"総合スコアでは{w['name']}({w['score']})が{l['name']}({l['score']})を上回る。"

    # スペック比較テーブル行
    spec_rows = ""
    for i, (label, val_a, val_b) in enumerate(specs):
        highlight_a = " style=\"background:#fff3e0;font-weight:700;\"" if i % 3 == 0 else ""
        highlight_b = " style=\"background:#e8f5e9;font-weight:700;\"" if i % 3 == 1 else ""
        spec_rows += f"""
        <tr>
          <td class="spec-label">{label}</td>
          <td{highlight_a}>{val_a}</td>
          <td{highlight_b}>{val_b}</td>
        </tr>"""

    amazon_a = make_amazon_search_url(pa["name"])
    amazon_b = make_amazon_search_url(pb["name"])
    rakuten_a = make_rakuten_search_url(pa["name"])
    rakuten_b = make_rakuten_search_url(pb["name"])

    review_a = pa.get("slug", f"review-{pa['name'].lower().replace(' ', '')}")
    review_b = pb.get("slug", f"review-{pb['name'].lower().replace(' ', '')}")

    score_bar_a = score_bar_width(pa["score"])
    score_bar_b = score_bar_width(pb["score"])

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <script>!function(){{if(location.pathname.startsWith('/en/'))return;if(localStorage.getItem('gadgetnavi_lang')==='ja')return;var l=(navigator.language||'').toLowerCase();if(l==='en'||l.startsWith('en-')){{localStorage.setItem('gadgetnavi_lang','en');location.replace('/en'+location.pathname+location.search);}}}}();</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <link rel="sitemap" type="application/xml" href="{BASE_URL}sitemap.xml">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{pa['name']} vs {pb['name']} 徹底比較【2026年版】">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="ガジェットナビ">
  <meta property="og:image" content="{BASE_URL}ogp-default.svg">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{pa['name']} vs {pb['name']} 徹底比較【2026年版】",
    "author": {{ "@type": "Organization", "name": "ガジェットナビ編集部" }},
    "datePublished": "{TODAY}",
    "dateModified": "{TODAY}",
    "description": "{desc}",
    "publisher": {{ "@type": "Organization", "name": "ガジェットナビ", "url": "{BASE_URL}" }}
  }}
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2054301472533985" crossorigin="anonymous"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-ERDKSGNEWS');
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800;900&display=swap" rel="stylesheet">
  <style>
    .compare-page {{ max-width: 860px; margin: 0 auto; padding: 40px 20px 80px; }}
    .breadcrumb {{ font-size: 0.8rem; color: var(--text-light); margin-bottom: 24px; display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
    .breadcrumb a {{ color: var(--primary); }}
    .compare-hero {{ border-radius: var(--radius); padding: 40px 32px; margin-bottom: 32px; background: {gradient}; color: #fff; text-align: center; }}
    .compare-hero .cat-badge {{ display: inline-block; background: rgba(255,255,255,0.15); color: rgba(255,255,255,0.9); font-size: 0.72rem; font-weight: 700; letter-spacing: 0.14em; padding: 4px 14px; border-radius: 20px; margin-bottom: 14px; }}
    .compare-hero h1 {{ font-size: clamp(1.2rem, 3vw, 1.8rem); font-weight: 900; line-height: 1.4; margin-bottom: 10px; }}
    .compare-hero .hero-emoji {{ font-size: 3rem; margin-bottom: 10px; display: block; }}
    .compare-hero .hero-sub {{ font-size: 0.85rem; color: rgba(255,255,255,0.7); }}
    .verdict-banner {{ background: linear-gradient(135deg, #fff8f0, #fff3e0); border: 2px solid var(--primary); border-radius: var(--radius); padding: 20px 24px; margin-bottom: 32px; }}
    .verdict-banner .verdict-label {{ font-size: 0.78rem; font-weight: 700; color: var(--primary); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px; }}
    .verdict-banner p {{ font-size: 1rem; font-weight: 700; color: #222; line-height: 1.6; margin: 0; }}
    .score-compare {{ display: grid; grid-template-columns: 1fr auto 1fr; gap: 16px; align-items: center; background: var(--secondary); border-radius: var(--radius); padding: 28px; margin-bottom: 32px; }}
    .score-card {{ background: rgba(255,255,255,0.07); border-radius: var(--radius-sm); padding: 20px 16px; text-align: center; color: #fff; }}
    .score-card .prod-name {{ font-size: 0.88rem; font-weight: 700; margin-bottom: 6px; color: rgba(255,255,255,0.8); }}
    .score-card .prod-price {{ font-size: 1rem; font-weight: 900; color: var(--accent); margin-bottom: 10px; }}
    .score-card .score-num {{ font-size: 3.2rem; font-weight: 900; color: var(--accent); line-height: 1; }}
    .score-card .score-max {{ font-size: 0.8rem; color: rgba(255,255,255,0.5); }}
    .score-card .score-bar-wrap {{ background: rgba(255,255,255,0.1); border-radius: 10px; height: 8px; overflow: hidden; margin-top: 10px; }}
    .score-card .score-bar {{ height: 100%; border-radius: 10px; background: var(--accent); }}
    .vs-badge {{ font-size: 1.4rem; font-weight: 900; color: #fff; background: var(--primary); width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
    .spec-compare-table {{ width: 100%; border-collapse: collapse; margin: 20px 0 32px; font-size: 0.88rem; }}
    .spec-compare-table th {{ background: var(--secondary); color: var(--white); padding: 12px 16px; font-weight: 700; }}
    .spec-compare-table .spec-label {{ background: #f5f5f5; font-weight: 700; color: #444; padding: 12px 16px; width: 28%; }}
    .spec-compare-table td {{ padding: 12px 16px; border-bottom: 1px solid var(--border); vertical-align: middle; }}
    .spec-compare-table tr:last-child td {{ border-bottom: none; }}
    .product-detail-section {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 32px; }}
    .product-card {{ background: #fafafa; border: 1px solid var(--border); border-radius: var(--radius); padding: 20px; }}
    .product-card h3 {{ font-size: 1rem; font-weight: 800; margin-bottom: 10px; color: var(--secondary); }}
    .product-card p {{ font-size: 0.88rem; line-height: 1.8; color: #555; margin: 0; }}
    .buy-section {{ background: #fff8f0; border: 2px solid var(--primary); border-radius: var(--radius); padding: 24px; margin-bottom: 32px; }}
    .buy-section h3 {{ font-size: 1rem; font-weight: 800; margin-bottom: 16px; color: #222; text-align: center; }}
    .buy-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
    .buy-item {{ text-align: center; }}
    .buy-item .buy-name {{ font-size: 0.85rem; font-weight: 700; margin-bottom: 10px; color: #333; }}
    .buy-btns {{ display: flex; flex-direction: column; gap: 8px; }}
    .btn-amazon {{ display: inline-flex; align-items: center; justify-content: center; gap: 8px; background: #ff9900; color: #111; padding: 10px 18px; border-radius: 50px; font-weight: 800; font-size: 0.85rem; transition: opacity 0.2s; }}
    .btn-amazon:hover {{ opacity: 0.85; }}
    .btn-rakuten {{ display: inline-flex; align-items: center; justify-content: center; gap: 8px; background: #bf0000; color: #fff; padding: 10px 18px; border-radius: 50px; font-weight: 800; font-size: 0.85rem; transition: opacity 0.2s; }}
    .btn-rakuten:hover {{ opacity: 0.85; }}
    .btn-review {{ display: inline-flex; align-items: center; justify-content: center; gap: 6px; background: var(--secondary); color: #fff; padding: 10px 18px; border-radius: 50px; font-weight: 700; font-size: 0.85rem; transition: opacity 0.2s; }}
    .btn-review:hover {{ opacity: 0.85; }}
    .summary-section {{ background: var(--secondary); color: #fff; border-radius: var(--radius); padding: 28px 32px; margin-bottom: 32px; }}
    .summary-section h2 {{ font-size: 1.1rem; font-weight: 800; margin-bottom: 16px; color: var(--accent); }}
    .summary-section p {{ font-size: 0.9rem; line-height: 1.85; color: rgba(255,255,255,0.85); margin: 0; }}
    @media (max-width: 768px) {{
      .compare-page {{ padding: 20px 14px 60px; }}
      .compare-hero {{ padding: 28px 16px; }}
      .score-compare {{ grid-template-columns: 1fr; gap: 12px; padding: 20px 14px; }}
      .vs-badge {{ margin: 0 auto; }}
      .product-detail-section {{ grid-template-columns: 1fr; }}
      .buy-grid {{ grid-template-columns: 1fr; }}
      .spec-compare-table th, .spec-compare-table td {{ padding: 9px 10px; font-size: 0.82rem; }}
    }}
  </style>
</head>
<body>
<header>
  <div class="header-inner">
    <a href="index.html" class="logo">📱 ガジェット<span class="logo-dot">ナビ</span></a>
    <nav>
      <a href="index.html#ranking">ランキング</a>
      <a href="index.html#reviews">レビュー</a>
      <a href="privacy.html">プライバシー</a>
    </nav>
    <div style="display:flex;align-items:center;gap:6px;">
      <span class="lang-btn active">🇯🇵 JA</span>
    </div>
  </div>
</header>

<div style="background:var(--white); padding: 12px 20px; border-bottom:1px solid var(--border);">
  <div class="compare-page" style="padding:0;">
    <div class="breadcrumb">
      <a href="index.html">トップ</a>
      <span>›</span>
      <a href="{cat_page}">{cat}</a>
      <span>›</span>
      <span>{pa['name']} vs {pb['name']}</span>
    </div>
  </div>
</div>

<main>
<div class="compare-page">

  <div class="compare-hero">
    <span class="hero-emoji">{emoji}</span>
    <div class="cat-badge">{cat_label} COMPARISON</div>
    <h1>{pa['name']} vs {pb['name']}<br>徹底比較【2026年版】</h1>
    <p class="hero-sub">どちらを買うべき？価格・スペック・使い勝手を徹底解説</p>
  </div>

  <div class="verdict-banner">
    <div class="verdict-label">📌 結論</div>
    <p>{verdict}</p>
  </div>

  <div class="score-compare">
    <div class="score-card">
      <div class="prod-name">{pa['name']}</div>
      <div class="prod-price">{pa['price']}</div>
      <div class="score-num">{pa['score']}</div>
      <div class="score-max">/ 5.0</div>
      <div class="score-bar-wrap"><div class="score-bar" style="width:{score_bar_a}%"></div></div>
    </div>
    <div class="vs-badge">VS</div>
    <div class="score-card">
      <div class="prod-name">{pb['name']}</div>
      <div class="prod-price">{pb['price']}</div>
      <div class="score-num">{pb['score']}</div>
      <div class="score-max">/ 5.0</div>
      <div class="score-bar-wrap"><div class="score-bar" style="width:{score_bar_b}%"></div></div>
    </div>
  </div>

  <h2 style="font-size:1.15rem;font-weight:800;margin:0 0 14px;padding-left:14px;border-left:4px solid var(--primary);">スペック比較</h2>
  <table class="spec-compare-table">
    <thead>
      <tr>
        <th>項目</th>
        <th>{pa['name']}</th>
        <th>{pb['name']}</th>
      </tr>
    </thead>
    <tbody>{spec_rows}
    </tbody>
  </table>

  <div class="product-detail-section">
    <div class="product-card">
      <h3>✅ {pa['name']} の特徴</h3>
      <p>{summary_a}</p>
    </div>
    <div class="product-card">
      <h3>✅ {pb['name']} の特徴</h3>
      <p>{summary_b}</p>
    </div>
  </div>

  <div class="buy-section">
    <h3>🛒 最安値をチェック・詳細レビューを見る</h3>
    <div class="buy-grid">
      <div class="buy-item">
        <div class="buy-name">{pa['name']}<br><small>{pa['price']} / スコア{pa['score']}</small></div>
        <div class="buy-btns">
          <a href="{amazon_a}" target="_blank" rel="noopener nofollow" class="btn-amazon">🛒 Amazonで見る</a>
          <a href="{rakuten_a}" target="_blank" rel="noopener nofollow" class="btn-rakuten">🛍️ 楽天で見る</a>
          <a href="{review_a}.html" class="btn-review">📄 詳細レビューを読む</a>
        </div>
      </div>
      <div class="buy-item">
        <div class="buy-name">{pb['name']}<br><small>{pb['price']} / スコア{pb['score']}</small></div>
        <div class="buy-btns">
          <a href="{amazon_b}" target="_blank" rel="noopener nofollow" class="btn-amazon">🛒 Amazonで見る</a>
          <a href="{rakuten_b}" target="_blank" rel="noopener nofollow" class="btn-rakuten">🛍️ 楽天で見る</a>
          <a href="{review_b}.html" class="btn-review">📄 詳細レビューを読む</a>
        </div>
      </div>
    </div>
  </div>

  <div class="summary-section">
    <h2>🏆 総評・まとめ</h2>
    <p>{score_comment}<br><br>{verdict}<br><br>どちらの製品も優れた選択肢ですが、使用目的・予算・既存の生態系との相性で最適解は変わります。詳しくは各製品の個別レビューページもご参照ください。</p>
  </div>

  <div style="text-align:center;margin-top:32px;">
    <a href="{cat_page}" style="display:inline-flex;align-items:center;gap:8px;background:var(--primary);color:#fff;padding:12px 28px;border-radius:50px;font-weight:700;font-size:0.9rem;">← {cat}の比較・レビュー一覧へ</a>
  </div>

</div>
</main>

<footer>
  <div class="footer-inner">
    <div class="logo" style="font-size:1.1rem;">📱 ガジェット<span class="logo-dot">ナビ</span></div>
    <p style="font-size:0.8rem;color:var(--text-light);margin-top:8px;">最新ガジェットのレビュー・比較情報を発信するメディアです。</p>
    <div class="footer-links">
      <a href="about.html">このサイトについて</a>
      <a href="privacy.html">プライバシーポリシー</a>
      <a href="contact.html">お問い合わせ</a>
    </div>
    <p class="footer-copy">© 2026 ガジェットナビ. All rights reserved.</p>
  </div>
</footer>

</body>
</html>"""
    return html


def update_sitemap(slugs):
    sitemap_path = os.path.join(OUTPUT_DIR, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_entries = ""
    for slug in slugs:
        new_entries += f"""  <url>
    <loc>{BASE_URL}{slug}.html</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""

    updated = content.replace("</urlset>", new_entries + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"sitemap.xml を更新しました（{len(slugs)}件追加）")


def main():
    generated = []
    for article in ARTICLES:
        slug = article["slug"]
        html = generate_html(article)
        filepath = os.path.join(OUTPUT_DIR, f"{slug}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"生成: {slug}.html")
        generated.append(slug)

    print(f"\n✅ {len(generated)} ファイルを生成しました")

    # sitemap.xml を更新
    update_sitemap(generated)
    print("完了！")


if __name__ == "__main__":
    main()
