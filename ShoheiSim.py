import pandas as pd
import matplotlib.pyplot as plt
import random 

season_league_totals={'AB':163465, 'H':39675,'1B':25877,'2B':7940, '3B':643, 'HR':5215, 'BB':14853, 'SO': 40812}
avg_player={'1B%':season_league_totals['1B']/season_league_totals['AB'], '2B%':season_league_totals['2B']/season_league_totals['AB'], 
     '3B%':season_league_totals['3B']/season_league_totals['AB'],'HR%':season_league_totals['HR']/season_league_totals['AB'], 
     'BB%':season_league_totals['BB']/season_league_totals['AB'], 'SO%':season_league_totals['SO']/season_league_totals['AB'],
     'OUT%':(season_league_totals['AB']-season_league_totals['H']-season_league_totals['BB']-season_league_totals['SO'])/season_league_totals['AB']}

Obat=pd.read_csv('OhtaniBatting.txt')
Opitch=pd.read_csv('OhtaniPitching.txt')

#Normal
ABb=0
Hb=0
twoBb=0
threeBb=0
HRb=0
BBb=0
SOb=0

ABp=0
Hp=0
twoBp=0
threeBp=0
HRp=0
BBp=0
SOp=0

#Sunny
ABbS=0
HbS=0
twoBbS=0
threeBbS=0
HRbS=0
BBbS=0
SObS=0

ABpS=0
HpS=0
twoBpS=0
threeBpS=0
HRpS=0
BBpS=0
SOpS=0

#Cloudy
ABbC=0
HbC=0
twoBbC=0
threeBbC=0
HRbC=0
BBbC=0
SObC=0

ABpC=0
HpC=0
twoBpC=0
threeBpC=0
HRpC=0
BBpC=0
SOpC=0

#Overcast
ABbO=0
HbO=0
twoBbO=0
threeBbO=0
HRbO=0
BBbO=0
SObO=0

ABpO=0
HpO=0
twoBpO=0
threeBpO=0
HRpO=0
BBpO=0
SOpO=0


#Dome
ABbD=0
HbD=0
twoBbD=0
threeBbD=0
HRbD=0
BBbD=0
SObD=0

ABpD=0
HpD=0
twoBpD=0
threeBpD=0
HRpD=0
BBpD=0
SOpD=0


ObatSunny=Obat.loc[Obat['Weather'] == 'Sunny']
ObatCloudy=Obat.loc[Obat['Weather'] == 'Cloudy']
ObatOvercast=Obat.loc[Obat['Weather'] == 'Overcast']
ObatDome=Obat.loc[Obat['Weather'] == 'Dome']

OpitchSunny=Opitch.loc[Opitch['Weather'] == 'Sunny']
OpitchCloudy=Opitch.loc[Opitch['Weather'] == 'Cloudy']
OpitchOvercast=Opitch.loc[Opitch['Weather'] == 'Overcast']
OpitchDome=Opitch.loc[Opitch['Weather'] == 'Dome']

#Normal
for i in Obat.index:
    ABb+=Obat['AB'][i]
    Hb+=Obat['H'][i]
    twoBb+=Obat['2B'][i]
    threeBb+=Obat['3B'][i]
    HRb+=Obat['HR'][i]
    BBb+=Obat['BB'][i]
    SOb+=Obat['SO'][i]
for i in Opitch.index:
    ABp+=Opitch['AB'][i]
    Hp+=Opitch['H'][i]
    twoBp+=Opitch['2B'][i]
    threeBp+=Opitch['3B'][i]
    HRp+=Opitch['HR'][i]
    BBp+=Opitch['BB'][i]
    SOp+=Opitch['SO'][i]
 
#Sunny
for i in ObatSunny.index:
    ABbS+=ObatSunny['AB'][i]
    HbS+=ObatSunny['H'][i]
    twoBbS+=ObatSunny['2B'][i]
    threeBbS+=ObatSunny['3B'][i]
    HRbS+=ObatSunny['HR'][i]
    BBbS+=ObatSunny['BB'][i]
    SObS+=ObatSunny['SO'][i]
for i in OpitchSunny.index:
    ABpS+=OpitchSunny['AB'][i]
    HpS+=OpitchSunny['H'][i]
    twoBpS+=OpitchSunny['2B'][i]
    threeBpS+=OpitchSunny['3B'][i]
    HRpS+=OpitchSunny['HR'][i]
    BBpS+=OpitchSunny['BB'][i]
    SOpS+=OpitchSunny['SO'][i]
    
#Cloudy
for i in ObatCloudy.index:
    ABbC+=ObatCloudy['AB'][i]
    HbC+=ObatCloudy['H'][i]
    twoBbC+=ObatCloudy['2B'][i]
    threeBbC+=ObatCloudy['3B'][i]
    HRbC+=ObatCloudy['HR'][i]
    BBbC+=ObatCloudy['BB'][i]
    SObC+=ObatCloudy['SO'][i]
for i in OpitchCloudy.index:
    ABpC+=OpitchCloudy['AB'][i]
    HpC+=OpitchCloudy['H'][i]
    twoBpC+=OpitchCloudy['2B'][i]
    threeBpC+=OpitchCloudy['3B'][i]
    HRpC+=OpitchCloudy['HR'][i]
    BBpC+=OpitchCloudy['BB'][i]
    SOpC+=OpitchCloudy['SO'][i]
    
