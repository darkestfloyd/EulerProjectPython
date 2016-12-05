# answer - 104743

import os
import time

print("Running", os.path.basename(__file__))


def is_prime(num):
    sqrt = int(num ** 0.5) + 1
    if num % 2 == 0:
        return False
    for i in range(3, sqrt, 2):
        if num % i == 0:
            return False
    return True


def get_next_prime(prev_prime):
    test_num = prev_prime + 1
    while True:
        if is_prime(test_num):
            return test_num
        else:
            test_num += 1


def run(length=10001):
    prime_list = [2]
    while len(prime_list) != length:
        prime_list.append(get_next_prime(prime_list[-1]))
    print(prime_list[-1])
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
