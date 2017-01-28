in_file = open("names.txt", 'r')

names = in_file \
    .read() \
    .replace('"', '') \
    .split(",")

# Algo -
# First merge sort the names
# Then convert to number and multiply by the index
