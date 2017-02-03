digits = 3

F = [0, 1, 1]


def fib(n):
    fsum = F[n - 1] + F[n - 2]
    F.append(fsum)
    return fsum


f = 0
counter = 3
while f < 10 ** (digits - 1):
    f = fib(counter)
    counter += 1

print(F)
