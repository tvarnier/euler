"""
https://projecteuler.net/problem=16

2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2¹⁰⁰⁰?
"""

def sum_digit_number(nbr):
    return sum([int(digit) for digit in str(nbr)])

if __name__ == '__main__':
    print(sum_digit_number(2 ** 1000))