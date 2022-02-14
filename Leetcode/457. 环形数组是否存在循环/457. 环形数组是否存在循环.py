# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:15:07 2021

@author: 11200
"""


def circularArrayLoop(nums):
    l = len(nums)
    # print()
    # print(nums)
    forward = {}
    # 以字典的形式记录nums里下标为k的元素的下一步的坐标v
    # 同时过滤1.这两个数符号不同的情况，满足题目全正或全负的要求
    # 2.k与v相同的情况，以满足题目中循环长度大于1的要求
    for k in range(l):
        v = (k + nums[k]) % l
        if nums[k] * nums[v] > 0:
            if k != v:
                forward[k] = v

    # print(forward)
    # 遍历所有可以作为起点的下标
    for k in list(forward.keys()):
        # 如果这个下标已经被pop，就continue
        if k not in forward:
            continue
        # 记录走过的步骤，初始为空
        steps = []
        # 用于记录下一个的下标，初始是k
        next_ = k
        # print(forward)
        while 1:
            steps.append(next_)
            next_ = forward[next_]
            # 如果下一步已经再记录当中，则说明已经有了循环
            if next_ in steps:
                return True
            # 如果下一步走不了，则将目前所经过的下标删除，并退出while
            if next_ not in forward:
                for s in steps:
                    forward.pop(s)
                break
    # 遍历玩所有仍然没有return True ，那就return
    else:
        return False


"""
def circularArrayLoop(nums):
    l = len(nums)
    # print()
    # print(nums)
    forward_1 = []
    forward_2 = []
    # 以两个列表的形式分别记录nums里下标为k的元素的下一步的坐标v
    # 同时过滤1.这两个数符号不同的情况，满足题目全正或全负的要求
    # 2.k与v相同的情况，以满足题目中循环长度大于1的要求
    for k in range(l):
        v = (k+nums[k]) % l
        if nums[k] * nums[v] > 0:
            if k != v:
                forward_1.append(k)
                forward_2.append(v)

    #print(forward_1)
    #print(forward_2)
    # 遍历所有可以作为起点的下标
    for k in range(len(forward_1)):
        # 如果这个下标已经被pop，就continue
        if forward_1[k] == -1:
            continue
        # 记录走过的步骤，初始为空
        steps = []
        # 用于记录下一个的下标，初始是k
        idx = k
        #print(forward_1)
        #print(forward_2)
        while 1:
            steps.append(idx)
            next_ = forward_2[idx]
            
            # 如果下一步走不了，则将目前所经过的下标删除，并退出while
            if next_ not in forward_1:
                for s in steps:
                    forward_1[s] = forward_2[s] = -1
                break
            else:
                idx=forward_1.index(next_)
                # 如果下一步已经再记录当中，则说明已经有了循环
                if idx in steps:
                    return True
    # 遍历玩所有仍然没有return True ，那就return
    else:
        return False

"""

"""
def circularArrayLoop(nums):
    n = len(nums)

    def next(cur):
        return (cur+nums[cur]) % n
    
    for i, num in enumerate(nums):
        if num == 0:
            continue
        slow, fast = i, next(i)
        while nums[slow]*nums[fast] > 0 and nums[slow]*nums[next(fast)] > 0:
            if slow == fast:
                if slow == next(slow):
                    break
                return True
            slow = next(slow)
            fast = next(next(fast))
        add = i
        while nums[add]*nums[next(add)] > 0:
            nums[add] = 0
            add = next(add)
    return False

"""

print(False == circularArrayLoop(nums=[2, -1, 1, -2, -2]))
print(False == circularArrayLoop(nums=[2, 2, 2, 2, 2, 4, 7]))
print(False == circularArrayLoop(nums=[-1, -2, -3, -4, -5]))
print(True == circularArrayLoop(nums=[2, -1, 1, 2, 2]))
print(False == circularArrayLoop(nums=[-1, 2]))
print(False == circularArrayLoop(nums=[-2, 1, -1, -2, -2]))

"""
457. 环形数组是否存在循环
存在一个不含 0 的 环形 数组 nums ，每个 nums[i] 都表示位于下标 i 的角色应该向前或向后移动的下标个数：

如果 nums[i] 是正数，向前 移动 nums[i] 步
如果 nums[i] 是负数，向后 移动 nums[i] 步
因为数组是 环形 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。

数组中的 循环 由长度为 k 的下标序列 seq ：

遵循上述移动规则将导致重复下标序列 seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
所有 nums[seq[j]] 应当不是 全正 就是 全负
k > 1
如果 nums 中存在循环，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [2,-1,1,2,2]
输出：true
解释：存在循环，按下标 0 -> 2 -> 3 -> 0 。循环长度为 3 。
示例 2：

输入：nums = [-1,2]
输出：false
解释：按下标 1 -> 1 -> 1 ... 的运动无法构成循环，因为循环的长度为 1 。根据定义，循环的长度必须大于 1 。
示例 3:

输入：nums = [-2,1,-1,-2,-2]
输出：false
解释：按下标 1 -> 2 -> 1 -> ... 的运动无法构成循环，因为 nums[1] 是正数，而 nums[2] 是负数。
所有 nums[seq[j]] 应当不是全正就是全负。
 

提示：

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
nums[i] != 0
"""
