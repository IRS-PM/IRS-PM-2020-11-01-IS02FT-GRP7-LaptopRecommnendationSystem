# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 16:44:45 2020
laptop backend involving rule engine
@author: 77433
"""
from match2 import get_id,get_info
from ruletable import ruletable
from flask import Flask, Response, request
import json
import sqlite3 as sql
#from url_explain import main_op
from flask_cors import *  #跨域支持
app = Flask(__name__)
CORS(app)
RT= ruletable('RULE.txt')
#col_names = ['id', 'name', 'cpu', 'cpu_rank', 'ram', 'disk', 'gpu', 'is_rtx', 'gpu_memory',
# 'price', 'disk_detail', 'weight', 'battery', 'weight_type', 'screen_size', 
# 'battery_life', 'has_camere', 'keyboard', 'keyboard_haslight', 
# 'description', 'video_type', 'thin_type', 'business_type', 'game_type', 
# 'is_apple', 'link', 'img_src']
col_names = ['id', 'brand','name', 'year', 'cpu_rank','cpu', 
             'ram', 'disk', 'is_rtx', 'gpu', 'gpu_memory', 'price',
             'disk_detail', 'weight', 'weight_type', 'battery','battery_life', 
             'screen_size',  'has_camere', 'keyboard_haslight', 'keyboard', 
             'video_type', 'thin_type', 'business_type', 'game_type', 
             'is_apple','description', 'link', 'img_src']
weight1={'cpu_rank':22.5,'ram':22.5,'gpu_memory':22.5,'price':37.5,
         'brand':30,'keyboard_haslight':5,'video_type':5,'thin_type':5,
         'business_type':5,'game_type':5,'is_apple':1000,
         'weight_type':5,'screen_size':5,'battery_life':10}

def convert(d):
    '''
    将d中的数字值转化为数值型
    '''
    for i in d.keys():
        try:
            a = int(d[i])
            if a != 1 and a!=0:
                d[i]=a
        except:
            continue
    return d
                

@app.route('/interface',methods =['POST','GET'])
def respond():
    req=request.form
    req=req.to_dict()
    print(req)
    temp = float(req['price'])
    req = convert(req)
    try:
       m=req['constraint']
       print('hard constraint:', m)
    except:
        m = 'price'
    config = RT.reason(req)
    if 'battery_life' in m:
        config['battery_life']='long'
    if 'weight' in m:
        config['weight']='light'
    del config['budget_type']
    config['price']=temp
    try:
        b = req['brand']
        config['brand']=b
    except:
        pass
#    for i in req.keys():
#        print(i)
    print(config.items())
    itemnumber = 3
    
    '''
    if 'is_apple' in config.keys():
        m = 'is_apple'
        print ('mainkey',m)
    '''
    idlist,score = get_id(config,itemnumber,weight1,mainkey=m)
    if idlist==0:
        mes=[{'mes':"no match laptop,please cancel or modify you constraint and try again",
            'message':"no match laptop,please cancel or modify you constraint and try again"}]
        return Response(json.dumps(mes), status=200, content_type="application/json")
    #print('score  ',len(score))
    infolist = get_info(idlist)  #获取 idlist中对应ID 的详细信息
    if len(infolist) < 1:
        return Response(json.dumps({'msg':404}), status=200, content_type="application/json")
    resp = []
    m=0
    for i in infolist:
        temp = {}
        k=0
        for j in col_names:
            temp[j]=i[k]
            k=k+1
        temp['matching_score']=score[m]
        m = m+1
        resp.append(temp)
    return Response(json.dumps(resp), status=200, content_type="application/json")
'''
@app.route('/interface2',methods =['POST','GET'])
def respond2():
    req=request.form
    print(req)
    url = req['url']
    config = main_op(url)
    price = float(req['price'])
    config['price']=price
    idlist,score = get_id(config)
    infolist = get_info(idlist)
    if len(infolist) < 1:
        return Response(json.dumps({'msg':404}), status=200, content_type="application/json")
    resp = []
    m=0
    for i in infolist:
        temp = {}
        k=0
        for j in col_names:
            temp[j]=i[k]
            k=k+1
        temp['matching_score']=score[m]
        m = m+1
        resp.append(temp)
    return Response(json.dumps(resp), status=200, content_type="application/json")
'''
if __name__ == '__main__':
   app.run(port = 5000,debug = True)
