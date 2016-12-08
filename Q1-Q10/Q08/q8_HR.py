import functools

t = int(input().strip())
for counter in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    print(max(functools.reduce(lambda x, y: x * y, [int(n) for n in num[i:i + k]]) for i in range(n)))
