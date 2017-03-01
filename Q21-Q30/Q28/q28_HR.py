t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    N = 2 * (n - 1) + 1

    steps = 1
    _sum = 1
    _n = 1
    count = 1

    while count < N:
        _sum += 2 * _n + 1
        if count % 4 == 0:
            steps += 1
        _n += steps
        count += 1

    print(_sum % 1000000007)
