# answer - 4782

digits = 1000
F = [1, 1]


def fib(n):
    fsum = F[n - 1] + F[n - 2]
    F.append(fsum)
    return fsum


f = 0
counter = 2
while f < 10 ** (digits - 1):
    f = fib(counter)
    counter += 1

print(counter)
