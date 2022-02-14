# class Solution:
#     def gridIllumination(self, n: int, lamps, queries):
#         grid = [[0] * n for _ in range(n)]
#         ans = []
#
#         def turn(r, c, m):
#             for i in range(n):
#                 grid[i][c] += m
#             for i in range(n):
#                 grid[r][i] += m
#             grid[r][c] -= m
#             i, j = r - 1, c - 1
#             while i >= 0 and j >= 0:
#                 grid[i][j] += m
#                 i -= 1
#                 j -= 1
#             i, j = r - 1, c + 1
#             while i >= 0 and j < n:
#                 grid[i][j] += m
#                 i -= 1
#                 j += 1
#             i, j = r + 1, c + 1
#             while i < n and j < n:
#                 grid[i][j] += m
#                 i += 1
#                 j += 1
#             i, j = r + 1, c - 1
#             while i < n and j >= 0:
#                 grid[i][j] += m
#                 i += 1
#                 j -= 1
#
#         for r, c in lamps:
#             turn(r, c, 1)
#
#         for r, c in queries:
#             ans.append(1 if grid[r][c] > 0 else 0)
#             for idx,(i, j) in enumerate(lamps):
#                 if abs(i - r) <= 1 and abs(j - c) <= 1:
#                     if grid[i][j]>0:
#                         turn(i, j, -1)
#                         lamps[idx]=[n+100,n+100]
#
#
#         return ans


class Solution:
    def gridIllumination(self, n: int, lamps, queries):
        from collections import Counter
        # diagonal对角线
        row, col, diagonal, antiDiagnal = Counter(), Counter(), Counter(), Counter()
        # points = set()
        for r, c in lamps:
            # if (r, c) in points:
            #     continue
            row[r] += 1
            col[c] += 1
            # 对角线上的点（c,r)  r=c+b b是截距 所以b=r-c
            diagonal[r - c] += 1
            # (c,r) r=-c+b b=r+c
            antiDiagnal[r + c] += 1
            # points.add((r, c))

        ans = [0] * len(queries)
        for idx, (r, c) in enumerate(queries):
            if row[r] or col[c] or diagonal[r - c] or antiDiagnal[r + c]:
                ans[idx] = 1
            # 灭灯
            # for i in range(r - 1, r + 1 + 1):
            #     for j in range(c - 1, c + 1 + 1):
            # if 0 <= i < n and 0 <= j < n and (i, j) in points:
            for idx_l, (i, j) in enumerate(lamps):
                if abs(i - r) <= 1 and abs(j - c) <= 1:
                    lamps[idx_l] = [-100, -100]
                    row[i] -= 1
                    col[j] -= 1
                    diagonal[i - j] -= 1
                    antiDiagnal[i + j] -= 1
                    # points.remove((i, j))

        return ans


solution = Solution()
f = solution.gridIllumination
examples = [
    [f(n=5, lamps=[[0, 0], [4, 4]], queries=[[1, 1], [1, 0]]), [1, 0]],
    [f(n=5, lamps=[[0, 0], [4, 4]], queries=[[1, 1], [1, 1]]), [1, 1]],
    [f(n=5, lamps=[[0, 0], [0, 4]], queries=[[0, 4], [0, 1], [1, 4]]), [1, 1, 0]],
    [f(5, [[0, 0], [0, 1], [0, 4]], [[0, 0], [0, 1], [0, 2]]), [1, 1, 1]],
    [f(5, [[0, 0], [1, 0]], [[1, 1], [1, 1]]), [1, 0]],
    [f(1, [[0, 0], [0, 0]], [[0, 0], [0, 0]]), [1, 0]]
]
for i, j in examples:
    print(i, j)
