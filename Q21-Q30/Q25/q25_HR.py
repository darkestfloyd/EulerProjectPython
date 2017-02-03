# score - 100

F = [1, 1]
F_digit = {0: 1}

f, counter, digit = 0, 2, 1
while f < 10 ** 20:
    f = F[counter - 1] + F[counter - 2]
    F.append(f)
    counter += 1
    if f > 10 ** digit:
        F_digit[digit] = counter
        digit += 1

t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    print(F_digit[n - 1])
