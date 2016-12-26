# new logic:
# use array not map(faster)
# pre-compute longest for all values under 5x10^6 + 1
# read input, print length from pre-computer array
# and no recursion!

t = int(input().strip())
for counter in range(t):
    tc = int(input().strip())
