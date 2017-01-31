# Algorithm:
# 1. Get all abundant numbers
# 2. Add all to get sums and mark the corresponding array to being abundant sum
# 3. The left out are non-abundant, add them

from utils import sieve_of_eratosthenes

MAX = 100  # No number over MAX is abundant
abundant_array = [0] * MAX

primes = sieve_of_eratosthenes.get_primes(MAX)


def flip(position):
    """This function flips the but in the abundant array"""
    position -= 1
    abundant_array[position] = 0 if abundant_array[position] else 1


def get_factor(n):
    """Returns the factors of the number n"""

    factors = [1]
    sqrt = (n ** 0.5) + 1
    for prime in primes:
        if prime >= sqrt:
            break
        if n % prime == 0:
            factors.append(prime)
            factors.append(n // prime)

    return factors


def is_abundant(n):
    """Checks if a number is abundant or deficient.
    Returns 1 for abundant and 0 for deficient"""

    factors = get_factor(n)
    if sum(factors) > n:
        print("sum of factors for", n, sum(factors))
        return True
    else:
        return False


flip(12)  # Because 12 is the smallest abundant number
for i in range(13, MAX):
    abundant_array[i] = 1 if is_abundant(i) else 0
