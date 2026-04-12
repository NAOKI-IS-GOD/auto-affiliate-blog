#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_v2_gen.py  —  Rich comparison pages (spec table + sections + pros/cons + who-to-buy)
Run:  python _v2_gen.py
"""
import pathlib, re
from urllib.parse import quote_plus

BASE  = pathlib.Path(r"C:\Users\81804\OneDrive\デスクトップ\auto-affiliate-blog-main")
EN    = BASE / "en"
SITE  = "https://auto-affiliate-blog-mauve.vercel.app/"
REDIR = "  <script>!function(){if(location.pathname.startsWith('/en/'))return;if(localStorage.getItem('gadgetnavi_lang')==='ja')return;var l=(navigator.language||'').toLowerCase();if(l==='en'||l.startsWith('en-')){localStorage.setItem('gadgetnavi_lang','en');location.replace('/en'+location.pathname+location.search);}}();</script>"
CAT_SLUG = {
  "スマートフォン":"cat-smartphone.html","イヤホン":"cat-earphone.html",
  "スマートウォッチ":"cat-smartwatch.html","タブレット":"cat-tablet.html",
  "ノートPC":"cat-laptop.html","ゲーム機":"cat-gaming.html",
  "モニター":"cat-monitor.html","カメラ":"cat-camera.html",
  "ロボット掃除機":"cat-robotvacuum.html","スピーカー":"cat-speaker.html",
}

# ── Device specs: [display, panel, chip, ram, storage, camera/key, battery, charging, weight, ip, os, price_ja, price_en]
SP = {
"iPhone 16 Pro Max":["6.9型","Super Retina XDR OLED ProMotion 1-120Hz","Apple A18 Pro","8GB","256GB〜1TB","48MP+48MP超広角+12MP 5倍望遠","4685mAh","27W有線/25W MagSafe","228g","IP68","iOS 18","¥194,800〜","$1,199+"],
"Galaxy S25 Ultra":["6.9型","Dynamic AMOLED 2X LTPO 1-120Hz","Snapdragon 8 Elite","12GB","256GB〜1TB","200MP+50MP超広角+10MP 3倍+50MP 5倍","5000mAh","45W有線/15Wワイヤレス","218g","IP68","Android 15","¥189,800〜","$1,299+"],
"iPhone 16":["6.1型","Super Retina XDR OLED 60-120Hz","Apple A18","8GB","128GB〜512GB","48MP+12MP超広角","3561mAh","25W有線/15W MagSafe","170g","IP68","iOS 18","¥124,800〜","$799+"],
"Pixel 9a":["6.3型","Actua OLED 60-120Hz","Google Tensor G4","8GB","128GB〜256GB","48MP+13MP超広角","5100mAh","23W有線","186g","IP67","Android 15","¥79,800〜","$499+"],
"Galaxy S25":["6.2型","Dynamic AMOLED 2X LTPO 1-120Hz","Snapdragon 8 Elite","12GB","128GB〜512GB","50MP+12MP超広角+10MP 3倍","4000mAh","25W有線/15Wワイヤレス","162g","IP68","Android 15","¥124,800〜","$799+"],
"iPhone SE4":["6.1型","Super Retina XDR OLED 60Hz","Apple A18","8GB","128GB〜256GB","48MP シングル","3279mAh","20W有線/15W MagSafe","167g","IP68","iOS 18","¥74,800〜","$429+"],
"Nothing Phone 3a":["6.77型","AMOLED 60-120Hz","Snapdragon 7s Gen 3","8GB","128GB〜256GB","50MP+50MP超広角+8MP望遠","5000mAh","45W有線","201g","IP54","Nothing OS 3.0","¥49,800〜","$329+"],
"Pixel 9 Pro":["6.3型","LTPO OLED 1-120Hz","Google Tensor G4","16GB","128GB〜1TB","50MP+48MP超広角+48MP 5倍望遠","4700mAh","27W有線/21Wワイヤレス","199g","IP68","Android 15","¥159,800〜","$999+"],
"Xiaomi 14 Ultra":["6.73型","AMOLED 1-120Hz","Snapdragon 8 Gen 3","16GB","256GB〜1TB","50MP Leica 4眼","5000mAh","90W有線/80Wワイヤレス","219g","IP68","HyperOS","¥159,800〜","$1,399+"],
"Xperia 1 VI":["6.5型","4K OLED 1-120Hz","Snapdragon 8 Gen 3","12GB","256GB〜512GB","52MP+12MP超広角+12MP望遠","5000mAh","30W有線/15Wワイヤレス","192g","IP65/68","Android 14","¥189,700〜","$1,299+"],
"OnePlus 13":["6.82型","LTPO4 AMOLED 1-120Hz","Snapdragon 8 Elite","16GB","256GB〜1TB","50MP+50MP超広角+50MP望遠","6000mAh","100W有線/50Wワイヤレス","210g","IP65","OxygenOS 15","¥109,800〜","$899+"],
"Xiaomi 15":["6.36型","OLED 1-120Hz","Snapdragon 8 Elite","16GB","256GB〜1TB","50MP Leica 3眼","5240mAh","90W有線/50Wワイヤレス","190g","IP68","HyperOS 2","¥129,800〜","$999+"],
"OPPO Find X8 Pro":["6.78型","AMOLED 1-120Hz","Snapdragon 8 Gen 3","16GB","256GB〜1TB","50MP Hasselblad 4眼","5910mAh","80W有線/50Wワイヤレス","218g","IP69","ColorOS 15","¥119,800〜","$999+"],
"Galaxy A55":["6.6型","Super AMOLED 120Hz","Exynos 1480","8GB","128GB〜256GB","50MP+12MP超広角+5MPマクロ","5000mAh","25W有線","213g","IP67","Android 14","¥59,800〜","$449+"],
"iPhone 16 Plus":["6.7型","Super Retina XDR OLED 60-120Hz","Apple A18","8GB","128GB〜512GB","48MP+12MP超広角","4674mAh","25W有線/15W MagSafe","223g","IP68","iOS 18","¥149,800〜","$899+"],
"Galaxy S25+":["6.7型","Dynamic AMOLED 2X LTPO 1-120Hz","Snapdragon 8 Elite","12GB","256GB〜512GB","50MP+12MP超広角+10MP 3倍","4900mAh","45W有線/15Wワイヤレス","190g","IP68","Android 15","¥159,800〜","$999+"],
"Apple Watch Series 10":["46mm","Always-On Retina LTPO OLED","Apple S10","−","64GB","心拍/血中酸素/ECG/皮膚温度","18時間","磁気高速充電","41.7g","IP6X/WR50","watchOS 11","¥59,800〜","$399+"],
"Apple Watch Ultra 2":["49mm","Always-On Retina LTPO OLED","Apple S9","−","64GB","心拍/血中酸素/ECG/水中深度計","60時間","磁気高速充電","61.4g","WR100m/MIL-STD","watchOS 11","¥129,800〜","$799+"],
"Galaxy Watch 7":["44mm","Super AMOLED Always-On","Exynos W1000","2GB","32GB","心拍/血中酸素/ECG/体成分","40時間","ワイヤレス充電","33.8g","IP68/5ATM","Wear OS 5","¥44,800〜","$299+"],
"Pixel Watch 3":["45mm","AMOLED Always-On 60Hz","Snapdragon W5","2GB","32GB","心拍/血中酸素/ECG/皮膚温度","24時間","磁気ワイヤレス","37g","IP68/5ATM","Wear OS 4","¥49,800〜","$349+"],
"Garmin Fenix 8":["47mm","MIP/AMOLED選択可","−","−","32GB","心拍/血中酸素/ECG/VO2Max/マルチスポーツ","最大16日間","ソーラー充電対応","79g","水深100m","Garmin OS","¥129,800〜","$799+"],
"Garmin Venu 3":["45mm","AMOLED Always-On","−","−","4GB","心拍/血中酸素/ストレス/睡眠","最大14日間","ワイヤレス充電","50g","5ATM/MIL-STD","Garmin OS","¥69,800〜","$449+"],
"MacBook Air M3":["13.6型","Liquid Retina IPS 2560×1664","Apple M3 8コア","8〜24GB","256GB〜2TB SSD","−","15〜18時間","USB-C/MagSafe","1.24kg","−","macOS","¥164,800〜","$1,099+"],
"MacBook Pro M4 Pro":["14.2型","Liquid Retina XDR OLED 3024×1964","Apple M4 Pro 12コア","24〜48GB","512GB〜4TB SSD","−","22〜24時間","USB-C/MagSafe 140W","1.55kg","−","macOS","¥298,800〜","$1,999+"],
"Dell XPS 15":["15.6型","OLED 3.5K 3456×2160","Intel Core i7-13700H","16〜64GB","512GB〜1TB SSD","RTX 4060","6〜8時間","130W USB-C","1.86kg","−","Windows 11","¥249,800〜","$1,699+"],
"Surface Pro 11":["13型","QLCD タッチ 2880×1920","Snapdragon X Elite","16〜64GB","256GB〜1TB SSD","−","12〜14時間","Surface Connect/USB-C","0.90kg(本体のみ)","−","Windows 11","¥219,800〜","$1,499+"],
"ThinkPad X1 Carbon":["14型","IPS/OLED選択可 1920×1200〜","Intel Core Ultra 7","16〜64GB","256GB〜1TB SSD","−","11〜15時間","USB-C 65W","1.12kg","MIL-STD-810H","Windows 11","¥229,800〜","$1,599+"],
"ASUS ROG Zephyrus G14":["14型","QHD+ OLED 2560×1600 165Hz","AMD Ryzen 9 7940HS","16〜32GB","512GB〜1TB SSD","RTX 4060/4070","8〜10時間(軽作業時)","140W USB-C","1.65kg","−","Windows 11","¥219,800〜","$1,699+"],
"Razer Blade 15":["15.6型","QHD OLED 2560×1440 240Hz","Intel Core i7-13800H","16〜32GB","1TB SSD","RTX 4070 Ti","4〜6時間(ゲーム時)","230W AC","2.01kg","−","Windows 11","¥299,800〜","$2,499+"],
"iPad Pro M4":["11〜13型","Ultra Retina XDR OLED tandem","Apple M4","8〜16GB","256GB〜2TB","12MP+10MP超広角","最大10時間","20W USB-C","444〜579g","IP68","iPadOS 18","¥168,800〜","$999+"],
"iPad Air M2":["11〜13型","Liquid Retina IPS 2360×1640","Apple M2","8GB","128GB〜1TB","12MP+12MP超広角","最大10時間","20W USB-C","462〜617g","−","iPadOS 18","¥98,800〜","$599+"],
"iPad Mini 7":["8.3型","Liquid Retina IPS 2266×1488","Apple A17 Pro","8GB","128GB〜512GB","12MP+12MP超広角","最大10時間","20W USB-C","293g","−","iPadOS 18","¥78,800〜","$499+"],
"Galaxy Tab S10 Ultra":["14.6型","Dynamic AMOLED 2X 2960×1848 120Hz","Snapdragon 8 Gen 3","12〜16GB","256GB〜1TB","13MP前面×2/12MP+8MP背面","11200mAh 最大15時間","45W有線/15Wワイヤレス","718g","IP68","Android 14","¥189,800〜","$1,199+"],
"Kindle Paperwhite":["6.8型","E Ink 300ppi","Mediatek MTK 8113","2GB","16〜32GB","−","最長6週間","USB-C 9W","213g","IPX8","Kindle OS","¥19,980〜","$139+"],
"Sony WF-1000XM5":["−","ドライバー 8.4mm","QN2e HDプロセッサ","−","−","LDAC/AAC/SBC","最大36時間(ケース込み)","8時間+ケース","5.9g/片耳","IPX4","−","¥39,600","$279"],
"Bose QC Earbuds II":["−","ドライバー 9.3mm","CustomTune テクノロジー","−","−","AAC/SBC","最大30時間(ケース込み)","6時間+ケース","6.2g/片耳","IPX4","−","¥38,500","$279"],
"Galaxy Buds 3 Pro":["−","ドライバー 10.5mm+6mm 2way","−","−","−","SSC/AAC/SBC","最大36時間(ケース込み)","6時間+ケース","5.5g/片耳","IPX7","−","¥29,800","$199"],
"JBL Tour Pro 3":["−","ドライバー 10mm","−","−","−","LDAC/AAC","最大50時間(スマートケース込み)","10時間+ケース","6.5g/片耳","IP55","−","¥34,800","$249"],
"Nothing Ear 2":["−","ドライバー 11.6mm","−","−","−","LDAC/AAC/SBC","最大42時間(ケース込み)","6.3時間+ケース","4.5g/片耳","IP54","−","¥18,800","$149"],
"Anker Liberty 4 NC":["−","ドライバー 11mm","−","−","−","LDAC/LHDC/AAC","最大60時間(ケース込み)","10時間+ケース","5.5g/片耳","IPX4","−","¥9,990","$79"],
"Sennheiser MOMENTUM TW4":["−","ドライバー 7mm","−","−","−","aptX Adaptive/AAC/SBC","最大43.5時間(ケース込み)","7.5時間+ケース","5.7g/片耳","IP54","−","¥44,000","$329"],
"Technics EAH-AZ80":["−","ドライバー 10mm","−","−","−","LDAC/aptX Adaptive/AAC","最大32時間(ケース込み)","7時間+ケース","7g/片耳","IPX4","−","¥44,000","$299"],
"Sony WH-1000XM5":["オーバーイヤー","ドライバー 30mm","V1+QN1チップ","−","−","LDAC/AAC/SBC","30時間(ANC ON)","3.5時間充電","250g","−","−","¥49,500","$349"],
"Bose QC45":["オーバーイヤー","ドライバー 40mm","Bose カスタム設計","−","−","AAC/SBC","24時間(ANC ON)","2.5時間充電","238g","−","−","¥44,000","$329"],
"JBL Flip 6":["ポータブル","ドライバー 44mm+パッシブ×2","−","−","−","Bluetooth 5.1","最大12時間","USB-C","530g","IP67","−","¥14,800","$129"],
"Bose SoundLink Max":["ポータブル","フルレンジ+パッシブラジエーター×2","−","−","−","Bluetooth 5.3/Wi-Fi","最大20時間","USB-C","1.03kg","IPX4","−","¥29,700","$399"],
"Marshall Emberton III":["ポータブル","フルレンジ×2+パッシブラジエーター","−","−","−","Bluetooth 5.3","最大30時間","USB-C","680g","IPX7","−","¥21,780","$149"],
"GoPro HERO12 Black":["アクションカム","センサー 1/1.9型","GP2チップ","−","−","5.3K60fps/4K120fps/HyperSmooth 6.0","最大70分","USB-C","154g","水深10m防水","−","¥49,800","$349"],
"DJI Osmo Action 4":["アクションカム","センサー 1/1.3型","DJI O4チップ","−","−","4K120fps/2.7K240fps/RockSteady 3.0","最大160分(1080p時)","USB-C","145g","水深18m防水","−","¥49,800","$199"],
"Insta360 X4":["360°カメラ","センサー 1/2型×2","Insta360チップ","−","−","8K30fps 360°/4K60fps/FlowState手ブレ補正","最大135分","USB-C","203g","水深10m防水","−","¥66,000","$399"],
"Sony ZV-E10 II":["ミラーレス APS-C","センサー 26.1MP Exmor R","BIONZ XR","−","Eマウント","4K30fps/FHD120fps/シングルAF","最大570枚","USB-C給電可","291g","−","Sony E Mount","¥89,800〜","$749+"],
"Canon EOS R50":["ミラーレス APS-C","センサー 24.2MP CMOS","DIGIC X","−","RF-Sマウント","4K30fps(クロップ)/FHD120fps/デュアルピクセルAF","最大210枚","USB-C給電可","375g","−","Canon RF-S","¥89,800〜","$679+"],
"Fujifilm X-T5":["ミラーレス APS-C","センサー 40.2MP X-Trans CMOS 5 HR","X-Processor 5","−","Xマウント","6.2K30fps/4K60fps/位相差AF+IBIS","最大740枚","USB-C給電可","557g","−","Fujifilm X Mount","¥239,800〜","$1,699+"],
"Sony α7C II":["ミラーレス フルサイズ","センサー 33MP BSI CMOS","BIONZ XR+AI","−","Eマウント","4K60fps(S35)/4K30fps(FF)/AIトラッキングAF","最大530枚","USB-C給電可","514g","−","Sony FE Mount","¥319,800〜","$2,199+"],
"LG 27GP850B":["27型","Nano IPS 2560×1440 QHD","−","−","HDMI×2/DP×1","165Hz / 1ms GtG","DisplayHDR 400","HDMI×2, DP×1, USB-A×2","5.4kg","−","−","¥39,800〜","$329+"],
"ASUS ROG Swift PG279QM":["27型","IPS 2560×1440 QHD","−","−","HDMI×2/DP×1","240Hz / 1ms GtG","DisplayHDR 400","HDMI×2, DP×1, USB-A×2","6.2kg","−","−","¥64,800〜","$499+"],
"Samsung Odyssey G7 28\"":["28型","IPS 3840×2160 4K","−","−","HDMI 2.1×2/DP 1.4×1","144Hz / 1ms GtG","DisplayHDR 400","HDMI 2.1×2, DP 1.4×1","5.6kg","−","−","¥54,800〜","$449+"],
"LG 45GR95QEB":["45型","OLED 3440×1440 UWQHD","−","−","HDMI 2.1×2/DP 1.4×2","240Hz / 0.03ms GtG","Dolby Vision/HDR TrueBlack 400","HDMI 2.1×2, DP 1.4×2","12.5kg","−","−","¥184,800〜","$1,499+"],
"BenQ PD3205U":["32型","IPS 3840×2160 4K","−","−","USB-C 96W/HDMI×2/DP×1","60Hz / 5ms GtG","DisplayHDR 400","USB-C 96W, HDMI×2, DP×1","8.2kg","−","−","¥79,800〜","$649+"],
"Dell U2723D":["27型","IPS Black 2560×1440 QHD","−","−","USB-C 90W/HDMI/DP/USB-A×5","60Hz / 5ms GtG","DisplayHDR 400","USB-C 90W, HDMI 1.4, DP 1.2, USB-A×5","6.4kg","−","−","¥69,800〜","$549+"],
"iRobot Roomba J9+":["−","カメラAI+3D Sense障害物認識","−","−","−","ゴムブラシ×2+サイドブラシ","最大75分/充電+自動ゴミ収集","自動ゴミ収集ベース","3.5kg","−","iRobot OS","¥99,800〜","$849+"],
"Eufy RoboVac X8":["−","LiDAR+AIカメラ","−","−","−","デュアルブラシ/4000Pa×2","最大180分+自動ゴミ収集","自動ゴミ収集ベース","3.9kg","−","EufyOS","¥59,800〜","$499+"],
"Roborock S8 MaxV":["−","LiDAR+ReactiveAI+カメラ","−","−","−","デュアルブラシ+振動モップ/10000Pa","最大180分+自動洗浄ドック","自動洗浄・乾燥ドック","4.2kg","−","Roborock OS","¥139,800〜","$1,099+"],
"Dreame X40 Ultra":["−","LiDAR+AIカメラ障害物認識","−","−","−","デュアルブラシ+回転モップ/12000Pa","最大180分+自動洗浄・乾燥ドック","自動洗浄・乾燥ドック","4.5kg","−","Dreame OS","¥159,800〜","$1,299+"],
"Ecovacs X5 Pro":["−","LiDAR+AIVI 3D AI視覚認識","−","−","−","デュアルブラシ+振動モップ/12000Pa","最大180分+自動洗浄ドック","自動洗浄ドック","4.6kg","−","ECOVACS OS","¥149,800〜","$1,199+"],
"Nintendo Switch 2":["7型","LCD/TV出力4K対応","NVIDIA Tegra T239","12GB","256GB","任天堂 第1/第3パーティ","最大9時間(携帯モード)","USB-C充電","約400g","−","Nintendo OS","¥49,980〜","$449+"],
"PS5 Slim":["−","最大4K/8K出力","AMD Zen 2 + RDNA 2","16GB","825GB NVMe SSD","PS5 第1/第3パーティ","−","220V AC","3.2kg","−","PS5 OS","¥79,980〜","$449+"],
"Xbox Series X":["−","最大4K/8K出力","AMD Zen 2 + RDNA 2","16GB","1TB NVMe SSD","Game Pass/第3パーティ","−","220V AC","4.45kg","−","Xbox OS","¥64,978〜","$499+"],
}

# ── Spec table labels per category ───────────────────────────────────────────
CAT_SPEC_LABELS = {
  "スマートフォン": [
    ("ディスプレイサイズ","Display Size",0),("パネル / リフレッシュレート","Panel / Refresh Rate",1),
    ("プロセッサ","Processor",2),("RAM","RAM",3),("ストレージ","Storage",4),
    ("カメラ","Camera",5),("バッテリー","Battery",6),("充電","Charging",7),
    ("重量","Weight",8),("防水","Water Resistance",9),("OS","OS",10),
    ("価格(税込)","Price",11 if True else 12),
  ],
  "スマートウォッチ": [
    ("ケースサイズ","Case Size",0),("ディスプレイ","Display",1),
    ("チップ","Chip",2),("ストレージ","Storage",4),("センサー / 健康機能","Sensors / Health",5),
    ("バッテリー","Battery Life",6),("充電","Charging",7),("重量","Weight",8),
    ("耐水性","Water Resistance",9),("OS","OS",10),("価格","Price",11),
  ],
  "ノートPC": [
    ("ディスプレイ","Display",0),("パネル","Panel",1),("プロセッサ","Processor",2),
    ("RAM","RAM",3),("ストレージ","Storage",4),("GPU","GPU",5),
    ("バッテリー","Battery",6),("充電","Charging",7),("重量","Weight",8),
    ("OS","OS",10),("価格","Price",11),
  ],
  "タブレット": [
    ("ディスプレイ","Display",0),("パネル","Panel",1),("チップ","Chip",2),
    ("RAM","RAM",3),("ストレージ","Storage",4),("カメラ","Camera",5),
    ("バッテリー","Battery",6),("充電","Charging",7),("重量","Weight",8),
    ("防水","Water Resistance",9),("OS","OS",10),("価格","Price",11),
  ],
  "イヤホン": [
    ("タイプ","Type",0),("ドライバー","Driver",1),("コーデック","Codec",5),
    ("バッテリー合計","Total Battery",6),("本体単体","Earbuds Battery",7),
    ("重量(片耳)","Weight (per earbud)",8),("防水","Water Resistance",9),("価格","Price",11),
  ],
  "スピーカー": [
    ("タイプ","Type",0),("ドライバー","Driver",1),("接続","Connectivity",5),
    ("バッテリー","Battery",6),("充電","Charging",7),("重量","Weight",8),
    ("防水","Water Resistance",9),("価格","Price",11),
  ],
  "カメラ": [
    ("タイプ","Type",0),("センサー","Sensor",1),("プロセッサ","Processor",2),
    ("マウント","Mount",4),("動画","Video",5),("バッテリー","Battery",6),
    ("重量","Weight",8),("価格","Price",11),
  ],
  "モニター": [
    ("サイズ","Size",0),("解像度 / パネル","Resolution / Panel",1),
    ("リフレッシュレート / 応答速度","Refresh / Response",6),("HDR","HDR",7),
    ("接続端子","Connectivity",5),("重量","Weight",8),("価格","Price",11),
  ],
  "ロボット掃除機": [
    ("ナビゲーション","Navigation",1),("ブラシ / 吸引","Brush / Suction",5),
    ("バッテリー / 自動機能","Battery / Auto Features",6),("付属ドック","Dock",7),
    ("重量","Weight",8),("OS","OS",10),("価格","Price",11),
  ],
  "ゲーム機": [
    ("ディスプレイ / 出力","Display / Output",0),("解像度","Resolution",1),
    ("チップ","Chip",2),("RAM","RAM",3),("ストレージ","Storage",4),
    ("バッテリー / 電源","Battery / Power",6),("重量","Weight",8),("価格","Price",11),
  ],
}
# Fallback
for k in ["アクションカム","360°カメラ"]:
    CAT_SPEC_LABELS[k] = [
        ("タイプ","Type",0),("センサー","Sensor",1),("プロセッサ","Processor",2),
        ("動画","Video",5),("バッテリー","Battery",6),("充電","Charging",7),
        ("重量","Weight",8),("防水","Waterproofing",9),("価格","Price",11),
    ]

# ── Category section templates ────────────────────────────────────────────────
def secs(c, lang):
    """Return list of (title, body) tuples for the comparison."""
    a,b,cat = c["a"]["name"], c["b"]["name"], c["cat"]
    asp = SP.get(a, ["−"]*13)
    bsp = SP.get(b, ["−"]*13)
    ja = (lang=="ja")

    def row(lbl_ja, lbl_en, va, vb):
        return (lbl_ja if ja else lbl_en, va, vb)

    if cat == "スマートフォン":
        return [
          ("デザイン・質感" if ja else "Design & Build",
           f"{a}は{asp[8]}、{asp[9]}防水でプレミアムな質感。"
           f"{b}は{bsp[8]}と{bsp[9]}防水を実現。両機種ともフラッグシップにふさわしいビルド品質を誇るが、"
           f"手に馴染む感覚や素材の高級感にはそれぞれ個性がある。エコシステムへの投資方針と合わせて選びたい。"
           if ja else
           f"The {a} weighs {asp[8]} with {asp[9]} water resistance. The {b} weighs {bsp[8]} with {bsp[9]} protection. "
           f"Both deliver flagship-grade build quality, but each has its own character in terms of materials and in-hand feel. "
           f"Your choice of ecosystem should guide this decision."),

          ("ディスプレイ" if ja else "Display",
           f"{a}は{asp[0]}の{asp[1]}を搭載。{b}は{bsp[0]}の{bsp[1]}を採用。"
           f"両機とも最高水準のOLEDパネルで、明るい屋外でも視認性は抜群。"
           f"色精度・コントラストともに2026年トップクラスの仕上がりで、動画・写真鑑賞に最適だ。"
           if ja else
           f"The {a} features a {asp[0]} {asp[1]} panel. The {b} uses a {bsp[0]} {bsp[1]}. "
           f"Both deliver top-tier OLED quality with excellent outdoor visibility. "
           f"Color accuracy and contrast are best-in-class on both — great for media consumption."),

          ("パフォーマンス" if ja else "Performance",
           f"{a}は{asp[2]}を搭載し、{asp[3]} RAMで快適な動作を実現。"
           f"{b}は{bsp[2]}と{bsp[3]} RAMの組み合わせ。"
           f"日常的なSNS・ブラウジング・動画視聴では体感差はほぼゼロ。"
           f"重い動画編集やゲームでは各チップの特性が活きてくる場面もある。"
           if ja else
           f"The {a} runs on the {asp[2]} with {asp[3]} RAM. The {b} pairs {bsp[2]} with {bsp[3]} RAM. "
           f"For everyday tasks like social media, browsing and video, the difference is imperceptible. "
           f"Heavy video editing and gaming is where each chip's unique strengths become apparent."),

          ("カメラ" if ja else "Camera System",
           f"{a}のカメラ構成は{asp[5]}。{b}は{bsp[5]}を搭載する。"
           f"メインセンサーの解像度や望遠の倍率、超広角の画角など、それぞれ強みのある設計だ。"
           f"静止画・動画いずれも最高水準だが、日中の自然光撮影から夜景・ポートレートまで幅広く試してから判断したい。"
           if ja else
           f"The {a} camera system: {asp[5]}. The {b} offers: {bsp[5]}. "
           f"Each design has its own strengths in resolution, zoom range, and ultrawide coverage. "
           f"Both are top-tier for stills and video — test both in varied lighting before deciding."),

          ("バッテリー・充電" if ja else "Battery & Charging",
           f"{a}は{asp[6]}バッテリーで{asp[7]}に対応。"
           f"{b}は{bsp[6]}と{bsp[7]}を搭載。"
           f"充電速度の差は日常使いで地味に影響する。特に旅行や外出が多いユーザーは充電速度をしっかり確認しよう。"
           f"どちらも1日の使用には十分なバッテリー容量を持つ。"
           if ja else
           f"The {a} has a {asp[6]} battery with {asp[7]} charging. "
           f"The {b} packs {bsp[6]} and supports {bsp[7]}. "
           f"Charging speed differences matter in real life, especially for frequent travelers. "
           f"Both phones comfortably last a full day of normal use."),
        ]

    if cat == "スマートウォッチ":
        return [
          ("デザイン・ケースサイズ" if ja else "Design & Case Size",
           f"{a}は{asp[0]}ケース・{asp[8]}の軽量設計。{b}は{bsp[0]}・{bsp[8]}。"
           f"日常使いではケースサイズと重量がつけ心地に直結する。"
           f"ファッションアイテムとして腕につける時間が長い分、デザインへのこだわりは重要だ。"
           if ja else
           f"The {a} uses a {asp[0]} case weighing {asp[8]}. The {b} measures {bsp[0]} at {bsp[8]}. "
           f"For everyday wear, case size and weight directly affect comfort. "
           f"Since you'll wear it all day, design preference matters more than on other gadgets."),

          ("健康・フィットネス機能" if ja else "Health & Fitness Features",
           f"{a}は{asp[5]}などの健康センサーを搭載。{b}は{bsp[5]}を備える。"
           f"どちらも心拍・血中酸素計測は標準装備。"
           f"本格的なアスリート向けの多機能を求めるか、日常的な健康管理で十分かによって選択が変わる。"
           if ja else
           f"The {a} offers {asp[5]}. The {b} includes {bsp[5]}. "
           f"Both cover heart rate and blood oxygen as standard. "
           f"The choice depends on whether you need serious athlete-grade tracking or everyday wellness monitoring."),

          ("バッテリー持続時間" if ja else "Battery Life",
           f"{a}のバッテリーは{asp[6]}。{b}は{bsp[6]}を実現。"
           f"バッテリー持続時間はスマートウォッチ選択の重要ポイント。"
           f"毎日充電を苦にしないか、数日〜数週間のバッテリー持ちが必要かで最適解が変わる。"
           if ja else
           f"The {a} lasts {asp[6]}. The {b} achieves {bsp[6]}. "
           f"Battery life is a critical differentiator for smartwatches. "
           f"Whether you're OK with daily charging or need multi-day endurance will define the right choice."),

          ("エコシステム・スマートフォン連携" if ja else "Ecosystem & Smartphone Integration",
           f"{a}は{asp[10]}環境との連携を前提に設計されている。{b}は{bsp[10]}との組み合わせで真価を発揮。"
           f"スマートウォッチはスマートフォンとのペアリングが使い心地に大きく影響する。"
           f"現在使っているスマートフォンと同じエコシステムのウォッチを選ぶのが最も快適な選択肢だ。"
           if ja else
           f"The {a} is designed to integrate seamlessly with {asp[10]} devices. The {b} pairs best with {bsp[10]}. "
           f"Smartwatch satisfaction is heavily influenced by smartphone pairing. "
           f"Choosing a watch in your existing ecosystem almost always delivers the best experience."),
        ]

    if cat == "ノートPC":
        return [
          ("デザイン・携帯性" if ja else "Design & Portability",
           f"{a}は{asp[8]}の軽量ボディ。{b}は{bsp[8]}。"
           f"毎日持ち歩くノートPCでは重量とサイズが疲労感に直結する。"
           f"カフェ・出張・通勤での利用頻度が高い場合、軽量性は最も重要なスペックのひとつだ。"
           if ja else
           f"The {a} weighs {asp[8]}. The {b} comes in at {bsp[8]}. "
           f"For a laptop you carry daily, weight and size directly affect fatigue. "
           f"If you commute or travel frequently, portability may be the most critical spec."),

          ("ディスプレイ" if ja else "Display Quality",
           f"{a}は{asp[0]}の{asp[1]}パネルを搭載。{b}は{bsp[0]}の{bsp[1]}。"
           f"長時間の作業では目の疲れに直結するため、パネルの品質は重要。"
           f"写真・動画編集など色精度が求められる作業ではOLEDパネルが有利な場面が多い。"
           if ja else
           f"The {a} has a {asp[0]} {asp[1]} display. The {b} features a {bsp[0]} {bsp[1]}. "
           f"Panel quality directly affects eye fatigue during long work sessions. "
           f"For photo/video editing requiring color accuracy, OLED panels generally have the edge."),

          ("パフォーマンス" if ja else "Performance",
           f"{a}の{asp[2]}は{asp[3]}RAMと組み合わせ、日常作業から専門的な編集作業まで快適に処理。"
           f"{b}は{bsp[2]}と{bsp[3]}RAMの構成。"
           f"クリエイティブ作業・プログラミング・マルチタスクいずれも快適にこなせるが、GPU性能が必要な場合は注意が必要だ。"
           if ja else
           f"The {a}'s {asp[2]} with {asp[3]} RAM handles everything from daily tasks to demanding creative work. "
           f"The {b} pairs {bsp[2]} with {bsp[3]} RAM. "
           f"Both handle creative work, coding, and multitasking well — check GPU specs if you need graphics performance."),

          ("バッテリー持続時間" if ja else "Battery Life",
           f"{a}のバッテリーは{asp[6]}の持続時間を誇る。{b}は{bsp[6]}を実現。"
           f"外出先での充電機会が限られる場合、バッテリー持ちは生産性に直結する。"
           f"実使用では公称値より短くなる場合が多いため、余裕をもって選ぶのが賢明だ。"
           if ja else
           f"The {a} offers {asp[6]} battery life. The {b} delivers {bsp[6]}. "
           f"When away from outlets, battery life directly impacts productivity. "
           f"Real-world usage is typically shorter than rated — factor in a buffer when comparing."),
        ]

    if cat == "タブレット":
        return [
          ("ディスプレイ・デザイン" if ja else "Display & Design",
           f"{a}は{asp[0]}の{asp[1]}パネルを搭載。{b}は{bsp[0]}の{bsp[1]}。"
           f"タブレットはディスプレイが体験の中心になる。動画視聴・読書・絵を描くいずれの用途でもパネル品質が快適さを左右。"
           f"OLEDと液晶の違いは暗い部屋でのコントラストや黒の締まり方に顕著に現れる。"
           if ja else
           f"The {a} features a {asp[0]} {asp[1]} display. The {b} uses a {bsp[0]} {bsp[1]}. "
           f"The display is the center of the tablet experience. For video, reading, or drawing, panel quality determines comfort. "
           f"OLED vs LCD differences are most visible in dark room contrast and black levels."),

          ("パフォーマンス" if ja else "Performance",
           f"{a}は{asp[2]}チップに{asp[3]}RAMを搭載。{b}は{bsp[2]}と{bsp[3]}RAM。"
           f"タブレットでの重い作業といえば動画編集・イラスト・マルチタスク。"
           f"プロ用途なら上位チップの恩恵が大きいが、日常的な用途ではどちらも快適に使える。"
           if ja else
           f"The {a} runs on {asp[2]} with {asp[3]} RAM. The {b} uses {bsp[2]} and {bsp[3]} RAM. "
           f"Heavy tablet tasks include video editing, illustration, and multitasking. "
           f"Pro use cases benefit from the higher-end chip, but both handle everyday use effortlessly."),

          ("OS・ソフトウェア体験" if ja else "OS & Software Experience",
           f"{a}は{asp[10]}で動作し、豊富なタブレット最適化アプリが利用可能。"
           f"{b}は{bsp[10]}を搭載。両者のOSは哲学が異なり、App Store vs Google Playのアプリ環境の差も大きい。"
           f"すでに所有するスマートフォンと同じエコシステムを選ぶとシームレスな連携が得られる。"
           if ja else
           f"The {a} runs {asp[10]} with a strong library of tablet-optimized apps. The {b} uses {bsp[10]}. "
           f"The OS philosophies differ significantly, as does the App Store vs Google Play ecosystem. "
           f"Choosing the same ecosystem as your smartphone delivers the most seamless experience."),

          ("価格・コストパフォーマンス" if ja else "Value & Price",
           f"{a}は{asp[11]}から。{b}は{bsp[11]}から。"
           f"タブレットは用途が限られるユーザーも多いため、コスパの観点は重要。"
           f"プロ向けの最高スペックが必要かどうかをよく検討した上で、予算に合ったモデルを選ぼう。"
           if ja else
           f"The {a} starts at {asp[12]}. The {b} starts from {bsp[12]}. "
           f"Since many tablet users have specific use cases, value for money matters greatly. "
           f"Carefully assess whether you truly need top-end pro specs before spending the premium."),
        ]

    if cat == "イヤホン":
        return [
          ("デザイン・装着感" if ja else "Design & Fit",
           f"{a}は{asp[8]}の軽量設計で長時間装着でも疲れにくい構造。{b}は{bsp[8]}。"
           f"イヤホンの快適さは耳の形状との相性が大きく、同じ人でもイヤーピースのサイズや素材で印象が変わる。"
           f"可能であれば実機試着が最も確実な選択方法だ。"
           if ja else
           f"The {a} weighs {asp[8]} per earbud for extended comfort. The {b} weighs {bsp[8]}. "
           f"Earphone comfort depends heavily on ear shape compatibility. Even the same person may prefer different tip sizes or materials. "
           f"If possible, try them on in person before buying."),

          ("音質" if ja else "Sound Quality",
           f"{a}はコーデック{asp[5]}対応で、ハイレゾ音源の再生にも対応。{b}は{bsp[5]}をサポート。"
           f"音の好みは主観的だが、LDACやaptX Adaptive対応モデルはより多くの音楽情報を伝送できる。"
           f"普段使いのストリーミングサービスがハイレゾ対応かどうかも確認しておこう。"
           if ja else
           f"The {a} supports {asp[5]} codecs, including hi-res audio formats. The {b} supports {bsp[5]}. "
           f"Sound preference is subjective, but LDAC and aptX Adaptive transmit more audio data for better quality. "
           f"Check if your streaming service supports hi-res audio before prioritizing codec support."),

          ("ノイズキャンセリング (ANC)" if ja else "Active Noise Cancellation",
           f"両機種ともANCを搭載しており、騒がしい環境での集中を助ける。"
           f"{a}のANCはハイエンドクラスで、{b}も高い水準のNCを誇る。"
           f"電車・飛行機・カフェなどでの主な利用用途ならANC性能は重要な選択基準のひとつ。"
           if ja else
           f"Both models feature ANC for focus in noisy environments. "
           f"The {a} delivers high-end ANC performance; the {b} also offers strong noise cancellation. "
           f"If you mainly use earphones on trains, planes, or in cafes, ANC quality is a key criterion."),

          ("バッテリー持続時間" if ja else "Battery Life",
           f"{a}は本体{asp[7]}、ケース込みで{asp[6]}の連続使用が可能。{b}は本体{bsp[7]}・合計{bsp[6]}。"
           f"通勤・出張・旅行での使用頻度が高い場合はケース込みのバッテリー容量が重要。"
           f"ケースを持ち歩く習慣があれば、本体単体のバッテリーは3〜4時間でも十分なケースも多い。"
           if ja else
           f"The {a} lasts {asp[7]} per charge, totaling {asp[6]} with the case. The {b}: {bsp[7]} per charge, {bsp[6]} total. "
           f"For commuters and travelers, total case battery capacity matters most. "
           f"If you always carry the case, 3-4 hours per earbud charge is often sufficient."),
        ]

    if cat == "スピーカー":
        return [
          ("デザイン・ポータビリティ" if ja else "Design & Portability",
           f"{a}は{asp[8]}のコンパクト設計で持ち運びに優れる。{b}は{bsp[8]}。"
           f"アウトドアや旅行での持ち運びを想定するなら重量とサイズが重要。"
           f"家での据え置き用途ならより大型のモデルが音量・音質で優れることが多い。"
           if ja else
           f"The {a} weighs {asp[8]} for easy portability. The {b} weighs {bsp[8]}. "
           f"For outdoor and travel use, weight and size are paramount. "
           f"For home use, larger models typically deliver better volume and sound quality."),

          ("音質・音量" if ja else "Sound Quality & Volume",
           f"{a}のドライバー構成は{asp[1]}。{b}は{bsp[1]}を搭載。"
           f"ドライバーのサイズと配置が低音の量感と全体の音圧に直結する。"
           f"実際の音量と音質はスペック表だけでは判断しにくいため、試聴できる機会を積極的に活用しよう。"
           if ja else
           f"The {a} uses {asp[1]} driver configuration. The {b} features {bsp[1]}. "
           f"Driver size and layout directly affect bass depth and overall volume. "
           f"Sound quality is hard to judge from specs alone — seek out a listening demo if possible."),

          ("防水・耐久性" if ja else "Water Resistance & Durability",
           f"{a}は{asp[9]}防水に対応しアウトドア使用も安心。{b}は{bsp[9]}。"
           f"プールサイドや海辺での使用や急な雨を考慮するなら防水規格の確認は必須。"
           f"IPX7以上なら水没テストもクリアしており、アウトドア用途でも頼りになる。"
           if ja else
           f"The {a} offers {asp[9]} water protection for outdoor confidence. The {b} provides {bsp[9]}. "
           f"If you use speakers near pools, beaches, or in rain, check IP ratings carefully. "
           f"IPX7 or above means the speaker can withstand full submersion."),

          ("バッテリー・接続性" if ja else "Battery & Connectivity",
           f"{a}は最大{asp[6]}の連続再生が可能。{b}は{bsp[6]}を実現。"
           f"屋外での長時間使用にはバッテリー持ちが決め手になる。"
           f"Bluetooth接続の安定性やペアリングのしやすさも日常使いでは重要なポイントだ。"
           if ja else
           f"The {a} delivers up to {asp[6]} of playback. The {b} achieves {bsp[6]}. "
           f"Battery life is decisive for long outdoor sessions. "
           f"Bluetooth stability and ease of pairing also matter greatly in everyday use."),
        ]

    if cat in ("カメラ","アクションカム","360°カメラ"):
        return [
          ("デザイン・操作性" if ja else "Design & Usability",
           f"{a}は{asp[8]}で{asp[0]}タイプ。{b}は{bsp[8]}の{bsp[0]}。"
           f"カメラの重量とグリップは長時間撮影の疲労に直接影響する。"
           f"フィールドワークや旅行での使用頻度が高い場合、軽量・コンパクトな設計が大きなアドバンテージになる。"
           if ja else
           f"The {a} weighs {asp[8]} as a {asp[0]}. The {b} is a {bsp[0]} at {bsp[8]}. "
           f"Camera weight and grip directly affect fatigue during long shoots. "
           f"For travel and fieldwork, a compact lightweight design is a major advantage."),

          ("画質・映像品質" if ja else "Image & Video Quality",
           f"{a}は{asp[1]}センサーで{asp[5]}の撮影が可能。{b}は{bsp[1]}センサーと{bsp[5]}に対応。"
           f"センサーサイズが大きいほど暗所でのノイズ耐性が高く、ダイナミックレンジも広がる傾向にある。"
           f"解像度だけでなく動画のフレームレートや手ブレ補正性能も総合的に判断しよう。"
           if ja else
           f"The {a} uses a {asp[1]} sensor with {asp[5]} capability. The {b} has {bsp[1]} and supports {bsp[5]}. "
           f"Larger sensors generally mean better low-light performance and dynamic range. "
           f"Consider resolution, frame rates, and stabilization together, not just megapixels."),

          ("バッテリー・電源" if ja else "Battery & Power",
           f"{a}のバッテリー持続時間は{asp[6]}。{b}は{bsp[6]}を実現する。"
           f"アクション系カメラではバッテリー交換のしやすさも重要なポイント。"
           f"予備バッテリーや充電方法(USB-C給電)の有無は長時間撮影時の信頼性に直結する。"
           if ja else
           f"The {a} lasts {asp[6]} on a charge. The {b} achieves {bsp[6]}. "
           f"For action cameras, ease of battery swapping is also critical. "
           f"Spare battery availability and USB-C charging support determine reliability on long shoots."),

          ("防水・耐環境性" if ja else "Water & Environmental Resistance",
           f"{a}は{asp[9]}の防水性能を持つ。{b}は{bsp[9]}の耐水性を誇る。"
           f"アウトドア・スポーツ撮影では防水性能がカメラ選択の根幹になる。"
           f"防水ケース不要で水中撮影できるモデルなら、サーフィン・スノボ・ダイビングにも対応可能だ。"
           if ja else
           f"The {a} is rated {asp[9]}. The {b} offers {bsp[9]} protection. "
           f"For outdoor and sports shooting, water resistance is foundational to camera selection. "
           f"Waterproof-without-case models support surfing, snowboarding, and even diving."),
        ]

    if cat == "モニター":
        return [
          ("ディスプレイ品質" if ja else "Display Quality",
           f"{a}は{asp[0]}の{asp[1]}パネルを採用。{b}は{bsp[0]}の{bsp[1]}。"
           f"解像度・パネル種別・色域はモニター選択の核心。"
           f"OLEDは黒の締まりとコントラストが圧倒的だが、IPSは均一性と価格のバランスに優れることが多い。"
           if ja else
           f"The {a} uses a {asp[0]} {asp[1]} panel. The {b} features a {bsp[0]} {bsp[1]}. "
           f"Resolution, panel type, and color gamut are the core of monitor selection. "
           f"OLED offers unmatched black levels and contrast; IPS typically excels in uniformity and value."),

          ("リフレッシュレート・応答速度" if ja else "Refresh Rate & Response Time",
           f"{a}は{asp[6]}のリフレッシュレート・応答速度。{b}は{bsp[6]}を実現。"
           f"ゲーム用途ではリフレッシュレートが高いほど映像の滑らかさとレスポンスが向上する。"
           f"クリエイティブ用途では応答速度より色精度・均一性の方が重要になることが多い。"
           if ja else
           f"The {a} achieves {asp[6]}. The {b} delivers {bsp[6]}. "
           f"For gaming, higher refresh rates mean smoother visuals and better responsiveness. "
           f"For creative work, color accuracy and uniformity usually matter more than response time."),

          ("接続端子・利便性" if ja else "Connectivity & Convenience",
           f"{a}の接続端子構成は{asp[5]}。{b}は{bsp[5]}を備える。"
           f"USB-C給電対応モデルはノートPCを繋ぐだけで充電・映像出力が同時に可能で、デスク周りをすっきり保てる。"
           f"KVM切替や内蔵USBハブの有無も複数PC利用者には重要なポイント。"
           if ja else
           f"The {a} offers {asp[5]} connectivity. The {b} provides {bsp[5]}. "
           f"USB-C Power Delivery lets you connect a laptop for simultaneous charging and video — great for a clean desk setup. "
           f"Built-in USB hub and KVM switching matter to users with multiple PCs."),

          ("用途別おすすめ" if ja else "Best Use Cases",
           f"{a}は{asp[0]}・{asp[6]}の特性からゲーミング向きの傾向が強い。"
           f"{b}は{bsp[0]}・{bsp[6]}の特性からクリエイター向きと言える場面が多い。"
           f"ゲームと仕事を兼用する場合は両方の要件を満たせるか、優先順位を明確にして選択しよう。"
           if ja else
           f"The {a}'s {asp[0]} at {asp[6]} makes it particularly suited for gaming. "
           f"The {b}'s {bsp[0]} at {bsp[6]} lends itself to creative and professional work. "
           f"For gaming and work combined, identify your priority to find the right balance."),
        ]

    if cat == "ロボット掃除機":
        return [
          ("ナビゲーション・マッピング" if ja else "Navigation & Mapping",
           f"{a}の障害物認識は{asp[1]}方式を採用。{b}は{bsp[1]}を搭載。"
           f"LiDARと視覚AIの組み合わせが最も精度の高いマッピングを実現する。"
           f"家具の多い部屋や暗い場所での認識精度は、実際の掃除効率に大きく影響する。"
           if ja else
           f"The {a} uses {asp[1]} for obstacle detection. The {b} relies on {bsp[1]}. "
           f"LiDAR combined with visual AI delivers the most accurate mapping. "
           f"Recognition accuracy in cluttered rooms and low light significantly affects real cleaning efficiency."),

          ("吸引力・ブラシ性能" if ja else "Suction & Brush Performance",
           f"{a}のブラシ・吸引力は{asp[5]}。{b}は{bsp[5]}の性能を持つ。"
           f"ペットの毛・絨毯・硬い床など使用環境によって必要な吸引力は異なる。"
           f"ゴムブラシは絡まりにくく、ペットがいる家庭や毛が多い環境で特に威力を発揮する。"
           if ja else
           f"The {a} offers {asp[5]} brush and suction. The {b} delivers {bsp[5]}. "
           f"Required suction varies by environment: pet hair, carpet, and hard floors all have different demands. "
           f"Rubber brushes resist tangles — especially valuable in homes with pets or long hair."),

          ("水拭き(モップ)機能" if ja else "Mopping Performance",
           f"両機種とも水拭き機能を搭載しており、掃き掃除と同時に床を拭くことができる。"
           f"自動洗浄・乾燥ドック付きのモデルは衛生面で優れ、メンテナンスの手間を大幅に削減できる。"
           f"モップパッドの自動洗浄機能があると、ユーザーが手を触れる頻度が激減する。"
           if ja else
           f"Both models include mopping capability to vacuum and mop simultaneously. "
           f"Models with auto-wash and auto-dry docks are more hygienic and dramatically reduce maintenance effort. "
           f"Automatic mop pad cleaning means you rarely need to touch the mop yourself."),

          ("自動化・メンテナンス" if ja else "Automation & Maintenance",
           f"{a}のドック機能は{asp[7]}。{b}は{bsp[7]}を採用。"
           f"完全自動化を求めるなら、ゴミ収集・水補給・モップ洗浄・乾燥まで一括対応するドックが理想。"
           f"購入後のランニングコスト(消耗品交換費)も選択時に確認しておこう。"
           if ja else
           f"The {a}'s dock offers {asp[7]}. The {b} provides {bsp[7]}. "
           f"For maximum automation, look for docks that handle emptying, refilling, washing, and drying. "
           f"Check ongoing costs for consumables (dust bags, mop pads) when comparing total ownership cost."),
        ]

    if cat == "ゲーム機":
        return [
          ("ハードウェア性能" if ja else "Hardware Performance",
           f"{a}は{asp[2]}チップに{asp[3]}RAMを搭載し、{asp[1]}の映像出力に対応。"
           f"{b}は{bsp[2]}と{bsp[3]}RAMで{bsp[1]}出力が可能。"
           f"現世代のゲーム機はいずれも4K・60fps以上のゲームプレイを実現しており、圧倒的な性能差はほぼない。"
           if ja else
           f"The {a} uses {asp[2]} with {asp[3]} RAM, supporting {asp[1]} output. "
           f"The {b} runs {bsp[2]} and {bsp[3]} RAM for {bsp[1]} output. "
           f"Current-gen consoles all deliver 4K/60fps+ gameplay — there's no overwhelming hardware gap."),

          ("ゲームライブラリ" if ja else "Game Library",
           f"{a}と{b}ではゲームライブラリの方向性が大きく異なる。"
           f"任天堂タイトル・PlayStation独占・Xbox Game Pass など、好みのタイトルがどのプラットフォームにあるかを最優先に考えよう。"
           f"クロスプラットフォーム対応タイトルが増えているが、独占タイトルは今でも強力な差別化要因だ。"
           if ja else
           f"The {a} and {b} have vastly different game library orientations. "
           f"Nintendo exclusives, PlayStation exclusives, and Xbox Game Pass — prioritize the platform with your favorite titles. "
           f"Cross-platform games are growing, but exclusives remain a powerful differentiator."),

          ("携帯性・プレイスタイル" if ja else "Portability & Play Style",
           f"{a}は{asp[8]}で持ち運び可能。{b}は{bsp[8]}の据え置き型。"
           f"外出先・旅行・通勤でのプレイを重視するか、自宅の大画面TVでのプレイを重視するかが選択の軸になる。"
           f"携帯・据え置き両方の使い方ができるハイブリッド機という選択肢も考慮に値する。"
           if ja else
           f"The {a} weighs {asp[8]} for portability. The {b} is a {bsp[8]} home console. "
           f"The key choice is between gaming on the go vs. playing on a big home TV. "
           f"A hybrid console that supports both modes is also worth considering."),

          ("コスト・サブスクリプション" if ja else "Cost & Subscriptions",
           f"{a}は{asp[11]}から購入可能。{b}は{bsp[11]}。"
           f"本体価格に加え、オンラインプレイに必要なサブスクリプション費用も試算しておこう。"
           f"Game Passのような月額制ゲームサービスを重視するか、ソフト買い切りを好むかも選択基準のひとつだ。"
           if ja else
           f"The {a} starts at {asp[12]}. The {b} is priced at {bsp[12]}. "
           f"Factor in subscription costs for online gaming beyond the console price. "
           f"Consider whether you prefer a monthly game service like Game Pass or buying games outright."),
        ]

    # Fallback
    return [
      ("特徴比較" if ja else "Key Features",
       f"{a}と{b}を徹底比較。主なスペックや使い勝手の違いを解説する。"
       if ja else
       f"In-depth comparison of {a} vs {b}. We break down the key spec and usability differences."),
      ("選び方ガイド" if ja else "How to Choose",
       f"どちらを選ぶかは用途・予算・エコシステムへの親和性で決まる。"
       if ja else
       f"The right choice depends on use case, budget, and ecosystem affinity."),
    ]

# ── CSS ───────────────────────────────────────────────────────────────────────
BASE_CSS = """  <style>
    .cmp{max-width:900px;margin:0 auto;padding:40px 20px 80px}
    .bc{font-size:.8rem;color:var(--text-light);margin-bottom:24px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
    .bc a{color:var(--primary)}
    .hero{border-radius:var(--radius);padding:40px 32px;margin-bottom:32px;color:#fff;text-align:center}
    .badge{display:inline-block;background:rgba(255,255,255,.15);color:rgba(255,255,255,.9);font-size:.72rem;font-weight:700;letter-spacing:.14em;padding:4px 14px;border-radius:20px;margin-bottom:14px}
    .hero h1{font-size:clamp(1.2rem,3vw,1.8rem);font-weight:900;line-height:1.4;margin-bottom:10px}
    .hero .sub{font-size:.85rem;color:rgba(255,255,255,.7)}
    .vrd{background:linear-gradient(135deg,#fff8f0,#fff3e0);border:2px solid var(--primary);border-radius:var(--radius);padding:20px 24px;margin-bottom:32px}
    .vrd .vl{font-size:.78rem;font-weight:700;color:var(--primary);text-transform:uppercase;letter-spacing:.1em;margin-bottom:8px}
    .vrd p{font-size:1rem;font-weight:700;color:#222;line-height:1.6;margin:0}
    .sc{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:center;background:var(--secondary);border-radius:var(--radius);padding:28px;margin-bottom:32px}
    .sc-card{background:rgba(255,255,255,.07);border-radius:var(--radius-sm);padding:20px 16px;text-align:center;color:#fff}
    .sc-card .pn{font-size:.88rem;font-weight:700;margin-bottom:6px;color:rgba(255,255,255,.8)}
    .sc-card .pp{font-size:1rem;font-weight:900;color:var(--accent);margin-bottom:10px}
    .sc-card .sn{font-size:3.2rem;font-weight:900;color:var(--accent);line-height:1}
    .sc-card .sm{font-size:.8rem;color:rgba(255,255,255,.5)}
    .sc-card .sb{background:rgba(255,255,255,.1);border-radius:10px;height:8px;overflow:hidden;margin-top:10px}
    .sc-card .sbf{height:100%;border-radius:10px;background:var(--accent)}
    .vs{font-size:1.4rem;font-weight:900;color:#fff;background:var(--primary);width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0}
    /* spec table */
    .spec-wrap{margin-bottom:32px}
    .spec-wrap h2{font-size:1.05rem;font-weight:800;color:#222;margin-bottom:12px}
    .spec-table{width:100%;border-collapse:collapse;font-size:.84rem}
    .spec-table th,.spec-table td{padding:10px 14px;border:1px solid var(--border);text-align:left;vertical-align:top}
    .spec-table thead th{background:var(--secondary);color:#fff;font-weight:700}
    .spec-table thead th:first-child{width:32%}
    .spec-table tbody tr:nth-child(even){background:#f9f9f9}
    .spec-table td:first-child{font-weight:700;color:#555;font-size:.8rem}
    /* article sections */
    .art-sec{margin-bottom:28px}
    .art-sec h2{font-size:1.05rem;font-weight:800;color:#222;border-left:4px solid var(--primary);padding-left:12px;margin-bottom:12px}
    .art-sec p{font-size:.9rem;line-height:1.85;color:#444;margin:0}
    /* pros/cons */
    .pc-wrap{margin-bottom:32px}
    .pc-wrap h2{font-size:1.05rem;font-weight:800;color:#222;margin-bottom:12px}
    .pc-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
    .pc-box{border-radius:var(--radius-sm);padding:16px}
    .pc-box.pros{background:#f0fdf4;border:1.5px solid #4ade80}
    .pc-box.cons{background:#fef2f2;border:1.5px solid #f87171}
    .pc-box h3{font-size:.82rem;font-weight:800;margin-bottom:8px}
    .pc-box.pros h3{color:#16a34a}
    .pc-box.cons h3{color:#dc2626}
    .pc-box ul{margin:0;padding-left:18px}
    .pc-box ul li{font-size:.84rem;line-height:1.7;color:#333}
    /* who should buy */
    .who-wrap{margin-bottom:32px}
    .who-wrap h2{font-size:1.05rem;font-weight:800;color:#222;margin-bottom:12px}
    .who-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
    .who-card{background:var(--secondary);color:#fff;border-radius:var(--radius-sm);padding:18px 16px}
    .who-card h3{font-size:.88rem;font-weight:800;color:var(--accent);margin-bottom:8px}
    .who-card p{font-size:.84rem;line-height:1.7;color:rgba(255,255,255,.85);margin:0}
    /* summary */
    .smry{background:var(--secondary);color:#fff;border-radius:var(--radius);padding:28px 32px;margin-bottom:32px}
    .smry h2{font-size:1.1rem;font-weight:800;margin-bottom:16px;color:var(--accent)}
    .smry p{font-size:.9rem;line-height:1.85;color:rgba(255,255,255,.85);margin:0}
    /* buy */
    .buy{background:#fff8f0;border:2px solid var(--primary);border-radius:var(--radius);padding:24px;margin-bottom:32px}
    .buy h3{font-size:1rem;font-weight:800;margin-bottom:16px;color:#222;text-align:center}
    .buy-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
    .buy-item{text-align:center}
    .buy-name{font-size:.85rem;font-weight:700;margin-bottom:10px;color:#333}
    .buy-btns{display:flex;flex-direction:column;gap:8px}
    .btn-amz{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:#ff9900;color:#111;padding:10px 18px;border-radius:50px;font-weight:800;font-size:.85rem;text-decoration:none}
    .btn-rkt{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:#bf0000;color:#fff;padding:10px 18px;border-radius:50px;font-weight:800;font-size:.85rem;text-decoration:none}
    .btn-rev{display:inline-flex;align-items:center;justify-content:center;gap:6px;background:var(--secondary);color:#fff;padding:10px 18px;border-radius:50px;font-weight:700;font-size:.85rem;text-decoration:none}
    @media(max-width:768px){
      .cmp{padding:20px 14px 60px}.hero{padding:28px 16px}
      .sc{grid-template-columns:1fr;gap:12px;padding:20px 14px}.vs{margin:0 auto}
      .pc-grid,.who-grid,.buy-grid{grid-template-columns:1fr}
      .spec-table{font-size:.78rem}
    }
  </style>"""

def spec_table_html(c, lang):
    a_name, b_name = c["a"]["name"], c["b"]["name"]
    cat = c["cat"]
    labels = CAT_SPEC_LABELS.get(cat, [])
    a_sp = SP.get(a_name, ["−"]*13)
    b_sp = SP.get(b_name, ["−"]*13)
    is_en = (lang == "en")
    h2 = "スペック比較" if not is_en else "Spec Comparison"
    th_label = "項目" if not is_en else "Spec"
    rows = ""
    for lbl_ja, lbl_en, idx in labels:
        lbl = lbl_en if is_en else lbl_ja
        va = a_sp[idx] if idx < len(a_sp) else "−"
        vb = b_sp[idx] if idx < len(b_sp) else "−"
        # price: use en price for en pages
        if (lbl_en == "Price") and is_en:
            va = a_sp[12] if len(a_sp) > 12 else a_sp[11]
            vb = b_sp[12] if len(b_sp) > 12 else b_sp[11]
        rows += f"<tr><td>{lbl}</td><td>{va}</td><td>{vb}</td></tr>\n"
    return f"""<div class="spec-wrap">
  <h2>📊 {h2}</h2>
  <table class="spec-table">
    <thead><tr><th>{th_label}</th><th>{a_name}</th><th>{b_name}</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>"""

def article_secs_html(c, lang):
    sections = secs(c, lang)
    html = ""
    for title, body in sections:
        paras = "".join(f"<p>{p.strip()}</p>" for p in body.split("\n") if p.strip())
        html += f'<div class="art-sec"><h2>{title}</h2>{paras}</div>\n'
    return html

def proscons_html(c, lang):
    a_name, b_name = c["a"]["name"], c["b"]["name"]
    is_en = (lang == "en")
    pa = c.get("pa_en" if is_en else "pa", [])
    ca = c.get("ca_en" if is_en else "ca", [])
    pb = c.get("pb_en" if is_en else "pb", [])
    cb = c.get("cb_en" if is_en else "cb", [])
    h2   = "メリット・デメリット" if not is_en else "Pros & Cons"
    pros = "メリット" if not is_en else "Pros"
    cons = "デメリット" if not is_en else "Cons"
    def li(items): return "".join(f"<li>{i}</li>" for i in items)
    return f"""<div class="pc-wrap">
  <h2>✅ {h2}</h2>
  <h3 style="font-size:.9rem;margin:0 0 8px;color:#333">{a_name}</h3>
  <div class="pc-grid" style="margin-bottom:16px">
    <div class="pc-box pros"><h3>👍 {pros}</h3><ul>{li(pa)}</ul></div>
    <div class="pc-box cons"><h3>👎 {cons}</h3><ul>{li(ca)}</ul></div>
  </div>
  <h3 style="font-size:.9rem;margin:0 0 8px;color:#333">{b_name}</h3>
  <div class="pc-grid">
    <div class="pc-box pros"><h3>👍 {pros}</h3><ul>{li(pb)}</ul></div>
    <div class="pc-box cons"><h3>👎 {cons}</h3><ul>{li(cb)}</ul></div>
  </div>
</div>"""

def whobuy_html(c, lang):
    a_name, b_name = c["a"]["name"], c["b"]["name"]
    is_en = (lang == "en")
    wa = c.get("wa_en" if is_en else "wa", "")
    wb = c.get("wb_en" if is_en else "wb", "")
    h2   = "こんな人におすすめ" if not is_en else "Who Should Buy"
    return f"""<div class="who-wrap">
  <h2>🎯 {h2}</h2>
  <div class="who-grid">
    <div class="who-card"><h3>{a_name}</h3><p>{wa}</p></div>
    <div class="who-card"><h3>{b_name}</h3><p>{wb}</p></div>
  </div>
</div>"""

def gen_page(c, lang="ja"):
    a, b = c["a"], c["b"]
    is_en = (lang == "en")
    bg1, bg2 = c["bg"].split(",")
    sba = int(a["score"] / 5 * 100)
    sbb = int(b["score"] / 5 * 100)
    amz_a = f"https://www.amazon.co.jp/s?k={quote_plus(a['name'])}"
    amz_b = f"https://www.amazon.co.jp/s?k={quote_plus(b['name'])}"
    rkt_a = f"https://search.rakuten.co.jp/search/mall/{quote_plus(a['name'])}/"
    rkt_b = f"https://search.rakuten.co.jp/search/mall/{quote_plus(b['name'])}/"
    cat_page = CAT_SLUG.get(c["cat"], "index.html")

    if is_en:
        html_lang,title  = "en", f"{a['name']} vs {b['name']} Comparison 2026 | GadgetNavi"
        desc             = f"Detailed {a['name']} vs {b['name']} comparison. Specs, pros, cons, and which one to buy in 2026."
        sub              = "Which one should you buy? 2026 In-Depth Comparison"
        verdict_lbl, verdict = "Verdict", c["verdict_en"]
        summary_lbl, summary = "Summary", c["summary_en"]
        buy_lbl, back    = "Buy Now", "Back to Comparisons"
        logo             = '📱 Gadget<span class="logo-dot">Navi</span>'
        canon            = f'{SITE}en/{c["slug"]}.html'
        home, cat_href   = "/en/", f'/en/{cat_page}'
        home_lbl, cat_lbl= "Home", c["cat_en"]
        nav              = '<a href="/en/#ranking">Rankings</a><a href="/en/#reviews">Reviews</a><a href="/en/#compare">Compare</a><a href="/en/faq.html">FAQ</a>'
        lang_btns        = f'<a href="/{c["slug"]}.html" class="lang-btn" onclick="localStorage.setItem(\'gadgetnavi_lang\',\'ja\')">&#127471;&#127477; JA</a><span class="lang-btn active">&#127468;&#127463; EN</span>'
        rev_a, rev_b     = f'/en/{a["slug"]}.html', f'/en/{b["slug"]}.html'
        rev_lbl, back_href="Full Review", "/en/#compare"
        footer_txt       = "This site participates in affiliate programs. We may earn commissions from purchases through links."
        footer_copy      = "2026 GadgetNavi All Rights Reserved."
        footer_links     = '<a href="/en/privacy.html" style="color:rgba(255,255,255,.5)">Privacy Policy</a>'
        redir            = ""
        badge            = c["cat_en"].upper() + " COMPARISON"
        buy_btns_a       = f'<a href="{amz_a}" target="_blank" rel="nofollow noopener" class="btn-amz">Amazon</a><a href="{rev_a}" class="btn-rev">{rev_lbl}</a>'
        buy_btns_b       = f'<a href="{amz_b}" target="_blank" rel="nofollow noopener" class="btn-amz">Amazon</a><a href="{rev_b}" class="btn-rev">{rev_lbl}</a>'
    else:
        html_lang,title  = "ja", f"{a['name']} vs {b['name']} 徹底比較【2026年版】｜ガジェットナビ"
        desc             = f"{a['name']}と{b['name']}を徹底比較。スペック・メリデメ・どちらを買うべきかを詳しく解説。"
        sub              = "どちらを買うべき？2026年版 徹底比較"
        verdict_lbl, verdict = "結論", c["verdict_ja"]
        summary_lbl, summary = "総評", c["summary_ja"]
        buy_lbl, back    = "購入リンク", "比較記事一覧に戻る"
        logo             = '📱 ガジェット<span class="logo-dot">ナビ</span>'
        canon            = f'{SITE}{c["slug"]}.html'
        home, cat_href   = "/", f'/{cat_page}'
        home_lbl, cat_lbl= "トップ", c["cat"]
        nav              = '<a href="/#ranking">ランキング</a><a href="/#reviews">レビュー</a><a href="/#compare">比較</a><a href="/privacy.html">プライバシー</a>'
        lang_btns        = f'<span class="lang-btn active">&#127471;&#127477; JA</span><a href="/en/{c["slug"]}.html" class="lang-btn" onclick="localStorage.setItem(\'gadgetnavi_lang\',\'en\')">&#127468;&#127463; EN</a>'
        rev_a, rev_b     = f'/{a["slug"]}.html', f'/{b["slug"]}.html'
        rev_lbl, back_href="詳細レビュー", "/#compare"
        footer_txt       = "当サイトはアフィリエイトプログラムに参加しています。リンク経由での購入により手数料が発生する場合があります。"
        footer_copy      = "2026 ガジェットナビ All Rights Reserved."
        footer_links     = '<a href="/privacy.html" style="color:rgba(255,255,255,.5)">プライバシーポリシー</a>'
        redir            = REDIR + "\n"
        badge            = c["cat_en"] + " COMPARISON"
        buy_btns_a       = f'<a href="{amz_a}" target="_blank" rel="nofollow noopener" class="btn-amz">Amazon</a><a href="{rkt_a}" target="_blank" rel="nofollow noopener" class="btn-rkt">楽天</a><a href="{rev_a}" class="btn-rev">{rev_lbl}</a>'
        buy_btns_b       = f'<a href="{amz_b}" target="_blank" rel="nofollow noopener" class="btn-amz">Amazon</a><a href="{rkt_b}" target="_blank" rel="nofollow noopener" class="btn-rkt">楽天</a><a href="{rev_b}" class="btn-rev">{rev_lbl}</a>'

    alt = (f'  <link rel="alternate" hreflang="ja" href="{SITE}{c["slug"]}.html">\n'
           f'  <link rel="alternate" hreflang="en" href="{SITE}en/{c["slug"]}.html">\n'
           f'  <link rel="alternate" hreflang="x-default" href="{SITE}{c["slug"]}.html">')
    price_a = SP.get(a["name"], ["−"]*13)[12 if is_en else 11]
    price_b = SP.get(b["name"], ["−"]*13)[12 if is_en else 11]

    body_parts = [
        spec_table_html(c, lang),
        article_secs_html(c, lang),
        proscons_html(c, lang),
        whobuy_html(c, lang),
    ]
    body_html = "\n".join(body_parts)

    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
{redir}  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canon}">
{alt}
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{SITE}ogp-default.svg">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2054301472533985" crossorigin="anonymous"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-ERDKSGNEWS');</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800;900&display=swap" rel="stylesheet">
{BASE_CSS}
</head>
<body>
<header>
  <div class="header-inner">
    <a href="{home}" class="logo">{logo}</a>
    <nav id="main-nav">{nav}</nav>
    <div style="display:flex;align-items:center;gap:6px;">{lang_btns}</div>
  </div>
</header>
<main>
<div class="cmp">
  <div class="bc"><a href="{home}">{home_lbl}</a><span>›</span><a href="{cat_href}">{cat_lbl}</a><span>›</span><span>{a["name"]} vs {b["name"]}</span></div>
  <div class="hero" style="background:linear-gradient(135deg,{bg1},{bg2})">
    <div class="badge">{badge}</div>
    <div style="font-size:3rem;margin-bottom:10px">{c["emoji"]}</div>
    <h1>{a["name"]} vs {b["name"]}</h1>
    <p class="sub">{sub}</p>
  </div>
  <div class="vrd"><div class="vl">📋 {verdict_lbl}</div><p>{verdict}</p></div>
  <div class="sc">
    <div class="sc-card">
      <div class="pn">{a["name"]}</div>
      <div class="pp">{price_a}</div>
      <div class="sn">{a["score"]}</div><div class="sm">/ 5.0</div>
      <div class="sb"><div class="sbf" style="width:{sba}%"></div></div>
    </div>
    <div class="vs">VS</div>
    <div class="sc-card">
      <div class="pn">{b["name"]}</div>
      <div class="pp">{price_b}</div>
      <div class="sn">{b["score"]}</div><div class="sm">/ 5.0</div>
      <div class="sb"><div class="sbf" style="width:{sbb}%"></div></div>
    </div>
  </div>
{body_html}
  <div class="smry"><h2>📊 {summary_lbl}</h2><p>{summary}</p></div>
  <div class="buy">
    <h3>🛒 {buy_lbl}</h3>
    <div class="buy-grid">
      <div class="buy-item"><div class="buy-name">{a["name"]}</div><div class="buy-btns">{buy_btns_a}</div></div>
      <div class="buy-item"><div class="buy-name">{b["name"]}</div><div class="buy-btns">{buy_btns_b}</div></div>
    </div>
  </div>
  <a href="{back_href}" style="display:inline-flex;align-items:center;gap:6px;color:var(--primary);font-weight:700;font-size:.9rem;">← {back}</a>
</div>
</main>
<footer>
  <div class="footer-inner">
    <div class="footer-disclaimer">{footer_txt}</div>
    <div class="footer-bottom"><p>© {footer_copy}</p><p>{footer_links}</p></div>
  </div>
</footer>
</body>
</html>"""

# ── Imported at run time ──────────────────────────────────────────────────────
if __name__ == "__main__":
    from _v2_data import COMPARISONS
    count_ja = count_en = 0
    for c in COMPARISONS:
        slug = c["slug"]
        # JA
        (BASE / f"{slug}.html").write_text(gen_page(c, "ja"), encoding="utf-8")
        count_ja += 1
        # EN
        (EN / f"{slug}.html").write_text(gen_page(c, "en"), encoding="utf-8")
        count_en += 1
    print(f"Done: {count_ja} JA + {count_en} EN pages regenerated.")
