# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:04:08 2019

@author: daman

Simple file for pulling and saving the logos and players of each cwl team as 
of 6/8/19. Currently, this process as can be seen is still somewhat manual 
and could be better suited for more automation for ease of updating. Only
issue is it looks like JS is used to handle these pieces and bs4 cannot 
properly pull it in.

"""
import urllib.request


# Team Logos

# Div A

urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/optic-gaming/optic-logo-black.png', "logos/og.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/luminocity/Luminosity-Logo.png', "logos/lg.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/team-space/GEN_G.png', "logos/geng.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/evil-geniuses/EG_Logo_Blue.png', "logos/eg.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/faze-clan/FAZE_CLAN.png', "logos/faze.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/reciprocity/RECIPROCITY.png', "logos/rec.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/uyu/uyu.png', "logos/uyu.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/midnight/midnightLogo.png', "logos/mdn.png")
 
 # Div B
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/splyce/Splyce_Branding2018_Seal.png', "logos/splyce.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/eunited/EUNITED.png', "logos/eu.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/one-hundred-thieves/32_100T_Logo_Red_1920x1080.jpg', "logos/100T.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/team-envy/Envy-Logo-Dark.png', "logos/envy.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/heretics/Team_Heretics_2018_08_05.png', "logos/heretics.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/excelerategg/Elevate.png', "logos/elvevate.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/denial-esports/DenialLogo.png', "logos/denial.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/enigma6/E6_BLACK.png', "logos/e6.png")
 
# Players

# Div A

#og
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/optic-gaming/Optic-Gaming-Scump.png', 'players/Scump.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/optic-gaming/Optic-Gaming-Crimsix.png', 'players/Crimsix.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/optic-gaming/Optic-Gaming-TJHaly.png', 'players/TJHaly.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/optic-gaming/Optic-Gaming-Karma.png', 'players/Karma.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/optic-gaming/Optic-Gaming-Dashy.png', 'players/Dashy.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/Generic-Headshot/cwl-default-headshot.png', 'players/TeePee.png')

#lg
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/luminocity/Luminosity-Slacked.png', "Slacked.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/pittsburgh-knights/Pittsburgh_Knights_ricky.png', "Ricky.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/luminocity/Luminosity-Formal.png', "Formal.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/luminocity/Luminosity-John.png', "John.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/luminocity/Luminosity-Classic.png', "Classic.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/luminocity/Luminosity-Gunless.png', "Gunless.png")

#geng
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/gen-g/GenG-Havok.png', "players/Havok.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/gen-g/GenG-Envoy.png', "players/Envoy.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/gen-g/GenG-Maniak.png', "players/MajorManiak.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/gen-g/GenG-Nagafen.png', "players/Nagafen.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/gen-g/GenG-Maux.png', "players/Maux.png")
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/team-space/Team_Space_Spacely.png', "players/Spacely.png")

#faze
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/faze-clan/Faze-Clan-Zooma.png', 'players/Zooma.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/faze-clan/Faze-Clan-Cellium.png', 'players/Cellium.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/faze-clan/Faze-Clan-Asim.png', 'players/Asim.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/faze-clan/Faze_Clan_Scrapz.png', 'players/Skrapz.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/faze-clan/Faze-Clan-Zero.png', 'players/Zer0.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/fc-black/Faze_Clan_Black_-_GRVTY.png', 'players/Grvty.png')

#rec
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/reciprocity/Reciprocity-Zedd.png', 'players/Zed.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/reciprocity/Reciprocity-Seanny.png', 'players/Seany.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/reciprocity/Reciprocity_-_Denz.png', 'players/Denz.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/reciprocity/Reciprocity-Wuskin.png', 'players/Wuskin.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/reciprocity/Reciprocity-Dylan.png', 'players/Dylan.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/reciprocity/Reciprocity-Tommey.png', 'players/Tommey.png')

#uyu
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/uyu/UYU_Methodz.png', 'players/Methodz.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/uyu/UYU-MayhemNEW.png', 'players/Mayhem.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/uyu/UYU_Royalty.png', 'players/Royalty.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/uyu/UYU_Zaptius.png', 'players/Zaptius.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/uyu/UYU-Parzelion.png', 'players/Parzelion.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/uyu/UYU-Proto.png', 'players/Proto.png')

#mdn
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/midnight/Midnight-llamagod.png', 'players/llamagod.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/midnight/Midnight-Saints.png', 'players/Saints.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/midnight/Midnight-Blazt.png', 'players/Blazt.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/midnight/Midnight-Lacefield.png', 'players/Lacefield.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/midnight/Midnight-Parasite.png', 'players/Parasite.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/Generic-Headshot/cwl-default-headshot.png', 'players/GorgoKnight.png')

 
# Div B

#Splyce
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/team-sween/Sween_-_Nolson-469.png', 'players/Nolson.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/splyce/Splyce-Aqua.png', 'players/Aqua.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/splyce/Splyce-Loony.png', 'players/Loony.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/splyce/Splyce-Temp.png', 'players/Temp.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/splyce/Splyce-Jurd.png', 'players/Jurd.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/splyce/Splyce-Accuracy.png', 'players/Accuracy.png')
 
#eu
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/eunited/eUnited-Clayster.png', 'players/Clayster.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/eunited/eUnited-Abezy.png', 'players/Abezy.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/eunited/eUnited-Simp.png', 'players/Simp.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/eunited/eUnited-Arcitys.png', 'players/Arcitys.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/eunited/eUnited-Prestinni.png', 'players/Prestinni.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/Generic-Headshot/cwl-default-headshot.png', 'players/Spoofs.png')
 
#100T
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/one-hundred-thieves/100_Thieves_-_Slasher.png', 'players/Slasher.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/one-hundred-thieves/100_Thieves_-_Octane.png', 'players/Octane.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/one-hundred-thieves/100_Thieves_-_Kenny.png', 'players/Kenny.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/one-hundred-thieves/100_Thieves_-_Priestahh.png', 'players/Priestahh.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/one-hundred-thieves/100_Thieves_-_Enable.png', 'players/Enable.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/Generic-Headshot/cwl-default-headshot.png', 'players/Crowder.png')
 
#Envy
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/team-envy/Envy_Aches.png', 'players/Aches.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/one-hundred-thieves/100_Thieves_F3ROCITYS.png', 'players/Fero.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/g2-esports/G2_-_Decimate.png', 'players/Decimate.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/team-envy/Envy_-_Silly.png', 'players/Silly.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/team-envy/Envy_-_Huke.png', 'players/Huke.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/Generic-Headshot/cwl-default-headshot.png', 'players/Bevils.png')
 
#Heretics
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/heretics/Heretics_-_Lucky.png', 'players/Lucky.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/heretics/Heretics_-_Methodzsick.png', 'players/Methodzsick.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/heretics/Heretics_-_Jurnii.png', 'players/Jurnii.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/heretics/Heretics_-_Sukry.png', 'players/Sukry.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/heretics/Heretics_-_Mettalz.png', 'players/Mettalz.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/Generic-Headshot/cwl-default-headshot.png', 'players/Lgend.png')


#elevate
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/overtime/Overtime_-_Wailers.png', 'players/Wailers.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/overtime/Overtime_-_Breeszy.png', 'players/Brezsy.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/excelerategg/Excelerate-Mruiz.png', 'players/MRuiz.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/excelerategg/Excelerate-Skyz.png', 'players/Skyz.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/excelerategg/Excelerate-Profezzy.png', 'players/Profeezy.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/overtime/Overtime_-_Rizk.png', 'players/Rizk.png')

#Denial
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/excelerategg/Excelerate-Brack.png', 'players/Brack.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/red-reserve/Red_Reserve_Joe.png', 'players/Joe.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/red-reserve/Red_Reserve_Bancce.png', 'players/Bance.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/red-reserve/Red_Reserve_Red.png', 'players/Rated.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/lightning-pandas/Lightning_Pandas_-_Alexx.png', 'players/Alexx.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/overtime/Overtime_-_Zeeked.png', 'players/Zeeked.png')

#e6
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/enigma6/Enigma6-General.png', 'players/General.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/enigma6/Enigma6_Frosty.png', 'players/Fr9sty.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/excelerategg/Excelerate-JetLi.png', 'players/JetLi.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/enigma6/Enigma6_Kismet.png', 'players/Kismet.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/pittsburgh-knights/Pittsburgh_Knights_godrx.png', 'players/GodRx.png')
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/Generic-Headshot/cwl-default-headshot.png', 'players/Sender.png')

# default if player does not exist in player png files
urllib.request.urlretrieve('https://www.callofduty.com/content/dam/atvi/callofduty/esportal/teams/Generic-Headshot/cwl-default-headshot.png', 'players/default.png')