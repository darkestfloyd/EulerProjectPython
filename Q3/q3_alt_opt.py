# only check till squared root of num, deduce the rest

import os
import time

print("Running", os.path.basename(__file__))

prime_list = []


def get_largest(num, prime_check=False):
    sqrt = int(num ** 0.5)
    for i in range(2, sqrt):
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
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
