# Leetcode
# 6. Z 字形变换
# https://leetcode-cn.com/problems/zigzag-conversion/

from typing import *
from collections import *
import numpy as np


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]

        i = 0
        r = 0
        while i < len(s):
            ans[r].append(s[i])
            if r == 0:
                dr = 1
            elif r == numRows - 1:
                dr = -1
            if 0 == numRows - 1:
                dr = 0
            i += 1
            r += dr
        return ''.join([''.join(row) for row in ans])
