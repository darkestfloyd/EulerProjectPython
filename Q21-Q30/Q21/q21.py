# answer - 31626

import os
import time

print("Running", os.path.basename(__file__))


def sum_of_divisors(n):
    nsum = 0
    sqrt = int(n ** 0.5)
    for x in range(2, sqrt + 1):
        if n % x == 0:
            nsum += x
            if x != sqrt:
                nsum += n // x
    return nsum + 1


def run(nmax=10000):
    amicable_sum = 0
    num_flag = [-1] * nmax
    for a in range(220, nmax):
        b = sum_of_divisors(a)
        num_flag[a] = b
        if b > a:
            c = sum_of_divisors(b)
            if c == a:
                amicable_sum += a + b
            if b <= nmax:
                num_flag[b] = c
    print(amicable_sum)
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
