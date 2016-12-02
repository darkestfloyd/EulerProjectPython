i1, i2, counter = 1, 1, 2
print("F1:", i1, "\nF2:", i2)
while i2 < 500:
    counter += 1
    i3 = i1 + i2
    i1 = i2
    i2 = i3
    print("F", counter, ": ", i3, sep='')
