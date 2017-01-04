# score - 38.46

MAX = int(5e6)
collatz_length = [-1] * (MAX + 1)
collatz = [-1] * (MAX + 1)


def get_collatz_length(n):
    temp_n = n
    length = -1
    while True:
        length += 1
        if temp_n < MAX:
            if collatz_length[temp_n] != -1:
                collatz_length[n] = collatz_length[temp_n] + length
                return collatz_length[n]
            else:
                temp_n = collatz[temp_n]
        else:
            if temp_n % 2 == 0:
                temp_n //= 2
            else:
                temp_n = 3 * temp_n + 1


def run(limit=1000000):
    nmax = 0
    nval = 0
    try:
        for n in range(2, limit + 1):
            test_num = get_collatz_length(n)
            if test_num >= nmax:
                nmax = test_num
                nval = n
        print(nval)
    except Exception as e:
        print(e.args, n)
    return


for col in range(1, MAX):
    if col % 2 == 0:
        collatz[col] = col // 2
    else:
        collatz[col] = 3 * col + 1
collatz[1] = 1
collatz_length[1] = 0
get_collatz_length(int(5e6))

# t = int(input().strip())
# for counter in range(t):
#     tt = int(input().strip())
#     run(tt)
