# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 09:23:28 2021

@author: 11200
"""


def reverseVowels(s):
    l = list(s)
    i, j = 0, len(s) - 1
    Vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    i_step = 1
    j_step = -1
    while i < j:
        if l[i] in Vowels:
            i_step = 0
        if l[j] in Vowels:
            j_step = 0

        if i_step == j_step == 0:
            l[i], l[j] = l[j], l[i]
            i_step = 1
            j_step = -1
        i += i_step
        j += j_step
    return ''.join(l)


print(reverseVowels("leetcode"))
print(reverseVowels("hello"))

"""
345. 反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

 

示例 1：

输入："hello"
输出："holle"
示例 2：

输入："leetcode"
输出："leotcede"
 

提示：

元音字母不包含字母 "y" 。
"""
