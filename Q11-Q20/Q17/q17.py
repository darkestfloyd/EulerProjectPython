import os
import time

print("Running", os.path.basename(__file__))
alphabets = {0: 'Zero',
             1: 'One',
             2: 'Two',
             3: 'Three',
             4: 'Four',
             5: 'Five',
             6: 'Six',
             7: 'Seven',
             8: 'Eight',
             9: 'Nine',
             10: 'Ten',
             11: 'Eleven',
             12: 'Twelve',
             13: 'Thirteen',
             14: 'Fourteen',
             15: 'Fifteen',
             16: 'Sixteen',
             17: 'Seventeen',
             18: 'Eighteen',
             19: 'Nineteen',
             20: 'Twenty',
             30: 'Thirty',
             40: 'Forty',
             50: 'Fifty',
             60: 'Sixty',
             70: 'Seventy',
             80: 'Eighty',
             90: 'Ninety',
             100: 'Hundred',
             1000: 'Thousand'}


def get_length(n):
    n_in_words = []
    length = 0
    for i in range(4):
        if i == 0:
            teen = n % 20  # always under 19 FIX!
            if 10 < teen < 20:
                n_in_words.append(alphabets[teen])
                n_in_words.append('hundred and')
                length += len(alphabets[teen]) + 10
                n //= 100
                i += 1
            continue
        digit = n % 10
        if digit != 0:
            n_in_words.append(alphabets[digit])
            length += len(alphabets[digit])
        n //= 10
        if n == 1:
            n_in_words.append('hundred and')
            length += 10
        if n == 3:
            n_in_words.append('thousand')
            length += 8
    return length, n_in_words


def run(n=1000):
    sum_of_digits = 0
    for i in range(1, n + 1):
        sum_of_digits += get_length(i)
    print(sum_of_digits)
    return


start_time = time.time()
# run(5)
print(get_length(999))
end_time = time.time()

print("Total time: ", (end_time - start_time), "sec")
