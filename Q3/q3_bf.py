# this is taking too long!

import os
import time

print("Running", os.path.basename(__file__))

prime_list = []


def is_prime(num):
    print("Prime check for", num)
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    return True


def get_largest(num):
    print("Checking for", num)
    largest = 1
    for i in range(2, num):
        if num % i == 0 and i not in prime_list and is_prime(i):
            prime_list.append(i)
            largest = i
    return largest


def run():
    print(get_largest(600851475143))
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
