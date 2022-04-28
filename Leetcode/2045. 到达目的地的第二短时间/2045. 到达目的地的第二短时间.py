from collections import deque


class Solution:
    def secondMinimum(self, n, edges, time, change) -> int:
        # 构建图
        G = [[] for _ in range(n + 1)]  # 因为顶点的编号从1开始
        for x, y in edges:
            G[x].append(y)
            G[y].append(x)

        # dist[i][0]表示顶点1到i的最短
        # dist[i][1]表示顶点1到i的第二段
        # 所以第二短路径长度结果就是dist[n][1]
        # 初始dist[1][0]=0，其余为inf
        dist = [[float("inf")] * 2 for _ in range(n + 1)]
        dist[1][0] = 0

        # 队列中的每一个元素是一个元组
        # (i,j)表示顶点1到i的路径长度
        q = deque([(1, 0)])

        while dist[n][1] == float("inf"):
            # 顶点编号,路径长度从队列中取出
            v, d = q.popleft()
            d = d + 1
            for j in G[v]:
                if d < dist[j][0]:
                    dist[j][0] = d
                    q.append((j, d))
                if dist[j][0] < d < dist[j][1]:
                    dist[j][1] = d
                    q.append((j, d))

        ans = 0
        for _ in range(dist[n][1]):
            if (i := ans // change) % 2 == 1:
                ans = (i + 1) * change
            ans += time
        return ans


solution = Solution()
print(solution.secondMinimum(n=5, edges=[[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], time=3, change=5), 13)
