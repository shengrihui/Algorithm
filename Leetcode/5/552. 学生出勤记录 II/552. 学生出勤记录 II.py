# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 09:21:05 2021

@author: 11200
"""


# 最初尝试


def checkRecord1(n):
    if n == 1:
        return 3
    if n == 2:
        return 8
    dp, late, present = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    # dp, late, present = {}, {}, {}
    present[0] = late[0] = 1
    present[1] = late[1] = 1
    present[2] = late[2] = 2
    dp[0], dp[1], dp[2] = 1, 2, 4

    for i in range(3, n + 1):
        present[i] = present[i - 1] + late[i - 1]
        late[i] = present[i - 1] + present[i - 2]
        dp[i] = (present[i] + late[i]) % (10 ** 9 + 7)
    # print(present)
    # print(dp)
    ret = 0
    for i in range(n):
        t = dp[i] * dp[n - 1 - i]
        ret += t % (10 ** 9 + 7)
    ret += dp[n]
    return ret % (10 ** 9 + 7)


# dp[i]
# = present[i]+late[i]
# =present[i-1]+late[i-1]+present[i-1]+present[i-2]
# =present[i-1]+(present[i-2]+present[i-3]) + present[i-1]+present[i-2]
# =2*present[i-1]+2*present[i-2]+present[i-3]

# 参考泰波纳契数列
def checkRecord2(n):
    if n == 1:
        return 3
    if n == 2:
        return 8
    if n == 3:
        return 19
    # dp = [0]*(n+1)
    dp = {}
    dp[0], dp[1], dp[2], dp[3] = 1, 2, 4, 7

    a, b, c = 1, 2, 4
    for i in range(4, n + 1):
        dp[i] = a + 2 * b + 2 * c
        a, b, c = b, c, a + b + c
    #     print(c)
    # print(dp)
    ret = 0
    for i in range(n):
        t = dp[i] * dp[n - 1 - i]
        ret += t % (10 ** 9 + 7)
    ret += dp[n]
    return ret % (10 ** 9 + 7)


# 修改第一种方法，测试时间


def checkRecord4(n):
    if n == 1:
        return 3
    if n == 2:
        return 8
    dp, present = [0] * (n + 1), [0] * (n + 1)
    # dp, late, present = {}, {}, {}
    present[0] = 1
    present[1] = 1
    present[2] = 2
    dp[0], dp[1], dp[2] = 1, 2, 4

    for i in range(3, n + 1):
        present[i] = present[i - 1] + present[i - 2] + present[i - 3]

        dp[i] = (present[i] + present[i - 1] + present[i - 2]) % (10 ** 9 + 7)
    # print(present)
    # print(dp)
    ret = 0
    for i in range(n):
        t = dp[i] * dp[n - 1 - i]
        ret += t % (10 ** 9 + 7)
    ret += dp[n]
    return ret % (10 ** 9 + 7)


# 参考官方题解的思路，自己再写一个


def checkRecord5(n):
    # 0 前面没有A，现在要加P  +=[0]+[1]+[2]
    # 1 前面没有A，上一个不是L，现在要加L  +=[0]
    # 2 前面没有A，上一个是L，现在要加L    +=[1]
    # 3 前面有A，现在要加P   +=[6]+[3]+[4]+[5]
    # 4 前面有A，上一个不是L，现在要加L    +=[6]+[3]
    # 5 前面有A，上一个是L，现在要加L     +=[4]
    # 6 现在要加A  +=[0]+[1]+[2]
    MOD = 10 ** 9 + 7
    # dp = [[0 for _ in range(7)] for _ in range(n+1)]
    # dp[1] = [1, 1, 0, 0, 0, 0, 1]
    # for i in range(2, n+1):
    #     dp[i][0] += (dp[i-1][0]+dp[i-1][1]+dp[i-1][2])% MOD
    #     dp[i][1] += dp[i-1][0]% MOD
    #     dp[i][2] += dp[i-1][1]% MOD
    #     dp[i][3] += (dp[i-1][6]+dp[i-1][3]+dp[i-1][4]+dp[i-1][5])% MOD
    #     dp[i][4] += (dp[i-1][6]+dp[i-1][3])% MOD
    #     dp[i][5] += dp[i-1][4]% MOD
    #     dp[i][6] += (dp[i-1][0]+dp[i-1][1]+dp[i-1][2])% MOD
    # return sum(dp[n])%MOD
    dp = [[0 for _ in range(7)], [0 for _ in range(7)]]
    dp[0][0] = 1
    for i in range(1, n + 1):
        a, b = i % 2, 1 - i % 2
        dp[a][0] += (dp[b][0] + dp[b][1] + dp[b][2]) % MOD
        dp[a][1] += dp[b][0] % MOD
        dp[a][2] += dp[b][1] % MOD
        dp[a][3] += (dp[b][6] + dp[b][3] + dp[b][4] + dp[b][5]) % MOD
        dp[a][4] += (dp[b][6] + dp[b][3]) % MOD
        dp[a][5] += dp[b][4] % MOD
        dp[a][6] += (dp[b][0] + dp[b][1] + dp[b][2]) % MOD
        dp[b] = [0] * 7
    return sum(dp[n % 2]) % MOD


# 官方题解
def checkRecord3(n):
    MOD = 10 ** 9 + 7
    # 长度，A 的数量，结尾连续 L 的数量
    dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(n + 1)]
    dp[0][0][0] = 1

    for i in range(1, n + 1):
        # 以 P 结尾的数量
        for j in range(0, 2):
            for k in range(0, 3):
                dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

        # 以 A 结尾的数量
        for k in range(0, 3):
            dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD

        # 以 L 结尾的数量
        for j in range(0, 2):
            for k in range(1, 3):
                dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % MOD

    total = 0
    for j in range(0, 2):
        for k in range(0, 3):
            total += dp[n][j][k]

    return total % MOD


# 矩阵快速幂（自己写）


def checkRecord6(n):
    mat = [
        [1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0]
    ]
    MOD = 10 ** 9 + 7

    def multiply(a, b):
        # a[r*m] * b[m*c] = ret[r*c]
        r, m, c = len(a), len(a[0]), len(b[0])
        ret = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                for k in range(m):
                    ret[i][j] += a[i][k] * b[k][j]
                    ret[i][j] %= MOD
        return ret

    def matrixpow(mat, n):
        ret = [[1], [0], [0], [0], [0], [0], [0]]
        while n:
            if n & 1:
                ret = multiply(mat, ret)
            mat = multiply(mat, mat)
            n >>= 1
        return ret

    ret = matrixpow(mat, n)
    ans = 0
    for i in ret:
        ans += i[0] % MOD
    return ans % MOD


def checkRecord7(n: int) -> int:
    MOD = 10 ** 9 + 7
    mat = [
        [1, 1, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0],
    ]

    def multiply(a, b):
        rows, columns, temp = len(a), len(b[0]), len(b)
        c = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                for k in range(temp):
                    c[i][j] += a[i][k] * b[k][j]
                    c[i][j] %= MOD
        return c

    def matrixPow(mat, n):
        ret = [[1, 0, 0, 0, 0, 0]]
        while n > 0:
            if (n & 1) == 1:
                ret = multiply(ret, mat)
            n >>= 1
            mat = multiply(mat, mat)
        return ret

    res = matrixPow(mat, n)
    ans = sum(res[0])
    return ans % MOD


ans = [19, 43, 94, 200, 418, 183236316, 749184020]
test = [3, 4, 5, 6, 7, 10101, 100000]
for a, b in zip(test, ans):
    print(b == checkRecord1(n=a))
    print(b == checkRecord2(n=a))
    print(b == checkRecord3(n=a))
    print(b == checkRecord5(n=a))
    print(b == checkRecord6(n=a))
    print(b == checkRecord7(n=a))
    # if a == 5:
    #     break
