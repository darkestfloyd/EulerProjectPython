# Algorithm:
# 1. Get all abundant numbers
# 2. Add all to get sums and mark the corresponding array to being abundant sum
# 3. The left out are non-abundant, add them

from utils import utils

MAX = 100  # No number over MAX is abundant
abundant_array = [12]
primes = utils.get_primes(MAX, return_type=1)


def is_abundant(n):
    """Checks if a number is abundant or deficient.
    Returns 1 for abundant and 0 for deficient"""

    factors = utils.get_factors(n, with_upper=False, with_1=True)
    if sum(factors) >= n:
        print("sum of factors for", n, sum(factors))
        return True
    else:
        return False


for i in range(13, MAX + 1):
    if is_abundant(i):
        abundant_array.append(i)

print(abundant_array)

# SUM = MAX * (MAX + 1) // 2
# for index1, num1 in enumerate(abundant_array):
#     for index2, num2 in enumerate(abundant_array):
#         if index2 < index1:
#             continue
#         else:
#             ab_sum = num1 + num2
#             if ab_sum < MAX:
#                 print(num1, "+", num2, "=", num1 + num2)
#                 SUM -= ab_sum
# print(SUM)
