# using n(n+1)/2
import os
import time

print("Running", os.path.basename(__file__))


def sum_for_multiplier(multiplier, range):
    max = int((range - 1) / multiplier)
    return int(multiplier * max * (max + 1) * 0.5)


start_time = time.time()
range = 10000000
print(sum_for_multiplier(3, range)
      + sum_for_multiplier(5, range)
      - sum_for_multiplier(15, range))
end_time = time.time()

print("Alternative approach took", (end_time - start_time), "sec")
