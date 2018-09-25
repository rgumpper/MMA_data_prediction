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
axs[0,0].set_ylim(-0.5, 6.5)

axs[0,1].boxplot(southpaw['Fighter SLpM'], 0, '')
axs[0,1].set_title('Southpaw')
axs[0,1].set_ylim(-0.5, 6.5)

axs[0,2].boxplot(switch['Fighter SLpM'], 0, '')
axs[0,2].set_title('Switch')
axs[0,2].set_ylim(-0.5, 6.5)



axs[1,0].boxplot(orthodox['Fighter SApM'], 0, '')
axs[1,0].set_ylabel('SApM')
axs[1,0].set_ylim(-0.5, 6.5)

axs[1,1].boxplot(southpaw['Fighter SApM'], 0, '')
axs[1,1].set_ylim(-0.5, 6.5)

axs[1,2].boxplot(switch['Fighter SApM'], 0, '')
axs[1,2].set_ylim(-0.5, 6.5)


axs[2,0].boxplot(orthodox['Fighter Striking Accuracy'], 0, '')
axs[2,0].set_ylabel('Striking Accuracy')
axs[2,0].set_ylim(15, 70)

axs[2,1].boxplot(southpaw['Fighter Striking Accuracy'], 0, '')
axs[2,1].set_ylim(15, 70)

axs[2,2].boxplot(switch['Fighter Striking Accuracy'], 0, '')
axs[2,2].set_ylim(15, 70)


axs[3,0].boxplot(orthodox['Fighter Striking Defence'], 0, '')
axs[3,0].set_ylabel('Striking Defence')
axs[3,0].set_ylim(25, 85)

axs[3,1].boxplot(southpaw['Fighter Striking Defence'], 0, '')
axs[3,1].set_ylim(25, 85)

axs[3,2].boxplot(switch['Fighter Striking Defence'], 0, '')
axs[3,2].set_ylim(25, 85)


plt.show()



#for PCA analysis 
noBD=['Fighter Height', 'Fighter Weight', 'Fighter Reach', 'Fighter SLpM', 'Fighter Striking Accuracy',
      'Fighter SApM', 'Fighter Striking Defence', 'Fighter Take Down Average', 'Fighter Take Down Accuracy', 
      'Fighter Take Down Defence', 'Fighter Submission Average', 'wins', 'loss', 'total', 'tie', 'win percent']
orthodox=orthodox[noBD]
southpaw=southpaw[noBD]
switch=switch[noBD]

dfnoBD = df[noBD]

#standardization of data for PCA
from sklearn.preprocessing import StandardScaler
orthodox_std=StandardScaler().fit_transform(orthodox)
southpaw_std=StandardScaler().fit_transform(southpaw)
switch_std=StandardScaler().fit_transform(switch)
dfnoBD_std = StandardScaler().fit_transform(dfnoBD)
#PCA analysis
from sklearn.decomposition import PCA as pca
sklearn_pca = sklearnPCA(n_components=2)
Y_sklearn_orthodox = sklearn_pca.fit_transform(orthodox_std)
Y_sklearn_southpaw = sklearn_pca.fit_transform(southpaw_std)
Y_sklearn_switch = sklearn_pca.fit_transform(switch_std)

pc = pca(n_components = 0.95, svd_solver = 'full')
pca_dfnoBD_std = pc.fit_transform(dfnoBD_std)

variance = pc.explained_variance_ratio_






#plot each PCA
plt.figure('PCA of Different Stances')
plt.scatter(Y_sklearn_orthodox[:,0], Y_sklearn_orthodox[:,1], color='red', alpha=0.5)
plt.scatter(Y_sklearn_southpaw[:,0], Y_sklearn_southpaw[:,1], color='blue', alpha=0.5)
plt.scatter(Y_sklearn_switch[:,0], Y_sklearn_switch[:,1], color='green', alpha=0.5)
plt.title('PCA of Different Stances')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.show()
#look at 3 dimension PCA
from mpl_toolkits.mplot3d import Axes3D
sklearn_pca_3d = sklearnPCA(n_components=3)
Y_sklearn_orthodox_3 = sklearn_pca_3d.fit_transform(orthodox_std)
Y_sklearn_southpaw_3 = sklearn_pca_3d.fit_transform(southpaw_std)
Y_sklearn_switch_3 = sklearn_pca_3d.fit_transform(switch_std)

fig = plt.figure(1, figsize=(4, 3))
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
plt.figure('PCA of Different Stances')
ax.scatter(Y_sklearn_orthodox_3[:,0], Y_sklearn_orthodox_3[:,1], Y_sklearn_orthodox_3[:,2], color='red', alpha=0.5)
ax.scatter(Y_sklearn_southpaw_3[:,0], Y_sklearn_southpaw_3[:,1], Y_sklearn_southpaw_3[:,2], color='blue', alpha=0.5)
ax.scatter(Y_sklearn_switch_3[:,0], Y_sklearn_switch_3[:,1], Y_sklearn_switch_3[:,1], color='green', alpha=0.5)


