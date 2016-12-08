def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return int((a * b) / gcd(a, b))


def lcm_for_range(counter, multiple, nmax):
    if counter == nmax:
        return multiple
    else:
        return lcm_for_range(counter + 1, lcm(multiple, counter), nmax)


def run(nmax=20):
    # print(lcm_for_range(1, 1, nmax)) # this is a recursive alternative
    multiple = 1
    for i in range(2, nmax + 1):
        multiple = lcm(multiple, i)
    print(multiple)
    return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
