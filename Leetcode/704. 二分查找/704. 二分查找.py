# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:14:01 2021

@author: 11200
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
        else:
            return -1
