prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
              349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
              467, 479, 487, 491, 499, 503, 509, 521, 523, 541]


def is_prime(num):
    sqrt = int(num ** 0.5) + 1
    for i in prime_list:
        if i > sqrt:
            return True
        if num % i == 0:
            return False
    return True


def get_next_prime(prev_prime):
    test_num = prev_prime + 2
    while True:
        if is_prime(test_num):
            return test_num
        else:
            test_num += 2


def run(length=10001):
    while len(prime_list) < length:
        prime_list.append(get_next_prime(prime_list[-1]))
    print(prime_list[length - 1])
    return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
