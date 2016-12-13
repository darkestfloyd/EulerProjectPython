import os
import time

print("Running", os.path.basename(__file__))


def run(n=1000):
    for a in range(1, n // 4):
        b = int((a ** 2 - (a - n) ** 2) / (2 * (a - n)))  # derived using a^2 + b^2 = N - a - b
        c = n - a - b
        if not (a < b < c):
            continue
        if a + b + c == n and a ** 2 + b ** 2 == c ** 2:
            print(a * b * c)
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
