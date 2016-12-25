import functools

for n in range(1, 36):
    upper = n * (n + 1) // 2
    factors = len(set(functools.reduce(list.__add__, ([i, upper // i] for i in range(1, int(upper ** 0.5) + 1)))))
    print(upper, factors)
