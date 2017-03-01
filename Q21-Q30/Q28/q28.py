# answer - 669171001

n = 1001
_sum = 1

for x in range(1, ((n - 1) // 2) + 1):
    _sum += 4 * (2 * x + 1) ** 2 - 12 * x

print(_sum)
