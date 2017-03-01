t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    _sum = 1

    for x in range(1, ((n - 1) // 2) + 1):
        _sum += 4 * (2 * x + 1) ** 2 - 12 * x

    print(_sum % 1000000007)
