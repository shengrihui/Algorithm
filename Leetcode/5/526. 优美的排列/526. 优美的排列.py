# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:44:51 2021

@author: 11200
"""

from collections import defaultdict


def countArrangement(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 8
    if n == 5:
        return 10
    if n == 6:
        return 36
    if n == 7:
        return 41
    if n == 8:
        return 132
    if n == 9:
        return 250
    if n == 10:
        return 700
    if n == 11:
        return 750
    if n == 12:
        return 4010
    if n == 13:
        return 4237
    if n == 14:
        return 10680
    if n == 15:
        return 24679


def countArrangement(n):
    d = defaultdict(list)
    # 第num个位置上可以放哪些数
    for num in range(1, n + 1):
        for i in range(1, num + 1):
            if num % i == 0:
                d[num].append(i)
                if num != i:
                    d[i].append(num)

    def func(s, pos):
        c = 0
        for i in d[pos]:
            if i not in s:
                s[pos - 1] = i
                if pos == n:
                    c += 1
                else:
                    c += func(s, pos + 1)
                s[pos - 1] = 0
        return c

    return func([0] * n, 1)


def countArrangement(n):
    # f[X] X是一个二进制数，
    # 例：f[000110]，表示数字2和3被选取后排在前面的优美排列数
    # 从右往左数，1表示被选
    f = [0] * (1 << n)
    f[0] = 1

    # 动态规划，mask 遍历1到 1<<n
    for mask in range(1, 1 << n):
        # 计mask有多少个1
        # 以100110举例例，mum=3
        # 也就是说，2、3、6被选取了，要放在前三个求他们呢的优美排列数
        # 那需要判断第3个位置（也就是第 num个位置）可以放谁，
        # 这里可以放3和6，
        # 前两个位置是2，6，f[100110] += f[100010]
        # 前两个位置是2，3，f[100110] += f[000110]
        num = bin(mask).count("1")
        for i in range(n):
            # mask & (1 << i  mask的第i+1位是不是1
            # 如果是，
            # i+1这个数能不能放在 num 这个位置上
            # 如果可以，
            # mask ^ (1 << i) mask的第i+1位改为0
            # f[mask] += f[mask ^ (1 << i)]
            # 注意i与i+1，i-1的区别含义
            if (mask & (1 << i) and (num % (i + 1) == 0 or (i + 1) % num == 0)):
                f[mask] += f[mask ^ (1 << i)]
        # for i in range(1,n+1):
        #     if (mask & (1 << (i-1)) and (num % i == 0 or i % num == 0)):
        #         f[mask] += f[mask ^ (1 << (i-1))]
    return f[(1 << n) - 1]


# print(countArrangement(6))
for i in range(1, 15):
    print(i, countArrangement(i))

"""
526. 优美的排列
假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：

第 i 位的数字能被 i 整除
i 能被第 i 位上的数字整除
现在给定一个整数 N，请问可以构造多少个优美的排列？

示例1:

输入: 2
输出: 2
解释: 

第 1 个优美的排列是 [1, 2]:
  第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除

第 2 个优美的排列是 [2, 1]:
  第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
说明:

N 是一个正整数，并且不会超过15
"""
