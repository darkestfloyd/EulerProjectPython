# answer - 76576500

import os
import time

print("Running", os.path.basename(__file__))


def run(count=500):
    n = 7
    while True:
        n += 1
        divisors = 0
        triangle_number = n * (n + 1) // 2
        sqrt = int(triangle_number ** 0.5)
        for i in range(1, sqrt + 1):
            if triangle_number % i == 0:
                divisors += 2
        if sqrt ** 2 == triangle_number:
            divisors -= 1
        if divisors > count:
            print(n, triangle_number)
            return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
