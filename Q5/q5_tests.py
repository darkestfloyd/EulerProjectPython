import time


def div_by_2(num, r):
    if all(num % n for n in range(2, r + 1)):
        return True
    return False


def div_by(num, r):
    for ele in range(2, r + 1):
        if num % ele != 0:
            return False
    return True


start_time = time.time()
for i in range(1000):
    div_by(2520, 10)

end_time = time.time()

print("Took", (end_time - start_time))

start_time = time.time()
for i in range(1000):
    div_by_2(2520, 10)

end_time = time.time()

print("Took", (end_time - start_time))
