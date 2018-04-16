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
name_record=[]
stats=[]
final_fighter_urls1=final_fighter_urls[2750:]
for i in final_fighter_urls1:
    response_1=requests.get(i)
    print(response.status_code)
    data_1=response_1.text
    soup_1=bsoup(data_1)
    combined1=[]
    combined1_1=[]
    combined3=[]
    for link in soup_1.find_all('span'):
        combined1.append(link.get_text())
    for link in soup_1.find_all('li'):
        combined3.append(link.get_text())
    for y in combined1:
        y= y.strip()
        combined1_1.append(y)
    combined3=combined3[8:22]
    combined3_1=[]
    for y in combined3:
        y=y.strip()
        combined3_1.append(y)
    combined3_2=[]
    for y in combined3_1:
        y=y.replace(' ', '')
        combined3_2.append(y)
    name_record.append(combined1_1)
    stats.append(combined3_2)
    sleep(30)

fighter_names=[]
fighter_records=[]
fighter_height=[]
fighter_weight=[]
fighter_reach=[]
fighter_stance=[]
fighter_DOB=[]
fighter_slpm=[]
fighter_stracc=[]
fighter_sapm=[]
fighter_strdef=[]
fighter_tdavg=[]
fighter_tdacc=[]
fighter_tddef=[]
fighter_subavg=[]


for i in name_record:
    fighter_names.append(i[0])
    fighter_records.append(i[1])
    
fighter_records_final=[]
for i in fighter_records:
    i=i.replace('Record: ','')
    fighter_records_final.append(i)
    
for i in stats:
    for y in i:
        if 'Height' in y:
            y=y.replace('Height:','')
            y=y.strip()
            fighter_height.append(y)
        elif 'Weight' in y:
            y=y.replace('Weight:','')
            y=y.strip()
            fighter_weight.append(y)
        elif 'Reach' in y:
            y=y.replace('Reach:','')
            y=y.strip()
            fighter_reach.append(y)
        elif 'STANCE' in y:
            y=y.replace('STANCE:','')
            y=y.strip()
            fighter_stance.append(y)
        elif 'DOB' in y:
            y=y.replace('DOB:','')
            y=y.strip()
            fighter_DOB.append(y)
        elif 'SLpM' in y:
            y=y.replace('SLpM:','')
            y=y.strip()
            fighter_slpm.append(y)
        elif 'Str.Acc.' in y:
            y=y.replace('Str.Acc.:', '')
            y=y.strip()
            fighter_stracc.append(y)
        elif 'SApM' in y:
            y=y.replace('SApM:', '')
            y=y.strip()
            fighter_sapm.append(y)
        elif 'Str.Def' in y:
            y=y.replace('Str.Def:','')
            y=y.strip()
            fighter_strdef.append(y)
        elif 'TDAvg' in y:
            y=y.replace('TDAvg.:','')
            y=y.strip()
            fighter_tdavg.append(y)
        elif 'TDAcc' in y:
            y=y.replace('TDAcc.:','')
            y=y.strip()
            fighter_tdacc.append(y)
        elif 'TDDef' in y:
            y=y.replace('TDDef.:','')
            y=y.strip()
            fighter_tddef.append(y)
        elif 'Sub.Avg' in y:
            y=y.replace('Sub.Avg.:','')
            y=y.strip()
            fighter_subavg.append(y)
            
df=pd.DataFrame(np.column_stack([fighter_names, fighter_records_final, fighter_height, fighter_weight,
                                 fighter_reach, fighter_stance, fighter_DOB, fighter_slpm, fighter_stracc,
                                 fighter_sapm, fighter_strdef, fighter_tdavg, fighter_tdacc, 
                                 fighter_tddef, fighter_subavg]), columns=['Fighter Name', 'Fighter Record',
                                'Fighter Height', 'Fighter Weight', 'Fighter Reach', 'Fighter Stance',
                                'Fighter DOB', 'Fighter SLpM', 'Fighter Striking Accuracy', 'Fighter SApM', 
                                'Fighter Striking Defence', 'Fighter Take Down Average', 'Fighter Take Down Accuracy',
                                'Fighter Take Down Defence', 'Fighter Submission Average'])
df.to_csv('FightMetricsData.csv')
            
    
        
                    

            

            
        
            
        