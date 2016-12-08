def prep(num=1000000):
    primes = [1] * (num + 1)
    primes[0] = primes[1] = 0
    for i in range(1, num + 1):
        if primes[i] == 1:
            for j in range(i * 2, num + 1, i):
                primes[j] = 0
    prime_sum = 0
    for i in range(num + 1):
        if primes[i] == 1:
            prime_sum += i
        primes[i] = prime_sum
    return primes


t = int(input().strip())
sums = prep()
for counter in range(t):
    n = int(input().strip())
    print(sums[n])
