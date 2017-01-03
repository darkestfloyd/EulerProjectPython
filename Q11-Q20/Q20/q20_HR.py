import functools
import math


def run(n=100):
    fact = str(math.factorial(n))
    print(
        functools.reduce(
            lambda x, y: x + y,
            [int(i) for i in fact]
        )
    )
    return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
