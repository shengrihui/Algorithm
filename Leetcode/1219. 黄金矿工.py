List = list


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        def DFS(x, y, s):
            nonlocal ans
            s = s + grid[x][y]
            ans = max(ans, s)
            r = grid[x][y]
            grid[x][y] = 0
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and grid[i][j] > 0:
                    DFS(i, j, s)
            grid[x][y] = r

        for x in range(m):
            for y in range(n):
                if grid[x][y] > 0:
                    DFS(x, y, 0)
        return ans


examples = [
    ([[0, 6, 0], [5, 8, 7], [0, 9, 0]], 24),
    ([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]], 28)
]

solution = Solution()
for data, ans in examples:
    print(solution.getMaximumGold(data), ans)
