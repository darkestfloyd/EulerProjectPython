# Algorithm:
# 1. Get all abundant numbers
# 2. Add all to get sums and mark the corresponding array to being abundant sum
# 3. The left out are non-abundant, add them

MAX = 28123
abundant_array = [0] * MAX


def flip(position):
    position -= 1
    abundant_array[position] = 0 if abundant_array[position] else 1


def get_factor(n):
    return 1


def is_abundant(n):
    return True


flip(12)
for i in range(13, MAX):
    abundant_array[i] = 1 if is_abundant(i) else 0
