# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:55:19 2020

@author: Huang109
"""

import numpy as np
#np.random.seed(10)
def rand():
    temp = np.arange(1,15)
    np.random.shuffle(temp)
    return list(temp[10:])
names=globals()
aq='abcdefghijklmnopqrstuvwxyz'
number='0123456789'
for item in (aq):
    for num in (number):
        names['%s%s' %(item,num)]=rand()
    
    
sort_dic={}
for item in (aq):
    for num in (number):
        for item2 in(names['%s%s' %(item,num)]):
            if item2 in sort_dic.keys():
                sort_dic[item2]+=1
            else:
                sort_dic.update( {item2 :1} )
sort_dic = sorted(sort_dic.items(), key=lambda x: x[1],reverse=True)
new={}
for i in sort_dic:
    new.update({i[0]:i[1]})
sort_dic = new
del new
Keys=list(sort_dic.keys())
Values = list(sort_dic.values())
for index in range(len(Keys)):
    print('{:^3} appears {:^5}times'.format(Keys[index],Values[index]))