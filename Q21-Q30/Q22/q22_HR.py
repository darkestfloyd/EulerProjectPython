# Score 100

names = []

N = int(input().strip())
for counter in range(N):
    names.append(input().strip())

names.sort()

Q = int(input().strip())
for counter in range(Q):
    name = input().strip()
    index = names.index(name) + 1

    name_sum = 0
    for ch in name:
        name_sum += (ord(ch) - 64)
    print(index * name_sum)
