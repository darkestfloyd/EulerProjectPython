import os
import time

print("Running", os.path.basename(__file__))


def run(num=100):
    sum_of_squares = (num * (num + 1) * ((2 * num) + 1)) / 6
    square_of_sums = (num * (num + 1) * 0.5) ** 2
    print(int(square_of_sums - sum_of_squares))
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
