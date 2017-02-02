def get_prime_factor(n, primes):
    """Returns prime factors of the number n"""

    factors = [1]
    sqrt = (n ** 0.5) + 1
    for prime in primes:
        if prime >= sqrt:
            break
        if n % prime == 0:
            factors.append(prime)

    return factors


def get_factors(n, proper_divisors=False):
    """Return factors for number n"""

    factors = [1]
    sqrt = int(n ** 0.5)
    steps = 2 if n % 2 == 1 else 1
    for num in range(1, sqrt):
        num += steps
        if n % num == 0:
            factors.append(num)
            if num ** 2 != n:
                factors.append(n // num)

    if not proper_divisors:
        factors.append(n)

    return sorted(factors)


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
