r = 10
collatz_array = [-1] * 2 * r


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
    print(length)


collatz_array[0] = 1
for i in range(1, r + 1):
    collatz_sequence(i)
