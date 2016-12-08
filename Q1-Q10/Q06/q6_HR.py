def run(num=100):
    sum_of_squares = (num * (num + 1) * ((2 * num) + 1)) // 6
    square_of_sums = (num * (num + 1) * 0.5) ** 2
    print(int(square_of_sums - sum_of_squares))
    return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
