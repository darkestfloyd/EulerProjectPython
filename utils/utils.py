def get_factor(n):
    """Returns the factors of the number n"""

    primes = get_primes(n)
    factors = [1]
    sqrt = (n ** 0.5) + 1
    for prime in primes:
        if prime >= sqrt:
            break
        if n % prime == 0:
            factors.append(prime)
            factors.append(n // prime)

    return factors


def get_primes(limit, return_type=1):
    """Returns primes upto limit
    return_type 1: return list of primes
    return_type 2: return raw list with 1s & 0s"""
    primes = [1] * (limit + 1)

    primes[0] = primes[1] = 0
    sqrt = int(limit ** 0.5)
    for num in range(2, sqrt + 1):
        if primes[num] == 0:
            continue
        for x in range(num ** 2, limit + 1, num):
            primes[x] = 0

    if return_type == 2:
        return primes
    prime_list = []
    for index, prime in enumerate(primes):
        if prime == 1:
            prime_list.append(index)

    return prime_list
