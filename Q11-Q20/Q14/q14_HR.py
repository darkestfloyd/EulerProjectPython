# new logic:
# use array not map(faster)
# pre-compute longest for all values under 5x10^6 + 1
# read input, print length from pre-computer array
# and no recursion!

collatz_sequence_length = [-1] * (3 * int(5e6) + 1)
total_length = [0] * int(5e6)


def get_collatz_length(cn):
    length = 0
    while collatz_sequence_length[cn] != 1:
        length += 1
        if cn % 2 == 0:
            cn //= 2
        else:
            cn = (3 * cn) + 1
    collatz_sequence_length[cn] = length
    return length


def generate_lengths():
    for human_n in range(2, 10):
        n = human_n - 1
        start = total_length[n - 1]
        nmax = nval = 0
        for n2 in range(start, n + 1):
            print(get_collatz_length(n2))
            pass
    return


collatz_sequence_length[0] = total_length[0] = 1
generate_lengths()
t = int(input().strip())
for counter in range(t):
    tc = int(input().strip())
