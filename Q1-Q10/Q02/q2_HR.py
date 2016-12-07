def even_fib(num):
    Fn, Fnm6, Fnm3, sum = 0, 0, 2, 2
    while 1:
        Fn = (4 * Fnm3) + Fnm6
        if Fn > num:
            break
        Fnm6 = Fnm3
        Fnm3 = Fn
        sum += Fn
    print(sum)


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    even_fib(n)
