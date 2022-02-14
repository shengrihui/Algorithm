# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 14:48:34 2021

@author: 11200
"""

from collections import defaultdict


def numberOfArithmeticSlices(nums):
    print(nums)
    n = len(nums)
    d_head_seq_dict = defaultdict(dict)
    for i in range(n - 1):  # i算到倒数第二个
        print(d_head_seq_dict)
        for j in range(i + 1, n):  # j从idx_1的下一个开始一直到最后一个
            d = nums[j] - nums[i]  # 计算nums[j]和nums[i]的差
            if d not in d_head_seq_dict:  # 如果这个差d不在d_dict里，
                d_head_seq_dict[d][i] = [i, j]  # 就新增它，并初始值为{i:[i,j]}
            else:  # 如果这个差d再d_dict里，
                for k in d_head_seq_dict[d]:  # 且已经有i在里面，
                    if d == 0:
                        if j not in d_head_seq_dict[d][k]:
                            if nums[d_head_seq_dict[d][k][-1]] == nums[j]:
                                d_head_seq_dict[d][k].append(j)
                        break
                    if i == d_head_seq_dict[d][k][-1]:  # 就将就j街道d_dict[d][i]后
                        d_head_seq_dict[d][k].append(j)
                        break
                else:  # 不然就新增d_dict[d][i]，并初始为[i,j]
                    d_head_seq_dict[d][i] = [i, j]
    else:
        d = nums[n - 1] - nums[n - 2]
        # print(d)
        # print(n-2)
        if d in d_head_seq_dict:
            for k in d_head_seq_dict[d]:
                if n - 2 == d_head_seq_dict[d][k][-1]:
                    d_head_seq_dict[d][k].append(n - 1)

    print(d_head_seq_dict)
    total = 0

    acc = {}

    def accumulate(x):
        ret = int((x - 2) * (x - 2 + 1) / 2)
        # d=2
        # nd=(x-1)//d
        # while nd>=2:
        #     m=nd*d
        #     ret+=(x-m)
        #     d+=1
        #     nd=(x-1)//d
        return ret

    for d, head_seq in d_head_seq_dict.items():
        for head, seq in head_seq.items():
            m = len(seq)
            if m < 3:
                continue
            if d == 0:
                # 计算C m取3，C m取4 ，一直到C m取l
                # 也就是2的m次方-C m取1-C m取2
                t = 2 ** m - 1 - m - m * (m - 1) / 2
                total += int(t)
            else:
                if m not in acc:
                    acc[m] = accumulate(m)
                total += acc[m]
    # print(acc)
    # print(total)
    return total


print(7 == numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
print(16 == numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]))
print(3 == numberOfArithmeticSlices(nums=[3, -1, -5, -9]))
print(2 == numberOfArithmeticSlices(nums=[2, 2, 3, 4]))
print(4 == numberOfArithmeticSlices(nums=[0, 1, 2, 2, 2, ]))

"""
446. 等差数列划分 II - 子序列
给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。

如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。

例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
再例如，[1, 1, 2, 5, 7] 不是等差序列。
数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。

例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
题目数据保证答案是一个 32-bit 整数。

 

示例 1：

输入：nums = [2,4,6,8,10]
输出：7
解释：所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
示例 2：

输入：nums = [7,7,7,7,7]
输出：16
解释：数组中的任意子序列都是等差子序列。
 

提示：

1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1

"""
