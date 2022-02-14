# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:43:15 2021

@author: 11200
"""


def longestPalindromeSubseq(s):
    n = len(s)
    f = [[(0 if i != j else 1) for j in range(n)] for i in range(n)]

    for i in range(n - 2, -1, -1):  # 最后一个没必要，一直到第一个0
        for j in range(i + 1, n):
            if s[i] == s[j]:
                f[i][j] = f[i + 1][j - 1] + 2
            else:
                f[i][j] = max(f[i + 1][j], f[i][j - 1])

    return f[0][n - 1]


print(4 == longestPalindromeSubseq(s="bbbab"))
print(2 == longestPalindromeSubseq(s="cbbd"))


def longestPalindromeSubseq(s):
    n = len(s)
    f = [[(0 if i != j else 1) for j in range(i + 2)] for i in range(n)]

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if s[i] == s[j]:
                f[i][j] = f[i - 1][j + 1] + 2
            else:
                f[i][j] = max(f[i - 1][j], f[i][j + 1])

    return f[n - 1][0]


print(4 == longestPalindromeSubseq(s="bbbab"))
print(2 == longestPalindromeSubseq(s="cbbd"))

"""
516. 最长回文子序列
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

 

示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
 

提示：

1 <= s.length <= 1000
s 仅由小写英文字母组成
"""
