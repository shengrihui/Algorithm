properties = [[1, 5], [10, 4], [10, 5], [4, 3]]
properties.sort(key=lambda x: (-x[0], x[1]))

print(properties)
