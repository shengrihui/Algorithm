# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 00:07:52 2021

@author: 11200
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n
        ret[0] = nums[0]
        for i in range(1, n):
            ret[i] = nums[i] + ret[i - 1]
        return ret


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums
