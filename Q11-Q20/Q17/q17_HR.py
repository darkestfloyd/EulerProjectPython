# HR follows US English. No 'and' in words

_0_in_words = 'Zero'
_100_in_words = 'Hundred'
_1_to_19 = {
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
    19: 'Nineteen'}
tens_scale = {
    20: 'Twenty',
    30: 'Thirty',
    40: 'Forty',
    50: 'Fifty',
    60: 'Sixty',
    70: 'Seventy',
    80: 'Eighty',
    90: 'Ninety'}
numeric_scale = {
    4: 'Trillion',
    3: 'Billion',
    2: 'Million',
    1: 'Thousand'}


def in_words(n):
    """This function returns the given number in words (for n < 1000)"""
    words = []
    hundreds_digit = n // 100
    if hundreds_digit != 0:
        words.append(_1_to_19[hundreds_digit])
        words.append(_100_in_words)
        n %= 100
    if n == 0:  # for say 400
        return words
    if n < 20:  # for say 412
        words.append(_1_to_19[n])
        return words
    tens_digit = n // 10
    ones_digit = n % 10
    words.append(tens_scale[tens_digit * 10])
    if ones_digit == 0:  # for say 440
        return words
    words.append(_1_to_19[ones_digit])
    return words


def run(n):
    # Split into groups of 3
    n_in_words = []
    grouped_n = format(n, ',').split(',')
    scale_counter = len(grouped_n)  # for adding scale
    for group in grouped_n:
        group = int(group)
        scale_counter -= 1
        if group == 0:
            continue
        n_in_words.extend(in_words(group))
        if scale_counter > 0:
            n_in_words.append(numeric_scale[scale_counter])
    print(*n_in_words)
    return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    run(n)
