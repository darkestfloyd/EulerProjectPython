# only check till squared root of num, deduce the rest
# reduced number of functions required, code runs faster with new optimizations

import os
import time

print("Running", os.path.basename(__file__))

prime_list = []


def get_largest(num, prime_check=False):
    increment = 1
    sqrt = int(num ** 0.5)
    if num % 2 == 0:
        if prime_check:
            return False
        else:
            increment = 2
    for i in range(3, sqrt, increment):
        if num % i == 0:
            if prime_check:
                return False
            elif i not in prime_list and get_largest(i, True):
                prime_list.append(i)

    if prime_check: return True
    return max(prime_list)


def run():
    num = 600851475143
    print(get_largest(num))
    return


start_time = time.time()
for i in range(100):
    run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
