# -*- coding: utf-8 -*-
"""
Created on 22:50 

@author: shengrihui
"""
# Leetcode
# 258. 各位相加
# https://leetcode-cn.com/problems/add-digits/

from typing import *
from collections import *
import numpy as np


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            num = sum
        return num

class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1)%9
examples = [
    [0, 0],
    [123, 6],
    [38, 2]
]

solution = Solution()
for data, ans in examples:
    print(data, solution.addDigits(data), ans)
