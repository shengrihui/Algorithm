# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 08:43:48 2021

@author: 11200
"""
from collections import defaultdict


# 方法一


def findCheapestPrice(n, flights, src, dst, k):
    dst_price = defaultdict(list)
    for s, d, p in flights:
        dst_price[s].append([d, p])
        # dst_price[d].append([s, p])
    # print(dst_price)
    next_place = [src]
    next_price = [0]
    temp_place = []
    temp_price = []
    kk = k
    ret = []
    while k >= 0:
        for f, p0 in zip(next_place, next_price):
            for d, p in dst_price[f]:
                temp_place.append(d)
                temp_price.append(p0 + p)
                # print(f,d,temp_place)
                # print(temp_price)
                if d == dst:
                    ret.append(p0 + p)
        next_place = temp_place
        next_price = temp_price
        # print(next_place)
        # print(next_price,"***")
        temp_place = []
        temp_price = []
        k -= 1
    return min(ret) if ret != [] else -1


# 方法二 回溯


def findCheapestPrice(n, flights, src, dst, k):
    dst_price = defaultdict(list)
    for s, d, p in flights:
        dst_price[s].append([d, p])

    place = [src]
    price = [0]
    ret = []

    def forward(k, place, price):
        if k < 0:
            return
        for d, p0 in dst_price[place[-1]]:
            if d == dst:
                ret.append(price[-1] + p0)
            place.append(d)
            price.append(price[-1] + p0)
            forward(k - 1, place, price)
            place.pop()
            price.pop()

    forward(k, place, price)
    return min(ret) if ret != [] else -1


# 方法三 动态规划


def findCheapestPrice(n, flights, src, dst, k):
    dp = [[float("inf")] * n for _ in range(k + 2)]
    dp[0][src] = 0
    ret = []
    for t in range(1, k + 2):
        for f, d, cost in flights:
            dp[t][d] = min(dp[t][d], dp[t - 1][f] + cost)
            if d == dst and dp[t][d] != float("inf"):
                ret.append(dp[t][d])
    return min(ret) if ret != [] else -1


# 方法三 动态规划


def findCheapestPrice(n, flights, src, dst, k):
    # dst_price = defaultdict(list)
    # for s, d, p in flights:
    #     dst_price[s].append([d, p])

    dp = [float("inf")] * n
    ans = float("inf")

    # next_place = [src]
    dp[src] = 0
    for t in range(1, k + 2):
        g = [float("inf")] * n
        for f, d, cost in flights:
            g[d] = min(g[d], dp[f] + cost)
            # temp = []
            # for f in next_place:
            #     for d, p in dst_price[f]:
            #         g[d] = min(g[d], dp[f]+p)
            #         temp.append(d)
            if d == dst:
                ans = min(ans, g[d])
        dp = g
        # next_place = temp
    return -1 if ans == float("inf") else ans


print(200, findCheapestPrice(n=3, flights=[
    [0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))
print(500, findCheapestPrice(n=3, flights=[
    [0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))
print(-1, findCheapestPrice(5, [[4, 1, 1], [1, 2, 3],
                                [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1))

"""
787. K 站中转内最便宜的航班
有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 toi 抵达 pricei。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。

 

示例 1：

输入: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出: 200
解释: 
城市航班图如下


从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。
示例 2：

输入: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
输出: 500
解释: 
城市航班图如下


从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。
 

提示：

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
航班没有重复，且不存在自环
0 <= src, dst, k < n
src != dst
"""
