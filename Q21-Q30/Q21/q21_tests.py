# There are 13 pairs under 10^5
# 1 220 284
# 2 1184 1210
# 3 2620 2924
# 4 5020 5564
# 5 6232 6368
# 6 10744 10856
# 7 12285 14595
# 8 17296 18416
# 9 63020 76084
# 10 66928 66992
# 11 67095 71145
# 12 69615 87633
# 13 79750 88730


def sum_of_divisors(n):
    nsum = 0
    sqrt = int(n ** 0.5)
    for x in range(2, sqrt + 1):
        if n % x == 0:
            nsum += x
            if x != sqrt:
                nsum += n // x
    return nsum + 1


num = 0
for a in range(100000):
    b = sum_of_divisors(a)
    if b > a:
        c = sum_of_divisors(b)
        if c == a:
            print(num, a, b)
            num += 1
