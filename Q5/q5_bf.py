import os
import time

print("Running", os.path.basename(__file__))


def div_by(num, max):
    for i in range(2, max + 1):
        if num % i != 0:
            return False
    return True


def run(nmax=20):
    test_num = nmax + 1
    while True:
        if div_by(test_num, nmax):
            return test_num
        else:
            test_num += 1


start_time = time.time()
print(run())
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
