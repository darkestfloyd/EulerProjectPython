def sum_of_divisors(n):
    nsum = 0
    sqrt = int(n ** 0.5)
    for x in range(2, sqrt + 1):
        if n % x == 0:
            nsum += x
            if x != sqrt:
                nsum += n // x
    return nsum + 1


def run(nmax=10000):
    amicable_sum = 0
    for a in range(2, nmax):
        b = sum_of_divisors(a)
        if b > a:
            c = sum_of_divisors(b)
            if c == a:
                amicable_sum += a
                if b <= nmax:
                    amicable_sum += b
    print(amicable_sum)
    return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
