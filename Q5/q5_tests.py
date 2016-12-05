def div_by(num, r):
    for i in range(2, r + 1):
        if num % i != 0:
            return False
    return True


print(div_by(2525, 10))
