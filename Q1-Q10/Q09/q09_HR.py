def run(n):
    run.nmax = 0
    for a in range(1, n // 2):
        b = (a ** 2 - (a - n) ** 2) // (2 * (a - n))  # derived using a^2 + b^2 = N - a - b
        c = n - a - b
        if not (a < b < c):
            continue
        if a + b + c == n and a ** 2 + b ** 2 == c ** 2:
            if a * b * c > run.nmax:
                run.nmax = a * b * c
    if run.nmax == 0:
        print(-1)
    else:
        print(run.nmax)


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
