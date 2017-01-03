# answer - 648

import functools
import math
import os
import time

print("Running", os.path.basename(__file__))


def run(n=100):
    fact = str(math.factorial(n))
    print(
        functools.reduce(
            lambda x, y: x + y,
            [int(i) for i in fact]
        )
    )
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
