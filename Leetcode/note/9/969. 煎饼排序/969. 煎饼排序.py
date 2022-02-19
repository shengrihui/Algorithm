# 969. 煎饼排序
# https://leetcode-cn.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr):
        ans = []
        n = len(arr)
        m = 0
        while m < n:
            max_i = 0
            for i in range(n - m):
                if arr[i] > arr[max_i]:
                    max_i = i
            arr = arr[max_i::-1] + arr[max_i + 1:]
            arr = arr[n - m - 1::-1] + arr[n - m::]
            m += 1
            ans.append(max_i + 1)
            ans.append(n - m + 1)
        return ans


class Solution:
    def pancakeSort(self, arr):
        ans = []
        for n in range(len(arr), 0, -1):
            k = 0
            for i in range(n):
                if arr[i] > arr[k]:
                    k = i
            if k == n - 1:
                continue
            i, j = 0, k
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i + 1, j - 1
            i, j = 0, n - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i + 1, j - 1
            ans.append(k + 1)
            ans.append(n)
        return ans


solution = Solution()
f = solution.pancakeSort
print([3, 2, 4, 1])
print(f([3, 2, 4, 1]))
