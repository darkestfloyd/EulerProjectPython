F = [1, 1]

f = 0
counter = 2
while f < 10 ** 2:
    f = F[counter - 1] + F[counter - 2]
    F.append(f)
    counter += 1

#
# t = int(input().strip())
# for counter in range(t):
#     n = int(input().strip())
