import math


def get_prime_factors(n):
    """
    Returns dictionary of prime factors. {factor: count}

    :param n: the number
    """

    temp_n = n
    factors = dict()
    sqrt = int(math.sqrt(n))
    start, steps = [3, 2] if n % 2 else [2, 1]
    for num in range(start, sqrt + 1, steps):
        if temp_n % num == 0:
            count = 0
            while temp_n % num == 0:
                temp_n /= num
                count += 1
            factors[num] = count

    return factors


def get_factors(n, proper_divisors=False, sort=True):
    """
    Returns factors of n

    :param n: the number
    :param proper_divisors: if True, returns only proper factors
    :param sort: if True, factors are sorted
    """

    factors = {1}
    sqrt = int(n ** 0.5)
    start, steps = [3, 2] if n % 2 else [2, 1]
    for num in range(start, sqrt + 1, steps):
        if n % num == 0:
            factors.add(num)
            factors.add(n // num)

    if not proper_divisors:
        factors.add(n)

    if sort:
        return sorted(factors)
    else:
        return factors


def sum_of_divisors(n, proper_divisors_only=False):
    """
    Returns sum of divisors of n

    :param n: the number
    :param proper_divisors_only: if True, returns sum of proper divisors
    """
    return sum(get_factors(n, proper_divisors_only, sort=False))


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
