in_file = open("names.txt", 'r')

names = in_file \
    .read() \
    .replace('"', '') \
    .split(",")

print(names[1])
