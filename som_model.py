# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 19:20:00 2021
@author: MahZaky
<<< SirMahZaky >>>
"""

import numpy as np 
import matplotlib.pyplot as plt 
import minisom as som
import random_cluster_generation as  gen 



x,y = gen.get_data()
color = ['red','blue']
labels = ['cluster 1', 'cluster 2' ]

ma = som.MiniSom(1,2,2,random_seed=10) 
ma.train_random(x, 1000) 

plt.subplot(1,2,1)#real Sample ploting
for i in range(2):
    dt = x[np.where(y == i)[0], :] 
    plt.scatter(dt[:,0], dt[:,1],
                c=color[i], label =labels[i] ) 
    
plt.legend()

llabels = ['cluster 1 learned', 'cluster 2 learned' ]
plt.subplot(1,2,2) #plting learned clusters
clasters_labels = ma.win_map(x) 
for key, poins in clasters_labels.items():
    i = np.ravel_multi_index(key,(1,2))
    poins = np.array(poins) 
    plt.scatter(poins[:,0],poins[:,1],
                c= color[i], label= llabels[i]) 

    




#plt.scatter(x[:,0], x[:,1]) 

wai = ma.get_weights()
wai = np.reshape(wai, (wai.shape[0]*wai.shape[1],2 ) )
plt.scatter(wai[:,0], wai[:,1], marker='x',c= 'k',
            s =[500,500], label= 'centroid') 

plt.legend() 









