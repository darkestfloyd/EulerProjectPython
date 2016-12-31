def run(n=20, m=20):
    mat = [[0 for x in range(m)] for y in range(n)]
    mat[n - 1][m - 1] = 1
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
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


t = int(input().strip())
for counter in range(t):
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    run(n, m)
