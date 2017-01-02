# score - 100

def run(n):
    print(sum([int(x) for x in str(2 ** n)]))
    return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
