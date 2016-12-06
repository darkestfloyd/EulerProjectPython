import os
import time

print("Running", os.path.basename(__file__))

prime_list = [2]


def is_prime(num):
    sqrt = int(num ** 0.5) + 1
    for i in prime_list:
        if i > sqrt:
            return True
        if num % i == 0:
            return False
    return True


def run():
    prime_sum = 2
    for i in range(3, 2000000, 2):
        if is_prime(i):
            prime_sum += i
            prime_list.append(i)
    print(prime_sum)
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
