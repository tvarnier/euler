"""
https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

def sum_diagonals_spiral(dim):
    i = 0
    current = 1
    sum = 1
    add = 0

    while current != dim * dim:
        if i % 4 == 0:
            add += 2
        current += add
        sum += current
        i += 1

    return sum

if __name__ == "__main__":
    print(sum_diagonals_spiral(1001))