collatz_length_for_n = {16: 5}
largest_collatz_length = {1: 1}


def collatz_length(n):
    length = 0
    while n != 1:
        if n in collatz_length_for_n:
            return collatz_length_for_n[n] + length
        length += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n) + 1
    return length + 1


def get_largest(upper):
    lower = largest_collatz_length[upper - 1]
    nmax = 0
    nval = 0
    for i in range(lower, upper + 1):
        test_num = collatz_length(i)
        if test_num >= nmax:
            nmax = test_num
            nval = i
    largest_collatz_length[upper] = nval
    return 0


# print(collatz_length(3))
for x in range(2, int(5e6)):
    if x % 1000 == 0:
        print(x / int(5e6) * 100)
    get_largest(x)

file = open("q14_generated.py", 'a+')

file.write('largest_collatz_length = {')
for l in range(1, max(largest_collatz_length) + 1):
    file.write(str(l) + ":" + str(largest_collatz_length[l]) + ", ")

file.write('}')

file.write("\n\n")
file.write("t = int(input().strip())\n")
file.write("for counter in range(t):\n")
file.write("    tt = int(input().strip())\n")
file.write("    print(largest_collatz_length[tt])\n\n")

file.close()
