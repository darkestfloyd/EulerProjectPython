# Algorithm:
# 1. Get all abundant numbers
# 2. Add all to get sums and mark the corresponding array to being abundant sum
# 3. The left out are non-abundant, add them

from utils import Euler

MAX = 20161  # No number over MAX is abundant
has_abundant_sum = [1] * MAX
primes = Euler.get_primes(MAX, return_type=1)


def is_abundant(n):
    """Checks if a number is abundant or deficient.
    Returns 1 for abundant and 0 for deficient"""

    factors = Euler.get_factors(n, with_upper=False, with_1=True)
    if sum(factors) > n:
        # print("sum of factors for", n, sum(factors))
        return True
    else:
        return False


abundant_array = list(x for x in range(12, MAX + 1) if is_abundant(x))

print(abundant_array)

s = len(abundant_array)
print(s)
for i in range(s):
    for j in range(i, s):
        ab_sum = abundant_array[i] + abundant_array[j]
        if ab_sum <= MAX:
            has_abundant_sum[ab_sum - 1] = 0

# print(has_abundant_sum)
SUM = 0
for x in range(MAX):
    if has_abundant_sum[x] == 0:
        SUM += x

print(SUM)
