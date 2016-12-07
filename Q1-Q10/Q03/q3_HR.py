def is_prime(num):
    sqrt = int(num ** 0.5) + 1
    if num % 2 == 0:
        return False
    for i in range(3, sqrt, 2):
        if num % i == 0:
            return False
    return True


def run(num):
    # sqrt = int(num ** 0.5) + 1
    prime_list = [2]
    nmax = num // 2 + 1
    for i in range(3, nmax):
        if num % i == 0 and i not in prime_list and is_prime(i):
            prime_list.append(i)
    if len(prime_list) == 1:
        prime_list.append(num)
    print(max(prime_list))
    return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
