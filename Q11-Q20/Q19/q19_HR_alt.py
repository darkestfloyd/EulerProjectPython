# Score - 28.57

# Using Zeller's Congruency
# h = (q + (13 * (m + 1) / 5) + K + K // 4 + J //4 + 5 * J) mod 7
# where, h is the day of the week (0 - Sat)
#        q is day of month
#        m is the month (3 - March ..., 13 - Jan, 14 - Feb)
#        K is the year of century (yr mod 100)
#    and J is yr // 100


def run(date_start=1, month_start=1, year_start=1901, date_end=1, month_end=1, year_end=2000):
    sundays = 0
    for yr in range(year_start, year_end + 1):
        # print()
        if yr == year_start:
            months = range(month_start, 13)
        elif yr == year_end:
            months = range(1, month_end)
        else:
            months = range(1, 13)
        months = [13 if x == 1 else x for x in months]
        months = [14 if x == 2 else x for x in months]

        for month in months:
            if yr == year_start and month == month_start and date_start != 1:
                continue
            if yr == year_end and month == month_end and date_end <= 1:
                continue
            x1 = (13 * (month + 1)) // 5
            K = yr % 100
            J = yr // 100

            h = (1 + x1 + K + K // 4 + J // 4 + 5 * J) % 7
            if h == 1:
                # print(month, yr)
                sundays += 1

    print(sundays)
    return


t = int(input().strip())
for counter in range(t):
    yrs, ms, ds = input().strip().split(' ')
    yre, me, de = input().strip().split(' ')
    yrs, ms, ds = [int(yrs), int(ms), int(ds)]
    yre, me, de = [int(yre), int(me), int(de)]
    run(ds, ms, yrs, de, me, yre)
