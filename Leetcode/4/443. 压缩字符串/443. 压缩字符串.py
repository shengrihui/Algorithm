# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 09:54:08 2021

@author: 11200
"""


def compress(chars):
    s = [chars[0]]
    c = 1
    i = 1
    n = len(chars)
    while i < n:
        if s[-1] != chars[i]:
            if c != 1:
                s.extend(list(str(c)))
            s.append(chars[i])
            c = 1
        else:
            c += 1
            if i == n - 1:
                s.extend(list(str(c)))
        i += 1
    for i, x in enumerate(s):
        chars[i] = x
    # print(chars)
    return len(s)


# def compress(chars):
#     write=left=0
#     n=len(chars)
#     for  right in range(1,n):
#         if chars[right]!=chars[write]or right==n-1:
#             l=right-left
#             if l!=1:
#                 for i in str(l):
#                     write+=1
#                     chars[write]=i
#             write+=1
#             chars[write]=chars[right]
#             left=right
#             right=left+1
#         else:
#             right+=1
#     print(chars)
#     return write


def compress(chars):
    write = left = 0
    n = len(chars)
    for right in range(n):
        if right == n - 1 or chars[right] != chars[right + 1]:
            l = right - left + 1
            if l != 1:
                for i in str(l):
                    write += 1
                    chars[write] = i
            left = right + 1
            if right != n - 1:
                write += 1
                chars[write] = chars[right + 1]
    # print(chars[:write+1])
    return write + 1


print(4, compress(chars=["a", "b", "b", "b", "b",
                         "b", "b", "b", "b", "b", "b", "b", "b"]))
print(6, compress(chars=["a", "a", "b", "b", "c", "c", "c"]))
print(1, compress(chars=["a"]))
print(2, compress(chars=["a", "b"]))

"""
443. 压缩字符串
给你一个字符数组 chars ，请使用下述算法压缩：

从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

如果这一组长度为 1 ，则将字符追加到 s 中。
否则，需要向 s 追加字符，后跟这一组的长度。
压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

请在 修改完输入数组后 ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

 

示例 1：

输入：chars = ["a","a","b","b","c","c","c"]
输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
解释：
"aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
示例 2：

输入：chars = ["a"]
输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
解释：
没有任何字符串被替代。
示例 3：

输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。
解释：
由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
注意每个数字在数组中都有它自己的位置。
 

提示：

1 <= chars.length <= 2000
chars[i] 可以是小写英文字母、大写英文字母、数字或符号

"""
