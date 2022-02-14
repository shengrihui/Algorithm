# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:49:48 2021

@author: 11200
"""


def reverseStr(s, k):
    kk = 2 * k
    n = len(s)
    i, j = 0, k - 1
    st = list(s)
    while i < n:
        start, end = i, j
        if j >= n:
            end = n - 1
        print(i, j, start, end, n)
        while start < end:
            st[start], st[end] = st[end], st[start]
            start += 1
            end -= 1
        i += kk
        j += kk
    return ''.join(st)


print(reverseStr("abcdefg", 2))
print(reverseStr("abcdefg", 8))
print(reverseStr("abcd", 2))
print(reverseStr("a", 2))
print(
    "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi" == reverseStr(
        "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39))

"""
给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 

示例 1：

输入：s = "abcdefg", k = 2
输出："bacdfeg"
示例 2：

输入：s = "abcd", k = 2
输出："bacd"
 

提示：

1 <= s.length <= 104
s 仅由小写英文组成
1 <= k <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
