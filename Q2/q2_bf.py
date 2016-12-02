import os
import time

print("Running", os.path.basename(__file__))


def run():
    i1, i2, i3, sum = 1, 1, 0, 0
    while i2 < 4000000000:
        i3 = i2 + i1
        if i3 % 2 == 0:
            sum += i3
        i1 = i2
        i2 = i3
    print(sum)
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
