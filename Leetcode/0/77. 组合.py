# -*- coding: utf-8 -*-
"""
Created on Sat May  8 20:17:56 2021

@author: 11200
"""


def combine(n, k):
    ret = []

    def func(path, n, k, startindex):

        if len(path) == k:
            ret.append([i for i in path])
            return

        for i in range(startindex, n + 1):
            path.append(i)
            func(path, n, k, i + 1)
            path.pop()

    func([], n, k, 1)
    return ret


print(combine(4, 2))

'''

77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
'''
