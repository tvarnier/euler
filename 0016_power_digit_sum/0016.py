def sum_digit_number(nbr):
    return sum([int(digit) for digit in str(nbr)])

if __name__ == '__main__':
    print(sum_digit_number(2 ** 1000))