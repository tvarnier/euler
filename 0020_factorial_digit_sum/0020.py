"""
https://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial_digit_sum(nbr):
    n = 1
    for i in range(1, nbr + 1):
        n *= i
    return sum(int(x) for x in str(n))

if __name__ == "__main__":
    print(factorial_digit_sum(100))