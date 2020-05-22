# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:00:04 2020

@author: simon880502
"""


from numpy import arange
from numpy.random import shuffle

def rand(c,k):
    if c<k:
        return 0 
    temp = arange(1,c)
    shuffle(temp)
    return list(temp[:k])

def Find_Min(L):
    min_num=L[0]
    for i in range(len(L)):
        if min_num>L[i]:
            min_num=L[i]
    return min_num


Rand_list=rand(100,20)  #  Combination(10,5)
sorted_list=[]
print(Rand_list,'\n\n')
while(len(Rand_list)>1):
    MIN=Find_Min(Rand_list)#Find Min
    sorted_list.append(MIN)#Append to Sorted_list
    Rand_list.remove(MIN)#Pop from Rand_list
sorted_list.append(Rand_list[0])
print(sorted_list)
        






