# new logic:
# use array not map(faster)
# pre-compute longest for all values under 5x10^6 + 1
# read input, print length from pre-computer array
# and no recursion!

collatz_sequence_length = {}
total_length = [0] * (int(5e6) + 5)


def get_collatz_length(cn):
    if cn in collatz_sequence_length:
        return collatz_sequence_length[cn]
    length = 0
    cn2 = cn
    while collatz_sequence_length[cn2] == -1:
        length += 1
        if cn2 % 2 == 0:
            cn2 //= 2
        else:
            cn2 = (3 * cn2) + 1
    collatz_sequence_length[cn] = length + collatz_sequence_length[cn2]
    return collatz_sequence_length[cn]


def generate_lengths():
    for n in range(2, int(5e6)):
        start = total_length[n - 1]
        nmax = nval = 0
        for n2 in range(start, n + 1):
            len_n2 = get_collatz_length(n2)
            if len_n2 >= nmax:
                nmax = len_n2
                nval = n2
        total_length[n] = nval
    return


collatz_sequence_length[0] = total_length[0] = -99
collatz_sequence_length[1] = total_length[1] = 1
generate_lengths()
print("done!")
t = int(input().strip())
for counter in range(t):
    tc = int(input().strip())
