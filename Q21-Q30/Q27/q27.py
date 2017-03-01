def f(a, b, n):
    return n ** 2 + a * n + b


def is_prime(n):
    sqrt = int(abs(n) ** 0.5)
    if n % 2 == 0:
        return False
    steps = 2
    for t in range(3, sqrt + 1, steps):
        if n % t == 0:
            return False
    return True


n_a, n_b = 0, 0
max_prime = 0
for a in range(-999, 1000):
    if a == 0:
        continue
    for b in range(-1000, 1001):
        if b == 0:
            continue
        n = 0
        while is_prime(f(a, b, n)):
            n += 1
        if n > max_prime:
            max_prime = n
            n_a, n_b = a, b

print(n_a, n_b, n_a * n_b)
