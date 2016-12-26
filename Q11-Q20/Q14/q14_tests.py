r = 10
collatz_array = [-1] * 2 * r


def collatz_sequence(n):
    while True:
        if n == 1:
            print(n)
            return
        print(n, end=" -> ")
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n) + 1


collatz_array[0] = 1
for i in range(1, r):
    collatz_sequence(i)
