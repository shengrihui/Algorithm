# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:23:31 2021

@author: 11200
"""

import itertools


def sumOddLengthSubarrays(arr):
    n = len(arr)
    SUM = 0
    for i in range(n):
        for j in range(i, n, 2):
            SUM += sum(arr[i:j + 1])
    return SUM


def sumOddLengthSubarrays(arr):
    n = len(arr)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + arr[i]
    SUM = 0
    for i in range(n):
        for j in range(i, n, 2):
            SUM += pre[j + 1] - pre[i]
    return SUM


print(58, sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3]))
print(3, sumOddLengthSubarrays(arr=[1, 2]))
print(66, sumOddLengthSubarrays(arr=[10, 11, 12]))

"""
1588. 所有奇数长度子数组的和
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。

 

示例 1：

输入：arr = [1,4,2,5,3]
输出：58
解释：所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
示例 2：

输入：arr = [1,2]
输出：3
解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
示例 3：

输入：arr = [10,11,12]
输出：66
 

提示：

1 <= arr.length <= 100
1 <= arr[i] <= 1000
"""
