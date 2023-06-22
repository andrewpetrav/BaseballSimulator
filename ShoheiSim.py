import pandas as pd
import random 

season_league_totals={'AB':163465, 'H':39675,'1B':25877,'2B':7940, '3B':643, 'HR':5215, 'BB':14853, 'SO': 40812}
avg_player={'1B%':season_league_totals['1B']/season_league_totals['AB'], '2B%':season_league_totals['2B']/season_league_totals['AB'], 
     '3B%':season_league_totals['3B']/season_league_totals['AB'],'HR%':season_league_totals['HR']/season_league_totals['AB'], 
     'BB%':season_league_totals['BB']/season_league_totals['AB'], 'SO%':season_league_totals['SO']/season_league_totals['AB'],
     'OUT%':(season_league_totals['AB']-season_league_totals['H']-season_league_totals['BB']-season_league_totals['SO'])/season_league_totals['AB']}

Obat=pd.read_csv('OhtaniBatting.txt')
Opitch=pd.read_csv('OhtaniPitching.txt')

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
    
oneBb=Hb-twoBb-threeBb-HRb
oneBp=Hp-twoBp-threeBp-HRp

OhtaniBatting={'1B%':oneBb/ABb, '2B%':twoBb/ABb, '3B%':threeBb/ABb,'HR%':HRb/ABb,'BB%':BBb/ABb, 'SO%':SOb/ABb, 'OUT%':(ABb-Hb-BBb-SOb)/ABb}
OhtaniPitching={'1B%':oneBp/ABp, '2B%':twoBp/ABp, '3B%':threeBp/ABp,'HR%':HRp/ABp,'BB%':BBp/ABp, 'SO%':SOp/ABp, 'OUT%':(ABp-Hp-BBp-SOp)/ABp}

#print(avg_player)
#print(OhtaniBatting)
#print(OhtaniPitching)

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

#print(OBvNA)
#print(OPvNA)
#print(OvNAA)
#print(E)

ABprobs=[E['1B%'], E['2B%'], E['3B%'], E['HR%'], E['BB%'], E['SO%'], E['OUT%']]

def atBat():
    options=['Single','Double','Triple','Home Run!!!', 'Walk', 'Strike Out', 'Field Out']
    choice=random.choices(options,ABprobs)
    print(choice)

def game():
    away=0
    home=0
    for inning in range(9):
        inning=inning+1
        outs=0
        first=0
        second=0
        third=0
        #Away team @ bat
        for outs in range(3):
            result=atBat()
        #Home team @ beat
        for outs in 



