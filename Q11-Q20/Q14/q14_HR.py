# new logic:
# use array not map(faster)
# pre-compute longest for all values under 5x10^6 + 1
# read input, print length from pre-computer array
# and no recursion!

collatz_array = [-1] * int(5e6)
length_array = [0] * int(5e6)


def generate_lengths():
    print("okay")
    return


collatz_array[0] = length_array[0] = 1
generate_lengths()
t = int(input().strip())
for counter in range(t):
    tc = int(input().strip())
