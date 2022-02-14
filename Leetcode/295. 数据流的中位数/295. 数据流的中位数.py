# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:47:02 2021

@author: 11200
"""


# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """


#     def addNum(self, num: int) -> None:


#     def findMedian(self) -> float:


# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.counter = []

    def addNum(self, num: int) -> None:
        self.counter.append(num)

    def findMedian(self) -> float:
        self.counter.sort()
        n = len(self.counter)
        a = self.counter[(n + 1) // 2 - 1]
        b = self.counter[n // 2 + 1 - 1]
        return float((a + b) / 2)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
