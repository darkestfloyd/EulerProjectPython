import os
import time

print("Running", os.path.basename(__file__))


def palindrome_check(num):
    return num[::-1] == num


def run(nmax=999, nmin=100):
    largest = 0
    for i in range(nmax + 1, nmin, -1):
        for j in range(nmax + 1, i, -1):
            prod = i * j
            if palindrome_check(str(prod)):
                if prod > largest:
                    largest = prod
    return largest, i, j


start_time = time.time()
print(run())
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
