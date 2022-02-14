# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:14:52 2021
Modified on Wed Aug 11 20:00:00 2021

@author: shengrihui
"""

import re


def longestPalindrome(s):
    if len(s) == 1:
        return s
    s = '!'.join(list(s))
    n = len(s)
    max_len = 0
    max_left, max_right = 0, 0
    for idx, w in enumerate(s):
        if w == '!':
            left, right, m = idx - 1, idx + 1, 0
        else:
            left, right, m = idx - 2, idx + 2, 1
        while left >= 0 and right <= n - 1:
            if s[left] == s[right]:
                m += 2
                left -= 2
                right += 2
            else:
                break
        if m > max_len:
            max_len = m
            if right - left == 2:
                max_left = left
                max_right = right
            else:
                max_left = left + 2
                max_right = right - 2

    ret = s[max_left:max_right + 1].split('!')
    return ''.join(ret)


print("bab", longestPalindrome(s="babad"))
print("bb", longestPalindrome(s="cbbd"))
print("a", longestPalindrome(s="a"))
print("a", "c", longestPalindrome(s="ac"))

"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成
"""
