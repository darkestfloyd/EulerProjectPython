def run(nmax):
    largest = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            prod = i * j
            if nmax > prod > largest and str(prod)[::-1] == str(prod):
                largest = prod
    print(largest)
    return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
