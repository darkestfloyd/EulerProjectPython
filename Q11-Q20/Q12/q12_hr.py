def run(count):
    n = 1
    while True:
        n += 1
        divisors = 0
        triangle_number = n * (n + 1) // 2
        sqrt = int(triangle_number ** 0.5)
        for i in range(1, sqrt + 1):
            if triangle_number % i == 0:
                divisors += 2
        if sqrt ** 2 == triangle_number:
            divisors -= 1
        if divisors > count:
            print(triangle_number)
            return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
