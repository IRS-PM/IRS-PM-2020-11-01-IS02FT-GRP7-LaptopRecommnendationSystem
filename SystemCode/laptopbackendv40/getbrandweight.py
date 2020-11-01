# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:38:40 2020

@author: 77433
"""
rank1=['联想','ThinkPad','戴尔','苹果','惠普','Acer','索尼','华硕','微软', 'Alienware','HUAWEI', 'msi', 'ROG']
rank2=['三星','神舟','机械革命', 'Razer','Redmi','雷神','富士通','东芝','荣耀','小米','炫龙']
rank3=['同方','方正','七彩虹','a豆','中柏','LG']
'''
一线：联想、ThinkPad、戴尔、苹果、惠普、Acer、索尼、华硕，微软, Alienware，HUAWEI, msi, ROG
二线：三星、神舟、机械革命, Razer，Redmi, 雷神，富士通，东芝，荣耀，小米，炫龙
三线：同方、方正、七彩虹，a豆，中柏，LG
'''

def getbrandweight(s,tar=None):
    '''
    s 为品牌字符串 数据库中的数据
    tar 为传入的想要的品牌
    '''
    if s in tar :
        return 1
    if s in rank1 :
        return 0.5
    if s in rank2:
        return 0.2
    if s in rank3:
        return 0.1
    return 0.01
    
    
if __name__ =='__main__':
    t = 'a豆'
    print(getbrandweight(t,'a豆苹果acer'))