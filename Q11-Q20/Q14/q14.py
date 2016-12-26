# answer - 837799

import os
import time

print("Running", os.path.basename(__file__))

collatz_length = {1: 1}


def get_collatz_length(n):
    if n in collatz_length:
        return collatz_length[n]
    else:
        if n % 2 == 0:
            length = get_collatz_length(n // 2)
        else:
            length = get_collatz_length((3 * n) + 1)
        collatz_length[n] = length + 1
        return collatz_length[n]


def run(limit=1000000):
    nmax = 0
    nval = 0
    for n in range(1, limit + 1):
        test_num = get_collatz_length(n)
        if test_num > nmax:
            nmax = test_num
            nval = n
    print(nval, nmax)
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
