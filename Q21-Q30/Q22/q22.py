# answer - 871198282

in_file = open("names.txt", 'r')

names = in_file \
    .read() \
    .replace('"', '') \
    .split(",")

# Algo -
# First merge sort the names
# Then convert to number and multiply by the index

names.sort()  # sort the names

name_score = 0
index = 1
for name in names:
    name_sum = 0
    for ch in name:
        name_sum += (ord(ch) - 64)
    name_score += name_sum * index
    index += 1

print(name_score)
