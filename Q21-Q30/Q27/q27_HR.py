pn = 10000
N = int(input().strip())
sieve = [True] * pn


def get_primes():
    global sieve
    sqrt = int(pn ** 0.5)
    sieve[0] = sieve[1] = False
    for x in range(2, sqrt + 1):
        if sieve[x]:
            for t in range(x * x, pn, x):
                sieve[t] = False
    return [x for x in range(pn) if sieve[x]]


primes = get_primes()


def is_prime(n):
    global sieve
    if n < 10000:
        return sieve[n]
    for t in primes:
        if n % t == 0:
            return False
    primes.append(n)
    return True


n_a, n_b = 0, 0
max_prime = 0
if N % 2 == 0:
    n_s, n_e = -(N - 1), N + 1
else:
    n_s, n_e = -N, N
for a in range(n_s, n_e, 2):
    if a == 0:
        continue
    for b in range(n_s, n_e, 2):
        if b == 0:
            continue
        if not is_prime(b):
            continue
        n = 0
        while is_prime(abs(n ** 2 + a * n + b)):
            n += 1
        if n > max_prime:
            max_prime = n
            n_a, n_b = a, b

print(n_a, n_b)