#Overcast
for i in ObatOvercast.index:
    ABbO+=ObatOvercast['AB'][i]
    HbO+=ObatOvercast['H'][i]
    twoBbO+=ObatOvercast['2B'][i]
    threeBbO+=ObatOvercast['3B'][i]
    HRbO+=ObatOvercast['HR'][i]
    BBbO+=ObatOvercast['BB'][i]
    SObO+=ObatOvercast['SO'][i]
for i in OpitchOvercast.index:
    ABpO+=OpitchOvercast['AB'][i]
    HpO+=OpitchOvercast['H'][i]
    twoBpO+=OpitchOvercast['2B'][i]
    threeBpO+=OpitchOvercast['3B'][i]
    HRpO+=OpitchOvercast['HR'][i]
    BBpO+=OpitchOvercast['BB'][i]
    SOpO+=OpitchOvercast['SO'][i]
    
#Dome
for i in ObatDome.index:
    ABbD+=ObatDome['AB'][i]
    HbD+=ObatDome['H'][i]
    twoBbD+=ObatDome['2B'][i]
    threeBbD+=ObatDome['3B'][i]
    HRbD+=ObatDome['HR'][i]
    BBbD+=ObatDome['BB'][i]
    SObD+=ObatDome['SO'][i]
for i in OpitchDome.index:
    ABpD+=OpitchDome['AB'][i]
    HpD+=OpitchDome['H'][i]
    twoBpD+=OpitchDome['2B'][i]
    threeBpD+=OpitchDome['3B'][i]
    HRpD+=OpitchDome['HR'][i]
    BBpD+=OpitchDome['BB'][i]
    SOpD+=OpitchDome['SO'][i]
    
#Normal  
oneBb=Hb-twoBb-threeBb-HRb
oneBp=Hp-twoBp-threeBp-HRp
#Sunny
oneBbS=HbS-twoBbS-threeBbS-HRbS
oneBpS=HpS-twoBpS-threeBpS-HRpS
#Cloudy
oneBbC=HbC-twoBbC-threeBbC-HRbC
oneBpC=HpC-twoBpC-threeBpC-HRpC
#Overcast
oneBbO=HbO-twoBbO-threeBbO-HRbO
oneBpO=HpO-twoBpO-threeBpO-HRpO
#Dome
oneBbD=HbD-twoBbD-threeBbD-HRbD
oneBpD=HpD-twoBpD-threeBpD-HRpD

#Normal
OhtaniBatting={'1B%':oneBb/ABb, '2B%':twoBb/ABb, '3B%':threeBb/ABb,'HR%':HRb/ABb,'BB%':BBb/ABb, 'SO%':SOb/ABb, 'OUT%':(ABb-Hb-BBb-SOb)/ABb}
OhtaniPitching={'1B%':oneBp/ABp, '2B%':twoBp/ABp, '3B%':threeBp/ABp,'HR%':HRp/ABp,'BB%':BBp/ABp, 'SO%':SOp/ABp, 'OUT%':(ABp-Hp-BBp-SOp)/ABp}
#Sunny
OhtaniBattingS={'1B%':oneBbS/ABbS, '2B%':twoBbS/ABbS, '3B%':threeBbS/ABbS,'HR%':HRbS/ABbS,'BB%':BBbS/ABbS, 'SO%':SObS/ABbS, 'OUT%':(ABbS-HbS-BBbS-SObS)/ABbS}
OhtaniPitchingS={'1B%':oneBpS/ABpS, '2B%':twoBpS/ABpS, '3B%':threeBpS/ABpS,'HR%':HRpS/ABpS,'BB%':BBpS/ABpS, 'SO%':SOpS/ABpS, 'OUT%':(ABpS-HpS-BBpS-SOpS)/ABpS}
#Cloudy
OhtaniBattingC={'1B%':oneBbC/ABbC, '2B%':twoBbC/ABbC, '3B%':threeBbC/ABbC,'HR%':HRbC/ABbC,'BB%':BBbC/ABbC, 'SO%':SObC/ABbC, 'OUT%':(ABbC-HbC-BBbC-SObC)/ABbC}
OhtaniPitchingC={'1B%':oneBpC/ABpC, '2B%':twoBpC/ABpC, '3B%':threeBpC/ABpC,'HR%':HRpC/ABpC,'BB%':BBpC/ABpC, 'SO%':SOpC/ABpC, 'OUT%':(ABpC-HpC-BBpC-SOpC)/ABpC}
#Overcast
OhtaniBattingO={'1B%':oneBbO/ABbO, '2B%':twoBbO/ABbO, '3B%':threeBbO/ABbO,'HR%':HRbO/ABbO,'BB%':BBbO/ABbO, 'SO%':SObO/ABbO, 'OUT%':(ABbO-HbO-BBbO-SObO)/ABbO}
OhtaniPitchingO={'1B%':oneBpO/ABpO, '2B%':twoBpO/ABpO, '3B%':threeBpO/ABpO,'HR%':HRpO/ABpO,'BB%':BBpO/ABpO, 'SO%':SOpO/ABpO, 'OUT%':(ABpO-HpO-BBpO-SOpO)/ABpO}
#Dome
OhtaniBattingD={'1B%':oneBbD/ABbD, '2B%':twoBbD/ABbD, '3B%':threeBbD/ABbD,'HR%':HRbD/ABbD,'BB%':BBbD/ABbD, 'SO%':SObD/ABbD, 'OUT%':(ABbD-HbD-BBbD-SObD)/ABbD}
OhtaniPitchingD={'1B%':oneBpD/ABpD, '2B%':twoBpD/ABpD, '3B%':threeBpD/ABpD,'HR%':HRpD/ABpD,'BB%':BBpD/ABpD, 'SO%':SOpD/ABpD, 'OUT%':(ABpD-HpD-BBpD-SOpD)/ABpD}

