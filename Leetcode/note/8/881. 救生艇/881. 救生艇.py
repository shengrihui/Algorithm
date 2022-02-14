# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:21:10 2021

@author: 11200
"""

from collections import defaultdict


def numRescueBoats(people, limit):
    d = defaultdict(int)
    i, j = limit + 1, 0
    for w in people:
        d[w] += 1
        if i > w:
            i = w
        if j < w:
            j = w
    boats = 0
    while i < j:
        if d[j] == 0:
            j -= 1
            continue
        if d[i] == 0:
            i += 1
            continue
        if i + j > limit:
            boats += d[j]
            j -= 1
            continue
        m = min(d[i], d[j])
        boats += m
        d[i] -= m
        d[j] -= m
        # i += (1-d[i]/1)
        # # if d[i]==0:
        # #     i-=1
        # j -= (1-d[j]/1)

    if i <= limit / 2:
        boats += (d[i] + 1) // 2
    else:
        boats += d[i]

    return boats


print(1, numRescueBoats(people=[1, 2], limit=3))
print(3, numRescueBoats(people=[3, 2, 2, 1], limit=3))
print(4, numRescueBoats(people=[3, 5, 3, 4], limit=5))
print(2, numRescueBoats(people=[2, 4], limit=5))
print(1, numRescueBoats(people=[2, 2], limit=6))
print(5, numRescueBoats(people=[1, 3, 4, 3, 3, 5], limit=5))
print()


def numRescueBoats(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0
    while i < j:
        if people[i] + people[j] > limit:
            j -= 1
            boats += 1
        else:
            boats += 1
            i += 1
            j -= 1
        # boats += 1
        if i == j:
            boats += 1
    return boats


print(1, numRescueBoats(people=[1, 2], limit=3))
print(3, numRescueBoats(people=[3, 2, 2, 1], limit=3))
print(4, numRescueBoats(people=[3, 5, 3, 4], limit=5))
print(2, numRescueBoats(people=[2, 4], limit=5))
print(1, numRescueBoats(people=[2, 2], limit=6))
print(5, numRescueBoats(people=[1, 3, 4, 3, 3, 5], limit=5))

"""
881. 救生艇
第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

 

示例 1：

输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)
示例 2：

输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)
示例 3：

输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)
提示：

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
"""
