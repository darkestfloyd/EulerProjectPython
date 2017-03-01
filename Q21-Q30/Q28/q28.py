# answer - 669171001

n = 1001
N = 2 * (n - 1) + 1

steps = 1
_sum = 1
_n = 1
count = 1

while count < N:
    f = 2 * _n + 1
    _sum += f
    if count % 4 == 0:
        steps += 1
    _n += steps
    count += 1

print(_sum)