#print(avg_player)
#print(OhtaniBatting)
#print(OhtaniPitching)

#Normal
#Ohtani Batting v National Average
OBvNA={'1B%':OhtaniBatting['1B%']-avg_player['1B%'], '2B%':OhtaniBatting['2B%']-avg_player['2B%'], '3B%':OhtaniBatting['3B%']-avg_player['3B%'],
       'HR%':OhtaniBatting['HR%']-avg_player['HR%'], 'BB%':OhtaniBatting['BB%']-avg_player['BB%'], 'SO%':OhtaniBatting['SO%']-avg_player['SO%'],
       'OUT%':OhtaniBatting['OUT%']-avg_player['OUT%']}

#Ohtani Pitching v National Average
OPvNA={'1B%':OhtaniPitching['1B%']-avg_player['1B%'], '2B%':OhtaniPitching['2B%']-avg_player['2B%'], '3B%':OhtaniPitching['3B%']-avg_player['3B%'],
       'HR%':OhtaniPitching['HR%']-avg_player['HR%'], 'BB%':OhtaniPitching['BB%']-avg_player['BB%'], 'SO%':OhtaniPitching['SO%']-avg_player['SO%'],
       'OUT%':OhtaniPitching['OUT%']-avg_player['OUT%']}

#Ohtani v National Average...Average
OvNAA={'1B%':OBvNA['1B%']-OPvNA['1B%'], '2B%':OBvNA['2B%']-OPvNA['2B%'], '3B%':OBvNA['3B%']-OPvNA['3B%'],
       'HR%':OBvNA['HR%']-OPvNA['HR%'], 'BB%':OBvNA['BB%']-OPvNA['BB%'], 'SO%':OBvNA['SO%']-OPvNA['SO%'],
       'OUT%':OBvNA['OUT%']-OPvNA['OUT%']}

#Expectation (Ohtani v Ohtani)
E={'1B%':OvNAA['1B%']+avg_player['1B%'], '2B%':OvNAA['2B%']+avg_player['2B%'], '3B%':OvNAA['3B%']+avg_player['3B%'],
       'HR%':OvNAA['HR%']+avg_player['HR%'], 'BB%':OvNAA['BB%']+avg_player['BB%'], 'SO%':OvNAA['SO%']+avg_player['SO%'],
       'OUT%':OvNAA['OUT%']+avg_player['OUT%']}

#Sunny
#Ohtani Batting v National Average
OBvNAS={'1B%':OhtaniBattingS['1B%']-avg_player['1B%'], '2B%':OhtaniBattingS['2B%']-avg_player['2B%'], '3B%':OhtaniBattingS['3B%']-avg_player['3B%'],
       'HR%':OhtaniBattingS['HR%']-avg_player['HR%'], 'BB%':OhtaniBattingS['BB%']-avg_player['BB%'], 'SO%':OhtaniBattingS['SO%']-avg_player['SO%'],
       'OUT%':OhtaniBattingS['OUT%']-avg_player['OUT%']}

#Ohtani Pitching v National Average
OPvNAS={'1B%':OhtaniPitchingS['1B%']-avg_player['1B%'], '2B%':OhtaniPitchingS['2B%']-avg_player['2B%'], '3B%':OhtaniPitchingS['3B%']-avg_player['3B%'],
       'HR%':OhtaniPitchingS['HR%']-avg_player['HR%'], 'BB%':OhtaniPitchingS['BB%']-avg_player['BB%'], 'SO%':OhtaniPitchingS['SO%']-avg_player['SO%'],
       'OUT%':OhtaniPitchingS['OUT%']-avg_player['OUT%']}

#Ohtani v National Average...Average
OvNAAS={'1B%':OBvNAS['1B%']-OPvNAS['1B%'], '2B%':OBvNAS['2B%']-OPvNAS['2B%'], '3B%':OBvNAS['3B%']-OPvNAS['3B%'],
       'HR%':OBvNAS['HR%']-OPvNAS['HR%'], 'BB%':OBvNAS['BB%']-OPvNAS['BB%'], 'SO%':OBvNAS['SO%']-OPvNAS['SO%'],
       'OUT%':OBvNAS['OUT%']-OPvNAS['OUT%']}

#Expectation (Ohtani v Ohtani)
ES={'1B%':OvNAAS['1B%']+avg_player['1B%'], '2B%':OvNAAS['2B%']+avg_player['2B%'], '3B%':OvNAAS['3B%']+avg_player['3B%'],
       'HR%':OvNAAS['HR%']+avg_player['HR%'], 'BB%':OvNAAS['BB%']+avg_player['BB%'], 'SO%':OvNAAS['SO%']+avg_player['SO%'],
       'OUT%':OvNAAS['OUT%']+avg_player['OUT%']}

#Cloudy
#Ohtani Batting v National Average
OBvNAC={'1B%':OhtaniBattingC['1B%']-avg_player['1B%'], '2B%':OhtaniBattingC['2B%']-avg_player['2B%'], '3B%':OhtaniBattingC['3B%']-avg_player['3B%'],
       'HR%':OhtaniBattingC['HR%']-avg_player['HR%'], 'BB%':OhtaniBattingC['BB%']-avg_player['BB%'], 'SO%':OhtaniBattingC['SO%']-avg_player['SO%'],
       'OUT%':OhtaniBattingC['OUT%']-avg_player['OUT%']}

