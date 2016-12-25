import functools

grid = []
size = 20
for grid_i in range(size):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
values = []
for i in range(size):
    for j in range(size):
        # print("\nrow", i, "col", j)
        if j < 17:
            # print("going right")
            values.append(functools.reduce(lambda a, b: a * b, [grid[i][j + k] for k in range(4)]))
            if i > 2:
                # print("going right up")
                values.append(functools.reduce(lambda a, b: a * b, [grid[i - k][j + k] for k in range(4)]))
        if i < 17:
            # print("going down")
            values.append(functools.reduce(lambda a, b: a * b, [grid[i + k][j] for k in range(4)]))
            if j > 2:
                # print("going left down")
                values.append(functools.reduce(lambda a, b: a * b, [grid[i + k][j - k] for k in range(4)]))
        if i < 17 and j < 17:
            # print("going right down")
            values.append(functools.reduce(lambda a, b: a * b, [grid[i + k][j + k] for k in range(4)]))
        if i > 2 and j > 2:
            # print("going left down")
            values.append(functools.reduce(lambda a, b: a * b, [grid[i - k][j - k] for k in range(4)]))
print(max(values))
