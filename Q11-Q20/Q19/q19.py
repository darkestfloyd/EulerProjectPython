import os
import time

print("Running", os.path.basename(__file__))


def run(year_start=1901, year_end=2000):
    no_of_days = 0
    for yr in range(year_start, year_end + 1):
        if yr % 4 == 0 and (yr % 100 != 100 or yr % 400 == 0):
            no_of_days += 1
        no_of_days += 365

    print(no_of_days)
    print(no_of_days // 365)
    print(no_of_days % 7)
    return


start_time = time.time()
run()
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