#Ohtani Pitching v National Average
OPvNAC={'1B%':OhtaniPitchingC['1B%']-avg_player['1B%'], '2B%':OhtaniPitchingC['2B%']-avg_player['2B%'], '3B%':OhtaniPitchingC['3B%']-avg_player['3B%'],
       'HR%':OhtaniPitchingC['HR%']-avg_player['HR%'], 'BB%':OhtaniPitchingC['BB%']-avg_player['BB%'], 'SO%':OhtaniPitchingC['SO%']-avg_player['SO%'],
       'OUT%':OhtaniPitchingC['OUT%']-avg_player['OUT%']}

#Ohtani v National Average...Average
OvNAAC={'1B%':OBvNAC['1B%']-OPvNAC['1B%'], '2B%':OBvNAC['2B%']-OPvNAC['2B%'], '3B%':OBvNAC['3B%']-OPvNAC['3B%'],
       'HR%':OBvNAC['HR%']-OPvNAC['HR%'], 'BB%':OBvNAC['BB%']-OPvNAC['BB%'], 'SO%':OBvNAC['SO%']-OPvNAC['SO%'],
       'OUT%':OBvNAC['OUT%']-OPvNAC['OUT%']}

#Expectation (Ohtani v Ohtani)
EC={'1B%':OvNAAC['1B%']+avg_player['1B%'], '2B%':OvNAAC['2B%']+avg_player['2B%'], '3B%':OvNAAC['3B%']+avg_player['3B%'],
       'HR%':OvNAAC['HR%']+avg_player['HR%'], 'BB%':OvNAAC['BB%']+avg_player['BB%'], 'SO%':OvNAAC['SO%']+avg_player['SO%'],
       'OUT%':OvNAAC['OUT%']+avg_player['OUT%']}

#Overcast
#Ohtani Batting v National Average
OBvNAO={'1B%':OhtaniBattingO['1B%']-avg_player['1B%'], '2B%':OhtaniBattingO['2B%']-avg_player['2B%'], '3B%':OhtaniBattingO['3B%']-avg_player['3B%'],
       'HR%':OhtaniBattingO['HR%']-avg_player['HR%'], 'BB%':OhtaniBattingO['BB%']-avg_player['BB%'], 'SO%':OhtaniBattingO['SO%']-avg_player['SO%'],
       'OUT%':OhtaniBattingO['OUT%']-avg_player['OUT%']}

#Ohtani Pitching v National Average
OPvNAO={'1B%':OhtaniPitchingO['1B%']-avg_player['1B%'], '2B%':OhtaniPitchingO['2B%']-avg_player['2B%'], '3B%':OhtaniPitchingO['3B%']-avg_player['3B%'],
       'HR%':OhtaniPitchingO['HR%']-avg_player['HR%'], 'BB%':OhtaniPitchingO['BB%']-avg_player['BB%'], 'SO%':OhtaniPitchingO['SO%']-avg_player['SO%'],
       'OUT%':OhtaniPitchingO['OUT%']-avg_player['OUT%']}

#Ohtani v National Average...Average
OvNAAO={'1B%':OBvNAO['1B%']-OPvNAO['1B%'], '2B%':OBvNAO['2B%']-OPvNAO['2B%'], '3B%':OBvNAO['3B%']-OPvNAO['3B%'],
       'HR%':OBvNAO['HR%']-OPvNAO['HR%'], 'BB%':OBvNAO['BB%']-OPvNAO['BB%'], 'SO%':OBvNAO['SO%']-OPvNAO['SO%'],
       'OUT%':OBvNAO['OUT%']-OPvNAO['OUT%']}

#Expectation (Ohtani v Ohtani)
EO={'1B%':OvNAAO['1B%']+avg_player['1B%'], '2B%':OvNAAO['2B%']+avg_player['2B%'], '3B%':OvNAAO['3B%']+avg_player['3B%'],
       'HR%':OvNAAO['HR%']+avg_player['HR%'], 'BB%':OvNAAO['BB%']+avg_player['BB%'], 'SO%':OvNAAO['SO%']+avg_player['SO%'],
       'OUT%':OvNAAO['OUT%']+avg_player['OUT%']}

#Dome
#Ohtani Batting v National Average
OBvNAD={'1B%':OhtaniBattingD['1B%']-avg_player['1B%'], '2B%':OhtaniBattingD['2B%']-avg_player['2B%'], '3B%':OhtaniBattingD['3B%']-avg_player['3B%'],
       'HR%':OhtaniBattingD['HR%']-avg_player['HR%'], 'BB%':OhtaniBattingD['BB%']-avg_player['BB%'], 'SO%':OhtaniBattingD['SO%']-avg_player['SO%'],
       'OUT%':OhtaniBattingD['OUT%']-avg_player['OUT%']}

#Ohtani Pitching v National Average
OPvNAD={'1B%':OhtaniPitchingD['1B%']-avg_player['1B%'], '2B%':OhtaniPitchingD['2B%']-avg_player['2B%'], '3B%':OhtaniPitchingD['3B%']-avg_player['3B%'],
       'HR%':OhtaniPitchingD['HR%']-avg_player['HR%'], 'BB%':OhtaniPitchingD['BB%']-avg_player['BB%'], 'SO%':OhtaniPitchingD['SO%']-avg_player['SO%'],
       'OUT%':OhtaniPitchingD['OUT%']-avg_player['OUT%']}

