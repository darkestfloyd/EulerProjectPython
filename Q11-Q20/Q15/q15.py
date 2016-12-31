import os
import time

print("Running", os.path.basename(__file__))


def run(n=20, m=20):
    mat = [[0] * n] * m
    mat[n - 1][m - 1] = 1
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            ip = jp = 0
            if j == m - 1:
                jp = 1
            else:
                jp = mat[i][j + 1]
            if i == n - 1:
                ip = 1
            else:
                ip = mat[i + 1][j]
            mat[i][j] = ip + jp
    print(mat[0][0])
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
