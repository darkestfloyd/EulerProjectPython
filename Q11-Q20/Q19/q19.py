import os
import time

print("Running", os.path.basename(__file__))


def run(date_start=1, date_end=1, month_start=1, month_end=1, year_start=1901, year_end=2000):
    no_of_days = 0
    for yr in range(year_start, year_end + 1):
        if yr == year_start:
            months = range(month_start, 13)
        elif yr == year_end:
            months = range(1, month_end + 1)
        for month in months:
            print(month)

    # print(no_of_days)
    # print(no_of_days // 365)
    # print(no_of_days % 7)
    return


start_time = time.time()
run(1, 31, 6, 2, 1901, 1902)
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
