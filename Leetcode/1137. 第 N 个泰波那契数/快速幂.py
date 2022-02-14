# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:27:20 2021

@author: 11200
"""


def multiply_pow_0(k, n):
    ret = 1
    for i in range(n):
        ret *= k
    return ret


def multiply_pow_1(k, n):
    t = k
    ret = 1
    while n:
        if n & 1:
            ret = ret * t
        t = t * t
        n >>= 1
    return ret


def multiply_pow_2(k, n):
    t = k
    ret = 1
    while n:
        if n % 2:
            ret = ret * t
        t = t * t
        n //= 2
    return ret


def multiply_pow_3(k, n):
    def func(t, n):
        if n == 0:
            return 1

        if n & 1:
            return t * func(t * t, n >> 1)
        else:
            return 1 * func(t * t, n >> 1)

    return func(k, n)


def test(k, n):
    import time

    def f(k, n, fun):
        start = time.time()
        ret = fun(k, n)
        end = time.time()
        # print(end-start)
        return end - start, ret

    # ret0=f(k,n,multiply_pow_0)
    t1, ret1 = f(k, n, multiply_pow_1)
    # t2, ret2 = f(k, n, multiply_pow_2)
    t3, ret3 = f(k, n, multiply_pow_3)

    print(t1)
    print(t3)
    print(ret1 == ret3)


test(9, 623456)
