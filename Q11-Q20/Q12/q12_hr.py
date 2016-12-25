prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
              349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
              467, 479, 487, 491, 499, 503, 509, 521, 523, 541]


def run(count):
    n = 0
    while True:
        n += 1
        divisors = {}
        triangle_number = n * (n + 1) // 2
        for i in prime_list:
            if i > triangle_number + 1:
                break
            divisor_count = 0
            temp = triangle_number
            while temp % i == 0 and temp != 1:
                divisor_count += 1
                divisors[i] = divisor_count
                temp /= i
        total_divisors = 1
        for divisor in divisors:
            total_divisors *= (divisors[divisor] + 1)
        if total_divisors > count:
            print(triangle_number)
            return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
