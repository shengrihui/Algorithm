# -*- coding: utf-8 -*-
"""
Created on 17:04 

@author: shengrihui
"""
# Leetcode
# 
# 

from typing import *
from collections import *
import numpy as np
import soupsieve


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum, n = 0, len(nums)
        for i in range(n - 1):
            maxVal, minVal = nums[i], nums[i]
            for j in range(i + 1, n):
                if nums[j] > maxVal:
                    maxVal = nums[j]
                if nums[j] < minVal:
                    minVal = nums[j]
                sum += maxVal - minVal
        return sum


examples = [
    [[1, 2, 3], 4],
    [[1, 3, 3], 4],
    [[4,-2,-3,4,1],59]
]

solution = Solution()
for data, ans in examples:
    print(data,solution.subArrayRanges(data), ans)