#Ohtani v National Average...Average
OvNAAD={'1B%':OBvNAD['1B%']-OPvNAD['1B%'], '2B%':OBvNAD['2B%']-OPvNAD['2B%'], '3B%':OBvNAD['3B%']-OPvNAD['3B%'],
       'HR%':OBvNAD['HR%']-OPvNAD['HR%'], 'BB%':OBvNAD['BB%']-OPvNAD['BB%'], 'SO%':OBvNAD['SO%']-OPvNAD['SO%'],
       'OUT%':OBvNAD['OUT%']-OPvNAD['OUT%']}

#Expectation (Ohtani v Ohtani)
ED={'1B%':OvNAAD['1B%']+avg_player['1B%'], '2B%':OvNAAD['2B%']+avg_player['2B%'], '3B%':OvNAAD['3B%']+avg_player['3B%'],
       'HR%':OvNAAD['HR%']+avg_player['HR%'], 'BB%':OvNAAD['BB%']+avg_player['BB%'], 'SO%':OvNAAD['SO%']+avg_player['SO%'],
       'OUT%':OvNAAD['OUT%']+avg_player['OUT%']}


#print(OBvNA)
#print(OPvNA)
#print(OvNAA)
#print(E)

#Normal
ABprobs=[E['1B%'], E['2B%'], E['3B%'], E['HR%'], E['BB%'], E['SO%'], E['OUT%']]
#Sunny
ABprobsS=[ES['1B%'], ES['2B%'], ES['3B%'], ES['HR%'], ES['BB%'], ES['SO%'], ES['OUT%']]
#Cloudy
ABprobsC=[EC['1B%'], EC['2B%'], EC['3B%'], EC['HR%'], EC['BB%'], EC['SO%'], EC['OUT%']]
#Overcast
ABprobsO=[EO['1B%'], EO['2B%'], EO['3B%'], EO['HR%'], EO['BB%'], EO['SO%'], EO['OUT%']]
#Dome
ABprobsD=[ED['1B%'], ED['2B%'], ED['3B%'], ED['HR%'], ED['BB%'], ED['SO%'], ED['OUT%']]

#Global variables
home=0
away=0
outs=0
bases=[0,0,0,0]

singlesHit=0
doublesHit=0
triplesHit=0
homersHit=0
walksTaken=0
strikeOutsTaken=0
fieldOutsTaken=0
totalAtBats=0

def atBat(n,probs):
    global singlesHit,doublesHit,triplesHit,homersHit,walksTaken,strikeOutsTaken,fieldOutsTaken,totalAtBats
    for i in range(n):
        totalAtBats+=1
        options=['Single','Double','Triple','Home Run!!!', 'Walk', 'Strike Out', 'Field Out']
        choice=random.choices(options,probs)[0]
        if choice=='Single':
            singlesHit+=1
        elif choice=='Double':
            doublesHit+=1
        elif choice=='Triple':
            triplesHit+=1
        elif choice=='Home Run!!!':
            homersHit+=1
        elif choice=='Walk':
            walksTaken+=1
        elif choice=='Strike Out':
            strikeOutsTaken+=1
        elif choice=='Field Out':
            fieldOutsTaken+=1
    return choice
           
    
    #return choice

#takes care of the bases
def run(n):
    global bases
    if n=='Single':
        for i in range(len(bases)-1):
            if bases[3-i-1]==1:
                bases[3-i]+=1
                bases[3-i-1]=0
        bases[0]=1
    elif n=='Double':
        if bases[2]==1:
            bases[3]+=1
            bases[2]=0
        for i in range(len(bases)-2):
            if bases[3-i-2]==1:
                bases[3-i]+=1
                bases[3-i-2]=0
        bases[1]=1
    elif n=='Triple':
        if bases[0]==1:
            bases[3]+=1
            bases[0]=0
        if bases[1]==1:
            bases[3]+=1
            bases[1]=0
        if bases[2]==1:
            bases[3]+=1
            bases[2]=0
        bases[2]=1
    elif n=='Home Run':
        bases[3]+=1
        if bases[0]==1:
            bases[3]+=1
            bases[0]=0
        if bases[1]==1:
            bases[3]+=1
            bases[1]=0
        if bases[2]==1:
            bases[3]+=1
            bases[2]=0
    elif n=='Walk':
        if bases[0]==0: #if first base empty
            bases[0]=1 #occupy just first base
        elif bases[0]==1: #else if runner on first
            if bases[1]==0: #if second base empty
                bases[1]=1
            else: #if second base not empty
                if bases[2]==0: #if third base empty
                    bases[2]=1
                else: #if third base not empty
                    bases[3]=1 #send a guy home 
    runs=bases[3]
    bases[3]=0
    return runs
              
def calcSlug(first,second,third,homers,ab):
    return((first+second*2+third*3+homers*4)/ab)

 #pitches=['Sweeper','4-Seam','Split','Cutter','Curveball','Sinker','Slider']
 #probs=[.374,.273,.119,.89,.85,.37,.24]
 #whiff=[.381,.203,.497,.232,.418,.270,.385] #swinging strike percentage
