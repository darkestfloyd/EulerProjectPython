# Using Zeller's Congruency

t = int(input().strip())
for counter in range(t):
    yrs, ms, ds = input().strip().split(' ')
    yre, me, de = input().strip().split(' ')
    yrs, ms, ds = [int(yrs), int(ms), int(ds)]
    yre, me, de = [int(yre), int(me), int(de)]
    # run(ds, ms, yrs, de, me, yre)
