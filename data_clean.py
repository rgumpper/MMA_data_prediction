# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 11:24:01 2018

@author: Ryan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_pickle('FightMetricsData.pkl')

df=df.replace('--', np.nan)
df=df.replace('', np.nan)

df=df.dropna(axis=0, how='any')

df.set_index('Fighter Name', inplace=True)
#conversion of height to inches and integer
df['Fighter Height']=df['Fighter Height'].str.split("'")
tup_heights=[]
for x, y in df['Fighter Height']:
    new=[]
    y=y.replace('"','')
    new.append(x)
    new.append(y)
    tup_heights.append(new)
heights=[]    
for x in tup_heights:
    ft_in=(int(x[0])*12)+int(x[1])
    heights.append(ft_in)
    
df['Fighter Height']=heights

#conversion of weight to numeric
df['Fighter Weight']=df['Fighter Weight'].str.replace('lbs.','')
df['Fighter Weight']=pd.to_numeric(df['Fighter Weight'])

#conversion reach to numeric
df['Fighter Reach']=df['Fighter Reach'].str.replace('"','')
df['Fighter Reach']=pd.to_numeric(df['Fighter Reach'])
#for most columns to numeric
cols=['Fighter SLpM', 'Fighter SApM', 'Fighter Take Down Average', 'Fighter Submission Average']
df[cols]=df[cols].apply(pd.to_numeric, errors='coerce', axis=1)

#for percentage columns to be replaced
cols1=['Fighter Striking Accuracy', 'Fighter Striking Defence', 'Fighter Take Down Accuracy', 'Fighter Take Down Defence']
for i in cols1:
    df[i]=df[i].str.replace('%','')

df[cols1]=df[cols1].apply(pd.to_numeric, errors='coerce', axis=1)


#DOB to a date-time still need to do
df['Fighter DOB']=pd.to_datetime(df['Fighter DOB'])


#for converting the record into a win, loss, tie, and nc columm
df['Fighter Record']=df['Fighter Record'].str.split('-') 
win=[]
loss=[]
tie=[]
nc=[]
for x, y, z in df['Fighter Record']:
    win.append(x)
    loss.append(y)
    tie.append(z[0])
df['wins']=win
df['loss']=loss
df['tie']=tie

cols2=['wins', 'loss', 'tie']
df[cols2]=df[cols2].apply(pd.to_numeric, errors='coerce', axis=1)

df.to_csv('FightMetric_clean_recordintact.csv')

df=df.drop('Fighter Record', axis=1)

df.to_csv('FightMetric_clean.csv')

df.plot(kind='hist', bins=100, subplots=True, layout=(4,4))
plt.show()
df.plot(kind='box', subplots=True, layout=(4,4))
plt.show()


plt.scatter(df['Fighter SLpM'], df['Fighter SApM'])
plt.title('SApM vs SLpM')
plt.xlabel('SLpM')
plt.ylabel('SApM')
plt.show()

df['total']=df['wins']+df['loss']+df['tie']
df['win percent']=df['wins']/df['total']
       
df['win percent'].plot(kind='hist', bins=100, alpha=0.5, color='red')
plt.title('Histogram of Win Percentage')
plt.xlabel('win percentage')
plt.ylabel('frequency') 
plt.show() 

