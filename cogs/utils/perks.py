class Surviver:
    surviver_perks = {
        '身軽':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/85/lightweight.png',
        'コソ泥の本能':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/87/plunderersInstinct.png',
        '小さな獲物':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/91/smallGame.png',
        'ツルツルとした肉体':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/90/slipperyMeat.png',
        'デジャヴ':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/83/dejaVu.png',
        '逆境魂':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/89/resilience.png',
        '痛みも気から':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/93/thisIsNotHappening.png',
        '血族':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/320/Kindred_Icon.png',
        'きっとやり遂げる':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/94/wellMakeIt.png',
        '希望':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/84/hope.png',
        '誰も見捨てはしない':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/86/noOneLeftBehind.png',
        '予感':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/88/premonition.png',
        '凍りつく背筋':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/92/spineChill.png',
        '闇の感覚':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/82/darkSense.png',
        '絆':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/15/70/bond.png',
        '有能の証明':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/15/72/provetyself.png',
        'リーダー':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/15/71/leader.png',
        '素早く静かに':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/14/68/quickandquiet.png',
        '全力疾走':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/14/69/sprintburst.png',
        'アドレナリン':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/14/67/adrenaline.png',
        '鋼の意志':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/13/65/ironwill.png',
        '魂の平穏':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/13/64/calmwill.png',
        'サボタージュ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/148/2156/Saboteur.png',
        '共感':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/16/74/empathy.png',
        '植物学の知識':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/16/73/botanyknowledge.png',
        'セルフケア':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/16/75/selfcare.png',
        'スマートな着地':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/53/311/balanced_landing.png',
        '都会の逃走術':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/53/313/urban_evasion.png',
        '都会の生存術':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/53/312/Streetwise.png',
        '唯一の生存者':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/57/427/Halloween_lastsurvivoricon.png',
        '執念の対象':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/57/428/Halloween_objectofobsession.png',
        '決死の一撃':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/57/426/Halloween_decisivestrike.png',
        '手札公開':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/64/468/openhanded.png',
        '賭け金のレイズ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/64/469/uptheante.png',
        '最後の切り札':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/64/467/aceinthehole.png',
        '置き去りにされた者':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/511/dbd-survivor-perk-left-behind.png',
        '与えられた猶予':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/510/dbd-survivor-perk-borrowed-time.png',
        '不滅':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/512/dbd-survivor-perk-unbreakable.png',
        'テクニシャン':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/76/528/dbd-survivor-perks-technician.png',
        'しなやか':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/76/527/dbd-survivor-perks-lithe.png',
        '警戒':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/76/526/dbd-survivor-perks-alert.png',
        'ずっと一緒だ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/85/571/dbd-survivor-kingperk2.png',
        'デッド・ハード':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/85/570/dbd-survivor-kingperk1.png',
        '弱音はナシだ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/85/572/dbd-survivor-kingperk3.png',
        '目を覚ませ！':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/97/644/wakeup.png',
        '調剤学':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/97/642/phar-macy.png',
        '寝ずの番':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/97/643/vigil.png',
        '執念':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/118/791/dbd-perk-tenacity.png',
        '刑事の直感':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/118/789/dbd-perk-detectiveshunch.png',
        '張り込み':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/118/790/dbd-perk-stakeout.png',
        'ダンス・ウィズ・ミー':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/185/1068/DBD_Chapter08-Kate-Perks-Dance_With_Me_.png',
        'ウィンドウズ・オブ・オポチュニティ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/185/1069/DBD_Chapter08-Kate-Perks-Windows_Of_Opportunity_.png',
        'ボイルオーバー':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/185/1067/DBD_Chapter08-Kate-Perks-Boil_Over_.png',
        '陽動':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/232/1101/diversion.png',
        '解放':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/232/1102/deliverance.png',
        '独学者':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/232/1103/autodidact.png',
        'ブレイクダウン':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/258/1212/survivor-perks-aftercare.png',
        'ディストーション':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/258/1214/survivor-perks-distortion.png',
        '連帯感':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/291/1797/Solidarity.png',
        '平常心':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/291/1798/Poised.png',
        '真っ向勝負':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/291/1799/HeadOn.png',
        'フリップ・フロップ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/303/2095/Teachable_flip-Flop.png',
        'ベルトを締めろ！':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/303/2096/Teachable_buckleUp.png',
        '英雄の奮起':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/303/2097/Teachable_mettleOfMan.png',
        '一緒にいよう':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/320/2089/Teachable_betterTogether.png',
        '執着心':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/320/2090/Teachable_fixated.png',
        '内なる力':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/320/2091/Teachable_innerStrength.png',
        'ベビーシッター':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/321/2092/Teachable_babysitter.png',
        '仲間意識':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/321/2093/Teachable_camaraderie.png',
        'セカンドウインド':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/321/2094/Teachable_secondWind.png',
        '怪我の功名':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/342/1957/lucky-break.png',
        '強硬手段':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/342/1958/any-means-necessary.png',
        '突破':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/342/1959/breakout_.png',
        'オフレコ':'https://us.v-cdn.net/6030815/uploads/631/J3HOJ1DEKJ0E.png',
        'おとり':'https://us.v-cdn.net/6030815/uploads/134/HA9SRK3A41UQ.png',
        '人々のために':'https://us.v-cdn.net/6030815/uploads/321/E5XEBB6UOXXV.png',
        'ソウルガード':'https://us.v-cdn.net/6030815/uploads/V5GD8VV2JELK/10.png',
        '血の協定':'https://us.v-cdn.net/6030815/uploads/Y2VH95SYJBF7/11.png',
        '抑圧の同盟':'https://us.v-cdn.net/6030815/uploads/NRYKOXBPDXA5/12.png'
    }

