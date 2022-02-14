# -*- coding: utf-8 -*-
"""
Created on Tue May 11 22:12:46 2021

@author: 11200
"""

from functools import reduce


def decode(encoded):
    n = len(encoded) + 1
    f = lambda x, y: x ^ y
    total = reduce(f, range(1, n + 1))
    odd = reduce(f, encoded[1::2])
    perm = [total ^ odd]

    for i in range(n - 1):
        perm.append(perm[-1] ^ encoded[i])

    return perm


print(decode([3, 1]))
print(decode([6, 5, 4, 6]))
"""
1734. 解码异或后的排列 
给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。

它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。

给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。

 

示例 1：

输入：encoded = [3,1]
输出：[1,2,3]
解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
示例 2：

输入：encoded = [6,5,4,6]
输出：[2,4,1,5,3]
 

提示：

3 <= n < 105
n 是奇数。
encoded.length == n - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-xored-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
