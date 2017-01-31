# Prints the array of primes till limit


def get_primes(limit):
    primes = [1] * (limit + 1)

    primes[0] = primes[1] = 0
    sqrt = int(limit ** 0.5)
    for num in range(2, sqrt + 1):
        if primes[num] == 0:
            continue
        for x in range(num ** 2, limit + 1, num):
            primes[x] = 0

    prime_list = []
    for index, prime in enumerate(primes):
        if prime == 1:
            prime_list.append(index)

    return prime_list
