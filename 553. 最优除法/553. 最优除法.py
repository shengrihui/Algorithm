# 553. 最优除法
# https://leetcode-cn.com/problems/optimal-division/

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        return str(nums[0]) + ("/" if len(nums) > 1 else "") + ("(" if len(nums) > 2 else "") + "/".join(
            list(map(str, nums[1:]))) + (")" if len(nums) > 2 else "")


class Node:
    def __init__(self):
        self.minVal = 1e4
        self.maxVal = 0
        self.minStr = ""
        self.maxStr = ""


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        dp = [[Node() for _ in range(n)] for _ in range(n)]
        for i, num in enumerate(nums):
            dp[i][i].minVal = num
            dp[i][i].maxVal = num
            dp[i][i].minStr = str(num)
            dp[i][i].maxStr = str(num)
        for i in range(n):
            for j in range(n - i):
                for k in range(j, j + i):
                    if dp[j][j + i].maxVal < dp[j][k].maxVal / dp[k + 1][j + i].minVal:
                        dp[j][j + i].maxVal = dp[j][k].maxVal / dp[k + 1][j + i].minVal
                        if k + 1 == j + i:
                            dp[j][j + i].maxStr = dp[j][k].maxStr + "/" + dp[k + 1][j + i].minStr
                        else:
                            dp[j][j + i].maxStr = dp[j][k].maxStr + "/(" + dp[k + 1][j + i].minStr + ")"
                    if dp[j][j + i].minVal > dp[j][k].minVal / dp[k + 1][j + i].maxVal:
                        dp[j][j + i].minVal = dp[j][k].minVal / dp[k + 1][j + i].maxVal
                        if k + 1 == j + i:
                            dp[j][j + i].minStr = dp[j][k].minStr + "/" + dp[k + 1][j + i].maxStr
                        else:
                            dp[j][j + i].minStr = dp[j][k].minStr + "/(" + dp[k + 1][j + i].maxStr + ")"
        return dp[0][n - 1].maxStr

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/optimal-division/solution/zui-you-chu-fa-by-leetcode-solution-lf4c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
