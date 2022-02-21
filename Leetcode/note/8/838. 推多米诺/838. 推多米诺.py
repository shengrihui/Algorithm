# 838. 推多米诺
# https://leetcode-cn.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = list(dominoes)
        l = r = 0
        while r < len(dominoes):
            if s[r] == ".":
                r += 1
            elif s[r] == "R":
                l = r
                r += 1
                while r < len(s) and s[r] != "R":
                    if s[r] == ".":
                        r += 1
                    elif s[r] == "L":
                        i, j = l + 1, r - 1
                        while i < j:
                            s[i] = "R"
                            s[j] = "L"
                            i, j = i + 1, j - 1
                        r += 1
                        l = r
                        break
                else:
                    for i in range(l, r):
                        s[i] = "R"

            elif s[r] == "L":
                for i in range(l, r):
                    s[i] = "L"
                r += 1
        return "".join(s)


# BFS
from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        q = deque()
        n = len(dominoes)
        time = [-1] * n
        force = [[] for _ in range(n)]
        for i, f in enumerate(dominoes):
            if f != ".":
                q.append(i)
                force[i].append(f)
                time[i] = 0
        res = ["." for _ in range(n)]
        while q:
            i = q.popleft()
            if len(force[i]) == 1:
                res[i] = f = force[i][0]
                ni = i + 1 if f == "R" else i - 1
                t = time[i]
                if 0 <= ni < 0:
                    if time[ni] == -1:
                        q.append(ni)
                        force[ni].append(f)
                        time[ni] = t + 1
                    elif time[ni] == t + 1:
                        force[ni].append(f)
        return ''.join(res)


examples = [
    [".L.R...LR..L..", "LL.RR.LLRRLL.."],
    ["RR.L", "RR.L"],
    ["L.....RR.RL.....L.R.", "L.....RRRRLLLLLLL.RR"],
    [".L.R...LR..L..", "LL.RR.LLRRLL.."]
]
solution = Solution()
for data, ans in examples:
    print(data)
    print(solution.pushDominoes(data))
    print(ans)
