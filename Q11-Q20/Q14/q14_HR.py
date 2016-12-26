collatz_length = {1: 1}


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


def gen_collatz_length():
    for i in range(1, 5000001):
        get_collatz_length(i)


gen_collatz_length()
print("done!")
t = int(input().strip())
for counter in range(t):
    tt = int(input().strip())
    nmax = nval = 0
    for nn in range(1, tt):
        if collatz_length[nn] >= nmax:
            nmax = collatz_length[nn]
            nval = nn
    print(nval)
