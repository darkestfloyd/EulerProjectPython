collatz_length = {1: 0}


def get_collatz_length(n):
    if n in collatz_length:
        return collatz_length[n]
    else:
        if n % 2 == 0:
            length = get_collatz_length(n // 2)
        else:
            length = get_collatz_length((3 * n) + 1)
        collatz_length[n] = length + 1
        return collatz_length[n]


def run(limit=1000000):
    nmax = 0
    nval = 0
    for n in range(1, limit + 1):
        test_num = get_collatz_length(n)
        if test_num > nmax:
            nmax = test_num
            nval = n
    print(nval)
    return


t = int(input().strip())
for counter in range(t):
    tt = int(input().strip())
    run(tt)
