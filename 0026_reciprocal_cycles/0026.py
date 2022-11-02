"""
https://projecteuler.net/problem=26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

"""
A fraction in lowest terms with a prime denominator other than 2 or 5 (i.e. coprime to 10) always produces a repeating decimal. The length of the repetend (period of the repeating decimal segment) of 1/p is equal to the order of 10 modulo p.
"""

def repetend_length(denominator):
    k = 0

    while (10 ** k) % denominator != 1 or k == 0:
        k += 1

    return k

if __name__ == '__main__':
    max_repetend = (0, 0)
    for denominator in range (2, 1000):
        if denominator % 2 != 0 and denominator % 5 != 0:
            length = repetend_length(denominator)
            if length > max_repetend[1]:
                max_repetend = (denominator, length)

    print(max_repetend)
