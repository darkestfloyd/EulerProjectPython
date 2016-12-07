# answer - 233168

import os
import time

print("Running", os.path.basename(__file__))

start_time = time.time()
numSum = 0
for i in range(1, 10000000):
    if i % 3 == 0 or i % 5 == 0:
        numSum += i

print(numSum)
end_time = time.time()

print("Brute force took", (end_time - start_time), "sec")
