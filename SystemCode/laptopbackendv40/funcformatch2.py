# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:06:26 2020

@author: 77433
"""


def get_duplicate_id(history_list):
    '''
    
    Returns
    -------
    a set contain the same id in then set of history_list

    '''
    result=set()
    length = len(history_list)
    if length<1:
        return set()
    history1 = history_list[0]
    for j in history1:
        for i, history in enumerate(history_list):
            if j not in history:
                break
            else:
                if i ==length-1:
                    result.add(j)
        continue

    return result


if __name__ =='__main__':
    a = set([5,2,3,1,6,1])
    b = set([5,2,4,1,6])
    c = set([5,8,3,1,6])
    history_list=[]
    history_list.append(a)
    history_list.append(b)
    history_list.append(c)
    res = get_duplicate_id(history_list)
    print(res)