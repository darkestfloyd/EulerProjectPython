# Sieve of Eratosthenes implementation

import os
import time

print("Running", os.path.basename(__file__))

primes = [1]


def run(num=2000000):
    primes = [1] * (num + 1)
    primes[0] = primes[1] = 0
    for i in range(1, num + 1):
        if primes[i] == 1:
            for j in range(i * 2, num + 1, i):
                primes[j] = 0
    prime_sum = 0
    for i in range(num + 1):
        if primes[i] == 1:
            prime_sum += i
    print(prime_sum)
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
