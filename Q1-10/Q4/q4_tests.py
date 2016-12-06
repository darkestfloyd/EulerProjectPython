# palindrome check
num = str(10001)
print(num[::-1] == num)

for i in range(105, 100, -1):
    for j in range(i, 100, -1):
        print(i, j)
    print()
