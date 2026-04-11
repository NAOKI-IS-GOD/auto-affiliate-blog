#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from urllib.parse import quote_plus

BASE = r"C:\Users\81804\OneDrive\デスクトップ\auto-affiliate-blog-main"
BASE_URL = "https://auto-affiliate-blog-mauve.vercel.app/"
TODAY = "2026-04-12"

COMPARISONS = [
  {"slug":"compare-iphone16promax-vs-galaxys25ultra","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"iPhone 16 Pro Max","price":"¥194,800","score":4.9,"slug":"review-iphone16promax"},"b":{"name":"Galaxy S25 Ultra","price":"¥189,800","score":4.7,"slug":"review-galaxys25ultra"},"verdict_ja":"カメラで妥協したくないならiPhone 16 Pro Max、AndroidでAI機能を最大限使いたいならGalaxy S25 Ultra","verdict_en":"Choose iPhone 16 Pro Max for best-in-class camera. Go Galaxy S25 Ultra for top Android AI features.","summary_ja":"iPhone 16 Pro MaxはA18 Proチップとカメラで圧倒的優位。Galaxy S25 UltraはSペンとGalaxy AIが強み。","summary_en":"iPhone 16 Pro Max dominates with A18 Pro chip and camera. Galaxy S25 Ultra leads with S Pen and Galaxy AI."},
  {"slug":"compare-iphone16-vs-pixel9a","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"iPhone 16","price":"¥124,800","score":4.4,"slug":"review-iphone16"},"b":{"name":"Pixel 9a","price":"¥79,800","score":4.4,"slug":"review-pixel9a"},"verdict_ja":"iOS・Apple生態系に慣れた人にはiPhone 16、コスパ重視・AI機能を使いたい人にはPixel 9a","verdict_en":"iPhone 16 for Apple ecosystem users; Pixel 9a for better value and Google AI features.","summary_ja":"同スコアで価格差4.5万円。Pixel 9aはAIカメラと長期アップデートで高コスパ。","summary_en":"Same score but ¥45,000 cheaper. Pixel 9a wins on AI camera and long-term software support."},
  {"slug":"compare-iphone16-vs-galaxy-s25","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"iPhone 16","price":"¥124,800","score":4.4,"slug":"review-iphone16"},"b":{"name":"Galaxy S25","price":"¥124,800","score":4.6,"slug":"review-galaxy-s25"},"verdict_ja":"Apple生態系ユーザーにはiPhone 16、AndroidでコンパクトなフラグシップをすすめるならGalaxy S25","verdict_en":"iPhone 16 for Apple ecosystem users; Galaxy S25 for a compact Android flagship with Galaxy AI.","summary_ja":"同価格帯の対決。Galaxy S25はSnapdragon 8 Elite搭載でパフォーマンス上。iPhoneはエコシステムの強さ。","summary_en":"Same price point. Galaxy S25 has performance edge with Snapdragon 8 Elite. iPhone wins on ecosystem."},
  {"slug":"compare-iphonese4-vs-nothingphone3a","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"iPhone SE4","price":"¥74,800","score":4.3,"slug":"review-iphonese4"},"b":{"name":"Nothing Phone 3a","price":"¥49,800","score":4.2,"slug":"review-nothingphone3a"},"verdict_ja":"iOSを使いたい低価格派にはiPhone SE4、ユニークなデザインとコスパを重視するならNothing Phone 3a","verdict_en":"iPhone SE4 for budget iOS users; Nothing Phone 3a for unique design and outstanding value.","summary_ja":"2.5万円の価格差。Nothing Phone 3aはデザイン・コスパで突出。SE4はiOSとApple Intelligenceが強み。","summary_en":"¥25,000 gap. Nothing Phone 3a stands out in design and value. SE4 wins with iOS and Apple Intelligence."},
  {"slug":"compare-iphone16promax-vs-pixel9pro","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"iPhone 16 Pro Max","price":"¥194,800","score":4.9,"slug":"review-iphone16promax"},"b":{"name":"Pixel 9 Pro","price":"¥159,800","score":4.7,"slug":"review-pixel9pro"},"verdict_ja":"最高峰iOSの性能を求めるならiPhone 16 Pro Max、GoogleのAI機能とコスパを重視するならPixel 9 Pro","verdict_en":"iPhone 16 Pro Max for peak iOS performance; Pixel 9 Pro for Google AI and better value.","summary_ja":"3.5万円の価格差。Pixel 9 ProはGoogle AI・カメラで高評価。Pro MaxはA18 Pro・ProResが圧倒的。","summary_en":"¥35,000 difference. Pixel 9 Pro excels in Google AI and camera. Pro Max dominates in chip and ProRes video."},
  {"slug":"compare-galaxys25ultra-vs-xiaomi14ultra","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"Galaxy S25 Ultra","price":"¥189,800","score":4.7,"slug":"review-galaxys25ultra"},"b":{"name":"Xiaomi 14 Ultra","price":"¥159,800","score":4.5,"slug":"review-xiaomi14ultra"},"verdict_ja":"SペンとGalaxy AIを重視するならGalaxy S25 Ultra、Leicaカメラと価格重視ならXiaomi 14 Ultra","verdict_en":"Galaxy S25 Ultra for S Pen and Galaxy AI; Xiaomi 14 Ultra for Leica camera at lower cost.","summary_ja":"3万円差でGalaxy S25 UltraはSペン・AIが優位。Xiaomi 14 UltraはLeicaカメラの写真表現が魅力。","summary_en":"¥30,000 gap. Galaxy S25 Ultra edges ahead with S Pen and AI. Xiaomi 14 Ultra shines with Leica artistry."},
  {"slug":"compare-xperia1vi-vs-galaxy-s25","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"Xperia 1 VI","price":"¥189,700","score":4.4,"slug":"review-xperia1vi"},"b":{"name":"Galaxy S25","price":"¥124,800","score":4.6,"slug":"review-galaxy-s25"},"verdict_ja":"音質・動画撮影品質にこだわるならXperia 1 VI、バランス重視で6万安く済ませるならGalaxy S25","verdict_en":"Xperia 1 VI for audiophiles and video creators; Galaxy S25 for balanced flagship at ¥65,000 less.","summary_ja":"6.5万円の差。XperiaはハイレゾオーディオとZ望遠が独自強み。Galaxy S25は汎用性とコスパ。","summary_en":"¥65,000 difference. Xperia excels in hi-res audio and zoom. Galaxy S25 wins on versatility and value."},
  {"slug":"compare-oneplus13-vs-xiaomi15","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"OnePlus 13","price":"¥109,800","score":4.4,"slug":"review-oneplus13"},"b":{"name":"Xiaomi 15","price":"¥129,800","score":4.7,"slug":"review-xiaomi15"},"verdict_ja":"充電速度と価格重視ならOnePlus 13、Leicaカメラと総合性能ならXiaomi 15","verdict_en":"OnePlus 13 for fast charging and value; Xiaomi 15 for Leica camera and all-round flagship performance.","summary_ja":"2万円差でXiaomi 15がスコア上。LeicaカメラとSnapdragon 8 Eliteが強力。OnePlus 13は100W充電が魅力。","summary_en":"¥20,000 gap. Xiaomi 15 scores higher with Leica and Snapdragon 8 Elite. OnePlus 13 impresses with 100W charging."},
  {"slug":"compare-pixel9a-vs-iphonese4","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"Pixel 9a","price":"¥79,800","score":4.4,"slug":"review-pixel9a"},"b":{"name":"iPhone SE4","price":"¥74,800","score":4.3,"slug":"review-iphonese4"},"verdict_ja":"Google AIと高度なカメラ機能を求めるならPixel 9a、iOSとコンパクトなボディを優先するならiPhone SE4","verdict_en":"Pixel 9a for Google AI and advanced camera; iPhone SE4 for iOS and compact form factor.","summary_ja":"5千円差の対決。Pixel 9aはAI機能とカメラが充実。SE4はiOSとApple Intelligenceが強み。","summary_en":"¥5,000 apart. Pixel 9a leads on AI and camera. SE4 wins with iOS and Apple Intelligence."},
  {"slug":"compare-iphone16plus-vs-galaxys25plus","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"iPhone 16 Plus","price":"¥149,800","score":4.5,"slug":"review-iphone16plus"},"b":{"name":"Galaxy S25+","price":"¥159,800","score":4.6,"slug":"review-galaxys25plus"},"verdict_ja":"大画面iPhoneを求めるならiPhone 16 Plus、Android大画面フラグシップならGalaxy S25+","verdict_en":"iPhone 16 Plus for large-screen iPhone experience; Galaxy S25+ for premium large Android flagship.","summary_ja":"1万円差。Galaxy S25+はSnapdragon 8 Elite搭載で性能優位。iPhone 16 Plusはバッテリー持ちが抜群。","summary_en":"¥10,000 apart. Galaxy S25+ has performance edge with Snapdragon 8 Elite. iPhone 16 Plus wins on battery life."},
  {"slug":"compare-oppofindx8pro-vs-xiaomi14ultra","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"OPPO Find X8 Pro","price":"¥119,800","score":4.3,"slug":"review-oppofindx8pro"},"b":{"name":"Xiaomi 14 Ultra","price":"¥159,800","score":4.5,"slug":"review-xiaomi14ultra"},"verdict_ja":"バランス重視でコスパ良くをすすめるならOPPO Find X8 Pro、カメラ性能で妥協しないならXiaomi 14 Ultra","verdict_en":"OPPO Find X8 Pro for balanced performance and value; Xiaomi 14 Ultra for uncompromising camera.","summary_ja":"4万円差。Xiaomi 14 UltraはLeicaカメラで圧倒。OPPO Find X8 ProはHasselblad共同開発で健闘。","summary_en":"¥40,000 gap. Xiaomi 14 Ultra dominates with Leica. OPPO Find X8 Pro punches back with Hasselblad."},
  {"slug":"compare-galaxya55-vs-nothingphone3a","cat":"スマートフォン","cat_en":"Smartphone","emoji":"📱","bg":"#1a1a2e,#16213e","a":{"name":"Galaxy A55","price":"¥59,800","score":4.1,"slug":"review-galaxya55"},"b":{"name":"Nothing Phone 3a","price":"¥49,800","score":4.2,"slug":"review-nothingphone3a"},"verdict_ja":"Samsungブランドの信頼性を求めるならGalaxy A55、独自デザインとコスパならNothing Phone 3a","verdict_en":"Galaxy A55 for Samsung brand reliability; Nothing Phone 3a for unique design and better value.","summary_ja":"1万円差でNothing Phone 3aがスコア上。グライフライトシステムの個性が光る。A55はサポートが充実。","summary_en":"¥10,000 gap, Nothing Phone 3a scores higher. Glyph interface stands out. Galaxy A55 has better long-term support."},
  {"slug":"compare-sonywf1000xm5-vs-boseqcearbuds2","cat":"イヤホン","cat_en":"Earphones","emoji":"🎧","bg":"#1a1a2e,#0f3460","a":{"name":"Sony WF-1000XM5","price":"¥39,600","score":4.7,"slug":"review-sonywf1000xm5"},"b":{"name":"Bose QC Earbuds II","price":"¥38,500","score":4.6,"slug":"review-boseqcearbuds2"},"verdict_ja":"音質とNC両立ならSony WF-1000XM5、快適装着感でNCを最優先するならBose QC Earbuds II","verdict_en":"Sony WF-1000XM5 for best sound quality and ANC; Bose QC Earbuds II for superior comfort and powerful ANC.","summary_ja":"ハイエンドの頂上対決。SonyはQN2eチップとLDACで音質◎。Boseは装着感と低音NCが圧倒的。","summary_en":"Top-tier showdown. Sony excels with QN2e chip and LDAC. Bose dominates in comfort and low-frequency ANC."},
  {"slug":"compare-sonywf1000xm5-vs-technicseahaz80","cat":"イヤホン","cat_en":"Earphones","emoji":"🎧","bg":"#1a1a2e,#0f3460","a":{"name":"Sony WF-1000XM5","price":"¥39,600","score":4.7,"slug":"review-sonywf1000xm5"},"b":{"name":"Technics EAH-AZ80","price":"¥44,000","score":4.6,"slug":"review-technicseahaz80"},"verdict_ja":"NC性能重視ならSony WF-1000XM5、3台マルチポイントと高音質を求めるならTechnics EAH-AZ80","verdict_en":"Sony WF-1000XM5 for ANC performance; Technics EAH-AZ80 for 3-device multipoint and audiophile sound.","summary_ja":"4400円差でTechnicsが高価格。3台同時接続と自然な音質はTechnics独自強み。SonyはNCとコスパ。","summary_en":"¥4,400 more for Technics. 3-device multipoint and natural sound are Technics strengths. Sony wins on ANC."},
  {"slug":"compare-galaxybuds3pro-vs-sonywf1000xm5","cat":"イヤホン","cat_en":"Earphones","emoji":"🎧","bg":"#1a1a2e,#0f3460","a":{"name":"Galaxy Buds 3 Pro","price":"¥29,800","score":4.5,"slug":"review-galaxybuds3pro"},"b":{"name":"Sony WF-1000XM5","price":"¥39,600","score":4.7,"slug":"review-sonywf1000xm5"},"verdict_ja":"Galaxyスマホユーザーならシームレス連携のGalaxy Buds 3 Pro、音質NCを最優先ならSony WF-1000XM5","verdict_en":"Galaxy Buds 3 Pro for seamless Galaxy ecosystem integration; Sony WF-1000XM5 for best ANC and sound.","summary_ja":"1万円の差。Galaxy Buds 3 ProはGalaxy端末との連携が強力。SonyはNC・音質で上回る。","summary_en":"¥10,000 gap. Galaxy Buds 3 Pro shines with Galaxy integration. Sony leads in ANC and audio quality."},
  {"slug":"compare-jbltourpro3-vs-sonywf1000xm5","cat":"イヤホン","cat_en":"Earphones","emoji":"🎧","bg":"#1a1a2e,#0f3460","a":{"name":"JBL Tour Pro 3","price":"¥34,800","score":4.4,"slug":"review-jbltourpro3"},"b":{"name":"Sony WF-1000XM5","price":"¥39,600","score":4.7,"slug":"review-sonywf1000xm5"},"verdict_ja":"スマートケースの利便性と価格を重視するならJBL Tour Pro 3、音質とNCの頂点ならSony WF-1000XM5","verdict_en":"JBL Tour Pro 3 for smart case convenience and lower price; Sony WF-1000XM5 for top-tier audio and ANC.","summary_ja":"4800円差。JBL Tour Pro 3はタッチ操作できるスマートケースがユニーク。Sonyは性能面で勝る。","summary_en":"¥4,800 difference. JBL Tour Pro 3 stands out with touchscreen smart case. Sony outperforms in ANC."},
  {"slug":"compare-nothingear2-vs-ankerliberty4nc","cat":"イヤホン","cat_en":"Earphones","emoji":"🎧","bg":"#1a1a2e,#0f3460","a":{"name":"Nothing Ear 2","price":"¥18,800","score":4.3,"slug":"review-nothingear2"},"b":{"name":"Anker Liberty 4 NC","price":"¥9,990","score":4.3,"slug":"review-ankerliberty4nc"},"verdict_ja":"デザインと音質バランスを求めるならNothing Ear 2、コスパ最優先ならAnker Liberty 4 NC","verdict_en":"Nothing Ear 2 for distinctive design and audio balance; Anker Liberty 4 NC for unbeatable value.","summary_ja":"同スコアで価格差8800円。Anker Liberty 4 NCは1万円以下でNCありの驚異的コスパ。","summary_en":"Same score, ¥8,800 apart. Anker Liberty 4 NC delivers incredible ANC value under ¥10,000."},
  {"slug":"compare-sennheisermomentum4-vs-boseqcearbuds2","cat":"イヤホン","cat_en":"Earphones","emoji":"🎧","bg":"#1a1a2e,#0f3460","a":{"name":"Sennheiser MOMENTUM TW4","price":"¥44,000","score":4.5,"slug":"review-sennheisermomentum4"},"b":{"name":"Bose QC Earbuds II","price":"¥38,500","score":4.6,"slug":"review-boseqcearbuds2"},"verdict_ja":"Sennheiserの音質にこだわるならMOMENTUM TW4、NC快適性を最優先するならBose QC Earbuds II","verdict_en":"Sennheiser MOMENTUM TW4 for audiophile-grade sound; Bose QC Earbuds II for top ANC comfort.","summary_ja":"5500円差でSennheiserが高価格。音質はSennheiser、NC快適性と装着感はBoseが上。","summary_en":"¥5,500 gap, Sennheiser costs more. Sennheiser leads in sound; Bose wins in ANC comfort and fit."},
  {"slug":"compare-sonywh1000xm5-vs-boseqc45","cat":"イヤホン","cat_en":"Earphones","emoji":"🎧","bg":"#1a1a2e,#0f3460","a":{"name":"Sony WH-1000XM5","price":"¥49,500","score":4.8,"slug":"review-sonywh1000xm5"},"b":{"name":"Bose QC45","price":"¥44,000","score":4.6,"slug":"review-boseqc45"},"verdict_ja":"最高峰の音質とNCを求めるならSony WH-1000XM5、軽量で快適な長時間リスニングならBose QC45","verdict_en":"Sony WH-1000XM5 for best-in-class audio and ANC; Bose QC45 for lightweight comfort in long sessions.","summary_ja":"5500円差でSonyが高価格だがスコア差も大きい。Sony WH-1000XM5はオーバーイヤー最高峰。","summary_en":"¥5,500 more for Sony but the score gap is clear. Sony WH-1000XM5 is the benchmark over-ear headphone."},
  {"slug":"compare-technicseahaz80-vs-boseqcearbuds2","cat":"イヤホン","cat_en":"Earphones","emoji":"🎧","bg":"#1a1a2e,#0f3460","a":{"name":"Technics EAH-AZ80","price":"¥44,000","score":4.6,"slug":"review-technicseahaz80"},"b":{"name":"Bose QC Earbuds II","price":"¥38,500","score":4.6,"slug":"review-boseqcearbuds2"},"verdict_ja":"3台マルチポイントと高音質を求めるならTechnics EAH-AZ80、快適なNC装着感を最優先ならBose QC Earbuds II","verdict_en":"Technics EAH-AZ80 for 3-device multipoint and audiophile sound; Bose QC Earbuds II for ANC comfort.","summary_ja":"同スコアで5500円差。Technicsは音質・マルチポイント、BoseはNC快適性で方向性が異なる。","summary_en":"Same score, ¥5,500 apart. Technics for audio and multipoint; Bose for ANC comfort."},
  {"slug":"compare-applewatchs10-vs-galaxywatch7","cat":"スマートウォッチ","cat_en":"Smartwatch","emoji":"⌚","bg":"#0d1b2a,#1b4332","a":{"name":"Apple Watch S10","price":"¥59,800","score":4.8,"slug":"review-applewatchs10"},"b":{"name":"Galaxy Watch 7","price":"¥44,800","score":4.6,"slug":"review-galaxywatch7"},"verdict_ja":"iPhoneユーザーならApple Watch S10一択、Android/GalaxyユーザーにはGalaxy Watch 7","verdict_en":"Apple Watch S10 is the clear choice for iPhone users; Galaxy Watch 7 is top pick for Android/Galaxy users.","summary_ja":"1.5万円差。Apple Watch S10はwatchOS×iPhone連携が圧倒的。Galaxy Watch 7はAndroidで最高。","summary_en":"¥15,000 gap. Apple Watch S10 dominates with watchOS-iPhone integration. Galaxy Watch 7 is best for Android."},
  {"slug":"compare-applewatchultra2-vs-garminfenix8","cat":"スマートウォッチ","cat_en":"Smartwatch","emoji":"⌚","bg":"#0d1b2a,#1b4332","a":{"name":"Apple Watch Ultra 2","price":"¥139,800","score":4.9,"slug":"review-applewatchultra2"},"b":{"name":"Garmin Fenix 8","price":"¥139,800","score":4.7,"slug":"review-garminfenix8"},"verdict_ja":"iPhoneと連携したアウトドア・ウォッチならApple Watch Ultra 2、本格アウトドア・長バッテリーならGarmin Fenix 8","verdict_en":"Apple Watch Ultra 2 for outdoor with iPhone integration; Garmin Fenix 8 for serious sports and longer battery.","summary_ja":"同価格の二大アウトドアウォッチ対決。Ultra 2はiPhone連携、Fenix 8はスポーツ機能とバッテリー。","summary_en":"Same price, two outdoor titans. Ultra 2 excels in iPhone ecosystem; Fenix 8 wins on sports and battery endurance."},
  {"slug":"compare-pixelwatch3-vs-galaxywatch7","cat":"スマートウォッチ","cat_en":"Smartwatch","emoji":"⌚","bg":"#0d1b2a,#1b4332","a":{"name":"Pixel Watch 3","price":"¥59,800","score":4.5,"slug":"review-pixelwatch3"},"b":{"name":"Galaxy Watch 7","price":"¥44,800","score":4.6,"slug":"review-galaxywatch7"},"verdict_ja":"Pixelスマホユーザーならシームレス連携のPixel Watch 3、GalaxyユーザーならGalaxy Watch 7","verdict_en":"Pixel Watch 3 for seamless Pixel phone integration; Galaxy Watch 7 for Galaxy users and best Android value.","summary_ja":"1.5万円差でGalaxy Watch 7がスコア上。Galaxy AI連携とコスパが強み。Pixel Watch 3はFitbit連携。","summary_en":"¥15,000 more for Pixel Watch 3, yet Galaxy Watch 7 scores higher. Galaxy AI and value are key."},
  {"slug":"compare-garminfenix8-vs-garminvenu3","cat":"スマートウォッチ","cat_en":"Smartwatch","emoji":"⌚","bg":"#0d1b2a,#1b4332","a":{"name":"Garmin Fenix 8","price":"¥139,800","score":4.7,"slug":"review-garminfenix8"},"b":{"name":"Garmin Venu 3","price":"¥69,800","score":4.5,"slug":"review-garminvenu3"},"verdict_ja":"本格アウトドアスポーツ志向にはGarmin Fenix 8、普段使いでスタイリッシュに健康管理するならGarmin Venu 3","verdict_en":"Garmin Fenix 8 for serious outdoor athletes; Garmin Venu 3 for stylish everyday health tracking.","summary_ja":"7万円差。Fenix 8は登山・マラソン・トライアスロン向け。Venu 3は日常ウェルネス管理に特化。","summary_en":"¥70,000 difference. Fenix 8 built for hiking, marathons, triathlons. Venu 3 focuses on daily wellness."},
  {"slug":"compare-applewatchs10-vs-applewatchultra2","cat":"スマートウォッチ","cat_en":"Smartwatch","emoji":"⌚","bg":"#0d1b2a,#1b4332","a":{"name":"Apple Watch S10","price":"¥59,800","score":4.8,"slug":"review-applewatchs10"},"b":{"name":"Apple Watch Ultra 2","price":"¥139,800","score":4.9,"slug":"review-applewatchultra2"},"verdict_ja":"普段使いにはApple Watch S10で十分、アウトドアやプロスポーツ用途ならApple Watch Ultra 2","verdict_en":"Apple Watch S10 is perfect for everyday use; Apple Watch Ultra 2 is built for outdoor adventures and pro sports.","summary_ja":"8万円差。日常利用ならS10で満足できる。Ultra 2はチタン・2000nit・水深100mでアウトドア特化。","summary_en":"¥80,000 gap. S10 satisfies daily use. Ultra 2 adds titanium build, 2000 nits, 100m water depth for outdoor."},
  {"slug":"compare-ipadprom4-vs-galaxytabs10ultra","cat":"タブレット","cat_en":"Tablet","emoji":"📟","bg":"#1a1a2e,#2d3748","a":{"name":"iPad Pro M4","price":"¥218,800","score":4.9,"slug":"review-ipadprom4"},"b":{"name":"Galaxy Tab S10 Ultra","price":"¥189,800","score":4.6,"slug":"review-galaxytabs10ultra"},"verdict_ja":"Apple生態系でクリエイティブ作業をするならiPad Pro M4、AndroidのDeXマルチタスクならGalaxy Tab S10 Ultra","verdict_en":"iPad Pro M4 for Apple creative workflows; Galaxy Tab S10 Ultra for Android multitasking with DeX.","summary_ja":"3万円差でiPad Pro M4がスコアで大幅上回る。M4チップはPC級。Galaxy Tab S10 UltraはDeX連携が強み。","summary_en":"¥30,000 gap, iPad Pro M4 scores much higher. M4 chip is PC-class. Galaxy Tab S10 Ultra shines with DeX."},
  {"slug":"compare-ipadairm2-vs-ipadprom4","cat":"タブレット","cat_en":"Tablet","emoji":"📟","bg":"#1a1a2e,#2d3748","a":{"name":"iPad Air M2","price":"¥98,800","score":4.5,"slug":"review-ipadairm2"},"b":{"name":"iPad Pro M4","price":"¥218,800","score":4.9,"slug":"review-ipadprom4"},"verdict_ja":"コスパ重視の普段使い・学生にはiPad Air M2、プロ級の性能とOLED画面ならiPad Pro M4","verdict_en":"iPad Air M2 for everyday use and students; iPad Pro M4 for professional-grade performance and OLED.","summary_ja":"12万円差。iPad Air M2は普段使いに十分。Pro M4はOLED・M4チップ・Thunderbolt 4で別次元。","summary_en":"¥120,000 difference. iPad Air M2 handles everyday tasks fine. Pro M4 is on another level with OLED and M4."},
  {"slug":"compare-ipadmini7-vs-kindlepaperwhite","cat":"タブレット","cat_en":"Tablet","emoji":"📟","bg":"#1a1a2e,#2d3748","a":{"name":"iPad mini 7","price":"¥78,800","score":4.4,"slug":"review-ipadmini7"},"b":{"name":"Kindle Paperwhite","price":"¥21,980","score":4.6,"slug":"review-kindlepaperwhite"},"verdict_ja":"電子書籍以外も使う多目的デバイスにはiPad mini 7、読書専用で目に優しい端末ならKindle Paperwhite","verdict_en":"iPad mini 7 for a versatile portable device; Kindle Paperwhite for eye-friendly dedicated reading.","summary_ja":"5.7万円差。Kindleは読書に特化した最高の端末。iPad mini 7はゲーム・動画・読書を1台で。","summary_en":"¥57,000 difference. Kindle is the ultimate reading device. iPad mini 7 handles gaming, video, and reading."},
  {"slug":"compare-surfacepro11-vs-ipadprom4","cat":"タブレット","cat_en":"Tablet","emoji":"📟","bg":"#1a1a2e,#2d3748","a":{"name":"Surface Pro 11","price":"¥228,800","score":4.5,"slug":"review-surfacepro11"},"b":{"name":"iPad Pro M4","price":"¥218,800","score":4.9,"slug":"review-ipadprom4"},"verdict_ja":"Windowsが必要なビジネスユーザーにはSurface Pro 11、Apple生態系でクリエイティブ作業ならiPad Pro M4","verdict_en":"Surface Pro 11 for business users who need Windows; iPad Pro M4 for creative professionals in Apple ecosystem.","summary_ja":"1万円差でiPad Pro M4がスコアで大差。ただしWindowsの互換性が必要ならSurface一択。","summary_en":"¥10,000 apart but iPad Pro M4 scores much higher. If Windows compatibility is essential, Surface is the choice."},
  {"slug":"compare-macbookairm3-vs-macbookprom4pro","cat":"ノートPC","cat_en":"Laptop","emoji":"💻","bg":"#1a1a2e,#2c3e50","a":{"name":"MacBook Air M3","price":"¥198,800","score":4.8,"slug":"review-macbookairm3"},"b":{"name":"MacBook Pro M4 Pro","price":"¥298,800","score":4.9,"slug":"review-macbookprom4pro"},"verdict_ja":"普段使いに軽く持ち運ぶにはMacBook Air M3で十分、本格的なプロ作業にはMacBook Pro M4 Pro","verdict_en":"MacBook Air M3 is perfect for everyday use and portability; MacBook Pro M4 Pro for serious professional workloads.","summary_ja":"10万円差。Air M3は薄型軽量・無ファンで日常最強。Pro M4 ProはM4 Pro・Liquid Retina XDRでプロ向け。","summary_en":"¥100,000 gap. Air M3 is slim, fanless, perfect daily use. Pro M4 Pro adds M4 Pro chip and Liquid Retina XDR."},
  {"slug":"compare-macbookairm3-vs-dellxps15","cat":"ノートPC","cat_en":"Laptop","emoji":"💻","bg":"#1a1a2e,#2c3e50","a":{"name":"MacBook Air M3","price":"¥198,800","score":4.8,"slug":"review-macbookairm3"},"b":{"name":"Dell XPS 15","price":"¥289,800","score":4.6,"slug":"review-dellxps15"},"verdict_ja":"macOSと長時間バッテリーを重視するならMacBook Air M3、WindowsとOLEDならDell XPS 15","verdict_en":"MacBook Air M3 for macOS and all-day battery; Dell XPS 15 for Windows with stunning OLED display.","summary_ja":"9万円差でMacBook Air M3がスコア上。M3チップは省電力性能が圧倒的。XPS 15はOLEDが魅力。","summary_en":"¥90,000 apart, MacBook Air M3 scores higher. M3 chip delivers unmatched power efficiency. XPS 15 has OLED."},
  {"slug":"compare-macbookairm3-vs-surfacepro11","cat":"ノートPC","cat_en":"Laptop","emoji":"💻","bg":"#1a1a2e,#2c3e50","a":{"name":"MacBook Air M3","price":"¥198,800","score":4.8,"slug":"review-macbookairm3"},"b":{"name":"Surface Pro 11","price":"¥228,800","score":4.5,"slug":"review-surfacepro11"},"verdict_ja":"軽量ノートPCならMacBook Air M3、タブレット兼用の2-in-1ならSurface Pro 11","verdict_en":"MacBook Air M3 for a lightweight laptop; Surface Pro 11 for a versatile 2-in-1 tablet/laptop combo.","summary_ja":"3万円差でMacBook Air M3がスコア上。Air M3は無ファン・18時間バッテリーが圧倒的。Surface Pro 11はタブレット兼用。","summary_en":"¥30,000 apart, MacBook Air M3 scores higher. Fanless and 18-hour battery are unbeatable. Surface doubles as tablet."},
  {"slug":"compare-asusrogzephyrusg14-vs-razerblade15","cat":"ノートPC","cat_en":"Laptop","emoji":"💻","bg":"#1a1a2e,#2c3e50","a":{"name":"ROG Zephyrus G14","price":"¥249,800","score":4.5,"slug":"review-asusrogzephyrusg14"},"b":{"name":"Razer Blade 15","price":"¥339,800","score":4.5,"slug":"review-razerblade15"},"verdict_ja":"コスパ重視のゲーミングノートにはROG Zephyrus G14、プレミアムな薄型ゲーミングにはRazer Blade 15","verdict_en":"ROG Zephyrus G14 for gaming performance at great value; Razer Blade 15 for premium slim gaming aesthetics.","summary_ja":"9万円差で同スコア。ROG G14はAMD APUでコスパ抜群。Razer Blade 15はアルミ筐体の高級感が圧倒的。","summary_en":"¥90,000 gap, same score. ROG G14 offers exceptional AMD APU value. Razer Blade 15 delivers premium aluminum build."},
  {"slug":"compare-thinkpadx1carbon-vs-dellxps15","cat":"ノートPC","cat_en":"Laptop","emoji":"💻","bg":"#1a1a2e,#2c3e50","a":{"name":"ThinkPad X1 Carbon","price":"¥289,800","score":4.7,"slug":"review-thinkpadx1carbon"},"b":{"name":"Dell XPS 15","price":"¥289,800","score":4.6,"slug":"review-dellxps15"},"verdict_ja":"ビジネス用途・軽量性を重視するならThinkPad X1 Carbon、OLEDとクリエイティブ作業ならDell XPS 15","verdict_en":"ThinkPad X1 Carbon for business mobility and legendary keyboard; Dell XPS 15 for OLED and creative work.","summary_ja":"同価格でThinkPadがスコア上。X1 CarbonはCarbon繊維で1.12kg・最軽量ビジネスノート。XPS 15はOLEDが魅力。","summary_en":"Same price, ThinkPad scores higher. X1 Carbon uses carbon fiber at 1.12kg. XPS 15 impresses with OLED."},
  {"slug":"compare-nintendoswitch2-vs-ps5slim","cat":"ゲーム機","cat_en":"Gaming","emoji":"🎮","bg":"#0d0d1a,#1a0033","a":{"name":"Nintendo Switch 2","price":"¥49,980","score":4.8,"slug":"review-nintendoswitch2"},"b":{"name":"PS5 Slim","price":"¥74,980","score":4.7,"slug":"review-ps5slim"},"verdict_ja":"携帯・リビング両用でNintendo独占タイトルを楽しむならSwitch 2、4K画質とPS独占タイトルならPS5 Slim","verdict_en":"Nintendo Switch 2 for portable/home hybrid and Nintendo exclusives; PS5 Slim for 4K gaming and PS exclusives.","summary_ja":"2.5万円差でSwitch 2が低価格。携帯と据置の両用でSwitch 2は最高。PS5 SlimはDualSenseが革命的。","summary_en":"¥25,000 gap. Switch 2 is better value. Hybrid portability is its edge. PS5 Slim DualSense haptics are revolutionary."},
  {"slug":"compare-ps5slim-vs-xboxseriesx","cat":"ゲーム機","cat_en":"Gaming","emoji":"🎮","bg":"#0d0d1a,#1a0033","a":{"name":"PS5 Slim","price":"¥74,980","score":4.7,"slug":"review-ps5slim"},"b":{"name":"Xbox Series X","price":"¥69,978","score":4.6,"slug":"review-xboxseriesx"},"verdict_ja":"PS独占タイトルとDualSenseの体験を重視するならPS5 Slim、Game Passと後方互換性ならXbox Series X","verdict_en":"PS5 Slim for PlayStation exclusives and DualSense experience; Xbox Series X for Game Pass and backward compatibility.","summary_ja":"5千円差。PS5 SlimはGod of War・Spider-Manなど独占タイトル。Xbox Series XはGame Passが圧倒的。","summary_en":"¥5,000 difference. PS5 Slim has God of War, Spider-Man exclusives. Xbox Series X Game Pass is unmatched value."},
  {"slug":"compare-nintendoswitch2-vs-xboxseriesx","cat":"ゲーム機","cat_en":"Gaming","emoji":"🎮","bg":"#0d0d1a,#1a0033","a":{"name":"Nintendo Switch 2","price":"¥49,980","score":4.8,"slug":"review-nintendoswitch2"},"b":{"name":"Xbox Series X","price":"¥69,978","score":4.6,"slug":"review-xboxseriesx"},"verdict_ja":"携帯ゲームと任天堂タイトルを楽しむならSwitch 2、4KグラフィックとGame Passを楽しむならXbox Series X","verdict_en":"Nintendo Switch 2 for portable gaming and Nintendo titles; Xbox Series X for 4K graphics and Game Pass library.","summary_ja":"2万円差でSwitch 2が低価格かつスコア上。携帯・据置の柔軟性が優位。Xbox Series XはGame Pass。","summary_en":"¥20,000 less and higher score for Switch 2. Hybrid portability is the edge. Xbox Series X wins with Game Pass."},
  {"slug":"compare-lg27gp850b-vs-asusrogswiftpg279qm","cat":"モニター","cat_en":"Monitor","emoji":"🖥️","bg":"#0d1b2a,#16213e","a":{"name":"LG 27GP850B","price":"¥44,800","score":4.6,"slug":"review-lg27gp850b"},"b":{"name":"ASUS ROG Swift PG279QM","price":"¥89,800","score":4.7,"slug":"review-asusrogswiftpg279qm"},"verdict_ja":"コスパ重視のゲーミングモニターにはLG 27GP850B、最高のゲーミング性能を求めるならASUS ROG Swift PG279QM","verdict_en":"LG 27GP850B for the best gaming monitor value; ASUS ROG Swift PG279QM for top gaming performance.","summary_ja":"4.5万円差。ROG Swift PG279QMは240Hz・G-Sync・1msで頂点。LG 27GP850Bは165Hzで十分コスパ。","summary_en":"¥45,000 gap. ROG Swift PG279QM peaks at 240Hz, G-Sync, 1ms. LG 27GP850B at 165Hz offers excellent value."},
  {"slug":"compare-dellu2723d-vs-benqpd3205u","cat":"モニター","cat_en":"Monitor","emoji":"🖥️","bg":"#0d1b2a,#16213e","a":{"name":"Dell U2723D","price":"¥89,800","score":4.7,"slug":"review-dellu2723d"},"b":{"name":"BenQ PD3205U","price":"¥79,800","score":4.6,"slug":"review-benqpd3205u"},"verdict_ja":"USB-Cハブ機能と色精度を重視するならDell U2723D、高解像度4Kとクリエイティブ作業ならBenQ PD3205U","verdict_en":"Dell U2723D for USB-C hub and color accuracy; BenQ PD3205U for 4K resolution and creative workflows.","summary_ja":"1万円差でDellがスコア上。U2723DはIPS Black・USB-Cハブが強み。BenQ PD3205Uは大型4K・32インチ。","summary_en":"¥10,000 gap, Dell scores higher. U2723D wins with IPS Black and USB-C hub. BenQ PD3205U offers large 4K 32-inch."},
  {"slug":"compare-samsungodysseyg7-vs-lg27gp850b","cat":"モニター","cat_en":"Monitor","emoji":"🖥️","bg":"#0d1b2a,#16213e","a":{"name":"Samsung Odyssey G7","price":"¥59,800","score":4.6,"slug":"review-samsungodysseyg7"},"b":{"name":"LG 27GP850B","price":"¥44,800","score":4.6,"slug":"review-lg27gp850b"},"verdict_ja":"曲面モニターとVAコントラストを求めるならSamsung Odyssey G7、フラットNano IPSのコスパならLG 27GP850B","verdict_en":"Samsung Odyssey G7 for curved display and VA contrast; LG 27GP850B for flat Nano IPS value.","summary_ja":"同スコアで1.5万円差。Odyssey G7は1000R曲面・VAのコントラストが魅力。LG 27GP850BはNano IPSの色域。","summary_en":"Same score, ¥15,000 apart. Odyssey G7 offers 1000R curve and VA contrast. LG 27GP850B wins with Nano IPS color."},
  {"slug":"compare-lg45gr95qeb-vs-samsungodysseyg7","cat":"モニター","cat_en":"Monitor","emoji":"🖥️","bg":"#0d1b2a,#16213e","a":{"name":"LG 45GR95QEB","price":"¥149,800","score":4.5,"slug":"review-lg45gr95qeb"},"b":{"name":"Samsung Odyssey G7","price":"¥59,800","score":4.6,"slug":"review-samsungodysseyg7"},"verdict_ja":"ウルトラワイドの没入ゲーミングを求めるならLG 45GR95QEB、コスパと実用性を重視するならSamsung Odyssey G7","verdict_en":"LG 45GR95QEB for ultra-wide immersive gaming; Samsung Odyssey G7 for practical gaming value.","summary_ja":"9万円差でOdyssey G7がスコア上。LG 45GR95QEBはOLED・45インチUWQHDの没入感が別次元。","summary_en":"¥90,000 difference, Odyssey G7 scores higher. LG 45GR95QEB offers next-level OLED 45-inch UWQHD immersion."},
  {"slug":"compare-goprohero12-vs-djiosmoaction4","cat":"カメラ","cat_en":"Camera","emoji":"📷","bg":"#1a0a00,#2d1a00","a":{"name":"GoPro HERO12","price":"¥54,800","score":4.5,"slug":"review-goprohero12"},"b":{"name":"DJI Osmo Action 4","price":"¥49,800","score":4.6,"slug":"review-djiosmoaction4"},"verdict_ja":"GoPro生態系とアクセサリー豊富さを求めるならHERO12、長時間録画と色再現性ならDJI Osmo Action 4","verdict_en":"GoPro HERO12 for extensive accessory ecosystem; DJI Osmo Action 4 for longer recording and color accuracy.","summary_ja":"5千円差でDJI Osmo Action 4がスコア上。DJIはHorizonSteady・大型センサーが強み。GoPro HERO12はエコシステム。","summary_en":"¥5,000 apart, DJI Osmo Action 4 scores higher. DJI wins with HorizonSteady and larger sensor. GoPro has ecosystem."},
  {"slug":"compare-sonyzve10ii-vs-canoneosr50","cat":"カメラ","cat_en":"Camera","emoji":"📷","bg":"#1a0a00,#2d1a00","a":{"name":"Sony ZV-E10 II","price":"¥79,800","score":4.8,"slug":"review-sonyzve10ii"},"b":{"name":"Canon EOS R50","price":"¥89,800","score":4.6,"slug":"review-canoneosr50"},"verdict_ja":"動画・Vlog中心の用途にはSony ZV-E10 II、写真と動画のバランスを求めるならCanon EOS R50","verdict_en":"Sony ZV-E10 II for video creators and vloggers; Canon EOS R50 for a balanced photo and video mirrorless camera.","summary_ja":"1万円差でSonyがスコア上。ZV-E10 IIは自動フレーミング・AI被写体認識でVlog向け最高峰。","summary_en":"¥10,000 gap, Sony scores higher. ZV-E10 II is the ultimate vlog camera with auto-framing and AI subject tracking."},
  {"slug":"compare-fujifilmxt5-vs-sonya7cii","cat":"カメラ","cat_en":"Camera","emoji":"📷","bg":"#1a0a00,#2d1a00","a":{"name":"Fujifilm X-T5","price":"¥299,800","score":4.7,"slug":"review-fujifilmxt5"},"b":{"name":"Sony a7C II","price":"¥389,800","score":4.8,"slug":"review-sonya7cii"},"verdict_ja":"フィルムシミュレーションと高解像APS-CをすすめるならFujifilm X-T5、フルサイズ総合性能ならSony a7C II","verdict_en":"Fujifilm X-T5 for Film Simulation and high-resolution APS-C; Sony a7C II for full-frame all-round performance.","summary_ja":"9万円差。X-T5は4020万画素APS-CとフィルムシミュレーションでFujiの真髄。a7C IIはフルサイズ・AI AF。","summary_en":"¥90,000 difference. X-T5 delivers 40MP APS-C and Film Simulation. a7C II offers full-frame sensor and AI AF."},
  {"slug":"compare-insta360x4-vs-goprohero12","cat":"カメラ","cat_en":"Camera","emoji":"📷","bg":"#1a0a00,#2d1a00","a":{"name":"Insta360 X4","price":"¥69,800","score":4.5,"slug":"review-insta360x4"},"b":{"name":"GoPro HERO12","price":"¥54,800","score":4.5,"slug":"review-goprohero12"},"verdict_ja":"360度動画で創造的な表現をするならInsta360 X4、従来型アクションカメラの信頼性ならGoPro HERO12","verdict_en":"Insta360 X4 for creative 360-degree video; GoPro HERO12 for proven traditional action camera reliability.","summary_ja":"1.5万円差で同スコア。Insta360 X4は360度撮影と8K動画が独自強み。GoPro HERO12はアクション専門。","summary_en":"¥15,000 difference, same score. Insta360 X4 excels with 360-degree capture and 8K video. GoPro HERO12 is the action specialist."},
  {"slug":"compare-roborocks8maxv-vs-dreameX40ultra","cat":"ロボット掃除機","cat_en":"Robot Vacuum","emoji":"🤖","bg":"#0a1628,#1a2744","a":{"name":"Roborock S8 MaxV Ultra","price":"¥159,800","score":4.9,"slug":"review-roborocks8maxv"},"b":{"name":"Dreame X40 Ultra","price":"¥149,800","score":4.7,"slug":"review-dreameX40ultra"},"verdict_ja":"吸引力と全自動メンテナンスを最優先するならRoborock S8 MaxV Ultra、機械腕の新技術ならDreame X40 Ultra","verdict_en":"Roborock S8 MaxV Ultra for top suction and auto maintenance; Dreame X40 Ultra for innovative robotic arm technology.","summary_ja":"1万円差でRoborockがスコア大幅上。38000Paの吸引力は業界最高峰。Dreame X40 Ultraは伸縮アームが革新的。","summary_en":"¥10,000 gap, Roborock scores much higher. 38,000Pa suction is industry-leading. Dreame X40 Ultra has extendable arm."},
  {"slug":"compare-dreameX40ultra-vs-ecovacsX5pro","cat":"ロボット掃除機","cat_en":"Robot Vacuum","emoji":"🤖","bg":"#0a1628,#1a2744","a":{"name":"Dreame X40 Ultra","price":"¥149,800","score":4.7,"slug":"review-dreameX40ultra"},"b":{"name":"Ecovacs X5 Pro","price":"¥139,800","score":4.6,"slug":"review-ecovacsX5pro"},"verdict_ja":"吸引力と新技術を重視するならDreame X40 Ultra、AI認識とコスパを重視するならEcovacs X5 Pro","verdict_en":"Dreame X40 Ultra for powerful suction and innovative features; Ecovacs X5 Pro for AI recognition and value.","summary_ja":"1万円差。Dreame X40 Ultraは伸縮アームで家具下まで清掃。Ecovacs X5 ProはAIVI 3Dが障害物認識。","summary_en":"¥10,000 difference. Dreame X40 Ultra arm reaches under furniture. Ecovacs X5 Pro excels with AIVI 3D obstacle recognition."},
  {"slug":"compare-iroombaj9plus-vs-eufyrobovacx8","cat":"ロボット掃除機","cat_en":"Robot Vacuum","emoji":"🤖","bg":"#0a1628,#1a2744","a":{"name":"iRobot Roomba j9+","price":"¥129,800","score":4.7,"slug":"review-iroombaj9plus"},"b":{"name":"Eufy RoboVac X8","price":"¥79,800","score":4.4,"slug":"review-eufyrobovacx8"},"verdict_ja":"自動ゴミ収集と使いやすさを重視するならRoomba j9+、5万円安くコスパ重視ならEufy RoboVac X8","verdict_en":"iRobot Roomba j9+ for auto-empty convenience and ease of use; Eufy RoboVac X8 for great value at lower cost.","summary_ja":"5万円差。Roomba j9+はAIスマートマップと自動ゴミ収集が便利。Eufy X8は2倍吸引力でコスパ優秀。","summary_en":"¥50,000 gap. Roomba j9+ excels with AI smart mapping and auto-empty. Eufy X8 impresses with dual-turbine suction."},
  {"slug":"compare-boseSoundLinkMax-vs-marshallEmberton3","cat":"スピーカー","cat_en":"Speaker","emoji":"🔊","bg":"#1a1a2e,#2d2d44","a":{"name":"Bose SoundLink Max","price":"¥29,700","score":4.7,"slug":"review-boseSoundLinkMax"},"b":{"name":"Marshall Emberton III","price":"¥18,700","score":4.5,"slug":"review-marshallEmberton3"},"verdict_ja":"音の深みと大音量Boseサウンドを求めるならBose SoundLink Max、クラシックなデザインとコスパならMarshall Emberton III","verdict_en":"Bose SoundLink Max for deep, powerful Bose sound; Marshall Emberton III for classic design and outstanding value.","summary_ja":"1.1万円差。Bose SoundLink Maxは360度サウンドとIP67が強み。Marshall Emberton IIIは個性的デザイン。","summary_en":"¥11,000 difference. Bose SoundLink Max wins with 360-degree sound and IP67. Marshall Emberton III has iconic design."},
  {"slug":"compare-jblflip6-vs-boseSoundLinkMax","cat":"スピーカー","cat_en":"Speaker","emoji":"🔊","bg":"#1a1a2e,#2d2d44","a":{"name":"JBL Flip 6","price":"¥14,800","score":4.5,"slug":"review-jblflip6"},"b":{"name":"Bose SoundLink Max","price":"¥29,700","score":4.7,"slug":"review-boseSoundLinkMax"},"verdict_ja":"コンパクトで持ち運びやすいポータブルスピーカーにはJBL Flip 6、より高音質の大型サウンドならBose SoundLink Max","verdict_en":"JBL Flip 6 for compact portability and value; Bose SoundLink Max for larger, richer sound quality.","summary_ja":"1.5万円差。JBL Flip 6はIP67防水・12時間で超コスパ。Bose SoundLink Maxは圧倒的な音量・音質。","summary_en":"¥15,000 difference. JBL Flip 6 offers IP67 and 12-hour battery at great value. Bose SoundLink Max delivers superior volume."},
]

CAT_SLUG_MAP = {"スマートフォン":"cat-smartphone.html","イヤホン":"cat-earphone.html","スマートウォッチ":"cat-smartwatch.html","タブレット":"cat-tablet.html","ノートPC":"cat-laptop.html","ゲーム機":"cat-gaming.html","モニター":"cat-monitor.html","カメラ":"cat-camera.html","ロボット掃除機":"cat-robotvacuum.html","スピーカー":"cat-speaker.html"}
REDIRECT_JS = '  <script>!function(){if(location.pathname.startsWith(\'/en/\'))return;if(localStorage.getItem(\'gadgetnavi_lang\')===\'ja\')return;var l=(navigator.language||\'\').toLowerCase();if(l===\'en\'||l.startsWith(\'en-\')){localStorage.setItem(\'gadgetnavi_lang\',\'en\');location.replace(\'/en\'+location.pathname+location.search);}}();</script>'

CSS = """  <style>
    .cmp{max-width:860px;margin:0 auto;padding:40px 20px 80px}
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
    .smry{background:var(--secondary);color:#fff;border-radius:var(--radius);padding:28px 32px;margin-bottom:32px}
    .smry h2{font-size:1.1rem;font-weight:800;margin-bottom:16px;color:var(--accent)}
    .smry p{font-size:.9rem;line-height:1.85;color:rgba(255,255,255,.85);margin:0}
    .buy{background:#fff8f0;border:2px solid var(--primary);border-radius:var(--radius);padding:24px;margin-bottom:32px}
    .buy h3{font-size:1rem;font-weight:800;margin-bottom:16px;color:#222;text-align:center}
    .buy-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
    .buy-item{text-align:center}
    .buy-name{font-size:.85rem;font-weight:700;margin-bottom:10px;color:#333}
    .buy-btns{display:flex;flex-direction:column;gap:8px}
    .btn-amz{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:#ff9900;color:#111;padding:10px 18px;border-radius:50px;font-weight:800;font-size:.85rem;text-decoration:none}
    .btn-rkt{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:#bf0000;color:#fff;padding:10px 18px;border-radius:50px;font-weight:800;font-size:.85rem;text-decoration:none}
    .btn-rev{display:inline-flex;align-items:center;justify-content:center;gap:6px;background:var(--secondary);color:#fff;padding:10px 18px;border-radius:50px;font-weight:700;font-size:.85rem;text-decoration:none}
    @media(max-width:768px){.cmp{padding:20px 14px 60px}.hero{padding:28px 16px}.sc{grid-template-columns:1fr;gap:12px;padding:20px 14px}.vs{margin:0 auto}.buy-grid{grid-template-columns:1fr}}
  </style>"""

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
    cat_page = CAT_SLUG_MAP.get(c["cat"], "index.html")

    if is_en:
        html_lang, title = "en", f"{a['name']} vs {b['name']} Comparison 2026 | GadgetNavi"
        desc = f"Compare {a['name']} vs {b['name']}. Price, specs, and which one to buy in 2026."
        sub = "Which one should you buy? 2026 In-Depth Comparison"
        verdict_label, verdict = "Verdict", c["verdict_en"]
        summary_label, summary = "Summary", c["summary_en"]
        buy_label, back = "Buy Now", "Back to Comparisons"
        logo = '📱 Gadget<span class="logo-dot">Navi</span>'
        canon = f'{BASE_URL}en/{c["slug"]}.html'
        home, cat_href = "/en/", f'/en/{cat_page}'
        home_label, cat_label = "Home", c["cat_en"]
        nav = '<a href="/en/#ranking">Rankings</a>\n      <a href="/en/#reviews">Reviews</a>\n      <a href="/en/#compare">Compare</a>\n      <a href="/en/faq.html">FAQ</a>'
        lang_btns = f'<a href="/{c["slug"]}.html" class="lang-btn" onclick="localStorage.setItem(\'gadgetnavi_lang\',\'ja\')">&#127471;&#127477; JA</a>\n      <span class="lang-btn active">&#127468;&#127463; EN</span>'
        rev_a, rev_b = f'/en/{a["slug"]}.html', f'/en/{b["slug"]}.html'
        rev_label, back_href = "Full Review", "/en/#compare"
        footer_txt = "This site participates in affiliate programs. We may earn commissions from purchases through links."
        footer_copy = "2026 GadgetNavi All Rights Reserved."
        footer_links = '<a href="/en/privacy.html" style="color:rgba(255,255,255,.5)">Privacy Policy</a>'
        redir = ""
        badge = c["cat_en"].upper() + " COMPARISON"
        buy_btns_a = f'<a href="{amz_a}" target="_blank" rel="nofollow noopener" class="btn-amz">Amazon</a>\n          <a href="{rev_a}" class="btn-rev">{rev_label}</a>'
        buy_btns_b = f'<a href="{amz_b}" target="_blank" rel="nofollow noopener" class="btn-amz">Amazon</a>\n          <a href="{rev_b}" class="btn-rev">{rev_label}</a>'
    else:
        html_lang, title = "ja", f"{a['name']} vs {b['name']} 徹底比較【2026年版】｜ガジェットナビ"
        desc = f"{a['name']}と{b['name']}を徹底比較。価格・スペック・どちらを買うべきかを解説。"
        sub = "どちらを買うべき？2026年版 徹底比較"
        verdict_label, verdict = "結論", c["verdict_ja"]
        summary_label, summary = "総評", c["summary_ja"]
        buy_label, back = "購入リンク", "比較記事一覧に戻る"
        logo = '📱 ガジェット<span class="logo-dot">ナビ</span>'
        canon = f'{BASE_URL}{c["slug"]}.html'
        home, cat_href = "/", f'/{cat_page}'
        home_label, cat_label = "トップ", c["cat"]
        nav = '<a href="/#ranking">ランキング</a>\n      <a href="/#reviews">レビュー</a>\n      <a href="/#compare">比較</a>\n      <a href="/privacy.html">プライバシー</a>'
        lang_btns = f'<span class="lang-btn active">&#127471;&#127477; JA</span>\n      <a href="/en/{c["slug"]}.html" class="lang-btn" onclick="localStorage.setItem(\'gadgetnavi_lang\',\'en\')">&#127468;&#127463; EN</span>'
        rev_a, rev_b = f'/{a["slug"]}.html', f'/{b["slug"]}.html'
        rev_label, back_href = "詳細レビュー", "/#compare"
        footer_txt = "当サイトはアフィリエイトプログラムに参加しています。リンク経由での購入により手数料が発生する場合があります。"
        footer_copy = "2026 ガジェットナビ All Rights Reserved."
        footer_links = '<a href="/privacy.html" style="color:rgba(255,255,255,.5)">プライバシーポリシー</a>'
        redir = REDIRECT_JS + "\n"
        badge = c["cat_en"] + " COMPARISON"
        buy_btns_a = f'<a href="{amz_a}" target="_blank" rel="nofollow noopener" class="btn-amz">Amazon</a>\n          <a href="{rkt_a}" target="_blank" rel="nofollow noopener" class="btn-rkt">楽天</a>\n          <a href="{rev_a}" class="btn-rev">{rev_label}</a>'
        buy_btns_b = f'<a href="{amz_b}" target="_blank" rel="nofollow noopener" class="btn-amz">Amazon</a>\n          <a href="{rkt_b}" target="_blank" rel="nofollow noopener" class="btn-rkt">楽天</a>\n          <a href="{rev_b}" class="btn-rev">{rev_label}</a>'

    alt = f'  <link rel="alternate" hreflang="ja" href="{BASE_URL}{c["slug"]}.html">\n  <link rel="alternate" hreflang="en" href="{BASE_URL}en/{c["slug"]}.html">\n  <link rel="alternate" hreflang="x-default" href="{BASE_URL}{c["slug"]}.html">'

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
  <meta property="og:image" content="{BASE_URL}ogp-default.svg">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2054301472533985" crossorigin="anonymous"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ERDKSGNEWS"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-ERDKSGNEWS');</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800;900&display=swap" rel="stylesheet">
{CSS}
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
  <div class="bc"><a href="{home}">{home_label}</a><span>›</span><a href="{cat_href}">{cat_label}</a><span>›</span><span>{a['name']} vs {b['name']}</span></div>
  <div class="hero" style="background:linear-gradient(135deg,{bg1.strip()},{bg2.strip()})">
    <div class="badge">{badge}</div>
    <div style="font-size:3rem;margin-bottom:10px">{c['emoji']}</div>
    <h1>{a['name']} vs {b['name']}</h1>
    <p class="sub">{sub}</p>
  </div>
  <div class="vrd"><div class="vl">&#128203; {verdict_label}</div><p>{verdict}</p></div>
  <div class="sc">
    <div class="sc-card"><div class="pn">{a['name']}</div><div class="pp">{a['price']}</div><div class="sn">{a['score']}</div><div class="sm">/ 5.0</div><div class="sb"><div class="sbf" style="width:{sba}%"></div></div></div>
    <div class="vs">VS</div>
    <div class="sc-card"><div class="pn">{b['name']}</div><div class="pp">{b['price']}</div><div class="sn">{b['score']}</div><div class="sm">/ 5.0</div><div class="sb"><div class="sbf" style="width:{sbb}%"></div></div></div>
  </div>
  <div class="smry"><h2>&#128202; {summary_label}</h2><p>{summary}</p></div>
  <div class="buy">
    <h3>&#128722; {buy_label}</h3>
    <div class="buy-grid">
      <div class="buy-item"><div class="buy-name">{a['name']}</div><div class="buy-btns">{buy_btns_a}</div></div>
      <div class="buy-item"><div class="buy-name">{b['name']}</div><div class="buy-btns">{buy_btns_b}</div></div>
    </div>
  </div>
  <a href="{back_href}" style="display:inline-flex;align-items:center;gap:6px;color:var(--primary);font-weight:700;font-size:.9rem;">&#8592; {back}</a>
</div>
</main>
<footer>
  <div class="footer-inner">
    <div class="footer-disclaimer">{footer_txt}</div>
    <div class="footer-bottom"><p>&#169; {footer_copy}</p><p>{footer_links}</p></div>
  </div>
</footer>
</body>
</html>"""


# Generate files
en_dir = os.path.join(BASE, "en")
ja_c = en_c = 0
for c in COMPARISONS:
    with open(os.path.join(BASE, f"{c['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(gen_page(c, "ja"))
        ja_c += 1
    with open(os.path.join(en_dir, f"{c['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(gen_page(c, "en"))
        en_c += 1
print(f"Pages: {ja_c} JA + {en_c} EN")

# Compare section for index pages
CAT_EMOJI = {"スマートフォン":"📱","イヤホン":"🎧","スマートウォッチ":"⌚","タブレット":"📟","ノートPC":"💻","ゲーム機":"🎮","モニター":"🖥️","カメラ":"📷","ロボット掃除機":"🤖","スピーカー":"🔊"}
CAT_GROUPS = {}
for c in COMPARISONS:
    CAT_GROUPS.setdefault(c["cat"], []).append(c)

SEC_STYLE = """    <style>
      .cmp-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:10px;margin-bottom:16px}
      .cmp-cat{font-size:.8rem;font-weight:800;color:var(--text-light);letter-spacing:.12em;text-transform:uppercase;margin:20px 0 8px;padding-left:2px}
      .cmp-card{display:flex;align-items:center;gap:12px;background:#fff;border:1.5px solid var(--border);border-radius:var(--radius-sm);padding:14px 16px;transition:border-color .2s,box-shadow .2s;text-decoration:none;color:inherit}
      .cmp-card:hover{border-color:var(--primary);box-shadow:0 4px 16px rgba(0,0,0,.08)}
      .cmp-emo{font-size:1.6rem;flex-shrink:0}
      .cmp-names{font-size:.85rem;font-weight:700;line-height:1.4;flex:1}
      .cmp-vs{color:var(--primary);font-weight:900;margin:0 2px}
      .cmp-sc{font-size:.75rem;color:var(--text-light);white-space:nowrap}
    </style>"""

def build_sec(title, subtitle, lang):
    sec = f'\n<!-- Compare -->\n<section class="section" id="compare">\n  <div class="container">\n    <div class="section-header">\n      <div class="section-label">&#9632; COMPARE</div>\n      <h2>{title}</h2>\n      <p>{subtitle}</p>\n    </div>\n{SEC_STYLE}\n'
    for cat, items in CAT_GROUPS.items():
        cat_label = items[0]["cat_en"] if lang == "en" else cat
        emoji = CAT_EMOJI.get(cat, "📦")
        sec += f'    <div class="cmp-cat">{emoji} {cat_label}</div>\n    <div class="cmp-grid">\n'
        for c in items:
            a, b = c["a"], c["b"]
            href = f'/en/{c["slug"]}.html' if lang == "en" else f'/{c["slug"]}.html'
            sec += f'      <a href="{href}" class="cmp-card"><span class="cmp-emo">{c["emoji"]}</span><div class="cmp-names">{a["name"]} <span class="cmp-vs">vs</span> {b["name"]}</div><span class="cmp-sc">{a["score"]}&#9733; vs {b["score"]}&#9733;</span></a>\n'
        sec += '    </div>\n'
    sec += '  </div>\n</section>\n'
    return sec

# Update index.html
idx_path = os.path.join(BASE, "index.html")
with open(idx_path, encoding="utf-8") as f:
    idx = f.read()
if 'id="compare"' not in idx:
    sec = build_sec("製品比較ガイド", "迷ったらここで比較。どちらを買うべきか2026年版で徹底解説", "ja")
    idx = idx.replace("\n<!-- Features -->", sec + "\n<!-- Features -->")
    idx = idx.replace(
        '<a href="#reviews">レビュー</a>\n      <a href="privacy.html">',
        '<a href="#reviews">レビュー</a>\n      <a href="#compare">比較</a>\n      <a href="privacy.html">'
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(idx)
    print("index.html: compare section + nav added")

# Update en/index.html
en_idx_path = os.path.join(en_dir, "index.html")
with open(en_idx_path, encoding="utf-8") as f:
    eidx = f.read()
if 'id="compare"' not in eidx:
    sec = build_sec("Product Comparison Guide", "Can't decide? Compare head-to-head and find your perfect pick.", "en")
    if '<!-- Features -->' in eidx:
        eidx = eidx.replace('<!-- Features -->', sec + '<!-- Features -->')
    else:
        eidx = eidx.replace('<footer>', sec + '<footer>', 1)
    eidx = eidx.replace(
        '<a href="/en/#reviews">Reviews</a>',
        '<a href="/en/#reviews">Reviews</a>\n      <a href="/en/#compare">Compare</a>'
    )
    with open(en_idx_path, "w", encoding="utf-8") as f:
        f.write(eidx)
    print("en/index.html: compare section + nav added")

# Update sitemap
sm_path = os.path.join(BASE, "sitemap.xml")
with open(sm_path, encoding="utf-8") as f:
    sm = f.read()
new = ""
for c in COMPARISONS:
    if f'{c["slug"]}.html' not in sm:
        new += f'  <url>\n    <loc>{BASE_URL}{c["slug"]}.html</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
    if f'en/{c["slug"]}.html' not in sm:
        new += f'  <url>\n    <loc>{BASE_URL}en/{c["slug"]}.html</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.7</priority>\n  </url>\n'
if new:
    sm = sm.replace("</urlset>", new + "</urlset>")
    with open(sm_path, "w", encoding="utf-8") as f:
        f.write(sm)
    print("sitemap.xml updated")

print("ALL DONE")
