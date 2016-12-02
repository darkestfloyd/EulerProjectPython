import os
import time

print("Running", os.path.basename(__file__))


def run():
    Fn, Fnm6, Fnm3, sum = 0, 0, 2, 2
    while 1:
        Fn = (4 * Fnm3) + Fnm6
        if Fn > 4000000000:
            break
        Fnm6 = Fnm3
        Fnm3 = Fn
        sum += Fn
    print(sum)
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
