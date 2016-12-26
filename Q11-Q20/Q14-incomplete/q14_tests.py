r = 9663


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


collatz_sequence(int(5e6))
# for i in range(1, r + 1):
#     collatz_sequence(i)
