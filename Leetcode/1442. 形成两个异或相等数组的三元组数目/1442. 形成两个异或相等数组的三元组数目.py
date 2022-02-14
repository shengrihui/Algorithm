# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:28:29 2021

@author: 11200
"""

from functools import reduce
from collections import Counter
from collections import defaultdict


def countTriplets1(arr):
    l = len(arr)
    f = lambda x, y: x ^ y
    total = 0
    for i in range(0, l - 1):
        for j in range(i + 1, l):
            a = reduce(f, arr[i:j])
            for k in range(j, l):
                b = reduce(f, arr[j:k + 1])
                if a == b:
                    total += 1
    return total


def countTriplets2(arr):
    n = len(arr)
    s = [0]
    for val in arr:
        s.append(s[-1] ^ val)
    # print(arr)
    # print(s)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j, n):
                if s[i] == s[k + 1]:
                    ans += 1
                    # print(i,j,k)
    return ans


def countTriplets3(arr):
    t = 0
    retdict = defaultdict(list)
    retdict[0].append(0)
    ans = 0
    for val in range(len(arr)):
        t = t ^ arr[val]
        retdict[t].append(val + 1)
        if len(retdict[t]) > 1:
            for i in retdict[t][:-1]:
                ans += (val + 1 - 1 - i)

    return ans


countTriplets = [countTriplets1, countTriplets2, countTriplets3]

for i in range(3):
    print(countTriplets[i](arr=[2, 3, 1, 6, 7]) == 4)
    print(countTriplets[i](arr=[1, 1, 1, 1, 1]) == 10)
    print(countTriplets[i](arr=[2, 3]) == 0)
    print(countTriplets[i](arr=[1, 3, 5, 7, 9]) == 3)
    print(countTriplets[i](arr=[7, 11, 12, 9, 5, 2, 7, 17, 22]) == 8)
    print()

"""
1442. 形成两个异或相等数组的三元组数目 1442. 形成两个异或相等数组的三元组数目
给你一个整数数组 arr 。

现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。

a 和 b 定义如下：

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
注意：^ 表示 按位异或 操作。

请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。

 

示例 1：

输入：arr = [2,3,1,6,7]
输出：4
解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
示例 2：

输入：arr = [1,1,1,1,1]
输出：10
示例 3：

输入：arr = [2,3]
输出：0
示例 4：

输入：arr = [1,3,5,7,9]
输出：3
示例 5：

输入：arr = [7,11,12,9,5,2,7,17,22]
输出：8
 

提示：

1 <= arr.length <= 300
1 <= arr[i] <= 10^8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
