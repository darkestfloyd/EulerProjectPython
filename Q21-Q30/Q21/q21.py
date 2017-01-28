import os
import time

print("Running", os.path.basename(__file__))


def sum_of_d(n):
    nsum = 0
    sqrt = n ** 0.5
    for x in range(1, int(sqrt + 1)):
        if n % x == 0:
            nsum += n
    return nsum


def run(nmax=10000):
    amicable_sum = 0
    num_flag = [-1] * nmax
    for a in range(2, nmax):
        if num_flag[a] != -1:
            continue
        b = sum_of_d(a)
        num_flag[a] = b
        if a == sum_of_d(b):
            amicable_sum += (a + b)
            num_flag[b] = a
    print(amicable_sum)
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
