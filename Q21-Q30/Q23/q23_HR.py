# HR accepted! Score 100

from utils.Euler import sum_of_divisors

MAX = 100000
abundant_numbers = set()

for num in range(12, MAX + 1):
    if sum_of_divisors(num, True) > num:
        abundant_numbers.add(num)

t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    flag = False
    for a in abundant_numbers:
        if n - a in abundant_numbers:
            flag = True
            break
    if flag:
        print("YES")
    else:
        print("NO")
