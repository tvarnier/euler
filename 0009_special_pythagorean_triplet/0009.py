"""
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

def special_pythagorean_triplet(target):
    for b in range(2, target // 2):
        for a in range(1, b - 1):
            c = math.sqrt(b ** 2 + a ** 2)
            if a + b + c == target:
                return a * b * c

if __name__ == '__main__':
    print(special_pythagorean_triplet(1000))