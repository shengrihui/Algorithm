# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:51:48 2021

@author: 11200
"""

# 剑指 Offer 10- I. 斐波那契数列

from matplotlib import pyplot as plt
import time
import tqdm
from itertools import accumulate


def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a + b
    return b % (10 ** 9 + 7)


def fib2(n):
    MOD = 10 ** 9 + 7
    if n < 2:
        return n

    def multiply(a, b):
        r, t, c = len(a), len(b), len(b[0])
        ret = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                for k in range(t):
                    ret[i][j] += a[i][k] * b[k][j]
        return ret

    # [2]=[1]+[0]
    # [1]=[1]
    mat = [
        [1, 1],
        [1, 0]
    ]

    def matrix_pow(mat, n):
        ret = [[1], [0]]
        while n:
            if n & 1:
                ret = multiply(mat, ret)
            mat = multiply(mat, mat)
            n >>= 1
        return ret

    ans = matrix_pow(mat, n)
    return ans[1][0] % MOD


if __name__ == '__main__':
    plt.figure(figsize=(16, 9), dpi=80)
    x = range(0, 1000)
    fib1_time = []
    fib2_time = []
    for i in tqdm.tqdm(x):
        t1 = time.time()
        fib1(i)
        t2 = time.time()
        fib1_time.append(t2 - t1)

        t1 = time.time()
        fib2(i)
        t2 = time.time()
        fib2_time.append(t2 - t1)

    fib1_time = list(accumulate(fib1_time))
    fib2_time = list(accumulate(fib2_time))
    plt.plot(x, fib1_time, label='fib1')
    plt.plot(x, fib2_time, label='fib2')

    plt.legend()
    plt.savefig("fib.jpg")
    plt.show()
