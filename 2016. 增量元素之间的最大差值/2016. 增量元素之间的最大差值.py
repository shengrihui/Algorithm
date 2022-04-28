# 2016. 增量元素之间的最大差值
# https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements/

class Solution:
    def maximumDifference(self, nums) -> int:
        ans = -1
        n = len(nums)
        for j in range(1, n):
            for i in range(j):
                if nums[i] < nums[j]:
                    ans = max(ans, nums[j] - nums[i])
        return ans


class Solution:
    def maximumDifference(self, nums) -> int:
        ans = -1
        n = len(nums)
        permin = nums[0]
        for i in range(1, n):
            if nums[i] > permin:
                ans = max(ans, nums[i] - permin)
            else:
                permin = nums[i]
        return ans


examples = [
    [[7, 1, 5, 4], 4],
    [[9, 4, 3, 2], -1],
    [[1, 5, 2, 10], 9]
]

solution = Solution()
for data, ans in examples:
    print(solution.maximumDifference(data), ans)
