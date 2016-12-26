import os
import time

print("Running", os.path.basename(__file__))

collatz_length = {1: 1}


def get_collatz_length(n):
    return 1


def run(limit=1e6):
    nmax = 0
    for n in range(int(limit)):
        test_num = get_collatz_length(n)
        if test_num > nmax:
            nmax = test_num
    print(nmax)
    return


start_time = time.time()
run(3)
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
