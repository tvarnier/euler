"""

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def get_limit(exp):
    i = 0
    sum = 0
    while i < len(str(sum)):
        sum += (9 ** exp)
        i += 1
    return sum

def get_sum(n, exp):
    sum = 0
    while (n != 0):
        sum += ((n % 10) ** exp)
        n = n // 10
    return sum

def sum_digits_exp(exp):
    sum = 0
    
    for i in range(2, get_limit(exp)):
        if i == get_sum(i, exp):
            sum += i
    return sum

if __name__ == '__main__':
    print(sum_digits_exp(5))