# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 12:15:09 2021

@author: 11200
"""

import numpy
import scipy.signal
import numpy as np
from collections import defaultdict


def findPaths(m, n, maxMove, startRow, startColumn):
    if maxMove == 0:
        return 0
    dp = [[[0 for c in range(n)] for r in range(m)] for move in range(maxMove)]
    outCounts = 0
    dp[0][startRow][startColumn] = 1
    for move in range(maxMove):
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0 or r == m - 1 or c == n - 1:
                    t = dp[move][r][c]
                    if t != 0:
                        if r - 1 < 0:
                            outCounts += t
                        if c - 1 < 0:
                            outCounts += t
                        if r + 1 == m:
                            outCounts += t
                        if c + 1 == n:
                            outCounts += t
                if move == maxMove - 1:
                    continue
                for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if i >= 0 and i < m and j >= 0 and j < n:
                        dp[move + 1][r][c] += dp[move][i][j]

    return outCounts % (10 ** 9 + 7)


print(findPaths(36, 5, 50, 15, 3))
print(findPaths(28, 9, 35, 3, 4))
print(findPaths(10, 10, 0, 5, 5))
print(6, findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
print(12, findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))


# 改用字典
def findPaths(m, n, maxMove, startRow, startColumn):
    if maxMove == 0:
        return 0
    dp = {0: {r: defaultdict(int) for r in range(m)}, 1: {
        r: defaultdict(int) for r in range(m)}}
    outCounts = 0
    dp[0][startRow][startColumn] = 1
    for move in range(maxMove):
        for r in range(m):
            for c in range(n):
                dp[1 - move % 2][r][c] = 0
                if r == 0 or c == 0 or r == m - 1 or c == n - 1:
                    t = dp[move % 2][r][c]
                    if t != 0:
                        # print(dp, t)
                        if r - 1 < 0:
                            outCounts += t
                        if c - 1 < 0:
                            outCounts += t
                        if r + 1 == m:
                            outCounts += t
                        if c + 1 == n:
                            outCounts += t
                if move == maxMove - 1:
                    continue
                for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if i >= 0 and i < m and j >= 0 and j < n:
                        dp[1 - move % 2][r][c] += dp[move % 2][i][j]

    return outCounts % (10 ** 9 + 7)


print(findPaths(36, 5, 50, 15, 3))
print(findPaths(28, 9, 35, 3, 4))
print(findPaths(10, 10, 0, 5, 5))
print(6, findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
print(12, findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))


def findPaths(m, n, maxMove, startRow, startColumn):
    if maxMove == 0:
        return 0
    dp = np.zeros((maxMove, m, n))
    # print(dp)
    outCounts = 0
    dp[0][startRow][startColumn] = 1
    for move in range(maxMove):
        for r in range(m):
            for c in range(n):

                if r == 0 or c == 0 or r == m - 1 or c == n - 1:
                    t = dp[move][r][c]
                    if t != 0:
                        t %= (10 ** 9 + 7)
                        if r - 1 < 0:
                            outCounts += t
                        if c - 1 < 0:
                            outCounts += t
                        if r + 1 == m:
                            outCounts += t
                        if c + 1 == n:
                            outCounts += t
                        outCounts %= (10 ** 9 + 7)
                if move == maxMove - 1:
                    continue
                for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= i < m and 0 <= j < n:
                        dp[move + 1][r][c] += dp[move][i][j] % (10 ** 9 + 7)

    return int(outCounts) % 1_000_000_007


print(findPaths(36, 5, 50, 15, 3))
print(findPaths(28, 9, 35, 3, 4))
print(findPaths(10, 10, 0, 5, 5))
print(6, findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))


def findPaths(m, n, maxMove, startRow, startColumn):
    if maxMove <= 0:
        return 0

    ans = 0

    a = numpy.zeros((m, n), )
    a[startRow, startColumn] = 1

    b = numpy.zeros((3, 3), int)
    b[0][1] = b[1][0] = b[-1][1] = b[1][-1] = 1
    print(a)
    for _ in range(maxMove):
        ans += (a[:, 0].sum() + a[:, -1].sum() +
                a[0, :].sum() + a[-1, :].sum()) % 1_000_000_007
        a = scipy.signal.convolve2d(a, b, 'same') % 1_000_000_007
        print(a)
    return int(ans) % 1_000_000_007


print(findPaths(36, 5, 50, 15, 3))
print(findPaths(28, 9, 35, 3, 4))
print(findPaths(10, 10, 0, 5, 5))
print(6, findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
print(12, findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))

"""
576. 出界的路径数
给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。

给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 109 + 7 取余 后的结果。

 

示例 1：


输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
输出：6
示例 2：


输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
输出：12
 

提示：

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
"""
