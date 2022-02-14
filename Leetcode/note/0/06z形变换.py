# -*- coding: utf-8 -*-
"""
Created on Mon May  3 11:34:30 2021

@author: 11200
"""


def fun(s, numRows):
    li = [[] for i in range(numRows)]
    index = 0
    flag = 1
    for w in s:
        li[index].append(w)

        if index + flag >= numRows or index + flag < 0:
            flag *= -1
        index += flag
    print(li)
    ret = [''.join(i) for i in li]
    print(ret)
    result = ''.join(ret)
    return result


print(fun('PAYPALISHIRING', 3))
