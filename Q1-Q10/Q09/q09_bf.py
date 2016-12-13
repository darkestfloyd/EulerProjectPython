# answer - 31875000

import os
import time

print("Running", os.path.basename(__file__))


def run(n=1000):
    for a in range(1, n):
        for b in range(1, n):
            c = (a ** 2 + b ** 2) ** 0.5
            if a + b + c == n:
                print(a * b * c)
                return
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
