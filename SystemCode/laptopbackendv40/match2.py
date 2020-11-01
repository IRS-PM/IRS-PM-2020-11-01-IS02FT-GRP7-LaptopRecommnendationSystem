# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:55:17 2020
refer to macth.py to get original code ,this version has been transfer into function
@author: 77433
"""

'''
数据库列名
'id', 'name', 'cpu', 'cpu_rank', 'ram', 'disk', 'gpu', 'is_rtx',
       'gpu_memory', 'price', 'disk_detail', 'weight', 'battery',
       'weight_type', 'screen_size', 'battery_life', 'has_camere', 'keyboard',
       'keyboard_haslight', 'description', 'video_type', 'thin_type',
       'business_type', 'game_type', 'is_apple','link', 'img_src'
       
其中 cpu_rank ,ram ,gpu_memory,is_rtx,gpu_memory,price ,weight_type ,screen_size,battery_life
keyboard_haslight ,video_type,thin_type,business_type,game_type  参与匹配
'''
import sqlite3 as sql
from getbrandweight import getbrandweight
from funcformatch2 import get_duplicate_id

weight={ 'cpu_rank':5,'ram':5,'gpu_memory':5 ,'is_rtx':3,'price':10,
        'weight_type':2,'screen_size':2,'battery_life':3,'keyboard_haslight':2,
        'video_type':2,'thin_type':2,'business_type':2,'game_type':2,'is_apple':3}

weight1={'cpu_rank':22.5,'ram':22.5,'gpu_memory':22.5,'price':37.5,
         'brand':30,'keyboard_haslight':5,'video_type':5,'thin_type':5,
         'business_type':5,'game_type':5,'is_apple':1000,
         'weight_type':5,'screen_size':5,'battery_life':10}
dbname = 'database.db'


def get_id(d,num=3,weight=weight1,mainkey='price'):
    '''
    d 为传入的字典
    num 为返回的电脑id 数量，如果num =3 ，那么返回最匹配的三台电脑
    mainkey 为强制选择的列，字符串类型，只可以为 'is_apple','price' mainkey = 'price'那么会首先选择一定价格范围内的电脑
    '''
    c={}
    answer =[]
    score = [0]*num
    history_list=[]
    
    con = sql.connect(dbname)
    #con.text_factory = str
    con.text_factory = lambda x : str(x, 'gbk', 'ignore')
    cur = con.cursor()
    mainkey_list = mainkey.split(',')
    for mainkey in mainkey_list:
        history = set()
        if mainkey=='price':
            sqlcmd = f'select id,{mainkey} from laptop where {mainkey} > {float(d[mainkey])*0.9} and {mainkey}<{float(d[mainkey])*1.1}'
            cur.execute(sqlcmd)
            result = cur.fetchall()
            #print('priceresult1',result)
            for j in result:
                history.add(j[0])
                c[j[0]]=float(d[mainkey])/float(j[1])*weight[mainkey]
    
        else:
            try:
                sqlcmd = f"select id,{mainkey} from laptop where {mainkey} >{int(d[mainkey])} "
                cur.execute(sqlcmd)
                result = cur.fetchall()
                for j in result:
                    history.add(j[0])
                    c[j[0]]=weight[mainkey]
            except:
                # con.text_factory = str
                # for row in con.execute(f" select id from laptop where {mainkey} = ?",(d[mainkey],)):
                #     history.add(row[0])
                
                if mainkey=='brand':
                    for i in d[mainkey].split(','):
                        print(i)
                        sqlcmd = f"select id,{mainkey} from laptop where {mainkey} ='{i}' "
                        cur.execute(sqlcmd)
                        result = cur.fetchall()
                        for j in result:
                            history.add(j[0])
                            c[j[0]]=weight[mainkey]
                else:
                    if mainkey=='weight':mainkey='weight_type'
                    sqlcmd = f"select id,{mainkey} from laptop where {mainkey} ='{d[mainkey]}' "
                    cur.execute(sqlcmd)
                    result = cur.fetchall()
                    for j in result:
                        history.add(j[0])
                        c[j[0]]=weight[mainkey]
                
        history_list.append(history)
    history = get_duplicate_id(history_list)
    if len(history)==0:
        return 0,0
    del d[mainkey]
    if len(history)<num:
        return history,score
    #print(history)
    for i in d.keys(): # price
        if i == 'price':
            sqlcmd = f'select id,{i} from laptop where {i} > {float(d[i])*0.9} and {i}<{float(d[i])*1.1}'
            cur.execute(sqlcmd)
            result = cur.fetchall()
            #print('priceresult',result)
            for j in result:
                if j[0] in history:
                    c[j[0]]=c[j[0]]+float(d[i])/float(j[1])*weight[i]# d -user  j-actual
        
        if i == 'cpu_rank': #数值型
            sqlcmd = f'select id,{i} from laptop where {i} > {float(d[i])*0.8} '
            cur.execute(sqlcmd)
            result = cur.fetchall()
            for j in result:
                if j[0] in history:
                    c[j[0]]= c[j[0]]+(0.1*(float(j[1])-float(d[i]))+1)*weight[i]
        
        if i == 'screen_size':
            sqlcmd = f'select id,{i} from laptop where {i} > {float(d[i])*0.7} and {i}<{float(d[i])*1.3}'
            cur.execute(sqlcmd)
            result = cur.fetchall()
            for j in result:
                if j[0] in history:
                    c[j[0]]= c[j[0]]+(1-abs(float(j[1])-float(d[i]))/float(d[i]))*weight[i]
        if i == 'ram':
            sqlcmd = f'select id,{i} from laptop where {i} > {0.9*float(d[i])} and {i} < {2.1*float(d[i])}'
            cur.execute(sqlcmd)
            result = cur.fetchall()
            for j in result:
                if j[0] in history:
                    c[j[0]]= c[j[0]]+(0.1*(float(j[1])/float(d[i]))+1)*weight[i]
        if i == 'gpu_memory':
            sqlcmd = f'select id,{i} from laptop where {i} > {0.9*float(d[i])} and {i} < {2.1*float(d[i])}'
            cur.execute(sqlcmd)
            result = cur.fetchall()
            for j in result:
                if j[0] in history:
                    c[j[0]]= c[j[0]]+(0.1*(float(j[1])-float(d[i]))+1)*weight[i]
        if i == 'brand':
            sqlcmd = f'select id,{i} from laptop where {i} != 0'
            cur.execute(sqlcmd)
            result = cur.fetchall()
            for j in result:
                if j[0] in history:
                    c[j[0]]= c[j[0]]+weight[i]*getbrandweight(j[1],d[i])
        else :
            sqlcmd = f"select id,{i} from laptop where {i} ='{d[i]}'"
            cur.execute(sqlcmd)
            result = cur.fetchall()
            for j in result:
                if j[0] in history:
                    c[j[0]]= c[j[0]]+weight[i]
    con.close()
    choose_list = sorted(c.items(),key=lambda x:x[1],reverse = True)
    i = 0
    score.clear()
    while len(answer)<num:
        answer.append(choose_list[i][0])
        score.append(choose_list[i][1])
        i=i+1
        try:
            while choose_list[i-1][1]-choose_list[i][1]<0.1:
                i=i+1
        except:
            return answer,score
    #return answer,choose_list
    return answer,score

def get_info(idlist):
    '''
    根据idlist求数据库获取对应 电脑的配置信息
    '''
    con = sql.connect(dbname)
    con.text_factory = lambda x : str(x, 'gbk', 'ignore')
    cur = con.cursor()
    result=[]
    for i in idlist:
        sqlcmd = f'select * from laptop where id ={i}'
        cur.execute(sqlcmd)
        temp = cur.fetchone()
        result.append(temp)
    con.close()
    return result
    

if __name__ == '__main__':
    case = {'price':5500,'cpu_rank':5,'ram':8,'gpu_memory': 4 ,'keyboard_haslight':'1','game_type':'1',
    'battery_life':'long','screen_size' : 15}
    resultid,score = get_id(case,3,weight)
    result = get_info(resultid)
    print(resultid)
    print(result)
    