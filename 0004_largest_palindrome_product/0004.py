"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math

def largest_palindrome_product(max):
    res = 0
    for x in range(0, max):
        for y in range(0, max):
            if is_palindrome(x * y) and res < x * y:
                res = x * y
    return res

def is_palindrome(n):
    if n < 10:
        return True
    
    digits = int(math.log10(n))+1
    
    div1 = 10 ** digits
    div2 = 10

    while div1 > div2:
        if (n % div1) // (div1 / 10) != (n % div2) // (div2 / 10):
            return False
        div1 /= 10
        div2 *= 10
    
    return True

if __name__ == '__main__':
    print(largest_palindrome_product(999))