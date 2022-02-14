from collections import deque


class Solution:
    def numEnclaves(self, grid) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        q = deque()
        s = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                q.append((i, j))
                flag = False
                while q:
                    p = q.popleft()
                    for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
                        x, y = p[0] + dx, p[1] + dy
                        if x < 0 or y < 0 or x >= m or y >= n:
                            continue
                        if grid[x][y] == 1:
                            if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                                flag = True
                                break
                            if (x, y) not in s:
                                q.append((x, y))
                                s.add((x, y))

                    if flag:
                        break
                if not flag:
                    ans += 1
                q.clear()
                s.clear()
        return ans


examples = [
    [[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 3],
    [[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]], 0]
]

solution = Solution()
for data, ans in examples:
    print(solution.numEnclaves(data), ans)

"""

1020.
飞地的数量
给你一个大小为
m
x
n
的二进制矩阵
grid ，其中
0
表示一个海洋单元格、1
表示一个陆地单元格。

一次
移动
是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过
grid
的边界。

返回网格中
无法
在任意次数的移动中离开网格边界的陆地单元格的数量。



示例
1：


输入：grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
输出：3
解释：有三个
1
被
0
包围。一个
1
没有被包围，因为它在边界上。
示例
2：


输入：grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
输出：0
解释：所有
1
都在边界上或可以到达边界。


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j]
的值为
0
或
1
"""
