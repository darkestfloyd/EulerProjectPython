def run(n):
    return


t = int(input().strip())
for counter in range(t):
    ys, ms, ds = input().strip().split(' ')
    ye, me, de = input().strip().split(' ')
    ys, ms, ds = [int(ys), int(ms), int(ds)]
    ye, me, de = [int(ye), int(me), int(de)]
    print(ys, ye)
