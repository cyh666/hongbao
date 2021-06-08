# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:26:07 2021

@author: Hulk
"""

import random

def hongbao(total,num):
    #total 紅包總金額 
    #num 紅包數量
    each=[]
    
    #已發紅包金額
    already = 0
    
    for i in range(1,num):
        #為當前紅包隨機分配金額
        #至少給剩下的每一人分一塊錢
        t=random.randint(1,(total-already)-(num-i))
        each.append(t)
        already = already + t
        
    #剩餘的給最後一人
    each.append(total-already)
    return each

if __name__=='__main__':
    total = 50
    num = 6
    
    #模擬30次
    for i in range(30):
        each=hongbao(total,num)
        print(each)