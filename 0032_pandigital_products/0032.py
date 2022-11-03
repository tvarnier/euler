"""
https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import itertools
import numpy as np

if __name__ == '__main__':
    permutations = np.array(["".join(s) for s in list(itertools.permutations("123456789"))])
    
    products = set()

    for perm in permutations:
        for multiplicand_len in range(1, 7 + 1):
            for multiplier_len in range(1, 7 + 1 - multiplicand_len):
                if int(perm[:multiplicand_len]) * int(perm[multiplicand_len:(multiplicand_len+multiplier_len)]) == int(perm[(multiplicand_len + multiplier_len):]):
                    products.add(int(perm[(multiplicand_len + multiplier_len):]))

    print(sum(products))