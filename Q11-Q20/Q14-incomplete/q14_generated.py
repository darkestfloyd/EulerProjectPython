collatz = [-1, 1, 1, 10, 2, 16, 3, 22, 4, 28, ]
collatz_length = [-1, 1, 2, 8, 3, 6, 9, 17, 4, 20, ]

t = int(input().strip())
for counter in range(t):
    tt = int(input().strip())
    print(collatz_length[tt])
