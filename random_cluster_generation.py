# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:06:42 2021
@author: MahZaky
<<< SirMahZaky >>>
"""

import numpy as np 
import matplotlib.pyplot as plt 


def get_clausters(cluster_num, sample_num=300):
    clusters = [np.random.normal( i*5 , .6,(sample_num,2) ) for i in range(cluster_num) ]
    labels = [np.ones((sample_num,1))*i for i in range(cluster_num)] 
    
    clusters = np.concatenate(clusters, axis=0) 
    labels =np.concatenate(labels,axis = 0) 
    
    indx = np.arange(cluster_num * sample_num) 
    np.random.shuffle(indx) 
    return clusters[indx], labels[indx] 
    



def get_data(num= 300):

    cluster_1 = np.random.normal(0,1,(num,2) ) 
    cluster_1_label = np.zeros((num,1)) 
    #plt.scatter(cluster_1[:,0],cluster_1[:,1],c='red') 
    
    cluster_2 = np.random.normal(size=(num,2) )+5
    cluster_2_label = np.ones((num,1)) 
    #plt.scatter(cluster_2[:,0],cluster_2[:,1],c='blue') 
    
    
    cluster = np.concatenate([cluster_1, cluster_2], axis=0)
    cluster_label = np.concatenate([cluster_1_label, cluster_2_label],axis=0)
    
    indx = np.arange(2*num)
    np.random.shuffle(indx)
    
    cluster = cluster[indx]
    cluster_label = cluster_label[indx]
    
    return cluster, cluster_label 

    

if __name__ == '__main__':
    x,y = get_data() 
    color = ['red','blue'] 
    for i in range(2):
        dt = x[np.where(y == i)[0], :] 
        plt.scatter(dt[:,0], dt[:,1], c=color[i]) 













