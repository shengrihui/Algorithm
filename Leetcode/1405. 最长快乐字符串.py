from sortedcontainers import SortedList

# exit(0)


example = [
    [1, 1, 7],
    [2, 2, 1],
    [7, 1, 0],
    [1, 2, 3],
    [5, 2, 3]
]
solution = Solution()
for data in example:
    print(*data, solution.longestDiverseString(*data))
