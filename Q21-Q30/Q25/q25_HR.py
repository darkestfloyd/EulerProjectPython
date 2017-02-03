# score - 66.67

F = [1, 1]

f, counter = 0, 2
while f < 10 ** 5000:
    f = F[counter - 1] + F[counter - 2]
    F.append(f)
    counter += 1

t = int(input().strip())
for counter in range(t):
    n, c = int(input().strip()), 1
    for x in F:
        if x > 10 ** (n - 1):
            print(c)
            break
        c += 1