r'''
pitchLoc=['Ball','Ball Top Left', 'Ball Top Right', 'Ball Bottom Left', 'Ball Bottom Right',  #first ball is outside of data zone, automatically count as ball
           'Strike Top Left','Strike Top Middle','Strike Top Right','Strike Middle Left','Strike Middle Middle', 'Strike Middle Right',
           'Strike Bottom Left','Strike Bottom Middle','Strike Bottom Right']
'''
#percent of times pitch thrown here (starting with balls, and then strikes, (left to right))
pitchLocPercent=[.002,.004,.018,.018,.029,.008,.033,.027,.027,.055,.011,.065,.057,.048,.018,.004, #BALLS
                 .025,.048,.049,.075,.11,.068,.079,.081,.041] #STRIKES
#how often batter will swing at pitcher's pitch
pitchLocSwingPercentPitcher=[.0001,.5,.4,.18,.02,.22,.12,.32,.21,.3,.38,.14,.32,.44,.46,.33, #BALLS
                             .71,.77,.49,.69,.79,.57,.54,.62,.45] #STRIKES
#how often Shohei swings
pitchLocSwingPercentBatter=[.02,.22,.41,.44,.08,.05,.43,.2,.44,.24,.38,.13,.34,.38,.38,.09, #BALLS
                            .52,.81,.88,.59,.8,.83,.49,.67,.59] #STRIKES
#how often AVERAGE PLAYER swings
pitchLocSwingPercentAvgBatter=[.055,.3225,.3325,.045,.175,.1525,.23,.2075,.195,.475,.45,.19,.105,.22,.2075,.1, #BALLS
                                .66,.735,.645,.6775,.74,.6575,.6325,.69,.615] #STRIKES
#how often batter will make contact if swings at pitcher's pitch
pitchLocContactPercentPitcher=[.005,.56,.42,.77,.005,.71,.995,.58,.71,.27,.59,.05,.18,.33,.35,.33, #BALLS
                               .73,.71,.76,.79,.88,.85,.66,.84,.78] #STRIKES
#how often Shohei makes contact (if swings)
pitchLocContactPercentBatter=[.5,.76,.7,.38,.33,.67,.9,.88,.76,.7,.5,.22,.48,.55,.3,.005, #BALLS
                              .81,.75,.78,.83,.87,.84,.8,.74,.75] #STRIKES
#how often pitch (not swung at) will be called a strike by the UMP
pitchLocCalledStrikePercent=[.005,.005,.05,.01,.005,.03,.005,.03,.03,.01,.04,.005,.04,.07,.06,.005, #BALLS
                     .55,.86,.56,.84,.995,.83,.67,.93,.75] #STRIKES

#probs=[single, double, triple, home run,foul tip,foul ball,field out] TODO: ball in play, foul, single/double/triple but some else gets out
resultProb=[
    #BALLS
    [7/96,4/96,1/960,1/960,5/96,41/96,39/96,3/57,3/57], #loc 1
    [7/96,4/96,1/960,1/960,5/96,41/96,39/96,3/57,3/57], #loc 2
    [7/96,4/96,1/960,1/960,5/96,41/96,39/96,3/57,3/57], #loc 3
    [7/119,2/119,1/1190,2/119,1/119,46/119,61/119,3/57,3/57], #loc 4
    [7/119,2/119,1/1190,2/119,1/119,46/119,61/119],3/57,3/57, #loc 5
    [7/96,4/96,1/960,1/960,5/96,41/96,39/96,3/57,3/57], #loc 6
    [7/119,2/119,1/1190,2/119,1/119,46/119,61/119,3/57,3/57], #loc 7
    [7/96,4/96,1/960,1/960,5/96,41/96,39/96,3/57,3/57], #loc 8
    [7/119,2/119,1/1190,2/119,1/119,46/119,61/119],3/57,3/57, #loc 9
    [17/238,1/238,1/2380,1/2380,1/238,53/238,166/238,3/57,3/57], #loc 10
    [7/168,1/1680,1/1680,5/168,4/168,49/168,103/68,3/57,3/57], #loc 11
    [17/238,1/238,1/2380,1/2380,1/238,53/238,166/238,3/57,3/57], #loc 12
    [17/238,1/238,1/2380,1/2380,1/238,53/238,166/238,3/57,3/57], #loc 13
    [17/238,1/238,1/2380,1/2380,1/238,53/238,166/238,3/57,3/57], #loc 14
    [7/168,1/1680,1/1680,5/168,4/168,49/168,108/168,3/57,3/57], #loc 15
    [7/168,1/1680,1/1680,5/168,4/168,49/168,108/168,3/57,3/57], #loc 16
    #STRIKES
    [8/86,3/86,1/86,3/86,1/86,32/86,38/86,3/57,3/57], #loc 17
    [8/140,4/140,2/140,9/140,4/140,62/140,55/140,3/57,3/57], #loc 18
    [7/117,2/117,1/117,4/117,5/117,44/117,54/117,3/57,3/57], #loc 19
    [10/183,9/183,2/183,2/183,10/183,69/183,80/183,3/57,3/57], #loc 20
    [15/218,4/218,1/2180,15/218,8/218,91/218,85/218,3/57,3/57], #loc 21
    [13/166,7/166,3/166,6/166,2/166,73/166,62/166,3/57,3/57], #loc 22
    [29/161,3/161,1/161,5/161,4/161,48/161,71/161,3/57,3/57], #loc 23
    [12/178,5/178,1/178,7/178,4/178,69/178,80/178,3/57,3/57], #loc 24
    [8/82,1/82,1/820,4/82,1/82,36/82,32/82,3/57,3/57] #loc 25
    ]

