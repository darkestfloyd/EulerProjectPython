r = 9


def collatz_sequence(n):
    length = 0
    while True:
        length += 1
        if n == 1:
            print(n, end=" !! ")
            break
        print(n, end=" -> ")
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n) + 1
    print("\n", length)


collatz_sequence(r)
# for i in range(1, r + 1):
#     collatz_sequence(i)


c = [1, 4, 7, 4, 2, 5, 5, 2, 7, 8, 9]
tt = int(input().strip())
nmax = nval = 0
for i in range(1, tt + 1):
    if c[i] >= nmax:
        nmax, nval = c[i], i

print(nval)
