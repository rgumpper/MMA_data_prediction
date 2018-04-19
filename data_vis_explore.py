# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:22:38 2018

@author: Ryan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import file
df=pd.read_csv('FightMetric_clean.csv')
#reset index
df=df.set_index('Fighter Name')

#separate Fighters by stance of win percent
orthodox=df[df['Fighter Stance']=='Orthodox'] 
southpaw=df[df['Fighter Stance']=='Southpaw']
switch=df[df['Fighter Stance']=='Switch']
#plot histogram for all stances
orthodox['win percent'].plot(kind='hist', bins=50, alpha=0.5, color='blue')
southpaw['win percent'].plot(kind='hist', bins=50, alpha=0.5, color='green')
switch['win percent'].plot(kind='hist', bins=50, alpha=0.5, color='red')
plt.legend(['Orthodox', 'Southpaw', 'Switch'])
plt.title('Histogram of Win Percentage by Stance')
plt.xlabel('win percentage')
plt.ylabel('frequency')
plt.show()
#boxplot by stance of win percent
plt.boxplot([orthodox['win percent'], southpaw['win percent'], switch['win percent']])
plt.title('Box Plot of Win Percentage by Stance')
plt.ylabel('Win Percentage')
plt.xticks([1,2,3], ['Orthodox', 'Southpaw', 'Switch'])
plt.show()

#boxplot by stance of SLpM, SApM, Stricking Accuracy, Stricking Defence
fig, axs=plt.subplots(4,3)

axs[0,0].boxplot(orthodox['Fighter SLpM'], 0, '')
axs[0,0].set_title('Orthodox')
axs[0,0].set_ylabel('SLpM')

axs[0,1].boxplot(southpaw['Fighter SLpM'], 0, '')
axs[0,1].set_title('Southpaw')

axs[0,2].boxplot(switch['Fighter SLpM'], 0, '')
axs[0,2].set_title('Switch')



axs[1,0].boxplot(orthodox['Fighter SApM'], 0, '')
axs[1,0].set_ylabel('SApM')

axs[1,1].boxplot(southpaw['Fighter SApM'], 0, '')


axs[1,2].boxplot(switch['Fighter SApM'], 0, '')


axs[2,0].boxplot(orthodox['Fighter Striking Accuracy'], 0, '')
axs[2,0].set_ylabel('Striking Accuracy')

axs[2,1].boxplot(southpaw['Fighter Striking Accuracy'], 0, '')


axs[2,2].boxplot(switch['Fighter Striking Accuracy'], 0, '')


axs[3,0].boxplot(orthodox['Fighter Striking Defence'], 0, '')
axs[3,0].set_ylabel('Striking Defence')

axs[3,1].boxplot(southpaw['Fighter Striking Defence'], 0, '')


axs[3,2].boxplot(switch['Fighter Striking Defence'], 0, '')


plt.show()



#for PCA analysis 
noBD=['Fighter Height', 'Fighter Weight', 'Fighter Reach', 'Fighter SLpM', 'Fighter Striking Accuracy',
      'Fighter SApM', 'Fighter Striking Defence', 'Fighter Take Down Average', 'Fighter Take Down Accuracy', 
      'Fighter Take Down Defence', 'Fighter Submission Average', 'wins', 'loss', 'total', 'tie', 'win percent']
orthodox=orthodox[noBD]
southpaw=southpaw[noBD]
switch=switch[noBD]

from sklearn.preprocessing import StandardScaler
orthodox=StandardScaler().fit_transform(orthodox)
southpaw=StandardScaler().fit_transform(southpaw)
switch=StandardScaler().fit_transform(switch)

from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca = sklearnPCA(n_components=2)
Y_sklearn_orthodox = sklearn_pca.fit_transform(orthodox)
Y_sklearn_southpaw = sklearn_pca.fit_transform(southpaw)
Y_sklearn_switch = sklearn_pca.fit_transform(switch)


plt.figure('PCA of Different Stances')
plt.scatter(Y_sklearn_orthodox[:,0], Y_sklearn_orthodox[:,1], color='red', alpha=0.5)
plt.scatter(Y_sklearn_southpaw[:,0], Y_sklearn_southpaw[:,1], color='blue', alpha=0.5)
plt.scatter(Y_sklearn_switch[:,0], Y_sklearn_switch[:,1], color='green', alpha=0.5)
plt.title('PCA of Different Stances')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.show()








