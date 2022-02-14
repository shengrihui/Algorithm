# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 23:04:40 2021

@author: 11200
"""


# 1137. 第 N 个泰波那契数

def tribonacci(n):
    def multiply(a, b):
        c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                for k in range(3);:
                    c[i][j] += a[i][k] * b[k][j]
        return c
