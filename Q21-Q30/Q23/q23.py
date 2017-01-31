# Algorithm:
# 1. Get all abundant numbers
# 2. Add all to get sums and mark the corresponding array to being abundant sum
# 3. The left out are non-abundant, add them

from utils import utils

MAX = 28123  # No number over MAX is abundant
abundant_array = [12]
has_abundant_sum = [0] * MAX
primes = utils.get_primes(MAX)  # Get all prime numbers under MAX (to calculate factors)


def is_abundant(n):
    """Checks if a number is abundant or deficient.
    Returns 1 for abundant and 0 for deficient"""

    factors = utils.get_factor(n)
    if sum(factors) > n:
        # print("sum of factors for", n, sum(factors))
        return True
    else:
        return False


for i in range(13, MAX):
    if is_abundant(i):
        abundant_array.append(i)

# print("Abundant numbers are:", abundant_array)

# Add all abundant numbers
s = len(abundant_array)
SUM = MAX * (MAX + 1) // 2
print(SUM)
for x in range(s):
    for y in range(x, s):
        ab_sum = abundant_array[x] + abundant_array[y]
        if ab_sum <= MAX:
            SUM -= ab_sum
            # has_abundant_sum[abundant_array[x] + abundant_array[y] - 1] = 1

print(SUM)
