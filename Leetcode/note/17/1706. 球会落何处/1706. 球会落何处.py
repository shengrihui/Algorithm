# 1706. 球会落何处
# https://leetcode-cn.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid):
        m, n = len(grid), len(grid[0])

        def DFS(row, col):
            if row == m:
                return col
            if grid[row][col] == 1:
                if col == n - 1 or grid[row][col + 1] == -1:
                    return -1
                if grid[row][col + 1] == 1:
                    return DFS(row + 1, col + 1)
            elif grid[row][col] == -1:
                if col == 0 or grid[row][col - 1] == 1:
                    return -1
                if grid[row][col - 1] == -1:
                    return DFS(row + 1, col - 1)

        return [DFS(0, i) for i in range(n)]


examples = [
    [dict(grid=[[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]),
     [1, -1, -1, -1, -1]],
    [dict(grid=[[-1]]), [-1]],
    [dict(grid=[[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]),
     [0, 1, 2, 3, 4, -1]],
    [dict(grid=[[1]]), [-1]]
]

solution = Solution()
for data, ans in examples:
    r = solution.findBall(**data)
    print(r)
    print(ans, r == ans)
