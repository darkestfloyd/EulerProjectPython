# answer - 2783915460

# Algo - 1. Get permutations of digits
#        2. Sort the permutations
#        3. print millionth permutation
import itertools

MAX = 1000000 - 1
element = list(next(itertools.islice(itertools.permutations(range(0, 10)), MAX, None)))

num, counter = 0, 0
for n in element[::-1]:
    num += (n * (10 ** counter))
    counter += 1

print(num)
