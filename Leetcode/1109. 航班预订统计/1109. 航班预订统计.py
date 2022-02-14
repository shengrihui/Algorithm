# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:28:03 2021

@author: 11200
"""


# def corpFlightBookings(bookings, n):
#     answer = [0]*n
#     for f, l, s in bookings:
#         for i in range(f-1, l):
#             answer[i] += s
#     return answer

# def corpFlightBookings(bookings, n):
#     answer = [0]*n
#     for i in range(1, n+1):
#         if i > 1:
#             answer[i-1] += answer[i-2]
#         for f, l, s in bookings:
#             if f == i:
#                 answer[i-1] += s
#                 if l < n:
#                     answer[l] -= s
#     return answer

def corpFlightBookings(bookings, n):
    answer = [0] * n
    for f, l, s in bookings:
        answer[f - 1] += s
        if l < n:
            answer[l] -= s
    # print(answer)
    for i in range(1, n):
        answer[i] += answer[i - 1]
    return answer


print([10, 55, 45, 25, 25], corpFlightBookings(
    bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))

"""
1109. 航班预订统计
这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。

 

示例 1：

输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]
解释：
航班编号        1   2   3   4   5
预订记录 1 ：   10  10
预订记录 2 ：       20  20
预订记录 3 ：       25  25  25  25
总座位数：      10  55  45  25  25
因此，answer = [10,55,45,25,25]
示例 2：

输入：bookings = [[1,2,10],[2,2,15]], n = 2
输出：[10,25]
解释：
航班编号        1   2
预订记录 1 ：   10  10
预订记录 2 ：       15
总座位数：      10  25
因此，answer = [10,25]
 

提示：

1 <= n <= 2 * 104
1 <= bookings.length <= 2 * 104
bookings[i].length == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 104
"""
