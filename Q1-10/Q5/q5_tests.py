def div_by(num, r):
    for ele in range(2, r + 1):
        if num % ele != 0:
            return False
    return True


for i in range(1000):
    div_by(2521, 10)
