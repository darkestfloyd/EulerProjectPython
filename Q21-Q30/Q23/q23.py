# Algorithm:
# 1. Get all abundant numbers
# 2. Add all to get sums and mark the corresponding array to being abundant sum
# 3. The left out are non-abundant, add them

from utils import sieve_of_eratosthenes

MAX = 28123  # No number over MAX is abundant
abundant_array = [12]
has_abundant_sum = [0] * MAX
primes = sieve_of_eratosthenes.get_primes(MAX)  # Get all prime numbers under MAX (to calculate factors)


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
        # print("sum of factors for", n, sum(factors))
        return True
    else:
        return False


for i in range(13, MAX):
    if is_abundant(i):
        abundant_array.append(i)

# Add all abundant numbers
has_abundant_sum[11] = 1  # Because 12 is the smallest abundant number
s = len(abundant_array)
for x in range(s + 1):
    for y in range(x, s + 1):
        has_abundant_sum[x + y - 1] = 1

SUM = 0
for x in range(len(has_abundant_sum)):
    if has_abundant_sum[x] == 1:
        SUM += x

print(SUM)
