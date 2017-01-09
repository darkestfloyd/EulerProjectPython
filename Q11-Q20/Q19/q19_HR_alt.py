# Using Zeller's Congruency
# h = (q + (13 * (m + 1) / 5) + K + K // 4 + J //4 + 5 * J) mod 7
# where, h is the day of the week (0 - Sat)
#        q is day of month
#        m is the month (3 - March ..., 13 - Jan, 14 - Feb)
#        K is the year of century (yr mod 100)
#    and J is yr // 100


def run(date_start=1, month_start=1, year_start=1901, date_end=1, month_end=1, year_end=2000):
    return


t = int(input().strip())
for counter in range(t):
    yrs, ms, ds = input().strip().split(' ')
    yre, me, de = input().strip().split(' ')
    yrs, ms, ds = [int(yrs), int(ms), int(ds)]
    yre, me, de = [int(yre), int(me), int(de)]
    # run(ds, ms, yrs, de, me, yre)
