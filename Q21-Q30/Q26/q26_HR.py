t = int(input().strip())


def soe(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    sqrt = int(n ** 0.5)
    for p in range(2, sqrt + 1):
        if sieve[p]:
            for x in range(p * p, n, p):
                sieve[x] = False

    return [x for x in range(n) if sieve[x]]


primes = soe(10000)[::-1]
for _ in range(t):
    d = int(input().strip())
    if d < 8:
        print(3)
        continue
    x = 0
    for x in primes:
        if x > d or x < 7:
            continue
        p = 1
        while pow(10, p, x) != 1 and p < x:
            p += 1
        if x - 1 == p:
            break

    print(x)
