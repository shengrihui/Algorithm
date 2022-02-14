# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:37:38 2021

@author: 11200
"""
'''
给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

 

示例 1：

输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。
示例 2：

输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-and-earn
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def answer(nums):
    maxVal = max(nums)
    total = [0] * (maxVal + 1)
    for val in nums:
        total[val] += val

    def rob(nums):
        size = len(nums)
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        return second

    return rob(total)


import time

print(answer([1]))
a = time.time()
for i in range(1000):
    answer(
        [12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91,
         85, 14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13,
         60, 57, 91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1,
         90, 63, 55, 64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93])
b = time.time()
t1 = b - a
print(answer(
    [12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91, 85,
     14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13, 60, 57,
     91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1, 90, 63, 55,
     64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]))

print()


def func(nums):
    # 取数组中的最大值
    max_num = max(nums)
    # total是每个数当下标对应的总和
    # +1是因为最大值也要取到
    total = [i * nums.count(i) for i in range(max_num + 1)]
    # print(total)

    # size表示total长度，
    # 或者有多少个数+1（0在第一个，但点数从1开始）
    # size=max_num+1
    size = len(total)

    max_dict = {}
    '''
    def maxf(sz):
        #print(sz)
        if sz==1:
            return total[0]
        elif sz==2:
            return max(total[0],total[1])
        elif sz==3:
            a=total[0]+total[2]
            return max(a,total[1])
        elif sz==4:
            a=total[3]+maxf(2)
            b=total[2]+total[0]
            return max(a,b)
        elif sz==5:
            a=total[4]+maxf(3)
            b=total[3]+maxf(2)
            return max(a,b)
        else:
            a=total[sz-1]+maxf(sz-2)
            b=total[sz-2]+maxf(sz-3)
            return max(a,b)
    '''
    '''
    max_dict[1]=max_dict.get(1,0)+total[1]
    max_dict[2]=max_dict.get(2,0)+max(total[1],total[2])
    max_dict[3]=max_dict.get(3,0)+max(total[1]+total[3],total[2])
    max_dict[4]=max_dict.get(4,0)+max(max_dict[2]+total[4],max_dict[1]+total[3])
    max_dict[5]=max_dict.get(5,0)+max(max_dict[3]+total[5],max_dict[2]+total[4])
    '''
    for sz in range(1, max_num + 1):

        if sz == 1:
            max_dict[1] = max_dict.get(1, 0) + total[1]
        elif sz == 2:
            max_dict[2] = max_dict.get(2, 0) + max(total[1], total[2])
        elif sz == 3:
            max_dict[3] = max_dict.get(3, 0) + max(total[1] + total[3], total[2])
        else:
            max_dict[sz] = max_dict.get(sz, 0) + max(max_dict[sz - 2] + total[sz], max_dict[sz - 3] + total[sz - 1])

    # print(max_dict)
    return max_dict[max_num]


print(func([2, 3, 4]))
print(func([2, 2, 3, 3, 3, 4]))
a = time.time()
for i in range(1000):
    func(
        [12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91,
         85, 14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13,
         60, 57, 91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1,
         90, 63, 55, 64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93])
b = time.time()
t2 = b - a
print(func(
    [12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91, 85,
     14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13, 60, 57,
     91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1, 90, 63, 55,
     64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]))


def func2(nums):
    # 取数组中的最大值
    max_num = max(nums)
    # total是每个数当下标对应的总和
    # +1是因为最大值也要取到
    # total=[ i*nums.count(i) for i in range(max_num+1)]
    total = {i: i * nums.count(i) for i in range(max_num + 1)}
    # print(total)

    # size表示total长度，
    # 或者有多少个数+1（0在第一个，但点数从1开始）
    # size=max_num+1
    size = len(total)

    pre_3, pre_2, max_i = total[0], total[1], total[2]
    # print(pre_3,pre_2,max_i)
    for i in range(3, size + 1):
        pre_3, pre_2, max_i = pre_2, max_i, max(pre_3 + total[i - 1], pre_2 + total[i])

    return max_i


print(func2([2, 3, 4]))
print(func2([2, 2, 3, 3, 3, 4]))
a = time.time()
# for i in  range(1000):
# func2([12,32,93,17,100,72,40,71,37,92,58,34,29,78,11,84,77,90,92,35,12,5,27,92,91,23,65,91,85,14,42,28,80,85,38,71,62,82,66,3,33,33,55,60,48,78,63,11,20,51,78,42,37,21,100,13,60,57,91,53,49,15,45,19,51,2,96,22,32,2,46,62,58,11,29,6,74,38,70,97,4,22,76,19,1,90,63,55,64,44,90,51,36,16,65,95,64,59,53,93])
b = time.time()
t3 = b - a
print(func2(
    [12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91, 85,
     14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13, 60, 57,
     91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1, 90, 63, 55,
     64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]))

print(t1)
print(t2)
