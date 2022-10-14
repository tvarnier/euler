"""
https://projecteuler.net/problem=12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import math

from numpy import tri

def highly_divisible_triangular_number(nbr_divisors_target):
    triangle_number = 0
    i = 1
    while 1:
        triangle_number = triangle_number + i
        nbr_factor = sum(2 for div in range(1, round(math.sqrt(triangle_number) + 1)) if not triangle_number % div)
        if nbr_factor > nbr_divisors_target:
            return triangle_number
        i = i + 1

if __name__ == '__main__':
    print(highly_divisible_triangular_number(500))
