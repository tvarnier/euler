"""
https://projecteuler.net/problem=27

Euler discovered the remarkable quadratic formula:
        n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| <= 1000
    
    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""


import math

def is_prime(n):
    n = abs(n)
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True

if __name__ == '__main__':
    max = (0, 0, 0)

    for a in range (-999, 1000):
        for b in range(0, 1001):
            # b must be a prime to get a prime with n = 0, n^2 + an + b = b 
            if is_prime(b):
                count = 0
                n = 0
                while is_prime(n**2 + a * n + b):
                    count += 1
                    n += 1
                if count > max[2]:
                    max = (a, b, count)
    print(max)
    print(max[0] * max[1])
