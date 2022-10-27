"""
https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import math

if __name__ == '__main__':
    abundants = []
    for i in range(12, 28123):
        if i % 2 == 0 or i % 5 == 0:
            if i < sum([div for div in range(1, (i // 2) + 1) if not i % div]):
                abundants.append(i)
    
    l = len(abundants)

    sum_abundants = set()
    i = 0
    while i < l:
        j = i
        while j < l and abundants[i] + abundants[j] < 28123:
            sum_abundants.add(abundants[i] + abundants[j])
            j += 1
        i += 1
    
    res = 0
    for i in range(1, 28123):
        if i not in sum_abundants:
            res += i
    print(res)