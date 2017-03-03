powers = set()

n_min, n_max = 2, 5
for a in range(n_min, n_max + 1):
    for b in range(n_min, n_max + 1):
        powers.add(pow(a, b))

print(sorted(powers))