class Killer:
    killer_perks = {
        'ずさんな肉屋':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/102/K_sloppyButcher.png',
        '忍び寄る者':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/95/K_deerstalker.png',
        '鋼の握力':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/98/K_ironGrasp.png',
        '呪術:狩りの興奮':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/497/IconPerks_thrillOfTheHunt.png',
        '無慈悲':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/104/K_unrelenting.png',
        '異形の祭壇':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/99/K_monstrousShrine.png',
        '苦悶の根源':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/96/K_distressing.png',
        '影の密偵':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/103/K_spiesFromTheShadows.png',
        '囁き':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/105/K_whispers.png',
        '狡猾':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/97/K_insidious.png',
        '憎悪の囁き':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/106/K_bitterMurmur.png',
        '呪術:誰も死から逃れられない':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/32/100/K_noOneEscapesDeath.png',
        '不安の元凶':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/20/55/unnerving.png',
        '野蛮な力':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/20/53/brutalstrength.png',
        '興奮':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/20/57/agitation.png',
        '捕食者':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/18/59/predator.png',
        '血の追跡者':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/18/58/bloodhound.png',
        '闇より出でし者':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/18/60/shadowborn.png',
        '不屈':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/19/61/Enduring.png',
        '光より出でし者':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/19/62/Lightborn.png',
        'ガラクタいじり':'http://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/19/63/Tinkerer.png',
        '喘鳴':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/50/318/dbd-killer-perk-stridor.png',
        '死恐怖症':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/50/319/dbd-killer-perk-thanatophobia.png',
        '看護婦の使命':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/50/317/dbd-killer-perk-nurses-calling.png',
        '最後のお楽しみ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/58/423/Save-best-for-last.png',
        '弄ばれる獲物':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/58/424/Play-with-your-food.png',
        '消えゆく灯':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/58/422/Dying-light.png',
        '呪術:第三の封印':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/65/464/thethirdseal.png',
        '呪術:破滅':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/65/463/ruin.png',
        '呪術:貪られる希望':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/65/462/devourhope.png',
        '圧倒的存在感':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/77/533/dbd-killer-perk-overwhelmingP.png',
        '観察&虐待':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/77/532/dbd-killer-perk-monitorabuse.png',
        'オーバーチャージ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/77/531/dbd-killer-perk-generationOvercharge.png',
        '猛獣':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/86/574/dbd-killer-hperk2.png',
        '縄張り意識':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/86/573/dbd-killer-hperk1.png',
        '呪術:女狩人の子守唄':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/86/575/dbd-killer-hperk3.png',
        'ノックアウト':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/91/610/dbd-killer-perk-leatherface1.png',
        'バーベキュー&チリ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/91/611/dbd-killer-perk-leatherface2.png',
        'フランクリンの悲劇':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/91/612/dbd-killer-perk-leatherface3.png',
        'ファイヤー・アップ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/95/639/fireupmanual.png',
        'リメンバー・ミー':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/95/640/remembermemanual.png',
        '血の番人':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/95/641/bloodwardenmanual.png',
        '処刑人の妙技':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/114/784/dbd-perk-hangmanstrick.png',
        '監視':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/114/786/dbd-perk-serveillance.png',
        '選択は君次第だ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/114/785/dbd-perk-makeyourchoice.png',
        'まやかし':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/187/1060/DBD_Chapter08-Clown-Perks-Bamboozle.png',
        'ピエロ恐怖症':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/187/1061/DBD_Chapter08-Clown-Perks-Coolrophobia.png',
        'イタチが飛び出した':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/187/1062/DBD_Chapter08-Clown-Perks-Pop_Goes_The_Weasle.png',
        '怨霊の怒り':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/234/1098/fury.png',
        '呪術：霊障の地':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/234/1099/hauntedground.png',
        '怨恨':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/234/1100/rancor.png',
        '不協和音':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/259/1215/killer-perks-discordance.png',
        '狂気の根性':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/259/1217/killer-perks-madgrit.png',
        'アイアンメイデン':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/259/1216/killer-perks-ironmaiden.png',
        '堕落の介入':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/292/1800/CorruptIntervention.png',
        '伝播する怖気':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/292/1801/InfectiousFright.png',
        '闇の信仰心':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/292/1802/DarkDevotion.png',
        '地獄耳':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/314/1893/iconPerks_imAllEars.png',
        '戦慄':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/314/1892/iconPerks_thrillingTremors.png',
        '隠密の追跡':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/314/1891/iconPerks_furtiveChase.png',
        'サージ':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/322/1937/Teachable_surge.png',
        'マインドブレーカー':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/322/1936/Teachable_mindbreaker.png',
        '無慈悲の極地':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/322/1935/Teachable_cruelLimits.png',
        '残心の戦術':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/340/1961/zanshin-tactics.png',
        '血の共鳴':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/340/1963/blood-echo.png',
        '天誅':'https://img.atwikiimg.com/www65.atwiki.jp/deadbydaylight/attach/340/1962/nemesis.png',
        '変速機':'https://us.v-cdn.net/6030815/uploads/927/AX74AEKIYWZN.png',
        '死人のスイッチ':'https://us.v-cdn.net/6030815/uploads/546/P2A2PD623ZSM.png',
        '呪術：報復':'https://us.v-cdn.net/6030815/uploads/905/YN5QDCTJSXYV.png',
        '強制苦行':'https://us.v-cdn.net/6030815/uploads/99PDYX3IA1BY/6.png',
        '煩悶のトレイル':'https://us.v-cdn.net/6030815/uploads/K8ZZH1Q3U9BA/7.png',
        'デスバウンド':'https://us.v-cdn.net/6030815/uploads/O4QBQ4H15KUO/8.png'
    }