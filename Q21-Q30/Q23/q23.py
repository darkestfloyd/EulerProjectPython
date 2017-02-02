# Algorithm:
# 1. Get all abundant numbers
# 2. Add all to get sums and mark the corresponding array to being abundant sum
# 3. The left out are non-abundant, add them

from utils import Euler

MAX, SUM = 30, 0

abundant_numbers = set()

for n in range(1, MAX + 1):
    if Euler.sum_of_divisors(n, True) > n:
        abundant_numbers.add(n)

print(abundant_numbers)