mikeTroutSwingPercent=[.0001,.5,.4,.18,.02,.22,.12,.32,.21,.3,.38,.14,.32,.44,.46,.33, #BALLS
                             .71,.77,.49,.69,.79,.57,.54,.62,.45] #STRIKES
def pitch():
    strikes=0
    balls=0
    while True:
        options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, #BALLS
             17,18,19,20,21,22,23,24,25] #STRIKES
        #where pitch will be located
        location=random.choices(options,pitchLocPercent)[0]-1
        # % a swing will occur based on location
        swingChance=(3*pitchLocSwingPercentBatter[location]+pitchLocSwingPercentPitcher[location])/4
        swingHappens=random.choices([0,1],[1-swingChance,swingChance])[0]
        if swingHappens:
            contactChance=(3*pitchLocContactPercentBatter[location]+pitchLocContactPercentPitcher[location])/4
            contactHappens=random.choices([0,1],[1-contactChance,contactChance])[0]
            if contactHappens:
                contactResult=random.choices(['Single','Double','Triple','Home Run','Foul Tip','Foul Ball','Field Out'], resultProb[location])[0]
                if contactResult=='Foul Tip':
                    if strikes<2: #if doesn't result in an out
                        strikes+=1
                    else: #batter makes a run for it
                        pass #TODO: calculate odds of making it
                elif contactResult=='Foul Ball':
                    #TODO: calculate odds of it being out
                    if strikes<2: #count as strike unless already 2 strikes
                        strikes+=1
                    else:
                        pass 
                else: #single, double, triple, homer, field out
                    return contactResult
                r'''
                elif contactResult=='Field Out':
                    return 'Field Out'
                else: #if a hit
                    run(contactResult)
                    return 0
                '''
            else: #no contact happens, but a swing does
                strikes+=1
        else: #no swing happens
            calledStrikeChance=pitchLocCalledStrikePercent[location]
            calledStrike=random.choices([0,1],[1-calledStrikeChance,calledStrikeChance])[0]
            if calledStrike:
                strikes+=1
            else:
                balls+=1
        print(balls,'-',strikes)
        if strikes==3:
            return 'Strike Out'
        elif balls==4:
            return 'Walk'
        

