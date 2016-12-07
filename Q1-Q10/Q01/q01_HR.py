# solution for HackerRank


def sum_for_multiplier(multiplier, range):
    max = (range - 1) // multiplier
    return (multiplier * max * (max + 1)) // 2


n = int(input().strip())
for counter in range(n):
    range = int(input().strip())
    print(sum_for_multiplier(3, range)
          + sum_for_multiplier(5, range)
          - sum_for_multiplier(15, range))
