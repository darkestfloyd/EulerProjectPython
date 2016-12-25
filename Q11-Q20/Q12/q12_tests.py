import functools

dict = {2: 5, 3: 6}

prod = 1
print(functools.reduce(lambda a, b: a * b, [dict[x] for x in dict]))