#for random forest for predicting wins percent
from sklearn.ensemble import RandomForestClassifier
rf_df=['Fighter Height', 'Fighter Weight', 'Fighter Reach', 'Fighter SLpM', 'Fighter Striking Accuracy',
      'Fighter SApM', 'Fighter Striking Defence', 'Fighter Take Down Average', 'Fighter Take Down Accuracy', 
      'Fighter Take Down Defence', 'Fighter Submission Average', 'wins']
orthodox_rf=orthodox[rf_df]
southpaw_rf=southpaw[rf_df]
switch_rf=switch[rf_df]

df_rf=df[rf_df]

df_rf['is_train'] = np.random.uniform(0, 1, len(df_rf)) <= .75

train, test = df_rf[df_rf['is_train']==True], df_rf[df_rf['is_train']==False]
features=['Fighter Height', 'Fighter Weight', 'Fighter Reach', 'Fighter SLpM', 'Fighter Striking Accuracy',
      'Fighter SApM', 'Fighter Striking Defence', 'Fighter Take Down Average', 'Fighter Take Down Accuracy', 
      'Fighter Take Down Defence', 'Fighter Submission Average']
clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(train[features], train['wins'])

predicted=clf.predict(test[features])

imp=list(zip(train[features], clf.feature_importances_))

x=[]
for i in range(1,343):
    x.append(i)

plt.figure('Predicted vs Actual Random Forest')
plt.scatter(x, predicted, c='red', alpha=0.5)
plt.scatter(x, test['wins'], c='blue', alpha=0.5)
plt.legend(['Predicted', 'Actual'])
plt.plot(x, predicted, alpha=0.2)
plt.plot(x, test['wins'], alpha=0.2)
plt.xlabel('Fighter Index')
plt.ylabel('Number of Wins')
plt.title('Predicted vs Actual Random Forest')


#Closer to 0 reflects the better predictions
plt.figure('Predicted vs Actual Random Forest_1')
plt.scatter(x, (test['wins']-predicted), c='red', alpha=0.5)
plt.plot(x, (test['wins']-predicted), alpha=0.2)
plt.xlabel('Fighter Index')
plt.ylabel('Difference between Actual and Predicted (Number of Wins)')
plt.title('Difference between Actual and Predicted: Random Forest')


#let's see how the weight classes match up with Random Forest
features_weight=['Fighter Height', 'Fighter Reach', 'Fighter SLpM', 'Fighter Striking Accuracy',
      'Fighter SApM', 'Fighter Striking Defence', 'Fighter Take Down Average', 'Fighter Take Down Accuracy', 
      'Fighter Take Down Defence', 'Fighter Submission Average', 'wins']
clf_weight = RandomForestClassifier(n_jobs=2, random_state=0, n_estimators=1000, max_features=3)
clf_weight.fit(train[features_weight], train['Fighter Weight'])

predicted_weight=clf_weight.predict(test[features_weight])

imp_weight=list(zip(train[features_weight], clf_weight.feature_importances_))

import seaborn as sns
#evaluate striking correlations
sns.pairplot(df, hue='Fighter Stance', vars=['Fighter Height', 'Fighter Reach',
                                             'Fighter SLpM', 'Fighter Striking Accuracy',
                                             'Fighter SApM', 'Fighter Striking Defence'])

#to plot striking accuracy, slpm
#sapm, slpm

#evaluate grappling correlations
sns.pairplot(df, hue='Fighter Stance', vars=['Fighter Height', 'Fighter Reach', 'Fighter Take Down Average', 
                                             'Fighter Take Down Accuracy', 'Fighter Take Down Defence', 
                                             'Fighter Submission Average'])

#reach, height, weight

sns.pairplot(df, hue='Fighter Stance', vars=['Fighter Height', 'Fighter Reach', 'Fighter Weight'])

#wins, loss, on striking
sns.pairplot(df, hue='Fighter Stance', vars=['wins', 'loss',
                                             'Fighter SLpM', 'Fighter Striking Accuracy',
                                             'Fighter SApM', 'Fighter Striking Defence'])

#wins, loss, on grappling
sns.pairplot(df, hue='Fighter Stance', vars=['wins', 'loss','Fighter Take Down Average', 
                                             'Fighter Take Down Accuracy', 'Fighter Take Down Defence', 
                                             'Fighter Submission Average'])
#sapm vs slpm
sns.lmplot('Fighter SLpM', 'Fighter SApM', hue='Fighter Stance', data=df)

sns.lmplot('Fighter SLpM', 'Fighter SApM', data=df)

#striking accuracy vs slpm
sns.lmplot('Fighter Striking Accuracy', 'Fighter SLpM', data=df, hue='Fighter Stance')
#need to plot and get stats
sns.lmplot('Fighter Striking Accuracy', 'Fighter SLpM', data=df)




