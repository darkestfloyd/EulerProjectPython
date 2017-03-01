t = int(input().strip())

for _ in range(t):
    d = int(input().strip())

    r_max, r_n = 0, 0
    for num in range(4, d):
        reminders, l = [-1] * num, 1
        r = 10 % num
        reminders[1] = r
        while reminders[r] == -1 and l < num:
            n = (r * 10) % num
            if n == 0:
                l = 0
                break
            reminders[r] = n
            r = n
            l += 1
        if l > r_max:
            r_max, r_n = l, num

    print(r_n)
