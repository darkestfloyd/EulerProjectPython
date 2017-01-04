MAX = 1000
collatz = [-1] * MAX
collatz_length = [-1] * MAX


def get_collatz_length(n):
    temp_n = n
    length = -1
    while True:
        length += 1
        if temp_n < MAX:
            if collatz_length[temp_n] != -1:
                collatz_length[n] = collatz_length[temp_n] + length
                return collatz_length[n]
            else:
                temp_n = collatz[temp_n]
        else:
            if temp_n % 2 == 0:
                temp_n //= 2
            else:
                temp_n = 3 * temp_n + 1


file = open("q14_generated.py", 'w')
file.close()

print("Generating collatz")
collatz[1] = 1
for i in range(2, MAX):
    if i % 2 == 0:
        collatz[i] = i // 2
    else:
        collatz[i] = 3 * i + 1
print("Done")

collatz_length[1] = 1
print("Generating lengths")
for i in range(2, MAX):
    collatz_length[i] = get_collatz_length(i)
print("Done")

file = open("q14_generated.py", 'a+')

print("Writing collatz")
file.write('collatz = [')
for l in range(len(collatz)):
    file.write(str(collatz[l]) + ', ')
file.write(']')
print("Done")

file.write("\n")

print("Writing lengths")
file.write('collatz_length = [')
for l in range(len(collatz_length)):
    file.write(str(collatz_length[l]) + ', ')
file.write(']')
print("Done")

file.write("\n\n")
file.write("t = int(input().strip())\n")
file.write("for counter in range(t):\n")
file.write("    tt = int(input().strip())\n")
file.write("    nmax = nval = 0\n")
file.write("    for xx in range(1, tt + 1):\n")
file.write("        if collatz_length[xx] >= nmax:\n")
file.write("            nmax, nval = collatz_length[xx], xx\n")
file.write("    print(nval)\n")

file.close()
