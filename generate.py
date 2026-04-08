import os, base64
from urllib.parse import quote_plus

OUTPUT_DIR = r"C:\Users\81804\OneDrive\デスクトップ\auto-affiliate-blog-main"
BASE_URL = "https://auto-affiliate-blog-mauve.vercel.app/"

PRODUCTS = [
    # スマートフォン
    {"slug":"review-iphone16promax","name":"iPhone 16 Pro Max 256GB","cat":"スマートフォン","emoji":"📱","price":"¥194,800","score":4.9,"bg":"#1a1a2e,#16213e","scores":[("カメラ",98,4.9),("パフォーマンス",100,5.0),("バッテリー",90,4.5),("デザイン",96,4.8),("コスパ",76,3.8)],"specs":[("ディスプレイ","6.9インチ Super Retina XDR 120Hz"),("チップ","A18 Pro（3nm）"),("カメラ","48MP+48MP+5倍光学ズーム"),("バッテリー","4,685mAh 最大33時間"),("重量","227g"),("防水","IP68")],"pros":["カメラが全シーンで最強","A18 Proで動作が完璧","バッテリーが1日余裕","チタン素材で高級感","ProRes動画が撮れる"],"cons":["価格が20万円近い","充電速度がAndroidに劣る","227gとやや重い","USB-C 3.0移行が遅い"],"desc":"iPhone史上最高傑作。カメラ・パフォーマンス・バッテリーすべてが最高水準。価格は高いが長期利用なら納得できる投資。","related":[("review-pixel9pro","🤖","スマートフォン","Google Pixel 9 Pro レビュー",4.7),("review-galaxy-s25","📱","スマートフォン","Samsung Galaxy S25 レビュー",4.6),("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8)]},
    {"slug":"review-iphone16plus","name":"iPhone 16 Plus 128GB","cat":"スマートフォン","emoji":"📱","price":"¥124,800","score":4.5,"bg":"#1c1c1e,#2c2c2e","scores":[("カメラ",86,4.3),("パフォーマンス",92,4.6),("バッテリー",96,4.8),("デザイン",90,4.5),("コスパ",84,4.2)],"specs":[("ディスプレイ","6.7インチ Super Retina XDR 60Hz"),("チップ","A18（3nm）"),("カメラ","48MP+12MP超広角"),("バッテリー","最大26時間ビデオ再生"),("重量","223g"),("防水","IP68")],"pros":["バッテリーが驚異的に長持ち","6.7型の大画面","A18チップで高速動作","カメラコントロール搭載","大手キャリアで買いやすい"],"cons":["ProMotion 120Hz非対応","望遠カメラなし","Proより重い","充電速度が遅め"],"desc":"大画面と長バッテリーが欲しいiPhoneユーザーへの最適解。Proの機能は要らないけど画面の大きさは欲しい方に。","related":[("review-iphone16promax","📱","スマートフォン","iPhone 16 Pro Max レビュー",4.9),("review-pixel9pro","🤖","スマートフォン","Google Pixel 9 Pro レビュー",4.7),("review-galaxy-s25","📱","スマートフォン","Samsung Galaxy S25 レビュー",4.6)]},
    {"slug":"review-iphone16","name":"iPhone 16 128GB","cat":"スマートフォン","emoji":"📱","price":"¥99,800","score":4.4,"bg":"#1a0533,#2e1065","scores":[("カメラ",84,4.2),("パフォーマンス",92,4.6),("バッテリー",84,4.2),("デザイン",88,4.4),("コスパ",88,4.4)],"specs":[("ディスプレイ","6.1インチ Super Retina XDR 60Hz"),("チップ","A18（3nm）"),("カメラ","48MP+12MP超広角"),("バッテリー","最大22時間ビデオ再生"),("重量","170g"),("防水","IP68")],"pros":["A18チップ搭載","カメラコントロールボタン","コンパクトで軽い170g","価格が最も手頃","アクションボタン搭載"],"cons":["60Hz止まり","望遠カメラなし","バッテリー容量やや少なめ","USB-C 2.0"],"desc":"標準iPhoneの完成形。10万円以内でA18チップとカメラコントロールを手に入れられる。","related":[("review-iphone16plus","📱","スマートフォン","iPhone 16 Plus レビュー",4.5),("review-iphone16promax","📱","スマートフォン","iPhone 16 Pro Max レビュー",4.9),("review-iphonese4","📱","スマートフォン","iPhone SE 第4世代 レビュー",4.3)]},
    {"slug":"review-iphonese4","name":"iPhone SE 第4世代 128GB","cat":"スマートフォン","emoji":"📱","price":"¥59,800","score":4.3,"bg":"#1c1917,#292524","scores":[("カメラ",78,3.9),("パフォーマンス",92,4.6),("バッテリー",76,3.8),("デザイン",82,4.1),("コスパ",96,4.8)],"specs":[("ディスプレイ","6.1インチ OLED 60Hz"),("チップ","A18（3nm）"),("カメラ","48MP シングルカメラ"),("バッテリー","最大18時間ビデオ再生"),("重量","167g"),("防水","IP68")],"pros":["6万円でA18チップ搭載","有機ELに刷新","Face ID対応","軽量コンパクト","初めてのiPhoneに最適"],"cons":["望遠・超広角カメラなし","バッテリーが少ない","60Hz止まり","Apple Intelligenceは一部制限"],"desc":"6万円台でA18チップと有機ELを実現した衝撃のコスパ機。初iPhoneや乗り換えの入門機として最適。","related":[("review-iphone16","📱","スマートフォン","iPhone 16 レビュー",4.4),("review-iphone16plus","📱","スマートフォン","iPhone 16 Plus レビュー",4.5),("review-pixel9a","🤖","スマートフォン","Google Pixel 9a レビュー",4.4)]},
    {"slug":"review-pixel9a","name":"Google Pixel 9a 128GB","cat":"スマートフォン","emoji":"🤖","price":"¥72,800","score":4.4,"bg":"#14532d,#166534","scores":[("カメラ",90,4.5),("AI機能",98,4.9),("バッテリー",86,4.3),("デザイン",82,4.1),("コスパ",96,4.8)],"specs":[("ディスプレイ","6.3インチ OLED 120Hz"),("チップ","Google Tensor G4"),("カメラ","64MP+13MP超広角"),("バッテリー","5,100mAh"),("重量","186g"),("防水","IP67")],"pros":["7万円台でPixelのAI機能フル搭載","夜景撮影が優秀","7年間OSサポート","軽量186g","コスパ最強クラス"],"cons":["発熱がやや気になる","望遠カメラなし","無線充電なし","ストレージ上限256GB"],"desc":"Pixelシリーズの最強コスパモデル。7万円台でGemini AIと優秀カメラを手に入れられる。","related":[("review-pixel9pro","🤖","スマートフォン","Google Pixel 9 Pro レビュー",4.7),("review-pixel8a","🤖","スマートフォン","Google Pixel 8a レビュー",4.3),("review-iphonese4","📱","スマートフォン","iPhone SE 第4世代 レビュー",4.3)]},
    {"slug":"review-pixel8a","name":"Google Pixel 8a 128GB","cat":"スマートフォン","emoji":"🤖","price":"¥62,800","score":4.3,"bg":"#1e3a5f,#2563eb","scores":[("カメラ",88,4.4),("AI機能",94,4.7),("バッテリー",84,4.2),("デザイン",80,4.0),("コスパ",94,4.7)],"specs":[("ディスプレイ","6.1インチ OLED 120Hz"),("チップ","Google Tensor G3"),("カメラ","64MP+13MP超広角"),("バッテリー","4,492mAh"),("重量","188g"),("防水","IP67")],"pros":["6万円台で高性能カメラ","AI写真編集機能が充実","7年間サポート","コンパクトサイズ","Googleの純粋なAndroid"],"cons":["Tensor G3は発熱あり","望遠カメラなし","充電速度が18W止まり"],"desc":"6万円台で手に入るPixelの実力は十分。AIカメラ機能と長期サポートで長く使える一台。","related":[("review-pixel9a","🤖","スマートフォン","Google Pixel 9a レビュー",4.4),("review-pixel9pro","🤖","スマートフォン","Google Pixel 9 Pro レビュー",4.7),("review-iphonese4","📱","スマートフォン","iPhone SE 第4世代 レビュー",4.3)]},
    {"slug":"review-xperia1vi","name":"Sony Xperia 1 VI 256GB","cat":"スマートフォン","emoji":"📱","price":"¥189,000","score":4.4,"bg":"#1e1b4b,#312e81","scores":[("カメラ",90,4.5),("パフォーマンス",88,4.4),("バッテリー",88,4.4),("ディスプレイ",96,4.8),("コスパ",72,3.6)],"specs":[("ディスプレイ","6.5インチ 有機EL 120Hz"),("チップ","Snapdragon 8 Gen 3"),("カメラ","52MP+12MP+12MP望遠"),("バッテリー","5,000mAh"),("重量","192g"),("防水","IP65/68")],"pros":["4K有機ELディスプレイが圧巻","光学ズームの描写が一眼並み","バッテリー大容量5000mAh","3.5mmイヤホンジャック健在","クリエイター向け動画機能充実"],"cons":["価格が19万円近く高い","アスペクト比が21:9で動画視聴向き","重さ192gとやや重い","国内専売で修理難"],"desc":"映像・音楽クリエイターのためのスマホ。Leica監修カメラと4K有機ELで圧倒的な映像体験。","related":[("review-iphone16promax","📱","スマートフォン","iPhone 16 Pro Max レビュー",4.9),("review-xiaomi14ultra","📱","スマートフォン","Xiaomi 14 Ultra レビュー",4.5),("review-pixel9pro","🤖","スマートフォン","Google Pixel 9 Pro レビュー",4.7)]},
    {"slug":"review-xiaomi14ultra","name":"Xiaomi 14 Ultra 512GB","cat":"スマートフォン","emoji":"📱","price":"¥199,800","score":4.5,"bg":"#7c2d12,#9a3412","scores":[("カメラ",98,4.9),("パフォーマンス",96,4.8),("バッテリー",90,4.5),("デザイン",90,4.5),("コスパ",82,4.1)],"specs":[("ディスプレイ","6.73インチ LTPO AMOLED 120Hz"),("チップ","Snapdragon 8 Gen 3"),("カメラ","50MP ライカ×4眼"),("バッテリー","5,000mAh 90W急速充電"),("重量","219g"),("防水","IP68")],"pros":["ライカ共同開発1インチセンサー","90W超急速充電","Leitzカメラアプリが本格的","写真画質がiPhoneを上回るシーンも","512GBストレージ標準搭載"],"cons":["20万円超の高価格","グローバル版は一部機能制限","重さ219g","日本のサポート体制が弱い"],"desc":"ライカと共同開発した1インチセンサーカメラが衝撃的。カメラ最重視なら世界最強クラスの一台。","related":[("review-iphone16promax","📱","スマートフォン","iPhone 16 Pro Max レビュー",4.9),("review-xperia1vi","📱","スマートフォン","Sony Xperia 1 VI レビュー",4.4),("review-pixel9pro","🤖","スマートフォン","Google Pixel 9 Pro レビュー",4.7)]},
    {"slug":"review-oppofindx8pro","name":"OPPO Find X8 Pro 512GB","cat":"スマートフォン","emoji":"📱","price":"¥159,800","score":4.3,"bg":"#0c4a6e,#075985","scores":[("カメラ",86,4.3),("パフォーマンス",88,4.4),("バッテリー",90,4.5),("防水性能",98,4.9),("コスパ",82,4.1)],"specs":[("ディスプレイ","6.78インチ AMOLED 120Hz"),("チップ","MediaTek Dimensity 9400"),("カメラ","50MP Hasselblad×4眼"),("バッテリー","5,910mAh 80W急速充電"),("重量","218g"),("防水","IP69K")],"pros":["IP69Kで潜水レベルの防水","Hasselblad監修カメラ","大容量5910mAhバッテリー","80W急速充電","独自の水中撮影モード搭載"],"cons":["国内認知度が低い","修理・サポートが不安","重さ218g","独自UIが使いにくい人も"],"desc":"IP69K防水と大容量バッテリーが魅力。アウトドア派・アクティブユーザーに刺さる唯一無二の一台。","related":[("review-xiaomi14ultra","📱","スマートフォン","Xiaomi 14 Ultra レビュー",4.5),("review-xperia1vi","📱","スマートフォン","Sony Xperia 1 VI レビュー",4.4),("review-oneplus13","📱","スマートフォン","OnePlus 13 レビュー",4.4)]},
    {"slug":"review-aquosr9","name":"SHARP AQUOS R9 256GB","cat":"スマートフォン","emoji":"📱","price":"¥138,600","score":4.2,"bg":"#134e4a,#0f766e","scores":[("ディスプレイ",96,4.8),("バッテリー",88,4.4),("カメラ",80,4.0),("パフォーマンス",82,4.1),("コスパ",76,3.8)],"specs":[("ディスプレイ","6.5インチ Pro IGZO OLED 240Hz"),("チップ","Snapdragon 8 Gen 3"),("カメラ","50MP+50MP超広角"),("バッテリー","5,000mAh"),("重量","189g"),("防水","IP68")],"pros":["Pro IGZO OLEDで省電力×高画質","240Hzの超滑らかスクロール","国産ブランドの安心感","サポートが日本語で充実","軽量189g"],"cons":["カメラ性能はiPhone・Pixelに劣る","価格の割にコスパ低め","グローバル展開なし","独自機能が少ない"],"desc":"日本製フラグシップの矜持。Pro IGZO OLEDと240Hzで日常の滑らかさは他の追随を許さない。","related":[("review-xperia1vi","📱","スマートフォン","Sony Xperia 1 VI レビュー",4.4),("review-iphone16promax","📱","スマートフォン","iPhone 16 Pro Max レビュー",4.9),("review-galaxy-s25","📱","スマートフォン","Samsung Galaxy S25 レビュー",4.6)]},
    {"slug":"review-oneplus13","name":"OnePlus 13 512GB","cat":"スマートフォン","emoji":"📱","price":"¥129,800","score":4.4,"bg":"#1e3a5f,#1e40af","scores":[("パフォーマンス",96,4.8),("バッテリー",94,4.7),("カメラ",84,4.2),("充電速度",100,5.0),("コスパ",88,4.4)],"specs":[("ディスプレイ","6.82インチ LTPO AMOLED 120Hz"),("チップ","Snapdragon 8 Elite"),("カメラ","50MP Hasselblad×3眼"),("バッテリー","6,000mAh 100W急速充電"),("重量","210g"),("防水","IP65")],"pros":["100W超急速充電で23分フル充電","6000mAh大容量バッテリー","Snapdragon 8 Elite搭載","価格が抑えられている","Hasselblad監修カメラ"],"cons":["望遠が3倍止まり","重さ210g","IP65で防水性はやや低め","日本でのサポートが限定的"],"desc":"充電速度100Wと6000mAhバッテリーが魅力。フラグシップ性能を手頃な価格で手に入れたい人に。","related":[("review-galaxy-s25","📱","スマートフォン","Samsung Galaxy S25 レビュー",4.6),("review-pixel9pro","🤖","スマートフォン","Google Pixel 9 Pro レビュー",4.7),("review-oppofindx8pro","📱","スマートフォン","OPPO Find X8 Pro レビュー",4.3)]},
    {"slug":"review-nothingphone3a","name":"Nothing Phone 3a 256GB","cat":"スマートフォン","emoji":"📱","price":"¥49,800","score":4.2,"bg":"#292524,#44403c","scores":[("デザイン",96,4.8),("コスパ",94,4.7),("カメラ",76,3.8),("パフォーマンス",78,3.9),("バッテリー",82,4.1)],"specs":[("ディスプレイ","6.77インチ AMOLED 120Hz"),("チップ","Snapdragon 7s Gen 3"),("カメラ","50MP+50MP超広角+2倍望遠"),("バッテリー","5,000mAh 45W急速充電"),("重量","201g"),("防水","IP54")],"pros":["Glyphインターフェースが唯一無二","5万円以下の破格コスパ","120Hz有機EL搭載","デザイン性が圧倒的に高い","軽快なピュアAndroid"],"cons":["チップがミドルレンジ","IP54で本格防水ではない","カメラ性能は価格相応","サポートが限定的"],"desc":"5万円以下で買える最もユニークなスマホ。Glyphインターフェースで他と差をつけたい人に。","related":[("review-galaxya55","📱","スマートフォン","Samsung Galaxy A55 レビュー",4.1),("review-pixel9a","🤖","スマートフォン","Google Pixel 9a レビュー",4.4),("review-motorolaedge50ultra","📱","スマートフォン","Motorola Edge 50 Ultra レビュー",4.3)]},
    {"slug":"review-galaxya55","name":"Samsung Galaxy A55 5G 256GB","cat":"スマートフォン","emoji":"📱","price":"¥59,800","score":4.1,"bg":"#0a3622,#14532d","scores":[("コスパ",88,4.4),("デザイン",82,4.1),("カメラ",78,3.9),("バッテリー",80,4.0),("パフォーマンス",76,3.8)],"specs":[("ディスプレイ","6.6インチ Super AMOLED 120Hz"),("チップ","Exynos 1480"),("カメラ","50MP+12MP超広角+5MP深度"),("バッテリー","5,000mAh 25W急速充電"),("重量","213g"),("防水","IP67")],"pros":["IP67防水で安心","光学手ぶれ補正付きカメラ","6万円以下でAMOLED搭載","5G対応","Samsung独自機能が充実"],"cons":["Exynos 1480はミドル性能","充電25W止まり","重さ213g","カメラ性能は価格相応"],"desc":"6万円以下で防水・光学手ぶれ補正・有機ELが揃う。コスパを最重視するAndroidユーザーに。","related":[("review-nothingphone3a","📱","スマートフォン","Nothing Phone 3a レビュー",4.2),("review-pixel9a","🤖","スマートフォン","Google Pixel 9a レビュー",4.4),("review-motorolaedge50ultra","📱","スマートフォン","Motorola Edge 50 Ultra レビュー",4.3)]},
    {"slug":"review-motorolaedge50ultra","name":"Motorola Edge 50 Ultra 512GB","cat":"スマートフォン","emoji":"📱","price":"¥89,800","score":4.3,"bg":"#312e81,#3730a3","scores":[("充電速度",100,5.0),("デザイン",88,4.4),("カメラ",82,4.1),("バッテリー",86,4.3),("コスパ",86,4.3)],"specs":[("ディスプレイ","6.7インチ pOLED 144Hz"),("チップ","Snapdragon 8s Gen 3"),("カメラ","50MP+50MP超広角+10MP望遠"),("バッテリー","4,500mAh 125W超急速充電"),("重量","197g"),("防水","IP68")],"pros":["125W超急速充電で2分で50%","144Hz pOLEDディスプレイ","IP68本格防水","9万円台のコスパ","無線充電50Wにも対応"],"cons":["Snapdragon 8s Gen 3はフラグシップより劣る","カメラはPixel・iPhoneに劣る","日本での普及率が低い"],"desc":"世界最速クラスの125W急速充電が最大の魅力。充電切れが怖い人への完璧な回答。","related":[("review-oneplus13","📱","スマートフォン","OnePlus 13 レビュー",4.4),("review-pixel9a","🤖","スマートフォン","Google Pixel 9a レビュー",4.4),("review-galaxya55","📱","スマートフォン","Samsung Galaxy A55 レビュー",4.1)]},
    {"slug":"review-galaxys25ultra","name":"Samsung Galaxy S25 Ultra 512GB","cat":"スマートフォン","emoji":"📱","price":"¥219,800","score":4.7,"bg":"#134e4a,#115e59","scores":[("カメラ",96,4.8),("S Pen",100,5.0),("パフォーマンス",98,4.9),("バッテリー",88,4.4),("コスパ",76,3.8)],"specs":[("ディスプレイ","6.9インチ Dynamic AMOLED 2X 120Hz"),("チップ","Snapdragon 8 Elite"),("カメラ","200MP+50MP+10MP+50MP望遠"),("バッテリー","5,000mAh 45W急速充電"),("重量","218g"),("防水","IP68")],"pros":["200MPカメラの圧倒的解像度","S Pen内蔵でメモ・イラスト制作","Snapdragon 8 Elite最高性能","Galaxy AI搭載","ビジネス用途で圧倒的生産性"],"cons":["22万円超の超高価格","重さ218g","S Penを使わないと価値半減","充電45Wは価格の割に遅め"],"desc":"S Pen内蔵×200MPカメラ×Snapdragon 8 Eliteの三冠王。スマホで仕事・創作を極めたい人の最終兵器。","related":[("review-galaxy-s25","📱","スマートフォン","Samsung Galaxy S25 レビュー",4.6),("review-iphone16promax","📱","スマートフォン","iPhone 16 Pro Max レビュー",4.9),("review-xiaomi14ultra","📱","スマートフォン","Xiaomi 14 Ultra レビュー",4.5)]},
    # ワイヤレスイヤホン
    {"slug":"review-sonywf1000xm5","name":"Sony WF-1000XM5","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥39,600","score":4.7,"bg":"#0c0a09,#1c1917","scores":[("ノイキャン",96,4.8),("音質",98,4.9),("装着感",88,4.4),("バッテリー",86,4.3),("コスパ",82,4.1)],"specs":[("ドライバー","8.4mm"),("ノイキャン","QN2e HDプロセッサー"),("再生時間","8時間（ANCオン）/36時間（ケース込）"),("防水","IPX4"),("コーデック","LDAC/AAC/SBC"),("接続","Bluetooth 5.3")],"pros":["音質が業界最高水準","LDAC対応でハイレゾ再生","ANC性能もトップクラス","小型化されて装着感向上","マルチポイント2台接続"],"cons":["AirPods Pro 2よりわずかにANCが劣る","Androidで真価を発揮（iOS制限あり）","4万円近い価格","前世代より小さくなったが人によって合わない"],"desc":"音質最重視のワイヤレスイヤホン最高峰。LDACハイレゾ再生対応でAndroidユーザーには最強の選択肢。","related":[("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8),("review-boseqcearbuds2","🎧","ワイヤレスイヤホン","Bose QC Earbuds II レビュー",4.6),("review-technicseahaz80","🎧","ワイヤレスイヤホン","Technics EAH-AZ80 レビュー",4.6)]},
    {"slug":"review-boseqcearbuds2","name":"Bose QuietComfort Earbuds II","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥38,500","score":4.6,"bg":"#1c1917,#292524","scores":[("ノイキャン",98,4.9),("装着感",98,4.9),("音質",86,4.3),("バッテリー",82,4.1),("コスパ",78,3.9)],"specs":[("ドライバー","独自Boseドライバー"),("ノイキャン","CustomTune個別最適化"),("再生時間","6時間（ANCオン）/24時間（ケース込）"),("防水","IPX4"),("コーデック","AAC/SBC"),("接続","Bluetooth 5.3")],"pros":["CustomTuneで個人最適化ANC","装着感が業界最高水準","フィット感が抜群で疲れない","外音取り込みも自然","通話品質が優秀"],"cons":["バッテリーが6時間と短め","音質はSonyに劣る","aptX非対応","4万円近い価格"],"desc":"装着感とノイキャン最優先ならBose一択。長時間の飛行機・通勤で真価を発揮する快適イヤホン。","related":[("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8),("review-sonywf1000xm5","🎧","ワイヤレスイヤホン","Sony WF-1000XM5 レビュー",4.7),("review-technicseahaz80","🎧","ワイヤレスイヤホン","Technics EAH-AZ80 レビュー",4.6)]},
    {"slug":"review-galaxybuds3pro","name":"Samsung Galaxy Buds 3 Pro","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥29,800","score":4.5,"bg":"#1a0533,#2e1065","scores":[("Galaxy連携",100,5.0),("ノイキャン",88,4.4),("音質",86,4.3),("装着感",86,4.3),("コスパ",84,4.2)],"specs":[("ドライバー","11mm+6.1mm2wayドライバー"),("ノイキャン","インテリジェントANC"),("再生時間","6時間（ANCオン）/30時間（ケース込）"),("防水","IPX7"),("コーデック","SSC/AAC/SBC"),("接続","Bluetooth 5.4")],"pros":["Galaxy AIとシームレス連携","Live Translateがリアルタイム翻訳","IPX7本格防水","3万円以下のコスパ","2Wayドライバーで音質良好"],"cons":["Galaxy以外では機能制限","aptX非対応","バッテリー6時間は短め"],"desc":"Galaxy/Androidユーザーには最高の選択肢。Galaxy AIとの連携機能が他社の追随を許さない。","related":[("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8),("review-sonywf1000xm5","🎧","ワイヤレスイヤホン","Sony WF-1000XM5 レビュー",4.7),("review-ankerliberty4nc","🎧","ワイヤレスイヤホン","Anker Soundcore Liberty 4 NC レビュー",4.3)]},
    {"slug":"review-technicseahaz80","name":"Technics EAH-AZ80","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥35,200","score":4.6,"bg":"#0f172a,#1e293b","scores":[("マルチポイント",100,5.0),("音質",92,4.6),("ノイキャン",86,4.3),("装着感",88,4.4),("コスパ",82,4.1)],"specs":[("ドライバー","10mm"),("ノイキャン","ハイブリッドANC"),("再生時間","7時間（ANCオン）/24時間（ケース込）"),("防水","IPX4"),("コーデック","LDAC/aptX/AAC/SBC"),("接続","マルチポイント3台同時")],"pros":["3台同時マルチポイント接続","LDAC対応ハイレゾ再生","テレワーカーに最適な設計","PCとスマホを自動切換え","音質がバランスよく優秀"],"cons":["ノイキャンはトップクラスに劣る","デザインが地味","価格3.5万円と高め"],"desc":"PC・スマホ・タブレット3台同時接続が可能なテレワーカー向け最強イヤホン。音質もLDAC対応で優秀。","related":[("review-sonywf1000xm5","🎧","ワイヤレスイヤホン","Sony WF-1000XM5 レビュー",4.7),("review-boseqcearbuds2","🎧","ワイヤレスイヤホン","Bose QC Earbuds II レビュー",4.6),("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8)]},
    {"slug":"review-ankerliberty4nc","name":"Anker Soundcore Liberty 4 NC","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥8,990","score":4.3,"bg":"#052e16,#14532d","scores":[("コスパ",100,5.0),("ノイキャン",76,3.8),("音質",76,3.8),("バッテリー",90,4.5),("装着感",82,4.1)],"specs":[("ドライバー","11mm"),("ノイキャン","ハイブリッドANC"),("再生時間","9時間（ANCオン）/50時間（ケース込）"),("防水","IPX4"),("コーデック","LDAC/AAC/SBC"),("接続","Bluetooth 5.3")],"pros":["9000円以下でANC搭載","LDACハイレゾ対応","50時間の超長バッテリー","コスパが圧倒的","ヒアリングテスト機能搭載"],"cons":["音質・ANCは価格相応","装着感は個人差あり","マルチポイント1台のみ"],"desc":"1万円以下でLDAC×ANC×50時間バッテリーを実現。コスパ最強イヤホンを探している方の答え。","related":[("review-nothingear2","🎧","ワイヤレスイヤホン","Nothing Ear 2 レビュー",4.3),("review-beatsstudiobudsplus","🎧","ワイヤレスイヤホン","Beats Studio Buds+ レビュー",4.2),("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8)]},
    {"slug":"review-jbltourpro3","name":"JBL Tour Pro 3","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥29,700","score":4.4,"bg":"#0c4a6e,#164e63","scores":[("スマートケース",100,5.0),("音質",86,4.3),("ノイキャン",84,4.2),("バッテリー",90,4.5),("コスパ",82,4.1)],"specs":[("ドライバー","10mm"),("ノイキャン","アダプティブANC"),("再生時間","10時間（ANCオン）/40時間（ケース込）"),("防水","IP55"),("コーデック","LC3/aptX/AAC/SBC"),("特徴","スマートケース1.45型タッチディスプレイ")],"pros":["ケースにタッチディスプレイ搭載","通知確認・音楽操作がケースで可能","10時間の長バッテリー","LC3次世代コーデック対応","デザインが洗練されている"],"cons":["スマートケースの実用性に疑問も","ANCはトップクラスに劣る","3万円の価格"],"desc":"ケース自体がスマートデバイスに変身する革新的イヤホン。ガジェット好きの所有欲を満たす一台。","related":[("review-sonywf1000xm5","🎧","ワイヤレスイヤホン","Sony WF-1000XM5 レビュー",4.7),("review-technicseahaz80","🎧","ワイヤレスイヤホン","Technics EAH-AZ80 レビュー",4.6),("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8)]},
    {"slug":"review-nothingear2","name":"Nothing Ear 2","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥19,800","score":4.3,"bg":"#1e1b4b,#312e81","scores":[("デザイン",96,4.8),("コスパ",88,4.4),("音質",82,4.1),("ノイキャン",76,3.8),("バッテリー",82,4.1)],"specs":[("ドライバー","11.6mm"),("ノイキャン","ハイブリッドANC"),("再生時間","6.3時間（ANCオン）/36時間（ケース込）"),("防水","IP54"),("コーデック","LHDC/AAC/SBC"),("特徴","透明デザイン")],"pros":["透明デザインが唯一無二","2万円以下でLHDC対応","11.6mm大ドライバー","デュアルコネクション対応","軽量4.5g"],"cons":["ANCは2万円クラスとしてやや弱め","IP54で本格防水でない","デザイン優先で機能は割り切り"],"desc":"2万円以下で手に入れられる最もスタイリッシュなイヤホン。見た目で選んでも音も十分満足できる。","related":[("review-ankerliberty4nc","🎧","ワイヤレスイヤホン","Anker Soundcore Liberty 4 NC レビュー",4.3),("review-beatsstudiobudsplus","🎧","ワイヤレスイヤホン","Beats Studio Buds+ レビュー",4.2),("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8)]},
    {"slug":"review-sennheisermomentum4","name":"Sennheiser MOMENTUM True Wireless 4","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥44,000","score":4.5,"bg":"#292524,#57534e","scores":[("音質",98,4.9),("ノイキャン",86,4.3),("装着感",88,4.4),("バッテリー",90,4.5),("コスパ",76,3.8)],"specs":[("ドライバー","7mm"),("ノイキャン","アダプティブANC"),("再生時間","7.5時間（ANCオン）/30時間（ケース込）"),("防水","IPX4"),("コーデック","aptX Adaptive/AAC/SBC"),("接続","Bluetooth 5.4")],"pros":["Hi-Fiオーディオ老舗の最高音質","aptX Adaptive対応で低遅延","7.5時間の長再生","Sennheiser Soundアプリが充実","高級感のある仕上げ"],"cons":["4.4万円の高価格","ANCはBose・Sonyに劣る","デザインが地味に感じる人も"],"desc":"音楽を本気で楽しみたいオーディオファンへ。Sennheiser渾身の音質は他社を圧倒する次元。","related":[("review-sonywf1000xm5","🎧","ワイヤレスイヤホン","Sony WF-1000XM5 レビュー",4.7),("review-boseqcearbuds2","🎧","ワイヤレスイヤホン","Bose QC Earbuds II レビュー",4.6),("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8)]},
    {"slug":"review-beatsstudiobudsplus","name":"Beats Studio Buds+","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥21,800","score":4.2,"bg":"#3f1f69,#4c1d95","scores":[("Apple/Android互換",96,4.8),("ノイキャン",80,4.0),("音質",78,3.9),("バッテリー",84,4.2),("コスパ",84,4.2)],"specs":[("ドライバー","独自デュアルエレメント"),("ノイキャン","アクティブノイズキャンセリング"),("再生時間","9時間（ANCオン）/36時間（ケース込）"),("防水","IPX4"),("コーデック","AAC/SBC"),("互換","iOS/Android両対応")],"pros":["iPhone・Android両方で最適化","9時間の長バッテリー","透明筐体のユニークデザイン","Apple/Google両ファインドマイ対応","2万円台のコスパ"],"cons":["ANCはAirPods Proに劣る","aptX非対応","音質はやや物足りない"],"desc":"iPhoneもAndroidも使うユーザーの最適解。どちらでも快適に使えるBeatsの強みが光る一台。","related":[("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8),("review-ankerliberty4nc","🎧","ワイヤレスイヤホン","Anker Soundcore Liberty 4 NC レビュー",4.3),("review-nothingear2","🎧","ワイヤレスイヤホン","Nothing Ear 2 レビュー",4.3)]},
    # スマートウォッチ
    {"slug":"review-applewatchs10","name":"Apple Watch Series 10（46mm）","cat":"スマートウォッチ","emoji":"⌚","price":"¥59,800","score":4.8,"bg":"#0f3460,#533483","scores":[("健康管理",98,4.9),("デザイン",96,4.8),("バッテリー",86,4.3),("Apple連携",100,5.0),("コスパ",82,4.1)],"specs":[("ディスプレイ","LTPO OLED Always-On"),("チップ","S10 SiP"),("バッテリー","最大18時間（通常）/36時間（省電力）"),("防水","WR50 耐水"),("センサー","心電図/血中酸素/皮膚温度/睡眠無呼吸"),("厚さ","9.7mm（歴代最薄）")],"pros":["歴代最薄9.7mm","睡眠時無呼吸症候群検知","ディスプレイが前世代比30%大型化","watchOSエコシステムが最強","Apple Payがスムーズ"],"cons":["Androidでは使えない","バッテリーが1日ギリギリ","価格が高い","充電ケーブルが独自規格"],"desc":"iPhoneユーザーのスマートウォッチはApple Watch一択。歴代最薄で日常装着のストレスが減った最高傑作。","related":[("review-applewatchultra2","⌚","スマートウォッチ","Apple Watch Ultra 2 レビュー",4.9),("review-galaxywatch7","⌚","スマートウォッチ","Samsung Galaxy Watch 7 レビュー",4.6),("review-garminfenix8","⌚","スマートウォッチ","Garmin Fenix 8 レビュー",4.7)]},
    {"slug":"review-galaxywatch7","name":"Samsung Galaxy Watch 7（44mm）","cat":"スマートウォッチ","emoji":"⌚","price":"¥44,800","score":4.6,"bg":"#1a0533,#3b0764","scores":[("健康管理",96,4.8),("Galaxy連携",98,4.9),("バッテリー",82,4.1),("デザイン",86,4.3),("コスパ",86,4.3)],"specs":[("ディスプレイ","Super AMOLED Always-On"),("チップ","Exynos W1000 3nm"),("バッテリー","最大40時間（省電力）"),("防水","IP68 / 5ATM"),("センサー","心電図/血圧/血糖値トレンド/体組成"),("OS","Wear OS 5")],"pros":["血糖値トレンド測定が革新的","3nmチップで省電力化","体組成測定（体脂肪率など）","Galaxyスマホと完全連動","価格が4.5万円台とリーズナブル"],"cons":["GalaxyスマホなしでAI機能制限","バッテリーは2日が限界","Googleアシスタント非搭載","デザインがシンプルすぎる"],"desc":"体組成測定と血糖値トレンドという唯一無二の健康機能が強み。Galaxyユーザーに最も深く刺さる一台。","related":[("review-applewatchs10","⌚","スマートウォッチ","Apple Watch Series 10 レビュー",4.8),("review-pixelwatch3","⌚","スマートウォッチ","Google Pixel Watch 3 レビュー",4.5),("review-amazfitgtr4","⌚","スマートウォッチ","Amazfit GTR 4 レビュー",4.1)]},
    {"slug":"review-garminfenix8","name":"Garmin Fenix 8（47mm）","cat":"スマートウォッチ","emoji":"⌚","price":"¥129,800","score":4.7,"bg":"#1c1917,#292524","scores":[("アウトドア性能",100,5.0),("バッテリー",98,4.9),("耐久性",98,4.9),("GPS精度",100,5.0),("コスパ",72,3.6)],"specs":[("ディスプレイ","AMOLED Always-On"),("チップ","独自アウトドアチップ"),("バッテリー","最大29日間（省電力）"),("防水","100m防水"),("センサー","マルチGNSS/心拍/高度/気圧/コンパス"),("特徴","ダイビングモード/スキーモード搭載")],"pros":["29日間の超長バッテリー","マルチGNSS対応で登山・ダイビング可","AMOLEDとアウトドア性能の両立","150以上のスポーツプロファイル","Wi-Fi/Bluetooth/ANT+対応"],"cons":["13万円の高価格","日常使いには多機能すぎる","重さ58g","スマホ通知などの日常機能は最低限"],"desc":"アウトドアアドベンチャーの最強パートナー。登山・トレラン・ダイビングまで制覇するガーミンの傑作。","related":[("review-applewatchultra2","⌚","スマートウォッチ","Apple Watch Ultra 2 レビュー",4.9),("review-garminvenu3","⌚","スマートウォッチ","Garmin Venu 3 レビュー",4.5),("review-withingsscanwatch2","⌚","スマートウォッチ","Withings ScanWatch 2 レビュー",4.4)]},
    {"slug":"review-pixelwatch3","name":"Google Pixel Watch 3（45mm）","cat":"スマートウォッチ","emoji":"⌚","price":"¥57,800","score":4.5,"bg":"#14532d,#166534","scores":[("Fitbit健康機能",96,4.8),("Google連携",94,4.7),("バッテリー",82,4.1),("デザイン",88,4.4),("コスパ",82,4.1)],"specs":[("ディスプレイ","AMOLED Always-On"),("チップ","Google Tensor G4"),("バッテリー","最大24時間（AODオン）/36時間（AODオフ）"),("防水","5ATM"),("センサー","心電図/心拍/血中酸素/皮膚電気活動"),("OS","Wear OS 4")],"pros":["Fitbitの健康アルゴリズムが最高","心拍異常リアルタイム検知","Google マップ/アシスタント完全対応","前世代比バッテリー20%向上","Googleフォト対応"],"cons":["AndroidでしかGoogleアシスタントフル活用できない","バッテリーは1日ギリギリ","ベゼルが太め","価格が6万円近い"],"desc":"FitbitとGoogleが融合した健康管理の最高峰。Pixel・Androidユーザーに最も深く刺さる一台。","related":[("review-applewatchs10","⌚","スマートウォッチ","Apple Watch Series 10 レビュー",4.8),("review-galaxywatch7","⌚","スマートウォッチ","Samsung Galaxy Watch 7 レビュー",4.6),("review-amazfitgtr4","⌚","スマートウォッチ","Amazfit GTR 4 レビュー",4.1)]},
    {"slug":"review-applewatchultra2","name":"Apple Watch Ultra 2（49mm）","cat":"スマートウォッチ","emoji":"⌚","price":"¥124,800","score":4.9,"bg":"#0c1445,#1e3a8a","scores":[("耐久性",100,5.0),("バッテリー",96,4.8),("GPS精度",100,5.0),("ディスプレイ",98,4.9),("コスパ",76,3.8)],"specs":[("ディスプレイ","3000nit LTPO OLED Always-On"),("チップ","S9 SiP"),("バッテリー","最大60時間（省電力）/36時間（通常）"),("防水","100m防水 / MIL-STD-810H"),("素材","チタニウム / サファイアガラス"),("特徴","デュアルGNSS / アクションボタン")],"pros":["3000nitの超高輝度ディスプレイ","60時間の超長バッテリー","100m防水×MIL規格の最高耐久性","2つのGNSS同時使用で精度最高","アクションボタンでワンタップ操作"],"cons":["12.5万円の超高価格","49mmの大きなケースは女性には大きい","重さ61g","デイリーユースには過剰スペック"],"desc":"アドベンチャーを本気でこなす人への最終回答。チタン×100m防水×60時間バッテリーで限界を超える。","related":[("review-applewatchs10","⌚","スマートウォッチ","Apple Watch Series 10 レビュー",4.8),("review-garminfenix8","⌚","スマートウォッチ","Garmin Fenix 8 レビュー",4.7),("review-garminvenu3","⌚","スマートウォッチ","Garmin Venu 3 レビュー",4.5)]},
    {"slug":"review-garminvenu3","name":"Garmin Venu 3（45mm）","cat":"スマートウォッチ","emoji":"⌚","price":"¥54,800","score":4.5,"bg":"#1e3a5f,#1e40af","scores":[("睡眠機能",96,4.8),("ライフスタイル",92,4.6),("バッテリー",86,4.3),("デザイン",88,4.4),("コスパ",84,4.2)],"specs":[("ディスプレイ","AMOLED Always-On"),("チップ","独自Garminチップ"),("バッテリー","最大14日間"),("防水","5ATM"),("センサー","心拍/血中酸素/ストレス/女性向け健康機能"),("特徴","スリープコーチング/車椅子モード")],"pros":["スリープコーチングが実践的","14日間バッテリーが魅力","AMOLEDで視認性抜群","車椅子使用者向けモードも搭載","Garminならではのスポーツ精度"],"cons":["アプリエコシステムはApple/Googleに劣る","スマートウォッチとしての通知機能が最低限","価格5.5万円はやや高め"],"desc":"スリープコーチングと14日バッテリーで生活習慣を改善。FenixのフラグシップをライフスタイルにチューンしたGarminの傑作。","related":[("review-garminfenix8","⌚","スマートウォッチ","Garmin Fenix 8 レビュー",4.7),("review-applewatchs10","⌚","スマートウォッチ","Apple Watch Series 10 レビュー",4.8),("review-withingsscanwatch2","⌚","スマートウォッチ","Withings ScanWatch 2 レビュー",4.4)]},
    {"slug":"review-withingsscanwatch2","name":"Withings ScanWatch 2（42mm）","cat":"スマートウォッチ","emoji":"⌚","price":"¥49,800","score":4.4,"bg":"#1e3a5f,#2563eb","scores":[("医療機能",98,4.9),("デザイン",94,4.7),("バッテリー",98,4.9),("スマート機能",74,3.7),("コスパ",82,4.1)],"specs":[("ディスプレイ","アナログ文字盤+有機EL小窓"),("バッテリー","最大30日間"),("防水","5ATM"),("センサー","心電図/血中酸素/皮膚温度/歩行速度"),("認証","CE医療機器認証取得"),("特徴","睡眠無呼吸リスク検知")],"pros":["30日間の超長バッテリー","CE医療機器認証取得の信頼性","アナログ時計のような外観","睡眠無呼吸リスク自動検知","医療現場でも使われる精度"],"cons":["スマートウォッチ機能は最低限","アプリが少ない","価格5万円","GPSなし"],"desc":"医療グレードの健康計測を上品なアナログデザインで実現。健康管理を静かに、でも本格的にやりたい人に。","related":[("review-applewatchs10","⌚","スマートウォッチ","Apple Watch Series 10 レビュー",4.8),("review-garminvenu3","⌚","スマートウォッチ","Garmin Venu 3 レビュー",4.5),("review-amazfitgtr4","⌚","スマートウォッチ","Amazfit GTR 4 レビュー",4.1)]},
    {"slug":"review-amazfitgtr4","name":"Amazfit GTR 4","cat":"スマートウォッチ","emoji":"⌚","price":"¥24,800","score":4.1,"bg":"#134e4a,#0f766e","scores":[("コスパ",96,4.8),("バッテリー",90,4.5),("スポーツ機能",88,4.4),("デザイン",78,3.9),("スマート機能",74,3.7)],"specs":[("ディスプレイ","AMOLED 1.43型 Always-On"),("バッテリー","最大14日間"),("防水","5ATM"),("センサー","心拍/血中酸素/ストレス/睡眠"),("GPS","4システム対応（GPS/GLONASS/Galileo/BeiDou）"),("スポーツ","150以上のワークアウトモード")],"pros":["2.5万円以下のコスパ","150以上のスポーツモード対応","14日間バッテリー","4衛星GPS対応","血中酸素・心拍・睡眠計測"],"cons":["Wear OSでないため対応アプリ少ない","スマートフォン通知の連携がやや弱い","Amazon Alexa搭載だが不完全","デザインが地味"],"desc":"2万円台で14日バッテリー×150スポーツモードを実現。スポーツ目的のコスパ重視ユーザーに最適。","related":[("review-galaxywatch7","⌚","スマートウォッチ","Samsung Galaxy Watch 7 レビュー",4.6),("review-pixelwatch3","⌚","スマートウォッチ","Google Pixel Watch 3 レビュー",4.5),("review-withingsscanwatch2","⌚","スマートウォッチ","Withings ScanWatch 2 レビュー",4.4)]},
    # タブレット
    {"slug":"review-ipadprom4","name":"iPad Pro M4 13インチ（WiFi 256GB）","cat":"タブレット","emoji":"📟","price":"¥218,800","score":4.9,"bg":"#1e3a5f,#2d6a4f","scores":[("ディスプレイ",100,5.0),("パフォーマンス",100,5.0),("デザイン",98,4.9),("Apple Pencil連携",98,4.9),("コスパ",72,3.6)],"specs":[("ディスプレイ","13インチ Ultra Retina XDR OLED"),("チップ","M4（3nm）"),("ストレージ","256GB〜2TB"),("重量","582g"),("防水","なし"),("特徴","5.1mm 史上最薄Apple製品")],"pros":["5.1mmという史上最薄ボディ","Ultra Retina XDR OLEDが革命的","M4チップでMacBook超えの性能","Apple Pencil Proと完全連携","ProMotion 120Hz搭載"],"cons":["22万円超の超高価格","OLEDは焼き付きリスクあり","iPadOSの制限でPCに届かない","アクセサリが高額"],"desc":"5.1mmの最薄ボディにM4チップとOLEDを詰め込んだタブレット史上最高傑作。クリエイターの夢を叶える一台。","related":[("review-ipadairm2","📟","タブレット","iPad Air M2 レビュー",4.5),("review-galaxytabs10ultra","📟","タブレット","Samsung Galaxy Tab S10 Ultra レビュー",4.6),("review-surfacepro11","📟","タブレット","Microsoft Surface Pro 11 レビュー",4.5)]},
    {"slug":"review-ipadairm2","name":"iPad Air M2 11インチ（WiFi 128GB）","cat":"タブレット","emoji":"📟","price":"¥98,800","score":4.5,"bg":"#1a3a2e,#064e3b","scores":[("コスパ",88,4.4),("パフォーマンス",90,4.5),("ディスプレイ",86,4.3),("Apple連携",94,4.7),("携帯性",90,4.5)],"specs":[("ディスプレイ","11インチ Liquid Retina 60Hz"),("チップ","M2（5nm）"),("ストレージ","128GB〜1TB"),("重量","462g"),("防水","なし"),("特徴","USB-C 2.0 / Apple Pencil Pro対応")],"pros":["M2チップで日常作業は全部こなせる","10万円以下で買えるiPad","Apple Pencil Pro対応","軽量462g","学生・ビジネスマンに最適"],"cons":["60Hz止まりでProに劣る","USB-C 2.0（Proは4.0）","4年前のOLED非搭載","ストレージ128GBは少ない"],"desc":"iPad ProとAirの間で迷ったらAir。10万円以下でM2チップとApple Pencil Proが使えるコスパ最強iPad。","related":[("review-ipadprom4","📟","タブレット","iPad Pro M4 レビュー",4.9),("review-ipadmini7","📟","タブレット","iPad mini 7 レビュー",4.4),("review-galaxytabs10ultra","📟","タブレット","Samsung Galaxy Tab S10 Ultra レビュー",4.6)]},
    {"slug":"review-galaxytabs10ultra","name":"Samsung Galaxy Tab S10 Ultra（WiFi 256GB）","cat":"タブレット","emoji":"📟","price":"¥198,800","score":4.6,"bg":"#1a0533,#2e1065","scores":[("ディスプレイ",98,4.9),("S Pen",96,4.8),("パフォーマンス",92,4.6),("生産性",90,4.5),("コスパ",74,3.7)],"specs":[("ディスプレイ","14.6インチ Dynamic AMOLED 2X 120Hz"),("チップ","Snapdragon 8 Gen 3"),("ストレージ","256GB〜1TB"),("重量","718g"),("防水","IP68"),("特徴","S Pen同梱 / DeX（PCモード）対応")],"pros":["14.6インチの巨大有機ELが圧巻","S Pen同梱で手書き・イラスト即使える","DexでPCライクに使える","IP68防水対応","Samsungのマルチウィンドウが優秀"],"cons":["20万円近い高価格","718gの重さ","iPadエコシステムに及ばない部分あり","Windowsほど自由でない"],"desc":"14.6インチの大画面有機EL×S Pen×DeX。Androidタブレットの最高峰で生産性を極限まで引き上げる。","related":[("review-ipadprom4","📟","タブレット","iPad Pro M4 レビュー",4.9),("review-surfacepro11","📟","タブレット","Microsoft Surface Pro 11 レビュー",4.5),("review-ipadairm2","📟","タブレット","iPad Air M2 レビュー",4.5)]},
    {"slug":"review-ipadmini7","name":"iPad mini 第7世代（WiFi 128GB）","cat":"タブレット","emoji":"📟","price":"¥78,800","score":4.4,"bg":"#0c1445,#1e3a8a","scores":[("携帯性",100,5.0),("パフォーマンス",88,4.4),("ゲーム",90,4.5),("読書",94,4.7),("コスパ",80,4.0)],"specs":[("ディスプレイ","8.3インチ Liquid Retina 60Hz"),("チップ","A17 Pro（3nm）"),("ストレージ","128GB/256GB"),("重量","293g"),("防水","なし"),("特徴","Apple Pencil Pro対応")],"pros":["293gの片手で使える軽さ","A17 Proで過去最高パフォーマンス","Apple Pencil Proで手書きメモ最適","通勤・読書・ゲームに最高のサイズ","コンパクトでどこにでも持ち運べる"],"cons":["60Hz止まり","画面が小さく動画は物足りない","ストレージ上限256GB","1万円前後の価格上昇"],"desc":"片手で持てる8.3インチに最高のパフォーマンス。通勤・旅行・読書にこれ以上ない相棒。","related":[("review-ipadairm2","📟","タブレット","iPad Air M2 レビュー",4.5),("review-ipadprom4","📟","タブレット","iPad Pro M4 レビュー",4.9),("review-kindlepaperwhite","📖","電子書籍","Kindle Paperwhite レビュー",4.6)]},
    {"slug":"review-pixeltablet","name":"Google Pixel Tablet（WiFi 128GB）","cat":"タブレット","emoji":"📟","price":"¥79,800","score":4.2,"bg":"#14532d,#15803d","scores":[("スマートホーム",96,4.8),("コスパ",84,4.2),("Google連携",92,4.6),("スペック",72,3.6),("充電スタンド",100,5.0)],"specs":[("ディスプレイ","10.95インチ LCD 60Hz"),("チップ","Google Tensor G2"),("ストレージ","128GB/256GB"),("重量","493g"),("防水","なし"),("特徴","充電スピーカーハブ同梱")],"pros":["充電スタンドがスマートスピーカーになる革命","Googleアシスタント×GoogleフォトがフルUXで使える","スタンドに置くだけで充電完了","8万円以下のコスパ","純粋なAndroidでシンプル"],"cons":["Tensor G2はやや非力","LCDで映像品質がライバルに劣る","アプリがAndroidスマホの転用が多い","スタンドなしでは普通のタブレット"],"desc":"充電スタンドに置いた瞬間スマートスピーカーになる唯一無二のコンセプト。自宅の情報ハブとして最高。","related":[("review-ipadairm2","📟","タブレット","iPad Air M2 レビュー",4.5),("review-firemax11","📟","タブレット","Amazon Fire Max 11 レビュー",3.9),("review-applehomedpodmini","🔊","スマートスピーカー","Apple HomePod mini レビュー",4.4)]},
    {"slug":"review-surfacepro11","name":"Microsoft Surface Pro 11（Core Ultra 5 128GB）","cat":"タブレット","emoji":"📟","price":"¥198,800","score":4.5,"bg":"#1e1b4b,#3730a3","scores":[("Windows互換",100,5.0),("パフォーマンス",90,4.5),("ディスプレイ",92,4.6),("携帯性",88,4.4),("コスパ",72,3.6)],"specs":[("ディスプレイ","13インチ OLED 120Hz"),("チップ","Snapdragon X Elite / Core Ultra 5"),("ストレージ","256GB〜1TB"),("重量","879g（カバーなし）"),("防水","なし"),("特徴","Copilot+ PC / Windows 11")],"pros":["フルWindowsがタブレットで使える","Copilot+ PCでAI機能が充実","OLEDの映像品質が高い","Surface Slim Pen 2が書き心地最高","Snapdragon版は軽量・長バッテリー"],"cons":["キーボードカバーが別売り高額","Snapdragon版はx86アプリ非対応も","20万円超の高価格","重量が1kgを超える"],"desc":"Windowsタブレットの最高峰。フルOSがタブレットで動くことへの需要は根強い。ビジネスマン必見。","related":[("review-ipadprom4","📟","タブレット","iPad Pro M4 レビュー",4.9),("review-galaxytabs10ultra","📟","タブレット","Samsung Galaxy Tab S10 Ultra レビュー",4.6),("review-macbookairm3","💻","ノートPC","MacBook Air M3 レビュー",4.8)]},
    {"slug":"review-firemax11","name":"Amazon Fire Max 11（64GB）","cat":"タブレット","emoji":"📟","price":"¥29,980","score":3.9,"bg":"#0c4a6e,#0369a1","scores":[("価格",100,5.0),("Amazon連携",96,4.8),("動画視聴",84,4.2),("スペック",60,3.0),("汎用性",62,3.1)],"specs":[("ディスプレイ","11インチ LCD 2000×1200"),("チップ","MediaTek MT8188J"),("ストレージ","64GB/128GB + microSD"),("重量","490g"),("防水","なし"),("特徴","Fire OS / Amazon Alexa搭載")],"pros":["3万円以下の破格コスパ","Amazon Prime Video・Music最適化","Alexa音声操作に対応","microSDで容量拡張可能","子供用にも安心"],"cons":["Fire OSでGoogle Play非対応","スペックが低くゲームは厳しい","カメラ性能が低い","iPadと比較するのが酷なレベル"],"desc":"Amazonサービス専用デバイスと割り切れば3万円以下は最高のコスパ。Prime Video視聴専用機として最適。","related":[("review-ipadairm2","📟","タブレット","iPad Air M2 レビュー",4.5),("review-pixeltablet","📟","タブレット","Google Pixel Tablet レビュー",4.2),("review-kindlepaperwhite","📖","電子書籍","Kindle Paperwhite レビュー",4.6)]},
    # ノートPC
    {"slug":"review-macbookprom4pro","name":"MacBook Pro M4 Pro 14インチ（24GB/512GB）","cat":"ノートPC","emoji":"💻","price":"¥298,800","score":4.9,"bg":"#1c1c1e,#3a3a3c","scores":[("パフォーマンス",100,5.0),("バッテリー",96,4.8),("ディスプレイ",98,4.9),("デザイン",96,4.8),("コスパ",72,3.6)],"specs":[("ディスプレイ","14.2インチ Liquid Retina XDR 120Hz"),("チップ","M4 Pro（3nm）12コアCPU/20コアGPU"),("メモリ","24GB / 48GB"),("ストレージ","512GB〜4TB SSD"),("バッテリー","最大22時間"),("重量","1.61kg")],"pros":["M4 Proは現行最高のノートPCチップ","22時間バッテリーで丸一日使える","Liquid Retina XDRが圧巻の美しさ","Thunderbolt 5接続","ファンが静か×発熱が少ない"],"cons":["30万円近い高価格","重さ1.61kgと軽くはない","RAMのアップグレードが高額","独自macOS環境"],"desc":"ノートPCの最高傑作。動画編集・機械学習・3DCGを22時間バッテリーで動かせるプロ向け最強機。","related":[("review-macbookairm3","💻","ノートPC","MacBook Air M3 レビュー",4.8),("review-dellxps15","💻","ノートPC","Dell XPS 15 レビュー",4.6),("review-thinkpadx1carbon","💻","ノートPC","ThinkPad X1 Carbon レビュー",4.7)]},
    {"slug":"review-macbookairm3","name":"MacBook Air M3 15インチ（16GB/512GB）","cat":"ノートPC","emoji":"💻","price":"¥188,800","score":4.8,"bg":"#292524,#57534e","scores":[("コスパ",92,4.6),("バッテリー",96,4.8),("静音性",100,5.0),("パフォーマンス",90,4.5),("携帯性",90,4.5)],"specs":[("ディスプレイ","15.3インチ Liquid Retina 60Hz"),("チップ","M3（3nm）8コアCPU/10コアGPU"),("メモリ","16GB / 24GB"),("ストレージ","256GB〜2TB SSD"),("バッテリー","最大18時間"),("重量","1.51kg")],"pros":["ファンレスで完全無音","18時間の超長バッテリー","ほぼ全ての人に推せる汎用性","15インチで1.51kg軽量","macOSの安定性・セキュリティ"],"cons":["60Hz（ProMotionなし）","ファンレスなので高負荷時に制限","DisplayPort出力は1台のみ（16GB以上は2台）","最安構成は16GB/256GBで不足しがち"],"desc":"すべての人に推せるノートPC。完全無音×18時間バッテリー×M3チップで日常作業のすべてを完璧にこなす。","related":[("review-macbookprom4pro","💻","ノートPC","MacBook Pro M4 Pro レビュー",4.9),("review-lggram17","💻","ノートPC","LG Gram 17 レビュー",4.4),("review-hpspectrex360","💻","ノートPC","HP Spectre x360 レビュー",4.5)]},
    {"slug":"review-dellxps15","name":"Dell XPS 15（Core Ultra 9/32GB/1TB）","cat":"ノートPC","emoji":"💻","price":"¥288,800","score":4.6,"bg":"#1e3a5f,#1e40af","scores":[("ディスプレイ",98,4.9),("パフォーマンス",92,4.6),("デザイン",94,4.7),("バッテリー",82,4.1),("コスパ",74,3.7)],"specs":[("ディスプレイ","15.6インチ 有機EL 3.5K OLED"),("チップ","Intel Core Ultra 9 185H"),("GPU","NVIDIA RTX 4070"),("メモリ","32GB LPDDR5"),("ストレージ","1TB SSD"),("重量","1.86kg")],"pros":["3.5K有機ELディスプレイが最高峰","RTX 4070でクリエイティブ作業が爆速","Thunderbolt 4×2端子","洗練されたアルミデザイン","Core Ultra 9の高性能"],"cons":["30万円近い高価格","バッテリーが4〜6時間と短め","1.86kgと重い","発熱が大きい"],"desc":"Windows最高峰の映像体験を提供する3.5K有機EL×RTX 4070の傑作。クリエイター・デザイナーに。","related":[("review-macbookprom4pro","💻","ノートPC","MacBook Pro M4 Pro レビュー",4.9),("review-razerblade15","💻","ノートPC","Razer Blade 15 レビュー",4.5),("review-asusrogzephyrusg14","💻","ノートPC","ASUS ROG Zephyrus G14 レビュー",4.5)]},
    {"slug":"review-thinkpadx1carbon","name":"ThinkPad X1 Carbon Gen 12（Core Ultra 7/32GB/1TB）","cat":"ノートPC","emoji":"💻","price":"¥278,000","score":4.7,"bg":"#1c1917,#44403c","scores":[("携帯性",96,4.8),("耐久性",98,4.9),("バッテリー",88,4.4),("ビジネス機能",98,4.9),("コスパ",72,3.6)],"specs":[("ディスプレイ","14インチ IPS 2.8K OLED"),("チップ","Intel Core Ultra 7 165U"),("メモリ","32GB LPDDR5x"),("ストレージ","1TB SSD"),("重量","1.08kg"),("認証","MIL-STD-810H")],"pros":["1.08kgの超軽量","MIL規格準拠の耐久性","Thunderbolt 4×2+USB 3.2×2など豊富な端子","最大48時間バッテリー（省電力）","指紋・顔認証のセキュリティが充実"],"cons":["28万円の高価格","14型のOLED搭載モデルは高額","グラフィック性能は非ゲーミング","冷却能力に限界あり"],"desc":"出張族・ビジネスマンのための最高のノートPC。1kg超えの軽さと伝説の打鍵感は唯一無二。","related":[("review-macbookairm3","💻","ノートPC","MacBook Air M3 レビュー",4.8),("review-hpspectrex360","💻","ノートPC","HP Spectre x360 レビュー",4.5),("review-lggram17","💻","ノートPC","LG Gram 17 レビュー",4.4)]},
    {"slug":"review-asusrogzephyrusg14","name":"ASUS ROG Zephyrus G14（Ryzen 9/32GB/1TB）","cat":"ノートPC","emoji":"💻","price":"¥268,800","score":4.5,"bg":"#4a1942,#6b21a8","scores":[("ゲーム性能",94,4.7),("携帯性",90,4.5),("ディスプレイ",92,4.6),("バッテリー",84,4.2),("コスパ",80,4.0)],"specs":[("ディスプレイ","14インチ Mini LED 2560×1600 165Hz"),("チップ","AMD Ryzen 9 8945HS"),("GPU","NVIDIA RTX 4070 Laptop"),("メモリ","32GB LPDDR5"),("ストレージ","1TB SSD"),("重量","1.65kg")],"pros":["1.65kgで持ち運べるゲーミングPC","ROG NebuliaDisplayのMini LEDが鮮明","Ryzen 9×RTX 4070の最強コンビ","MUXスイッチでGPU直結対応","冷却性能が優秀で長時間ゲームでも安定"],"cons":["27万円の高価格","1.65kgは軽いが毎日持ち歩くにはギリギリ","バッテリーはゲーム時3〜4時間"],"desc":"最軽量クラスのゲーミングノートPC。「持ち運べてゲームもできる」の最終回答。","related":[("review-razerblade15","💻","ノートPC","Razer Blade 15 レビュー",4.5),("review-dellxps15","💻","ノートPC","Dell XPS 15 レビュー",4.6),("review-macbookprom4pro","💻","ノートPC","MacBook Pro M4 Pro レビュー",4.9)]},
    {"slug":"review-hpspectrex360","name":"HP Spectre x360 14（Core Ultra 7/32GB/2TB）","cat":"ノートPC","emoji":"💻","price":"¥248,800","score":4.5,"bg":"#0c4a6e,#075985","scores":[("2-in-1",96,4.8),("ディスプレイ",90,4.5),("バッテリー",88,4.4),("デザイン",92,4.6),("コスパ",76,3.8)],"specs":[("ディスプレイ","13.5インチ OLED 2.8K タッチ"),("チップ","Intel Core Ultra 7 155H"),("メモリ","32GB LPDDR5x"),("ストレージ","2TB SSD"),("重量","1.40kg"),("特徴","360°回転/ペン入力/4つのモード")],"pros":["360°回転で4モードに対応","OLED 2.8Kのタッチ体験","HP Stylus Pen同梱","1.4kgの携帯性","Thunderbolt 4×2端子"],"cons":["25万円の高価格","冷却性能が限られる","バッテリー動作は8〜10時間程度"],"desc":"ペン入力×2-in-1×有機ELの三冠王。タッチ&ペンで思考をそのままデジタル化するプレミアム機。","related":[("review-macbookairm3","💻","ノートPC","MacBook Air M3 レビュー",4.8),("review-thinkpadx1carbon","💻","ノートPC","ThinkPad X1 Carbon レビュー",4.7),("review-surfacepro11","📟","タブレット","Microsoft Surface Pro 11 レビュー",4.5)]},
    {"slug":"review-lggram17","name":"LG Gram 17（Core Ultra 7/32GB/1TB）","cat":"ノートPC","emoji":"💻","price":"¥248,800","score":4.4,"bg":"#052e16,#14532d","scores":[("携帯性",96,4.8),("バッテリー",90,4.5),("画面サイズ",96,4.8),("パフォーマンス",82,4.1),("コスパ",76,3.8)],"specs":[("ディスプレイ","17インチ IPS 2560×1600 60Hz"),("チップ","Intel Core Ultra 7 155H"),("メモリ","32GB LPDDR5"),("ストレージ","1TB SSD"),("重量","1.35kg"),("認証","MIL-STD-810H")],"pros":["17型で1.35kgの軽量設計","MIL規格準拠の耐久性","大画面で作業効率が高い","Thunderbolt 4×2端子","バッテリー最大17時間"],"cons":["25万円の高価格","17型は持ち運びに大きい","IPS 60Hzで映像品質は普通","グラフィック性能は控えめ"],"desc":"17型なのに1.35kgという矛盾を解決した名機。大画面で作業効率を最大化したい人の最適解。","related":[("review-macbookairm3","💻","ノートPC","MacBook Air M3 レビュー",4.8),("review-thinkpadx1carbon","💻","ノートPC","ThinkPad X1 Carbon レビュー",4.7),("review-hpspectrex360","💻","ノートPC","HP Spectre x360 レビュー",4.5)]},
    {"slug":"review-razerblade15","name":"Razer Blade 15（Core Ultra 9/32GB/1TB）","cat":"ノートPC","emoji":"💻","price":"¥348,800","score":4.5,"bg":"#292524,#57534e","scores":[("ゲーム性能",96,4.8),("デザイン",96,4.8),("ディスプレイ",94,4.7),("バッテリー",74,3.7),("コスパ",68,3.4)],"specs":[("ディスプレイ","15.6インチ QHD OLED 240Hz"),("チップ","Intel Core Ultra 9 185H"),("GPU","NVIDIA RTX 4080 Laptop"),("メモリ","32GB DDR5"),("ストレージ","1TB SSD"),("重量","2.01kg")],"pros":["RTX 4080のゲーミング最高性能","QHD OLED 240Hzが圧倒的","MacBook並みの洗練されたデザイン","Thunderbolt 4×2端子","冷却性能が優秀"],"cons":["35万円の超高価格","2kgの重さ","バッテリーはゲーム時2〜3時間","1mm単位で高い修理費"],"desc":"ゲーミングの最高性能を洗練されたデザインに収めたRazerの本気作。最高峰を妥協なく求める人に。","related":[("review-asusrogzephyrusg14","💻","ノートPC","ASUS ROG Zephyrus G14 レビュー",4.5),("review-dellxps15","💻","ノートPC","Dell XPS 15 レビュー",4.6),("review-macbookprom4pro","💻","ノートPC","MacBook Pro M4 Pro レビュー",4.9)]},
    # モニター
    {"slug":"review-lg27gp850b","name":"LG 27GP850-B","cat":"モニター","emoji":"🖥️","price":"¥54,800","score":4.6,"bg":"#1e3a5f,#1e40af","scores":[("ゲーム性能",90,4.5),("色再現性",90,4.5),("汎用性",92,4.6),("価格",86,4.3),("コスパ",90,4.5)],"specs":[("サイズ","27インチ"),("解像度","2560×1440（WQHD）"),("パネル","Nano IPS"),("リフレッシュレート","180Hz"),("応答速度","1ms（GtG）"),("色域","sRGB 98% / DCI-P3 72%")],"pros":["180Hz×Nano IPS×sRGB98%の三冠","ゲームもクリエイティブ作業も両立","価格5.5万円のコスパ","USB-C給電対応","HDR400対応"],"cons":["HDRはエントリークラス","DCI-P3 72%でプロ映像には不足","OLED/Mini LEDに映像品質で劣る"],"desc":"ゲーマー×テレワーカー×クリエイターの万能モニター。一台で全部こなせるベストバイ。","related":[("review-asusrogswiftpg279qm","🖥️","モニター","ASUS ROG Swift PG279QM レビュー",4.7),("review-dellu2723d","🖥️","モニター","Dell U2723D レビュー",4.7),("review-samsungodysseyg7","🖥️","モニター","Samsung Odyssey G7 レビュー",4.6)]},
    {"slug":"review-asusrogswiftpg279qm","name":"ASUS ROG Swift PG279QM","cat":"モニター","emoji":"🖥️","price":"¥89,800","score":4.7,"bg":"#1a0533,#3b0764","scores":[("ゲーム性能",100,5.0),("応答速度",100,5.0),("色再現性",88,4.4),("価格",76,3.8),("コスパ",84,4.2)],"specs":[("サイズ","27インチ"),("解像度","2560×1440（WQHD）"),("パネル","Fast IPS"),("リフレッシュレート","240Hz"),("応答速度","1ms（GtG）"),("特徴","G-Sync Ultimate対応")],"pros":["240HzとFast IPSで競技FPS最強","G-Sync Ultimateで完璧な同期","1ms応答速度で残像ゼロ","sRGB 99%で色も優秀","HDR600対応"],"cons":["9万円の高価格","G-SyncのためNVIDIA GPUが必要","ゲーム以外では過剰スペック"],"desc":"競技FPS・eスポーツプレイヤーへの最終回答。240Hz×G-Sync Ultimateで有利な状況を作り出す。","related":[("review-lg27gp850b","🖥️","モニター","LG 27GP850-B レビュー",4.6),("review-samsungodysseyg7","🖥️","モニター","Samsung Odyssey G7 レビュー",4.6),("review-benqpd3205u","🖥️","モニター","BenQ PD3205U レビュー",4.6)]},
    {"slug":"review-dellu2723d","name":"Dell U2723D","cat":"モニター","emoji":"🖥️","price":"¥78,000","score":4.7,"bg":"#0c1445,#1e3a8a","scores":[("色再現性",96,4.8),("ビジネス機能",96,4.8),("USB-C",96,4.8),("価格",80,4.0),("コスパ",86,4.3)],"specs":[("サイズ","27インチ"),("解像度","3840×2160（4K UHD）"),("パネル","IPS Black"),("リフレッシュレート","60Hz"),("色域","sRGB 100% / DCI-P3 98%"),("特徴","USB-C 90W給電 / Thunderbolt 4")],"pros":["IPS Blackで黒の深さがIPSとは別次元","USB-C 1本で映像+電源+データ転送","DCI-P3 98%のプロ仕様色域","4K解像度","エルゴノミクススタンドが優秀"],"cons":["7.8万円の高価格","60Hz止まりでゲームには不向き","IPS Blackも有機ELには劣る"],"desc":"テレワーカー・クリエイターの最高のビジネスモニター。USB-C1本で繋がるシンプルさが革命的。","related":[("review-benqpd3205u","🖥️","モニター","BenQ PD3205U レビュー",4.6),("review-lg27gp850b","🖥️","モニター","LG 27GP850-B レビュー",4.6),("review-lg45gr95qeb","🖥️","モニター","LG 45GR95QE-B レビュー",4.5)]},
    {"slug":"review-benqpd3205u","name":"BenQ PD3205U","cat":"モニター","emoji":"🖥️","price":"¥84,800","score":4.6,"bg":"#134e4a,#0f766e","scores":[("色再現性",94,4.7),("クリエイター機能",96,4.8),("USB-C",90,4.5),("価格",76,3.8),("コスパ",82,4.1)],"specs":[("サイズ","32インチ"),("解像度","3840×2160（4K UHD）"),("パネル","IPS"),("リフレッシュレート","60Hz"),("色域","DCI-P3 95% / Rec.2020 72%"),("特徴","USB-C 90W / KVM機能 / ホットキーパック2")],"pros":["DCI-P3 95%のクリエイター仕様","KVMスイッチでPC2台切り替え","ホットキーパック2で設定が簡単","32インチの作業面積","BenQ独自のColorGenie自動色調整"],"cons":["8.5万円の高価格","60HzでゲームNG","IPS有機ELに映像では劣る"],"desc":"デザイナー・映像クリエイターが選ぶ32型4Kモニター。色の信頼性がプロの現場で評価される一台。","related":[("review-dellu2723d","🖥️","モニター","Dell U2723D レビュー",4.7),("review-lg27gp850b","🖥️","モニター","LG 27GP850-B レビュー",4.6),("review-asusrogswiftpg279qm","🖥️","モニター","ASUS ROG Swift PG279QM レビュー",4.7)]},
    {"slug":"review-samsungodysseyg7","name":"Samsung Odyssey G7 32インチ","cat":"モニター","emoji":"🖥️","price":"¥74,800","score":4.6,"bg":"#1a0533,#2e1065","scores":[("没入感",98,4.9),("ゲーム性能",92,4.6),("色再現性",86,4.3),("デザイン",90,4.5),("コスパ",82,4.1)],"specs":[("サイズ","32インチ"),("解像度","2560×1440（WQHD）"),("パネル","VA曲面 1000R"),("リフレッシュレート","240Hz"),("応答速度","1ms（MPRT）"),("特徴","G-Sync Compatible / FreeSync Premium Pro")],"pros":["1000R強烈な湾曲で圧倒的没入感","240Hz×1msのゲーミング最高峰","32型の大画面","DisplayHDR 600対応","G-Sync/FreeSync両対応"],"cons":["VA固有のコントラストは高いが色域は普通","7.5万円の価格","1000Rは使い慣れるまで時間がかかる"],"desc":"強烈な湾曲で包み込まれる没入感が唯一無二。FPS・RPG・レース系すべてのゲームが別次元になる。","related":[("review-asusrogswiftpg279qm","🖥️","モニター","ASUS ROG Swift PG279QM レビュー",4.7),("review-lg27gp850b","🖥️","モニター","LG 27GP850-B レビュー",4.6),("review-lg45gr95qeb","🖥️","モニター","LG 45GR95QE-B レビュー",4.5)]},
    {"slug":"review-lg45gr95qeb","name":"LG 45GR95QE-B","cat":"モニター","emoji":"🖥️","price":"¥168,000","score":4.5,"bg":"#1c1917,#292524","scores":[("没入感",100,5.0),("ディスプレイ品質",96,4.8),("作業効率",96,4.8),("価格",66,3.3),("コスパ",76,3.8)],"specs":[("サイズ","45インチ"),("解像度","3440×1440（WQHD）"),("パネル","WOLED"),("リフレッシュレート","240Hz"),("特徴","800R湾曲 / デュアルQHD相当"),("応答速度","0.03ms")],"pros":["45型WOLED×800Rの究極没入感","デュアルモニター不要の広大な作業面積","0.03msの超高速応答","有機ELの黒の深さが圧倒的","ゲームも作業もこなせる万能機"],"cons":["17万円の超高価格","横幅1m超で設置場所を選ぶ","有機ELの焼き付きリスク","重量10kg超"],"desc":"1台でデュアルモニターを超える究極の体験。45型WOLEDは一度使ったら元に戻れないレベルの没入感。","related":[("review-samsungodysseyg7","🖥️","モニター","Samsung Odyssey G7 レビュー",4.6),("review-dellu2723d","🖥️","モニター","Dell U2723D レビュー",4.7),("review-asusrogswiftpg279qm","🖥️","モニター","ASUS ROG Swift PG279QM レビュー",4.7)]},
    # カメラ
    {"slug":"review-sonyzve10ii","name":"Sony ZV-E10 II","cat":"カメラ","emoji":"📸","price":"¥99,800","score":4.8,"bg":"#78350f,#92400e","scores":[("動画性能",98,4.9),("AF性能",96,4.8),("携帯性",92,4.6),("コスパ",88,4.4),("使いやすさ",94,4.7)],"specs":[("センサー","APS-C 2610万画素"),("動画","4K 60fps / 10bit"),("AF","AIプロセッシングユニット リアルタイムトラッキング"),("手ぶれ補正","電子式"),("重量","291g（ボディのみ）"),("特徴","ビューファインダーなし / 全指向性マイク搭載")],"pros":["4K 60fps×10bitの高品質動画","AI被写体認識AFが秀逸","291gの軽量コンパクト","全指向性マイクが入門者に親切","USB-C給電しながら撮影可能"],"cons":["ボディ内手ぶれ補正なし（電子式のみ）","バリアングルの液晶は固定軸","防塵防滴なし","ファインダーなし"],"desc":"YouTubeデビューに最適なミラーレス入門機。4K 60fps×AI AFで動画撮影が劇的に楽になる。","related":[("review-canoneosr50","📸","カメラ","Canon EOS R50 レビュー",4.6),("review-sonya7cii","📸","カメラ","Sony α7C II レビュー",4.8),("review-nikonz30","📸","カメラ","Nikon Z30 レビュー",4.5)]},
    {"slug":"review-sonya7cii","name":"Sony α7C II（ボディ）","cat":"カメラ","emoji":"📸","price":"¥258,000","score":4.8,"bg":"#7c2d12,#9a3412","scores":[("センサー",98,4.9),("AF",100,5.0),("動画",94,4.7),("携帯性",90,4.5),("コスパ",74,3.7)],"specs":[("センサー","フルサイズ 33MP BSI CMOS"),("動画","4K 60fps"),("AF","リアルタイム認識AF（AI強化）"),("手ぶれ補正","ボディ内5軸 7.0段"),("重量","514g（ボディのみ）"),("特徴","コンパクトフルサイズ")],"pros":["フルサイズセンサー33MPの圧倒的画質","7段ボディ内手ぶれ補正","AIオートフォーカスが最高精度","514gのコンパクトフルサイズ","4K 60fps動画対応"],"cons":["26万円の高価格","バッテリーがやや弱い（ILCE-7CM2）","グリップが浅い","メニューUIが複雑"],"desc":"コンパクトボディにフルサイズの夢を詰め込んだ傑作。旅行・ポートレート・動画すべてをプロ品質で。","related":[("review-sonyzve10ii","📸","カメラ","Sony ZV-E10 II レビュー",4.8),("review-fujifilmxt5","📸","カメラ","Fujifilm X-T5 レビュー",4.7),("review-canoneosr50","📸","カメラ","Canon EOS R50 レビュー",4.6)]},
    {"slug":"review-fujifilmxt5","name":"Fujifilm X-T5（ボディ）","cat":"カメラ","emoji":"📸","price":"¥248,000","score":4.7,"bg":"#92400e,#b45309","scores":[("画質",98,4.9),("フィルムシミュレーション",100,5.0),("デザイン",96,4.8),("動画",80,4.0),("コスパ",76,3.8)],"specs":[("センサー","APS-C 4020万画素"),("動画","4K 30fps"),("フィルムシミュレーション","20種類"),("手ぶれ補正","ボディ内7段"),("重量","557g（ボディ+バッテリー）"),("特徴","レトロデザイン / メカニカルダイヤル")],"pros":["4020万画素の圧倒的解像度","20種のフィルムシミュレーションが芸術的","レトロダイヤル操作が楽しい","APS-Cで最高クラスの画質","ボディ内7段手ぶれ補正"],"cons":["動画は4K 30fps止まり（クロップあり）","25万円の高価格","バッテリー持ちが普通","FUJIFILMレンズも高額"],"desc":"フィルムカメラの感触と最新デジタル性能を融合した芸術品。写真を本気で楽しみたい人の最高の相棒。","related":[("review-sonya7cii","📸","カメラ","Sony α7C II レビュー",4.8),("review-sonyzve10ii","📸","カメラ","Sony ZV-E10 II レビュー",4.8),("review-canoneosr50","📸","カメラ","Canon EOS R50 レビュー",4.6)]},
    {"slug":"review-canoneosr50","name":"Canon EOS R50（ボディ）","cat":"カメラ","emoji":"📸","price":"¥99,800","score":4.6,"bg":"#431407,#7c2d12","scores":[("使いやすさ",96,4.8),("AF",92,4.6),("コスパ",90,4.5),("動画",86,4.3),("携帯性",88,4.4)],"specs":[("センサー","APS-C 24.2MP"),("動画","4K 30fps"),("AF","デュアルピクセル CMOS AF II"),("手ぶれ補正","デジタル"),("重量","375g（ボディのみ）"),("特徴","被写体自動検出AF / Vlog向け仕様")],"pros":["375gの軽量設計","デュアルピクセルAFが優秀","スマホ感覚で使える直感UI","瞳AFが動物・乗り物も対応","10万円以下のコスパ"],"cons":["ボディ内手ぶれ補正なし","4K時クロップあり","バッテリー持ちがやや弱い","連写速度が控えめ"],"desc":"カメラデビューに最適な入門ミラーレス。スマホのような直感操作で本格写真がすぐに撮れる。","related":[("review-sonyzve10ii","📸","カメラ","Sony ZV-E10 II レビュー",4.8),("review-nikonz30","📸","カメラ","Nikon Z30 レビュー",4.5),("review-goprohero12","📸","カメラ","GoPro HERO12 Black レビュー",4.5)]},
    {"slug":"review-goprohero12","name":"GoPro HERO12 Black","cat":"カメラ","emoji":"📸","price":"¥59,800","score":4.5,"bg":"#1c1917,#292524","scores":[("防水",100,5.0),("手ぶれ補正",98,4.9),("動画",90,4.5),("コスパ",82,4.1),("携帯性",96,4.8)],"specs":[("動画","5.3K 60fps / 4K 120fps"),("手ぶれ補正","HyperSmooth 6.0"),("防水","10m防水（ハウジングなし）"),("バッテリー","最大70分（5.3K撮影）"),("重量","154g"),("特徴","縦横切り替え / タイムラプス")],"pros":["HyperSmooth 6.0の手ぶれ補正が革命的","10m防水でハウジング不要","5.3K 60fpsの高解像度","154gの超コンパクト","縦動画撮影に対応（SNS最適）"],"cons":["バッテリーが70分と短い","5.6万円の価格","夜間撮影はミラーレスに劣る","マイクは外部接続必要"],"desc":"アクティブライフスタイルのための最強カメラ。登山・サーフィン・スキーで一切ブレない映像を記録。","related":[("review-djiosmoaction4","📸","カメラ","DJI Osmo Action 4 レビュー",4.6),("review-insta360x4","📸","カメラ","Insta360 X4 レビュー",4.5),("review-sonyzve10ii","📸","カメラ","Sony ZV-E10 II レビュー",4.8)]},
    {"slug":"review-insta360x4","name":"Insta360 X4","cat":"カメラ","emoji":"📸","price":"¥74,800","score":4.5,"bg":"#052e16,#14532d","scores":[("360度撮影",100,5.0),("防水",96,4.8),("編集アプリ",94,4.7),("画質",86,4.3),("コスパ",78,3.9)],"specs":[("動画","8K 360度 30fps / 4K 100fps"),("防水","10m防水"),("バッテリー","最大135分（8K撮影）"),("重量","203g"),("特徴","見えない自撮り棒 / AI編集"),("ストレージ","microSD")],"pros":["8K 360度撮影が可能","見えない自撮り棒で神カメラワーク","AI編集が爆速","10m防水","インスタ・TikTok最強コンテンツが作れる"],"cons":["7.5万円の価格","8K動画の容量が大きい","スマホ連携での編集が必須","360度以外の用途は限定的"],"desc":"インスタ・TikTok最強コンテンツを量産できる全天球カメラ。見えない自撮り棒の魔法を体験せよ。","related":[("review-goprohero12","📸","カメラ","GoPro HERO12 Black レビュー",4.5),("review-djiosmoaction4","📸","カメラ","DJI Osmo Action 4 レビュー",4.6),("review-sonyzve10ii","📸","カメラ","Sony ZV-E10 II レビュー",4.8)]},
    {"slug":"review-djiosmoaction4","name":"DJI Osmo Action 4","cat":"カメラ","emoji":"📸","price":"¥49,800","score":4.6,"bg":"#0c4a6e,#164e63","scores":[("防水",100,5.0),("寒冷地対応",96,4.8),("手ぶれ補正",92,4.6),("動画",88,4.4),("コスパ",86,4.3)],"specs":[("動画","4K 120fps"),("防水","16m防水 / -20℃低温動作"),("手ぶれ補正","RockSteady 3.0 / HorizonBalancing"),("バッテリー","160分（標準）"),("重量","145g"),("特徴","縦横切り替え / デュアルスクリーン")],"pros":["16m防水×-20℃耐寒で最強防水","4K 120fpsのスローモーション","デュアルスクリーン搭載","160分の長バッテリー","GoProより若干安い"],"cons":["GoProに比べてブランド認知が低い","5万円の価格","夜間画質はミラーレスに劣る"],"desc":"-20℃の雪山から水深16mまで対応する全天候型アクションカメラ。GoProと迷ったらバッテリーと防水でDJIを選べ。","related":[("review-goprohero12","📸","カメラ","GoPro HERO12 Black レビュー",4.5),("review-insta360x4","📸","カメラ","Insta360 X4 レビュー",4.5),("review-sonyzve10ii","📸","カメラ","Sony ZV-E10 II レビュー",4.8)]},
    {"slug":"review-nikonz30","name":"Nikon Z30（ボディ）","cat":"カメラ","emoji":"📸","price":"¥89,800","score":4.5,"bg":"#1e3a5f,#2563eb","scores":[("動画",90,4.5),("使いやすさ",90,4.5),("コスパ",88,4.4),("AF",86,4.3),("携帯性",88,4.4)],"specs":[("センサー","APS-C 20.9MP"),("動画","4K 30fps / フルHD 120fps"),("AF","顔・瞳検出AF"),("手ぶれ補正","電子式VR"),("重量","405g（ボディのみ）"),("特徴","ファインダーレス/Vlog専用設計")],"pros":["vlog向け設計でフリップ液晶搭載","405gの軽量設計","顔・瞳認識AFが優秀","USB-C給電対応","マイク端子搭載"],"cons":["ボディ内手ぶれ補正なし","4K時1.5倍クロップ","ファインダーなし","写真よりも動画特化"],"desc":"ニコン入門機の動画特化版。vlog・YouTube配信に必要な機能を9万円以下に凝縮した実用的な一台。","related":[("review-sonyzve10ii","📸","カメラ","Sony ZV-E10 II レビュー",4.8),("review-canoneosr50","📸","カメラ","Canon EOS R50 レビュー",4.6),("review-goprohero12","📸","カメラ","GoPro HERO12 Black レビュー",4.5)]},
    # モバイルバッテリー・充電器
    {"slug":"review-anker733","name":"Anker 733 Power Bank（GaNPrime PowerCore 65W）","cat":"モバイルバッテリー","emoji":"🔋","price":"¥10,990","score":4.7,"bg":"#134e4a,#065f46","scores":[("コンセプト",100,5.0),("携帯性",96,4.8),("充電速度",88,4.4),("コスパ",88,4.4),("機能性",90,4.5)],"specs":[("容量","10,000mAh"),("出力","65W（USB-C×2/USB-A×1）"),("充電","コンセント一体型"),("重量","302g"),("サイズ","W72×H72×D29mm"),("特徴","充電器として単体使用可")],"pros":["コンセントに直差しで給電しながら充電","ノートPCまで65Wで充電可能","モバイルバッテリーと充電器が1つになる","旅行の荷物を大幅削減","10,990円のコスパ"],"cons":["302gとやや重め","自身の充電時間が長め（3時間以上）","コンセント一体型で厚みがある"],"desc":"旅行・出張での荷物を劇的に減らす充電器兼バッテリー。ノートPCまで65Wで充電できる最適解。","related":[("review-ankerprime20000","🔋","モバイルバッテリー","Anker Prime 20000 レビュー",4.8),("review-ciosmartcoby","🔋","充電器","CIO SMARTCOBY Pro レビュー",4.5),("review-ugreennexode140w","🔋","充電器","Ugreen Nexode 140W レビュー",4.5)]},
    {"slug":"review-ankerprime20000","name":"Anker Prime 20000mAh（200W）","cat":"モバイルバッテリー","emoji":"🔋","price":"¥22,990","score":4.8,"bg":"#052e16,#166534","scores":[("容量",96,4.8),("充電速度",100,5.0),("アプリ連携",96,4.8),("コスパ",80,4.0),("機能性",98,4.9)],"specs":[("容量","20,000mAh"),("出力","200W（USB-C×2/USB-A×1）"),("充電","140W双方向充電"),("重量","451g"),("特徴","Ankerアプリ連携 / 残量・充電状況管理"),("認証","PSE適合")],"pros":["200W双方向出力でノートPCを2台同時急速充電","スマートアプリで充電状況をリアルタイム管理","20,000mAhの大容量","140Wでバッテリー自体も高速充電","USB-C2口の出力が柔軟"],"cons":["2.3万円と高価格","451gの重さ","アプリ管理が不要な人には過剰"],"desc":"最強の大容量モバイルバッテリー。ノートPCを200Wで充電しながら自身も140Wで充電できる次世代品。","related":[("review-anker733","🔋","モバイルバッテリー","Anker 733 レビュー",4.7),("review-ugreennexode140w","🔋","充電器","Ugreen Nexode 140W レビュー",4.5),("review-anker547","🔋","充電器","Anker 547 充電ステーション レビュー",4.6)]},
    {"slug":"review-ciosmartcoby","name":"CIO SMARTCOBY Pro PLUG 65W","cat":"充電器","emoji":"🔋","price":"¥5,480","score":4.5,"bg":"#14532d,#15803d","scores":[("薄さ",100,5.0),("コスパ",96,4.8),("出力",84,4.2),("品質",88,4.4),("携帯性",96,4.8)],"specs":[("容量","13,400mAh"),("出力","65W（USB-C×2/USB-A×1）"),("充電","コンセント一体型"),("重量","225g"),("厚さ","約14mm"),("国内規格","PSE適合")],"pros":["14mmの圧倒的な薄さ","225gの軽量","国内メーカーで品質安心","65Wでノートpcも充電可","コンセント直差し充電器兼バッテリー"],"cons":["容量13,400mAhはやや少なめ","USB-C×2のみでUSB-Aが1つ","薄いため発熱が気になる場合も"],"desc":"財布と同じ薄さ14mmのモバイルバッテリー兼充電器。国産ブランドCIOの品質と革命的薄さを体感せよ。","related":[("review-anker733","🔋","モバイルバッテリー","Anker 733 レビュー",4.7),("review-ankerprime20000","🔋","モバイルバッテリー","Anker Prime 20000 レビュー",4.8),("review-ugreennexode140w","🔋","充電器","Ugreen Nexode 140W レビュー",4.5)]},
    {"slug":"review-ugreennexode140w","name":"Ugreen Nexode 140W 充電器","cat":"充電器","emoji":"🔋","price":"¥7,980","score":4.5,"bg":"#0a3622,#14532d","scores":[("出力",98,4.9),("コスパ",94,4.7),("ポート数",92,4.6),("サイズ",82,4.1),("品質",88,4.4)],"specs":[("出力","140W（USB-C×3/USB-A×1）"),("USB-C単独","140W"),("USB-C×2","100W+40W"),("重量","265g"),("サイズ","W63×H63×D32mm"),("特徴","GaN III技術 / 4ポート同時充電")],"pros":["140WでMacBook Pro 16インチを急速充電","4ポート同時充電で家族全員分","8000円以下のコスパ","GaN IIIで小型・高効率","USB-C 140Wが最大出力"],"cons":["265gの重さ","コンセントが縦差しのため隣のコンセントを塞ぐ場合も","ブランド知名度がAnkerに劣る"],"desc":"4ポート×140WでMacBook・iPad・iPhone・AirPodsを一気に充電。充電器はこれ1台で完結できる最強品。","related":[("review-anker733","🔋","モバイルバッテリー","Anker 733 レビュー",4.7),("review-anker547","🔋","充電器","Anker 547 充電ステーション レビュー",4.6),("review-ciosmartcoby","🔋","充電器","CIO SMARTCOBY Pro レビュー",4.5)]},
    {"slug":"review-anker547","name":"Anker 547 Charging Station（6-in-1）","cat":"充電器","emoji":"🔋","price":"¥5,990","score":4.6,"bg":"#064e3b,#065f46","scores":[("ポート数",96,4.8),("コスパ",94,4.7),("利便性",92,4.6),("品質",90,4.5),("デザイン",84,4.2)],"specs":[("ポート","USB-A×3/USB-C×2/ACコンセント×1"),("最大出力","USB-C 65W"),("ケーブル長","1.5m"),("重量","290g"),("特徴","デスク用6in1電源タップ"),("認証","PSE適合")],"pros":["デスクのケーブル地獄を一掃","USB-C 65W+複数口で同時充電","6,000円以下の価格","1.5mのゆとりあるケーブル長","Ankerブランドの品質保証"],"cons":["持ち運びには向かない据え置き型","ACコンセントが1口のみ","USB-C最大65Wはやや控えめ"],"desc":"在宅ワークのデスクをスッキリ整理する6in1電源タップ。デスク周りのケーブル地獄を6,000円で解消。","related":[("review-ugreennexode140w","🔋","充電器","Ugreen Nexode 140W レビュー",4.5),("review-ciosmartcoby","🔋","充電器","CIO SMARTCOBY Pro レビュー",4.5),("review-anker733","🔋","モバイルバッテリー","Anker 733 レビュー",4.7)]},
    # ゲーミング
    {"slug":"review-nintendoswitch2","name":"Nintendo Switch 2","cat":"ゲーミング","emoji":"🎮","price":"¥49,980","score":4.8,"bg":"#7f1d1d,#991b1b","scores":[("ゲームライブラリ",98,4.9),("携帯性",96,4.8),("性能向上",90,4.5),("Joy-Con",92,4.6),("コスパ",86,4.3)],"specs":[("ディスプレイ","8インチ LCD 1080p"),("ドック出力","4K（アップスケール）"),("ストレージ","256GB（microSD拡張可）"),("バッテリー","2〜6.5時間"),("Joy-Con","マグネット接続 / マウス機能"),("特徴","GameChatボイスチャット機能")],"pros":["待望のNintendo Switch後継機","4Kアップスケール対応","Joy-Conのマグネット接続が快適","Nintendo独占タイトルが充実","前モデルとの一部互換性あり"],"cons":["4Kはネイティブでなくアップスケール","バッテリーが6.5時間止まり","価格が5万円と上昇","MicroSD規格が変更"],"desc":"待望のSwitch後継機がついに登場。4K×マグネットJoy-Con×256GBで次世代ゲーム体験へ。","related":[("review-ps5slim","🎮","ゲーミング","PlayStation 5 Slim レビュー",4.7),("review-xboxseriesx","🎮","ゲーミング","Xbox Series X レビュー",4.6),("review-metaquest3","🥽","VR/AR","Meta Quest 3 レビュー",4.7)]},
    {"slug":"review-ps5slim","name":"PlayStation 5 Slim（ディスクエディション）","cat":"ゲーミング","emoji":"🎮","price":"¥74,980","score":4.7,"bg":"#1e3a5f,#1e40af","scores":[("ゲーム性能",96,4.8),("独占タイトル",98,4.9),("コントローラー",96,4.8),("サイズ",86,4.3),("コスパ",82,4.1)],"specs":[("CPU","AMD Zen 2 3.5GHz"),("GPU","AMD RDNA 2 10.3TF"),("ストレージ","1TB SSD（NVMe）"),("映像","8K/4K 120fps対応"),("重量","3.2kg（旧型比30%減）"),("特徴","UHD Blu-ray / DualSense ワイヤレスコントローラー")],"pros":["DualSenseのハプティクスが革命的","4K 120fpsのゲーム体験","旧PS5比30%小型化","PlayStation独占タイトルが魅力","SSDの爆速ローディング"],"cons":["7.5万円の価格","専用TV/モニターが必要","Game Passほどのサービスがない"],"desc":"DualSenseの触覚フィードバックが他を圧倒するゲーム機。God of War・Spider-Manなど独占タイトルも魅力。","related":[("review-xboxseriesx","🎮","ゲーミング","Xbox Series X レビュー",4.6),("review-nintendoswitch2","🎮","ゲーミング","Nintendo Switch 2 レビュー",4.8),("review-logicoolGProXSuperlight2","🖱️","ゲーミング","G Pro X Superlight 2 レビュー",4.8)]},
    {"slug":"review-xboxseriesx","name":"Xbox Series X","cat":"ゲーミング","emoji":"🎮","price":"¥69,978","score":4.6,"bg":"#14532d,#15803d","scores":[("Game Pass",100,5.0),("性能",96,4.8),("後方互換",100,5.0),("独占タイトル",72,3.6),("コスパ",88,4.4)],"specs":[("CPU","AMD Zen 2 3.8GHz"),("GPU","AMD RDNA 2 12TF"),("ストレージ","1TB NVMe SSD"),("映像","8K/4K 120fps対応"),("重量","4.45kg"),("特徴","Xbox Game Pass / 後方互換 / Quick Resume")],"pros":["Game Passで月額費用でゲームし放題","12TFで業界最高水準の処理能力","Xbox One以降の後方互換が完全","Quick Resumeで瞬時に複数ゲーム切り替え","PCゲームとのクロスプレイが容易"],"cons":["PS5と比べ独占タイトルが少ない","7万円の価格","大きく重い4.45kg","縦置きのみ（横置きは公式非推奨）"],"desc":"Game Passという最強のサブスクで月額費用で最新ゲームし放題。性能も最高峰でコスパが突出している。","related":[("review-ps5slim","🎮","ゲーミング","PlayStation 5 Slim レビュー",4.7),("review-nintendoswitch2","🎮","ゲーミング","Nintendo Switch 2 レビュー",4.8),("review-elgatostreamdeck","🎮","ゲーミング","Elgato Stream Deck MK.2 レビュー",4.5)]},
    {"slug":"review-logicoolGProXSuperlight2","name":"Logicool G Pro X Superlight 2","cat":"ゲーミング","emoji":"🖱️","price":"¥19,800","score":4.8,"bg":"#1a0533,#3b0764","scores":[("軽量性",100,5.0),("センサー",100,5.0),("クリック感",96,4.8),("バッテリー",94,4.7),("コスパ",82,4.1)],"specs":[("重量","60g以下"),("センサー","HERO 2（最大32,000DPI）"),("接続","LIGHTSPEED ワイヤレス / USB有線"),("バッテリー","最大95時間"),("ポーリングレート","最大2000Hz"),("特徴","プロeスポーツ選手御用達")],"pros":["60g以下の超軽量で長時間疲れない","HERO 2センサーの精度が最高峰","95時間の長バッテリー","LIGHTSPEEDの安定した遅延なしワイヤレス","eスポーツプロが実際に使う信頼性"],"cons":["2万円の価格","サイドボタンが少ない","カスタマイズ性がロジクールの上位モデルに劣る"],"desc":"プロゲーマーが実際に使う60g以下の超軽量マウス。FPS・MOBAでの操作精度は他の追随を許さない。","related":[("review-razerdeathadder","🖱️","PC周辺機器","Razer DeathAdder V3 レビュー",4.6),("review-logicoolmxmaster3s","🖱️","PC周辺機器","Logicool MX Master 3S レビュー",4.8),("review-steelseriesarctisnova","🎧","ゲーミング","SteelSeries Arctis Nova Pro レビュー",4.7)]},
    {"slug":"review-steelseriesarctisnova","name":"SteelSeries Arctis Nova Pro Wireless","cat":"ゲーミング","emoji":"🎧","price":"¥38,980","score":4.7,"bg":"#0c4a6e,#075985","scores":[("音質",94,4.7),("マルチシステム",100,5.0),("ANC",88,4.4),("バッテリー",92,4.6),("コスパ",78,3.9)],"specs":[("ドライバー","40mmハイファイドライバー"),("ANC","アクティブノイズキャンセリング"),("接続","2.4GHz / Bluetooth / 有線"),("バッテリー","最大22時間（基地局交換可）"),("互換","PS5/PS4/PC/Switch/Mac"),("特徴","交換式バッテリーシステム")],"pros":["PS5・Xbox・PC・Switchを全部つなげる","交換バッテリーで実質無限稼働","Hi-Fiレベルの音質","ANCでゲーム没入度が増す","OLED搭載ベースステーションが便利"],"cons":["4万円の高価格","有線接続端子はPS5/Xboxで制限","重さ337g"],"desc":"PS5・Xbox・PC・Switchを1つのヘッドセットで切り替える究極の利便性。音質もHi-Fiクラスで妥協なし。","related":[("review-hyperxcloudalpha","🎧","ゲーミング","HyperX Cloud Alpha Wireless レビュー",4.5),("review-logicoolGProXSuperlight2","🖱️","ゲーミング","G Pro X Superlight 2 レビュー",4.8),("review-ps5slim","🎮","ゲーミング","PlayStation 5 Slim レビュー",4.7)]},
    {"slug":"review-elgatostreamdeck","name":"Elgato Stream Deck MK.2（15キー）","cat":"ゲーミング","emoji":"🎮","price":"¥18,980","score":4.5,"bg":"#312e81,#4338ca","scores":[("配信効率",100,5.0),("カスタマイズ",98,4.9),("使いやすさ",90,4.5),("コスパ",82,4.1),("品質",88,4.4)],"specs":[("キー数","15キー（LCD液晶ボタン）"),("接続","USB-A"),("ソフト","Stream Deck（無料）"),("互換","OBS / Twitch / YouTube / Discord等"),("カスタマイズ","アイコン・マクロ・フォルダ機能"),("対応OS","Windows / macOS")],"pros":["ワンタッチで配信切り替え・マクロ実行","LCDボタンでアイコンを自由にカスタマイズ","OBS・Discordなど主要ソフトと完璧連携","配信者・VTuberの生産性が劇的向上","プラグインエコシステムが豊富"],"cons":["2万円の価格","キーボードに慣れた人には必要性が薄い","ソフトがやや複雑"],"desc":"配信者・VTuber・動画編集者の生産性を劇的に変えるデバイス。ワンボタンで配信・カット・BGM切り替え。","related":[("review-blueyetix","🎙️","PC周辺機器","Blue Yeti X レビュー",4.6),("review-elgatocamlink4k","🖨️","PC周辺機器","Elgato Cam Link 4K レビュー",4.5),("review-xboxseriesx","🎮","ゲーミング","Xbox Series X レビュー",4.6)]},
    {"slug":"review-hyperxcloudalpha","name":"HyperX Cloud Alpha Wireless","cat":"ゲーミング","emoji":"🎧","price":"¥17,980","score":4.5,"bg":"#134e4a,#0f766e","scores":[("バッテリー",100,5.0),("音質",88,4.4),("コスパ",94,4.7),("装着感",86,4.3),("マイク",84,4.2)],"specs":[("ドライバー","50mmデュアルチャンバードライバー"),("バッテリー","最大300時間"),("接続","2.4GHz ワイヤレス"),("重量","335g"),("マイク","取り外し可能 Discord認定"),("互換","PC / PS5 / PS4")],"pros":["300時間の化け物バッテリー","デュアルチャンバーで低音が豊か","Discord認定マイク搭載","2万円以下のコスパ","取り外しマイクでヘッドフォンとしても使える"],"cons":["300Hz充電しないリスクで充電タイミングを忘れがち","Xbox非対応","重さ335g","Bluetooth非搭載"],"desc":"300時間バッテリーという常識外れのスタミナ。充電を忘れても絶対切れない最強ゲーミングヘッドセット。","related":[("review-steelseriesarctisnova","🎧","ゲーミング","SteelSeries Arctis Nova Pro レビュー",4.7),("review-sonywh1000xm5","🎧","PC周辺機器","Sony WH-1000XM5 レビュー",4.8),("review-logicoolGProXSuperlight2","🖱️","ゲーミング","G Pro X Superlight 2 レビュー",4.8)]},
    # PC周辺機器
    {"slug":"review-logicoolmxmaster3s","name":"Logicool MX Master 3S","cat":"PC周辺機器","emoji":"🖱️","price":"¥16,980","score":4.8,"bg":"#0c1445,#1e3a8a","scores":[("スクロール",100,5.0),("ボタン数",96,4.8),("エルゴノミクス",96,4.8),("マルチデバイス",94,4.7),("コスパ",84,4.2)],"specs":[("センサー","Darkfield 8,000DPI"),("接続","Bluetooth / Logi Bolt USB"),("バッテリー","最大70日"),("マルチペアリング","3台切り替え"),("特徴","MagSpeedスクロール / サムホイール"),("互換","Windows / macOS / Linux")],"pros":["MagSpeedスクロールが爆速かつ精密","3台デバイス切り替えがシームレス","エルゴノミクス形状で長時間でも疲れない","サムホイールで横スクロールが快適","静音クリックで集中できる"],"cons":["1.7万円の価格","左利き用モデルなし","重さ141g"],"desc":"テレワーカー・デザイナーが絶賛する最強マウス。MagSpeedスクロールを一度体験したら戻れない。","related":[("review-logicoolmxkeysmini","⌨️","PC周辺機器","Logicool MX Keys Mini レビュー",4.6),("review-keychronk2pro","⌨️","PC周辺機器","Keychron K2 Pro レビュー",4.7),("review-caldigitts4","🔌","PC周辺機器","CalDigit TS4 レビュー",4.7)]},
    {"slug":"review-keychronk2pro","name":"Keychron K2 Pro（RGBバックライト）","cat":"PC周辺機器","emoji":"⌨️","price":"¥18,700","score":4.7,"bg":"#1c1917,#44403c","scores":[("打鍵感",96,4.8),("ホットスワップ",100,5.0),("マルチOS",96,4.8),("コスパ",88,4.4),("デザイン",90,4.5)],"specs":[("キー数","84キー（テンキーレス）"),("スイッチ","ホットスワップ対応（Gateron G Pro等）"),("接続","Bluetooth 5.1 / USB-C"),("バックライト","RGBバックライト"),("対応OS","macOS / Windows / Android / iOS"),("特徴","アルミフレーム")],"pros":["スイッチをドライバーなしで交換可能","Mac/Windowsキー切り替えが簡単","アルミフレームで高級感","3台マルチペアリング対応","豊富なカラーとスイッチ選択肢"],"cons":["テンキーなしで数字入力が多い人には不向き","充電式でバッテリー切れのリスク","重さ800g台（アルミ製のため）"],"desc":"キーボードカスタマイズ入門に最高の一台。スイッチを交換しながら自分だけの打鍵感を追求できる。","related":[("review-logicoolmxmaster3s","🖱️","PC周辺機器","Logicool MX Master 3S レビュー",4.8),("review-logicoolmxkeysmini","⌨️","PC周辺機器","Logicool MX Keys Mini レビュー",4.6),("review-caldigitts4","🔌","PC周辺機器","CalDigit TS4 レビュー",4.7)]},
    {"slug":"review-sonywh1000xm5","name":"Sony WH-1000XM5","cat":"PC周辺機器","emoji":"🎧","price":"¥44,000","score":4.8,"bg":"#292524,#57534e","scores":[("ノイキャン",100,5.0),("音質",96,4.8),("バッテリー",94,4.7),("装着感",90,4.5),("コスパ",80,4.0)],"specs":[("ドライバー","30mm"),("ノイキャン","8マイクANC（業界最高水準）"),("再生時間","30時間（ANCオン）"),("急速充電","3分充電で3時間再生"),("コーデック","LDAC/AAC/SBC"),("接続","マルチポイント2台")],"pros":["業界最高のノイキャン性能","30時間×3分急速充電","LDACハイレゾ対応","折りたたみできてコンパクト収納","在宅ワークのフォーカス度が劇的向上"],"cons":["4.4万円の高価格","重さ250g（長時間で疲れる人も）","コーデック切り替えが少し面倒"],"desc":"ヘッドフォン型ANCの世界最高峰。在宅ワーク・飛行機・カフェどこでも無音の空間を作り出す。","related":[("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8),("review-boseqcearbuds2","🎧","ワイヤレスイヤホン","Bose QC Earbuds II レビュー",4.6),("review-sonywf1000xm5","🎧","ワイヤレスイヤホン","Sony WF-1000XM5 レビュー",4.7)]},
    {"slug":"review-logicoolmxkeysmini","name":"Logicool MX Keys Mini（バックライトあり）","cat":"PC周辺機器","emoji":"⌨️","price":"¥14,960","score":4.6,"bg":"#1e1b4b,#4338ca","scores":[("打鍵感",88,4.4),("マルチデバイス",96,4.8),("コンパクト",94,4.7),("バックライト",90,4.5),("コスパ",86,4.3)],"specs":[("キー数","78キー（テンキーレス）"),("接続","Bluetooth / Logi Bolt USB"),("バッテリー","最大10日（バックライト最大）/5ヶ月（バックライトオフ）"),("マルチペアリング","3台切り替え"),("特徴","近接センサーでバックライト自動点灯"),("対応OS","Windows / macOS / iOS / Android")],"pros":["テンキーレスで省スペース","3台切り替えがOne-Key Flow対応","近接センサーで電力節約","macOS/Windowsキー自動切替","1.5万円のコスパ"],"cons":["フルサイズに慣れた人はミスタイプ増える","充電式でバッテリー管理が必要","ファンクションキーが小さい"],"desc":"テンキーレスで省スペース×3台切り替えのテレワーク最強キーボード。MX Masterとセットが定番の組み合わせ。","related":[("review-keychronk2pro","⌨️","PC周辺機器","Keychron K2 Pro レビュー",4.7),("review-logicoolmxmaster3s","🖱️","PC周辺機器","Logicool MX Master 3S レビュー",4.8),("review-caldigitts4","🔌","PC周辺機器","CalDigit TS4 レビュー",4.7)]},
    {"slug":"review-blueyetix","name":"Blue Yeti X","cat":"PC周辺機器","emoji":"🎙️","price":"¥24,800","score":4.6,"bg":"#0c4a6e,#164e63","scores":[("音質",92,4.6),("使いやすさ",90,4.5),("機能性",90,4.5),("コスパ",84,4.2),("デザイン",88,4.4)],"specs":[("マイク","コンデンサーマイク"),("極性パターン","単一・双方向・全指向・ステレオ×4種"),("接続","USB-A"),("周波数特性","20Hz〜20kHz"),("特徴","リアルタイムメーターLEDインジケーター"),("重量","181g（ヘッドのみ）")],"pros":["4つの指性パターンで多用途","USB接続で手軽にプロ品質","リアルタイム入力レベルが一目でわかる","Logicool G HUBで詳細設定可能","YouTube・Podcast・会議すべてに対応"],"cons":["2.5万円の価格","デスクに置くスペースが必要","ハイエンドXLRマイクには音質で劣る"],"desc":"YouTuber・Podcast・ゲーム配信者の定番USBマイク。USB繋ぐだけで声が劇的に変わる入門の決定版。","related":[("review-elgatostreamdeck","🎮","ゲーミング","Elgato Stream Deck MK.2 レビュー",4.5),("review-elgatocamlink4k","🖨️","PC周辺機器","Elgato Cam Link 4K レビュー",4.5),("review-logicoolmxmaster3s","🖱️","PC周辺機器","Logicool MX Master 3S レビュー",4.8)]},
    {"slug":"review-caldigitts4","name":"CalDigit TS4（Thunderbolt 4ドック）","cat":"PC周辺機器","emoji":"🔌","price":"¥49,800","score":4.7,"bg":"#1a0533,#2e1065","scores":[("ポート数",100,5.0),("Thunderbolt性能",100,5.0),("MacBook連携",98,4.9),("価格",68,3.4),("コスパ",80,4.0)],"specs":[("接続","Thunderbolt 4 / USB4"),("ポート","合計18ポート（TB4×2/USB-C×2/USB-A×5等）"),("給電","98W MacBook給電対応"),("映像出力","最大2×8K / 1×8K+1×4K"),("Ethernet","2.5GbE"),("特徴","SDカードスロット搭載")],"pros":["18ポートでMacBookのハブ問題を完全解決","98W給電でMacBook Pro 16も充電可","2.5GbEで有線LAN高速化","Thunderbolt 4×2で8K出力可能","SDカードも読み込める"],"cons":["5万円の高価格","Thunderbolt PCのみ（USB-Cのみは機能制限）","電源アダプターが大きい"],"desc":"MacBook 1本繋ぐだけで18台のデバイスを接続できる最強ドック。デスク環境が完全に変わる。","related":[("review-logicoolmxmaster3s","🖱️","PC周辺機器","Logicool MX Master 3S レビュー",4.8),("review-keychronk2pro","⌨️","PC周辺機器","Keychron K2 Pro レビュー",4.7),("review-dellu2723d","🖥️","モニター","Dell U2723D レビュー",4.7)]},
    {"slug":"review-samsungt9ssd","name":"Samsung T9 外付けSSD 4TB","cat":"PC周辺機器","emoji":"💾","price":"¥54,800","score":4.7,"bg":"#1a0533,#312e81","scores":[("転送速度",100,5.0),("容量",96,4.8),("耐久性",90,4.5),("コンパクト",88,4.4),("コスパ",80,4.0)],"specs":[("容量","4TB"),("転送速度","読込2,000MB/s / 書込2,000MB/s"),("接続","USB 3.2 Gen 2×2"),("耐衝撃","3m落下耐性"),("重量","98g"),("特徴","AES 256bit暗号化")],"pros":["2,000MB/sの爆速転送で4K動画編集が快適","4TBの大容量","98gの超コンパクト","3m落下耐性の堅牢設計","AES暗号化でセキュリティ安心"],"cons":["5.5万円の高価格","USB 3.2 Gen 2×2ケーブルが普及していない","発熱がやや多い"],"desc":"プロカメラマン・映像クリエイターが使う外付けSSDの最速機。4K素材の転送をストレスゼロにする。","related":[("review-wdmypassport5tb","💾","PC周辺機器","WD My Passport 5TB レビュー",4.4),("review-caldigitts4","🔌","PC周辺機器","CalDigit TS4 レビュー",4.7),("review-macbookprom4pro","💻","ノートPC","MacBook Pro M4 Pro レビュー",4.9)]},
    {"slug":"review-wdmypassport5tb","name":"WD My Passport 5TB","cat":"PC周辺機器","emoji":"💾","price":"¥18,800","score":4.4,"bg":"#1c1917,#44403c","scores":[("容量",98,4.9),("コスパ",94,4.7),("信頼性",88,4.4),("速度",72,3.6),("携帯性",86,4.3)],"specs":[("容量","5TB"),("転送速度","読込約120MB/s（HDD）"),("接続","USB-C / USB-A"),("重量","210g"),("暗号化","256bit AES"),("特徴","3年保証")],"pros":["5TBの大容量で2万円以下","コスパが圧倒的","WDの信頼性が高い","3年保証で安心","USB-C接続に対応"],"cons":["HDD型なので衝撃に弱い","転送速度がSSDに劣る","210gで少し重め","振動音がある"],"desc":"写真・動画・バックアップに最適な大容量外付けHDD。2万円以下で5TBは他に選択肢がない。","related":[("review-samsungt9ssd","💾","PC周辺機器","Samsung T9 SSD レビュー",4.7),("review-caldigitts4","🔌","PC周辺機器","CalDigit TS4 レビュー",4.7),("review-logicoolmxmaster3s","🖱️","PC周辺機器","Logicool MX Master 3S レビュー",4.8)]},
    {"slug":"review-razerdeathadder","name":"Razer DeathAdder V3 HyperSpeed","cat":"PC周辺機器","emoji":"🖱️","price":"¥9,980","score":4.6,"bg":"#0c4a6e,#164e63","scores":[("軽量性",90,4.5),("センサー",92,4.6),("コスパ",96,4.8),("デザイン",88,4.4),("バッテリー",90,4.5)],"specs":[("重量","64g"),("センサー","Focus X（最大18,000DPI）"),("接続","HyperSpeed ワイヤレス"),("バッテリー","最大200時間"),("ポーリングレート","最大1000Hz"),("特徴","エルゴノミクスデザイン")],"pros":["64gの軽量×エルゴノミクス形状","1万円以下のコスパ","200時間の超長バッテリー","HyperSpeedの安定ワイヤレス","長時間ゲームでも疲れにくい"],"cons":["センサーはG Pro X Superlightに劣る","左利き非対応","1000Hzまで（競技用は2000Hz以上がある）"],"desc":"1万円以下で買えるエルゴノミクスワイヤレスマウス。200時間バッテリーと快適な持ち心地で長時間ゲームに最適。","related":[("review-logicoolGProXSuperlight2","🖱️","ゲーミング","G Pro X Superlight 2 レビュー",4.8),("review-logicoolmxmaster3s","🖱️","PC周辺機器","Logicool MX Master 3S レビュー",4.8),("review-steelseriesarctisnova","🎧","ゲーミング","SteelSeries Arctis Nova Pro レビュー",4.7)]},
    {"slug":"review-elgatocamlink4k","name":"Elgato Cam Link 4K","cat":"PC周辺機器","emoji":"🖨️","price":"¥19,800","score":4.5,"bg":"#312e81,#4c1d95","scores":[("互換性",96,4.8),("画質",90,4.5),("使いやすさ",90,4.5),("コスパ",84,4.2),("遅延",86,4.3)],"specs":[("入力","HDMI（4K 30fps / 1080p 60fps）"),("接続","USB-A 3.0"),("対応OS","Windows / macOS"),("遅延","超低遅延"),("重量","17g"),("特徴","DSLR/ミラーレス/ビデオカメラ接続対応")],"pros":["一眼・ビデオカメラをWebカメラ化","4K 30fps/1080p 60fps対応","超軽量17gで邪魔にならない","OBS / Zoom / Teams完全対応","プラグ＆プレイで設定不要"],"cons":["2万円の価格","映像入力のみ（音声は別途設定）","4K 30fps（60fps非対応）"],"desc":"会議・配信の映像品質を一眼レフレベルに引き上げる17gのデバイス。一度試したら戻れないクオリティ差。","related":[("review-blueyetix","🎙️","PC周辺機器","Blue Yeti X レビュー",4.6),("review-elgatostreamdeck","🎮","ゲーミング","Elgato Stream Deck MK.2 レビュー",4.5),("review-sonyzve10ii","📸","カメラ","Sony ZV-E10 II レビュー",4.8)]},
    # スマートホーム・その他
    {"slug":"review-metaquest3","name":"Meta Quest 3（128GB）","cat":"VR/AR","emoji":"🥽","price":"¥74,800","score":4.7,"bg":"#1e1b4b,#312e81","scores":[("MR体験",100,5.0),("性能",92,4.6),("コンテンツ",88,4.4),("装着感",84,4.2),("コスパ",84,4.2)],"specs":[("CPU/GPU","Snapdragon XR2 Gen 2"),("解像度","2064×2208（片眼）"),("リフレッシュレート","最大120Hz"),("視野角","110°水平/96°垂直"),("重量","515g"),("特徴","カラーパス スルーMR / Touchコントローラー")],"pros":["現実とVRが融合する混合現実（MR）体験","Quest 2比2倍以上の処理能力","PCなしでスタンドアローン動作","Meta Horizon Worldsのコンテンツが充実","価格が競合より安い"],"cons":["515gの重さで長時間使用は疲れる","バッテリーが2〜3時間","高品質コンテンツはまだ少ない","ソーシャルアカウント必要"],"desc":"現実とバーチャルが融合するMRの入門機として最高。家がゲームフィールドになる体験は一度したら忘れられない。","related":[("review-nintendoswitch2","🎮","ゲーミング","Nintendo Switch 2 レビュー",4.8),("review-ps5slim","🎮","ゲーミング","PlayStation 5 Slim レビュー",4.7),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},
    {"slug":"review-kindlepaperwhite","name":"Kindle Paperwhite 第11世代（16GB）","cat":"電子書籍リーダー","emoji":"📖","price":"¥19,980","score":4.6,"bg":"#134e4a,#0f766e","scores":[("読書体験",98,4.9),("バッテリー",96,4.8),("目への優しさ",96,4.8),("コスパ",92,4.6),("防水",88,4.4)],"specs":[("ディスプレイ","6.8インチ 300ppi E-Ink"),("防水","IPX8（水深2m 60分）"),("ストレージ","8GB/16GB"),("バッテリー","最大10週間"),("重量","205g"),("特徴","フロントライト・ウォームライト搭載")],"pros":["10週間バッテリーで充電を忘れられる","300ppiの目に優しいE-Inkディスプレイ","IPX8防水でお風呂で読書可","フロントライトで夜間読書も快適","2万円以下のコスパ"],"cons":["カラー表示非対応","ページ送りに微妙なコントラスト変化","AmazonのKindle本専用（他書店は制限あり）"],"desc":"読書専用デバイスの最高峰。スマホで読むとは別次元の集中力と目への優しさを10週間バッテリーで実現。","related":[("review-ipadmini7","📟","タブレット","iPad mini 7 レビュー",4.4),("review-firemax11","📟","タブレット","Amazon Fire Max 11 レビュー",3.9),("review-applehomedpodmini","🔊","スマートスピーカー","Apple HomePod mini レビュー",4.4)]},
    {"slug":"review-applehomedpodmini","name":"Apple HomePod mini 第2世代","cat":"スマートスピーカー","emoji":"🔊","price":"¥12,800","score":4.4,"bg":"#1a1a2e,#16213e","scores":[("Appleエコシステム",100,5.0),("音質",86,4.3),("スマートホーム",90,4.5),("コスパ",88,4.4),("サイズ",96,4.8)],"specs":[("チップ","S5"),("スピーカー","360°全方位スピーカー"),("接続","Wi-Fi / Bluetooth / Thread"),("対応","Siri / HomeKit / Matter / Ultra Wideband"),("重量","345g"),("特徴","iPhone近づけるだけで接続切替")],"pros":["Appleデバイスとのシームレス連携","Matter対応でスマートホーム拡張性大","Ultra Widebandで空間オーディオ体験","1.3万円の低価格","インテリアに馴染むコンパクトデザイン"],"cons":["AndroidではSiri機能が制限される","音量が大きい部屋には物足りない","Apple専用エコシステムに依存"],"desc":"iPhoneユーザーのスマートホーム入門として最高。1.3万円でAppleの全デバイスを音声でコントロール。","related":[("review-amazonechoshow10","🔊","スマートスピーカー","Amazon Echo Show 10 レビュー",4.3),("review-philipshue","💡","スマートホーム","Philips Hue スターターキット レビュー",4.3),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},
    {"slug":"review-amazonechoshow10","name":"Amazon Echo Show 10（第3世代）","cat":"スマートスピーカー","emoji":"🔊","price":"¥32,980","score":4.3,"bg":"#0c4a6e,#0369a1","scores":[("Alexa機能",96,4.8),("自動追尾",96,4.8),("Amazon連携",98,4.9),("音質",80,4.0),("コスパ",76,3.8)],"specs":[("ディスプレイ","10.1インチ HD"),("スピーカー","1インチツィーター+3インチウーファー"),("カメラ","13MPオートフレーミング"),("回転","自動追尾で±175°回転"),("接続","Wi-Fi / Bluetooth / Zigbee"),("特徴","Fire TV内蔵 / ビデオ通話対応")],"pros":["自動追尾カメラが顔を常に中心に捉える","Alexa×Amazonエコシステムが最強","Fire TVで動画視聴もできる","スマートホームの司令塔として優秀","ビデオ通話がハンズフリーで快適"],"cons":["3.3万円の高価格","追尾機能が気持ち悪いと感じる人も","音質はHi-Fiとはいえない","Alexa以外のアシスタント非対応"],"desc":"自動でカメラが追いかけてくる先進スマートスピーカー。ビデオ会議・料理・スマートホーム操作のハブに。","related":[("review-applehomedpodmini","🔊","スマートスピーカー","Apple HomePod mini レビュー",4.4),("review-philipshue","💡","スマートホーム","Philips Hue スターターキット レビュー",4.3),("review-eufyrobovacx8","🤖","家電","Anker Eufy RoboVac X8 レビュー",4.4)]},
    {"slug":"review-dysonv15","name":"Dyson V15 Detect（コードレス）","cat":"家電","emoji":"🧹","price":"¥99,800","score":4.5,"bg":"#1c1917,#292524","scores":[("吸引力",98,4.9),("レーザー検知",100,5.0),("バッテリー",84,4.2),("使いやすさ",86,4.3),("コスパ",72,3.6)],"specs":[("吸引力","最大230AW"),("レーザー","グリーンレーザーでホコリ可視化"),("センサー","ゴミ量自動表示（LCD）"),("バッテリー","最大60分（省電力モード）"),("重量","3.1kg"),("特徴","HEPA H13フィルター")],"pros":["レーザーで見えなかったホコリが見えて衝撃","ゴミ量センサーで掃除完了を判断できる","最大230AWの超強力吸引","HEPA H13フィルターでアレルゲン除去","ヘッドが自動でパワー調整"],"cons":["10万円の超高価格","3.1kgの重さ","最大60分バッテリーは短め（強モードは20分）","本体価格以外にアタッチメントが高額"],"desc":"レーザーで見えないホコリを可視化する衝撃機能。一度使ったら他の掃除機では満足できない最強コードレス。","related":[("review-eufyrobovacx8","🤖","家電","Anker Eufy RoboVac X8 レビュー",4.4),("review-applehomedpodmini","🔊","スマートスピーカー","Apple HomePod mini レビュー",4.4),("review-philipshue","💡","スマートホーム","Philips Hue スターターキット レビュー",4.3)]},
    {"slug":"review-eufyrobovacx8","name":"Anker Eufy RoboVac X8 Hybrid","cat":"家電","emoji":"🤖","price":"¥49,800","score":4.4,"bg":"#431407,#7c2d12","scores":[("AI障害物回避",94,4.7),("吸引力",90,4.5),("マッピング",88,4.4),("コスパ",88,4.4),("水拭き",84,4.2)],"specs":[("吸引力","2,000Pa（デュアルターボ）"),("AI","iPath レーザーナビゲーション"),("障害物回避","AIによる靴・コード・家具の自動回避"),("バッテリー","最大180分"),("水拭き","電動マイクロファイバーモップ"),("対応アプリ","EufyHome")],"pros":["AIが障害物を自動回避（靴・ケーブルOK）","デュアルターボで強力吸引","水拭き同時対応","スマートマッピングで部屋別設定","5万円以下のコスパ"],"cons":["高価格な障害物がある場合は引っかかることも","水タンクが小さめ","動作音がやや大きい"],"desc":"ケーブルも靴も自動回避するAI搭載ロボット掃除機。帰ってきたら床がキレイになっている快適な生活へ。","related":[("review-dysonv15","🧹","家電","Dyson V15 Detect レビュー",4.5),("review-applehomedpodmini","🔊","スマートスピーカー","Apple HomePod mini レビュー",4.4),("review-philipshue","💡","スマートホーム","Philips Hue スターターキット レビュー",4.3)]},
    {"slug":"review-appletv4k","name":"Apple TV 4K 第3世代（Wi-Fi）","cat":"エンタメ","emoji":"📺","price":"¥19,800","score":4.5,"bg":"#1e3a5f,#2563eb","scores":[("Apple連携",100,5.0),("画質",94,4.7),("アプリ",86,4.3),("音質",90,4.5),("コスパ",86,4.3)],"specs":[("チップ","A15 Bionic"),("解像度","4K / Dolby Vision / HDR10+"),("音声","Dolby Atmos"),("接続","Wi-Fi 6 / Bluetooth 5.0 / HDMI 2.1"),("リモコン","Siri Remote（タッチパッド）"),("特徴","AirPlay / Thread / HomeKit")],"pros":["A15 Bionicで動作が爆速","Dolby Vision×Dolby Atmosの最高画質・音質","AirPlayでiPhoneの映像を瞬時に出力","HomeKit対応デバイスをTV画面で管理","Siri Remoteが使いやすい"],"cons":["2万円（Fire StickやChromecastより高い）","Disney+・Hulu等の一部機能でiOS依存","ゲームタイトルはPS5/Switchに劣る"],"desc":"Appleデバイスを持つ家庭のリビングに最適なストリーミングデバイス。Dolby Vision×Atmosで映像体験を最高に。","related":[("review-metaquest3","🥽","VR/AR","Meta Quest 3 レビュー",4.7),("review-applehomedpodmini","🔊","スマートスピーカー","Apple HomePod mini レビュー",4.4),("review-ps5slim","🎮","ゲーミング","PlayStation 5 Slim レビュー",4.7)]},
    {"slug":"review-sonysrsxb43","name":"Sony SRS-XB43","cat":"スピーカー","emoji":"🔊","price":"¥22,000","score":4.5,"bg":"#14532d,#166534","scores":[("音質",90,4.5),("防水",96,4.8),("バッテリー",92,4.6),("EXTRA BASS",98,4.9),("コスパ",88,4.4)],"specs":[("出力","35W"),("防水","IP67"),("バッテリー","最大24時間"),("接続","Bluetooth 5.0 / NFC"),("特徴","EXTRA BASS / ライティング機能"),("重量","1,380g")],"pros":["IP67防水でアウトドア最強","EXTRA BASSの重低音が最強","24時間バッテリー","NFC接続が便利","パーティーライティング搭載"],"cons":["1.4kgの重さ","音質はピュアオーディオ派には物足りない","Bluetoothのみ（Wi-Fi非対応）"],"desc":"キャンプ・BBQ・海水浴の最強パートナー。IP67防水×24時間×EXTRA BASSで外でも最高の音楽体験を。","related":[("review-soundcorex600","🔊","スピーカー","Anker Soundcore Motion X600 レビュー",4.6),("review-applehomedpodmini","🔊","スマートスピーカー","Apple HomePod mini レビュー",4.4),("review-dysonv15","🧹","家電","Dyson V15 Detect レビュー",4.5)]},
    {"slug":"review-soundcorex600","name":"Anker Soundcore Motion X600","cat":"スピーカー","emoji":"🔊","price":"¥16,990","score":4.6,"bg":"#0c4a6e,#0369a1","scores":[("空間オーディオ",98,4.9),("音質",88,4.4),("防水",92,4.6),("バッテリー",88,4.4),("コスパ",92,4.6)],"specs":[("出力","50W"),("空間オーディオ","対応"),("防水","IPX7"),("バッテリー","最大12時間"),("接続","Bluetooth 5.3"),("重量","1,640g")],"pros":["空間オーディオ対応で音が立体的","50W×IPX7で防水高出力","1.7万円のコスパ","USB-C充電対応","Soundcoreアプリでイコライザー調整"],"cons":["1.6kgの重さ","最大12時間のバッテリーはSonyより短い","空間オーディオ効果が慣れるまで不自然に感じることも"],"desc":"空間オーディオ対応×50W高出力で1.7万円というコスパ最強ポータブルスピーカー。音が360度に広がる体験を。","related":[("review-sonysrsxb43","🔊","スピーカー","Sony SRS-XB43 レビュー",4.5),("review-applehomedpodmini","🔊","スマートスピーカー","Apple HomePod mini レビュー",4.4),("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8)]},
    {"slug":"review-philipshue","name":"Philips Hue スターターキット（E26 ×3+ブリッジ）","cat":"スマートホーム","emoji":"💡","price":"¥19,800","score":4.3,"bg":"#1e1b4b,#3730a3","scores":[("スマートホーム連携",100,5.0),("エンタメ連携",96,4.8),("使いやすさ",84,4.2),("コスパ",72,3.6),("品質",90,4.5)],"specs":[("電球","E26スマート電球×3個"),("明るさ","最大800lm"),("色温度","2200K〜6500K"),("接続","Zigbee（ブリッジ経由）/ Bluetooth"),("互換","Alexa / Google / Siri / HomeKit / Matter"),("特徴","1600万色フルカラー対応")],"pros":["映画・音楽・ゲームに照明が同期（Hue Sync）","1600万色のフルカラー演出","全主要スマートホームと連携","スマートホーム入門として最適","アプリで細かいシーン設定が可能"],"cons":["2万円の初期投資が高め","ブリッジが必要でセットアップが少し手間","電球1個が高価（2,500円〜）"],"desc":"部屋の照明が映画に合わせて変わる感動体験。Philips Hueはスマートホームの中でも特に生活の質を高める投資。","related":[("review-applehomedpodmini","🔊","スマートスピーカー","Apple HomePod mini レビュー",4.4),("review-amazonechoshow10","🔊","スマートスピーカー","Amazon Echo Show 10 レビュー",4.3),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},

    # テレビ
    {"slug":"review-sonybraviaA95L","name":"Sony BRAVIA XR A95L 65インチ","cat":"テレビ","emoji":"📺","price":"¥550,000","score":4.9,"bg":"#0f172a,#1e3a5f","scores":[("画質",100,5.0),("音質",96,4.8),("輝度",94,4.7),("デザイン",96,4.8),("コスパ",72,3.6)],"specs":[("パネル","QD-OLED（量子ドットOLED）"),("解像度","4K HDR（Cognitive Processor XR）"),("音声","Acoustic Surface Audio+"),("OS","Google TV"),("HDMI","HDMI 2.1×4"),("消費電力","240W")],"pros":["QD-OLEDで色域・輝度が有機EL最高峰","Acoustic Surface Audioで画面から音が出る感覚","Google TVで主要アプリ全対応","PS5と相性抜群（HDMI 2.1×4）","圧倒的な黒の締まりと発色"],"cons":["55万円の超高価格","有機ELで焼き付きリスク","輝度がミニLEDに劣る場面あり"],"desc":"QD-OLEDの頂点。映画館を超えると言われる色再現と音響が1台に。PS5・シネマ用途で予算を惜しまない人の最終解答。","related":[("review-lgoledevoC4","📺","テレビ","LG OLED evo C4 レビュー",4.8),("review-samsungneo95D","📺","テレビ","Samsung Neo QLED QN95D レビュー",4.7),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},
    {"slug":"review-lgoledevoC4","name":"LG OLED evo C4 65インチ","cat":"テレビ","emoji":"📺","price":"¥330,000","score":4.8,"bg":"#0c1445,#1a237e","scores":[("画質",98,4.9),("ゲーム対応",100,5.0),("音質",88,4.4),("デザイン",92,4.6),("コスパ",82,4.1)],"specs":[("パネル","OLED evo（α9 AI Processor Gen7）"),("解像度","4K 120Hz Dolby Vision"),("ゲーム","VRR / G-Sync / FreeSync / ALLM"),("OS","webOS 24"),("HDMI","HDMI 2.1×4"),("入力遅延","1ms（ゲームモード）")],"pros":["HDMI2.1×4でPS5+PC同時接続","1ms入力遅延でゲームが超快適","Dolby Vision IQで映画が劇場級","webOSが使いやすい","有機ELの完全な黒"],"cons":["33万円","有機ELで焼き付きリスク","音質はサウンドバー別途推奨"],"desc":"ゲーマーとシネマファン両方の最適解。HDMI2.1×4は世界最多クラス。PCモニター代わりにも使える夢のパネル。","related":[("review-sonybraviaA95L","📺","テレビ","Sony BRAVIA XR A95L レビュー",4.9),("review-samsungneo95D","📺","テレビ","Samsung Neo QLED QN95D レビュー",4.7),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},
    {"slug":"review-samsungneo95D","name":"Samsung Neo QLED QN95D 65インチ","cat":"テレビ","emoji":"📺","price":"¥360,000","score":4.7,"bg":"#1a1a2e,#3949ab","scores":[("輝度",100,5.0),("画質",96,4.8),("音質",90,4.5),("明るい部屋",100,5.0),("コスパ",78,3.9)],"specs":[("パネル","Neo QLED（Mini LED）"),("輝度","最大4,000nits"),("解像度","4K 144Hz"),("音声","Dolby Atmos OTS+"),("OS","Tizen"),("特徴","Anti-Reflection コーティング")],"pros":["4000nitsの圧倒的輝度で昼間も鮮明","Mini LEDで局所調光が精密","144Hzでゲームも映像も滑らか","Anti-Reflectionコートで映り込みゼロ","Dolby Atmos OTS+で音が上下から"],"cons":["有機ELより黒の締まりは劣る","36万円","HDMI2.1は2ポートのみ"],"desc":"明るい部屋での視聴に限れば世界最強クラス。4000nitsの輝度はHDRコンテンツを圧倒的な体験に変える。","related":[("review-lgoledevoC4","📺","テレビ","LG OLED evo C4 レビュー",4.8),("review-sonybraviaA95L","📺","テレビ","Sony BRAVIA XR A95L レビュー",4.9),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},
    {"slug":"review-sonybravia7","name":"Sony BRAVIA 7 65インチ","cat":"テレビ","emoji":"📺","price":"¥220,000","score":4.6,"bg":"#1e293b,#334155","scores":[("画質",92,4.6),("輝度",96,4.8),("音質",90,4.5),("コスパ",88,4.4),("スマート機能",90,4.5)],"specs":[("パネル","Mini LED（XR Backlight Master Drive）"),("解像度","4K 120Hz"),("音声","Acoustic Multi-Audio"),("OS","Google TV"),("HDMI","HDMI 2.1×2"),("輝度","約1,300nits")],"pros":["XRプロセッサで自然な色再現","Mini LEDで高コントラスト","Google TVで操作が直感的","22万円のコスパ","Acoustic Multi-Audioで音場が広い"],"cons":["HDMI2.1が2ポート","OLEDには黒の締まりで劣る","輝度はQN95Dに劣る"],"desc":"SONYの画質哲学をMini LEDで22万円に凝縮。XRプロセッサの自然な映像処理はAI処理と一線を画す上質さ。","related":[("review-lgoledevoC4","📺","テレビ","LG OLED evo C4 レビュー",4.8),("review-samsungneo95D","📺","テレビ","Samsung Neo QLED QN95D レビュー",4.7),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},
    {"slug":"review-tcl575qm891","name":"TCL QM891G 55インチ","cat":"テレビ","emoji":"📺","price":"¥130,000","score":4.4,"bg":"#1b5e20,#2e7d32","scores":[("コスパ",100,5.0),("画質",88,4.4),("輝度",90,4.5),("音質",80,4.0),("スマート機能",86,4.3)],"specs":[("パネル","Mini LED QLED"),("輝度","最大2,000nits"),("解像度","4K 144Hz"),("OS","Google TV"),("HDMI","HDMI 2.1×2"),("特徴","Dolby Vision / HDR10+")],"pros":["13万円でMini QLED 144Hz","2000nitsの高輝度","Google TV搭載","Dolby Vision対応","PS5・PCゲームに最適な144Hz"],"cons":["音質が平凡でサウンドバー必須","ローカル調光精度は上位機に劣る","ブランド認知度が低い"],"desc":"中国メーカーが放つコスパ最強Mini QLED。13万円でMini LED・2000nits・144Hzを実現。音質だけ妥協できるなら最強の選択。","related":[("review-hisenseu8n","📺","テレビ","Hisense U8N レビュー",4.4),("review-lgoledevoC4","📺","テレビ","LG OLED evo C4 レビュー",4.8),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},
    {"slug":"review-hisenseu8n","name":"Hisense U8N 65インチ","cat":"テレビ","emoji":"📺","price":"¥150,000","score":4.4,"bg":"#004d40,#00695c","scores":[("コスパ",100,5.0),("輝度",96,4.8),("画質",86,4.3),("音質",82,4.1),("スマート機能",84,4.2)],"specs":[("パネル","Mini LED ULED"),("輝度","最大3,000nits"),("解像度","4K 144Hz"),("OS","VIDAA U7"),("HDMI","HDMI 2.1×2"),("特徴","144Hz / Dolby Vision IQ")],"pros":["15万円で3000nitsはコスパ異常","144Hz対応でゲーム用途にも","Dolby Vision IQ対応","国内で増えているハイセンスサポート","独自チップで映像処理が向上"],"cons":["VIDAA OSが使いにくい","HDMI2.1が2ポート","音質は別途サウンドバー推奨"],"desc":"15万円で3000nitsというコスパが話題。輝度重視なら国産メーカーの2〜3倍の価値がある。ゲームや明るい部屋に最適。","related":[("review-tcl575qm891","📺","テレビ","TCL QM891G レビュー",4.4),("review-lgoledevoC4","📺","テレビ","LG OLED evo C4 レビュー",4.8),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},
    # ドライヤー
    {"slug":"review-dysonsupersonichd15","name":"Dyson Supersonic r HD15","cat":"ドライヤー","emoji":"💨","price":"¥79,800","score":4.8,"bg":"#7c2d12,#9a3412","scores":[("速乾性",96,4.8),("ヘアダメージ",100,5.0),("デザイン",100,5.0),("静音性",90,4.5),("コスパ",68,3.4)],"specs":[("モーター","Dyson V9 デジタルモーター（110,000rpm）"),("温度制御","41℃×40回/秒センシング"),("重量","659g"),("騒音","79dB"),("付属品","磁気ノズル×5"),("特徴","Air Multiplier技術")],"pros":["温度を40回/秒制御でダメージゼロ","磁気アタッチメントで瞬時切替","業界最小クラスのモーター","セット後の仕上がりがサロン級","カラーバリエーションが豊富"],"cons":["8万円の高価格","659gとやや重い","乾燥速度は他社大風量に劣る場合も"],"desc":"毛髪ダメージの心配から解放される革命的ドライヤー。温度制御技術は他社と次元が違う。一度使うと戻れない。","related":[("review-panasonicnanoeEH-NA0J","💨","ドライヤー","Panasonic EH-NA0J レビュー",4.6),("review-reprizer4dplus","💨","ドライヤー","レプロナイザー 4D Plus レビュー",4.5),("review-refadryerpro","💨","ドライヤー","ReFa BEAUTECH DRYER PRO レビュー",4.6)]},
    {"slug":"review-panasonicnanoeEH-NA0J","name":"Panasonic ナノケア EH-NA0J","cat":"ドライヤー","emoji":"💨","price":"¥29,800","score":4.6,"bg":"#1e3a5f,#1565c0","scores":[("ナノイー効果",98,4.9),("速乾性",90,4.5),("静音性",92,4.6),("コスパ",90,4.5),("使いやすさ",92,4.6)],"specs":[("風量","1.3m³/分"),("特徴","ナノイー × ミネラル"),("温度","温冷リズム送風"),("重量","612g"),("騒音","68dB（静音モード）"),("ノズル","速乾ノズル付")],"pros":["ナノイー×ミネラルで髪がしっとり","68dBの静音モード（夜間使用可）","3万円のコスパ","温冷リズム送風でキューティクルを整える","軽量612gで腕が疲れにくい"],"cons":["Dysonより速乾性が劣る","大風量モードは騒音あり","ナノイー効果は実感に個人差"],"desc":"ナノイーで髪をケアしながら乾かす3万円の優等生。静音モードは深夜使用でも家族に迷惑をかけない設計。","related":[("review-dysonsupersonichd15","💨","ドライヤー","Dyson Supersonic r HD15 レビュー",4.8),("review-refadryerpro","💨","ドライヤー","ReFa BEAUTECH DRYER PRO レビュー",4.6),("review-reprizer4dplus","💨","ドライヤー","レプロナイザー 4D Plus レビュー",4.5)]},
    {"slug":"review-refadryerpro","name":"ReFa BEAUTECH DRYER PRO","cat":"ドライヤー","emoji":"💨","price":"¥55,000","score":4.6,"bg":"#4a1942,#6a1b4d","scores":[("美髪効果",96,4.8),("速乾性",94,4.7),("デザイン",98,4.9),("静音性",88,4.4),("コスパ",76,3.8)],"specs":[("特徴","プラズマイオン×温感ミスト"),("風量","2.1m³/分（大風量）"),("重量","570g"),("騒音","75dB"),("モード","プラズマイオン / スカルプ / ドライ"),("カラー","クリスタルブラック / パールホワイト")],"pros":["プラズマイオン×温感ミストで艶髪","業界トップクラスの2.1m³/分風量","570gの軽量","デザインがスタイリッシュでインテリアになる","速乾とケアを両立"],"cons":["5.5万円の高価格","Dysonほどの温度制御精度はない","修理対応が国内限定"],"desc":"速乾×美髪×デザインの三拍子を揃えた女性向けプレミアムドライヤー。お風呂上がりのルーティンが楽しくなる一台。","related":[("review-dysonsupersonichd15","💨","ドライヤー","Dyson Supersonic r HD15 レビュー",4.8),("review-panasonicnanoeEH-NA0J","💨","ドライヤー","Panasonic EH-NA0J レビュー",4.6),("review-reprizer4dplus","💨","ドライヤー","レプロナイザー 4D Plus レビュー",4.5)]},
    {"slug":"review-reprizer4dplus","name":"レプロナイザー 4D Plus","cat":"ドライヤー","emoji":"💨","price":"¥68,000","score":4.5,"bg":"#1a1a2e,#16213e","scores":[("バイオプログラミング",100,5.0),("仕上がり",96,4.8),("速乾性",80,4.0),("コスパ",64,3.2),("使いやすさ",82,4.1)],"specs":[("技術","バイオプログラミング テクノロジー"),("重量","590g"),("特徴","細胞活性化による艶・ツヤ"),("温度","60〜130℃"),("付属品","なし"),("生産","日本製")],"pros":["美容師・モデルが愛用するほどの仕上がり","バイオプログラミングで細胞レベルのケア","日本製の品質","使うたびに髪が改善されていく実感","縮毛・広がりが抑制される"],"cons":["6.8万円の超高価格","見た目は普通のドライヤー","効果に科学的根拠を求める人には不向き","速乾性は普通"],"desc":"美容師が自腹で買うドライヤー。バイオプログラミング技術の効果は使い続けるほど実感できる。本物の美髪を求める人への投資。","related":[("review-dysonsupersonichd15","💨","ドライヤー","Dyson Supersonic r HD15 レビュー",4.8),("review-refadryerpro","💨","ドライヤー","ReFa BEAUTECH DRYER PRO レビュー",4.6),("review-panasonicnanoeEH-NA0J","💨","ドライヤー","Panasonic EH-NA0J レビュー",4.6)]},
    # 電動歯ブラシ
    {"slug":"review-oralbioS9","name":"Oral-B iO Series 9","cat":"電動歯ブラシ","emoji":"🪥","price":"¥49,800","score":4.7,"bg":"#0d47a1,#1565c0","scores":[("磨き性能",98,4.9),("AIガイド",100,5.0),("デザイン",96,4.8),("バッテリー",88,4.4),("コスパ",76,3.8)],"specs":[("モーション","マイクロバイブレーション（12,000回/分）"),("AI","AIコーチングアプリ連携"),("充電","14日間（1回充電）"),("重量","168g"),("モード","7種類"),("特徴","プレッシャーコントロール・磨き残しマップ")],"pros":["AIが磨き残し箇所をスマホにマッピング","プレッシャーセンサーで歯茎へのダメージゼロ","7つのモードで歯石・ホワイトニング対応","14日バッテリーで旅行も安心","歯科医推奨ブランドNo.1"],"cons":["5万円の高価格","替えブラシが高い（約2,000円/個）","アプリ必須で端末が必要"],"desc":"歯医者に通う回数が減ると口コミで話題。AIが磨き残しをマップ化することで完璧なブラッシングを実現する最高峰電動歯ブラシ。","related":[("review-philipssonicare9900","🪥","電動歯ブラシ","Philips Sonicare 9900 Prestige レビュー",4.6),("review-panasonicDoltzEWDP51","🪥","電動歯ブラシ","Panasonic Doltz EW-DP51 レビュー",4.5),("review-oralbioS7","🪥","電動歯ブラシ","Oral-B iO Series 7 レビュー",4.4)]},
    {"slug":"review-philipssonicare9900","name":"Philips Sonicare 9900 Prestige","cat":"電動歯ブラシ","emoji":"🪥","price":"¥54,780","score":4.6,"bg":"#4a148c,#6a1b9a","scores":[("音波振動",98,4.9),("アプリ連携",94,4.7),("デザイン",90,4.5),("バッテリー",92,4.6),("コスパ",72,3.6)],"specs":[("振動数","62,000回/分（音波振動）"),("特徴","SenseIQ・プレッシャーセンサー"),("充電","3週間（1回充電）"),("重量","150g"),("モード","4種類＋3段階強度"),("連携","Philips Sonicare アプリ")],"pros":["62,000回/分の音波振動が歯周ポケットまで届く","SenseIQが自動で振動強度を最適化","3週間充電不要","150gの軽量","歯科医評価が高い"],"cons":["5.5万円","替えブラシが高い","振動が強く感じる人もいる"],"desc":"音波歯ブラシの最高峰。毎分62,000回の音波がプロクリーニング並みの洗浄力を自宅で実現。3週間充電不要も旅行者に嬉しい。","related":[("review-oralbioS9","🪥","電動歯ブラシ","Oral-B iO Series 9 レビュー",4.7),("review-panasonicDoltzEWDP51","🪥","電動歯ブラシ","Panasonic Doltz EW-DP51 レビュー",4.5),("review-oralbioS7","🪥","電動歯ブラシ","Oral-B iO Series 7 レビュー",4.4)]},
    {"slug":"review-panasonicDoltzEWDP51","name":"Panasonic Doltz EW-DP51","cat":"電動歯ブラシ","emoji":"🪥","price":"¥22,000","score":4.5,"bg":"#1565c0,#1976d2","scores":[("コスパ",96,4.8),("磨き性能",90,4.5),("防水",94,4.7),("使いやすさ",92,4.6),("バッテリー",88,4.4)],"specs":[("振動","超音波＋音波 W振動"),("防水","IPX7"),("充電","約10日間"),("重量","160g"),("特徴","舌クリーナー・歯間ケアノズル付"),("モード","4種類")],"pros":["2.2万円のコスパ","IPX7防水でシャワー中も使用可","舌クリーナー付きで口臭ケアまで","ダブル振動で歯面と歯茎を同時ケア","国内メーカーの安心感"],"cons":["国際的なブランド力はiO・Sonicareに劣る","アプリ連携非対応","替えブラシの入手しやすさ"],"desc":"国産コスパ電動歯ブラシの最高峰。舌クリーナー付きの2.2万円は口腔ケア全般をカバーする優れた設計。毎日使いたい。","related":[("review-oralbioS9","🪥","電動歯ブラシ","Oral-B iO Series 9 レビュー",4.7),("review-philipssonicare9900","🪥","電動歯ブラシ","Philips Sonicare 9900 Prestige レビュー",4.6),("review-oralbioS7","🪥","電動歯ブラシ","Oral-B iO Series 7 レビュー",4.4)]},
    {"slug":"review-oralbioS7","name":"Oral-B iO Series 7","cat":"電動歯ブラシ","emoji":"🪥","price":"¥29,800","score":4.4,"bg":"#006064,#00838f","scores":[("磨き性能",92,4.6),("コスパ",86,4.3),("AIガイド",88,4.4),("デザイン",88,4.4),("バッテリー",84,4.2)],"specs":[("モーション","マイクロバイブレーション"),("AI","カラーセンサーでプレッシャー検知"),("充電","2週間"),("重量","165g"),("モード","5種類"),("特徴","iO Senseアプリ対応")],"pros":["3万円でiOシリーズのAI機能","プレッシャーカラーセンサー搭載","Series 9より2万円安い","2週間バッテリー","7つのブラッシングモードは5に絞り使いやすい"],"cons":["磨き残しマップはSeries 9に劣る","替えブラシコストは同じ","Series 9との差を感じる人も"],"desc":"iOシリーズのコスパ版。Series 9の80%の機能を60%の価格で実現。初めてiOシリーズを試すなら最適なエントリーモデル。","related":[("review-oralbioS9","🪥","電動歯ブラシ","Oral-B iO Series 9 レビュー",4.7),("review-philipssonicare9900","🪥","電動歯ブラシ","Philips Sonicare 9900 Prestige レビュー",4.6),("review-panasonicDoltzEWDP51","🪥","電動歯ブラシ","Panasonic Doltz EW-DP51 レビュー",4.5)]},
    # シェーバー
    {"slug":"review-panasoniclamdash9x","name":"Panasonic ラムダッシュ PRO ES-LS9AX","cat":"シェーバー","emoji":"🪒","price":"¥59,800","score":4.8,"bg":"#1a237e,#283593","scores":[("剃り心地",100,5.0),("肌への優しさ",96,4.8),("洗浄機能",98,4.9),("バッテリー",90,4.5),("コスパ",78,3.9)],"specs":[("刃","6枚刃（直線＋曲線ヘッド）"),("洗浄","全自動洗浄充電器付"),("防水","IPX7"),("充電","60分フル充電（45分使用）"),("特徴","リニアモーター駆動×52,000ストローク/分"),("重量","175g")],"pros":["52,000ストローク/分のリニアモーターが剃り残しゼロ","6枚刃で顔の凹凸に追従","全自動洗浄機付属でメンテ不要","IPX7で風呂剃り可","肌への負担が圧倒的に少ない"],"cons":["6万円","替刃が高い（約7,000円）","充電時間が60分"],"desc":"電気シェーバーの最高峰。リニアモーターの52,000ストロークは剃り残しゼロを実現。肌が弱い男性への最高の投資。","related":[("review-braunseries9pro","🪒","シェーバー","Braun Series 9 Pro レビュー",4.7),("review-philips9000prestige","🪒","シェーバー","Philips S9000 Prestige レビュー",4.6),("review-panasoniclamdash5x","🪒","シェーバー","Panasonic ラムダッシュ ES-LV67 レビュー",4.4)]},
    {"slug":"review-braunseries9pro","name":"Braun Series 9 Pro 9477cc","cat":"シェーバー","emoji":"🪒","price":"¥45,800","score":4.7,"bg":"#212121,#424242","scores":[("剃り心地",96,4.8),("多方向対応",100,5.0),("洗浄機能",96,4.8),("バッテリー",92,4.6),("コスパ",82,4.1)],"specs":[("刃","5刃（ProGlide刃×2）"),("洗浄","全自動洗浄充電器（5アクション）"),("防水","IPX7"),("充電","1時間フル充電（60分使用）"),("特徴","10方向フレックスヘッド"),("重量","161g")],"pros":["10方向に動くフレックスヘッドが顔の輪郭に完全追従","ProGlide刃でフラットな毛を捉える","全自動洗浄充電器が5段階洗浄","161gの軽さ","世界的なシェーバーブランドの信頼"],"cons":["替刃が非常に高い（約8,000円）","ラムダッシュより剃り心地は好みによる","洗浄液の消耗コスト"],"desc":"欧米で絶大な支持を誇るBraunの最高峰。10方向フレックスヘッドの追従性は剃り残しを限りなくゼロに近づける。","related":[("review-panasoniclamdash9x","🪒","シェーバー","Panasonic ラムダッシュ PRO ES-LS9AX レビュー",4.8),("review-philips9000prestige","🪒","シェーバー","Philips S9000 Prestige レビュー",4.6),("review-panasoniclamdash5x","🪒","シェーバー","Panasonic ラムダッシュ ES-LV67 レビュー",4.4)]},
    {"slug":"review-philips9000prestige","name":"Philips S9000 Prestige SP9883","cat":"シェーバー","emoji":"🪒","price":"¥38,800","score":4.6,"bg":"#0d47a1,#1976d2","scores":[("コスパ",88,4.4),("剃り心地",92,4.6),("肌感知",96,4.8),("バッテリー",88,4.4),("使いやすさ",92,4.6)],"specs":[("刃","V-Track刃×3"),("センサー","SkinIQ（肌状態感知）"),("防水","IPX7"),("充電","1時間（60分使用）"),("特徴","自動パワー調整×角度追従"),("重量","202g")],"pros":["SkinIQが肌状態をリアルタイム感知","V-Track刃で寝た毛・短い毛を捉える","3.9万円のコスパ","IPX7防水","肌への刺激が最小限"],"cons":["202gとやや重い","Panasonic・Braunより剃り心地は好みによる","替刃コスト"],"desc":"肌感知テクノロジーで敏感肌を守るPhilipsの最高峰。SkinIQが肌を読み取り自動でパワーを調整。肌荒れしやすい人に最適。","related":[("review-panasoniclamdash9x","🪒","シェーバー","Panasonic ラムダッシュ PRO ES-LS9AX レビュー",4.8),("review-braunseries9pro","🪒","シェーバー","Braun Series 9 Pro レビュー",4.7),("review-panasoniclamdash5x","🪒","シェーバー","Panasonic ラムダッシュ ES-LV67 レビュー",4.4)]},
    {"slug":"review-panasoniclamdash5x","name":"Panasonic ラムダッシュ ES-LV67","cat":"シェーバー","emoji":"🪒","price":"¥22,800","score":4.4,"bg":"#1b5e20,#2e7d32","scores":[("コスパ",96,4.8),("剃り心地",88,4.4),("防水",94,4.7),("バッテリー",88,4.4),("使いやすさ",90,4.5)],"specs":[("刃","5枚刃"),("防水","IPX7"),("充電","1時間"),("特徴","全方位密着5枚刃 / お風呂剃り対応"),("重量","185g"),("バッテリー","45分使用")],"pros":["2.3万円でラムダッシュ5枚刃","IPX7防水でシャワー中使用可","剃り残しが少ない","パナソニックの安心品質","コンパクトで旅行にも"],"cons":["洗浄充電器なし（別売）","9xシリーズよりリニアモーター非搭載","替刃コスト"],"desc":"コスパで選ぶならこれ一択。2.3万円でラムダッシュブランドの5枚刃剃りを毎朝楽しめる。まずシェーバーを試したい人に。","related":[("review-panasoniclamdash9x","🪒","シェーバー","Panasonic ラムダッシュ PRO ES-LS9AX レビュー",4.8),("review-braunseries9pro","🪒","シェーバー","Braun Series 9 Pro レビュー",4.7),("review-philips9000prestige","🪒","シェーバー","Philips S9000 Prestige レビュー",4.6)]},
    # ロボット掃除機
    {"slug":"review-roborocks8maxv","name":"Roborock S8 MaxV Ultra","cat":"ロボット掃除機","emoji":"🤖","price":"¥189,800","score":4.9,"bg":"#1a1a2e,#16213e","scores":[("障害物回避",100,5.0),("吸引力",100,5.0),("水拭き",98,4.9),("自動ドック",100,5.0),("コスパ",72,3.6)],"specs":[("吸引力","10,000Pa"),("カメラ","RGB+構造光3Dカメラ"),("水拭き","振動モップ×2（フロアタイプ自動判別）"),("ドック","自動給水・排水・洗浄・ゴミ収集"),("マッピング","3Dマップ生成"),("特徴","ペット・ケーブル・靴まで認識回避")],"pros":["10,000Paの業界最高吸引力","3Dカメラが糞・ケーブル・靴を認識回避","全自動ドックで水補充・排水・モップ洗浄まで","振動モップ2基で磨き掃除","3Dマップで家具・部屋を学習"],"cons":["19万円の超高価格","ドック本体が大きい","高価格製品でサポートが重要"],"desc":"ロボット掃除機の完全到達点。10,000Paの吸引力と3Dカメラの障害物認識、全自動ドックを組み合わせた未来の家電。掃除から完全解放される。","related":[("review-iroombaj9plus","🤖","ロボット掃除機","iRobot Roomba j9+ レビュー",4.7),("review-ecovacsX5pro","🤖","ロボット掃除機","Ecovacs Deebot X5 Pro レビュー",4.6),("review-dreameX40ultra","🤖","ロボット掃除機","Dreame X40 Ultra レビュー",4.7)]},
    {"slug":"review-iroombaj9plus","name":"iRobot Roomba j9+","cat":"ロボット掃除機","emoji":"🤖","price":"¥119,800","score":4.7,"bg":"#0a0a0a,#1a1a2a","scores":[("AIナビゲーション",96,4.8),("吸引力",90,4.5),("自動ゴミ収集",98,4.9),("ペット対応",100,5.0),("コスパ",76,3.8)],"specs":[("吸引力","100倍（比Roomba 600シリーズ）"),("カメラ","PrecisionVision Navigation"),("ドック","Clean Base（60日分ゴミ収集）"),("特徴","Pet Owner Official Product"),("マッピング","3D Reactive AI"),("バッテリー","最大75分")],"pros":["ペットの毛に特化した設計（ペット認定製品）","60日分ゴミを自動収集するClean Base","PrecisionVisionがペット排泄物を自動回避","家の学習精度が高い","iRobotの10年以上の信頼"],"cons":["12万円","吸引力のスペックはRoborockに劣る","水拭き機能がない"],"desc":"ペットを飼っている家庭の最終解答。ペット認定製品として排泄物まで認識・回避。60日自動収集でごみ捨て月2回だけ。","related":[("review-roborocks8maxv","🤖","ロボット掃除機","Roborock S8 MaxV Ultra レビュー",4.9),("review-dreameX40ultra","🤖","ロボット掃除機","Dreame X40 Ultra レビュー",4.7),("review-ecovacsX5pro","🤖","ロボット掃除機","Ecovacs Deebot X5 Pro レビュー",4.6)]},
    {"slug":"review-dreameX40ultra","name":"Dreame X40 Ultra","cat":"ロボット掃除機","emoji":"🤖","price":"¥159,800","score":4.7,"bg":"#3e2723,#4e342e","scores":[("吸引力",100,5.0),("水拭き",96,4.8),("障害物回避",96,4.8),("自動ドック",98,4.9),("コスパ",78,3.9)],"specs":[("吸引力","12,000Pa（業界最高水準）"),("水拭き","回転モップ（カーペット自動リフト）"),("ドック","全自動（給排水・乾燥・ゴミ収集）"),("カメラ","3Dセンサー＋RGB"),("特徴","カーペット上でモップ自動リフトアップ"),("マッピング","高精度LiDARマッピング")],"pros":["12,000Pa業界最高吸引力","カーペットを検知してモップを自動リフト","全自動ドックでモップ乾燥まで","16万円でRoborock S8 MaxVと互角以上","LiDARマッピングで精度が高い"],"cons":["16万円","Dreameのサポート体制","ドックが大きい"],"desc":"Roborockと並ぶロボット掃除機最高峰。12,000Paの吸引力とカーペット自動リフト機能は他を圧倒する。全自動で家が常にキレイ。","related":[("review-roborocks8maxv","🤖","ロボット掃除機","Roborock S8 MaxV Ultra レビュー",4.9),("review-iroombaj9plus","🤖","ロボット掃除機","iRobot Roomba j9+ レビュー",4.7),("review-ecovacsX5pro","🤖","ロボット掃除機","Ecovacs Deebot X5 Pro レビュー",4.6)]},
    {"slug":"review-ecovacsX5pro","name":"Ecovacs Deebot X5 Pro Omni","cat":"ロボット掃除機","emoji":"🤖","price":"¥139,800","score":4.6,"bg":"#006064,#00838f","scores":[("AI認識",94,4.7),("吸引力",92,4.6),("水拭き",94,4.7),("コスパ",84,4.2),("ナビゲーション",92,4.6)],"specs":[("吸引力","8,200Pa"),("AI","AIVI 3Dでリアルタイム障害物認識"),("水拭き","OZMO Turbo 2.0（高速回転モップ）"),("ドック","Omni Station（5in1全自動）"),("マッピング","TrueMapping 2.0"),("特徴","声でコントロール（Alexa/Google）")],"pros":["AIVI 3DでAIが障害物をリアルタイム認識","OZMO Turbo 2.0の高速モップが強力","Omni Stationが5つの機能を全自動","TrueMapping 2.0で精密ナビ","Alexa・Google対応"],"cons":["14万円","Roborockに吸引力で劣る","アプリの日本語対応が不完全な場合あり"],"desc":"AI認識技術のエコバックスが放つ全自動ロボット掃除機。AIVI 3Dが靴・おもちゃを認識しながら家全体を自動清掃。","related":[("review-roborocks8maxv","🤖","ロボット掃除機","Roborock S8 MaxV Ultra レビュー",4.9),("review-dreameX40ultra","🤖","ロボット掃除機","Dreame X40 Ultra レビュー",4.7),("review-iroombaj9plus","🤖","ロボット掃除機","iRobot Roomba j9+ レビュー",4.7)]},
    # コーヒーメーカー
    {"slug":"review-delonghimagnificaevo","name":"De'Longhi マグニフィカ エボ ECAM29051B","cat":"コーヒーメーカー","emoji":"☕","price":"¥99,800","score":4.7,"bg":"#3e2723,#4e342e","scores":[("エスプレッソ品質",96,4.8),("使いやすさ",92,4.6),("コスパ",84,4.2),("豆→カップ速度",94,4.7),("メンテナンス",90,4.5)],"specs":[("方式","全自動エスプレッソマシン"),("グラインダー","コニカル刃グラインダー13段階"),("圧力","15気圧"),("容量","タンク1.8L / 豆ホッパー250g"),("特徴","ラテクレマシステム / スチームノズル"),("重量","9.5kg")],"pros":["豆を入れてボタン一つでカフェラテが完成","13段階グラインドで豆の個性を引き出す","15気圧で本格エスプレッソ","スチームノズルでラテアートも可能","10万円でフルオート本格派"],"cons":["10万円の初期投資","9.5kgの重さ","定期的なクリーニングが必要（15〜20分）"],"desc":"毎朝カフェに行く必要がなくなるフルオートマシン。豆から1分でカフェラテが完成する幸せを1日何杯でも。10万円の元を1年で取れる。","related":[("review-nespressovertutenext","☕","コーヒーメーカー","Nespresso Vertuo Next レビュー",4.4),("review-sirocaSCC111","☕","コーヒーメーカー","シロカ SC-C111 レビュー",4.3),("review-panasonicNC-A57","☕","コーヒーメーカー","Panasonic NC-A57 レビュー",4.4)]},
    {"slug":"review-nespressovertutenext","name":"Nespresso Vertuo Next","cat":"コーヒーメーカー","emoji":"☕","price":"¥16,500","score":4.4,"bg":"#1b5e20,#2e7d32","scores":[("手軽さ",100,5.0),("コスパ",86,4.3),("カップサイズ",98,4.9),("片付け",94,4.7),("コーヒー品質",86,4.3)],"specs":[("方式","カプセル式"),("特徴","Centrifusion技術（バーコード自動認識）"),("サイズ","エスプレッソ〜カラフェ（40ml〜535ml）"),("接続","Wi-Fi / Bluetooth"),("重量","3.8kg"),("特徴","リサイクルカプセル対応")],"pros":["ボタン1つで最適な抽出を自動設定","エスプレッソから大容量カラフェまで対応","1.7万円の低価格","コンパクトで置き場所を選ばない","Nespresso公式リサイクル対応"],"cons":["カプセルコストが高い（1杯約100〜150円）","フル自動機と比べてコーヒー品質は劣る","カプセル在庫管理が必要"],"desc":"忙しい朝の最強パートナー。バーコード読み取りで最適抽出を自動化。1杯30秒で本格コーヒーが飲める手軽さが最大の魅力。","related":[("review-delonghimagnificaevo","☕","コーヒーメーカー","De'Longhi マグニフィカ エボ レビュー",4.7),("review-sirocaSCC111","☕","コーヒーメーカー","シロカ SC-C111 レビュー",4.3),("review-panasonicNC-A57","☕","コーヒーメーカー","Panasonic NC-A57 レビュー",4.4)]},
    {"slug":"review-sirocaSCC111","name":"シロカ 全自動コーヒーメーカー SC-C111","cat":"コーヒーメーカー","emoji":"☕","price":"¥19,800","score":4.3,"bg":"#263238,#37474f","scores":[("コスパ",100,5.0),("使いやすさ",90,4.5),("豆対応",86,4.3),("保温",80,4.0),("静音性",78,3.9)],"specs":[("方式","全自動（豆・粉対応）"),("グラインダー","コーン式5段階"),("容量","最大4杯"),("特徴","コンパクト全自動 / ドリップ式"),("重量","2.9kg"),("フィルター","ペーパー・ステンレスメッシュ両対応")],"pros":["2万円以下のコスパ全自動","豆・粉両対応で使い方が自由","コンパクト2.9kgでキッチンに馴染む","ステンレスメッシュフィルター付属","豆の粗さ5段階調整"],"cons":["4杯まで（大家族には物足りない）","抽出圧力はエスプレッソマシンに大幅に劣る","保温機能が短め"],"desc":"2万円で豆から全自動という衝撃のコスパ。毎朝挽きたてのコーヒーを楽しむ生活への敷居を最低限に下げた国民的マシン。","related":[("review-delonghimagnificaevo","☕","コーヒーメーカー","De'Longhi マグニフィカ エボ レビュー",4.7),("review-nespressovertutenext","☕","コーヒーメーカー","Nespresso Vertuo Next レビュー",4.4),("review-panasonicNC-A57","☕","コーヒーメーカー","Panasonic NC-A57 レビュー",4.4)]},
    {"slug":"review-panasonicNC-A57","name":"Panasonic 全自動コーヒーメーカー NC-A57","cat":"コーヒーメーカー","emoji":"☕","price":"¥29,800","score":4.4,"bg":"#1a237e,#283593","scores":[("豆挽き品質",92,4.6),("コスパ",90,4.5),("機能性",88,4.4),("使いやすさ",90,4.5),("デザイン",84,4.2)],"specs":[("方式","全自動（豆・粉対応）"),("グラインダー","コーン式"),("容量","最大5杯"),("特徴","ミル性能が高くアイスコーヒーにも対応"),("保温","ステンレスサーバー"),("重量","3.2kg")],"pros":["ステンレスサーバーで保温が長持ち","5杯対応で家族向け","アイスコーヒーモード搭載","パナソニックの安心品質","豆挽きの精度がシロカより高い"],"cons":["3万円","デザインが地味","SC-C111より高いが機能差が伝わりにくい"],"desc":"シロカより一段上の全自動コーヒーメーカー。ステンレスサーバーの保温力と豆挽き精度でコーヒーの質が上がる。家族で飲む人に最適。","related":[("review-delonghimagnificaevo","☕","コーヒーメーカー","De'Longhi マグニフィカ エボ レビュー",4.7),("review-nespressovertutenext","☕","コーヒーメーカー","Nespresso Vertuo Next レビュー",4.4),("review-sirocaSCC111","☕","コーヒーメーカー","シロカ SC-C111 レビュー",4.3)]},
    # プロジェクター
    {"slug":"review-xgimihorizonultra","name":"XGIMI HORIZON Ultra","cat":"プロジェクター","emoji":"📽️","price":"¥259,800","score":4.7,"bg":"#0d47a1,#1565c0","scores":[("4K画質",98,4.9),("明るさ",96,4.8),("HDR",100,5.0),("Android TV",92,4.6),("コスパ",78,3.9)],"specs":[("解像度","4K UHD（DLP）"),("輝度","2,300 ISOルーメン"),("HDR","Dolby Vision / HDR10+"),("OS","Android TV 11"),("スピーカー","Harman Kardon×2（20W）"),("特徴","ISA 3.0（自動補正）")],"pros":["4K Dolby Visionが自宅シアターを超える","ISA 3.0で台形補正・フォーカス・障害物回避を自動化","Harman Kardon 20Wスピーカー内蔵","Android TV 11でNetflixも直接視聴","2,300ルーメンで明るい部屋でも見やすい"],"cons":["26万円","ランプ寿命管理が必要","真っ暗な部屋が理想"],"desc":"自宅に映画館を作る夢を現実にするフラグシップ4Kプロジェクター。Dolby Visionの映像×Harman Kardonの音で映画体験が革命的に変わる。","related":[("review-ankernebulacosmos4k","📽️","プロジェクター","Anker Nebula Cosmos Laser 4K レビュー",4.5),("review-benqw2720i","📽️","プロジェクター","BenQ W2720i レビュー",4.5),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},
    {"slug":"review-ankernebulacosmos4k","name":"Anker Nebula Cosmos Laser 4K","cat":"プロジェクター","emoji":"📽️","price":"¥139,800","score":4.5,"bg":"#1a1a2e,#2d2d5e","scores":[("コスパ",94,4.7),("4K画質",90,4.5),("明るさ",88,4.4),("Android TV",90,4.5),("レーザー寿命",96,4.8)],"specs":[("解像度","4K UHD（レーザー光源）"),("輝度","2,200 ANSIルーメン"),("レーザー寿命","25,000時間"),("OS","Android TV 10"),("スピーカー","40W Dolby Audio"),("特徴","ISA（自動セットアップ）")],"pros":["レーザー光源で25,000時間（ランプ交換不要）","14万円でレーザー4Kの圧倒的コスパ","2,200ルーメンで明るい部屋でも視聴可","40W Dolby Audioスピーカー内蔵","Android TVでストリーミング直接対応"],"cons":["XGIMI HORIZON Ultraより画質が劣る","14万円でもコスパ基準で見ると高い","重量が重め（4.2kg）"],"desc":"レーザー光源×4Kを14万円で実現したAnkerの傑作。25,000時間のランプ寿命で10年以上使える。映画・スポーツ・ゲームを大画面で楽しみたい人へ。","related":[("review-xgimihorizonultra","📽️","プロジェクター","XGIMI HORIZON Ultra レビュー",4.7),("review-benqw2720i","📽️","プロジェクター","BenQ W2720i レビュー",4.5),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},
    {"slug":"review-benqw2720i","name":"BenQ W2720i","cat":"プロジェクター","emoji":"📽️","price":"¥99,800","score":4.5,"bg":"#0f4c75,#1b6ca8","scores":[("コスパ",96,4.8),("4K画質",90,4.5),("明るさ",86,4.3),("設置のしやすさ",90,4.5),("スマート機能",84,4.2)],"specs":[("解像度","4K UHD（DLP）"),("輝度","2,000 ISOルーメン"),("HDR","HDR10 / HLG"),("OS","Android TV 11"),("スピーカー","5W×2"),("特徴","1.3倍ズーム / ±30°縦台形補正")],"pros":["10万円4KプロジェクターでBenQの信頼","Android TV 11内蔵","1.3倍光学ズームで設置場所の柔軟性","±30°台形補正","BenQのシネマカラー技術"],"cons":["内蔵スピーカーが5Wで音は別途推奨","レーザーではないためランプ寿命あり","暗い部屋専用"],"desc":"10万円で4Kシネマを自宅に。BenQのシネマカラー技術が色再現性を保証。設置場所を選ばない1.3倍ズームと台形補正で賃貸でも安心。","related":[("review-xgimihorizonultra","📽️","プロジェクター","XGIMI HORIZON Ultra レビュー",4.7),("review-ankernebulacosmos4k","📽️","プロジェクター","Anker Nebula Cosmos Laser 4K レビュー",4.5),("review-appletv4k","📺","エンタメ","Apple TV 4K レビュー",4.5)]},
    # サウンドバー
    {"slug":"review-sonyHTA7000","name":"Sony HT-A7000","cat":"サウンドバー","emoji":"🔊","price":"¥159,800","score":4.8,"bg":"#1a1a2e,#16213e","scores":[("音質",98,4.9),("Dolby Atmos",100,5.0),("デザイン",96,4.8),("接続性",96,4.8),("コスパ",76,3.8)],"specs":[("チャンネル","7.1.2ch"),("出力","500W"),("対応フォーマット","Dolby Atmos / DTS:X / 360 Reality Audio"),("HDMI","eARC / 4K HDR Pass Through"),("特徴","Vertical Surround Engine / S-Force PRO"),("Bluetooth","LDAC対応")],"pros":["7.1.2chで天井から音が降ってくる立体音場","LDAC対応で高音質Bluetooth","Sony BRAVIA TVとの完璧な連携","360 Reality Audio対応","別売りリアスピーカーで9.1.4chまで拡張可能"],"cons":["16万円","設置スペースが必要","BRAVIA以外のTVとの相性は普通"],"desc":"Dolby Atmosの立体音場がリビングを映画館に変える。Sony BRAVIA TVとのXRサウンド連携は唯一無二。音に投資するなら最終解答。","related":[("review-samsungHWQ990D","🔊","サウンドバー","Samsung HW-Q990D レビュー",4.7),("review-sonosarcUltra","🔊","サウンドバー","Sonos Arc Ultra レビュー",4.8),("review-boseSmartSoundbar900","🔊","サウンドバー","Bose Smart Soundbar 900 レビュー",4.6)]},
    {"slug":"review-sonosarcUltra","name":"Sonos Arc Ultra","cat":"サウンドバー","emoji":"🔊","price":"¥139,800","score":4.8,"bg":"#212121,#424242","scores":[("音質",100,5.0),("Dolby Atmos",98,4.9),("マルチルーム",100,5.0),("デザイン",96,4.8),("コスパ",78,3.9)],"specs":[("チャンネル","7.0.4ch（サウンドバー単体）"),("ドライバー","14個（ツィーター・ウーファー・高音域）"),("対応フォーマット","Dolby Atmos / DTS:X"),("接続","HDMI eARC / Wi-Fi / Bluetooth"),("特徴","Sonos S2エコシステム / Trueplay音調整"),("音場補正","自動音場補正（Trueplay）")],"pros":["14個のドライバーが単体で7.0.4ch空間を実現","Trueplayが部屋の形状に自動最適化","Sonosエコシステムで家中マルチルーム音楽","HDMI eARCでTVと1本接続","サウンドバー最高水準の音質"],"cons":["14万円","Sonosアプリに依存","Wi-Fi接続必須でBluetoothのみは制限あり"],"desc":"サウンドバー界の最高峰。14個ドライバーが作り出す空間音場は現実を超える。Sonosエコシステムで家全体が一つのオーディオに。","related":[("review-sonyHTA7000","🔊","サウンドバー","Sony HT-A7000 レビュー",4.8),("review-samsungHWQ990D","🔊","サウンドバー","Samsung HW-Q990D レビュー",4.7),("review-boseSmartSoundbar900","🔊","サウンドバー","Bose Smart Soundbar 900 レビュー",4.6)]},
    {"slug":"review-samsungHWQ990D","name":"Samsung HW-Q990D","cat":"サウンドバー","emoji":"🔊","price":"¥189,800","score":4.7,"bg":"#1a237e,#283593","scores":[("チャンネル数",100,5.0),("Dolby Atmos",98,4.9),("ワイヤレスリア",100,5.0),("音質",96,4.8),("コスパ",70,3.5)],"specs":[("チャンネル","11.1.4ch"),("構成","サウンドバー+ワイヤレスリア+ワイヤレスサブウーファー"),("出力","656W"),("対応","Dolby Atmos / DTS:X / Q-Symphony"),("接続","HDMI eARC 2.1"),("特徴","SpaceFit Sound+")],"pros":["11.1.4chが家庭用で業界最大","ワイヤレスリアスピーカー付属で設置が簡単","656W出力","Samsung TV とのQ-Symphony完全連携","SpaceFit Soundが部屋を自動解析"],"cons":["19万円の超高価格","Samsung TVでないとQ-Symphonyが使えない","置き場所がリアスピーカー分必要"],"desc":"家庭用11.1.4chで映画館の立体音響を完全再現。ワイヤレスリア付属で設置の手間ゼロ。Samsung TVユーザーの最終到達点。","related":[("review-sonyHTA7000","🔊","サウンドバー","Sony HT-A7000 レビュー",4.8),("review-sonosarcUltra","🔊","サウンドバー","Sonos Arc Ultra レビュー",4.8),("review-boseSmartSoundbar900","🔊","サウンドバー","Bose Smart Soundbar 900 レビュー",4.6)]},
    {"slug":"review-boseSmartSoundbar900","name":"Bose Smart Soundbar 900","cat":"サウンドバー","emoji":"🔊","price":"¥98,800","score":4.6,"bg":"#1b5e20,#2e7d32","scores":[("音質",94,4.7),("Dolby Atmos",92,4.6),("コスパ",84,4.2),("デザイン",96,4.8),("使いやすさ",92,4.6)],"specs":[("チャンネル","5.0.2ch"),("ドライバー","PhaseGuide × 5"),("対応","Dolby Atmos / DTS:X"),("接続","HDMI eARC / Wi-Fi / Bluetooth / AirPlay 2"),("特徴","TrueSpace（仮想サラウンド）"),("音声アシスタント","Alexa / Google / Apple Siri")],"pros":["AirPlay 2対応でiPhoneから即接続","PhaseGuideが広い音場を演出","Alexa内蔵でスマートホーム操作","スリムなデザインでTVの邪魔にならない","10万円以下のコスパ"],"cons":["リアスピーカー別売り","Sonosほどのエコシステムはない","低音は別途サブウーファー推奨"],"desc":"Boseの音作りとAirPlay 2・Alexa対応を10万円以下で。スリムなデザインとAppleエコシステムとの親和性がiPhoneユーザーに最適。","related":[("review-sonosarcUltra","🔊","サウンドバー","Sonos Arc Ultra レビュー",4.8),("review-sonyHTA7000","🔊","サウンドバー","Sony HT-A7000 レビュー",4.8),("review-samsungHWQ990D","🔊","サウンドバー","Samsung HW-Q990D レビュー",4.7)]},
    # ネットワーク機器
    {"slug":"review-tplinkdecoXE75pro","name":"TP-Link Deco XE75 Pro","cat":"ネットワーク機器","emoji":"📡","price":"¥49,800","score":4.6,"bg":"#1b5e20,#33691e","scores":[("Wi-Fi速度",96,4.8),("メッシュ安定性",94,4.7),("コスパ",90,4.5),("設置のしやすさ",94,4.7),("アプリ",88,4.4)],"specs":[("規格","Wi-Fi 6E（トライバンド）"),("速度","最大5,400Mbps"),("対応台数","最大200台"),("メッシュ","2台セット（約240m²カバー）"),("特徴","AIメッシュ / WPA3"),("アプリ","Deco アプリ")],"pros":["Wi-Fi 6Eで6GHz帯の超高速通信","AIメッシュが接続端末を自動最適化","2台で240m²をシームレスカバー","200台接続対応","5万円でWi-Fi 6E メッシュのコスパ"],"cons":["5万円","プロバイダのWi-Fi 6E対応が必要","1台での単体使用はコスパが下がる"],"desc":"一軒家・マンションで途切れるWi-Fiを完全解決するメッシュルーター。6GHz帯のWi-Fi 6Eで通信速度が劇的向上。テレワーク・4K動画を快適に。","related":[("review-asusZenWiFiET12","📡","ネットワーク機器","ASUS ZenWiFi Pro ET12 レビュー",4.6),("review-netgearorbiRBK863S","📡","ネットワーク機器","Netgear Orbi RBK863S レビュー",4.5),("review-eeromax7","📡","ネットワーク機器","Eero Max 7 レビュー",4.5)]},
    {"slug":"review-asusZenWiFiET12","name":"ASUS ZenWiFi Pro ET12","cat":"ネットワーク機器","emoji":"📡","price":"¥69,800","score":4.6,"bg":"#b71c1c,#c62828","scores":[("速度",100,5.0),("安定性",96,4.8),("ゲーマー向け",100,5.0),("コスパ",76,3.8),("設定詳細度",96,4.8)],"specs":[("規格","Wi-Fi 6E（トライバンド）"),("速度","最大11,000Mbps"),("対応台数","最大150台"),("特徴","ゲーマーモード / AiProtection Pro"),("ハードウェア","Quad-core 2.6GHz"),("バックホール","6GHz専用バックホール")],"pros":["11,000Mbpsの業界最高水準速度","6GHz専用バックホールでメッシュ通信が高速","AiProtection Proでセキュリティ完備","ゲーマーモードで優先帯域確保","詳細なネットワーク管理ができる"],"cons":["7万円の高価格","設定が複雑でプロ向け","消費電力が高い"],"desc":"ゲーマーとパワーユーザーのための最高峰メッシュWi-Fi。11,000Mbpsの速度と6GHz専用バックホールが家中どこでも超高速通信を実現。","related":[("review-tplinkdecoXE75pro","📡","ネットワーク機器","TP-Link Deco XE75 Pro レビュー",4.6),("review-netgearorbiRBK863S","📡","ネットワーク機器","Netgear Orbi RBK863S レビュー",4.5),("review-eeromax7","📡","ネットワーク機器","Eero Max 7 レビュー",4.5)]},
    {"slug":"review-netgearorbiRBK863S","name":"Netgear Orbi RBK863S","cat":"ネットワーク機器","emoji":"📡","price":"¥89,800","score":4.5,"bg":"#006064,#00838f","scores":[("カバー範囲",100,5.0),("速度",94,4.7),("大型住宅向け",100,5.0),("コスパ",70,3.5),("設定のしやすさ",82,4.1)],"specs":[("規格","Wi-Fi 6E（トライバンド）"),("速度","最大10,800Mbps"),("カバー範囲","3台で約800m²"),("接続","最大200台"),("特徴","10Gbpsポート / 専用バックホール"),("アプリ","Orbi アプリ")],"pros":["3台で800m²の超広域カバー","10Gbps有線ポートで超高速有線接続","専用バックホールで接続が安定","大型一戸建て・オフィスに最適","Netgearの信頼性"],"cons":["9万円の超高価格","大型住宅以外ではオーバースペック","設定がやや複雑"],"desc":"大型一戸建てやオフィスのWi-Fi問題を完全解決。3台で800m²カバーという圧倒的な広域対応力。10Gbpsポートが次世代回線にも対応。","related":[("review-tplinkdecoXE75pro","📡","ネットワーク機器","TP-Link Deco XE75 Pro レビュー",4.6),("review-asusZenWiFiET12","📡","ネットワーク機器","ASUS ZenWiFi Pro ET12 レビュー",4.6),("review-eeromax7","📡","ネットワーク機器","Eero Max 7 レビュー",4.5)]},
    {"slug":"review-eeromax7","name":"Amazon Eero Max 7","cat":"ネットワーク機器","emoji":"📡","price":"¥99,800","score":4.5,"bg":"#0d47a1,#1565c0","scores":[("速度",98,4.9),("Alexa連携",100,5.0),("有線バックホール",100,5.0),("コスパ",68,3.4),("デザイン",92,4.6)],"specs":[("規格","Wi-Fi 6E（クアッドバンド）"),("速度","最大9,400Mbps"),("特徴","有線・無線ハイブリッドメッシュ"),("接続","10GbEポート×2 / 2.5GbEポート×2"),("Alexa","Alexa内蔵"),("バックホール","有線バックホール対応")],"pros":["有線バックホールで安定性が最高峰","10GbEポートが次世代回線対応","Alexa内蔵でスマートホームハブになる","Amazon Eeroの圧倒的な使いやすさ","クアッドバンドで干渉を最小化"],"cons":["10万円","Amazon依存のエコシステム","Eeroアプリ有料機能あり"],"desc":"使いやすさと有線バックホールの安定性を両立するAmazonの最高峰ルーター。Alexa内蔵でスマートホームのハブとしても機能する。","related":[("review-tplinkdecoXE75pro","📡","ネットワーク機器","TP-Link Deco XE75 Pro レビュー",4.6),("review-asusZenWiFiET12","📡","ネットワーク機器","ASUS ZenWiFi Pro ET12 レビュー",4.6),("review-netgearorbiRBK863S","📡","ネットワーク機器","Netgear Orbi RBK863S レビュー",4.5)]},
    # ゲーミングチェア
    {"slug":"review-secretlabTitanEvo","name":"Secretlab TITAN Evo 2022","cat":"ゲーミングチェア","emoji":"🪑","price":"¥69,800","score":4.8,"bg":"#1a1a2e,#16213e","scores":[("座り心地",100,5.0),("腰サポート",100,5.0),("耐久性",98,4.9),("デザイン",96,4.8),("コスパ",82,4.1)],"specs":[("素材","NEO Hybrid Leatherette / SoftWeave Plus"),("腰サポート","4-way L-DURA lumbar"),("アームレスト","4D"),("リクライニング","165°"),("重量","62kg"),("対応体重","最大130kg")],"pros":["4-way腰サポートが完璧なポジションを維持","165°リクライニングで仮眠も可","NEO Hybrid素材が通気性と耐久性を両立","4Dアームレストで正確な位置調整","世界中のプロゲーマーが愛用"],"cons":["7万円","重量62kgで移動が大変","Sサイズは別料金"],"desc":"プロゲーマーが長時間セッションで選ぶ椅子。4-way腰サポートが正しい姿勢を強制的に維持し腰痛を予防。10時間座り続けても疲れない。","related":[("review-akracingProX","🪑","ゲーミングチェア","AKRacing Pro-X V2 レビュー",4.5),("review-noblechairsHERO","🪑","ゲーミングチェア","noblechairs HERO レビュー",4.6),("review-dxracerformula","🪑","ゲーミングチェア","DXRacer Formula Series レビュー",4.3)]},
    {"slug":"review-noblechairsHERO","name":"noblechairs HERO ゲーミングチェア","cat":"ゲーミングチェア","emoji":"🪑","price":"¥79,800","score":4.6,"bg":"#212121,#424242","scores":[("座り心地",96,4.8),("素材品質",100,5.0),("腰サポート",94,4.7),("デザイン",94,4.7),("コスパ",76,3.8)],"specs":[("素材","本革 / PUレザー"),("腰サポート","メモリーフォームクッション内蔵"),("アームレスト","4D"),("リクライニング","135°"),("耐荷重","150kg"),("特徴","デュアルデンシティフォーム")],"pros":["デュアルデンシティフォームが長時間でも沈み込まない","本革オプションで高級感が圧倒的","メモリーフォーム腰クッションが最高","150kg耐荷重","ドイツブランドの品質"],"cons":["8万円（本革は13万円）","135°リクライニングはSecretlabより少ない","重量が重い"],"desc":"ゲーミングチェアを高級家具として捉えるnoblechairsのフラグシップ。本革モデルは本物のオフィスチェア以上の品質。座るだけで仕事とゲームの生産性が上がる。","related":[("review-secretlabTitanEvo","🪑","ゲーミングチェア","Secretlab TITAN Evo 2022 レビュー",4.8),("review-akracingProX","🪑","ゲーミングチェア","AKRacing Pro-X V2 レビュー",4.5),("review-dxracerformula","🪑","ゲーミングチェア","DXRacer Formula Series レビュー",4.3)]},
    {"slug":"review-akracingProX","name":"AKRacing Pro-X V2","cat":"ゲーミングチェア","emoji":"🪑","price":"¥49,800","score":4.5,"bg":"#b71c1c,#c62828","scores":[("コスパ",94,4.7),("座り心地",90,4.5),("腰サポート",88,4.4),("デザイン",88,4.4),("耐久性",90,4.5)],"specs":[("素材","PUレザー"),("腰サポート","ランバーピロー付属"),("アームレスト","3D"),("リクライニング","180°"),("耐荷重","150kg"),("特徴","コールドフォームクッション")],"pros":["5万円のコスパゲーミングチェア","180°フルフラットリクライニング","150kg耐荷重","AKRacingの国内サポートが充実","カラーバリエーションが豊富"],"cons":["Secretlabほどの長時間快適性はない","PUレザーは劣化が速い","アームレストは3Dのみ"],"desc":"ゲーミングチェア入門の定番。5万円で180°フルフラット・AKRacingブランドの品質を入手できる。初めてゲーミングチェアを試す人に最適。","related":[("review-secretlabTitanEvo","🪑","ゲーミングチェア","Secretlab TITAN Evo 2022 レビュー",4.8),("review-noblechairsHERO","🪑","ゲーミングチェア","noblechairs HERO レビュー",4.6),("review-dxracerformula","🪑","ゲーミングチェア","DXRacer Formula Series レビュー",4.3)]},
    {"slug":"review-dxracerformula","name":"DXRacer Formula Series OH/FH08","cat":"ゲーミングチェア","emoji":"🪑","price":"¥34,800","score":4.3,"bg":"#e65100,#ef6c00","scores":[("コスパ",100,5.0),("デザイン",90,4.5),("座り心地",82,4.1),("耐久性",84,4.2),("ブランド",88,4.4)],"specs":[("素材","PUレザー / ファブリック"),("腰サポート","ランバークッション付属"),("アームレスト","3D"),("リクライニング","135°"),("耐荷重","100kg"),("特徴","コンパクトサイズ（小柄向け）")],"pros":["3.5万円の最安クラス","DXRacerの元祖ゲーミングチェアブランド","コンパクトで日本人体型に合いやすい","豊富なカラーバリエーション","ゲーミング感あふれるデザイン"],"cons":["耐荷重100kgで体格が良い人には不向き","長時間は腰がきつい","PUレザーの耐久性が課題"],"desc":"ゲーミングチェアの元祖ブランドのエントリーモデル。3.5万円で始めるゲーミングチェア生活。コンパクトサイズが日本の部屋に馴染む。","related":[("review-secretlabTitanEvo","🪑","ゲーミングチェア","Secretlab TITAN Evo 2022 レビュー",4.8),("review-noblechairsHERO","🪑","ゲーミングチェア","noblechairs HERO レビュー",4.6),("review-akracingProX","🪑","ゲーミングチェア","AKRacing Pro-X V2 レビュー",4.5)]},
    # コードレス掃除機
    {"slug":"review-dysonv12detectslim","name":"Dyson V12 Detect Slim","cat":"コードレス掃除機","emoji":"🧹","price":"¥69,800","score":4.7,"bg":"#4a148c,#6a1b9a","scores":[("レーザー検知",100,5.0),("軽量性",96,4.8),("吸引力",90,4.5),("バッテリー",88,4.4),("コスパ",82,4.1)],"specs":[("吸引力","150AW"),("レーザー","グリーンレーザーホコリ可視化"),("重量","2.1kg"),("バッテリー","最大60分"),("HEPA","H13フィルター"),("特徴","自動吸引調整（LCDゴミ量表示）")],"pros":["レーザーで床のホコリが見える衝撃","2.1kgの軽量でV15より700g軽い","自動でゴミ量に応じてパワー調整","H13 HEPAフィルターでアレルギー対策","7万円でDysonレーザー体験"],"cons":["V15より吸引力が劣る（150AW vs 230AW）","バッテリー60分（強モードは20分）","替えフィルターが高い"],"desc":"Dysonのレーザー検知をV15より安く体験できるモデル。2.1kgの軽さで女性でも疲れにくい。フローリング中心の家庭に最高のコスパ。","related":[("review-dysonv15","🧹","家電","Dyson V15 Detect レビュー",4.5),("review-makitaCL003GZ","🧹","コードレス掃除機","マキタ CL003GZ レビュー",4.3),("review-panasonicMCSBU830K","🧹","コードレス掃除機","Panasonic MC-SBU830K レビュー",4.4)]},
    {"slug":"review-panasonicMCSBU830K","name":"Panasonic MC-SBU830K","cat":"コードレス掃除機","emoji":"🧹","price":"¥39,800","score":4.4,"bg":"#0d47a1,#1565c0","scores":[("コスパ",92,4.6),("吸引力",88,4.4),("軽量性",90,4.5),("ナノイー",94,4.7),("使いやすさ",90,4.5)],"specs":[("吸引力","強モード 180W"),("特徴","ナノイー除菌"),("重量","1.7kg（ヘッドなし）"),("バッテリー","最大60分（標準モード）"),("フィルター","HEPA13対応"),("ノズル","自走式ハイグレードノズル")],"pros":["1.7kgの超軽量","ナノイーで除菌・消臭しながら掃除","4万円の国産コスパ","自走式ノズルで力いらず","60分バッテリー"],"cons":["吸引力はDysonに劣る","ナノイー効果の体感は個人差","大型ゴミの吸い込みは苦手"],"desc":"国産コードレス掃除機の優等生。1.7kgの軽さとナノイー除菌機能が日常の掃除を快適に。パナソニックの安心感とコスパが魅力。","related":[("review-dysonv12detectslim","🧹","コードレス掃除機","Dyson V12 Detect Slim レビュー",4.7),("review-dysonv15","🧹","家電","Dyson V15 Detect レビュー",4.5),("review-makitaCL003GZ","🧹","コードレス掃除機","マキタ CL003GZ レビュー",4.3)]},
    {"slug":"review-makitaCL003GZ","name":"マキタ CL003GZ（40V）","cat":"コードレス掃除機","emoji":"🧹","price":"¥29,800","score":4.3,"bg":"#1b5e20,#2e7d32","scores":[("プロ吸引力",96,4.8),("耐久性",100,5.0),("コスパ",90,4.5),("使いやすさ",80,4.0),("静音性",78,3.9)],"specs":[("規格","40Vmax"),("吸引力","業務用レベル"),("重量","2.3kg（本体のみ）"),("対応バッテリー","BL4025 / BL4040等"),("特徴","マキタ工具バッテリー流用可"),("フィルター","紙パック式")],"pros":["工具メーカー品質の圧倒的耐久性","40Vの業務用吸引力","マキタ工具バッテリーと共有できる","プロの現場でも使われる信頼性","シンプルな構造でメンテが楽"],"cons":["デザインがプロ仕様で家庭向けでない","バッテリー別売り（本体のみ）","静音性が低い"],"desc":"家庭用の枠を超えた業務用品質コードレス掃除機。マキタのバッテリーを電動工具と共用できる職人仕様。とにかく吸うことと壊れないことを優先する人向け。","related":[("review-dysonv12detectslim","🧹","コードレス掃除機","Dyson V12 Detect Slim レビュー",4.7),("review-panasonicMCSBU830K","🧹","コードレス掃除機","Panasonic MC-SBU830K レビュー",4.4),("review-dysonv15","🧹","家電","Dyson V15 Detect レビュー",4.5)]},
    # 調理家電
    {"slug":"review-sharpHealsioAXXA20","name":"シャープ ヘルシオ AX-XA20","cat":"調理家電","emoji":"🍳","price":"¥99,800","score":4.7,"bg":"#e65100,#bf360c","scores":[("ウォーターオーブン",100,5.0),("ヘルシー調理",100,5.0),("機能数",96,4.8),("コスパ",78,3.9),("操作性",88,4.4)],"specs":[("方式","ウォーターオーブン（過熱水蒸気）"),("容量","30L"),("機能","ウォーターオーブン / 電子レンジ / スチーム / トースター"),("AI","AIoT対応（COCORO KITCHEN）"),("重量","22kg"),("特徴","まかせて調理（AI献立提案）")],"pros":["過熱水蒸気が栄養を守りながら調理","揚げ物が油なしでサクサクに","AI献立提案で何を作るか悩まない","電子レンジ・スチーム・トースターを1台で","ヘルシーな調理が続けられる"],"cons":["10万円","22kgの重さ","庫内のお手入れが必要"],"desc":"調理革命をもたらすウォーターオーブン。過熱水蒸気が油なし揚げ物・栄養満点蒸し料理を実現。健康的な食生活をAIがサポート。","related":[("review-panasonicBistroNEBS1600","🍳","調理家電","Panasonic ビストロ NE-BS1600 レビュー",4.6),("review-instantpotDuo","🍳","調理家電","Instant Pot Duo レビュー",4.4),("review-sharpKNHW24G","🍳","調理家電","シャープ KN-HW24G レビュー",4.5)]},
    {"slug":"review-panasonicBistroNEBS1600","name":"Panasonic ビストロ NE-BS1600","cat":"調理家電","emoji":"🍳","price":"¥79,800","score":4.6,"bg":"#880e4f,#ad1457","scores":[("スチーム機能",96,4.8),("AI調理",94,4.7),("操作性",92,4.6),("コスパ",82,4.1),("デザイン",88,4.4)],"specs":[("方式","スチームオーブンレンジ"),("容量","30L"),("機能","スチーム / オーブン / レンジ / トースター"),("AI","AI自動メニュー"),("重量","20kg"),("特徴","スマホ連携 / 1000Wマイクロ波")],"pros":["1000W高出力マイクロ波で素早い加熱","スチーム機能でパンの温め直しが完璧","AI自動メニューが食材を入れるだけで調理","スマホ連携でレシピ転送","パナソニックの安心品質"],"cons":["8万円","20kgの重さ","ヘルシオほどのウォーター機能はない"],"desc":"毎日の料理を楽にするパナソニックの全部入りスチームオーブン。AI自動メニューが初心者でもプロ級の料理を可能に。家族の健康管理を美味しく続けられる。","related":[("review-sharpHealsioAXXA20","🍳","調理家電","シャープ ヘルシオ AX-XA20 レビュー",4.7),("review-sharpKNHW24G","🍳","調理家電","シャープ KN-HW24G レビュー",4.5),("review-instantpotDuo","🍳","調理家電","Instant Pot Duo レビュー",4.4)]},
    {"slug":"review-sharpKNHW24G","name":"シャープ ホットクック KN-HW24G","cat":"調理家電","emoji":"🍳","price":"¥49,800","score":4.5,"bg":"#4a148c,#6a1b9a","scores":[("自動調理",100,5.0),("料理の仕上がり",94,4.7),("コスパ",86,4.3),("使いやすさ",90,4.5),("レシピ数",96,4.8)],"specs":[("容量","2.4L（4〜6人用）"),("方式","水なし自動調理鍋"),("AI","AIoT / COCORO KITCHEN連携"),("操作","60分タイマー / 予約12時間"),("メニュー","350種以上"),("特徴","かき混ぜユニット自動化")],"pros":["材料を入れてスイッチを押すだけで完成","かき混ぜユニットが自動でカレー・シチューも作れる","350種以上のメニュー","12時間予約で帰ったらできている","5万円のコスパ"],"cons":["電気圧力鍋ほど時短効果はない","内鍋の手入れが必要","時間がかかる料理もある"],"desc":"共働き家庭を救う自動調理鍋。材料を入れてスイッチを押すだけで本格的な煮込み料理が完成。帰宅時に食事の準備ができている生活は想像以上に楽。","related":[("review-sharpHealsioAXXA20","🍳","調理家電","シャープ ヘルシオ AX-XA20 レビュー",4.7),("review-panasonicBistroNEBS1600","🍳","調理家電","Panasonic ビストロ NE-BS1600 レビュー",4.6),("review-instantpotDuo","🍳","調理家電","Instant Pot Duo レビュー",4.4)]},
    {"slug":"review-instantpotDuo","name":"Instant Pot Duo 7-in-1","cat":"調理家電","emoji":"🍳","price":"¥12,800","score":4.4,"bg":"#1b5e20,#2e7d32","scores":[("コスパ",100,5.0),("時短調理",96,4.8),("多機能",94,4.7),("使いやすさ",88,4.4),("デザイン",80,4.0)],"specs":[("機能","圧力鍋 / スロークッカー / 炊飯器 / スチーマー / ソテー / ヨーグルト / 保温"),("容量","5.7L"),("圧力","最大11.6psi"),("重量","5.3kg"),("特徴","プログラマブル"),("対応","インダクション不可（100V電源）")],"pros":["1.3万円で7役のコスパが異常","圧力鍋で煮込み時間を1/3に短縮","ヨーグルト・炊飯まで一台で","世界的に人気の定番モデル","レシピが豊富（世界中のコミュニティ）"],"cons":["初期設定が少し複雑","ホットクックのような自動かき混ぜ機能なし","圧力調理後の蒸気排出に注意"],"desc":"世界中で愛される電気圧力鍋の定番。1.3万円で7つの調理法をカバーし、圧力で煮込み時間を劇的に短縮。忙しい人の味方。","related":[("review-sharpKNHW24G","🍳","調理家電","シャープ ホットクック KN-HW24G レビュー",4.5),("review-sharpHealsioAXXA20","🍳","調理家電","シャープ ヘルシオ AX-XA20 レビュー",4.7),("review-panasonicBistroNEBS1600","🍳","調理家電","Panasonic ビストロ NE-BS1600 レビュー",4.6)]},
    # スマートフォン追加
    {"slug":"review-galaxys25plus","name":"Samsung Galaxy S25+","cat":"スマートフォン","emoji":"📱","price":"¥154,800","score":4.7,"bg":"#1a237e,#283593","scores":[("AI機能",100,5.0),("カメラ",94,4.7),("バッテリー",92,4.6),("パフォーマンス",96,4.8),("コスパ",82,4.1)],"specs":[("ディスプレイ","6.7インチ Dynamic AMOLED 2X 120Hz"),("チップ","Snapdragon 8 Elite"),("カメラ","50MP+12MP+10MP 3倍望遠"),("バッテリー","4,900mAh 45W充電"),("重量","190g"),("AI","Galaxy AI（Circle to Search / Live Translate）")],"pros":["Snapdragon 8 Eliteで最強パフォーマンス","Galaxy AI機能が圧倒的に便利","190gで大画面6.7インチは軽い","45W急速充電","S25 Ultraより10万円安い"],"cons":["Sペン非対応","Ultra比でカメラがやや劣る","15.5万円は高い"],"desc":"S25 Ultraの機能を190gに凝縮した最強バランスモデル。Galaxy AIの便利さはPixelを超える瞬間が多く、大画面・高性能・Galaxy AIを求めるなら最適解。","related":[("review-galaxy-s25","📱","スマートフォン","Samsung Galaxy S25 レビュー",4.6),("review-galaxys25ultra","📱","スマートフォン","Samsung Galaxy S25 Ultra レビュー",4.8),("review-iphone16promax","📱","スマートフォン","iPhone 16 Pro Max レビュー",4.9)]},
    {"slug":"review-xperia10vi","name":"Sony Xperia 10 VII","cat":"スマートフォン","emoji":"📱","price":"¥64,800","score":4.2,"bg":"#1b5e20,#2e7d32","scores":[("コスパ",90,4.5),("バッテリー",96,4.8),("軽量性",98,4.9),("カメラ",76,3.8),("パフォーマンス",78,3.9)],"specs":[("ディスプレイ","6.1インチ 21:9 有機EL 60Hz"),("チップ","Snapdragon 6 Gen 1"),("カメラ","48MP+8MP超広角+8MP望遠"),("バッテリー","5,000mAh"),("重量","155g"),("防水","IPX5/IPX8")],"pros":["155gの超軽量","5,000mAhの大容量バッテリー","ソニーのAudio技術（3.5mmジャック）","IPX8防水","6.5万円のコスパ"],"cons":["60Hz（リフレッシュレートが低い）","チップがミドルレンジ","カメラ性能がフラッグシップに大きく劣る"],"desc":"軽さとバッテリーに特化したソニーのミドルレンジ。155gという軽さはiPhone 16より80g軽く、重いスマホが嫌いな人に刺さる。3.5mmジャック搭載も嬉しい。","related":[("review-xperia1vi","📱","スマートフォン","Xperia 1 VI レビュー",4.6),("review-pixel8a","📱","スマートフォン","Pixel 8a レビュー",4.5),("review-galaxya55","📱","スマートフォン","Galaxy A55 5G レビュー",4.3)]},
    {"slug":"review-iphone16e","name":"iPhone 16e","cat":"スマートフォン","emoji":"📱","price":"¥84,800","score":4.4,"bg":"#2d2d2d,#404040","scores":[("コスパ",88,4.4),("Apple Intelligence",94,4.7),("カメラ",86,4.3),("バッテリー",88,4.4),("コンパクト",96,4.8)],"specs":[("ディスプレイ","6.1インチ Super Retina XDR 60Hz"),("チップ","A16 Bionic"),("カメラ","48MP シングルカメラ"),("バッテリー","最大26時間ビデオ再生"),("重量","167g"),("特徴","Apple Intelligence対応")],"pros":["A16 BionicでApple Intelligence全機能対応","167gの軽量","8.5万円でiPhoneエコシステム","USB-C対応","Apple Intelligence入門として最安"],"cons":["シングルカメラ（望遠・超広角なし）","60Hz（ProMotion非対応）","Proと比べて機能が限定的"],"desc":"Apple Intelligenceを最安で体験できる新しいエントリーiPhone。8.5万円でA16チップを搭載し、AI機能を日常で活用したい人への最適解。","related":[("review-iphonese4","📱","スマートフォン","iPhone SE 第4世代 レビュー",4.3),("review-iphone16","📱","スマートフォン","iPhone 16 レビュー",4.5),("review-pixel9a","📱","スマートフォン","Pixel 9a レビュー",4.4)]},
    {"slug":"review-motorolaedge50pro","name":"Motorola Edge 50 Pro","cat":"スマートフォン","emoji":"📱","price":"¥69,800","score":4.3,"bg":"#4a148c,#6a1b9a","scores":[("コスパ",94,4.7),("充電速度",100,5.0),("カメラ",86,4.3),("パフォーマンス",88,4.4),("デザイン",86,4.3)],"specs":[("ディスプレイ","6.7インチ pOLED 144Hz"),("チップ","Snapdragon 7 Gen 3"),("カメラ","50MP+13MP超広角+10MP望遠"),("充電","125W有線（34分フル充電）"),("重量","186g"),("防水","IP68")],"pros":["125Wで34分フル充電という異次元の速さ","144Hz pOLED ディスプレイ","7万円のコスパ","IP68防水","ピュアAndroidに近いUI"],"cons":["Snapdragon 7 Gen 3はミドルレンジ","カメラはハイエンドに劣る","日本では認知度が低い"],"desc":"充電速度世界最速クラスの125Wを7万円で。34分でフル充電というのは使ってみると革命的な体験。スペックと価格のバランスが優れたダークホース。","related":[("review-motorolaedge50ultra","📱","スマートフォン","Motorola Edge 50 Ultra レビュー",4.5),("review-oneplus13","📱","スマートフォン","OnePlus 13 レビュー",4.6),("review-galaxya55","📱","スマートフォン","Galaxy A55 5G レビュー",4.3)]},
    # ワイヤレスイヤホン追加
    {"slug":"review-final-ze3000","name":"final ZE3000 ANC","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥19,800","score":4.4,"bg":"#1a237e,#283593","scores":[("音質",90,4.5),("ANC",86,4.3),("コスパ",94,4.7),("装着感",88,4.4),("ドライバー品質",94,4.7)],"specs":[("ドライバー","6mm f-Core DU ダイナミックドライバー"),("ANC","対応（ハイブリッド）"),("再生時間","ANCオン7時間（ケース含28時間）"),("接続","Bluetooth 5.2"),("コーデック","AAC / SBC"),("重量","5.5g")],"pros":["5.5gの超軽量イヤホン","finalの高音質ドライバーが2万円以下","ANC・外音取り込み対応","装着が安定するfinal型イヤーピース付属","音楽のディテールが繊細"],"cons":["ANCはソニー・ボーズに劣る","ケース込み28時間は短め","LDAC非対応"],"desc":"オーディオブランドfinalがコスパ重視で作った一台。5.5gの軽さと高音質ドライバーの組み合わせは国産イヤホンの誇り。音楽好きに刺さる。","related":[("review-sonywf1000xm5","🎧","ワイヤレスイヤホン","Sony WF-1000XM5 レビュー",4.8),("review-ankerliberty4nc","🎧","ワイヤレスイヤホン","Anker Liberty 4 NC レビュー",4.5),("review-nothingear2","🎧","ワイヤレスイヤホン","Nothing Ear (2) レビュー",4.4)]},
    {"slug":"review-jabra-evolve2buds","name":"Jabra Evolve2 Buds","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥49,800","score":4.5,"bg":"#006064,#00838f","scores":[("通話品質",100,5.0),("ANC",94,4.7),("ビジネス向け",100,5.0),("音質",86,4.3),("コスパ",80,4.0)],"specs":[("マイク","6マイクシステム"),("ANC","AdvancedANC"),("再生時間","8時間（ケース含27時間）"),("接続","Bluetooth 5.2 / USB-A Dongle付属"),("認定","Microsoft Teams / Zoom認定"),("重量","6.2g")],"pros":["6マイクで通話・会議音声が圧倒的にクリア","Microsoft Teams / Zoom認定","USB Dongle付属で会社PCとも安定接続","ANC性能が高く集中作業に最適","在宅・オフィス兼用の最強ビジネスイヤホン"],"cons":["5万円","音楽用途よりビジネス特化","デザインはシンプル"],"desc":"テレワーク・会議に特化した最強ビジネスイヤホン。6マイクの通話品質はAirPodsを超える。オンライン会議で声が届かない問題を完全解決。","related":[("review-sonywf1000xm5","🎧","ワイヤレスイヤホン","Sony WF-1000XM5 レビュー",4.8),("review-boseqcearbuds2","🎧","ワイヤレスイヤホン","Bose QC Earbuds II レビュー",4.6),("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8)]},
    {"slug":"review-shokzOpenRunPro2","name":"Shokz OpenRun Pro 2","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥26,880","score":4.4,"bg":"#0d47a1,#1565c0","scores":[("骨伝導音質",96,4.8),("開放感",100,5.0),("スポーツ適性",100,5.0),("ANC",20,1.0),("コスパ",88,4.4)],"specs":[("方式","骨伝導"),("再生時間","最大10時間"),("防水","IP55"),("充電","USB-C（10分で1.5時間）"),("重量","29g"),("特徴","耳をふさがない開放型")],"pros":["耳をふさがないので外の音が聞こえる（安全）","ランニング・サイクリングに最適","IP55防水で汗・雨対応","骨伝導最高峰の音質","10時間バッテリー"],"cons":["ANC機能なし（仕様上不可）","骨伝導特有の音質（低音が弱い）","耳掛け型で着け外しが必要"],"desc":"スポーツ×安全性の最強骨伝導イヤホン。走りながら周囲の音が聞こえる安心感は通常イヤホンでは実現不可能。ランナー・サイクリストの定番。","related":[("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8),("review-ankerliberty4nc","🎧","ワイヤレスイヤホン","Anker Liberty 4 NC レビュー",4.5),("review-nothingear2","🎧","ワイヤレスイヤホン","Nothing Ear (2) レビュー",4.4)]},
    # カメラ追加
    {"slug":"review-fujifilmx100vi","name":"Fujifilm X100VI","cat":"カメラ","emoji":"📷","price":"¥238,000","score":4.9,"bg":"#795548,#6d4c41","scores":[("写真品質",100,5.0),("デザイン",100,5.0),("コンパクト性",96,4.8),("フィルムシミュレーション",100,5.0),("コスパ",74,3.7)],"specs":[("センサー","APS-C 4020万画素 X-Trans CMOS 5 HR"),("レンズ","23mmF2（換算35mm）固定"),("手ブレ補正","7段IBIS"),("動画","6.2K / 4K 120fps"),("重量","521g"),("特徴","20種のフィルムシミュレーション")],"pros":["4020万画素APS-CセンサーでX100史上最高画質","7段手ブレ補正で手持ち撮影が安定","20種フィルムシミュレーションで撮って出し最強","521gで1日持ち歩いても疲れない","クラシックなデザインが圧倒的人気"],"cons":["24万円","固定レンズ（交換不可）","供給不足で入手困難な場合がある"],"desc":"写真史上最も話題になったコンデジ。1台でフォトジャーナリスト・旅行・日常すべてをカバー。フィルムシミュレーションの撮って出しは現像不要の芸術品。","related":[("review-fujifilmxt5","📷","カメラ","Fujifilm X-T5 レビュー",4.8),("review-sonya7cii","📷","カメラ","Sony α7C II レビュー",4.7),("review-canoneosr50","📷","カメラ","Canon EOS R50 レビュー",4.5)]},
    {"slug":"review-nikonz50ii","name":"Nikon Z50 II","cat":"カメラ","emoji":"📷","price":"¥129,800","score":4.5,"bg":"#ffd600,#1a1a1a","scores":[("コスパ",92,4.6),("操作性",94,4.7),("APS-C画質",90,4.5),("AF速度",88,4.4),("動画",86,4.3)],"specs":[("センサー","APS-C 2088万画素"),("AF","被写体検出AF（人物・動物・乗り物）"),("連写","最大11コマ/秒"),("動画","4K UHD 30fps"),("重量","450g"),("特徴","Zマウント×充実ダイヤル操作")],"pros":["13万円でNikon Zマウントの高品質","450gの軽量","被写体検出AFが人物・動物・乗り物対応","充実したダイヤル操作で撮影が楽しい","Nikon Z レンズの豊富なラインナップ"],"cons":["センサーは2088万画素（最新機種より少ない）","動画は4K 30fps止まり","手ブレ補正が本体にない（レンズ依存）"],"desc":"操作を楽しめる写真好きのためのAPS-Cミラーレス。13万円でNikonの光学技術とZマウントに入門できる。ダイヤル操作の楽しさはスマホカメラとは別次元。","related":[("review-fujifilmxt5","📷","カメラ","Fujifilm X-T5 レビュー",4.8),("review-canoneosr50","📷","カメラ","Canon EOS R50 レビュー",4.5),("review-sonya7cii","📷","カメラ","Sony α7C II レビュー",4.7)]},
    {"slug":"review-goprohero13black","name":"GoPro HERO13 Black","cat":"カメラ","emoji":"📷","price":"¥63,800","score":4.6,"bg":"#1b5e20,#2e7d32","scores":[("アクション耐久性",100,5.0),("手ブレ補正",98,4.9),("4K品質",92,4.6),("コスパ",84,4.2),("バッテリー",80,4.0)],"specs":[("解像度","5.3K60 / 4K120fps / 2.7K240fps"),("手ブレ補正","HyperSmooth 6.0"),("防水","10m防水（ケースなし）"),("重量","154g"),("接続","Bluetooth / Wi-Fi / USB-C"),("特徴","磁気スワップ / Max Lens Mod 2.0対応")],"pros":["5.3K 60fpsが154gで撮れる衝撃","HyperSmooth 6.0の超強力手ブレ補正","10m防水でアクティビティ全対応","磁気マウントで脱着が超速","360°レンズmodで仮想ジンバル"],"cons":["バッテリーが1.5〜2時間","低照度は大センサーに劣る","広角固定（ズームなし）"],"desc":"スポーツ・旅行・アクティビティの記録に最強。HyperSmooth 6.0の手ブレ補正は走りながら撮影してもヌルヌル。アドベンチャーを美しく残せる。","related":[("review-djiosmoaction4","📷","カメラ","DJI Osmo Action 4 レビュー",4.6),("review-insta360x4","📷","カメラ","Insta360 X4 レビュー",4.6),("review-sonyzve10ii","📷","カメラ","Sony ZV-E10 II レビュー",4.8)]},
    # モニター追加
    {"slug":"review-lgultrafine5k27md5kl","name":"LG UltraFine 5K 27MD5KL","cat":"モニター","emoji":"🖥️","price":"¥118,800","score":4.6,"bg":"#1a1a2e,#16213e","scores":[("5K解像度",100,5.0),("Mac連携",100,5.0),("色精度",96,4.8),("コスパ",72,3.6),("デザイン",88,4.4)],"specs":[("解像度","5120×2880（5K）"),("サイズ","27インチ"),("パネル","IPS"),("接続","Thunderbolt 3×2（94W給電）"),("色域","P3広色域"),("特徴","Apple公式推奨")],"pros":["5K解像度がMacBook Proのテキストを完璧に表示","Thunderbolt 3 94W給電でMacを充電しながら使用","Apple公式推奨モニター","P3広色域で写真・動画編集に最適","スッキリしたケーブル1本接続"],"cons":["12万円","Windows PCとの相性は普通","27インチのみ（32インチ非対応）"],"desc":"MacユーザーのためのApple公式推奨モニター。5Kの超高精細表示×Thunderbolt 3給電で、MacBook Proのポテンシャルを100%引き出す。クリエイターに最適。","related":[("review-benqpd3205u","🖥️","モニター","BenQ PD3205U レビュー",4.6),("review-dellu2723d","🖥️","モニター","Dell U2723D レビュー",4.5),("review-asusrogswiftpg279qm","🖥️","モニター","ASUS ROG Swift PG279QM レビュー",4.6)]},
    {"slug":"review-dellalienware34oled","name":"Dell Alienware 34 OLED（AW3423DWF）","cat":"モニター","emoji":"🖥️","price":"¥179,800","score":4.8,"bg":"#0d0221,#1a0033","scores":[("OLEDゲーム画質",100,5.0),("応答速度",100,5.0),("湾曲没入感",100,5.0),("コスパ",76,3.8),("デザイン",96,4.8)],"specs":[("パネル","QD-OLED（量子ドットOLED）"),("解像度","3440×1440（UWQHD）"),("サイズ","34インチ湾曲（1800R）"),("リフレッシュレート","165Hz"),("応答速度","0.1ms"),("接続","HDMI 2.0×2 / DisplayPort 1.4×1")],"pros":["QD-OLEDが黒の締まり×色域×輝度を全部満たす","0.1ms応答でゲームの入力遅延ゼロ","34インチ湾曲の圧倒的没入感","165HzでFPS・RPG両方快適","Alienwareデザインの格好よさ"],"cons":["18万円","OLEDで焼き付きリスク","輝度はMini LEDより低い場合あり"],"desc":"PCゲームの映像体験を革命的に変えるQD-OLED湾曲モニター。0.1msの応答速度と完璧な黒で、ゲームが映画を超える体験になる。","related":[("review-asusrogswiftpg279qm","🖥️","モニター","ASUS ROG Swift PG279QM レビュー",4.6),("review-lg45gr95qeb","🖥️","モニター","LG UltraGear 45GR95QE-B レビュー",4.7),("review-samsungodysseyg7","🖥️","モニター","Samsung Odyssey G7 レビュー",4.5)]},
    # モバイルバッテリー追加
    {"slug":"review-anker747powerbank","name":"Anker 747 Power Bank","cat":"モバイルバッテリー","emoji":"🔋","price":"¥12,990","score":4.7,"bg":"#1a237e,#283593","scores":[("容量",100,5.0),("出力",96,4.8),("コスパ",92,4.6),("重量",72,3.6),("対応端末",96,4.8)],"specs":[("容量","26,800mAh"),("出力","最大140W（USB-C）"),("入力","最大65W（USB-C）"),("ポート","USB-C×2 / USB-A×2"),("重量","693g"),("特徴","ノートPC・iPad対応")],"pros":["140Wでノート・スマホ・タブレット同時給電","26,800mAhでiPhone 16を約5.5回充電","4ポート同時出力","65W入力で2.5時間フル充電","Ankerの品質保証"],"cons":["693gの重さ","大型で持ち運びには荷物になる","旅行の航空機持ち込みは要確認（100Wh以下）"],"desc":"ノートPCまで充電できるモバイルバッテリーの決定版。140W出力×4ポートで出張先でのコンセント争奪戦から解放される。デスク据え置き用途にも最適。","related":[("review-ankerprime20000","🔋","モバイルバッテリー","Anker Prime 20000mAh レビュー",4.8),("review-ciosmartcoby","🔋","モバイルバッテリー","CIO SMARTCOBY レビュー",4.5),("review-anker733","⚡","充電器","Anker 733 GaNPrime レビュー",4.7)]},
    {"slug":"review-ciosmartcobypro30w","name":"CIO SMARTCOBY Pro SLIM 30W","cat":"モバイルバッテリー","emoji":"🔋","price":"¥5,980","score":4.5,"bg":"#004d40,#00695c","scores":[("薄さ",100,5.0),("コスパ",96,4.8),("出力",84,4.2),("重量",90,4.5),("ブランド",82,4.1)],"specs":[("容量","10,000mAh"),("出力","最大30W（USB-C）"),("重量","185g"),("厚さ","13.5mm（クレジットカード2枚分）"),("特徴","ケーブル内蔵（USB-C）"),("日本メーカー","CIO（大阪）")],"pros":["13.5mmの超薄型でバッグに入れても邪魔にならない","ケーブル内蔵で忘れ物なし","6千円のコスパ","185gの軽量","日本メーカーの安心感"],"cons":["10,000mAh（大容量機には劣る）","30W出力（ノートPCは難しい）","ケーブルがUSB-Cのみ（Lightning非対応）"],"desc":"バッグに常備しておきたい超薄型モバイルバッテリー。13.5mmというクレジットカード2枚分の薄さは持ち運びの概念を変える。ケーブル内蔵でいつでも充電可能。","related":[("review-ankerprime20000","🔋","モバイルバッテリー","Anker Prime 20000mAh レビュー",4.8),("review-anker747powerbank","🔋","モバイルバッテリー","Anker 747 Power Bank レビュー",4.7),("review-ciosmartcoby","🔋","モバイルバッテリー","CIO SMARTCOBY レビュー",4.5)]},
    # スピーカー追加
    {"slug":"review-boseSoundLinkMax","name":"Bose SoundLink Max","cat":"スピーカー","emoji":"🔊","price":"¥54,800","score":4.7,"bg":"#1a1a2e,#16213e","scores":[("音質",98,4.9),("音量",96,4.8),("防水",94,4.7),("バッテリー",88,4.4),("コスパ",80,4.0)],"specs":[("出力","最大80dB"),("防水","IP67"),("バッテリー","最大20時間"),("接続","Bluetooth 5.3 / USB-C"),("重量","1,300g"),("特徴","Bose最大級の低音")],"pros":["Boseポータブル史上最大の音量と低音","IP67防水でアウトドア全対応","20時間バッテリー","USB-Cパススルー充電（スマホを充電しながら使用）","Boseの豊かな音質で音楽に没頭できる"],"cons":["5.5万円","1.3kgとやや重い","サイズが大きめ"],"desc":"Boseが本気で作ったポータブルスピーカーの最高峰。圧倒的な音量と低音でBBQ・キャンプ・パーティーを支配する。Boseブランドの音質哲学をどこでも。","related":[("review-sonysrsxb43","🔊","スピーカー","Sony SRS-XB43 レビュー",4.5),("review-soundcorex600","🔊","スピーカー","Anker Soundcore Motion X600 レビュー",4.6),("review-jblflip6","🔊","スピーカー","JBL Flip 6 レビュー",4.5)]},
    {"slug":"review-jblflip6","name":"JBL Flip 6","cat":"スピーカー","emoji":"🔊","price":"¥19,800","score":4.5,"bg":"#e65100,#bf360c","scores":[("コスパ",96,4.8),("音質",88,4.4),("防水",100,5.0),("携帯性",96,4.8),("バッテリー",88,4.4)],"specs":[("出力","30W（ツインホーン・2方向放音）"),("防水","IP67（水没OK）"),("バッテリー","最大12時間"),("接続","Bluetooth 5.1"),("重量","550g"),("特徴","PartyBoost（複数台接続）")],"pros":["2万円のコスパが異常","IP67で水没・砂浜OKの最強防水","PartyBoostで複数台接続","550gの携帯性","JBLの定番として世界中で使われる"],"cons":["12時間バッテリー（SonyやAnkerに劣る）","通話マイク品質が普通","単体ではステレオ非対応"],"desc":"防水×コスパの神スピーカー。2万円でIP67防水・PartyBoost対応・JBLブランドを手に入れられる。世界中のアウトドア愛好家が選ぶ定番中の定番。","related":[("review-boseSoundLinkMax","🔊","スピーカー","Bose SoundLink Max レビュー",4.7),("review-sonysrsxb43","🔊","スピーカー","Sony SRS-XB43 レビュー",4.5),("review-soundcorex600","🔊","スピーカー","Anker Soundcore Motion X600 レビュー",4.6)]},
    # スマートホーム追加
    {"slug":"review-switchbotmini4k","name":"SwitchBot ハブ2","cat":"スマートホーム","emoji":"💡","price":"¥9,980","score":4.5,"bg":"#1a237e,#283593","scores":[("赤外線制御",100,5.0),("コスパ",100,5.0),("温湿度計",94,4.7),("Matter対応",90,4.5),("設置のしやすさ",92,4.6)],"specs":[("赤外線","学習リモコン（TV・エアコン・照明対応）"),("温湿度","温湿度センサー内蔵"),("接続","Wi-Fi / Matter / Thread"),("互換","Alexa / Google / Siri / HomeKit"),("電源","USB給電"),("特徴","SwitchBot Matter対応ハブ")],"pros":["1万円でスマートホームの司令塔","既存のリモコン家電をスマート化","温湿度が測れる多機能","Matter対応で将来の拡張性抜群","Alexa/Google/HomeKit全対応"],"cons":["Wi-Fi 2.4GHzのみ（5GHz非対応）","赤外線が届かない方向はNG","スマホアプリ必須"],"desc":"1万円でリモコン家電を全部スマート化できる最強ハブ。TV・エアコン・照明を音声コントロール・自動化・外出先操作が可能に。スマートホーム入門の正解。","related":[("review-philipshue","💡","スマートホーム","Philips Hue スターターキット レビュー",4.3),("review-applehomedpodmini","🔊","スマートスピーカー","Apple HomePod mini レビュー",4.4),("review-amazonechoshow10","🔊","スマートスピーカー","Amazon Echo Show 10 レビュー",4.3)]},
    {"slug":"review-naturedremov4","name":"Nature Remo 4","cat":"スマートホーム","emoji":"💡","price":"¥14,800","score":4.4,"bg":"#004d40,#00695c","scores":[("日本製品対応",100,5.0),("コスパ",94,4.7),("自動化",92,4.6),("デザイン",90,4.5),("API",96,4.8)],"specs":[("方式","Wi-Fi接続スマートリモコン"),("制御","赤外線 / Bluetooth SIG / Wi-Fi"),("対応","Alexa / Google Home / HomeKit / Matter"),("特徴","Nature Remoサービス × IFTTT"),("API","Nature API公開"),("電源","USB給電")],"pros":["日本製家電との相性が最高（エアコン・TV・照明）","API公開でプログラマブルな自動化","HomeKit対応で完全な音声制御","IFTTT連携で自由なオートメーション","すっきりしたミニマルデザイン"],"cons":["1.5万円（SwitchBotハブ2より高い）","温湿度センサーなし（別売）","国内特化でグローバル製品への対応は限定的"],"desc":"日本製スマートリモコンの最高峰。エアコン・TV・照明を細かく自動化できる。プログラマーにはAPIが嬉しい。日本の家電を賢くするなら国産を選ぶ理由がある。","related":[("review-switchbotmini4k","💡","スマートホーム","SwitchBot ハブ2 レビュー",4.5),("review-philipshue","💡","スマートホーム","Philips Hue スターターキット レビュー",4.3),("review-applehomedpodmini","🔊","スマートスピーカー","Apple HomePod mini レビュー",4.4)]},
    # 充電器追加
    {"slug":"review-ankernano4100w","name":"Anker Nano 4 100W","cat":"充電器","emoji":"⚡","price":"¥4,990","score":4.6,"bg":"#1a237e,#283593","scores":[("出力",96,4.8),("コンパクト",100,5.0),("コスパ",98,4.9),("対応端末",94,4.7),("安全性",92,4.6)],"specs":[("出力","100W（USB-C単体）"),("ポート","USB-C×1"),("対応","PD 3.1 / PPS / QC4+"),("サイズ","約35×35×40mm"),("重量","87g"),("折りたたみ","プラグ折りたたみ式")],"pros":["5千円以下で100W出力の衝撃コスパ","87gの超軽量","35×35mmの超コンパクト","MacBook Pro 14インチも充電可","折りたたみで旅行・出張に便利"],"cons":["ポートが1つのみ","発熱は複数ポート競合機より多い","コードが別途必要"],"desc":"5千円以下でノートPCまで充電できる100W充電器。87gでポケットに入るサイズは出張の必需品。充電器沼の終着点の一つ。","related":[("review-anker733","⚡","充電器","Anker 733 GaNPrime レビュー",4.7),("review-ugreennexode140w","⚡","充電器","Ugreen Nexode 140W レビュー",4.7),("review-anker547","⚡","充電器","Anker 547 レビュー",4.5)]},
    {"slug":"review-belkin40w2port","name":"Belkin BOOST↑CHARGE PRO 40W 2ポート","cat":"充電器","emoji":"⚡","price":"¥4,480","score":4.3,"bg":"#0d47a1,#1565c0","scores":[("安全性",100,5.0),("Apple認定",100,5.0),("コスパ",88,4.4),("出力",82,4.1),("コンパクト",84,4.2)],"specs":[("出力","40W（USB-C×1 + USB-A×1）"),("USB-C","最大30W PD"),("USB-A","最大12W"),("特徴","Apple認定 Made for iPhone"),("重量","69g"),("安全","過電流・過電圧保護")],"pros":["Apple公式認定で iPhone/iPad が最適充電","過電流・過電圧・過熱の3重保護","69gの軽量","USB-A＋USB-C で2台同時充電","Belkinブランドの安心感"],"cons":["40W（ノートPCには不十分）","Ankerより高め","デザインがシンプルすぎる"],"desc":"Apple製品を安全に充電したいなら選ぶべきBelkin。Apple認定の品質保証と3重保護回路でiPhoneを大切に充電。品質に妥協しない人向け。","related":[("review-ankernano4100w","⚡","充電器","Anker Nano 4 100W レビュー",4.6),("review-anker733","⚡","充電器","Anker 733 GaNPrime レビュー",4.7),("review-anker547","⚡","充電器","Anker 547 レビュー",4.5)]},

    # 追加製品バッチ2
    # ゲーミング追加
    {"slug":"review-asusrogallyX","name":"ASUS ROG Ally X","cat":"ゲーミング","emoji":"🎮","price":"¥119,800","score":4.7,"bg":"#1a1a2e,#2d1b69","scores":[("ゲーム性能",96,4.8),("ディスプレイ",94,4.7),("携帯性",90,4.5),("バッテリー",82,4.1),("コスパ",80,4.0)],"specs":[("CPU/GPU","AMD Ryzen Z1 Extreme"),("RAM","24GB LPDDR5"),("ストレージ","1TB NVMe SSD"),("ディスプレイ","7インチ FHD 120Hz"),("バッテリー","80Wh"),("重量","678g")],"pros":["Z1 Extremeの圧倒的なAPU性能","120Hz FHDディスプレイが滑らか","24GBメモリでゲーム＋バックグラウンドも余裕","Windows 11でPC全ゲームが遊べる","外付けGPU（XG Mobile）拡張対応"],"cons":["12万円","678gと携帯ゲーム機より重い","バッテリーが2〜3時間（ゲーム時）","発熱管理が必要"],"desc":"PCゲームを持ち歩ける革命的デバイス。Steam・Epic・Xbox全部遊べるWindows PCがコントローラー付きで手のひらに。出張先のホテルでも本格ゲームが可能。","related":[("review-nintendoswitch2","🎮","ゲーミング","Nintendo Switch 2 レビュー",4.8),("review-ps5slim","🎮","ゲーミング","PlayStation 5 Slim レビュー",4.7),("review-xboxseriesx","🎮","ゲーミング","Xbox Series X レビュー",4.6)]},
    {"slug":"review-logicoolG502X","name":"Logicool G502 X Plus","cat":"ゲーミング","emoji":"🎮","price":"¥16,980","score":4.6,"bg":"#0d1b2a,#1b263b","scores":[("センサー精度",100,5.0),("ボタン配置",96,4.8),("重量調整",96,4.8),("バッテリー",90,4.5),("コスパ",88,4.4)],"specs":[("センサー","HERO 25K（最大25,600DPI）"),("接続","LIGHTSPEED / Bluetooth / 有線"),("重量","106g（最軽量時）"),("バッテリー","最大130時間"),("ボタン","13個プログラマブル"),("特徴","HYPERTENSIONバネ式クリック")],"pros":["HERO 25Kセンサーが業界最高精度","HYPERTENSIONクリックの超軽量クリック感","130時間バッテリーで充電を忘れられる","重量調整ウェイト付属","FPS・MOBA両方に最適"],"cons":["1.7万円","右手専用（左利きNG）","有線版より重い"],"desc":"FPSプロゲーマーが選ぶ最強マウス。HERO 25Kセンサーは照準の精度を限界まで高める。130時間バッテリーとHYPERTENSIONクリックで長時間プレイが快適。","related":[("review-logicoolGProXSuperlight2","🎮","ゲーミング","Logicool G Pro X Superlight 2 レビュー",4.8),("review-razerdeathadder","🎮","ゲーミング","Razer DeathAdder V3 レビュー",4.6),("review-steelseriesarctisnova","🎮","ゲーミング","SteelSeries Arctis Nova Pro レビュー",4.7)]},
    {"slug":"review-corsairK100air","name":"Corsair K100 Air Wireless","cat":"ゲーミング","emoji":"🎮","price":"¥29,800","score":4.5,"bg":"#1a0a0a,#2d1515","scores":[("キー品質",96,4.8),("ワイヤレス遅延",100,5.0),("バックライト",96,4.8),("バッテリー",88,4.4),("コスパ",80,4.0)],"specs":[("スイッチ","CORSAIR MLX Ultra-Low Profile"),("接続","SLIPSTREAM WIRELESS / Bluetooth / 有線"),("バックライト","RGB 16.8M色"),("バッテリー","200時間（バックライトオフ）"),("遅延","1ms ワイヤレス"),("重量","810g")],"pros":["SLIPSTREAM 1msワイヤレスは有線と遅延差ゼロ","200時間バッテリーで実質充電不要","Ultra-Low Profileキーで打鍵感が軽快","iCUEで全キー細かくプログラム","キーボード＋マウスのワイヤレス化で机がスッキリ"],"cons":["3万円","810gの重さ","Ultra-Low Profileの打鍵感が好みを分ける"],"desc":"ゲーミングキーボードのワイヤレス最高峰。1ms遅延で有線と体感差ゼロ、200時間バッテリーは圧倒的。机上をケーブルフリーにしたいゲーマーへ。","related":[("review-keychronk2pro","⌨️","PC周辺機器","Keychron K2 Pro レビュー",4.6),("review-logicoolG502X","🎮","ゲーミング","Logicool G502 X Plus レビュー",4.6),("review-steelseriesarctisnova","🎮","ゲーミング","SteelSeries Arctis Nova Pro レビュー",4.7)]},
    # PC周辺機器追加
    {"slug":"review-sonyinzone-m9ii","name":"Sony INZONE M9 II","cat":"PC周辺機器","emoji":"🖥️","price":"¥128,800","score":4.7,"bg":"#0d0221,#1a0a3a","scores":[("4K OLED",100,5.0),("ゲーム機能",96,4.8),("PS5連携",100,5.0),("応答速度",98,4.9),("コスパ",76,3.8)],"specs":[("パネル","WOLED 4K 144Hz"),("サイズ","27インチ"),("応答速度","0.03ms GtG"),("接続","HDMI 2.1×2 / DP 1.4×1"),("特徴","PS5 Auto HDR Tone Mapping / 1ms"),("スピーカー","内蔵2.5W×2")],"pros":["0.03ms GTGの超高速応答でゲームが超滑らか","PS5 Auto HDR Tone Mappingで自動最適化","WOLED 4Kの圧倒的画質","HDMI 2.1×2でPS5+PC同時接続","Sony INZONE ヘッドセットとの連携"],"cons":["13万円","27インチのみ","スピーカーは最低限"],"desc":"PS5ゲーマーのための最強モニター。0.03msとPS5最適化機能がゲーム体験を別次元に引き上げる。PS5持ちなら最高の選択肢。","related":[("review-dellalienware34oled","🖥️","モニター","Dell Alienware 34 OLED レビュー",4.8),("review-asusrogswiftpg279qm","🖥️","モニター","ASUS ROG Swift PG279QM レビュー",4.6),("review-ps5slim","🎮","ゲーミング","PlayStation 5 Slim レビュー",4.7)]},
    {"slug":"review-elgatovave","name":"Elgato Wave DX","cat":"PC周辺機器","emoji":"🎙️","price":"¥19,800","score":4.5,"bg":"#1a1a2e,#2d2d5e","scores":[("音質",92,4.6),("コスパ",92,4.6),("ノイズ除去",90,4.5),("設置のしやすさ",88,4.4),("配信向け",94,4.7)],"specs":[("方式","ダイナミックマイク（XLR）"),("周波数","50Hz〜20kHz"),("感度","-51dBV/Pa"),("接続","XLR（Wave XLRドック対応）"),("重量","316g"),("特徴","心臓部：ダイナミック×Wave Link")],"pros":["ダイナミック収音で周囲の音を拾わない","Wave XLRドックでUSBプラグ＆プレイ","Wave Linkで複数音源のミキシング","2万円のコスパ","Elgatoエコシステムとの親和性"],"cons":["XLRのため単体ではPCに直接接続不可","Blue Yeti XほどのUSB直結の手軽さはない","コンデンサーより音の太さが控えめ"],"desc":"配信・在宅ワークの音声品質を劇的に改善するダイナミックマイク。背景ノイズを拾わない特性がゲーム配信・会議に最適。Elgatoエコシステムと組み合わせると更に輝く。","related":[("review-blueyetix","🎙️","PC周辺機器","Blue Yeti X レビュー",4.6),("review-elgatocamlink4k","🎙️","PC周辺機器","Elgato Cam Link 4K レビュー",4.5),("review-elgatostreamdeck","🎮","ゲーミング","Elgato Stream Deck MK.2 レビュー",4.5)]},
    {"slug":"review-logicoolmxbrio4k","name":"Logicool MX Brio 4K","cat":"PC周辺機器","emoji":"📷","price":"¥27,980","score":4.6,"bg":"#1b5e20,#2e7d32","scores":[("映像品質",98,4.9),("AI背景処理",96,4.8),("コスパ",86,4.3),("接続性",90,4.5),("対応OS",92,4.6)],"specs":[("解像度","4K 30fps / 1080p 60fps"),("視野角","90°"),("AI","AI顔追跡・背景ブラー"),("接続","USB-C / USB-A"),("対応","Windows / macOS / Chrome OS"),("特徴","Logicool AI仮想背景")],"pros":["4K解像度でテレビ会議の映像が激変","AI顔追跡で動いても常にフレームに入る","AI仮想背景が自然できれい","USB-C×USB-A両対応","Teams・Zoom認定"],"cons":["2.8万円","4K 60fps非対応（30fpsまで）","AIの顔追跡は動き方による"],"desc":"テレワークの第一印象を変えるWebカメラ。4K×AIで映像品質が圧倒的に向上し、会議での印象が劇的に変わる。フルタイムリモートワーカーへの最優先投資。","related":[("review-elgatocamlink4k","📷","PC周辺機器","Elgato Cam Link 4K レビュー",4.5),("review-blueyetix","🎙️","PC周辺機器","Blue Yeti X レビュー",4.6),("review-jabra-evolve2buds","🎧","ワイヤレスイヤホン","Jabra Evolve2 Buds レビュー",4.5)]},
    # タブレット追加
    {"slug":"review-ipadprom413inch","name":"iPad Pro M4 13インチ","cat":"タブレット","emoji":"📟","price":"¥218,800","score":4.8,"bg":"#1a1a2e,#16213e","scores":[("OLED画質",100,5.0),("M4性能",100,5.0),("薄さ",100,5.0),("Apple Pencil Pro",98,4.9),("コスパ",72,3.6)],"specs":[("チップ","M4"),("ディスプレイ","13インチ Ultra Retina XDR OLED"),("厚さ","5.1mm（世界最薄）"),("重量","582g"),("Apple Pencil","Pro対応"),("接続","Thunderbolt 4 / Wi-Fi 6E")],"pros":["5.1mmという非常識な薄さ","M4チップでMacBook Pro 14と同等性能","Ultra Retina XDR OLEDの圧倒的画質","Apple Pencil Proの触感フィードバック","Thunderbolt 4で4Kモニター出力可"],"cons":["22万円","Magic Keyboard別売りでPC化に追加費用","重量は582gあるため長時間持つのは辛い"],"desc":"コンピューターの概念を変える13インチOLEDタブレット。5.1mmの薄さとM4の性能は他の追随を許さない。クリエイターがMacBookの代わりに選ぶ時代が来た。","related":[("review-ipadprom4","📟","タブレット","iPad Pro M4 11インチ レビュー",4.7),("review-ipadairm2","📟","タブレット","iPad Air M2 レビュー",4.5),("review-galaxytabs10ultra","📟","タブレット","Galaxy Tab S10 Ultra レビュー",4.6)]},
    {"slug":"review-galaxytabs10FE","name":"Samsung Galaxy Tab S10 FE","cat":"タブレット","emoji":"📟","price":"¥79,800","score":4.3,"bg":"#1a237e,#283593","scores":[("コスパ",92,4.6),("S Pen",100,5.0),("画面サイズ",90,4.5),("性能",80,4.0),("バッテリー",88,4.4)],"specs":[("チップ","Exynos 1580"),("ディスプレイ","10.9インチ TFT LCD 90Hz"),("S Pen","付属"),("バッテリー","10,090mAh"),("重量","523g"),("接続","Wi-Fi 6 / 5G対応モデルあり")],"pros":["S Pen付属で8万円のコスパ","10,090mAhの大容量バッテリー","90Hzで動作が滑らか","Galaxy AIの一部機能対応","10.9インチの大画面"],"cons":["LCD（OLEDではない）","Exynos 1580はミドルレンジ","Tab S10 Ultraに劣る仕上がり感"],"desc":"S Penを8万円で入手できるGalaxyタブレット入門機。手書きメモ・スケッチが標準機能として使えるコスパは国内最高水準。学生・ビジネスマンに最適。","related":[("review-galaxytabs10ultra","📟","タブレット","Galaxy Tab S10 Ultra レビュー",4.6),("review-ipadairm2","📟","タブレット","iPad Air M2 レビュー",4.5),("review-ipadprom4","📟","タブレット","iPad Pro M4 レビュー",4.7)]},
    # スマートウォッチ追加
    {"slug":"review-applewatchseries10","name":"Apple Watch Series 10 46mm","cat":"スマートウォッチ","emoji":"⌚","price":"¥62,800","score":4.7,"bg":"#1a1a2e,#16213e","scores":[("健康機能",96,4.8),("薄さ",100,5.0),("睡眠追跡",96,4.8),("Apple連携",100,5.0),("コスパ",80,4.0)],"specs":[("ディスプレイ","46mm LTPO OLED Always-On"),("チップ","S10"),("薄さ","9.7mm（過去最薄）"),("センサー","心拍・血中酸素・水温・睡眠無呼吸検知"),("防水","50m防水"),("特徴","睡眠時無呼吸症候群検知（新機能）")],"pros":["睡眠時無呼吸症候群検知が追加（世界初）","9.7mmの過去最薄設計","水温センサーで海・プール対応","LTPO Always-Onで常時表示","iPhoneユーザーに最も統合された体験"],"cons":["6.3万円","Android非対応","バッテリーは18〜36時間（競合に劣る）"],"desc":"睡眠時無呼吸症候群を検知できるようになった最新Apple Watch。9.7mmの薄さと健康管理機能の充実度でiPhoneユーザーの最高の相棒に。","related":[("review-applewatchs10","⌚","スマートウォッチ","Apple Watch S10 レビュー",4.6),("review-applewatchultra2","⌚","スマートウォッチ","Apple Watch Ultra 2 レビュー",4.8),("review-galaxywatch7","⌚","スマートウォッチ","Galaxy Watch 7 レビュー",4.5)]},
    {"slug":"review-garminvivomove5","name":"Garmin Vívomove Sport","cat":"スマートウォッチ","emoji":"⌚","price":"¥28,800","score":4.2,"bg":"#1b5e20,#2e7d32","scores":[("デザイン",98,4.9),("健康追跡",86,4.3),("コスパ",90,4.5),("バッテリー",88,4.4),("アナログ感",100,5.0)],"specs":[("デザイン","アナログ時計×隠しディスプレイ"),("センサー","心拍・ストレス・血中酸素"),("バッテリー","最大5日"),("防水","5ATM"),("接続","Bluetooth"),("特徴","隠れたデジタルディスプレイ")],"pros":["アナログ時計に見えるスマートウォッチ","職場でも使えるビジネス対応デザイン","2.9万円のコスパ","5ATM防水","Garmin Connectとの連携"],"cons":["Garmin上位機より健康機能が少ない","ディスプレイが小さく情報量が少ない","GPS非内蔵"],"desc":"スマートウォッチを着けていると思われたくない人のための一台。アナログ時計の見た目でスマートウォッチ機能を隠し持つ。ビジネスシーンでも完全に馴染む。","related":[("review-garminvenu3","⌚","スマートウォッチ","Garmin Venu 3 レビュー",4.5),("review-withingsscanwatch2","⌚","スマートウォッチ","Withings ScanWatch 2 レビュー",4.5),("review-amazfitgtr4","⌚","スマートウォッチ","Amazfit GTR 4 レビュー",4.2)]},
    # ノートPC追加
    {"slug":"review-asuszenbook14oled","name":"ASUS Zenbook 14 OLED","cat":"ノートPC","emoji":"💻","price":"¥149,800","score":4.6,"bg":"#1a237e,#283593","scores":[("OLED画質",100,5.0),("コスパ",88,4.4),("軽量性",90,4.5),("バッテリー",86,4.3),("性能",90,4.5)],"specs":[("CPU","AMD Ryzen 7 8840HS"),("ディスプレイ","14インチ 2.8K OLED 120Hz"),("RAM","16GB LPDDR5X"),("SSD","512GB NVMe"),("重量","1.2kg"),("バッテリー","最大15時間")],"pros":["15万円で14インチ2.8K OLED×120Hz","1.2kgの軽量","OLEDで映画・写真編集が圧倒的に美しい","Ryzen 7 8840HSの高性能NPU（AI機能）","15時間バッテリー"],"cons":["512GBは拡張が限られる","AMD GPUは一部ソフトで動作確認必要","冷却がやや弱い（連続高負荷時）"],"desc":"15万円でOLEDディスプレイとRyzen 7を両立したコスパ最強ノートPC。写真・動画編集からビジネス用途まで。OLEDの美しさは一度使うと戻れない。","related":[("review-macbookairm3","💻","ノートPC","MacBook Air M3 レビュー",4.7),("review-dellxps15","💻","ノートPC","Dell XPS 15 レビュー",4.7),("review-hpspectrex360","💻","ノートPC","HP Spectre x360 レビュー",4.6)]},
    {"slug":"review-lenovo-yoga9i","name":"Lenovo Yoga 9i Gen 9","cat":"ノートPC","emoji":"💻","price":"¥179,800","score":4.5,"bg":"#212121,#424242","scores":[("2-in-1設計",100,5.0),("ディスプレイ",96,4.8),("音質",98,4.9),("バッテリー",90,4.5),("コスパ",78,3.9)],"specs":[("CPU","Intel Core Ultra 7 155H"),("ディスプレイ","14インチ OLED 2.8K タッチ"),("RAM","16GB"),("音声","Bose スピーカー×4"),("重量","1.35kg"),("特徴","360°ヒンジ / ペン付属")],"pros":["360°ヒンジでタブレットとして使える","Bose 4スピーカーがノートPC最高水準の音質","OLED 2.8Kタッチディスプレイ","ペン付属で手書き入力即対応","デザインが洗練されている"],"cons":["18万円","1.35kgはビジネスモバイルでは重め","Core Ultra 7は高負荷で発熱"],"desc":"タブレットにもなるプレミアムノートPC。BoseスピーカーとOLEDの組み合わせは他社の追随を許さない。音楽・映画・創作活動に理想の相棒。","related":[("review-hpspectrex360","💻","ノートPC","HP Spectre x360 レビュー",4.6),("review-macbookairm3","💻","ノートPC","MacBook Air M3 レビュー",4.7),("review-surfacepro11","📟","タブレット","Surface Pro 11 レビュー",4.4)]},
    # スマートフォン追加2
    {"slug":"review-googlepixel9proXL","name":"Google Pixel 9 Pro XL","cat":"スマートフォン","emoji":"📱","price":"¥189,900","score":4.8,"bg":"#1a237e,#283593","scores":[("AI機能",100,5.0),("カメラ",98,4.9),("バッテリー",94,4.7),("Tensor G4",92,4.6),("コスパ",76,3.8)],"specs":[("ディスプレイ","6.8インチ LTPO OLED 1〜120Hz"),("チップ","Google Tensor G4"),("カメラ","50MP+48MP超広角+48MP 5倍望遠"),("バッテリー","5,060mAh 37W"),("重量","221g"),("AI","Google AI Overviews / Gemini統合")],"pros":["Gemini AI統合で最も賢いAndroid","5060mAhで1日以上安心","カメラが全シーン最強クラス（6.8インチモデル）","最長7年のOS・セキュリティアップデート","Pixel Dropsで機能が増え続ける"],"cons":["19万円","Tensor G4は発熱が課題","5倍以上のズームはiPhone 16 Pro Maxに劣る"],"desc":"GoogleのAI能力が最大限発揮される最高峰Pixel。Gemini統合×7年更新保証は他のAndroidが追いつけない強み。AI機能を活用したいならPixel 9 Pro XL。","related":[("review-pixel9pro","📱","スマートフォン","Google Pixel 9 Pro レビュー",4.7),("review-iphone16promax","📱","スマートフォン","iPhone 16 Pro Max レビュー",4.9),("review-galaxys25ultra","📱","スマートフォン","Samsung Galaxy S25 Ultra レビュー",4.8)]},
    {"slug":"review-iphone16promaxnatural","name":"iPhone 16 Pro 256GB","cat":"スマートフォン","emoji":"📱","price":"¥159,800","score":4.8,"bg":"#2d2d2d,#3d3d3d","scores":[("カメラ",98,4.9),("A18 Pro",100,5.0),("コンパクト性",90,4.5),("バッテリー",90,4.5),("コスパ",76,3.8)],"specs":[("ディスプレイ","6.3インチ Super Retina XDR 120Hz"),("チップ","A18 Pro（3nm）"),("カメラ","48MP+48MP+5倍光学ズーム"),("バッテリー","最大27時間"),("重量","199g"),("特徴","カメラコントロール / ProRes 4K 120fps")],"pros":["Pro Maxと同じカメラ・チップで199g","6.3インチはPro Maxより片手操作しやすい","ProRes 4K 120fpsの動画が撮れる","チタン素材の高級感","Pro Maxより3.5万円安い"],"cons":["16万円","バッテリーはPro Maxに劣る","USB-Cは3.0（Pro Max同様）"],"desc":"Pro Maxと同じカメラ・チップを199gに収めた最強コンパクトiPhone Pro。Pro Maxは大きすぎると感じる人のベストアンサー。性能は全く妥協なし。","related":[("review-iphone16promax","📱","スマートフォン","iPhone 16 Pro Max レビュー",4.9),("review-iphone16","📱","スマートフォン","iPhone 16 レビュー",4.5),("review-pixel9pro","📱","スマートフォン","Google Pixel 9 Pro レビュー",4.7)]},
    {"slug":"review-xiaomi15","name":"Xiaomi 15","cat":"スマートフォン","emoji":"📱","price":"¥129,800","score":4.7,"bg":"#ff6d00,#1a1a1a","scores":[("コスパ",96,4.8),("カメラ",96,4.8),("Snapdragon 8 Elite",100,5.0),("充電速度",96,4.8),("バッテリー",90,4.5)],"specs":[("チップ","Snapdragon 8 Elite"),("カメラ","50MP×3（Leica共同開発）"),("充電","90W有線 + 50Wワイヤレス"),("バッテリー","5,240mAh"),("重量","190g"),("特徴","Leica Summilux光学系")],"pros":["Leica共同開発カメラが写真をアート作品に","90Wで40分フル充電","Snapdragon 8 Eliteで最強性能","5,240mAhで2日使える","13万円でフラッグシップ全部入り"],"cons":["グローバルモデルで日本語サポートが限定的","Leica効果は使い方に依存","Google標準より独自UIの使い勝手が好み分かれる"],"desc":"Leicaカメラ×Snapdragon 8 Elite×90Wを13万円で実現した価格破壊フラッグシップ。写真を芸術的に撮りたい人にとってXiaomi 15は最高の相棒。","related":[("review-xiaomi14ultra","📱","スマートフォン","Xiaomi 14 Ultra レビュー",4.7),("review-oppofindx8pro","📱","スマートフォン","OPPO Find X8 Pro レビュー",4.5),("review-oneplus13","📱","スマートフォン","OnePlus 13 レビュー",4.6)]},
    # カメラ追加
    {"slug":"review-omSystem-OM5","name":"OM SYSTEM OM-5 Mark II","cat":"カメラ","emoji":"📷","price":"¥119,800","score":4.5,"bg":"#1a237e,#283593","scores":[("防塵防滴",100,5.0),("手ブレ補正",100,5.0),("コンパクト性",96,4.8),("画質",86,4.3),("コスパ",82,4.1)],"specs":[("センサー","マイクロフォーサーズ 2037万画素"),("手ブレ補正","最大7.5段（ボディ内）"),("防塵防滴","IP53（マイナス10℃耐低温）"),("重量","414g"),("連写","最大30コマ/秒"),("特徴","野生動物AF / 最大240コマ高解像度合成")],"pros":["IP53防塵防滴でマイナス10℃まで対応","7.5段手ブレ補正で夜景手持ち可能","414gの超軽量","野生動物・乗り物AFの精度が高い","OM SYSTEMの山岳・アウトドア向け設計"],"cons":["マイクロフォーサーズはフルサイズより高感度が劣る","動画は4K 30fps止まり","12万円は競合比でやや高め"],"desc":"アウトドア・旅行カメラの最高峰。IP53防塵防滴でマイナス10℃まで動作し、7.5段手ブレ補正で激しい環境でも撮り逃しゼロ。山岳カメラマンの愛機。","related":[("review-fujifilmx100vi","📷","カメラ","Fujifilm X100VI レビュー",4.9),("review-fujifilmxt5","📷","カメラ","Fujifilm X-T5 レビュー",4.8),("review-goprohero13black","📷","カメラ","GoPro HERO13 Black レビュー",4.6)]},
    # スピーカー追加
    {"slug":"review-marshallEmberton3","name":"Marshall Emberton III","cat":"スピーカー","emoji":"🔊","price":"¥19,800","score":4.4,"bg":"#1a1a0a,#2a2a0a","scores":[("デザイン",100,5.0),("音質",88,4.4),("防水",94,4.7),("コスパ",90,4.5),("バッテリー",86,4.3)],"specs":[("出力","5W×2（ステレオ）"),("防水","IP67"),("バッテリー","最大30時間"),("接続","Bluetooth 5.3"),("重量","700g"),("特徴","ロック感あふれるクラシックデザイン")],"pros":["30時間バッテリーが圧倒的","Marshallのヴィンテージデザインがインテリアになる","IP67で屋外・風呂でも使える","ステレオ出力で左右の分離感","2万円のコスパ"],"cons":["700gはポータブルとして重め","低音はSONY XB43より控えめ","Bluetooth 5.3のみ（Wi-Fi非対応）"],"desc":"音楽と一緒に生きるブランドMarshallのポータブルスピーカー。30時間バッテリーとヴィンテージデザインがインテリアと音楽生活を同時に格上げする。","related":[("review-jblflip6","🔊","スピーカー","JBL Flip 6 レビュー",4.5),("review-boseSoundLinkMax","🔊","スピーカー","Bose SoundLink Max レビュー",4.7),("review-sonysrsxb43","🔊","スピーカー","Sony SRS-XB43 レビュー",4.5)]},
    # ワイヤレスイヤホン追加
    {"slug":"review-bose-ultra-earbuds","name":"Bose Ultra Open Earbuds","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥39,600","score":4.5,"bg":"#1b5e20,#2e7d32","scores":[("開放感",100,5.0),("音質",86,4.3),("オープンイヤー安全性",100,5.0),("コスパ",78,3.9),("装着感",92,4.6)],"specs":[("方式","オープンイヤー（耳をふさがない）"),("再生時間","7時間（ケース含48時間）"),("防水","IPX4"),("接続","Bluetooth 5.3"),("重量","8.2g"),("特徴","OpenAudio技術")],"pros":["耳をふさがないので外音が聞こえる安全性","Boseの音質クォリティをオープンで実現","48時間ケース込みバッテリー","独自クリップで耳に安定装着","通話しながら外音が聞こえる自然な体験"],"cons":["4万円","音漏れがある（公共の場で注意）","ANCなし（オープンイヤーの仕様上）"],"desc":"耳をふさがない新体験を4万円で。外の音が聞こえるオープンイヤーはランニング・オフィス・育児に最適。Boseの音質でオープンイヤー市場を塗り替えた一台。","related":[("review-shokzOpenRunPro2","🎧","ワイヤレスイヤホン","Shokz OpenRun Pro 2 レビュー",4.4),("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8),("review-boseqcearbuds2","🎧","ワイヤレスイヤホン","Bose QC Earbuds II レビュー",4.6)]},
    {"slug":"review-sony-wf1000xm5-sport","name":"Sony WF-SP910N","cat":"ワイヤレスイヤホン","emoji":"🎧","price":"¥18,980","score":4.3,"bg":"#006064,#00838f","scores":[("スポーツ向け",96,4.8),("ANC",84,4.2),("防水",96,4.8),("コスパ",90,4.5),("音質",82,4.1)],"specs":[("ANC","対応"),("防水","IPX4（スポーツ向け）"),("再生時間","9時間（ANCオン）"),("接続","Bluetooth 5.0"),("重量","6.5g"),("特徴","Sony 360 Reality Audio部分対応")],"pros":["IPX4でジムのシャワーでも安心","1.9万円のコスパ","ANC対応でトレーニングに集中","ソニーの安心品質","フィット感がスポーツ時に安定"],"cons":["フラッグシップWF-1000XM5より音質が劣る","ANCはWF-1000XM5に大差をつけられる","デザインがスポーティで普段使いに合わないことも"],"desc":"ジム・ランニング・スポーツ専用ならこれで完結。IPX4防水×ANC×ソニー品質で2万円以下という圧倒的コスパ。汗・水に強いスポーツイヤホンの定番。","related":[("review-shokzOpenRunPro2","🎧","ワイヤレスイヤホン","Shokz OpenRun Pro 2 レビュー",4.4),("review-sonywf1000xm5","🎧","ワイヤレスイヤホン","Sony WF-1000XM5 レビュー",4.8),("review-ankerliberty4nc","🎧","ワイヤレスイヤホン","Anker Liberty 4 NC レビュー",4.5)]},
    # モニター追加
    {"slug":"review-asusproadart27","name":"ASUS ProArt PA27UCX-K 27インチ","cat":"モニター","emoji":"🖥️","price":"¥198,000","score":4.7,"bg":"#1a237e,#283593","scores":[("色精度",100,5.0),("HDR",100,5.0),("クリエイター向け",100,5.0),("コスパ",72,3.6),("接続性",96,4.8)],"specs":[("パネル","IPS 4K 60Hz"),("色域","DCI-P3 99% / Adobe RGB 99%"),("HDR","DisplayHDR 1000（True Black）"),("キャリブレーション","ハードウェアキャリブレーション対応"),("接続","Thunderbolt 3×2 / HDMI 2.0×2"),("特徴","Delta E < 2 の出荷時校正済み")],"pros":["Delta E <2の出荷時色校正済み","DCI-P3 99%×Adobe RGB 99%×DisplayHDR 1000","ハードウェアキャリブレーション対応","Thunderbolt 3×2でMacとの連携が完璧","写真・映像・印刷に完璧な色再現"],"cons":["20万円","4K 60Hz（ゲーム向きではない）","重量が重い"],"desc":"プロフォトグラファー・映像クリエイターの最高峰モニター。出荷時の色校正済みでキャリブレーション不要から即戦力。色で妥協できない人への究極の答え。","related":[("review-benqpd3205u","🖥️","モニター","BenQ PD3205U レビュー",4.6),("review-lgultrafine5k27md5kl","🖥️","モニター","LG UltraFine 5K レビュー",4.6),("review-dellalienware34oled","🖥️","モニター","Dell Alienware 34 OLED レビュー",4.8)]},
    {"slug":"review-boseqc45","name":"Bose QuietComfort 45","cat":"PC周辺機器","emoji":"🎧","price":"¥37,400","score":4.6,"bg":"#0a3622,#14532d","scores":[("ノイキャン",92,4.6),("装着感",96,4.8),("バッテリー",90,4.5),("音質",86,4.3),("コスパ",84,4.2)],"specs":[("ドライバー","40mm"),("ノイキャン","TriPort ANC"),("再生時間","22時間"),("充電","USB-C / 15分で3時間"),("重量","237g"),("コーデック","AAC / SBC")],"pros":["237gの軽量で長時間装着が快適","22時間の長バッテリー","15分急速充電で3時間再生","Bose特有の柔らかいANCが快適","折りたたみで収納コンパクト"],"cons":["ANC性能はWH-1000XM5に劣る","aptX非対応","Bluetoothのみ（有線は3.5mm）","XM5と比較すると音質でやや劣る"],"desc":"長時間着けても疲れない快適さが最大の強み。フライト・テレワーク・通勤で1日中装着しても苦にならない。","related":[("review-sonywh1000xm5","🎧","PC周辺機器","Sony WH-1000XM5 レビュー",4.8),("review-boseqcearbuds2","🎧","ワイヤレスイヤホン","Bose QC Earbuds II レビュー",4.6),("review-airpods-pro2","🎧","ワイヤレスイヤホン","AirPods Pro 2 レビュー",4.8)]},
]

CAT_SVG_DECO = {
    "スマートフォン": '''
        <rect x="320" y="55" width="160" height="285" rx="24" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="333" y="88" width="134" height="210" rx="8" fill="rgba(255,255,255,0.07)"/>
        <rect x="368" y="328" width="64" height="6" rx="3" fill="rgba(255,255,255,0.3)"/>
        <circle cx="400" cy="73" r="5" fill="rgba(255,255,255,0.25)"/>''',
    "ワイヤレスイヤホン": '''
        <ellipse cx="320" cy="135" rx="42" ry="58" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <ellipse cx="480" cy="135" rx="42" ry="58" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <path d="M362 195 Q400 230 438 195" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <rect x="345" y="218" width="110" height="46" rx="23" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>''',
    "スマートウォッチ": '''
        <rect x="338" y="52" width="124" height="166" rx="36" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="352" y="72" width="96" height="126" rx="22" fill="rgba(255,255,255,0.07)"/>
        <rect x="356" y="28" width="22" height="28" rx="6" fill="rgba(255,255,255,0.2)"/>
        <rect x="422" y="28" width="22" height="28" rx="6" fill="rgba(255,255,255,0.2)"/>
        <rect x="356" y="218" width="88" height="22" rx="11" fill="rgba(255,255,255,0.15)"/>''',
    "ノートPC": '''
        <rect x="235" y="75" width="330" height="210" rx="14" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="249" y="90" width="302" height="180" rx="7" fill="rgba(255,255,255,0.07)"/>
        <path d="M175 285 Q400 268 625 285" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="14" stroke-linecap="round"/>''',
    "タブレット": '''
        <rect x="255" y="50" width="290" height="195" rx="18" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="268" y="63" width="264" height="169" rx="9" fill="rgba(255,255,255,0.07)"/>
        <circle cx="400" cy="262" r="13" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>''',
    "カメラ": '''
        <rect x="240" y="90" width="320" height="200" rx="22" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <circle cx="400" cy="190" r="70" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <circle cx="400" cy="190" r="44" fill="rgba(255,255,255,0.07)"/>
        <circle cx="400" cy="190" r="18" fill="rgba(255,255,255,0.12)"/>
        <rect x="290" y="75" width="62" height="20" rx="7" fill="rgba(255,255,255,0.2)"/>''',
    "ゲーミング": '''
        <rect x="255" y="90" width="290" height="175" rx="32" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <circle cx="338" cy="182" r="24" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <circle cx="462" cy="160" r="11" fill="rgba(255,255,255,0.15)"/>
        <circle cx="483" cy="182" r="11" fill="rgba(255,255,255,0.15)"/>
        <circle cx="462" cy="204" r="11" fill="rgba(255,255,255,0.15)"/>
        <circle cx="441" cy="182" r="11" fill="rgba(255,255,255,0.15)"/>''',
    "モニター": '''
        <rect x="215" y="60" width="370" height="210" rx="14" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="228" y="73" width="344" height="184" rx="7" fill="rgba(255,255,255,0.07)"/>
        <path d="M362 270 L438 270 L445 295 L355 295 Z" fill="rgba(255,255,255,0.15)"/>
        <rect x="335" y="294" width="130" height="9" rx="4" fill="rgba(255,255,255,0.15)"/>''',
    "PC周辺機器": '''
        <rect x="265" y="125" width="270" height="95" rx="14" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="280" y="138" width="28" height="22" rx="5" fill="rgba(255,255,255,0.15)"/>
        <rect x="316" y="138" width="22" height="22" rx="5" fill="rgba(255,255,255,0.15)"/>
        <rect x="346" y="138" width="22" height="22" rx="5" fill="rgba(255,255,255,0.15)"/>
        <circle cx="472" cy="215" r="32" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="3"/>
        <circle cx="472" cy="215" r="10" fill="rgba(255,255,255,0.15)"/>''',
    "充電器": '''
        <rect x="342" y="68" width="116" height="136" rx="20" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="373" y="204" width="18" height="52" rx="5" fill="rgba(255,255,255,0.22)"/>
        <rect x="409" y="204" width="18" height="52" rx="5" fill="rgba(255,255,255,0.22)"/>
        <circle cx="400" cy="136" r="22" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>''',
    "モバイルバッテリー": '''
        <rect x="298" y="100" width="204" height="105" rx="18" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="500" y="122" width="18" height="62" rx="7" fill="rgba(255,255,255,0.22)"/>
        <rect x="316" y="118" width="52" height="70" rx="5" fill="rgba(255,255,255,0.2)"/>
        <rect x="376" y="118" width="52" height="70" rx="5" fill="rgba(255,255,255,0.12)"/>
        <rect x="436" y="118" width="52" height="70" rx="5" fill="rgba(255,255,255,0.06)"/>''',
    "スマートスピーカー": '''
        <ellipse cx="400" cy="175" rx="82" ry="115" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <line x1="328" y1="140" x2="472" y2="140" stroke="rgba(255,255,255,0.1)" stroke-width="2"/>
        <line x1="323" y1="165" x2="477" y2="165" stroke="rgba(255,255,255,0.1)" stroke-width="2"/>
        <line x1="322" y1="190" x2="478" y2="190" stroke="rgba(255,255,255,0.1)" stroke-width="2"/>
        <line x1="328" y1="215" x2="472" y2="215" stroke="rgba(255,255,255,0.1)" stroke-width="2"/>''',
    "スピーカー": '''
        <rect x="288" y="75" width="224" height="200" rx="22" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <circle cx="400" cy="165" r="68" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <circle cx="400" cy="165" r="42" fill="rgba(255,255,255,0.07)"/>
        <circle cx="400" cy="165" r="16" fill="rgba(255,255,255,0.18)"/>''',
    "VR/AR": '''
        <path d="M235 175 Q235 128 278 128 L522 128 Q565 128 565 175 Q565 222 522 222 L278 222 Q235 222 235 175 Z" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <circle cx="338" cy="175" r="36" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <circle cx="462" cy="175" r="36" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <rect x="374" y="165" width="52" height="20" rx="4" fill="rgba(255,255,255,0.15)"/>''',
    "電子書籍リーダー": '''
        <rect x="308" y="55" width="184" height="250" rx="14" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="322" y="75" width="156" height="190" rx="6" fill="rgba(255,255,255,0.07)"/>
        <line x1="335" y1="115" x2="465" y2="115" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <line x1="335" y1="140" x2="465" y2="140" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <line x1="335" y1="165" x2="465" y2="165" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <line x1="335" y1="190" x2="430" y2="190" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>''',
    "スマートホーム": '''
        <path d="M400 68 L525 158 L525 275 L275 275 L275 158 Z" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="366" y="198" width="68" height="77" rx="9" fill="rgba(255,255,255,0.1)"/>
        <rect x="290" y="186" width="62" height="52" rx="7" fill="rgba(255,255,255,0.1)"/>
        <rect x="448" y="186" width="62" height="52" rx="7" fill="rgba(255,255,255,0.1)"/>''',
    "エンタメ": '''
        <rect x="268" y="100" width="264" height="160" rx="14" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <circle cx="344" cy="228" r="22" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <circle cx="456" cy="228" r="22" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <circle cx="400" cy="180" r="28" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <polygon points="392,170 416,180 392,190" fill="rgba(255,255,255,0.3)"/>''',
    "テレビ": '''
        <rect x="200" y="60" width="400" height="220" rx="16" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="214" y="74" width="372" height="192" rx="8" fill="rgba(255,255,255,0.07)"/>
        <path d="M350 280 L380 280 L390 305 L410 305 L420 280 L450 280" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <rect x="300" y="306" width="200" height="8" rx="4" fill="rgba(255,255,255,0.15)"/>''',
    "ドライヤー": '''
        <ellipse cx="350" cy="165" rx="80" ry="80" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <path d="M430 165 L530 165" stroke="rgba(255,255,255,0.3)" stroke-width="14" stroke-linecap="round"/>
        <path d="M350 85 Q420 60 460 90" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <path d="M350 245 Q420 270 460 240" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <line x1="460" y1="100" x2="510" y2="80" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <line x1="460" y1="165" x2="520" y2="165" stroke="rgba(255,255,255,0.1)" stroke-width="2"/>
        <line x1="460" y1="230" x2="510" y2="250" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>''',
    "電動歯ブラシ": '''
        <rect x="368" y="52" width="64" height="220" rx="32" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="380" y="52" width="40" height="70" rx="20" fill="rgba(255,255,255,0.18)"/>
        <line x1="340" y1="130" x2="460" y2="130" stroke="rgba(255,255,255,0.1)" stroke-width="2"/>
        <circle cx="400" cy="198" r="16" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>''',
    "シェーバー": '''
        <rect x="320" y="60" width="160" height="240" rx="30" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="338" y="75" width="124" height="80" rx="20" fill="rgba(255,255,255,0.12)"/>
        <rect x="338" y="168" width="38" height="38" rx="8" fill="rgba(255,255,255,0.1)"/>
        <rect x="384" y="168" width="38" height="38" rx="8" fill="rgba(255,255,255,0.1)"/>
        <rect x="338" y="214" width="124" height="16" rx="6" fill="rgba(255,255,255,0.15)"/>''',
    "ロボット掃除機": '''
        <circle cx="400" cy="165" r="120" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <circle cx="400" cy="165" r="70" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <circle cx="400" cy="165" r="20" fill="rgba(255,255,255,0.2)"/>
        <circle cx="370" cy="100" r="10" fill="rgba(255,255,255,0.25)"/>
        <circle cx="430" cy="100" r="10" fill="rgba(255,255,255,0.25)"/>''',
    "コーヒーメーカー": '''
        <rect x="300" y="80" width="120" height="180" rx="16" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="420" y="160" width="60" height="80" rx="10" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <path d="M340 200 Q360 230 380 200" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round"/>
        <path d="M310 80 Q330 45 360 55 Q390 45 380 80" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <line x1="316" y1="155" x2="416" y2="155" stroke="rgba(255,255,255,0.1)" stroke-width="2"/>''',
    "プロジェクター": '''
        <rect x="240" y="120" width="240" height="120" rx="18" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <circle cx="310" cy="180" r="36" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <circle cx="310" cy="180" r="18" fill="rgba(255,255,255,0.18)"/>
        <path d="M480 120 L570 60 M480 240 L570 300 M480 180 L590 180" stroke="rgba(255,255,255,0.12)" stroke-width="2"/>''',
    "サウンドバー": '''
        <rect x="180" y="145" width="440" height="80" rx="18" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <circle cx="230" cy="185" r="18" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.18)" stroke-width="2"/>
        <circle cx="570" cy="185" r="18" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.18)" stroke-width="2"/>
        <line x1="265" y1="160" x2="540" y2="160" stroke="rgba(255,255,255,0.08)" stroke-width="3"/>
        <line x1="265" y1="185" x2="540" y2="185" stroke="rgba(255,255,255,0.08)" stroke-width="3"/>
        <line x1="265" y1="210" x2="540" y2="210" stroke="rgba(255,255,255,0.08)" stroke-width="3"/>''',
    "ネットワーク機器": '''
        <rect x="310" y="110" width="180" height="130" rx="16" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <line x1="400" y1="110" x2="400" y2="60" stroke="rgba(255,255,255,0.2)" stroke-width="3"/>
        <line x1="400" y1="60" x2="320" y2="30" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <line x1="400" y1="60" x2="480" y2="30" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
        <line x1="400" y1="240" x2="310" y2="270" stroke="rgba(255,255,255,0.12)" stroke-width="2"/>
        <line x1="400" y1="240" x2="400" y2="275" stroke="rgba(255,255,255,0.12)" stroke-width="2"/>
        <line x1="400" y1="240" x2="490" y2="270" stroke="rgba(255,255,255,0.12)" stroke-width="2"/>''',
    "ゲーミングチェア": '''
        <path d="M320 80 Q280 80 275 140 L275 220 Q275 260 310 270 L310 290 Q310 310 340 310 L460 310 Q490 310 490 290 L490 270 Q525 260 525 220 L525 140 Q520 80 480 80 Z" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="315" y="130" width="170" height="100" rx="12" fill="rgba(255,255,255,0.07)"/>
        <circle cx="320" cy="310" r="18" fill="rgba(255,255,255,0.15)"/>
        <circle cx="480" cy="310" r="18" fill="rgba(255,255,255,0.15)"/>''',
    "コードレス掃除機": '''
        <rect x="370" y="50" width="40" height="220" rx="10" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <path d="M370 270 Q350 290 300 295 L280 295 L280 300 Q280 310 290 310 L500 310 Q510 310 510 300 L510 295 L490 295 Q440 290 420 270 Z" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>
        <rect x="340" y="50" width="100" height="40" rx="12" fill="rgba(255,255,255,0.15)"/>
        <line x1="390" y1="220" x2="430" y2="280" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>''',
    "調理家電": '''
        <rect x="250" y="100" width="300" height="180" rx="20" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <rect x="268" y="118" width="264" height="144" rx="10" fill="rgba(255,255,255,0.07)"/>
        <circle cx="310" cy="80" r="18" fill="rgba(255,255,255,0.18)"/>
        <circle cx="370" cy="80" r="18" fill="rgba(255,255,255,0.18)"/>
        <circle cx="430" cy="80" r="18" fill="rgba(255,255,255,0.18)"/>
        <circle cx="490" cy="80" r="18" fill="rgba(255,255,255,0.18)"/>''',
    "家電": '''
        <ellipse cx="400" cy="120" rx="95" ry="55" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <path d="M305 120 L305 230 Q305 260 400 260 Q495 260 495 230 L495 120" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3"/>
        <line x1="340" y1="155" x2="460" y2="155" stroke="rgba(255,255,255,0.12)" stroke-width="2"/>
        <line x1="335" y1="185" x2="465" y2="185" stroke="rgba(255,255,255,0.12)" stroke-width="2"/>
        <line x1="335" y1="215" x2="465" y2="215" stroke="rgba(255,255,255,0.12)" stroke-width="2"/>''',
}

def make_hero_svg(p):
    bg1, bg2 = [c.strip() for c in p["bg"].split(",")]
    deco = CAT_SVG_DECO.get(p["cat"], "")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 300">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
  </defs>
  <rect width="800" height="300" fill="url(#g)"/>
  {deco}
</svg>'''
    encoded = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"

CAT_IMAGES = {
    "スマートフォン":      "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&q=80",
    "ワイヤレスイヤホン":  "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&q=80",
    "スマートウォッチ":    "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&q=80",
    "ノートPC":            "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&q=80",
    "カメラ":              "https://images.unsplash.com/photo-1502920917128-1aa500764765?w=800&q=80",
    "ゲーミング":          "https://images.unsplash.com/photo-1592478411213-6153e4ebc07d?w=800&q=80",
    "モニター":            "https://images.unsplash.com/photo-1593640495253-23196b27a87f?w=800&q=80",
    "タブレット":          "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&q=80",
    "PC周辺機器":          "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&q=80",
    "充電器":              "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=800&q=80",
    "モバイルバッテリー":  "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=800&q=80",
    "スマートスピーカー":  "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
    "スピーカー":          "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=800&q=80",
    "VR/AR":               "https://images.unsplash.com/photo-1617802690992-c344b8f57fad?w=800&q=80",
    "電子書籍リーダー":    "https://images.unsplash.com/photo-1507842217343-583bb97e8949?w=800&q=80",
    "スマートホーム":      "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
    "エンタメ":            "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=800&q=80",
    "家電":                "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800&q=80",
}

REVIEW_STYLE = """
    .review-page { max-width: 800px; margin: 0 auto; padding: 40px 20px 80px; }
    .breadcrumb { font-size: 0.8rem; color: var(--text-light); margin-bottom: 24px; display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
    .breadcrumb a { color: var(--primary); }
    .breadcrumb span { color: #bbb; }
    .article-header { margin-bottom: 32px; }
    .article-category { display: inline-block; background: var(--primary); color: var(--white); font-size: 0.75rem; font-weight: 700; padding: 4px 14px; border-radius: 20px; margin-bottom: 12px; }
    .article-header h1 { font-size: clamp(1.4rem, 3.5vw, 2rem); font-weight: 800; line-height: 1.4; margin-bottom: 16px; }
    .article-meta { display: flex; align-items: center; gap: 16px; font-size: 0.82rem; color: var(--text-light); flex-wrap: wrap; }
    .article-meta .author { display: flex; align-items: center; gap: 6px; font-weight: 600; color: var(--text); }
    .avatar { width: 28px; height: 28px; border-radius: 50%; background: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 0.8rem; }
    .article-hero { width: 100%; height: 260px; border-radius: var(--radius); margin-bottom: 32px; display: flex; align-items: center; justify-content: center; }
    .hero-illust { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 14px; }
    .hero-illust-emoji { font-size: 6rem; line-height: 1; filter: drop-shadow(0 4px 24px rgba(0,0,0,0.5)); }
    .hero-illust-cat { color: rgba(255,255,255,0.6); font-size: 0.8rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; }
    .score-box { background: var(--secondary); color: var(--white); border-radius: var(--radius); padding: 28px; margin-bottom: 36px; display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: center; }
    .total-score { text-align: center; }
    .score-number { font-size: 4rem; font-weight: 900; color: var(--accent); line-height: 1; }
    .score-label { font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-top: 4px; }
    .score-breakdown { display: flex; flex-direction: column; gap: 10px; }
    .score-item { display: flex; align-items: center; gap: 10px; font-size: 0.85rem; }
    .score-item-label { min-width: 90px; color: rgba(255,255,255,0.75); }
    .score-bar-wrap { flex: 1; background: rgba(255,255,255,0.1); border-radius: 10px; height: 8px; overflow: hidden; }
    .score-bar { height: 100%; border-radius: 10px; background: var(--accent); }
    .score-item-val { min-width: 32px; text-align: right; font-weight: 700; color: var(--accent); }
    .affiliate-box { background: #fff8f0; border: 2px solid var(--primary); border-radius: var(--radius); padding: 24px; margin: 32px 0; text-align: center; }
    .affiliate-box .prod-name { font-size: 1.1rem; font-weight: 700; margin-bottom: 6px; }
    .affiliate-box .prod-price { font-size: 1.5rem; font-weight: 900; color: var(--primary); margin-bottom: 16px; }
    .affiliate-btns { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
    .btn-amazon { display: inline-flex; align-items: center; gap: 8px; background: #ff9900; color: #111; padding: 12px 28px; border-radius: 50px; font-weight: 800; font-size: 0.9rem; transition: opacity 0.2s, transform 0.2s; }
    .btn-amazon:hover { opacity: 0.85; transform: translateY(-1px); }
    .btn-rakuten { display: inline-flex; align-items: center; gap: 8px; background: #bf0000; color: #fff; padding: 12px 28px; border-radius: 50px; font-weight: 800; font-size: 0.9rem; transition: opacity 0.2s, transform 0.2s; }
    .btn-rakuten:hover { opacity: 0.85; transform: translateY(-1px); }
    .article-body h2 { font-size: 1.3rem; font-weight: 800; margin: 40px 0 14px; padding-left: 14px; border-left: 4px solid var(--primary); }
    .article-body h3 { font-size: 1.05rem; font-weight: 700; margin: 28px 0 10px; }
    .article-body p { font-size: 0.95rem; line-height: 1.85; margin-bottom: 18px; color: #444; }
    .article-body ul { margin: 12px 0 18px 1.5em; font-size: 0.95rem; line-height: 1.8; color: #444; }
    .pros-cons { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 24px 0; }
    .pros, .cons { border-radius: var(--radius); padding: 20px; }
    .pros { background: #f0fff4; border: 1px solid #68d391; }
    .cons { background: #fff5f5; border: 1px solid #fc8181; }
    .pros h4 { color: #276749; font-size: 0.9rem; font-weight: 700; margin-bottom: 10px; }
    .cons h4 { color: #9b2335; font-size: 0.9rem; font-weight: 700; margin-bottom: 10px; }
    .pros li, .cons li { font-size: 0.85rem; line-height: 1.7; list-style: none; padding-left: 0; }
    .pros li::before { content: "✅ "; }
    .cons li::before { content: "❌ "; }
    .spec-table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 0.88rem; }
    .spec-table th, .spec-table td { padding: 12px 16px; text-align: left; border-bottom: 1px solid var(--border); }
    .spec-table th { background: var(--secondary); color: var(--white); font-weight: 700; width: 35%; }
    .spec-table tr:nth-child(even) td { background: #f9f9f9; }
    .info-box { background: #eff6ff; border-left: 4px solid #3b82f6; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; padding: 16px 20px; margin: 24px 0; font-size: 0.88rem; color: #1e40af; line-height: 1.7; }
    .cta-bottom { background: linear-gradient(135deg, var(--secondary), #0f3460); color: var(--white); border-radius: var(--radius); padding: 32px; text-align: center; margin-top: 48px; }
    .cta-bottom h3 { font-size: 1.2rem; font-weight: 800; margin-bottom: 8px; }
    .cta-bottom p { font-size: 0.88rem; color: rgba(255,255,255,0.75); margin-bottom: 20px; }
    .back-to-top { position:fixed; bottom:24px; right:24px; width:44px; height:44px; border-radius:50%; background:var(--primary); color:#fff; border:none; font-size:1.1rem; font-weight:700; cursor:pointer; opacity:0; pointer-events:none; transition:opacity 0.2s, transform 0.2s; z-index:999; box-shadow:0 4px 16px rgba(240,90,40,0.4); }
    .back-to-top.visible { opacity:1; pointer-events:auto; }
    .back-to-top:hover { transform:translateY(-3px); }
    @media (max-width: 768px) {
      .review-page { padding: 24px 16px 60px; }
      .article-header h1 { font-size: 1.3rem; }
      .article-hero { height: 180px; }
      .hero-illust-emoji { font-size: 4rem; }
      .score-box { grid-template-columns: 1fr; gap: 16px; padding: 20px 16px; }
      .score-number { font-size: 3rem; }
      .pros-cons { grid-template-columns: 1fr; }
      .spec-table th { width: 40%; font-size: 0.82rem; }
      .spec-table td { font-size: 0.82rem; }
      .spec-table th, .spec-table td { padding: 10px 12px; }
      .affiliate-box { padding: 18px 14px; }
      .affiliate-btns { flex-direction: column; }
      .btn-amazon, .btn-rakuten { justify-content: center; padding: 13px 20px; }
      .article-body h2 { font-size: 1.1rem; }
      .cta-bottom { padding: 24px 16px; }
    }
"""

def generate_html(p):
    score_stars = "★" * int(p["score"]) + ("☆" if p["score"] % 1 < 0.5 else "★") if p["score"] % 1 != 0 else "★" * int(p["score"])
    score_items_html = "\n".join([
        f'''        <div class="score-item">
          <span class="score-item-label">{label}</span>
          <div class="score-bar-wrap"><div class="score-bar" style="width:{w}%;"></div></div>
          <span class="score-item-val">{val}</span>
        </div>''' for label, w, val in p["scores"]
    ])
    specs_html = "\n".join([f'        <tr><th>{k}</th><td>{v}</td></tr>' for k, v in p["specs"]])
    pros_html = "\n".join([f"            <li>{x}</li>" for x in p["pros"]])
    cons_html = "\n".join([f"            <li>{x}</li>" for x in p["cons"]])
    related_html = "\n".join([
        f'''        <a href="{slug}.html" class="related-card">
          <div class="related-thumb">{emoji}</div>
          <div class="related-cat">{cat}</div>
          <div class="related-title">{title}</div>
          <div class="related-score"><span>★</span> {score} / 5.0</div>
        </a>''' for slug, emoji, cat, title, score in p["related"]
    ])
    bg1, bg2 = p["bg"].split(",")
    cat_slug = CAT_SLUGS.get(p['cat'], "cat-other")
    amazon_url = f"https://www.amazon.co.jp/s?k={quote_plus(p['name'])}"
    rakuten_url = f"https://search.rakuten.co.jp/search/mall/{quote_plus(p['name'])}/"

    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <link rel="sitemap" type="application/xml" href="{BASE_URL}sitemap.xml">
  <title>{p["name"]} レビュー【2026年版】スペック・評判まとめ｜ガジェットナビ</title>
  <meta name="description" content="{p["name"]}のスペック・特徴・評判をまとめました。{p["desc"][:80]}スコア{p["score"]}/5.0。">
  <link rel="canonical" href="{BASE_URL}{p["slug"]}.html">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{p["name"]} レビュー【2026年版】スペック・評判まとめ">
  <meta property="og:description" content="{p["desc"][:100]}">
  <meta property="og:url" content="{BASE_URL}{p["slug"]}.html">
  <meta property="og:site_name" content="ガジェットナビ">
  <meta property="og:image" content="https://auto-affiliate-blog-mauve.vercel.app/ogp-default.svg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://auto-affiliate-blog-mauve.vercel.app/ogp-default.svg">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Review",
    "name": "{p["name"]} レビュー【2026年版】",
    "author": {{ "@type": "Organization", "name": "ガジェットナビ編集部" }},
    "datePublished": "2026-04-05",
    "dateModified": "2026-04-06",
    "description": "{p["desc"]}",
    "reviewRating": {{
      "@type": "Rating",
      "ratingValue": "{p["score"]}",
      "bestRating": "5",
      "worstRating": "1"
    }},
    "itemReviewed": {{
      "@type": "Product",
      "name": "{p["name"]}",
      "image": "{BASE_URL}favicon.svg",
      "offers": {{
        "@type": "Offer",
        "priceCurrency": "JPY",
        "price": "{p["price"].replace('¥', '').replace(',', '')}",
        "availability": "https://schema.org/InStock",
        "url": "{BASE_URL}{p["slug"]}.html"
      }},
      "aggregateRating": {{
        "@type": "AggregateRating",
        "ratingValue": "{p["score"]}",
        "bestRating": "5",
        "worstRating": "1",
        "reviewCount": "1"
      }}
    }},
    "publisher": {{ "@type": "Organization", "name": "ガジェットナビ", "url": "{BASE_URL}" }}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "トップ", "item": "{BASE_URL}" }},
      {{ "@type": "ListItem", "position": 2, "name": "{p["cat"]}", "item": "{BASE_URL}{cat_slug}.html" }},
      {{ "@type": "ListItem", "position": 3, "name": "{p["name"]} レビュー" }}
    ]
  }}
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2054301472533985" crossorigin="anonymous"></script>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-ERDKSGNEWS');
  </script>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800;900&display=swap" rel="stylesheet">
  <style>{REVIEW_STYLE}</style>
</head>
<body>
<header>
  <div class="header-inner">
    <div class="logo">📱 ガジェット<span class="logo-dot">ナビ</span></div>
    <nav>
      <a href="index.html#ranking">ランキング</a>
      <a href="index.html#reviews">レビュー</a>
      <a href="privacy.html">プライバシー</a>
    </nav>
  </div>
</header>

<div style="background:var(--white); padding: 12px 20px; border-bottom:1px solid var(--border);">
  <div class="review-page" style="padding:0;">
    <div class="breadcrumb">
      <a href="index.html">トップ</a><span>›</span>
      <a href="{cat_slug}.html">{p["cat"]}</a><span>›</span>
      {p["name"]} レビュー
    </div>
  </div>
</div>

<div style="background:var(--bg); padding: 20px;">
  <div class="review-page">

    <div class="article-header">
      <div class="article-category">{p["emoji"]} {p["cat"]}</div>
      <h1>【2026年版】{p["name"]} レビュー｜スペック・特徴・評判まとめ</h1>
      <div class="article-meta">
        <div class="author"><div class="avatar">👤</div><span>ガジェットナビ編集部</span></div>
        <span>📅 2026年4月5日</span>
        <span>🕐 読了目安：6分</span>
      </div>
    </div>

    <div class="article-hero" style="background:linear-gradient(135deg,{bg1.strip()},{bg2.strip()});">
      <div class="hero-illust">
        <span class="hero-illust-emoji">{p["emoji"]}</span>
        <span class="hero-illust-cat">{p["cat"]}</span>
      </div>
    </div>

    <div class="score-box">
      <div class="total-score">
        <div class="score-number">{p["score"]}</div>
        <div style="color:var(--accent); font-size:1.5rem;">{'★' * round(p["score"])}</div>
        <div class="score-label">総合スコア（5点満点）</div>
      </div>
      <div class="score-breakdown">
{score_items_html}
      </div>
    </div>

    <div class="affiliate-box">
      <div class="prod-name">{p["emoji"]} {p["name"]}</div>
      <div class="prod-price">{p["price"]}〜</div>
      <div class="affiliate-btns">
        <a href="{amazon_url}" class="btn-amazon" target="_blank" rel="noopener">🛒 Amazonで見る</a>
        <a href="{rakuten_url}" class="btn-rakuten" target="_blank" rel="noopener">🛒 楽天で見る</a>
      </div>
      <p style="font-size:0.75rem; color:#999; margin-top:12px;">※価格は2026年4月時点のものです。最新価格は各サイトでご確認ください。</p>
    </div>

    <div class="article-body">

      <div class="info-box">
        📌 この記事では{p["name"]}のスペック・特徴・ユーザー評判を調査してまとめています。購入前の参考にお役立てください。
      </div>

      <h2>{p["name"]} の特徴・選ぶ理由</h2>
      <p>{p["desc"]}</p>
      <p>スペック・評判を調査した結果、特に{p["pros"][0]}という点が多くのユーザーから評価されています。一方で{p["cons"][0]}という点は購入前に把握しておく必要があります。</p>

      <h2>主なスペック</h2>
      <table class="spec-table">
{specs_html}
      </table>

      <h2>良い点・惜しい点</h2>
      <div class="pros-cons">
        <div class="pros">
          <h4>良い点</h4>
          <ul>
{pros_html}
          </ul>
        </div>
        <div class="cons">
          <h4>惜しい点</h4>
          <ul>
{cons_html}
          </ul>
        </div>
      </div>

      <h2>こんな人におすすめ</h2>
      <p><strong>おすすめな人：</strong>{p["cat"]}に{p["pros"][0]}を求める方、{p["pros"][1]}を重視する方、コスパを重視する方。</p>
      <p><strong>おすすめしない人：</strong>{p["cons"][0]}が気になる方、別の用途が優先される方。</p>

      <h2>総評</h2>
      <p>{p["desc"]}　総合評価は<strong>{p["score"]}点（5点満点）</strong>です。</p>
      <p>特に<strong>{p["pros"][0]}</strong>という点が他の製品と差別化されており、購入を検討する価値が十分あります。</p>

    </div>

    <div class="affiliate-box" style="margin-top:40px;">
      <div class="prod-name">{p["emoji"]} {p["name"]}</div>
      <div class="prod-price">{p["price"]}〜</div>
      <div class="affiliate-btns">
        <a href="{amazon_url}" class="btn-amazon" target="_blank" rel="noopener">🛒 Amazonで購入</a>
        <a href="{rakuten_url}" class="btn-rakuten" target="_blank" rel="noopener">🛒 楽天で購入</a>
      </div>
    </div>

    <div class="cta-bottom">
      <h3>他のおすすめ{p["cat"]}も確認する</h3>
      <p>ランキングでは予算別・用途別のおすすめも紹介しています</p>
      <a href="index.html#reviews" class="btn-affiliate">レビュー一覧を見る →</a>
    </div>

    <div class="related-articles">
      <h3>関連レビュー記事</h3>
      <div class="related-grid">
{related_html}
      </div>
    </div>

  </div>
</div>

<button class="back-to-top" id="backToTop" aria-label="トップへ戻る">↑</button>

<footer>
  <div class="footer-inner">
    <div class="footer-disclaimer">
      ⚠️ 当サイトはアフィリエイトプログラムに参加しています。記事内のリンクから商品を購入した場合、当サイトが報酬を受け取ることがあります。ただし、報酬の有無は評価に一切影響しません。
    </div>
    <div class="footer-bottom">
      <p>© 2026 ガジェットナビ All Rights Reserved.</p>
      <p><a href="privacy.html" style="color:rgba(255,255,255,0.5);">プライバシーポリシー</a></p>
    </div>
  </div>
</footer>
<script>
  // Back to Top
  const btn = document.getElementById('backToTop');
  window.addEventListener('scroll', () => {{ btn.classList.toggle('visible', window.scrollY > 400); }});
  btn.addEventListener('click', () => {{ window.scrollTo({{top:0,behavior:'smooth'}}); }});

  document.querySelectorAll('.affiliate-box').forEach(box => {{
    const link = box.querySelector('.btn-amazon');
    if (link) {{
      box.style.cursor = 'pointer';
      box.addEventListener('click', e => {{
        if (!e.target.closest('a, button')) window.open(link.href, '_blank', 'noopener');
      }});
    }}
  }});
</script>
</body>
</html>'''

CAT_SLUGS = {
    "スマートフォン":     "cat-smartphone",
    "PC周辺機器":         "cat-peripherals",
    "ワイヤレスイヤホン": "cat-earphone",
    "スマートウォッチ":   "cat-smartwatch",
    "ノートPC":           "cat-laptop",
    "カメラ":             "cat-camera",
    "タブレット":         "cat-tablet",
    "ゲーミング":         "cat-gaming",
    "モニター":           "cat-monitor",
    "充電器":             "cat-charger",
    "モバイルバッテリー": "cat-battery",
    "スマートスピーカー": "cat-speaker",
    "スピーカー":         "cat-speaker2",
    "VR/AR":              "cat-vrar",
    "電子書籍リーダー":   "cat-ereader",
    "スマートホーム":     "cat-smarthome",
    "エンタメ":           "cat-entertainment",
    "家電":               "cat-appliance",
    "テレビ":           "cat-tv",
    "ドライヤー":       "cat-dryer",
    "電動歯ブラシ":     "cat-toothbrush",
    "シェーバー":       "cat-shaver",
    "ロボット掃除機":   "cat-robotvacuum",
    "コーヒーメーカー": "cat-coffee",
    "プロジェクター":   "cat-projector",
    "サウンドバー":     "cat-soundbar",
    "ネットワーク機器": "cat-network",
    "ゲーミングチェア": "cat-gamingchair",
    "コードレス掃除機": "cat-cordlessvacuum",
    "調理家電":         "cat-cooking",
}

def generate_category_html(cat_name, products):
    slug = CAT_SLUGS.get(cat_name, "cat-other")
    img_url = CAT_IMAGES.get(cat_name, "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&q=80")
    cards_html = "\n".join([f'''      <a href="{p['slug']}.html" class="cat-card">
        <div class="cat-card-thumb" style="background:linear-gradient(135deg,{p['bg'].split(',')[0].strip()},{p['bg'].split(',')[1].strip()})">
          <img src="{CAT_IMAGES.get(p['cat'], img_url)}" alt="{p['name']}" style="width:100%;height:100%;object-fit:cover;opacity:0.8;" loading="lazy">
        </div>
        <div class="cat-card-body">
          <div class="cat-card-name">{p['name']}</div>
          <div class="cat-card-score">★ {p['score']} / 5.0</div>
          <div class="cat-card-price">{p['price']}〜</div>
          <div class="cat-card-desc">{p['desc'][:60]}…</div>
        </div>
      </a>''' for p in products])
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2054301472533985" crossorigin="anonymous"></script>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-ERDKSGNEWS');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <title>{cat_name}おすすめランキング【2026年版】｜ガジェットナビ</title>
  <meta name="description" content="{cat_name}のおすすめ製品を{len(products)}機種まとめました。スペック・特徴・評判を比較してご紹介します。">
  <link rel="canonical" href="{BASE_URL}{slug}.html">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{cat_name}おすすめランキング【2026年版】｜ガジェットナビ">
  <meta property="og:description" content="{cat_name}のおすすめ{len(products)}機種をまとめました。">
  <meta property="og:url" content="{BASE_URL}{slug}.html">
  <meta property="og:site_name" content="ガジェットナビ">
  <meta property="og:image" content="https://auto-affiliate-blog-mauve.vercel.app/ogp-default.svg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://auto-affiliate-blog-mauve.vercel.app/ogp-default.svg">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "{cat_name}おすすめランキング【2026年版】",
    "description": "{cat_name}のおすすめ製品{len(products)}機種を比較まとめ",
    "numberOfItems": {len(products)},
    "itemListElement": [
{chr(10).join(['      {"@type":"ListItem","position":'+str(i+1)+',"name":"'+p['name']+'","url":"'+BASE_URL+p['slug']+'.html"}' for i,p in enumerate(products[:10])])}
    ]
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type":"ListItem","position":1,"name":"トップ","item":"{BASE_URL}"}},
      {{"@type":"ListItem","position":2,"name":"{cat_name}"}}
    ]
  }}
  </script>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800;900&display=swap" rel="stylesheet">
  <style>
    .cat-page {{ max-width: 1100px; margin: 0 auto; padding: 40px 20px 80px; }}
    .cat-hero {{ background: var(--secondary); color: var(--white); border-radius: var(--radius); padding: 40px 32px; margin-bottom: 40px; position: relative; overflow: hidden; }}
    .cat-hero h1 {{ font-size: clamp(1.5rem, 3vw, 2.2rem); font-weight: 900; margin-bottom: 8px; }}
    .cat-hero p {{ color: rgba(255,255,255,0.7); font-size: 0.95rem; }}
    .cat-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }}
    .cat-card {{ background: var(--white); border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow-sm); transition: transform 0.2s, box-shadow 0.2s; display: flex; flex-direction: column; }}
    .cat-card:hover {{ transform: translateY(-4px); box-shadow: var(--shadow); }}
    .cat-card-thumb {{ height: 180px; overflow: hidden; }}
    .cat-card-body {{ padding: 16px; flex: 1; display: flex; flex-direction: column; gap: 6px; }}
    .cat-card-name {{ font-size: 0.95rem; font-weight: 700; color: var(--text); }}
    .cat-card-score {{ font-size: 0.85rem; color: var(--primary); font-weight: 700; }}
    .cat-card-price {{ font-size: 1rem; font-weight: 900; color: var(--primary); }}
    .cat-card-desc {{ font-size: 0.8rem; color: var(--text-muted); line-height: 1.6; margin-top: auto; }}
    .breadcrumb {{ font-size: 0.8rem; color: var(--text-light); margin-bottom: 20px; display: flex; gap: 8px; flex-wrap: wrap; }}
    .breadcrumb a {{ color: var(--primary); }}
  </style>
</head>
<body>
<header>
  <div class="header-inner">
    <div class="logo"><a href="index.html" style="color:inherit;">📱 ガジェット<span class="logo-dot">ナビ</span></a></div>
    <nav>
      <a href="index.html#ranking">ランキング</a>
      <a href="index.html#reviews">レビュー</a>
      <a href="privacy.html">プライバシー</a>
    </nav>
  </div>
</header>
<div style="background:var(--bg); padding:20px; min-height:80vh;">
  <div class="cat-page">
    <div class="breadcrumb">
      <a href="index.html">トップ</a><span>›</span>
      <span>{cat_name}</span>
    </div>
    <div class="cat-hero">
      <h1>{cat_name} おすすめランキング【2026年版】</h1>
      <p>全{len(products)}機種のスペック・特徴・評判をまとめました</p>
    </div>
    <div class="cat-grid">
{cards_html}
    </div>
  </div>
</div>
<footer>
  <div class="footer-inner">
    <div class="footer-disclaimer">⚠️ 当サイトはアフィリエイトプログラムに参加しています。記事内のリンクから商品を購入した場合、当サイトが報酬を受け取ることがあります。</div>
    <div class="footer-bottom">
      <p>© 2026 ガジェットナビ All Rights Reserved.</p>
      <p><a href="privacy.html" style="color:rgba(255,255,255,0.5);">プライバシーポリシー</a></p>
    </div>
  </div>
</footer>
</body>
</html>'''

# Generate all pages
count = 0
for p in PRODUCTS:
    path = os.path.join(OUTPUT_DIR, f"{p['slug']}.html")
    html = generate_html(p)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1
    print(f"Generated: {p['slug']}.html")

print(f"\nTotal: {count} pages generated")

# Generate category pages
from collections import defaultdict
cat_map = defaultdict(list)
for p in PRODUCTS:
    cat_map[p["cat"]].append(p)

cat_count = 0
for cat_name, prods in cat_map.items():
    slug = CAT_SLUGS.get(cat_name, "cat-other")
    path = os.path.join(OUTPUT_DIR, f"{slug}.html")
    html = generate_category_html(cat_name, prods)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    cat_count += 1
    print(f"Generated: {slug}.html ({len(prods)} products)")

print(f"Category pages: {cat_count}")

# Generate updated sitemap
import datetime
today = datetime.date.today().isoformat()
sitemap_urls = [
    ("", today, "weekly", "1.0"),
    ("privacy.html", "2026-04-01", "yearly", "0.3"),
    ("about.html", "2026-04-07", "yearly", "0.3"),
    ("contact.html", "2026-04-07", "yearly", "0.2"),
    ("sitemap-page.html", today, "weekly", "0.5"),
]
for cat_name in cat_map:
    slug = CAT_SLUGS.get(cat_name, "cat-other")
    sitemap_urls.append((f"{slug}.html", today, "weekly", "0.9"))
for p in PRODUCTS:
    sitemap_urls.append((f"{p['slug']}.html", today, "monthly", "0.8"))

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for path, lastmod, freq, pri in sitemap_urls:
    sitemap += f'''  <url>
    <loc>{BASE_URL}{path}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>
'''
sitemap += '</urlset>'

with open(os.path.join(OUTPUT_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap)
print("sitemap.xml updated")

# Generate HTML sitemap page
cat_sections = ""
for cat_name, prods in sorted(cat_map.items(), key=lambda x: -len(x[1])):
    slug = CAT_SLUGS.get(cat_name, "cat-other")
    links = "\n".join([f'        <li><a href="{p["slug"]}.html">{p["name"]}</a></li>' for p in prods])
    cat_sections += f'''  <div class="sitemap-section">
    <h2><a href="{slug}.html">{cat_name}（{len(prods)}件）</a></h2>
    <ul>
{links}
    </ul>
  </div>
'''

sitemap_page = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2054301472533985" crossorigin="anonymous"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-ERDKSGNEWS');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <title>サイトマップ｜ガジェットナビ</title>
  <meta name="description" content="ガジェットナビの全記事一覧です。カテゴリ別にご覧いただけます。">
  <link rel="canonical" href="{BASE_URL}sitemap-page.html">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800;900&display=swap" rel="stylesheet">
  <style>
    .sitemap-wrap {{ max-width: 900px; margin: 0 auto; padding: 48px 20px 80px; }}
    .sitemap-wrap h1 {{ font-size: 1.8rem; font-weight: 800; margin-bottom: 40px; }}
    .sitemap-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 28px; }}
    .sitemap-section h2 {{ font-size: 1rem; font-weight: 800; color: var(--white); background: var(--secondary); padding: 10px 16px; border-radius: var(--radius-sm) var(--radius-sm) 0 0; margin: 0; }}
    .sitemap-section h2 a {{ color: var(--accent); }}
    .sitemap-section ul {{ list-style: none; background: var(--white); border: 1px solid var(--border); border-top: none; border-radius: 0 0 var(--radius-sm) var(--radius-sm); padding: 12px 16px; margin: 0; }}
    .sitemap-section li {{ border-bottom: 1px solid var(--border); }}
    .sitemap-section li:last-child {{ border-bottom: none; }}
    .sitemap-section li a {{ display: block; padding: 8px 0; font-size: 0.83rem; color: var(--text); transition: color 0.15s; }}
    .sitemap-section li a:hover {{ color: var(--primary); }}
    .sitemap-static {{ background: var(--white); border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 12px 16px; margin-bottom: 32px; }}
    .sitemap-static h2 {{ font-size: 1rem; font-weight: 800; margin-bottom: 10px; }}
    .sitemap-static ul {{ list-style: none; display: flex; gap: 16px; flex-wrap: wrap; }}
    .sitemap-static a {{ font-size: 0.88rem; color: var(--primary); }}
  </style>
</head>
<body>
<header>
  <div class="header-inner">
    <div class="logo"><a href="index.html" style="color:inherit;">📱 ガジェット<span class="logo-dot">ナビ</span></a></div>
    <nav>
      <a href="index.html#ranking">ランキング</a>
      <a href="index.html#reviews">レビュー</a>
      <a href="privacy.html">プライバシー</a>
    </nav>
  </div>
</header>
<div style="background:var(--bg); min-height:80vh;">
  <div class="sitemap-wrap">
    <h1>サイトマップ</h1>
    <div class="sitemap-static">
      <h2>サイト情報</h2>
      <ul>
        <li><a href="index.html">トップページ</a></li>
        <li><a href="about.html">運営者情報</a></li>
        <li><a href="contact.html">お問い合わせ</a></li>
        <li><a href="privacy.html">プライバシーポリシー</a></li>
      </ul>
    </div>
    <div class="sitemap-grid">
{cat_sections}
    </div>
  </div>
</div>
<footer>
  <div class="footer-inner">
    <div class="footer-disclaimer">⚠️ 当サイトはアフィリエイトプログラムに参加しています。</div>
    <div class="footer-bottom">
      <p>© 2026 ガジェットナビ All Rights Reserved.</p>
      <p>
        <a href="privacy.html" style="color:rgba(255,255,255,0.5);">プライバシーポリシー</a> ／
        <a href="about.html" style="color:rgba(255,255,255,0.5);">運営者情報</a> ／
        <a href="contact.html" style="color:rgba(255,255,255,0.5);">お問い合わせ</a>
      </p>
    </div>
  </div>
</footer>
</body>
</html>'''

with open(os.path.join(OUTPUT_DIR, 'sitemap-page.html'), 'w', encoding='utf-8') as f:
    f.write(sitemap_page)
print("sitemap-page.html generated")
