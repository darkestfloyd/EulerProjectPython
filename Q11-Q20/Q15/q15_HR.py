# score - 100
# ATTENTION!! accepted in python2. python3 wrong answer.
import math

f = math.factorial


def run(n=20, m=20):
    print(int((f(m + n) // (f(m) * f(n))) % 1000000007))
    return


t = int(input().strip())
for counter in range(t):
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    run(n, m)
