# 688. 骑士在棋盘上的概率
# https://leetcode-cn.com/problems/knight-probability-in-chessboard/

from collections import deque


# BFS
# class Solution:
#     def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
#         Dirs = [(-1, -2), (1, -2),
#                 (-2, -1), (2, -1),
#                 (-2, 1), (2, 1),
#                 (-1, 2), (1, 2)]
#         q = deque()
#         q.append((row, column, k))
#         cnt = 0
#         while q:
#             r, c, kk = q.popleft()
#             # # 取出kk==0，cnt+1
#             # # 也就是，走到最后一步再计数
#             # if kk == 0:
#             #     cnt += 1
#             #     continue
#             # for x, y in Dirs:
#             #     if 0 <= r + x < n and 0 <= c + y < n:
#             #         q.append((r + x, c + y, kk - 1))
#
#         return cnt / pow(8, k)

# DP
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        Dirs = [(-1, -2), (1, -2),
                (-2, -1), (2, -1),
                (-2, 1), (2, 1),
                (-1, 2), (1, 2)]
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1
        for step in range(k):
            for i in range(n):
                for j in range(n):
                    if dp[step][i][j] > 0:
                        for di, dj in Dirs:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                # dp[step+1][ni][nj]+=1
                                dp[step + 1][ni][nj] += dp[step][i][j]
        cnt = 0
        for i in range(n):
            cnt += sum(dp[-1][i])
        return cnt / pow(8, k)


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        for step in range(k + 1):
            for i in range(n):
                for j in range(n):
                    if step == 0:
                        dp[step][i][j] = 1
                    else:
                        for di, dj in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                dp[step][i][j] += dp[step - 1][ni][nj] / 8
        return dp[k][row][column]


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/knight-probability-in-chessboard/solution/qi-shi-zai-qi-pan-shang-de-gai-lu-by-lee-2qhk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        Dirs = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2))
        dp = [[[0] * (n + 4) for _ in range(n + 4)] for _ in range(2)]
        for i in range(2, 2 + n):
            for j in range(2, 2 + n):
                dp[0][i][j] = 1
        for step in range(1, k + 1):
            for i in range(2, 2 + n):
                for j in range(2, 2 + n):
                    dp[step % 2][i][j] = 0
                    for di, dj in Dirs:
                        ni, nj = i + di, j + dj
                        dp[step % 2][i][j] += dp[1 - step % 2][ni][nj] / 8
        return dp[k % 2][row + 2][column + 2]


examples = [
    [dict(n=3, k=2, row=0, column=0), 0.0625],
    [dict(n=1, k=0, row=0, column=0), 1.0],
    [dict(n=8, k=30, row=6, column=4), 0.0],
    [dict(n=3, k=3, row=0, column=0), 0.01562],
    [dict(n=3, k=1, row=0, column=0), 0.25]
]
solution = Solution()
for data, ans in examples:
    print(solution.knightProbability(**data), ans)
