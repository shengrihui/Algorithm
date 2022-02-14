# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:41:54 2021

@author: 11200
"""


def numberOfArithmeticSlices(nums):
    n = len(nums)
    if n < 3:
        return 0

    # 取出其中的一段等差数列，计算其中的等差数列的数量
    # x是该等差数列首末
    def acc(x):
        if x < 2:
            return 0
        x = x - 1
        return (x + 1) * x / 2

    number = 0
    pos = 0
    while pos <= n - 3:
        tmp = pos + 1
        d = nums[pos + 1] - nums[pos]
        while d == nums[tmp + 1] - nums[tmp]:
            tmp += 1
            if tmp == n - 1:
                break
        number += acc(tmp - pos)
        pos = tmp
    return int(number)


print(3 == numberOfArithmeticSlices(nums=[1, 2, 3, 4]))
print(0 == numberOfArithmeticSlices(nums=[1]))
print(6 == numberOfArithmeticSlices([1, 3, 5, 7, 9]))
print(0 == numberOfArithmeticSlices([2, 1, 3, 4, 2, 3]))

"""
413. 等差数列划分
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。

 

示例 1：

输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
示例 2：

输入：nums = [1]
输出：0
 

提示：

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
"""
