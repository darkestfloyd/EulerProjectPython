import functools
import os
import time

print("Running", os.path.basename(__file__))


def run(count=500):
    n = 7
    while True:
        n += 1
        upper = n * (n + 1) // 2
        factors = set(functools.reduce(list.__add__,
                                       ([i, upper // i] for i in range(1, int(n ** 0.5) + 1))))
        print(n, len(factors))
        if len(factors) > count:
            print(upper)
            return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
