# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 16:47:23 2021

@author: 11200
"""

import time
import heapq


def Answer_1(n, primes):
    dp = [0] * (n + 1)
    dp[1] = 1
    m = len(primes)
    pointers = [1] * m

    for i in range(2, n + 1):
        min_num = min(dp[pointers[j]] * primes[j] for j in range(m))
        dp[i] = min_num
        for j in range(m):
            if dp[pointers[j]] * primes[j] == min_num:
                pointers[j] += 1

    return dp[n]


def A(n, primes):
    seen = {1}
    heap = [1]
    for i in range(n):  # 循环n次，第一次的ugly是1
        ugly = heapq.heappop(heap)  # 弹出heap当中最小的数
        if i == n - 1:
            continue
        for prime in primes:
            nxt = ugly * prime
            if nxt not in seen:  # 如果nxt不在seen里面，就将它加到seen和heap里
                seen.add(nxt)
                heapq.heappush(heap, nxt)
    return ugly


def nthSuperUglyNumber(n, primes):
    nums = 1
    ugly = 1
    while nums < n:
        ugly += 1
        tmp = ugly
        for p in primes:
            if tmp % p == 0:
                while tmp % p == 0:
                    tmp /= p
            if tmp == 1:
                # print(ugly)

                nums += 1
                break
    return ugly


# n=12
primes = [2, 7, 13, 19]
for n in range(12, 13):
    ret = A(n, primes)
    print(ret)
    ans = nthSuperUglyNumber(n, primes)
    print(ans)
    print(ret == ans)
    if ret == ans:
        start = time.time()
        for i in range(100):
            ans = nthSuperUglyNumber(n, primes)
        end = time.time()
        print(end - start)

# for num in dp:
#     ret={2:0,7:0,13:0,19:0}
#     for p in primes:
#         while num:
#             if num % p ==0:
#                 num/=p
#                 ret[p]+=1
#             else :
#                 break
#     print(list(ret.values()))
