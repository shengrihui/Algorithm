# https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree/
from collections import defaultdict


class Solution:
    def checkWays(self, pairs) -> int:
        adj = defaultdict(set)

        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)
        for x in adj:
            adj[x].add(x)
        for i in adj:
            print(i, adj[i])
        adj = sorted(adj.values(), key=lambda item: len(item))
        n = len(adj)
        if len(adj[-1]) < n:
            return 0
        ans = 1
        print(adj)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if adj[i].issubset(adj[j]):
                    if ans != 2 and adj[i] == adj[j]:
                        ans = 2
                    break
            else:
                return 0
        return ans


from sys import maxsize


class Solution:
    def checkWays(self, pairs) -> int:
        adj = defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)

        # 检测是否存在根节点
        root = next((node for node, neighbours in adj.items() if len(neighbours) == len(adj) - 1), -1)
        # # 没有根节点
        if root == -1:
            return 0

        ans = 1
        for node, neighbours in adj.items():
            if node == root:
                continue

            # # 遍历过程当中当前节点的Degree
            currDegree = len(neighbours)
            parent = -1
            parentDegree = maxsize
            # 根据 degree 的大小找到 node 的父节点 parent
            # # 遍历 adj[node] ,就是和 node 有关系的所有节点
            for neighbour in neighbours:
                # # 找到 node 的可能父节点—— parentDegree >= currDegree
                if currDegree <= len(adj[neighbour]) < parentDegree:
                    parent = neighbour
                    parentDegree = len(adj[neighbour])
            # 检测 neighbours 是否为 adj[parent] 的子集
            # # if parent == -1 or not neighbours.issubset(adj[parent]):
            # # ??
            # if parent == -1 or any(neighbour != parent and neighbour not in adj[parent] for neighbour in neighbours):
            print(neighbours, parent)
            print([neighbour != parent for neighbour in neighbours])
            print([neighbour not in adj[parent] for neighbour in neighbours])
            print([neighbour != parent and neighbour not in adj[parent] for neighbour in neighbours])
            if any(neighbour != parent and neighbour not in adj[parent] for neighbour in neighbours):
                return 0

            if parentDegree == currDegree:
                ans = 2
        return ans


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree/solution/zhong-gou-yi-ke-shu-de-fang-an-shu-by-le-36e1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

examples = [
    [[[1, 2], [2, 3]], 1],
    [[[1, 2], [2, 3], [1, 3]], 2],
    [[[1, 2], [2, 3], [2, 4], [1, 5]], 0],
    [[[3, 4], [2, 3], [4, 5], [2, 4], [2, 5], [1, 5], [1, 4]], 0]
]
solution = Solution()
for data, ans in examples:
    print(solution.checkWays(data), ans)
