t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    n //= 2

    prod = 16 * n ** 3 + 30 * n ** 2 + 26 * n + 3
    prod //= 3

    print(round(prod) % 1000000007)
