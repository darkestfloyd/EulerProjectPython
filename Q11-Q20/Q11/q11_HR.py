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
            values.append(grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3])
            if i > 2:
                # print("going right up")
                values.append(grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3])
        if i < 17:
            # print("going down")
            values.append(grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j])
            if j > 2:
                # print("going left down")
                values.append(grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3])
print(max(values))
