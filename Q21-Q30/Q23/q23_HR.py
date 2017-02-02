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


MAX = 100000
abundant_numbers = set()

for num in range(12, MAX + 1):
    if sum_of_divisors(num) > num:
        abundant_numbers.add(num)

t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    for a in abundant_numbers:
        if n - a in abundant_numbers:
            print("YES")
            exit()
    print("NO")
