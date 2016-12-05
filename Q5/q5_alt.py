# lcm(a, b) = (a * b) / gcd(a, b)

import math
import os
import time

print("Running", os.path.basename(__file__))


def lcm(a, b):
    return int((a * b) / math.gcd(a, b))


def lcm_for_range(counter, multiple, nmax):
    if counter == nmax:
        return multiple
    else:
        return lcm_for_range(counter + 1, lcm(multiple, counter), nmax)


def run(nmax=20):
    # print(lcm_for_range(1, 1, nmax)) # this is a recursive alternative
    multiple = 1
    for i in range(2, nmax + 1):
        multiple = lcm(multiple, i)
    print(multiple)
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
