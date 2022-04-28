# -*- coding: utf-8 -*-
"""
Created on 19:11

@author: shengrihui
"""
# Leetcode
# 564. 寻找最近的回文数
# https://leetcode-cn.com/problems/find-the-closest-palindrome/

from typing import *
from collections import *
import numpy as np


# 评论区的某个回答
class Solution1:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        if l == 1:
            return str(int(n) - 1)
        s = n[: l // 2 + l % 2]
        s1 = str(int(s) - 1)
        s2 = str(int(s) + 1)
        return min(
            '9' * (l - 1),
            '1' + '0' * (l - 1) + '1',
            s + s[-1 - l % 2::-1],
            s1 + s1[-1 - l % 2::-1],
            s2 + s2[-1 - l % 2::-1],
            key=lambda x: (abs(int(x) - int(n)) or 114514, int(x))
        )


class Solution2:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        i, j = (m + 1) // 2, m // 2 + 1
        candidate_1 = n[:i] + n[:j - 1][::-1]
        candidate_2 = (nn := str(int(n[:i]) + 1)) + nn[:j - 1][::-1]
        candidate_3 = (nn := str(int(n[:i]) - 1)) + nn[:j - 1][::-1]
        ans = -1
        selfNumber = int(n)
        candidate_list = list(map(int, [candidate_3, candidate_2, candidate_1]))
        candidate_list.append(x := (10 ** (m - 1) - 1))
        candidate_list.append(x + 2)
        for num in candidate_list:
            if num != selfNumber:
                if ans == -1 or \
                        abs(selfNumber - num) < abs(selfNumber - ans) or \
                        abs(selfNumber - num) == abs(selfNumber - ans) and num < ans:
                    ans = num
        return str(ans)

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1]
        selfPrefix = int(n[:(m + 1) // 2])
        for x in range(selfPrefix - 1, selfPrefix + 2):
            y = x if m % 2 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)

        ans = -1
        selfNumber = int(n)
        for candidate in candidates:
            if candidate != selfNumber:
                if ans == -1 or \
                        abs(candidate - selfNumber) < abs(ans - selfNumber) or \
                        abs(candidate - selfNumber) == abs(ans - selfNumber) and candidate < ans:
                    ans = candidate
        return str(ans)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/find-the-closest-palindrome/solution/xun-zhao-zui-jin-de-hui-wen-shu-by-leetc-biyt/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


examples = [
    # ["123", "121"],
    # ["1", " 0"],
    # ["1234", "1221"],
    # ["4321", "4334"],
    # ['29', '33'],
    ["10", "9"],
    ["100000010000001","ss"]
]

solution = [Solution(),Solution1(),Solution2()]
for data, ans in examples:
    for s in solution:
        print(data, s.nearestPalindromic(data), ans)

a=[1,2,3,4]

print(min(a,key=lambda x:-x))
print(min(a,key=lambda x:(abs(x-2) or 114514,x)))

f=lambda x:(abs(x-2) or 114514,x)
for i in a:
    print(i,f(i))

print()
n="100000010000001"
l = len(n)

s = n[: l // 2 + l % 2]
s1 = str(int(s) - 1)
s2 = str(int(s) + 1)
aa=[
    '9' * (l - 1),
    '1' + '0' * (l - 1) + '1',
    s + s[-1 - l % 2::-1],
    s1 + s1[-1 - l % 2::-1],
    s2 + s2[-1 - l % 2::-1]
    ]


f=lambda x: (abs(int(x) - int(n)) or 114514, int(x))
ll=[f(i) for i in aa]
print(sorted(ll))
for i in aa:
    print(f(i))


