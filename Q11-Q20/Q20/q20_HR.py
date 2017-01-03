import functools
import math


def run(n=100):
    """Returns the sum of the digits in factorial of a number"""
    print(
        functools.reduce(
            lambda x, y: x + y,
            [int(i) for i in str(math.factorial(n))]
        )
    )
    return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