def game(n):
    innings=0
    homeBatters=0
    awayBatters=0
    homeRuns=0
    awayRuns=0
    homeHits=0
    awayHits=0
    homeWalks=0
    homeSingles=0
    homeDoubles=0
    homeTriples=0
    homeHomers=0
    awayWalks=0
    awaySingles=0
    awayDoubles=0
    awayTriples=0
    awayHomers=0
    homeWins=0
    awayWins=0
    homeWinsProbs=[]
    totGames=[]
    totHomePitchCount=0
    totAwayPitchCount=0
    for i in range(n):
        global home,away,outs,bases
        away=0
        home=0
        awayPitchCount=0
        awayPitcherStrikeOut=0
        homePitchCount=0
        homePitcherStrikeOut=0
    
        for inning in range(9):
            innings+=1
            inning=inning+1
            outs=0
            bases=[0,0,0,0]
        
            #Away team @ bat
            print('AWAY TEAM AT BAT')
            print()
            while outs<3:
               print('0 - 0')
               result=pitch()
               homePitchCount+=1
               print(result)
               if result=='Field Out':
                   awayBatters+=1
                   if bases[1]==1: #if person on first already
                       doublePlay=random.choices([0,1],[1-0.045,0.045])
                       if doublePlay and outs<2:
                           print('Double Play!!!')
                           outs+=2
                       else:
                           outs+=1
                   else:
                       outs+=1
               elif result=='Walk':
                   awayBatters+=1
                   away+=run('Walk')
                   awayWalks+=1
               elif result=='Single':
                   awayBatters+=1
                   away+=run('Single')
                   awaySingles+=1
                   awayHits+=1
               elif result=='Double':
                   awayBatters+=1
                   away+=run('Double')
                   awayDoubles+=1
                   awayHits+=1
               elif result=='Triple':
                   awayBatters+=1
                   away+=run('Triple')
                   awayTriples+=1
                   awayHits+=1
               elif result=='Home Run':
                   awayBatters+=1
                   away+=run('Home Run')
                   awayHomers+=1
                   awayHits+=1
               elif result=='Strike Out':
                   awayBatters+=1
                   homePitcherStrikeOut+=1
                   outs+=1
               print()
            
           
            outs=0
            bases=[0,0,0,0]
            print()
            print('Middle of inning ',inning,' Home: ',home,' Away: ',away)
            print()
            #Home team @ beat
            print('HOME TEAM AT BAT')
            print()
            while outs<3:
               print('0 - 0')
               result=pitch()
               awayPitchCount+=1
               print(result)
               if result=='Field Out':
                   homeBatters+=1
                   if bases[1]==1: #if person on first already
                       doublePlay=random.choices([0,1],[1-0.045,0.045])
                       if doublePlay and outs<2:
                           print('Double Play!!!')
                           outs+=2
                       else:
                           outs+=1
                   else:
                       outs+=1
               elif result=='Walk':
                   homeBatters+=1
                   home+=run('Walk')
                   homeWalks+=1
               elif result=='Single':
                   homeBatters+=1
                   home+=run('Single')
                   homeSingles+=1
                   homeHits+=1
               elif result=='Double':
                   homeBatters+=1
                   home+=run('Double')
                   homeDoubles+=1
                   homeHits+=1
               elif result=='Triple':
                   homeBatters+=1
                   home+=run('Triple')
                   homeTriples+=1
                   homeHits+=1
               elif result=='Home Run':
                   homeBatters+=1
                   home+=run('Home Run')
                   homeHomers+=1
                   homeHits+=1
               elif result=='Strike Out':
                   homeBatters+=1
                   awayPitcherStrikeOut+=1
                   outs+=1
               print()
            print()
            print('End of inning ',inning,' Home: ',home,' Away: ',away)
            print()
        while away==home: #if tie game
            innings+=1
            inning=inning+1
            outs=0
            bases=[0,0,0,0]
            
            #Away team @ bat
            print()
            print('AWAY TEAM AT BAT')
            print()
            while outs<3:
                print('0 - 0')
                result=pitch()
                homePitchCount+=1
                print(result)
                if result=='Field Out':
                    awayBatters+=1
                    if bases[1]==1: #if person on first already
                        doublePlay=random.choices([0,1],[1-0.045,0.045])
                        if doublePlay and outs<2:
                            print('Double Play!!!')
                            outs+=2
                        else:
                            outs+=1
                    else:
                        outs+=1
                elif result=='Walk':
                    awayBatters+=1
                    away+=run('Walk')
                    awayWalks+=1
                elif result=='Single':
                    awayBatters+=1
                    away+=run(1)
                    awaySingles+=1
                    awayHits+=1
                elif result=='Double':
                    awayBatters+=1
                    away+=run(2)
                    awayDoubles+=1
                    awayHits+=1
                elif result=='Triple':
                    awayBatters+=1
                    away+=run(3)
                    awayTriples+=1
                    awayHits+=1
                elif result=='Home Run':
                    awayBatters+=1
                    away+=run(4)
                    awayHomers+=1
                    awayHits+=1
                elif result=='Strike Out':
                    awayBatters+=1
                    outs+=1
                print()
                
               
            outs=0
            bases=[0,0,0,0]
            print()
            print('Middle of inning ',inning,' Home: ',home,' Away: ',away)
            print()
            #Home team @ beat
            print()
            print('HOME TEAM AT BAT')
            print()
            while outs<3:
                print('0 - 0')
                result=pitch()
                awayPitchCount+=1
                print(result)
                if result=='Field Out':
                    homeBatters+=1
                    if bases[1]==1: #if person on first already
                        doublePlay=random.choices([0,1],[1-0.045,0.045])
                        if doublePlay and outs<2:
                            print('Double Play!!!')
                            outs+=2
                        else:
                            outs+=1
                    else:
                        outs+=1
                elif result=='Walk':
                    homeBatters+=1
                    home+=run('Walk')
                    homeWalks+=1
                elif result=='Single':
                    homeBatters+=1
                    home+=run(1)
                    homeSingles+=1
                    homeHits+=1
                elif result=='Double':
                    homeBatters+=1
                    home+=run(2)
                    homeDoubles+=1
                    homeHits+=1
                elif result=='Triple':
                    homeBatters+=1
                    home+=run(3)
                    homeTriples+=1
                    homeHits+=1
                elif result=='Home Run':
                    homeBatters+=1
                    home+=run(4)
                    homeHomers+=1
                    homeHits+=1
                elif result=='Strike Out':
                    homeBatters+=1
                    outs+=1
                print()
            print()
            print('End of inning ',inning,' Home: ',home,' Away: ',away)
            print()
        
        print()
        print('FINAL   Home:', home, ' Away: ',away)
        
        if home>away:
            homeWins+=1
        if away>home:
            awayWins+=1
        homeRuns+=home
        awayRuns+=away
        homeWinsProbs.append(homeWins/(i+1))
        totGames.append(i+1)

        totHomePitchCount+=homePitchCount
        totAwayPitchCount+=awayPitchCount
    
    #Plotting win probability by trial
    plt.plot(totGames, homeWinsProbs)
    plt.title('Home Win Probability')
    plt.xlabel('Number of Games')
    plt.ylabel('Win Percentage')
    print(homeWins)
    print(awayWins)
    plt.axhline(y=0.5)#Add horizontal line at 0.5
    plt.show()
    
    #Pitch Counts
    plt.bar(['Home Pitch Count', 'Away Pitch Count'],
             [totHomePitchCount,totAwayPitchCount])
    plt.show()
    print('Home ERA: ',homeRuns/innings)
    print('Home Batting Average: ',homeHits/homeBatters)
    print('Home Slugging: ',(homeSingles+2*homeDoubles+3*homeTriples+4*homeHomers)/homeBatters)
    print('Home On-Base %: ',(homeHits+homeWalks)/homeBatters)
    print('Home OPS: ',(homeBatters*(homeHits+homeWalks) + (homeSingles+2*homeDoubles+3*homeTriples+4*homeHomers)*(homeBatters+homeWalks))/(homeBatters*(homeBatters+homeWalks)) )
    print('Away ERA: ',awayRuns/innings)
    print('Away Batting Average: ',awayHits/awayBatters)
    print('Away Slugging: ',(awaySingles+2*awayDoubles+3*awayTriples+4*awayHomers)/awayBatters)
    print('Away On-Base %: ',(awayHits+awayWalks)/awayBatters)
    print('Away OPS: ',(awayBatters*(awayHits+awayWalks) + (awaySingles+2*awayDoubles+3*awayTriples+4*awayHomers)*(awayBatters+awayWalks))/(awayBatters*(awayBatters+awayWalks)) )




