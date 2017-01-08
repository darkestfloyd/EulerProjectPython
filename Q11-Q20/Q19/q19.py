import os
import time

print("Running", os.path.basename(__file__))


def run(date_start=1, date_end=1, month_start=1, month_end=1, year_start=1901, year_end=2000):
    no_of_days = 0
    for yr in range(year_start, year_end + 1):
        months = []
        ys = ye = False
        if yr == year_start:
            ys = True
            months = range(month_start, 13)
        elif yr == year_end:
            ye = True
            months = range(1, month_end + 1)
        else:
            months = range(1, 13)
        for month in months:
            if ye and month == month_end:
                dmax = date_end
            else:
                if month in [3, 5, 8, 10]:
                    dmax = 30
                elif month == 2:
                    dmax = 29 if yr % 400 == 0 or (yr % 4 == 0 and yr % 100 != 0) else 28
                else:
                    dmax = 31

            if ys and month == month_start:
                days = range(date_start, dmax + 1)
            else:
                days = range(1, dmax + 1)

            for x in days:
                print(x, month, yr)
    # print(no_of_days)
    # print(no_of_days // 365)
    # print(no_of_days % 7)
    return


start_time = time.time()
run(12, 13, 12, 2, 1901, 1903)
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
