import math


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


def prime_sieve(n, as_numbers=False):
    """
    Returns primes upto n

    :param n: limit (generates primes till n)
    :param as_numbers: if True, returns list of primes, else returns the sieve
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    sqrt = int(math.sqrt(n))
    for num in range(2, sqrt + 1):
        if sieve[num]:
            for num_pow in range(num ** 2, n + 1, num):
                sieve[num_pow] = False

    if not as_numbers:
        return sieve
    else:
        return [i for i, x in enumerate(sieve) if x]
