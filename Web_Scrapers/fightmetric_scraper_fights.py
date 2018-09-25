from bs4 import BeautifulSoup as bsoup
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
from time import sleep



url_overall=[]
url_base='http://www.fightmetric.com/statistics/fighters'
url_chunk=['?char=a&page=all', '?char=b&page=all', '?char=c&page=all', '?char=d&page=all',
           '?char=e&page=all', '?char=f&page=all', '?char=g&page=all', '?char=h&page=all',
           '?char=i&page=all', '?char=j&page=all', '?char=k&page=all', '?char=l&page=all',
           '?char=m&page=all', '?char=n&page=all', '?char=o&page=all', '?char=p&page=all',
           '?char=q&page=all', '?char=r&page=all', '?char=s&page=all', '?char=t&page=all',
           '?char=u&page=all', '?char=v&page=all', '?char=w&page=all', '?char=x&page=all',
           '?char=y&page=all', '?char=z&page=all']


final_fighter_urls=[]
for i in url_chunk:
    x=url_base+i
    url_overall.append(x)
for x in url_overall:
    response=requests.get(x)
    print(response.status_code)
    data=response.text
    soup=bsoup(data)
    fighter_urls=[]
    for link in soup.find_all('a'):
        fighter_urls.append(link.get('href'))
    for fighter in fighter_urls:
        if fighter in final_fighter_urls:
            pass
        elif fighter is None:
            pass
        elif 'fighter-details' in fighter:
            final_fighter_urls.append(fighter)
total_fights_urls = []            
name_record=[]
stats=[]
for i in final_fighter_urls:
    response_1=requests.get(i)
    print(response.status_code)
    data_1=response_1.text
    soup_1=bsoup(data_1)
    urls = []
    for link in soup_1.find_all('a'):
        urls.append(link.get('href'))
    for details in urls:
        if details in total_fights_urls:
            pass
        elif details is None:
            pass
        elif 'fight-details' in details:
            total_fights_urls.append(details)
df1 = pd.DataFrame(data = total_fights_urls)
df1.to_csv('AllFightUrls.csv')  


fighters = []
winlossorder = []
Overall_Detail = []
KD = []
SigStr = []
SigStrPer = []
TotalStr = []
TD = []
TDPer = []
SubAtt = []
Pass = []
Rev = []
SigStrHead = []
SigStrBody = []
SigStrLeg = []
SigStrDis = []
SigStrClinch = []
SigStrGround = []
for i in total_fights_urls:
    response_2 = requests.get(i)
    print(response.status_code)
    data_2 = response_2.text
    soup_2 = bsoup(data_2)
    i_s = []  #give you Win and Loss and Stat Box Under, Plus the entire bottom panel
    spans = [] #give you fighter names (first is the winner second is the loser)
    p_s = []
    th = []
    for link in soup_2.find_all('i'):
        i_s.append(link.get_text())
    for link in soup_2.find_all('span'):
        spans.append(link.get_text())
    for link in soup_2.find_all('p'):
        p_s.append(link.get_text())
    if len(spans) > 6:    
        winlossorder.append((i_s[12], i_s[13]))
        fighters.append((p_s[5], p_s[6]))
        Overall_Detail.append((p_s[2], p_s[3]))
        KD.append((p_s[7], p_s[8]))
        SigStr.append((p_s[9], p_s[10]))
        SigStrPer.append((p_s[11], p_s[12]))
        TotalStr.append((p_s[13], p_s[14]))
        TD.append((p_s[15], p_s[16]))
        TDPer.append((p_s[17], p_s[18]))
        SubAtt.append((p_s[19], p_s[20]))
        Pass.append((p_s[21], p_s[22]))
        Rev.append((p_s[23], p_s[24]))
    for p in p_s:
        count = 0
        if 'Significant Strikes' in p:
            SigStrHead.append((p_s[count+7], p_s[count+8]))
            SigStrBody.append((p_s[count+9], p_s[count+10]))
            SigStrLeg.append((p_s[count+11], p_s[count+12]))
            SigStrDis.append((p_s[count+13], p_s[count+14]))
            SigStrClinch.append((p_s[count+15], p_s[count+16]))
            SigStrGround.append((p_s[count+17], p_s[count+18]))
        count = count+1

df = pd.DataFrame(data = {'Fighters': fighters, 'WinLossOrder': winlossorder,
                          'Overall_Details': Overall_Detail, 'KD': KD,
                          'SigStr': SigStr, 'SigStrPer': SigStrPer,
                          'TotalStr': TotalStr, 'TD': TD, 'TDPer': TDPer,
                          'SubAtt': SubAtt, 'Pass': Pass, 'Rev': Rev,
                          'SigStrHead': SigStrHead, 'SigStrBody': SigStrBody, 
                          'SigStrLeg': SigStrLeg, 'SigStrDis': SigStrDis,
                          'SigStrClinch': SigStrClinch, 'SigStrGround': SigStrGround})   
        
df.to_csv('All_fights_fighters.csv')