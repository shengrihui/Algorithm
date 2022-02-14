# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:03:19 2021

@author: 11200
"""

from collections import defaultdict


def countDigitOne(n):
    """纯暴力解法。
    遍历小于等于n的数，如果最后一位是1 if i % 10==1 ，
    计数加一，然后整除10"""
    c = 0
    for i in range(n + 1):
        while i:
            if i % 10 == 1:
                c += 1
            i //= 10
    return c


# print(6==countDigitOne(13))
# print(0==countDigitOne(0))
print(countDigitOne(1595865))


def countDigitOne(n):
    if n < 10:
        return 1 if n > 0 else 0

    d = {k: (1 if k == 1 else 0) for k in range(10)}
    num_len = 2
    for i in range(10, n + 1):
        highest = pow(10, num_len - 1)
        t = d[i % highest]
        if i // highest == 1:
            t += 1
        elif i // highest == 10:
            num_len += 1
            t += 1
        d[i] = t
    return sum(d.values())


print(13, 6, countDigitOne(13))
print(0, 0, countDigitOne(0))
print(countDigitOne(1595865))


def countDigitOne(n):
    c = 0
    numk = 1
    while n >= numk:
        c += (n // (numk * 10)) * numk
        r = n % (numk * 10) - numk + 1
        if r <= 0:
            c += 0
        elif r >= numk:
            c += numk
        else:
            c += r
        numk *= 10
    return c


print(13, 6, countDigitOne(13))
print(0, 0, countDigitOne(0))
print(countDigitOne(1595865))

"""
233. 数字 1 的个数
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

 

示例 1：

输入：n = 13
输出：6
示例 2：

输入：n = 0
输出：0
 

提示：

0 <= n <= 2 * 109
"""
